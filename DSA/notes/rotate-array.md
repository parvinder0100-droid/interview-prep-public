---
type: note
problem: Rotate Array
topic: Arrays/Basics
updated: 2026-07-12
---

# Rotate Array (O(1) space)

## Intuition

Left-rotate by `k`: split into chunk `A=[0,k-1]` and `B=[k,n-1]`, want `B+A`
with each chunk's internal order preserved.

## Why the Reversal Trick Works

Reversing the whole array `A+B` gives `reverse(B)+reverse(A)` — swaps chunk
order AND flips each chunk's internal order. Only the swap is wanted, so
cancel the internal flip in advance: pre-reverse each chunk individually
first, giving `reverse(A)+reverse(B)`. Reversing *that* whole thing gives
`reverse(reverse(B))+reverse(reverse(A)) = B+A` — double reversal cancels,
leaving just the chunk swap with original internal order intact.

## Recipe

1. `k = k % n`
2. Reverse `arr[0..k-1]`
3. Reverse `arr[k..n-1]`
4. Reverse whole `arr[0..n-1]`

## Mistake Made

Fully stuck — no idea how to do it in O(1) space, needed the full
double-reversal derivation walked through concretely on `[1,2,3,4,5], k=2`
before it landed.

## Complexity

O(n) time, O(1) space.
