#!/usr/bin/env python3
"""
Conference Classification (CC) — Add normalized CONF-CC field to all papers.

3-Phase waterfall:
  Phase 1: Local heuristic (regex on publication + type fields, instant)
  Phase 2: OpenAlex API (DOI lookup, 0.1s rate limit)
  Phase 3: Semantic Scholar API (arXiv/DOI lookup, 4s rate limit)

Usage:
  ../.venv/bin/python PYTHON/add_conference_field_cc.py             # Full run
  ../.venv/bin/python PYTHON/add_conference_field_cc.py --dry-run   # Preview
  ../.venv/bin/python PYTHON/add_conference_field_cc.py --phase 1   # Phase 1 only
  ../.venv/bin/python PYTHON/add_conference_field_cc.py --report    # Stats only
  ../.venv/bin/python PYTHON/add_conference_field_cc.py --force     # Re-classify all
  ../.venv/bin/python PYTHON/add_conference_field_cc.py 1 500       # Batch range
"""

import re
import sys
import json
import time
import functools
import argparse
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime
from collections import Counter

print = functools.partial(print, flush=True)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent
WORKSPACE = SCRIPT_DIR.parent
PAPERS_DIR = WORKSPACE / "papers"
LOGS_DIR = WORKSPACE / "logs"

# ---------------------------------------------------------------------------
# YAML helpers (safe regex, no parse→rebuild round-trip)
# ---------------------------------------------------------------------------

def get_frontmatter(content: str):
    """Extract frontmatter and body. Returns (frontmatter, body) or (None, content)."""
    if not content.startswith('---'):
        return None, content
    end = content.find('\n---\n', 3)
    if end != -1:
        return content[3:end], content[end + 5:]
    return None, content


def get_field(frontmatter: str, key: str) -> str:
    """Extract a single field value from frontmatter text."""
    m = re.search(rf'^{re.escape(key)}:\s*"?(.+?)"?\s*$', frontmatter, re.MULTILINE)
    return m.group(1).strip() if m else ""


def set_field(frontmatter: str, key: str, value: str) -> str:
    """Set a field in frontmatter using safe regex (no round-trip)."""
    safe_val = value.replace('"', "'")
    replacement = f'{key}: "{safe_val}"'
    pattern = re.compile(rf'^{re.escape(key)}:\s*.*$', re.MULTILINE)
    new_fm, n = pattern.subn(replacement, frontmatter, count=1)
    if n > 0:
        return new_fm
    # Field doesn't exist — insert after publication: or before DATE_ADDED:
    for anchor in ['publication:', 'DATE_ADDED:']:
        anchor_pat = re.compile(rf'^({re.escape(anchor)}\s*.*)$', re.MULTILINE)
        m = anchor_pat.search(frontmatter)
        if m:
            if anchor == 'publication:':
                return frontmatter[:m.end()] + f'\n{replacement}' + frontmatter[m.end():]
            else:
                return frontmatter[:m.start()] + f'{replacement}\n' + frontmatter[m.start():]
    # Last resort: append
    return frontmatter.rstrip() + f'\n{replacement}'


def validate_frontmatter(frontmatter: str) -> bool:
    """Quick validation: check for mismatched quotes and orphaned list items."""
    for line in frontmatter.split('\n'):
        if '"' in line and line.count('"') % 2 != 0:
            return False
    return True


def extract_arxiv_id(frontmatter: str) -> str:
    """Extract arXiv ID from DOI or URL fields."""
    doi_m = re.search(r'doi:\s*"?10\.48550/arXiv\.([\d.]+)"?', frontmatter, re.IGNORECASE)
    if doi_m:
        return doi_m.group(1)
    url_m = re.search(r'url:\s*"?https?://arxiv\.org/abs/([\d.]+)"?', frontmatter, re.IGNORECASE)
    if url_m:
        return url_m.group(1)
    return ""


def extract_doi(frontmatter: str) -> str:
    """Extract DOI (non-arXiv) from frontmatter."""
    m = re.search(r'^doi:\s*"?(10\.\d{4,}/[^\s"]+)"?', frontmatter, re.MULTILINE)
    if m:
        doi = m.group(1)
        if 'arxiv' not in doi.lower():
            return doi
    return ""


# ---------------------------------------------------------------------------
# Conference normalization
# ---------------------------------------------------------------------------

