---
type: statistics
updated: 2026-09-01
---

# Learning Analytics

## Overall Counts

- Questions solved (Codolio import, 2026-07-10): 195/455 (42.86%)
- Confirmed breakdown (12 of ~18 steps, see progress.md): 173/317
- ~~Stack/Queue, Sliding Window, Heaps, Greedy, Graphs, final section (~138 problems):
  confirmed by user (2026-07-10) as not covered — treat as genuine new-learning
  material, not a data gap~~ **superseded 2026-07-26**: user confirmed the full
  Striver A2Z sheet was solved ~2 years ago. These are **rusty 2yr recall**, not
  uncovered material — the import just never captured that pass. Same
  re-verification treatment as every other topic, longer decay window. See
  `progress.md` Current Position.
- Questions solved independently vs with hints vs failed: **derive this by
  grepping `../Progress/progress.md`** (`grep -c 'solved: independently'`,
  `grep -c 'solved: with-hints'`, `grep -c 'solved: failed'`) rather than
  hand-tallying a name list here — a hand-kept count+list previously drifted
  from its own enumeration (list had more names than the stated count, caught
  2026-07-25) because every new save had to remember to update two places in
  sync. `progress.md`'s per-problem lines are the single source of truth for
  this number going forward.
- Average solving time / hints per problem: not tracked — no real
  time-capture wired in (see `interview-prep-pace` Step 0). Don't recompute
  by hand; leave unstated rather than re-introducing a stale-prone estimate.

## Topic Mastery

- Topics mastered (100%, per import): Binary Search, LinkedList, BST — but **solved
  2-3 months ago with no practice since (user-confirmed 2026-07-10)**, so treat as
  "coverage confirmed, current recall unverified" until re-tested live
- Topics near-complete: Trees (92%, 3 unconfirmed gaps), Tries (86%, 1 known gap:
  Maximum XOR With an Element From Array), DP (79%, 12 unconfirmed gaps) — same 2-3
  month staleness applies
- Topics with the lowest recent-import coverage (priority order by gap size, **not
  "never learned"** — see the 2026-07-26 correction): Basics (0%), Sorting (0%),
  Arrays (5%), Recursion (8%), Bit Manipulation (6%), Strings (20%). Live work has
  since put Arrays at 27 problems re-verified (Basics/Easy/Medium subtopics
  complete, Hard untouched).
- Zero live activity **this cycle** (was "not started, confirmed 2026-07-10" —
  reclassified 2026-07-26 to rusty 2yr recall): the sheet's final section only.
  Stack/Queue, Sliding Window, and Graph have all had live sessions (Graph
  started 2026-07-25, 18 problems/algorithms through 2026-08-01, core
  algorithm list complete). **Heaps** started 2026-08-01 (5 problems through
  08-02) and **Greedy** 2026-08-02 (9 problems through 2026-08-11: Task
  Scheduler, N Meetings, Minimum Platforms, Jump Game I/II, Job Sequencing,
  Fractional Knapsack, Candy, Assign Cookies) — this line previously still read
  "zero", corrected 2026-08-08. **10 as of 2026-08-12** (+ Lemonade Change).
  **12 as of 2026-08-13** (+ Valid Parenthesis String, code closed; + Merge
  Intervals). **13 as of 2026-08-14** (+ Shortest Job First). Greedy remainder
  on the sheet: Minimum Coins, Insert Interval, Non-overlapping Intervals —
  Insert Interval was posed 08-14 and declined as boring, still queued.
  **Stack/Queue live count: 9 as of 2026-08-27** (+ LC 84 Largest Rectangle,
  LC 907 Sum of Subarray Minimums, LC 739 Daily Temperatures, plus LC 42's
  O(1)-space follow-up closed). 3 new problems in one 85-min session is the
  highest coverage rate of the cycle; prior best was 2.

## Pattern Mastery

