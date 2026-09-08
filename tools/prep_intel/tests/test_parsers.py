import unittest
from pathlib import Path
from prep_intel.parsers import ProgressParser, ReviewParser, NotesParser

class TestParsers(unittest.TestCase):
    def test_progress_parser(self):
        parser = ProgressParser()
        problems = parser.parse()
        self.assertGreater(len(problems), 50)
        solved = [p for p in problems if p.is_solved]
        self.assertGreater(len(solved), 40)
        topics = {p.topic for p in problems}
        self.assertIn("Recursion", topics)
        self.assertIn("Graph", topics)
        self.assertIn("Arrays", topics)

    def test_review_parser(self):
        parser = ReviewParser()
        schedule = parser.parse_schedule()
        logs = parser.parse_logs()
        self.assertGreater(len(schedule), 50)
        self.assertGreater(len(logs), 50)
        for item in schedule:
            self.assertIsInstance(item.days_overdue, int)
            self.assertGreaterEqual(item.review_num, 1)

    def test_notes_parser(self):
        parser = NotesParser()
        mistakes = parser.parse_mistake_journal()
        notes = parser.parse_notes_invariants()
        self.assertGreater(len(mistakes), 100)
        self.assertGreater(len(notes), 20)
        categories = {m.category for m in mistakes}
        self.assertIn("Monotonicity & Invariants", categories)
        self.assertIn("Loop & Boundary Off-by-One", categories)

if __name__ == "__main__":
    unittest.main()
