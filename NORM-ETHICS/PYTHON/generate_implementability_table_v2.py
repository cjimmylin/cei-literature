#!/usr/bin/env python3
"""
Generate cross-framework implementability table v2 — adds normative ethics filters.
Extends the v1 table with YAML frontmatter fields:
  ethics_overall, virtue_ethics, deontological_ethics, utilitarian_ethics,
  ethics_perspective, normative_ethics_benchmark
"""

import re
import json
import csv
import sys
from pathlib import Path

# === Paths ===
BASE       = Path(__file__).parent.parent
STATS      = BASE / "STATISTICS"
PAPERS_DIR = BASE / "papers"
OUT_HTML   = STATS / "20260313-implementability-cross-framework-table-v2.html"
OUT_CSV    = STATS / "20260313-implementability-cross-framework-table-v2.csv"

# === Tier codes ===
IMPLEMENTED  = "IMPLEMENTED"
READY        = "READY"
POSSIBLE     = "POSSIBLE"
BARRIERS     = "BARRIERS"
NOT_FEASIBLE = "NOT_FEASIBLE"
NA           = "N_A"

TIER_ORDER = {IMPLEMENTED: 5, READY: 4, POSSIBLE: 3, BARRIERS: 2, NOT_FEASIBLE: 1, NA: 0}
TIER_DISPLAY = {
    IMPLEMENTED: "In", READY: "Ready", POSSIBLE: "Possible",
    BARRIERS: "Barriers", NOT_FEASIBLE: "✗", NA: "—",
}

LIGHTEVAL_TIER_MAP = {
    "Ready": READY, "Possible": POSSIBLE,
    "Barriers": BARRIERS, "Not Implementable": NOT_FEASIBLE,
}

ETHICS_INT_FIELDS = [
    "ethics_overall", "virtue_ethics", "deontological_ethics", "utilitarian_ethics",
]
ETHICS_STR_FIELDS = [
    "ethics_perspective", "normative_ethics_benchmark",
]


# ── Key normalization ──────────────────────────────────────────────────────────
def normalize_key(s):
    return s.strip().strip("`").removesuffix(".md").strip()

def get_year(key):
    m = re.match(r"^(\d{4})", key)
    return m.group(1) if m else "0000"


# ── Master paper list ──────────────────────────────────────────────────────────
def load_master_papers():
    papers = {}
    for p in PAPERS_DIR.iterdir():
        if p.suffix == ".md":
            papers[p.stem] = get_year(p.stem)
    return papers


# ── Fuzzy key match ────────────────────────────────────────────────────────────
def fuzzy_match(key, master):
    parts = key.split("-")
    if len(parts) >= 2:
        prefix = parts[0] + "-" + parts[1] + "-"
        candidates = [k for k in master if k.startswith(prefix)]
        if len(candidates) == 1:
            return candidates[0]
    return None

def resolve_key(raw, master):
    key = normalize_key(raw)
    if key in master:
        return key
    matched = fuzzy_match(key, master)
    if matched:
        return matched
    print(f"  UNMATCHED: {repr(key)}", file=sys.stderr)
    return None


# ── Ethics YAML loader ─────────────────────────────────────────────────────────
def load_paper_ethics(master):
    """Read ethics-related YAML fields from each paper's frontmatter."""
    result = {}
    for key in master:
        filepath = PAPERS_DIR / (key + ".md")
        if not filepath.exists():
            result[key] = _empty_ethics()
            continue
        text = filepath.read_text(encoding="utf-8", errors="replace")
        fm_m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        fm = fm_m.group(1) if fm_m else ""
        data = {}
        for field in ETHICS_INT_FIELDS:
            m = re.search(rf"^{re.escape(field)}:\s*(\d+)", fm, re.MULTILINE)
            data[field] = int(m.group(1)) if m else 0
        for field in ETHICS_STR_FIELDS:
            m = re.search(rf'^{re.escape(field)}:\s*(.+?)$', fm, re.MULTILINE)
            if m:
                data[field] = m.group(1).strip().strip('"').strip("'")
            else:
                data[field] = ""
        result[key] = data
    return result

