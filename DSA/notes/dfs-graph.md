---
type: note
problem: DFS Traversal of Graph
topic: Graph
updated: 2026-07-25
---

Initially proposed marking `visited` on recursion-exit ("while coming out")
instead of recursion-entry. Corrected via counterexample: nodes 0-1 mutually
connected — `dfs(0)` recurses into `dfs(1)` before 0 is marked, so 1's
neighbor-list check on 0 would re-enter it (infinite recursion on cycles).
Fixed: mark `visited[src]=true` as the first thing inside the recursive call,
before the neighbor loop. Code was clean once this was corrected.

Also confirmed: `visited` doesn't need to be an instance field — passing it
as a param through the recursive calls works identically (Java arrays pass by
reference), just declare it locally in the wrapper method instead.

Complexity: O(V+E) time, O(V) space (recursion stack).
