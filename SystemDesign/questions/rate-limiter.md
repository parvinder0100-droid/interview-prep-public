---
type: question_note
question: Rate Limiter
depth: partial
attempted: 2026-08-11 17:47-18:27 (~38 min)
---

# Rate Limiter

First System Design case study of the sprint. Cold draw, no reference material.

## Requirements — how the policy was derived

Opened by asserting a limit (3 req/min) with no scoping questions asked. Two
platform variants used to force the real axes out:

    A: internal payments API, 200 enterprise customers, 500 req/sec total
    B: public free-tier weather API, 2M signups, scrapers are the threat

Derived independently: limit is keyed on a **subject** (enterprise customer vs
individual signup) over a **window** (per-second vs per-day). Specific number is
config, not architecture.

Failure traces that produced the final policy:

- **Per-customer static limit alone** — set at 500/sec on a platform whose total
  capacity is 500/sec: 200 x 500 = 100,000 possible. Self-caught.
- **Global cap alone** — one customer at 500/sec starves the other 199.
  Reintroduces the abuse case the limiter exists to prevent.
- **Per-customer sized to fit (2/sec)** — safe when all 200 busy, but on a
  normal day with 3 busy customers wanting 100/sec each: serves 6, rejects 294,
  leaves 494 req/sec of capacity idle.
- **Pure dynamic admission ("allow if capacity free right now")** — first-come
  -first-served, so the aggressive customer wins the race. Same starvation as
  the global cap.

**Landed policy**: guaranteed minimum per customer + shared pool above it.
Derived, not recited.

## Architecture

- Placement: API gateway.
- Gateway is N instances behind an LB. Local per-gateway counters breach the
  limit by exactly N (10 gateways, limit 100 -> 1000 through).
- Shared store (Redis) for counters. Costs: network hop on every request's
  critical path, plus SPOF.
- **Redis down**: fail open. Standard answer. Standard rebuttal — Redis fails
  *under load*, which is exactly when the limiter is load-bearing, so the
  fallback disappears at the worst moment. Mitigation direction (parked, not
  built): local per-gateway fallback limit rather than pure open.

## Atomicity

Naive sequence `read -> check -> increment -> allow` is a non-atomic
read-modify-write. 10 gateways, counter at 99, limit 100: all 10 read 99, all
10 allow. 10 through where 1 should have been. Fix: `INCR` returns the new
value atomically — check the return, never read separately.

## Counting algorithms

- **Fixed window + TTL** — counter expires on the window boundary. Breaks: 100
  at 10:00:59 plus 100 at 10:01:01 = 200 in two seconds, both calendar windows
  individually legal. 2x the limit in any 60-second stretch.
- **Sub-buckets (sliding)** — count per bucket, sum the last N.
  - "Store last access time" was the first answer and is insufficient state: one
    timestamp cannot distinguish 100 requests in the last minute from 3.
  - Per-second buckets, platform B (2M users, 1000/hour): 3600 buckets/user =
    **7.2 billion counters**. Infeasible.
  - Minute buckets: 60/user = 120M. Feasible.
- **Residual error is bounded by bucket size.** Minute buckets, 1000/hour:
  1000 requests at 10:30:59 land in bucket[10:30]; at 11:30:00 the sum covers
  buckets 10:31..11:30 and drops bucket[10:30], so the counter reads 0 and
  another 1000 go through. 2000 in 59m01s. Same bug as the fixed-window
  boundary, one order of magnitude smaller.

## Open gaps (not covered — for the next pass)

- What the client actually receives on reject: 429, `Retry-After`, rate-limit
  headers, drop vs queue.
- Local per-gateway fallback for the Redis-down case (parked ~18:08).
- How limit rules are stored and distributed to gateway instances.
- **Policy and implementation are disconnected**: ~17 min produced a
  floor + shared-pool policy; the next ~20 min built counters that implement a
  flat per-customer limit. Nothing in the counting design grants a guaranteed
  floor or manages a shared pool. This is the first question a real interviewer
  would ask next.
