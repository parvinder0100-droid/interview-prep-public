---
type: topic
topic: Graph
updated: 2026-09-05
status: in-progress — started 2026-07-25, top Week 3 priority
---

# Graph

## Subtopics (Striver A2Z order)

Standard Striver order: BFS/DFS (done), number of provinces/islands (done), flood
fill (done), rotten oranges (done), cycle detection (BFS & DFS, directed & undirected)
(done), topological sort (done), bipartite check (done), strongly connected components
(Kosaraju) (done), Dijkstra (done), Bellman-Ford (done), Floyd-Warshall (done,
2026-08-01), MST/Prim's/Kruskal's (done, 2026-08-01), disjoint set/Union-Find
(done). Full core list covered at least once as of 2026-08-01 — remaining
work is review-ladder consolidation, not new material.

## Patterns That Show Up Here

- Graph Traversal (BFS/DFS) — visited-at-push (BFS) / visited-on-entry (DFS)
- Connected Components (DFS/BFS over adjacency matrix or grid)
- Multi-source BFS — level counter gated on "work done this level," not
  loop iteration count
- Cycle Detection — undirected: global visited + parent-skip suffices.
  Directed: global visited alone gives false positives (converging paths in
  a DAG look identical to a real back edge) — needs path-state (3-color
  DFS: gray=on current path=cycle, black=finished branch=safe) or Kahn's
  in-degree BFS (count processed nodes == n at end, else cycle).
- Bipartite Check — color array (2 colors) instead of plain visited, flip
  color per edge walked, conflict = neighbor already colored same. Odd
  cycle length -> bipartite impossible (odd number of flips can't return to
  starting color, but closing edge forces same node = contradiction).
  Disconnected graphs need the outer-loop-over-all-nodes pattern (same as
  Number of Provinces) — single DFS/BFS from one node isn't enough.
- Topological Sort (DFS) — DFS on DAG, append node to list on exit/finish
  (not entry), reverse list at end. Plain visited array suffices (graph
  guaranteed acyclic, no need for 3-color). Equivalent to using an actual
  Stack and popping.
- Kosaraju's Algorithm (SCC) — 3 steps: (1) DFS for finish order/stack
  (topo sort step), (2) reverse all edges, (3) process nodes in finish-order
  (stack top first), DFS on reversed graph, each tree = one SCC. Why order
  matters: the node finishing LAST in step 1 has no incoming edges from
  other SCCs originally (all its cross-SCC edges point OUT) — after
  reversal those become incoming-only, so a DFS starting there is
  structurally trapped inside its own SCC, can't leak into another.
  Starting from a random/wrong node (e.g. mid-chain) risks walking a
  reversed bridge edge backward and wrongly merging two SCCs into one.
- Dijkstra — min-heap (dist,node), pop global min, skip stale entries, relax
  outgoing edges. "Pop = final" is safe only because non-negative weights make
  path-extension monotonic (never lowers a total) — the priority queue alone
  doesn't give this. See `../patterns/Dijkstra.md`.
- Bellman-Ford — edge-list relaxation, V-1 fixed rounds (a shortest path has
  ≤ V-1 edges), then a Vth round purely as a negative-cycle detector. Every
  loop that reads `dist[u]` needs an `dist[u] != INF` guard, or unreachable
  nodes produce fake finite path lengths. See `../patterns/BellmanFord.md`.

## Problems Log

- Min Cost to Connect All Points (Kruskal's/Prim's) — https://leetcode.com/problems/min-cost-to-connect-all-points/ — done (2026-08-01). Solved 3 ways: Kruskal's (PQ+Union-Find, `parent[0]` bug found+fixed), Prim's heap-based (relax-rule mistaken as cumulative, corrected), Prim's array-based O(n²) (first exposure, mentor-scaffolded). See [note](../notes/mst-min-cost-connect-points.md) and mistake_journal.
- BFS Traversal of Graph — 2026-07-25 — with-hints:1
- DFS Traversal of Graph — 2026-07-25 — with-hints:1
- Number of Provinces — 2026-07-25 — with-hints:1 (approach only)
- Number of Islands — 2026-07-25 — independently (approach only)
- Rotten Oranges — 2026-07-25 — with-hints:3 (approach only, multi-source BFS)
- Flood Fill — 2026-07-25 — with-hints:1 (approach only) — BFS, guard
  `newColor==originalColor`, source always repainted even if isolated
- Cycle Detection (Undirected, BFS) — 2026-07-25 — independently (approach
  only) — (node,parent) pairs, skip parent edge, visited-and-not-parent=cycle
- Cycle Detection (Directed, DFS) — 2026-07-25 — with-hints:1 (approach
  only, terminology only) — self-derived "check if node in current stack,"
  formalized as 3-color (white/gray/black); plain visited-array gives false
  positives on DAGs with converging paths (diamond shape)
