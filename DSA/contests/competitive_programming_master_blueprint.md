---
type: master_blueprint
title: Mastering Competitive Programming & Technical Interviews
target: Consistently Solve 3-4 Contest Problems & Pass FAANG Loops
updated: 2026-09-04
---

# Mastering Competitive Programming & Technical Interviews
## The Complete Algorithmic Blueprint to Consistently Solve 3–4 LeetCode Contest Problems and Pass Top-Tier FAANG Loops

---

## 1. Statistical & Contest Landscape Analysis

### Empirical Contest Data and Difficulty Distribution
An empirical evaluation of LeetCode Weekly and Biweekly contests reveals an engineered partition across the four-problem contest architecture. Each problem slot maps to a targeted difficulty band calibrated against global contestant performance.

| Contest Problem Slot | Empirical Elo Rating Range | Platform Difficulty Tier | Primary Algorithmic Paradigms | Target Execution Time |
| :--- | :---: | :---: | :--- | :---: |
| **Q1** | **1100 – 1350** | Easy | Direct simulation, linear array scanning, basic string formatting, brute force within tiny bounds ($N \le 100$) | 2 – 5 minutes |
| **Q2** | **1400 – 1750** | Medium (Lower Tier) | Hash maps, sliding windows, two pointers, prefix sums, sorting with greedy element selection, basic BFS/DFS | 8 – 15 minutes |
| **Q3** | **1700 – 2100** | Medium (Upper) / Hard | Binary search on the answer, monotonic stacks and deques, 1D/2D dynamic programming, state-augmented graphs, tree traversals | 20 – 35 minutes |
| **Q4** | **2100 – 2800+** | Hard | Digit DP, bitmask DP over submasks, interval DP with optimizations, tree rerooting, advanced segment trees, flow networks | 30 – 50 minutes |

Problem ratings reflect the skill level at which a competitor maintains an equilibrium win rate against the problem, defined as a **50% probability of solving it within the contest window** under standard conditions. 
* The competitive rating threshold for the **Knight badge** sits at approximately **1850** (representing the top 20–25% of active, repeat participants with ratings $\ge 1600$).
* The **Guardian badge** demands a rating exceeding approximately **2200** (the top 5% of active participants).

---

### Mathematical Rating Architecture: Elo, Bradley-Terry, and Rank Equilibrium

The rating updates applied to contest participants derive from the **Bradley-Terry preference model**, adapted for multi-contestant tournaments using formulation techniques analogous to the Codeforces rating system.

In a contest containing $M$ participants, every pair of participants $(i, j)$ is modeled as a latent Bernoulli comparison. Given prior ratings $R_i$ and $R_j$, the logistic probability that participant $j$ places ahead of participant $i$ is formulated as:

$$P(j \succ i) = rac{1}{1 + 10^{(R_i - R_j) / 400}}$$

Under this formulation, the expected rank $\mathbb{E}[	ext{Rank}_i]$ of participant $i$ corresponds to the sum of these pairwise probabilities over all other competitors in the field:

$$\mathbb{E}[	ext{Rank}_i] = 1 + \sum_{j 
e i} P(j \succ i) = 1 + \sum_{j 
e i} rac{1}{1 + 10^{(R_i - R_j) / 400}}$$

To determine the performance rating $R_{	ext{perf}}$ achieved by participant $i$ during a contest, the scoring engine solves for the root of the rank-equilibrium function using monotonic binary search:

$$\mathbb{E}[	ext{Rank}(R_{	ext{perf}})] = 	ext{Rank}_{	ext{actual}}$$

Once $R_{	ext{perf}}$ is isolated, the participant's new rating $R_{	ext{new}}$ is updated using an inertia dampening factor $f(K)$, where $K$ denotes the participant's historical contest participation count:

$$R_{	ext{new}} = R_{	ext{old}} + f(K) \cdot (R_{	ext{perf}} - R_{	ext{old}})$$

The inertia dampener initializes at $f(1) = 0.5$ for new entrants and converges monotonically toward an asymptotic floor of $f(K) 	o rac{2}{9} pprox 0.222$ as $K 	o \infty$. This structural dampening prevents erratic shifts caused by transient variance while reflecting sustained performance trends.

---

### The Q3 Gatekeeper Phenomenon: Cognitive, Structural, and Complexity Plateaus

Statistical analysis of contest standings indicates that the majority of active candidates **plateau between ratings of 1500 and 1650**, reliably solving Q1 and Q2 but failing to cross the Q3 threshold. This stagnation stems from qualitative shifts in problem design rather than incremental increases in code length:

