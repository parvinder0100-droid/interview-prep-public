---
type: dashboard
updated: 2026-09-05
---

# Master Dashboard

Regenerated at the start/end of every session. Single place to answer: "what should I
work on right now, across everything?" **Counts and pointers only — no narrative.**
Dated signals, mistake detail, and session notes live in each track's own
`Progress/progress.md` / `mistakes/mistake_journal.md` — this file never duplicates
them, it points at them.

## Cycle

**DECISIONS 2026-08-30 19:59 (audit, day 52) — three parked items closed.**
Full text in `30day-sprint.md`. (1) **Coverage queue re-ordered**: bucket 2
(Recursion/Backtracking) is formally the head, DP follows; naming the 12 DP
problems is a ~15-min chore outside a session block, due by ~2026-09-02 or DP
drops behind bucket 3. (2) **The weekend reviews-only batch is retired** — 11
zero-review sessions and 6 zero weekends say it never executed. Replaced by 2-3
review questions inside *every* coverage block, before new work, non-optional;
reversal trigger is 3 consecutive sessions that skip them. **The backlog was
NOT archived** — considered and rejected, because the 08-27 cut already removed
the calendar-only items and all ~47 overdue entries now carry
`[derive]`/`[leech]`. (3) **LC 131 comes off the coverage list** after a 3rd
decline; **Word Break (LC 139)** substituted — same variable-length-piece move,
boolean answer.

**Audit correction, recorded so the number isn't reused**: the review backlog is
**56 dated items, ~47 strictly overdue**, not the 74/87 previously reported. The
higher figures swept in the already-Dropped 2026-08-27 section. Dashboard and
`review_schedule.md` disagreed; the file is right.

**Pace, first good news of the cycle**: 9 of the 94 done in the 3 days since the
cut, all judge-confirmed, against 7.4/week required — remaining 85 over ~13.1
weeks now needs **6.5/week**. Ahead of the line.

**DECISION 2026-08-27 19:00 — scope cut, not a date move.** The audit run this
evening fired the plan's own guardrail (rate under 14/week for two consecutive
weeks; actual 5.3 since 08-11). Per `cycle.md`, a 3rd `target_end` move would
mean the goal is wrong — so the goal was cut: **~197 remaining problems -> ~94**,
requirement drops 14.5/week -> 7.4/week. Review backlog cut the same way:
**77 -> 48** (3 `[leech]` + 42 `[derive]` kept, 35 calendar-only items archived
in `review_schedule.md`, recoverable). Both cuts are reversible and the add-back
trigger is written into `30day-sprint.md` — but it explicitly ranks the four
zero tracks above every re-added DSA bucket. Full list: `coverage_cut_list.md`.

**Sequencing decision, same session (19:02, user)**: **finish the 94 first,
then the cut buckets.** This supersedes the add-back rule's zero-track guard —
the trigger will not fire mid-list. Consequence, recorded once: Behavioral and
SystemDesign open ~mid-October at 14/week. The switch trigger (screen or onsite
scheduled -> zero tracks take block 1) remains the safety net and is unchanged.

**DECISION 2026-08-31 17:51 (user) — PLAN B: the 94 finishes by 2026-09-17.**
Full text in `30day-sprint.md`. User asked for the whole cut list in one week;
84 remaining / 7 days = 12 a day, ~5-6 h/day, against an observed 2-3 per
60-70 min session — costed and declined in favour of **2 sessions/day weekdays,
3 weekend sessions/day, ~40/week**, finishing 2026-09-17 at **18 h 40 m/week**
(~42 h total). Requirement rises **6.5/week -> 40/week**. The first draft of
this plan under-weighted weekends off the "6 zero weekends" line — those were
zero *reviews*, not zero coverage; Sat 08-29 and Sun 08-30 both ran 2 sessions
and Sunday held the cycle's best block. Weekends carry the surge. **The blocker is bigger than DP**: `grep -c '^- \[ \]'` returns 0
for all nine remaining buckets — **79 of the 84 are unnamed**, so 2026-09-01
opens with a 2-hour Codolio itemization block that is transcription, not
coverage. Bucket 2's last 5 named the same day (N-Queens, M-Coloring, LC 60,
LC 37, LC 282). Re-cut trigger: under 24 problems by Sunday 2026-09-07 — and
`target_end` does **not** move a 4th time. Consequence: Behavioral and
SystemDesign open ~a month earlier than the mid-October previously recorded.

- Mode: `sprint` (see [Progress/cycle.md](cycle.md) for dates/definitions)
- Day 58 of cycle (2026-09-05) · 2026-09-05 12:59-14:00, ~61 min (user-set
  90, ended early). Leech drill declined again before starting (24+ days,
  now longest-running). **3 problems, 3/3 submitted, 3/3 Accepted** — Course
  Schedule II (LC 210, independently, cold), Alien Dictionary (LC 269,
  with-hints:many — approach recall failed despite "solved before" claim,
  plus 3 live code bugs: cast-precedence, prefix-check order, distinct-letter
  count), Number of Enclaves (LC 1020, with-hints:1 — visited-at-pop bug,
  TLE, **4th recurrence** of the visited-timing rule already written in
  `DSA/topics/Graph.md`). Graph coverage-queue now **4/12**. Week 1 running
  count: **10 of 32** (checkpoint tomorrow, 2026-09-07, needs 24).
  Prior entry:
- Day 57 of cycle (2026-09-04) · session 1 · 2026-09-04 15:23-15:42, ~19 min
  (user-set 10, ran over to close ELI5 derivation). **Review-only session, 0 new
  problems, 2 reviews cleared.**
  (1) Course Schedule (LC 207) `[derive]` review #1 cleared **clean**: Kahn's BFS
  indegree direction (v -> u => indegree[u]++) and queue.size() level-snapshot
  redundancy both answered cold and clean.
  (2) Power of Two (LC 231) review #1 (carried over from 09-03 incomplete) cleared
  **hint/guided**: Integer.MIN_VALUE underflow on n-1 and false-positive
  (n & (n-1)) == 0 trap closed via ELI5 odometer analog; loop closed with user
  justifying n > 0 guard because powers of two cannot be negative.
  Both advance to review #2, due 2026-09-07. Next coverage: Course Schedule II (LC 210).
  Prior entry:
