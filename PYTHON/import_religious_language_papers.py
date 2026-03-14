#!/usr/bin/env python3
"""
Import Religious & Language Search Papers into the Vault

Creates paper markdown files from the consolidated master list.
Each file follows the exact YAML field order and body template of
existing vault papers.

Inputs:
  - logs/20260213-religious_language_master_list.json

Outputs:
  - papers/{year}-{author}-{short_title}.md (one per approved candidate)
  - logs/20260213-import_log.json (audit trail)

Usage:
    python import_religious_language_papers.py [--dry-run]
"""

import functools
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Optional

# Force flush
print = functools.partial(print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
WORKSPACE_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(WORKSPACE_ROOT / ".agent"))

from lib.yaml_utils import validate_frontmatter

PAPERS_DIR = WORKSPACE_ROOT / "papers"
LOGS_DIR = WORKSPACE_ROOT / "logs"

DATE_ADDED = "20260213"
EXSR_START = 301  # Next available after EXSR0300


# ============================================================
# Name Processing
# ============================================================

def normalize_for_filename(text: str) -> str:
    """Strip diacritics and non-ASCII for safe filenames."""
    # Decompose Unicode, strip combining marks
    nfkd = unicodedata.normalize("NFKD", text)
    ascii_text = "".join(c for c in nfkd if not unicodedata.combining(c))
    # Keep only word chars, spaces, hyphens
    ascii_text = re.sub(r'[^\w\s-]', '', ascii_text)
    return ascii_text.strip()


def extract_first_author_lastname(authors_str: str) -> str:
    """Extract first author's last name from various author string formats."""
    if not authors_str or authors_str.lower() in ("unknown", ""):
        return "Unknown"

    # Clean up any wikilink markup
    authors_str = authors_str.replace("[[", "").replace("]]", "")

    # Get first author (split on ; or ,)
    first = authors_str.split(";")[0].strip()
    if "," in first and not re.search(r',\s*[A-Z][a-z]+\s', first):
        # "LastName, FirstName" format
        parts = first.split(",")
        return normalize_for_filename(parts[0].strip())
    else:
        # "FirstName LastName" format — take last word
        # Handle "and others", "et al." etc
        first = re.sub(r'\s+(and others|et al\.?)$', '', first, flags=re.IGNORECASE)
        parts = first.strip().split()
        if parts:
            return normalize_for_filename(parts[-1])
    return "Unknown"


def make_short_title(title: str, max_words: int = 6) -> str:
    """Create a short title slug for filenames."""
    # Remove benchmark/dataset names in parens at end for the slug
    clean = re.sub(r'\s*\([^)]+\)\s*$', '', title)
    # Remove special chars except spaces and hyphens
    clean = re.sub(r'[^\w\s-]', '', clean)
    words = clean.split()[:max_words]
    slug = " ".join(words)
    return slug.strip()


def make_filename(year: int, authors_str: str, title: str) -> str:
    """Create the paper filename: {year}-{LastName}-{ShortTitle}.md"""
    y = str(year) if year else "0000"
    lastname = extract_first_author_lastname(authors_str)
    short = make_short_title(title)
    filename = f"{y}-{lastname}-{short}.md"
    # Replace multiple spaces with single space
    filename = re.sub(r'\s+', ' ', filename)
    return filename


# ============================================================
# Author Formatting
# ============================================================

def format_authors_yaml(authors_str: str) -> str:
    """Format authors for YAML (wikilinked, semicolon-separated)."""
    if not authors_str or authors_str.lower() in ("unknown", ""):
        return '"[[Unknown]]"'

    # Clean up existing formatting
    authors_str = authors_str.replace("[[", "").replace("]]", "")
    # Split on semicolons or " and " or ", and "
    parts = re.split(r'\s*;\s*|\s+and\s+', authors_str)
    wikilinked = []
    for p in parts:
        p = p.strip().rstrip(".")
        if not p or p.lower() in ("others", "not fully extracted", "not fully extracted - multiple authors"):
            continue
        wikilinked.append(f"[[{p}]]")
    if not wikilinked:
        return '"[[Unknown]]"'
    return '"' + "; ".join(wikilinked) + '"'


