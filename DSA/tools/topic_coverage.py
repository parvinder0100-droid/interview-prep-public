#!/usr/bin/env python3
"""
Generates ~/InterviewPrep/DSA/Progress/topic_coverage.html — a standalone,
offline horizontal-bar visualization of DSA topic coverage for the CURRENT
PREP CYCLE re-verification pass (Striver A2Z sheet).

IMPORTANT FRAMING (do not lose this when editing DATA below): the user solved
the *entire* 455-problem Striver A2Z sheet once, ~2 years ago. The numbers
here are NOT lifetime knowledge — they are how much of each topic has been
*re-verified live* in the current prep cycle. A topic showing 0 in Panel 2
means "no re-verification rep yet this cycle," not "never learned." See
~/InterviewPrep/DSA/Progress/progress.md "Current Position" /
"Topics Not Started — reclassified 2026-07-26" for the source framing.

This is a hand-maintained data file, not a markdown parser — progress.md is
prose-heavy and not worth round-tripping. When progress.md's numbers move,
update the DATA dicts below by hand and re-run:

    python3 topic_coverage.py

Source: ~/InterviewPrep/DSA/Progress/progress.md (Current Position section,
Topics Started section), read on 2026-08-01.
"""

import datetime
import os

# ---------------------------------------------------------------------------
# DATA — edit these when progress.md changes materially.
# ---------------------------------------------------------------------------

GENERATED_DATE = "2026-08-01"

# Panel 1: Striver-sheet topics that have a clean known /N denominator
# (solved, total, source note). Sorted by % desc at render time.
PANEL1 = [
    # (topic, solved, total, note)
    ("Binary Search", 32, 32, "solved ~2-3mo ago, rusty, needs re-verification"),
    ("LinkedList", 31, 31, "solved ~2-3mo ago, rusty, needs re-verification"),
    ("BST", 16, 16, "solved ~2-3mo ago, rusty, needs re-verification"),
    ("Trees", 36, 39, "near-complete, 3 unconfirmed gaps"),
    ("Tries", 6, 7, "1 known gap: Max XOR With Element From Array"),
    ("DP", 44, 56, "12 unconfirmed gaps in later lectures, high interview weight"),
    ("Arrays", 27, 40, "live: Basics/Easy/Medium done (27), Hard (11) untouched"),
    ("Strings", 3, 15, "in progress"),
    ("Recursion", 2, 25, "in progress, priority gap"),
    ("Bit Manipulation", 1, 18, "in progress"),
    ("Basics", 0, 31, "not started this cycle, low priority given prior experience"),
    ("Sorting", 0, 7, "not started this cycle"),
]

# Panel 2: topics without a clean /N this cycle (new-material or
# algorithm-count based) — shown as live-solved COUNTS, not a fake percent.
PANEL2 = [
    # (topic, count, note)
    ("Graph", 18,
     "algorithms/problems done — core set (BFS/DFS, cycle detection, "
     "bipartite, topo sort, Kosaraju's, Dijkstra, Bellman-Ford, "
     "Floyd-Warshall, Kruskal's, Prim's, Union-Find) covered at least once"),
    ("Stack/Queue", 6, "problems solved live"),
    ("Sliding Window", 6, "problems solved live"),
    ("Heaps", 0, "0 solved live this cycle — solved ~2yr ago, not yet re-verified"),
    ("Greedy", 0, "0 solved live this cycle — solved ~2yr ago, not yet re-verified"),
    ("Final/Misc section", 0,
     "0 solved live this cycle — solved ~2yr ago, not yet re-verified"),
]

OUT_PATH = os.path.expanduser("~/InterviewPrep/DSA/Progress/topic_coverage.html")

# ---------------------------------------------------------------------------
# Sequential single-hue ramp (blue), light -> dark, per the dataviz skill's
# palette.md. 13 steps spanning the documented 100->700 range.
# ---------------------------------------------------------------------------

LIGHT_RAMP = [
    "#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7",
    "#3987e5", "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b",
]

# Dark-mode companion ramp: sequential "flips anchor" on a dark surface —
# near-zero recedes toward the dark surface instead of toward white, and the
# high end is the brightest step so it still pops. Not in palette.md verbatim
# (that file only tabulates the light-surface steps); built as the same hue
# family re-stepped for a dark surface, per color-formula.md's "flips anchor
# in dark" note. Sequential ramps are explicitly out of scope for the
# categorical validator (color-formula.md "Scope" section), so this is a
# manual, defensible re-step rather than a validated categorical slot.
DARK_RAMP = [
    "#18293d", "#1c375a", "#1f4573", "#225390", "#2a63a8", "#3372c4",
    "#3987e5", "#5598e7", "#6da7ec", "#86b6ef", "#9ec5f4", "#b7d3f6", "#cde2fb",
]


