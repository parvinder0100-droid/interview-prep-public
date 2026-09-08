---
type: note
problem: Combination Sum (LC 39)
topic: Recursion/Backtracking
date: 2026-08-28
---

# Combination Sum (LC 39)

## The defect

Three recursive branches were written where two suffice:

    A  skip nums[index] forever      dfs(sum,               index+1)
    B  take, stay (reuse allowed)    dfs(sum+nums[index],   index)
    C  take, move on                 dfs(sum+nums[index],   index+1)

**C is redundant**: every path through C is a B-step followed by an A-step.
`[2,3]`, target 5 reaches `[2,3]` twice — once as B-then-A, once as C-then-B.
A `HashSet` on the result was absorbing the duplicates.

## The rule worth keeping

A `Set` on the output of a backtracking search is a **branching bug** until
proven otherwise. Uniqueness should fall out of the shape of the search; if it
has to be filtered afterwards, the search is visiting states more than once and
paying exponentially for it.

## Second fix

`sum == target` must be checked **above** the `index == nums.length` bound, or
an exact hit landing at the end of the array is discarded.

## Complexity

Depth is bounded by `target/min(candidates)`, not `target` — each take-step adds
at least the smallest candidate. Plus `n` skip-steps. Time
`O(2^(target/m) · target/m)`, the trailing factor being the copy into `res`.
Auxiliary space `O(target/m + n)`.

## Also

`Set` has no `asList()` — `new ArrayList<>(set)`.
