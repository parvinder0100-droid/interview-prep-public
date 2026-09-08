---
type: note
problem: Sort Array of 0s, 1s, 2s (Dutch National Flag)
topic: Arrays/Medium
updated: 2026-07-12
---

# Sort 0s, 1s, 2s (DNF)

## Pointers

- `low`: everything `< low` is confirmed 0.
- `mid`: scanner, everything in `[low, mid-1]` is confirmed 1.
- `high`: everything `> high` is confirmed 2.
- Loop while `mid <= high`.

## Rules

- `arr[mid]==0`: swap(low,mid), `low++`, `mid++`
- `arr[mid]==1`: `mid++`
- `arr[mid]==2`: swap(mid,high), `high--` (mid stays — swapped-in value from
  `high` is unknown, needs recheck)

## Why 0-swap Can Advance `mid` but 2-swap Can't

`arr[low]` is always the front of the already-confirmed 1-zone (or the zone
is empty and `low==mid`), so swapping it into `mid` brings a *known* 1 — safe
to advance `mid`. The 2-swap brings in an *unknown* value from the
unprocessed region beyond `high` — must not advance `mid`.

## Why `[low, mid-1]` Is Always All 1s (elimination argument)

Every index `< mid` has already been examined and classified as 0, 1, or 2.
- Classified 0 → shipped to before `low` (that's the 0-zone).
- Classified 2 → shipped to after `high` (that's the 2-zone) — a 2 is never
  left behind in the middle, it's relocated the instant it's found.
- So whatever's left behind in `[low, mid-1]`, unrelocated, can only be 1 —
  by elimination, not by tracking.

## Mistake Made

Got the swap-asymmetry rule right after one hint, but had no understanding
of *why* the invariant holds. Induction framing (base case + inductive step)
didn't land — the elimination-argument framing (what's NOT true about the
leftover region) is what finally worked. Worth defaulting to elimination
framing for partition/invariant explanations generally.

## Complexity

O(n) time, O(1) space, single pass.
