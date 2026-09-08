"""Readiness assessment algorithm and executive readiness profile."""

from typing import List
from ..models import Problem, ReviewItem, MistakeEntry, ReadinessProfile
from .weakness_engine import WeaknessEngine

class ReadinessCalculator:
    def __init__(self, problems: List[Problem], review_items: List[ReviewItem], mistakes: List[MistakeEntry]):
        self.problems = problems
        self.review_items = review_items
        self.mistakes = mistakes
        self.weakness_engine = WeaknessEngine(problems, review_items)

    def calculate_profile(self) -> ReadinessProfile:
        total_p = len(self.problems)
        solved_p = [p for p in self.problems if p.is_solved]
        solved_cnt = len(solved_p)

        coverage_pct = (solved_cnt / total_p * 100.0) if total_p > 0 else 0.0

        hint_cnt = sum(1 for p in solved_p if p.hint_count > 0)
        clean_cnt = solved_cnt - hint_cnt
        hint_reliance_idx = (hint_cnt / solved_cnt * 100.0) if solved_cnt > 0 else 0.0

        overdue_cnt = sum(1 for r in self.review_items if r.days_overdue > 0)
        leech_cnt = sum(1 for r in self.review_items if "[leech]" in r.tags)

        # Multi-factor formula:
        # 1. Coverage Component (30% weight) -> coverage_pct * 0.30
        comp_coverage = min(100.0, coverage_pct) * 0.30

        # 2. Clean Solve Component (30% weight) -> (100 - hint_reliance) * 0.30
        comp_clean = max(0.0, (100.0 - hint_reliance_idx)) * 0.30

        # 3. Spaced Retention Freshness (25% weight)
        # Ratio of non-overdue items
        total_reviews = len(self.review_items)
        if total_reviews > 0:
            fresh_ratio = max(0.0, (total_reviews - overdue_cnt) / total_reviews)
            comp_retention = fresh_ratio * 100.0 * 0.25
        else:
            comp_retention = 25.0

        # 4. Leech / Defect Mitigation (15% weight)
        comp_mitigation = max(0.0, 15.0 - (leech_cnt * 3.0))

        overall_readiness = round(comp_coverage + comp_clean + comp_retention + comp_mitigation, 1)

        # Diagnose Top Weaknesses
        top_weaknesses = []
        topic_health = self.weakness_engine.compute_topic_health()
        
        # 1. Stalled / Fragile topics
        fragile_topics = [th.topic for th in topic_health if th.health_score < 60]
        if fragile_topics:
            top_weaknesses.append(f"Fragile Topics: {', '.join(fragile_topics[:3])} (low retention or high hint debt)")

        # 2. High Hint Reliance
        if hint_reliance_idx > 35:
            top_weaknesses.append(f"High Hint Dependency ({round(hint_reliance_idx, 1)}% of solves required guided hints)")

        # 3. Review Backlog Decay
        if overdue_cnt > 20:
            top_weaknesses.append(f"Spaced Review Debt ({overdue_cnt} items overdue; forgetting curve actively degrading recall)")

        if leech_cnt > 0:
            top_weaknesses.append(f"Active Leech Concepts ({leech_cnt} items failing same core invariant 3+ times)")

        return ReadinessProfile(
            total_problems=total_p,
            solved_count=solved_cnt,
            coverage_pct=round(coverage_pct, 1),
            hint_reliance_index=round(hint_reliance_idx, 1),
            total_overdue_reviews=overdue_cnt,
            overall_readiness_pct=overall_readiness,
            top_weaknesses=top_weaknesses,
            active_leech_count=leech_cnt,
            total_mistakes_logged=len(self.mistakes)
        )
