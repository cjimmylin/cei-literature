#!/usr/bin/env python3
"""
Phase 1F — Select 5 Qualitative Case Study Candidates

Per Council Recommendation R11, select 3 candidates per slot for council
selection of 5 qualitative case studies illustrating what keyword scoring
captures and misses.

Slots:
  1. Japanese syncretic paper
  2. Southeast Asian paper
  3. Sanctions-affected country paper
  4. Latin American Spanish paper (low buen_vivir despite relevant content)
  5. rv_* vs nw_* divergence (rv_islam vs nw_islamic_ethics)

Data sources:
  - DATA/20260403-nw-scores.json
  - DATA/20260403-author-geography.json
  - Paper YAML files for rv_* scores, short_title, abstract

Output: COUNCIL/20260403-case-study-candidates.md
"""
from __future__ import annotations

import functools
import json
import re
import sys
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Paths ──────────────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
_CULTURAL_GLOBAL = _SCRIPT_DIR.parent
_CEI_LIT_WS = _CULTURAL_GLOBAL.parent
_PAPERS_DIR = _CEI_LIT_WS / "papers"
_DATA_DIR = _CULTURAL_GLOBAL / "DATA"
_COUNCIL_DIR = _CULTURAL_GLOBAL / "COUNCIL"

NW_SCORES_FILE = _DATA_DIR / "20260403-nw-scores.json"
GEO_FILE = _DATA_DIR / "20260403-author-geography.json"

SANCTIONS_COUNTRIES = {"IR", "SY", "CU", "KP", "VE"}
LATAM_KEYWORDS = re.compile(
    r"latin\s*america|decolonial|indigenous|buen\s*vivir|sumak|andean|"
    r"postcolonial|colonialism|global\s*south|equity|developing\s*countr",
    re.IGNORECASE,
)

NW_FIELDS = [
    "nw_confucian",
    "nw_ubuntu",
    "nw_islamic_jurisprudence",  # still named this in the data file
    "nw_buddhist",
    "nw_dharmic",
    "nw_indigenous_relational",
    "nw_buen_vivir",
]