# Short aliases → canonical name (without year)
CONFERENCE_ALIASES = {
    # NeurIPS / NIPS
    "neurips": "NeurIPS",
    "nips": "NeurIPS",
    "neural information processing systems": "NeurIPS",
    "conference on neural information processing systems": "NeurIPS",
    "advances in neural information processing systems": "NeurIPS",
    # ICML
    "icml": "ICML",
    "international conference on machine learning": "ICML",
    # ICLR
    "iclr": "ICLR",
    "international conference on learning representations": "ICLR",
    # ACL
    "acl": "ACL",
    "annual meeting of the association for computational linguistics": "ACL",
    "association for computational linguistics": "ACL",
    # EMNLP
    "emnlp": "EMNLP",
    "conference on empirical methods in natural language processing": "EMNLP",
    "empirical methods in natural language processing": "EMNLP",
    # NAACL
    "naacl": "NAACL",
    "north american chapter of the association for computational linguistics": "NAACL",
    # COLING
    "coling": "COLING",
    "international conference on computational linguistics": "COLING",
    # EACL
    "eacl": "EACL",
    "conference of the european chapter of the association for computational linguistics": "EACL",
    "european chapter of the association for computational linguistics": "EACL",
    # AACL
    "aacl": "AACL",
    "aacl-ijcnlp": "AACL",
    "ijcnlp-aacl": "AACL",
    # AAAI
    "aaai": "AAAI",
    "aaai conference on artificial intelligence": "AAAI",
    # IJCAI
    "ijcai": "IJCAI",
    "international joint conference on artificial intelligence": "IJCAI",
    # AIES
    "aies": "AIES",
    "aaai/acm conference on ai, ethics, and society": "AIES",
    "aaai/acm aies": "AIES",
    # FAccT
    "facct": "FAccT",
    "acm facct": "FAccT",
    "conference on fairness, accountability and transparency": "FAccT",
    "fat*": "FAccT",
    "fat": "FAccT",
    # CHI
    "chi": "CHI",
    "acm chi": "CHI",
    # COLM
    "colm": "COLM",
    # TACL
    "tacl": "TACL",
    "transactions of the acl": "TACL",
    "transactions of the association for computational linguistics": "TACL",
    # Vision conferences
    "cvpr": "CVPR",
    "computer vision and pattern recognition": "CVPR",
    "eccv": "ECCV",
    "iccv": "ICCV",
    "accv": "ACCV",
    "bmvc": "BMVC",
    "british machine vision conference": "BMVC",
    # Web/IR/Data
    "www": "WWW",
    "acm web conference": "WWW",
    "kdd": "KDD",
    "sigkdd": "KDD",
    "sigir": "SIGIR",
    "cikm": "CIKM",
    "asonam": "ASONAM",
    # NLP workshops and shared tasks
    "semeval": "SemEval",
    "international workshop on semantic evaluation": "SemEval",
    "lrec": "LREC",
    "lrec-coling": "LREC-COLING",
    "icwsm": "ICWSM",
    "ranlp": "RANLP",
    "nodalida": "NoDaLiDa",
    "propor": "PROPOR",
    "icon": "ICON",
    "rocling": "ROCLING",
    "stil": "STIL",
    "evalita": "EVALITA",
    "iberlef": "IberLEF",
    "clef": "CLEF",
    "fire": "FIRE",
    # Other ML
    "interspeech": "INTERSPEECH",
    "icprai": "ICPRAI",
    "hcii": "HCII",
    "ecai": "ECAI",
    "ecml pkdd": "ECML-PKDD",
    "tmlr": "TMLR",
}

# Journals: EXACT match (lowercase pub must equal key exactly)
JOURNAL_EXACT = {
    "science": "Science",
    "nature": "Nature",
    "pnas": "PNAS",
    "cognition": "Cognition",
    "neurocomputing": "Neurocomputing",
    "patterns": "Patterns",
    "plos one": "PLOS ONE",
    "ai and ethics": "AI and Ethics",
    "ai & ethics": "AI and Ethics",
    "ai ethics": "AI and Ethics",
    "ai & society": "AI & Society",
    "ai and society": "AI & Society",
    "ai & society (springer)": "AI & Society",
    "ai and ethics (springer)": "AI and Ethics",
    "springer ai and ethics": "AI and Ethics",
    "springer ai & ethics": "AI and Ethics",
    "minds and machines": "Minds and Machines",
    "philosophical studies": "Philosophical Studies",
    "philosophy & technology": "Philosophy & Technology",
    "springer philosophy & technology": "Philosophy & Technology",
    "ieee access": "IEEE Access",
    "tacl": "TACL",
    "findings": "N/A",
    "acm computing surveys": "ACM Computing Surveys",
    "acm tosem": "ACM TOSEM",
    "scientific reports": "Nature Scientific Reports",
    "scientific reports (nature)": "Nature Scientific Reports",
    "nature scientific reports": "Nature Scientific Reports",
    "nature scientific reports 2025": "Nature Scientific Reports",
    "nature scientific data": "Nature Scientific Data",
    "nature scientific data 2025": "Nature Scientific Data",
    "nature human behaviour": "Nature Human Behaviour",
    "nature machine intelligence": "Nature Machine Intelligence",
    "npj artificial intelligence": "npj AI",
    "artificial intelligence": "Artificial Intelligence",
    "artificial intelligence review": "Artificial Intelligence Review",
    "frontiers": "Frontiers",
    "frontiers in big data": "Frontiers in Big Data",
}

