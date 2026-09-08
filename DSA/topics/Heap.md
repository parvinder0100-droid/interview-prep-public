---
type: topic
topic: Heap
updated: 2026-08-02
status: in-progress
---

# Heap

## Subtopics (Striver A2Z order)

Started 2026-08-01 with the classic entry point (Kth Largest Element).
Rest of the Striver order to be filled in as reached.

## Patterns That Show Up Here

- Fixed-size min/max heap for top-k / kth-element problems — see
  Kth Largest Element below.

## Problems Log

- Kth Largest Element in an Array — 2026-08-01 — with-hints:1 — both
  max-heap (pop k-1) and min-heap-of-size-k (O(n log k), better for
  k≪n) approaches self-derived cold; only gap was the build-heap/heapify
  O(n) fact (first exposure). See mistake_journal.
- Top K Frequent Elements (LC 347) — 2026-08-01 — with-hints:1 —
  freq-map + min-heap-of-size-k self-derived; eviction-comparator
  direction (asc vs desc) briefly confused, self-corrected. Approach only,
  no code written. https://leetcode.com/problems/top-k-frequent-elements/
  See mistake_journal.
- Find Median from Data Stream (LC 295) — 2026-08-02 10:47 — **in progress,
  not solved** — two-heap structure named cold, halves initially assigned
  backwards, self-corrected after 1 concrete-instantiation question.
  `addNum`/rebalance rule and complexity not yet derived; naive-baseline
  cost asked twice, never answered.
  https://leetcode.com/problems/find-median-from-data-stream/
  See mistake_journal.
- Find Median from Data Stream (LC 295) — 2026-08-02 16:54 — **closed** —
  with-hints:several — full code written; NPE guard and missing min→max
  rebalance both found by trace and self-fixed. Bounded-range `[0,100]`
  variant (freq array of 101 + cumulative walk, O(1)/O(1)) also derived.
  See mistake_journal.
- Merge k Sorted Lists (LC 23) — 2026-08-02 16:54 — with-hints:2 —
  approach only, code skipped. Heap-size-≤-k and O(N log k) cold;
  auxiliary space O(k) vs output needed 2 escalations.
  https://leetcode.com/problems/merge-k-sorted-lists/ See mistake_journal.
- Task Scheduler (LC 621) — 2026-08-02 16:54 — with-hints:several —
  approach only, code not written. Heap-backed greedy; see [[Greedy]].
  https://leetcode.com/problems/task-scheduler/ See mistake_journal.

## Common Mistakes Seen in This Topic

- Not knowing bottom-up `build-heap`/`heapify` is O(n), not O(n log n) —
  2026-08-01, first exposure, see [[mistake_journal]].
- Confusing "descending comparator" (max at top) with "min-heap eviction"
  (should keep smallest at top to discard) — 2026-08-01, see
  [[mistake_journal]].

## Cut-list queue — itemized 2026-08-31 (Day 0)

From `Progress/coverage_cut_list.md`. `- [ ]` = scheduled, not yet solved.

**6 slots; 2 of the cut list's named items are already done.**

- [ ] Kth Largest Element in an Array (LC 215)
- [ ] Merge k Sorted Lists (LC 23)
- [ ] Top K Frequent Elements (LC 347)
- [ ] Hand of Straights (LC 846)
- [ ] TBD — 2 slots unnamed; cut list says "k-th largest variants"
- [x] Find Median from Data Stream — done, see review_schedule
- [x] Task Scheduler (LC 621) — done, graduated off `[leech]` 2026-08-30
