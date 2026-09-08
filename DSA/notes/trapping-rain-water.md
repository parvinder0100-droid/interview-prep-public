---
type: note
problem: Trapping Rain Water (LC 42)
status: SOLVED 2026-08-26 (with-hints:5)
---

# Trapping Rain Water (LC 42)

https://leetcode.com/problems/trapping-rain-water/

## Status

Solved 2026-08-26, ~30 min session. ~14 min on the boundary rule, ~6 min code
(cold, correct on first submit), rest on complexity/edge cases. O(n)/O(n).

## The rule

    level_i = min(maxLeft[i], maxRight[i])
    water_i = max(0, level_i - height[i])
    answer  = sum of water_i          # per column, width 1

`maxLeft[i]` / `maxRight[i]` are **exclusive** of `i` in the code written
(`left[i] = max(left[i-1], height[i-1])`), which is fine — `left[0] = 0` and
`right[n-1] = 0` make both endpoints clamp to 0.

## The thing that took 14 minutes: nearest vs tallest

The first three candidate rules were all "nearest something" — nearest smaller,
then nearest taller — retrieved off the Stack topic's `nsl/nsr` template rather
than derived. The discriminating instance:

    [3, 0, 1, 0, 2], index 3

    nearest taller each side  ->  min(1, 2) - 0 = 1     WRONG
    tallest each side         ->  min(3, 2) - 0 = 2     right

**Why tallest**: a shorter bar between `i` and the tall wall is itself submerged
to the same level, so it leaks nothing. Traced on `[3,1,0,2]`: index 1 (height
1) holds 1 unit, so its surface sits at 2 — the same level as index 2. The
surface is flat across the dip; the short bar is under water, not a wall.

## Clamp semantics

`cur < 0 ? 0 : cur` fires on every bar taller than the lower of its two walls —
both endpoints, and every local peak (`[1,5,1]` at index 1: `min(1,1)-5 = -4`).
Not just the endpoints, which was the first answer given.

## Edge cases

`n=0` -> 0 (loops don't run). `n=1`, e.g. `[5]` -> 0 (`left[0]=right[0]=0`,
clamped).

## Left open — next session opens here

O(1)-space two-pointer version. Not attempted, no hint given.

## Dead code in the submitted version

`int max = 0;` declared and never used — drop it.

## O(1)-space follow-up (2026-08-27)

Two pointers from both ends, one running max each.

    leftMax  = exact for l, lower bound for r
    rightMax = exact for r, lower bound for l

Branch on `leftMax < rightMax`: then `leftMax < rightMax <= trueRightMax`, so
`min(trueLeftMax, trueRightMax) = leftMax` **regardless of the unseen middle**.
Settle `l`, move `l`. Mirror otherwise. Ties fall either way — both maxima equal.

Updating the max *before* the subtraction guarantees `leftMax >= height[l]`, so
no clamp is needed (the array version needed one).

Derivation came cold across 5 questions; the code was requested rather than
attempted — see the assembly-gap entry in [[mistake_journal]] 2026-08-27.
