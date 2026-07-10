"""
Generate dashboard v8 = v7 + two new tabs:
  - Tab 7 "Gate-Passers" : the 47 papers that passed both quality gates
    (Religious Discriminability >= 30 AND public data URL available).
  - Tab 8 "All Candidates" : the full 401-paper screening corpus, with a
    gate-status badge per row and an exclusion-reason breakdown.

Strategy: fork-by-injection.  Read the v7 HTML byte-for-byte, surgically
inject two new <li>s in the nav-tabs and two new <div class="tab-pane">s
before the tab-content closer.  v7 source files are not modified.

All client-side rendering uses DOM API (createElement / textContent) rather
than innerHTML, per the vault's security-hook policy.

Inputs:
  - dashboard/20260413-religious-values-dashboard-v7.html        (base)
  - data/20260404-religious-benchmark-feature-matrix-v2.json     (401 rows)

Output:
  - dashboard/20260430-religious-values-dashboard-v8.html
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V7_HTML = ROOT / "dashboard" / "20260413-religious-values-dashboard-v7.html"
FEATURE_MATRIX = ROOT / "data" / "20260404-religious-benchmark-feature-matrix-v2.json"
V8_HTML = ROOT / "dashboard" / "20260430-religious-values-dashboard-v8.html"


URL_RE = re.compile(r'https?://[^\s"\'<>]+')


def clean_url(raw):
    if not raw:
        return ""
    raw = raw.strip()
    if raw.upper() in {"NA", "N/A", "NONE", ""}:
        return ""
    m = URL_RE.search(raw)
    if not m:
        return ""
    return m.group(0).rstrip(".,;)\"'")


def first_url(raw):
    """Some DATA_URL fields contain comma-separated URLs; take the first."""
    if not raw:
        return ""
    parts = re.split(r"[,\s]+", raw)
    for p in parts:
        u = clean_url(p)
        if u:
            return u
    return clean_url(raw)


def detect_arxiv(url):
    m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", url)
    return m.group(1) if m else ""


def _row_from_entry(e, rank):
    paper_url = clean_url(e.get("url", ""))
    data_url = first_url(e.get("DATA_URL", ""))
    arxiv_id = detect_arxiv(paper_url)
    return {
        "rank": rank,
        "title": (e.get("short_title") or "").strip(),
        "first_author": (e.get("first_author") or "").strip(),
        "year": str(e.get("year") or ""),
        "tradition": e.get("D5_primary_tradition") or "",
        "family": e.get("D6_tradition_family") or "",
        "format": e.get("P1_format") or "",
        "composite": round(float(e["COMPOSITE"]), 1),
        "rd": round(float(e["RD_score"]), 1),
        "pe": round(float(e["PE_score"]), 1),
        "ci": round(float(e["CI_score"]), 1),
        "citations": int(e.get("C1_citation_count") or 0),
        "venue": (e.get("C3_venue") or "").strip(),
        "venue_tier": e.get("C3_venue_tier") or "",
        "languages": (e.get("P10_language") or "").strip(),
        "paper_url": paper_url,
        "data_url": data_url,
        "arxiv_id": arxiv_id,
        "passes_gates": bool(e.get("passes_gates")),
        "gate_rd": bool(e.get("gate_RD")),
        "gate_data": bool(e.get("gate_data")),
    }


def load_passers():
    fm = json.loads(FEATURE_MATRIX.read_text())
    passers = [e for e in fm["entries"] if e.get("passes_gates")]
    passers.sort(key=lambda e: -e["COMPOSITE"])
    return [_row_from_entry(e, rank) for rank, e in enumerate(passers, 1)]


def load_all_candidates():
    """All 401 candidates, ranked by composite descending."""
    fm = json.loads(FEATURE_MATRIX.read_text())
    entries = sorted(fm["entries"], key=lambda e: -e["COMPOSITE"])
    return [_row_from_entry(e, rank) for rank, e in enumerate(entries, 1)]


_BADGE_STYLE = (
    'display:inline-block; width:18px; height:18px; line-height:18px; '
    'text-align:center; border-radius:50%; background:#4C78A8; color:#fff; '
    'font-size:0.7rem; margin-right:6px;'
)


def build_nav_link_gp():
    return (
        '    <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" '
        'href="#tab-gatepassers">'
        f'<span class="reading-badge" style="{_BADGE_STYLE}">7</span>'
        'Gate-Passers'
        '<span class="tab-sub">47 papers &middot; scores &amp; links</span>'
        '</a></li>\n'
    )


def build_nav_link_all():
    return (
        '    <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" '
        'href="#tab-all401">'
        f'<span class="reading-badge" style="{_BADGE_STYLE}">8</span>'
        'All Candidates'
        '<span class="tab-sub">401 screened &middot; full corpus</span>'
        '</a></li>\n'
    )


def build_tab_pane_gp():
    return r"""
<div class="tab-pane fade" id="tab-gatepassers">

<h2 class="section-title">The 47 Gate-Passing Benchmarks</h2>

<p style="max-width: 900px; line-height: 1.6; margin-bottom: 14px;">
  Out of 401 candidate religious-values benchmarks identified through database
  search, citation chaining, and expert referral, <strong>47 cleared both hard
  quality gates</strong>: a Religious Discriminability score of 30 or higher
  (out of 100) <em>and</em> a publicly accessible dataset URL.  Composite
  rankings combine three weighted axes &mdash; Religious Depth (40%),
  Practical Ease (35%), and Citation Impact (25%) &mdash; on a 0&ndash;100
  scale.  Each row links out to the original paper (when an open-access URL is
  available) and to the published dataset.
</p>

