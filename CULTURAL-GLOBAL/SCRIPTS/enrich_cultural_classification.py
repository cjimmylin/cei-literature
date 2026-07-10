#!/usr/bin/env python3
"""
Cultural Classification Enrichment for CEI Literature Vault

Classifies ~899 papers with national_ethnic_cultural: "N/A" using heuristic
rules applied to title, abstract, PDF extract text, authors, and URLs.

Priority order:
    1. Language-based (title/abstract/extract mentions specific language/culture)
    2. Country-based (study population in a specific country/region)
    3. Dataset-based (language-specific datasets)
    4. Cultural framework mentions
    5. Author affiliation (weak signal from author_geography.json)
    6. Default: "Western" for Global North institutions, else "N/A"

Output: CULTURAL-GLOBAL/DATA/20260403-cultural-enrichment.json (JSON sidecar only)
        CULTURAL-GLOBAL/STATISTICS/20260403-cultural-enrichment-report.md

IMPORTANT: Does NOT modify paper YAML files.

DASHBOARD NOTE: generate_cultural_dashboard.py reads this JSON output.
When "Western (inferred)" was introduced (2026-04-03), the dashboard script
needs updates to:
  - Distinguish "Western (inferred)" from "Western" (explicit) in cultural
    label bar charts and pie charts
  - Optionally collapse both into a single "Western" bucket with a toggle
  - Read the new "western_type" field ("inferred" vs "explicit") for any
    Western-specific breakdowns
  - The WEIRD sub-dimensions chart (line ~222, ~548) is unaffected since it
    uses its own scoring, not the cultural label
"""
from __future__ import annotations

import functools
import json
import re
import sys
from collections import Counter
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Path setup ───────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent  # CULTURAL-GLOBAL/SCRIPTS/ → CEI-Lit-WS/
_PYTHON_DIR = _CEI_LIT_WS / "PYTHON"
_AGENT_LIB = _CEI_LIT_WS / ".agent" / "lib"
sys.path.insert(0, str(_PYTHON_DIR))
sys.path.insert(0, str(_AGENT_LIB))

from ethics_scoring import load_extract
from config import PAPERS_DIR

# ── Output paths ─────────────────────────────────────────────────────
DATA_DIR = _CEI_LIT_WS / "CULTURAL-GLOBAL" / "DATA"
STATS_DIR = _CEI_LIT_WS / "CULTURAL-GLOBAL" / "STATISTICS"
DATA_DIR.mkdir(parents=True, exist_ok=True)
STATS_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_JSON = DATA_DIR / "20260403-cultural-enrichment.json"
OUTPUT_REPORT = STATS_DIR / "20260403-cultural-enrichment-report.md"

# ── Load author geography data ───────────────────────────────────────
GEO_DATA_PATH = DATA_DIR / "20260403-author-geography.json"
AUTHOR_GEO: dict[str, dict] = {}

if GEO_DATA_PATH.exists():
    with open(GEO_DATA_PATH, "r", encoding="utf-8") as f:
        geo_json = json.load(f)
    for entry in geo_json.get("papers", []):
        AUTHOR_GEO[entry["filename"]] = entry


# =====================================================================
# CULTURAL DETECTION PATTERNS
# =====================================================================
# All patterns MUST be lowercase (count_matches lowercases text)

# Maps: pattern → (cultural_label, region, confidence_boost)
# Higher confidence_boost = more specific match

