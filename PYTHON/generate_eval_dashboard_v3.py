#!/usr/bin/env python3
"""Generate Eval Framework Dashboard v3 with per-framework tabs and paper detail modals."""

import json
import re
import sys
import html as html_mod
from pathlib import Path

# === Paths ===
BASE = Path(__file__).resolve().parent.parent  # CEI-Lit-WS/
STATS = BASE / "STATISTICS"
DASH = BASE / "DASHBOARDS"
OUTPUT = STATS / "20260313-eval-framework-dashboard-v3.html"
EXISTING = DASH / "20260313-eval-framework-dashboard.html"

REPORTS = {
    'lm_eval': STATS / '20260312-lm-eval-implementability-report.md',
    'eleutherai': STATS / '20260312-eleutherai-eval-harness-integration.md',
    'inspect': STATS / '20260312-inspect-eval-implementability-report.md',
    'helm': STATS / '20260312-helm-values-alignment-integration-report.md',
    'lighteval_impl': STATS / '20260312-lighteval-implementability-report.md',
    'lighteval_papers': STATS / '20260312-lighteval-paper-reports.md',
    'openai_impl': STATS / '20260312-openai-evals-implementability-report.md',
    'openai_papers': STATS / '20260312-openai-evals-paper-reports.md',
}

# ============================================================
# 1. GENERIC MARKDOWN PARSING
# ============================================================

def clean_cell(s):
    s = s.strip()
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'`(.+?)`', r'\1', s)
    return s.strip()


def parse_md_table(lines):
    tlines = [l for l in lines if l.strip().startswith('|')]
    if len(tlines) < 3:
        return []
    headers = [clean_cell(h) for h in tlines[0].split('|')[1:-1]]
    rows = []
    for line in tlines[2:]:
        cells = line.split('|')[1:-1]
        if len(cells) == len(headers):
            rows.append({h: clean_cell(c) for h, c in zip(headers, cells)})
    return rows


def split_sections(text):
    sections = {}
    current = None
    lines = []
    for line in text.split('\n'):
        if line.startswith('## '):
            if current is not None:
                sections[current] = '\n'.join(lines)
            current = line[3:].strip()
            lines = []
        else:
            lines.append(line)
    if current is not None:
        sections[current] = '\n'.join(lines)
    return sections


def find_tables(text):
    tables = []
    cur = []
    for line in text.split('\n'):
        if line.strip().startswith('|'):
            cur.append(line)
        else:
            if cur:
                t = parse_md_table(cur)
                if t:
                    tables.append(t)
                cur = []
    if cur:
        t = parse_md_table(cur)
        if t:
            tables.append(t)
    return tables


def find_section(sections, pattern):
    for key, val in sections.items():
        if re.search(pattern, key, re.IGNORECASE):
            return val
    return None


def strip_md(s):
    """Remove .md extension from paper names."""
    return re.sub(r'\.md$', '', s)

# ============================================================
# 2. REPORT-SPECIFIC PARSERS
# ============================================================

def parse_lm_eval():
    text = REPORTS['lm_eval'].read_text(encoding='utf-8')
    secs = split_sections(text)
    data = []

    # Section 1: Already in harness
    content = find_section(secs, r'^1\.')
    if content:
        for t in find_tables(content):
            for r in t:
                data.append({
                    'k': strip_md(r.get('Paper', '')),
                    'tier': 'In Harness',
                    'score': '',
                    'bench': r.get('Harness Task', ''),
                    'type': r.get('Match Method', ''),
                    'url': '',
                    'notes': r.get('Availability', ''),
                })

    # Section 2: Ready
    content = find_section(secs, r'^2\.')
    if content:
        for t in find_tables(content):
            for r in t:
                data.append({
                    'k': strip_md(r.get('Paper', '')),
                    'tier': 'Ready',
                    'score': r.get('Score', ''),
                    'bench': r.get('Benchmark', ''),
                    'type': r.get('Type', ''),
                    'url': r.get('Data URL', ''),
                    'notes': r.get('Key Signals', ''),
                })

    # Section 3: Needs Dataset Hosting
    content = find_section(secs, r'^3\.')
    if content:
        for t in find_tables(content):
            for r in t:
                data.append({
                    'k': strip_md(r.get('Paper', '')),
                    'tier': 'Needs Dataset',
                    'score': r.get('Score', ''),
                    'bench': '',
                    'type': '',
                    'url': r.get('Data URL', ''),
                    'notes': r.get("What's Missing", r.get("What\u2019s Missing", '')),
                })

    # Section 4: Needs More Info (partial)
    content = find_section(secs, r'^4\.')
    if content:
        for t in find_tables(content):
            for r in t:
                data.append({
                    'k': strip_md(r.get('Paper', '')),
                    'tier': 'Needs Info',
                    'score': r.get('Score', ''),
                    'bench': '',
                    'type': '',
                    'url': '',
                    'notes': r.get('Missing Items', ''),
                })

    tiers = {'In Harness': 65, 'Ready': 178, 'Needs Dataset': 413,
             'Needs Info': 580, 'Not Implementable': 754}
    return {'data': data, 'tiers': tiers, 'total': 1990}


def parse_eleutherai():
    text = REPORTS['eleutherai'].read_text(encoding='utf-8')
    secs = split_sections(text)
    data = []

    content = find_section(secs, r'Existing')
    if content:
        for t in find_tables(content):
            for r in t:
                data.append({
                    'k': strip_md(r.get('Paper', '')),
                    'bench': r.get('Benchmark', ''),
                    'task': r.get('EleutherAI Task', ''),
                    'cat': 'Existing',
                    'extra': '',
                })

    content = find_section(secs, r'New Papers')
    if content:
        for t in find_tables(content):
            for r in t:
                data.append({
                    'k': strip_md(r.get('Paper', '')),
                    'bench': r.get('Key', ''),
                    'task': '',
                    'cat': 'New',
                    'extra': r.get('Classification', ''),
                })

    return {'data': data, 'total': len(data)}


def parse_inspect():
    text = REPORTS['inspect'].read_text(encoding='utf-8')
    secs = split_sections(text)
    data = []

    # Already in Inspect
    content = find_section(secs, r'^1\.\s')
    if content:
        for t in find_tables(content):
            for r in t:
                data.append({
                    'k': strip_md(r.get('Paper', '')),
                    'tier': 'In Inspect',
                    'detail': r.get('Inspect Eval', ''),
                    'cat': r.get('Category', ''),
                    'scorer': r.get('Scorer', ''),
                    'score': '',
                    'notes': '',
                })

    # Ready
    content = find_section(secs, r'^2\.\s')
    if content:
        for t in find_tables(content):
            for r in t:
                data.append({
                    'k': strip_md(r.get('Paper', '')),
                    'tier': 'Ready',
                    'detail': r.get('Eval Pattern', ''),
                    'cat': '',
                    'scorer': '',
                    'score': r.get('Score', ''),
                    'notes': r.get('Key Signals', ''),
                })

    # Model-Graded
    content = find_section(secs, r'Model-Graded')
    if content:
        for t in find_tables(content):
            for r in t:
                data.append({
                    'k': strip_md(r.get('Paper', '')),
                    'tier': 'Model-Graded',
                    'detail': r.get('Pattern', ''),
                    'cat': '',
                    'scorer': '',
                    'score': r.get('Score', ''),
                    'notes': r.get('Why Model-Graded', ''),
                })

    # Needs Dataset Work
    content = find_section(secs, r'Needs Dataset')
    if content:
        for t in find_tables(content):
            for r in t:
                data.append({
                    'k': strip_md(r.get('Paper', '')),
                    'tier': 'Needs Dataset',
                    'detail': '',
                    'cat': '',
                    'scorer': '',
                    'score': r.get('Score', ''),
                    'notes': r.get("What's Missing", ''),
                })

    tiers = {'In Inspect': 38, 'Ready': 23, 'Model-Graded': 29,
             'Needs Dataset': 483, 'Needs Info': 695, 'Not Implementable': 775}
    return {'data': data, 'tiers': tiers, 'total': 2043}


def parse_helm():
    text = REPORTS['helm'].read_text(encoding='utf-8')
    secs = split_sections(text)
    data = []

    # Phase 1: Existing
    content = find_section(secs, r'Phase 1|Existing Papers')
    if content:
        for t in find_tables(content):
            for r in t:
                data.append({
                    'k': strip_md(r.get('File', r.get('Benchmark', ''))),
                    'bench': r.get('Benchmark', ''),
                    'status': r.get('Status', 'Tagged'),
                    'phase': 'Existing',
                })

    # Phase 2: New papers — look for Paper subsections
    content = find_section(secs, r'Phase 2|New Papers')
    if content:
        subs = re.split(r'###\s+', content)
        for sub in subs[1:]:
            name = sub.split('\n')[0].strip()
            tables = find_tables(sub)
            if tables:
                info = {}
                for row in tables[0]:
                    f = row.get('Field', '')
                    v = row.get('Value', '')
                    if f:
                        info[f] = v
                data.append({
                    'k': strip_md(info.get('File', name)),
                    'bench': name.split(':')[-1].strip() if ':' in name else name,
                    'status': 'New',
                    'phase': 'New',
                })

    return {'data': data, 'total': len(data)}


