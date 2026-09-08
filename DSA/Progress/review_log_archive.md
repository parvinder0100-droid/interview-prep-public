---
type: review_log_archive
updated: 2026-09-04
---

# Review Log Archive

Append-only log of completed reviews, moved out of `review_schedule.md` so
that file stays scannable as volume grows (that file holds only what's still
due/upcoming). Grouped by month. Never delete entries — this is historical
record, same as the mistake journal.

## 2026-09

- Course Schedule (LC 207) `[derive]` — review #1 — completed: 2026-09-04 15:42 — outcome:
  clean — Kahn's BFS indegree direction (v -> u => indegree[u]++) and queue.size()
  level snapshot redundancy answered cold and clean.
- Power of Two (LC 231) — review #1 — completed: 2026-09-04 15:42 — outcome:
  hint — Integer.MIN_VALUE (-2^31) sign-bit underflow on n-1 and false-positive
  (n & (n-1)) == 0 trap closed via ELI5 odometer analog; loop closed with user
  justifying n > 0 guard because powers of two cannot be negative.
- Single Number III (LC 260) `[derive]` — review #1 — completed: 2026-09-03 17:34 — outcome:
  hint — split-rule precision and any-bit difference rationale.

## 2026-08

- Rotate Array `[leech]` — review #4 — completed: 2026-08-01 18:10 — outcome:
  clean — full "why" derivation landed via concrete trace ([1,2,3,4,5],k=2)
  plus fragmented-but-causally-complete reasoning ("it negates the earlier
  reverse" + correct final-order readback). Mentor initially over-flagged
  this as "not clean" for lacking one synthesized paragraph, retracted after
  user pushback — see [[feedback_socratic_teaching]] pace-cap correction.
  1 of 2 consecutive clean needed to graduate off `[leech]` status.

## 2026-07

- Print Subarray with Maximum Sum `[derive]` — review #2 — completed:
  2026-07-27 19:00 — clean, start=tempStart derivation held on own, no
  mechanism hint given (only a concrete-numbers instantiation) — see
  mistake_journal grading correction.
- Rotate Matrix (90°) `[derive]` — review #1 — completed: 2026-07-13 —
  repeated rust, forgot full-row-reverse again — see mistake_journal.
- Frog Jump (DP-3) — review #1 — completed: 2026-07-11 — due was 2026-07-11 —
  surfaced a second rust bug (missing dp[2] base case), fixed — see mistake_journal.
- Find the Largest Element in an Array — review #1 — completed: 2026-07-12 — clean.
- Second Largest Element in an Array — review #1 — completed: 2026-07-12 — clean,
  duplicate-of-max edge case correctly handled this time.
- Check if Array is Sorted — review #1 — completed: 2026-07-12 — clean.
- Remove Duplicates from Sorted Array — review #1 — completed: 2026-07-12 — clean,
  two-pointer mechanics correct on re-derivation.
- Move Zeroes to End — review #1 — completed: 2026-07-12 — clean, two-pass with
  explicit tail zero-fill correctly reproduced.
- Rotate Array — review #1 — completed: 2026-07-13 — clean.
- Union of Two Sorted Arrays — review #1 — completed: 2026-07-13 — clean.
- Missing Number — review #1 — completed: 2026-07-13 — clean.
- Max Consecutive Ones — review #1 — completed: 2026-07-13 — clean, boundary
  fix held (max updated every iteration, not just at reset).
- Single Number — review #1 — completed: 2026-07-13 — clean.
- Longest Subarray with Sum K — review #1 — completed: 2026-07-13 — clean.
- Two Sum — review #1 — completed: 2026-07-13 — clean.
- Sort Array of 0s, 1s, 2s — review #1 — completed: 2026-07-13 — clean,
  invariant reasoning held this time.
- Majority Element (Boyer-Moore) — review #1 — completed: 2026-07-13 — clean.
- Kadane's Maximum Subarray Sum — review #1 — completed: 2026-07-13 — clean,
  all-negative fix held.
- Stock Buy and Sell — review #1 — completed: 2026-07-13 — clean.
- Rearrange Array Elements by Sign — review #1 — completed: 2026-07-13 — clean.
- Next Permutation — review #1 — completed: 2026-07-13 — clean, full
  pivot/successor/suffix-reverse recall held.
- Leaders in an Array — review #1 — completed: 2026-07-13 — clean.
- Longest Consecutive Sequence — review #1 — completed: 2026-07-13 — clean,
  sequence-start pruning recalled correctly.
- Set Matrix Zeroes — review #1 — completed: 2026-07-13 — clean, marker order
  (inner cells first) recalled correctly.
- Frog Jump (DP-3) — review #2 — completed: 2026-07-17 — due was 2026-07-14 —
  clean, dp[2] base case held, no repeat of prior rust.
- Spiral Traversal — review #1 — completed: 2026-07-17 — due was 2026-07-14 —
  clean, one hint (right-pointer direction).
- Subarray Sum Equals K — review #1 — completed: 2026-07-17 — due was
  2026-07-14 — clean, one self-corrected hint (map update logic).
- Find the Largest Element in an Array — review #2 — completed: 2026-07-17 —
  clean.
- Second Largest Element in an Array — review #2 — completed: 2026-07-17 —
  new sentinel-value bug (init -1 collides with negative input), see
  mistake_journal.
- Check if Array is Sorted — review #2 — completed: 2026-07-17 — clean.
- Remove Duplicates from Sorted Array — review #2 — completed: 2026-07-17 —
  clean.
- Move Zeroes to End — review #2 — completed: 2026-07-17 — clean, correctly
  recalled the swap-based one-pass optimization.
- Linear Search — review #1 — completed: 2026-07-17 — clean, first actual
  re-quiz (previously skipped).
- Rotate Array — review #2 — completed: 2026-07-17 — one hint, split-boundary
  confusion (k vs n-k), self-corrected via trace.
- Union of Two Sorted Arrays — review #2 — completed: 2026-07-17 — clean.
- Missing Number — review #2 — completed: 2026-07-17 — clean.
- Max Consecutive Ones — review #2 — completed: 2026-07-17 — clean.
- Single Number — review #2 — completed: 2026-07-17 — clean.
- Longest Subarray with Sum K — review #2 — completed: 2026-07-17 —
  algorithm clean, conceptual gap on seed-value (-1) reasoning closed via
  self-derivation, see mistake_journal.
- Two Sum — review #2 — completed: 2026-07-17 — clean.
- Sort Array of 0s, 1s, 2s — review #2 — completed: 2026-07-17 — clean,
  invariant reasoning held strongly.
- Majority Element (Boyer-Moore) — review #2 — completed: 2026-07-17 — clean.
- Kadane's Maximum Subarray Sum — review #2 — completed: 2026-07-17 — clean,
  correct max-before-reset order.
- Stock Buy and Sell — review #2 — completed: 2026-07-17 — two hints,
  reverted to wrong -1 floor before correcting to 0, see mistake_journal.
- Rearrange Array Elements by Sign — review #2 — completed: 2026-07-17 —
  clean.
- Next Permutation — review #2 — completed: 2026-07-17 — needed real
  correction: pivot index confusion + `>=` vs strict `>` swap-partner bug,
  see mistake_journal.
- Leaders in an Array — review #2 — completed: 2026-07-17 — clean.
- Longest Consecutive Sequence — review #2 — completed: 2026-07-17 — clean,
  strong retention including amortized-complexity reasoning.
- Set Matrix Zeroes — review #2 — completed: 2026-07-17 — clean, resolved a
  genuine follow-up question on shared-cell flags correctly.
- Rotate Matrix (90°) — review #2 — completed: 2026-07-17 — original
  repeat-rust (partial row-reverse) did NOT recur; new slip on transpose
  diagonal swap, self-corrected, see mistake_journal.
- Linear Search — review #2 — completed: 2026-07-20 — clean.
- Spiral Traversal — review #2 — completed: 2026-07-20 — needed real
  correction (pass 3 guard, `bottom--` direction, pass 3/4 direction swap) —
  repeat of 2026-07-13 gap, see mistake_journal.
- Subarray Sum Equals K — review #2 — completed: 2026-07-20 — needed real
  correction (lookup-vs-insert `+1` conflation), see mistake_journal.
- Valid Parentheses — review #1 — completed: 2026-07-21 — clean, no hints.
- Second Largest Element in an Array — review #3 — completed: 2026-07-21 —
  clean, correct INT_MIN sentinel and update-order reasoning cold.
- Kadane's Maximum Subarray Sum — review #3 — completed: 2026-07-21 —
  correct order (max before reset) recalled cold, but the "why" derivation
  was hand-wavy, needed 1 guided-trace hint to land concretely.
- Min Stack — review #1 — completed: 2026-07-21 — needed real escalation (2
  hints): mechanics correct, but "why not a global minSoFar" reasoning was
  genuinely off track until walked through a concrete push/pop trace.
