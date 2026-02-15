#!/usr/bin/env python3
"""
Apply direct PDF candidates with strict verification.

Workflow:
1. Read candidate rows from logs/20260214-alt-method-direct-pdf-candidates.csv
2. Download each candidate PDF
3. Verify match against paper title/DOI using PDF metadata + first-page text
4. On verified match: place into PDFs/<year>/ and update paper frontmatter
5. On failed/uncertain match: move file to recycle for manual review

This script is intentionally conservative: it will skip rather than force-link.
"""

from __future__ import annotations

import argparse
import csv
import functools
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import fitz

# Add PYTHON dir to path for yaml_frontmatter_utils import
_script_dir = Path(__file__).resolve().parent
if str(_script_dir) not in sys.path:
    sys.path.insert(0, str(_script_dir))

from yaml_frontmatter_utils import extract_frontmatter, parse_frontmatter, validate_frontmatter  # noqa: E402

print = functools.partial(print, flush=True)

WORKSPACE = Path(__file__).resolve().parents[1]
LOGS_DIR = WORKSPACE / "logs"
PAPERS_DIR = WORKSPACE / "papers"
RECYCLE_DIR = WORKSPACE / "RECYCLE-BIN" / "20260214-alt-method-rejected-verify"
VAULT_CONFIG = WORKSPACE / ".vault-config.json"

UA = (
    "CEI-Lit-WS/apply-alt-method-direct/1.0 "
    "(Academic Research; mailto:research@cei-literature.org)"
)

STOPWORDS = {
    "the",
    "a",
    "an",
    "and",
    "or",
    "of",
    "for",
    "to",
    "in",
    "on",
    "with",
    "from",
    "by",
    "using",
    "based",
    "towards",
    "toward",
    "new",
    "study",
    "analysis",
    "dataset",
    "datasets",
    "language",
    "model",
    "models",
}

TRUSTED_HIGH_HOSTS = {
    "pmc.ncbi.nlm.nih.gov",
    "aclanthology.org",
    "arxiv.org",
    "www.cambridge.org",
    "www.sciengine.com",
    "www.scirp.org",
}


@dataclass
class PaperMeta:
    paper: str
    path: Path
    title: str
    short_title: str
    year: str
    doi: str
    url: str
    external_pdf: str
    local_pdf: str


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
    # Faster/portable similarity without external libs.
    na = normalize_title(a)
    nb = normalize_title(b)
    if not na or not nb:
        return 0.0
    sa = set(na.split())
    sb = set(nb.split())
    if not sa or not sb:
        return 0.0
    overlap = len(sa & sb) / max(1, min(len(sa), len(sb)))
    # Blend token overlap with prefix containment.
    contains_bonus = 0.2 if (na in nb or nb in na) else 0.0
    return min(1.0, overlap * 0.8 + contains_bonus)


def key_term_hit_ratio(title: str, text: str) -> float:
    tt = [w for w in normalize_title(title).split() if len(w) >= 4 and w not in STOPWORDS]
    if len(tt) < 4:
        return 0.0
    body = normalize_title(text)
    hits = sum(1 for t in set(tt) if t in body)
    return hits / max(1, len(set(tt)))


def get_pdfs_dir() -> Path:
    cfg = read_json(VAULT_CONFIG)
    return Path(cfg["pdf_path"]).resolve()


