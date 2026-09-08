---
type: pattern
pattern: MST
updated: 2026-08-01
status: in-use
---

# Minimum Spanning Tree (Kruskal's + Prim's)

## When This Pattern Applies

Connect all nodes in a weighted undirected graph at minimum total edge
cost, no cycles. "Connect all points," network design, clustering with a
cost floor.

## Core Idea

Two greedy approaches, both correct by the cut property (cheapest edge
crossing any cut is safe to add — swapping it in for a pricier crossing
edge in any tree strictly lowers cost):

- **Kruskal's** — edge-centric. Sort/heap all edges globally, repeatedly
  take the cheapest one that doesn't form a cycle (checked via Union-Find).
  Order-independent of any starting node.
- **Prim's** — vertex-centric. Grow one tree from a start node; at each
  step add the cheapest edge from the current tree to any node not yet in
  it. Always a single connected piece — visited-set instead of Union-Find.
  - Heap-based: PQ of (node, cost), lazy deletion of stale entries.
  - Array-based (dense/complete graphs): `dist[]` array + linear min-scan
    each iteration instead of a heap — drops the log n factor.

## Problems Using This Pattern

- Min Cost to Connect All Points (LeetCode 1584) — 2026-08-01 — solved all
  3 ways same session. See [note](../notes/mst-min-cost-connect-points.md)
  and mistake_journal.

## Common Pitfalls

- **Prim's relax rule mistaken as cumulative (Dijkstra transfer).** Prim's
  `dist[v]` = cheapest single edge connecting v to the tree, not distance
  from a fixed source — `dist[v]=min(dist[v], edge_weight(u,v))`, no
  `+dist[u]`. Both algorithms share the same frontier-PQ skeleton, so the
  one differing line is easy to pattern-match wrong. 2026-08-01.
- **Union-Find init loop off-by-one.** Skipping index 0 in the init loop
  can look correct by accident if the language zero-defaults arrays and
  node 0's correct self-parent value is also 0 — fragile, not by design.
  Always initialize the full index range explicitly. 2026-08-01.
- **Assuming heap-based Prim's beats Kruskal's on dense graphs.** Both are
  O(n² log n) for a complete graph (n² edges either way) — no win. The
  actual win is array-based Prim's, O(n²), no heap.

## Complexity

- Kruskal's: O(E log E) generally; O(n² log n) for a complete graph (E=n²).
- Prim's (heap): O(E log V) generally; O(n² log n) for a complete graph —
  same class as Kruskal's, no advantage.
- Prim's (array, dense/complete graphs): O(V²) — the right choice when
  E ≈ V².
