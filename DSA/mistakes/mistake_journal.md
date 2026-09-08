---
type: mistake_journal
updated: 2026-09-02
---

# Mistake Journal

Permanent log of every mistake made during problem solving or review. Never delete entries —
this file is the primary source for weakness detection.

## Log (newest first within today)

### 2026-08-31 — M-Coloring (GFG) — derived the rule in words, then coded the rule it replaced
- Mistake: stated the legality test correctly ("reads `color[neighbor]` for every neighbor in `graph[curNode]`") and then wrote `if(i != prvNodeColor)` — the previous-node-only version corrected two minutes earlier.
- Root Cause: the correction lived in speech only; the code was written from the pre-correction mental template, not from the sentence just spoken.
- Correct Thinking: legality on a graph is a scan over the adjacency row, never over the call path.
- How to Avoid: after deriving a predicate aloud, write that predicate as the *first* line of code, before the surrounding structure. Same family as the 08-28/08-29/08-30 transfer gaps, but the gap here is minutes, not hours.
- Pattern: Backtracking
- Review Date: 2026-09-01

### 2026-08-31 — M-Coloring (GFG) — `continue` aimed at the inner loop; the validity scan was dead code
- Mistake: wrote the neighbour scan as `for(kids) if(color[kids]==i) continue;` — `continue` advances the *neighbour* loop, so the scan computed nothing and the colour was always taken.
- Root Cause: `continue` read as "skip this colour" (an intent about the outer loop) rather than "skip this iteration of the loop it sits in".
- Correct Thinking: a nested check must publish its result to the outer scope — a flag plus `break`, or a helper returning boolean.
- How to Avoid: if a loop body assigns to nothing outside itself, it does nothing. Check what each inner loop *writes* before trusting it.
- Pattern: Backtracking
- Review Date: 2026-09-02

### 2026-08-31 — M-Coloring (GFG) — superseded check left in place, became an unconditional false
- Mistake: after the neighbour scan replaced `prvNodeColor`, the old guard `if(color[curNode]==prvNodeColor) return false;` stayed. On the self-edge in `V=2, edges=[[0,1],[0,0]]` the recursion re-entered vertex 0 with its own colour as `prvNodeColor`, returned false, poisoned `res`. WA at 1/1114.
- Root Cause: fixes added, nothing removed — the redesign was additive.
- Correct Thinking: when a mechanism is replaced, its parameter and its guard are both dead and must go in the same edit.
- How to Avoid: after replacing a check, grep the function for the old variable. If it still appears, the edit isn't finished.
- Pattern: Backtracking
- Review Date: 2026-09-02

### 2026-08-31 — M-Coloring (GFG) — recursion entered at vertex 0 only
- Mistake: `return dfs(graph, color, m, 0, -1);` — a graph walk from vertex 0 reaches only vertex 0's component. `V=3, edge 1-2, m=1` coloured the isolated vertex 0, ran an empty kids loop, returned true. Correct answer false. WA at 6/1114.
- Root Cause: the recursion was structured as an edge walk (recurse into neighbours) rather than as a decision-per-vertex; an edge walk has no way to reach a component with no edge into it.
- Correct Thinking: the decision sequence is "vertex 0..V-1, pick a colour", so the driver loops all V and combines.
- How to Avoid: on any graph problem, ask "is the input guaranteed connected?" before the entry call. Standing test: `V=3, edge 1-2, m=1` -> false.
- Pattern: Backtracking
- Review Date: 2026-09-02

### 2026-08-31 — M-Coloring (GFG) — complexity not reached
- Mistake: "no idea" on time and space for the finished, Accepted solution.
- Root Cause: session ended mid-derivation; the two-step scaffold (colours tried at vertex 0, then at vertex 1) had been posed but not answered.
- Correct Thinking: `m` choices per vertex over `V` vertices bounds the tree at `m^V`, each node paying `O(degree)` for the scan; space `O(V)` for `color[]` plus recursion depth.
- How to Avoid: open item — carry to the next session, do not let an Accepted verdict close a problem with the complexity unstated.
- Pattern: Backtracking
- Review Date: 2026-09-01

### 2026-08-31 — Opening review block skipped a 2nd consecutive session (meta)
- Mistake: the mandatory opening review was proposed and declined ("lets solve new probs"); 0 reviews cleared, backlog ~52. 4th consecutive decline of the two-item `[leech]` drill (Bellman-Ford, Redundant Connection) — now 19 days without their mandated daily recall.
- Root Cause: coverage is the felt priority; the mechanism has no cost attached to skipping it.
- Correct Thinking: the mechanism adopted 08-30 has now run once and been skipped twice. **Reversal trigger is 3 consecutive skips — this is 2.**
- How to Avoid: next session opens with the review block before any problem statement is given, or the mechanism is retired at the audit rather than left nominally in force.
- Pattern: process
- Review Date: 2026-09-01


### 2026-08-29 — Combination Sum II (LC 40) — base cases in the wrong order
- Mistake: `if(index>=nums.length||sum>target) return;` placed **above**
  `if(sum==target)`. Any combination whose last element is the array's last
  element is discarded — `[2,5,2,1,2]`, target 5 loses `[5]`.
- Root Cause: the index guard was written as a generic "am I out of bounds"
  check without asking what state the call is in when it fires. A call can be
  simultaneously out of candidates and holding a complete answer.
- Correct Thinking: a terminal check that *accepts* must run before a terminal
  check that *rejects*, or the accept never gets a chance.
- How to Avoid: **this exact rule was written into `../flashcards/recursion.md`
  at 22:17 on 2026-08-28 and the defect was produced at 13:58 on 2026-08-29** —
  16 hours. Reading it did not encode it. Order the two checks by asking "can
  this call be both finished and correct?" before writing either.
- Pattern: Backtracking
- Review Date: 2026-08-30

### 2026-08-29 — Combination Sum II (LC 40) — `HashSet` result set, 2nd occurrence in 2 days
- Mistake: declared `Set<List<Integer>> res` and converted to a list at the
  end, exactly as in LC 39 the day before. The duplicate paths are real —
  `[1,7]` on `[1,1,2,5,6,7,10]` is produced twice, once per copy of `1`.
- Root Cause: dedup was treated as an output-formatting step, not as evidence
  about the search. The rule "a `Set` on a backtracking result is a branching
  bug" was made the top pitfall in `../patterns/Backtracking.md` on 08-28.
- Correct Thinking: declining a value means declining **every copy** of it at
  that depth; sorting makes those copies adjacent so the skip is one
  contiguous run. `index+1` in the take branch enforces use-once; the skip
  lives only in the decline branch, so `[1,1,6]` is still reachable.
- How to Avoid: before writing `Set`, name one input where two paths build the
  same list, then cut the second path at its parent.
- Pattern: Backtracking
- Review Date: 2026-08-30

### 2026-08-29 — Written notes are not transferring; in-session derivation is (meta)
- Mistake: both defects in LC 40 had been written into the tracker the
  previous night (the `Set` pitfall in `patterns/Backtracking.md`, the base-case
  ordering in `flashcards/recursion.md`) and both were reproduced anyway. This is
  the 3rd instance of the class — LC 735 reproduced its own written-up bug
  verbatim on 2026-08-24.
- Root Cause: reading a diagnosis is recognition; producing it under load is
  recall. Only the second was ever practised.
- Correct Thinking: the counter-evidence is in the same session — skip-on-decline
  took 6 escalations plus a guided trace on LC 40, then came out **cold and
  unprompted on LC 90 five minutes later**, and the copy-cost complexity nudge
  closed inside 6 minutes. What was derived transferred; what was read did not.
- How to Avoid: the write-up is not the encoding step. Yesterday's notes must be
  re-derived as a question at the start of the next session, not re-read — this
  is what the `recall/daily.md` file exists for and it has never been run as a
  drill.
- Pattern: Process
- Review Date: 2026-08-30

### 2026-08-29 — Code before approach, twice (process)
- Mistake: asked for the approach before any code on both LC 40 and LC 90;
  both times a full implementation came back instead, and on LC 40 the
  base-case ordering bug was fixed silently after one targeted question
  without ever stating what had broken.
- Root Cause: solving is treated as done when the judge accepts. The spoken
  derivation is the graded part of an interview and it is being skipped.
- Correct Thinking: silent fix = the defect is unnamed = it recurs (see the
  16-hour flashcard recurrence above).
- How to Avoid: state the node's decision and the base case in one line before
  the first keystroke. On any fix, say what broke before saying it is fixed.
- Pattern: Process
- Review Date: 2026-08-31

### 2026-08-27 — Sum of Subarray Minimums (LC 907) — tie rule carried over from LC 84
- Mistake: reused the `nsl/nsr` code from LC 84 verbatim, popping on `<=` in
  **both** passes, so both sides found the nearest *strictly* smaller. On
  `[2,2]` the subarray `[2,2]` is claimed by both twos — 8 returned, 6 correct.
- Root Cause: the machinery transferred, the tie rule did not. Under `max`
  (LC 84) a double-claimed span changes nothing; under `sum` every double-claim
  is added twice. The difference was never checked before reuse.
- Correct Thinking: contribution counting requires the subarrays to be
  **partitioned** — each owned by exactly one element. Break ties one way:
  strict on one side, non-strict on the other (here: right pass pops on `<`),
  which credits every subarray to the leftmost occurrence of its minimum.
- How to Avoid: before reusing an `nsl/nsr` template, ask "what does the
  problem do with duplicates — max, sum, or strict comparison?" Test `[2,2]`
  (or any all-equal pair) as a mandatory case on every monotonic-stack problem.
- Pattern: [[MonotonicStack]]
- Class: template-first retrieval
- Recurrence: **2nd occurrence** (1st: LC 42, 2026-08-26). First one cost time
  only; this one produced a wrong answer.
- Review Date: 2026-08-30

### 2026-08-27 — Sum of Subarray Minimums (LC 907) — endpoint counting off-by-one
- Mistake: asked how many valid left/right endpoints index 2 has, answered
  "0, 1" — counted elements *beyond* `i` rather than endpoints *including* `i`.
- Root Cause: same inclusive-range blind spot as Stock Span; `i` itself is
  always a valid endpoint because `[i,i]` is a subarray.
- Correct Thinking: `leftSide = i - nsl` counts choices of **start**,
  `rightSide = nsr - i` counts choices of **end**; a subarray is the *pair*, so
  the count is a product. `i` appearing in both sets is not double counting.
- How to Avoid: enumerate the pairs on a 4-element array before trusting the
  formula — `[3,1,2,4]` at `i=1` gives 2x3 = 6 pairs, listable in one line.
- Pattern: [[MonotonicStack]]
- Class: inclusive-range off-by-one
- Recurrence: 3rd (Stock Span 07-21, traversal-direction 07-24, this)
- Review Date: 2026-08-30

### 2026-08-27 — Sum of Subarray Minimums (LC 907) — int overflow, mod declared unused
- Mistake: `int res` accumulating `leftSide*rightSide*arr[i]`; `mod` declared
  and never applied.
- Root Cause: constraints not converted to a magnitude before choosing types —
  `n=3e4` gives counts near `2.25e8`, times values `3e4` = `~6.75e12` vs
  `int` cap `2.147e9`. Silent wraparound, no exception.
- Correct Thinking: `long res`, `long` operands (Java keeps `int*int` as `int`
  even when assigned to `long`), mod folded in each iteration.
- How to Avoid: any problem stating "answer mod 1e9+7" is stating that the raw
  answer overflows — treat the mod as a constraint signal, not decoration.
- Pattern: [[MonotonicStack]]
- Class: overflow / constraint-to-magnitude
- Recurrence: 1st logged
- Review Date: 2026-08-30

### 2026-08-27 — Trapping Rain Water (LC 42) O(1) follow-up — derivation-to-code assembly gap
- Mistake: derived every component of the two-pointer argument cold (leftMax
  maintainable / rightMax not, the lower-bound chain, both branch conditions,
  which pointer moves), then said "I don't know how to code it up" and
  requested the code.
- Root Cause: pieces were derived as separate answers, never assembled into a
  loop body. The gap is between "I can justify each step" and "I can write the
  loop that runs them."
- Correct Thinking: the loop body is 4 lines and each one was already stated
  aloud — update both maxima, compare, settle the smaller side, move that
  pointer.
- How to Avoid: after a derivation closes, ask for the **skeleton first**
  (loop header + variables), then have them fill the body, rather than asking
  for the whole function at once.
- Pattern: [[TwoPointers]]
- Class: derivation-to-code assembly (new class)
- Recurrence: 1st logged
- Review Date: 2026-08-29

### 2026-08-27 — Java: `java.util.Stack` (Java track, first live signal in 49 days)
- Mistake: no knowledge of why `Stack` is discouraged; answered "no idea".
- Root Cause: Java Collections track has been at zero for the full cycle; this
  is trivia-by-exposure, not derivable.
- Correct Thinking: `Stack extends Vector`, so every method is `synchronized`
  (lock cost on single-threaded use); its iterator walks bottom-to-top, the
  reverse of stack semantics; the JDK javadoc itself points to `Deque`. Use
  `Deque<Integer> s = new ArrayDeque<>()` — unsynchronized, array-backed,
  rejects `null`.
- How to Avoid: this is the Java track's job, not DSA's — logged here because
  it surfaced live. Every monotonic-stack solve from here uses `ArrayDeque`.
- Pattern: n/a (Java Collections)
- Class: Java-track knowledge gap
- Recurrence: 1st
- Review Date: 2026-08-29

### 2026-08-27 — Mentor error: re-drilled a justification that was already correct
- Mistake: after the user stated LC 739's tie rule correctly ("warmer is
  strict, so equals must be popped"), the follow-up asked twice more for a
  concrete failing instance. User pushed back: "why are u irritating me".
- Root Cause: treated a stated rule as incomplete without an instance, on a
  problem that had already been solved independently and accepted.
- Correct Thinking: the rule *was* the answer. Instance-hunting is a tool for
  when the rule is missing or wrong, not a mandatory second step.
- How to Avoid: **once the justification is stated correctly, stop.** Instances
  are for unlocking, not for verifying an unlock that already happened.
- Pattern: cross-cutting (mentor protocol)
- Class: mentor error
- Recurrence: 2nd mentor error logged (1st: 2026-08-18, wrong problem statement)
- Review Date: n/a

### 2026-08-27 — Two cold justifications in one session (meta, positive)
- Mistake: none — logged as continuing counter-evidence to the silent-fix streak.
- Root Cause: n/a. LC 84's "taller bars can be cut down to h[i], shorter ones
  can't" and LC 739's strictness argument both came unprompted, first ask.
- Correct Thinking: n/a — 2nd and 3rd cold justifications in two sessions,
  after a 7-problem streak where the *why* always needed the ladder.
- How to Avoid: n/a — the pattern to watch is that both came on problems whose
  mechanism is **physical/visual** (bars, temperatures). LC 907's abstract
  counting is where it still needed enumeration.
- Pattern: cross-cutting (method)
- Class: justification-weakness countermeasure
- Recurrence: 3rd consecutive session with a cold *why*
- Review Date: n/a

### 2026-08-06 — Job Sequencing Problem (GFG)
- Mistake: two independent wrong choices before landing the correct
  approach: (1) proposed sorting jobs by deadline ascending (tie-break
  profit descending) instead of profit descending; (2) proposed placing
  each job in the earliest available slot ≤ deadline instead of the latest
  available slot.
- Root Cause: (1) optimized for the wrong objective — deadline order has
  nothing to do with maximizing profit, only proximity does; (2) reasoned
  "process ASAP" as a generic scheduling instinct without checking it
  against the actual goal (preserving flexibility for jobs with less of it).
- Correct Thinking: sort jobs by profit descending; for each, place in the
  latest available slot ≤ its deadline (skip if none free) — this lets
  higher-profit jobs claim contested slots first, and placing late leaves
  earlier slots open for jobs with tighter deadlines.
- How to Avoid: for greedy slot/resource-assignment problems, ask "what
  does the objective actually optimize for" before picking a sort key —
  then ask "does my placement choice burn a resource another candidate
  needs more" before defaulting to first-available.
- Pattern: SlotAssignmentGreedy — first exposure, both wrong turns closed
  via constructed counterexamples (A/B/C deadline-tie trace; C/A slot-
  direction trace), see `../patterns/SlotAssignmentGreedy.md`.
- Class: transfer-gap
- Recurrence: 1
- Review Date: 2026-08-07

### 2026-08-06 — Jump Game (LC 55)
- Mistake: initial "why greedy works" answer restated the goal ("reach the
  end faster, not count ways") rather than giving the actual mechanism.
- Root Cause: hadn't isolated the dominance argument (a bigger reach is
  always a superset of what a smaller reach can do) as the reason branching
  is unnecessary.
- Correct Thinking: for any two paths reaching index i, only the larger
  resulting reach matters — it dominates the smaller one, so collapsing
  every path into a single running max loses no information.
- How to Avoid: for "why is greedy sufficient" questions, name the
  dominance relation (does option A's outcome fully contain option B's)
  rather than restating the objective.
- Pattern: MaxReachGreedy — first exposure, see `../patterns/MaxReachGreedy.md`.
- Class: invariant-why
- Recurrence: 1
- Review Date: 2026-08-07

## Entry Format

```
### YYYY-MM-DD — Problem Name
- Mistake:
- Root Cause:
- Correct Thinking:
- How to Avoid:
- Pattern:
- Class: boundary | invariant-why | stale-recall | transfer-gap | code-vs-derivation
- Recurrence: 1 | 2 | 3+ (of <first entry's problem name/slug>, if this exact
  point has come up before — otherwise 1)
- Review Date:
```

`Class`/`Recurrence` added 2026-07-25 (audit finding: recurrence was only
findable by reading prose like "3rd time" — unsearchable at volume). Added
**going forward only** — existing entries below aren't retrofitted, that's a
one-time cost not worth paying; `grep 'Recurrence: 3'` becomes a real
standing-weakness query once enough new entries carry the field. Classes are
the five buckets this journal's entries already cluster into (memorized-
without-why, boundary/post-loop misses, stale-recall on old topics, pattern
not transferring to a new context, and code contradicting a correct verbal
derivation) — add a new class only if an entry genuinely doesn't fit any of
these five, don't invent one per entry.

## Log

### 2026-08-05 — N Meetings in One Room
- Mistake: could not justify "why sort by end time" unprompted — first answer
  ("earliest end considered first") was circular, restated the rule instead
  of explaining it. Same gap on the follow-up ("why not duration") — flat
  "no idea."
- Root Cause: mechanics (sort by end, compare against last-picked end) were
  solid and correct from the first attempt; the *why* (freeing the room
  soonest maximizes remaining options) was never derived, only pattern-
  matched from having seen the technique before.
- Correct Thinking: constructed counterexamples closed both — start-sort:
  A=(1,10),B=(2,3),C=(5,7) gives 1 vs end-sort's 2; duration-sort:
  Z=(4,5)dur1,P=(0,3)dur3,Q=(6,10)dur4 gives 2 vs end-sort's 3. Landed on
  "end-time frees the room soonest, the other two orderings don't track that."
- How to Avoid: when a greedy ordering choice feels automatic, force the
  "what if I sorted by X instead" counterexample before trusting the
  mechanics-only recall.
- Pattern: IntervalGreedy (sort-by-end-time family — Task Scheduler, Merge
  Intervals, Non-overlapping Intervals will reuse this justification)
- Class: invariant-why
- Recurrence: 1 (same class as Kruskal's cut-property escalation 2026-08-01
  and Bipartite's odd-cycle escalation 2026-07-25 — "why does the greedy/
  invariant choice work" is a recurring weak spot across topics, watch for
  a 3rd hit on this specific interval-greedy point)
- Review Date: 2026-08-06

### 2026-08-05 — Minimum Number of Platforms
- Mistake: guessed closed-form counts twice (`n/2`, then `(n+1)/2`) for the
  fully-chained edge case instead of tracing the counter step by step.
- Root Cause: reflexive formula-guessing when asked "what happens in this
  case" — same session-conduct pattern flagged 2026-08-02 (answers the
  question by pattern-matching to a plausible-looking formula instead of
  deriving/tracing first).
- Correct Thinking: forced step-by-step trace of a 3-train chain
  `(1,5),(5,9),(9,13)` — counter sequence 1,2,1,2,1,0 — landed max=2.
- How to Avoid: when asked "what's the count/result in this case," trace it
  before naming a formula.
- Pattern: MergeIntervals (interval-counting sweep)
- Class: invariant-why
- Recurrence: 1 (this exact point) — but the formula-before-trace habit
  itself is a repeat of the 2026-08-02 session-conduct signal, watch for it
  independent of topic