LANGUAGE_PATTERNS: list[tuple[str, str, str, int]] = [
    # (regex, cultural_label, region, confidence_boost)
    # East Asian languages
    (r"\bchinese\s+(?:language|text|nlp|corpus|dataset|social media|internet|online|news|sentiment|named entity|word segmentation|machine translation)", "Chinese", "East Asia", 15),
    (r"\bmandarin\b", "Chinese", "East Asia", 10),
    (r"\bcantonese\b", "Chinese", "East Asia", 10),
    (r"\bjapanese\s+(?:language|text|nlp|corpus|dataset|sentiment|named entity|machine translation)", "Japanese", "East Asia", 15),
    (r"\bkorean\s+(?:language|text|nlp|corpus|dataset|sentiment|named entity|machine translation)", "Korean", "East Asia", 15),
    # South Asian languages
    (r"\bhindi\s+(?:language|text|nlp|corpus|dataset|sentiment|hate speech)", "Indian", "South Asia", 15),
    (r"\bbangla\b", "Indian", "South Asia", 10),
    (r"\bbengali\s+(?:language|text|nlp|corpus|dataset|sentiment)", "Indian", "South Asia", 15),
    (r"\burdu\s+(?:language|text|nlp|corpus|dataset|sentiment)", "Pakistani/South Asian", "South Asia", 15),
    (r"\btamil\s+(?:language|text|nlp|corpus|dataset|sentiment)", "Indian", "South Asia", 15),
    (r"\btelugu\b", "Indian", "South Asia", 10),
    (r"\bmarathi\b", "Indian", "South Asia", 10),
    (r"\bsinhala\b", "South Asian", "South Asia", 10),
    (r"\bnepali\b", "South Asian", "South Asia", 10),
    # Southeast Asian languages
    (r"\bindonesian\s+(?:language|text|nlp|corpus|dataset|sentiment)", "Indonesian", "Southeast Asia", 15),
    (r"\bmalay\s+(?:language|text|nlp|corpus)", "Malay", "Southeast Asia", 15),
    (r"\bthai\s+(?:language|text|nlp|corpus|dataset|sentiment|word segmentation)", "Thai", "Southeast Asia", 15),
    (r"\bvietnamese\s+(?:language|text|nlp|corpus|dataset|sentiment)", "Vietnamese", "Southeast Asia", 15),
    (r"\bfilipino\s+(?:language|text|nlp|corpus|dataset|hate speech)", "Filipino", "Southeast Asia", 15),
    (r"\btagalog\b", "Filipino", "Southeast Asia", 10),
    # MENA languages
    (r"\barabic\s+(?:language|text|nlp|corpus|dataset|sentiment|hate speech|named entity|dialect)", "Arabic", "MENA", 15),
    (r"\bturkish\s+(?:language|text|nlp|corpus|dataset|sentiment|hate speech|named entity)", "Turkish", "MENA", 15),
    (r"\bpersian\s+(?:language|text|nlp|corpus|dataset|sentiment)", "Persian/Iranian", "MENA", 15),
    (r"\bfarsi\b", "Persian/Iranian", "MENA", 10),
    (r"\bhebrew\s+(?:language|text|nlp|corpus|dataset)", "Israeli", "MENA", 15),
    # Sub-Saharan African languages
    (r"\bswahili\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\byoruba\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\bhausa\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\bamharic\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\bigbo\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\bzulu\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\bxhosa\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\bkinyarwanda\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\bwolof\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\btwi\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\btigrinya\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\bsomali\b(?!.{0,20}pirat)", "African/Ubuntu", "Sub-Saharan Africa", 8),
    (r"\bafrican\s+(?:language|nlp|text)", "African/Ubuntu", "Sub-Saharan Africa", 12),
    (r"\bmasakhane\b", "African/Ubuntu", "Sub-Saharan Africa", 15),
    # Eastern European
    (r"\brussian\s+(?:language|text|nlp|corpus|dataset|sentiment|hate speech)", "Russian", "Eastern Europe & Central Asia", 15),
    (r"\bukrainian\s+(?:language|text|nlp|corpus)", "Ukrainian", "Eastern Europe & Central Asia", 15),
    (r"\bpolish\s+(?:language|text|nlp|corpus)", "Polish", "Eastern Europe & Central Asia", 15),
    (r"\bczech\s+(?:language|text|nlp|corpus)", "Czech", "Eastern Europe & Central Asia", 15),
    # Latin American
    (r"\bportugues(?:e|a)\s+(?:language|text|nlp|corpus|dataset|sentiment)", "Brazilian", "Latin America & Caribbean", 12),
    (r"\bspanish\s+(?:language|text|nlp|corpus|dataset|sentiment|hate speech)", "Spanish", "Western Europe", 10),
    # Western European
    (r"\bgerman\s+(?:language|text|nlp|corpus|dataset|sentiment|hate speech)", "German", "Western Europe", 12),
    (r"\bfrench\s+(?:language|text|nlp|corpus|dataset|sentiment|hate speech)", "French", "Western Europe", 12),
    (r"\bitalian\s+(?:language|text|nlp|corpus|dataset|sentiment)", "Italian", "Western Europe", 12),
    (r"\bdutch\s+(?:language|text|nlp|corpus|dataset|sentiment)", "Dutch", "Western Europe", 12),
    # Indic general
    (r"\bindic\s+(?:language|script|nlp)", "Indian", "South Asia", 12),
    # Tibetan / minority languages in China
    (r"\btibetan\b", "Chinese", "East Asia", 10),
    (r"\buyghur\b", "Chinese", "East Asia", 10),
    # Kurdish
    (r"\bkurdish\b", "Kurdish", "MENA", 10),
    (r"\bsorani\b", "Kurdish", "MENA", 10),
]

