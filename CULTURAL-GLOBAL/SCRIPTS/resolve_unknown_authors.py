#!/usr/bin/env python3
"""Resolve papers with authors: "Unknown" via 3-tier API lookup.

Tier 1: Semantic Scholar (10s delay)
Tier 2: CrossRef (1s delay)
Tier 3: OpenAlex (1s delay)

Usage:
    python resolve_unknown_authors.py [--dry-run] [--skip-rename]
"""
from __future__ import annotations

import argparse
import functools
import json
import os
import re
import sys
import time
import urllib.parse
from pathlib import Path

import requests

print = functools.partial(print, flush=True)

# Paths
WS = Path(__file__).resolve().parent.parent.parent  # CEI-Lit-WS
PAPERS_DIR = WS / "papers"
DATA_DIR = Path(__file__).resolve().parent.parent / "DATA"
REPORT_PATH = DATA_DIR / "20260403-author-resolutions.json"

SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "CEI-Literature-Vault/1.0 (academic research)"})


def find_unknown_papers() -> list[Path]:
    """Find all paper files with 'Unknown' in the filename."""
    return sorted(p for p in PAPERS_DIR.iterdir()
                  if p.suffix == ".md" and "-Unknown-" in p.name)


def extract_title(content: str) -> str | None:
    """Extract short_title from YAML frontmatter."""
    m = re.search(r'^short_title:\s*"((?:[^"\\]|\\.)*)"', content, re.MULTILINE)
    if m:
        return m.group(1)
    m = re.search(r"^short_title:\s*'((?:[^'\\]|\\.)*)'", content, re.MULTILINE)
    if m:
        return m.group(1)
    return None


def normalize(s: str) -> str:
    """Lowercase, strip punctuation for comparison."""
    return re.sub(r'[^a-z0-9 ]', '', s.lower()).strip()


def title_match(api_title: str, our_title: str) -> bool:
    """Check if titles match (first 40 chars, case-insensitive)."""
    a = normalize(api_title)[:40]
    b = normalize(our_title)[:40]
    if not a or not b:
        return False
    # Check if one starts with the other or high overlap
    return a.startswith(b) or b.startswith(a) or a == b


def format_author_name(name: str) -> str:
    """Normalize author name: 'First Last' format."""
    return name.strip()


def surname_from_name(name: str) -> str:
    """Extract surname (last word) from a full name."""
    parts = name.strip().split()
    if not parts:
        return "Unknown"
    return parts[-1]


# --- API Tiers ---

def search_semantic_scholar(title: str) -> dict | None:
    """Tier 1: Semantic Scholar title search."""
    try:
        params = {"query": title, "limit": 3, "fields": "title,authors,year,externalIds,url"}
        resp = SESSION.get(
            "https://api.semanticscholar.org/graph/v1/paper/search",
            params=params, timeout=30
        )
        if resp.status_code == 429:
            print("  [S2] Rate limited (429), skipping")
            return None
        resp.raise_for_status()
        data = resp.json()
        for paper in data.get("data", []):
            if paper.get("title") and title_match(paper["title"], title):
                authors = paper.get("authors", [])
                if authors and authors[0].get("name"):
                    return {
                        "source": "semantic_scholar",
                        "first_author": format_author_name(authors[0]["name"]),
                        "all_authors": [format_author_name(a["name"]) for a in authors if a.get("name")],
                        "matched_title": paper["title"],
                    }
    except Exception as e:
        print(f"  [S2] Error: {e}")
    return None


def search_crossref(title: str) -> dict | None:
    """Tier 2: CrossRef title search."""
    try:
        params = {"query.title": title, "rows": 3}
        resp = SESSION.get(
            "https://api.crossref.org/works",
            params=params, timeout=30
        )
        resp.raise_for_status()
        data = resp.json()
        for item in data.get("message", {}).get("items", []):
            item_titles = item.get("title", [])
            if item_titles and title_match(item_titles[0], title):
                authors = item.get("author", [])
                if authors:
                    first = authors[0]
                    first_name = f"{first.get('given', '')} {first.get('family', '')}".strip()
                    all_names = []
                    for a in authors:
                        n = f"{a.get('given', '')} {a.get('family', '')}".strip()
                        if n:
                            all_names.append(n)
                    if first_name:
                        return {
                            "source": "crossref",
                            "first_author": first_name,
                            "all_authors": all_names,
                            "matched_title": item_titles[0],
                        }
    except Exception as e:
        print(f"  [CR] Error: {e}")
    return None


def search_openalex(title: str) -> dict | None:
    """Tier 3: OpenAlex title search."""
    try:
        params = {"search": title, "per_page": 3}
        resp = SESSION.get(
            "https://api.openalex.org/works",
            params=params, timeout=30
        )
        resp.raise_for_status()
        data = resp.json()
        for item in data.get("results", []):
            item_title = item.get("title", "")
            if item_title and title_match(item_title, title):
                authorships = item.get("authorships", [])
                if authorships:
                    first_name = authorships[0].get("author", {}).get("display_name", "")
                    all_names = [
                        a.get("author", {}).get("display_name", "")
                        for a in authorships
                        if a.get("author", {}).get("display_name")
                    ]
                    if first_name:
                        return {
                            "source": "openalex",
                            "first_author": first_name,
                            "all_authors": all_names,
                            "matched_title": item_title,
                        }
    except Exception as e:
        print(f"  [OA] Error: {e}")
    return None


def resolve_authors(title: str) -> dict | None:
    """3-tier lookup. Returns resolution dict or None."""
    # Tier 1: Semantic Scholar
    result = search_semantic_scholar(title)
    if result:
        return result
    time.sleep(10)  # S2 rate limit

    # Tier 2: CrossRef
    result = search_crossref(title)
    if result:
        return result
    time.sleep(1)

    # Tier 3: OpenAlex
    result = search_openalex(title)
    if result:
        return result
    time.sleep(1)

    return None


