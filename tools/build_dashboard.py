#!/usr/bin/env python3
"""Parse the ~/InterviewPrep markdown tracker and emit a single self-contained
HTML dashboard.

Usage:  python3 tools/build_dashboard.py [--out PATH] [--no-history]

Reads (all optional — missing files degrade to empty sections):
  Progress/cycle.md                   mode, start, target_end
  Progress/dashboard.md               track readiness lines
  DSA/Progress/review_schedule.md     open spaced-repetition queue
  DSA/Progress/review_log_archive.md  completed reviews + outcomes
  DSA/Progress/progress.md            completed problems + session notes
  DSA/mistakes/mistake_journal.md     every logged mistake
  SystemDesign/Progress/progress.md   case-study checklist

Writes a snapshot row to Progress/metrics_history.jsonl on each run so the
backlog trend keeps accumulating even where the markdown can't reconstruct it.

Tunables (scope estimates, session cap) live in CONFIG below.
"""

import argparse
import datetime as dt
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = dt.date.today()

CONFIG = {
    "session_review_cap": 12,
    "hours": {                      # rough per-item costs for the pace estimate
        "review": 0.12,
        "graph_algo_remaining": 0.6,
        "import_backlog_item": 0.15,
        "system_design_case": 1.0,
        "zero_track_bootstrap": 4.0,
    },
    "import_backlog_remaining": 160,
    "graph_algos_remaining": 3,     # Floyd-Warshall close-out, Prim's, Kruskal's
}

DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
HEALTH = {"warnings": [], "counts": {}}


def warn(kind, detail):
    HEALTH["warnings"].append({"kind": kind, "detail": detail})


def read(*parts):
    path = os.path.join(ROOT, *parts)
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        warn("missing-file", os.path.join(*parts))
        return ""


def parse_date(text):
    m = DATE_RE.search(text or "")
    if not m:
        return None
    try:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def bullets(section_text):
    """Join wrapped continuation lines so each top-level '- ' bullet is one string."""
    out = []
    for line in section_text.splitlines():
        if re.match(r"^\s*-\s", line) and not line.startswith("  "):
            out.append(line.strip())
        elif line.startswith("  ") and out:
            out[-1] += " " + line.strip()
    return out


def section(text, heading):
    pat = re.compile(r"^##\s+" + re.escape(heading) + r"\s*$(.*?)(?=^##\s|\Z)",
                     re.M | re.S)
    m = pat.search(text)
    if not m and text:
        warn("missing-section", heading)
    return m.group(1) if m else ""


def norm(name):
    """Normalize a problem name for joining across files."""
    s = name.lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def strip_tags(raw):
    tags = re.findall(r"\[(derive|leech)\]", raw)
    name = re.sub(r"`?\[(derive|leech)\]`?", "", raw).strip(" `—")
    return name, sorted(set(tags))


def find_opener(text):
    """The schedule often names the exact question a review must open with."""
    m = re.search(
        r"(?:open the review with|start(?:s)? with|open with|must open with)\s*[:\-]?\s*"
        r"[\"“']?(.+?)[\"”']?(?=\s+(?:—|before any code|before code|before the|then\b)|$)",
        text, re.I)
    if not m:
        return ""
    out = re.sub(r"\s+", " ", m.group(1))
    out = re.split(r"[\"”']", out)[0]      # a quoted opener ends at its closing quote
    out = out.strip(" .,;—-")
    return out if 10 < len(out) < 220 else ""


# --------------------------------------------------------------------------
# cycle
# --------------------------------------------------------------------------

def parse_cycle():
    text = read("Progress", "cycle.md")

    def field(name):
        m = re.search(rf"^{name}:\s*(.+)$", text, re.M)
        return m.group(1).strip() if m else ""

    start = parse_date(field("start"))
    end = parse_date(field("target_end"))
    return {
        "mode": field("mode") or "unknown",
        "name": field("cycle_name") or "—",
        "start": start.isoformat() if start else None,
        "end": end.isoformat() if end else None,
        "day": (TODAY - start).days + 1 if start else None,
        "days_left": (end - TODAY).days if end else None,
        "total_days": (end - start).days + 1 if start and end else None,
        "today": TODAY.isoformat(),
    }


# --------------------------------------------------------------------------
# open review queue
# --------------------------------------------------------------------------

REVIEW_RE = re.compile(
    r"^-\s+(?P<name>.+?)\s+—\s+due:\s*(?P<due>\d{4}-\d{2}-\d{2})\s+—\s+review\s*#(?P<n>\d+)"
    r"\s*(?:—\s*(?P<note>.*))?$"
)


def parse_reviews():
    text = read("DSA", "Progress", "review_schedule.md")
    body = section(text, "Upcoming Reviews")
    items, skipped = [], 0
    for b in bullets(body):
        if b.startswith("- _") or b.startswith("- `"):
            continue
        m = REVIEW_RE.match(b)
        if not m:
            skipped += 1
            warn("unparsed-review", b[:110])
            continue
        name, tags = strip_tags(m.group("name"))
        due = parse_date(m.group("due"))
        overdue = (TODAY - due).days
        note = re.sub(r"\s+", " ", m.group("note") or "").strip()
        items.append({
            "name": name,
            "key": norm(name),
            "due": due.isoformat(),
            "n": int(m.group("n")),
            "tags": tags,
            "overdue_days": overdue,
            "status": "overdue" if overdue > 0 else ("today" if overdue == 0 else "upcoming"),
            "watch": bool(re.search(r"1 more repeat|2nd occurrence|recurrence 2|watch closely",
                                    b, re.I)),
            "opener": find_opener(b),
            "note": note[:220],
        })
    items.sort(key=lambda x: (x["due"], -x["n"]))
    HEALTH["counts"]["reviews_parsed"] = len(items)
    HEALTH["counts"]["reviews_skipped"] = skipped

    graduated = [b for b in bullets(section(text, "Graduated")) if not b.startswith("- _")]
    return items, len(graduated)


# --------------------------------------------------------------------------
# completed review archive  (the retention signal)
# --------------------------------------------------------------------------

ARCHIVE_RE = re.compile(
    r"^-\s+(?P<name>.+?)\s+—\s+review\s*#(?P<n>\d+)\s+—\s+completed:\s*"
    r"(?P<done>\d{4}-\d{2}-\d{2})(?:\s+\d{1,2}:\d{2})?"   # entries may carry HH:MM
    r"\s*(?:—\s*(?P<rest>.*))?$"
)


# Phrases describing a failure that did NOT happen. Stripped before grading, or
# "clean, no repeat of the old rust" scores as a correction. Every misgrade this
# fixes ran the same direction: avoided failures counted as failures.
NEGATED = re.compile(
    r"\b(?:no|not|without|never|avoided|zero)\s+"
    r"(?:a\s+|any\s+|the\s+)?"
    # optional "repeat (of)" prefix, so "no repeat rust" swallows the noun too
    # rather than negating "repeat" and leaving "rust" to score as a failure
    r"(?:repeat(?:s|ed)?(?:\s+of)?\s+)?"
    # up to two words of filler ("no *mechanism* hint given"), but never "idea",
    # since "no idea" is itself a failure signal CORRECTION must still see
    r"(?:(?!idea\b)\w+\s+){0,2}"
    r"(?:hints?|nudges?|escalations?|rust|bugs?|regressions?|errors?|mistakes?|"
    r"slips?|decay|confusion|repeat(?:s|ed)?|missed|misses|gaps?)\b"
    r"|\bno longer\s+\w+"
    r"|\bunprompted\b|\bself-corrected\b|\bdid(?:n't| not)\s+recur\b", re.I)

# "the prior regression point ... held", "the 3x-flagged boundary bug did not
# recur" — a named failure that did NOT happen. The negation trails the noun
# here, so leading-negation stripping misses it. Strip the noun when a
# did-not-happen phrase follows inside the same clause.
HELD = re.compile(
    r"\b(?:regressions?|bugs?|rust|gaps?|points?|cases?|mistakes?|errors?|slips?|"
    r"confusions?|boundary|fix(?:es)?)\b"
    r"(?=[^.;—]{0,70}\b(?:held|did\s?n[o']?t\s+(?:recur|repeat|return)|"
    r"no longer|stayed clean)\b)", re.I)

