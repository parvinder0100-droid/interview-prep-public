---
type: flashcards
topic: recursion
updated: 2026-08-28
---

# Recursion / Backtracking Flashcards

Format: Q on one line, A (intuition/complexity only, never full code) below it.

Q: Backtracking result set needs a `HashSet` to remove duplicates. What does that tell you?
A: It is a branching bug until proven otherwise — the search reaches the same state by more than one path and pays exponentially for it. Delete the `Set` and find the redundant branch.

Q: Subsets vs Combination Sum — what is the difference in the branch set?
A: Subsets is take / not-take (each element used once). Combination Sum is take-stay / skip — recursing with the **same** index is what permits unlimited reuse. A third "take and move on" branch is redundant: it equals take-stay followed by skip.

Q: Time complexity of Subsets — why is O(2^n) wrong?
A: Each of the 2^n results is copied into the answer list at O(n). Total O(n·2^n). Standing checklist item on every enumeration problem: "what does recording one answer cost?"

Q: In Combination Sum, why is the recursion depth not O(target)?
A: Every take-step adds at least `m = min(candidates)`, so depth is `target/m` (plus n skip-steps). `candidates=[50]`, `target=100` has depth 2, not 100.

Q: Ordering of the base cases in a target-sum backtracking search?
A: Check `sum == target` **before** the index bound, or an exact hit landing at the end of the array is discarded.

Q: Input has duplicate values and the output must have no duplicate combinations. What is the branch rule?
A: Sort, then take = `index+1` as usual, but **decline = skip every copy** of that value. Taking a later equal value rebuilds the identical list. The skip is in the decline branch only, so a value can still appear twice in one answer.

Q: If declining skips every copy of a value, how can `[1,1,6]` still be an answer?
A: Because that path never declines. `index+1` in the take branch enforces use-once; the skip loop only runs after a decline. Duplicate values stay usable, duplicate paths do not.

Q: Why must the array be sorted for the adjacent-duplicate skip to work?
A: The test `nums[i]==nums[i+1]` only ever compares neighbours. Unsorted, equal values are not adjacent and the skip never fires. Sorting also gives each subset one canonical spelling, so `[1,2]` and `[2,1]` cannot both appear.

Q: Palindrome partitioning — does a cut require both sides to be palindromes?
A: No. Only the left piece is tested; the remainder is handed to the recursion, which partitions it further. `"aab"` cuts after `"a"` even though `"ab"` is not a palindrome.

Q: Which terminal check goes first — the goal check or the validity check?
A: Wrong question. Ask what the goal check *assumes*. Rat in a Maze: it assumes the cell is open and on the board, so validity goes first. Combination Sum II: `index >= n` is not a precondition of the sum, so `sum == target` goes first. Preconditions decide the order, not a fixed rule.

Q: N-Queens — you place row by row. Which attack lines still need checking?
A: Column and both diagonals. The row is free by construction: one queen per row is baked into the recursion shape.