# Simpler language mentions (weaker signal — found anywhere in text)
LANGUAGE_SIMPLE: list[tuple[str, str, str]] = [
    (r"\bchinese\b", "Chinese", "East Asia"),
    (r"\bjapanese\b", "Japanese", "East Asia"),
    (r"\bkorean\b", "Korean", "East Asia"),
    (r"\bhindi\b", "Indian", "South Asia"),
    (r"\barabic\b", "Arabic", "MENA"),
    (r"\bturkish\b", "Turkish", "MENA"),
    (r"\bindonesian\b", "Indonesian", "Southeast Asia"),
    (r"\bthai\b", "Thai", "Southeast Asia"),
    (r"\bvietnamese\b", "Vietnamese", "Southeast Asia"),
    (r"\brussian\b", "Russian", "Eastern Europe & Central Asia"),
    (r"\bbrazilian\b", "Brazilian", "Latin America & Caribbean"),
]

# Country/region mentions in study context
COUNTRY_STUDY_PATTERNS: list[tuple[str, str, str, int]] = [
    # (regex, cultural_label, region, confidence_boost)
    # The regex tries to match country in study context
    (r"\bin\s+china\b", "Chinese", "East Asia", 12),
    (r"\bchinese\s+(?:user|participant|respondent|population|student|worker|society|context|culture|value)", "Chinese", "East Asia", 15),
    (r"\bin\s+japan\b", "Japanese", "East Asia", 12),
    (r"\bjapanese\s+(?:user|participant|respondent|population|student|worker|society|context|culture|value)", "Japanese", "East Asia", 15),
    (r"\bin\s+(?:south\s+)?korea\b", "Korean", "East Asia", 12),
    (r"\bkorean\s+(?:user|participant|respondent|population|student|worker|society|context|culture|value)", "Korean", "East Asia", 15),
    (r"\bin\s+india\b", "Indian", "South Asia", 12),
    (r"\bindian\s+(?:user|participant|respondent|population|student|worker|society|context|culture|value)", "Indian", "South Asia", 15),
    (r"\bin\s+pakistan\b", "Pakistani/South Asian", "South Asia", 12),
    (r"\bin\s+(?:saudi\s+)?arab(?:ia|ic\s+countries)\b", "Arabic", "MENA", 12),
    (r"\bin\s+turkey\b", "Turkish", "MENA", 12),
    (r"\bin\s+iran\b", "Persian/Iranian", "MENA", 12),
    (r"\bin\s+indonesia\b", "Indonesian", "Southeast Asia", 12),
    (r"\bin\s+brazil\b", "Brazilian", "Latin America & Caribbean", 12),
    (r"\bin\s+mexico\b", "Mexican", "Latin America & Caribbean", 12),
    (r"\bin\s+nigeria\b", "African/Ubuntu", "Sub-Saharan Africa", 12),
    (r"\bin\s+kenya\b", "African/Ubuntu", "Sub-Saharan Africa", 12),
    (r"\bin\s+(?:south\s+)?africa\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\bin\s+(?:sub-saharan|west|east)\s+africa\b", "African/Ubuntu", "Sub-Saharan Africa", 12),
    (r"\bin\s+russia\b", "Russian", "Eastern Europe & Central Asia", 12),
    (r"\bin\s+germany\b", "German", "Western Europe", 10),
    (r"\bin\s+france\b", "French", "Western Europe", 10),
    (r"\bglobal\s+south\b", "Multicultural/Cross-cultural", "Global South", 8),
    (r"\blatin\s+america\b", "Latin American", "Latin America & Caribbean", 10),
    (r"\bsoutheast\s+asia\b", "Southeast Asian", "Southeast Asia", 10),
    (r"\bmiddle\s+east\b", "Arabic", "MENA", 8),
    (r"\bsub-saharan\s+africa\b", "African/Ubuntu", "Sub-Saharan Africa", 10),
    (r"\bafrican\s+(?:context|perspective|country|countries|society|continent|culture|value)", "African/Ubuntu", "Sub-Saharan Africa", 12),
    (r"\bindigenous\s+(?:people|community|communities|culture|knowledge|language|perspective)", "Indigenous", "Various", 10),
    (r"\bmaori\b", "Maori/Oceanian", "Oceania", 12),
    (r"\baboriginal\b", "Australian Aboriginal", "Oceania", 10),
    (r"\bfirst\s+nations\b", "Indigenous", "North America", 10),
]

