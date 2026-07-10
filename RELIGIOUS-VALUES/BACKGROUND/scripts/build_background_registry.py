#!/usr/bin/env python3
"""
Build BACKGROUND registry and summary report from markdown paper files.

Reads all .md files in BACKGROUND subdirectories, validates YAML frontmatter,
performs deduplication, and generates:
  - BACKGROUND-registry.json
  - 20260403-literature-search-report.md

Usage:
    python build_background_registry.py [--check-vault]

    --check-vault   Also cross-reference against CEI-Lit-WS vault (2,043 papers)
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

BACKGROUND_DIR = Path(__file__).resolve().parent.parent
VAULT_PAPERS_DIR = BACKGROUND_DIR.parent.parent / "papers"

EXPERT_NAMES = {
    1: "Islamic Ethics & Bioethics",
    2: "Christian Theological Ethics",
    3: "Dharmic Philosophy",
    4: "Confucian Philosophy",
    5: "African Philosophy & Ubuntu",
    6: "Jewish Studies & Computational Talmudics",
    7: "AI Evaluation & Benchmarking",
    8: "Cross-Cultural HCI & Psychology",
    9: "Philosophy of Information & AI Ethics",
    10: "NLP & Religious Text Computation",
    11: "Cognitive Science & AI Fairness",
    12: "AI Governance & Comparative Ethics",
    13: "Psychometrics & Educational Measurement",
    14: "Statistical Methods & Bibliometrics",
}

FOLDER_MAP = {
    "01-ai-values-alignment": 1,
    "02-religious-nlp": 2,
    "03-cultural-values-ai": 3,
    "04-islamic-ai-ethics": 4,
    "05-christian-ethics-ai": 5,
    "06-dharmic-ethics-ai": 6,
    "07-comparative-religious-ethics": 7,
    "08-benchmark-psychometrics": 8,
    "09-ai-bias-religion": 9,
    "10-indigenous-african-ai": 10,
    "11-jewish-ethics-ai": 11,
    "12-east-asian-philosophy-ai": 12,
}

# Subdirectory names that are NOT paper folders (skip during collection)
SKIP_DIRS = {"scripts", "council", "logs", "Documents"}


def parse_frontmatter(text: str) -> dict | None:
    """Extract YAML frontmatter from markdown text (simple parser, no PyYAML needed)."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm_text = text[3:end].strip()
    result: dict = {}
    current_key: str | None = None
    list_items: list = []

    for line in fm_text.split("\n"):
        # List item continuation
        if line.strip().startswith("- ") and current_key:
            item = line.strip()[2:].strip().strip('"').strip("'")
            list_items.append(item)
            continue

        # If we were accumulating list items, save them
        if list_items and current_key:
            result[current_key] = list_items
            list_items = []

        # Key: value pair
        m = re.match(r'^(\w[\w_]*)\s*:\s*(.*)', line)
        if m:
            current_key = m.group(1)
            val = m.group(2).strip()

            # Inline list: [a, b, c]
            if val.startswith("[") and val.endswith("]"):
                items = [x.strip().strip('"').strip("'")
                         for x in val[1:-1].split(",") if x.strip()]
                result[current_key] = items
            elif val.startswith('"') and val.endswith('"'):
                result[current_key] = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                result[current_key] = val[1:-1]
            elif val == "":
                # Might be followed by list items
                pass
            else:
                result[current_key] = val
        else:
            current_key = None

    # Final list
    if list_items and current_key:
        result[current_key] = list_items

    return result


