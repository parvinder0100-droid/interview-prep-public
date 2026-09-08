---
type: mistake_journal
updated: 2026-08-11
---

# System Design Mistake Journal

Permanent log of every design mistake, gap, or missed trade-off. Never delete entries —
primary source for weakness detection in this track.

## Entry Format

```
### YYYY-MM-DD — Question/Concept
- Mistake:
- Root Cause:
- Correct Thinking:
- How to Avoid:
- Pattern (e.g. caching, sharding, consistency, queueing):
- Review Date:
```

## Log

### 2026-08-11 18:27 — Rate Limiter (requirements phase)
- Mistake: opened with a solution ("3 req/min, then drop"), asked the interviewer zero clarifying questions in the first ~2 min
- Root Cause: treated the one-line prompt as complete spec; no scoping habit
- Correct Thinking: subject + window + limit are derived from platform shape (200 enterprise vs 2M free-tier), not asserted
- How to Avoid: first move on any design prompt is questions, not a number
- Pattern: requirements gathering
- Class: code-vs-derivation
- Recurrence: 1
- Review Date: 2026-08-12

### 2026-08-11 18:27 — Rate Limiter (policy)
- Mistake: after tracing that per-customer-only and global-only each fail, answered "we can have limits per customer" — a design already shown broken
- Root Cause: failure reasons not retained between traces; each trace evaluated in isolation
- Correct Thinking: both constraints hold simultaneously — guaranteed floor per subject + shared pool above it
- How to Avoid: write each rejected option and *why* before proposing the next; don't re-propose from memory
- Pattern: fairness / resource allocation
- Class: invariant-why
- Recurrence: 1
- Review Date: 2026-08-12

### 2026-08-11 18:27 — Rate Limiter (sliding window state)
- Mistake: said "sliding window", then named the stored state as "last access time"
- Root Cause: pattern name recalled from Alex Xu (~2yr) without the underlying state; rusty recall
- Correct Thinking: one timestamp cannot distinguish 100 requests in the window from 3 — needs per-bucket counts (or the timestamps themselves)
- How to Avoid: never answer a design question with an algorithm name; state the data structure and what it costs in the same breath
- Pattern: sliding window / counting
- Class: stale-recall
- Recurrence: 1
- Review Date: 2026-08-12

### 2026-08-11 18:27 — Rate Limiter (bucket granularity)
- Mistake: could not identify the residual error in minute-buckets ~4 min after independently deriving the identical fixed-window boundary bug at second-scale ("I don't know what the problem would be"); needed a category pointer plus a full guided trace
- Root Cause: bug learned as a fact about fixed windows, not as a property of any coarse bucket
- Correct Thinking: coarse bucket = cannot see inside it = error bounded by bucket size, at every scale
- How to Avoid: after solving any bug, ask "what class of thing was that, and where else does it live?" before moving on
- Pattern: sliding window / counting
- Class: transfer-gap
- Recurrence: 2 (2nd transfer-gap; first was DSU-not-retrieved 2026-08-07, DSA)
- Review Date: 2026-08-12

### 2026-08-11 18:27 — Rate Limiter (session-wide pattern)
- Mistake: on 4 separate two-part questions, delivered the mechanism and silently dropped the cost/justification half — the local-counter breach number, the fail-open worst case, the minute-bucket tradeoff, the memory price of per-second buckets
- Root Cause: same shape as the logged Greedy justification signal — mechanics are cold-solid, "why / what does it cost" is not rehearsed
- Correct Thinking: in a design loop the tradeoff half is the scored half; the mechanism alone is par
- How to Avoid: answer every design claim in the form "X, which costs Y" — never state X alone
- Pattern: trade-off articulation
- Class: code-vs-derivation
- Recurrence: 3+ (cross-track — confirms the DSA Greedy/justification signal is not DSA-specific)
- Review Date: 2026-08-12
