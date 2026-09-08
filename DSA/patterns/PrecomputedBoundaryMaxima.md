---
type: pattern
pattern: PrecomputedBoundaryMaxima
status: in-use
updated: 2026-08-26
---

# Precomputed Boundary Maxima

Two linear passes build, for every index, the best (max/min) value strictly to
its left and strictly to its right. A third pass answers a per-index question
in O(1) using both. O(n) time, O(n) space; often collapsible to O(1) space with
two pointers once you see that only the smaller side's max is ever binding.

## When it applies

The answer at index `i` depends on an aggregate over *all* of one side, not on
the nearest qualifying element. That distinction is the whole pattern — if the
answer depends on the nearest qualifying element, it is [[MonotonicStack]]
instead.

**Test to tell them apart**: does an intervening element that fails the
predicate block the far one? If it blocks -> nearest -> monotonic stack. If it
does not -> aggregate -> this pattern.

## Problems Using This Pattern

- Trapping Rain Water (LC 42) — 2026-08-26 — `min(maxLeft, maxRight) - h[i]`,
  clamped at 0, summed. The short bar between does NOT block: it is submerged
  to the same level. See [note](../notes/trapping-rain-water.md).

## Common Pitfalls

- Reaching for nearest-greater/nearest-smaller because the problem sits in the
  Stack chapter. Run the blocking test above before picking — 2026-08-26.
- Forgetting the clamp: any index taller than the lower of its two walls gives
  a negative contribution (both endpoints, plus every local peak).
- Multiplying by a width. These sums are per-column, width 1 — the area
  multiply belongs to Largest Rectangle in Histogram, not here.