- Day 56 of cycle (2026-09-03) — no coverage session, **0 problems**. Ran a
  full audit (see this file's history) + git push (12 local commits rebased
  onto 1 remote, clean), then researched Biweekly Contest 190 (2026-08-29,
  the past week's) and rated contest-readiness against the tracker.
  **New finding, not previously named**: zero timed/cold-contest data exists
  anywhere in this tracker — every solve stat is untimed and hint-permitted
  (`with-hints:N`), so contest performance is unverified, not just unknown.
  Two topic gaps surfaced with no prior exposure in progress.md: prefix/suffix
  array computation paired with number-theory (GCD-type) reasoning, and
  greedy string/array construction with boundary edge-cases. Recommended and
  not yet scheduled: (1) a weekly timed virtual-contest rep, (2) enforcing the
  two already-written-and-ignored prescriptions (predicate-first-line-of-code;
  state-the-defect-before-pasting-fix) starting immediately, (3) a small
  targeted set (4-5 each) on the two named gaps rather than folding them into
  the existing coverage queue.
- Day 56 of cycle (2026-09-03) · session 3 · 2026-09-03 21:01-21:18, ~17 min
  (user-set 30, wrapped early). **1 problem, Course Schedule (LC 207,
  with-hints:1)** — first Graph coverage-queue item, Kahn's BFS. Live bug
  (indegree wired to wrong node) found by trace, defect only stated after a
  silent fix. Leech drill (Bellman-Ford/Redundant Connection) declined again
  before starting — 22+ days, still untouched. **N-Queens (LC 51) dropped at
  a 3rd decline**, same threshold as LC 131; Permutations II (LC 47) declined
  a 2nd time, genuinely this time. **Tracker error caught**: Kth Permutation
  Sequence (LC 60) was mislabeled Medium, is actually Hard — corrected.
  Reviews: 0.
  Prior entry:
- Day 55 of cycle (2026-09-02) · 2026-09-02 17:04-17:46, ~42 min (user-set 30,
  ran over). **3 problems, 3/3 submitted, 3/3 Accepted** — Single Number III
  (LC 260, with-hints:5), Power of Two (LC 231, with-hints:3), Number of 1 Bits
  (LC 191, with-hints:1). **BitManip closes at 5/5** — cut-list slot complete.
  **Reviews: 0 — 6th consecutive skip**, opening review block (3 due + 2-item
  leech drill) declined outright ("new prob") before any question was asked.
  Bellman-Ford and Redundant Connection now 21 days without their mandated
  daily recall; M-Coloring's carried-over review (due 09-01) dropped a 2nd day
  running. Content-wise: no derivation-to-code regression this session — both
  live mistakes were pre-code reasoning gaps (LC 260's "either" vs "exactly
  one" on an XOR bit; LC 231's guard missing the Integer.MIN_VALUE single-bit
  negative), both corrected same-session, neither recurring.
  Prior entry:
- Day 54 of cycle (2026-09-01) · 2026-09-01 17:15-18:47, 92 min (user-set 120,
  ended 28 min early). **3 problems, 3/3 submitted, 3/3 Accepted** — Sudoku
  Solver (LC 37, with-hints:7), Single Number (LC 136, cold, a re-verify of the
  2026-07-12 solve), Single Number II (LC 137, with-hints:3). Bucket 2 now
  **12/15**; Bit Manipulation opened at 2 of 5. LC 47 declined at approach, LC
  260 posed and not started.
  **Reviews: 0 — 3rd consecutive skip, so the in-block review mechanism's own
  reversal trigger has fired.** It goes to the audit as retired-or-enforced
  rather than left nominally in force. **5th consecutive leech-drill decline**;
  Bellman-Ford and Redundant Connection are now 20 days without their mandated
  daily recall. M-Coloring's complexity, carried into today's plan as the first
  review item, was dropped with the block.
  **The headline is where the failures live.** Eight defects across LC 37 and
  LC 137, **all eight at the write step, none in the derivation.** On LC 37 both
  conceptual halves were cold — constraint tracking volunteered with no
  greedy-first-match, and the base case justified by the invariant ("if they
  conflict we will backtrack"). On LC 137 the entire derivation was correct
  before any code: XOR is a per-bit count mod 2, so triples survive; HashMap
  fails the space bar; count mod 3; 32 slots and bit 31 must be counted. Then
  the code said `%2`. **Derivation-to-code regression is 2 for 2 across two
  sessions at an interval of minutes**, and the 08-31 prescription (write the
  derived predicate as the first line of code) has not been run either time.
  **The new content item is arithmetic, not algorithms**: `(r/3)*3 + c/3` took
  12 minutes and the full escalation ladder — sample cells, two 9x9 pictures, a
  cinema-seat analog — and was still handed over; the same gap wrote `i*3+j` as
  the cell stride on a 9-wide grid. Row-major flattening recurs on every grid
  problem and is cheap to close. Now in `../DSA/patterns/Backtracking.md`.
  **Process, unchanged**: 3rd occurrence of "do I need to code it?"; 3rd paste
  with no one-line defect statement (gate 3 — the gate that exists to catch
  exactly the `%2` slip); 5th hint-shape match, two defects named in one message
  and one fixed.
  **Correction to PLAN B, carried so the wrong number isn't reused**: "79 of 84
  unnamed" is stale — Day 0 itemization partly ran 08-31. Disk shows **~33 named
  and workable** (Graph 6, Stack/Queue 6, Strings 6, BitManip 5, Heap 4, Sorting
  2, Trie 1, bucket 2's 3) against ~49 still `TBD` (Arrays 13, DP 12, Graph 6,
  SlidingWindow 6, Stack 4, Trees 3, Greedy 3, Heap 2). Itemization is no longer
  an immediate blocker; it is due before the named 33 run out, ~week 2.
  Prior entry:
- Day 53 of cycle (2026-08-31) · session 2 · 2026-08-31 21:18-21:48, 30 min
  (user-set 30). **1 problem, submitted and Accepted 1114/1114** — M-Coloring
  (GFG), with-hints:6, on the 3rd submission. Bucket 2 now **11 of 15**.
  **Reviews: 0. 2nd consecutive skip of the opening-review rule** ("lets solve
  new probs") and the **4th consecutive leech-drill decline** — Bellman-Ford and
  Redundant Connection now 19 days without their mandated daily recall.
  **Reversal trigger is 3 consecutive skips; this is 2.**
  **The headline is a genuine close on the top content item.**
  Greedy-first-match — named as item 1 five hours earlier, on two problems —
  appeared a 3rd time in the opening approach ("on conflict return false") and
  **closed in one question, cold**: "no, we should try other colors for previous
  nodes". The pre-code check written into the 08-31 prescription ("which line
  brings control back here?") was then answered unprompted. First time this
  family self-corrected without escalation. The previous-node-only legality rule
  closed on one traced instance in the same way.
  **And then the code was written with the rule that had just been discarded**
  (`i != prvNodeColor`, two minutes after "reads `color[neighbor]` for every
  neighbor"). **Derivation-to-code regression** — same family as the 08-28/29/30
  transfer gaps, but the gap is now *minutes*, not 16 hours. This is the item.
  **The three judge-visible defects were all mechanical, none conceptual**: a
  `continue` aimed at the inner loop (the legality scan ran and discarded its
  verdict); the vestigial `prvNodeColor` guard left in after the scan replaced
  it, firing on a self-edge (WA 1/1114); and `dfs(0)` as the only entry point,
  so disconnected components went uncoloured (WA 6/1114).
  **New evidence on parking a trace**: the disconnected-component case was posed
  as a guided trace, declined mid-way ("i will have to come back at this question
  later"), and arrived 4 minutes later as the judge's failing test. The trace
  would have been free; the WA was not.
  Complexity **not reached** ("no idea") — session ended there, `m^V` is where the
  two-step scaffold was heading. Carried as the first item of the 09-01 review.
  Closing exchange: user asked whether the problem was too hard for them. Answered
  no, on the evidence — both conceptual halves were self-derived, all three
  failures were mechanical.
  Prior entry:
- Day 53 of cycle (2026-08-31) · 2026-08-31 16:23-17:30, 67 min (user-set 70).
  **2 problems Accepted, 1 WA-and-abandoned; 3/3 submitted to the judge.**
  LC 139 Word Break (with-hints:5) and LC 46 Permutations (with-hints:3) both
  Accepted; N-Queens attempted a 2nd time, WA on n=4, declined. Bucket 2 now
  **10 of 15**.
  **The headline is one finding, seen twice in one session: greedy-first-match.**
  Both LC 139 and LC 51 opened with "take the first legal choice and advance" —
  no branch, no undo. This *replaces* the 08-30 variable-length-piece claim as
  the top content item; that claim predicted LC 139 would bite and it did, but
  one level up and on a grid problem too, so it is not about string indices or
  about piece length. Closed on LC 139 by a constructed counterexample
  (`"catsdog"`, since `"catsandog"` is greedily right); **not** closed on LC 51,
  which is where the session ended.
  **Process, and this is the item to act on: hint-shape matching, 4th
  occurrence, twice today, once *after* being named aloud.** N-Queens: shown a
  5-character row string, added an `else`, left the `res` shape (the actual
  question) untouched. LC 46: told there were two precedence bugs, fixed the one
  the compiler pointed at. The 08-30 prescription ("re-run the counterexample
  before declaring a fix") has now failed to fire three sessions running —
  replaced with **restate the defect in one sentence before pasting the code**.
  Also 5th silent fix; both LC 139 defects were only spoken when asked directly,
  one needing 4 escalations and an analogy.
  **Positive, and it is a real one**: the place/recurse/undo skeleton on LC 46
  was written **cold, both undos present, 20 minutes after that exact mechanism
  was declined on N-Queens**. Memoization on LC 139 also went in unprompted —
  the exponential hole flagged before coding never appeared. Both LC 139
  defects were found by tracing, not handed over, and "cost bug, still returns
  right answer" was volunteered — the same question shape as the Redundant
  Connection `[leech]` item declined at the top of this session.
  **Reviews: 0. First skip of the new opening-review rule** (adopted 08-30, ran
  once, declined here with "will solve new problms") and the **3rd consecutive
  leech-drill decline**. Reversal trigger is 3 consecutive skips — this is 1.
  Prior entry:
- Day 52 of cycle (2026-08-30) · session 2 · 2026-08-30 20:47-21:13, ~26 min
  (user-set 30). **First non-zero review session of the cycle** — new
  opening-review mechanism (adopted this morning) ran for the first time: LC
  79 closed clean, LC 216 closed via guided derivation on the 3rd asking
  (first time not handed over), Task Scheduler `[leech]` recall went 2/2
  clean and **graduated off `[leech]`**, resumes ladder at review #3 (due
  2026-09-13). Ran ~7 min over the 5-8 min review budget so Word Break (LC
  139) did not start — still next up. Process note: Task Scheduler opened
  with "i think i have solved this before" (2nd occurrence of the Frog Jump
  pattern), pushed back on, then answered clean.
  Prior entry:
- Day 52 of cycle (2026-08-30) · last session 2026-08-30 14:51-15:51, 60 min
  (user-set 60, **ran the full booked block — first time in three sessions**).
  **Sunday, weekend policy is reviews-only, coverage chosen again — 0 reviews,
  11th consecutive zero-review session, 6th consecutive weekend at zero.** The
  leech drill was again proposed as the opening block and again declined ("we
  will solve new probs") — 2nd consecutive decline. Audit skipped by user
  decision, so the DP-12 blocker is still unresolved after 3 sessions.
  Bucket 2 continued: **3 problems, all Accepted on the judge in-session** —
  LC 17 Letter Combinations (with-hints:3), LC 79 Word Search (with-hints:4),
  LC 216 Combination Sum III (with-hints:2).
  **The headline is verification, not content: this is the first session of the
  cycle where every problem attempted got a verdict.** Against Frog Jump (logged
  "solved" 07-10, contained a crash bug) and Rat in a Maze (entered 08-29 never
  judge-confirmed), 3/3 Accepted is the thing the tracker has been missing. New
  series in `../DSA/Progress/statistics.md`.
  **The 08-29 predictive boundary is falsified as stated and now sharper.** The
  claim was board/grid state works, string-index state does not. LC 17 is a
  string-index problem and it ran clean — approach complete *before* code, index
  carried down, base case correct, no stall. LC 131 was declined a 3rd time with
  no attempt, so it added no evidence. Revised claim: the blocker is not string
  indices, it is **choosing a variable-length piece** (`j` ranging over `i..n-1`)
  versus advancing by a **fixed stride of 1** (LC 17, LC 79). Narrower, testable,
  and it predicts which remaining bucket-2 problems will bite.
  **Two rules met again, opposite outcomes.** (a) Base-case ordering by
  precondition, 4th encounter — **stated cold and correctly** on LC 79 ("all
  chars matched, doesn't depend on i j"), the first clean instance after three
  corrected ones. (b) **Hint-shape matching fired exactly as predicted 08-29**,
  2nd occurrence: told `|` vs `||`, explained the cost correctly, then changed
  the operator on the `return` line while the four calls stayed eagerly assigned
  above it — nothing short-circuited. The 08-29 prescription (re-run the
  counterexample before declaring a fix) was written the day before and did not
  transfer.
  Also: the copy-cost family reached its 3rd encounter and was **derived rather
  than nudged out** for the first time (`O(n²)` from `res+c`, closed by one
  4-frame trace); start-index dedup transferred **cold** from LC 39/40 two days
  earlier; the `board[i][j]=cur` restore was deleted and silently restored, the
  3rd silent fix (08-25, 08-29, 08-30), though the symptom question — declined on
  Rat in a Maze 08-29 — was answered this time via counterexample.
  **New process signal, first occurrence: explicit resistance to writing code**
  ("do i need to write it?"), resolved by citing the coverage guardrail. Both
  "i didnt get it" moments closed on a concrete instance, consistent with the
  standing prescription; 2 declines ("can we move?", "lets not go in this ques
  yet") left the `||` mechanism, LC 79's complexity and LC 131 unspoken.
  Prior entry:
- Day 51 of cycle (2026-08-29) · last session 2026-08-29 16:03-16:51, ~48 min
  (user-set 60, **ended early on a stated focus break — "someone was at the
  door and i felt the urge to check phone"**). Second session of the same day;
  both ended early on attention grounds, 95 of 180 booked minutes used.
  **Saturday, weekend policy is reviews-only, coverage chosen again — 0 reviews,
  10th consecutive zero-review session, 5th consecutive weekend at zero.** The
  recall drill was proposed as the opening block, per the finding written four
  hours earlier, and declined ("we will solve new probs").
  Bucket 2 continued: **Rat in a Maze (GFG) with-hints:4** (code correct on
  review, never judge-confirmed), **N-Queens approach-only**, **LC 131 reopened
  and abandoned a 2nd time**.
  **Two findings, opposite signs.** (1) The base-case ordering rule was met for
  the 3rd time in two days and, for the first time, **spoken aloud** — but only
  after a fix sequence that ran silent patch -> patch reverted without the swap,
  which put the bug straight back -> correct swap. Worse, the rule as summarised
  ("reject before accept — same as LC 40") is **inverted with respect to LC 40**
  and was wrongly affirmed; both `../DSA/patterns/Backtracking.md` and the
  flashcard are now rewritten around preconditions rather than order. (2) The
  approach came **before** code on N-Queens, unprompted — first time in 3
  sessions — followed by four cold correct derivations in a row (row-per-level,
  row-free-by-construction, `r+c`, `r-c`). Rat in a Maze, 20 minutes earlier,
  was still code-first.
  **New boundary, and it is nameable**: same session, cold derivation on a
  chessboard and a maze grid, total non-start on a string index (LC 131 stalled
  going from `j=0,1,2` on `"aab"` to `j` over `i..n-1`). Both LC 131
  abandonments are "I don't understand", never a wrong answer. Extends the 08-27
  physical/visual finding to a *predictive* split.
  Two mentor errors logged: the inverted rule affirmed, and praise language
  ("Best question of the session") which the user rejected outright — **standing
  rule now: no praise language**.
  Prior entry:
- Day 51 of cycle (2026-08-29) · last session 2026-08-29 13:49-14:36, ~47 min
  (user-set 120, ended early), **Saturday — weekend policy is reviews-only and
  the user chose coverage, 0 reviews cleared. 9th consecutive zero-review
  session and the 4th consecutive weekend at zero** (08-16, 08-22, 08-23,
  08-29). Bucket 2 (Recursion/Backtracking) continued: **2 problems Accepted,
  1 left open mid-derivation** — LC 40 Combination Sum II (with-hints:6),
  LC 90 Subsets II (**independent, cold, first submit**), LC 131 Palindrome
  Partitioning approach-only.
  **The finding of the session is a clean split between two kinds of transfer.**
  Both defects in LC 40 were already written in the tracker the night before —
  the `Set`-on-result pitfall (top entry of `../DSA/patterns/Backtracking.md`,
  written 08-28) and the accept-before-reject base-case ordering (written into
  `../DSA/flashcards/recursion.md` at 22:17 on 08-28, reproduced at 13:58 on
  08-29, a **16-hour** gap). Neither written note transferred. In the same
  session, the skip-on-decline rule that cost six escalations plus a guided
  trace on LC 40 came out **cold and unprompted on LC 90 five minutes later**,
  and the copy-cost complexity nudge closed inside 6 minutes — the 5th transfer
  gap logged and the first one to close within a session. Read as: derivation
  encodes, reading does not, and `recall/daily.md` has never once been run as
  the drill it was created to be. That is now the top item.
  Process, unchanged and worth watching: 2 "just tell me", 2 "i didnt get it",
  and code arrived before the approach on **both** problems despite the approach
  being asked for first each time; LC 40's base-case bug was fixed silently
  without ever naming what broke.
  Prior entry:
- Day 50 of cycle (2026-08-28) · last session 2026-08-28 21:26-22:13, ~47 min
  (user-set 60), **Friday, coverage day, 0 reviews cleared** — 8th consecutive
  session at zero. **3 problems: 1 long-open item closed, 2 new intake.**
  Frog Jump (DP-3) closed after 7 weeks — the three follow-ups asked 07-10 and
  never answered were all answered, O(1)-space code Accepted — plus Subsets
  (LC 78, **independent, cold, correct first submit**) and Combination Sum
  (LC 39, with-hints:2). **The finding of the session is that a recorded solve
  was not a solve.** Closing Frog Jump surfaced two live defects in code the
  tracker had carried as correct since 07-10: `dp[i-2]` indexed from `i=1`
  (throws on every `n>=2` input, so it had never been run on a judge) and a
  roll storing `oneStep` — a dp value *plus a jump cost* — where `dp[i-1]`
  belonged (`[0,10,100,10]` returns 100 instead of 10, invisible for n<=3).
  Both were found by naming the invariant before touching the code, the same
  unlock as 08-25. This is the first hard evidence for the 07-26 whole-sheet
  rusty-not-safe reclassification, and it arrived the same session the user
  twice declined an attempt with "i think i have solved this prblm before" —
  the first of those two being this exact problem. **Second finding: the
  transfer gap is now sub-15-minute.** The O(n) copy cost of
  `res.add(new ArrayList<>(list))` was derived correctly on Subsets after one
  nudge, then omitted again on Combination Sum 12 minutes later, same line of
  code — 4th transfer gap logged. **Third, and generalizable**: a `Set` on a
  backtracking result set is a branching bug — Combination Sum ran three
  branches where two suffice, and the `HashSet` was filtering duplicates the
  search should never have produced. Now the top pitfall in
  `../DSA/patterns/Backtracking.md`. New pattern file `SpaceOptimizedDP.md`.
  Escalations: 3 "just tell me" (4 on 08-27), so most again terminated at full
  explanation rather than co-derivation.
  **BLOCKER RAISED — bucket 1 of the coverage queue is not executable.** "DP
  gaps 12" cannot be worked top-down because the 12 are unnamed: the archived
  export itemizes only Lec 1 (1) and Lec 2 (5) of DP's 56, so 38 solved and all
  12 unsolved are unrecoverable from disk. The first problem proposed from it
  (Ninja's Training) was challenged by the user as probably sitting in the
  *cut* 161-problem re-verification backlog — correct, and the mentor's pick
  was wrong on scope. Itemizing from the Codolio web UI was started and
  abandoned by user decision; the session ran in bucket 2
  (Recursion/Backtracking) instead, which is unambiguously scoped.
  **Take to the weekend audit: name the 12, or re-order the queue.**
  Prior entry:
- Day 49 of cycle (2026-08-27) · last session 2026-08-27 17:20-18:45, 85 min
  (user-set 90), **Thursday, coverage day, 0 reviews cleared** — 7th
  consecutive session at zero, backlog flat at 77. **3 new problems + 1
  follow-up closed — the highest coverage output of the cycle** (prior best 2):
  LC 84 Largest Rectangle in Histogram (Hard, with-hints:2), LC 907 Sum of
  Subarray Minimums (with-hints:4), LC 739 Daily Temperatures (**independent,
  cold, first submit, 0 ms**), plus LC 42's O(1)-space two-pointer, left open by
  design on 08-26. **Two findings, opposite signs.** (1) The justification
  signal keeps improving: LC 84's *why* ("taller bars can be cut down to
  `h[i]`, shorter ones can't") and LC 739's (`>=` because "warmer" is strict)
  both came **cold and unprompted** — 3rd consecutive session with a cold *why*
  after the 7-problem silent streak. Both were physical/visual mechanisms;
  LC 907's abstract counting still needed pair enumeration, which locates the
  remaining weakness precisely. (2) **Template-first retrieval recurred (2nd
  occurrence) and this time produced a wrong answer** — LC 907 inherited LC 84's
  `nsl/nsr` with strict `<=` on both sides, which is harmless under `max` and an
  overcount under `sum` (`[2,2]` → 8 vs 6). Same machinery met three times in one
  session with three different tie rules; the rule is now written into
  [[MonotonicStack]] as the file's top entry, with an all-equal input mandated as
  a standing test case. Also new: a **derivation-to-code assembly gap** (LC 42's
  argument derived cleanly across 5 questions, then code requested rather than
  attempted) and 4 "just tell me" requests, so most escalations terminated at
  full explanation rather than co-derivation — the inverse of 08-26. **Mentor
  error logged**: LC 739's justification was re-drilled twice after being stated
  correctly; standing fix is to stop once the *why* is spoken. Java came off zero
  incidentally (`Stack extends Vector`, unknown).
  Prior entry:
- Day 48 of cycle (2026-08-26) · last session 2026-08-26 18:48-19:18, 30 min
  (user-set 30), **Wednesday, coverage day, 0 reviews cleared** — 6th
  consecutive session at zero, backlog flat at 77. 1 problem, and this one is
  **new intake, not an open item**: LC 42 Trapping Rain Water, Hard,
  with-hints:5, code cold and correct on first submit. **The finding is that
  the silent-fix streak broke.** Complexity (O(n)/O(n)), both edge cases
  (`n=0`, `n=1`) and the justification were all stated — the first fully-spoken
  solve since 08-21, against four straight sessions where they went unsaid.
  What unlocked the *why* was a 4-element analog traced one line at a time
  (`[3,1,0,2]`, "how much water sits on index 1?"), not a re-explanation of the
  5-element instance already on the table — 3rd confirmation that guided
  tracing beats re-asking (07-12, 08-18, today). **New mistake class logged:
  template-first retrieval** — the boundary rule was reached for as this
  topic's stored `nsl/nsr` before anyone asked what physically holds water
  above one index, and 14 of 30 min went to it. Resolved by one discriminating
  instance (`[3,0,1,0,2]` separates nearest from tallest in a single step),
  which is the same numeric-instantiation prescription the tracker has carried
  since 08-08 — now doing work on a *retrieval* error, not just a
  justification one. Left open by design: the O(1)-space two-pointer version,
  which opens the next Stack/Queue session.
  Prior entry:
- Day 47 of cycle (2026-08-25) · last session 2026-08-25 20:40-21:41, ~25 min
  active (user-set 20; a 55-min gap sits inside that span, the working time was
  not an hour), **Tuesday, coverage day, 0 reviews cleared** — 5th consecutive
  session at zero. 1 problem, again an **open item closed, not new intake**: LC
  930 Binary Subarrays With Sum, code finally written after being declined
  08-23, with-hints:1. **Two findings, and the second is the bigger one.** (a)
  The `atMost(goal) - atMost(goal-1)` transfer survived two days of decay and
  came out cold a second time — genuine retention, the first clean instance of
  it in the tracker. (b) The bug was a shrink guard `i<j` that forbids the
  window from ever emptying, which silently breaks every `goal=0` input; it was
  fixed after one targeted question and **fixed silently** — invariant,
  complexity and edge case were each asked for twice and never stated, session
  ended out of time. That is the **abstract-vs-concrete / encoding-not-verified
  class landing on a fourth track** (Greedy, SystemDesign, Stack, now
  SlidingWindow), one day after LC 735 demonstrated the same class costs a
  verbatim bug reproduction. Logged as unspoken, not covered; review #1 opens
  on the why, not the code.
  Prior entry:
- Day 46 of cycle (2026-08-24) · last session 2026-08-24 17:00-17:29, ~28 min
  (user-set 30), **Monday, coverage day, 0 reviews cleared** — 4th consecutive
  session at zero, and the weekend batch (08-22/23) never fired either. 1
  problem, and it was an **open item closed, not new intake**: LC 735 Asteroid
  Collision solved with-hints:4 after failing cold 08-23. **The finding of the
  session is an encoding failure, not a solve**: the cold re-attempt reproduced
  08-23's symmetric-collision bug verbatim, one day after that exact defect was
  written up in its own note. Reading a diagnosis did not encode it; numeric
  instantiation on a number line closed it in one trace. That is now the
  abstract-vs-concrete prescription landing on a **third** track (Greedy,
  SystemDesign, now Stack). Amortized O(n) justification came independently on
  first ask — first time in the tracker; every prior session needed 2-3
  escalations. LC 735 scheduled at a **2-day** interval by explicit user
  decision, off the normal ladder. LC 930 code still unwritten.
  Prior entry:
- Day 45 of cycle (2026-08-23) · last session 2026-08-23 09:42-10:33, ~51 min
  (user-set 60), **Sunday, weekend = reviews-only by policy — user chose
  coverage instead, 0 reviews cleared. Third weekend session running with zero
  reviews (08-16, 08-22 both unrun, 08-23 spent on coverage).** 3 problems
  touched: LC 1358 solved independently full code cold no bugs; LC 930
  approach-only (`atMost` transfer retrieved unprompted, **code declined**);
  LC 735 Asteroid Collision **failed, left unresolved** with 2 open bugs.
  Insert Interval declined a 2nd time — now marked DEFERRED, not queued.
  **Live decay datapoint: LC 435 (solved 08-15, with-hints:1) returned total
  blank recall at 8 days** — its review #1 was due 08-16 and never ran.
  Prior entry:
- Day 40 of cycle (2026-08-18) · last session 2026-08-18 17:34-17:43, ~10 min
  (user-set 10), DSA/Greedy coverage, 1 problem (Minimum Coins {1,2,5,10},
  solved independently) — **08-16 Sunday and 08-17 both missed, so the second
  weekend review batch never ran**; backlog 60 → 72 purely by items coming due.
  Prior entry:
- Day 37 of cycle (2026-08-15) · last session 2026-08-15 15:10-17:20, ~130 min
  (user-set 120, ran over to close LC 435) — **first weekend batch: 12 reviews
  cleared, ending an 18-session drought**, plus 1 new Greedy problem (LC 435).
  Longest logged session in the tracker. Prior entry:
- Day 36 of cycle (2026-08-14) · last session 2026-08-14 21:51-22:20, ~29 min
  (user-set 30), DSA/Greedy (Insert Interval declined as boring, no attempt;
  Shortest Job First cold code, statement needed a guided trace)
  · **target_end moved 2026-08-11 to 2026-11-30**
  (2nd move; 1st was 08-01 to 08-23). Goal changed with it: **finish DSA
  coverage end-to-end**, ~210 problems, before resuming other tracks.
  **Focus now**: the Coverage Queue in
  [30day-sprint.md](30day-sprint.md) — started-but-open topics (Greedy, Heaps,
  Stack/Queue, Sliding Window) first, then DP gaps, then Recursion.
  **Weekdays** 2h: coverage only — the `+1` review block was struck 2026-08-12.
  **Weekends**: reviews only, 2 sessions, cap 12 each. Full code every problem.
- Last full audit: 2026-07-20 (not re-run since — run `interview-prep-audit`
  for a current one rather than trusting this date).

## Reviews Due

- **2026-09-05 14:00** — leech drill declined again (opening ask, before any
  coverage) — now 24+ days, longest-running decline of the cycle. 3 new
  `[derive]` items entered, all due 2026-09-06: Course Schedule II (LC 210,
  clean), Alien Dictionary (LC 269, opens on approach not code), Number of
  Enclaves (LC 1020, opens on the visited-timing rule). Overdue unchanged:
  Sudoku Solver (LC 37), Single Number II (LC 137), Number of 1 Bits
  (LC 191).
- **2026-09-04 15:42** — 19-min review block (user-set 10). **2 reviews cleared**:
  (1) Course Schedule (LC 207, review #1, clean — indegree indexing direction & queue.size() redundancy);
  (2) Power of Two (LC 231, review #1, hint — Integer.MIN_VALUE edge case closed via ELI5 odometer).
  Both advance to review #2, due 2026-09-07. Overdue reviews remaining: Sudoku Solver (LC 37),
  Single Number II (LC 137), Number of 1 Bits (LC 191), and leech drill (Bellman-Ford / Redundant Connection, 23 days).
- **2026-09-03 17:34** — 10-min block, review-questions-only (no coverage
  time). 1 of 4 due items reached full closure: Single Number III (LC 260)
  outcome **hint** on both open items — the split-rule imprecision from the
  original solve recurred verbatim in different words ("uncertain" for
  "either"), 2nd occurrence of the same point. Power of Two (LC 231) review
  **incomplete** — Integer.MIN_VALUE still not named, same gap as the
  09-02 solve, escalation cut short by save mid-question. Number of 1 Bits
  and Daily Temperatures reviews **not reached**. Bellman-Ford/Redundant
  Connection `[leech]` still untouched, now 22+ days.
- **~59 DSA due as of 2026-09-02 17:46** — **none cleared, 6th consecutive
  zero-review session — the mechanism the 08-30 decision said would be
  reversed-or-enforced at 3 skips has now run 3 more.** Opening review block
  declined before any question was posed ("new prob"). 56 -> 59 is new intake
  only: LC 260, LC 231, LC 191, all due 2026-09-03. Bellman-Ford/Redundant
  Connection `[leech]` now **21 days** without recall; M-Coloring's own review
  (due 09-01) unrun for a 2nd session. Take to the audit: the reversal
  question from 09-01 is now overdue by one more session. Prior snapshot:
- **~56 DSA due as of 2026-09-01 18:47** — **none cleared, 3rd consecutive
  zero-review session, and that is the reversal trigger the 08-30 mechanism set
  for itself.** The opening block was proposed with all five questions written
  out (M-Coloring complexity + both `[leech]` items) and declined with "lets
  solve new probs". ~53 -> ~56 is new intake only: LC 37 `[derive]`, LC 136, LC
  137 `[derive]`, all at +1 for 2026-09-02. **5th consecutive decline of the
  two-item `[leech]` drill** (Bellman-Ford, Redundant Connection — 20 days).
  M-Coloring's review came due today and was not run. Take to the audit: the
  in-block mechanism has now failed on the same terms the weekend batch did,
  which makes it the **second** retention mechanism this cycle to be adopted and
  never executed — the question for the audit is not which mechanism to write
  next, it is whether any review happens that is not scheduled as the only
  content of a session. Prior snapshot:
- **~53 DSA due as of 2026-08-31 21:48** — **none cleared, 2nd consecutive
  zero-review session under the new mechanism** and the **4th consecutive
  decline of the two-item `[leech]` drill** (Bellman-Ford, Redundant
  Connection — 19 days without their mandated daily recall). ~52 -> ~53 is new
  intake only: M-Coloring `[derive]`, `+1` for 2026-09-01. **Reversal trigger
  for the in-block review mechanism is 3 consecutive skips; this is 2** — the
  next session either opens with the block before any problem statement is
  given, or the mechanism gets retired at the audit rather than left nominally
  in force. Prior snapshot:
- **~52 DSA due as of 2026-08-31 17:30** — **none cleared, 1st zero-review
  session since the new mechanism was adopted.** The opening review questions
  were proposed and declined ("will solve new problms"), which is also the 3rd
  consecutive decline of the two-item `[leech]` drill (Bellman-Ford, Redundant
  Connection — now **18 days** without their mandated daily recall). ~50 -> ~52
  is new intake only: LC 139 and LC 46, both `+1` for 2026-09-01. Note the
  session answered the *content* of the Redundant Connection leech question
  incidentally — "cost bug, still returns right answer" was volunteered on the
  LC 139 memo key — without the leech item itself being touched. **Reversal
  trigger for the in-block review mechanism is 3 consecutive skips; this is 1.**
  Prior snapshot:
- **~50 DSA due as of 2026-08-30 21:13** (`tools/build_dashboard.py`) — **2
  cleared this session, streak broken: 12th consecutive zero-review session
  did not happen.** New opening-review mechanism's first run: LC 79 (clean),
  LC 216 (hint — closed via guided derivation on the 3rd asking), Task
  Scheduler `[leech]` recall (2/2 clean, **graduated off `[leech]`**, resumes
  ladder at review #3, due 2026-09-13 — the leech mechanism's first-ever
  clearance). Two of three `[leech]` items remain (Bellman-Ford, Redundant
  Connection). Prior snapshot:
- **87 DSA due as of 2026-08-30 15:51** — **none cleared, 11th consecutive
  zero-review session, 6th consecutive weekend the batch did not fire.** 84 ->
  87 is new intake only (LC 17, LC 79 `[derive]`, LC 216 `[derive]`, all at +1
  for 2026-08-31). The three `[leech]` items are now **17 days** without their
  mandated daily recall. The drill was proposed as the opening block for the
  second session running and declined again. One item did close sideways: Rat in
  a Maze's open question (2), the symptom of deleting the visited-restore, was
  answered today on LC 79 via counterexample and is struck through in
  `review_schedule.md`. **The audit is now 8 sessions overdue** and was
  explicitly skipped today. Prior snapshot:
- **84 DSA due as of 2026-08-29 16:51** — **none cleared, 10th consecutive
  zero-review session, 5th consecutive weekend the batch did not fire.** 82 ->
  84 is new intake only (Rat in a Maze `[derive]` at +1 for 2026-08-30; N-Queens
  and LC 131 are open, not scheduled). The three `[leech]` items are now **16
  days** without their mandated daily recall. The recall drill was **proposed as
  the session's opening block and declined** — that is the first time the 08-29
  top-item action reached the table, and it did not run. The audit is now 7
  sessions overdue. Prior snapshot:
- **82 DSA due as of 2026-08-29 14:40** — **none cleared, 9th consecutive
  zero-review session, and the 4th weekend in a row that the batch did not
  fire.** 80 -> 82 is new intake only (LC 40 `[derive]`, LC 90, both at +1 for
  2026-08-30). The three `[leech]` items are now **15 days** without their
  mandated daily recall. The weekend-only decision was due today and was not
  taken; the audit still has not been run. Today's evidence bears directly on
  it: two defects written up the previous night were reproduced within 16
  hours, while a rule *derived* in-session transferred within 5 minutes. That
  is an argument about **how** review must be run (re-derive, not re-read) as
  much as when — take both to the audit. Prior snapshot:
- **80 DSA due as of 2026-08-28 22:15** — **none cleared, 8th consecutive
  zero-review session.** 77 -> 80 is new intake only: Frog Jump (DP-3)
  `[derive]`, Subsets and Combination Sum `[derive]` all entered at 2026-08-29,
  deliberately on the +1 rung so they land in this weekend's batch rather than
  after it. The three `[leech]` items are now **14 days** without their
  mandated daily recall. **The weekend-only decision is due tomorrow and the
  audit still has not been run** — flagged 08-24, 08-25, 08-26, 08-27. Today
  adds evidence on the retention side specifically: a problem recorded as
  solved on 07-10 turned out to contain a crash bug and a wrong answer, which
  is a failure of verification rather than of spacing, but it lands on the same
  question — what the tracker's "solved" column is actually worth without a
  review that re-runs the code. Prior snapshot:
- **77 DSA due as of 2026-08-27 18:50** (per `tools/build_dashboard.py`) —
  **none cleared, 7th consecutive zero-review session.** Flat at 77 for a third
  day: 3 new items entered future-dated (LC 84 → 08-30, LC 907 `[derive]` → 08-30
  on a deliberate 3-day short interval, LC 739 → 09-03), and LC 735 remains
  due-and-unrun since 08-26. The three `[leech]` items are now **13 days** without
  their mandated daily recall. **The weekend-only decision is due this weekend —
  it is 2 days away and the audit has not been run.** Today adds a second piece of
  evidence in the amendment's favour (a weekday coverage session produced 3 new
  problems, the cycle's best), which sharpens rather than settles the question:
  coverage throughput is clearly served by weekday-only coverage, and retention is
  clearly not being served by a review batch that has not fired in 12 days. Those
  are separable decisions and the audit should treat them separately. Prior snapshot:
- **77 DSA due as of 2026-08-26 19:20** (per `tools/build_dashboard.py`) —
  **none cleared, 6th consecutive zero-review session.** Flat at 77 for a
  second day, and this time nothing moved in either direction: LC 42 entered
  the ladder future-dated to 08-29, and LC 735 remains due-and-unrun from
  today. The three `[leech]` items are now **12 days** without their mandated
  daily recall — the mechanism has been inoperative for longer than it has ever
  operated. **The weekend-only decision is now overdue at the audit rather than
  merely due**: it was flagged 08-24 and 08-25 as a decision to take before
  this weekend, and this weekend is in 3 days. Note today supplies the first
  evidence in the amendment's *favour* — a weekday coverage session produced a
  fully-spoken Hard solve — so the audit has two-sided data, not just the three
  failures (LC 435, LC 735, LC 930). Prior snapshot:
- **77 DSA due as of 2026-08-26 18:50** (per `tools/build_dashboard.py`) —
  **none cleared, 5th consecutive zero-review session.** Flat at 77 is
  coincidence, not stability: LC 930 left the due set (rescheduled 08-24 →
  08-29 after its code was written) and LC 735 entered it (due 08-26, today,
  unrun). No new intake — the session closed an open item rather than adding
  one. The three `[leech]` items are now **11 days** without their mandated
  daily recall. Three weekend batches (08-22/23, 08-16) unrun. The evidence
  against weekend-only batching is now three-deep: LC 435's 8-day blank recall,
  LC 735's 1-day non-retention of a written diagnosis, and now LC 930's silent
  fix. **This is overdue as a decision — take it to `interview-prep-audit`
  before the next weekend, not after.** Prior snapshot:
- **77 DSA due as of 2026-08-24 17:29** (per `tools/build_dashboard.py`) —
  **none cleared**, 4th consecutive zero-review session. 75 → 77 is intake and
  roll-forward only: LC 1358 and LC 930 came due today untouched, and LC 735
  went from an unsolved-problem line to a real review item at **2026-08-26**
  (2-day short interval, user decision — a problem that failed cold twice has
  no evidence behind +1/+3 spacing). The three `[leech]` items are now **9 days**
  without their mandated daily recall. Two weekend batches (08-22/23) plus this
  weekday session have produced zero cleared reviews; the weekend-only
  amendment is now carrying contrary evidence from two directions (LC 435's
  8-day blank recall, and LC 735's 1-day total non-retention of a written-up
  diagnosis). **Take this to the next audit as a decision, not an observation.**
  Prior snapshot:
- **75 DSA due as of 2026-08-23 10:33** (per `tools/build_dashboard.py`; +3
  new, all future-dated to 08-24: LC 1358, LC 930 `[derive]` code-unwritten,
  LC 735 `[derive]` unsolved) — **none cleared**. 72 → 75 is new intake only;
  the backlog itself did not move because no weekend batch has fired since
  08-15. The three `[leech]` items (Bellman-Ford 0/2, Redundant Connection 0/2,
  Task Scheduler 1/2) are now **8 days without the daily recall their own rule
  mandates** — the leech mechanism is inoperative under weekend-only batching,
  and 08-15's "do not re-open the weekday `+1` trade on this data" now has
  contrary evidence (see the LC 435 blank-recall entry above). Decide at the
  next audit. Prior snapshot:
- **72 DSA due as of 2026-08-18 17:43** (per `tools/build_dashboard.py`; +1
  new, future-dated: Minimum Coins review #1 → 08-22) — none cleared, weekday
  coverage session under the weekend-only policy. **The 60 → 72 jump is not
  new intake — it is the missed weekend**: 08-16's batch never ran and three
  days of scheduled items came due behind it. One missed weekend costs ~12
  items, exactly the concentration risk the plan named. Next weekend batch
  (08-22/23) now carries two weekends' worth against a 12-item cap. Prior
  snapshot:
- **60 DSA due as of 2026-08-15 17:20** (per `tools/build_dashboard.py`) —
  **12 cleared, the first non-zero session in 18.** 69 → 60 nets out as: 12
  reviewed and rescheduled forward, 1 graduated off the ladder entirely (Rotate
  Array — first graduation since the mechanism was added 2026-07-25), +1 new
  (LC 435, due 08-16), and 3 `[leech]` items now carrying explicit due dates so
  the parser counts them. **The weekend-only amendment passed its first test**:
  6 of 12 clean cold, including three (Kosaraju, Dijkstra, Prim's) that needed
  heavy escalation on their previous pass. No `correction`-where-`clean`-used-to-
  be signal. Do not re-open the weekday `+1` trade on this data. Two items
  newly `[leech]` (Bellman-Ford, Redundant Connection), one at 1/2 clean toward
  graduating off it (Task Scheduler). Prior snapshot:
- **69 DSA due as of 2026-08-14 22:20** (+1 added, future-dated: Shortest Job
  First review #1 → 08-16), **17th** consecutive session with no reviews
  cleared, weekend-only policy. The weekend batch is **tomorrow** — 08-15/16 is
  the amendment's first real test, watch whether review #1 outcomes come back
  `correction` where they used to come back `clean`. Prior snapshot:
- **69 DSA due as of 2026-08-13 17:39** (+2 added, both future-dated to the
  weekend batch: LC 678 review #1 → 08-15, Merge Intervals review #1 → 08-16),
  **16th** consecutive session with no reviews cleared, still weekend-only
  policy, not slippage. The count moving 70 → 69 is a **parser effect, not a
  cleared review**: LC 678's problem line was missing a `solved:` field, so it
  was skipped by `tools/build_dashboard.py` until this session. Next weekend
  (08-15/16) is the first real test of the weekend-only amendment — watch
  whether review #1 outcomes come back `correction` where they used to come
  back `clean`. Prior snapshot:
- **70 DSA due as of 2026-08-12 20:38** — unchanged (nothing newly solved; LC
  678 code still open, so no review item created), **15th** consecutive session
  with no reviews, still policy not slippage. Prior snapshot:
- **70 DSA due as of 2026-08-12 17:52** (+1: Lemonade Change LC 860, `[derive]`,
  scheduled to **2026-08-15**, not `+1`) — none cleared, **14th** consecutive
  session with no reviews, but this one is **policy, not slippage**: user's
  standing instruction is "always coverage, reviews on weekend," and the weekday
  `+1` block is now struck from the plan (`30day-sprint.md` Block 2). The
  amendment's tell-tale is the weekend clean-rate on review #1 — if those start
  coming back `correction`, re-open the trade. Assign Cookies `[derive]` and
  Candy `[derive]` now roll to 08-15; LC 621 `[leech]` 8 days late.
  Prior snapshot:
- **69 DSA due as of 2026-08-11 20:30** (+1: Assign Cookies LC 455, due
  2026-08-12, `[derive]`) — none cleared, **13th** consecutive session with no
  reviews, and the first miss of the DSA-First plan's non-negotiable `+1` block
  (session ran ~25 min, ended mid-Block-1). Candy `[derive]` now 2 days late;
  LC 621 `[leech]` 7 days late. Prior snapshot:
- **68 DSA due as of 2026-08-11 18:27** — none cleared, **12th** consecutive
  session with no Block B; session was System Design only, no DSA touched. **+1
  on the SystemDesign track** (Rate Limiter, due 2026-08-12, `[derive]`) — first
  entry that track has ever had, and it is not counted in the 68 (the script
  parses DSA). LC 621 `[leech]` now 6 days late. Prior snapshot:
- **67 due as of 2026-08-09 16:43** (+1: Candy LC 135, due 2026-08-10,
  `[derive]`, code unwritten) — none cleared, **11th** consecutive session with
  no Block B. **LC 621 review #2 tagged `[leech]` this session** — 6 days late,
  tagged on the standing miss rule rather than a 3rd failed answer (basis noted
  in `../DSA/Progress/review_schedule.md`). **Count correction**: this 67 is
  `tools/build_dashboard.py`'s number. The hand-carried figures in the snapshots
  below had drifted low (they read 58 where the script says 67, and the
  logged-live count read 69 with only 68 in the file) — re-run the script and
  read counts off it rather than incrementing the previous line by hand.
  Prior snapshot:
- **58 due as of 2026-08-08 23:24** (+1: Fractional Knapsack, due 2026-08-09,
  `[derive]`, code still unwritten) — none cleared, 10th consecutive session
  with no Block B. LC 621 review #2 still 5 days late. Prior snapshot:
- **57 due as of 2026-08-08 20:46** — none cleared, 9th consecutive session
  with no Block B; no new items (nothing solved, Fractional Knapsack left
  open mid-derivation). LC 621 review #2 now 5 days late. Prior snapshot:
- **57 due as of 2026-08-08** (+1: Job Sequencing bounded-heap variant, due
  2026-08-09, `[derive]`, logged **read-not-derived**) — none cleared, 8th
  consecutive session with no Block B. LC 621 review #2 (due 08-05) now 4
  days late — one more miss triggers `[leech]`. Prior snapshot below still
  applies:
- **56 due as of 2026-08-07** (per `tools/build_dashboard.py`) — none
  cleared, no new items (session was pressure-test only). LC 621 review #2
  (due 08-05) still open, 3 days late. Prior snapshot below still applies:
- **~54 due as of 2026-08-06** (est. — 4 new items added: Min Platforms,
  Jump Game, Jump Game II, Job Sequencing, all due 2026-08-07) — none
  cleared, 6th consecutive session choosing new material over Block B by
  explicit user preference ("solve all new problems first, reviews after").
  LC 621 review #2 (due 08-05) still open — one more miss triggers
  `[leech]`. Prior snapshot below still applies:
- **50 due as of 2026-08-05** (per `tools/build_dashboard.py`) — none
  cleared, 5th consecutive session choosing new material over Block B
  (N Meetings in One Room, Minimum Number of Platforms both new). LC 621
  review #2 (due 08-05) also still open — one more miss triggers `[leech]`.
  Prior snapshot below still applies:
- **43 due as of 2026-08-02 16:54** (+3 this session — Find Median from Data
  Stream, Merge k Sorted Lists, Task Scheduler, all due 2026-08-03) — none
  cleared, user chose new material over Block B for the 4th session running.
  Prior snapshot below still applies:
- **40 due as of 2026-08-02 10:50** (per `tools/build_dashboard.py`) — none
  cleared 2026-08-02, user chose new material over Block B for the 3rd
  session running. Prior snapshot below still applies:
- **33 due as of 2026-08-01 22:03** (+1 this session — Top K Frequent
  Elements, due 2026-08-02, `[derive]`, comparator-direction mistake
  flagged for next review). Prior snapshot below still applies:
- **32 due as of 2026-08-01** (per `python3 tools/build_dashboard.py`; +3
  new added this session — Floyd-Warshall, Kruskal's, Prim's, all due
  2026-08-02 — offset by cleared/closed items). Core Graph algorithm
  coverage (Dijkstra/Bellman-Ford/Floyd-Warshall/Kruskal's/Prim's/Union-
  Find) is now complete at least once — Graph work going forward is
  review-ladder only, not new material.
- **32 due as of 2026-07-30 17:50** (4 cleared this session: Min Stack #2,
  Dijkstra #1, Bellman-Ford #1, Redundant Connection #1 — none fully clean).
  Tiers: 07-24 (8), 07-25 (6), 07-26 (11, Graph batch #1s incl. Kosaraju
  `[derive]`, deferred today), 07-27 (7). Prior snapshot below still applies:
- **35 due as of 2026-07-27 19:17** — counts here are now generated, not
  hand-tallied: run `python3 tools/build_dashboard.py` and read them off, or
  open `Progress/dashboard.html`. Tiers: 07-24 (9, 3d late), 07-25 (6, all
  Sliding Window #1s), 07-26 (11, Graph batch #1s), 07-27 (9, incl. Dijkstra
  and Bellman-Ford `[derive]`). 13 of the 35 are `[derive]`.
  **Policy change 2026-07-27: with 13 days left and 4 tracks at zero, do NOT
  open with a full 12-item Block B.** Cap reviews at ~5 (leech + `[derive]`
  only) and give the rest of the session to the zero tracks — a loop is scored
  on its weakest round, and 71% of reviews now come back clean, so slipping
  the settled ones costs retention, not the interview. See
  `../DSA/Progress/review_schedule.md` for the full list.
- Import backlog (Binary Search/LinkedList/BST/Trees/DP/Tries, solved 2-3mo
  ago, first re-verification pass): ~161 problems, 1 done (Frog Jump).

## Track Readiness

    DSA           195/455 import (42.86%) + 106 logged live · ~63 reviews due · 95 reviews done, 69% clean · 2 graduated · LC 51 off the list (3 declines, like LC 131); LC 47 declined 2x · Graph coverage-queue 4/12 (Course Schedule, Course Schedule II, Alien Dictionary, Number of Enclaves) · bucket 2 at 12/15, remainder (LC 60, LC 282) both Hard · BitManip 5/5 (complete) · see DSA/Progress/progress.md
    SystemDesign  1/24 case studies · Rate Limiter depth partial (2026-08-11, 3 gaps open) · 2 concepts · 5 mistakes · 1 review due 08-12
    LLD           0 logged · not started
    Behavioral    0 logged · not started
    Java          0 sessions · 1 incidental signal 2026-08-27 (Stack vs ArrayDeque, unknown) · see Java/topics/Collections.md
    Applications  1 active (1 target, referral out) · see Applications/tracker.md

## Top Weak Area Pointer

**Update 2026-09-01 18:47 — item 1 is unchanged and now has a second instance;
item 3 from 08-31 is closed by its own prescription being ignored twice.**

**Item 1, and it is the same item as last night: derivation-to-code regression.**
LC 137's mod-3 rule was derived aloud, checked by hand on the binary columns of
`[1,1,1,2]`, and then written as `freq[i]%2` — the rule from LC 136, solved ten
minutes earlier. Interval: minutes, same as M-Coloring's `i != prvNodeColor`.
Across LC 37 and LC 137 the count is **8 defects, 8 at the write step, 0 in the
derivation**. The prescription has not changed and has not been run: **after
deriving a predicate aloud, write that predicate as the first line of code,
before the surrounding structure.** Two sessions, two misses; if it goes unrun a
third time it should be replaced with something that fires without being
remembered — the derived line pasted into the editor as a comment before coding
starts, for instance.

**Item 2, new and it is the cheapest thing on this list: row-major flattening.**
`box = (r/3)*3 + c/3` cost 12 minutes and the full escalation ladder, ending in
a handover, and the identical misunderstanding produced `i*3+j` as a cell stride
on a 9-wide grid. The blocking idea is that `(r/3)*3` is not `r` — truncation
happens first. This is not backtracking and not Sudoku; it is grid indexing, it
will appear in every remaining grid problem, and it closes in one focused
sitting. Written up in `../DSA/patterns/Backtracking.md` and the LC 37 note.

**Item 3, structural, and it outranks the content items now: reviews are not
happening at all.** Three consecutive skips retires the 08-30 in-block
mechanism by its own terms, and it is the second mechanism this cycle adopted
and never executed. 56 items due, 5 straight declines of a two-question leech
drill, and M-Coloring's own carried complexity question dropped on the day it
came due. The audit should not design a third mechanism before answering why
the first two produced zero reviews.

**Item 4, unchanged: hint-shape matching, 5th occurrence.** Two defects named in
one message on LC 37; the one pointed at a specific token was fixed and pasted,
the other ignored. The replacement prescription from 08-31 — restate the defect
in one sentence in the same message as the pasted fix — went unrun on all three
pastes today.

**Positives, and they are the reason the item list is short on content.** No
greedy-first-match in three problems. The base-case invariant stated cold on LC
37, and the LC 137 derivation complete and unaided end to end, including
rejecting the HashMap on the space bar and reaching "we need bit 31 too". Both
complexities cold on LC 37 (`O(9^k)`, `O(1)`), which is the question that ended
the previous session unreached.

**Update 2026-08-31 21:48 (session 2) — item 1 of the 17:30 update closed, and
what replaces it is narrower and cheaper to act on.**

**Item 1, and it supersedes greedy-first-match: derivation-to-code regression.**
On M-Coloring the legality rule was derived correctly in words ("reads
`color[neighbor]` for every neighbor in `graph[curNode]`") and the code written
two minutes later used `i != prvNodeColor` — the previous-node-only version that
had *just* been refuted by a traced counterexample. This is the 08-28/29/30
transfer-gap family, but the interval collapsed from 16 hours to minutes, which
rules out decay and points at the writing step itself: code is being produced
from a stored template rather than from the sentence just spoken.
**Prescription: after deriving a predicate aloud, write that predicate as the
first line of code, before the surrounding structure.** Cheap, checkable, and it
does not depend on remembering anything later.

**Item 2, the 17:30 item 1 is closed — greedy-first-match self-corrected cold.**
Third occurrence, opening approach on M-Coloring ("on conflict return false"),
and it took **one question** — "does that prove the graph can't be coloured?" —
to produce "no, we should try other colors for previous nodes". The pre-code
check prescribed at 17:30 ("if this choice dead-ends, which line brings control
back here?") was then answered **unprompted**. First member of this family to
close without escalation. Keep the check; stop treating the family as open.

**Item 3, new and it is about method, not content: parking a trace is expensive.**
The disconnected-component question was posed as a guided trace, declined
mid-way ("i will have to come back at this question later"), and returned 4
minutes later as the judge's failing test (`V=3, edge 1-2, m=1`). The same
session's other two WAs were also mechanical defects that a trace would have
caught. Against the standing evidence that derivation encodes and reading does
not, this says the trace is not an optional teaching device — it is the cheapest
available verification. **Finish the trace, or accept the WA as its substitute.**

**Item 4, unchanged and still unfired: hint-shape matching.** No new occurrence
this session — but also no test of it, since all three fixes were directed at a
named line. The 17:30 replacement prescription ("restate the defect in one
sentence in the same message as the pasted fix") was **not** followed on any of
the three pastes and was not enforced. Carry it forward; it has not yet had a
real trial.

**Item 5, process, now at the mechanism's own threshold**: 2nd consecutive skip
of the opening-review block, 4th consecutive `[leech]` decline, 19 days without
the mandated recall. **One more skip retires the mechanism by its own reversal
trigger.** Decide at the audit rather than letting it lapse silently.

**Update 2026-08-31 17:30 — the content item changed and the process item is
unchanged and now urgent.**

**Item 1, content, new and it supersedes the 08-30 boundary: greedy-first-match.**
Twice in one session, on two unrelated problem shapes. LC 139 opened with a trie
plus "take the first word that matches and advance `start`"; LC 51 opened with
two nested loops placing a queen in the first non-attacked column of each row.
Neither had a return path. The 08-30 claim — that the blocker is *choosing where
a variable-length piece ends* — predicted LC 139 correctly but is too narrow:
this is one level up (legality is being read as correctness) and it fired on a
board problem too, where piece length is not a concept. **Prescription, and it
is a pre-code check, not a debugging one: before writing the loop, answer "if
this choice dead-ends three levels down, which line brings control back here?"
No answer means it is greedy.** Note the counterexample must be constructed with
care — `"catsandog"` returns the right answer greedily; `"catsdog"` is what
exposes it.

**Item 2, process, 4th occurrence and the prescription has now failed 3 sessions
running: hint-shape matching.** Twice today, and the second time was *after* it
had been named aloud in-session. (a) N-Queens: shown a 5-character row string as
an illustration, added an `else`, left the `res` shape — which was the actual
question — untouched. (b) LC 46: told two precedence bugs existed, fixed the one
the compiler named and left `goalMask` alone. The 08-30 prescription was "re-run
the counterexample before declaring a fix"; it has not fired once. **Replacement,
narrower and cheaper: restate the defect in one sentence in the same message as
the pasted fix. If it can't be stated, the edit isn't the fix.** Related: 5th
silent fix — both LC 139 defects were spoken only when asked directly, one after
4 escalations and an analogy.

**Item 3, positive and it is the strongest signal of the session**: the
place/recurse/undo skeleton on LC 46 was written **cold, correct, with both
undos present, 20 minutes after that exact mechanism had been declined on
N-Queens**. Memoization on LC 139 also went in unprompted. Whatever is failing
on N-Queens, it is not the backtracking template.

**Item 4, a decline to watch**: N-Queens is at 2 declines. LC 131 came off the
coverage list at 3. The approach has been restated cold and correctly twice and
the fix was named correctly by the user — only the code is missing, so a
dedicated short block should close it before it hits the same threshold.

**Update 2026-08-30 15:51 — the top item is now a process item, and the
content boundary got narrower.** Three problems, three judge verdicts, all
Accepted — the first clean verification session of the cycle, and it removes
"is a logged solve real" from the open questions for these three.

**Item 1, and it is the one to act on: hint-shape matching, 2nd occurrence.**
On LC 79 the `|` vs `||` distinction was stated correctly *and* its cost was
stated correctly ("the other three subtrees still run, at every level") — and
the fix that followed still changed only the operator on the `return` line,
leaving four eager assignments above it. Explaining the mechanism did not
produce a correct edit. The 08-29 prescription for exactly this ("re-run the
counterexample before declaring a fix") was one day old and did not fire.
**Prescription, stronger: after any hint-driven edit, the counterexample gets
re-run before the fix is called done — by the user, out loud, not assumed.**

**Item 2: the 08-29 board/grid-vs-string-index prediction is wrong as stated.**
LC 17 is string-index and produced a complete correct approach before any code.
LC 131 was declined a 3rd time without an attempt, contributing no evidence
either way. The surviving distinction is **fixed-stride vs variable-length
choice**: advancing `index+1` is fine (LC 17, LC 79, LC 216); choosing where a
piece *ends* (`j` over `i..n-1`) is where LC 131 has stalled three times. That
is narrow enough to predict and to design a drill against, and LC 131 should
either get a dedicated block on that one move or come off the list — take to
the audit.

**Item 3, positive and worth protecting**: the concrete-instance prescription
closed both "i didnt get it" moments inside a few minutes each (the 4-frame
space trace on LC 17, the `k=3,n=3,[1,2]` instance on LC 216), and start-index
dedup came back **cold** from LC 39/40 two days later. Derivation is still the
only thing that encodes — `DSA/recall/daily.md` has now gone unused for four
sessions and the drill has been declined twice running.

Process, unchanged: 2 declines left the `||` mechanism, LC 79's complexity, and
the `>=` monotonicity reason handed over rather than spoken. New this session:
explicit resistance to writing code at all, first occurrence.

**Update 2026-08-29 16:51 — the top item is unchanged and now has a third
data point, but a sharper second item appeared.** The base-case ordering rule
was met a 3rd time in two days on Rat in a Maze. It was fixed silently, then
**un-fixed** — the patch was removed without performing the swap it was being
traded for, restoring the original bug — then fixed correctly, and only then
spoken aloud, after being asked what the accept branch assumes. Two things to
act on. (a) The generalization that came out of it was **wrong** and was
affirmed: "reject before accept — same as LC 40" is inverted with respect to
LC 40, where accept must go first. `../DSA/patterns/Backtracking.md` and
`../DSA/flashcards/recursion.md` are rewritten to state the rule as a question
about preconditions, which yields both orderings. (b) When a hint is given,
the edit that follows is matching the hint's *shape* rather than the defect —
re-run the counterexample before declaring a fix.
**Second item, and this is the new one: there is now a predictive boundary.**
In one session: N-Queens produced four cold correct derivations and the user
closed their own "why not just one oprn?" by computing a counterexample
unprompted; Rat in a Maze produced correct code unaided; LC 131 was abandoned a
second time with "i dont understand this prblem" *after* its concrete layer had
already been derived correctly. The split is board/grid state vs string-index
state, and it extends the 08-27 physical/visual finding from a description into
a prediction. Prescription: on string-index problems, draw and label the index
line before generalizing.
Positive signals: approach before code on N-Queens, unprompted, first in 3
sessions; lexicographic call ordering fixed on one prompt.
Process: complexity declined outright ("lets move") on Rat in a Maze, so it is
logged unspoken, not covered — the same outcome as 08-25.

**Update 2026-08-29 14:40 — the top item is that written notes do not encode,
and there is now a controlled comparison for it.** LC 40 reproduced two defects
that were sitting in the tracker from the night before: the `Set`-on-result
pitfall (`../DSA/patterns/Backtracking.md`, top entry) and accept-before-reject
base-case ordering (`../DSA/flashcards/recursion.md`, written 22:17 on 08-28,
reproduced 13:58 on 08-29). Against that, the skip-on-decline rule — six
escalations and a guided trace to derive on LC 40 — came back **cold and
unprompted on LC 90 five minutes later**, and the copy-cost complexity gap that
took a nudge on LC 40 was stated cold on LC 90 six minutes later, closing the
5th logged transfer gap inside one session. Same day, same topic, opposite
outcomes; the variable is derived-vs-read. **Consequence to act on: the
`DSA/recall/daily.md` questions must be run as an opening drill, cold, before
new problems — the file has been written to for three sessions and never once
used.** Second item, process: code arrived before the approach on both problems
after the approach was explicitly asked for first, and LC 40's base-case bug was
fixed silently with no statement of what had broken — the same silent-fix
pattern logged 08-25. Positive signal: LC 90 was independent, cold, correct on
first submit with complexity stated unprompted.

**Update 2026-08-28 22:15 — the top item is no longer a reasoning weakness, it**Update 2026-08-28 22:15 — the top item is no longer a reasoning weakness, it
is a bookkeeping one.** Frog Jump had sat in `progress.md` as solved since
07-10 with a "corrected recurrence"; it contained an out-of-bounds crash on
every `n>=2` input and, once rewritten, a roll that returns the wrong answer.
Neither could have survived a single judge submission, which means the entry
recorded a *derivation*, not a solve. The guardrail already says coverage
counts only with working code — today shows an entry that predates the
guardrail slipping through anyway. **Consequence to act on: entries logged
before the guardrail (pre-08-11) are not evidence of a passing submission, and
the 12 unnamed DP gaps sit in exactly that region.** Two content items behind
it. (1) The **transfer gap has compressed to 12 minutes** — the copy cost in
`res.add(new ArrayList<>(list))` was priced correctly on Subsets and omitted on
Combination Sum, same line, same session. That is the 4th transfer gap and the
shortest interval yet; the countermeasure is a checklist item, "what does
recording one answer cost?", now in `../DSA/flashcards/recursion.md`. (2) A new
and unusually portable rule: **a `Set` on a backtracking result is a branching
bug** — filed as the top pitfall in `../DSA/patterns/Backtracking.md`. Positive
signal: Subsets was cold, independent and correct on first submit, and the
`2^n` justification came on the 2nd ask without a ladder. Process, unchanged
from 08-27: 3 "just tell me" requests, most escalations still terminating at
full explanation.

**Update 2026-08-27 18:50 — the weakness has narrowed to a nameable boundary,
and a second one appeared.** Three sessions running, the *why* now comes cold
when the mechanism is **physical or visual** (LC 42's submerged bars 08-26,
LC 84's cuttable taller bars, LC 739's strictness of "warmer"). It still does
not come cold when the mechanism is **abstract counting**: LC 907's endpoint
count needed the pairs enumerated on a 4-element array before `i` was accepted
as its own endpoint. That is a sharper target than "justification weakness" and
it matches the standing prescription — instantiate numerically — with a
condition on *when* it is needed. Second, new, and more expensive: **the tie
rule in a reused template**. LC 84 and LC 907 share `nsl/nsr` code exactly; the
first tolerates duplicate double-claims because it takes a `max`, the second is
corrupted by them because it takes a `sum`. The template moved, the rule did
not, and the result was a wrong answer rather than lost time — the escalation
the 08-26 template-first entry predicted. Filed as the top entry in
`../DSA/patterns/MonotonicStack.md` with an all-equal input now mandated as a
standing test case for the pattern. Third item, process not content: 4 "just
tell me" requests in one session, against 1 the session before. The escalation
ladder mostly terminated at full explanation. Worth watching whether that
tracks session length (85 min, the longest in weeks) or problem difficulty
(2 Hards).

DSA is the only track with live signal — see
`../DSA/mistakes/mistake_journal.md` for the current recurring-mistake list
(boundary/post-loop checks, invariant-"why" derivations, and visited-timing
have each recurred 3+ times) rather than restating it here. **SystemDesign came
off zero 2026-08-11** — Rate Limiter, ~38 min, depth partial. LLD/Behavioral/
Java remain at zero for the full 33 days — **12 days left, still the top
overall gap**. Note the zero-track drought did not break via the +15min slot
(skipped 15 straight sessions and never once run); it broke by giving System
Design a full session block. Read that as the fix: schedule the zero track as
the session's *first* block, not a 15-minute tail.

**Update 2026-08-11 18:27 — the justification signal is confirmed cross-track,
and it is the single most portable finding in the tracker.** The System Design
track's very first session reproduced the DSA Greedy pattern exactly, four
times in 38 minutes: the mechanism came out cold every time (N x L breach,
INCR lost-update trace, 2x fixed-window boundary, 7.2B counter arithmetic),
and the paired cost/tradeoff half had to be asked twice every time. Same
abstract-vs-concrete split too — "what do you build?" got "I don't know";
the identical question with 3 customers / 100 req/sec / 494 idle got a correct
independent derivation of floor + shared-pool. This is no longer a Greedy
issue or a DSA issue. The prescription stands unchanged and now applies
everywhere: instantiate numerically, then symbolize, then force the
conclusion's form. Second finding, new class: a transfer-gap inside a single
session — the fixed-window boundary bug was derived independently at
second-scale, then not recognized at minute-scale four minutes later
(2nd transfer-gap logged; first was DSU, 2026-08-07).

**Update 2026-08-11 20:30 — the justification weakness got its first
countermeasure the user asked for.** Assign Cookies reproduced the pattern a
6th time (mechanics + code + edge case cold, `why` needed the ladder), but the
session's output was method, not problems: the user asked what "instantiate →
symbolize → conclusion form" means, what the conclusion form *is*, and how to
run it live. All three are now written down in
`../DSA/patterns/GreedyExchangeArgument.md` — two proof shapes, a 3-part test
for whether an answer even qualifies as a proof (named rival plan + explicit
move + compared number), and a 4-sentence interview script. **Next Greedy
problem tests the script, not the intuition**: ask for rule → rival → move →
close, in that order. Second item: sort-space misaccounting recurred (said
O(1) for a primitive sort, true O(log n)) — 2nd in 4 days, opposite direction
from the 08-08 TimSort miss; "primitives or objects?" is now a standing
complexity checklist item.

**Update 2026-08-12 17:52 — the greedy *why* now has a reproducible unlock, and
a second standing instruction landed.** Lemonade Change made it 7 consecutive
Greedy problems where mechanics come cold and the justification does not — but
for the first time the prompt that unlocks it is specific and reusable rather
than improvised: **"write both wallets right after the same customer — what's
the exact difference?"** That is a *state-domination* swap (compare the
resources you hold afterwards), distinct from the value-comparison swaps used
on Knapsack/Assign Cookies, and it is now filed as a sub-shape in
[[GreedyExchangeArgument]]. The 4-sentence interview script written on 08-11 was
offered and declined ("I already solved the problem") — **still untested live,
so pose it as the first question on the next Greedy problem, before the code, or
it will keep reading as redundant after a correct solve.** Two process changes
this session, both user-set and both recorded rather than re-argued: reviews are
weekend-only (see Reviews Due), and **session length is asked for at resume, not
assumed** (both resume SKILL.md files updated). New positive signal: the user
raised a proof obligation *unprompted* for the first time ("how do we guarantee
it's a solid run and not holes") — that is the justification weakness inverting,
and worth watching for a second occurrence before calling it a trend.

**Update 2026-08-12 20:38 — the justification weakness has a diagnosable cause,
not just a working prompt.** LC 678's derivation finished but all four remaining
pieces needed escalation, and the session ended on *"i dont think i really
understand why am i even implementing this"* — after the question "min and max
are the min and max of **what collection**?" had been asked three times and
answered vaguely each time. Mechanics were being built on a state whose meaning
was never stated, so the clamp and the bail-out were unjustifiable by
construction. **Standing fix, cross-track: when a problem carries compressed
state (an interval, a counter, a monotonic stack, a rate-limiter bucket), do not
advance to mechanics until the user says what that state ranges over. A vague
answer there predicts the whole "why" chain failing later.** Second item: when
asked to trace a failing input through their own code, the user patched a
suspect line instead (deleting a correctly-derived `min--`, adding a new bug)
— 2nd guess-instead-of-trace (first: Minimum Platforms 08-05). Third: correct
reachable set produced, then misread when stating the rule, twice; "what's the
min of the set you just wrote?" recovered it both times in one step.

**Update 2026-08-13 17:39 — the justification streak broke, first time in 9
problems.** Merge Intervals (LC 56) came out cold end to end: full code correct
first try, complexity right including the `int[][]` sort buffer, the tie-break
spotted as dead code, and the load-bearing justification ("ends increase along
the kept list, so the last end is the largest") produced after **one** re-aim,
with no ladder and no counterexample supplied. Eight consecutive problems
(08-05 through 08-12) had needed real escalation on the *why*; this one did
not. One occurrence is not a trend — the test is the next unfamiliar
justification, and the LC 678 equivalence still sits open. Second item, the
countermeasure that worked on LC 678: the user found the dead `else if` in two
questions, and building the `")*"` counterexample was the part that needed the
ladder — so **counterexample construction, not proof comprehension, is the
narrower live weakness**; the fix is to solve backwards from what the accept
path requires rather than searching over inputs. Third, a mentor-side
correction the user raised directly: the interval justification was pressed for
a second round after a substantially correct answer ("you're irritating me with
question 2 every time"). Same class as the 2026-07-27 hint-grading fix — a
correct answer closes the question. Standing rule added to `../CLAUDE.md`.

**Update 2026-08-14 22:20 — the session's costs were engagement and
comprehension, not reasoning, which is a new axis for this tracker.** Two of
~29 minutes' worth: Insert Interval was posed and sat ~6 minutes with no
attempt before "i dont like this problem" (routed in one question — boring, not
murky — and swapped without argument; it stays queued, but **do not re-pose it
as an opener**), and the replacement problem's *statement* then needed a guided
trace before any algorithm could start ("I don't understand this problem"), on
a problem whose code came out cold and correct minutes later. Every previous
entry in this dashboard is about mechanics or justification; neither of these
is. One occurrence each, so not a trend — but the cheap countermeasure for the
second is now written down: **run the sample under any arbitrary choice and diff
it against the expected output; the gap names what the problem is asking.**
Third item, and the one with a standing consequence: **the 4-sentence greedy
script has now been declined three times** ("i dont think we need script for all
the problems"). The objection is right — it is scaffolding for a stuck *why*,
not a per-problem recital — so [[GreedyExchangeArgument]] is amended to ask the
plain one-sentence why by default and expand only when that sentence doesn't
come. Counterweight: the primitives-vs-objects sort-space miss recurred a 4th
time but was **recovered in a single nudge off the user's own checklist item**,
where 08-08 and 08-11 both took real escalation.

**Update 2026-08-15 17:20 — twelve reviews in one sitting split the tracker's
central weakness cleanly in two, and the split is the finding.** Everything that
came back clean was **mechanics**; everything that failed was **why it works**.
Clean cold: Lemonade's state-domination swap, Rotate Array's double-reversal,
Kosaraju's finish-order argument, Prim's cut rule *and* its why, Dijkstra's
contradiction proof (handed over entirely last pass), Nearest Smaller's code and
pop rule. Failed: Floyd-Warshall (6th attempt), Redundant Connection (4th
escalation), Bellman-Ford (both points, verbatim repeats), LC 678 (4
escalations), Kth Largest. The user named this themselves mid-session — *"do we
need more reviews on these kind of problems? I already know their workings"* —
and they are right about the workings and about 6 of the 12. **Policy answer
given, and it should hold**: a flat 60-item backlog is the wrong shape —
graduate aggressively (the 2-consecutive-clean rule has existed since 07-25 and
fired for the first time today), keep `[leech]` + last-session failures, and
give the remaining weekend capacity to coverage, since the plan already declares
the backlog frozen. The one counterweight, stated to the user: Bellman-Ford was
clean cold on 07-26 and failing on 07-30 — the *why* decays in four days even
when mechanics don't, so "I know it" and "I'll know it in a month" are different
claims.

**Three findings with standing consequences.** (1) **The unprompted-proof-demand
is now a trend, not a one-off** — told that `V-1` bounds a shortest path, the
user refused the assertion (*"it's not convincing"*) and built the entire
cycle-cutting argument themselves. The 08-12 entry asked to watch for a second
occurrence before calling it; this is it, and it is the justification weakness
running in reverse. (2) **First transfer *success* in the tracker** — LC 435's
earliest-end rule is the same rule that broke twice on N Meetings in One Room
(08-05, constructed counterexample both times); it came out cold here on an
unfamiliar problem. Every prior `transfer` entry is a gap (DSU 08-07,
fixed-window 08-11). (3) **A memorized complexity hid a coverage hole** —
build-heap's O(n) was recalled correctly, then "I don't understand the heapify
method": sift-down had never been built, and the constant had been carried since
08-02 attached to nothing. New mistake class `coverage-gap`. Standing fix: when
a review turns up a correct constant, ask for the mechanism before accepting it.

**Process, 2026-08-15**: session durations now log to
`~/LifeOS/Work/deep_work_log.md` on every save (user instruction). Prompted by
"what's the total study time" being unanswerable — `~/InterviewPrep` has no
duration field at all, and `deep_work_log.md` had 2 entries between 07-13 and
07-31. Cycle total on the books before today: ~7.2h across 36 days, against a
plan written for 2h/weekday.

**Update 2026-08-18 17:43 — the justification ladder now closes inside a
10-minute block, and the session's only real error was the mentor's.** Minimum
Coins reproduced the greedy-*why* pattern an 8th time (mechanics and complexity
cold, first answer to "why" a mechanics-restatement), but the fix ran to form
and finished in ~3 minutes: instantiate both plans numerically (n=39, 6 coins vs
7), then ask for the general bound, which came cold — dropping one 10 costs ≥2
coins back. The prescription is no longer just correct, it is *fast*; treat it
as the default opening move on any greedy why, not an escalation step. Second
item, and the one with a standing consequence: **the OJ link and the problem
statement disagreed** — the statement was paraphrased from memory (full Indian
denomination set, return-the-list) while the link was the {1,2,5,10} count
variant, and a wrong expected output was asserted for n=121. The user's code was
correct and they said so; the correct response to "my code is right" was to
re-read the link, not ask another pointed question. ~3 of 10 minutes went to a
defect that did not exist. **Standing fix: pose the statement from the linked
page's own text, never from memory.** Logged in the mistake journal as a
mentor-side entry, same as the 07-27 hint-grading and 08-13 re-ask corrections.

**Pace re-run 2026-08-07 22:13** (`interview-prep-pace`): ~149h estimated
remaining vs 17 days to 08-23 = ~8.8h/calendar day, ~13.7h per *active* day
at the 64% show-rate (18/28 days active). Not achievable. ~120h of the 149
is DSA new + stale-backlog — the lowest-yield share, re-verifying topics
already at full coverage while LLD/Behavioral/Java/SystemDesign sit at
zero; those four total ~22h and do fit in the window. **The recommendation
was a scope cut, not more hours.**

**DECISION 2026-08-11 18:56 — DSA-first, end-to-end coverage. ACTIVE.**
User's stated goal: finish DSA coverage before anything else, for confidence
to interview anywhere. `target_end` moved to **2026-11-30** (`cycle.md`),
~210 problems at ~17.5/week on weekdays. SystemDesign/Behavioral/LLD/Java are
**paused, not cut** — they resume at block 1 when a screen or onsite is
scheduled. Session shape, coverage queue, and guardrails:
[30day-sprint.md](30day-sprint.md) "DSA-First Coverage Plan". Non-negotiable
inside it: the daily `+1` review (weekends carry the rest) and full code per
problem — approach-only is what the old coverage already was. Accepted
consequence, recorded so it is not a November surprise: **the 68-item review
backlog is frozen, not clearing** — weekend capacity (24) roughly matches new
weekday intake (15-20). Third `target_end` move re-opens the goal, not the
date.

*Superseded, kept for the decision trail — the 18:45 scope cut:*

**DECISION 2026-08-11 18:45 — scope cut adopted.** (Superseded an 18:40
decision to keep full scope and add hours; reversed 5 min later once 12.3h/day
was acknowledged as not doable. Both recorded in
`~/LifeOS/Wisdom/decision_journal.md`.) Budget assumed **2h/day × 12 days =
~24h** through 08-23 — a deliberately conservative floor, not a target; if a
day runs longer the extra goes to whatever sits next in the priority order
below, it does not reinstate the dropped scope.

    KEEP — 24h allocation
      SystemDesign   ~6h   4 more case studies (URL Shortener next)
      Behavioral     ~4h   5-6 STAR stories, from zero
      Java           ~3h   4 subtopics (Collections, Concurrency, JVM-GC, OOP)
      LLD            ~3h   SOLID + 1 case study
      Reviews        ~6h   4-5/session, [leech] + [derive] priority only
      DSA new        ~2h   max 1 problem/session

    DROPPED — explicitly, not deferred
      · 161-problem stale-import re-verification (Binary Search/LinkedList/
        BST/Trees/DP/Tries) — cut entirely, ~100h+, lowest yield in the plan
      · DSA new-material push beyond 1/session
      · Clearing the 68-review backlog — it will not clear; leeches and
        [derive] get worked, the settled tail is accepted as decay

**Priority order when a day is missed** (and days will be missed at a ~64%
show-rate): zero tracks first, reviews second, DSA new last. This inverts the
last 12 sessions' actual behaviour, which is the entire point of the cut —
the target loop is 2 DSA + 1 system design + behavioral, and DSA is the one
track already covered.

**Update 2026-08-09 16:43 — the justification gap is not a Greedy problem, it
is a proof-form problem.** Candy (LC 135) is not selection-order greedy (no
sort, no exchange argument — two-pass constraint propagation, new pattern file
`../DSA/patterns/TwoPassConstraintPropagation.md`), yet the *same* failure
appeared: every mechanic cold, the **minimality** proof cold, and the
**validity** proof needing the full ladder (2 "i don't get it", 1 "no idea")
until it was instantiated on a concrete array. Reframe the weak area
accordingly — it is not "greedy justification", it is *any* justification posed
abstractly. The working prescription is unchanged and now cross-topic:
instantiate numerically, then symbolize, then force the conclusion's form.
Secondary this session: Fractional Knapsack's code came out correct and cold on
the first try, including both bug surfaces predicted at the last save — the
first evidence that a flagged code-skip, when actually collected, closes clean.

**Update 2026-08-08 23:24 — the greedy-justification signal has a first
resolution.** The Fractional Knapsack exchange argument was produced (5th
Greedy session, first success), but only after the swap was decomposed into
per-unit values, both totals written out, and the delta subtracted — the
intermediate guess was wrong (20 vs +5) and the first conclusion was the
*rule*, not the proof. Working form recorded in
`../DSA/patterns/GreedyExchangeArgument.md`: instantiate numerically, then
symbolize, then force "we can construct ___, therefore P is not ___." Treat
the abstract phrasing as known-not-to-work, not as a harder test to keep
trying. Secondary: 4/4 edge cases clean and cold — edge-case work is now
consistently the strongest block, complexity facts the weakest (space read as
O(log n), TimSort's O(n) object-array buffer unknown).

Fourth signal, 2026-08-08: **greedy justification** has now needed real
escalation in 4 of 4 Greedy sessions (08-05 "why end-time", 08-06 "why
max-reach", 08-08 "why evicting the heap min is never regretted", 08-08 20:46
"why highest ratio first"). Mechanics come out cold every time; the *why* does
not — and opening with the justification question (tried 20:46) did not change
the outcome, so the fix is the *form* of the answer, not the ordering: demand a
concrete two-item swap with a numeric delta, per the new
`../DSA/patterns/GreedyExchangeArgument.md`. Counterweight 08-08: the 08-07 DSU
transfer-gap re-posed and closed in 1 nudge.

Third signal, new 2026-08-07: first **transfer-gap** mistake logged (DSU
recognized in Graphs, not retrieved as a "nearest free resource ≤ x"
accelerator in a Greedy problem). Distinct class from stale-recall — the
technique was coded cleanly 12 days earlier. Watch whether it repeats on
other cross-topic reuses.

Second signal, new 2026-08-02: derivations are being verified against a
single traced example and then lost. Task Scheduler's closed form was
derived, checked on two inputs, and unrecallable ~5 minutes later — same
shape as Floyd-Warshall's 5-session invariant stall. Close every derivation
by restating what each term counts, in words, before moving on.

## Model (added 2026-09-01)

Prep sessions run on **Sonnet 5** from 2026-09-01 (cost: $2/$10 per 1M vs Opus 5's
$5/$25, both 1M context). **One model per session, start to finish, including the
save** — a mid-session switch re-sends the whole conversation and prompt caches
are model-scoped, so switching to Opus for the save alone pays full uncached rate
on everything. Log the model in the session ledger in
[model_eval.md](model_eval.md); that file is the periodic Opus check for whether
the switch cost anything, due after ~8-10 Sonnet sessions (~2026-09-15).

## Session Protocol (adopted 2026-07-20, review-cap lowered 2026-08-01)

**2026-08-01 update**: given the target_end extension and remaining-scope math
(`interview-prep-pace`), reviews are capped at ~3-5/session (leech + `[derive]`
priority only, same selection rule as the 07-27 policy) — the rest of session
time goes to new problems, not the old 30% Block B split. Rationale: front-
loading all new material with reviews deferred entirely risks a backlog that
comes back mostly rusty (Bellman-Ford regressed clean-to-failing in 4 days,
07-26→07-30; clean-rate drops 74%→36% from review #1 to #3) — a small
continuous review cap avoids that without the old 12-item tax on new-topic
time.

Every session, fixed 3-block split — do not revert to single-topic grinding:

- **Block A (30-40%)**: rusty 2yr-recall re-verification, no topic is
  genuinely new (corrected 2026-07-26 — full sheet solved 2yrs ago; see
  `../DSA/Progress/progress.md` Current Position) — currently Graphs
  (Dijkstra + Bellman-Ford done 07-26; Floyd-Warshall/Prim's/Kruskal's/
  Union-Find remain — do Union-Find before/with Kruskal's)
- **Block B (30%)**: due reviews — hard cap 12/session, overflow rolls to next
  day; skipped-as-trivial counts as NOT done; never two consecutive
  same-subtopic problems
- **Block C (20-30%)**: stale import backlog re-verify, 3-5 problems, rotate
  topic daily
- **+15 min**: one zero-track item — 1 STAR story draft OR 1 Java subtopic OR
  1 LLD concept

Standing rules:
- **1 timed cold solve per session**: pick a problem already clean at review
  #1+, 25 min (Easy/Medium) or 40 min (Hard), no hints, full code. Log as
  `clean-in-time | solved-overtime | failed`.
- **`[derive]`-tagged reviews**: start with the "why" before any code — unable
  to derive = failed review even if code is correct.
- **`[leech]`-tagged reviews** (added 2026-07-25): daily short recall on just
  the stuck point until 2 clean, then resume the ladder — see
  `../DSA/Progress/review_schedule.md`.
- **Show-rate beats session length**: 90 min daily beats a planned 12-hour
  sprint that doesn't happen.

## How This File Updates

After every session, refresh only what changed: day counter (sprint mode
only), this week's focus (if the week rolled over), reviews-due count, and the
readiness table row(s) for tracks touched. Never re-add narrative detail that
belongs in a track's own progress.md/mistake_journal.md.
