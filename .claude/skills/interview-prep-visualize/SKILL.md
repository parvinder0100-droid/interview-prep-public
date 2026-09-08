---
name: interview-prep-visualize
description: >-
  Refresh the "Interview Prep" NotebookLM notebook with the latest
  ~/InterviewPrep tracker files and generate high-level visual overviews
  (video, slide deck, mind map) — built to surface blind spots (repeat
  mistakes, stale "done" topics, zero-activity tracks), not just recap
  progress. Use at milestones — end of a sprint week, a track hitting a
  completion threshold, or whenever the user asks to "visualize my prep",
  "update NotebookLM", "generate an overview", or similar. Read-only
  against tracker files — only copies/uploads, never edits them.
---

# Interview Prep — NotebookLM Milestone Visualization

Refreshes the NotebookLM notebook registered as `interview-prep` (created
2026-07-24, share URL in the MCP library — `list_notebooks` to confirm it's
still there) with current tracker content, then hands the user ready-to-paste
prompts for NotebookLM's Video Overview / Slide Deck / Mind Map generators.
The generators are steered to hunt for things the user likely doesn't
consciously realize (recurring mistakes, false-"done" topics, silent
zero-activity tracks) — a plain recap is not the goal.

## Step 1: Confirm the notebook

`list_notebooks` (MCP) — if `interview-prep` isn't there, ask the user for
the share URL and re-register with `add_notebook` before continuing.
`select_notebook` to make it active.

## Step 2: Rebuild the filtered file set

Not every file in `~/InterviewPrep` is worth pushing — skip pure-stub files
(not-started topics with only template headers, empty mistake journals) and
`.claude/skills/*.md` (tooling, not prep content). A file is a stub if,
after its frontmatter and headers, every remaining line is empty or a
placeholder like `_None yet._` / `_No entries yet._` — check with a quick
`grep -v` pass per candidate file rather than assuming last time's skip list
still applies (topics move from stub to real content as they're started).

Flatten survivors into one directory with `/`→`__` in filenames (so e.g.
`DSA/Progress/progress.md` → `DSA__Progress__progress.md`), same pattern
used 2026-07-24:

```sh
DEST=<scratchpad>/notebooklm_upload
rm -rf "$DEST" && mkdir -p "$DEST"
cd ~/InterviewPrep
find . -name "*.md" -not -path "./.git/*" -not -path "./.claude/*" | while read -r f; do
  # skip if stub (see filter logic above), else:
  rel="${f#./}"; flat=$(echo "$rel" | sed 's#/#__#g')
  cp "$f" "$DEST/$flat"
done
```

## Step 3: Get the files into NotebookLM

**The MCP `add_source` tool has a known reliability bug** (confirmed
2026-07-24): it fails to open the "Add source" dialog consistently, even on
a 1-line test source, with or without `show_browser`. Don't burn more than
one retry on it. Default straight to the manual path:

1. Tell the user the folder path from Step 2.
2. Have them open it in Finder (Cmd+Shift+G → paste path), Cmd+A to select
   all, then drag the whole selection onto the "or drop your files" zone in
   their open NotebookLM tab.
3. If this is a re-push (files already existed from a prior milestone),
   duplicates will appear — point them at the "Find duplicates" tool in the
   NotebookLM sidebar (visible in the sources panel) to clean up after.

If the MCP tool has since been fixed (check by trying a single small test
source first — if it succeeds, proceed with it for the rest), prefer it
over the manual flow since it skips the Finder round-trip entirely.

## Step 4: Verify ingestion

`ask_question` (MCP) with something like "Summarize what these sources
cover in 3 sentences" — if the answer is a real grounded summary (not just
a "thinking"/planning preamble, which is a separate known glitch in this
tool's answer-extraction), sources are indexed. Otherwise tell the user to
eyeball the source count in the NotebookLM sidebar themselves.

## Step 5: Hand off the generator prompts

Give the user these three, adapted to whatever's actually current in the
dashboard/mistake journals at the time (name specific recurring items, not
placeholders — pull real problem/topic names before handing these over):

**Video Overview** (Customize box) — two-part: fast recap, then a
blind-spot hunt through mistake journals/progress notes for (a) mistakes
that recurred more than once without the user noticing the pattern, (b)
topics believed "safe" that sources flag as stale/rusty/unverified, (c)
stated-plan-vs-actual-behavior contradictions, (d) zero-activity
tracks/subtopics not being treated as urgent. Must cite real names, not
generic advice.

**Slide Deck** (Customize box) — reference deck: sprint status, one slide
per DSA pattern learned (core idea + which problems used it), standing
weak points pulled verbatim from repeat-rust flags, zero-activity tracks
called out plainly, next-session priorities pulled verbatim from
"Notes for Next Session" / "resume here" entries. Dense bullets, no
generic interview advice.

**Mind Map** — root at the sprint, branch into the five tracks, DSA
branches by topic then by pattern/mistake (mistake labels pulled from the
journal, not invented), other four tracks show started/not-started status,
one root-level branch for cross-track risks (stale import backlog, any
mistake/pattern recurring across different problems).

Adjust the specifics session-to-session — these are templates, not fixed
text; a Week 3 milestone should reference different named gaps than a
Week 1 one would.

## Step 6: Confirm briefly

One line: sources refreshed (count), which overview(s) were generated or
handed off as prompts. Don't re-summarize the tracker itself — that's
what the video/deck/mindmap are for.
