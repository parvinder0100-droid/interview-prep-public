---
type: flashcards
topic: Greedy
updated: 2026-08-06
---

# Greedy — Flashcards

Q: N Meetings in One Room — sort key and boundary condition?
A: Sort by end time. Next meeting's start must be strictly greater than the
last-picked meeting's end (`end < nextStart`, no back-to-back at the same
instant). O(n log n) time, O(n) space (must pair start/end before sorting).

Q: N Meetings — why sort by end time, not start time or duration?
A: End time is what determines when the room frees up. Start-time-sort can
pick a long early-starting meeting that blocks two shorter later ones
(counterexample: (1,10) vs (2,3)+(5,7), 1 vs 2). Duration-sort can pick a
short-but-late meeting that blocks two others spanning it (counterexample:
(4,5) vs (0,3)+(6,10), 2 vs 3). Neither tracks room-availability.

Q: Minimum Number of Platforms — approach and space?
A: Sort arrival[] and departure[] independently (no pairing needed — only
counts matter, not train identity), two-pointer sweep: +1 on arrival, -1 on
departure, track max. O(n log n) time, O(1) extra space.

Q: Minimum Number of Platforms — tie-break when arrival == departure?
A: Process arrival before departure. The problem counts simultaneous
arrival+departure as needing 2 platforms momentarily; departure-first would
net to the same count and silently miss the real overlap.

Q: Minimum Number of Platforms — why does a fully-chained schedule
(each train's departure = next train's arrival) cap at 2 platforms
regardless of chain length?
A: Each interval touches only its immediate neighbor at a single point,
never overlaps two neighbors' interiors — so at any moment at most 2
intervals share that point (the one ending, the one starting).

Q: Jump Game — why does tracking only the max reach so far (not every
path) still guarantee correctness?
A: For any two paths reaching the same index, only the larger resulting
reach matters — it dominates the smaller one (whatever the smaller reach
can do, the bigger one can too, plus more), so collapsing all paths to one
running max loses no information.

Q: Jump Game II — fastest correct approach and complexity?
A: Two-pointer/BFS-level greedy: track current jump's boundary and the
farthest reach seen within it; increment jump count and reset boundary
when the scan passes it. O(n)/O(1) — no heap needed (a max-heap of all
i+nums[i] values also works, correctly, but costs O(n log n)).

Q: Job Sequencing — sort key and why?
A: Sort by profit descending, not deadline. The objective is max profit;
deadline order has no relationship to that and lets a low-profit job claim
a slot a higher-profit job also needed (counterexample: A(d1,p1),
B(d2,p2), C(d2,p100) — deadline-sort gives 101, profit-sort gives 102).

Q: Job Sequencing — which slot does each job take, once sorted?
A: The latest available slot ≤ its deadline, not the earliest. Taking the
latest slot leaves earlier (tighter-deadline) slots free for jobs with no
other option — a bigger-deadline job has more flexibility to slide later.

Q: Job Sequencing — worst-case cost of the naive downward slot scan, and
which input shape hits it?
A: O(n²). All n deadlines = n: the k-th placed job walks past k-1 filled
slots, summing to n(n-1)/2. All deadlines = 1 is only O(n) — each scan
stops in one step.

Q: How do you beat the O(n²) slot scan in Job Sequencing?
A: DSU over slots. `parent[i]` = nearest free slot ≤ i (init parent[i]=i,
index 0 = "no slot" sentinel). `find(deadline)` returns the slot, 0 means
drop the job; after filling slot s, set `parent[s] = s-1`. Path
compression collapses the walked chain, so each find is ~O(α(n)) and the
total drops to O(n log n) — now sort-bound. Generalizes: DSU works on any
"next free/unused resource ≤ x" query, not just graph connectivity.

Q: Job Sequencing sorted by profit descending in one solution and deadline
ascending in another — both correct. What decides the sort key?
A: What the rest of the algorithm does. Array/DSU version: the sort IS the
selection, so it must order by the objective (profit desc). Heap version: a
min-heap does the selection by evicting the weakest, so the sort only has to
supply feasibility order (deadline asc), letting `pq.size()` stand for "slots
used so far".

