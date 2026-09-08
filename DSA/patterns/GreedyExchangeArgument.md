---
type: pattern
pattern: GreedyExchangeArgument
status: in-use
updated: 2026-08-11
---

# Greedy Exchange Argument

Not an algorithm — the standard way to *justify* a greedy rule. Created
2026-08-08 after the same justification gap recurred in 4 consecutive Greedy
sessions: mechanics come out cold every time, the "why" does not.

## The Shape

Take any optimal solution `OPT` that disagrees with the greedy choice at the
first point of disagreement. Transform `OPT` into one that agrees, by a single
local swap. Show the swap (a) keeps the solution feasible, and (b) does not
decrease its value. Therefore a solution making the greedy choice is at least
as good — repeat down the sequence.

Key discipline: name **what the later steps actually read** (remaining
capacity, remaining slots, the current end time) and show the swap leaves it
no worse. Restating the objective ("we want the max value so we take the best
item") proves nothing — that is the recurring failure mode below.

## Problems Using This Pattern

- N Meetings in One Room — why sort by end time (swap the first meeting of OPT
  for the earliest-ending one; the room frees no later) — 2026-08-05.
- Jump Game (LC 55) — why max-reach dominates — 2026-08-06.
- Job Sequencing, bounded-heap variant — why evicting the heap minimum is
  never regretted (swap leaves the count of selected jobs invariant, raises
  total profit) — 2026-08-08.
- Fractional Knapsack — why highest value/weight ratio first — **closed
  2026-08-08 23:24**. Swap one unit of weight between two items: the delta is
  exactly ratio(high) − ratio(low) > 0 and the weight is unchanged, so any
  packing holding a lower-ratio unit while a higher-ratio item is unexhausted
  is strictly improvable, hence not optimal. What the later steps read here is
  *remaining capacity*, and a unit-for-unit swap leaves it identical.
- Assign Cookies (LC 455) — why the greediest child takes the largest cookie —
  2026-08-11. Rival gives C cookie k and D the largest L; swap them. C survives
  (`s[L] ≥ s[k] ≥ g[C]`), D survives because C is the greediest remaining, so
  `g[D] ≤ g[C] ≤ s[k]`. Count unchanged. Second branch is separate and easier:
  if `s[L] < g[C]` then no remaining cookie fits C, so dropping C is free.
- Lemonade Change (LC 860) — why paying a $20 with ten+five is never regretted
  — 2026-08-12. **New sub-shape: state-domination, not value-comparison.** The
  swap compares *resources held afterwards*, not the objective: vs a rival
  paying 5+5+5, you hold 2 extra fives and 1 fewer ten. A ten's only job is the
  $15 owed on a $20; two fives do that job and also serve a $10 customer, which
  a ten cannot. So your state dominates the rival's at every future step.
  **The prompt that unlocks it**: "write both wallets right after the same
  customer — what's the exact difference?" Use this whenever the greedy choice
  is *which resource to spend* rather than *which item to take*.
- Shortest Job First (GFG) — why shortest burst first minimizes average wait —
  **open, not attempted 2026-08-14.** Code and complexity came cold; the
  argument was posed as the Interview Script below and declined. Queued for the
  08-16 review as a one-sentence why. (For the mentor's own reference, not to
  be handed over: a job of length `b` run at position `k` from the end adds `b`
  to the wait of every one of the `k-1` jobs behind it, so swapping an adjacent
  out-of-order pair strictly reduces the total.)

## Common Pitfalls

- Answering "why is this greedy safe" by restating the goal instead of
  performing a swap. 4 occurrences, 2026-08-05 through 2026-08-08.
- Arguing at the level of the whole solution rather than the **first point of
  disagreement** — the induction needs a local swap, not a global comparison.
- Forgetting the feasibility half: a swap that raises value but breaks
  capacity/deadline proves nothing.
- Stopping at the *rule* ("take as much of A as possible, fill the rest with
  B") instead of the *proof* ("from P we can construct a strictly better
  packing, therefore P is not optimal"). The rule is the algorithm; the
  conclusion has to be a contradiction about optimality — 2026-08-08.

## What Actually Works (2026-08-08)

Five sessions of failure with abstract phrasing, one success: the argument
only comes out when it is instantiated numerically. Working sequence — value
of one unit of each item, old total written out, new total written out,
subtract, *then* express the delta symbolically, *then* fill in "we can
construct ___, therefore P is not ___". Skipping straight to the delta
produced a guess (20 vs the true +5).

## Conclusion Form (added 2026-08-11, user asked for it directly)

The proof is only finished when the last sentence has this shape. Two variants:

**Shape 1 — exchange (equal or better).**
> Take any optimal plan O that differs from our choice at the first step. Build
> O' by <the swap>. count(O') ≥ count(O). So no optimal plan beats our choice.

**Shape 2 — strictly improves (contradiction).**
> If a plan does not do what we do, we can construct a strictly better plan.
> Therefore that plan was not optimal.

Test for whether an answer qualifies: it must contain a **named rival plan**, an
**explicit move**, and a **compared number**. "We'd lose the count" has none of
the three and is the recurring non-answer.

## Interview Script (added 2026-08-11)

Four sentences, ~60 seconds, delivered in symbols:

1. State the rule.
2. Name the rival — "suppose an optimal solution does something else at the
   first step".
3. Make the move, check both halves (feasible / value).
4. Close with Shape 1 or Shape 2, then "induct on the remainder".

Delivery rules: do the numeric instantiation on scratch paper or narrate it as
"let me sanity-check a small case" — examples are the derivation tool, not the
answer. Never open with the example; open with the rule. If stuck with time
running, say "intuition is X, let me verify with an exchange argument" and build
it aloud — the attempt at rigor is what is being scored.

Framing that landed for this user: instantiation is the scientist half (cheap,
finds the shape, never conclusive); symbolizing is the mathematician half (makes
it airtight against every input). An interview answer needs both, in that order,
but only the second is spoken.

**How to pose it — amended 2026-08-14 after a 3rd decline.** The script has now
been offered three times and run zero times: 08-12 ("I already solved the
problem"), 08-13 (not posed), 08-14 ("i dont think we need script for all the
problems"). The objection is correct on its own terms — this is a delivery
format for a hard *why*, not a per-problem ritual, and posing it after a clean
solve reads as make-work. **Stop asking for "the script."** Ask the plain
one-sentence why on every greedy; expand to the four sentences only when that
sentence doesn't come, or when the rule is genuinely non-obvious (a new
sub-shape, or a problem where the user's first answer restates the goal). The
script's value is as scaffolding for a stuck answer, not as a recital.

## Flashcard-worthy

Q: What are the two things every exchange argument must show?
A: The swap keeps the solution feasible, and does not decrease its value.
- Minimum Coins {1,2,5,10} — why largest-denomination-first — 2026-08-18.
  Swap shape: remove one unit of the chosen coin and pay the same amount with
  smaller ones; the replacement costs ≥2 coins because the next denomination is
  less than half. Landed in 2 escalations via the standard numeric
  instantiation (n=39: 6 coins vs 7). **Scope note**: this argument reads the
  denomination *ratios*, so it does not generalize — {1,3,4} breaks it (6 = 3+3
  beats 4+1+1), which is why general coin change is DP.
