---
type: note
problem: Combination Sum II (LC 40)
updated: 2026-08-29
---

# Combination Sum II (LC 40)

Solved 2026-08-29, with-hints:6, Accepted. Each candidate used at most once,
input contains duplicates, output must contain no duplicate combination.

## The two defects — both were already in the tracker

1. **Base cases ordered wrong.** `if(index>=nums.length||sum>target) return;`
   sat above `if(sum==target)`. A call can be both out of candidates and
   holding a complete answer: `[1,2,2,2,5]`, target 5 loses `[5]`. The accept
   check must precede the reject check. This exact rule was written into
   `../flashcards/recursion.md` 16 hours earlier.
2. **`Set<List<Integer>> res`.** Same as LC 39 the previous day, one day after
   it became the top pitfall in `../patterns/Backtracking.md`.

## The rule that removes the Set

Declining a value means declining **every copy** of it at that depth.

If you decline `nums[index]` and later take an equal `nums[j]`, the list built
is identical value-for-value to the one where you took `nums[index]` instead,
and so is every continuation. That subtree is a rerun.

Sorting is what makes it cheap: equal values are adjacent, so "every copy" is
one contiguous run to jump.

    // take nums[index]
    list.add(nums[index]);
    dfs(..., sum + nums[index], index + 1);
    list.remove(list.size() - 1);

    // decline nums[index] — and every copy of it
    int j = index;
    while (j < nums.length && nums[j] == nums[index]) j++;
    dfs(..., sum, j);

## The confusion worth keeping

"We can only use each number once, so why skip adjacent equals?" — because the
two rules live in different branches. `index+1` in the **take** branch enforces
use-once. The skip fires **only on decline**. So duplicate *values* stay usable
(`[1,1,6]` is still produced by taking both `1`s) while duplicate *paths* are
cut. Verified by tracing that the `while` loop never executes on the path that
builds `[1,1,6]`.

## Complexity

`O(n · 2^n)` time — `O(2^n)` was the first answer, corrected on the copy-cost
nudge for the second day running. `O(n)` auxiliary space (depth + `list`).

See [[Backtracking]].
