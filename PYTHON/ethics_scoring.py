#!/usr/bin/env python3
"""
Ethics Confidence Scoring Engine for CEI Literature Vault

Replaces binary Yes/No ethics classification with 0-100 confidence scores.
All keyword lists consolidated here as the canonical source.

Scoring formula per field:
    score = strong_matches * 15 + medium_matches * 5 - fp_context * 10 + title_bonus
    clamped to [0, 100]

Threshold: score >= 50 treated as old "Yes".

Source of keyword lists: review_normative_audit.py lines 34-146.
"""

import json
import re
import sys
from pathlib import Path

# ── Path setup ───────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(_SCRIPT_DIR))
sys.path.insert(0, str(_SCRIPT_DIR.parent / ".agent" / "lib"))

from config import PAPERS_DIR, PDF_EXTRACTS_DIR, STATISTICS_DIR

# =====================================================================
# KEYWORD TIERS — Canonical source for all ethics classification
# =====================================================================

# ── VIRTUE ETHICS ────────────────────────────────────────────────────

VIRTUE_STRONG = [
    r"\bvirtue ethics\b", r"\bvirtue-ethics\b", r"\bvirtue ethicist\w*\b",
    r"\beudaimonia\b", r"\bphronesis\b", r"\barete\b",
    r"\baristotelian ethics\b", r"\baristotelian virtue\b",
    r"\bmoral character\b", r"\bmoral virtue\b",
    r"\bvirtue-based\b", r"\bvirtue theory\b",
    r"\bcharacter ethics\b",
    r"\bpractical wisdom\b",
    r"\bmoral exemplar\w*\b",
    r"\bhuman flourishing\b",
    r"\btelos\b",
]

VIRTUE_MEDIUM = [
    r"\bvirtues?\b", r"\bvirtuous\b", r"\bflourishing\b",
    r"\bexcellence\b", r"\baristotel\w*\b",
    r"\bprudence\b", r"\btemperance\b",
    r"\bmoral development\b",
    r"\bmoral education\b",
]

VIRTUE_FP = [
    r"\bvirtual\b", r"\bcharacter recognition\b", r"\bcharacter encoding\b",
    r"\bcharacter set\b", r"\bcharacter level\b", r"\bcharacter-level\b",
    r"\bcharacter embed\w*\b", r"\bunicode character\b",
    r"\bexcellence in\s+(?:research|teaching|service)\b",
    r"\bcenter\w* of excellence\b",
    r"\bexcellence\s+(?:award|program|initiative)\b",
]

# ── DEONTOLOGICAL ETHICS ────────────────────────────────────────────

DEONT_STRONG = [
    r"\bdeontolog\w*\b", r"\bkantian ethics\b", r"\bkantian moral\b",
    r"\bcategorical imperative\b", r"\bduty-based\b", r"\brights-based ethics\b",
    r"\brossian\b", r"\bprima facie dut\w*\b",
    r"\bmoral law\b", r"\bmoral rules?\b(?=.*(?:binding|absolute|universal))",
    r"\bkant'?s?\s+(?:ethics|moral|categorical|theory|philosophy)\b",
    r"\bkingdom of ends\b",
    r"\buniversalizability\b",
    r"\brespect for persons\b",
    r"\bmoral autonomy\b",
]

DEONT_MEDIUM = [
    r"\bkant\b", r"\bduty\b", r"\bduties\b", r"\bobligation\b",
    r"\bmoral principles?\b", r"\bmoral duty\b",
    r"\bimperative\b", r"\brule-based\b",
    r"\buniversal\w* law\b", r"\bintrinsic\w* wrong\b",
]

DEONT_FP = [
    r"\brule-based\s+(?:system|model|approach|method|classifier|extraction|reasoning)\b",
    r"\bduty\s+(?:cycle|officer|station|roster)\b",
    r"\bobligation\s+(?:bond|debt|financial)\b",
    r"\b(?:contractual|legal|regulatory|statutory|fiduciary|tax)\s+obligation\b",
    r"\bimperative\s+(?:programming|mood|sentence|form)\b",
    r"\bit is imperative\b", r"\bimperative to\b", r"\bimperative that\b",
    r"\b(?:strategic|business|economic|commercial|operational)\s+imperative\b",
]

