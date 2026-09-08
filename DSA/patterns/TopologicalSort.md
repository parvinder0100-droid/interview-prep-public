---
type: pattern
pattern: TopologicalSort
updated: 2026-09-05
status: in-use
---

# TopologicalSort

## When This Pattern Applies

DAG (directed, acyclic), need an ordering where every edge u→v has u before
v. Also the finish-order backbone Kosaraju's algorithm reuses.

## Core Idea

BFS (Kahn's): repeatedly pull nodes with in-degree 0, decrement neighbors'
in-degree. DFS: recurse, append node to a list on exit/finish (not entry),
reverse the list at the end (or use an actual Stack and pop). Plain visited
array suffices for DFS version — input's guaranteed acyclic, no 3-color
needed (contrast with cycle detection on unknown-acyclic-or-not graphs).

## Problems Using This Pattern

- Topological Sort (DFS) — 2026-07-25 — 1 nudge on which of two connected
  nodes finishes DFS first.
- Kosaraju's Algorithm (SCC) — 2026-07-25 — step 1 reuses this exact
  DFS-finish-order step.
- Course Schedule (LC 207) — 2026-09-03 — Kahn's BFS as cycle detection
  (`done == numCourses`); indegree-direction bug, see pitfalls.
- Course Schedule II (LC 210) — 2026-09-05 — same skeleton, append node to
  result on pop. Cold, clean, no hints.
- Alien Dictionary (LC 269) — 2026-09-05 — edges from adjacent-word
  comparison instead of direct prerequisite pairs; 26-letter graph. See
  pitfalls (prefix-check order, distinct-node counting).

## Common Pitfalls

- Pushing/appending on entry instead of exit — inverts the order.
- Reaching for 3-color state out of cycle-detection habit — unnecessary
  here since the graph's already guaranteed acyclic.
- Kahn's BFS: for edge `[a, b]` (b prerequisite of a), `indegree[a]++` not
  `indegree[b]++` — the indegree belongs to the dependent node. Wrong
  direction breaks small cases silently, only caught by tracing.
- The inner `size`-snapshot level-layering (multi-source BFS shape) is not
  needed here — cycle detection only cares whether every node's indegree
  reaches 0, not depth/order. A plain single-poll BFS is sufficient.
- When edges come from pairwise word comparison (Alien Dictionary): find the
  first differing character *before* checking which word is shorter — a
  length check that runs first wrongly flags real edges as invalid prefix
  cases. The prefix-invalid case only applies when the scan finds no
  difference at all.
- Cycle-detection counter must count **distinct nodes**, not total input
  occurrences — snapshotting `indegree[i]==0` across all slots before any
  edges are added gives the right count; incrementing once per raw input
  token (e.g. once per character across all words) overcounts and the
  counter never reaches 0.
