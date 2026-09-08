---
type: flashcards
topic: graphs
updated: 2026-07-25
---

# Graphs Flashcards

Format: Q on one line, A (intuition/complexity only, never full code) below it.

Q: In BFS, when do you mark a node `visited` — on push or on pop?
A: On push (enqueue). Marking on pop lets the same node be enqueued multiple
times by different unprocessed neighbors before it's ever marked.

Q: In DFS (recursive), when do you mark a node `visited`?
A: On entry, before recursing into neighbors — else a cycle re-enters an
in-progress node before it's marked (can infinite-loop).

Q: How does adjacency-matrix DFS/BFS differ from adjacency-list?
A: Neighbor lookup for node `src` becomes a full row scan
(`isConnected[src][j]==1` for `j` in `0..n`) instead of `adj.get(src)` —
same traversal logic, O(V) per node instead of O(degree).

Q: Multi-source BFS (Rotten Oranges) — when do you increment the
minute/level counter?
A: Only if at least one node was actually pushed during that level — not
every loop iteration. Gating on "a level ran" overcounts when nothing got
converted (e.g. no fresh oranges to start).

Q: Undirected cycle detection (BFS/DFS) — how do you tell a real cycle
from just walking back to the node you came from?
A: Carry the parent alongside each node. Skip the neighbor equal to parent;
if any other neighbor is already visited, that's a real cycle.

Q: Why doesn't the undirected parent-skip trick work for directed graphs?
A: A DAG can have two valid paths converge on the same node (diamond
shape) with zero cycles — plain visited-and-not-parent false-positives.
Need path-state (3-color DFS: gray=on current path=cycle, black=finished
branch=safe) or Kahn's in-degree BFS (count processed==n, else cycle).

Q: Why is a graph non-bipartite exactly when it has an odd-length cycle?
A: Walking a cycle flips color once per edge. L flips must land back on
the start node's original color for consistency — only even L does that.
Odd L forces the closing edge to connect two same-colored nodes.

Q: Kosaraju's SCC — why start the 2nd DFS from the last-finished node, not
any unvisited node?
A: Last-finished node has no incoming edges from other SCCs originally (all
its cross-SCC edges point out). After reversing the graph, those become
incoming-only — so DFS from there is trapped inside its own SCC, can't
leak into another via a reversed bridge edge.

Q: Dijkstra — a node can get pushed to the heap multiple times. When you pop
one, how do you know it's stale?
A: Compare popped distance to `dist[node]`; if `dist[node] < poppedDist`,
skip — a smaller value was already found and processed.

Q: Why does Dijkstra give a wrong (not infinite-loop) answer with a single
negative edge and no cycle?
A: The smaller-distance node pops first and gets locked in (visited). A
later node with a very negative edge into it could produce a smaller true
distance, but the lock skips relaxing into an already-finalized node.
Removing the lock fixes correctness but breaks the O(E log V) guarantee —
use Bellman-Ford instead.

Q: Dijkstra's "pop = final" is safe with non-negative weights. Which fact is
load-bearing — the priority queue or the weights?
A: The weights. The queue only gives "every unpopped node has dist ≥ the
popped value"; non-negativity gives "extending a path never lowers the
total." Without the second, an alternative path can still come back cheaper.

Q: Bellman-Ford runs V-1 relaxation rounds. Why exactly V-1?
A: Any shortest path has ≤ V-1 edges. A repeated vertex means a cycle, and a
cycle inside a shortest path implies a negative cycle — otherwise it'd be
droppable for an equal-or-shorter path.

Q: In Bellman-Ford, why must every loop reading `dist[u]` be guarded with
`dist[u] != INF`?
A: `dist[u] + wt` claims a path length source→u→v. If `dist[u]` is the
sentinel there's no source→u path, so the sum is a fake finite value (the
sentinel is a real integer, not true infinity). Missing the guard on the
detection loop reports a false negative cycle on unreachable components.

Q: Why not replace Bellman-Ford's fixed V-1 loop with "repeat until a full
pass changes nothing"?
A: Same answer and often faster with no negative cycle, same O(V·E) worst
case — but with a negative cycle something improves every pass, so it never
terminates. Fixed V-1 + a Vth detection pass makes termination unconditional
and lets you *report* the cycle.

Q: Dijkstra — reproduce the pop-is-final argument in 5 steps.
A: 1) Pop V with key 7. 2) Assume a shorter path to V exists, length 5.
3) It leaves the settled set at some node u still in the queue. 4) The queue
returned V, not u, so key[u] >= 7 — the prefix to u already costs >= 7.
5) The rest (u to V) is non-negative, so the total is >= 7 > 5. Contradiction.
Non-negativity is load-bearing at step 5 only; the PQ only supplies step 4.

Q: Bellman-Ford — what does V-1 count?
A: Edges, not neighbours. A path visiting V vertices has V-1 edges, and no
shortest path repeats a vertex (a repeat means a cycle — a non-negative one
is droppable for an equal-or-shorter path, a negative one means no shortest
path exists). Round k finalizes all shortest paths of k edges, so V-1 rounds
finalize every one of them.

Q: A Vth Bellman-Ford round still improves something. What does that prove?
A: A reachable negative *cycle* — not a negative edge. Negative edges are
fine: S-5->A, A-(-3)->B settles and a further round changes nothing.

Q: Floyd-Warshall — what does dist[i][j] mean right after the k-th outer
pass, and why must k be the outermost loop?
A: Shortest path from i to j using only nodes 1..k as intermediates. k
outer guarantees each phase is fully built (all i,j pairs updated) before
the next k starts, so dist[i][k]/dist[k][j] read during phase k are always
already-finalized from phases 1..k-1.

Q: Prim's relax rule vs Dijkstra's — what's the one differing line?
A: Prim's: dist[v] = min(dist[v], edge_weight(u,v)) — raw edge weight,
"cheapest edge connecting v to the tree." Dijkstra's: dist[v] =
min(dist[v], dist[u] + edge_weight(u,v)) — cumulative from source. Same
frontier-PQ skeleton otherwise; easy to pattern-match the wrong one.

Q: Prim's (heap) vs Kruskal's — which is faster on a dense/complete graph?
A: Neither, at O(n² log n) each (n² edges either way). The real win on
dense graphs is array-based Prim's (no heap, linear min-scan per
iteration): O(n²), drops the log n factor entirely.

Q: Kahn's topo sort — for edge `[a, b]` (b is a's prerequisite), which
node's indegree increments?
A: `a`'s (the dependent), not `b`'s. `graph[b].add(a)`, `indegree[a]++`.
Swapping this passes compilation and small "should be true" cases can
still look plausible — only a concrete trace catches it.

Q: Java gotcha — `sb.append((char)cur+'a')` vs `sb.append((char)(cur+'a'))`?
A: `(char)` is unary, binds only to `cur`. The first is `((char)cur)+'a'`
(char+char=int, `append(int)` writes digits); the second casts the sum,
writing the actual letter. Always parenthesize the arithmetic before casting.

Q: Alien Dictionary — why must the shorter-prefix-after-longer-word check
run *after* scanning for a differing character, not before?
A: A length mismatch alone doesn't mean invalid — "ba" vs "a" differ at
index 0 (a real edge, b->a). Only "no difference found, and the second word
ran out first" (like "abc" then "ab") is the actual invalid case.