def _empty_ethics():
    d = {f: 0 for f in ETHICS_INT_FIELDS}
    d.update({f: "" for f in ETHICS_STR_FIELDS})
    return d


# ── Framework parsers (identical to v1) ───────────────────────────────────────
def parse_lm_eval(master):
    results = {}
    ea_path = STATS / "20260312-eleutherai-eval-harness-integration.md"
    ea_text = ea_path.read_text(encoding="utf-8")
    for m in re.finditer(r"^\| \d+ \| (.+?) \|", ea_text, re.MULTILINE):
        raw = m.group(1).strip()
        if not re.match(r"\d{4}-", raw):
            continue
        key = resolve_key(raw, master)
        if key:
            results[key] = (IMPLEMENTED, None)

    lm_text = (STATS / "20260312-lm-eval-implementability-report.md").read_text(encoding="utf-8")

    sec1 = re.search(r"## 1\. Already.*?\n(.*?)(?=## 2\.)", lm_text, re.DOTALL)
    if sec1:
        for m in re.finditer(r"^\| (.+?) \| \d{4} \|", sec1.group(1), re.MULTILINE):
            raw = m.group(1).strip()
            if raw == "Paper": continue
            key = resolve_key(raw, master)
            if key: results[key] = (IMPLEMENTED, None)

    for section, tier in [
        (r"## 2\. Ready.*?\n(.*?)(?=## 3\.)",          READY),
        (r"## 3\. Needs Dataset.*?\n(.*?)(?=## 4\.)",   POSSIBLE),
        (r"## 4\. Needs More Info.*?\n(.*?)(?=## 5\.)", BARRIERS),
    ]:
        sec = re.search(section, lm_text, re.DOTALL)
        if sec:
            for m in re.finditer(r"^\| \d+ \| (.+?) \| (\d+) \|", sec.group(1), re.MULTILINE):
                raw, score = m.group(1).strip(), int(m.group(2))
                key = resolve_key(raw, master)
                if key and key not in results:
                    results[key] = (tier, score)

    for key in master:
        if key not in results:
            results[key] = (NOT_FEASIBLE, None)
    return results


def parse_inspect(master):
    results = {}
    text = (STATS / "20260312-inspect-eval-implementability-report.md").read_text(encoding="utf-8")

    sec1 = re.search(r"## 1\. Already.*?\n(.*?)(?=## 2\.)", text, re.DOTALL)
    if sec1:
        for m in re.finditer(r"^\| (.+?\.md) \|", sec1.group(1), re.MULTILINE):
            raw = m.group(1).strip()
            if raw == "Paper": continue
            key = resolve_key(raw, master)
            if key: results[key] = (IMPLEMENTED, None)

    for section, tier in [
        (r"## 2\. Ready.*?\n(.*?)(?=## 3\.)",           READY),
        (r"## 3\. Model-Graded.*?\n(.*?)(?=## 4\.)",    POSSIBLE),
    ]:
        sec = re.search(section, text, re.DOTALL)
        if sec:
            for m in re.finditer(r"^\| (.+?\.md) \| [^|]+ \| (\d+) \|", sec.group(1), re.MULTILINE):
                raw, score = m.group(1).strip(), int(m.group(2))
                if raw == "Paper": continue
                key = resolve_key(raw, master)
                if key and key not in results:
                    results[key] = (tier, score)

    sec5 = re.search(r"## 5\. Needs Dataset Work.*?\n(.*?)(?=## 6\.)", text, re.DOTALL)
    if sec5:
        for m in re.finditer(r"^\| (.+?\.md) \| (\d+) \|", sec5.group(1), re.MULTILINE):
            raw, score = m.group(1).strip(), int(m.group(2))
            if raw == "Paper": continue
            key = resolve_key(raw, master)
            if key and key not in results:
                results[key] = (BARRIERS, score)

    for key in master:
        if key not in results:
            results[key] = (NA, None)
    return results


