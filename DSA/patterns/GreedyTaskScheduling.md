---
type: pattern
pattern: Greedy Task Scheduling (frequency-first with cooldown)
status: in-use
updated: 2026-08-04
---

# Greedy Task Scheduling

## When This Pattern Applies

Scheduling repeated items under a separation/cooldown constraint, minimizing
total elapsed time (or counting idle slots).

## Core Idea

Among the items currently *available*, always run the one with the highest
remaining count. The highest-frequency item fixes the schedule's skeleton —
`maxFreq-1` gaps that everything else fills — so delaying it delays the whole
chain. A heap ordered by remaining frequency plus a cooldown queue implements
this; with a bounded alphabet the heap is constant-sized, giving `O(N)` time
and `O(1)` space.

Closed form, no heap needed:

    max( (maxFreq - 1) * (n + 1) + countMax ,  totalTasks )

`maxFreq-1` full blocks of width `n+1` (item + its gap), plus one slot per
item tied at max frequency. The `totalTasks` term takes over once there are
enough distinct items to fill every idle slot.

## Problems Using This Pattern

- Task Scheduler (LC 621) — 2026-08-02, approach only, code not written.

## Common Pitfalls

- Ordering the heap by availability time and breaking ties arbitrarily (or by
  label). Ties must break on remaining frequency, descending.
- Re-push offset `current + n` instead of `current + n + 1` — `n` counts the
  empty slots *between* runs. Test `[A,A]`, `n=2`: answer 4, off-by-one gives 3.
- Quoting the closed form without the `max(..., totalTasks)` guard.
- Formula decays fast if only verified against a traced example — restate
  what each term counts, in words, right after deriving it (2 occurrences
  on Task Scheduler already, 2026-08-02 and 2026-08-04).
