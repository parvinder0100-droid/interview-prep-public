---
type: pattern
pattern: K-way Merge (bounded heap over k sources)
status: in-use
updated: 2026-08-02
---

# K-way Merge

## When This Pattern Applies

Merging `k` already-sorted sequences (lists, arrays, streams) into one sorted
output, where materializing everything and re-sorting is wasteful or
impossible.

## Core Idea

Hold exactly one candidate per source in a min-heap — the current head of each
sequence. Pop the global minimum, append it to the output, then push that
source's successor. The heap never exceeds `k`, so each of the `N` total
elements costs `O(log k)`.

Time `O(N log k)`, auxiliary space `O(k)`.

## Problems Using This Pattern

- Merge k Sorted Lists (LC 23) — 2026-08-02, approach only, code not written.

## Common Pitfalls

- Pushing *every* node up front instead of one head per list — still correct,
  but degrades to `O(N log N)` time and `O(N)` space.
- Counting the output as auxiliary space. For linked lists the result can
  **relink existing nodes**, allocating nothing — auxiliary space is the heap
  alone, `O(k)` — 2026-08-02, see [[mistake_journal]].
- Forgetting that `lists` may be empty, or contain `null` entries: skip nulls
  during initialization, and an empty heap after init means return `null`.
