---
type: note
problem: Move Zeroes to End
topic: Arrays/Two Pointers
updated: 2026-07-11
---

# Move Zeroes to End

## Intuition

Two pointer, but plain overwrite (like remove-duplicates) leaves trailing
garbage instead of zeroes — must either two-pass (copy non-zeroes forward, then
zero out the rest) or one-pass with **swap** instead of overwrite, since
`arr[i]` is guaranteed 0 at swap time.

## Algorithm (one-pass, swap)

```java
void moveZeroes(int[] arr) {
    int n = arr.length;
    int i = 0;
    for (int j = 0; j < n; j++) {
        if (arr[j] != 0) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
        }
    }
}
```

## Mistake Made

Initial approach was two-pass (copy forward + separate zero-out pass) — correct,
but didn't spot it until asked to trace what plain overwrite alone leaves
behind. One-pass swap version is the interview follow-up ("can you do it in one
pass?").

## Complexity

O(n) time, O(1) space (one-pass swap version).
