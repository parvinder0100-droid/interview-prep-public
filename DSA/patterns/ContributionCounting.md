---
type: pattern
pattern: ContributionCounting
updated: 2026-08-27
status: in-use
---

# ContributionCounting

## When This Pattern Applies

"Sum some property over **all** subarrays/subsets" — where enumerating them is
O(n^2) or worse, but each element's total contribution is computable in O(1).

Signal words: *sum of minimums / maximums / ranges over all subarrays*.

## Core Idea

Invert the loop. Instead of iterating subarrays and asking "what's your min?",
iterate elements and ask **"how many subarrays am I the min of?"** Then

    answer = sum over i of  arr[i] * count(i)

For a subarray to have `arr[i]` as its minimum it must contain `i` and must not
reach past a smaller element on either side — so the boundaries are exactly
`nsl[i]` and `nsr[i]` ([[MonotonicStack]]):

    count(i) = (i - nsl[i]) * (nsr[i] - i)

Left factor = number of valid **start** indices, right factor = number of valid
**end** indices. A subarray is the *pair*, so it is a product. `i` is a valid
endpoint on both sides — `[i,i]` is a subarray, and excluding it is the
off-by-one this pattern invites.

## The correctness condition — partition, not cover

The sum is only valid if every subarray is counted by **exactly one** element.
Duplicates violate this by default: in `[2,2]` both twos are minima of `[2,2]`.

Fix: break ties one way — strict comparison on exactly one side, non-strict on
the other, which credits each subarray to (say) the leftmost occurrence of its
minimum.

    left  pass:  pop while cur <= arr[peek]     -> nearest strictly smaller
    right pass:  pop while cur <  arr[peek]     -> nearest smaller-or-equal

## Problems Using This Pattern

- Sum of Subarray Minimums (LC 907) — Medium — solved 2026-08-27 with 4 hints;
  technique named cold, tie rule and overflow both missed. See
  [note](../notes/sum-of-subarray-minimums.md).

## Common Pitfalls

- **Counting "extra elements beyond i" instead of endpoints including i.** `i`
  itself is always one valid start and one valid end. Enumerate the pairs on a
  4-element array before trusting the formula.
- **Reusing an `nsl/nsr` template from a `max` problem.** Double-claims are free
  under `max` and fatal under `sum` — see the tie-rule entry in
  [[MonotonicStack]].
- **Overflow.** Counts are O(n^2)-sized even though the algorithm is O(n): at
  `n=3e4`, `count * value` reaches ~`6.75e12`. A stated "mod 1e9+7" is the
  problem telling you the raw answer overflows. In Java, `int * int` stays `int`
  even when assigned to a `long` — cast the operands.

## Related

- [[MonotonicStack]] — supplies the boundaries.
- Sum-of-subarray-**maximums** is the same code with the comparisons flipped;
  "sum of subarray ranges" is max-sum minus min-sum.
