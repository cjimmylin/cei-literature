#!/usr/bin/env python3
"""Convert 20260313-eval-already-included-comparison.md to styled HTML (TABLE 1)."""

import re
import json
from pathlib import Path

BASE  = Path(__file__).parent.parent
STATS = BASE / "STATISTICS"
SRC   = STATS / "20260313-eval-already-included-comparison.md"
OUT   = STATS / "20260313-eval-already-included-table.html"


def parse_table(text: str) -> list[dict]:
    rows = []
    in_table = False
    for line in text.splitlines():
        if line.startswith("| Paper | Year |"):
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table and line.startswith("| ") and "|" in line[2:]:
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) < 8:
                continue
            paper, year, ea, lm, ins, helm, le, oa = (cols + [""] * 8)[:8]
            if paper == "Paper":
                continue
            # Count coverage (non-empty, non-dash, non-"—" cells)
            coverage = sum(
                1 for v in [ea, lm, ins, helm]
                if v and v not in ("—", "")
            )
            rows.append({
                "paper": paper,
                "year": year,
                "ea": ea,
                "lm": lm,
                "ins": ins,
                "helm": helm,
                "le": le,
                "oa": oa,
                "coverage": coverage,
            })
        elif in_table and not line.startswith("|"):
            break
    # Sort: coverage DESC, then year DESC, then paper ASC
    rows.sort(key=lambda r: (-r["coverage"], -int(r["year"]) if r["year"].isdigit() else 0, r["paper"]))
    return rows


def fw_chips(val: str, fw: str) -> str:
    """Render task ID(s) as colored chips for a given framework."""
    if not val or val == "—":
        return f'<span class="na">—</span>'
    if val == "✓":
        return f'<span class="chip chip-{fw}">✓</span>'
    # Multiple tasks separated by ", " or ", "
    tasks = [t.strip().strip("`") for t in val.replace("`, `", ",").split(",")]
    return " ".join(f'<span class="chip chip-{fw}">{t}</span>' for t in tasks if t)


def coverage_dots(row: dict) -> str:
    fws = [
        ("ea",   row["ea"]),
        ("lm",   row["lm"]),
        ("ins",  row["ins"]),
        ("helm", row["helm"]),
    ]
    parts = []
    for fw, val in fws:
        active = val and val not in ("—", "")
        cls = f"dot dot-{fw}" if active else "dot dot-off"
        label = fw.upper()
        parts.append(f'<span class="{cls}" title="{label}"></span>')
    return "".join(parts)


def generate_html(rows: list[dict]) -> str:
    total = len(rows)
    multi = sum(1 for r in rows if r["coverage"] >= 2)
    all4  = sum(1 for r in rows if r["coverage"] == 4)
    ea_c  = sum(1 for r in rows if r["ea"] and r["ea"] != "—")
    lm_c  = sum(1 for r in rows if r["lm"] and r["lm"] != "—")
    ins_c = sum(1 for r in rows if r["ins"] and r["ins"] != "—")
    hm_c  = sum(1 for r in rows if r["helm"] and r["helm"] != "—")

    rows_json = json.dumps(rows, ensure_ascii=False)

    table_rows_html = []
    for r in rows:
        cov = r["coverage"]
        cov_cls = "cov4" if cov == 4 else "cov3" if cov == 3 else "cov2" if cov == 2 else "cov1"
        table_rows_html.append(f"""<tr data-cov="{cov}" data-year="{r['year']}" data-paper="{r['paper'].lower()}">
  <td class="paper-col"><span class="paper-key">{r['paper']}</span><span class="yr">{r['year']}</span></td>
  <td class="fw-col">{fw_chips(r['ea'],  'ea')}</td>
  <td class="fw-col">{fw_chips(r['lm'],  'lm')}</td>
  <td class="fw-col">{fw_chips(r['ins'], 'ins')}</td>
  <td class="fw-col">{fw_chips(r['helm'],'helm')}</td>
  <td class="fw-col na-col"><span class="na-tracked">not tracked</span></td>
  <td class="fw-col na-col"><span class="na-tracked">not tracked</span></td>
  <td class="cov-col"><span class="cov-badge {cov_cls}">{cov}/4</span>{coverage_dots(r)}</td>
</tr>""")

    table_body = "\n".join(table_rows_html)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TABLE 1 — Already Included in Eval Frameworks — CEI Vault</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0f0f1a; color: #e0e0e0; font-size: 13px; }}