# Journals: SUBSTRING match (if key appears anywhere in lowercase pub)
JOURNAL_SUBSTRING = {
    "language resources and evaluation": "Language Resources and Evaluation",
    "ethics and information technology": "Ethics and Information Technology",
    "information processing and management": "Information Processing and Management",
    "information processing & management": "Information Processing and Management",
    "data in brief": "Data in Brief",
    "peerj computer science": "PeerJ Computer Science",
    "big data & society": "Big Data & Society",
    "humanities and social sciences communications": "Humanities and Social Sciences Communications",
    "journal of cross-cultural psychology": "Journal of Cross-Cultural Psychology",
    "topics in cognitive science": "Topics in Cognitive Science",
    "computers in human behavior": "Computers in Human Behavior",
    "knowledge-based systems": "Knowledge-Based Systems",
    "natural language processing": "Natural Language Processing",
    "ieee transactions on affective computing": "IEEE TAC",
    "ieee transactions on computational social systems": "IEEE TCSS",
    "acm transactions on intelligent systems": "ACM TIST",
    "acm transactions on asian": "ACM TALIP",
    "proceedings of the national academy of sciences": "PNAS",
    "machine learning": "Machine Learning",
}

# Sources that indicate preprint / non-venue
PREPRINT_INDICATORS = {
    "arxiv", "arxiv.org", "arxiv preprint", "arxiv (preprint)",
    "arxiv (withdrawn)", "arxiv (data article)",
    "corr", "ssrn", "medrxiv", "techrxiv",
    "researchgate", "openreview", "philarchive",
    "huggingface", "hugging face", "github", "github / huggingface",
    "web", "unknown", "not specified",
}

# Non-venue publishers (need API for actual venue)
PUBLISHER_ONLY = {
    "springer", "acm", "ieee", "mdpi", "sciencedirect",
    "elsevier", "pubmed", "frontiers", "taylor & francis",
    "sage", "acl anthology",
}


def _extract_year(text: str) -> str:
    """Extract a 4-digit year from text."""
    m = re.search(r'(20[0-2]\d|19\d\d)', text)
    return m.group(1) if m else ""


def _normalize_conf_name(text: str) -> str:
    """Try to match text against known conference aliases."""
    low = text.lower().strip()
    # Direct match
    if low in CONFERENCE_ALIASES:
        return CONFERENCE_ALIASES[low]
    # Try without year suffix
    no_year = re.sub(r'\s*\d{4}\s*$', '', low).strip()
    if no_year in CONFERENCE_ALIASES:
        return CONFERENCE_ALIASES[no_year]
    # Try removing common prefixes
    for prefix in ["proceedings of the ", "proceedings of ", "the "]:
        if low.startswith(prefix):
            trimmed = low[len(prefix):]
            if trimmed in CONFERENCE_ALIASES:
                return CONFERENCE_ALIASES[trimmed]
            no_year_t = re.sub(r'\s*\d{4}\s*$', '', trimmed).strip()
            if no_year_t in CONFERENCE_ALIASES:
                return CONFERENCE_ALIASES[no_year_t]
            # Strip ordinal + try again: "60th annual meeting..." → "annual meeting..."
            stripped_ord = re.sub(r'^\d+(?:st|nd|rd|th)\s+', '', trimmed)
            if stripped_ord != trimmed:
                if stripped_ord in CONFERENCE_ALIASES:
                    return CONFERENCE_ALIASES[stripped_ord]
                no_year_o = re.sub(r'\s*\d{4}\s*$', '', stripped_ord).strip()
                if no_year_o in CONFERENCE_ALIASES:
                    return CONFERENCE_ALIASES[no_year_o]
                # Also strip parenthetical volume info: "(Volume 1: Long Papers)"
                no_parens = re.sub(r'\s*\(.*?\)\s*$', '', stripped_ord).strip()
                if no_parens in CONFERENCE_ALIASES:
                    return CONFERENCE_ALIASES[no_parens]
    return ""


def _match_journal(text: str) -> str:
    """Try to match text against known journals (exact first, then substring)."""
    low = text.lower().strip().strip('"').strip("'")
    # Exact match first
    if low in JOURNAL_EXACT:
        return JOURNAL_EXACT[low]
    # Substring match for longer, unambiguous journal names
    for pattern, canonical in JOURNAL_SUBSTRING.items():
        if pattern in low:
            return canonical
    return ""


