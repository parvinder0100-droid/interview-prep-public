"""Interactive HTML Intelligent Visualizer for PrepIntel."""

import json
from pathlib import Path
from typing import Dict, List
from ..config import OUTPUT_DASHBOARD_HTML
from ..models import Problem, ReviewItem, MistakeEntry, ReadinessProfile, TopicHealth

def generate_html_dashboard(
    profile: ReadinessProfile,
    topic_health: List[TopicHealth],
    problems: List[Problem],
    review_items: List[ReviewItem],
    mistakes: List[MistakeEntry],
    output_path: Path = OUTPUT_DASHBOARD_HTML
) -> Path:
    """Emits an intelligent, interactive single-page visualizer for browser exploration."""

    data = {
        "profile": {
            "readiness": profile.overall_readiness_pct,
            "solved": profile.solved_count,
            "total": profile.total_problems,
            "coverage": profile.coverage_pct,
            "hint_idx": profile.hint_reliance_index,
            "overdue": profile.total_overdue_reviews,
            "leeches": profile.active_leech_count,
            "mistakes": profile.total_mistakes_logged,
            "weaknesses": profile.top_weaknesses,
            "current_track": "Graph (Classic Problems) — 1/12 complete",
            "next_problem": "Course Schedule II (LC 210)",
            "sprint_day": "Day 57 (Plan B: Target 2026-09-17)",
        },
        "topics": [
            {
                "topic": t.topic,
                "total": t.total_problems,
                "solved": t.solved_count,
                "clean": t.clean_solved_count,
                "hints": t.hint_solved_count,
                "hint_pct": t.hint_reliance_pct,
                "score": t.health_score,
                "status": t.status,
                "overdue": t.overdue_reviews_count
            } for t in topic_health
        ],
        "problems": [
            {
                "name": p.name,
                "id": p.id_code,
                "topic": p.topic,
                "difficulty": p.difficulty,
                "is_solved": p.is_solved,
                "hints": p.hint_count,
                "date": p.solved_date or "Prior pass",
                "summary": p.session_summary[:140] if p.session_summary else "",
                "elo": p.elo_rating
            } for p in problems
        ],
        "reviews": [
            {
                "name": r.problem_name,
                "due": r.due_date,
                "rev_num": r.review_num,
                "overdue": r.days_overdue,
                "tags": r.tags,
                "prompt": r.recall_prompt if r.recall_prompt else "State optimal algorithmic invariant and time complexity cold."
            } for r in review_items
        ],
        "mistakes": [
            {
                "date": m.date,
                "problem": m.problem,
                "category": m.category,
                "title": m.title,
                "mistake": m.mistake,
                "root_cause": m.root_cause,
                "how_to_avoid": m.how_to_avoid,
                "pattern": m.pattern
            } for m in mistakes
        ]
    }

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PrepIntel Live Visualizer — Interview Preparation Command Center</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 4px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #475569; }}
    .tab-btn.active {{ border-color: #3b82f6; color: #f8fafc; background: rgba(59, 130, 246, 0.12); }}
    .tab-btn:not(.active) {{ border-color: transparent; color: #94a3b8; }}
  </style>
</head>
<body class="bg-[#0b1120] text-[#f8fafc] antialiased min-h-screen p-3 sm:p-5 lg:p-7">

  <div class="max-w-7xl mx-auto space-y-5">

    <!-- Top Live Status & Telemetry Header -->
    <header class="bg-[#131d32] border border-[#233554] rounded-2xl p-5 shadow-lg relative overflow-hidden">
      <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 relative z-10">
        <div class="space-y-1.5">
          <div class="flex flex-wrap items-center gap-2">
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
              LIVE TRACKER • {profile.overall_readiness_pct}% FAANG READY
            </span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-500/10 text-blue-400 border border-blue-500/30">
              Sprint: Day 57 (Plan B)
            </span>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-purple-500/10 text-purple-400 border border-purple-500/30">
              Target: 2026-09-17
            </span>
          </div>
          <h1 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-[#f8fafc]">
            Interview Preparation Intelligent Visualizer
          </h1>
          <p class="text-xs sm:text-sm text-[#94a3b8] max-w-3xl">
            Unified telemetry tracking your 88 solved problems, 97 overdue spaced reviews, 172 mistake post-mortems, and active topic fragility.
          </p>
        </div>

        <!-- Live KPI Badges -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 shrink-0">
          <div class="bg-[#0b1120]/90 border border-[#233554] rounded-xl p-3 text-center min-w-[95px]">
            <div class="text-[10px] uppercase font-bold text-[#94a3b8]">Readiness Index</div>
            <div class="text-xl font-black text-emerald-400">{profile.overall_readiness_pct}%</div>
            <div class="text-[9px] text-[#94a3b8]">FAANG Baseline</div>
          </div>
          <div class="bg-[#0b1120]/90 border border-[#233554] rounded-xl p-3 text-center min-w-[95px]">
            <div class="text-[10px] uppercase font-bold text-[#94a3b8]">Sprint Cut List</div>
            <div class="text-xl font-black text-blue-400">{profile.solved_count}/{profile.total_problems}</div>
            <div class="text-[9px] text-blue-300 font-bold">{profile.coverage_pct}% Solved</div>
          </div>
          <div class="bg-[#0b1120]/90 border border-[#233554] rounded-xl p-3 text-center min-w-[95px]">
            <div class="text-[10px] uppercase font-bold text-[#94a3b8]">Hint Debt</div>
            <div class="text-xl font-black text-amber-400">{profile.hint_reliance_index}%</div>
            <div class="text-[9px] text-amber-400/80">Guided Solves</div>
          </div>
          <div class="bg-[#0b1120]/90 border border-[#233554] rounded-xl p-3 text-center min-w-[95px]">
            <div class="text-[10px] uppercase font-bold text-[#94a3b8]">Review Backlog</div>
            <div class="text-xl font-black text-red-400">{profile.total_overdue_reviews}</div>
            <div class="text-[9px] text-red-300 font-bold">Overdue Items</div>
          </div>
        </div>
      </div>

      <!-- Currently Happening Banner -->
      <div class="mt-4 pt-3 border-t border-[#233554] flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
        <div class="flex items-center gap-2">
          <span class="font-bold text-[#94a3b8] uppercase text-[10px]">Current Active Focus:</span>
          <span class="font-semibold text-[#f8fafc] bg-[#1e293b] px-2 py-0.5 rounded border border-[#334155]">
            Graph (Classic Problems) — 1/12 Complete
          </span>
          <span class="text-[#94a3b8]">→ Next up: <strong class="text-amber-400">Course Schedule II (LC 210)</strong></span>
        </div>
        <div class="text-[11px] text-[#94a3b8]">
          Last Review Cleared: <span class="text-emerald-400 font-medium">Course Schedule (Clean) • Power of Two (Hint)</span>
        </div>
      </div>
    </header>

    <!-- Navigation Tabs -->
    <nav class="flex gap-2 border-b border-[#233554] pb-2 overflow-x-auto no-scrollbar">
      <button onclick="switchTab('overview')" id="tab-btn-overview" class="tab-btn active px-4 py-2 text-xs sm:text-sm font-bold rounded-xl border transition-all shrink-0">
        1. Radar & Weaknesses
      </button>
      <button onclick="switchTab('recall')" id="tab-btn-recall" class="tab-btn px-4 py-2 text-xs sm:text-sm font-bold rounded-xl border transition-all shrink-0">
        2. Spaced Repetition ({profile.total_overdue_reviews} Due)
      </button>
      <button onclick="switchTab('mistakes')" id="tab-btn-mistakes" class="tab-btn px-4 py-2 text-xs sm:text-sm font-bold rounded-xl border transition-all shrink-0">
        3. Mistake Taxonomy ({profile.total_mistakes_logged} Logged)
      </button>
      <button onclick="switchTab('problems')" id="tab-btn-problems" class="tab-btn px-4 py-2 text-xs sm:text-sm font-bold rounded-xl border transition-all shrink-0">
        4. Problem Archive & Elo ({profile.solved_count} Solved)
      </button>
    </nav>

    <!-- ========================================== -->
    <!-- TAB 1: RADAR & TOPIC WEAKNESSES           -->
    <!-- ========================================== -->
    <section id="section-overview" class="space-y-5">
      
      <!-- Top Diagnostic Alerts -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <div class="p-3.5 rounded-xl bg-red-500/10 border border-red-500/30 space-y-1">
          <div class="text-[10px] font-bold text-red-400 uppercase tracking-wider">Top Fragile Topics</div>
          <div class="text-sm font-extrabold text-[#f8fafc]">Recursion (19.8%) & Stack (35.0%)</div>
          <p class="text-[11px] text-[#cbd5e1]">85.7% of Recursion solves needed mentor hints. Must be re-tested cold.</p>
        </div>

        <div class="p-3.5 rounded-xl bg-amber-500/10 border border-amber-500/30 space-y-1">
          <div class="text-[10px] font-bold text-amber-400 uppercase tracking-wider">Spaced Review Decay</div>
          <div class="text-sm font-extrabold text-[#f8fafc]">{profile.total_overdue_reviews} Reviews Overdue</div>
          <p class="text-[11px] text-[#cbd5e1]">Active forgetting curve is eroding solved material. Open every session with 2 reviews.</p>
        </div>

        <div class="p-3.5 rounded-xl bg-purple-500/10 border border-purple-500/30 space-y-1">
          <div class="text-[10px] font-bold text-purple-400 uppercase tracking-wider">Active Leech Concepts</div>
          <div class="text-sm font-extrabold text-[#f8fafc]">Bellman-Ford & Redundant Connection</div>
          <p class="text-[11px] text-[#cbd5e1]">Failed the exact same causal invariant 3+ times. Needs daily 3-minute micro-recall.</p>
        </div>
      </div>

      <!-- Full Topic Health Matrix Grid -->
      <div class="bg-[#131d32] border border-[#233554] rounded-2xl p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <h2 class="text-base font-bold text-[#f8fafc]">Topic Mastery & Fragility Radar</h2>
            <p class="text-xs text-[#94a3b8]">Color-coded by empirical retention score (Health = Coverage - Hint Debt - Overdue Decay)</p>
          </div>
          <div class="flex items-center gap-2 text-xs">
            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span> Solid (&gt;75)</span>
            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span> Moderate (60-75)</span>
            <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-red-500"></span> Fragile (&lt;60)</span>
          </div>
        </div>

        <!-- Topic Cards Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-3.5" id="topics-grid">
          <!-- Injected by JavaScript -->
        </div>
      </div>

      <!-- High-Risk Problems Alert Table -->
      <div class="bg-[#131d32] border border-[#233554] rounded-2xl p-5 space-y-3">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-sm font-bold text-[#f8fafc]">Highest Risk Problems (Heavy Hints + Decay)</h3>
            <p class="text-xs text-[#94a3b8]">Problems that were solved with guided assistance and now have overdue review decay</p>
          </div>
          <span class="px-2 py-0.5 rounded bg-red-500/20 text-red-300 text-[10px] font-bold">Immediate Priority</span>
        </div>

        <div class="overflow-x-auto border border-[#233554] rounded-xl">
          <table class="w-full text-xs text-left">
            <thead class="bg-[#0b1120] text-[#94a3b8] border-b border-[#233554]">
              <tr>
                <th class="p-2.5">Problem Name</th>
                <th class="p-2.5">Topic</th>
                <th class="p-2.5">Hints Consumed</th>
                <th class="p-2.5">Days Overdue</th>
                <th class="p-2.5">Difficulty</th>
                <th class="p-2.5">Action</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-[#233554] font-medium" id="high-risk-tbody">
              <!-- Injected by JS -->
            </tbody>
          </table>
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 2: SPACED REPETITION & ACTIVE RECALL  -->
    <!-- ========================================== -->
    <section id="section-recall" class="space-y-5 hidden">
      
      <!-- Interactive Flashcard Drill Box -->
      <div class="bg-[#131d32] border-2 border-blue-500/40 rounded-2xl p-5 space-y-4 shadow-xl">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-[#233554] pb-3">
          <div>
            <span class="px-2 py-0.5 rounded bg-blue-500/20 text-blue-400 text-[10px] font-bold uppercase">Active Recall Terminal</span>
            <h2 class="text-lg font-extrabold text-[#f8fafc] mt-0.5" id="flashcard-title">Sudoku Solver (LC 37)</h2>
            <div class="flex items-center gap-2 text-xs text-[#94a3b8] mt-0.5" id="flashcard-meta">
              <span class="text-red-400 font-bold">[derive]</span>
              <span>• Review #1</span>
              <span>• 3 days overdue</span>
            </div>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="prevCard()" class="px-3 py-1.5 rounded-lg bg-[#0b1120] border border-[#233554] text-xs hover:border-blue-500">← Prev</button>
            <span class="text-xs font-mono text-[#94a3b8]" id="card-index-display">1 of 30</span>
            <button onclick="nextCard()" class="px-3 py-1.5 rounded-lg bg-[#0b1120] border border-[#233554] text-xs hover:border-blue-500">Next →</button>
          </div>
        </div>

        <!-- Question Box -->
        <div class="p-4 rounded-xl bg-[#0b1120] border border-[#233554] space-y-2">
          <div class="text-[10px] uppercase font-bold text-amber-400 flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            Active Recall Challenge Question (Test Yourself Before Looking):
          </div>
          <p class="text-sm font-semibold text-[#f8fafc] leading-relaxed" id="flashcard-question">
            Loading prompt...
          </p>
        </div>

        <!-- Hidden Invariant Reveal Block -->
        <div id="flashcard-answer-block" class="hidden p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 space-y-2">
          <div class="text-[10px] uppercase font-bold text-emerald-400">Core Invariant & Derivation Notes:</div>
          <div class="text-xs text-[#cbd5e1] leading-relaxed" id="flashcard-answer">
            Invariant details...
          </div>
        </div>

        <!-- Action Bar -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-2">
          <button onclick="toggleAnswer()" id="reveal-btn" class="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 font-bold text-xs text-white transition-colors">
            Reveal Invariant & Known Bugs
          </button>

          <div class="flex items-center gap-2" id="grade-buttons">
            <span class="text-xs text-[#94a3b8]">Self-Grade:</span>
            <button onclick="gradeCard('clean')" class="px-3 py-1.5 rounded-lg bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-xs font-bold hover:bg-emerald-500/30">1. Clean (+3/+7d)</button>
            <button onclick="gradeCard('hint')" class="px-3 py-1.5 rounded-lg bg-amber-500/20 text-amber-400 border border-amber-500/30 text-xs font-bold hover:bg-amber-500/30">2. Guided (repeat 2d)</button>
            <button onclick="gradeCard('fail')" class="px-3 py-1.5 rounded-lg bg-red-500/20 text-red-400 border border-red-500/30 text-xs font-bold hover:bg-red-500/30">3. Failed (Day 1)</button>
          </div>
        </div>
      </div>

      <!-- Overdue Reviews List -->
      <div class="bg-[#131d32] border border-[#233554] rounded-2xl p-5 space-y-3">
        <div class="flex items-center justify-between">
          <h3 class="text-sm font-bold text-[#f8fafc]">Complete Spaced Repetition Queue ({profile.total_overdue_reviews} Overdue)</h3>
          <span class="text-xs text-[#94a3b8]">Sorted by days overdue</span>
        </div>

        <div class="space-y-2 max-h-[450px] overflow-y-auto pr-1" id="reviews-list-container">
          <!-- Injected by JS -->
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 3: MISTAKE TAXONOMY                   -->
    <!-- ========================================== -->
    <section id="section-mistakes" class="space-y-5 hidden">
      
      <!-- Mistake Category Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5" id="mistake-categories-grid">
        <!-- Injected by JS -->
      </div>

      <!-- Mistake Explorer & Search -->
      <div class="bg-[#131d32] border border-[#233554] rounded-2xl p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h3 class="text-sm font-bold text-[#f8fafc]">Mistake Post-Mortem Explorer (172 Logged)</h3>
            <p class="text-xs text-[#94a3b8]">Inspect root causes and preventive rules derived from real sessions</p>
          </div>
          <div class="flex items-center gap-2">
            <select id="mistake-filter-cat" onchange="renderMistakesList()" class="bg-[#0b1120] border border-[#233554] rounded-lg px-2.5 py-1.5 text-xs text-[#f8fafc] outline-none">
              <option value="ALL">All Categories</option>
              <option value="Algorithmic Logic & Modeling">Algorithmic Logic & Modeling</option>
              <option value="Monotonicity & Invariants">Monotonicity & Invariants</option>
              <option value="Loop & Boundary Off-by-One">Loop & Boundary Off-by-One</option>
              <option value="Process & Consistency">Process & Consistency</option>
              <option value="Type Bounds & Overflow">Type Bounds & Overflow</option>
              <option value="Edge Cases & Degeneracy">Edge Cases & Degeneracy</option>
            </select>
          </div>
        </div>

        <div class="space-y-3 max-h-[500px] overflow-y-auto pr-1" id="mistakes-list-container">
          <!-- Injected by JS -->
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- TAB 4: PROBLEM ARCHIVE & ELO               -->
    <!-- ========================================== -->
    <section id="section-problems" class="space-y-5 hidden">
      
      <div class="bg-[#131d32] border border-[#233554] rounded-2xl p-5 space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div>
            <h3 class="text-base font-bold text-[#f8fafc]">Solved Problems & Sprint Coverage</h3>
            <p class="text-xs text-[#94a3b8]">88 solved across the cut list with historical contest Elo calibration</p>
          </div>
          
          <div class="flex flex-wrap items-center gap-2">
            <input 
              type="text" 
              id="problem-search" 
              placeholder="Search problem or ID..." 
              oninput="renderProblemsTable()"
              class="bg-[#0b1120] border border-[#233554] rounded-lg px-3 py-1.5 text-xs text-[#f8fafc] placeholder-[#94a3b8] outline-none focus:border-blue-500"
            />
            <select id="problem-topic-filter" onchange="renderProblemsTable()" class="bg-[#0b1120] border border-[#233554] rounded-lg px-2.5 py-1.5 text-xs text-[#f8fafc] outline-none">
              <option value="ALL">All Topics</option>
            </select>
            <select id="problem-diff-filter" onchange="renderProblemsTable()" class="bg-[#0b1120] border border-[#233554] rounded-lg px-2.5 py-1.5 text-xs text-[#f8fafc] outline-none">
              <option value="ALL">All Difficulties</option>
              <option value="Easy">Easy</option>
              <option value="Medium">Medium</option>
              <option value="Hard">Hard</option>
            </select>
          </div>
        </div>

        <div class="overflow-x-auto border border-[#233554] rounded-xl">
          <table class="w-full text-xs text-left">
            <thead class="bg-[#0b1120] text-[#94a3b8] border-b border-[#233554]">
              <tr>
                <th class="p-3">Problem Title</th>
                <th class="p-3">Topic</th>
                <th class="p-3">Difficulty</th>
                <th class="p-3">Contest Elo</th>
                <th class="p-3">Solve Verdict</th>
                <th class="p-3">Solved Date</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-[#233554] font-medium" id="problems-tbody">
              <!-- Injected by JS -->
            </tbody>
          </table>
        </div>
        
        <div class="text-xs text-[#94a3b8] text-right" id="problem-count-footer">
          Showing 88 problems
        </div>
      </div>

    </section>

  </div>

  <script>
    const db = {json.dumps(data)};
    let currentCardIdx = 0;
    let answerRevealed = false;

    function switchTab(tId) {{
      const tabs = ['overview', 'recall', 'mistakes', 'problems'];
      tabs.forEach(t => {{
        const sec = document.getElementById('section-' + t);
        const btn = document.getElementById('tab-btn-' + t);
        if (t === tId) {{
          sec.classList.remove('hidden');
          btn.classList.add('active');
        }} else {{
          sec.classList.add('hidden');
          btn.classList.remove('active');
        }}
      }});
    }}

    // --- Render Topics ---
    function renderTopics() {{
      const grid = document.getElementById('topics-grid');
      const topicFilter = document.getElementById('problem-topic-filter');

      grid.innerHTML = db.topics.map(t => {{
        const sColor = t.health_score >= 80 ? 'emerald' : (t.health_score >= 60 ? 'amber' : 'red');
        return `
          <div class="bg-[#0b1120] border border-[#233554] rounded-xl p-4 space-y-2.5 hover:border-blue-500/50 transition-colors">
            <div class="flex items-center justify-between">
              <span class="font-bold text-sm text-[#f8fafc]">${{t.topic}}</span>
              <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-${{sColor}}-500/10 text-${{sColor}}-400 border border-${{sColor}}-500/30">
                ${{t.status}}
              </span>
            </div>
            
            <div class="flex items-baseline justify-between text-xs">
              <span class="text-[#94a3b8]">Health Score:</span>
              <span class="text-base font-black text-${{sColor}}-400">${{t.score}}/100</span>
            </div>

            <div class="w-full bg-[#1e293b] rounded-full h-1.5 overflow-hidden">
              <div class="bg-${{sColor}}-500 h-1.5 rounded-full" style="width: ${{t.score}}%"></div>
            </div>

            <div class="grid grid-cols-3 gap-1 text-[11px] pt-2 border-t border-[#233554] text-center">
              <div>
                <div class="text-[9px] uppercase text-[#94a3b8]">Solved</div>
                <div class="font-bold text-[#f8fafc]">${{t.solved}}/${{t.total}}</div>
              </div>
              <div>
                <div class="text-[9px] uppercase text-[#94a3b8]">Hint %</div>
                <div class="font-bold text-amber-400">${{t.hint_pct}}%</div>
              </div>
              <div>
                <div class="text-[9px] uppercase text-[#94a3b8]">Overdue</div>
                <div class="font-bold text-red-400">${{t.overdue}}</div>
              </div>
            </div>
          </div>
        `;
      }}).join('');

      // Populate select dropdown
      db.topics.forEach(t => {{
        const opt = document.createElement('option');
        opt.value = t.topic;
        opt.innerText = t.topic;
        topicFilter.appendChild(opt);
      }});
    }}

    // --- High Risk Problems Table ---
    function renderHighRisk() {{
      const tbody = document.getElementById('high-risk-tbody');
      // filter solved problems with hints >= 2 or overdue
      const highRisk = db.problems.filter(p => p.is_solved && p.hints >= 2).slice(0, 8);

      tbody.innerHTML = highRisk.map(p => `
        <tr class="hover:bg-[#1e293b]/40">
          <td class="p-2.5 text-[#f8fafc] font-bold">${{p.name}} <span class="text-[10px] text-[#94a3b8]">(${{p.id}})</span></td>
          <td class="p-2.5 text-[#94a3b8]">${{p.topic}}</td>
          <td class="p-2.5"><span class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-400 font-bold">${{p.hints}} Hints Needed</span></td>
          <td class="p-2.5 text-red-400 font-bold">Review Overdue</td>
          <td class="p-2.5 text-${{p.difficulty === 'Easy' ? 'emerald' : (p.difficulty === 'Medium' ? 'blue' : 'red')}}-400 font-bold">${{p.difficulty}}</td>
          <td class="p-2.5"><button onclick="switchTab('recall')" class="px-2 py-1 rounded bg-blue-500/20 text-blue-400 hover:bg-blue-500/30 text-[11px] font-bold">Review Now</button></td>
        </tr>
      `).join('');
    }}

    // --- Flashcards Logic ---
    function updateFlashcard() {{
      if (db.reviews.length === 0) return;
      const r = db.reviews[currentCardIdx];
      document.getElementById('flashcard-title').innerText = r.name;
      document.getElementById('flashcard-meta').innerHTML = `
        <span class="text-red-400 font-bold">${{r.tags.join(' ')}}</span>
        <span>• Review #${{r.rev_num}}</span>
        <span class="text-amber-400 font-bold">• ${{r.overdue > 0 ? r.overdue + ' days overdue' : 'Due today'}}</span>
      `;
      document.getElementById('flashcard-question').innerText = r.prompt;
      document.getElementById('card-index-display').innerText = `${{currentCardIdx + 1}} of ${{Math.min(30, db.reviews.length)}}`;

      // Match invariant from mistakes or notes if available
      const mMatch = db.mistakes.find(m => m.problem.toLowerCase().includes(r.name.toLowerCase()));
      if (mMatch) {{
        document.getElementById('flashcard-answer').innerHTML = `
          <div class="space-y-1">
            <p><strong>Preventive Invariant:</strong> <span class="text-emerald-300">${{mMatch.how_to_avoid}}</span></p>
            <p><strong>Historical Pitfall:</strong> <span class="text-red-300">${{mMatch.mistake}}</span></p>
            <p><strong>Root Cause:</strong> <span class="text-[#94a3b8]">${{mMatch.root_cause}}</span></p>
          </div>
        `;
      }} else {{
        document.getElementById('flashcard-answer').innerHTML = `
          <p>Review the problem invariant cold: derive the mathematical condition and state why the base case terminates.</p>
        `;
      }}

      // Reset reveal state
      answerRevealed = false;
      document.getElementById('flashcard-answer-block').classList.add('hidden');
      document.getElementById('reveal-btn').innerText = "Reveal Invariant & Known Bugs";
    }}

    function toggleAnswer() {{
      answerRevealed = !answerRevealed;
      const block = document.getElementById('flashcard-answer-block');
      const btn = document.getElementById('reveal-btn');
      if (answerRevealed) {{
        block.classList.remove('hidden');
        btn.innerText = "Hide Invariant";
      }} else {{
        block.classList.add('hidden');
        btn.innerText = "Reveal Invariant & Known Bugs";
      }}
    }}

    function nextCard() {{
      if (currentCardIdx < Math.min(30, db.reviews.length) - 1) {{
        currentCardIdx++;
        updateFlashcard();
      }}
    }}

    function prevCard() {{
      if (currentCardIdx > 0) {{
        currentCardIdx--;
        updateFlashcard();
      }}
    }}

    function gradeCard(grade) {{
      nextCard();
    }}

    // --- Render Overdue Reviews List ---
    function renderReviewsList() {{
      const container = document.getElementById('reviews-list-container');
      container.innerHTML = db.reviews.slice(0, 40).map((r, i) => `
        <div class="p-3 rounded-xl bg-[#0b1120] border border-[#233554] flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
          <div class="space-y-1">
            <div class="flex items-center gap-2">
              <span class="font-bold text-[#f8fafc] text-sm">${{r.name}}</span>
              <span class="px-1.5 py-0.5 rounded bg-blue-500/20 text-blue-400 text-[10px] font-bold">#${{r.rev_num}}</span>
              ${{r.tags.map(t => `<span class="px-1.5 py-0.5 rounded bg-red-500/20 text-red-400 text-[10px] font-bold">${{t}}</span>`).join('')}}
            </div>
            <p class="text-[#94a3b8] italic">${{r.prompt.slice(0, 110)}}...</p>
          </div>
          <div class="text-right shrink-0">
            <span class="px-2.5 py-1 rounded text-xs font-bold ${{r.overdue > 0 ? 'bg-red-500/20 text-red-400' : 'bg-emerald-500/20 text-emerald-400'}}">
              ${{r.overdue > 0 ? r.overdue + 'd Overdue' : 'Due Today'}}
            </span>
          </div>
        </div>
      `).join('');
    }}

    // --- Mistake Categories Grid ---
    function renderMistakeCategories() {{
      const grid = document.getElementById('mistake-categories-grid');
      const cats = {{}};
      db.mistakes.forEach(m => {{
        cats[m.category] = (cats[m.category] || 0) + 1;
      }});

      const total = db.mistakes.length;
      grid.innerHTML = Object.entries(cats).map(([cat, count]) => {{
        const pct = ((count / total) * 100).toFixed(1);
        return `
          <div class="bg-[#131d32] border border-[#233554] rounded-xl p-4 space-y-2">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-[#f8fafc]">${{cat}}</span>
              <span class="text-xs font-mono font-bold text-purple-400">${{count}} (${{pct}}%)</span>
            </div>
            <div class="w-full bg-[#0b1120] rounded-full h-1.5">
              <div class="bg-purple-500 h-1.5 rounded-full" style="width: ${{pct}}%"></div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    // --- Mistake Explorer List ---
    function renderMistakesList() {{
      const filter = document.getElementById('mistake-filter-cat').value;
      const container = document.getElementById('mistakes-list-container');
      const filtered = filter === 'ALL' ? db.mistakes : db.mistakes.filter(m => m.category === filter);

      container.innerHTML = filtered.slice(0, 35).map(m => `
        <div class="p-3.5 rounded-xl bg-[#0b1120] border border-[#233554] space-y-2 text-xs">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <span class="font-bold text-amber-400 text-sm">${{m.problem}}</span>
              <span class="text-[#94a3b8] text-[11px]">• ${{m.date}}</span>
            </div>
            <span class="px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 text-[10px] font-bold">${{m.category}}</span>
          </div>

          <div class="font-semibold text-[#f8fafc]">${{m.title}}</div>
          <div class="text-[#cbd5e1] leading-relaxed"><strong>Symptom:</strong> ${{m.mistake}}</div>
          <div class="text-[#94a3b8]"><strong>Root Cause:</strong> ${{m.root_cause}}</div>
          <div class="text-emerald-400 font-medium pt-1.5 border-t border-[#233554]">
            <strong>Preventive Rule:</strong> ${{m.how_to_avoid}}
          </div>
        </div>
      `).join('');
    }}

    // --- Problem Archive Table ---
    function renderProblemsTable() {{
      const q = document.getElementById('problem-search').value.toLowerCase();
      const topicF = document.getElementById('problem-topic-filter').value;
      const diffF = document.getElementById('problem-diff-filter').value;
      const tbody = document.getElementById('problems-tbody');

      const filtered = db.problems.filter(p => {{
        if (q && !p.name.toLowerCase().includes(q) && !p.id.toLowerCase().includes(q)) return false;
        if (topicF !== 'ALL' && p.topic !== topicF) return false;
        if (diffF !== 'ALL' && p.difficulty !== diffF) return false;
        return true;
      }});

      tbody.innerHTML = filtered.map(p => `
        <tr class="hover:bg-[#0b1120]/60">
          <td class="p-3 text-[#f8fafc] font-bold">${{p.name}} <span class="text-[10px] text-[#94a3b8]">(${{p.id}})</span></td>
          <td class="p-3 text-[#94a3b8]">${{p.topic}}</td>
          <td class="p-3 font-bold text-${{p.difficulty === 'Easy' ? 'emerald' : (p.difficulty === 'Medium' ? 'blue' : 'red')}}-400">${{p.difficulty}}</td>
          <td class="p-3 font-mono text-amber-400 font-bold">${{p.elo ? p.elo.toFixed(1) : '—'}}</td>
          <td class="p-3">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold ${{p.hints === 0 ? 'bg-emerald-500/20 text-emerald-400' : 'bg-amber-500/20 text-amber-400'}}">
              ${{p.hints === 0 ? 'Clean Solve' : p.hints + ' Hints'}}
            </span>
          </td>
          <td class="p-3 text-[11px] text-[#94a3b8]">${{p.date}}</td>
        </tr>
      `).join('');

      document.getElementById('problem-count-footer').innerText = `Showing ${{filtered.length}} of ${{db.problems.length}} problems`;
    }}

    // Initialize all sections
    window.addEventListener('DOMContentLoaded', () => {{
      renderTopics();
      renderHighRisk();
      updateFlashcard();
      renderReviewsList();
      renderMistakeCategories();
      renderMistakesList();
      renderProblemsTable();
    }});
  </script>
</body>
</html>
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html_content, encoding="utf-8")
    return output_path
