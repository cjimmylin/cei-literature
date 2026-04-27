#!/usr/bin/env python3
"""
Moral Psychology Confidence Scoring Engine for CEI Literature Vault

Replaces flat comma-separated moral_psychology string with 8 individual
0-100 confidence scores (mp_mft, mp_schwartz, mp_trolley, mp_kohlberg,
mp_dual_process, mp_intuitionist, mp_dyadic, mp_identity).

Scoring formula per theory:
    score = strong_matches * 15 + medium_matches * 5 - fp_context * 10 + title_bonus
    clamped to [0, 100]

Threshold: score >= 50 treated as detected.

Reuses count_matches, load_extract, safe_yaml_set_int from ethics_scoring.py.
"""

import re
import sys
from pathlib import Path

# ── Path setup ───────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(_SCRIPT_DIR))
sys.path.insert(0, str(_SCRIPT_DIR.parent / ".agent" / "lib"))

from ethics_scoring import count_matches, load_extract, safe_yaml_set_int

# =====================================================================
# KEYWORD TIERS — Canonical source for moral psychology classification
# =====================================================================

# ── MFT (Moral Foundations Theory) ──────────────────────────────────

MFT_STRONG = [
    r"\bmoral foundations\b", r"\bmft\b", r"\bmfq\b", r"\bmftc\b",
    r"\bcare/harm\b", r"\bcare[\s/]harm\b",
    r"\bsanctity/degradation\b", r"\bsanctity[\s/]degradation\b",
    r"\bloyalty/betrayal\b", r"\bloyalty[\s/]betrayal\b",
    r"\bauthority/subversion\b", r"\bauthority[\s/]subversion\b",
    r"\bliberty/oppression\b", r"\bliberty[\s/]oppression\b",
    r"\bfairness/cheating\b", r"\bfairness[\s/]cheating\b",
    r"\bbinding foundation\b", r"\bindividualizing foundation\b",
]

MFT_MEDIUM = [
    r"\bhaidt\b(?=.*\bmoral\b)",
    r"\bgraham\b(?=.*\b(?:moral|foundation)\b)",
    r"\bfive foundations\b", r"\bfoundations of morality\b",
]

MFT_FP = [
    r"\bgraham\b(?!.*\b(?:moral|foundation|haidt)\b)",
    r"\bresearch foundation\b", r"\bnational (?:science )?foundation\b",
    r"\bfoundation model\b",
]

# ── VALUE PLURALISM / SCHWARTZ ──────────────────────────────────────

SCHWARTZ_STRONG = [
    r"\bschwartz(?:'s)? theory\b", r"\bschwartz(?:'s)? values?\b",
    r"\bbasic human values\b", r"\bvalue pluralism\b",
    r"\bsvs\b", r"\bpvq\b", r"\bportrait values questionnaire\b",
    r"\bshalom schwartz\b",
]

SCHWARTZ_MEDIUM = [
    r"\bschwartz\b(?=.*\b(?:theor|value|pluralism|svs|pvq)\b)",
    r"\buniversalism\b(?=.*\bvalue\b)",
    r"\bbenevolence\b(?=.*\bvalue\b)",
    r"\bself-direction\b(?=.*\bvalue\b)",
]

SCHWARTZ_FP = [
    r"\bachievement\b(?!.*\bschwartz\b)(?!.*\bvalue pluralism\b)(?!.*\bbasic human values\b)",
    r"\bpower\b(?!.*\bschwartz\b)(?!.*\bvalue pluralism\b)(?!.*\bbasic human values\b)",
    r"\bsecurity\b(?!.*\bschwartz\b)(?!.*\bvalue pluralism\b)(?!.*\bbasic human values\b)",
    r"\bconformity\b(?!.*\bschwartz\b)(?!.*\bvalue pluralism\b)",
    r"\btradition\b(?!.*\bschwartz\b)(?!.*\bvalue pluralism\b)",
]

# ── TROLLEY / DILEMMAS (PSYCH) ──────────────────────────────────────

TROLLEY_STRONG = [
    r"\btrolley problem\b", r"\btrolley dilemma\b",
    r"\bmoral machine\b", r"\bfootbridge problem\b",
    r"\bsacrificial dilemma\b", r"\bswitch problem\b",
]

TROLLEY_MEDIUM = [
    r"\bmoral dilemma\b(?=.*\bexperiment\b)",
    r"\bautonomous vehicle\b(?=.*\bmoral\b)",
]

