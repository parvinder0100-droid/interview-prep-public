---
name: interview-prep-resume
description: >-
  Resume or start a session in the user's unified interview prep tracker at
  ~/InterviewPrep (DSA/Striver A2Z, System Design, LLD, Behavioral, Java) — a
  career-long system that runs in cycles (active sprint, then maintenance/dormant
  upkeep), not just a one-time 30-day sprint. Use when the user wants to continue,
  resume, or start today's prep — phrases like "let's continue my interview prep",
  "start today's DSA session", "resume prep", "what should I work on today", or
  opening a new session to pick up where a previous one left off. Reads the tracker
  files directly instead of asking the user to re-explain context.
---

# Resume Interview Prep

The user runs a career-long prep system across five tracks, tracked entirely in
markdown at `~/InterviewPrep`, cycling between active job-search sprints and
lighter maintenance/dormant periods between them. This skill picks the session up
from disk state — never ask "where did we leave off," read it instead.

## Step 0: Check cycle mode and staleness

Read `~/InterviewPrep/Progress/cycle.md` first. Note `mode` (sprint / maintenance
/ dormant) — it governs whether day-counter/week-of-sprint framing applies at all
in Step 1 and Step 3 below. Then check the date of the most recent dated entry in
`DSA/Progress/progress.md` (or `git log -1` in the repo):

- **Gap ≤ 60 days**: proceed normally to Step 1.
- **Gap > 60 days**: this is a long-dormant reopen, not a routine resume. Do
  **not** trust `review_schedule.md` due dates — hundreds of items may show
  "overdue," but that's dormancy, not necessarily forgetting. Instead:
  1. Tell the user this looks like a reopen after a long gap and propose a
     re-baseline instead of grinding the stale due-date backlog.
  2. Pick 2-3 problems per major topic from the DSA Graduated list (or, if no
     Graduated list exists yet, from topics marked 100%/near-complete) and run
     them as cold timed solves — no due-date honoring, no hint-free assumption.
  3. Rebuild `review_schedule.md`'s Upcoming Reviews from these results only
     (rust found → fresh review #1; clean → straight to a late-stage interval or
     re-graduate) — archive the old stale queue rather than trying to reconcile
     it line by line.
  4. Mistake journals and pattern files carry over untouched — they're the
     durable asset and don't decay just because time passed.
  Only after this re-baseline does the rest of this skill's flow apply.

## Step 1: Read the master state

Read, in order:
1. `~/InterviewPrep/Progress/dashboard.md` — reviews due, top weak areas per
   track, active application bias, readiness snapshot. Day count / this week's
   focus only apply if `cycle.md` mode is `sprint`.
2. `~/InterviewPrep/Progress/30day-sprint.md` — the week-by-week plan (sprint mode
   only — skip this file entirely in maintenance/dormant mode, it has no
   week-of-sprint to map to).

## Step 2: Read the relevant track's detail

Based on the dashboard's top weak areas / this week's focus, read the specific
track's files before starting:
- `~/InterviewPrep/DSA/Progress/progress.md`, `review_schedule.md`, and the
  relevant `~/InterviewPrep/DSA/topics/<Topic>.md` file(s).
- `~/InterviewPrep/DSA/flashcards/review_log.md` — dashboard flashcard review
  history (box level, last-reviewed date, miss count per card). Low-box or
  frequently-missed cards are live weak-spot signal, same weight as a mistake
  journal entry. This file only updates when the user pastes a "save progress
  to repo" export from the dashboard into a session — if it says no exports
  processed yet, flashcard activity since then isn't visible here; don't
  assume silence means no review happened.
- Or the equivalent `Progress/progress.md` (+ `mistakes/mistake_journal.md`) under
  `SystemDesign/`, `LLD/`, `Behavioral/`, or `Java/` if that's the track in focus.

Pay attention to staleness/rust notes (e.g. topics solved months ago with no
practice since get treated as needing real re-verification, not a rubber-stamp
review) and to any topic explicitly marked "confirmed not started" vs "unknown."

## Step 3: Recap and propose, briefly

Give a short recap (2-4 lines): in `sprint` mode, day X of the cycle + this
week's focus; in `maintenance`/`dormant` mode, skip the day counter and just
state the mode + what's due. Either way: what's due for review today, and a
proposed next problem/topic — pulled from the files, not invented. Let the user
confirm or redirect before diving in.

**Always ask how long the session is (added 2026-08-12, user instruction).**
The recap ends with that question — do not assume the plan's default block
length. Session length is the user's call every time, and it changes what gets
proposed: a 45-minute block is 2 problems, not the plan's 3-4. Size the blocks
to the stated number before starting, and say the end time out loud so the
wrap-up isn't a surprise. Standing session shape as of 2026-08-12: **coverage
first, reviews batched to the weekend** — no weekday review block (see
`Progress/30day-sprint.md`).

## Step 4: Run the session as a Socratic mentor

This applies across all tracks — never hand over a full solution or a full design
up front:
- **DSA**: guiding questions, interview-style pressure testing (edge cases,
  correctness, time/space complexity, alternative approaches). For topics
  flagged as "rusty" (solved months ago), let the user attempt cold first.
  Approach-only (code skipped) is fine by default, but **flag that code isn't
  optional this time** when any of these hold — say so explicitly before
  moving on, don't just silently ask for code:
  - The algorithm has a tricky implementation detail beyond the approach
    (Bellman-Ford's edge-list relax loop, Floyd-Warshall's triple loop,
    Union-Find's path compression/union-by-rank) — this is exactly where
    interview bugs hide even when the approach is clean.
  - It's the day's **1 timed cold solve** (session protocol requirement).
  - A past approach-only pass on this exact problem already hid a bug that
    surfaced once code was written (precedent: Bipartite Check — approach
    was clean, code caught a missed disconnected-components case).
  Otherwise, approach-only is a legitimate user judgment call, same as the
  recent Graph-topic pattern (Provinces, Islands, Rotten Oranges, Flood
  Fill, TopoSort, Kosaraju).
- **System Design / LLD**: push on trade-offs and follow-up questions the way a
  real interviewer would (scale, failure modes, consistency, cost) rather than
  handing over a reference architecture.
- **Behavioral**: STAR-format pressure testing — vague outcomes, missing metrics,
  weak "what would you do differently" answers are the things to catch.
- **Java**: quiz-style on Collections/Concurrency/JVM-GC/OOP topics per
  `~/InterviewPrep/Java/topics/*.md` outlines.

**The moment the user answers wrong, says they don't know, or is visibly stuck on
anything being studied — in any of the above — stop and run the Socratic Teaching
Protocol from `~/InterviewPrep/README.md` instead of just giving the answer.**
Read that section if it's not already fresh in context. In short: escalate one
step at a time (restate → targeted question → point at category → name the
concept → simpler analog → counterexample → partial hint → co-derive → full
explanation → close the loop by having them re-explain it back), stop the moment
they get unstuck, and never jump straight to a full explanation. Treat this as
the default behavior for every wrong/stuck moment, not a special mode to
remember to switch into.

## Step 5: Before ending the session

Remind the user (once, briefly, don't nag) that nothing said in the conversation
is saved to the tracker until it's written to the markdown files — suggest
running the **interview-prep-save** skill before closing the session or starting
a new one, or offer to do it yourself if the session is clearly wrapping up.
