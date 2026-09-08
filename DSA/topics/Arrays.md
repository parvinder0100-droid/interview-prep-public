---
type: topic
topic: Arrays
updated: 2026-07-20
status: in-progress — 27 problems confirmed solved live — Basics+Easy+Medium
  subtopics complete (Medium finished 2026-07-20 with Print Subarray with
  Maximum Sum). Hard subtopic (11 problems) untouched. Codolio import
  separately said 2/40 (exact 2 unknown) — priority gap topic
---

# Arrays

## Subtopics (Striver A2Z order)

- Basics: largest element, second largest/smallest, check sorted, remove duplicates from
  sorted array, rotate array, move zeroes to end.
- Easy: linear search variants, union of two sorted arrays, missing number, max consecutive
  ones, single number (XOR), longest subarray with sum K.
- Medium: two sum, sort array of 0s/1s/2s (Dutch National Flag), majority element (>n/2),
  Kadane's maximum subarray sum, print subarray with max sum, stock buy/sell, rearrange
  positive/negative, next permutation, leaders in array, longest consecutive sequence,
  set matrix zeroes, rotate matrix, spiral traversal, subarray sum equals K, Pascal's
  triangle.
- Hard: majority element (>n/3), 3-sum, 4-sum, largest subarray with 0 sum, count
  subarrays with XOR K, merge overlapping intervals, merge two sorted arrays without
  extra space, find repeating and missing number, count inversions, reverse pairs,
  maximum product subarray.

## Patterns That Show Up Here

- [[TwoPointers]]
- [[Kadanes]]
- [[SlidingWindow]]
- [[PrefixSum]]
- [[MergeIntervals]]

## Problems Log

_Populated as problems are completed. See the `../notes/` folder for individual problem notes._

Codolio import (2026-07-10) reports 2/40 solved in this topic, but the per-question
solved flags in that export were inconsistent for this topic specifically (didn't sum
to 2 on any individual entries) — **treat the exact 2 solved problems as unknown until
confirmed live.** Only ~5% done here despite Binary Search/LinkedList being 100%, so
this is a real priority gap for Week 1.

- [x] Find the Largest Element in an Array — Basics — Easy — solved: independently
  — 2026-07-11
- [x] Second Largest Element in an Array — Basics — Easy — solved: with-hints:1 —
  2026-07-11 — duplicate-of-max edge case, see [[mistake_journal]] and
  [note](../notes/second-largest-element.md)
- [x] Check if Array is Sorted — Basics — Easy — solved: independently — 2026-07-11
- [x] Remove Duplicates from Sorted Array — Basics/Two Pointers — Medium —
  solved: with-hints:2 — 2026-07-11 — see
  [note](../notes/remove-duplicates-sorted-array.md)
- [x] Move Zeroes to End — Basics/Two Pointers — Medium — solved: with-hints:1 —
  2026-07-11 — see [note](../notes/move-zeroes-to-end.md)

- [x] Rotate Array — Basics — Easy — solved: with-hints:3 — 2026-07-12 — fully
  stuck on O(1)-space reversal trick, see [[mistake_journal]] and
  [note](../notes/rotate-array.md)
- [x] Linear Search — Easy — Easy — solved: independently — 2026-07-12
- [x] Union of Two Sorted Arrays — Easy — Easy — solved: with-hints:1 —
  2026-07-12 — missed dedup step initially
- [x] Missing Number — Easy — Easy — solved: independently — 2026-07-12
- [x] Max Consecutive Ones — Easy — Easy — solved: with-hints:1 — 2026-07-12 —
  missed post-loop check for trailing window
- [x] Single Number — Easy — Easy — solved: independently — 2026-07-12
- [x] Longest Subarray with Sum K — Easy — Medium — solved: with-hints:4 —
  2026-07-12 — fully stuck on negative-number generalization, see
  [note](../notes/longest-subarray-sum-k.md)
- [x] Two Sum — Medium — Easy — solved: with-hints:1 — 2026-07-12 —
  over-engineered duplicate handling, self-corrected
- [x] Sort Array of 0s, 1s, 2s (DNF) — Medium — Medium — solved: with-hints:5 —
  2026-07-12 — deep invariant confusion, see [note](../notes/sort-012.md)

- [x] Majority Element (>n/2, Boyer-Moore) — Medium — Medium — solved:
  independently — 2026-07-12
- [x] Kadane's Maximum Subarray Sum — Medium — Medium — solved: with-hints:2 —
  2026-07-12 — all-negative edge case, see [note](../notes/kadanes-max-subarray.md)
