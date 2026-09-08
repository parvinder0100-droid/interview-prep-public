# CLAUDE.md

Read `README.md` first — it is the source of truth: tracks, cross-track rules,
Socratic Teaching Protocol, mistake journal convention, session structure,
spaced-repetition schedule. Nothing in this file duplicates it; this file is
only the pointer plus standing per-session behaviors.

## Skills

Use the `InterviewPrep:interview-prep-*` skills (resume/save/audit/pace/apply,
plus `interview-prep-archive`/`interview-prep-visualize`) for session flow —
they read/write the tracker files directly. Don't hand-edit dashboard.md or
progress.md outside a skill unless the user explicitly asks for a one-off fix.

## Standing rules (follow every session)

Learned from session corrections. Append-only: when a new correction reveals a
standing behavior, add one bullet at the end of this list (rule + short why) —
never restructure this file for it.

- **No priming hints, ever** — never name the pattern, technique, sub-steps, or
  components of an approach before the user's cold attempt (applies to reviews
  AND new problems). Includes when explaining *why* full code is required this
  time — justify in general terms (interview precedent, past bug history),
  never by listing the mechanism pieces. Record pattern names in
  `DSA/patterns/*.md`, not in chat.
- **OJ links**: whenever a new problem starts, give the LeetCode/GFG link up
  front and log it in that topic's `Problems Log` (e.g. `DSA/topics/<Topic>.md`)
  — not just when asked once. Paste as bare plain URL (no markdown `[text](url)`
  wrapping, no backticks) so the terminal auto-detects and makes it clickable.
- **Socratic on wrong/stuck answers**: escalate hints gradually; never hand the
  answer directly. Every escalation past a light clarifying nudge is a weakness
  signal — log it in that track's mistake journal per README convention.
- **Guided tracing when stuck mid-derivation**: walk the user through their own
  code/derivation one line at a time, asking at each step — don't trace it
  yourself and present the result.
- **Answer batched asks in one response**: user often sends multi-part
  messages; address every part in a single reply, no split turns.
- **No markdown tables in chat**: they render as raw pipes in the user's CLI.
  Use plain aligned text. (Tables inside tracker *files* are fine.)
- **Token discipline on saves**: prefer Edit over Write for tracker updates,
  keep entries terse, touch only the tracks actually worked this session.
- **Hint-grading rule**: instantiating an abstract question with concrete
  numbers/example (to make it testable) is NOT a hint — only counts as
  escalation if the mechanism/answer itself is revealed. If the user already
  stated the correct rule in general terms and only applies it to the
  concrete case, that's clean, not a repeat needing escalation. Corrected
  2026-07-27 after mis-flagging a clean Print-Subarray review as needing a
  hint / heading toward `[leech]`.
- **A correct answer closes the question — don't re-ask for a better-worded
  one.** Once the user has named the load-bearing fact, move on; asking the
  same thing again to get it phrased more formally reads as badgering, not
  rigor. Flagged directly 2026-08-13 ("you're irritating me with question 2
  every time") after Merge Intervals' last-interval justification was pressed a
  second time. Same class as the hint-grading correction above: judge the
  content, not the polish. If a first answer really is only the *rule* and not
  the *reason*, one re-aim is fair — a third pass is not.
- **No praise language.** Confirm correctness flatly ("correct", "that's it")
  and move to the next question. No "great question", "best question of the
  session", "nice catch". Flagged directly 2026-08-29 ("dont do fakeness here
  like this one"). Signal is carried by what gets asked next, not by praise.
- **Check a claimed generalization against the problem it cites.** When the user
  summarises a rule as "same as <earlier problem>", verify it against that
  problem before agreeing. 2026-08-29: "reject before accept — same as LC 40"
  was affirmed and is inverted with respect to LC 40, where accept must run
  first. An affirmed wrong rule is worse than an unstated one.