TROLLEY_FP = [
    r"\bdilemma\b(?!.*\b(?:trolley|moral|sacrific|footbridge)\b)",
]

# ── COGNITIVE DEVELOPMENTAL (KOHLBERG) ──────────────────────────────

KOHLBERG_STRONG = [
    r"\bkohlberg\b", r"\bstages of moral development\b",
    r"\bheinz dilemma\b", r"\bdefining issues test\b",
    r"\bpre-conventional\b", r"\bpost-conventional\b",
]

KOHLBERG_MEDIUM = [
    r"\bpiaget\b(?=.*\bmoral\b)",
    r"\bmoral development\b", r"\bmoral stage\b",
    r"\bRest\b(?=.*\b(?:DIT|defining issues|moral development)\b)",
]

KOHLBERG_FP = [
    # "Rest" removed — too common a word (FP magnet)
    # "DIT" needs context — acronym collision
    r"\bdit\b(?!.*\b(?:kohlberg|moral development|defining issues)\b)",
    r"\bconventional\b(?!.*\b(?:kohlberg|moral|pre-conventional|post-conventional)\b)",
]

# ── DUAL PROCESS THEORY ─────────────────────────────────────────────

DUAL_PROCESS_STRONG = [
    r"\bdual process\b(?=.*\bmoral\b)",
    r"\bjoshua greene\b",
    r"\butilitarian vs deontological processing\b",
    r"\bsystem 1.*system 2\b",
    r"\bsystem 2.*system 1\b",
    # Expanded: Greene's key constructs
    r"\butilitarian vs\.? deontological\b(?=.*\b(?:judg|reason|dilemma|moral)\b)",
    r"\bcognitive load\b(?=.*\bmoral\b)",
    r"\bpersonal force\b(?=.*\b(?:moral|dilemma)\b)",
    r"\bpersonal vs\.? impersonal\b(?=.*\bdilemma\b)",
    r"\bgreene\b(?=.*\bmoral\b)",
    r"\baffect\b(?=.*\bcognition\b)(?=.*\bmoral\b)",
    r"\bresponse time\b(?=.*\bmoral\b)",
]

DUAL_PROCESS_MEDIUM = [
    r"\bdual process\b",
    r"\bfast and slow\b(?=.*\bmoral\b)",
    r"\bautomatic.*deliberat\w*\b(?=.*\bmoral\b)",
    # Expanded: broader indicators
    r"\bautomatic\b(?=.*\bmoral\b)(?=.*\b(?:judg|reason|process)\b)",
    r"\bdeliberat\w+\b(?=.*\bmoral\b)(?=.*\b(?:judg|reason|process)\b)",
    r"\bsystem 1\b(?=.*\b(?:moral|intuiti|dilemma)\b)",
    r"\bsystem 2\b(?=.*\b(?:moral|deliberat|dilemma)\b)",
    r"\beffortful\b(?=.*\bmoral\b)",
    r"\bemotional response\b(?=.*\b(?:utilitarian|deontological)\b)",
]

DUAL_PROCESS_FP = [
    r"\bdual process\b(?=.*\b(?:cognitive science|memory|attention|perception)\b)(?!.*\bmoral\b)",
    r"\bfast and slow\b(?!.*\bmoral\b)",
    r"\bautomatic\b(?!.*\b(?:moral|ethic|dilemma|utilitarian|deontological)\b)",
]

# ── SOCIAL INTUITIONIST MODEL ───────────────────────────────────────

INTUITIONIST_STRONG = [
    r"\bsocial intuitionist\b",
    r"\bmoral dumbfounding\b",
    r"\breasoning comes second\b",
    # Expanded: Haidt + context, emotion-first framing
    r"\bhaidt\b(?=.*\b(?:intuit|moral|foundation|dumbfound)\b)",
    r"\bpost[- ]hoc rationali[sz]\w+\b(?=.*\bmoral\b)",
    r"\bgut feeling\b(?=.*\bmoral\b)",
    r"\bemotion[- ]first\b(?=.*\bmoral\b)",
    r"\bmoral heuristic\b",
    r"\bmoral sentiment\b(?=.*\b(?:judgment|intuiti|reason)\b)",
]

