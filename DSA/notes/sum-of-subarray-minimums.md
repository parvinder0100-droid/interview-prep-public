---
type: note
problem: Sum of Subarray Minimums (LC 907)
topic: Stack / MonotonicStack / Contribution counting
created: 2026-08-27
---

# Sum of Subarray Minimums (LC 907)

https://leetcode.com/problems/sum-of-subarray-minimums/

## The technique

Don't loop over subarrays (O(n^2)). Loop over **elements** and ask each: *how
many subarrays am I the minimum of?* Sum `arr[i] * count(i)`.

    count(i) = (i - nsl[i]) * (nsr[i] - i)

`leftSide` counts choices of **start index**, `rightSide` counts choices of
**end index**. A subarray is the pair, so the count is a product. `i` belongs
to both sets — `[i,i]` is a subarray, not a double count.

## Why the counts must partition

Summing per-element counts is only valid if every subarray has **exactly one
owner**. Duplicates break that: in `[2,2]`, both twos are legitimately the
minimum of `[2,2]`.

Tie rule: strict on one side, non-strict on the other. Right pass pops on `<`
so `nsr` = nearest smaller-**or-equal**; every subarray is then credited to the
**leftmost** occurrence of its minimum.

    left  pass:  pop while cur <= arr[peek]    -> nearest strictly smaller
    right pass:  pop while cur <  arr[peek]    -> nearest smaller-or-equal

`[2,2]`: wrong version gives 8, correct gives 6.

## Contrast with LC 84 (same session)

Identical `nsl/nsr` machinery. LC 84 takes a **max**, so a double-claimed span
is harmless — strict on both sides is fine there. Here it is a **sum**, so
every double-claim is added twice. The machinery transfers; the tie rule does
not.

## Overflow

`n = 3e4` -> counts near `2.25e8`, times values `3e4` -> `~6.75e12`. `int` caps
at `2.147e9`. Use `long`, and note Java keeps `int * int` as `int` even when
assigned to a `long`. The problem stating "mod 1e9+7" *is* the overflow warning.

## Review focus

Open on the tie rule, not the code: why strict-on-both-sides double-counts, and
which side gets the non-strict comparison. Then the endpoint count formula from
first principles (enumerate pairs on `[3,1,2,4]`, `i=1`).
