---
type: progress
updated: 2026-08-30
---

# Progress Tracker

## Current Position

**Major correction (2026-07-26)**: user confirmed the **complete Striver A2Z
sheet (all 455) was solved ~2 years ago**. The 2026-07-10 Codolio import's
42.86% and per-topic percentages below reflect only a **2-3-month-ago
re-solve pass**, not the true baseline — they undercount actual lifetime
coverage. Correct framing for the ENTIRE sheet, no exceptions: **rusty
2-year recall, re-verification task everywhere, no topic is genuinely new**.
This supersedes the "confirmed real gaps" / "confirmed not started" language
below (kept for history) — treat every topic, including Arrays/Recursion/
Bit-Manipulation/Strings/Basics/Sorting, the same rusty-not-safe way as
Binary Search/DP/etc., just with a longer (2yr vs 2-3mo) decay window.
Evidence: Dijkstra (2026-07-26, previously "0%") came out cold/clean on core
mechanics — a recall pattern, not first-exposure.

- **Sheet**: Striver A2Z
- **Overall**: 195/455 (42.86%) solved, per Codolio import on 2026-07-10 (raw file
  archived at `../codolio_import_raw.json`). This is **not** a fresh start.
- **Confirmed complete (100%)**: Binary Search (32/32), LinkedList (31/31), BST (16/16).
- **Confirmed near-complete**: Trees (36/39, 92%), Tries (6/7, 86% — 1 known gap:
  Maximum XOR With an Element From Array), DP (44/56, 79% — 12 unverified gaps in
  un-itemized later lectures).
- **Retention risk (user-confirmed, 2026-07-10)**: all six of the above (Binary Search,
  LinkedList, BST, Trees, Tries, DP) were solved **2–3 months ago**, not recently — no
  practice since. "100%/near-100% complete" describes coverage, not current recall.
  Treat as **rusty, not safe** — genuine interview-speed re-verification needed early
  (Week 1), not a light Week 3 warm-up. If gaps show up on re-test, that's new signal,
  log it as a fresh mistake, not evidence the import was wrong.
- ~~Confirmed real gaps~~ **reclassified 2026-07-26 — actually rusty 2yr recall,
  not gaps**: Arrays (2/40, 5%), Recursion (2/25, 8%), Bit Manipulation (1/18, 6%),
  Strings (3/15, 20%), Basics (0/31), Sorting (0/7) — solved 2 years ago, Codolio
  just never captured a recent re-solve pass for these.
- ~~Confirmed not started~~ **reclassified 2026-07-26 — actually rusty 2yr recall,
  not ground-up**: Stack/Queue, Sliding Window, Heaps, Greedy, Graphs, and the
  sheet's final section — 2026-07-10 "not covered at all" confirmation superseded;
  user solved these 2 years ago. Re-verification task, expect faster core-mechanics
  recall than true first exposure (confirmed by Dijkstra 2026-07-26 performance).
  **Graphs still gets priority time** given interview weight, but framed as
  decay-repair, not new-topic teaching.

## Import History (2026-07-10)

Two Codolio export attempts were combined:
1. A chat-pasted export that truncated at the same point 3 times, giving full detail
   for Steps 1–8 (Basics, Sorting, Arrays, Binary Search, Strings, LinkedList,
   Recursion, Bit Manipulation).
2. A file export (`~/Downloads/codolio_dsa_progress.json`, archived at
   `../codolio_import_raw.json`) that added Steps 13, 14, 16, 17 (Trees, BST, DP,
   Tries) but itself only fully itemized some lectures within each topic (e.g. BST is
   fully itemized; Trees/DP/Tries have solid aggregate topic-level percentages but
   incomplete per-problem lists beyond the first lecture or two).

