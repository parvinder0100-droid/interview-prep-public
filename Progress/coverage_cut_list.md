---
type: plan
created: 2026-08-27
status: APPLIED 2026-08-27 — coverage queue, review schedule and cycle.md all updated
---

# Coverage Cut List — 197 remaining -> ~94 kept

Drafted 2026-08-27 after the audit showed actual pace at 5.3 problems/week
against 14.5 needed for `target_end: 2026-11-30`. `cycle.md` says a 3rd date
move means the goal is wrong, not the schedule — so this cuts the goal.

**Basis for keeping**: interview frequency at L4-equivalent loops, and whether
the topic's *pattern* is already covered by something else on the keep list.
Nothing here is cut for being hard.

    KEEP    ~94     finishes at 7.4/week — absorbs missed days at the logged 69% show-rate
    CUT    ~103     stays on the sheet, never scheduled

## Keep

    DP gaps                    12   highest interview weight on the sheet, all 12 unverified
    Recursion / Backtracking   15   of ~23 — subsets, permutations, combination sum,
                                    N-Queens, Sudoku, palindrome partition, word search,
                                    rat in maze. Cut the arithmetic-recursion warmups
    Arrays — Hard subtopic     13   untouched, and Hard-Arrays is the most common
                                    first-round shape (intervals, matrix, majority-II,
                                    4sum, subarray-sum families)
    Graph                      12   of ~36 — core algorithms already done, so keep only
                                    the classic problem set: word ladder, surrounded
                                    regions, course schedule I/II, alien dictionary,
                                    number of enclaves, shortest path variants
    Stack / Queue              10   of ~20 — monotonic-stack family (LC 84/907/739 done),
                                    keep: largest rectangle in matrix, sliding window
                                    max, LRU, LFU, min-stack variants, celebrity
    Strings                     6   of 12 — anagrams, roman/integer, longest palindrome,
                                    KMP, string-to-integer, compare version
    Sliding Window              6   remainder — all of it, small and high weight
    Heaps                       6   of 12 — k-th largest variants, merge k, median stream
                                    (done), top-k, task scheduler (done), hand of straights
    Bit Manipulation            5   of 17 — single number I/II/III, count set bits, power
                                    of two, subsets-via-bitmask. Cut the rest
    Trees                       3   the 3 known gaps
    Greedy                      3   remainder, nearly complete already
    Sorting                     2   merge sort + quick sort only (asked as concepts)
    Tries                       1   Maximum XOR With an Element From Array
                               ---
                                94

## Cut

    Basics                     31   lowest weight on the sheet, and 2 years of prior
                                    coverage. Never asked at this level
    Graph remainder            24   core algorithms are covered; the rest are variants
                                    of problems already on the keep list
    Recursion warmups           8   arithmetic/print-pattern recursion — subsumed by the
                                    backtracking problems kept
    Final section              15   Segment Tree / Fenwick / advanced Union-Find. Real
                                    topics, wrong loop — these show up in competitive
                                    programming, not standard SDE rounds
    Bit Manipulation rest      12   XOR-trick problems beyond the 5 kept are the same
                                    trick repeated
    Strings rest                6
    Heaps rest                  6
    Stack/Queue rest           10
    Arrays remainder            0   (Hard subtopic is the remainder — all kept)
    Sorting rest                5
    Re-verification backlog   161   Binary Search / LinkedList / BST / Trees / DP /
                                    Tries — already cut 2026-08-11, restated here so it
                                    is not silently re-added
                              ----
                             ~103 (+161 backlog already cut)

## What this changes

    before   197 remaining / 13.6 weeks = 14.5/week   (actual: 5.3)
    after     94 remaining / 13.6 weeks =  7.4/week

At 4 sessions/week x 2h x 3.5 problems = 14/week, the kept scope finishes
around **mid-October**, leaving ~6 weeks for the four zero tracks
(SystemDesign, Behavioral, LLD, Java) before 11-30 — which is the actual
reason to cut, since a target loop is 2 DSA + 1 system design + behavioral and
two of those three tracks have never been opened.

## Review queue, same decision

77 items, frozen 7 sessions, no weekend batch since 08-15. Keep only what has
failed at least once — the 3 `[leech]` items and the `[derive]`-tagged
problems whose *why* was never spoken. Drop the rest from `review_schedule.md`
rather than carrying a backlog that is never scheduled.

    keep    48 — 3 [leech] + 42 [derive] + 3 future-dated
    drop    35 — archived in review_schedule.md, not deleted

**Correction on application (2026-08-27)**: the estimate above said ~12
`[derive]` items. Actual count is 42 — the tag is applied far more widely than
assumed, so the backlog went 77 -> 48, not 77 -> 15. Kept all of them rather
than tightening the filter arbitrarily: 48 clears in 2 weekend batches at the
12/session cap, and they are precisely the items whose *why* was never spoken.
