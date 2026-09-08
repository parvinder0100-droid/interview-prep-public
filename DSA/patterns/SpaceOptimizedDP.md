---
type: pattern
pattern: SpaceOptimizedDP
updated: 2026-08-28
status: in-use
---

# Space-Optimized DP (rolling variables)

## When This Pattern Applies

A 1D DP whose recurrence reads only a fixed window back (`dp[i-1]`, `dp[i-2]`,
...). The array can be replaced by that many scalars, dropping O(n) space to
O(1).

## Core Idea

State the invariant **before** writing the loop:

    at the top of iteration i:  backbyone = dp[i-1],  backbytwo = dp[i-2]

Then the roll is forced, and its order is forced with it:

    backbytwo = backbyone;   // old dp[i-1] -- must come first
    backbyone = cur;

## Problems Using This Pattern

- Frog Jump (DP-3) — 2026-08-28 — O(n) -> O(1), both pitfalls below hit live

## Common Pitfalls

- **Rolling off a computed candidate instead of a dp value.** `oneStep =
  dp[i-1] + cost` is a dp value *plus a jump cost*; assigning it to the
  `dp[i-2]` slot inflates every later comparison. Check each assignment against
  the invariant, not against what happens to be in scope.
- **The bug is invisible on small n.** With a 2-back window, n<=3 never reads
  the corrupted slot. Always test n>=4 — `h=[0,10,100,10]` returns 100 instead
  of 10.
- **Peel the base iterations.** A `dp[i-2]` recurrence cannot run at `i=1`;
  set `dp[1]` explicitly and start the loop at `i=2`. Evaluate the body at
  `i=k-1` before choosing the loop bound.