<div class="finding-callout" style="margin-bottom:18px">
  <strong>Distribution.</strong> Islam dominates the surviving set (28 of 47;
  60%), followed by Christianity and Buddhism (6 each), Hinduism (5), Sikhism
  (2), and Confucianism (1).  Eight traditions <em>(Judaism, Jainism, Taoism,
  Shinto, Ubuntu, Indigenous, Baha&rsquo;i, Zoroastrianism)</em> have zero
  gate-passers &mdash; the structural void documented in the
  <a class="cross-ref" onclick="document.querySelector('[href=\'#tab-void\']').click()">Tradition Void tab</a>.
</div>

<div class="row" style="margin-bottom: 14px;">
  <div class="col-12 col-lg-6">
    <div class="chart-container">
      <h3 class="chart-title">Gate-Passers by Tradition</h3>
      <div id="chart-gatepassers-trad" style="width:100%; height:340px;"></div>
    </div>
  </div>
  <div class="col-12 col-lg-6">
    <div class="chart-container">
      <h3 class="chart-title">Composite Score Distribution</h3>
      <div id="chart-gatepassers-composite" style="width:100%; height:340px;"></div>
    </div>
  </div>
</div>

<div class="chart-container">
  <h3 class="chart-title">Filter &amp; Browse the 47 Gate-Passers</h3>

  <div class="row g-2" style="margin-bottom: 12px;">
    <div class="col-12 col-md-3">
      <label style="font-size:0.75rem; color:var(--text-secondary); display:block; margin-bottom:2px;">Family</label>
      <select id="gp-filter-family" class="form-select form-select-sm" style="background:var(--bg-secondary); color:var(--text-primary); border:1px solid var(--border);">
        <option value="">All families</option>
      </select>
    </div>
    <div class="col-12 col-md-3">
      <label style="font-size:0.75rem; color:var(--text-secondary); display:block; margin-bottom:2px;">Tradition</label>
      <select id="gp-filter-tradition" class="form-select form-select-sm" style="background:var(--bg-secondary); color:var(--text-primary); border:1px solid var(--border);">
        <option value="">All traditions</option>
      </select>
    </div>
    <div class="col-12 col-md-3">
      <label style="font-size:0.75rem; color:var(--text-secondary); display:block; margin-bottom:2px;">Format</label>
      <select id="gp-filter-format" class="form-select form-select-sm" style="background:var(--bg-secondary); color:var(--text-primary); border:1px solid var(--border);">
        <option value="">All formats</option>
      </select>
    </div>
    <div class="col-12 col-md-3">
      <label style="font-size:0.75rem; color:var(--text-secondary); display:block; margin-bottom:2px;">Search title / author</label>
      <input id="gp-filter-search" type="search" class="form-control form-control-sm" placeholder="e.g. Quran, Sikh, Patel" style="background:var(--bg-secondary); color:var(--text-primary); border:1px solid var(--border);">
    </div>
  </div>

  <div style="overflow-x:auto;">
    <table id="gp-table" class="table table-sm" style="color:var(--text-primary); font-size:0.78rem; min-width:1080px;">
      <thead style="position:sticky; top:0; background:var(--bg-card); z-index:1;">
        <tr style="border-bottom:1px solid var(--border);">
          <th data-sort="rank" style="cursor:pointer; white-space:nowrap;">#</th>
          <th data-sort="composite" style="cursor:pointer; white-space:nowrap;">Composite &darr;</th>
          <th data-sort="title" style="cursor:pointer;">Title (1st author, year)</th>
          <th data-sort="tradition" style="cursor:pointer;">Tradition</th>
          <th data-sort="format" style="cursor:pointer;">Format</th>
          <th data-sort="rd" style="cursor:pointer; white-space:nowrap;">RD</th>
          <th data-sort="pe" style="cursor:pointer; white-space:nowrap;">PE</th>
          <th data-sort="ci" style="cursor:pointer; white-space:nowrap;">CI</th>
          <th data-sort="citations" style="cursor:pointer; white-space:nowrap;">Cites</th>
          <th data-sort="languages" style="cursor:pointer;">Lang</th>
          <th>Links</th>
        </tr>
      </thead>
      <tbody id="gp-tbody"></tbody>
    </table>
    <div id="gp-empty" style="display:none; text-align:center; padding:18px; color:var(--text-secondary); font-size:0.85rem;">
      No gate-passers match the current filters.
    </div>
    <div style="margin-top:8px; font-size:0.72rem; color:var(--text-secondary);">
      Showing <span id="gp-count">47</span> of 47 gate-passers.
      Click any column header to sort.
      <strong>RD</strong> = Religious Depth (0&ndash;100),
      <strong>PE</strong> = Practical Ease (0&ndash;100),
      <strong>CI</strong> = Citation Impact (0&ndash;100),
      <strong>Cites</strong> = Semantic Scholar citation count.
    </div>
  </div>
</div>

<div style="margin-top: 20px; padding: 14px 18px; background: var(--bg-secondary); border-left: 3px solid var(--accent-orange); border-radius: 4px;">
  <strong style="color: var(--accent-orange)">Caveat &mdash; Gating is necessary, not sufficient.</strong>
  Passing both gates means a benchmark is <em>scoreable</em> (data is
  retrievable) and <em>religiously discriminable</em> (it is unambiguously
  about religion).  It does <strong>not</strong> mean the benchmark validly
  measures religious values.  See the
  <a class="cross-ref" onclick="document.querySelector('[href=\'#tab-values\']').click()">Values Relevance tab</a>
  for the headline finding (values relevance score 30/100; t = -4.93,
  p &lt; 0.001, d = -1.23) that most benchmarks below this gate do not actually
  test values reasoning even after passing both gates.
