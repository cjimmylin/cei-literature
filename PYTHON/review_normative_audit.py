#!/usr/bin/env python3
"""
Deep-analysis review of Tier 2 and Tier 3 normative audit papers.

For each paper, performs contextual analysis beyond simple keyword matching:
- Checks if keywords appear in meaningful ethics-discussion contexts
- Distinguishes incidental keyword usage from substantive framework discussion
- Applies false-positive filters for ambiguous terms
- Produces decisions JSON files ready for apply_normative_audit_decisions.py

Usage:
    python review_normative_audit.py --tier 2
    python review_normative_audit.py --tier 3
    python review_normative_audit.py --tier 2 --verbose

Output:
    STATISTICS/20260312-normative-audit-tier{N}-decisions.json
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent / ".agent" / "lib"))

from yaml_utils import extract_frontmatter, parse_frontmatter
from config import PAPERS_DIR, PDF_EXTRACTS_DIR, STATISTICS_DIR
from ethics_scoring import (
    VIRTUE_STRONG, VIRTUE_MEDIUM, VIRTUE_FP,
    DEONT_STRONG, DEONT_MEDIUM, DEONT_FP,
    UTIL_STRONG, UTIL_MEDIUM, UTIL_FP,
    ETHICS_STRONG, ETHICS_FP,
    count_matches, load_extract, is_ethics_yes,
)

# Map old local names to imported names for backward compatibility
VIRTUE_FP_CONTEXT = VIRTUE_FP
DEONT_FP_CONTEXT = DEONT_FP
UTIL_FP_CONTEXT = UTIL_FP
ETHICS_FP_CONTEXT = ETHICS_FP


def has_any_match(text, patterns):
    """Check if any pattern matches."""
    text_lower = text.lower()
    for pat in patterns:
        if re.search(pat, text_lower):
            return True
    return False


def analyze_virtue(title, abstract, extract):
    """Determine if paper should be tagged virtue_ethics=Yes."""
    combined = f"{title} {abstract} {extract}"

    # Check false-positive contexts first
    fp_count, _ = count_matches(combined, VIRTUE_FP_CONTEXT)

    # Strong indicators — one match is enough
    strong_count, strong_terms = count_matches(combined, VIRTUE_STRONG)
    if strong_count >= 1:
        return True, f"strong: {', '.join(set(strong_terms))}"

    # Medium indicators — need 2+ matches in ethics context
    med_count, med_terms = count_matches(combined, VIRTUE_MEDIUM)
    if med_count >= 2 and fp_count == 0:
        # Check if in ethics context
        if has_any_match(combined, [r"\bethic", r"\bmoral", r"\bnormative"]):
            return True, f"medium ({med_count}): {', '.join(set(med_terms))}"

    return False, ""


def analyze_deont(title, abstract, extract):
    """Determine if paper should be tagged deontological_ethics=Yes."""
    combined = f"{title} {abstract} {extract}"

    fp_count, _ = count_matches(combined, DEONT_FP_CONTEXT)

    strong_count, strong_terms = count_matches(combined, DEONT_STRONG)
    if strong_count >= 1:
        return True, f"strong: {', '.join(set(strong_terms))}"

    med_count, med_terms = count_matches(combined, DEONT_MEDIUM)
    if med_count >= 2 and fp_count == 0:
        if has_any_match(combined, [r"\bethic", r"\bmoral", r"\bnormative"]):
            return True, f"medium ({med_count}): {', '.join(set(med_terms))}"

    return False, ""


def analyze_util(title, abstract, extract):
    """Determine if paper should be tagged utilitarian_ethics=Yes."""
    combined = f"{title} {abstract} {extract}"

    fp_count, fp_terms = count_matches(combined, UTIL_FP_CONTEXT)

    strong_count, strong_terms = count_matches(combined, UTIL_STRONG)
    if strong_count >= 1 and fp_count == 0:
        return True, f"strong: {', '.join(set(strong_terms))}"

    # For utilitarian, even strong terms can be FP (e.g., "utility function" in ML)
    # If we have strong AND FP context, reject
    if strong_count >= 1 and fp_count >= 1:
        # Only accept if strong terms are clearly ethical
        ethical_strong = [t for t in strong_terms if t in (
            "utilitarianism", "consequentialism", "consequentialist",
            "greatest good", "greatest happiness", "bentham", "sidgwick"
        )]
        if ethical_strong:
            return True, f"strong (with FP context): {', '.join(set(ethical_strong))}"
        return False, ""

    med_count, med_terms = count_matches(combined, UTIL_MEDIUM)
    if med_count >= 3 and fp_count == 0:
        if has_any_match(combined, [r"\bethic", r"\bmoral", r"\bnormative"]):
            return True, f"medium ({med_count}): {', '.join(set(med_terms))}"

    return False, ""


def analyze_ethics_overall(title, abstract, extract):
    """Determine if paper should be tagged ethics_overall=Yes (for Tier 3)."""
    combined = f"{title} {abstract} {extract}"

    # Check for false-positive contexts
    fp_count, _ = count_matches(combined, ETHICS_FP_CONTEXT)

    # Strong ethics indicators
    strong_count, strong_terms = count_matches(combined, ETHICS_STRONG)

    # Title-based: if title contains clear ethics terms, very strong signal
    title_lower = title.lower()
    title_ethics = bool(re.search(
        r"\bethic|moral|fairness|bias|responsible ai|ai safety|value alignment|hate speech|toxic|discriminat|accountab|stereotyp",
        title_lower
    ))

    if title_ethics and strong_count >= 1:
        return True, f"title + strong ({strong_count}): {', '.join(set(strong_terms[:5]))}"

    if strong_count >= 3:
        return True, f"strong ({strong_count}): {', '.join(set(strong_terms[:5]))}"

    if strong_count >= 2 and fp_count == 0:
        return True, f"strong ({strong_count}, no FP): {', '.join(set(strong_terms[:5]))}"

    # If only FP-context matches, keep as No
    if strong_count <= 1 and fp_count >= 2:
        return False, f"FP context dominant ({fp_count} FP vs {strong_count} strong)"

    return False, ""


def load_all_papers():
    """Load all papers and return list of dicts."""
    papers = []
    for path in sorted(PAPERS_DIR.iterdir()):
        if not path.is_file() or path.suffix != ".md":
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            continue
        try:
            fm_text, body = extract_frontmatter(content)
        except Exception:
            continue

        fields = parse_frontmatter(fm_text)
        abstract = fields.get("abstract", "").strip().strip('"').strip("'")

        papers.append({
            "filename": path.name,
            "stem": path.stem,
            "year": fields.get("year", ""),
            "title": fields.get("short_title", path.stem).strip('"').strip("'"),
            "abstract": abstract,
            "ethics_overall": fields.get("ethics_overall", "").strip('"'),
            "virtue_ethics": fields.get("virtue_ethics", "").strip('"'),
            "deontological_ethics": fields.get("deontological_ethics", "").strip('"'),
            "utilitarian_ethics": fields.get("utilitarian_ethics", "").strip('"'),
            "ethics_perspective": fields.get("ethics_perspective", "").strip('"'),
        })
    return papers


# Normative keywords for pre-filtering (same as generate script)
NORMATIVE_KEYWORDS = [
    r"\bdeontolog\w*\b", r"\bkantian\b", r"\bcategorical imperative\b",
    r"\bduty-based\b", r"\brights-based\b", r"\brossian\b",
    r"\bprima facie dut\w*\b", r"\butilitarian\w*\b", r"\bconsequentialis\w*\b",
    r"\bbentham\b", r"\bsidgwick\b", r"\bgreatest good\b", r"\bhedonic calculus\b",
    r"\bvirtue ethic\w*\b", r"\baristotel\w*\b", r"\beudaimonia\b", r"\bphronesis\b",
    r"\bcare ethic\w*\b", r"\bnormative ethic\w*\b", r"\bnormative framework\b",
    r"\bnormative theor\w*\b", r"\bmoral theor\w*\b", r"\bethical theor\w*\b",
    r"\bmoral philosophy\b",
]

ETHICS_OVERALL_KEYWORDS = [
    r'\bethics?\b', r'\bethical\b', r'\bmoral\b', r'\bmorality\b', r'\bvalues?\b',
    r'\bnormative\b', r'\bfairness\b', r'\bjustice\b', r'\bbias\b', r'\bharm\b',
    r'\bsafety\b', r'\balignment\b', r'\bresponsible\b', r'\baccountable\b',
    r'\bhate speech\b', r'\btoxic\b', r'\boffensive\b', r'\babusive\b',
    r'\bstereotype\b', r'\bdiscrimination\b', r'\bhuman rights\b',
    r'\bprosocial\b', r'\bimmoral\b', r'\bunethical\b', r'\bwrongdoing\b',
    r'\bmoral reasoning\b', r'\bmoral judgment\b', r'\bmoral decision\b',
    r'\bmoral dilemma\b', r'\btrolley problem\b', r'\bmoral foundations\b',
]

HIGH_YIELD_PERSPECTIVES = {
    "Moral Reasoning & Psychology", "Machine Ethics", "Applied Ethics", "General Ethics",
}


def filter_tier2(papers):
    """Tier 2: ethics=Yes, all frameworks=No, keyword-filtered."""
    candidates = [
        p for p in papers
        if is_ethics_yes(p["ethics_overall"])
        and not is_ethics_yes(p["virtue_ethics"])
        and not is_ethics_yes(p["deontological_ethics"])
        and not is_ethics_yes(p["utilitarian_ethics"])
    ]
    result = []
    for p in candidates:
        extract = load_extract(p["stem"])
        text = f"{p['abstract']} {extract}"
        norm_count, _ = count_matches(text, NORMATIVE_KEYWORDS)
        has_perspective = p["ethics_perspective"] in HIGH_YIELD_PERSPECTIVES
        if norm_count > 0 or has_perspective:
            p["_extract"] = extract
            result.append(p)
    return result


def filter_tier3(papers):
    """Tier 3: ethics=No, keyword-filtered."""
    candidates = [p for p in papers if not is_ethics_yes(p["ethics_overall"])]
    result = []
    for p in candidates:
        extract = load_extract(p["stem"])
        text = f"{p['abstract']} {extract}"
        ethics_count, _ = count_matches(text, ETHICS_OVERALL_KEYWORDS)
        norm_count, _ = count_matches(text, NORMATIVE_KEYWORDS)
        if ethics_count > 0 or norm_count > 0:
            p["_extract"] = extract
            result.append(p)
    return result


def filter_tier1(papers):
    """Tier 1: any framework = Yes."""
    return [
        p for p in papers
        if is_ethics_yes(p["virtue_ethics"])
        or is_ethics_yes(p["deontological_ethics"])
        or is_ethics_yes(p["utilitarian_ethics"])
    ]


def is_false_positive_virtue(title, abstract, extract):
    """Check if virtue_ethics=Yes is a false positive."""
    combined = f"{title} {abstract} {extract}"
    # A paper currently tagged virtue=Yes is a false positive if:
    # 1. No strong virtue indicators at all
    # 2. Only weak/ambiguous terms (character, excellence, courage, wisdom)
    #    in non-ethics contexts
    strong_count, strong_terms = count_matches(combined, VIRTUE_STRONG)
    if strong_count >= 1:
        return False, ""  # Not a false positive

    # Check medium indicators
    med_count, med_terms = count_matches(combined, VIRTUE_MEDIUM)
    fp_count, fp_terms = count_matches(combined, VIRTUE_FP_CONTEXT)

    # If ONLY FP contexts for the keywords, it's a false positive
    if fp_count > 0 and med_count <= fp_count:
        return True, f"FP context: {', '.join(set(fp_terms[:3]))}"

    # Check if the paper is about ethics at all
    ethics_context = has_any_match(combined, [r"\bethic", r"\bmoral", r"\bnormative", r"\bvirtue"])
    if not ethics_context and med_count <= 1:
        return True, f"no ethics context, weak match: {', '.join(set(med_terms[:3]))}"

    return False, ""


def is_false_positive_deont(title, abstract, extract):
    """Check if deontological_ethics=Yes is a false positive."""
    combined = f"{title} {abstract} {extract}"
    strong_count, strong_terms = count_matches(combined, DEONT_STRONG)
    if strong_count >= 1:
        return False, ""

    med_count, med_terms = count_matches(combined, DEONT_MEDIUM)
    fp_count, fp_terms = count_matches(combined, DEONT_FP_CONTEXT)

    # If paper discusses ethics/moral topics substantively, FP context alone
    # shouldn't override — "imperative to" in an ethics paper may coexist
    # with genuine deontological discussion
    ethics_context = has_any_match(combined, [r"\bethic", r"\bmoral", r"\bnormative", r"\bdeontolog",
                                              r"\brights-based\b", r"\bduty-based\b", r"\bmachine ethics\b"])

    if fp_count > 0 and med_count <= fp_count and not ethics_context:
        return True, f"FP context: {', '.join(set(fp_terms[:3]))}"

    if not ethics_context and med_count <= 1:
        return True, f"no ethics context, weak match: {', '.join(set(med_terms[:3]))}"

    return False, ""


def is_false_positive_util(title, abstract, extract):
    """Check if utilitarian_ethics=Yes is a false positive."""
    combined = f"{title} {abstract} {extract}"
    strong_count, strong_terms = count_matches(combined, UTIL_STRONG)

    # Check FP context even for strong terms (utility function is very common in ML)
    fp_count, fp_terms = count_matches(combined, UTIL_FP_CONTEXT)

    # If all strong terms are actually FP (e.g., "utility function", "maximize accuracy")
    if strong_count > 0 and fp_count >= strong_count:
        # Check if there are ALSO clearly ethical strong terms
        ethical_strong = [t for t in strong_terms if t in (
            "utilitarianism", "consequentialism", "consequentialist",
            "greatest good", "greatest happiness", "bentham", "sidgwick",
            "utilitarian ethics",
        )]
        if not ethical_strong:
            return True, f"FP context ({fp_count}): {', '.join(set(fp_terms[:3]))}"

    if strong_count == 0:
        med_count, med_terms = count_matches(combined, UTIL_MEDIUM)
        if fp_count > 0 and med_count <= fp_count:
            return True, f"FP context: {', '.join(set(fp_terms[:3]))}"

        ethics_context = has_any_match(combined, [r"\bethic", r"\bmoral", r"\bnormative", r"\butilitarian"])
        if not ethics_context and med_count <= 1:
            return True, f"no ethics context, weak match: {', '.join(set(med_terms[:3]))}"

    return False, ""


def review_tier1(papers, verbose=False):
    """Review Tier 1 papers: check for false positives in existing framework tags."""
    filtered = filter_tier1(papers)
    print(f"Tier 1: {len(filtered)} papers to review for false positives")

    decisions = []
    stats = {"virtue_fp": 0, "deont_fp": 0, "util_fp": 0, "any_change": 0}

    for i, p in enumerate(filtered):
        if (i + 1) % 50 == 0:
            print(f"  Reviewing {i+1}/{len(filtered)}...")

        title = p["title"]
        abstract = p["abstract"]
        extract = load_extract(p["stem"])

        changes = {}
        notes = []

        if is_ethics_yes(p["virtue_ethics"]):
            is_fp, reason = is_false_positive_virtue(title, abstract, extract)
            if is_fp:
                changes["virtue_ethics"] = "No"
                notes.append(f"V-FP: {reason}")
                stats["virtue_fp"] += 1

        if is_ethics_yes(p["deontological_ethics"]):
            is_fp, reason = is_false_positive_deont(title, abstract, extract)
            if is_fp:
                changes["deontological_ethics"] = "No"
                notes.append(f"D-FP: {reason}")
                stats["deont_fp"] += 1

        if is_ethics_yes(p["utilitarian_ethics"]):
            is_fp, reason = is_false_positive_util(title, abstract, extract)
            if is_fp:
                changes["utilitarian_ethics"] = "No"
                notes.append(f"U-FP: {reason}")
                stats["util_fp"] += 1

        if changes:
            stats["any_change"] += 1
            note = "; ".join(notes)
            decisions.append({
                "filename": p["filename"],
                "changes": changes,
                "note": note,
            })
            if verbose:
                print(f"  FALSE POSITIVE: {p['filename']}")
                print(f"    {note}")

    print(f"\nTier 1 results:")
    print(f"  Papers with false positives: {stats['any_change']}")
    print(f"  Virtue false positives: {stats['virtue_fp']}")
    print(f"  Deontological false positives: {stats['deont_fp']}")
    print(f"  Utilitarian false positives: {stats['util_fp']}")

    return decisions


def review_tier2(papers, verbose=False):
    """Review Tier 2 papers: should any framework be tagged Yes?"""
    filtered = filter_tier2(papers)
    print(f"Tier 2: {len(filtered)} papers to review")

    decisions = []
    stats = {"virtue": 0, "deont": 0, "util": 0, "any_change": 0}

    for i, p in enumerate(filtered):
        if (i + 1) % 25 == 0:
            print(f"  Reviewing {i+1}/{len(filtered)}...")

        title = p["title"]
        abstract = p["abstract"]
        extract = p.get("_extract", "")

        changes = {}
        notes = []

        v_yes, v_reason = analyze_virtue(title, abstract, extract)
        if v_yes:
            changes["virtue_ethics"] = "Yes"
            notes.append(f"V: {v_reason}")
            stats["virtue"] += 1

        d_yes, d_reason = analyze_deont(title, abstract, extract)
        if d_yes:
            changes["deontological_ethics"] = "Yes"
            notes.append(f"D: {d_reason}")
            stats["deont"] += 1

        u_yes, u_reason = analyze_util(title, abstract, extract)
        if u_yes:
            changes["utilitarian_ethics"] = "Yes"
            notes.append(f"U: {u_reason}")
            stats["util"] += 1

        if changes:
            stats["any_change"] += 1
            note = "; ".join(notes)
            decisions.append({
                "filename": p["filename"],
                "changes": changes,
                "note": note,
            })
            if verbose:
                print(f"  CHANGE: {p['filename']}")
                print(f"    {note}")

    print(f"\nTier 2 results:")
    print(f"  Papers with changes: {stats['any_change']}")
    print(f"  Virtue tags added: {stats['virtue']}")
    print(f"  Deontological tags added: {stats['deont']}")
    print(f"  Utilitarian tags added: {stats['util']}")

    return decisions


def review_tier3(papers, verbose=False):
    """Review Tier 3 papers: should ethics_overall or frameworks change?"""
    filtered = filter_tier3(papers)
    print(f"Tier 3: {len(filtered)} papers to review")

    decisions = []
    stats = {"ethics_overall": 0, "virtue": 0, "deont": 0, "util": 0, "any_change": 0}

    for i, p in enumerate(filtered):
        if (i + 1) % 25 == 0:
            print(f"  Reviewing {i+1}/{len(filtered)}...")

        title = p["title"]
        abstract = p["abstract"]
        extract = p.get("_extract", "")

        changes = {}
        notes = []

        # First check ethics_overall
        e_yes, e_reason = analyze_ethics_overall(title, abstract, extract)
        if e_yes:
            changes["ethics_overall"] = "Yes"
            notes.append(f"E: {e_reason}")
            stats["ethics_overall"] += 1

            # Also check frameworks if ethics_overall changes
            v_yes, v_reason = analyze_virtue(title, abstract, extract)
            if v_yes:
                changes["virtue_ethics"] = "Yes"
                notes.append(f"V: {v_reason}")
                stats["virtue"] += 1

            d_yes, d_reason = analyze_deont(title, abstract, extract)
            if d_yes:
                changes["deontological_ethics"] = "Yes"
                notes.append(f"D: {d_reason}")
                stats["deont"] += 1

            u_yes, u_reason = analyze_util(title, abstract, extract)
            if u_yes:
                changes["utilitarian_ethics"] = "Yes"
                notes.append(f"U: {u_reason}")
                stats["util"] += 1

        if changes:
            stats["any_change"] += 1
            note = "; ".join(notes)
            decisions.append({
                "filename": p["filename"],
                "changes": changes,
                "note": note,
            })
            if verbose:
                print(f"  CHANGE: {p['filename']}")
                print(f"    {note}")

    print(f"\nTier 3 results:")
    print(f"  Papers with changes: {stats['any_change']}")
    print(f"  Ethics overall flipped: {stats['ethics_overall']}")
    print(f"  Virtue tags added: {stats['virtue']}")
    print(f"  Deontological tags added: {stats['deont']}")
    print(f"  Utilitarian tags added: {stats['util']}")

    return decisions


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Review normative audit papers")
    parser.add_argument("--tier", type=int, required=True, choices=[1, 2, 3])
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    print(f"Loading papers from {PAPERS_DIR}...")
    papers = load_all_papers()
    print(f"  Loaded {len(papers)} papers\n")

    if args.tier == 1:
        decisions_list = review_tier1(papers, args.verbose)
    elif args.tier == 2:
        decisions_list = review_tier2(papers, args.verbose)
    else:
        decisions_list = review_tier3(papers, args.verbose)

    output = {
        "audit_tier": f"tier{args.tier}",
        "audit_date": "2026-03-12",
        "decisions": decisions_list,
    }

    STATISTICS_DIR.mkdir(exist_ok=True)
    out_path = STATISTICS_DIR / f"20260312-normative-audit-tier{args.tier}-decisions.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nDecisions written to: {out_path}")
    print(f"  Total decisions: {len(decisions_list)}")


if __name__ == "__main__":
    main()