INTUITIONIST_MEDIUM = [
    r"\bmoral intuition\b",
    r"\bintuitive judgment\b(?=.*\bmoral\b)",
    # Expanded: broader intuitionist indicators
    r"\bmoral sentiment\b",
    r"\bhumean\b(?=.*\bmoral\b)",
    r"\bsentimentalism\b(?=.*\b(?:moral|ethic)\b)",
    r"\bintuitive\b(?=.*\bmoral\b)(?=.*\b(?:judg|reason|response)\b)",
    r"\baffect\b(?=.*\breason\w*\b)(?=.*\bmoral\b)",
]

INTUITIONIST_FP = [
    # "SIM" removed entirely — SIM cards, simulations, too many FPs
    r"\bintuition\b(?!.*\b(?:moral|intuitionist|dumbfounding|judgment|sentiment|ethic)\b)",
    r"\bsentiment\b(?!.*\b(?:moral|ethic|intuitionist|humean)\b)",
]

# ── DYADIC MORALITY ─────────────────────────────────────────────────

DYADIC_STRONG = [
    r"\bdyadic morality\b",
    r"\bkurt gray\b",
    r"\bmoral typecasting\b",
    # Expanded: Gray & Schein constructs
    r"\bharm perception\b(?=.*\b(?:moral|agent|patient)\b)",
    r"\bschein\b(?=.*\b(?:moral|dyadic|gray|typecasting)\b)",
    r"\bagent[- ]patient\b(?=.*\bharm\b)",
    r"\btheory of dyadic morality\b",
]

DYADIC_MEDIUM = [
    r"\bmoral dyad\b",
    r"\bagent and patient\b(?=.*\bmoral\b)",
    # Expanded: broader dyadic indicators
    r"\bmoral patient\b",
    r"\bmoral agent\b(?=.*\bpatient\b)",
    r"\bcomplete moral dyad\b",
    r"\bharm[- ]based moral\w*\b",
    r"\bgray\b(?=.*\bschein\b)(?=.*\bmoral\b)",
]

DYADIC_FP = [
    r"\bdyad\b(?!.*\b(?:moral|typecasting|kurt gray|harm|agent|patient)\b)",
    r"\bpatient\b(?!.*\b(?:moral|agent|dyad|typecasting|harm)\b)",
]

# ── MORAL IDENTITY ──────────────────────────────────────────────────

IDENTITY_STRONG = [
    r"\bmoral identity\b",
    r"\bself-importance of moral identity\b",
    r"\bmoral self-concept\b",
    r"\bmoral exemplar\b",
]

IDENTITY_MEDIUM = [
    r"\baquino\b(?=.*\bmoral\b)",
    r"\bmoral character\b",
]

IDENTITY_FP = [
    # "Reed" removed — too common a surname
    r"\bidentity\b(?!.*\b(?:moral|self-concept|exemplar)\b)",
]


# ── Title bonus patterns (per theory) ────────────────────────────────

TITLE_PATTERNS = {
    "mp_mft": re.compile(
        r"\bmoral foundations?\b|MFT|MFQ|MFTC|care.harm|loyalty.betrayal",
        re.IGNORECASE,
    ),
    "mp_schwartz": re.compile(
        r"\bschwartz\b|basic human values|value pluralism|SVS|PVQ",
        re.IGNORECASE,
    ),
    "mp_trolley": re.compile(
        r"\btrolley\b|moral machine|footbridge|sacrificial dilemma",
        re.IGNORECASE,
    ),
    "mp_kohlberg": re.compile(
        r"\bkohlberg\b|moral development|heinz dilemma|defining issues",
        re.IGNORECASE,
    ),
    "mp_dual_process": re.compile(
        r"\bdual process\b|joshua greene|utilitarian vs\.? deontological"
        r"|cognitive load.*moral|personal force.*dilemma|system 1.*system 2",
        re.IGNORECASE,
    ),
    "mp_intuitionist": re.compile(
        r"\bsocial intuitionist\b|moral dumbfounding|reasoning comes second"
        r"|moral intuition|moral sentiment|moral heuristic|haidt.*intuit",
        re.IGNORECASE,
    ),
    "mp_dyadic": re.compile(
        r"\bdyadic morality\b|kurt gray|moral typecasting"
        r"|harm perception.*moral|agent.*patient.*harm|moral dyad",
        re.IGNORECASE,
    ),
    "mp_identity": re.compile(
        r"\bmoral identity\b|moral self-concept|moral exemplar",
        re.IGNORECASE,
    ),
}

# ── Field → keyword-tier mapping ────────────────────────────────────

