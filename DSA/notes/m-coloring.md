---
type: note
problem: M-Coloring Problem (GFG)
topic: Recursion / Backtracking (graph variant)
date: 2026-08-31
result: Accepted 1114/1114, 3rd submission, with-hints:6
---

# M-Coloring — the derivation was right, the code was the old version

Link: https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1
(the bare slug without the trailing `/1` 404s).

## What the session actually showed

Both of the cycle's named content defects appeared in the spoken approach and
**both were self-corrected**, one of them cold:

1. **Legality as "differs from the previous node."** Closed by one traced
   instance on `0-1, 1-2, 2-3, 3-0, 0-2`: colour `0,1,2` red/green/blue, arrive
   at vertex 3, whose row is `{0, 2}` — the rule checks only 2, so 3 takes red
   and collides with 0. Restated correctly: *reads `color[neighbor]` for every
   neighbor in `graph[curNode]`*.
2. **Greedy-first-match, 3rd occurrence** ("on conflict return false"). One
   question — "does that prove the graph can't be coloured?" — produced "no, we
   should try other colors for previous nodes", and the pre-code check ("which
   line brings control back here?") was answered unprompted: *the recursive call
   returns false, so the loop tries the next color*. **First time this family
   closed without escalation.**

Then the code was written with `if(i != prvNodeColor)` — the rule discarded two
minutes earlier. That is the finding: **derivation-to-code regression**, and the
gap was minutes, not the 16 hours logged on 08-29.

## The three judge-visible defects, all mechanical

    for(int kids : graph[curNode]){        // scan runs
        if(color[kids]==i) continue;       // ...advances THIS loop
    }                                      // verdict discarded

`continue` targets the loop it sits in. The scan wrote to nothing, so every
colour was accepted. Fixed with `boolean isValid` + `break`.

**WA 1/1114** — `V=2, edges=[[0,1],[0,0]]`, expected true, got false. The
vestigial `if(color[curNode]==prvNodeColor) return false` survived the redesign;
on the self-edge the recursion re-enters vertex 0 carrying vertex 0's own colour,
so the guard is trivially true. Deleting the guard *and* the parameter fixed it.

**WA 6/1114** — `V=3, single edge 1-2, m=1`, expected false, got true.
`graphColoring` ended in `return dfs(graph,color,m,0,-1)`. Vertex 0 is isolated,
`graph[0]` is empty, the kids loop never runs, `res` stays true. Vertices 1 and 2
were never visited. Fixed by looping `i` over `0..V-1` with `res &= dfs(...)`.

**This exact trace had been posed 4 minutes before the first submission and
parked** ("i will have to come back at this question later"). The judge then
delivered it as the failing case. Worth remembering as an argument for finishing
a trace rather than parking it.

## Open

- **Complexity was never reached** — "no idea", session ended there. `m^V`
  assignments, `O(degree)` scan per node, `O(V)` colour array + `O(V)` depth.
  First item of the 2026-09-01 review.

## Shape worth keeping

Driver loops every vertex (graphs are not guaranteed connected); the recursive
frame scans the adjacency row for legality, assigns, recurses, and resets to `0`
on failure before trying the next colour. The undo was named correctly and
unprompted — `color[curNode]=0` — and was the one part that went in clean.
