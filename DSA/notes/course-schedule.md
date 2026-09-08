---
type: note
problem: Course Schedule (LC 207)
updated: 2026-09-03
---

Kahn's BFS topological sort, used as cycle detection (`done == numCourses`).

**Bug**: `indegree[pre[1]]++` instead of `indegree[pre[0]]++`. `pre = [a, b]`
means edge `b -> a` (b is prerequisite for a), so `graph[b].add(a)` is right,
but the indegree belongs to `a` (the dependent node), not `b`. Swapping this
silently breaks simple 2-node cases (`n=2, [[1,0]]` returns false instead of
true) without throwing — found only by tracing a concrete small case, not by
inspection.

**Confirmed by removing it**: the inner `size`-snapshot layering (multi-source
level-BFS shape) is not needed for this problem — order/depth is irrelevant,
only whether every node's indegree eventually hits 0. A plain single-poll BFS
gives the same answer. Don't reach for the level-layering template out of
habit when the problem doesn't need levels.
