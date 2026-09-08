---
type: note
problem: Job Sequencing Problem (GFG)
topic: Greedy
updated: 2026-08-07
---

Two wrong approaches before the correct one, both self-corrected via
constructed counterexamples the user traced by hand.

**Wrong sort key (deadline instead of profit).** Trace on
A(d=1,p=1), B(d=2,p=2), C(d=2,p=100), 2 slots: deadline-ascending order
processes A first, claims slot1, leaving B to be dropped when C takes
slot2 → total 101. Profit-descending order lets B also claim a slot →
total 102. Deadline has no relationship to the objective (maximize
profit); profit does.

**Wrong slot direction (earliest instead of latest available).** Trace on
C(p=100,d=2), A(p=50,d=1), 2 slots, profit-desc order (C then A): if C
takes the earliest available slot (slot1), A (deadline=1) has nowhere to
go → total 100. If C takes the latest available slot ≤ its deadline
(slot2), A gets slot1 → total 150. Taking the latest slot preserves
earlier slots for jobs with less deadline flexibility.

**Correct approach:** sort by profit descending; for each job, scan down
from its deadline to find the latest still-free slot; skip if none free.

```java
Arrays.sort(grp, (a,b) -> b.profit - a.profit);
for (job in grp) {
    int slot = job.deadline;
    while (slot > 0 && slots[slot]) slot--;
    if (slot == 0) continue;
    slots[slot] = true;
    profit += job.profit;
}
```

Complexity: O(n log n) sort + O(n · maxDeadline) worst case for the
slot-search loop (maxDeadline ≤ n per problem constraints) → O(n²) worst
case overall.

**Pressure-test closed 2026-08-07.** Per-job scan is ≤ d steps; worst case
is all deadlines = n (k-th placed job walks past k-1 filled slots, sum
n(n-1)/2 = Θ(n²)). All deadlines = 1 is only O(n) — each scan stops
immediately. DSU optimization (`parent[i]` = nearest free slot ≤ i,
`find(deadline)`, `parent[slot] = slot-1` on fill, 0 = "no slot"
sentinel) drops the search to ~O(α(n)) amortized → O(n log n) total,
sort-bound. Complexity and worst-case shape were derived cleanly; the DSU
idea was **not** reached — full explanation given after a category hint
and a parking-lot analog both failed. See mistake_journal 2026-08-07.
