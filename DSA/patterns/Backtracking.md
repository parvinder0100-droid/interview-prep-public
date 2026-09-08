---
type: pattern
pattern: Backtracking
updated: 2026-08-30
status: in-use
---

# Backtracking

## When This Pattern Applies

Enumerate every member of an exponential space (all subsets, all combinations,
all permutations, all placements) where each element carries a small set of
choices and partial states can be extended or abandoned.

## Core Idea

One decision per level, undo it on the way out:

    choose -> recurse -> un-choose

Two shapes seen so far:

    take / not-take        each element used at most once   (Subsets)
    take-stay / skip       each element reusable            (Combination Sum)

`take-stay` means recursing with the **same** index, which is what permits
unlimited reuse. Adding a third "take and move on" branch on top of these two is
**redundant** — it equals take-stay followed by skip.

## Problems Using This Pattern

- Subsets (LC 78) — 2026-08-28 — take/not-take, independent cold solve
- Combination Sum (LC 39) — 2026-08-28 — take-stay/skip, redundant 3rd branch
- Combination Sum II (LC 40) — 2026-08-29 — take/skip-all-copies, with-hints:6
- Subsets II (LC 90) — 2026-08-29 — same skip, transferred cold in 5 min
- Rat in a Maze (GFG) — 2026-08-29 — grid variant, with-hints:4
- N-Queens (LC 51) — 2026-08-29 — OPEN, approach only
- Letter Combinations (LC 17) — 2026-08-30 — index-over-string, Accepted, with-hints:3
- Word Search (LC 79) — 2026-08-30 — grid variant + string index, Accepted, with-hints:4
- Combination Sum III (LC 216) — 2026-08-30 — start-index dedup + pruning, Accepted, with-hints:2
- Word Break (LC 139) — 2026-08-31 — variable-length piece + memo, Accepted, with-hints:5
- Permutations (LC 46) — 2026-08-31 — bitmask used-set, Accepted, with-hints:3
- N-Queens (LC 51) — 2026-08-31 — WA, written greedy-iterative, abandoned (2nd decline)
- M-Coloring (GFG) — 2026-08-31 — graph variant, Accepted 1114/1114, with-hints:6

## Pruning (added 2026-08-30)

- **Write the reject guard as the complement of the accept check above it**, not
  as a list of failure cases that come to mind. LC 216: accept is
  `cnt==k && sum==n`, so reject is `cnt==k || sum>=n`. The hand-enumerated
  version `(cnt==k && sum<n) || (cnt<k && sum>=n)` silently misses
  `cnt==k && sum>n` and recurses past `k` recording nothing.
- **Name the property that licenses the prune.** `sum >= target` (not just `>`)
  is prunable only because all candidates are **positive**, making `sum` monotone
  down a path — a prefix already at `target` with picks owed can never return to
  it. Introduce a 0 or a negative value and the prune becomes a wrong answer.

## Cost of the partial state (added 2026-08-30)

What each **frame** holds is part of the space bound, not just how many frames
there are.

    carry `res + c` (String)      new allocation per frame   O(n²) on one path
    carry a StringBuilder         one buffer, append/undo    O(n)
    carry a List + copy at leaf   one list, copy is the leaf cost

The copy at the leaf is unavoidable in all three — it is the `· n` in
`O(branching^n · n)`. What is avoidable is copying on the way *down*.

## Duplicate Inputs — the third shape

    take / skip-every-copy     each element used once, input has duplicates

Sort first, then: taking is `index+1` as usual; **declining `nums[index]` must
also decline every copy of it**, because taking a later equal value rebuilds the
identical list. The skip lives only in the decline branch, so a value may still
appear twice in one answer (`[1,1,6]`).

    int j = index; while (j < n && nums[j] == nums[index]) j++;   // decline branch only

Sorting buys two separate things: duplicates become adjacent so an
adjacent-only comparison can see them, and each answer gets one canonical
spelling (`[1,2]`, never also `[2,1]`).

Used by: Combination Sum II (LC 40), Subsets II (LC 90).

## Common Pitfalls