def classify_phase1(pub: str, paper_type: str, year: str) -> str:
    """Phase 1: Local heuristic classification from publication + type fields.

    Returns normalized venue string or empty string if unresolved.
    """
    if not pub and not paper_type:
        return ""

    pub_stripped = pub.strip().strip('"').strip("'")
    pub_low = pub_stripped.lower()

    # --- Handle "arXiv / VENUE" pattern ---
    slash_match = re.match(
        r'^(?:arxiv\.?o?r?g?\s*/\s*|arxiv\s*\(.*?\)\s*/\s*)',
        pub_stripped, re.IGNORECASE
    )
    if slash_match:
        after_slash = pub_stripped[slash_match.end():].strip()
        # Recurse on the venue part
        result = classify_phase1(after_slash, paper_type, year)
        if result and result != "Preprint":
            return result

    # --- Handle "arXiv / ACL Anthology (VENUE)" ---
    acl_anth_match = re.match(
        r'^(?:arxiv[^/]*/\s*)?ACL\s+Anthology\s*\(([^)]+)\)',
        pub_stripped, re.IGNORECASE
    )
    if acl_anth_match:
        inner = acl_anth_match.group(1).strip()
        result = classify_phase1(inner, paper_type, year)
        if result and result != "Preprint":
            return result

    # --- Handle "ACL Anthology (VENUE)" ---
    acl_anth_match2 = re.match(
        r'^ACL\s+Anthology\s*\(([^)]+)\)',
        pub_stripped, re.IGNORECASE
    )
    if acl_anth_match2:
        inner = acl_anth_match2.group(1).strip()
        result = classify_phase1(inner, paper_type, year)
        if result and result != "Preprint":
            return result

    # --- Handle "ACL Anthology / VENUE" ---
    acl_anth_slash = re.match(
        r'^ACL\s+Anthology\s*/\s*(.+)$',
        pub_stripped, re.IGNORECASE
    )
    if acl_anth_slash:
        after = acl_anth_slash.group(1).strip()
        result = classify_phase1(after, paper_type, year)
        if result and result != "Preprint":
            return result

    # --- Handle "arxiv.org / VENUE" ---
    arxiv_org_slash = re.match(
        r'^arxiv\.org\s*/\s*(.+)$',
        pub_stripped, re.IGNORECASE
    )
    if arxiv_org_slash:
        after = arxiv_org_slash.group(1).strip()
        result = classify_phase1(after, paper_type, year)
        if result and result != "Preprint":
            return result

    # --- Handle "Findings of VENUE YEAR" ---
    findings_match = re.match(
        r'^(?:Findings\s+of\s+)(\w+)\s*(\d{4})?\s*(Findings)?',
        pub_stripped, re.IGNORECASE
    )
    if findings_match:
        venue_part = findings_match.group(1)
        yr = findings_match.group(2) or ""
        conf = _normalize_conf_name(venue_part)
        if conf:
            yr = yr or _extract_year(pub_stripped) or year
            return f"{conf} {yr} Findings".strip() if yr else f"{conf} Findings"

    # --- Handle "VENUE YEAR Findings" ---
    findings_match2 = re.match(
        r'^(\w+)\s+(\d{4})\s+Findings',
        pub_stripped, re.IGNORECASE
    )
    if findings_match2:
        venue_part = findings_match2.group(1)
        yr = findings_match2.group(2)
        conf = _normalize_conf_name(venue_part)
        if conf:
            return f"{conf} {yr} Findings"

    # --- Handle "arXiv / VENUE YEAR Findings" ---
    arxiv_findings = re.match(
        r'^arXiv\s*/\s*(\w+)\s+(\d{4})\s+Findings',
        pub_stripped, re.IGNORECASE
    )
    if arxiv_findings:
        venue_part = arxiv_findings.group(1)
        yr = arxiv_findings.group(2)
        conf = _normalize_conf_name(venue_part)
        if conf:
            return f"{conf} {yr} Findings"

    # --- Handle "arXiv / ACL Anthology (VENUE Findings)" or similar ---
    findings_in_parens = re.search(
        r'\(([^)]*Findings[^)]*)\)', pub_stripped, re.IGNORECASE
    )
    if findings_in_parens:
        inner = findings_in_parens.group(1).strip()
        # Try "ACL 2025 Findings"
        fm = re.match(r'(\w+)\s+(\d{4})\s+Findings', inner, re.IGNORECASE)
        if fm:
            conf = _normalize_conf_name(fm.group(1))
            if conf:
                return f"{conf} {fm.group(2)} Findings"
        # Try "Findings of ACL 2025"
        fm2 = re.match(r'Findings\s+of\s+(\w+)\s+(\d{4})', inner, re.IGNORECASE)
        if fm2:
            conf = _normalize_conf_name(fm2.group(1))
            if conf:
                return f"{conf} {fm2.group(2)} Findings"

    # --- Check for "Workshop" in pub ---
    if re.search(r'\bworkshop\b', pub_low):
        # Try to extract parent conference
        for alias, canonical in CONFERENCE_ALIASES.items():
            if re.search(rf'\b{re.escape(alias)}\b', pub_low):
                yr = _extract_year(pub_stripped) or year
                return f"{canonical} {yr} Workshop".strip() if yr else f"{canonical} Workshop"
        # Generic workshop
        yr = _extract_year(pub_stripped) or year
        return f"Workshop ({yr})" if yr else "Workshop"

    # --- Check for "Demo" track ---
    if re.search(r'\bdemo\b', pub_low):
        for alias, canonical in CONFERENCE_ALIASES.items():
            if re.search(rf'\b{re.escape(alias)}\b', pub_low):
                yr = _extract_year(pub_stripped) or year
                return f"{canonical} {yr} Demo".strip() if yr else f"{canonical} Demo"

    # --- Check for "Shared task" / evaluation campaign ---
    if re.search(r'\bshared\s+task\b', pub_low) or re.search(r'\biberlef\b', pub_low):
        for alias, canonical in CONFERENCE_ALIASES.items():
            if re.search(rf'\b{re.escape(alias)}\b', pub_low):
                yr = _extract_year(pub_stripped) or year
                return f"{canonical} {yr}".strip() if yr else canonical
        yr = _extract_year(pub_stripped) or year
        return f"Shared Task ({yr})" if yr else "Shared Task"

    # --- Check "Datasets and Benchmarks Track" ---
    if re.search(r'datasets?\s+and\s+benchmarks?\s+track', pub_low):
        for alias, canonical in CONFERENCE_ALIASES.items():
            if re.search(rf'\b{re.escape(alias)}\b', pub_low):
                yr = _extract_year(pub_stripped) or year
                return f"{canonical} {yr} D&B".strip() if yr else f"{canonical} D&B"

    # --- Direct conference match ---
    # Try matching "CONF YEAR" or "CONF'YY" patterns
    conf_year_match = re.match(
        r"^([A-Z][A-Za-z/\-*']+(?:\s+[A-Za-z/\-]+)*)\s*'?(\d{2,4})\b",
        pub_stripped
    )
    if conf_year_match:
        conf_part = conf_year_match.group(1).strip()
        yr_part = conf_year_match.group(2)
        if len(yr_part) == 2:
            yr_part = "20" + yr_part
        conf = _normalize_conf_name(conf_part)
        if conf:
            return f"{conf} {yr_part}"

    # Try the whole pub string as a conference name
    conf = _normalize_conf_name(pub_stripped)
    if conf:
        yr = _extract_year(pub_stripped) or year
        return f"{conf} {yr}".strip() if yr else conf

    # --- Try matching long-form names with year in parens ---
    # "Proceedings of the 30th Conference on Neural Information Processing Systems (NIPS 2016)"
    paren_match = re.search(r'\(([^)]+)\)\s*$', pub_stripped)
    if paren_match:
        inner = paren_match.group(1).strip()
        conf = _normalize_conf_name(inner)
        if conf:
            yr = _extract_year(inner) or _extract_year(pub_stripped) or year
            return f"{conf} {yr}".strip() if yr else conf
        # Also try the text before parens
        before_parens = pub_stripped[:paren_match.start()].strip().rstrip(',')
        conf = _normalize_conf_name(before_parens)
        if conf:
            yr = _extract_year(pub_stripped) or year
            return f"{conf} {yr}".strip() if yr else conf

    # --- Try scanning for known conference abbreviations anywhere in text ---
    # Only for short, unambiguous abbreviations
    SHORT_CONF_ABBREVS = [
        ("neurips", "NeurIPS"), ("nips", "NeurIPS"), ("icml", "ICML"),
        ("iclr", "ICLR"), ("emnlp", "EMNLP"), ("naacl", "NAACL"),
        ("coling", "COLING"), ("eacl", "EACL"), ("aacl", "AACL"),
        ("aaai", "AAAI"), ("ijcai", "IJCAI"), ("aies", "AIES"),
        ("facct", "FAccT"), ("fat\\*", "FAccT"), ("colm", "COLM"),
        ("tacl", "TACL"), ("cvpr", "CVPR"), ("eccv", "ECCV"),
        ("iccv", "ICCV"), ("icwsm", "ICWSM"), ("semeval", "SemEval"),
        ("lrec-coling", "LREC-COLING"), ("lrec", "LREC"),
        ("ranlp", "RANLP"), ("nodalida", "NoDaLiDa"),
        ("propor", "PROPOR"), ("evalita", "EVALITA"),
        ("iberlef", "IberLEF"), ("clef", "CLEF"),
        ("sigir", "SIGIR"), ("kdd", "KDD"), ("cikm", "CIKM"),
        ("asonam", "ASONAM"), ("accv", "ACCV"),
    ]
    for abbrev, canonical in SHORT_CONF_ABBREVS:
        if re.search(rf'\b{abbrev}\b', pub_low):
            yr = _extract_year(pub_stripped) or year
            return f"{canonical} {yr}".strip() if yr else canonical

    # Also check for "ACL" but not as part of other words
    if re.search(r'\bACL\b', pub_stripped) and not re.search(r'ACL\s+Anthology', pub_stripped, re.IGNORECASE):
        yr = _extract_year(pub_stripped) or year
        # Check for Findings
        if re.search(r'\bfindings?\b', pub_low):
            return f"ACL {yr} Findings".strip() if yr else "ACL Findings"
        # Check for SRW
        if re.search(r'\bsrw\b', pub_low):
            return f"ACL {yr} SRW".strip() if yr else "ACL SRW"
        return f"ACL {yr}".strip() if yr else "ACL"

    # --- Journal matching ---
    journal = _match_journal(pub_stripped)
    if journal:
        return journal

    # --- Check for "Springer (VENUE)" ---
    springer_match = re.match(r'^Springer\s*\(([^)]+)\)', pub_stripped, re.IGNORECASE)
    if springer_match:
        inner = springer_match.group(1).strip()
        # Could be a conference or journal
        conf = _normalize_conf_name(inner)
        if conf:
            yr = _extract_year(pub_stripped) or year
            return f"{conf} {yr}".strip() if yr else conf
        journal = _match_journal(inner)
        if journal:
            return journal
        return inner  # Use as-is

    # --- Preprint indicators ---
    if pub_low in PREPRINT_INDICATORS or any(pub_low.startswith(p) for p in ["websearch:", "arxiv (", "arxiv preprint"]):
        return "Preprint"
    if pub_low.startswith("arxiv") and "/" not in pub_low:
        return "Preprint"

    # --- Type-based fallback ---
    if not pub_stripped and paper_type == "preprint":
        return "Preprint"

    # --- Publisher-only (need API) ---
    if pub_low.split()[0] if pub_low else "" in PUBLISHER_ONLY:
        return ""  # Unresolved, try API

    # For "ACL Anthology" alone (no parens, no slash), unresolved
    if pub_low == "acl anthology":
        return ""

    return ""


