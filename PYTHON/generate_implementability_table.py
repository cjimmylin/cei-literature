#!/usr/bin/env python3
"""Generate cross-framework implementability comparison table (TABLE 2)."""

import re
import json
import csv
import sys
from pathlib import Path

# === Paths ===
BASE = Path(__file__).parent.parent  # CEI-Lit-WS/
STATS = BASE / "STATISTICS"
PAPERS_DIR = BASE / "papers"
OUT_HTML = STATS / "20260313-implementability-cross-framework-table.html"
OUT_CSV = STATS / "20260313-implementability-cross-framework-table.csv"

# === Tier codes ===
IMPLEMENTED = "IMPLEMENTED"
READY = "READY"
POSSIBLE = "POSSIBLE"
BARRIERS = "BARRIERS"
NOT_FEASIBLE = "NOT_FEASIBLE"
NA = "N_A"

TIER_ORDER = {IMPLEMENTED: 5, READY: 4, POSSIBLE: 3, BARRIERS: 2, NOT_FEASIBLE: 1, NA: 0}
TIER_DISPLAY = {
    IMPLEMENTED: "In",
    READY: "Ready",
    POSSIBLE: "Possible",
    BARRIERS: "Barriers",
    NOT_FEASIBLE: "✗",
    NA: "—",
}

LIGHTEVAL_TIER_MAP = {
    "Ready": READY,
    "Possible": POSSIBLE,
    "Barriers": BARRIERS,
    "Not Implementable": NOT_FEASIBLE,
}


# === Key normalization ===
def normalize_key(s: str) -> str:
    return s.strip().strip("`").removesuffix(".md").strip()


def get_year(key: str) -> str:
    m = re.match(r"^(\d{4})", key)
    return m.group(1) if m else "0000"


# === Master paper list ===
def load_master_papers() -> dict:
    papers = {}
    for p in PAPERS_DIR.iterdir():
        if p.suffix == ".md":
            key = p.stem
            papers[key] = get_year(key)
    return papers


# === Fuzzy match on YYYY-Author- prefix ===
def fuzzy_match(key: str, master: dict):
    parts = key.split("-")
    if len(parts) >= 2:
        prefix = parts[0] + "-" + parts[1] + "-"
        candidates = [k for k in master if k.startswith(prefix)]
        if len(candidates) == 1:
            return candidates[0]
    return None


def resolve_key(raw: str, master: dict):
    key = normalize_key(raw)
    if key in master:
        return key
    matched = fuzzy_match(key, master)
    if matched:
        return matched
    print(f"  UNMATCHED: {repr(key)}", file=sys.stderr)
    return None


# === Parser 1: lm-eval (merges eleutherai) ===
def parse_lm_eval(master: dict) -> dict:
    results = {}

    # --- Eleutherai report: 22 IMPLEMENTED papers ---
    ea_path = STATS / "20260312-eleutherai-eval-harness-integration.md"
    ea_text = ea_path.read_text(encoding="utf-8")
    for m in re.finditer(r"^\| \d+ \| (.+?) \|", ea_text, re.MULTILINE):
        raw = m.group(1).strip()
        if not re.match(r"\d{4}-", raw):
            continue
        key = resolve_key(raw, master)
        if key:
            results[key] = (IMPLEMENTED, None)

    # --- lm-eval main report ---
    lm_path = STATS / "20260312-lm-eval-implementability-report.md"
    lm_text = lm_path.read_text(encoding="utf-8")

    # Section 1: Already in Harness — format: | PaperKey | YYYY | task | ...
    sec1 = re.search(r"## 1\. Already.*?\n(.*?)(?=## 2\.)", lm_text, re.DOTALL)
    if sec1:
        for m in re.finditer(r"^\| (.+?) \| \d{4} \|", sec1.group(1), re.MULTILINE):
            raw = m.group(1).strip()
            if raw == "Paper":
                continue
            key = resolve_key(raw, master)
            if key:
                results[key] = (IMPLEMENTED, None)

    # Section 2: Ready (score >= 65) — format: | # | PaperKey | Score | ...
    sec2 = re.search(r"## 2\. Ready.*?\n(.*?)(?=## 3\.)", lm_text, re.DOTALL)
    if sec2:
        for m in re.finditer(r"^\| \d+ \| (.+?) \| (\d+) \|", sec2.group(1), re.MULTILINE):
            raw, score = m.group(1).strip(), int(m.group(2))
            key = resolve_key(raw, master)
            if key and key not in results:
                results[key] = (READY, score)

    # Section 3: Needs Dataset Hosting → POSSIBLE
    sec3 = re.search(r"## 3\. Needs Dataset.*?\n(.*?)(?=## 4\.)", lm_text, re.DOTALL)
    if sec3:
        for m in re.finditer(r"^\| \d+ \| (.+?) \| (\d+) \|", sec3.group(1), re.MULTILINE):
            raw, score = m.group(1).strip(), int(m.group(2))
            key = resolve_key(raw, master)
            if key and key not in results:
                results[key] = (POSSIBLE, score)

    # Section 4: Needs More Info → BARRIERS
    sec4 = re.search(r"## 4\. Needs More Info.*?\n(.*?)(?=## 5\.)", lm_text, re.DOTALL)
    if sec4:
        for m in re.finditer(r"^\| \d+ \| (.+?) \| (\d+) \|", sec4.group(1), re.MULTILINE):
            raw, score = m.group(1).strip(), int(m.group(2))
            key = resolve_key(raw, master)
            if key and key not in results:
                results[key] = (BARRIERS, score)

    # Residual → NOT_FEASIBLE
    for key in master:
        if key not in results:
            results[key] = (NOT_FEASIBLE, None)

    return results


