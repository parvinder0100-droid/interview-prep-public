---
type: topic
topic: DP (Step 16)
updated: 2026-08-28
status: in-progress — 44/56 (78.57%) per Codolio import, 2026-07-10 — solved 2-3 months ago, no practice since — rusty, HIGH PRIORITY for early re-verification given interview weight. Frog Jump (DP-3) **fully closed 2026-08-28** — all three 07-10 follow-ups answered and O(1)-space code Accepted; closing them exposed two defects in the "corrected" 07-10 recurrence (see Problems Log).
---

# Dynamic Programming

Imported from Codolio (`~/Downloads/codolio_dsa_progress.json`, 2026-07-10):
**44/56 (78.57%)** — strong coverage, but the export only itemized the first two
lectures; later DP lectures (2D/grid DP, DP on subsequences/strings, stocks, LIS,
partition-based, squares, etc. per standard Striver order) make up the rest of the 56
and aren't itemized — 12 unsolved somewhere in there, specific ones unknown.

## Subtopics (Striver A2Z order, partial detail)

- Lec 1: Introduction to DP (1/1, 100%).
- Lec 2: 1D DP (5/5, 100%) — Climbing Stairs, Frog Jump (DP-3), Frog Jump with K
  distances (DP-4), Maximum sum of non-adjacent elements (DP-5), House Robber (DP-6).
- Remaining ~50 problems across later lectures (2D/grid DP, subsequence/string DP,
  stock DP, LIS-based, partition DP, squares in matrix, etc.) — 38/50 solved per
  aggregate, 12 unsolved, not itemized in the export.

## Patterns That Show Up Here

_To be linked as problems are worked through._

## Problems Log

Confirmed solved (6): DP Introduction, Climbing Stairs, Frog Jump (DP-3), Frog Jump
with K distances (DP-4), Max sum of non-adjacent elements (DP-5), House Robber (DP-6).

- [x] Frog Jump (DP-3) — re-verified 2026-07-10 — solved: with-hints:1 — first
  attempt was pure Fibonacci recurrence (ignored height cost), corrected after one
  hint to `dp[i]=min(dp[i-1]+|h[i]-h[i-1]|, dp[i-2]+|h[i]-h[i-2]|)`. See
  [[mistake_journal]]. Follow-up pressure-test questions asked but
  **all answered 2026-08-28**: (1) n=1 returns 0, recurrence body never runs;
  (2) O(n)/O(n), one pass, dp array of size n; (3) O(1) space via two rolling
  variables, code written and Accepted.
- [x] Frog Jump (DP-3) — closure session 2026-08-28 — with-hints:2 — **two live
  defects found in code previously recorded as solved**: `dp[i-2]` indexed from
  `i=1` (crashes every n>=2 input, so it had never been submitted anywhere), and
  a roll of `backbytwo = oneStep` — a dp value plus a jump cost — which returns
  100 instead of 10 on `[0,10,100,10]` and is invisible for n<=3. See
  [[SpaceOptimizedDP]] and [note](../notes/frog-jump-dp-3.md).

Remaining ~50: aggregate says 38 solved / 12 unsolved but individual problems not
captured — confirm live given DP is high interview weight and this is the biggest
"mostly done but unverified" topic in the import.

**BLOCKER (2026-08-28)**: the 12 unsolved cannot be recovered from disk.
`codolio_import_raw.json` itemizes only Lec 1 (1 problem) and Lec 2 (5) of the
56 — every later lecture was dropped by the export, so 38 solved and all 12
unsolved are unnamed. Bucket 1 of the post-cut coverage queue ("DP gaps 12")
is therefore **not executable top-down** until the 12 are named from the
Codolio web UI. Picking an arbitrary later-lecture problem risks landing in the
*cut* 161-problem re-verification backlog instead. Take to the weekend audit.

## Common Mistakes Seen in This Topic

- 2026-07-10: Frog Jump (DP-3) — defaulted to memorized Fibonacci-shaped recurrence
  instead of deriving from the problem's cost function. See
  [[mistake_journal]].

## Cut-list queue — itemized 2026-08-31 (Day 0)

From `Progress/coverage_cut_list.md`. `- [ ]` = scheduled, not yet solved.

**12 slots — the blocker first raised 2026-08-28, still open.**
The archived `../codolio_import_raw.json` **cannot** resolve this: its export is
truncated, carrying 2 subtopics and 6 questions of DP's 56. Checked 2026-08-31,
recorded so it is not re-attempted. 44/56 were solved at import; the 12
unsolved need the Codolio web UI's per-problem checkmarks.

- [ ] TBD x12 — Codolio required
