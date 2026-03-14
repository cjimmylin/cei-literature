#!/usr/bin/env python3
"""
Religious Values Confidence Scoring Engine for CEI Literature Vault

Replaces flat comma-separated religious_values string with 14 individual
0-100 confidence scores (rv_islam, rv_christianity, rv_buddhism, rv_judaism,
rv_hinduism, rv_sikhism, rv_confucianism, rv_taoism, rv_shinto, rv_jainism,
rv_bahai, rv_zoroastrianism, rv_ubuntu, rv_indigenous).

Scoring formula per tradition:
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
# KEYWORD TIERS — Canonical source for religious values classification
# =====================================================================

# ── ISLAM ─────────────────────────────────────────────────────────────
# NOTE: All patterns are lowercase because count_matches() lowercases
# the text before matching (re.finditer without IGNORECASE).

ISLAM_STRONG = [
    r"\bislam\w*\b", r"\bmuslim\w*\b", r"\bquran\b", r"\bqur'an\b", r"\bhadith\b",
    r"\bsharia\b", r"\bfatwa\b", r"\bislamicpcqa\b", r"\bfatwaset\b", r"\bqasina\b",
]

ISLAM_MEDIUM = [
    r"\bsirah\b", r"\bnabawiyah\b", r"\bhajj\b",
    r"\bhalal\b", r"\bharam\b", r"\bmosque\b", r"\bummah\b",
]

ISLAM_FP = []  # Islam/Muslim are unambiguous

# ── CHRISTIANITY ──────────────────────────────────────────────────────

CHRISTIANITY_STRONG = [
    r"\bchristian\w*\b", r"\bbible\b", r"\bbiblical\b",
    r"\bgospel\b", r"\bprotestant\b", r"\bcatholic\b", r"\bevangelical\b",
]

CHRISTIANITY_MEDIUM = [
    r"\bword of god\b",
    r"\bchurch\b(?=.*(?:ethic|moral|value|religio))",
]

CHRISTIANITY_FP = []  # Low risk

# ── BUDDHISM ──────────────────────────────────────────────────────────

BUDDHISM_STRONG = [
    r"\bbuddhis\w*\b",
    r"\bdharmabench\b", r"\bbuddhismeval\b",
    r"\bbodhisattva\b", r"\bfour noble truths\b", r"\beightfold path\b",
]

BUDDHISM_MEDIUM = [
    r"\bkarma\b", r"\bnirvana\b", r"\bsangha\b",
    r"\bfive precepts\b", r"\bpaticcasamuppada\b",
    r"\bdharma\b(?=.*(?:buddh|bodhisattva|sangha|noble|eightfold))",
]

BUDDHISM_FP = [
    r"\bdharma\b(?!.*(?:buddh|bodhisattva|sangha|noble|eightfold))",
    r"\bkarma\b(?=.*(?:reddit|social media|point|score|system))",
]

# ── JUDAISM ───────────────────────────────────────────────────────────

JUDAISM_STRONG = [
    r"\bjewish\b", r"\bjudaism\b", r"\btorah\b", r"\btalmud\w*\b",
    r"\brabbinical\b", r"\bhalakha\b", r"\bmitzvot\b",
]

JUDAISM_MEDIUM = [
    r"\bshabbat\b", r"\bkosher\b", r"\bjewish ethics\b",
]

JUDAISM_FP = []  # Low risk

# ── HINDUISM ──────────────────────────────────────────────────────────

HINDUISM_STRONG = [
    r"\bhindu\w*\b", r"\bvedic\b",
    r"\bbhagavad gita\b", r"\bupanishad\b",
]

HINDUISM_MEDIUM = [
    r"\bdharmic\b", r"\bmoksha\b",
    r"\bahimsa\b(?!.*\bjain\w*\b)",
    r"\bsamsara\b",
]

HINDUISM_FP = [
    r"\batman\b(?!.*(?:hindu|vedic|upanishad|bhagavad|dharmic))",
]

# ── SIKHISM ───────────────────────────────────────────────────────────

SIKHISM_STRONG = [
    r"\bsikh\w*\b", r"\bgurbani\b", r"\bguru granth\b",
    r"\bkhalsa\b", r"\bwaheguru\b",
]

SIKHISM_MEDIUM = [
    r"\bfive ks\b", r"\bsewa\b",
]

SIKHISM_FP = []  # Low risk

# ── CONFUCIANISM ──────────────────────────────────────────────────────

CONFUCIANISM_STRONG = [
    r"\bconfucian\w*\b", r"\bconfucius\b",
    r"\banalects\b", r"\bmencius\b",
]

CONFUCIANISM_MEDIUM = [
    r"\bjunzi\b", r"\bfilial piety\b",
    r"\bren\b(?=.*\byi\b)",
]

CONFUCIANISM_FP = []  # Low risk

# ── TAOISM ────────────────────────────────────────────────────────────

TAOISM_STRONG = [
    r"\btaois\w*\b", r"\bdaois\w*\b",
    r"\btao te ching\b", r"\bdaodejing\b", r"\blaozi\b",
]

TAOISM_MEDIUM = [
    r"\bwu wei\b", r"\bzhuangzi\b", r"\byin[\s-]?yang\b", r"\bziran\b",
]

TAOISM_FP = []  # Low risk

# ── SHINTO ────────────────────────────────────────────────────────────

SHINTO_STRONG = [
    r"\bshinto\w*\b",
]

SHINTO_MEDIUM = [
    r"\bkami\b(?=.*(?:japan|shinto|spirit|sacred))",
    r"\btorii\b", r"\bbushido\b", r"\bpurification ritual\b",
]

SHINTO_FP = [
    r"\bkami\b(?!.*(?:japan|shinto|spirit|sacred))",
]

# ── JAINISM ───────────────────────────────────────────────────────────

JAINISM_STRONG = [
    r"\bjain\w*\b", r"\banekantavada\b",
    r"\bmahavira\b", r"\btirthankara\b",
]

JAINISM_MEDIUM = [
    r"\bahimsa\b(?=.*\bjain\w*\b)",
]

JAINISM_FP = []  # Low risk

# ── BAHA'I ────────────────────────────────────────────────────────────

BAHAI_STRONG = [
    r"\bbaha'i\b", r"\bbahai\b",
]

BAHAI_MEDIUM = []

BAHAI_FP = []

# ── ZOROASTRIANISM ────────────────────────────────────────────────────

ZOROASTRIANISM_STRONG = [
    r"\bzoroastrian\w*\b", r"\bavesta\b", r"\bzarathustra\b",
]

ZOROASTRIANISM_MEDIUM = []

ZOROASTRIANISM_FP = []

# ── UBUNTU PHILOSOPHY ─────────────────────────────────────────────────

UBUNTU_STRONG = [
    r"\bubuntu\b(?!.*(?:linux|operat(?:ing|e)|server|desktop|kernel|install))",
    r"\bafrican ethic\w*\b", r"\bafrican philosophy\b", r"\bafrican moral\b",
]

UBUNTU_MEDIUM = [
    r"\bcommunitarian\b(?=.*\bafrican\b)",
]

UBUNTU_FP = [
    r"\bubuntu\b(?=.*(?:linux|operat(?:ing|e)|server|desktop|kernel|install))",
]

# ── INDIGENOUS SPIRITUALITY ───────────────────────────────────────────

INDIGENOUS_STRONG = [
    r"\bindigenous spiritual\w*\b", r"\bindigenous ethic\w*\b", r"\bindigenous moral\b",
    r"\baboriginal dreaming\b", r"\bdreamtime\b",
    r"\bdata sovereignty\b(?=.*\bindigenous\b)",
    r"\btwo[\s-]?eyed seeing\b",
]

INDIGENOUS_MEDIUM = [
    r"\bindigenous knowledge\b",
    r"\bfirst nations?\b(?=.*\bethic\b)",
    r"\boral tradition\b(?=.*\bethic\b)",
    r"\belder wisdom\b", r"\bsacred land\b",
    r"\bdecoloniz\w+\b(?=.*\bethic\b)",
    r"\bwhakapapa\b", r"\bmana\b(?=.*\btapu\b)",
]

INDIGENOUS_FP = [
    r"\bindigenous\b(?!.*(?:ethic\w*|moral|spiritual|knowledge|data sovereignty|elder|sacred|dreaming|oral tradition|decoloniz))",
]


# ── Title bonus patterns (per tradition) ────────────────────────────

TITLE_PATTERNS = {
    "rv_islam": re.compile(
        r"\b(?:Islam\w*|Muslim\w*|Quran\w*|Qur['\u2019.]?an\w*|Hadith|Sharia\w*|Fatwa\w*|IslamicPCQA|FatwaSet|QASiNa)\b",
        re.IGNORECASE,
    ),
    "rv_christianity": re.compile(
        r"\b(?:Christian\w*|Bible|Biblical|Gospel\w*|Protestant\w*|Catholic\w*|Evangelical\w*)\b",
        re.IGNORECASE,
    ),
    "rv_buddhism": re.compile(
        r"\b(?:Buddhis\w*|Dharma\w*|DharmaBench|BuddhismEval|bodhisattva\w*|Noble Truth|Eightfold)\b",
        re.IGNORECASE,
    ),
    "rv_judaism": re.compile(
        r"\b(?:Jewish|Judaism|Torah\w*|Talmud\w*|Rabbinical|halakha\w*)\b",
        re.IGNORECASE,
    ),
    "rv_hinduism": re.compile(
        r"\b(?:Hindu\w*|Vedic|Bhagavad Gita|Upanishad\w*)\b",
        re.IGNORECASE,
    ),
    "rv_sikhism": re.compile(
        r"\b(?:Sikh\w*|Gurbani|Guru Granth|Khalsa|Waheguru)\b",
        re.IGNORECASE,
    ),
    "rv_confucianism": re.compile(
        r"\b(?:Confucian\w*|Confucius|Analects|Mencius)\b",
        re.IGNORECASE,
    ),
    "rv_taoism": re.compile(
        r"\b(?:Taois\w*|Daois\w*|Tao Te Ching|Daodejing|Laozi)\b",
        re.IGNORECASE,
    ),
    "rv_shinto": re.compile(
        r"\b(?:Shinto\w*)\b",
        re.IGNORECASE,
    ),
    "rv_jainism": re.compile(
        r"\b(?:Jain\w*|anekantavada|Mahavira|Tirthankara)\b",
        re.IGNORECASE,
    ),
    "rv_bahai": re.compile(
        r"\b(?:Baha['\u2019.]?i\w*|Bahai\w*)\b",
        re.IGNORECASE,
    ),
    "rv_zoroastrianism": re.compile(
        r"\b(?:Zoroastrian\w*|Avesta\w*|Zarathustra)\b",
        re.IGNORECASE,
    ),
    "rv_ubuntu": re.compile(
        r"\b(?:Ubuntu)\b(?!.*[Ll]inux)|\b(?:African ethic\w*|African philosophy|African moral\w*)\b",
        re.IGNORECASE,
    ),
    "rv_indigenous": re.compile(
        r"\b(?:Indigenous (?:spiritual\w*|ethic\w*|moral\w*)|Aboriginal dreaming|Dreamtime"
        r"|data sovereignty|two[\s-]?eyed seeing)\b",
        re.IGNORECASE,
    ),
}

# ── Field → keyword-tier mapping ────────────────────────────────────

FIELD_KEYWORDS = {
    "rv_islam": {
        "strong": ISLAM_STRONG,
        "medium": ISLAM_MEDIUM,
        "fp": ISLAM_FP,
    },
    "rv_christianity": {
        "strong": CHRISTIANITY_STRONG,
        "medium": CHRISTIANITY_MEDIUM,
        "fp": CHRISTIANITY_FP,
    },
    "rv_buddhism": {
        "strong": BUDDHISM_STRONG,
        "medium": BUDDHISM_MEDIUM,
        "fp": BUDDHISM_FP,
    },
    "rv_judaism": {
        "strong": JUDAISM_STRONG,
        "medium": JUDAISM_MEDIUM,
        "fp": JUDAISM_FP,
    },
    "rv_hinduism": {
        "strong": HINDUISM_STRONG,
        "medium": HINDUISM_MEDIUM,
        "fp": HINDUISM_FP,
    },
    "rv_sikhism": {
        "strong": SIKHISM_STRONG,
        "medium": SIKHISM_MEDIUM,
        "fp": SIKHISM_FP,
    },
    "rv_confucianism": {
        "strong": CONFUCIANISM_STRONG,
        "medium": CONFUCIANISM_MEDIUM,
        "fp": CONFUCIANISM_FP,
    },
    "rv_taoism": {
        "strong": TAOISM_STRONG,
        "medium": TAOISM_MEDIUM,
        "fp": TAOISM_FP,
    },
    "rv_shinto": {
        "strong": SHINTO_STRONG,
        "medium": SHINTO_MEDIUM,
        "fp": SHINTO_FP,
    },
    "rv_jainism": {
        "strong": JAINISM_STRONG,
        "medium": JAINISM_MEDIUM,
        "fp": JAINISM_FP,
    },
    "rv_bahai": {
        "strong": BAHAI_STRONG,
        "medium": BAHAI_MEDIUM,
        "fp": BAHAI_FP,
    },
    "rv_zoroastrianism": {
        "strong": ZOROASTRIANISM_STRONG,
        "medium": ZOROASTRIANISM_MEDIUM,
        "fp": ZOROASTRIANISM_FP,
    },
    "rv_ubuntu": {
        "strong": UBUNTU_STRONG,
        "medium": UBUNTU_MEDIUM,
        "fp": UBUNTU_FP,
    },
    "rv_indigenous": {
        "strong": INDIGENOUS_STRONG,
        "medium": INDIGENOUS_MEDIUM,
        "fp": INDIGENOUS_FP,
    },
}

RV_FIELDS = [
    "rv_islam", "rv_christianity", "rv_buddhism", "rv_judaism",
    "rv_hinduism", "rv_sikhism", "rv_confucianism", "rv_taoism",
    "rv_shinto", "rv_jainism", "rv_bahai", "rv_zoroastrianism",
    "rv_ubuntu", "rv_indigenous",
]

# Display name mapping: field → human-readable tradition name
FIELD_DISPLAY_NAMES = {
    "rv_islam": "Islam",
    "rv_christianity": "Christianity",
    "rv_buddhism": "Buddhism",
    "rv_judaism": "Judaism",
    "rv_hinduism": "Hinduism",
    "rv_sikhism": "Sikhism",
    "rv_confucianism": "Confucianism",
    "rv_taoism": "Taoism",
    "rv_shinto": "Shinto",
    "rv_jainism": "Jainism",
    "rv_bahai": "Baha'i",
    "rv_zoroastrianism": "Zoroastrianism",
    "rv_ubuntu": "Ubuntu Philosophy",
    "rv_indigenous": "Indigenous Spirituality",
}

# Reverse mapping: display name → field
DISPLAY_NAME_TO_FIELD = {v: k for k, v in FIELD_DISPLAY_NAMES.items()}

# Aliases from legacy/LLM names → canonical display name
TRADITION_ALIASES = {
    "Ubuntu": "Ubuntu Philosophy",
    "Ubuntu philosophy": "Ubuntu Philosophy",
    "Indigenous": "Indigenous Spirituality",
    "Indigenous spirituality": "Indigenous Spirituality",
    "Baha'i": "Baha'i",
    "Bahai": "Baha'i",
    "Tao": "Taoism",
    "Dao": "Taoism",
    "Daoism": "Taoism",
    "Confucian": "Confucianism",
    "Buddhist": "Buddhism",
    "Hindu": "Hinduism",
    "Islamic": "Islam",
    "Zoroastrian": "Zoroastrianism",
    "Jain": "Jainism",
    "Sikh": "Sikhism",
    "Shintoist": "Shinto",
    "Shintoism": "Shinto",
}

DEFAULT_THRESHOLD = 50


# =====================================================================
# SCORING ENGINE
# =====================================================================

def compute_rv_score(text, title, field):
    """
    Compute a 0-100 confidence score for a given religious tradition.

    Formula:
        strong_matches * 15 + medium_matches * 5 - fp_context * 10 + title_bonus
        Clamped to [0, 100].

    Religion names are highly specific — a single "Islam" or "Buddhist" IS a
    true positive. Therefore, if any strong match is found, a minimum floor
    of 50 is applied before FP subtraction.

    Args:
        text: Combined title + abstract + extract text.
        title: Paper title (checked for bonus).
        field: One of RV_FIELDS.

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

    # Strong-match floor: religion names are highly specific,
    # so any strong match guarantees at least threshold score
    if strong_count > 0:
        raw = max(raw, DEFAULT_THRESHOLD)

    return max(0, min(100, raw))


