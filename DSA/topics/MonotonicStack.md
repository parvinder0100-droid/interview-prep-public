---
type: topic
topic: MonotonicStack
updated: 2026-08-27
status: in-progress
---

# MonotonicStack

## Subtopics (Striver A2Z order)

_To be filled in as more of the topic is reached._

## Patterns That Show Up Here

- See `../patterns/` — no dedicated MonotonicStack pattern file yet, only one
  problem solved so far.

## Problems Log

- Next Greater Element — Medium — solved: with-hints:1 — 2026-07-20 — see
  Stack/Queue in progress.md and mistake_journal.
- Nearest Smaller to the Left — Easy — solved: with-hints:2 — 2026-07-21 —
  generalized traversal-direction rule needed escalation; see mistake_journal.
- Stock Span Problem — Medium — solved: with-hints:1 — 2026-07-21 —
  https://leetcode.com/problems/online-stock-span/ — off-by-one in the span
  formula, fixed by inclusive-range derivation; see mistake_journal.
- Largest Rectangle in Histogram (LC 84) — Hard — solved: with-hints:2 —
  2026-08-27 — `(nsr-nsl-1)*h[i]`; ties harmless under `max`.
- Sum of Subarray Minimums (LC 907) — Medium — solved: with-hints:4 —
  2026-08-27 — contribution counting `(i-nsl)*(nsr-i)`; ties **must** break one
  way (strict on exactly one side) or subarrays are double-counted.
- Daily Temperatures (LC 739) — Medium — solved: independently — 2026-08-27 —
  right-to-left, pop on `>=` because "warmer" is strict.

## Common Mistakes Seen in This Topic

- **The tie rule is the only thing that varies across `nsl/nsr` problems, and it
  is set by the problem's own wording** — "largest area" (ties harmless),
  "sum of minimums" (strict on exactly one side, else double-count),
  "*warmer*" (strict, so equals must be popped). All three met 2026-08-27; the
  second was carried over from the first and produced a wrong answer.

- Pushed the computed answer onto the stack instead of the original array
  value — see [[mistake_journal]] 2026-07-20.
- Traversal direction treated as problem-specific intuition rather than a rule
  — the transferable form is "start from the query side" — see
  [[mistake_journal]] 2026-07-21 and 2026-07-24 (2nd occurrence).
- Index-difference formulas guessed rather than derived; use `b-a+1` for an
  inclusive range instead of trusting an intuitive `-1` — see
  [[mistake_journal]] 2026-07-21.