</div>

</div>
"""


def build_tab_pane_all():
    return r"""
<div class="tab-pane fade" id="tab-all401">

<h2 class="section-title">The Full Screening Corpus &mdash; All 401 Candidates</h2>

<p style="max-width: 900px; line-height: 1.6; margin-bottom: 14px;">
  This is the complete corpus of 401 candidate religious-values benchmarks
  identified through Semantic Scholar, arXiv, Google Scholar, citation
  chaining, and expert referral.  Each row carries a gate-status badge
  &mdash; <span style="color:var(--accent-green); font-weight:600">PASS</span>
  if it cleared both gates,
  <span style="color:var(--accent-orange); font-weight:600">RD&lt;30</span> if
  Religious Discriminability fell below 30,
  <span style="color:var(--accent-red); font-weight:600">No data</span> if
  no public dataset URL is available, or
  <span style="color:#B279A2; font-weight:600">RD&lt;30 + No data</span> if
  both.  The 47 PASS rows are the same set shown in the
  <a class="cross-ref" onclick="document.querySelector('[href=\'#tab-gatepassers\']').click()">Gate-Passers tab</a>.
</p>

<div class="row" style="margin-bottom: 14px;">
  <div class="col-12 col-md-3">
    <div class="metric-card" style="background:var(--bg-card); padding:14px; border-radius:6px; border:1px solid var(--border);">
      <div style="font-size:1.6rem; font-weight:700;" id="all401-total">401</div>
      <div style="font-size:0.75rem; color:var(--text-secondary);">Total candidates</div>
    </div>
  </div>
  <div class="col-12 col-md-3">
    <div class="metric-card" style="background:var(--bg-card); padding:14px; border-radius:6px; border:1px solid var(--border-color, var(--border)); border-left:3px solid var(--accent-green);">
      <div style="font-size:1.6rem; font-weight:700; color:var(--accent-green);" id="all401-pass">47</div>
      <div style="font-size:0.75rem; color:var(--text-secondary);">Passed both gates</div>
    </div>
  </div>
  <div class="col-12 col-md-3">
    <div class="metric-card" style="background:var(--bg-card); padding:14px; border-radius:6px; border:1px solid var(--border); border-left:3px solid var(--accent-orange);">
      <div style="font-size:1.6rem; font-weight:700; color:var(--accent-orange);" id="all401-rdfail">&mdash;</div>
      <div style="font-size:0.75rem; color:var(--text-secondary);">RD &lt; 30 only</div>
    </div>
  </div>
  <div class="col-12 col-md-3">
    <div class="metric-card" style="background:var(--bg-card); padding:14px; border-radius:6px; border:1px solid var(--border); border-left:3px solid var(--accent-red);">
      <div style="font-size:1.6rem; font-weight:700; color:var(--accent-red);" id="all401-datafail">&mdash;</div>
      <div style="font-size:0.75rem; color:var(--text-secondary);">No public data only</div>
    </div>
  </div>
</div>

<div class="row" style="margin-bottom: 14px;">
  <div class="col-12 col-lg-6">
    <div class="chart-container">
      <h3 class="chart-title">Gate Outcome by Tradition</h3>
      <div id="chart-all401-trad" style="width:100%; height:380px;"></div>
    </div>
  </div>
  <div class="col-12 col-lg-6">
    <div class="chart-container">
      <h3 class="chart-title">Composite Score Distribution (PASS vs FAIL)</h3>
      <div id="chart-all401-composite" style="width:100%; height:380px;"></div>
    </div>
  </div>
</div>

<div class="chart-container">
  <h3 class="chart-title">Filter &amp; Browse All 401 Candidates</h3>

  <div class="row g-2" style="margin-bottom: 12px;">
    <div class="col-12 col-md-3">
      <label style="font-size:0.75rem; color:var(--text-secondary); display:block; margin-bottom:2px;">Gate status</label>
      <select id="all-filter-gate" class="form-select form-select-sm" style="background:var(--bg-secondary); color:var(--text-primary); border:1px solid var(--border);">
        <option value="">All (401)</option>
        <option value="pass">PASS only (47)</option>
        <option value="rd-fail">RD &lt; 30 only</option>
        <option value="data-fail">No data only</option>
        <option value="both-fail">RD &lt; 30 + No data</option>
      </select>
    </div>
    <div class="col-12 col-md-3">
      <label style="font-size:0.75rem; color:var(--text-secondary); display:block; margin-bottom:2px;">Family</label>
      <select id="all-filter-family" class="form-select form-select-sm" style="background:var(--bg-secondary); color:var(--text-primary); border:1px solid var(--border);">
        <option value="">All families</option>
      </select>
    </div>
    <div class="col-12 col-md-3">
      <label style="font-size:0.75rem; color:var(--text-secondary); display:block; margin-bottom:2px;">Tradition</label>
      <select id="all-filter-tradition" class="form-select form-select-sm" style="background:var(--bg-secondary); color:var(--text-primary); border:1px solid var(--border);">
        <option value="">All traditions</option>
      </select>
    </div>
    <div class="col-12 col-md-3">
      <label style="font-size:0.75rem; color:var(--text-secondary); display:block; margin-bottom:2px;">Search title / author</label>
      <input id="all-filter-search" type="search" class="form-control form-control-sm" placeholder="e.g. Quran, Buddhism, Patel" style="background:var(--bg-secondary); color:var(--text-primary); border:1px solid var(--border);">
    </div>
  </div>

  <div style="overflow-x:auto; max-height: 70vh; overflow-y:auto; border:1px solid var(--border); border-radius:4px;">
    <table id="all-table" class="table table-sm" style="color:var(--text-primary); font-size:0.78rem; min-width:1080px; margin-bottom:0;">
      <thead style="position:sticky; top:0; background:var(--bg-card); z-index:1; box-shadow: 0 1px 0 var(--border);">
        <tr>
          <th data-sort="rank" style="cursor:pointer; white-space:nowrap;">#</th>
          <th data-sort="gate" style="cursor:pointer; white-space:nowrap;">Gate</th>
          <th data-sort="composite" style="cursor:pointer; white-space:nowrap;">Composite &darr;</th>
          <th data-sort="title" style="cursor:pointer;">Title (1st author, year)</th>
          <th data-sort="tradition" style="cursor:pointer;">Tradition</th>
          <th data-sort="format" style="cursor:pointer;">Format</th>
          <th data-sort="rd" style="cursor:pointer; white-space:nowrap;">RD</th>
          <th data-sort="pe" style="cursor:pointer; white-space:nowrap;">PE</th>
          <th data-sort="ci" style="cursor:pointer; white-space:nowrap;">CI</th>
          <th data-sort="citations" style="cursor:pointer; white-space:nowrap;">Cites</th>
          <th>Links</th>
        </tr>
      </thead>
      <tbody id="all-tbody"></tbody>
    </table>
    <div id="all-empty" style="display:none; text-align:center; padding:18px; color:var(--text-secondary); font-size:0.85rem;">
      No candidates match the current filters.
    </div>
  </div>
  <div style="margin-top:8px; font-size:0.72rem; color:var(--text-secondary);">
    Showing <span id="all-count">401</span> of 401 candidates.
    Click any column header to sort.  Sticky headers keep gate-status visible while scrolling.
  </div>
