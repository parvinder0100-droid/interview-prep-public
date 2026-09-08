---
type: note
problem: Rotten Oranges
topic: Graph
updated: 2026-07-25
---

Multi-source BFS: push all initially-rotten cells first, then level-order BFS,
1 minute per level. -1 check: after BFS, scan for any fresh orange left
(equivalently, track a `freshCount` decremented on each conversion, -1 if
nonzero at end).

Minute-counter bug chain (3 iterations to the correct rule):
1. "Increment every level" — overcounts by 1 when there are 0 fresh oranges
   (e.g. `[[2]]`), since the initial rotten-only level still counts as a level.
2. Patch: "if initial queue size == total cells, return 0" — only handles the
   all-rotten case, still breaks on `[[2,0],[0,0]]` (rotten + empty, no fresh).
3. Patch: "increment if queue size > 1 after processing" — wrong threshold,
   breaks on `[[2,1]]` (exactly 1 fresh converted, answer should be 1, queue
   size after = 1, not > 1).
4. Correct: increment only if **at least one node was pushed during this
   level** (something was actually converted) — decouples the counter from
   queue size entirely.

Complexity: O(m·n) time, O(m·n) space.