def _strip_quotes(s: str) -> str:
    """Strip surrounding single or double quotes from a value."""
    s = s.strip()
    if len(s) >= 2 and ((s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'"))):
        return s[1:-1].strip()
    return s


def parse_paper_meta(paper_file: str) -> Optional[PaperMeta]:
    p = PAPERS_DIR / paper_file
    if not p.exists():
        return None
    txt = p.read_text(encoding="utf-8", errors="ignore")
    try:
        fm_text, _body = extract_frontmatter(txt)
        fields = parse_frontmatter(fm_text)
    except ValueError:
        return None
    short_title = _strip_quotes(fields.get("short_title", ""))
    title = short_title or _strip_quotes(fields.get("title", "")) or p.stem
    year = _strip_quotes(fields.get("year", ""))
    doi = _strip_quotes(fields.get("doi", ""))
    url = _strip_quotes(fields.get("url", ""))
    external_pdf = _strip_quotes(fields.get("external_pdf", ""))
    local_pdf = _strip_quotes(fields.get("local_pdf", ""))
    if doi:
        doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
        doi = doi.replace("doi:", "").strip().rstrip(".")
    return PaperMeta(
        paper=paper_file,
        path=p,
        title=normalize_space(title),
        short_title=normalize_space(short_title),
        year=year,
        doi=doi,
        url=url,
        external_pdf=external_pdf,
        local_pdf=local_pdf,
    )


def canonicalize_url(url: str) -> str:
    url = (url or "").strip().replace("&amp;", "&")
    if not url:
        return ""
    return url


def host_of(url: str) -> str:
    from urllib.parse import urlsplit

    try:
        return urlsplit(url).netloc.lower()
    except Exception:
        return ""


def download_pdf(url: str, out_path: Path, timeout_sec: int = 120) -> Tuple[bool, dict]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "curl",
        "-sS",
        "-L",
        "--max-time",
        str(timeout_sec),
        "--connect-timeout",
        "20",
        "-H",
        f"User-Agent: {UA}",
        "-H",
        "Accept: application/pdf,text/html;q=0.9,*/*;q=0.8",
        "-o",
        str(out_path),
        "-w",
        "%{http_code}\t%{url_effective}\t%{content_type}\t%{size_download}",
        url,
    ]
    try:
        cp = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_sec + 10)
    except Exception as e:
        return False, {"error": f"curl_exception: {e}"}

    meta = {"curl_stderr": cp.stderr.strip()}
    if cp.returncode != 0:
        meta["error"] = f"curl_return_{cp.returncode}"
        return False, meta

    parts = cp.stdout.strip().split("\t")
    if len(parts) >= 4:
        meta["http_code"] = parts[0]
        meta["final_url"] = parts[1]
        meta["content_type"] = parts[2]
        meta["size_download"] = parts[3]
    else:
        meta["error"] = "curl_parse_error"
        return False, meta

    if meta["http_code"] != "200":
        meta["error"] = f"http_{meta['http_code']}"
        return False, meta
    if not out_path.exists() or out_path.stat().st_size < 1024:
        meta["error"] = "file_missing_or_too_small"
        return False, meta
    with out_path.open("rb") as f:
        header = f.read(5)
    if header != b"%PDF-":
        meta["error"] = "not_pdf_header"
        return False, meta
    return True, meta


def extract_pdf_signals(pdf_path: Path) -> dict:
    info = {
        "meta_title": "",
        "first_page_text": "",
        "page_count": 0,
        "extract_error": "",
    }
    try:
        doc = fitz.open(pdf_path)
        info["page_count"] = doc.page_count
        md = doc.metadata or {}
        info["meta_title"] = normalize_space(md.get("title", "") or "")
        if doc.page_count > 0:
            t = doc[0].get_text("text") or ""
            info["first_page_text"] = normalize_space(t[:5000])
        doc.close()
    except Exception as e:
        info["extract_error"] = str(e)
    return info