FIELD_KEYWORDS = {
    "mp_mft": {
        "strong": MFT_STRONG,
        "medium": MFT_MEDIUM,
        "fp": MFT_FP,
    },
    "mp_schwartz": {
        "strong": SCHWARTZ_STRONG,
        "medium": SCHWARTZ_MEDIUM,
        "fp": SCHWARTZ_FP,
    },
    "mp_trolley": {
        "strong": TROLLEY_STRONG,
        "medium": TROLLEY_MEDIUM,
        "fp": TROLLEY_FP,
    },
    "mp_kohlberg": {
        "strong": KOHLBERG_STRONG,
        "medium": KOHLBERG_MEDIUM,
        "fp": KOHLBERG_FP,
    },
    "mp_dual_process": {
        "strong": DUAL_PROCESS_STRONG,
        "medium": DUAL_PROCESS_MEDIUM,
        "fp": DUAL_PROCESS_FP,
    },
    "mp_intuitionist": {
        "strong": INTUITIONIST_STRONG,
        "medium": INTUITIONIST_MEDIUM,
        "fp": INTUITIONIST_FP,
    },
    "mp_dyadic": {
        "strong": DYADIC_STRONG,
        "medium": DYADIC_MEDIUM,
        "fp": DYADIC_FP,
    },
    "mp_identity": {
        "strong": IDENTITY_STRONG,
        "medium": IDENTITY_MEDIUM,
        "fp": IDENTITY_FP,
    },
}

MP_FIELDS = [
    "mp_mft", "mp_schwartz", "mp_trolley", "mp_kohlberg",
    "mp_dual_process", "mp_intuitionist", "mp_dyadic", "mp_identity",
]

# Display name mapping: field → human-readable theory name
FIELD_DISPLAY_NAMES = {
    "mp_mft": "Moral Foundations Theory",
    "mp_schwartz": "Value Pluralism / Schwartz",
    "mp_trolley": "Trolley / Dilemmas (Psych)",
    "mp_kohlberg": "Cognitive Developmental",
    "mp_dual_process": "Dual Process Theory",
    "mp_intuitionist": "Social Intuitionist Model",
    "mp_dyadic": "Dyadic Morality",
    "mp_identity": "Moral Identity",
}

# Reverse mapping: display name → field
DISPLAY_NAME_TO_FIELD = {v: k for k, v in FIELD_DISPLAY_NAMES.items()}

# Aliases from consolidate_moral_psych.py — normalize LLM/legacy names
CATEGORY_ALIASES = {
    "Dual Process Theory (Moral Cognition)": "Dual Process Theory",
    "Social Intuitionist": "Social Intuitionist Model",
    "Trolley / Dilemmas": "Trolley / Dilemmas (Psych)",
    "Trolley/Dilemmas (Psych)": "Trolley / Dilemmas (Psych)",
    "Value Pluralism/Schwartz": "Value Pluralism / Schwartz",
    "Schwartz": "Value Pluralism / Schwartz",
    "Kohlberg": "Cognitive Developmental",
}

DEFAULT_THRESHOLD = 50


# =====================================================================
# SCORING ENGINE
# =====================================================================

