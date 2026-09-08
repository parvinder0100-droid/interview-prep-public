"""Spaced repetition schedule calculator based on Leitner / SuperMemo progression."""

import datetime as dt
from typing import Optional, Tuple
from ..config import SR_INTERVALS
from ..models import ReviewItem, ReviewLogEntry

class SpacedScheduler:
    INTERVAL_MAP = {
        1: 1,   # R1 -> +1 day
        2: 3,   # R2 -> +3 days
        3: 7,   # R3 -> +7 days
        4: 14,  # R4 -> +14 days
        5: 30,  # R5 -> +30 days
        6: 60,  # R6 -> +60 days
        7: 90   # R7 -> +90 days
    }

    @classmethod
    def calculate_next_interval(
        cls, 
        current_rev: int, 
        outcome: str, 
        base_date: Optional[dt.date] = None
    ) -> Tuple[int, str, bool]:
        """
        Calculates (next_review_number, next_due_date_str, is_graduated).
        outcome in {"clean", "hint", "guided", "fail"}.
        """
        ref = base_date or dt.date.today()
        outcome = outcome.lower()

        if outcome == "clean":
            next_rev = current_rev + 1
            if current_rev >= 4:
                # Candidate for graduation
                pass
            days = cls.INTERVAL_MAP.get(next_rev, 30)
            next_due = (ref + dt.timedelta(days=days)).strftime("%Y-%m-%d")
            is_graduated = next_rev > 6
            return next_rev, next_due, is_graduated

        elif outcome in ("hint", "guided"):
            # Partial recall - repeat same review number in 2 days
            next_due = (ref + dt.timedelta(days=2)).strftime("%Y-%m-%d")
            return current_rev, next_due, False

        else:  # "fail"
            # Complete lapse - reset back to Review 1, due tomorrow
            next_due = (ref + dt.timedelta(days=1)).strftime("%Y-%m-%d")
            return 1, next_due, False
