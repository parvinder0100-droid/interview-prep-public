---
type: note
problem: Bipartite Check (LC 785)
topic: Graph
updated: 2026-07-25
---

Approach (color array, flip color per edge, conflict=same-color-adjacent)
self-derived clean. Odd-cycle "why" needed heavy escalation — 2 failed
attempts before a light-switch parity analog landed: walking a cycle flips
color once per edge; L flips must return to the start node's original color,
so L must be even. Odd L forces a contradiction at the closing edge.

Code bug: first draft only called `dfs(graph, color, 0, 1)` — single start
node, missed disconnected components (e.g. isolated nodes never colored,
trivially "bipartite" without ever being checked). Self-fixed after tracing
a disconnected graph: added `for(i=0;i<v;i++) if(color[i]==0) dfs(...)`,
same outer-loop-over-all-nodes pattern as Number of Provinces.

Complexity: O(V+E) time, O(V) space.
