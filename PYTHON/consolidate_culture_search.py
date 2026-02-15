#!/usr/bin/env python3
"""
Consolidate Culture/Nationality Search Agent Reports

Merges 30 agent JSON reports from the culture/nationality benchmark search,
deduplicates within new results, and cross-references against existing vault
papers to produce a master list of truly new papers.

Deduplication order:
  1. DOI match (normalized, excluding arXiv DOIs)
  2. arXiv ID match (with YYMM prefix validation)
  3. Title word-overlap >= 85%

Output:
  - logs/20260215-culture_search_master_list.json  (structured)
  - logs/20260215-culture_search_master_list.md     (human-readable)

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/consolidate_culture_search.py
"""

import functools
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Optional

# Force flush
print = functools.partial(print, flush=True)

# --- Path setup ---
SCRIPT_DIR = Path(__file__).parent.resolve()
WORKSPACE_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(WORKSPACE_ROOT / ".agent"))

from lib.yaml_utils import extract_frontmatter, parse_frontmatter

PAPERS_DIR = WORKSPACE_ROOT / "papers"
LOGS_DIR = WORKSPACE_ROOT / "logs"
DATE_PREFIX = "20260215"

# Agent report glob pattern
AGENT_REPORT_PATTERN = f"{DATE_PREFIX}-culture_search_agent_*.json"

# arXiv ID validation
ARXIV_ID_RE = re.compile(r'(\d{4}\.\d{4,5})')


def _is_valid_arxiv_id(candidate: str) -> bool:
    """Validate that a candidate arXiv ID has a plausible YYMM prefix."""
    parts = candidate.split(".")
    if len(parts) < 2:
        return False
    yymm = parts[0]
    if len(yymm) < 4:
        return False
    yy = int(yymm[:2])
    mm = int(yymm[2:4])
    return 7 <= yy <= 26 and 1 <= mm <= 12


def normalize_doi(doi_str: str) -> Optional[str]:
    """Normalize DOI: lowercase, strip URL prefix, skip N/A and arXiv DOIs."""
    if not doi_str or doi_str.strip().upper() in ("N/A", ""):
        return None
    doi = doi_str.strip().lower()
    doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    doi = doi.replace("https://dx.doi.org/", "").replace("http://dx.doi.org/", "")
    doi = doi.strip('"').strip("'").strip()
    if doi.startswith("10.48550/arxiv"):
        return None
    return doi if doi else None


def extract_arxiv_id_from_url(url: str) -> Optional[str]:
    """Extract arXiv ID from a URL string, with YYMM validation."""
    if not url:
        return None
    url_lower = url.lower()
    if "arxiv.org" not in url_lower and "10.48550" not in url_lower:
        return None
    m = ARXIV_ID_RE.search(url)
    if m and _is_valid_arxiv_id(m.group(1)):
        return m.group(1)
    return None