# ---------------------------------------------------------------------------
# Phase 2: OpenAlex API
# ---------------------------------------------------------------------------

OPENALEX_URL = "https://api.openalex.org/works/https://doi.org/{doi}?select=primary_location,type,title"
OPENALEX_POLITE_EMAIL = "cei-literature-vault@example.com"

_last_openalex_call = 0.0


def _openalex_rate_limit():
    global _last_openalex_call
    elapsed = time.time() - _last_openalex_call
    if elapsed < 0.15:
        time.sleep(0.15 - elapsed)
    _last_openalex_call = time.time()


def classify_phase2(doi: str):
    """Query OpenAlex by DOI. Returns (venue, is_journal) or ("", False)."""
    if not doi:
        return "", False
    _openalex_rate_limit()
    url = OPENALEX_URL.format(doi=doi)
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', f'CEI-Literature-Vault/1.0 (mailto:{OPENALEX_POLITE_EMAIL})')
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except (urllib.error.HTTPError, urllib.error.URLError, Exception) as e:
        return "", False

    # Extract source info
    loc = data.get('primary_location') or {}
    source = loc.get('source') or {}
    source_name = source.get('display_name', '')
    source_type = source.get('type', '')

    if not source_name:
        return "", False

    # Try conference normalization
    conf = _normalize_conf_name(source_name)
    if conf:
        return conf, False  # Conference — caller should add year

    # Check journals
    journal = _match_journal(source_name)
    if journal:
        return journal, True

    # If source_type is "journal", use the name directly
    if source_type == 'journal' and source_name.lower() not in PREPRINT_INDICATORS:
        return source_name, True

    # If source is arXiv or similar, it's a preprint
    if source_name.lower() in PREPRINT_INDICATORS:
        return "Preprint", False

    return source_name, (source_type == 'journal')