# === Parser 2: Inspect ===
def parse_inspect(master: dict) -> dict:
    results = {}
    path = STATS / "20260312-inspect-eval-implementability-report.md"
    text = path.read_text(encoding="utf-8")

    # Section 1: Already in Inspect — format: | Paper.md | eval | cat | scorer |
    sec1 = re.search(r"## 1\. Already.*?\n(.*?)(?=## 2\.)", text, re.DOTALL)
    if sec1:
        for m in re.finditer(r"^\| (.+?\.md) \|", sec1.group(1), re.MULTILINE):
            raw = m.group(1).strip()
            if raw == "Paper":
                continue
            key = resolve_key(raw, master)
            if key:
                results[key] = (IMPLEMENTED, None)

    # Section 2: Ready — format: | Paper.md | Benchmark | Score | Pattern | URL | Signals |
    sec2 = re.search(r"## 2\. Ready.*?\n(.*?)(?=## 3\.)", text, re.DOTALL)
    if sec2:
        for m in re.finditer(r"^\| (.+?\.md) \| [^|]+ \| (\d+) \|", sec2.group(1), re.MULTILINE):
            raw, score = m.group(1).strip(), int(m.group(2))
            if raw == "Paper":
                continue
            key = resolve_key(raw, master)
            if key and key not in results:
                results[key] = (READY, score)

    # Section 3: Model-Graded Candidates → POSSIBLE
    sec3 = re.search(r"## 3\. Model-Graded.*?\n(.*?)(?=## 4\.)", text, re.DOTALL)
    if sec3:
        for m in re.finditer(r"^\| (.+?\.md) \| [^|]+ \| (\d+) \|", sec3.group(1), re.MULTILINE):
            raw, score = m.group(1).strip(), int(m.group(2))
            if raw == "Paper":
                continue
            key = resolve_key(raw, master)
            if key and key not in results:
                results[key] = (POSSIBLE, score)

    # Section 5: Needs Dataset Work (30 listed) → BARRIERS
    sec5 = re.search(r"## 5\. Needs Dataset Work.*?\n(.*?)(?=## 6\.)", text, re.DOTALL)
    if sec5:
        for m in re.finditer(r"^\| (.+?\.md) \| (\d+) \|", sec5.group(1), re.MULTILINE):
            raw, score = m.group(1).strip(), int(m.group(2))
            if raw == "Paper":
                continue
            key = resolve_key(raw, master)
            if key and key not in results:
                results[key] = (BARRIERS, score)

    # All others → N_A
    for key in master:
        if key not in results:
            results[key] = (NA, None)

    return results


