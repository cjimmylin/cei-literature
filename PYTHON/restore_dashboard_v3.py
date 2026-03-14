#!/usr/bin/env python3
"""
Restore browser-saved LLM Ethics Dashboard to a clean, self-contained v3 HTML.

The browser "Save As Complete Web Page" operation introduces artifacts:
  - Local file references instead of CDN URLs
  - Pre-rendered ECharts canvas elements (static bitmaps, won't re-render)
  - Pre-populated dynamic containers (JS appends → doubled content)
  - Browser metadata comments and modified attributes

This script strips all artifacts and produces a clean working dashboard.

Input:  DASHBOARDS/CEI Literature Vault — LLM Ethics Dashboard.html
Output: DASHBOARDS/20260210-vault-dashboard-3.html
"""

import re
import sys
import functools
from pathlib import Path

print = functools.partial(print, flush=True)

SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
INPUT = WS_ROOT / "DASHBOARDS" / "CEI Literature Vault — LLM Ethics Dashboard.html"
OUTPUT = WS_ROOT / "DASHBOARDS" / "20260210-vault-dashboard-3.html"

if not INPUT.exists():
    print(f"ERROR: Input file not found: {INPUT}")
    sys.exit(1)

print(f"Reading: {INPUT.name}")
html = INPUT.read_text(encoding="utf-8")
print(f"  Input size: {len(html):,} bytes ({len(html) // 1024} KB)")

stats = {}

# ══════════════════════════════════════════════════════════════════════════
# PHASE 1: Global string replacements (safe for entire file)
# ══════════════════════════════════════════════════════════════════════════

# Remove browser "saved from url" comment
html = re.sub(r'<!-- saved from url=[^\n]*-->\n?', '', html)

# Fix meta charset (browser rewrites this)
html = html.replace(
    '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">',
    '<meta charset="UTF-8">'
)

# Replace local asset references with CDN URLs
html = re.sub(
    r'<link href="\./CEI Literature Vault[^"]*?/css2" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700'
    '&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">',
    html
)
html = re.sub(
    r'<script src="\./CEI Literature Vault[^"]*?/echarts\.min\.js"></script>',
    '<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.1/dist/echarts.min.js"></script>',
    html
)

# Fix preconnect URLs (browser adds trailing slashes)
html = html.replace(
    'href="https://fonts.googleapis.com/"', 'href="https://fonts.googleapis.com"'
)
html = html.replace(
    'href="https://fonts.gstatic.com/"', 'href="https://fonts.gstatic.com"'
)
html = html.replace(' crossorigin=""', ' crossorigin')

print("  Phase 1: Global replacements ✓")


# ══════════════════════════════════════════════════════════════════════════
# PHASE 2: Body section cleanup (strip rendering artifacts)
# ══════════════════════════════════════════════════════════════════════════

# Extract body section (between <body> and inline <script>)
body_start = html.index('<body>')
# The inline script starts on its own line (not the CDN <script src=...>)
script_match = re.search(r'\n<script>\n', html[body_start:])
if not script_match:
    print("ERROR: Could not find inline <script> tag")
    sys.exit(1)
inline_script_pos = body_start + script_match.start()
body = html[body_start:inline_script_pos]


def empty_element_by_id(text, elem_id, strip_style=False):
    """Find an HTML element by ID and remove all its children.

    Args:
        text: HTML string to modify
        elem_id: ID attribute value to search for
        strip_style: If True, remove inline style attribute (for chart containers)
    """
    marker = f'id="{elem_id}"'
    idx = text.find(marker)
    if idx == -1:
        return text

    # Find start of containing tag
    tag_start = text.rfind('<', 0, idx)
    tag_name_match = re.match(r'<(\w+)', text[tag_start:])
    if not tag_name_match:
        return text
    tag_name = tag_name_match.group(1)

    # Find end of opening tag
    tag_end = text.find('>', idx) + 1
    opening = text[tag_start:tag_end]

    # Optionally remove inline styles (ECharts artifacts)
    if strip_style:
        opening = re.sub(r'\s+style="[^"]*"', '', opening)

    # Track nesting depth to find matching close tag
    close_tag = f'</{tag_name}>'
    open_re = re.compile(rf'<{tag_name}[\s>/]')
    pos = tag_end
    depth = 1

    while depth > 0 and pos < len(text):
        next_open_m = open_re.search(text, pos)
        next_close = text.find(close_tag, pos)
        if next_close == -1:
            break
        next_open = next_open_m.start() if next_open_m else len(text)

        if next_open < next_close:
            depth += 1
            pos = next_open + 1
        else:
            depth -= 1
            if depth == 0:
                close_end = next_close + len(close_tag)
                text = text[:tag_start] + opening + close_tag + text[close_end:]
                break
            pos = next_close + len(close_tag)

    return text


