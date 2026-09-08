---
type: note
problem: Longest Subarray with Sum K
topic: Arrays/Easy
updated: 2026-07-12
---

# Longest Subarray with Sum K

## Two Regimes

- **Non-negative array**: variable-size sliding window works — sum grows
  monotonically as window expands, so shrink-when-sum>k is valid.
- **Negatives allowed**: sliding window breaks (sum isn't monotonic). Need
  prefix sum + hashmap instead.

## General Case (negatives allowed)

`sum(i+1..j) = prefixSum[j] - prefixSum[i]`. Want this `= k`, so
`prefixSum[i] = prefixSum[j] - k`.

Scan left to right, maintain `{prefixSum value -> earliest index}` map. At
each `j`: compute `prefixSum[j]`, look up `prefixSum[j]-k` in the map — if
found at index `i`, candidate length `j-i`, update max. Insert
`prefixSum[j]->j` only if not already present (earliest index maximizes
future lengths).

## Mistake Made

Defaulted to sliding window without checking for negatives. When pushed,
proposed a Kadane's-style "restart window on sum<0" fix — wrong, that's for
max-subarray-sum, not exact-target-sum. Needed full derivation of the
prefix-sum+hashmap approach, including the rearranged equation and the
"earliest index" reasoning.

## Complexity

O(n) time, O(n) space.
