---
name: interview-prep-audit
description: >-
  Check whether the user's interview prep system (~/InterviewPrep) is on
  track — compares actual progress against the week-by-week plan (when in an
  active sprint), surfaces overdue reviews, untouched tracks, stale/rusty
  topics, and repeating mistake patterns, then gives a ranked list of concrete
  next actions. Use when the user asks "am I on track", "how am I doing
  overall", "what are my gaps", "am I behind", "give me a status check", or
  wants a checkpoint across the whole cycle rather than just today's session.
  Read-only — does not modify tracker files (that's interview-prep-save).
---

# Interview Prep Audit

Read-only checkpoint across the whole cycle. Different from
**interview-prep-resume** (picks one track/problem to start a session) — this
answers "big picture, am I actually on pace" and hands back a gap list, not a
single next problem. Never edit any tracker file during this skill; if the user
wants corrections logged, point them to interview-prep-save afterward.

## Step 1: Establish where "on track" should be

Read `~/InterviewPrep/Progress/cycle.md` first for `mode`. If `mode: sprint`:
1. `~/InterviewPrep/Progress/dashboard.md` — day count, current week, stated top
   weak areas, readiness table.
2. `~/InterviewPrep/Progress/30day-sprint.md` — find the week matching today's
   date (`cycle.md`'s `start`) and read that week's bullet list per track. That
   bullet list is the target to check actuals against — not invented criteria.

Compute day-of-cycle and which week that falls in (Week 1: days 1-7, Week 2:
8-14, Week 3: 15-21, Week 4: 22-30) from the current date vs `cycle.md`'s
`start`.

If `mode: maintenance` or `mode: dormant`: there's no week-by-week plan to check
against. Skip the pace-vs-plan comparison (Step 3.2) entirely and instead check
only overdue reviews, stale exposure, and recurring patterns — plus whether the
weekly maintenance/dormant quota (per `cycle.md`) is actually being kept.

## Step 2: Pull actuals for every track, not just the active one

Unlike interview-prep-save (touch only active tracks), an audit must check
**all five tracks** — silence in a track is itself a finding. Read each:
- `DSA/Progress/progress.md`, `DSA/Progress/review_schedule.md`,
  `DSA/mistakes/mistake_journal.md`
- `SystemDesign/Progress/progress.md`, `SystemDesign/Progress/review_schedule.md`,
  `SystemDesign/mistakes/mistake_journal.md`
- `LLD/Progress/progress.md`, `LLD/mistakes/mistake_journal.md`
- `Behavioral/Progress/progress.md`
- `Java/Progress/progress.md`, `Java/mistakes/mistake_journal.md`
- `Applications/tracker.md`

If a file is effectively empty (just headers, no entries), that's a "zero
activity" finding for that track — don't skip reading it to save time, the
absence is the signal.

## Step 3: Check four specific gap categories

Work through each; only report what the data actually shows, never invent a
gap the files don't support:

1. **Overdue reviews** — any `review_schedule.md` line under Upcoming Reviews
   (or Import Backlog) with a due date before today, not yet in Completed
   Reviews Log. Rank by interview weight noted in the files (e.g. DP/Binary
   Search called out as highest-weight) and by how overdue.
2. **Pace vs plan** — for the current week's bullet list (Step 1), which
   listed items have zero corresponding entries in that track's progress.md?
   E.g. if Week 1 says "draft 5-6 STAR stories" and Behavioral/Progress/
   progress.md has none, that's behind, not just "not started yet" — check the
   day count against how much of the week has elapsed before calling it
   urgent (day 2 of a 7-day week ≠ day 6).
3. **Stale/rust exposure** — topics flagged in progress.md or review_schedule.md
   as "solved months ago, no practice since" that still show zero
   re-verification entries. Treat these as live risk per the existing
   staleness notes in the files, not resolved just because the topic sheet
   shows high %.
4. **Recurring mistake patterns** — scan each mistakes/mistake_journal.md for
   entries sharing a Root Cause, Pattern, or Topic Area. Two or more
   independent entries with the same underlying cause (e.g. "edge case on
   boundary/duplicate handling" appearing across separate problems) is a
   systemic gap worth naming explicitly, not just a list of unrelated
   mistakes — this is the highest-value output of the audit since individual
   session recaps don't surface cross-problem patterns.

## Step 4: Report — compact, scannable, no prose

This is a dashboard, not an essay. Hard rules:
- **No paragraphs.** Every line is a table row or a short bullet (name +
  number/status, not a sentence explaining why).
- **Whole report fits on one screen** — roughly 20-25 lines total, including
  headers. If a category (e.g. overdue DSA reviews) has more than ~5 items,
  collapse to a count + the 2-3 highest-priority names, not a full list —
  full detail lives in the track files, this is a triage view.
- **One line of context max per item**, in parentheses, only if it changes
  what the user should do (e.g. "(repeat-rust)"). No Root Cause/How-to-Avoid
  prose — that's what the mistake journal is for.

**No markdown tables.** They render as raw literal `|` pipes in plain-text
terminals/CLI clients (confirmed bad in practice) — use plain indented text
with aligned columns instead, not `|---|---|` syntax.

Format, in this order:

```
<Day X/30 · Week N | MAINTENANCE | DORMANT> · <ON TRACK | BEHIND>

OVERDUE (total count)
  <category>   <count> left: <top 2-3 named>, or "cleared"

TRACKS
  DSA           <status>   <missing, terse>
  SystemDesign  <status>   <missing, terse>
  LLD           <status>   <missing, terse>
  Behavioral    <status>   <missing, terse>
  Java          <status>   <missing, terse>
  Applications  <status>   <missing, terse>

PATTERNS (2+ occurrences only)
  <pattern>            Nx

NEXT
  1. ...
  2. ...
  3. ...
```

Align the second column loosely with spaces (not a real table, just eyeball
alignment) so it still scans as columns without markdown table syntax. Skip
any section that's genuinely empty (e.g. no recurring patterns found) — don't
pad with "none found" filler rows unless it's the Overdue section (where
"cleared" is itself useful signal).

## Step 5: Offer, don't act

End by asking whether to start on the top recommended action now (handing off
to interview-prep-resume for that track) — do not auto-start a session or edit
any file. This skill's job ends at the report.
