---
type: pattern
pattern: TwoPassConstraintPropagation
status: in-use
updated: 2026-08-09
---

# Two-Pass Constraint Propagation

Each element carries a lower bound imposed by its left neighbour and another
imposed by its right neighbour. One sweep per direction computes each bound
independently; the answer per element is the **max** of the two. Created
2026-08-09 on Candy (LC 135), after the user asked directly how it differs
from the greedy work done so far — the distinction is worth keeping.

## Not Selection-Order Greedy

Everything else logged under Greedy so far (N Meetings, Job Sequencing,
Fractional Knapsack) is *selection-order* greedy: sort by a key, pick items one
at a time, justify with [[GreedyExchangeArgument]]. This pattern has no sort,
no selection, and no exchange argument — the justification is a lower-bound
argument instead (below). Filed under Greedy by Striver; the reusable idea is
"bidirectional local constraint → one sweep per direction → merge."

Same family: Trapping Rain Water (maxLeft / maxRight), Product of Array Except
Self (prefix / suffix products).

## The Shape

1. Left-to-right sweep: `left[i] = left[i-1] + 1` when the left constraint
   binds at i, else the base value.
2. Right-to-left sweep, symmetric.
3. `c[i] = max(left[i], right[i])`.

The second sweep does not need its own array — it can carry a running counter
and accumulate `max(left[i], running)` into the total on the fly. O(n) time,
O(n) space, or O(1) with a run-length formulation (see Open below).

## Why `max` Is Correct

**Valid.** Suppose the left constraint binds at i. Then the *right* pass leaves
`right[i-1]` at its base value, so `c[i-1] = left[i-1]`, and
`c[i] ≥ left[i] = left[i-1] + 1 > left[i-1] = c[i-1]`. Symmetric on the other
side. The non-obvious step is that the two passes cannot fight: whichever
constraint binds at i pins where `c[i-1]` takes its value from.

**Minimal.** `left[i]` counts the length of the run ending at i, and along a
strictly increasing run each element must exceed the previous with the first at
the base value — so *any* valid assignment has `v[i] ≥ left[i]`, symmetrically
`v[i] ≥ right[i]`, hence `v[i] ≥ c[i]` everywhere. `c` is valid and pointwise
minimal, therefore optimal.

## Problems Using This Pattern

- Candy (LC 135) — 2026-08-09 — approach closed, code open. Minimality half
  derived cold; validity half needed the full escalation ladder.

## Common Pitfalls

- Checking the constraint against one neighbour only when validating a
  candidate allocation (`[1,0,2]` → `1,1,2`) — 2026-08-09.
- Arguing the merge is valid by restating what each pass guarantees *alone*,
  which says nothing about what survives the `max` — 2026-08-09.
- Summing the two passes instead of taking the max (valid, not minimal).

## Open

O(1)-space run-length variant: sweep once, add the arithmetic series over each
up-run and down-run. Unresolved detail — the peak is shared by both runs and
must be counted once, at `max(up, down)`. Parked 2026-08-09.

## Flashcard-worthy

Q: Two passes give element i a lower bound from each side — why is the max of
them valid, not just a heuristic?
A: Whichever constraint binds at i forces the neighbour's value to come from
the *same* pass, so that pass's strict inequality survives the max.
