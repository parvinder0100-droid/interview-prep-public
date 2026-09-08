---
name: token_optimization_plan
status: proposed — nothing applied yet
created: 2026-09-01 16:51
---

# Token Optimization Plan — InterviewPrep tracker

Trigger: `/usage` showed `/interview-prep-save` = 20% of usage,
`/interview-prep-resume` = 8%, and 25% of usage at >150k context.

## Diagnosis

Cost is **not** in the SKILL.md files (14KB + 8KB, one-time). It is in the
tracker files the skills read and edit every run.

Measured 2026-09-01:

```
DSA/mistakes/mistake_journal.md    169KB  ~42k tok   161 entries, never rotated
DSA/Progress/progress.md           113KB  ~28k tok
Progress/dashboard.md               77KB  ~19k tok   1122 lines
DSA/Progress/review_schedule.md     36KB   ~9k tok
Progress/30day-sprint.md            26KB   ~6k tok
DSA/recall/daily.md                 21KB   ~5k tok
DSA/Progress/statistics.md          16KB   ~4k tok
                                   ----   -------
                          full read set   ~114k tok
```

`interview-prep-resume` Step 1+2 reads dashboard + 30day-sprint + progress +
review_schedule = **~63k tokens before the first word of actual work**.
`interview-prep-save` edits most of the same set. That is the >150k context line.

Root cause: three files meant to hold *current state* became *append-only logs*.

- `Progress/dashboard.md` — 1122 lines. `## Cycle` spans lines 14-369 (355 lines
  of superseded dated decision blocks). `## Top Weak Area Pointer` spans
  620-1067 (447 lines, same pattern). A dashboard should hold current state;
  history belongs in an archive.
- `DSA/Progress/progress.md` — `## Notes for Next Session` spans lines 665-1403
  (738 lines of accumulated session recaps).
- `DSA/mistakes/mistake_journal.md` — 161 entries, no rotation.

## Fixes, ranked

### 1. Archive superseded prose  (biggest win, ~55k tok saved per resume AND per save)

- `Progress/dashboard.md`: keep only latest cycle decision + Reviews Due +
  Track Readiness table + current Top Weak Areas. Move all superseded dated
  blocks to `Progress/dashboard_archive.md`. Target 77KB -> ~8KB.
- `DSA/Progress/progress.md`: keep last 3 session notes, move the rest to
  `DSA/Progress/session_notes_archive.md`. Target 113KB -> ~25KB.
- `DSA/mistakes/mistake_journal.md`: split to `mistakes/archive/2026-Q3.md`,
  keep current quarter live.

Nothing deleted, repo is git-tracked, fully reversible.
Check `tools/build_dashboard.py` still parses after the split — it reads
progress.md, mistake_journal.md, review_schedule.md, review_log_archive.md.
Archive files must either match the same format or be added to its read list.

### 2. Append by shell, not Read+Edit  (rule change in interview-prep-save)

Save currently forces a Read of a 113KB file just to append one line.

- End-of-file logs (`mistake_journal.md`, `DSA/recall/daily.md`): `cat >> file <<'EOF'`.
  Zero read cost.
- Mid-file lists (`progress.md` Completed Problems, ends at `## Topics Started`;
  `review_schedule.md` Upcoming Reviews): `sed -i` insert at the section anchor.

Add as a hard rule in the skill's "Token discipline" block, superseding the
current "use Edit, never Write" phrasing — Edit still forces a Read.

### 3. Resume reads slices, not whole files  (rule change in interview-prep-resume)

Skill currently says "Read". Replace with explicit slice commands:

- `sed -n '1,120p' Progress/dashboard.md` (after fix 1 lands)
- grep `review_schedule.md` for items due <= today only
- `tail -60` on progress.md session notes
- skip `30day-sprint.md` entirely outside `sprint` mode (skill already says this)

### 4. Cheaper model for save  (optional)

Add `model: claude-sonnet-5` to `interview-prep-save` frontmatter. Save is
mechanical file surgery once the mistake `Class` is chosen. Trade-off: that
classification judgment moves to Sonnet.

## Separate finding — correctness bug, not tokens

Two divergent copies of both skills exist:

```
~/.claude/skills/interview-prep-save/SKILL.md              10448 B
~/InterviewPrep/.claude/skills/interview-prep-save/SKILL.md 14703 B   (116-line diff on resume too)
```

- Project copy is **missing the "post-session only" rule** (user instruction,
  2026-08-27) — save must never run mid-session.
- User copy is **missing Step 0 (HH:MM timestamp)** and the note-link fields in
  the progress.md line format.

Whichever copy wins at runtime, a rule is lost. Consolidate to one file; the
merged version needs both the post-session-only rule and Step 0.

## Suggested order

1 + 2 + 3 together = roughly a 60% cut on both skills. 4 and the skill
consolidation are independent and can land any time.
