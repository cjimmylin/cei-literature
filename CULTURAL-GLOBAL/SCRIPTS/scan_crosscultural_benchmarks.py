#!/usr/bin/env python3
"""Scan CEI-Lit-WS vault for papers relevant to cross-cultural values alignment benchmarks.

Reads YAML frontmatter via regex (no YAML parser) and scores relevance 0-100.
Outputs JSON to CULTURAL-GLOBAL/DATA/20260404-benchmark-candidates.json.

Safety: read-only scan — never modifies paper files.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
WS_ROOT = SCRIPT_DIR.parent.parent          # CEI-Lit-WS/
PAPERS_DIR = WS_ROOT / "papers"
EXTRACTS_DIR = WS_ROOT / "PDF Extracts"
OUTPUT_DIR = SCRIPT_DIR.parent / "DATA"
OUTPUT_FILE = OUTPUT_DIR / "20260404-benchmark-candidates.json"

# ── Keywords ───────────────────────────────────────────────────────────────
KEYWORDS: list[str] = [
    "cross-cultural", "values alignment", "moral judgment", "moral reasoning",
    "cultural", "WEIRD", "non-Western", "non-western", "pluralistic",
    "fairness across", "global values", "moral foundations", "Schwartz values",
    "world values survey", "WVS", "Moral Machine", "CultureBench",
    "GlobalOpinionQA", "ETHICS dataset", "NORMAD", "VALUE-BENCH", "PRISM",
    "MoralChoice", "Delphi", "MoralBench", "MoralExceptQA", "PVQ", "SVS",
    "MFQ", "cultural commonsense", "multicultural", "multilingual moral",
    "culture-specific", "value survey", "moral dilemma", "ethical reasoning",
    "cultural bias", "cultural awareness", "Ubuntu", "Confucian",
    "Islamic ethics", "Buddhist ethics", "Dharmic", "Indigenous", "buen vivir",
    "maqasid", "harmony", "tikanga", "ubuntu", "dharma", "karma", "ren", "li",
]

# Pre-compile case-insensitive patterns — use word boundaries for short tokens
KEYWORD_PATTERNS: list[tuple[str, re.Pattern[str]]] = []
for kw in KEYWORDS:
    # Short tokens (<=3 chars) need word boundaries to avoid false positives
    if len(kw) <= 3:
        pat = re.compile(r"\b" + re.escape(kw) + r"\b", re.IGNORECASE)
    else:
        pat = re.compile(re.escape(kw), re.IGNORECASE)
    KEYWORD_PATTERNS.append((kw, pat))

# ── Helpers ────────────────────────────────────────────────────────────────

def extract_frontmatter(text: str) -> str | None:
    """Return frontmatter string between first and second --- markers."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        # Try finding just '--' on its own line (known corruption pattern)
        m = re.search(r"^---?\s*$", text[4:], re.MULTILINE)
        if m:
            end = m.start() + 4
        else:
            return None
    return text[3:end]


