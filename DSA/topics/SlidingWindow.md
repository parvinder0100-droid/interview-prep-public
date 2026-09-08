---
type: topic
topic: SlidingWindow
updated: 2026-08-23
status: in-progress
---

# SlidingWindow

## Subtopics (Striver A2Z order)

Fixed window, variable window (shrink-while-invalid), at-most-K
(monotonic-best, shrink-while-invalid via `if`), variable window
(shrink-while-still-valid, e.g. Minimum Window Substring).

## Patterns That Show Up Here

[[SlidingWindow]] (`../patterns/SlidingWindow.md`).

## Problems Log

- Maximum Sum Subarray of Size K — Fixed Window — solved: independently —
  2026-07-24.
- Longest Substring Without Repeating Characters — Variable Window —
  solved: independently — 2026-07-24.
- Max Consecutive Ones III — At-most-K — solved: independently — 2026-07-24.
- Fruit Into Baskets — At-most-K — solved: independently — 2026-07-24.
- Longest Repeating Character Replacement — At-most-K — solved:
  with-hints:3 — 2026-07-24.
- Minimum Window Substring — Variable Window (shrink-while-valid) — solved:
  independently — 2026-07-24.
- Number of Substrings Containing All Three Characters (LC 1358) — At-most-K
  (exactly-K by subtraction) — solved: independently, full code cold, no bugs —
  2026-08-23. https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
  O(n)/O(1). Justification needed escalation twice — see [[mistake_journal]].
- Binary Subarrays With Sum (LC 930) — At-most-K (exactly-K by subtraction) —
  **solved: with-hints:1** — 2026-08-25 (approach cold 2026-08-23, code written
  2026-08-25). https://leetcode.com/problems/binary-subarrays-with-sum/ —
  `atMost(goal) - atMost(goal-1)` retrieved cold and unprompted 2 days earlier;
  still correct on re-derivation. O(n)/O(1). One bug: shrink guard `i<j` instead
  of `i<=j`, so the window could never empty — see [note](../notes/binary-subarrays-with-sum.md).
  Fixed after 1 targeted question, but **fixed silently**: invariant, complexity
  and edge case all went unstated. Logged as unspoken, not as covered.

## Common Mistakes Seen in This Topic

- Shrink guard written to protect a non-empty window (`i<j`) rather than derived
  from the loop's exit invariant — breaks exactly when the window must empty
  (single element over budget, and every `atMost(-1)` call) — 2026-08-25, see
  [[mistake_journal]].
- Counting-window claims answered by restating the condition rather than the
  superset/monotonicity argument — 2026-08-23, 3 escalations, see
  [[mistake_journal]].
- Using the alphabet constraint implicitly: "exactly-K distinct" and "contains
  all K" only coincide when the alphabet IS those K characters — 2026-08-23,
  see [[mistake_journal]].

- At-most-K variant: false belief that net window length can shrink after
  growing once the tracked "best stat" goes stale post-shrink — see
  [[mistake_journal]] 2026-07-24 (Longest Repeating Character Replacement).

## Cut-list queue — itemized 2026-08-31 (Day 0)

From `Progress/coverage_cut_list.md`. `- [ ]` = scheduled, not yet solved.

**6 slots — cut list says "remainder, all of it", so every unsolved Step-10
problem qualifies. Names not yet transcribed.**

- [ ] TBD x6 — needs the sheet or Codolio; nothing on disk names them