# Dataset-based patterns (strong signal)
DATASET_PATTERNS: list[tuple[str, str, str]] = [
    # Chinese datasets
    (r"\bclue\s+benchmark\b", "Chinese", "East Asia"),
    (r"\bcn-?dbpedia\b", "Chinese", "East Asia"),
    (r"\bchinese\s+treebank\b", "Chinese", "East Asia"),
    (r"\bctb\d\b", "Chinese", "East Asia"),
    (r"\bweibo\b", "Chinese", "East Asia"),
    (r"\bbaike\b", "Chinese", "East Asia"),
    (r"\bzhihu\b", "Chinese", "East Asia"),
    # Japanese datasets
    (r"\bjsnli\b", "Japanese", "East Asia"),
    (r"\bjcommonsenseqa\b", "Japanese", "East Asia"),
    (r"\bjglue\b", "Japanese", "East Asia"),
    (r"\bjblimp\b", "Japanese", "East Asia"),
    # Korean datasets
    (r"\bklue\b", "Korean", "East Asia"),
    (r"\bkorquad\b", "Korean", "East Asia"),
    # Arabic datasets
    (r"\basad\b", "Arabic", "MENA"),
    (r"\bqadi\b", "Arabic", "MENA"),
    (r"\bnadi\b", "Arabic", "MENA"),
    (r"\barse(?:ntd|val)\b", "Arabic", "MENA"),
    # Indian datasets
    (r"\biitb\s+(?:hindi|english)\b", "Indian", "South Asia"),
    (r"\bhasoc\b", "Indian", "South Asia"),
    # Turkish datasets
    (r"\btrmorph\b", "Turkish", "MENA"),
    # Brazilian/Portuguese datasets
    (r"\bassin\b", "Brazilian", "Latin America & Caribbean"),
    (r"\bolid-br\b", "Brazilian", "Latin America & Caribbean"),
    # Russian datasets
    (r"\brusse\b", "Russian", "Eastern Europe & Central Asia"),
    # Multilingual specific
    (r"\bmasakhane\b", "African/Ubuntu", "Sub-Saharan Africa"),
    (r"\bamericas\s*nlp\b", "Indigenous", "Latin America & Caribbean"),
]

# Cultural framework mentions
CULTURAL_FRAMEWORK_PATTERNS: list[tuple[str, str, str, int]] = [
    # Confucian
    (r"\bconfucian\b", "Chinese", "East Asia", 12),
    (r"\bharmony\b(?=.*\b(?:chinese|confucian|east\s+asian)\b)", "Chinese", "East Asia", 10),
    # Ubuntu
    (r"\bubuntu\b(?!.*\blinux\b)(?!.*\boperating\b)", "African/Ubuntu", "Sub-Saharan Africa", 12),
    # Islamic
    (r"\bislamic\s+(?:ethics|values|perspective|law|jurisprudence|finance)\b", "Islamic", "MENA", 12),
    (r"\bsharia\b", "Islamic", "MENA", 10),
    (r"\bmaqasid\b", "Islamic", "MENA", 12),
    # Buddhist
    (r"\bbuddhist\s+(?:ethics|values|perspective|philosophy)\b", "Buddhist/East Asian", "East Asia", 12),
    # Hindu / Dharmic
    (r"\bhindu\s+(?:ethics|values|perspective|philosophy)\b", "Indian", "South Asia", 12),
    (r"\bdharmic\b", "Indian", "South Asia", 10),
    # Indigenous
    (r"\bkaitiakitanga\b", "Maori/Oceanian", "Oceania", 15),
    (r"\btikanga\b", "Maori/Oceanian", "Oceania", 15),
    (r"\bdata\s+sovereignty\b(?=.*\bindigenous\b)", "Indigenous", "Various", 10),
    (r"\bbuen\s+vivir\b", "Latin American", "Latin America & Caribbean", 15),
    (r"\bsumak\s+kawsay\b", "Latin American", "Latin America & Caribbean", 15),
    # WEIRD
    (r"\bweird\b(?=.*\b(?:western|educated|industrialized|rich|democratic)\b)", "Multicultural/Cross-cultural", "Various", 8),
    # Cross-cultural
    (r"\bcross-cultural\b", "Multicultural/Cross-cultural", "Various", 8),
    (r"\bmulticultural\b", "Multicultural/Cross-cultural", "Various", 8),
    (r"\bintercultural\b", "Multicultural/Cross-cultural", "Various", 8),
]

# Cross-cultural detection patterns (paper studies multiple cultures)
CROSS_CULTURAL_INDICATORS = [
    r"\bcross-cultural\b",
    r"\bmulticultural\b",
    r"\bintercultural\b",
    r"\bcultural\s+comparison\b",
    r"\bcompare\w*\s+(?:across|between)\s+(?:culture|countr|region|nation)",
    r"\bmultilingual\b(?=.*\b(?:cultur|countr|nation|diverse)\b)",
    r"\bglobal\s+(?:perspective|survey|comparison|analysis|study)\b",
    r"\bcultural\s+(?:difference|variation|diversity|dimension|bias)\b",
]