def compute_verification(
    paper: PaperMeta,
    row: dict,
    final_url: str,
    pdf_signals: dict,
) -> dict:
    paper_title = paper.title
    source_title = row.get("source_title", "")
    conf = int(row.get("confidence") or 0)
    cand_host = host_of(row.get("candidate_url", ""))
    final_host = host_of(final_url)

    meta_title = pdf_signals.get("meta_title", "")
    first_text = pdf_signals.get("first_page_text", "")

    sim_source = title_similarity(paper_title, source_title)
    sim_meta = title_similarity(paper_title, meta_title)
    ratio_terms = key_term_hit_ratio(paper_title, first_text)
    sim_first = title_similarity(paper_title, first_text[:800])

    doi = (paper.doi or "").lower()
    doi_in_url = bool(doi and doi in (final_url or "").lower())
    doi_in_text = bool(doi and doi in (first_text or "").lower())

    first_contains = ratio_terms >= 0.55 or sim_first >= 0.70
    meta_match = sim_meta >= 0.82
    source_strong = sim_source >= 0.90

    evidence: List[str] = []
    if meta_match:
        evidence.append(f"meta_title_sim={sim_meta:.2f}")
    if first_contains:
        evidence.append(f"first_page_match(term_ratio={ratio_terms:.2f},sim={sim_first:.2f})")
    if doi_in_url:
        evidence.append("doi_in_final_url")
    if doi_in_text:
        evidence.append("doi_in_first_page_text")
    if source_strong:
        evidence.append(f"source_title_sim={sim_source:.2f}")

    trusted = (final_host in TRUSTED_HIGH_HOSTS) or (cand_host in TRUSTED_HIGH_HOSTS)

    # Strict gate: require hard evidence extracted from the retrieved file/URL.
    # Source-title agreement alone is not sufficient for auto-linking.
    verified = bool(meta_match or first_contains or doi_in_url or doi_in_text)

    reason = "verified" if verified else "verification_failed"
    return {
        "verified": verified,
        "reason": reason,
        "evidence": "; ".join(evidence),
        "sim_source": round(sim_source, 3),
        "sim_meta": round(sim_meta, 3),
        "term_ratio": round(ratio_terms, 3),
        "sim_first": round(sim_first, 3),
        "doi_in_url": doi_in_url,
        "doi_in_text": doi_in_text,
        "trusted_host": trusted,
        "final_host": final_host,
        "candidate_host": cand_host,
    }


def compute_year(paper: PaperMeta) -> str:
    m = re.match(r"^(\d{4})-", paper.paper)
    if m:
        return m.group(1)
    y = (paper.year or "").strip()
    if re.fullmatch(r"\d{4}", y):
        return y
    return "0000"


def safe_update_external_pdf(paper_path: Path, pdf_url: str) -> bool:
    text = paper_path.read_text(encoding="utf-8")
    new_line = f'external_pdf: "{pdf_url.replace(chr(34), chr(39))}"'
    if re.search(r"^external_pdf:.*$", text, flags=re.MULTILINE):
        text = re.sub(r"^external_pdf:.*$", new_line, text, count=1, flags=re.MULTILINE)
    elif re.search(r"^url:.*$", text, flags=re.MULTILINE):
        text = re.sub(r"(^url:.*$\n)", r"\1" + new_line + "\n", text, count=1, flags=re.MULTILINE)
    else:
        text = text.replace("DATE_ADDED:", new_line + "\nDATE_ADDED:", 1)
    # Validate frontmatter before writing
    try:
        fm_text, _body = extract_frontmatter(text)
        is_valid, issues = validate_frontmatter(fm_text)
        if not is_valid:
            print(f"  WARN: validate_frontmatter failed for {paper_path.name}: {issues}")
            return False
    except ValueError as exc:
        print(f"  WARN: frontmatter extraction failed for {paper_path.name}: {exc}")
        return False
    paper_path.write_text(text, encoding="utf-8")
    return True


