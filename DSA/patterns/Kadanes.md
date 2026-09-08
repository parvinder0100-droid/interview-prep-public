---
type: pattern
pattern: Kadanes
updated: 2026-07-20
status: in-use
---

# Kadanes

## When This Pattern Applies

Max/best-subarray-value problems over a contiguous run, where you need the best
value (or the best window itself) seen while scanning left to right once.

## Core Idea

Maintain a running sum/state that resets when it stops helping (goes negative,
or a reset condition triggers); record the best-so-far using the value *before*
the reset, every iteration, not just at reset time. For "return the subarray"
variants, track a separate window-start pointer (`tempStart`) that only moves on
reset, distinct from the best-window-start pointer (`start`) that only moves on
a new max.

## Problems Using This Pattern

- Kadane's Maximum Subarray Sum — Arrays/Medium — solved 2026-07-12, review #1/#2 clean.
- Print Subarray with Maximum Sum — Arrays/Medium — Kadane's variant with
  dual-pointer window tracking, resolved 2026-07-20 (see mistake_journal).

## Common Pitfalls

- Only updating `max` at reset time — loses the best value on all-negative
  arrays where the running sum never has a chance to be positive before reset.
  Fix: `sum+=x; max=max(max,sum); if sum<0: sum=0` — record before reset, always.
- For window-tracking variants: collapsing the recorded start pointer to the
  *current index* on a new max, instead of copying the running window's start
  (`tempStart`). The two pointers update on different triggers (reset vs.
  new-max) and must stay separate.
- The window-tracking "why start=tempStart" derivation has decayed TWICE now
  (07-17 mid-derivation, 07-20 "closed", 07-21 fully blank again) — treat as
  a standing weak point needing extra recall checks, not just the normal
  spaced interval.
- The base-value "why" (order-before-reset) can be recalled correctly while
  the underlying failure-mode explanation is still hand-wavy — push for a
  concrete small-array trace, don't accept a restated procedure as a passed
  derivation.
