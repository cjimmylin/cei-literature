#!/usr/bin/env python3
"""
Phase 3: Build Religious Values Benchmark Feature Matrix

Reads Phase 1 candidates + Phase 2 external results, enriches with PDF extract
data, and constructs a feature matrix with 3-axis scoring:
  - RD: Religious/Theological Depth (40%)
  - PE: Practical Ease (35%)
  - CI: Citation Impact (25%)

Each candidate is scored on R1-R6 (depth), P1-P10 (ease), C1-C6 (impact) axes.

Output: RELIGIOUS-VALUES/data/YYYYMMDD-religious-benchmark-feature-matrix.json
        RELIGIOUS-VALUES/data/YYYYMMDD-format-taxonomy.json
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
WS_ROOT = PROJECT_DIR.parent
PAPERS_DIR = WS_ROOT / "papers"
EXTRACTS_DIR = WS_ROOT / "PDF Extracts"
DATA_DIR = PROJECT_DIR / "data"

TODAY = date.today().strftime("%Y%m%d")

# ---------------------------------------------------------------------------
# Format Taxonomy
# ---------------------------------------------------------------------------
FORMAT_TAXONOMY = {
    "MCQ": {"name": "Multiple Choice", "description": "Fixed answer choices (A/B/C/D)", "harness_compat": "high"},
    "MRC": {"name": "Machine Reading Comprehension", "description": "Extract answer from passage", "harness_compat": "high"},
    "BIN": {"name": "Binary Classification", "description": "Yes/No, Halal/Haram, True/False", "harness_compat": "high"},
    "SCN": {"name": "Scenario-based", "description": "Present dilemma, evaluate response quality", "harness_compat": "medium"},
    "OPN": {"name": "Open-ended Generation", "description": "Free-text theological response", "harness_compat": "low"},
    "PSY": {"name": "Psychometric/Survey", "description": "Likert or forced-choice value statements", "harness_compat": "medium"},
    "MTN": {"name": "Multi-turn Dialogue", "description": "Conversational theological engagement", "harness_compat": "low"},
    "RAG": {"name": "Retrieval-Augmented", "description": "Retrieval from sacred texts + generation", "harness_compat": "low"},
    "TXT": {"name": "Text Classification", "description": "Classify passages by tradition/theme", "harness_compat": "high"},
    "MUL": {"name": "Multimodal", "description": "Visual + text (religious imagery, calligraphy)", "harness_compat": "low"},
    "SHT": {"name": "Shared Task", "description": "Competition format with train/dev/test splits", "harness_compat": "high"},
    "MIX": {"name": "Mixed Format", "description": "Multiple formats combined", "harness_compat": "medium"},
}

# ---------------------------------------------------------------------------
# Tradition and family definitions
# ---------------------------------------------------------------------------
TRADITION_FAMILY = {
    "Islam": "Abrahamic", "Christianity": "Abrahamic", "Judaism": "Abrahamic",
    "Hinduism": "Dharmic", "Buddhism": "Dharmic", "Jainism": "Dharmic", "Sikhism": "Dharmic",
    "Confucianism": "East Asian", "Taoism": "East Asian", "Shinto": "East Asian",
    "Ubuntu Philosophy": "African/Indigenous", "Indigenous Spirituality": "African/Indigenous",
    "Baha'i": "Other", "Zoroastrianism": "Other",
}

# ---------------------------------------------------------------------------
# Format detection heuristics
# ---------------------------------------------------------------------------
FORMAT_KEYWORDS = {
    "MCQ": ["multiple choice", "multiple-choice", "mcq", "4 choices", "four choices", "a/b/c/d", "answer options"],
    "MRC": ["reading comprehension", "extractive", "span extraction", "passage-based"],
    "BIN": ["binary", "yes/no", "true/false", "halal/haram", "permissible/forbidden", "classification"],
    "SCN": ["scenario", "dilemma", "vignette", "moral scenario", "ethical dilemma", "case study"],
    "OPN": ["open-ended", "free-form", "generation", "essay", "open response"],
    "PSY": ["psychometric", "likert", "survey", "questionnaire", "forced choice", "scale", "typology"],
    "MTN": ["multi-turn", "dialogue", "conversation", "chat", "counseling"],
    "RAG": ["retrieval", "rag", "retrieval-augmented", "knowledge base"],
    "TXT": ["text classification", "topic classification", "sentiment", "categorization"],
    "MUL": ["multimodal", "image", "visual", "audio", "calligraphy"],
    "SHT": ["shared task", "competition", "semeval", "track"],
}


def detect_format(title: str, abstract: str, data_desc: str) -> str:
    """Detect benchmark format from text content."""
    text = f"{title} {abstract} {data_desc}".lower()
    scores = {}
    for fmt, keywords in FORMAT_KEYWORDS.items():
        scores[fmt] = sum(1 for kw in keywords if kw in text)

    if not any(scores.values()):
        return "MIX"  # default

    # Return highest-scoring format
    best = max(scores, key=scores.get)
    if scores[best] > 0:
        return best
    return "MIX"


# ---------------------------------------------------------------------------
# Dataset size extraction
# ---------------------------------------------------------------------------
SIZE_PATTERNS = [
    (r'(\d{1,3}(?:,\d{3})+)\s*(?:questions|items|examples|samples|instances|entries|scenarios|pairs|cases)', lambda m: int(m.group(1).replace(",", ""))),
    (r'(\d+)\s*(?:questions|items|examples|samples|instances|entries|scenarios|pairs|cases)', lambda m: int(m.group(1))),
    (r'(\d+)k\s*(?:questions|items|examples|samples)', lambda m: int(m.group(1)) * 1000),
    (r'dataset\s*(?:of|with|containing)\s*(\d{1,3}(?:,\d{3})+)', lambda m: int(m.group(1).replace(",", ""))),
    (r'dataset\s*(?:of|with|containing)\s*(\d+)', lambda m: int(m.group(1))),
    (r'(\d+)\s*test\s*cases', lambda m: int(m.group(1))),
]


def extract_dataset_size(title: str, abstract: str, data_desc: str, data_metrics: str) -> int:
    """Try to extract dataset size from text."""
    for text in [data_metrics, data_desc, abstract, title]:
        if not text:
            continue
        for pattern, extractor in SIZE_PATTERNS:
            m = re.search(pattern, text.lower())
            if m:
                try:
                    size = extractor(m)
                    if 1 < size < 10_000_000:  # sanity bounds
                        return size
                except Exception:
                    pass
    return 0


# ---------------------------------------------------------------------------
# Theological depth scoring (R-axis)
# ---------------------------------------------------------------------------
THEOLOGICAL_DEPTH_KEYWORDS = {
    5: ["fiqh", "jurisprudence", "exegesis", "hermeneutic", "systematic theology",
        "catechism", "abhidharma", "halakha", "usul al-fiqh"],
    4: ["scripture", "scriptural", "doctrine", "doctrinal", "theological reasoning",
        "biblical scholarship", "quranic studies", "talmudic", "vedantic"],
    3: ["theology", "theological", "sacred text", "religious knowledge",
        "spiritual values", "faith benchmark"],
    2: ["religious values", "moral values", "ethical reasoning", "interfaith",
        "religious bias", "cultural values"],
    1: ["religion", "religious", "faith", "belief", "worship"],
}

SCRIPTURAL_REFS = {
    "quran": 5, "qur'an": 5, "quranic": 5, "bible": 5, "biblical": 5,
    "torah": 5, "talmud": 5, "vedas": 5, "vedic": 5, "upanishad": 5,
    "bhagavad gita": 5, "guru granth": 5, "gurbani": 5, "tripitaka": 5,
    "pali canon": 5, "analects": 5, "tao te ching": 5, "daodejing": 5,
    "hadith": 4, "sunnah": 4, "midrash": 4, "gospel": 3, "sutra": 3,
    "psalm": 3, "proverb": 3, "genesis": 3, "revelation": 3,
}

DENOMINATIONAL_KEYWORDS = {
    "sunni": True, "shia": True, "shiite": True, "sufi": True, "salafi": True,
    "catholic": True, "protestant": True, "orthodox": True, "evangelical": True,
    "reformed": True, "lutheran": True, "baptist": True, "methodist": True,
    "theravada": True, "mahayana": True, "vajrayana": True, "zen": True,
    "hasidic": True, "orthodox jewish": True, "reform jewish": True,
    "vaishnava": True, "shaiva": True, "shakta": True,
    "khalsa": True, "nanaksar": True,
}


def score_theological_depth(title: str, abstract: str, data_desc: str,
                            traditions: list, nw_scores: dict,
                            candidate_classification: str = "",
                            languages_list: str = "") -> dict:
    """Score R1-R6 theological depth axes."""
    text = f"{title} {abstract} {data_desc}".lower()

    # R1: Traditions tested (count)
    r1_count = len(traditions)
    r1_traditions = {t["tradition"]: t["score"] for t in traditions}

    # R2: Depth of theological engagement (1-5)
    #
    # Strategy: combine classification anchor, keyword counting (requiring >=2
    # hits at a depth level to earn that level), and title boosting.
    title_lower = title.lower()
    classification = candidate_classification if candidate_classification else ""

    # Count keyword hits at each depth level, weighting title matches 2x
    depth_hits: dict[int, float] = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for depth_level, keywords in THEOLOGICAL_DEPTH_KEYWORDS.items():
        for kw in keywords:
            if kw in title_lower:
                depth_hits[depth_level] += 2  # title match counts double
            elif kw in text:
                depth_hits[depth_level] += 1

    # Determine highest depth level with at least 2 weighted hits
    r2_score = 1
    for depth_level in sorted(depth_hits.keys(), reverse=True):
        if depth_hits[depth_level] >= 2:
            r2_score = depth_level
            break

    # Classification-based floor: anchors prevent collapse to 1
    if classification == "theological":
        r2_score = max(r2_score, 3)
    elif classification == "theological-values":
        r2_score = max(r2_score, 2)

    # R3: Scriptural references (0-5)
    r3_score = 0
    for ref, score in SCRIPTURAL_REFS.items():
        if ref in text:
            r3_score = max(r3_score, score)

    # R3 source-language bonus: +1 if the benchmark processes scripture in its
    # original liturgical language rather than English translations.
    # Recognized source languages: Arabic (Quran/Hadith), Sanskrit (Vedas/Gita),
    # Hebrew (Torah/Talmud), Pali (Tripitaka), Classical Chinese (Analects/Tao Te Ching).
    SOURCE_LANG_KEYWORDS = [
        "arabic",       # Quran, Hadith
        "sanskrit",     # Vedas, Bhagavad Gita, Upanishads
        "hebrew",       # Torah, Talmud
        "pali",         # Tripitaka, Pali Canon
        "classical chinese",  # Analects, Tao Te Ching
    ]
    lang_field = (languages_list or "").lower()
    # Check both the language field and the text for source-language indicators
    if any(sl in lang_field for sl in SOURCE_LANG_KEYWORDS) or any(
            sl in text for sl in SOURCE_LANG_KEYWORDS):
        r3_score = min(5, r3_score + 1)

    # R4: Denominational distinction (0-3)
    denom_hits = sum(1 for kw in DENOMINATIONAL_KEYWORDS if kw in text)
    r4_score = min(3, denom_hits)

    # R5: Pluralism (0-5) - tests multiple perspectives
    r5_score = 0
    if r1_count >= 5:
        r5_score = 5
    elif r1_count >= 3:
        r5_score = 4
    elif r1_count >= 2:
        r5_score = 3
    elif r1_count == 1 and denom_hits >= 2:
        r5_score = 2
    elif r1_count == 1:
        r5_score = 1

    # R6: Expert grounding (0-5) — heuristic based on venue and author signals
    r6_score = 2  # default: unknown
    if any(kw in text for kw in ["peer-review", "expert-reviewed", "theologian", "religious scholar",
                                  "seminary", "divinity", "religious studies"]):
        r6_score = 4
    elif any(kw in text for kw in ["expert", "domain expert", "annotator"]):
        r6_score = 3
    # NW scores boost
    if max(nw_scores.values(), default=0) >= 80:
        r6_score = max(r6_score, 3)

    return {
        "R1_traditions": r1_traditions,
        "R1_count": r1_count,
        "R2_depth": r2_score,
        "R3_scriptural": r3_score,
        "R4_denominational": r4_score,
        "R5_pluralism": r5_score,
        "R6_grounding": r6_score,
    }


def compute_rd_score(rd: dict) -> float:
    """Compute Religious/Theological Depth composite score (0-100)."""
    # Normalize each sub-score to 0-100
    r1_norm = min(100, rd["R1_count"] * 20)  # 5+ traditions = 100
    r2_norm = (rd["R2_depth"] / 5) * 100
    r3_norm = (rd["R3_scriptural"] / 5) * 100
    r4_norm = (rd["R4_denominational"] / 3) * 100
    r5_norm = (rd["R5_pluralism"] / 5) * 100
    r6_norm = (rd["R6_grounding"] / 5) * 100

    # Weighted composite (matches plan weights)
    return round(
        r1_norm * 0.15 +
        r2_norm * 0.25 +
        r3_norm * 0.15 +
        r4_norm * 0.10 +
        r5_norm * 0.15 +
        r6_norm * 0.20
    , 1)


# ---------------------------------------------------------------------------
# Practical ease scoring (P-axis)
# ---------------------------------------------------------------------------
def score_practical_ease(candidate: dict) -> dict:
    """Score P1-P10 practical ease axes."""
    data_url = candidate.get("DATA_URL", "")
    is_available = bool(data_url and data_url.lower() not in ("na", "n/a", ""))

    # P1: Format
    fmt = detect_format(
        candidate.get("short_title", ""),
        candidate.get("abstract", ""),
        candidate.get("data_description", ""),
    )

    # P2: Dataset size
    size = extract_dataset_size(
        candidate.get("short_title", ""),
        candidate.get("abstract", ""),
        candidate.get("data_description", ""),
        candidate.get("data_metrics", ""),
    )

    # P3: Data availability
    p3_availability = "Not available"
    p3_url = data_url
    if data_url:
        url_lower = data_url.lower()
        if "github" in url_lower:
            p3_availability = "GitHub"
        elif "huggingface" in url_lower:
            p3_availability = "HuggingFace"
        elif "gitlab" in url_lower:
            p3_availability = "GitLab"
        elif "kaggle" in url_lower:
            p3_availability = "Kaggle"
        elif "zenodo" in url_lower or "osf" in url_lower:
            p3_availability = "Archive"
        elif url_lower.startswith("http"):
            p3_availability = "Website"

    # P5: License (heuristic from source)
    license_val = "Unspecified"
    if "github" in (data_url or "").lower():
        license_val = "Likely Open Source"
    elif "huggingface" in (data_url or "").lower():
        license_val = "Likely Open Source"

    # P7: Implementability composite (0-10)
    p7_score = 0.0
    if is_available:
        p7_score += 3.0
    if fmt in ("MCQ", "MRC", "BIN", "TXT", "SHT"):
        p7_score += 2.5
    elif fmt in ("SCN", "PSY", "MIX"):
        p7_score += 1.5
    else:
        p7_score += 0.5
    if size >= 100:
        p7_score += 1.5
    elif size >= 10:
        p7_score += 0.5
    if candidate.get("LLM_assessed") and candidate["LLM_assessed"].lower() not in ("na", ""):
        p7_score += 1.5
    if p3_availability in ("GitHub", "HuggingFace", "GitLab"):
        p7_score += 1.0

    p7_score = min(10.0, p7_score)

    # P9: Model compatibility
    llm_str = (candidate.get("LLM_assessed", "") or "").lower()
    if any(m in llm_str for m in ["gpt", "claude", "gemini"]) and any(m in llm_str for m in ["llama", "mistral", "phi"]):
        p9_compat = "Both"
    elif any(m in llm_str for m in ["gpt", "claude", "gemini"]):
        p9_compat = "Closed-only"
    elif any(m in llm_str for m in ["llama", "mistral", "phi", "bert"]):
        p9_compat = "Open-only"
    else:
        p9_compat = "Unknown"

    # P10: Language
    languages = candidate.get("languages_list", "")

    return {
        "P1_format": fmt,
        "P2_dataset_size": size,
        "P3_data_availability": p3_availability,
        "P3_url": p3_url,
        "P4_code_availability": "Unknown",  # would need paper reading
        "P5_license": license_val,
        "P7_implementability": round(p7_score, 1),
        "P8_scorer_type": "Unknown",
        "P9_model_compat": p9_compat,
        "P10_language": languages,
    }


def compute_pe_score(pe: dict) -> float:
    """Compute Practical Ease composite score (0-100).

    Combines six sub-features with the following weights:
      P7 implementability (0-10 -> 0-100)  30%
      P3 data availability                  25%
      P9 model compatibility                15%
      P10 language                          10%
      P5 license                            10%
      P4 code availability                  10%
    """
    # P7: primary driver (0-10 scale, normalize to 0-100)
    p7_norm = pe["P7_implementability"] * 10

    # P3: data availability
    p3_map = {
        "GitHub": 90, "HuggingFace": 85, "GitLab": 80,
        "Kaggle": 75, "Archive": 70, "Website": 50,
        "Not available": 0,
    }
    p3_norm = p3_map.get(pe["P3_data_availability"], 50)

    # P9: model compatibility
    p9_map = {"Both": 90, "Open-only": 60, "Closed-only": 40, "Unknown": 30}
    p9_norm = p9_map.get(pe["P9_model_compat"], 30)

    # P10: language normalization — liturgical/scholarly languages treated as
    # equivalent to English, correcting WEIRD bias that penalized non-English
    # benchmarks. Recognized liturgical languages: Arabic, Sanskrit, Hebrew,
    # Pali, Classical Chinese, Tibetan.
    lang = (pe.get("P10_language") or "").lower()
    liturgical = {"arabic", "sanskrit", "hebrew", "pali", "classical chinese", "tibetan"}
    if "multilingual" in lang:
        p10_norm = 90
    elif any(lit in lang for lit in liturgical) or "english" in lang:
        p10_norm = 70
    elif lang:
        p10_norm = 50
    else:
        p10_norm = 30

    # P5: license
    p5_map = {
        "Open Source": 90, "Likely Open Source": 70, "CC": 90,
        "Restricted": 30, "Unspecified": 50,
    }
    p5_norm = p5_map.get(pe["P5_license"], 50)

    # P4: code availability
    p4_map = {"Available": 80, "Unknown": 40}
    p4_norm = p4_map.get(pe["P4_code_availability"], 40)

    return round(
        p7_norm * 0.30 +
        p3_norm * 0.25 +
        p9_norm * 0.15 +
        p10_norm * 0.10 +
        p5_norm * 0.10 +
        p4_norm * 0.10
    , 1)


# ---------------------------------------------------------------------------
# Citation impact scoring (C-axis)
# ---------------------------------------------------------------------------
def score_citation_impact(candidate: dict) -> dict:
    """Score C1-C6 citation impact axes."""
    # C1: Raw citations
    c1_raw = 0
    s2_id = candidate.get("s2_paper_id", "")
    # We can't query S2 here without API calls; use what we have
    # Citation count might be in candidate from vault or external search
    c1_raw = candidate.get("citations", 0) or 0

    # C2: Citations per year
    year_str = candidate.get("year", "2025")
    try:
        year = int(year_str[:4])
    except (ValueError, TypeError):
        year = 2025
    years_since = max(1, 2026 - year)
    c2_per_year = round(c1_raw / years_since, 1) if c1_raw else 0

    # C3: Venue tier (heuristic)
    pub = (candidate.get("publication", "") or "").lower()
    c3_venue = candidate.get("publication", "")
    c3_tier = "Tier 3 (other)"
    tier1_venues = ["neurips", "icml", "iclr", "acl", "emnlp", "naacl", "aaai", "nature", "science"]
    tier2_venues = ["coling", "lrec", "aacl", "findings", "workshop", "arxiv", "eacl"]
    if any(v in pub for v in tier1_venues):
        c3_tier = "Tier 1 (top conf)"
    elif any(v in pub for v in tier2_venues):
        c3_tier = "Tier 2 (good conf/journal)"

    return {
        "C1_citation_count": c1_raw,
        "C2_citations_per_year": c2_per_year,
        "C3_venue": c3_venue,
        "C3_venue_tier": c3_tier,
        "C4_downstream_adoption": 0,  # would need S2 citation analysis
        "C5_leaderboard": None,
        "C6_community": False,
    }


def compute_ci_score(ci: dict) -> float:
    """Compute Citation Impact composite score (0-100)."""
    # Normalize citations: 100+ = top, 50+ = good, 10+ = moderate
    c1_norm = min(100, ci["C1_citation_count"] * 2)  # 50 citations = 100
    c2_norm = min(100, ci["C2_citations_per_year"] * 10)  # 10/yr = 100

    # Venue tier
    tier_scores = {"Tier 1 (top conf)": 100, "Tier 2 (good conf/journal)": 60, "Tier 3 (other)": 30}
    c3_norm = tier_scores.get(ci["C3_venue_tier"], 30)

    # C6: community activity bonus
    c6_bonus = 10 if ci.get("C6_community") else 0

    return round(
        c1_norm * 0.35 +
        c2_norm * 0.30 +
        c3_norm * 0.25 +
        c6_bonus * 0.10
    , 1)


# ---------------------------------------------------------------------------
# Build matrix entry
# ---------------------------------------------------------------------------
def build_matrix_entry(candidate: dict, entry_id: int) -> dict:
    """Build a complete feature matrix entry for a candidate."""
    title = candidate.get("short_title", "")
    abstract = candidate.get("abstract", "")
    data_desc = candidate.get("data_description", "")
    traditions = candidate.get("traditions", [])
    nw_scores = candidate.get("nw_scores", {})

    # Score all axes
    classification = candidate.get("classification", "")
    languages = candidate.get("languages_list", "")
    rd = score_theological_depth(title, abstract, data_desc, traditions, nw_scores,
                                 candidate_classification=classification,
                                 languages_list=languages)
    pe = score_practical_ease(candidate)
    ci = score_citation_impact(candidate)

    # Compute composite scores
    rd_score = compute_rd_score(rd)
    pe_score = compute_pe_score(pe)
    ci_score = compute_ci_score(ci)
    composite = round(rd_score * 0.40 + pe_score * 0.35 + ci_score * 0.25, 1)

    # Hard gates
    gate_rd = rd_score >= 30
    gate_data = pe["P3_data_availability"] != "Not available"
    gate_theological = candidate.get("classification", "") in ("theological", "theological-values")
    passes_gates = gate_rd and gate_data

    # Metadata axes
    primary_tradition = candidate.get("primary_tradition", "Unknown")

    entry = {
        "id": entry_id,
        "filename": candidate.get("filename", ""),
        "key": candidate.get("key", ""),
        "short_title": title,
        "year": candidate.get("year", ""),
        "first_author": candidate.get("first_author", ""),
        "url": candidate.get("url", ""),
        "publication": candidate.get("publication", ""),
        "classification": candidate.get("classification", ""),
        # RD axis
        **rd,
        "RD_score": rd_score,
        # PE axis
        **pe,
        "PE_score": pe_score,
        # CI axis
        **ci,
        "CI_score": ci_score,
        # Composite
        "COMPOSITE": composite,
        "gate_RD": gate_rd,
        "gate_data": gate_data,
        "gate_theological": gate_theological,
        "passes_gates": passes_gates,
        # Metadata
        "D1_year": candidate.get("year", ""),
        "D2_domain": "Religious values",
        "D3_llms_tested": candidate.get("LLM_assessed", ""),
        "D4_annotators": "Unknown",
        "D5_primary_tradition": primary_tradition,
        "D6_tradition_family": TRADITION_FAMILY.get(primary_tradition, "Unknown"),
        # Original data
        "is_benchmark": candidate.get("is_benchmark", False),
        "is_eval": candidate.get("is_eval", False),
        "is_dataset": candidate.get("is_dataset", False),
        "rv_scores": candidate.get("rv_scores", {}),
        "nw_scores": nw_scores,
        "max_rv": candidate.get("max_rv", 0),
        "s2_paper_id": candidate.get("s2_paper_id", ""),
        "DATA_URL": candidate.get("DATA_URL", ""),
        "abstract": abstract[:300],
    }

    return entry


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"=== Phase 3: Build Religious Values Benchmark Feature Matrix ===")

    # Load Phase 1 candidates
    candidates_path = sorted(DATA_DIR.glob("*-religious-benchmark-candidates.json"))
    if not candidates_path:
        print("ERROR: No Phase 1 candidates file found. Run identify_religious_benchmarks.py first.")
        sys.exit(1)

    candidates_file = candidates_path[-1]  # latest
    print(f"Loading candidates from: {candidates_file.name}")
    with open(candidates_file) as f:
        phase1 = json.load(f)

    candidates = phase1["candidates"]
    print(f"Primary candidates: {len(candidates)}")

    # Load Phase 2 external results if available
    external_path = sorted(DATA_DIR.glob("*-external-search-results.json"))
    external_results = []
    if external_path:
        print(f"Loading external results from: {external_path[-1].name}")
        with open(external_path[-1]) as f:
            phase2 = json.load(f)
        external_results = phase2.get("results", [])
        print(f"External results: {len(external_results)}")

    # Build feature matrix for primary candidates
    print(f"\nBuilding feature matrix...")
    matrix = []
    for i, candidate in enumerate(candidates, 1):
        entry = build_matrix_entry(candidate, i)
        matrix.append(entry)

    # Sort by COMPOSITE descending
    matrix.sort(key=lambda x: (-x["COMPOSITE"], x["filename"]))

    # Re-number after sort
    for i, entry in enumerate(matrix, 1):
        entry["id"] = i

    # Statistics
    passing = [e for e in matrix if e["passes_gates"]]
    theological = [e for e in matrix if e["gate_theological"]]
    with_data = [e for e in matrix if e["gate_data"]]

    print(f"\n{'='*60}")
    print(f"FEATURE MATRIX STATISTICS")
    print(f"{'='*60}")
    print(f"Total entries:           {len(matrix)}")
    print(f"Pass all gates:          {len(passing)}")
    print(f"Gate: RD >= 30:          {sum(1 for e in matrix if e['gate_RD'])}")
    print(f"Gate: Data available:    {len(with_data)}")
    print(f"Gate: Theological:       {len(theological)}")

    print(f"\n--- Score Distribution ---")
    if matrix:
        composites = [e["COMPOSITE"] for e in matrix]
        print(f"  COMPOSITE: min={min(composites):.1f}, max={max(composites):.1f}, "
              f"mean={sum(composites)/len(composites):.1f}")
        rd_scores = [e["RD_score"] for e in matrix]
        print(f"  RD_score:  min={min(rd_scores):.1f}, max={max(rd_scores):.1f}, "
              f"mean={sum(rd_scores)/len(rd_scores):.1f}")
        pe_scores = [e["PE_score"] for e in matrix]
        print(f"  PE_score:  min={min(pe_scores):.1f}, max={max(pe_scores):.1f}, "
              f"mean={sum(pe_scores)/len(pe_scores):.1f}")
        ci_scores = [e["CI_score"] for e in matrix]
        print(f"  CI_score:  min={min(ci_scores):.1f}, max={max(ci_scores):.1f}, "
              f"mean={sum(ci_scores)/len(ci_scores):.1f}")

    # R2 depth distribution
    print(f"\n--- R2 Theological Depth Distribution ---")
    from collections import Counter
    r2_dist = Counter(e["R2_depth"] for e in matrix)
    for k in sorted(r2_dist):
        pct = r2_dist[k] / len(matrix) * 100
        print(f"  depth={k}: {r2_dist[k]:3d} ({pct:5.1f}%)")

    # Tradition distribution of gate-passers
    print(f"\n--- Gate-Passing by Tradition Family ---")
    family_pass = {}
    for e in passing:
        fam = e["D6_tradition_family"]
        family_pass[fam] = family_pass.get(fam, 0) + 1
    for fam, count in sorted(family_pass.items(), key=lambda x: -x[1]):
        print(f"  {fam:25s} {count}")

    # Format distribution
    print(f"\n--- Format Distribution ---")
    fmt_counts = {}
    for e in passing:
        fmt = e["P1_format"]
        fmt_counts[fmt] = fmt_counts.get(fmt, 0) + 1
    for fmt, count in sorted(fmt_counts.items(), key=lambda x: -x[1]):
        name = FORMAT_TAXONOMY.get(fmt, {}).get("name", fmt)
        print(f"  {fmt:5s} ({name:30s}) {count}")

    # Top 20 by composite
    print(f"\n--- Top 20 by COMPOSITE (gate-passing) ---")
    for i, e in enumerate(passing[:20], 1):
        trads = ", ".join(list(e.get("R1_traditions", {}).keys())[:3])
        print(f"  {i:2d}. COMP={e['COMPOSITE']:5.1f} RD={e['RD_score']:5.1f} "
              f"PE={e['PE_score']:5.1f} CI={e['CI_score']:5.1f} "
              f"[{e['P1_format']:3s}] [{e['D6_tradition_family'][:8]:8s}] "
              f"{e['year'][:4]} {e['short_title'][:45]} | {trads}")

    # --- Write feature matrix ---
    output_matrix = {
        "generated": TODAY,
        "scoring_weights": {"RD": 0.40, "PE": 0.35, "CI": 0.25},
        "gates": {"RD_minimum": 30, "data_available": True},
        "total_entries": len(matrix),
        "gate_passing": len(passing),
        "entries": matrix,
    }

    out_path = DATA_DIR / f"{TODAY}-religious-benchmark-feature-matrix-v2.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output_matrix, f, indent=2, ensure_ascii=False)
    print(f"\nFeature matrix: {out_path}")

    # --- Write format taxonomy ---
    tax_path = DATA_DIR / f"{TODAY}-format-taxonomy.json"
    with open(tax_path, "w", encoding="utf-8") as f:
        json.dump(FORMAT_TAXONOMY, f, indent=2, ensure_ascii=False)
    print(f"Format taxonomy: {tax_path}")

    print(f"\nDone.")


if __name__ == "__main__":
    main()