def normalize_title(title: str) -> str:
    """Normalize title for dedup comparison."""
    t = title.lower()
    t = unicodedata.normalize("NFKD", t)
    t = re.sub(r'[^\w\s]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def word_overlap(a: str, b: str) -> float:
    """Compute word overlap ratio between two normalized titles.
    Uses max(len) as denominator to avoid false positives when
    a short title is a prefix of a longer one."""
    words_a = set(a.split())
    words_b = set(b.split())
    if not words_a or not words_b:
        return 0.0
    stop = {"the", "a", "an", "of", "in", "on", "for", "and", "to",
            "its", "by", "from", "with", "as"}
    words_a = words_a - stop
    words_b = words_b - stop
    if len(words_a) < 3 or len(words_b) < 3:
        return 0.0
    intersection = words_a & words_b
    return len(intersection) / max(len(words_a), len(words_b))


def load_vault_titles() -> set[str]:
    """Load normalized titles from CEI-Lit-WS vault for cross-reference."""
    titles: set[str] = set()
    if not VAULT_PAPERS_DIR.exists():
        return titles
    for p in VAULT_PAPERS_DIR.iterdir():
        if p.suffix == ".md":
            try:
                text = p.read_text(encoding="utf-8", errors="replace")[:2000]
                m = re.search(r'^short_title:\s*"?(.+?)"?\s*$', text, re.MULTILINE)
                if m:
                    titles.add(normalize_title(m.group(1)))
            except Exception:
                pass
    return titles


def collect_papers() -> list[dict]:
    """Collect all paper entries from BACKGROUND subdirectories."""
    papers: list[dict] = []
    for subdir in sorted(BACKGROUND_DIR.iterdir()):
        if not subdir.is_dir() or subdir.name.startswith("."):
            continue
        if subdir.name in SKIP_DIRS:
            continue
        folder_name = subdir.name
        for md_file in sorted(subdir.glob("*.md")):
            try:
                text = md_file.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                print(f"  WARNING: Cannot read {md_file}: {e}")
                continue
            fm = parse_frontmatter(text)
            if fm is None:
                print(f"  WARNING: No frontmatter in {md_file.relative_to(BACKGROUND_DIR)}")
                continue
            fm["_file"] = str(md_file.relative_to(BACKGROUND_DIR))
            fm["_folder"] = folder_name
            papers.append(fm)
    return papers


def deduplicate(papers: list[dict]) -> tuple[list[dict], list[dict]]:
    """Deduplicate by DOI exact match and title word overlap (>0.85)."""
    unique: list[dict] = []
    duplicates: list[dict] = []
    seen_dois: dict[str, dict] = {}
    seen_titles: dict[str, dict] = {}

    for p in papers:
        doi = p.get("doi", "").strip().lower()
        title = p.get("title", "")
        norm_t = normalize_title(title)
        is_dup = False

        # DOI exact match
        if doi and doi not in ("", "null", "n/a"):
            if doi in seen_dois:
                orig = seen_dois[doi]
                _merge_expert_source(orig, p)
                duplicates.append({**p, "_dup_reason": f"DOI match with {orig['_file']}"})
                is_dup = True
                continue

        # Title similarity
        if norm_t and not is_dup:
            for prev_title, prev_p in seen_titles.items():
                if word_overlap(norm_t, prev_title) > 0.85:
                    _merge_expert_source(prev_p, p)
                    duplicates.append({**p, "_dup_reason": f"Title overlap with {prev_p['_file']}"})
                    is_dup = True
                    break

        if not is_dup:
            unique.append(p)
            if doi and doi not in ("", "null", "n/a"):
                seen_dois[doi] = p
            if norm_t:
                seen_titles[norm_t] = p

    return unique, duplicates


def _merge_expert_source(orig: dict, new: dict) -> None:
    """Merge expert_source lists from new into orig."""
    orig_experts = orig.get("expert_source", [])
    new_experts = new.get("expert_source", [])
    if isinstance(orig_experts, str):
        orig_experts = [orig_experts]
    if isinstance(new_experts, str):
        new_experts = [new_experts]
    merged = sorted(set(str(e) for e in orig_experts) | set(str(e) for e in new_experts))
    orig["expert_source"] = merged


def validate_paper(p: dict) -> list[str]:
    """Validate a paper entry, return list of issues."""
    issues: list[str] = []
    required = ["title", "authors", "year", "source", "type", "priority"]
    for field in required:
        if field not in p or not p[field]:
            issues.append(f"Missing required field: {field}")

    year = p.get("year", "")
    try:
        y = int(year)
        if y < 2000:
            issues.append(f"Year {y} seems too old (expected >= 2000)")
    except (ValueError, TypeError):
        issues.append(f"Invalid year: {year}")

    valid_types = {"journal_article", "conference_paper", "working_paper",
                   "report", "book_chapter", "book"}
    if p.get("type") and p["type"] not in valid_types:
        issues.append(f"Invalid type: {p['type']} (expected one of {valid_types})")

    valid_priorities = {"must_read", "important", "supplementary"}
    if p.get("priority") and p["priority"] not in valid_priorities:
        issues.append(f"Invalid priority: {p['priority']} (expected one of {valid_priorities})")

    return issues


def build_registry(papers: list[dict]) -> list[dict]:
    """Build clean registry entries from paper data."""
    registry: list[dict] = []
    for p in papers:
        entry = {
            "title": p.get("title", ""),
            "authors": p.get("authors", []),
            "year": p.get("year", ""),
            "doi": p.get("doi", ""),
            "url": p.get("url", ""),
            "source": p.get("source", ""),
            "type": p.get("type", ""),
            "priority": p.get("priority", ""),
            "expert_source": p.get("expert_source", []),
            "topic_tags": p.get("topic_tags", []),
            "relevance_note": p.get("relevance_note", ""),
            "local_document": p.get("local_document", ""),
            "document_acquired": p.get("document_acquired", "false"),
            "file": p.get("_file", ""),
            "folder": p.get("_folder", ""),
        }
        registry.append(entry)
    return registry


def generate_report(papers: list[dict], duplicates: list[dict],
                    vault_overlap: list[str], validation_issues: dict[str, list[str]]) -> str:
    """Generate the dated literature search report."""
    lines = [
        "# Literature Search Report: Religious Values AI Benchmarks Background",
        "",
        "**Date:** 2026-04-03",
        f"**Total unique papers:** {len(papers)}",
        f"**Duplicates removed:** {len(duplicates)}",
        f"**Vault overlaps found:** {len(vault_overlap)}",
        "",
    ]

    # --- Papers by Priority Tier ---
    priority_counts = Counter(p.get("priority", "unknown") for p in papers)
    lines.append("## Papers by Priority Tier")
    lines.append("")
    lines.append("| Tier | Count |")
    lines.append("|------|-------|")
    for tier in ["must_read", "important", "supplementary"]:
        lines.append(f"| {tier} | {priority_counts.get(tier, 0)} |")
    unknown = priority_counts.get("unknown", 0)
    if unknown:
        lines.append(f"| unknown | {unknown} |")
    lines.append(f"| **Total** | **{len(papers)}** |")
    lines.append("")

    # --- Papers by Expert Domain ---
    expert_counts: dict[int, int] = defaultdict(int)
    for p in papers:
        sources = p.get("expert_source", [])
        if isinstance(sources, str):
            sources = [sources]
        for s in sources:
            try:
                expert_counts[int(s)] += 1
            except (ValueError, TypeError):
                pass
    lines.append("## Papers by Expert Domain")
    lines.append("")
    lines.append("| # | Expert Domain | Papers |")
    lines.append("|---|---------------|--------|")
    for i in range(1, max(EXPERT_NAMES.keys()) + 1):
        name = EXPERT_NAMES.get(i, f"Expert {i}")
        count = expert_counts.get(i, 0)
        flag = " (low)" if count < 5 else ""
        lines.append(f"| {i} | {name} | {count}{flag} |")
    lines.append("")

    # --- Papers by Folder ---
    folder_counts = Counter(p.get("_folder", "unknown") for p in papers)
    lines.append("## Papers by Folder")
    lines.append("")
    lines.append("| Folder | Count |")
    lines.append("|--------|-------|")
    for folder in sorted(folder_counts.keys()):
        lines.append(f"| {folder} | {folder_counts[folder]} |")
    lines.append("")

    # --- Papers by Type ---
    type_counts = Counter(p.get("type", "unknown") for p in papers)
    lines.append("## Papers by Type")
    lines.append("")
    lines.append("| Type | Count |")
    lines.append("|------|-------|")
    for t, c in type_counts.most_common():
        lines.append(f"| {t} | {c} |")
    lines.append("")

    # --- Papers by Year ---
    year_counts: Counter = Counter()
    for p in papers:
        try:
            year_counts[int(p.get("year", 0))] += 1
        except (ValueError, TypeError):
            year_counts["unknown"] += 1
    lines.append("## Papers by Year")
    lines.append("")
    lines.append("| Year | Count |")
    lines.append("|------|-------|")
    for y in sorted(year_counts.keys(), key=lambda x: (isinstance(x, str), x), reverse=True):
        lines.append(f"| {y} | {year_counts[y]} |")
    lines.append("")

    # --- Top Venues ---
    venue_counts = Counter(p.get("source", "unknown") for p in papers)
    lines.append("## Top Venues")
    lines.append("")
    lines.append("| Venue | Count |")
    lines.append("|-------|-------|")
    for v, c in venue_counts.most_common(20):
        lines.append(f"| {v} | {c} |")
    lines.append("")

    # --- Topic Tag Frequency ---
    tag_counts: Counter = Counter()
    for p in papers:
        tags = p.get("topic_tags", [])
        if isinstance(tags, str):
            tags = [tags]
        for t in tags:
            t_clean = t.strip()
            if t_clean:
                tag_counts[t_clean] += 1
    lines.append("## Topic Tag Frequency")
    lines.append("")
    lines.append("| Tag | Count |")
    lines.append("|-----|-------|")
    for t, c in tag_counts.most_common(30):
        lines.append(f"| {t} | {c} |")
    lines.append("")

    # --- Validation Issues ---
    if validation_issues:
        lines.append("## Validation Issues")
        lines.append("")
        for fname, issues in sorted(validation_issues.items()):
            lines.append(f"- **{fname}**: {'; '.join(issues)}")
        lines.append("")
    else:
        lines.append("## Validation Issues")
        lines.append("")
        lines.append("No validation issues found.")
        lines.append("")

    # --- Duplicates Removed ---
    if duplicates:
        lines.append("## Duplicates Removed")
        lines.append("")
        for d in duplicates:
            lines.append(f"- {d.get('_file', '?')}: {d.get('_dup_reason', '?')}")
        lines.append("")
    else:
        lines.append("## Duplicates Removed")
        lines.append("")
        lines.append("No duplicates found.")
        lines.append("")

    # --- Vault Cross-Reference ---
    if vault_overlap:
        lines.append("## Vault Cross-Reference Matches")
        lines.append("")
        for title in vault_overlap:
            lines.append(f"- {title}")
        lines.append("")

    # --- Gap Analysis ---
    lines.append("## Gap Analysis")
    lines.append("")

    # Folders with < 5 papers
    low_folders = [f for f in sorted(FOLDER_MAP.keys()) if folder_counts.get(f, 0) < 5]
    if low_folders:
        lines.append("### Under-represented Folders (< 5 papers)")
        lines.append("")
        for f in low_folders:
            lines.append(f"- {f}: {folder_counts.get(f, 0)} papers")
        lines.append("")

    # Expert domains with < 5 papers
    low_experts = [i for i in sorted(EXPERT_NAMES.keys()) if expert_counts.get(i, 0) < 5]
    if low_experts:
        lines.append("### Under-represented Expert Domains (< 5 papers)")
        lines.append("")
        for i in low_experts:
            lines.append(f"- Expert {i}: {EXPERT_NAMES.get(i, '?')} ({expert_counts.get(i, 0)} papers)")
        lines.append("")

    if not low_folders and not low_experts:
        lines.append("All folders and expert domains have >= 5 papers.")
        lines.append("")

    # Must-read target
    must_reads = priority_counts.get("must_read", 0)
    if must_reads < 25:
        lines.append(f"### Must-read deficit: {must_reads}/25 target")
        lines.append("")

    # Total target
    total = len(papers)
    if total < 95:
        lines.append(f"### Below total target: {total}/95 minimum")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    check_vault = "--check-vault" in sys.argv

    print("Collecting papers from BACKGROUND subdirectories...")
    papers = collect_papers()
    print(f"  Found {len(papers)} paper files")

    print("Validating frontmatter...")
    validation_issues: dict[str, list[str]] = {}
    for p in papers:
        issues = validate_paper(p)
        if issues:
            validation_issues[p.get("_file", "?")] = issues
    if validation_issues:
        print(f"  {len(validation_issues)} files have validation issues")
    else:
        print("  All files valid")

    print("Deduplicating...")
    unique, duplicates = deduplicate(papers)
    print(f"  {len(unique)} unique, {len(duplicates)} duplicates removed")

    vault_overlap: list[str] = []
    if check_vault:
        print("Cross-referencing against CEI-Lit-WS vault...")
        vault_titles = load_vault_titles()
        print(f"  Loaded {len(vault_titles)} vault titles")
        for p in unique:
            norm = normalize_title(p.get("title", ""))
            for vt in vault_titles:
                if word_overlap(norm, vt) > 0.85:
                    vault_overlap.append(p.get("title", "?"))
                    break
        print(f"  {len(vault_overlap)} overlaps with vault")

    print("Building registry...")
    registry = build_registry(unique)
    registry_path = BACKGROUND_DIR / "BACKGROUND-registry.json"
    registry_path.write_text(
        json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"  Written {registry_path.name} ({len(registry)} entries)")

    print("Generating report...")
    report = generate_report(unique, duplicates, vault_overlap, validation_issues)
    report_path = BACKGROUND_DIR / "20260403-literature-search-report.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"  Written {report_path.name}")

    # Summary
    priority_counts = Counter(p.get("priority", "unknown") for p in unique)
    print(f"\n=== SUMMARY ===")
    print(f"  Total unique: {len(unique)}")
    print(f"  Must-read:    {priority_counts.get('must_read', 0)}")
    print(f"  Important:    {priority_counts.get('important', 0)}")
    print(f"  Supplementary:{priority_counts.get('supplementary', 0)}")
    print(f"  Duplicates:   {len(duplicates)}")
    if validation_issues:
        print(f"  Validation issues: {len(validation_issues)}")


if __name__ == "__main__":
    main()