</div>

<div style="margin-top: 20px; padding: 14px 18px; background: var(--bg-secondary); border-left: 3px solid var(--accent-blue); border-radius: 4px;">
  <strong style="color: var(--accent-blue)">How candidates were assembled.</strong>
  Database queries on Semantic Scholar (religion + benchmark/dataset/eval keywords),
  arXiv (cs.CL with religious-tradition terms), Google Scholar
  (citation chaining from anchor papers), plus expert referral.  Each was
  scored on the same 6-component Religious Discriminability rubric and the
  same 9-component Practical Ease rubric used for the gate-passers.
  See the <a class="cross-ref" onclick="document.querySelector('[href=\'#tab-overview\']').click()">Overview tab</a>
  for the full pipeline diagram and the
  <a class="cross-ref" onclick="document.querySelector('[href=\'#tab-void\']').click()">Tradition Void tab</a>
  for which traditions are absent at every gate.
</div>

</div>
"""


GATEPASSERS_JS = r"""
// ===== v8: Gate-Passers tab (DOM API; no innerHTML) =====
const GATEPASSERS = __DATA__;

const GP_FAMILY_COLORS = {
    'Abrahamic':  '#4C78A8',
    'Dharmic':    '#F58518',
    'East Asian': '#54A24B',
    'Other':      '#B279A2'
};

function _gpMakeCell(text, opts) {
    var td = document.createElement('td');
    if (opts && opts.style) td.setAttribute('style', opts.style);
    if (text != null) td.textContent = String(text);
    return td;
}

function _gpMakeLink(url, label, color) {
    var a = document.createElement('a');
    a.href = url;
    a.target = '_blank';
    a.rel = 'noopener';
    a.textContent = label;
    a.setAttribute('style',
        'display:inline-block; padding:2px 6px; margin-right:4px; ' +
        'font-size:0.7rem; background:' + color + '; color:#fff; ' +
        'border-radius:3px; text-decoration:none;');
    return a;
}

function _gpClear(node) {
    while (node.firstChild) node.removeChild(node.firstChild);
}

function _gpBuildRow(r) {
    var tr = document.createElement('tr');

    tr.appendChild(_gpMakeCell(r.rank, { style: 'color:var(--text-secondary)' }));

    var compTd = document.createElement('td');
    var strong = document.createElement('strong');
    strong.textContent = r.composite.toFixed(1);
    compTd.appendChild(strong);
    tr.appendChild(compTd);

    // Title cell with sub-line for author/year/venue tier
    var titleTd = document.createElement('td');
    titleTd.setAttribute('style', 'max-width:340px;');
    var titleSpan = document.createElement('span');
    titleSpan.textContent = r.title;
    titleSpan.title = r.title + (r.venue ? '  \u2014  ' + r.venue : '');
    titleTd.appendChild(titleSpan);
    var subDiv = document.createElement('div');
    subDiv.setAttribute('style', 'color:var(--text-secondary); font-size:0.7rem; margin-top:1px;');
    var subParts = [r.first_author];
    if (r.year) subParts.push(r.year);
    if (r.venue_tier) subParts.push(r.venue_tier);
    subDiv.textContent = subParts.join(' \u00b7 ');
    titleTd.appendChild(subDiv);
    tr.appendChild(titleTd);

    // Tradition cell with family-color dot
    var tradTd = document.createElement('td');
    var dot = document.createElement('span');
    var color = GP_FAMILY_COLORS[r.family] || '#8b949e';
    dot.setAttribute('style',
        'display:inline-block; width:8px; height:8px; border-radius:50%; ' +
        'background:' + color + '; margin-right:5px; vertical-align:middle;');
    tradTd.appendChild(dot);
    tradTd.appendChild(document.createTextNode(r.tradition));
    tr.appendChild(tradTd);

    tr.appendChild(_gpMakeCell(r.format));
    tr.appendChild(_gpMakeCell(r.rd.toFixed(1)));
    tr.appendChild(_gpMakeCell(r.pe.toFixed(1)));
    tr.appendChild(_gpMakeCell(r.ci.toFixed(1)));
    tr.appendChild(_gpMakeCell(r.citations));
    tr.appendChild(_gpMakeCell(r.languages, { style: 'font-size:0.7rem;' }));

    var linksTd = document.createElement('td');
    linksTd.setAttribute('style', 'white-space:nowrap;');
    if (r.paper_url) {
        var label = r.arxiv_id ? ('arXiv ' + r.arxiv_id) : 'Paper';
        linksTd.appendChild(_gpMakeLink(r.paper_url, label, '#4C78A8'));
    }
    if (r.data_url) {
        linksTd.appendChild(_gpMakeLink(r.data_url, 'Data', '#54A24B'));
    }
    tr.appendChild(linksTd);

    return tr;
}

