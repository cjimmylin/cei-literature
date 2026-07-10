#!/usr/bin/env python3
"""Extract moral psychology benchmark candidates from the vault.

Uses multiple signals to identify candidates:
1. mp_* scores >= 50 (keyword scorer hits)
2. is_benchmark/is_eval/is_dataset papers with moral-psych-relevant content
3. Papers with DATA_URL and moral/values/ethics keywords in abstract or key_contribution
4. Very strong keyword match (>= 5 patterns)
5. Known benchmark names in title/abstract
6. Non-Western theory keyword density in full-text PDF extracts (Phase 2 expansion)

Covers 11 moral psychology theories (8 Western + 3 non-Western):
  MFT, Schwartz, Trolley, Kohlberg, Dual Process, Intuitionist,
  Dyadic, Identity, Islamic Maqasid, Confucian Role Ethics, Ubuntu Communalism
Plus secondary search patterns for Buddhist ethics and Indigenous relational ethics.

Outputs a JSON file with all candidate papers and their metadata.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from datetime import datetime

PAPERS_DIR = Path(__file__).resolve().parent.parent / "papers"
EXTRACTS_DIR = Path(__file__).resolve().parent.parent / "PDF Extracts"
OUTPUT_DIR = Path(__file__).resolve().parent

# Moral psychology relevance keywords (broader than mp_* scorer)
MP_KEYWORDS = [
    # MFT
    r"\bmoral foundations?\b", r"\bmft\b", r"\bmfq\b", r"\bcare.harm\b",
    r"\bfairness.cheating\b", r"\bloyalty.betrayal\b", r"\bauthority.subversion\b",
    r"\bsanctity\b", r"\bpurity.degradation\b", r"\bliberty.oppression\b",
    # Schwartz
    r"\bschwartz\b", r"\bbasic human values\b", r"\bvalue pluralism\b",
    r"\bpvq\b", r"\bportrait values\b", r"\bvalue orientation\b",
    r"\bvalue survey\b", r"\bworld values survey\b",
    # Trolley / Dilemmas
    r"\btrolley\b", r"\bmoral dilemma\b", r"\bmoral machine\b",
    r"\bfootbridge\b", r"\bsacrificial dilemma\b",
    # Kohlberg
    r"\bkohlberg\b", r"\bmoral development\b", r"\bdefining issues test\b",
    r"\bdit\b", r"\bpre.conventional\b", r"\bpost.conventional\b",
    r"\bheinz dilemma\b",
    # Dual Process
    r"\bdual process\b", r"\bjoshua greene\b", r"\bsystem 1\b", r"\bsystem 2\b",
    # Social Intuitionist
    r"\bsocial intuitionist\b", r"\bmoral dumbfounding\b", r"\bmoral intuition\b",
    # Dyadic
    r"\bdyadic morality\b", r"\bkurt gray\b", r"\bmoral typecasting\b",
    # Moral Identity
    r"\bmoral identity\b", r"\bmoral self\b", r"\bmoral exemplar\b",
    # General moral psychology
    r"\bmoral psychology\b", r"\bmoral cognition\b", r"\bmoral reasoning\b",
    r"\bmoral judgment\b", r"\bmoral judgement\b", r"\bmoral decision\b",
    r"\bethical judgment\b", r"\bethical reasoning\b",
    # Psychometric instruments used for values
    r"\bpsychometric\b", r"\blikert\b", r"\binventory\b",
    r"\bmoral sens\b", r"\bmoral foundation vignette\b",
    # Values alignment
    r"\bvalues? alignment\b", r"\bvalue alignment\b",
    r"\bhuman values?\b", r"\bshared values?\b",
    # Specific benchmarks
    r"\bethics dataset\b", r"\bethics benchmark\b", r"\bmoral bench\b",
    r"\bmoralbench\b", r"\bvaluebench\b", r"\bscruples\b",
    r"\bsocial chemistry\b", r"\bdelphi\b", r"\bmachiavelli\b",
    r"\bmoral integrity corpus\b", r"\bmic\b",
    r"\bmoral stories\b", r"\bmoral choice\b",
    # ----- Theory 9: Islamic Maqasid al-Shariah -----
    r"\bmaqasid\b", r"\bmaslaha\b", r"\bistihsan\b", r"\bhifz al-\w+\b",
    r"\bijtihad\b", r"\bqiyas\b", r"\bislamic ethics\b", r"\bislamic moral\b",
    r"\bfiqh\b", r"\bshariah\b", r"\bhalal\b", r"\bharam\b", r"\bfatwa\b",
    r"\bislamic jurisprudence\b", r"\bislamic law\b", r"\bislamic values\b",
    # ----- Theory 10: Confucian Role Ethics -----
    r"\bconfucian\b", r"\bfilial piety\b", r"\bxiao\b", r"\bjunzi\b",
    r"\bwulun\b", r"\bmencius\b", r"\bmengzi\b", r"\brole ethics\b",
    r"\bchinese ethics\b", r"\beast asian ethics\b", r"\britual propriety\b",
    # ----- Theory 11: Ubuntu Communalism -----
    r"\bubuntu\b", r"\bumuntu\b", r"\bngumuntu\b",
    r"\bcommunitarian ethics\b", r"\bafrican ethics\b", r"\bafrican moral\b",
    r"\brelational personhood\b", r"\bharambee\b", r"\bujamaa\b",
    r"\bcommunal moral\b", r"\bcommunal agency\b",
    r"\bafrican moral philosophy\b", r"\bafrican philosophy\b",
    # ----- Secondary: Buddhist Ethics -----
    r"\bbuddhist ethics\b", r"\bbuddhist moral\b", r"\bfive precepts\b",
    r"\brahma.viharas\b", r"\bsila\b", r"\bahimsa\b",
    # ----- Secondary: Indigenous Relational Ethics -----
    r"\bindigenous ethics\b", r"\bindigenous moral\b", r"\btikanga\b",
    r"\bkaitiakitanga\b", r"\btwo.eyed seeing\b",
    r"\brelational accountability\b",
]
MP_PATTERNS = [re.compile(p, re.IGNORECASE) for p in MP_KEYWORDS]

# Theory-specific keyword groups for per-theory scoring on full-text extracts
THEORY_KEYWORDS: dict[str, list[str]] = {
    "maqasid": [
        r"\bmaqasid\b", r"\bmaslaha\b", r"\bistihsan\b", r"\bhifz al-\w+\b",
        r"\bijtihad\b", r"\bqiyas\b", r"\bislamic ethics\b", r"\bislamic moral\b",
        r"\bfiqh\b", r"\bshariah\b", r"\bhalal\b", r"\bharam\b", r"\bfatwa\b",
        r"\bislamic jurisprudence\b", r"\bislamic law\b", r"\bislamic values\b",
    ],
    "confucian": [
        r"\bconfucian\b", r"\bfilial piety\b", r"\bxiao\b", r"\bjunzi\b",
        r"\bwulun\b", r"\bmencius\b", r"\bmengzi\b", r"\brole ethics\b",
        r"\bchinese ethics\b", r"\beast asian ethics\b", r"\britual propriety\b",
    ],
    "ubuntu": [
        r"\bubuntu\b", r"\bumuntu\b", r"\bngumuntu\b",
        r"\bcommunitarian ethics\b", r"\bafrican ethics\b", r"\bafrican moral\b",
        r"\brelational personhood\b", r"\bharambee\b", r"\bujamaa\b",
        r"\bcommunal moral\b", r"\bcommunal agency\b",
        r"\bafrican moral philosophy\b", r"\bafrican philosophy\b",
    ],
    "buddhist": [
        r"\bbuddhist ethics\b", r"\bbuddhist moral\b", r"\bfive precepts\b",
        r"\brahma.viharas\b", r"\bsila\b", r"\bahimsa\b",
    ],
    "indigenous": [
        r"\bindigenous ethics\b", r"\bindigenous moral\b", r"\btikanga\b",
        r"\bkaitiakitanga\b", r"\btwo.eyed seeing\b",
        r"\brelational accountability\b",
    ],
}
THEORY_PATTERNS: dict[str, list[re.Pattern]] = {
    k: [re.compile(p, re.IGNORECASE) for p in v]
    for k, v in THEORY_KEYWORDS.items()
}

# Theory labels and short names (11 primary + 2 secondary)
THEORY_LABELS = {
    "mft": "Moral Foundations Theory",
    "schwartz": "Schwartz Values",
    "trolley": "Trolley Problem",
    "kohlberg": "Kohlberg Stages",
    "dual_process": "Dual Process",
    "intuitionist": "Intuitionist",
    "dyadic": "Dyadic Morality",
    "identity": "Moral Identity",
    "maqasid": "Islamic Maqasid",
    "confucian": "Confucian Role Ethics",
    "ubuntu": "Ubuntu Communalism",
}

THEORY_SHORT = {
    "mft": "MFT",
    "schwartz": "Schwartz",
    "trolley": "Trolley",
    "kohlberg": "Kohlberg",
    "dual_process": "Dual Proc.",
    "intuitionist": "Intuitionist",
    "dyadic": "Dyadic",
    "identity": "Identity",
    "maqasid": "Maqasid",
    "confucian": "Confucian",
    "ubuntu": "Ubuntu",
}


def extract_field(text: str, key: str) -> str:
    """Extract a YAML field value from frontmatter text."""
    m = re.search(rf'^{re.escape(key)}:\s*"?((?:[^"\n\\]|\\.)*)"?\s*$', text, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"')
    # Fallback for unquoted values
    m = re.search(rf'^{re.escape(key)}:\s*(.+)$', text, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"')
    return ""


def extract_int_field(text: str, key: str) -> int:
    """Extract an integer YAML field."""
    val = extract_field(text, key)
    try:
        return int(val)
    except (ValueError, TypeError):
        return 0


def get_frontmatter(filepath: Path) -> str:
    """Extract YAML frontmatter from a markdown file."""
    content = filepath.read_text(encoding="utf-8", errors="replace")
    if not content.startswith("---"):
        return ""
    end = content.find("\n---", 3)
    if end == -1:
        return ""
    return content[3:end]


def count_keyword_matches(text: str) -> tuple[int, list[str]]:
    """Count how many moral psychology keyword patterns match in text."""
    matches = []
    for pat in MP_PATTERNS:
        if pat.search(text):
            matches.append(pat.pattern)
    return len(matches), matches


def resolve_extract_path(paper_stem: str) -> Path | None:
    """Find PDF extract file for a paper.  Searches year-based subdirs."""
    for subdir in EXTRACTS_DIR.iterdir():
        if not subdir.is_dir():
            continue
        candidate = subdir / f"{paper_stem}.md"
        if candidate.exists():
            return candidate
    return None


def load_extract_text(paper_stem: str) -> str:
    """Load full-text extract for a paper (up to 25K chars)."""
    path = resolve_extract_path(paper_stem)
    if path is None:
        return ""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        return text[:25000].lower()
    except Exception:
        return ""


def count_extract_theory_hits(extract_text: str) -> dict[str, int]:
    """Count per-theory keyword hits in a full-text extract.

    Returns dict mapping theory key -> number of distinct patterns matched.
    Covers 3 new primary theories + 2 secondary search groups.
    """
    hits: dict[str, int] = {}
    if not extract_text:
        return hits
    for theory_key, patterns in THEORY_PATTERNS.items():
        matched = sum(1 for pat in patterns if pat.search(extract_text))
        if matched > 0:
            hits[theory_key] = matched
    return hits


def classify_candidate_type(mp_max: int, is_benchmark: bool, is_eval: bool,
                            is_dataset: bool, keyword_count: int) -> str:
    """Classify the candidate into tiers for the tiered scoring approach."""
    if is_benchmark or is_eval:
        return "benchmark"
    elif is_dataset:
        return "dataset"
    elif mp_max >= 50 or keyword_count >= 3:
        return "dataset"  # potential dataset, needs verification
    return "other"


def main():
    if not PAPERS_DIR.exists():
        print(f"ERROR: Papers directory not found: {PAPERS_DIR}")
        sys.exit(1)

    candidates = []
    all_papers_count = 0

    for paper_file in sorted(PAPERS_DIR.iterdir()):
        if not paper_file.name.endswith(".md"):
            continue
        all_papers_count += 1

        fm = get_frontmatter(paper_file)
        if not fm:
            continue

        # Extract core fields
        short_title = extract_field(fm, "short_title")
        year = extract_int_field(fm, "year")
        authors = extract_field(fm, "authors")
        first_author = extract_field(fm, "first_author")
        doi = extract_field(fm, "doi")
        url = extract_field(fm, "url")
        publication = extract_field(fm, "publication")
        conf_cc = extract_field(fm, "CONF-CC")
        abstract = extract_field(fm, "abstract")
        key_contribution = extract_field(fm, "key_contribution")
        significance = extract_field(fm, "significance")
        data_url = extract_field(fm, "DATA_URL")
        llm_assessed = extract_field(fm, "LLM_assessed")
        data_description = extract_field(fm, "data_description")
        data_metrics = extract_field(fm, "data_metrics")
        pdf_extract = extract_field(fm, "pdf_extract")

        # Benchmark/eval/dataset flags
        is_benchmark = extract_field(fm, "is_benchmark").lower() in ("yes", "true")
        is_eval = extract_field(fm, "is_eval").lower() in ("yes", "true")
        is_dataset = extract_field(fm, "is_dataset").lower() in ("yes", "true")

        # Ethics scores
        ethics_overall = extract_int_field(fm, "ethics_overall")

        # Moral psychology scores (8 original + 3 new non-Western)
        mp_scores = {
            "mp_mft": extract_int_field(fm, "mp_mft"),
            "mp_schwartz": extract_int_field(fm, "mp_schwartz"),
            "mp_trolley": extract_int_field(fm, "mp_trolley"),
            "mp_kohlberg": extract_int_field(fm, "mp_kohlberg"),
            "mp_dual_process": extract_int_field(fm, "mp_dual_process"),
            "mp_intuitionist": extract_int_field(fm, "mp_intuitionist"),
            "mp_dyadic": extract_int_field(fm, "mp_dyadic"),
            "mp_identity": extract_int_field(fm, "mp_identity"),
            "mp_maqasid": extract_int_field(fm, "mp_maqasid"),
            "mp_confucian": extract_int_field(fm, "mp_confucian"),
            "mp_ubuntu": extract_int_field(fm, "mp_ubuntu"),
        }
        mp_max = max(mp_scores.values())
        mp_any_above_50 = any(v >= 50 for v in mp_scores.values())
        moral_psychology = extract_field(fm, "moral_psychology")

        # Keyword matching on searchable text
        searchable = " ".join([
            short_title, abstract, key_contribution, significance,
            data_description, paper_file.stem
        ]).lower()
        keyword_count, keyword_matches = count_keyword_matches(searchable)

        # Selection criteria: include if any of these are true
        include = False
        inclusion_reasons = []

        # Signal 1: High mp_* scores
        if mp_any_above_50:
            include = True
            inclusion_reasons.append(f"mp_score_above_50 (max={mp_max})")

        # Signal 2: Benchmark/eval/dataset with moral psych keywords
        if (is_benchmark or is_eval or is_dataset) and keyword_count >= 2:
            include = True
            inclusion_reasons.append(f"benchmark_with_keywords ({keyword_count} matches)")

        # Signal 3: Has DATA_URL and strong keyword match
        if data_url and keyword_count >= 3:
            include = True
            inclusion_reasons.append(f"data_url_with_keywords ({keyword_count} matches)")

        # Signal 4: Very strong keyword match regardless
        if keyword_count >= 5:
            include = True
            inclusion_reasons.append(f"strong_keyword_match ({keyword_count} matches)")

        # Signal 5: Known benchmark names in title/abstract
        known_benchmarks = [
            "ethics dataset", "ethics benchmark", "moralbench", "valuebench",
            "scruples", "social chemistry", "delphi", "machiavelli",
            "moral integrity corpus", "moral machine", "trolleybench",
            "moral foundations vignette", "moral choice", "value fulcra",
            "cmoraleval", "jethics", "worldvaluesbench", "promoral",
            "bengalimoralbench",
        ]
        for name in known_benchmarks:
            if name in searchable:
                include = True
                inclusion_reasons.append(f"known_benchmark ({name})")
                break

        # Signal 6: Full-text extract hits for non-Western theories
        extract_text = load_extract_text(paper_file.stem)
        extract_theory_hits = count_extract_theory_hits(extract_text)
        # Also scan searchable (title/abstract) for the new theories
        searchable_theory_hits = count_extract_theory_hits(searchable)
        # Merge: take the max per theory
        all_theory_hits: dict[str, int] = {}
        for tk in set(list(extract_theory_hits.keys()) + list(searchable_theory_hits.keys())):
            all_theory_hits[tk] = max(
                extract_theory_hits.get(tk, 0),
                searchable_theory_hits.get(tk, 0),
            )
        if any(v >= 2 for v in all_theory_hits.values()):
            include = True
            hit_summary = ", ".join(
                f"{k}={v}" for k, v in sorted(all_theory_hits.items()) if v >= 2
            )
            inclusion_reasons.append(f"non_western_theory_hit ({hit_summary})")

        if not include:
            continue

        candidate_type = classify_candidate_type(
            mp_max, is_benchmark, is_eval, is_dataset, keyword_count
        )

        candidates.append({
            "file": paper_file.name,
            "short_title": short_title,
            "year": year,
            "authors": authors,
            "first_author": first_author,
            "doi": doi,
            "url": url,
            "publication": publication,
            "conf_cc": conf_cc,
            "abstract": abstract[:500] if abstract else "",
            "key_contribution": key_contribution,
            "significance": significance,
            "data_url": data_url,
            "llm_assessed": llm_assessed,
            "data_description": data_description,
            "data_metrics": data_metrics,
            "pdf_extract": pdf_extract,
            "is_benchmark": is_benchmark,
            "is_eval": is_eval,
            "is_dataset": is_dataset,
            "ethics_overall": ethics_overall,
            "mp_scores": mp_scores,
            "mp_max": mp_max,
            "moral_psychology": moral_psychology,
            "keyword_count": keyword_count,
            "keyword_matches": keyword_matches[:10],  # top 10
            "candidate_type": candidate_type,
            "inclusion_reasons": inclusion_reasons,
            "has_data": bool(data_url),
            "extract_theory_hits": all_theory_hits,
            "has_extract": bool(extract_text),
        })

    # Sort by mp_max desc, then keyword_count desc, then year desc
    candidates.sort(key=lambda c: (-c["mp_max"], -c["keyword_count"], -c["year"]))

    # Summary stats
    summary = {
        "total_papers_scanned": all_papers_count,
        "total_candidates": len(candidates),
        "benchmarks": sum(1 for c in candidates if c["candidate_type"] == "benchmark"),
        "datasets": sum(1 for c in candidates if c["candidate_type"] == "dataset"),
        "with_data_url": sum(1 for c in candidates if c["has_data"]),
        "with_mp_above_50": sum(1 for c in candidates if c["mp_max"] >= 50),
        "mp_theory_coverage": {
            theory: sum(1 for c in candidates if c["mp_scores"][theory] >= 50)
            for theory in [
                "mp_mft", "mp_schwartz", "mp_trolley", "mp_kohlberg",
                "mp_dual_process", "mp_intuitionist", "mp_dyadic", "mp_identity",
                "mp_maqasid", "mp_confucian", "mp_ubuntu",
            ]
        },
        "extract_theory_coverage": {
            theory: sum(
                1 for c in candidates
                if c.get("extract_theory_hits", {}).get(theory, 0) >= 2
            )
            for theory in ["maqasid", "confucian", "ubuntu", "buddhist", "indigenous"]
        },
        "year_range": {
            "min": min((c["year"] for c in candidates if c["year"]), default=0),
            "max": max((c["year"] for c in candidates if c["year"]), default=0),
        },
        "extraction_date": datetime.now().strftime("%Y-%m-%d"),
    }

    output = {
        "summary": summary,
        "candidates": candidates,
    }

    date_prefix = datetime.now().strftime("%Y%m%d")
    output_path = OUTPUT_DIR / f"{date_prefix}-moral-psych-benchmark-candidates.json"
    output_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Scanned {all_papers_count} papers")
    print(f"Found {len(candidates)} candidates:")
    print(f"  - Benchmarks: {summary['benchmarks']}")
    print(f"  - Datasets: {summary['datasets']}")
    print(f"  - With DATA_URL: {summary['with_data_url']}")
    print(f"  - With mp_* >= 50: {summary['with_mp_above_50']}")
    print(f"\nTheory coverage (papers with mp_* >= 50):")
    for theory, count in summary["mp_theory_coverage"].items():
        print(f"  {theory}: {count}")
    print(f"\nExtract-based non-Western theory coverage (>=2 pattern hits):")
    for theory, count in summary["extract_theory_coverage"].items():
        print(f"  {theory}: {count}")
    print(f"\nOutput: {output_path}")


if __name__ == "__main__":
    main()
