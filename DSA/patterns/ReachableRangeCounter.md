---
type: pattern
pattern: ReachableRangeCounter
status: in-use
updated: 2026-08-12
---

# Reachable-Range Counter

When a scan carries one integer of state (an open-bracket count, a balance, a
budget) and some inputs are *ambiguous* — a wildcard that could push the state
several ways — the honest state is the **set of values still reachable**. The
pattern: prove that set is always a contiguous interval, then carry only its
two endpoints instead of the set.

## The Shape

1. Start from the singleton `[0, 0]`.
2. Each deterministic character shifts the whole interval (`+1`, `-1`).
3. Each ambiguous character replaces the interval with the union of its shifted
   copies. Because the shifts differ by 1 and the interval is contiguous, the
   copies overlap — the union is `[lo - 1, hi + 1]`, still contiguous.
4. Prune states that are permanently dead (a negative open-count can never
   recover, since a `)` already went unmatched). Pruning removes a *prefix*,
   which keeps the interval contiguous — hence `lo = max(lo, 0)`.
5. If the whole interval dies (`hi < 0`), fail immediately.
6. At the end, accept if the target value lies inside `[lo, hi]`.

O(n) time, O(1) space. The DP-over-(index, balance) formulation gives the same
answer in O(n²) and is worth naming as the fallback in an interview.

## Why It Is Not Just "Track Min and Max"

The compression is only legal because of step 3 and 4 — that every operation
maps a contiguous set to a contiguous set. Without that, `(lo, hi)` would admit
values the string cannot actually produce. The induction *is* the pattern; a
solution that states `lo`/`hi` updates without it is a memorized formula.

## Problems Using This Pattern

- Valid Parenthesis String (LC 678) — started 2026-08-12, parked with the
  representation and the contiguity induction complete, update rules and code
  still open. 20:38: all update rules + clamp + bail-out + accept condition
  derived (each needing escalation); code written but buggy, still open.
  **Closed 2026-08-13**: both defects fixed by the user, `")*"` built as the
  counterexample to the chained form, O(n)/O(n). The accept condition
  simplifies to `min == 0` alone — `min >= 0` is forced by the clamp and
  `max >= 0` by the bail-out, so `min <= 0 <= max` collapses to one test.

## Common Pitfalls

- Carrying the reachable set as an actual collection (or reaching for DP)
  before checking whether it is an interval.
- Forgetting the clamp — letting `lo` go negative silently readmits dead
  branches and accepts invalid strings.
- Checking only `hi >= 0` at the end instead of asking whether the *target*
  (0 for balanced brackets) is inside the surviving interval.
- **Chaining the clamp and the bail-out as `if (lo<0) lo=0; else if (hi<0)
  return false;`** — `hi<0` implies `lo<0`, so the bail-out is dead code and a
  lone `)` is accepted. The two checks are independent (2026-08-12).
- Reading `lo < 0` as "the input is invalid". It kills one assignment, not all
  of them; only `hi < 0` kills the string. Counterexample: `*)` reaches
  `lo = -1` and is valid.
