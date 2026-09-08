---
type: pattern
pattern: ReversalAlgorithm
updated: 2026-07-20
status: in-use
---

# ReversalAlgorithm

## When This Pattern Applies

O(1)-space array rotation — shift elements left/right by k without an extra array.

## Core Idea

Whole-array reverse of `A+B` gives `reverse(B)+reverse(A)` (swaps chunk order
AND flips each chunk's internal order). Pre-reversing each chunk individually
first cancels the unwanted internal flip, leaving just the chunk swap. Recipe:
reverse first chunk, reverse second chunk, reverse whole array. For a
right-rotation by k on an n-length array: first chunk = first `n-k` elements,
second chunk = last `k` elements (verify split direction with a concrete small
trace before trusting it — left/right rotation swaps which chunk is which size).

## Problems Using This Pattern

- Rotate Array — Arrays/Basics — solved 2026-07-12 with full derivation
  (genuine new-material gap at the time).

## Common Pitfalls

- Split-boundary direction: splitting at index `k` (first k, last n-k) instead
  of `n-k` (first n-k, last k) for right-rotation-by-k — confirmed as a repeat
  rust bug at review #2 (2026-07-17).
- Trusting the split boundary from memory instead of verifying with a small
  concrete trace first.
- The underlying "why" (double-reversal cancels chunk-internal flip while
  swapping chunk order) has never been independently derivable — 3 reviews
  in a row (07-13, 07-17, 07-21) recall the mechanical recipe fine but can't
  explain why it works unaided. Next review should test the derivation
  itself as the pass/fail bar, not the split boundary.
