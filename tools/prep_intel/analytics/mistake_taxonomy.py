"""Taxonomy and pattern aggregator for mistake post-mortems."""

from collections import Counter, defaultdict
from typing import Dict, List, Tuple
from ..models import MistakeEntry

CATEGORY_RULES = {
    "Type Bounds & Overflow": "Cast operands to `(long)` BEFORE multiplication/prefix sums. In Java, (1L << i) for shifts >= 31. Modulo addition requires `((a % M) + (b % M)) % M`.",
    "Monotonicity & Invariants": "Do not assume window sum monotonicity if numbers can be negative (switch to Prefix Sum + HashMap). In binary search, verify predicate truth table is monotonic FFF...TTT.",
    "Loop & Boundary Off-by-One": "Verify difference array allocation size is N+2 to absorb D[R+1]. In two-pointer while loops, ensure pointers strictly advance per iteration to prevent infinite loops.",
    "Edge Cases & Degeneracy": "Always dry run: N=1, empty string, all elements equal, negative arrays, and disconnected graph components before code submission.",
    "Process & Consistency": "Never code before the invariant is derived and proven. Never skip the 5-8 minute opening review block on due spaced-repetition items.",
    "Algorithmic Logic & Modeling": "Double-check problem constraints: if N=10^5, reject O(N^2) approaches immediately. Look for sorting, stack, or binary search pivots.",
}

class MistakeTaxonomy:
    def __init__(self, mistakes: List[MistakeEntry]):
        self.mistakes = mistakes

    def get_category_breakdown(self) -> List[Tuple[str, int, float, str]]:
        """Returns list of (Category, Count, Percentage, Preventive Rule)."""
        if not self.mistakes:
            return []

        counts = Counter(m.category for m in self.mistakes)
        total = len(self.mistakes)

        results = []
        for cat, cnt in counts.most_common():
            pct = round((cnt / total) * 100.0, 1)
            rule = CATEGORY_RULES.get(cat, "Maintain rigorous invariant checks.")
            results.append((cat, cnt, pct, rule))

        return results

    def get_pattern_breakdown(self, limit: int = 8) -> List[Tuple[str, int]]:
        """Returns most frequent algorithmic patterns causing mistakes."""
        counts = Counter(m.pattern for m in self.mistakes if m.pattern and m.pattern != "General")
        return counts.most_common(limit)

    def get_recent_mistakes_by_category(self, category: str, limit: int = 5) -> List[MistakeEntry]:
        filtered = [m for m in self.mistakes if m.category == category]
        return filtered[:limit]
