---
type: note
problem: Longest Consecutive Sequence
topic: Arrays/Medium
updated: 2026-07-12
---

# Longest Consecutive Sequence

## Algorithm

1. Build a hash set from the entire array (full pass, upfront).
2. For each element `x` in the array: check if `x-1` is in the set. If not,
   `x` is a sequence start — expand rightward (`x+1, x+2, ...`) checking set
   membership, tracking length. If `x-1` IS in the set, skip — `x` will be
   covered by some earlier element's expansion.
3. Track the max length seen across all expansions.

## Why This Is O(n), Not O(n²)

Naively expanding from every element is O(n²) worst case (e.g. one long run
`[1,2,3,4,5]` — starting from every element and walking the full remaining
run each time). The `x-1 not in set` check ensures expansion only starts
from true sequence starts — every element then gets visited in exactly one
expansion across the whole run, giving true O(n).

## Order Independence

The hash set is built completely upfront, before any expansion. So even if
`2` appears before `1` in the array and gets processed first, checking
`1 in set` at that point still returns true (the set is already complete) —
`2` correctly gets skipped as a non-start, and nothing is lost, because `1`
will still get its own turn in the loop and trigger the full expansion
through `2, 3, ...` when it's reached.

## Mistake Made

Initial approach expanded from every element (O(n²)), self-corrected the
complexity claim from "amortized O(n)" to O(n²) after counting operations.
Then needed a nudge to find the `x-1 not in set` pruning rule, plus a
follow-up clarification on why processing order in the array doesn't matter
given the set is built upfront.

## Complexity

O(n) time, O(n) space.
