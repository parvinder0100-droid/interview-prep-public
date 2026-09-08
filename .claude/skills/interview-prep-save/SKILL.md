---
name: interview-prep-save
description: >-
  Save, log, or persist this session's interview prep progress into the
  ~/InterviewPrep markdown tracker (DSA/Striver A2Z, System Design, LLD,
  Behavioral, Java). Use when the user wants to save progress, log what was
  covered, update the tracker, or wrap up before closing a session or starting a
  new one — phrases like "save my progress", "log what we did", "update the
  tracker", "save this before I close". Nothing discussed in a session persists
  until it's written to these files, so run this before context is lost.
---

# Save Interview Prep Progress

Everything of value from the session must land in files under `~/InterviewPrep`
— conversation history does not persist across sessions, the markdown tracker
does. This is a routine, frequent operation (potentially every session), so it
must stay cheap. The one-time deep reconciliation work done on 2026-07-10
(Codolio import, staleness analysis) was a rare exception — do not treat it as
the normal pattern to repeat.

## Token discipline (read this before doing anything)

- **Use Edit, never Write, for existing files.** Every update in this skill is a
  small, targeted change (append one line, bump a number, flip a status). Write
  requires re-outputting the entire file and forces a Read first — for files
  that only grow (dashboard.md, statistics.md, topic files), that cost compounds
  every single save. Use Edit's `old_string`/`new_string` to touch only the
  lines that actually changed.
- **Touch only the track(s) with real activity this session.** Do not read,
  open, or mention tracks that had zero activity — no "System Design: no data"
  filler, no scanning their files "just in case."
- **Keep new entries terse.** One line per problem, the standard mistake-journal
  field format (already short), one line per review-schedule entry. Do not
  write new multi-sentence explanatory paragraphs the way the 2026-07-10 import
  reconciliation did — that was a one-off data-recovery effort, not the
  template for routine logging.
- **Don't regenerate whole sections.** Dashboard/statistics updates are single
  number or line edits (e.g. bump a count in a table cell), not a rewrite of
  the surrounding prose. Only rewrite a prose paragraph (like "Top Weak Areas")
  if something genuinely new must be said — not to reflect one more solved
  problem in an already-documented weak topic.
- **Skip files with nothing new.** If nothing happened in review_schedule,
  statistics, applications, or the sprint plan this session, don't open them.
- **"Active track" includes its support dirs, not just progress/mistakes/
  reviews.** DSA also has `flashcards/`, `patterns/`, and `notes/` — these are
  real, load-bearing files (not optional extras) and go stale silently if
  skipped, the same way progress.md would. Terse still applies (a flashcard is
  1 Q/1-line-A, a pattern update is a few lines in an existing section) — stay
  terse, but don't skip the file entirely just because it's not
  progress.md/mistake_journal.md. This was flagged directly (2026-07-21) after
  `flashcards/*.md` sat empty since 2026-07-06 despite 30+ problems solved, and
  6 of 8 `patterns/*.md` stubs went unfilled for two weeks of active pattern
  use — both silently stale until an explicit audit caught them.

## Step 0: Capture the timestamp

