---
type: note
problem: Frog Jump (DP-3)
topic: DP/1D DP
updated: 2026-07-11
---

# Frog Jump (DP-3)

## Intuition

`dp[i]` = min cost to reach stair `i`. Frog can jump from `i-1` or `i-2`, cost of a
jump = `|height[current] - height[from]|`. Take the cheaper of the two arrivals.

## Recurrence (1-indexed stairs, dp size n+1)

- `dp[1] = 0` (frog starts here)
- `dp[2] = dp[1] + |height[1]-height[0]|` (base case — two-jump term would need
  `dp[0]` and `height[-1]`, neither exists)
- `dp[i] = min(dp[i-1] + |height[i-1]-height[i-2]|, dp[i-2] + |height[i-1]-height[i-3]|)`
  for `i = 3..n`

## Mistakes Made (see mistake_journal.md for full entries)

1. 2026-07-10: first attempt was pure Fibonacci shape, ignored height/cost
   entirely — rust from 2-3 months no practice.
2. 2026-07-11: two-jump term initially reused the one-jump term's height diff
   (`height[i-1]-height[i-2]` twice) instead of `height[i-1]-height[i-3]`.
3. 2026-07-11: missed that `dp[2]` needs its own base case — the general
   recurrence breaks for `i=2` (references `dp[0]`/`height[-1]`).

## Complexity

- Unoptimized: O(n) time, O(n) space (dp array).
- Optimized: O(n) time, O(1) space — only `dp[i-1]` and `dp[i-2]` ever needed,
  replace array with two variables.

## Edge Cases

- n=1: only stair 1 exists, loop never runs, `dp[1]=0` is the answer directly.
- n=2: must hit the `dp[2]` base case, not the general recurrence.


---

## Closure, 2026-08-28 (7 weeks after the entry above)

All three follow-ups from 07-10 answered, O(1)-space version Accepted. Closing
them exposed **two defects in code that had been recorded as solved**:

1. **Out of bounds at `i=1`.** The recurrence was carried in its general form,
   `dp[i] = min(dp[i-1]+|h[i]-h[i-1]|, dp[i-2]+|h[i]-h[i-2]|)`, with the loop
   starting at `i=1`. `dp[-1]` throws on every input with `n>=2`, which means
   the 07-10/07-11 "corrected recurrence" had never been submitted to a judge.
   Fix: peel — `dp[1] = |h[1]-h[0]|`, loop from `i=2`.

2. **Wrong roll in the O(1) version.** `backbytwo = oneStep`, where
   `oneStep = dp[i-1] + |h[i]-h[i-1]|` — a dp value **plus a jump cost**, in the
   slot that must hold `dp[i-2]`. Every later `twoStep` inherited the inflation.
   `[0,10,100,10]` returns 100 instead of 10. Invisible for `n<=3`, because the
   loop returns `backbyone` before the corrupted slot is ever read.

   Correct roll, order mandatory:

       backbytwo = backbyone;   // old dp[i-1]
       backbyone = cur;

The unlock for (2) was naming the invariant first — "at the top of iteration
`i`, `backbyone = dp[i-1]` and `backbytwo = dp[i-2]`" — after which the user
found the defect in one step. Same prescription as 08-25's shrink-guard bug.

Complexity, all stated cold: O(n) time (one pass, O(1) work per iteration),
O(n) space for the array version, O(1) rolled.