1. **Imperative vs. Non-Constructive Predicates**: Q1 and Q2 problems are predominantly imperative: the prompt specifies a concrete procedure, and the task reduces to syntax translation. In contrast, Q3 introduces non-constructive predicates: the problem specifies an optimization objective or existential condition without delineating the algorithmic path. Brute-force simulations fail with Time Limit Exceeded ($O(N^2)$ vs. required $O(N)$ or $O(N \log N)$).
2. **Higher-Order Invariants**: Q3 problems frequently enforce monotonicity invariants that require structural abstractions, such as binary search on the answer space, monotonic stacks, and multi-variable dynamic programming. Bridging this gap requires recognizing problem triggers, isolating mathematical invariants, and selecting optimal algorithms directly from input constraints.

---

## 2. The Exhaustive Pattern Taxonomy

---

### Pattern 1: Range Processing
**Prefix Sums, Dual Prefix-Suffix Arrays, and Difference Arrays**

#### Triggers & Constraints
* **Triggers**: Queries over intervals $[L, R]$, requirements to evaluate properties of an array while excluding a single element $i$, or demands to apply bulk additive updates across arbitrary ranges $[L, R]$ prior to an evaluation phase.
* **Constraints**: $N \le 10^5$, $Q \le 10^5 \implies O(N + Q)$ overall runtime with $O(N)$ auxiliary space.

#### Mathematical Invariants
A prefix sum array $P$ is initialized with $P[0] = 0$ such that $P[k] = \sum_{j=0}^{k-1} A[j]$ for $k \ge 1$. For any range query spanning $[L, R]$:
$$\sum_{j=L}^{R} A[j] = P[R + 1] - P[L]$$

For operations requiring exclusion of element $i$ across an associative binary operator $\oplus$:
$$	ext{Result}[i] = 	ext{Prefix}[i - 1] \oplus 	ext{Suffix}[i + 1]$$

A difference array $D$ models changes between adjacent terms ($D[i] = A[i] - A[i-1]$). Adding an offset $V$ across range $[L, R]$ updates exactly two boundary points:
$$D[L] \leftarrow D[L] + V, \quad D[R + 1] \leftarrow D[R + 1] - V$$
The final state is reconstructed by computing the prefix sum of $D$:
$$A[k] = \sum_{j=0}^{k} D[j]$$

#### Primary Failure Modes
* 32-bit integer overflow during prefix accumulation ($10^5 	imes 10^9 = 10^{14} > 2^{31} - 1$).
* Index out-of-bounds on $D[R + 1]$ at edge $R = N - 1$ without an allocated buffer of size $N + 1$.
* Attempting prefix division when zero elements exist in the input domain.

#### Production Implementations

**Java**:
```java
public class RangeProcessing {
    public static long[] applyRangeUpdates(int n, int[][] updates) {
        long[] diff = new long[n + 1];
        for (int[] u : updates) {
            int left = u[0], right = u[1], val = u[2];
            diff[left] += val;
            if (right + 1 < n) {
                diff[right + 1] -= val;
            }
        }
        long[] result = new long[n];
        long running = 0;
        for (int i = 0; i < n; i++) {
            running += diff[i];
            result[i] = running;
        }
        return result;
    }

    public static long[] productExceptSelf(int[] nums) {
        int n = nums.length;
        long[] result = new long[n];
        result[0] = 1;
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }
        long suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= suffix;
            suffix *= nums[i];
        }
        return result;
    }
}
```

**Python**:
```python
def apply_range_updates(n: int, updates: list[list[int]]) -> list[int]:
    diff = [0] * (n + 1)
    for left, right, val in updates:
        diff[left] += val
        diff[right + 1] -= val
    
    result = [0] * n
    running = 0
    for i in range(n):
        running += diff[i]
        result[i] = running
    return result

def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]
    
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result
```

---

### Pattern 2: Two Pointers & Sliding Window
**Variable-Size Monotonic Window and Exact-to-At-Most-K Transformation**

#### Triggers & Constraints
* **Triggers**: Longest or shortest contiguous subarray satisfying an inequality constraint, or exact count of subarrays containing a specific quantity $K$ of distinct elements.
* **Constraints**: $N \le 2 	imes 10^5$, non-negative entries $\implies O(N)$ amortized runtime, $O(\min(N, \Sigma))$ space.

#### Mathematical Invariants
Relies on range monotonicity: if subsegment $[L_1, R]$ violates the predicate, then for all $L_0 < L_1$, $[L_0, R]$ must also violate it. 
While "exactly $K$" is non-monotonic, "at most $K$" is strictly monotonic:
$$	ext{Count}(	ext{Exact}(K)) = 	ext{Count}(	ext{AtMost}(K)) - 	ext{Count}(	ext{AtMost}(K - 1))$$