def compute_all_rv_scores(title, abstract, extract):
    """
    Compute scores for all 14 religious traditions.

    Args:
        title: Paper title.
        abstract: Paper abstract.
        extract: PDF extract text.

    Returns:
        dict: {field: int} for all RV_FIELDS.
    """
    text = f"{title} {abstract} {extract}"
    return {field: compute_rv_score(text, title, field) for field in RV_FIELDS}


def score_paper_rv(filename, title, abstract, extract=""):
    """
    Score a paper across all religious traditions.

    Args:
        filename: Paper filename for extract lookup.
        title: Paper title.
        abstract: Paper abstract.
        extract: PDF extract text (loaded from disk if empty).

    Returns:
        dict: {field: int} for all RV_FIELDS.
    """
    if not extract:
        stem = Path(filename).stem
        extract = load_extract(stem)

    return compute_all_rv_scores(title, abstract, extract)


# =====================================================================
# DERIVED STRING HELPERS
# =====================================================================

def derive_religious_values_string(scores, threshold=DEFAULT_THRESHOLD):
    """
    Generate the derived religious_values display string from individual scores.

    Returns the tradition name if exactly 1 detected, "Multiple Religions"
    if 2+ detected, or "N/A" if none detected.
    """
    detected = []
    for field in RV_FIELDS:
        if scores.get(field, 0) >= threshold:
            detected.append(FIELD_DISPLAY_NAMES[field])

    if len(detected) == 0:
        return "N/A"
    if len(detected) == 1:
        return detected[0]
    return "Multiple Religions"


