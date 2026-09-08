---
type: flashcard_review_log
updated: 2026-07-22
---

# Flashcard Review Log

Durable, git-tracked record of dashboard flashcard review activity (Leitner
box level, last-reviewed date, miss count per card). This is the canonical
source — any Claude session should read this file directly (not the
dashboard) to know what's been reviewed via flashcards.

**How this file gets updated**: the dashboard (`Progress/dashboard/dashboard.html`)
tracks review state client-side (box/lastSeen/wrong per card, driven by
clicking "got it"/"missed it"), since a static page can't write to git
directly. The dashboard has a "save progress to repo" button that copies
that state as JSON — when the user pastes it into a chat session, this file
gets updated from it (and the dashboard's embedded `SEED_STATE` gets
regenerated from this file, so the two stay in sync). Nothing here updates
automatically from browser activity alone; it requires that export+paste
step.

**Reading this at session start**: cards with a low box level (1-2) and/or a
non-zero `wrong` count are weak spots — cross-reference against
`mistake_journal.md` entries by pattern. A card matching a mistake_journal
entry flagged as chronic/repeat-decay that has since reached box 3+ (two
consecutive clean self-ratings) is a candidate to mark that chronic flag
resolved — verify with a real question before doing so, don't just trust
the self-rating alone.

## Card State

_No exports processed yet — click "save progress to repo" in the dashboard's
Flashcard Review section, then paste the copied JSON into a session to
populate this._

`- <card-id> — box: N/5 — last reviewed: YYYY-MM-DD — missed: N times`

## Export History

_Each time an export is processed, append one line here so staleness is
visible:_

`- YYYY-MM-DD — processed export, N cards updated`