/* ── Header ── */
header {{ background: #1a1a2e; padding: 14px 20px; border-bottom: 2px solid #3a3a6a; }}
header h1 {{ font-size: 1.1rem; color: #a0b4e0; font-weight: 600; }}
header p  {{ font-size: 0.72rem; color: #5868a0; margin-top: 3px; }}

/* ── Summary cards ── */
.summary {{ background: #141424; padding: 14px 20px; border-bottom: 1px solid #1e1e38; display: flex; flex-wrap: wrap; gap: 12px; align-items: flex-start; }}
.stat-card {{ background: #1a1a2e; border: 1px solid #2a2a4a; border-radius: 5px; padding: 10px 14px; min-width: 110px; }}
.stat-card .val {{ font-size: 1.5rem; font-weight: 700; color: #a0b8e8; line-height: 1; }}
.stat-card .lbl {{ font-size: 0.65rem; color: #4858a0; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 4px; }}

/* framework stat colors */
.stat-card.ea   .val {{ color: #b388ff; }}
.stat-card.lm   .val {{ color: #64b5f6; }}
.stat-card.ins  .val {{ color: #4db6ac; }}
.stat-card.helm .val {{ color: #ffb74d; }}

/* ── Overlap matrix ── */
.overlap {{ background: #141424; padding: 0 20px 14px; border-bottom: 1px solid #1e1e38; }}
.overlap h3 {{ font-size: 0.7rem; color: #4858a0; text-transform: uppercase; letter-spacing: 0.05em; padding: 10px 0 6px; }}
.overlap table {{ border-collapse: collapse; font-size: 0.72rem; }}
.overlap th, .overlap td {{ padding: 5px 12px; border: 1px solid #1e1e38; text-align: center; color: #8090b8; }}
.overlap th {{ background: #1a1a2e; color: #6878a8; font-weight: 600; }}
.overlap td.self {{ color: #2a2a4a; }}
.overlap td.val {{ color: #a0b8e8; font-weight: 600; }}

/* ── Controls ── */
.controls {{ background: #181828; padding: 9px 20px; border-bottom: 1px solid #252540; position: sticky; top: 0; z-index: 100; display: flex; flex-wrap: wrap; gap: 8px 12px; align-items: flex-end; }}
.ctrl-group {{ display: flex; flex-direction: column; gap: 3px; }}
.ctrl-group label {{ font-size: 0.65rem; color: #6878a8; text-transform: uppercase; letter-spacing: 0.04em; }}
.controls input, .controls select {{ background: #242438; border: 1px solid #3a3a5a; color: #d0d8f0; padding: 5px 8px; border-radius: 3px; font-size: 0.75rem; }}
.controls input {{ width: 210px; }}
.controls button {{ background: #2e2e50; border: 1px solid #4a4a7a; color: #a0b0d8; padding: 5px 10px; border-radius: 3px; cursor: pointer; font-size: 0.72rem; align-self: flex-end; }}
.controls button:hover {{ background: #3a3a68; }}

/* ── Stats bar ── */
.stats-bar {{ background: #111120; padding: 6px 20px; font-size: 0.7rem; color: #4858a0; border-bottom: 1px solid #1a1a34; display: flex; flex-wrap: wrap; gap: 0 18px; }}
.stats-bar .val {{ color: #7888c0; font-weight: 600; }}

/* ── Table ── */
.table-wrap {{ overflow: auto; height: calc(100vh - 270px); }}
table.main {{ width: 100%; border-collapse: collapse; }}
table.main thead th {{ background: #1a1a2e; padding: 9px 8px; text-align: left; color: #6878a8; font-size: 0.67rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 2px solid #3a3a6a; position: sticky; top: 0; white-space: nowrap; }}
table.main thead th.fw-h {{ text-align: left; min-width: 90px; }}
table.main thead th.cov-h {{ text-align: center; width: 90px; }}
table.main thead th.na-h {{ color: #2e3858; }}
table.main tbody tr {{ border-bottom: 1px solid #161626; }}
table.main tbody tr:hover {{ background: #1a1a30; }}
table.main td {{ padding: 6px 8px; vertical-align: middle; }}

td.paper-col {{ max-width: 320px; }}
.paper-key {{ color: #b0c4e8; font-size: 0.72rem; line-height: 1.35; word-break: break-word; }}
.yr {{ color: #3a4870; font-size: 0.65rem; margin-left: 5px; }}

td.fw-col {{ vertical-align: middle; }}
td.na-col {{ opacity: 0.3; }}
.na-tracked {{ font-size: 0.62rem; color: #3a4060; font-style: italic; }}

/* ── Chips ── */
.chip {{ display: inline-block; padding: 2px 6px; border-radius: 3px; font-size: 0.62rem; font-weight: 600; font-family: 'SF Mono', 'Fira Code', monospace; margin: 1px 1px 1px 0; white-space: nowrap; }}
.chip-ea   {{ background: #2d1b69; color: #ce93d8; border: 1px solid #4a1e8a; }}
.chip-lm   {{ background: #0d2a4a; color: #90caf9; border: 1px solid #1a4a7a; }}
.chip-ins  {{ background: #0d3a35; color: #80cbc4; border: 1px solid #1a5a52; }}
.chip-helm {{ background: #3e2300; color: #ffcc80; border: 1px solid #6a3a00; }}
.na {{ font-size: 0.65rem; color: #1e2445; }}

/* ── Coverage column ── */
td.cov-col {{ text-align: center; white-space: nowrap; }}
.cov-badge {{ display: inline-block; padding: 2px 5px; border-radius: 3px; font-size: 0.65rem; font-weight: 700; margin-right: 5px; }}
.cov4 {{ background: #1b5e20; color: #a5d6a7; }}
.cov3 {{ background: #1a3a6a; color: #90caf9; }}
.cov2 {{ background: #2a2a50; color: #9090d8; }}
.cov1 {{ background: #1e1e32; color: #5060a0; }}

/* ── Coverage dots ── */
.dot {{ display: inline-block; width: 7px; height: 7px; border-radius: 50%; margin: 0 1px; vertical-align: middle; }}
.dot-ea   {{ background: #b388ff; }}
.dot-lm   {{ background: #64b5f6; }}
.dot-ins  {{ background: #4db6ac; }}
.dot-helm {{ background: #ffb74d; }}
.dot-off  {{ background: #1e1e30; border: 1px solid #2a2a44; }}

/* ── Framework legend in header ── */
.fw-legend {{ display: flex; gap: 12px; flex-wrap: wrap; margin-top: 8px; }}
.fw-legend span {{ font-size: 0.68rem; display: flex; align-items: center; gap: 5px; }}
.fw-legend .dot {{ width: 9px; height: 9px; }}

/* ── Footer ── */
.footer {{ padding: 10px 20px; color: #2e3858; font-size: 0.67rem; border-top: 1px solid #1a1a34; line-height: 1.7; }}

/* ── Hidden rows ── */
tr.hidden {{ display: none; }}
</style>
</head>
<body>

<header>
  <h1>TABLE 1 — Eval Framework Coverage: Already Included</h1>
  <p>CEI Literature Vault &nbsp;·&nbsp; {total} papers already implemented in ≥1 framework &nbsp;·&nbsp; Generated 2026-03-13</p>
  <div class="fw-legend">
    <span><span class="dot dot-ea"></span>EleutherAI (22)</span>
    <span><span class="dot dot-lm"></span>lm-eval (63)</span>
    <span><span class="dot dot-ins"></span>Inspect (37)</span>
    <span><span class="dot dot-helm"></span>HELM (19)</span>
  </div>
</header>

<div class="summary">
  <div class="stat-card">
    <div class="val">{total}</div>
    <div class="lbl">Total papers</div>
  </div>
  <div class="stat-card">
    <div class="val">{multi}</div>
    <div class="lbl">In 2+ frameworks</div>
  </div>
  <div class="stat-card">
    <div class="val">{all4}</div>
    <div class="lbl">In all 4</div>
  </div>
  <div class="stat-card ea">
    <div class="val">{ea_c}</div>
    <div class="lbl">EleutherAI</div>
  </div>
  <div class="stat-card lm">
    <div class="val">{lm_c}</div>
    <div class="lbl">lm-eval</div>
  </div>
  <div class="stat-card ins">
    <div class="val">{ins_c}</div>
    <div class="lbl">Inspect</div>
  </div>
  <div class="stat-card helm">
    <div class="val">{hm_c}</div>
    <div class="lbl">HELM</div>
  </div>
</div>

<div class="overlap">
  <h3>Pairwise Overlap</h3>
  <table>
    <thead><tr><th></th><th>EleutherAI (22)</th><th>lm-eval (63)</th><th>Inspect (37)</th><th>HELM (19)</th></tr></thead>
    <tbody>
      <tr><th>EleutherAI</th><td class="self">—</td><td class="val">9</td><td class="val">6</td><td class="val">4</td></tr>
      <tr><th>lm-eval</th><td class="val">9</td><td class="self">—</td><td class="val">15</td><td class="val">6</td></tr>
      <tr><th>Inspect</th><td class="val">6</td><td class="val">15</td><td class="self">—</td><td class="val">4</td></tr>
      <tr><th>HELM</th><td class="val">4</td><td class="val">6</td><td class="val">4</td><td class="self">—</td></tr>
    </tbody>
  </table>
</div>

<div class="controls">
  <div class="ctrl-group">
    <label>Search paper</label>
    <input type="text" id="search" placeholder="Filter by title…">
  </div>
  <div class="ctrl-group">
    <label>Min frameworks</label>
    <select id="minCov">
      <option value="0">Any</option>
      <option value="1">1+</option>
      <option value="2">2+</option>
      <option value="3">3+</option>
      <option value="4">All 4</option>
    </select>
  </div>
  <div class="ctrl-group">
    <label>Year</label>
    <select id="yearFilter">
      <option value="">Any</option>
      <option value="2016">2016</option>
      <option value="2018">2018</option>
      <option value="2019">2019</option>
      <option value="2020">2020</option>
      <option value="2021">2021</option>
      <option value="2022">2022</option>
      <option value="2023">2023</option>
      <option value="2024">2024</option>
      <option value="2025">2025</option>
      <option value="2026">2026</option>
    </select>
  </div>
  <div class="ctrl-group">
    <label>Framework presence</label>
    <select id="fwFilter">
      <option value="">Any</option>
      <option value="ea">EleutherAI</option>
      <option value="lm">lm-eval</option>
      <option value="ins">Inspect</option>
      <option value="helm">HELM</option>
    </select>
  </div>
  <button onclick="resetFilters()">Reset</button>
</div>

<div class="stats-bar">
  <span>Showing <span class="val" id="showCount">{total}</span> of {total}</span>
  <span>lm-eval ∩ Inspect: <span class="val">15</span></span>
  <span>EleutherAI ∩ lm-eval: <span class="val">9</span></span>
</div>

<div class="table-wrap">
<table class="main" id="mainTable">
<thead>
<tr>
  <th style="min-width:280px">Paper</th>
  <th class="fw-h">EleutherAI</th>
  <th class="fw-h">lm-eval</th>
  <th class="fw-h">Inspect</th>
  <th class="fw-h">HELM</th>
  <th class="fw-h na-h">lighteval</th>
  <th class="fw-h na-h">OpenAI Evals</th>
  <th class="cov-h">Coverage</th>
</tr>
</thead>
<tbody id="tableBody">
{table_body}
</tbody>
</table>
</div>

<div class="footer">
  <strong>Notes:</strong>
  Cells show the framework's internal task/benchmark ID for papers it already implements.
  ✓ = paper is tagged as incorporated but has no single mapped task ID.
  lighteval and OpenAI Evals track implementability only — no "already included" data.
  Coverage dots: <span class="dot dot-ea"></span> EA &nbsp; <span class="dot dot-lm"></span> lm-eval &nbsp; <span class="dot dot-ins"></span> Inspect &nbsp; <span class="dot dot-helm"></span> HELM &nbsp; <span class="dot dot-off"></span> absent.
  <br>
  <em>Sources: 20260312-eleutherai-eval-harness-integration.md, 20260312-helm-values-alignment-integration-report.md, 20260312-lm-eval-implementability-report.md, 20260312-inspect-eval-implementability-report.md</em>
</div>

<script>
const rows = Array.from(document.querySelectorAll("#tableBody tr"));

function applyFilters() {{
  const search  = document.getElementById("search").value.toLowerCase();
  const minCov  = parseInt(document.getElementById("minCov").value) || 0;
  const year    = document.getElementById("yearFilter").value;
  const fw      = document.getElementById("fwFilter").value;

  // fw presence check — need access to row data
  const DATA = {rows_json};
  const dataMap = {{}};
  DATA.forEach(function(d) {{ dataMap[d.paper.toLowerCase()] = d; }});

  let count = 0;
  rows.forEach(function(tr) {{
    const paper = tr.dataset.paper;
    const cov   = parseInt(tr.dataset.cov);
    const y     = tr.dataset.year;
    const d     = dataMap[paper];

    let show = true;
    if (search && paper.indexOf(search) === -1) show = false;
    if (cov < minCov) show = false;
    if (year && y !== year) show = false;
    if (fw && d) {{
      const val = d[fw];
      if (!val || val === "—" || val === "") show = false;
    }}

    if (show) {{ tr.classList.remove("hidden"); count++; }}
    else       {{ tr.classList.add("hidden"); }}
  }});
  document.getElementById("showCount").textContent = count;
}}

function resetFilters() {{
  document.getElementById("search").value = "";
  document.getElementById("minCov").value = "0";
  document.getElementById("yearFilter").value = "";
  document.getElementById("fwFilter").value = "";
  applyFilters();
}}

document.getElementById("search").addEventListener("input", applyFilters);
["minCov","yearFilter","fwFilter"].forEach(function(id) {{
  document.getElementById(id).addEventListener("change", applyFilters);
}});
</script>
</body>
</html>"""


def main():
    text = SRC.read_text(encoding="utf-8")
    rows = parse_table(text)
    print(f"Parsed {len(rows)} rows")
    html = generate_html(rows)
    OUT.write_text(html, encoding="utf-8")
    print(f"Generated {OUT}")


if __name__ == "__main__":
    main()
