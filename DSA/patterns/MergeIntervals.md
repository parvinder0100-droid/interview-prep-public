---
type: pattern
pattern: MergeIntervals
updated: 2026-08-05
status: in-use
---

# MergeIntervals

## When This Pattern Applies

Interval-scheduling greedy problems: selecting a max compatible subset, or
counting max simultaneous overlap.

## Core Idea

Sort by the coordinate that determines when a resource frees up (end time for
selection, both endpoints merged as events for overlap-counting) — not by
start time or duration. Selection: pick greedily, next candidate's start must
clear the last-picked end. Overlap-counting: two-pointer sweep over
independently-sorted arrival/departure arrays, +1 on arrival, -1 on departure,
track the max; tie-break arrival-before-departure when inclusive overlap
counts a simultaneous arrival+departure as needing 2 resources.

## Problems Using This Pattern

- N Meetings in One Room — sort by end time, strict `end < nextStart`.
- Minimum Number of Platforms — two-pointer sweep, arrival-before-departure
  tie-break (inclusive overlap rule).
- Merge Intervals (LC 56) — 2026-08-13, cold, no bugs. The **merging** variant,
  not selection: sort by *start* here (selection sorts by end), then compare
  each incoming interval against only the last kept one and extend it with
  `max` of the two ends. Overlap test is `last[1] >= cur[0]` — `>=` because
  touching intervals merge.

- Non-overlapping Intervals (LC 435) — 2026-08-15 — the **earliest-end**
  variant, not the merge variant. Sort by end; on conflict keep the interval
  that ends first. Same rule as N Meetings in One Room, and it transferred cold
  here after failing twice there (08-05).

## Common Pitfalls

- Sorting by start time or duration instead of end time for selection —
  both produce a smaller subset in general; neither tracks "when does the
  resource free up." Not obvious without a constructed counterexample.
- Pairing arrival/departure arrays together before sorting when unneeded —
  only pair when identity matters (selection); pure counting only needs
  independently-sorted arrays, O(1) extra space.
- Justifying "compare only against the last kept interval" by restating the
  sort ("everything earlier is already merged") instead of naming the quantity:
  the kept list's **ends are increasing**, so the last end is the largest, and
  clearing it clears every earlier one — 2026-08-13.
- Adding a secondary sort key on the end coordinate for merging: it costs
  nothing but does nothing either, since the merge takes `max` of the ends
  regardless of order. Real in *selection*/non-overlapping variants, dead here.
- Tie-break order at equal timestamps: arrival-before-departure captures a
  real simultaneous need for 2 resources; departure-first silently
  undercounts it.

- **Deciding the sort key before deciding the keep-rule.** Sorting by start and
  then always keeping the first interval is wrong on `[[1,100],[2,3],[3,4]]`
  (deletes 2, answer is 1). Ask "when two conflict, which do I keep?" *first* —
  the sort key falls out of that answer. 2026-08-15, LC 435.
- **`>` vs `>=` on the overlap test.** Touching endpoints (`[1,2]`, `[2,3]`) do
  not overlap, so the test must be strict `cur[1] > next[0]`. This is
  load-bearing, not incidental — `>=` fails that exact case.
- **Scan-and-jump loops are sound but need an argument.** A loop that breaks at
  the first non-overlapping interval and makes it the new `cur` does *not* miss
  later intervals that overlapped the old `cur`: any such `X` starts before the
  new `cur` starts and (being sorted later by end) ends after it, so `X`
  strictly contains the new `cur` and is caught on the next comparison.