# ---------------------------------------------------------------------------
# Phase 3: Semantic Scholar API
# ---------------------------------------------------------------------------

SS_URL_ARXIV = "https://api.semanticscholar.org/graph/v1/paper/ArXiv:{arxiv_id}?fields=venue,year,publicationVenue"
SS_URL_DOI = "https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=venue,year,publicationVenue"

_last_ss_call = 0.0


def _ss_rate_limit():
    global _last_ss_call
    elapsed = time.time() - _last_ss_call
    if elapsed < 4.0:
        time.sleep(4.0 - elapsed)
    _last_ss_call = time.time()


def classify_phase3(arxiv_id: str, doi: str) -> str:
    """Query Semantic Scholar. Returns normalized venue or empty string."""
    if not arxiv_id and not doi:
        return ""

    _ss_rate_limit()

    # Prefer arXiv ID
    if arxiv_id:
        url = SS_URL_ARXIV.format(arxiv_id=arxiv_id)
    else:
        url = SS_URL_DOI.format(doi=doi)

    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)')
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print("  [SS] Rate limited, sleeping 15s...")
            time.sleep(15)
            try:
                req2 = urllib.request.Request(url)
                req2.add_header('User-Agent', 'Mozilla/5.0')
                with urllib.request.urlopen(req2, timeout=15) as resp2:
                    data = json.loads(resp2.read().decode('utf-8'))
            except Exception:
                return ""
        else:
            return ""
    except Exception:
        return ""

    # Extract venue
    venue_name = ""
    if data.get('publicationVenue') and data['publicationVenue'].get('name'):
        venue_name = data['publicationVenue']['name']
    elif data.get('venue'):
        venue_name = data['venue']

    if not venue_name or venue_name.lower() in ('arxiv', 'corr', 'arxiv.org', 'arxiv (cs)'):
        return "Preprint"

    # Try conference normalization
    conf = _normalize_conf_name(venue_name)
    if conf:
        ss_year = str(data.get('year', ''))
        return f"{conf} {ss_year}".strip() if ss_year else conf

    # Journal match
    journal = _match_journal(venue_name)
    if journal:
        return journal

    return venue_name


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def load_papers(batch_start: int = 0, batch_end: int = 0):
    """Load all paper files sorted by name. Returns list of (path, frontmatter, body)."""
    papers = []
    for f in sorted(PAPERS_DIR.iterdir()):
        if f.suffix != '.md':
            continue
        try:
            content = f.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        fm, body = get_frontmatter(content)
        if fm is not None:
            papers.append((f, fm, body))

    if batch_start > 0 and batch_end > 0:
        papers = papers[batch_start - 1:batch_end]

    return papers


