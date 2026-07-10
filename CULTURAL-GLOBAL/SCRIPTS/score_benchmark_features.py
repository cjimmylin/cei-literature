#!/usr/bin/env python3
"""
score_benchmark_features.py — Auto-extract benchmark features from YAML frontmatter
and PDF extracts for the top 200 cross-cultural benchmark candidates.

Reads:
  - CULTURAL-GLOBAL/DATA/20260404-benchmark-candidates.json (candidate list)
  - papers/<filename> (YAML frontmatter, read-only)
  - PDF Extracts/YYYY/<filename> (first 15K chars, read-only)

Writes:
  - CULTURAL-GLOBAL/DATA/20260404-benchmark-features.json

Safety: NEVER modifies paper files. Read-only access only.
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
WS = Path(__file__).resolve().parent.parent.parent  # CEI-Lit-WS/
PAPERS_DIR = WS / "papers"
EXTRACTS_DIR = WS / "PDF Extracts"
CANDIDATES_PATH = WS / "CULTURAL-GLOBAL" / "DATA" / "20260404-benchmark-candidates.json"
OUTPUT_PATH = WS / "CULTURAL-GLOBAL" / "DATA" / "20260404-benchmark-features.json"

TOP_N = 200
MIN_SCORE = 40
EXTRACT_CHARS = 15_000

# ---------------------------------------------------------------------------
# Country & language lists for cultural scope detection
# ---------------------------------------------------------------------------
COUNTRIES = [
    "Afghanistan", "Albania", "Algeria", "Argentina", "Armenia", "Australia",
    "Austria", "Azerbaijan", "Bahrain", "Bangladesh", "Belarus", "Belgium",
    "Benin", "Bhutan", "Bolivia", "Bosnia", "Botswana", "Brazil", "Brunei",
    "Bulgaria", "Burkina Faso", "Cambodia", "Cameroon", "Canada", "Chad",
    "Chile", "China", "Colombia", "Congo", "Costa Rica", "Croatia", "Cuba",
    "Cyprus", "Czech", "Denmark", "Dominican", "Ecuador", "Egypt",
    "El Salvador", "Estonia", "Ethiopia", "Fiji", "Finland", "France",
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Guatemala",
    "Guinea", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia",
    "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan",
    "Jordan", "Kazakhstan", "Kenya", "Korea", "Kuwait", "Kyrgyzstan", "Laos",
    "Latvia", "Lebanon", "Libya", "Lithuania", "Luxembourg", "Madagascar",
    "Malawi", "Malaysia", "Mali", "Malta", "Mexico", "Moldova", "Mongolia",
    "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nepal",
    "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway",
    "Oman", "Pakistan", "Palestine", "Panama", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia",
    "Rwanda", "Saudi Arabia", "Senegal", "Serbia", "Sierra Leone",
    "Singapore", "Slovakia", "Slovenia", "Somalia", "South Africa",
    "South Korea", "Spain", "Sri Lanka", "Sudan", "Sweden", "Switzerland",
    "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo",
    "Trinidad", "Tunisia", "Turkey", "Turkmenistan", "Uganda", "Ukraine",
    "United Arab Emirates", "United Kingdom", "United States", "Uruguay",
    "Uzbekistan", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe",
]
# Short aliases that are unambiguous in academic text
COUNTRY_ALIASES = {
    "U.S.": "United States", "US ": "United States", "USA": "United States",
    "UK ": "United Kingdom", "U.K.": "United Kingdom",
    "UAE": "United Arab Emirates", "PRC": "China",
    "South Korean": "South Korea", "Korean": "Korea",
    "Chinese": "China", "Japanese": "Japan", "Indian": "India",
    "Brazilian": "Brazil", "German": "Germany", "French": "France",
    "Italian": "Italy", "Spanish": "Spain", "Turkish": "Turkey",
    "Egyptian": "Egypt", "Nigerian": "Nigeria", "Kenyan": "Kenya",
    "Saudi": "Saudi Arabia", "Iranian": "Iran", "Iraqi": "Iraq",
    "Pakistani": "Pakistan", "Bangladeshi": "Bangladesh",
    "Indonesian": "Indonesia", "Thai": "Thailand",
    "Vietnamese": "Vietnam", "Filipino": "Philippines",
    "Malaysian": "Malaysia", "Singaporean": "Singapore",
    "Ghanaian": "Ghana", "Tanzanian": "Tanzania",
    "Ugandan": "Uganda", "Rwandan": "Rwanda",
    "Senegalese": "Senegal", "Cameroonian": "Cameroon",
    "Ethiopian": "Ethiopia", "Moroccan": "Morocco",
    "Tunisian": "Tunisia", "Algerian": "Algeria",
    "South African": "South Africa",
}

GLOBAL_SOUTH_COUNTRIES = {
    "Afghanistan", "Algeria", "Angola", "Argentina", "Bangladesh", "Benin",
    "Bhutan", "Bolivia", "Botswana", "Brazil", "Burkina Faso", "Cambodia",
    "Cameroon", "Chad", "Chile", "China", "Colombia", "Congo", "Costa Rica",
    "Cuba", "Dominican", "Ecuador", "Egypt", "El Salvador", "Ethiopia",
    "Fiji", "Gabon", "Gambia", "Ghana", "Guatemala", "Guinea", "Haiti",
    "Honduras", "India", "Indonesia", "Iran", "Iraq", "Jamaica", "Jordan",
    "Kazakhstan", "Kenya", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon",
    "Libya", "Madagascar", "Malawi", "Malaysia", "Mali", "Mexico", "Moldova",
    "Mongolia", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nepal",
    "Nicaragua", "Niger", "Nigeria", "Oman", "Pakistan", "Palestine",
    "Panama", "Paraguay", "Peru", "Philippines", "Qatar", "Rwanda",
    "Saudi Arabia", "Senegal", "Sierra Leone", "Somalia", "South Africa",
    "Sri Lanka", "Sudan", "Syria", "Tajikistan", "Tanzania", "Thailand",
    "Togo", "Trinidad", "Tunisia", "Turkey", "Turkmenistan", "Uganda",
    "Ukraine", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam", "Yemen",
    "Zambia", "Zimbabwe",
}

LANGUAGES = [
    "English", "Chinese", "Mandarin", "Cantonese", "Arabic", "Hindi", "Urdu",
    "Bengali", "Japanese", "Korean", "Spanish", "Portuguese", "French",
    "German", "Russian", "Italian", "Dutch", "Turkish", "Persian", "Farsi",
    "Thai", "Vietnamese", "Indonesian", "Malay", "Tagalog", "Filipino",
    "Swahili", "Hausa", "Yoruba", "Igbo", "Amharic", "Tigrinya",
    "Hebrew", "Greek", "Polish", "Czech", "Romanian", "Hungarian",
    "Swedish", "Norwegian", "Danish", "Finnish", "Tamil", "Telugu",
    "Marathi", "Gujarati", "Kannada", "Malayalam", "Sinhala", "Nepali",
    "Burmese", "Khmer", "Lao", "Tibetan", "Uyghur", "Pashto", "Kurdish",
    "Ukrainian", "Serbian", "Croatian", "Bulgarian", "Slovak", "Slovenian",
    "Estonian", "Latvian", "Lithuanian", "Georgian", "Armenian", "Azerbaijani",
    "Kazakh", "Uzbek", "Turkmen", "Tajik", "Kyrgyz", "Mongolian",
    "Catalan", "Basque", "Galician", "Welsh", "Irish", "Scottish",
    "Afrikaans", "Zulu", "Xhosa", "Sotho", "Tswana",
]

INDIGENOUS_KEYWORDS = [
    "indigenous", "first nations", "maori", "aboriginal", "tikanga",
    "kaitiakitanga", "native american", "inuit", "data sovereignty",
    "decolonize", "decolonise", "decolonial",
]

NW_FRAMEWORKS = [
    ("MFT", r"\b(?:moral foundations theory|mft)\b"),
    ("Moral Foundations", r"\bmoral foundations\b"),
    ("Schwartz", r"\b(?:schwartz|schwartz values|svs|pvq|portrait values)\b"),
    ("Kohlberg", r"\b(?:kohlberg|dit|defining issues test|moral development stages)\b"),
    ("Virtue Ethics", r"\bvirtue ethics\b"),
    ("Deontological", r"\b(?:deontolog|kantian|categorical imperative)\b"),
    ("Utilitarian", r"\b(?:utilitarian|consequential|greatest good|welfare maximiz)\b"),
    ("Care Ethics", r"\b(?:care ethics|ethics of care|nel noddings|carol gilligan)\b"),
    ("Contractarian", r"\b(?:contractarian|social contract|rawls|veil of ignorance)\b"),
    ("Confucian", r"\b(?:confuci|ren|li |junzi|dao|filial piety|five relationships)\b"),
    ("Ubuntu", r"\bubuntu\b"),
    ("Islamic Ethics", r"\b(?:islamic ethics|sharia|maqasid|fiqh|halal|haram)\b"),
    ("Buddhist", r"\b(?:buddhist ethics|dharma|karma|ahimsa|middle way|noble eightfold)\b"),
    ("Dharmic", r"\b(?:dharmic|hindu ethics|vedant|bhagavad)\b"),
    ("Indigenous", r"\b(?:indigenous|tikanga|kaitiakitanga|buen vivir|sumak kawsay)\b"),
    ("Buen Vivir", r"\b(?:buen vivir|sumak kawsay)\b"),
]

# LLM names for A6 detection
LLM_NAMES_RE = re.compile(
    r"\b(?:gpt[-\s]?[34o]|chatgpt|claude|llama[-\s]?\d|gemini|gemma|mistral|"
    r"phi[-\s]?\d|qwen|deepseek|palm|bard|vicuna|alpaca|falcon|bloom|"
    r"language model(?:s)?)\b",
    re.IGNORECASE,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_paper_frontmatter(filename: str) -> str:
    """Return raw YAML frontmatter string from papers/<filename>."""
    path = PAPERS_DIR / filename
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    if end == -1:
        return text
    return text[3:end]


def read_extract(filename: str) -> str:
    """Return first EXTRACT_CHARS of the PDF extract for the given paper filename."""
    # Derive extract path: papers/YYYY-Author-Title.md -> PDF Extracts/YYYY/YYYY-Author-Title.md
    stem = filename  # e.g. "2025-Wu-CVC.md"
    # Extract year from filename
    m = re.match(r"^(\d{4})-", stem)
    if m:
        year = m.group(1)
    else:
        year = "0000"
    extract_path = EXTRACTS_DIR / year / stem
    if not extract_path.exists():
        # Try looking across all year subdirs
        for ydir in EXTRACTS_DIR.iterdir():
            if ydir.is_dir():
                candidate = ydir / stem
                if candidate.exists():
                    extract_path = candidate
                    break
        else:
            return ""
    text = extract_path.read_text(encoding="utf-8", errors="replace")
    return text[:EXTRACT_CHARS]


def yaml_field(fm: str, key: str) -> str:
    """Extract a single YAML field value from frontmatter string using regex."""
    m = re.search(rf'^{re.escape(key)}:\s*"?(.*?)"?\s*$', fm, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"')
    return ""


def yaml_field_int(fm: str, key: str) -> int | None:
    """Extract an integer YAML field."""
    val = yaml_field(fm, key)
    if val:
        try:
            return int(val)
        except ValueError:
            return None
    return None


def count_countries(text: str) -> tuple[list[str], int]:
    """Count distinct country names mentioned in text. Returns (list, count)."""
    found = set()
    text_lower = text.lower()
    for country in COUNTRIES:
        if country.lower() in text_lower:
            found.add(country)
    for alias, canonical in COUNTRY_ALIASES.items():
        if alias.lower() in text_lower:
            found.add(canonical)
    return sorted(found), len(found)


def count_languages(text: str) -> int:
    """Count distinct language names mentioned."""
    found = set()
    text_lower = text.lower()
    for lang in LANGUAGES:
        if lang.lower() in text_lower:
            found.add(lang)
    return len(found)


def detect_format_type(text: str) -> str | None:
    """Keyword scan for format types."""
    text_lower = text.lower()
    # Priority order - more specific first
    format_kws = [
        ("vignette", r"\bvignette"),
        ("scenario", r"\bscenario"),
        ("dilemma", r"\b(?:dilemma|trolley)"),
        ("survey", r"\bsurvey\b"),
        ("questionnaire", r"\bquestionnaire"),
        ("ranking", r"\branking\b"),
        ("pairwise", r"\bpairwise\b"),
        ("annotation", r"\bannotat"),
        ("game", r"\b(?:game|economic game|dictator game|ultimatum game|prisoners dilemma)"),
        ("likert", r"\blikert\b"),
    ]
    detected = []
    for label, pattern in format_kws:
        if re.search(pattern, text_lower):
            detected.append(label)
    if detected:
        return detected[0]  # Primary format
    return None


def detect_response_format(text: str) -> str | None:
    """Keyword scan for response format."""
    text_lower = text.lower()
    resp_kws = [
        ("Likert", r"\blikert\b"),
        ("forced_choice", r"\bforced.?choice\b"),
        ("multiple_choice", r"\bmultiple.?choice\b"),
        ("open_ended", r"\b(?:open.?ended|free.?response|free.?text)\b"),
        ("pairwise", r"\bpairwise\b"),
        ("binary", r"\b(?:yes/no|true/false|binary)\b"),
    ]
    for label, pattern in resp_kws:
        if re.search(pattern, text_lower):
            return label
    return None


def detect_likert_points(text: str) -> int | None:
    """Regex for N-point Likert scale."""
    m = re.search(r"(\d)[- ]point\s*(?:likert|scale)", text, re.IGNORECASE)
    if m:
        return int(m.group(1))
    m = re.search(r"likert[- ](\d)", text, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None


def detect_item_count(text: str) -> int | None:
    """Regex for item/question/scenario count."""
    # Look for patterns like "150 items", "30 scenarios", etc.
    patterns = [
        r"(\d{1,6})\s*(?:items|questions|scenarios|prompts|vignettes|dilemmas|"
        r"examples|instances|test cases|stimuli|situations|stories|moral dilemmas|"
        r"value rules|entries|samples|data points|pairs|problems)",
    ]
    candidates = []
    for pat in patterns:
        for m in re.finditer(pat, text, re.IGNORECASE):
            val = int(m.group(1))
            # Filter out implausibly small or very large numbers
            if 5 <= val <= 999_999:
                candidates.append(val)
    if candidates:
        # Return the most common or largest plausible count
        return max(candidates)
    return None


def detect_subscale_count(text: str) -> int | None:
    """Regex for subscale/dimension/factor count."""
    m = re.search(
        r"(\d{1,3})\s*(?:subscales?|dimensions?|factors?|categories|domains|pillars|axes)",
        text, re.IGNORECASE,
    )
    if m:
        val = int(m.group(1))
        if 2 <= val <= 100:
            return val
    return None


def detect_sample_size(text: str) -> int | None:
    """Regex for total sample size."""
    patterns = [
        r"(\d[\d,]*)\s*(?:participants|respondents|annotators|raters|subjects|"
        r"samples|responses|people|individuals|workers|crowd.?workers|human judges)",
    ]
    candidates = []
    for pat in patterns:
        for m_hit in re.finditer(pat, text, re.IGNORECASE):
            val_str = m_hit.group(1).replace(",", "")
            try:
                val = int(val_str)
                if 10 <= val <= 10_000_000:
                    candidates.append(val)
            except ValueError:
                continue
    if candidates:
        return max(candidates)
    return None


def detect_cultural_scope(countries_found: list[str], text: str) -> str:
    """Classify cultural scope based on country count and keywords."""
    n = len(countries_found)
    text_lower = text.lower()
    if "universal" in text_lower and ("value" in text_lower or "moral" in text_lower):
        return "universal_claim"
    if n > 3:
        return "multicultural"
    if n >= 2:
        return "bicultural"
    if n == 1:
        return "culture_specific"
    # Check for culture keywords even without country names
    if re.search(r"\bcross[- ]?cultur", text_lower):
        return "multicultural"
    if re.search(r"\bmulti[- ]?cultur", text_lower):
        return "multicultural"
    return "monocultural"


def detect_primary_theory(text: str, nw_scores: dict[str, int]) -> str | None:
    """Detect primary theoretical framework."""
    text_lower = text.lower()
    scores: dict[str, int] = {}
    for label, pattern in NW_FRAMEWORKS:
        matches = len(re.findall(pattern, text_lower))
        if matches > 0:
            scores[label] = matches
    # Also check nw_scores from YAML for high-scoring frameworks
    nw_map = {
        "nw_confucian": "Confucian",
        "nw_ubuntu": "Ubuntu",
        "nw_islamic_ethics": "Islamic Ethics",
        "nw_buddhist": "Buddhist",
        "nw_dharmic": "Dharmic",
        "nw_indigenous_relational": "Indigenous",
        "nw_buen_vivir": "Buen Vivir",
    }
    for field, label in nw_map.items():
        val = nw_scores.get(field, 0)
        if val >= 50:
            scores[label] = scores.get(label, 0) + 10  # Strong bonus
    if scores:
        return max(scores, key=scores.get)
    return None


def count_nw_frameworks(nw_scores: dict[str, int]) -> int:
    """Count non-western frameworks with score >= 20."""
    return sum(1 for v in nw_scores.values() if v >= 20)


def detect_reliability(text: str) -> bool:
    """Check if reliability measures are reported."""
    return bool(re.search(
        r"\b(?:cronbach|alpha\s*=|reliability|icc\b|inter[- ]?rater|cohen.s kappa|"
        r"test[- ]?retest|internal consistency|split[- ]?half)\b",
        text, re.IGNORECASE,
    ))


def detect_measurement_invariance(text: str) -> str | None:
    """Detect measurement invariance level."""
    text_lower = text.lower()
    if "scalar invariance" in text_lower or "scalar equivalence" in text_lower:
        return "scalar"
    if "metric invariance" in text_lower or "metric equivalence" in text_lower:
        return "metric"
    if "configural invariance" in text_lower or "configural equivalence" in text_lower:
        return "configural"
    if "measurement invariance" in text_lower or "measurement equivalence" in text_lower:
        return "mentioned"
    return None


def detect_llm_administrable(format_type: str | None, item_count: int | None) -> str:
    """Determine if benchmark is LLM-administrable."""
    text_formats = {"vignette", "scenario", "dilemma", "survey", "questionnaire",
                    "ranking", "pairwise", "likert", "annotation"}
    if format_type and format_type in text_formats:
        if item_count is not None and item_count <= 200:
            return "yes"
        if item_count is not None and item_count > 200:
            return "partial"
        return "likely"
    if format_type == "game":
        return "partial"
    return "unknown"


def detect_human_baseline(text: str) -> bool:
    """Check for human baseline availability."""
    return bool(re.search(
        r"\b(?:human baseline|human performance|human evaluation|human annotator|"
        r"human judge|human rater|human agreement|human accuracy|human benchmark|"
        r"gold standard|expert annotation|ground truth)\b",
        text, re.IGNORECASE,
    ))


def detect_prior_llm_testing(text: str) -> bool:
    """Check for prior LLM testing/assessment."""
    return bool(LLM_NAMES_RE.search(text))


def detect_data_availability(data_url: str) -> str:
    """Classify data availability from DATA_URL field."""
    if not data_url:
        return "unavailable"
    url_lower = data_url.lower()
    if any(s in url_lower for s in ["github.com", "huggingface", "zenodo", "kaggle",
                                      "figshare", "dataverse", "osf.io", "gitlab"]):
        return "open_source"
    if any(s in url_lower for s in ["drive.google", "dropbox", "request", "email"]):
        return "upon_request"
    return "available"


def detect_creator_region(fm: str) -> str | None:
    """Detect creator region from author_region field in frontmatter."""
    region = yaml_field(fm, "author_region")
    if region:
        return region
    country = yaml_field(fm, "author_country")
    if country:
        return country
    return None


def detect_non_english_primary(fm: str, text: str) -> bool:
    """Check if the primary language is non-English."""
    langs_list = yaml_field(fm, "languages_list")
    if langs_list:
        # If first listed language is not English
        first_lang = langs_list.split(",")[0].strip().lower()
        if first_lang and first_lang != "english":
            return True
    # Check title for non-English language indicators
    title = yaml_field(fm, "short_title")
    ne_indicators = ["chinese", "arabic", "korean", "japanese", "hindi", "urdu",
                     "french", "german", "spanish", "portuguese", "russian",
                     "turkish", "persian", "thai", "vietnamese", "indonesian",
                     "malay", "swahili", "hebrew", "tamil", "telugu"]
    title_lower = title.lower()
    for indicator in ne_indicators:
        if indicator in title_lower:
            return True
    return False


# ---------------------------------------------------------------------------
# Main extraction
# ---------------------------------------------------------------------------

def extract_features(
    candidate: dict,
    fm: str,
    extract_text: str,
) -> dict:
    """Extract all auto-extractable benchmark features for a single paper."""
    combined_text = fm + "\n" + extract_text
    nw_scores = candidate.get("nw_scores", {})

    features: dict = {}

    # --- Dimension 1: Format ---
    features["F1_format_type"] = detect_format_type(combined_text)
    features["F2_response_format"] = detect_response_format(combined_text)
    features["F3_likert_points"] = detect_likert_points(combined_text)
    features["F4_item_count"] = detect_item_count(combined_text)
    features["F5_time_to_complete"] = None
    features["F6_stimulus_modality"] = None
    features["F7_scoring_method"] = None
    features["F8_subscale_count"] = detect_subscale_count(combined_text)

    # --- Dimension 2: Cultural ---
    countries_found, countries_count = count_countries(combined_text)
    features["C1_cultural_scope"] = detect_cultural_scope(countries_found, combined_text)
    features["C2_cultural_framework"] = None
    features["C3_countries_count"] = countries_count if countries_count > 0 else None
    features["C4_countries_list"] = countries_found if countries_found else None
    features["C5_global_south_included"] = any(c in GLOBAL_SOUTH_COUNTRIES for c in countries_found)
    # Use extract_text only (not combined_text) to avoid false positives from
    # YAML field names like "nw_indigenous_relational"
    features["C6_indigenous_included"] = any(
        kw in extract_text.lower() for kw in INDIGENOUS_KEYWORDS
    )
    features["C7_emic_etic_approach"] = None
    features["C8_cultural_adaptation_method"] = None

    # --- Dimension 3: Language ---
    langs_count = count_languages(combined_text)
    l1_yaml = yaml_field(fm, "languages_list")
    # regex for "N languages"
    m_lang = re.search(r"(\d+)\s*languages?", combined_text, re.IGNORECASE)
    yaml_lang_count = len([x.strip() for x in l1_yaml.split(",") if x.strip()]) if l1_yaml else 0
    regex_lang_count = int(m_lang.group(1)) if m_lang else 0
    features["L1_languages_count"] = max(langs_count, yaml_lang_count, regex_lang_count) or None
    features["L2_languages_list"] = l1_yaml if l1_yaml else None
    features["L3_translation_method"] = None
    features["L4_translation_validation"] = None
    features["L5_non_english_primary"] = detect_non_english_primary(fm, combined_text)

    # --- Dimension 4: Population ---
    features["P1_total_sample_size"] = detect_sample_size(combined_text)
    features["P2_sample_demographics"] = None
    features["P3_expert_vs_crowd"] = None
    features["P4_age_range"] = None
    features["P5_education_level"] = None

    # --- Dimension 5: Theory ---
    features["T1_primary_theory"] = detect_primary_theory(combined_text, nw_scores)
    features["T2_theory_adaptation"] = None
    features["T3_western_framework_count"] = None
    nw_count = count_nw_frameworks(nw_scores)
    features["T4_nonwestern_framework_count"] = nw_count if nw_count > 0 else None
    features["T5_theoretical_integration"] = None

    # --- Dimension 6: Psychometric ---
    features["Q1_reliability_reported"] = detect_reliability(combined_text)
    features["Q2_validity_evidence"] = None
    features["Q3_factor_structure"] = None
    features["Q4_cross_cultural_validity"] = None
    features["Q5_measurement_invariance_level"] = detect_measurement_invariance(combined_text)

    # --- Dimension 7: Ecological ---
    features["V1_ecological_validity"] = None
    features["V2_real_world_scenarios"] = None
    features["V3_context_specificity"] = None

    # --- Dimension 8: LLM ---
    features["A1_llm_administrable"] = detect_llm_administrable(
        features["F1_format_type"], features["F4_item_count"]
    )
    features["A2_input_format"] = None
    features["A3_output_parsing"] = None
    features["A4_prompt_sensitivity"] = None
    features["A5_human_baseline_available"] = detect_human_baseline(combined_text)
    features["A6_prior_llm_testing"] = detect_prior_llm_testing(combined_text)

    # --- Dimension 9: Data ---
    data_url = candidate.get("data_url", "")
    features["R1_data_availability"] = detect_data_availability(data_url)
    features["R2_license_type"] = None
    features["R3_data_url"] = data_url if data_url else None

    # --- Dimension 10: Temporal ---
    features["D1_year_published"] = yaml_field(fm, "year") or None
    features["D2_last_updated"] = None
    features["D3_version"] = None

    # --- Dimension 11: Scope ---
    features["S1_ethical_domain"] = None
    features["S2_application_context"] = None
    features["S3_target_population"] = None

    # --- Dimension 12: Methodology ---
    features["M1_development_method"] = None
    features["M2_pilot_testing"] = None
    features["M3_iterative_refinement"] = None

    # --- Dimension 13: Provenance ---
    features["E1_creator_region"] = detect_creator_region(fm)
    features["E2_creator_institution"] = None
    features["E3_funding_source"] = None

    # Null placeholder features to reach 96 total (60 named + 36 reserved)
    # Dimensions 14-16 (reserved for future expansion)
    for i in range(1, 37):
        features[f"X{i}_reserved"] = None

    return features


def count_extracted(features: dict) -> int:
    """Count non-null features."""
    return sum(1 for v in features.values() if v is not None and v != "" and v is not False)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print(f"Loading candidates from {CANDIDATES_PATH}")
    with open(CANDIDATES_PATH) as f:
        data = json.load(f)

    candidates = data["candidates"]
    # Filter to top N by relevance_score (already sorted descending)
    top = [c for c in candidates if c["relevance_score"] >= MIN_SCORE][:TOP_N]
    print(f"Processing top {len(top)} candidates (score >= {MIN_SCORE})")

    results = []
    total_extracted = 0
    feature_counts: Counter = Counter()
    format_dist: Counter = Counter()
    scope_dist: Counter = Counter()
    llm_admin_dist: Counter = Counter()
    data_avail_dist: Counter = Counter()
    theory_dist: Counter = Counter()
    extract_found = 0
    fm_found = 0

    for i, cand in enumerate(top):
        filename = cand["filename"]
        fm = read_paper_frontmatter(filename)
        if fm:
            fm_found += 1
        extract = read_extract(filename)
        if extract:
            extract_found += 1

        features = extract_features(cand, fm, extract)
        n_extracted = count_extracted(features)
        total_extracted += n_extracted

        # Track distributions
        if features["F1_format_type"]:
            format_dist[features["F1_format_type"]] += 1
        scope_dist[features["C1_cultural_scope"]] += 1
        llm_admin_dist[features["A1_llm_administrable"]] += 1
        data_avail_dist[features["R1_data_availability"]] += 1
        if features["T1_primary_theory"]:
            theory_dist[features["T1_primary_theory"]] += 1

        # Track per-feature extraction rates
        for k, v in features.items():
            if v is not None and v != "" and v is not False:
                feature_counts[k] += 1

        results.append({
            "filename": filename,
            "short_title": cand.get("short_title", ""),
            "relevance_score": cand["relevance_score"],
            "features": features,
            "extraction_notes": f"auto-extracted {n_extracted}/96 features",
        })

        if (i + 1) % 50 == 0:
            print(f"  Processed {i + 1}/{len(top)} papers...")

    avg_extracted = total_extracted / len(top) if top else 0
    total_features = len(results[0]["features"]) if results else 0

    # Count how many distinct features were auto-extracted at least once
    auto_extracted_distinct = len(feature_counts)

    output = {
        "metadata": {
            "date": "2026-04-04",
            "papers_scored": len(top),
            "features_per_paper": total_features,
            "auto_extracted_features": auto_extracted_distinct,
            "null_features": total_features - auto_extracted_distinct,
            "avg_features_per_paper": round(avg_extracted, 1),
            "frontmatter_found": fm_found,
            "extracts_found": extract_found,
        },
        "feature_extraction_rates": {
            k: v for k, v in sorted(feature_counts.items(), key=lambda x: -x[1])
        },
        "distributions": {
            "format_type": dict(format_dist.most_common()),
            "cultural_scope": dict(scope_dist.most_common()),
            "llm_administrable": dict(llm_admin_dist.most_common()),
            "data_availability": dict(data_avail_dist.most_common()),
            "primary_theory": dict(theory_dist.most_common()),
        },
        "papers": results,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False, default=str)
    print(f"\nOutput written to {OUTPUT_PATH}")

    # ---------------------------------------------------------------------------
    # Summary stats
    # ---------------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("BENCHMARK FEATURE EXTRACTION - SUMMARY")
    print("=" * 70)
    print(f"Papers scored:          {len(top)}")
    print(f"Frontmatter found:      {fm_found}/{len(top)}")
    print(f"PDF extracts found:     {extract_found}/{len(top)}")
    print(f"Total feature slots:    {total_features} per paper")
    print(f"Distinct features auto-extracted (at least once): {auto_extracted_distinct}")
    print(f"Average features per paper: {avg_extracted:.1f}")
    print()

    print("--- Feature Extraction Rates (top 25) ---")
    for k, v in sorted(feature_counts.items(), key=lambda x: -x[1])[:25]:
        pct = v / len(top) * 100
        print(f"  {k:40s} {v:4d} ({pct:5.1f}%)")

    print()
    print("--- Format Type Distribution ---")
    for k, v in format_dist.most_common():
        print(f"  {k:20s} {v:4d}")

    print()
    print("--- Cultural Scope Distribution ---")
    for k, v in scope_dist.most_common():
        print(f"  {k:20s} {v:4d}")

    print()
    print("--- LLM Administrability ---")
    for k, v in llm_admin_dist.most_common():
        print(f"  {k:20s} {v:4d}")

    print()
    print("--- Data Availability ---")
    for k, v in data_avail_dist.most_common():
        print(f"  {k:20s} {v:4d}")

    print()
    print("--- Primary Theory (top 15) ---")
    for k, v in theory_dist.most_common(15):
        print(f"  {k:20s} {v:4d}")

    # Highlight high-value candidates
    print()
    print("--- Top 10 Richest Extractions ---")
    sorted_results = sorted(results, key=lambda r: -count_extracted(r["features"]))
    for r in sorted_results[:10]:
        n = count_extracted(r["features"])
        print(f"  {r['filename']:60s} {n:3d}/96  (rel={r['relevance_score']})")

    print()
    print("--- Global South Coverage ---")
    gs_count = sum(1 for r in results if r["features"]["C5_global_south_included"])
    print(f"  Papers with Global South countries: {gs_count}/{len(top)} ({gs_count/len(top)*100:.1f}%)")

    print()
    print("--- Indigenous Coverage ---")
    ind_count = sum(1 for r in results if r["features"]["C6_indigenous_included"])
    print(f"  Papers mentioning indigenous: {ind_count}/{len(top)} ({ind_count/len(top)*100:.1f}%)")

    print()
    print("--- Non-English Primary ---")
    ne_count = sum(1 for r in results if r["features"]["L5_non_english_primary"])
    print(f"  Papers with non-English primary: {ne_count}/{len(top)} ({ne_count/len(top)*100:.1f}%)")

    print()
    print("--- Reliability Reported ---")
    rel_count = sum(1 for r in results if r["features"]["Q1_reliability_reported"])
    print(f"  Papers reporting reliability: {rel_count}/{len(top)} ({rel_count/len(top)*100:.1f}%)")

    print()
    print("--- Prior LLM Testing ---")
    llm_count = sum(1 for r in results if r["features"]["A6_prior_llm_testing"])
    print(f"  Papers with prior LLM testing: {llm_count}/{len(top)} ({llm_count/len(top)*100:.1f}%)")

    print("\nDone.")


if __name__ == "__main__":
    main()
