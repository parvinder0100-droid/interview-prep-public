---
type: note
problem: Task Scheduler (LC 621)
topic: Heaps / Greedy
updated: 2026-08-04
---

# Task Scheduler (LC 621)

Attempted 2026-08-02 16:54 — approach only, **code not written, formula and
edge cases still open**.

## Greedy rule

Among tasks currently available, always run the one with the highest
remaining frequency. The max-frequency task fixes the skeleton — `maxFreq-1`
gaps of width `n` that everything else fills. Scheduling it late only pushes
its own chain later.

## The two things that broke

**Tie-break key.** Ordering by availability time alone leaves ties
undetermined, and breaking them by task label is arbitrary. Ties must break
on **remaining frequency, descending**.

**Cooldown offset.** Re-push availability is `current + n + 1`, not
`current + n` — `n` counts the *empty slots between* two runs of the same
task. Smallest case that exposes it: `[A,A]`, `n=2` → schedule is
`A _ _ A` = 4 slots; `current + n` reports 3.

## Complexity

Heap holds at most 26 entries, a constant → `O(N)` time, `O(1)` space.

## Closed form (open — decayed within minutes of being derived)

Block picture: `maxFreq-1` full blocks, each `n+1` wide (one task + its gap),
then a final partial block holding one slot per max-frequency task.

    (maxFreq - 1) * (n + 1) + countMax

Verified: `A×4, n=2` → 3*3+1 = 10 ✓ · `A×3,B×3, n=2` → 2*3+2 = 8 ✓

**Still open at session end**: the formula undercounts when there are enough
distinct tasks to fill every idle slot — e.g. `[A,A,B,B,C,C,D,D]`, `n=1`
gives 6 but the answer is 8. True answer is `max(formula, tasks.length)`.
Edge cases and code also not done.

## 2026-08-04 — review #1, formula fully decayed, rebuilt

Cold recall gave `(maxFreq-1)*n + maxFreq` — wrong on two counts (block width
should be `n+1` not `n`; last term should be `countMax` not `maxFreq`).
Caught via trace (A×3,B×3,n=2 → formula 7, true 8) and rebuilt via own
index-diff trace (A positions 0,3,6 → gap 3 = n+1). Landed back on
`(maxFreq-1)*(n+1) + countMax`, closed the loop verbally this time. **Still
open**: the "why does it undercount vs `max(formula, tasks.length)`" question
was posed but session ended before an answer — resume there, then edge cases,
then code. 2nd decay of this exact formula — one more repeat is `[leech]`.
