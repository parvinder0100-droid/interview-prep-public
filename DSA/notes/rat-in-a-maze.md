---
type: note
problem: Rat in a Maze (GFG)
topic: Recursion / Backtracking / Grid
date: 2026-08-29
---

# Rat in a Maze

## What happened

Code was written immediately, with no approach stated, roughly 13 minutes after
the approach-first rule had been set for the session. The skeleton was right on
the first try — 4-direction recursion, mark-visited by mutating the cell to `0`,
restore to `1` on the way out, string built by concatenation.

Two defects, one of them the interesting one.

## Defect 1 — the accept branch ran before its own preconditions

Original order:

    if (curx==m-1 && cury==n-1) { list.add(s); return; }   // accept
    if (out of bounds || maze[curx][cury]==0) return;      // reject

On this maze the code reports a path where none exists:

    1 1
    1 0

The rat steps onto `(1,1)`, the accept branch fires, and a path onto a **blocked**
cell is recorded.

**The fix sequence is the thing worth remembering**, not the fix:

1. patched with `&& maze[m-1][n-1]==1` — works, but the rule stayed unnamed
   (3rd silent fix logged, after 08-25 and 08-29 morning)
2. the patch was then **removed without swapping the blocks**, which put the
   original bug straight back
3. blocks finally swapped, which needs no extra condition at all

The rule was only spoken after being asked what the accept branch *assumes*
about the cell it is standing on — answer: that the cell is open and in bounds.

## The rule, stated correctly

**Every precondition the accept branch relies on must already be established
when it runs.**

Do not memorise this as "reject before accept" — that ordering is right here and
**wrong** on Combination Sum II, where `sum == target` must be tested *before*
the index bound. The difference:

- Rat in a Maze: "this cell is open and on the board" **is** a precondition of
  the destination being a real path end -> validity check first.
- Combination Sum II: `index >= nums.length` is only "ran out of items", not a
  precondition of the sum being correct -> accept first, or an exact hit landing
  on the last element is dropped.

Same underlying rule, opposite orderings. The ordering is a consequence; the
precondition question is the thing to ask.

## Defect 2 — lexicographic output

GFG wants the paths sorted. The recursion order *is* the output order, so the
calls must go `D, L, R, U`. Original was `D, R, L, U`.

## Left unstated (declined, "lets move")

- time / space complexity, including the cost of building `s` by concatenation
- what concretely breaks if the trailing `maze[curx][cury]=1` restore is deleted
- an unused `StringBuilder sb` declared in the wrapper
