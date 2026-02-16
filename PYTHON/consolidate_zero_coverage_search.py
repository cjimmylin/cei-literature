#!/usr/bin/env python3
"""
Consolidate Zero-Coverage Religious Tradition Search Agent Reports

Merges agent JSON reports from the Shinto/Baha'i/Zoroastrian/Indigenous search,
deduplicates within new results, and cross-references against existing vault
papers to produce a master list of truly new papers.

Deduplication order:
  1. DOI match (normalized, excluding arXiv DOIs)
  2. arXiv ID match (with YYMM prefix validation)
  3. Title word-overlap >= 85%

Output:
  - logs/20260216-zero_coverage_search_master_list.json  (structured)
  - logs/20260216-zero_coverage_search_master_list.md     (human-readable)

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/consolidate_zero_coverage_search.py
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
DATE_PREFIX = "20260216"

# Agent report glob pattern
AGENT_REPORT_PATTERN = f"{DATE_PREFIX}-zero_coverage_agent_*.json"

# arXiv ID validation
ARXIV_ID_RE = re.compile(r'(\d{4}\.\d{4,5})')


def _is_valid_arxiv_id(candidate: str) -> bool:
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
    if not title:
        return ""
    t = title.lower()
    t = re.sub(r'[^a-z0-9\s]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def title_word_overlap(title_a: str, title_b: str) -> float:
    words_a = set(normalize_title(title_a).split())
    words_b = set(normalize_title(title_b).split())
    if not words_a or not words_b:
        return 0.0
    intersection = words_a & words_b
    union = words_a | words_b
    return len(intersection) / len(union) if union else 0.0


def load_existing_papers() -> list:
    papers = []
    for p in sorted(PAPERS_DIR.iterdir()):
        if not p.name.endswith('.md'):
            continue
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
    reports = []
    for rp in sorted(LOGS_DIR.glob(AGENT_REPORT_PATTERN)):
        try:
            data = json.loads(rp.read_text(encoding='utf-8'))
            reports.append(data)
            print(f"  Loaded {rp.name}: {len(data.get('papers', []))} papers from agent {data.get('agent_id', '?')}")
        except Exception as e:
            print(f"  ERROR loading {rp.name}: {e}")
    return reports


def merge_papers(reports: list) -> list:
    all_papers = []
    for report in reports:
        agent_id = report.get('agent_id', 'unknown')
        for paper in report.get('papers', []):
            paper['source_agent'] = agent_id
            all_papers.append(paper)
    return all_papers


def deduplicate_new_papers(papers: list) -> list:
    if not papers:
        return []

    doi_groups = defaultdict(list)
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
        url = p.get('url', '')
        aid = extract_arxiv_id_from_url(url)
        if aid:
            arxiv_groups[aid].append(i)

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

    for doi, indices in doi_groups.items():
        for i in range(1, len(indices)):
            union(indices[0], indices[i])

    for aid, indices in arxiv_groups.items():
        for i in range(1, len(indices)):
            union(indices[0], indices[i])

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

    groups = defaultdict(list)
    for i in range(len(papers)):
        groups[find(i)].append(i)

    deduped = []
    merge_count = 0
    for group_indices in groups.values():
        if len(group_indices) > 1:
            merge_count += 1
        best_idx = max(group_indices, key=lambda i: _richness(papers[i]))
        representative = papers[best_idx].copy()
        all_traditions = set()
        all_agents = set()
        for idx in group_indices:
            traditions = papers[idx].get('traditions_covered', [])
            if isinstance(traditions, list):
                all_traditions.update(traditions)
            elif isinstance(traditions, str):
                all_traditions.update(t.strip() for t in traditions.split(','))
            all_agents.add(papers[idx].get('source_agent', ''))
        representative['traditions_covered'] = sorted(all_traditions)
        representative['source_agents'] = sorted(all_agents)
        representative['duplicate_count'] = len(group_indices)
        deduped.append(representative)

    print(f"  Internal dedup: {len(papers)} -> {len(deduped)} ({merge_count} merge groups)")
    return deduped


def _richness(paper: dict) -> int:
    score = 0
    for key in ('title', 'authors', 'year', 'url', 'arxiv_id', 'doi',
                'benchmark_name', 'abstract_snippet', 'data_url', 'relevance_notes',
                'traditions_covered'):
        val = paper.get(key, '')
        if val and str(val).strip() and str(val).strip().lower() not in ('n/a', 'none', ''):
            score += 1
    return score


def cross_reference(new_papers: list, existing_papers: list) -> tuple:
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

        doi = normalize_doi(paper.get('doi', ''))
        if doi and doi in existing_dois:
            matched_file = existing_dois[doi]

        if not matched_file:
            arxiv_id = paper.get('arxiv_id', '')
            if arxiv_id and arxiv_id in existing_arxiv:
                matched_file = existing_arxiv[arxiv_id]
            else:
                url = paper.get('url', '')
                aid = extract_arxiv_id_from_url(url)
                if aid and aid in existing_arxiv:
                    matched_file = existing_arxiv[aid]

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
    output = {
        'date': DATE_PREFIX,
        'search_type': 'zero-coverage religious tradition search',
        'total_agents': len(reports),
        'total_papers_found': len(new_papers) + len(already_in_vault),
        'truly_new': len(new_papers),
        'already_in_vault': len(already_in_vault),
        'new_papers': new_papers,
        'already_in_vault_papers': already_in_vault,
        'agent_summaries': [
            {
                'agent_id': r.get('agent_id', '?'),
                'traditions': r.get('traditions', []),
                'total_found': len(r.get('papers', [])),
            }
            for r in reports
        ],
    }
    outpath = LOGS_DIR / f"{DATE_PREFIX}-zero_coverage_search_master_list.json"
    outpath.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"  Written: {outpath.name}")
    return outpath


def write_master_list_md(new_papers, already_in_vault, reports):
    lines = []
    lines.append(f"# Zero-Coverage Religious Tradition Search Master List \u2014 {DATE_PREFIX}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Agents:** {len(reports)}")
    lines.append(f"- **Total papers found:** {len(new_papers) + len(already_in_vault)}")
    lines.append(f"- **Truly new (not in vault):** {len(new_papers)}")
    lines.append(f"- **Already in vault:** {len(already_in_vault)}")
    lines.append("")

    lines.append("## Agent Summary")
    lines.append("")
    lines.append("| Agent | Traditions | Papers Found |")
    lines.append("|-------|-----------|-------------|")
    for r in reports:
        traditions = ", ".join(r.get('traditions', []))
        lines.append(f"| {r.get('agent_id', '?')} | {traditions} | {len(r.get('papers', []))} |")
    lines.append("")

    lines.append("## New Papers to Import")
    lines.append("")
    for i, paper in enumerate(new_papers, 1):
        title = paper.get('title', 'Untitled')
        authors = paper.get('authors', 'Unknown')
        year = paper.get('year', '????')
        url = paper.get('url', '')
        arxiv_id = paper.get('arxiv_id', '')
        doi = paper.get('doi', '')
        traditions = paper.get('traditions_covered', [])
        if isinstance(traditions, list):
            traditions = ", ".join(traditions)
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
        lines.append(f"- **Traditions:** {traditions}")
        if benchmark:
            lines.append(f"- **Benchmark:** {benchmark}")
        if data_url:
            lines.append(f"- **Code/Data:** {data_url}")
        if snippet:
            lines.append(f"- **Abstract:** {snippet}")
        lines.append(f"- **Source Agent(s):** {source_agents}")
        lines.append("")

    if already_in_vault:
        lines.append("## Already in Vault (skipped)")
        lines.append("")
        lines.append("| Title | Matched File | Traditions |")
        lines.append("|-------|-------------|-----------|")
        for paper in already_in_vault:
            title = paper.get('title', 'Untitled')[:60]
            matched = paper.get('matched_vault_file', '?')
            traditions = paper.get('traditions_covered', [])
            if isinstance(traditions, list):
                traditions = ", ".join(traditions)
            lines.append(f"| {title} | {matched} | {traditions} |")
        lines.append("")

    outpath = LOGS_DIR / f"{DATE_PREFIX}-zero_coverage_search_master_list.md"
    outpath.write_text("\n".join(lines), encoding='utf-8')
    print(f"  Written: {outpath.name}")
    return outpath


def main():
    print("=" * 60)
    print("CONSOLIDATE ZERO-COVERAGE RELIGIOUS TRADITION SEARCH")
    print("=" * 60)
    print()

    print("[1/5] Loading agent reports...")
    reports = load_agent_reports()
    if not reports:
        print("  ERROR: No agent reports found matching pattern:", AGENT_REPORT_PATTERN)
        sys.exit(1)
    print(f"  Loaded {len(reports)} reports")
    print()

    print("[2/5] Merging papers from all agents...")
    all_papers = merge_papers(reports)
    print(f"  Total papers before dedup: {len(all_papers)}")
    print()

    print("[3/5] Deduplicating within new results...")
    deduped = deduplicate_new_papers(all_papers)
    print()

    print("[4/5] Loading existing vault papers for cross-reference...")
    existing = load_existing_papers()
    print(f"  Loaded {len(existing)} existing papers")
    truly_new, already_in_vault = cross_reference(deduped, existing)
    print()

    print("[5/5] Writing master lists...")
    write_master_list_json(truly_new, already_in_vault, reports)
    write_master_list_md(truly_new, already_in_vault, reports)
    print()

    print("=" * 60)
    print("CONSOLIDATION SUMMARY")
    print(f"  Agent reports loaded:    {len(reports)}")
    print(f"  Total papers found:      {len(all_papers)}")
    print(f"  After internal dedup:    {len(deduped)}")
    print(f"  Already in vault:        {len(already_in_vault)}")
    print(f"  Truly new papers:        {len(truly_new)}")
    print("=" * 60)

    tradition_counts = defaultdict(int)
    for paper in truly_new:
        traditions = paper.get('traditions_covered', [])
        if isinstance(traditions, list):
            for t in traditions:
                tradition_counts[t] += 1
        elif isinstance(traditions, str):
            for t in traditions.split(','):
                tradition_counts[t.strip()] += 1

    if tradition_counts:
        print("\nTradition coverage of new papers:")
        for tradition, count in sorted(tradition_counts.items(), key=lambda x: -x[1]):
            print(f"  {tradition}: {count}")


if __name__ == '__main__':
    main()
