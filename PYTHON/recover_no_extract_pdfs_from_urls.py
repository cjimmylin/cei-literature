#!/usr/bin/env python3
"""
Recover missing PDFs/extracts for unresolved no-extract papers by probing URL fields.

Input:
  - logs/YYYYMMDD-llm-data-fix-unresolved.csv

Behavior:
  - For rows with reason=no_extract_no_candidates, probe URL candidates from:
      * YAML frontmatter: external_pdf, url
      * Any direct PDF-like URL in the paper content
  - Download first confirmed PDF
  - Save PDF under configured PDFS_DIR/<year>/<paper-stem>.pdf
  - Create extract under PDF Extracts/<year>/<paper-stem>.md
  - Update paper YAML fields:
      local_pdf: "[[PDFs/<year>/<paper-stem>.pdf]]"
      pdf_extract: "PDF Extracts/<year>/<paper-stem>.md"

Output:
  - logs/YYYYMMDD-no-extract-recovery-results.csv
  - logs/YYYYMMDD-no-extract-recovery-summary.md
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import subprocess
import tempfile
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import fitz  # PyMuPDF

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent"))
from lib.config import LOGS_DIR, PAPERS_DIR, PDFS_DIR, PDF_EXTRACTS_DIR  # noqa: E402
from lib.yaml_utils import extract_frontmatter, parse_frontmatter, validate_frontmatter  # noqa: E402


def clean_scalar(value: str | None) -> str:
    s = (value or "").strip()
    if len(s) >= 2 and ((s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'"))):
        s = s[1:-1].strip()
    return s


def parse_urls(text: str) -> list[str]:
    urls = re.findall(r"https?://[^\s\"'<>]+", text or "")
    out = []
    seen = set()
    for url in urls:
        u = url.rstrip(".,;:)}]>")
        if "](" in u:
            u = u.split("](", 1)[0]
        if u and u not in seen:
            out.append(u)
            seen.add(u)
    return out


def split_maybe_multi_url(value: str) -> list[str]:
    raw_urls = parse_urls(value)
    if raw_urls:
        return raw_urls
    parts = re.split(r"[;,]\s*|\s+", value.strip())
    return [p for p in parts if p.startswith("http://") or p.startswith("https://")]


def is_direct_pdf_like(url: str) -> bool:
    ul = url.lower()
    return (
        ".pdf" in ul
        or "/pdf/" in ul
        or "download" in ul
        or "blobtype=pdf" in ul
    )


def rank_url(url: str) -> tuple[int, str]:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]

    # Prefer direct PDF-like links and common scientific hosts.
    score = 10
    if is_direct_pdf_like(url):
        score = 0
    if "arxiv.org" in host:
        score -= 2
    if "springer.com" in host or "acm.org" in host or "ieee.org" in host:
        score -= 1
    return (score, url)


def extract_pdf_links_from_html(html: str, base_url: str) -> list[str]:
    links = []
    for href in re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.IGNORECASE):
        h = href.strip()
        if not h:
            continue
        if h.startswith("//"):
            h = "https:" + h
        elif h.startswith("/"):
            h = urljoin(base_url, h)
        elif not (h.startswith("http://") or h.startswith("https://")):
            h = urljoin(base_url, h)
        if is_direct_pdf_like(h):
            links.append(h)
    # Deduplicate preserving order
    out = []
    seen = set()
    for link in links:
        key = link.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(link)
    return out


def host_matches(base_url: str, candidate_url: str) -> bool:
    base = urlparse(base_url).netloc.lower().strip()
    cand = urlparse(candidate_url).netloc.lower().strip()
    if base.startswith("www."):
        base = base[4:]
    if cand.startswith("www."):
        cand = cand[4:]
    if not base or not cand:
        return False
    if base == cand or base.endswith("." + cand) or cand.endswith("." + base):
        return True
    # Allow arXiv PDF redirects from abstract pages.
    if "arxiv.org" in base and "arxiv.org" in cand:
        return True
    return False


def curl_download(url: str, out_path: Path, timeout: int = 15) -> tuple[bool, str]:
    cmd = [
        "curl",
        "-L",
        "--fail",
        "--max-time",
        str(timeout),
        "-A",
        "Mozilla/5.0",
        "-o",
        str(out_path),
        url,
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True, ""
    except subprocess.CalledProcessError as exc:
        stderr = (exc.stderr or "").strip()
        return False, stderr[-500:]


def looks_like_pdf(file_path: Path) -> bool:
    if not file_path.exists() or file_path.stat().st_size < 800:
        return False
    with file_path.open("rb") as f:
        head = f.read(8)
    return head.startswith(b"%PDF")


def write_extract(pdf_path: Path, extract_path: Path) -> int:
    doc = fitz.open(pdf_path)
    num_pages = len(doc)
    page_texts = []
    for page_num in range(num_pages):
        page = doc[page_num]
        text = page.get_text()
        page_texts.append(f"--- Page {page_num + 1} ---\n\n{text}")
    doc.close()

    now = datetime.now().isoformat()
    title = extract_path.stem
    content = f"""---