def empty_select_keep_default(text, select_id):
    """Empty a <select> but keep its first (default) <option>."""
    marker = f'id="{select_id}"'
    idx = text.find(marker)
    if idx == -1:
        return text
    tag_start = text.rfind('<select', 0, idx)
    tag_end = text.find('>', idx) + 1
    close_idx = text.find('</select>', tag_end)
    if close_idx == -1:
        return text
    inner = text[tag_end:close_idx]
    first_opt_m = re.search(r'<option value="">.*?</option>', inner)
    default_opt = first_opt_m.group(0) if first_opt_m else '<option value="">All</option>'
    return text[:tag_end] + '\n      ' + default_opt + '\n    ' + text[close_idx:]


# ── Strip ECharts instance attributes ──────────────────────────────────
body = re.sub(r'\s*_echarts_instance_="[^"]*"', '', body)

# ── Empty all chart containers (strip ECharts inline styles) ───────────
chart_ids = re.findall(r'id="(chart-[^"]+)"', body)
for cid in chart_ids:
    body = empty_element_by_id(body, cid, strip_style=True)
stats['charts'] = len(chart_ids)
print(f"  Phase 2: Emptied {len(chart_ids)} chart containers")

# ── Empty KPI rows (JS uses appendChild → would double) ───────────────
kpi_ids = [
    'kpi-row',
    'norm-kpi-row', 'norm-ve-kpis', 'norm-de-kpis', 'norm-cu-kpis',
    'cult-kpi-row',
    'mpsy-kpi-row', 'mpsy-mft-kpis', 'mpsy-schwartz-kpis', 'mpsy-dev-kpis',
    'relig-kpi-row', 'relig-islamic-kpis', 'relig-abrahamic-kpis',
    'relig-dharmic-kpis', 'relig-confucian-kpis',
]
for kid in kpi_ids:
    body = empty_element_by_id(body, kid, strip_style=False)
stats['kpis'] = len(kpi_ids)
print(f"  Phase 2: Emptied {len(kpi_ids)} KPI containers")

# ── Empty table bodies (JS uses innerHTML → safe, but cleaner) ─────────
tbody_ids = re.findall(r'id="([^"]*-tbody)"', body)
for tid in tbody_ids:
    body = empty_element_by_id(body, tid, strip_style=False)
stats['tables'] = len(tbody_ids)
print(f"  Phase 2: Emptied {len(tbody_ids)} table bodies")

# ── Empty pagination (JS rebuilds) ────────────────────────────────────
body = empty_element_by_id(body, 'res-pagination')

# ── Empty narrative divs (JS injects from DATA.narratives) ─────────────
narrative_ids = re.findall(r'id="([^"]*-narrative-[^"]*)"', body)
for nid in narrative_ids:
    body = empty_element_by_id(body, nid, strip_style=False)
stats['narratives'] = len(narrative_ids)
print(f"  Phase 2: Emptied {len(narrative_ids)} narrative containers")

# ── Empty gap grids and multi-paper containers ─────────────────────────
for gid in ['mpsy-gap-grid', 'relig-gap-grid', 'norm-multi-papers']:
    body = empty_element_by_id(body, gid, strip_style=False)

