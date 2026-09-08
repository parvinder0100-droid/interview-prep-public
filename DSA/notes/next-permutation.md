---
type: note
problem: Next Permutation
topic: Arrays/Medium
updated: 2026-07-12
---

# Next Permutation

## Algorithm

1. Find the largest index `i` such that `arr[i] < arr[i+1]` (the pivot,
   scanning from the right — the suffix after `i` is guaranteed descending).
2. Find the largest index `j > i` such that `arr[j] > arr[i]` — since the
   suffix is descending, scanning it from the right finds the *smallest*
   element still greater than the pivot first.
3. Swap `arr[i]` and `arr[j]`.
4. Reverse the suffix `arr[i+1..end]` (equivalent to sorting it ascending,
   since it's already descending).

If no pivot exists (array fully descending), reverse the whole array —
same as sorting it, since it's already the maximum permutation and needs to
wrap to the minimum.

## Why "Smallest Greater" and Not "Any Greater"

The next permutation is the smallest permutation greater than the current
one. Swapping with the smallest-greater element minimizes the increase at
the pivot position; then reversing the suffix (making it ascending, the
smallest arrangement) minimizes everything after.

## Mistake Made

Initial approach found *a* greater permutation (swapped pivot with the
first smaller-than-it... — actually first candidate found, without the
"smallest greater" rule) but not the *next* one, and never reversed the
suffix. Verified wrong by checking: on `[1,3,5,4,2]`, initial answer
`[1,5,3,4,2]` skipped valid smaller permutations like `[1,4,...]`. Correct
answer: `[1,4,2,3,5]`.

## Complexity

O(n) time, O(1) space.
