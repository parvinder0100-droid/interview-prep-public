---
type: pattern
pattern: FloydWarshall
updated: 2026-08-01
status: in-use
---

# Floyd-Warshall (All-Pairs Shortest Path)

## When This Pattern Applies

All-pairs shortest paths on a small-to-medium graph (V³ acceptable),
handles negative edges (not negative cycles). Dense graphs where running
Dijkstra/Bellman-Ford from every node would be worse or more complex.

## Core Idea

`dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`, k as the
**outermost** loop over all nodes, i and j inner. Base case: `dist[i][i]=0`,
direct edges from input, else INF.

## Invariant (the load-bearing "why")

After the k-th outer pass finishes, `dist[i][j]` for any pair = shortest
path from i to j using only nodes `1..k` as allowed intermediates. k
outermost guarantees phase k is fully built (every i,j pair updated) before
phase k+1 starts — so `dist[i][k]`/`dist[k][j]` read during phase k are
always already-finalized from phases `1..k-1`.

## Problems Using This Pattern

- Floyd-Warshall's Algorithm (derivation, no LeetCode problem attached) —
  closed 2026-08-01 16:32, 5th attempt (07-26, 07-30, 07-31, 08-01 08:35,
  08-01 16:32). See mistake_journal.

## Common Pitfalls

- **"Why k outer" stalling on an abstract re-trace.** Re-running the same
  abstract A-B-C-D chain trace 4 times didn't land it — what worked was
  anchoring on two concrete pair-values (one already-resolved, one not)
  and asking what's different between them, then generalizing from that.
- Deeper "prove k-inner breaks concretely under i/j-outer order" is past
  interview bar — cap at the invariant statement + why-k-outer-guarantees-
  it, don't chase the full order-dependency proof.

## Complexity

`O(V³)` time, `O(V²)` space (or O(1) extra if updating in place).
