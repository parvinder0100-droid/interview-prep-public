---
type: note
problem: Remove Duplicates from Sorted Array
topic: Arrays/Two Pointers
updated: 2026-07-11
---

# Remove Duplicates from Sorted Array

## Intuition

In-place, two pointer. `i` = last confirmed-unique position, `j` = scanner.
Compare `arr[j]` against `arr[i]` (last unique), **not** `arr[j+1]` (next
element) — comparing against next requires a special-case for the last array
element (never gets a "next" to compare against). Comparing against `arr[i]`
avoids that entirely; loop runs `j` fully from 1 to n-1.

## Algorithm

```java
int removeDuplicates(int[] arr) {
    int n = arr.length;
    if (n == 0) return 0;
    int i = 0;
    for (int j = 1; j < n; j++) {
        if (arr[i] != arr[j]) {
            i++;
            arr[i] = arr[j];
        }
    }
    return i + 1;
}
```

Copy, not swap — nothing at `arr[i+1]` needs preserving, fast pointer already
scanned past it.

## Mistake Made

First instinct was "compare current vs next," which works but forces a
last-element special case. Reframing to "compare current vs last-confirmed
unique" removes the special case — same pattern reused later for move-zeroes /
partition-style problems.

## Complexity

O(n) time, O(1) space.
