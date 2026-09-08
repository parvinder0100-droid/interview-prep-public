---
type: note
problem: N-Queens (LC 51)
topic: Recursion / Backtracking
date: 2026-08-29 (updated 2026-08-31)
status: OPEN — 2 declines; 2026-08-31 attempt was WA (greedy, no recursion)
---

# N-Queens — open at the diagonal index shift

## What landed cold

Approach was volunteered **before** any code, the first time in three sessions.
Then four correct derivations in a row, each on the first ask:

- a row holds at most one queen, so the choice at each recursion level is
  *which column*, and the recursion runs one row per level
- at row `r` the row check is free by construction; column and both diagonals
  are not
- `r+c` is constant along a `/` diagonal
- `r-c` is constant along a `\` diagonal

One miss: asked which columns in row 1 are legal after a queen at `(0,0)` on
`n=4`, the answer was "2" — column 3 was dropped. Corrected in one question by
walking the three attack lines through `(1,3)`.

## The user's own question, and how it closed

> "why do we have to r-c and r+c, why not just one oprn?"

Closed by the user computing `r+c` down the `\` diagonal `(0,0),(1,1),(2,2),(3,3)`
-> `0, 2, 4, 6`, not constant. So `r+c` cannot name that diagonal, and the two
directions need two different keys.

Worth noting what worked here: the two grids of `r+c` and `r-c` values written
out in full did **not** land; computing one line of four numbers did. Same
prescription as 08-26 and 08-18 — instantiate, don't illustrate.

## Where it stopped

`r-c` spans `-(n-1)` to `n-1`, so it is not directly usable as an array index
(`-3` throws `ArrayIndexOutOfBoundsException`, which the user identified). The
shift and the resulting array size were the open question when the session
ended.

Resume there, cold, then code.

## 2026-08-31 — 2nd attempt, WA, abandoned

Approach restated **cold and correct** for the second time: one queen per row so
recursion runs row-by-row, three sets — `colSet`, `r+c`, `r-c` — added on place
and checked before placing. No hint needed for any of it.

The code did not implement it. It was two nested loops:

    for i in rows:
        found = false
        for j in cols:
            if !found && no conflict:  place, mark sets, found = true

An outer `for` cannot go back to an earlier row, so there is no undo and no
search — the same greedy shape as the LC 139 opening 40 minutes earlier.

Judge, n=4:

    output   [["Q..."], ["..Q."], ["...."], [".Q.."]]
    expected [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]

Two separate defects visible in that one line, and the user read both off it
when asked:

1. **3 queens, one empty row.** Row 2 had no legal column, the loop just fell
   through. The wrong choice was row 0 taking column 0 — which is exactly what
   backtracking exists to revisit. Fix named correctly: "backtrack and try
   column 1 in row 0."
2. **Shape.** `res.add(list)` runs once per row with `list` holding one string,
   so each element of `res` is a *row*, not a *board*. `List<String> list`
   needs to live inside the recursion and accumulate all `n` rows before a
   single `res.add`.

A separate 5-character-row bug (`s += "Q"` then falling through to `s += "."`)
was fixed with an `else` — but that was the only thing fixed, while the `res`
shape question that had actually been asked went untouched. Logged as
hint-shape matching.

Stopped here: "we will come to this problem some other time." Second decline.

**Resume point**: write `solve(row)` only — base case `row == n` records the
board, loop over columns, place / recurse / remove from all three sets. The
approach does not need re-deriving; it has been correct twice.