def get_field(fm: str, field: str) -> str:
    """Extract a single field value from frontmatter using regex."""
    m = re.search(rf'^{re.escape(field)}:\s*"?(.*?)"?\s*$', fm, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"')
    return ""


def get_int_field(fm: str, field: str) -> int:
    """Extract an integer field, defaulting to 0."""
    val = get_field(fm, field)
    if val:
        try:
            return int(val)
        except ValueError:
            return 0
    return 0


def get_nw_fields(fm: str) -> dict[str, int]:
    """Extract all nw_* fields and their integer values."""
    results = {}
    for m in re.finditer(r'^(nw_\w+):\s*(\d+)', fm, re.MULTILINE):
        results[m.group(1)] = int(m.group(2))
    return results


def get_rv_fields(fm: str) -> dict[str, int]:
    """Extract all rv_* fields and their integer values."""
    results = {}
    for m in re.finditer(r'^(rv_\w+):\s*(\d+)', fm, re.MULTILINE):
        results[m.group(1)] = int(m.group(2))
    return results


def read_extract(fm: str, paper_filename: str) -> str:
    """Read PDF extract text (first 15000 chars). Try pdf_extract field, then construct path."""
    extract_path_str = get_field(fm, "pdf_extract")
    if extract_path_str:
        full_path = WS_ROOT / extract_path_str
        if full_path.exists():
            try:
                return full_path.read_text(errors="replace")[:15000]
            except Exception:
                pass

    # Construct from paper filename: papers/YYYY-Author-Title.md → PDF Extracts/YYYY/YYYY-Author-Title.md
    stem = paper_filename  # already the filename like "2024-Author-Title.md"
    m = re.match(r"(\d{4})-", stem)
    if m:
        year = m.group(1)
        constructed = EXTRACTS_DIR / year / stem
        if constructed.exists():
            try:
                return constructed.read_text(errors="replace")[:15000]
            except Exception:
                pass

    return ""


def find_keyword_matches(title: str, abstract: str, extract: str) -> list[str]:
    """Find which keywords match in the combined text."""
    combined = f"{title} {abstract} {extract}"
    found = []
    for kw, pat in KEYWORD_PATTERNS:
        if pat.search(combined):
            found.append(kw)
    return found


def score_paper(
    is_bench: bool,
    is_eval: bool,
    is_data: bool,
    nw_scores: dict[str, int],
    ethics_overall: int,
    moral_psych: bool,
    rv_scores: dict[str, int],
    keyword_matches: list[str],
) -> tuple[int, dict[str, int]]:
    """Compute relevance score 0-100 with breakdown."""
    breakdown: dict[str, int] = {}

    # Benchmark/eval/dataset flags
    bench_bonus = 20 if is_bench else 0
    eval_bonus = 15 if is_eval else 0
    data_bonus = 10 if is_data else 0
    breakdown["benchmark_flag"] = bench_bonus
    breakdown["eval_flag"] = eval_bonus
    breakdown["dataset_flag"] = data_bonus

    # Non-Western framework scores: +15 per framework >= 20, cap 30
    nw_count = sum(1 for v in nw_scores.values() if v >= 20)
    nw_bonus = min(nw_count * 15, 30)
    breakdown["nw_score_bonus"] = nw_bonus

    # Ethics overall
    ethics_bonus = 10 if ethics_overall >= 50 else 0
    breakdown["ethics_bonus"] = ethics_bonus

    # Moral psychology
    mp_bonus = 5 if moral_psych else 0
    breakdown["moral_psych_bonus"] = mp_bonus

    # Religious values
    rv_bonus = 5 if any(v >= 50 for v in rv_scores.values()) else 0
    breakdown["rv_bonus"] = rv_bonus

    # Keyword matches: +3 each, cap 30
    kw_bonus = min(len(keyword_matches) * 3, 30)
    breakdown["keyword_bonus"] = kw_bonus

    total = bench_bonus + eval_bonus + data_bonus + nw_bonus + ethics_bonus + mp_bonus + rv_bonus + kw_bonus
    total = min(total, 100)

    return total, breakdown


# ── Main ───────────────────────────────────────────────────────────────────

def main() -> None:
    if not PAPERS_DIR.exists():
        print(f"ERROR: Papers directory not found: {PAPERS_DIR}", file=sys.stderr)
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Collect all .md files in papers/ (flat directory)
    paper_files = sorted(PAPERS_DIR.iterdir())
    paper_files = [f for f in paper_files if f.suffix == ".md" and f.is_file()]

    total_scanned = 0
    benchmarks_found = 0
    evals_found = 0
    datasets_found = 0
    candidates: list[dict] = []

    for pf in paper_files:
        total_scanned += 1
        try:
            text = pf.read_text(errors="replace")
        except Exception as e:
            print(f"  WARN: Could not read {pf.name}: {e}", file=sys.stderr)
            continue

        fm = extract_frontmatter(text)
        if fm is None:
            continue

        # Extract fields
        short_title = get_field(fm, "short_title")
        abstract = get_field(fm, "abstract")
        title_field = get_field(fm, "title")
        title = short_title or title_field

        is_bench_str = get_field(fm, "is_benchmark")
        is_eval_str = get_field(fm, "is_eval")
        is_data_str = get_field(fm, "is_dataset")
        is_bench = is_bench_str.strip().lower() == "yes"
        is_eval_flag = is_eval_str.strip().lower() == "yes"
        is_data = is_data_str.strip().lower() == "yes"

        if is_bench:
            benchmarks_found += 1
        if is_eval_flag:
            evals_found += 1
        if is_data:
            datasets_found += 1

        ethics_overall = get_int_field(fm, "ethics_overall")
        moral_psych_str = get_field(fm, "moral_psychology")
        moral_psych = moral_psych_str.strip().lower() == "yes"

        nw_scores = get_nw_fields(fm)
        rv_scores = get_rv_fields(fm)

        data_url = get_field(fm, "DATA_URL")
        if data_url.upper() in ("NA", "N/A", ""):
            data_url = ""

        # Read extract for benchmarks/evals/datasets (extra keyword signal)
        extract_text = ""
        if is_bench or is_eval_flag or is_data:
            extract_text = read_extract(fm, pf.name)

        # Keyword matching
        keyword_matches = find_keyword_matches(title, abstract, extract_text)

        # Score
        relevance, breakdown = score_paper(
            is_bench, is_eval_flag, is_data,
            nw_scores, ethics_overall, moral_psych,
            rv_scores, keyword_matches,
        )

        if relevance >= 20:
            # Filter nw_scores to only non-zero for compactness
            nw_nonzero = {k: v for k, v in nw_scores.items() if v > 0}
            rv_nonzero = {k: v for k, v in rv_scores.items() if v > 0}

            candidates.append({
                "filename": pf.name,
                "short_title": short_title,
                "relevance_score": relevance,
                "score_breakdown": breakdown,
                "is_benchmark": is_bench,
                "is_eval": is_eval_flag,
                "is_dataset": is_data,
                "nw_scores": nw_nonzero,
                "rv_scores": rv_nonzero,
                "ethics_overall": ethics_overall,
                "moral_psychology": moral_psych,
                "data_url": data_url,
                "keyword_matches": keyword_matches,
            })

    # Sort by relevance descending, then by filename for stability
    candidates.sort(key=lambda c: (-c["relevance_score"], c["filename"]))

    # Build output
    above_30 = sum(1 for c in candidates if c["relevance_score"] >= 30)
    output = {
        "metadata": {
            "date": "2026-04-04",
            "total_papers_scanned": total_scanned,
            "benchmarks_found": benchmarks_found,
            "evals_found": evals_found,
            "datasets_found": datasets_found,
            "candidates_scored": len(candidates),
            "candidates_above_30": above_30,
        },
        "candidates": candidates,
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    # ── Summary ────────────────────────────────────────────────────────────
    print("=" * 72)
    print("CROSS-CULTURAL VALUES ALIGNMENT BENCHMARK SCAN")
    print("=" * 72)
    print(f"  Papers scanned:         {total_scanned}")
    print(f"  Benchmarks (is_benchmark=Yes): {benchmarks_found}")
    print(f"  Evaluations (is_eval=Yes):     {evals_found}")
    print(f"  Datasets (is_dataset=Yes):     {datasets_found}")
    print(f"  Candidates (score >= 20):      {len(candidates)}")
    print(f"  Candidates (score >= 30):      {above_30}")
    print(f"  Output: {OUTPUT_FILE}")
    print()

    # Top 20
    print(f"{'Rank':<5} {'Score':<6} {'Bench':<6} {'Eval':<5} {'Data':<5} {'Filename'}")
    print("-" * 72)
    for i, c in enumerate(candidates[:20], 1):
        b = "Y" if c["is_benchmark"] else "-"
        e = "Y" if c["is_eval"] else "-"
        d = "Y" if c["is_dataset"] else "-"
        name = c["filename"]
        if len(name) > 48:
            name = name[:45] + "..."
        print(f"{i:<5} {c['relevance_score']:<6} {b:<6} {e:<5} {d:<5} {name}")

    # Score distribution
    print()
    print("Score distribution:")
    brackets = [(80, 100), (60, 79), (40, 59), (30, 39), (20, 29)]
    for lo, hi in brackets:
        count = sum(1 for c in candidates if lo <= c["relevance_score"] <= hi)
        print(f"  {lo}-{hi}: {count} papers")

    # Top keyword hits
    from collections import Counter
    kw_counter: Counter[str] = Counter()
    for c in candidates:
        kw_counter.update(c["keyword_matches"])
    print()
    print("Top 15 keywords across all candidates:")
    for kw, cnt in kw_counter.most_common(15):
        print(f"  {cnt:>4}x  {kw}")


if __name__ == "__main__":
    main()