# ── UTILITARIAN ETHICS ───────────────────────────────────────────────

UTIL_STRONG = [
    r"\butilitarian\w*\b", r"\bconsequentialis\w*\b",
    r"\bgreatest good\b", r"\bgreatest happiness\b", r"\bgreatest number\b",
    r"\bhedonic calculus\b", r"\bbentham\b", r"\bsidgwick\b",
    r"\bmill'?s?\s+(?:utilitarianism|ethics|moral|principle)\b",
    r"\bharm reduction\b(?=.*(?:ethic|moral|utilitarian))",
    r"\bcost-benefit\s+(?:analysis|framework)\b(?=.*(?:ethic|moral))",
    r"\boutcome-based ethics\b",
    r"\bact utilitarianism\b",
    r"\brule utilitarianism\b",
    r"\bpreference utilitarian\w*\b",
    r"\beffective altruism\b",
    r"\baggregate welfare\b",
]

UTIL_MEDIUM = [
    r"\butility\b", r"\bmaximize?\b", r"\bwelfare\b",
    r"\bwell-being\b", r"\bwellbeing\b", r"\bbeneficence\b",
    r"\bnet benefit\b", r"\bcost-benefit\b", r"\bhedonism\b",
    r"\bmill\b",
]

UTIL_FP = [
    r"\butility\s+(?:function|value|score|measure|class|method|library|tool|software|computing)\b",
    r"\bmaximize\s+(?:accuracy|performance|likelihood|profit|reward|return|score|f1|auc|precision|recall|throughput|efficiency)\b",
    r"\bmaximise\s+(?:accuracy|performance|likelihood|profit|reward|return|score)\b",
    r"\bmaximize?\s+(?:the\s+)?(?:objective|loss|log|function|output|margin|entropy)\b",
    r"\bmaximise?\s+(?:the\s+)?(?:objective|loss|log|function|output|margin|entropy)\b",
    r"\bmill\s+(?:creek|valley|river|road|street)\b",
    r"\bpaper mill\b", r"\bsaw ?mill\b", r"\btextile mill\b",
    r"\bwindmill\b", r"\bwatermill\b",
    r"\bmill\s+et\s+al\b",
    r"\bmill\s*[\(,]\s*\d{4}",
    r"\bmills\b",
]

# ── CARE ETHICS ─────────────────────────────────────────────────────

CARE_STRONG = [
    r"\bcare ethics\b", r"\bethics of care\b", r"\bcaring ethic\w*\b",
    r"\bgilligan\b", r"\bnoddings\b",
    r"\bheld\b(?=.*(?:care|ethic|feminist))",
    r"\bslote\b(?=.*(?:care|ethic|moral))",
    r"\brelational ethics\b", r"\bfeminist ethics\b",
]

CARE_MEDIUM = [
    r"\bempathy\b", r"\bcaregiving\b", r"\bcare\s+robot\b",
    r"\bcompassion\b", r"\brelational\b(?=.*(?:moral|ethic))",
    r"\binterdependence\b",
]

CARE_FP = [
    r"\bhealthcare\b", r"\bcare\s+(?:of|for)\s+(?:the\s+)?(?:data|model|system|patient)\b",
    r"\btake care\b", r"\bcareful\w*\b",
]

# ── CONTRACTARIAN ETHICS ────────────────────────────────────────────

CONTRACT_STRONG = [
    r"\bsocial contract\b", r"\bcontractarian\w*\b", r"\bcontractualis\w*\b",
    r"\brawlsian\b", r"\bjustice as fairness\b", r"\bveil of ignorance\b",
    r"\boriginal position\b",
    r"\bscanlon\b(?=.*(?:contract|moral|ethic|reason))",
    r"\bdistributive justice\b",
]

CONTRACT_MEDIUM = [
    r"\brawls\b", r"\bsocial justice\b",
    r"\bfair\s+(?:distribution|allocation)\b",
    r"\bmaximin\b", r"\bdifference principle\b",
]