var _gpState = { sortKey: 'composite', sortDir: 'desc' };

function _gpFiltered() {
    var f = document.getElementById('gp-filter-family').value;
    var t = document.getElementById('gp-filter-tradition').value;
    var fmt = document.getElementById('gp-filter-format').value;
    var q = document.getElementById('gp-filter-search').value.trim().toLowerCase();
    return GATEPASSERS.filter(function(r) {
        if (f && r.family !== f) return false;
        if (t && r.tradition !== t) return false;
        if (fmt && r.format !== fmt) return false;
        if (q) {
            var hay = (r.title + ' ' + r.first_author + ' ' + r.venue + ' ' + r.languages).toLowerCase();
            if (hay.indexOf(q) === -1) return false;
        }
        return true;
    });
}

function _gpSort(rows) {
    var k = _gpState.sortKey, d = _gpState.sortDir === 'asc' ? 1 : -1;
    return rows.slice().sort(function(a, b) {
        var av = a[k], bv = b[k];
        if (typeof av === 'number' && typeof bv === 'number') return (av - bv) * d;
        return String(av).localeCompare(String(bv)) * d;
    });
}

function _gpRedraw() {
    var rows = _gpSort(_gpFiltered());
    var tbody = document.getElementById('gp-tbody');
    _gpClear(tbody);
    var frag = document.createDocumentFragment();
    rows.forEach(function(r) { frag.appendChild(_gpBuildRow(r)); });
    tbody.appendChild(frag);
    document.getElementById('gp-count').textContent = String(rows.length);
    document.getElementById('gp-empty').style.display = rows.length ? 'none' : '';
}

function _gpFillSelect(id, values) {
    var sel = document.getElementById(id);
    values.forEach(function(v) {
        var o = document.createElement('option');
        o.value = v;
        o.textContent = v;
        sel.appendChild(o);
    });
}

function _gpUnique(key) {
    var s = new Set();
    GATEPASSERS.forEach(function(r) { if (r[key]) s.add(r[key]); });
    return Array.from(s).sort();
}

function renderGatepassers() {
    _gpFillSelect('gp-filter-family',    _gpUnique('family'));
    _gpFillSelect('gp-filter-tradition', _gpUnique('tradition'));
    _gpFillSelect('gp-filter-format',    _gpUnique('format'));

    ['gp-filter-family','gp-filter-tradition','gp-filter-format','gp-filter-search']
      .forEach(function(id) {
          document.getElementById(id).addEventListener('input', _gpRedraw);
      });

    document.querySelectorAll('#gp-table thead th[data-sort]').forEach(function(th) {
        th.addEventListener('click', function() {
            var k = th.getAttribute('data-sort');
            if (_gpState.sortKey === k) {
                _gpState.sortDir = _gpState.sortDir === 'asc' ? 'desc' : 'asc';
            } else {
                _gpState.sortKey = k;
                _gpState.sortDir = (k === 'title' || k === 'tradition' || k === 'format' || k === 'languages') ? 'asc' : 'desc';
            }
            _gpRedraw();
        });
    });

    _gpRedraw();

    // Tradition bar chart (color by family)
    var tradCounts = {};
    var tradFamily = {};
    GATEPASSERS.forEach(function(r) {
        tradCounts[r.tradition] = (tradCounts[r.tradition] || 0) + 1;
        tradFamily[r.tradition] = r.family;
    });
    var tradPairs = Object.keys(tradCounts).map(function(k) {
        return { name: k, value: tradCounts[k], family: tradFamily[k] };
    }).sort(function(a, b) { return b.value - a.value; }).reverse();
    var tradChart = echarts.init(document.getElementById('chart-gatepassers-trad'));
    tradChart.setOption({
        grid: { left: 100, right: 30, top: 20, bottom: 30 },
        tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
        xAxis: { type: 'value', name: 'gate-passers', nameTextStyle: { color: '#c9d1d9' },
                 axisLabel: { color: '#c9d1d9' }, splitLine: { lineStyle: { color: '#30363d' } } },
        yAxis: { type: 'category',
                 data: tradPairs.map(function(p) { return p.name; }),
                 axisLabel: { color: '#c9d1d9' } },
        series: [{
            type: 'bar',
            data: tradPairs.map(function(p) {
                return { value: p.value, itemStyle: { color: GP_FAMILY_COLORS[p.family] || '#4C78A8' } };
            }),
            label: { show: true, position: 'right', color: '#e6edf3' }
        }],
        backgroundColor: 'transparent'
    });

    // Composite histogram (5-pt bins)
    var bins = [];
    for (var lo = 25; lo < 55; lo += 5) {
        var hi = lo + 5;
        var n = GATEPASSERS.filter(function(r) { return r.composite >= lo && r.composite < hi; }).length;
        bins.push({ label: lo + '\u2013' + hi, value: n });
    }
    var compChart = echarts.init(document.getElementById('chart-gatepassers-composite'));
    compChart.setOption({
        grid: { left: 50, right: 30, top: 20, bottom: 50 },
        tooltip: { trigger: 'axis' },
        xAxis: { type: 'category', data: bins.map(function(b) { return b.label; }),
                 name: 'composite score', nameLocation: 'middle', nameGap: 30,
                 nameTextStyle: { color: '#c9d1d9' }, axisLabel: { color: '#c9d1d9' } },
        yAxis: { type: 'value', name: 'gate-passers', nameTextStyle: { color: '#c9d1d9' },
                 axisLabel: { color: '#c9d1d9' }, splitLine: { lineStyle: { color: '#30363d' } } },
        series: [{
            type: 'bar',
            data: bins.map(function(b) { return b.value; }),
            itemStyle: { color: '#4C78A8' },
            label: { show: true, position: 'top', color: '#e6edf3' }
        }],
        backgroundColor: 'transparent'
    });
}
"""


ALL401_JS = r"""
// ===== v8: All 401 Candidates tab (DOM API; no innerHTML) =====
const ALL401 = __DATA__;

