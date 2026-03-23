#!/usr/bin/env python3
"""
Normalize placeholder-author filenames across papers and linked assets.

Scope:
- Targets papers/* where filename contains: results]], retrieved, available, authors, various
- Resolves authors via strict deterministic order:
  1) existing metadata
  2) arXiv API (exact id)
  3) ACL Anthology BibTeX (exact id)
  4) Crossref works/{doi} (exact DOI)
  5) fallback Unknown

Apply behavior:
- Rename paper file stem author token
- Rename matching Lit-WS-PDFs/**/{old_stem}.pdf
- Rename matching PDF Extracts/**/{old_stem}.md
- Update paper frontmatter: authors/first_author/last_author/authors_incomplete/local_pdf/pdf_extract
- Update paper body: ## Authors section and **Authors:** metadata line
- Rewrite exact old->new filename/path references across selected repository folders
- Emit CSV/JSON unresolved reports in logs/

Dry-run is default; use --execute to apply.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as et
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple


SCRIPT_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
if str(WORKSPACE_ROOT / ".agent") not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT / ".agent"))

from vault_config import LOGS_DIR, PAPERS_DIR, PDFS_DIR, PDF_EXTRACTS_DIR, WORKSPACE_ROOT as VC_WORKSPACE_ROOT
from yaml_frontmatter_utils import (  # noqa: E402
    extract_frontmatter,
    parse_frontmatter,
    validate_frontmatter,
)


DATE_TAG = "20260214"
MAP_CSV = LOGS_DIR / f"{DATE_TAG}-placeholder-author-filename-fix-map.csv"
REPORT_JSON = LOGS_DIR / f"{DATE_TAG}-placeholder-author-filename-fix-report.json"
UNRESOLVED_CSV = LOGS_DIR / f"{DATE_TAG}-placeholder-author-filename-fix-unresolved.csv"

TARGET_FILENAME_RE = re.compile(r"(results\]\]|retrieved|available|authors|various)", re.IGNORECASE)
EXPECTED_TARGET_COUNT = 106

PLACEHOLDER_PHRASES = {
    "unknown",
    "authors",
    "multiple authors",
    "various",
    "retrieved",
    "available",
    "not fully listed in search results",
    "not fully listed in search result",
    "authors not fully retrieved",
    "authors not fully available",
    "authors not fully specified",
    "not fully specified",
    "published on arxiv",
}

ARXIV_ID_RE = re.compile(
    r"(?:arxiv\.org/(?:abs|pdf)/|arxiv:\s*)(?P<id>(?:\d{4}\.\d{4,5}|[a-z\-]+/\d{7}))(?:v\d+)?",
    re.IGNORECASE,
)
ACL_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
DOI_RE = re.compile(r"(10\.\d{4,9}/[^\s\"'<>]+)", re.IGNORECASE)
WIKILINK_TARGET_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")

FILE_INVALID_RE = re.compile(r'[\\/:*?"<>|\x00]')

TEXT_FILE_EXTS = {
    ".md",
    ".txt",
    ".csv",
    ".json",
    ".py",
    ".yaml",
    ".yml",
}

SCAN_DIRS = [
    "papers",
    "Authors",
    "PDF Extracts",
    "STATISTICS",
    "logs",
    "PYTHON",
    "docs",
    "_OPERATING-SYSTEM",
]

HTTP_RETRYABLE = {429, 500, 502, 503, 504}
UA = "CEI-Lit-WS/fix-placeholder-author-filenames/1.0"


@dataclass
class RecoveryResult:
    authors: List[str]
    source: str
    source_id: str
    unresolved: bool


@dataclass
class RenamePlan:
    old_paper_path: Path
    old_filename: str
    old_stem: str
    year_token: str
    old_author_slot: str
    title_segment: str
    new_author_slot: str
    new_stem: str
    new_filename: str
    new_paper_path: Path
    frontmatter: str
    body: str
    fields: Dict[str, str]
    recovery: RecoveryResult
    old_local_pdf_raw: str
    old_pdf_extract_raw: str
    old_local_pdf_rel: str
    old_pdf_extract_rel: str
    local_pdf_is_na: bool
    pdf_extract_is_blank: bool
    pdf_matches: List[Path] = field(default_factory=list)
    extract_matches: List[Path] = field(default_factory=list)
    pdf_rename_pairs: List[Tuple[Path, Path]] = field(default_factory=list)
    extract_rename_pairs: List[Tuple[Path, Path]] = field(default_factory=list)
    collision: bool = False
    collision_reasons: List[str] = field(default_factory=list)
    error: str = ""
    applied: bool = False
    paper_renamed: bool = False
    paper_updated: bool = False
    pdf_renamed_count: int = 0
    extract_renamed_count: int = 0
    new_local_pdf_rel: str = ""
    new_pdf_extract_rel: str = ""


def now_iso() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def strip_quotes(text: str) -> str:
    s = (text or "").strip()
    if len(s) >= 2 and ((s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'"))):
        return s[1:-1].strip()
    return s


def normalize_token(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def is_placeholder_name(name: str) -> bool:
    norm = normalize_token(name)
    if not norm:
        return True
    if norm in {"na", "n a", "n", "none"}:
        return True
    for phrase in PLACEHOLDER_PHRASES:
        if phrase in norm:
            return True
    return False


def clean_author_name(name: str) -> str:
    s = strip_quotes(name)
    if s.startswith("[[") and s.endswith("]]"):
        s = s[2:-2]
    # Strip common BibTeX/LaTeX escapes from author names.
    s = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    s = s.replace("{", "").replace("}", "")
    if "|" in s:
        s = s.split("|", 1)[0]
    s = s.strip().strip("[]()")
    s = normalize_spaces(s).strip(" ,;")
    return s


def is_human_like_name(name: str) -> bool:
    cleaned = clean_author_name(name)
    if not cleaned:
        return False
    if is_placeholder_name(cleaned):
        return False
    lower = cleaned.lower()
    if "http://" in lower or "https://" in lower or "doi.org/" in lower:
        return False
    if len(cleaned) > 120:
        return False
    if not re.search(r"[A-Za-z]", cleaned):
        return False
    return True


def dedupe_keep_order(values: Sequence[str]) -> List[str]:
    out: List[str] = []
    seen: Set[str] = set()
    for item in values:
        key = normalize_spaces(item).lower()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(normalize_spaces(item))
    return out


def parse_authors_field(raw_value: str) -> List[str]:
    text = strip_quotes(raw_value)
    if not text:
        return []

    links = [clean_author_name(x) for x in WIKILINK_TARGET_RE.findall(text)]
    if links:
        return dedupe_keep_order([x for x in links if x])

    parts = re.split(r"\s*;\s*|\s+\band\b\s+", text, flags=re.IGNORECASE)
    cleaned = [clean_author_name(x) for x in parts if clean_author_name(x)]
    return dedupe_keep_order(cleaned)


def split_frontmatter(content: str) -> Optional[Tuple[str, str]]:
    """Extract YAML frontmatter from content. Delegates to shared extract_frontmatter()."""
    try:
        fm, body = extract_frontmatter(content)
        return fm, body
    except ValueError:
        return None


def parse_fields(frontmatter: str) -> Dict[str, str]:
    """Parse frontmatter fields. Delegates to shared parse_frontmatter()."""
    return parse_frontmatter(frontmatter)


def get_field(fields: Dict[str, str], key: str) -> str:
    return fields.get(key, "").strip()


def set_or_add_field(frontmatter: str, key: str, raw_value: str) -> str:
    lines = frontmatter.splitlines()
    prefix = f"{key}:"
    replacement = f"{prefix} {raw_value}" if raw_value != "" else f"{prefix} "
    replaced = False
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            lines[i] = replacement
            replaced = True
            break
    if not replaced:
        lines.append(replacement)
    return "\n".join(lines)


def parse_filename_parts(stem: str) -> Optional[Tuple[str, str, str]]:
    parts = stem.split("-", 2)
    if len(parts) != 3:
        return None
    year, author_slot, title_segment = parts
    if not re.fullmatch(r"\d{4}", year):
        return None
    return year, author_slot, title_segment


def sanitize_author_slot(token: str) -> str:
    t = clean_author_name(token)
    t = FILE_INVALID_RE.sub("-", t)
    t = normalize_spaces(t).strip(".")
    if not t:
        return "Unknown"
    return t


def sanitize_stem(stem: str) -> str:
    cleaned = FILE_INVALID_RE.sub("-", stem)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    cleaned = re.sub(r"-{2,}", "-", cleaned)
    return cleaned


def surname_from_author(name: str) -> str:
    cleaned = clean_author_name(name)
    if not cleaned or is_placeholder_name(cleaned):
        return "Unknown"

    if "," in cleaned:
        surname = cleaned.split(",", 1)[0].strip()
    else:
        bits = [x for x in cleaned.split(" ") if x]
        surname = bits[-1] if bits else cleaned

    surname = surname.strip("[](){}<>.,;:!?\"'")
    return sanitize_author_slot(surname or "Unknown")


def is_na_value(raw_value: str) -> bool:
    return normalize_token(strip_quotes(raw_value)) in {"n a", "na", "n", "none"}


def parse_link_or_plain(raw_value: str) -> str:
    value = strip_quotes(raw_value)
    if not value:
        return ""
    if value.startswith("[[") and value.endswith("]]"):
        inner = value[2:-2]
        inner = inner.split("|", 1)[0].strip()
        return inner
    return value.strip()


def path_to_pdf_rel(path: Path) -> str:
    return f"Lit-WS-PDFs/{path.relative_to(PDFS_DIR).as_posix()}"


def path_to_extract_rel(path: Path) -> str:
    return f"PDF Extracts/{path.relative_to(PDF_EXTRACTS_DIR).as_posix()}"


def collect_index(root: Path, ext: str) -> Dict[str, List[Path]]:
    index: Dict[str, List[Path]] = {}
    for path in root.rglob(f"*{ext}"):
        index.setdefault(path.stem, []).append(path)
    for stem in index:
        index[stem] = sorted(index[stem])
    return index


def _http_get(url: str, timeout: int, attempts: int = 3) -> Optional[bytes]:
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except urllib.error.HTTPError as exc:
            if exc.code in HTTP_RETRYABLE and attempt < attempts - 1:
                continue
            return None
        except Exception:
            if attempt < attempts - 1:
                continue
            return None
    return None


class DeterministicResolver:
    def __init__(self, timeout: int = 15):
        self.timeout = timeout
        self.arxiv_cache: Dict[str, Optional[List[str]]] = {}
        self.acl_cache: Dict[str, Optional[List[str]]] = {}
        self.crossref_cache: Dict[str, Optional[List[str]]] = {}

    def from_existing_metadata(self, fields: Dict[str, str]) -> Optional[RecoveryResult]:
        existing_authors = parse_authors_field(get_field(fields, "authors"))
        if existing_authors and all(is_human_like_name(x) for x in existing_authors):
            return RecoveryResult(
                authors=dedupe_keep_order([clean_author_name(x) for x in existing_authors]),
                source="existing_metadata_authors",
                source_id="authors",
                unresolved=False,
            )

        first_author = clean_author_name(get_field(fields, "first_author"))
        last_author = clean_author_name(get_field(fields, "last_author"))
        resolved: List[str] = []
        if is_human_like_name(first_author):
            resolved.append(first_author)
        if is_human_like_name(last_author) and normalize_spaces(last_author).lower() != normalize_spaces(first_author).lower():
            resolved.append(last_author)
        if resolved:
            return RecoveryResult(
                authors=dedupe_keep_order(resolved),
                source="existing_metadata_first_last",
                source_id="first_last",
                unresolved=False,
            )
        return None

    def extract_arxiv_ids(self, fields: Dict[str, str]) -> List[str]:
        out: List[str] = []
        for key in ("url", "external_pdf"):
            text = strip_quotes(get_field(fields, key))
            if not text:
                continue
            for match in ARXIV_ID_RE.finditer(text):
                out.append(match.group("id"))
        return dedupe_keep_order(out)

    def fetch_arxiv(self, arxiv_id: str) -> Optional[List[str]]:
        if arxiv_id in self.arxiv_cache:
            return self.arxiv_cache[arxiv_id]

        encoded = urllib.parse.quote(arxiv_id, safe="")
        url = f"https://export.arxiv.org/api/query?id_list={encoded}&max_results=1"
        raw = _http_get(url, timeout=self.timeout)
        if not raw:
            self.arxiv_cache[arxiv_id] = None
            return None

        try:
            root = et.fromstring(raw)
        except Exception:
            self.arxiv_cache[arxiv_id] = None
            return None

        ns = {"atom": "http://www.w3.org/2005/Atom"}
        names: List[str] = []
        for entry in root.findall("atom:entry", ns):
            for author_elem in entry.findall("atom:author", ns):
                name_elem = author_elem.find("atom:name", ns)
                if name_elem is None or not name_elem.text:
                    continue
                candidate = clean_author_name(name_elem.text)
                if is_human_like_name(candidate):
                    names.append(candidate)

        names = dedupe_keep_order(names)
        self.arxiv_cache[arxiv_id] = names or None
        return self.arxiv_cache[arxiv_id]

    def extract_acl_ids(self, fields: Dict[str, str]) -> List[str]:
        ids: List[str] = []
        for key in ("url", "external_pdf"):
            value = strip_quotes(get_field(fields, key))
            if "aclanthology.org/" not in value.lower():
                continue
            try:
                parsed = urllib.parse.urlsplit(value)
            except Exception:
                continue
            segments = [s for s in parsed.path.split("/") if s]
            if not segments:
                continue
            acl_id = segments[0]
            if acl_id.lower().endswith(".pdf"):
                acl_id = acl_id[:-4]
            if acl_id.lower() in {"events", "anthology", "search"}:
                continue
            if ACL_ID_RE.fullmatch(acl_id) and re.search(r"\d", acl_id):
                ids.append(acl_id)
        return dedupe_keep_order(ids)

    def fetch_acl(self, acl_id: str) -> Optional[List[str]]:
        if acl_id in self.acl_cache:
            return self.acl_cache[acl_id]

        url = f"https://aclanthology.org/{acl_id}.bib"
        raw = _http_get(url, timeout=self.timeout)
        if not raw:
            self.acl_cache[acl_id] = None
            return None

        text = raw.decode("utf-8", errors="ignore")
        m = re.search(r"author\s*=\s*[{\"](?P<authors>.+?)[}\"]\s*,", text, flags=re.IGNORECASE | re.DOTALL)
        if not m:
            self.acl_cache[acl_id] = None
            return None

        raw_authors = m.group("authors")
        pieces = [clean_author_name(x) for x in raw_authors.split(" and ")]
        names = [x for x in pieces if is_human_like_name(x)]
        names = dedupe_keep_order(names)
        self.acl_cache[acl_id] = names or None
        return self.acl_cache[acl_id]

    def extract_dois(self, fields: Dict[str, str]) -> List[str]:
        candidates: List[str] = []
        for key in ("doi", "url", "external_pdf"):
            value = strip_quotes(get_field(fields, key))
            if not value:
                continue
            for m in DOI_RE.finditer(value):
                doi = m.group(1).rstrip(").,;]}").strip()
                if doi:
                    candidates.append(doi.lower())
        return dedupe_keep_order(candidates)

    def fetch_crossref(self, doi: str) -> Optional[List[str]]:
        if doi in self.crossref_cache:
            return self.crossref_cache[doi]

        url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}"
        raw = _http_get(url, timeout=self.timeout)
        if not raw:
            self.crossref_cache[doi] = None
            return None

        try:
            obj = json.loads(raw.decode("utf-8", errors="ignore"))
            message = obj.get("message", {})
            authors_obj = message.get("author", [])
        except Exception:
            self.crossref_cache[doi] = None
            return None

        names: List[str] = []
        for author in authors_obj:
            if not isinstance(author, dict):
                continue
            family = normalize_spaces(str(author.get("family", "")))
            given = normalize_spaces(str(author.get("given", "")))
            full = normalize_spaces(f"{given} {family}").strip()
            if not full:
                full = normalize_spaces(str(author.get("name", "")))
            if is_human_like_name(full):
                names.append(clean_author_name(full))

        names = dedupe_keep_order(names)
        self.crossref_cache[doi] = names or None
        return self.crossref_cache[doi]

    def resolve(self, fields: Dict[str, str]) -> RecoveryResult:
        existing = self.from_existing_metadata(fields)
        if existing:
            return existing

        for arxiv_id in self.extract_arxiv_ids(fields):
            names = self.fetch_arxiv(arxiv_id)
            if names and all(is_human_like_name(x) for x in names):
                return RecoveryResult(authors=names, source="arxiv_api", source_id=arxiv_id, unresolved=False)

        for acl_id in self.extract_acl_ids(fields):
            names = self.fetch_acl(acl_id)
            if names and all(is_human_like_name(x) for x in names):
                return RecoveryResult(authors=names, source="acl_bibtex", source_id=acl_id, unresolved=False)

        for doi in self.extract_dois(fields):
            names = self.fetch_crossref(doi)
            if names and all(is_human_like_name(x) for x in names):
                return RecoveryResult(authors=names, source="crossref_doi", source_id=doi, unresolved=False)

        return RecoveryResult(authors=["Unknown"], source="fallback_unknown", source_id="", unresolved=True)


def choose_new_local_pdf_rel(plan: RenamePlan) -> str:
    if plan.local_pdf_is_na:
        return ""

    renamed_pdf_rels = [path_to_pdf_rel(new) for _old, new in plan.pdf_rename_pairs]
    if plan.old_local_pdf_rel:
        replaced = plan.old_local_pdf_rel.replace(plan.old_stem, plan.new_stem)
        if replaced.startswith("Lit-WS-PDFs/"):
            return replaced
    if renamed_pdf_rels:
        return renamed_pdf_rels[0]
    return ""


def choose_new_pdf_extract_rel(plan: RenamePlan) -> str:
    renamed_extract_rels = [path_to_extract_rel(new) for _old, new in plan.extract_rename_pairs]
    if plan.old_pdf_extract_rel:
        replaced = plan.old_pdf_extract_rel.replace(plan.old_stem, plan.new_stem)
        if replaced.startswith("PDF Extracts/"):
            return replaced
    if renamed_extract_rels:
        return renamed_extract_rels[0]
    return ""


def update_body_authors(body: str, authors: List[str], unresolved: bool) -> str:
    names = ["Unknown"] if unresolved else dedupe_keep_order([clean_author_name(x) for x in authors])
    if not names:
        names = ["Unknown"]

    authors_wikilinks = ", ".join(f"[[{x}]]" for x in names)
    body_authors_line = ", ".join(names)

    authors_section_re = re.compile(r"(?ms)^## Authors\s*\n.*?(?=\n## |\Z)")
    if authors_section_re.search(body):
        body = authors_section_re.sub(lambda _m: f"## Authors\n\n{authors_wikilinks}\n", body, count=1)

    body = re.sub(r"(?m)^\*\*Authors:\*\*.*$", lambda _m: f"**Authors:** {body_authors_line}", body, count=1)
    return body


def build_updated_paper_content(plan: RenamePlan) -> str:
    frontmatter = plan.frontmatter
    body = plan.body

    authors = ["Unknown"] if plan.recovery.unresolved else dedupe_keep_order([clean_author_name(x) for x in plan.recovery.authors])
    if not authors:
        authors = ["Unknown"]

    author_links = [f"[[{name}]]" for name in authors]
    first_author = author_links[0]
    last_author = author_links[-1]

    frontmatter = set_or_add_field(frontmatter, "authors", f"\"{'; '.join(author_links)}\"")
    frontmatter = set_or_add_field(frontmatter, "first_author", f"\"{first_author}\"")
    frontmatter = set_or_add_field(frontmatter, "last_author", f"\"{last_author}\"")
    frontmatter = set_or_add_field(frontmatter, "authors_incomplete", "true" if plan.recovery.unresolved else "false")

    new_local_pdf_rel = choose_new_local_pdf_rel(plan)
    plan.new_local_pdf_rel = new_local_pdf_rel
    if plan.local_pdf_is_na or not new_local_pdf_rel:
        frontmatter = set_or_add_field(frontmatter, "local_pdf", "N/A" if plan.local_pdf_is_na else get_field(plan.fields, "local_pdf"))
    else:
        frontmatter = set_or_add_field(frontmatter, "local_pdf", f"\"[[{new_local_pdf_rel}]]\"")

    new_extract_rel = choose_new_pdf_extract_rel(plan)
    plan.new_pdf_extract_rel = new_extract_rel
    if plan.pdf_extract_is_blank and not new_extract_rel:
        frontmatter = set_or_add_field(frontmatter, "pdf_extract", "")
    elif new_extract_rel:
        frontmatter = set_or_add_field(frontmatter, "pdf_extract", f"\"{new_extract_rel}\"")

    body = update_body_authors(body, authors, unresolved=plan.recovery.unresolved)
    return f"---\n{frontmatter}\n---\n{body}"


def update_extract_content(path: Path, old_stem: str, new_stem: str, dry_run: bool) -> None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if old_stem not in text:
        return
    new_text = text.replace(old_stem, new_stem)
    if new_text != text and not dry_run:
        path.write_text(new_text, encoding="utf-8")


def scan_target_papers() -> List[Path]:
    papers = sorted(PAPERS_DIR.glob("*.md"))
    return [p for p in papers if TARGET_FILENAME_RE.search(p.name)]


def build_plans(resolver: DeterministicResolver, timeout: int) -> Tuple[List[RenamePlan], List[str]]:
    del timeout  # kept for compatibility with caller intent
    targets = scan_target_papers()

    pdf_index = collect_index(PDFS_DIR, ".pdf")
    extract_index = collect_index(PDF_EXTRACTS_DIR, ".md")

    plans: List[RenamePlan] = []
    planning_errors: List[str] = []

    for paper_path in targets:
        text = paper_path.read_text(encoding="utf-8", errors="ignore")
        split = split_frontmatter(text)
        if split is None:
            planning_errors.append(f"{paper_path.name}: frontmatter_unparseable")
            continue

        frontmatter, body = split
        fields = parse_fields(frontmatter)

        stem = paper_path.stem
        parts = parse_filename_parts(stem)
        if not parts:
            planning_errors.append(f"{paper_path.name}: bad_filename_pattern")
            continue
        year_token, old_author_slot, title_segment = parts

        recovery = resolver.resolve(fields)
        new_author_slot = "Unknown" if recovery.unresolved else surname_from_author(recovery.authors[0])
        new_author_slot = sanitize_author_slot(new_author_slot)

        new_stem = sanitize_stem(f"{year_token}-{new_author_slot}-{title_segment}")
        new_filename = f"{new_stem}.md"
        new_paper_path = paper_path.with_name(new_filename)

        old_local_pdf_raw = get_field(fields, "local_pdf")
        old_pdf_extract_raw = get_field(fields, "pdf_extract")
        old_local_pdf_rel = parse_link_or_plain(old_local_pdf_raw)
        old_pdf_extract_rel = parse_link_or_plain(old_pdf_extract_raw)

        local_pdf_is_na = is_na_value(old_local_pdf_raw) or old_local_pdf_raw.strip() == ""
        pdf_extract_is_blank = old_pdf_extract_raw.strip() == ""

        pdf_matches = list(pdf_index.get(stem, []))
        extract_matches = list(extract_index.get(stem, []))
        pdf_rename_pairs = [(src, src.with_name(f"{new_stem}.pdf")) for src in pdf_matches]
        extract_rename_pairs = [(src, src.with_name(f"{new_stem}.md")) for src in extract_matches]

        plan = RenamePlan(
            old_paper_path=paper_path,
            old_filename=paper_path.name,
            old_stem=stem,
            year_token=year_token,
            old_author_slot=old_author_slot,
            title_segment=title_segment,
            new_author_slot=new_author_slot,
            new_stem=new_stem,
            new_filename=new_filename,
            new_paper_path=new_paper_path,
            frontmatter=frontmatter,
            body=body,
            fields=fields,
            recovery=recovery,
            old_local_pdf_raw=old_local_pdf_raw,
            old_pdf_extract_raw=old_pdf_extract_raw,
            old_local_pdf_rel=old_local_pdf_rel,
            old_pdf_extract_rel=old_pdf_extract_rel,
            local_pdf_is_na=local_pdf_is_na,
            pdf_extract_is_blank=pdf_extract_is_blank,
            pdf_matches=pdf_matches,
            extract_matches=extract_matches,
            pdf_rename_pairs=pdf_rename_pairs,
            extract_rename_pairs=extract_rename_pairs,
        )
        plans.append(plan)

    detect_collisions(plans)
    return plans, planning_errors


def detect_collisions(plans: List[RenamePlan]) -> None:
    paper_targets: Dict[Path, List[RenamePlan]] = {}
    for plan in plans:
        if plan.new_paper_path == plan.old_paper_path:
            continue
        paper_targets.setdefault(plan.new_paper_path, []).append(plan)
        if plan.new_paper_path.exists():
            plan.collision = True
            plan.collision_reasons.append(f"paper_target_exists:{plan.new_paper_path.name}")

    for target, target_plans in paper_targets.items():
        if len(target_plans) > 1:
            for plan in target_plans:
                plan.collision = True
                plan.collision_reasons.append(f"paper_target_duplicate:{target.name}")

    asset_targets: Dict[Path, List[RenamePlan]] = {}
    for plan in plans:
        for old_path, new_path in plan.pdf_rename_pairs + plan.extract_rename_pairs:
            if old_path == new_path:
                continue
            asset_targets.setdefault(new_path, []).append(plan)
            if new_path.exists() and new_path != old_path:
                plan.collision = True
                plan.collision_reasons.append(f"asset_target_exists:{new_path}")

    for new_path, target_plans in asset_targets.items():
        if len(target_plans) > 1:
            for plan in target_plans:
                plan.collision = True
                plan.collision_reasons.append(f"asset_target_duplicate:{new_path}")


def apply_renames(plan: RenamePlan, dry_run: bool) -> Tuple[Path, List[Path]]:
    rename_ops: List[Tuple[Path, Path]] = []
    if plan.old_paper_path != plan.new_paper_path:
        rename_ops.append((plan.old_paper_path, plan.new_paper_path))
    rename_ops.extend(plan.pdf_rename_pairs)
    rename_ops.extend(plan.extract_rename_pairs)

    if dry_run:
        new_extract_paths = [dst for _src, dst in plan.extract_rename_pairs]
        return (plan.new_paper_path if plan.old_paper_path != plan.new_paper_path else plan.old_paper_path), new_extract_paths

    rollback: List[Tuple[Path, Path]] = []
    for src, dst in rename_ops:
        if src == dst:
            continue
        src.rename(dst)
        rollback.append((dst, src))

    plan.paper_renamed = plan.old_paper_path != plan.new_paper_path
    plan.pdf_renamed_count = sum(1 for src, dst in plan.pdf_rename_pairs if src != dst)
    plan.extract_renamed_count = sum(1 for src, dst in plan.extract_rename_pairs if src != dst)

    new_paper_path = plan.new_paper_path if plan.old_paper_path != plan.new_paper_path else plan.old_paper_path
    new_extract_paths = [dst for _src, dst in plan.extract_rename_pairs]
    return new_paper_path, new_extract_paths


def collect_replacement_pairs(plans: Iterable[RenamePlan]) -> Tuple[Dict[str, str], List[str]]:
    replacements: Dict[str, str] = {}
    conflicts: List[str] = []

    def add(old: str, new: str) -> None:
        if not old or not new or old == new:
            return
        current = replacements.get(old)
        if current and current != new:
            conflicts.append(f"{old} -> {current} / {new}")
            return
        replacements[old] = new

    for plan in plans:
        if plan.error or plan.collision:
            continue
        if plan.old_filename != plan.new_filename:
            add(plan.old_filename, plan.new_filename)
            add(f"papers/{plan.old_filename}", f"papers/{plan.new_filename}")
            add(f"[[papers/{plan.old_filename}]]", f"[[papers/{plan.new_filename}]]")
            add(f"[[papers/{plan.old_filename}|", f"[[papers/{plan.new_filename}|")

        old_pdf_name = f"{plan.old_stem}.pdf"
        new_pdf_name = f"{plan.new_stem}.pdf"
        old_md_name = f"{plan.old_stem}.md"
        new_md_name = f"{plan.new_stem}.md"
        add(old_pdf_name, new_pdf_name)
        add(old_md_name, new_md_name)
        add(f"[[{plan.old_stem}]]", f"[[{plan.new_stem}]]")
        add(f"[[{plan.old_stem}|", f"[[{plan.new_stem}|")
        add(f"# PDF Extract: {plan.old_stem}", f"# PDF Extract: {plan.new_stem}")
        add(f"title: \"{plan.old_stem} - PDF Extract\"", f"title: \"{plan.new_stem} - PDF Extract\"")

        for old_path, new_path in plan.pdf_rename_pairs:
            old_rel = path_to_pdf_rel(old_path)
            new_rel = path_to_pdf_rel(new_path)
            add(old_rel, new_rel)
            add(f"[[{old_rel}]]", f"[[{new_rel}]]")
            add(f"[[{old_rel}|", f"[[{new_rel}|")

        for old_path, new_path in plan.extract_rename_pairs:
            old_rel = path_to_extract_rel(old_path)
            new_rel = path_to_extract_rel(new_path)
            add(old_rel, new_rel)
            add(f"[[{old_rel}]]", f"[[{new_rel}]]")
            add(f"[[{old_rel}|", f"[[{new_rel}|")

    return replacements, conflicts


def iter_text_files() -> List[Path]:
    files: List[Path] = []
    for rel in SCAN_DIRS:
        directory = VC_WORKSPACE_ROOT / rel
        if not directory.exists():
            continue
        for path in directory.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in TEXT_FILE_EXTS:
                continue
            files.append(path)
    return sorted(files)


def apply_repo_replacements(
    replacements: Dict[str, str],
    dry_run: bool,
    skip_paths: Optional[Set[Path]] = None,
) -> Dict[str, object]:
    skip_paths = skip_paths or set()
    ordered = sorted(replacements.items(), key=lambda item: len(item[0]), reverse=True)

    files_scanned = 0
    files_changed = 0
    replacement_count = 0
    changed_files: List[str] = []

    for path in iter_text_files():
        files_scanned += 1
        if path in skip_paths:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        new_text = text
        local_count = 0
        for old, new in ordered:
            if old in new_text:
                count = new_text.count(old)
                if count > 0:
                    new_text = new_text.replace(old, new)
                    local_count += count
        if local_count > 0:
            files_changed += 1
            replacement_count += local_count
            changed_files.append(path.relative_to(VC_WORKSPACE_ROOT).as_posix())
            if not dry_run:
                path.write_text(new_text, encoding="utf-8")

    return {
        "files_scanned": files_scanned,
        "files_changed": files_changed,
        "replacement_count": replacement_count,
        "changed_files": changed_files,
    }


def validate_local_pdf_wikilinks(plans: Iterable[RenamePlan]) -> List[str]:
    issues: List[str] = []
    for plan in plans:
        paper_path = plan.new_paper_path if plan.paper_renamed else plan.old_paper_path
        if not paper_path.exists():
            continue
        text = paper_path.read_text(encoding="utf-8", errors="ignore")
        split = split_frontmatter(text)
        if split is None:
            issues.append(f"{paper_path.name}: frontmatter_unparseable")
            continue
        fields = parse_fields(split[0])
        raw = get_field(fields, "local_pdf")
        if not raw or is_na_value(raw):
            continue
        value = strip_quotes(raw)
        if not (value.startswith("[[") and value.endswith("]]")):
            issues.append(f"{paper_path.name}: local_pdf_not_wikilink:{value}")
            continue
        inner = value[2:-2]
        if "]]" in inner:
            issues.append(f"{paper_path.name}: local_pdf_contains_double_bracket:{value}")
            continue
        if not inner.startswith("Lit-WS-PDFs/"):
            issues.append(f"{paper_path.name}: local_pdf_not_pdfs_path:{value}")
    return issues


def find_stale_old_refs(
    replacements: Dict[str, str],
    skip_paths: Optional[Set[Path]] = None,
) -> List[str]:
    skip_paths = skip_paths or set()
    stale: List[str] = []
    search_items = sorted(replacements.keys(), key=len, reverse=True)
    for path in iter_text_files():
        if path in skip_paths:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for old in search_items:
            if old and old in text:
                stale.append(f"{path.relative_to(VC_WORKSPACE_ROOT).as_posix()}::{old}")
    return stale


def write_csv(path: Path, fieldnames: List[str], rows: List[Dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def plan_status(plan: RenamePlan) -> str:
    if plan.error:
        return "error"
    if plan.collision:
        return "collision"
    if plan.applied:
        return "applied"
    return "planned"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize placeholder author filenames and linked assets.")
    parser.add_argument("--execute", action="store_true", help="Apply all changes. Default is dry-run.")
    parser.add_argument("--expected-count", type=int, default=EXPECTED_TARGET_COUNT, help="Expected target paper count.")
    parser.add_argument("--probe-timeout", type=int, default=15, help="HTTP timeout in seconds for deterministic APIs.")
    parser.add_argument("--map-csv", type=Path, default=MAP_CSV, help="Output CSV map path.")
    parser.add_argument("--report-json", type=Path, default=REPORT_JSON, help="Output report JSON path.")
    parser.add_argument("--unresolved-csv", type=Path, default=UNRESOLVED_CSV, help="Output unresolved CSV path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    dry_run = not args.execute

    resolver = DeterministicResolver(timeout=args.probe_timeout)
    plans, planning_errors = build_plans(resolver=resolver, timeout=args.probe_timeout)

    initial_target_count = len(plans)
    _unused_replacements, replacement_conflicts = collect_replacement_pairs(plans)

    map_rows: List[Dict[str, object]] = []
    unresolved_rows: List[Dict[str, object]] = []
    changed_files: List[str] = []

    for plan in plans:
        if plan.collision:
            map_rows.append(
                {
                    "old_paper": plan.old_filename,
                    "new_paper": plan.new_filename,
                    "old_stem": plan.old_stem,
                    "new_stem": plan.new_stem,
                    "old_author_slot": plan.old_author_slot,
                    "new_author_slot": plan.new_author_slot,
                    "recovery_source": plan.recovery.source,
                    "recovery_id": plan.recovery.source_id,
                    "status": "collision",
                    "reason": "; ".join(dedupe_keep_order(plan.collision_reasons)),
                    "paper_rename": plan.old_filename != plan.new_filename,
                    "pdf_rename_count": len(plan.pdf_rename_pairs),
                    "extract_rename_count": len(plan.extract_rename_pairs),
                    "local_pdf_old": plan.old_local_pdf_raw,
                    "local_pdf_new": "",
                    "pdf_extract_old": plan.old_pdf_extract_raw,
                    "pdf_extract_new": "",
                }
            )
            if plan.recovery.unresolved:
                unresolved_rows.append(
                    {
                        "paper": plan.old_filename,
                        "old_author_slot": plan.old_author_slot,
                        "new_author_slot": plan.new_author_slot,
                        "recovery_source": plan.recovery.source,
                        "recovery_id": plan.recovery.source_id,
                        "reason": "collision",
                        "url": strip_quotes(get_field(plan.fields, "url")),
                        "external_pdf": strip_quotes(get_field(plan.fields, "external_pdf")),
                        "doi": strip_quotes(get_field(plan.fields, "doi")),
                    }
                )
            continue

        try:
            target_paper_path, new_extract_paths = apply_renames(plan, dry_run=dry_run)
            updated_content = build_updated_paper_content(plan)

            if not dry_run:
                # Validate frontmatter before writing
                try:
                    updated_fm, _updated_body = extract_frontmatter(updated_content)
                    is_valid, fm_issues = validate_frontmatter(updated_fm)
                    if not is_valid:
                        plan.error = f"validate_frontmatter failed: {fm_issues}"
                        raise ValueError(plan.error)
                except ValueError:
                    raise

                target_paper_path.write_text(updated_content, encoding="utf-8")
                plan.paper_updated = True
                changed_files.append(target_paper_path.relative_to(VC_WORKSPACE_ROOT).as_posix())

            # Always update extract metadata references when we have matching extract files.
            for extract_path in new_extract_paths:
                if extract_path.exists():
                    update_extract_content(extract_path, plan.old_stem, plan.new_stem, dry_run=dry_run)
                    if not dry_run:
                        changed_files.append(extract_path.relative_to(VC_WORKSPACE_ROOT).as_posix())

            plan.applied = True
        except Exception as exc:
            plan.error = str(exc)

        map_rows.append(
            {
                "old_paper": plan.old_filename,
                "new_paper": plan.new_filename,
                "old_stem": plan.old_stem,
                "new_stem": plan.new_stem,
                "old_author_slot": plan.old_author_slot,
                "new_author_slot": plan.new_author_slot,
                "recovery_source": plan.recovery.source,
                "recovery_id": plan.recovery.source_id,
                "status": plan_status(plan),
                "reason": "unresolved" if plan.recovery.unresolved else "",
                "paper_rename": plan.old_filename != plan.new_filename,
                "pdf_rename_count": len(plan.pdf_rename_pairs),
                "extract_rename_count": len(plan.extract_rename_pairs),
                "local_pdf_old": plan.old_local_pdf_raw,
                "local_pdf_new": plan.new_local_pdf_rel,
                "pdf_extract_old": plan.old_pdf_extract_raw,
                "pdf_extract_new": plan.new_pdf_extract_rel,
            }
        )

        if plan.recovery.unresolved:
            unresolved_rows.append(
                {
                    "paper": plan.old_filename,
                    "old_author_slot": plan.old_author_slot,
                    "new_author_slot": plan.new_author_slot,
                    "recovery_source": plan.recovery.source,
                    "recovery_id": plan.recovery.source_id,
                    "reason": plan.error or "fallback_unknown",
                    "url": strip_quotes(get_field(plan.fields, "url")),
                    "external_pdf": strip_quotes(get_field(plan.fields, "external_pdf")),
                    "doi": strip_quotes(get_field(plan.fields, "doi")),
                }
            )

    # Repo-wide exact string replacements (including logs)
    applied_or_planned = [p for p in plans if not p.collision and not p.error]
    replacements, replacement_conflicts_apply = collect_replacement_pairs(applied_or_planned)
    replacement_conflicts.extend(replacement_conflicts_apply)

    skip_paths = {args.map_csv, args.unresolved_csv, args.report_json}
    propagation = apply_repo_replacements(replacements, dry_run=dry_run, skip_paths=skip_paths)
    if not dry_run:
        changed_files.extend(propagation["changed_files"])

    # Validation
    local_pdf_issues = validate_local_pdf_wikilinks(applied_or_planned) if not dry_run else []
    stale_refs = find_stale_old_refs(replacements, skip_paths=skip_paths) if not dry_run else []

    # Reports
    args.map_csv.parent.mkdir(parents=True, exist_ok=True)
    args.unresolved_csv.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.parent.mkdir(parents=True, exist_ok=True)

    write_csv(
        args.map_csv,
        [
            "old_paper",
            "new_paper",
            "old_stem",
            "new_stem",
            "old_author_slot",
            "new_author_slot",
            "recovery_source",
            "recovery_id",
            "status",
            "reason",
            "paper_rename",
            "pdf_rename_count",
            "extract_rename_count",
            "local_pdf_old",
            "local_pdf_new",
            "pdf_extract_old",
            "pdf_extract_new",
        ],
        map_rows,
    )
    write_csv(
        args.unresolved_csv,
        [
            "paper",
            "old_author_slot",
            "new_author_slot",
            "recovery_source",
            "recovery_id",
            "reason",
            "url",
            "external_pdf",
            "doi",
        ],
        unresolved_rows,
    )

    target_count = initial_target_count
    collision_count = sum(1 for p in plans if p.collision)
    error_count = sum(1 for p in plans if p.error)
    unresolved_count = sum(1 for p in plans if p.recovery.unresolved)
    renamed_papers = sum(1 for p in plans if p.old_filename != p.new_filename and not p.collision and not p.error)
    renamed_pdfs = sum(len(p.pdf_rename_pairs) for p in plans if not p.collision and not p.error)
    renamed_extracts = sum(len(p.extract_rename_pairs) for p in plans if not p.collision and not p.error)

    summary = {
        "generated_at": now_iso(),
        "dry_run": dry_run,
        "target_count": target_count,
        "expected_target_count": args.expected_count,
        "target_count_matches_expected": target_count == args.expected_count,
        "planning_errors": planning_errors,
        "replacement_conflicts": replacement_conflicts,
        "collision_count": collision_count,
        "error_count": error_count,
        "unresolved_count": unresolved_count,
        "renamed_papers": renamed_papers,
        "renamed_pdfs": renamed_pdfs,
        "renamed_extracts": renamed_extracts,
        "repo_reference_rewrite": propagation,
        "validation": {
            "local_pdf_issues": local_pdf_issues,
            "stale_old_references": stale_refs,
        },
        "changed_files": sorted(dedupe_keep_order(changed_files)),
        "unresolved_papers": [p.old_filename for p in plans if p.recovery.unresolved],
        "collisions": [
            {"paper": p.old_filename, "reasons": dedupe_keep_order(p.collision_reasons)}
            for p in plans
            if p.collision
        ],
        "errors": [{"paper": p.old_filename, "error": p.error} for p in plans if p.error],
    }
    args.report_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("=" * 88)
    print(f"Placeholder Author Filename Fix {'(DRY RUN)' if dry_run else '(EXECUTE)'}")
    print("=" * 88)
    print(f"Target papers: {target_count} (expected {args.expected_count})")
    print(f"Collisions: {collision_count}")
    print(f"Errors: {error_count}")
    print(f"Unresolved fallback (Unknown): {unresolved_count}")
    print(f"Planned/Applied paper renames: {renamed_papers}")
    print(f"Planned/Applied PDF renames: {renamed_pdfs}")
    print(f"Planned/Applied extract renames: {renamed_extracts}")
    print(
        "Reference propagation: "
        f"{propagation['files_changed']} files, {propagation['replacement_count']} replacements"
    )
    print(f"Map CSV: {args.map_csv}")
    print(f"Report JSON: {args.report_json}")
    print(f"Unresolved CSV: {args.unresolved_csv}")

    if planning_errors:
        print("\nPlanning errors:")
        for item in planning_errors:
            print(f"  - {item}")
    if replacement_conflicts:
        print("\nReplacement conflicts:")
        for item in replacement_conflicts[:30]:
            print(f"  - {item}")
        if len(replacement_conflicts) > 30:
            print(f"  - ... {len(replacement_conflicts) - 30} more")
    if not dry_run and local_pdf_issues:
        print("\nlocal_pdf validation issues:")
        for item in local_pdf_issues[:30]:
            print(f"  - {item}")
        if len(local_pdf_issues) > 30:
            print(f"  - ... {len(local_pdf_issues) - 30} more")
    if not dry_run and stale_refs:
        print("\nStale old-reference hits:")
        for item in stale_refs[:30]:
            print(f"  - {item}")
        if len(stale_refs) > 30:
            print(f"  - ... {len(stale_refs) - 30} more")

    if target_count != args.expected_count:
        return 2
    if error_count > 0:
        return 1
    if not dry_run and (local_pdf_issues or stale_refs):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