def normalize_title(title: str) -> str:
    """Normalize a title for comparison: lowercase, strip punctuation, collapse whitespace."""
    if not title:
        return ""
    t = title.lower()
    t = re.sub(r'[^a-z0-9\s]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def title_word_overlap(title_a: str, title_b: str) -> float:
    """Compute word overlap ratio between two titles (Jaccard-like)."""
    words_a = set(normalize_title(title_a).split())
    words_b = set(normalize_title(title_b).split())
    if not words_a or not words_b:
        return 0.0
    intersection = words_a & words_b
    union = words_a | words_b
    return len(intersection) / len(union) if union else 0.0


def load_existing_papers() -> list:
    """Load existing vault papers' identifiers for cross-referencing."""
    papers = []
    for p in sorted(PAPERS_DIR.glob("*.md")):
        try:
            content = p.read_text(encoding='utf-8')
            fm_text, _ = extract_frontmatter(content)
            if not fm_text:
                continue
            fields = parse_frontmatter(fm_text)
            doi = normalize_doi(fields.get('doi', ''))
            arxiv_id = None
            for field_name in ('url', 'external_pdf', 'doi'):
                val = fields.get(field_name, '')
                if val:
                    aid = extract_arxiv_id_from_url(val)
                    if aid:
                        arxiv_id = aid
                        break
            papers.append({
                'filename': p.name,
                'title': fields.get('short_title', '').strip('"').strip("'"),
                'doi': doi,
                'arxiv_id': arxiv_id,
            })
        except Exception as e:
            print(f"  WARNING: Could not parse {p.name}: {e}")
    return papers


def load_agent_reports() -> list:
    """Load all agent JSON reports from logs/."""
    reports = []
    for rp in sorted(LOGS_DIR.glob(AGENT_REPORT_PATTERN)):
        try:
            data = json.loads(rp.read_text(encoding='utf-8'))
            reports.append(data)
            print(f"  Loaded {rp.name}: {data.get('total_found', '?')} papers from agent {data.get('agent_id', '?')}")
        except Exception as e:
            print(f"  ERROR loading {rp.name}: {e}")
    return reports


def merge_papers(reports: list) -> list:
    """Extract all papers from all agent reports into a flat list."""
    all_papers = []
    for report in reports:
        agent_id = report.get('agent_id', 'unknown')
        for paper in report.get('papers_found', []):
            paper['source_agent'] = agent_id
            all_papers.append(paper)
    return all_papers


def deduplicate_new_papers(papers: list) -> list:
    """Deduplicate within new search results using DOI, arXiv ID, title overlap."""
    if not papers:
        return []

    # Index by DOI
    doi_groups = defaultdict(list)
    # Index by arXiv ID
    arxiv_groups = defaultdict(list)

    for i, p in enumerate(papers):
        doi = normalize_doi(p.get('doi', ''))
        if doi:
            doi_groups[doi].append(i)

        arxiv_id = p.get('arxiv_id', '')
        if arxiv_id:
            aid = arxiv_id.strip()
            if '.' in aid and _is_valid_arxiv_id(aid):
                arxiv_groups[aid].append(i)
        # Also try extracting from URL field
        url = p.get('url', '')
        aid = extract_arxiv_id_from_url(url)
        if aid:
            arxiv_groups[aid].append(i)

    # Union-Find for grouping duplicates
    parent = list(range(len(papers)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    # Merge by DOI
    for doi, indices in doi_groups.items():
        for i in range(1, len(indices)):
            union(indices[0], indices[i])

    # Merge by arXiv ID
    for aid, indices in arxiv_groups.items():
        for i in range(1, len(indices)):
            union(indices[0], indices[i])

    # Merge by title overlap (only for papers not yet grouped)
    for i in range(len(papers)):
        for j in range(i + 1, len(papers)):
            if find(i) == find(j):
                continue
            overlap = title_word_overlap(
                papers[i].get('title', ''),
                papers[j].get('title', '')
            )
            if overlap >= 0.85:
                union(i, j)

    # Collect groups and pick representative (most fields populated)
    groups = defaultdict(list)
    for i in range(len(papers)):
        groups[find(i)].append(i)

    deduped = []
    merge_count = 0
    for group_indices in groups.values():
        if len(group_indices) > 1:
            merge_count += 1
        # Pick the paper with most populated fields as representative
        best_idx = max(group_indices, key=lambda i: _richness(papers[i]))
        representative = papers[best_idx].copy()
        # Merge cultures_covered from all duplicates
        all_cultures = set()
        all_agents = set()
        for idx in group_indices:
            cultures = papers[idx].get('cultures_covered', [])
            if isinstance(cultures, list):
                all_cultures.update(cultures)
            elif isinstance(cultures, str):
                all_cultures.update(c.strip() for c in cultures.split(','))
            all_agents.add(papers[idx].get('source_agent', ''))
        representative['cultures_covered'] = sorted(all_cultures)
        representative['source_agents'] = sorted(all_agents)
        representative['duplicate_count'] = len(group_indices)
        deduped.append(representative)

    print(f"  Internal dedup: {len(papers)} -> {len(deduped)} ({merge_count} merge groups)")
    return deduped


def _richness(paper: dict) -> int:
    """Score how many fields are populated in a paper dict."""
    score = 0
    for key in ('title', 'authors', 'year', 'url', 'arxiv_id', 'doi',
                'benchmark_name', 'abstract_snippet', 'data_url', 'relevance_notes',
                'cultures_covered'):
        val = paper.get(key, '')
        if val and str(val).strip() and str(val).strip().lower() not in ('n/a', 'none', ''):
            score += 1
    return score


def cross_reference(new_papers: list, existing_papers: list) -> tuple:
    """Cross-reference new papers against existing vault papers.

    Returns (truly_new, already_in_vault).
    """
    # Build lookup indices for existing papers
    existing_dois = {}
    existing_arxiv = {}
    existing_titles = []

    for ep in existing_papers:
        if ep['doi']:
            existing_dois[ep['doi']] = ep['filename']
        if ep['arxiv_id']:
            existing_arxiv[ep['arxiv_id']] = ep['filename']
        existing_titles.append((ep['title'], ep['filename']))

    truly_new = []
    already_in_vault = []

    for paper in new_papers:
        matched_file = None

        # Check DOI
        doi = normalize_doi(paper.get('doi', ''))
        if doi and doi in existing_dois:
            matched_file = existing_dois[doi]

        # Check arXiv ID
        if not matched_file:
            arxiv_id = paper.get('arxiv_id', '')
            if arxiv_id and arxiv_id in existing_arxiv:
                matched_file = existing_arxiv[arxiv_id]
            else:
                # Try extracting from URL
                url = paper.get('url', '')
                aid = extract_arxiv_id_from_url(url)
                if aid and aid in existing_arxiv:
                    matched_file = existing_arxiv[aid]

        # Check title overlap
        if not matched_file:
            paper_title = paper.get('title', '')
            for existing_title, existing_file in existing_titles:
                if title_word_overlap(paper_title, existing_title) >= 0.85:
                    matched_file = existing_file
                    break

        if matched_file:
            paper['matched_vault_file'] = matched_file
            already_in_vault.append(paper)
        else:
            truly_new.append(paper)

    print(f"  Cross-reference: {len(truly_new)} new, {len(already_in_vault)} already in vault")
    return truly_new, already_in_vault


def write_master_list_json(new_papers, already_in_vault, reports):
    """Write the structured master list JSON."""
    output = {
        'date': DATE_PREFIX,
        'search_type': 'culture/nationality benchmark search',
        'total_agents': len(reports),
        'total_papers_found': len(new_papers) + len(already_in_vault),
        'truly_new': len(new_papers),
        'already_in_vault': len(already_in_vault),
        'new_papers': new_papers,
        'already_in_vault_papers': already_in_vault,
        'agent_summaries': [
            {
                'agent_id': r.get('agent_id', '?'),
                'cultures': r.get('cultures', []),
                'total_found': r.get('total_found', 0),
            }
            for r in reports
        ],
    }
    outpath = LOGS_DIR / f"{DATE_PREFIX}-culture_search_master_list.json"
    outpath.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"  Written: {outpath.name}")
    return outpath


def write_master_list_md(new_papers, already_in_vault, reports):
    """Write the human-readable master list markdown."""
    lines = []
    lines.append(f"# Culture/Nationality Search Master List \u2014 {DATE_PREFIX}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Agents:** {len(reports)}")
    lines.append(f"- **Total papers found:** {len(new_papers) + len(already_in_vault)}")
    lines.append(f"- **Truly new (not in vault):** {len(new_papers)}")
    lines.append(f"- **Already in vault:** {len(already_in_vault)}")
    lines.append("")

    # Agent summary table
    lines.append("## Agent Summary")
    lines.append("")
    lines.append("| Agent | Cultures | Papers Found |")
    lines.append("|-------|----------|-------------|")
    for r in reports:
        cultures = ", ".join(r.get('cultures', []))
        lines.append(f"| {r.get('agent_id', '?')} | {cultures} | {r.get('total_found', 0)} |")
    lines.append("")

    # New papers
    lines.append("## New Papers to Import")
    lines.append("")
    for i, paper in enumerate(new_papers, 1):
        title = paper.get('title', 'Untitled')
        authors = paper.get('authors', 'Unknown')
        year = paper.get('year', '????')
        url = paper.get('url', '')
        arxiv_id = paper.get('arxiv_id', '')
        doi = paper.get('doi', '')
        cultures = paper.get('cultures_covered', [])
        if isinstance(cultures, list):
            cultures = ", ".join(cultures)
        benchmark = paper.get('benchmark_name', '')
        snippet = paper.get('abstract_snippet', '')
        data_url = paper.get('data_url', '')
        source_agents = paper.get('source_agents', [])
        if isinstance(source_agents, list):
            source_agents = ", ".join(source_agents)

        lines.append(f"### {i}. {title}")
        lines.append(f"- **Authors:** {authors}")
        lines.append(f"- **Year:** {year}")
        if arxiv_id:
            lines.append(f"- **arXiv:** [{arxiv_id}](https://arxiv.org/abs/{arxiv_id})")
        if doi:
            lines.append(f"- **DOI:** [{doi}](https://doi.org/{doi})")
        if url:
            lines.append(f"- **URL:** {url}")
        lines.append(f"- **Cultures:** {cultures}")
        if benchmark:
            lines.append(f"- **Benchmark:** {benchmark}")
        if data_url:
            lines.append(f"- **Code/Data:** {data_url}")
        if snippet:
            lines.append(f"- **Abstract:** {snippet}")
        lines.append(f"- **Source Agent(s):** {source_agents}")
        lines.append("")

    # Already in vault (summary only)
    if already_in_vault:
        lines.append("## Already in Vault (skipped)")
        lines.append("")
        lines.append("| Title | Matched File | Cultures |")
        lines.append("|-------|-------------|----------|")
        for paper in already_in_vault:
            title = paper.get('title', 'Untitled')[:60]
            matched = paper.get('matched_vault_file', '?')
            cultures = paper.get('cultures_covered', [])
            if isinstance(cultures, list):
                cultures = ", ".join(cultures)
            lines.append(f"| {title} | {matched} | {cultures} |")
        lines.append("")

    outpath = LOGS_DIR / f"{DATE_PREFIX}-culture_search_master_list.md"
    outpath.write_text("\n".join(lines), encoding='utf-8')
    print(f"  Written: {outpath.name}")
    return outpath


def main():
    print("=" * 60)
    print("CONSOLIDATE CULTURE/NATIONALITY SEARCH AGENT REPORTS")
    print("=" * 60)
    print()

    # 1. Load agent reports
    print("[1/5] Loading agent reports...")
    reports = load_agent_reports()
    if not reports:
        print("  ERROR: No agent reports found matching pattern:", AGENT_REPORT_PATTERN)
        sys.exit(1)
    print(f"  Loaded {len(reports)} reports")
    print()

    # 2. Merge all papers into flat list
    print("[2/5] Merging papers from all agents...")
    all_papers = merge_papers(reports)
    print(f"  Total papers before dedup: {len(all_papers)}")
    print()

    # 3. Deduplicate within new results
    print("[3/5] Deduplicating within new results...")
    deduped = deduplicate_new_papers(all_papers)
    print()

    # 4. Cross-reference against existing vault
    print("[4/5] Loading existing vault papers for cross-reference...")
    existing = load_existing_papers()
    print(f"  Loaded {len(existing)} existing papers")
    truly_new, already_in_vault = cross_reference(deduped, existing)
    print()

    # 5. Write output
    print("[5/5] Writing master lists...")
    write_master_list_json(truly_new, already_in_vault, reports)
    write_master_list_md(truly_new, already_in_vault, reports)
    print()

    # Summary
    print("=" * 60)
    print("CONSOLIDATION SUMMARY")
    print(f"  Agent reports loaded:    {len(reports)}")
    print(f"  Total papers found:      {len(all_papers)}")
    print(f"  After internal dedup:    {len(deduped)}")
    print(f"  Already in vault:        {len(already_in_vault)}")
    print(f"  Truly new papers:        {len(truly_new)}")
    print("=" * 60)

    # Culture coverage breakdown
    culture_counts = defaultdict(int)
    for paper in truly_new:
        cultures = paper.get('cultures_covered', [])
        if isinstance(cultures, list):
            for c in cultures:
                culture_counts[c] += 1
        elif isinstance(cultures, str):
            for c in cultures.split(','):
                culture_counts[c.strip()] += 1

    if culture_counts:
        print("\nCulture coverage of new papers:")
        for culture, count in sorted(culture_counts.items(), key=lambda x: -x[1]):
            print(f"  {culture}: {count}")


if __name__ == '__main__':
    main()
