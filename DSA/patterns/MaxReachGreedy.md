---
type: pattern
pattern: MaxReachGreedy
status: in-use
updated: 2026-08-06
---

# MaxReachGreedy

## When This Pattern Applies

Array of per-index jump/reach lengths; question is reachability or min
steps to the end. Distinct from interval-scheduling greedy (MergeIntervals)
— no sorting, single left-to-right pass tracking a running best.

## Core Idea

Track the farthest index reachable so far (`maxReach`). At each index `i`,
if `i > maxReach`, the end is unreachable from here — fail. Otherwise
update `maxReach = max(maxReach, i + nums[i])`. Works because any two
paths that reach the same index collapse to one number: the larger
resulting reach always dominates the smaller (whatever the smaller reach
can do, the bigger one can too, plus more) — no need to branch or track
individual paths.

For min-jumps (not just reachability), add a second pointer: `boundary`
(current jump's limit) and `farthest` (best reach found within it).
Increment jump count and set `boundary = farthest` when the scan passes
`boundary`. O(n)/O(1) — a max-heap of all `i+nums[i]` values also gives a
correct answer (global max always dominated by an already-reachable
position's extension) but costs O(n log n) for no benefit.

## Problems Using This Pattern

- Jump Game (LC 55) — reachability only, single running max.
- Jump Game II (LC 45) — min jumps, boundary/farthest two-pointer (or a
  max-heap, correct but strictly worse complexity).

## Common Pitfalls

- Stating "why greedy works" as a restatement of the goal ("reach the end
  faster") instead of the dominance argument — doesn't actually justify
  why branching is unnecessary.
- Reaching for a heap/PQ out of habit for "track the best so far" — a
  heap is never wrong here (dominance still holds regardless of when an
  entry was added), just an unneeded O(log n) factor.