- [x] Stock Buy and Sell — Medium — Easy — solved: with-hints:1 — 2026-07-12
- [x] Rearrange Array Elements by Sign — Medium — Medium — solved: with-hints:1
  — 2026-07-12
- [x] Next Permutation — Medium — Hard — solved: with-hints:5 — 2026-07-12 —
  deep stuck, see [note](../notes/next-permutation.md)
- [x] Leaders in an Array — Medium — Easy — solved: with-hints:1 — 2026-07-12
- [x] Longest Consecutive Sequence — Medium — Medium — solved: with-hints:4 —
  2026-07-12 — see [note](../notes/longest-consecutive-sequence.md)
- [x] Set Matrix Zeroes — Medium — Medium — solved: with-hints:2 — 2026-07-12
  — (0,0) shared-cell conflict
- [x] Rotate Matrix (90°) — Medium — Medium — solved: with-hints:2 —
  2026-07-12 — transpose+reverse-rows derivation

- [x] Spiral Traversal — Medium — Medium — solved: with-hints:5 — 2026-07-13 —
  deep stuck on outer-loop condition (top<=bottom && left<=right) and the two
  extra pass-guards (top<=bottom before bottom-row pass, left<=right before
  left-col pass), see [[mistake_journal]]

- [x] Subarray Sum Equals K — Medium — Medium — solved: with-hints:3 —
  2026-07-13 — initially proposed sliding-window (invalid, negatives
  allowed), self-corrected to prefix-sum+count-hashmap after being pointed
  at own mistake log, see [[mistake_journal]]

- [x] Pascal's Triangle — Medium — Medium — solved: with-hints:2 —
  2026-07-17 — trailing-1 append and middle-recurrence loop bounds needed
  clarification, correct once traced concretely.

- [x] Print Subarray with Maximum Sum — Medium — Medium — solved:
  with-hints:many — 2026-07-20 — dual-pointer (tempStart vs start) Kadane's
  variant, resolved via guided trace, see [[mistake_journal]]
  https://www.geeksforgeeks.org/problems/kadanes-algorithm/1

Medium subtopic complete (15/15). Hard subtopic (11 problems) untouched —
next up if continuing Arrays.

## Common Mistakes Seen in This Topic

- 2026-07-11: guessed instead of tracing on a duplicate-handling edge case
  (Second Largest).
- 2026-07-11: default two-pointer instinct compares current-vs-next instead of
  current-vs-last-confirmed-good, forcing avoidable special cases (Remove
  Duplicates).
- 2026-07-11: reused a prior pattern (overwrite-forward) without checking the
  new problem's postcondition on the untouched tail of the array (Move
  Zeroes). See [[mistake_journal]] for full entries.
- 2026-07-12: boundary/tail case missed a 3rd time — no post-loop check for
  the final window (Max Consecutive Ones). Confirmed recurring pattern, not
  one-off — standing checklist item now.
- 2026-07-12: two problems required full derivation from stuck (Rotate Array
  reversal trick; Longest Subarray Sum K prefix-sum+hashmap generalization for
  negatives) — genuine new-pattern gaps, not rust. See [[mistake_journal]].
- 2026-07-12 (session 2): three more deep-derivation stuck points (Kadane's
  all-negative edge case, Next Permutation's swap-partner+suffix-reverse rule,
  Longest Consecutive Sequence's O(n²)->O(n) fix) — all genuine new-pattern
  gaps. Guided one-line-at-a-time tracing (vs asking for a full self-trace)
  is what unstuck Kadane's — default to that style for future stuck moments.
- 2026-07-13: Spiral Traversal deep stuck on outer-loop AND-condition and the
  two per-pass guards — resolved via guided one-line-at-a-time tracing
  (matches the style that worked 2026-07-12). Same-day review reps (17 of 18
  due Arrays problems) all clean except Rotate Matrix, which repeated its
  original rust (forgot full-row-reverse after transpose) — standing gap, not
  yet solid.

## Cut-list queue — itemized 2026-08-31 (Day 0)

From `Progress/coverage_cut_list.md`. `- [ ]` = scheduled, not yet solved.

**13 slots — the Hard subtopic, recorded as *untouched*, so all 13 are
unsolved and no solved/unsolved split is needed. Only the names are missing.**
Cut list describes the shape: intervals, matrix, majority-II, 4sum,
subarray-sum families.

- [ ] TBD x13 — needs the sheet's Step 3 Hard sub-section
