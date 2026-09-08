---
type: recall_log
frequency: daily
updated: 2026-09-04
---

# Daily Active Recall Log

One section per day. Recall questions are generated live during sessions and logged here for
future spaced-repetition review — never with the answer written out, only the question and a
pointer to the relevant note.

## 2026-07-06

_Session started. Recall questions will be appended here as the first problem is worked
through._

## 2026-07-20

- Why is Queue-via-Two-Stacks O(1) amortized per operation, despite a single
  dequeue sometimes costing O(n)? — see mistake_journal 2026-07-20
  (Implement Queue using Two Stacks).

## 2026-07-21

- Why does wrong-order Kadane's (reset before max-check) break on an
  all-negative array? — see mistake_journal 2026-07-21 (Kadane's, review #3).
- Why not just one global `minSoFar` variable instead of a per-frame pair? —
  see mistake_journal 2026-07-21 (Min Stack, review #1).
- Why does reverse-chunk1/reverse-chunk2/reverse-whole actually rotate the
  array? — see mistake_journal 2026-07-21 (Rotate Array, review #3).
- Why `start=tempStart` not `start=i` on a new max? — see mistake_journal
  2026-07-21 (Print Subarray with Maximum Sum, review #1, 2nd decay).

## 2026-07-24

- Why does pushing the computed answer instead of the original value break
  Next Greater Element's comparisons? — see mistake_journal 2026-07-24
  (Next Greater Element, review #1).
- Why is Frog Jump's recurrence a `min`, not an addition, of the two jump
  options? — see mistake_journal 2026-07-24 (Frog Jump, review #3).
- Why can't the net sliding-window length shrink back down once it's grown,
  in an at-most-K problem, even though maxFreq goes stale? — see
  mistake_journal 2026-07-24 (Longest Repeating Character Replacement).
- What's the transferable rule for choosing monotonic-stack traversal
  direction (left-to-right vs right-to-left)? — see mistake_journal
  2026-07-24 (Nearest Smaller to the Left, review #1).

## 2026-07-25

- Why is it safe to advance `mid` when `arr[mid]==0` in Dutch National Flag
  — what do you know about the value that was at `low`? — see
  mistake_journal (Sort 0s/1s/2s, review #3, [note](../notes/sort-012.md)).
- In DFS on a graph, when should you mark a node visited — before recursing
  or after? — see mistake_journal 2026-07-25 (DFS Traversal of Graph).
- In BFS, does marking `visited` on pop vs on push change correctness — walk
  the case where two unprocessed nodes share a neighbor. — see
  mistake_journal 2026-07-25 (BFS Traversal of Graph).
- In multi-source BFS (Rotten Oranges), what should gate the minute-counter
  increment — a level running, or something else? — see mistake_journal
  2026-07-25 (Rotten Oranges).
- Why does an odd-length cycle make a graph non-bipartite — connect it to
  color-flips per edge. — see mistake_journal 2026-07-25 (Bipartite Check).
- In Kosaraju's algorithm, why does the second DFS have to start from the
  last-finished node (not any unvisited node) to correctly isolate SCCs? —
  see mistake_journal 2026-07-25 (Kosaraju's Algorithm).
- Longest Consecutive Sequence's start-pruning is O(n) — how many times does
  any single element get visited inside the inner while-expansion loop,
  across the whole run? — see mistake_journal 2026-07-25 (Longest
  Consecutive Sequence, review #3).

## 2026-07-26

- What's the complexity of Dijkstra, derived from operation count (not a
  memorized formula)? — see mistake_journal 2026-07-26 (Dijkstra's
  Algorithm, complexity notation).
- Why does Dijkstra give a wrong answer (not an infinite loop) with a single
  negative edge and no cycle? — see mistake_journal 2026-07-26 (Dijkstra's
  Algorithm, negative-edge failure mode).
- Dijkstra's "pop = final" promise: which is load-bearing, the priority queue
  or the non-negative weights, and what exactly does a negative edge break? —
  see mistake_journal 2026-07-26 15:28 (Dijkstra visited-lock, recurrence 2).
- In Bellman-Ford, why does the negative-cycle detection loop need the same
  `dist[u] != INF` guard as the relaxation loop? — see mistake_journal
  2026-07-26 15:28 (Bellman-Ford).
- In Floyd-Warshall, why must `k` be the outermost loop — what does
  `dist[i][j]` mean after the `k` loop finishes iteration `k=K`? — see
  mistake_journal 2026-07-26 23:27 (Floyd-Warshall, unresolved).

## 2026-07-27

- In union-by-rank, why does rank only increment on the tie branch — what
  goes wrong (concretely, not just "the number's wrong") if it increments on
  a strict win too? — see mistake_journal 2026-07-27 16:36 (Union-Find rank
  invariant).

## 2026-07-30

- Min Stack: what exactly does getMin() promise — and which single operation
  makes one global min variable insufficient? — see mistake_journal
  2026-07-30 17:06.
- Dijkstra: reproduce the pop-is-final argument as 5 numbered steps, cold,
  with no node handed to you. — see mistake_journal 2026-07-30 17:17.
- Bellman-Ford: V-1 counts what, exactly? And a still-improving Vth round
  proves what, exactly? — see mistake_journal 2026-07-30 17:27.
- Union-Find: who reads `rank`, and what wrong decision does an inflated rank
  cause? — see mistake_journal 2026-07-30 17:44.

## 2026-07-31

- Floyd-Warshall: state the invariant `dist[i][j]` holds right after the k=B
  pass finishes, and why that makes it safe to use in the k=C pass — see
  mistake_journal 2026-07-31 15:49 (3rd stall, same point).

## 2026-08-01

- Floyd-Warshall: after stepping both k-outer and k-inner traces yourself
  (interactive artifact), state in your own words why k must be the
  outermost loop — see mistake_journal 2026-08-01 08:35 (4th stall, same
  point).
- Min Cost to Connect All Points: state the cut-property swap-argument for
  why cheapest-edge-first is safe, cold, no numeric example handed to you —
  see mistake_journal 2026-08-01 09:24.
- Prim's: state the relax rule cold, and say out loud why it's not
  cumulative like Dijkstra's — see mistake_journal 2026-08-01 16:52.
- Prim's array-based O(n²): write the full loop unaided (min-scan +
  visited + relax, no PQ) — see mistake_journal 2026-08-01 17:09.
- Kruskal's: explain why `parent[0]` was wrong even though it "worked" —
  see mistake_journal 2026-08-01 16:39.
- Kth Largest Element: is push-one-by-one the only way to build a heap?
  What's the faster way, and why is it faster? — see mistake_journal
  2026-08-01 17:37.
- Top K Frequent Elements: min-heap-of-size-k eviction — which comparator
  direction, and why does it have to match what you're evicting? — see
  mistake_journal 2026-08-01 22:00.

## 2026-08-02

- Find Median from Data Stream: which half goes in which heap, and what
  makes that assignment (not the reverse) the one that gives O(1) median?
  — see mistake_journal 2026-08-02 10:47.
- Find Median from Data Stream: your rebalance only moves max→min. What
  state does that let the heaps reach, and what does the median read
  become? — see mistake_journal 2026-08-02 16:54.
- Merge k Sorted Lists: auxiliary space — what exactly are you holding
  beyond input and output, and does the result allocate anything? — see
  mistake_journal 2026-08-02 16:54.
- Task Scheduler: a task just ran at time t with cooldown n. When is it
  next available, and what does n count? — see mistake_journal
  2026-08-02 16:54.
- Task Scheduler: state the closed-form formula and say what each term
  counts, without tracing a schedule first — see mistake_journal
  2026-08-02 16:54.

## 2026-08-04

- Task Scheduler: why does the closed-form formula undercount when there
  are enough distinct tasks to fill every idle slot? — see mistake_journal
  2026-08-04 (Task Scheduler, 2nd decay).

## 2026-08-06

- Jump Game: why does tracking only the max reach (not every path) still
  guarantee correctness? — see mistake_journal 2026-08-06.
- Job Sequencing: what should the sort key be, given the goal is maximizing
  profit — and why isn't deadline order enough? — see mistake_journal
  2026-08-06.
- Job Sequencing: once sorted, which slot should a job take — earliest or
  latest available ≤ deadline — and why? — see mistake_journal 2026-08-06.

## 2026-08-07

- Job Sequencing: the naive scan re-walks the same filled slots for every
  job — what would you store per slot to jump straight to the nearest free
  slot ≤ d, and which structure is that? — see mistake_journal 2026-08-07.

## 2026-08-08

- Job Sequencing (heap variant): the heap is full and a new job's profit
  beats the minimum — why can you never regret evicting that minimum? —
  see mistake_journal 2026-08-08.
- Fractional Knapsack: a filled bag contains a unit of a lower-ratio item
  while a higher-ratio item still has weight left outside — what does
  swapping one unit do to the total, and why does that prove the rule? —
  see mistake_journal 2026-08-08 20:46.
- Fractional Knapsack: you sort an array of item objects by ratio — what is
  the space complexity of the solution, and what decides it? — see
  mistake_journal 2026-08-08 23:24.

## 2026-08-09

- Candy: index i takes the max of the two passes, and i-1 might have taken its
  value from the *other* pass — why does the strict inequality still hold? —
  see mistake_journal 2026-08-09 16:39.
- Candy: is O(1) extra space reachable, and what structure in the ratings array
  makes it possible? — see mistake_journal 2026-08-09 16:41.

## 2026-08-11

- Assign Cookies: your solution sorts two arrays and declares four ints — what
  is the space complexity, and what decides it? — see mistake_journal
  2026-08-11 20:10.
- Assign Cookies: an optimal assignment gives the greediest child C a cookie
  that is not the largest — what one move turns it into ours, and why does
  neither child stop being content? — see mistake_journal 2026-08-11 20:12.

## 2026-08-12

- Lemonade Change: an optimal plan pays a $20 customer with three fives where
  yours pays ten+five — what do the two wallets differ by right after that
  customer, and why does that difference never hurt you? — see mistake_journal
  2026-08-12 17:32.
- Lemonade Change: your code sorts `bills` before the sweep — what does
  `[10,5]` return, and what does it say about when sorting is free? — see
  mistake_journal 2026-08-12 17:26.
- Valid Parenthesis String: the reachable open-counts after `(**` are
  `{0,1,2,3}` — why is that set never full of holes, whatever the input? — see
  mistake_journal 2026-08-12 17:43.
- Valid Parenthesis String: `min` and `max` are the smallest and largest of
  *what* collection of numbers? — see mistake_journal 2026-08-12 20:22.
- Valid Parenthesis String: `min` goes negative but `max` is still 3 — why is
  the string not yet dead, and what is `min` set to? — see mistake_journal
  2026-08-12 20:22.
- Valid Parenthesis String: in `if (min<0) min=0; else if (max<0) return false;`
  what does `)` return, and why can the second check never run? — see
  mistake_journal 2026-08-12 20:31.

## 2026-08-13

- Valid Parenthesis String: your loop clamps `min` at 0 and bails on `max<0`.
  Build a string that the buggy `else if` version wrongly accepts — what has to
  be true at the end for it to return true? — see mistake_journal 2026-08-13 17:10.
- Valid Parenthesis String: the accept condition you derived was `min<=0<=max`,
  the code checks only `min==0` — why are those the same? — see progress.md
  2026-08-13 (parked open).
- Merge Intervals: you compare the incoming interval only with the last one in
  the output list — name the quantity that makes an earlier overlap impossible.
  — see mistake_journal 2026-08-13 17:36.

## 2026-08-14

- Shortest Job First: you sort ascending and it's correct — in one sentence,
  why does running a shorter job before a longer one never raise the total
  waiting time? — open, declined in session, see progress.md 2026-08-14 22:20.
- Shortest Job First: `Arrays.sort` on `int[]` vs on `Integer[]` — which space
  cost does each carry, and why do they differ? — see mistake_journal
  2026-08-14 22:20.

## 2026-08-15

- Floyd-Warshall: after the outer loop finishes value `k`, what does `dist[i][j]`
  mean? (ask this *before* "why k outer") — see mistake_journal 2026-08-15.
- Union-Find: which single operation reads `rank`, and is an inflated rank a
  correctness bug or a cost bug? — see mistake_journal 2026-08-15.
- Bellman-Ford: can a shortest path repeat a node? Therefore how many edges can
  it have? — see mistake_journal 2026-08-15.
- Bellman-Ford: does the algorithm work on graphs with negative edges? So what
  can a still-improving Vth round mean? — see mistake_journal 2026-08-15.
- LC 678: list every open-bracket count reachable after the prefix `(*`. Is
  `min` always one of them? — see mistake_journal 2026-08-15.
- Heaps: sift-down assumes what about a node's subtrees, and why does that force
  build-heap to run bottom-up? — see mistake_journal 2026-08-15.
- Heaps: which nodes cost `log n` sift-down steps, and how many such nodes are
  there? — see mistake_journal 2026-08-15.
- Java: you passed a comparator to `Arrays.sort`. What does that tell you about
  the sort's space cost, without looking at the array's type? — see
  mistake_journal 2026-08-15.
- LC 435: two intervals overlap and exactly one must be removed. Which do you
  keep, and what property makes it safe? — see mistake_journal 2026-08-15.

## 2026-08-18

- Minimum Coins: drop one 10 from a plan. What is the fewest coins that can
  cover that missing 10, and what does that number prove? — see mistake_journal
  2026-08-18.

## 2026-08-23

- LC 1358: in an at-most window you add `j-i+1` at each step. Why is no
  substring counted twice, and why is none missed? — see mistake_journal
  2026-08-23.
- "Exactly 3 distinct characters" and "contains at least one a, one b, one c" —
  when are these the same set, and when do they come apart? — see
  mistake_journal 2026-08-23.
- LC 735: two asteroids are adjacent on the stack. Under exactly which sign
  combination do they collide, and which combinations never meet? — see
  mistake_journal 2026-08-23.

## 2026-08-24

- LC 735: a pop-cascade just emptied several asteroids off the stack. Which of
  the three outcome cases can now be true that was false before the loop ran? —
  see mistake_journal 2026-08-24.
- Why is a stack simulation with a nested `while` still O(n) and not O(n^2)? —
  see mistake_journal 2026-08-24.

## 2026-08-25

- LC 930: state the exit invariant of the shrink `while` in one sentence —
  "when this loop exits, `[i..j]` is ___". Does your guard guarantee it when
  the window must empty? — see mistake_journal 2026-08-25.
- Why does `atMost(-1)` return 0 without any explicit `goal < 0` short-circuit?
  — see mistake_journal 2026-08-25.

## 2026-08-26

- LC 42: why is the boundary the *tallest* bar on each side and not the nearest
  taller one? Answer with what happens to a short bar in between. — see
  mistake_journal 2026-08-26.
- LC 42: `min(left[i], right[i]) - height[i]` goes negative on which indices,
  and what property do they share? — see mistake_journal 2026-08-26.

## 2026-08-27

- LC 907: your `nsl/nsr` code is identical to LC 84's. Why does `[2,2]` come out
  wrong here and right there? — see mistake_journal 2026-08-27.
- LC 907: how many valid start indices does index `i` have, and why is `i` one
  of them? — see mistake_journal 2026-08-27.
- LC 907: the problem says "mod 1e9+7". What is that telling you about `int`?
  — see mistake_journal 2026-08-27.
- LC 42 O(1): write the 4-line loop body from the argument you derived — update,
  compare, settle, move. — see mistake_journal 2026-08-27.
- Java: why does an interviewer flag `new Stack<>()`, and what replaces it?
  — see mistake_journal 2026-08-27.

## 2026-08-28

- Frog Jump O(1): at the top of iteration `i`, what must `backbyone` and
  `backbytwo` each hold, in `dp[...]` terms? — see mistake_journal 2026-08-28.
- Frog Jump: your recurrence indexes `dp[i-2]`. What is the smallest `i` the
  loop may start at, and why? — see mistake_journal 2026-08-28.
- Subsets: how many times does `res.add(new ArrayList<>(list))` run, and what
  does each run cost? — see mistake_journal 2026-08-28.
- Combination Sum: you wrote three recursive calls. Which one is redundant, and
  which two paths produce the same combination? — see mistake_journal 2026-08-28.
- Combination Sum: you declared `res` as a `HashSet`. What does needing it tell
  you about the branching? — see mistake_journal 2026-08-28.

## 2026-08-29

- Combination Sum II: your two terminal checks are `sum==target` and
  `index>=nums.length`. Which must run first, and what input proves it? — see
  mistake_journal 2026-08-29.
- Combination Sum II: after you decline `nums[index]`, which later indices are
  guaranteed to rebuild a list you already produced? — see mistake_journal
  2026-08-29.
- Combination Sum II: if declining skips every copy of a value, how is `[1,1,6]`
  still produced? — see mistake_journal 2026-08-29.
- Subsets II: the skip condition is `nums[index]==nums[index+1]`. Which pairs of
  elements can it ever compare, and what does that force about the input? — see
  mistake_journal 2026-08-29.
- Palindrome Partitioning: a node at index `i` — how many children does it have,
  and what distinguishes them? (OPEN — session ended here.)

- Rat in a Maze: your accept branch does `list.add(s)`. What does it assume is
  already true about `(curx, cury)`? — see mistake_journal 2026-08-29.
- Rat in a Maze: LC 40 wants accept first, this wants reject first. What single
  rule produces both? — see mistake_journal 2026-08-29.
- Rat in a Maze: what breaks if you delete the trailing `maze[curx][cury]=1`?
  Give the symptom. (OPEN — declined 2026-08-29.)
- Rat in a Maze: time and space, including the cost of `s+"D"`. (OPEN —
  declined 2026-08-29.)
- N-Queens: why can't one arithmetic expression identify both diagonals? — see
  [note](../notes/n-queens.md).
- N-Queens: `r-c` spans -(n-1)..n-1. What shift makes it a legal index, and how
  big is the array? (OPEN — session ended here 2026-08-29.)
- Palindrome Partitioning: at index `i` in a string of length `n`, what is the
  full set of first pieces? (OPEN — 2nd abandonment 2026-08-29.)

## 2026-08-30

- Why is the auxiliary space of a recursion that carries `res + c` down each
  level `O(n²)` rather than `O(n)`, and what single change makes it `O(n)`? —
  see mistake_journal 2026-08-30 (LC 17).
- What does the `'-'` mark on a grid cell mean during backtracking, and what
  follows from that about when it must be undone? — see mistake_journal
  2026-08-30 (LC 79).
- Given `boolean a = dfs(...); boolean b = dfs(...); return a || b;` — does the
  `||` prevent the second call from running? Why? — see mistake_journal
  2026-08-30 (LC 79).
- What property of the candidate values licenses pruning a backtracking branch
  at `sum >= target`, and what kind of input would invalidate that prune? — see
  mistake_journal 2026-08-30 (LC 216).

## 2026-08-31

- Your solver takes the first dictionary word that matches at position `i` and
  advances. Give an input where that returns the wrong answer, and say what
  line has to exist for it not to. — see mistake_journal 2026-08-31 (LC 139).
- A memo writes `true` under `start+"-"+i` and reads under `start+"-"+start`.
  Is that a correctness bug or a cost bug, and which results get cached? — see
  mistake_journal 2026-08-31 (LC 139).
- In Java, what does `mask & (1<<i) == 0` actually parse as, and what does
  `1 << (n+1)-1` evaluate to for n=3? — see mistake_journal 2026-08-31 (LC 46).
- N-Queens: two nested loops place one queen per row in the first legal column.
  Name the two things wrong with the returned `List<List<String>>`, given
  output `[["Q..."],["..Q."],["...."],[".Q.."]]` for n=4. — see mistake_journal
  2026-08-31 (LC 51).


- You defined "legal colour" as differing from every neighbour, then wrote
  `if(i != prvNodeColor)`. On `0-1, 1-2, 2-3, 3-0, 0-2`, which neighbour of
  vertex 3 does that line never look at? — see mistake_journal 2026-08-31
  (M-Coloring).
- A `for(kids) if(color[kids]==i) continue;` sits inside the colour loop.
  Which loop does `continue` advance, and what does the scan accomplish?
  — see mistake_journal 2026-08-31 (M-Coloring).
- `graphColoring` ends with `return dfs(graph,color,m,0,-1)`. Give a `V=3`
  input where that returns true and the answer is false. — see mistake_journal
  2026-08-31 (M-Coloring).
- M-Coloring: `m` colours, `V` vertices. How many colour assignments does the
  search tree hold, and what does each node pay on top? — see mistake_journal
  2026-08-31 (M-Coloring, complexity unreached).

## 2026-09-01

- `(r/3)*3` — why does this not simplify to `r`? Give its value at `r=7`.
  — see mistake_journal 2026-09-01 (Sudoku Solver).
- A 9x9 grid numbered row-major 0..80. Which number is cell `(0,4)`, and which
  cell comes after it? — see mistake_journal 2026-09-01 (Sudoku Solver).
- `isValid` returns true and has already written to the board. Name what breaks
  the first time someone calls it just to check. — see mistake_journal
  2026-09-01 (Sudoku Solver).
- XOR over an array is a per-bit count mod what? What replaces it when every
  element but one appears three times? — see mistake_journal 2026-09-01
  (Single Number II).
- Which two operator laws let `4^1^2^1^2` be regrouped as `4^(1^1)^(2^2)`, and
  why is `x^x=0` alone not enough? — see mistake_journal 2026-09-01
  (Single Number).

## 2026-09-02

- A set bit in `x^y` means exactly what about x and y at that position? Why
  does that let duplicate pairs land together and x,y land apart under any
  set bit? — see mistake_journal 2026-09-02 (Single Number III).
- `n & (n-1) == 0` checks for exactly one set bit. What signed int passes this
  check despite being negative, and why? — see mistake_journal 2026-09-02
  (Power of Two).

## 2026-09-03

- Single Number III: at the bit you pick from `x^y`, is it "uncertain" whether
  the other number has that bit — or do you know for certain? — see
  mistake_journal 2026-09-03 (LC 260, split-rule recurrence).
- Single Number III: pick a non-MSB set bit of `x^y` — does the split still
  separate x from y? Why? — see mistake_journal 2026-09-03 (LC 260, any-bit
  generality).
- Power of Two: in 32-bit two's complement, what value has only the sign bit
  (bit 31) set, and nothing else? (CLOSED 2026-09-04 via odometer analog: Integer.MIN_VALUE.)
- Course Schedule (Kahn's BFS): for edge `[a, b]` where b is a's
  prerequisite, whose indegree increments — a's or b's, and why? — see
  mistake_journal 2026-09-03 21:18 (Course Schedule). (CLOSED 2026-09-04: a's, cold.)

## 2026-09-04

- Power of Two: why does `Integer.MIN_VALUE - 1` roll around to `Integer.MAX_VALUE` in 32-bit signed two's complement, and why does `n & (n-1)` evaluate to 0 for it? Why does `n > 0` fix this? — see [note](../notes/power-of-two.md).
- Course Schedule (Kahn's BFS): why is an inner `int size = queue.size()` snapshot redundant when running Kahn's algorithm for cycle detection/topo-sort? — see [note](../notes/course-schedule.md).

## 2026-09-05

- Alien Dictionary: given two adjacent words in dictionary order, what's the one piece of order information you extract from them, and why don't you need to compare every pair of words? — see mistake_journal 2026-09-05 13:15.
- Alien Dictionary: `(char)cur+'a'` vs `(char)(cur+'a')` — which does Java actually evaluate, and why? — see mistake_journal 2026-09-05 13:35.
- Alien Dictionary: why must the shorter-word length check run after scanning for a differing character, not before? — see mistake_journal 2026-09-05 13:38.
- Number of Enclaves: why does marking `visited` at pop instead of push cause a cell to be enqueued more than once? — see mistake_journal 2026-09-05 13:55.

