"""Domain dataclasses for PrepIntel."""

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Problem:
    name: str
    id_code: str = ""
    topic: str = "General"
    subtopic: str = ""
    difficulty: str = "Medium"
    is_solved: bool = False
    solved_date: Optional[str] = None
    hint_count: int = 0
    note_relpath: Optional[str] = None
    session_summary: str = ""
    elo_rating: Optional[float] = None

@dataclass
class ReviewItem:
    problem_name: str
    due_date: str
    review_num: int
    tags: List[str] = field(default_factory=list)
    days_overdue: int = 0
    recall_prompt: str = ""
    note_relpath: Optional[str] = None

@dataclass
class ReviewLogEntry:
    problem_name: str
    review_num: int
    completed_date: str
    outcome: str  # "clean", "hint", "guided", "fail"
    notes: str = ""

@dataclass
class MistakeEntry:
    date: str
    problem: str
    title: str
    mistake: str
    root_cause: str
    correct_thinking: str
    how_to_avoid: str
    pattern: str = "General"
    category: str = "General Logic"

@dataclass
class TopicHealth:
    topic: str
    total_problems: int
    solved_count: int
    clean_solved_count: int
    hint_solved_count: int
    hint_reliance_pct: float
    overdue_reviews_count: int
    health_score: float  # 0.0 to 100.0
    status: str  # "Solid", "Needs Review", "High Hint Debt", "Unstarted"

@dataclass
class ReadinessProfile:
    total_problems: int
    solved_count: int
    coverage_pct: float
    hint_reliance_index: float
    total_overdue_reviews: int
    overall_readiness_pct: float
    top_weaknesses: List[str]
    active_leech_count: int
    total_mistakes_logged: int