# An explicit token beats any heuristic. interview-prep-save can emit
# "outcome: clean|hint|correction" and this parser will prefer it.
EXPLICIT = re.compile(r"\boutcome:\s*(clean|hint|correction)\b", re.I)

CORRECTION = re.compile(
    r"\bescalat\w*|\brust\b|\bbugs?\b|\bregress\w*|\bdecay\w*|\bwrong\b|\bfailed\b|"
    r"\bconfus\w*|\bconflat\w*|\bmissed\b|\bno idea\b|\bblank\b|\bcould ?n[o']?t\b|"
    # deliberately NOT "correction" or "gap": both collide with prose about the
    # grading rules themselves ("see mistake_journal grading correction") and with
    # gaps that were closed in-session. Keyword tuning has a ceiling — the
    # explicit `outcome:` token is the real fix.
    r"\bneeded real\b|\bmisidentif\w*|\bnot clean\b|\bslip(?:s|ped)?\b", re.I)
HINT = re.compile(r"\bhints?\b|\bnudges?\b|\bprompted\b|\bpushed\b", re.I)
CLEAN = re.compile(r"\bclean\b|\bheld\b|\bcorrect(?:ly)?\b", re.I)


def classify_outcome(text):
    """Grade a completed review from its log note. Returns (outcome, explicit?)."""
    m = EXPLICIT.search(text)
    if m:
        return m.group(1).lower(), True
    # HELD must run first: NEGATED would otherwise consume the "did not recur"
    # phrase that HELD needs to see trailing its noun.
    t = NEGATED.sub(" ", HELD.sub(" ", text))
    if CORRECTION.search(t):
        return "correction", False
    if HINT.search(t):
        return "hint", False
    if CLEAN.search(t):
        return "clean", False
    return "unknown", False


