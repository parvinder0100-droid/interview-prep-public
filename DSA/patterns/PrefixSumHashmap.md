---
type: pattern
pattern: PrefixSumHashmap
updated: 2026-07-20
status: in-use
---

# PrefixSumHashmap

## When This Pattern Applies

Subarray-sum-equals-target problems where the array can contain **negative
numbers** — sliding window breaks here because sum no longer grows
monotonically as the window expands. First check: "does this array allow
negatives?" If yes, go straight to this pattern, not sliding window.

## Core Idea

`sum(i+1..j) = prefixSum[j] - prefixSum[i]`. Want this equal to k →
`prefixSum[i] = prefixSum[j] - k`. Scan left to right maintaining a hashmap of
prefix-sum values seen so far. Two variants:
- **Longest subarray with sum k**: map stores `{prefixSum -> earliest index}`
  (earliest index maximizes length); seed `{0:-1}` so a prefix summing to k
  from index 0 gives length `i-(-1)=i+1`, not `i-0=i` (derive the seed from the
  length formula, don't just memorize it).
- **Count of subarrays with sum k**: map stores `{prefixSum -> count}`; seed
  `{0:1}`. At each index: (1) look up `sum-k`, add the found count to the
  answer as-is, no `+1`; (2) THEN insert/increment `sum` in the map, `+1`
  happens only here. Keep read and write as separate mental steps.

O(n) time/space, works with negatives.

## Problems Using This Pattern

- Longest Subarray with Sum K — Arrays/Easy — solved 2026-07-12 with full
  derivation (genuine new-material gap at the time).
- Subarray Sum Equals K — Arrays/Medium — solved 2026-07-13, count variant.

## Common Pitfalls

- Defaulting to sliding window on a sum-target problem without checking for
  negatives first — confirmed trap twice (2026-07-12 and 2026-07-13, one day
  apart), didn't spontaneously generalize the rule the first time.
- Seed-value amnesia: recalling `{0:-1}` or `{0:1}` as a fact instead of being
  able to re-derive it from the formula when asked why.
- Lookup-vs-insert conflation on the count variant: adding `+1` to the count
  found via lookup (belongs only to the insert/increment step) — confirmed
  regression at review #2 (2026-07-20).