def _lerp(a, b, t):
    return round(a + (b - a) * t)


def _hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _rgb_to_hex(rgb):
    return "#" + "".join(f"{max(0, min(255, c)):02x}" for c in rgb)


def ramp_color(t, ramp):
    """t in [0,1] -> interpolated hex color along the given ramp."""
    t = max(0.0, min(1.0, t))
    n = len(ramp) - 1
    pos = t * n
    i = int(pos)
    if i >= n:
        return ramp[n]
    frac = pos - i
    c0, c1 = _hex_to_rgb(ramp[i]), _hex_to_rgb(ramp[i + 1])
    return _rgb_to_hex(tuple(_lerp(c0[k], c1[k], frac) for k in range(3)))


def esc(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def build_panel1_rows():
    rows = []
    ranked = sorted(PANEL1, key=lambda r: (r[1] / r[2]) if r[2] else 0, reverse=True)
    for topic, solved, total, note in ranked:
        pct = (solved / total) if total else 0.0
        pct_label = round(pct * 100)
        light = ramp_color(pct, LIGHT_RAMP)
        dark = ramp_color(pct, DARK_RAMP)
        # keep a sliver visible even at 0% so the row doesn't read as "no data"
        width_pct = max(pct * 100, 1.2)
        rows.append(
            f"""
            <div class="bar-row" role="listitem">
              <div class="bar-label">{esc(topic)}</div>
              <div class="bar-track" aria-hidden="true">
                <div class="bar-fill" style="width:{width_pct:.1f}%; --bar-color-light:{light}; --bar-color-dark:{dark};"></div>
              </div>
              <div class="bar-value">{pct_label}%<span class="bar-value-sub"> ({solved}/{total})</span></div>
              <div class="bar-note">{esc(note)}</div>
            </div>"""
        )
    return "\n".join(rows)


def build_panel2_rows():
    rows = []
    max_count = max((r[1] for r in PANEL2), default=1) or 1
    ranked = sorted(PANEL2, key=lambda r: r[1], reverse=True)
    for topic, count, note in ranked:
        t = count / max_count
        light = ramp_color(t, LIGHT_RAMP)
        dark = ramp_color(t, DARK_RAMP)
        width_pct = max(t * 100, 1.2)
        rows.append(
            f"""
            <div class="bar-row" role="listitem">
              <div class="bar-label">{esc(topic)}</div>
              <div class="bar-track" aria-hidden="true">
                <div class="bar-fill" style="width:{width_pct:.1f}%; --bar-color-light:{light}; --bar-color-dark:{dark};"></div>
              </div>
              <div class="bar-value">{count}<span class="bar-value-sub"> / {max_count} max</span></div>
              <div class="bar-note">{esc(note)}</div>
            </div>"""
        )
    return "\n".join(rows)


def build_table_rows():
    rows = []
    for topic, solved, total, note in PANEL1:
        pct = round((solved / total) * 100) if total else 0
        rows.append(
            f"<tr><td>{esc(topic)}</td><td>Striver /N</td>"
            f"<td>{solved}/{total} ({pct}%)</td><td>{esc(note)}</td></tr>"
        )
    for topic, count, note in PANEL2:
        rows.append(
            f"<tr><td>{esc(topic)}</td><td>count-based</td>"
            f"<td>{count} solved live</td><td>{esc(note)}</td></tr>"
        )
    return "\n".join(rows)


def build_html():
    panel1_rows = build_panel1_rows()
    panel2_rows = build_panel2_rows()
    table_rows = build_table_rows()

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DSA Topic Coverage — InterviewPrep</title>
<style>
  :root {{ color-scheme: light dark; }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    padding: 32px 20px 60px;
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    background: #f9f9f7;
    color: #0b0b0b;
  }}
  @media (prefers-color-scheme: dark) {{
    body:where(:not([data-theme="light"])) {{ background: #0d0d0d; color: #ffffff; }}
  }}
  body[data-theme="dark"] {{ background: #0d0d0d; color: #ffffff; }}

  .wrap {{ max-width: 880px; margin: 0 auto; }}

  header {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; margin-bottom: 4px; }}
  h1 {{ font-size: 1.5rem; margin: 0 0 4px; }}
  .subtitle {{ font-size: 0.95rem; color: #52514e; margin: 0; }}
  @media (prefers-color-scheme: dark) {{
    body:where(:not([data-theme="light"])) .subtitle {{ color: #c3c2b7; }}
  }}
  body[data-theme="dark"] .subtitle {{ color: #c3c2b7; }}

  #theme-toggle {{
    font: inherit;
    font-size: 0.85rem;
    padding: 6px 12px;
    border-radius: 6px;
    border: 1px solid rgba(11,11,11,0.15);
    background: transparent;
    color: inherit;
    cursor: pointer;
    flex-shrink: 0;
  }}
  @media (prefers-color-scheme: dark) {{
    body:where(:not([data-theme="light"])) #theme-toggle {{ border-color: rgba(255,255,255,0.2); }}
  }}
  body[data-theme="dark"] #theme-toggle {{ border-color: rgba(255,255,255,0.2); }}

  .banner {{
    margin: 20px 0 32px;
    padding: 14px 16px;
    border-radius: 8px;
    border: 1px solid rgba(11,11,11,0.10);
    background: rgba(42,120,214,0.06);
    font-size: 0.88rem;
    line-height: 1.5;
    color: #52514e;
  }}
  @media (prefers-color-scheme: dark) {{
    body:where(:not([data-theme="light"])) .banner {{
      border-color: rgba(255,255,255,0.10);
      background: rgba(57,135,229,0.08);
      color: #c3c2b7;
    }}
  }}
  body[data-theme="dark"] .banner {{
    border-color: rgba(255,255,255,0.10);
    background: rgba(57,135,229,0.08);
    color: #c3c2b7;
  }}
  .banner strong {{ color: inherit; }}

  .viz-root {{ margin-bottom: 44px; }}
  .panel-title {{ font-size: 1.05rem; margin: 0 0 2px; }}
  .panel-desc {{ font-size: 0.85rem; color: #898781; margin: 0 0 18px; }}

  .bar-list {{ display: flex; flex-direction: column; gap: 14px; }}
  .bar-row {{
    display: grid;
    grid-template-columns: 128px minmax(0,1fr) 96px;
    grid-template-rows: auto auto;
    column-gap: 12px;
    row-gap: 2px;
    align-items: center;
  }}
  .bar-label {{ font-size: 0.85rem; font-weight: 500; text-align: right; grid-column: 1; grid-row: 1; }}
  .bar-track {{
    grid-column: 2; grid-row: 1;
    position: relative;
    height: 16px;
    border-radius: 8px;
    background: #e1e0d9;
    overflow: hidden;
  }}
  @media (prefers-color-scheme: dark) {{
    body:where(:not([data-theme="light"])) .bar-track {{ background: #2c2c2a; }}
  }}
  body[data-theme="dark"] .bar-track {{ background: #2c2c2a; }}

  .bar-fill {{
    height: 100%;
    border-radius: 8px;
    background: var(--bar-color-light);
  }}
  @media (prefers-color-scheme: dark) {{
    body:where(:not([data-theme="light"])) .bar-fill {{ background: var(--bar-color-dark); }}
  }}
  body[data-theme="dark"] .bar-fill {{ background: var(--bar-color-dark); }}

  .bar-value {{ grid-column: 3; grid-row: 1; font-size: 0.85rem; font-variant-numeric: tabular-nums; white-space: nowrap; }}
  .bar-value-sub {{ color: #898781; font-size: 0.78rem; }}
  .bar-note {{ grid-column: 2 / 4; grid-row: 2; font-size: 0.74rem; color: #898781; line-height: 1.35; }}

  .axis {{
    display: grid;
    grid-template-columns: 128px minmax(0,1fr) 96px;
    column-gap: 12px;
    margin-bottom: 10px;
    font-size: 0.7rem;
    color: #898781;
  }}
  .axis-track {{ grid-column: 2; position: relative; height: 14px; }}
  .axis-tick {{ position: absolute; top: 0; transform: translateX(-50%); }}
  .axis-tick::before {{
    content: "";
    position: absolute;
    top: 14px;
    left: 50%;
    width: 1px;
    height: 6px;
    background: #e1e0d9;
  }}
  @media (prefers-color-scheme: dark) {{
    body:where(:not([data-theme="light"])) .axis-tick::before {{ background: #2c2c2a; }}
  }}
  body[data-theme="dark"] .axis-tick::before {{ background: #2c2c2a; }}

  details.table-view {{ margin-top: 8px; }}
  details.table-view summary {{ cursor: pointer; font-size: 0.85rem; color: #52514e; }}
  @media (prefers-color-scheme: dark) {{
    body:where(:not([data-theme="light"])) details.table-view summary {{ color: #c3c2b7; }}
  }}
  body[data-theme="dark"] details.table-view summary {{ color: #c3c2b7; }}

  table {{ width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 0.8rem; }}
  th, td {{ text-align: left; padding: 6px 8px; border-bottom: 1px solid #e1e0d9; }}
  @media (prefers-color-scheme: dark) {{
    body:where(:not([data-theme="light"])) th, body:where(:not([data-theme="light"])) td {{ border-bottom-color: #2c2c2a; }}
  }}
  body[data-theme="dark"] th, body[data-theme="dark"] td {{ border-bottom-color: #2c2c2a; }}
  th {{ font-weight: 600; color: #52514e; }}
  @media (prefers-color-scheme: dark) {{
    body:where(:not([data-theme="light"])) th {{ color: #c3c2b7; }}
  }}
  body[data-theme="dark"] th {{ color: #c3c2b7; }}

  footer {{ margin-top: 40px; font-size: 0.75rem; color: #898781; line-height: 1.6; }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div>
      <h1>DSA Topic Coverage</h1>
      <p class="subtitle">Striver A2Z sheet &mdash; current-cycle re-verification, not lifetime knowledge</p>
    </div>
    <button id="theme-toggle" type="button" onclick="toggleTheme()">Toggle theme</button>
  </header>

  <div class="banner">
    <strong>Read this before the bars:</strong> the full 455-problem Striver A2Z
    sheet was solved once, ~2 years ago. Every bar below measures only how much
    of each topic has been <strong>re-verified live in the current prep cycle</strong>
    &mdash; a low or 0 bar means "not re-tested yet this cycle," not "never
    learned." Source: <code>DSA/Progress/progress.md</code>, "Current Position"
    and "Topics Started" sections, as of {esc(GENERATED_DATE)}.
  </div>

  <section class="viz-root">
    <p class="panel-title">Striver-sheet topics with a known /N total</p>
    <p class="panel-desc">Sorted by % complete. Color encodes the % value (light&nbsp;=&nbsp;low, dark&nbsp;=&nbsp;high) &mdash; it does not identify the topic.</p>
    <div class="axis" aria-hidden="true">
      <div></div>
      <div class="axis-track">
        <span class="axis-tick" style="left:0%">0%</span>
        <span class="axis-tick" style="left:25%">25%</span>
        <span class="axis-tick" style="left:50%">50%</span>
        <span class="axis-tick" style="left:75%">75%</span>
        <span class="axis-tick" style="left:100%">100%</span>
      </div>
      <div></div>
    </div>
    <div class="bar-list" role="list">
{panel1_rows}
    </div>
  </section>

  <section class="viz-root">
    <p class="panel-title">New-material / algorithm topics (solved-count, no clean /N)</p>
    <p class="panel-desc">Graph is algorithm-count based, not problem-count based; Stack/Queue and Sliding Window are new-topic live counts. Bars scaled to this panel's own max (Graph&nbsp;=&nbsp;18). Color encodes relative count, same ramp as above.</p>
    <div class="bar-list" role="list">
{panel2_rows}
    </div>
  </section>

  <details class="table-view">
    <summary>Table view (all topics, raw numbers)</summary>
    <table>
      <thead><tr><th>Topic</th><th>Basis</th><th>Coverage</th><th>Note</th></tr></thead>
      <tbody>
{table_rows}
      </tbody>
    </table>
  </details>

  <footer>
    Generated {esc(GENERATED_DATE)} by <code>DSA/tools/topic_coverage.py</code> from
    <code>DSA/Progress/progress.md</code>. Regenerate after a material progress.md
    update by editing the DATA dicts at the top of that script and re-running it.
    Local file, not published anywhere.
  </footer>
</div>

<script>
  function toggleTheme() {{
    var cur = document.body.getAttribute('data-theme');
    if (cur === 'dark') {{
      document.body.setAttribute('data-theme', 'light');
    }} else if (cur === 'light') {{
      document.body.removeAttribute('data-theme');
    }} else {{
      document.body.setAttribute('data-theme', 'dark');
    }}
  }}
</script>
</body>
</html>
"""


def main():
    html = build_html()
    with open(OUT_PATH, "w") as f:
        f.write(html)
    print(f"Wrote {OUT_PATH} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
