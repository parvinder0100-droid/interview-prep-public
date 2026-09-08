---
type: pattern
pattern: TwoPointers
updated: 2026-08-27
status: in-use
---

# TwoPointers

## When This Pattern Applies

In-place array compaction/partition problems (keep some elements, drop/move
others, no extra array) — dedup, move-to-end, or multi-way partition by
category (0s/1s/2s).

## Core Idea

Default to comparing the scanner pointer against the *last-confirmed-good*
pointer (not the *next* element) — generalizes cleanly to the end of the array
with no special-casing. For 3-way partition (Dutch National Flag), reason about
the invariant by elimination (what's provably NOT in the untouched middle
zone), not induction — elimination framing lands better here.

## Problems Using This Pattern

- Trapping Rain Water (LC 42), O(1)-space version — Hard — 2026-08-27 —
  converging pointers each carrying a running max. The transferable idea:
  **a variable that is exact for its own pointer and a lower bound for the
  other is still enough**, because the branch condition guarantees the exact
  side is the one the `min` selects. See [note](../notes/trapping-rain-water.md).

- Remove Duplicates from Sorted Array — Arrays/Two Pointers — solved 2026-07-11.
- Move Zeroes to End — Arrays/Two Pointers — solved 2026-07-11.
- Sort Array of 0s, 1s, 2s (Dutch National Flag) — Arrays/Medium — 3-pointer
  variant, solved 2026-07-12.

## Common Pitfalls

- Comparing scanner against the *next* element instead of the last-confirmed
  pointer — forces an ugly last-element special case. Compare against the
  last-confirmed pointer instead.
- Only handling the front compacted region, forgetting the postcondition on
  the *rest* of the array (e.g. Move Zeroes needs the tail explicitly zeroed,
  not just left with stale values).
- Dutch National Flag: treating the 0-swap and 2-swap cases as symmetric on
  whether `mid` advances — 0-swap brings a *known* value into `mid` (safe to
  advance), 2-swap brings an *unknown* value from the unprocessed region
  (must not advance).
