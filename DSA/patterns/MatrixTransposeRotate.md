---
type: pattern
pattern: MatrixTransposeRotate
updated: 2026-07-20
status: in-use
---

# MatrixTransposeRotate

## When This Pattern Applies

In-place 90°-rotation of a square matrix, no extra matrix allowed.

## Core Idea

Two-step decomposition: (1) transpose — `arr[i][j] <-> arr[j][i]` for `i != j`
only (diagonal elements have `i==j`, stay fixed, must be a no-op); (2) reverse
each row **fully**, end-to-end (e.g. `[1,2,3,4]` -> `[4,3,2,1]`, not just
swapping the two endpoints). Transpose alone gives columns-as-rows; the full
row-reverse then produces the 90° clockwise result.

## Problems Using This Pattern

- Rotate Matrix (90°, in-place) — Arrays/Matrix/Medium — solved 2026-07-12
  with full derivation (genuine new-material gap at the time).

## Common Pitfalls

- Standing repeat-rust: forgetting the row-reverse must be a *full* reverse,
  not just swapping the two end elements — recurred at review #1 (2026-07-13),
  did NOT recur at review #2 (2026-07-17), so the explicit-phrase rehearsal
  fix appears to be holding.
- New slip at review #2 (2026-07-17): applying the transpose swap to a
  diagonal position (`i==j`) instead of skipping it — diagonal elements must
  stay fixed.
