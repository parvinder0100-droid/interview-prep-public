---
type: note
problem: Asteroid Collision (LC 735)
status: SOLVED 2026-08-24 (with-hints:4) — failed cold 2026-08-23
---

# Asteroid Collision (LC 735)

https://leetcode.com/problems/asteroid-collision/

## Status

Attempted cold 2026-08-23 (~10 min): failed, 2 bugs, left open. Re-attempted
cold 2026-08-24 (~20 min writing + ~7 min Socratic): solved. O(n)/O(n).

## The one condition

Only `stackTop > 0 && cur < 0` is a collision. A left-mover already on the
stack and a later right-mover **diverge** — the gap opens every tick, they
never meet. Modelling collision as sign-opposite in either order is what
breaks `[-2,-1,1,2]`.

## Bug 1 — symmetric collision (reproduced on the cold re-attempt)

08-23's note named this defect explicitly. The 08-24 cold restart shipped it
again, verbatim: `stTop<0&&cur>=0 || stTop>=0&&cur<0`. Reading the diagnosis
did not encode it.

What did encode it: putting the pair on a number line with positions.

    t=0:   -1 at 0        +2 at 5     gap 5
    t=1:   -1 at -1       +2 at 6     gap 7

One trace, condition derived immediately. Abstract sign-reasoning had failed
twice by that point.

## Bug 2 — equality unhandled after the cascade (new, found 08-24)

Equality was tested only in the `if` *before* the pop-loop. After the `while`
pops smaller asteroids, the incoming one faces a **new** top that was never
re-tested for equality.

    [10, 2, -10]   expected []   got [10, -10]

Fix: re-test both `<` and `==` against the surviving top after the loop.

## Complexity

O(n) time — each asteroid is pushed once and popped at most once, so total
pops ≤ n regardless of the nested `while`. O(n) space.

## Edge cases worth keeping

    [-2,-1,1,2]    diverging pairs, nothing collides
    [8,-8]         equality at the first comparison
    [10,2,-10]     equality reached only after a cascade
    [1,-2,-3]      stack empties mid-cascade, then pushes
