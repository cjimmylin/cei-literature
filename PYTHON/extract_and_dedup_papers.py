#!/usr/bin/env python3
"""
Extract papers from all 13 agent reports and deduplicate them.
Produces MASTER_PAPER_LIST_2026_02_07.md in the logs directory.

Created: 2026-02-07, Session 34 (Deduplication)
Usage: python3 PYTHON/extract_and_dedup_papers.py
  (run from CEI-Lit-WS/ directory)

This script was used to deduplicate ~292 raw papers from 13 exhaustive
literature search agent reports into 251 unique papers. It can be re-run
if Agent 1 (citation graph) results need to be incorporated — just add
the new report file to REPORT_FILES and re-run.

Key design decisions:
- DOI regex MUST validate 10.XXXX/ prefix to avoid markdown ** false matches
- arXiv regex handles 3 formats: arXiv:ID, arXiv ID: ID, [ID](url)
- Index sync: when paper A is merged into B by title, arXiv/DOI indexes
  must be updated to point to B, not A (zombie reference prevention)
- Fuzzy title threshold: 0.90 general, 0.95 for short titles (<20 chars)
"""

import re
import os
from collections import defaultdict
from difflib import SequenceMatcher

LOGS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")

REPORT_FILES = [
    ("Agent 2", "AGENT2_ACL_ANTHOLOGY_SEARCH_2026_02_07.md"),
    ("Agent 3", "Agent3_AIES_FAccT_Proceedings_Mining_Report.md"),
    ("Agent 4", "Agent4_Workshop_Proceedings_Report.md"),
    ("Agent 5", "Agent5_PapersWithCode_HuggingFace_Report.md"),
    ("Agent 6", "Agent6_PhilPapers_Philosophy_Report.md"),
    ("Agent 7-8", "Agent7_8_AuthorNetwork_GitHub_Report.md"),
    ("Agent 9-11", "Agent9_11_NonWestern_Ethics_Report.md"),
    ("Agent 12-13", "Agent12_13_EastAsian_Multilingual_Report.md"),
    ("Agent 14", "Agent14_Professional_Ethics_Report.md"),
    ("Agent 15", "Agent15_Prosocial_Empathy_Report.md"),
    ("Agent 16", "Agent16_Safety_RedTeaming_Report.md"),
    ("Agent 17", "Agent17_Political_Values_Report.md"),
    ("Agent 18", "Agent18_GameTheory_Persuasion_Report.md"),
    ("Agent 19", "Agent19_Moral_Psychology_Report.md"),
]


def normalize_title(title):
    """Normalize a paper title for comparison."""
    t = re.sub(r'[*_`#]', '', title)
    t = re.sub(r'^\s*\(.*?\)\s*', '', t)
    t = t.lower().strip()
    t = re.sub(r'[:\-\u2013\u2014,;.!?\'\"(){}[\]]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def extract_arxiv_id(text):
    """Extract arXiv ID from text."""
    patterns = [
        r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}(?:v\d+)?)',
        r'arXiv(?:\s*(?:ID|/DOI))?[:\s*]*(\d{4}\.\d{4,5}(?:v\d+)?)',
        r'\[(\d{4}\.\d{4,5}(?:v\d+)?)\]\(https?://arxiv',
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            aid = m.group(1)
            aid = re.sub(r'v\d+$', '', aid)
            return aid
    return None