# =====================================================================
# REGION ↔ CULTURAL LABEL MAPPING (for affiliation fallback)
# =====================================================================

REGION_TO_CULTURAL: dict[str, str] = {
    "East Asia": "East Asian",
    "South Asia": "South Asian",
    "Southeast Asia": "Southeast Asian",
    "MENA": "Arabic",
    "Sub-Saharan Africa": "African/Ubuntu",
    "Latin America & Caribbean": "Latin American",
    "Eastern Europe & Central Asia": "Eastern European",
    "Western Europe": "Western",
    "North America": "Western",
    "Oceania": "Western",
}

WESTERN_REGIONS = {"Western Europe", "North America", "Oceania"}


# =====================================================================
# HELPER FUNCTIONS
# =====================================================================

def extract_frontmatter_field(content: str, field: str) -> str:
    """Extract a single YAML frontmatter field value."""
    m = re.search(rf'^{re.escape(field)}:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    if m:
        val = m.group(1).strip().strip('"')
        return val
    return ""


def read_paper(filepath: Path) -> dict:
    """Read key fields from a paper's YAML frontmatter."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return {}

    # Only parse frontmatter
    if not content.startswith("---"):
        return {}

    fm_end = content.find("---", 3)
    if fm_end == -1:
        fm = content
    else:
        fm = content[:fm_end]

    return {
        "filename": filepath.name,
        "stem": filepath.stem,
        "title": extract_frontmatter_field(fm, "short_title"),
        "abstract": extract_frontmatter_field(fm, "abstract"),
        "authors": extract_frontmatter_field(fm, "authors"),
        "url": extract_frontmatter_field(fm, "url"),
        "national_ethnic_cultural": extract_frontmatter_field(fm, "national_ethnic_cultural"),
    }


def build_text_corpus(paper: dict) -> str:
    """Combine title + abstract + extract into a single lowercase text corpus."""
    parts = []
    if paper.get("title"):
        parts.append(paper["title"])
    if paper.get("abstract"):
        parts.append(paper["abstract"])

    # Load PDF extract
    extract = load_extract(paper.get("stem", ""))
    if extract:
        parts.append(extract)

    return "\n".join(parts).lower()


def count_pattern_matches(text: str, patterns: list[str]) -> tuple[int, list[str]]:
    """Count regex matches in already-lowercased text."""
    total = 0
    matched = []
    for pat in patterns:
        for m in re.finditer(pat, text):
            total += 1
            matched.append(m.group())
    return total, matched


# =====================================================================
# CLASSIFICATION ENGINE
# =====================================================================

def classify_paper(paper: dict, text: str) -> dict:
    """
    Classify a paper's cultural focus using heuristic rules.
    Returns a classification dict.
    """
    filename = paper["filename"]
    title = (paper.get("title") or "").lower()
    abstract = (paper.get("abstract") or "").lower()
    title_abstract = f"{title} {abstract}"

    # Track all detections with scores
    detections: list[dict] = []

    # ── 1. Language-based (strong patterns in title/abstract) ─────────
    for pat, label, region, boost in LANGUAGE_PATTERNS:
        # Search title/abstract first (stronger signal)
        ta_matches = len(re.findall(pat, title_abstract))
        if ta_matches > 0:
            detections.append({
                "label": label, "region": region,
                "confidence": "high", "method": "language_mention",
                "score": boost + 5,  # title/abstract bonus
                "evidence": f"Title/abstract: '{re.search(pat, title_abstract).group()}'"
            })
        else:
            # Search full text (weaker)
            text_matches = len(re.findall(pat, text))
            if text_matches >= 2:  # Need at least 2 mentions in extract
                detections.append({
                    "label": label, "region": region,
                    "confidence": "medium", "method": "language_mention",
                    "score": boost,
                    "evidence": f"Extract text: {text_matches} matches of '{pat}'"
                })

    # ── 2. Country-based study population ─────────────────────────────
    for pat, label, region, boost in COUNTRY_STUDY_PATTERNS:
        ta_matches = len(re.findall(pat, title_abstract))
        if ta_matches > 0:
            detections.append({
                "label": label, "region": region,
                "confidence": "high", "method": "country_mention",
                "score": boost + 5,
                "evidence": f"Title/abstract: '{re.search(pat, title_abstract).group()}'"
            })
        else:
            text_matches = len(re.findall(pat, text))
            if text_matches >= 3:
                detections.append({
                    "label": label, "region": region,
                    "confidence": "medium", "method": "country_mention",
                    "score": boost - 2,
                    "evidence": f"Extract text: {text_matches} matches"
                })

    # ── 3. Dataset-based ──────────────────────────────────────────────
    for pat, label, region in DATASET_PATTERNS:
        if re.search(pat, title_abstract):
            detections.append({
                "label": label, "region": region,
                "confidence": "high", "method": "dataset",
                "score": 18,
                "evidence": f"Dataset mention: '{re.search(pat, title_abstract).group()}'"
            })
        elif re.search(pat, text):
            detections.append({
                "label": label, "region": region,
                "confidence": "medium", "method": "dataset",
                "score": 12,
                "evidence": f"Dataset in extract: '{re.search(pat, text).group()}'"
            })

    # ── 4. Cultural framework mentions ────────────────────────────────
    for pat, label, region, boost in CULTURAL_FRAMEWORK_PATTERNS:
        if re.search(pat, title_abstract):
            detections.append({
                "label": label, "region": region,
                "confidence": "high", "method": "framework",
                "score": boost + 3,
                "evidence": f"Framework: '{re.search(pat, title_abstract).group()}'"
            })
        elif re.search(pat, text):
            detections.append({
                "label": label, "region": region,
                "confidence": "medium", "method": "framework",
                "score": boost,
                "evidence": f"Framework in extract"
            })

    # ── 5. Simple language mentions (weaker, title/abstract only) ─────
    if not detections:
        for pat, label, region in LANGUAGE_SIMPLE:
            ta_count = len(re.findall(pat, title_abstract))
            if ta_count > 0:
                # Verify it's a cultural context, not just adjective
                # e.g., "Chinese" as in "Chinese language" vs "Chinese restaurant"
                detections.append({
                    "label": label, "region": region,
                    "confidence": "medium", "method": "language_mention",
                    "score": 8,
                    "evidence": f"Simple language mention in title/abstract: '{label}'"
                })

    # ── Check for cross-cultural ──────────────────────────────────────
    cross_cultural_count, _ = count_pattern_matches(text, CROSS_CULTURAL_INDICATORS)
    is_cross_cultural = cross_cultural_count >= 2 or any(
        re.search(p, title_abstract) for p in CROSS_CULTURAL_INDICATORS
    )

    # ── Aggregate detections ──────────────────────────────────────────
    if not detections:
        # ── 6. Affiliation fallback ───────────────────────────────────
        geo = AUTHOR_GEO.get(filename, {})
        author_region = geo.get("author_region", "Unknown")
        author_country = geo.get("author_country", "")

        if author_region in WESTERN_REGIONS:
            return {
                "filename": filename,
                "original_cultural": "N/A",
                "inferred_cultural": "Western (inferred)",
                "western_type": "inferred",
                "study_population_region": author_region,
                "cultural_comparison_type": "universal-claim",
                "positionality": "universal",
                "confidence": "low",
                "method": "default",
                "evidence": f"No cultural markers; author affiliation: {author_region} ({author_country})"
            }
        elif author_region != "Unknown":
            cultural = REGION_TO_CULTURAL.get(author_region, "N/A")
            result = {
                "filename": filename,
                "original_cultural": "N/A",
                "inferred_cultural": cultural,
                "study_population_region": author_region,
                "cultural_comparison_type": "universal-claim",
                "positionality": "universal",
                "confidence": "low",
                "method": "affiliation",
                "evidence": f"No cultural markers; author affiliation: {author_region} ({author_country})"
            }
            if cultural == "Western":
                result["inferred_cultural"] = "Western (inferred)"
                result["western_type"] = "inferred"
            return result
        else:
            return {
                "filename": filename,
                "original_cultural": "N/A",
                "inferred_cultural": "N/A",
                "study_population_region": "Unknown",
                "cultural_comparison_type": "universal-claim",
                "positionality": "universal",
                "confidence": "low",
                "method": "default",
                "evidence": "No cultural markers found; unknown author affiliation"
            }

    # ── Pick best detection ───────────────────────────────────────────
    # Sort by score descending
    detections.sort(key=lambda d: d["score"], reverse=True)

    # Count distinct cultural labels
    distinct_labels = set(d["label"] for d in detections)

    # If multiple distinct non-Western cultures detected → cross-cultural
    non_western_labels = {l for l in distinct_labels if l not in ("Western", "German", "French", "Italian", "Dutch")}

    if len(non_western_labels) > 1 or is_cross_cultural:
        # Cross-cultural paper
        top = detections[0]
        labels_str = ", ".join(sorted(non_western_labels)[:3]) if non_western_labels else "Multicultural/Cross-cultural"
        if len(non_western_labels) > 1:
            cultural_label = "Multicultural/Cross-cultural"
        elif is_cross_cultural:
            cultural_label = "Multicultural/Cross-cultural"
        else:
            cultural_label = top["label"]

        regions = sorted(set(d["region"] for d in detections if d["region"] != "Various"))
        region_str = ", ".join(regions[:3]) if regions else "Various"

        result = {
            "filename": filename,
            "original_cultural": "N/A",
            "inferred_cultural": cultural_label,
            "study_population_region": region_str,
            "cultural_comparison_type": "cross-cultural",
            "positionality": "collaborative",
            "confidence": top["confidence"],
            "method": top["method"],
            "evidence": f"Multiple cultures: {labels_str}; {top['evidence']}"
        }
        if cultural_label == "Western":
            result["western_type"] = "explicit"
        return result

    # Single culture
    top = detections[0]

    # Determine positionality
    geo = AUTHOR_GEO.get(filename, {})
    author_region = geo.get("author_region", "Unknown")
    study_region = top["region"]

    if author_region == study_region:
        positionality = "endogenous"
    elif author_region in WESTERN_REGIONS and study_region not in WESTERN_REGIONS:
        positionality = "exogenous"
    elif author_region == "Unknown":
        positionality = "universal"
    else:
        positionality = "collaborative"

    result = {
        "filename": filename,
        "original_cultural": "N/A",
        "inferred_cultural": top["label"],
        "study_population_region": top["region"],
        "cultural_comparison_type": "single-culture",
        "positionality": positionality,
        "confidence": top["confidence"],
        "method": top["method"],
        "evidence": top["evidence"]
    }
    if top["label"] == "Western":
        result["western_type"] = "explicit"
    return result


# =====================================================================
# MAIN
# =====================================================================

def main():
    print("=" * 70)
    print("Cultural Classification Enrichment — CEI Literature Vault")
    print("=" * 70)

    # Collect papers with N/A cultural classification
    na_papers = []
    total_papers = 0

    for paper_path in sorted(PAPERS_DIR.iterdir()):
        if not paper_path.name.endswith(".md"):
            continue
        total_papers += 1

        paper = read_paper(paper_path)
        if not paper:
            continue

        nec = paper.get("national_ethnic_cultural", "")
        if nec in ("N/A", ""):
            na_papers.append(paper)

    print(f"\nTotal papers: {total_papers}")
    print(f"Papers with N/A cultural classification: {len(na_papers)}")
    print(f"Processing...\n")

    # Classify each paper
    results = []
    for i, paper in enumerate(na_papers, 1):
        if i % 100 == 0:
            print(f"  [{i}/{len(na_papers)}] Processing {paper['filename'][:60]}...")

        text = build_text_corpus(paper)
        classification = classify_paper(paper, text)
        results.append(classification)

    # ── Summary statistics ────────────────────────────────────────────
    cultural_counts = Counter(r["inferred_cultural"] for r in results)
    region_counts = Counter(r["study_population_region"] for r in results)
    method_counts = Counter(r["method"] for r in results)
    confidence_counts = Counter(r["confidence"] for r in results)
    comparison_counts = Counter(r["cultural_comparison_type"] for r in results)
    positionality_counts = Counter(r["positionality"] for r in results)

    classified_count = sum(1 for r in results if r["inferred_cultural"] != "N/A")
    western_inferred = sum(1 for r in results if r.get("western_type") == "inferred")
    western_explicit = sum(1 for r in results if r.get("western_type") == "explicit")

    print(f"\n{'=' * 70}")
    print(f"RESULTS SUMMARY")
    print(f"{'=' * 70}")
    print(f"Total classified: {classified_count}/{len(results)} ({100*classified_count/max(len(results),1):.1f}%)")
    print(f"Remaining N/A: {len(results) - classified_count}")
    print(f"Western (inferred — no cultural markers): {western_inferred}")
    print(f"Western (explicit — cultural markers found): {western_explicit}")
    print()

    print("Top 15 cultural labels:")
    for label, count in cultural_counts.most_common(15):
        print(f"  {label:40s} {count:4d}")
    print()

    print("Regions:")
    for region, count in region_counts.most_common():
        print(f"  {region:40s} {count:4d}")
    print()

    print("Methods:")
    for method, count in method_counts.most_common():
        print(f"  {method:40s} {count:4d}")
    print()

    print("Confidence levels:")
    for conf, count in confidence_counts.most_common():
        print(f"  {conf:40s} {count:4d}")
    print()

    print("Comparison types:")
    for comp, count in comparison_counts.most_common():
        print(f"  {comp:40s} {count:4d}")
    print()

    print("Positionality:")
    for pos, count in positionality_counts.most_common():
        print(f"  {pos:40s} {count:4d}")

    # ── Save JSON ─────────────────────────────────────────────────────
    output = {
        "date": "20260403",
        "total_na_papers": len(na_papers),
        "total_classified": classified_count,
        "remaining_na": len(results) - classified_count,
        "western_inferred": western_inferred,
        "western_explicit": western_explicit,
        "summary": {
            "cultural_labels": dict(cultural_counts.most_common()),
            "regions": dict(region_counts.most_common()),
            "methods": dict(method_counts.most_common()),
            "confidence": dict(confidence_counts.most_common()),
            "comparison_types": dict(comparison_counts.most_common()),
            "positionality": dict(positionality_counts.most_common()),
        },
        "papers": results,
    }

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nJSON saved: {OUTPUT_JSON}")

    # ── Save report ───────────────────────────────────────────────────
    report_lines = [
        "# Cultural Classification Enrichment Report",
        f"**Date:** 2026-04-03",
        f"**Total papers processed:** {len(na_papers)}",
        f"**Successfully classified:** {classified_count} ({100*classified_count/max(len(results),1):.1f}%)",
        f"**Remaining N/A:** {len(results) - classified_count}",
        f"**Western (inferred, no cultural markers):** {western_inferred}",
        f"**Western (explicit, cultural markers found):** {western_explicit}",
        "",
        "## Method",
        "Heuristic classification using keyword patterns applied to paper title,",
        "abstract, and PDF extract text. Six priority tiers:",
        "1. **Language-based** — title/abstract mentions a specific language + NLP context",
        "2. **Country-based** — study population in a specific country/region",
        "3. **Dataset-based** — language-specific NLP datasets",
        "4. **Cultural framework** — explicit discussion of cultural values/traditions",
        "5. **Affiliation** — weak signal from author geography",
        "6. **Default** — Western for Global North affiliations, else N/A",
        "",
        "## Cultural Label Distribution",
        "",
        "| Cultural Label | Count | % |",
        "|---|---:|---:|",
    ]
    for label, count in cultural_counts.most_common():
        pct = 100 * count / max(len(results), 1)
        report_lines.append(f"| {label} | {count} | {pct:.1f}% |")

    report_lines += [
        "",
        "## Region Distribution",
        "",
        "| Region | Count | % |",
        "|---|---:|---:|",
    ]
    for region, count in region_counts.most_common():
        pct = 100 * count / max(len(results), 1)
        report_lines.append(f"| {region} | {count} | {pct:.1f}% |")

    report_lines += [
        "",
        "## Detection Method",
        "",
        "| Method | Count | % |",
        "|---|---:|---:|",
    ]
    for method, count in method_counts.most_common():
        pct = 100 * count / max(len(results), 1)
        report_lines.append(f"| {method} | {count} | {pct:.1f}% |")

    report_lines += [
        "",
        "## Confidence Distribution",
        "",
        "| Confidence | Count | % |",
        "|---|---:|---:|",
    ]
    for conf, count in confidence_counts.most_common():
        pct = 100 * count / max(len(results), 1)
        report_lines.append(f"| {conf} | {count} | {pct:.1f}% |")

    report_lines += [
        "",
        "## Cultural Comparison Type",
        "",
        "| Type | Count | % |",
        "|---|---:|---:|",
    ]
    for comp, count in comparison_counts.most_common():
        pct = 100 * count / max(len(results), 1)
        report_lines.append(f"| {comp} | {count} | {pct:.1f}% |")

    report_lines += [
        "",
        "## Positionality",
        "",
        "| Positionality | Count | % |",
        "|---|---:|---:|",
    ]
    for pos, count in positionality_counts.most_common():
        pct = 100 * count / max(len(results), 1)
        report_lines.append(f"| {pos} | {count} | {pct:.1f}% |")

    # Sample high-confidence non-Western classifications
    non_western_high = [r for r in results if r["confidence"] == "high"
                        and r["inferred_cultural"] not in ("Western", "Western (inferred)", "N/A")]
    if non_western_high:
        report_lines += [
            "",
            "## Sample High-Confidence Non-Western Classifications",
            "",
            "| Paper | Cultural Label | Method | Evidence |",
            "|---|---|---|---|",
        ]
        for r in non_western_high[:30]:
            fn = r["filename"][:50]
            evidence = r["evidence"][:60].replace("|", "\\|")
            report_lines.append(f"| {fn} | {r['inferred_cultural']} | {r['method']} | {evidence} |")

    report_lines.append("")
    with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    print(f"Report saved: {OUTPUT_REPORT}")


if __name__ == "__main__":
    main()
