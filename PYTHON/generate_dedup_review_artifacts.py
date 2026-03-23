#!/usr/bin/env python3
"""
Generate dedup review artifacts from exact and fuzzy duplicate detection.

This script does not mutate papers. It creates review artifacts:
  - logs/YYYYMMDD-duplicate_groups_review.csv
  - logs/YYYYMMDD-duplicate_candidates_fuzzy.csv
  - logs/YYYYMMDD-duplicate_candidates_fuzzy.json
  - logs/YYYYMMDD-dedup_manual_review.csv
  - logs/YYYYMMDD-duplicate_groups_fuzzy_approved.json
  - logs/YYYYMMDD-dedup_review_summary.json

Workflow:
1) Load exact duplicate groups from detect_duplicates.py output.
2) Build an exact-group review CSV with safety flags.
3) Exhaustively scan all paper pairs for fuzzy title/author/year similarity.
4) Build/update manual review queue (preserving prior decisions by pair_key).
5) Emit approved fuzzy groups JSON (for consolidate_duplicates.py input).
"""

from __future__ import annotations

import argparse
import csv
import functools
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import Dict, List, Optional, Tuple

print = functools.partial(print, flush=True)

SCRIPT_DIR = Path(__file__).parent.resolve()
WORKSPACE_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(WORKSPACE_ROOT / ".agent"))

from vault_config import LOGS_DIR, PAPERS_DIR, PDFS_DIR, PDF_EXTRACTS_DIR  # noqa: E402
from lib.yaml_utils import extract_frontmatter, parse_frontmatter  # noqa: E402


ARXIV_ID_RE = re.compile(r"(\d{4}\.\d{4,5})(v\d+)?")
YEAR_RE = re.compile(r"^\d{4}$")
NON_WORD_RE = re.compile(r"[^a-z0-9\s]")
SPACE_RE = re.compile(r"\s+")


@dataclass
class PaperRecord:
    filename: str
    key: str
    title: str
    norm_title: str
    first_author: str
    norm_first_author: str
    year: str
    doi: str
    arxiv_id: str
    url: str
    external_pdf: str
    richness: int
    has_pdf_on_disk: bool
    has_extract_on_disk: bool


def normalize_text(value: str) -> str:
    x = (value or "").lower().strip()
    x = NON_WORD_RE.sub(" ", x)
    x = SPACE_RE.sub(" ", x).strip()
    return x


def normalize_author(value: str) -> str:
    x = (value or "").replace("[[", "").replace("]]", "").strip()
    return normalize_text(x)


def normalize_doi(value: str) -> str:
    x = (value or "").strip().lower()
    if not x or x in {"n/a", "na", "none", "unknown", "pending"}:
        return ""
    x = x.replace("https://doi.org/", "").replace("http://doi.org/", "")
    x = x.replace("https://dx.doi.org/", "").replace("http://dx.doi.org/", "")
    x = x.replace("doi:", "").strip().rstrip(".")
    return x


def extract_arxiv_id(*values: str) -> str:
    for raw in values:
        text = (raw or "").lower()
        if "arxiv" not in text and "10.48550" not in text:
            continue
        m = ARXIV_ID_RE.search(text)
        if m:
            return m.group(1)
    return ""


def compute_richness(fields: dict, body: str, key: str) -> int:
    score = 0

    if fields.get("key_contribution", "").strip() and fields.get("key_contribution", "").strip().upper() != "N/A":
        score += 2
    if fields.get("significance", "").strip() and fields.get("significance", "").strip().upper() != "N/A":
        score += 2

    abstract = fields.get("abstract", "")
    if len(abstract) > 100:
        score += 2

    doi = fields.get("doi", "")
    if doi and doi.strip().upper() != "N/A":
        score += 1

    if fields.get("publication", "").strip():
        score += 1

    pages = fields.get("pages", "")
    if pages and pages.strip().upper() != "N/A":
        score += 1
    elif "**Pages:**" in body:
        score += 1

    local_pdf = fields.get("local_pdf", "")
    if "[[" in local_pdf and "]]" in local_pdf:
        score += 1

    if fields.get("pdf_extract", "").strip():
        score += 1

    first_author = fields.get("first_author", "")
    if "[[" in first_author and "]]" in first_author:
        score += 1

    if "## Abstract" in body and len(body.split("## Abstract", 1)[-1].split("##")[0].strip()) > 50:
        score += 1
    if "## Citation Info" in body or "## Citation" in body:
        score += 1

    if key.startswith("EXSR"):
        score -= 2
    if key.startswith("AUTO_"):
        score -= 1

    return score


