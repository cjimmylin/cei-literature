#!/usr/bin/env python3
"""
Ingest External Discoveries into CEI Literature Vault

Reads Phase 2 external search results, filters for quality and relevance,
deduplicates against existing vault papers, and creates paper stubs with
YAML frontmatter.

Quality filters:
  - Must have title + abstract
  - Title must contain at least one religious/benchmark keyword
  - Removes known false positives (physics experiments, medical studies, etc.)
  - Checks for vault duplicates via normalized title matching

Output: New .md files in papers/ directory
        RELIGIOUS-VALUES/data/YYYYMMDD-ingest-report.json

Naming convention: papers/YYYY-Author-Short Title.md
Key convention: EXSR0623+ (next available after current max)
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
WS_ROOT = PROJECT_DIR.parent
PAPERS_DIR = WS_ROOT / "papers"
DATA_DIR = PROJECT_DIR / "data"

TODAY = date.today().strftime("%Y%m%d")

# ---------------------------------------------------------------------------
# Quality filter keywords
# ---------------------------------------------------------------------------
RELIGIOUS_MUST_HAVE = {
    "religion", "religious", "theology", "theological", "faith", "spiritual",
    "scripture", "scriptural", "sacred", "divine",
    "quran", "quranic", "bible", "biblical", "torah", "talmud", "hadith",
    "fatwa", "fiqh", "sharia", "islamic", "muslim",
    "christian", "church", "gospel",
    "jewish", "judaism", "hebrew",
    "hindu", "vedic", "vedanta", "dharma", "gita", "bhagavad",
    "buddhist", "buddhism", "pali", "zen", "sutra",
    "sikh", "gurbani", "guru granth",
    "confucian", "analects", "cvalues",
    "taoist", "taoism", "tao te ching",
    "shinto",
    "jain", "jainism", "ahimsa",
    "ubuntu", "african philosophy",
    "indigenous", "aboriginal", "maori", "decolonial",
    "interfaith", "inter-faith",
    "moral values", "ethical values", "values alignment",
    "religious bias", "hate speech",
    "sattvic", "karma", "reincarnation",
    "prayer", "mosque", "temple", "synagogue",
    "imam", "rabbi", "priest", "monk",
}

# Known false-positive patterns to reject
FP_PATTERNS = [
    r"TAO\s+Conceptual\s+Design",  # physics experiment
    r"CUAD.*Contract\s+Review",     # legal contract dataset
    r"diabetes.*free.text",         # medical study
    r"anorexia.*detection",         # medical study
    r"anorexic.*girls.*blog",        # medical study in Hebrew
    r"infertility.*evaluation.*jewish\s+law",  # old medical
    r"backdoor.*explainable.*benchmark",  # unrelated security benchmark
    r"AEGIS.*video",               # video generation benchmark
    r"ridge.*random\s+forest.*metric.*MT",  # MT metric, not religious
    r"VLM.*school.*German",        # German education, not religious
    r"workplace\s+spirituality.*predicting",  # HR study
    r"LiveBench.*contamination",   # general LLM benchmark
]


def is_relevant(title: str, abstract: str) -> bool:
    """Check if paper is genuinely about religious values + benchmarks."""
    text = f"{title} {abstract}".lower()

    # Check for false positive patterns
    for pattern in FP_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return False

    # Must have at least one religious keyword
    has_religious = any(kw in text for kw in RELIGIOUS_MUST_HAVE)
    return has_religious


# ---------------------------------------------------------------------------
# Dedup against vault
# ---------------------------------------------------------------------------
def load_vault_titles() -> dict[str, str]:
    """Load normalized vault titles → filename mapping."""
    titles = {}
    for pf in PAPERS_DIR.iterdir():
        if pf.suffix != ".md":
            continue
        try:
            content = pf.read_text(encoding="utf-8")[:3000]
            m = re.search(r'^short_title:\s*"?(.*?)"?\s*$', content, re.MULTILINE)
            if m:
                norm = re.sub(r'[^a-z0-9\s]', '', m.group(1).lower()).strip()[:80]
                titles[norm] = pf.name
        except Exception:
            pass
    return titles


def normalize_title(title: str) -> str:
    return re.sub(r'[^a-z0-9\s]', '', title.lower()).strip()[:80]


# ---------------------------------------------------------------------------
# Key allocation
# ---------------------------------------------------------------------------
def find_next_exsr_key() -> int:
    """Find the next available EXSR key number."""
    max_key = 0
    for pf in PAPERS_DIR.iterdir():
        if pf.suffix != ".md":
            continue
        try:
            content = pf.read_text(encoding="utf-8")[:2000]
            m = re.search(r'^key:\s*EXSR(\d+)', content, re.MULTILINE)
            if m:
                max_key = max(max_key, int(m.group(1)))
        except Exception:
            pass
    return max_key + 1


# ---------------------------------------------------------------------------
# Filename generation
# ---------------------------------------------------------------------------
def make_filename(year: str, first_author: str, title: str) -> str:
    """Generate vault filename: YYYY-Author-Short Title.md"""
    yr = year[:4] if year else "0000"

    # Clean author name
    author = first_author.split(",")[0].split(" ")[-1] if first_author else "Unknown"
    author = re.sub(r'[^\w\s-]', '', author).strip()[:20]
    if not author:
        author = "Unknown"

    # Clean title: take first ~6 significant words
    title_words = re.sub(r'[^\w\s]', '', title).strip().split()
    # Skip common leading words
    skip = {"a", "an", "the", "on", "of", "for", "in", "to", "and", "with"}
    significant = [w for w in title_words if w.lower() not in skip][:6]
    if not significant:
        significant = title_words[:6]
    short_title = " ".join(significant)

    filename = f"{yr}-{author}-{short_title}.md"
    # Sanitize
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    return filename


# ---------------------------------------------------------------------------
# Paper stub generation (YAML frontmatter)
# ---------------------------------------------------------------------------
def generate_paper_stub(result: dict, key_num: int) -> str:
    """Generate a complete paper stub with YAML frontmatter."""
    title = result.get("title", "Unknown Title")
    year = result.get("year", "")[:4] if result.get("year") else ""
    abstract = result.get("abstract", "")
    url = result.get("url", "")
    authors_list = result.get("authors", [])
    venue = result.get("venue", "")
    tradition = result.get("tradition", "")
    family = result.get("family", "")
    s2_id = result.get("s2_paper_id", "")
    citations = result.get("citations", 0)
    source = result.get("source", "")

    # Format authors
    first_author = authors_list[0] if authors_list else "Unknown"
    last_author = authors_list[-1] if len(authors_list) > 1 else first_author
    authors_str = "; ".join(authors_list) if authors_list else "Unknown"

    # Determine type
    if "arxiv" in (url or "").lower() or "arxiv" in (venue or "").lower():
        pub_type = "preprint"
        conf_cc = "Preprint"
    elif venue:
        pub_type = "conferencePaper"
        conf_cc = "N/A"
    else:
        pub_type = "preprint"
        conf_cc = "Preprint"

    # Escape quotes in abstract
    abstract_safe = abstract.replace('"', '\\"') if abstract else ""

    key = f"EXSR{key_num:04d}"

    # Build YAML — using the exact format from existing EXSR papers
    # (includes blank lines at top for Obsidian compatibility)
    stub = f"""---