def format_first_author(authors_str: str) -> str:
    """Format first author for YAML: '[[LastName, FirstName]]'."""
    if not authors_str or authors_str.lower() in ("unknown", ""):
        return '"[[Unknown]]"'

    authors_str = authors_str.replace("[[", "").replace("]]", "")
    first = authors_str.split(";")[0].strip().rstrip(".")

    # Handle "and others" etc
    first = re.sub(r'\s+(and others|et al\.?)$', '', first, flags=re.IGNORECASE)

    if not first or first.lower() in ("not fully extracted", "not fully extracted - multiple authors"):
        return '"[[Unknown]]"'

    # If already "LastName, FirstName" format, use as-is
    if "," in first:
        return f'"[[{first}]]"'

    # Convert "FirstName LastName" to "LastName, FirstName"
    parts = first.strip().split()
    if len(parts) >= 2:
        lastname = parts[-1]
        firstname = " ".join(parts[:-1])
        return f'"[[{lastname}, {firstname}]]"'
    return f'"[[{first}]]"'


def format_last_author(authors_str: str) -> str:
    """Format last author for YAML: '[[LastName, FirstName]]'."""
    if not authors_str or authors_str.lower() in ("unknown", ""):
        return '"[[Unknown]]"'

    authors_str = authors_str.replace("[[", "").replace("]]", "")
    # Split and get last real author
    parts = re.split(r'\s*;\s*', authors_str)
    # Filter out placeholders
    real_parts = [p.strip().rstrip(".") for p in parts
                  if p.strip() and p.strip().lower() not in
                  ("others", "not fully extracted", "not fully extracted - multiple authors", "and others")]
    if not real_parts:
        return '"[[Unknown]]"'

    last = real_parts[-1]
    last = re.sub(r'\s+(and others|et al\.?)$', '', last, flags=re.IGNORECASE).strip()

    if "," in last:
        return f'"[[{last}]]"'

    parts = last.strip().split()
    if len(parts) >= 2:
        lastname = parts[-1]
        firstname = " ".join(parts[:-1])
        return f'"[[{lastname}, {firstname}]]"'
    return f'"[[{last}]]"'


# ============================================================
# URL Helpers
# ============================================================

def make_external_pdf_url(entry: dict) -> str:
    """Derive external PDF URL from entry metadata."""
    arxiv_id = entry.get("arxiv_id", "")
    if arxiv_id:
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    url = entry.get("url", "")
    if url and url.endswith(".pdf"):
        return url
    # ACL anthology: add .pdf
    if "aclanthology.org" in url and not url.endswith(".pdf"):
        return url.rstrip("/") + ".pdf"
    return ""


def determine_type(entry: dict) -> str:
    """Determine paper type from venue info."""
    venue = (entry.get("venue", "") or "").lower()
    paper_type = (entry.get("paper_type", "") or "").lower()

    if "arxiv" in venue or "preprint" in venue:
        return "preprint"
    if any(w in venue for w in ("conference", "proceedings", "workshop", "acl", "emnlp",
                                 "naacl", "neurips", "icml", "aaai", "aies", "iclr",
                                 "chi", "facct", "fat*")):
        return "conference_paper"
    if any(w in venue for w in ("journal", "transactions", "review")):
        return "journal_article"
    if "arxiv" in (entry.get("url", "") or "").lower():
        return "preprint"
    return "preprint"


def determine_publication(entry: dict) -> str:
    """Determine publication venue string."""
    venue = entry.get("venue", "") or ""
    if not venue:
        if entry.get("arxiv_id"):
            return "arXiv"
        return ""
    # Clean up source prefixes from A-agents
    venue = re.sub(r'^(ACL Anthology / |arXiv / |Semantic Scholar|Google Scholar)\s*', '', venue)
    return venue.strip() or ("arXiv" if entry.get("arxiv_id") else "")


# ============================================================
# Paper File Builder
# ============================================================