def parse_paper_reports(path, framework):
    """Parse per-paper reports with 9-dimension scoring matrices."""
    text = path.read_text(encoding='utf-8')
    papers = []

    # Split by --- delimiter
    entries = re.split(r'\n---\n', text)

    for entry in entries:
        title_m = re.search(r'###\s+(.+)', entry)
        if not title_m:
            continue
        title = strip_md(title_m.group(1).strip())

        score_m = re.search(r'Score:\s*([\d.]+)/10\.0', entry)
        if not score_m:
            continue
        score = float(score_m.group(1))

        tier_m = re.search(r'Tier:\s*\*{0,2}([\w\s]+?)\*{0,2}\s*\|', entry)
        tier = tier_m.group(1).strip() if tier_m else 'Unknown'

        if framework == 'lighteval':
            type_m = re.search(r'lighteval type:\s*`?(\w+)`?', entry)
        else:
            type_m = re.search(r'Template:\s*`?(\w+)`?', entry)
        task_type = type_m.group(1) if type_m else 'unknown'

        # Extract raw dimension scores
        dims = []
        for dm in re.finditer(
            r'\|\s*D\d\s*\|[^|]+\|[^|]+\|\s*[^\d]*([\d.]+)\s*\|[^|]+\|', entry
        ):
            dims.append(float(dm.group(1)))

        # Count missing
        missing_m = re.search(r'\*\*Missing:\*\*\s*(.+)', entry)
        missing = 0
        if missing_m:
            mt = missing_m.group(1).strip()
            if mt and mt.lower() not in ('none', '\u2014', '-', ''):
                missing = len([x for x in mt.split(',') if x.strip()])

        papers.append({
            'k': title,
            's': score,
            't': tier,
            'ty': task_type,
            'm': missing,
            'd': dims if len(dims) == 9 else None,
        })

    return papers


def parse_appendix_table(text):
    """Parse appendix summary table from paper reports."""
    papers = []
    # Find appendix section
    app_m = re.search(r'(?:## Appendix|## Below Threshold)(.*)', text, re.DOTALL)
    if not app_m:
        return papers

    for t in find_tables(app_m.group(1)):
        for r in t:
            title = strip_md(r.get('Paper', ''))
            if not title:
                continue
            score_str = r.get('Score', '0')
            try:
                score = float(score_str)
            except ValueError:
                score = 0
            tier = r.get('Tier', 'Unknown')
            ty = r.get('Task Type', r.get('Template', 'unknown'))
            notes = r.get('Notes', r.get('Missing', ''))
            missing_m = re.search(r'(\d+)\s*missing', notes)
            missing = int(missing_m.group(1)) if missing_m else 0
            papers.append({
                'k': title,
                's': score,
                't': tier,
                'ty': ty,
                'm': missing,
                'd': None,
            })

    return papers


def parse_lighteval():
    # Summary from implementability report
    impl_text = REPORTS['lighteval_impl'].read_text(encoding='utf-8')
    impl_secs = split_sections(impl_text)

    tiers = {'Ready': 99, 'Possible': 771, 'Barriers': 903, 'Not Implementable': 217}
    # Try to extract from executive summary
    content = find_section(impl_secs, r'Executive Summary')
    if content:
        for t in find_tables(content):
            for r in t:
                tier = r.get('Tier', '')
                count_str = r.get('Count', '0')
                try:
                    tiers[tier] = int(count_str)
                except ValueError:
                    pass

    # Parse detailed paper reports
    detailed = parse_paper_reports(REPORTS['lighteval_papers'], 'lighteval')

    # Parse appendix
    app_text = REPORTS['lighteval_papers'].read_text(encoding='utf-8')
    appendix = parse_appendix_table(app_text)

    # Merge (detailed takes priority)
    seen = {p['k'] for p in detailed}
    combined = detailed[:]
    for p in appendix:
        if p['k'] not in seen:
            combined.append(p)
            seen.add(p['k'])

    return {'data': combined, 'tiers': tiers, 'total': 1990}


def parse_openai():
    impl_text = REPORTS['openai_impl'].read_text(encoding='utf-8')
    impl_secs = split_sections(impl_text)

    tiers = {'Ready': 783, 'Possible': 872, 'Barriers': 306, 'Not Implementable': 82}
    content = find_section(impl_secs, r'Executive Summary')
    if content:
        for t in find_tables(content):
            for r in t:
                tier = r.get('Tier', '')
                count_str = r.get('Count', '0')
                try:
                    tiers[tier] = int(count_str)
                except ValueError:
                    pass

    # Parse detailed paper reports
    detailed = parse_paper_reports(REPORTS['openai_papers'], 'openai')

    # Parse appendix if present
    app_text = REPORTS['openai_papers'].read_text(encoding='utf-8')
    appendix = parse_appendix_table(app_text)

    seen = {p['k'] for p in detailed}
    combined = detailed[:]
    for p in appendix:
        if p['k'] not in seen:
            combined.append(p)
            seen.add(p['k'])

    return {'data': combined, 'tiers': tiers, 'total': 2043}


# ============================================================
# 2b. PAPER BIBLIOGRAPHIC INFO
# ============================================================

def load_paper_info():
    """Load bibliographic info from all paper YAML frontmatter.

    Returns dict[paper_stem → {t, a, y, p, d, u, ab}] with short keys
    to minimize JSON size (~400 chars per paper × 2,043 papers).
    """
    papers_dir = BASE / "papers"
    info = {}
    fields_re = {
        't': re.compile(r'^short_title:\s*"?(.*?)"?\s*$', re.MULTILINE),
        'a': re.compile(r'^authors:\s*"?(.*?)"?\s*$', re.MULTILINE),
        'y': re.compile(r'^year:\s*(\S+)', re.MULTILINE),
        'p': re.compile(r'^publication:\s*"?(.*?)"?\s*$', re.MULTILINE),
        'd': re.compile(r'^doi:\s*(\S+)', re.MULTILINE),
        'u': re.compile(r'^url:\s*"?(.*?)"?\s*$', re.MULTILINE),
        'ab': re.compile(r'^abstract:\s*"(.*)"', re.MULTILINE),
    }
    for f in papers_dir.iterdir():
        if not f.suffix == '.md':
            continue
        try:
            text = f.read_text(encoding='utf-8')
        except Exception:
            continue
        if not text.startswith('---'):
            continue
        # Extract frontmatter between first --- and next ---
        parts = text[3:].split('\n---')
        if not parts:
            continue
        fm = parts[0]
        rec = {}
        for key, pat in fields_re.items():
            m = pat.search(fm)
            if m:
                val = m.group(1).strip()
                if val:
                    rec[key] = val
        if 't' not in rec:
            continue  # skip papers with no title
        # Use stem (filename without .md) as key
        info[f.stem] = rec
    print(f"  Paper info loaded: {len(info)} papers")
    return info


# ============================================================
# 3. IFRAME EXTRACTION
# ============================================================

def extract_iframes():
    """Extract srcdoc content from existing dashboard iframes."""
    html = EXISTING.read_text(encoding='utf-8')
    matches = re.findall(r'srcdoc="([^"]*)"', html, re.DOTALL)
    if len(matches) < 3:
        print(f"WARNING: Expected 3 iframes, found {len(matches)}", file=sys.stderr)
    return matches


