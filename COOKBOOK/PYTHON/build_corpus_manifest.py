#!/usr/bin/env python3
"""
COOKBOOK Phase 0 — Corpus manifest builder.

Filters papers/ YAML frontmatter for the values-alignment subset and emits a
dated manifest JSON that drives the evidence-card reader fan-out. Also
enumerates PDF Extracts/AI Labs/ into a dated listing for shortlist curation.

Read-only over the corpus; writes only into COOKBOOK/30-EVIDENCE/.

Usage:
    python build_corpus_manifest.py
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]  # CEI-Lit-WS/
sys.path.insert(0, str(WORKSPACE / ".agent"))

from lib.config import PAPERS_DIR, PDF_EXTRACTS_DIR, WORKSPACE_ROOT  # noqa: E402
from lib.yaml_utils import extract_frontmatter  # noqa: E402

EVIDENCE_DIR = WORKSPACE / "COOKBOOK" / "30-EVIDENCE"
DATE_PREFIX = "20260705"

NORMATIVE_KEYS = [
    "virtue_ethics",
    "deontological_ethics",
    "utilitarian_ethics",
    "contractarian_ethics",
    "care_ethics",
]

ETHICS_PERSPECTIVES = {
    "AI Safety & Alignment",
    "Moral Reasoning & Psychology",
    "Machine Ethics",
    "Social & Cultural Values",
    "General Ethics",
}

THIN_LINE_THRESHOLD = 50


def num_field(fm: str, key: str):
    m = re.search(rf'^{re.escape(key)}:\s*"?(-?\d+)"?\s*$', fm, re.M)
    return int(m.group(1)) if m else None


def str_field(fm: str, key: str):
    m = re.search(rf'^{re.escape(key)}:\s*"?([^"\n]*?)"?\s*$', fm, re.M)
    if not m:
        return None
    val = m.group(1).strip()
    return val if val and val != "N/A" else None


def prefixed_positive(fm: str, prefix: str) -> bool:
    """Any key matching ^<prefix>_\\w+: with an integer value > 0."""
    for m in re.finditer(rf'^{prefix}_\w+:\s*"?(\d+)"?\s*$', fm, re.M):
        if int(m.group(1)) > 0:
            return True
    return False


def count_lines(path: Path) -> int:
    try:
        with open(path, "rb") as f:
            return sum(1 for _ in f)
    except OSError:
        return -1


def resolve_extract(fm: str, stem: str):
    """Return (extract_path_str_or_None, resolved_Path_or_None)."""
    rel = str_field(fm, "pdf_extract")
    if rel:
        p = WORKSPACE_ROOT / rel
        if p.exists():
            return rel, p
    # Fallback: conventional location by year prefix
    year = stem[:4]
    p = PDF_EXTRACTS_DIR / year / f"{stem}.md"
    if p.exists():
        return str(p.relative_to(WORKSPACE_ROOT)), p
    return (rel, None)


def build_paper_manifest():
    rows = []
    parse_failures = []
    for paper_path in sorted(PAPERS_DIR.glob("*.md")):
        try:
            content = paper_path.read_text(encoding="utf-8")
            fm, _ = extract_frontmatter(content)
        except (ValueError, UnicodeDecodeError) as e:
            parse_failures.append((paper_path.name, str(e)))
            continue

        ethics_overall = num_field(fm, "ethics_overall")
        if ethics_overall is None or ethics_overall < 50:
            continue

        normative = any((num_field(fm, k) or 0) > 0 for k in NORMATIVE_KEYS)
        mp = prefixed_positive(fm, "mp")
        rv = prefixed_positive(fm, "rv")
        nw = prefixed_positive(fm, "nw")
        is_benchmark = (str_field(fm, "is_benchmark") or "").lower() == "yes"
        is_eval = (str_field(fm, "is_eval") or "").lower() == "yes"
        perspective = str_field(fm, "ethics_perspective")

        if not (
            normative or mp or rv or nw or is_benchmark
            or (perspective in ETHICS_PERSPECTIVES)
        ):
            continue

        stem = paper_path.stem
        extract_rel, extract_abs = resolve_extract(fm, stem)
        if extract_abs is not None:
            lines = count_lines(extract_abs)
            quality = "thin" if lines < THIN_LINE_THRESHOLD else "ok"
        else:
            lines = 0
            quality = "missing"

        domain_tags = []
        if normative:
            domain_tags.append("normative")
        if mp:
            domain_tags.append("mp")
        if rv:
            domain_tags.append("rv")
        if nw:
            domain_tags.append("nw")
        if is_benchmark:
            domain_tags.append("benchmark")

        rows.append({
            "stem": stem,
            "paper_path": str(paper_path.relative_to(WORKSPACE_ROOT)),
            "extract_path": extract_rel,
            "has_extract": extract_abs is not None,
            "extract_lines": lines,
            "extract_quality": quality,
            "ethics_overall": ethics_overall,
            "is_benchmark": is_benchmark,
            "is_eval": is_eval,
            "ethics_perspective": perspective,
            "weird_score": num_field(fm, "weird_score"),
            "domain_tags": domain_tags,
            "reader_tier": "opus" if is_benchmark else "sonnet",
        })
    return rows, parse_failures


ARXIV_RE = re.compile(r"_(\d{4})\.\d{4,5}(v\d+)?$")


def build_ailabs_listing():
    rows = []
    labs_dir = PDF_EXTRACTS_DIR / "AI Labs"
    for path in sorted(labs_dir.rglob("*.md")):
        try:
            content = path.read_text(encoding="utf-8")
            fm, _ = extract_frontmatter(content)
        except (ValueError, UnicodeDecodeError):
            fm = ""
        title = str_field(fm, "title") or path.stem
        title = re.sub(r"\s*-\s*PDF Extract\s*$", "", title)
        m = ARXIV_RE.search(path.stem)
        arxiv_year = None
        if m:
            yy = int(m.group(1)[:2])
            arxiv_year = 2000 + yy
        rows.append({
            "stem": path.stem,
            "extract_path": str(path.relative_to(WORKSPACE_ROOT)),
            "company": str_field(fm, "company"),
            "title": title,
            "pages": num_field(fm, "pages"),
            "arxiv_year": arxiv_year,
            "extract_lines": count_lines(path),
        })
    return rows


def main():
    EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

    rows, failures = build_paper_manifest()
    manifest = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "filter": (
            "ethics_overall>=50 AND (any normative branch>0 OR any mp_*>0 OR "
            "any rv_*>0 OR any nw_*>0 OR is_benchmark==Yes OR "
            "ethics_perspective in " + str(sorted(ETHICS_PERSPECTIVES)) + ")"
        ),
        "counts": {
            "total": len(rows),
            "has_extract": sum(r["has_extract"] for r in rows),
            "quality_ok": sum(r["extract_quality"] == "ok" for r in rows),
            "quality_thin": sum(r["extract_quality"] == "thin" for r in rows),
            "quality_missing": sum(r["extract_quality"] == "missing" for r in rows),
            "tier_opus": sum(r["reader_tier"] == "opus" for r in rows),
            "tier_sonnet": sum(r["reader_tier"] == "sonnet" for r in rows),
            "parse_failures": len(failures),
        },
        "papers": rows,
    }
    manifest_path = EVIDENCE_DIR / f"{DATE_PREFIX}-corpus-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=1), encoding="utf-8")

    ailabs = build_ailabs_listing()
    listing = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "count": len(ailabs),
        "reports": ailabs,
    }
    listing_path = EVIDENCE_DIR / f"{DATE_PREFIX}-ailabs-listing.json"
    listing_path.write_text(json.dumps(listing, indent=1), encoding="utf-8")

    print(f"Manifest: {manifest_path}")
    for k, v in manifest["counts"].items():
        print(f"  {k}: {v}")
    print(f"AI Labs listing: {listing_path} ({len(ailabs)} reports)")
    if failures:
        print("Parse failures:")
        for name, err in failures[:20]:
            print(f"  {name}: {err}")
    thin_missing = [
        (r["stem"], r["extract_quality"], r["extract_lines"])
        for r in rows if r["extract_quality"] != "ok"
    ]
    print(f"Thin/missing extracts ({len(thin_missing)}):")
    for stem, q, n in thin_missing:
        print(f"  [{q}:{n}] {stem}")


if __name__ == "__main__":
    main()