Per-question `solved` flags were internally consistent (individual flags summed to the
topic total) for: Binary Search, LinkedList, BST, Strings, Recursion, Tries. **Not
consistent for Arrays** (topic said 2 solved, no individual question flagged true) — the
exact 2 solved Array problems are unknown. Trees and DP have partial itemization only
(later lectures' individual problems unknown even though aggregate % is solid).

User confirmed on 2026-07-10 that the missing cluster (Stack/Queue, Sliding Window,
Heaps, Greedy, Graphs, final section) simply wasn't covered — no further export needed,
treat as 0% and plan real learning time, not verification.

## Completed Problems

_Full problem-level log lives in `../topics/*.md` per topic. Going forward, each newly
completed or newly-confirmed problem is appended to its topic file, and significant
ones logged here as:_

`- [ ] Problem Name — Topic/Subtopic — Difficulty — [note](../notes/problem-slug.md) — solved: independently | with-hints:N | failed`

- [ ] Non-overlapping Intervals (LC 435) — Greedy/Intervals — Medium — solved: with-hints:1
- [ ] Number of Substrings Containing All Three Characters (LC 1358) — SlidingWindow/At-most-K — Medium — solved: independently
- [ ] Binary Subarrays With Sum (LC 930) — SlidingWindow/At-most-K — Medium — [note](../notes/binary-subarrays-with-sum.md) — solved: with-hints:1 (2026-08-25; approach cold 2026-08-23, code written 2026-08-25) — complexity + edge case **never stated**, invariant **never spoken**
- [ ] Asteroid Collision (LC 735) — Stack/Simulation — Medium — [note](../notes/asteroid-collision.md) — solved: with-hints:4 (2026-08-24; failed cold 2026-08-23, closed on re-attempt)
- [ ] Trapping Rain Water (LC 42) — Stack/Queue section (solved via prefix-max arrays, no stack) — Hard — [note](../notes/trapping-rain-water.md) — solved: with-hints:5 (2026-08-26) — code cold and correct first submit; O(n)/O(n) + edge cases + the *why* all stated, first fully-spoken solve in 5 sessions
- [ ] Trapping Rain Water (LC 42) — O(1)-space follow-up — Hard — [note](../notes/trapping-rain-water.md) — solved: with-hints:6 (2026-08-27) — **derivation clean, assembly failed**: lower-bound argument (`leftMax < rightMax <= trueRightMax`, so the unseen middle can't matter) derived cold across 5 questions, then code was requested outright rather than attempted
- [ ] Largest Rectangle in Histogram (LC 84) — Stack/MonotonicStack — Hard — solved: with-hints:2 (2026-08-27) — approach, `nsr-nsl-1` width formula and the justification ("taller bars can be cut down to h[i], shorter ones can't") all **cold**; code correct first attempt, O(n)/O(n) + amortized argument cold. Java `Stack` vs `ArrayDeque` unknown
- [ ] Sum of Subarray Minimums (LC 907) — Stack/MonotonicStack/Contribution — Medium — [note](../notes/sum-of-subarray-minimums.md) — solved: with-hints:4 (2026-08-27) — contribution technique named cold, but **two defects**: duplicate double-count (strict `<=` on both sides) and int overflow with `mod` declared-and-unused. Endpoint counting needed enumeration
- [ ] Daily Temperatures (LC 739) — Stack/MonotonicStack — Medium — solved: independently (2026-08-27) — cold, first submit, Accepted 0 ms; `>=` pop condition correct and justified unprompted ("warmer is strict, so equals must go")
- [x] Frog Jump (DP-3) — DP/1D DP — Medium — [note](../notes/frog-jump-dp-3.md) — solved: with-hints:2 (2026-08-28) — **07-10 follow-ups finally closed after 7 weeks**: n=1 (returns 0, recurrence never runs), n=2 (peel `dp[1]`, loop from i=2), O(n)/O(n) with reasons cold, then O(1)-space code written and Accepted. Two live defects found in the process — `dp[i-2]` out of bounds at i=1 (would crash every n>=2 input, so the 07-10 "corrected recurrence" had never been run on a judge), and a wrong roll `backbytwo=oneStep` (a dp value plus a jump cost, not a dp value)
- [ ] Subsets (LC 78) — Recursion/Backtracking — Medium — solved: independently (2026-08-28) — **cold, first attempt, correct**: take/not-take with a proper undo and a deep copy on `res.add`. 2^n justified cold on the 2nd ask ("each element has a choice"). Complexity O(2^n) needed one nudge at the copy line to become O(n·2^n); auxiliary-vs-output distinction correct
- [ ] Combination Sum (LC 39) — Recursion/Backtracking — Medium — [note](../notes/combination-sum.md) — solved: with-hints:2 (2026-08-28) — **over-generating branch masked by a `HashSet`**: three recursive calls where two suffice (take-then-move-on is take-stay followed by skip), so duplicates were filtered after the fact instead of never being produced. Also `Set.asList()` (does not exist). Redundant branch not identified when asked; trace requested, then "just tell me"

- [ ] Combination Sum II (LC 40) — Recursion/Backtracking — Medium — [note](../notes/combination-sum-ii.md) — solved: with-hints:6 (2026-08-29) — **both defects were already written down in the tracker the previous night**: base cases ordered `index>=nums.length` before `sum==target` (drops any exact hit landing on the last index — `[5]` in example 2), the exact case of the 08-28 flashcard; and `Set<List<Integer>> res` again, one day after that became the top pitfall in `../patterns/Backtracking.md`. Dedup-on-decline took the full escalation ladder (1 "just tell me", 2 "i didnt get it", closed by guided trace). Complexity `O(2^n)` → `O(n·2^n)` needed the same copy-cost nudge as Subsets 1 day earlier
- [ ] Subsets II (LC 90) — Recursion/Backtracking — Medium — solved: independently (2026-08-29) — **cold, correct first submit, skip-on-decline transferred with no prompt 5 min after LC 40 needed six escalations for it**. `O(n·2^n)` stated cold with no nudge — the copy-cost gap closed inside 6 minutes. Space `O(n)` correct. Open: why `Arrays.sort` is required needed 3 escalations and ended in "just tell me" — named the symptom ("won't get unique subsets"), not the mechanism (`while` compares only adjacent elements)
- [ ] Palindrome Partitioning (LC 131) — Recursion/Backtracking — Medium — **OPEN, approach only, no code written (2026-08-29)** — session ended mid-derivation. Two corrections landed: claimed both left and right pieces must be palindromes (self-corrected in 1 counterexample — only the left piece is tested, the remainder is recursed on), and gave "a single char is a palindrome" when asked for the recursion's record base case (closed by analogy to LC 90's `index == nums.length`). Stopped at: how many children a node at `i` has, and what distinguishes them. **Reopened 2026-08-29 16:05 and abandoned a 2nd time (~12 min, no code).** The concrete layer worked: all 4 cuts of `"aab"` enumerated, the 2 dead ones killed with the right reason (`ab`, `aab` not palindromes), and grouping by first piece produced the child set (`a`, `aa`, `aab`) mapped to `j = 0,1,2`. Generalizing `j` to the range `i..n-1` did not land — "i dont understand this prblem, can we do something else". Both abandonments are "I don't understand", never a wrong answer
- [ ] Rat in a Maze (GFG) — Recursion/Backtracking/Grid — Medium — [note](../notes/rat-in-a-maze.md) — solved: with-hints:4 (2026-08-29) — **code arrived with no approach ~13 min after the approach-first rule was stated for this session**. Final code correct on review; never confirmed on the judge. Two defects. (1) The destination check ran *before* the bounds/blocked check, so a blocked `(n-1,n-1)` was still recorded as a path. Fix sequence is the finding: silent patch (`&& maze[m-1][n-1]==1`, rule unnamed) -> **patch reverted without swapping the blocks, reintroducing the bug** -> correct swap. The rule was finally spoken on the 3rd encounter, after a targeted question about what the accept branch assumes. (2) Recursion order `D,R,L,U` not lexicographic, fixed to `D,L,R,U` on one prompt. Complexity, the `maze[curx][cury]=1` restore and a dead `StringBuilder` were all declined ("lets move")
- [ ] N-Queens (LC 51) — Recursion/Backtracking — Hard — [note](../notes/n-queens.md) — **OPEN, approach only, no code (2026-08-29)** — **approach stated before code for the first time in 3 sessions, unprompted.** Four derivations cold and correct in a row: one queen per row, so the choice at each level is a column; the row check is free by construction while column and both diagonals are not; `r+c` constant along `/`; `r-c` constant along `\`. Missed column 3 in the first legality enumeration from `(0,0)`, corrected in 1 question. "why not just one oprn?" was the user's own question and the user closed it themselves by computing `r+c` down the `\` diagonal (`0,2,4,6`, not constant). Stopped at: shifting `r-c` (spans `-(n-1)..n-1`) into a non-negative array index
- [x] Letter Combinations of a Phone Number (LC 17) — Recursion/Backtracking — Medium — [note](../notes/letter-combinations.md) — solved: with-hints:3 (2026-08-30) — **Accepted on the judge**. Approach stated in full before any code and correct: loop at a level runs over the chars of the current digit, index carried down, base case `index == digits.length()`. Two defects, both found by the user on questioning: `Integer.parseInt(char)` does not compile (closed in 2 rungs — guessed `Character` class, then derived `charAt(i)-'0'` once `'0'`=48 was given), and `digits=""` returning `[""]` instead of `[]` (**asked 4 times before it was traced** — answered correctly once the `0>=0` branch was walked). **Space derived to `O(n²)`, not the textbook `O(n)`**: `res+c` allocates a new immutable String per frame, so one live path holds `0+1+…+n` chars. Needed one concrete 4-frame trace after "i didnt get it", then the closed form and the `StringBuilder` + undo fix came cold
- [x] Word Search (LC 79) — Recursion/Backtracking/Grid — Medium — [note](../notes/word-search.md) — solved: with-hints:4 (2026-08-30) — **Accepted on the judge**. **Code arrived before the approach again**, ~2 min after all 3 approach questions were asked. Defects: (1) `exist` called `dfs` only from `(0,0)` — found by the user when asked to trace `"SEE"`, fixed to the 2D start loop cold; (2) `|` not `||` — the difference was stated correctly and so was the cost ("the other three subtrees still run, at every level"), but the fix that followed **changed the operator at the `return` while leaving the four calls eagerly assigned above**, so nothing short-circuited; handed over after "can we move?"; (3) the `board[i][j]=cur` restore was commented out mid-session and **silently restored in the next paste with the symptom question still unanswered** — closed on the 2nd ask via a 2x2 counterexample (`[["A","B"],["A","D"]]`, `"AAB"`), with one correction (named the destroyed cell as the path's start, it is the 2nd step). **Base-case ordering stated cold and correctly by precondition** ("all chars matched, doesn't depend on i j") — 4th encounter, first clean one. Complexity declined, handed over
- [x] Combination Sum III (LC 216) — Recursion/Backtracking — Medium — [note](../notes/combination-sum-iii.md) — solved: with-hints:2 (2026-08-30) — **Accepted on the judge**. First approach looped `1..9` at every level; **the start-index fix came cold from the user after one duplicate-path probe** — direct transfer from LC 39/40 two days earlier. All three base outcomes named correctly (accept, `cnt==k` with wrong sum, over-sum). Wrote the code only after the coverage guardrail was cited ("do i need to write it?"). Live defect found by guided trace: the reject guard `(cnt==k&&sum<n)||(cnt<k&&sum>=n)` **misses `cnt==k && sum>n`**, so the loop recurses with `cnt` past `k` — no wrong answers, pure wasted search; tightened to `cnt==k||sum>=n` cold. The `>=` justification (all candidates positive, so `sum` is monotone down a path) needed the ladder and was ultimately handed over — the condition was restated in place of the reason
- [x] Word Break (LC 139) — Recursion/Backtracking+Memo — Medium — [note](../notes/word-break.md) — solved: with-hints:5 (2026-08-31) — **Accepted on the judge**. Opened **greedy-first-match** (trie + advance `start` on the first hit); `"catsandog"` returned the right answer for the wrong reason, closed by the constructed counterexample `"catsdog"` / `["cat","cats","dog"]`. `f(start)` and the base case (`start==s.length()` -> true, "empty string left, nothing to segment") both stated correctly; the branch-and-continue structure came back after one re-trace when the first iterative restatement silently reverted to greedy. **Memo added unprompted** — the predicted exponential hole never landed. Two defects found by tracing: `index` is provably always equal to `start` (every call site passes `i+1,i+1`), and the success path reassigned `key=start+"-"+i` before `put`, so **every `true` was stored under a key no lookup ever asks for** — cost bug, not correctness, named as such by the user. Rewritten to `Boolean[n]`. `O(n³)` derived (n states x n splits x O(n) substring+hash); space `O(n)` + `O(sum of word lengths)` cold
- [x] Permutations (LC 46) — Recursion/Backtracking/Bitmask — Medium — solved: with-hints:3 (2026-08-31) — **Accepted on the judge**. **Structure cold and correct**: bitmask of used indices, place/recurse/undo with *both* undos present (`list.remove` and `mask^=1<<i`) — written 20 minutes after that exact mechanism was declined on N-Queens. Both defects were **operator precedence, same root cause**: `mask&(1<<i)==0` parses as `mask & ((1<<i)==0)` (compile error — `==` binds tighter than `&`), and `1<<(n+1)-1` parses as `1<<n` (`-` binds tighter than `<<`), giving 8 instead of 7 at n=3 so `mask==goalMask` never fires and nothing is ever recorded. Complexity first answered `2^n` (the subsets count), corrected to `O(n!·n)` off the worked example; space `O(n)` auxiliary
- [x] M-Coloring Problem (GFG) — Recursion/Backtracking — Medium — [note](../notes/m-coloring.md) — solved: with-hints:6 (2026-08-31) — **Accepted on the judge, 1114/1114, on the 3rd submission.** Approach v1 carried both of the cycle's named defects and **both were self-corrected**: legality defined as "differs from the previously coloured node" (closed by one traced instance — vertex 3 touches 0 and 2, the rule only checks 2), and **greedy-first-match, 3rd occurrence** ("on conflict return false") — closed in **one question, cold**: "no, we should try other colors for previous nodes", and the return path was then named unprompted ("the recursive call returns false, so the loop tries the next color"). **The code then reverted to the version just discarded** (`i != prvNodeColor`) — derivation-to-code regression, the session's finding. Three judge-visible defects, all mechanical: (1) the neighbour scan's `continue` targeted the inner loop, so the scan ran and threw its result away — a dead legality check; (2) the vestigial `if(color[curNode]==prvNodeColor) return false` survived the redesign and fired on the self-edge in `V=2, edges=[[0,1],[0,0]]`, poisoning `res` — WA 1/1114; (3) `graphColoring` called `dfs` on vertex 0 only, so disconnected components were never coloured — WA 6/1114 on `V=3, edge 1-2, m=1`, which is **the exact trace the user had parked 4 minutes earlier**. Fixed by looping `i` over all `V` and `res &= dfs(...)`. Complexity **not reached** — "no idea", session ended mid-derivation at `m^V`
- [ ] N-Queens (LC 51) — Recursion/Backtracking — Hard — [note](../notes/n-queens.md) — solved: failed (2026-08-31) — **2nd decline; WA on the judge, then abandoned.** Approach restated cold and correct (row-per-level, `colSet` + `r+c` + `r-c`). The code written was **iterative and greedy** — two nested loops, first valid column taken, no recursion and no undo — the same shape as the LC 139 opening 40 minutes earlier. Judge output on `n=4`: `[["Q..."],["..Q."],["...."],[".Q.."]]` — 3 queens, one empty row, and each entry one *row* rather than one *board*. User read both symptoms off their own output and named the fix ("backtrack and try column 1 in row 0"), then stopped before writing it ("we will come to this problem some other time")
- [ ] N-Queens (LC 51) — 3rd decline (2026-09-03 21:03, "not this one"), no attempt — **dropped from bucket 2's coverage list**, same threshold that took LC 131 off 2026-09-01. Approach has been correct cold twice; only the code was ever missing.
- [x] Frog Jump (DP-3) — DP/1D DP — Medium — solved: with-hints:1 — re-verification
  from stale import backlog surfaced real rust (Fibonacci-shaped first attempt,
  ignored height cost). See `../mistakes/mistake_journal.md`. Review #1 wrap-up
  completed 2026-07-11: edge cases (n=1, n=2), complexity (O(n)/O(n) unoptimized,
  O(n)/O(1) optimized) all closed — surfaced a second rust incident (missing
  dp[2] base case), logged as fresh mistake. [note](../notes/frog-jump-dp-3.md).
- [x] Find the Largest Element in an Array — Arrays/Basics — Easy — solved:
  independently — O(n)/O(1), correctly initialized max=arr[0] handling negatives
  and size-1 arrays.
- [x] Second Largest Element in an Array — Arrays/Basics — Easy — solved:
  with-hints:1 — guessed wrong on duplicate-of-max handling before tracing
  corrected it. [note](../notes/second-largest-element.md).
- [x] Check if Array is Sorted — Arrays/Basics — Easy — solved: independently —
  O(n)/O(1), correct on size 0/1 edge cases.
- [x] Remove Duplicates from Sorted Array — Arrays/Two Pointers — Medium —
  solved: with-hints:2 — initial current-vs-next comparison needed a
  last-element special case; guided to cleaner current-vs-last-unique pattern.
  [note](../notes/remove-duplicates-sorted-array.md).
- [x] Move Zeroes to End — Arrays/Two Pointers — Medium — solved: with-hints:1 —
  missed that plain overwrite leaves trailing garbage instead of zeroes; landed
  on one-pass swap version. [note](../notes/move-zeroes-to-end.md).
- [x] Rotate Array — Arrays/Basics — Easy — solved: with-hints:3 — fully stuck
  on O(1)-space approach, needed full derivation of reversal trick. [note](../notes/rotate-array.md).
- [x] Linear Search — Arrays/Easy — Easy — solved: independently.
- [x] Union of Two Sorted Arrays — Arrays/Easy — Easy — solved: with-hints:1 —
  missed dedup step initially (plain merge, not union).
- [x] Missing Number — Arrays/Easy — Easy — solved: independently — XOR approach,
  also named sum-formula alternative and its overflow tradeoff unprompted.
- [x] Max Consecutive Ones — Arrays/Easy — Easy — solved: with-hints:1 — missed
  post-loop check for trailing window, 3rd boundary-case miss this session.
- [x] Single Number — Arrays/Easy — Easy — solved: independently — XOR approach.
- [x] Longest Subarray with Sum K — Arrays/Easy — Medium — solved: with-hints:4 —
  fully stuck on negative-number case, needed full derivation of prefix-sum +
  hashmap generalization. [note](../notes/longest-subarray-sum-k.md).
- [x] Two Sum — Arrays/Medium — Easy — solved: with-hints:1 — proposed
  unnecessary duplicate-index-list complexity, self-corrected.
- [x] Sort Array of 0s, 1s, 2s (Dutch National Flag) — Arrays/Medium — Medium —
  solved: with-hints:5 — got swap mechanics after one hint, but deep confusion
  on why the invariant holds; induction framing failed, elimination-argument
  explanation landed. [note](../notes/sort-012.md).
- [x] Majority Element (>n/2, Boyer-Moore) — Arrays/Medium — Medium — solved:
  independently — correctly named the verification pass needed when no true
  majority exists.
- [x] Kadane's Maximum Subarray Sum — Arrays/Medium — Medium — solved:
  with-hints:2 — missed all-negative-array edge case (reset-before-recording
  max bug). [note](../notes/kadanes-max-subarray.md).
- [x] Stock Buy and Sell (single transaction) — Arrays/Medium — Easy — solved:
  with-hints:1 — clarified maxProfit=0 init guarantees non-negative floor.
- [x] Rearrange Array Elements by Sign — Arrays/Medium — Medium — solved:
  with-hints:1 — initial answer too vague, nailed down even/odd index
  mechanism after a prompt.
- [x] Next Permutation — Arrays/Medium — Hard — solved: with-hints:5 — deep
  stuck, missing rightmost-smallest-greater-than-pivot swap partner and
  suffix-reverse steps, needed full derivation. [note](../notes/next-permutation.md).
- [x] Leaders in an Array — Arrays/Medium — Easy — solved: with-hints:1 —
  self-derived correct monotonic-stack approach, then simpler O(1)-space
  right-to-left-max approach after one prompt.
- [x] Longest Consecutive Sequence — Arrays/Medium — Medium — solved:
  with-hints:4 — deep stuck, initial approach was O(n²) not O(n); needed
  guidance to sequence-start optimization and resolving processing-order
  confusion. [note](../notes/longest-consecutive-sequence.md).
- [x] Set Matrix Zeroes — Arrays/Medium — Medium — solved: with-hints:2 —
  correct core marker approach self-proposed, missed the (0,0) shared-cell
  conflict, resolved with row0Flag/col0Flag.
- [x] Rotate Matrix (90°, in-place) — Arrays/Medium — Medium — solved:
  with-hints:2 — no idea initially, needed guided transpose-then-reverse-rows
  derivation.
- [x] Spiral Traversal — Arrays/Medium — Medium — solved: with-hints:5 —
  deep stuck on outer-loop condition and per-pass guards, resolved via guided
  one-line-at-a-time tracing. See `../mistakes/mistake_journal.md`.
- [x] Subarray Sum Equals K — Arrays/Medium — Medium — solved: with-hints:3 —
  initially proposed sliding-window (invalid with negatives), self-corrected
  to prefix-sum+count-hashmap. See `../mistakes/mistake_journal.md`.
- [x] Pascal's Triangle — Arrays/Medium — Medium — solved: with-hints:2 —
  2026-07-17 — needed clarification on the trailing-1 append and the
  middle-recurrence loop bounds (prevRow[j-1]+prevRow[j]), correct once
  traced concretely.
- [x] Print Subarray with Maximum Sum — Arrays/Medium — Medium — solved:
  with-hints:many — 2026-07-20 (resumed from 2026-07-17 mid-derivation) —
  dual-pointer (tempStart vs start) Kadane's variant, fully resolved via
  guided trace + self-written code. See mistake_journal.
- [x] Valid Parentheses — Stack/Queue — Easy — solved: independently —
  2026-07-20, first Stack/Queue problem (new topic). Clean push/match/pop
  logic + correct post-loop `stack.isEmpty()` check.
- [x] Min Stack — Stack/Queue — Medium — solved: independently — 2026-07-20 —
  value+minSoFar pair per stack frame, all ops O(1).
- [x] Next Greater Element — Stack/Queue — Medium — solved: with-hints:1 —
  2026-07-20 — correct monotonic-stack approach and trace cold, but initial
  code pushed the computed answer instead of the original value onto the
  stack; fixed with a separate output array. [note](../notes/next-greater-element.md).
- [x] Implement Queue using Two Stacks — Stack/Queue — Medium — solved:
  independently — 2026-07-20 — correct lazy-transfer algorithm cold; amortized
  O(1) complexity reasoning needed real escalation (why ≤3 ops/element, not
  =3) before landing. Code skipped.
- [x] Nearest Smaller to the Left — Stack/Queue — Easy — solved: with-hints:2 —
  2026-07-21 — instance mechanics (left-to-right traversal, pop-while-top >=
  current including ties, -1 sentinel) derived correctly and fast, but
  generalizing "why does traversal direction depend on the problem" into a
  transferable rule needed real escalation (two circular answers first). Landed
  on: traversal-start-side = query-side. See mistake_journal.
  **Backfilled 2026-07-27** — was solved live but never got a Completed
  Problems line; found by the dashboard's parser health check.
- [x] Stock Span Problem — Stack/Queue — Medium — solved: with-hints:1 —
  2026-07-21 — correctly identified span as the distance from the
  nearest-greater-left index, but the formula carried an off-by-one
  (`curIndex-ngeIndex-1` instead of `curIndex-ngeIndex`); resolved by deriving
  via inclusive-range counting (`b-a+1`) rather than guessing the offset.
  Verified on `[5,10]` at i=1, confirming the -1 sentinel needs no
  special-casing. See mistake_journal. **Backfilled 2026-07-27** — same gap as
  above.
- [x] Maximum Sum Subarray of Size K — Sliding Window/Fixed Window — Easy —
  solved: independently — 2026-07-24 — running sum, add incoming/subtract
  outgoing, O(n)/O(1); correct on k>array.length edge case (-1). First
  Sliding Window problem (new topic). Code skipped (user judgment).
- [x] Longest Substring Without Repeating Characters — Sliding Window/Variable
  Window — Medium — solved: independently — 2026-07-24 — hashset + shrink
  left while duplicate present, O(n) amortized, correct on empty string (0).
  Code skipped.
- [x] Max Consecutive Ones III — Sliding Window/At-most-K — Medium — solved:
  independently — 2026-07-24 — zero-counter + shrink-while->k, correct on
  k=0 edge (reduces to plain max-consecutive-ones). Code skipped.
- [x] Fruit Into Baskets — Sliding Window/At-most-K — Medium — solved:
  independently — 2026-07-24 — freq map + distinct-type count, correct on
  all-one-type edge. Code skipped.
- [x] Longest Repeating Character Replacement — Sliding Window/At-most-K —
  Medium — solved: with-hints:3 — 2026-07-24 — validity formula
  (`len-maxFreq<=k`) self-derived after 1 hint, but held a false belief
  that net window length can shrink after growing; corrected via guided
  trace on "AABABBA",k=1. See mistake_journal.
- [x] Minimum Window Substring — Sliding Window/Variable Window — Hard —
  solved: independently — 2026-07-24 — need-map/window-map comparison
  approach valid cold; also walked through the cleaner O(1)
  matched-counter refinement. Correct on t-has-duplicates and
  no-valid-window edges. Code skipped.
- [x] BFS Traversal of Graph — Graph/Traversal — Easy — solved: with-hints:1
  — 2026-07-25 — first Graph problem (new topic). Design (representation,
  regions, complexity) derived cold; first code draft marked visited at
  pop-time and pushed neighbors without a visited check, self-corrected
  once pointed at the contradiction with own derivation. [note](../notes/bfs-graph.md).
- [x] DFS Traversal of Graph — Graph/Traversal — Easy — solved: with-hints:1
  — 2026-07-25 — initially proposed marking visited on exit (post-order),
  self-corrected via a 0-1 cycle counterexample to visited-on-entry.
  Code clean once corrected. [note](../notes/dfs-graph.md).
- [x] Number of Provinces — Graph/Connected Components — Medium — solved:
  with-hints:1 — 2026-07-25 — approach only (code skipped, user judgment).
  Component counter initially set to 1, self-corrected to 0. Correctly
  adapted DFS from adjacency-list to adjacency-matrix traversal.
- [x] Number of Islands — Graph/Connected Components (Grid) — Medium —
  solved: independently — 2026-07-25 — approach only (code skipped).
  Correct bounds/cell/visited base cases and outer-loop trigger condition,
  no hints.
- [x] Rotten Oranges — Graph/Multi-source BFS — Medium — solved:
  with-hints:3 — 2026-07-25 — approach only (code skipped). Multi-source
  setup (push all initial rotten cells) and -1 check (post-BFS fresh scan)
  both clean cold; the minute-counter increment rule took 3 counterexample
  iterations to land on "increment only if a node was actually pushed this
  level," not "every level" or a queue-size-vs-total-cells special case.
  [note](../notes/rotten-oranges.md).
- [x] Flood Fill — Graph/Traversal — Easy — solved: with-hints:1 — 2026-07-25
  — approach only (code skipped). Initially proposed marking visited at pop
  time (3rd recurrence of this bug), self-caught via 2x2 grid trace showing
  duplicate push; isolated-cell edge case (source still repaints even with
  no same-color neighbors) needed 1 correction.
- [x] Cycle Detection (Undirected, BFS) — Graph/Cycle Detection — Medium —
  solved: independently — 2026-07-25 — approach only (code skipped).
  (node,parent) pair BFS, parent-skip, visited-and-not-parent=cycle,
  self-derived cold with no hints.
- [x] Cycle Detection (Directed, DFS + BFS) — Graph/Cycle Detection — Medium
  — solved: with-hints:2 total — 2026-07-25 — approach only (code skipped).
  DFS: self-derived "track current path" idea, needed formal 3-color
  (white/gray/black) naming only. BFS (Kahn's): self-derived in-degree-zero
  queueing, needed 1 nudge on exact termination check (processed count vs
  n). Also correctly worked out via guided example why plain global-visited
  false-positives on directed DAGs with converging paths (undirected trick
  doesn't transfer).
- [x] Bipartite Check (LC 785) — Graph/Bipartite — Medium — solved:
  with-hints:many — 2026-07-25 — full code written. Approach (color array,
  flip-on-push, same-color-conflict) self-derived clean. Odd-cycle "why"
  needed heavy escalation (2 failed attempts, closed via light-switch
  parity analog + concrete triangle/square trace). Code bug: DFS'd only
  from node 0, missed disconnected components — self-fixed via
  disconnected-graph trace, added outer loop (same pattern as Number of
  Provinces).
- [x] Topological Sort (DFS) — Graph/Topological Sort — Medium — solved:
  with-hints:1 — 2026-07-25 — approach only (code deliberately skipped,
  deferred to Kosaraju). Kahn's (BFS) recalled instantly; DFS approach
  (finish-order + reverse, plain visited sufficient on guaranteed-acyclic
  input) needed 1 nudge then derived cleanly.
- [x] Kosaraju's Algorithm (SCC) — Graph/SCC — Hard — solved: with-hints:
  many — 2026-07-25 — approach only, heaviest derivation today. 3-step
  skeleton recalled unaided; "why finish-order, not random start" needed 3
  escalation rounds via concrete 4-node 2-SCC-bridge trace before landing
  cleanly, full correct self-explanation at close.
- [x] Dijkstra's Algorithm — Graph/Shortest Path — Medium — solved:
  with-hints:many — 2026-07-26 — min-heap (dist,node), relax, non-negative
  justification all self-derived cold. Stale-heap-entry skip check needed 1
  nudge. Complexity notation needed 3 escalation rounds before landing
  O(E log E)=O(E log V). Negative-edge failure: 1st answer wrong (conflated
  with negative-cycle non-termination), needed full guided concrete trace
  (S→Y=2, S→X=3, X→Y=-100) to see the real "visited-lock finalizes wrong
  value" failure mode. Sharp follow-up: why not skip the visited-lock and
  just compare dist — correct on correctness, but breaks Dijkstra's O(E log V)
  guarantee (unbounded re-relaxation), which is exactly why Bellman-Ford
  exists instead. See mistake_journal.
- [x] Bellman-Ford Algorithm — Graph/Shortest Path — Medium — solved:
  with-hints:several — 2026-07-26 15:28 — full code written (GFG "Distance
  from the Source"). Derivation (from 10:20 session) held; code dropped the
  Vth negative-cycle detection round and used an `Integer.MAX_VALUE-1000`
  infinity fudge with no unreachable guard. Both fixed, then a 2nd bug: guard
  added to the relaxation loop but not the structurally identical detection
  loop — false "negative cycle" on an unreachable component with a negative
  edge, caught via 2-component trace. Complexity O(V·E)/O(V) clean cold,
  negative-weight condition clean, early-exit-variant trap (infinite loop on
  negative cycle) clean. Dijkstra visited-lock "why" needed 4 escalation
  rounds — 2nd time today. [note](../notes/bellman-ford.md).
- [x] Redundant Connection (Union-Find) — Graph/Disjoint Set — Medium — solved:
  with-hints:2 — 2026-07-27 16:36 — full code written. Approach (parent array,
  union by rank, path compression) stated correctly cold; code initially
  incremented `rank[winner]` on every union win instead of only on ties,
  breaking the rank-as-height-bound invariant (correctness unaffected, height
  guarantee lost) — fixed after a constructed counterexample. Also needed
  simple-analog escalation on inverse Ackermann / O(α(n)). [note](../notes/union-find-redundant-connection.md).
- [x] Floyd-Warshall's Algorithm — Graph/Shortest Path — Medium — solved:
  with-hints:many — 2026-08-01 16:32 — approach/derivation only, code not
  written. "Why k outer" invariant finally derived after 5 sessions/attempts
  (07-26, 07-30, 07-31, 08-01 08:35, closed 08-01 16:32) — landed via
  concrete instantiation (dist[A][C] vs dist[A][D] right after k=B pass)
  rather than the abstract chain trace. See mistake_journal.
- [x] Min Cost to Connect All Points (Kruskal's: PQ + Union-Find) —
  Graph/MST — Medium — solved: with-hints:2 — 2026-08-01 16:39 — full code
  written. `parent[0]` relied on `int[]` zero-default instead of explicit
  init (loop started at i=1) — fixed. Complexity O(n²log n) confirmed cold.
  [note](../notes/mst-min-cost-connect-points.md).
- [x] Min Cost to Connect All Points (Prim's, heap-based) — Graph/MST —
  Medium — solved: with-hints:1 — 2026-08-01 17:04 — full code written
  (matches an already-accepted LeetCode submission). Relax rule mistaken as
  cumulative (Dijkstra-style) during verbal derivation, corrected via
  counterexample before code was written; O(n²log n), no improvement over
  Kruskal's. See mistake_journal.
- [x] Min Cost to Connect All Points (Prim's, array-based O(n²)) —
  Graph/MST — Medium — solved: with-hints:many — 2026-08-01 17:12 — first
  exposure to this variant. Min-scan sub-step self-derived (same shape as
  "find largest element"), corrected relax rule applied; full loop assembly
  mentor-supplied after sub-pieces confirmed. Verified against LeetCode
  1584 editorial thread. See mistake_journal.
- [ ] Course Schedule (LC 207) — Graph/Topological Sort — Medium —
  [note](../notes/course-schedule.md) — solved: with-hints:1 — 2026-09-03
  21:18 — Kahn's BFS, cold, no approach spoken first. Live bug:
  `indegree[pre[1]]++` (prereq node) instead of `indegree[pre[0]]++`
  (dependent node) — found via a 2-node trace, fixed silently, defect only
  stated after being asked to restate it. Complexity O(V+E) cold. Confirmed
  layering (`size` snapshot) is unnecessary here by removing it and
  reasoning why (order doesn't matter, only whether every node reaches
  indegree 0) — closed clean once asked to say it in words.
- [x] Course Schedule II (LC 210) — Graph/Topological Sort — Medium — solved:
  independently — 2026-09-05 13:08 — Kahn's BFS, add to result list on pop,
  cycle check via `ctr==numCourses`. Cold, clean, no hints, complexity/space/
  edge-case all self-stated.
- [x] Alien Dictionary (LC 269) — Graph/Topological Sort — Hard —
  [note](../notes/alien-dictionary.md) — solved: with-hints:many — 2026-09-05
  13:43 — approach recall needed heavy escalation despite a prior "solved
  this before" claim. 3 live code bugs: `(char)cur+'a'` cast-precedence
  (bound to `cur` alone, produced int not char); `compareWords` length-check
  ran before the character scan, wrongly flagging valid pairs as invalid;
  cycle-check counter counted total characters across words instead of
  distinct letters. All 3 found by guided trace, fixed and defect restated
  each time.
- [x] Number of Enclaves (LC 1020) — Graph/Multi-source BFS — Medium —
  [note](../notes/number-of-enclaves.md) — solved: with-hints:1 — 2026-09-05
  13:57 — cold approach and cold first code, but marked visited at pop
  instead of push, causing duplicate queue entries -> TLE. Same
  visited-at-push rule already documented in `topics/Graph.md`, first time
  it actually cost a failing run.
- [x] Kth Largest Element in an Array — Heaps — Medium — solved:
  with-hints:1 — 2026-08-01 17:42 — first Heaps problem (new topic).
  Max-heap-pop-k-1 approach self-derived cold; min-heap-of-size-k
  alternative (O(n log k)) also self-derived cold, code clean independently,
  edge cases (k=1, k=n) correct. Only gap: didn't know `build-heap`/
  `heapify` is O(n), not O(n log n) — told directly (fact, not a
  derivable technique). See mistake_journal.
- [x] Top K Frequent Elements (LC 347) — Heaps — Medium — solved:
  with-hints:1 — 2026-08-01 22:03 — approach/derivation only, code not
  written (user declined, late session). Freq map + min-heap-of-size-k
  self-derived, but briefly stated eviction comparator as descending
  (top-of-heap = largest freq), which contradicts min-heap eviction of the
  smallest — self-corrected after 2 targeted questions to ascending
  (`a.freq - b.freq`). Complexity O(n log k) stated correctly throughout.
  [note](../notes/top-k-frequent-elements.md). See mistake_journal.
- [x] Find Median from Data Stream (LC 295) — Heaps/Two Heaps — Hard —
  solved: with-hints:several — 2026-08-02 16:54 — full code written
  (resumed from 10:43 stall). Two real code bugs, both surfaced by trace:
  NPE from `minHeap.isEmpty() && maxHeap.peek()>minHeap.peek()` missing the
  `!`, and no min→max rebalance at all (sizes drifted 1 vs 3, returned 1.5
  instead of 2.5 on `{1,2,3,4}`) — both fixes self-derived once the hole was
  located. Complexity O(log n)/O(1)/O(n) cold. Naive baseline and the
  bounded-range `[0,100]` counting-array variant (O(1)/O(1)) both closed,
  the latter after heavy escalation. [note](../notes/find-median-data-stream.md).
- [x] Merge k Sorted Lists (LC 23) — Heaps/K-way Merge — Hard — solved:
  with-hints:2 — 2026-08-02 16:54 — approach only, code skipped (user
  judgment, mentor flagged code as advisable given the last two heap
  problems broke in code; user declined). Heap-size-≤-k and O(N log k)
  both cold; edge cases named unprompted. Space needed 2 escalations —
  answered O(N) counting the output, then O(N)+O(k), before separating
  extra space O(k) from output and seeing that relinking beats allocating.
- [x] Task Scheduler (LC 621) — Heaps/Greedy — Medium — solved:
  with-hints:several — 2026-08-02 16:54 — approach only, code not written.
  First Greedy-flavoured problem. Two rule bugs, both self-corrected:
  heap tie-break given as label order before landing on frequency-desc,
  and re-push offset `current+n` instead of `current+n+1` (caught on
  `[A,A]`,n=2 → gave 3, true 4). Greedy justification clean at interview
  bar. O(N)/O(1) after simplifying the log-26 constant. Closed-form
  `(maxFreq-1)*(n+1)+countMax` derived, then **decayed within ~5 minutes**
  and had to be re-anchored on the user's own concrete schedule.
  [note](../notes/task-scheduler.md).
- [x] N Meetings in One Room — Greedy — Medium — solved: with-hints:several —
  2026-08-05 — approach only, code skipped (user judgment). Sort-by-end +
  strict `end<nextStart` boundary self-derived cold, O(n log n)/O(n) clean.
  "Why end-time, not start/duration" needed heavy escalation both times
  (constructed counterexamples). See mistake_journal.
- [x] Jump Game (LC 55) — Greedy — Medium — solved: independently — 2026-08-06
  — full code cold, no bugs, correct on `[0]`/`[2,0,0]` edge cases, O(n)/O(1).
  "Why greedy (max-reach dominates)" needed 1 targeted question before
  landing the dominance argument. See mistake_journal.
- [x] Jump Game II (LC 45) — Greedy — Medium — solved: independently —
  2026-08-06 — two correct solutions: heap-based O(n log n) first (self-
  derived cold, verified across 4 traces), then self-optimized to O(n)
  two-pointer unprompted after being asked whether the heap was necessary.
  No bugs in either version.
- [x] Job Sequencing Problem (GFG) — Greedy — Medium — solved: with-hints:2 —
  2026-08-06 — two real approach mistakes, both self-corrected via
  constructed counterexamples: (1) sorted by deadline ascending instead of
  profit descending; (2) placed jobs in the earliest available slot instead
  of the latest available slot ≤ deadline. Code correct once both were
  fixed, verified against both counterexamples. [note](../notes/job-sequencing.md).
  **Pressure-test closed 2026-08-07**: per-job scan cost, O(n²) worst case,
  and the all-deadlines-=-n worst-case shape (n(n-1)/2) all derived cold and
  unprompted; the DSU slot-find optimization was not reached — full
  explanation given after a category hint and an analog both failed.
  See mistake_journal 2026-08-06 and 2026-08-07. **DSU close-the-loop closed
  2026-08-08** (1 nudge). **Bounded-heap variant added 2026-08-08 — read, not
  derived** (code pasted from GFG, self-disclosed): sort-key-flip reasoning,
  O(n log n)/O(n), and the dead `!pq.isEmpty()` branch all cold; the
  no-regret exchange argument needed 4 escalations. Problem now covered three
  ways (array O(n²), DSU O(n·α), heap O(n log n)).
- [x] Fractional Knapsack (GFG) — Greedy — Medium — solved: with-hints:several —
  2026-08-08 23:24 — approach only, code declined by user. Mechanics (ratio
  order, fraction of the last item) carried over from the 20:46 session; the
  **exchange argument finally produced here** via the guided unit-swap (first
  delta answer 20, correct +5, then expressed as ratio(A)−ratio(B)) and
  generalized cleanly: any packing holding a lower-ratio unit while a
  higher-ratio item is unexhausted can be strictly improved, so it is not
  optimal. O(n log n) time cold; space given as O(log n) — the gap was not
  knowing object-array `Arrays.sort` is TimSort with an O(n) buffer (library
  fact, stated directly), landed O(n). All four edge cases (W=0, single item
  heavier than W, all-equal ratios, total weight < W) clean and cold, with a
  correct `while (remaining > 0 && i < n)` loop header.
  [note](../notes/fractional-knapsack.md). See mistake_journal.
  **Code written and closed 2026-08-09 16:22** — correct first try, cold, no
  bugs: `(double)val[i]/wt[i]` cast before dividing and `capacity*cur[1]`
  promoting to double, i.e. both flagged bug surfaces clean. Space O(n) cold
  this time (was O(log n) on 08-08). Heap-vs-sort pressure test clean: sort
  gives the same order upfront, heap only wins when capacity fills after
  k << n items (O(n) heapify + k log n) — and correctly not claimed for this
  code, which uses n inserts, not a bulk heapify.
- [x] Candy (LC 135) — Greedy/Two-Pass Constraint Propagation — Hard —
  solved: with-hints:many — 2026-08-09 16:43 — approach only, code declined.
  n-candy floor, two-pass structure, both passes on `[1,3,2,1]`, and the
  `max` merge rule all cold. Minimality half (`left[i]` counts the increasing
  run, so any valid `v[i]` ≥ that) cold and clean. The **validity** half
  needed the full ladder (2 "i don't get it" + 1 "no idea"): the worry —
  does `c[i] > c[i-1]` survive the max when `c[i-1]` might come from the
  right pass — only moved after instantiation on `[1,3,2,1]`, a `max(a,b) ≥ a`
  analog, and link-by-link chain assembly; chain then stated correctly
  (`c[i] ≥ left[i] = left[i-1]+1 > left[i-1] = c[i-1]`, the key being
  `right[i-1] = 1` whenever the left constraint applies at i). First attempt
  at `[1,0,2]` gave `1,1,2` (violates the left neighbour) — self-corrected in
  1 nudge. O(n)/O(n) and the one-array refinement cold; **O(1) run-length
  variant open** — asserted unreachable, then the run-length idea landed in 1
  question but the peak-sharing detail did not, and the variant was parked at
  the user's call. [note](../notes/candy.md). See mistake_journal.
- [x] Assign Cookies (LC 455) — Greedy — Easy — solved: independently —
  2026-08-11 20:21 — **full code cold, correct first try, no bugs** (descending
  two-pointer over both sorted arrays; `i--` every iteration, `j--` only on
  assignment). Time O(n log n + m log m) cold. Space answered O(1), 1 nudge to
  O(log n) — primitive `Arrays.sort` = dual-pivot quicksort stack, mirror of the
  08-08 TimSort miss. Edge case (empty `s` → 0) cold. Exchange argument needed
  the full instantiate-then-symbolize ladder (5th greedy *why* running), landed
  as `g[D] ≤ g[C] ≤ s[k]`. See mistake_journal.
- [x] Lemonade Change (LC 860) — Greedy — Easy — solved: with-hints:1 —
  2026-08-12 17:26 — full code written. One real bug: `Arrays.sort(bills)` on
  an order-dependent input, caught via the `[10,5]` counterexample; everything
  else clean cold (both feasibility guards, and the ten+five-before-three-fives
  preference). O(n)/O(1) cold — genuinely O(1) here only because the sort is
  gone, the mirror of Assign Cookies' O(log n). Edge case (empty input → true,
  loop never runs) cold. Exchange argument landed after 4 exchanges via the
  wallet-diff prompt (2 extra fives vs 1 fewer ten, fives dominate); the
  4-sentence interview-script delivery was offered and declined, still
  untested live. See mistake_journal.
- [x] Valid Parenthesis String (LC 678) — Greedy/Reachable-Range — Medium —
  solved: with-hints:many — 2026-08-13 17:23 —
  **parked mid-derivation 2026-08-12 17:50**, no code. Reached: `{0,1,2}` for
  `(*`, dead-negative-branch pruning, and the full solidity induction (`(`/`)`
  are shifts, `*` is the union of three overlapping shifts, pruning cuts a
  prefix) → carry only `(min,max)`. User raised the solidity-proof question
  unprompted, which is new. Open: per-character update rules, the min-clamp at
  0, the early bail-out, the accept condition, and the code. DP-with-memo named
  as an O(n²) fallback.
  **Derivation completed 2026-08-12 20:38, code still open (buggy).** All three
  update rules, the `max < 0` bail-out (+ why: largest reachable count negative
  ⇒ all are), the min-clamp to 0, and the accept condition (`min <= 0 <= max`,
  simplifying to `min == 0`) all landed — but every one of the four needed
  escalation. Code written, two defects: `if (min<0) ... else if (max<0)` makes
  the max check unreachable (`)` returns true), and the blind "fix" deleted
  `min--` on `)`, breaking `()`. Complexity never stated. **Resume: trace `)`
  and `()` on the user's own code, restore `min--`, unchain the two checks.**
  **Code closed 2026-08-13 17:23 — with-hints:2.** Both defects fixed by the
  user: the dead-code chain located in 2 questions (named the guard condition,
  then derived `min<=max` ⇒ `max<0` unreachable), and `min--` restored
  unprompted. Building the failing input `")*"` needed a 3-step ladder (which
  char lowers max → which raises it → which leaves min at 0) after "I don't
  know". Return simplified to `min==0` independently. O(n) time cold; space
  O(n) after 1 nudge on `toCharArray()` — 3rd hidden-allocation question this
  month, first caught in one nudge. **Open: why `min==0` alone equals
  `min<=0<=max`** — both halves (`x>=0 ∧ x<=0 ⇒ x==0`; reaching the return
  implies `max>=0`) were stated back correctly, user judged it not landed and
  parked it.
- [x] Merge Intervals (LC 56) — Greedy/Intervals — Medium — solved:
  independently — 2026-08-13 17:32 — **full code cold, correct first try, no
  bugs**: sort by start (tie by end), merge into the last kept interval when
  `last[1] >= cur[0]`, mutating through the stored reference, then copy out to
  `int[][]`. O(n log n)/O(n) cold, including the `int[][]` sort buffer.
  Pressure test both landed: the last-interval-only comparison justified as
  **"ends are increasing in the list, so the last holds the largest end"**
  (first answer restated the sort rule, correct quantity named on the re-ask),
  and the `a[1]-b[1]` tie-break identified as dead code cold. First problem in
  the Greedy run where mechanics *and* a justification both came without a
  real escalation.
- [x] Shortest Job First (GFG) — Greedy/Scheduling — Easy — solved:
  with-hints:2 — 2026-08-14 22:20 — **full code cold, correct first try, no
  bugs** (sort ascending, running clock, accumulate each process's wait before
  adding its burst; `total/n` floor). The 2 hints were *not* on the algorithm:
  (1) the **problem statement itself** didn't parse — "I don't understand this
  problem" — closed by a guided trace of the unsorted order on the sample
  (user computed waits 14, 15 correctly and then named the choice as "the order
  to run them in"); (2) space stated O(n), re-aimed with the standing
  "primitives or objects?" checklist item and corrected to O(log n) in **one
  nudge**. Time O(n log n) cold. **Open: the *why*** — the exchange argument was
  posed as the 4-sentence script and declined ("i dont think we need script for
  all the problems"), 3rd decline. Side observation not raised by the user:
  `Arrays.sort(bt)` mutates the caller's array.
- [x] Minimum Coins of 1, 2, 5 and 10 (GFG) — Greedy/Denominations — Easy —
  solved: independently — 2026-08-18 17:43 — **full code cold, correct first
  try, no bugs** (descending fixed denomination array, `cnt += n/val; n %= val`).
  O(1)/O(1) cold — correctly tied to the fixed 4-denomination set, no dependence
  on `n`. The *why* needed 2 escalations and followed the known ladder: first
  answer was mechanics-restatement ("our code always settles with higher
  denomination first"), then both plans instantiated on n=39 (3+1+2 = 6 coins
  vs 2+3+2 = 7), then the general form landed cold — **dropping one 10 forces
  ≥2 coins back, since the largest smaller coin is 5, so no swap-down ever
  reduces the count**. Mentor error this session: the problem statement given
  with the OJ link was the wrong problem (full Indian denomination set,
  return-the-list variant); user's code was right and the mentor's stated
  expected output for n=121 was wrong. User pushed back correctly ("my code is
  right").

- [x] Sudoku Solver (LC 37) — Recursion/Backtracking — Hard —
  [note](../notes/sudoku-solver.md) — solved: with-hints:7 — 2026-09-01 18:13 —
  **Accepted 10/10, 125 ms.** Approach cold and complete (row/col/box trackers,
  try digits, undo on dead end) with **no greedy-first-match** — "backtrack" was
  volunteered unprompted, and the base case was justified by the invariant, cold
  ("if they conflict we would have backtracked"). The 12-minute block was
  `(r/3)*3 + c/3` — 2D->1D flattening, escalated through a cinema-seat analog and
  finally handed over; the same gap produced `i*3+j` as the cell stride. Six code
  defects, **all mechanical**, each found by tracing once pointed at the line:
  wrong stride, prefilled cell returning true, `i>=m&&j>=n` base case (crashes at
  `(9,0)`), `cols[i]` for `cols[j]` twice, missing `(char)('0'+val)`.
  `O(9^k)` / `O(1)` both cold.
- [x] Single Number (LC 136) — BitManipulation — Easy — solved: independently —
  2026-09-01 18:33 — **Accepted. Re-verify**, not new: first solved 2026-07-12,
  see `../topics/Arrays.md:68`. XOR named instantly, cold, with the cancellation
  argument. Gap: could not name commutativity/associativity as the licence for
  reordering the fold — handed over after 2 escalations.
- [x] Single Number II (LC 137) — BitManipulation — Medium —
  [note](../notes/single-number-ii.md) — solved: with-hints:3 — 2026-09-01 18:46
  — **Accepted.** Rejected XOR by tracing `[1,1,1,2]` -> 3, rejected the HashMap
  on the space constraint unprompted once pointed at it, derived per-bit count
  mod 3 by hand on the binary columns, and produced "32 slots, and we need bit 31
  too" after one push. Two code defects, both at the write step: `%2` where `%3`
  had just been derived, and `i<<1` for `1<<i`.
- [ ] Permutations II (LC 47) [Medium] — **declined at approach 2026-09-01, not
  counted.** Cost of the naive set-of-finished-permutations version was derived
  correctly (`n!` built, 1 survives at `n=8` all-equal), but the per-call
  `Set` of values tried at this depth appeared **inside the mentor's own
  question** rather than being derived — user flagged this correctly and stopped.
  Re-pose cold, without the phrase.
- [ ] Permutations II (LC 47) — 2nd decline, re-posed clean this time
  (2026-09-03 21:04, "i dont like this problem"), no priming issue this time —
  genuine decline, not a mentor error.
- [x] Single Number III (LC 260) — BitManipulation — Medium —
  [note](../notes/single-number-iii.md) — solved: with-hints:5 — 2026-09-02 17:46
  — **Accepted.** Cold start had no approach. Escalation ladder to the
  differing-bit split: named XOR-all -> x^y unaided once restated, but "either
  element has a set bit" needed a correction (exactly one does), and generalizing
  to "any set bit works" needed a numeric split-by-bit before landing. Code
  correct first submit, traced clean on `[1,2,1,3,2,5]`.
- [x] Power of Two (LC 231) — BitManipulation — Easy —
  [note](../notes/power-of-two.md) — solved: with-hints:3 — 2026-09-02 17:46
  — **Accepted.** Cold start had no approach; closed via binary instantiation
  (1,2,4,8,16 all single-set-bit) then `n & (n-1) == 0` derived from
  `8 & 7`. Code bug: guard checked only `n==0`, missed negative n (Integer.
  MIN_VALUE has exactly one set bit) — fixed after being pointed at the test case.
- [x] Number of 1 Bits (LC 191) — BitManipulation — Easy —
  solved: with-hints:1 — 2026-09-02 17:46 — **Accepted.** Loop-and-mask
  approach and O(1)/O(1) complexity both cold, clean solve.

## Topics Started

- Binary Search: complete (32/32) — solved ~2-3 months ago, rusty, needs re-verification
- LinkedList: complete (31/31) — solved ~2-3 months ago, rusty, needs re-verification
- BST: complete (16/16) — solved ~2-3 months ago, rusty, needs re-verification
- Trees: near-complete (36/39) — solved ~2-3 months ago, rusty + 3 unconfirmed gaps
- Tries: near-complete (6/7) — solved ~2-3 months ago, rusty + 1 known gap
- DP: strong (44/56) — solved ~2-3 months ago, rusty + 12 unconfirmed gaps, high
  interview weight, priority for early re-verification
- Arrays: in progress — 27 problems confirmed solved live — Basics 6/6,
  Easy 6/6, Medium 15/15 done (Print Subarray with Maximum Sum closed
  2026-07-20). Hard subtopic (11 problems) untouched.
- Strings: in progress (3/15)
- Recursion: in progress (2/25) — priority gap
- Bit Manipulation: in progress (1/18)
- Basics: not started (0/31) — low priority given prior experience
- Sorting: not started (0/7)
- Stack/Queue: 6 problems solved live (Valid Parentheses, Min Stack, Next
  Greater Element, Implement Queue using Two Stacks, Nearest Smaller to the
  Left, Stock Span Problem) — no new problems 2026-07-24, only review reps
- Sliding Window: in progress — 6 problems solved live 2026-07-24 (Maximum
  Sum Subarray of Size K, Longest Substring Without Repeating Characters,
  Max Consecutive Ones III, Fruit Into Baskets, Longest Repeating Character
  Replacement, Minimum Window Substring). Pattern file + topic file updated
  with the At-most-K variant.
- Graph: rusty recall (2yr-old, see reclassification note below), in
  progress — 12 problems/variants solved live 2026-07-25 (BFS
  Traversal, DFS Traversal, Number of Provinces, Number of Islands, Rotten
  Oranges, Flood Fill, Cycle Detection Undirected-BFS, Cycle Detection
  Directed-DFS, Cycle Detection Directed-BFS/Kahn's, Bipartite Check,
  Topological Sort-DFS, Kosaraju's/SCC). First real session on this topic
  (previously 0%, top Week 3 priority). Cycle detection = best performance
  of the day, mostly self-derived; Kosaraju's "why finish-order" was the
  day's toughest derivation (3 escalation rounds), Bipartite's odd-cycle
  derivation close behind. Dijkstra added 07-26 morning. Bellman-Ford
  derivation 07-26 (2nd session) + **code closed 07-26 15:28 (3rd session)**.
  18 problems/algorithms done as of 2026-08-01 (Floyd-Warshall derivation
  closed 16:32; Kruskal's, Prim's-heap, Prim's-array all coded same
  session). Core graph-algorithm list (Dijkstra, Bellman-Ford, Floyd-
  Warshall, Kruskal's, Prim's, Union-Find) is now fully covered at least
  once — remaining work is review-ladder consolidation, not new material.
- Heaps: 0% live prior to today — 1 problem solved live 2026-08-01 (Kth
  Largest Element in an Array, both max-heap and min-heap-of-k approaches,
  clean except the build-heap/heapify O(n) fact, unknown before this
  session). First real session on this topic. **5 as of 2026-08-02**:
  + Top K Frequent (08-01), Find Median from Data Stream (closed 08-02,
  only one with code written), Merge k Sorted Lists, Task Scheduler.
- Greedy: started 2026-08-02 via Task Scheduler (heap-backed greedy) —
  formula/edge-cases/code still open. 2026-08-05: N Meetings in One Room
  closed (approach+edge cases, code skipped); Minimum Number of Platforms
  started, mechanics + tie-break derived, chain-edge-case "why" open —
  see Notes for Next Session.
- 2026-07-26: Reviews closed — Two Sum review #3 (clean), Rearrange Array
  Elements by Sign review #3 (clean, plus correctly derived the unequal-
  count leftover-append variant unprompted). Then Dijkstra's Algorithm
  (new Graph algo) — see Completed Problems entry above; complexity
  notation and negative-edge failure mode both needed real escalation, 2
  fresh mistakes logged. System Design track started same session: case
  study sheet built (24 studies), Rate Limiter proposed as first, not yet
  attempted (session ended on requirements-gathering setup).
- 2026-07-26 10:20 (2nd session today): Bellman-Ford (new Graph algo, Block A
  next-after-Dijkstra) — derivation only, clean cold, no real mistakes:
  correctly recalled Dijkstra's visited-lock failure mode as the reason
  negative edges break it; self-derived shortest-path ≤ V-1 edges (a cycle in
  a shortest path implies negative cycle, else it'd be droppable for an
  equal/shorter path); negative-cycle detection (extra Vth relaxation round,
  still-improving = negative cycle) landed clean after one re-aimed question
  (first answer addressed a different sub-question, not wrong content).
  **Code not yet written — session got redirected into a meta-discussion
  (updated interview-prep-save + interview-prep-resume skills: added
  timestamp logging (Step 0 + HH:MM in entries) and a rule flagging when code
  is mandatory vs skippable). Bellman-Ford qualifies as code-mandatory
  (edge-list relax loop is a real implementation-bug surface) — resume here
  next session and write the code before moving to Floyd-Warshall/MST/
  Union-Find.** Block B (11 due Graph review #1s + Dijkstra review #1, due
  07-26/07-27) also untouched this session — user chose new material over
  reviews; still due, pick up before they compound.
- 2026-07-26 15:28 (3rd session today): Bellman-Ford **code written and
  closed** (the open item from 10:20). Two real code bugs, both caught by
  guided trace rather than hint — see mistake_journal. Pressure-test results:
  complexity/space clean, negative-weight condition clean, early-exit-variant
  analysis clean (same answer, faster, but hangs forever on a negative cycle
  — which is *why* fixed V-1 + a Vth detection pass is the right shape).
  Weak point: the Dijkstra visited-lock "why" needed 4 escalation rounds, 2nd
  time today, and the non-negativity monotonicity argument was misattributed
  to the priority queue rather than the weights. User was **correct** on a
  challenged point (with the guard in place, `Integer.MAX_VALUE` cannot
  overflow — the real reason for `1e8` is GFG's output contract); mentor
  framing was wrong, corrected in session.
  **Block B still untouched — 27 reviews now due (10 from 07-24, 6 from
  07-25, 11 Graph #1s from 07-26). Dashboard previously undercounted this as
  11; corrected. Next session must open with reviews, not new material.**
  Graph pending after this: Floyd-Warshall, Prim's, Kruskal's, Union-Find
  (do Union-Find before/with Kruskal's — Kruskal's depends on it).
- 2026-07-26 23:27 (4th session today): user chose new material over Block B
  again — started **Floyd-Warshall** (first exposure this cycle). Approach,
  base case (`dist[i][i]=0`, edges from input, else INF), and update rule
  (`dist[i][j]=min(dist[i][j], dist[i][k]+dist[k][j])`) all correctly
  self-derived, k correctly named as outer loop. But the "why k outer"
  invariant derivation stalled completely (2x "no idea") even after a
  concrete 3-node trace (A-2->B-3->C, no direct A->C edge) was set up —
  session ended mid-trace, k=A step walked by mentor, k=B step handed to
  user, unanswered. **Resume here next session: finish the A->B->C trace
  (k=B step: does dist[A][C] update via A->B->C?), then generalize to "why k
  outer" and complexity/space before moving to Prim's/Kruskal's/Union-Find.**
  See mistake_journal 2026-07-26 23:27.

## Topics Not Started — reclassified 2026-07-26

**Correction to 2026-07-10 confirmation**: user now recalls solving the
**complete Striver sheet ~2 years ago** (predates the current Codolio import
history), contradicting the 07-10 "simply wasn't covered" confirmation for
Stack/Queue, Sliding Window, Heaps, Greedy, Graphs. Reclassify all of these as
**rusty 2-year-old recall, not ground-up new material** — same treatment as
Binary Search/LinkedList/BST/Trees/Tries/DP (rusty-not-safe), just an older
decay window. Evidence fits: Dijkstra (2026-07-26) core mechanics came out
cold, clean, fast — a recall pattern, not first-exposure. Gaps that surfaced
(complexity notation, negative-edge case) are decay/detail loss, not missing
foundational knowledge.

Heaps, Greedy, and the sheet's final section (~129 problems) — still 0 solved
live this cycle, but treat as rusty-recall re-verification, not from-scratch
teaching. Expect faster re-derivation of core mechanics than a true first
exposure would take.

## Notes for Next Session

- 2026-09-01 17:15-18:47 (~92 min, user-set 120 — ended 28 min early, "lets
  solve some other probs" then wrap): **3 problems Accepted, 4/4 submitted this
  week's standard held.** Sudoku Solver (LC 37) closes bucket 2's constraint-set
  ladder at **12/15**; Single Number (LC 136, re-verify) and Single Number II
  (LC 137) open Bit Manipulation. LC 47 declined at approach, LC 260 posed and
  not started. **Reviews: 0 — 3rd consecutive skip, so the in-block review
  mechanism's own reversal trigger has now fired**; it goes to the audit as
  retired-or-enforced, not left nominally in force. Leech drill declined a 5th
  time (Bellman-Ford, Redundant Connection — 20 days).
  **The session's finding is that the algorithm was never the problem.** On LC
  37 both conceptual halves were cold (constraint tracking, and the base-case
  invariant), and every one of the six defects was mechanical. On LC 137 the
  whole derivation — why XOR fails, why the HashMap fails, count-mod-3, 32 slots
  including the sign bit — was correct before any code, and the code then said
  `%2`. **Derivation-to-code regression is now 2 for 2 across two sessions, at
  an interval of minutes**, and the 08-31 prescription (write the derived
  predicate as the first line of code) has not been run either time.
  **The genuinely new gap is arithmetic, not algorithms**: `(r/3)*3 + c/3` took
  12 minutes and a cinema-seat analog, and the same misunderstanding produced
  `i*3+j` for a 9-wide grid. Row-major flattening will recur on every grid
  problem; it is cheap to fix and worth a dedicated 15 minutes.
  **Process, unchanged and now costed**: 3rd occurrence of "do I need to code
  it?" (LC 136, answered honestly — low learning value there, but gate 4 means
  an unjudged problem stays on the list); 3rd paste without the one-line defect
  statement, which is the gate that would have caught `%2`; 5th hint-shape
  match (two defects named in one message, one fixed).
  **Tracker correction worth carrying**: PLAN B's "79 of 84 unnamed" is stale —
  Day 0 itemization partly ran on 08-31. Disk shows **~33 named and workable**
  (Graph 6, Stack/Queue 6, Strings 6, BitManip 5, Heap 4, Sorting 2, Trie 1,
  bucket 2's 3) against ~49 still `TBD`. Itemization is no longer an immediate
  blocker; deadline is before the named 33 run out, ~week 2.

- 2026-08-30 20:47-21:13 (~26 min, user-set 30): **review-only session, no new
  problem — first non-zero review session of the cycle.** New opening-review
  mechanism (adopted this morning's audit) ran for the first time: LC 79's
  `||`-chaining question closed clean, LC 216's `sum>=n` reason closed via
  guided derivation on the 3rd asking (first time not handed over), and the
  Task Scheduler `[leech]` daily recall went 2/2 clean — **graduates off
  `[leech]`, resumes the ladder at review #3 (due 2026-09-13)**. Ran ~7 min
  over the reserved 5-8 min review budget, so Word Break (LC 139, next in
  bucket 2) did not start this session — still next up. Process note: Task
  Scheduler opened with "i think i have solved this before" (2nd occurrence of
  the Frog Jump pattern) before the user engaged and answered clean anyway.
- 2026-08-28 21:26-22:13 (~47 min, user-set 60): **coverage day, 3 problems —
  1 long-open item closed, 2 new intake.** Frog Jump (DP-3) finally closed: the
  three follow-ups asked 2026-07-10 and never answered (n=1, complexity, O(1)
  space) were all answered today, and closing them **surfaced two defects in
  code that had been recorded as solved** — `dp[i-2]` indexed from `i=1` (crashes
  every `n>=2` input, so it had never been submitted) and a rolling-variable
  update that stored `oneStep` (a dp value **plus a jump cost**) where `dp[i-1]`
  belonged. Then Subsets (LC 78) cold, independent, correct first submit, and
  Combination Sum (LC 39) with-hints:2.
  **Three findings.** (1) **"I already solved this" is not evidence** — said
  twice this session, and the first time it was followed 10 minutes later by a
  crash bug and a wrong answer in the same problem. The whole-sheet
  rusty-not-safe framing now has a live demonstration rather than an argument.
  (2) **Copy-cost transfer failed inside 12 minutes** — the O(n) cost of
  `res.add(new ArrayList<>(list))` was derived correctly on Subsets after one
  nudge, then omitted again on Combination Sum, which uses the identical line.
  4th transfer-gap logged (DSU 08-07, fixed-window 08-11, template tie-rule
  08-27). (3) **A `Set` on a backtracking result is a branching bug** — the
  named lesson of Combination Sum, generalizable and now in
  `patterns/Backtracking.md`.
  **Process finding, and it blocks the queue**: bucket 1 of the post-cut
  coverage queue is "DP gaps 12", but the 12 are not itemized anywhere. The
  archived export (`codolio_import_raw.json`) names only Lec 1 (1) and Lec 2 (5)
  of the 56 — all 12 unsolved and 38 of the 44 solved are unnamed on disk. So
  bucket 1 **cannot be worked top-down as written**, and the first problem
  proposed from it (Ninja's Training) was challenged by the user as probably
  sitting in the *cut* 161-problem re-verification backlog, which was correct.
  Itemizing from the Codolio web UI was started and abandoned mid-way by user
  decision ("lets solve prblems"); session continued in bucket 2
  (Recursion/Backtracking), which is unambiguously scoped. **Bucket 1 stays
  blocked until the 12 are named — take it to the weekend audit.**
  Reviews: **none cleared, 8th consecutive zero-review session.** 3 "just tell
  me" requests (4 on 08-27), so 2 of 3 escalations again terminated at full
  explanation rather than co-derivation.
- 2026-08-27 17:20-18:45 (85 min, user-set 90): **coverage day, 3 new problems +
  1 follow-up, best raw output of the cycle** — LC 84 (Hard) with-hints:2, LC 907
  with-hints:4, LC 739 independent cold/first-submit, plus LC 42's O(1)-space
  follow-up closed. Four items.
  (1) **The justification streak broke in the right direction, twice.** LC 84's
  *why* ("taller bars can be cut down to h[i], shorter ones can't") and LC 739's
  (`>=` because "warmer" is strict) both came **cold, unprompted** — 2nd and 3rd
  cold justifications after 08-26's, against the 7-problem silent streak that
  preceded them.
  (2) **Template-first retrieval recurred, 2nd occurrence, and this time it cost
  a wrong answer.** LC 907 reused LC 84's `nsl/nsr` with strict `<=` on *both*
  sides. Harmless under `max` (LC 84), an overcount under `sum` (LC 907 → 8 vs 6
  on `[2,2]`). Same machinery three times today with three different tie rules —
  filed in [[MonotonicStack]] as the transferable rule.
  (3) **New class: derivation-to-code assembly gap.** LC 42's O(1) argument was
  derived cleanly and then not written; user asked for code outright. Four
  "just tell me" requests this session (LC 42 code, Java `Stack`, LC 907 both
  defects, LC 739 tie instance) — most escalations terminated at full
  explanation rather than co-derivation, the opposite of 08-26.
  (4) **Mentor error**: after LC 739's rule was stated correctly, the follow-up
  was pushed twice more for a concrete failing instance; user pushed back
  ("why are u irritating me"). **Standing fix: once the justification is stated
  correctly, stop — do not re-drill it for an instance.**
  Reviews: none (weekday, weekend-only policy); backlog 77, 7th consecutive
  zero-review session. Java track produced its first live signal in 49 days
  (`Stack extends Vector`, unknown).

- 2026-07-27 19:00 (5th session today, Block B review opened): Print Subarray
  with Maximum Sum `[derive]` review #2 — clean, start=tempStart derivation
  held unprompted. Mentor initially mis-flagged this as needing a hint (gave
  concrete numbers) and moving toward `[leech]`; user correctly pushed back —
  instantiating an abstract question with concrete numbers isn't a hint,
  corrected in CLAUDE.md standing rules. Min Stack `[derive]` review #2 posed,
  session interrupted before an answer — **resume there next**, then continue
  the remaining Block B batch (due 2026-07-24/25 items) — see
  review_schedule.md.
- Do not ask the user where we left off — read this file instead.
- Do not treat Binary Search/LinkedList/BST/Trees/Tries/DP as brand-new material (the
  underlying understanding is there) — but do NOT treat them as safe either. They were
  solved 2-3 months ago with zero practice since, so treat every one of them as "needs
  a real interview-speed re-solve, expect some rust" rather than a rubber-stamp review.
- Prioritize Arrays and Recursion first for genuinely new gap-filling, but interleave
  early re-verification reps of the stale "done" topics (start with DP and Binary
  Search — highest interview weight) so any decay surfaces in Week 1, not Week 4.
- Then move into Stack/Queue/Sliding Window/Heaps/Greedy/Graphs as genuine new material
  starting Week 2 — Graphs should not slip to Week 4.
- 2026-07-11: Frog Jump review #1 closed (found + fixed a second rust bug — missing
  dp[2] base case). Continue Arrays next session with rotate array (Basics
  subtopic next item), then Easy subtopic. All 5 Arrays problems solved today
  needed real derivation (only 2/5 fully independent) — Arrays rust/gap risk is
  real, keep interview-speed pressure on each new one rather than assuming
  early problems make later ones easy.
- 2026-07-12: Review #1 on all 5 prior Arrays problems — clean, no repeat
  mistakes. Basics+Easy subtopics finished; Medium subtopic started (Two Sum,
  Sort 012 done). Boundary/tail-case miss confirmed a 3rd time (Max Consecutive
  Ones) — treat as a standing checklist item: always check "what happens after
  the loop ends." Two deep stuck points (Rotate Array reversal trick, Longest
  Subarray Sum K negative-number generalization) plus one very deep one (Sort
  012 invariant reasoning) — see mistake_journal.
- 2026-07-12 (continued): Majority Element through Rotate Matrix done (9 more
  Medium problems) — Majority Element/Leaders solid, but 3 more deep-derivation
  stuck points (Kadane's all-negative edge case, Next Permutation's swap-partner
  + suffix-reverse rule, Longest Consecutive Sequence's O(n²)->O(n) fix). Guided
  one-line-at-a-time tracing (vs. asking for a full self-trace) is what
  unstuck Kadane's — worth defaulting to that style going forward.
- 2026-07-13: Spiral Traversal completed — deep stuck on outer-loop condition,
  resolved via guided tracing. Then review #1 on all 18 due Arrays problems
  (Rotate Array through Rotate Matrix): 16 clean (Linear Search skipped as
  trivial, not actually re-quizzed), 1 repeat-rust (Rotate Matrix — forgot
  full-row-reverse again, same gap as original solve, now a standing pattern
  worth extra attention). Then Subarray Sum Equals K — self-corrected a
  near-repeat of the Longest-Subarray-Sum-K sliding-window trap after being
  pointed at the mistake log. Next: Pascal's Triangle.
- 2026-07-17 (after a 3-day gap, no session 07-14 to 07-16): cleared entire
  overdue review backlog (26 items — all review #1/#2 items due 07-13 to
  07-16). 22 clean or single-hint; 6 needed real correction, all logged in
  mistake_journal: Second Largest (new sentinel-value bug), Rotate Array
  (split-boundary k vs n-k confusion), Longest Subarray Sum K (seed-value
  reasoning gap, resolved), Stock Buy/Sell (reverted to wrong -1 floor),
  Next Permutation (pivot index + strict-vs-equal swap regression — most
  significant), Rotate Matrix (new diagonal-transpose slip, but the
  standing full-row-reverse repeat-rust did NOT recur this time). Then
  solved Pascal's Triangle (with-hints:2). Then started **Print Subarray
  with Maximum Sum** — genuine new bug found: candidate solution tracked a
  running max correctly (matches standard Kadane's value) but collapsed the
  recorded start/end pointers to the *current single index* every time a
  new max was found, instead of using a separate `tempStart` (window-start,
  only reset when sum<0) vs `start` (best-window start, set to `tempStart`
  — not current index — when a new max is found). Confirmed broken via
  concrete trace on `[-2,1,-3,4,-1,2,1,-5,4]` (max=6 tracked correctly, but
  reported subarray would be wrong). **Mid-derivation when session ended —
  user was walking through the tempStart-vs-start distinction one step at a
  time (guided tracing), had correctly identified tempStart=1 after the
  first reset, next question in progress was: at index 5 (new max, no reset
  since index 3), does `start` become 5 or `tempStart`(=3)? Resume here —
  do not restart from scratch, continue the guided trace.**
- 2026-07-20: user pasted a **correct** full implementation of Print Subarray
  with Max Sum unprompted (in a non-prep session) — `start=tempStart` on new
  max (the exact stuck point, now resolved in code), max-update-before-reset
  order correct (old Kadane's bug did not recur), verified clean on
  `[-2,1,-3,4,-1,2,1,-5,4]` → (3,6) and all-negative `[-3,-1,-2]` → (1,1).
  **Close-loop still pending** before marking resolved: (1) explain in words
  why `start=tempStart` not `start=i`; (2) walk `[5]` single-element edge.
  Run those two questions at next session start, then mark resolved and put
  the 07-17 mistake entry on the normal review schedule.
- 2026-07-20 (prep session): closed item (1) — full guided one-line-at-a-time
  re-trace of the whole array from scratch (not just the stuck point),
  user correctly derived `start=tempStart` (not current index) and
  explained why in own words. Item (2) (`[5]` single-element edge) not
  explicitly run — deferred to review #1 (2026-07-21, `[derive]`-tagged).
  Then reviews #2: Linear Search (clean), Spiral Traversal (real
  correction — repeat of 07-13 guard confusion, new `bottom--` direction
  slip, pass 3/4 direction swap), Subarray Sum Equals K (real correction —
  lookup-vs-insert `+1` conflation). Arrays Medium subtopic now complete
  (15/15); only Hard (11 problems) untouched. Next: Block A (Stack/Queue,
  new material, Week 2 priority, still untouched).
- 2026-07-20 (Block A, Stack/Queue started): Valid Parentheses and Min Stack
  both solved independently, clean. Next Greater Element: correct
  monotonic-stack approach and full trace derived cold, but first code
  attempt pushed the computed answer onto the stack instead of the original
  value (self-corrected once shown a failing trace) — see mistake_journal.
  Also backfilled `DSA/patterns/*.md` for 7 already-used patterns (Kadanes,
  TwoPointers, ReversalAlgorithm, NextPermutation, PrefixSumHashmap,
  BoundaryShrinkingTraversal, MatrixTransposeRotate) — was stale/empty
  despite being in use since Week 1. Then Implement Queue using Two Stacks:
  correct lazy-transfer algorithm derived cold, amortized-complexity
  reasoning needed real Socratic escalation (concrete per-element move-count
  trace) before landing — session wrapped after. Next: continue Stack/Queue
  (more problems) or move to Sliding Window.
- 2026-07-24 (carryover reviews, all `[derive]`, all overdue since 07-21):
  Next Greater Element review #1 — mechanics clean cold, but "why pushing
  ans[i] instead of arr[i] breaks it" needed heavy escalation (counterexample
  trace + direct prompts) before landing — 2nd time this exact point needed
  real help (1st was self-caught during original coding). Implement Queue
  using Two Stacks review #1 — clean, no hints, better than original solve's
  amortized-complexity struggle. Rotate Matrix (90°) review #3 — clean: both
  historically-buggy points (transpose diagonal i<j, full row-reverse exact
  bounds) nailed precisely this time, no repeat rust. Frog Jump (DP-3) review
  #3 — 1 hint (pushed from "just take min" to naming the two-option
  jump-cost framing), no repeat of the Fibonacci-shaped bug. Then started
  **Sliding Window** (new topic, Week 2 material carrying into Week 3):
  Maximum Sum Subarray of Size K (fixed window) and Longest Substring
  Without Repeating Characters (variable window, hashset) both solved
  independently, cold, no hints — user declined to write code for either
  (judged unnecessary once approach+complexity+edge case confirmed verbally).
- 2026-07-24 (continued, Sliding Window Block A): Max Consecutive Ones III
  (clean), Fruit Into Baskets (clean), Longest Repeating Character
  Replacement (heavy escalation — false belief net window length can
  shrink post-shrink, corrected via guided trace), Minimum Window
  Substring (independent, then walked through O(1) matched-counter
  refinement) all solved. `DSA/patterns/SlidingWindow.md` updated with the
  At-most-K monotonic-best variant. Then switched to Block B reviews
  (12-item cap, front-loaded oldest-due + `[derive]` items): Pascal's
  Triangle review #1 (1 hint, same loop-bound point as original solve —
  self-corrected via trace), Nearest Smaller to the Left review #1
  (escalation needed again on the generalized traversal-direction rule,
  mechanics solid), Stock Span Problem review #1 (clean this time, no
  repeat of the off-by-one). Sort 0s/1s/2s review #3 posed, session ended
  before an answer. **Resume here next session: Sort 0s/1s/2s `[derive]`
  review #3 (why does the invariant hold), then continue the remaining 8
  of the 12-cap Block B batch — see review_schedule.md.**
- 2026-07-21 (Block A, Stack/Queue continued): Nearest Smaller to the Left
  solved — instance mechanics (left-to-right traversal, pop-while->=
  including ties) derived correctly and fairly quickly, but generalizing
  "why does traversal direction depend on the problem" into a transferable
  rule needed real Socratic escalation (two circular answers before guided
  questions about stack contents at index i got there). Landed on: start
  traversal from the end matching the query side. See mistake_journal.
  Updated MonotonicStack.md pattern file with the generalized rule and
  added flashcards. Then Stock Span Problem: correctly identified span as
  the distance from the nearest-greater-left index, but the formula had an
  off-by-one (`curIndex-ngeIndex-1` instead of `curIndex-ngeIndex`) —
  resolved by deriving via inclusive-range counting (`b-a+1`) rather than
  guessing the offset. See mistake_journal. Next: continue Stack/Queue or
  move to Sliding Window.
- 2026-07-25: Sort 0s/1s/2s `[derive]` review #3 closed — invariant "why"
  derivation held via elimination framing (regions, why 0-case swap is safe,
  why 2-case must recheck mid, why loop terminates), 1 light nudge, no
  repeat of original deep confusion. Move Zeroes to End review #3 clean, no
  hints. Then switched to Graphs (new topic, Week 3 top priority, previously
  0%): BFS Traversal and DFS Traversal both solved with 1 hint each (BFS:
  code contradicted own "visited-at-push" derivation; DFS: initially
  proposed visited-on-exit, corrected via 0-1 cycle counterexample). Number
  of Provinces (counter init 1→0 self-corrected) and Number of Islands
  (clean) both approach-only, code skipped by user judgment. Remaining
  Block B batch (Remove Duplicates #3, Max Consecutive Ones #3, Set Matrix
  Zeroes #3, Longest Consecutive Sequence #3, Two Sum #3, Rearrange by Sign
  #3 + overflow) deferred to evening session — **resume there next,
  before new material.**
- 2026-07-25 (evening, overdue-review sweep): Set Matrix Zeroes review #3
  clean, no hints. Longest Consecutive Sequence review #3 — pruning
  mechanic clean, but "why O(n)" needed 1 escalation (inner-while-visited-
  once accounting), 2nd time this exact justification needed help, tagged
  `[derive]` going forward. Two Sum review #3 posed, session interrupted
  before an answer — **resume there next** (Rearrange by Sign #3, Leaders
  #3, Majority Element #3 still queued after).
- 2026-07-21 (Block B, review batch — 8 of 12 due items done, cap hit):
  Valid Parentheses (clean), Second Largest (clean), Kadane's (order clean,
  "why" needed 1 hint), Min Stack ("why not global var" needed real
  escalation, 2 hints), Rotate Array (heavy escalation, "why" derivation
  still absent 3rd time), Longest Subarray Sum K (1 hint, extra +1
  confusion), Next Permutation (clean, exact regression point held), Print
  Subarray with Max Sum (heavy escalation — item 1 derivation had fully
  decayed AGAIN since "closed" 07-20, item 2 `[5]` edge case now clean).
  Created new pattern file `StackAugmentedState.md` for Min Stack's
  per-frame-min technique (parked mid-session, added at save). **4 items
  from today's 12 NOT done — session interrupted mid-question on Next
  Greater Element**: Next Greater Element, Implement Queue using Two
  Stacks, Rotate Matrix (90°), Frog Jump (DP-3) — all still due, pick these
  up first next session before new material.
- 2026-07-27 19:17 (tooling session, no problems solved): built
  `tools/build_dashboard.py` — parses cycle/schedule/archive/progress/journal/
  SystemDesign into a generated HTML dashboard (`Progress/dashboard.html`),
  plus `Progress/metrics_history.jsonl` snapshots. Counts in dashboard.md are
  now read off that script rather than hand-tallied. Findings worth keeping:
  (1) **clean review rate 71% across 75 completed reviews**, and it drops to
  **36% at review #3** vs 74%/72% at #1/#2 — see statistics.md; (2) the
  dashboard's parser health check found Nearest Smaller to the Left and Stock
  Span Problem scheduled for review with no Completed Problems entry —
  **backfilled above, and added to topics/MonotonicStack.md**, which was also
  missing them; (3) statistics.md's stale "not covered"/"no data yet" lines
  corrected. **Policy change: stop opening every session with a full 12-item
  Block B** — with 13 days left and 4 tracks at zero, cap reviews at ~5 (leech
  + `[derive]`) and spend the rest on LLD/Behavioral/Java. Rationale in
  dashboard.md Reviews Due. Still open from 07-26: Floyd-Warshall "why k
  outer" mid-trace, and Prim's/Kruskal's untouched.
- 2026-07-30 17:05 (Block B, capped at 4 per the 07-27 policy — no new
  problems solved): Min Stack `[derive]` #2, Dijkstra `[derive]` #1,
  Bellman-Ford `[derive]` #1, Redundant Connection `[derive]` #1. **None
  fully clean** — see mistake_journal 2026-07-30 for all four. Headline
  signals: (1) Dijkstra's tracked attribution question came out **correct and
  cold** for the first time (07-26 missed it twice) — the remaining gap is
  reproducing the contradiction proof unprompted, not the attribution; a
  `[leech]` tag was raised mid-session and **retracted** as over-tagging
  (user pushed back, correctly — it was being applied to a harder test than
  the schedule specified). (2) **Bellman-Ford regressed in 4 days**: negative
  edge vs negative cycle, and V-1 justified by degree count rather than
  edges-on-a-path — both were clean cold on 07-26. This is the clearest
  stale-recall datapoint yet on freshly-derived graph material. (3) Recurring
  shape across all four: mechanics recalled fine, *consequences* absent
  (what breaks, what it costs). Kosaraju #1 deferred to keep time for Block A.
  **Block A did not happen** — Floyd-Warshall was re-posed at the exact 07-26
  stall point (k=B pass on A-2->B-3->C: does dist[A][C] update?) and the
  session ended before an answer. **Resume there next session, first thing.**
  Prim's/Kruskal's still untouched. Zero-track slot also missed — 4 tracks
  still at zero with 10 days left.
- 2026-07-31 15:49 (Block A, Floyd-Warshall "why k outer", 3rd session on
  same stall): concrete 4-node counterexample trace (A-1->B-1->C-1->D) run
  fully — user correctly traced both the correct k-outer result (dist[A][D]
  =3, using dist[A][C]=2 already fixed by the k=B pass) and the broken
  k-inner case (dist[A][D] stays INF because no bridge value had been
  opened yet). Named-analogy explanation (hubs "opening" one at a time)
  given, but the closing "explain the invariant in your own words" question
  was not answered before session end — session moved to save/wrap-up
  instead. **Resume here next: re-ask the closing invariant question first
  (dist[i][j] after k=B pass = ?), do not re-run the trace from scratch —
  it's held, only the generalization/naming is missing.** See
  mistake_journal 2026-07-31 15:49 (Recurrence 3+). Prim's/Kruskal's/
  Union-Find-before-Kruskal's still queued after. Zero-track slot (Java/LLD/
  Behavioral/SystemDesign) missed again — 9 days left, still 4 tracks at
  zero.
- 2026-08-01 09:24 (2nd session today): switched off Floyd-Warshall, started
  **Min Cost to Connect All Points** (queued since 07-27, next core Graph
  algo — Prim's/Kruskal's). Approach (Kruskal's via PQ of all-pairs edges +
  union-find) self-derived cold. Complexity O(n^2 log n) needed 1 nudge
  (initially multiplied wrong, n^3 log n). Correctness (cut property/swap
  argument) needed heavy escalation — 3 circular answers before a concrete
  3-node numeric counterexample landed it; full formal proof depth flagged
  by user as too intimidating and correctly capped at interview bar (see
  [[feedback_socratic_teaching]] depth-cap update). Alternative approach
  (array-based Prim's, O(n^2), better for this dense graph) identified with
  light prompting. Edge cases (n=1 -> 0, duplicate points -> 0-weight edge)
  both correct, no hints. **Code not yet written — resume here next session,
  write Kruskal's (or Prim's) code before moving on.** See mistake_journal
  2026-08-01 09:24.
- 2026-08-01 08:35 (4th stall on Floyd-Warshall "why k outer"): re-posed
  cold, still "i dont know why outer loop correct then inner one" — no
  progress since 07-31. Built an interactive step-through artifact
  (k-outer vs k-inner trace, A-B-C-D chain, both modes user-steppable) as a
  self-study aid instead of another guided verbal derivation this session —
  no answer attempted against it yet. See mistake_journal 2026-08-01 08:35
  (4th occurrence, same exact point). **Resume here next: re-ask the
  closing invariant question after the user has used the artifact, don't
  default straight to another guided trace.** Prim's/Kruskal's/
  Union-Find-before-Kruskal's still queued after. Zero-track slot missed
  again — 8 days left, still 4 tracks at zero. Session also spent time on a
  a careers-site application (profile edits, not yet submitted) — no
  InterviewPrep tracker entry per the save skill's "only log if it actually
  went out" rule.
- 2026-08-01 16:14 (3rd session today): Floyd-Warshall "why k outer" **finally
  closed at 16:32** (5th attempt) — abandoned the abstract A-B-C-D re-trace
  and anchored on two concrete pair-values (dist[A][C]=2 fixed after k=B,
  dist[A][D]=INF still) before generalizing; landed clean. Deeper
  "prove k-inner breaks concretely" follow-up was correctly capped as
  over-depth by user, same as Kruskal's cut-property earlier the same day.
  Then **Kruskal's code written** for Min Cost to Connect All Points (LC
  1584): `parent[0]` bug (relied on `int[]` zero-default, loop started at
  i=1) found + fixed; complexity O(n²log n) confirmed cold; rank-vs-path-
  compression tradeoff needed 1 nudge (dominated by the n²log n term either
  way). Then **Prim's heap-based version**: real mistake caught before
  coding — relax rule initially described as cumulative ("like Dijkstra"),
  corrected via a 3-node counterexample (A-B=10,A-C=1,C-B=3) showing
  double-counting; code then written clean, matches an already-accepted
  submission. Then **Prim's array-based O(n²) version** (first exposure,
  the "better for dense graphs" variant flagged 09:24): min-scan sub-step
  self-derived, but full assembly needed mentor scaffold after "i dont
  know this approach" — verified against the LeetCode 1584 editorial
  thread (user pasted it after a WebFetch 403), confirms exact match to
  the "Prim's for Complete Graph" optimization. **All of this session's
  target queue (Floyd-Warshall close, Kruskal's, Prim's) is now done** —
  core graph-algorithm coverage complete, remaining Graph work is
  review-ladder, not new material. Zero-track slot (Java/LLD/Behavioral/
  SystemDesign) missed again — 8 days left, still 4 tracks at zero, this
  is now the top gap heading into final week.
- 2026-08-01 18:41 (6th session today, review-cap-policy + pace-projection
  session, no new problems solved): Rotate Array `[leech]` review #4 —
  closed **clean** (see review_log_archive.md), 1 of 2 consecutive clean
  needed to graduate off leech. Mentor initially over-flagged it as "not
  clean" for lacking one polished synthesized paragraph despite every
  causal piece already being correctly produced across a concrete trace —
  user pushed back hard, mentor retracted and tightened its own teaching-
  pace rule (see `[[feedback_socratic_teaching]]`, pace-cap section). Then
  ran `interview-prep-pace`: full-455 + all-tracks completion at current
  61% show-rate projects to ~mid-December, DSA-alone to ~late-November —
  neither is close to the original 2026-08-09 target. User chose to extend
  `target_end` to **2026-08-23** (cycle.md, 30day-sprint.md, dashboard.md
  all updated, with an explicit Extension-section caveat that 2 weeks alone
  doesn't close the gap) and to lower the review cap to ~3-5/session
  (leech+`[derive]` priority only, rest of session time to new material) —
  see dashboard.md Session Protocol. Redundant Connection `[derive]` review
  #2 was posed (who reads `rank`, cost of an inflated value) but never
  answered — session got redirected to the pace/target discussion.
  **Resume there next**, then pick new material (Heaps continuation or
  Greedy start, both floated but neither chosen before session end).
- 2026-08-02 10:43 (short session, ~10 min): user chose new material over
  Block B — reviews proposed (Redundant Connection #2, Rotate Array
  `[leech]`, Kth Largest #1, Top K Frequent #1) and **all skipped again**,
  backlog now 40. Started **Find Median from Data Stream (LC 295)**, Heaps
  continuation. Two-heap structure named cold and unprompted, but halves
  assigned backwards (min-heap for the lower half) while simultaneously
  saying the spare element sits in the max-heap — self-corrected after one
  concrete-instantiation question (`[1,2,3,4]`, which two values produce
  2.5). Second occurrence in two days of naming a heap type before deriving
  what its top must be (1st: Top K comparator, 08-01 22:00). **Not solved —
  resume here next: `addNum` rule (which heap to push to, rebalance
  condition) traced on `5,3,8,1`, then complexity. Naive-baseline cost
  (no heaps) asked twice, never answered — re-ask it.** Zero-track slot
  (Java/LLD/Behavioral/SystemDesign) missed for the 6th consecutive
  session — 21 days left, still 4 tracks at zero.
- 2026-08-02 16:54 (2nd session today, ~60 min, new material only): user
  asked for new problems, Block B skipped again (4th consecutive session,
  backlog 43). **LC 295 closed** — see Completed Problems; both code bugs
  were found by making the user trace their own `while` condition term by
  term rather than by reading the code aloud, which is what the last two
  heap sessions lacked. **LC 23** approach-only. **LC 621 started Greedy**
  — approach correct, two rule details wrong and self-corrected, but the
  closed-form formula decayed within minutes of the user deriving it.
  **Resume here next: LC 621 — re-derive `(maxFreq-1)*(n+1)+countMax` from
  the block picture cold, then the `max(formula, tasks.length)` failure
  case (`[A,A,B,B,C,C,D,D]`, n=1 — formula 6, true 8), then edge cases,
  then code.** Session-conduct signal worth watching: in multi-part asks
  the user reliably answers the last part and drops the rest — the
  naive-baseline question needed 5 asks and edge-cases 3 before landing.
  Ask one question at a time when the answer is load-bearing. Also flagged
  and unresolved: OJ links are not clickable in the user's terminal in
  either bare or markdown form — terminal-side, not output-format-side.
  Zero-track slot missed for the **7th** consecutive session.
- 2026-08-04 (short session): LC 621 review #1 (1 day late) — formula
  decayed again exactly as predicted (2nd occurrence, 1 more triggers
  `[leech]`), rebuilt via two traces (A×3,B×3,n=2 caught the `n` vs `n+1`
  and `maxFreq` vs `countMax` errors; index-diff trace closed the "why
  n+1" gap), closed the loop verbally this time. **Still open — resume
  here next: the `max(formula, tasks.length)` "why undercounts" question
  was posed but unanswered, then edge cases, then code.** Zero-track slot
  missed for the **8th** consecutive session.
- 2026-08-05 (new material only, LC 621 review still not revisited): **N
  Meetings in One Room** closed — sort-by-end + strict boundary self-derived
  cold, but "why end-time not start/duration" needed heavy escalation both
  times (2 constructed counterexamples) before landing clean; edge cases
  clean. Then started **Minimum Number of Platforms**: two-pointer sweep +
  arrival-before-departure tie-break self-derived cold with correct
  reasoning; O(n log n)/O(1) clean, correctly explained why no pairing is
  needed here (unlike N Meetings). Edge cases: empty/all-simultaneous clean,
  but the fully-chained case (`(1,5),(5,9),(9,13)`) got two wrong reflexive
  formula guesses (`n/2`, `(n+1)/2`) before a forced step-by-step trace
  landed the correct answer (2, not n-dependent) — the generalizing "why does
  it cap at 2 regardless of chain length" question was posed and **session
  ended before an answer**. **Resume here next: re-ask that question before
  anything else, do not re-run the trace from scratch (it's held, only the
  generalization is missing)**, then close edge cases, then code (not yet
  attempted). LC 621 review #2 (due 08-05, still open, one more miss
  triggers `[leech]`) also not revisited. Zero-track slot missed for the
  **9th** consecutive session.
- 2026-08-06 (new material only, user explicitly chose new-before-reviews
  this session — LC 621 review #2 skipped again, 6th consecutive session):
  **Minimum Number of Platforms** generalization closed — combined
  yesterday's "arrival coincides with departure" answer with today's
  "each interval touches only its immediate neighbor, never overlaps two"
  to derive why max platforms caps at 2 regardless of chain length. Code
  still not written. Then **Jump Game (LC 55)** closed — independent cold
  solve, full code, no bugs; "why greedy" needed 1 targeted question. Then
  **Jump Game II (LC 45)** closed — heap-based O(n log n) self-derived
  cold, then self-optimized to O(n) two-pointer unprompted once asked if
  the heap was necessary; no bugs in either. Then **Job Sequencing
  Problem** started — two real approach mistakes (deadline-sort instead of
  profit-sort; earliest-slot instead of latest-slot placement), both
  self-corrected via constructed counterexamples the user traced by hand;
  code correct once fixed. **Pressure-test (complexity of the slot-search
  loop, all-same-deadline edge case, faster-than-current approach) posed,
  unanswered — resume there first next session.** Zero-track slot missed
  for the **10th** consecutive session.
- 2026-08-07 (short session): **Job Sequencing pressure-test closed.**
  Per-job scan bound (≤ d), worst-case shape (all deadlines = n, not all =
  1), and the n(n-1)/2 → Θ(n²) sum all derived cold with no hints. Then the
  "beat O(n²)" question: category hint and parking-lot analog both failed,
  user asked directly, DSU slot-find given as full explanation (first
  transfer-gap entry — technique known from Redundant Connection, not
  retrieved outside Graphs). Close-the-loop question posed but user moved
  on — **re-ask next session: why does `parent[slot] = slot-1` stay correct
  when slot-1 is itself already full?** Then **Fractional Knapsack** posed
  (greedy-key question) — unanswered, session went to `interview-prep-pace`
  instead. **Resume there.** Pace re-run 22:13: ~149h remaining vs 17 days
  = ~8.8h/calendar day, ~13.7h/active day at the 64% show-rate (18/28) —
  not achievable; ~120h of that is DSA new + stale-backlog, the
  lowest-yield share while 4 tracks sit at zero. Scope cut recommended, not
  more effort. Zero-track slot missed for the **11th** consecutive session.
- 2026-08-08 (short session, ~35 min): **Job Sequencing fully closed, three
  approaches.** User brought a **pasted GFG heap solution** (self-disclosed,
  logged as read-not-derived, on the ladder at review #1 with no solve
  credit). Everything around it was genuinely cold: why the sort key flips to
  deadline-ascending in this shape (the heap does the selecting, sort only
  supplies feasibility order), O(n log n)/O(n), and `!pq.isEmpty()` being a
  dead branch since `size >= d >= 1`. The one real gap: the no-regret
  exchange argument took **4 escalations** — first answer circular ("removing
  the min won't hurt"), next two stayed at mechanic level, landed only after
  a concrete before/after heap swap forced the count-invariance out. **Third
  greedy-*why* escalation in three Greedy sessions** (08-05 N Meetings, 08-06
  Jump Game, 08-08 here) — the standing shape is mechanics cold, justification
  needing help; worth opening the next Greedy problem with the "why" rather
  than the mechanics. Then the DSU close-the-loop question (3rd posing,
  dodged twice) closed in **1 nudge** — real improvement over 08-07's full
  explanation. **Fractional Knapsack posed a 3rd time, still unanswered —
  resume there, first thing.** Reviews: none cleared, backlog still ~56, LC
  621 review #2 now 4 days late (one more miss = `[leech]`). Zero-track slot
  missed for the **12th** consecutive session. Pace/scope-cut decision from
  08-07 still not made.
- 2026-08-08 20:46 (2nd session today, ~35 min): **Fractional Knapsack finally
  attempted** (4th posing). Mechanics cold and correct — value/weight ratio,
  max-heap, fraction of the final item. Opened with the *why* rather than the
  mechanics, per the standing signal, and the justification came back circular
  ("we want max value so we pick the highest ratio") — goal-restatement, same
  shape as the 08-08 heap-eviction answer. Escalated to a concrete unit swap
  (W=10, A w6/v60, B w10/v50, claimed-optimal 2A+8B — swap 1 unit of B out for
  1 of A, compute the delta); **session ended before the answer. Resume
  exactly there — do not re-pose the ratio question, that half is held.** Then
  complexity, edge cases (capacity 0, one item heavier than W, all-equal
  ratios), and code — none attempted. Created
  `patterns/GreedyExchangeArgument.md` to hold the justification skeleton,
  since this is now the 4th consecutive Greedy session failing the same way.
  Reviews: none cleared again (9th consecutive session), backlog 57, LC 621
  review #2 now 5 days late. Zero-track slot missed for the **13th**
  consecutive session. Pace/scope-cut decision from 08-07 still not made.
- 2026-08-08 23:24 (3rd session today, ~22 min): **Fractional Knapsack closed
  except code.** The exchange argument came out — first real greedy
  justification produced in 5 Greedy sessions — but only through the full
  guided ladder: "i didn't get it" on the swap setup, then per-unit values
  (10, 5) correct, then a wrong delta (20) before old-total/new-total (60, 65)
  were traced line by line, then the conclusion stated as a *rule* ("take max
  of A, fill rest with B") before a fill-in-the-blank forced the proof form
  ("we can construct a better packing, so P is not optimal"). Concrete
  instantiation is what works here — the abstract form fails every time.
  Complexity: time cold, space wrong (O(log n)) from an unknown library fact —
  object-array `Arrays.sort` = TimSort, O(n) auxiliary; primitives =
  dual-pivot quicksort, O(log n) stack. Told directly, same handling as
  build-heap O(n) on 08-01. Edge cases: 4/4 clean cold, best block of the
  session. **Code not written (user declined) — resume there: the comparator
  direction and the integer-division trap in the fractional step are the two
  live bug surfaces, and the last three code-skipped problems have all come
  back weaker.** Reviews: none cleared (10th consecutive session), backlog now
  58 with this problem added, LC 621 review #2 5 days late. Zero-track slot
  missed for the **14th** consecutive session. Pace/scope-cut decision from
  08-07 still not made.
- 2026-08-09 16:43 (~30 min): **Fractional Knapsack fully closed** — code
  correct first try and cold, both predicted bug surfaces clean, space right
  this time. Heap-vs-sort pressure test clean including when the heap actually
  wins. Then **Candy (LC 135)** — new problem, new pattern shape for this user
  (two-pass constraint propagation, not selection-order greedy; the user asked
  the classification question directly, so it was answered and filed as
  `patterns/TwoPassConstraintPropagation.md`). Split result: everything
  mechanical cold (floor, two passes, both arrays, max merge, O(n)/O(n),
  one-array refinement) and the **minimality** proof cold; the **validity**
  proof took the full escalation ladder and only moved on concrete
  instantiation — 3rd session running where the abstract form of a
  justification fails and the numeric form works. O(1) run-length variant
  parked mid-derivation at the user's call ("too confusing") — **resume there
  or drop it; it is an optimisation, the two-pass answer is interview-
  sufficient.** Code declined — **Candy code is the first open item next
  session.** Reviews: none cleared (**11th** consecutive session), backlog 59.
  LC 621 review #2 6 days late and **now tagged `[leech]`** per the standing
  miss rule. Zero-track slot missed for the **15th** consecutive session.
  Pace/scope-cut decision from 08-07 still not made — 14 days left.
- 2026-08-11 20:05-20:30 (~25 min, first session under the DSA-First Coverage
  Plan): **Assign Cookies (LC 455) closed** — code cold and correct first try,
  the first problem under the new "full code every problem" rule and it cost
  nothing. Sort-space nudge (said O(1), primitives take O(log n) quicksort
  stack) — 2nd sort-space miss in 4 days, now a standing checklist item.
  Exchange argument again needed the ladder, but **the session's real output
  was meta, not the problem**: the user asked directly what "instantiate →
  symbolize → conclusion form" means, then what the conclusion form *is*, then
  how to use it in a live interview. All three answered and filed in
  [[GreedyExchangeArgument]] (two proof shapes + a 4-sentence interview script).
  This is the first time the user has asked for the *method* rather than the
  answer — treat the script as the thing under test next Greedy problem: ask
  for the rule first, rival second, move third, close fourth.
  **Lemonade Change (LC 860) posed with link, not attempted — session ended
  there. Resume on it cold.** Block 2 (`+1` review: Candy `[derive]`, LC 621
  `[leech]`) did not run — **13th** consecutive session with no reviews cleared,
  and the first miss of the new plan's non-negotiable block. Backlog 68→69.
- 2026-08-12 17:11-17:52 (~41 min, user-declared 45-min block): **plan amendment
  first — user's standing instruction is "always coverage, reviews on weekend."**
  The daily `+1` block is removed from weekday sessions; recorded in
  `../../Progress/30day-sprint.md`. Consequence stated once and not re-raised:
  Monday's problems now get their first review on day 5+, so the steep part of
  the curve is untested. **Lemonade Change (LC 860) closed** — one real bug
  (sorted an order-dependent input), rest cold, edge case cold, O(n)/O(1). The
  greedy *why* needed 4 exchanges for the **7th** consecutive Greedy problem —
  but the unlock is now reproducible and specific: **"write both wallets right
  after the same customer; what's the exact difference?"** The 4-sentence
  interview script was offered and declined ("I already solved the problem"), so
  it is still untested live after being written down 08-11 — pose it as the
  *first* question on the next Greedy problem, before the code, or it will keep
  getting skipped as redundant. **Valid Parenthesis String (LC 678) parked
  mid-derivation** at the `(min,max)` representation with the solidity induction
  complete — resume there, do not restart. New signal worth watching: the user
  asked "how do we guarantee it's a solid run and not holes" **unprompted** —
  first time a proof obligation has been raised by the user rather than the
  mentor. Counter-signal same session: a full stall on applying their own
  counter rule to a single number, 4 minutes after stating it (3rd short-horizon
  decay, after Floyd-Warshall and Task Scheduler); quoting their own rule back
  recovered it in one step. Reviews: none — **14th** consecutive session, now by
  explicit policy rather than slippage. Backlog 69→70.
- 2026-08-12 20:11-20:38 (~27 min, user-declared 25-min block; 2nd session
  today): **Valid Parenthesis String (LC 678) — derivation finished, code still
  open.** Resumed at the park point as planned, no restart. All four open pieces
  landed — the three update rules, the `max<0` bail-out with its justification,
  the min-clamp, and the accept condition — but **every one needed escalation**,
  and the session's real finding is *why*: the question "min and max are the min
  and max of what collection?" was asked three times and never answered, so the
  clamp and the bail-out had no referent. That surfaced explicitly at the end
  ("i dont think i really understand why am i even implementing this"), at which
  point the state's meaning was supplied outright. **Standing fix, for any
  problem carrying compressed state: do not proceed to mechanics on a vague
  answer to "what does this state mean" — the mechanics get memorized and the
  interview's "why" question has nothing behind it.** Two mechanical failures
  worth their own entries: the correct reachable set was produced and then
  misread when stating the rule (twice, both recovered by "what's the min of the
  set you just wrote?"), and when asked to trace `)` through their own code the
  user patched a line instead — deleting a correctly-derived `min--` and breaking
  `()` — leaving the actual defect (`else if` makes the `max<0` check
  unreachable) untouched. **Resume next session on that code**: trace `)` and
  `()`, restore `min--`, unchain the two checks, then state complexity (never
  given). Reviews: none — **15th** consecutive session, by weekend-only policy.
  Backlog still 70.
- 2026-08-13 17:03-17:39 (~36 min actual, user-set 45-min block): **LC 678 code
  closed** (both defects fixed by the user; the dead `else if` chain located in
  2 questions, `min--` restored unprompted, `")*"` counterexample built via a
  3-step ladder, return simplified to `min==0`), then **Merge Intervals (LC 56)
  solved cold with full code, no bugs, no escalation** — including the
  last-interval-only justification and spotting the tie-break as dead code.
  Notable: the Greedy justification streak broke here — 8 consecutive problems
  had needed the ladder for the *why*, this one did not. Two process items.
  (1) **Open item, user-parked**: why `min==0` alone is the whole accept
  condition; both halves were stated back correctly but the user said "I didn't
  get it fully" and chose to move on — re-pose it at the LC 678 review, do not
  re-open it cold. (2) **Mentor error, logged not repeated**: Merge Intervals'
  last-interval question was re-asked after a substantially correct answer, and
  the user pushed back ("you're irritating me with question 2 every time").
  Same class as the 2026-07-27 hint-grading correction — a correct answer in
  general terms is closed, not a candidate for one more round. Standing rule
  added to `../../CLAUDE.md`. Reviews: none — **16th** consecutive session, by
  weekend-only policy; backlog 70, weekend batch is 2026-08-15/16.
- 2026-08-14 22:20 (~29 min, user-set 30): coverage only, 1 problem.
  **Insert Interval was posed first and declined as boring** after ~6 min with
  no attempt ("i dont like this problem" → routed with one question, boring vs
  murky, boring) — swapped to a different shape rather than pushed. Both Insert
  Interval and Non-overlapping Intervals stay queued; do not re-pose Insert
  Interval as the opener next session. **Shortest Job First** then went cold
  and correct in code, but the *statement* needed a guided trace before the
  algorithm could start — new failure surface, distinct from every prior entry
  (all of which were mechanics or justification). **Process item: the
  4-sentence greedy script has now been declined 3 times** (08-12 "I already
  solved the problem", 08-13 not posed, 08-14 "we don't need script for all the
  problems"). The user's objection is reasonable on its face — it is not a
  per-problem ritual — so stop posing it as a script. Ask the one-sentence
  *why* instead and reserve the full four sentences for a problem where the
  rule is genuinely non-obvious. Reviews: none — **17th** consecutive session,
  weekend-only policy; weekend batch is tomorrow, 2026-08-15/16.

### 2026-08-15 15:10-17:20 (~130 min, user-set 120 + overrun to close LC 435) — weekend review batch + 1 new problem

First weekend batch under the 2026-08-12 weekend-only amendment, and the first
session in **18** to clear any reviews at all. 12 reviews run, then one new
Greedy problem by user request.

**The amendment's feared failure did not appear.** The watch-item was whether
review #1 outcomes would come back `correction` where they used to come back
`clean`. Of 12 items, 6 were clean cold — Lemonade Change, Rotate Array,
Kosaraju, Prim's, Dijkstra, Nearest Smaller to the Left — and **three of those
(Kosaraju, Dijkstra, Prim's) had needed heavy escalation on their previous
pass**. No evidence of decay attributable to the weekend batching. Do not
re-open the weekday `+1` trade on this data.

**The clean/failed split is the finding, and it is the same split the tracker
has been recording for a month, now visible in one sitting:** everything clean
was *mechanics*; everything that failed was *why it works*. Clean cold —
Lemonade's state-domination swap, Rotate Array's double-reversal, Kosaraju's
finish-order argument, Prim's cut rule + why, Dijkstra's contradiction proof
(handed over entirely last time), Nearest Smaller's code and pop rule. Failed —
Floyd-Warshall (6th attempt, not derived, handed over), Redundant Connection
(4th escalation on rank's *cost*, handed over), Bellman-Ford (both points
repeat-missed from 07-30), LC 678 (4 escalations), Kth Largest (heapify itself
turned out to be unknown, not just its complexity).

**Two items moved on the ladder**: Rotate Array took its 2nd consecutive clean
and **graduates off `[leech]`**; Task Scheduler's formula came back clean cold
for the first time in 3 attempts (1 of 2 toward graduation), though the code
shipped without the `max(formula, tasks.length)` clamp — found and fixed cold
once a counterexample was posed. **Two items tagged `[leech]`**: Bellman-Ford
(both the `V-1` justification and the negative-*cycle* point are 3rd
occurrences, both were clean on 07-26 and failing by 07-30 — 4 days) and
Redundant Connection (3rd session, 4th escalation, same single point).

**Heapify was a genuine coverage hole, not rust.** The build-heap O(n) fact was
recalled, but "I don't understand the heapify method" surfaced when asked why —
sift-down had never been built. Constructed from scratch this session
(precondition → larger-child swap → sift loop → bottom-up order → cost = height
→ the n/2·0 + n/4·1 + … sum). Filed as new material under Heaps, not as a
failed review.

**User raised the review-value question directly**: *"do we need more reviews on
these kind of problems? I already know their workings."* Correct on the
mechanics and correct about 6 of the 12. The answer given, and it should hold as
policy: a flat 69-item backlog is the wrong shape — graduate aggressively (the
2-consecutive-clean rule exists and has never fired because reviews rarely run),
keep only `[leech]` + last-session failures, and give the rest of weekend
capacity to coverage, since the plan already declares the backlog frozen. The
one counterweight stated: Bellman-Ford was clean on 07-26 and failing by 07-30,
so "I know it" and "I'll know it in a month" are different claims — the *why*
decays in days even when mechanics don't.

**Transfer success, first in the tracker.** LC 435's greedy rule is the same
earliest-end rule that broke twice on N Meetings in One Room (08-05, needed a
constructed counterexample both times). It came out cold here, in one sentence,
on an unfamiliar problem. Every prior `transfer` entry in the journal is a
transfer *gap* (DSU 08-07, fixed-window 08-11); this is the first in the other
direction.

**Second occurrence of the unprompted-proof-demand, now a trend.** Told that
`V-1` bounds a shortest path, the user refused the assertion — *"it's not
convincing"* — and then built the entire cycle-cutting argument themselves
(≥V edges ⇒ repeated node ⇒ contains a cycle ⇒ cut it for a no-worse path, or
the cycle is negative and no shortest path exists). First occurrence was
2026-08-12; the dashboard asked to watch for a second before calling it a
trend. This is it, and it is the justification weakness running in reverse.

**Process**: user set a standing instruction that every session's duration is
logged to `~/LifeOS/Work/deep_work_log.md`, prompted by asking for total study
time and finding it unanswerable — `~/InterviewPrep` has no duration field at
all (durations appear only in prose, only after 08-02) and `deep_work_log.md`
had 2 entries between 07-13 and 07-31. Recorded total on the books for the
cycle before today: ~7.2h across 36 days.

Reviews: **12 cleared** (see review_schedule.md). New problems: 1 (LC 435).

- 2026-08-18 17:34-17:43 (~10 min, user-set 10): coverage only, 1 problem —
  **Minimum Coins of 1, 2, 5 and 10 (GFG), solved independently, code cold and
  correct, O(1)/O(1) cold.** Two items. (1) **The justification ladder ran to
  form and worked in ~3 min**: first answer was mechanics-restatement, the
  numeric instantiation (both plans costed on n=39, 6 vs 7) was produced
  correctly by the user, and the general statement — dropping one 10 costs ≥2
  coins back — came cold on the next question. Same prescription the tracker has
  been recording since 08-08, now closing inside a 10-minute block. (2) **Mentor
  error, logged so it isn't repeated**: the problem statement posed with the OJ
  link was a *different* problem (full Indian denomination set, return-the-list
  variant), and the expected output stated for n=121 was wrong. User's code was
  correct and they said so ("my code is right") — the correct move would have
  been to re-read the link before pushing them to trace a phantom defect.
  **Standing fix: state the problem from the link's own text, or give the link
  and let the user read the statement — do not paraphrase from memory.**
  Note the cost: 3 of 10 minutes went to a defect that did not exist. Reviews:
  none (weekday, weekend-only policy); backlog still 60. **Missed sessions
  08-16 (Sunday) and 08-17 — the second weekend review batch never ran.**
