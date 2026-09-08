---
type: flashcards
topic: arrays
updated: 2026-07-20
---

# Arrays Flashcards

Format: Q on one line, A (intuition/complexity only, never full code) below it.

Q: Rotate array O(1) space — what's the trick?
A: Reverse both chunks individually, then reverse the whole array (double
reversal cancels the internal flip, keeps just the chunk swap).

Q: Kadane's — how do you avoid losing the max on an all-negative array?
A: Record `max=max(max,sum)` every iteration, before the `if sum<0: sum=0`
reset — not just at reset time.

Q: Subarray sum problems with negative numbers allowed — sliding window or
prefix-sum+hashmap?
A: Prefix-sum+hashmap. Sliding window needs monotonic sum growth, breaks with
negatives.

Q: Next Permutation — 3 steps?
A: Find pivot (largest i, arr[i]<arr[i+1]) → find rightmost j>i with
arr[j]>arr[i] strictly → swap, then reverse suffix after i.

Q: Rotate Matrix 90° in-place — 2 steps?
A: Transpose (i!=j only, diagonal stays fixed) → reverse each row fully
(not just swap endpoints).

Q: Dutch National Flag (sort 0s/1s/2s) — why does mid advance on a 0-swap but
not a 2-swap?
A: 0-swap brings in a *known* value from the confirmed-1 zone (safe to
advance). 2-swap brings in an *unknown* value from unprocessed region (must
recheck it, don't advance).

Q: Standing checklist item for window/run-tracking loops (Max Consecutive
Ones and others) — what do you always check?
A: What happens to the last window when the loop ends without a reset
trigger — post-loop finalization, don't rely only on the reset branch.

Q: Rotate array — WHY does reverse-chunk1/reverse-chunk2/reverse-whole
actually rotate (not just the steps)?
A: Reversing each chunk first flips its internal order; reversing the whole
array afterward double-flips each chunk back to original order (cancels)
while swapping the two chunks' positions. Net effect: rotation. (3 reviews
in a row recalled the steps but not this — treat as the real pass/fail bar.)

Q: Print Subarray with Max Sum — why `start=tempStart` not `start=i` on a
new max?
A: `tempStart` is the current running (unreset-since-last-negative) window's
start — at the moment a new max is found, that running window IS the
winning one. `start=i` would wrongly report a length-1 subarray.

Q: Prefix-sum+hashmap, longest-subarray variant — after seeding `{0:-1}`, do
you ever add an extra `+1` to `i - map[sum-k]`?
A: No — the `-1` seed already produces the correct `i+1` length when needed
(`i - (-1) = i+1`). Adding another `+1` on top double-counts.