def parse_archive():
    text = read("DSA", "Progress", "review_log_archive.md")
    done, skipped = [], 0
    for month in re.findall(r"^##\s+\d{4}-\d{2}\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S):
        for b in bullets(month):
            m = ARCHIVE_RE.match(b)
            if not m:
                if b.startswith("- "):
                    skipped += 1
                    warn("unparsed-archive", b[:110])
                continue
            name, tags = strip_tags(m.group("name"))
            rest = m.group("rest") or ""
            due = None
            dm = re.search(r"due was\s*:?\s*(\d{4}-\d{2}-\d{2})", rest)
            if dm:
                due = dm.group(1)
                rest = rest[dm.end():]
            outcome, explicit = classify_outcome(rest)
            done.append({
                "name": name,
                "key": norm(name),
                "n": int(m.group("n")),
                "completed": m.group("done"),
                "due": due,
                "tags": tags,
                "outcome": outcome,
                "explicit": explicit,
            })
    done.sort(key=lambda x: x["completed"])
    HEALTH["counts"]["archive_parsed"] = len(done)
    HEALTH["counts"]["archive_skipped"] = skipped
    HEALTH["counts"]["archive_graded_by_keyword"] = sum(1 for d in done if not d["explicit"])
    if done and not any(d["explicit"] for d in done):
        warn("outcomes-all-heuristic",
             "no review carries an explicit 'outcome:' token — clean rate is inferred "
             "from prose and should be read as approximate")
    return done


# --------------------------------------------------------------------------
# solved problems / session notes
# --------------------------------------------------------------------------

SOLVED_RE = re.compile(r"solved:\s*(independently|with-hints:\s*\w+|failed)", re.I)


def hint_cost(token):
    token = token.lower()
    if token.startswith("independently"):
        return 0
    if token.startswith("failed"):
        return 6
    tail = token.split(":", 1)[1].strip()
    return int(tail) if tail.isdigit() else 5


def parse_solved():
    text = read("DSA", "Progress", "progress.md")
    problems, skipped = [], 0
    for b in bullets(section(text, "Completed Problems")):
        if not b.startswith("- [x]") and not b.startswith("- [ ]"):
            continue
        m = SOLVED_RE.search(b)
        if not m:
            skipped += 1
            warn("problem-missing-solved-field", b[:110])
            continue
        body = b[5:].strip()
        parts = [p.strip() for p in body.split("—")]
        topic = parts[1] if len(parts) > 1 else "—"
        difficulty = parts[2] if len(parts) > 2 else "—"
        name = parts[0]
        problems.append({
            "name": name,
            "key": norm(name),
            "topic": topic.split("/")[0],
            "subtopic": topic,
            "difficulty": difficulty if difficulty in ("Easy", "Medium", "Hard") else "—",
            "hints": hint_cost(m.group(1)),
            "date": (parse_date(b).isoformat() if parse_date(b) else None),
        })
    HEALTH["counts"]["problems_parsed"] = len(problems)
    HEALTH["counts"]["problems_skipped"] = skipped
    return problems


def parse_session_notes():
    text = read("DSA", "Progress", "progress.md")
    dates, threads = set(), []
    for heading in ("Topics Started", "Notes for Next Session"):
        for b in bullets(section(text, heading)):
            d = parse_date(b[:16])
            if d:
                dates.add(d.isoformat())
            for bold in re.findall(r"\*\*(.+?)\*\*", b):
                if re.search(r"resume|untouched|not yet|still due|must open|pick up|code not",
                             bold, re.I):
                    clean = re.sub(r"\s+", " ", bold).strip(" .*")
                    if 20 < len(clean) < 400:
                        threads.append({"date": d.isoformat() if d else None, "text": clean})
    return sorted(dates), threads[-6:]


# --------------------------------------------------------------------------
# mistakes
# --------------------------------------------------------------------------

def parse_mistakes():
    text = read("DSA", "mistakes", "mistake_journal.md")
    entries = []
    for chunk in re.split(r"^###\s+", section(text, "Log"), flags=re.M)[1:]:
        head, _, rest = chunk.partition("\n")
        date = parse_date(head)
        title = head.split("—", 1)[1].strip() if "—" in head else head.strip()

        def field(name):
            m = re.search(rf"^-\s*{name}:\s*(.+?)(?=^-\s*\w[\w\- ]*:|\Z)", rest, re.M | re.S)
            return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""

        cls, inferred = field("Class"), False
        if not cls:
            inferred = True
            blob = (field("Mistake") + " " + field("Root Cause")).lower()
            if re.search(r"code|first draft|implementation", blob):
                cls = "code-vs-derivation"
            elif re.search(r"boundary|post-loop|off-by-one|edge case|last element", blob):
                cls = "boundary"
            elif re.search(r"rust|decay|memoriz|recall", blob):
                cls = "stale-recall"
            elif re.search(r"reus|transfer|pattern-match|didn't transfer", blob):
                cls = "transfer-gap"
            else:
                cls = "invariant-why"
        rec = field("Recurrence")
        m = re.match(r"(\d+)", rec)
        rec_n = int(m.group(1)) if m else (
            2 if re.search(r"2nd|twice|3rd|3\+", title + " " + rest, re.I) else 1)
        pattern = field("Pattern") or field("Topic Area")
        entries.append({
            "date": date.isoformat() if date else None,
            "title": title,
            "cls": cls,
            "inferred": inferred,
            "recurrence": rec_n,
            "pattern": re.sub(r"\[\[.*?\]\]\s*|\(`?[^)]*`?\)", "", pattern).split("—")[0].strip(" .`"),
        })
    entries.sort(key=lambda e: e["date"] or "")
    HEALTH["counts"]["mistakes_parsed"] = len(entries)
    HEALTH["counts"]["mistakes_class_inferred"] = sum(1 for e in entries if e["inferred"])
    return entries


# --------------------------------------------------------------------------
# other tracks
# --------------------------------------------------------------------------

def parse_tracks():
    dash = read("Progress", "dashboard.md")
    rows = []
    for line in section(dash, "Track Readiness").splitlines():
        line = line.strip()
        if not line or line.startswith("_"):
            continue
        parts = line.split(None, 1)
        if len(parts) == 2 and parts[0][0].isupper():
            rows.append({"track": parts[0], "detail": parts[1].split("·")[0].strip()})
    sd = read("SystemDesign", "Progress", "progress.md")
    cases = re.findall(r"^-\s*\[([ x])\]\s*(.+)$", section(sd, "Case Study Sheet"), re.M)
    return rows, {"done": sum(1 for c, _ in cases if c == "x"), "total": len(cases)}


# --------------------------------------------------------------------------
# derived: backlog history, session batch, analysis
# --------------------------------------------------------------------------

def backlog_history(cycle, reviews, archive):
    """Reconstruct open-review-count per day from due dates and completion dates.

    Archived items with no recorded 'due was' are assumed done on time, so they
    never count as backlog — this biases the early curve low. Labelled as
    approximate on the page.
    """
    if not cycle["start"]:
        return []
    start = dt.date.fromisoformat(cycle["start"])
    series, d = [], start
    while d <= TODAY:
        iso = d.isoformat()
        open_now = sum(1 for r in reviews if r["due"] <= iso)
        open_then = sum(1 for a in archive
                        if a["due"] and a["due"] <= iso < a["completed"])
        series.append({"date": iso, "open": open_now + open_then})
        d += dt.timedelta(days=1)
    return series


def build_batch(reviews, problems, cap):
    """Compose the next Block B batch under the tracker's own rules:
    oldest-due first, leech/watch items pulled forward, [derive] prioritised,
    and never two consecutive problems from the same subtopic."""
    sub = {p["key"]: p["subtopic"] for p in problems}
    pool = [dict(r, subtopic=sub.get(r["key"], "—"))
            for r in reviews if r["status"] in ("overdue", "today")]
    pool.sort(key=lambda r: (r["due"],
                             0 if (r["watch"] or "leech" in r["tags"]) else 1,
                             0 if "derive" in r["tags"] else 1,
                             -r["n"]))
    picked, ordered, last, collisions = pool[:cap], [], None, 0
    remaining = list(picked)
    while remaining:
        nxt = next((r for r in remaining if r["subtopic"] != last), None)
        if nxt is None:
            nxt = remaining[0]
            collisions += 1
        remaining.remove(nxt)
        ordered.append(nxt)
        last = nxt["subtopic"]
    return {
        "items": ordered,
        "collisions": collisions,
        "rollover": max(0, len(pool) - cap),
        "unmatched_subtopic": sum(1 for r in ordered if r["subtopic"] == "—"),
    }


def analyse(cycle, reviews, archive, problems, mistakes, active_days, cases):
    cap = CONFIG["session_review_cap"]
    overdue = [r for r in reviews if r["status"] == "overdue"]
    due_today = [r for r in reviews if r["status"] == "today"]
    backlog = overdue + due_today

    buckets = {}
    for r in backlog:
        buckets.setdefault(r["due"], []).append(r)
    tiers = [{"due": d, "count": len(v),
              "overdue_days": max(x["overdue_days"] for x in v),
              "derive": sum(1 for x in v if "derive" in x["tags"])}
             for d, v in sorted(buckets.items())]

    by_day = {}
    for p in problems:
        if p["date"]:
            by_day.setdefault(p["date"], []).append(p["hints"])
    trend = [{"date": d, "mean": round(sum(v) / len(v), 2), "n": len(v)}
             for d, v in sorted(by_day.items())]

    # review outcomes over time — the actual retention signal
    out_by_day = {}
    for a in archive:
        slot = out_by_day.setdefault(a["completed"], {"clean": 0, "hint": 0,
                                                      "correction": 0, "unknown": 0})
        slot[a["outcome"]] += 1
    outcomes = [dict(date=d, **v) for d, v in sorted(out_by_day.items())]
    totals = {k: sum(o[k] for o in outcomes) for k in ("clean", "hint", "correction", "unknown")}
    graded = sum(totals[k] for k in ("clean", "hint", "correction"))
    clean_rate = round(100 * totals["clean"] / graded) if graded else 0

    # Does the interval ladder actually work? Clean rate by review number answers the
    # one question spaced repetition needs answered, and tests the dashboard's own
    # claim that [derive] items decay fastest.
    def rate(subset):
        g = [a for a in subset if a["outcome"] != "unknown"]
        return {"n": len(g),
                "clean": round(100 * sum(1 for a in g if a["outcome"] == "clean") / len(g))
                if g else None}

    by_number = [dict(label=f"review #{n}", **rate([a for a in archive if a["n"] == n]))
                 for n in sorted({a["n"] for a in archive})]
    by_tag = [
        dict(label="[derive] items", **rate([a for a in archive if "derive" in a["tags"]])),
        dict(label="untagged items", **rate([a for a in archive if not a["tags"]])),
    ]

    # repeat offenders: same problem needing a non-clean review more than once
    repeats = {}
    for a in archive:
        if a["outcome"] in ("hint", "correction"):
            repeats.setdefault(a["name"], []).append(f"#{a['n']} {a['completed']}")
    repeat_offenders = sorted(((k, v) for k, v in repeats.items() if len(v) > 1),
                              key=lambda kv: -len(kv[1]))[:6]

    # All-time class counts make a weakness look permanent even after it stops
    # recurring — split recent from earlier so a fixed problem can read as fixed.
    cutoff = (TODAY - dt.timedelta(days=14)).isoformat()
    cls_counts, cls_recent, pat_counts = {}, {}, {}
    for m in mistakes:
        cls_counts[m["cls"]] = cls_counts.get(m["cls"], 0) + 1
        if (m["date"] or "") >= cutoff:
            cls_recent[m["cls"]] = cls_recent.get(m["cls"], 0) + 1
        if m["pattern"]:
            pat_counts[m["pattern"]] = pat_counts.get(m["pattern"], 0) + 1

    span = cycle["day"] or len(active_days)
    show_rate = round(100 * len(active_days) / span) if span else 0

    est = {
        "reviews": len(backlog) * CONFIG["hours"]["review"],
        "graph_remaining": CONFIG["graph_algos_remaining"] * CONFIG["hours"]["graph_algo_remaining"],
        "import_backlog": CONFIG["import_backlog_remaining"] * CONFIG["hours"]["import_backlog_item"],
        "system_design": (cases["total"] - cases["done"]) * CONFIG["hours"]["system_design_case"],
        "lld_behavioral_java": 3 * CONFIG["hours"]["zero_track_bootstrap"],
    }
    total_hours = round(sum(est.values()))
    days_left = max(cycle["days_left"] or 1, 1)
    # Most of the scope total comes from CONFIG constants, not from disk. Report it
    # as a three-state feasibility call at 5h granularity rather than a decimal that
    # claims accuracy the constants can't support — and divide by the days actually
    # worked, since show rate is sitting right there.
    active_left = max(round(days_left * show_rate / 100), 1)
    per_active = total_hours / active_left
    feasibility = ("not feasible as scoped" if per_active > 5
                   else "tight" if per_active > 2.5 else "feasible")
    parsed_hours = round(est["reviews"] + est["system_design"])

    return {
        "overdue": len(overdue), "due_today": len(due_today), "backlog": len(backlog),
        "upcoming": len(reviews) - len(backlog),
        "sessions_to_clear": -(-len(backlog) // cap) if backlog else 0,
        "cap": cap, "tiers": tiers,
        "oldest_overdue": max((r["overdue_days"] for r in backlog), default=0),
        "derive_in_backlog": sum(1 for r in backlog if "derive" in r["tags"]),
        "leech_watch": [r for r in reviews if r["watch"] or "leech" in r["tags"]],
        "trend": trend, "outcomes": outcomes, "outcome_totals": totals,
        "clean_rate": clean_rate, "reviews_completed": len(archive),
        "reviews_graded": graded,
        "explicit_grades": sum(1 for a in archive if a["explicit"]),
        "by_number": by_number, "by_tag": by_tag,
        "repeat_offenders": repeat_offenders,
        "cls_recent": cls_recent, "cls_cutoff": cutoff,
        "cls_counts": dict(sorted(cls_counts.items(), key=lambda kv: -kv[1])),
        "pat_counts": dict(sorted(pat_counts.items(), key=lambda kv: -kv[1])[:8]),
        "repeat_mistakes": [m for m in mistakes if m["recurrence"] >= 2],
        "active_days": active_days, "show_rate": show_rate,
        "independent_rate": round(100 * sum(1 for p in problems if p["hints"] == 0)
                                  / len(problems)) if problems else 0,
        "est_hours": int(round(total_hours / 5.0) * 5),
        "parsed_hours": parsed_hours,
        "active_days_left": active_left,
        "feasibility": feasibility,
        "per_active_day": round(per_active, 1),
        "est_breakdown": {k: round(v, 1) for k, v in est.items()},
    }


def build_verdict(cycle, A, tracks, cases, snapshots):
    """Which constraint binds depends on where in the cycle you are.

    A loop is scored on its weakest round, not its average, so once the window is
    short and a track is still at zero, breadth outranks polish — however large the
    review queue is. Triggering on queue size alone (the earlier rule) starves new
    material in exactly the window where a missing track is unrecoverable and a
    slipped review costs a few points of retention.
    """
    zero = [t["track"] for t in tracks if re.match(r"^0 |not started", t["detail"])]
    days_left = cycle["days_left"] or 999
    endgame = days_left <= 14 and len(zero) >= 1
    miss = round(100 - A["clean_rate"])

    steps = []
    if endgame:
        keep = [r for r in A["leech_watch"]][:5]
        steps.append(f"Cap reviews at ~5 this session, not {A['cap']}: the leech and watch "
                     f"items only ({len(keep)} of them right now). The rest of the queue is "
                     "mostly problems already clean at review #3 — slipping those a few days "
                     "costs retention, not the interview.")
        steps.append(f"Give the rest of the session to {', '.join(zero[:2])}. "
                     f"{len(zero)} tracks at zero with {days_left} days left is the "
                     "unrecoverable gap; the review queue is not.")
        if cases["done"] == 0 and cases["total"]:
            steps.append(f"Book one System Design case study now — 0 of {cases['total']} "
                         "attempted, and it is the second-most-weighted round after coding.")
        if A["derive_in_backlog"]:
            steps.append(f"Of whatever reviews you do run, take <code>[derive]</code> items "
                         f"first ({A['derive_in_backlog']} in the queue).")
    else:
        if A["backlog"] > A["cap"]:
            steps.append(f"Open with Block B. {A['backlog']} reviews due against a "
                         f"{A['cap']}-per-session cap — {A['sessions_to_clear']} sessions of "
                         "pure review to level the queue, and it grows with every new problem.")
        if A["derive_in_backlog"]:
            steps.append(f"Front-load the {A['derive_in_backlog']} <code>[derive]</code> items.")
        if zero:
            steps.append(f"Spend the +15 on {zero[0]}. {len(zero)} tracks sit at zero.")

    growth = ""
    if len(snapshots) >= 2:
        d = snapshots[-1]["backlog"] - snapshots[0]["backlog"]
        if d:
            growth = (f" Across {len(snapshots)} recorded snapshots the backlog has "
                      f"{'grown' if d > 0 else 'shrunk'} by {abs(d)}.")

    grading = ("" if A["explicit_grades"] else
               " Outcomes are graded from prose, not an explicit field, so treat that "
               "rate as approximate.")

    if endgame:
        head = "Breadth is the binding constraint now, not review debt"
        body = (f"{days_left} days left and {len(zero)} tracks still at zero "
                f"({', '.join(zero)}). An interview loop is scored on its weakest round, so "
                f"the marginal hour is worth more on a track that would currently score zero "
                f"than on the {A['backlog']}-item review queue, where "
                f"{A['clean_rate']}% of re-tests already come back clean.{growth} "
                f"Scope remaining is <strong>{A['feasibility']}</strong> — roughly "
                f"{A['est_hours']}h against about {A['active_days_left']} days you'll "
                f"actually work at a {A['show_rate']}% show rate.{grading}")
    elif A["backlog"] > A["cap"]:
        head = "Review debt is the binding constraint"
        body = (f"{A['backlog']} reviews due, oldest by {A['oldest_overdue']} days, with "
                f"{days_left} days left.{growth} Re-tests come back clean "
                f"{A['clean_rate']}% of the time, so about {miss}% of the queue is hiding "
                f"something real. Scope remaining is <strong>{A['feasibility']}</strong>: "
                f"~{A['est_hours']}h against about {A['active_days_left']} working days at a "
                f"{A['show_rate']}% show rate.{grading}")
    else:
        head = "Queue is level — spend the session on new material"
        body = (f"{A['backlog']} reviews due, clearable in one session. {days_left} days "
                f"left, ~{A['est_hours']}h scope, <strong>{A['feasibility']}</strong> at a "
                f"{A['show_rate']}% show rate. Clean rate {A['clean_rate']}%.{grading}")
    return {"head": head, "body": body, "steps": steps, "endgame": endgame}


def load_snapshots():
    """Real per-run snapshots — unlike the reconstructed curve, these aren't inferred."""
    path = os.path.join(ROOT, "Progress", "metrics_history.jsonl")
    rows = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    try:
                        rows.append(json.loads(line))
                    except json.JSONDecodeError:
                        warn("bad-history-row", line[:80])
    return sorted(rows, key=lambda r: r.get("date", ""))


def append_history(analysis, enabled):
    """Snapshot per run so future trends survive markdown that can't be replayed."""
    if not enabled:
        return
    path = os.path.join(ROOT, "Progress", "metrics_history.jsonl")
    row = {"date": TODAY.isoformat(), "backlog": analysis["backlog"],
           "overdue": analysis["overdue"], "clean_rate": analysis["clean_rate"],
           "reviews_completed": analysis["reviews_completed"],
           "show_rate": analysis["show_rate"],
           "independent_rate": analysis["independent_rate"]}
    lines = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            lines = [l for l in fh.read().splitlines()
                     if l.strip() and json.loads(l).get("date") != row["date"]]
    lines.append(json.dumps(row))
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


# --------------------------------------------------------------------------
# render
# --------------------------------------------------------------------------

HTML = r"""<title>Prep Signal — interview prep tracker</title>
<style>
:root {
  --ground:#EFF2F0; --surface:#FFFFFF; --sunk:#E4E9E6;
  --ink:#101619; --muted:#5C6A66; --line:#D5DCD8;
  --accent:#136B66; --accent-soft:#D5E7E4;
  --crit:#A63D28; --crit-soft:#F2DED8;
  --warn:#8F6410; --warn-soft:#F3E7CE;
  --good:#37764B; --good-soft:#DCEBDF;
  --display:"Iowan Old Style","Charter","Palatino Linotype",Palatino,Georgia,serif;
  --body:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono:ui-monospace,"SF Mono",SFMono-Regular,Menlo,Consolas,monospace;
  --r:3px;
}
@media (prefers-color-scheme: dark) {
  :root {
    --ground:#0D1214; --surface:#141B1D; --sunk:#101719;
    --ink:#E2E9E5; --muted:#8B9A94; --line:#25302E;
    --accent:#54B6AC; --accent-soft:#17332F;
    --crit:#E2805F; --crit-soft:#38201A;
    --warn:#D6A241; --warn-soft:#332715;
    --good:#6DBC82; --good-soft:#16301D;
  }
}
:root[data-theme="dark"] {
  --ground:#0D1214; --surface:#141B1D; --sunk:#101719;
  --ink:#E2E9E5; --muted:#8B9A94; --line:#25302E;
  --accent:#54B6AC; --accent-soft:#17332F;
  --crit:#E2805F; --crit-soft:#38201A;
  --warn:#D6A241; --warn-soft:#332715;
  --good:#6DBC82; --good-soft:#16301D;
}
:root[data-theme="light"] {
  --ground:#EFF2F0; --surface:#FFFFFF; --sunk:#E4E9E6;
  --ink:#101619; --muted:#5C6A66; --line:#D5DCD8;
  --accent:#136B66; --accent-soft:#D5E7E4;
  --crit:#A63D28; --crit-soft:#F2DED8;
  --warn:#8F6410; --warn-soft:#F3E7CE;
  --good:#37764B; --good-soft:#DCEBDF;
}

body { background:var(--ground); color:var(--ink); font-family:var(--body);
  font-size:15px; line-height:1.55; -webkit-font-smoothing:antialiased; }
.wrap { max-width:1120px; margin:0 auto; padding:40px 24px 80px;
  display:flex; flex-direction:column; gap:28px; }

.mast { display:flex; flex-wrap:wrap; align-items:flex-end; justify-content:space-between;
  gap:20px; border-bottom:2px solid var(--ink); padding-bottom:16px; }
.mast h1 { font-family:var(--display); font-size:38px; line-height:1.05; font-weight:600;
  letter-spacing:-0.015em; text-wrap:balance; margin:0; }
.mast .sub { color:var(--muted); font-size:13px; margin-top:6px; }
.stamp { font-family:var(--mono); font-size:11px; color:var(--muted);
  text-align:right; letter-spacing:0.04em; }

.strip { display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
  gap:1px; background:var(--line); border:1px solid var(--line); }
.cell { background:var(--surface); padding:14px 16px; display:flex; flex-direction:column; gap:3px; }
.cell .k { font-size:10.5px; text-transform:uppercase; letter-spacing:0.09em; color:var(--muted); }
.cell .v { font-family:var(--mono); font-size:26px; font-variant-numeric:tabular-nums;
  line-height:1.1; }
.cell .n { font-size:11.5px; color:var(--muted); }
.cell.alert .v { color:var(--crit); }
.cell.warn .v { color:var(--warn); }
.cell.good .v { color:var(--good); }
.track { height:5px; background:var(--sunk); position:relative; overflow:hidden; }
.track i { position:absolute; inset:0 auto 0 0; background:var(--accent); }

.grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(330px,1fr)); gap:20px; }
.panel { background:var(--surface); border:1px solid var(--line);
  padding:18px 20px 20px; display:flex; flex-direction:column; gap:12px; }
.panel.wide { grid-column:1/-1; }
.panel > header { display:flex; align-items:baseline; justify-content:space-between; gap:12px;
  border-bottom:1px solid var(--line); padding-bottom:9px; flex-wrap:wrap; }
.panel h2 { font-family:var(--display); font-size:18px; font-weight:600; margin:0;
  letter-spacing:-0.01em; }
.panel .hint { font-size:11px; color:var(--muted); font-family:var(--mono); }
.lede { font-size:13.5px; color:var(--muted); margin:0; max-width:64ch; }

.verdict { border-left:4px solid var(--crit); background:var(--crit-soft);
  padding:16px 20px; display:flex; flex-direction:column; gap:8px; }
.verdict h2 { font-family:var(--display); font-size:20px; margin:0; }
.verdict p { margin:0; font-size:14px; max-width:74ch; }
.verdict ol { margin:4px 0 0; padding-left:20px; font-size:14px; }
.verdict li { margin-bottom:4px; }
.verdict code { font-family:var(--mono); font-size:12.5px; }

.tier { display:grid; grid-template-columns:88px 1fr 42px; align-items:center; gap:12px;
  font-size:13px; }
.tier .d { font-family:var(--mono); font-size:12px; color:var(--muted);
  font-variant-numeric:tabular-nums; }
.tier .bar { height:20px; background:var(--sunk); position:relative; }
.tier .bar i { position:absolute; inset:0 auto 0 0; }
.tier .bar b { position:absolute; inset:0 auto 0 0; opacity:0.55;
  background:repeating-linear-gradient(45deg,transparent 0 3px,currentColor 3px 4px); }
.tier .c { font-family:var(--mono); font-size:13px; text-align:right;
  font-variant-numeric:tabular-nums; }
.sev-3 i { background:var(--crit); } .sev-3 b { color:var(--crit); }
.sev-2 i { background:var(--warn); } .sev-2 b { color:var(--warn); }
.sev-1 i { background:var(--accent); } .sev-1 b { color:var(--accent); }

.rows { display:flex; flex-direction:column; }
.row { display:grid; grid-template-columns:1fr auto; gap:12px; align-items:baseline;
  padding:7px 0; border-bottom:1px solid var(--line); font-size:13.5px; }
.row:last-child { border-bottom:0; }
.row .m { font-family:var(--mono); font-size:12px; color:var(--muted);
  font-variant-numeric:tabular-nums; }
.pill { font-family:var(--mono); font-size:10px; text-transform:uppercase;
  letter-spacing:0.07em; padding:1.5px 6px; border-radius:var(--r); white-space:nowrap; }
.p-crit { background:var(--crit-soft); color:var(--crit); }
.p-warn { background:var(--warn-soft); color:var(--warn); }
.p-good { background:var(--good-soft); color:var(--good); }
.p-acc  { background:var(--accent-soft); color:var(--accent); }
.tags { display:inline-flex; gap:5px; margin-left:7px; vertical-align:middle; }

/* batch */
.batch { display:flex; flex-direction:column; counter-reset:step; }
.step { display:grid; grid-template-columns:26px 1fr auto; gap:12px; padding:10px 0;
  border-bottom:1px solid var(--line); align-items:baseline; }
.step:last-child { border-bottom:0; }
.step .i { font-family:var(--mono); font-size:12px; color:var(--muted);
  font-variant-numeric:tabular-nums; }
.step .nm { font-size:14px; }
.step .op { font-size:12.5px; color:var(--muted); margin-top:3px;
  border-left:2px solid var(--accent); padding-left:9px; max-width:70ch; }
.step .sub { font-family:var(--mono); font-size:11px; color:var(--muted); margin-top:3px; }
.step .r { text-align:right; }

.blist { display:flex; flex-direction:column; gap:8px; }
.b { display:grid; grid-template-columns:1fr 44px; gap:10px; align-items:center; font-size:13px; }
.b .lab { display:flex; flex-direction:column; gap:4px; }
.b .meter { height:7px; background:var(--sunk); }
.b .meter i { display:block; height:100%; background:var(--accent); }
.b .n { font-family:var(--mono); font-size:12.5px; text-align:right;
  font-variant-numeric:tabular-nums; color:var(--muted); }

.cal { display:flex; flex-wrap:wrap; gap:3px; }
.cal span { width:15px; height:15px; background:var(--sunk); border-radius:1px; }
.cal span.on { background:var(--accent); }
.cal span.future { background:transparent; border:1px dashed var(--line); }
.legend { display:flex; gap:14px; font-size:11.5px; color:var(--muted); flex-wrap:wrap; }
.legend i { display:inline-block; width:9px; height:9px; margin-right:5px; }

.scroll { overflow-x:auto; }
table { border-collapse:collapse; width:100%; font-size:13px; }
th { text-align:left; font-size:10.5px; text-transform:uppercase; letter-spacing:0.08em;
  color:var(--muted); font-weight:600; padding:0 12px 7px 0; border-bottom:1px solid var(--line); }
td { padding:7px 12px 7px 0; border-bottom:1px solid var(--line); vertical-align:top; }
tr:last-child td { border-bottom:0; }
td.num { font-family:var(--mono); font-variant-numeric:tabular-nums; text-align:right;
  padding-right:0; }
td.m { font-family:var(--mono); font-size:12px; color:var(--muted);
  font-variant-numeric:tabular-nums; white-space:nowrap; }

.filters { display:flex; gap:6px; flex-wrap:wrap; }
.filters button { font-family:var(--mono); font-size:11px; text-transform:uppercase;
  letter-spacing:0.06em; padding:4px 10px; background:transparent; color:var(--muted);
  border:1px solid var(--line); border-radius:var(--r); cursor:pointer; }
.filters button:hover { color:var(--ink); border-color:var(--muted); }
.filters button[aria-pressed="true"] { background:var(--accent); color:var(--surface);
  border-color:var(--accent); }
.filters button:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }

svg { display:block; width:100%; height:auto; overflow:visible; }
.ax { font-family:var(--mono); font-size:9px; fill:var(--muted); }

.divider { display:flex; align-items:center; gap:14px; color:var(--muted);
  font-family:var(--mono); font-size:11px; text-transform:uppercase; letter-spacing:0.08em; }
.divider::before, .divider::after { content:""; flex:1; height:1px; background:var(--line); }

.b .meter i.recent { background:var(--crit); }
.b .meter { position:relative; }
.b .meter i.overlay { position:absolute; inset:0 auto 0 0; }

.health { font-size:12.5px; display:flex; flex-direction:column; gap:6px; }
.health .ok { color:var(--good); }
.health .bad { color:var(--crit); }
.health ul { margin:4px 0 0; padding-left:18px; color:var(--muted); font-size:12px; }
.health code { font-family:var(--mono); font-size:11.5px; }

.foot { font-size:12px; color:var(--muted); border-top:1px solid var(--line);
  padding-top:14px; }
.foot code { font-family:var(--mono); font-size:11.5px; background:var(--sunk);
  padding:1px 5px; border-radius:var(--r); }
@media (max-width:560px) {
  .mast h1 { font-size:29px; }
  .wrap { padding:26px 16px 60px; }
  .step { grid-template-columns:22px 1fr; }
  .step .r { grid-column:2; text-align:left; }
}
@media (prefers-reduced-motion:reduce) { * { transition:none !important; animation:none !important; } }
</style>

<div class="wrap">
  <header class="mast">
    <div>
      <h1>Prep Signal</h1>
      <div class="sub" id="subtitle"></div>
    </div>
    <div class="stamp" id="stamp"></div>
  </header>

  <section class="strip" id="strip"></section>
  <section class="verdict" id="verdict"></section>

  <section class="panel wide">
    <header><h2>Next session's Block B</h2><span class="hint" id="batch-hint"></span></header>
    <p class="lede">Built from the queue under the tracker's own rules: oldest due first,
      leech and watch items pulled forward, <code>[derive]</code> ahead of plain reviews, and
      no two consecutive problems from the same subtopic. Where the schedule already records
      the question a review must open with, it is quoted.</p>
    <div class="batch" id="batch"></div>
  </section>

  <section class="panel wide">
    <header><h2>Threads left mid-air</h2><span class="hint">from progress.md</span></header>
    <p class="lede">Sessions that ended inside a derivation. Cheaper to close now than to
      rebuild cold later.</p>
    <div class="rows" id="threads"></div>
  </section>

  <div class="grid">
    <section class="panel">
      <header><h2>One repeat from a leech</h2><span class="hint">recurrence ≥ 2</span></header>
      <p class="lede">Same specific point already corrected twice. A third pulls it off the
        interval ladder onto daily recall.</p>
      <div class="rows" id="leech"></div>
    </section>

    <section class="panel">
      <header><h2>Problems that keep failing review</h2><span class="hint">non-clean ≥ 2</span></header>
      <p class="lede">Not the same as a leech — this counts any review that needed help, across
        the whole archive.</p>
      <div class="rows" id="offenders"></div>
    </section>
  </div>

  <div class="divider"><span>Below here is weekly-audit material — not needed before a session</span></div>

  <div class="grid">
    <section class="panel">
      <header><h2>Is the ladder working?</h2><span class="hint" id="ladder-hint"></span></header>
      <p class="lede">Clean rate by review number, then by tag. If later reviews are not
        cleaner than earlier ones, the intervals are wrong. The second pair tests this
        page's own claim that <code>[derive]</code> items decay fastest.</p>
      <div class="blist" id="ladder"></div>
    </section>

    <section class="panel">
      <header><h2>Review outcomes</h2><span class="hint" id="out-hint"></span></header>
      <p class="lede">Every completed review, graded from its own log note.</p>
      <div id="outcomes"></div>
      <div class="legend">
        <span><i style="background:var(--good)"></i>clean</span>
        <span><i style="background:var(--warn)"></i>needed a hint</span>
        <span><i style="background:var(--crit)"></i>real correction</span>
      </div>
    </section>

    <section class="panel">
      <header><h2>What actually goes wrong</h2><span class="hint" id="class-hint"></span></header>
      <p class="lede">Mistakes by failure class. The inner bar is the last 14 days — a
        weakness that stopped recurring should stop reading as current.</p>
      <div class="blist" id="classes"></div>
    </section>

    <section class="panel">
      <header><h2>Patterns that keep biting</h2><span class="hint">mistakes logged</span></header>
      <p class="lede">Ranked by how often a mistake traced back to that pattern.</p>
      <div class="blist" id="patterns"></div>
    </section>

    <section class="panel">
      <header><h2>Track balance</h2><span class="hint" id="track-hint"></span></header>
      <p class="lede">A loop is scored on its weakest round, not its average.</p>
      <div class="rows" id="tracks"></div>
    </section>

    <section class="panel">
      <header><h2>Show rate</h2><span class="hint" id="cal-hint"></span></header>
      <p class="lede">Days with logged activity since the cycle started.</p>
      <div class="cal" id="cal"></div>
      <div class="legend">
        <span><i style="background:var(--accent)"></i>logged</span>
        <span><i style="background:var(--sunk)"></i>silent</span>
        <span><i style="border:1px dashed var(--line)"></i>ahead</span>
      </div>
    </section>
  </div>

  <section class="panel wide">
    <header><h2>Review debt, by the day it came due</h2>
      <span class="hint" id="tier-hint"></span></header>
    <p class="lede">Solid bar = items past due. Hatched = the <code>[derive]</code> share.</p>
    <div id="tiers"></div>
  </section>

  <section class="panel wide">
    <header><h2>Full review queue</h2>
      <div class="filters" id="filters">
        <button data-f="all" aria-pressed="true">all</button>
        <button data-f="overdue" aria-pressed="false">overdue</button>
        <button data-f="derive" aria-pressed="false">derive</button>
        <button data-f="upcoming" aria-pressed="false">upcoming</button>
      </div></header>
    <div class="scroll"><table id="queue"></table></div>
  </section>

  <section class="panel wide">
    <header><h2>Data health</h2><span class="hint">parser self-check</span></header>
    <p class="lede">Every number on this page is regex-parsed from markdown. If a tracker
      entry stops matching its expected shape it silently disappears — this panel is how
      that gets caught.</p>
    <div class="health" id="health"></div>
  </section>

  <footer class="foot" id="foot"></footer>
</div>

<script>
const D = __DATA__;
// returns a detached node when a panel is absent, so removing markup can
// never throw and take the rest of the page's rendering with it
const $ = id => document.getElementById(id) || document.createElement('div');
const el = (t, c, h) => { const n = document.createElement(t);
  if (c) n.className = c; if (h !== undefined) n.innerHTML = h; return n; };
const esc = s => String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const plural = (n, w) => n + " " + w + (n === 1 ? "" : "s");
const A = D.analysis;

$("subtitle").textContent = D.cycle.mode === "sprint"
  ? `Cycle ${D.cycle.name} · day ${D.cycle.day} of ${D.cycle.total_days} · ends ${D.cycle.end}`
  : `Cycle ${D.cycle.name} · ${D.cycle.mode} mode`;
$("stamp").innerHTML = `generated ${D.cycle.today}<br>${D.meta.files} tracker files parsed`;

/* strip */
[
  { k:"Days left", v:D.cycle.days_left, n:`of ${D.cycle.total_days}`,
    sev:D.cycle.days_left <= 14 ? "warn" : "", bar:1 - D.cycle.days_left / D.cycle.total_days },
  { k:"Reviews due now", v:A.backlog, n:`${A.sessions_to_clear} sessions at ${A.cap}/session`,
    sev:A.backlog > 20 ? "alert" : A.backlog > 8 ? "warn" : "" },
  { k:"Oldest overdue", v:A.oldest_overdue + "d", n:`${A.derive_in_backlog} are [derive]`,
    sev:A.oldest_overdue >= 3 ? "alert" : A.oldest_overdue > 0 ? "warn" : "" },
  { k:"Clean review rate", v:A.clean_rate + "%", n:`${A.reviews_graded} of ${A.reviews_completed} graded`,
    sev:A.clean_rate >= 70 ? "good" : A.clean_rate >= 50 ? "warn" : "alert" },
  { k:"Solved cold", v:A.independent_rate + "%", n:`${D.problems.length} problems logged`,
    sev:A.independent_rate < 40 ? "warn" : "" },
  { k:"Show rate", v:A.show_rate + "%", n:`${A.active_days.length} active days`,
    sev:A.show_rate < 60 ? "warn" : "" },
  { k:"Scope remaining", v:A.feasibility.split(" ")[0], n:`~${A.est_hours}h over ~${A.active_days_left} working days`,
    sev:A.feasibility.startsWith("not") ? "alert" : A.feasibility === "tight" ? "warn" : "good" },
].forEach(c => {
  const n = el("div", "cell " + (c.sev || ""));
  n.append(el("span", "k", esc(c.k)), el("span", "v", esc(c.v)), el("span", "n", esc(c.n)));
  if (c.bar !== undefined) {
    const t = el("div", "track"), i = el("i");
    i.style.width = Math.max(0, Math.min(100, c.bar * 100)) + "%";
    t.appendChild(i); n.appendChild(t);
  }
  $("strip").appendChild(n);
});

$("verdict").innerHTML = `<h2>${esc(D.verdict.head)}</h2><p>${D.verdict.body}</p>
  <ol>${D.verdict.steps.map(s => `<li>${s}</li>`).join("")}</ol>`;

/* batch */
const B = D.batch;
$("batch-hint").textContent =
  `${B.items.length} of ${B.items.length + B.rollover} due · ${B.rollover} roll over`;
B.items.forEach((r, i) => {
  const tags = r.tags.map(t =>
    `<span class="pill ${t === "leech" ? "p-crit" : "p-acc"}">${t}</span>`).join(" ");
  const watch = r.watch && !r.tags.includes("leech")
    ? '<span class="pill p-warn">2 of 3</span>' : "";
  const step = el("div", "step");
  step.append(el("div", "i", String(i + 1).padStart(2, "0")));
  const mid = el("div");
  mid.appendChild(el("div", "nm",
    `${esc(r.name)} <span class="tags">${tags} ${watch}</span>`));
  if (r.opener) mid.appendChild(el("div", "op", "Open with: " + esc(r.opener)));
  mid.appendChild(el("div", "sub",
    `${esc(r.subtopic)} · review #${r.n} · due ${r.due}` +
    (r.overdue_days > 0 ? ` · ${r.overdue_days}d late` : "")));
  step.appendChild(mid);
  step.appendChild(el("div", "r",
    r.overdue_days > 0 ? `<span class="pill p-crit">${r.overdue_days}d</span>`
                       : '<span class="pill p-warn">today</span>'));
  $("batch").appendChild(step);
});
if (B.collisions) {
  $("batch").appendChild(el("div", "step",
    `<div class="i">!</div><div class="sub">${B.collisions} adjacent pair(s) share a subtopic —
     the queue is too Arrays-heavy to alternate fully.</div><div></div>`));
}

/* tiers */
const maxTier = Math.max(1, ...A.tiers.map(t => t.count));
$("tier-hint").textContent = plural(A.backlog, "item") + " across " + plural(A.tiers.length, "tier");
A.tiers.forEach(t => {
  const sev = t.overdue_days >= 3 ? 3 : t.overdue_days >= 1 ? 2 : 1;
  const row = el("div", "tier sev-" + sev);
  row.appendChild(el("div", "d",
    t.due + (t.overdue_days > 0 ? ` <span style="opacity:.7">+${t.overdue_days}d</span>` : "")));
  const bar = el("div", "bar"), i = el("i"), b = el("b");
  i.style.width = (t.count / maxTier * 100) + "%";
  b.style.width = (t.derive / maxTier * 100) + "%";
  bar.append(i, b); row.append(bar, el("div", "c", t.count));
  $("tiers").appendChild(row);
});

/* outcomes stacked bars */
(function () {
  const o = A.outcomes; if (!o.length) return;
  $("out-hint").textContent =
    `${A.outcome_totals.clean} clean · ${A.outcome_totals.hint} hint · ${A.outcome_totals.correction} correction`;
  const W = 460, H = 150, PL = 26, PR = 8, PT = 12, PB = 22;
  const maxY = Math.max(1, ...o.map(d => d.clean + d.hint + d.correction + d.unknown));
  const bw = (W - PL - PR) / o.length;
  const y = v => PT + (1 - v / maxY) * (H - PT - PB);
  let bars = "";
  o.forEach((d, i) => {
    let acc = 0;
    [["clean", "var(--good)"], ["hint", "var(--warn)"],
     ["correction", "var(--crit)"], ["unknown", "var(--sunk)"]].forEach(([k, col]) => {
      if (!d[k]) return;
      const y0 = y(acc + d[k]), y1 = y(acc);
      bars += `<rect x="${(PL + i * bw + 1.5).toFixed(1)}" y="${y0.toFixed(1)}"
        width="${(bw - 3).toFixed(1)}" height="${(y1 - y0).toFixed(1)}" fill="${col}"><title>${d.date} ${k}: ${d[k]}</title></rect>`;
      acc += d[k];
    });
  });
  const grid = [0, maxY].map(v =>
    `<line x1="${PL}" x2="${W - PR}" y1="${y(v)}" y2="${y(v)}" stroke="var(--line)"/>
     <text class="ax" x="0" y="${y(v) + 3}">${Math.round(v)}</text>`).join("");
  const labs = o.map((d, i) => (i === 0 || i === o.length - 1)
    ? `<text class="ax" x="${(PL + i * bw + bw / 2).toFixed(1)}" y="${H - 6}" text-anchor="middle">${d.date.slice(5)}</text>` : "").join("");
  $("outcomes").innerHTML =
    `<svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Review outcomes by date">${grid}${bars}${labs}</svg>`;
})();

/* leech */
if (!A.leech_watch.length && !A.repeat_mistakes.length) {
  $("leech").appendChild(el("div", "row", "<span>Nothing at recurrence 2 or higher.</span>"));
} else {
  A.leech_watch.forEach(r => {
    const tag = r.tags.includes("leech")
      ? '<span class="pill p-crit">leech</span>' : '<span class="pill p-warn">2 of 3</span>';
    $("leech").appendChild(el("div", "row",
      `<span>${esc(r.name)}<span class="tags">${tag}</span></span><span class="m">due ${r.due}</span>`));
  });
  A.repeat_mistakes.slice(-4).forEach(m => {
    $("leech").appendChild(el("div", "row",
      `<span>${esc(m.title)}<span class="tags"><span class="pill p-acc">journal</span></span></span>
       <span class="m">×${m.recurrence}</span>`));
  });
}

/* repeat offenders */
if (!A.repeat_offenders.length) {
  $("offenders").appendChild(el("div", "row", "<span>No problem has needed help twice.</span>"));
}
A.repeat_offenders.forEach(([name, reps]) => {
  $("offenders").appendChild(el("div", "row",
    `<span>${esc(name)}</span><span class="m">${reps.length}× · ${esc(reps.join(", "))}</span>`));
});

/* classes */
const CLS_NOTE = {
  "invariant-why": "knows the steps, not why they hold",
  "boundary": "post-loop and off-by-one misses",
  "stale-recall": "was solid once, decayed",
  "transfer-gap": "pattern didn't carry to a new shape",
  "code-vs-derivation": "correct in words, wrong in code",
};
const clsE = Object.entries(A.cls_counts), clsMax = Math.max(1, ...clsE.map(e => e[1]));
$("class-hint").textContent = plural(D.mistakes.length, "entry") + " · inner = since " + A.cls_cutoff;
clsE.forEach(([k, v]) => {
  const recent = A.cls_recent[k] || 0;
  const n = el("div", "b"), lab = el("div", "lab");
  lab.appendChild(el("div", null,
    `${esc(k)} <span style="color:var(--muted);font-size:12px">— ${esc(CLS_NOTE[k] || "")}</span>`));
  const meter = el("div", "meter"), i = el("i"), r = el("i", "overlay recent");
  i.style.width = (v / clsMax * 100) + "%";
  r.style.width = (recent / clsMax * 100) + "%";
  meter.append(i, r); lab.appendChild(meter);
  n.append(lab, el("div", "n", recent ? `${v}<br><span style="color:var(--crit)">${recent}</span>` : v));
  $("classes").appendChild(n);
});

/* ladder: does spaced repetition actually pay off here */
$("ladder-hint").textContent = `${A.reviews_graded} graded`;
[...A.by_number, {label: "", clean: null, n: 0}, ...A.by_tag].forEach(row => {
  if (!row.label) {
    $("ladder").appendChild(el("div", "b",
      '<div style="grid-column:1/-1;height:1px;background:var(--line)"></div>'));
    return;
  }
  const n = el("div", "b"), lab = el("div", "lab");
  lab.appendChild(el("div", null,
    `${esc(row.label)} <span style="color:var(--muted);font-size:12px">— ${row.n} graded</span>`));
  const meter = el("div", "meter"), i = el("i");
  i.style.width = (row.clean === null ? 0 : row.clean) + "%";
  i.style.background = row.clean === null ? "var(--sunk)"
    : row.clean >= 70 ? "var(--good)" : row.clean >= 50 ? "var(--warn)" : "var(--crit)";
  meter.appendChild(i); lab.appendChild(meter);
  n.append(lab, el("div", "n", row.clean === null ? "—" : row.clean + "%"));
  $("ladder").appendChild(n);
});

/* patterns */
const patE = Object.entries(A.pat_counts), patMax = Math.max(1, ...patE.map(e => e[1]));
patE.forEach(([k, v]) => {
  const n = el("div", "b"), lab = el("div", "lab");
  lab.appendChild(el("div", null, esc(k)));
  const meter = el("div", "meter"), i = el("i");
  i.style.width = (v / patMax * 100) + "%";
  meter.appendChild(i); lab.appendChild(meter);
  n.append(lab, el("div", "n", v));
  $("patterns").appendChild(n);
});

/* tracks */
$("track-hint").textContent = D.tracks.filter(t => /^0 |not started/.test(t.detail)).length + " at zero";
D.tracks.forEach(t => {
  const zero = /^0 |not started/.test(t.detail);
  $("tracks").appendChild(el("div", "row",
    `<span>${esc(t.track)}${zero ? '<span class="tags"><span class="pill p-crit">untouched</span></span>' : ""}</span>
     <span class="m">${esc(t.detail)}</span>`));
});

/* calendar */
const startD = new Date(D.cycle.start + "T00:00:00"), on = new Set(A.active_days);
$("cal-hint").textContent = A.show_rate + "% of days";
for (let i = 0; i < D.cycle.total_days; i++) {
  const d = new Date(startD.getTime() + i * 86400000).toISOString().slice(0, 10);
  const s = el("span");
  s.className = on.has(d) ? "on" : (d > D.cycle.today ? "future" : "");
  s.title = d + (on.has(d) ? " — logged" : d > D.cycle.today ? "" : " — no entry");
  $("cal").appendChild(s);
}

/* threads */
D.threads.slice().reverse().forEach(t => {
  $("threads").appendChild(el("div", "row",
    `<span>${esc(t.text)}</span><span class="m">${t.date || ""}</span>`));
});

/* queue + filters */
const q = $("queue");
q.innerHTML = "<thead><tr><th>Problem</th><th>Due</th><th>Rev</th><th>Tags</th><th class='num'>Status</th></tr></thead>";
const tb = el("tbody");
D.reviews.forEach(r => {
  const pill = r.status === "overdue" ? `<span class="pill p-crit">${r.overdue_days}d late</span>`
    : r.status === "today" ? '<span class="pill p-warn">today</span>'
    : '<span class="pill p-good">ahead</span>';
  const tags = r.tags.map(t =>
    `<span class="pill ${t === "leech" ? "p-crit" : "p-acc"}">${t}</span>`).join(" ");
  const tr = el("tr");
  tr.dataset.status = r.status;
  tr.dataset.derive = r.tags.includes("derive") ? "1" : "0";
  tr.innerHTML = `<td>${esc(r.name)}</td><td class="m">${r.due}</td>
    <td class="num">#${r.n}</td><td>${tags}</td><td class="num">${pill}</td>`;
  tb.appendChild(tr);
});
q.appendChild(tb);
$("filters").addEventListener("click", e => {
  const btn = e.target.closest("button"); if (!btn) return;
  [...$("filters").children].forEach(b => b.setAttribute("aria-pressed", b === btn));
  const f = btn.dataset.f;
  [...tb.children].forEach(tr => {
    const show = f === "all" ? true
      : f === "derive" ? tr.dataset.derive === "1"
      : f === "overdue" ? tr.dataset.status === "overdue"
      : tr.dataset.status === "upcoming";
    tr.style.display = show ? "" : "none";
  });
});

/* health */
const H = D.health;
const groups = {};
H.warnings.forEach(w => (groups[w.kind] = groups[w.kind] || []).push(w.detail));
const counts = Object.entries(H.counts)
  .map(([k, v]) => `${k.replace(/_/g, " ")} <strong>${v}</strong>`).join(" · ");
$("health").appendChild(el("div", null, counts));
if (!H.warnings.length) {
  $("health").appendChild(el("div", "ok", "✓ Every bullet in every parsed section matched its expected shape."));
} else {
  Object.entries(groups).forEach(([kind, items]) => {
    const d = el("div", "bad", `${items.length} × ${esc(kind)}`);
    const ul = el("ul");
    items.slice(0, 4).forEach(t => ul.appendChild(el("li", null, `<code>${esc(t)}</code>`)));
    d.appendChild(ul);
    $("health").appendChild(d);
  });
}

$("foot").innerHTML = `Regenerate with
  <code>python3 ~/InterviewPrep/tools/build_dashboard.py</code> after
  <code>interview-prep-save</code>, then republish. Scope estimate assumes
  ${Object.entries(A.est_breakdown).map(([k, v]) => `${k.replace(/_/g, " ")} ${v}h`).join(" · ")}
  — tunable in <code>CONFIG</code> at the top of the script.`;
</script>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(ROOT, "Progress", "dashboard.html"))
    ap.add_argument("--no-history", action="store_true",
                    help="skip appending today's snapshot to metrics_history.jsonl")
    args = ap.parse_args()

    cycle = parse_cycle()
    reviews, graduated = parse_reviews()
    archive = parse_archive()
    problems = parse_solved()
    mistakes = parse_mistakes()
    active_days, threads = parse_session_notes()
    active_days = sorted(set(active_days)
                         | {p["date"] for p in problems if p["date"]}
                         | {m["date"] for m in mistakes if m["date"]}
                         | {a["completed"] for a in archive})
    tracks, cases = parse_tracks()

    known = {p["key"] for p in problems}
    for r in reviews:
        if r["key"] not in known:
            warn("review-without-matching-problem", r["name"])

    analysis = analyse(cycle, reviews, archive, problems, mistakes, active_days, cases)
    history = backlog_history(cycle, reviews, archive)
    batch = build_batch(reviews, problems, CONFIG["session_review_cap"])
    append_history(analysis, not args.no_history)
    snapshots = load_snapshots()
    verdict = build_verdict(cycle, analysis, tracks, cases, snapshots)

    data = {
        "cycle": cycle, "reviews": reviews, "problems": problems, "mistakes": mistakes,
        "tracks": tracks, "cases": cases, "threads": threads, "analysis": analysis,
        "verdict": verdict, "history": history, "snapshots": snapshots,
        "batch": batch, "health": HEALTH,
        "meta": {"files": 7, "graduated": graduated},
    }
    html = HTML.replace("__DATA__", json.dumps(data))
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(html)

    print(f"wrote {args.out}")
    print("  " + " · ".join(f"{k.replace('_', ' ')} {v}" for k, v in HEALTH["counts"].items()))
    print(f"  backlog {analysis['backlog']} · clean rate {analysis['clean_rate']}% "
          f"· {len(active_days)} active days · {len(HEALTH['warnings'])} warnings")
    for w in HEALTH["warnings"][:6]:
        print(f"    ! {w['kind']}: {w['detail'][:90]}")


if __name__ == "__main__":
    main()
