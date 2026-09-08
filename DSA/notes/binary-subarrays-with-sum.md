---
type: note
problem: Binary Subarrays With Sum (LC 930)
topic: SlidingWindow / At-most-K
link: https://leetcode.com/problems/binary-subarrays-with-sum/
created: 2026-08-25
---

# Binary Subarrays With Sum (LC 930)

Transfer landed cold, twice: `exactly(goal) = atMost(goal) - atMost(goal-1)`
came out unprompted on 2026-08-23 and again on re-derivation 2026-08-25 with
two days of decay in between. That part is solid — see [[AtMostKCounting]].

## The bug: shrink guard `i<j`

```java
while (i < j && sum > goal) { sum -= nums[i]; i++; }   // wrong
while (i <= j && sum > goal) { sum -= nums[i]; i++; }  // right
```

`i<j` stops the shrink with one element still in the window. So a window that
must empty can't. Two cases it breaks, both reachable in this exact problem:

- `nums=[1], goal=0` — `sum=1 > 0`, but `i==j` so the loop never runs. `cnt +=
  j-i+1 = 1`, counting a sum-1 subarray as "at most 0".
- **Every `goal=0` input**, because it calls `atMost(-1)`. No budget can satisfy
  `sum > -1`, so the window must empty on every index.

With `i<=j`, `i` walks to `j+1`, `cnt += j-i+1` evaluates to 0, and `atMost(-1)`
returns 0 with no special-case branch. The guard is the short-circuit — an
explicit `if (goal < 0) return 0;` is belt-and-braces, not the fix.

The invariant the guard has to preserve: **on exit, `[i..j]` is the longest
suffix ending at `j` whose sum is within budget — possibly empty.** Drop
"possibly empty" and `i<j` looks correct.

## Verified

    [1,0,1,0,1], goal=2  ->  atMost(2)=14, atMost(1)=10, ans 4
    [0,0,0],     goal=0  ->  atMost(0)=6,  atMost(-1)=0,  ans 6
    [1],         goal=0  ->  0

## Open — carry into review #1

Complexity, edge case, and the invariant were **never stated**; the fix was
applied silently after one question. Review opens on the *why*, not the code:
state the exit invariant, then O(n) time / O(1) space with the justification
(each pointer advances at most n across both `atMost` calls), then name an edge
case unprompted. Code is already known-correct — re-running it proves nothing.
