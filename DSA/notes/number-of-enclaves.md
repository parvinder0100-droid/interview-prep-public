---
type: note
problem: Number of Enclaves (LC 1020)
updated: 2026-09-05
---

Multi-source BFS from every boundary land cell, mark reachable land, count
land cells left unmarked.

**Bug — visited-at-pop instead of visited-at-push**: `grid[cur[0]][cur[1]]=2`
ran at dequeue time, not when the cell was added to the queue. A cell can be
discovered (and enqueued) by more than one neighbor before it's popped, since
the `==1` check that gates enqueuing doesn't see the mark until pop —
duplicate enqueues, TLE on larger grids. Fix: mark `2` at the moment of
`q.add(...)`, both in the boundary-init loop and the BFS expansion.

This is the same rule already written in `../topics/Graph.md`'s Common
Mistakes ("visited-at-push (BFS) / visited-on-entry (DFS)") — 4th recurrence
of that exact pattern, first time it actually cost a failing run instead of
being self-caught.
