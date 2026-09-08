---
type: note
problem: Single Number III (LC 260)
topic: BitManipulation
created: 2026-09-02
---

# Single Number III (LC 260)

**Accepted 2026-09-02, with-hints:5.** No cold approach — started with "I don't know".

## The derivation, escalated in steps

1. XOR-all gives `x^y` (the two singles), self-derived once restated against the
   LC 136/137 mechanism.
2. Initial answer on the split rule was wrong: "either element has a set bit" —
   corrected to **exactly one** of x, y has any given set bit of `x^y` (that's
   what a set XOR bit means).
3. Landed the split via concrete instantiation, not derivation: a duplicate pair
   (a, a) has identical bits everywhere, so it always lands in the same group at
   any bit k; x and y differ at every set bit of `x^y`, so they always land in
   different groups. Confirmed by the user once posed this way.
4. "Why does it not matter which set bit you pick" was not derived — user said
   "I don't know" and then self-corrected via the same duplicate/differ argument
   applied generally (any set bit works for the same reason bit-by-bit).
5. Complexity O(n)/O(1) came cold, unprompted.

## Code

Correct first submit — array XOR, linear scan for lowest set bit, split-and-XOR
into two groups. Traced clean on `[1,2,1,3,2,5]` -> `[3,5]` before submission.

## Weak point to watch

The jump from "x and y differ at this bit" to "therefore pairs always land
together and x,y always land apart" needed a concrete pair example before it
generalized — same shape as prior bit-manipulation sessions (LC 136, LC 137):
mechanics recalled fast, the *why* behind a split/count needs numeric grounding
first.
