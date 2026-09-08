---
type: pattern
pattern: SlotAssignmentGreedy
status: in-use
updated: 2026-08-08
---

# SlotAssignmentGreedy

## When This Pattern Applies

Each item wants one of a bounded number of discrete slots, has a deadline
(latest slot it can occupy) and a value; maximize total value taken.
Distinct from MergeIntervals (continuous time, resource frees up at a
fixed point) and MaxReachGreedy (no per-item value to optimize).

## Core Idea

Sort items by value descending — the objective is total value, and
deadline order has no relationship to that (a low-value early-deadline
item can steal a slot a high-value item also needed). For each item in
that order, place it in the **latest** still-free slot ≤ its deadline
(skip if none free) — taking the latest slot preserves earlier
(tighter-deadline) slots for items with less flexibility.

Naive slot search (scan down from deadline) is O(n · maxDeadline), worst
case O(n²) since maxDeadline ≤ n. A DSU over slots (union each filled slot
to the next free one down) finds the latest free slot in near-O(1)
amortized, bringing the total to O(n log n).

### Variant: bounded heap with eviction (sort flips to deadline ascending)

Same problem, different division of labour. Sort by **deadline ascending**
and keep a min-heap of the profits currently selected; `pq.size()` is the
number of slots used. For each job: if `deadline > pq.size()` there's room,
push it; otherwise the heap is full, so replace the minimum if the new
profit beats it. Answer = heap contents at the end. O(n log n)/O(n).

The sort key flips because the heap now does the selecting — the sort only
has to supply feasibility order. Safety is an exchange argument: a future
job's feasibility test reads `pq.size()`, never *which* jobs are held, so
evict+insert leaves the count (hence every future decision) unchanged while
profit strictly increases.

## Problems Using This Pattern

- Job Sequencing Problem (GFG) — value=profit, one slot per unit time,
  naive O(n²) slot search used; DSU optimization closed 2026-08-07
  (`parent[i]` = nearest free slot ≤ i, `find(deadline)`, `parent[slot] =
  slot-1` on fill; 0 = "no slot" sentinel → O(n log n) total, sort-bound).
  Bounded-heap variant added 2026-08-08 (deadline-asc sort + min-heap
  eviction, O(n log n)) — code read from GFG, not derived; exchange argument
  derived in-session.

## Common Pitfalls

- Sorting by deadline instead of value — doesn't track the actual
  objective. Counterexample: A(d=1,v=1), B(d=2,v=2), C(d=2,v=100), 2
  slots — deadline-sort gives 101, value-sort gives 102.
- Placing each item in the earliest available slot instead of the latest.
  Counterexample: C(v=100,d=2), A(v=50,d=1), 2 slots, value-desc order —
  earliest-slot gives 100 (A dropped), latest-slot gives 150.
- Justifying the eviction/exchange step by restating the objective ("we want
  max profit so dropping the min can't hurt") instead of naming the quantity
  future steps depend on (the count) and showing it's invariant — 2026-08-08,
  4 escalations.
- Assuming the sort key is a property of the problem. It's a property of the
  *solution shape*: profit-desc when the sort selects, deadline-asc when a
  heap selects.
