#!/usr/bin/env python3
"""Build the unified feature matrix by merging:
  - Candidate extraction data (YAML frontmatter)
  - Depth assessment (Experts 1-4: A2, A4, A5, A6, A7, A8, B1, B2, B10, theories)
  - Impact assessment (Experts 5-7: safety, B6-B9, C3, C5)
  - Citation counts (Semantic Scholar: C1, C2)

Then compute composite scores with 50/30/20 weighting.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

BASE = Path("/Users/jimmy.lin/Documents/CEI-Literature-Vault/CEI-Lit-WS/MORAL-PSYCH")
CURRENT_YEAR = 2026


def load_json(path: Path) -> list | dict:
    return json.loads(path.read_text(encoding="utf-8"))


def index_by_file(entries: list) -> dict:
    """Index a list of dicts by their 'file' field."""
    idx = {}
    for e in entries:
        f = e.get("file", "")
        if f:
            idx[f] = e
    return idx


def compute_age_normalized_rate(citations: int, year: int) -> float:
    """Citations per year, with minimum age of 0.5 years."""
    age = max(CURRENT_YEAR - year + 0.5, 0.5)
    return round(citations / age, 1)


def score_a1(theories: list) -> float:
    """A1: Number of theories engaged. Normalize to 0-100."""
    n = len(theories) if theories else 0
    # Scale: 0=0, 1=30, 2=60, 3=80, 4+=100
    if n == 0: return 0
    if n == 1: return 30
    if n == 2: return 60
    if n == 3: return 80
    return 100


def score_a2(val: int) -> float:
    """A2: Operationalization depth. 1-4 -> 0-100."""
    return {1: 10, 2: 40, 3: 70, 4: 100}.get(val, 0)


def score_a3(measurement_target: str) -> float:
    """A3: Measurement target richness."""
    targets = {
        "Values/dispositions": 80, "Judgments": 70, "Reasoning process": 90,
        "Behavioral tendencies": 60, "Meta-cognitive awareness": 100,
    }
    # Default based on format
    return 70  # Most benchmarks measure judgments


def score_a4(source_instrument: str) -> float:
    """A4: Source instrument. Has one = 100, partial = 50, none = 0."""
    if not source_instrument or source_instrument.lower() in ("none", "n/a", ""):
        return 0
    if "original" in source_instrument.lower():
        return 80  # Original but purpose-built
    return 100  # Validated instrument


def score_a5(human_baseline: str) -> float:
    """A5: Human baseline availability."""
    bl = human_baseline.lower() if human_baseline else "no"
    if "published norms" in bl: return 100
    if "paper-specific" in bl: return 70
    if "partial" in bl: return 40
    return 0


def score_a6(val: int) -> float:
    """A6: Construct validity. 1-5 -> 0-100."""
    return {1: 10, 2: 30, 3: 50, 4: 75, 5: 100}.get(val, 0)


def compute_pd(a1, a2, a3, a4, a5, a6) -> float:
    """Psychological Depth composite.
    PD = A2×25 + A6×20 + A1×15 + A5×15 + A3×15 + A4×10
    Weights sum to 100.
    """
    return (a2 * 0.25 + a6 * 0.20 + a1 * 0.15 + a5 * 0.15 + a3 * 0.15 + a4 * 0.10)


def score_b1(fmt: str) -> float:
    """B1: Format. MCQ/Binary are easiest for LLMs."""
    fmt_lower = (fmt or "").lower()
    if "mcq" in fmt_lower or "multiple choice" in fmt_lower: return 100
    if "binary" in fmt_lower: return 90
    if "forced-choice" in fmt_lower: return 85
    if "likert" in fmt_lower: return 70
    if "scenario rating" in fmt_lower: return 60
    if "mixed" in fmt_lower: return 50
    if "free-text" in fmt_lower: return 30
    if "multi-turn" in fmt_lower: return 20
    if "game" in fmt_lower: return 15
    return 40


def score_b2(size: int) -> float:
    """B2: Dataset size. Larger = better, with diminishing returns."""
    if size <= 0: return 10
    if size < 50: return 20
    if size < 200: return 40
    if size < 1000: return 60
    if size < 5000: return 75
    if size < 20000: return 85
    return 100


def score_b3(data_url: str) -> float:
    """B3: Data availability."""
    if not data_url: return 0
    url = data_url.lower()
    if "huggingface" in url: return 100
    if "github.com" in url: return 95
    if "osf.io" in url: return 90
    if "anonymous" in url: return 60  # Anonymous review links may expire
    return 70


def score_b4(has_code: bool) -> float:
    """B4: Code availability."""
    return 80 if has_code else 10


def score_b6(impl_score: float) -> float:
    """B6/B7: Harness implementability (already 0-100 scale)."""
    return min(max(impl_score, 0), 100)


def score_b10(fidelity: str) -> float:
    """B10: LLM administration fidelity."""
    fl = (fidelity or "").lower()
    if "direct" in fl: return 100
    if "adapted" in fl: return 70
    if "substantially" in fl: return 40
    if "paradigm" in fl: return 10
    return 50


def compute_pe(b1, b2, b3, b4, b6, b7, b10) -> float:
    """Practical Ease composite.
    PE = B3×20 + B2×15 + B6×15 + B7×15 + B1×10 + B4×10 + B10×15
    Weights sum to 100.
    """
    return (b3 * 0.20 + b2 * 0.15 + b6 * 0.15 + b7 * 0.15 +
            b1 * 0.10 + b4 * 0.10 + b10 * 0.15)


def score_c1(citations: int) -> float:
    """C1: Raw citation count, log-scaled."""
    if citations is None or citations <= 0: return 0
    if citations < 5: return 10
    if citations < 20: return 30
    if citations < 50: return 50
    if citations < 100: return 65
    if citations < 200: return 75
    if citations < 500: return 85
    return 100


def score_c2(rate: float) -> float:
    """C2: Age-normalized citation rate."""
    if rate <= 0: return 0
    if rate < 2: return 15
    if rate < 5: return 30
    if rate < 10: return 50
    if rate < 25: return 65
    if rate < 50: return 80
    if rate < 100: return 90
    return 100


def score_c3(tier: int) -> float:
    """C3: Venue tier."""
    return {1: 100, 2: 70, 3: 45, 4: 20}.get(tier, 20)


def score_c5(hub: str) -> float:
    """C5: Hub/leaderboard presence."""
    h = (hub or "").lower()
    if "paperswithcode" in h: return 100
    if "huggingface" in h: return 90
    if "github" in h: return 50
    return 0


def compute_ci(c1, c2, c3, c5) -> float:
    """Citation Impact composite.
    CI = C1×25 + C2×25 + C3×20 + C4×15 + C5×15
    Note: C4 (downstream adoption) is hard to measure, so we redistribute its weight.
    CI = C1×30 + C2×30 + C3×25 + C5×15
    """
    return (c1 * 0.30 + c2 * 0.30 + c3 * 0.25 + c5 * 0.15)


def main():
    # Load all data sources
    candidates_data = load_json(BASE / "20260403-moral-psych-benchmark-candidates.json")
    candidates = candidates_data["candidates"]
    cand_idx = index_by_file(candidates)

    depth = load_json(BASE / "20260403-council-depth-assessment.json")
    depth_idx = index_by_file(depth)

    impact = load_json(BASE / "20260403-council-impact-assessment.json")
    impact_idx = index_by_file(impact)

    citations = load_json(BASE / "20260403-citation-counts.json")
    cite_idx = index_by_file(citations)

    # Build matrix for papers that have depth assessment (top ~40)
    matrix = []
    seen_files = set()

    for d in depth:
        f = d.get("file", "")
        if not f or f in seen_files:
            continue
        seen_files.add(f)

        c = cand_idx.get(f, {})
        imp = impact_idx.get(f, {})
        cit = cite_idx.get(f, {})

        year = c.get("year", 0)
        raw_citations = cit.get("citation_count")
        age_rate = compute_age_normalized_rate(raw_citations or 0, year) if raw_citations else 0

        # Tier A scores
        a1 = score_a1(d.get("theories_verified", []))
        a2 = score_a2(d.get("A2_operationalization", 0))
        a3 = score_a3("")  # Default
        a4 = score_a4(d.get("A4_source_instrument", ""))
        a5 = score_a5(d.get("A5_human_baseline", ""))
        a6 = score_a6(d.get("A6_construct_validity", 0))
        pd = compute_pd(a1, a2, a3, a4, a5, a6)

        # Tier B scores
        b1 = score_b1(d.get("B1_format", ""))
        b2 = score_b2(d.get("B2_size", 0) or 0)
        b3 = score_b3(c.get("data_url", ""))
        b4 = score_b4(bool(c.get("data_url", "")))
        b6 = score_b6(imp.get("B7_implementability_score", 30))
        b7 = b6  # Same as B6 for now
        b10 = score_b10(d.get("B10_llm_fidelity", ""))
        pe = compute_pe(b1, b2, b3, b4, b6, b7, b10)

        # Tier C scores
        c1 = score_c1(raw_citations)
        c2 = score_c2(age_rate)
        c3 = score_c3(imp.get("C3_venue_tier", 4))
        c5 = score_c5(imp.get("C5_hub_presence", ""))
        ci = compute_ci(c1, c2, c3, c5)

        # COMPOSITE = PD × 0.50 + PE × 0.30 + CI × 0.20
        composite = pd * 0.50 + pe * 0.30 + ci * 0.20

        entry = {
            "file": f,
            "short_title": c.get("short_title", d.get("short_title", "")),
            "year": year,
            "authors": c.get("authors", ""),
            "publication": c.get("publication", ""),
            "data_url": c.get("data_url", ""),
            "candidate_type": c.get("candidate_type", ""),
            "has_data": c.get("has_data", False),
            # Raw Tier A
            "A1_theories": d.get("theories_verified", []),
            "A2_operationalization": d.get("A2_operationalization", 0),
            "A2_rationale": d.get("A2_rationale", ""),
            "A4_source_instrument": d.get("A4_source_instrument", ""),
            "A5_human_baseline": d.get("A5_human_baseline", ""),
            "A6_construct_validity": d.get("A6_construct_validity", 0),
            "A6_rationale": d.get("A6_rationale", ""),
            "A7_cultural_provenance": d.get("A7_cultural_provenance", ""),
            "A8_languages": d.get("A8_languages", []),
            # Raw Tier B
            "B1_format": d.get("B1_format", ""),
            "B2_size": d.get("B2_size", 0),
            "B2_size_notes": d.get("B2_size_notes", ""),
            "B8_scorer_type": imp.get("B8_scorer_type", ""),
            "B9_model_compat": imp.get("B9_model_compat", ""),
            "B10_llm_fidelity": d.get("B10_llm_fidelity", ""),
            # Raw Tier C
            "C1_citations": raw_citations,
            "C2_age_normalized": age_rate,
            "C3_venue_tier": imp.get("C3_venue_tier", 4),
            "C5_hub_presence": imp.get("C5_hub_presence", ""),
            # Tier D metadata
            "D3_llms_evaluated": c.get("llm_assessed", ""),
            "D5_source_publication": d.get("A4_source_instrument", ""),
            # Safety
            "safety_relevance": imp.get("safety_relevance", 0),
            # Harness tiers
            "harness_tiers": imp.get("B6_harness_tiers", {}),
            "implementability_score": imp.get("B7_implementability_score", 0),
            # Scored values (0-100)
            "scores": {
                "A1": round(a1, 1), "A2": round(a2, 1), "A3": round(a3, 1),
                "A4": round(a4, 1), "A5": round(a5, 1), "A6": round(a6, 1),
                "PD": round(pd, 1),
                "B1": round(b1, 1), "B2": round(b2, 1), "B3": round(b3, 1),
                "B4": round(b4, 1), "B6": round(b6, 1), "B10": round(b10, 1),
                "PE": round(pe, 1),
                "C1": round(c1, 1), "C2": round(c2, 1), "C3": round(c3, 1),
                "C5": round(c5, 1),
                "CI": round(ci, 1),
            },
            "composite": round(composite, 2),
        }
        matrix.append(entry)

    # Sort by composite descending
    matrix.sort(key=lambda e: -e["composite"])

    # Add rank
    for i, e in enumerate(matrix, 1):
        e["rank"] = i

    # Summary
    summary = {
        "total_entries": len(matrix),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "weighting": "PD=0.50, PE=0.30, CI=0.20",
        "composite_stats": {
            "max": round(max(e["composite"] for e in matrix), 2),
            "min": round(min(e["composite"] for e in matrix), 2),
            "mean": round(sum(e["composite"] for e in matrix) / len(matrix), 2),
            "median": round(sorted(e["composite"] for e in matrix)[len(matrix) // 2], 2),
        },
        "hard_gate_pass": sum(1 for e in matrix if e["scores"]["PD"] >= 40 and e["has_data"]),
    }

    output = {"summary": summary, "matrix": matrix}

    out_path = BASE / "20260403-moral-psych-benchmark-feature-matrix.json"
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Feature matrix written: {out_path}")
    print(f"Entries: {len(matrix)}")
    print(f"Composite range: {summary['composite_stats']['min']} - {summary['composite_stats']['max']}")
    print(f"Mean: {summary['composite_stats']['mean']}")
    print(f"Papers passing hard gates (PD>=40 + data): {summary['hard_gate_pass']}")

    print(f"\n{'Rank':>4} {'Comp':>6} {'PD':>5} {'PE':>5} {'CI':>5} {'Title':<50} {'Theories'}")
    print("-" * 120)
    for e in matrix[:25]:
        title = e["short_title"][:45]
        theories = ",".join(e["A1_theories"])[:25]
        print(f"{e['rank']:4} {e['composite']:6.1f} {e['scores']['PD']:5.1f} {e['scores']['PE']:5.1f} {e['scores']['CI']:5.1f} {title:<50} {theories}")


if __name__ == "__main__":
    main()
