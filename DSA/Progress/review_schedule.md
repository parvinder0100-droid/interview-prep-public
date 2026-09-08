---
type: review_schedule
updated: 2026-09-04
---

# Review Schedule Queue

Spaced repetition intervals used for every completed problem:
Review 1 = +1 day, Review 2 = +3 days, Review 3 = +7 days, Review 4 = +14 days,
Review 5 = +30 days, Review 6 = +60 days, Review 7 = +90 days — compressed
toward the front only when `../../Progress/cycle.md` mode is `sprint` and an
interval would otherwise land past `target_end`. In `maintenance`/`dormant`
mode, use the full uncompressed intervals.

Completed reviews live in `review_log_archive.md`, not inline in this file —
this file only holds what's still due or upcoming, so it stays scannable as
volume grows.

**`[derive]` tag**: items with repeat-rust on memorized procedures. Their
review starts with the "why" question (e.g. "why does reversing both chunks
then the whole array rotate?") before any code — unable to derive = failed
review even if code is correct.

**`[leech]` tag** (added 2026-07-25): items that have needed real correction
on the *same specific point* 3 or more times (across the original solve and
subsequent reviews) — mechanics are fine, but the "why" keeps failing to
stick. Leech items come off the normal interval ladder and instead get a
short daily/every-other-day recall (just the stuck point, not the whole
problem) until 2 clean answers in a row, then re-enter the ladder at review
#3. Track candidates that are at 2 occurrences with a note — the tag is only
added on the 3rd.

**Graduation rule** (added 2026-07-25): an item that gets 2 **consecutive**
fully clean (no hints, no nudges) reviews at #3 or later moves to the
`## Graduated` list below and stops being scheduled — the ladder isn't meant
to run forever on material that's already solid. A nudge/hint resets the
"consecutive" count to zero even if the underlying answer was ultimately
right. Graduated items are the pool `interview-prep-resume`'s re-baseline
step (long-dormancy reopen) and `cycle.md`'s dormant-mode weekly quota draw
from.

Hard cap 12 reviews/session; overflow rolls forward, early pulls allowed,
batch-late never.

**REPLACED 2026-08-30 (audit, day 52) — reviews move inside the coverage block.**
The weekday/weekend split below never executed: 11 consecutive zero-review
sessions, 6 consecutive weekends at zero, 0 leech recalls in 17 days. New
mechanism, non-optional:

- **Every session opens with 2-3 review questions** on the *previous* session's
  problems, plus the stuck point of any `[leech]`. ~5-8 min, before new coverage.
  Questions come from that problem's "Open on:" text in this file — they are
  already written, one per entry.
- **No separate batch, no cap, no weekend slot.** Throughput is 2-3/session, so
  the ~47-item overdue set is worked opportunistically, not drained. Accepted.
- **The backlog was NOT archived** (considered and rejected 2026-08-30): the
  08-27 cut already removed every calendar-only item, so what remains is the
  `[derive]`/`[leech]` set that cut protected. An elapsed interval is not signal;
  a `[derive]` tag is.
- **Reversal trigger**: 3 consecutive sessions opening without their review
  questions means this failed the same way the batch did — escalate to
  `../../Progress/cycle.md` rather than redesigning a third time.

Historical, kept for the record — **weekday/weekend split, adopted 2026-08-11**
(see `../../Progress/30day-sprint.md`, DSA-First Coverage Plan). The
"batch-late never" rule above still binds the `+1` interval and nothing else:

- **Weekdays**: review *only* the previous day's problems (the `+1`) plus any
  `[leech]`. ~15 min. The `+1` is the steep part of the forgetting curve and
  cannot be moved.
- **Weekends**: everything else — `+3 / +7 / +14 / +30` and backlog — in 2
  sessions, cap 12 each. Later intervals are not date-sensitive; a `+14`
  landing on day 16 costs almost nothing.
- **Missed weekend**: the next weekday's review block expands to the full 12
  rather than letting two weekends stack.
- **Known consequence**: weekday intake is 15-20 new items/week against 24
  weekend capacity, so the backlog is held flat, not drained. Revisit if the
  clean-rate starts falling.

## Import Backlog (~161 problems: Binary Search, LinkedList, BST, Trees, DP, Tries)

User confirmed (2026-07-10) these were all solved **2-3 months ago**, with no practice
since — not "unknown date," but "known stale." That's a real forgetting-curve risk, not
just a formality. Treat this as **elevated priority, not a background warm-up**:

- **Week 1, start immediately**: DP (44 solved, highest interview weight — verify this
  first) and Binary Search (32 solved) — interview-speed re-solves, 5-8 problems per
  session, log any rust as a fresh mistake in `../mistakes/mistake_journal.md` (decay
  is real signal, not noise). Frog Jump (DP-3) re-verified 2026-07-10 — rust confirmed
  and corrected (1 hint), see mistake_journal. Review #1 wrap-up 2026-07-11 surfaced a
  second rust bug (missing dp[2] base case), corrected. **CLOSED 2026-08-28** — all
  three 07-10 follow-ups answered and O(1)-space code Accepted; closing them exposed
  two further defects (out-of-bounds at `i=1`, wrong roll), so the 07-10/07-11
  "corrected" code had never actually been run on a judge. 43 DP problems still
  unverified — **and the 12 unsolved ones are unnamed on disk**, see topics/DP.md.
- **Week 1-2**: LinkedList (31), BST (16), Trees (36, only 13 itemized).
- **Lower urgency**: Tries (6, small surface area, quick to re-verify whenever).

Goal: surface any decay now, while there's 3+ weeks to re-solidify, instead of
discovering it during Week 4 mock interviews. (Note: "3+ weeks" was sprint-mode
framing — in maintenance/dormant mode this backlog has no deadline pressure but
the same decay risk; work it down opportunistically instead.)

## Graduated

- **Rotate Array** — graduated 2026-08-15. Was `[leech]`; took its 2nd
  consecutive clean recall (08-01 review #4 via concrete trace, 08-15 cold with
  no hints: "a segment reversed twice returns to its original internal order,
  while the two blocks swap position"). Off `[leech]` and off the ladder.
  First item to graduate since the mechanism was added 2026-07-25.

_Others still one clean review away are flagged inline below in Upcoming
Reviews (Second Largest, Next Permutation, Move Zeroes)._

## Upcoming Reviews

_Sorted by due date, oldest first. Added as problems are completed:_

`- Problem Name — due: YYYY-MM-DD — review #N — [note](../notes/problem-slug.md)`

- Sudoku Solver (LC 37) `[derive]` — due: 2026-09-02 — review #1 — Accepted 10/10 on 2026-09-01, do NOT re-run the code. **Open on three things, two of them arithmetic**: (1) derive `box = (r/3)*3 + c/3` from scratch and say why the `/3` and `*3` do not cancel — this took 12 minutes and a cinema-seat analog and was ultimately handed over; (2) which cell follows `(0,4)` walking a 9x9 row-major, and what the flat-index termination test is; (3) state why `isValid` must not write to the board — see [note](../notes/sudoku-solver.md)
- Single Number (LC 136) — due: 2026-09-02 — review #1 — Accepted 2026-09-01, cold, code trivial — do NOT re-run it. **Open on one thing**: name the two operator laws that license reordering the XOR fold, and give the reason `x^x=0` alone is not enough (the duplicates are not adjacent). Handed over on 2026-09-01
- Single Number II (LC 137) `[derive]` — due: 2026-09-02 — review #1 — Accepted 2026-09-01, do NOT re-run the code. Derivation was complete and cold; **the review is about the write step**: (1) say why XOR fails for triples, in the "count mod 2" framing; (2) why bit 31 is counted and not skipped; (3) justify calling a 32-slot array `O(1)`. Also re-ask the `%2`-for-`%3` slip directly — see [note](../notes/single-number-ii.md)
- Power of Two (LC 231) — due: 2026-09-07 — review #2 — review #1 (2026-09-04) outcome: hint (closed via odometer ELI5 analog; Integer.MIN_VALUE single sign bit underflows to Integer.MAX_VALUE on n-1, so (n & (n-1)) == 0 holds; resolved with n > 0 guard because powers of 2 cannot be negative) — see [note](../notes/power-of-two.md)
- Number of 1 Bits (LC 191) — due: 2026-09-03 — review #1 — Accepted 2026-09-02, clean solve, nothing to re-drill — ask complexity only (not reached 2026-09-03, session ran out of time)
- Single Number III (LC 260) `[derive]` — due: 2026-09-06 — review #2 — review #1 (2026-09-03) outcome: hint. Item 1 (split precision) recurred — "either"/"uncertain" imprecision from the original solve resurfaced as "the other is uncertain" before self-correcting to "certain, 0" on 1 targeted question. Item 2 (any-bit generality) defended MSB specifically first, needed re-aim to "any bit", then needed a 2nd push for the *why* (that bit is a difference bit between x,y) — see [note](../notes/single-number-iii.md)
- M-Coloring (GFG) `[derive]` — due: 2026-09-01 — review #1 — **NOT REVIEWED 2026-09-01, session opened with new problems; item (1) below, the complexity, was carried into the session plan and dropped with it** — Accepted 1114/1114 on the 3rd submission, do NOT re-run the code. **Open on three things**: (1) the complexity, which was never reached — `m` colours over `V` vertices, plus the per-node scan cost; (2) why the driver loops all `V` instead of calling `dfs(0)` — give the `V=3, edge 1-2, m=1` counterexample; (3) restate the legality predicate in one sentence, since the derived version and the coded version disagreed — see [note](../notes/m-coloring.md)
- Combination Sum II (LC 40) `[derive]` — due: 2026-08-30 — review #1 — Accepted 2026-08-29, do NOT re-run the code. **Open on both defects, which were pre-written in the tracker and reproduced anyway**: (1) state which terminal check runs first and the input that proves it; (2) state why declining a value must decline every copy, and why `[1,1,6]` survives that rule — see [note](../notes/combination-sum-ii.md)
- Subsets II (LC 90) — due: 2026-08-30 — review #1 — independent, cold, correct first submit, complexity cold — do NOT re-run the code. **Open on one thing only**: why `Arrays.sort` is required — the mechanism (adjacent-only comparison + one canonical spelling per subset), not the symptom. Ended in "just tell me" on 2026-08-29
- Rat in a Maze (GFG) `[derive]` — due: 2026-08-30 — review #1 — code correct on review but **never confirmed on the judge**, so this review re-runs it. Open on three things, all declined 2026-08-29: (1) complexity including the cost of `s+"D"`; (2) ~~the symptom if the `maze[curx][cury]=1` restore is deleted~~ **CLOSED 2026-08-30** — answered on LC 79 via the `[["A","B"],["A","D"]] / "AAB"` counterexample; the mark is path state, not visited-ever; (3) the precondition rule stated so it covers *both* this and LC 40 — see [note](../notes/rat-in-a-maze.md)
- Letter Combinations of a Phone Number (LC 17) — due: 2026-08-31 — review #1 — **Accepted on the judge 2026-08-30**, approach was cold and complete — do NOT re-run the code. Open on two things: (1) state the auxiliary space of the `res+c` version and *why* it is `O(n²)` (this was derived once, after a 4-frame trace — check it survives a day); (2) state the standing empty-input test for any recursion that records at a leaf — see [note](../notes/letter-combinations.md)
- Word Search (LC 79) `[derive]` — due: 2026-08-31 — review #1 — **Accepted on the judge 2026-08-30** — do NOT re-run the code. **Item (1) CLOSED 2026-08-30 21:00, clean, no nudge**: "chain the four calls directly with `||` in one return, no intermediate variables, so short-circuit stops later calls." Still open: (2) time and space complexity, and the restore symptom **cold** — see [note](../notes/word-search.md)
- Combination Sum III (LC 216) `[derive]` — due: 2026-08-31 — review #1 — **Accepted on the judge 2026-08-30**, do NOT re-run the code. **CLOSED 2026-08-30 21:12, outcome: hint** — 3rd asking (2 prior handovers), this time closed via 3-step guided derivation (restate -> targeted nudge -> close) rather than being told: user derived "sum==n, cnt<k can never recover" unaided once framed, then named the wasted-search consequence unaided. First time this item wasn't fully handed over — see [note](../notes/combination-sum-iii.md)
- Word Break (LC 139) `[derive]` — due: 2026-09-01 — review #1 — **Accepted on the judge 2026-08-31** — do NOT re-run the code. Open on two things, both of which had to be dragged out in-session: (1) give an input where taking the first matching dictionary word returns the wrong answer, cold, and say what line prevents it; (2) state why storing `true` under `start+"-"+i` while reading `start+"-"+start` is a *cost* bug and which results survive in the cache. Complexity `O(n³)` was derived, re-ask it — see [note](../notes/word-break.md)
- Permutations (LC 46) — due: 2026-09-01 — review #1 — **Accepted on the judge 2026-08-31**, structure cold and correct — do NOT re-run the code. Open on the two precedence bugs, asked as one question: what does `mask & (1<<i) == 0` parse as, and what is `1<<(n+1)-1` at n=3? Also re-ask complexity — `2^n` was the first answer, `O(n!·n)` the corrected one
- N-Queens (LC 51) — **OPEN, not scheduled, 2 declines** — 2026-08-29 approach-only; 2026-08-31 code written **greedy-iterative** (no recursion, no undo), WA on n=4, abandoned before the rewrite. The approach has now been restated cold twice and the fix was named correctly by the user ("backtrack and try column 1 in row 0") — what is missing is only the code. **LC 131 came off the coverage list at 3 declines; this is at 2.** Resume by writing `solve(row)` with the base case and the three set-undos, nothing else — see [note](../notes/n-queens.md)
- Palindrome Partitioning (LC 131) — **OPEN, not scheduled** — approach only, no code, session ended 2026-08-29 mid-derivation at "how many children does a node at `i` have". Resume there, cold, then full code. **Declined a 3rd time 2026-08-30** ("lets not go in this ques yet") — the index line was drawn and the two generalization questions posed, neither attempted. Three sessions, no code. **Take to the audit: either it gets a dedicated block or it comes off the list.** Note LC 17 the same session ran the same machinery (index into a string, loop at a level, recurse on the rest) cleanly — so the blocker is not string indices as such, it is choosing a **variable-length** piece (`j` over `i..n-1`) rather than advancing by a fixed 1
- Frog Jump (DP-3) `[derive]` — due: 2026-08-29 — review #1 — closed 2026-08-28 after 7 weeks open; O(1)-space code Accepted, do NOT re-run it. **Open on the invariant**: state what `backbyone`/`backbytwo` hold at the top of iteration `i` *before* writing any code, then say why `n<=3` hides a wrong roll. Test that must be run: `[0,10,100,10]` (expect 10) — see [note](../notes/frog-jump-dp-3.md) and [[SpaceOptimizedDP]]
- Subsets (LC 78) — due: 2026-08-29 — review #1 — independent, cold, correct first submit; do NOT re-run the code. **Open on complexity**: state time and space unprompted, including what recording one answer costs — O(2^n) was the first answer and needed a nudge
- Combination Sum (LC 39) `[derive]` — due: 2026-08-29 — review #1 — **re-attempt cold, full code, and without a `Set`**. Then: name the redundant branch and give the two paths that produce the same combination (this was asked on 2026-08-28, not identified, and ended in "just tell me") — see [note](../notes/combination-sum.md)
- Binary Subarrays With Sum (LC 930) `[derive]` — due: 2026-08-29 — review #1 — code written 2026-08-25 and **verified correct** (`[1,0,1,0,1]/2`, `[0,0,0]/0`, `[1]/0`) — do NOT re-run it, that proves nothing. **Open on the why**: state the shrink loop's exit invariant including the empty case, then O(n)/O(1) with justification, then name an edge case unprompted. All three were asked for twice on 2026-08-25 and never given — see [note](../notes/binary-subarrays-with-sum.md)
- Asteroid Collision (LC 735) `[derive]` — due: 2026-08-26 — review #1 — **short interval (2d), not the +1/+3 ladder** — user decision 2026-08-24: failed cold twice, and the 08-24 cold re-attempt reproduced 08-23's exact bug, so the normal spacing has no evidence behind it here. Re-attempt **cold, full code**; do not re-read the note first. Tests that must be run before declaring done: `[-2,-1,1,2]`, `[8,-8]`, `[10,2,-10]`, `[1,-2,-3]` — see [note](../notes/asteroid-collision.md)
- Trapping Rain Water (LC 42) `[derive]` — due: 2026-08-29 — review #1 — code was cold and correct on first submit, and complexity/edge cases were stated — do NOT re-run the code. **Open on the boundary rule**: why the tallest bar each side and not the nearest taller one (5 escalations to get there, all spent on template-first retrieval), then the O(1)-space two-pointer version, which was left unattempted — see [note](../notes/trapping-rain-water.md)
- Largest Rectangle in Histogram (LC 84) — due: 2026-08-30 — review #1 — solved with-hints:2 2026-08-27; approach, `nsr-nsl-1` and the justification were all cold, so **do not re-run the code**. Open on: why ties are harmless here but not on LC 907, and the amortized O(n) argument
- Sum of Subarray Minimums (LC 907) `[derive]` — due: 2026-08-30 — review #1 — **short interval (3d), not the +1/+3 ladder** — two defects on first write (duplicate double-count, int overflow) and the tie rule was carried over wholesale from LC 84. Re-attempt **cold, full code**. Mandatory tests before declaring done: `[2,2]`, `[3,1,2,4]` (=17), and a magnitude check on `n=3e4` — see [note](../notes/sum-of-subarray-minimums.md)
- Daily Temperatures (LC 739) — due: 2026-09-03 — review #1 — solved independently, cold, first submit, Accepted 0 ms. Nothing to re-drill on the code; ask only for the `>=` justification and move on
- Minimum Coins of 1, 2, 5 and 10 (GFG) `[derive]` — due: 2026-08-22 — review #1 —
  solved independently 2026-08-18, code and O(1)/O(1) cold; the *why* took 2
  escalations. Ask the exchange argument only (mechanics are not in question):
  "drop one 10 — fewest coins that cover it, and what does that prove?" Follow
  with the scope question: does the same argument work for {1,3,4}?
- Dijkstra's Algorithm `[derive]` — due: 2026-08-22 — review #3 — review #2
  (2026-08-15) **clean**: the contradiction proof came out cold in prose —
  a shorter path must route through another node, and non-negative weights mean
  the remaining segment can only add, so the alternative prefix is already
  ≥ `dist[u]`. Handed over entirely on review #1; produced unaided this time.
  Not numbered as asked, but judged on content per the CLAUDE.md polish rule.
  Next review: if clean again it graduates (2 consecutive clean at #3+).
- Bellman-Ford Algorithm `[derive]` `[leech]` — due: 2026-08-16 — review #3 — daily recall (0/2 clean) —
  [note](../notes/bellman-ford.md) — review #2 (2026-08-15) **not clean, both
  points repeated verbatim from review #1**: `V-1` justified by degree ("any
  node has at most V-1 edges connecting to it"), and a still-improving Vth
  round again called a negative *edge*. **Tagged `[leech]` 2026-08-15** on the
  tag's own definition — 3rd correction on the same two points, and the
  07-26→07-30 window shows these go clean→failing in 4 days. Daily short
  recall on just these two questions, in this order, until 2 clean:
  (1) "does Bellman-Ford work on graphs with negative edges? so what can a
  Vth-round improvement mean?" — self-corrected to *cycle* in 2 steps today;
  (2) "can a shortest path repeat a node? therefore how many edges?" — closed
  in 2 steps today. Do **not** open with "why V-1"; it has failed twice.
  Code guards (`dist[u]!=INF` on *both* loops, `while(changed)` trap) still
  unretested — after the leech clears.
- Min Stack `[derive]` — due: 2026-08-06 — review #3 — review #2
  (2026-07-30) not clean: opened with the wrong mechanism (getMin treated as
  a local/windowed min), self-corrected via own push/pop construction. Next
  review: state what getMin promises *before* arguing storage
- Longest Repeating Character Replacement `[derive]` — due: 2026-07-25 —
  review #1 — false belief net window can shrink post-shrink, corrected via
  guided trace
  bug (self-caught this time via trace), watch closely next review
  self-derived, no hints
- Cycle Detection (Directed, DFS+BFS) `[derive]` — due: 2026-07-26 —
  review #1 — start with "why does plain visited fail on directed graphs"
  before mechanics; 3-color naming and Kahn's exact termination check both
  needed a nudge this time
- Bipartite Check (LC 785) `[derive]` — due: 2026-07-26 — review #1 —
  start with "why odd cycle breaks bipartiteness" before code; needed heavy
  escalation this time (2 failed attempts before light-switch analog
  landed). Also re-check the disconnected-graph outer-loop fix holds.
  needed 1 nudge (finish-order direction), watch for recurrence next review
- Kosaraju's Algorithm (SCC) `[derive]` — due: 2026-08-18 — review #2 —
  review #1 (2026-08-15) **clean, cold, complete** — finish-order puts a node
  of a source component on top, reversing the edges traps traversal inside a
  component, internal reachability survives the reversal. Needed 3 escalation
  rounds on the original pass; needed none this time. Biggest single
  improvement in the 08-15 batch.
  hint, same loop-bound point as original solve, self-corrected via trace
- Nearest Smaller to the Left `[derive]` — due: 2026-08-22 — review #3 —
  review #2 (2026-08-15) **clean**: code cold and correct (verified on
  `[1,6,4,10,2,5]`), pop-comparison rule given cold *with* its reason (pop
  everything that can no longer be the answer). Direction rule needed one
  concrete re-aim ("nearest smaller to the *right* — which way?") and was then
  correct for both variants — **not counted as a 3rd occurrence** per the
  hint-grading rule (instantiating is not a hint), so **no `[leech]`**; stays
  at 2. Still unstated: *why* the direction rule holds (traverse from the far
  side toward the searched side, so the stack holds only already-visited
  elements on that side) — that was handed over.
- Stock Span Problem `[derive]` — due: 2026-07-27 — review #2 — review #1
  clean, no repeat of the off-by-one
- Next Greater Element `[derive]` — due: 2026-07-27 — review #2 — review #1
  needed heavy escalation on the "why pushing ans[i] breaks it" derivation
  (2nd occurrence) — 1 more repeat triggers `[leech]`
- Implement Queue using Two Stacks `[derive]` — due: 2026-07-27 — review #2 —
  review #1 clean, no hints
- Spiral Traversal `[derive]` — due: 2026-07-27 — review #3
  clean, also correctly derived unequal-count leftover-append variant
- ~~Rotate Array `[leech]`~~ — **GRADUATED 2026-08-15**, see `## Graduated`
  above. 2nd consecutive clean, cold, no hints.
- Longest Subarray with Sum K `[derive]` — due: 2026-08-04 — review #4 — [note](../notes/longest-subarray-sum-k.md) — 1 hint, extra +1 confusion self-corrected
- Next Permutation `[derive]` — due: 2026-08-04 — review #4 — [note](../notes/next-permutation.md) — review #3 clean; **if clean again, graduates** (2 consecutive clean at #3+)
- Kadane's Maximum Subarray Sum `[derive]` — due: 2026-08-04 — review #4 — [note](../notes/kadanes-max-subarray.md) — order recalled clean, "why" needed 1 hint last time
- Rotate Matrix (90°) `[derive]` — due: 2026-08-07 — review #4 — review #3
  clean, both historically-buggy points (diagonal i<j, full row-reverse
  bounds) held that time
- Frog Jump (DP-3) `[derive]` — due: 2026-08-07 — review #4 — [note](../notes/frog-jump-dp-3.md)
  — review #3 clean, 1 hint on "why min" framing, no Fibonacci-shape repeat
- Longest Consecutive Sequence `[derive]` — due: 2026-08-08 — review #4 — [note](../notes/longest-consecutive-sequence.md) — review #3: pruning mechanic clean, but "why O(n)" needed 1 escalation (inner-while-visits-once accounting) — 2nd time this exact justification needed help
- Sort Array of 0s, 1s, 2s `[derive]` — due: 2026-08-08 — review #4 — [note](../notes/sort-012.md) — review #3 needed 1 light nudge (not fully clean, consecutive-clean count reset)
- Redundant Connection (Union-Find) `[derive]` `[leech]` — due: 2026-08-16 — review #3 — daily recall (0/2 clean) — [note](../notes/union-find-redundant-connection.md) — review #2 (2026-08-15) **not clean, 4 escalations, handed over**: gave what `rank` is *for* and restated `find`'s cost as tree height, but never reached which decision an inflated rank corrupts. **Tagged `[leech]` 2026-08-15** — 3rd correction on this one point. Daily recall on exactly two questions: "which single operation reads `rank`?" (answer: `union`, choosing the child) and "is an inflated rank a correctness bug or a cost bug?" (cost only — `find` still returns the right root; the O(α(n)) bound degrades toward O(log n)).
- Floyd-Warshall's Algorithm `[derive]` — due: 2026-08-18 — review #2 —
  review #1 (2026-08-15) **not clean, 6th failure**: the role of `k` came out
  fine, what breaks with `k` innermost did not; a guided 4-node trace was
  declined mid-way and the answer was handed over. **Change the question.**
  Three phrasings of "why k outer" have now failed (abstract chain 08-01,
  concrete pair-values, guided trace). Ask instead: **"after the outer loop
  finishes value `k`, what does `dist[i][j]` mean?"** The missing piece is the
  invariant (shortest path using only intermediates from `{0..k}`); the loop
  order is a consequence of it, and every attempt so far has demanded the
  consequence without the premise. Counterexample on file if needed:
  `0→3, 3→2, 2→1` all weight 1, where `k`-innermost leaves `dist[0][1] = INF`.
- Min Cost to Connect All Points (Kruskal's) `[derive]` — due: 2026-08-02 —
  review #1 — [note](../notes/mst-min-cost-connect-points.md) — check
  `parent[0]` init (real bug this session) and complexity (O(n²log n))
  cold before code
- Min Cost to Connect All Points (Prim's) `[derive]` — due: 2026-08-18 —
  review #2 — review #1 (2026-08-15) **clean**: the relax rule (raw edge
  weight, not cumulative) came cold — the exact point that broke on 08-01 —
  and the why followed in one sentence ("the objective is the tree's total
  edge weight, so distance from the start never enters it"). Heap vs array
  variant not re-tested; do that next.
- Kth Largest Element in an Array `[derive]` — due: 2026-08-16 — review #2 —
  review #1 (2026-08-15): the O(n) fact **had** stuck, but the follow-up
  exposed that **heapify itself was never learned** ("I don't understand the
  heapify method") — the constant was memorized with no mechanism under it.
  Sift-down and build-heap were constructed from scratch this session and are
  logged as new Heaps material, not as a review. Next: re-ask the *method*
  (precondition, larger-child swap, bottom-up order) before the complexity;
  a correct O(n) with no sift-down behind it is not a pass.
- Top K Frequent Elements (LC 347) `[derive]` — due: 2026-08-02 — review #1 —
  [note](../notes/top-k-frequent-elements.md) — approach only, no code
  written this pass — start with comparator direction cold ("what sits on
  top, and why"), the exact point that broke this session
- Find Median from Data Stream (LC 295) `[derive]` — due: 2026-08-03 —
  review #1 — [note](../notes/find-median-data-stream.md) — start with
  "which guard catches min running away, and why does handing min's top
  back preserve order" before any code; both `addNum` bugs were code-only,
  approach was fine
  only, no code written this pass — ask auxiliary space cold (O(k), not
  O(N)); relink-vs-allocate was the exact miss
- Task Scheduler (LC 621) `[derive]` — due: 2026-09-13 — review #3 — daily recall (**2/2 clean, GRADUATED OFF `[leech]` 2026-08-30, resumes ladder at review #3**) —
  [note](../notes/task-scheduler.md) — 2026-08-30 21:12: code recalled cold and correct
  (`(mf-1)*n + mf + mfCnt - 1`, `Math.max` guard present), both open "why"
  points closed with no hint — the skeleton/`mfCnt-1` accounting and the
  undershoot condition were both stated unaided. **Process note, not scored**:
  opened with "i think i have solved this before" and an attempt decline —
  same phrase that preceded the Frog Jump 7-week false-solved entry; pushed
  back citing the `[leech]` tag itself as the reason it can't be assumed
  retained. Prior: review #2 (2026-08-15) formula clean cold; code shipped
  without the clamp then, found and fixed cold on `n=0` counterexample.
- N Meetings in One Room `[derive]` — due: 2026-08-06 — review #1 — start
  with "why sort by end time, not start or duration" cold, no example —
  needed a constructed counterexample both times this session, see
  mistake_journal 2026-08-05
- Print Subarray with Maximum Sum `[derive]` — due: 2026-08-03 — review #3 —
  review #2 clean (2026-07-27 19:00) — start=tempStart derivation held
  unprompted this time, only needed a concrete-numbers instantiation, not a
  mechanism hint
- Minimum Number of Platforms `[derive]` — due: 2026-08-07 — review #1 —
  code still not written. "Why caps at 2 regardless of chain length" closed
  2026-08-06 via "each interval touches only its immediate neighbor" —
  start review with this "why" cold before anything else
- Jump Game (LC 55) `[derive]` — due: 2026-08-07 — review #1 — code clean
  cold, but "why greedy (max-reach dominates)" needed 1 targeted question —
  start with that "why" before mechanics
  O(n) two-pointer solutions clean, no hints — check the O(n) version is
  still the first thing recalled, not the heap
- Job Sequencing Problem (GFG) `[derive]` — due: 2026-08-07 — review #1 —
  [note](../notes/job-sequencing.md) — two real approach mistakes (sort key,
  slot direction), both self-corrected via counterexample. Start with "what
  should the sort key be, and why" cold. Pressure-test (complexity, DSU
  optimization) still open from 2026-08-06 — close that first, then review.
  Pressure-test closed 2026-08-07; DSU close-the-loop closed 2026-08-08.
- Job Sequencing — bounded-heap variant (GFG) `[derive]` — due: 2026-08-09 —
  review #1 — **read, not derived** (code pasted from GFG) — re-solve cold
  from scratch, no credit carried over. Then the two derived pieces: why the
  sort key flips to deadline-ascending here, and why evicting the heap
  minimum is never regretted (needed 4 escalations on 2026-08-08).
- Fractional Knapsack (GFG) `[derive]` — due: 2026-08-09 — review #1 —
  [note](../notes/fractional-knapsack.md) — code never written; approach and
  all 4 edge cases clean. Start with the "why highest ratio first" exchange
  argument cold — it took 5 sessions and a fully guided numeric swap to
  produce once, so this is the item under test, not the mechanics. **Code
  written 2026-08-09, correct and cold** — both predicted bug surfaces
  (comparator direction, integer division) clean, and space answered O(n) this
  time, so neither needs re-asking; the exchange argument is the only live item.
- Candy (LC 135) `[derive]` — due: 2026-08-10 — review #1 —
  [note](../notes/candy.md) — code never written. Start with the **validity**
  half cold ("why does taking the max of the two passes keep every constraint
  satisfied") — that is the item under test; mechanics, merge rule and the
  minimality half were all cold. If it stalls, instantiate on `[1,3,2,1]`
  immediately rather than re-running the abstract argument. Then the code.
- Lemonade Change (LC 860) `[derive]` — due: 2026-08-18 — review #2 — review #1
  (2026-08-15) **clean cold, both items, no ladder**. The exchange argument came
  out plainly when asked as a one-sentence why rather than as the 4-sentence
  script: `$5` settles both `$10` and `$20`, `$10` settles only `$20`, so spend
  the less flexible bill first. Order-carries-information answered correctly
  (customers are a queue; sorting destroys the problem). **This is the
  vindication of the 08-14 amendment** — the plain one-sentence ask worked
  where the script had been declined three times.
- Valid Parenthesis String (LC 678) `[derive]` — due: 2026-08-18 — review #2 —
  review #1 (2026-08-15) **not clean, 4 escalations**. Both live items failed
  cold: the state's meaning drew the same mechanics-restatement as 08-12, and
  the `min == 0` equivalence did not come. Both closed only after instantiating
  on `(*` and enumerating `{0,1,2}` — the chain then landed (`min` is always a
  *member* of the achievable set, so `min == 0` means 0 is achievable, which is
  validity). **Open with the enumeration next time, never the abstract
  phrasing** — it has now failed on both attempts. Parking it on 08-13 was the
  right call; the item genuinely had not landed.
  escalation on 08-13, so this is a retention check, not a repair. Ask the
  last-interval-only justification (must name *ends are increasing*, not the
  sort rule) and whether the tie-break comparator does any work. Code and
  complexity were clean.
- Shortest Job First (GFG) `[derive]` — due: 2026-08-16 — review #1 — code was
  cold and correct, so the code is not the test. Two live items: the **one-
  sentence why** (why does a shorter job before a longer one never raise the
  total wait — declined in session, ask it plainly, not as the 4-sentence
  script), and sort space cold (said O(n), true O(log n) for `int[]`). If the
  statement itself needs re-reading before the algorithm comes back, log that
  separately — it was the real cost on 08-14.
- Assign Cookies (LC 455) `[derive]` — due: 2026-08-12 — review #1 — code and
  edge case clean cold, so those aren't the test. Two live items: **state the
  exchange argument in the 4-sentence interview form** (rule → rival → move →
  close, per [[GreedyExchangeArgument]]) with no numbers handed over, and the
  space complexity cold (said O(1), true O(log n) — primitives sort).
- Non-overlapping Intervals (LC 435) `[derive]` — due: 2026-08-16 — review #1 —
  https://leetcode.com/problems/non-overlapping-intervals/ — final code correct
  and the one-sentence why came cold ("the earlier end leaves more room for the
  rest"), so neither is the test. Two live items: the **first attempt kept the
  earlier-*starting* interval** (sorted by start, always deleted the later one;
  failed `[[1,100],[2,3],[3,4]]`) — re-pose as "when two overlap and one must
  go, which do you keep?" before any code; and **sort space**, given as
  O(log n), true O(n) — `int[][]` is an object array. Ask the sharpened form:
  "you passed a comparator — what does that alone tell you about the space?"
- Course Schedule (LC 207) `[derive]` — due: 2026-09-07 — review #2 — [note](../notes/course-schedule.md) — review #1 (2026-09-04) outcome: clean — Kahn's BFS indegree direction (v -> u => indegree[u]++) and queue.size() level snapshot redundancy both answered cold and clean.
- Course Schedule II (LC 210) — due: 2026-09-06 — review #1 — solved
  independently, cold, no hints.
- Alien Dictionary (LC 269) `[derive]` — due: 2026-09-06 — review #1 —
  [note](../notes/alien-dictionary.md) — approach recall failed despite
  "solved before" claim; 3 code bugs (cast-precedence, prefix-check order,
  distinct-letter count) — review #1 opens on the approach, not the code.
- Number of Enclaves (LC 1020) `[derive]` — due: 2026-09-06 — review #1 —
  [note](../notes/number-of-enclaves.md) — visited-at-pop bug, 4th
  recurrence of the visited-timing rule.

## Dropped 2026-08-27 — calendar-only backlog (recoverable, not deleted)

Cut with the coverage scope (see `../../Progress/coverage_cut_list.md`). These
items' only claim to a review slot was an elapsed interval — none of them ever
failed a review or carried a `[derive]`/`[leech]` tag. The backlog had been
frozen for 7 sessions with no weekend batch since 2026-08-15, so this records a
decision that the calendar had already made.

**To re-add**: move a line back under Upcoming Reviews and set a new due date.
Do that for any problem that later fails cold in a session — a fresh failure is
real signal, an elapsed interval is not.

- Number of Substrings Containing All Three Characters (LC 1358) — due: 2026-08-24 — review #1 — solved independently, full code cold, no bugs; the *why* needed 3 escalations, so review #1 opens with the counting justification, not the code
- Valid Parentheses — due: 2026-07-24 — review #2 — clean, no hints
- Find the Largest Element in an Array — due: 2026-07-24 — review #3
- Check if Array is Sorted — due: 2026-07-24 — review #3
- Union of Two Sorted Arrays — due: 2026-07-24 — review #3
- Missing Number — due: 2026-07-24 — review #3
- Single Number — due: 2026-07-24 — review #3
- Leaders in an Array — due: 2026-07-24 — review #3
- Majority Element (Boyer-Moore) — due: 2026-07-24 — review #3
- Maximum Sum Subarray of Size K — due: 2026-07-25 — review #1
- Longest Substring Without Repeating Characters — due: 2026-07-25 — review #1
- Max Consecutive Ones III — due: 2026-07-25 — review #1
- Fruit Into Baskets — due: 2026-07-25 — review #1
- Minimum Window Substring — due: 2026-07-25 — review #1
- BFS Traversal of Graph — due: 2026-07-26 — review #1 — [note](../notes/bfs-graph.md)
- DFS Traversal of Graph — due: 2026-07-26 — review #1 — [note](../notes/dfs-graph.md)
- Number of Provinces — due: 2026-07-26 — review #1
- Number of Islands — due: 2026-07-26 — review #1
- Rotten Oranges — due: 2026-07-26 — review #1 — [note](../notes/rotten-oranges.md) — minute-counter rule took 3 iterations, watch closely next review
- Flood Fill — due: 2026-07-26 — review #1 — 3rd recurrence of visited-at-pop
- Cycle Detection (Undirected, BFS) — due: 2026-07-26 — review #1 — clean,
- Topological Sort (DFS) — due: 2026-07-26 — review #1 — DFS approach
- Pascal's Triangle — due: 2026-07-27 — review #2 — review #1 needed 1
- Subarray Sum Equals K — due: 2026-07-27 — review #3
- Two Sum — due: 2026-08-09 — review #4 — review #3 clean
- Rearrange Array Elements by Sign — due: 2026-08-09 — review #4 — review #3
- Second Largest Element in an Array — due: 2026-08-04 — review #4 — [note](../notes/second-largest-element.md) — review #3 clean; **if clean again, graduates** (2 consecutive clean at #3+)
- Max Consecutive Ones — due: 2026-08-08 — review #4 — review #3 clean, boundary/post-loop fix (max updated every iteration, not just on reset) held, no repeat of the standing 3x-flagged bug
- Set Matrix Zeroes — due: 2026-08-08 — review #4 — review #3 clean, flags-then-mark-then-zero order held, no hints
- Stock Buy and Sell — due: 2026-08-08 — review #4 — review #3 clean, no hints
- Remove Duplicates from Sorted Array — due: 2026-08-08 — review #4 — [note](../notes/remove-duplicates-sorted-array.md) — review #3: mechanics clean via guided trace, 1 light nudge on return-value (slow+1) reasoning
- Move Zeroes to End — due: 2026-08-08 — review #4 — [note](../notes/move-zeroes-to-end.md) — review #3 clean; **if clean again, graduates** (2 consecutive clean at #3+)
- Merge k Sorted Lists (LC 23) — due: 2026-08-03 — review #1 — approach
- Jump Game II (LC 45) — due: 2026-08-07 — review #1 — both heap-based and
- Merge Intervals (LC 56) — due: 2026-08-16 — review #1 — solved cold with no