#### Primary Failure Modes
* Passing $K = 0$ into an `AtMost(K - 1)` query without immediately returning 0.
* Negative values in input (destroys running sum monotonicity $\implies$ requires prefix sum + hashmap).
* Off-by-one errors when advancing `left` past `right`.

#### Production Implementations

**Java**:
```java
public class SlidingWindow {
    public static int subarraysWithExactlyKDistinct(int[] nums, int k) {
        return atMostK(nums, k) - atMostK(nums, k - 1);
    }

    private static int atMostK(int[] nums, int k) {
        if (k < 0) return 0;
        int n = nums.length;
        int[] freq = new int[n + 1];
        int left = 0, distinct = 0, count = 0;

        for (int right = 0; right < n; right++) {
            if (freq[nums[right]]++ == 0) {
                distinct++;
            }
            while (distinct > k) {
                if (--freq[nums[left]] == 0) {
                    distinct--;
                }
                left++;
            }
            count += (right - left + 1);
        }
        return count;
    }
}
```

**Python**:
```python
def subarrays_with_exact_k_distinct(nums: list[int], k: int) -> int:
    def at_most(limit: int) -> int:
        if limit < 0:
            return 0
        freq = {}
        left = 0
        count = 0
        for right, val in enumerate(nums):
            freq[val] = freq.get(val, 0) + 1
            while len(freq) > limit:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            count += (right - left + 1)
        return count

    return at_most(k) - at_most(k - 1)
```

---

### Pattern 3: Binary Search
**Classic Bounds and Binary Search on the Answer Space**

#### Triggers & Constraints
* **Triggers**: Sorted inputs, or optimization objectives phrased as "minimize the maximum value," "maximize the minimum capacity," or "find the smallest threshold where feasibility holds."
* **Constraints**: Search domain up to $hi \le 10^{18}$, predicate $P(x)$ in $O(N) \implies O(N \log(hi - lo))$ total runtime.

#### Mathematical Invariants
Requires a monotonic predicate $P(x): \mathcal{S} 	o \{0, 1\}$ where $P(x_1) \le P(x_2)$ for all $x_1 \le x_2$. The search window $[lo, hi]$ brackets the boundary:
$$P(x) = 0 \quad orall x < 	ext{boundary}, \qquad P(x) = 1 \quad orall x \ge 	ext{boundary}$$
Midpoint calculation must avoid overflow: $mid = lo + \lfloor(hi - lo) / 2floor$.

#### Primary Failure Modes
* 32-bit signed overflow on `(low + high) / 2`.
* Infinite loop when assigning `low = mid` without integer ceiling division.
* Under-bounding `high` lower than the actual achievable answer.

#### Production Implementations

**Java**:
```java
public class BinarySearch {
    public static long binarySearchFirstTrue(long low, long high, java.util.function.LongPredicate predicate) {
        long ans = high + 1;
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (predicate.test(mid)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
}
```

**Python**:
```python
from typing import Callable

def binary_search_first_true(low: int, high: int, predicate: Callable[[int], bool]) -> int:
    ans = high + 1
    while low <= high:
        mid = low + (high - low) // 2
        if predicate(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
```

---

### Pattern 4: Monotonic Structures
**Monotonic Stack, Monotonic Deque, and Subarray Contribution**

#### Triggers & Constraints
* **Triggers**: Next Greater Element ($NGE$), Next Smaller Element ($NSE$), Previous Greater Element ($PGE$), Previous Smaller Element ($PSE$), sliding window extrema over window $K$, sum of subarray minimums or maximums.
* **Constraints**: $N \le 10^5 \implies O(N)$ amortized runtime, $O(N)$ space.

#### Mathematical Invariants
The contribution principle states that element $A[i]$ acts as the minimum across:
$$	ext{Count}(i) = (i - L[i]) 	imes (R[i] - i)$$
where $L[i]$ is the previous smaller element index and $R[i]$ is the next smaller element index. Total sum:
$$	ext{Sum} = \sum_{i=0}^{N-1} A[i] 	imes (i - L[i]) 	imes (R[i] - i)$$
**Tie-breaking rule**: To prevent double-counting duplicate values across overlapping subsegments, define $PSE$ with a strict inequality ($<$) and $NSE$ with a non-strict inequality ($\le$).

#### Primary Failure Modes
* Using non-strict inequalities on both sides (double-counts duplicate elements).
* Empty stack exceptions when sentinels ($L[i] = -1$, $R[i] = N$) are omitted.
* Expired front elements not purged from sliding window deques ($idx \le right - K$).

#### Production Implementations

