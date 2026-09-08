---
type: topic
topic: Greedy
updated: 2026-08-23
status: in-progress (started 2026-08-02 via Task Scheduler; prior "not-started" flag from 2026-07-10 superseded by the 2026-07-26 rusty-2yr-recall reclassification)
---

# Greedy

## Subtopics (Striver A2Z order)

Striver's Greedy step is **16 problems**. Logged here: 14. Remaining:

    Insert Interval (LC 57)              DEFERRED 2026-08-23 (declined twice)
    LRU Page Replacement Algorithm       not attempted

Enumerated 2026-08-23 — this section had been an empty placeholder, so nothing
in the tracker said what "Greedy complete" would even mean.

## Patterns That Show Up Here

_To be linked as problems are worked through._

## Problems Log

- Minimum Number of Platforms (GFG) — 2026-08-05, generalization closed
  2026-08-06 — two-pointer sweep + arrival-before-departure tie-break
  self-derived cold; O(n log n)/O(1) clean. "Why caps at 2 regardless of
  chain length" closed via "each interval touches only its immediate
  neighbor, never overlaps two." Code still not written.
  https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
- Jump Game (LC 55) — 2026-08-06 — solved independently, cold, full code,
  no bugs. "Why greedy (max-reach dominates)" needed 1 targeted question.
  O(n)/O(1). https://leetcode.com/problems/jump-game/
- Jump Game II (LC 45) — 2026-08-06 — solved independently. Heap-based
  O(n log n) self-derived cold first, then self-optimized to O(n)
  two-pointer unprompted once asked if the heap was necessary. No bugs
  either version. https://leetcode.com/problems/jump-game-ii/
- Job Sequencing Problem (GFG) — 2026-08-06 — with-hints:2. Two real
  approach mistakes (deadline-sort instead of profit-sort; earliest-slot
  instead of latest-slot), both self-corrected via constructed
  counterexamples. Code correct once fixed. **Pressure-test closed
  2026-08-07**: O(n²) worst case + the all-deadlines-=-n shape derived
  cold; DSU slot-find optimization (O(n log n)) needed full explanation.
  **DSU close-the-loop closed 2026-08-08** in 1 nudge (`parent[x]` is a
  redirect, not a claim that x is free — only a root is a real free slot).
  [note](../notes/job-sequencing.md)
  https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
- Job Sequencing — bounded-heap variant — 2026-08-08 — **read, not derived**
  (code pasted from GFG, self-disclosed). Deadline-asc sort + min-heap of
  selected profits, evict min when `deadline <= pq.size()`. Derived in
  session: why the sort key flips (heap does the selecting, sort only
  supplies feasibility order), O(n log n)/O(n), and `!pq.isEmpty()` is a dead
  branch (`size >= d >= 1`) — all cold. The no-regret exchange argument
  needed 4 escalations. Third approach to this problem (array O(n²), DSU
  O(n·α), heap O(n log n)). See mistake_journal 2026-08-08.