Human View:
Human View Date:
Human View note:
Not AI:
key: {key}
type: {pub_type}
short_title: "{title[:120]}"
year: {year}
first_author: "[[{first_author}]]"
last_author: "[[{last_author}]]"
authors: "{authors_str}"
authors_incomplete: true
url: "{url}"
external_pdf:
pdf_extract:
local_pdf: N/A
publication: "{venue or source}"
CONF-CC: "{conf_cc}"
DATE_ADDED: {TODAY}
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "{tradition}"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "{tradition}"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags:
tags:
abstract: "{abstract_safe[:500]}"
LLM_assessed: "NA"
DATA_URL: "NA"
CONFERENCE: "{conf_cc}"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
is_benchmark: "Unknown"
is_eval: "Unknown"
is_dataset: "Unknown"
data_description: ""
data_metrics: "Not specified"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
s2_paper_id: "{s2_id}"
citation_count: {citations}
---
# {title}

## Authors

{', '.join(f'[[{a}]]' for a in authors_list) if authors_list else '[[Unknown]]'}

## Metadata

**Authors:** {authors_str}

**Year:** {year}

**Type:** {pub_type}

**Venue:** {venue or source}

## Links

- **URL:** {url}

## Abstract

{abstract[:500]}

## Notes

**Source:** Religious Values External Search ({TODAY})
**Tradition:** {tradition} ({family})
**Implementation Readiness:** NEEDS ASSESSMENT
"""
    return stub


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    dry_run = "--dry-run" in sys.argv

    print(f"=== Ingest External Discoveries into CEI Literature Vault ===")
    print(f"Dry run: {dry_run}")

    # Load external results
    ext_files = sorted(DATA_DIR.glob("*-external-search-results.json"))
    if not ext_files:
        print("ERROR: No external search results found.")
        sys.exit(1)

    with open(ext_files[-1]) as f:
        ext_data = json.load(f)

    results = ext_data["results"]
    print(f"External results: {len(results)}")

    # Load vault titles for dedup
    vault_titles = load_vault_titles()
    print(f"Vault titles loaded: {len(vault_titles)}")

    # Find next key
    next_key = find_next_exsr_key()
    print(f"Next EXSR key: EXSR{next_key:04d}")

    # Process each result
    ingested = []
    skipped_dup = []
    skipped_quality = []
    skipped_no_title = []

    for result in results:
        title = result.get("title", "").strip()
        if not title or len(title) < 10:
            skipped_no_title.append(result)
            continue

        # Dedup check
        norm = normalize_title(title)
        if norm in vault_titles:
            skipped_dup.append({"title": title, "existing": vault_titles[norm]})
            continue

        # Quality filter
        abstract = result.get("abstract", "") or ""
        if not is_relevant(title, abstract):
            skipped_quality.append({"title": title, "reason": "Failed relevance filter"})
            continue

        # Generate filename
        year = result.get("year", "")[:4] if result.get("year") else "0000"
        authors = result.get("authors", [])
        first_author = authors[0] if authors else "Unknown"
        filename = make_filename(year, first_author, title)

        # Check filename collision
        target_path = PAPERS_DIR / filename
        if target_path.exists():
            # Add key suffix to avoid collision
            filename = filename.replace(".md", f"-{next_key}.md")
            target_path = PAPERS_DIR / filename

        # Generate stub
        stub = generate_paper_stub(result, next_key)

        if dry_run:
            print(f"  [DRY] Would create: {filename} (EXSR{next_key:04d}) — {title[:60]}")
        else:
            target_path.write_text(stub, encoding="utf-8")
            print(f"  Created: {filename} (EXSR{next_key:04d})")

        ingested.append({
            "filename": filename,
            "key": f"EXSR{next_key:04d}",
            "title": title,
            "year": year,
            "tradition": result.get("tradition", ""),
            "family": result.get("family", ""),
            "source": result.get("source", ""),
        })

        # Update for next iteration
        vault_titles[norm] = filename
        next_key += 1

    # Summary
    print(f"\n{'='*60}")
    print(f"INGEST SUMMARY")
    print(f"{'='*60}")
    print(f"Total external results:     {len(results)}")
    print(f"Ingested (new papers):      {len(ingested)}")
    print(f"Skipped (duplicates):       {len(skipped_dup)}")
    print(f"Skipped (quality filter):   {len(skipped_quality)}")
    print(f"Skipped (no title):         {len(skipped_no_title)}")

    # By tradition
    print(f"\n--- Ingested by Tradition ---")
    trad_counts = {}
    for r in ingested:
        trad = r["tradition"]
        trad_counts[trad] = trad_counts.get(trad, 0) + 1
    for trad, count in sorted(trad_counts.items(), key=lambda x: -x[1]):
        print(f"  {trad:25s} {count}")

    # Quality-filtered details
    if skipped_quality:
        print(f"\n--- Skipped by Quality Filter ---")
        for s in skipped_quality[:10]:
            print(f"  {s['title'][:70]}")

    # Save ingest report
    report = {
        "generated": TODAY,
        "total_processed": len(results),
        "ingested_count": len(ingested),
        "skipped_duplicate": len(skipped_dup),
        "skipped_quality": len(skipped_quality),
        "skipped_no_title": len(skipped_no_title),
        "tradition_distribution": trad_counts,
        "ingested": ingested,
        "skipped_quality_details": skipped_quality,
        "skipped_duplicate_details": skipped_dup,
    }

    report_path = DATA_DIR / f"{TODAY}-ingest-report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nIngest report: {report_path}")

    if not dry_run and ingested:
        print(f"\n*** NEXT STEPS ***")
        print(f"1. Run classification pipeline on new papers:")
        print(f"   ../.venv/bin/python PYTHON/classify_ethics.py")
        print(f"2. Run religious scoring:")
        print(f"   ../.venv/bin/python PYTHON/religious_scoring.py")
        print(f"3. Validate:")
        print(f"   ../.venv/bin/python PYTHON/validate_all_papers.py")
        print(f"4. Re-run religious values pipeline:")
        print(f"   ../.venv/bin/python RELIGIOUS-VALUES/scripts/identify_religious_benchmarks.py")


if __name__ == "__main__":
    main()