- Cycle Detection (Directed, BFS / Kahn's) — 2026-07-25 — with-hints:1
  (approach only) — self-derived in-degree-zero queueing, needed 1 nudge on
  precise termination check (count processed == n vs < n)
- Bipartite Check (LC 785) — 2026-07-25 — with-hints:many (full code
  written and debugged) — approach (color array, flip on push) and
  same-color-conflict detection self-derived clean; odd-cycle "why" needed
  heavy Socratic escalation (light-switch-parity analog after 2 failed
  attempts). First code attempt missing outer loop over all nodes (only
  DFS'd from node 0) — disconnected-graph bug, self-fixed after being
  pointed at a disconnected-graph trace, no further issues.
- Topological Sort (DFS) — 2026-07-25 — with-hints:1 (approach only, code
  skipped — deliberately deferred to Kosaraju, which reuses this exact
  step). Recalled Kahn's (BFS) immediately; DFS-based approach needed 1
  nudge (which of two connected nodes finishes DFS first), then correctly
  derived finish-order + reverse cold, including that plain visited (not
  3-color) suffices since input's guaranteed acyclic.
- Kosaraju's Algorithm (SCC) — 2026-07-25 — with-hints:many (approach
  only, code skipped, heaviest derivation of the day). 3-step skeleton
  (DFS finish-order, reverse graph, DFS again in finish-order) recalled
  correctly unaided. "Why does processing order matter, not any random
  node" needed 3 escalation rounds — a 4-node 2-SCC-plus-bridge example,
  traced twice (correct-order vs wrong-order start), before landing on:
  last-finished node has no incoming cross-SCC edges originally, so after
  reversal it has no outgoing cross-SCC edges, trapping DFS inside its own
  SCC. Closed with a full, correct self-explanation.
- Dijkstra's Algorithm — 2026-07-26 (morning) — with-hints:many (approach
  only). Min-heap/relax/non-negative justification self-derived cold; stale-
  entry skip needed 1 nudge; complexity notation 3 escalation rounds;
  negative-edge failure mode needed a full guided trace (first answer
  conflated it with negative-cycle non-termination).
- Bellman-Ford Algorithm — 2026-07-26 15:28 — with-hints:several (full code
  written, GFG "Distance from the Source"). Derivation from the 10:20 session
  held. Code bugs: missing Vth detection round; `Integer.MAX_VALUE-1000`
  infinity fudge with no unreachable guard; then guard applied to the
  relaxation loop but not the identical detection loop (false negative-cycle
  on an unreachable component with a negative edge). Complexity O(V·E)/O(V),
  negative-weight condition, and the early-exit-variant trap (hangs forever
  on a negative cycle) all clean.
- Floyd-Warshall "why k outer" — 2026-08-01 16:32 — closed on the 5th
  attempt (07-26 through 08-01). Prim's/Kruskal's — 2026-08-01 — Kruskal's
  `parent[0]` accidental-default bug found+fixed; Prim's relax rule
  mistaken as cumulative (Dijkstra transfer), corrected via counterexample;
  array-based O(n²) Prim's needed mentor scaffold (first exposure). See
  mistake_journal and [note](../notes/mst-min-cost-connect-points.md).
- Course Schedule II (LC 210) — 2026-09-05 13:08 — independently, cold, no
  hints. Kahn's BFS, append-on-pop, cycle check via `ctr==numCourses`.
- Alien Dictionary (LC 269) — 2026-09-05 13:43 — with-hints:many. Approach
  (adjacent-word comparison -> Kahn's BFS) needed heavy escalation despite a
  prior "solved before" claim. 3 code bugs, see
  [note](../notes/alien-dictionary.md).
- Number of Enclaves (LC 1020) — 2026-09-05 13:57 — with-hints:1. Cold
  approach (multi-source boundary BFS), cold first code; visited-at-pop bug
  caused TLE, see [note](../notes/number-of-enclaves.md).

## Common Mistakes Seen in This Topic

- Marking `visited` too late (on dequeue/pop instead of on enqueue/push for
  BFS; on recursion-exit instead of recursion-entry for DFS) — causes
  duplicate processing or infinite recursion on cycles. See [[mistake_journal]]
  2026-07-25. Recurred a 3rd time on Flood Fill (self-caught via trace this
  time, no hint needed for the fix itself, 1 hint on isolated-cell edge case).
  **4th recurrence, Number of Enclaves (2026-09-05)** — this time it actually
  cost a TLE rather than being self-caught; the rule was already written in
  this file and not applied before coding.
- Sentinel-infinity arithmetic — treating `INF` as a number rather than "no
  path exists," so `dist[u]+wt` yields a fake finite value. Guard every loop
  that reads `dist[u]`, not just the first one you fix. Bellman-Ford
  2026-07-26.
- Clean derivation in one session not surviving into code in a later session
  (Bellman-Ford's Vth detection round derived 10:20, absent from the 15:28
  code draft) — re-read derivation notes before coding a deferred algorithm.
- Algorithms sharing a code skeleton (Prim's/Dijkstra: both frontier-PQ,
  pop-mark-relax) pattern-matching the wrong differing line from whichever
  was drilled more recently — Prim's relax rule (raw edge weight) mistaken
  for Dijkstra's (cumulative from source), 2026-08-01. Say the one
  differing line out loud before coding, don't assume shared skeleton means
  shared formula.

## Cut-list queue — itemized 2026-08-31 (Day 0)

From `Progress/coverage_cut_list.md`. `- [ ]` = scheduled, not yet solved.

**12 slots; 7 named in the cut list, 5 unnamed ("shortest path variants").**
Core algorithms (Dijkstra, Bellman-Ford, topo sort, Union-Find) are already
covered — this bucket is the classic *problem* set only.

- [ ] Word Ladder (LC 127)
- [ ] Surrounded Regions (LC 130)
- [x] Course Schedule (LC 207) — solved with-hints:1, 2026-09-03. Kahn's BFS,
  indegree-direction bug (wrong node incremented), found via trace.
- [x] Course Schedule II (LC 210) — solved independently, 2026-09-05, no hints.
- [x] Alien Dictionary (LC 269) — solved with-hints:many, 2026-09-05. 3 code
  bugs (cast-precedence, prefix-check order, distinct-letter count).
- [x] Number of Enclaves (LC 1020) — solved with-hints:1, 2026-09-05.
  Visited-at-pop bug -> TLE.
- [ ] TBD x6 — "shortest path variants", unnamed in the cut list