def compute_mp_score(text, title, field):
    """
    Compute a 0-100 confidence score for a given moral psychology theory.

    Formula:
        strong_matches * 15 + medium_matches * 5 - fp_context * 10 + title_bonus
        Clamped to [0, 100].

    Unlike ethics keywords (broad, many co-occurring terms), moral psychology
    keywords are narrow and highly specific — a single "trolley problem" or
    "Moral Foundations Theory" IS a true positive. Therefore, if any strong
    match is found, a minimum floor of 50 is applied before FP subtraction.

    Args:
        text: Combined title + abstract + extract text.
        title: Paper title (checked for bonus).
        field: One of MP_FIELDS.

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

    # Strong-match floor: moral psych keywords are highly specific,
    # so any strong match guarantees at least threshold score
    if strong_count > 0:
        raw = max(raw, DEFAULT_THRESHOLD)

    return max(0, min(100, raw))


def compute_all_mp_scores(title, abstract, extract):
    """
    Compute scores for all 8 moral psychology theories.

    Args:
        title: Paper title.
        abstract: Paper abstract.
        extract: PDF extract text.

    Returns:
        dict: {field: int} for all MP_FIELDS.
    """
    text = f"{title} {abstract} {extract}"
    return {field: compute_mp_score(text, title, field) for field in MP_FIELDS}


def score_paper_mp(filename, title, abstract, extract=""):
    """
    Score a paper across all moral psychology theories.

    Args:
        filename: Paper filename for extract lookup.
        title: Paper title.
        abstract: Paper abstract.
        extract: PDF extract text (loaded from disk if empty).

    Returns:
        dict: {field: int} for all MP_FIELDS.
    """
    if not extract:
        stem = Path(filename).stem
        extract = load_extract(stem)

    return compute_all_mp_scores(title, abstract, extract)


# =====================================================================
# DERIVED STRING HELPERS
# =====================================================================

def derive_moral_psychology_string(scores, threshold=DEFAULT_THRESHOLD):
    """
    Generate the derived moral_psychology display string from individual scores.

    Returns comma-separated theory names for scores >= threshold, or "N/A".
    """
    detected = []
    for field in MP_FIELDS:
        if scores.get(field, 0) >= threshold:
            detected.append(FIELD_DISPLAY_NAMES[field])

    return ", ".join(detected) if detected else "N/A"


def parse_moral_psychology_string(value):
    """
    Parse a legacy moral_psychology comma-separated string into a list of
    canonical theory names.

    Handles aliases and normalization.
    """
    if not value or value.strip('"').strip("'").strip() in ("N/A", "Unknown", ""):
        return []

    raw = value.strip('"').strip("'")
    categories = [c.strip() for c in raw.split(",")]
    normalized = []
    for cat in categories:
        canonical = CATEGORY_ALIASES.get(cat, cat)
        if canonical not in normalized and canonical != "N/A":
            normalized.append(canonical)
    return normalized


# =====================================================================
# BACKWARD COMPATIBILITY
# =====================================================================

def parse_mp_value(raw):
    """
    Convert any legacy or new mp_* value to an integer score.

    Handles:
        int / str(int) → int
        None / "" / "N/A" → 0
    """
    if raw is None:
        return 0
    if isinstance(raw, int):
        return raw
    if isinstance(raw, float):
        return int(raw)

    s = str(raw).strip().strip('"').strip("'").lower()
    if s in ("n/a", "unknown", ""):
        return 0

    try:
        return int(s)
    except ValueError:
        pass
    try:
        return int(float(s))
    except ValueError:
        return 0


def is_mp_detected(raw, threshold=DEFAULT_THRESHOLD):
    """
    Check if a moral psychology theory is detected (score >= threshold).
    """
    return parse_mp_value(raw) >= threshold


# =====================================================================
# SAFE YAML INSERTION HELPER
# =====================================================================

def insert_mp_fields_before_moral_psychology(fm_text, scores):
    """
    Insert 8 mp_* fields immediately before the moral_psychology: line.

    Also updates the moral_psychology: line with the derived string.

    Uses regex insertion — no parse→rebuild round-trip (CLAUDE.md rule #2).

    Args:
        fm_text: Raw frontmatter text (without --- delimiters).
        scores: dict {field: int} for all MP_FIELDS.

    Returns:
        (new_fm_text, success_bool)
    """
    # Build the insertion block
    mp_lines = []
    for field in MP_FIELDS:
        mp_lines.append(f"{field}: {int(scores.get(field, 0))}")

    mp_block = "\n".join(mp_lines)

    # Derive the new moral_psychology string
    derived = derive_moral_psychology_string(scores)

    # Insert mp_* block before moral_psychology: and update its value
    pattern = r'^moral_psychology:.*$'
    replacement = f'{mp_block}\nmoral_psychology: "{derived}"'
    new_fm, count = re.subn(pattern, replacement, fm_text, count=1, flags=re.MULTILINE)

    return new_fm, count > 0


def update_existing_mp_fields(fm_text, scores):
    """
    Update existing mp_* fields in frontmatter (for re-scoring).

    Also updates the derived moral_psychology: string.

    Args:
        fm_text: Raw frontmatter text (without --- delimiters).
        scores: dict {field: int} for all MP_FIELDS.

    Returns:
        new_fm_text
    """
    new_fm = fm_text
    for field in MP_FIELDS:
        new_fm, _ = safe_yaml_set_int(new_fm, field, scores.get(field, 0))

    # Update derived string
    derived = derive_moral_psychology_string(scores)
    new_fm, _ = re.subn(
        r'^moral_psychology:.*$',
        f'moral_psychology: "{derived}"',
        new_fm, count=1, flags=re.MULTILINE,
    )

    return new_fm