- Fractional Knapsack (GFG) — posed 08-07, 08-08, attempted 2026-08-08 20:46.
  Mechanics **cold and correct** (value/weight ratio, max-heap, fraction of
  the last item). The "why is highest-ratio-first safe" answer was circular
  (restated the objective) — escalated to a concrete unit-swap
  (W=10, A w6/v60, B w10/v50, claimed-optimal 2A+8B), **session ended before
  the delta was computed**. Not solved; complexity/edge cases/code all still
  open. https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
  **Closed 2026-08-08 23:24 (except code)** — with-hints:several. Exchange
  argument produced after the swap was decomposed unit by unit (delta guessed
  20 before the two totals were traced to 60 and 65, giving +5 =
  ratio(A)−ratio(B)); conclusion then stated in proof form. Time O(n log n)
  cold; space O(n) after the TimSort fact was supplied (answered O(log n)).
  Edge cases 4/4 clean cold. [note](../notes/fractional-knapsack.md).
  **Code closed 2026-08-09** — correct first try and cold, no bugs; space O(n)
  cold this time; heap-vs-sort pressure test clean (sort gives the same order
  upfront; the heap only wins at k << n via bulk heapify, which this code
  doesn't use).
- Candy (LC 135) — 2026-08-09 — with-hints:many — approach only, code declined.
  Not selection-order greedy: two-pass constraint propagation, see
  [[TwoPassConstraintPropagation]]. Mechanics all cold (two passes, both arrays
  on `[1,3,2,1]`, `max` merge, O(n)/O(n), one-array refinement); minimality
  proof cold; **validity proof needed the full ladder** and only landed on
  concrete instantiation. O(1) run-length variant open (parked). Code open.
  https://leetcode.com/problems/candy/ See mistake_journal 2026-08-09.
- N Meetings in One Room (GFG) — 2026-08-05 — with-hints:several —
  approach only, code skipped (user judgment). Sort-by-end-time mechanics +
  strict `end < nextStart` boundary self-derived cold, O(n log n)/O(n) clean.
  "Why end-time, not start-time or duration" needed heavy escalation both
  times (constructed counterexamples), closed cleanly after. Edge cases
  (empty/single/identical/all-overlapping) clean.
  https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
  See mistake_journal 2026-08-05.
- Task Scheduler (LC 621) — 2026-08-02 16:54 — with-hints:several —
  approach only, code not written. Greedy rule (highest remaining
  frequency among available tasks first) justified at interview bar;
  tie-break key and cooldown offset both wrong before self-correction.
  Closed-form `(maxFreq-1)*(n+1)+countMax` derived then lost within
  minutes — `max(formula, tasks.length)` case still open.
  https://leetcode.com/problems/task-scheduler/ See mistake_journal.
- Assign Cookies (LC 455) — 2026-08-11 20:21 — solved independently, full code
  cold, no bugs. Sort both ascending, walk both from the back; `i--` always,
  `j--` only on assignment. O(n log n + m log m) time cold; space O(log n) after
  1 nudge (said O(1)). Empty-`s` edge cold. Exchange argument produced via the
  numeric ladder (`g=[3,1]`, `s=[4,9]`), generalized to `g[D] ≤ g[C] ≤ s[k]`;
  drop-branch justified ("no *remaining* cookie can satisfy C").
  https://leetcode.com/problems/assign-cookies/ See mistake_journal 2026-08-11.
- Lemonade Change (LC 860) — posed 2026-08-11 20:27 with link, **not attempted**,
  session ended. https://leetcode.com/problems/lemonade-change/
  **Closed 2026-08-12 17:26 — with-hints:1**, full code. Bug: `Arrays.sort` on
  an order-dependent input (`[10,5]` counterexample). Guards, the
  ten+five-over-three-fives preference, O(n)/O(1), and the empty-input edge all
  cold. Exchange argument landed in 4 exchanges via the wallet-diff prompt:
  vs a rival paying 5+5+5, you end with 2 extra fives and 1 fewer ten, and the
  ten's only job (15 owed on a $20) is coverable by fives, which also serve a
  $10 customer. See mistake_journal 2026-08-12.
- Valid Parenthesis String (LC 678) — started 2026-08-12 17:38, **parked
  mid-derivation, no code**. Landed: reachable open-counts form a set, dead
  negative branches prune, and the set is always a solid interval (`(`/`)`
  shift it, `*` unions three overlapping shifts, pruning cuts a prefix) — so
  carry only `(min,max)`. Open: per-character update rules, min-clamp at 0,
  early bail-out, accept condition, code. DP+memo named as the O(n²) fallback.
  https://leetcode.com/problems/valid-parenthesis-string/
  **2026-08-12 20:38 — derivation closed, code open.** with-hints:many. Rules
  (`(` both+1, `)` both−1, `*` min−1/max+1), `max<0` bail, min-clamp to 0, accept
  `min==0` — all reached, all via escalation. Twice produced the correct
  reachable set then misread it when stating the rule. Code has an unreachable
  `max<0` check (`else if`) and a blind patch that removed `min--` on `)`.
  Session ended with "I don't understand why I'm even implementing this" — the
  meaning of the carried state had been asked for 3x and never given.
  **Code closed 2026-08-13 17:23 — with-hints:2.** Dead `else if` chain located
  in 2 questions (`min<=max` ⇒ `max<0` unreachable), `min--` restored
  unprompted, `")*"` counterexample built via a 3-step ladder, return
  simplified to `min==0` alone. O(n)/O(n) (`toCharArray()`, 1 nudge). Open: the
  `min==0` ⇔ `min<=0<=max` equivalence, user-parked.
- Merge Intervals (LC 56) — 2026-08-13 17:32 — **solved independently, full
  code cold, no bugs, no escalation**. Sort by start, merge into the last kept
  interval on `last[1] >= cur[0]`, mutate through the stored reference.
  O(n log n)/O(n) cold with the `int[][]` buffer counted. Both pressure tests
  cold: last-interval-only is safe because **ends increase along the list, so
  the last holds the largest end**; the `a[1]-b[1]` tie-break is dead code.
  https://leetcode.com/problems/merge-intervals/
- Shortest Job First (GFG) — 2026-08-14 22:20 — with-hints:2, **full code cold,
  correct first try**. Sort ascending, running clock, add the clock to the total
  before advancing it by the current burst; `total/n` floors as required.
  O(n log n) time cold; space O(n) first, corrected to **O(log n)** in one nudge
  off the "primitives or objects?" checklist (`int[]` → dual-pivot quicksort
  stack, no TimSort buffer). Neither hint was algorithmic: one was the problem
  *statement* not parsing, one was the sort-space item. The exchange argument is
  **open** — posed as the 4-sentence script and declined.
  `Arrays.sort(bt)` mutates the caller's array (not raised by the user).
  https://www.geeksforgeeks.org/problems/shortest-job-first/1
- Insert Interval (LC 57) — posed 2026-08-14 (**declined as boring**) and again
  2026-08-23 (**declined as "pain"**). No attempt either time. **Status changed
  2026-08-23: explicitly DEFERRED, not queued** — so the coverage count stops
  reporting it as open work in progress.
  https://leetcode.com/problems/insert-interval/

- Non-overlapping Intervals (LC 435) — 2026-08-15 16:52 — with-hints:1 —
  https://leetcode.com/problems/non-overlapping-intervals/ — first code sorted
  by **start** and always kept the earlier interval; failed `[[1,100],[2,3],
  [3,4]]` (returned 2, answer 1). Counterexample handed over; user then named
  the fix (keep earliest-ending) and the *why* — "the earlier end leaves more
  room for the rest" — cold, one sentence. Non-textbook loop shape (scan-and-
  jump rather than lastEnd tracking) verified sound: anything overlapping the
  old `cur` starts before the new `cur` and ends after it, so it strictly
  contains the new `cur` and is caught on the next comparison. Complexity
  O(n log n) time; space given as O(log n), corrected to **O(n)** (`int[][]`
  is an object array → TimSort buffer). Edge case: empty array (given),
  touching endpoints `[[1,2],[2,3]]` (the load-bearing one — strict `>` in the
  overlap test is what makes it pass).

