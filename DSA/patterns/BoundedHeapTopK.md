---
type: pattern
pattern: Bounded Heap (Top-K)
status: in-use
updated: 2026-08-01
---

# Bounded Heap (Top-K)

## When This Pattern Applies

Need the k largest/smallest elements (by some key) out of n, k ≤ n, and
don't need the rest sorted.

## Core Idea

Maintain a heap capped at size k. For "k largest by key", use a *min*-heap
(ascending comparator on key) — top is always the current smallest of the
k kept, so it's the correct one to evict when size exceeds k. Symmetric
for "k smallest": max-heap, evict the current largest. O(n log k).

## Problems Using This Pattern

- Kth Largest Element in an Array — min-heap-of-size-k variant (O(n log k)).
- Top K Frequent Elements (LC 347) — freq map + min-heap-of-size-k on count.

## Common Pitfalls

- Comparator direction vs. heap "name" mismatch: a descending comparator
  puts the largest on top, which is the wrong end to evict for a "keep k
  largest" min-heap — 2026-08-01, Top K Frequent Elements.

- **Knowing `buildHeap` is O(n) without knowing `siftDown`.** Surfaced
  2026-08-15: the constant had been carried since 08-02 as a memorized fact
  with no method under it. `siftDown` requires both subtrees to already be
  heaps, swaps with the **larger** child, and repeats until the node dominates
  or bottoms out — so its cost is the node's *distance to the bottom*, not
  `log n`. `buildHeap` runs it bottom-up from the last non-leaf so that
  precondition always holds; leaves are size-1 heaps and are skipped. The sum
  `n/2·0 + n/4·1 + n/8·2 + …` converges to O(n); `n log n` wrongly charges
  every node the root's cost. If a review turns up a correct complexity, ask
  for the mechanism before accepting it.