# ── YAML helpers ───────────────────────────────────────────────────────
def extract_yaml_field(text: str, field: str) -> str:
    """Extract a single YAML field value from frontmatter text."""
    m = re.search(rf'^{re.escape(field)}:\s*"?([^"\n]*)"?\s*$', text, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"')
    return ""


def extract_yaml_int(text: str, field: str) -> int:
    """Extract integer YAML field."""
    m = re.search(rf'^{re.escape(field)}:\s*(\d+)', text, re.MULTILINE)
    if m:
        return int(m.group(1))
    return 0


def load_paper_yaml(filename: str) -> str | None:
    """Load paper file content."""
    p = _PAPERS_DIR / filename
    if p.exists():
        return p.read_text(errors="replace")
    return None


# ── Load data ──────────────────────────────────────────────────────────
def load_data() -> tuple[dict, dict]:
    """Load NW scores and geography data, indexed by filename."""
    with open(NW_SCORES_FILE) as f:
        nw_data = json.load(f)
    with open(GEO_FILE) as f:
        geo_data = json.load(f)

    # Index by filename
    nw_by_file: dict[str, dict] = {}
    for p in nw_data["papers"]:
        nw_by_file[p["filename"]] = p["scores"]

    geo_by_file: dict[str, dict] = {}
    for p in geo_data["papers"]:
        geo_by_file[p["filename"]] = {
            "author_country": p.get("author_country", ""),
            "author_region": p.get("author_region", ""),
        }

    return nw_by_file, geo_by_file


# ── Slot 1: Japanese Syncretic ─────────────────────────────────────────
def find_japanese_syncretic(
    nw_by_file: dict, geo_by_file: dict
) -> list[dict]:
    """Find top-3 Japanese papers by nw_confucian score."""
    candidates = []
    for fn, geo in geo_by_file.items():
        if geo["author_country"] != "JP":
            continue
        scores = nw_by_file.get(fn, {})
        confucian = scores.get("nw_confucian", 0)
        candidates.append({
            "filename": fn,
            "nw_confucian": confucian,
            "scores": scores,
        })
    candidates.sort(key=lambda x: x["nw_confucian"], reverse=True)
    return candidates[:3]


# ── Slot 2: Southeast Asian ────────────────────────────────────────────
def find_southeast_asian(
    nw_by_file: dict, geo_by_file: dict
) -> list[dict]:
    """Find top-3 SE Asian papers by max across all nw_* scores."""
    candidates = []
    for fn, geo in geo_by_file.items():
        if geo["author_region"] != "Southeast Asia":
            continue
        scores = nw_by_file.get(fn, {})
        max_score = max(scores.values()) if scores else 0
        max_field = max(scores, key=scores.get) if scores else "none"
        candidates.append({
            "filename": fn,
            "max_nw_score": max_score,
            "max_field": max_field,
            "scores": scores,
        })
    candidates.sort(key=lambda x: x["max_nw_score"], reverse=True)
    return candidates[:3]


# ── Slot 3: Sanctions-Affected ─────────────────────────────────────────
def find_sanctions_affected(
    nw_by_file: dict, geo_by_file: dict
) -> list[dict]:
    """Find papers from sanctions-affected countries."""
    candidates = []
    for fn, geo in geo_by_file.items():
        if geo["author_country"] not in SANCTIONS_COUNTRIES:
            continue
        scores = nw_by_file.get(fn, {})
        max_score = max(scores.values()) if scores else 0
        candidates.append({
            "filename": fn,
            "author_country": geo["author_country"],
            "max_nw_score": max_score,
            "scores": scores,
        })
    candidates.sort(key=lambda x: x["max_nw_score"], reverse=True)
    return candidates[:3]


# ── Slot 4: Latin American Low Buen Vivir ──────────────────────────────
def find_latam_low_buen_vivir(
    nw_by_file: dict, geo_by_file: dict
) -> list[dict]:
    """Find LatAm papers with lowest buen_vivir despite relevant content."""
    candidates = []
    for fn, geo in geo_by_file.items():
        if geo["author_region"] != "Latin America & Caribbean":
            continue
        scores = nw_by_file.get(fn, {})
        bv = scores.get("nw_buen_vivir", 0)

        # Check if title/abstract mentions relevant terms
        text = load_paper_yaml(fn)
        if text is None:
            continue
        title = extract_yaml_field(text, "short_title")
        abstract = extract_yaml_field(text, "abstract")
        combined = f"{title} {abstract}"
        if not LATAM_KEYWORDS.search(combined):
            continue

        candidates.append({
            "filename": fn,
            "nw_buen_vivir": bv,
            "short_title": title[:80],
            "scores": scores,
        })
    # Sort ascending — lowest buen_vivir first
    candidates.sort(key=lambda x: x["nw_buen_vivir"])
    return candidates[:3]


# ── Slot 5: rv_islam vs nw_islamic divergence ──────────────────────────
def find_rv_nw_divergence(nw_by_file: dict) -> list[dict]:
    """Find papers with max |rv_islam - nw_islamic_jurisprudence|."""
    candidates = []
    for fn, scores in nw_by_file.items():
        nw_islamic = scores.get("nw_islamic_jurisprudence", 0)
        text = load_paper_yaml(fn)
        if text is None:
            continue
        rv_islam = extract_yaml_int(text, "rv_islam")
        divergence = abs(rv_islam - nw_islamic)
        if divergence < 10:
            continue
        short_title = extract_yaml_field(text, "short_title")
        candidates.append({
            "filename": fn,
            "rv_islam": rv_islam,
            "nw_islamic": nw_islamic,
            "divergence": divergence,
            "short_title": short_title[:80],
        })
    candidates.sort(key=lambda x: x["divergence"], reverse=True)
    return candidates[:3]


# ── Format helpers ─────────────────────────────────────────────────────
def fmt_scores(scores: dict) -> str:
    """Format all nw_* scores as a compact string."""
    parts = []
    labels = {
        "nw_confucian": "Conf",
        "nw_ubuntu": "Ubu",
        "nw_islamic_jurisprudence": "Isl",
        "nw_buddhist": "Bud",
        "nw_dharmic": "Dha",
        "nw_indigenous_relational": "Ind",
        "nw_buen_vivir": "BV",
    }
    for k, abbr in labels.items():
        v = scores.get(k, 0)
        if v > 0:
            parts.append(f"{abbr}={v}")
    return ", ".join(parts) if parts else "all 0"


def get_short_title(fn: str) -> str:
    """Get short_title from paper YAML."""
    text = load_paper_yaml(fn)
    if text:
        t = extract_yaml_field(text, "short_title")
        if t:
            return t[:70]
    # Fallback: extract from filename
    return fn.replace(".md", "")[:70]


# ── Main ───────────────────────────────────────────────────────────────
def main() -> None:
    print("Loading data...")
    nw_by_file, geo_by_file = load_data()
    print(f"  NW scores: {len(nw_by_file)} papers")
    print(f"  Geography: {len(geo_by_file)} papers")

    # ── Slot 1 ─────────────────────────────────────────────────────────
    print("\n== Slot 1: Japanese Syncretic ==")
    jp_cands = find_japanese_syncretic(nw_by_file, geo_by_file)
    if not jp_cands:
        print("  No Japanese papers found!")
    for c in jp_cands:
        print(f"  {c['filename'][:60]} | confucian={c['nw_confucian']} | {fmt_scores(c['scores'])}")

    # ── Slot 2 ─────────────────────────────────────────────────────────
    print("\n== Slot 2: Southeast Asian ==")
    sea_cands = find_southeast_asian(nw_by_file, geo_by_file)
    for c in sea_cands:
        print(f"  {c['filename'][:60]} | max={c['max_nw_score']} ({c['max_field']}) | {fmt_scores(c['scores'])}")

    # ── Slot 3 ─────────────────────────────────────────────────────────
    print("\n== Slot 3: Sanctions-Affected Country ==")
    sanc_cands = find_sanctions_affected(nw_by_file, geo_by_file)
    if not sanc_cands:
        print("  NO papers from sanctions-affected countries — this absence IS the case study")
    for c in sanc_cands:
        print(f"  {c['filename'][:60]} | country={c['author_country']} | max={c['max_nw_score']}")

    # ── Slot 4 ─────────────────────────────────────────────────────────
    print("\n== Slot 4: Latin American Low Buen Vivir ==")
    latam_cands = find_latam_low_buen_vivir(nw_by_file, geo_by_file)
    if not latam_cands:
        print("  No LatAm papers with relevant content and low buen_vivir found")
    for c in latam_cands:
        print(f"  {c['filename'][:60]} | buen_vivir={c['nw_buen_vivir']} | {c['short_title']}")

    # ── Slot 5 ─────────────────────────────────────────────────────────
    print("\n== Slot 5: rv_islam vs nw_islamic Divergence ==")
    div_cands = find_rv_nw_divergence(nw_by_file)
    for c in div_cands:
        print(f"  {c['filename'][:60]} | rv_islam={c['rv_islam']} nw_islamic={c['nw_islamic']} div={c['divergence']}")

    # ── Write output ───────────────────────────────────────────────────
    out_path = _COUNCIL_DIR / "20260403-case-study-candidates.md"
    lines: list[str] = []
    lines.append("# Case Study Candidates for Deliberation #2\n")
    lines.append("Per Council Recommendation R11 from Deliberation 01.\n")
    lines.append("3 candidates per slot for council selection.\n")
    lines.append(f"Data: {NW_SCORES_FILE.name}, {GEO_FILE.name}, paper YAML files.\n")
    lines.append("")

    # Slot 1
    lines.append("## Slot 1: Japanese Syncretic\n")
    lines.append("**Criterion:** Highest nw_confucian score among papers with author_country = JP.\n")
    lines.append("**Purpose:** Illustrate how keyword scoring handles hybrid Shinto-Buddhist-Confucian traditions.\n")
    lines.append("")
    if jp_cands:
        lines.append("| # | Paper | nw_confucian | Other NW Scores | Rationale |")
        lines.append("|---|-------|-------------|-----------------|-----------|")
        for i, c in enumerate(jp_cands, 1):
            title = get_short_title(c["filename"])
            other = fmt_scores({k: v for k, v in c["scores"].items() if k != "nw_confucian" and v > 0})
            rationale = "Highest Confucian score from JP" if i == 1 else f"#{i} Confucian score from JP"
            lines.append(f"| {i} | {title} | {c['nw_confucian']} | {other or 'none'} | {rationale} |")
    else:
        lines.append("**No Japanese papers found in vault.** This absence itself demonstrates the geographic gap in East Asian coverage beyond China.")
    lines.append("")

    # Slot 2
    lines.append("## Slot 2: Southeast Asian\n")
    lines.append("**Criterion:** Highest max across all 7 nw_* scores among papers with author_region = Southeast Asia.\n")
    lines.append("**Purpose:** Illustrate what keywords capture/miss in this culturally diverse, underrepresented region.\n")
    lines.append("")
    if sea_cands:
        lines.append("| # | Paper | Max NW Score | Leading Framework | All NW Scores | Rationale |")
        lines.append("|---|-------|-------------|-------------------|---------------|-----------|")
        for i, c in enumerate(sea_cands, 1):
            title = get_short_title(c["filename"])
            all_scores = fmt_scores(c["scores"])
            label_map = {
                "nw_confucian": "Confucian",
                "nw_ubuntu": "Ubuntu",
                "nw_islamic_jurisprudence": "Islamic",
                "nw_buddhist": "Buddhist",
                "nw_dharmic": "Dharmic",
                "nw_indigenous_relational": "Indigenous",
                "nw_buen_vivir": "Buen Vivir",
            }
            leading = label_map.get(c["max_field"], c["max_field"])
            lines.append(f"| {i} | {title} | {c['max_nw_score']} | {leading} | {all_scores} | Top SE Asian paper |")
    else:
        lines.append("**No Southeast Asian papers found.**")
    lines.append("")

    # Slot 3
    lines.append("## Slot 3: Sanctions-Affected Country\n")
    lines.append("**Criterion:** Paper with author_country in {IR, SY, CU, KP, VE}.\n")
    lines.append("**Purpose:** Illustrate structural exclusion from the corpus due to geopolitical sanctions.\n")
    lines.append("")
    if sanc_cands:
        lines.append("| # | Paper | Country | Max NW Score | All NW Scores | Rationale |")
        lines.append("|---|-------|---------|-------------|---------------|-----------|")
        for i, c in enumerate(sanc_cands, 1):
            title = get_short_title(c["filename"])
            all_scores = fmt_scores(c["scores"])
            lines.append(f"| {i} | {title} | {c['author_country']} | {c['max_nw_score']} | {all_scores} | Sanctions-affected country |")
    else:
        lines.append("**NO papers from sanctions-affected countries (IR, SY, CU, KP, VE) found in the vault.**\n")
        lines.append("This absence is itself the case study. Per Dr. Reza Shaker's testimony in Deliberation 01,")
        lines.append("Iranian AI ethics scholarship exists (Sharif University, University of Tehran, Isfahan University")
        lines.append("of Technology) but faces severe structural barriers: international sanctions limit access to")
        lines.append("computational resources, conference travel, journal subscriptions, and collaboration platforms.")
        lines.append("Iranian authors are sometimes blocked from submitting to Western journals. The complete absence")
        lines.append("of papers from all five sanctions-affected countries confirms that the corpus reflects")
        lines.append("geopolitical power structures, not intellectual engagement with AI ethics.\n")
        lines.append("**Recommendation:** Document this absence as a structural exclusion case study in the paper,")
        lines.append("citing Shaker's testimony and the broader sanctions literature on scholarly access barriers.")
    lines.append("")

    # Slot 4
    lines.append("## Slot 4: Latin American — Low Buen Vivir Despite Relevant Content\n")
    lines.append("**Criterion:** Paper with author_region = Latin America & Caribbean, lowest nw_buen_vivir score")
    lines.append("despite title/abstract mentioning Latin America, decolonial, indigenous, or related terms.\n")
    lines.append("**Purpose:** Illustrate the language/indexing gap — Latin American papers engaging relevant")
    lines.append("concepts in Western-legible vocabulary score low on buen_vivir keywords.\n")
    lines.append("")
    if latam_cands:
        lines.append("| # | Paper | nw_buen_vivir | Other NW Scores | Short Title | Rationale |")
        lines.append("|---|-------|--------------|-----------------|-------------|-----------|")
        for i, c in enumerate(latam_cands, 1):
            other = fmt_scores({k: v for k, v in c["scores"].items() if k != "nw_buen_vivir" and v > 0})
            lines.append(f"| {i} | {c['filename'][:60]} | {c['nw_buen_vivir']} | {other or 'none'} | {c['short_title']} | Low BV despite LatAm content |")
    else:
        lines.append("**No Latin American papers with relevant content and low buen_vivir found.**")
        lines.append("This may indicate the keyword list is working correctly, or that Latin American")
        lines.append("papers in the vault do not use buen vivir-adjacent vocabulary even in English.")
    lines.append("")

    # Slot 5
    lines.append("## Slot 5: rv_islam vs nw_islamic Divergence\n")
    lines.append("**Criterion:** Paper with maximum |rv_islam - nw_islamic_jurisprudence| score divergence.\n")
    lines.append("**Purpose:** Illustrate the descriptive-vs-normative distinction between religious values")
    lines.append("detection (rv_islam: Islamic content broadly) and normative framework detection")
    lines.append("(nw_islamic_ethics: engagement with Islamic ethical reasoning).\n")
    lines.append("")
    if div_cands:
        lines.append("| # | Paper | rv_islam | nw_islamic | Divergence | Short Title | Rationale |")
        lines.append("|---|-------|----------|-----------|------------|-------------|-----------|")
        for i, c in enumerate(div_cands, 1):
            lines.append(
                f"| {i} | {c['filename'][:55]} | {c['rv_islam']} | {c['nw_islamic']} | "
                f"{c['divergence']} | {c['short_title'][:50]} | "
                f"{'High rv, low nw: descriptive not normative' if c['rv_islam'] > c['nw_islamic'] else 'High nw, low rv: normative without religious framing'} |"
            )
    else:
        lines.append("**No papers with significant rv/nw divergence found.**")
    lines.append("")

    # Write
    out_path.write_text("\n".join(lines))
    print(f"\nOutput written to: {out_path}")
    print("Done.")


if __name__ == "__main__":
    main()