- Review Date: 2026-08-06
- **Open, unresolved**: the generalizing question ("why does chaining more
  trains never push the count past 2, regardless of n") was posed and the
  session ended before an answer — resume there next session first, don't
  re-run the trace, only the generalization is missing.

### 2026-07-25 — Rotten Oranges
- Mistake: minute-counter increment rule wrong, 3 iterations to fix —
  "every level" overcounted on zero-fresh cases, a queue-size-vs-total-cells
  patch only covered the all-rotten case, "queue size > 1" broke on
  exactly-1-fresh cases.
- Root Cause: treated "a BFS level happened" as the trigger instead of "did
  this level actually convert something" — conflated loop iteration with
  real state change.
- Correct Thinking: increment the counter only if at least one node was
  pushed during that level's processing.
- How to Avoid: for any "count steps/levels" BFS, gate the counter on
  observed work done this level, not on the loop structure itself — test
  the zero-work and one-work edge cases explicitly.
- Pattern: Multi-source BFS
- Review Date: 2026-07-26

### 2026-07-25 — DFS Traversal of Graph
- Mistake: proposed marking a node `visited` on recursion-exit instead of
  recursion-entry.
- Root Cause: first exposure to graph cycles — tree-traversal intuition
  (order of operations doesn't matter for acyclic structures) didn't
  transfer.
- Correct Thinking: mark visited as the first statement inside the
  recursive call, before recursing into neighbors — else a cycle re-enters
  an in-progress node.
- How to Avoid: for any graph traversal, ask "can this node be reached again
  before I've marked it?" before deciding when to mark.
- Pattern: Graph Traversal (BFS/DFS)
- Review Date: 2026-07-26

### 2026-07-25 — BFS Traversal of Graph
- Mistake: first code draft marked `visited` on dequeue and pushed neighbors
  without a visited check — contradicted own verbal derivation (mark at
  enqueue time).
- Root Cause: verbal derivation didn't automatically transfer to code;
  defaulted to a naive queue-processing shape.
- Correct Thinking: check+set `visited` at push time, not pop time, so a
  node already in the queue is never enqueued twice.
- How to Avoid: after deriving an invariant verbally, explicitly re-check
  the written code line-by-line against it before treating it as done.
- Pattern: Graph Traversal (BFS/DFS)
- Review Date: 2026-07-26

### 2026-07-10 — Frog Jump (DP-3)
- Mistake: First recurrence attempt was pure Fibonacci (`dp[i]=dp[i-1]+dp[i-2]`),
  ignored `height[]` and the `|height[i]-height[j]|` cost entirely.
- Root Cause: Pattern-matched to Climbing Stairs' recurrence shape from memory
  instead of re-deriving from this problem's actual cost function — real rust
  from 2-3 months without practice, not a first-time gap.
- Correct Thinking: `dp[i]` = min cost to reach step i. Transitions from i-1 and
  i-2 each carry a cost `|height[i]-height[prev]|`, so
  `dp[i] = min(dp[i-1]+|h[i]-h[i-1]|, dp[i-2]+|h[i]-h[i-2]|)`, with
  `dp[0]=0`, `dp[1]=|h[1]-h[0]|+dp[0]`.
- How to Avoid: When a DP recurrence looks structurally like a memorized problem,
  explicitly check whether every input array/cost term in the current problem
  is used in the recurrence before trusting it.
- Pattern: 1D DP (DP-3 family) — corrected after one hint pointing out the unused
  height array.
- Review Date: 2026-07-11

### 2026-07-11 — Frog Jump (DP-3), review #1
- Mistake: Two-jump term of the recurrence reused the one-jump term's height
  diff (`height[i-1]-height[i-2]` twice) instead of `height[i-1]-height[i-3]`;
  separately, missed that `dp[2]` needs its own base case — the general
  recurrence for `i=2` references `dp[0]` and `height[-1]`, neither valid.
- Root Cause: Re-derived the recurrence from partial memory rather than
  checking each term's index bounds against the smallest valid `i`.
- Correct Thinking: `dp[1]=0`, `dp[2]=dp[1]+|height[1]-height[0]|` as explicit
  base cases; general recurrence
  `dp[i]=min(dp[i-1]+|h[i-1]-h[i-2]|, dp[i-2]+|h[i-1]-h[i-3]|)` only valid for
  `i>=3`.
- How to Avoid: When writing a DP recurrence with `i-2`/`i-3` offsets, check the
  smallest loop-start `i` against every offset used — if any offset goes
  negative/out of bounds, that index needs a base case, not the general formula.
- Pattern: 1D DP (DP-3 family) — base-case boundary check.
- Review Date: 2026-07-14

### 2026-07-11 — Second Largest Element in Array
- Mistake: Guessed (before tracing) that a duplicate of the max value would
  incorrectly get assigned into `secondLargest`.
- Root Cause: Answered from intuition instead of tracing the exact
  comparison logic against a concrete duplicate-containing example.
- Correct Thinking: With `arr[i] > largest` and
  `arr[i] < largest && arr[i] > secondLargest` as the two update conditions, a
  value equal to `largest` fails both checks and is correctly skipped.
- How to Avoid: On comparison-heavy edge cases (duplicates, boundaries), trace
  the actual conditions against a concrete array before answering — don't guess.
- Pattern: Arrays — single-pass tracking with two running variables.
- Review Date: 2026-07-12

### 2026-07-11 — Remove Duplicates from Sorted Array
- Mistake: Default two-pointer instinct compared `arr[j]` against `arr[j+1]`
  (current vs next), which requires a special-case for the last array element.
- Root Cause: Didn't consider the cleaner invariant of comparing against the
  last-confirmed-unique element (`arr[i]`) instead of the next element.
- Correct Thinking: `i` = last unique position, `j` = scanner; compare
  `arr[i]` vs `arr[j]`, loop `j` fully through the array with no special case
  needed for the last element.
- How to Avoid: For two-pointer "keep unique/valid elements" problems, default
  to comparing the scanner against the last-confirmed-good pointer, not against
  the next element — generalizes cleanly and avoids off-by-one boundary cases.
- Pattern: Arrays — two-pointer in-place compaction.
- Review Date: 2026-07-12

### 2026-07-12 — Rotate Array (O(1) space)
- Mistake: No idea how to rotate in-place without extra array; fully stuck on
  the reversal-algorithm trick.
- Root Cause: Never encountered the "reverse both chunks, then reverse whole
  array" pattern before — genuine new-material gap, not rust.
- Correct Thinking: Whole-array reverse of `A+B` gives `reverse(B)+reverse(A)`
  (swaps chunk order AND flips internal order). Pre-reversing each chunk first
  cancels the unwanted internal flip, leaving just the chunk swap.
- How to Avoid: Recognize "rotate array" as a named pattern → reversal trick,
  same tier as two-pointer/sliding window. Memorize the 3-reversal recipe.
- Pattern: Arrays — reversal algorithm (block swap via double reversal).
- Review Date: 2026-07-13

### 2026-07-12 — Union of Two Sorted Arrays
- Mistake: Initial approach was a plain sorted-merge, didn't account for
  duplicates (across or within arrays) — "union" requires distinct elements.
- Root Cause: Defaulted to the more familiar merge-two-sorted-arrays pattern
  without checking the problem's actual postcondition (distinctness).
- Correct Thinking: Compare the smaller candidate against the last element
  already placed in the result; skip if equal, append otherwise. Handles both
  within-array and cross-array duplicates for free.
- How to Avoid: Before reusing a merge pattern, check if the target problem
  wants distinct values, not just sorted order.
- Pattern: Arrays — merge with a last-inserted dedup check.
- Review Date: 2026-07-13

### 2026-07-12 — Max Consecutive Ones
- Mistake: Sliding-window (start/end pointer) approach never captured the max
  run if the array's last run of 1s reaches the end without hitting a 0.
- Root Cause: Only saved the running max on the "reset" trigger (hitting a 0),
  missed that the loop can end without ever triggering a reset.
- Correct Thinking: Add an explicit post-loop check for the final window, or
  avoid the issue entirely with a single running counter (reset to 0 on 0,
  `max=max(max,counter)` every iteration, no post-loop step needed).
- How to Avoid: Standing checklist item now — for any window/run-tracking
  loop, explicitly ask "what happens to the last window when the loop ends
  without a reset trigger." 3rd occurrence of a boundary/tail miss this
  session (after Remove Duplicates, Move Zeroes) — confirmed recurring
  pattern, not one-off.
- Pattern: Arrays — window/run tracking, missing post-loop finalization.
- Review Date: 2026-07-13

### 2026-07-12 — Longest Subarray with Sum K (negatives allowed)
- Mistake: Proposed variable-size sliding window (shrink when sum>k) without
  checking whether it holds for arrays with negative numbers; when pushed,
  proposed a Kadane's-style "restart window on sum<0" fix, which is wrong for
  this problem (exact-sum-k, not max-subarray-sum).
- Root Cause: Sliding window relies on sum growing monotonically as the window
  expands — true only for non-negative arrays. Didn't know the general-case
  fallback (prefix sum + hashmap) at all; needed full derivation.
- Correct Thinking: `sum(i+1..j) = prefixSum[j] - prefixSum[i]`. Want this
  equal to k → `prefixSum[i] = prefixSum[j] - k`. Scan left to right, maintain
  `{prefixSum value -> earliest index}` map; at each j, look up
  `prefixSum[j]-k`; if found at i, candidate length `j-i`. Insert
  `prefixSum[j]->j` only if not already present (earliest index maximizes
  length). O(n) time/space, works with negatives.
- How to Avoid: Before defaulting to sliding window on a sum-target problem,
  explicitly check "does this array allow negatives" — if yes, go straight to
  prefix-sum + hashmap.
- Pattern: Arrays — prefix sum + hashmap for exact-target subarray sum.
- Review Date: 2026-07-13

### 2026-07-12 — Two Sum
- Mistake: Proposed storing a list of indices per value to handle duplicates,
  unnecessary for classic Two Sum (only one valid pair needed).
- Root Cause: Over-engineered before checking whether the simpler single-index
  hashmap already handles the duplicate case correctly.
- Correct Thinking: Check-before-insert with a single index per value is
  sufficient — self-verified correct on `[3,3]`, target `6`.
- How to Avoid: Before adding complexity for an edge case, test whether the
  simpler version already handles it.
- Pattern: Arrays — hashmap complement lookup, avoid premature complexity.
- Review Date: 2026-07-13

### 2026-07-12 — Sort Array of 0s, 1s, 2s (Dutch National Flag)
- Mistake: Initially treated the 0-swap and 2-swap cases as symmetric (neither
  advancing `mid`), missing that they're not. Deeper issue: no understanding
  of *why* the `[low, mid-1]` region is guaranteed all 1s — induction framing
  didn't land, needed an elimination argument instead.
- Root Cause: Never built the invariant intuition from first principles;
  pattern-recalled the pointer roles without understanding why they hold.
- Correct Thinking: 0-swap brings a *known* 1 into `mid` (since `arr[low]` is
  always the front of the already-confirmed 1-zone), so `mid` safely advances
  too. 2-swap brings an *unknown* value from the unprocessed region, so `mid`
  must not advance. Why the middle zone is all 1s: every examined index is
  either shipped to the 0-zone (via swap with `low`) or the 2-zone (via swap
  with `high`) the instant it's classified — nothing else is ever relocated.
  Whatever's left behind, unrelocated, in `[low,mid-1]` can only be 1, by
  elimination.
- How to Avoid: For 3-way partition invariants, explain them via elimination
  (what's NOT true about the leftover region) if induction framing doesn't
  land — sometimes the elimination angle is more intuitive than induction.
- Pattern: Arrays — 3-pointer partition (Dutch National Flag), invariant
  reasoning by elimination.
- Review Date: 2026-07-13

### 2026-07-12 — Kadane's Maximum Subarray Sum
- Mistake: Reset-based approach ("reset running sum to 0 when it goes
  negative") lost the max value on all-negative arrays — never recorded a
  candidate max before the premature reset threw the info away.
- Root Cause: Only updated `max` at reset time, not every iteration; a
  losing (negative) running sum never got a chance to be captured.
- Correct Thinking: `sum += x; max = max(max, sum); if sum<0: sum=0` — record
  max using the sum that includes the current element, before resetting.
- How to Avoid: For any "reset on losing condition" accumulator pattern,
  record the best-so-far using the value *before* the reset, not after.
- Pattern: Arrays — Kadane's, all-negative edge case.
- Review Date: 2026-07-13

### 2026-07-12 — Next Permutation
- Mistake: Initial approach found *a* pivot swap that produced a greater
  permutation, but not the smallest one — missing two pieces: swap with the
  smallest element greater than the pivot (not just any greater element),
  and reverse the suffix after swapping.
- Root Cause: Never encountered this specific pattern before — genuine
  new-material gap, needed full derivation of both missing pieces plus a
  concrete trace to verify.
- Correct Thinking: Find largest `i` where `arr[i]<arr[i+1]` (pivot). Find
  largest `j>i` where `arr[j]>arr[i]` (suffix is descending, so scanning
  from the right finds the smallest-greater element first). Swap `i,j`.
  Reverse suffix `[i+1..end]`. If no pivot exists, reverse whole array.
- How to Avoid: Recognize as a named pattern (next-permutation via
  pivot+smallest-successor+suffix-reverse), same tier as reversal-algorithm.
- Pattern: Arrays — next permutation (pivot/successor/suffix-reverse).
- Review Date: 2026-07-13

### 2026-07-12 — Longest Consecutive Sequence
- Mistake: Initial hash-set approach expanded left+right from *every*
  element, which is O(n²) worst case, not O(n) — initially misjudged it as
  amortized O(n). Also got confused about whether skipping non-start
  elements would lose count if array order processed them before their
  sequence's true start.
- Root Cause: Didn't know the "only expand from sequence starts" pruning
  rule; separately, conflated "processing order in the loop" with "hash set
  build order" — the set is built fully upfront, so membership checks are
  order-independent even though the outer loop still visits every element.
- Correct Thinking: Build the hash set from the whole array first. Then for
  each element `x`, only expand rightward if `x-1` is not in the set (i.e.
  `x` is a true sequence start). Every element is visited in exactly one
  expansion across the whole run, giving true O(n).
- How to Avoid: For "expand from every element" approaches, explicitly check
  for a start/dedup condition before trusting the complexity is linear.
- Pattern: Arrays — hash set, sequence-start pruning for true O(n).
- Review Date: 2026-07-13

### 2026-07-12 — Set Matrix Zeroes
- Mistake: Correctly proposed using first row/col as O(1)-space markers, but
  missed that cell `(0,0)` is shared between the row-0 marker and col-0
  marker, causing ambiguity about whether row 0 or col 0 itself needs
  zeroing.
- Root Cause: Didn't pre-check row 0 / col 0 for their own zeroes before
  overwriting them as markers for the rest of the matrix.
- Correct Thinking: Store `row0Flag`/`col0Flag` (row 0 / col 0 originally
  have a zero) in separate booleans first. Use rest of row 0/col 0 as
  markers for inner cells. Zero the inner matrix using markers, THEN zero
  row 0/col 0 using the flags (order matters — flags must be read before
  being overwritten).
- How to Avoid: When reusing part of the input as scratch space, check for
  self-conflicts (shared cells serving double duty) before overwriting.
- Pattern: Arrays/Matrix — in-place marker reuse, shared-cell conflict.
- Review Date: 2026-07-13

### 2026-07-12 — Rotate Matrix (90°, in-place)
- Mistake: No idea how to rotate in-place; fully stuck on the transpose +
  reverse-rows trick.
- Root Cause: Never encountered this specific decomposition before — genuine
  new-material gap, needed a concrete worked example to see the pattern.
- Correct Thinking: Transpose (`arr[i][j] <-> arr[j][i]` for `i<j`), then
  reverse each row. Transpose alone gives columns-as-rows; reversing each
  row then produces the 90° clockwise result.
- How to Avoid: Recognize as a named 2-step decomposition pattern.
- Pattern: Arrays/Matrix — rotate via transpose + row-reverse.
- Review Date: 2026-07-13

### 2026-07-13 — Spiral Traversal
- Mistake: Had the right high-level shape (4 boundary pointers, print ring,
  shrink) but no idea what the outer `while` continue-condition was, nor that
  the 3rd/4th passes (bottom-row, left-col) need their own guards.
- Root Cause: Never derived why a single-row/single-column collapsed box
  causes duplicate prints unless the later passes are explicitly guarded.
- Correct Thinking: Remaining cells = `(bottom-top+1)*(right-left+1)` — a
  product, zero if either factor collapses. So outer loop needs
  `top<=bottom && left<=right` (AND, not OR — either dimension collapsing
  means zero cells regardless of the other). Passes 3/4 additionally need
  `top<=bottom` / `left<=right` guards respectively, since a single
  remaining row/column already got fully printed by pass 1/2 and would
  otherwise be printed again by pass 3/4.
- How to Avoid: For shrinking-box/ring problems, frame the stop condition as
  "remaining area = product of two ranges," not two independent checks —
  makes the AND obvious and flags where per-pass guards are needed.
- Pattern: Arrays/Matrix — boundary-shrinking traversal, collapsed-dimension
  guard.
- Review Date: 2026-07-14

### 2026-07-13 — Rotate Matrix (90°), review #1
- Mistake: Same gap as the original 2026-07-12 solve — forgot that transpose
  must be followed by a *full* row reverse, initially said "swap first and
  last column" (only fixes the two end columns, leaves middle untouched).
- Root Cause: The transpose+reverse-rows decomposition hasn't actually stuck
  yet — this is the 2nd time the same specific piece (full reverse, not
  partial) was missing.
- Correct Thinking: After transpose, each row must be fully reversed
  end-to-end (e.g. `[1,2,3,4]` -> `[4,3,2,1]`), not just have its two
  endpoints swapped.
- How to Avoid: Standing gap — explicitly rehearse "transpose, THEN reverse
  each row completely" as a fixed phrase before attempting this problem next
  time, don't rely on partial recall.
- Pattern: Arrays/Matrix — rotate via transpose + full row-reverse, repeat
  rust (2nd occurrence).
- Review Date: 2026-07-16

### 2026-07-13 — Subarray Sum Equals K
- Mistake: First proposed sliding-window ("at most K" / "at most K-1" trick)
  despite the array allowing negatives — same trap as Longest Subarray with
  Sum K one day earlier, initially didn't connect the two.
- Root Cause: Didn't spontaneously apply own "check negatives before
  sliding window" rule until prompted to recall it.
- Correct Thinking: Prefix-sum + hashmap, but storing **count** of each
  prefix sum seen (not first index) since this problem counts subarrays, not
  max length. Seed `{0:1}`. Look up `sum-k` before inserting current sum
  (avoids counting a spurious zero-length self-match when k=0).
- How to Avoid: The negative-number check needs to become an automatic first
  step on any sum-target array problem, not something recalled only when
  pointed at the mistake log — 2nd occurrence of the same trap in 2 days.
- Pattern: Arrays — prefix sum + count-hashmap for subarray-count-equals-k;
  same negative-number check as Longest Subarray Sum K, but count vs index.
- Review Date: 2026-07-14

### 2026-07-17 — Second Largest Element in an Array, review #2
- Mistake: Initialized both `max`/`secondMax` to sentinel `-1`; for arrays
  with negative numbers (e.g. `[-1,-2]`), `-1` collides with real data and
  elements equal to it get silently skipped, corrupting the result.
- Root Cause: Sentinel choice wasn't guaranteed collision-free with the
  input range.
- Correct Thinking: Use `Integer.MIN_VALUE` as sentinel, not an arbitrary
  small number.
- How to Avoid: Any sentinel init value must be provably impossible for real
  input, not just "small enough" — default to MIN_VALUE/MAX_VALUE unless the
  input range is explicitly bounded away from it.
- Pattern: Arrays — single-pass tracking, sentinel initialization.
- Review Date: 2026-07-20

### 2026-07-17 — Rotate Array, review #2
- Mistake: Split the reversal chunks at index `k` (first k, last n-k)
  instead of `n-k` (first n-k, last k) for a right-rotation by k.
- Root Cause: Reversed which chunk size maps to which rotation direction.
- Correct Thinking: Right-rotate-by-k: first chunk = first (n-k) elements,
  second chunk = last k elements; reverse each, then reverse whole array.
- How to Avoid: Verify split boundary with a concrete small trace before
  trusting it — left/right rotation swaps which chunk is which size.
- Pattern: Arrays — reversal algorithm, split-boundary direction.
- Review Date: 2026-07-20

### 2026-07-17 — Longest Subarray with Sum K, review #2
- Mistake: Used the correct seed `{0:-1}` but couldn't initially explain why
  the value is `-1` rather than `0`.
- Root Cause: Memorized the seed without deriving it from the length
  formula.
- Correct Thinking: `length = i - map[sum-k]`; for a prefix summing to k
  from index 0, the formula needs `map[0]=-1` so `i-(-1)=i+1`, the correct
  full length.
- How to Avoid: For any hashmap-seed trick, be able to derive the seed value
  from the formula, not just recall it as a fact.
- Pattern: Arrays — prefix sum + hashmap, seed-value derivation.
- Review Date: 2026-07-20

### 2026-07-17 — Stock Buy and Sell, review #2
- Mistake: Proposed returning `-1` for a strictly-decreasing (no-profit)
  array, reverting from the previously-established `maxProfit=0` insight.
- Root Cause: Lost the "profit of doing nothing = 0, not -1" framing between
  sessions.
- Correct Thinking: `maxProfit` inits to 0 (profit of not transacting),
  already correct when no profitable trade exists — no special `-1` case.
- How to Avoid: Re-anchor on "what does doing nothing return" whenever an
  edge-case return value is in doubt.
- Pattern: Arrays — running min/max tracking, floor-value regression.
- Review Date: 2026-07-20

### 2026-07-17 — Next Permutation, review #2
- Mistake: Two errors: (1) initially misidentified the pivot index (picked
  the larger-value index instead of `i` where `arr[i]<arr[i+1]`); (2) stated
  the swap-partner condition as "greater than or equal to" instead of
  strictly greater, which breaks on duplicates (e.g. `[1,2,1]` would wrongly
  become `[1,1,2]` instead of `[2,1,1]`).
- Root Cause: Both pieces of the original hard-won derivation had decayed
  since review #1.
- Correct Thinking: Pivot = largest `i` with `arr[i]<arr[i+1]`. Swap partner
  = rightmost `j>i` with `arr[j]` STRICTLY greater than `arr[i]` — an
  equal-value swap is a no-op, doesn't advance to the next permutation.
- How to Avoid: This problem has two independent hard-to-retain pieces —
  rehearse both explicitly rather than assuming "I remember the general
  shape" is enough.
- Pattern: Arrays — next permutation, full derivation regression across two
  sub-pieces.
- Review Date: 2026-07-20

### 2026-07-17 — Rotate Matrix (90°), review #2
- Mistake: During transpose, swapped diagonal elements `arr[0][0]` and
  `arr[2][2]` with each other (diagonal elements have `i==j` and shouldn't
  move at all). Note: the original standing bug (partial row-reverse) did
  NOT recur this time.
- Root Cause: Applied the swap operation to a diagonal position without
  checking that `i==j` makes it a no-op.
- Correct Thinking: Transpose only swaps `arr[i][j]` with `arr[j][i]` for
  `i != j`; diagonal elements stay fixed.
- How to Avoid: When transposing, explicitly skip/no-op the diagonal case
  rather than blindly applying the swap to every cell.
- Pattern: Arrays/Matrix — transpose, diagonal no-op check (distinct from
  the prior row-reverse bug, which held clean this time).
- Review Date: 2026-07-20

### 2026-07-17 — Print Subarray with Maximum Sum — RESOLVED 2026-07-20
- Mistake: Kadane's-based approach tracked the running max sum correctly but
  collapsed the recorded start/end pointers to the *current single index*
  every time a new max was found — didn't maintain a separate
  window-start pointer that persists across a growing (non-reset) window.
- Root Cause: Conflated "the index where a new max was noticed" with "the
  index where the winning window actually began."
- Correct Thinking: two pointers — `tempStart` (current running window's
  start, only moves on a sum<0 reset) and `start`/`end` (best window found so
  far). On `sum<0` reset: `tempStart = i+1`. On new max (`sum>maxSum`):
  `start=tempStart`, `end=i` — NOT `start=end=i`. `end` is simply `i` every
  time; `start` copies `tempStart`, never the current index. Resolved via
  full guided trace on `[-2,1,-3,4,-1,2,1,-5,4]` (max=6, start=3, end=6,
  subarray `[4,-1,2,1]`), then self-written and self-verified working code.
- How to Avoid: For "track best window, not just best value" problems,
  separate the *current window's* start pointer from the *best window's*
  start pointer explicitly — they update on different triggers (reset vs.
  new-max).
- Pattern: Arrays — Kadane's variant, dual-pointer (running-window-start vs
  best-window-start) tracking.
- Review Date: 2026-07-21

### 2026-07-20 — Spiral Traversal, review #2
- Mistake: Three errors: (1) used `top<=bottom` as the guard for pass 3
  (bottom row) instead of `left<=right`; (2) said `bottom++` after the
  bottom-row pass instead of `bottom--`; (3) initial restate swapped pass
  3/4 directions (said pass 3 goes "bottom to top", pass 4 "left to right").
- Root Cause: Same guard-confusion area flagged 2026-07-13 (per-pass
  guards) resurfaced — not internalized from the first correction.
- Correct Thinking: Guards alternate by which dimension the *previous* pass
  shrank — pass 2 guards `top<=bottom` (pass1 shrank rows), pass 3 guards
  `left<=right` (pass2 shrank columns), pass 4 guards `top<=bottom` again
  (pass3 shrank rows). Boundaries always shrink toward the center
  (`bottom--`, `left++`, etc.), never grow.
- How to Avoid: Rehearse the guard-alternation rule explicitly ("guard
  checks the dimension the PREVIOUS pass just shrank") rather than
  recalling which specific comparison goes where — 2nd occurrence of this
  gap, standing weak spot.
- Pattern: Arrays/Matrix — boundary-shrinking traversal, per-pass guard
  alternation, repeat rust (2nd occurrence).
- Review Date: 2026-07-27

### 2026-07-20 — Subarray Sum Equals K, review #2
- Mistake: Conflated the lookup step and the insert step — proposed adding
  `+1` to the count found via `map[runningSum-k]` lookup before adding to
  the answer (e.g. treated a found count of 3 as 3+1=4).
- Root Cause: The `+1` belongs only to the map's *insert* operation
  (`map[runningSum] = count+1`) and the one-time seed (`{0:1}`) — mixed it
  into the *lookup* operation, which should add the found count as-is.
- Correct Thinking: Two separate operations per index: (1) lookup
  `runningSum-k`, add whatever count is found to `answer`, no `+1`; (2)
  insert/increment `runningSum` itself in the map, `+1` happens here only.
  Verified via trace on `[0,0,0]`, k=0 (expected 6 subarrays) — using the
  raw found count at each step gives 1+2+3=6, correct; a spurious +1 at
  lookup would have given 7, wrong.
- How to Avoid: Keep "read from map" and "write to map" as clearly separate
  steps mentally — the `+1` is a write-side detail, never bleeds into the
  read side.
- Pattern: Arrays — prefix sum + count-hashmap, lookup-vs-insert
  conflation.
- Review Date: 2026-07-27

### 2026-07-20 — Next Greater Element
- Mistake: Correct monotonic-stack approach and full trace derived cold, but
  first code attempt overwrote `nums[i]` with the computed answer before
  pushing it onto the stack — stack ended up holding answers, not original
  array values, corrupting later comparisons.
- Root Cause: Reused the input array as both the output and the stack's
  source of truth without separating the two roles.
- Correct Thinking: Use a separate output array (`nge[i]`); push the original
  `nums[i]` onto the stack, never the computed answer.
- How to Avoid: When a loop both reads from and writes an answer into the
  same array, check whether a later iteration still needs the original
  (unwritten) value — if yes, use a separate output array.
- Pattern: [[MonotonicStack]] (`../patterns/MonotonicStack.md`) — Stack/Queue,
  first new-topic problem.
- Review Date: 2026-07-21

### 2026-07-20 — Implement Queue using Two Stacks
- Mistake: Could not initially explain why amortized complexity per operation
  is O(1) despite a single dequeue potentially costing O(n) (full transfer).
- Root Cause: No mental model for "amortized" beyond the term — needed
  Socratic escalation (restate → concrete 3-element trace → count total ops
  per element → generalize to n) before connecting "≤3 ops per element,
  ever" to "O(1) per operation, spread over n operations."
- Correct Thinking: Each element is pushed once, transferred at most once,
  popped once — ≤3 total ops across its entire lifetime (fewer if never
  dequeued/transferred). n elements → ≤3n total ops however they're
  distributed across dequeue calls → O(1) amortized per operation, even
  though any single call can spike to O(n).
- How to Avoid: For amortized-complexity questions, default to "count total
  work per element across its whole lifetime, then divide by number of
  operations" rather than reasoning about worst-case single calls.
- Topic Area: Stack/Queue — lazy-transfer two-stack queue, amortized analysis.
- Review Date: 2026-07-21

### 2026-07-11 — Move Zeroes to End
- Mistake: Initial two-pointer plan only accounted for copying non-zero
  elements forward, didn't account for what's left in the trailing positions.
- Root Cause: Reused the remove-duplicates overwrite pattern without checking
  whether this problem's postcondition (trailing zeroes, not just compacted
  front) needed something extra.
- Correct Thinking: Either two-pass (copy non-zeroes forward, then zero out
  `i..n-1`), or one-pass with swap instead of overwrite (`arr[i]` is guaranteed
  0 at swap time).
- How to Avoid: Before reusing a two-pointer pattern from a prior problem,
  check the postcondition on the *rest* of the array, not just the front
  compacted region.
- Pattern: Arrays — two-pointer in-place partition (zero/non-zero).
- Review Date: 2026-07-12

### 2026-07-21 — Nearest Smaller to the Left
- Mistake: Got the concrete mechanics right quickly (left-to-right traversal,
  pop-while-top->=current including ties), but when asked to generalize
  "why does traversal direction flip between problems" and "state the rule
  for any nearest-X-in-direction-Y problem," gave circular answers twice
  ("we look left because we want left") instead of the actual mechanism.
- Root Cause: Had the specific instances (NGE right-to-left, this problem
  left-to-right) correctly intuited but hadn't abstracted *why* — needed
  guided questions (what indices are in the stack at index i, for each
  problem) before connecting it to a transferable rule.
- Correct Thinking: For "nearest X in direction Y," start traversal from the
  end matching side Y (so elements on that side are already pushed onto the
  stack by the time you reach index i) — traversal-start-side = query-side.
  Pop while the top fails the "X" comparison against current, using >=/<=
  (not strict) so equal-valued ties are excluded, since "greater"/"smaller"
  are strict relations.
- How to Avoid: When a new monotonic-stack variant is solved correctly,
  explicitly state the general rule (direction + pop condition) out loud
  before moving on — don't let "got this instance right" substitute for
  "can derive the next instance cold."
- Pattern: [[MonotonicStack]] (`../patterns/MonotonicStack.md`) — direction-
  of-traversal generalization, second problem in this pattern.
- Review Date: 2026-07-22

### 2026-07-21 — Stock Span Problem
- Mistake: Correctly identified the core relationship (span = everything
  between the nearest-greater-left index and current index, since those
  values are all <= current), but the formula was off by one:
  `span = curIndex - ngeIndex - 1` instead of `curIndex - ngeIndex`.
- Root Cause: Didn't derive the formula from first principles (inclusive
  range counting) — guessed at the arithmetic directly and got a spurious
  extra `-1`. Also needed a definitional reminder that "today" (curIndex)
  is always included in its own span per the problem statement.
- Correct Thinking: span covers indices `ngeIndex+1` through `curIndex`
  inclusive. Count of an inclusive range `[a,b]` is `b-a+1`; substituting
  `a=ngeIndex+1, b=curIndex` gives `curIndex-(ngeIndex+1)+1 = curIndex-ngeIndex`.
  Verified on `[5,10]` at i=1 (no NGE, ngeIndex=-1): `1-(-1)=2`, correct —
  also confirms the -1 sentinel needs no special-casing.
- How to Avoid: When a formula involves an index difference for an inclusive
  range, explicitly derive it via `b-a+1` rather than guessing the offset —
  don't trust an intuitive "-1" without checking it against a small concrete
  example first.
- Pattern: [[MonotonicStack]] (`../patterns/MonotonicStack.md`) — nearest-
  greater-left used as a span/distance calculation, not just an index answer.
- Review Date: 2026-07-22

### 2026-07-21 — Min Stack, review #1
- Mistake: Mechanics (value+minSoFar pair per frame) correct cold, but asked
  why not just one global `minSoFar` variable, gave an unrelated/confused
  answer first (conflated with a different sliding-window-style problem).
- Root Cause: Never actually derived the pop-side failure mode of a global
  var — only ever reasoned about the push side.
- Correct Thinking: A single global var can't un-learn a min once its owning
  element pops off (e.g. push 2, push 5, push 1 [global→1], pop 1 → global
  still says 1, but true remaining min is 2). Per-frame storage makes pop
  restore the prior min automatically.
- How to Avoid: For "why not a single running variable" questions on any
  stack-augmentation problem, explicitly trace a pop of the *current best*
  element before answering — push-side reasoning alone misses the real
  justification.
- Topic Area: Stack/Queue — state-augmented stack, pop-invalidation reasoning.
- Review Date: 2026-07-24

### 2026-07-21 — Rotate Array, review #3
- Mistake: Boundary (`n-k` vs `k` split) self-corrected fast, but asked to
  derive *why* reverse-chunk1/reverse-chunk2/reverse-whole rotates the
  array, said "I don't know the internals, I just know the formula" —
  needed a full guided one-line-at-a-time trace to rebuild it.
- Root Cause: This is the 3rd review in a row where the mechanical steps
  hold but the underlying "why" has never actually been internalized —
  purely memorized procedure, no conceptual anchor.
- Correct Thinking: Reversing each chunk individually first flips their
  internal order; reversing the whole array afterward double-flips each
  chunk back to original internal order (cancels) while swapping the two
  chunks' positions — net effect is rotation.
- How to Avoid: Standing gap specific to this problem — next review should
  start with "derive the why from scratch, unaided" as the pass/fail bar,
  not just the split-boundary check (which is no longer the actual weak
  point).
- Pattern: [[ReversalAlgorithm]] (`../patterns/ReversalAlgorithm.md`) —
  derivation never internalized despite 3 clean-ish mechanical recalls.
- Review Date: 2026-08-04

### 2026-07-21 — Kadane's Maximum Subarray Sum, review #3
- Mistake: Correct order (max-check before reset) recalled cold and
  correctly, but the "why does wrong order break on all-negative arrays"
  explanation was hand-wavy/imprecise ("check which minimum negative we
  found") until walked through a concrete `[-3,-1,-2]` trace.
- Root Cause: Procedure memorized correctly, underlying failure-mode
  reasoning not independently reproducible without a concrete trace prompt.
- Correct Thinking: Reset-before-check with buggy order throws away every
  candidate value before `max` ever sees it — final answer stays at the
  initial value (e.g. 0) instead of the true best (e.g. -1).
- How to Avoid: For `[derive]` reviews where the "why" answer is vague, push
  for a concrete small-array trace before accepting the explanation as
  passing.
- Pattern: [[Kadanes]] (`../patterns/Kadanes.md`) — order recalled solid,
  "why" still needs a trace prompt.
- Review Date: 2026-08-04

### 2026-07-21 — Print Subarray with Maximum Sum, review #1
- Mistake: Item (1) close-loop question ("why start=tempStart not start=i")
  — supposedly closed 2026-07-20 via full guided re-trace — came back fully
  blank ("I don't remember how I solved this problem"). Needed a complete
  rebuild from scratch, one variable at a time, including re-deriving
  tempStart's reset-to-`i+1` rule along the way.
- Root Cause: 2nd decay of the identical derivation point within roughly 24
  hours — the 07-20 "closed" session's guided re-trace did not stick at all,
  not even partially.
- Correct Thinking: unchanged from 07-20 entry — `tempStart` holds the
  current running window's start; at the moment a new max is found, that
  running window IS the winning one, so `start=tempStart` (not `start=i`,
  which would wrongly report a length-1 subarray).
- How to Avoid: This specific derivation needs more than one guided rebuild
  to stick — schedule an extra short recall-only check before the next
  scheduled review, not just wait for the normal interval.
- Pattern: [[Kadanes]] (`../patterns/Kadanes.md`) — dual-pointer variant,
  repeat decay (2nd occurrence) of the same derivation point.
- Review Date: 2026-07-24

### 2026-07-24 — Next Greater Element, review #1
- Mistake: Mechanics (monotonic stack, correct value pushed) recalled clean,
  but asked why pushing the computed answer (instead of original value)
  breaks the stack, gave circular/incomplete answers until walked through a
  concrete buggy-trace comparison.
- Root Cause: The 07-20 coding bug got fixed in code but the underlying
  reasoning was never independently internalized — only the fix stuck, not
  the "why."
- Correct Thinking: Stack must hold real array values so future comparisons
  see true data; pushing `ans[i]` instead corrupts every later comparison —
  concretely, index 2's true answer (10) gets lost the moment index 3's slot
  holds "-1" instead of "10".
- How to Avoid: For "why did this bug happen" reviews, don't accept "we
  should push X" as sufficient — require a concrete trace showing where the
  buggy version diverges from correct output.
- Pattern: [[MonotonicStack]] (`../patterns/MonotonicStack.md`) — repeat
  derivation gap, mechanics solid but underlying reasoning needed a 2nd
  rebuild.
- Review Date: 2026-07-27

### 2026-07-24 — Frog Jump (DP-3), review #3
- Mistake: Recurrence (`dp[i]=min(...)`) stated correctly cold, but the "why
  min not addition" explanation was terse/circular ("we take minimum cost")
  until pushed to name what each term physically represents.
- Root Cause: Formula memorized correctly this time, but the two-option-cost
  framing (jump from i-1 vs i-2, each with its own cost) wasn't
  spontaneously articulated.
- Correct Thinking: Two ways to reach frog i (from i-1 or i-2), each carries
  its own jump cost on top of that predecessor's best cost — take whichever
  total is cheaper, hence min not addition.
- How to Avoid: For DP "why min" questions, require naming what each
  recurrence term physically represents, not just restating "take the
  minimum."
- Pattern: 1D DP (DP-3 family) — recurrence solid, "why min" needed one
  prompt.
- Review Date: 2026-08-07

### 2026-07-24 — Longest Repeating Character Replacement
- Mistake: Correctly derived the validity formula (`windowLen-maxFreq<=k`)
  after one hint, but then asserted the net window length CAN shrink back
  down after growing, once the tracked maxFreq goes stale post-shrink.
- Root Cause: Reasoned from the formula in the abstract instead of tracing
  concrete index-by-index state; didn't realize the shrink step is a single
  `if` (not `while`) precisely so the window only ever slides at constant
  size, never shrinks net.
- Correct Thinking: Traced `"AABABBA"`,k=1 step by step — after the first
  invalid window, `if`-shrink moved left by 1 while right stayed put, so
  window length stayed 4 (not less). Net window length is non-decreasing
  across the whole traversal; the final length at loop end is the answer.
- How to Avoid: For any "at-most-K, monotonic-best" sliding window problem,
  don't reason from the formula alone — trace a concrete invalid-window
  transition to confirm net length never drops.
- Pattern: [[SlidingWindow]] (`../patterns/SlidingWindow.md`) — At-most-K
  variant, first exposure to this specific misconception.
- Review Date: 2026-07-25

### 2026-07-24 — Nearest Smaller to the Left, review #1
- Mistake: Instance mechanics (pop-while->=, -1 sentinel) recalled clean,
  but the `[derive]` "why left-to-right traversal" question got circular
  answers ("because the question asks for left") twice before landing on
  the transferable rule, comparing against Next Greater Element's
  right-to-left traversal.
- Root Cause: Same generalization gap as the original 2026-07-21 solve —
  instance-level mechanics stuck, but the transferable principle across
  problems did not automatically re-surface on review.
- Correct Thinking: Start traversal from the query side, moving toward the
  other end — by the time index `i` is processed, the stack holds exactly
  the already-processed elements from the query side.
- How to Avoid: This generalization has now needed escalation twice
  (2026-07-21 original solve, 2026-07-24 review #1) — treat as a standing
  weak point, not resolved after one correct explanation; re-test the rule
  itself (not just the instance) at the next review.
- Pattern: [[MonotonicStack]] (`../patterns/MonotonicStack.md`) — repeat
  generalization gap, 2nd occurrence.
- Review Date: 2026-07-27

### 2026-07-25 — Flood Fill
- Mistake: Proposed marking visited (repainting) at pop time instead of
  push time — 3rd recurrence of this exact bug today (after BFS/DFS
  Traversal). Self-caught this time via own 2x2-grid trace showing a
  duplicate push, before writing any code.
- Root Cause: Visited-at-push rule not yet fully automatic despite 2 prior
  same-day corrections — still needs a concrete trace to re-derive, not
  spontaneously recalled.
- Correct Thinking: Repaint/mark at push time, always, no exceptions for
  grid-traversal variants of BFS/DFS.
- How to Avoid: Treat "mark at push, never pop" as a fixed rule to state
  before writing any BFS on a new problem shape, not something to
  re-derive per problem.
- Pattern: Graph Traversal (BFS/DFS) — 3rd same-day recurrence.
- Review Date: 2026-07-26

### 2026-07-25 — Bipartite Check (LC 785)
- Mistake: (1) Odd-cycle "why bipartite fails" derivation — 2 failed
  attempts, needed a light-switch parity analog before landing. (2) First
  code draft only DFS'd from node 0, missing disconnected components.
- Root Cause: (1) No mental model connecting cycle length parity to color
  parity beyond the mechanical color-flip rule. (2) Reused single-DFS
  shape without checking the "disconnected graph" edge case already known
  from Number of Provinces.
- Correct Thinking: Walking a cycle flips color once per edge; an odd
  number of flips can't return to the start node's original color, but the
  closing edge forces exactly that — contradiction. For disconnected
  graphs: loop over all nodes, DFS from every uncolored one.
- How to Avoid: For any "does X property hold on this whole structure"
  graph problem, explicitly check the disconnected-graph case before
  considering the solution complete — same reflex as Number of Provinces.
- Pattern: Graph/Bipartite — [note](../notes/bipartite-check.md).
- Review Date: 2026-07-26

### 2026-07-25 — Longest Consecutive Sequence, review #3
- Mistake: Restated the pruning rule ("only expand from starts") when asked
  why it's O(n) not O(n²), instead of giving the actual accounting argument.
- Root Cause: Conflated "stating the rule" with "proving the bound" —
  recurrence of the same complexity-justification gap as the original
  2026-07-12 solve (misjudged as amortized O(n) then, too).
- Correct Thinking: Each array element enters the inner while-expansion loop
  at most once across the whole run (once consumed into a sequence, it's
  never a start again) — total inner-loop work sums to ≤n, not n per outer
  iteration.
- How to Avoid: For "why is this O(n)" questions on prune-and-expand
  patterns, require a per-element visit-count argument, not a restatement of
  the pruning condition.
- Pattern: Arrays — hash set, sequence-start pruning, complexity proof.
- Class: invariant-why
- Recurrence: 2 (of Longest Consecutive Sequence's O(n) justification, 1st
  was the 2026-07-12 original solve)
- Review Date: 2026-08-08

### 2026-07-26 — Dijkstra's Algorithm, complexity notation
- Mistake: Repeated a garbled mixed complexity expression (`O(v+elogv+e`)
  twice, even after being asked to isolate what each term meant, before
  landing on O(E log E) (≡ O(E log V) since E≤V²).
- Root Cause: No clean mental model of what operation contributes the log
  factor (heap push/pop count vs vertex count) — pattern-matched to a
  half-remembered formula instead of deriving from operation counts.
- Correct Thinking: Total push/pop operations ≤ E (one per successful
  relaxation); each costs O(log heap-size) = O(log E) = O(log V). So
  O(E log V) overall, dominating the O(V) setup term.
- How to Avoid: For "what's the complexity" questions, force a two-step
  answer — count of operations, then cost per operation — instead of
  reciting a remembered formula.
- Pattern: Graph — Dijkstra (priority-queue relaxation).
- Class: invariant-why
- Recurrence: 1
- Review Date: 2026-07-27

### 2026-07-26 — Dijkstra's Algorithm, negative-edge failure mode
- Mistake: First answer to "why does Dijkstra fail with negative weights"
  described a negative-cycle infinite-loop, not the actual asked case (a
  single negative edge, no cycle) — conflated two distinct failure modes.
- Root Cause: Only knew "negative weights break Dijkstra" as a fact, not the
  underlying mechanism (premature visited-lock finalizing a wrong distance)
  — defaulted to the more commonly-cited (cycle) explanation.
- Correct Thinking: With a concrete no-cycle counterexample (S→Y=2, S→X=3,
  X→Y=-100), Y pops first (smaller key) and gets locked in at dist=2; X pops
  later and its -100 edge would produce a true dist of -97, but the
  visited-lock skips relaxing into an already-finalized node — wrong answer,
  no crash, no loop. Removing the lock (compare-dist-only) fixes correctness
  but destroys the O(E log V) guarantee (unbounded re-relaxation in
  adversarial graphs) — why Bellman-Ford exists instead of a patched
  Dijkstra.
- How to Avoid: When asked "why does X fail," name the concrete mechanism
  first, not the closest-sounding memorized fact — a cycle and a single bad
  edge are different failure modes even though both involve negative
  weights.
- Pattern: Graph — Dijkstra (priority-queue relaxation), contrast with
  Bellman-Ford.
- Class: transfer-gap
- Recurrence: 1
- Review Date: 2026-07-27

### 2026-07-25 — Kosaraju's Algorithm (SCC)
- Mistake: Recalled the 3-step skeleton (DFS finish-order, reverse graph,
  DFS again in finish-order) correctly unaided, but "why does processing
  order matter, not any random start node" needed 3 escalation rounds —
  two "no idea" responses before a concrete 4-node 2-SCC-plus-bridge trace
  (correct-order vs wrong-order start) made it land.
- Root Cause: Had the procedure memorized without the underlying
  topological-DAG-of-SCCs reasoning — no model for why the last-finished
  node is safe to start from.
- Correct Thinking: The node finishing last in the original DFS has no
  incoming edges from other SCCs (all its cross-SCC edges point out).
  After reversing, those become incoming-only, so a DFS starting there is
  structurally trapped inside its own SCC — can't leak into another.
  Starting from a random/earlier-finished node risks walking a reversed
  bridge edge backward and merging two SCCs into one.
- How to Avoid: For Kosaraju specifically, rehearse the "why last-finished
  node is safe" derivation explicitly before the next review — mechanics
  alone (3-step recipe) isn't enough, this problem's real difficulty is
  the reasoning, not the steps.
- Pattern: Graph/SCC — heaviest derivation of 2026-07-25's session.
- Review Date: 2026-07-26

### 2026-07-26 15:28 — Bellman-Ford (code translation of a prior derivation)
- Mistake: First code draft omitted the Vth negative-cycle detection round
  entirely (derived cleanly 5 hours earlier, same day) and used
  `Integer.MAX_VALUE-1000` as infinity with no unreachable guard. After both
  were fixed, the detection loop still lacked the `dist[u]!=INF` guard that
  the structurally identical relaxation loop had — false "negative cycle"
  return on a graph with an unreachable component containing a negative edge.
- Root Cause: Derivation-to-code gap plus asymmetric fixing — a guard was
  added at the first site it was pointed out, not at every site reading the
  same value.
- Correct Thinking: `dist[u]+wt` claims "length of path source→u→v." If
  `dist[u]` is the sentinel, no source→u path exists, so the number is a
  fake finite path length produced only because `1e8` is a real integer, not
  true infinity. The guard belongs on every loop reading `dist[u]`. Sentinel
  must be `1e8` for GFG's output contract; the guard (not a `-1000` fudge) is
  what prevents overflow — `MAX_VALUE-1000` still wraps for any `wt > 1000`,
  and a wrapped-negative looks like a huge improvement, corrupting everything
  downstream.
- How to Avoid: After fixing a guard or condition, scan the file for
  structurally identical loops and apply it there too. Re-read the prior
  session's derivation notes before coding an algorithm derived earlier.
- Pattern: Graph/Bellman-Ford — edge-list relaxation.
- Class: code-vs-derivation
- Recurrence: 1
- Review Date: 2026-07-27

### 2026-07-26 15:28 — Dijkstra visited-lock "why" (2nd escalation same day)
- Mistake: Asked to name the mechanism by which one negative edge breaks
  Dijkstra, answered "i didnt get it" — needed 4 escalation rounds (visited-set
  semantics → the S→Y=2 / S→X=3 / X→Y=-100 trace → what happens to the -97
  offer) before landing. The identical trace had been walked in full that
  morning. Then, on why "pop = final" is safe with non-negative weights,
  attributed the guarantee to "the property of the priority queue."
- Root Cause: Invariant-why decay inside a single day. The correctness
  argument has two parts — the queue gives "every unpopped node has dist ≥
  popped value," and non-negative weights give "extending a path never lowers
  the total" — and only the queue half was retained.
- Correct Thinking: The load-bearing fact is the weights, not the queue. Any
  alternative path to Y must run through an unpopped node (dist ≥ 2) plus more
  edges; with weights ≥ 0 that total can never drop below 2. A negative edge
  destroys that monotonicity — the queue behaves exactly the same.
- How to Avoid: Rehearse as "which of the two facts is load-bearing, and what
  breaks it," not as "what's the answer." Dijkstra's `[derive]` review #1 (due
  07-27) must open with this exact question.
- Pattern: Graph — Dijkstra correctness invariant.
- Class: invariant-why
- Recurrence: 2 (2nd time on 2026-07-26 the negative-edge failure mode needed
  full escalation — 1 more repeat triggers `[leech]`)
- Review Date: 2026-07-27

### 2026-07-26 23:27 — Floyd-Warshall (first exposure this cycle)
- Mistake: could not derive why `k` must be the outermost loop (vs `i`/`j`) —
  no idea offered even after a concrete 3-node trace (A→B→C, no direct A→C
  edge) was set up; session ended mid-trace at the k=B step, unresolved.
- Root Cause: no prior exposure to the "expanding allowed-intermediate-set"
  invariant framing (`dist[i][j]` after `k` iterations = shortest path using
  only vertices `0..k` as intermediates) — approach/base-case/update-rule
  were all recalled correctly, only the loop-order "why" was missing.
- Correct Thinking: not yet closed — resume the guided trace at k=B (A→B→C)
  next session before moving to k=C or general "why k outer" derivation.
- How to Avoid: n/a yet, first exposure.
- Pattern: Graph — Floyd-Warshall all-pairs shortest path.
- Class: invariant-why
- Recurrence: 1
- Review Date: 2026-07-27

### 2026-07-27 16:36 — Union-Find rank-increment invariant (Redundant Connection)
- Mistake: coded `rank[winner]++` on every union win (including the strict
  `rank[pu] > rank[pv]` branch), not only on ties. Approach stated correctly
  in words beforehand (rank/size to avoid skew) but the code didn't match it.
- Root Cause: didn't connect "rank must upper-bound true height" to "so it can
  only legitimately grow when two equal-height trees merge" — treated rank as
  just "a bigger-wins counter," not a height invariant with a specific growth
  rule. Also initially argued "it's just a number rising, not complexity" —
  needed a constructed counterexample (inflated rank forcing a genuinely
  taller tree to nest under a shorter one) to see the real height-guarantee
  loss.
- Correct Thinking: rank increments only on the tie branch — merging two
  equal-height trees is the only case true height grows by 1. Any other
  increment desyncs rank from real height, and since rank drives who stays
  root, that desync can force worse (deeper) merges later, degrading the
  O(log n) height / O(α(n)) find guarantee even though connectivity stays
  correct.
- How to Avoid: before coding union-by-rank, state the one-line invariant
  ("rank = upper bound on height, only grows on ties") and check each branch
  against it, not just "does the bigger one win."
- Pattern: Graph/DisjointSet — Union-Find rank invariant.
- Class: invariant-why
- Recurrence: 1
- Review Date: 2026-07-28

### 2026-07-30 17:06 — Min Stack review #2 (why not a single global min var)
- Mistake: first answer gave the wrong mechanism — "min for the current
  element = previous index element", i.e. treated getMin as a windowed/local
  min rather than the min of the whole current stack contents.
- Root Cause: never articulated what getMin actually promises, so the
  justification for per-frame storage was invented rather than recalled.
- Correct Thinking: self-corrected via own construction (push 10,20,30,40,5,
  100,200 then pop past 5) — pop can remove the current min, and a single
  variable has no record of the previous min, so restoring it needs an O(n)
  rescan, breaking the O(1) contract.
- How to Avoid: state what the query returns (min of all elements currently
  in the stack) before arguing about storage.
- Pattern: Stack/Queue — StackAugmentedState.
- Class: invariant-why
- Recurrence: 1
- Review Date: 2026-08-06

### 2026-07-30 17:17 — Dijkstra pop-is-final (proof reproduction)
- Mistake: could not reproduce the contradiction argument unprompted;
  answers restated the conclusion ("it's shortest because edges are
  non-negative") twice. Needed the "first not-yet-popped node u on the
  hypothetical shorter path" construction handed over before the chain moved.
- Root Cause: the argument is held as a conclusion, not as a 5-step chain.
- Correct Thinking: the two load-bearing steps were produced independently
  once u existed — key[u] >= popped key, and "a total of 5 with a prefix of 7
  would need a negative edge". Full chain: pop V key 7 -> assume shorter path
  len 5 -> it exits the settled set at u -> queue chose V so key[u] >= 7 ->
  prefix >= 7 -> remainder non-negative -> total >= 7 > 5, contradiction.
- How to Avoid: rehearse as a numbered 5-step chain, not as a sentence.
- Note: the tracked schedule question ("which is load-bearing, the PQ or the
  non-negative weights?") was answered **correctly and cold** — an
  improvement on 07-26, where it was misattributed to the PQ twice. A
  `[leech]` tag was raised mid-session and then **retracted**: it was being
  applied to a stricter test (reproduce the formal proof) than the scheduled
  one. Stays `[derive]`.
- Pattern: Graph/ShortestPath — Dijkstra.
- Class: invariant-why
- Recurrence: 3 (but attribution half now clean — see note)
- Review Date: 2026-08-02

### 2026-07-30 17:27 — Bellman-Ford review #1 (V-1 rounds, Vth round)
- Mistake: two errors. (1) said a still-improving Vth round proves a
  "negative edge" in the graph — it proves a negative *cycle*; Bellman-Ford
  handles negative edges fine. (2) justified V-1 via max edge count
  (V(V-1)) and vertex degree, neither of which yields a round count.
- Root Cause: 4-day decay — both points were derived cleanly and cold on
  2026-07-26. The V-1 reason regressed from a path property to a
  degree/edge-count property.
- Correct Thinking: (1) counterexample S-5->A, A-(-3)->B settles and a Vth
  round improves nothing, so negative edge alone is not the trigger —
  negative cycle is. (2) V-1 counts the max **edges** on a shortest path: a
  path visiting V vertices has V-1 edges, and no vertex repeats (a repeat
  means a cycle — non-negative cycle is droppable, negative cycle means no
  shortest path exists). Missing link, stated at close: round k finalizes all
  shortest paths of k edges, so V-1 rounds finalize everything.
- How to Avoid: answer "V-1 counts edges on a path", never "V-1 neighbours".
- Pattern: Graph/ShortestPath — BellmanFord.
- Class: stale-recall
- Recurrence: 1 (first regression of a previously clean derivation)
- Review Date: 2026-08-02

### 2026-07-30 17:44 — Union-Find rank review #1 (cost of an inflated rank)
- Mistake: height mechanics were clean cold (rank 3 under rank 5 leaves
  height 5; tie 5+5 gives 6), but "what actually broke when rank incremented
  on every win" drew a vague non-answer and then "I don't know" twice.
- Root Cause: rank understood as a height *label*, not as the input that
  decides who stays root on later unions.
- Correct Thinking: given after escalation — an inflated rank (P: height 2,
  rank 9) beats an honest one (Q: height 5, rank 5), so Q nests under P and
  the tree becomes height 6 instead of 5. Repeated, heights drift toward O(n);
  find walks node-to-root so its cost *is* the height, degrading O(log n) to
  O(n), and union calls find twice. Answers stay correct — that's what makes
  it a silent bug.
- How to Avoid: for any tuning field, ask "who reads this value, and what
  decision does it drive?" before asking whether its value looks right.
- Pattern: Graph/DisjointSet — UnionFind.
- Class: invariant-why
- Recurrence: 2 (same invariant as 2026-07-27 16:36, different half)
- Review Date: 2026-08-02

### 2026-07-31 15:49 — Floyd-Warshall "why k outer" (3rd stall)
- Mistake: could not derive why k must be the outermost loop, 3rd session
  running on the exact same point (07-26 stalled at k=A step, 07-30 re-posed
  at same point ended with no answer, 07-31 needed a full concrete 4-node
  counterexample trace (A-B-C-D) plus a named-analogy explanation before
  attempting a restate — restate still not given by session end).
- Root Cause: no grasp of the "allowed-intermediate-set" invariant (dist[i][j]
  after k passes = shortest path using only nodes 1..k as intermediates) —
  without it, k-outer vs k-inner looks like an arbitrary loop-order choice
  rather than a correctness requirement.
- Correct Thinking: k outer means each pass "opens" one more hub as a legal
  stepping-stone, permanently, before the next hub opens — so a k=C pass can
  chain onto a bridge (e.g. A-C) that a prior k=B pass already fixed. With k
  innermost, no such opening order exists inside one (i,j) pair's single
  pass, so multi-hop (3+ edge) chains can never assemble.
- How to Avoid: open every Floyd-Warshall review with "state the invariant
  dist[i][j] holds after k passes" before anything else — mechanics/base
  case are not the weak point, this invariant is.
- Pattern: Graph/ShortestPath — FloydWarshall (pattern file not yet created).
- Class: invariant-why
- Recurrence: 3+ (07-26 23:27, 07-30 17:05, 07-31 15:49 — same exact point)
- Review Date: 2026-08-01

### 2026-08-01 09:24 — Min Cost to Connect All Points, complexity (n^2 edges * log(n^2))
- Mistake: first answer multiplied edge count by op cost incorrectly (`n^2 *
  n log n`, i.e. n^3 log n) instead of `n^2 * log(n^2)`.
- Root Cause: didn't separate "how many edges" from "cost per PQ op" before
  combining — merged them into one guessed expression.
- Correct Thinking: n^2 edges pushed to PQ, each push/pop costs log(PQ size)
  = log(n^2) = O(log n). Total O(n^2 log n).
- How to Avoid: for PQ-based complexity, always answer as two separate
  numbers (item count, cost per op) before multiplying.
- Pattern: Graph/MST — Kruskal's via PQ + Union-Find.
- Class: boundary
- Recurrence: 1
- Review Date: 2026-08-04

### 2026-08-01 09:24 — Min Cost to Connect All Points, MST greedy correctness (cut property)
- Mistake: asked why picking the cheapest non-cycle-forming edge each step
  guarantees minimum total, gave three circular/restating answers ("because
  we want minimum cost", "it won't [hurt]", "cheapest is never negative")
  before landing the actual swap-argument via a concrete 3-node numeric
  counterexample (A-B=1, A-C=5, swapping A-C for A-B in a tree dropped cost
  by 4, so a tree skipping the cheapest crossing edge can't be optimal).
  Generalizing that to "why does Kruskal's global-sorted-order + union-find
  apply this at every step" needed a further nudge and the full formal
  chain (no cheaper crossing edge survives past its own accept/reject
  decision) turned out to be past interview bar — user flagged it as
  intimidating, correct call, capped at the swap-argument + cut-property
  one-liner instead of the full proof.
- Root Cause: had the mechanical algorithm (PQ + union-find) right cold, but
  no derived model for *why* greedy-by-cheapest-edge is safe — first
  exposure to the cut-property/exchange-argument idea for MST.
- Correct Thinking: for any cut (any split of vertices into two groups), the
  cheapest edge crossing it is safe to add — if an optimal tree used a
  pricier crossing edge instead, swapping in the cheap one strictly lowers
  cost, contradicting optimality. Kruskal's applies this at every accepted
  edge implicitly. Interview-caliber depth stops at the swap-argument +
  this one-liner, not a full sorted-order proof.
- How to Avoid: for "why is this greedy choice safe" questions on MST/
  exchange-argument problems, go straight to a concrete numeric swap trace
  rather than trying to reason abstractly first.
- Pattern: Graph/MST — Kruskal's, cut property (pattern file not yet
  created — problem not closed, no code written yet).
- Class: invariant-why
- Recurrence: 1
- Review Date: 2026-08-04

### 2026-08-01 08:35 — Floyd-Warshall "why k outer" (4th stall)
- Mistake: still could not derive the invariant — "i dont know why outer loop
  correct then inner one" when re-posed cold, no progress beyond 07-31's
  held trace.
- Root Cause: same as prior three entries — no internalized
  allowed-intermediate-set framing. Session shifted to a self-serve
  interactive step-through tool (k-outer vs k-inner trace, A-B-C-D chain)
  instead of another guided verbal derivation; no verbal answer attempted
  yet against it.
- Correct Thinking: unchanged from 07-31 entry — not yet closed.
- How to Avoid: re-pose the closing invariant question after the user has
  used the interactive artifact, before defaulting to another guided trace.
- Pattern: Graph/ShortestPath — FloydWarshall (pattern file still not
  created — hold off until this closes).
- Class: invariant-why
- Recurrence: 3+ (07-26 23:27, 07-30 17:05, 07-31 15:49, 08-01 08:35 — same
  exact point, 4 sessions running)
- Review Date: 2026-08-02

### 2026-08-01 16:32 — Floyd-Warshall "why k outer" — RESOLVED (5th attempt)
- Mistake: n/a — closing entry. Landed via a fresh concrete instantiation
  (dist[A][C]=2 vs dist[A][D]=INF, both checked right after k=B pass) rather
  than re-running the abstract A-B-C-D chain trace again.
- Root Cause: prior 4 attempts stayed too abstract too early; this time
  anchored on two single concrete numbers before generalizing.
- Correct Thinking: after the k-loop finishes node k, dist[i][j] for any
  pair = shortest path using only nodes 1..k as intermediates; k outer
  guarantees each phase is fully built before the next starts, so
  dist[i][k]/dist[k][j] read during phase k are always already-finalized
  values from phases 1..k-1. Deeper "why must k be outermost, concretely,
  under i/j-outer order" was raised but user correctly pushed back
  (over-depth) — capped at the invariant statement, same as Kruskal's cut
  property earlier the same day.
- How to Avoid: for repeat-stalled invariant derivations, switch from
  re-running the full abstract trace to picking two/three concrete number
  pairs (one resolved, one not) and asking "what's different."
- Pattern: Graph/ShortestPath — FloydWarshall (pattern file to create).
- Class: invariant-why
- Recurrence: resolved (was 3+, this closes it)
- Review Date: 2026-08-02

### 2026-08-01 16:52 — Prim's relax rule mistaken as cumulative (Dijkstra transfer)
- Mistake: verbally described Prim's relax step as `dist[u] + edge_weight`
  ("like Dijkstra"), i.e. cumulative distance-from-source, instead of the
  raw edge weight alone.
- Root Cause: Prim's and Dijkstra share the exact same code skeleton
  (frontier PQ, pop-mark-relax) — the one line that differs (relax formula)
  got pattern-matched to the more recently-drilled algorithm.
- Correct Thinking: caught via a 3-node counterexample (A-B=10, A-C=1,
  C-B=3) — cumulative dist[B] via C computes to 4 (1+3), but adding that to
  a running total that already counted the 1 for A-C double-counts, giving
  5 instead of the real MST cost 4. Prim's dist[node] = cheapest single
  edge connecting that node to the current tree, not distance from a fixed
  source — resets its meaning at every node, unlike Dijkstra's cumulative
  invariant.
- How to Avoid: before coding either algorithm, say the one differing line
  out loud first (raw edge vs cumulative) rather than assuming the shared
  skeleton means shared relax formula.
- Pattern: Graph/MST — Prim's (pattern file to create).
- Class: transfer-gap
- Recurrence: 1
- Review Date: 2026-08-02

### 2026-08-01 17:09 — Prim's array-based O(n²) variant — first exposure, heavy scaffold
- Mistake: n/a (no prior exposure, not a corrected error) — after correctly
  deriving the min-scan sub-step (track min value+index over unvisited,
  same shape as "find largest element") and the corrected relax rule, user
  could not assemble the full loop unaided ("i dont know this approach...
  give me the code") and the full array-based implementation was supplied
  after the sub-pieces were confirmed.
- Root Cause: genuinely new mechanism (no-heap Prim's for dense graphs),
  not rust — heap-based Prim's and Kruskal's were both solved cold same
  session, this variant simply hadn't been seen before.
- Correct Thinking: outer loop n times; each iteration linear-scan
  unvisited nodes for min `dist[]` (same as min-scan sub-step), mark
  visited, add `dist[u]` to cost, relax all unvisited neighbors via
  `dist[v]=min(dist[v], edge_weight(u,v))`. O(n²) total, no PQ needed —
  matches the "Prim's for Complete Graph" optimization independently
  verified against the LeetCode 1584 editorial thread.
- How to Avoid: n/a — flagged for review to convert this from
  scaffolded-derivation into independent recall.
- Pattern: Graph/MST — Prim's, array-based variant (pattern file to create).
- Class: transfer-gap
- Recurrence: 1
- Review Date: 2026-08-02

### 2026-08-01 17:37 — Kth Largest Element, didn't know build-heap is O(n)
- Mistake: when asked whether push-one-by-one is the only way to build a
  heap from an array, said "no idea" — unaware `heapify`/bottom-up
  build-heap runs in O(n), not O(n log n).
- Root Cause: never encountered the technique before — first Heaps
  problem this cycle, not a rust/recall failure.
- Correct Thinking: bottom-up build-heap sifts down from the last
  non-leaf node to the root (skipping leaves); most nodes sit near the
  bottom and only sift a short distance, so the height-weighted sum of
  work converges to O(n). Java's `new PriorityQueue<>(Collection)` and
  Python's `heapq.heapify()` both use this internally.
- How to Avoid: n/a (informational fact, told directly — not a technique
  to derive). Flag on next Heaps review to confirm it stuck.
- Pattern: Heap — build-heap/heapify.
- Class: transfer-gap
- Recurrence: 1
- Review Date: 2026-08-02

### 2026-08-01 22:00 — Top K Frequent Elements, eviction-comparator direction
- Mistake: stated the min-heap-of-size-k comparator as descending (freq
  dec) — top-of-heap would then be the *largest* freq, contradicting the
  stated eviction goal of discarding the smallest.
- Root Cause: conflated "min-heap" as a label with what the comparator
  actually orders — didn't check that eviction target (smallest) matches
  what descending puts on top (largest).
- Correct Thinking: comparator must be ascending (`a.freq - b.freq`) so
  the smallest freq sits on top and gets popped when size>k, leaving the
  k largest.
- How to Avoid: before fixing comparator direction, state in words what
  should sit on top for the intended eviction, then derive the direction
  from that — don't pick a direction first and hope it matches.
- Pattern: Bounded Heap (Top-K).
- Class: invariant-why
- Recurrence: 1
- Review Date: 2026-08-02

### 2026-08-02 10:47 — Find Median from Data Stream, inverted heap-half assignment
- Mistake: two-heap structure named correctly, but halves assigned
  backwards — "min-heap covers elements less than the middle" — while
  simultaneously saying the extra element is kept in the max-heap.
- Root Cause: picked heap types before asking which single element each
  heap must expose in O(1); lower half needs its *largest* on top, upper
  half its *smallest*.
- Correct Thinking: lower half in max-heap, upper half in min-heap; the
  two tops are exactly the two candidate middle values.
- How to Avoid: same rule as the 08-01 comparator slip — state what must
  sit on top and why *before* naming the heap type.
- Pattern: Two Heaps (Median Maintenance).
- Class: invariant-why
- Recurrence: 2 (of "name the heap type before deriving what its top must
  be" — 1st was Top K Frequent comparator direction, 2026-08-01 22:00)
- Review Date: 2026-08-03

### 2026-08-02 16:54 — Find Median from Data Stream, `addNum` guard bugs
- Mistake: two bugs in one method — `minHeap.isEmpty() && maxHeap.peek()>
  minHeap.peek()` (missing `!`, NPE on the first ever call), and a rebalance
  that only ever moved max→min, so min could exceed max without limit
  (1 vs 3 on `{1,2,3,4}`, median returned 1.5 instead of 2.5).
- Root Cause: guard written for the direction being thought about at the
  time; the symmetric case was never tested. `findMedian` was separately
  patched to read the bigger heap, which masked the imbalance instead of
  fixing it.
- Correct Thinking: a size invariant needs a guard on *both* sides —
  `maxSize > minSize+1` and `minSize > maxSize`; handing min's top back is
  order-safe because it is the smallest of the larger half.
- How to Avoid: after writing any asymmetric condition, immediately state
  the mirrored case and check which clause catches it.
- Pattern: Two Heaps (Median Maintenance).
- Class: invariant-why
- Recurrence: 1
- Review Date: 2026-08-03

### 2026-08-02 16:54 — Merge k Sorted Lists, space accounting
- Mistake: gave space as O(N), then O(N)+O(k), counting the output list as
  space and assuming new nodes must be allocated.
- Root Cause: no separation between auxiliary space and output size; never
  asked whether the result could reuse the input nodes.
- Correct Thinking: relink existing nodes, output is not extra space —
  auxiliary space is the heap alone, O(k).
- How to Avoid: on any linked-structure problem, answer "does this allocate
  or relink?" before quoting a space figure.
- Pattern: K-way Merge.
- Class: transfer-gap
- Recurrence: 1
- Review Date: 2026-08-03

### 2026-08-02 16:54 — Task Scheduler, scheduling-key and cooldown offset
- Mistake: heap ordered by availability time with ties broken arbitrarily,
  then by task label; and re-push offset given as `current + n`.
- Root Cause: cooldown treated as "next slot is n away" rather than "n empty
  slots sit between two runs"; tie-break chosen before asking what the greedy
  actually optimises.
- Correct Thinking: among available tasks pick highest remaining frequency
  (it dictates the skeleton); next availability is `current + n + 1`.
- How to Avoid: instantiate the smallest legal case (`[A,A]`, n=2) before
  trusting any offset arithmetic.
- Pattern: Greedy Task Scheduling.
- Class: boundary
- Recurrence: 1
- Review Date: 2026-08-03

### 2026-08-02 16:54 — Task Scheduler, closed-form formula decayed in minutes
- Mistake: derived `(maxFreq-1)*n + maxFreq`, verified it on two concrete
  inputs, correctly added the `countMax-1` tie term — then five minutes later
  said "i forgot how we derived the formula" and could not restate it.
- Root Cause: the formula was read off a specific traced schedule but never
  re-anchored to the block picture (`maxFreq-1` blocks of width `n+1`, plus a
  final partial block), so nothing structural was retained.
- Correct Thinking: `(maxFreq-1)*(n+1) + countMax`, and the true answer is
  `max(formula, tasks.length)`.
- How to Avoid: after any derived formula, immediately restate what each term
  counts in one sentence before moving on — same close-the-loop step the
  Socratic protocol ends on.
- Pattern: Greedy Task Scheduling.
- Class: stale-recall
- Recurrence: 1 (but same shape as Floyd-Warshall's repeated invariant loss —
  derivations verified only against a traced example don't survive)
- Review Date: 2026-08-03

### 2026-08-04 — Task Scheduler, closed-form formula (2nd decay, review #1)
- Mistake: cold recall gave `(maxFreq-1)*n + maxFreq` — missing block width
  `n+1` and using `maxFreq` instead of `countMax`; caught via trace
  (A×3,B×3,n=2: formula gave 7, true 8). Also briefly conflated idle-slot
  count (n, between two same-task runs) with block span (n+1, task+its gap)
  when asked to explain the miss.
- Root Cause: same formula as 2026-08-02, decayed exactly as that entry
  predicted — verified only against a traced example last time, never
  re-anchored to the block picture.
- Correct Thinking: `(maxFreq-1)*(n+1) + countMax`; block width = task-slot
  (1) + idle-slots (n) = n+1, confirmed via own index-diff trace (positions
  0,3,6 → gap 3 = n+1, not n).
- How to Avoid: same fix as 08-02 — restate what each term counts, in words,
  immediately after deriving, not just verify it numerically.
- Pattern: [[GreedyTaskScheduling]] (`../patterns/GreedyTaskScheduling.md`).
- Class: stale-recall
- Recurrence: 2 (of Task Scheduler's closed-form formula, 1st 2026-08-02) —
  **leech candidate, 1 more repeat triggers `[leech]`**
- Review Date: 2026-08-05

### 2026-08-07 — Job Sequencing, DSU slot-find optimization
- Mistake: could not reach (or recognize) Union-Find as the way to beat the
  O(n²) slot scan — "I don't know" / "no idea" through a category hint and a
  parking-lot analog; asked directly for the answer, full explanation given.
- Root Cause: DSU is filed under Graphs/connectivity only. The abstraction it
  actually provides — "point me at the representative of my group, and
  collapse the chain" — isn't indexed as a general tool, so a non-graph use
  (slots, not nodes) doesn't retrieve it.
- Correct Thinking: repeated re-walking of a known-filled region is the tell.
  Store a redirect per position (`parent[i]` = nearest free slot ≤ i) instead
  of a boolean; `find` follows and compresses; `parent[slot] = slot-1` on
  fill; index 0 = "no slot" sentinel. O(n log n) total, sort-bound.
- How to Avoid: when a scan repeatedly re-traverses positions already known
  dead, ask "what would each dead position have to point at to make this one
  hop" — that question, not the word "graph", is DSU's trigger.
- Pattern: [[UnionFind]] + [[SlotAssignmentGreedy]].
- Class: transfer-gap (technique known in one context, not retrieved in
  another) — distinct from stale-recall; Redundant Connection's DSU code was
  written cleanly 2026-07-27.
- Recurrence: 1
- Review Date: 2026-08-08

Note: the two derivations *before* this one were clean and cold — per-job
scan cost (≤ d steps), worst-case input shape (all deadlines = n, not all =
1), and the n(n-1)/2 sum, all unprompted. The gap is specifically
recognizing an unfamiliar application of a known structure, not complexity
reasoning.

### 2026-08-08 — Job Sequencing (heap variant): no-regret / exchange argument
- Mistake: asked why evicting the min-profit job from a full heap is never
  regretted, answered "because we are looking for max profit and removing the
  min won't hurt" — the claim restated as its own justification. Two further
  attempts stayed at the mechanic level ("remove the smallest, others
  unchanged") without naming what the swap preserves. 4 escalations before
  landing.
- Root Cause: greedy safety argued from the objective ("we want max profit")
  instead of from feasibility — no habit of asking what future decisions
  actually read off the current state.
- Correct Thinking: a future job's feasibility test is `deadline > pq.size()`
  — it reads the **count**, never the identity of what's held. Evict+insert
  leaves the count unchanged, so every future decision is identical, while
  total profit strictly increases. No regret possible.
- How to Avoid: to justify any exchange/swap greedy, find the quantity later
  steps actually depend on, then show the swap leaves it invariant. "It's
  better because we want better" is the tell that the invariant is missing.
- Pattern: [[SlotAssignmentGreedy]] (bounded-heap-with-eviction variant).
- Recurrence: 3 in the greedy-justification family (2026-08-05 N Meetings
  "why end-time", 2026-08-06 Jump Game "why max-reach", both also needed
  prompting). Mechanics keep coming out cold; the *why* keeps needing help.
- Review Date: 2026-08-09

### 2026-08-08 — Session conduct: solution pasted, not derived
- Mistake: brought the heap approach as a copy-pasted GFG solution ("i like
  its idea and need to review it later") rather than deriving it.
- Root Cause: none — self-disclosed immediately, no false credit claimed.
  Logged so the tracker doesn't record it as a solve.
- Correct Thinking: the surrounding reasoning was genuine and mostly cold —
  the sort-key flip (deadline-asc is right *here* because the heap does the
  profit selection), O(n log n)/O(n), and spotting `!pq.isEmpty()` as a dead
  branch (`size ≥ d ≥ 1`) all unprompted. Only the exchange argument needed
  escalation (entry above).
- How to Avoid: logged as **read, not derived** — goes on the review ladder
  at #1 with no independent-solve credit; re-solve from scratch at review.
- Pattern: [[SlotAssignmentGreedy]].
- Review Date: 2026-08-09

### 2026-08-08 — Job Sequencing DSU close-the-loop (carried from 2026-08-07)
- Mistake: none of substance — the parked question (why `parent[slot] =
  slot-1` stays correct when slot-1 is itself full) went "I don't know,
  explain it" first, but closed after **1 nudge** (was `find` recursive?),
  vs. a full explanation needed the day before.
- Correct Thinking: `parent[x]` is a redirect ("continue the search from
  here"), not an assertion that x is free; only a root is a real free slot.
  User stated both in own words.
- How to Avoid: n/a — improvement datapoint, kept as the counterweight to
  the transfer-gap entry of 2026-08-07.
- Pattern: [[UnionFind]].
- Recurrence: transfer-gap entry 2026-08-07 now has one clean follow-up.
- Review Date: 2026-08-11

### 2026-08-08 20:46 — Fractional Knapsack: greedy justification circular again
- Mistake: mechanics answered cold and correct (value/weight ratio, max-heap,
  fraction of the last item). "Why is highest-ratio-first safe" answered with
  "since we want the maximum value, we pick the highest ratio first" — restates
  the objective, proves nothing.
- Root Cause: same shape as 2026-08-08 Job Sequencing ("removing the min won't
  hurt") — justification given as goal-restatement rather than an exchange
  argument on a concrete pair.
- Correct Thinking: not yet reached — escalated to a concrete swap
  (W=10, A w6/v60, B w10/v50; claimed-optimal 2A+8B, swap 1 unit B out for
  1 unit A in, compute the delta). Session ended before the answer.
- How to Avoid: on any greedy, ask the *why* before the mechanics, and demand
  a two-item swap with numbers rather than a sentence.
- Pattern: [[GreedyExchangeArgument]].
- Class: invariant-why
- Recurrence: 3+ (4th consecutive Greedy session needing real escalation on
  justification — 08-05 N Meetings, 08-06 Jump Game, 08-08 Job Sequencing
  heap variant, 08-08 here).
- Review Date: 2026-08-09

### 2026-08-08 23:24 — Fractional Knapsack: exchange argument closed, but only concretely
- Mistake: the swap question from 20:46 was not usable as posed ("i didn't get
  it"); once decomposed, per-unit values (10, 5) were right, but the swap delta
  was answered 20 instead of +5, and the generalization came out as a *rule*
  ("take max of A, fill the rest with B") rather than a proof.
- Root Cause: the abstract form of the exchange argument has no grip yet — every
  step lands only after being instantiated with numbers. The delta error was
  guessing rather than differencing the two totals (old 60, new 65).
- Correct Thinking: delta = ratio(A) − ratio(B) > 0, so a packing holding a
  lower-ratio unit while a higher-ratio item is unexhausted can always be
  improved by one unit-swap, hence is not optimal. User produced both the
  formula and the "so P is not optimal" conclusion.
- How to Avoid: keep posing greedy *why* questions as a numeric two-item swap,
  and ask for the delta as new-total minus old-total (both written out), never
  as a single guessed number. Then force the proof form explicitly: "from P we
  can construct ___, therefore P is not ___."
- Pattern: [[GreedyExchangeArgument]].
- Class: invariant-why
- Recurrence: 3+ (5th consecutive Greedy session, but the first where the
  argument was actually produced — closure, not a fresh failure).
- Review Date: 2026-08-09

### 2026-08-08 23:24 — Fractional Knapsack: sort space complexity
- Mistake: total space given as O(log n), reasoning from an in-place quicksort
  stack.
- Root Cause: unknown library fact — Java's `Arrays.sort` dispatches by element
  type; object arrays get TimSort (stable, O(n) auxiliary buffer), primitives
  get dual-pivot quicksort (in-place, O(log n) stack). The items here must be
  sorted as objects/pairs to keep weight and value together, so the O(n) branch
  applies. Also missed that the constructed `Item[]` is itself O(n).
- Correct Thinking: O(n) total, with the sort buffer and the item array both
  O(n) — neither strictly dominates. User stated the type of thing being sorted
  correctly and closed the loop once the library fact was supplied.
- How to Avoid: before answering sort-based space, ask two things — am I sorting
  primitives or objects, and did I allocate a new array to sort? Stability is
  the reason for the split (a merge gives it cheaply, quicksort does not).
- Pattern: n/a (library/complexity fact, same handling as build-heap O(n),
  2026-08-01).
- Class: stale-recall
- Recurrence: 1
- Review Date: 2026-08-09

### 2026-08-09 16:30 — Candy (LC 135): one-sided constraint check
- Mistake: allocated `1,1,2` for `ratings = [1,0,2]` — child 0 outranks child 1
  but got the same count.
- Root Cause: checked each child against its *right* neighbour only; the
  constraint is two-sided and the left-hand pair was never tested.
- Correct Thinking: `2,1,2` = 5. Every adjacent pair has to be checked in both
  directions — which is exactly what forces the two-pass structure later.
- How to Avoid: on any neighbour-constraint problem, verify a candidate
  allocation pair by pair in both directions before quoting a total.
- Pattern: [[TwoPassConstraintPropagation]].
- Class: boundary
- Recurrence: 1
- Review Date: 2026-08-10

### 2026-08-09 16:39 — Candy: why `max` of the two passes stays valid
- Mistake: justified the merge with "left pass guarantees the left neighbour,
  right pass guarantees the right neighbour" — true of each pass alone, but not
  an argument that either guarantee survives taking the max.
- Root Cause: same failure shape as the greedy-*why* series — the abstract form
  of a justification does not come out. Needed 3 explicit stuck signals ("i
  don't get it" x2, "no idea") before instantiation unblocked it.
- Correct Thinking: if the left constraint applies at i then `ratings[i-1] <
  ratings[i]`, so the right pass leaves `right[i-1] = 1` and `c[i-1] =
  left[i-1]`. Then `c[i] ≥ left[i] = left[i-1]+1 > left[i-1] = c[i-1]`.
  Symmetric on the other side. The user assembled the chain correctly once the
  links were posed one at a time.
- How to Avoid: the working ladder here was concrete array first
  (`[1,3,2,1]`), then a number-level analog (`max(a,b) ≥ a`), then link-by-link
  chain assembly — never the abstract statement. Same prescription as
  [[GreedyExchangeArgument]]: instantiate, then symbolize.
- Pattern: [[TwoPassConstraintPropagation]].
- Class: invariant-why
- Recurrence: 3+ (justification-in-abstract-form failing; 08-05, 08-06, 08-08
  x2, now 08-09 — first occurrence outside selection-order greedy, so the
  weakness is the proof form itself, not the Greedy topic).
- Review Date: 2026-08-10

### 2026-08-09 16:41 — Candy: reflexive "no" on the O(1)-space question
- Mistake: answered "no" to whether O(1) extra space is reachable, with no
  attempt to derive.
- Root Cause: treated an open feasibility question as a recall lookup. One
  targeted question (view the ratings as up-runs and down-runs — do you need
  per-index values or just run lengths?) produced the right idea immediately,
  so the knowledge was there and the reflex was the failure.
- Correct Thinking: O(1) is reachable — sweep once summing arithmetic series
  over each up-run and down-run. The remaining gap is the shared peak, which
  belongs to `max(up, down)`; that step was not reached (parked at user's call).
- How to Avoid: on "is X possible" questions, spend one pass looking for
  structure in the input before answering — the same reflexive-guess reflex as
  the Minimum Platforms formula guesses (2026-08-05).
- Pattern: [[TwoPassConstraintPropagation]].
- Class: invariant-why
- Recurrence: 2 (of reflexive-guessing instead of deriving; 1st was Minimum
  Platforms' chained case, 2026-08-05).
- Review Date: 2026-08-10

### 2026-08-11 20:10 — Assign Cookies: sort space read as O(1)
- Mistake: gave space as O(1) for a solution that sorts two `int[]`s.
- Root Cause: counted only variables declared in the method; the sort's own
  memory not treated as part of the solution's space. Exact mirror of 08-08,
  where the error went the other way (O(log n) claimed for an *object* sort).
- Correct Thinking: JDK `Arrays.sort` on primitives = dual-pivot quicksort,
  O(log n) recursion stack; on objects = TimSort, O(n) buffer. So O(log n +
  log m) here, never O(1).
- How to Avoid: standing checklist item — whenever a solution sorts, ask
  "primitives or objects?" before stating space. Recovered in 1 nudge here.
- Pattern: complexity accounting (not topic-specific).
- Class: stale-recall
- Recurrence: 2 (of sort-space misaccounting; 1st was Fractional Knapsack's
  TimSort buffer, 2026-08-08 23:24).
- Review Date: 2026-08-12

### 2026-08-11 20:12 — Assign Cookies: greedy *why* answered as intuition again
- Mistake: "if you don't assign the largest to the greediest, the next largest
  may not satisfy the previous person, so we lose the count" — asserts the
  conclusion, no rival plan, no move, no compared number.
- Root Cause: 5th consecutive greedy justification attempted in abstract form.
  The user also stalled on the *setup* this time ("i didnt get it whats o"),
  i.e. the symbolic framing itself blocked entry, not just the argument.
- Correct Thinking: swap C's cookie k with D's cookie L. C survives
  (`s[L] ≥ s[k] ≥ g[C]`), D survives because C is the greediest remaining, so
  `g[D] ≤ g[C] ≤ s[k]`. Count unchanged, so no optimal plan beats the choice.
  Drop-branch: `s[L] < g[C]` means no *remaining* cookie fits C, so discarding
  is free.
- How to Avoid: unchanged prescription, now with the exit criterion written
  down — an answer is not a proof until it names a rival plan, states one move,
  and compares two counts. Ladder that worked (again): numbers first
  (`g=[3,1]`, `s=[4,9]`), then rename to C/D/k/L, then the closing sentence.
  Full method + interview script now in [[GreedyExchangeArgument]].
- Pattern: [[GreedyExchangeArgument]].
- Class: invariant-why
- Recurrence: 3+ (justification-in-abstract-form; 08-05, 08-06, 08-08 x2,
  08-09, now 08-11 — 6th).
- Review Date: 2026-08-12

### 2026-08-12 17:26 — Lemonade Change: sorted an order-dependent input
- Mistake: `Arrays.sort(bills)` before the sweep. Customer order *is* the
  problem; sorting rewrites the instance.
- Root Cause: sort-first reflex. The last five Greedy problems (N Meetings,
  Job Sequencing, Fractional Knapsack, Candy, Assign Cookies) all open with a
  sort, so it went in before checking whether order carries information.
- Correct Thinking: `[10,5]` is false (first customer unchangeable); sorted to
  `[5,10]` it returns true. Rest of the code was correct — guards and the
  ten-before-three-fives preference both clean cold.
- How to Avoid: before sorting, ask "is this input a set or a sequence?"
  Sorting is free only on sets.
- Pattern: [[GreedyExchangeArgument]] (sort-first reflex).
- Class: code-vs-derivation
- Recurrence: 1
- Review Date: 2026-08-13

### 2026-08-12 17:32 — Lemonade Change: greedy *why* as intuition, 7th running
- Mistake: no rival plan, no move, no compared quantity until each was asked
  for separately; and the ten's role was first stated wrong ("helps settle a
  ten-dollar bill" — change owed on a $10 is $5, which a ten cannot pay).
- Root Cause: same abstract-form entry as the previous six. Content was
  present (flexibility asymmetry named unprompted); structure was not.
- Correct Thinking: rival P pays the $20 with 5+5+5 where G pays 10+5 — after
  the same customer G holds 2 extra fives and 1 fewer ten. The ten's only job
  is the 15 owed on a $20 (as 10+5); two fives cover that same job and also
  serve a $10 customer, which the ten never can. So G dominates P.
- How to Avoid: the unlock was "write both wallets right after the same
  customer — what's the exact difference?" Keep that as the standard *move*
  prompt for hoard-vs-spend greedy. Wrong ten's-job answer self-corrected in 1
  nudge ("how much change do you owe a $10 customer?").
- Pattern: [[GreedyExchangeArgument]].
- Class: invariant-why
- Recurrence: 3+ (justification-in-abstract-form; 08-05, 08-06, 08-08 x2,
  08-09, 08-11, now 08-12 — 7th).
- Review Date: 2026-08-13

### 2026-08-12 17:43 — Valid Parenthesis String: own rule not applied 4 min later
- Mistake: stated the counter rule cleanly (`(` +1, `)` -1, fail below zero),
  then answered "no idea how to handle this" when asked what `)` does to the
  single value 2.
- Root Cause: the question was read as a new abstract sub-problem rather than
  an application of the rule just given. Same short-horizon decay shape as
  Task Scheduler's closed form (gone ~5 min after deriving) and Floyd-Warshall's
  invariant.
- Correct Thinking: 2 → 1, so `{2,3,4,5}` → `{1,2,3,4}`. `(`/`)` are pure
  shifts; `*` is the union of the −1/0/+1 shifts, which overlap; pruning
  negatives cuts a prefix. So the reachable set is always a solid interval and
  only `(min,max)` need carrying.
- How to Avoid: when a stall follows a rule the user stated minutes earlier,
  quote their own rule back before any new hint — recovered it in one step here.
- Pattern: [[ReachableRangeCounter]].
- Class: stale-recall
- Recurrence: 3+ (short-horizon derivation decay; Floyd-Warshall 07-26..08-01,
  Task Scheduler 08-02, now 08-12).
- Review Date: 2026-08-13

### 2026-08-12 20:15 — Valid Parenthesis String: correct set, misread when stating the rule
- Mistake: twice produced the right reachable set and then stated a rule
  contradicting it — `)` on `{1,2,3}` → `{0,1,2}` but the rule came out
  "decreases max" (min frozen); `*` on `{1,2,3}` → `{0,1,2,3,4}` but the rule
  came out "min stays, max +1".
- Root Cause: the rule was answered from intuition about the character rather
  than read off the set just written one line above.
- Correct Thinking: `)` shifts both endpoints down; `*` is min−1 / max+1. Both
  are visible in the user's own set — min of `{0,1,2,3,4}` is 0, not 1.
- How to Avoid: after instantiating, force the read-off explicitly — "what is
  the min of the set you just wrote?" That recovered it both times in one step.
- Pattern: [[ReachableRangeCounter]].
- Class: code-vs-derivation
- Recurrence: 2 (same session, twice).
- Review Date: 2026-08-15

### 2026-08-12 20:22 — Valid Parenthesis String: min < 0 read as whole-string invalid
- Mistake: "if min goes negative the string is invalid" — conflated one dead
  assignment with all of them; `max < 0` kills the string, `min < 0` kills only
  a branch.
- Root Cause: the carried state had no meaning attached. "min and max are the
  min and max of *what collection*" was asked three times and never answered
  (answers were "they calculate solid run"), so the clamp had nothing to be a
  clamp *on*. Surfaced at the end as "I don't understand why I'm even
  implementing this."
- Correct Thinking: `[min,max]` is the set of unmatched-`(` counts still
  achievable over all live `*` assignments so far. A negative branch is one dead
  assignment; the surviving smallest is 0, hence the clamp.
- How to Avoid: closed only by the counterexample `*)` — min hits −1 yet the
  string is valid (`*`=`(`). Ladder step that worked: ask for an assignment that
  works. Standing fix: do not accept a vague answer to "what does this state
  mean" and move on to mechanics — the mechanics then get memorized and the
  interview question ("why the clamp?") has no answer.
- Pattern: [[ReachableRangeCounter]].
- Class: invariant-why
- Recurrence: 3+ (justification-in-abstract-form; 8th consecutive problem).
- Review Date: 2026-08-15

### 2026-08-12 20:31 — Valid Parenthesis String: patched the code instead of tracing it
- Mistake: asked to trace `)` line by line through their own code, instead
  deleted `min--` from the `)` branch — a rule they had derived correctly — and
  resubmitted. The new version returns false on `()`.
- Root Cause: bug located by guessing at which line "looked wrong" rather than
  running the failing input. The actual defect is structural, untouched by the
  patch: `if (min<0) min=0; else if (max<0) return false;` — `max<0` implies
  `min<0`, so the max check is unreachable and `)` returns true.
- Correct Thinking: the two checks are independent, not alternatives.
- How to Avoid: when a trace is requested, produce the trace — a patch offered
  in place of a trace leaves the real bug in and adds a second one.
- Pattern: [[ReachableRangeCounter]].
- Class: code-vs-derivation
- Recurrence: 2 (of guess-instead-of-trace; first was Minimum Platforms'
  chained-case count, 2026-08-05).
- Review Date: 2026-08-15

### 2026-08-13 17:10 — Valid Parenthesis String: could not construct the failing input
- Mistake: with the dead `else if` chain correctly identified, could not build a
  string that exposes it ("i dont know, this question is tough"); needed a
  3-step ladder (which character lowers `max` → which raise it → which of those
  leaves `min` at 0) before `")*"` appeared.
- Root Cause: counterexample construction treated as a search over whole
  strings rather than as solving backwards from the conditions the bug needs —
  here "max dips below 0" and "final min==0".
- Correct Thinking: read the required end-state off the buggy return, then pick
  characters by what they do to each variable.
- How to Avoid: to break a check, write down what the accept path requires, then
  choose characters one at a time to satisfy each requirement.
- Pattern: [[ReachableRangeCounter]].
- Class: invariant-why
- Recurrence: 1
- Review Date: 2026-08-15

### 2026-08-13 17:36 — Merge Intervals: justification given as the rule, not the quantity
- Mistake: asked why comparing only against the *last* kept interval is safe,
  answered "we're sorting by start time, so anything before is already merged" —
  restates the procedure rather than naming what makes an earlier overlap
  impossible.
- Root Cause: the same abstract-form answer that has failed across the Greedy
  run; the load-bearing fact (the kept list's ends are increasing, so the last
  end is the maximum) went unstated.
- Correct Thinking: `cur[0] > last[1] >= every earlier end`, so clearing the
  last interval clears all of them.
- How to Avoid: a justification must name a quantity and compare it, not
  describe the loop.
- Pattern: [[MergeIntervals]].
- Class: invariant-why
- Recurrence: 3+ (justification-in-abstract-form; but **closed in one re-ask
  with no hint** — the weakest form of this entry so far, and the rest of the
  problem needed no escalation at all).
- Review Date: 2026-08-16

### 2026-08-14 22:20 — Shortest Job First: problem statement not parsed, no attempt started
- Mistake: "I don't understand this problem" on the SJF statement — 8 minutes
  passed with no approach attempted. The algorithm turned out to be known cold
  once the statement landed.
- Root Cause: the statement gives burst times and asks for average waiting
  time, but never says out loud that the *order is yours to choose*; the user
  read it as a computation on a fixed input rather than an optimization.
- Correct Thinking: run one arbitrary order on the sample, total it (40/5 = 8),
  compare against the expected answer (4) — the gap is what proves the order is
  the decision variable.
- How to Avoid: when a statement doesn't parse, compute the sample under any
  arbitrary choice and diff it against the expected output. The disagreement
  localizes what the problem is actually asking.
- Pattern: n/a (statement comprehension, not a technique).
- Class: code-vs-derivation
- Recurrence: 1 — **new surface**. Every prior entry in this journal is
  mechanics or justification; this is the first on reading the problem itself.
  Watch whether it repeats on GFG-style statements specifically (SJF, Job
  Sequencing, Minimum Platforms are all terser than LeetCode's).
- Review Date: 2026-08-17

### 2026-08-14 22:20 — Shortest Job First: sort space given as O(n) for a primitive array
- Mistake: space stated O(n) for `Arrays.sort(int[])`; correct is O(log n)
  (dual-pivot quicksort recursion stack, no auxiliary buffer).
- Root Cause: the sort-space fact is stored as one undifferentiated "sorting
  costs extra space" rather than as the primitives/objects branch.
- Correct Thinking: `int[]` → dual-pivot quicksort, in-place, O(log n) stack.
  Object array → TimSort, O(n) merge buffer.
- How to Avoid: the standing checklist item already exists — ask "primitives or
  objects?" before answering sort space. It worked here.
- Pattern: [[GreedyExchangeArgument]] (complexity checklist).
- Class: stale-recall
- Recurrence: 3+ (4th in this class: 08-08 O(log n) for objects, 08-11 O(1) for
  primitives, 08-12 Lemonade correct-by-absence, now O(n) for primitives).
  **Improving, though** — this one was recovered in a single nudge off the
  user's own checklist item, where the previous three took real escalation.
- Review Date: 2026-08-16

### 2026-08-15 — Non-overlapping Intervals (LC 435): kept the earlier-starting interval, not the earliest-ending
- Mistake: sorted by start and, on every overlap, unconditionally kept `cur`
  and deleted the later interval. Returned 2 on `[[1,100],[2,3],[3,4]]`
  (answer 1).
- Root Cause: the removal choice was never posed as a choice — the loop encoded
  "first one wins" without asking which of the two overlapping intervals is
  cheaper to keep.
- Correct Thinking: when two intervals overlap and exactly one must go, keep
  the one that ends earlier — it leaves at least as much room for everything
  after it, so no later interval is lost by the swap.
- How to Avoid: on any interval problem, before writing the loop, ask "when two
  conflict, which one do I keep, and what property makes that safe" — the sort
  key follows from that answer rather than preceding it.
- Pattern: [[MergeIntervals]] / earliest-end greedy.
- Class: justification
- Recurrence: 1 for the miss — but note the *rule* transferred cold from N
  Meetings in One Room once the counterexample landed, and the one-sentence
  "why" needed no ladder. See progress.md 2026-08-15 (transfer success).
- Review Date: 2026-08-16

### 2026-08-15 — LC 435: sort space given as O(log n) for `int[][]`
- Mistake: space stated O(log n); correct is O(n) — `int[][]` is an array of
  references, so `Arrays.sort` with a comparator runs TimSort with an O(n)
  merge buffer.
- Root Cause: **regression** — this exact call shape was answered correctly on
  Merge Intervals 08-13, so the fact is stored but not reliably retrieved. The
  checklist prompt ("primitives or objects?") was also not understood as a
  question this time, which is new: previous misses were wrong answers, this
  was the checklist item itself failing to parse.
- Correct Thinking: primitive arrays → dual-pivot quicksort, in-place,
  O(log n) stack. Object arrays (incl. `int[][]`, `Integer[]`) → TimSort, O(n)
  buffer. Fastest tell: **a comparator was passed** — the primitive overloads
  have no comparator form, because `Comparator<T>` cannot be parameterized on a
  primitive.
- How to Avoid: replace the "primitives or objects?" prompt with the sharper
  mechanical one — "did I pass a comparator?" Comparator present ⇒ object array
  ⇒ TimSort ⇒ O(n). No type reasoning required.
- Pattern: [[GreedyExchangeArgument]] (complexity checklist).
- Class: stale-recall
- Recurrence: 5 (08-08 objects, 08-11 primitives, 08-12 by-absence, 08-14
  primitives, now `int[][]` — and this one is a regression off a correct
  08-13 answer, the first time this fact has gone backwards).
- Review Date: 2026-08-17

### 2026-08-15 — Heapify: the method itself was unknown, not just its complexity
- Mistake: build-heap's O(n) was recalled correctly, but "I don't understand
  the heapify method" surfaced on the follow-up — sift-down had never been
  built, so the complexity was a memorized fact attached to nothing.
- Root Cause: the fact entered the tracker on 2026-08-02 as a first-exposure
  note on Kth Largest ("clean except build-heap/heapify O(n) fact") and was
  logged as a *fact to re-check* rather than as *a method never learned*. Nine
  review-schedule mentions later it was still being tested as recall.
- Correct Thinking: sift-down assumes both subtrees are already heaps, swaps
  the node with its **larger** child, and repeats until the node dominates its
  children or hits the bottom — so its cost is the node's distance to the
  bottom, not log n. Build-heap runs it on every internal node bottom-up
  (last non-leaf → index 0) so the precondition always holds; leaves are
  size-1 heaps and are skipped. Cost sums to n/2·0 + n/4·1 + n/8·2 + … = O(n);
  `n log n` wrongly charges every node the root's cost.
- How to Avoid: when a review turns up a memorized complexity, ask for the
  method before accepting the number. A correct constant with no mechanism
  under it is a coverage hole wearing a review's clothes.
- Pattern: [[BoundedHeapTopK]] / [[TwoHeaps]] — heap construction.
- Class: coverage-gap (new class — every prior entry is rust, justification, or
  transfer; this is material never covered, mislabelled as a review item)
- Recurrence: 1
- Review Date: 2026-08-16

### 2026-08-15 — Floyd-Warshall: "why k outermost" not derived, 6th attempt
- Mistake: gave the role of `k` (intermediate node) correctly, then could not
  say what breaks when `k` is innermost; a guided trace on a 4-node graph was
  declined mid-way ("do we really need to dig deep into its core mechanics?").
  Full explanation handed over.
- Root Cause: the loop order is stored as a rule with no invariant attached, so
  there is nothing to reason *from* when asked what it protects.
- Correct Thinking: after the outer loop finishes value `k`, `dist[i][j]` is
  the shortest `i→j` path using only intermediates from `{0..k}`. `k` outermost
  makes it an induction over the allowed-intermediate set — every pair is
  brought current for `{0..k}` before `k` advances, so both halves of
  `dist[i][k] + dist[k][j]` are already final w.r.t. `{0..k-1}`. `k` innermost
  freezes a pair and sweeps intermediates against an unfinished table; on
  `0→3, 3→2, 2→1` (weight 1 each), `dist[0][1]` needs `dist[0][2]`, which is
  only fixed at a later `j`, and `(0,1)` never comes back — `INF` forever.
- How to Avoid: this has now failed 6 times across 5 sessions with three
  different approaches (abstract chain, concrete pair-values, guided trace).
  Stop asking "why k outer" — ask instead "**what does `dist[i][j]` mean after
  the outer loop finishes k?**" The invariant is the thing missing; the loop
  order is a consequence of it, and every attempt so far has asked for the
  consequence first.
- Pattern: [[FloydWarshall]]
- Class: stale-recall
- Recurrence: 6
- Review Date: 2026-08-16

### 2026-08-15 — Redundant Connection: what an inflated `rank` costs (4th escalation, `[leech]`)
- Mistake: answered what `rank` is *for* (attach smaller tree under bigger),
  restated `find`'s cost as tree height, but could not say which decision an
  inflated rank corrupts or what it costs. Handed over after 4 escalations.
- Root Cause: `rank` is held as a procedure, not as an invariant with a reader.
  Without "who reads this value," a question about corrupting it has nothing to
  attach to.
- Correct Thinking: `rank` has exactly one reader — `union`, choosing which
  root becomes the child. An inflated rank makes `union` attach the genuinely
  taller tree *under* the shorter one; height grows, `find` walks further, and
  the amortized O(α(n)) bound degrades toward O(log n). Correctness never
  breaks — every `find` still returns the right root. Rank is a
  **performance-only** invariant.
- How to Avoid: for any auxiliary field (rank, size, lazy tag, dirty flag), ask
  "who reads it, and is it load-bearing for correctness or only for cost"
  before asking what corrupting it does.
- Pattern: [[UnionFind]]
- Class: justification
- Recurrence: 3 (2026-07-30 review #1 needed two escalations plus a constructed
  example; original solve; today) — **tagged `[leech]` on the tag's own
  definition** (same specific point, 3rd correction), not on the miss rule.
- Review Date: 2026-08-16

### 2026-08-15 — Bellman-Ford: `V-1` justified by degree, Vth-round improvement called a negative *edge* (`[leech]`)
- Mistake: both errors are verbatim repeats of the 2026-07-30 review. `V-1`
  explained as "any node has at most V-1 edges connecting to it" (degree, not
  path length); a still-improving Vth round said to prove a negative **edge**.
- Root Cause: both facts are stored as sentence fragments attached to the
  symbol `V-1` and "Vth round" rather than to what the algorithm is doing;
  the wrong noun (edges at a node, a single edge) is locally plausible and
  never gets contradicted without a counterexample.
- Correct Thinking: round `r` finalizes nodes whose shortest path uses `r`
  edges; a shortest path cannot repeat a node, so ≤V nodes and ≤V-1 edges,
  hence V-1 rounds. Bellman-Ford *handles* negative edges by design — that is
  why it exists — so a Vth-round improvement can only mean a negative **cycle**
  reachable from the source, in which case no finite shortest path exists.
- How to Avoid: both recovered fast once re-aimed ("does Bellman-Ford work on
  negative edges?" → self-corrected in 2 steps; "can a shortest path repeat a
  node?" → closed in 2). Lead with those two questions, not with "why V-1".
- Pattern: [[BellmanFord]]
- Class: stale-recall
- Recurrence: 3 on both points (clean cold 07-26, failed 07-30, failed today —
  note the 4-day clean→failing window). **Tagged `[leech]`.**
- Review Date: 2026-08-16

### 2026-08-15 — LC 678: `min == 0` equivalence and the state's meaning (4 escalations)
- Mistake: asked what `min`/`max` range over, restated the mechanics ("they
  count open brackets") — the same vague answer that needed 3 asks on 08-12.
  Then could not say why `min == 0` alone is the whole accept condition.
- Root Cause: the parked item from 08-13 was parked precisely because it had
  not landed; re-posing it cold confirmed that, and the state-meaning gap
  underneath it is what makes the equivalence unreachable.
- Correct Thinking: the collection is the set of open-counts achievable across
  all readings of the stars seen so far (`(*` → `{0,1,2}`). `min` is the
  smallest *member* of that set, so it is itself always achievable — therefore
  `min == 0` means 0 is achievable, which is exactly validity.
- How to Avoid: the unlock, both times, was instantiating on `(*` and asking
  for the set by enumeration. Skip the abstract phrasing entirely on this item;
  open with "list every open-count reachable after `(*`".
- Pattern: [[ReachableRangeCounter]]
- Class: justification
- Recurrence: 2 (08-12, today)
- Review Date: 2026-08-18

### 2026-08-18 17:43 — Minimum Coins (GFG): greedy *why* answered as mechanics (2 escalations)
- Mistake: asked what guarantees taking as many 10s as possible is never worse,
  answered "our code always settles with higher denomination first" — a
  restatement of what the loop does, not a reason it is optimal.
- Root Cause: same abstract-form failure the tracker has logged since 08-05 —
  the *why* is asked abstractly and answered by describing the mechanic.
- Correct Thinking: drop one 10 from any plan and you owe 10 more using coins
  ≤ 5, which needs at least 2 coins, so the swap-down never lowers the count.
  Instantiated first on n=39: 3+1+2 = 6 coins vs 2+3+2 = 7.
- How to Avoid: unchanged and now fast — instantiate numerically, cost both
  plans, then ask for the general bound. Took ~3 min inside a 10-min block.
- Pattern: [[GreedyExchangeArgument]]
- Class: justification
- Recurrence: 3+ (of greedy-why answered as goal/mechanics restatement:
  08-05, 08-06, 08-08 x2, 08-09, 08-11, 08-12, today)
- Review Date: 2026-08-21

### 2026-08-18 17:38 — Mentor error: problem statement paraphrased from memory, not the link
- Mistake: **mentor-side, not user-side.** The OJ link given was GFG's "Minimum
  Coins of 1, 2, 5 and 10" (denominations {1,2,5,10}, returns a count), but the
  statement posed was a different problem (full Indian set, return the list of
  values), and n=121 was asserted to be 3 when the real answer is 13. The user's
  code was correct throughout and they were pushed to trace a non-existent bug.
- Root Cause: statement written from memory of a similar problem instead of read
  off the linked page.
- Correct Thinking: the user's "my code is right" was correct and should have
  triggered a re-read of the link, not another pointed question.
- How to Avoid: state the problem from the link's own text, or give the link
  and let the user read it. Never paraphrase a statement from memory. Same
  class as the 07-27 hint-grading and 08-13 re-ask corrections — mentor error
  logged rather than repeated.
- Pattern: n/a (process)
- Class: code-vs-derivation
- Recurrence: 1
- Review Date: n/a

### 2026-08-23 10:16 — LC 1358: "nothing is missed" answered by restating the condition
- Mistake: asked why a substring starting before `i` can be skipped, answered
  "that will violate our condition" — asserting the conclusion, not proving it.
- Root Cause: same abstract-proof-form gap as the greedy *why* series; the
  argument was never instantiated.
- Correct Thinking: `[i-1..j]` had > need distinct (that is why `i` passed it);
  any `i' < i` gives a window containing `[i-1..j]`; supersets never have fewer
  distinct; therefore every start before `i` exceeds `need`.
- How to Avoid: on any window-counting claim, name the superset relation and the
  monotonicity fact before the conclusion. Fixed here in 3 targeted questions
  (set containment / can-it-decrease / what-stopped-the-loop) — that chain is the
  working form.
- Pattern: [[SlidingWindow]], at-most-K counting
- Class: justification-by-restatement
- Recurrence: 5th of this shape (08-05, 08-06, 08-08 x2, 08-09, 08-23)
- Review Date: 2026-08-24

### 2026-08-23 10:09 — LC 1358: exactly-K-distinct vs contains-all-K conflated
- Mistake: first answer to "why does atMost(3)-atMost(2) solve it" was "we look
  around the three occurrences of a, b, c" — restatement, no argument.
- Root Cause: the alphabet constraint was used implicitly and never named.
- Correct Thinking: two separate claims — (A) atMost(k)-atMost(k-1) counts
  exactly-k-distinct, true for any alphabet; (B) exactly-3-distinct = contains
  all of a,b,c, true ONLY because the alphabet is {a,b,c}. Counterexample "abd"
  is 3-distinct without a `c`.
- How to Avoid: when a constraint makes two different predicates coincide, say
  which one the code computes and which one the problem asks for. Follow-up
  "same question but lowercase a-z" breaks B, not A.
- Note: user's pushback ("correct regardless of abc") was right about claim A —
  logged as a real distinction reached, not a plain miss.
- Pattern: [[SlidingWindow]], at-most-K counting
- Class: constraint-not-named
- Recurrence: 1
- Review Date: 2026-08-26

### 2026-08-23 09:51 — LC 435 recall blank at 8 days
- Mistake: could not recall Non-overlapping Intervals at all ("whats lc 435",
  "i forgot how i solved 435") — solved 2026-08-15 with-hints:1.
- Root Cause: review #1 was due 2026-08-16 and never ran; 08-16 and 08-22
  weekend batches both missed.
- Correct Thinking: this is the weekend-only amendment's predicted failure mode
  showing up as data, not as forecast — the amendment traded the `+1` away and
  then the weekend batch did not fire either.
- How to Avoid: decide the amendment on this signal at the next audit. One
  8-day-old with-hints problem returning zero recall is the cheapest evidence
  available that batching is not holding.
- Pattern: n/a (process)
- Class: decay/schedule
- Recurrence: 1 (first measured total-blank recall)
- Review Date: n/a

### 2026-08-23 10:32 — LC 735 Asteroid Collision: collision modeled as symmetric (UNRESOLVED)
- Mistake: push/pop conditions treat both sign orders as colliding. Two bugs —
  (1) a right-mover arriving after a left-mover is dropped instead of pushed,
  so `[-2,-1,1,2]` returns `[-2,-1]`; (2) equal magnitudes keep the positive
  instead of both exploding, so `[8,-8]` returns `[8]`.
- Root Cause: the "which pairs actually collide" step was asked for explicitly
  before coding and skipped — only `stack top > 0 && cur < 0` is a collision.
- Correct Thinking: a left-mover already on the stack can never be hit by a
  later right-mover; they diverge. Equal magnitude destroys both.
- How to Avoid: run the given examples against the written code before
  submitting — `[-2,-1,1,2]` was handed over in the problem statement and fails.
- Pattern: stack simulation (not monotonic-stack)
- Class: condition-derivation / untested-against-given-examples
- Recurrence: 1
- Review Date: 2026-08-24 (problem still open, no working code)

### 2026-08-24 17:28 — LC 735 Asteroid Collision: same bug reproduced on a cold re-attempt
- Mistake: cold restart one day later shipped 08-23's symmetric-collision
  condition verbatim (`stTop<0&&cur>=0 || stTop>=0&&cur<0`). Second, new bug:
  equality tested only *before* the pop-cascade, never against the surviving
  top after it — `[10,2,-10]` returned `[10,-10]` instead of `[]`.
- Root Cause: reasoning about direction from signs abstractly. Reading the
  08-23 diagnosis did not encode it; the defect survived a full night and a
  fresh attempt.
- Correct Thinking: instantiate numerically before deriving. Positions on a
  number line (`-1` at 0, `+2` at 5; gap 5 → 7) produced the condition in one
  trace after abstract reasoning had failed twice.
- How to Avoid: put actual numbers on an actual line before writing any
  sign-based condition. Same prescription already logged for Greedy and
  SystemDesign — this is the third track it has landed on.
- Pattern: stack simulation (not monotonic-stack)
- Class: condition-derivation / abstract-vs-concrete / untested-against-given-examples
- Recurrence: 2 (same defect as 2026-08-23; abstract-vs-concrete class ~6th)
- Review Date: 2026-08-26 (short interval, see review_schedule.md)

### 2026-08-24 17:28 — Post-cascade state not re-tested (generalizable)
- Mistake: after a `while` loop mutates the stack, the incoming element was
  compared only against the top it saw *before* the loop.
- Root Cause: treating the pop-cascade as terminal rather than as a step that
  produces a new comparison state.
- Correct Thinking: every branch of the case analysis must be re-evaluated
  against the post-loop top, not just the branch that failed to fire.
- How to Avoid: after any loop that pops, ask "which of my cases could now be
  true that wasn't before?" before pushing.
- Pattern: stack simulation
- Class: post-loop state check
- Recurrence: 1 (new class; adjacent to the recurring boundary/post-loop-check
  family already at 3+)
- Review Date: 2026-08-26

### 2026-08-25 20:46 — LC 930 shrink guard `i<j` (window can never empty)
- Mistake: `while (i < j && sum > goal)` — shrink loop stops with one element
  left, so the window cannot empty. Breaks `nums=[1], goal=0` and every
  `atMost(-1)` call, which `goal = 0` always makes.
- Root Cause: guard written to keep the window non-empty (a shape assumption)
  instead of derived from what the loop must guarantee on exit.
- Correct Thinking: on exit `[i..j]` is the longest suffix ending at `j` within
  budget, **possibly empty**. `i <= j` lets `i` reach `j+1`; `cnt += j-i+1`
  then contributes 0 and `atMost(-1)` returns 0 with no special case.
- How to Avoid: before writing any loop guard, state the exit invariant in one
  sentence including the degenerate case, then read the guard against it.
- Pattern: [[AtMostKCounting]] / sliding window
- Class: boundary/post-loop check (the family already at 3+) + degenerate-empty
  case
- Recurrence: boundary/post-loop-check class ~4th
- Review Date: 2026-08-29

### 2026-08-25 21:41 — Fixed silently; the "why" never spoken (meta)
- Mistake: corrected `i<j` to `i<=j` and resubmitted code with no explanation.
  Complexity, edge case, and the exit invariant were all asked for twice and
  never given; session ended out of time.
- Root Cause: the fix was pattern-matched off a targeted question rather than
  re-derived — same shape as reading a diagnosis without instantiating it.
- Correct Thinking: an unexplained fix is not evidence of encoding. LC 735
  (2026-08-24) reproduced its own written-up bug one day later on exactly this
  failure mode.
- How to Avoid: say the invariant out loud before editing the line. A silent
  edit gets logged as unspoken, and the review opens on the why, not the code.
- Pattern: cross-cutting (not problem-specific)
- Class: abstract-vs-concrete / encoding-not-verified
- Recurrence: 4th track for this class (Greedy, SystemDesign, Stack, now
  SlidingWindow) — this is the tracker's most-repeated finding
- Review Date: 2026-08-29

### 2026-08-26 — Trapping Rain Water (LC 42)
- Mistake: reached for `nsl/nsr` (nearest smaller/greater) as the boundary
  quantity, then "nearest taller", before landing on tallest-each-side. Also
  proposed a width-multiply (rectangle area) on a per-column sum.
- Root Cause: template retrieval from the Stack topic instead of derivation
  from the problem's physics — the rule was picked before asking what actually
  holds water above one index.
- Correct Thinking: `level_i = min(maxLeft_i, maxRight_i)`; a shorter bar
  between `i` and the tall wall cannot cap the level because it is itself
  submerged to that same level. Columns are width 1, so no area multiply.
- How to Avoid: on a new problem, state the physical/defining quantity for ONE
  index before naming any stored pattern. If a candidate rule is proposed,
  instantiate it on a 5-element array immediately — `[3,0,1,0,2]` separated
  nearest (gives 1) from tallest (gives 2) in one step.
- Pattern: [[PrecomputedBoundaryMaxima]]
- Class: template-first retrieval (new class; related to abstract-vs-concrete
  in that both are resolved by numeric instantiation)
- Recurrence: 1st logged occurrence of template-first specifically
- Review Date: 2026-08-29

### 2026-08-26 — The "why" got spoken cold (meta, positive)
- Mistake: none — logged as counter-evidence to the 4-session silent-fix streak.
- Root Cause: n/a. What worked: guided one-line-at-a-time tracing on a 4-element
  analog (`[3,1,0,2]`, "how much water sits on index 1?") produced the
  submerged-bar justification cold on the next question.
- Correct Thinking: user stated "shorter bars get submerged to the same level"
  unprompted, then gave O(n)/O(n) and both edge cases without escalation.
- How to Avoid: n/a — replicate. The unlock was a 4-element analog, not a
  re-explanation of the 5-element instance that was already on the table.
- Pattern: cross-cutting (method, not problem-specific)
- Class: justification-weakness countermeasure
- Recurrence: matches the 2026-08-18 result (ladder closed inside a short block)
  and the 07-12 guided-tracing finding — 3rd confirmation that tracing beats
  re-asking
- Review Date: n/a

### 2026-08-28 — Frog Jump (DP-3), O(1)-space rewrite
- Mistake: `backbytwo = oneStep` in the rolling update, where `oneStep =
  dp[i-1] + |h[i]-h[i-1]|`. Stored a dp value **plus a jump cost** in the slot
  that must hold `dp[i-2]`.
- Root Cause: rolled the variables off whatever was already computed in the
  loop body instead of off the stated invariant.
- Correct Thinking: name the invariant first — at the top of iteration `i`,
  `backbyone = dp[i-1]` and `backbytwo = dp[i-2]` — then the only legal roll is
  `backbytwo = backbyone` **before** `backbyone = cur`.
- How to Avoid: on any variable-rolled DP, write the invariant as a comment
  above the loop and check each assignment against it. Test with n>=4: n<=3
  never reads the corrupted slot, so the bug is invisible (`[0,10,100,10]`
  returns 100 instead of 10).
- Pattern: [[SpaceOptimizedDP]]
- Class: invariant-not-stated (same family as the 08-25 shrink-guard `i<j`)
- Recurrence: 2nd
- Review Date: 2026-08-29

### 2026-08-28 — Frog Jump (DP-3), boundary at i=1
- Mistake: recurrence written as `dp[i] = min(dp[i-1]+..., dp[i-2]+...)` with
  the loop starting at `i=1`, so `dp[-1]` is indexed on every input with n>=2.
- Root Cause: recurrence transcribed in its general form without asking which
  `i` values can actually evaluate both branches.
- Correct Thinking: peel the first iteration — `dp[1] = |h[1]-h[0]|`, loop from
  `i=2`.
- How to Avoid: for any `dp[i-k]` recurrence, evaluate the body at `i=k-1`
  before writing the loop bound. **Also**: this had been recorded as solved
  since 07-10 — a recurrence that has never been run on a judge is not a solve.
- Pattern: [[SpaceOptimizedDP]]
- Class: boundary/post-loop check
- Recurrence: 4th
- Review Date: 2026-08-29

### 2026-08-28 — Combination Sum (LC 39)
- Mistake: three recursive branches (skip / take-stay / take-move-on) where two
  suffice, producing duplicate combinations that a `HashSet` then filtered out.
- Root Cause: branch set assembled from "what moves are legal" rather than from
  "what states are reachable exactly once". take-move-on is take-stay followed
  by skip, so it re-derives paths the other two already generate.
- Correct Thinking: uniqueness should come from the shape of the search, not
  from de-duplicating its output.
- How to Avoid: **standing rule — a `Set` on a backtracking result set is a
  branching bug until proven otherwise.** When one appears, delete it and find
  the redundant branch before shipping.
- Pattern: [[Backtracking]]
- Class: over-generating search (new class)
- Recurrence: 1st
- Review Date: 2026-08-29

### 2026-08-28 — Copy cost omitted twice in one session (transfer gap)
- Mistake: complexity of Subsets given as O(2^n), corrected to O(n·2^n) after
  one nudge at the `res.add(new ArrayList<>(list))` line — then Combination Sum,
  12 minutes later and using the identical line, was given as O(2^target) with
  the same copy factor missing.
- Root Cause: the correction was accepted as a fact about Subsets, not encoded
  as a property of "recording a result into a collection".
- Correct Thinking: every `res.add(new ArrayList<>(list))` costs O(list length),
  so total time is (number of results) x (result length), never just the node
  count.
- How to Avoid: standing complexity-checklist item — **"what does recording one
  answer cost?"** — asked on every enumeration problem before stating a bound.
- Pattern: cross-cutting
- Class: transfer gap (encoding-not-verified family)
- Recurrence: 4th transfer gap (DSU 08-07, fixed-window 08-11, template tie-rule
  08-27, this)
- Review Date: 2026-08-29

### 2026-08-28 — "I already solved this" as evidence (meta)
- Mistake: two problems declined on recall ("i think i have solved this prblm
  before") before any attempt. On the first, Frog Jump, the existing code
  contained an out-of-bounds crash and a wrong answer.
- Root Cause: coverage memory being treated as verified state — exactly what the
  2026-07-26 whole-sheet reclassification says it is not.
- Correct Thinking: the sheet was solved 2 years ago; every item is
  re-verification, and the only evidence that counts is code passing today.
- How to Avoid: when recall is offered instead of an attempt, ask for the code,
  not the memory. This session is the citable demonstration.
- Pattern: cross-cutting (process)
- Class: coverage-vs-verification
- Recurrence: 1st logged explicitly
- Review Date: n/a

### 2026-08-29 — Rat in a Maze: accept branch ran before its preconditions
- Mistake: the destination check was placed above the bounds/blocked check, so a
  blocked `(n-1,n-1)` was recorded as a valid path (`[[1,1],[1,0]]` returns a
  path where none exists).
- Root Cause: the accept branch was written as "am I at the goal?" without
  asking what it assumes about the cell it is standing on.
- Correct Thinking: every precondition the accept branch relies on must already
  be established when it runs. Here that means cell-is-open comes first. This is
  **not** "reject before accept" as a blanket rule — Combination Sum II needs the
  opposite order, because there the index bound is not a precondition of the sum.
- How to Avoid: at every terminal check, ask "what does this branch assume is
  already true?" and put those checks above it.
- Pattern: [[Backtracking]]
- Class: base-case ordering (3rd encounter: LC 40 08-29, flashcard 08-28, here)
- Recurrence: 3rd — and the first time the rule was actually spoken aloud
- Review Date: 2026-08-30

### 2026-08-29 — the fix that un-fixed itself (process)
- Mistake: defect above was first patched with `&& maze[m-1][n-1]==1` (silent, no
  rule named), and when told a cleaner fix existed the patch was **removed
  without performing the swap**, restoring the original bug.
- Root Cause: acting on the shape of the hint rather than on the defect —
  "remove the extra condition" was executed, "swap the blocks" was not.
- Correct Thinking: before changing code in response to a hint, restate the
  defect the change is supposed to remove, then check the edit actually removes
  it.
- How to Avoid: re-run the counterexample against the edited code before
  declaring it fixed. `[[1,1],[1,0]]` would have caught it in one trace.
- Pattern: cross-cutting (process)
- Class: silent fix (3rd: 08-25, 08-29 morning, here)
- Recurrence: 3rd
- Review Date: 2026-08-30

### 2026-08-29 — string-index vs grid structure (boundary, new)
- Mistake: LC 131 abandoned a second time ("i dont understand this prblm") after
  the concrete layer had already been derived correctly; in the same session
  N-Queens produced four cold correct derivations and Rat in a Maze produced
  correct code unaided.
- Root Cause: candidate boundary — problems whose state is a **position on a
  visible board** are being derived cold; problems whose state is an **index
  into a string** are not, even when the concrete enumeration is already done.
  LC 131's stall was exactly the step from `j = 0,1,2` on `"aab"` to `j` ranging
  over `i..n-1`.
- Correct Thinking: `s[i..j]` is the same object as a board coordinate; the
  substring is just a cell with two indices.
- How to Avoid: on string-index problems, draw the index line and label it the
  way a grid gets labelled, before generalizing.
- Pattern: cross-cutting
- Class: abstract-vs-concrete (extends the 08-27 physical/visual finding)
- Recurrence: 1st logged as a boundary; consistent with 08-26, 08-27
- Review Date: 2026-09-01

### 2026-08-29 — MENTOR ERROR: an inverted rule was affirmed
- Mistake: the user summarised the base-case rule as "reject before accept —
  same as LC 40" and this was accepted as correct. It is inverted with respect
  to LC 40, where `sum == target` must be checked **before** the index bound.
- Root Cause: the label matched the local fix, so it was not tested against the
  problem it was being generalized from.
- Correct Thinking: the transferable rule is about preconditions, not order;
  the order falls out differently per problem.
- How to Avoid: when a rule is stated as "same as <problem X>", check it against
  X before agreeing.
- Pattern: cross-cutting (mentor process)
- Class: mentor error
- Recurrence: 3rd logged mentor error (08-18 wrong statement, 08-27 over-drilling)
- Review Date: n/a

### 2026-08-29 — MENTOR ERROR: praise language
- Mistake: "Best question of the session" — user response: "dont do fakeness
  here like this one".
- Root Cause: default affirmation habit, not requested and not useful.
- Correct Thinking: signal is carried by the next question, not by praise.
- How to Avoid: **standing rule — no praise language.** Confirm correctness
  flatly ("correct", "that's it") and move.
- Pattern: cross-cutting (mentor process)
- Class: mentor error
- Recurrence: 1st
- Review Date: n/a

### 2026-08-29 — focus break ended the session early (process)
- Mistake: session ended at 48 of a booked 60 minutes. User's words: "i am not
  able to focus, someone was at the door and i felt the urge to check phone."
- Root Cause: one external interruption plus one internal pull, in an unprotected
  block. Second early end of the same day — the 13:49 session ran 47 of a booked
  120 ("i need a break"). 95 of 180 booked minutes used today.
- Correct Thinking: booked length has stopped predicting working time. A 60-min
  booking that reliably yields ~45 should be planned as ~45, or the block needs
  actual protection (phone out of reach, door handled beforehand).
- How to Avoid: candidate for the audit — either shorten the booked block to
  what actually gets used, or add a pre-session setup step. Do not keep sizing
  plans against a number that has missed twice in one day.
- Pattern: cross-cutting (process)
- Class: session hygiene
- Recurrence: 1st explicitly logged; 2nd early end on 2026-08-29 alone
- Review Date: n/a — take to `interview-prep-audit`

### 2026-08-30 — LC 17: empty input returns `[""]` instead of `[]`
- Mistake: base case fires at `index >= digits.length()` with `index=0, length=0`
  and records the empty string. Question asked 4 times before it was traced.
- Root Cause: base case treated as "recursion finished" without asking whether the
  path it finished on was ever a real path.
- Correct Thinking: `digits=""` is a **precondition on the input**, not a leaf of
  the search. Guard once in the caller, not per-leaf.
- How to Avoid: run the empty/zero-size input through the first call by hand before
  submitting. Standing test case for every recursion that records at a leaf.
- Pattern: [[Backtracking]]
- Class: edge case
- Recurrence: 1st
- Review Date: 2026-08-31

### 2026-08-30 — LC 17: string concatenation makes the space O(n²), not O(n)
- Mistake: space stated as `O(n)` for code carrying `res+c` down the recursion.
- Root Cause: recursion-depth heuristic applied without pricing what each frame
  holds. Java strings are immutable, so `res+c` is an allocation, not an append.
- Correct Thinking: one live root-to-leaf path holds strings of length
  `0,1,…,n` at once = `n(n+1)/2` = `O(n²)`. A `StringBuilder` with append/undo is
  one buffer, `O(n)`, and moves the copy to the leaf where it is the `· n` in
  `O(4^n · n)`.
- How to Avoid: at every recursion, ask what each **frame** holds, not just how
  many frames there are.
- Pattern: [[Backtracking]]
- Class: complexity
- Recurrence: 3rd of the copy-cost family (Subsets 08-28, Combination Sum 08-28)
  — **first one derived rather than nudged out**, closed by one 4-frame trace
- Review Date: 2026-08-31

### 2026-08-30 — LC 79: `dfs` called from only one start cell
- Mistake: `exist` called `dfs(...,0,0,0)` once. Any word not starting at `(0,0)`
  returns false.
- Root Cause: the recursion was written before the driver; the driver inherited
  the recursion's parameter list instead of being derived from the problem.
- Correct Thinking: the search has no given origin — every cell is a candidate
  start, so the driver loops over all of them.
- How to Avoid: after writing `dfs`, ask separately "who calls this first, and
  with what?" — the entry point is its own design decision.
- Pattern: [[Backtracking]]
- Class: coverage of search space
- Recurrence: 1st
- Review Date: 2026-08-31

### 2026-08-30 — LC 79: the fix matched the hint's shape, not the defect
- Mistake: told `|` vs `||`, changed the operator on `return down||left||right||up`
  while the four `dfs` calls stayed as eager assignments on the lines above. No
  short-circuiting happened. The mechanism was explained correctly *before* the
  fix ("the other three subtrees still run, at every level") and the fix still
  missed.
- Root Cause: the edit targets the token the hint named rather than the behaviour
  the hint described.
- Correct Thinking: assignment forces evaluation; `||` can only skip operands it
  has not yet computed. The short-circuit must be in the call chain.
- How to Avoid: **after any hint-driven edit, re-run the original counterexample
  against the new code.** Written as a prediction on 2026-08-29; fired here.
- Pattern: cross-cutting (debugging process)
- Class: hint-shape matching
- Recurrence: **2nd** (1st: Rat in a Maze 2026-08-29, patch reverted without the swap)
- Review Date: 2026-08-31

### 2026-08-30 — LC 79: path mark deleted, then silently restored
- Mistake: `board[i][j]=cur` commented out, then put back in the next paste with
  the symptom question left unanswered. Same question was declined on Rat in a
  Maze on 2026-08-29.
- Root Cause: fixing by reverting rather than by naming what breaks.
- Correct Thinking: the mark means **"on the current path"**, not "visited ever".
  It is path state, so it is undone on the way out. Counterexample that shows it:
  `[["A","B"],["A","D"]]`, `"AAB"` — `(0,0)` is left poisoned by a failed start
  and the true path's *second step* dies.
- How to Avoid: never revert a line to fix a bug — state the symptom of removing
  it first. Same silent-fix pattern logged 08-25 and 08-29.
- Pattern: [[Backtracking]]
- Class: silent fix / visited-timing
- Recurrence: 3rd silent fix (08-25, 08-29, 08-30); the visited-timing question
  itself is 2nd (declined 08-29, answered 08-30)
- Review Date: 2026-08-31

### 2026-08-30 — LC 216: reject guard left a hole
- Mistake: `if (cnt==k && sum<n || cnt<k && sum>=n) return;` never catches
  `cnt==k && sum>n`, so the search recurses with `cnt` past `k`, recording
  nothing, until `i` runs out at 9.
- Root Cause: guard written by enumerating the failure cases that came to mind
  rather than by complementing the accept condition.
- Correct Thinking: once the accept check above has taken `cnt==k && sum==n`,
  everything with `cnt==k` or `sum>=n` is dead — `cnt==k || sum>=n`.
- How to Avoid: write the reject guard as the **complement of the accept**, then
  trace one input that satisfies neither.
- Pattern: [[Backtracking]]
- Class: pruning / correctness-adjacent waste
- Recurrence: 1st
- Review Date: 2026-08-31

### 2026-08-30 — LC 216: pruning at `sum >= n` justified by the condition, not the reason
- Mistake: asked why pruning at `sum == n` with `cnt < k` is safe, answered
  "i didnt get it", then after the concrete instance answered with the condition
  restated (`cnt<k && sum>=n`) rather than the reason.
- Root Cause: the justification weakness on **abstract monotonicity** — the same
  boundary logged 08-27 (physical/visual reasons come cold, counting/abstract ones
  do not).
- Correct Thinking: all candidates are positive, so `sum` increases monotonically
  down a path; a prefix already at `n` with picks owed can never return to `n`.
  **The prune is invalid the moment 0 or negatives are allowed.**
- How to Avoid: for any prune, name the property of the input that licenses it,
  then name the input that would break it.
- Pattern: [[Backtracking]]
- Class: justification (abstract mechanism)
- Recurrence: consistent with the 08-27 physical-vs-abstract split
- Review Date: 2026-08-31

### 2026-08-30 — leech recall declined for the 2nd consecutive session (process)
- Mistake: the leech drill was proposed as the opening block and declined again
  ("we will solve new probs"). 11th consecutive zero-review session; 6th
  consecutive weekend at zero; the three `[leech]` items are now 17 days without
  their mandated daily recall.
- Root Cause: coverage is chosen over retention every time the choice is offered,
  including on days the plan reserves for reviews.
- Correct Thinking: the plan's own weekend policy is reviews-only. Offering the
  choice each session is producing the same answer each session.
- How to Avoid: **take to the audit** — either the weekend-only review policy is
  real and the drill is not optional, or the policy should be rewritten to match
  what actually happens. The current state is a plan that has not been executed
  for 11 sessions running.
- Pattern: cross-cutting (process)
- Class: plan adherence
- Recurrence: 11th zero-review session; 2nd explicit decline of the drill
- Review Date: n/a — take to `interview-prep-audit`

### 2026-08-30 21:15 — LC 216 `sum>=n` review question, 3rd asking, closed
- Mistake: n/a — this entry updates the 2026-08-30 LC 216 entry above. The
  same question, asked a 3rd time inside the new opening-review mechanism,
  closed via 3-step guided derivation (never handed over) — first clean
  closure of this specific point after 2 straight handovers same day.
- Root Cause: n/a (resolution entry).
- Correct Thinking: framing as "can this branch ever recover" (not "what's
  the rule") let the user derive it stepwise instead of pattern-matching a
  rule they'd already failed to state twice.
- How to Avoid: n/a.
- Pattern: [[Backtracking]]
- Class: justification (abstract mechanism) — resolved
- Recurrence: 3rd occurrence of this exact point, 1st clean-via-derivation
- Review Date: 2026-09-06 (confirm it survives a week, not just same-day)

### 2026-08-30 21:12 — Task Scheduler (leech recall) — "solved before" decline
- Mistake: opened the leech recall with "i think i have solved this before"
  and no attempt — same phrase that preceded Frog Jump sitting 7 weeks as a
  false "solved" entry with a live crash bug.
- Root Cause: a problem being previously attempted is being read as evidence
  of retention, which the `[leech]` tag itself exists to contradict (this item
  needed 3+ corrections on the same point historically).
- Correct Thinking: `[leech]`/prior-attempt status is a *reason to check*, not
  a reason to skip. The recall this time was in fact clean.
- How to Avoid: treat "I think I solved this before" as the leech drill's own
  trigger, not a valid decline reason — named directly in-session.
- Pattern: cross-cutting (process)
- Class: stale-recall
- Recurrence: 2nd (1st: Frog Jump, 2026-08-28 discovery)
- Review Date: n/a — process note

### 2026-08-31 — Word Break (LC 139) / N-Queens (LC 51) — greedy-first-match
- Mistake: on both problems the opening algorithm took the first choice that
  passed a local check and advanced, with no branch and no undo — Word Break
  advanced `start` on the first dictionary hit; N-Queens placed a queen in the
  first non-attacked column of each row.
- Root Cause: "this choice is legal here" is being read as "this choice is
  correct", so the search never gets built. Not a string-index problem — the
  08-30 boundary was about *where a piece ends*; this is one level up and
  applies to grids too.
- Correct Thinking: a local legality test tells you a branch is worth
  exploring, not that it is the branch. Every legal option at a level is a
  child; failure below must return and try the next one.
- How to Avoid: before writing the loop, ask "if this choice dead-ends three
  levels down, what line brings me back here?" No answer means no backtracking.
- Pattern: [[Backtracking]]
- Class: algorithm-structure
- Recurrence: 2nd occurrence inside one session (LC 139 16:26, LC 51 17:08)
- Review Date: 2026-09-01

### 2026-08-31 — Word Break (LC 139) — memo key never matched its lookup
- Mistake: looked up `map.get(start+"-"+index)` but on success stored
  `map.put(start+"-"+i, true)` after reassigning `key`. Lookups are always of
  the form `"k-k"` (since `index==start` always), so no `true` was ever read
  back — only failures were memoized.
- Root Cause: the memo key was built from two variables without checking
  whether both carry information, and the write key was edited independently of
  the read key.
- Correct Thinking: the memo key must be exactly the state the function is
  parameterized by. Here that is one integer, so `Boolean[n]`, not a string
  concatenation of a value and its own duplicate.
- How to Avoid: write the read key and the write key as one variable, assigned
  once at the top, never reassigned. If a key needs two parts, prove the second
  part can differ from the first.
- Pattern: [[Backtracking]] / memoization
- Class: correctness-adjacent (cost bug — right answer, dead cache)
- Recurrence: 1st
- Review Date: 2026-09-01

### 2026-08-31 — hint-shape matching, 4th occurrence
- Mistake: after each hint, the edit changed the surface detail the hint
  displayed rather than the defect it named. (a) N-Queens: shown a 5-character
  row string, added an `else` and left the `res` shape untouched — the question
  had been about `res`. (b) LC 46: told two precedence bugs existed, fixed the
  one the compiler pointed at and left `goalMask` alone. (c) it recurred after
  being named aloud mid-session.
- Root Cause: the hint's example is being treated as the specification of the
  fix. Same mechanism as 2026-08-29 (Rat in a Maze) and 2026-08-30 (LC 79).
- Correct Thinking: an example illustrates the defect; the defect is what the
  sentence says. Re-read the question after the edit and check it is answered.
- How to Avoid: the 08-30 prescription (re-run the counterexample before
  declaring a fix) has now failed to fire three sessions running. Stronger and
  narrower: **after any hint-driven edit, restate the defect in one sentence
  before pasting the code.** If it can't be stated, the edit isn't the fix.
- Pattern: cross-cutting (process)
- Class: hint-shape matching
- Recurrence: 4th (08-29, 08-30, and twice on 08-31)
- Review Date: 2026-09-01

### 2026-08-31 — silent fixes, 5th occurrence
- Mistake: both LC 139 rewrites (the `Boolean[n]` memo, the `else` on the
  N-Queens string) arrived as clean pastes with no statement of what had been
  wrong; the defects were only spoken after being asked directly, one of them
  needing four escalations and an analogy.
- Root Cause: the code compiling is being treated as the end of the loop.
- Correct Thinking: a fix isn't done until the defect can be named. That
  naming is what transfers to the next problem — the fix does not.
- How to Avoid: paste the fix *with* the one-line defect statement attached,
  in the same message.
- Pattern: cross-cutting (process)
- Class: silent-fix
- Recurrence: 5th (08-25, 08-29, 08-30, 08-31 x2)
- Review Date: 2026-09-01

### 2026-08-31 — Permutations (LC 46) — Java operator precedence
- Mistake: `mask&(1<<i)==0` (compile error: `==` binds tighter than `&`) and
  `1<<(n+1)-1` (evaluates as `1<<n`, so `goalMask` was 8 not 7 at n=3 and the
  accept branch could never fire).
- Root Cause: bitwise operators sit *below* comparison and arithmetic in Java's
  precedence table, which is the opposite of how they read left to right.
- Correct Thinking: `&`, `|`, `^`, `<<`, `>>` are all lower than `==`, `+`,
  `-`. Any mixed expression needs explicit parentheses.
- How to Avoid: parenthesize every bitwise sub-expression on sight —
  `((mask & (1<<i)) == 0)`, `((1<<n) - 1)`. Never rely on the table.
- Pattern: [[Backtracking]] / bitmask
- Class: language-mechanics
- Recurrence: 1st
- Review Date: 2026-09-03

### 2026-09-01 — Sudoku Solver (LC 37) — row-major index flattening
- Mistake: could not derive `box = (r/3)*3 + c/3`; separately coded the cell
  stride as `i*3+j` on a 9-wide grid, so `(0,4)` advanced to `(1,2)`.
- Root Cause: `(r/3)*3` read as cancelling back to `r` — integer truncation not
  applied. Row-major flattening treated as something to recall, not derive.
- Correct Thinking: `r/3` truncates to the band index, `*3` re-expands to that
  band's first row, so they do not cancel (`r=7` -> `2` -> `6`). Row-major:
  `index = row*width + col`, width 9 for cells, 3 for boxes.
- How to Avoid: on any grid problem write `width` down first and derive the
  flatten/unflatten pair before the loop; verify on two cells (`(7,8)`, `(3,0)`).
- Pattern: [[Backtracking]] / grid indexing
- Class: arithmetic-derivation
- Recurrence: 1st named — but two instances in one session (box index, cell stride)
- Review Date: 2026-09-02

### 2026-09-01 — Single Number II (LC 137) — derivation-to-code regression
- Mistake: derived "count the 1s per bit, mod 3" aloud and by hand on the binary
  columns, then wrote `freq[i]%2` two minutes later. Also `i<<1` for `1<<i`.
- Root Cause: code produced from the neighbouring problem's template — LC 136,
  solved 10 minutes earlier, is mod-2 cancellation — rather than from the
  sentence just spoken.
- Correct Thinking: the derived predicate is the specification; the previous
  problem's shape is not evidence about this one.
- How to Avoid: the standing 08-31 prescription — write the derived predicate as
  the **first** line of code, before the surrounding structure. Not run here, not
  run on 08-31.
- Pattern: cross-cutting (process)
- Class: transfer-gap
- Recurrence: 2nd (08-31 M-Coloring `i != prvNodeColor`); interval is minutes both times
- Review Date: 2026-09-02

### 2026-09-01 — Sudoku Solver (LC 37) — hint-shape matching
- Mistake: two defects named in one message (undo's `cols[i]`, and
  `board[i][j]=(char)val`); fixed the first, pasted, left the second untouched.
- Root Cause: acts on the item pointed at a specific token; the second item was
  described rather than pointed at.
- Correct Thinking: a message naming N defects needs N fixes, or an explicit
  "I don't see the second one".
- How to Avoid: count the defects named before pasting; one line per fix saying
  what it fixes (this is gate 3, and it went unrun 3 times today).
- Pattern: cross-cutting (process)
- Class: hint-shape-matching
- Recurrence: 5th (08-29, 08-30, 08-31 x2, 09-01)
- Review Date: 2026-09-02

### 2026-09-01 — Sudoku Solver (LC 37) — a query that mutates
- Mistake: `isValid` returned a boolean **and** wrote the digit and set three
  trackers; the matching undo lived in `dfs`'s else-branch.
- Root Cause: place and undo split across two functions, so the pairing is
  invisible at both sites.
- Correct Thinking: the predicate reads only; `dfs` does place -> recurse -> undo
  on three adjacent lines. Any future call site that only wants to *check*
  silently corrupts state otherwise — user reached this once asked what the board
  looks like after such a call.
- How to Avoid: if a function's name asks a question, it must not write.
- Pattern: [[Backtracking]] / code hygiene
- Class: design
- Recurrence: 1st (relative of the 08-31 vestigial `prvNodeColor` guard, which
  survived because state changes were scattered)
- Review Date: 2026-09-04

### 2026-09-01 — Single Number (LC 136) — why the XOR fold may be reordered
- Mistake: knew "same values cancel" but could not name what lets two duplicates
  separated by other elements be brought together.
- Root Cause: the cancellation fact is stored; the algebraic licence for
  reordering a left-to-right fold is not.
- Correct Thinking: three facts, all needed — `x^x=0`, `x^0=x`, and
  commutativity + associativity. `((((4^1)^2)^1)^2)` only becomes
  `4^(1^1)^(2^2)` because operands may be moved and re-bracketed. `-` and `/`
  have neither law, which is why no such trick exists for them.
- How to Avoid: for any fold-the-whole-array trick, state which operator laws
  make evaluation order irrelevant before claiming the cancellation.
- Pattern: bit tricks
- Class: knowledge-gap
- Recurrence: 1st
- Review Date: 2026-09-03

### 2026-09-02 17:46 — Single Number III (LC 260) — "either" instead of "exactly one"
- Mistake: asked what a set bit of `x^y` means for x and y, answered "either of
  those elements was having a set bit" — true but not the load-bearing fact.
- Root Cause: recalled that the bit distinguishes them, not the precise XOR
  semantics (exactly one of the two operands has it set).
- Correct Thinking: a set bit in `x^y` means x and y disagree there — exactly
  one has it. That's what licenses splitting the whole array into two groups
  where duplicate pairs always land together and x, y always land apart.
- How to Avoid: when reasoning from an XOR result bit, state "exactly one of"
  explicitly rather than "either" — the loose form doesn't rule out "both".
- Pattern: bit tricks / [[BitCountingModK]]
- Class: knowledge-gap
- Recurrence: 1st
- Review Date: 2026-09-03

### 2026-09-02 17:46 — Power of Two (LC 231) — bit-count check missed a sign edge case
- Mistake: `n & (n-1) == 0` guarded only against `n == 0`, not negative n.
  `Integer.MIN_VALUE` has exactly one set bit (the sign bit) and passed as a
  false positive.
- Root Cause: the single-set-bit check was derived correctly in the positive
  domain; the two's-complement sign-bit case was never considered before
  writing the guard.
- Correct Thinking: "exactly one set bit" bit-tricks only mean "power of two"
  when the number is also known positive — guard with `n <= 0`, not `n == 0`.
- How to Avoid: for any single-set-bit check on a signed int, test
  `Integer.MIN_VALUE` explicitly before declaring the guard sufficient.
- Pattern: bit tricks
- Class: boundary
- Recurrence: 1st
- Review Date: 2026-09-03

### 2026-09-03 17:34 — Single Number III (LC 260) review #1 — split-rule imprecision recurred
- Mistake: asked to restate the split rule precisely, said "one bit set in one
  of them, another is uncertain" — same imprecision as the original solve's
  "either" (should be "exactly one, the other is 0, for certain").
- Root Cause: the mechanism (XOR-all, split by a bit) is solid, but the exact
  claim about the *other* number at that bit position was never pinned down
  hard enough to survive a day.
- Correct Thinking: at the bit chosen from x^y, exactly one of x,y has it set
  and the other has it clear — known, not uncertain.
- How to Avoid: when restating a split/XOR rule, state the claim about *both*
  sides of the split explicitly, not just the side that's set.
- Pattern: bit tricks
- Class: stale-recall
- Recurrence: 2 (same precision point as the 2026-09-02 original-solve mistake)
- Review Date: 2026-09-06

### 2026-09-03 17:34 — Single Number III (LC 260) review #1 — any-bit generality not derived unaided
- Mistake: asked why any set bit of x^y works (not just MSB), first answer
  defended MSB specifically; re-aimed to "any bit", got "yes" with no reason;
  needed a second push before naming the reason.
- Root Cause: MSB was memorized as *the* choice from the original solve
  rather than understood as one instance of a general property.
- Correct Thinking: any set bit of x^y is a position where x and y differ, so
  splitting on it always separates x from y; duplicate pairs agree at every
  bit and cancel identically inside whichever group they land in.
- How to Avoid: after deriving a specific-instance rule, test it against a
  non-standard instance (e.g. a non-MSB bit) before calling it understood.
- Pattern: bit tricks
- Class: invariant-why
- Recurrence: 1st
- Review Date: 2026-09-06

### 2026-09-03 17:34 — Power of Two (LC 231) review #1 — Integer.MIN_VALUE still not recalled
- Mistake: asked to name the specific negative value with exactly one set bit;
  restated the fix ("n<=0 return false") instead, then "I don't have any
  idea" when pushed for the value itself. Session ended mid-escalation
  (32-bit sign-bit hint given, unanswered) — review #1 left incomplete.
- Root Cause: same gap as the original 2026-09-02 solve — the guard's fix was
  learned, the specific counterexample driving it was not.
- Correct Thinking: Integer.MIN_VALUE (`-2147483648`) is `1000...0` in 32-bit
  two's complement — one set bit (the sign bit), so `n & (n-1) == 0` passes it
  despite being negative.
- How to Avoid: for any single-set-bit bit trick on a signed int, keep
  Integer.MIN_VALUE as the standing counterexample to name, not just the fix.
- Pattern: bit tricks
- Class: stale-recall
- Recurrence: 2 (same point as the 2026-09-02 original-solve mistake, unresolved)
- Review Date: 2026-09-04

### 2026-09-03 21:18 — Course Schedule (LC 207) — indegree wired to the wrong node, code arrived with no approach spoken
- Mistake: code pasted cold with no approach given first; `indegree[pre[1]]++`
  incremented the prerequisite node instead of the dependent node
  (`indegree[pre[0]]++`). Bug found via a 2-node trace requested by the
  mentor, then fixed and re-pasted silently — defect only stated once asked
  directly to restate it.
- Root Cause: `graph[pre[1]].add(pre[0])` (edge direction) was derived
  correctly, but indegree ownership was not separately reasoned about before
  writing it — copied the same index used for the edge without asking which
  node the count actually belongs to.
- Correct Thinking: edge `b -> a` means indegree belongs to `a` (the
  dependent, the node that can't run until `b` is done), not `b`.
- How to Avoid: after wiring an edge, ask explicitly "whose count does this
  edge affect" before touching `indegree[]` — don't reuse the edge's index
  variable by default.
- Pattern: [[TopologicalSort]]
- Class: code-vs-derivation
- Recurrence: 1 (first on Graph topic; same family as the bucket-2
  derivation-to-code regressions logged repeatedly 08-28..09-01)
- Review Date: 2026-09-06

### 2026-09-05 13:15 — Alien Dictionary (LC 269) — approach not recalled despite "solved before"
- Mistake: named "topological sort" as the category cold, but couldn't
  rebuild the edge-extraction step (compare adjacent words, first differing
  char = edge) unaided.
- Root Cause: category recalled, mechanism not — same shape as prior
  "I think I've solved this before" declines that turned out to hide a real
  gap (Frog Jump, Task Scheduler).
- Correct Thinking: adjacent-word comparison only; non-adjacent pairs are
  redundant since the list is already sorted (transitivity covers them).
- How to Avoid: naming the category is not evidence of retrieval — always
  ask for the mechanism before treating "seen this before" as coverage.
- Pattern: [[TopologicalSort]]
- Class: stale-recall
- Recurrence: 3 (same "solved before" mismatch class as Frog Jump 08-28,
  Task Scheduler 08-30)
- Review Date: 2026-09-08

### 2026-09-05 13:35 — Alien Dictionary (LC 269) — cast-precedence bug, wrong char written
- Mistake: `sb.append((char)cur+'a')` — cast bound to `cur` alone
  (`((char)cur)+'a'`), producing `char+char=int`; `append(int)` wrote digits
  instead of the letter.
- Root Cause: treated `(char)` as if it applied to the whole expression
  following it, not just the next operand — same binding rule as unary
  minus, not checked against it.
- Correct Thinking: unary operators (cast included) bind only to the
  immediate operand; parenthesize the arithmetic first: `(char)(cur+'a')`.
- How to Avoid: whenever casting the result of an expression, write the
  parens around the expression explicitly rather than trusting precedence.
- Pattern: [[TopologicalSort]]
- Class: language-mechanics
- Recurrence: 1
- Review Date: 2026-09-08

### 2026-09-05 13:38 — Alien Dictionary (LC 269) — prefix length-check ran before character scan
- Mistake: `compareWords` returned invalid whenever `slen<flen`, before
  scanning for a differing character — wrongly rejected valid pairs like
  `"ba"`/`"a"` (differ at index 0, a real edge) as if they were an invalid
  prefix case.
- Root Cause: the two exit conditions (found a difference / ran out with no
  difference) were not kept in the right precedence — the length-based one
  was checked as a fast-path before the loop that actually finds
  differences.
- Correct Thinking: the length check is only meaningful *after* the scan
  finds no differing character at all (true prefix relationship); it must
  run after the loop, not before it.
- How to Avoid: for any "compare then classify by length" logic, run the
  general-case scan first and use length only to interpret a scan that found
  nothing.
- Pattern: [[TopologicalSort]]
- Class: boundary
- Recurrence: 1
- Review Date: 2026-09-08

### 2026-09-05 13:41 — Alien Dictionary (LC 269) — cycle-check counter counted occurrences, not distinct letters
- Mistake: `cntr` incremented once per character across every word
  (including repeats), then compared to 0 after decrementing once per
  distinct letter popped from the BFS — the counts were never on the same
  scale, so the check almost never passed even on valid input.
- Root Cause: copied the "count processed nodes" shape from Course Schedule
  II without checking what "a node" means in this problem (a distinct
  letter, not a character occurrence).
- Correct Thinking: snapshot `indegree[i]==0` across all 26 slots right
  after marking present letters, before any edges are added — that counts
  distinct letters exactly once each.
- How to Avoid: when transferring a "count == total nodes" check to a new
  problem, re-derive what a node is in the new problem before reusing the
  counting method.
- Pattern: [[TopologicalSort]]
- Class: transfer-gap
- Recurrence: 1
- Review Date: 2026-09-08

### 2026-09-05 13:55 — Number of Enclaves (LC 1020) — visited marked at pop instead of push, TLE
- Mistake: `grid[cur[0]][cur[1]]=2` ran at dequeue time; a cell already
  sitting in the queue (still marked `1`) could be discovered and re-enqueued
  by more than one neighbor before it was ever popped.
- Root Cause: the visited-at-push rule for BFS was already written in
  `topics/Graph.md`'s Common Mistakes section (since 2026-07-25, recurred
  3rd time on Flood Fill) but not applied before writing this code.
- Correct Thinking: mark visited the moment a cell is added to the queue,
  not when it's removed — prevents the same cell being queued more than
  once.
- How to Avoid: for any new BFS, check the mark-visited line's position
  against the written rule before running it, not after a TLE.
- Pattern: Graph Traversal (BFS visited-at-push) — see `../topics/Graph.md`
  Common Mistakes
- Class: transfer-gap
- Recurrence: 4th (2026-07-25 original, recurred on Flood Fill 2026-07-25,
  now here) — first time it actually failed a run instead of self-catching
- Review Date: 2026-09-08

