#!/usr/bin/env python3
"""
Execute Wave3 browser interactive queue batches (P2-P4).

This runner:
1) Attempts candidate URLs per queue row and optional fallback waterfall lookup.
2) Downloads and validates PDFs, then updates paper YAML (external_pdf/local_pdf).
3) Extracts text for newly downloaded PDFs and updates pdf_extract.
4) Refreshes queue CSV/MD/summary and final Wave3 audit snapshot.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import subprocess
import tempfile
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import fitz  # PyMuPDF

import comprehensive_pdf_finder as cpf


ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "papers"
LOGS_DIR = ROOT / "logs"
QUEUE_CSV_DEFAULT = LOGS_DIR / "20260214-wave3-browser-interactive-queue.csv"
QUEUE_MD_DEFAULT = LOGS_DIR / "20260214-wave3-browser-interactive-queue.md"
QUEUE_SUMMARY_DEFAULT = LOGS_DIR / "20260214-wave3-browser-interactive-queue-summary.json"
FINAL_AUDIT_DEFAULT = LOGS_DIR / "20260214-wave3-final-audit-implemented.json"
DATE_PREFIX = "20260214"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "using",
    "into",
    "onto",
    "that",
    "this",
    "these",
    "those",
    "over",
    "under",
    "toward",
    "towards",
    "through",
    "about",
    "between",
    "across",
    "language",
    "languages",
    "model",
    "models",
    "dataset",
    "datasets",
    "study",
    "analysis",
    "benchmark",
    "evaluation",
    "approach",
}

FAILURE_PRIORITY = [
    "HTTP 403",
    "HTTP 401",
    "HTTP 429",
    "HTTP 404",
    "HTTP 500",
    "HTTP 503",
    "not_pdf_header",
    "title_mismatch",
    "too_small",
    "HTTP 000",
    "no_candidate",
    "no_pdf_found",
]


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def now_human() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def load_pdf_root() -> Path:
    config = json.loads((ROOT / ".vault-config.json").read_text(encoding="utf-8"))
    return ROOT / config["pdf_path"]


def parse_year_from_stem(stem: str, fallback_year: str = "0000") -> str:
    m = re.match(r"^(\d{4})-", stem)
    if m:
        return m.group(1)
    m2 = re.match(r"^\d{4}$", fallback_year.strip())
    if m2:
        return m2.group(0)
    return "0000"


def read_queue_rows(queue_csv: Path) -> List[Dict[str, str]]:
    with queue_csv.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def write_queue_rows(queue_csv: Path, rows: List[Dict[str, str]]) -> None:
    if not rows:
        return
    fields = list(rows[0].keys())
    with queue_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def unique_keep_order(values: Iterable[str]) -> List[str]:
    seen = set()
    out: List[str] = []
    for v in values:
        vv = (v or "").strip()
        if not vv or vv in seen:
            continue
        seen.add(vv)
        out.append(vv)
    return out


def normalize_text(text: str) -> str:
    t = (text or "").lower()
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def title_tokens(title: str, cap: int = 7) -> List[str]:
    tokens = []
    for raw in normalize_text(title).split():
        if len(raw) >= 4 and raw not in STOPWORDS:
            tokens.append(raw)
        elif any(ch.isdigit() for ch in raw) and len(raw) >= 2:
            tokens.append(raw)
    if not tokens:
        tokens = [t for t in normalize_text(title).split() if len(t) >= 3]
    deduped = []
    seen = set()
    for t in tokens:
        if t not in seen:
            seen.add(t)
            deduped.append(t)
    return deduped[:cap]


def extract_pdf_preview(pdf_path: Path, max_pages: int = 2) -> str:
    try:
        doc = fitz.open(pdf_path)
        pages = min(len(doc), max_pages)
        chunks = []
        for idx in range(pages):
            chunks.append(doc[idx].get_text())
        doc.close()
        return "\n".join(chunks)
    except Exception:
        return ""


def verify_pdf_title(pdf_path: Path, title: str) -> Tuple[bool, str]:
    tks = title_tokens(title)
    if not tks:
        return True, "title_tokens:0/0"

    preview = normalize_text(extract_pdf_preview(pdf_path))
    if len(preview) < 50:
        return True, "title_tokens:0/0"

    hits = sum(1 for tk in tks if tk in preview)
    required = max(2, math.ceil(0.35 * len(tks)))
    ok = hits >= required
    return ok, f"title_tokens:{hits}/{len(tks)}"


def build_candidate_urls(row: Dict[str, str]) -> List[str]:
    urls = []
    for i in range(1, 7):
        urls.append(row.get(f"candidate_{i}", ""))
    urls.append(row.get("url", ""))
    urls.append(row.get("doi_url", ""))

    url = (row.get("url") or "").strip()
    doi = (row.get("doi") or "").strip()
    host = (row.get("host") or "").strip().lower()

    if doi:
        urls.append(f"https://doi.org/{doi}")

    # OJS / OCS-style article pages
    if "/article/view/" in url:
        m = re.search(r"/article/view/(\d+)", url)
        if m:
            aid = m.group(1)
            base = url.split("/article/view/")[0]
            urls.append(f"{base}/article/download/{aid}")
            urls.append(f"{base}/article/download/{aid}/0")

    # Springer direct PDF patterns
    if "link.springer.com" in host and doi:
        urls.append(f"https://link.springer.com/content/pdf/{doi}.pdf")
        urls.append(f"https://link.springer.com/content/pdf/{doi}.pdf?download=1")

    # IEEE direct PDF patterns
    if "ieeexplore.ieee.org" in host:
        m_doc = re.search(r"/document/(\d+)", url)
        m_ar = re.search(r"arnumber=(\d+)", url)
        arnumber = (m_doc.group(1) if m_doc else "") or (m_ar.group(1) if m_ar else "")
        if arnumber:
            urls.append(f"https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber={arnumber}")

    # ScienceDirect OA patterns
    if "sciencedirect.com" in host:
        m_pii = re.search(r"/pii/([A-Z0-9]+)", url)
        if m_pii:
            pii = m_pii.group(1)
            urls.append(f"https://www.sciencedirect.com/science/article/pii/{pii}/pdf")
            urls.append(
                f"https://www.sciencedirect.com/science/article/pii/{pii}/pdfft?"
                "isDTMRedir=true&download=true"
            )

    # SSRN patterns
    m_ssrn = re.search(r"10\.2139/ssrn\.(\d+)", doi, re.I)
    if m_ssrn:
        aid = m_ssrn.group(1)
        urls.append(f"https://papers.ssrn.com/sol3/Delivery.cfm/{aid}.pdf")
        urls.append(f"https://papers.ssrn.com/sol3/papers.cfm?abstract_id={aid}")
    m_abs = re.search(r"abstract_id=(\d+)", url)
    if m_abs:
        aid = m_abs.group(1)
        urls.append(f"https://papers.ssrn.com/sol3/Delivery.cfm/{aid}.pdf")

    # arXiv patterns
    if "arxiv.org" in host:
        m_abs = re.search(r"arxiv\.org/(abs|pdf)/([^/?#]+)", url)
        if m_abs:
            arxiv_id = m_abs.group(2).replace(".pdf", "")
            urls.append(f"https://arxiv.org/pdf/{arxiv_id}.pdf")

    # MDPI patterns
    if "mdpi.com" in host and "/pdf" not in url and url:
        urls.append(url.rstrip("/") + "/pdf")
        urls.append(url.rstrip("/") + "/pdf?download=1")

    # TechRxiv direct pattern
    if "techrxiv.org" in host and doi:
        urls.append(f"https://www.techrxiv.org/doi/pdf/{doi}")

    return unique_keep_order(urls)


def curl_download(url: str, out_path: Path) -> Tuple[bool, str, str, int]:
    cmd = [
        "curl",
        "-sS",
        "-L",
        "--compressed",
        "--max-time",
        "30",
        "--connect-timeout",
        "8",
        "-A",
        USER_AGENT,
        "-o",
        str(out_path),
        "-w",
        "%{http_code}|%{content_type}|%{url_effective}",
        url,
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=100)
    except subprocess.TimeoutExpired:
        return False, "timeout", url, 0

    output = (proc.stdout or "").strip()
    parts = output.split("|", 2)
    http = parts[0] if parts else "000"
    effective = parts[2] if len(parts) >= 3 else url

    if http != "200":
        if out_path.exists():
            out_path.unlink()
        return False, f"HTTP {http}", effective, 0

    if not out_path.exists():
        return False, "download_missing", effective, 0

    size = out_path.stat().st_size
    if size < 1200:
        out_path.unlink(missing_ok=True)
        return False, "too_small", effective, size

    with out_path.open("rb") as f:
        if f.read(5) != b"%PDF-":
            out_path.unlink(missing_ok=True)
            return False, "not_pdf_header", effective, size

    return True, "ok", effective, size


def failure_reason_from_attempts(attempts: List[Dict[str, str]]) -> str:
    if not attempts:
        return "no_candidate"
    reasons = [a.get("result", "") for a in attempts if a.get("result") != "ok"]
    if not reasons:
        return "no_pdf_found"
    for pref in FAILURE_PRIORITY:
        for r in reasons:
            if pref in r:
                return pref
    return reasons[0]


def format_attempts_for_csv(attempts: List[Dict[str, str]], cap: int = 3) -> str:
    parts = []
    for a in attempts:
        if a.get("result") == "ok":
            continue
        parts.append(f"{a.get('url','')} [{a.get('result','')}]")
        if len(parts) >= cap:
            break
    return " | ".join(parts)


def extract_to_markdown(pdf_path: Path, extract_path: Path) -> int:
    doc = fitz.open(pdf_path)
    pages = len(doc)
    page_texts = []
    for idx in range(pages):
        page_texts.append(f"--- Page {idx + 1} ---\n\n{doc[idx].get_text()}")
    doc.close()

    extract_path.parent.mkdir(parents=True, exist_ok=True)
    title = extract_path.stem
    now = datetime.now().isoformat()
    content = (
        "---\n"
        f'title: "{title} - PDF Extract"\n'
        f'source_pdf: "{pdf_path.name}"\n'
        f"pages: {pages}\n"
        f'extracted_at: "{now}"\n'
        "---\n\n"
        f"# PDF Extract: {title}\n\n"
        f"**Source PDF:** {pdf_path.name}\n"
        f"**Total Pages:** {pages}\n\n"
        "---\n\n"
        "## Content\n\n"
        "```\n"
        f"{chr(10).join(page_texts)}\n"
        "```\n"
    )
    extract_path.write_text(content, encoding="utf-8")
    return pages


def update_pdf_extract_field(paper_path: Path, extract_rel: str) -> None:
    content = paper_path.read_text(encoding="utf-8")
    if "pdf_extract:" in content and "PDF Extracts/" in content:
        return

    extract_line = f'pdf_extract: "PDF Extracts/{extract_rel}"'

    new_content, n = re.subn(
        r"^pdf_extract:\s*$",
        extract_line,
        content,
        count=1,
        flags=re.MULTILINE,
    )
    if n > 0:
        paper_path.write_text(new_content, encoding="utf-8")
        return

    new_content, n = re.subn(
        r"^pdf_extract:.*$",
        extract_line,
        content,
        count=1,
        flags=re.MULTILINE,
    )
    if n > 0:
        paper_path.write_text(new_content, encoding="utf-8")
        return

    if "local_pdf:" in content:
        content = re.sub(
            r'(local_pdf:\s*"?\[\[[^\]]*\]\]"?\n)',
            r"\1" + extract_line + "\n",
            content,
            count=1,
        )
    elif "external_pdf:" in content:
        content = re.sub(
            r'(external_pdf:\s*"[^"]*"\n)',
            r"\1" + extract_line + "\n",
            content,
            count=1,
        )
    else:
        content = content.replace("DATE_ADDED:", extract_line + "\nDATE_ADDED:")

    paper_path.write_text(content, encoding="utf-8")


def run_priority_batch(
    rows: List[Dict[str, str]],
    priority: str,
    use_waterfall: bool,
    include_blocked: bool,
) -> Tuple[List[Dict[str, str]], List[Dict[str, object]]]:
    pdf_root = load_pdf_root()
    timestamp = now_human()
    results = []

    for row in rows:
        if row.get("priority") != priority:
            continue
        status = row.get("status")
        if status not in {"pending", "blocked"}:
            continue
        if status == "blocked" and not include_blocked:
            continue

        paper_name = row["paper"]
        key = row.get("key", "")
        paper_path = PAPERS_DIR / paper_name
        attempts: List[Dict[str, str]] = []

        if not paper_path.exists():
            row["status"] = "blocked"
            row["status_note"] = "blocked (paper_missing)"
            row["last_attempted"] = timestamp
            row["recent_failed_attempts"] = ""
            row["resolved_source_url"] = ""
            row["resolved_pdf_path"] = ""
            results.append(
                {
                    "paper": paper_name,
                    "key": key,
                    "status": "blocked",
                    "source_url": "",
                    "dest": "",
                    "bytes": 0,
                    "verify": "",
                    "attempts": [],
                }
            )
            continue

        meta = cpf.extract_paper_metadata(paper_path)
        meta["category"] = cpf.classify_paper(meta)
        target_title = row.get("title", "").strip() or meta.get("title", paper_path.stem)
        year = parse_year_from_stem(paper_path.stem, meta.get("year", ""))
        dest_rel = f"{year}/{paper_path.stem}.pdf"
        dest_pdf = pdf_root / dest_rel

        candidate_urls = build_candidate_urls(row)
        attempted_urls = set()
        resolved = False
        source_url = ""
        verify = ""
        size_bytes = 0

        if not candidate_urls:
            attempts.append({"url": "", "result": "no_candidate"})

        for cand in candidate_urls:
            if cand in attempted_urls:
                continue
            attempted_urls.add(cand)

            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                tmp_path = Path(tmp.name)
            ok, dl_reason, effective_url, dl_size = curl_download(cand, tmp_path)
            if not ok:
                attempts.append({"url": cand, "result": dl_reason})
                tmp_path.unlink(missing_ok=True)
                continue

            verified, verify_msg = verify_pdf_title(tmp_path, target_title)
            if not verified:
                attempts.append({"url": cand, "result": f"title_mismatch ({verify_msg})"})
                tmp_path.unlink(missing_ok=True)
                continue

            dest_pdf.parent.mkdir(parents=True, exist_ok=True)
            tmp_path.replace(dest_pdf)
            cpf.safe_update_external_pdf(paper_path, effective_url)
            cpf.safe_update_local_pdf(paper_path, dest_rel)

            attempts.append({"url": cand, "result": "ok", "verify": verify_msg})
            resolved = True
            source_url = effective_url
            verify = verify_msg
            size_bytes = dl_size
            break

        if (not resolved) and use_waterfall and row.get("category") != "RESOURCE_PAGE_NO_PDF":
            wf = cpf.run_waterfall(meta, dry_run=True)
            wf_url = wf.get("pdf_url") if wf.get("found") else ""
            if wf_url and wf_url not in attempted_urls:
                with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                    tmp_path = Path(tmp.name)
                ok, dl_reason, effective_url, dl_size = curl_download(wf_url, tmp_path)
                if ok:
                    verified, verify_msg = verify_pdf_title(tmp_path, target_title)
                    if verified:
                        dest_pdf.parent.mkdir(parents=True, exist_ok=True)
                        tmp_path.replace(dest_pdf)
                        cpf.safe_update_external_pdf(paper_path, effective_url)
                        cpf.safe_update_local_pdf(paper_path, dest_rel)
                        attempts.append(
                            {
                                "url": wf_url,
                                "result": "ok",
                                "verify": verify_msg,
                                "strategy": wf.get("strategy", ""),
                            }
                        )
                        resolved = True
                        source_url = effective_url
                        verify = verify_msg
                        size_bytes = dl_size
                    else:
                        attempts.append({"url": wf_url, "result": f"title_mismatch ({verify_msg})"})
                        tmp_path.unlink(missing_ok=True)
                else:
                    attempts.append({"url": wf_url, "result": dl_reason})
                    tmp_path.unlink(missing_ok=True)

        if resolved:
            row["status"] = "resolved"
            row["status_note"] = f"verified ({verify})"
            row["resolved_source_url"] = source_url
            row["resolved_pdf_path"] = str(dest_pdf.resolve())
            row["last_attempted"] = timestamp
            row["recent_failed_attempts"] = format_attempts_for_csv(attempts)
            results.append(
                {
                    "paper": paper_name,
                    "key": key,
                    "status": "resolved",
                    "source_url": source_url,
                    "dest": str(dest_pdf.resolve()),
                    "bytes": size_bytes,
                    "verify": verify,
                    "attempts": attempts,
                }
            )
        else:
            fail = failure_reason_from_attempts(attempts)
            row["status"] = "blocked"
            row["status_note"] = f"blocked ({fail})"
            row["resolved_source_url"] = ""
            row["resolved_pdf_path"] = ""
            row["last_attempted"] = timestamp
            row["recent_failed_attempts"] = format_attempts_for_csv(attempts)
            results.append(
                {
                    "paper": paper_name,
                    "key": key,
                    "status": "blocked",
                    "source_url": "",
                    "dest": "",
                    "bytes": 0,
                    "verify": "",
                    "attempts": attempts,
                }
            )

    return rows, results


def run_extract_for_results(batch_results: List[Dict[str, object]]) -> Dict[str, object]:
    extracted_results = []
    extracted = 0
    failed = 0

    for item in batch_results:
        if item.get("status") != "resolved":
            continue

        paper_name = str(item["paper"])
        paper_path = PAPERS_DIR / paper_name
        pdf_path = Path(str(item["dest"]))
        if not paper_path.exists() or not pdf_path.exists():
            failed += 1
            extracted_results.append(
                {"paper": paper_name, "status": "failed", "error": "missing_paper_or_pdf"}
            )
            continue

        year = parse_year_from_stem(paper_path.stem)
        extract_rel = f"{year}/{paper_path.stem}.md"
        extract_path = ROOT / "PDF Extracts" / extract_rel
        try:
            pages = extract_to_markdown(pdf_path, extract_path)
            update_pdf_extract_field(paper_path, extract_rel)
            extracted += 1
            extracted_results.append(
                {
                    "paper": paper_name,
                    "status": "extracted",
                    "pages": pages,
                    "extract": f"PDF Extracts/{extract_rel}",
                }
            )
        except Exception as e:  # pragma: no cover - defensive
            failed += 1
            extracted_results.append({"paper": paper_name, "status": "failed", "error": str(e)})

    return {
        "total": len([r for r in batch_results if r.get("status") == "resolved"]),
        "extracted": extracted,
        "failed": failed,
        "results": extracted_results,
    }


def build_queue_summary(rows: List[Dict[str, str]], queue_csv: Path, queue_md: Path, summary_path: Path) -> dict:
    status_counts = Counter(r.get("status", "") for r in rows)
    by_priority = Counter(r.get("priority", "") for r in rows)

    p1_rows = [r for r in rows if r.get("priority") == "P1"]
    p1_counts = Counter(r.get("status", "") for r in p1_rows)

    summary = {
        "timestamp": now_iso(),
        "total": len(rows),
        "by_priority": {
            "P1": by_priority.get("P1", 0),
            "P2": by_priority.get("P2", 0),
            "P3": by_priority.get("P3", 0),
            "P4": by_priority.get("P4", 0),
        },
        "status_counts": {
            "resolved": status_counts.get("resolved", 0),
            "blocked": status_counts.get("blocked", 0),
            "pending": status_counts.get("pending", 0),
        },
        "p1": {
            "resolved": p1_counts.get("resolved", 0),
            "blocked": p1_counts.get("blocked", 0),
            "pending": p1_counts.get("pending", 0),
        },
        "files": {
            "csv": str(queue_csv.resolve()),
            "markdown": str(queue_md.resolve()),
            "summary": str(summary_path.resolve()),
        },
    }
    return summary


def generate_queue_markdown(rows: List[Dict[str, str]], summary: dict) -> str:
    by_priority_category: Dict[str, Dict[str, List[Dict[str, str]]]] = {
        "P1": defaultdict(list),
        "P2": defaultdict(list),
        "P3": defaultdict(list),
        "P4": defaultdict(list),
    }
    for row in rows:
        p = row.get("priority", "")
        if p not in by_priority_category:
            continue
        by_priority_category[p][row.get("category", "UNCATEGORIZED")].append(row)

    out = []
    out.append("# Wave3 Browser Interactive Queue")
    out.append("")
    out.append(f"- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    out.append("- Scope: LSRC0001-LSRC0345")
    out.append(f"- Remaining papers: {summary['status_counts']['pending']}")
    out.append(
        "- Status counts: "
        f"resolved={summary['status_counts']['resolved']}, "
        f"blocked={summary['status_counts']['blocked']}, "
        f"pending={summary['status_counts']['pending']}"
    )
    out.append("")
    out.append("Legend: `[x]` resolved, `[ ]` pending/blocked.")
    out.append("")

    for priority in ["P1", "P2", "P3", "P4"]:
        categories = by_priority_category[priority]
        for category in categories:
            items = categories[category]
            out.append(f"## {priority} · {category} ({len(items)})")
            out.append("")
            for row in items:
                checked = "x" if row.get("status") == "resolved" else " "
                out.append(f"- [{checked}] `{row.get('key','')}` `{row.get('paper','')}`")
                out.append(
                    f"  Status: {row.get('status','')} - {row.get('status_note','').strip()}"
                )
                out.append(f"  Title: {row.get('title','').strip()}")
                out.append(f"  Host: `{row.get('host','').strip()}`")
                out.append(f"  Open: {row.get('url','').strip()}")

                candidates = [row.get(f"candidate_{i}", "").strip() for i in range(1, 7)]
                candidates = [c for c in candidates if c]
                if candidates:
                    out.append("  Direct candidates:")
                    for c in candidates:
                        out.append(f"  - {c}")

                if row.get("doi_url", "").strip():
                    out.append(f"  DOI: {row.get('doi_url','').strip()}")

                out.append(f"  OpenAlex: {row.get('openalex_search','').strip()}")
                out.append(f"  Scholar: {row.get('scholar_search','').strip()}")
                out.append(f"  Tactic: {row.get('manual_tactic','').strip()}")

                if row.get("status") == "resolved":
                    out.append(f"  Resolved source: {row.get('resolved_source_url','').strip()}")
                    out.append(f"  Local PDF: {row.get('resolved_pdf_path','').strip()}")
                if row.get("recent_failed_attempts", "").strip():
                    out.append(
                        f"  Recent failed attempts: {row.get('recent_failed_attempts','').strip()}"
                    )
                out.append("")

    return "\n".join(out).strip() + "\n"


def parse_frontmatter_field(content: str, field: str) -> str:
    m = re.search(rf"^{field}:\s*\"?([^\"\n]*)\"?\s*$", content, re.MULTILINE)
    return m.group(1).strip() if m else ""


def parse_wikilink_path(value: str) -> str:
    m = re.search(r"\[\[([^\]]+)\]\]", value or "")
    return m.group(1).strip() if m else ""


def in_wave3_scope(key: str) -> bool:
    m = re.match(r"LSRC(\d{4})$", key or "")
    if not m:
        return False
    num = int(m.group(1))
    return 1 <= num <= 345


def compute_final_audit() -> dict:
    missing_pdf = []
    missing_extract = []
    missing_abstract = []
    placeholder_authors = []

    strict_missing_pdf = 0
    strict_missing_extract = 0
    strict_missing_abstract = 0
    strict_placeholder_authors = 0

    total = 0

    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        content = paper_path.read_text(encoding="utf-8")
        key = parse_frontmatter_field(content, "key")
        if not in_wave3_scope(key):
            continue
        total += 1

        authors = parse_frontmatter_field(content, "authors")
        abstract = parse_frontmatter_field(content, "abstract")
        local_pdf_field = parse_frontmatter_field(content, "local_pdf")
        extract_field = parse_frontmatter_field(content, "pdf_extract")

        local_pdf_link = parse_wikilink_path(local_pdf_field)
        has_local_pdf = bool(local_pdf_link)
        has_extract = bool(extract_field and "PDF Extracts/" in extract_field)

        if not has_local_pdf:
            missing_pdf.append({"key": key, "paper": paper_path.name})
        if not has_extract:
            missing_extract.append({"key": key, "paper": paper_path.name})
        if not abstract or abstract in {"N/A", "Unknown"}:
            missing_abstract.append({"key": key, "paper": paper_path.name})
        if re.search(r"\bunknown\b", authors, re.IGNORECASE):
            placeholder_authors.append({"key": key, "paper": paper_path.name, "authors": authors})

        # strict diagnostics: field present but target file missing also counts as missing
        pdf_exists = False
        if local_pdf_link:
            pdf_exists = (ROOT / local_pdf_link).exists() or (ROOT.parent / local_pdf_link).exists()
        strict_pdf_missing = (not has_local_pdf) or (not pdf_exists)
        strict_extract_missing = (not has_extract) or not (ROOT / extract_field).exists()
        strict_abstract_missing = not abstract or abstract in {"N/A", "Unknown"}
        strict_author_placeholder = bool(re.search(r"\bunknown\b", authors, re.IGNORECASE))

        strict_missing_pdf += 1 if strict_pdf_missing else 0
        strict_missing_extract += 1 if strict_extract_missing else 0
        strict_missing_abstract += 1 if strict_abstract_missing else 0
        strict_placeholder_authors += 1 if strict_author_placeholder else 0

    return {
        "timestamp": now_iso(),
        "scope": "LSRC0001-LSRC0345",
        "counts": {
            "total_papers": total,
            "baseline": {
                "missing_pdf": len(missing_pdf),
                "missing_extract": len(missing_extract),
                "missing_abstract": len(missing_abstract),
                "placeholder_authors": len(placeholder_authors),
            },
            "strict_diagnostics": {
                "missing_pdf": strict_missing_pdf,
                "missing_extract": strict_missing_extract,
                "missing_abstract": strict_missing_abstract,
                "placeholder_authors": strict_placeholder_authors,
            },
        },
        "residuals": {
            "baseline_missing_pdf": missing_pdf,
            "baseline_missing_extract": missing_extract,
            "missing_abstract": missing_abstract,
            "placeholder_authors": placeholder_authors,
        },
        "completion_status": "manual_browser_pass_executed",
    }


def execute(priority: str, queue_csv: Path, use_waterfall: bool, include_blocked: bool) -> None:
    rows = read_queue_rows(queue_csv)
    rows, batch_results = run_priority_batch(
        rows,
        priority,
        use_waterfall=use_waterfall,
        include_blocked=include_blocked,
    )
    write_queue_rows(queue_csv, rows)

    resolved_count = sum(1 for r in batch_results if r.get("status") == "resolved")
    blocked_count = sum(1 for r in batch_results if r.get("status") == "blocked")

    exec_log = {
        "timestamp": now_iso(),
        "scope": f"{priority} queue execution",
        "total": len(batch_results),
        "resolved": resolved_count,
        "blocked": blocked_count,
        "results": batch_results,
    }
    exec_log_path = LOGS_DIR / f"{DATE_PREFIX}-wave3-{priority.lower()}-execution-results.json"
    exec_log_path.write_text(json.dumps(exec_log, indent=2), encoding="utf-8")

    extract_summary = run_extract_for_results(batch_results)
    post_extract_log = {
        "timestamp": now_iso(),
        "scope": f"{priority} resolved papers",
        **extract_summary,
    }
    post_extract_path = LOGS_DIR / f"{DATE_PREFIX}-wave3-{priority.lower()}-post-extract.json"
    post_extract_path.write_text(json.dumps(post_extract_log, indent=2), encoding="utf-8")

    # Refresh queue markdown and summary
    rows_after = read_queue_rows(queue_csv)
    summary = build_queue_summary(rows_after, queue_csv, QUEUE_MD_DEFAULT, QUEUE_SUMMARY_DEFAULT)
    QUEUE_SUMMARY_DEFAULT.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    QUEUE_MD_DEFAULT.write_text(generate_queue_markdown(rows_after, summary), encoding="utf-8")

    # Refresh final audit snapshot
    audit = compute_final_audit()
    FINAL_AUDIT_DEFAULT.write_text(json.dumps(audit, indent=2), encoding="utf-8")

    print(
        f"{priority}: total={len(batch_results)} resolved={resolved_count} blocked={blocked_count} "
        f"extracted={extract_summary['extracted']} failed_extract={extract_summary['failed']}"
    )
    print(f"Execution log: {exec_log_path}")
    print(f"Post-extract log: {post_extract_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Execute Wave3 interactive queue by priority tier")
    parser.add_argument("priority", choices=["P2", "P3", "P4"], help="Priority tier to execute")
    parser.add_argument(
        "--queue-csv",
        default=str(QUEUE_CSV_DEFAULT),
        help="Path to wave3 queue CSV",
    )
    parser.add_argument(
        "--no-waterfall",
        action="store_true",
        help="Disable comprehensive waterfall fallback after direct candidates fail",
    )
    parser.add_argument(
        "--include-blocked",
        action="store_true",
        help="Reprocess blocked rows for the selected priority",
    )
    args = parser.parse_args()

    queue_csv = Path(args.queue_csv).resolve()
    execute(
        args.priority,
        queue_csv,
        use_waterfall=not args.no_waterfall,
        include_blocked=args.include_blocked,
    )


if __name__ == "__main__":
    main()
