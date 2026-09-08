---
type: pattern
pattern: Two Heaps (Median Maintenance)
status: in-use
updated: 2026-08-02
---

# Two Heaps (Median Maintenance)

## When This Pattern Applies

Need a running middle-of-the-stream statistic (median, or a balanced
split point) under interleaved inserts and queries, with no ability to
re-sort per query.

## Core Idea

Split the multiset into a lower half and an upper half. Lower half lives
in a **max**-heap (its top = largest of the small side), upper half in a
**min**-heap (its top = smallest of the big side). The two tops are
exactly the candidate middle values, so the query is O(1) and inserts are
O(log n). Keep sizes within 1 of each other so the tops stay on the true
middle.

## Problems Using This Pattern

- Find Median from Data Stream (LC 295) — **closed 2026-08-02 16:54**,
  full code written. Structure derived 10:43, rebalance + code 16:54.

## Common Pitfalls

- Assigning the halves backwards (lower half into the min-heap). Derive
  from "which single element must this heap expose in O(1)?", not from
  the heap's name — 2026-08-02, see [[mistake_journal]]. Same root shape
  as the Bounded Heap comparator-direction slip, see
  [[BoundedHeapTopK]].
- Guarding only one side of the size invariant. `maxSize > minSize+1` stops
  max running away but nothing stops min — sizes drifted 1 vs 3 and the
  median read wrong. Both directions need a move — 2026-08-02, see
  [[mistake_journal]].
- Emptiness guard written as `heap.isEmpty() && heap.peek() > ...` instead
  of `!heap.isEmpty() && ...` — NPE on the first call, since `peek()` on an
  empty `PriorityQueue<Integer>` returns `null` and unboxes.
- Patching `findMedian` to read whichever heap is larger *hides* an
  imbalance rather than fixing it — fix the invariant in `addNum`.