**Java**:
```java
import java.util.ArrayDeque;
import java.util.Deque;

public class MonotonicStructures {
    public static int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        long MOD = 1_000_000_007;
        int[] left = new int[n];
        int[] right = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            left[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }

        stack.clear();

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                stack.pop();
            }
            right[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }

        long totalSum = 0;
        for (int i = 0; i < n; i++) {
            long count = (long) (i - left[i]) * (right[i] - i) % MOD;
            totalSum = (totalSum + arr[i] * count) % MOD;
        }
        return (int) totalSum;
    }
}
```

**Python**:
```python
def sum_subarray_mins(arr: list[int]) -> int:
    MOD = 1_000_000_007
    n = len(arr)
    left = [-1] * n
    right = [n] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    stack.clear()

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    total_sum = 0
    for i in range(n):
        count = (i - left[i]) * (right[i] - i)
        total_sum = (total_sum + arr[i] * count) % MOD

    return total_sum
```

---

### Pattern 5: Dynamic Programming
**Linear, State-Augmented, Knapsack, Interval & Knuth's, Bitmask, Digit, and Tree DP**

#### 1. 1D/2D Linear Formulations
Optimal substructure at index $i$ depends strictly on evaluations of states $k < i$ (LCS, Edit Distance, LIS).

#### 2. State-Augmented Dynamic Programming
When historical context violates the Markov property (e.g. cooldowns, transaction limits, at most 1 power/skip), expand the state space to $DP[i][k][flag]$ to maintain subproblem independence.

#### 3. Knapsack Variants
* **0/1 Knapsack**: Loop capacity backward ($W 	o w_i$) to prevent item reuse in 1D array.
* **Unbounded Knapsack**: Loop capacity forward ($w_i 	o W$) to allow multiple selections.

#### 4. Interval DP & Knuth's Optimization
Standard interval DP evaluates ranges $[i, j]$ by length:
$$DP[i][j] = \min_{i \le k < j} ig(DP[i][k] + DP[k+1][j]ig) + C(i, j) \quad [O(N^3)]$$
If cost $C(i, j)$ satisfies the Quadrangle Inequality ($C(a, c) + C(b, d) \le C(a, d) + C(b, c)$ for $a \le b \le c \le d$), then optimal split points satisfy:
$$opt[i][j-1] \le opt[i][j] \le opt[i+1][j]$$
Restricting $k$ to $[opt[i][j-1], opt[i+1][j]]$ telescopes evaluations, reducing runtime to **$O(N^2)$**.

#### 5. Bitmask DP
For small element sets ($N \le 20$), encode configuration as an integer bitmask $mask \in [0, 2^N - 1]$. Evaluates in $O(2^N \cdot N^2)$.

#### 6. Digit DP
Counts integers in range $[A, B]$ matching digit criteria via memoized search over tuples: `(idx, last_digit, is_tight, is_leading_zero)`.

#### 7. Tree DP & Rerooting
Calculates tree aggregations in $O(N)$ instead of $O(N^2)$. First DFS computes subtree contributions; second DFS dynamically shifts root identity down edges in $O(1)$.

#### Production Implementations (Digit DP Example)

**Java**:
```java
import java.util.Arrays;

public class DynamicProgramming {
    private static String numStr;
    private static int[][][] memoDigit;

    public static int countValidIntegers(String nVal) {
        numStr = nVal;
        int len = nVal.length();
        memoDigit = new int[len][11][2];
        for (int[][] mat : memoDigit) {
            for (int[] row : mat) Arrays.fill(row, -1);
        }
        return solveDigit(0, 10, 1, 1);
    }

    private static int solveDigit(int idx, int lastDigit, int isTight, int isLeadingZero) {
        if (idx == numStr.length()) {
            return isLeadingZero == 1 ? 0 : 1;
        }
        if (isLeadingZero == 0 && memoDigit[idx][lastDigit][isTight] != -1) {
            return memoDigit[idx][lastDigit][isTight];
        }

        int limit = (isTight == 1) ? (numStr.charAt(idx) - '0') : 9;
        int totalWays = 0;

        for (int digit = 0; digit <= limit; digit++) {
            if (isLeadingZero == 0 && digit == lastDigit) continue;

            int nextTight = (isTight == 1 && digit == limit) ? 1 : 0;
            int nextLeading = (isLeadingZero == 1 && digit == 0) ? 1 : 0;
            int nextDigitStored = nextLeading == 1 ? 10 : digit;

            totalWays += solveDigit(idx + 1, nextDigitStored, nextTight, nextLeading);
        }

        if (isLeadingZero == 0) {
            memoDigit[idx][lastDigit][isTight] = totalWays;
        }
        return totalWays;
    }
}
```

