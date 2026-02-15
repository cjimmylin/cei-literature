#!/usr/bin/env python3
"""
Resolve All Unknown Authors — Combined discover + apply script

Scans all papers with "Unknown" or "[[Unknown]]" in filenames,
resolves via arXiv API, Semantic Scholar API, CrossRef API, and OpenAlex API,
then directly updates YAML and renames files.

Usage:
    cd CEI-Lit-WS
    ../.venv/bin/python PYTHON/resolve_all_unknown_authors.py --dry-run
    ../.venv/bin/python PYTHON/resolve_all_unknown_authors.py
"""

import argparse
import functools
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Tuple

print = functools.partial(print, flush=True)

SCRIPT_DIR = Path(__file__).parent.resolve()
WORKSPACE_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from vault_config import PAPERS_DIR, PDF_EXTRACTS_DIR, PDFS_DIR, LOGS_DIR, AUTHORS_DIR

DATE_PREFIX = date.today().strftime("%Y%m%d")
OUTPUT_JSON = LOGS_DIR / f"{DATE_PREFIX}-all-unknown-authors-resolved.json"

USER_AGENT = "CEI-Literature-Vault/1.0 (mailto:cei-vault@example.com)"

# Rate limits
ARXIV_DELAY = 3.0
CROSSREF_DELAY = 1.0
SEMANTIC_DELAY = 15.0  # very aggressive rate limit — needs long delays
S2_SKIP_UNTIL = 0  # skip S2 until this timestamp if we get 429
OPENALEX_DELAY = 1.0


# ============================================================
# YAML helpers
# ============================================================

def extract_yaml_field(content: str, field: str) -> str:
    m = re.search(rf'^{re.escape(field)}:\s*(.*)', content, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"')
    return ""


def safe_replace_field(content: str, key: str, new_value: str) -> Tuple[str, int]:
    safe_value = new_value.replace('"', "'")
    if any(c in safe_value for c in (':', '[', ']', '{', '}', '#', '&', '*', '!', '|', '>', "'", ',')):
        replacement = f'{key}: "{safe_value}"'
    else:
        replacement = f'{key}: {safe_value}'
    pattern = rf'^{re.escape(key)}:\s*.*$'
    result, count = re.subn(pattern, replacement, content, count=1, flags=re.MULTILINE)
    return result, count


# ============================================================
# Detection
# ============================================================

def find_unknown_papers() -> List[Dict]:
    papers = []
    for p in sorted(PAPERS_DIR.glob("*.md")):
        name = p.name
        if "Unknown" not in name and "[[Unknown]]" not in name:
            continue
        content = p.read_text(encoding="utf-8")
        fm_match = re.match(r"---\n(.*?)\n---\n", content, re.DOTALL)
        if not fm_match:
            continue
        frontmatter = fm_match.group(1)
        fields = {}
        for line in frontmatter.split("\n"):
            m = re.match(r'^([^:]+):\s*(.*)', line)
            if m and not line.startswith("  "):
                fields[m.group(1).strip()] = m.group(2).strip().strip('"')

        title = fields.get("short_title", "") or fields.get("title", "")
        # Clean title of wikilinks
        title = re.sub(r'\[\[([^\]]+)\]\]', r'\1', title)

        papers.append({
            "filename": name,
            "path": str(p),
            "title": title,
            "url": fields.get("url", ""),
            "external_pdf": fields.get("external_pdf", ""),
            "doi": fields.get("doi", ""),
            "first_author": fields.get("first_author", ""),
            "authors": fields.get("authors", ""),
            "year": fields.get("year", ""),
            "local_pdf": fields.get("local_pdf", ""),
            "pdf_extract": fields.get("pdf_extract", ""),
        })
    return papers


# ============================================================
# API resolvers
# ============================================================

def extract_arxiv_id(url: str, external_pdf: str = "") -> Optional[str]:
    for u in [url, external_pdf]:
        if not u:
            continue
        m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", u)
        if m:
            return m.group(1)
    return None


def fetch_arxiv_by_id(arxiv_id: str) -> Optional[List[str]]:
    try:
        url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}&max_results=1"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml_data = resp.read()
        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        authors = []
        for entry in root.findall("atom:entry", ns):
            for a in entry.findall("atom:author", ns):
                name_elem = a.find("atom:name", ns)
                if name_elem is not None and name_elem.text:
                    authors.append(name_elem.text.strip())
        return authors if authors else None
    except Exception as e:
        print(f"    arXiv error: {e}")
        return None


