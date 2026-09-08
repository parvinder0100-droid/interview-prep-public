---
type: concept
status: covered
first_covered: 2026-08-11
---

# Rate Limiting Algorithms

Derived 2026-08-11 during [Rate Limiter](../questions/rate-limiter.md), not read.

## The one tradeoff

Every counting scheme trades **memory** against **precision**. The error is
bounded by how coarse your time granularity is. That single sentence generates
all of the below.

## Ladder

- **Fixed window + TTL** — one counter per subject, expires on the window
  boundary. Cheapest. Allows **2x the limit** across a boundary (100 at
  10:00:59 + 100 at 10:01:01).
- **Sub-bucket / sliding** — N counters per subject, sum the trailing N.
  Boundary error shrinks from window-size to bucket-size. Cost scales with
  N per subject: per-second buckets on a 1-hour window = 3600/user, which at
  2M users is 7.2B counters (infeasible); minute buckets = 60/user = 120M.
- **Exact timestamp log** — store the actual request times, count what's in
  the window. Zero error, worst memory. (Named here for completeness — not
  derived in session.)
- **Token bucket** — not covered 2026-08-11. Gap.

## Insufficient state (mistake worth remembering)

A single "last access time" per subject cannot enforce N-per-window: one
timestamp cannot distinguish 100 requests in the last minute from 3. Any
scheme needs either counts-per-bucket or the timestamps themselves.

## Where the limit is keyed

Two independent knobs, chosen from platform shape:
- **subject** — per API key / customer / user / IP / endpoint, or global
- **window** — per second / minute / hour / day

Per-subject alone doesn't protect aggregate capacity. Global alone starves
quiet subjects when one is aggressive. Real answer is layered: a guaranteed
floor per subject plus a shared pool above it.
