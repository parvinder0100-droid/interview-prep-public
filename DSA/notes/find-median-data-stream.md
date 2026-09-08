---
type: note
problem: Find Median from Data Stream (LC 295)
topic: Heaps / Two Heaps
updated: 2026-08-02
---

# Find Median from Data Stream (LC 295)

Solved 2026-08-02 16:54 (started 10:43). Approach was right on day one;
everything that went wrong went wrong in code.

## What broke

**1. NPE on the very first call.** The guard read
`minHeap.isEmpty() && maxHeap.peek() > minHeap.peek()`. On an empty min-heap
the first clause is *true*, so the second evaluates and unboxes `null`. Needed
`!minHeap.isEmpty()`.

**2. Rebalance guarded one direction only.** `maxSize > minSize+1` stops max
running away; nothing stopped min. On `1,2,3,4` the heaps settled at 1 and 3
and the even-branch read `(1+2)/2 = 1.5` against a true median of 2.5.
`findMedian` had been patched to read whichever heap was bigger, which hid the
symptom without fixing the cause.

## The invariant, stated properly

- Ordering: every element of max-heap ≤ every element of min-heap.
- Size: `maxSize == minSize` or `maxSize == minSize + 1`.

Both need enforcing. Handing min's top back to max is order-safe because
min's top is the *smallest* of the larger half, so it is ≥ everything in max.

A single `addNum` can only ever violate by one element, so one corrective
move per direction suffices — `if` would do, `while` is harmless.

## Complexity

`addNum` O(log n), `findMedian` O(1), space O(n).

Baselines worth being able to quote:
- Plain list: `addNum` O(1), `findMedian` O(n log n) sorting per call, or
  O(n) average via quickselect (O(n²) worst on bad pivots).
- **Values bounded to `[0,100]`**: frequency array of 101 slots. `addNum`
  O(1). `findMedian` walks cumulative counts and stops at the first index
  where `cum >= position` (position from `n` alone: `(n+1)/2` if odd, else
  `n/2` and `n/2+1` averaged). Both O(1), space O(1) — strictly better than
  heaps *when the range constraint holds*.

## Interview polish

`maxHeap.peek() + minHeap.peek()` is `int` addition. Safe under LC's
`[-10^5, 10^5]` constraint — say so out loud rather than leaving it silent.
