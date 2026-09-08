---
type: note
problem: Letter Combinations of a Phone Number (LC 17)
date: 2026-08-30
---

# LC 17 — Letter Combinations of a Phone Number

Accepted 2026-08-30, with-hints:3. Approach was complete and correct **before**
code, unprompted-in-structure: one level picks a letter for the current digit,
the loop at that level runs over that digit's letters, `index` carried down,
base case `index == digits.length()`.

## The two defects

- `Integer.parseInt(digits.charAt(index))` does not compile — no `parseInt(char)`
  overload. `Character.getNumericValue(c)` works; `c - '0'` is the idiom.
- **`digits = ""` returns `[""]`, not `[]`.** The base case fires immediately at
  `0 >= 0` and records the empty string. Guard in `letterCombinations` before the
  call, not inside the base case — it is a precondition on the input, checked
  once, not a per-leaf test.

## The real content: space is O(n²), not O(n)

`res + c` allocates a **new** immutable String each frame. On one live root-to-leaf
path the frames hold strings of length `0, 1, 2, …, n` simultaneously:

    0 + 1 + 2 + … + n = n(n+1)/2 = O(n²)

Carry a `StringBuilder`, `append` before the call and delete the last char after,
and it drops to **O(n)** — one buffer mutated instead of `n` copies. The copy then
happens once per leaf, at `list.add(sb.toString())` — that is exactly the `· n` in
the `O(4^n · n)` time bound.

Time `O(4^n · n)`: 4 is the **max branching factor** (digits 7 and 9), not the
alphabet size.

## Status

3rd encounter of the copy-cost family (Subsets 08-28, Combination Sum 08-28) and
the **first derived rather than nudged out** — one concrete 4-frame trace was
enough, no ladder.
