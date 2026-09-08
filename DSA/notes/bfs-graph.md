---
type: note
problem: BFS Traversal of Graph
topic: Graph
updated: 2026-07-25
---

First code draft marked `visited[val]=true` on poll (pop) and pushed neighbors
without checking `visited` first — contradicted the derivation just done
verbally (mark visited at push time to avoid duplicate queue entries when two
unprocessed nodes share a neighbor). Self-corrected once asked to compare code
against own derivation. Fixed version: check `visited[nodes]` before push,
set `visited[nodes]=true` immediately, then push.

Complexity: O(V+E) time, O(V) space.
