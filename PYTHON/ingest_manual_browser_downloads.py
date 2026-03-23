#!/usr/bin/env python3
"""
Ingest manually downloaded PDFs for queue papers and sync paper metadata.

This script checks queue papers for expected local PDF paths:
  Lit-WS-PDFs/<year>/<paper_stem>.pdf

If the PDF exists and is valid, it will:
1) Ensure `local_pdf` points to the expected PDF.
2) Ensure `pdf_extract` points to an extract file.
3) Create/update the extract file if missing.

By default this script does not touch `external_pdf`.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

import fitz  # PyMuPDF


ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "papers"
LOGS_DIR = ROOT / "logs"
DEFAULT_QUEUE = (
    LOGS_DIR / "20260214-browser-fetch-manual-plan-after-wave3-plus-europepmc-plus-wave4-remapped.csv"
)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_pdf_root() -> Path:
    cfg = json.loads((ROOT / ".vault-config.json").read_text(encoding="utf-8"))
    return ROOT.parent / cfg["pdf_path"]


def parse_year(stem: str) -> str:
    m = re.match(r"^(\d{4})-", stem)
    return m.group(1) if m else "0000"


def extract_field(text: str, name: str) -> str:
    m = re.search(rf"^{re.escape(name)}:\s*(.*)$", text, flags=re.MULTILINE)
    if not m:
        return ""
    return m.group(1).strip().strip('"').strip("'")


def is_missing_value(v: str) -> bool:
    s = (v or "").strip().strip('"').strip("'").upper()
    return s in {"", "NA", "N/A", "NULL", "NONE"}


def set_or_insert_field(text: str, field: str, value_line: str) -> str:
    pattern = rf"^{re.escape(field)}:.*$"
    if re.search(pattern, text, flags=re.MULTILINE):
        return re.sub(pattern, value_line, text, count=1, flags=re.MULTILINE)

    if re.search(r"^local_pdf:.*$", text, flags=re.MULTILINE):
        return re.sub(
            r"(^local_pdf:.*$\n)",
            r"\1" + value_line + "\n",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    if re.search(r"^external_pdf:.*$", text, flags=re.MULTILINE):
        return re.sub(
            r"(^external_pdf:.*$\n)",
            r"\1" + value_line + "\n",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    if re.search(r"^url:.*$", text, flags=re.MULTILINE):
        return re.sub(
            r"(^url:.*$\n)",
            r"\1" + value_line + "\n",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    return text.replace("DATE_ADDED:", value_line + "\nDATE_ADDED:", 1)


def build_local_pdf_line(rel_pdf: str) -> str:
    if "[[" in rel_pdf or "]]" in rel_pdf:
        return f'local_pdf: "{rel_pdf}"'
    return f'local_pdf: "[[{rel_pdf}]]"'


def extract_to_markdown(pdf_path: Path, extract_path: Path) -> int:
    doc = fitz.open(pdf_path)
    pages = len(doc)
    chunks = []
    for i in range(pages):
        chunks.append(f"--- Page {i + 1} ---\n\n{doc[i].get_text()}")
    doc.close()

    extract_path.parent.mkdir(parents=True, exist_ok=True)
    title = extract_path.stem
    content = (
        "---\n"
        f'title: "{title} - PDF Extract"\n'
        f'source_pdf: "{pdf_path.name}"\n'
        f"pages: {pages}\n"
        f'extracted_at: "{datetime.now().isoformat()}"\n'
        "---\n\n"
        f"# PDF Extract: {title}\n\n"
        f"**Source PDF:** {pdf_path.name}\n"
        f"**Total Pages:** {pages}\n\n"
        "---\n\n"
        "## Content\n\n"
        "```\n"
        + "\n".join(chunks)
        + "\n```\n"
    )
    extract_path.write_text(content, encoding="utf-8")
    return pages


def valid_pdf(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 1200:
        return False
    try:
        with path.open("rb") as f:
            return f.read(5) == b"%PDF-"
    except Exception:
        return False


def unique_papers_from_queue(queue_csv: Path) -> List[str]:
    rows = list(csv.DictReader(queue_csv.open(encoding="utf-8")))
    seen = set()
    papers = []
    for r in rows:
        p = (r.get("paper") or "").strip()
        if p and p not in seen:
            seen.add(p)
            papers.append(p)
    return papers


def run(queue_csv: Path, apply: bool) -> Dict[str, object]:
    pdf_root = load_pdf_root()
    papers = unique_papers_from_queue(queue_csv)

    counters = Counter()
    records: List[Dict[str, object]] = []

    for paper_name in papers:
        paper_path = PAPERS_DIR / paper_name
        rec: Dict[str, object] = {"paper": paper_name}

        if not paper_path.exists():
            counters["missing_paper"] += 1
            rec["status"] = "missing_paper"
            records.append(rec)
            continue

        stem = paper_path.stem
        year = parse_year(stem)
        rel_pdf = f"Lit-WS-PDFs/{year}/{stem}.pdf"
        abs_pdf = pdf_root / year / f"{stem}.pdf"
        rel_extract = f"PDF Extracts/{year}/{stem}.md"
        abs_extract = ROOT / rel_extract

        rec["expected_pdf"] = str(abs_pdf)
        rec["expected_extract"] = str(abs_extract)

        if not valid_pdf(abs_pdf):
            counters["pdf_missing_or_invalid"] += 1
            rec["status"] = "pdf_missing_or_invalid"
            records.append(rec)
            continue

        counters["pdf_present_valid"] += 1

        text = paper_path.read_text(encoding="utf-8")
        old_local = extract_field(text, "local_pdf")
        old_extract = extract_field(text, "pdf_extract")

        local_line = build_local_pdf_line(rel_pdf)
        new_text = set_or_insert_field(text, "local_pdf", local_line)
        new_text = set_or_insert_field(new_text, "pdf_extract", f'pdf_extract: "{rel_extract}"')

        changed_fields = new_text != text

        extract_created = False
        extract_touched = False
        pages = 0
        if not abs_extract.exists():
            extract_created = True
            extract_touched = True
            pages = extract_to_markdown(abs_pdf, abs_extract) if apply else 0
        elif apply:
            # keep extract in sync with local file if it exists but appears malformed
            try:
                hdr = abs_extract.read_text(encoding="utf-8", errors="ignore")[:80]
                if "---" not in hdr:
                    extract_touched = True
                    pages = extract_to_markdown(abs_pdf, abs_extract)
            except Exception:
                extract_touched = True
                pages = extract_to_markdown(abs_pdf, abs_extract)

        if apply and changed_fields:
            paper_path.write_text(new_text, encoding="utf-8")
            counters["papers_updated"] += 1
        elif changed_fields:
            counters["papers_would_update"] += 1

        if extract_created:
            counters["extract_created"] += 1
        if extract_touched and not extract_created:
            counters["extract_rebuilt"] += 1

        rec.update(
            {
                "status": "synced" if (changed_fields or extract_touched) else "already_synced",
                "old_local_pdf": old_local,
                "old_pdf_extract": old_extract,
                "new_local_pdf": rel_pdf,
                "new_pdf_extract": rel_extract,
                "field_changed": changed_fields,
                "extract_created": extract_created,
                "extract_rebuilt": (extract_touched and not extract_created),
                "pages": pages,
            }
        )
        records.append(rec)

    return {
        "generated_at": now_iso(),
        "queue_csv": str(queue_csv),
        "apply": apply,
        "counters": dict(counters),
        "records": records,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Ingest manual browser downloads into paper metadata.")
    ap.add_argument("--queue-csv", type=Path, default=DEFAULT_QUEUE)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    queue_csv = args.queue_csv.resolve()
    result = run(queue_csv=queue_csv, apply=not args.dry_run)

    stamp = datetime.now().strftime("%Y%m%d")
    mode = "dryrun" if args.dry_run else "apply"
    out_json = LOGS_DIR / f"{stamp}-manual-browser-ingest-{mode}.json"
    out_json.write_text(json.dumps(result, indent=2), encoding="utf-8")

    print(f"Queue: {queue_csv}")
    print(f"Mode: {mode}")
    print("Counters:")
    for k, v in sorted(result["counters"].items()):
        print(f"- {k}: {v}")
    print(f"Report: {out_json}")


if __name__ == "__main__":
    main()