def run_report():
    """Print distribution of existing CONF-CC values."""
    dist = Counter()
    total = 0
    has_field = 0

    for f in sorted(PAPERS_DIR.iterdir()):
        if f.suffix != '.md':
            continue
        try:
            content = f.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        fm, _ = get_frontmatter(content)
        if fm is None:
            continue
        total += 1
        val = get_field(fm, 'CONF-CC')
        if val:
            has_field += 1
            dist[val] += 1

    print(f"\n=== CONF-CC Distribution Report ===")
    print(f"Total papers: {total}")
    print(f"Has CONF-CC: {has_field} ({100*has_field/total:.1f}%)")
    print(f"Missing CONF-CC: {total - has_field}")
    print(f"Unique values: {len(dist)}")

    # Category breakdown
    conferences = {k: v for k, v in dist.items() if k not in ("Preprint", "N/A") and not _match_journal(k)}
    journals = {k: v for k, v in dist.items() if _match_journal(k)}
    preprints = dist.get("Preprint", 0)
    na_count = dist.get("N/A", 0)
    other = has_field - sum(conferences.values()) - sum(journals.values()) - preprints - na_count

    print(f"\n--- Categories ---")
    print(f"  Conference papers: {sum(conferences.values())}")
    print(f"  Journal articles:  {sum(journals.values()) + other}")
    print(f"  Preprints:         {preprints}")
    print(f"  N/A:               {na_count}")

    print(f"\n--- Top 40 venues ---")
    for val, count in dist.most_common(40):
        print(f"  [{count:4d}] {val}")


