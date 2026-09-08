---
type: pattern
pattern: NextPermutation
updated: 2026-07-20
status: in-use
---

# NextPermutation

## When This Pattern Applies

"Give the next lexicographically greater arrangement" problems on arrays/sequences.

## Core Idea

Three-step decomposition: (1) find pivot = largest index `i` where
`arr[i]<arr[i+1]` (suffix from `i+1` is non-increasing); (2) find swap partner
= rightmost `j>i` where `arr[j]` is STRICTLY greater than `arr[i]` (scanning
from the right finds the smallest-greater element first, since the suffix is
descending); (3) swap `i,j`, then reverse the suffix `[i+1..end]`. If no pivot
exists, the array is the last permutation — reverse the whole array.

## Problems Using This Pattern

- Next Permutation — Arrays/Medium — solved 2026-07-12 with full derivation
  (genuine new-material gap at the time).

## Common Pitfalls

- Misidentifying the pivot index — picking the larger-value index instead of
  the correct `i` where `arr[i]<arr[i+1]` (repeat rust, review #2, 2026-07-17).
- Swap-partner condition stated as `>=` instead of strictly `>` — breaks on
  duplicates (e.g. `[1,2,1]` would wrongly become `[1,1,2]` instead of
  `[2,1,1]`); an equal-value swap is a no-op and doesn't advance to the next
  permutation (same review #2 regression).
- Two independent hard-to-retain pieces (pivot rule + swap-partner rule) —
  rehearse both explicitly, "I remember the general shape" isn't enough.
