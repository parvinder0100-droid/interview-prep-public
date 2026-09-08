---
type: note
problem: Combination Sum III (LC 216)
date: 2026-08-30
---

# LC 216 — Combination Sum III

Accepted 2026-08-30, with-hints:2.

## Transfer that worked

First approach looped `1..9` at every level, which generates each combination in
every order. Asked for a second pick-sequence reaching `[1,2,4]`, the user
skipped the counterexample and went straight to the fix: **start index, next
level begins at `i+1`.** Cold, from LC 39/40 two days earlier. That one move
kills reuse and reordering together.

## The guard hole

Written guard, after the accept check:

    if (cnt==k && sum<n || cnt<k && sum>=n) return;

Java precedence groups it correctly, and it is not *wrong* — but trace
`k=2, n=3` picking `1` then `9`: `cnt==2, sum=10`. Accept fails (`sum!=n`),
first clause fails (`10 < 3` is false), second fails (`cnt<k` is false). It
falls through to the loop and keeps recursing with `cnt` **past** `k`, adding
nothing, until `i` runs out at 9. Wasted search, not a wrong answer — nothing
can be recorded once `cnt > k`.

Tightened, cold:

    if (cnt==k || sum>=n) return;

Correct only because the accept check runs directly above it and has already
taken the `cnt==k && sum==n` case.

## Why `>=` and not `>` (needed the ladder, handed over)

All candidates are positive, so `sum` is **monotonically increasing** down a
path. A prefix that has already reached `n` with picks still owed can never come
back to `n` — the next pick is at least 1. That same monotonicity is what makes
`sum > n` prunable at all. **It fails the moment a problem allows 0 or negative
values** — that is the condition to check before reusing this prune.

Asked for the rule, the condition was restated instead. Logged as prompted, not
cold.