const ALL_FAMILY_COLORS = {
    'Abrahamic':  '#4C78A8',
    'Dharmic':    '#F58518',
    'East Asian': '#54A24B',
    'Other':      '#B279A2'
};

function _allGateLabel(r) {
    if (r.passes_gates) return { text: 'PASS',           color: '#54A24B' };
    if (!r.gate_rd && !r.gate_data) return { text: 'RD<30 + No data', color: '#B279A2' };
    if (!r.gate_rd) return { text: 'RD<30',          color: '#F58518' };
    return { text: 'No data',         color: '#E45756' };
}

function _allMakeCell(text, opts) {
    var td = document.createElement('td');
    if (opts && opts.style) td.setAttribute('style', opts.style);
    if (text != null) td.textContent = String(text);
    return td;
}

function _allMakeLink(url, label, color) {
    var a = document.createElement('a');
    a.href = url;
    a.target = '_blank';
    a.rel = 'noopener';
    a.textContent = label;
    a.setAttribute('style',
        'display:inline-block; padding:2px 6px; margin-right:4px; ' +
        'font-size:0.7rem; background:' + color + '; color:#fff; ' +
        'border-radius:3px; text-decoration:none;');
    return a;
}

function _allClear(node) { while (node.firstChild) node.removeChild(node.firstChild); }

function _allBuildRow(r) {
    var tr = document.createElement('tr');

    tr.appendChild(_allMakeCell(r.rank, { style: 'color:var(--text-secondary)' }));

    var gate = _allGateLabel(r);
    var gateTd = document.createElement('td');
    var pill = document.createElement('span');
    pill.textContent = gate.text;
    pill.setAttribute('style',
        'display:inline-block; padding:1px 7px; font-size:0.65rem; '
        + 'border-radius:9px; font-weight:600; '
        + 'background:' + gate.color + '22; color:' + gate.color + '; '
        + 'border:1px solid ' + gate.color + ';');
    gateTd.appendChild(pill);
    tr.appendChild(gateTd);

    var compTd = document.createElement('td');
    compTd.textContent = r.composite.toFixed(1);
    if (r.passes_gates) {
        var b = document.createElement('strong');
        b.textContent = r.composite.toFixed(1);
        compTd.textContent = '';
        compTd.appendChild(b);
    }
    tr.appendChild(compTd);

    var titleTd = document.createElement('td');
    titleTd.setAttribute('style', 'max-width:340px;');
    var titleSpan = document.createElement('span');
    titleSpan.textContent = r.title;
    titleSpan.title = r.title + (r.venue ? '  \u2014  ' + r.venue : '');
    titleTd.appendChild(titleSpan);
    var subDiv = document.createElement('div');
    subDiv.setAttribute('style', 'color:var(--text-secondary); font-size:0.7rem; margin-top:1px;');
    var subParts = [r.first_author];
    if (r.year) subParts.push(r.year);
    if (r.venue_tier) subParts.push(r.venue_tier);
    subDiv.textContent = subParts.filter(Boolean).join(' \u00b7 ');
    titleTd.appendChild(subDiv);
    tr.appendChild(titleTd);

    var tradTd = document.createElement('td');
    var dot = document.createElement('span');
    var color = ALL_FAMILY_COLORS[r.family] || '#8b949e';
    dot.setAttribute('style',
        'display:inline-block; width:8px; height:8px; border-radius:50%; ' +
        'background:' + color + '; margin-right:5px; vertical-align:middle;');
    tradTd.appendChild(dot);
    tradTd.appendChild(document.createTextNode(r.tradition || '\u2014'));
    tr.appendChild(tradTd);

    tr.appendChild(_allMakeCell(r.format || '\u2014'));
    tr.appendChild(_allMakeCell(r.rd.toFixed(1)));
    tr.appendChild(_allMakeCell(r.pe.toFixed(1)));
    tr.appendChild(_allMakeCell(r.ci.toFixed(1)));
    tr.appendChild(_allMakeCell(r.citations));

    var linksTd = document.createElement('td');
    linksTd.setAttribute('style', 'white-space:nowrap;');
    if (r.paper_url) {
        var label = r.arxiv_id ? ('arXiv ' + r.arxiv_id) : 'Paper';
        linksTd.appendChild(_allMakeLink(r.paper_url, label, '#4C78A8'));
    }
    if (r.data_url) {
        linksTd.appendChild(_allMakeLink(r.data_url, 'Data', '#54A24B'));
    }
    tr.appendChild(linksTd);

    return tr;
}

