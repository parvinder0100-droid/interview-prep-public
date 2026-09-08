---
type: flashcards
topic: stack_queue
updated: 2026-07-20
---

# Stack/Queue Flashcards

Format: Q on one line, A (intuition/complexity only, never full code) below it.

Q: Valid Parentheses — what do you check after the loop ends, and why?
A: Stack must be empty — catches unclosed opens (e.g. `"(("`), not just
mismatched closes.

Q: Min Stack — how do you get O(1) getMin without recomputing?
A: Each stack frame stores `(value, minSoFar)` as a pair, so the min up to
that point is always at the top.

Q: Next Greater Element — direction of traversal and what the stack holds?
A: Right to left, monotonic-decreasing stack of *original values* (not
computed answers) — pop everything ≤ current before reading top as the
answer.

Q: Queue via Two Stacks — when do you transfer stack1→stack2?
A: Only when stack2 is empty. If stack2 has elements, pop straight from it,
no transfer.

Q: Queue via Two Stacks — why is it O(1) amortized despite a single dequeue
sometimes costing O(n)?
A: Each element is pushed once, transferred at most once, popped once — ≤3
ops total across its whole lifetime, however those ops are distributed
across n dequeue calls.

Q: Nearest Smaller to the Left — direction of traversal and pop condition?
A: Left to right (traversal starts at the end matching the query side); pop
while top >= current (>= not >, so equal-valued ties don't count as
"smaller").

Q: Monotonic stack — general rule for picking traversal direction on any
"nearest X in direction Y" problem?
A: Start traversal from the end matching side Y, so the stack already holds
the already-processed elements on the queried side by the time you reach
index i.

Q: Stock Span Problem — formula for span given the nearest-greater-left
index?
A: `span = curIndex - nearestGreaterLeftIdx` (no extra -1) — derive via
inclusive-range counting (`b-a+1`, a=ngeIdx+1, b=curIndex), don't guess the
offset. The -1 sentinel for "no such element" needs no special-casing.

Q: Min Stack — why not just one global `minSoFar` variable instead of a
per-frame pair?
A: A global var can't un-learn a min once its owning element pops — e.g.
push 2, push 5, push 1 (global→1), pop 1 → global still says 1, but true
remaining min is 2. Per-frame storage restores the prior min automatically
on pop.

Q: Next Greater Element — why does pushing the computed answer instead of
the original value break it?
A: Later comparisons need real array data, not results — pushing `ans[i]`
means the next element compares against a stale answer, not the true
predecessor value, silently corrupting downstream results.

Q: Min Stack — pair-per-frame vs a separate min-stack: which uses less space?
A: The two-stack version never loses. On 1M increasing pushes the min changes
once, so B holds 1 value (~1M total vs the pair version's 2M). Its worst case
is strictly decreasing input, where every push is a new min and both store 2M.
The pair version's real advantage is simpler code, not space.

Q: Min Stack — what does getMin() actually promise?
A: The minimum of *all elements currently in the stack* — not a window, not a
min "as of the current element". Stating this first is what makes the
"why not one global variable" answer fall out: pop can remove that minimum.

Q: Stack simulation with directional items (Asteroid Collision) — which pairs
actually interact?
A: Only `stack top moving right` + `incoming moving left`. A left-mover already
on the stack and a later right-mover diverge and never meet. Derive this one
condition before writing any push/pop logic — modelling it as symmetric is what
breaks `[-2,-1,1,2]`. Equal magnitudes destroy BOTH, so the survivor test must
be strict.

Q: Stack simulation — you pop several items in a `while`, then continue. What
must you re-check?
A: Every case in the analysis, against the NEW top. Equality/less-than tested
only before the loop misses the pair the cascade exposes: `[10,2,-10]` returns
`[10,-10]` instead of `[]` when equality is checked only pre-loop.

Q: A stack simulation nests a `while` inside a `for`. Why isn't it O(n^2)?
A: Amortized — each element is pushed once and popped at most once, so total
pops across the whole run are bounded by n regardless of how they cluster.

Q: Trapping Rain Water — water level above index i is set by which two bars?
A: The TALLEST bar on each side, not the nearest taller one. A shorter bar in
between is itself submerged to that level, so it caps nothing.
`level = min(maxLeft, maxRight)`, `water_i = max(0, level - height[i])`, summed
per column (width 1 — no area multiply). O(n)/O(n) with two prefix arrays.

Q: In the prefix-max solution to LC 42, when does `min(left,right)-height[i]`
go negative?
A: On every bar taller than the lower of its two walls — both endpoints
(`left[0]=right[n-1]=0`) and every local peak. Clamp with `max(0, ...)`.

Q: Two `nsl/nsr` problems use identical stack code. What decides whether ties must be broken?
A: What the caller does with the spans. `max` (LC 84) tolerates a span claimed by both duplicates; `sum` (LC 907) adds it twice. Strict on exactly one side when summing.

Q: Sum of Subarray Minimums — count of subarrays where `i` is the min?
A: `(i - nsl[i]) * (nsr[i] - i)` — choices of start times choices of end. `i` is a valid endpoint on both sides; `[i,i]` is a subarray.

Q: Largest Rectangle in Histogram — why does the bar at `i` extend exactly to the nearest *smaller* bar each side?
A: Taller bars can be cut down to `h[i]` and still contribute full width; a shorter bar would force the rectangle below `h[i]`. Width = `nsr - nsl - 1`.

Q: Daily Temperatures — why pop on `>=` and not `>`?
A: "Warmer" is strict, so an equal temperature is not an answer. `[73,73]` returns `[1,0]` with `>` instead of `[0,0]`.

Q: Trapping Rain Water in O(1) space — why is it safe to use `leftMax` when it may be smaller than the true left max?
A: The branch only fires when `rightMax < leftMax`, so `rightMax` is the min either way; underestimating the other side can't change `min`.

Q: `java.util.Stack` — why avoid it?
A: Extends `Vector`, so every method is `synchronized`; its iterator runs bottom-to-top, reverse of stack order. Use `ArrayDeque` (no nulls allowed).
