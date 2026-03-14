#!/usr/bin/env python3
"""
Classify papers by Moral Psychological Perspectives (Score-based).

Uses moral_psych_scoring.py to compute 0-100 confidence scores for 8 theories:
  mp_mft, mp_schwartz, mp_trolley, mp_kohlberg,
  mp_dual_process, mp_intuitionist, mp_dyadic, mp_identity

Also writes a derived moral_psychology string from scores >= threshold.

YAML safety: uses re.subn() with count=1, flags=re.MULTILINE — no parse->rebuild.
"""

import functools
import os
import re
import sys
from pathlib import Path
from typing import Dict, Tuple

print = functools.partial(print, flush=True)

# ── Path setup ───────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(_SCRIPT_DIR))
sys.path.insert(0, str(_SCRIPT_DIR.parent / ".agent" / "lib"))

from moral_psych_scoring import (
    compute_all_mp_scores, derive_moral_psychology_string,
    MP_FIELDS, FIELD_DISPLAY_NAMES, DEFAULT_THRESHOLD,
    score_paper_mp,
    insert_mp_fields_before_moral_psychology,
    update_existing_mp_fields,
)
from ethics_scoring import safe_yaml_set_int, load_extract
from yaml_utils import extract_frontmatter, parse_frontmatter, validate_frontmatter
from config import PAPERS_DIR
from insight_logger import InsightLogger

# =====================================================================
# LEGACY PATTERNS — kept for reference only. Scoring is now handled
# by moral_psych_scoring.FIELD_KEYWORDS with strong/medium/fp tiers.
# =====================================================================
#
# PSYCH_PATTERNS = {
#     "Moral Foundations Theory": [
#         r"\bMoral Foundations\b", r"\bMFT\b", r"\bHaidt\b", r"\bGraham\b",
#         r"\b5 foundations\b", r"\bcare/harm\b", r"\bsanctity/degradation\b",
#         r"\bliberty/oppression\b", r"\bloyalty/betrayal\b", r"\bauthority/subversion\b",
#         r"\bMFQ\b", r"\bMFTC\b"
#     ],
#     "Dual Process Theory": [
#         r"\bDual Process\b", r"\bJoshua Greene\b", r"\bfast and slow\b",
#         r"\bcognitive vs emotional\b", r"\butilitarian vs deontological processing\b",
#         r"\bmanual mode\b", r"\bautomatic settings\b"
#     ],
#     "Dyadic Morality": [
#         r"\bDyadic Morality\b", r"\bTheory of Dyadic Morality\b", r"\bKurt Gray\b",
#         r"\bmoral typecasting\b", r"\bagent and patient\b", r"\bdyad\b"
#     ],
#     "Social Intuitionist": [
#         r"\bSocial Intuitionist\b", r"\bSIM\b", r"\bintuitive judgment\b",
#         r"\breasoning comes second\b", r"\bmoral dumbfounding\b"
#     ],
#     "Moral Identity": [
#         r"\bMoral Identity\b", r"\bself-importance of moral identity\b",
#         r"\bAquino\b", r"\bReed\b"
#     ],
#     "Cognitive Developmental": [
#         r"\bKohlberg\b", r"\bPiaget\b", r"\bstages of moral development\b",
#         r"\bpre-conventional\b", r"\bpost-conventional\b",
#         r"\bconventional level\b", r"\bHeinz dilemma\b",
#         r"\bRest\b", r"\bDefining Issues Test\b", r"\bDIT\b"
#     ],
#     "Value Pluralism / Schwartz": [
#         r"\bSchwartz Theory\b", r"\bBasic Human Values\b", r"\bSchwartz Values\b",
#         r"\bValue Pluralism\b", r"\bUniversalism\b", r"\bBenevolence\b",
#         r"\bSelf-Direction\b", r"\bStimulation\b", r"\bHedonism\b",
#         r"\bAchievement\b", r"\bPower\b", r"\bSecurity\b", r"\bConformity\b",
#         r"\bTradition\b"
#     ],
#     "Trolley / Dilemmas (Psych)": [
#         r"\bTrolley problem\b", r"\bMoral Machine\b", r"\bsacrificial dilemma\b",
#         r"\bfootbridge problem\b", r"\bswitch problem\b"
#     ]
# }


def update_frontmatter_with_scores(fm_text: str, scores: Dict[str, int]) -> str:
    """
    Write mp_* score fields and derived moral_psychology string into frontmatter.

    If mp_* fields already exist, update them via safe_yaml_set_int.
    If they don't exist, insert them before moral_psychology: line.

    Uses regex-based replacement only (CLAUDE.md rule #2).
    """
    # Check if mp_* fields already exist
    has_mp_fields = re.search(r'^mp_mft:', fm_text, re.MULTILINE) is not None

    if has_mp_fields:
        return update_existing_mp_fields(fm_text, scores)
    else:
        # Check if moral_psychology: line exists
        has_mp_line = re.search(r'^moral_psychology:', fm_text, re.MULTILINE) is not None
        if has_mp_line:
            new_fm, success = insert_mp_fields_before_moral_psychology(fm_text, scores)
            if success:
                return new_fm

        # moral_psychology: line doesn't exist — append everything at end
        derived = derive_moral_psychology_string(scores)
        mp_lines = []
        for field in MP_FIELDS:
            mp_lines.append("{}: {}".format(field, int(scores.get(field, 0))))
        mp_lines.append('moral_psychology: "{}"'.format(derived))
        return fm_text.rstrip() + "\n" + "\n".join(mp_lines)


