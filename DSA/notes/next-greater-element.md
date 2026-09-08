---
type: note
problem: Next Greater Element
topic: Stack/Queue
updated: 2026-07-20
---

# Next Greater Element

## Intuition

Traverse right to left, maintain a monotonic-decreasing stack of *candidate*
values. For each index: pop everything ≤ current (they can never be the
answer for anything further left), whatever remains on top is the answer (or
-1 if empty), then push current.

## Mistake Made

First code attempt overwrote `nums[i]` with the computed answer before
pushing — pushed the answer onto the stack instead of the original value,
corrupting later comparisons. Fixed with a separate output array (`nge[]`),
stack only ever holds original values.

## Complexity

Amortized O(n) time (each element pushed/popped at most once across the
whole run, not per-i), O(n) space (stack + output).
