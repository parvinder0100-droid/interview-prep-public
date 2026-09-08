---
type: flashcards
topic: sliding_window
updated: 2026-07-24
---

# Sliding Window Flashcards

Format: Q on one line, A (intuition/complexity only, never full code) below it.

Q: Fixed-size window (e.g. max sum subarray of size k) — how do you avoid
recomputing the sum from scratch each slide?
A: Add the incoming element, subtract the outgoing one — running sum update
in O(1) per slide, O(n) total.

Q: Longest Substring Without Repeating Characters — why is the shrink loop
a `while`, not an `if`?
A: A single duplicate can require shrinking past more than one character to
clear it — `while` keeps shrinking until the window is valid again, not just
one step.

Q: "At-most-K" variant (Max Consecutive Ones III, Fruit Into Baskets,
Longest Repeating Char Replacement) — why is shrink a single `if`, and why
doesn't a stale tracked "best stat" (maxFreq, distinct count) break
correctness?
A: Net window length only grows or stays the same across the whole
traversal — a stale best-stat only makes the validity check stricter than
reality, worst case the window slides at the same size, it never shrinks
net. Final window length at loop end IS the answer.

Q: Minimum Window Substring — how do you check window validity in O(1)
without comparing two full frequency maps each step?
A: Maintain a `matched` counter — increment only when a needed char's
window-count crosses exactly from `need[c]-1` to `need[c]` (strict `==`,
never `>=`, so it never double-fires); decrement only when removing a char
during shrink drops it back below `need[c]`. Valid when
`matched==distinctCharsInT`.

Q: You need substrings/subarrays with EXACTLY k of something. The window only
handles "at most". How do you get exactly?
A: `exactly(k) = atMost(k) - atMost(k-1)`. Works for any "at most" predicate
that is monotone in the window (distinct-count, sum of non-negatives). Both
calls are O(n), so the whole thing stays O(n). Guard the `k-1` call when k can
be 0 — `atMost(-1)` must return 0, not run the loop.

Q: In an at-most window, why is `cnt += j - i + 1` correct — no double count,
nothing missed?
A: Those are exactly the valid substrings ENDING at j, so each substring is
counted once at its unique right endpoint. Nothing is missed because any start
before `i` yields a window containing `[i-1..j]`, which already exceeded the
budget — supersets never have fewer distinct/smaller sums.

Q: "Exactly 3 distinct characters" and "contains all of a, b, c" — same thing?
A: Only when the alphabet IS {a,b,c}. With a wider alphabet "abd" is 3-distinct
without a `c`. Name which predicate the code computes vs which the problem asks
for; a "now it's a-z" follow-up breaks the second, not the first.

Q: At-most-K shrink loop — should the guard be `i < j` or `i <= j`, and what
breaks with the wrong one?
A: `i <= j`. The window must be allowed to empty. With `i < j` a single element
over budget survives the shrink (`[1]` with goal 0 counts as valid), and every
`atMost(-1)` call — which `goal = 0` always makes — returns garbage instead of
0. State the exit invariant as "longest suffix ending at j within budget,
possibly empty"; `i <= j` is what makes "possibly empty" true.
