#!/usr/bin/env python3
"""
Consolidate Religious & Language Search Results

Parses R-agent markdown reports and A-agent JSON files, normalizes to a
unified schema, deduplicates within candidates and against the vault,
applies QC filters, and produces a master candidate list for import.

Inputs:
  - logs/20260213-AgentR*_Report.md   (10 markdown files)
  - logs/20260213-language_search_agent_A*.json  (5 JSON files)
  - logs/20260213-vault_dedup_reference.txt  (846 existing papers)

Outputs:
  - logs/20260213-religious_language_master_list.json   (structured)
  - logs/20260213-religious_language_master_list.md     (human-readable)
  - logs/20260213-religious_language_dedup_log.json     (audit trail)

Usage:
    python consolidate_religious_language_search.py [--dry-run]
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

LOGS_DIR = WORKSPACE_ROOT / "logs"


# ============================================================
# Identifier Extraction & Normalization (from detect_duplicates.py)
# ============================================================

ARXIV_ID_RE = re.compile(r'(\d{4}\.\d{4,5})')


def _is_valid_arxiv_id(candidate: str) -> bool:
    """Validate that a candidate arXiv ID has a plausible YYMM prefix."""
    yymm = candidate.split(".")[0]
    yy = int(yymm[:2])
    mm = int(yymm[2:])
    return 7 <= yy <= 26 and 1 <= mm <= 12


def normalize_doi(doi_str: str) -> Optional[str]:
    """Normalize DOI: lowercase, strip URL prefix, skip N/A and arXiv DOIs."""
    if not doi_str or str(doi_str).strip().upper() in ("N/A", "", "NONE"):
        return None
    doi = str(doi_str).strip().lower()
    doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    doi = doi.replace("https://dx.doi.org/", "").replace("http://dx.doi.org/", "")
    doi = doi.strip('"').strip("'").strip()
    # Skip arXiv DOIs
    if doi.startswith("10.48550/arxiv"):
        return None
    return doi if doi else None


def extract_arxiv_id_from_str(value: str) -> Optional[str]:
    """Extract arXiv ID from a URL or field value."""
    if not value:
        return None
    value_lower = value.lower()
    if "arxiv.org" in value_lower or "10.48550" in value_lower:
        m = ARXIV_ID_RE.search(value)
        if m and _is_valid_arxiv_id(m.group(1)):
            return m.group(1)
    return None


def normalize_arxiv_id(raw: str) -> Optional[str]:
    """Clean raw arXiv ID string (may be 'N/A' or URL or bare ID)."""
    if not raw or str(raw).strip().upper() in ("N/A", "", "NONE"):
        return None
    raw = str(raw).strip()
    # If it looks like a bare ID already
    m = ARXIV_ID_RE.search(raw)
    if m and _is_valid_arxiv_id(m.group(1)):
        return m.group(1)
    return None


def normalize_title(title: str) -> str:
    """Normalize title for comparison: lowercase, strip punctuation, collapse spaces."""
    t = title.lower().strip()
    t = re.sub(r'[^\w\s]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def title_word_overlap(t1: str, t2: str) -> float:
    """Compute word overlap ratio between two normalized titles."""
    words1 = set(normalize_title(t1).split())
    words2 = set(normalize_title(t2).split())
    if not words1 or not words2:
        return 0.0
    intersection = words1 & words2
    min_len = min(len(words1), len(words2))
    return len(intersection) / min_len if min_len > 0 else 0.0


# ============================================================
# Union-Find for Dedup Grouping
# ============================================================

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1


# ============================================================
# R-Agent Markdown Parser
# ============================================================

def parse_r_agent_report(filepath: Path) -> list[dict]:
    """Parse an R-agent markdown report into structured entries."""
    text = filepath.read_text(encoding="utf-8")

    # Extract agent name from header
    agent_match = re.search(r'\*\*Agent:\*\*\s*(\S+)', text)
    agent_id = agent_match.group(1) if agent_match else filepath.stem

    entries = []
    # Split on entry headers: ### N. Title
    entry_pattern = re.compile(r'^### (\d+)\.\s+(.+)$', re.MULTILINE)
    matches = list(entry_pattern.finditer(text))

    for i, m in enumerate(matches):
        entry_num = int(m.group(1))
        title = m.group(2).strip()

        # Extract block text between this entry and the next (or end)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]

        # Parse structured fields
        def get_field(name: str) -> str:
            pattern = rf'- \*\*{re.escape(name)}:\*\*\s*(.+?)(?:\n|$)'
            fm = re.search(pattern, block)
            return fm.group(1).strip() if fm else ""

        authors_raw = get_field("Authors")
        year_raw = get_field("Year")
        venue = get_field("Venue")
        arxiv_raw = get_field("arXiv")
        doi_raw = get_field("DOI")
        traditions = get_field("Religious Traditions")
        paper_type = get_field("Paper Type")
        dataset_size = get_field("Dataset Size")
        languages = get_field("Languages")
        llms_tested = get_field("LLMs Tested")
        code_data = get_field("Code/Data")
        readiness = get_field("Implementation Readiness")
        source_agents = get_field("Source Agent(s)")

        # Extract description paragraph (text after last field line, before ---)
        # Find the last "- **...**" line
        field_lines = list(re.finditer(r'^- \*\*.+?\*\*.*$', block, re.MULTILINE))
        if field_lines:
            desc_start = field_lines[-1].end()
        else:
            desc_start = 0
        # Find the next --- separator
        sep_match = re.search(r'^---', block[desc_start:], re.MULTILINE)
        if sep_match:
            description = block[desc_start:desc_start + sep_match.start()].strip()
        else:
            description = block[desc_start:].strip()
        # Also try "**Summary:**" prefix
        description = re.sub(r'^\*\*Summary:\*\*\s*', '', description)

        # Build URL from arXiv if no explicit URL
        url = ""
        arxiv_id = normalize_arxiv_id(arxiv_raw)
        if arxiv_id:
            url = f"https://arxiv.org/abs/{arxiv_id}"

        entry = {
            "title": title,
            "authors": authors_raw,
            "year": int(year_raw) if year_raw.isdigit() else 0,
            "venue": venue,
            "arxiv_id": arxiv_id or "",
            "doi": doi_raw if doi_raw and doi_raw.upper() != "N/A" else "",
            "url": url,
            "religious_traditions": traditions,
            "paper_type": paper_type,
            "dataset_size": dataset_size,
            "languages": languages,
            "llms_tested": llms_tested,
            "code_data_url": code_data if code_data and code_data.upper() != "N/A" else "",
            "implementation_readiness": readiness.upper() if readiness else "MEDIUM",
            "description": description,
            "source_agents": [source_agents if source_agents else agent_id],
            "benchmark_name": "",
            "source_type": "R-agent",
        }

        # Try to extract benchmark name from title or description
        # Common patterns: "(...BenchmarkName)", title contains benchmark name
        bench_match = re.search(r'\(([A-Z][A-Za-z0-9_-]+)\)\s*$', title)
        if bench_match:
            entry["benchmark_name"] = bench_match.group(1)

        entries.append(entry)

    print(f"  Parsed {len(entries)} entries from {filepath.name}")
    return entries


# ============================================================
# A-Agent JSON Parser
# ============================================================

def parse_a_agent_json(filepath: Path) -> list[dict]:
    """Parse an A-agent JSON file into structured entries."""
    data = json.loads(filepath.read_text(encoding="utf-8"))
    agent_id = data.get("agent_id", filepath.stem)
    languages_focus = data.get("languages", [])
    papers = data.get("papers_found", [])

    entries = []
    for p in papers:
        title = p.get("title", "").strip()
        if not title:
            continue

        # Normalize authors
        authors_raw = p.get("authors", [])
        if isinstance(authors_raw, list):
            authors_str = "; ".join(str(a) for a in authors_raw)
        else:
            authors_str = str(authors_raw)

        # Clean up "Not fully extracted" author entries
        if "not fully extracted" in authors_str.lower():
            authors_str = ""

        year = p.get("year", 0)
        if isinstance(year, str):
            year = int(year) if year.isdigit() else 0

        arxiv_id = normalize_arxiv_id(p.get("arxiv_id", ""))
        doi = normalize_doi(p.get("doi", ""))

        url = p.get("url", "")
        if not url and arxiv_id:
            url = f"https://arxiv.org/abs/{arxiv_id}"

        languages_covered = p.get("languages_covered", [])
        if isinstance(languages_covered, list):
            languages_str = ", ".join(languages_covered)
        else:
            languages_str = str(languages_covered)

        # Build description from abstract_snippet + relevance_notes
        desc_parts = []
        if p.get("abstract_snippet"):
            desc_parts.append(p["abstract_snippet"])
        if p.get("relevance_notes"):
            desc_parts.append(p["relevance_notes"])
        description = " ".join(desc_parts)

        readiness = str(p.get("implementation_readiness", "MEDIUM")).upper()
        if readiness not in ("HIGH", "MEDIUM", "LOW"):
            readiness = "MEDIUM"

        entry = {
            "title": title,
            "authors": authors_str,
            "year": year,
            "venue": p.get("source", ""),
            "arxiv_id": arxiv_id or "",
            "doi": doi or "",
            "url": url,
            "religious_traditions": "",
            "paper_type": "",
            "dataset_size": "",
            "languages": languages_str,
            "llms_tested": "",
            "code_data_url": p.get("data_url", "") or "",
            "implementation_readiness": readiness,
            "description": description,
            "source_agents": [f"A{agent_id}" if not agent_id.startswith("A") else agent_id],
            "benchmark_name": p.get("benchmark_name", "") or "",
            "source_type": "A-agent",
        }
        entries.append(entry)

    print(f"  Parsed {len(entries)} entries from {filepath.name}")
    return entries


# ============================================================
# Vault Reference Loader
# ============================================================

def load_vault_reference(filepath: Path) -> list[dict]:
    """Load vault dedup reference file."""
    entries = []
    for line in filepath.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line.strip():
            continue
        parts = line.split(" ||| ")
        if len(parts) != 3:
            continue
        title, doi, arxiv_id = [p.strip() for p in parts]
        entries.append({
            "title": title,
            "doi": normalize_doi(doi) or "",
            "arxiv_id": normalize_arxiv_id(arxiv_id) or "",
        })
    print(f"  Loaded {len(entries)} vault reference entries")
    return entries


# ============================================================
# QC Filters
# ============================================================

# Keywords that suggest pure NLP infrastructure without values/ethics focus
NLP_INFRA_KEYWORDS = [
    "machine translation", "part-of-speech", "pos tagging", "dependency parsing",
    "named entity recognition", "speech recognition", "text-to-speech",
    "language identification", "spell check", "grammar check",
    "word embedding", "tokenizer", "tokenization",
]

# Keywords that indicate values/ethics/cultural relevance
VALUES_KEYWORDS = [
    "ethic", "moral", "value", "bias", "fairness", "stereotype", "toxic",
    "hate speech", "cultural", "religious", "alignment", "safety",
    "discrimination", "prejudice", "offensive", "sentiment",
    "ubuntu", "confucian", "buddhis", "hindu", "islam", "christian",
    "jewish", "indigenous", "decolonial", "communitarian",
]


def is_pure_nlp_infrastructure(entry: dict) -> bool:
    """Check if a paper is pure NLP infrastructure without values/ethics focus."""
    text = (entry.get("title", "") + " " + entry.get("description", "")).lower()

    # If it has values/ethics keywords, keep it regardless
    for kw in VALUES_KEYWORDS:
        if kw in text:
            return False

    # Check for NLP infrastructure keywords
    for kw in NLP_INFRA_KEYWORDS:
        if kw in text:
            return True

    return False


def apply_qc_filters(entries: list[dict]) -> tuple[list[dict], list[dict]]:
    """Apply QC filters, return (approved, excluded) lists."""
    approved = []
    excluded = []

    for entry in entries:
        readiness = entry.get("implementation_readiness", "MEDIUM").upper()

        # Filter 1: Exclude LOW readiness
        if readiness == "LOW":
            entry["exclude_reason"] = "LOW implementation readiness"
            excluded.append(entry)
            continue

        # Filter 2: Exclude pure NLP infrastructure (A-agent only)
        if entry.get("source_type") == "A-agent" and is_pure_nlp_infrastructure(entry):
            entry["exclude_reason"] = "Pure NLP infrastructure without values/ethics component"
            excluded.append(entry)
            continue

        # Filter 3: Flag missing data for review (but don't exclude)
        if not entry.get("authors") or entry.get("authors", "").lower() in ("unknown", ""):
            entry["review_flag"] = "Missing authors"
        if not entry.get("url") and not entry.get("arxiv_id") and not entry.get("doi"):
            entry["review_flag"] = "No URL/DOI/arXiv ID"

        approved.append(entry)

    return approved, excluded


# ============================================================
# Dedup Engine
# ============================================================

def dedup_candidates(entries: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Deduplicate candidates against each other using 3-tier matching.
    Returns (unique entries, duplicate log entries).
    """
    n = len(entries)
    uf = UnionFind(n)
    dedup_log = []

    # Build indexes
    doi_index = defaultdict(list)
    arxiv_index = defaultdict(list)

    for i, e in enumerate(entries):
        doi = normalize_doi(e.get("doi", ""))
        if doi:
            doi_index[doi].append(i)
        arxiv_id = e.get("arxiv_id", "")
        if arxiv_id:
            arxiv_index[arxiv_id].append(i)

    # Tier 1: DOI match
    for doi, indices in doi_index.items():
        for j in range(1, len(indices)):
            a, b = indices[0], indices[j]
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
                dedup_log.append({
                    "tier": "DOI",
                    "match_value": doi,
                    "entries": [entries[a]["title"], entries[b]["title"]],
                    "sources": [entries[a]["source_agents"], entries[b]["source_agents"]],
                })

    # Tier 2: arXiv ID match
    for arxiv_id, indices in arxiv_index.items():
        for j in range(1, len(indices)):
            a, b = indices[0], indices[j]
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
                dedup_log.append({
                    "tier": "arXiv",
                    "match_value": arxiv_id,
                    "entries": [entries[a]["title"], entries[b]["title"]],
                    "sources": [entries[a]["source_agents"], entries[b]["source_agents"]],
                })

    # Tier 3: Title word overlap >= 85%
    for i in range(n):
        for j in range(i + 1, n):
            if uf.find(i) == uf.find(j):
                continue  # Already grouped
            overlap = title_word_overlap(entries[i]["title"], entries[j]["title"])
            if overlap >= 0.85:
                uf.union(i, j)
                dedup_log.append({
                    "tier": "title_overlap",
                    "match_value": f"{overlap:.2f}",
                    "entries": [entries[i]["title"], entries[j]["title"]],
                    "sources": [entries[i]["source_agents"], entries[j]["source_agents"]],
                })

    # Group entries and pick richest
    groups = defaultdict(list)
    for i in range(n):
        groups[uf.find(i)].append(i)

    unique = []
    for root, indices in groups.items():
        if len(indices) == 1:
            unique.append(entries[indices[0]])
        else:
            # Pick the richest entry (most metadata)
            best_idx = max(indices, key=lambda i: _richness_score(entries[i]))
            best = entries[best_idx].copy()
            # Merge source_agents from all entries
            all_agents = []
            for idx in indices:
                for a in entries[idx].get("source_agents", []):
                    if a not in all_agents:
                        all_agents.append(a)
            best["source_agents"] = all_agents
            # Merge fields from other entries if best is missing them
            for idx in indices:
                if idx == best_idx:
                    continue
                other = entries[idx]
                for field in ("authors", "doi", "arxiv_id", "url", "code_data_url",
                              "religious_traditions", "benchmark_name", "languages",
                              "description", "llms_tested"):
                    if not best.get(field) and other.get(field):
                        best[field] = other[field]
            unique.append(best)

    return unique, dedup_log


