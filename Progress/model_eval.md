---
type: eval
created: 2026-09-01
purpose: measure whether Sonnet-run prep sessions degrade against an Opus baseline
run_with: Opus (this file is the checklist for a periodic Opus session)
---

# Model Quality Check — Sonnet vs Opus on InterviewPrep

## Why this file exists

As of **2026-09-01** the user switched prep sessions to **Sonnet 5** to cut cost
(Opus 5 is $5/$25 per 1M tokens, Sonnet 5 is $2/$10; both 1M context). Mixing
models *inside* a session was ruled out — a mid-session switch re-sends the whole
conversation and prompt caches are model-scoped, so the Opus request after a
Sonnet session pays full uncached rate on everything. Model choice is therefore
**per session, start to finish, including the save.**

This file is the test that tells you whether that switch cost anything. It is
written to be run **by an Opus session**, later, against the Sonnet sessions that
accumulated in between. It is deliberately mechanical: every check is a grep or a
git command against files the save skill already writes, so the answer does not
depend on anyone's impression of how a session "felt".

**How to use it**: after ~8-10 Sonnet sessions, start one Opus session, tell it
"run Progress/model_eval.md", and have it fill in a row of the Results Log at the
bottom. Nothing else. That is one Opus session per two weeks — negligible cost,
and it is the only way to notice slow degradation, which by construction is
invisible from inside the sessions that are degrading.

---

## Session ledger — fill this in as you go

One line per session. **The `model` column is the whole point** — without it none
of the checks below can be attributed. Add the line during the save.

| date | model | minutes | problems | reviews | commit |
|---|---|---|---|---|---|
| 2026-09-01 | opus-5 | 92 | 3 | 0 | f279dba |
| 2026-09-03 | sonnet-5 | 22 | 0 | 1 | f026324 |
| 2026-09-03 | sonnet-5 | 17 | 1 | 0 | 30cef10 |

---

## The baseline: 2026-09-01, Opus, commit `f279dba`

A 92-minute session, 3 problems (LC 37, LC 136, LC 137), all judge-confirmed.
Measured output of the save that followed:

    files changed by the save          15   (a 16th, token_optimization_plan.md,
                                             was a pre-existing untracked file
                                             swept in by `git add -A` — ignore it)
    lines added                       547   (excluding that file)
    mistake-journal entries             5
    of those, carrying an explicit
      recurrence count                  5   ("2nd", "5th", "1st named", ...)
    recall questions written            5
    new pattern files                   1   (BitCountingModK.md)
    existing pattern files updated      1   (Backtracking.md)
    flashcards added                    9   (4 recursion + 5 bit manipulation)
    problem notes created               2

Three claims in that save were **cross-session** — they could not be produced
from the session alone, only by holding it against files written on other days.
These are the specific things to look for later, because they are the first thing
to disappear:

1. *"Derivation-to-code regression is 2 for 2 across two sessions, at an interval
   of minutes"* — required connecting LC 137's `%2` to M-Coloring's
   `i != prvNodeColor` from **2026-08-31**, and noticing that the gap had
   collapsed from 16 hours to minutes.
2. *"8 defects, 8 at the write step, 0 in the derivation"* — required classifying
   every defect by where it occurred and recognising the same shape as the
   previous session's three WAs. This became a new series in `statistics.md`.
3. *"PLAN B's '79 of 84 unnamed' is stale"* — the plan file asserted a number;
   `grep -c '^- \[ \]' DSA/topics/*.md` contradicted it. Caught by checking the
   claim instead of repeating it, and corrected in three files.

