#!/usr/bin/env python3
"""
Populate unknown author metadata using PDF extracts plus optional API fallback.

Pipeline:
1) Build strict unknown-author cohort (Unknown marker in authors/first_author/last_author)
2) Parse candidate authors from PDF extracts (aggressive parsing mode by default)
3) Fallback to external metadata APIs for unresolved records
4) LLM verification (two-model consensus) for extract-backed records
5) Apply approved metadata updates (YAML + body)
6) Rename placeholder author tokens in paper/PDF/extract filenames
7) Emit review CSV + JSON report
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from vault_config import LOGS_DIR, PAPERS_DIR, PDF_EXTRACTS_DIR, WORKSPACE_ROOT
from llm_verify_author_candidates import ModelSpec, summarize_verified_rows, verify_records
from sync_author_names_in_assets import (
    apply_candidate as apply_rename_candidate,
    build_candidate as build_rename_candidate,
    propagate_references,
)


USER_AGENT = "CEI-Lit-WS/unknown-author-enrichment"
UNKNOWN_RE = re.compile(r"\bunknown\b", re.IGNORECASE)
ARXIV_API_BASE = "http://export.arxiv.org/api/query"
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper"

PLACEHOLDER_NAME_RE = re.compile(
    r"\bunknown\b|not fully|authors? incomplete|authors? not fully|\bet al\.?\b|and others",
    re.IGNORECASE,
)

NOISE_FRAGMENTS = {
    "contents lists available",
    "science direct",
    "journal",
    "proceedings",
    "corresponding author",
    "all rights reserved",
    "copyright",
    "preprint",
    "conference",
    "university",
    "department",
    "institute",
    "laboratory",
    "school of",
    "faculty of",
    "research gate",
    "doi",
    "arxiv",
}

PERSON_STOP_TOKENS = {
    "african",
    "ai",
    "artificial",
    "analysis",
    "approach",
    "article",
    "articles",
    "asia",
    "attribution",
    "ave",
    "benchmark",
    "benchmarks",
    "belo",
    "bengal",
    "campus",
    "center",
    "centre",
    "city",
    "college",
    "comparative",
    "computer",
    "conference",
    "commonsense",
    "corporation",
    "corpus",
    "cc",
    "by",
    "dataset",
    "datasets",
    "decolonizing",
    "deep",
    "degree",
    "department",
    "detection",
    "development",
    "english",
    "education",
    "engineering",
    "evaluation",
    "futures",
    "framework",
    "guard",
    "gal",
    "gerais",
    "google",
    "hate",
    "horizonte",
    "highway",
    "hindi",
    "intelligence",
    "inference",
    "identification",
    "inclusive",
    "institute",
    "injustice",
    "journal",
    "keywords",
    "learning",
    "laboratory",
    "language",
    "languages",
    "level",
    "levels",
    "license",
    "linguistics",
    "long",
    "latin",
    "member",
    "mexico",
    "method",
    "methods",
    "minas",
    "model",
    "models",
    "multilingual",
    "natural",
    "oracle",
    "need",
    "new",
    "office",
    "paper",
    "pages",
    "polytechnique",
    "polytechnic",
    "processing",
    "rights",
    "rate",
    "pdf",
    "pipeline",
    "posts",
    "proceedings",
    "program",
    "project",
    "robust",
    "qa",
    "research",
    "road",
    "shaping",
    "southeast",
    "sudparis",
    "scholar",
    "science",
    "senior",
    "success",
    "social",
    "source",
    "speech",
    "statistics",
    "study",
    "suite",
    "survey",
    "systems",
    "task",
    "tasks",
    "tehran",
    "today",
    "this",
    "translate",
    "technology",
    "test",
    "tests",
    "total",
    "understanding",
    "llms",
    "university",
    "vol",
    "west",
    "america",
    "defense",
    "workshop",
    "york",
}

NAME_BANNED_PHRASES = {
    "an up to date",
    "as africans",
    "attribution license",
    "code switched english swahili",
    "data sciences",
    "evaluating code mixed",
    "image courtesy",
    "lingual stability",
    "offensive content identification",
    "presbiteriana mackenzie",
    "southeast asia",
    "tehran polytechnic",
    "universidade estadual",
    "universidade federal",
}

PARTICLES = {
    "da",
    "de",
    "del",
    "della",
    "di",
    "du",
    "la",
    "le",
    "van",
    "von",
    "bin",
    "al",
    "ibn",
    "dos",
    "das",
}
SUFFIXES = {"jr", "sr", "ii", "iii", "iv", "v", "phd", "md"}
ORGANIZATION_HINT_RE = re.compile(
    r"\b(team|consortium|center|centre|institute|foundation|project|lab|laboratory|group|university|committee|network)\b",
    re.IGNORECASE,
)


def split_frontmatter(content: str) -> Optional[Tuple[str, str]]:
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---\n", 4)
    if end == -1:
        return None
    frontmatter = content[4:end]
    body = content[end + 5 :]
    return frontmatter, body


def extract_field(frontmatter: str, key: str) -> Optional[str]:
    prefix = f"{key}:"
    for line in frontmatter.splitlines():
        if line.startswith(prefix):
            return line[len(prefix) :].strip()
    return None


def set_or_add_field(frontmatter: str, key: str, value: str) -> str:
    lines = frontmatter.splitlines()
    prefix = f"{key}:"
    for idx, line in enumerate(lines):
        if line.startswith(prefix):
            lines[idx] = f"{prefix} {value}"
            return "\n".join(lines)
    lines.append(f"{prefix} {value}")
    return "\n".join(lines)


def parse_wikilink_or_plain(raw_value: str) -> str:
    value = raw_value.strip().strip('"').strip("'")
    if not value:
        return ""
    if value.startswith("[[") and value.endswith("]]"):
        value = value[2:-2].strip()
    return value.split("|", 1)[0].strip()


def strip_wrapping_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and ((value[0] == '"' and value[-1] == '"') or (value[0] == "'" and value[-1] == "'")):
        return value[1:-1].strip()
    return value


def clean_token(token: str) -> str:
    token = strip_wrapping_quotes(token)
    token = token.replace("[[", "").replace("]]", "")
    token = re.sub(r"\s+", " ", token).strip(" [](){}")
    return token


def parse_plain_author_list(raw_value: str) -> List[str]:
    raw = strip_wrapping_quotes(raw_value)
    if not raw:
        return []
    if ";" in raw:
        parts = [x.strip() for x in raw.split(";") if x.strip()]
    else:
        parts = [x.strip() for x in re.split(r"\s*,\s*", raw) if x.strip()]
    out: List[str] = []
    seen = set()
    for part in parts:
        cleaned = clean_token(part)
        if not cleaned:
            continue
        key = cleaned.casefold()
        if key in seen:
            continue
        seen.add(key)
        out.append(cleaned)
    return out


def is_strict_unknown(frontmatter: str) -> bool:
    values = []
    for key in ("authors", "first_author", "last_author"):
        value = extract_field(frontmatter, key) or ""
        values.append(value)
    return bool(UNKNOWN_RE.search(" | ".join(values)))


def title_from_body(body: str, fallback: str) -> str:
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def find_unknown_papers(limit: Optional[int] = None) -> List[Dict[str, object]]:
    out: List[Dict[str, object]] = []
    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        text = paper_path.read_text(encoding="utf-8", errors="ignore")
        split = split_frontmatter(text)
        if split is None:
            continue
        frontmatter, body = split
        if not is_strict_unknown(frontmatter):
            continue

        out.append(
            {
                "paper_filename": paper_path.name,
                "paper_path": str(paper_path),
                "title": title_from_body(body, paper_path.stem),
                "doi": strip_wrapping_quotes(extract_field(frontmatter, "doi") or ""),
                "url": strip_wrapping_quotes(extract_field(frontmatter, "url") or ""),
                "external_pdf": strip_wrapping_quotes(extract_field(frontmatter, "external_pdf") or ""),
                "pdf_extract": strip_wrapping_quotes(extract_field(frontmatter, "pdf_extract") or ""),
                "old_authors": extract_field(frontmatter, "authors") or "",
                "old_first_author": extract_field(frontmatter, "first_author") or "",
                "old_last_author": extract_field(frontmatter, "last_author") or "",
                "old_authors_incomplete": extract_field(frontmatter, "authors_incomplete") or "",
            }
        )
        if limit is not None and len(out) >= limit:
            break
    return out


def _strip_extract_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :]
    return text


def _first_page_region(text: str) -> str:
    body = _strip_extract_frontmatter(text)

    # Prefer first code block content if present.
    code_match = re.search(r"```(?:\w+)?\n(.*?)\n```", body, flags=re.DOTALL)
    if code_match:
        body = code_match.group(1)

    page1 = body
    m1 = re.search(r"--- Page 1 ---", body)
    if m1:
        start = m1.end()
        m2 = re.search(r"--- Page 2 ---", body[start:])
        if m2:
            page1 = body[start : start + m2.start()]
        else:
            page1 = body[start:]
    return page1.strip()


def build_evidence_window(extract_path: Path, max_chars: int = 8000) -> Tuple[str, str]:
    text = extract_path.read_text(encoding="utf-8", errors="ignore")
    page1 = _first_page_region(text)
    if len(page1) > max_chars:
        page1 = page1[:max_chars]

    abstract_idx = -1
    for keyword in ("Abstract", "ABSTRACT", "Introduction", "INTRODUCTION"):
        idx = page1.find(keyword)
        if idx != -1:
            abstract_idx = idx
            break
    if abstract_idx == -1:
        targeted = page1[: min(len(page1), 3500)]
    else:
        targeted = page1[: min(abstract_idx, 3500)]

    return page1, targeted


def _looks_like_author_name(text: str) -> bool:
    token = " ".join((text or "").strip().split())
    if not token:
        return False
    low = token.casefold()
    if PLACEHOLDER_NAME_RE.search(low):
        return False
    for fragment in NOISE_FRAGMENTS:
        if fragment in low:
            return False

    if any(ch.isdigit() for ch in token):
        return False

    words = token.split()
    if len(words) < 2 or len(words) > 6:
        return False

    # At least one uppercase initial token and not all lowercase.
    if not any(w[:1].isupper() for w in words):
        return False

    for word in words:
        if "@" in word:
            return False
        if re.search(r"[^A-Za-z\-\.'`]", word):
            return False
    return True


def parse_authors_from_extract_window(window: str) -> List[str]:
    # Remove common affix markers and symbols.
    text = re.sub(r"[\u00B9\u00B2\u00B3\u2070-\u209F]", " ", window)
    text = re.sub(r"[\*\u2020\u2021\u00A7#]+", " ", text)
    text = re.sub(r"\s+", " ", text)

    # Candidate spans likely to contain author names.
    spans: List[str] = []
    for sep_chunk in re.split(r"(?:\.\s+|\n+)", window):
        chunk = " ".join(sep_chunk.split())
        if not chunk:
            continue
        if len(chunk) > 220:
            continue
        spans.append(chunk)

    names: List[str] = []
    seen = set()

    # Aggressive split on common separators.
    for span in spans:
        cleaned = re.sub(r"[\(\)\[\]\{\}]", " ", span)
        parts = re.split(r"\s*[;,|]\s*|\s+and\s+|\s+·\s+|\s+•\s+", cleaned)
        for part in parts:
            candidate = " ".join(part.split()).strip(" ,;.-")
            if not candidate:
                continue
            if not _looks_like_author_name(candidate):
                continue
            key = candidate.casefold()
            if key in seen:
                continue
            seen.add(key)
            names.append(candidate)

    # Regex fallback for contiguous Title-Case names.
    regex = re.compile(
        r"\b([A-Z][A-Za-z'\-\.]+(?:\s+[A-Z][A-Za-z'\-\.]+){1,4})\b"
    )
    for match in regex.findall(text):
        candidate = " ".join(match.split()).strip(" ,;.-")
        if not _looks_like_author_name(candidate):
            continue
        key = candidate.casefold()
        if key in seen:
            continue
        seen.add(key)
        names.append(candidate)

    return names


def _normalize_simple(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def _line_is_author_like(line: str) -> bool:
    low = _normalize_simple(line)
    if not line.strip():
        return False
    if any(fragment in low for fragment in NOISE_FRAGMENTS):
        return False
    if any(mark in low for mark in ("keywords", "abstract", "introduction", "copyright", "all rights reserved")):
        return False
    if not any(delim in line for delim in [",", ";", " and ", "·"]):
        return False
    return True


def _clean_candidate_name(name: str) -> str:
    value = " ".join(str(name).strip().split())
    value = re.sub(r"^[,&\-\s]+|[,&\-\s]+$", "", value)
    value = re.sub(r"^(and|&)\s+", "", value, flags=re.IGNORECASE)
    return value.strip()


def _strict_person_name(name: str) -> bool:
    value = _clean_candidate_name(name)
    if not value:
        return False
    if any(ch.isdigit() for ch in value):
        return False
    low = _normalize_simple(value)
    if any(fragment in low for fragment in NOISE_FRAGMENTS):
        return False
    if any(phrase in low for phrase in NAME_BANNED_PHRASES):
        return False
    if ORGANIZATION_HINT_RE.search(value):
        return False
    words = value.split()
    if len(words) < 2 or len(words) > 6:
        return False
    norm_tokens = [_normalize_simple(word) for word in words]
    if any(token in PERSON_STOP_TOKENS for token in norm_tokens):
        return False
    if norm_tokens[0] in PERSON_STOP_TOKENS or norm_tokens[-1] in PERSON_STOP_TOKENS:
        return False
    for word in words:
        if not re.match(r"^[A-ZÀ-ÖØ-Þ][A-Za-zÀ-ÖØ-öø-ÿ'`.\-]+$", word):
            return False
        bare = re.sub(r"[^A-Za-zÀ-ÖØ-öø-ÿ]", "", word)
        if not bare:
            return False
        if len(bare) == 1 and "." not in word:
            return False
        if word.isupper() and len(bare) <= 3:
            return False
    # Avoid obvious all-caps acronyms in names.
    if any(len(w) > 2 and w.isupper() for w in words):
        return False
    return True


def self_verify_records(records: List[Dict[str, object]]) -> Tuple[List[Dict[str, object]], Dict[str, int]]:
    """
    Local, no-API verification by directly comparing parsed names to extract evidence.
    Conservative policy:
    - Candidate must be person-like.
    - Candidate must appear on an author-like line in the evidence snippet.
    - Require >=2 verified names to auto-approve.
    """
    out: List[Dict[str, object]] = []
    summary = {
        "rows_total": 0,
        "self_accept": 0,
        "self_reject": 0,
        "self_unsure": 0,
    }

    for record in records:
        row = dict(record)
        summary["rows_total"] += 1
        parsed_authors = row.get("parsed_authors", [])
        if not isinstance(parsed_authors, list):
            parsed_authors = []
        snippet = str(row.get("evidence_snippet", "") or "")

        kept: List[str] = []
        seen = set()
        lines = snippet.splitlines()

        for candidate in parsed_authors:
            candidate_text = _clean_candidate_name(str(candidate))
            if not _strict_person_name(candidate_text):
                continue
            norm_candidate = _normalize_simple(candidate_text)
            if not norm_candidate:
                continue

            matching_line = ""
            for line in lines:
                if norm_candidate in _normalize_simple(line):
                    matching_line = line
                    break
            if not matching_line:
                continue
            if not _line_is_author_like(matching_line):
                continue

            key = norm_candidate
            if key in seen:
                continue
            seen.add(key)
            kept.append(candidate_text)

        if len(kept) >= 2:
            row["llm_consensus_decision"] = "self_accept"
            row["llm_consensus_approved"] = True
            row["llm_consensus_authors"] = kept
            summary["self_accept"] += 1
        elif kept:
            row["llm_consensus_decision"] = "self_unsure"
            row["llm_consensus_approved"] = False
            row["llm_consensus_authors"] = kept
            summary["self_unsure"] += 1
        else:
            row["llm_consensus_decision"] = "self_reject"
            row["llm_consensus_approved"] = False
            row["llm_consensus_authors"] = []
            summary["self_reject"] += 1

        row["llm_model_a_verdict"] = {}
        row["llm_model_b_verdict"] = {}
        row["llm_model_a_error"] = ""
        row["llm_model_b_error"] = ""
        out.append(row)

    return out, summary


def check_network(timeout: float = 5.0) -> bool:
    req = urllib.request.Request(
        "https://api.crossref.org/works?rows=0",
        headers={"User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return 200 <= response.status < 300
    except Exception:
        return False


def try_crossref_authors(doi: str, timeout: float = 10.0) -> Optional[List[str]]:
    if not doi:
        return None
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status != 200:
                return None
            data = json.loads(response.read().decode("utf-8", errors="ignore"))
    except Exception:
        return None

    authors = data.get("message", {}).get("author", [])
    out: List[str] = []
    for entry in authors:
        if not isinstance(entry, dict):
            continue
        given = str(entry.get("given", "")).strip()
        family = str(entry.get("family", "")).strip()
        full = f"{given} {family}".strip()
        if full:
            out.append(full)
    return out or None


def extract_arxiv_id(text: str) -> Optional[str]:
    if not text:
        return None
    match = re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})", text, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


def try_arxiv_authors(arxiv_id: str, timeout: float = 10.0) -> Optional[List[str]]:
    if not arxiv_id:
        return None
    url = f"{ARXIV_API_BASE}?id_list={urllib.parse.quote(arxiv_id)}&max_results=1"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status != 200:
                return None
            xml_data = response.read()
    except Exception:
        return None

    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError:
        return None

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    out: List[str] = []
    for author in root.findall(".//atom:author", ns):
        name_elem = author.find("atom:name", ns)
        if name_elem is not None and name_elem.text:
            out.append(name_elem.text.strip())
    return out or None


def try_semantic_scholar_authors(doi: str, timeout: float = 10.0) -> Optional[List[str]]:
    if not doi:
        return None
    url = f"{SEMANTIC_SCHOLAR_API}/DOI:{urllib.parse.quote(doi, safe='')}?fields=authors"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status != 200:
                return None
            data = json.loads(response.read().decode("utf-8", errors="ignore"))
    except Exception:
        return None

    authors = data.get("authors", [])
    out: List[str] = []
    for author in authors:
        if isinstance(author, dict) and isinstance(author.get("name"), str):
            value = author["name"].strip()
            if value:
                out.append(value)
    return out or None


def pick_candidate_authors(
    record: Dict[str, object],
    network_available: bool,
    allow_network_fallback: bool,
) -> Dict[str, object]:
    out = dict(record)
    parsed_authors: List[str] = []
    source = "unresolved"
    reason = ""

    pdf_extract_rel = str(record.get("pdf_extract", "")).strip()
    extract_path: Optional[Path] = None
    evidence_window = ""
    full_page = ""

    if pdf_extract_rel:
        extract_path = WORKSPACE_ROOT / pdf_extract_rel
        if extract_path.exists():
            full_page, evidence_window = build_evidence_window(extract_path)
            parsed_authors = parse_authors_from_extract_window(evidence_window)
            source = "pdf_extract"
            if not parsed_authors:
                reason = "extract_parse_empty"
        else:
            reason = "pdf_extract_missing"
    else:
        reason = "pdf_extract_blank"

    # API fallback only when no parsed extract authors.
    if not parsed_authors and allow_network_fallback and network_available:
        doi = str(record.get("doi", "")).strip()
        url = str(record.get("url", "")).strip()
        external_pdf = str(record.get("external_pdf", "")).strip()

        api_candidates: Optional[List[str]] = None
        if doi:
            api_candidates = try_crossref_authors(doi)
            if api_candidates:
                source = "crossref_doi"
        if not api_candidates:
            arxiv_id = extract_arxiv_id(url) or extract_arxiv_id(external_pdf)
            if arxiv_id:
                api_candidates = try_arxiv_authors(arxiv_id)
                if api_candidates:
                    source = "arxiv_api"
        if not api_candidates and doi:
            api_candidates = try_semantic_scholar_authors(doi)
            if api_candidates:
                source = "semantic_scholar_doi"

        if api_candidates:
            parsed_authors = api_candidates
            reason = ""
        elif not reason:
            reason = "api_fallback_failed"

    out["parsed_authors"] = parsed_authors
    out["source_type"] = source
    out["candidate_reason"] = reason
    out["evidence_snippet"] = evidence_window
    out["evidence_page1"] = full_page
    out["has_extract_file"] = bool(extract_path and extract_path.exists())
    return out


def canonical_name_last_first(name: str) -> str:
    value = clean_token(name)
    if not value:
        return ""

    if ORGANIZATION_HINT_RE.search(value):
        return value

    if "," in value:
        left, right = [x.strip() for x in value.split(",", 1)]
        if left and right:
            return f"{left}, {right}"
        return value

    parts = value.split()
    if len(parts) == 1:
        return parts[0]

    if parts[-1].casefold() in SUFFIXES and len(parts) >= 3:
        surname_parts = [parts[-2], parts[-1]]
        given_parts = parts[:-2]
    else:
        surname_parts = [parts[-1]]
        idx = len(parts) - 2
        while idx >= 0 and parts[idx].casefold() in PARTICLES:
            surname_parts.insert(0, parts[idx])
            idx -= 1
        given_parts = parts[: idx + 1]

    if not given_parts:
        return " ".join(surname_parts)
    return f"{' '.join(surname_parts)}, {' '.join(given_parts)}"


def to_wikilink(last_first_name: str) -> str:
    cleaned = clean_token(last_first_name)
    return f"[[{cleaned}]]"


def update_body_author_sections(body: str, author_wikilinks: List[str], author_plain: List[str]) -> str:
    lines = body.splitlines()
    author_line = ", ".join(author_wikilinks)
    metadata_line = "; ".join(author_plain)

    # Update or insert ## Authors section.
    authors_heading_idx = -1
    for idx, line in enumerate(lines):
        if line.strip().lower() == "## authors":
            authors_heading_idx = idx
            break

    if authors_heading_idx >= 0:
        j = authors_heading_idx + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j < len(lines):
            lines[j] = author_line
        else:
            lines.extend(["", author_line])
    else:
        # Insert after first title heading.
        insert_at = 0
        for idx, line in enumerate(lines):
            if line.startswith("# "):
                insert_at = idx + 1
                break
        block = ["", "## Authors", "", author_line, ""]
        lines[insert_at:insert_at] = block

    # Update or insert **Authors:** metadata line.
    metadata_updated = False
    for idx, line in enumerate(lines):
        if line.startswith("**Authors:**"):
            lines[idx] = f"**Authors:** {metadata_line}"
            metadata_updated = True
            break
    if not metadata_updated:
        metadata_heading_idx = -1
        for idx, line in enumerate(lines):
            if line.strip().lower() == "## metadata":
                metadata_heading_idx = idx
                break
        if metadata_heading_idx >= 0:
            insert_idx = metadata_heading_idx + 1
            while insert_idx < len(lines) and not lines[insert_idx].strip():
                insert_idx += 1
            lines.insert(insert_idx, f"**Authors:** {metadata_line}")

    return "\n".join(lines)


def update_paper_authors(paper_path: Path, author_plain: List[str], mark_incomplete: bool = True) -> Dict[str, object]:
    content = paper_path.read_text(encoding="utf-8", errors="ignore")
    split = split_frontmatter(content)
    if split is None:
        raise RuntimeError(f"Frontmatter unparseable: {paper_path.name}")
    frontmatter, body = split

    canonical = [canonical_name_last_first(x) for x in author_plain if clean_token(x)]
    canonical = [x for x in canonical if x]
    # Deduplicate after canonicalization.
    deduped: List[str] = []
    seen = set()
    for name in canonical:
        key = name.casefold()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(name)

    if not deduped:
        raise RuntimeError(f"No valid canonical authors generated: {paper_path.name}")

    wikilinks = [to_wikilink(x) for x in deduped]
    authors_value = "; ".join(wikilinks)
    first_author = wikilinks[0]
    last_author = wikilinks[-1]

    old_authors = extract_field(frontmatter, "authors") or ""
    old_first = extract_field(frontmatter, "first_author") or ""
    old_last = extract_field(frontmatter, "last_author") or ""
    old_incomplete = extract_field(frontmatter, "authors_incomplete") or ""

    frontmatter = set_or_add_field(frontmatter, "authors", f'"{authors_value}"')
    frontmatter = set_or_add_field(frontmatter, "first_author", f'"{first_author}"')
    frontmatter = set_or_add_field(frontmatter, "last_author", f'"{last_author}"')
    incomplete_value = "true" if mark_incomplete else "false"
    frontmatter = set_or_add_field(frontmatter, "authors_incomplete", incomplete_value)

    body = update_body_author_sections(body, wikilinks, [clean_token(x) for x in author_plain if clean_token(x)])
    paper_path.write_text(f"---\n{frontmatter}\n---\n{body}", encoding="utf-8")

    return {
        "old_authors": old_authors,
        "old_first_author": old_first,
        "old_last_author": old_last,
        "old_authors_incomplete": old_incomplete,
        "new_authors": authors_value,
        "new_first_author": first_author,
        "new_last_author": last_author,
        "new_authors_incomplete": incomplete_value,
    }


def write_review_csv(records: List[Dict[str, object]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "paper_filename",
        "title",
        "source_type",
        "candidate_reason",
        "pdf_extract",
        "has_extract_file",
        "parsed_authors",
        "llm_consensus_decision",
        "llm_consensus_approved",
        "llm_consensus_authors",
        "approved_for_apply",
        "apply_status",
        "apply_reason",
        "old_authors",
        "new_authors",
        "old_first_author",
        "new_first_author",
        "old_last_author",
        "new_last_author",
        "rename_status",
        "renamed_paper",
        "renamed_pdf",
        "renamed_extract",
        "evidence_preview",
    ]
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            row = dict(record)
            for key in ("parsed_authors", "llm_consensus_authors"):
                row[key] = json.dumps(row.get(key, []), ensure_ascii=False)
            preview = str(row.get("evidence_snippet", "")).replace("\n", " ").strip()
            row["evidence_preview"] = preview[:400]
            writer.writerow({field: row.get(field, "") for field in fields})


def default_output_paths(date_str: str) -> Tuple[Path, Path]:
    json_path = LOGS_DIR / f"{date_str}-unknown-author-enrichment-report.json"
    csv_path = LOGS_DIR / f"{date_str}-unknown-author-enrichment-review.csv"
    return json_path, csv_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Populate unknown authors from extracts + LLM verification.")
    parser.add_argument("--apply", action="store_true", help="Apply approved updates.")
    parser.add_argument("--review-only", action="store_true", help="Never mutate files; only generate reports.")
    parser.add_argument("--self-verify", action="store_true", help="Use built-in local verifier instead of API LLM calls.")
    parser.add_argument("--limit", type=int, default=None, help="Process only first N unknown papers.")
    parser.add_argument("--no-network-fallback", action="store_true", help="Disable DOI/arXiv/API fallback.")
    parser.add_argument("--skip-llm", action="store_true", help="Skip LLM verification step.")
    parser.add_argument(
        "--allow-api-without-llm",
        action="store_true",
        help="Allow apply for API-only records without extract-backed LLM verification.",
    )
    parser.add_argument("--report-json", type=Path, default=None)
    parser.add_argument("--report-csv", type=Path, default=None)

    parser.add_argument("--model-a-provider", choices=["openai", "anthropic", "gemini"], default="gemini")
    parser.add_argument("--model-a", type=str, default="gemini-2.0-flash")
    parser.add_argument("--model-b-provider", choices=["openai", "anthropic", "gemini"], default="gemini")
    parser.add_argument("--model-b", type=str, default="gemini-2.0-flash")
    parser.add_argument("--llm-timeout", type=float, default=45.0)
    parser.add_argument("--llm-temperature", type=float, default=0.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    now = dt.datetime.now()
    date_str = now.strftime("%Y%m%d")

    report_json, report_csv = default_output_paths(date_str)
    if args.report_json is not None:
        report_json = args.report_json
    if args.report_csv is not None:
        report_csv = args.report_csv

    unknown_records = find_unknown_papers(limit=args.limit)
    allow_network_fallback = not args.no_network_fallback
    network_available = check_network() if allow_network_fallback else False

    working: List[Dict[str, object]] = []
    for record in unknown_records:
        enriched = pick_candidate_authors(record, network_available, allow_network_fallback)
        enriched["llm_consensus_decision"] = ""
        enriched["llm_consensus_approved"] = False
        enriched["llm_consensus_authors"] = []
        enriched["approved_for_apply"] = False
        enriched["apply_status"] = "pending"
        enriched["apply_reason"] = ""
        enriched["rename_status"] = ""
        enriched["renamed_paper"] = ""
        enriched["renamed_pdf"] = ""
        enriched["renamed_extract"] = ""
        working.append(enriched)

    # LLM verification for records with extract evidence.
    llm_inputs = [r for r in working if r.get("has_extract_file")]
    llm_summary: Dict[str, int] = {}
    if args.self_verify and llm_inputs:
        verified_inputs, llm_summary = self_verify_records(llm_inputs)
        by_filename = {str(r.get("paper_filename", "")): r for r in verified_inputs}
        for record in working:
            match = by_filename.get(str(record.get("paper_filename", "")))
            if not match:
                continue
            record["llm_consensus_decision"] = match.get("llm_consensus_decision", "")
            record["llm_consensus_approved"] = bool(match.get("llm_consensus_approved", False))
            record["llm_consensus_authors"] = match.get("llm_consensus_authors", [])
            record["llm_model_a_verdict"] = {}
            record["llm_model_b_verdict"] = {}
            record["llm_model_a_error"] = ""
            record["llm_model_b_error"] = ""
    elif not args.skip_llm and llm_inputs:
        model_a = ModelSpec(
            provider=args.model_a_provider,
            model=args.model_a,
            timeout=args.llm_timeout,
            temperature=args.llm_temperature,
        )
        model_b = ModelSpec(
            provider=args.model_b_provider,
            model=args.model_b,
            timeout=args.llm_timeout,
            temperature=args.llm_temperature,
        )
        verified_inputs = verify_records(llm_inputs, model_a, model_b)
        llm_summary = summarize_verified_rows(verified_inputs)
        by_filename = {str(r.get("paper_filename", "")): r for r in verified_inputs}
        for record in working:
            match = by_filename.get(str(record.get("paper_filename", "")))
            if not match:
                continue
            record["llm_consensus_decision"] = match.get("llm_consensus_decision", "")
            record["llm_consensus_approved"] = bool(match.get("llm_consensus_approved", False))
            record["llm_consensus_authors"] = match.get("llm_consensus_authors", [])
            record["llm_model_a_verdict"] = match.get("llm_model_a_verdict", {})
            record["llm_model_b_verdict"] = match.get("llm_model_b_verdict", {})
            record["llm_model_a_error"] = match.get("llm_model_a_error", "")
            record["llm_model_b_error"] = match.get("llm_model_b_error", "")
    else:
        llm_summary = {
            "rows_total": len(llm_inputs),
            "consensus_accept": 0,
            "consensus_reject": 0,
            "consensus_unsure": 0,
            "consensus_disagree_decision": 0,
            "consensus_disagree_authors": 0,
            "model_a_errors": 0,
            "model_b_errors": 0,
        }

    # Final approval routing.
    for record in working:
        parsed_authors = record.get("parsed_authors", [])
        if not isinstance(parsed_authors, list):
            parsed_authors = []
        has_extract = bool(record.get("has_extract_file"))
        source_type = str(record.get("source_type", ""))
        llm_ok = bool(record.get("llm_consensus_approved", False))
        llm_authors = record.get("llm_consensus_authors", [])
        if not isinstance(llm_authors, list):
            llm_authors = []

        approved = False
        apply_authors: List[str] = []
        reason = ""
        if has_extract and llm_ok and llm_authors:
            approved = True
            apply_authors = [str(x) for x in llm_authors if str(x).strip()]
            reason = "llm_consensus_accept"
        elif (not has_extract) and source_type.startswith(("crossref", "arxiv", "semantic")) and parsed_authors:
            if args.allow_api_without_llm:
                approved = True
                apply_authors = [str(x) for x in parsed_authors if str(x).strip()]
                reason = "api_no_extract_allowed"
            else:
                reason = "api_no_extract_requires_manual"
        else:
            reason = "not_approved"

        record["approved_for_apply"] = approved
        record["approved_authors"] = apply_authors
        if not record.get("apply_reason"):
            record["apply_reason"] = reason

    dry_run = (not args.apply) or args.review_only
    changed_files: List[str] = []
    rename_candidates = []
    renamed_candidates = []
    apply_errors: List[str] = []

    if dry_run:
        for record in working:
            if record.get("approved_for_apply"):
                record["apply_status"] = "would_apply"
            else:
                record["apply_status"] = "skipped"
    else:
        for record in working:
            paper_filename = str(record.get("paper_filename", ""))
            approved_authors = record.get("approved_authors", [])
            if not record.get("approved_for_apply") or not isinstance(approved_authors, list) or not approved_authors:
                record["apply_status"] = "skipped"
                continue
            paper_path = PAPERS_DIR / paper_filename
            if not paper_path.exists():
                record["apply_status"] = "error"
                record["apply_reason"] = "paper_missing_at_apply"
                apply_errors.append(f"{paper_filename}: paper_missing_at_apply")
                continue
            try:
                source_type = str(record.get("source_type", "") or "")
                # Conservative default for extract/self-verified updates:
                # retain authors_incomplete=true unless explicitly high-certainty API metadata is used.
                mark_incomplete = not source_type.startswith(("crossref", "arxiv", "semantic"))
                update_result = update_paper_authors(
                    paper_path,
                    [str(x) for x in approved_authors],
                    mark_incomplete=mark_incomplete,
                )
                record.update(update_result)
                record["apply_status"] = "applied"
                changed_files.append(paper_filename)
            except Exception as exc:
                record["apply_status"] = "error"
                record["apply_reason"] = str(exc)
                apply_errors.append(f"{paper_filename}: {exc}")

        # Filename sync for changed records.
        for filename in changed_files:
            candidate, reason = build_rename_candidate(filename)
            if candidate is None:
                for record in working:
                    if record.get("paper_filename") == filename and record.get("apply_status") == "applied":
                        record["rename_status"] = f"skip:{reason}"
                continue
            rename_candidates.append(candidate)

        for candidate in rename_candidates:
            try:
                apply_rename_candidate(candidate)
                renamed_candidates.append(candidate)
                old_name = candidate.old_paper_path.name
                for record in working:
                    if record.get("paper_filename") == old_name:
                        record["rename_status"] = "applied"
                        record["renamed_paper"] = candidate.new_paper_path.name
                        record["renamed_pdf"] = candidate.new_pdf_rel
                        record["renamed_extract"] = candidate.new_extract_rel
                        record["paper_filename"] = candidate.new_paper_path.name
                        break
            except Exception as exc:
                apply_errors.append(f"{candidate.paper_filename}: rename_error:{exc}")
                for record in working:
                    if record.get("paper_filename") == candidate.paper_filename:
                        record["rename_status"] = f"error:{exc}"

        if renamed_candidates:
            propagation = propagate_references(renamed_candidates, apply=True)
        else:
            propagation = {
                "files_scanned": 0,
                "files_changed": 0,
                "replacement_count": 0,
                "changed_files": [],
            }
    # Dry-run propagation preview for rename candidates.
    if dry_run:
        for filename in changed_files:
            candidate, _reason = build_rename_candidate(filename)
            if candidate is not None:
                rename_candidates.append(candidate)
        if rename_candidates:
            propagation = propagate_references(rename_candidates, apply=False)
        else:
            propagation = {
                "files_scanned": 0,
                "files_changed": 0,
                "replacement_count": 0,
                "changed_files": [],
            }

    # Optional YAML validation after apply.
    yaml_validation = {"ran": False, "exit_code": 0, "stdout": "", "stderr": ""}
    if not dry_run:
        cmd = ["python3", "PYTHON/validate_yaml_hook.py"]
        proc = subprocess.run(cmd, cwd=str(WORKSPACE_ROOT), capture_output=True, text=True)
        yaml_validation = {
            "ran": True,
            "exit_code": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }
        if proc.returncode != 0:
            apply_errors.append("yaml_validation_failed")

    summary = {
        "unknown_total": len(unknown_records),
        "with_extract_file": sum(1 for r in working if r.get("has_extract_file")),
        "candidate_nonempty": sum(1 for r in working if r.get("parsed_authors")),
        "approved_for_apply": sum(1 for r in working if r.get("approved_for_apply")),
        "applied": sum(1 for r in working if r.get("apply_status") == "applied"),
        "would_apply": sum(1 for r in working if r.get("apply_status") == "would_apply"),
        "skipped": sum(1 for r in working if r.get("apply_status") == "skipped"),
        "errors": sum(1 for r in working if r.get("apply_status") == "error"),
        "rename_candidates": len(rename_candidates),
        "renamed": len(renamed_candidates),
    }

    report = {
        "generated_at": now.isoformat(timespec="seconds"),
        "dry_run": dry_run,
        "network_fallback_enabled": allow_network_fallback,
        "network_available": network_available,
        "llm_summary": llm_summary,
        "summary": summary,
        "propagation": propagation,
        "yaml_validation": yaml_validation,
        "apply_errors": apply_errors,
        "records": working,
    }

    report_json.parent.mkdir(parents=True, exist_ok=True)
    report_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_review_csv(working, report_csv)

    print("=" * 80)
    print(f"Unknown Author Enrichment {'(DRY RUN)' if dry_run else '(APPLY)'}")
    print("=" * 80)
    print(f"Unknown papers: {summary['unknown_total']}")
    print(f"With extract file: {summary['with_extract_file']}")
    print(f"Non-empty candidates: {summary['candidate_nonempty']}")
    print(f"Approved for apply: {summary['approved_for_apply']}")
    print(f"Applied: {summary['applied']}")
    print(f"Would apply: {summary['would_apply']}")
    print(f"Renamed: {summary['renamed']}")
    print(f"Errors: {summary['errors']}")
    print(f"Report JSON: {report_json}")
    print(f"Review CSV:  {report_csv}")

    if apply_errors:
        print("\nApply errors:")
        for item in apply_errors[:50]:
            print(f"  - {item}")

    if not dry_run and yaml_validation.get("exit_code", 0) != 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