# === Parser 3: LightEval ===
def parse_lighteval(master: dict) -> dict:
    results = {}
    path = STATS / "20260312-lighteval-paper-reports.md"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Phase A: detailed reports (score >= 5.0)
    # Pattern: ### YYYY-Author-Title\n\n**Score: X.X/10.0** | Tier: **TierName**
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("### ") and re.match(r"### \d{4}-", line):
            raw = line[4:].strip()
            for j in range(i + 1, min(i + 6, len(lines))):
                sm = re.search(
                    r"\*\*Score:\s*([\d.]+)/10\.0\*\*\s*\|\s*Tier:\s*\*\*([\w ]+)\*\*",
                    lines[j],
                )
                if sm:
                    score_val = float(sm.group(1))
                    tier = LIGHTEVAL_TIER_MAP.get(sm.group(2).strip(), NA)
                    key = resolve_key(raw, master)
                    if key and key not in results:
                        results[key] = (tier, score_val)
                    break
        i += 1

    # Phase B: appendix table (score < 5.0)
    # Format: | Paper | Score | Tier | Task Type | Notes |
    app = re.search(r"## Appendix: Below Threshold\n(.*?)$", text, re.DOTALL)
    if app:
        for m in re.finditer(
            r"^\| (.+?) \| ([\d.]+) \| ([\w][\w ]+?) \|",
            app.group(1),
            re.MULTILINE,
        ):
            raw, score_str, tier_name = m.group(1).strip(), m.group(2), m.group(3).strip()
            if raw in ("Paper", "#"):
                continue
            tier = LIGHTEVAL_TIER_MAP.get(tier_name, NA)
            key = resolve_key(raw, master)
            if key and key not in results:
                results[key] = (tier, float(score_str))

    # All others → N_A
    for key in master:
        if key not in results:
            results[key] = (NA, None)

    return results


# === Parser 4: HELM ===
def parse_helm(master: dict) -> dict:
    results = {}
    path = STATS / "20260312-helm-values-alignment-integration-report.md"
    text = path.read_text(encoding="utf-8")

    # Find all paper file references: `2022-Liang-....md` or `papers/2022-Liang-....md`
    for m in re.finditer(r"`(?:papers/)?(\d{4}-[^`]+\.md)`", text):
        raw = m.group(1)
        key = resolve_key(raw, master)
        if key:
            results[key] = (IMPLEMENTED, None)

    # All others → N_A
    for key in master:
        if key not in results:
            results[key] = (NA, None)

    return results


# === Parser 5: OpenAI Evals ===
def parse_openai(master: dict) -> dict:
    results = {}
    path = STATS / "20260312-openai-evals-paper-reports.md"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Phase A: detailed reports (score >= 5.0) — same structure as lighteval
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("### ") and re.match(r"### \d{4}-", line):
            raw = line[4:].strip()
            for j in range(i + 1, min(i + 6, len(lines))):
                sm = re.search(
                    r"\*\*Score:\s*([\d.]+)/10\.0\*\*\s*\|\s*Tier:\s*\*\*([\w ]+)\*\*",
                    lines[j],
                )
                if sm:
                    score_val = float(sm.group(1))
                    tier = LIGHTEVAL_TIER_MAP.get(sm.group(2).strip(), NA)
                    key = resolve_key(raw, master)
                    if key and key not in results:
                        results[key] = (tier, score_val)
                    break
        i += 1

    # Phase B: appendix (score < 5.0)
    # Format: | Paper | Score | Tier | Template | Status |
    app = re.search(r"## Appendix:.*?\n(.*?)$", text, re.DOTALL)
    if app:
        for m in re.finditer(
            r"^\| (.+?) \| ([\d.]+) \| ([\w][\w ]+?) \|",
            app.group(1),
            re.MULTILINE,
        ):
            raw, score_str, tier_name = m.group(1).strip(), m.group(2), m.group(3).strip()
            if raw in ("Paper", "#"):
                continue
            tier = LIGHTEVAL_TIER_MAP.get(tier_name, NA)
            key = resolve_key(raw, master)
            if key and key not in results:
                results[key] = (tier, float(score_str))

    # All others → N_A
    for key in master:
        if key not in results:
            results[key] = (NA, None)

    return results


