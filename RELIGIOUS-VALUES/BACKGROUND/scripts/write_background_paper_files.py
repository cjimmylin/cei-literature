#!/usr/bin/env python3
"""
Write paper markdown files from a JSON input list.

Usage:
    python write_background_paper_files.py papers.json

Input JSON format: list of objects with fields:
    title, authors, year, doi, url, source, type, priority,
    expert_source, topic_tags, relevance_note, folder,
    local_document (optional), document_acquired (optional)
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

BACKGROUND_DIR = Path(__file__).resolve().parent.parent


def slugify_title(title: str) -> str:
    """Create a short title slug for filenames (~4 meaningful words)."""
    t = re.sub(r'^(the|a|an)\s+', '', title.lower())
    words = re.findall(r'[a-z0-9]+', t)
    slug_words = []
    for w in words[:6]:
        if len(w) <= 2 and w not in ("ai", "eu", "us", "uk"):
            continue
        slug_words.append(w.capitalize())
        if len(slug_words) >= 4:
            break
    return " ".join(slug_words) if slug_words else "Untitled"


def extract_first_author(authors: list | str) -> str:
    """Extract first author last name."""
    if isinstance(authors, str):
        authors = [authors]
    if not authors:
        return "Unknown"
    first = authors[0]
    # "Last, First" format
    if "," in first:
        return first.split(",")[0].strip()
    # "First Last" format
    parts = first.strip().split()
    return parts[-1] if parts else "Unknown"


def make_filename(year: str | int, authors: list | str, title: str) -> str:
    """Create YYYY-Author-Short Title.md filename."""
    y = str(year) if year else "XXXX"
    author = extract_first_author(authors)
    short = slugify_title(title)
    return f"{y}-{author}-{short}.md"


def format_yaml_list(items: list, indent: str = "  ") -> str:
    """Format a list as YAML list items."""
    if not items:
        return "[]"
    if len(items) == 1:
        val = items[0]
        if isinstance(val, str):
            return f'["{val}"]' if "," in val or ":" in val else f"[{val}]"
    lines = []
    for item in items:
        if isinstance(item, str):
            if any(c in item for c in ",:[]{}#&*!|>'\"%@`"):
                lines.append(f'{indent}- "{item}"')
            else:
                lines.append(f'{indent}- {item}')
        else:
            lines.append(f'{indent}- {item}')
    return "\n".join(lines)


def write_paper_file(paper: dict, target_dir: Path) -> str | None:
    """Write a single paper markdown file. Returns filename or None on error."""
    title = paper.get("title", "")
    authors = paper.get("authors", [])
    year = paper.get("year", "")
    doi = paper.get("doi", "")
    url = paper.get("url", "")
    source = paper.get("source", "")
    ptype = paper.get("type", "journal_article")
    priority = paper.get("priority", "supplementary")
    expert_source = paper.get("expert_source", [])
    topic_tags = paper.get("topic_tags", [])
    relevance_note = paper.get("relevance_note", "")
    local_document = paper.get("local_document", "")
    document_acquired = paper.get("document_acquired", False)

    if isinstance(authors, str):
        authors = [a.strip() for a in authors.split(";")]
    if isinstance(expert_source, (int, str)):
        expert_source = [expert_source]
    if isinstance(topic_tags, str):
        topic_tags = [t.strip() for t in topic_tags.split(",")]

    filename = make_filename(year, authors, title)
    filepath = target_dir / filename

    # Avoid overwriting — append -2, -3, etc.
    if filepath.exists():
        base = filepath.stem
        for i in range(2, 10):
            candidate = target_dir / f"{base}-{i}.md"
            if not candidate.exists():
                filepath = candidate
                filename = candidate.name
                break

    # Build frontmatter
    lines = ["---"]
    lines.append(f'title: "{title}"')
    lines.append("authors:")
    for a in authors:
        lines.append(f'  - "{a}"')
    lines.append(f"year: {year}")
    if doi:
        lines.append(f'doi: "{doi}"')
    if url:
        lines.append(f'url: "{url}"')
    lines.append(f'source: "{source}"')
    lines.append(f"type: {ptype}")
    lines.append(f"priority: {priority}")
    lines.append(f"expert_source: [{', '.join(str(e) for e in expert_source)}]")
    lines.append(f"topic_tags: [{', '.join(str(t) for t in topic_tags)}]")
    lines.append(f'relevance_note: "{relevance_note}"')
    lines.append(f'local_document: "{local_document}"')
    lines.append(f"document_acquired: {'true' if document_acquired else 'false'}")
    lines.append("---")
    lines.append("")

    filepath.write_text("\n".join(lines), encoding="utf-8")
    return filename


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python write_background_paper_files.py papers.json")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"ERROR: Input file not found: {input_path}")
        sys.exit(1)

    papers = json.loads(input_path.read_text(encoding="utf-8"))
    print(f"Processing {len(papers)} papers...")

    # Map folder names to directories
    folder_dirs: dict[str, Path] = {}
    for d in BACKGROUND_DIR.iterdir():
        if d.is_dir() and not d.name.startswith(".") and d.name != "scripts":
            folder_dirs[d.name] = d

    written = 0
    errors = 0
    for p in papers:
        folder = p.get("folder", "01-ai-values-alignment")
        target = folder_dirs.get(folder)
        if target is None:
            target = BACKGROUND_DIR / folder
            target.mkdir(exist_ok=True)
            folder_dirs[folder] = target
        try:
            fname = write_paper_file(p, target)
            if fname:
                written += 1
                print(f"  + {folder}/{fname}")
        except Exception as e:
            errors += 1
            print(f"  ! Error writing {p.get('title', '?')}: {e}")

    print(f"\nDone: {written} written, {errors} errors")


if __name__ == "__main__":
    main()
