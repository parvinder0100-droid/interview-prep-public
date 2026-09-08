---
type: flashcards
topic: Heaps
updated: 2026-08-01
---

# Heaps — Flashcards

Q: Kth Largest Element — two heap approaches, and when is each better?
A: Max-heap of all n, pop k-1, peek: O(n log n + k log n). Min-heap capped
at size k (pop min whenever size > k), peek at end: O(n log k) — better
when k ≪ n.

Q: Is push-one-by-one the only way to build a heap from an array?
A: No — bottom-up `build-heap`/`heapify` is O(n), not O(n log n). Sift down
from the last non-leaf node to the root (skip leaves); most nodes are near
the bottom and sift a short distance, so the total work converges to O(n).
Java's `new PriorityQueue<>(Collection)` and Python's `heapq.heapify()`
both use this internally.

Q: Top K Frequent Elements — approach and why min-heap-of-k, not max-heap?
A: Freq map, then min-heap capped at size k over (count, num); pop when
size>k. Min-heap evicts the smallest count each time, leaving the k
largest. O(n log k) vs O(n log n) for sorting all distinct counts.

Q: Min-heap eviction — which comparator direction?
A: Ascending (`a.freq - b.freq`), so smallest sits on top and gets popped.
A descending comparator puts the largest on top instead — wrong end for
eviction. "Min-heap" = what's on top, driven by comparator direction, not
a separate property.

Q: Running median over a stream — which half goes in which heap, and why?
A: Lower half in a max-heap, upper half in a min-heap. Each heap must
expose the element nearest the middle in O(1): the largest of the small
side and the smallest of the big side. Reverse the assignment and the
tops are the two *extremes*, useless for a median.

Q: Two-heap median — what are the two invariants, and why does handing an
element back from the min-heap preserve ordering?
A: (1) every element in max-heap ≤ every element in min-heap; (2) sizes
equal, or max exactly one larger. Min's top is the *smallest* of the larger
half, so it is ≥ everything in max — safe to move across. Guard both
directions: `maxSize > minSize+1` and `minSize > maxSize`.

Q: Running median when all values are bounded to `[0, 100]` — beat the heaps?
A: Frequency array of 101 slots. addNum O(1); findMedian walks cumulative
counts and stops at the first index where `cum >= position`, where position
comes from n alone ((n+1)/2 if odd, else n/2 and n/2+1 averaged). O(1) time
and space both — but only while the range constraint holds.

Q: Merging k sorted lists — heap size, complexity, auxiliary space?
A: One head per list, so heap ≤ k. O(N log k) time. Auxiliary space O(k) —
relink the existing nodes, the output is not extra space.

Q: Task Scheduler — which task to run next, and when is it available again?
A: Highest remaining frequency among currently available tasks (it dictates
the skeleton). Next availability is `current + n + 1` — n counts the empty
slots *between* runs, not the distance to the next one.

Q: Task Scheduler closed form?
A: `max( (maxFreq-1)*(n+1) + countMax, totalTasks )`. First term = maxFreq-1
blocks of width n+1, plus one slot per task tied at max frequency. Second
term takes over when there are enough distinct tasks to fill every idle slot.

Q: What precondition does `siftDown` assume, and what does that force about build-heap's traversal order?
A: Both subtrees of the node must already be valid heaps. So build-heap runs
bottom-up, from the last non-leaf down to index 0 — leaves are size-1 heaps and
need no work.

Q: Why is build-heap O(n) and not O(n log n)?
A: A node's sift-down cost is its distance to the bottom, not the tree height.
Half the nodes are leaves (cost 0), a quarter cost ≤1, an eighth cost ≤2; only
the root costs log n. The sum converges to O(n). `n log n` charges every node
what only the root pays.

Q: In sift-down, why swap with the *larger* child rather than either one?
A: Swapping with the smaller child puts a value above its larger sibling and
breaks the heap property immediately.
