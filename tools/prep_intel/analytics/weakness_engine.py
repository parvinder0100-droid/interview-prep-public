"""Engine for diagnosing topic weaknesses, hint debt, and forgetting decay."""

from collections import defaultdict
from typing import Dict, List, Tuple
from ..models import Problem, ReviewItem, TopicHealth

class WeaknessEngine:
    def __init__(self, problems: List[Problem], review_items: List[ReviewItem]):
        self.problems = problems
        self.review_items = review_items

    def compute_topic_health(self) -> List[TopicHealth]:
        topic_probs = defaultdict(list)
        for p in self.problems:
            t = p.topic.split("/")[0].strip() if p.topic else "General"
            topic_probs[t].append(p)

        # Count overdue reviews per topic
        overdue_by_prob_name = {
            r.problem_name.lower(): r.days_overdue 
            for r in self.review_items 
            if r.days_overdue > 0
        }

        results: List[TopicHealth] = []

        for topic, p_list in topic_probs.items():
            total = len(p_list)
            solved_list = [p for p in p_list if p.is_solved]
            solved_cnt = len(solved_list)
            hint_cnt = sum(1 for p in solved_list if p.hint_count > 0)
            clean_cnt = solved_cnt - hint_cnt

            hint_pct = (hint_cnt / solved_cnt * 100.0) if solved_cnt > 0 else 0.0

            # Count overdue
            overdue_cnt = 0
            for p in solved_list:
                for r_name, ov_days in overdue_by_prob_name.items():
                    if p.name.lower() in r_name or r_name in p.name.lower():
                        overdue_cnt += 1
                        break

            # Calculate Health Score (0 - 100)
            # Base 100, penalized by:
            # - Unsolved ratio (up to 40 pts)
            # - Hint reliance (up to 30 pts)
            # - Overdue decay (up to 30 pts)
            coverage_penalty = (1.0 - (solved_cnt / total)) * 40.0 if total > 0 else 40.0
            hint_penalty = (hint_pct / 100.0) * 30.0
            decay_penalty = min(30.0, overdue_cnt * 5.0)

            score = max(0.0, min(100.0, 100.0 - (coverage_penalty + hint_penalty + decay_penalty)))

            if score >= 80:
                status = "Solid"
            elif score >= 60:
                status = "Moderate"
            elif solved_cnt > 0:
                status = "Fragile / Hint Debt"
            else:
                status = "Unstarted"

            results.append(TopicHealth(
                topic=topic,
                total_problems=total,
                solved_count=solved_cnt,
                clean_solved_count=clean_cnt,
                hint_solved_count=hint_cnt,
                hint_reliance_pct=round(hint_pct, 1),
                overdue_reviews_count=overdue_cnt,
                health_score=round(score, 1),
                status=status
            ))

        # Sort: lowest health score first (highest weakness first)
        results.sort(key=lambda x: (x.health_score, -x.hint_reliance_pct))
        return results

    def get_highest_risk_problems(self, limit: int = 10) -> List[Tuple[Problem, str]]:
        """Returns specific problems with the highest risk profile (hints + overdue)."""
        risks = []
        for p in self.problems:
            if not p.is_solved:
                continue
            reason = []
            if p.hint_count >= 3:
                reason.append(f"Heavy Hints ({p.hint_count})")
            elif p.hint_count > 0:
                reason.append(f"Hints ({p.hint_count})")

            # Check if overdue
            for r in self.review_items:
                if (p.name.lower() in r.problem_name.lower() or r.problem_name.lower() in p.name.lower()) and r.days_overdue > 0:
                    reason.append(f"{r.days_overdue}d Overdue")
                    break

            if reason:
                risks.append((p, " • ".join(reason)))

        risks.sort(key=lambda x: x[0].hint_count, reverse=True)
        return risks[:limit]
