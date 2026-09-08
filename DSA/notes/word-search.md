---
type: note
problem: Word Search (LC 79)
date: 2026-08-30
---

# LC 79 — Word Search

Accepted 2026-08-30, with-hints:4. Code arrived before the approach, ~2 min
after the approach questions were asked.

## Defects

1. **Only one start cell.** `exist` called `dfs(...,0,0,0)` once. Any word not
   beginning at `(0,0)` returns false — found by tracing `"SEE"`. Fix: nested
   loop over every `(i,j)` as a start, early-return on the first `true`.
2. **`|` instead of `||`, then the fix missed.** The difference was stated
   correctly ("`|` evaluates all four", "the other three subtrees still run, at
   every level"), but the edit changed the operator on the `return` line while
   the four calls stayed as eager assignments above it. Assignment forces
   evaluation — `||` on already-computed booleans short-circuits nothing. The
   short-circuit has to live in the call chain:

       boolean found = dfs(i+1,j,index+1)
                    || dfs(i-1,j,index+1)
                    || dfs(i,j+1,index+1)
                    || dfs(i,j-1,index+1);
       board[i][j] = cur;
       return found;

   **2nd occurrence of hint-shape matching** — the 08-29 prediction ("the edit
   that follows matches the hint's shape rather than the defect") firing exactly
   as written.
3. **Restore commented out.** `board[i][j]=cur` was deleted, then silently put
   back in the next paste without the symptom ever being stated.

## The restore question (open since Rat in a Maze 08-29, now closed)

Counterexample that separates it:

    board = [["A","B"],        word = "AAB"      answer: true
             ["A","D"]]                          path: (1,0) -> (0,0) -> (0,1)

The outer loop tries `(0,0)` first, marks it `'-'`, fails, and without the
restore leaves it `'-'` forever. The true path starts at `(1,0)` — untouched —
but its **second step** needs `(0,0)`, which is now poisoned. Answer flips to
false.

Rule: the mark means **"on the current path"**, not "visited ever". It is part
of the path's state, so it is undone on the way out — same object as the
`list.remove(list.size()-1)` in subset backtracking.

## Positive

Base-case ordering stated **cold, by precondition**: `index >= word.length()`
may run with `(i,j)` off the board and is still correct, because "all chars
matched" does not depend on `(i,j)`. 4th encounter of the rule, first clean one,
and phrased as a precondition rather than a memorized order.

## Complexity (declined, handed over)

`O(m·n·4^L)` time — every cell as a start, ≤4 branches per step (really 3 after
the first, the marked cell blocks the step back). `O(L)` stack. Board mutated in
place; the `'-'` sentinel is safe only because the constraints say letters only.