def _parse_scored_report(path, master, default_tier):
    results = {}
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
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
    app = re.search(r"## Appendix:.*?\n(.*?)$", text, re.DOTALL)
    if app:
        for m in re.finditer(r"^\| (.+?) \| ([\d.]+) \| ([\w][\w ]+?) \|", app.group(1), re.MULTILINE):
            raw, score_str, tier_name = m.group(1).strip(), m.group(2), m.group(3).strip()
            if raw in ("Paper", "#"): continue
            tier = LIGHTEVAL_TIER_MAP.get(tier_name, NA)
            key = resolve_key(raw, master)
            if key and key not in results:
                results[key] = (tier, float(score_str))
    for key in master:
        if key not in results:
            results[key] = (default_tier, None)
    return results


def parse_lighteval(master):
    return _parse_scored_report(
        STATS / "20260312-lighteval-paper-reports.md", master, NA)

def parse_openai(master):
    return _parse_scored_report(
        STATS / "20260312-openai-evals-paper-reports.md", master, NA)


def parse_helm(master):
    results = {}
    text = (STATS / "20260312-helm-values-alignment-integration-report.md").read_text(encoding="utf-8")
    for m in re.finditer(r"`(?:papers/)?(\d{4}-[^`]+\.md)`", text):
        key = resolve_key(m.group(1), master)
        if key: results[key] = (IMPLEMENTED, None)
    for key in master:
        if key not in results:
            results[key] = (NA, None)
    return results


# ── Build rows ─────────────────────────────────────────────────────────────────
def build_rows(master, lm, inspect, lighteval, helm, openai, ethics):
    rows = []
    for key, year in master.items():
        lm_tier,  lm_score  = lm.get(key,        (NA, None))
        ins_tier, ins_score  = inspect.get(key,   (NA, None))
        le_tier,  le_score   = lighteval.get(key, (NA, None))
        helm_tier, _         = helm.get(key,      (NA, None))
        oa_tier,  oa_score   = openai.get(key,    (NA, None))
        eth = ethics.get(key, _empty_ethics())

        tiers = [lm_tier, ins_tier, le_tier, helm_tier, oa_tier]
        tier_vals = [TIER_ORDER[t] for t in tiers]
        best_val  = max(tier_vals)
        best_tier = next(t for t in tiers if TIER_ORDER[t] == best_val)
        n_ready   = sum(1 for t in tiers if TIER_ORDER[t] >= TIER_ORDER[READY])
        sort_score = sum(tier_vals) / len(tier_vals)

        rows.append({
            "paper_key":        key,
            "year":             year,
            "lm_eval_tier":     lm_tier,  "lm_eval_score":   lm_score,
            "inspect_tier":     ins_tier, "inspect_score":   ins_score,
            "lighteval_tier":   le_tier,  "lighteval_score": le_score,
            "helm_tier":        helm_tier,
            "openai_tier":      oa_tier,  "openai_score":    oa_score,
            "best_tier":        best_tier,
            "n_ready_or_better": n_ready,
            "sort_score":       sort_score,
            # ethics fields
            "ethics_overall":            eth.get("ethics_overall", 0),
            "virtue_ethics":             eth.get("virtue_ethics", 0),
            "deontological_ethics":      eth.get("deontological_ethics", 0),
            "utilitarian_ethics":        eth.get("utilitarian_ethics", 0),
            "ethics_perspective":        eth.get("ethics_perspective", ""),
            "normative_ethics_benchmark": eth.get("normative_ethics_benchmark", ""),
        })

    rows.sort(key=lambda r: (-r["n_ready_or_better"], -r["sort_score"]))
    return rows


