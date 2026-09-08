---
type: note
problem: Redundant Connection
topic: UnionFind
updated: 2026-07-27
---

# Redundant Connection (Union-Find)

Approach: parent array (path compression via recursive find), union by rank.

Bug found in code review: `rank[winner]++` fired on every union win, not just
on ties — this breaks the invariant that rank upper-bounds true tree height.
Correctness (connectivity) unaffected, but the O(log n) height guarantee (and
thus amortized O(α(n)) find) is lost — a wrong-rank tree can force taller
trees to nest under it, growing true height ~linearly with unions instead of
log n. Fix: only increment rank on the tie branch.

Complexity: O(α(n)) amortized per op with both path compression + union by
rank — practically constant (α(n) ≤ 4 for any real n) but not literal O(1).