def derive_religious_values_list_string(scores, threshold=DEFAULT_THRESHOLD):
    """
    Generate the derived religious_values_list string from individual scores.

    Returns comma-separated tradition names for all scores >= threshold,
    or "N/A" if none detected.
    """
    detected = []
    for field in RV_FIELDS:
        if scores.get(field, 0) >= threshold:
            detected.append(FIELD_DISPLAY_NAMES[field])

    return ", ".join(detected) if detected else "N/A"


def parse_religious_values_string(value):
    """
    Parse a legacy religious_values comma-separated string into a list of
    canonical tradition names.

    Handles aliases and normalization.
    """
    if not value or str(value).strip('"').strip("'").strip() in ("N/A", "Unknown", ""):
        return []

    raw = str(value).strip('"').strip("'")
    traditions = [t.strip() for t in raw.split(",")]
    normalized = []
    for trad in traditions:
        canonical = TRADITION_ALIASES.get(trad, trad)
        if canonical not in normalized and canonical not in ("N/A", "Multiple Religions"):
            normalized.append(canonical)
    return normalized


# =====================================================================
# BACKWARD COMPATIBILITY
# =====================================================================

def parse_rv_value(raw):
    """
    Convert any legacy or new rv_* value to an integer score.

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


def is_rv_detected(raw, threshold=DEFAULT_THRESHOLD):
    """
    Check if a religious tradition is detected (score >= threshold).
    """
    return parse_rv_value(raw) >= threshold


# =====================================================================
# SAFE YAML INSERTION HELPER
# =====================================================================

def insert_rv_fields_between_religious_values(fm_text, scores):
    """
    Insert 14 rv_* fields between religious_values: and religious_values_list: lines.

    Also updates both derived string fields.

    Uses regex insertion — no parse→rebuild round-trip (CLAUDE.md rule #2).

    Args:
        fm_text: Raw frontmatter text (without --- delimiters).
        scores: dict {field: int} for all RV_FIELDS.

    Returns:
        (new_fm_text, success_bool)
    """
    # Build the insertion block
    rv_lines = []
    for field in RV_FIELDS:
        rv_lines.append(f"{field}: {int(scores.get(field, 0))}")

    rv_block = "\n".join(rv_lines)

    # Derive the new string values
    derived_rv = derive_religious_values_string(scores)
    derived_list = derive_religious_values_list_string(scores)

    # Strategy: replace religious_values_list: line with rv_block + religious_values_list:
    # This inserts rv_* fields right before religious_values_list:
    pattern = r'^religious_values_list:.*$'
    replacement = f'{rv_block}\nreligious_values_list: "{derived_list}"'
    new_fm, count = re.subn(pattern, replacement, fm_text, count=1, flags=re.MULTILINE)

    if count == 0:
        return fm_text, False

    # Also update religious_values: with derived value
    new_fm, count2 = re.subn(
        r'^religious_values:.*$',
        f'religious_values: "{derived_rv}"',
        new_fm, count=1, flags=re.MULTILINE,
    )

    return new_fm, (count > 0 and count2 > 0)


def update_existing_rv_fields(fm_text, scores):
    """
    Update existing rv_* fields in frontmatter (for re-scoring).

    Also updates both derived string fields.

    Args:
        fm_text: Raw frontmatter text (without --- delimiters).
        scores: dict {field: int} for all RV_FIELDS.

    Returns:
        new_fm_text
    """
    new_fm = fm_text
    for field in RV_FIELDS:
        new_fm, _ = safe_yaml_set_int(new_fm, field, scores.get(field, 0))

    # Update derived strings
    derived_rv = derive_religious_values_string(scores)
    derived_list = derive_religious_values_list_string(scores)

    new_fm, _ = re.subn(
        r'^religious_values:.*$',
        f'religious_values: "{derived_rv}"',
        new_fm, count=1, flags=re.MULTILINE,
    )
    new_fm, _ = re.subn(
        r'^religious_values_list:.*$',
        f'religious_values_list: "{derived_list}"',
        new_fm, count=1, flags=re.MULTILINE,
    )

    return new_fm
