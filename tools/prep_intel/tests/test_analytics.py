import unittest
from prep_intel.parsers import ProgressParser, ReviewParser, NotesParser
from prep_intel.analytics import WeaknessEngine, MistakeTaxonomy, ReadinessCalculator

class TestAnalytics(unittest.TestCase):
    def test_weakness_engine(self):
        problems = ProgressParser().parse()
        reviews = ReviewParser().parse_schedule()
        engine = WeaknessEngine(problems, reviews)
        topic_health = engine.compute_topic_health()
        self.assertGreater(len(topic_health), 5)
        for th in topic_health:
            self.assertTrue(0.0 <= th.health_score <= 100.0)
            self.assertTrue(0.0 <= th.hint_reliance_pct <= 100.0)

    def test_mistake_taxonomy(self):
        mistakes = NotesParser().parse_mistake_journal()
        tax = MistakeTaxonomy(mistakes)
        breakdown = tax.get_category_breakdown()
        self.assertGreaterEqual(len(breakdown), 4)
        total_pct = sum(b[2] for b in breakdown)
        self.assertTrue(99.0 <= total_pct <= 101.0)

    def test_readiness_calculator(self):
        problems = ProgressParser().parse()
        reviews = ReviewParser().parse_schedule()
        mistakes = NotesParser().parse_mistake_journal()
        calc = ReadinessCalculator(problems, reviews, mistakes)
        profile = calc.calculate_profile()
        self.assertTrue(0.0 <= profile.overall_readiness_pct <= 100.0)
        self.assertGreater(profile.solved_count, 0)
        self.assertGreater(len(profile.top_weaknesses), 0)

if __name__ == "__main__":
    unittest.main()