title: "{title} - PDF Extract"
source_pdf: "{pdf_path.name}"
pages: {num_pages}
extracted_at: "{now}"
---

# PDF Extract: {title}

**Source PDF:** {pdf_path.name}
**Total Pages:** {num_pages}

---

## Content

```
{chr(10).join(page_texts)}
```
"""
    extract_path.parent.mkdir(parents=True, exist_ok=True)
    extract_path.write_text(content, encoding="utf-8")
    return num_pages


def yaml_scalar_line(key: str, value: str) -> str:
    safe = value.replace('"', "'")
    if safe.upper() == "NA":
        return f"{key}: NA"
    return f'{key}: "{safe}"'


def set_yaml_scalar(frontmatter: str, key: str, value: str, anchors: list[str]) -> tuple[str, str]:
    line = yaml_scalar_line(key, value)
    pattern = r"^{}:.*$".format(re.escape(key))
    replaced, count = re.subn(pattern, line, frontmatter, count=1, flags=re.MULTILINE)
    if count > 0:
        return replaced, "replaced"

    for anchor in anchors:
        m = re.search(r"^{}:.*$".format(re.escape(anchor)), frontmatter, flags=re.MULTILINE)
        if m:
            pos = m.end()
            return frontmatter[:pos] + "\n" + line + frontmatter[pos:], f"inserted_after_{anchor}"

    return frontmatter.rstrip() + "\n" + line, "appended"


def main() -> None:
    parser = argparse.ArgumentParser(description="Recover missing PDFs/extracts for unresolved no-extract rows")
    parser.add_argument("--date-prefix", default=date.today().strftime("%Y%m%d"))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-papers", type=int, default=0, help="Optional cap for testing")
    args = parser.parse_args()

    unresolved_csv = LOGS_DIR / f"{args.date_prefix}-llm-data-fix-unresolved.csv"
    if not unresolved_csv.exists():
        raise SystemExit(f"Missing unresolved CSV: {unresolved_csv}")

    rows = list(csv.DictReader(unresolved_csv.open("r", encoding="utf-8")))
    targets = [r for r in rows if r.get("reason") == "no_extract_no_candidates"]
    if args.max_papers > 0:
        targets = targets[:args.max_papers]

    results = []
    counts = Counter()

    for r in targets:
        paper_name = r["paper"]
        paper_path = PAPERS_DIR / paper_name
        result = {
            "paper": paper_name,
            "status": "",
            "selected_url": "",
            "attempted_url_count": 0,
            "pdf_path": "",
            "extract_path": "",
            "pages": "",
            "error": "",
        }

        if not paper_path.exists():
            result["status"] = "missing_paper"
            results.append(result)
            counts["missing_paper"] += 1
            continue

        content = paper_path.read_text(encoding="utf-8", errors="ignore")
        try:
            fm_text, body = extract_frontmatter(content)
        except Exception as exc:
            result["status"] = "frontmatter_error"
            result["error"] = str(exc)
            results.append(result)
            counts["frontmatter_error"] += 1
            continue

        fields = parse_frontmatter(fm_text)
        candidates = []

        for key in ("external_pdf", "url"):
            v = clean_scalar(fields.get(key))
            if not v or v.upper() == "N/A":
                continue
            candidates.extend(split_maybe_multi_url(v))

        # Expand arXiv abs links if present.
        expanded = []
        for u in candidates:
            expanded.append(u)
            if "arxiv.org/abs/" in u:
                expanded.append(u.replace("/abs/", "/pdf/") + ".pdf")
        candidates = expanded

        # Deduplicate and rank.
        deduped = []
        seen = set()
        for u in candidates:
            key = u.lower()
            if key in seen:
                continue
            seen.add(key)
            deduped.append(u)
        deduped = sorted(deduped, key=rank_url)
        result["attempted_url_count"] = len(deduped)

        if not deduped:
            result["status"] = "no_url_candidates"
            results.append(result)
            counts["no_url_candidates"] += 1
            continue

        year_match = re.match(r"^(\d{4})-", paper_path.stem)
        year = year_match.group(1) if year_match else "0000"
        pdf_dest_dir = PDFS_DIR / year
        pdf_dest_dir.mkdir(parents=True, exist_ok=True)
        pdf_dest = pdf_dest_dir / f"{paper_path.stem}.pdf"
        extract_dest = PDF_EXTRACTS_DIR / year / f"{paper_path.stem}.md"

        selected_url = ""
        tmp_pdf = None
        last_err = ""

        for candidate in deduped:
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tf:
                tmp_path = Path(tf.name)
            ok, err = curl_download(candidate, tmp_path)
            if not ok:
                tmp_path.unlink(missing_ok=True)
                last_err = err or "curl_failed"
                continue

            if looks_like_pdf(tmp_path):
                tmp_pdf = tmp_path
                selected_url = candidate
                break

            # Try extracting PDF links from HTML and retry quickly.
            try:
                html = tmp_path.read_text(encoding="utf-8", errors="ignore")
                pdf_links = extract_pdf_links_from_html(html, candidate)
            except Exception:
                pdf_links = []
            pdf_links = [link for link in pdf_links if host_matches(candidate, link)]
            tmp_path.unlink(missing_ok=True)
            for link in pdf_links[:6]:
                with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tf2:
                    tmp2 = Path(tf2.name)
                ok2, err2 = curl_download(link, tmp2)
                if not ok2:
                    tmp2.unlink(missing_ok=True)
                    last_err = err2 or "curl_failed_html_link"
                    continue
                if looks_like_pdf(tmp2):
                    tmp_pdf = tmp2
                    selected_url = link
                    break
                tmp2.unlink(missing_ok=True)
            if tmp_pdf is not None:
                break

        if tmp_pdf is None:
            result["status"] = "download_failed"
            result["error"] = last_err[:500]
            results.append(result)
            counts["download_failed"] += 1
            continue

        if not args.dry_run:
            shutil.move(str(tmp_pdf), str(pdf_dest))
            pages = write_extract(pdf_dest, extract_dest)

            # Update frontmatter fields.
            new_fm, _ = set_yaml_scalar(
                fm_text,
                "local_pdf",
                f"[[PDFs/{year}/{paper_path.stem}.pdf]]",
                anchors=["external_pdf", "url", "pdf_extract"],
            )
            new_fm, _ = set_yaml_scalar(
                new_fm,
                "pdf_extract",
                f"PDF Extracts/{year}/{paper_path.stem}.md",
                anchors=["local_pdf", "external_pdf", "url"],
            )

            valid, issues = validate_frontmatter(new_fm)
            if not valid:
                result["status"] = "yaml_validation_failed"
                result["error"] = "; ".join(issues)
                results.append(result)
                counts["yaml_validation_failed"] += 1
                continue

            new_content = f"---\n{new_fm.rstrip()}\n---\n{body}"
            paper_path.write_text(new_content, encoding="utf-8")
        else:
            pages = ""
            tmp_pdf.unlink(missing_ok=True)

        result["status"] = "recovered" if not args.dry_run else "would_recover"
        result["selected_url"] = selected_url
        result["pdf_path"] = str(pdf_dest)
        result["extract_path"] = str(extract_dest)
        result["pages"] = pages
        results.append(result)
        counts[result["status"]] += 1

    out_csv = LOGS_DIR / f"{args.date_prefix}-no-extract-recovery-results.csv"
    out_md = LOGS_DIR / f"{args.date_prefix}-no-extract-recovery-summary.md"

    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "paper",
                "status",
                "selected_url",
                "attempted_url_count",
                "pdf_path",
                "extract_path",
                "pages",
                "error",
            ],
        )
        w.writeheader()
        for row in results:
            w.writerow(row)

    lines = [
        "# No-Extract Recovery Summary",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Mode: {'dry-run' if args.dry_run else 'write'}",
        f"Target unresolved rows: {len(targets)}",
        "",
        "## Status Counts",
        "",
    ]
    for k, v in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"- {k}: {v}")
    lines.extend(
        [
            "",
            "## Artifacts",
            "",
            f"- `{out_csv}`",
            f"- `{out_md}`",
            "",
        ]
    )
    out_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"targets={len(targets)}")
    print(f"status_counts={dict(counts)}")
    print(f"results_csv={out_csv}")
    print(f"summary_md={out_md}")


if __name__ == "__main__":
    main()