Get current time (`HH:MM`, from the session's date/time context) before writing
anything. Same-day sessions are otherwise indistinguishable by date alone —
this bit the user 2026-07-26 when an earlier-same-day Dijkstra entry read as
ambiguous relative to a later same-day session. Use this `HH:MM` in every
timestamped entry below, not just the date.

## Step 1: Inventory what happened this session

Identify only the track(s) that actually had activity (DSA / SystemDesign / LLD
/ Behavioral / Java / Applications). For each active track, note: problems or
questions attempted (solved independently / with hints / failed), mistakes made
(including any point the Socratic Teaching Protocol had to escalate past a
light clarifying nudge — see `~/InterviewPrep/README.md`), and any plan
deviation worth recording. Ignore inactive tracks entirely.

## Step 2: Update per-problem/per-topic files (Edit, not Write)

For each item, on the specific track touched:

- `<Track>/Progress/progress.md` — append one line under Completed Problems:
  `- [ ] Problem Name — Topic/Subtopic — Difficulty — [note](../notes/problem-slug.md) — solved: independently | with-hints:N | failed — HH:MM`
  Omit the note link if no note file was created (see below). The `HH:MM` is
  the Step 0 timestamp — required so same-day multi-session entries are
  distinguishable.
- `<Track>/topics/<Topic>.md` — append one line to Problems Log; only touch
  `status:`/`updated:` frontmatter if the topic's overall state actually changed
  (e.g. went from in-progress to complete), not on every single problem.
- `DSA/Progress/statistics.md` — bump the relevant counts only if this is a
  DSA session (single-line edits to the counters, not a rewrite).
- `DSA/notes/<problem-slug>.md` — **only create this** if there's a real
  mistake, non-obvious insight, or rust worth remembering. A clean
  independent solve with nothing notable doesn't need a note file — the one
  line in progress.md is enough. Never paste a full solution. **If you link
  `[note](../notes/problem-slug.md)` from progress.md or mistake_journal.md,
  create that exact file in the same save** — a link to a file that doesn't
  exist is a broken reference (this happened 2026-07-20: Next Greater
  Element linked from two files, note never created, caught a day later by
  the user, not by this skill).
- `DSA/flashcards/<topic>.md` — append 1 short Q/A card per problem that
  taught something genuinely reusable (a technique, a gotcha, a rule of
  thumb) — skip routine/clean solves with nothing new to distill. Create the
  topic's flashcard file if it doesn't exist yet (existing files only cover
  arrays/dp/graphs/trees — e.g. `stack_queue.md` didn't exist until
  2026-07-20). Q on one line, A (intuition/complexity only, never full code)
  below it — same format already in the files.
- `DSA/patterns/<PatternName>.md` — if the problem used a named pattern,
  update (or create) that pattern's file: add the problem under "Problems
  Using This Pattern" (one line), add any new failure mode under "Common
  Pitfalls" (one line), flip `status: not-started` → `status: in-use` on
  first real use. Skip if the pattern file already covers this exact
  pitfall/problem. Never name the pattern to the user before their cold
  attempt (see [[feedback_no_priming_hints]]) — this file is where the name
  goes, not the chat.

## Step 3: Log every mistake — this is the core weakness log

For **any** mistake (coding, design, or behavioral), append one entry to that
track's `mistakes/mistake_journal.md` via Edit (insert after the last entry, or
after the "Log" header if it's the first). Never delete existing entries. Keep
each field to a short phrase, not a paragraph:

```
### YYYY-MM-DD HH:MM — Problem/Question/Concept
- Mistake:
- Root Cause:
- Correct Thinking:
- How to Avoid:
- Pattern (or Topic Area / Principle, per track):
- Class: boundary | invariant-why | stale-recall | transfer-gap | code-vs-derivation
- Recurrence: 1 | 2 | 3+ (of <problem/point this repeats>, else 1)
- Review Date:
```

`Class` is one of the five fixed buckets above — pick the closest fit, don't
invent a new one per entry. `Recurrence` only goes above 1 if this exact
point (not just the same problem) has genuinely come up before — check the
journal for a prior entry on the same point before guessing.

Free-form narrative additions (progress.md's "Notes for Next Session", topic
session recaps) should also lead with `YYYY-MM-DD HH:MM` instead of date-only,
same reason as Step 0.

## Step 3b: Recall log (DSA only, cheap)

If a Socratic escalation happened this session (Step 3), append one bare
question (no answer) to `DSA/recall/daily.md` under today's `## YYYY-MM-DD`
heading (create the heading if today's is missing) — question only, plus a
pointer to the mistake_journal entry, per the file's existing format. Skip
entirely if no escalation happened — don't manufacture a question just to
fill the log. Never write historical/backdated entries for past sessions this
skill didn't run for; only log live, same-session escalations going forward.

## Step 4: Update the review schedule (DSA, SystemDesign only)

For any problem/question newly solved, append one line to that track's
`Progress/review_schedule.md` under Upcoming Reviews (LLD has no review
schedule file yet — only create one if LLD problems actually start getting
solved):

`- Problem Name — due: YYYY-MM-DD — review #1 — [note](../notes/problem-slug.md)`

Intervals: +1, +3, +7, +14, +30, +60, +90 days — compressed toward the front
only if `Progress/cycle.md` mode is `sprint` and the interval would land past
`target_end`; in `maintenance`/`dormant` mode use the full uncompressed
intervals. If a review was completed this session, move that one line from
Upcoming Reviews to Completed Reviews Log (or `review_log_archive.md` — see
that file's own header) and add the next interval, unless the item just
graduated (see review_schedule.md's Graduated section) — don't touch unrelated
entries.

**Every archived review must carry an explicit `outcome:` token**, written
immediately after the completion date:

`- Problem Name — review #N — completed: YYYY-MM-DD — outcome: clean — <prose note>`

Grade with exactly one of three values, using the same bar as the Socratic
Teaching Protocol and the hint-grading rule in `../../CLAUDE.md`:

- `clean` — recalled unaided. Instantiating an abstract question with concrete
  numbers to make it testable does **not** count against this.
- `hint` — one light nudge or prompt was needed, but the mechanism came from
  the user.
- `correction` — the mechanism or answer had to be supplied, a real escalation
  chain ran, or a prior mistake recurred.

Write the token even when the prose already says "clean" — the prose is for a
human, the token is what `../../tools/build_dashboard.py` grades the retention
metric from. Without it, the dashboard falls back to keyword-matching the note,
which reads systematically low: a note saying "clean, no repeat of the old
rust" scored as a correction until that parser was fixed on 2026-07-27, and any
new phrasing can reintroduce the same class of error. Backfilling old entries
is not required — the parser handles both shapes and reports how many were
graded by keyword.

For problems re-verified from the "2-3 months stale" import backlog (Binary
Search, LinkedList, BST, Trees, DP, Tries): remove/check off just that one
problem from the Import Backlog list; log any rust as a Step 3 mistake entry.

## Step 5: Dashboard — targeted edits only

Update `~/InterviewPrep/Progress/dashboard.md` with small Edits, only for what
actually changed this session:
- Day counter / this week's focus — only if the date or week actually rolled
  over since the last save.
- Reviews Due Today — only add/remove the specific line(s) affected.
- Track Readiness Snapshot table — update just the cell(s) (Logged / Mistakes /
  Review Backlog) for the track(s) touched.
- Top Weak Areas / Active Applications — only rewrite if something genuinely
  new emerged (a new weak pattern, a new application stage) — not routinely.

## Step 6: Sprint plan — rare

Only touch `~/InterviewPrep/Progress/30day-sprint.md` if something this session
should change future weeks. This should be rare — most sessions don't need it.

## Step 7: Applications tracker

Only if an application went out, an interview got scheduled, or a stage
changed: append/edit the relevant line in `Applications/tracker.md` and the
matching dashboard line.

If the user describes how an actual interview round went (questions asked,
how they performed), create/update `Applications/debriefs/<company>-<round-
slug>.md` per the format in `Applications/debriefs/README.md` — this is
separate from the terse tracker `Notes:` field and is the durable record real
interview questions live in. Never fabricate a debrief the user didn't
actually report.

## Step 8: Commit the session (git snapshot)

`~/InterviewPrep` is a git repo with a private remote
(github.com/<owner>/InterviewPrep). After all file edits are done,
commit in one shot:

```sh
cd ~/InterviewPrep && git add -A && git commit -m "day N: <one-line session summary>"
```

Message = day number + terse summary in `sprint` mode (e.g. "day 12:
stack/queue intro, 8 reviews, STAR story 1"); in `maintenance`/`dormant` mode
use the date instead of a day number (e.g. "2027-03-02: graph review, 2
graduated-pool solves"). No push needed — a nightly launchd job
(`com.user.interviewprep-push`, 21:00) pushes any unpushed commits. If
nothing changed on disk this session, skip the commit (don't create empty
commits).

## Step 8b: Log deep work (standing behavior, added 2026-08-01)

Every time this skill runs and real work happened this session (Step 8 did
not skip an empty commit), also invoke the `deep-work-log` skill for the
session, project = "InterviewPrep <Track>" (the track(s) actually touched).
Don't re-run its full 6-question debrief from scratch — this skill already
gathered most of it:

- Objective / Done / Blocker / Root cause / Next action: derive from Step 1's
  inventory, Step 3's mistake entries, and progress.md's "Notes for Next
  Session" entry just written — draft them and show the user for a quick
  confirm/adjust rather than asking cold.
- Duration: **do not ask** (changed 2026-08-12, user instruction). The user
  declares a session length at resume, so take the duration from the actual
  clock — first prompt to last — and put the declared block in the objective
  line ("user-set 45-minute block"). Log actual elapsed, not the declared
  number: the pace forecast reads this field, and declared-vs-actual drift is
  itself signal. deep-work-log's rule against a bare duration still holds — the
  debrief fields above are what satisfies it, not the asking.
- Energy level: **do not ask** (same instruction). Write `—` in that column.

Skip this step only if the user explicitly declines, or if this save covered
zero real activity (nothing to log).

## Step 9: Confirm briefly

One short line, not a full dump — e.g. "Logged 2 Arrays problems + 1 mistake,
updated review schedule. Day 3, DSA 197/455." Bump `updated:` frontmatter only
on files actually touched.