def load_papers() -> List[PaperRecord]:
    out: List[PaperRecord] = []

    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        try:
            content = paper_path.read_text(encoding="utf-8")
            fm_text, body = extract_frontmatter(content)
            fields = parse_frontmatter(fm_text)
        except Exception:
            continue

        key = fields.get("key", "")
        title = (
            fields.get("short_title", "").strip('"').strip("'")
            or fields.get("title", "").strip('"').strip("'")
            or paper_path.stem
        )
        first_author = fields.get("first_author", "")
        year = fields.get("year", "").strip().strip('"').strip("'")
        doi = normalize_doi(fields.get("doi", ""))
        url = fields.get("url", "").strip().strip('"').strip("'")
        external_pdf = fields.get("external_pdf", "").strip().strip('"').strip("'")
        arxiv_id = extract_arxiv_id(url, external_pdf, fields.get("doi", ""))
        richness = compute_richness(fields, body, key)

        has_pdf = False
        local_pdf = fields.get("local_pdf", "")
        if local_pdf and "[[" in local_pdf and "]]" in local_pdf:
            ref = local_pdf.replace("[[", "").replace("]]", "").split("|")[0].strip()
            ref = ref.replace("Lit-WS-PDFs/", "")
            pdf_path = PDFS_DIR / ref
            has_pdf = pdf_path.exists()

        has_extract = False
        extract_ref = fields.get("pdf_extract", "").strip().strip('"').strip("'")
        if extract_ref:
            extract_path = PDF_EXTRACTS_DIR / extract_ref.replace("PDF Extracts/", "")
            has_extract = extract_path.exists()

        out.append(
            PaperRecord(
                filename=paper_path.name,
                key=key,
                title=title,
                norm_title=normalize_text(title),
                first_author=first_author,
                norm_first_author=normalize_author(first_author),
                year=year,
                doi=doi,
                arxiv_id=arxiv_id,
                url=url,
                external_pdf=external_pdf,
                richness=richness,
                has_pdf_on_disk=has_pdf,
                has_extract_on_disk=has_extract,
            )
        )

    return out


def choose_primary(a: PaperRecord, b: PaperRecord) -> str:
    if a.richness != b.richness:
        return a.filename if a.richness > b.richness else b.filename
    if a.has_pdf_on_disk != b.has_pdf_on_disk:
        return a.filename if a.has_pdf_on_disk else b.filename
    if a.has_extract_on_disk != b.has_extract_on_disk:
        return a.filename if a.has_extract_on_disk else b.filename
    return a.filename if len(a.filename) <= len(b.filename) else b.filename


def year_gap(a: str, b: str) -> Optional[int]:
    if not YEAR_RE.match(a or "") or not YEAR_RE.match(b or ""):
        return None
    return abs(int(a) - int(b))


def similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def load_existing_decisions(path: Path) -> Dict[str, Tuple[str, str]]:
    if not path.exists():
        return {}
    out: Dict[str, Tuple[str, str]] = {}
    try:
        rows = csv.DictReader(path.open(encoding="utf-8"))
        for r in rows:
            pair_key = (r.get("pair_key") or "").strip()
            if not pair_key:
                continue
            out[pair_key] = (
                (r.get("decision") or "").strip(),
                (r.get("review_notes") or "").strip(),
            )
    except Exception:
        return {}
    return out


