---
type: note
problem: Power of Two (LC 231)
topic: BitManipulation
created: 2026-09-02
---

# Power of Two (LC 231)

**Accepted 2026-09-02, with-hints:3.** No cold approach — started with "no idea".

## The derivation

1. Closed via instantiation, not from a name: wrote 1, 2, 4, 8, 16 in binary and
   named the shared property unaided — exactly one set bit.
2. `n & (n-1) == 0` derived from a concrete pair, `8 & 7` — did not need it
   generalized further, saw it holds for any single-set-bit number.
3. Edge case (n=0) named unaided once asked what could break the check.

## Code bug — real, judge-relevant

First draft guarded only `n == 0`. Missed: **`Integer.MIN_VALUE`
(-2147483648) has exactly one set bit** (the sign bit alone), so
`n & (n-1) == 0` passes for it despite being negative. Guard needed to be
`n <= 0`, not `n == 0`. Fixed once pointed at the specific test case
(`Integer.MIN_VALUE`) — not derived independently; this is a real edge case in
LC 231's judge test set, not a hypothetical.

## Standing pitfall for this topic

Any "exactly one set bit" check needs an explicit sign check first — two's
complement means the most negative int is a false positive under bit-count-only
tests. Filed to `../patterns/BitCountingModK.md` if that file is the right home,
otherwise worth a dedicated bit-tricks pitfalls note if this recurs.