var _allState = { sortKey: 'composite', sortDir: 'desc' };

function _allCategorize(r) {
    if (r.passes_gates) return 'pass';
    if (!r.gate_rd && !r.gate_data) return 'both-fail';
    if (!r.gate_rd) return 'rd-fail';
    return 'data-fail';
}

function _allFiltered() {
    var g = document.getElementById('all-filter-gate').value;
    var f = document.getElementById('all-filter-family').value;
    var t = document.getElementById('all-filter-tradition').value;
    var q = document.getElementById('all-filter-search').value.trim().toLowerCase();
    return ALL401.filter(function(r) {
        if (g && _allCategorize(r) !== g) return false;
        if (f && r.family !== f) return false;
        if (t && r.tradition !== t) return false;
        if (q) {
            var hay = (r.title + ' ' + r.first_author + ' ' + r.venue + ' ' + r.languages).toLowerCase();
            if (hay.indexOf(q) === -1) return false;
        }
        return true;
    });
}

function _allSort(rows) {
    var k = _allState.sortKey, d = _allState.sortDir === 'asc' ? 1 : -1;
    return rows.slice().sort(function(a, b) {
        var av, bv;
        if (k === 'gate') { av = _allCategorize(a); bv = _allCategorize(b); }
        else { av = a[k]; bv = b[k]; }
        if (typeof av === 'number' && typeof bv === 'number') return (av - bv) * d;
        return String(av).localeCompare(String(bv)) * d;
    });
}

function _allRedraw() {
    var rows = _allSort(_allFiltered());
    var tbody = document.getElementById('all-tbody');
    _allClear(tbody);
    var frag = document.createDocumentFragment();
    rows.forEach(function(r) { frag.appendChild(_allBuildRow(r)); });
    tbody.appendChild(frag);
    document.getElementById('all-count').textContent = String(rows.length);
    document.getElementById('all-empty').style.display = rows.length ? 'none' : '';
}

function _allFillSelect(id, values) {
    var sel = document.getElementById(id);
    values.forEach(function(v) {
        var o = document.createElement('option');
        o.value = v; o.textContent = v;
        sel.appendChild(o);
    });
}

function _allUnique(key) {
    var s = new Set();
    ALL401.forEach(function(r) { if (r[key]) s.add(r[key]); });
    return Array.from(s).sort();
}