# ── CSV ────────────────────────────────────────────────────────────────────────
def generate_csv(rows):
    fields = [
        "paper_key", "year",
        "lm_eval_tier", "lm_eval_score",
        "inspect_tier", "inspect_score",
        "lighteval_tier", "lighteval_score",
        "helm_tier",
        "openai_tier", "openai_score",
        "best_tier", "n_ready_or_better", "sort_score",
        "ethics_overall", "virtue_ethics", "deontological_ethics", "utilitarian_ethics",
        "ethics_perspective", "normative_ethics_benchmark",
    ]
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"Generated {OUT_CSV}")


# ── HTML ───────────────────────────────────────────────────────────────────────
def generate_html(rows):
    total    = len(rows)
    lm_ready = sum(1 for r in rows if TIER_ORDER[r["lm_eval_tier"]]      >= TIER_ORDER[READY])
    ins_ready= sum(1 for r in rows if TIER_ORDER[r["inspect_tier"]]       >= TIER_ORDER[READY])
    le_ready = sum(1 for r in rows if TIER_ORDER[r["lighteval_tier"]]     >= TIER_ORDER[READY])
    helm_impl= sum(1 for r in rows if r["helm_tier"] == IMPLEMENTED)
    oa_ready = sum(1 for r in rows if TIER_ORDER[r["openai_tier"]]        >= TIER_ORDER[READY])

    # Collect distinct ethics_perspective values (sorted by frequency)
    from collections import Counter
    persp_counts = Counter(r["ethics_perspective"] for r in rows if r["ethics_perspective"])
    perspectives = [v for v, _ in persp_counts.most_common()]

    # Compact JSON payload
    json_rows = []
    for r in rows:
        json_rows.append({
            "k":   r["paper_key"],
            "y":   r["year"],
            "lm":  r["lm_eval_tier"],  "ls": r["lm_eval_score"],
            "ins": r["inspect_tier"],  "isc": r["inspect_score"],
            "le":  r["lighteval_tier"],"les": r["lighteval_score"],
            "hm":  r["helm_tier"],
            "oa":  r["openai_tier"],   "oas": r["openai_score"],
            "bt":  r["best_tier"],
            "nr":  r["n_ready_or_better"],
            "eo":  r["ethics_overall"],
            "ve":  r["virtue_ethics"],
            "de":  r["deontological_ethics"],
            "ue":  r["utilitarian_ethics"],
            "ep":  r["ethics_perspective"],
            "nb":  r["normative_ethics_benchmark"],
        })

    data_json = json.dumps(json_rows, ensure_ascii=False)

    persp_options = "\n".join(
        f'      <option value="{v}">{v}</option>' for v in perspectives
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cross-Framework Implementability + Ethics Filters — CEI Vault</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0f0f1a; color: #e0e0e0; font-size: 13px; }}
header {{ background: #1a1a2e; padding: 14px 20px; border-bottom: 2px solid #3a3a6a; }}
header h1 {{ font-size: 1.1rem; color: #a0b4e0; font-weight: 600; }}
header p  {{ font-size: 0.72rem; color: #5868a0; margin-top: 3px; }}

/* ── Controls ── */
.controls {{ background: #181828; border-bottom: 1px solid #252540; position: sticky; top: 0; z-index: 100; }}
.ctrl-row {{ padding: 8px 20px; display: flex; flex-wrap: wrap; gap: 7px 11px; align-items: flex-end; }}
.ctrl-row + .ctrl-row {{ border-top: 1px solid #1e1e38; background: #151522; }}
.ctrl-section-label {{ font-size: 0.6rem; color: #3a4878; text-transform: uppercase; letter-spacing: 0.08em; align-self: center; padding-right: 4px; white-space: nowrap; border-right: 1px solid #252545; margin-right: 4px; padding-bottom: 1px; }}
.ctrl-group {{ display: flex; flex-direction: column; gap: 2px; }}
.ctrl-group label {{ font-size: 0.62rem; color: #5868a0; text-transform: uppercase; letter-spacing: 0.04em; }}
.controls input, .controls select {{ background: #242438; border: 1px solid #3a3a5a; color: #d0d8f0; padding: 4px 7px; border-radius: 3px; font-size: 0.73rem; }}
.controls input {{ width: 190px; }}
.controls select {{ min-width: 110px; }}
.controls button {{ background: #2e2e50; border: 1px solid #4a4a7a; color: #a0b0d8; padding: 4px 10px; border-radius: 3px; cursor: pointer; font-size: 0.7rem; align-self: flex-end; }}
.controls button:hover {{ background: #3a3a68; }}
.controls button.eth-btn {{ background: #1a2840; border-color: #2a5080; color: #7ab0e0; }}
.controls button.eth-btn:hover {{ background: #1e3355; }}

/* ethics filter row highlight */
.ctrl-row.ethics-row {{ background: #11182a; }}
.ctrl-row.ethics-row .ctrl-group label {{ color: #4878a8; }}
.eth-score-select {{ border-color: #2a4a6a !important; }}

/* ── Stats bar ── */
.stats-bar {{ background: #111120; padding: 6px 20px; font-size: 0.7rem; color: #4858a0; border-bottom: 1px solid #1a1a34; display: flex; flex-wrap: wrap; gap: 0 18px; }}
.stats-bar .val {{ color: #7888c0; font-weight: 600; }}

/* ── Table ── */
.table-wrap {{ overflow: auto; height: calc(100vh - 178px); }}
table {{ width: 100%; border-collapse: collapse; }}
thead th {{ background: #1a1a2e; padding: 9px 8px; text-align: left; color: #6878a8; font-size: 0.67rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; border-bottom: 2px solid #3a3a6a; position: sticky; top: 0; white-space: nowrap; }}
thead th.fw {{ text-align: center; min-width: 76px; }}
thead th.eth-h {{ text-align: center; min-width: 82px; color: #3a5878; border-left: 1px solid #1e2a3a; }}
tbody tr {{ border-bottom: 1px solid #161626; }}
tbody tr:hover {{ background: #1a1a30; }}
td {{ padding: 6px 8px; vertical-align: middle; }}
td.paper {{ max-width: 300px; }}
td.paper .key {{ color: #b0c4e8; font-size: 0.72rem; line-height: 1.3; word-break: break-word; }}
td.paper .yr  {{ color: #3a4870; font-size: 0.65rem; margin-left: 4px; }}
td.cell {{ text-align: center; }}
td.eth-cell {{ text-align: center; border-left: 1px solid #1a2030; }}

/* ── Framework badges ── */
.badge {{ display: inline-block; padding: 2px 6px; border-radius: 2px; font-size: 0.63rem; font-weight: 700; color: #fff; cursor: default; white-space: nowrap; }}
.badge.IMPLEMENTED {{ background: #1565c0; }}
.badge.READY       {{ background: #2e7d32; }}
.badge.POSSIBLE    {{ background: #f57f17; color: #1a0f00; }}
.badge.BARRIERS    {{ background: #bf360c; }}
.badge.NOT_FEASIBLE{{ background: #7f0000; }}
.badge.N_A         {{ background: #1e1e2e; color: #3a4060; border: 1px solid #252545; }}
.badge.best-badge  {{ outline: 2px solid rgba(255,255,255,0.18); outline-offset: 1px; }}

/* ── Ethics column ── */
.eth-block {{ display: flex; flex-direction: column; align-items: center; gap: 3px; }}
.eth-score {{ font-size: 0.72rem; font-weight: 700; }}
.eth-score.hi  {{ color: #66bb6a; }}
.eth-score.mid {{ color: #ffa726; }}
.eth-score.lo  {{ color: #5060a0; }}
.eth-score.nil {{ color: #222840; }}
.eth-trio {{ display: flex; gap: 3px; }}
.eth-pip {{ display: inline-block; width: 18px; height: 4px; border-radius: 2px; }}
.eth-label {{ font-size: 0.55rem; color: #304060; text-align: center; width: 18px; line-height: 1; }}

/* ── Footer ── */
.footer {{ padding: 10px 20px; color: #2e3858; font-size: 0.67rem; border-top: 1px solid #1a1a34; line-height: 1.7; }}
</style>
</head>
<body>

<header>
  <h1>TABLE 2 — Cross-Framework Implementability + Ethics Filters (v2)</h1>
  <p>CEI Literature Vault &nbsp;·&nbsp; {total} papers &times; 5 frameworks &nbsp;·&nbsp; Generated 2026-03-13</p>
</header>

<!-- Row 1: framework filters -->
<div class="controls">
<div class="ctrl-row">
  <span class="ctrl-section-label">Framework</span>
  <div class="ctrl-group">
    <label>Search</label>
    <input type="text" id="search" placeholder="Filter by paper title…">
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
      <option value="rp">In Framework</option>
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
  <button onclick="resetFilters()">Reset all</button>
</div>

<!-- Row 2: normative ethics filters -->
<div class="ctrl-row ethics-row">
  <span class="ctrl-section-label">Ethics</span>
  <div class="ctrl-group">
    <label>ethics_overall ≥</label>
    <select id="f_eo" class="eth-score-select">
      <option value="0">Any</option>
      <option value="1">Any non-zero</option>
      <option value="25">≥ 25</option>
      <option value="50">≥ 50 (ethics yes)</option>
      <option value="75">≥ 75 (strong)</option>
    </select>
  </div>
  <div class="ctrl-group">
    <label>virtue_ethics ≥</label>
    <select id="f_ve" class="eth-score-select">
      <option value="0">Any</option>
      <option value="1">Any non-zero</option>
      <option value="25">≥ 25</option>
      <option value="50">≥ 50</option>
    </select>
  </div>
  <div class="ctrl-group">
    <label>deontological ≥</label>
    <select id="f_de" class="eth-score-select">
      <option value="0">Any</option>
      <option value="1">Any non-zero</option>
      <option value="25">≥ 25</option>
      <option value="50">≥ 50</option>
    </select>
  </div>
  <div class="ctrl-group">
    <label>utilitarian ≥</label>
    <select id="f_ue" class="eth-score-select">
      <option value="0">Any</option>
      <option value="1">Any non-zero</option>
      <option value="25">≥ 25</option>
      <option value="50">≥ 50</option>
    </select>
  </div>
  <div class="ctrl-group">
    <label>ethics_perspective</label>
    <select id="f_ep">
      <option value="">Any</option>
{persp_options}
    </select>
  </div>
  <div class="ctrl-group">
    <label>normative_benchmark</label>
    <select id="f_nb">
      <option value="">Any</option>
      <option value="Yes">Yes</option>
      <option value="Borderline">Borderline</option>
      <option value="Yes|Borderline">Yes or Borderline</option>
    </select>
  </div>
</div>
</div><!-- /.controls -->

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
  <th style="min-width:260px">Paper</th>
  <th class="fw">lm-eval</th>
  <th class="fw">Inspect</th>
  <th class="fw">LightEval</th>
  <th class="fw">HELM</th>
  <th class="fw">OpenAI</th>
  <th class="fw">Best</th>
  <th class="eth-h">Ethics<br><span style="font-size:0.55rem;font-weight:400;letter-spacing:0">overall · V · D · U</span></th>
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
  &nbsp;·&nbsp;
  <strong>Ethics column:</strong> overall score (green ≥75, amber ≥50, dim &lt;25) + trio bars: V=virtue D=deontological U=utilitarian (height ∝ score/100).
  <br>
  <strong>Notes:</strong>
  (1)&nbsp;Inspect: ~1,440 bottom-tier papers not individually resolvable — shown as N/A.
  (2)&nbsp;HELM: 19 of {total} papers are in HELM.
  (3)&nbsp;ethics_overall ≥ 50 = ethics "yes" threshold per vault convention.
</div>

<script>
const TIER_ORDER   = {{"IMPLEMENTED":5,"READY":4,"POSSIBLE":3,"BARRIERS":2,"NOT_FEASIBLE":1,"N_A":0}};
const TIER_DISPLAY = {{"IMPLEMENTED":"In","READY":"Ready","POSSIBLE":"Possible","BARRIERS":"Barriers","NOT_FEASIBLE":"✗","N_A":"—"}};
const TOTAL = {total};
const DATA  = {data_json};

let filtered = DATA.slice();

function tord(t) {{ return TIER_ORDER[t] || 0; }}

function matchesFW(row, col, val) {{
  if (!val) return true;
  const o = tord(row[col]);
  if (val === "rp") return o >= 4;
  if (val === "pp") return o >= 3;
  if (val === "bw") return o <= 2;
  if (val === "na") return o === 0;
  return true;
}}

function applyFilters() {{
  const search  = document.getElementById("search").value.toLowerCase();
  const minR    = parseInt(document.getElementById("minReady").value) || 0;
  const fLm     = document.getElementById("f_lm").value;
  const fIns    = document.getElementById("f_ins").value;
  const fLe     = document.getElementById("f_le").value;
  const fHm     = document.getElementById("f_hm").value;
  const fOa     = document.getElementById("f_oa").value;
  const fEo     = parseInt(document.getElementById("f_eo").value) || 0;
  const fVe     = parseInt(document.getElementById("f_ve").value) || 0;
  const fDe     = parseInt(document.getElementById("f_de").value) || 0;
  const fUe     = parseInt(document.getElementById("f_ue").value) || 0;
  const fEp     = document.getElementById("f_ep").value;
  const fNb     = document.getElementById("f_nb").value;

  filtered = DATA.filter(function(r) {{
    if (search && r.k.toLowerCase().indexOf(search) === -1) return false;
    if (r.nr < minR) return false;
    if (!matchesFW(r, "lm",  fLm))  return false;
    if (!matchesFW(r, "ins", fIns)) return false;
    if (!matchesFW(r, "le",  fLe))  return false;
    if (!matchesFW(r, "hm",  fHm))  return false;
    if (!matchesFW(r, "oa",  fOa))  return false;
    // ethics score filters
    if (fEo === 1 && r.eo <= 0) return false;
    if (fEo  > 1 && r.eo < fEo) return false;
    if (fVe === 1 && r.ve <= 0) return false;
    if (fVe  > 1 && r.ve < fVe) return false;
    if (fDe === 1 && r.de <= 0) return false;
    if (fDe  > 1 && r.de < fDe) return false;
    if (fUe === 1 && r.ue <= 0) return false;
    if (fUe  > 1 && r.ue < fUe) return false;
    // ethics_perspective
    if (fEp && r.ep !== fEp) return false;
    // normative_benchmark
    if (fNb) {{
      if (fNb === "Yes|Borderline") {{
        if (r.nb !== "Yes" && r.nb !== "Borderline") return false;
      }} else {{
        if (r.nb !== fNb) return false;
      }}
    }}
    return true;
  }});

  document.getElementById("showCount").textContent = filtered.length;
  renderTable();
}}

function scoreClass(v) {{
  if (v >= 75) return "hi";
  if (v >= 50) return "mid";
  if (v >= 25) return "lo";
  return "nil";
}}

function pipColor(v) {{
  if (v >= 75) return "#388e3c";
  if (v >= 50) return "#f57f17";
  if (v >= 25) return "#1e4a6a";
  return "#181828";
}}

function ethicsCell(r) {{
  const cls = scoreClass(r.eo);
  const vCol = pipColor(r.ve);
  const dCol = pipColor(r.de);
  const uCol = pipColor(r.ue);
  const vH = Math.max(2, Math.round(r.ve / 100 * 14)) + "px";
  const dH = Math.max(2, Math.round(r.de / 100 * 14)) + "px";
  const uH = Math.max(2, Math.round(r.ue / 100 * 14)) + "px";
  const scoreStr = r.eo > 0 ? r.eo : "—";
  let tip = "ethics_overall: " + r.eo;
  if (r.ve) tip += " | virtue: " + r.ve;
  if (r.de) tip += " | deont: " + r.de;
  if (r.ue) tip += " | util: " + r.ue;
  if (r.ep) tip += " | " + r.ep;
  if (r.nb) tip += " | benchmark: " + r.nb;
  return '<td class="eth-cell" title="' + tip + '">' +
    '<div class="eth-block">' +
    '<span class="eth-score ' + cls + '">' + scoreStr + '</span>' +
    '<div class="eth-trio">' +
    '<div style="display:flex;flex-direction:column;align-items:center;gap:1px">' +
      '<div class="eth-pip" style="background:' + vCol + ';height:' + vH + '"></div>' +
      '<span class="eth-label">V</span>' +
    '</div>' +
    '<div style="display:flex;flex-direction:column;align-items:center;gap:1px">' +
      '<div class="eth-pip" style="background:' + dCol + ';height:' + dH + '"></div>' +
      '<span class="eth-label">D</span>' +
    '</div>' +
    '<div style="display:flex;flex-direction:column;align-items:center;gap:1px">' +
      '<div class="eth-pip" style="background:' + uCol + ';height:' + uH + '"></div>' +
      '<span class="eth-label">U</span>' +
    '</div>' +
    '</div>' +
    '</div>' +
    '</td>';
}}

function badge(tier, score, extra) {{
  const d = TIER_DISPLAY[tier] || tier;
  const tip = score !== null && score !== undefined ? tier + " (" + score + ")" : tier;
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
      ethicsCell(r),
      '</tr>'
    );
  }}
  tbody.innerHTML = parts.join("");
}}

function resetFilters() {{
  ["search"].forEach(function(id) {{ document.getElementById(id).value = ""; }});
  ["minReady","f_lm","f_ins","f_le","f_hm","f_oa",
   "f_eo","f_ve","f_de","f_ue","f_ep","f_nb"].forEach(function(id) {{
    document.getElementById(id).value = id === "minReady" ? "0" : "";
    if (id.startsWith("f_e") || id.startsWith("f_v") || id.startsWith("f_d") || id.startsWith("f_u")) {{
      document.getElementById(id).value = "0";
    }}
  }});
  applyFilters();
}}

document.getElementById("search").addEventListener("input", applyFilters);
["minReady","f_lm","f_ins","f_le","f_hm","f_oa",
 "f_eo","f_ve","f_de","f_ue","f_ep","f_nb"].forEach(function(id) {{
  document.getElementById(id).addEventListener("change", applyFilters);
}});

applyFilters();
</script>
</body>
</html>"""

    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"Generated {OUT_HTML}")


# ── Main ───────────────────────────────────────────────────────────────────────
def count_tier(d, tier):
    return sum(1 for t, _ in d.values() if t == tier)

def main():
    print("Loading master paper list...")
    master = load_master_papers()
    print(f"  {len(master)} papers")

    print("Loading ethics YAML fields from frontmatter...")
    ethics = load_paper_ethics(master)
    eth_nonzero = sum(1 for v in ethics.values() if v.get("ethics_overall", 0) > 0)
    print(f"  ethics_overall > 0: {eth_nonzero} papers")

    print("Parsing lm-eval...")
    lm = parse_lm_eval(master)
    print("Parsing Inspect...")
    inspect = parse_inspect(master)
    print("Parsing LightEval...")
    lighteval = parse_lighteval(master)
    print("Parsing HELM...")
    helm = parse_helm(master)
    print("Parsing OpenAI Evals...")
    openai = parse_openai(master)

    print("Building rows...")
    rows = build_rows(master, lm, inspect, lighteval, helm, openai, ethics)

    print("Generating CSV...")
    generate_csv(rows)
    print("Generating HTML...")
    generate_html(rows)

    print(f"\nDone. {len(rows)} rows. HELM IMPL: {count_tier(helm, IMPLEMENTED)}")

if __name__ == "__main__":
    main()