def fetch_arxiv_by_title(title: str) -> Optional[Tuple[List[str], str]]:
    """Search arXiv by title. Returns (authors, arxiv_id) or None."""
    try:
        # Use first 8 significant words
        words = [w for w in title.split() if len(w) > 2][:8]
        query = "+AND+".join(f"ti:{urllib.parse.quote(w)}" for w in words)
        url = f"http://export.arxiv.org/api/query?search_query={query}&max_results=3"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml_data = resp.read()
        root = ET.fromstring(xml_data)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for entry in root.findall("atom:entry", ns):
            entry_title = entry.find("atom:title", ns)
            if entry_title is None or not entry_title.text:
                continue
            if title_match_score(title, entry_title.text.strip()) < 0.7:
                continue
            authors = []
            for a in entry.findall("atom:author", ns):
                name_elem = a.find("atom:name", ns)
                if name_elem is not None and name_elem.text:
                    authors.append(name_elem.text.strip())
            # Get arXiv ID
            aid = ""
            id_elem = entry.find("atom:id", ns)
            if id_elem is not None and id_elem.text:
                m = re.search(r"(\d{4}\.\d{4,5})", id_elem.text)
                if m:
                    aid = m.group(1)
            if authors:
                return (authors, aid)
        return None
    except Exception as e:
        print(f"    arXiv title search error: {e}")
        return None


def fetch_crossref_by_doi(doi: str) -> Optional[List[str]]:
    if not doi:
        return None
    try:
        url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        authors = []
        for a in data.get("message", {}).get("author", []):
            given = a.get("given", "")
            family = a.get("family", "")
            if given and family:
                authors.append(f"{given} {family}")
            elif family:
                authors.append(family)
        return authors if authors else None
    except Exception as e:
        print(f"    CrossRef error: {e}")
        return None


def fetch_semantic_scholar_by_doi(doi: str) -> Optional[List[str]]:
    global S2_SKIP_UNTIL
    if not doi:
        return None
    if time.time() < S2_SKIP_UNTIL:
        print(f"    S2 skip (rate-limited)")
        return None
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{urllib.parse.quote(doi, safe='')}?fields=authors"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        authors = [a["name"] for a in data.get("authors", []) if a.get("name")]
        return authors if authors else None
    except urllib.error.HTTPError as e:
        if e.code == 429:
            S2_SKIP_UNTIL = time.time() + 120  # back off 2 min
            print(f"    S2 429 — backing off 2 min")
        else:
            print(f"    S2 DOI error: {e}")
        return None
    except Exception as e:
        print(f"    S2 DOI error: {e}")
        return None


def fetch_semantic_scholar_by_title(title: str) -> Optional[List[str]]:
    global S2_SKIP_UNTIL
    if time.time() < S2_SKIP_UNTIL:
        print(f"    S2 skip (rate-limited)")
        return None
    try:
        query = urllib.parse.quote(title[:200])
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&fields=authors,title&limit=3"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        for paper in data.get("data", []):
            if title_match_score(title, paper.get("title", "")) < 0.7:
                continue
            authors = [a["name"] for a in paper.get("authors", []) if a.get("name")]
            if authors:
                return authors
        return None
    except urllib.error.HTTPError as e:
        if e.code == 429:
            S2_SKIP_UNTIL = time.time() + 120
            print(f"    S2 429 — backing off 2 min")
        else:
            print(f"    S2 title error: {e}")
        return None
    except Exception as e:
        print(f"    S2 title error: {e}")
        return None


def fetch_openalex_by_title(title: str) -> Optional[List[str]]:
    try:
        query = urllib.parse.quote(title[:200])
        url = f"https://api.openalex.org/works?search={query}&per_page=3&mailto=cei-vault@example.com"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        for work in data.get("results", []):
            work_title = work.get("title", "")
            if title_match_score(title, work_title) < 0.7:
                continue
            authors = []
            for authorship in work.get("authorships", []):
                name = authorship.get("author", {}).get("display_name", "")
                if name:
                    authors.append(name)
            if authors:
                return authors
        return None
    except Exception as e:
        print(f"    OpenAlex error: {e}")
        return None


def title_match_score(t1: str, t2: str) -> float:
    """Word overlap score between two titles."""
    def normalize(t):
        t = re.sub(r'[^\w\s]', '', t.lower())
        return set(t.split())
    w1 = normalize(t1)
    w2 = normalize(t2)
    if not w1 or not w2:
        return 0.0
    overlap = len(w1 & w2)
    return overlap / max(len(w1), len(w2))


