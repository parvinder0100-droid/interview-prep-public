---
type: pattern
pattern: StackSimulationDirectional
updated: 2026-08-24
status: in-use
---

# StackSimulationDirectional

## When This Pattern Applies

Sequential items that carry a **direction** and interact only with the most
recent surviving neighbour — asteroid collisions, particle annihilation,
token/bracket destruction with strength. Distinct from MonotonicStack: the
stack here is not kept ordered, it holds survivors.

## Core Idea

The stack holds everything that has survived so far. For each incoming item,
resolve it against the top repeatedly until it either dies, destroys the top
and continues, or the interaction condition goes false — then push.

**Derive the interaction condition first.** It is almost never symmetric.
Asteroid Collision: only `top > 0 && cur < 0` collides; the reverse pair
diverges and never meets.

## Skeleton

    for each item:
        while stack non-empty AND interacts(top, item) AND item wins:
            pop
        if stack non-empty AND interacts(top, item):
            if tie: pop; item also dies; continue outer
            else:   item dies; continue outer
        push item

Both the tie test and the loss test must appear **after** the loop — the
cascade exposes a new top that the pre-loop tests never saw.

## Complexity

O(n) time, O(n) space. Amortized: pushed once, popped at most once.

## Problems Using This Pattern

- Asteroid Collision (LC 735) — 2026-08-24, with-hints:4 (failed cold 08-23)

## Common Pitfalls

- Treating the interaction as symmetric in the sign/direction test — breaks
  `[-2,-1,1,2]` (2026-08-23, repeated 2026-08-24).
- Testing equality/loss only before the pop-cascade — breaks `[10,2,-10]`
  (2026-08-24).
- Reasoning about direction from signs abstractly. Put positions on a number
  line and advance one tick; the condition falls out immediately.
