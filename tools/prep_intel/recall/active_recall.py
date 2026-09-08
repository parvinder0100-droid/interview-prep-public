"""Active recall prompt generator and flashcard session engine."""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
from ..models import ReviewItem
from .scheduler import SpacedScheduler

@dataclass
class ActiveRecallCard:
    problem_name: str
    review_num: int
    tags: List[str]
    days_overdue: int
    question: str
    revealed_invariant: str
    known_trap: str
    note_path: Optional[str] = None

class ActiveRecallSession:
    def __init__(self, review_items: List[ReviewItem], notes_data: Dict[str, Dict[str, str]]):
        self.review_items = review_items
        self.notes_data = notes_data

    def generate_cards(self, max_cards: int = 10, priority_only: bool = True) -> List[ActiveRecallCard]:
        cards: List[ActiveRecallCard] = []

        # Filter items: prioritize leeches, derive tags, and overdue items
        pool = list(self.review_items)
        if priority_only:
            pool.sort(
                key=lambda x: (
                    "[leech]" in x.tags,
                    "[derive]" in x.tags,
                    x.days_overdue > 0,
                    x.days_overdue
                ),
                reverse=True
            )

        for it in pool[:max_cards]:
            norm_name = it.problem_name.lower()
            note_info = self.notes_data.get(norm_name, {})
            
            # Formulate the active recall question
            if it.recall_prompt:
                q = it.recall_prompt
            else:
                q = f"State the core algorithmic invariant and derivation approach for {it.problem_name} without looking at code."

            known_trap = note_info.get("bug", "")
            if not known_trap and "[derive]" in it.tags:
                known_trap = "Review tag indicates repeat rust on memorized procedure; must derive causality from scratch."

            invariant = note_info.get("preview", "Review problem note for complete invariant details.")

            cards.append(ActiveRecallCard(
                problem_name=it.problem_name,
                review_num=it.review_num,
                tags=it.tags,
                days_overdue=it.days_overdue,
                question=q,
                revealed_invariant=invariant,
                known_trap=known_trap,
                note_path=it.note_relpath
            ))

        return cards