# ============================================================
# Author name processing
# ============================================================

def get_first_author_surname(authors: List[str]) -> str:
    """Extract surname from first author for filename."""
    if not authors:
        return "Unknown"
    name = authors[0].strip()
    # Remove affiliation markers
    name = re.sub(r'[∗†‡§¶\d,]+$', '', name).strip()
    # Handle "LastName, FirstName" format
    if ", " in name:
        parts = name.split(", ")
        return parts[0].strip()
    # Handle "FirstName LastName" format
    parts = name.split()
    if len(parts) >= 2:
        return parts[-1].strip()
    return name


def format_authors_for_yaml(authors: List[str]) -> str:
    """Format author list for YAML authors field."""
    cleaned = []
    for a in authors:
        a = re.sub(r'[∗†‡§¶]+', '', a).strip()
        a = a.replace('"', "'")
        if a:
            cleaned.append(a)
    return "; ".join(cleaned)


def make_wikilink_author(name: str) -> str:
    """Format author name as wikilink."""
    name = re.sub(r'[∗†‡§¶]+', '', name).strip()
    name = name.replace('"', "'")
    return f"[[{name}]]"


# ============================================================
# Apply changes
# ============================================================

def apply_resolution(paper: Dict, authors: List[str], source: str, dry_run: bool) -> Dict:
    """Apply author resolution to a paper. Returns result dict."""
    filename = paper["filename"]
    path = Path(paper["path"])
    year = paper["year"] or re.match(r'^(\d{4})', filename).group(1)

    surname = get_first_author_surname(authors)
    authors_str = format_authors_for_yaml(authors)
    first_wikilink = make_wikilink_author(authors[0])
    last_wikilink = make_wikilink_author(authors[-1]) if len(authors) > 1 else first_wikilink

    # Build new filename
    old_stem = filename.rsplit(".", 1)[0]
    # Replace Unknown or [[Unknown]] with surname
    new_stem = re.sub(r'\[\[Unknown\]\]|Unknown', surname, old_stem, count=1)
    new_filename = new_stem + ".md"

    result = {
        "old_filename": filename,
        "new_filename": new_filename,
        "authors": [a for a in authors],
        "first_author": authors[0],
        "last_author": authors[-1] if len(authors) > 1 else authors[0],
        "surname": surname,
        "source": source,
        "changes": [],
    }

    if dry_run:
        result["changes"].append(f"[DRY RUN] Would update YAML and rename to {new_filename}")
        return result

    # 1. Update YAML
    content = path.read_text(encoding="utf-8")

    # Update authors field
    content, n = safe_replace_field(content, "authors", authors_str)
    if n:
        result["changes"].append("updated authors")

    # Update first_author
    content, n = safe_replace_field(content, "first_author", first_wikilink)
    if n:
        result["changes"].append("updated first_author")

    # Update last_author
    content, n = safe_replace_field(content, "last_author", last_wikilink)
    if n:
        result["changes"].append("updated last_author")

    # Remove authors_incomplete if present
    content, n = re.subn(r'^authors_incomplete:\s*.*\n', '', content, count=1, flags=re.MULTILINE)
    if n:
        result["changes"].append("removed authors_incomplete")

    # Update local_pdf reference if it contains Unknown
    old_local_pdf = extract_yaml_field(content, "local_pdf")
    if old_local_pdf and "Unknown" in old_local_pdf:
        new_local_pdf = old_local_pdf.replace("Unknown", surname)
        content, n = safe_replace_field(content, "local_pdf", new_local_pdf)
        if n:
            result["changes"].append("updated local_pdf ref")

    # Update pdf_extract reference if it contains Unknown
    old_extract = extract_yaml_field(content, "pdf_extract")
    if old_extract and "Unknown" in old_extract:
        new_extract = old_extract.replace("Unknown", surname)
        content, n = safe_replace_field(content, "pdf_extract", new_extract)
        if n:
            result["changes"].append("updated pdf_extract ref")

    # Update body Authors section
    content = re.sub(
        r'^(\*\*Authors:\*\*\s*).*$',
        f'\\1{", ".join(authors)}',
        content, count=1, flags=re.MULTILINE
    )

    path.write_text(content, encoding="utf-8")

    # 2. Rename paper file
    if new_filename != filename:
        new_path = PAPERS_DIR / new_filename
        if not new_path.exists():
            path.rename(new_path)
            result["changes"].append(f"renamed paper: {filename} -> {new_filename}")
        else:
            result["changes"].append(f"SKIP rename: {new_filename} already exists")

    # 3. Rename PDF if it contains Unknown
    if old_local_pdf and "Unknown" in old_local_pdf:
        pdf_name = old_local_pdf.replace("[[", "").replace("]]", "")
        pdf_path = WORKSPACE_ROOT.parent / pdf_name
        if pdf_path.exists():
            new_pdf_name = pdf_name.replace("Unknown", surname)
            new_pdf_path = WORKSPACE_ROOT.parent / new_pdf_name
            if not new_pdf_path.exists():
                pdf_path.rename(new_pdf_path)
                result["changes"].append(f"renamed PDF")

    # 4. Rename extract if it contains Unknown
    if old_extract and "Unknown" in old_extract:
        extract_path = WORKSPACE_ROOT / old_extract
        if extract_path.exists():
            new_extract_name = old_extract.replace("Unknown", surname)
            new_extract_path = WORKSPACE_ROOT / new_extract_name
            if not new_extract_path.exists():
                extract_path.rename(new_extract_path)
                result["changes"].append(f"renamed extract")

    return result


