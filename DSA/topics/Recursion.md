---
type: topic
topic: Recursion (Step 7)
updated: 2026-08-31 (session 2)
status: in-progress — 2/25 (8%) per Codolio import, 2026-07-10 — priority gap topic. Live coverage started 2026-08-28 (bucket 2 of the post-cut queue): 11 solved (Subsets, Combination Sum, Combination Sum II, Subsets II, Rat in a Maze, Letter Combinations, Word Search, Combination Sum III, Word Break, Permutations, M-Coloring); N-Queens open (2 declines), Palindrome Partitioning off the list
---

# Recursion (Striver A2Z Step 7, pattern-wise)

## Subtopics (Striver A2Z order)

- Get a Strong Hold (5): recursive atoi, pow(x,n), count good numbers, sort/reverse a
  stack using recursion.
- Subsequences Pattern (12): generate binary strings, generate parentheses, print all
  subsequences/power set, subsequence pattern theory, count/check subsequence with sum
  K, combination sum I/II/III, subset sum I/II, letter combinations of phone number.
- Trying All Combos / Hard (8): palindrome partitioning, word search, N-Queens, rat in
  a maze, word break, M-coloring, Sudoku solver, expression add operators.

## Patterns That Show Up Here

- [[Backtracking]]

## Problems Log

Codolio import (2026-07-10) — 2 solved, consistent with individual flags:

- Generate all binary strings [Easy] — solved
- Generate Parentheses [Medium] — solved

Live (2026-08-28, bucket 2 of the post-cut coverage queue — 15 of ~23 kept):

- [x] Subsets (LC 78) [Medium] — 2026-08-28 — **independent, cold, correct first
  submit**. take/not-take with proper undo, deep copy on record. `2^n` justified
  cold ("each element has a choice"). Time needed one nudge: O(2^n) -> O(n·2^n)
  once the cost of `res.add(new ArrayList<>(list))` was priced.
- [x] Combination Sum (LC 39) [Medium] — 2026-08-28 — with-hints:2. Three
  branches where two suffice; duplicates filtered by a `HashSet` instead of
  never being generated. See [note](../notes/combination-sum.md) and
  [[Backtracking]].

- [x] Combination Sum II (LC 40) [Medium] — 2026-08-29 — with-hints:6, Accepted.
  Both defects were already written in the tracker the night before: base cases
  ordered reject-before-accept (16h after that flashcard was written), and
  `Set` on the result again. Rule learned: declining a value declines every
  copy; the skip lives in the decline branch only. See
  [note](../notes/combination-sum-ii.md) and [[Backtracking]].
- [x] Subsets II (LC 90) [Medium] — 2026-08-29 — **independent, cold, correct
  first submit**; the skip-on-decline rule transferred with no prompt 5 minutes
  after LC 40 needed six escalations for it, and `O(n·2^n)` came cold. Open:
  the *why* of sorting (mechanism not named, ended in "just tell me").
- [x] Word Break (LC 139) [Medium] — 2026-08-31 — with-hints:5, **Accepted**.
  Substituted 2026-08-30 for LC 131 to test the variable-length-piece move; it
  did bite, but as **greedy-first-match**, not as string-index confusion. See
  the 2026-08-31 block below.
- [ ] ~~Palindrome Partitioning (LC 131)~~ — **OFF THE COVERAGE LIST 2026-08-30**
  after a 3rd decline; not counted against the 94. Revisit after LC 139. Blocker
  identified: variable-length piece choice (`j` over `i..n-1`), not string-index
  state — LC 17 was clean the same session. Prior detail below.
- [ ] Palindrome Partitioning (LC 131) [Medium] — **OPEN 2026-08-29**, approach
  only, no code. Corrected: only the left piece must be a palindrome. **Abandoned
  a 2nd time 2026-08-29 16:05** — child set derived concretely on `"aab"`
  (`a`/`aa`/`aab`, `j=0,1,2`), then the generalization to `j` in `i..n-1` stalled.
- [x] Rat in a Maze (GFG) [Medium] — 2026-08-29 — with-hints:4. Grid backtracking,
  4 directions in lexicographic order `D,L,R,U`, visited-by-mutation with restore.
  Accept-before-reject base case, 3rd encounter; see [note](../notes/rat-in-a-maze.md).
- [ ] N-Queens (LC 51) [Hard] — **OPEN, 2 declines (2026-08-29 approach-only,
  2026-08-31 WA-then-abandoned)**. Approach (row-per-level, `colSet` + `r+c` +
  `r-c`) has now been restated cold twice. The 08-31 attempt was iterative and
  greedy — no recursion, no undo. **LC 131 came off the list at 3 declines; this
  is at 2.** See [note](../notes/n-queens.md).

Live (2026-08-30) — all three judge-confirmed in session:

- [x] Letter Combinations of a Phone Number (LC 17) [Medium] — 2026-08-30 —
  with-hints:3, **Accepted**. Approach complete before code. `parseInt(char)`
  non-compile; `digits=""` returned `[""]` (asked 4x before it was traced).
  **Space derived to `O(n²)`** — `res+c` allocates per frame, one path holds
  `0+1+…+n` chars; `StringBuilder` + undo restores `O(n)`. See
  [note](../notes/letter-combinations.md).
- [x] Word Search (LC 79) [Medium] — 2026-08-30 — with-hints:4, **Accepted**.
  Code before approach. Single start cell `(0,0)`; `|` vs `||` fixed at the
  return while the calls stayed eagerly assigned (**hint-shape matching, 2nd
  occurrence**); restore commented out then silently restored. Base-case
  ordering stated **cold by precondition** — 4th encounter, first clean. See
  [note](../notes/word-search.md).
