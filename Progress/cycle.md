---
type: cycle
updated: 2026-08-27
---

# Cycle State

```
mode: sprint
cycle_name: 2026-07-jobsearch
start: 2026-07-10
target_end: 2026-11-30
goal: DSA coverage, cut scope (Striver A2Z, ~94 of ~197 remaining kept — cut 2026-08-27)
```

**Target end moved 2026-08-11 from 2026-08-23 to 2026-11-30** (2nd move; the
1st was 08-01, from 08-09 to 08-23). Not breathing room — the honest
completion date for the goal the user chose: finish DSA coverage end-to-end
before broad prep.

Basis, with reviews batched to weekends so coverage runs on 5 days not 7:

    ~210 problems at ~3.5 per 2h weekday session = 17.5/week

    weekdays only, 100% adherence      ~2026-11-04
    weekdays + light weekend coverage  ~2026-10-21
    weekdays only, at the logged 64%   ~2026-12-22

**2026-11-30 is deliberately not the optimistic end** — it does not require 12
perfect weeks, and it absorbs the fact that the remaining problems skew hard
(DP gaps, Arrays Hard, Segment Tree/Fenwick), where 30 min/problem with full
code is optimistic. Show-rate is the dominant variable: 64%→90% is worth more
than every allocation decision in the plan combined.

**Scope cut instead of a 3rd date move — 2026-08-27.** The rule below was
honoured: `target_end` stays 2026-11-30 and the *goal* was cut, from ~197
remaining problems to ~94 (see `coverage_cut_list.md` and the Coverage Queue in
`30day-sprint.md`). Basis: actual pace since 08-11 is 5.3/week against 14.5
needed; the cut scope needs 7.4/week, which the logged 69% weekday show-rate
supports. Reversible — the add-back rule and its trigger are in
`30day-sprint.md`.

**If this date moves a third time, that is evidence the goal needs changing,
not the schedule.** Plan: [30day-sprint.md](30day-sprint.md), "DSA-First
Coverage Plan".

Single source of truth for "what mode is the system in right now." Every skill
that used to hardcode a day-counter or `2026-08-09` reads `mode`/`start`/
`target_end` from here instead.

## Modes

- **sprint** — active job-search countdown. Day counter, pace math (`interview-
  prep-pace`), and the week-by-week plan in `30day-sprint.md` all apply.
  `target_end` is set.
- **maintenance** — no active search, staying sharp on a regular cadence
  (heavier than dormant — still doing real new-material sessions, just no
  deadline). No day counter, no pace math. `target_end` absent.
- **dormant** — no active search, minimal upkeep only: weekly ~30 min (2
  Graduated-pool problems solved cold + 1 flashcard pass — see
  `DSA/Progress/review_schedule.md` Graduated list). `target_end` absent.

## How skills use this

- `interview-prep-resume`, `interview-prep-audit`, `interview-prep-pace`,
  `interview-prep-save` read `mode` here first, before any date math.
  Day-of-sprint / week-of-sprint / `target_end`-relative pace calculations
  only run when `mode: sprint`. In `maintenance`/`dormant`, they skip that math
  entirely rather than computing a negative or nonsensical day count.
- `interview-prep-resume` additionally checks `start`/last-active date: if the
  gap since last activity exceeds 60 days, it re-baselines instead of trusting
  `review_schedule.md` due dates (see that skill's re-baseline step).

## Changing mode

- **Ending a sprint** (offer landed, or sprint window lapsed without one):
  run `interview-prep-archive` first — it snapshots the finished cycle, then
  flips `mode` here to `maintenance` or `dormant`.
- **Starting a new sprint** (new job search begins): archive the old cycle if
  one is still active, then set `mode: sprint`, bump `cycle_name`, `start` to
  today, `target_end` to the new deadline.