CONTRACT_FP = [
    r"\bcontract\s+(?:law|negotiation|management|employee|worker)\b",
    r"\bsmart contract\b", r"\bcontract\s+(?:testing|verification)\b",
]

# ── ETHICS OVERALL ───────────────────────────────────────────────────

ETHICS_STRONG = [
    r"\bai ethics\b", r"\barthificial intelligence ethics\b",
    r"\bmachine ethics\b", r"\brobot ethics\b", r"\broboethics\b",
    r"\bethical ai\b", r"\bresponsible ai\b",
    r"\balgorithmic fairness\b", r"\balgorithmic bias\b",
    r"\balgorithmic discrimination\b", r"\balgorithmic justice\b",
    r"\bethical\s+(?:implications?|considerations?|issues?|challenges?|concerns?|dilemmas?|frameworks?|guidelines?|principles?)\b",
    r"\bmoral\s+(?:reasoning|judgment|decision|dilemma|status|agency|patient|consideration)\b",
    r"\bhuman rights\b(?=.*(?:ai|algorithm|automat|digital|technolog))",
    r"\btrolley problem\b", r"\bmoral foundations\b",
    r"\bvalue alignment\b", r"\bai alignment\b", r"\bai safety\b",
    r"\bfairness\b(?=.*(?:machine learning|algorithm|classif|predict|model|bias))",
    r"\bbias\b(?=.*(?:fairness|discriminat|protected|demographic|racial|gender|ethic))",
    r"\bhate speech\b", r"\btoxic\w*\b(?=.*(?:detect|classif|model|nlp|language))",
    r"\boffensive\s+(?:language|speech|content|text)\b",
    r"\bstereotype\w*\b(?=.*(?:bias|fairness|nlp|language model|gender|racial))",
    r"\bdiscrimination\b(?=.*(?:algorithm|ai|automat|model|fairness))",
    r"\baccountab\w*\b(?=.*(?:ai|algorithm|automat|system))",
    r"\btransparency\b(?=.*(?:ai|algorithm|model|decision|automat))",
    r"\bexplainab\w*\b(?=.*(?:ai|ethic|fairness|accountab|trust))",
]

ETHICS_FP = [
    r"\bselection bias\b", r"\binductive bias\b", r"\bsampling bias\b",
    r"\bcognitive bias\b(?!.*(?:ethic|moral|fairness))",
    r"\bconfirmation bias\b(?!.*(?:ethic|moral))",
    r"\bstatistical bias\b", r"\bestimation bias\b", r"\bvariance.{0,20}bias\b",
    r"\bbias-variance\b", r"\bregularization bias\b",
    r"\bsafety\s+(?:critical|factor|margin|standard|protocol|test|requirement|system|analysis)\b(?!.*ethic)",
    r"\bfunctional safety\b", r"\bindustrial safety\b",
    r"\bparameter values?\b", r"\bnumerical values?\b", r"\bpixel values?\b",
    r"\bfeature values?\b", r"\bdefault values?\b", r"\breturn values?\b",
    r"\btext alignment\b", r"\bsequence alignment\b", r"\bword alignment\b",
    r"\bimage alignment\b",
]

# ── Title bonus patterns (field-specific) ────────────────────────────

TITLE_PATTERNS = {
    "ethics_overall": re.compile(
        r"\bethic|moral|fairness|bias|responsible ai|ai safety|value alignment"
        r"|hate speech|toxic|discriminat|accountab|stereotyp",
        re.IGNORECASE,
    ),
    "virtue_ethics": re.compile(
        r"\bvirtue|eudaimonia|phronesis|arete|aristotel|flourishing|practical wisdom|moral character",
        re.IGNORECASE,
    ),
    "deontological_ethics": re.compile(
        r"\bdeontolog|kantian|categorical imperative|duty-based|rights-based|universalizability|kingdom of ends|moral autonomy",
        re.IGNORECASE,
    ),
    "utilitarian_ethics": re.compile(
        r"\butilitarian|consequential|greatest good|bentham|sidgwick|effective altruism|aggregate",
        re.IGNORECASE,
    ),
    "care_ethics": re.compile(
        r"\bcare ethics|ethics of care|gilligan|noddings|feminist ethics|relational ethics",
        re.IGNORECASE,
    ),
    "contractarian_ethics": re.compile(
        r"\bcontract|rawls|justice as fairness|veil of ignorance|distributive justice",
        re.IGNORECASE,
    ),
}

