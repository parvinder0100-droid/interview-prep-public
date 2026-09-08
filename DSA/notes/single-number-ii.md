---
type: note
problem: Single Number II (LC 137)
topic: BitManipulation
created: 2026-09-01
---

# Single Number II (LC 137)

**Accepted 2026-09-01, with-hints:3.**

## The derivation, which was correct in full before any code

1. XOR-everything fails: on `[1,1,1,2]` it gives `1^2 = 3`. Pairs cancel, so a
   triple leaves one copy behind.
2. Reframed: XOR on a single bit position is **the count of 1s, mod 2**. That is
   exactly why pairs vanish and triples do not.
3. HashMap of frequencies is `O(n)` space — rejected against the `O(1)` bar.
4. So: count the 1s per bit position, take each count **mod 3**, and the surviving
   bits are the loner's. Verified by hand on the binary columns of `[1,1,1,2]`:
   counts `3` and `1`, mod 3 gives `0` and `1` -> `010` = 2.
5. 32 slots, not 31 — indices `0..31`. Bit 31 must be counted, not skipped:
   constraints allow negatives, and in two's complement the sign bit is just
   another column that obeys the same mod-3 rule.
6. `O(32n) = O(n)` time; the 32-slot array is fixed size, independent of `n`, so
   `O(1)` space.

## The two defects, both at the write step

- `freq[i] % 2` — **the mod-2 rule from LC 136, written minutes after mod 3 was
  derived by hand.** This is the derivation-to-code regression, second sighting
  in two sessions.
- `res |= freq[i]>0 ? i<<1 : 0` — operands swapped; `1<<i` was meant. Fails at
  `i=0` (`0<<1 = 0`).

## Standing fix

Write the derived predicate as the first line of code, before the surrounding
structure. Prescribed 2026-08-31, not run on either occasion since.
