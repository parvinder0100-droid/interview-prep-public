import unittest
import datetime as dt
from prep_intel.recall import SpacedScheduler, ActiveRecallSession
from prep_intel.parsers import ReviewParser, NotesParser

class TestRecall(unittest.TestCase):
    def test_spaced_scheduler_clean(self):
        base = dt.date(2026, 9, 1)
        next_rev, due_str, grad = SpacedScheduler.calculate_next_interval(1, "clean", base)
        self.assertEqual(next_rev, 2)
        self.assertEqual(due_str, "2026-09-04")
        self.assertFalse(grad)

    def test_spaced_scheduler_hint(self):
        base = dt.date(2026, 9, 1)
        next_rev, due_str, grad = SpacedScheduler.calculate_next_interval(3, "hint", base)
        self.assertEqual(next_rev, 3)
        self.assertEqual(due_str, "2026-09-03")
        self.assertFalse(grad)

    def test_spaced_scheduler_fail(self):
        base = dt.date(2026, 9, 1)
        next_rev, due_str, grad = SpacedScheduler.calculate_next_interval(4, "fail", base)
        self.assertEqual(next_rev, 1)
        self.assertEqual(due_str, "2026-09-02")
        self.assertFalse(grad)

    def test_active_recall_session(self):
        reviews = ReviewParser().parse_schedule()
        notes = NotesParser().parse_notes_invariants()
        session = ActiveRecallSession(reviews, notes)
        cards = session.generate_cards(max_cards=5)
        self.assertEqual(len(cards), 5)
        for c in cards:
            self.assertTrue(len(c.problem_name) > 0)
            self.assertTrue(len(c.question) > 0)

if __name__ == "__main__":
    unittest.main()