def build_authors_string(all_authors: list[str]) -> str:
    """Build a compact authors string for YAML."""
    if len(all_authors) <= 5:
        return "; ".join(all_authors)
    return "; ".join(all_authors[:5]) + " et al."


def update_paper_yaml(filepath: Path, resolution: dict, dry_run: bool) -> bool:
    """Update first_author and authors in paper YAML. Returns True if changed."""
    content = filepath.read_text(encoding="utf-8")
    first_author = resolution["first_author"]
    authors_str = build_authors_string(resolution["all_authors"])

    # Update first_author
    new_content, c1 = re.subn(
        r'^first_author:\s*"?\[\[Unknown\]\]"?',
        f'first_author: "[[{first_author}]]"',
        content, count=1, flags=re.MULTILINE
    )

    # Update authors
    new_content, c2 = re.subn(
        r'^authors:\s*"?Unknown"?',
        f'authors: "{authors_str}"',
        new_content, count=1, flags=re.MULTILINE
    )

    # Update last_author if it exists as Unknown
    new_content, c3 = re.subn(
        r'^last_author:\s*"?\[\[Unknown\]\]"?',
        f'last_author: "[[{resolution["all_authors"][-1]}]]"',
        new_content, count=1, flags=re.MULTILINE
    )

    # Clear authors_incomplete if we resolved
    new_content, c4 = re.subn(
        r'^authors_incomplete:\s*true',
        'authors_incomplete: false',
        new_content, count=1, flags=re.MULTILINE
    )

    if c1 + c2 == 0:
        print("  No YAML fields matched for replacement")
        return False

    if dry_run:
        print(f"  [DRY-RUN] Would update: first_author=[[{first_author}]], authors=\"{authors_str}\"")
        return True

    filepath.write_text(new_content, encoding="utf-8")
    return True


def rename_paper(filepath: Path, resolution: dict, dry_run: bool) -> Path | None:
    """Rename YYYY-Unknown-Title.md -> YYYY-Surname-Title.md. Returns new path or None."""
    surname = surname_from_name(resolution["first_author"])
    old_name = filepath.name
    # Replace first occurrence of "Unknown" with surname
    new_name = old_name.replace("-Unknown-", f"-{surname}-", 1)
    if new_name == old_name:
        return None

    new_path = filepath.parent / new_name
    if new_path.exists():
        print(f"  Rename target already exists: {new_name}, skipping rename")
        return None

    if dry_run:
        print(f"  [DRY-RUN] Would rename: {old_name} -> {new_name}")
        return new_path

    os.rename(filepath, new_path)
    print(f"  Renamed: {old_name} -> {new_name}")
    return new_path


def main():
    parser = argparse.ArgumentParser(description="Resolve Unknown authors via API lookup")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    parser.add_argument("--skip-rename", action="store_true", help="Update YAML but don't rename files")
    args = parser.parse_args()

    papers = find_unknown_papers()
    print(f"Found {len(papers)} papers with Unknown authors\n")

    results = []
    resolved = {"semantic_scholar": 0, "crossref": 0, "openalex": 0}
    unresolved = 0

    for i, paper_path in enumerate(papers, 1):
        print(f"[{i}/{len(papers)}] {paper_path.name}")
        content = paper_path.read_text(encoding="utf-8")
        title = extract_title(content)
        if not title:
            print("  Could not extract title, skipping")
            results.append({
                "filename": paper_path.name,
                "old_authors": "Unknown",
                "new_authors": None,
                "source": "error_no_title",
                "confidence": 0,
            })
            unresolved += 1
            continue

        print(f"  Title: {title}")

        resolution = resolve_authors(title)

        if resolution:
            source = resolution["source"]
            resolved[source] += 1
            print(f"  RESOLVED via {source}: {resolution['first_author']} "
                  f"(+{len(resolution['all_authors'])-1} co-authors)")

            yaml_updated = update_paper_yaml(paper_path, resolution, args.dry_run)

            new_path = None
            if not args.skip_rename and yaml_updated:
                new_path = rename_paper(paper_path, resolution, args.dry_run)

            results.append({
                "filename": paper_path.name,
                "new_filename": new_path.name if new_path else None,
                "old_authors": "Unknown",
                "new_authors": build_authors_string(resolution["all_authors"]),
                "first_author": resolution["first_author"],
                "source": source,
                "matched_title": resolution["matched_title"],
                "confidence": 0.9 if source == "semantic_scholar" else 0.8,
            })
        else:
            unresolved += 1
            print("  UNRESOLVED after all 3 tiers")
            results.append({
                "filename": paper_path.name,
                "old_authors": "Unknown",
                "new_authors": None,
                "source": "unresolved",
                "confidence": 0,
            })

        # Rate limit: 10s after each Semantic Scholar call (already handled in resolve_authors)
        # Add small buffer between papers
        if i < len(papers):
            time.sleep(1)

    # Summary
    total_resolved = sum(resolved.values())
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Total papers:     {len(papers)}")
    print(f"Resolved:         {total_resolved}")
    print(f"  Semantic Scholar: {resolved['semantic_scholar']}")
    print(f"  CrossRef:         {resolved['crossref']}")
    print(f"  OpenAlex:         {resolved['openalex']}")
    print(f"Unresolved:       {unresolved}")

    # Save report
    if not args.dry_run:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        REPORT_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nReport saved: {REPORT_PATH}")
    else:
        print(f"\n[DRY-RUN] Report would be saved to: {REPORT_PATH}")


if __name__ == "__main__":
    main()
