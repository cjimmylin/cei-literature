#!/usr/bin/env python3
"""
Ingest Moral Psychology External Search Discoveries into CEI Literature Vault

Reads the merged external search results, filters for classification ==
"not_in_vault_relevant" (14 papers), deduplicates against existing vault
papers, and creates paper stubs with YAML frontmatter.

Output: New .md files in papers/ directory
        MORAL-PSYCH/20260404-phase2a-ingestion-report.json

Naming convention: papers/YYYY-Author-Short Title.md
Key convention: EXSR0676+ (next available after current max)
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
SOURCE_JSON = PROJECT_DIR / "20260403-external-search-merged.json"

TODAY = "20260404"
DATE_ADDED = 20260404


# ---------------------------------------------------------------------------
# Dedup against vault
# ---------------------------------------------------------------------------
def load_vault_titles() -> dict[str, str]:
    """Load normalized vault titles -> filename mapping."""
    titles: dict[str, str] = {}
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
# Author parsing
# ---------------------------------------------------------------------------
def parse_authors(authors_str: str) -> tuple[str, str, str]:
    """
    Parse author string into (first_author, last_author, authors_formatted).

    Examples:
      "Feffer et al." -> ("Feffer", "Feffer", "Feffer et al.")
      "Marraffini, Cotton, Hsueh, Fridman, Wisznia, del Corro"
          -> ("Marraffini", "del Corro", "Marraffini; Cotton; Hsueh; ...")
      "Cheung et al. (UCL, UCLA)" -> ("Cheung", "Cheung", "Cheung et al.")
      "Unknown (arXiv:2603.16017)" -> ("Unknown", "Unknown", "Unknown")
      "Max Planck Institute" -> ("Max Planck Institute", "Max Planck Institute", "Max Planck Institute")
      "Gabriel et al. (Google DeepMind)" -> ("Gabriel", "Gabriel", "Gabriel et al.")
    """
    if not authors_str or authors_str.strip() == "Unknown":
        return ("Unknown", "Unknown", "Unknown")

    # Strip parenthetical affiliations: "Cheung et al. (UCL, UCLA)" -> "Cheung et al."
    cleaned = re.sub(r'\s*\(.*?\)\s*', '', authors_str).strip()

    # Handle "et al." pattern
    et_al_m = re.match(r'^(\w[\w\s]*?)\s+et\s+al\.?$', cleaned)
    if et_al_m:
        first = et_al_m.group(1).strip()
        return (first, first, f"{first} et al.")

    # Handle institutional author (no comma-separated list pattern)
    # e.g. "Max Planck Institute"
    if cleaned.startswith("Unknown"):
        return ("Unknown", "Unknown", "Unknown")

    # Handle comma-separated list: "Marraffini, Cotton, Hsueh, Fridman, Wisznia, del Corro"
    # Also handles: "Chakraborty, Wang, Jurgens"
    # Also handles: "Gothard, Davies"
    parts = [p.strip() for p in cleaned.split(",") if p.strip()]
    if len(parts) > 1:
        first_author = parts[0]
        last_author = parts[-1]
        authors_formatted = "; ".join(parts)
        return (first_author, last_author, authors_formatted)

    # Single name
    return (cleaned, cleaned, cleaned)


def extract_first_surname(author_name: str) -> str:
    """Extract surname for filename generation.
    'Marraffini' -> 'Marraffini'
    'del Corro' -> 'del Corro'
    'Max Planck Institute' -> 'Institute'
    """
    if not author_name or author_name == "Unknown":
        return "Unknown"
    # Use last word as surname unless it's a known prefix
    parts = author_name.strip().split()
    return parts[-1] if parts else "Unknown"


# ---------------------------------------------------------------------------
# Filename generation
# ---------------------------------------------------------------------------
def make_filename(year: int | str, first_author: str, title: str) -> str:
    """Generate vault filename: YYYY-Author-Short Title.md"""
    yr = str(year)[:4] if year else "0000"

    # Clean author name -> surname
    surname = extract_first_surname(first_author)
    surname = re.sub(r'[^\w\s-]', '', surname).strip()[:20]
    if not surname:
        surname = "Unknown"

    # Clean title: take first ~6 significant words
    title_words = re.sub(r'[^\w\s]', '', title).strip().split()
    skip = {"a", "an", "the", "on", "of", "for", "in", "to", "and", "with"}
    significant = [w for w in title_words if w.lower() not in skip][:6]
    if not significant:
        significant = title_words[:6]
    short_title = " ".join(significant)

    filename = f"{yr}-{surname}-{short_title}.md"
    # Sanitize
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    return filename


# ---------------------------------------------------------------------------
# Paper stub generation (YAML frontmatter)
# ---------------------------------------------------------------------------
def generate_paper_stub(result: dict, key_num: int,
                        first_author: str, last_author: str,
                        authors_formatted: str) -> str:
    """Generate a complete paper stub with YAML frontmatter."""
    title = result.get("title", "Unknown Title")
    year = result.get("year", "")
    year_str = str(year)[:4] if year else ""
    abstract = result.get("abstract_snippet", "")
    url = result.get("doi_or_url", "")
    venue = result.get("venue", "")
    target_theory = result.get("target_theory", "")
    relevance_notes = result.get("relevance_notes", "")

    # Determine type
    url_lower = (url or "").lower()
    venue_lower = (venue or "").lower()
    if "arxiv" in url_lower or "arxiv" in venue_lower:
        pub_type = "preprint"
        conf_cc = "Preprint"
    elif venue:
        pub_type = "conferencePaper"
        conf_cc = "N/A"
    else:
        pub_type = "preprint"
        conf_cc = "Preprint"

    # Escape quotes in strings for YAML
    abstract_safe = abstract.replace('"', '\\"') if abstract else ""
    title_safe = title.replace('"', '\\"')
    venue_safe = venue.replace('"', '\\"') if venue else ""
    relevance_safe = relevance_notes.replace('"', '\\"') if relevance_notes else ""
    authors_safe = authors_formatted.replace('"', '\\"')

    key = f"EXSR{key_num:04d}"

    # Moral psychology field: set to target_theory if available
    moral_psych_val = target_theory if target_theory else "N/A"

    # newtags as comma-separated string
    newtags = "moral-psychology, benchmark, external-search"

    # Build author wikilinks for body
    author_parts = [a.strip() for a in authors_formatted.split(";")]
    author_wikilinks = ", ".join(f"[[{a}]]" for a in author_parts if a and a != "Unknown")
    if not author_wikilinks:
        author_wikilinks = "[[Unknown]]"

    stub = f"""---