def run_pipeline(phases=(1, 2, 3), dry_run=False, force=False,
                 batch_start=0, batch_end=0):
    """Run the classification pipeline."""
    papers = load_papers(batch_start, batch_end)
    total = len(papers)
    print(f"Loaded {total} papers (batch: {batch_start}-{batch_end})" if batch_start else f"Loaded {total} papers")

    results = []
    stats = Counter()
    phase_stats = Counter()

    for idx, (path, fm, body) in enumerate(papers, 1):
        filename = path.name
        existing = get_field(fm, 'CONF-CC')
        if existing and existing != "N/A" and not force:
            stats['skipped_existing'] += 1
            continue

        pub = get_field(fm, 'publication')
        paper_type = get_field(fm, 'type')
        paper_year = get_field(fm, 'year')
        arxiv_id = extract_arxiv_id(fm)
        doi = extract_doi(fm)

        venue = ""
        phase_used = 0

        # Phase 1: Local heuristic
        if 1 in phases:
            venue = classify_phase1(pub, paper_type, paper_year)
            if venue:
                phase_used = 1

        # Phase 2: OpenAlex (DOI required)
        if not venue and 2 in phases and doi:
            if idx % 50 == 0:
                print(f"  [{idx}/{total}] Phase 2 (OpenAlex) for {filename[:60]}...")
            venue, is_journal = classify_phase2(doi)
            if venue:
                # Add year only for conferences (not journals)
                if not re.search(r'\d{4}', venue) and paper_year and not is_journal:
                    venue = f"{venue} {paper_year}"
                phase_used = 2

        # Phase 3: Semantic Scholar (arXiv or DOI)
        if not venue and 3 in phases and (arxiv_id or doi):
            if idx % 20 == 0 or True:  # Always print for phase 3 (slow)
                print(f"  [{idx}/{total}] Phase 3 (SS) for {filename[:60]}...")
            venue = classify_phase3(arxiv_id, doi)
            if venue:
                phase_used = 3

        # Fallback: type-based
        if not venue:
            if paper_type == "preprint":
                venue = "Preprint"
                phase_used = 0
            elif paper_type in ("journalArticle", "journal_article"):
                # Use publication as-is if it's not a known preprint source
                if pub and pub.lower() not in PREPRINT_INDICATORS and pub.lower() not in PUBLISHER_ONLY:
                    venue = pub
                    phase_used = 0
                else:
                    venue = "N/A"
                    phase_used = 0
            else:
                venue = "N/A"
                phase_used = 0

        # Record
        results.append({
            "file": filename,
            "CONF-CC": venue,
            "phase": phase_used,
            "publication": pub,
            "type": paper_type,
        })
        stats[venue] += 1
        if phase_used > 0:
            phase_stats[f"phase{phase_used}"] += 1
        else:
            phase_stats["fallback"] += 1

        # Write to file
        if not dry_run:
            new_fm = set_field(fm, 'CONF-CC', venue)
            if not validate_frontmatter(new_fm):
                print(f"  WARNING: Validation failed for {filename}, skipping write")
                stats['write_errors'] += 1
                continue
            new_content = f"---{new_fm}\n---\n{body}"
            path.write_text(new_content, encoding='utf-8')

    # Summary
    classified = len(results)
    print(f"\n=== Classification Summary ===")
    print(f"Papers processed: {classified}")
    print(f"Skipped (existing): {stats.get('skipped_existing', 0)}")
    print(f"Write errors: {stats.get('write_errors', 0)}")
    print(f"\n--- Phase attribution ---")
    for k, v in sorted(phase_stats.items()):
        print(f"  {k}: {v}")
    print(f"\n--- Top 30 assigned values ---")
    venue_dist = Counter(r['CONF-CC'] for r in results)
    for val, count in venue_dist.most_common(30):
        print(f"  [{count:4d}] {val}")

    # Save log
    today = datetime.now().strftime('%Y%m%d')
    log_path = LOGS_DIR / f"{today}-conference_classification_cc.json"
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "total_papers": total,
        "classified": classified,
        "skipped_existing": stats.get('skipped_existing', 0),
        "write_errors": stats.get('write_errors', 0),
        "dry_run": dry_run,
        "phases": list(phases),
        "phase_stats": dict(phase_stats),
        "distribution": dict(venue_dist.most_common()),
        "results": results,
    }
    LOGS_DIR.mkdir(exist_ok=True)
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, indent=2, ensure_ascii=False)
    print(f"\nLog saved to: {log_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Conference Classification (CC)")
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--phase', type=int, choices=[1, 2, 3], help='Run single phase only')
    parser.add_argument('--report', action='store_true', help='Print distribution report')
    parser.add_argument('--force', action='store_true', help='Re-classify papers with existing CONF-CC')
    parser.add_argument('batch_range', nargs='*', type=int, help='START END batch range')
    args = parser.parse_args()

    if args.report:
        run_report()
        return

    phases = (args.phase,) if args.phase else (1, 2, 3)
    batch_start = args.batch_range[0] if len(args.batch_range) >= 1 else 0
    batch_end = args.batch_range[1] if len(args.batch_range) >= 2 else 0

    if args.dry_run:
        print("=== DRY RUN (no files will be modified) ===\n")

    run_pipeline(
        phases=phases,
        dry_run=args.dry_run,
        force=args.force,
        batch_start=batch_start,
        batch_end=batch_end,
    )


if __name__ == "__main__":
    main()