- [x] Combination Sum III (LC 216) [Medium] — 2026-08-30 — with-hints:2,
  **Accepted**. Start-index dedup transferred **cold** from LC 39/40. Guard hole
  `cnt==k && sum>n` found on trace, tightened to `cnt==k||sum>=n` cold; the
  `>=` monotonicity reason was handed over. See
  [note](../notes/combination-sum-iii.md).

Live (2026-08-31) — 2 judge-confirmed, 1 abandoned:

- [x] Word Break (LC 139) [Medium] — 2026-08-31 — with-hints:5, **Accepted**.
  Opened greedy-first-match (trie + advance on first hit); closed by the
  constructed counterexample `"catsdog"` / `["cat","cats","dog"]` — note
  `"catsandog"` gives the *right* answer greedily, so it proves nothing.
  **Memo written unprompted.** Two traced defects: the `index` param is always
  equal to `start`, and the success path stored `true` under `start+"-"+i`
  while every lookup asks `"k-k"` — so only `false` was ever cached. Cost bug,
  named as such. `Boolean[n]` rewrite; `O(n³)` / `O(n)` + dict, both derived.
  See [note](../notes/word-break.md) and [[Backtracking]].
- [x] Permutations (LC 46) [Medium] — 2026-08-31 — with-hints:3, **Accepted**.
  **Bitmask + place/recurse/undo, structure cold** — both undos present, 20 min
  after declining that mechanism on N-Queens. Both bugs were operator
  precedence: `mask&(1<<i)==0` (compile error) and `1<<(n+1)-1` = `1<<n`, so
  `goalMask` was 8 not 7. `O(n!·n)` after `2^n` was offered first.
- [ ] N-Queens (LC 51) [Hard] — **2nd decline**, see the entry above.

Live (2026-08-31, session 2 — 30 min, 1 problem):

- [x] M-Coloring Problem (GFG) [Medium] — 2026-08-31 — with-hints:6, **Accepted
  1114/1114** on the 3rd submission. **Greedy-first-match, 3rd occurrence, and
  the first one closed cold in a single question** — the return path was then
  named unprompted. Legality-as-"differs from the previous node" closed on one
  traced instance. Then the code reverted to the discarded rule
  (`i != prvNodeColor`): **derivation-to-code regression**. Judge found the rest
  — a `continue` aimed at the inner loop (dead scan), a vestigial early-return
  that fired on a self-edge, and `dfs(0)` only, so disconnected components went
  uncoloured. Complexity not reached. See [note](../notes/m-coloring.md) and
  [[Backtracking]].

Remaining 18 are gaps — this is the backtracking-heavy topic and a real priority for
Week 1/2 given only 8% coverage; it directly feeds into Trees/Graphs/DP interview
questions later.

## Common Mistakes Seen in This Topic

- 2026-08-28: Combination Sum — over-generating search masked by a `HashSet`;
  redundant "take and move on" branch. Standing rule now in [[Backtracking]]:
  a `Set` on a backtracking result is a branching bug until proven otherwise.
- 2026-08-28: copy cost into the result list omitted from the complexity twice
  in one session (Subsets, then Combination Sum 12 min later) — transfer gap,
  see [[mistake_journal]].
- 2026-08-30: Word Search — `|` vs `||` explained correctly, then the fix changed
  the operator on the `return` line while the four calls stayed eagerly assigned
  above it. Nothing short-circuited. **Hint-shape matching, 2nd occurrence** —
  re-run the counterexample before declaring a fix.
- 2026-08-30: Word Search — the path mark deleted, then silently restored without
  the symptom being stated. Rule now in [[Backtracking]]: the mark means "on the
  current path", not "visited ever", so it is undone on the way out.
- 2026-08-30: Combination Sum III — reject guard left a hole (`cnt==k && sum>n`)
  that recursed past `k` doing nothing. Prune conditions need a trace, not a
  read-through.
- 2026-08-31: M-Coloring — legality scanned every neighbour but the `continue`
  targeted the inner loop, so the scan's result never reached the colour loop.
  A validity check that writes to nothing is dead code the compiler won't flag.
- 2026-08-31: M-Coloring — a parameter (`prvNodeColor`) left in place after the
  logic it served was replaced. It became an unconditional `return false` on a
  self-edge. **Rule: when a check is superseded, delete it in the same edit.**
- 2026-08-31: M-Coloring — recursion entered at vertex 0 only. On a graph, the
  driver loops over all vertices; edge-walking alone never reaches a
  disconnected component. Standing test case: `V=3, edge 1-2, m=1` -> false.

Live (2026-09-01 — 92 min, 3 problems across two topics):

- [x] Sudoku Solver (LC 37) [Hard] — 2026-09-01 — with-hints:7, **Accepted
  10/10, 125 ms**. Bucket 2 -> **12/15**. Constraint-set ladder held: the
  adjacency-scan legality of M-Coloring transferred to row/col/box trackers,
  and the approach was cold — trackers, try digits, undo on dead end, with
  **no greedy-first-match** and the base-case invariant stated cold. The block
  was arithmetic, not backtracking: `box = (r/3)*3 + c/3` needed full
  escalation and was handed over, and the same gap wrote `i*3+j` as the cell
  stride on a 9-wide grid. Six defects, all mechanical. `O(9^k)` / `O(1)` cold.
  See [note](../notes/sudoku-solver.md) and [[Backtracking]].
- [ ] Permutations II (LC 47) [Medium] — **declined at approach 2026-09-01**;
  the per-call dedup set was named in the mentor's question, not derived.
  Re-pose cold.
