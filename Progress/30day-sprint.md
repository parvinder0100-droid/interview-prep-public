---
type: sprint_plan
start_date: 2026-07-10
target_end_date: 2026-08-23
updated: 2026-08-11
---

# 30-Day Sprint Plan

Living plan — adjust as actual pace deviates. Primary-weighted: DSA and System Design
get the most hours; LLD/Behavioral/Java are woven in, not blocked off into separate time.
Applications start immediately, in parallel with training (not after it).

## Week 1 — Days 1–7 (2026-07-10 to 2026-07-16)

- **DSA**: two combined 2026-07-10 Codolio imports showed 195/455 (42.86%) already
  solved — Binary Search, LinkedList, and BST are 100% done, Trees 92%, Tries 86%,
  DP 79%, but **all solved 2-3 months ago with no practice since** (user-confirmed) —
  treat as rusty, not safe; interleave short interview-speed re-solve reps (start with
  DP and Binary Search, highest interview weight) alongside new material this week,
  don't push all review to later weeks. Real Week 1 priority for genuinely new gaps is
  **Arrays (5%) and Recursion (8%)** first (highest interview weight + biggest
  confirmed holes), then Bit Manipulation and Strings. Basics/Sorting are low-priority
  quick wins given prior experience. Stack/Queue, Sliding Window, Heaps, Greedy, and
  Graphs (~138 problems) are confirmed genuinely untouched — real new-learning
  material for Week 2/3, with Graphs as the top priority among them given its
  interview weight.
- **System Design**: fundamentals as encountered — scaling, load balancing, caching,
  DB indexing, CAP theorem.
- **Java**: Collections framework basics.
- **Behavioral**: draft 5–6 STAR stories (leadership, conflict, failure, ownership,
  impact). Resume is ready — start applying now, in parallel with training.
- **Applications**: `Applications/tracker.md` starts empty per user's choice; log
  entries as applications actually go out.

## Week 2 — Days 8–14 (2026-07-17 to 2026-07-23)

- **DSA**: Stack/Queue and Sliding Window/Two Pointer — genuinely new material, learn
  from scratch. Continue Recursion/Backtracking. Finish re-verifying LinkedList/BST/
  Trees reps started in Week 1 (2-3mo stale, same rust-risk treatment).
- **System Design**: first full case studies (e.g. URL shortener, rate limiter).
- **LLD**: SOLID principles, core design patterns.
- **Java**: concurrency basics (threads, locks, executors).

## Week 3 — Days 15–21 (2026-07-24 to 2026-07-30)

- **DSA**: Heaps, Greedy, and **Graphs** (all genuinely new material — Graphs is the
  highest-priority of the three given its near-universal presence in big-tech
  interview loops), finish verifying DP gaps.
- **System Design**: larger systems (news feed, chat app, distributed cache).
- **LLD**: case studies (parking lot, elevator system, etc.).
- **Java**: JVM internals & GC.
- Start first full mock interviews (coding + system design).

## Week 4 — Days 22–30 (2026-07-31 to 2026-08-09)

- **DSA**: close out whatever's left in Stack/Queue/Sliding Window/Heaps/Greedy/Graphs,
  finish DP gaps, Segment Tree/Fenwick/Union Find only if time allows.
- **All tracks**: heavy spaced-repetition review of every logged weak area — this is the
  highest-leverage week, not new-topic week.
- Full mock interviews back to back (coding + system design + behavioral).
- Application follow-ups and interview scheduling.

## Extension — Days 31–44 (2026-08-10 to 2026-08-23)