# ── Empty <select> dropdowns that JS populates via appendChild ─────────
for sel_id in ['res-cat', 'res-year', 'norm-overview-fw',
               'mpsy-overview-theory', 'relig-overview-trad']:
    body = empty_select_keep_default(body, sel_id)

# ── Fix initial active states (set Overview as default everywhere) ─────
# Browser save captured whatever tab was active at save time.
# Reset to Overview for a clean initial load.

# Main tabs: deactivate all, activate overview
body = re.sub(r'<div class="tab active"', '<div class="tab"', body)
body = body.replace(
    '<div class="tab" data-tab="overview">',
    '<div class="tab active" data-tab="overview">'
)

# Main sections: deactivate all, activate overview
body = re.sub(r'class="section active"', 'class="section"', body)
body = body.replace(
    '<div class="section" id="sec-overview">',
    '<div class="section active" id="sec-overview">'
)

# Sub-navigation pills + sub-sections: set overview active
for prefix in ['cult', 'norm', 'mpsy', 'relig']:
    body = re.sub(
        rf'<div class="{prefix}-pill active"',
        f'<div class="{prefix}-pill"', body
    )
    body = body.replace(
        f'<div class="{prefix}-pill" data-sub="overview">',
        f'<div class="{prefix}-pill active" data-sub="overview">'
    )
    body = re.sub(
        rf'<div class="{prefix}-sub active"',
        f'<div class="{prefix}-sub"', body
    )
    body = body.replace(
        f'<div class="{prefix}-sub" id="{prefix}-overview">',
        f'<div class="{prefix}-sub active" id="{prefix}-overview">'
    )

print("  Phase 2: Fixed active states ✓")

# Put cleaned body back into full HTML
html = html[:body_start] + body + html[inline_script_pos:]


# ══════════════════════════════════════════════════════════════════════════
# PHASE 3: Script bug fixes
# ══════════════════════════════════════════════════════════════════════════

# Fix operator precedence bug in Religious Values KPIs:
#   Original: (rv.christian_jewish||{}).count||0 + (rv.dharmic||{}).count||0 + ...
#   The || binds looser than +, so this evaluates as count||(0+count||(0+count||0))
#   instead of (count||0) + (count||0) + (count||0)
old_expr = (
    "(rv.christian_jewish||{}).count||0 + "
    "(rv.dharmic||{}).count||0 + "
    "(rv.confucian||{}).count||0"
)
new_expr = (
    "((rv.christian_jewish||{}).count||0) + "
    "((rv.dharmic||{}).count||0) + "
    "((rv.confucian||{}).count||0)"
)
if old_expr in html:
    html = html.replace(old_expr, new_expr)
    print("  Phase 3: Fixed operator precedence bug in Religious KPIs")

# Fix }; → ]; syntax error for kpis array closing bracket
# Context: after the last Religious KPI entry, the array closes with }; not ];
count_before = len(html)
html = re.sub(
    r"(label: 'Benchmark Candidates' },\s*)};(\s*const kpiRow = "
    r"document\.getElementById\('relig-kpi-row'\))",
    r"\1];\2",
    html
)
if len(html) != count_before:
    print("  Phase 3: Fixed }; → ]; syntax error")

print("  Phase 3: Script fixes ✓")


# ══════════════════════════════════════════════════════════════════════════
# PHASE 4: Final cleanup and output
# ══════════════════════════════════════════════════════════════════════════

# Remove excessive blank lines
html = re.sub(r'\n{3,}', '\n\n', html)

# Write output
OUTPUT.write_text(html, encoding='utf-8')

size_kb = len(html) / 1024
print(f"\n{'=' * 60}")
print(f"Output: {OUTPUT.name}")
print(f"  Size: {len(html):,} bytes ({size_kb:.0f} KB)")
print(f"  Charts: {stats.get('charts', 0)}")
print(f"  Tables: {stats.get('tables', 0)}")
print(f"  Narratives: {stats.get('narratives', 0)}")
print(f"  KPI rows: {stats.get('kpis', 0)}")
print(f"\nDone! Open in browser to verify.")
