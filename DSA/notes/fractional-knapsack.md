---
type: note
problem: Fractional Knapsack (GFG)
topic: Greedy
difficulty: Medium
updated: 2026-08-08
---

# Fractional Knapsack

https://www.geeksforgeeks.org/problems/fractional-knapsack-1/1

Solved 2026-08-08 23:24, approach only — code declined, still open.

## Why highest ratio first (the part that took 5 sessions)

Concrete swap that finally landed it:

    W = 10.  A: weight 6, value 60 (10 per unit).  B: weight 10, value 50 (5 per unit).
    Claimed-optimal packing: 2 units of A + 8 units of B  -> 20 + 40 = 60
    Swap 1 unit of B out for 1 unit of A: 3A + 7B         -> 30 + 35 = 65

Delta = +5 = ratio(A) − ratio(B). Weight is unchanged, so the swap stays
feasible. Generalized: any packing that holds a unit of a lower-ratio item
while a higher-ratio item still has weight left outside can be strictly
improved by one unit-swap, therefore it is not optimal. Only the
highest-ratio-first packing survives.

Note the failure mode this replaces: "we want the max value so we pick the
highest ratio" restates the objective and proves nothing. See
`../patterns/GreedyExchangeArgument.md`.

## Complexity

O(n log n) time, sort-dominated. Space **O(n)**, not O(log n): the items must
be sorted as objects/pairs (weight and value have to travel together), and
Java's `Arrays.sort` uses TimSort for object arrays — stable, O(n) auxiliary
buffer. The O(log n) answer describes the *primitive* branch (dual-pivot
quicksort, in-place). The constructed `Item[]` is also O(n), so the two tie.

## Edge cases (all clean cold)

- W = 0: `while (remaining > 0 && i < n)` skips entirely, returns 0.
- Single item heavier than W (W=5, w10/v100): take the 0.5 fraction, return 50.
- All ratios equal, total weight > W: sort order irrelevant, answer = ratio × W.
- Total weight < W: loop ends on `i < n` (not on capacity), returns the sum of
  all values — this is what the `i < n` half of the guard is for.

## Open

Code not written. Live bug surfaces to watch when it is: comparator direction
(burned on Top K Frequent, 2026-08-01) and integer division when computing the
ratio and the final fraction.
