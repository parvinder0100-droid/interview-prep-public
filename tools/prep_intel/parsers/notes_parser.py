"""Parser for problem notes in DSA/notes/*.md and DSA/mistakes/mistake_journal.md."""

import re
from pathlib import Path
from typing import Dict, List, Optional

from ..config import MISTAKE_JOURNAL_MD, NOTES_DIR
from ..models import MistakeEntry

class NotesParser:
    def __init__(self, notes_dir: Optional[Path] = None, journal_path: Optional[Path] = None):
        self.notes_dir = notes_dir or NOTES_DIR
        self.journal_path = journal_path or MISTAKE_JOURNAL_MD

    def _categorize_mistake(self, title: str, mistake: str, root_cause: str) -> str:
        text = f"{title} {mistake} {root_cause}".lower()

        if any(k in text for k in ["overflow", "long", "modulo", "int.max", "int.min", "shift", "operator precedence"]):
            return "Type Bounds & Overflow"
        if any(k in text for k in ["monotonic", "predicate", "greedy", "invariant", "direction", "indegree"]):
            return "Monotonicity & Invariants"
        if any(k in text for k in ["index", "boundary", "off-by-one", "continue", "inner loop", "termination"]):
            return "Loop & Boundary Off-by-One"
        if any(k in text for k in ["disconnected", "empty", "n=1", "n=0", "edge case", "single node", "isolated"]):
            return "Edge Cases & Degeneracy"
        if any(k in text for k in ["process", "skipped", "review block", "meta", "declined"]):
            return "Process & Consistency"
        return "Algorithmic Logic & Modeling"

    def parse_mistake_journal(self) -> List[MistakeEntry]:
        mistakes: List[MistakeEntry] = []
        if not self.journal_path.exists():
            return mistakes

        content = self.journal_path.read_text(encoding="utf-8")
        sections = content.split("### ")

        for sec in sections[1:]:
            lines = sec.strip().splitlines()
            if not lines:
                continue

            header = lines[0].strip()
            h_parts = [p.strip() for p in header.split("—")]

            date = h_parts[0] if len(h_parts) > 0 else ""
            problem = h_parts[1] if len(h_parts) > 1 else ""
            title = h_parts[2] if len(h_parts) > 2 else header

            mistake_text = ""
            root_cause = ""
            correct_thinking = ""
            how_to_avoid = ""
            pattern = "General"

            for l in lines[1:]:
                l_str = l.strip()
                if l_str.startswith("- Mistake:"):
                    mistake_text = l_str[10:].strip()
                elif l_str.startswith("- Root Cause:"):
                    root_cause = l_str[13:].strip()
                elif l_str.startswith("- Correct Thinking:"):
                    correct_thinking = l_str[19:].strip()
                elif l_str.startswith("- How to Avoid:"):
                    how_to_avoid = l_str[15:].strip()
                elif l_str.startswith("- Pattern:"):
                    pattern = l_str[10:].strip()

            cat = self._categorize_mistake(title, mistake_text, root_cause)

            mistakes.append(MistakeEntry(
                date=date,
                problem=problem,
                title=title,
                mistake=mistake_text,
                root_cause=root_cause,
                correct_thinking=correct_thinking,
                how_to_avoid=how_to_avoid,
                pattern=pattern,
                category=cat
            ))

        return mistakes

    def parse_notes_invariants(self) -> Dict[str, Dict[str, str]]:
        """Scans DSA/notes/*.md for core invariants and documented bugs."""
        notes_data: Dict[str, Dict[str, str]] = {}
        if not self.notes_dir.exists():
            return notes_data

        for note_file in self.notes_dir.glob("*.md"):
            try:
                text = note_file.read_text(encoding="utf-8")
                problem_name = note_file.stem.replace("-", " ").title()

                # check frontmatter for problem name
                m_prob = re.search(r"problem:\s*(.*)", text)
                if m_prob:
                    problem_name = m_prob.group(1).strip()

                bug = ""
                m_bug = re.search(r"\*\*Bug\*\*:\s*(.*?)(?=\n\n|\Z)", text, re.DOTALL)
                if m_bug:
                    bug = m_bug.group(1).strip()

                notes_data[problem_name.lower()] = {
                    "file": str(note_file.name),
                    "bug": bug,
                    "preview": text[:200]
                }
            except Exception:
                pass

        return notes_data