Q: How do you name a diagonal with a single integer?
A: `r+c` is constant along `/`, `r-c` is constant along `\`. Two directions, two arrays — `r+c` is not constant down a `\` diagonal (`0,2,4,6` on n=4), so one operation cannot cover both.

Q: `r-c` as an array index — what goes wrong?
A: It spans `-(n-1)..n-1`, and a negative index throws `ArrayIndexOutOfBoundsException`. (Shift and array size: OPEN, 2026-08-29.)

Q: Grid backtracking where the output must be in lexicographic order — what controls the order?
A: The order of the recursive calls, nothing else. For `D/L/R/U` moves, call them in that order.

Q: You carry `res + c` (a String) down each level of a recursion of depth `n`. What is the auxiliary space?
A: `O(n²)`, not `O(n)`. Strings are immutable, so each frame allocates its own copy — one live path holds lengths `0,1,…,n` at once = `n(n+1)/2`. A `StringBuilder` with append + delete-last is one buffer: `O(n)`.

Q: Where does the `· n` in `O(4^n · n)` actually get paid?
A: At the leaf, on `list.add(sb.toString())` — the one copy you cannot avoid, because the buffer keeps mutating after you record.

Q: A recursion that records at its leaf — what is the standing test case before you submit?
A: The empty / zero-size input. It reaches the base case immediately and records a bogus answer (`[""]` on LC 17). Guard it in the caller: it is a precondition on the input, not a leaf of the search.

Q: Grid backtracking — does marking a cell mean "visited" or something else?
A: "On the current path." It is path state, so it is undone on the way out, exactly like `list.remove(list.size()-1)`. Leave it marked and a failed attempt poisons the board for every later start — `[["A","B"],["A","D"]]`, `"AAB"` flips true to false.

Q: `boolean a = f(); boolean b = g(); return a || b;` — what does the `||` short-circuit?
A: Nothing. Assignment already forced both calls. `||` can only skip operands it has not yet evaluated, so the short-circuit has to be in the call chain itself.

Q: How do you write a backtracking reject guard so it has no holes?
A: As the complement of the accept check placed directly above it, not as a list of failure cases you thought of. LC 216: accept is `cnt==k && sum==n`, so reject is `cnt==k || sum>=n` — writing `(cnt==k&&sum<n)||(cnt<k&&sum>=n)` misses `cnt==k && sum>n`.

Q: What licenses pruning a branch at `sum >= target` rather than `sum > target`?
A: All candidates are positive, so `sum` is monotone down a path — a prefix already at `target` with picks still owed can never come back. The prune is invalid the moment 0 or negative values are allowed.

Q: A choice at level `i` passes every legality check. Does that mean you take it and move on?
A: No — it means it is one child, not the answer. Legality licenses exploring a branch; only a return from below tells you it was right. If no line brings control back to level `i` after a dead end, there is no backtracking, only greed. Word Break: `"catsdog"` with `["cat","cats","dog"]` — "cat" is legal and fatal.

Q: What must a memo key be, exactly?
A: The state the function is parameterized by — nothing more. LC 139's `dfs(s,start,index)` always had `index==start`, so the key was one integer wearing a two-part disguise; `Boolean[n]` replaces the whole `HashMap<String,Boolean>` and the per-call string concat with it.

Q: You look up `key` at the top, then reassign `key` before `put(key,true)`. What breaks?
A: Nothing visible — the answer stays right. But every `true` lands under a key no lookup ever asks for, so only failures are cached and every success is recomputed. Cost bug, not correctness.

Q: In Java, does `mask & (1<<i) == 0` do what it reads like?
A: No. `==` binds tighter than `&`, so it parses as `mask & ((1<<i)==0)` — int & boolean, compile error. Same family: `1<<(n+1)-1` is `1<<n`, not `(1<<n)-1`. Parenthesize every bitwise sub-expression.

Q: Permutations via bitmask — what are the two undos?
A: `list.remove(list.size()-1)` and `mask ^= 1<<i`. Both, every time. Time `O(n!·n)` (n! leaves, `new ArrayList<>(list)` costs n at each), space `O(n)` auxiliary — `2^n` is the *subsets* count, not this.


Q: On a graph-colouring backtrack, what does "is colour `i` legal for `u`" read?
A: `color[v]` for **every** `v` in `graph[u]` — the whole adjacency row. Not the caller's colour, not the previously-coloured vertex. A parent-only check misses every already-coloured non-parent neighbour (`3` adjacent to both `0` and `2` is the minimal witness).

Q: Backtracking on a graph — where does the recursion start?
A: A driver loop over all `V` vertices, combining results. Recursing only into neighbours from vertex 0 is an *edge walk*, and it never reaches a component with no edge into it. Standing test: `V=3, single edge 1-2, m=1` -> false.

Q: A validity scan sits in a nested loop and uses `continue`. What breaks?
A: `continue` advances the loop it sits in — the inner one — so the scan computes and discards. Publish the result outward: a flag plus `break`, or a helper returning boolean. A loop body that writes to nothing outside itself does nothing.

Q: M-Coloring — time and space?
A: `O(m^V · V)` — `m` colour choices at each of `V` vertices, and each node pays `O(degree)` for the neighbour scan (summing to `O(V+E)` per level). Space `O(V)` for `color[]` plus `O(V)` recursion depth, on top of `O(V+E)` for the adjacency list.

Q: Sudoku — which 3x3 box does cell `(r,c)` belong to, and why do the `/3` and `*3` not cancel?
A: `box = (r/3)*3 + c/3`. Integer division truncates first, so `r/3` is the band index and `*3` re-expands it to that band's first row (`r=7` -> `2` -> `6`). It is row-major flattening of a 3x3 grid of boxes: `index = row*width + col`.

Q: Walking a 9x9 grid cell by cell with one flat counter — what's the stride, and what maps back?
A: `flat = r*9 + c`; back is `(flat/9, flat%9)`. Termination is `flat >= 81`, not `r>=9 && c>=9` — after `(8,8)` the next cell is `(9,0)`, where a row-and-column test never fires and the board access throws.

Q: A backtracking base case returns true without checking the board. Justify it.
A: The invariant — an illegal value is never left in place, because every placement was legality-checked and every failure undone. So "all cells filled" already implies "valid". A verification pass at the leaf is redundant work.

Q: Your `isValid` places the digit and sets the trackers, and `dfs` undoes them. What's wrong?
A: A query that mutates, with its inverse in a different function. The place/undo pair is invisible at both sites, and any later call that only wants to check corrupts state silently. Keep the predicate read-only; place, recurse and undo belong on three adjacent lines.