function renderAll401() {
    // Counter cards
    var nPass = ALL401.filter(function(r) { return r.passes_gates; }).length;
    var nRdOnly = ALL401.filter(function(r) { return !r.passes_gates && !r.gate_rd && r.gate_data; }).length;
    var nDataOnly = ALL401.filter(function(r) { return !r.passes_gates && r.gate_rd && !r.gate_data; }).length;
    document.getElementById('all401-pass').textContent = String(nPass);
    document.getElementById('all401-rdfail').textContent = String(nRdOnly);
    document.getElementById('all401-datafail').textContent = String(nDataOnly);

    _allFillSelect('all-filter-family',    _allUnique('family'));
    _allFillSelect('all-filter-tradition', _allUnique('tradition'));

    ['all-filter-gate','all-filter-family','all-filter-tradition','all-filter-search']
      .forEach(function(id) {
          document.getElementById(id).addEventListener('input', _allRedraw);
      });

    document.querySelectorAll('#all-table thead th[data-sort]').forEach(function(th) {
        th.addEventListener('click', function() {
            var k = th.getAttribute('data-sort');
            if (_allState.sortKey === k) {
                _allState.sortDir = _allState.sortDir === 'asc' ? 'desc' : 'asc';
            } else {
                _allState.sortKey = k;
                _allState.sortDir = (k === 'title' || k === 'tradition' || k === 'format' || k === 'gate') ? 'asc' : 'desc';
            }
            _allRedraw();
        });
    });

    _allRedraw();

    // Stacked bar: gate outcome by tradition (top 10 traditions by count)
    var byTrad = {};
    ALL401.forEach(function(r) {
        var t = r.tradition || '(unspecified)';
        if (!byTrad[t]) byTrad[t] = { pass: 0, rdFail: 0, dataFail: 0, bothFail: 0, family: r.family || 'Other' };
        var cat = _allCategorize(r);
        if (cat === 'pass') byTrad[t].pass++;
        else if (cat === 'rd-fail') byTrad[t].rdFail++;
        else if (cat === 'data-fail') byTrad[t].dataFail++;
        else byTrad[t].bothFail++;
    });
    var tradList = Object.keys(byTrad).map(function(t) {
        return { name: t, total: byTrad[t].pass + byTrad[t].rdFail + byTrad[t].dataFail + byTrad[t].bothFail };
    }).sort(function(a, b) { return b.total - a.total; }).slice(0, 12).map(function(p) { return p.name; });

    var tradChart = echarts.init(document.getElementById('chart-all401-trad'));
    tradChart.setOption({
        grid: { left: 100, right: 30, top: 30, bottom: 40 },
        legend: { data: ['PASS','RD<30','No data','Both fail'], textStyle: { color: '#c9d1d9' }, top: 0 },
        tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
        xAxis: { type: 'value', name: 'candidates', nameTextStyle: { color: '#c9d1d9' },
                 axisLabel: { color: '#c9d1d9' }, splitLine: { lineStyle: { color: '#30363d' } } },
        yAxis: { type: 'category', data: tradList.slice().reverse(), axisLabel: { color: '#c9d1d9' } },
        series: [
            { name: 'PASS',     type: 'bar', stack: 'total', itemStyle: { color: '#54A24B' },
              data: tradList.slice().reverse().map(function(t) { return byTrad[t].pass; }) },
            { name: 'RD<30',    type: 'bar', stack: 'total', itemStyle: { color: '#F58518' },
              data: tradList.slice().reverse().map(function(t) { return byTrad[t].rdFail; }) },
            { name: 'No data',  type: 'bar', stack: 'total', itemStyle: { color: '#E45756' },
              data: tradList.slice().reverse().map(function(t) { return byTrad[t].dataFail; }) },
            { name: 'Both fail',type: 'bar', stack: 'total', itemStyle: { color: '#B279A2' },
              data: tradList.slice().reverse().map(function(t) { return byTrad[t].bothFail; }) }
        ],
        backgroundColor: 'transparent'
    });

    // Composite histogram (all 401, with PASS overlay) -- 5-pt bins from 0 to 60
    var bins = [];
    for (var lo = 0; lo < 60; lo += 5) {
        var hi = lo + 5;
        var allN = ALL401.filter(function(r) { return r.composite >= lo && r.composite < hi; }).length;
        var passN = ALL401.filter(function(r) { return r.composite >= lo && r.composite < hi && r.passes_gates; }).length;
        bins.push({ label: lo + '\u2013' + hi, all: allN, pass: passN, fail: allN - passN });
    }
    var compChart = echarts.init(document.getElementById('chart-all401-composite'));
    compChart.setOption({
        grid: { left: 50, right: 30, top: 30, bottom: 50 },
        legend: { data: ['PASS','FAIL'], textStyle: { color: '#c9d1d9' }, top: 0 },
        tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
        xAxis: { type: 'category', data: bins.map(function(b) { return b.label; }),
                 name: 'composite score', nameLocation: 'middle', nameGap: 30,
                 nameTextStyle: { color: '#c9d1d9' }, axisLabel: { color: '#c9d1d9' } },
        yAxis: { type: 'value', name: 'candidates', nameTextStyle: { color: '#c9d1d9' },
                 axisLabel: { color: '#c9d1d9' }, splitLine: { lineStyle: { color: '#30363d' } } },
        series: [
            { name: 'PASS', type: 'bar', stack: 'tot', itemStyle: { color: '#54A24B' },
              data: bins.map(function(b) { return b.pass; }) },
            { name: 'FAIL', type: 'bar', stack: 'tot', itemStyle: { color: '#8b949e' },
              data: bins.map(function(b) { return b.fail; }) }
        ],
        backgroundColor: 'transparent'
    });
}
"""


def main():
    html = V7_HTML.read_text()
    passers = load_passers()
    candidates = load_all_candidates()
    assert len(passers) == 47, f"expected 47 gate-passers, got {len(passers)}"
    assert len(candidates) == 401, f"expected 401 candidates, got {len(candidates)}"

    # 1. Inject two <li>s in nav-tabs after the crossvendor li
    crossvendor_li_re = re.compile(
        r'(    <li class="nav-item"><a class="nav-link" data-bs-toggle="tab" href="#tab-crossvendor">.*?</li>\n)',
        re.DOTALL,
    )
    new_lis = build_nav_link_gp() + build_nav_link_all()
    html, n = crossvendor_li_re.subn(lambda m: m.group(1) + new_lis, html, count=1)
    assert n == 1, "failed to inject nav-links after #tab-crossvendor"

    # 2. Inject two tab-panes just before </div><!-- /tab-content -->
    tabcontent_close = '</div><!-- /tab-content -->'
    assert html.count(tabcontent_close) == 1, "tab-content closer not unique"
    panes = build_tab_pane_gp() + "\n" + build_tab_pane_all()
    html = html.replace(tabcontent_close, panes + "\n" + tabcontent_close)

    # 3. Inject GATEPASSERS + ALL401 JS data + render fns before "// ===== Initialize ====="
    init_anchor = '// ===== Initialize ====='
    assert html.count(init_anchor) == 1, "init anchor not unique"
    gp_js = GATEPASSERS_JS.replace("__DATA__", json.dumps(passers, ensure_ascii=False))
    all_js = ALL401_JS.replace("__DATA__", json.dumps(candidates, ensure_ascii=False))
    html = html.replace(init_anchor, gp_js + "\n" + all_js + "\n" + init_anchor)

    # 4. Wire renderGatepassers() and renderAll401() into the tab-shown dispatcher.
    dispatch_anchor = "else if (target === 'crossvendor') { renderCrossvendor(); renderVendorTypology(); renderT2Span(); renderRubricCeiling(); }"
    assert html.count(dispatch_anchor) == 1, "dispatch anchor not unique"
    html = html.replace(
        dispatch_anchor,
        dispatch_anchor
        + "\n                else if (target === 'gatepassers') renderGatepassers();"
        + "\n                else if (target === 'all401') renderAll401();",
    )

    # 5. Update version markers v7 -> v8
    html = html.replace(
        '<title>Religious Values Benchmark: Meta-Evaluation Dashboard (v7)</title>',
        '<title>Religious Values Benchmark: Meta-Evaluation Dashboard (v8)</title>',
    )
    html = html.replace(
        'CEI Religious Values Benchmark Meta-Evaluation Dashboard (v7)',
        'CEI Religious Values Benchmark Meta-Evaluation Dashboard (v8)',
    )
    html = html.replace(
        'Dashboard generated 2026-04-13 (v7)',
        'Dashboard generated 2026-04-30 (v8)',
    )

    V8_HTML.write_text(html)
    print(f"WROTE {V8_HTML.relative_to(ROOT.parent)}")
    print(f"  size: {len(html):,} bytes")
    print(f"  gate-passers injected: {len(passers)}")
    print(f"  all candidates injected: {len(candidates)}")


if __name__ == "__main__":
    main()
