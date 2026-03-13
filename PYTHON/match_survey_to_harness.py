#!/usr/bin/env python3
"""Match benchmark survey entries to lm-eval-harness task aliases.

Agent 3 (Survey Matcher) in the 10-agent swarm.
Reads the 986-entry benchmark survey JSON and cross-references benchmark_names
against known lm-eval-harness tasks using fuzzy matching.
"""

from __future__ import annotations

import json
import re
import string
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Tuple

# ── Known harness task aliases ──────────────────────────────────────────────

HARNESS_ALIASES = {
    "bbq": ["bbq", "bias benchmark for qa", "bias benchmark for question answering"],
    "truthfulqa": ["truthfulqa", "truthful qa"],
    "toxigen": ["toxigen"],
    "crows_pairs": ["crows-pairs", "crows pairs", "crowspairs"],
    "ethics_cm": ["ethics", "hendrycks ethics", "ethics commonsense"],
    "ethics_deontology": ["ethics deontology"],
    "ethics_justice": ["ethics justice"],
    "ethics_utilitarianism": ["ethics utilitarianism"],
    "ethics_virtue": ["ethics virtue"],
    "bold": ["bold", "bias in open-ended language generation"],
    "realtoxicityprompts": ["realtoxicityprompts", "real toxicity prompts"],
    "winogender": ["winogender"],
    "winobias": ["winobias"],
    "mmlu_moral_scenarios": ["mmlu moral scenarios", "moral scenarios"],
    "mmlu_moral_disputes": ["mmlu moral disputes", "moral disputes"],
    "mmlu_business_ethics": ["mmlu business ethics", "business ethics"],
    "hatecheck": ["hatecheck"],
    "social_iqa": ["social iqa", "socialiqa"],
    "jiminy_cricket": ["jiminy cricket", "what would jiminy cricket do"],
    "weat": ["weat", "word embedding association test"],
    "equity_evaluation_corpus": ["eec", "equity evaluation corpus"],
    "stereoset": ["stereoset"],
    "seat": ["seat", "sentence encoder association test"],
    "regard": ["regard"],
    "honest": ["honest"],
    "holistic_bias": ["holistic bias"],
    "discrim_eval": ["discrim-eval"],
    "xstest": ["xstest"],
    "machiavelli": ["machiavelli"],
    "moral_machine": ["moral machine"],
}

# Words to strip during normalization
STRIP_WORDS = {"benchmark", "dataset", "test"}


def normalize(text: str) -> str:
    """Lowercase, strip punctuation, remove filler words."""
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Remove strip words
    tokens = text.split()
    tokens = [t for t in tokens if t not in STRIP_WORDS]
    return " ".join(tokens).strip()


def match_benchmark(benchmark_name: str) -> tuple[str | None, str]:
    """Try to match a benchmark_name to a harness task.

    Returns (harness_key, match_method) or (None, "none").
    """
    norm = normalize(benchmark_name)

    # Pass 1: exact match against any alias
    for key, aliases in HARNESS_ALIASES.items():
        for alias in aliases:
            if norm == normalize(alias):
                return key, "exact"

    # Pass 2: substring — alias is substring of benchmark_name or vice versa
    # For short aliases (<=4 chars), require word-boundary match to avoid
    # false positives like "eec" matching "speech"
    norm_tokens = set(norm.split())
    for key, aliases in HARNESS_ALIASES.items():
        for alias in aliases:
            norm_alias = normalize(alias)
            if len(norm_alias) <= 4:
                # Short alias: must appear as a whole word/token
                if norm_alias in norm_tokens:
                    return key, "substring"
            elif len(norm_alias) >= 3 and norm_alias in norm:
                return key, "substring"
            if len(norm) >= 3 and norm in norm_alias:
                return key, "substring"

    return None, "none"


def main():
    ws = Path(__file__).resolve().parent.parent  # CEI-Lit-WS/
    input_path = ws / "logs" / "20260216-benchmark_survey_candidates.json"
    output_path = ws / "logs" / "20260312-harness-matches.json"

    with open(input_path) as f:
        survey = json.load(f)

    entries = []
    availability_counts: dict[str, int] = {}

    for item in survey:
        benchmark_name = item.get("benchmark_name", "")
        harness_key, method = match_benchmark(benchmark_name)

        avail = item.get("availability", "Unknown")
        availability_counts[avail] = availability_counts.get(avail, 0) + 1

        entry = {
            "filename": item.get("filename", ""),
            "benchmark_name": benchmark_name,
            "harness_match": harness_key,
            "match_method": method,
            "availability": avail,
            "dataset_size": item.get("dataset_size", ""),
            "what_measures": item.get("what_measures", ""),
            "how_measures": item.get("how_measures", ""),
        }
        entries.append(entry)

    matched = [e for e in entries if e["harness_match"] is not None]
    unmatched = [e for e in entries if e["harness_match"] is None]

    result = {
        "agent": "survey_matcher",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "count": len(matched),
        "summary": {
            "total_survey_entries": len(survey),
            "matched_to_harness": len(matched),
            "unmatched": len(unmatched),
            "availability_breakdown": dict(
                sorted(availability_counts.items(), key=lambda x: -x[1])
            ),
        },
        "entries": entries,
    }

    with open(output_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Total survey entries: {len(survey)}")
    print(f"Matched to harness:   {len(matched)}")
    print(f"Unmatched:            {len(unmatched)}")
    print(f"Availability breakdown:")
    for k, v in sorted(availability_counts.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    print(f"\nOutput written to: {output_path}")

    # Show matched harness tasks
    harness_hits: dict[str, int] = {}
    for e in matched:
        k = e["harness_match"]
        harness_hits[k] = harness_hits.get(k, 0) + 1
    print(f"\nHarness tasks matched ({len(harness_hits)} unique):")
    for k, v in sorted(harness_hits.items(), key=lambda x: -x[1]):
        m = [e for e in matched if e["harness_match"] == k]
        methods = set(e["match_method"] for e in m)
        print(f"  {k}: {v} paper(s) [{', '.join(methods)}]")


if __name__ == "__main__":
    main()