**Python**:
```python
class DigitDP:
    def count_valid_integers(self, n_str: str) -> int:
        memo = {}

        def dfs(idx: int, last_digit: int, is_tight: bool, is_leading: bool) -> int:
            if idx == len(n_str):
                return 0 if is_leading else 1
            
            state = (idx, last_digit, is_tight, is_leading)
            if state in memo:
                return memo[state]

            limit = int(n_str[idx]) if is_tight else 9
            total = 0

            for digit in range(limit + 1):
                if not is_leading and digit == last_digit:
                    continue
                next_tight = is_tight and (digit == limit)
                next_leading = is_leading and (digit == 0)
                next_digit = 10 if next_leading else digit
                total += dfs(idx + 1, next_digit, next_tight, next_leading)

            memo[state] = total
            return total

        return dfs(0, 10, True, True)
```

---

### Pattern 6: Graph Algorithms
**Multi-Source BFS, State-Expanded BFS, 0-1 BFS, Dijkstra, Kahn's Algorithm, Cycle Detection, and DSU**

#### Core Invariants
* **Multi-Source BFS**: Initialize queue with all source nodes at distance 0 (e.g. distance to nearest water cell).
* **State-Expanded BFS**: Expand visited state to `visited[node][remaining_power]` when traversing constraints.
* **0-1 BFS**: Edge weights restricted to $\{0, 1\}$. Push weight-0 edges to queue front, weight-1 edges to back. Achieves $O(V + E)$ without Dijkstra's $O((V + E) \log V)$ overhead.
* **Dijkstra Pruning**: Skip stale priority queue entries (`if (d > dist[u]) continue;`).
* **Kahn's Topological Sort**: Queue nodes with in-degree 0. Decrement dependent neighbors. If processed count $< V$, a cycle exists.
* **DSU with Path Compression & Union by Rank/Size**: Achieves $O(M \cdot lpha(N)) pprox O(1)$ per operation.

#### Production Implementations

**Java**:
```java
import java.util.*;

public class GraphAlgorithms {
    public static int zeroOneBFS(int n, List<int[]>[] adj, int src, int target) {
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        Deque<Integer> deque = new ArrayDeque<>();

        dist[src] = 0;
        deque.addFirst(src);

        while (!deque.isEmpty()) {
            int u = deque.pollFirst();
            if (u == target) return dist[u];

            for (int[] edge : adj[u]) {
                int v = edge[0], weight = edge[1];
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    if (weight == 0) {
                        deque.addFirst(v);
                    } else {
                        deque.addLast(v);
                    }
                }
            }
        }
        return dist[target] == Integer.MAX_VALUE ? -1 : dist[target];
    }

    public static class DisjointSetUnion {
        private final int[] parent;
        private final int[] size;

        public DisjointSetUnion(int n) {
            parent = new int[n];
            size = new int[n];
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public int find(int i) {
            if (parent[i] == i) return i;
            return parent[i] = find(parent[i]);
        }

        public boolean union(int i, int j) {
            int rootI = find(i);
            int rootJ = find(j);
            if (rootI == rootJ) return false;

            if (size[rootI] < size[rootJ]) {
                parent[rootI] = rootJ;
                size[rootJ] += size[rootI];
            } else {
                parent[rootJ] = rootI;
                size[rootI] += size[rootJ];
            }
            return true;
        }
    }
}
```

**Python**:
```python
from collections import deque

def zero_one_bfs(n: int, adj: list[list[tuple[int, int]]], src: int, target: int) -> int:
    dist = [float('inf')] * n
    dist[src] = 0
    dq = deque([src])

    while dq:
        u = dq.popleft()
        if u == target:
            return int(dist[u])

        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                if weight == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

    return -1 if dist[target] == float('inf') else int(dist[target])

class DisjointSetUnion:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i: int) -> int:
        path = []
        while self.parent[i] != i:
            path.append(i)
            i = self.parent[i]
        for node in path:
            self.parent[node] = i
        return i

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False
        if self.size[root_i] < self.size[root_j]:
            root_i, root_j = root_j, root_i
        self.parent[root_j] = root_i
        self.size[root_i] += self.size[root_j]
        return True
```

---

### Pattern 7: Greedy Strategies
**Exchange Arguments, Interval Scheduling, and Priority-Queue Simulation**