- Rotate Array — review #3 — completed: 2026-07-21 — needed heavy
  escalation: boundary self-corrected quickly, but full "why" derivation of
  the 3-reversal trick was absent, needed full guided one-line trace — 3rd
  time this problem's derivation has needed real help.
- Longest Subarray with Sum K — review #3 — completed: 2026-07-21 — 1 hint:
  added a spurious extra `+1` on top of the `-1` seed, self-corrected via
  the `[5]`,k=5 counterexample.
- Next Permutation — review #3 — completed: 2026-07-21 — clean, no hints,
  full cold derivation, exact prior regression point (pivot + strict `>`
  swap partner) held solid this time.
- Print Subarray with Maximum Sum — review #1 — completed: 2026-07-21 —
  needed heavy escalation: item (1) "why start=tempStart" had fully decayed
  again since the 07-20 "closed" session (2nd decay of the identical point,
  rebuilt from scratch via guided trace); item (2) `[5]` edge case clean
  once broken into single-variable steps.
- Next Greater Element — review #1 — completed: 2026-07-24 — due was
  2026-07-21 — mechanics clean, "why" needed heavy escalation, see
  mistake_journal.
- Implement Queue using Two Stacks — review #1 — completed: 2026-07-24 —
  due was 2026-07-21 — clean, no hints.