def build_paper_file(entry: dict, exsr_num: int) -> tuple[str, list[str]]:
    """
    Build a complete paper markdown file.
    Returns (file_content, validation_issues).
    """
    title = entry.get("title", "Untitled")
    authors_raw = entry.get("authors", "")
    year = entry.get("year", 0)
    url = entry.get("url", "")
    arxiv_id = entry.get("arxiv_id", "")
    doi = entry.get("doi", "")
    description = entry.get("description", "")
    benchmark_name = entry.get("benchmark_name", "")
    code_data_url = entry.get("code_data_url", "")
    religious_traditions = entry.get("religious_traditions", "")

    # Sanitize title for YAML (escape quotes)
    safe_title = title.replace('"', "'")
    short_title = make_short_title(title)
    safe_short_title = short_title.replace('"', "'")

    # Format authors
    first_author = format_first_author(authors_raw)
    last_author = format_last_author(authors_raw)
    authors_yaml = format_authors_yaml(authors_raw)

    # Determine if authors are incomplete
    authors_incomplete = "false"
    if not authors_raw or "not fully extracted" in authors_raw.lower() or authors_raw.lower() in ("unknown", ""):
        authors_incomplete = "true"

    # External PDF
    external_pdf = make_external_pdf_url(entry)
    safe_external_pdf = external_pdf.replace('"', "'") if external_pdf else ""

    # Type and publication
    paper_type = determine_type(entry)
    publication = determine_publication(entry)

    # URL
    if not url and arxiv_id:
        url = f"https://arxiv.org/abs/{arxiv_id}"

    # Safe abstract from description
    safe_abstract = description.replace('"', "'").replace('\n', ' ').strip()
    if len(safe_abstract) > 1000:
        safe_abstract = safe_abstract[:997] + "..."

    # Religious values list
    rvl = "N/A"
    if religious_traditions and religious_traditions.strip():
        rvl = religious_traditions.replace('"', "'")

    # EXSR key
    key = f"EXSR{exsr_num:04d}"

    # Build YAML frontmatter
    fm_lines = [
        "---",
        "",
        "",
        "",
        "Human View: ",
        "Human View Date: ",
        "Human View note: ",
        "Not AI: ",
        f'key: {key}',
        f'type: {paper_type}',
        f'short_title: "{safe_short_title}"',
        f'year: {year}',
        f'first_author: {first_author}',
        f'last_author: {last_author}',
        f'authors: {authors_yaml}',
        f'authors_incomplete: {authors_incomplete}',
        f'url: "{url}"',
        f'external_pdf: "{safe_external_pdf}"',
        f'local_pdf: "N/A"',
        f'pdf_extract: ""',
        f'publication: {publication}',
        f'DATE_ADDED: {DATE_ADDED}',
        f'ethics_overall: ""',
        f'virtue_ethics: ""',
        f'deontological_ethics: ""',
        f'utilitarian_ethics: ""',
        f'national_ethnic_cultural: ""',
        f'religious_values: ""',
        f'rv_islam: 0',
        f'rv_christianity: 0',
        f'rv_buddhism: 0',
        f'rv_judaism: 0',
        f'rv_hinduism: 0',
        f'rv_sikhism: 0',
        f'rv_confucianism: 0',
        f'rv_taoism: 0',
        f'rv_shinto: 0',
        f'rv_jainism: 0',
        f'rv_bahai: 0',
        f'rv_zoroastrianism: 0',
        f'rv_ubuntu: 0',
        f'rv_indigenous: 0',
        f'religious_values_list: "{rvl}"',
        f'mp_mft: 0',
        f'mp_schwartz: 0',
        f'mp_trolley: 0',
        f'mp_kohlberg: 0',
        f'mp_dual_process: 0',
        f'mp_intuitionist: 0',
        f'mp_dyadic: 0',
        f'mp_identity: 0',
        f'moral_psychology: "N/A"',
        f'newtags: ',
        f'is_benchmark: ""',
        f'is_eval: ""',
        f'is_dataset: ""',
        f'tags: ',
        f'abstract: "{safe_abstract}"',
        f'data_description: ""',
        f'data_metrics: ""',
        f'LLM_assessed: "NA"',
        f'DATA_URL: "{code_data_url}"',
        "---",
    ]

    frontmatter_str = "\n".join(fm_lines)

    # Validate frontmatter (the part between --- delimiters)
    inner_fm = "\n".join(fm_lines[1:-1])
    is_valid, issues = validate_frontmatter(inner_fm)

    # Build body
    # Author wikilinks for body
    authors_body_raw = authors_raw.replace("[[", "").replace("]]", "")
    author_links = []
    for a in re.split(r'\s*;\s*', authors_body_raw):
        a = a.strip().rstrip(".")
        if a and a.lower() not in ("others", "not fully extracted", "not fully extracted - multiple authors"):
            author_links.append(f"[[{a}]]")

    body_lines = [
        f"# {title}",
        "",
        "## Authors",
        "",
        ", ".join(author_links) if author_links else "Unknown",
        "",
        "## Metadata",
        "",
        f"**Authors:** {authors_body_raw or 'Unknown'}",
        "",
        f"**Year:** {year}",
        "",
        f"**Type:** {paper_type}",
        "",
    ]
    if publication:
        body_lines.append(f"**Venue:** {publication}")
        body_lines.append("")

    body_lines.append("## Links")
    body_lines.append("")
    if arxiv_id:
        body_lines.append(f"- **arXiv:** https://arxiv.org/abs/{arxiv_id}")
    if doi:
        body_lines.append(f"- **DOI:** https://doi.org/{doi}")
    if url and "arxiv.org" not in url:
        body_lines.append(f"- **URL:** {url}")
    if code_data_url:
        body_lines.append(f"- **Code/Data:** {code_data_url}")
    body_lines.append("")

    body_lines.append("## Abstract")
    body_lines.append("")
    body_lines.append(description or "(Abstract not available)")
    body_lines.append("")

    if benchmark_name:
        body_lines.append("## Benchmark")
        body_lines.append("")
        body_lines.append(f"**Name:** {benchmark_name}")
        body_lines.append("")

    if entry.get("dataset_size"):
        body_lines.append("## Dataset Information")
        body_lines.append("")
        body_lines.append(entry["dataset_size"])
        body_lines.append("")

    body_lines.append("## Notes")
    body_lines.append("")
    agents = ", ".join(entry.get("source_agents", []))
    body_lines.append(f"**Source:** Religious & Language Search (2026-02-13), {agents}")
    readiness = entry.get("implementation_readiness", "MEDIUM")
    body_lines.append(f"**Implementation Readiness:** {readiness}")
    body_lines.append("")

    body_lines.append("## Tags")
    body_lines.append("")

    content = frontmatter_str + "\n" + "\n".join(body_lines)
    return content, issues