# ── Field → keyword-tier mapping ────────────────────────────────────

FIELD_KEYWORDS = {
    "ethics_overall": {
        "strong": ETHICS_STRONG,
        "medium": [],  # ethics_overall has no medium tier — uses strong only
        "fp": ETHICS_FP,
    },
    "virtue_ethics": {
        "strong": VIRTUE_STRONG,
        "medium": VIRTUE_MEDIUM,
        "fp": VIRTUE_FP,
    },
    "deontological_ethics": {
        "strong": DEONT_STRONG,
        "medium": DEONT_MEDIUM,
        "fp": DEONT_FP,
    },
    "utilitarian_ethics": {
        "strong": UTIL_STRONG,
        "medium": UTIL_MEDIUM,
        "fp": UTIL_FP,
    },
}

ETHICS_FIELDS = ["ethics_overall", "virtue_ethics", "deontological_ethics", "utilitarian_ethics"]

DEFAULT_THRESHOLD = 50


# =====================================================================
# LOW-LEVEL HELPERS
# =====================================================================

def count_matches(text, patterns):
    """Count total regex matches in text. Returns (count, matched_terms)."""
    text_lower = text.lower()
    total = 0
    matched_terms = []
    for pat in patterns:
        for m in re.finditer(pat, text_lower):
            total += 1
            matched_terms.append(m.group())
    return total, matched_terms


def load_extract(stem):
    """Load extract body text for a paper (first ~5000 chars, no frontmatter)."""
    for year_dir in sorted(PDF_EXTRACTS_DIR.iterdir()):
        if not year_dir.is_dir():
            continue
        candidate = year_dir / f"{stem}.md"
        if candidate.exists():
            try:
                content = candidate.read_text(encoding="utf-8")
                if content.startswith("---"):
                    end = content.find("---", 3)
                    if end != -1:
                        content = content[end + 3:]
                return content[:10000]
            except Exception:
                return ""
    return ""


# =====================================================================
# SCORING ENGINE
# =====================================================================

def compute_score(text, title, field):
    """
    Compute a 0-100 confidence score for a given ethics field.

    Formula:
        strong_matches * 15 + medium_matches * 5 - fp_context * 10 + title_bonus
        Clamped to [0, 100].

    Args:
        text: Combined abstract + extract text.
        title: Paper title (checked for bonus).
        field: One of ETHICS_FIELDS.

    Returns:
        int: 0-100 confidence score.
    """
    kw = FIELD_KEYWORDS[field]

    strong_count, _ = count_matches(text, kw["strong"])
    medium_count, _ = count_matches(text, kw["medium"])
    fp_count, _ = count_matches(text, kw["fp"])

    # Title bonus: +20 if title contains relevant terms
    title_bonus = 0
    if title and TITLE_PATTERNS[field].search(title):
        title_bonus = 20

    raw = strong_count * 15 + medium_count * 5 - fp_count * 10 + title_bonus

    return max(0, min(100, raw))


def compute_all_scores(title, abstract, extract):
    """
    Compute scores for all 4 ethics fields.

    Args:
        title: Paper title.
        abstract: Paper abstract.
        extract: PDF extract text.

    Returns:
        dict: {field: int} for all ETHICS_FIELDS.
    """
    text = f"{title} {abstract} {extract}"
    scores = {field: compute_score(text, title, field) for field in ETHICS_FIELDS}

    # Co-occurrence boost: if 2+ normative ethics fields each have ≥1 strong match,
    # all matched fields should score ≥ 50. Targets multi-framework papers (surveys,
    # benchmarks, comparative studies) where keyword hits are diluted across frameworks.
    ne_fields = ["virtue_ethics", "deontological_ethics", "utilitarian_ethics"]
    ne_strong = []
    for field in ne_fields:
        kw = FIELD_KEYWORDS[field]
        count, _ = count_matches(text, kw["strong"])
        if count >= 1:
            ne_strong.append(field)

    if len(ne_strong) >= 2:
        for field in ne_strong:
            scores[field] = max(scores[field], 50)

    return scores


