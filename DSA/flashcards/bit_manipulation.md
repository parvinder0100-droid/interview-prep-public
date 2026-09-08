---
type: flashcards
topic: BitManipulation
updated: 2026-09-02
---

# Bit Manipulation — Flashcards

Q: Every element appears twice except one. Which three facts make XOR-everything work?
A: `x^x = 0`, `x^0 = x`, and commutativity + associativity. The third is the one that gets skipped: duplicates are not adjacent in the array, so the fold `((((4^1)^2)^1)^2)` may only be regrouped as `4^(1^1)^(2^2)` because operands can be moved and re-bracketed. `-` and `/` have neither law, which is why no equivalent trick exists for them.

Q: Why does XOR fail when every element but one appears three times?
A: XOR on a bit position is the count of 1s **mod 2**. Triples leave one copy: `[1,1,1,2]` -> `1^2 = 3`. Same framing gives the fix — count per bit and take mod 3.

Q: Single Number II with `O(1)` space — the algorithm, and why is a 32-slot array still `O(1)`?
A: For each of 32 bit positions count how many `nums[i]` have it set; `count % 3` is that bit of the answer; reassemble with `res |= 1<<i`. `O(32n) = O(n)` time. The array's size is fixed by the width of `int`, not by `n`, so the space is constant.

Q: Do you skip bit 31 when the values can be negative?
A: No — indices are `0..31`, all 32. In two's complement the sign bit is an ordinary column and obeys the same mod-3 rule; dropping it returns a wrong (non-negative) answer whenever the loner is negative.

Q: Java: why is `char c = '0' + val;` a compile error?
A: Arithmetic on `char` promotes to `int`, and `int` -> `char` is narrowing, so it needs `(char)('0'+val)`. Compound assignment (`c += val`) carries a hidden cast. Cleanest avoidance in grid/digit problems: loop over `char` directly and use `d-'0'` only where an index is required.

Q: Two elements appear once, rest appear twice (Single Number III). Why does any set bit of `x^y` correctly split the array?
A: A duplicate pair has identical bits everywhere, so at any bit it lands together in one group. `x` and `y` differ at every set bit of `x^y`, so at that bit they land in different groups. XOR each group to cancel its pairs and isolate its singleton — this works for *any* set bit of `x^y`, not a special one.

Q: `n & (n-1) == 0` checks "exactly one set bit" (Power of Two). What false positive does this miss?
A: `Integer.MIN_VALUE` (-2147483648) has exactly one set bit (the sign bit alone) and passes the check despite being negative. Guard with `n > 0` before applying the bit check, not just `n != 0`.