# ============================================================
# 4. HTML GENERATION
# ============================================================

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body {
    font-family: 'Inter', -apple-system, system-ui, sans-serif;
    background: #0f0f1a; color: #c8d0e8;
    overflow: hidden; height: 100vh;
}
#header {
    background: #1a1a2e; padding: 14px 28px;
    border-bottom: 1px solid #252545;
    display: flex; align-items: baseline; gap: 16px;
}
#header h1 { font-size: 1.25rem; color: #a0b4e0; font-weight: 700; }
#header .subtitle { font-size: 0.78rem; color: #6a7490; }
#tabbar {
    display: flex; background: #141424;
    border-bottom: 1px solid #252545;
    overflow-x: auto; padding: 0 8px;
    scrollbar-width: thin;
}
.tab-btn {
    background: none; border: none; color: #6a7490;
    padding: 9px 16px; font-size: 0.73rem; font-weight: 600;
    cursor: pointer; border-bottom: 3px solid transparent;
    white-space: nowrap; transition: all .15s;
    font-family: inherit;
}
.tab-btn:hover { color: #a0b4e0; }
.tab-btn.active { color: #a0b4e0; border-bottom-color: #a0b4e0; }
.tab-btn.tab-lm         { color: #64b5f6; }
.tab-btn.tab-lm.active  { color: #64b5f6; border-bottom-color: #64b5f6; }
.tab-btn.tab-ea         { color: #b388ff; }
.tab-btn.tab-ea.active  { color: #b388ff; border-bottom-color: #b388ff; }
.tab-btn.tab-ins        { color: #4db6ac; }
.tab-btn.tab-ins.active { color: #4db6ac; border-bottom-color: #4db6ac; }
.tab-btn.tab-helm       { color: #ffb74d; }
.tab-btn.tab-helm.active{ color: #ffb74d; border-bottom-color: #ffb74d; }
.tab-btn.tab-le         { color: #7ae0ff; }
.tab-btn.tab-le.active  { color: #7ae0ff; border-bottom-color: #7ae0ff; }
.tab-btn.tab-oai        { color: #7affc8; }
.tab-btn.tab-oai.active { color: #7affc8; border-bottom-color: #7affc8; }
#content-area { height: calc(100vh - 88px); position: relative; }
.tab-panel { display: none; height: 100%; }
.tab-panel.active { display: block; }
.tab-panel iframe { width: 100%; height: 100%; border: none; background: #0f0f1a; }
.tab-panel.has-narrative { display: none; flex-direction: column; }
.tab-panel.has-narrative.active { display: flex; }
.tab-narrative { padding: 16px 28px 12px; color: #6a7490; font-size: 0.82rem; line-height: 1.6; max-width: 1100px; flex-shrink: 0; }
.tab-panel.has-narrative iframe { flex: 1; min-height: 0; }

/* Framework panels */
.fw-panel { overflow-y: auto; padding: 24px 28px 40px; }
.fw-inner { max-width: 1500px; margin: 0 auto; }
.fw-title { color: #a0b4e0; font-size: 1.3rem; margin: 0 0 18px; font-weight: 700; }

/* Stat cards */
.stat-row { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 20px; }
.stat-card {
    background: #1a1a2e; border-radius: 6px; padding: 14px 18px;
    min-width: 110px; text-align: center; border: 1px solid #252545;
}
.stat-card .sv { font-size: 1.7rem; font-weight: 700; color: #a0b4e0; }
.stat-card .sl {
    font-size: 0.65rem; color: #6a7490; margin-top: 3px;
    text-transform: uppercase; letter-spacing: 0.5px;
}

/* Controls */
.controls { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; flex-wrap: wrap; }
.controls input[type="text"] {
    background: #1a1a2e; border: 1px solid #252545; color: #c8d0e8;
    padding: 7px 11px; border-radius: 4px; font-size: 0.78rem; width: 260px;
    font-family: inherit; outline: none;
}
.controls input:focus { border-color: #4a5a8a; }
.controls select {
    background: #1a1a2e; border: 1px solid #252545; color: #c8d0e8;
    padding: 7px 11px; border-radius: 4px; font-size: 0.78rem;
    font-family: inherit; outline: none;
}
.cnt { color: #6a7490; font-size: 0.75rem; margin-left: auto; }

/* Tables */
.table-wrap { overflow-x: auto; }
.fw-table { width: 100%; border-collapse: collapse; font-size: 0.73rem; }
.fw-table th {
    position: sticky; top: 0; z-index: 2;
    background: #1a1a2e; color: #7888b8; padding: 7px 9px;
    text-align: left; border-bottom: 2px solid #252545;
    cursor: pointer; white-space: nowrap; user-select: none;
    font-weight: 600; font-size: 0.68rem; text-transform: uppercase;
    letter-spacing: 0.3px;
}
.fw-table th:hover { color: #a0b4e0; }
.fw-table td { padding: 5px 9px; border-bottom: 1px solid #1e1e30; }
.fw-table tr:hover { background: rgba(160,180,224,0.04); }
.fw-table td.notes-cell {
    max-width: 280px; overflow: hidden;
    text-overflow: ellipsis; white-space: nowrap;
}
.fw-table a { color: #7ab4ff; text-decoration: none; font-size: 0.7rem; }
.fw-table a:hover { text-decoration: underline; }

/* Badges */
.badge {
    display: inline-block; padding: 2px 6px; border-radius: 2px;
    font-size: 0.6rem; font-weight: 700; color: #fff; white-space: nowrap;
}
.badge.IMPLEMENTED { background: #1565c0; }
.badge.READY { background: #2e7d32; }
.badge.POSSIBLE { background: #f57f17; color: #1a0f00; }
.badge.BARRIERS { background: #bf360c; }
.badge.NOT_FEASIBLE { background: #7f0000; }
.badge.N_A { background: #1e1e2e; color: #3a4060; border: 1px solid #252545; }

/* Detail expansion */
.detail-row td { background: #141424; padding: 10px 16px !important; }
.dim-table { border-collapse: collapse; font-size: 0.7rem; margin: 4px 0; }
.dim-table th { background: #1a1a2e; padding: 4px 10px; font-weight: 600; color: #7888b8; text-transform: none; letter-spacing: 0; }
.dim-table td { padding: 4px 10px; border-bottom: 1px solid #1e1e30; }
.dim-ok { color: #66bb6a; }
.dim-part { color: #ffa726; }
.dim-miss { color: #5060a0; }
.clickable { cursor: pointer; }
.clickable:hover { background: rgba(160,180,224,0.08) !important; }

/* Overview */
.ov-inner { max-width: 1100px; margin: 0 auto; }
.ov-inner h1 { color: #a0b4e0; font-size: 1.5rem; margin-bottom: 6px; }
.ov-inner h2 { color: #8892aa; font-size: 1.05rem; margin: 24px 0 10px; border-bottom: 1px solid #252545; padding-bottom: 6px; }
.ov-inner p { color: #6a7490; font-size: 0.82rem; line-height: 1.5; margin-bottom: 10px; }
.tg { width: 100%; border-collapse: collapse; font-size: 0.78rem; margin-top: 12px; }
.tg th { text-align: left; padding: 7px 12px; background: #1a1a2e; color: #7888b8; border-bottom: 2px solid #252545; }
.tg td { padding: 7px 12px; border-bottom: 1px solid #1e1e30; }
.tg .tn { color: #a0b4e0; font-weight: 600; }
.tg .tc { color: #6a7490; font-size: 0.75rem; }
.tg tbody tr { cursor: pointer; }
.tg tbody tr:hover { background: rgba(160,180,224,0.08); }

/* Framework chip colors (matching TABLE 1) */
.chip { display:inline-block; padding:2px 8px; border-radius:3px; font-size:0.68rem; font-weight:600; border:1px solid; }
.chip-lm  { background:#0d2a4a; color:#64b5f6; border-color:#1a4a7a; }
.chip-ea  { background:#2d1b69; color:#b388ff; border-color:#4a1e8a; }
.chip-ins { background:#0d3a35; color:#4db6ac; border-color:#1a5a52; }
.chip-helm{ background:#3e2300; color:#ffb74d; border-color:#6a3a00; }
.chip-le  { background:#1a3a5e; color:#7ae0ff; border-color:#2a5a8e; }
.chip-oai { background:#1a3a2a; color:#7affc8; border-color:#2a5a4a; }

/* Framework-colored stat cards */
.stat-card.sc-lm  .sv { color:#64b5f6; }
.stat-card.sc-ea  .sv { color:#b388ff; }
.stat-card.sc-ins .sv { color:#4db6ac; }
.stat-card.sc-helm .sv { color:#ffb74d; }
.stat-card.sc-le  .sv { color:#7ae0ff; }
.stat-card.sc-oai .sv { color:#7affc8; }
.stat-card.sc-lm  { border-color:#1a4a7a; }
.stat-card.sc-ea  { border-color:#4a1e8a; }
.stat-card.sc-ins { border-color:#1a5a52; }
.stat-card.sc-helm{ border-color:#6a3a00; }
.stat-card.sc-le  { border-color:#2a5a8e; }
.stat-card.sc-oai { border-color:#2a5a4a; }

/* Clickable stat cards */
.stat-card.clickable-card { cursor: pointer; transition: all .15s; }
.stat-card.clickable-card:hover { border-color: #4a5a8a; transform: translateY(-1px); }
.stat-card.active-card { border-color: #a0b4e0 !important; box-shadow: 0 0 8px rgba(160,180,224,0.2); }

/* Tier badges for methodology section */
.tier-badge { display:inline-block; padding:1px 7px; border-radius:3px; font-size:0.72rem; font-weight:600; }
.tier-ready { background:#1b5e20; color:#a5d6a7; }
.tier-possible { background:#4a3600; color:#ffe082; }
.tier-barriers { background:#4a1400; color:#ef9a9a; }
.tier-notimpl { background:#3a0000; color:#e57373; }

/* Framework cards */
.framework-cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 18px; margin-bottom: 36px; }
.card { background: #1a1a2e; border: 1px solid #2a2a4a; border-radius: 8px; padding: 18px 20px; transition: border-color .15s; }
.card:hover { border-color: #4a5a8a; }
.card-header { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.org { font-size: .78rem; color: #5a6480; }
.card p { font-size: .875rem; color: #8892aa; line-height: 1.6; margin-bottom: 10px; }
.card code { background: #12122a; padding: 1px 5px; border-radius: 3px; font-size: .82rem; color: #a0b4e0; }
.stats-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 10px; }
.stat { font-size: .78rem; padding: 3px 9px; border-radius: 12px; font-weight: 600; }
.stat.in-fw    { background: #1a3a5e; color: #7ab4e8; }
.stat.ready    { background: #1a3a2e; color: #7ae8b4; }
.stat.possible { background: #2a2a1a; color: #d8c870; }
.best-for { font-size: .82rem; color: #6a7490; }
/* Framework badges */
.fw-badge { display: inline-block; font-size: .75rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; letter-spacing: .04em; }
.fw-badge.lm        { background: #1a2a5e; color: #7ab4ff; }
.fw-badge.inspect   { background: #3a1a5e; color: #c87aff; }
.fw-badge.lighteval { background: #1a3a5e; color: #7ae0ff; }
.fw-badge.helm      { background: #2a1a3e; color: #ff9aef; }
.fw-badge.oaievals  { background: #1a3a2a; color: #7affc8; }

/* Paper detail modal */
#paper-modal-overlay {
    display:none; position:fixed; inset:0; z-index:1000;
    background:rgba(0,0,0,0.65); backdrop-filter:blur(2px);
}
#paper-modal-overlay.visible { display:flex; align-items:center; justify-content:center; }
#paper-modal {
    background:#1a1a2e; border:1px solid #2a2a4a; border-radius:10px;
    width:90%; max-width:680px; max-height:80vh; overflow-y:auto;
    padding:28px 32px; position:relative; box-shadow:0 12px 40px rgba(0,0,0,0.5);
}
#paper-modal-close { position:absolute; top:12px; left:14px; background:none;
    border:none; color:#6a7490; font-size:1.3rem; cursor:pointer; padding:4px 8px; border-radius:4px; }
#paper-modal-close:hover { color:#c8d0e8; background:rgba(160,180,224,0.1); }
#paper-modal h3 { color:#a0b4e0; font-size:1.1rem; margin:0 0 16px 28px; line-height:1.4; }
.modal-field { display:flex; margin-bottom:8px; font-size:.82rem; }
.modal-label { color:#7888b8; min-width:130px; font-weight:600; flex-shrink:0; }
.modal-value { color:#c8d0e8; word-break:break-word; }
.modal-value a { color:#7ab4ff; text-decoration:none; }
.modal-value a:hover { text-decoration:underline; }
.modal-divider { border:none; border-top:1px solid #252545; margin:14px 0; }
.modal-section-title { color:#7888b8; font-size:.75rem; font-weight:700;
    text-transform:uppercase; letter-spacing:.5px; margin:14px 0 8px; }
"""

def make_overview_html(data):
    """Generate colorful, data-driven Overview panel."""
    # Extract row counts from actual data
    lm_rows = len(data['lm_eval']['data'])
    ea_rows = len(data['eleutherai']['data'])
    ins_rows = len(data['inspect']['data'])
    helm_rows = len(data['helm']['data'])
    le_rows = len(data['lighteval']['data'])
    oai_rows = len(data['openai']['data'])

    # Cross-framework summary counts
    lm_in = data['lm_eval']['tiers'].get('In Harness', 0)
    lm_ready = data['lm_eval']['tiers'].get('Ready', 0)
    lm_possible = data['lm_eval']['tiers'].get('Needs Dataset', 0)
    ins_in = data['inspect']['tiers'].get('In Inspect', 0)
    ins_ready = data['inspect']['tiers'].get('Ready', 0)
    ins_possible = data['inspect']['tiers'].get('Model-Graded', 0)
    le_ready = data['lighteval']['tiers'].get('Ready', 0)
    le_possible = data['lighteval']['tiers'].get('Possible', 0)
    helm_existing = sum(1 for d in data['helm']['data'] if d['phase'] == 'Existing')
    oai_ready = data['openai']['tiers'].get('Ready', 0)
    oai_possible = data['openai']['tiers'].get('Possible', 0)

    return f"""
<div id="panel-overview" class="tab-panel active fw-panel">
<div class="ov-inner">
<h1>Eval Framework Dashboard v3</h1>
<p>Cross-framework implementability analysis for the CEI Literature Vault.
Covers 2,043 papers across 6 evaluation frameworks: lm-eval-harness, EleutherAI,
UK AISI Inspect, HELM, LightEval, and OpenAI Evals.</p>

<div class="stat-row">
<div class="stat-card"><div class="sv">10</div><div class="sl">Tabs</div></div>
<div class="stat-card"><div class="sv">6</div><div class="sl">Frameworks</div></div>
<div class="stat-card"><div class="sv">2,043</div><div class="sl">Papers</div></div>
<div class="stat-card"><div class="sv">8</div><div class="sl">Source Reports</div></div>
</div>

<h2>Framework Coverage</h2>
<div class="stat-row">
<div class="stat-card sc-lm" style="cursor:pointer" onclick="switchTab('lmeval')"><div class="sv">{lm_rows:,}</div><div class="sl"><span class="chip chip-lm">lm-eval</span></div></div>
<div class="stat-card sc-ea" style="cursor:pointer" onclick="switchTab('eleutherai')"><div class="sv">{ea_rows:,}</div><div class="sl"><span class="chip chip-ea">EleutherAI</span></div></div>
<div class="stat-card sc-ins" style="cursor:pointer" onclick="switchTab('inspect')"><div class="sv">{ins_rows:,}</div><div class="sl"><span class="chip chip-ins">Inspect</span></div></div>
<div class="stat-card sc-helm" style="cursor:pointer" onclick="switchTab('helm')"><div class="sv">{helm_rows:,}</div><div class="sl"><span class="chip chip-helm">HELM</span></div></div>
<div class="stat-card sc-le" style="cursor:pointer" onclick="switchTab('lighteval')"><div class="sv">{le_rows:,}</div><div class="sl"><span class="chip chip-le">LightEval</span></div></div>
<div class="stat-card sc-oai" style="cursor:pointer" onclick="switchTab('openai')"><div class="sv">{oai_rows:,}</div><div class="sl"><span class="chip chip-oai">OpenAI Evals</span></div></div>
</div>

<h2>Tab Guide</h2>
<table class="tg">
<tr><th>#</th><th>Tab</th><th>Description</th><th>Papers</th></tr>
<tbody>
<tr style="cursor:pointer" onclick="switchTab('overview')"><td>1</td><td class="tn">Overview</td><td class="tc">This page &mdash; dashboard summary and tab guide</td><td>&mdash;</td></tr>
<tr style="cursor:pointer" onclick="switchTab('tab1')"><td>2</td><td class="tn">1. Incorporated papers</td><td class="tc">Papers already implemented in at least one framework</td><td>107</td></tr>
<tr style="cursor:pointer" onclick="switchTab('tab2')"><td>3</td><td class="tn">2. Implementability</td><td class="tc">Full cross-framework implementability matrix</td><td>2,043</td></tr>
<tr style="cursor:pointer" onclick="switchTab('tab3')"><td>4</td><td class="tn">3. Implement. for Ethics</td><td class="tc">Implementability matrix with ethics scores overlay</td><td>2,043</td></tr>
<tr style="cursor:pointer" onclick="switchTab('lmeval')"><td>5</td><td class="tn"><span class="chip chip-lm">lm-eval</span></td><td class="tc">lm-evaluation-harness: in-harness + ready papers</td><td>{lm_rows:,}</td></tr>
<tr style="cursor:pointer" onclick="switchTab('eleutherai')"><td>6</td><td class="tn"><span class="chip chip-ea">EleutherAI</span></td><td class="tc">EleutherAI harness integration: existing + new papers</td><td>{ea_rows:,}</td></tr>
<tr style="cursor:pointer" onclick="switchTab('inspect')"><td>7</td><td class="tn"><span class="chip chip-ins">Inspect</span></td><td class="tc">UK AISI Inspect: in-framework + ready + model-graded</td><td>{ins_rows:,}</td></tr>
<tr style="cursor:pointer" onclick="switchTab('helm')"><td>8</td><td class="tn"><span class="chip chip-helm">HELM</span></td><td class="tc">Stanford HELM values-alignment benchmarks</td><td>{helm_rows:,}</td></tr>
<tr style="cursor:pointer" onclick="switchTab('lighteval')"><td>9</td><td class="tn"><span class="chip chip-le">LightEval</span></td><td class="tc">HuggingFace LightEval: papers scored with 9-dimension breakdown</td><td>{le_rows:,}</td></tr>
<tr style="cursor:pointer" onclick="switchTab('openai')"><td>10</td><td class="tn"><span class="chip chip-oai">OpenAI Evals</span></td><td class="tc">OpenAI Evals: papers scored with template classification</td><td>{oai_rows:,}</td></tr>
</tbody>
</table>

<h2>Methodology</h2>
<p>Each paper is scored on 9 dimensions (dataset availability, public access,
framework-specific format support, code availability, clear metrics, data size,
LLM evaluation presence, task type identifiability, and full text availability)
weighted to a 10-point scale. Papers are tiered:
<span class="tier-badge tier-ready">Ready</span> (8+),
<span class="tier-badge tier-possible">Possible</span> (5&ndash;7.9),
<span class="tier-badge tier-barriers">Barriers</span> (2&ndash;4.9),
<span class="tier-badge tier-notimpl">Not Implementable</span> (&lt;2).</p>

<h2>Source Reports</h2>
<p>Generated 2026-03-12 from PDF extracts and paper metadata.
See STATISTICS/ for full markdown reports.</p>

<h2>Cross-Framework Summary</h2>
<table class="tg">
<tr><th>Framework</th><th>In Framework</th><th>Ready</th><th>Possible</th><th>Notes</th></tr>
<tbody>
<tr style="cursor:pointer" onclick="switchTab('lmeval')"><td class="tn"><span class="chip chip-lm">lm-eval</span></td><td>{lm_in}</td><td>{lm_ready}</td><td>{lm_possible}</td><td class="tc">EleutherAI &middot; 200+ benchmarks</td></tr>
<tr style="cursor:pointer" onclick="switchTab('inspect')"><td class="tn"><span class="chip chip-ins">Inspect</span></td><td>{ins_in}</td><td>{ins_ready}</td><td>{ins_possible}</td><td class="tc">UK AISI &middot; model_graded_qa unique</td></tr>
<tr style="cursor:pointer" onclick="switchTab('lighteval')"><td class="tn"><span class="chip chip-le">LightEval</span></td><td>&mdash;</td><td>{le_ready}</td><td>{le_possible}</td><td class="tc">HuggingFace &middot; no In-Framework tier</td></tr>
<tr style="cursor:pointer" onclick="switchTab('helm')"><td class="tn"><span class="chip chip-helm">HELM</span></td><td>{helm_existing}</td><td>&mdash;</td><td>&mdash;</td><td class="tc">Stanford CRFM &middot; holistic scenarios</td></tr>
<tr style="cursor:pointer" onclick="switchTab('openai')"><td class="tn"><span class="chip chip-oai">OpenAI Evals</span></td><td>&mdash;</td><td>{oai_ready}</td><td>{oai_possible}</td><td class="tc">All 2,043 papers scored</td></tr>
</tbody>
</table>
<p style="color:#6a7490;font-size:0.78rem;margin-top:8px">107 papers appear in &ge;1 framework (<span style="cursor:pointer;color:#7ab4ff" onclick="switchTab('tab1')">TABLE 1</span>).</p>

<h2>Framework Profiles</h2>

<div class="framework-cards">
<div class="card" style="cursor:pointer" onclick="switchTab('lmeval')">
  <div class="card-header">
    <span class="fw-badge lm">lm-eval</span>
    <span class="org">EleutherAI &middot; lm-evaluation-harness</span>
  </div>
  <p>Community-standard harness with 200+ benchmarks. Supports <code>multiple_choice</code>, <code>log-likelihood</code>, and <code>generate_until</code> task types.</p>
  <div class="stats-row">
    <span class="stat in-fw">{lm_in} In Framework</span>
    <span class="stat ready">{lm_ready} Ready</span>
    <span class="stat possible">{lm_possible} Possible</span>
  </div>
  <p class="best-for"><strong>Best for:</strong> reproducing published results; automated eval pipelines</p>
</div>

<div class="card" style="cursor:pointer" onclick="switchTab('inspect')">
  <div class="card-header">
    <span class="fw-badge inspect">Inspect</span>
    <span class="org">UK AI Safety Institute &middot; inspect_ai</span>
  </div>
  <p>Safety and alignment evals with <code>model_graded_qa()</code> scorer and rubric-based scenarios.</p>
  <div class="stats-row">
    <span class="stat in-fw">{ins_in} In Framework</span>
    <span class="stat ready">{ins_ready} Ready</span>
    <span class="stat possible">{ins_possible} Possible (model-graded)</span>
  </div>
  <p class="best-for"><strong>Best for:</strong> safety/alignment evals requiring LLM-as-judge</p>
</div>

<div class="card" style="cursor:pointer" onclick="switchTab('lighteval')">
  <div class="card-header">
    <span class="fw-badge lighteval">LightEval</span>
    <span class="org">HuggingFace &middot; lighteval</span>
  </div>
  <p>Lightweight HF-native harness with easiest HuggingFace dataset integration. No &ldquo;In Framework&rdquo; tier.</p>
  <div class="stats-row">
    <span class="stat ready">{le_ready} Ready</span>
    <span class="stat possible">{le_possible} Possible</span>
  </div>
  <p class="best-for"><strong>Best for:</strong> teams in the HF ecosystem; fast iteration</p>
</div>

<div class="card" style="cursor:pointer" onclick="switchTab('helm')">
  <div class="card-header">
    <span class="fw-badge helm">HELM</span>
    <span class="org">Stanford CRFM &middot; helm</span>
  </div>
  <p>Holistic evaluation with scenario abstraction and broadest metric coverage.</p>
  <div class="stats-row">
    <span class="stat in-fw">{helm_existing} In Framework</span>
  </div>
  <p class="best-for"><strong>Best for:</strong> comprehensive multi-metric evaluation</p>
</div>

<div class="card" style="cursor:pointer" onclick="switchTab('openai')">
  <div class="card-header">
    <span class="fw-badge oaievals">OpenAI Evals</span>
    <span class="org">OpenAI &middot; evals</span>
  </div>
  <p>JSONL registry with templates (<code>Match</code>, <code>ModelBasedClassify</code>, <code>FreeForm</code>). All 2,043 papers scored.</p>
  <div class="stats-row">
    <span class="stat ready">{oai_ready} Ready</span>
    <span class="stat possible">{oai_possible} Possible</span>
  </div>
  <p class="best-for"><strong>Best for:</strong> structured community contributions; judge-based evals</p>
</div>
</div>

</div>
</div>
"""


def generate_framework_panel(tab_id, title, tiers, columns, has_detail=False,
                             extra_filter=None, has_score_filter=False, narrative=''):
    """Generate HTML for a framework tab panel.

    Args:
        extra_filter: tuple (label, filter_id_suffix) for a secondary dropdown, or None
        has_score_filter: if True, add a score-range dropdown (for scored tabs)
    """
    cards = []
    for name, count in tiers.items():
        tier_esc = html_mod.escape(name)
        cards.append(
            f'<div class="stat-card clickable-card" data-tier="{tier_esc}" '
            f'onclick="filterByTier(\'{tab_id}\',\'{tier_esc}\')">'
            f'<div class="sv">{count:,}</div>'
            f'<div class="sl">{tier_esc}</div></div>'
        )

    tier_opts = ''.join(
        f'<option value="{html_mod.escape(t)}">{html_mod.escape(t)}</option>'
        for t in tiers
    )

    hdrs = ''.join(
        f'<th onclick="sortCol(\'{tab_id}\',{i})">{html_mod.escape(c)}</th>'
        for i, c in enumerate(columns)
    )

    detail_note = ''
    if has_detail:
        detail_note = '<p style="color:#5a6480;font-size:0.72rem;margin-bottom:10px">Click any row for paper details and dimension breakdown</p>'

    # Extra filter dropdown
    extra_html = ''
    if extra_filter:
        label, suffix = extra_filter
        extra_html = (
            f'<select id="extra-{tab_id}" onchange="doFilter(\'{tab_id}\')">'
            f'<option value="">All {html_mod.escape(label)}</option>'
            f'</select>'
        )

    # Score range filter dropdown
    score_html = ''
    if has_score_filter:
        score_html = (
            f'<select id="score-{tab_id}" onchange="doFilter(\'{tab_id}\')">'
            f'<option value="">All Scores</option>'
            f'<option value="8">8+ (Ready)</option>'
            f'<option value="5">5\u20137.9 (Possible)</option>'
            f'<option value="2">2\u20134.9 (Barriers)</option>'
            f'<option value="0">&lt;2 (Not Implementable)</option>'
            f'</select>'
        )

    narrative_html = ''
    if narrative:
        narrative_html = f'<p style="color:#6a7490;font-size:0.82rem;line-height:1.6;margin:0 0 16px;max-width:1100px">{narrative}</p>'

    return f'''<div id="panel-{tab_id}" class="tab-panel fw-panel">
<div class="fw-inner">
<h2 class="fw-title">{html_mod.escape(title)}</h2>
{narrative_html}
<div class="stat-row">{"".join(cards)}</div>
<div class="controls">
<input type="text" id="search-{tab_id}" placeholder="Search papers\u2026" oninput="doFilter('{tab_id}')">
<select id="tier-{tab_id}" onchange="doFilter('{tab_id}')">
<option value="">All Tiers</option>
{tier_opts}
</select>
{extra_html}
{score_html}
<span class="cnt">Showing <b id="count-{tab_id}">0</b> papers</span>
</div>
{detail_note}
<div class="table-wrap">
<table class="fw-table"><thead><tr>{hdrs}</tr></thead>
<tbody id="tbody-{tab_id}"></tbody></table>
</div>
</div></div>'''


JS_CODE = r"""
// === Tab switching ===
var ACTIVE_TAB = 'overview';
function switchTab(name) {
    document.querySelectorAll('.tab-panel').forEach(function(p){ p.classList.remove('active'); });
    document.querySelectorAll('.tab-btn').forEach(function(b){ b.classList.remove('active'); });
    var panel = document.getElementById('panel-' + name);
    if (panel) panel.classList.add('active');
    var btns = document.querySelectorAll('.tab-btn');
    var names = TAB_NAMES;
    for (var i = 0; i < names.length; i++) {
        if (names[i] === name && btns[i]) btns[i].classList.add('active');
    }
    ACTIVE_TAB = name;
    if (!tabInited[name] && TAB_DATA[name]) {
        tabInited[name] = true;
        initExtraFilter(name);
        doFilter(name);
    }
}

var TAB_NAMES = ['overview','tab1','tab2','tab3','lmeval','eleutherai','inspect','helm','lighteval','openai'];
var tabInited = {};

// === Tier badge class mapping ===
function tierCls(tier) {
    var m = {
        'In Harness':'IMPLEMENTED','In Inspect':'IMPLEMENTED','Existing':'IMPLEMENTED',
        'Ready':'READY','New':'READY',
        'Possible':'POSSIBLE','Model-Graded':'POSSIBLE',
        'Needs Dataset':'BARRIERS','Needs Info':'BARRIERS','Barriers':'BARRIERS',
        'Not Implementable':'NOT_FEASIBLE','Tagged':'IMPLEMENTED'
    };
    return m[tier] || 'N_A';
}

function esc(s) {
    if (!s) return '';
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function urlCell(u) {
    if (!u || u === 'NA' || u === '' || u === 'None') return '<span style="color:#3a4060">\u2014</span>';
    var short = u.length > 40 ? u.substring(0,37) + '\u2026' : u;
    return '<a href="' + esc(u) + '" target="_blank" rel="noopener" onclick="event.stopPropagation()">' + esc(short) + '</a>';
}

// === Dimension constants ===
var LE_DIMS = ["Dataset exists","Data publicly available","HuggingFace presence","Code/repo available","Clear eval metrics","Quantified data size","LLM evaluation exists","Task type identifiable","Full text available"];
var LE_WEIGHTS = [1.5,1.5,2.0,1.0,1.0,0.5,0.5,1.0,1.0];
var OA_DIMS = ["Dataset exists","Data publicly available","JSONL-convertible format","Code/repo available","Clear eval metrics","Quantified data size","LLM evaluation exists","Eval template mappable","Full text available"];
var OA_WEIGHTS = [1.5,1.5,1.5,1.0,1.0,0.5,0.5,1.5,1.0];

// === Row renderers ===
var RENDERERS = {
    lmeval: function(r, idx) {
        return '<tr class="clickable" onclick="showPaperModal(\'lmeval\',' + idx + ')"><td>' + esc(r.k) + '</td>'
            + '<td><span class="badge ' + tierCls(r.tier) + '">' + esc(r.tier) + '</span></td>'
            + '<td>' + (r.score || '\u2014') + '</td>'
            + '<td>' + esc(r.bench) + '</td>'
            + '<td>' + esc(r.type) + '</td>'
            + '<td>' + urlCell(r.url) + '</td>'
            + '<td class="notes-cell" title="' + esc(r.notes) + '">' + esc(r.notes || '\u2014') + '</td></tr>';
    },
    eleutherai: function(r, idx) {
        return '<tr class="clickable" onclick="showPaperModal(\'eleutherai\',' + idx + ')"><td>' + esc(r.k) + '</td>'
            + '<td><span class="badge ' + tierCls(r.cat) + '">' + esc(r.cat) + '</span></td>'
            + '<td>' + esc(r.bench) + '</td>'
            + '<td>' + esc(r.task) + '</td>'
            + '<td class="notes-cell">' + esc(r.extra || '\u2014') + '</td></tr>';
    },
    inspect: function(r, idx) {
        return '<tr class="clickable" onclick="showPaperModal(\'inspect\',' + idx + ')"><td>' + esc(r.k) + '</td>'
            + '<td><span class="badge ' + tierCls(r.tier) + '">' + esc(r.tier) + '</span></td>'
            + '<td>' + (r.score || '\u2014') + '</td>'
            + '<td>' + esc(r.detail) + '</td>'
            + '<td>' + esc(r.cat) + '</td>'
            + '<td>' + esc(r.scorer) + '</td>'
            + '<td class="notes-cell" title="' + esc(r.notes) + '">' + esc(r.notes || '\u2014') + '</td></tr>';
    },
    helm: function(r, idx) {
        return '<tr class="clickable" onclick="showPaperModal(\'helm\',' + idx + ')"><td>' + esc(r.k) + '</td>'
            + '<td><span class="badge ' + tierCls(r.phase) + '">' + esc(r.phase) + '</span></td>'
            + '<td>' + esc(r.bench) + '</td>'
            + '<td>' + esc(r.status) + '</td></tr>';
    },
    lighteval: function(r, idx) {
        return '<tr class="clickable" onclick="showPaperModal(\'lighteval\',' + idx + ')">'
            + '<td>' + esc(r.k) + '</td>'
            + '<td>' + r.s.toFixed(1) + '</td>'
            + '<td><span class="badge ' + tierCls(r.t) + '">' + esc(r.t) + '</span></td>'
            + '<td>' + esc(r.ty) + '</td>'
            + '<td>' + r.m + '</td></tr>';
    },
    openai: function(r, idx) {
        return '<tr class="clickable" onclick="showPaperModal(\'openai\',' + idx + ')">'
            + '<td>' + esc(r.k) + '</td>'
            + '<td>' + r.s.toFixed(1) + '</td>'
            + '<td><span class="badge ' + tierCls(r.t) + '">' + esc(r.t) + '</span></td>'
            + '<td>' + esc(r.ty) + '</td>'
            + '<td>' + r.m + '</td></tr>';
    }
};

function dimTable(d, dims, weights) {
    var h = '<table class="dim-table"><tr><th>Dimension</th><th>Weight</th><th>Raw</th><th>Weighted</th></tr>';
    var total = 0;
    for (var i = 0; i < 9; i++) {
        var raw = d[i];
        var w = raw * weights[i];
        total += w;
        var sym = raw >= 1 ? '\u2713' : raw >= 0.5 ? '\u25d0' : '\u2717';
        var cls = raw >= 1 ? 'dim-ok' : raw >= 0.5 ? 'dim-part' : 'dim-miss';
        h += '<tr><td>' + dims[i] + '</td><td>' + weights[i].toFixed(1) + '</td>'
            + '<td class="' + cls + '">' + sym + ' ' + raw.toFixed(1) + '</td>'
            + '<td>' + w.toFixed(1) + '</td></tr>';
    }
    h += '<tr style="font-weight:700"><td>Total</td><td>' + weights.reduce(function(a,b){return a+b;},0).toFixed(1)
        + '</td><td></td><td>' + total.toFixed(1) + '</td></tr></table>';
    return h;
}

// === Paper detail modal ===
var FIELD_LABELS = {
    lmeval: [['tier','Tier'],['score','Score'],['bench','Benchmark / Task'],
             ['type','Type / Method'],['url','Data URL'],['notes','Notes']],
    eleutherai: [['cat','Category'],['bench','Benchmark / Key'],
                 ['task','Task ID'],['extra','Classification']],
    inspect: [['tier','Tier'],['score','Score'],['detail','Eval / Pattern'],
              ['cat','Category'],['scorer','Scorer'],['notes','Notes']],
    helm: [['phase','Phase'],['bench','Benchmark'],['status','Status']],
    lighteval: [['s','Score'],['t','Tier'],['ty','Task Type'],['m','Missing Dimensions']],
    openai: [['s','Score'],['t','Tier'],['ty','Template'],['m','Missing Dimensions']]
};

// === Bibliographic info renderer ===
function renderBiblio(info) {
    var h = '';
    if (info.t) h += '<div class="modal-field"><span class="modal-label">Title</span><span class="modal-value">' + esc(info.t) + '</span></div>';
    if (info.a) h += '<div class="modal-field"><span class="modal-label">Authors</span><span class="modal-value">' + esc(info.a) + '</span></div>';
    if (info.y) h += '<div class="modal-field"><span class="modal-label">Year</span><span class="modal-value">' + esc(info.y) + '</span></div>';
    if (info.p) h += '<div class="modal-field"><span class="modal-label">Publication</span><span class="modal-value">' + esc(info.p) + '</span></div>';
    if (info.d) h += '<div class="modal-field"><span class="modal-label">DOI</span><span class="modal-value"><a href="https://doi.org/' + esc(info.d) + '" target="_blank" rel="noopener" onclick="event.stopPropagation()">' + esc(info.d) + '</a></span></div>';
    if (info.u) h += '<div class="modal-field"><span class="modal-label">URL</span><span class="modal-value"><a href="' + esc(info.u) + '" target="_blank" rel="noopener" onclick="event.stopPropagation()">' + esc(info.u) + '</a></span></div>';
    if (info.ab) h += '<div class="modal-field" style="flex-direction:column"><span class="modal-label" style="margin-bottom:4px">Abstract</span><span class="modal-value" style="max-height:200px;overflow-y:auto;font-size:0.78rem;line-height:1.5">' + esc(info.ab) + '</span></div>';
    return h;
}

function showPaperModal(tabId, idx) {
    var r = TAB_DATA[tabId][idx];
    if (!r) return;
    document.getElementById('paper-modal-title').textContent = r.k;
    var body = document.getElementById('paper-modal-body');
    var html = '';

    // Bibliographic info first
    var info = PAPER_INFO[r.k];
    if (info) {
        html += renderBiblio(info);
        html += '<hr class="modal-divider">';
        html += '<div class="modal-section-title">Framework Details</div>';
    }

    var fields = FIELD_LABELS[tabId] || [];
    for (var i = 0; i < fields.length; i++) {
        var key = fields[i][0], label = fields[i][1];
        var val = r[key];
        if (val === undefined || val === null) val = '';
        var valStr = '';
        // Format scores
        if (key === 's' && typeof val === 'number') {
            valStr = val.toFixed(1) + ' / 10.0';
        } else if (key === 'score' && val) {
            valStr = val;
        // Format URLs as links
        } else if (key === 'url' && val && val !== 'NA' && val !== 'None' && val !== '') {
            valStr = '<a href="' + esc(val) + '" target="_blank" rel="noopener" onclick="event.stopPropagation()">' + esc(val) + '</a>';
        // Format tiers/phases as badges
        } else if (key === 'tier' || key === 'phase' || key === 't') {
            valStr = '<span class="badge ' + tierCls(String(val)) + '">' + esc(String(val)) + '</span>';
        } else {
            valStr = esc(String(val || '\u2014'));
        }
        html += '<div class="modal-field"><span class="modal-label">' + label + '</span><span class="modal-value">' + valStr + '</span></div>';
    }
    // Dimension breakdown for lighteval/openai
    if ((tabId === 'lighteval' || tabId === 'openai') && r.d) {
        html += '<hr class="modal-divider">';
        html += '<div class="modal-section-title">Dimension Breakdown</div>';
        var dims = tabId === 'lighteval' ? LE_DIMS : OA_DIMS;
        var weights = tabId === 'lighteval' ? LE_WEIGHTS : OA_WEIGHTS;
        html += dimTable(r.d, dims, weights);
    }
    body.innerHTML = html;
    document.getElementById('paper-modal-overlay').classList.add('visible');
}

// === Modal for iframe-based tabs (biblio only) ===
function showPaperModalByKey(paperKey) {
    var info = PAPER_INFO[paperKey];
    document.getElementById('paper-modal-title').textContent = paperKey;
    var body = document.getElementById('paper-modal-body');
    if (info) {
        body.innerHTML = renderBiblio(info);
    } else {
        body.innerHTML = '<div class="modal-field"><span class="modal-value" style="color:#6a7490">Paper metadata not available</span></div>';
    }
    document.getElementById('paper-modal-overlay').classList.add('visible');
}

// === Setup click handlers for iframe rows ===
function setupIframeClicks() {
    var iframes = document.querySelectorAll('.tab-panel iframe');
    for (var i = 0; i < iframes.length; i++) {
        (function(iframe) {
            function attach() {
                try {
                    var doc = iframe.contentDocument;
                    if (!doc || !doc.body) return;
                    // Inject cursor style
                    var style = doc.createElement('style');
                    style.textContent = 'tbody tr, #tableBody tr { cursor: pointer; } tbody tr:hover, #tableBody tr:hover { background: rgba(160,180,224,0.08) !important; }';
                    doc.head.appendChild(style);
                    // Find tbody — either #tableBody or first <tbody>
                    var tbody = doc.getElementById('tableBody') || doc.querySelector('tbody');
                    if (!tbody) return;
                    tbody.addEventListener('click', function(e) {
                        // Don't intercept link clicks
                        if (e.target.tagName === 'A') return;
                        var row = e.target.closest('tr');
                        if (!row) return;
                        // Extract paper key from .paper-key or .key span
                        var keyEl = row.querySelector('.paper-key, .key');
                        if (keyEl) {
                            window.showPaperModalByKey(keyEl.textContent.trim());
                        }
                    });
                } catch(ex) {
                    // Cross-origin or not ready — silently skip
                }
            }
            if (iframe.contentDocument && iframe.contentDocument.readyState === 'complete') {
                attach();
            }
            iframe.addEventListener('load', attach);
        })(iframes[i]);
    }
}

function closePaperModal(event) {
    var overlay = document.getElementById('paper-modal-overlay');
    if (event.target === overlay || event.target.id === 'paper-modal-close' || event.type === 'keydown') {
        overlay.classList.remove('visible');
    }
}

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closePaperModal(e);
});

// === Clickable stat cards ===
function filterByTier(tabId, tier) {
    var sel = document.getElementById('tier-' + tabId);
    if (!sel) return;
    sel.value = (sel.value === tier) ? '' : tier;
    highlightCard(tabId, sel.value);
    doFilter(tabId);
}

function highlightCard(tabId, activeTier) {
    var panel = document.getElementById('panel-' + tabId);
    if (!panel) return;
    panel.querySelectorAll('.stat-card').forEach(function(c) {
        c.classList.remove('active-card');
    });
    if (activeTier) {
        panel.querySelectorAll('.stat-card').forEach(function(c) {
            if (c.getAttribute('data-tier') === activeTier) c.classList.add('active-card');
        });
    }
}

// === Extra filter (second dimension) ===
function getExtra(tabId, r) {
    if (tabId === 'lmeval') return r.type || '';
    if (tabId === 'inspect') return r.cat || '';
    if (tabId === 'lighteval' || tabId === 'openai') return r.ty || '';
    return '';
}

function initExtraFilter(tabId) {
    var sel = document.getElementById('extra-' + tabId);
    if (!sel) return;
    var data = TAB_DATA[tabId];
    if (!data) return;
    var vals = {};
    for (var i = 0; i < data.length; i++) {
        var v = getExtra(tabId, data[i]);
        if (v) vals[v] = true;
    }
    var sorted = Object.keys(vals).sort();
    for (var j = 0; j < sorted.length; j++) {
        var opt = document.createElement('option');
        opt.value = sorted[j];
        opt.textContent = sorted[j];
        sel.appendChild(opt);
    }
}

// === Filtering ===
function getTier(tabId, r) {
    if (tabId === 'lmeval') return r.tier;
    if (tabId === 'eleutherai') return r.cat;
    if (tabId === 'inspect') return r.tier;
    if (tabId === 'helm') return r.phase;
    if (tabId === 'lighteval' || tabId === 'openai') return r.t;
    return '';
}

function getScore(tabId, r) {
    if (tabId === 'lighteval' || tabId === 'openai') return r.s;
    return null;
}

function doFilter(tabId) {
    var data = TAB_DATA[tabId];
    if (!data) return;
    var searchEl = document.getElementById('search-' + tabId);
    var tierEl = document.getElementById('tier-' + tabId);
    var extraEl = document.getElementById('extra-' + tabId);
    var scoreEl = document.getElementById('score-' + tabId);
    var search = searchEl ? searchEl.value.toLowerCase() : '';
    var tierFilter = tierEl ? tierEl.value : '';
    var extraFilter = extraEl ? extraEl.value : '';
    var scoreFilter = scoreEl ? scoreEl.value : '';

    // Sync card highlight with dropdown
    highlightCard(tabId, tierFilter);

    var filtered = [];
    for (var i = 0; i < data.length; i++) {
        var r = data[i];
        if (search && r.k.toLowerCase().indexOf(search) === -1) continue;
        if (tierFilter && getTier(tabId, r) !== tierFilter) continue;
        if (extraFilter && getExtra(tabId, r) !== extraFilter) continue;
        if (scoreFilter) {
            var s = getScore(tabId, r);
            if (s !== null) {
                var sv = parseFloat(scoreFilter);
                if (sv >= 8 && s < 8) continue;
                if (sv >= 5 && sv < 8 && (s < 5 || s >= 8)) continue;
                if (sv >= 2 && sv < 5 && (s < 2 || s >= 5)) continue;
                if (sv < 2 && s >= 2) continue;
            }
        }
        filtered.push({r: r, i: i});
    }

    var tbody = document.getElementById('tbody-' + tabId);
    if (!tbody) return;

    var renderer = RENDERERS[tabId];
    var parts = [];
    for (var j = 0; j < filtered.length; j++) {
        parts.push(renderer(filtered[j].r, filtered[j].i));
    }
    tbody.innerHTML = parts.join('');

    var countEl = document.getElementById('count-' + tabId);
    if (countEl) countEl.textContent = filtered.length;
}

// === Sorting ===
var sortState = {};

function getSortKey(tabId, r, col) {
    if (tabId === 'lmeval') {
        var keys = [r.k, r.tier, parseFloat(r.score)||0, r.bench, r.type, r.url, r.notes];
        return keys[col];
    }
    if (tabId === 'eleutherai') {
        var keys = [r.k, r.cat, r.bench, r.task, r.extra];
        return keys[col];
    }
    if (tabId === 'inspect') {
        var keys = [r.k, r.tier, parseFloat(r.score)||0, r.detail, r.cat, r.scorer, r.notes];
        return keys[col];
    }
    if (tabId === 'helm') {
        var keys = [r.k, r.phase, r.bench, r.status];
        return keys[col];
    }
    if (tabId === 'lighteval' || tabId === 'openai') {
        var keys = [r.k, r.s, r.t || r.ty, r.ty || r.t, r.m];
        return keys[col];
    }
    return '';
}

function sortCol(tabId, col) {
    var key = tabId + '-' + col;
    sortState[key] = sortState[key] === 'asc' ? 'desc' : 'asc';
    var dir = sortState[key];
    var data = TAB_DATA[tabId];
    if (!data) return;

    data.sort(function(a, b) {
        var va = getSortKey(tabId, a, col);
        var vb = getSortKey(tabId, b, col);
        var na = typeof va === 'number' ? va : parseFloat(va);
        var nb = typeof vb === 'number' ? vb : parseFloat(vb);
        if (!isNaN(na) && !isNaN(nb)) {
            return dir === 'asc' ? na - nb : nb - na;
        }
        va = String(va || ''); vb = String(vb || '');
        return dir === 'asc' ? va.localeCompare(vb) : vb.localeCompare(va);
    });
    doFilter(tabId);
}

// Init iframe click handlers on load
setupIframeClicks();
"""


def build_html(data, iframes, paper_info):
    """Assemble the complete HTML file."""
    parts = []

    # DOCTYPE + head
    parts.append('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    parts.append('<meta charset="UTF-8">\n')
    parts.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    parts.append('<title>Eval Framework Dashboard v3 — CEI Literature Vault</title>\n')
    parts.append('<style>\n')
    parts.append(CSS)
    parts.append('</style>\n</head>\n<body>\n')

    # Header
    parts.append('<div id="header">\n')
    parts.append('<h1>Eval Framework Dashboard v3</h1>\n')
    parts.append('<span class="subtitle">CEI Literature Vault \u2014 2,043 papers \u00d7 6 frameworks \u2014 Generated 2026-03-13</span>\n')
    parts.append('</div>\n')

    # Tab bar
    tab_defs = [
        ('overview', 'Overview', ''),
        ('tab1', '1. Incorporated papers', ''),
        ('tab2', '2. Implementability', ''),
        ('tab3', '3. Implement. for Ethics', ''),
        ('lmeval', 'lm-eval', 'tab-lm'),
        ('eleutherai', 'EleutherAI', 'tab-ea'),
        ('inspect', 'Inspect', 'tab-ins'),
        ('helm', 'HELM', 'tab-helm'),
        ('lighteval', 'LightEval', 'tab-le'),
        ('openai', 'OpenAI Evals', 'tab-oai'),
    ]

    parts.append('<div id="tabbar">\n')
    for i, (tid, label, cls) in enumerate(tab_defs):
        active = ' active' if i == 0 else ''
        extra = f' {cls}' if cls else ''
        parts.append(f'<button class="tab-btn{active}{extra}" onclick="switchTab(\'{tid}\')">{html_mod.escape(label)}</button>\n')
    parts.append('</div>\n')

    # Content area
    parts.append('<div id="content-area">\n')

    # Overview panel (data-driven)
    parts.append(make_overview_html(data))

    # --- Narrative text for each tab ---
    narrative_tab1 = ('Papers already implemented in at least one of the six evaluation frameworks. '
                      'Identified by cross-referencing CEI vault papers against each framework\u2019s '
                      'task registry, benchmark lists, and integration documentation. These 107 papers '
                      'represent benchmarks with confirmed existing implementations \u2014 the strongest '
                      'candidates for immediate ethics-focused evaluation work.')
    narrative_tab2 = ('Full cross-framework implementability matrix covering all 2,043 papers. '
                      'Each paper is scored on 9 dimensions (dataset availability, public access, '
                      'framework format support, code availability, clear metrics, data size, '
                      'LLM evaluation presence, task type identifiability, and full text availability) '
                      'weighted to a 10-point scale. Tier assignments: Ready (8+), Possible (5\u20137.9), '
                      'Barriers (2\u20134.9), Not Implementable (&lt;2).')
    narrative_tab3 = ('The same implementability matrix as Tab 2, overlaid with ethics classification '
                      'scores from the CEI pipeline. This view highlights which ethics-relevant papers '
                      'are most actionable for framework integration \u2014 combining technical '
                      'implementability with normative relevance to prioritize evaluation development.')

    lm_rows = len(data['lm_eval']['data'])
    ea_existing = sum(1 for d in data['eleutherai']['data'] if d['cat'] == 'Existing')
    ea_new = sum(1 for d in data['eleutherai']['data'] if d['cat'] == 'New')
    ins_rows = len(data['inspect']['data'])
    ins_tiers = len(data['inspect']['tiers'])
    helm_existing = sum(1 for d in data['helm']['data'] if d['phase'] == 'Existing')
    helm_new = sum(1 for d in data['helm']['data'] if d['phase'] == 'New')
    le_rows = len(data['lighteval']['data'])
    oai_rows = len(data['openai']['data'])

    narrative_lmeval = (f'EleutherAI\u2019s lm-evaluation-harness \u2014 the most widely adopted '
                        f'open-source LLM evaluation framework. Papers were matched against the '
                        f'harness task registry by benchmark name, dataset identifier, and task type. '
                        f'This tab covers {lm_rows:,} papers with tier breakdowns showing which are '
                        f'already in the harness, ready for integration, or blocked by missing data.')
    narrative_eleutherai = (f'EleutherAI harness integration analysis distinguishing between papers '
                            f'with existing task implementations and new candidates identified from '
                            f'the CEI vault. The {ea_existing} existing entries map to registered '
                            f'harness tasks; {ea_new} new papers were identified as potential additions '
                            f'based on dataset availability and format compatibility.')
    narrative_inspect = (f'UK AI Safety Institute\u2019s Inspect framework \u2014 purpose-built for '
                         f'safety and alignment evaluations with support for model-graded scoring. '
                         f'Papers were scored on implementability and categorized by evaluation pattern '
                         f'(direct scoring, model-graded, multi-turn). This tab covers {ins_rows:,} '
                         f'papers across {ins_tiers} tiers.')
    narrative_helm = (f'Stanford\u2019s Holistic Evaluation of Language Models (HELM) \u2014 focused '
                      f'on values-alignment benchmarks. Papers were matched against HELM\u2019s scenario '
                      f'registry and assessed for integration potential. This tab covers '
                      f'{helm_existing + helm_new} papers split between {helm_existing} already tagged '
                      f'in HELM and {helm_new} new candidates from the CEI vault.')
    narrative_lighteval = (f'HuggingFace\u2019s LightEval framework with a 9-dimension weighted '
                           f'scoring breakdown. Each paper receives dimension-level scores that can be '
                           f'expanded by clicking a row. This tab covers {le_rows:,} papers. Click any '
                           f'row for paper details and the full dimension breakdown.')
    narrative_openai = (f'OpenAI\u2019s evaluation framework with template-based classification. '
                        f'Each paper is scored on 9 dimensions weighted for OpenAI\u2019s '
                        f'JSONL-convertible format and eval template mapping requirements. This tab '
                        f'covers {oai_rows:,} papers. Click any row for paper details and dimension breakdown.')

    # Existing iframe panels (tabs 1-3) with narratives
    tab_narratives = [narrative_tab1, narrative_tab2, narrative_tab3]
    for i, iframe_content in enumerate(iframes[:3]):
        tid = f'tab{i+1}'
        parts.append(f'<div id="panel-{tid}" class="tab-panel has-narrative">\n')
        parts.append(f'<div class="tab-narrative">{tab_narratives[i]}</div>\n')
        parts.append(f'<iframe srcdoc="{iframe_content}"></iframe>\n')
        parts.append('</div>\n')

    # lm-eval panel
    parts.append(generate_framework_panel(
        'lmeval', 'lm-eval-harness',
        data['lm_eval']['tiers'],
        ['Paper', 'Tier', 'Score', 'Benchmark / Task', 'Type / Method', 'Data URL', 'Notes'],
        extra_filter=('Types', 'type'),
        narrative=narrative_lmeval
    ))

    # EleutherAI panel
    parts.append(generate_framework_panel(
        'eleutherai', 'EleutherAI lm-evaluation-harness',
        {'Existing': ea_existing, 'New': ea_new},
        ['Paper', 'Category', 'Benchmark / Key', 'Task ID', 'Classification'],
        narrative=narrative_eleutherai
    ))

    # Inspect panel
    parts.append(generate_framework_panel(
        'inspect', 'UK AISI Inspect',
        data['inspect']['tiers'],
        ['Paper', 'Tier', 'Score', 'Eval / Pattern', 'Category', 'Scorer', 'Notes'],
        extra_filter=('Categories', 'cat'),
        narrative=narrative_inspect
    ))

    # HELM panel
    parts.append(generate_framework_panel(
        'helm', 'HELM Values-Alignment',
        {'Existing': helm_existing, 'New': helm_new},
        ['Paper / File', 'Phase', 'Benchmark', 'Status'],
        narrative=narrative_helm
    ))

    # LightEval panel
    parts.append(generate_framework_panel(
        'lighteval', 'LightEval (HuggingFace)',
        data['lighteval']['tiers'],
        ['Paper', 'Score', 'Tier', 'Task Type', 'Missing Dims'],
        has_detail=True,
        extra_filter=('Task Types', 'tasktype'),
        has_score_filter=True,
        narrative=narrative_lighteval
    ))

    # OpenAI Evals panel
    parts.append(generate_framework_panel(
        'openai', 'OpenAI Evals',
        data['openai']['tiers'],
        ['Paper', 'Score', 'Tier', 'Template', 'Missing Dims'],
        has_detail=True,
        extra_filter=('Templates', 'template'),
        has_score_filter=True,
        narrative=narrative_openai
    ))

    # Paper detail modal
    parts.append('<div id="paper-modal-overlay" onclick="closePaperModal(event)">\n')
    parts.append('<div id="paper-modal">\n')
    parts.append('<button id="paper-modal-close" onclick="closePaperModal(event)">&times;</button>\n')
    parts.append('<h3 id="paper-modal-title"></h3>\n')
    parts.append('<div id="paper-modal-body"></div>\n')
    parts.append('</div>\n</div>\n')

    parts.append('</div>\n')  # end content-area

    # JavaScript: data + rendering code
    parts.append('<script>\n')

    # Embed data
    parts.append('var TAB_DATA = {};\n')
    parts.append(f'TAB_DATA.lmeval = {json.dumps(data["lm_eval"]["data"], ensure_ascii=False)};\n')
    parts.append(f'TAB_DATA.eleutherai = {json.dumps(data["eleutherai"]["data"], ensure_ascii=False)};\n')
    parts.append(f'TAB_DATA.inspect = {json.dumps(data["inspect"]["data"], ensure_ascii=False)};\n')
    parts.append(f'TAB_DATA.helm = {json.dumps(data["helm"]["data"], ensure_ascii=False)};\n')
    parts.append(f'TAB_DATA.lighteval = {json.dumps(data["lighteval"]["data"], ensure_ascii=False)};\n')
    parts.append(f'TAB_DATA.openai = {json.dumps(data["openai"]["data"], ensure_ascii=False)};\n')

    # Paper bibliographic info for modals
    parts.append(f'var PAPER_INFO = {json.dumps(paper_info, ensure_ascii=False)};\n')

    # JS rendering code
    parts.append(JS_CODE)
    parts.append('\n</script>\n')

    parts.append('</body>\n</html>\n')

    return ''.join(parts)


# ============================================================
# 5. MAIN
# ============================================================

def main():
    print("Parsing reports...")

    lm_eval = parse_lm_eval()
    print(f"  lm-eval: {len(lm_eval['data'])} rows")

    eleutherai = parse_eleutherai()
    print(f"  EleutherAI: {len(eleutherai['data'])} rows")

    inspect = parse_inspect()
    print(f"  Inspect: {len(inspect['data'])} rows")

    helm = parse_helm()
    print(f"  HELM: {len(helm['data'])} rows")

    lighteval = parse_lighteval()
    print(f"  LightEval: {len(lighteval['data'])} rows")

    openai = parse_openai()
    print(f"  OpenAI Evals: {len(openai['data'])} rows")

    print("Loading paper bibliographic info...")
    paper_info = load_paper_info()

    print("Extracting existing dashboard iframes...")
    iframes = extract_iframes()
    print(f"  Found {len(iframes)} iframes")

    data = {
        'lm_eval': lm_eval,
        'eleutherai': eleutherai,
        'inspect': inspect,
        'helm': helm,
        'lighteval': lighteval,
        'openai': openai,
    }

    print("Generating HTML...")
    html = build_html(data, iframes, paper_info)

    OUTPUT.write_text(html, encoding='utf-8')
    size_mb = len(html.encode('utf-8')) / (1024 * 1024)
    print(f"Output: {OUTPUT}")
    print(f"Size: {size_mb:.1f} MB")
    print(f"Total data rows: {sum(len(d['data']) for d in data.values()):,}")


if __name__ == '__main__':
    main()