- Patterns mastered: none yet, by the graduation bar (2 consecutive fully clean
  reviews at #3+ — the `Graduated` list in `review_schedule.md` is still empty).
  Closest: Second Largest, Next Permutation, Move Zeroes — each one clean review
  away. Binary Search On Answer, Fast/Slow Pointers, and BST-recursion are implied
  strong by 100% topic completion but have never been pressure-tested live.
- Patterns weak: Backtracking (Recursion topic only 8% done). Graph patterns
  live-verified 2026-07-25: traversal (BFS/DFS, visited-timing mistake
  recurred 3x same day), connected components, multi-source BFS, cycle
  detection (undirected clean, directed needed 3-color/Kahn's escalation),
  bipartite check (heavy escalation, odd-cycle derivation), topological
  sort, Kosaraju/SCC (heaviest derivation of the day, 3 escalation rounds).
  2026-07-26: Dijkstra added — core mechanics cold/clean, but complexity
  notation and negative-edge failure mode both needed real escalation, see
  `patterns/Dijkstra.md`. Bellman-Ford added 2026-07-26 (derivation clean,
  2 code bugs — see `patterns/BellmanFord.md`); Union-Find added 2026-07-27
  (rank-increment invariant wrong in code, see `patterns/UnionFind.md`).
  Floyd-Warshall closed 2026-08-01 (5th attempt on "why k outer"). MST
  (Kruskal's, Prim's heap, Prim's array) all solved 2026-08-01 — see
  `patterns/MST.md`, `patterns/FloydWarshall.md`. Full core graph-algorithm
  list now covered at least once.

## Trends

- **Judge-confirmation rate (new series, started 2026-08-30)**: 2026-08-30 was
  the first session of the cycle where **every** problem attempted was submitted
  and Accepted in-session (3/3). Prior sessions recorded solves without a judge
  submission — Frog Jump sat as "solved" from 07-10 with a crash bug, and Rat in
  a Maze entered 08-29 never judge-confirmed. Track this per session; a solve
  without a verdict is a derivation.
  **2026-08-31: 3/3 submitted, 2/3 Accepted** (LC 139, LC 46; LC 51 WA and
  abandoned). Two sessions, 6 submissions, 5 Accepted — the series is holding,
  and the one WA was caught by the judge rather than by the tracker, which is
  the point of it.
  **2026-08-31 session 2: 1/1 submitted, 1/1 Accepted** (M-Coloring, on the 3rd
  attempt — 1/1114, then 6/1114, then 1114/1114). Three sessions, 7 submissions,
  6 Accepted. Note the shape: both intermediate WAs were *mechanical* defects in
  a correct approach, and the second one was a trace the user had parked minutes
  earlier — the judge is now doing work the trace would have done for free.
  **2026-09-01: 3/3 submitted, 3/3 Accepted** (LC 37 Sudoku Solver, LC 136, LC
  137). Four sessions, 10 submissions, 9 Accepted. LC 37 needed 2 non-Accepted
  submissions first, both compile errors on the same `char` cast line. Also this
  session: LC 47 declined at approach and LC 260 posed but not started — neither
  counts, and the series only tracks what reached the judge.
  **2026-09-02: 3/3 submitted, 3/3 Accepted** (LC 260 Single Number III, LC 231
  Power of Two, LC 191 Number of 1 Bits). Five sessions, 13 submissions, 12
  Accepted. BitManip cut-list slot closes at 5/5.
- **Failure-site series (new, started 2026-09-01)**: of the 8 defects across LC
  37 and LC 137 this session, **8 were at the write step and 0 in the
  derivation** — wrong stride, wrong base case, `cols[i]` for `cols[j]` twice,
  missing cast, `%2` for a derived `%3`, `i<<1` for `1<<i`. Combined with
  2026-08-31 (all three M-Coloring WAs mechanical), two consecutive sessions
  where the approach was sound and every failure came from transcribing it. This
  is the argument for the 08-31 prescription — write the derived predicate first
  — which has now gone unrun twice.
- Confidence trend: **102 problems logged live as of 2026-09-02** (the 53/16
  figures below are a stale 2026-07-30 snapshot, kept only for the trend line).
  Earlier reading: 53 problems logged live, 16 solved cold with no hints (30%).
  Mean hints/problem by session is the usable series — derive it from
  `progress.md`'s `solved:` fields rather than restating a number here (see
  `../../tools/build_dashboard.py`, which charts it).
- Clean review rate (2026-07-30): **67%** — 79 completed, 53 clean. Down from
  71% because all 4 reviews on 07-30 needed a correction or escalation; that
  batch was 3 `[derive]` graph algorithms plus one `[derive]` stack problem,
  i.e. the hardest slice of the queue, not a random sample.
- Clean review rate (2026-07-27): **71%** — 75 reviews completed, 53 clean, the
  rest needing a hint or a real correction. So roughly 1 in 3.5 re-tests still
  finds something. Graded from each archive entry's prose by
  `../../tools/build_dashboard.py`; going forward entries carry an explicit
  `outcome:` token (see the save skill) and the number becomes measured rather
  than inferred.
- Clean rate by review number (2026-07-27): #1 74%, #2 72%, **#3 36%** — the
  drop at #3 is the standout signal, and the opposite of what a working
  interval ladder should show. Either the 7-day gap is too long or #3 is where
  the `[derive]` "why" questions start. Watch whether it holds as n grows (14
  graded at #3 so far).
- Failure-class distribution (53 mistake-journal entries, 2026-07-27):
  invariant-why 28, stale-recall 11, transfer-gap 6, code-vs-derivation 6,
  boundary 2. Entries before 2026-07-25 predate the `Class` field and are
  keyword-classified. **The dominant failure mode is knowing a procedure without
  being able to rebuild why it holds** — which is what the `[derive]` tag exists
  to catch, so `[derive]` items are the highest-value reviews in the queue.
- Mistake-source hotspots by pattern: Arrays 21, Arrays/Matrix 6, Graph 4,
  1D DP 3, Graph Traversal 3. Arrays reads as "done" by coverage and is still the
  single largest source of logged errors.
- Retention score: first real signal in — of 53 logged mistakes, 11 are `stale-recall`
  and multiple `[derive]` items have decayed within 24h of being "closed" (Print
  Subarray twice, Dijkstra's negative-edge mode twice in one day). Treat the
  79-100% coverage numbers on Binary Search/LinkedList/BST/Trees/Tries/DP as
  unverified until each is re-tested live; nothing in that group has been yet
  except Frog Jump.
- Interview readiness score: baseline ~43% raw coverage per Codolio, but coverage ≠
  readiness — the whole sheet is 2yr-stale recall (see correction below), the recent
  re-solve pass covered it unevenly, and the live signal since 2026-07-10 says
  re-verification finds real decay more often than not (31% cold-solve rate). Also
  DSA-only: SystemDesign 0/24 case studies, LLD/Behavioral/Java at zero logged.
- Revision backlog: ~160 problems awaiting first interview-speed review rep (32 Binary
  Search + 31 LinkedList + 16 BST + 36 Trees + 43 DP + 6 Tries — Frog Jump DP-3 done),
  elevated priority given the 2-3 month staleness — not a passive warm-up queue
- **Major correction (2026-07-26)**: full Striver A2Z sheet was solved ~2yrs ago
  (user-confirmed). Every topic — including Stack/Queue, Sliding Window, Heaps,
  Greedy, Graphs — is rusty 2yr recall, not new material. The "genuinely new" /
  "not covered" framing this file used to carry is struck through in place above;
  see `progress.md` Current Position for the full correction. Do not reintroduce
  "not started" language for a topic without checking that section first.
- Consistency streak: broken — no sessions 07-28 or 07-29; resumed 07-30.
  Show rate 12 of 21 cycle days (57%); gaps 07-14→07-16, 07-18→07-19, 07-28→07-29.
- Decay-rate datapoint (2026-07-30): Bellman-Ford's V-1 derivation and the
  negative-cycle condition were both **clean cold on 07-26 and both wrong on
  07-30** — 4 days, with a 2-day gap in the middle. First measurement of how
  fast a freshly-derived graph proof decays without a rep. Compare against
  Dijkstra, derived 07-26 and re-tested the same span: its attribution half
  *improved* to clean — the difference being that Dijkstra got repeat
  exposure on 07-26 (twice) while Bellman-Ford's derivation was touched once.
- Failure shape (2026-07-30, 4/4 reviews): mechanics recalled correctly in
  every case; what failed was consequences — what breaks, what it costs, why
  the rule holds. Consistent with `invariant-why` being the dominant class.
- Repeat-rust flag: Rotate Matrix (90°) rusted the same way twice (2026-07-12
  original solve, 2026-07-13 review #1) — full-row-reverse step not sticking,
  worth targeted re-practice before next review.
- Repeat-rust flag (2026-07-21): Rotate Array's "why" derivation has never
  landed across 3 reviews (mechanics recalled fine each time) — see
  ReversalAlgorithm pattern file.
- Repeat-rust flag (2026-07-21): Print Subarray with Maximum Sum's
  start=tempStart derivation decayed a 2nd time within ~24hrs of being
  "closed" 07-20 — needs an extra recall check before its next scheduled
  review, see Kadanes pattern file.
- Repeat-rust flag (2026-07-24): Next Greater Element's "why push original
  value not answer" derivation needed real escalation again at review #1 —
  2nd time this specific point needed help (1st was self-caught during
  original coding, not fully independent recall). Rotate Matrix (90°) and
  Frog Jump (DP-3), by contrast, both held clean/near-clean at their
  review #3 — repeat-rust is not universal across all `[derive]` items.
- Repeat-rust flag (2026-07-25): visited-at-push (not pop) recurred 3x in
  one session — BFS Traversal, DFS Traversal, then Flood Fill (3rd time,
  self-caught without a hint this time). Not yet fully automatic despite
  same-day repetition; watch on the next new graph-traversal problem.
- Repeat-rust flag (2026-07-26): Dijkstra's negative-edge failure mode needed
  full escalation **twice in one day** (10:20 original solve, 15:28
  Bellman-Ford contrast question) — 2nd occurrence of this exact point, 1 more
  triggers `[leech]`. Underlying gap is the monotonicity half of the
  correctness argument (attributed to the priority queue instead of the
  non-negative weights), not the mechanics.
- New failure class observed (2026-07-26): clean derivation in one session not
  surviving into code written in a **later same-day** session (Bellman-Ford's
  Vth detection round, derived 10:20, absent at 15:28). Distinct from
  ordinary decay — argues for coding an algorithm in the same session it's
  derived, or re-reading the note first.

- Streak broken (2026-08-13): Merge Intervals (LC 56) is the **first problem
  since 2026-08-05** where the greedy/invariant *why* did not need an
  escalation ladder — 8 consecutive problems had. Mechanics, code, complexity,
  the justification, and a dead-comparator observation all cold in one pass.
  One data point; the retest is the next unfamiliar justification.
- New failure surface (2026-08-14): first entry in this tracker where the
  **problem statement** was the blocker, not the mechanics or the *why* — SJF's
  algorithm and code came cold once "the order is yours to choose" landed, but
  8 minutes passed before that. Both this and the same session's declined
  Insert Interval are engagement/comprehension costs, a different axis from the
  invariant-why series. Sample of one on each; watch GFG-style terse statements.
- Sort-space checklist working (2026-08-14): 4th miss in the primitives/objects
  class, but the **first recovered in a single nudge** off the user's own
  checklist item (08-08, 08-11 both took real escalation). Two of the four are
  now one-nudge or clean.
- Narrower diagnosis (2026-08-13): on LC 678 the user located a dead-code
  defect in 2 questions but could not **construct** the input that exposes it
  ("this question is tough") until walked through it variable by variable.
  Counterexample construction, not proof comprehension, is the live weakness —
  distinct from the 08-05..08-12 justification entries above.

- Snapshot 2026-08-18 17:43 (`tools/build_dashboard.py`): 76 problems logged
  live, review backlog **72**, clean rate 69%, 27 active days. The backlog rose
  60 → 72 on a missed weekend batch (08-16/17), not on new intake — one skipped
  weekend costs roughly a full weekend's cap.
- Greedy *why* series, 8th occurrence (2026-08-18): mechanics + complexity cold,
  first answer to the justification a mechanics-restatement, closed by numeric
  instantiation in ~3 min inside a 10-minute block. The ladder's cost is now
  small enough to run by default rather than as an escalation.

## How This File Updates

After every completed problem or review session, append/update the relevant counters
above. Keep this file as the single source of truth for aggregate stats — per-problem
detail lives in `notes/` and per-topic detail lives in `topics/`.

Anything countable (solve counts, failure-class split, pattern hotspots, show rate,
review backlog) is computed from the source files by
`../../tools/build_dashboard.py` — run that instead of re-tallying by hand, and
paste its numbers here only as a dated snapshot. Hand-kept tallies in this file have
drifted before (2026-07-25).

When a framing turns out to be wrong, strike the old text through and mark it
superseded in place rather than deleting it — a silently rewritten history is how
"confirmed not started" survived here for a day after being disproven.
