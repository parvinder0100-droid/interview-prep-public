---
type: pattern
name: Bit Counting mod k
status: in-use
created: 2026-09-01
---

# Bit Counting mod k

## When This Pattern Applies

Every element of an array repeats exactly `k` times except one (or a few), and
the problem demands `O(n)` time with `O(1)` extra space — so no hash map, and no
sort.

## Core Idea

Look at one bit position at a time. Across the whole array, a value repeating
`k` times contributes `k` (or `0`) to that column's count of 1s. Therefore

    count_of_ones_at_bit_i  %  k

is exactly the loner's bit at position `i`. Reassemble with `res |= 1<<i`.

`k = 2` is the special case where the mod is free: XOR **is** a per-bit count
mod 2. That is the whole reason the XOR trick works, and the reason it stops
working the moment `k` is 3.

## Problems Using This Pattern

- Single Number (LC 136) — `k=2`, so plain XOR. Accepted 2026-09-01, cold.
- Single Number II (LC 137) — `k=3`, explicit `int[32]` counts. Accepted
  2026-09-01. See [note](../notes/single-number-ii.md).
- Single Number III (LC 260) — posed 2026-09-01, not started.

## Common Pitfalls

- **Writing `%2` when `%3` was derived.** Happened on LC 137 within minutes of
  deriving mod 3 by hand — the neighbouring problem's rule overwrote the one
  just spoken.
- **31 slots instead of 32.** Indices run `0..31`. The sign bit is not special:
  in two's complement it obeys the same mod rule, and skipping it returns a
  wrong answer whenever the loner is negative.
- **Claiming this is not `O(1)` space** — or failing to justify why it is. The
  array's size is fixed by the width of `int`, not by `n`.
- Reassembly is `1<<i`, not `i<<1`.

## Why XOR may be reordered at all

`x^x=0` and `x^0=x` only help if the duplicates can be brought together;
duplicates are generally not adjacent. Commutativity and associativity supply
that licence. Any fold-the-whole-array trick needs both laws stated, not just
the cancellation fact.
