---
name: interview-prep-pace
description: >-
  Compute the deep-work hours/day needed, from today onward, to finish the
  user's active interview prep sprint (~/InterviewPrep) on time — converts
  remaining scope across all tracks (DSA problems, review backlog, System
  Design/LLD case studies, Java topics, Behavioral stories) into estimated
  hours using rough per-item time estimates, divides by days left, and checks
  that against actual historical show-rate. Only meaningful when
  Progress/cycle.md mode is "sprint" (a target_end date exists) — has no
  deadline to compute against in maintenance/dormant mode. Use when the user
  asks "how many hours do I need", "am I going to make it", "what's my
  required pace", "how much deep work do I need today/this week", "will I hit
  my deadline", or wants a projection instead of just a gap list (that's
  interview-prep-audit). Read-only — does not modify tracker files.
---

# Interview Prep Pace Planner

Answers "how many deep-work hours do I need, and doing what, to actually hit
the sprint deadline" — a forward projection, not a backward-looking gap list
(that's **interview-prep-audit**, which this skill should be run alongside,
not instead of — audit tells you what's wrong, this tells you the hours math
to fix it). Never edit any tracker file; this is a read + compute + report
skill.

## Step 0: Check mode — this skill only applies in sprint mode

Read `~/InterviewPrep/Progress/cycle.md`. If `mode` is `maintenance` or
`dormant`, there's no deadline to divide remaining scope by — say so plainly
and stop; point the user at `interview-prep-audit` instead (it works in every
mode). Don't fabricate a pace number against a nonexistent or lapsed deadline.

If `mode: sprint`, continue. Time estimates are rough regardless — there is no
real time-tracking wired in (the user chose markdown-activity estimation over
pulling actual hours from the Notion Deep Work Logger). Every hour figure this
skill produces is a rough estimate from the per-item table in Step 3, not
measured fact. Always present numbers as estimates ("~X hours"), never as
precise commitments, and say so once in the report.

## Step 1: Establish the timeline

Read `~/InterviewPrep/Progress/cycle.md` for `start` and `target_end`. Compute:
- `days_elapsed` = today − `start`
- `days_remaining` = `target_end` − today (inclusive of today)

## Step 2: Pull remaining scope, per track

Read every track's `Progress/progress.md` (and `review_schedule.md` where it
exists — DSA, System Design):

- **DSA**: remaining *new* problems = sum of each not-yet-complete topic's
  remaining count as stated in `progress.md` (e.g. "Arrays Hard subtopic (11)
  untouched", "Recursion 2/25" → 23 remaining, Stack/Queue/Sliding
  Window/Heaps/Greedy/Graphs remaining per the confirmed-not-started list
  minus whatever's been solved live since). Remaining *reviews* = every line
  in `review_schedule.md` under Upcoming Reviews/Import Backlog not yet in
  Completed Reviews Log, split into "stale-backlog first-verification" (~1
  rep) vs "spaced-repetition review" (already-live-solved problems).
- **System Design / LLD**: these are organic tracks with no fixed
  Striver-sheet-style total. Use a stated default target — **8 System Design
  case studies and 6 LLD case studies + core SOLID/pattern concepts by sprint
  end** — call this an assumption in the report, not a hard requirement, and
  subtract whatever's already logged in `progress.md`.
- **Java**: remaining = topics in `Progress/progress.md` still `not started`
  out of the 4 pre-populated (Collections, Concurrency, JVM_GC, CoreOOP).
- **Behavioral**: remaining = 6 − stories logged in `progress.md`, plus a
  pressure-test pass per story if not yet marked pressure-tested.
- **Applications**: not a deep-work-hours item — skip from the hours math,
  but flag separately if `Applications/tracker.md` Active section is still
  empty (this runs in parallel, doesn't consume sprint study hours the same
  way).

## Step 3: Convert remaining scope to estimated hours

Apply these rough per-item estimates (state in the report that they're rough
and haven't been calibrated against real logged time):

- DSA new problem (genuinely new pattern): ~25 min
- DSA stale-backlog first re-verification: ~15 min
- DSA spaced-repetition review (already reviewed once+): ~8 min
- System Design case study (full depth): ~90 min
- LLD case study or concept: ~45 min
- Java topic/subtopic quiz session: ~30 min
- Behavioral STAR story (draft + pressure-test): ~30 min

Multiply counts × estimates, sum per track, sum to a grand total, convert to
hours.

## Step 4: Sanity-check against actual historical show-rate

Scan each track's `progress.md` "Notes for Next Session" section (or DSA's
dated Completed Problems entries) for distinct calendar dates with logged
activity since 2026-07-10. `show_rate = distinct_active_days / days_elapsed`.
Multiply by `days_remaining` to get a realistic projected number of *active*
days left (not calendar days) — this is usually the harshest constraint, not
the hours math. If required daily average assumes every remaining calendar
day is a work day but show-rate says otherwise, say so explicitly and
recompute required hours **per actual active day** too (total hours ÷
projected active days), since that's the number that matters.

## Step 5: Report — compact, no prose, no markdown tables

```
Day X of cycle · N days left (target: <cycle.md target_end>) · show-rate: A/B days active (C%)

REMAINING SCOPE (est. hours, rough)
  DSA new              ~Xh  (N problems)
  DSA reviews          ~Xh  (N due: M stale-backlog, K spaced-rep)
  System Design        ~Xh  (N/8 case studies, assumption)
  LLD                  ~Xh  (N/6 case studies, assumption)
  Java                 ~Xh  (N/4 topics)
  Behavioral           ~Xh  (N/6 stories)
  TOTAL                ~Xh

PACE
  Required, every calendar day left:     ~X.Xh/day
  Required, if only active days repeat:  ~X.Xh/day  (harder number — this is
                                                       the real constraint)

TODAY
  Suggested split (per Session Protocol in dashboard.md — Block A/B/C/+15min):
  1. ...
  2. ...
  3. ...
```

Skip a track's row if it's fully done (0 remaining) — don't pad.

## Step 6: Offer, don't act

End by asking whether to start today's session on the top track now (hand off
to **interview-prep-resume**) — do not auto-start a session or edit any file.
If the required-hours number looks unrealistic given the show-rate history,
say so plainly rather than softening it — that's the point of this skill.
