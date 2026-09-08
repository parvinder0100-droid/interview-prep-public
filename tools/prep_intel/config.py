"""Configuration constants and file paths for PrepIntel."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

PROGRESS_MD = REPO_ROOT / "DSA" / "Progress" / "progress.md"
REVIEW_SCHEDULE_MD = REPO_ROOT / "DSA" / "Progress" / "review_schedule.md"
REVIEW_LOG_MD = REPO_ROOT / "DSA" / "Progress" / "review_log_archive.md"
MISTAKE_JOURNAL_MD = REPO_ROOT / "DSA" / "mistakes" / "mistake_journal.md"
DASHBOARD_MD = REPO_ROOT / "Progress" / "dashboard.md"
NOTES_DIR = REPO_ROOT / "DSA" / "notes"
CONTESTS_JSON = REPO_ROOT / "DSA" / "contests" / "weekly_contests_past_50.json"
OUTPUT_DASHBOARD_HTML = REPO_ROOT / "Progress" / "prep_dashboard.html"

# Spaced Repetition Standard Progression
SR_INTERVALS = [1, 3, 7, 14, 30, 60, 90]

# Empirical LeetCode Elo Thresholds
ELO_THRESHOLDS = {
    "Q1": 1220,
    "Q2": 1485,
    "Q3_MEDIAN": 1871,
    "Q4": 2281,
    "KNIGHT": 1850,
    "GUARDIAN": 2200,
}