Q: In the heap version of Job Sequencing, why is evicting the min-profit job
never regretted?
A: A future job's feasibility test is `deadline > pq.size()` — it reads the
count, not which jobs are held. Evict+insert leaves the count unchanged, so
every future decision is identical while total profit strictly rises. General
form of the exchange argument: find what later steps depend on, show the swap
leaves it invariant.

Q: What two things must every greedy exchange argument show?
A: Take an optimal solution that disagrees with the greedy choice at the FIRST
point of disagreement, swap locally, then show (1) still feasible, (2) value
does not decrease. Restating the objective ("we want max value") proves
nothing. See patterns/GreedyExchangeArgument.md.

Q: Fractional Knapsack — prove highest value/weight ratio first is optimal
(not just state the rule).
A: Take a packing holding one unit of weight of a lower-ratio item while a
higher-ratio item still has weight outside the bag. Swap that unit. Weight is
unchanged (feasible), value changes by ratio(high) − ratio(low) > 0, so the
packing was strictly improvable, therefore not optimal. Only highest-ratio-
first survives.

Q: You sort an array of (weight, value) items by ratio in Java. What is the
space complexity, and why isn't it O(log n)?
A: O(n). O(log n) is the primitive branch — `Arrays.sort(int[])` is an
in-place dual-pivot quicksort. Object/pair arrays go to TimSort, which is
stable and allocates an O(n) auxiliary buffer. The `Item[]` you build is O(n)
too, so the two tie.

Q: Candy (LC 135) — you compute a left-to-right pass and a right-to-left pass.
Why is taking the max of the two per child valid, and why is it minimal?
A: Valid — if the left constraint binds at i then ratings[i-1] < ratings[i], so
the right pass leaves right[i-1] at 1 and c[i-1] = left[i-1]; then
c[i] >= left[i] = left[i-1]+1 > left[i-1] = c[i-1]. Symmetric on the other
side, so the two passes can never fight. Minimal — left[i] is the length of the
increasing run ending at i, and any valid assignment must exceed the previous
child along that run, so v[i] >= left[i] and symmetrically v[i] >= right[i].

Q: Assign Cookies — prove giving the greediest child the largest cookie is safe.
A: Rival gives greediest child C some cookie k, and largest cookie L to another
child D. Swap. C still content since s[L] ≥ s[k] ≥ g[C]; D still content since C
was the greediest, so g[D] ≤ g[C] ≤ s[k]. Count unchanged, so the greedy choice
is never worse. Other branch: if even L can't satisfy C, no remaining cookie
can, so dropping C costs nothing.

Q: You sort an `int[]` and use four scalar variables. Space complexity?
A: O(log n), not O(1) — `Arrays.sort(int[])` is dual-pivot quicksort and uses
O(log n) recursion stack. Primitives O(log n), objects O(n) (TimSort buffer).
Whenever a solution sorts, ask "primitives or objects?" before answering space.

Q: What must a greedy justification contain before it counts as a proof?
A: A named rival plan, one explicit move applied to it, and two compared
numbers. Closing sentence takes one of two shapes: "count(O') ≥ count(O), so no
optimal plan beats ours" or "we can construct a strictly better plan, therefore
that plan wasn't optimal." Intuition sentences ("we'd waste it") are not proofs.

Q: When does a max-heap beat sorting for a "process items in key order" greedy?
A: Only when you stop early. Bulk heapify is O(n) and k pops cost k log n, so
it wins at k << n. Inserting n items one at a time is O(n log n) and wins
nothing — the sort gives the same order upfront.

