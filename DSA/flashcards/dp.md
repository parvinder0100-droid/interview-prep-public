---
type: flashcards
topic: dp
updated: 2026-08-28
---

# DP Flashcards

Format: Q on one line, A (intuition/complexity only, never full code) below it.

Q: Rolling two variables to make a 1D DP O(1) space — what must each hold at the top of iteration `i`, and what is the only legal roll?
A: `backbyone = dp[i-1]`, `backbytwo = dp[i-2]`. Roll is `backbytwo = backbyone` **then** `backbyone = cur`. Assigning any computed candidate (e.g. `dp[i-1] + cost`) into the `dp[i-2]` slot inflates every later comparison.

Q: Why does a rolled-variable DP bug often pass small tests?
A: With a 2-back window, n<=3 never reads the `dp[i-2]` slot after it is first corrupted. Test n>=4 — Frog Jump on `[0,10,100,10]` returns 100 instead of 10.

Q: A recurrence reads `dp[i-2]`. Where does the loop start?
A: `i=2`, with `dp[1]` set explicitly. Evaluate the body at `i=k-1` before choosing the bound — `dp[-1]` throws ArrayIndexOutOfBoundsException on every `n>=2` input.