# === Build rows ===
def build_rows(master, lm, inspect, lighteval, helm, openai) -> list:
    rows = []
    for key, year in master.items():
        lm_tier, lm_score = lm.get(key, (NA, None))
        ins_tier, ins_score = inspect.get(key, (NA, None))
        le_tier, le_score = lighteval.get(key, (NA, None))
        helm_tier, _ = helm.get(key, (NA, None))
        oa_tier, oa_score = openai.get(key, (NA, None))

        tiers = [lm_tier, ins_tier, le_tier, helm_tier, oa_tier]
        tier_vals = [TIER_ORDER[t] for t in tiers]

        best_val = max(tier_vals)
        best_tier = next(t for t in tiers if TIER_ORDER[t] == best_val)
        n_ready = sum(1 for t in tiers if TIER_ORDER[t] >= TIER_ORDER[READY])
        sort_score = sum(tier_vals) / len(tier_vals)

        rows.append(
            {
                "paper_key": key,
                "year": year,
                "lm_eval_tier": lm_tier,
                "lm_eval_score": lm_score,
                "inspect_tier": ins_tier,
                "inspect_score": ins_score,
                "lighteval_tier": le_tier,
                "lighteval_score": le_score,
                "helm_tier": helm_tier,
                "openai_tier": oa_tier,
                "openai_score": oa_score,
                "best_tier": best_tier,
                "n_ready_or_better": n_ready,
                "sort_score": sort_score,
            }
        )

    rows.sort(key=lambda r: (-r["n_ready_or_better"], -r["sort_score"]))
    return rows


# === Generate CSV ===
def generate_csv(rows):
    fields = [
        "paper_key", "year",
        "lm_eval_tier", "lm_eval_score",
        "inspect_tier", "inspect_score",
        "lighteval_tier", "lighteval_score",
        "helm_tier",
        "openai_tier", "openai_score",
        "best_tier", "n_ready_or_better", "sort_score",
    ]
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"Generated {OUT_CSV}")


