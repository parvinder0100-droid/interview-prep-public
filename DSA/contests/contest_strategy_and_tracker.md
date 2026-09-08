---
type: contest_strategy_and_tracker
target: 3/4 problems consistently (Rating 1850–2000+)
updated: 2026-09-04
contests_logged: 0
average_solves: 0.0
---

# LeetCode Contest Master Strategy & Progress Tracker

> **Core Objective**: Consistently solve **3 out of 4 problems** (Q1, Q2, Q3) in every LeetCode Weekly and Biweekly contest within the 90-minute window, with zero unnecessary penalty submissions.

---

## Part 1: The Constraint-to-Algorithm Decoder

Always check $N$ before picking an approach. $N$ dictates the required time complexity to stay under the $10^8$ operations/sec limit.

| Constraint ($N$) | Target Time Complexity | Mandatory Patterns to Consider |
| :--- | :--- | :--- |
| **$N \le 10$** | $O(N!)$ or $O(N^2 \cdot 2^N)$ | Full permutation search, brute-force recursion with backtracking. |
| **$N \le 20$** | $O(2^N)$ or $O(N \cdot 2^N)$ | **Bitmask DP**, Subset enumeration, Meet-in-the-middle ($2^{N/2}$). |
| **$N \le 100$** | $O(N^3)$ or $O(N^4)$ | 2D/3D Grid DP, Floyd-Warshall, Interval DP ($[i \dots j]$). |
| **$N \le 1,000$** | $O(N^2)$ | All-pairs comparison, 2D Matrix DP, Tree LCA via DFS, nested simulation. |
| **$N \le 10^5$** | $O(N \log N)$ or $O(N)$ | **Sorting**, **Binary Search on Answer**, **Two Pointers / Sliding Window**, **Monotonic Stack**, **Heaps**, **Prefix Arrays**, **BFS/DFS/Dijkstra**, **DSU**. |
| **$N \le 10^9$** | $O(\sqrt{N})$ or $O(\log N)$ or $O(1)$ | Math, Prime factorization ($O(\sqrt{N})$), Binary Exponentiation, Digit DP, Closed-form formulas. |

---

## Part 2: The 8 Essential Contest Patterns (Q1–Q3)

### 1. Dual Prefix + Suffix Arrays (The Exclusion Pattern)
* **Trigger**: *"Find the best score if you remove/skip at most one element"* or *"Evaluate array excluding index $i$"*.
* **Formula**: $\text{Combined} = f(\text{pref}[i-1], \text{suff}[i+1])$
* **Use Cases**: Range GCD/LCM, Product of array except self, Max subarray excluding one element.

### 2. Prefix Sum + HashMap (Subarray Counters)
* **Trigger**: *"Count subarrays with sum $= K$"*, *"Count balanced subarrays (0s and 1s, even/odd parity)"*.
* **Formula**: $P[j] - P[i-1] = K \implies P[i-1] = P[j] - K$.
* **Guard**: Always initialize `map.put(0, 1)` for subarrays starting at index 0.

### 3. At-Most-K Sliding Window Reduction
* **Trigger**: *"Count subarrays with **exactly** $K$ distinct elements / odd numbers / conditions"*.
* **Formula**: $\text{Count}(\text{Exact } K) = \text{Count}(\text{At Most } K) - \text{Count}(\text{At Most } K - 1)$.

### 4. Binary Search on the Answer (Predicate Search)
* **Trigger**: *"Minimize the maximum..."*, *"Maximize the minimum..."*, *"Find the smallest threshold $X$ to finish within $T$"*.
* **Technique**: Range $[L, R]$ is monotonic ($FFFFFTTTTT$). Implement an $O(N)$ greedy/counting verification function `canAchieve(mid)`.

### 5. Monotonic Stack & Contribution Technique
* **Trigger**: *"Sum of $\min(B)$ or $\max(B)$ over all subarrays"*, *"Find nearest greater/smaller element on left/right"*.
* **Technique**:
  * Use monotonic stack to find Previous Less Element (`PLE[i]`) and Next Less Element (`NLE[i]`) in $O(N)$.
  * Total Contribution of $A[i] = A[i] \times (i - \text{PLE}[i]) \times (\text{NLE}[i] - i)$.
  * Use strict `<` on one side and non-strict $\le$ on the other to prevent double-counting duplicates.