Q: When is sorting the input free, and when does it destroy the problem?
A: Free only when the input is a set (Assign Cookies' cookie sizes, Fractional
Knapsack's items). It destroys a *sequence* — Lemonade Change's bills arrive in
queue order and change must exist at the moment each customer pays, so `[10,5]`
is false while sorted `[5,10]` is true. Ask "set or sequence?" before sorting.

Q: $20 customer, you hold both a ten and three fives. Which do you give, why?
A: ten+five. Against a rival paying 5+5+5 you end up with 2 extra fives and 1
fewer ten. A ten's only job is the $15 owed on a $20 (as 10+5); two fives cover
that same job *and* can pay a $10 customer, which a ten never can. Spend the
rigid bill, hoard the flexible one.

Q: A scan carries an open-bracket count and the input has wildcards. What is the
honest state, and what do you actually store?
A: The *set* of counts still reachable over all live wildcard assignments. Every
operation maps a contiguous set to a contiguous set (deterministic chars shift
it, a wildcard unions three overlapping shifts, pruning cuts a prefix), so store
only the two endpoints. O(n)/O(1). DP over (index, balance) is the O(n²)
fallback.

Q: `min` goes negative vs `max` goes negative — different consequences?
A: `max < 0` = the largest reachable count is negative, so every assignment is
dead: fail immediately. `min < 0` = only the lowest branch died; clamp to 0 and
keep walking. `*)` hits min = −1 and is still valid (`*`=`(`).

Q: Accept condition at the end of a reachable-range scan?
A: The target must lie in the surviving interval: `min <= 0 <= max`, which with
the clamp already applied is just `min == 0`. Not `max >= 0`.

Q: Merging overlapping intervals — sort by which endpoint, and why not the one used for interval *selection*?
A: Sort by **start** for merging (selection sorts by end). Merging asks "does this one touch the block I'm building", which is a question about starts; selection asks "when does the resource free up", which is about ends.

Q: When merging intervals, why is it enough to compare each incoming interval against only the last one kept?
A: The kept intervals are disjoint and their **ends increase**, so the last end is the largest. If the incoming start clears that end, it clears every earlier one.

Q: `[1,4]` and `[4,5]` — merge or not, and what does that make the overlap test?
A: Merge (they touch). Test is `last[1] >= cur[0]`, with `>=`, not `>`.

Q: Reachable-range scan for `*` wildcards — why does the accept condition `min <= 0 <= max` collapse to `min == 0`?
A: The clamp forces `min >= 0` and the `max < 0` bail-out means reaching the return implies `max >= 0`. So only `min <= 0` is left to test, and with `min >= 0` that is `min == 0`.

Q: Why must the clamp `if (min<0) min=0` and the bail `if (max<0) return false` be two independent `if`s?
A: `min <= max` always, so `max < 0` implies `min < 0`. Chained as `else if`, the clamp always fires first and the bail is dead code — `")*"` is then wrongly accepted.

Q: SJF — waiting time of the i-th process run, in terms of the burst times?
A: The sum of every burst that ran before it. So one pass with a running clock: add the clock to the total, then advance the clock by this burst. Sort ascending first.

Q: `Arrays.sort(int[])` vs `Arrays.sort(Integer[])` — space?
A: `int[]` is dual-pivot quicksort, in-place, O(log n) recursion stack. Object arrays are TimSort, O(n) merge buffer. Always ask "primitives or objects?" before answering sort space.

Q: A scheduling statement gives you burst times and asks for average waiting time. What's the hidden decision variable?
A: The order you run them in. If a statement won't parse, run the sample under any arbitrary choice and diff against the expected output — the gap names the choice.

Q: Two intervals overlap and exactly one must be removed. Which do you keep?
A: The one that ends earlier — it leaves at least as much room for everything
after it, so no later interval is lost by the swap. Sort by end, not by start.

Q: You passed a comparator to `Arrays.sort`. What does that alone tell you about the space cost?
A: O(n). The primitive overloads have no comparator form (`Comparator<T>` can't
be parameterized on a primitive), so a comparator means an object array, which
means TimSort and its O(n) merge buffer. `int[][]` counts as an object array.

Q: Coins {1,2,5,10}, take as many 10s as possible first. Why is that optimal?
A: Removing one 10 leaves 10 to cover with coins ≤ 5, which needs ≥2 coins, so
every swap-down costs at least one extra coin. Note this argument depends on
the denomination set — it is not a general coin-change proof (LC 322 needs DP).