# ============================================================
# Main
# ============================================================

def main():
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("Import Religious & Language Search Papers")
    print("=" * 60)

    # Load master list
    master_path = LOGS_DIR / "20260213-religious_language_master_list.json"
    if not master_path.exists():
        print(f"ERROR: Master list not found: {master_path}")
        print("Run consolidate_religious_language_search.py first.")
        sys.exit(1)

    data = json.loads(master_path.read_text(encoding="utf-8"))
    approved = data.get("approved", [])
    print(f"  Loaded {len(approved)} approved candidates")

    # Process each entry
    import_log = {
        "date": DATE_ADDED,
        "total_candidates": len(approved),
        "imported": [],
        "skipped": [],
        "validation_warnings": [],
    }

    exsr_num = EXSR_START
    created = 0
    skipped = 0
    warnings = 0

    for i, entry in enumerate(approved):
        title = entry.get("title", "Untitled")
        filename = make_filename(entry.get("year", 0), entry.get("authors", ""), title)
        filepath = PAPERS_DIR / filename

        # Collision detection
        if filepath.exists():
            print(f"  [{i+1}/{len(approved)}] SKIP (exists): {filename}")
            import_log["skipped"].append({
                "title": title,
                "filename": filename,
                "reason": "File already exists",
            })
            skipped += 1
            continue

        # Build paper file
        content, issues = build_paper_file(entry, exsr_num)

        if issues:
            print(f"  [{i+1}/{len(approved)}] WARN: {filename} — {'; '.join(issues)}")
            import_log["validation_warnings"].append({
                "title": title,
                "filename": filename,
                "issues": issues,
            })
            warnings += 1

        if dry_run:
            if (i + 1) <= 3:  # Show first 3 in dry-run
                print(f"  [{i+1}/{len(approved)}] Would create: {filename} (EXSR{exsr_num:04d})")
        else:
            filepath.write_text(content, encoding="utf-8")
            if (i + 1) % 50 == 0 or (i + 1) <= 5:
                print(f"  [{i+1}/{len(approved)}] Created: {filename}")

        import_log["imported"].append({
            "title": title,
            "filename": filename,
            "key": f"EXSR{exsr_num:04d}",
            "arxiv_id": entry.get("arxiv_id", ""),
            "doi": entry.get("doi", ""),
        })
        exsr_num += 1
        created += 1

    # Write import log
    log_path = LOGS_DIR / "20260213-import_log.json"
    if not dry_run:
        log_path.write_text(json.dumps(import_log, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\n  Wrote import log: {log_path.name}")

    # Summary
    print(f"\n{'=' * 60}")
    print(f"SUMMARY")
    print(f"{'=' * 60}")
    print(f"  Total candidates:       {len(approved)}")
    print(f"  Created:                {created}")
    print(f"  Skipped (collision):    {skipped}")
    print(f"  Validation warnings:    {warnings}")
    print(f"  EXSR range:             EXSR{EXSR_START:04d} - EXSR{exsr_num - 1:04d}")
    if dry_run:
        print(f"  [DRY RUN — no files written]")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
