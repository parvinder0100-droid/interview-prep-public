---
type: note
problem: Kadane's Maximum Subarray Sum
topic: Arrays/Medium
updated: 2026-07-12
---

# Kadane's Maximum Subarray Sum

## Algorithm

```
sum = 0
max = -infinity
for x in arr:
    sum += x
    max = max(max, sum)
    if sum < 0: sum = 0
```

## Why Record Before Reset

Recording `max` using the sum that includes the current element, before the
reset check, means even a losing (negative) running sum gets a chance to be
captured as best-so-far. This is what makes it correct on all-negative
arrays — otherwise the reset throws away every negative sum before it's
ever compared.

## Mistake Made

Original approach only updated `max` when a reset was triggered, not every
iteration — silently broken on all-negative arrays (`[-3,-1,-2]` should
return `-1`, the least-negative single element, but a reset-only version
never captures it).

## Complexity

O(n) time, O(1) space.