Human View:
Human View Date:
Human View note:
Not AI:
key: {key}
type: {pub_type}
short_title: "{title_safe[:120]}"
year: {year_str}
first_author: "[[{first_author}]]"
last_author: "[[{last_author}]]"
authors: "{authors_safe}"
authors_incomplete: true
url: "{url or ''}"
external_pdf:
pdf_extract:
local_pdf: N/A
publication: "{venue_safe}"
CONF-CC: "{conf_cc}"
DATE_ADDED: {DATE_ADDED}
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: ""
religious_values: "N/A"
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
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "{moral_psych_val}"
newtags: "{newtags}"
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
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
s2_paper_id: ""
citation_count: 0
is_benchmark: "Unknown"
is_eval: "Unknown"
is_dataset: "Unknown"
data_description: ""
data_metrics: "Not specified"
---
# {title}

## Authors

{author_wikilinks}

## Metadata

**Authors:** {authors_formatted}

**Year:** {year_str}

**Type:** {pub_type}

**Venue:** {venue}

## Links

- **URL:** {url}

## Abstract

{abstract[:500]}

## Notes

**Source:** Moral Psychology External Search ({TODAY})
**Target Theory:** {target_theory}
**Relevance:** {relevance_notes}
"""
    return stub


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    dry_run = "--dry-run" in sys.argv

    print("=== Ingest Moral Psychology Discoveries into CEI Literature Vault ===")
    print(f"Dry run: {dry_run}")

    # Load source JSON
    if not SOURCE_JSON.exists():
        print(f"ERROR: Source file not found: {SOURCE_JSON}")
        sys.exit(1)

    with open(SOURCE_JSON, encoding="utf-8") as f:
        data = json.load(f)

    all_results = data["results"]
    # Filter for not_in_vault_relevant only
    results = [r for r in all_results if r.get("classification") == "not_in_vault_relevant"]
    print(f"Total results: {len(all_results)}")
    print(f"Filtered (not_in_vault_relevant): {len(results)}")

    # Load vault titles for dedup
    vault_titles = load_vault_titles()
    print(f"Vault titles loaded: {len(vault_titles)}")

    # Find next key
    next_key = find_next_exsr_key()
    print(f"Next EXSR key: EXSR{next_key:04d}")

    # Process each result
    ingested = []
    skipped_dup = []
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

        # Parse authors
        authors_raw = result.get("authors", "Unknown")
        first_author, last_author, authors_formatted = parse_authors(authors_raw)

        # Generate filename
        year = result.get("year", "")
        filename = make_filename(year, first_author, title)

        # Check filename collision
        target_path = PAPERS_DIR / filename
        if target_path.exists():
            filename = filename.replace(".md", f"-{next_key}.md")
            target_path = PAPERS_DIR / filename

        # Generate stub
        stub = generate_paper_stub(
            result, next_key,
            first_author, last_author, authors_formatted,
        )

        if dry_run:
            print(f"  [DRY] Would create: {filename} (EXSR{next_key:04d}) -- {title[:60]}")
        else:
            target_path.write_text(stub, encoding="utf-8")
            print(f"  Created: {filename} (EXSR{next_key:04d})")

        ingested.append({
            "filename": filename,
            "key": f"EXSR{next_key:04d}",
            "title": title,
            "year": str(year)[:4] if year else "",
            "target_theory": result.get("target_theory", ""),
            "authors": authors_formatted,
        })

        # Update for next iteration
        vault_titles[norm] = filename
        next_key += 1

    # Summary
    print(f"\n{'='*60}")
    print("INGEST SUMMARY")
    print(f"{'='*60}")
    print(f"Total filtered results:     {len(results)}")
    print(f"Ingested (new papers):      {len(ingested)}")
    print(f"Skipped (duplicates):       {len(skipped_dup)}")
    print(f"Skipped (no title):         {len(skipped_no_title)}")

    # By target theory
    print("\n--- Ingested by Target Theory ---")
    theory_counts: dict[str, int] = {}
    for r in ingested:
        theory = r["target_theory"]
        theory_counts[theory] = theory_counts.get(theory, 0) + 1
    for theory, count in sorted(theory_counts.items(), key=lambda x: -x[1]):
        print(f"  {theory:25s} {count}")

    # Save ingest report
    report = {
        "generated": TODAY,
        "source_file": str(SOURCE_JSON.name),
        "total_in_source": len(all_results),
        "filtered_relevant": len(results),
        "ingested_count": len(ingested),
        "skipped_duplicate": len(skipped_dup),
        "skipped_no_title": len(skipped_no_title),
        "theory_distribution": theory_counts,
        "ingested": ingested,
        "skipped_duplicate_details": skipped_dup,
    }

    report_path = PROJECT_DIR / f"{TODAY}-phase2a-ingestion-report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nIngest report: {report_path}")

    if not dry_run and ingested:
        print("\n*** NEXT STEPS ***")
        print("1. Run moral psych scoring:")
        print("   ../.venv/bin/python PYTHON/classify_moral_psych.py")
        print("2. Run classification pipeline:")
        print("   ../.venv/bin/python PYTHON/classify_ethics.py")
        print("3. Validate:")
        print("   ../.venv/bin/python PYTHON/validate_all_papers.py")


if __name__ == "__main__":
    main()