Also in the baseline, on the failure side, recorded honestly: **one priming leak.**
On LC 47 the dedup rule ("a set per recursive call, holding values already tried
at that position") appeared inside the mentor's own question. **The user caught
it, the model did not.** So the baseline is not a clean sheet — it is 1 leak per
4 problems attempted.

---

## Checks

Run all six. Each has a command, a baseline, and a threshold that means
"something is actually wrong" rather than "this session was quieter".

### Check 1 — Priming leaks

The worst failure mode: naming the pattern, technique, or a load-bearing step
before the user's cold attempt. It permanently contaminates that problem — it can
never be re-run cold — and the tracker's whole model of "solved independently"
depends on it not happening.

```sh
cd ~/InterviewPrep
grep -rn "declined at approach\|mentor's question\|named in the mentor\|priming" \
  DSA/Progress/progress.md DSA/topics/*.md | tail -20
```

Then read the last ~5 sessions' entries in `DSA/Progress/progress.md` and count
problems where the approach was handed over before a cold attempt.

- Baseline: **1 in 4 problems attempted** (LC 47), and the user caught it.
- Concerning: more than ~1 in 4, **or any leak that the save did not record.**
  An unrecorded leak is worse than a recorded one — it means the session also
  lost the ability to notice it, so the logged "solved independently" counts
  become unreliable.

### Check 2 — Cross-session accounting in the mistake journal

```sh
cd ~/InterviewPrep
# entries in the window, and how many carry an occurrence count
grep -c '^### 2026-' DSA/mistakes/mistake_journal.md
grep -A9 '^### 2026-' DSA/mistakes/mistake_journal.md | grep -c 'Recurrence:'
# how many claim a repeat rather than a first sighting
grep 'Recurrence:' DSA/mistakes/mistake_journal.md | grep -vc '1st'
```

- Baseline: every entry carries a `Recurrence:` line, and 4 of 5 cite specific
  prior dates.
- Concerning: entries that say `Recurrence: 1st` for something the journal
  already contains. That is the signature of a session that logged what happened
  in front of it and never read backwards. Spot-check by picking one `1st` entry
  and grepping the journal for its `Class:` value.

### Check 3 — Contradictions caught

The tracker is full of numbers that go stale — problem counts, backlog sizes,
"blockers" that were resolved in a later session. A good save notices when the
file disagrees with itself.

```sh
cd ~/InterviewPrep
grep -rn "stale\|CORRECTION\|correction, recorded\|disagree\|superseded\|falsified" \
  Progress/dashboard.md Progress/30day-sprint.md | tail -20
```

- Baseline: 1 per session over the last three (08-30 the review-backlog figure,
  08-31 the itemization blocker, 09-01 the "79 unnamed" correction).
- Concerning: a run of 8-10 sessions with **zero**. The tracker does not stop
  producing contradictions; it only stops having them noticed. Cross-check by
  re-running the verification yourself:

```sh
cd ~/InterviewPrep
grep -c '^- \[ \]' DSA/topics/*.md          # named vs TBD, vs what the plan claims
grep -c '^- ' DSA/Progress/review_schedule.md
```

### Check 4 — Judge discipline

Gate 4 of PLAN B: every problem gets a verdict, or the count is fiction. This
existed because Frog Jump sat as "solved" from 07-10 with a live crash bug.

```sh
cd ~/InterviewPrep
grep -c 'Accepted' DSA/Progress/progress.md
grep -n 'solved: ' DSA/Progress/progress.md | tail -20
```

- Baseline: 3/3 submitted and Accepted (09-01); the series in
  `DSA/Progress/statistics.md` § Trends stands at 10 submissions, 9 Accepted
  over four sessions.
- Concerning: problem lines logged with no verdict, or the series in
  `statistics.md` not updated. Both mean solves are being recorded on the
  session's own say-so again.

### Check 5 — Save completeness

```sh
cd ~/InterviewPrep
git log --format='%h %ad %s' --date=short -15
git show --stat --format='' <commit> | tail -3
```

- Baseline: 15 files, ~547 insertions for a 3-problem session. The support dirs
  are the ones that rot silently — `flashcards/`, `patterns/`, `notes/`,
  `recall/` — and they have been caught stale before (2026-07-21).
- Concerning: saves that touch only `progress.md`, `dashboard.md` and
  `mistake_journal.md`. That is the shape of a save that did the bookkeeping and
  skipped the distillation. Check directly:

```sh
cd ~/InterviewPrep
git log --format='%h' -10 | while read c; do
  printf '%s %s\n' "$c" "$(git show --stat --format='' $c | grep -c 'patterns/\|flashcards/\|notes/\|recall/')"
done
```

### Check 6 — Pushback

Hardest to automate, so do it by hand: read the last 3 sessions' entries in
`progress.md` and answer one question — **did the model ever tell the user they
were wrong about something the user had stated confidently?**

Baseline instances, all from 09-01: `board[i][j]+'0'` corrected as the wrong
variable; "an area of size thirty" corrected twice (32 slots, and bit 31 must be
counted); `(row+1)*3` refuted by substituting all three rows; the claim that
`(0,4)` and `(0,0)` share a box refuted before the user re-derived it.

- Concerning: sessions where every user answer is accepted and moved past. A
  model that grades a near-answer as correct produces clean-looking logs that are
  worth nothing — and this failure is invisible in the counts, which is why it
  needs reading.

---

## Decision rule

Stated in advance so the result isn't rationalised after the fact.

- **Checks 1-6 all hold** -> stay on Sonnet. The savings are real and free.
- **Only checks 5 (completeness) or 2 (accounting) slip** -> stay on Sonnet for
  sessions, run **one Opus session every ~10** whose only job is the audit and a
  cross-session synthesis pass. That is the cheap fix: the per-session work is
  fine, the long-horizon reading is what needs the bigger model.
- **Check 1 (priming) or check 6 (pushback) slips** -> go back to Opus for
  coverage sessions. These two corrupt the *data*, not just the write-up: a
  leaked pattern and a rubber-stamped wrong answer both enter the tracker as
  clean solves, and nothing downstream can distinguish them from real ones.
- **Check 3 (contradictions) at zero across 10 sessions** -> treat as check-1
  severity. It means the tracker has stopped being reconciled, which is the
  slow-motion version of the same failure.

Note the asymmetry deliberately: the cost of staying on Sonnet when it is not
good enough is a month of corrupted progress data, discovered late. The cost of
going back to Opus unnecessarily is money. They are not symmetric, so the
thresholds above are set to fail toward Opus.

---

## Results Log

Fill in one block per Opus check-in.

### 2026-09-01 — baseline established (Opus)

Not a comparison — the reference point. Numbers above under "The baseline".
Sessions run on Sonnet from here on; first check-in due after ~8-10 of them,
roughly 2026-09-15.

### <date> — check-in #1

    sessions in window        (n, dates, all Sonnet?)
    check 1 priming           pass / fail   (leaks per problems attempted)
    check 2 accounting        pass / fail   ('1st' entries that aren't)
    check 3 contradictions    pass / fail   (count in window)
    check 4 judge             pass / fail   (unverdicted solves)
    check 5 completeness      pass / fail   (files/commit, support dirs touched)
    check 6 pushback          pass / fail   (instances found, read by hand)
    verdict                   stay / hybrid / revert
    notes
