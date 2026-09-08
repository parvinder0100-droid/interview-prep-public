---
name: interview-prep-archive
description: >-
  Close out a finished interview-prep cycle (offer landed, or the sprint
  window lapsed) — snapshots the cycle's dashboard/sprint-plan/stats into
  Archive/<cycle_name>/, thins the live dashboard back to a maintenance
  template, and flips Progress/cycle.md to maintenance or dormant mode. Use
  when the user says "I got the offer", "close out this sprint", "archive
  this cycle", "I'm done job hunting for now", or when interview-prep-audit/
  resume notices the sprint's target_end has passed with no new cycle
  started. Without this step the dashboard just keeps stating a lapsed day
  count forever — this is what actually ends a cycle cleanly.
---

# Archive a Prep Cycle

Ends a cycle without deleting anything — the goal is a clean snapshot future-
you can reopen (via `interview-prep-resume`'s re-baseline path) plus a live
dashboard that no longer references a dead deadline.

## Step 1: Confirm why this cycle is ending

Ask (briefly, don't over-interrogate): offer landed and accepted (→ likely
`dormant` next), or just pausing the active search (→ `maintenance` or
`dormant`, user's call), or the sprint window lapsed without an offer and the
user wants to keep searching (→ start a **new** sprint cycle instead of just
archiving — archive the old one first, then set up the new one per
`cycle.md`'s "Starting a new sprint" section).

## Step 2: Snapshot the cycle

Read `Progress/cycle.md` for the current `cycle_name`. Create
`Archive/<cycle_name>/` and copy (don't move — originals get reset in Step 3,
not deleted) into it:
- `Progress/dashboard.md`
- `Progress/30day-sprint.md`
- `DSA/Progress/statistics.md`
- `Applications/tracker.md`

Add one `Archive/<cycle_name>/CLOSED.md` with: cycle dates, outcome (offer/
no offer/paused), final readiness snapshot pulled from the dashboard being
archived, and 3-5 lines on what worked/didn't for next time (pull from
dashboard's own audit notes if present — don't invent new analysis here).

## Step 3: Reset live files

- `Progress/dashboard.md` → replace with a thin maintenance-mode template:
  mode line, review-due count (derived, see interview-prep's dashboard-drift
  fix), one line per track's readiness, no day counter, no narrative weak-
  area prose (that lives in each track's own mistake journal already).
- `Progress/30day-sprint.md` → leave in place but add a one-line header
  pointing at the archived copy; don't delete (it's the plan that produced
  the archived outcome, worth keeping at the top level for one more cycle in
  case of quick reference, then it can move into the archive folder too on
  the *next* archive run).
- `Applications/tracker.md` → move any `Active` entries that ended
  (rejected/withdrawn) to `Past / Closed`. If the outcome was an accepted
  offer, note which company/role at the top of the file before clearing
  `Active`.

## Step 4: Flip cycle mode

Edit `Progress/cycle.md`: set `mode` to `maintenance` or `dormant` (per Step
1's answer), clear `target_end`, leave `cycle_name`/`start` as historical
record of the cycle just closed (a new cycle starting later gets a new
`cycle_name` and `start`, not a mutation of these).

## Step 5: Commit and confirm

`cd ~/InterviewPrep && git add -A && git commit -m "archive cycle: <cycle_name> (<outcome>)"`.
One short confirmation line: what got archived, new mode, and — if starting a
new sprint — hand off to setting up `cycle.md` for it.