- **The legality predicate must not also place.** (LC 37, 2026-09-01) An
  `isValid` that returns a boolean *and* writes the digit *and* sets the
  trackers, with the undo living in the caller's else-branch, hides the
  place/undo pairing from both sites. Keep the predicate read-only; place,
  recurse, undo go on three adjacent lines.

- **A superseded check must be deleted, not left (added 2026-08-31,
  M-Coloring).** The neighbour scan replaced `prvNodeColor`, but the old guard
  `if(color[curNode]==prvNodeColor) return false` stayed behind. It then fired
  on a self-edge — the recursion re-enters a vertex holding its own colour —
  and returned false for a colourable graph. **When a mechanism is replaced,
  its parameter and its guard go in the same edit; grep the function for the
  old variable before submitting.**
- **The driver loops all vertices; the recursion walks edges (added
  2026-08-31, M-Coloring).** Entering at vertex 0 and recursing into
  neighbours only ever reaches vertex 0's component. On a graph problem the
  decision sequence is per *vertex*, so the entry point is
  `for v in 0..V-1: res &= dfs(v)`. Standing test case: `V=3`, single edge
  `1-2`, `m=1` — an edge walk returns true, the answer is false.
- **A nested validity scan has to publish its result (added 2026-08-31,
  M-Coloring).** `for(nb) if(color[nb]==i) continue;` advances the *neighbour*
  loop, so the scan runs and its verdict is discarded — dead code the compiler
  will not flag. Use a flag plus `break`, or a helper returning boolean. Rule:
  if a loop body writes to nothing outside itself, it does nothing.
- **Greed wearing backtracking's clothes (added 2026-08-31, 2 occurrences in
  one session; 3rd occurrence M-Coloring 2026-08-31, closed cold in one
  question — first time this was self-corrected without escalation).** The loop finds the first legal option, commits, and moves on;
  there is no return path and no undo. It reads like a search because the
  legality test is there, but the legality test is not the search.

      LC 139   took the first dictionary word matching at `i`.
               `"catsdog"` / `["cat","cats","dog"]` -> false, answer is true.
      LC 51    took the first non-attacked column per row, in two nested loops.
               n=4 -> 3 queens and one empty row; an outer `for` cannot return
               to an earlier iteration, so a dead end has nowhere to go.

  Test before writing the loop: *if this choice dead-ends three levels down,
  which line brings control back here?* No such line means no backtracking.

- **The memo key must be exactly the state (added 2026-08-31).** `dfs(s,start,
  index)` on LC 139 always had `index==start` — every call site passed
  `(i+1,i+1)` — so a two-part string key was one integer in disguise, and a
  `Boolean[n]` replaced both the `HashMap` and the per-call concatenation.
  Worse, the write key was reassigned before `put`, so `true` was stored where
  nothing ever looked: only failures were cached. Right answer, dead cache —
  a cost bug. Build the key once at the top and never reassign it.

- **Parenthesize bitwise sub-expressions (added 2026-08-31, LC 46).** In Java
  `&`/`|`/`^`/`<<` all bind *looser* than `==` and `-`. `mask&(1<<i)==0` is
  `mask & ((1<<i)==0)` (compile error) and `1<<(n+1)-1` is `1<<n`, not
  `(1<<n)-1` — the latter is silent: `goalMask` is 8 instead of 7, the accept
  branch never fires, and the result is empty rather than wrong.


- **Terminal-check ordering is decided by preconditions, not by a fixed rule.**
  Ask what the accept branch *assumes is already true*, and put those checks
  above it. This produces **opposite** orderings on two problems already solved:

      Combination Sum II   accept first   `index >= n` is not a precondition of
                                          the sum; testing it first drops an
                                          exact hit on the last element
                                          (`[1,2,2,2,5]`, target 5, loses `[5]`)
      Rat in a Maze        reject first   "cell is open and on the board" IS a
                                          precondition of the goal being a real
                                          path end; testing it second reports a
                                          path onto a blocked destination
                                          (`[[1,1],[1,0]]`)

  Recorded 2026-08-29 after "reject before accept — same as LC 40" was stated
  and wrongly affirmed; the label is inverted with respect to LC 40. Third
  encounter with this family in two days.

