#!/usr/bin/env python3
"""
Repair paper author frontmatter profiles.

Targets:
- authors
- first_author
- last_author
- authors_incomplete

Policy:
- Canonical format: wikilinked `[[Last, First]]` tokens.
- Full list resolved => authors_incomplete: false
- Unresolved/partial => authors_incomplete: true
- Unresolved with no usable names => [[Unknown]] placeholders.

External resolution order (when network is available):
1) Crossref DOI
2) arXiv API
3) Semantic Scholar title search

If external access is unavailable, the script falls back to local metadata only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from vault_config import LOGS_DIR, PAPERS_DIR

USER_AGENT = "CEI-Lit-WS/author-frontmatter-repair"
PLACEHOLDER_RE = re.compile(
    r"\bunknown\b|not fully listed|authors? not fully|authors? incomplete|"
    r"\bet al\.?\b|and others|results,\s*not fully listed|"
    r"^\[\[\[\[",
    re.IGNORECASE,
)
NA_RE = re.compile(r"^(N/A|NA|NONE|NULL)?$", re.IGNORECASE)

ORGANIZATION_HINT_RE = re.compile(
    r"\b(team|consortium|center|centre|institute|foundation|project|lab|laboratory|group|university|committee|network)\b",
    re.IGNORECASE,
)

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
SUFFIXES = {"Jr", "Jr.", "Sr", "Sr.", "II", "III", "IV", "V", "PhD", "MD"}

TARGET_KEYS = ("first_author", "last_author", "authors", "authors_incomplete")


def split_frontmatter(content: str) -> Optional[Tuple[List[str], str]]:
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---\n", 4)
    if end == -1:
        return None
    frontmatter = content[4:end].split("\n")
    body = content[end + 5 :]
    return frontmatter, body


def strip_wrapping_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and ((value[0] == '"' and value[-1] == '"') or (value[0] == "'" and value[-1] == "'")):
        return value[1:-1].strip()
    return value


def clean_token(token: str) -> str:
    token = token.strip()
    token = strip_wrapping_quotes(token)
    token = token.replace("[[[[", "").replace("]]]]", "")
    token = token.replace("[[", "").replace("]]", "")
    token = token.strip("[](){}")
    token = re.sub(r"\s+", " ", token).strip()
    return token


def is_placeholder(value: str) -> bool:
    value = clean_token(value)
    if not value:
        return True
    if NA_RE.match(value):
        return True
    if PLACEHOLDER_RE.search(value):
        return True
    return False


def maybe_split_comma_list(value: str) -> List[str]:
    # Heuristic: distinguish single "Last, First" from comma-separated names.
    parts = [p.strip() for p in value.split(",") if p.strip()]
    if len(parts) <= 1:
        return [value]
    if len(parts) == 2 and len(parts[0].split()) == 1 and len(parts[1].split()) <= 3:
        # Likely one name in Last, First format.
        return [value]
    return parts


def parse_author_list(raw_value: str) -> Tuple[List[str], bool]:
    """
    Returns (author_tokens, incomplete_hint).
    """
    raw = strip_wrapping_quotes(raw_value)
    if not raw:
        return [], True

    incomplete_hint = False
    if PLACEHOLDER_RE.search(raw):
        incomplete_hint = True

    tokens: List[str]
    if ";" in raw:
        tokens = [t.strip() for t in raw.split(";") if t.strip()]
    elif raw.count("[[") > 1 and "]]," in raw:
        tokens = [t.strip() for t in re.split(r"\]\]\s*,\s*", raw) if t.strip()]
        tokens = [t if t.endswith("]]") else f"{t}]]" for t in tokens]
    elif "," in raw:
        tokens = maybe_split_comma_list(raw)
    else:
        tokens = [raw]

    cleaned: List[str] = []
    for t in tokens:
        ct = clean_token(t)
        if not ct:
            continue
        if PLACEHOLDER_RE.search(ct):
            incomplete_hint = True
            continue
        cleaned.append(ct)

    # Deduplicate while preserving order.
    seen = set()
    out: List[str] = []
    for n in cleaned:
        key = n.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(n)
    return out, incomplete_hint


def extract_field(lines: List[str], key: str) -> Optional[str]:
    prefix = f"{key}:"
    for line in lines:
        if line.startswith(prefix):
            return line[len(prefix) :].strip()
    return None


def extract_body_author_line(body: str) -> Optional[str]:
    # Find first non-empty line after "## Authors"
    match = re.search(r"^## Authors\s*$", body, re.MULTILINE)
    if not match:
        return None
    rest = body[match.end() :]
    for line in rest.splitlines():
        if line.strip():
            return line.strip()
    return None


def extract_metadata_author_line(body: str) -> Optional[str]:
    match = re.search(r"^\*\*Authors:\*\*\s*(.+)$", body, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def canonical_name_last_first(name: str) -> str:
    name = clean_token(name)
    if not name:
        return ""

    if ORGANIZATION_HINT_RE.search(name):
        return name

    # Keep existing Last, First shape.
    if "," in name:
        left, right = [p.strip() for p in name.split(",", 1)]
        if left and right:
            return f"{left}, {right}"
        return name

    parts = name.split()
    if len(parts) == 1:
        return parts[0]

    # Handle suffixes (e.g., "Hal Daumé III" -> "Daumé III, Hal")
    if parts[-1] in SUFFIXES and len(parts) >= 3:
        surname_parts = [parts[-2], parts[-1]]
        given_parts = parts[:-2]
    else:
        surname_parts = [parts[-1]]
        i = len(parts) - 2
        while i >= 0 and parts[i].lower() in PARTICLES:
            surname_parts.insert(0, parts[i])
            i -= 1
        given_parts = parts[: i + 1]

    if not given_parts:
        return " ".join(surname_parts)
    return f"{' '.join(surname_parts)}, {' '.join(given_parts)}"


def to_wikilink(last_first_name: str) -> str:
    value = clean_token(last_first_name)
    return f"[[{value}]]"


def try_crossref(doi: str, timeout: float = 8.0) -> Optional[List[str]]:
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
    for a in authors:
        given = (a.get("given") or "").strip()
        family = (a.get("family") or "").strip()
        full = f"{given} {family}".strip()
        if full:
            out.append(full)
    return out or None


def extract_arxiv_id(url: str) -> str:
    if not url:
        return ""
    match = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5}(?:v\d+)?)", url)
    return match.group(1) if match else ""


def try_arxiv(arxiv_id: str, timeout: float = 8.0) -> Optional[List[str]]:
    if not arxiv_id:
        return None
    api_url = f"http://export.arxiv.org/api/query?search_query=id:{urllib.parse.quote(arxiv_id)}&start=0&max_results=1"
    req = urllib.request.Request(api_url, headers={"User-Agent": USER_AGENT})
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
    for entry in root.findall("atom:entry", ns):
        for author in entry.findall("atom:author", ns):
            name_el = author.find("atom:name", ns)
            if name_el is not None and name_el.text:
                out.append(name_el.text.strip())
    return out or None


def normalize_text_for_match(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def title_similarity_ok(query: str, candidate: str) -> bool:
    q_tokens = set(normalize_text_for_match(query).split())
    c_tokens = set(normalize_text_for_match(candidate).split())
    if not q_tokens or not c_tokens:
        return False
    overlap = len(q_tokens & c_tokens) / max(1, len(q_tokens))
    return overlap >= 0.45


def try_semantic_scholar(title: str, timeout: float = 8.0) -> Optional[List[str]]:
    if not title:
        return None
    url = (
        "https://api.semanticscholar.org/graph/v1/paper/search?"
        f"query={urllib.parse.quote(title)}&limit=1&fields=title,authors"
    )
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status != 200:
                return None
            data = json.loads(response.read().decode("utf-8", errors="ignore"))
    except Exception:
        return None

    rows = data.get("data") or []
    if not rows:
        return None
    top = rows[0]
    cand_title = (top.get("title") or "").strip()
    if cand_title and not title_similarity_ok(title, cand_title):
        return None

    out = []
    for a in top.get("authors", []):
        name = (a.get("name") or "").strip()
        if name:
            out.append(name)
    return out or None


def external_network_available() -> bool:
    # Probe once; if DNS/network blocked, skip all external calls to avoid long timeouts.
    req = urllib.request.Request("https://api.crossref.org/works/10.1038%2Fs41586-020-2649-2", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=5.0) as response:
            return response.status == 200
    except Exception:
        return False


def choose_author_source(
    fields: Dict[str, str],
    body: str,
    external_enabled: bool,
) -> Tuple[List[str], bool, str, bool]:
    """
    Returns: (author_names, incomplete, source_label, attempted_external)
    """
    attempted_external = False
    authors_raw = fields.get("authors", "")
    first_raw = fields.get("first_author", "")
    last_raw = fields.get("last_author", "")
    doi = clean_token(fields.get("doi", ""))
    url = clean_token(fields.get("url", ""))
    short_title = clean_token(fields.get("short_title", ""))

    # 1) External-first aggressive resolution.
    if external_enabled:
        attempted_external = True

        if doi and not is_placeholder(doi):
            authors = try_crossref(doi)
            if authors:
                return authors, False, "crossref_doi", attempted_external

        arxiv_id = extract_arxiv_id(url)
        if arxiv_id:
            authors = try_arxiv(arxiv_id)
            if authors:
                return authors, False, "arxiv", attempted_external

        if short_title and not is_placeholder(short_title):
            authors = try_semantic_scholar(short_title)
            if authors:
                return authors, False, "semantic_scholar", attempted_external

    # 2) Local fallbacks.
    local_names, local_incomplete = parse_author_list(authors_raw)
    if local_names:
        return local_names, local_incomplete, "local_authors_field", attempted_external

    body_author_line = extract_body_author_line(body) or ""
    body_names, body_incomplete = parse_author_list(body_author_line)
    if body_names:
        return body_names, body_incomplete, "local_body_authors", attempted_external

    meta_line = extract_metadata_author_line(body) or ""
    meta_names, meta_incomplete = parse_author_list(meta_line)
    if meta_names:
        return meta_names, meta_incomplete, "local_body_metadata", attempted_external

    # 3) first/last fallback if individually present.
    first_clean = clean_token(first_raw)
    last_clean = clean_token(last_raw)
    names = []
    if first_clean and not is_placeholder(first_clean):
        names.append(first_clean)
    if last_clean and not is_placeholder(last_clean) and last_clean.lower() != first_clean.lower():
        names.append(last_clean)
    if names:
        return names, True, "local_first_last_partial", attempted_external

    return [], True, "unresolved", attempted_external


def build_updated_frontmatter(lines: List[str], authors_links: List[str], incomplete: bool) -> List[str]:
    # Remove target keys, preserving all non-target lines.
    kept = [ln for ln in lines if not any(ln.startswith(f"{k}:") for k in TARGET_KEYS)]

    first = authors_links[0] if authors_links else "[[Unknown]]"
    last = authors_links[-1] if authors_links else "[[Unknown]]"
    authors_value = "; ".join(authors_links) if authors_links else "[[Unknown]]"

    block = [
        f'first_author: "{first}"',
        f'last_author: "{last}"',
        f'authors: "{authors_value}"',
        f"authors_incomplete: {'true' if incomplete else 'false'}",
    ]

    # Insert block after year if present; otherwise after short_title/type/key.
    anchor_candidates = ("year:", "short_title:", "type:", "key:")
    insert_idx = len(kept)
    for i, ln in enumerate(kept):
        if any(ln.startswith(prefix) for prefix in anchor_candidates):
            insert_idx = i + 1

    return kept[:insert_idx] + block + kept[insert_idx:]


def canonicalize_author_list(names: List[str]) -> List[str]:
    out: List[str] = []
    seen = set()
    for n in names:
        canon = canonical_name_last_first(n)
        if not canon:
            continue
        key = canon.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(to_wikilink(canon))
    return out


def is_paper_flagged(lines: List[str]) -> bool:
    fields = {}
    for line in lines:
        if ":" in line:
            k, v = line.split(":", 1)
            if k in TARGET_KEYS:
                fields[k] = v.strip()

    authors = fields.get("authors", "")
    first = fields.get("first_author", "")
    last = fields.get("last_author", "")
    incomplete = fields.get("authors_incomplete", "").strip().strip('"').lower() == "true"

    if incomplete:
        return True
    if not authors or is_placeholder(authors):
        return True
    if not first or is_placeholder(first):
        return True
    if not last or is_placeholder(last):
        return True
    if "[[[[" in authors or "[[[[" in first or "[[[[" in last:
        return True

    # Intentionally do not flag based only on style mismatch (e.g., "First Last" vs "Last, First").
    # This pass is for incomplete/placeholder/malformed author frontmatter repair.
    return False


def repair_paper(path: Path, external_enabled: bool, write: bool) -> Dict:
    content = path.read_text(encoding="utf-8", errors="ignore")
    split = split_frontmatter(content)
    if split is None:
        return {"paper": path.name, "changed": False, "error": "frontmatter_unparseable"}
    lines, body = split

    if not is_paper_flagged(lines):
        return {"paper": path.name, "changed": False, "skipped": "not_flagged"}

    fields = {}
    for line in lines:
        if ":" in line:
            k, v = line.split(":", 1)
            fields[k] = v.strip()

    names, incomplete_hint, source, attempted_external = choose_author_source(fields, body, external_enabled)
    canon_links = canonicalize_author_list(names)

    if not canon_links:
        canon_links = ["[[Unknown]]"]
        incomplete = True
    else:
        incomplete = bool(incomplete_hint)

    new_lines = build_updated_frontmatter(lines, canon_links, incomplete)
    new_content = f"---\n" + "\n".join(new_lines) + "\n---\n" + body

    changed = new_content != content
    if changed and write:
        path.write_text(new_content, encoding="utf-8")

    result = {
        "paper": path.name,
        "changed": changed,
        "source": source,
        "attempted_external": attempted_external,
        "resolved_count": len(canon_links),
        "authors_incomplete": incomplete,
    }
    if canon_links == ["[[Unknown]]"]:
        result["unresolved"] = True
    return result


def summarize(results: List[Dict]) -> Dict[str, int]:
    summary = {
        "papers_scanned": len(results),
        "papers_changed": 0,
        "papers_flagged": 0,
        "resolved_crossref_doi": 0,
        "resolved_arxiv": 0,
        "resolved_semantic_scholar": 0,
        "resolved_local_authors_field": 0,
        "resolved_local_body_authors": 0,
        "resolved_local_body_metadata": 0,
        "resolved_local_first_last_partial": 0,
        "unresolved_unknown": 0,
        "authors_incomplete_true_after": 0,
        "frontmatter_unparseable": 0,
    }
    for r in results:
        if r.get("error") == "frontmatter_unparseable":
            summary["frontmatter_unparseable"] += 1
            continue
        if r.get("skipped") == "not_flagged":
            continue
        summary["papers_flagged"] += 1
        if r.get("changed"):
            summary["papers_changed"] += 1
        src = r.get("source", "")
        if src == "crossref_doi":
            summary["resolved_crossref_doi"] += 1
        elif src == "arxiv":
            summary["resolved_arxiv"] += 1
        elif src == "semantic_scholar":
            summary["resolved_semantic_scholar"] += 1
        elif src == "local_authors_field":
            summary["resolved_local_authors_field"] += 1
        elif src == "local_body_authors":
            summary["resolved_local_body_authors"] += 1
        elif src == "local_body_metadata":
            summary["resolved_local_body_metadata"] += 1
        elif src == "local_first_last_partial":
            summary["resolved_local_first_last_partial"] += 1

        if r.get("unresolved"):
            summary["unresolved_unknown"] += 1
        if r.get("authors_incomplete"):
            summary["authors_incomplete_true_after"] += 1
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Repair incomplete author frontmatter.")
    parser.add_argument("--dry-run", action="store_true", help="Analyze and log without writing files.")
    parser.add_argument(
        "--log-path",
        type=Path,
        default=None,
        help="Optional output log JSON path.",
    )
    args = parser.parse_args()

    date_tag = dt.datetime.now().strftime("%Y%m%d")
    log_path = args.log_path or (LOGS_DIR / f"{date_tag}-author-frontmatter-repair.json")

    external_enabled = external_network_available()
    results: List[Dict] = []
    for paper in sorted(PAPERS_DIR.glob("*.md")):
        results.append(repair_paper(paper, external_enabled=external_enabled, write=not args.dry_run))

    summary = summarize(results)
    summary["external_network_available"] = int(external_enabled)

    report = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "dry_run": args.dry_run,
        "external_network_available": external_enabled,
        "summary": summary,
        "results": results,
    }
    log_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"log_path={log_path}")


if __name__ == "__main__":
    main()
