---
type: pattern
pattern: BellmanFord
updated: 2026-07-26
status: in-use
---

# Bellman-Ford

## When This Pattern Applies

Single-source shortest path with **negative edge weights allowed**, or when you
need to **detect a negative cycle**. Dijkstra handles neither.

## Core Idea

Work off the raw edge list — no adjacency structure needed. Repeat V-1 times:
relax every edge (`if dist[u] != INF && dist[u] + wt < dist[v]` then update).
V-1 rounds suffice because any shortest path has at most V-1 edges — a repeated
vertex would mean a cycle, and a cycle in a shortest path implies a negative
cycle (otherwise it could be dropped for an equal-or-shorter path).

Then run **one more** pass, used purely as a detector: if anything still
improves on round V, that improvement can only come from a negative cycle.

## Problems Using This Pattern

- Bellman-Ford Algorithm (GFG "Distance from the Source") — 2026-07-26 — full
  code; two guard bugs and a missing detection round. See mistake_journal and
  `../notes/bellman-ford.md`.

## Common Pitfalls

- **Sentinel arithmetic.** `dist[u] + wt` is meaningless when `dist[u]` is the
  INF sentinel — no source→u path exists, so the sum is a fake finite path
  length. Guard with `dist[u] != INF`.
- **Guarding only one loop.** The relaxation loop and the detection loop are
  structurally identical and both read `dist[u]`. Guarding only the first
  produces a false "negative cycle" on any unreachable component holding a
  negative edge.
- **Fudged sentinels.** `Integer.MAX_VALUE - 1000` to dodge overflow still
  wraps for `wt > 1000`, and a wrapped-negative value looks like a large
  improvement. Use a real guard; pick the sentinel the problem's output
  contract demands (`1e8` for GFG).
- **Dropping the Vth round.** Without it there is no negative-cycle report —
  and derivations of it done in an earlier session do not automatically survive
  into code written later. Re-read notes before coding.
- **`while (changed)` instead of fixed V-1.** Same answer and often faster when
  no negative cycle exists, same `O(V·E)` worst case — but never terminates when
  one does. The fixed bound is what makes termination unconditional.

## Complexity

`O(V·E)` time, `O(V)` space.
