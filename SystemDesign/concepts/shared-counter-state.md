---
type: concept
status: covered
first_covered: 2026-08-11
---

# Shared Counter State Across N Stateless Instances

Derived 2026-08-11 during [Rate Limiter](../questions/rate-limiter.md).
Reusable well beyond rate limiting — applies to any quota, budget, or
sequence counter read by a horizontally-scaled tier.

## Local counters multiply the limit by N

N instances behind a load balancer, each enforcing limit L against its own
local counter, admit **N x L**. Not an approximation — exactly N times, if the
LB spreads evenly. 10 gateways, limit 100 -> 1000 through.

## Read-modify-write is a lost update

`read -> check -> increment -> allow` is not atomic. Counter at 99, limit 100,
10 instances receive a request simultaneously: all 10 read 99, all 10 see room,
all 10 admit. Fix: an atomic operation that returns the new value (`INCR`) and
check the *return*, never a separate read. Multi-step logic (increment + set
expiry, or conditional admit) needs a Lua script or equivalent to stay atomic.

## Cost of centralizing

A shared store puts a network hop on the critical path of every request, and
makes the store a SPOF for the entire tier.

## Fail-open vs fail-closed

When the store is unreachable:
- **Fail open** (admit) — the standard answer; rejecting all traffic because
  the *limiter* is down is worse than over-serving.
- **The standard rebuttal**: the store tends to fail *under load*, which is
  exactly when the limiter is load-bearing. The fallback vanishes at the worst
  possible moment — the failure is correlated, not random.
- **Stronger answer**: fail open *to a conservative local limit*, not to
  unlimited. Degrades precision instead of abandoning protection.

Say the rebuttal unprompted in an interview — "fail open" alone is par.