# =====================================================================
# BACKWARD COMPATIBILITY
# =====================================================================

def parse_ethics_value(raw):
    """
    Convert any legacy or new ethics value to an integer score.

    Handles:
        "Yes" / "yes"  → 80  (high but not pinned)
        "No" / "no"    → 0
        "Unknown" / ""  → 0
        int / str(int)  → int
        None            → 0
    """
    if raw is None:
        return 0
    if isinstance(raw, int):
        return raw
    if isinstance(raw, float):
        return int(raw)

    s = str(raw).strip().strip('"').strip("'").lower()

    if s == "yes":
        return 80
    if s in ("no", "unknown", "n/a", ""):
        return 0

    # Try numeric
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return int(float(s))
    except ValueError:
        return 0


def is_ethics_yes(raw, threshold=DEFAULT_THRESHOLD):
    """
    Backward-compatible binary check.

    Returns True if the parsed score >= threshold.
    Works with both legacy "Yes"/"No" and new integer scores.
    """
    return parse_ethics_value(raw) >= threshold


# =====================================================================
# USER-REVIEWED PINS
# =====================================================================

# Pinned scores from Tier 1 normative audit (user-reviewed decisions).
# Papers in the decisions list had specific fields confirmed as false positives → score 5.
# The specific fields NOT flagged in those papers were implicitly confirmed → score 95.
_USER_PINS = {}  # populated by _load_user_pins()
_PINS_LOADED = False


def _load_user_pins():
    """Load user-reviewed pin data from Tier 1 decisions JSON."""
    global _USER_PINS, _PINS_LOADED
    if _PINS_LOADED:
        return

    tier1_path = STATISTICS_DIR / "20260312-normative-audit-tier1-decisions.json"
    if not tier1_path.exists():
        _PINS_LOADED = True
        return

    try:
        with open(tier1_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        _PINS_LOADED = True
        return

    for dec in data.get("decisions", []):
        filename = dec.get("filename", "")
        changes = dec.get("changes", {})
        if not filename:
            continue

        if filename not in _USER_PINS:
            _USER_PINS[filename] = {}

        # Fields that were changed to "No" = confirmed false positives → pin at 5
        for field, new_val in changes.items():
            if new_val == "No":
                _USER_PINS[filename][field] = 5

    _PINS_LOADED = True


def get_pinned_score(filename, field):
    """
    Return pinned score if user reviewed this paper+field, else None.

    Confirmed false positive → 5
    """
    _load_user_pins()
    pins = _USER_PINS.get(filename, {})
    return pins.get(field)


# =====================================================================
# SAFE YAML WRITE HELPER
# =====================================================================

def safe_yaml_set_int(frontmatter_text, field, value):
    """
    Replace a YAML field value with an unquoted integer using safe regex.

    Per CLAUDE.md rule #2: re.subn() with count=1, re.MULTILINE.
    Returns (new_frontmatter, was_replaced).
    """
    pattern = rf'^{re.escape(field)}:.*$'
    replacement = f'{field}: {int(value)}'
    new_fm, count = re.subn(pattern, replacement, frontmatter_text, count=1, flags=re.MULTILINE)
    return new_fm, count > 0


# =====================================================================
# CONVENIENCE: FULL PAPER SCORING
# =====================================================================

def score_paper(filename, title, abstract, extract=""):
    """
    Score a paper across all ethics fields, respecting user pins.

    Args:
        filename: Paper filename (e.g., "2024-Smith-Example.md") for pin lookup.
        title: Paper title.
        abstract: Paper abstract.
        extract: PDF extract text (optional, loaded if empty).

    Returns:
        dict: {field: int} for all ETHICS_FIELDS.
    """
    if not extract:
        stem = Path(filename).stem
        extract = load_extract(stem)

    scores = compute_all_scores(title, abstract, extract)

    # Apply user pins (override algorithm)
    for field in ETHICS_FIELDS:
        pinned = get_pinned_score(filename, field)
        if pinned is not None:
            scores[field] = pinned

    return scores
