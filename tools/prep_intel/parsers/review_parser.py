"""Parser for review_schedule.md and review_log_archive.md."""

import datetime as dt
import re
from pathlib import Path
from typing import List, Optional, Tuple

from ..config import REVIEW_SCHEDULE_MD, REVIEW_LOG_MD
from ..models import ReviewItem, ReviewLogEntry

class ReviewParser:
    def __init__(self, schedule_path: Optional[Path] = None, log_path: Optional[Path] = None):
        self.schedule_path = schedule_path or REVIEW_SCHEDULE_MD
        self.log_path = log_path or REVIEW_LOG_MD

    def parse_schedule(self, target_date: Optional[dt.date] = None) -> List[ReviewItem]:
        items: List[ReviewItem] = []
        if not self.schedule_path.exists():
            return items

        ref_date = target_date or dt.date.today()
        content = self.schedule_path.read_text(encoding="utf-8")

        for line in content.splitlines():
            line = line.strip()
            if not (line.startswith("- ") and "due:" in line):
                continue

            parts = [p.strip() for p in line[2:].split("—")]
            if not parts:
                continue

            raw_name = parts[0]
            tags = []
            if "[derive]" in raw_name:
                tags.append("[derive]")
            if "[leech]" in raw_name:
                tags.append("[leech]")

            name = re.sub(r"`?\[(derive|leech)\]`?", "", raw_name).strip()

            due_str = ""
            m_due = re.search(r"due:\s*(\d{4}-\d{2}-\d{2})", line)
            if m_due:
                due_str = m_due.group(1)

            rev_num = 1
            m_rev = re.search(r"review\s*#(\d+)", line)
            if m_rev:
                rev_num = int(m_rev.group(1))

            prompt = ""
            if "Open on" in line:
                prompt = line.split("Open on", 1)[1].strip(": —*")
            elif "outcome:" in line:
                prompt = line.split("outcome:", 1)[1].strip()

            note_path = None
            m_note = re.search(r"\[note\]\((.*?)\)", line)
            if m_note:
                note_path = m_note.group(1)

            days_overdue = 0
            if due_str:
                try:
                    d_val = dt.datetime.strptime(due_str, "%Y-%m-%d").date()
                    days_overdue = (ref_date - d_val).days
                except ValueError:
                    pass

            items.append(ReviewItem(
                problem_name=name,
                due_date=due_str,
                review_num=rev_num,
                tags=tags,
                days_overdue=days_overdue,
                recall_prompt=prompt,
                note_relpath=note_path
            ))

        # Sort: most overdue first
        items.sort(key=lambda x: x.days_overdue, reverse=True)
        return items

    def parse_logs(self) -> List[ReviewLogEntry]:
        entries: List[ReviewLogEntry] = []
        if not self.log_path.exists():
            return entries

        content = self.log_path.read_text(encoding="utf-8")

        for line in content.splitlines():
            line = line.strip()
            if not (line.startswith("- ") and "completed:" in line):
                continue

            parts = [p.strip() for p in line[2:].split("—")]
            if len(parts) < 3:
                continue

            raw_name = parts[0]
            name = re.sub(r"`?\[(derive|leech)\]`?", "", raw_name).strip()

            rev_num = 1
            m_rev = re.search(r"review\s*#(\d+)", line)
            if m_rev:
                rev_num = int(m_rev.group(1))

            completed_date = ""
            m_comp = re.search(r"completed:\s*(\d{4}-\d{2}-\d{2})", line)
            if m_comp:
                completed_date = m_comp.group(1)

            outcome = "clean"
            m_out = re.search(r"outcome:\s*(\w+)", line)
            if m_out:
                outcome = m_out.group(1).lower()

            notes = parts[-1] if len(parts) > 3 else ""

            entries.append(ReviewLogEntry(
                problem_name=name,
                review_num=rev_num,
                completed_date=completed_date,
                outcome=outcome,
                notes=notes
            ))

        return entries