def safe_update_local_pdf(paper_path: Path, rel_pdf_path: str) -> bool:
    text = paper_path.read_text(encoding="utf-8")
    # Obsidian wikilinks cannot safely represent paths containing "[[" or "]]".
    if "[[" in rel_pdf_path or "]]" in rel_pdf_path:
        new_line = f'local_pdf: "{rel_pdf_path}"'
    else:
        new_line = f'local_pdf: "[[{rel_pdf_path}]]"'
    if re.search(r"^local_pdf:.*$", text, flags=re.MULTILINE):
        text = re.sub(r"^local_pdf:.*$", new_line, text, count=1, flags=re.MULTILINE)
    elif re.search(r"^external_pdf:.*$", text, flags=re.MULTILINE):
        text = re.sub(
            r"(^external_pdf:.*$\n)",
            r"\1" + new_line + "\n",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    elif re.search(r"^url:.*$", text, flags=re.MULTILINE):
        text = re.sub(r"(^url:.*$\n)", r"\1" + new_line + "\n", text, count=1, flags=re.MULTILINE)
    else:
        text = text.replace("DATE_ADDED:", new_line + "\nDATE_ADDED:", 1)
    # Validate frontmatter before writing
    try:
        fm_text, _body = extract_frontmatter(text)
        is_valid, issues = validate_frontmatter(fm_text)
        if not is_valid:
            print(f"  WARN: validate_frontmatter failed for {paper_path.name}: {issues}")
            return False
    except ValueError as exc:
        print(f"  WARN: frontmatter extraction failed for {paper_path.name}: {exc}")
        return False
    paper_path.write_text(text, encoding="utf-8")
    return True


def file_has_valid_local_pdf(paper: PaperMeta, pdfs_dir: Path) -> bool:
    val = (paper.local_pdf or "").strip().strip('"')
    m = re.search(r"\[\[(.*?)\]\]", val)
    if not m:
        return False
    rel = m.group(1).split("|")[0].strip()
    path = (WORKSPACE.parent / rel).resolve() if rel.startswith("PDFs/") else (pdfs_dir / rel).resolve()
    return path.exists() and path.stat().st_size > 1024


def main() -> None:
    ap = argparse.ArgumentParser(description="Apply verified direct PDF candidates.")
    ap.add_argument(
        "--input-csv",
        type=Path,
        default=LOGS_DIR / "20260214-alt-method-direct-pdf-candidates.csv",
        help="Direct candidate CSV path.",
    )
    ap.add_argument("--limit", type=int, default=0, help="Process only first N rows.")
    ap.add_argument("--dry-run", action="store_true", help="Run verification without writing files.")
    args = ap.parse_args()

    input_csv = args.input_csv
    if not input_csv.exists():
        raise SystemExit(f"Input CSV not found: {input_csv}")

    pdfs_dir = get_pdfs_dir()
    RECYCLE_DIR.mkdir(parents=True, exist_ok=True)

    rows = list(csv.DictReader(input_csv.open(encoding="utf-8")))
    if args.limit and args.limit > 0:
        rows = rows[: args.limit]

    print(f"Rows to process: {len(rows)}")
    print(f"PDF root: {pdfs_dir}")
    if args.dry_run:
        print("*** DRY RUN: no writes ***")

    results: List[dict] = []
    counters = Counter()

    for i, row in enumerate(rows, start=1):
        paper_file = row.get("paper", "")
        candidate_url = canonicalize_url(row.get("candidate_url", ""))
        print(f"[{i:03d}/{len(rows):03d}] {paper_file}")

        if not paper_file or not candidate_url:
            counters["invalid_row"] += 1
            results.append({"paper": paper_file, "status": "invalid_row"})
            continue

        meta = parse_paper_meta(paper_file)
        if not meta:
            counters["missing_paper"] += 1
            results.append({"paper": paper_file, "status": "missing_paper"})
            continue

        if file_has_valid_local_pdf(meta, pdfs_dir):
            counters["already_has_pdf"] += 1
            results.append({"paper": paper_file, "status": "already_has_pdf"})
            continue

        year = compute_year(meta)
        pdf_name = f"{meta.path.stem}.pdf"
        rel_pdf = f"PDFs/{year}/{pdf_name}"
        dest_pdf = pdfs_dir / year / pdf_name

        with tempfile.NamedTemporaryFile(prefix="altcand_", suffix=".pdf", delete=False) as tf:
            temp_path = Path(tf.name)

        ok, dl_meta = download_pdf(candidate_url, temp_path)
        if not ok:
            counters["download_failed"] += 1
            try:
                if temp_path.exists():
                    temp_path.unlink()
            except Exception:
                pass
            results.append(
                {
                    "paper": paper_file,
                    "status": "download_failed",
                    "candidate_url": candidate_url,
                    "error": dl_meta.get("error", ""),
                    "http_code": dl_meta.get("http_code", ""),
                }
            )
            continue

        pdf_signals = extract_pdf_signals(temp_path)
        ver = compute_verification(
            paper=meta,
            row=row,
            final_url=dl_meta.get("final_url", "") or candidate_url,
            pdf_signals=pdf_signals,
        )

        if not ver["verified"]:
            counters["rejected_verification"] += 1
            recycle_name = f"{meta.path.stem}__rejected.pdf"
            recycle_path = RECYCLE_DIR / recycle_name
            if recycle_path.exists():
                recycle_path = RECYCLE_DIR / f"{meta.path.stem}__rejected_{int(datetime.now().timestamp())}.pdf"
            if args.dry_run:
                temp_path.unlink(missing_ok=True)
            else:
                shutil.move(str(temp_path), str(recycle_path))
            results.append(
                {
                    "paper": paper_file,
                    "status": "rejected_verification",
                    "candidate_url": candidate_url,
                    "final_url": dl_meta.get("final_url", ""),
                    "evidence": ver["evidence"],
                    "sim_source": ver["sim_source"],
                    "sim_meta": ver["sim_meta"],
                    "term_ratio": ver["term_ratio"],
                    "sim_first": ver["sim_first"],
                    "recycle_pdf": str(recycle_path),
                }
            )
            continue

        # Verified and accepted.
        if args.dry_run:
            temp_path.unlink(missing_ok=True)
            counters["accepted_dry_run"] += 1
            results.append(
                {
                    "paper": paper_file,
                    "status": "accepted_dry_run",
                    "candidate_url": candidate_url,
                    "final_url": dl_meta.get("final_url", ""),
                    "evidence": ver["evidence"],
                    "dest_pdf": str(dest_pdf),
                    "rel_pdf": rel_pdf,
                }
            )
            continue

        dest_pdf.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(temp_path), str(dest_pdf))
        safe_update_external_pdf(meta.path, dl_meta.get("final_url", "") or candidate_url)
        safe_update_local_pdf(meta.path, rel_pdf)
        counters["accepted"] += 1
        results.append(
            {
                "paper": paper_file,
                "status": "accepted",
                "candidate_url": candidate_url,
                "final_url": dl_meta.get("final_url", ""),
                "evidence": ver["evidence"],
                "dest_pdf": str(dest_pdf),
                "rel_pdf": rel_pdf,
                "size_bytes": dest_pdf.stat().st_size if dest_pdf.exists() else 0,
            }
        )

    ts = datetime.now().strftime("%Y%m%d")
    out_json = LOGS_DIR / f"{ts}-alt-method-direct-apply-log.json"
    out_csv = LOGS_DIR / f"{ts}-alt-method-direct-apply-results.csv"
    summary_json = LOGS_DIR / f"{ts}-alt-method-direct-apply-summary.json"

    out_json.write_text(
        json.dumps(
            {
                "generated_at": now_iso(),
                "input_csv": str(input_csv),
                "dry_run": bool(args.dry_run),
                "counters": dict(counters),
                "results": results,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    csv_fields = sorted({k for r in results for k in r.keys()}) if results else ["paper", "status"]
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=csv_fields, extrasaction="ignore")
        w.writeheader()
        for r in results:
            w.writerow(r)

    summary = {
        "generated_at": now_iso(),
        "input_csv": str(input_csv),
        "dry_run": bool(args.dry_run),
        "total_rows": len(rows),
        "counters": dict(counters),
        "outputs": {
            "log_json": str(out_json),
            "results_csv": str(out_csv),
            "summary_json": str(summary_json),
            "recycle_dir": str(RECYCLE_DIR),
        },
    }
    summary_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\nApply summary")
    print(f"- total rows: {len(rows)}")
    for k in sorted(counters):
        print(f"- {k}: {counters[k]}")
    print(f"- wrote: {out_json}")
    print(f"- wrote: {out_csv}")
    print(f"- wrote: {summary_json}")


if __name__ == "__main__":
    main()
