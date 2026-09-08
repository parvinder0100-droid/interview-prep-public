---
type: pattern
pattern: BoundaryShrinkingTraversal
updated: 2026-07-20
status: in-use
---

# BoundaryShrinkingTraversal

## When This Pattern Applies

Ring/spiral-style matrix traversal problems using 4 shrinking boundary
pointers (top/bottom/left/right).

## Core Idea

Remaining cells = `(bottom-top+1)*(right-left+1)` — a product, zero if either
factor collapses. Outer loop stop condition: `top<=bottom && left<=right`
(AND, not OR — either dimension collapsing means zero cells regardless of the
other). Each of the 4 passes needs a guard checking the dimension the
*previous* pass just shrank (pass 2 guards `top<=bottom` since pass 1 shrank
rows; pass 3 guards `left<=right` since pass 2 shrank columns; pass 4 guards
`top<=bottom` again). Without per-pass guards, a collapsed single row/column
already fully printed by an earlier pass gets printed again. Boundaries always
shrink toward center, never grow.

## Problems Using This Pattern

- Spiral Traversal — Arrays/Matrix/Medium — solved 2026-07-13.

## Common Pitfalls

- Missing or wrong per-pass guards — standing weak spot, regressed twice
  (review #1 2026-07-17 one hint, review #2 2026-07-20 three separate errors:
  wrong guard dimension for pass 3, `bottom++` instead of `bottom--`, and
  swapped pass 3/4 direction descriptions).
- Rehearse the rule as "guard checks the dimension the PREVIOUS pass just
  shrank" rather than memorizing which specific comparison goes where — the
  specific-comparison memorization is what keeps failing to stick.