- Rotate Matrix (90°) — review #3 — completed: 2026-07-24 — due was
  2026-07-21 — clean, no repeat rust.
- Frog Jump (DP-3) — review #3 — completed: 2026-07-24 — due was 2026-07-21 —
  1 hint, see mistake_journal.
- Pascal's Triangle — review #1 — completed: 2026-07-24 — due was
  2026-07-18 — 1 hint, same loop-bound point (`1` to `L-1` vs `L`) as
  original solve, self-corrected via concrete trace.
- Nearest Smaller to the Left — review #1 — completed: 2026-07-24 — due
  was 2026-07-22 — instance mechanics clean, generalized traversal-
  direction rule needed escalation again (2nd occurrence), see
  mistake_journal.
- Stock Span Problem — review #1 — completed: 2026-07-24 — due was
  2026-07-22 — clean, formula and edge case held, no repeat of the
  off-by-one.
- Sort Array of 0s, 1s, 2s `[derive]` — review #3 — completed: 2026-07-25 —
  due was 2026-07-23 — 1 light nudge on invariant restate, then full "why"
  derivation held cold via elimination framing (regions, safe-mid-advance,
  why 2-case must recheck, termination) — first clean full derivation after
  2 prior reviews of deep confusion on this exact point.
- Move Zeroes to End — review #3 — completed: 2026-07-25 — due was
  2026-07-23 — clean, no hints.
- Stock Buy and Sell — review #3 — completed: 2026-07-25 — due was
  2026-07-22 — clean, no hints; correctly derived why maxProfit=0 floor is
  safe on strictly-decreasing input.
- Remove Duplicates from Sorted Array — review #3 — completed: 2026-07-25 —
  due was 2026-07-23 — mechanics clean via one-line-at-a-time guided trace
  on [1,1,2,2,3]; 1 light nudge needed on why return value is slow+1 (not
  slow), self-corrected immediately.
- Max Consecutive Ones — review #3 — completed: 2026-07-25 — due was
  2026-07-23 — clean, no hints; correctly tracked max every iteration (not
  just on zero-reset), so trailing-run edge case needed no post-loop check —
  standing 3x-flagged boundary bug did not recur.
- Two Sum — review #3 — completed: 2026-07-26 — due was 2026-07-23 — clean,
  no hints.
- Rearrange Array Elements by Sign — review #3 — completed: 2026-07-26 —
  due was 2026-07-23 — clean, plus correctly derived the unequal-count
  leftover-append variant unprompted.
- Min Stack — review #2 — completed: 2026-07-30 — due was 2026-07-24 —
  outcome: correction — first answer had the wrong mechanism (getMin as a
  local/windowed min), self-corrected with own push/pop construction; final
  reasoning (pop removes the min, single var needs an O(n) rescan) correct.
- Dijkstra's Algorithm — review #1 — completed: 2026-07-30 — due was
  2026-07-27 — outcome: partial — scheduled attribution question answered
  correctly cold (non-negative weights, not the PQ; improvement on 07-26),
  but the contradiction proof needed the "node u" construction handed over.
  A `[leech]` tag was raised and retracted as over-tagging.
- Bellman-Ford Algorithm — review #1 — completed: 2026-07-30 — due was
  2026-07-27 — outcome: correction — negative edge vs negative cycle slip
  (fixed by counterexample), and the V-1 justification regressed to
  degree/edge-count reasoning. Both had been clean cold on 07-26.
- Redundant Connection (Union-Find) — review #1 — completed: 2026-07-30 —
  due was 2026-07-28 — outcome: partial — height mechanics clean cold
  (better than the original solve), consequence-of-inflated-rank needed two
  escalations and a constructed example.
- Single Number III (LC 260) — review #1 — completed: 2026-09-03 — outcome: hint —
  split-rule precision needed 1 targeted question (recurrence of the original
  solve's "either" imprecision); any-set-bit generality needed 2 nudges (first
  defended MSB specifically, then gave "yes" with no reason) before landing the
  difference-bit justification unaided.
