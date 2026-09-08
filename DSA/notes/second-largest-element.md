---
type: note
problem: Second Largest Element in Array
topic: Arrays/Basics
updated: 2026-07-11
---

# Second Largest Element

## Intuition

Second largest **distinct** value, not second position — duplicates of the max
don't count. Single pass, two variables `largest` and `secondLargest`.

## Update Rule

For each `arr[i]`:
- if `arr[i] > largest`: `secondLargest = largest; largest = arr[i]`
- else if `arr[i] < largest && arr[i] > secondLargest`: `secondLargest = arr[i]`

The `arr[i] < largest` guard in the second branch is what makes duplicates of
`largest` safe — without it, an equal-to-largest value could wrongly leak into
`secondLargest`.

## Mistake Made

Guessed (wrong, before tracing) that a duplicate of the max would incorrectly
overwrite `secondLargest`. Tracing `[8,8,5,3]` step by step showed both
conditions evaluate false for the second `8`, so it's correctly skipped.
Lesson: trace before answering when unsure, don't guess on comparison-heavy edge
cases.

## Complexity

O(n) time, O(1) space.
