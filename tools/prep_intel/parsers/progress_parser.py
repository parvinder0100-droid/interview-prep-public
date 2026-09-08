"""Parser for progress.md and sprint coverage with topic normalization."""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional

from ..config import PROGRESS_MD, CONTESTS_JSON
from ..models import Problem

CANONICAL_TOPICS = [
    ("Recursion", ["recursion", "backtracking", "queens", "permutations"]),
    ("Stack/Queue", ["stack", "queue", "rain water", "parentheses", "next greater"]),
    ("Sliding Window", ["sliding", "window", "two pointers"]),
    ("Graph", ["graph", "bfs", "dfs", "dijkstra", "kahn", "topological", "provinces"]),
    ("DP", ["dp", "dynamic", "knapsack", "frog jump", "subsequence"]),
    ("Bit Manipulation", ["bit", "manipulation", "xor", "power of two", "single number"]),
    ("Heaps", ["heap", "priority", "median"]),
    ("Binary Search", ["binary search", "search", "matrix search"]),
    ("Trees", ["tree", "bst", "traversal"]),
    ("LinkedList", ["linked", "list"]),
    ("Strings", ["string", "anagram", "palindrome"]),
    ("Greedy", ["greedy", "intervals", "jump game"]),
    ("Arrays", ["array", "kadane", "pascal", "two sum", "sorting", "matrix"]),
]

class ProgressParser:
    def __init__(self, progress_path: Optional[Path] = None, contests_path: Optional[Path] = None):
        self.progress_path = progress_path or PROGRESS_MD
        self.contests_path = contests_path or CONTESTS_JSON
        self._elo_lookup = self._load_elo_lookup()

    def _load_elo_lookup(self) -> Dict[str, float]:
        lookup: Dict[str, float] = {}
        if not self.contests_path.exists():
            return lookup
        try:
            with open(self.contests_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for contest in data:
                for p in contest.get("problems", []):
                    title = p.get("title", "").strip().lower()
                    if title and "rating" in p:
                        lookup[title] = float(p["rating"])
        except Exception:
            pass
        return lookup

    def _clean_name(self, raw_name: str) -> str:
        name = re.sub(r"`?\[(derive|leech|Medium|Easy|Hard)\]`?", "", raw_name)
        name = re.sub(r"\(.*?\)", "", name)
        return name.strip()

    def _extract_id(self, raw_name: str) -> str:
        m = re.search(r"\((.*?)\)", raw_name)
        return m.group(1).strip() if m else ""

    def _normalize_topic(self, raw_topic: str, problem_name: str) -> str:
        haystack = f"{raw_topic} {problem_name}".lower()
        for canonical, keywords in CANONICAL_TOPICS:
            if any(k in haystack for k in keywords):
                return canonical
        return "General"

    def parse(self) -> List[Problem]:
        problems: List[Problem] = []
        if not self.progress_path.exists():
            return problems

        content = self.progress_path.read_text(encoding="utf-8")

        for line in content.splitlines():
            line = line.strip()
            if not (line.startswith("- [x]") or line.startswith("- [ ]")):
                continue

            is_solved = line.startswith("- [x]")
            body = line[5:].strip()
            parts = [p.strip() for p in body.split("—")]
            if not parts:
                continue

            raw_name = parts[0]
            name = self._clean_name(raw_name)
            id_code = self._extract_id(raw_name)
            raw_topic = parts[1] if len(parts) > 1 else "General"
            diff = parts[2] if len(parts) > 2 else "Medium"

            topic = self._normalize_topic(raw_topic, name)

            note_path = None
            hints = 0
            solved_date = None
            summary = ""

            for part in parts[3:]:
                if "[note]" in part:
                    m_note = re.search(r"\[note\]\((.*?)\)", part)
                    if m_note:
                        note_path = m_note.group(1)
                elif "solved:" in part or "with-hints:" in part:
                    m_hint = re.search(r"with-hints:(\d+)", part)
                    if m_hint:
                        hints = int(m_hint.group(1))
                    elif "independently" in part or "clean" in part:
                        hints = 0
                    m_date = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", part)
                    if m_date:
                        solved_date = m_date.group(1)
                else:
                    if not summary:
                        summary = part

            elo = self._elo_lookup.get(name.lower())

            problems.append(Problem(
                name=name,
                id_code=id_code,
                topic=topic,
                subtopic="",
                difficulty=diff,
                is_solved=is_solved,
                solved_date=solved_date,
                hint_count=hints,
                note_relpath=note_path,
                session_summary=summary,
                elo_rating=elo
            ))

        return problems
