---
type: pattern
pattern: SlidingWindow
updated: 2026-07-24
status: in-use
---

# SlidingWindow

## When This Pattern Applies

Contiguous-subarray/substring problems asking for a max/min/count over
windows — fixed size (`k` given) or variable size (grown/shrunk based on a
condition).

## Core Idea

**Fixed window:** maintain a running sum/state over the last `k` elements —
add the incoming element, subtract the outgoing one as the window slides,
compare against a running max. O(n) time, O(1) space.

**Variable window:** two pointers, grow the right edge always; shrink the
left edge in a `while` loop whenever the window violates its condition
(duplicate found, sum exceeds target, etc.), then measure/record after each
valid state. O(n) amortized — each element enters and leaves the window at
most once across the whole run, same amortized argument as monotonic stack.

**"At most K" monotonic-best variant** (distinct subtype, don't conflate
with plain variable window above): condition is a budget (`k` flips, `k`
distinct types, `k` replacements). Shrink is a single `if`, not a `while`,
and the tracked "best stat" (maxFreq, distinct count) is **never
decremented** even when it goes stale after a shrink. Consequence: net
window length (`right-left+1`) only grows or stays the same across the
whole traversal, never shrinks — so the final window length at the end
of the loop IS the answer, and any shorter valid window was already
counted while the pointer passed through it. Stale "best stat" can never
cause a wrong (too-large) window to be accepted, only a same-size slide.

## Problems Using This Pattern

- Maximum Sum Subarray of Size K — Sliding Window/Fixed Window — solved
  2026-07-24, independently, no hints. Correct on k>array.length (-1).
- Longest Substring Without Repeating Characters — Sliding Window/Variable
  Window — solved 2026-07-24, independently, no hints. Correct on empty
  string (0).
- Max Consecutive Ones III — Sliding Window/At-most-K — solved 2026-07-24,
  independently, no hints. Correct on k=0 edge (reduces to plain max-
  consecutive-ones).
- Fruit Into Baskets — Sliding Window/At-most-K (distinct-type budget) —
  solved 2026-07-24, independently, no hints. Correct on all-one-type edge.
- Longest Repeating Character Replacement — Sliding Window/At-most-K —
  solved 2026-07-24, with-hints (heavy escalation) — see pitfall below.

## Common Pitfalls

- Fixed-window off-by-one on which index enters/exits the window each slide.
- Plain variable window: shrink must be a `while`, not a single `if` (may
  need to shrink by more than one element).
- **At-most-K variant, 2026-07-24 (Longest Repeating Character
  Replacement):** false belief that net window length can shrink after
  growing, because the tracked maxFreq goes stale post-shrink. Corrected
  via concrete trace on `"AABABBA", k=1` — window length is non-decreasing
  throughout; a stale maxFreq only means the *validity check* is stricter
  than reality, so worst case the window slides at the same size, it never
  shrinks net. Don't reason about this from the formula alone — trace it
  index-by-index if the "why" isn't automatic.

## Related

- [[AtMostKCounting]] (`AtMostKCounting.md`) — the counting variant
  (`exactly(k) = atMost(k) - atMost(k-1)`), split out 2026-08-23. Use that file
  for count-the-subarrays problems; this one stays the length/extremum variant.
