---
type: topic
topic: Stack
updated: 2026-08-27
status: in-progress
---

# Stack

## Subtopics (Striver A2Z order)

_To be filled in as more of the topic is reached._

## Patterns That Show Up Here

- [[MonotonicStack]] — Next Greater Element

## Problems Log

- Valid Parentheses — Easy — solved: independently — 2026-07-20
- Min Stack — Medium — solved: independently — 2026-07-20
- Next Greater Element — Medium — solved: with-hints:1 — 2026-07-20
- Nearest Smaller to the Left — Medium — solved: with-hints:2 — 2026-07-21 —
  mechanics (direction, pop-condition, ties) correct quickly; generalizing
  the direction-of-traversal rule needed real Socratic escalation.
- Stock Span Problem — Medium — solved: with-hints:3 — 2026-07-21 — core
  relationship (span = gap from nearest-greater-left index) derived
  correctly, but formula had an off-by-one (`-1` extra) until derived from
  inclusive-range counting.
- Asteroid Collision (LC 735) — Medium — **solved: with-hints:4** — 2026-08-24
  (failed cold 2026-08-23) — https://leetcode.com/problems/asteroid-collision/ —
  O(n)/O(n), amortized argument independent on first ask. Cold re-attempt
  reproduced 08-23's symmetric-collision bug verbatim; fixed to
  `stTop>0 && cur<0` after number-line instantiation. Second bug found this
  session: equality unhandled after the cascade `while`, so `[10,2,-10]`
  returned `[10,-10]`. [note](../notes/asteroid-collision.md)
- Trapping Rain Water (LC 42) — Hard — **solved: with-hints:5** — 2026-08-26 —
  https://leetcode.com/problems/trapping-rain-water/ — O(n)/O(n) via prefix-max
  and suffix-max arrays (**no stack used**; listed here only because Striver
  files it in the Stack/Queue section). Code cold and correct on first submit;
  complexity, clamp semantics and edge cases all stated. The 14 min before the
  code went to nearest-vs-tallest: the rule was reached for as `nsl/nsr` off
  this topic's own template instead of derived from the physics.
  [note](../notes/trapping-rain-water.md)
- Trapping Rain Water (LC 42) — O(1)-space follow-up — **with-hints:6** —
  2026-08-27 — two-pointer, O(n)/O(1). Key argument derived cold: each of
  `leftMax`/`rightMax` is exact for its own pointer and a **lower bound** for the
  opposite one, and the branch condition guarantees the min is the exact side, so
  the unseen middle never matters. Code was not attempted — requested outright.
- Largest Rectangle in Histogram (LC 84) — Hard — **solved: with-hints:2** —
  2026-08-27 — https://leetcode.com/problems/largest-rectangle-in-histogram/ —
  O(n)/O(n), two `nsl`/`nsr` passes + `(nsr-nsl-1)*h[i]`. Approach, formula and
  justification all cold; amortized O(n) argument cold. Ties harmless here
  (`max` ignores double-claims).
- Sum of Subarray Minimums (LC 907) — Medium — **solved: with-hints:4** —
  2026-08-27 — https://leetcode.com/problems/sum-of-subarray-minimums/ —
  contribution counting, `(i-nsl)*(nsr-i)*arr[i]`. Two defects: duplicate
  double-count and int overflow. [note](../notes/sum-of-subarray-minimums.md)
- Daily Temperatures (LC 739) — Medium — **solved: independently** — 2026-08-27
  — https://leetcode.com/problems/daily-temperatures/ — O(n)/O(n), right-to-left
  monotonic stack, `>=` pop. Cold, first submit, Accepted 0 ms.

## Common Mistakes Seen in This Topic

- Reusing this topic's `nsl/nsr` template without checking the **tie rule** the
  problem needs — strict on both sides is harmless under `max` (LC 84) and an
  overcount under `sum` (LC 907, `[2,2]` gave 8 vs 6) — 2026-08-27, 2nd
  template-first occurrence, see [[mistake_journal]].
- Counting subarray endpoints as "extra elements beyond i" rather than endpoints
  including `i` — 3rd inclusive-range off-by-one (Stock Span 07-21) — 2026-08-27.

- Reaching for this topic's stored template (`nearest smaller/greater`) before
  asking what the problem's physics requires — on LC 42 the boundary needed is
  the **tallest** bar each side, not the nearest taller one, because anything
  shorter in between is submerged to the same level — 2026-08-26, see
  [[mistake_journal]].

- Stack simulation: assuming both orderings of a pair interact. Only one sign
  order collides (top moving right, incoming moving left); the reverse diverges
  — 2026-08-23, see [[mistake_journal]].
- Not running the problem statement's own given examples against written code
  before declaring done — 2026-08-23, see [[mistake_journal]].

- Next Greater Element: pushed the computed answer onto the stack instead of
  the original array value — see [[mistake_journal]] 2026-07-20.
- Nearest Smaller to the Left: could state the correct algorithm for this
  instance but couldn't generalize "why this direction" until guided to
  compare stack contents at index i across both problems — see
  [[mistake_journal]] 2026-07-21.
- Stock Span Problem: off-by-one in the span formula (`curIndex-ngeIndex-1`
  instead of `curIndex-ngeIndex`) — guessed the arithmetic instead of
  deriving it via inclusive-range counting — see [[mistake_journal]]
  2026-07-21.

## Cut-list queue — itemized 2026-08-31 (Day 0)

From `Progress/coverage_cut_list.md`. `- [ ]` = scheduled, not yet solved.

**10 slots across Stack/Queue; 6 named in the cut list, 4 unnamed.**
The monotonic-stack family (LC 84 / 907 / 739) is already done.

- [ ] Maximal Rectangle — largest rectangle in a binary matrix (LC 85)
- [ ] Sliding Window Maximum (LC 239)
- [ ] LRU Cache (LC 146)
- [ ] LFU Cache (LC 460)
- [ ] Min Stack (LC 155)
- [ ] Find the Celebrity (LC 277)
- [ ] TBD x4 — unnamed in the cut list
