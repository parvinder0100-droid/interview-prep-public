---
system: DSA Mastery OS
source: Striver A2Z Sheet
created: 2026-07-06
---

# DSA Mastery OS — Knowledge Base

This is the persistent knowledge base for a long-term DSA mastery system built around the
Striver A2Z Sheet. It is maintained by Claude Code acting as a Socratic mentor, not a
solution generator.

## Purpose

- Track progress through every topic/subtopic of the Striver A2Z Sheet.
- Store one note per problem solved, with intuition, mistakes, and complexity — never a
  copy-pasted solution.
- Drive spaced repetition reviews (1, 3, 7, 14, 30, 60, 90 day intervals).
- Maintain a permanent mistake journal to catch recurring error patterns.
- Track confidence, weak topics/patterns, and interview readiness over time.

## Folder Structure

- `Progress/` — overall progress, statistics, and the review schedule queue.
- `topics/` — one file per Striver topic (Arrays, Strings, Trees, DP, Graph, ...).
- `patterns/` — one file per recurring pattern (Two Pointers, Kadane's, Backtracking, ...).
- `mistakes/mistake_journal.md` — permanent log of every mistake and its root cause.
- `flashcards/` — active recall flashcards grouped by topic.
- `recall/` — daily/weekly/monthly recall question logs.
- `notes/` — one self-contained Markdown file per problem attempted.

## How Sessions Work

1. **Startup**: read `Progress/progress.md` and `Progress/review_schedule.md`, surface
   today's due reviews, pending reviews, weak topics, and the suggested next problem —
   without asking where we left off.
2. **During the session**: Socratic questioning (Levels 1–10), incremental hints only when
   stuck, interview-style pressure testing (edge cases, correctness, complexity,
   alternatives).
3. **Shutdown**: update progress, statistics, review schedule, mistake journal, and
   generate tomorrow's revision list.

## Current Status

See [Progress/progress.md](Progress/progress.md) for the live snapshot.

**2026-07-10 update**: a Codolio export of this sheet was imported, showing real prior
progress — 195/455 (42.86%) solved overall. Binary Search and LinkedList are already
100% complete (review-only topics now). Confirmed gaps: Basics 0/31, Sorting 0/7,
Arrays 2/40, Strings 3/15, Recursion 2/25, Bit Manipulation 1/18. The export was
truncated before Steps 9+ (Stack/Queue, Sliding Window, Heaps, Greedy, Trees, BST,
Graphs, DP, Trie, Segment Tree, etc.) — that data is still pending import. This is no
longer a fresh start; it's a gap-filling sprint on top of real prior work.
