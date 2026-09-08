---
type: note
problem: Sudoku Solver (LC 37)
topic: Recursion/Backtracking
created: 2026-09-01
---

# Sudoku Solver (LC 37)

**Accepted 10/10, 125 ms, 2026-09-01. with-hints:7.**

## What was cold

- Constraint tracking + try digits + undo on dead end, stated as the approach
  with **no greedy-first-match** — "backtrack" was volunteered. Third problem in
  a row where that family did not appear.
- The base case, justified by the invariant rather than by a check: a full board
  is necessarily valid, because an illegal digit is never left on it. Asked why
  the 81 digits can be trusted, the answer was "if at any point they conflict,
  we will backtrack". That is the argument.
- `boolean[9][9]` for rows and cols, indexed `[r][d-'1']`, reached after one
  question about what `rows[0]` holds.
- `O(9^k)` for `k` empty cells, and `O(1)` space with recursion depth <= 81.

## Where the 12 minutes went — and it was not backtracking

`box = (r/3)*3 + c/3`. Escalated the full ladder: the four sample cells, the
`boxRow`/`boxCol` table, the 9x9 picture with box numbers, the 9x9 picture with
`(r,c)` pairs, a cinema-seat analog (3 seats per row, tickets numbered 0..8) —
which produced `row*3 + seat` correctly — and then the substitution back into
`(r/3)*3 + c/3` still had to be handed over.

The blocking idea: **`(r/3)*3` is not `r`.** Integer division truncates first,
so it snaps `r` down to the start of its band (7 -> 2 -> 6). The `/3` and `*3`
do not cancel.

The same gap wrote `getNextValidCell` as `i*3 + j` on a **9-wide** grid, so
`(0,4)` advanced to `(1,2)`. One arithmetic idea, two wrong places, same session.

## The six defects, all mechanical

1. `i*3+j` / `next/3` / `next%3` — wrong width, should be 9.
2. Base case `... || board[i][j]!='.'` returned true at any prefilled cell, so
   `solveSudoku` returned with the board untouched. Fix: recurse to the next
   cell instead.
3. `i>=m && j>=n` never fires — after `(8,8)` the next cell is `(9,0)`, so
   `j>=n` is false and `board[9][0]` throws. Fixed as `i*9+j >= 81`.
4. `cols[i][val]` where `cols[j][val]` was meant, in `isValid`.
5. Same bug again in the undo block.
6. `board[i][j]=(char)val` writes a control character; needs `(char)('0'+val)`,
   and `'0'+val` alone is a compile error (int -> char).

Every one was found by tracing, once pointed at the line. None was conceptual.

## Design point raised at the end

`isValid` both answered a question and wrote the digit + three tracker flags,
while the undo lived in `dfs`. A query that mutates, with its inverse in another
function. Any later call site that only wants to check corrupts state silently.
`dfs` should do place -> recurse -> undo on three adjacent lines.

## Java note that cost a submission

Arithmetic on `char` promotes to `int`; assigning back needs an explicit cast.
Cleanest avoidance: loop over `char d='1'; d<='9'; d++` and use `d-'1'` only
where an index is required — the digit never leaves `char`.