# ============================================================
# Main
# ============================================================

def resolve_paper(paper: Dict) -> Tuple[Optional[List[str]], str]:
    """Try all API sources to resolve authors. Returns (authors, source) or (None, "")."""
    title = paper["title"]
    doi = paper["doi"]
    url = paper["url"]
    external_pdf = paper["external_pdf"]

    if not title or len(title) < 5:
        return None, ""

    # 1. arXiv by ID
    arxiv_id = extract_arxiv_id(url, external_pdf)
    if arxiv_id:
        print(f"    Trying arXiv ID: {arxiv_id}")
        authors = fetch_arxiv_by_id(arxiv_id)
        if authors:
            return authors, f"arxiv_id:{arxiv_id}"
        time.sleep(ARXIV_DELAY)

    # 2. CrossRef by DOI
    if doi:
        print(f"    Trying CrossRef DOI: {doi}")
        authors = fetch_crossref_by_doi(doi)
        if authors:
            return authors, f"crossref_doi:{doi}"
        time.sleep(CROSSREF_DELAY)

    # 3. Semantic Scholar by DOI
    if doi:
        print(f"    Trying S2 DOI: {doi}")
        authors = fetch_semantic_scholar_by_doi(doi)
        if authors:
            return authors, f"s2_doi:{doi}"
        time.sleep(SEMANTIC_DELAY)

    # 4. OpenAlex by title (fast, generous rate limit)
    print(f"    Trying OpenAlex title search")
    authors = fetch_openalex_by_title(title)
    if authors:
        return authors, "openalex_title"
    time.sleep(OPENALEX_DELAY)

    # 5. arXiv by title search
    print(f"    Trying arXiv title search")
    result = fetch_arxiv_by_title(title)
    if result:
        return result[0], f"arxiv_title:{result[1]}"
    time.sleep(ARXIV_DELAY)

    # 6. Semantic Scholar by title (last resort, slow)
    print(f"    Trying S2 title search")
    authors = fetch_semantic_scholar_by_title(title)
    if authors:
        return authors, "s2_title"
    time.sleep(SEMANTIC_DELAY)

    return None, ""


def main():
    parser = argparse.ArgumentParser(description="Resolve all Unknown authors")
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    papers = find_unknown_papers()
    print(f"Found {len(papers)} papers with Unknown authors")

    results = {
        "timestamp": date.today().isoformat(),
        "total_found": len(papers),
        "resolved": [],
        "failed": [],
    }

    for i, paper in enumerate(papers, 1):
        print(f"\n[{i}/{len(papers)}] {paper['filename']}")
        print(f"    Title: {paper['title'][:80]}...")

        authors, source = resolve_paper(paper)

        if authors:
            print(f"    RESOLVED via {source}: {authors[0]} et al. ({len(authors)} authors)")
            result = apply_resolution(paper, authors, source, args.dry_run)
            results["resolved"].append(result)
        else:
            print(f"    FAILED - no authors found")
            results["failed"].append({
                "filename": paper["filename"],
                "title": paper["title"],
                "reason": "no_api_match",
            })

    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"  Total:    {len(papers)}")
    print(f"  Resolved: {len(results['resolved'])}")
    print(f"  Failed:   {len(results['failed'])}")
    print(f"{'='*60}")

    # Write results
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResults written to: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