def build_exact_pair_set(exact_groups: List[dict]) -> set:
    pairs = set()
    for g in exact_groups:
        papers = [p.get("filename", "") for p in g.get("papers", []) if p.get("filename")]
        papers = sorted(set(papers))
        for i in range(len(papers)):
            for j in range(i + 1, len(papers)):
                pairs.add((papers[i], papers[j]))
    return pairs


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate dedup review artifacts")
    parser.add_argument("--date-prefix", default=date.today().strftime("%Y%m%d"))
    parser.add_argument("--exact-groups", default=None, help="Path to duplicate_groups.json")
    args = parser.parse_args()

    date_prefix = args.date_prefix

    if args.exact_groups:
        exact_path = Path(args.exact_groups)
        if not exact_path.is_absolute():
            exact_path = WORKSPACE_ROOT / exact_path
    else:
        exact_path = LOGS_DIR / f"{date_prefix}-duplicate_groups.json"

    if not exact_path.exists():
        raise SystemExit(f"Exact groups file not found: {exact_path}")

    exact_groups = json.loads(exact_path.read_text(encoding="utf-8"))
    papers = load_papers()
    paper_by_name: Dict[str, PaperRecord] = {p.filename: p for p in papers}
    exact_pair_set = build_exact_pair_set(exact_groups)

    print(f"Loaded papers: {len(papers)}")
    print(f"Loaded exact groups: {len(exact_groups)}")

    # 1) Exact review CSV
    exact_review_rows: List[dict] = []
    for g in exact_groups:
        gid = g.get("group_id")
        shared = g.get("shared_identifiers", [])
        sid_types = sorted({x.get("type", "") for x in shared if isinstance(x, dict)})
        sid_value = " | ".join(f"{x.get('type')}:{x.get('value')}" for x in shared if isinstance(x, dict))
        group_papers = g.get("papers", [])
        primary = next((x for x in group_papers if x.get("is_primary")), None)
        duplicates = [x for x in group_papers if not x.get("is_primary")]

        dois = {normalize_doi((x.get("doi") or "")) for x in group_papers}
        dois = {d for d in dois if d}
        doi_conflict = len(dois) > 1

        auto_safe = all(t in {"doi", "arxiv", "url"} for t in sid_types) and not doi_conflict
        needs_review = doi_conflict

        for dup in duplicates:
            exact_review_rows.append(
                {
                    "group_id": gid,
                    "group_size": len(group_papers),
                    "shared_identifiers": sid_value,
                    "identifier_types": ",".join(sid_types),
                    "primary_filename": (primary or {}).get("filename", ""),
                    "primary_key": (primary or {}).get("key", ""),
                    "duplicate_filename": dup.get("filename", ""),
                    "duplicate_key": dup.get("key", ""),
                    "primary_richness": (primary or {}).get("richness_score", ""),
                    "duplicate_richness": dup.get("richness_score", ""),
                    "auto_safe": "true" if auto_safe else "false",
                    "needs_review": "true" if needs_review else "false",
                    "review_reason": "doi_conflict" if doi_conflict else "",
                }
            )

    exact_review_path = LOGS_DIR / f"{date_prefix}-duplicate_groups_review.csv"
    with exact_review_path.open("w", encoding="utf-8", newline="") as f:
        fields = list(exact_review_rows[0].keys()) if exact_review_rows else [
            "group_id", "group_size", "shared_identifiers", "identifier_types",
            "primary_filename", "primary_key", "duplicate_filename", "duplicate_key",
            "primary_richness", "duplicate_richness", "auto_safe", "needs_review", "review_reason",
        ]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in exact_review_rows:
            w.writerow(r)

    # 2) Exhaustive fuzzy scan
    fuzzy_rows: List[dict] = []
    candidate_idx = 1
    total_pairs = 0

    for i in range(len(papers)):
        a = papers[i]
        if not a.norm_title:
            continue
        for j in range(i + 1, len(papers)):
            b = papers[j]
            if not b.norm_title:
                continue
            total_pairs += 1

            sim = similarity(a.norm_title, b.norm_title)
            if sim < 0.88:
                continue

            author_match = bool(a.norm_first_author and b.norm_first_author and a.norm_first_author == b.norm_first_author)
            same_doi = bool(a.doi and b.doi and a.doi == b.doi)
            same_arxiv = bool(a.arxiv_id and b.arxiv_id and a.arxiv_id == b.arxiv_id)
            gap = year_gap(a.year, b.year)
            gap_ok = gap is not None and gap <= 1

            confidence = ""
            reason_parts: List[str] = []
            if sim >= 0.96:
                confidence = "HIGH"
                reason_parts.append("title>=0.96")
            elif sim >= 0.93 and (author_match or same_doi or same_arxiv):
                confidence = "HIGH"
                reason_parts.append("title>=0.93+support")
            elif sim >= 0.90 and (author_match or same_arxiv or gap_ok):
                confidence = "MEDIUM"
                reason_parts.append("title>=0.90+support")
            elif sim >= 0.88 and author_match:
                confidence = "MEDIUM"
                reason_parts.append("title>=0.88+author")
            else:
                continue

            pair = tuple(sorted((a.filename, b.filename)))
            exact_overlap = pair in exact_pair_set
            recommended_primary = choose_primary(a, b)
            pair_key = f"{pair[0]}||{pair[1]}"

            if author_match:
                reason_parts.append("author_match")
            if same_doi:
                reason_parts.append("same_doi")
            if same_arxiv:
                reason_parts.append("same_arxiv")
            if gap is not None:
                reason_parts.append(f"year_gap={gap}")
            if exact_overlap:
                reason_parts.append("already_in_exact_group")

            fuzzy_rows.append(
                {
                    "candidate_id": f"FUZ{candidate_idx:06d}",
                    "pair_key": pair_key,
                    "paper_a": a.filename,
                    "paper_b": b.filename,
                    "key_a": a.key,
                    "key_b": b.key,
                    "title_a": a.title,
                    "title_b": b.title,
                    "title_similarity": f"{sim:.4f}",
                    "author_match": "true" if author_match else "false",
                    "same_doi": "true" if same_doi else "false",
                    "same_arxiv": "true" if same_arxiv else "false",
                    "year_gap": "" if gap is None else str(gap),
                    "exact_overlap": "true" if exact_overlap else "false",
                    "recommended_primary": recommended_primary,
                    "confidence": confidence,
                    "reason": ";".join(reason_parts),
                }
            )
            candidate_idx += 1

    fuzzy_rows.sort(key=lambda r: (-float(r["title_similarity"]), r["paper_a"], r["paper_b"]))

    fuzzy_csv_path = LOGS_DIR / f"{date_prefix}-duplicate_candidates_fuzzy.csv"
    fuzzy_json_path = LOGS_DIR / f"{date_prefix}-duplicate_candidates_fuzzy.json"
    with fuzzy_csv_path.open("w", encoding="utf-8", newline="") as f:
        fields = list(fuzzy_rows[0].keys()) if fuzzy_rows else [
            "candidate_id", "pair_key", "paper_a", "paper_b", "key_a", "key_b",
            "title_a", "title_b", "title_similarity", "author_match", "same_doi",
            "same_arxiv", "year_gap", "exact_overlap", "recommended_primary",
            "confidence", "reason",
        ]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in fuzzy_rows:
            w.writerow(r)

    fuzzy_payload = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "total_papers": len(papers),
        "total_pairs_scanned": total_pairs,
        "candidate_count": len(fuzzy_rows),
        "confidence_counts": dict(Counter(r["confidence"] for r in fuzzy_rows)),
        "candidates": fuzzy_rows,
    }
    fuzzy_json_path.write_text(json.dumps(fuzzy_payload, indent=2, ensure_ascii=False), encoding="utf-8")

    # 3) Manual review queue (preserve prior decisions)
    manual_path = LOGS_DIR / f"{date_prefix}-dedup_manual_review.csv"
    prior_decisions = load_existing_decisions(manual_path)

    manual_rows: List[dict] = []
    for r in fuzzy_rows:
        if r["exact_overlap"] == "true":
            # Exact groups are handled via exact consolidation pass.
            continue
        pair_key = r["pair_key"]
        prior_decision, prior_notes = prior_decisions.get(pair_key, ("defer", ""))
        manual_rows.append(
            {
                "candidate_id": r["candidate_id"],
                "pair_key": pair_key,
                "paper_a": r["paper_a"],
                "paper_b": r["paper_b"],
                "title_similarity": r["title_similarity"],
                "author_match": r["author_match"],
                "year_gap": r["year_gap"],
                "same_doi": r["same_doi"],
                "same_arxiv": r["same_arxiv"],
                "recommended_primary": r["recommended_primary"],
                "confidence": r["confidence"],
                "reason": r["reason"],
                "decision": prior_decision or "defer",
                "review_notes": prior_notes,
            }
        )

    with manual_path.open("w", encoding="utf-8", newline="") as f:
        fields = list(manual_rows[0].keys()) if manual_rows else [
            "candidate_id", "pair_key", "paper_a", "paper_b", "title_similarity",
            "author_match", "year_gap", "same_doi", "same_arxiv", "recommended_primary",
            "confidence", "reason", "decision", "review_notes",
        ]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in manual_rows:
            w.writerow(r)

    # 4) Build approved fuzzy groups JSON
    approved_edges = []
    for r in manual_rows:
        if (r.get("decision") or "").strip().lower() == "approve_merge":
            approved_edges.append((r["paper_a"], r["paper_b"], r["candidate_id"]))

    parent: Dict[str, str] = {}
    edge_meta: Dict[Tuple[str, str], List[str]] = defaultdict(list)

    def find(x: str) -> str:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for a, b, cid in approved_edges:
        for node in (a, b):
            if node not in parent:
                parent[node] = node
        pair = tuple(sorted((a, b)))
        edge_meta[pair].append(cid)
        union(a, b)

    groups_by_root: Dict[str, List[str]] = defaultdict(list)
    for node in parent:
        groups_by_root[find(node)].append(node)

    fuzzy_groups = []
    gid = 1
    for _, members in sorted(groups_by_root.items()):
        members = sorted(set(members))
        if len(members) < 2:
            continue

        member_records = [paper_by_name[m] for m in members if m in paper_by_name]
        if len(member_records) < 2:
            continue
        member_records.sort(
            key=lambda p: (
                -p.richness,
                -(1 if p.has_pdf_on_disk else 0),
                -(1 if p.has_extract_on_disk else 0),
                len(p.filename),
            )
        )
        primary_name = member_records[0].filename

        ids = []
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                pair = tuple(sorted((members[i], members[j])))
                for cid in edge_meta.get(pair, []):
                    ids.append({"type": "fuzzy_manual", "value": cid})

        fuzzy_groups.append(
            {
                "group_id": gid,
                "shared_identifiers": ids or [{"type": "fuzzy_manual", "value": "manual_approved"}],
                "papers": [
                    {
                        "filename": p.filename,
                        "key": p.key,
                        "richness_score": p.richness,
                        "is_primary": p.filename == primary_name,
                        "has_pdf_on_disk": p.has_pdf_on_disk,
                        "has_extract_on_disk": p.has_extract_on_disk,
                        "doi": p.doi,
                        "year": p.year,
                        "first_author": p.first_author,
                    }
                    for p in member_records
                ],
            }
        )
        gid += 1

    fuzzy_approved_path = LOGS_DIR / f"{date_prefix}-duplicate_groups_fuzzy_approved.json"
    fuzzy_approved_path.write_text(json.dumps(fuzzy_groups, indent=2, ensure_ascii=False), encoding="utf-8")

    summary_path = LOGS_DIR / f"{date_prefix}-dedup_review_summary.json"
    summary = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "date_prefix": date_prefix,
        "inputs": {
            "exact_groups_json": str(exact_path),
            "total_papers": len(papers),
        },
        "exact": {
            "group_count": len(exact_groups),
            "pair_rows": len(exact_review_rows),
            "review_csv": str(exact_review_path),
        },
        "fuzzy": {
            "pairs_scanned": total_pairs,
            "candidate_count": len(fuzzy_rows),
            "confidence_counts": dict(Counter(r["confidence"] for r in fuzzy_rows)),
            "candidates_csv": str(fuzzy_csv_path),
            "candidates_json": str(fuzzy_json_path),
        },
        "manual_review": {
            "rows": len(manual_rows),
            "decision_counts": dict(Counter((r.get("decision") or "defer").strip().lower() for r in manual_rows)),
            "csv": str(manual_path),
        },
        "fuzzy_approved_groups": {
            "group_count": len(fuzzy_groups),
            "json": str(fuzzy_approved_path),
        },
    }
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\nReview artifact summary")
    print(f"- exact review rows: {len(exact_review_rows)}")
    print(f"- fuzzy pairs scanned: {total_pairs}")
    print(f"- fuzzy candidates: {len(fuzzy_rows)}")
    print(f"- manual review rows: {len(manual_rows)}")
    print(f"- approved fuzzy groups: {len(fuzzy_groups)}")
    print(f"- wrote: {exact_review_path}")
    print(f"- wrote: {fuzzy_csv_path}")
    print(f"- wrote: {fuzzy_json_path}")
    print(f"- wrote: {manual_path}")
    print(f"- wrote: {fuzzy_approved_path}")
    print(f"- wrote: {summary_path}")


if __name__ == "__main__":
    main()
