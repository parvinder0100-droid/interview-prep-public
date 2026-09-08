---
type: pattern
pattern: Dijkstra
updated: 2026-07-26
status: in-use
---

# Dijkstra

## When This Pattern Applies

Single-source shortest path, weighted graph, all edge weights non-negative.

## Core Idea

Min-heap of (dist, node). Push (source, 0). Pop global min; if popped dist >
recorded `dist[node]`, it's stale, skip. Otherwise relax all outgoing edges:
if `dist[node]+weight < dist[neighbor]`, update and push. Non-negative
weights guarantee that once a node is popped as the global min, no later
path (which must add ≥0 per edge) can beat it — that's what makes "pop =
final" safe. Breaks immediately with even one negative edge (see Common
Pitfalls) — use Bellman-Ford instead for that case.

## Problems Using This Pattern

- Dijkstra's Algorithm — 2026-07-26 — core mechanics self-derived cold;
  complexity notation and negative-edge failure mode both needed real
  escalation. See mistake_journal.

## Common Pitfalls

- Complexity: total ops ≤ E pushes/pops, each O(log heap-size) = O(log V) →
  O(E log V) overall, not some garbled V/E mix — derive from operation
  counts, don't recite a remembered formula.
- Negative edge (no cycle): a node can pop, get locked in (visited) at a
  distance that's later beaten by a very negative edge from a
  later-processed node — silently wrong answer, not an infinite loop.
  Infinite loop is the *negative-cycle* failure mode, a different thing.
- Removing the visited-lock (compare-dist-only) fixes correctness but
  destroys the O(E log V) bound — unbounded re-relaxation possible. Don't
  patch Dijkstra for negative weights; switch to Bellman-Ford.