### 6. State-Augmented Dynamic Programming (The "+1 Power" Twist)
* **Trigger**: Standard DP with an extra capability: *"You can multiply at most 1 subarray"*, *"You can skip at most 1 item"*, *"You can make at most 1 swap"*.
* **Technique**: Add a small state dimension:
  * `dp[i][0]`: Best score up to $i$ **without** using the power.
  * `dp[i][1]`: Best score up to $i$ **having used** the power.

### 7. State-Expanded BFS / 0-1 BFS
* **Trigger**: Shortest path in a grid/graph with a limit: *"at most $K$ obstacles eliminated"* or *"at most $K$ consecutive steps in the same direction"*.
* **Technique**: Expand the visited state: `visited[row][col][remaining_k]`.

### 8. Greedy with Exchange Arguments
* **Trigger**: *"Find the optimal ordering of tasks/enemies to minimize total penalty/damage"*.
* **Technique**: Compare two adjacent items $A$ and $B$. Sort by the condition where processing $A$ before $B$ produces lower total cost than $B$ before $A$ (e.g. $t_A \cdot d_B < t_B \cdot d_A$).

---

## Part 3: The 5-Point Pre-Submission Checklist (0-WA Rule)

Before clicking **Submit**, check these 5 items to avoid the 5-minute penalty and debugging panic:

1. [ ] **Integer Overflow**: Will sum or product exceed $2 \cdot 10^9$? Cast intermediate operations explicitly: `(long) a * b`.
2. [ ] **Extreme $N$**: Does the logic hold for $N = 1$ and $N = 0$?
3. [ ] **Duplicates**: Does the code break if all elements are identical (e.g. `[2, 2, 2, 2]`)?
4. [ ] **All Negatives / Zeros**: Are variables initialized to `0` instead of `-INF` or `arr[0]`?
5. [ ] **Sign Bits**: Does `Integer.MIN_VALUE` ($-2^{31}$) cause false positives in bit tricks or `Math.abs()`?

---

## Part 4: The 90-Minute Contest Clock Protocol

```
00:00 ────────── 00:10 ──────────────── 00:30 ──────────────────────────────────────── 01:30
  │   Q1 (Easy)    │     Q2 (Medium)      │                   Q3 (Hard/Medium)            │
  │   Target: 8m   │     Target: 18m      │                   Target: 50m                 │
  │   Quick & Clean│     Verify Edges     │                   15m Paper Derivation        │
  └────────────────┴──────────────────────┴───────────────────────────────────────────┘
```

* **Minutes 0–10 (Q1)**: Simple, brute-force simulation is fine. Don't over-optimize.
* **Minutes 10–30 (Q2)**: Match to standard pattern. Test $N=1$ and edge cases before submitting.
* **Minutes 30–45 (Q3 Paper Analysis)**: **No typing**. Write constraints, test for monotonicity, define the DP state or greedy invariant.
* **Minutes 45–80 (Q3 Implementation)**: Code steadily with clear variable names.
* **Minutes 80–90**: Fix edge cases, or attempt Q4 if Q3 is already Accepted.

---

## Part 5: Contest Performance Log

Log every live or virtual contest here immediately after completion.

| # | Date | Contest Name | Solves | Total Time | Penalties | Q3 Topic / Pattern | Q3 Result | Stuck Point & Lessons Learned |
|---|---|---|:---:|:---:|:---:|---|:---:|---|
| *Ref* | 2026-08-29 | Biweekly 190 | 2/4 | 42m | 1 | Prefix/Suffix GCD | Failed | Missed prefix/suffix exclusion; struggled with number-theory reasoning. |
| 1 | | | /4 | | | | | |
| 2 | | | /4 | | | | | |
| 3 | | | /4 | | | | | |
| 4 | | | /4 | | | | | |
| 5 | | | /4 | | | | | |

---

## Part 6: Post-Contest Debrief Protocol

For any contest where Q3 was not solved:
1. **The 30-Minute Blind Retry**: Attempt Q3 again without looking at discussion, editorial, or tags.
2. **Classification**: Which of the 8 patterns did it belong to?
3. **Failure Diagnosis**:
   * Was it an **Identification Failure** (didn't realize it was binary search on answer)?
   * Was it a **Mathematical/Invariant Gap** (missed the formula or exchange argument)?
   * Was it an **Implementation/Time Failure** (ran out of time because Q1/Q2 took 45+ minutes)?
4. **Log Actionable Question**: Add 1 bare active recall question to `../recall/daily.md`.
