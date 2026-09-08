---
type: pattern
pattern: StackAugmentedState
updated: 2026-07-21
status: in-use
---

# StackAugmentedState

## When This Pattern Applies

"Track running min/max/aggregate alongside a stack, with O(1) query" problems
— where a single global variable would break because it can't un-learn a
value once the element holding it pops off.

## Core Idea

Store the aggregate (e.g. `minSoFar`) alongside the value in each stack
frame, not in one global variable. On push: new frame's aggregate =
`combine(currentValue, previous top's aggregate)`. On query: read straight
off the top frame. On pop: the aggregate "reverts" automatically, since the
frame carrying the stale aggregate is gone and the new top still holds the
correct aggregate for what's left.

## Problems Using This Pattern

- Min Stack — Stack/Queue/Medium — solved 2026-07-20, mechanics correct
  independently; the "why not a global var" derivation needed real
  escalation at review #1 (2026-07-21), see mistake_journal.

## Common Pitfalls

- Defaulting to one global tracking variable — works for push but silently
  goes stale on pop (can't un-learn a min once its element is popped).
  Concrete counterexample: push 2, push 5, push 1 (global→1), pop 1 → global
  still says 1, true remaining min is 2.
- Reasoning about only the push side when asked "why not global" — the real
  justification is entirely about pop-time correctness.

## Variant: two stacks instead of pairs (2026-07-30)

Stack A holds plain values; Stack B receives a value only when a new minimum
appears, and pops in lockstep when the popped value is the current min.
`getMin()` = top of B. Space: B's size = number of times the min changed,
which is 1 on increasing input and n on strictly-decreasing input — so the
two-stack form ties the pair form in the worst case and beats it otherwise.
Pick pairs for interview-code simplicity, the two-stack form when asked to
optimize space.