def extract_doi(text):
    """Extract DOI from text. Only returns valid DOI patterns (10.XXXX/...)."""
    patterns = [
        r'(?:https?://doi\.org/)?(10\.\d{4,9}/[^\s\)\]>*]+)',
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            doi = m.group(1).rstrip('.;,')
            if '/' in doi and len(doi) > 10:
                return doi
    return None


def extract_year(text):
    """Extract publication year from citation text."""
    m = re.search(r'\((\d{4})\)', text)
    if m:
        year = int(m.group(1))
        if 2018 <= year <= 2026:
            return str(year)
    m = re.search(r'\b(202[0-6]|201[89])\b', text)
    if m:
        return m.group(1)
    return None


def extract_venue(citation):
    """Extract venue from citation text."""
    venue_patterns = [
        (r'ACL\s*202\d', 'ACL'),
        (r'EMNLP\s*202\d', 'EMNLP'),
        (r'NAACL\s*202\d', 'NAACL'),
        (r'EACL\s*202\d', 'EACL'),
        (r'COLING\s*202\d', 'COLING'),
        (r'LREC-COLING\s*202\d', 'LREC-COLING'),
        (r'NeurIPS\s*202\d', 'NeurIPS'),
        (r'ICML\s*202\d', 'ICML'),
        (r'ICLR\s*202\d', 'ICLR'),
        (r'AIES\s*202\d', 'AIES'),
        (r'FAccT\s*202\d', 'FAccT'),
        (r'EAAMO\s*202\d', 'EAAMO'),
        (r'AAAI\s*202\d', 'AAAI'),
        (r'SIGKDD|KDD', 'KDD'),
        (r'AACL[-\s]?IJCNLP\s*202\d', 'AACL'),
        (r'Findings of.*?ACL', 'Findings of ACL'),
        (r'Findings of.*?EMNLP', 'Findings of EMNLP'),
        (r'Findings of.*?NAACL', 'Findings of NAACL'),
        (r'Scientific Reports', 'Scientific Reports'),
        (r'Nature Machine Intelligence', 'Nature MI'),
        (r'arXiv preprint', 'arXiv'),
        (r'arXiv', 'arXiv'),
        (r'PNAS', 'PNAS'),
        (r'Datasets?\s*(?:and|&)\s*Benchmarks?\s*Track', 'NeurIPS D&B'),
        (r'CHI\s*202\d', 'CHI'),
        (r'CSCW\s*202\d', 'CSCW'),
        (r'TACL', 'TACL'),
    ]
    for pat, venue in venue_patterns:
        if re.search(pat, citation, re.IGNORECASE):
            m = re.search(r'(' + pat + r')', citation, re.IGNORECASE)
            if m:
                return m.group(1).strip()
            return venue
    return "Unknown"


def extract_implementation_readiness(text):
    """Extract implementation readiness level."""
    m = re.search(r'(?:Implementation\s+)?Readiness.*?(High|Medium|Low)', text, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    return "UNKNOWN"


def extract_code_urls(text):
    """Extract code/data URLs."""
    urls = []
    for m in re.finditer(r'https?://github\.com/[^\s\)>]+', text):
        urls.append(m.group(0).rstrip('.,;)'))
    for m in re.finditer(r'https?://huggingface\.co/[^\s\)>]+', text):
        urls.append(m.group(0).rstrip('.,;)'))
    return '; '.join(urls) if urls else "None listed"


def extract_dataset_size(text):
    """Extract dataset size information."""
    m = re.search(
        r'\*{0,2}Dataset\s+(?:Size(?:\s*(?:&|and)\s*Format)?|Details)\s*\*{0,2}[:\s]*\**\s*(.*?)(?:\n-\s*\*\*|\n\*\*[A-Z]|\n###|\n##|\Z)',
        text, re.IGNORECASE | re.DOTALL
    )
    if m:
        size_text = m.group(1).strip()
        lines = [l.strip().lstrip('- ') for l in size_text.split('\n') if l.strip()]
        if lines:
            result = lines[0][:200]
            result = re.sub(r'\*{2,}', '', result).strip()
            return result
    return "See report"


def extract_authors_from_citation(citation):
    """Extract first author and 'et al.' from citation."""
    c = re.sub(r'^[-\s]*\**Full Citation\**[:\s]*', '', citation).strip()
    m = re.match(r'([^"(]+?)(?:\s*\(|\s*")', c)
    if m:
        authors = m.group(1).strip().rstrip('.,')
        if len(authors) > 80:
            first = re.split(r',\s*|\s+and\s+', authors)[0]
            return first + " et al."
        return authors
    return "Unknown"


def split_into_paper_blocks(text):
    """Split a report into individual paper blocks."""
    papers = []
    header_patterns = [
        r'^##\s+NEW\s+Finding\s+#\d+[:\.]?\s*(.+?)$',       # Agent 5
        r'^###\s+NEW[-\u2013]\d+[:\.]?\s*(.+?)$',            # Agent 7-8
        r'^###\s+(?:Paper\s+)?\d+[\.\d]*\s*[:\.]?\s*(.+?)$', # Agents 2,3,4,6,9-19
    ]

    lines = text.split('\n')
    current_title = None
    current_block = []

    for line in lines:
        matched = False
        for pat in header_patterns:
            m = re.match(pat, line)
            if m:
                if current_title:
                    papers.append((current_title, '\n'.join(current_block)))
                current_title = m.group(1).strip()
                current_block = [line]
                matched = True
                break
        if not matched and current_title:
            current_block.append(line)

    if current_title:
        papers.append((current_title, '\n'.join(current_block)))

    return papers


def extract_papers_from_report(agent_name, filepath):
    """Extract all papers from a single report file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    blocks = split_into_paper_blocks(text)
    papers = []

    for title, block in blocks:
        title_lower = title.lower()
        if any(kw in title_lower for kw in [
            'search strategy', 'summary table', 'methodology', 'dedup',
            'key finding', 'cross-agent', 'notes on', 'table of contents',
            'notable gap', 'gap analysis', 'executive summary', 'overview',
            'recommendations', 'appendix', 'search terms', 'who 2025',
            'engineering ethics', 'business ethics', 'gaps identified',
            'not found', 'no dedicated', 'policy guidelines',
        ]):
            continue

        if not re.search(r'(?:Full\s+Citation|Citation)[:\s]*\**', block, re.IGNORECASE):
            if not (re.search(r'(?:Authors?|Venue)[:\s]*\**', block, re.IGNORECASE) and
                    re.search(r'(?:arXiv|DOI|10\.\d{4})', block, re.IGNORECASE)):
                continue

        arxiv_id = extract_arxiv_id(block)
        doi = extract_doi(block)
        year = extract_year(block)

        citation_match = re.search(r'\*\*Full Citation[:\s]*\**\s*(.*?)(?:\n|$)', block)
        citation = citation_match.group(1).strip() if citation_match else ""

        authors = extract_authors_from_citation(citation) if citation else "Unknown"
        venue = extract_venue(block)
        readiness = extract_implementation_readiness(block)
        code_urls = extract_code_urls(block)
        dataset_size = extract_dataset_size(block)

        clean_title = re.sub(r'[*_`]', '', title).strip()

        paper = {
            'title': clean_title,
            'authors': authors,
            'year': year or 'Unknown',
            'venue': venue,
            'arxiv_id': arxiv_id,
            'doi': doi,
            'dataset_size': dataset_size,
            'code_urls': code_urls,
            'readiness': readiness,
            'source_agents': [agent_name],
            'citation': citation,
        }
        papers.append(paper)

    return papers


def fuzzy_title_match(t1, t2, threshold=0.90):
    """Check if two normalized titles are similar enough to be duplicates."""
    if not t1 or not t2:
        return False
    if len(t1) < 20 or len(t2) < 20:
        threshold = 0.95
    len_ratio = min(len(t1), len(t2)) / max(len(t1), len(t2))
    if len_ratio < 0.6:
        return False
    ratio = SequenceMatcher(None, t1, t2).ratio()
    return ratio >= threshold


def merge_paper(existing, new):
    """Merge new paper data into existing paper entry."""
    for agent in new['source_agents']:
        if agent not in existing['source_agents']:
            existing['source_agents'].append(agent)

    if not existing['arxiv_id'] and new['arxiv_id']:
        existing['arxiv_id'] = new['arxiv_id']
    if not existing['doi'] and new['doi']:
        existing['doi'] = new['doi']
    if existing['year'] == 'Unknown' and new['year'] != 'Unknown':
        existing['year'] = new['year']
    if existing['venue'] == 'Unknown' and new['venue'] != 'Unknown':
        existing['venue'] = new['venue']
    if existing['authors'] == 'Unknown' and new['authors'] != 'Unknown':
        existing['authors'] = new['authors']
    if existing['code_urls'] == 'None listed' and new['code_urls'] != 'None listed':
        existing['code_urls'] = new['code_urls']
    if existing['readiness'] == 'UNKNOWN' and new['readiness'] != 'UNKNOWN':
        existing['readiness'] = new['readiness']
    if not existing['citation'] and new['citation']:
        existing['citation'] = new['citation']


def deduplicate_papers(all_papers):
    """Deduplicate papers by arXiv ID, DOI, then fuzzy title match."""
    arxiv_index = {}
    doi_index = {}
    unique_papers = []
    merge_log = []

    def update_indexes(canonical, new_paper):
        if canonical.get('arxiv_id'):
            arxiv_index[canonical['arxiv_id']] = canonical
        if new_paper.get('arxiv_id'):
            arxiv_index[new_paper['arxiv_id']] = canonical
        if canonical.get('doi'):
            doi_index[canonical['doi']] = canonical
        if new_paper.get('doi'):
            doi_index[new_paper['doi']] = canonical

    for paper in all_papers:
        merged = False
        agent = paper['source_agents'][0]

        if paper['arxiv_id']:
            if paper['arxiv_id'] in arxiv_index:
                existing = arxiv_index[paper['arxiv_id']]
                merge_log.append(f"  ARXIV: '{paper['title']}' ({agent}) -> '{existing['title']}'")
                merge_paper(existing, paper)
                update_indexes(existing, paper)
                merged = True

        if not merged and paper['doi']:
            if paper['doi'] in doi_index:
                existing = doi_index[paper['doi']]
                merge_log.append(f"  DOI: '{paper['title']}' ({agent}) -> '{existing['title']}'")
                merge_paper(existing, paper)
                update_indexes(existing, paper)
                merged = True

        if not merged:
            norm_title = normalize_title(paper['title'])
            found_match = False
            for existing in unique_papers:
                existing_norm = normalize_title(existing['title'])
                if fuzzy_title_match(norm_title, existing_norm):
                    ratio = SequenceMatcher(None, norm_title, existing_norm).ratio()
                    merge_log.append(f"  TITLE ({ratio:.2f}): '{paper['title']}' ({agent}) -> '{existing['title']}'")
                    merge_paper(existing, paper)
                    update_indexes(existing, paper)
                    found_match = True
                    break

            if not found_match:
                unique_papers.append(paper)
                if paper['arxiv_id']:
                    arxiv_index[paper['arxiv_id']] = paper
                if paper['doi']:
                    doi_index[paper['doi']] = paper

    if merge_log:
        print(f"\n=== DEDUP MERGE LOG ({len(merge_log)} merges) ===")
        for entry in merge_log:
            print(entry)

    return unique_papers


def generate_master_list(unique_papers):
    """Generate the master list markdown document."""
    unique_papers.sort(key=lambda p: (-int(p['year']) if p['year'].isdigit() else 0, p['title']))

    readiness_counts = defaultdict(int)
    for p in unique_papers:
        readiness_counts[p['readiness']] += 1

    year_counts = defaultdict(int)
    for p in unique_papers:
        year_counts[p['year']] += 1

    multi_agent = [p for p in unique_papers if len(p['source_agents']) > 1]

    lines = []
    lines.append("# Master Paper List: Ethical Values Alignment Benchmarks & Datasets for LLMs")
    lines.append(f"**Generated:** 2026-02-07")
    lines.append(f"**Source:** 13 agent reports (Agents 2-19, excluding Agent 1)")
    lines.append(f"**Deduplication:** arXiv ID -> DOI -> fuzzy title match (threshold=0.90)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Summary Statistics")
    lines.append("")
    lines.append(f"- **Total unique papers:** {len(unique_papers)}")
    lines.append(f"- **Papers found by multiple agents:** {len(multi_agent)}")
    lines.append(f"- **Implementation Readiness:** HIGH={readiness_counts.get('HIGH',0)}, MEDIUM={readiness_counts.get('MEDIUM',0)}, LOW={readiness_counts.get('LOW',0)}, UNKNOWN={readiness_counts.get('UNKNOWN',0)}")
    lines.append("")
    lines.append("### By Year")
    lines.append("")
    for year in sorted(year_counts.keys(), reverse=True):
        lines.append(f"- {year}: {year_counts[year]}")
    lines.append("")

    lines.append("### Multi-Agent Papers (found by 2+ agents)")
    lines.append("")
    if multi_agent:
        for p in sorted(multi_agent, key=lambda x: len(x['source_agents']), reverse=True):
            lines.append(f"- **{p['title']}** -- {', '.join(p['source_agents'])}")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Complete Paper List")
    lines.append("")

    for i, p in enumerate(unique_papers, 1):
        lines.append(f"### {i}. {p['title']}")
        lines.append("")
        lines.append(f"- **Authors:** {p['authors']}")
        lines.append(f"- **Year:** {p['year']}")
        lines.append(f"- **Venue:** {p['venue']}")
        if p['arxiv_id']:
            lines.append(f"- **arXiv:** [{p['arxiv_id']}](https://arxiv.org/abs/{p['arxiv_id']})")
        if p['doi']:
            lines.append(f"- **DOI:** {p['doi']}")
        lines.append(f"- **Dataset Size:** {p['dataset_size']}")
        lines.append(f"- **Code/Data:** {p['code_urls']}")
        lines.append(f"- **Implementation Readiness:** {p['readiness']}")
        lines.append(f"- **Source Agent(s):** {', '.join(p['source_agents'])}")
        lines.append("")
        lines.append("---")
        lines.append("")

    return '\n'.join(lines)


def main():
    all_papers = []

    for agent_name, filename in REPORT_FILES:
        filepath = os.path.join(LOGS_DIR, filename)
        if not os.path.exists(filepath):
            print(f"WARNING: Missing report file: {filepath}")
            continue

        papers = extract_papers_from_report(agent_name, filepath)
        print(f"{agent_name}: extracted {len(papers)} papers from {filename}")
        all_papers.append((agent_name, papers))

    flat_papers = []
    for agent_name, papers in all_papers:
        flat_papers.extend(papers)

    print(f"\nTotal raw papers extracted: {len(flat_papers)}")

    unique = deduplicate_papers(flat_papers)
    print(f"Unique papers after dedup: {len(unique)}")

    output = generate_master_list(unique)
    output_path = os.path.join(LOGS_DIR, "MASTER_PAPER_LIST_2026_02_07.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"\nMaster list written to: {output_path}")

    multi = [p for p in unique if len(p['source_agents']) > 1]
    print(f"\nPapers found by multiple agents ({len(multi)}):")
    for p in sorted(multi, key=lambda x: len(x['source_agents']), reverse=True):
        print(f"  [{len(p['source_agents'])} agents] {p['title']} -- {', '.join(p['source_agents'])}")

    unknown_by_agent = defaultdict(int)
    for p in unique:
        if p['readiness'] == 'UNKNOWN':
            for a in p['source_agents']:
                unknown_by_agent[a] += 1
    if unknown_by_agent:
        print(f"\nUNKNOWN readiness by source agent:")
        for agent, count in sorted(unknown_by_agent.items()):
            print(f"  {agent}: {count}")


if __name__ == '__main__':
    main()
