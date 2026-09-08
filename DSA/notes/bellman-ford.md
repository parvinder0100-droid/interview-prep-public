---
type: note
problem: Bellman-Ford Algorithm
topic: Graph/Shortest Path
solved: 2026-07-26 15:28
---

# Bellman-Ford

GFG "Distance from the Source (Bellman-Ford Algorithm)" — return dist array
from src, or `[-1]` if a negative cycle exists.

## What went wrong (code, not derivation)

Derivation was clean the session before. Three code-level defects:

1. **Vth detection round missing entirely.** The V-1 bound and the extra
   detection pass were both derived correctly at 10:20; only the V-1 loop made
   it into the code.
2. **`Integer.MAX_VALUE-1000` as infinity, no unreachable guard.** The `-1000`
   is a fudge to stop `INF + wt` wrapping negative. It fails for any
   `wt > 1000`, and a wrapped-negative reads as a huge improvement, so it
   relaxes everything downstream to garbage.
3. **Guard applied asymmetrically.** After adding `dist[u] != INF` to the
   relaxation loop, the structurally identical detection loop still lacked it.

## The trace that exposed defect 3

```
V = 4, src = 0
edges = [[0,1,4], [2,3,-5]]

   [0] --4--> [1]        [2] --(-5)--> [3]
   (reachable)           (unreachable, no cycle anywhere)
```

Detection loop hits `[2,3,-5]`: `dist[2] = dist[3] = 1e8`, so
`1e8 - 5 < 1e8` is **true** → returns `[-1]` on a graph with no cycle at all.

## The idea to keep

`dist[u] + wt` claims "length of some path source→u→v." If `dist[u]` is the
sentinel, there is no source→u path, so that number describes a path that does
not exist — it only looks finite because `1e8` is a real integer, not true
infinity. Guard **every** loop that reads `dist[u]`.

Sentinel choice: `1e8` is required by GFG's output contract for unreachable
nodes. With the guard in place `Integer.MAX_VALUE` would not overflow — the
guard, not the sentinel value, is what makes it safe.

## Why fixed V-1 rounds, not loop-until-stable

Early-exit (`while (changed)`) gives the same answer and is often faster on
graphs with no negative cycle — worst case is still V-1 passes, so `O(V·E)` is
unchanged.

But on a graph **with** a negative cycle, some `dist` improves on every pass,
so `changed` is never false and the loop never terminates. The fixed V-1 bound
plus a Vth pass used purely as a detector is what makes termination
unconditional and lets you *report* a negative cycle instead of hanging.

Interview phrasing: "Early exit is a valid optimization when the graph is
guaranteed free of negative cycles, but the fixed bound plus a detection pass
is what lets you report them."

## Complexity

- Time `O(V·E)` — V-1 passes over all E edges.
- Space `O(V)` — the dist array; the edge list is input, not extra.

Versus Dijkstra `O(E log V)`: use Dijkstra when all weights are non-negative.
Reach for Bellman-Ford when negative weights exist, or when you need to
*detect* a negative cycle (Dijkstra cannot). See
[[../patterns/BellmanFord]] and [[../patterns/Dijkstra]].
