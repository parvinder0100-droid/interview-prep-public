---
type: pattern
pattern: MonotonicStack
updated: 2026-08-27
status: in-use
---

# MonotonicStack

## When This Pattern Applies

"Next/previous greater/smaller element" problems — for each index, find the
nearest element (left or right) satisfying a comparison.

## Core Idea

**General rule (derived 2026-07-21, on the second problem in this pattern):**
for "nearest X in direction Y," start traversal from the end matching side Y
— so that by the time you reach index i, the stack already holds exactly the
already-processed elements on the queried side. (Query right → start at the
right end, traverse right-to-left. Query left → start at the left end,
traverse left-to-right.) At each index: pop everything that fails the "X"
comparison against the current element. **The tie comparison (`>=/<=` vs
strict `>/<`) is NOT fixed by the pattern — it is set by the problem** (see
"Tie rule" below; the blanket "always use >=/<=" written here on 2026-07-20 was
corrected 2026-08-27 after it produced a wrong answer on LC 907). Whatever remains on top is the answer
(or -1/sentinel if empty), then push current. Amortized O(n) — each element
is pushed and popped at most once across the entire run. Stack stays
monotonic: decreasing (top-to-bottom) for "greater" queries, increasing for
"smaller" queries.

## Problems Using This Pattern

- Next Greater Element — Stack/Queue/Medium — solved 2026-07-20 with 1 hint
  (correct approach cold, code bug — see Common Pitfalls).
- Nearest Smaller to the Left — Stack/Queue/Medium — solved 2026-07-21 with
  2 hints (instance mechanics correct quickly; generalizing the direction
  rule needed guided questions — see Common Pitfalls).
- Stock Span Problem — Stack/Queue/Medium — solved 2026-07-21 with 3 hints
  (correctly identified span = distance from nearest-greater-left index,
  off-by-one in the formula itself — see Common Pitfalls).
- Largest Rectangle in Histogram (LC 84) — Stack/Hard — solved 2026-08-27 with
  2 hints (approach, `nsr-nsl-1` width and the justification all cold; ties
  harmless because the caller takes a `max`).
- Sum of Subarray Minimums (LC 907) — Stack/Medium — solved 2026-08-27 with
  4 hints (contribution counting cold; **tie rule carried over from LC 84 and
  double-counted** — see Common Pitfalls).
- Daily Temperatures (LC 739) — Stack/Medium — solved 2026-08-27 independently,
  cold, first submit (`>=` pop justified unprompted).

## Common Pitfalls

- **Tie rule (2026-08-27, the single highest-value entry in this file).** Three
  problems in one session used identical `nsl/nsr` code with three different tie
  requirements, and the rule is set by the problem's wording, never by the
  pattern:

      "largest area"        LC 84   ties harmless — caller takes a max, a
                                    double-claimed span changes nothing
      "sum of minimums"     LC 907  strict on EXACTLY ONE side, else every
                                    tied subarray is added twice ([2,2] -> 8 vs 6)
      "warmer"              LC 739  strict comparison, so equals must be popped

  Before reusing this template, ask: **does the caller take a max, a sum, or a
  strict comparison?** Mandatory test case on every problem in this pattern:
  an all-equal input (`[2,2]`).

- Pushing the *computed answer* onto the stack instead of the *original
  array value* — corrupts later comparisons, since the stack needs to hold
  real values to compare against, not results. Use a separate output array;
  never let the answer array and the stack share storage. **Repeat-decay
  flag (2026-07-24):** the mechanical fix stuck, but the "why" still needed
  a full guided rebuild at review #1 — treat this as a standing weak point,
  not resolved after one correction.
- Getting one direction/pop-condition instance right without being able to
  *derive* the next one — the transferable rule is "traversal starts from
  the end matching the query side" plus "pop with >=/<= to exclude ties,"
  not a memorized direction per problem.
- When a nearest-greater/smaller index is used to compute a *distance* (span,
  width, count) rather than returned directly as the answer: derive the
  formula via inclusive-range counting (`b-a+1` for range `[a,b]`), don't
  guess the offset. `span = curIndex - nearestGreaterLeftIdx` (no extra -1) —
  the -1 sentinel for "no such element" needs no special-casing since it
  falls straight out of the formula.
