"""Import cultural-global literature search results as paper stubs into the vault.

Reads JSON search result files, filters to in_vault: false papers, deduplicates
against each other and existing vault papers, then creates stub .md files.

Usage:
    ../.venv/bin/python CULTURAL-GLOBAL/SCRIPTS/import_from_search_results.py [--dry-run]
"""
from __future__ import annotations

import argparse
import functools
import json
import re
import sys
from pathlib import Path

print = functools.partial(print, flush=True)

# Paths
WS_DIR = Path(__file__).resolve().parent.parent.parent  # CEI-Lit-WS
PAPERS_DIR = WS_DIR / "papers"
SEARCH_DIR = WS_DIR / "CULTURAL-GLOBAL" / "LITERATURE-SEARCH"

INPUT_FILES = [
    SEARCH_DIR / "20260403-literature-search-results.json",
    SEARCH_DIR / "20260403-targeted-gap-search-results.json",
]


def sanitize_filename(s: str) -> str:
    """Remove special characters, keep alphanumeric and spaces."""
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def short_title_from_title(title: str, max_words: int = 6) -> str:
    """First N words of title, sanitized for filename."""
    words = title.split()[:max_words]
    return sanitize_filename(' '.join(words))


def extract_surname(authors: str) -> str:
    """Extract first author surname from author string."""
    if not authors or authors.strip().lower() == "unknown":
        return "Unknown"
    # Handle "et al." suffix
    name = authors.split(" et al.")[0].strip()
    # Handle "First Last" or "Last, First" formats
    if "," in name:
        return name.split(",")[0].strip()
    parts = name.split()
    if len(parts) >= 2:
        return parts[-1].strip()
    return parts[0].strip() if parts else "Unknown"


def infer_type(url: str, source: str) -> str:
    """Infer document type from URL and source."""
    url_lower = url.lower() if url else ""
    source_lower = source.lower() if source else ""

    if "arxiv.org" in url_lower:
        return "preprint"
    if any(kw in source_lower for kw in ["conference", "proceedings"]):
        return "conferencePaper"
    if any(kw in source_lower for kw in ["journal", "sciencedirect", "springer"]):
        return "journalArticle"
    return "document"


def normalize_title(title: str) -> str:
    """Normalize title for dedup: lowercase, strip punctuation, first 40 chars."""
    t = re.sub(r'[^\w\s]', '', title.lower()).strip()
    return t[:40]


def load_vault_short_titles() -> set[str]:
    """Scan existing papers for short_title values, return normalized set."""
    titles = set()
    pattern = re.compile(r'^short_title:\s*"?([^"\n]+)"?\s*$', re.MULTILINE)
    for f in PAPERS_DIR.iterdir():
        if not f.suffix == '.md':
            continue
        try:
            text = f.read_text(encoding='utf-8')[:3000]  # short_title always near top
            m = pattern.search(text)
            if m:
                titles.add(normalize_title(m.group(1)))
        except Exception:
            pass
    return titles


def make_filename(year: int | str, surname: str, title: str) -> str:
    """Build YYYY-Surname-Short Title.md filename."""
    short = short_title_from_title(title)
    return f"{year}-{sanitize_filename(surname)}-{short}.md"


def safe_write(path: Path, content: str, dry_run: bool) -> Path:
    """Write file, appending -2, -3 etc. on collision. Returns actual path used."""
    if not path.exists():
        if not dry_run:
            path.write_text(content, encoding='utf-8')
        return path

    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    counter = 2
    while True:
        candidate = parent / f"{stem}-{counter}{suffix}"
        if not candidate.exists():
            if not dry_run:
                candidate.write_text(content, encoding='utf-8')
            return candidate
        counter += 1


