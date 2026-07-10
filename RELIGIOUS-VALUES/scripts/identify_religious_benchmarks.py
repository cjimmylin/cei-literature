#!/usr/bin/env python3
"""
Phase 1: Identify Religious Values Benchmark Candidates from Vault

Scans all papers in the vault for the intersection of:
  - is_benchmark/is_eval/is_dataset = Yes
  - rv_* >= 50 OR nw_* >= 50
  - Filters out demographic-only papers (bias/fairness where religion is incidental)

Scope: Theological + Values (genuine religious content, not just bias-as-demographic)

Output: RELIGIOUS-VALUES/data/YYYYMMDD-religious-benchmark-candidates.json
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent          # RELIGIOUS-VALUES/
WS_ROOT = PROJECT_DIR.parent             # CEI-Lit-WS/
PAPERS_DIR = WS_ROOT / "papers"
EXTRACTS_DIR = WS_ROOT / "PDF Extracts"
DATA_DIR = PROJECT_DIR / "data"

TODAY = date.today().strftime("%Y%m%d")

# ---------------------------------------------------------------------------
# Religious Values fields (14 traditions) and Non-Western fields (7)
# ---------------------------------------------------------------------------
RV_FIELDS = [
    "rv_islam", "rv_christianity", "rv_buddhism", "rv_judaism",
    "rv_hinduism", "rv_sikhism", "rv_confucianism", "rv_taoism",
    "rv_shinto", "rv_jainism", "rv_bahai", "rv_zoroastrianism",
    "rv_ubuntu", "rv_indigenous",
]

NW_FIELDS = [
    "nw_confucian", "nw_ubuntu", "nw_islamic_ethics",
    "nw_buddhist", "nw_dharmic", "nw_indigenous_relational", "nw_buen_vivir",
]

TRADITION_LABELS = {
    "rv_islam": "Islam", "rv_christianity": "Christianity",
    "rv_buddhism": "Buddhism", "rv_judaism": "Judaism",
    "rv_hinduism": "Hinduism", "rv_sikhism": "Sikhism",
    "rv_confucianism": "Confucianism", "rv_taoism": "Taoism",
    "rv_shinto": "Shinto", "rv_jainism": "Jainism",
    "rv_bahai": "Baha'i", "rv_zoroastrianism": "Zoroastrianism",
    "rv_ubuntu": "Ubuntu Philosophy", "rv_indigenous": "Indigenous Spirituality",
    "nw_confucian": "Confucian (NW)", "nw_ubuntu": "Ubuntu (NW)",
    "nw_islamic_ethics": "Islamic Ethics (NW)",
    "nw_buddhist": "Buddhist (NW)", "nw_dharmic": "Dharmic (NW)",
    "nw_indigenous_relational": "Indigenous Relational (NW)",
    "nw_buen_vivir": "Buen Vivir (NW)",
}

TRADITION_FAMILY = {
    "Islam": "Abrahamic", "Christianity": "Abrahamic", "Judaism": "Abrahamic",
    "Hinduism": "Dharmic", "Buddhism": "Dharmic", "Jainism": "Dharmic", "Sikhism": "Dharmic",
    "Confucianism": "East Asian", "Taoism": "East Asian", "Shinto": "East Asian",
    "Ubuntu Philosophy": "African/Indigenous", "Indigenous Spirituality": "African/Indigenous",
    "Baha'i": "Other", "Zoroastrianism": "Other",
}

# Theological content keywords (signals genuine religious content vs demographic)
THEOLOGICAL_KEYWORDS = [
    "theological", "theology", "scripture", "scriptural", "doctrine", "doctrinal",
    "jurisprudence", "fiqh", "exegesis", "hermeneutic", "homiletic", "catechism",
    "liturgy", "liturgical", "soteriology", "eschatology", "christology",
    "quran", "qur'an", "quranic", "hadith", "sunnah", "fatwa", "sharia",
    "bible", "biblical", "gospel", "torah", "talmud", "midrash", "halakha",
    "vedic", "veda", "upanishad", "bhagavad", "gita", "dharma", "sutra",
    "pali", "tripitaka", "abhidharma", "vinaya",
    "guru granth", "gurbani", "japji",
    "analects", "confucian", "mencius", "tao te ching", "daodejing",
    "spiritual values", "religious knowledge", "faith benchmark",
    "moral reasoning", "ethical reasoning", "values alignment",
    "religious bias", "interfaith", "inter-faith",
]

# ---------------------------------------------------------------------------
# Field extraction (standard vault pattern, handles escaped quotes)
# ---------------------------------------------------------------------------
def extract_field(text: str, name: str) -> str:
    """Extract a YAML field value from frontmatter text."""
    m = re.search(rf"^{re.escape(name)}:\s*(.*)$", text, re.MULTILINE)
    if not m:
        return ""
    val = m.group(1).strip().strip('"').strip("'")
    if val.startswith("[[") and val.endswith("]]"):
        val = val[2:-2]
    return val.strip()


def extract_int_field(text: str, name: str) -> int:
    """Extract an integer YAML field, defaulting to 0."""
    raw = extract_field(text, name)
    try:
        return int(raw)
    except (ValueError, TypeError):
        return 0


def get_frontmatter(content: str) -> str:
    """Extract YAML frontmatter block from markdown content."""
    if not content.startswith("---"):
        return ""
    match = re.search(r'\n---\s*\n', content[3:])
    if match:
        return content[3:match.start() + 3]
    return ""


# ---------------------------------------------------------------------------
# Classification logic
# ---------------------------------------------------------------------------
def classify_candidate(fm: str, abstract: str, filename: str) -> dict | None:
    """
    Classify a paper as a religious values benchmark candidate.
    Returns a dict with metadata if it qualifies, else None.
    """
    # --- Gate 1: Must be benchmark/eval/dataset ---
    is_benchmark = extract_field(fm, "is_benchmark").lower().strip()
    is_eval = extract_field(fm, "is_eval").lower().strip()
    is_dataset = extract_field(fm, "is_dataset").lower().strip()

    if is_benchmark != "yes" and is_eval != "yes" and is_dataset != "yes":
        return None

    # --- Gate 2: Must have religious values content ---
    rv_scores = {}
    max_rv = 0
    for field in RV_FIELDS:
        score = extract_int_field(fm, field)
        rv_scores[field] = score
        max_rv = max(max_rv, score)

    nw_scores = {}
    max_nw = 0
    for field in NW_FIELDS:
        score = extract_int_field(fm, field)
        nw_scores[field] = score
        max_nw = max(max_nw, score)

    if max_rv < 50 and max_nw < 50:
        return None

    # --- Theological vs Demographic filter ---
    ethics_perspective = extract_field(fm, "ethics_perspective").lower()
    abstract_lower = (abstract or "").lower()
    title = extract_field(fm, "short_title").lower()
    combined_text = f"{title} {abstract_lower}"

    # Count theological keywords
    theo_hits = sum(1 for kw in THEOLOGICAL_KEYWORDS if kw in combined_text)

    # Classification
    if ethics_perspective in ("bias & fairness", "bias and fairness"):
        if max_rv < 80 and max_nw < 50 and theo_hits < 2:
            classification = "demographic-only"
        else:
            classification = "theological-values"
    elif theo_hits >= 2:
        classification = "theological"
    elif max_rv >= 80 or max_nw >= 80:
        classification = "theological-values"
    else:
        classification = "values"

    # --- Build traditions list ---
    traditions = []
    for field in RV_FIELDS:
        if rv_scores[field] >= 50:
            label = TRADITION_LABELS[field]
            traditions.append({"tradition": label, "score": rv_scores[field],
                               "family": TRADITION_FAMILY.get(label, "Other")})

    primary_tradition = traditions[0]["tradition"] if traditions else "Unknown"
    primary_family = traditions[0]["family"] if traditions else "Unknown"

    # --- Extract metadata ---
    short_title = extract_field(fm, "short_title")
    year = extract_field(fm, "year")
    data_url = extract_field(fm, "DATA_URL")
    llm_assessed = extract_field(fm, "LLM_assessed")
    data_description = extract_field(fm, "data_description")
    data_metrics = extract_field(fm, "data_metrics")
    religious_values = extract_field(fm, "religious_values")
    religious_values_list = extract_field(fm, "religious_values_list")
    first_author = extract_field(fm, "first_author")
    key = extract_field(fm, "key")
    url = extract_field(fm, "url")
    publication = extract_field(fm, "publication")
    languages = extract_field(fm, "languages_list")
    author_country = extract_field(fm, "author_country")
    author_region = extract_field(fm, "author_region")
    ethics_overall = extract_int_field(fm, "ethics_overall")
    citation_count = extract_field(fm, "citation_count")  # may not exist
    s2_paper_id = extract_field(fm, "s2_paper_id")

    return {
        "filename": filename,
        "key": key,
        "short_title": short_title,
        "year": year,
        "first_author": first_author,
        "url": url,
        "publication": publication,
        "is_benchmark": is_benchmark == "yes",
        "is_eval": is_eval == "yes",
        "is_dataset": is_dataset == "yes",
        "classification": classification,
        "primary_tradition": primary_tradition,
        "primary_family": primary_family,
        "traditions": traditions,
        "tradition_count": len(traditions),
        "rv_scores": rv_scores,
        "nw_scores": nw_scores,
        "max_rv": max_rv,
        "max_nw": max_nw,
        "theological_keyword_hits": theo_hits,
        "DATA_URL": data_url,
        "data_description": data_description,
        "data_metrics": data_metrics,
        "LLM_assessed": llm_assessed,
        "religious_values": religious_values,
        "religious_values_list": religious_values_list,
        "languages_list": languages,
        "author_country": author_country,
        "author_region": author_region,
        "ethics_overall": ethics_overall,
        "s2_paper_id": s2_paper_id,
        "abstract": (abstract or "")[:500],  # truncate for JSON size
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"=== Phase 1: Religious Values Benchmark Candidate Identification ===")
    print(f"Scanning: {PAPERS_DIR}")
    print()

    paper_files = sorted(PAPERS_DIR.iterdir())
    paper_files = [f for f in paper_files if f.suffix == ".md"]
    print(f"Total papers: {len(paper_files)}")

    candidates = []
    demographic_only = []
    skipped = 0

    for pf in paper_files:
        try:
            content = pf.read_text(encoding="utf-8")
        except Exception:
            skipped += 1
            continue

        fm = get_frontmatter(content)
        if not fm:
            skipped += 1
            continue

        abstract = extract_field(fm, "abstract")
        result = classify_candidate(fm, abstract, pf.name)

        if result is None:
            continue

        if result["classification"] == "demographic-only":
            demographic_only.append(result)
        else:
            candidates.append(result)

    # Sort by max_rv descending, then by theological keyword hits
    candidates.sort(key=lambda x: (-x["max_rv"], -x["theological_keyword_hits"], x["filename"]))
    demographic_only.sort(key=lambda x: (-x["max_rv"], x["filename"]))

    # --- Statistics ---
    print(f"\n{'='*60}")
    print(f"RESULTS")
    print(f"{'='*60}")
    print(f"Primary candidates (theological + values): {len(candidates)}")
    print(f"Demographic-only (excluded from primary):  {len(demographic_only)}")
    print(f"Skipped (no frontmatter):                  {skipped}")

    # Tradition distribution
    print(f"\n--- Tradition Distribution (Primary Candidates) ---")
    tradition_counts = {}
    for c in candidates:
        for t in c["traditions"]:
            trad = t["tradition"]
            tradition_counts[trad] = tradition_counts.get(trad, 0) + 1
    for trad, count in sorted(tradition_counts.items(), key=lambda x: -x[1]):
        family = TRADITION_FAMILY.get(trad, "Other")
        print(f"  {trad:30s} [{family:20s}] {count:3d}")

    # Family distribution
    print(f"\n--- Family Distribution ---")
    family_counts = {}
    for c in candidates:
        fam = c["primary_family"]
        family_counts[fam] = family_counts.get(fam, 0) + 1
    for fam, count in sorted(family_counts.items(), key=lambda x: -x[1]):
        print(f"  {fam:25s} {count:3d}")

    # Classification distribution
    print(f"\n--- Classification Distribution ---")
    class_counts = {}
    for c in candidates:
        cl = c["classification"]
        class_counts[cl] = class_counts.get(cl, 0) + 1
    for cl, count in sorted(class_counts.items(), key=lambda x: -x[1]):
        print(f"  {cl:25s} {count:3d}")

    # Format stats
    has_data_url = sum(1 for c in candidates if c["DATA_URL"] and c["DATA_URL"].lower() not in ("na", "n/a", ""))
    has_benchmark = sum(1 for c in candidates if c["is_benchmark"])
    has_eval = sum(1 for c in candidates if c["is_eval"])
    has_dataset = sum(1 for c in candidates if c["is_dataset"])

    print(f"\n--- Data Availability ---")
    print(f"  With DATA_URL:  {has_data_url}")
    print(f"  is_benchmark:   {has_benchmark}")
    print(f"  is_eval:        {has_eval}")
    print(f"  is_dataset:     {has_dataset}")

    # Year distribution
    print(f"\n--- Year Distribution ---")
    year_counts = {}
    for c in candidates:
        yr = c["year"][:4] if c["year"] else "Unknown"
        year_counts[yr] = year_counts.get(yr, 0) + 1
    for yr, count in sorted(year_counts.items()):
        print(f"  {yr}: {count}")

    # Top candidates
    print(f"\n--- Top 20 Candidates (by rv score + theological depth) ---")
    for i, c in enumerate(candidates[:20], 1):
        trads = ", ".join(t["tradition"] for t in c["traditions"][:3])
        data_flag = "DATA" if (c["DATA_URL"] and c["DATA_URL"].lower() not in ("na", "n/a", "")) else "----"
        bm_flag = "BM" if c["is_benchmark"] else "  "
        ev_flag = "EV" if c["is_eval"] else "  "
        ds_flag = "DS" if c["is_dataset"] else "  "
        print(f"  {i:2d}. [{c['classification'][:5]:5s}] {bm_flag} {ev_flag} {ds_flag} [{data_flag}] "
              f"rv={c['max_rv']:3d} theo={c['theological_keyword_hits']:2d} "
              f"{c['year'][:4]} {c['short_title'][:55]:55s} | {trads}")

    # --- Write output ---
    output = {
        "generated": TODAY,
        "scope": "theological+values",
        "total_papers_scanned": len(paper_files),
        "primary_candidate_count": len(candidates),
        "demographic_only_count": len(demographic_only),
        "tradition_distribution": tradition_counts,
        "family_distribution": family_counts,
        "candidates": candidates,
        "demographic_only": demographic_only,
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DATA_DIR / f"{TODAY}-religious-benchmark-candidates.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nOutput: {out_path}")
    print(f"Done.")


if __name__ == "__main__":
    main()
