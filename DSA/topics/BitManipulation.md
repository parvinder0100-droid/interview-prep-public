---
type: topic
topic: BitManipulation
updated: 2026-09-02
status: complete — 5 of 5 cut-list slots done live (LC 136, 137, 260, 231, 191) as of 2026-09-02; Codolio import reported 1/18, partial data
---

# BitManipulation

## Subtopics (Striver A2Z order)

_18 problems total per Codolio; the export got cut off before listing them — subtopic
breakdown to be filled in when this topic is actually reached._

## Patterns That Show Up Here

_To be linked as problems are worked through._

## Problems Log

Codolio import (2026-07-10) reports 1/18 solved, but the export was truncated before
the individual question list for this topic — **which specific problem is unknown.**
Confirm live or re-import.

## Common Mistakes Seen in This Topic

_None logged yet — see [[mistake_journal]]._

## Cut-list queue — itemized 2026-08-31 (Day 0)

From `Progress/coverage_cut_list.md`. `- [ ]` = scheduled, not yet solved.

**5 slots, 6 candidates named in the cut list — one gets dropped at Day 0+1.**

- [x] Single Number (LC 136) — 2026-09-01, **Accepted**, cold (re-verify of the 2026-07-12 solve)
- [x] Single Number II (LC 137) — 2026-09-01, **Accepted**, with-hints:3
- [x] Single Number III (LC 260) — 2026-09-02, **Accepted**, with-hints:5
- [x] Count Set Bits / Number of 1 Bits (LC 191) — 2026-09-02, **Accepted**, with-hints:1
- [x] Power of Two (LC 231) — 2026-09-02, **Accepted**, with-hints:3
- [ ] ~~Subsets via bitmask~~ — **drop candidate**: already covered by Subsets
      (LC 78, solved 2026-08-28) and the LC 46 bitmask on 2026-08-31

## Live Log

- 2026-09-01 — **LC 136 Accepted, cold.** XOR named instantly with the
  cancellation argument. Gap: could not name commutativity/associativity as the
  property that lets separated duplicates be brought together — `x^x=0` alone
  does not license reordering a left-to-right fold. Handed over.
- 2026-09-01 — **LC 137 Accepted, with-hints:3.** Full derivation before code:
  XOR fails because it is a per-bit count **mod 2** and triples leave one copy;
  HashMap fails the `O(1)` space bar; per-bit count **mod 3** rebuilds the
  loner. 32 slots, and bit 31 must be counted (constraints allow negatives —
  two's complement makes the sign bit just another column). Two write-step
  defects: `%2` for `%3` minutes after deriving mod 3, and `i<<1` for `1<<i`.
  See [note](../notes/single-number-ii.md).
- 2026-09-02 — **LC 260 Accepted, with-hints:5.** No cold approach. Restated
  the LC 136/137 XOR-all mechanism unaided (`x^y`), but "either element has a
  set bit" needed correcting to "exactly one differs" — closed via a
  duplicate-pair vs differing-pair numeric split. Code correct first try.
  See [note](../notes/single-number-iii.md).
- 2026-09-02 — **LC 231 Accepted, with-hints:3.** No cold approach; closed via
  binary instantiation of small powers, then `n & (n-1) == 0` derived from
  `8 & 7`. Code bug: guard was `n==0` only, missed Integer.MIN_VALUE
  (single-set-bit negative) — fixed once pointed at the test case.
  See [note](../notes/power-of-two.md).
- 2026-09-02 — **LC 191 Accepted, with-hints:1.** Loop-and-mask approach and
  O(1)/O(1) complexity both cold. Clean, no notable defect.

**Topic complete — 5/5 cut-list slots done live.**