# === Generate HTML ===
def generate_html(rows):
    total = len(rows)
    lm_ready = sum(1 for r in rows if TIER_ORDER[r["lm_eval_tier"]] >= TIER_ORDER[READY])
    ins_ready = sum(1 for r in rows if TIER_ORDER[r["inspect_tier"]] >= TIER_ORDER[READY])
    le_ready = sum(1 for r in rows if TIER_ORDER[r["lighteval_tier"]] >= TIER_ORDER[READY])
    helm_impl = sum(1 for r in rows if r["helm_tier"] == IMPLEMENTED)
    oa_ready = sum(1 for r in rows if TIER_ORDER[r["openai_tier"]] >= TIER_ORDER[READY])

    # Build compact JSON rows
    json_rows = []
    for r in rows:
        json_rows.append({
            "k": r["paper_key"],
            "y": r["year"],
            "lm": r["lm_eval_tier"],
            "ls": r["lm_eval_score"],
            "ins": r["inspect_tier"],
            "isc": r["inspect_score"],
            "le": r["lighteval_tier"],
            "les": r["lighteval_score"],
            "hm": r["helm_tier"],
            "oa": r["openai_tier"],
            "oas": r["openai_score"],
            "bt": r["best_tier"],
            "nr": r["n_ready_or_better"],
        })

    data_json = json.dumps(json_rows, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cross-Framework Implementability — CEI Vault</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0f0f1a; color: #e0e0e0; font-size: 13px; }}
header {{ background: #1a1a2e; padding: 14px 20px; border-bottom: 2px solid #3a3a6a; display: flex; justify-content: space-between; align-items: center; }}
header h1 {{ font-size: 1.1rem; color: #a0b4e0; font-weight: 600; }}
header p {{ font-size: 0.72rem; color: #5868a0; }}
.controls {{ background: #181828; padding: 10px 20px; border-bottom: 1px solid #252540; position: sticky; top: 0; z-index: 100; display: flex; flex-wrap: wrap; gap: 8px 12px; align-items: flex-end; }}
.ctrl-group {{ display: flex; flex-direction: column; gap: 3px; }}
.ctrl-group label {{ font-size: 0.65rem; color: #6878a8; text-transform: uppercase; letter-spacing: 0.04em; }}
.controls input, .controls select {{ background: #242438; border: 1px solid #3a3a5a; color: #d0d8f0; padding: 5px 8px; border-radius: 3px; font-size: 0.75rem; }}
.controls input {{ width: 200px; }}
.controls button {{ background: #2e2e50; border: 1px solid #4a4a7a; color: #a0b0d8; padding: 5px 10px; border-radius: 3px; cursor: pointer; font-size: 0.72rem; align-self: flex-end; }}
.controls button:hover {{ background: #3a3a68; }}
.stats-bar {{ background: #111120; padding: 7px 20px; font-size: 0.7rem; color: #5060a0; border-bottom: 1px solid #1e1e38; display: flex; flex-wrap: wrap; gap: 0 20px; }}
.stats-bar .val {{ color: #8090c8; font-weight: 600; }}
.table-wrap {{ overflow: auto; height: calc(100vh - 145px); }}
table {{ width: 100%; border-collapse: collapse; }}
thead th {{ background: #1a1a2e; padding: 9px 8px; text-align: left; color: #8090b8; font-size: 0.7rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 2px solid #3a3a6a; position: sticky; top: 0; white-space: nowrap; }}
thead th.fw {{ text-align: center; min-width: 76px; }}
tbody tr {{ border-bottom: 1px solid #161626; transition: background 0.1s; }}
tbody tr:hover {{ background: #1a1a30; }}
td {{ padding: 6px 8px; vertical-align: middle; }}
td.paper {{ max-width: 340px; }}
td.paper .key {{ color: #b0c4e8; font-size: 0.72rem; line-height: 1.3; word-break: break-word; }}
td.paper .yr {{ color: #4858a0; font-size: 0.65rem; margin-left: 5px; }}
td.cell {{ text-align: center; }}
.badge {{ display: inline-block; padding: 2px 6px; border-radius: 2px; font-size: 0.63rem; font-weight: 700; color: #fff; cursor: default; white-space: nowrap; }}
.badge.IMPLEMENTED {{ background: #1565c0; }}
.badge.READY {{ background: #2e7d32; }}
.badge.POSSIBLE {{ background: #f57f17; color: #1a0f00; }}
.badge.BARRIERS {{ background: #bf360c; }}
.badge.NOT_FEASIBLE {{ background: #7f0000; }}
.badge.N_A {{ background: #1e1e2e; color: #3a4060; border: 1px solid #252545; }}
.badge.best-badge {{ outline: 2px solid rgba(255,255,255,0.2); outline-offset: 1px; }}
.footer {{ padding: 12px 20px; color: #3a4870; font-size: 0.68rem; border-top: 1px solid #1e1e38; line-height: 1.7; }}
</style>
</head>
<body>
<header>
  <div>
    <h1>TABLE 2 — Cross-Framework Implementability Comparison</h1>
    <p>CEI Literature Vault &nbsp;·&nbsp; {total} papers &times; 5 frameworks &nbsp;·&nbsp; Generated 2026-03-13</p>
  </div>
</header>

<div class="controls">
  <div class="ctrl-group">
    <label>Search paper title</label>
    <input type="text" id="search" placeholder="Type to filter…">
  </div>
  <div class="ctrl-group">
    <label>Min Ready+ frameworks</label>
    <select id="minReady">
      <option value="0">Any</option>
      <option value="1">1+</option>
      <option value="2">2+</option>
      <option value="3">3+</option>
      <option value="4">4+</option>
    </select>
  </div>
  <div class="ctrl-group">
    <label>lm-eval</label>
    <select id="f_lm">
      <option value="">Any</option>
      <option value="rp">≥ Ready</option>
      <option value="pp">≥ Possible</option>
      <option value="bw">Barriers or worse</option>
    </select>
  </div>
  <div class="ctrl-group">
    <label>Inspect</label>
    <select id="f_ins">
      <option value="">Any</option>
      <option value="rp">≥ Ready</option>
      <option value="pp">≥ Possible</option>
      <option value="bw">Barriers or worse</option>
    </select>
  </div>
  <div class="ctrl-group">
    <label>LightEval</label>
    <select id="f_le">
      <option value="">Any</option>
      <option value="rp">≥ Ready</option>
      <option value="pp">≥ Possible</option>
      <option value="bw">Barriers or worse</option>
    </select>
  </div>
  <div class="ctrl-group">
    <label>HELM</label>
    <select id="f_hm">
      <option value="">Any</option>
      <option value="rp">In Framework only</option>
      <option value="na">N/A only</option>
    </select>
  </div>
  <div class="ctrl-group">
    <label>OpenAI Evals</label>
    <select id="f_oa">
      <option value="">Any</option>
      <option value="rp">≥ Ready</option>
      <option value="pp">≥ Possible</option>
      <option value="bw">Barriers or worse</option>
    </select>
  </div>
  <button onclick="resetFilters()">Reset</button>
</div>

<div class="stats-bar">
  <span>Showing <span class="val" id="showCount">{total}</span> of {total}</span>
  <span>lm-eval Ready+: <span class="val">{lm_ready}</span></span>
  <span>Inspect Ready+: <span class="val">{ins_ready}</span></span>
  <span>LightEval Ready+: <span class="val">{le_ready}</span></span>
  <span>HELM In: <span class="val">{helm_impl}</span></span>
  <span>OpenAI Ready+: <span class="val">{oa_ready}</span></span>
</div>

<div class="table-wrap">
<table id="mainTable">
<thead>
<tr>
  <th style="min-width:280px">Paper</th>
  <th class="fw">lm-eval</th>
  <th class="fw">Inspect</th>
  <th class="fw">LightEval</th>
  <th class="fw">HELM</th>
  <th class="fw">OpenAI</th>
  <th class="fw">Best</th>
</tr>
</thead>
<tbody id="tableBody"></tbody>
</table>
</div>

<div class="footer">
  <strong>Color key:</strong>
  <span class="badge IMPLEMENTED">In Framework</span>&nbsp;
  <span class="badge READY">Ready</span>&nbsp;
  <span class="badge POSSIBLE">Possible</span>&nbsp;
  <span class="badge BARRIERS">Barriers</span>&nbsp;
  <span class="badge NOT_FEASIBLE">✗ Not Feasible</span>&nbsp;
  <span class="badge N_A">— N/A</span>
  <br>
  <strong>Notes:</strong>
  (1)&nbsp;Inspect: ~1,440 papers in bottom tiers not individually resolvable from report — shown as N/A.
  (2)&nbsp;HELM: Only 19 of {total} papers are in HELM; column is mostly N/A.
  (3)&nbsp;lm-eval: 754 "Not Implementable" papers are a residual set; exact scores not recoverable.
  (4)&nbsp;Hover over a badge to see raw score.
</div>

<script>
const TIER_ORDER = {{"IMPLEMENTED":5,"READY":4,"POSSIBLE":3,"BARRIERS":2,"NOT_FEASIBLE":1,"N_A":0}};
const TIER_DISPLAY = {{"IMPLEMENTED":"In","READY":"Ready","POSSIBLE":"Possible","BARRIERS":"Barriers","NOT_FEASIBLE":"✗","N_A":"—"}};
const TOTAL = {total};
const DATA = {data_json};

let filtered = DATA.slice();

function tord(t) {{ return TIER_ORDER[t] || 0; }}

function matchesFilter(row, col, val) {{
  if (!val) return true;
  const o = tord(row[col]);
  if (val === "rp") return o >= 4;
  if (val === "pp") return o >= 3;
  if (val === "bw") return o <= 2;
  if (val === "na") return o === 0;
  return true;
}}

function applyFilters() {{
  const search = document.getElementById("search").value.toLowerCase();
  const minR = parseInt(document.getElementById("minReady").value) || 0;
  const fLm  = document.getElementById("f_lm").value;
  const fIns = document.getElementById("f_ins").value;
  const fLe  = document.getElementById("f_le").value;
  const fHm  = document.getElementById("f_hm").value;
  const fOa  = document.getElementById("f_oa").value;

  filtered = DATA.filter(function(row) {{
    if (search && row.k.toLowerCase().indexOf(search) === -1) return false;
    if (row.nr < minR) return false;
    if (!matchesFilter(row, "lm",  fLm))  return false;
    if (!matchesFilter(row, "ins", fIns)) return false;
    if (!matchesFilter(row, "le",  fLe))  return false;
    if (!matchesFilter(row, "hm",  fHm))  return false;
    if (!matchesFilter(row, "oa",  fOa))  return false;
    return true;
  }});

  document.getElementById("showCount").textContent = filtered.length;
  renderTable();
}}

function badge(tier, score, extra) {{
  const d = TIER_DISPLAY[tier] || tier;
  const tip = score !== null && score !== undefined ? tier + " (score: " + score + ")" : tier;
  const cls = extra ? "badge " + tier + " " + extra : "badge " + tier;
  return '<span class="' + cls + '" title="' + tip + '">' + d + '</span>';
}}

function renderTable() {{
  const tbody = document.getElementById("tableBody");
  const parts = [];
  for (let i = 0; i < filtered.length; i++) {{
    const r = filtered[i];
    parts.push(
      '<tr>',
      '<td class="paper"><span class="key">' + r.k + '</span><span class="yr">' + r.y + '</span></td>',
      '<td class="cell">' + badge(r.lm,  r.ls,  null) + '</td>',
      '<td class="cell">' + badge(r.ins, r.isc, null) + '</td>',
      '<td class="cell">' + badge(r.le,  r.les, null) + '</td>',
      '<td class="cell">' + badge(r.hm,  null,  null) + '</td>',
      '<td class="cell">' + badge(r.oa,  r.oas, null) + '</td>',
      '<td class="cell">' + badge(r.bt,  null,  "best-badge") + '</td>',
      '</tr>'
    );
  }}
  tbody.innerHTML = parts.join("");
}}

function resetFilters() {{
  document.getElementById("search").value = "";
  document.getElementById("minReady").value = "0";
  ["f_lm","f_ins","f_le","f_hm","f_oa"].forEach(function(id) {{
    document.getElementById(id).value = "";
  }});
  applyFilters();
}}

document.getElementById("search").addEventListener("input", applyFilters);
document.getElementById("minReady").addEventListener("change", applyFilters);
["f_lm","f_ins","f_le","f_hm","f_oa"].forEach(function(id) {{
  document.getElementById(id).addEventListener("change", applyFilters);
}});

applyFilters();
</script>
</body>
</html>"""

    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"Generated {OUT_HTML}")


# === Main ===
def count_tier(d, tier):
    return sum(1 for t, _ in d.values() if t == tier)


def main():
    print("Loading master paper list...")
    master = load_master_papers()
    print(f"  {len(master)} papers found")

    print("Parsing lm-eval (+ EleutherAI)...")
    lm = parse_lm_eval(master)
    print(
        f"  IMPL={count_tier(lm,IMPLEMENTED)} READY={count_tier(lm,READY)} "
        f"POSSIBLE={count_tier(lm,POSSIBLE)} BARRIERS={count_tier(lm,BARRIERS)} "
        f"NOT_FEASIBLE={count_tier(lm,NOT_FEASIBLE)}"
    )

    print("Parsing Inspect...")
    inspect = parse_inspect(master)
    print(
        f"  IMPL={count_tier(inspect,IMPLEMENTED)} READY={count_tier(inspect,READY)} "
        f"POSSIBLE={count_tier(inspect,POSSIBLE)} BARRIERS={count_tier(inspect,BARRIERS)} "
        f"NA={count_tier(inspect,NA)}"
    )

    print("Parsing LightEval (large file, may take a moment)...")
    lighteval = parse_lighteval(master)
    print(
        f"  READY={count_tier(lighteval,READY)} POSSIBLE={count_tier(lighteval,POSSIBLE)} "
        f"BARRIERS={count_tier(lighteval,BARRIERS)} NOT_FEASIBLE={count_tier(lighteval,NOT_FEASIBLE)} "
        f"NA={count_tier(lighteval,NA)}"
    )

    print("Parsing HELM...")
    helm = parse_helm(master)
    print(f"  IMPL={count_tier(helm,IMPLEMENTED)} NA={count_tier(helm,NA)}")

    print("Parsing OpenAI Evals (large file, may take a moment)...")
    openai = parse_openai(master)
    print(
        f"  READY={count_tier(openai,READY)} POSSIBLE={count_tier(openai,POSSIBLE)} "
        f"BARRIERS={count_tier(openai,BARRIERS)} NOT_FEASIBLE={count_tier(openai,NOT_FEASIBLE)} "
        f"NA={count_tier(openai,NA)}"
    )

    print("\nBuilding rows and sorting...")
    rows = build_rows(master, lm, inspect, lighteval, helm, openai)

    print("Generating CSV...")
    generate_csv(rows)

    print("Generating HTML...")
    generate_html(rows)

    print(f"\nDone. {len(rows)} rows total.")
    print(f"HELM check: {count_tier(helm, IMPLEMENTED)} IMPLEMENTED (expect ~19)")


if __name__ == "__main__":
    main()