#### Core Invariants
* **Exchange Argument**: Prove optimality by demonstrating that swapping any adjacent out-of-order pair $(x, y)$ to $(y, x)$ does not degrade the objective function ($	ext{Cost}(S') \le 	ext{Cost}(S^*)$).
* **Interval Scheduling**: Sort by earliest end-time to maximize non-overlapping intervals.

#### Production Implementations

**Java**:
```java
import java.util.Arrays;

public class GreedyStrategies {
    public static int maxNonOverlappingIntervals(int[][] intervals) {
        if (intervals.length == 0) return 0;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));

        int count = 1;
        int lastEnd = intervals[0][1];

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] >= lastEnd) {
                count++;
                lastEnd = intervals[i][1];
            }
        }
        return count;
    }
}
```

**Python**:
```python
def max_non_overlapping_intervals(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    count = 1
    last_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= last_end:
            count += 1
            last_end = end
    return count
```

---

### Pattern 8: Bit Manipulation
**Two's Complement Extremes, Submask Traversal, and Bit Counting Modulo K**

#### Core Invariants
* **Two's Complement Asymmetry**: Signed 32-bit int bounds are $[-2^{31}, 2^{31}-1]$. `-Integer.MIN_VALUE` overflows back to `-2^{31}`. Cast to `long` before absolute value operations.
* **Submask Enumeration in $O(3^N)$**:
  ```python
  sub = mask
  while sub > 0:
      sub = (sub - 1) & mask
  ```
* **Bit Counting Modulo $K$**: Summing per-bit frequencies mod $K$ cancels repeating elements, isolating the unique value.

#### Production Implementations

**Java**:
```java
public class BitManipulation {
    public static long isolateLowestBit(long x) {
        return x & (-x);
    }

    public static void processSubmasks(int mask) {
        int sub = mask;
        while (sub > 0) {
            sub = (sub - 1) & mask;
        }
    }

    public static int singleNumberModuloK(int[] nums, int k) {
        int[] bitCounts = new int[32];
        for (int x : nums) {
            for (int i = 0; i < 32; i++) {
                if (((x >> i) & 1) == 1) {
                    bitCounts[i]++;
                }
            }
        }
        int result = 0;
        for (int i = 0; i < 32; i++) {
            if (bitCounts[i] % k != 0) {
                result |= (1 << i);
            }
        }
        return result;
    }
}
```

**Python**:
```python
def isolate_lowest_bit(x: int) -> int:
    return x & (-x)

def process_submasks(mask: int):
    sub = mask
    while sub > 0:
        sub = (sub - 1) & mask

def single_number_modulo_k(nums: list[int], k: int) -> int:
    result = 0
    for i in range(32):
        bit_count = sum((x >> i) & 1 for x in nums)
        if bit_count % k != 0:
            result |= (1 << i)
    if result >= (1 << 31):
        result -= (1 << 32)
    return result
```

---

### Pattern 9: Number Theory & Combinatorics
**Sieve Methods, SPF Acceleration, Modular Arithmetic, and Combinatorics**

#### Core Invariants
* **Sieve & SPF**: Precompute Smallest Prime Factor (`spf[x]`) in $O(N \log \log N)$ to factor any query $X$ in $O(\log X)$.
* **Fermat's Little Theorem**: When $MOD$ is prime, modular division is:
  $$rac{A}{B} \equiv A \cdot B^{MOD-2} \pmod{MOD}$$
* **Multinomial Coefficient**:
  $$rac{N!}{c_1! \cdot c_2! \cdots c_k!} \pmod P = N! \cdot \prod_{i=1}^k (c_i!)^{P-2} \pmod P$$

#### Production Implementations

**Java**:
```java
public class NumberTheory {
    private static final int MAX = 1_000_000;
    private static final int MOD = 1_000_000_007;
    public static int[] spf = new int[MAX + 1];

    public static void initSPF() {
        for (int i = 1; i <= MAX; i++) spf[i] = i;
        for (int i = 2; i * i <= MAX; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= MAX; j += i) {
                    if (spf[j] == j) spf[j] = i;
                }
            }
        }
    }

    public static long powerMod(long base, long exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }

    public static long modInverse(long n) {
        return powerMod(n, MOD - 2);
    }
}
```

**Python**:
```python
MOD = 1_000_000_007
MAX = 1_000_000

spf = list(range(MAX + 1))
for i in range(2, int(MAX**0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, MAX + 1, i):
            if spf[j] == j:
                spf[j] = i

def get_prime_factors(x: int) -> list[int]:
    factors = []
    while x > 1:
        factors.append(spf[x])
        x //= spf[x]
    return factors

def power_mod(base: int, exp: int, mod: int = MOD) -> int:
    return pow(base, exp, mod)

def mod_inverse(n: int, mod: int = MOD) -> int:
    return pow(n, mod - 2, mod)
```

---

### Pattern 10: String Matching & Processing
**Rabin-Karp Rolling Hash and Prefix/XOR Trie**

#### Core Invariants
* **Rabin-Karp Rolling Hash**: Updates window of size $L$ in $O(1)$:
  $$H_{	ext{new}} = ig((H_{	ext{old}} - S[i] \cdot B^{L-1}) \cdot B + S[i+L]ig) \pmod M$$
* **Bitwise XOR Trie**: Greedily follows complementary bit ($1 - b_k$) at each depth to locate maximum XOR partner in $O(32) = O(1)$ per query.

#### Production Implementations

**Java**:
```java
public class StringProcessing {
    public static class TrieNode {
        TrieNode[] children = new TrieNode[2];
    }

    public static class XORTrie {
        private final TrieNode root = new TrieNode();

        public void insert(int val) {
            TrieNode curr = root;
            for (int i = 31; i >= 0; i--) {
                int bit = (val >> i) & 1;
                if (curr.children[bit] == null) {
                    curr.children[bit] = new TrieNode();
                }
                curr = curr.children[bit];
            }
        }

        public int findMaxXOR(int val) {
            TrieNode curr = root;
            int maxXor = 0;
            for (int i = 31; i >= 0; i--) {
                int bit = (val >> i) & 1;
                int desired = 1 - bit;
                if (curr.children[desired] != null) {
                    maxXor |= (1 << i);
                    curr = curr.children[desired];
                } else {
                    curr = curr.children[bit];
                }
            }
            return maxXor;
        }
    }
}
```

**Python**:
```python
class TrieNode:
    def __init__(self):
        self.children = [None, None]

class XORTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, val: int):
        curr = self.root
        for i in range(31, -1, -1):
            bit = (val >> i) & 1
            if not curr.children[bit]:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]

    def find_max_xor(self, val: int) -> int:
        curr = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (val >> i) & 1
            desired = 1 - bit
            if curr.children[desired]:
                max_xor |= (1 << i)
                curr = curr.children[desired]
            else:
                curr = curr.children[bit]
        return max_xor
```

---

## 3. Constraints-to-Algorithm Decoder

| Input Size Constraint ($N$) | Maximum Permissible Complexity | Viable Algorithmic Strategies | Disqualified Approaches |
| :--- | :--- | :--- | :--- |
| **$N \le 10$** | $O(N!)$, $O(N^2 \cdot 2^N)$ | Full permutation generation, recursive backtracking, Traveling Salesperson DP | Heuristic approximations without verification |
| **$N \le 20$** | $O(2^N \cdot N)$, $O(3^N)$ | Bitmask DP, submask enumeration, meet-in-the-middle ($2^{N/2}$) | Full factorial search ($20! pprox 2.4 	imes 10^{18}$) |
| **$N \le 100$** | $O(N^4)$, $O(N^3)$ | Floyd-Warshall, Interval DP, 2D Grid DP, Bellman-Ford | Unmemoized exponential recursions |
| **$N \le 1000$** | $O(N^2)$ | All-pairs algorithms, nested loops, 2D prefix sums, string DP (LCS, Edit Distance) | $O(N^3)$ range evaluations |
| **$N \le 10^5$** | $O(N \log N)$, $O(N)$ | Monotonic stack/deque, sliding window, sorting + two pointers, binary search, segment trees, Dijkstra, DSU | Quadratic nested loops ($O(N^2) = 10^{10} \implies 	ext{TLE}$) |
| **$N \ge 10^9$** | $O(\log N)$, $O(\sqrt{N})$, $O(1)$ | Binary search on the answer, matrix exponentiation, prime testing ($O(\sqrt{N})$), closed-form combinatorics | Any linear scan ($O(N) \ge 10^9 \implies 	ext{TLE}$) |

---

## 4. The 0-Wrong-Answer (0-WA) Pre-Submission Audit

| Audit Category | Specific Defect Check | Correction Mechanism |
| :--- | :--- | :--- |
| **Integer Bounds** | Intermediate accumulation overflowing signed 32-bit limits | Cast accumulators to 64-bit types (`long` / `int64`) before multiplying or summing large elements. |
| **Modular Arithmetic** | Negative results produced by modular subtraction | Apply the standard wrapping idiom: `((a - b) % MOD + MOD) % MOD`. |
| **Array Extremes** | Index out-of-bounds or invalid pointer updates on $N = 1$ | Verify base-case branches directly on arrays of length 1 and 2. |
| **Duplicates** | Identical elements causing infinite loops or incorrect contribution counts | Ensure asymmetric comparison operators ($<$ on left, $\le$ on right) are applied across monotonic stack traversals. |
| **Off-by-One** | Half-open ranges omitting endpoint evaluation | Verify loop bounds (`<=` versus `<`) and ensure difference arrays allocate $N + 1$ slots when updating up to index $N - 1$. |
| **Recursion Limits** | Deep DFS calls causing stack overflows | In Python, configure recursion depth (`sys.setrecursionlimit`); in Java, convert deep traversals to iterative routines. |
| **Signed Bit Shifts** | Negative numbers introducing leading 1s during right shifts | Use unsigned right shift operators (`>>>`) when working with raw bit representations. |
| **Two's Complement** | Negating `Integer.MIN_VALUE` producing a negative result | Cast to 64-bit integer types prior to invoking absolute value or negation routines. |

---

## 5. Contest & Interview Clock Strategy

### 90-Minute Contest Tactical Timeline

| Time Phase | Target Task | Operational Objectives |
| :---: | :--- | :--- |
| **00:00 – 10:00** | **Q1 Execution** | Read prompt completely, identify direct simulation rules, write simplest correct code, verify edge cases ($N=1$), submit cleanly. |
| **10:00 – 30:00** | **Q2 Optimization** | Analyze constraints ($N \le 10^3 \implies O(N^2)$, $N \le 10^5 \implies O(N \log N)$), apply standard patterns (two pointers, sliding window, prefix sums), test sample inputs, submit. |
| **30:00 – 45:00** | **Q3 Paper Derivation** | **Do not write code immediately**. Write down the DP state recurrence, binary search predicate, or monotonic stack invariant on paper. Verify against small counter-examples. |
| **45:00 – 60:00** | **Q3 Implementation** | Implement validated design, review 0-WA checklist, submit. |
| **60:00 – 90:00** | **Q4 Evaluation** | Match constraints against decoder ($N \le 20 \implies 	ext{Bitmask DP}$). If full approach is unclear within 10 min, evaluate simpler sub-cases or partial scores. |

---

### 45-Minute FAANG Technical Interview Protocol

| Interview Phase | Duration | Core Deliverables and Candidate Expectations |
| :---: | :---: | :--- |
| **Phase 1: Clarification** | 00:00 – 05:00 | Restate problem statement, clarify input/output types, confirm edge-case constraints, and state boundary expectations. |
| **Phase 2: Architectural Design** | 05:00 – 15:00 | Propose baseline brute-force solution, then present optimal approach by identifying underlying invariant. State time and space complexities using Big-O notation and confirm agreement with interviewer before writing code. |
| **Phase 3: Clean Implementation** | 15:00 – 35:00 | Write production-grade code with descriptive variable names, modular helpers, and zero unhandled branch conditions. Explain design decisions and invariants continuously while writing. |
| **Phase 4: Manual Dry-Run** | 35:00 – 45:00 | Trace code using a non-trivial example, step through pointer updates manually, verify extreme boundary values, and address scalability follow-ups. |

---

### Triage Protocols & Dead-End Detection

* **The 5-Minute Invariant Rule**: If a proposed algorithm requires introducing special-case patches for basic inputs during the design phase, the underlying model is fundamentally flawed. Abandon the approach immediately and re-evaluate the constraints table.
* **Greedy Verification Failure**: If a proposed greedy strategy cannot be justified via an adjacent exchange argument, construct a small counter-example of size $N = 3$ or $N = 4$. If a counter-example is found, pivot immediately to dynamic programming or a graph formulation.
* **Complexity Mismatch**: If an algorithm's required state space or time complexity exceeds the $10^8$ operations per second limit for the given input size, stop implementation immediately. Rework the state definition or search for monotonic properties.
* **State-Space Simplification**: When multi-dimensional DP state transitions become unmanageable under time pressure, evaluate whether the optimization problem can be converted into a decision problem: *"Can a configuration achieve value $\ge X$?"* $\implies$ converts to binary search on answer with a greedy predicate.

---

## 6. Synthesis & Strategic Conclusions

Consistently solving 3–4 contest problems and passing top-tier technical interviews requires shifting from superficial code pattern matching to formal algorithmic reasoning:
1. **Input Constraints Dictate Algorithms**: The input size $N$ provides an immediate filter for identifying viable time and space complexity classes using the $10^8$ operations per second baseline.
2. **Monotonicity Yields Efficiency**: Identifying monotonic properties across search spaces, window boundaries, and value distributions allows quadratic searches to be reduced to $O(N)$ or $O(N \log N)$ operations via binary search, two pointers, and monotonic data structures.
3. **State Definitions Must Preserve the Markov Property**: Construct DP state vectors with explicit, independent parameters that fully encapsulate the necessary history, adding auxiliary variables only when needed to maintain state independence.
4. **Pre-Submission Audits Prevent Penalties**: Systematically check for integer overflow, boundary cases ($N=1$), duplicates, and off-by-one errors to avoid accumulation of submission penalties and interview red flags.