def _richness_score(entry: dict) -> int:
    """Score how rich/complete a candidate's metadata is."""
    score = 0
    if entry.get("authors"):
        score += 2
    if entry.get("doi"):
        score += 2
    if entry.get("arxiv_id"):
        score += 2
    if entry.get("url"):
        score += 1
    if entry.get("code_data_url"):
        score += 2
    if entry.get("description") and len(entry["description"]) > 50:
        score += 1
    if entry.get("benchmark_name"):
        score += 1
    if entry.get("religious_traditions"):
        score += 1
    if entry.get("llms_tested"):
        score += 1
    if entry.get("implementation_readiness") == "HIGH":
        score += 1
    return score


def dedup_against_vault(entries: list[dict], vault: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Check candidates against vault reference.
    Returns (new entries, already-in-vault entries).
    """
    vault_dois = set()
    vault_arxiv = set()
    vault_titles = []

    for v in vault:
        if v["doi"]:
            vault_dois.add(v["doi"])
        if v["arxiv_id"]:
            vault_arxiv.add(v["arxiv_id"])
        vault_titles.append(normalize_title(v["title"]))

    new_entries = []
    existing = []

    for entry in entries:
        matched = False
        match_reason = ""

        # Check DOI
        doi = normalize_doi(entry.get("doi", ""))
        if doi and doi in vault_dois:
            matched = True
            match_reason = f"DOI match: {doi}"

        # Check arXiv ID
        if not matched and entry.get("arxiv_id"):
            if entry["arxiv_id"] in vault_arxiv:
                matched = True
                match_reason = f"arXiv match: {entry['arxiv_id']}"

        # Check title overlap
        if not matched:
            entry_title_norm = normalize_title(entry["title"])
            for vt in vault_titles:
                if title_word_overlap(entry["title"], vt) >= 0.85:
                    matched = True
                    match_reason = f"Title match: '{vt[:60]}...'"
                    break

        if matched:
            entry["vault_match_reason"] = match_reason
            existing.append(entry)
        else:
            new_entries.append(entry)

    return new_entries, existing


# ============================================================
# Report Generation
# ============================================================

def generate_markdown_report(
    approved: list[dict],
    excluded_qc: list[dict],
    dedup_internal: list[dict],
    existing_vault: list[dict],
    raw_r_count: int,
    raw_a_count: int,
) -> str:
    """Generate a human-readable markdown report."""
    lines = [
        "# Religious & Language Search — Consolidated Master List",
        "",
        f"**Generated:** 2026-02-13",
        f"**Raw candidates:** {raw_r_count} (R-agents) + {raw_a_count} (A-agents) = {raw_r_count + raw_a_count}",
        f"**After internal dedup:** {len(approved) + len(existing_vault)}",
        f"**Already in vault:** {len(existing_vault)}",
        f"**QC excluded:** {len(excluded_qc)}",
        f"**Approved for import:** {len(approved)}",
        "",
        "---",
        "",
    ]

    # Summary by religious tradition
    tradition_counts = defaultdict(int)
    for e in approved:
        traditions = e.get("religious_traditions", "")
        if traditions:
            for t in re.split(r'[,;/]', traditions):
                t = t.strip()
                if t:
                    tradition_counts[t] += 1
        else:
            tradition_counts["(language/cultural - no specific tradition)"] += 1

    lines.append("## Summary by Religious Tradition")
    lines.append("")
    for t, c in sorted(tradition_counts.items(), key=lambda x: -x[1]):
        lines.append(f"- **{t}:** {c}")
    lines.append("")

    # Summary by readiness
    readiness_counts = defaultdict(int)
    for e in approved:
        readiness_counts[e.get("implementation_readiness", "MEDIUM")] += 1
    lines.append("## Summary by Implementation Readiness")
    lines.append("")
    for r in ("HIGH", "MEDIUM"):
        lines.append(f"- **{r}:** {readiness_counts.get(r, 0)}")
    lines.append("")

    # Summary by source type
    r_count = sum(1 for e in approved if e.get("source_type") == "R-agent")
    a_count = sum(1 for e in approved if e.get("source_type") == "A-agent")
    both_count = sum(1 for e in approved if len(e.get("source_agents", [])) > 1)
    lines.append("## Summary by Source")
    lines.append("")
    lines.append(f"- R-agent only: {r_count}")
    lines.append(f"- A-agent only: {a_count}")
    lines.append(f"- Found by multiple agents: {both_count}")
    lines.append("")

    # Year distribution
    year_counts = defaultdict(int)
    for e in approved:
        year_counts[e.get("year", 0)] += 1
    lines.append("## Year Distribution")
    lines.append("")
    for y in sorted(year_counts.keys(), reverse=True):
        if y > 0:
            lines.append(f"- **{y}:** {year_counts[y]}")
    if 0 in year_counts:
        lines.append(f"- **Unknown:** {year_counts[0]}")
    lines.append("")

    # Flagged for review
    flagged = [e for e in approved if e.get("review_flag")]
    if flagged:
        lines.append("## Flagged for Review")
        lines.append("")
        for e in flagged:
            lines.append(f"- **{e['title']}** — {e['review_flag']}")
        lines.append("")

    lines.append("---")
    lines.append("")

    # Full paper list
    lines.append("## Approved Papers")
    lines.append("")
    for i, e in enumerate(approved, 1):
        lines.append(f"### {i}. {e['title']}")
        lines.append(f"- **Authors:** {e.get('authors', 'Unknown')}")
        lines.append(f"- **Year:** {e.get('year', 'Unknown')}")
        if e.get("venue"):
            lines.append(f"- **Venue:** {e['venue']}")
        if e.get("arxiv_id"):
            lines.append(f"- **arXiv:** {e['arxiv_id']}")
        if e.get("doi"):
            lines.append(f"- **DOI:** {e['doi']}")
        if e.get("url"):
            lines.append(f"- **URL:** {e['url']}")
        if e.get("religious_traditions"):
            lines.append(f"- **Religious Traditions:** {e['religious_traditions']}")
        if e.get("languages"):
            lines.append(f"- **Languages:** {e['languages']}")
        if e.get("benchmark_name"):
            lines.append(f"- **Benchmark:** {e['benchmark_name']}")
        lines.append(f"- **Readiness:** {e.get('implementation_readiness', 'MEDIUM')}")
        lines.append(f"- **Source:** {', '.join(e.get('source_agents', []))}")
        if e.get("code_data_url"):
            lines.append(f"- **Code/Data:** {e['code_data_url']}")
        if e.get("review_flag"):
            lines.append(f"- **REVIEW FLAG:** {e['review_flag']}")
        if e.get("description"):
            lines.append(f"")
            lines.append(f"{e['description']}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # QC Excluded section
    if excluded_qc:
        lines.append("## QC-Excluded Papers")
        lines.append("")
        for e in excluded_qc:
            lines.append(f"- **{e['title']}** — {e.get('exclude_reason', 'Unknown reason')} [{', '.join(e.get('source_agents', []))}]")
        lines.append("")

    # Already in vault
    if existing_vault:
        lines.append("## Already in Vault (Skipped)")
        lines.append("")
        for e in existing_vault:
            lines.append(f"- **{e['title']}** — {e.get('vault_match_reason', '')} [{', '.join(e.get('source_agents', []))}]")
        lines.append("")

    return "\n".join(lines)


# ============================================================
# Main
# ============================================================

def main():
    dry_run = "--dry-run" in sys.argv

    print("=" * 60)
    print("Religious & Language Search — Consolidation")
    print("=" * 60)

    # --- Step 1: Parse all sources ---
    print("\n--- Step 1: Parsing R-agent reports ---")
    r_files = sorted(LOGS_DIR.glob("20260213-AgentR*_Report.md"))
    all_r_entries = []
    for f in r_files:
        all_r_entries.extend(parse_r_agent_report(f))
    print(f"  Total R-agent entries: {len(all_r_entries)}")

    print("\n--- Step 2: Parsing A-agent reports ---")
    a_files = sorted(LOGS_DIR.glob("20260213-language_search_agent_A*.json"))
    all_a_entries = []
    for f in a_files:
        all_a_entries.extend(parse_a_agent_json(f))
    print(f"  Total A-agent entries: {len(all_a_entries)}")

    raw_r_count = len(all_r_entries)
    raw_a_count = len(all_a_entries)
    all_entries = all_r_entries + all_a_entries
    print(f"\n  Combined raw total: {len(all_entries)}")

    # --- Step 2: QC Filters ---
    print("\n--- Step 3: Applying QC filters ---")
    filtered, excluded_qc = apply_qc_filters(all_entries)
    print(f"  Approved after QC: {len(filtered)}")
    print(f"  QC excluded: {len(excluded_qc)}")
    for reason, entries in defaultdict(list, {}).items():
        pass
    # Count by reason
    reason_counts = defaultdict(int)
    for e in excluded_qc:
        reason_counts[e.get("exclude_reason", "Unknown")] += 1
    for reason, count in sorted(reason_counts.items()):
        print(f"    - {reason}: {count}")

    # --- Step 3: Internal Dedup ---
    print("\n--- Step 4: Internal dedup (within candidates) ---")
    unique, dedup_internal_log = dedup_candidates(filtered)
    print(f"  After internal dedup: {len(unique)} (removed {len(filtered) - len(unique)} dups)")

    # --- Step 4: Vault Dedup ---
    print("\n--- Step 5: Vault dedup (against 846 existing papers) ---")
    vault_ref_path = LOGS_DIR / "20260213-vault_dedup_reference.txt"
    vault_ref = load_vault_reference(vault_ref_path)
    new_entries, existing_vault = dedup_against_vault(unique, vault_ref)
    print(f"  New (not in vault): {len(new_entries)}")
    print(f"  Already in vault: {len(existing_vault)}")

    # --- Sort approved by year (descending), then title ---
    approved = sorted(new_entries, key=lambda e: (-e.get("year", 0), e.get("title", "")))

    # --- Step 5: Generate outputs ---
    print(f"\n--- Step 6: Generating outputs ---")

    # JSON master list
    master_json_path = LOGS_DIR / "20260213-religious_language_master_list.json"
    # Dedup log
    dedup_log_path = LOGS_DIR / "20260213-religious_language_dedup_log.json"
    # Markdown report
    master_md_path = LOGS_DIR / "20260213-religious_language_master_list.md"

    master_data = {
        "generated": "2026-02-13",
        "raw_r_count": raw_r_count,
        "raw_a_count": raw_a_count,
        "qc_excluded_count": len(excluded_qc),
        "internal_dedup_removed": len(filtered) - len(unique),
        "vault_matches": len(existing_vault),
        "approved_count": len(approved),
        "approved": approved,
        "excluded_qc": excluded_qc,
        "existing_vault": [{"title": e["title"], "vault_match_reason": e.get("vault_match_reason", "")} for e in existing_vault],
    }

    dedup_data = {
        "generated": "2026-02-13",
        "internal_dedup_log": dedup_internal_log,
        "vault_dedup_log": [
            {"title": e["title"], "reason": e.get("vault_match_reason", "")}
            for e in existing_vault
        ],
    }

    md_report = generate_markdown_report(
        approved, excluded_qc, dedup_internal_log, existing_vault,
        raw_r_count, raw_a_count,
    )

    if dry_run:
        print(f"\n  [DRY RUN] Would write {len(approved)} entries to:")
        print(f"    {master_json_path}")
        print(f"    {master_md_path}")
        print(f"    {dedup_log_path}")
    else:
        master_json_path.write_text(json.dumps(master_data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Wrote {master_json_path.name}")

        dedup_log_path.write_text(json.dumps(dedup_data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Wrote {dedup_log_path.name}")

        master_md_path.write_text(md_report, encoding="utf-8")
        print(f"  Wrote {master_md_path.name}")

    # --- Summary ---
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Raw candidates:       {raw_r_count + raw_a_count} ({raw_r_count} R + {raw_a_count} A)")
    print(f"  QC excluded:          {len(excluded_qc)}")
    print(f"  Internal dups:        {len(filtered) - len(unique)}")
    print(f"  Already in vault:     {len(existing_vault)}")
    print(f"  Approved for import:  {len(approved)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