- **A `Set` on the result is a branching bug until proven otherwise.** If
  duplicates have to be filtered out of the output, the search is reaching the
  same state by more than one path and paying exponentially for it. Delete the
  `Set`, find the redundant branch.
- **Copy cost is part of the complexity.** `res.add(new ArrayList<>(list))` is
  O(list length), so total time is (number of results) x (result length) — not
  the node count alone. Subsets is O(n·2^n), not O(2^n).
- Record the answer (`sum == target`) **before** testing the index bound, or an
  exact hit that lands at the end of the array is silently dropped.
- Depth on target-driven searches is `target / min(element)`, not `target`.
- Deep-copy on record (`new ArrayList<>(list)`), never the live list.

## Grid Variant (added 2026-08-29)

State is a cell, not an index. Same `choose -> recurse -> un-choose`, with three
differences:

- **visited** is the grid itself: set `maze[r][c]=0` before recursing, restore to
  `1` after. No separate visited array needed when the blocked marker is reusable.
- **output order is call order.** If the answer must be lexicographic, order the
  recursive calls that way (`D, L, R, U`) — there is nothing else to sort by.
- **the goal cell still has to be legal.** See the precondition pitfall above.
- **the mark means "on the current path", not "visited ever"** (added 2026-08-30).
  That is the whole reason it is restored on the way out. Delete the restore and a
  failed attempt poisons the grid for every later start:

      board = [["A","B"],   word = "AAB"   true via (1,0)->(0,0)->(0,1)
               ["A","D"]]

  The outer loop tries `(0,0)` first, marks it, fails, leaves it marked — the true
  path's **second step** is now blocked and the answer flips to false. This differs
  from a graph `visited` set, where "seen once" is exactly what you want.
- **every cell is a candidate start** unless the problem names an origin. Rat in a
  Maze starts at `(0,0)`; Word Search does not, so the driver loops over all `m·n`
  cells. The entry point is a separate design decision from the recursion.
- **`|` vs `||` matters here, and the fix is not on the `return` line.** Assigning
  each branch to a local forces all of them to run; short-circuiting requires the
  calls to be chained with `||` directly. Costs a full search after the answer is
  already found, at every level of the stack.

Used by: Rat in a Maze, Word Search.

## Board Variant — constraint keys (added 2026-08-29)

When placements conflict along lines rather than by value, give each line an
integer key and keep one boolean array per line family:

    column      c                 size n
    `/` diag    r+c               size 2n-1
    `\` diag    r-c + (n-1)       size 2n-1   (shift: r-c spans -(n-1)..n-1)

One queen per row is enforced by the recursion shape (one row per level), so the
row never needs checking. `r+c` alone cannot cover both diagonals — it is not
constant down a `\` diagonal.

Used by: N-Queens (open), Sudoku Solver (LC 37, Accepted 2026-09-01).

**Sudoku Solver (LC 37), 2026-09-01** — the constraint-key idea moved cleanly
from M-Coloring's adjacency scan to three key families: `rows[r]`, `cols[c]`,
and `boxes[(r/3)*3 + c/3]`, each a `boolean[9]` over digits. The ladder
N-Queens -> M-Coloring -> Sudoku held; the approach was cold.

The cost was **not** the constraint idea, it was indexing. Two failures from one
misunderstanding:

- `box = (r/3)*3 + c/3` could not be derived. `(r/3)*3` is not `r` — integer
  division truncates to the band index, the `*3` re-expands to that band's start.
- The cell walk was written `i*3 + j` on a 9-wide grid, so `(0,4)` advanced to
  `(1,2)`.

Standing rule for grid backtracking: write the width down first, derive
`flat = r*width + c` and its inverse `(flat/width, flat%width)`, and verify on
two cells before writing the loop. Terminate on `flat >= width*height` — a
`r>=h && c>=w` test never fires, since the overflow cell is `(h, 0)`.

Also from LC 37: a prefilled/fixed cell must **recurse onward**, not return
true. Returning true at the first fixed cell ends the whole search with the
board untouched.
