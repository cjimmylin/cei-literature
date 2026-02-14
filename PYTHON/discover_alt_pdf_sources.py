#!/usr/bin/env python3
"""
Discover alternate PDF sources for unresolved papers.

This script does NOT download or modify papers. It only identifies candidate
PDF source URLs and scores them for manual/automated follow-up.

Default input:
  logs/20260214-unresolved-pdf-action-list.csv

Outputs:
  logs/20260214-alt-method-source-candidates.csv
  logs/20260214-alt-method-source-candidates.json
  logs/20260214-alt-method-priority-shortlist.csv
  logs/20260214-alt-method-summary.json
"""

from __future__ import annotations

import argparse
import csv
import difflib
import functools
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

print = functools.partial(print, flush=True)

WORKSPACE = Path(__file__).resolve().parents[1]
PAPERS_DIR = WORKSPACE / "papers"
LOGS_DIR = WORKSPACE / "logs"

UA = (
    "CEI-Lit-WS/alt-source-finder/1.0 "
    "(Academic Research; mailto:research@cei-literature.org)"
)
HEADERS = {"User-Agent": UA}
UNPAYWALL_EMAIL = "research@cei-literature.org"
RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_space(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def normalize_title(s: str) -> str:
    s = normalize_space(s).lower()
    s = re.sub(r"\[[^\]]+\]", " ", s)
    s = re.sub(r"\([^)]*\)", " ", s)
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def title_similarity(a: str, b: str) -> float:
    na = normalize_title(a)
    nb = normalize_title(b)
    if not na or not nb:
        return 0.0
    return difflib.SequenceMatcher(None, na, nb).ratio()


def extract_field(text: str, name: str) -> str:
    m = re.search(rf"^{re.escape(name)}:\s*(.*)$", text, re.MULTILINE)
    if not m:
        return ""
    val = m.group(1).strip().strip('"').strip("'")
    if val.startswith("[[") and val.endswith("]]"):
        val = val[2:-2]
    return val.strip()


def parse_paper_meta(paper_path: Path) -> dict:
    text = paper_path.read_text(encoding="utf-8", errors="ignore")
    short_title = extract_field(text, "short_title")
    title = short_title or extract_field(text, "title") or paper_path.stem
    doi = extract_field(text, "doi")
    url = extract_field(text, "url")
    external_pdf = extract_field(text, "external_pdf")
    first_author = extract_field(text, "first_author").replace("[[", "").replace("]]", "")
    publication = extract_field(text, "publication")
    year = extract_field(text, "year")

    if (not doi) and url:
        m = re.search(r"doi\.org/(10\.[^/?#\s]+(?:/[^\s?#]+)?)", url, flags=re.I)
        if m:
            doi = m.group(1).rstrip(" .")

    if doi:
        doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
        doi = doi.replace("doi:", "").strip().rstrip(".")

    return {
        "paper": paper_path.name,
        "paper_path": str(paper_path),
        "title": normalize_space(title),
        "doi": doi,
        "url": url,
        "external_pdf": external_pdf,
        "first_author": first_author,
        "publication": publication,
        "year": year,
    }


def canonicalize_url(url: str) -> str:
    if not url:
        return ""
    url = url.strip().replace("&amp;", "&")
    parsed = urllib.parse.urlsplit(url)
    if not parsed.scheme:
        return ""
    # Remove fragments; keep query.
    parsed = parsed._replace(fragment="")
    return urllib.parse.urlunsplit(parsed)


def get_host(url: str) -> str:
    try:
        return urllib.parse.urlsplit(url).netloc.lower()
    except Exception:
        return ""


def request_bytes(url: str, timeout: int = 18) -> Tuple[int, str, str, bytes]:
    req = urllib.request.Request(
        url,
        headers={
            **HEADERS,
            "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.8",
            "Range": "bytes=0-2047",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        status = getattr(resp, "status", 200)
        ctype = resp.headers.get("Content-Type", "")
        final = resp.geturl()
        data = resp.read(2048)
        return status, ctype, final, data


def probe_url(url: str) -> dict:
    out = {
        "http_code": "000",
        "content_type": "",
        "probe_kind": "error",
        "final_url": "",
        "note": "",
    }
    try:
        status, ctype, final, data = request_bytes(url)
        out["http_code"] = str(status)
        out["content_type"] = ctype
        out["final_url"] = final
        ctype_l = (ctype or "").lower()

        is_pdf_magic = data.startswith(b"%PDF-")
        is_pdf_ctype = "pdf" in ctype_l
        if is_pdf_magic or is_pdf_ctype or final.lower().endswith(".pdf"):
            out["probe_kind"] = "direct_pdf"
            return out

        if status == 200:
            out["probe_kind"] = "landing_page"
            return out

        out["probe_kind"] = "http_non_200"
        return out
    except urllib.error.HTTPError as e:
        out["http_code"] = str(e.code)
        out["final_url"] = e.geturl() if hasattr(e, "geturl") else ""
        out["content_type"] = e.headers.get("Content-Type", "") if e.headers else ""
        if e.code in (401, 403):
            out["probe_kind"] = "blocked"
        elif e.code in (404, 410):
            out["probe_kind"] = "not_found"
        else:
            out["probe_kind"] = "http_error"
        out["note"] = str(e)
        return out
    except Exception as e:
        out["note"] = str(e)
        return out


def _retry_sleep(attempt: int, retry_after: Optional[str] = None) -> None:
    if retry_after:
        try:
            n = float(retry_after.strip())
            if 0.0 < n <= 60.0:
                time.sleep(n)
                return
        except Exception:
            pass
    # 0.8s, 1.6s, 3.2s
    time.sleep(min(3.2, 0.8 * (2**attempt)))


def safe_api_json(url: str, timeout: int = 18, attempts: int = 3) -> Optional[dict]:
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8", errors="ignore"))
        except urllib.error.HTTPError as e:
            if (e.code in RETRYABLE_HTTP_CODES) and (attempt < attempts - 1):
                _retry_sleep(attempt, e.headers.get("Retry-After") if e.headers else None)
                continue
            return None
        except Exception:
            if attempt < attempts - 1:
                _retry_sleep(attempt)
                continue
            return None
    return None


def fetch_text_with_final(
    url: str,
    timeout: int = 18,
    attempts: int = 3,
) -> Optional[Tuple[str, str]]:
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                final = resp.geturl()
                body = resp.read().decode("utf-8", errors="ignore")
                return final, body
        except urllib.error.HTTPError as e:
            if (e.code in RETRYABLE_HTTP_CODES) and (attempt < attempts - 1):
                _retry_sleep(attempt, e.headers.get("Retry-After") if e.headers else None)
                continue
            return None
        except Exception:
            if attempt < attempts - 1:
                _retry_sleep(attempt)
                continue
            return None
    return None


def safe_api_text(url: str, timeout: int = 18, attempts: int = 3) -> Optional[str]:
    got = fetch_text_with_final(url, timeout=timeout, attempts=attempts)
    if not got:
        return None
    return got[1]


def normalize_doi(s: str) -> str:
    s = (s or "").strip()
    if not s:
        return ""
    s = s.replace("https://doi.org/", "").replace("http://doi.org/", "")
    s = s.replace("doi:", "").strip().rstrip(".")
    return s.lower()


def collect_urls_from_text(text: str) -> List[str]:
    if not text:
        return []
    raw = re.findall(r"https?://[^\s\"'<>]+", text, flags=re.I)
    out: List[str] = []
    seen: Set[str] = set()
    for u in raw:
        cu = canonicalize_url(u.rstrip(").,;]}'\""))
        if cu and cu not in seen:
            seen.add(cu)
            out.append(cu)
    return out


def collect_urls_from_obj(obj: object, limit: int = 120) -> List[str]:
    out: List[str] = []
    seen: Set[str] = set()

    def walk(x: object) -> None:
        if len(out) >= limit:
            return
        if isinstance(x, dict):
            for v in x.values():
                walk(v)
                if len(out) >= limit:
                    return
            return
        if isinstance(x, list):
            for v in x:
                walk(v)
                if len(out) >= limit:
                    return
            return
        if isinstance(x, str):
            for u in collect_urls_from_text(x):
                if u not in seen:
                    seen.add(u)
                    out.append(u)
                    if len(out) >= limit:
                        return

    walk(obj)
    return out


def url_looks_pdfish(url: str) -> bool:
    u = (url or "").lower()
    if not u.startswith("http"):
        return False
    signals = (
        ".pdf",
        "/pdf",
        "blobtype=pdf",
        "download",
        "bitstream",
        "fulltext",
        "ptpmcrender.fcgi",
    )
    return any(sig in u for sig in signals)


def maybe_arxiv_pdf(url: str) -> List[str]:
    url = canonicalize_url(url)
    if not url:
        return []
    out = [url]
    m = re.search(r"arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5})(v\d+)?", url, flags=re.I)
    if m:
        aid = m.group(1)
        ver = m.group(2) or ""
        out.append(f"https://arxiv.org/pdf/{aid}{ver}.pdf")
    return out


def semantic_scholar_record_to_candidates(
    meta: dict,
    rec: dict,
    method: str,
    method_detail_prefix: str,
    sim_override: Optional[float] = None,
) -> List[dict]:
    out = []
    source_title = normalize_space(rec.get("title", ""))
    ext_ids = rec.get("externalIds") or {}
    source_doi = normalize_doi(ext_ids.get("DOI", ""))
    sim = sim_override if sim_override is not None else title_similarity(meta["title"], source_title)

    oa = rec.get("openAccessPdf") or {}
    oa_url = oa.get("url")
    if oa_url:
        out.append(
            {
                "method": method,
                "method_detail": f"{method_detail_prefix}.openAccessPdf.url",
                "candidate_url": oa_url,
                "source_title": source_title,
                "source_doi": source_doi,
                "title_similarity": sim,
            }
        )

    arxiv_id = (ext_ids.get("ArXiv") or "").strip()
    if arxiv_id and re.fullmatch(r"[0-9]{4}\.[0-9]{4,5}(v\d+)?", arxiv_id):
        out.append(
            {
                "method": method,
                "method_detail": f"{method_detail_prefix}.externalIds.ArXiv",
                "candidate_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
                "source_title": source_title,
                "source_doi": source_doi,
                "title_similarity": sim,
            }
        )

    paper_url = rec.get("url")
    if paper_url and url_looks_pdfish(paper_url):
        out.append(
            {
                "method": method,
                "method_detail": f"{method_detail_prefix}.url",
                "candidate_url": paper_url,
                "source_title": source_title,
                "source_doi": source_doi,
                "title_similarity": sim,
            }
        )
    return out


def semantic_scholar_candidates(meta: dict, cache: dict) -> List[dict]:
    title = meta["title"]
    doi = normalize_doi(meta["doi"])
    out: List[dict] = []

    if doi:
        ck = ("semantic_scholar_doi", doi)
        data = cache.get(ck)
        if data is None:
            url = (
                "https://api.semanticscholar.org/graph/v1/paper/DOI:"
                f"{urllib.parse.quote(doi, safe='')}"
                "?fields=title,openAccessPdf,externalIds,url"
            )
            data = safe_api_json(url, attempts=3)
            cache[ck] = data
            time.sleep(0.9)
        if isinstance(data, dict) and data.get("title"):
            out.extend(
                semantic_scholar_record_to_candidates(
                    meta=meta,
                    rec=data,
                    method="semantic_scholar_doi",
                    method_detail_prefix="paper",
                )
            )

    ck = ("semantic_scholar_title", normalize_title(title))
    data = cache.get(ck)
    if data is None:
        q = urllib.parse.quote(title[:170])
        url = (
            "https://api.semanticscholar.org/graph/v1/paper/search"
            f"?query={q}&fields=title,openAccessPdf,externalIds,url&limit=5"
        )
        data = safe_api_json(url, attempts=3)
        cache[ck] = data
        time.sleep(1.0)

    for rec in (data or {}).get("data", [])[:5]:
        source_title = rec.get("title", "")
        sim = title_similarity(title, source_title)
        if sim < 0.72:
            continue
        out.extend(
            semantic_scholar_record_to_candidates(
                meta=meta,
                rec=rec,
                method="semantic_scholar_title",
                method_detail_prefix="search",
                sim_override=sim,
            )
        )
    return out


def core_candidates(meta: dict, cache: dict) -> List[dict]:
    title = meta["title"]
    doi = normalize_doi(meta["doi"])
    out: List[dict] = []

    query = f'"{title[:140]}"'
    if doi:
        query = f'doi:"{doi}" OR "{title[:120]}"'
    ck = ("core_search", normalize_title(title), doi)
    data = cache.get(ck)
    if data is None:
        url = (
            "https://api.core.ac.uk/v3/search/works"
            f"?q={urllib.parse.quote(query)}&limit=5"
        )
        data = safe_api_json(url, attempts=3)
        cache[ck] = data
        time.sleep(0.8)

    for rec in (data or {}).get("results", [])[:5]:
        source_title = normalize_space(rec.get("title", ""))
        source_doi = normalize_doi(rec.get("doi", ""))
        sim = title_similarity(title, source_title)
        doi_match = bool(doi and source_doi and doi == source_doi)
        if (not doi_match) and sim < 0.70:
            continue

        candidate_urls: List[Tuple[str, str]] = []
        dl = rec.get("downloadUrl")
        if dl:
            candidate_urls.append(("downloadUrl", dl))
        for u in rec.get("sourceFulltextUrls", []) or []:
            if isinstance(u, str):
                candidate_urls.append(("sourceFulltextUrls", u))
        for u in rec.get("links", []) or []:
            if isinstance(u, str):
                candidate_urls.append(("links", u))

        for detail, u in candidate_urls:
            for expanded in maybe_arxiv_pdf(u):
                out.append(
                    {
                        "method": "core",
                        "method_detail": detail,
                        "candidate_url": expanded,
                        "source_title": source_title,
                        "source_doi": source_doi,
                        "title_similarity": sim,
                    }
                )
    return out


def openaire_candidates(meta: dict, cache: dict) -> List[dict]:
    doi = normalize_doi(meta["doi"])
    title = meta["title"]
    if not doi:
        return []

    ck = ("openaire_doi", doi)
    data = cache.get(ck)
    if data is None:
        url = (
            "https://api.openaire.eu/search/publications"
            f"?doi={urllib.parse.quote(doi, safe='')}&format=json"
        )
        data = safe_api_json(url, attempts=3)
        cache[ck] = data
        time.sleep(0.5)

    if not isinstance(data, dict):
        return []

    out: List[dict] = []
    urls = collect_urls_from_obj(data, limit=200)
    for u in urls:
        if not url_looks_pdfish(u):
            continue
        out.append(
            {
                "method": "openaire_doi",
                "method_detail": "json_url_scan",
                "candidate_url": u,
                "source_title": title,
                "source_doi": doi,
                "title_similarity": 1.0,
            }
        )
        if len(out) >= 16:
            break
    return out

def openalex_candidates(meta: dict, cache: dict) -> List[dict]:
    title = meta["title"]
    doi = meta["doi"]
    out = []

    if doi:
        cache_key = ("openalex_doi", doi)
        data = cache.get(cache_key)
        if data is None:
            udoi = urllib.parse.quote(f"https://doi.org/{doi}", safe="")
            url = (
                f"https://api.openalex.org/works/{udoi}"
                f"?select=doi,title,display_name,open_access,primary_location,locations"
                f"&mailto={urllib.parse.quote(UNPAYWALL_EMAIL, safe='')}"
            )
            data = safe_api_json(url, attempts=3)
            cache[cache_key] = data
            time.sleep(0.08)
        if isinstance(data, dict) and data.get("id"):
            out.extend(openalex_work_to_candidates(meta, data, "openalex_doi"))

    cache_key = ("openalex_title", normalize_title(title))
    data = cache.get(cache_key)
    if data is None:
        q = urllib.parse.quote(title[:160])
        url = (
            "https://api.openalex.org/works"
            f"?search={q}&per-page=5"
            "&select=doi,title,display_name,open_access,primary_location,locations"
            f"&mailto={urllib.parse.quote(UNPAYWALL_EMAIL, safe='')}"
        )
        data = safe_api_json(url, attempts=3)
        cache[cache_key] = data
        time.sleep(0.08)

    for work in (data or {}).get("results", [])[:5]:
        sim = title_similarity(title, work.get("display_name") or work.get("title") or "")
        if sim < 0.70:
            continue
        out.extend(openalex_work_to_candidates(meta, work, "openalex_title", sim_override=sim))

    return out


def openalex_work_to_candidates(meta: dict, work: dict, method: str, sim_override: Optional[float] = None) -> List[dict]:
    title_ref = work.get("display_name") or work.get("title") or ""
    sim = sim_override if sim_override is not None else title_similarity(meta["title"], title_ref)
    candidates = []

    oa = work.get("open_access") or {}
    oa_url = oa.get("oa_url")
    if oa_url:
        candidates.append(
            {
                "method": method,
                "method_detail": "open_access.oa_url",
                "candidate_url": oa_url,
                "source_title": title_ref,
                "source_doi": (work.get("doi") or "").replace("https://doi.org/", ""),
                "title_similarity": sim,
            }
        )

    pl = work.get("primary_location") or {}
    pdf_url = pl.get("pdf_url")
    if pdf_url:
        candidates.append(
            {
                "method": method,
                "method_detail": "primary_location.pdf_url",
                "candidate_url": pdf_url,
                "source_title": title_ref,
                "source_doi": (work.get("doi") or "").replace("https://doi.org/", ""),
                "title_similarity": sim,
            }
        )

    for loc in work.get("locations", []) or []:
        lp = loc.get("pdf_url")
        if not lp:
            continue
        candidates.append(
            {
                "method": method,
                "method_detail": "locations.pdf_url",
                "candidate_url": lp,
                "source_title": title_ref,
                "source_doi": (work.get("doi") or "").replace("https://doi.org/", ""),
                "title_similarity": sim,
            }
        )
    return candidates


def unpaywall_candidates(meta: dict, cache: dict) -> List[dict]:
    doi = meta["doi"]
    if not doi:
        return []
    cache_key = ("unpaywall", doi)
    data = cache.get(cache_key)
    if data is None:
        url = (
            "https://api.unpaywall.org/v2/"
            f"{urllib.parse.quote(doi, safe='')}?email={UNPAYWALL_EMAIL}"
        )
        data = safe_api_json(url)
        cache[cache_key] = data
        time.sleep(0.9)

    out = []
    if not isinstance(data, dict):
        return out

    for loc in data.get("oa_locations", []) or []:
        pdf_url = loc.get("url_for_pdf") or loc.get("pdf_url")
        if pdf_url:
            out.append(
                {
                    "method": "unpaywall",
                    "method_detail": "oa_locations.url_for_pdf",
                    "candidate_url": pdf_url,
                    "source_title": data.get("title", ""),
                    "source_doi": doi,
                    "title_similarity": title_similarity(meta["title"], data.get("title", "")),
                }
            )
        elif loc.get("url"):
            out.append(
                {
                    "method": "unpaywall",
                    "method_detail": "oa_locations.url",
                    "candidate_url": loc.get("url"),
                    "source_title": data.get("title", ""),
                    "source_doi": doi,
                    "title_similarity": title_similarity(meta["title"], data.get("title", "")),
                }
            )
    return out


def crossref_candidates(meta: dict, cache: dict) -> List[dict]:
    doi = meta["doi"]
    if not doi:
        return []

    cache_key = ("crossref", doi)
    data = cache.get(cache_key)
    if data is None:
        url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
        data = safe_api_json(url)
        cache[cache_key] = data
        time.sleep(0.03)

    msg = (data or {}).get("message", {})
    if not msg:
        return []

    src_title = ""
    if isinstance(msg.get("title"), list) and msg["title"]:
        src_title = msg["title"][0]

    out = []
    for link in msg.get("link", []) or []:
        u = link.get("URL")
        if not u:
            continue
        out.append(
            {
                "method": "crossref",
                "method_detail": f"link:{link.get('content-type','')}",
                "candidate_url": u,
                "source_title": src_title,
                "source_doi": doi,
                "title_similarity": title_similarity(meta["title"], src_title),
            }
        )
    if msg.get("URL"):
        out.append(
            {
                "method": "crossref",
                "method_detail": "message.URL",
                "candidate_url": msg.get("URL"),
                "source_title": src_title,
                "source_doi": doi,
                "title_similarity": title_similarity(meta["title"], src_title),
            }
        )
    return out


def arxiv_candidates(meta: dict, cache: dict) -> List[dict]:
    title = meta["title"]
    cache_key = ("arxiv", normalize_title(title))
    xml_text = cache.get(cache_key)
    if xml_text is None:
        q = urllib.parse.quote(f'ti:"{title[:120]}"')
        url = (
            "http://export.arxiv.org/api/query"
            f"?search_query={q}&start=0&max_results=3&sortBy=relevance"
        )
        xml_text = safe_api_text(url)
        cache[cache_key] = xml_text
        time.sleep(0.4)

    if not xml_text:
        return []

    out = []
    try:
        root = ET.fromstring(xml_text)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for ent in root.findall("atom:entry", ns)[:3]:
            t_el = ent.find("atom:title", ns)
            i_el = ent.find("atom:id", ns)
            if t_el is None or i_el is None:
                continue
            t = normalize_space(t_el.text or "")
            sim = title_similarity(meta["title"], t)
            if sim < 0.76:
                continue
            arxiv_id = (i_el.text or "").split("/abs/")[-1].strip()
            if not arxiv_id:
                continue
            out.append(
                {
                    "method": "arxiv_title",
                    "method_detail": "atom.entry",
                    "candidate_url": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
                    "source_title": t,
                    "source_doi": "",
                    "title_similarity": sim,
                }
            )
    except Exception:
        return []
    return out


def wayback_candidates(meta: dict, unresolved_row: dict, cache: dict) -> List[dict]:
    bucket = unresolved_row.get("action_bucket", "")
    latest = unresolved_row.get("latest_source_url", "")
    if bucket != "BROKEN_OR_REMOVED_URL" or not latest:
        return []
    latest = canonicalize_url(latest)
    if not latest:
        return []

    cache_key = ("wayback", latest)
    data = cache.get(cache_key)
    if data is None:
        cdx = (
            "https://web.archive.org/cdx/search/cdx"
            f"?url={urllib.parse.quote(latest, safe='')}"
            "&output=json&fl=timestamp,original,statuscode,mimetype"
            "&filter=statuscode:200&limit=5"
        )
        data = safe_api_json(cdx)
        cache[cache_key] = data
        time.sleep(0.2)

    rows = data or []
    if not isinstance(rows, list) or len(rows) < 2:
        return []

    out = []
    for rec in rows[1:]:
        if not isinstance(rec, list) or len(rec) < 4:
            continue
        ts, orig, status, mime = rec[:4]
        wb = f"https://web.archive.org/web/{ts}if_/{orig}"
        out.append(
            {
                "method": "wayback",
                "method_detail": f"cdx:{mime}",
                "candidate_url": wb,
                "source_title": "",
                "source_doi": "",
                "title_similarity": 0.0,
            }
        )
    return out


def transform_known_pdf_urls(seed_url: str, doi: str = "") -> List[str]:
    seed = canonicalize_url(seed_url)
    if not seed:
        return []
    doi_norm = normalize_doi(doi)
    out: List[str] = [seed]
    host = get_host(seed)
    parsed = urllib.parse.urlsplit(seed)
    path = parsed.path or ""

    # Common publisher transforms.
    if "/doi/abs/" in path:
        out.append(seed.replace("/doi/abs/", "/doi/pdf/"))
    if "/doi/full/" in path:
        out.append(seed.replace("/doi/full/", "/doi/pdf/"))
    if "/doi/epdf/" in path:
        out.append(seed.replace("/doi/epdf/", "/doi/pdf/"))
    if ("/doi/" in path) and ("/doi/pdf/" not in path) and ("/doi/pdfdirect/" not in path):
        out.append(seed.rstrip("/") + "/pdf")

    if "wiley.com" in host and "/doi/" in path:
        out.append(seed.replace("/doi/abs/", "/doi/pdfdirect/"))
        out.append(seed.replace("/doi/full/", "/doi/pdfdirect/"))

    if "techrxiv.org" in host and "/doi/" in path:
        out.append(seed.replace("/doi/epdf/", "/doi/pdf/"))
        out.append(seed.replace("/doi/pdf/", "/doi/epdf/"))

    if "sciencedirect.com" in host:
        m = re.search(r"/science/article/pii/([A-Z0-9]+)", path, flags=re.I)
        if m:
            pii = m.group(1)
            out.append(
                f"https://www.sciencedirect.com/science/article/pii/{pii}/pdfft?isDTMRedir=true&download=true"
            )

    if "mdpi.com" in host and ("/pdf" not in path):
        out.append(seed.rstrip("/") + "/pdf")

    if "springer.com" in host and doi_norm:
        out.append(
            "https://link.springer.com/content/pdf/"
            f"{urllib.parse.quote(doi_norm, safe='')}.pdf"
        )

    if "ieee.org" in host:
        m = re.search(r"/document/(\d+)", path)
        if m:
            out.append(f"https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber={m.group(1)}")

    m = re.search(r"arxiv\.org/abs/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)", seed, flags=re.I)
    if m:
        out.append(f"https://arxiv.org/pdf/{m.group(1)}.pdf")

    cleaned: List[str] = []
    seen: Set[str] = set()
    for u in out:
        cu = canonicalize_url(u)
        if cu and cu not in seen:
            seen.add(cu)
            cleaned.append(cu)
    return cleaned


def extract_pdf_links_from_html(url: str, html: str, limit: int = 10) -> List[str]:
    attr_links = re.findall(
        r'(?:href|src|data-pdf-url|data-download-url)=["\']([^"\']+)["\']',
        html,
        flags=re.I,
    )
    out: List[str] = []
    seen: Set[str] = set()
    for link in attr_links:
        full = canonicalize_url(urllib.parse.urljoin(url, link))
        if not full:
            continue
        if (not url_looks_pdfish(full)) and (not full.lower().endswith(".pdf")):
            continue
        if full in seen:
            continue
        seen.add(full)
        out.append(full)
        if len(out) >= limit:
            return out

    for raw in collect_urls_from_text(html):
        if (not url_looks_pdfish(raw)) and (not raw.lower().endswith(".pdf")):
            continue
        if raw in seen:
            continue
        seen.add(raw)
        out.append(raw)
        if len(out) >= limit:
            break
    return out


def collect_seed_urls(meta: dict, row: dict) -> List[Tuple[str, str]]:
    seed_urls: List[Tuple[str, str]] = []
    for field in ("url", "external_pdf"):
        u = meta.get(field, "")
        if u and u.startswith("http"):
            seed_urls.append(("meta_" + field, u))

    latest = row.get("latest_source_url", "")
    if latest and latest.startswith("http"):
        seed_urls.append(("latest_source_url", latest))

    doi = normalize_doi(meta.get("doi", ""))
    if doi:
        seed_urls.append(("doi_resolver", f"https://doi.org/{doi}"))

    out: List[Tuple[str, str]] = []
    seen: Set[str] = set()
    for detail, u in seed_urls:
        cu = canonicalize_url(u)
        if not cu or cu in seen:
            continue
        seen.add(cu)
        out.append((detail, cu))
    return out


def html_link_followups(meta: dict, row: dict, cache: dict) -> List[dict]:
    out = []
    doi = meta.get("doi", "")
    seed_urls = collect_seed_urls(meta, row)

    for detail, seed in seed_urls[:3]:
        for transformed in transform_known_pdf_urls(seed, doi=doi)[:8]:
            out.append(
                {
                    "method": "host_transform",
                    "method_detail": detail,
                    "candidate_url": transformed,
                    "source_title": "",
                    "source_doi": normalize_doi(doi),
                    "title_similarity": 0.0,
                }
            )

        cache_key = ("html_final", seed)
        got = cache.get(cache_key)
        if got is None:
            got = fetch_text_with_final(seed, timeout=16, attempts=2)
            cache[cache_key] = got
            time.sleep(0.1)
        if not got:
            continue
        final_url, html = got

        # Use redirected landing URL as additional transform seed.
        for transformed in transform_known_pdf_urls(final_url, doi=doi)[:8]:
            out.append(
                {
                    "method": "host_transform",
                    "method_detail": f"{detail}:final",
                    "candidate_url": transformed,
                    "source_title": "",
                    "source_doi": normalize_doi(doi),
                    "title_similarity": 0.0,
                }
            )

        for pdf in extract_pdf_links_from_html(final_url or seed, html):
            out.append(
                {
                    "method": "html_pdf_link",
                    "method_detail": detail,
                    "candidate_url": pdf,
                    "source_title": "",
                    "source_doi": normalize_doi(doi),
                    "title_similarity": 0.0,
                }
            )
    return out


def score_candidate(meta: dict, c: dict, probe: dict) -> Tuple[int, str, str]:
    method = c["method"]
    sim = float(c.get("title_similarity") or 0.0)
    doi = (meta.get("doi") or "").lower()
    source_doi = (c.get("source_doi") or "").lower().replace("https://doi.org/", "")
    url = c.get("candidate_url", "").lower()

    base = {
        "unpaywall": 80,
        "crossref": 72,
        "openalex_doi": 78,
        "openalex_title": 66,
        "semantic_scholar_doi": 80,
        "semantic_scholar_title": 67,
        "core": 64,
        "openaire_doi": 62,
        "arxiv_title": 68,
        "wayback": 60,
        "host_transform": 58,
        "html_pdf_link": 56,
        "meta_field": 50,
    }.get(method, 52)

    score = base
    if probe["probe_kind"] == "direct_pdf":
        score += 18
    elif probe["probe_kind"] == "landing_page":
        score -= 10
    elif probe["probe_kind"] == "blocked":
        score -= 20
    elif probe["probe_kind"] in {"not_found", "error"}:
        score -= 28

    if doi and (doi in url or doi.replace("/", "%2f") in url):
        score += 8
    if doi and source_doi and source_doi == doi:
        score += 10
    elif doi and source_doi and source_doi != doi:
        score -= 15

    if sim >= 0.90:
        score += 10
    elif sim >= 0.82:
        score += 6
    elif sim >= 0.75:
        score += 2
    elif sim > 0 and sim < 0.55:
        score -= 8

    # Guardrail: title-only discovery should not look "high confidence" unless
    # title similarity is strong.
    if method in {"openalex_title", "arxiv_title", "semantic_scholar_title"}:
        if sim < 0.82 and not (doi and source_doi and source_doi == doi):
            score = min(score, 68)

    score = max(0, min(100, int(round(score))))
    if score >= 85:
        label = "HIGH"
    elif score >= 70:
        label = "MEDIUM"
    elif score >= 55:
        label = "LOW"
    else:
        label = "VERY_LOW"

    title_only_low = method in {"openalex_title", "arxiv_title", "semantic_scholar_title"} and sim < 0.82

    if probe["probe_kind"] == "direct_pdf" and score >= 70 and not title_only_low:
        action = "TRY_DOWNLOAD"
    elif probe["probe_kind"] == "direct_pdf":
        action = "MANUAL_VERIFY"
    elif probe["probe_kind"] == "blocked" and score >= 60:
        action = "BROWSER_FETCH"
    elif probe["probe_kind"] == "landing_page" and score >= 60:
        action = "OPEN_LANDING_PAGE"
    else:
        action = "LOW_PRIORITY"
    return score, label, action


def collect_candidates_for_paper(meta: dict, unresolved_row: dict, cache: dict) -> List[dict]:
    collected: List[dict] = []
    seen = set()

    def add(c: dict):
        cu = canonicalize_url(c.get("candidate_url", ""))
        if not cu or not cu.startswith("http"):
            return
        k = (c["method"], cu)
        if k in seen:
            return
        seen.add(k)
        x = dict(c)
        x["candidate_url"] = cu
        collected.append(x)

    # Metadata fields first.
    for field in ("external_pdf", "url"):
        u = canonicalize_url(meta.get(field, ""))
        if u:
            add(
                {
                    "method": "meta_field",
                    "method_detail": field,
                    "candidate_url": u,
                    "source_title": "",
                    "source_doi": meta.get("doi", ""),
                    "title_similarity": 0.0,
                }
            )
    latest = canonicalize_url(unresolved_row.get("latest_source_url", ""))
    if latest:
        add(
            {
                "method": "meta_field",
                "method_detail": "latest_source_url",
                "candidate_url": latest,
                "source_title": "",
                "source_doi": meta.get("doi", ""),
                "title_similarity": 0.0,
            }
        )

    for c in unpaywall_candidates(meta, cache):
        add(c)
    for c in crossref_candidates(meta, cache):
        add(c)
    for c in semantic_scholar_candidates(meta, cache):
        add(c)
    for c in core_candidates(meta, cache):
        add(c)
    for c in openaire_candidates(meta, cache):
        add(c)
    for c in openalex_candidates(meta, cache):
        add(c)
    for c in arxiv_candidates(meta, cache):
        add(c)
    for c in wayback_candidates(meta, unresolved_row, cache):
        add(c)
    for c in html_link_followups(meta, unresolved_row, cache):
        add(c)

    return collected


def choose_default_input() -> Path:
    # Prefer 20260214 list; fallback to latest unresolved list.
    preferred = LOGS_DIR / "20260214-unresolved-pdf-action-list.csv"
    if preferred.exists():
        return preferred
    cands = sorted(LOGS_DIR.glob("*-unresolved-pdf-action-list.csv"))
    if not cands:
        raise FileNotFoundError("No unresolved action list CSV found in logs/")
    return cands[-1]


def date_prefix_from_path(path: Path) -> str:
    m = re.match(r"^(\d{8})-", path.name)
    if m:
        return m.group(1)
    return datetime.now().strftime("%Y%m%d")


def write_csv(path: Path, rows: List[dict], fields: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)


def main() -> None:
    ap = argparse.ArgumentParser(description="Discover alternative PDF source candidates.")
    ap.add_argument("--input-csv", type=Path, default=None, help="Unresolved action list CSV.")
    ap.add_argument("--limit", type=int, default=0, help="Limit number of papers (0 = all).")
    ap.add_argument("--probe-timeout", type=int, default=18, help="Probe timeout seconds.")
    args = ap.parse_args()

    input_csv = args.input_csv or choose_default_input()
    if not input_csv.exists():
        raise SystemExit(f"Input CSV not found: {input_csv}")

    date_prefix = date_prefix_from_path(input_csv)

    out_candidates_csv = LOGS_DIR / f"{date_prefix}-alt-method-source-candidates.csv"
    out_candidates_json = LOGS_DIR / f"{date_prefix}-alt-method-source-candidates.json"
    out_shortlist_csv = LOGS_DIR / f"{date_prefix}-alt-method-priority-shortlist.csv"
    out_summary_json = LOGS_DIR / f"{date_prefix}-alt-method-summary.json"

    unresolved_rows = list(csv.DictReader(input_csv.open(encoding="utf-8")))
    if args.limit and args.limit > 0:
        unresolved_rows = unresolved_rows[: args.limit]

    print(f"Input unresolved rows: {len(unresolved_rows)}")
    print(f"Source list: {input_csv}")

    cache: Dict[Tuple[str, str], object] = {}
    all_candidate_rows: List[dict] = []
    per_paper_best: Dict[str, dict] = {}

    probe_fn = probe_url
    if args.probe_timeout != 18:
        # Lightweight timeout override wrapper.
        def probe_with_timeout(url: str) -> dict:
            out = {
                "http_code": "000",
                "content_type": "",
                "probe_kind": "error",
                "final_url": "",
                "note": "",
            }
            try:
                status, ctype, final, data = request_bytes(url, timeout=args.probe_timeout)
                out["http_code"] = str(status)
                out["content_type"] = ctype
                out["final_url"] = final
                ctype_l = (ctype or "").lower()
                if data.startswith(b"%PDF-") or "pdf" in ctype_l or final.lower().endswith(".pdf"):
                    out["probe_kind"] = "direct_pdf"
                elif status == 200:
                    out["probe_kind"] = "landing_page"
                else:
                    out["probe_kind"] = "http_non_200"
            except urllib.error.HTTPError as e:
                out["http_code"] = str(e.code)
                out["final_url"] = e.geturl() if hasattr(e, "geturl") else ""
                out["content_type"] = e.headers.get("Content-Type", "") if e.headers else ""
                if e.code in (401, 403):
                    out["probe_kind"] = "blocked"
                elif e.code in (404, 410):
                    out["probe_kind"] = "not_found"
                else:
                    out["probe_kind"] = "http_error"
                out["note"] = str(e)
            except Exception as e:
                out["note"] = str(e)
            return out

        probe_fn = probe_with_timeout

    for idx, row in enumerate(unresolved_rows, start=1):
        paper = row.get("paper", "")
        paper_path = PAPERS_DIR / paper
        if not paper_path.exists():
            continue
        meta = parse_paper_meta(paper_path)
        print(f"[{idx:03d}/{len(unresolved_rows):03d}] {paper}")

        candidates = collect_candidates_for_paper(meta, row, cache)
        if not candidates:
            continue

        # Probe each candidate URL and score it.
        for c in candidates:
            probe = probe_fn(c["candidate_url"])
            final_url = canonicalize_url(probe.get("final_url", "")) or c["candidate_url"]
            score, label, action = score_candidate(meta, c, probe)

            record = {
                "paper": paper,
                "key": row.get("key", ""),
                "priority_tier": row.get("priority_tier", ""),
                "action_bucket": row.get("action_bucket", ""),
                "title": meta.get("title", ""),
                "doi": meta.get("doi", ""),
                "method": c.get("method", ""),
                "method_detail": c.get("method_detail", ""),
                "source_title": c.get("source_title", ""),
                "source_doi": c.get("source_doi", ""),
                "title_similarity": f"{float(c.get('title_similarity') or 0.0):.3f}",
                "candidate_url": c.get("candidate_url", ""),
                "candidate_host": get_host(c.get("candidate_url", "")),
                "final_url": final_url,
                "final_host": get_host(final_url),
                "http_code": probe.get("http_code", ""),
                "content_type": probe.get("content_type", ""),
                "probe_kind": probe.get("probe_kind", ""),
                "note": probe.get("note", ""),
                "confidence": score,
                "confidence_label": label,
                "recommended_action": action,
            }
            all_candidate_rows.append(record)

            best = per_paper_best.get(paper)
            if best is None:
                per_paper_best[paper] = record
            else:
                # Prefer highest confidence; break ties in favor of direct PDF.
                if (
                    record["confidence"] > best["confidence"]
                    or (
                        record["confidence"] == best["confidence"]
                        and record["probe_kind"] == "direct_pdf"
                        and best["probe_kind"] != "direct_pdf"
                    )
                ):
                    per_paper_best[paper] = record

    # Sort and write outputs.
    all_candidate_rows.sort(
        key=lambda r: (
            r["paper"],
            -int(r["confidence"]),
            0 if r["probe_kind"] == "direct_pdf" else 1,
            r["method"],
        )
    )

    fields = [
        "paper",
        "key",
        "priority_tier",
        "action_bucket",
        "title",
        "doi",
        "method",
        "method_detail",
        "source_title",
        "source_doi",
        "title_similarity",
        "candidate_url",
        "candidate_host",
        "final_url",
        "final_host",
        "http_code",
        "content_type",
        "probe_kind",
        "confidence",
        "confidence_label",
        "recommended_action",
        "note",
    ]
    write_csv(out_candidates_csv, all_candidate_rows, fields)
    out_candidates_json.write_text(
        json.dumps(
            {
                "generated_at": now_iso(),
                "input_csv": str(input_csv),
                "total_unresolved_input": len(unresolved_rows),
                "total_candidate_rows": len(all_candidate_rows),
                "candidates": all_candidate_rows,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    shortlist_rows = [
        r
        for r in per_paper_best.values()
        if (
            r["probe_kind"] == "direct_pdf"
            and r["confidence"] >= 70
            and r["recommended_action"] in {"TRY_DOWNLOAD", "MANUAL_VERIFY"}
        )
    ]
    shortlist_rows.sort(
        key=lambda r: (
            0 if r["priority_tier"] == "P2-Medium" else 1,
            -int(r["confidence"]),
            r["paper"],
        )
    )
    write_csv(out_shortlist_csv, shortlist_rows, fields)

    by_method = Counter(r["method"] for r in all_candidate_rows)
    by_probe = Counter(r["probe_kind"] for r in all_candidate_rows)
    by_conf = Counter(r["confidence_label"] for r in all_candidate_rows)
    best_conf_by_paper = Counter(r["confidence_label"] for r in per_paper_best.values())
    best_probe_by_paper = Counter(r["probe_kind"] for r in per_paper_best.values())

    papers_with_candidates = len(per_paper_best)
    papers_with_direct_pdf = sum(
        1 for r in per_paper_best.values() if r["probe_kind"] == "direct_pdf"
    )
    papers_with_high_medium_direct = sum(
        1
        for r in per_paper_best.values()
        if r["probe_kind"] == "direct_pdf" and r["confidence"] >= 70
    )

    summary = {
        "generated_at": now_iso(),
        "input_csv": str(input_csv),
        "total_unresolved_input": len(unresolved_rows),
        "papers_with_candidates": papers_with_candidates,
        "papers_with_best_direct_pdf": papers_with_direct_pdf,
        "papers_with_best_direct_pdf_conf_70_plus": papers_with_high_medium_direct,
        "total_candidate_rows": len(all_candidate_rows),
        "candidate_rows_by_method": dict(by_method),
        "candidate_rows_by_probe_kind": dict(by_probe),
        "candidate_rows_by_confidence_label": dict(by_conf),
        "best_candidate_by_paper_confidence_label": dict(best_conf_by_paper),
        "best_candidate_by_paper_probe_kind": dict(best_probe_by_paper),
        "outputs": {
            "candidates_csv": str(out_candidates_csv),
            "candidates_json": str(out_candidates_json),
            "priority_shortlist_csv": str(out_shortlist_csv),
            "summary_json": str(out_summary_json),
        },
    }
    out_summary_json.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("\nDiscovery summary")
    print(f"- Papers input: {len(unresolved_rows)}")
    print(f"- Papers with candidates: {papers_with_candidates}")
    print(f"- Best=direct_pdf: {papers_with_direct_pdf}")
    print(f"- Best=direct_pdf with confidence>=70: {papers_with_high_medium_direct}")
    print(f"- Candidate rows: {len(all_candidate_rows)}")
    print(f"- Wrote: {out_candidates_csv}")
    print(f"- Wrote: {out_shortlist_csv}")
    print(f"- Wrote: {out_summary_json}")


if __name__ == "__main__":
    main()
