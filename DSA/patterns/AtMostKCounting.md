---
type: pattern
name: At-Most-K Counting (exactly-K by subtraction)
status: in-use
created: 2026-08-23
---

# At-Most-K Counting

Counting problems asking for **exactly k** of some monotone window property,
solved as `exactly(k) = atMost(k) - atMost(k-1)`.

Applies when the predicate is monotone in the window: extending a window can
only increase the tracked quantity (distinct count, sum of non-negative values).
That monotonicity is what makes a single forward two-pointer sweep valid.

Core loop, per `atMost`: extend right, shrink from the left while over budget,
then `cnt += j - i + 1`.

## Why `cnt += j - i + 1`

Counts exactly the valid windows ending at `j`. Each qualifying subarray is
counted once, at its unique right endpoint — no double counting. Nothing is
missed because any start before `i` produces a window containing `[i-1..j]`,
which already exceeded the budget, and supersets never have a smaller tracked
quantity.

## Problems Using This Pattern

- Number of Substrings Containing All Three Characters (LC 1358) — 2026-08-23,
  solved independently, full code cold, no bugs. O(n)/O(1).
- Binary Subarrays With Sum (LC 930) — 2026-08-25, **solved with-hints:1**,
  O(n)/O(1). Transfer recognised cold and unprompted on 2026-08-23 and again on
  re-derivation two days later. One bug: shrink guard `i<j` — see Pitfalls.

## Common Pitfalls

- **`k-1` underflow**: when `k` can be 0, `atMost(-1)` must yield 0. **Refined
  2026-08-25 — no explicit short-circuit is needed if the shrink guard is
  `i <= j`**: the window empties, `i` reaches `j+1`, and `cnt += j-i+1` adds 0
  on every index. With `i < j` the same call silently returns garbage. The
  guard IS the short-circuit; an `if (k < 0) return 0;` is belt-and-braces.
- **Shrink guard written for shape, not invariant**: `i < j` keeps the window
  non-empty, which looks safe and is wrong. Exit invariant is "longest suffix
  ending at `j` within budget, **possibly empty**" — LC 930, 2026-08-25, see
  [[mistake_journal]].
- **Predicate substitution**: "exactly k distinct" equals "contains all k
  specific values" *only* when the alphabet is exactly those k values. State
  which predicate the code computes vs which the problem asks for.
- **Justifying by restatement**: "a start before `i` violates the condition"
  asserts the conclusion. The argument is superset-containment plus
  monotonicity — 2026-08-23, 3 escalations, see [[mistake_journal]].