- Minimum Coins of 1, 2, 5 and 10 (GFG) — 2026-08-18 17:43 — **solved
  independently, full code cold, no bugs** —
  https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1 —
  descending denomination array, `cnt += n/val; n %= val`. O(1)/O(1) cold
  (4 fixed denominations, no dependence on `n`). Exchange argument landed after
  2 escalations via numeric instantiation on n=39 (6 coins vs 7): dropping one
  10 forces ≥2 coins back, since the largest smaller coin is 5. Mentor gave the
  wrong problem statement with the link (full Indian set + return-the-list);
  user's code and traced output (121 → 13) were correct.

## Common Mistakes Seen in This Topic

- Treating cooldown `n` as "next slot is n away" rather than "n empty
  slots between two runs" — off-by-one in the re-push offset,
  2026-08-02, see [[mistake_journal]].
- Choosing a heap ordering key before asking what the greedy optimises
  (ordered by availability time, ties broken by label) — 2026-08-02,
  see [[mistake_journal]].
- Greedy ordering choice (sort-by-end-time) recalled as mechanics but not
  justified — "why this order, not start/duration" needs a constructed
  counterexample every time so far, not spontaneous — 2026-08-05, see
  [[mistake_journal]].
- Reflexive formula-guessing on "what's the count in this case" questions
  instead of tracing first (2 wrong guesses on Minimum Platforms'
  fully-chained case) — 2026-08-05, see [[mistake_journal]].
- Picking a sort key that doesn't match the actual objective (sorted by
  deadline when the goal was maximizing profit, Job Sequencing) — 2026-08-06,
  see [[mistake_journal]].
- Defaulting to "process ASAP / earliest available" for resource placement
  without checking whether it burns a slot another candidate needs more
  (Job Sequencing) — 2026-08-06, see [[mistake_journal]].
- Not retrieving a known structure outside the topic it was learned in
  (DSU as a "nearest free slot" accelerator, not just graph connectivity) —
  2026-08-07, see [[mistake_journal]].
- Justifying a greedy exchange step by restating the objective ("we want max
  profit so dropping the min can't hurt") instead of naming what future steps
  actually read and showing the swap leaves it invariant — 2026-08-08, 4
  escalations. Third greedy-*why* escalation in this topic (08-05, 08-06,
  08-08): mechanics come out cold, justification does not. See
  [[mistake_journal]].
- Same shape a **4th** time on Fractional Knapsack (2026-08-08 20:46): "we want
  max value so we pick the highest ratio" — goal-restatement, not an exchange
  argument. Standing fix: on any greedy, answer the *why* with a concrete
  two-item swap and a numeric delta before touching mechanics. See
  [[mistake_journal]].
- Answering a swap-delta question with a guessed single number instead of
  differencing the two totals (said 20, true +5) — 2026-08-08 23:24. The fix
  that worked: write the old total and the new total separately, subtract.
  Same session, the exchange argument *did* land — the working form is
  numeric instantiation, never the abstract statement.
- Justifying a merge/combine step by restating what each input guarantees on
  its own, instead of showing the guarantee survives the combine (Candy's
  `max` of two passes) — 2026-08-09. Same abstract-form failure as the greedy
  *why* series, now seen outside selection-order greedy, so the weakness is the
  proof form itself, not the topic. See [[mistake_journal]].
- Reading sort space as O(log n) without checking whether objects or
  primitives are being sorted — object arrays take TimSort's O(n) buffer —
  2026-08-08, see [[mistake_journal]].
- Sorting an input whose *order is the problem* (Lemonade Change's customer
  queue) — sort-first reflex carried over from five consecutive sort-based
  greedy problems. Ask "set or sequence?" before sorting. 2026-08-12, see
  [[mistake_journal]].

## Cut-list queue — itemized 2026-08-31 (Day 0)

From `Progress/coverage_cut_list.md`. `- [ ]` = scheduled, not yet solved.

**3 slots — cut list says "remainder, nearly complete already". Names not
yet transcribed.**

- [ ] TBD x3 — needs Codolio to identify which of Step 12 is unsolved
