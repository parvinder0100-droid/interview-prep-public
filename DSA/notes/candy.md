---
type: note
problem: Candy (LC 135)
topic: Greedy / Two-Pass Constraint Propagation
updated: 2026-08-09
---

# Candy (LC 135)

https://leetcode.com/problems/candy/

Approach closed 2026-08-09, **code not written**. Pattern:
[[TwoPassConstraintPropagation]].

## What came out cold

- The n-candy floor.
- Two-pass structure, unprompted.
- Both passes computed correctly on `[1,3,2,1]` (left `[1,2,1,1]`, right
  `[1,3,2,1]`), and the merged value at index 1.
- The `max` merge rule.
- **Minimality**: `left[i]` counts the increasing run ending at i, so any valid
  assignment has `v[i] ≥ left[i]`.
- O(n)/O(n), and that the right pass needs no array of its own.

## What broke

- `[1,0,2]` allocated as `1,1,2` — only the right-hand neighbour was checked.
  Self-corrected in one nudge.
- **Validity of the merge.** The question "does `c[i] > c[i-1]` survive the max
  when `c[i-1]` might come from the right pass" produced two "i don't get it"
  and one "no idea". What unblocked it, in order: instantiate on `[1,3,2,1]` →
  ask what the right pass gives index 0 and why → generalize to `right[i-1] = 1`
  whenever the left constraint binds at i → number-level analog `max(a,b) ≥ a`
  → assemble the chain one link at a time. The user then stated it correctly:
  `c[i] ≥ left[i] = left[i-1] + 1 > left[i-1] = c[i-1]`.
- "Is O(1) space reachable?" answered "no" reflexively; the run-length idea
  landed on one targeted question, but the shared-peak detail did not, and the
  variant was parked.

## Next session

1. Write the code (one-array version: store the left pass, accumulate the right
   pass on the fly).
2. Optional: finish or drop the O(1) run-length variant — the two-pass answer
   is interview-sufficient.