**Target end extended 2026-08-01** (was 2026-08-09) — pace math showed the
original window couldn't cover DSA new/backlog/reviews plus zero-activity
SD/LLD/Java/Behavioral at the 61% historical show-rate (`interview-prep-pace`
projected full completion around mid-Dec at that rate). 2 extra weeks does not
close that gap on its own (~163h remaining vs. ~11.6h/day needed even across
all 14 extra days) — treat this as breathing room, not a fix. Priority order
for the extension: (1) close the zero-activity tracks (LLD/Behavioral/Java/
SystemDesign — flagged repeatedly as the top gap), (2) Greedy + remaining DP
gaps (highest interview weight of what's left), (3) mocks, (4) DSA
backlog/review volume — accept this will not fully clear by 08-23 either.

## DSA-First Coverage Plan — 2026-08-11 18:56 (ACTIVE — supersedes everything above)

Goal, in the user's words: **finish DSA coverage end-to-end, to be confident
enough to interview anywhere.** Everything else waits. This supersedes both the
extension priorities and the 18:45 scope cut below.

    target        Striver A2Z, ~210 problems remaining (~245/455 covered)
    rate          2h/weekday, ~3.5 problems/session = 17.5/week
    target_end    2026-11-30 (see cycle.md for the three-scenario basis)
    other tracks  SystemDesign/Behavioral/LLD/Java paused at current state

### Weekday session (Mon-Fri, ~2h)

1. **Block 1 — coverage, ~1h45, 3-4 new problems.** Draw from the Coverage
   Queue below, top-down. Do not topic-hop mid-block; finish a topic's queue
   entry before starting the next. Every problem gets: OJ link given up front,
   cold attempt, full code written (not approach-only — approach-only solves
   are what produced the "code unwritten" flags on Candy, Fractional Knapsack,
   Job Sequencing), complexity stated, one edge case named.
2. ~~**Block 2 — the +1 review only, ~15 min.**~~ **AMENDED 2026-08-12 — the
   weekday review block is removed.** User's standing instruction: *"always
   coverage, reviews on weekend."* Weekdays are coverage + save; every review,
   including what would have been the `+1`, batches to the weekend sessions.
   Recorded rather than re-argued each session. What this costs, stated once so
   November isn't a surprise: the `+1` was the steep part of the forgetting
   curve, and Monday's problems now get their first look on day 5+, so
   `review_schedule.md`'s "batch-late never" rule no longer holds for the first
   interval. Watch the weekend clean-rate — if review #1 outcomes start coming
   back `correction` where they used to come back `clean`, that is the amendment
   showing up in the data, and the trade should be re-opened then, not before.
3. **Close — save.** Run `interview-prep-save`. Duration must be logged, or
   the pace forecast has nothing to read.

### Weekend session (Sat/Sun) — RETIRED 2026-08-30, see DECISIONS above

~~Reviews only, hard cap 12 each.~~ Never executed: 6 consecutive weekends at
zero. Replaced by review questions inside every coverage block. Kept below for
history.

### Weekend session (Sat/Sun, 2 sessions, hard cap 12 each) — historical

Reviews only — the batched `+3 / +7 / +14 / +30` intervals, plus whatever can
be chipped off the 68-item backlog. No new coverage required; any that happens
is ahead of schedule and pulls the target_end in.

**Why the split rather than pure weekend batching**: `review_schedule.md`'s
standing rule is "overflow rolls forward, early pulls allowed, **batch-late
never**." The `+1` is the steep part of the forgetting curve and the
highest-yield review in the system — batched to Saturday, Monday's problems
get reviewed on day 5 and the `+1` stops existing. Later intervals genuinely
are not date-sensitive; a `+14` landing on day 16 costs almost nothing.

**Capacity, stated so it is not a surprise in November**: weekdays generate
15-20 new review items/week; weekend capacity at the 12-cap is 24. Weekends
therefore roughly break even against new intake and **the 68-item backlog is
frozen, not clearing**. That is an accepted consequence of this plan, not an
oversight — revisit only if clean-rate starts falling.

**Concentration risk**: at a 64% show-rate a missed weekend kills a full
week of reviews at once, where a missed weekday kills one day's. If a weekend
is missed, the following weekday's Block 2 expands to 12 rather than letting
two weeks stack.

### PLAN B — finish the 94 cut list by 2026-09-17 (user decision 2026-08-31)

**Origin**: user asked to finish the entire cut list in one week. That was
costed and declined in favour of this. The arithmetic, recorded so it is not
re-litigated:

    remaining          84 of 94 (bucket 2 has 10 done; dashboard's 83 is the
                       same number with the known +/-1 drift)
    one week           12 problems/day, ~5-6 h/day deep work, 35-42 h total
    observed rate      2-3 problems per 60-70 min session; best day this cycle
                       was 3 problems / ~86 min across two sessions
    verdict            12/day is 4x the best observed day, sustained 7 days
                       including a weekend that has gone to zero 6 times

The deciding objection was not the hours, it was the protocol. 25 min/problem
does not fit cold approach + code + judge + defect named aloud + complexity
derived + journal entry. It fits code-and-submit — which is the mode that
produced the Codolio import this cut list exists to re-verify, and which put
Frog Jump on the books as "solved" from 07-10 with a live crash bug.

**CORRECTION 2026-09-01**: the "79 of 84 unnamed" figure below is **stale** —
Day 0 itemization partly ran on the evening of 08-31. Disk now shows **~33 named
and workable** (Graph 6, Stack/Queue 6, Strings 6, BitManip 5, Heap 4, Sorting 2,
Trie 1, plus bucket 2's remaining 3) against **~49 still `TBD`** (Arrays 13,
DP 12, Graph 6, SlidingWindow 6, Stack 4, Trees 3, Greedy 3, Heap 2).
Consequence: itemization is **not** an immediate blocker and does not need to
pre-empt a coverage block. It is due before the named 33 are exhausted — call it
end of week 1 — and it stays a transcription chore, not a session.

**THE REAL BLOCKER, and it is not DP**: as of 2026-08-31, `grep -c '^- \[ \]'`
returns **0 for every one of the nine remaining buckets**. Arrays Hard, Graph,
Stack/Queue, Sliding Window, Strings, Heaps, Bit Manipulation, Trees, Greedy,
Sorting, Tries, DP — none itemized. **79 of the 84 remaining problems are
unnamed.** The 08-28 "BLOCKER on bucket 1" was a special case of this, not a
DP-specific issue. Nothing solves until they are named.

**Shape (revised 2026-08-31 17:51, user chose the faster split)**:
2 sessions/day weekdays, **3 sessions/day weekends**, ~70 min each.
**~40/week**, finishing **2026-09-17**. New requirement is 40/week,
superseding both the 6.5/week set on 2026-08-30 and the 28/week first drafted
this evening.

**Weekend weighting corrected.** The first draft gave weekends *half* the
weekday load, reasoning from "6 consecutive weekends at zero". That was a
misreading: those were zero **reviews** — the reviews-only weekend policy that
never fired and was retired 2026-08-30. Weekend *coverage* was fine, and is in
fact the best in the cycle:

    Sat 2026-08-29   2 sessions (14:40, 16:03)
    Sun 2026-08-30   2 sessions (14:51, 20:47) — 3 problems in 60 min, best
                                                 single block of the cycle

Weekends are the days without a job in them and the days with the highest
observed throughput. They carry the surge.

**Time cost, stated so it is not discovered mid-week:**

    Mon-Fri    2 x 70 min      2 h 20 m/day     ~5 problems
    Sat, Sun   3 x 70 min      3 h 30 m/day     ~7-8 problems
    week                       18 h 40 m        ~40 problems
    total                      ~42 h            84 problems
    plus Day 0                 + 2 h            Tue 09-01 is 4 h 20 m

40 problems / 18 h 40 m = 2.1 per hour, the low end of the observed 2-3 per
70-min session — the plan does not assume the rate improves. Total hours are
unchanged from the 3-week draft; the schedule is compressed, not cheapened.

    Day 0   Tue 2026-09-01, 2.0 h, NOT a session block
            Itemize all 9 buckets from the Codolio web UI into topics/*.md.
            This is transcription, not study — it does not come out of
            coverage time, and no bucket after 2 is executable without it.

    Week 1  Tue 09-01 -> Sun 09-07   32   bucket 2 remainder (5) + DP gaps (12)
                                         + Arrays Hard (13) + Graph (2)
                                         4 weekdays only, and Day 0 costs a block
    Week 2  Mon 09-08 -> Sun 09-14   40   Graph (10) + Stack/Queue (10)
                                         + Sliding Window (6) + Strings (6)
                                         + Heaps (6) + Bit Manip (2)
    Week 3  Mon 09-15 -> Wed 09-17   12   Bit Manip (3) + Trees 3 / Greedy 3
                                         / Sorting 2 / Tries 1
                                    --
                                    84

**Bucket 2's remaining 5, named 2026-08-31** (they were never itemized either):
N-Queens (LC 51, open at 2 declines), ~~M-Coloring (GFG)~~ **done 2026-08-31,
Accepted**, Kth Permutation Sequence (LC 60), Sudoku Solver (LC 37), Expression
Add Operators (LC 282). **4 remain; bucket 2 is 11/15.** The ladder held — the
adjacency-scan legality that M-Coloring needed is the same constraint-set move
Sudoku wants next, so LC 37 is the natural follow-on even with N-Queens open.
Order is a transfer ladder — N-Queens -> M-Coloring -> Sudoku moves the same
constraint-set idea from `colSet`/`r+c`/`r-c` to adjacency to row/col/box.
Expression Add Operators goes last: it hits the variable-length-piece move that
killed LC 131 *and* operator precedence, which bit on LC 46.

**Update 2026-09-03 21:04**: Kth Permutation Sequence (LC 60) is **Hard**, not
Medium as tagged above — tracker error, caught live by the user off the actual
LeetCode page. **N-Queens dropped at a 3rd decline** (2026-09-03, "not this
one"), same threshold that took LC 131 off the list — approach has been
correct cold twice, code was never written. Sudoku Solver (LC 37) is already
done (09-01). Bucket 2's coverage-list remainder is Kth Permutation Sequence
(LC 60) and Expression Add Operators (LC 282) — both Hard, no Medium left in
the bucket.

**Gates, carried into every session of all three weeks:**

1. Open with the 2-3 review questions (08-30 mechanism). Currently at 1 of 3
   consecutive skips; 3 retires it, and it is the second retention mechanism
   this cycle.
2. Pre-code, spoken, every problem: "if this choice dead-ends three levels
   down, which line brings control back here?" — the greedy-first-match fix.
3. Every pasted fix carries a one-line statement of the defect it fixes.
   Replaces the counterexample-rerun prescription, which has not fired in
   three sessions.
4. Judge verdict on every problem. Without it the 84 is a number, not a fact.

**LC 47 status, 2026-09-01**: Permutations II — the substitute named below for a
3rd N-Queens decline — was itself **declined at approach on its first outing**,
after the dedup rule appeared inside the mentor's question rather than being
derived. It is not consumed; re-pose it cold, without the phrase "a set per
recursive call".

**N-Queens rule**: code-only block, no re-deriving — the approach has been
correct cold twice. A 3rd decline takes it off the list exactly as LC 131 went,
with **Permutations II (LC 47)** substituting.

**Week 1 running count**: 3 of 32 as of 2026-09-01 (LC 37, LC 136, LC 137), one
session of ~92 min. The plan's weekday shape is 2 sessions/day; day 1 ran one.

**Checkpoint and re-cut trigger**: Sunday 2026-09-07. If week 1 lands under
**24** (75% of its 32), the plan is wrong — re-cut the scope. Do **not** move `target_end` a 4th
time; per `cycle.md` that is the signal the goal itself is wrong, which is how
the 08-27 cut was arrived at.

**Untested assumptions, stated once.** (a) 2 sessions/day has happened twice
(08-29, 08-30) and both days ended a session early on attention grounds — 95 of
180 booked minutes on 08-29. This plan assumes it holds for ~14 weekdays.
(b) **3 sessions/day on a weekend has never been run** — the ceiling observed is
2. Six weekend days in this plan need it. If the 3rd weekend block is the one
that consistently doesn't fire, that is a ~6 problem/week shortfall and the
09-07 checkpoint will catch it.

**Consequence worth recording**: at 40/week the 94 finishes ~2026-09-17 rather
than the ~mid-October implied by 6.5/week. Per the 08-27 sequencing decision the
zero tracks (Behavioral, SystemDesign) then open **about a month earlier** than
previously recorded.

### DECISIONS 2026-08-30 (audit, day 52) — three parked items resolved

**1. Coverage queue re-ordered. Bucket 2 is the head; DP follows.**
Option 2 of the 08-28 blocker is taken. Bucket 2 has led for 3 sessions and
produced the best stretch of the cycle (9 problems in 3 days, 3/3 judge-confirmed
on 08-30) — the blocker was never blocking coverage, only bucket 1. Naming the 12
DP problems from the Codolio web UI is a **~15-min chore outside a session block**,
not a coverage block. Due before bucket 2 empties (7 of 15 left, ~2.5 sessions,
so by ~2026-09-02). If it is not done by then, DP moves behind bucket 3 rather
than stalling the queue again.

**2. The weekend reviews-only batch is dead. Reviews move inside the coverage
block.** Evidence: 11 consecutive zero-review sessions, 6 consecutive weekends at
zero, 0 leech recalls in 17 days. A policy that has never once executed is not a
policy. Replacement, non-optional:

    every session opens with 2-3 review questions on the PREVIOUS session's
    problems, plus any `[leech]` point — ~5-8 min, before new coverage

Basis is 2026-08-30's own data: the one review-shaped question that got answered
in 12 days (Rat in a Maze's visited-restore symptom) closed cleanly *because* it
rode inside new-problem work on LC 79, not as a separate block.

**The backlog is NOT archived.** An archive was considered and rejected on
inspection: the 08-27 cut already removed the calendar-only items, so all ~47
overdue entries now carry `[derive]` or `[leech]` — they are the set that cut
deliberately protected. Cutting them would drop the signal and keep nothing.
The backlog stays frozen and is worked down opportunistically by the opening
questions; that is an accepted consequence, recorded once.

**Reversal trigger**: if 3 consecutive sessions open without their review
questions, the mechanism has failed the same way the weekend batch did — at that
point stop redesigning it and take the retention goal itself to `cycle.md` as
wrong.

**3. Palindrome Partitioning (LC 131) comes off the coverage list. Word Break
(LC 139) replaces it.** 3 declines across 3 sessions (08-29 x2, 08-30), ~30 min
spent, no code, every abandonment "I don't understand" rather than a wrong
answer. 2026-08-30 narrowed the blocker: not string-index state (LC 17 was clean
the same session) but **choosing a variable-length piece** — `j` over `i..n-1`
versus a fixed `index+1`. LC 139 is the same move with a boolean answer instead
of enumerating every partition: same skill, less output machinery. LC 131 is
revisitable after LC 139 lands, and is not counted against the 94 meanwhile.

### Coverage Queue — REPLACED 2026-08-27 (scope cut, see `coverage_cut_list.md`)

**Scope cut from ~197 remaining to ~94.** Trigger: this plan's own guardrail
("under ~14/week for two consecutive weeks, the 11-30 date is wrong") fired —
actual rate since the plan was adopted 08-11 is **5.3/week**. `cycle.md` says a
3rd `target_end` move means the goal is wrong rather than the schedule, so the
goal was cut instead of the date.

    before   197 remaining / 13.6 weeks = 14.5/week   (actual 5.3)
    after     94 remaining / 13.6 weeks =  7.4/week

Ordered — do them top-down, finish a bucket before starting the next:

    1. Recursion / Backtracking   15   <- HEAD (re-ordered 2026-08-30), 11 done
    2. DP gaps                    12   blocked until the 12 are named
    3. Arrays — Hard subtopic     13
    4. Graph (classic problems)   12
    5. Stack / Queue              10
    6. Sliding Window              6
    7. Strings                     6
    8. Heaps                       6
    9. Bit Manipulation            5
   10. Trees (3 gaps) / Greedy (3) / Sorting (2) / Tries (1)   9

**Cut, not scheduled**: Basics (31), Graph remainder (24), Segment Tree /
Fenwick / advanced Union-Find (15), Bit Manipulation rest (12), Stack/Queue rest
(10), Recursion warmups (8), Strings rest (6), Heaps rest (6), Sorting rest (5).
Plus the 161-problem re-verification backlog already cut 2026-08-11.

### BLOCKER on bucket 1 (2026-08-28)

**"DP gaps 12" cannot be executed as written — the 12 are unnamed.**
`DSA/codolio_import_raw.json` itemizes only Lec 1 (1 problem) and Lec 2 (5) of
DP's 56; every later lecture was dropped by the export, so 38 of the 44 solved
and **all 12 unsolved** are unrecoverable from disk. Any later-lecture DP
problem picked by hand is as likely to land in the *cut* 161-problem
re-verification backlog as in the kept 12.

Options for the weekend audit, in preference order:

1. Name the 12 from the Codolio web UI (per-problem checkmarks exist there),
   write them into `DSA/topics/DP.md`, and bucket 1 becomes executable.
2. Re-order the queue so bucket 2 (Recursion/Backtracking, 15) leads and DP
   follows once itemized.

Until one of those happens, **coverage runs from bucket 2 onward**, which is
what 2026-08-28 did. This does not change the 94 total or the 7.4/week
requirement — only the order.

### Add-back rule (2026-08-27)

The cut is reversible, and finishing early is the intended way to reverse it.
**Trigger**: at any Sunday checkpoint, if completed problems are **20+ ahead**
of the 7.4/week line (i.e. `weeks_elapsed * 7.4 + 20`), pull the next bucket
back in. Priority order for add-backs:

    1. Segment Tree / Fenwick        15   the most defensible cut; goes back first
    2. Graph remainder               24   pull 12 at a time, not all 24
    3. Stack/Queue rest              10
    4. Heaps rest + Strings rest     12
    5. Bit Manipulation rest         12
    6. Basics + Sorting rest         36   last, and only if everything else is done

**Sequencing — user decision 2026-08-27, supersedes the zero-track guard
below.** The 94-problem cut list is finished **first**, end to end; the cut
buckets are tackled after it, in the priority order above. The add-back trigger
therefore does not fire mid-list — running ahead of 7.4/week means finishing the
94 sooner, not widening the list.

~~**Do not add back to "stay busy."** The four zero tracks (SystemDesign,
Behavioral, LLD, Java) outrank every line above.~~ **Superseded 2026-08-27** by
the sequencing decision above. Recorded rather than re-argued each session. What
it costs, stated once so it isn't a surprise: at 14/week the 94 finishes
~mid-October, so Behavioral/SystemDesign get their first block with ~6 weeks
left, and LLD/Java likely later still. **The switch trigger is the safety net
and stays active**: if a screen or any onsite gets scheduled, the zero
tracks take block 1 for the days before it, cut list or not.

### Coverage Queue — superseded 2026-08-27 (kept for history)

    1. Finish the started-but-open topics   Greedy, Heaps, Stack/Queue,
                                            Sliding Window — small remainders,
                                            highest weight, fastest wins
    2. DP gaps (12 unverified)              highest interview weight on the sheet
    3. Recursion / Backtracking (~23)       high weight, low live coverage
    4. Strings (~12), Bit Manipulation (~17)
    5. Arrays — Hard subtopic (untouched)
    6. Trees (3 gaps), Tries (1 gap: Maximum XOR With an Element From Array)
    7. Final section — Segment Tree / Fenwick / Union-Find
    8. Basics (31), Sorting (7)             lowest weight, clear last and fast

### Guardrails

- **Coverage is not "seen it".** A problem counts as covered only with working
  code + stated complexity. Reading the approach and moving on is what the
  2-years-ago coverage already was, and this cycle measured what it was worth.
- **Weekly checkpoint, Sundays**: run `interview-prep-audit`. The tracked rate
  is **17.5 problems/week**. Under ~14/week for two consecutive weeks, the
  11-30 date is wrong — restate it rather than carrying a stale one.
- **Switch trigger**: when a screen or any onsite gets scheduled, the
  zero tracks (System Design, Behavioral) take block 1 for the days before it.
  The screen is pure DSA so this plan serves it directly; an onsite is where
  untrained System Design and Behavioral would cost the loop.
- **If `target_end` needs a 3rd move**, that is a signal about the goal's size,
  not the schedule's. Re-open the scope question rather than moving the date.

## Scope Cut — 2026-08-11 18:45 (SUPERSEDED ~10 min later by the plan above)

The extension section above said "accept this will not fully clear by 08-23."
That is now an explicit cut rather than an expectation. Trigger: ~148h of
remaining scope against 12 days requires 12.3h/day with no days off;
acknowledged as not doable, so the cut was chosen deliberately instead of
being left to the calendar.

Plan for 08-12..08-23, sized to a conservative 2h/day (~24h):

- **Every session opens with a zero-track block, not a +15min tail.** The
  15-minute slot was skipped 15 consecutive sessions and never once ran — it
  is removed from the protocol rather than re-attempted. The drought broke on
  2026-08-11 only when System Design got a full block first.
- **Order within the zero tracks: SystemDesign, then Behavioral, then Java,
  then LLD** — the target loop is 2 DSA + 1 system
  design + behavioral, so the two tested tracks come first.
- **Reviews: 4-5/session, `[leech]` + `[derive]` only.** The 68-item backlog
  is not going to clear and is no longer treated as a target.
- **DSA: max 1 new problem/session.**
- **Cut entirely**: the ~161-problem stale-import re-verification backlog
  (Binary Search/LinkedList/BST/Trees/DP/Tries). This is the single biggest
  line item and the lowest-yield one — material already at coverage on the
  strongest track, while three tracks sit at zero.

Full allocation table and the missed-day priority order live in
[dashboard.md](dashboard.md) under the 2026-08-11 decision block.

## Notes

- **Correction (2026-07-26)**: user confirmed the complete Striver A2Z sheet
  was solved ~2 years ago — the "genuinely new" framing used throughout the
  weekly plans above (Arrays/Recursion/Stack-Queue/Sliding-Window/Heaps/
  Greedy/Graphs) is superseded. Everything is rusty 2yr recall needing
  re-verification, not ground-up learning — see `../DSA/Progress/progress.md`
  Current Position. Past weeks' logged work stands as-is; this only changes
  framing/pace going forward.
- If interviews get scheduled mid-sprint, `Applications/tracker.md` entries should
  reprioritize the current week's focus toward that company's known format — check
  `Progress/dashboard.md` for the active bias.
- Review intervals are compressed versus the standard 90-day DSA schedule where the
  30-day window would otherwise push a review past the sprint end.
- **Planned: 2026-07-18 & 07-19 — 2-day holiday deep-work sprint** (12+ hrs/day,
  agreed 2026-07-17). Order: close out Print Subarray with Max Sum (unresolved)
  → Recursion (new, full depth) → Binary Search (review, fast pace) → DP (review,
  fast pace) → Stack/Queue (new, full depth) → Sliding Window (new, full depth) →
  LinkedList+BST (review, fast pace) → Trees+Tries (review, fast pace) →
  Behavioral 5-6 STAR stories → 1 System Design case study (Rate Limiter).
  Rationale: clear the entire 2-3mo-stale import backlog (highest live decay
  risk) plus first real exposure to Week 2's new material, in one sitting.
  Explicitly deferred: Graphs, Heaps, Greedy, Java, Applications, Arrays Hard
  subtopic — still at zero after this sprint, revisit in Week 2's remaining
  days. Fatigue risk flagged for Day 2's late blocks (Trees+Tries onward,
  running past 22:00) — cut short rather than log false-clean reviews if
  quality drops.
