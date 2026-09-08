---
type: note
problem: Min Cost to Connect All Points (LeetCode 1584)
updated: 2026-08-01
---

# Min Cost to Connect All Points — MST (Kruskal's + Prim's)

Solved 3 ways same session (2026-08-01): Kruskal's (PQ + Union-Find), Prim's
(heap-based), Prim's (array-based O(n²)).

## Real bugs/gaps this session

- **Kruskal's — `parent[0]` accidental correctness.** `uf(n+1)` sized the
  array too big, and the init loop started at `i=1`, skipping index 0
  entirely. Worked only because `int[]` zero-initializes and node 0's
  correct self-parent value is also 0 — swap to `Integer[]` or reuse the
  helper on a problem where index 0 isn't self-parent-0, and it breaks
  silently. Fixed: `uf(n)`, `int[n+1]`, loop `i=0..n` inclusive.
- **Prim's — relax rule mistaken as cumulative.** Both algorithms share the
  same frontier-PQ skeleton, and the one differing line (relax formula) got
  pattern-matched from the more recently-drilled Dijkstra. Prim's:
  `dist[v] = min(dist[v], edge_weight(u,v))` — raw edge weight only.
  Dijkstra: `dist[v] = min(dist[v], dist[u] + edge_weight(u,v))` —
  cumulative from source. Caught via a 3-node counterexample
  (A-B=10, A-C=1, C-B=3): cumulative gives dist[B]=4 through C, and adding
  that to a running total that already counted the A-C edge (1) double-
  counts to 5, when the real MST cost is 4.

## Complexity notes

- Kruskal's (PQ of all n² edges + Union-Find): O(n² log n).
- Prim's heap-based (push up to n `Pair`s per visited node): also
  O(n² log n) — **no complexity win over Kruskal's for a dense/complete
  graph**, despite the different mechanism.
- Prim's array-based (no heap — linear min-scan each of n iterations):
  O(n²) — this is the actual win for dense graphs, avoids the log n factor
  entirely. Verified against the LeetCode 1584 editorial thread
  ("Prim's for Complete Graph" section) — same shape as what was derived
  here (`min_d[]` array, linear scan, raw-edge relax).

## Correctness ("why greedy works")

Cut property / exchange argument — capped at interview bar (swap-argument
+ one-liner), full formal proof flagged as over-depth by user, correctly.
See mistake_journal 2026-08-01 09:24.
