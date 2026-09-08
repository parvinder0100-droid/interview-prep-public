---
type: pattern
pattern: UnionFind
updated: 2026-08-07
status: in-use
---

# Union-Find (Disjoint Set)

## When This Pattern Applies

Dynamic connectivity — repeatedly asking "are x and y in the same group" and
"merge these two groups," without needing to enumerate group members. Cycle
detection in undirected graphs, Kruskal's MST, grouping/clustering problems.

## Core Idea

Parent array, each node initially its own parent. `find(x)`: recurse to the
root, then path-compress (point every visited node directly at the root on
the way back). `union(x, y)`: find both roots, attach one under the other —
by rank (tree height estimate) or size, to avoid a degenerate chain.

## Problems Using This Pattern

- Redundant Connection (LeetCode 684) — 2026-07-27 — full code; rank-increment
  bug, see mistake_journal and `../notes/union-find-redundant-connection.md`.
- Job Sequencing Problem (GFG) — 2026-08-07 — non-graph use: DSU over *slots*
  as an accelerator for "nearest free slot ≤ d" (see
  [[SlotAssignmentGreedy]]). Not recognized as a DSU problem cold — needed
  full explanation, see mistake_journal 2026-08-07.

## Common Pitfalls

- **Rank increment on every win, not just ties.** Rank is only a valid upper
  bound on tree height if it increments exactly when two equal-rank trees
  merge. Incrementing on a strict win desyncs rank from true height — doesn't
  break correctness (connectivity), but can force taller trees to nest under
  shorter ones later, degrading the O(log n) height guarantee.
- **Forgetting path compression.** Without it, `find` degrades toward O(n) on
  a skewed chain — union-by-rank alone only bounds height at O(log n), not
  the near-constant O(α(n)) both techniques give together.

## Complexity

`O(α(n))` amortized per operation with both path compression + union by rank —
practically constant (α(n) ≤ 4 for any realistic n), not literal O(1).