def process_paper(filepath: Path, ilog: InsightLogger = None) -> Tuple[str, str, Dict[str, int]]:
    """
    Process a single paper file: compute mp_* scores and write them.

    Returns (filename, moral_psychology_string, scores_dict).
    """
    content = filepath.read_text(encoding="utf-8")
    fm_text, body = extract_frontmatter(content)

    # Capture old mp_* values before scoring
    old_scores = {}
    if ilog:
        for field in MP_FIELDS:
            match = re.search(rf'^{re.escape(field)}:\s*(\d+)', fm_text, re.MULTILINE)
            if match:
                old_scores[field] = int(match.group(1))

    title_match = re.search(r'^short_title:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ''

    abstract_match = re.search(r'^abstract:\s*["\']?(.*?)["\']?\s*$', fm_text, re.MULTILINE)
    abstract = abstract_match.group(1).strip() if abstract_match else ''

    # Compute scores via scoring module
    scores = score_paper_mp(filepath.name, title, abstract)

    # Log reclassifications and disagreements
    if ilog:
        for field in MP_FIELDS:
            if field in old_scores:
                old_val = old_scores[field]
                new_val = scores.get(field, 0)
                if old_val < DEFAULT_THRESHOLD <= new_val:
                    ilog.reclassification(filepath.name, field, old_val, new_val)
                elif new_val < DEFAULT_THRESHOLD <= old_val:
                    ilog.reclassification(filepath.name, field, old_val, new_val,
                                          "{} dropped below threshold: {} -> {}".format(field, old_val, new_val))
                elif abs(new_val - old_val) > 20:
                    ilog.disagreement(filepath.name, field, old_val, new_val)

    # Update frontmatter with mp_* fields + derived moral_psychology
    new_fm = update_frontmatter_with_scores(fm_text, scores)

    # Validate YAML before writing
    is_valid, issues = validate_frontmatter(new_fm)
    if not is_valid:
        print("  Warning: YAML validation issues in {}: {}".format(filepath.name, issues))

    # Atomic write
    reconstructed = "---\n{}\n---\n{}".format(new_fm.rstrip(), body)
    tmp_path = filepath.parent / ".tmp.{}.{}".format(os.getpid(), filepath.name)
    tmp_path.write_text(reconstructed, encoding="utf-8")
    os.replace(str(tmp_path), str(filepath))

    derived = derive_moral_psychology_string(scores)
    return filepath.name, derived, scores


def main():
    """Process all papers and generate summary."""
    ilog = InsightLogger("classify_moral_psych")

    papers = list(PAPERS_DIR.glob("*.md"))
    print("Found {} papers to process\n".format(len(papers)))

    # Per-theory score distribution tracking
    theory_score_bins = {field: {"0": 0, "1-49": 0, "50-79": 0, "80-100": 0}
                         for field in MP_FIELDS}
    psych_counts = {}
    results = []

    for paper in sorted(papers):
        try:
            name, moral_psych, scores = process_paper(paper, ilog)
            results.append((name, moral_psych, scores))

            # Track per-theory bins
            for field in MP_FIELDS:
                s = scores.get(field, 0)
                if s == 0:
                    theory_score_bins[field]["0"] += 1
                elif s < DEFAULT_THRESHOLD:
                    theory_score_bins[field]["1-49"] += 1
                elif s < 80:
                    theory_score_bins[field]["50-79"] += 1
                else:
                    theory_score_bins[field]["80-100"] += 1

            if moral_psych != "N/A":
                for p in moral_psych.split(", "):
                    psych_counts[p] = psych_counts.get(p, 0) + 1
            else:
                psych_counts["N/A"] = psych_counts.get("N/A", 0) + 1

        except Exception as e:
            print("Error processing {}: {}".format(paper.name, e))

    # Print summary
    print("=" * 60)
    print("MORAL PSYCHOLOGY CLASSIFICATION SUMMARY")
    print("=" * 60)
    for theory, count in sorted(psych_counts.items(), key=lambda x: -x[1]):
        print("  {}: {}".format(theory, count))

    # Per-theory score distributions
    print("\n" + "=" * 60)
    print("SCORE DISTRIBUTIONS BY THEORY")
    print("=" * 60)
    print("  {:30s} {:>6s} {:>6s} {:>6s} {:>6s}".format(
        "Theory", "0", "1-49", "50-79", "80+"))
    print("  " + "-" * 56)
    for field in MP_FIELDS:
        bins = theory_score_bins[field]
        display = FIELD_DISPLAY_NAMES[field]
        print("  {:30s} {:>6d} {:>6d} {:>6d} {:>6d}".format(
            display, bins["0"], bins["1-49"], bins["50-79"], bins["80-100"]))

    # Print papers with classifications (non-N/A)
    print("\n" + "=" * 60)
    print("PAPERS WITH IDENTIFIED MORAL PSYCHOLOGY")
    print("=" * 60)
    psych_papers = [(n, p, s) for n, p, s in results if p != "N/A"]
    for name, moral_psych, scores in sorted(psych_papers):
        print("  {}".format(name))
        print("    Theory: {}".format(moral_psych))
        detected = {f: v for f, v in scores.items() if v >= DEFAULT_THRESHOLD}
        if detected:
            score_strs = ["{}: {}".format(FIELD_DISPLAY_NAMES[f], v)
                          for f, v in detected.items()]
            print("    Scores: {}".format(", ".join(score_strs)))

    print("\n\nTotal papers processed: {}".format(len(results)))
    print("Papers with identified psychology: {}".format(len(psych_papers)))

    # Log summary stats
    ilog.stat("Processed {} papers, {} with identified psychology".format(
        len(results), len(psych_papers)))
    for field in MP_FIELDS:
        bins = theory_score_bins[field]
        display = FIELD_DISPLAY_NAMES[field]
        above = bins["50-79"] + bins["80-100"]
        ilog.stat("{}: {} papers >= 50".format(display, above),
                  {"bins": bins})

    ilog.finalize()


if __name__ == "__main__":
    main()
