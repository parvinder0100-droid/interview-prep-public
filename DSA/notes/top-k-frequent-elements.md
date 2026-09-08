---
type: note
problem: Top K Frequent Elements (LC 347)
topic: Heaps
updated: 2026-08-01
---

# Top K Frequent Elements

## Intuition

Build a frequency map (num -> count), then maintain a min-heap capped at
size k over (count, num) pairs. Whenever size exceeds k, pop — this evicts
the *smallest* count, so the k largest counts survive. O(n log k), better
than sorting all distinct counts when k is small relative to distinct count.

## Gotcha: comparator direction vs. eviction

A min-heap needs the smallest element at the top so it's the one popped.
Comparator must be ascending (`a.freq - b.freq`) — a descending comparator
puts the *largest* at the top, which would evict the wrong end. "Min-heap"
describes what sits on top (the min), not a free-standing label independent
of comparator direction.