def build_stub(paper: dict, key_num: int) -> str:
    """Build YAML frontmatter stub for a paper."""
    key = f"CGSR{key_num:04d}"
    title = paper.get("title", "Unknown Title")
    year = paper.get("year", 2025)
    authors_raw = paper.get("authors", "Unknown")
    url = paper.get("url", "")
    description = paper.get("description", "")
    gap_cat = paper.get("gap_category", "")
    doc_type = infer_type(url, paper.get("source", ""))

    # Author wikilink
    if authors_raw.strip().lower() == "unknown":
        first_author = "[[Unknown]]"
        authors_str = "Unknown"
    else:
        surname = extract_surname(authors_raw)
        first_author = f"[[{authors_raw.split(' et al.')[0].strip()}]]"
        authors_str = authors_raw

    # Flatten newlines and escape quotes in strings
    description = re.sub(r'\s*\n\s*', ' ', description).strip()
    safe_title = title.replace('"', '\\"')
    safe_desc = description.replace('"', '\\"')
    safe_authors = authors_str.replace('"', '\\"')
    safe_first = first_author  # wikilinks don't need escaping

    return f"""---
key: "{key}"
type: "{doc_type}"
short_title: "{safe_title}"
year: {year}
first_author: "{safe_first}"
authors: "{safe_authors}"
url: "{url}"
abstract: "{safe_desc}"
DATE_ADDED: 20260403
cultural_gap_category: "{gap_cat}"
ethics_overall: 0
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
care_ethics: 0
contractarian_ethics: 0
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
---
"""


def main():
    parser = argparse.ArgumentParser(description="Import cultural-global search results as paper stubs")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created without writing")
    args = parser.parse_args()

    # Load all papers from both files
    all_papers = []
    for fpath in INPUT_FILES:
        if not fpath.exists():
            print(f"WARNING: {fpath.name} not found, skipping")
            continue
        data = json.loads(fpath.read_text(encoding='utf-8'))
        papers = [p for p in data.get("papers", []) if not p.get("in_vault", True)]
        print(f"  Loaded {len(papers)} new papers from {fpath.name}")
        all_papers.extend(papers)

    print(f"\nTotal candidates (in_vault=false): {len(all_papers)}")

    # Dedup among candidates by normalized title (first 40 chars)
    seen_titles: dict[str, int] = {}
    unique_papers = []
    cross_dedup = 0
    for p in all_papers:
        norm = normalize_title(p.get("title", ""))
        if norm in seen_titles:
            cross_dedup += 1
            continue
        seen_titles[norm] = len(unique_papers)
        unique_papers.append(p)

    print(f"After cross-file dedup: {len(unique_papers)} (removed {cross_dedup} duplicates)")

    # Dedup against existing vault
    vault_titles = load_vault_short_titles()
    print(f"Existing vault short_titles loaded: {len(vault_titles)}")

    final_papers = []
    vault_dedup = 0
    for p in unique_papers:
        norm = normalize_title(p.get("title", ""))
        if norm in vault_titles:
            vault_dedup += 1
            continue
        final_papers.append(p)

    print(f"After vault dedup: {len(final_papers)} (removed {vault_dedup} already in vault)")

    if not final_papers:
        print("\nNo new papers to import.")
        return

    # Create stubs
    category_counts: dict[str, int] = {}
    created = 0
    prefix = "[DRY RUN] " if args.dry_run else ""

    for i, paper in enumerate(final_papers, start=1):
        year = paper.get("year", 2025)
        surname = extract_surname(paper.get("authors", "Unknown"))
        title = paper.get("title", "Unknown")
        gap_cat = paper.get("gap_category", "Unknown")

        filename = make_filename(year, surname, title)
        target = PAPERS_DIR / filename
        content = build_stub(paper, i)
        actual_path = safe_write(target, content, args.dry_run)

        category_counts[gap_cat] = category_counts.get(gap_cat, 0) + 1
        created += 1

        if created <= 5 or created % 20 == 0:
            print(f"  {prefix}Created: {actual_path.name}")

    # Summary
    print(f"\n{'=' * 60}")
    print(f"{'DRY RUN ' if args.dry_run else ''}IMPORT SUMMARY")
    print(f"{'=' * 60}")
    print(f"Papers created:          {created}")
    print(f"Cross-file duplicates:   {cross_dedup}")
    print(f"Vault duplicates:        {vault_dedup}")
    print(f"Total candidates:        {len(all_papers)}")
    print(f"\nBreakdown by gap_category:")
    for cat in sorted(category_counts):
        print(f"  {cat:40s} {category_counts[cat]:4d}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
