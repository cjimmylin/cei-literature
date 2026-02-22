#!/usr/bin/env python3
"""
Generate data.js for CEI Literature Vault Dashboard v7c.

Scans paper YAML frontmatter, benchmark survey JSON, normative v2 JSON,
and author map to produce a JavaScript data file consumed by the static
HTML/CSS/JS frontend.

v7b additions: Authors & Collaboration tab data, fixed author KPI.
v7c additions: Moral Psychology tab overhaul — 13 new analytical features, 5 subtabs.

Output: STATISTICS/cei-dashboard-7c/data.js

Data sources:
  - papers/*.md YAML frontmatter (2,034 papers)
  - logs/20260216-benchmark_survey_all_classifications.json (2,002 entries)
  - logs/20260216-benchmark_survey_candidates.json (~989 entries)
  - logs/20260207-normative_v2_all_classifications.json (266 entries)
  - logs/20260220-author_paper_map.json (2,034 entries)
  - logs/20260220-conference_classification_cc.json (phase stats)
"""

import json
import re
import sys
import functools
from collections import defaultdict, Counter
from pathlib import Path
from datetime import date

print = functools.partial(print, flush=True)

# ── Paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
LOGS_DIR = WS_ROOT / "logs"
STATS_DIR = WS_ROOT / "STATISTICS"
PAPERS_DIR = WS_ROOT / "papers"

CANDIDATES_FILE = LOGS_DIR / "20260216-benchmark_survey_candidates.json"
ALL_CLASSIFICATIONS_FILE = LOGS_DIR / "20260216-benchmark_survey_all_classifications.json"
NORMATIVE_FILE = LOGS_DIR / "20260207-normative_v2_all_classifications.json"
AUTHOR_MAP_FILE = LOGS_DIR / "20260220-author_paper_map.json"
AUTHOR_PROFILES_DIR = WS_ROOT / "Authors"
AI_LABS_DIR = WS_ROOT / "AI Labs"
OUTPUT_DIR = STATS_DIR / "cei-dashboard-8"
OUTPUT_FILE = OUTPUT_DIR / "data.js"

# ── Import from existing scripts ──────────────────────────────────────────
sys.path.insert(0, str(SCRIPT_DIR))
from generate_benchmark_survey_report import CATEGORIES, classify_entry, extract_year
from generate_conference_report_cc import (
    categorize_venue, extract_conference_family, KNOWN_JOURNALS,
)
from add_conference_field_cc import JOURNAL_EXACT, JOURNAL_SUBSTRING


# ═══════════════════════════════════════════════════════════════════════════
# PATTERN DEFINITIONS (from generate_vault_dashboard_3.py)
# ═══════════════════════════════════════════════════════════════════════════

MODEL_FAMILIES = {
    "GPT-4": r"\bgpt[\s\-_]?4\b",
    "GPT-3.5": r"\bgpt[\s\-_]?3\.?5\b|\bchatgpt\b",
    "GPT-3": r"\bgpt[\s\-_]?3\b(?!\.?5)",
    "GPT-2": r"\bgpt[\s\-_]?2\b",
    "Claude": r"\bclaude\b",
    "Llama": r"\bll?ama[\s\-_]?\d?\b",
    "Gemini": r"\bgemini\b|\bgemma\b",
    "Mistral/Mixtral": r"\bmistral\b|\bmixtral\b",
    "Qwen": r"\bqwen\b",
    "DeepSeek": r"\bdeepseek\b",
    "BERT family": r"\bbert\b|\broberta\b|\balbert\b|\bdeberta\b|\belectra\b",
    "T5/Flan": r"\b(?:flan[\s\-_]?)?t5\b|\bflan\b",
    "Falcon": r"\bfalcon\b",
    "Phi": r"\bphi[\s\-_]?\d\b",
    "Vicuna": r"\bvicuna\b",
    "BLOOM": r"\bbloom\b(?!berg)",
    "OPT": r"\bopt[\s\-_]\d|\bopt\b(?=[\s,\-]|\Z)",
    "PaLM": r"\bpalm\b|\bpalm[\s\-_]?2\b",
    "Cohere": r"\bcohere\b|\bcommand[\s\-_]?r\b",
    "Word2Vec/GloVe": r"\bword2vec\b|\bglove\b|\bfasttext\b",
    "Delphi": r"\bdelphi\b",
    "Alpaca": r"\balpaca\b",
    "Aya": r"\baya\b",
    "Baichuan": r"\bbaichuan\b",
    "Yi": r"\b(?:yi[\s\-_]?\d|yi\b(?=[\s,]))",
    "InternLM": r"\binternlm\b",
    "ChatGLM": r"\bchatglm\b|\bglm\b",
    "WizardLM": r"\bwizardlm\b",
    "Zephyr": r"\bzephyr\b",
    "StableLM": r"\bstablelm\b|\bstable[\s\-_]?lm\b",
    "MPT": r"\bmpt[\s\-_]?\d",
    "Gemma": r"\bgemma\b(?!.*gemini)",
    "Jurassic/AI21": r"\bjurassic\b|\bai21\b|\bj2\b",
}
_MODEL_PATTERNS = {k: re.compile(v, re.IGNORECASE) for k, v in MODEL_FAMILIES.items()}


def extract_model_families(text):
    if not text:
        return []
    return [name for name, pat in _MODEL_PATTERNS.items() if pat.search(text)]


# ── Virtue Keyword Taxonomy ──────────────────────────────────────────────

VIRTUE_KEYWORDS = {
    "Honesty":         ["honesty", "truthful", "deception", "lying"],
    "Justice":         ["justice"],
    "Fairness":        ["fairness", "fair treatment", "equitable"],
    "Prudence":        ["prudence", "phronesis", "practical wisdom"],
    "Temperance":      ["temperance", "moderation", "self-control"],
    "Courage":         ["courage", "bravery"],
    "Compassion":      ["compassion", "empathy", "empathetic"],
    "Integrity":       ["integrity"],
    "Humility":        ["humility", "humble"],
    "Trustworthiness": ["trustworth"],
    "Care":            ["care ethic", "ethics of care", "caring"],
    "Wisdom":          ["wisdom", "wise"],
    "Benevolence":     ["benevolence", "benevolent"],
    "Eudaimonia":      ["eudaimonia", "flourishing", "well-being"],
    "Character":       ["character trait", "moral character", "character-based"],
}


def scan_virtue_keywords(title, abstract):
    """Count which virtue keywords appear in a paper's title + abstract."""
    text = (title + " " + abstract).lower()
    found = set()
    for virtue, patterns in VIRTUE_KEYWORDS.items():
        if any(p in text for p in patterns):
            found.add(virtue)
    return found


# ── Deontological Concept Taxonomy ────────────────────────────────────────

DEONTOLOGY_KEYWORDS = {
    "Rules / Norms":         ["rule-based", "rule-follow", "rule violation",
                              "moral rule", "ethical rule", "moral norm", "ethical norm"],
    "Kantian Ethics":        ["kantian", "categorical imperative", "universaliz",
                              "universal law"],
    "Duty / Duties":         ["duty", "duties", "duty-based", "obligat"],
    "Rights":                ["rights", "human rights", "right to"],
    "Moral Judgment":        ["moral judg", "ethical judg", "normative judg"],
    "Moral Dilemma":         ["moral dilemma", "ethical dilemma"],
    "Trolley Problem":       ["trolley", "footbridge"],
    "Deontic Logic":         ["deontic"],
    "Moral Agency":          ["moral agent", "moral agency"],
    "Fairness / Justice":    ["fairness", "justice", "equitable"],
    "Autonomy":              ["moral autonomy", "autonomous moral", "self-legislat"],
    "Consent":               ["informed consent", "consent"],
}


def scan_deontology_keywords(title, abstract):
    """Count which deontological concepts appear in a paper's title + abstract."""
    text = (title + " " + abstract).lower()
    found = set()
    for concept, patterns in DEONTOLOGY_KEYWORDS.items():
        if any(p in text for p in patterns):
            found.add(concept)
    return found


# ── Consequentialist Concept Taxonomy ─────────────────────────────────────

CU_CONCEPT_KEYWORDS = {
    "Outcome / Consequences":       ["outcome", "consequen", "result-based"],
    "Trade-off Reasoning":          ["trade-off", "tradeoff", "trade off",
                                     "cost-benefit", "cost benefit"],
    "Utility / Welfare":            ["utility function", "expected utility",
                                     "utility maximiz", "social welfare",
                                     "welfare function", "nash product",
                                     "utilitarian sum"],
    "Greatest Good":                ["greatest good", "greatest number",
                                     "greatest happiness", "maximiz", "maximis"],
    "Harm Calculus":                ["harm reduct", "harm minimiz", "risk-benefit",
                                     "instrumental harm"],
    "Trolley / Moral Dilemmas":     ["trolley", "footbridge", "moral dilemma",
                                     "ethical dilemma"],
    "Moral Machine / AV":           ["moral machine", "autonomous driv",
                                     "autonomous vehicle", "self-driving"],
    "Value Alignment":              ["value alignment", "ai alignment",
                                     "moral alignment", "aligned with human"],
    "Preference Aggregation":       ["preference", "aggregat"],
    "Well-being / Flourishing":     ["well-being", "wellbeing", "flourishing",
                                     "human welfare"],
    "RLHF / Reward Modeling":       ["rlhf", "reinforcement learning from human",
                                     "reward model", "reward function"],
    "Multi-agent Deliberation":     ["multi-agent", "multiagent", "deliberat",
                                     "collective decision"],
    "Impartiality":                 ["impartial", "impersonal"],
}


def scan_cu_concepts(title, abstract):
    """Count which consequentialist concepts appear in a paper's title + abstract."""
    text = (title + " " + abstract).lower()
    found = set()
    for concept, patterns in CU_CONCEPT_KEYWORDS.items():
        if any(p in text for p in patterns):
            found.add(concept)
    return found


# ── Care Ethics Keyword Taxonomy ─────────────────────────────────────
CARE_ETHICS_KEYWORDS = {
    "Ethics of Care": ["ethics of care", "care ethic", "caring ethic"],
    "Relational Ethics": ["relational ethic", "relational autonomy"],
    "Feminist Ethics": ["feminist ethic", "feminist moral", "feminist approach"],
    "Vulnerability": ["vulnerability", "vulnerable", "dependent"],
    "Empathy/Compassion": ["empathy", "empathetic", "compassion", "compassionate"],
    "Caregiving": ["caregiving", "caregiver", "care work", "care labor"],
    "Attentiveness": ["attentiveness", "attentive", "responsiveness"],
    "Interdependence": ["interdependence", "interdependent", "interconnected"],
}

CONTRACTUALISM_KEYWORDS = {
    "Social Contract": ["social contract", "contractarian", "contractualis"],
    "Rawlsian": ["rawlsian", "rawls", "veil of ignorance", "original position"],
    "Justice as Fairness": ["justice as fairness", "fairness principle"],
    "Distributive Justice": ["distributive justice", "distributive fairness"],
    "Procedural Justice": ["procedural justice", "procedural fairness"],
    "Consent": ["consent", "consensual", "mutual agreement"],
    "Rights": ["rights-based", "natural rights", "human rights framework"],
}

PRINCIPLISM_KEYWORDS = {
    "Autonomy": ["autonomy", "autonomous", "self-determination", "informed consent"],
    "Beneficence": ["beneficence", "beneficent", "do good"],
    "Non-maleficence": ["non-maleficence", "nonmaleficence", "do no harm", "primum non nocere"],
    "Justice": ["justice", "just distribution", "equitable access"],
    "Beauchamp & Childress": ["beauchamp", "childress", "principl"],
    "Bioethics": ["bioethic", "medical ethic", "clinical ethic"],
}


def scan_care_keywords(title, abstract):
    text = (title + " " + abstract).lower()
    found = set()
    for concept, patterns in CARE_ETHICS_KEYWORDS.items():
        if any(p in text for p in patterns):
            found.add(concept)
    return found


def scan_contractualism_keywords(title, abstract):
    text = (title + " " + abstract).lower()
    found = set()
    for concept, patterns in CONTRACTUALISM_KEYWORDS.items():
        if any(p in text for p in patterns):
            found.add(concept)
    return found


def scan_principlism_keywords(title, abstract):
    text = (title + " " + abstract).lower()
    found = set()
    for concept, patterns in PRINCIPLISM_KEYWORDS.items():
        if any(p in text for p in patterns):
            found.add(concept)
    return found


# ── Cultural Region Mapping ───────────────────────────────────────────────

CULTURE_TO_REGION = {
    "Chinese": "East Asia", "China": "East Asia", "Japanese": "East Asia",
    "Japan": "East Asia", "Korean": "East Asia", "Korea": "East Asia",
    "South Korean": "East Asia", "Taiwanese": "East Asia", "Taiwan": "East Asia",
    "Hong Kong": "East Asia", "Mongolian": "East Asia",
    "Indian": "South Asia", "India": "South Asia", "Pakistani": "South Asia",
    "Pakistan": "South Asia", "Bangladeshi": "South Asia", "Bangladesh": "South Asia",
    "Sri Lankan": "South Asia", "Nepali": "South Asia", "Nepal": "South Asia",
    "Indonesian": "Southeast Asia", "Indonesia": "Southeast Asia",
    "Filipino": "Southeast Asia", "Philippines": "Southeast Asia",
    "Vietnamese": "Southeast Asia", "Vietnam": "Southeast Asia",
    "Thai": "Southeast Asia", "Thailand": "Southeast Asia",
    "Malaysian": "Southeast Asia", "Malaysia": "Southeast Asia",
    "Singaporean": "Southeast Asia", "Singapore": "Southeast Asia",
    "Burmese": "Southeast Asia", "Myanmar": "Southeast Asia",
    "Cambodian": "Southeast Asia", "Laotian": "Southeast Asia",
    "Arabic": "MENA", "Arab": "MENA", "Saudi": "MENA", "Saudi Arabian": "MENA",
    "Egyptian": "MENA", "Egypt": "MENA", "Iranian": "MENA", "Iran": "MENA",
    "Iraqi": "MENA", "Turkish": "MENA", "Turkey": "MENA",
    "Israeli": "MENA", "Israel": "MENA", "Palestinian": "MENA",
    "Lebanese": "MENA", "Jordanian": "MENA", "Emirati": "MENA", "UAE": "MENA",
    "Kuwaiti": "MENA", "Qatari": "MENA", "Bahraini": "MENA",
    "Omani": "MENA", "Yemeni": "MENA", "Syrian": "MENA",
    "Moroccan": "MENA", "Tunisian": "MENA", "Algerian": "MENA",
    "Libyan": "MENA", "Persian": "MENA",
    "African": "Sub-Saharan Africa", "Nigerian": "Sub-Saharan Africa",
    "Nigeria": "Sub-Saharan Africa", "Kenyan": "Sub-Saharan Africa",
    "South African": "Sub-Saharan Africa", "Ethiopian": "Sub-Saharan Africa",
    "Ghanaian": "Sub-Saharan Africa", "Tanzanian": "Sub-Saharan Africa",
    "Ugandan": "Sub-Saharan Africa", "Rwandan": "Sub-Saharan Africa",
    "Senegalese": "Sub-Saharan Africa", "Congolese": "Sub-Saharan Africa",
    "Zimbabwean": "Sub-Saharan Africa", "Cameroonian": "Sub-Saharan Africa",
    "Somali": "Sub-Saharan Africa", "Sudanese": "Sub-Saharan Africa",
    "Swahili": "Sub-Saharan Africa",
    "American": "North America", "US": "North America", "USA": "North America",
    "United States": "North America", "Canadian": "North America", "Canada": "North America",
    "British": "Western Europe", "UK": "Western Europe", "English": "Western Europe",
    "German": "Western Europe", "Germany": "Western Europe",
    "French": "Western Europe", "France": "Western Europe",
    "Italian": "Western Europe", "Italy": "Western Europe",
    "Spanish": "Western Europe", "Spain": "Western Europe",
    "Dutch": "Western Europe", "Netherlands": "Western Europe",
    "Swedish": "Western Europe", "Sweden": "Western Europe",
    "Norwegian": "Western Europe", "Norway": "Western Europe",
    "Danish": "Western Europe", "Denmark": "Western Europe",
    "Finnish": "Western Europe", "Finland": "Western Europe",
    "Swiss": "Western Europe", "Switzerland": "Western Europe",
    "Austrian": "Western Europe", "Belgian": "Western Europe",
    "Irish": "Western Europe", "Portuguese": "Western Europe",
    "Greek": "Western Europe", "Luxembourg": "Western Europe",
    "Russian": "Eastern Europe", "Russia": "Eastern Europe",
    "Polish": "Eastern Europe", "Poland": "Eastern Europe",
    "Ukrainian": "Eastern Europe", "Ukraine": "Eastern Europe",
    "Czech": "Eastern Europe", "Romanian": "Eastern Europe",
    "Hungarian": "Eastern Europe", "Bulgarian": "Eastern Europe",
    "Serbian": "Eastern Europe", "Croatian": "Eastern Europe",
    "Slovak": "Eastern Europe", "Slovenian": "Eastern Europe",
    "Lithuanian": "Eastern Europe", "Latvian": "Eastern Europe",
    "Estonian": "Eastern Europe", "Bosnian": "Eastern Europe",
    "Albanian": "Eastern Europe", "Macedonian": "Eastern Europe",
    "Belarusian": "Eastern Europe",
    "Brazilian": "Latin America", "Brazil": "Latin America",
    "Mexican": "Latin America", "Mexico": "Latin America",
    "Argentine": "Latin America", "Argentina": "Latin America",
    "Colombian": "Latin America", "Peruvian": "Latin America",
    "Chilean": "Latin America", "Venezuelan": "Latin America",
    "Ecuadorian": "Latin America", "Bolivian": "Latin America",
    "Cuban": "Latin America", "Dominican": "Latin America",
    "Latin American": "Latin America", "Costa Rican": "Latin America",
    "Australian": "Oceania", "Australia": "Oceania",
    "New Zealand": "Oceania", "New Zealander": "Oceania",
    "Kazakh": "Central Asia", "Uzbek": "Central Asia",
    "Kyrgyz": "Central Asia", "Tajik": "Central Asia",
    "Afghan": "Central Asia", "Afghanistan": "Central Asia",
    "Western": "Multi-Region", "Eastern": "Multi-Region",
    "Global": "Multi-Region", "Multicultural": "Multi-Region",
    "Cross-cultural": "Multi-Region", "International": "Multi-Region",
    "Multilingual": "Multi-Region", "Diverse": "Multi-Region",
    "Multi-country": "Multi-Region", "Multi-national": "Multi-Region",
}

WEIRD_REGIONS = {"Western Europe", "North America", "Oceania"}


def classify_region(culture):
    if not culture:
        return "Other"
    if culture in CULTURE_TO_REGION:
        return CULTURE_TO_REGION[culture]
    culture_lower = culture.lower()
    for k, v in CULTURE_TO_REGION.items():
        if k.lower() == culture_lower:
            return v
        if k.lower() in culture_lower or culture_lower in k.lower():
            return v
    return "Other"


def classify_weird(region):
    if region in WEIRD_REGIONS:
        return "WEIRD"
    if region == "Multi-Region":
        return "Mixed"
    return "Non-WEIRD"


# ── Language family & region mappings (for Cultural Values enrichment) ────
LANG_TO_FAMILY = {
    "English": "Indo-European", "German": "Indo-European", "French": "Indo-European",
    "Spanish": "Indo-European", "Portuguese": "Indo-European", "Italian": "Indo-European",
    "Dutch": "Indo-European", "Russian": "Indo-European", "Hindi": "Indo-European",
    "Urdu": "Indo-European", "Bengali": "Indo-European", "Persian": "Indo-European",
    "Greek": "Indo-European", "Polish": "Indo-European", "Romanian": "Indo-European",
    "Swedish": "Indo-European", "Norwegian": "Indo-European", "Danish": "Indo-European",
    "Czech": "Indo-European", "Marathi": "Indo-European", "Gujarati": "Indo-European",
    "Nepali": "Indo-European", "Sinhala": "Indo-European", "Pashto": "Indo-European",
    "Kurdish": "Indo-European", "Ukrainian": "Indo-European",
    "Chinese": "Sino-Tibetan", "Mandarin": "Sino-Tibetan", "Cantonese": "Sino-Tibetan",
    "Burmese": "Sino-Tibetan", "Tibetan": "Sino-Tibetan",
    "Arabic": "Afro-Asiatic", "Hebrew": "Afro-Asiatic", "Amharic": "Afro-Asiatic",
    "Hausa": "Afro-Asiatic", "Somali": "Afro-Asiatic",
    "Japanese": "Japonic",
    "Korean": "Koreanic",
    "Turkish": "Turkic", "Azerbaijani": "Turkic", "Uzbek": "Turkic", "Kazakh": "Turkic",
    "Indonesian": "Austronesian", "Malay": "Austronesian", "Filipino": "Austronesian",
    "Tagalog": "Austronesian", "Javanese": "Austronesian",
    "Vietnamese": "Austroasiatic", "Khmer": "Austroasiatic",
    "Thai": "Tai-Kadai", "Lao": "Tai-Kadai",
    "Swahili": "Niger-Congo", "Yoruba": "Niger-Congo", "Igbo": "Niger-Congo",
    "Zulu": "Niger-Congo", "Xhosa": "Niger-Congo", "Twi": "Niger-Congo",
    "Tamil": "Dravidian", "Telugu": "Dravidian", "Kannada": "Dravidian",
    "Malayalam": "Dravidian",
    "Finnish": "Uralic", "Hungarian": "Uralic", "Estonian": "Uralic",
    "Georgian": "Kartvelian",
}

LANG_TO_REGION = {
    # Must use same region names as CULTURE_TO_REGION for radar alignment
    "English": "North America", "French": "Western Europe", "German": "Western Europe",
    "Spanish": "Latin America", "Portuguese": "Latin America", "Italian": "Western Europe",
    "Dutch": "Western Europe", "Swedish": "Western Europe", "Norwegian": "Western Europe",
    "Danish": "Western Europe", "Greek": "Western Europe", "Polish": "Eastern Europe",
    "Romanian": "Eastern Europe", "Czech": "Eastern Europe", "Ukrainian": "Eastern Europe",
    "Russian": "Eastern Europe",
    "Chinese": "East Asia", "Mandarin": "East Asia", "Cantonese": "East Asia",
    "Japanese": "East Asia", "Korean": "East Asia",
    "Hindi": "South Asia", "Urdu": "South Asia", "Bengali": "South Asia",
    "Marathi": "South Asia", "Gujarati": "South Asia", "Nepali": "South Asia",
    "Sinhala": "South Asia", "Tamil": "South Asia", "Telugu": "South Asia",
    "Kannada": "South Asia", "Malayalam": "South Asia",
    "Arabic": "MENA", "Hebrew": "MENA",
    "Persian": "MENA", "Turkish": "MENA",
    "Kurdish": "MENA", "Pashto": "MENA",
    "Indonesian": "Southeast Asia", "Malay": "Southeast Asia", "Filipino": "Southeast Asia",
    "Tagalog": "Southeast Asia", "Javanese": "Southeast Asia", "Vietnamese": "Southeast Asia",
    "Khmer": "Southeast Asia", "Thai": "Southeast Asia", "Lao": "Southeast Asia",
    "Burmese": "Southeast Asia", "Tibetan": "East Asia",
    "Swahili": "Sub-Saharan Africa", "Yoruba": "Sub-Saharan Africa",
    "Igbo": "Sub-Saharan Africa", "Zulu": "Sub-Saharan Africa",
    "Xhosa": "Sub-Saharan Africa", "Twi": "Sub-Saharan Africa",
    "Hausa": "Sub-Saharan Africa", "Amharic": "Sub-Saharan Africa",
    "Somali": "Sub-Saharan Africa",
    "Azerbaijani": "Central Asia", "Uzbek": "Central Asia", "Kazakh": "Central Asia",
    "Finnish": "Western Europe", "Hungarian": "Eastern Europe", "Estonian": "Eastern Europe",
    "Georgian": "Eastern Europe",
}


def classify_lang_family(lang):
    """Map a language name to its language family."""
    if not lang:
        return "Other"
    if lang in LANG_TO_FAMILY:
        return LANG_TO_FAMILY[lang]
    lang_lower = lang.lower()
    for k, v in LANG_TO_FAMILY.items():
        if k.lower() == lang_lower:
            return v
    return "Other"


def classify_lang_region(lang):
    """Map a language name to a geographic region."""
    if not lang:
        return "Other"
    if lang in LANG_TO_REGION:
        return LANG_TO_REGION[lang]
    lang_lower = lang.lower()
    for k, v in LANG_TO_REGION.items():
        if k.lower() == lang_lower:
            return v
    return "Other"


# ── Moral Psychology Patterns ─────────────────────────────────────────────

THEORY_PATTERNS = {
    "MFT": re.compile(r'moral\s+foundation|MFT\b|MFQ\b|haidt|care/harm|fairness/cheat|loyalty/betray|authority/subver|sanctity/degrad|liberty/oppress|binding\s+foundation|individualiz', re.I),
    "Schwartz": re.compile(r'schwartz|basic\s+human\s+values?|value\s+survey|SVS\b|PVQ\b|value\s+pluralism|schwartz.*value|value\s+orientat', re.I),
    "Kohlberg": re.compile(r'kohlberg|moral\s+development|cognitive\s+development.*moral|DIT\b|defining\s+issues\s+test|post[\s\-]?conventional|pre[\s\-]?conventional', re.I),
    "Trolley": re.compile(r'trolley|footbridge|fat\s+man|moral\s+dilemma|ethical\s+dilemma|thought\s+experiment', re.I),
    "DualProc": re.compile(r'dual\s+process|system\s+1.*system\s+2|automatic.*deliberat|intuiti.*reason.*moral|type\s+1.*type\s+2', re.I),
    "SIM": re.compile(r'social\s+intuitionist|SIM\b.*haidt|haidt.*intuitionist|moral\s+intuition.*social', re.I),
    "Dyadic": re.compile(r'dyadic\s+moral|moral\s+dyad|agent.*patient\s+model|gray.*schein', re.I),
    "MoralID": re.compile(r'moral\s+identity|moral\s+self[\s\-]?concept|moral\s+character|moral\s+exemplar', re.I),
}

MFT_FOUNDATIONS = [
    "Care/Harm", "Fairness/Cheating", "Loyalty/Betrayal",
    "Authority/Subversion", "Sanctity/Degradation", "Liberty/Oppression",
]

MFT_FOUNDATION_PATTERNS = {
    "Care/Harm": re.compile(r'care[/\s]harm|care\s+foundation|harm\s+foundation|compassion.*cruelty|nurtur.*suffer', re.I),
    "Fairness/Cheating": re.compile(r'fairness[/\s]cheat|fairness\s+foundation|justice.*reciproc|proportional.*justice', re.I),
    "Loyalty/Betrayal": re.compile(r'loyalty[/\s]betray|loyalty\s+foundation|in[\s\-]?group.*loyal|patriot.*betray', re.I),
    "Authority/Subversion": re.compile(r'authority[/\s]subver|authority\s+foundation|hierarch.*obedien|respect.*authority', re.I),
    "Sanctity/Degradation": re.compile(r'sanctity[/\s]degrad|sanctity\s+foundation|purity.*disgust|sacred.*contamina', re.I),
    "Liberty/Oppression": re.compile(r'liberty[/\s]oppress|liberty\s+foundation|freedom.*tyrann|autonomy.*coerci', re.I),
}

SCHWARTZ_VALUES = [
    "Self-Direction", "Stimulation", "Hedonism", "Achievement", "Power",
    "Security", "Conformity", "Tradition", "Benevolence", "Universalism",
]

SCHWARTZ_VALUE_PATTERNS = {
    "Self-Direction": re.compile(r'self[\s\-]?direction|autonomy|independence|creativity|curious', re.I),
    "Stimulation": re.compile(r'stimulation|excitement|novelty|daring|varied\s+life', re.I),
    "Hedonism": re.compile(r'hedonism|pleasure|gratification|enjoyment|self[\s\-]?indulgen', re.I),
    "Achievement": re.compile(r'achievement|success|ambition|capab|competen|influenti', re.I),
    "Power": re.compile(r'\bpower\b|dominan|status|prestige|control.*resource|social\s+power', re.I),
    "Security": re.compile(r'security|safety|stability|social\s+order|family\s+security|reciprocat', re.I),
    "Conformity": re.compile(r'conformity|obedien|self[\s\-]?disciplin|polite|honor.*elder', re.I),
    "Tradition": re.compile(r'\btradition|devout|humble|accept.*life|moderate|custom', re.I),
    "Benevolence": re.compile(r'benevolence|helpfulness|honest|forgiv|loyal|responsible|true\s+friend', re.I),
    "Universalism": re.compile(r'universalism|equality|social\s+justice|broad[\s\-]?minded|peace|environ|inner\s+harmon', re.I),
}

THEORY_META = [
    {"name": "Moral Foundations Theory", "abbrev": "MFT", "color": "#6366f1"},
    {"name": "Schwartz Value Theory", "abbrev": "Schwartz", "color": "#22d3ee"},
    {"name": "Kohlberg's Moral Development", "abbrev": "Kohlberg", "color": "#f59e0b"},
    {"name": "Trolley/Moral Dilemmas", "abbrev": "Trolley", "color": "#ec4899"},
    {"name": "Dual Process Theory", "abbrev": "DualProc", "color": "#22c55e"},
    {"name": "Social Intuitionist Model", "abbrev": "SIM", "color": "#a855f7"},
    {"name": "Dyadic Morality", "abbrev": "Dyadic", "color": "#f97316"},
    {"name": "Moral Identity", "abbrev": "MoralID", "color": "#14b8a6"},
]


def classify_theories(text):
    if not text or text.lower() in ('n/a', 'na', 'no', 'none', ''):
        return []
    return [abbrev for abbrev, pat in THEORY_PATTERNS.items() if pat.search(text)]


# ── v7c: Schwartz Higher-Order Quadrants ─────────────────────────────────

SCHWARTZ_HIGHER_ORDER = {
    "Openness to Change": ["Self-Direction", "Stimulation", "Hedonism"],
    "Self-Enhancement": ["Hedonism", "Achievement", "Power"],
    "Conservation": ["Security", "Conformity", "Tradition"],
    "Self-Transcendence": ["Benevolence", "Universalism"],
}

# ── v7c: Alignment Outcome Patterns ─────────────────────────────────────

ALIGNMENT_OUTCOME_PATTERNS = {
    "Aligned": re.compile(r'align(ed|ment)|consistent\s+with\s+human|match(es|ed|ing)\s+(human|moral)|moral\s+agreement', re.I),
    "Misaligned": re.compile(r'misalign|inconsisten|diverge[sd]?\s+from|fail(s|ed)?\s+to\s+align|moral\s+gap|moral\s+blind', re.I),
    "Mixed": re.compile(r'partial(ly)?\s+align|mixed\s+result|varies?\s+(across|by)|depends?\s+on|context[\s\-]?dependent', re.I),
    "Culturally Variable": re.compile(r'cultur(e|al)(ly)?\s+(vari|differ|bias|specif)|cross[\s\-]?cultural\s+differ|western\s+bias', re.I),
}

# ── v7c: Methodology Patterns ───────────────────────────────────────────

METHODOLOGY_PATTERNS = {
    "Questionnaire / Survey": re.compile(r'questionnaire|survey|MFQ\b|SVS\b|PVQ\b|WVS\b|DIT\b|likert|self[\s\-]?report', re.I),
    "Prompt-Based Probing": re.compile(r'prompt[\s\-]?(based|engineer|prob)|zero[\s\-]?shot|few[\s\-]?shot|in[\s\-]?context\s+learn', re.I),
    "Scenario / Vignette": re.compile(r'scenario|vignette|trolley|dilemma|thought\s+experiment|moral\s+machine', re.I),
    "Corpus / Text Analysis": re.compile(r'corpus|text\s+analysis|content\s+analysis|NLP|dictionary[\s\-]?based|MFD\b|eMFD\b', re.I),
    "Human Comparison": re.compile(r'human\s+comparison|human\s+baseline|human\s+annotator|inter[\s\-]?annotator|human\s+subject', re.I),
}

# ── v7c: Instrument Patterns ────────────────────────────────────────────

INSTRUMENT_PATTERNS = {
    "MFQ": re.compile(r'MFQ\b|Moral\s+Foundations?\s+Questionnaire', re.I),
    "MFD / eMFD": re.compile(r'MFD\b|eMFD\b|Moral\s+Foundations?\s+Dictionary', re.I),
    "SVS / PVQ": re.compile(r'SVS\b|PVQ\b|Schwartz\s+Value\s+Survey|Portrait\s+Values?\s+Questionnaire', re.I),
    "WVS": re.compile(r'WVS\b|World\s+Values?\s+Survey', re.I),
    "DIT": re.compile(r'DIT\b|Defining\s+Issues?\s+Test', re.I),
    "Moral Machine": re.compile(r'Moral\s+Machine', re.I),
    "ETHICS dataset": re.compile(r'ETHICS\s+(dataset|benchmark)|Hendrycks.*ETHICS', re.I),
}

# ── v7c: MFT Approach Patterns ──────────────────────────────────────────

MFT_APPROACH_PATTERNS = {
    "MFQ Instrument": re.compile(r'MFQ\b|Moral\s+Foundations?\s+Questionnaire|likert.*foundation|foundation.*likert', re.I),
    "MFD Dictionary": re.compile(r'MFD\b|eMFD\b|Moral\s+Foundations?\s+Dictionary|dictionary[\s\-]?based.*moral', re.I),
    "Prompt-Based": re.compile(r'prompt[\s\-]?(based|engineer|prob).*moral|moral.*prompt[\s\-]?(based|engineer)|zero[\s\-]?shot.*foundation|foundation.*zero[\s\-]?shot', re.I),
    "Corpus / Text": re.compile(r'corpus.*moral|moral.*corpus|text\s+analysis.*moral|moral.*text\s+analysis|NLP.*foundation|foundation.*NLP', re.I),
}

# 5 active theories for filtered cooccurrence (exclude SIM, Dyadic, MoralID — <5 papers each)
ACTIVE_THEORIES = ["MFT", "Schwartz", "Kohlberg", "Trolley", "DualProc"]


# ── Religious Tradition Patterns ──────────────────────────────────────────

TRADITION_META = [
    {"name": "Islam", "abbrev": "Islam", "color": "#22c55e"},
    {"name": "Christianity", "abbrev": "Christianity", "color": "#6366f1"},
    {"name": "Buddhism", "abbrev": "Buddhism", "color": "#f59e0b"},
    {"name": "Hinduism", "abbrev": "Hinduism", "color": "#ec4899"},
    {"name": "Confucian", "abbrev": "Confucian", "color": "#22d3ee"},
    {"name": "Judaism", "abbrev": "Judaism", "color": "#a855f7"},
    {"name": "Shinto", "abbrev": "Shinto", "color": "#e879f9"},
    {"name": "Ubuntu", "abbrev": "Ubuntu", "color": "#f97316"},
    {"name": "Indigenous", "abbrev": "Indigenous", "color": "#14b8a6"},
]

RELIG_TRAD_PATTERNS = {
    "Islam": re.compile(r'islam|muslim|sharia|quran|hadith|fiqh|maqasid|halal|haram', re.I),
    "Christianity": re.compile(r'christian|bible|biblical|protestant|catholic|orthodox\s+christian|gospel|new\s+testament', re.I),
    "Buddhism": re.compile(r'buddhis[mt]|buddhist\s+ethic|zen\b|theravada|mahayana|tibetan\s+buddhis', re.I),
    "Hinduism": re.compile(r'hindu|vedic|bhagavad|upanishad', re.I),
    "Confucian": re.compile(r'confucian|confucius|mencius', re.I),
    "Judaism": re.compile(r'jewish|judaism|talmud|torah|rabbinic|halakh', re.I),
    "Shinto": re.compile(r'shinto|kami\b(?!.*kaze)|techno.?animis|animis.*japan|japan.*animis', re.I),
    "Ubuntu": re.compile(r'ubuntu(?!.*(?:linux|operat))|african\s+ethic|african\s+moral', re.I),
    "Indigenous": re.compile(r'indigenous\s+(?:ethic|value|spirit|religi)|first\s+nation|aboriginal\s+(?:spirit|religi)|native\s+(?:american|spirit)', re.I),
}


def classify_relig_traditions(values_list, extra_text=""):
    combined = " ".join(values_list) + " " + extra_text if values_list else extra_text
    if not combined.strip():
        return []
    return [name for name, pat in RELIG_TRAD_PATTERNS.items() if pat.search(combined)]


# ── Religious Tradition Extended Analysis Constants ──────────────────────

# Islamic Knowledge Domain Patterns (for treemap classification)
ISLAMIC_DOMAIN_PATTERNS = {
    "Quran/Quranic": re.compile(r"quran|qur.an|quranic|ayah|surah|tafsir|recit", re.I),
    "Hadith/Sunnah": re.compile(r"hadith|sunnah|sahih|bukhari|isnad|matn", re.I),
    "Fatwa/Fiqh": re.compile(r"fatwa|fiqh|jurisprud|madhab|madhahib|sharia|muft", re.I),
    "Bias/Islamophobia": re.compile(r"islamophob|anti.muslim|bias.*islam|islam.*bias|stereotyp.*muslim|muslim.*stereotyp", re.I),
    "Values Alignment": re.compile(r"value.*align|align.*value|maqasid|moral.*islam|islam.*moral|ethic.*islam|islam.*ethic", re.I),
    "General Islamic NLP": re.compile(r"arab.*nlp|nlp.*arab|muslim.*commun|islamic.*text|arabic.*process", re.I),
}

# Islamic Textual Source Patterns (for radar chart)
ISLAMIC_SOURCE_PATTERNS = {
    "Quran": re.compile(r"quran|qur.an|quranic|tafsir|ayah|surah", re.I),
    "Hadith/Sunnah": re.compile(r"hadith|sunnah|sahih|bukhari|isnad", re.I),
    "Fiqh/Fatwa": re.compile(r"fiqh|fatwa|jurisprud|madhab|muft", re.I),
    "Ijma/Consensus": re.compile(r"ijma|consensus.*islam|islamic.*consensus", re.I),
    "Qiyas/Analogy": re.compile(r"qiyas|analog.*islam|islamic.*analog|ijtihad", re.I),
}

# Christian-Jewish Theological Concept Patterns (for radar chart)
THEOLOGICAL_CONCEPT_PATTERNS = {
    "Natural Law/Aquinas": re.compile(r"natural\s+law|aquinas|thomist|thomistic", re.I),
    "Divine Command": re.compile(r"divine\s+command|god.s\s+will|theistic\s+ethics", re.I),
    "Theological Virtue": re.compile(r"theological\s+virtue|faith.*hope.*charit|charity.*faith", re.I),
    "Liberation Theology": re.compile(r"liberation\s+theolog|preferential\s+option|option.*poor", re.I),
    "Biblical Hermeneutics": re.compile(r"hermeneutic|biblical\s+interpret|scriptural\s+interpret|exeges", re.I),
    "Halakhic Reasoning": re.compile(r"halakh|jewish\s+law|talmudic\s+reason", re.I),
    "Tikkun Olam": re.compile(r"tikkun\s+olam|repair.*world", re.I),
    "Imago Dei": re.compile(r"imago\s+dei|image\s+of\s+god", re.I),
    "Mussar": re.compile(r"mussar|musar", re.I),
    "Scriptural NLP": re.compile(r"bible\s+qa|biblical\s+qa|scripture.*nlp|bible.*corpus|torah.*nlp", re.I),
}

# Dharmic Ethical Concept Patterns (for dual-polygon radar)
DHARMIC_CONCEPT_PATTERNS = {
    "Ahimsa": re.compile(r"ahimsa|non.?harm|non.?violen", re.I),
    "Karma": re.compile(r"\bkarma\b|karmic", re.I),
    "Dharma": re.compile(r"\bdharma\b|dharmic", re.I),
    "Compassion": re.compile(r"\bkaruna\b|\bmetta\b|loving.?kindness|compassion", re.I),
    "Middle Way": re.compile(r"middle\s+way|madhyamaka|middle\s+path", re.I),
    "Mindfulness": re.compile(r"mindful|sati\b|vipassana|meditation", re.I),
    "Moksha/Nirvana": re.compile(r"moksha|nirvana|nibbana|liberation.*cycle|samsara", re.I),
    "Upaya": re.compile(r"upaya|skillful\s+means", re.I),
    "Dukkha": re.compile(r"dukkha|suffering|four\s+noble\s+truth", re.I),
    "Vedanta/Texts": re.compile(r"vedant|upanishad|bhagavad|gita\b|purana|veda\b|vedic", re.I),
}

# Confucian Concept Keywords (simple containment — papers already filtered to Confucian subset)
CONFUCIAN_CONCEPT_KEYWORDS = {
    "Ren/仁 (Benevolence)": ["ren ", " ren", "仁", "benevolence", "humaneness", "human-heartedness"],
    "Li/禮 (Ritual)": ["禮", "ritual propriety", "propriety", "ritual"],
    "Yi/義 (Righteousness)": ["義", "righteousness"],
    "Zhi/智 (Wisdom)": ["智", "wisdom"],
    "Xin/信 (Fidelity)": ["信", "fidelity", "trustworthiness"],
    "Xiao/孝 (Filial Piety)": ["xiao", "孝", "filial piety", "filial"],
    "Junzi/君子": ["junzi", "君子", "exemplary person", "superior person"],
    "Harmony/和": ["harmony", "和谐", "harmonious", "social harmony"],
    "Mencius": ["mencius", "mengzi", "孟子", "four sprout"],
    "Five Relationships": ["five relationship", "five bond", "wu lun", "五倫", "five cardinal"],
    "Moral Cultivation": ["moral cultivat", "self-cultivat", "xiuyang", "修養"],
    "The Analects": ["analects", "lunyu", "論語"],
}

# Ubuntu/Indigenous Research Theme Patterns (for radar chart)
UBUNTU_THEME_PATTERNS = {
    "AI Governance": re.compile(r"governance|policy|regulat|guideline|framework.*ai|ai.*framework", re.I),
    "Data Sovereignty": re.compile(r"data\s+sovereign|OCAP|CARE\s+principle|indigenous\s+data|data.*right|data.*govern", re.I),
    "Decolonization": re.compile(r"decoloni|colonial|postcolonial|neo.?colonial|power.*imbalanc|global\s+south", re.I),
    "Language/NLP": re.compile(r"language.*model|nlp|natural\s+language|translat|corpus|low.?resource|endangered\s+lang", re.I),
    "Ethics & Values": re.compile(r"ethic|moral|value|virtue|justice|fairness|harm", re.I),
    "Robot/Agent Design": re.compile(r"robot|agent|embod|animis|kami|techno.?animis|anthropomorph", re.I),
    "Education": re.compile(r"educat|teach|learn|pedagog|curricul|school|universit", re.I),
    "Healthcare": re.compile(r"health|medical|clinic|patient|diagnos|bioethic", re.I),
}

# Shinto sub-tradition pattern (for Ubuntu/Indigenous breakdown)
SHINTO_PATTERN = re.compile(r"shinto|kami|techno.?animis|animis.*japan|japan.*animis", re.I)

# ── Per-Tradition Pattern Constants (from v4 for individual tradition tabs) ──

CHRISTIANITY_DENOM_PATTERNS = {
    "Catholic": re.compile(r"catholic|papal|vatican|pope|magisterium|encyclical", re.I),
    "Protestant": re.compile(r"protestant|reform|lutheran|calvini|evangelical|baptist|methodist|pentecost", re.I),
    "Orthodox": re.compile(r"orthodox\s+christian|eastern\s+orthodox|coptic|greek\s+orthodox|russian\s+orthodox", re.I),
    "Evangelical": re.compile(r"evangelic|born.?again|megachurch", re.I),
}
CHRISTIANITY_CONCEPT_PATTERNS = {
    "Natural Law": re.compile(r"natural\s+law|aquinas|thomist|thomistic", re.I),
    "Divine Command": re.compile(r"divine\s+command|god.s\s+will|theistic\s+ethics", re.I),
    "Thomistic Virtue": re.compile(r"thomistic\s+virtue|theological\s+virtue|faith.*hope.*charit|charity.*faith|aquinas.*virtue", re.I),
    "Liberation Theology": re.compile(r"liberation\s+theolog|preferential\s+option|option.*poor", re.I),
    "Imago Dei": re.compile(r"imago\s+dei|image\s+of\s+god", re.I),
    "Sola Scriptura": re.compile(r"sola\s+scriptura|scripture\s+alone|biblical\s+authority", re.I),
}
CHRISTIANITY_TEXT_PATTERNS = {
    "Old Testament": re.compile(r"old\s+testament|hebrew\s+bible|genesis|exodus|psalm|proverb|isaiah|deuteronom", re.I),
    "New Testament": re.compile(r"new\s+testament|gospel|matthew|mark|luke|john|paul.*epistle|revelation|acts\s+of", re.I),
    "Patristic": re.compile(r"patristic|church\s+father|augustin|chrysostom|athanasius", re.I),
}

# Judaism — concept & textual patterns
JUDAISM_CONCEPT_PATTERNS = {
    "Tikkun Olam": re.compile(r"tikkun\s+olam|repair.*world", re.I),
    "Pikuach Nefesh": re.compile(r"pikuach\s+nefesh|sanctity\s+of\s+life|preserv.*life", re.I),
    "Mussar": re.compile(r"mussar|musar", re.I),
    "Halakha": re.compile(r"halakh|jewish\s+law|halacha", re.I),
    "Tzedakah": re.compile(r"tzedakah|tzedaka|righteous.*giving|jewish.*charit", re.I),
    "B'tselem Elohim": re.compile(r"b.?tselem|image\s+of\s+god.*judai|judai.*image\s+of\s+god", re.I),
}
JUDAISM_TEXT_PATTERNS = {
    "Torah": re.compile(r"\btorah\b|pentateuch|five\s+books\s+of\s+moses", re.I),
    "Talmud": re.compile(r"\btalmud|talmudic|gemara", re.I),
    "Mishnah": re.compile(r"mishnah|mishnaic", re.I),
    "Midrash": re.compile(r"midrash|midrashic", re.I),
    "Responsa": re.compile(r"responsa|she.?elot|teshuvot", re.I),
}

# Buddhism — school, concept, textual patterns
BUDDHISM_SCHOOL_PATTERNS = {
    "Theravada": re.compile(r"theravada|pali\s+canon|hinayana|southern\s+buddhis", re.I),
    "Mahayana": re.compile(r"mahayana|bodhisattva|pure\s+land|northern\s+buddhis", re.I),
    "Vajrayana": re.compile(r"vajrayana|tantric\s+buddhis|tibetan\s+buddhis|dzogchen", re.I),
    "Zen": re.compile(r"\bzen\b|chan\s+buddhis|seon\s+buddhis|rinzai|soto", re.I),
    "Secular Buddhism": re.compile(r"secular\s+buddhis|modern\s+buddhis|engaged\s+buddhis", re.I),
}
BUDDHISM_CONCEPT_PATTERNS = {
    "Four Noble Truths": re.compile(r"four\s+noble\s+truth|dukkha|four\s+truth", re.I),
    "Eightfold Path": re.compile(r"eightfold\s+path|noble\s+eightfold|right\s+action.*right\s+speech", re.I),
    "Ahimsa": re.compile(r"ahimsa|non.?harm|non.?violen", re.I),
    "Karuna": re.compile(r"\bkaruna\b|compassion.*buddhis|buddhis.*compassion", re.I),
    "Metta": re.compile(r"\bmetta\b|loving.?kindness|maitri", re.I),
    "Upaya": re.compile(r"upaya|skillful\s+means", re.I),
    "Middle Way": re.compile(r"middle\s+way|madhyamaka|middle\s+path", re.I),
    "Dependent Origination": re.compile(r"dependent\s+originat|pratityasamutpada|conditioned\s+aris", re.I),
    "Sunyata": re.compile(r"sunyata|shunyata|emptiness.*buddhis|buddhis.*emptiness", re.I),
}
BUDDHISM_TEXT_PATTERNS = {
    "Pali Canon": re.compile(r"pali\s+canon|tipitaka|tripitaka|sutta\s+pitaka|vinaya", re.I),
    "Mahayana Sutras": re.compile(r"heart\s+sutra|diamond\s+sutra|lotus\s+sutra|prajnaparamita|mahayana\s+sutra", re.I),
    "Tibetan Texts": re.compile(r"tibetan\s+text|kangyur|tengyur|tibetan\s+canon|bardo\s+thodol", re.I),
}

# Hinduism — text, concept, school patterns
HINDUISM_TEXT_PATTERNS = {
    "Vedas": re.compile(r"\bveda[s]?\b|vedic|rigved|samaved|yajurved|atharva", re.I),
    "Upanishads": re.compile(r"upanishad", re.I),
    "Bhagavad Gita": re.compile(r"bhagavad|gita\b|geeta", re.I),
    "Dharmashastra": re.compile(r"dharmashastra|dharmasutra|smriti", re.I),
    "Manusmriti": re.compile(r"manusmriti|manu.*smriti|laws\s+of\s+manu", re.I),
}
HINDUISM_CONCEPT_PATTERNS = {
    "Dharma": re.compile(r"\bdharma\b(?!.*buddhis)|\bdharmic\b", re.I),
    "Karma": re.compile(r"\bkarma\b|karmic", re.I),
    "Moksha": re.compile(r"moksha|liberation.*cycle|samsara", re.I),
    "Ahimsa": re.compile(r"ahimsa|non.?harm|non.?violen", re.I),
    "Purushartha": re.compile(r"purushartha|four\s+aim|artha.*kama.*dharma", re.I),
    "Svadharma": re.compile(r"svadharma|personal\s+duty|caste\s+duty", re.I),
    "Rta": re.compile(r"\brta\b|cosmic\s+order|vedic\s+order", re.I),
}
HINDUISM_SCHOOL_PATTERNS = {
    "Vedanta": re.compile(r"vedanta|advaita|dvaita|vishishtadvaita|shankar", re.I),
    "Samkhya": re.compile(r"samkhya|sankhya", re.I),
    "Yoga": re.compile(r"yoga\s+philosoph|patanjali|yoga\s+sutra|raja\s+yoga", re.I),
    "Nyaya": re.compile(r"\bnyaya\b|nyaya.*logic|indian\s+logic", re.I),
    "Mimamsa": re.compile(r"mimamsa|mimansa", re.I),
}

# Shinto — concept & theme patterns
SHINTO_CONCEPT_PATTERNS = {
    "Kami": re.compile(r"\bkami\b(?!.*kaze)|spirit.*shinto|shinto.*spirit|divinit.*shinto", re.I),
    "Wa (Harmony)": re.compile(r"\bwa\b.*harmon|harmon.*\bwa\b|japanese\s+harmon", re.I),
    "Harae (Purification)": re.compile(r"harae|harai|purif.*shinto|shinto.*purif|misogi", re.I),
    "Ma": re.compile(r"\bma\b.*spac|negative\s+space|japanese\s+aesthet.*space", re.I),
    "Musubi": re.compile(r"musubi|creative.*interconnect|shinto.*creation", re.I),
}
SHINTO_THEME_PATTERNS = {
    "Techno-Animism": re.compile(r"techno.?animis|robot.*spirit|spirit.*robot|ai.*soul|soul.*ai", re.I),
    "Robot Ethics": re.compile(r"robot\s+ethic|robot.*moral|embodi.*ethic.*japan", re.I),
    "AI Personhood": re.compile(r"ai\s+person|machine\s+person|artificial.*person|robot.*person", re.I),
    "Cultural Alignment": re.compile(r"cultur.*align|japan.*value|japanese.*ethic|cultural.*ai.*japan", re.I),
}

# Ubuntu — concept & research theme patterns
UBUNTU_CONCEPT_PATTERNS = {
    "Communalism": re.compile(r"communal|community.*ethic|collective.*value|umuntu|ngumuntu", re.I),
    "Relational Personhood": re.compile(r"relational\s+person|person.*through.*person|relational\s+ontolog", re.I),
    "Indaba": re.compile(r"indaba|consensus.*decision|communal.*deliberat", re.I),
    "Restorative Justice": re.compile(r"restorative\s+justice|reconciliat|conflict.*resolut.*commun", re.I),
    "Collective Flourishing": re.compile(r"collective\s+flourish|communal.*flourish|common\s+good.*afric", re.I),
}
UBUNTU_RESEARCH_THEMES = {
    "AI Governance": re.compile(r"ai\s+governance|governance.*ai|regulat.*ai|ai.*regulat|policy.*ai", re.I),
    "Decolonization": re.compile(r"decoloni|colonial|postcolonial|neo.?colonial|global\s+south", re.I),
    "Data Ethics": re.compile(r"data\s+ethic|data\s+sovereign|data\s+justice|data.*right", re.I),
    "Community Values": re.compile(r"community\s+value|local.*value|indigenous.*value|communit.*centred", re.I),
}

# Indigenous — tradition & theme patterns
INDIGENOUS_TRADITION_PATTERNS = {
    "Maori": re.compile(r"maori|aotearoa|te\s+ao\s+maori|whanau|tikanga", re.I),
    "First Nations": re.compile(r"first\s+nation|metis|inuit|canadian\s+indigenous", re.I),
    "Aboriginal Australian": re.compile(r"aboriginal\s+austral|torres\s+strait|dreamtime|first\s+australi", re.I),
    "Native American": re.compile(r"native\s+american|american\s+indian|navajo|cherokee|lakota|ojibwe|hopi|apache", re.I),
}
INDIGENOUS_THEME_PATTERNS = {
    "Data Sovereignty": re.compile(r"data\s+sovereign|OCAP|CARE\s+principle|indigenous\s+data|data.*right.*indigen", re.I),
    "Decolonization": re.compile(r"decoloni|colonial.*indigen|indigen.*colonial|epistemic\s+justice", re.I),
    "Language Preservation": re.compile(r"language\s+preserv|endanger.*lang|revitali.*lang|indigenous.*lang|lang.*indigen", re.I),
    "Knowledge Systems": re.compile(r"indigenous\s+knowledge|traditional\s+knowledge|oral\s+tradition|knowledge\s+system", re.I),
    "Land/Place Ethics": re.compile(r"land.*ethic|place.*ethic|country.*connection|land.*connect|seven\s+generation", re.I),
}

# Other Traditions — Jainism, Sikhism, Taoism, Baha'i, Zoroastrianism
OTHER_TRADITIONS_CONCEPTS = {
    "Jainism": {
        "pattern": re.compile(r"jain|ahimsa.*jain|jain.*ahimsa|anekantavada|syadvada", re.I),
        "concepts": {"Ahimsa": re.compile(r"ahimsa|non.?violen", re.I),
                     "Anekantavada": re.compile(r"anekantavada|many.?sided|non.?absolut", re.I)},
    },
    "Sikhism": {
        "pattern": re.compile(r"sikh|guru\s+granth|gurdwara|khalsa|waheguru", re.I),
        "concepts": {"Seva": re.compile(r"\bseva\b|selfless\s+service", re.I),
                     "Equality": re.compile(r"sikh.*equal|equal.*sikh|langar|casteless", re.I)},
    },
    "Taoism": {
        "pattern": re.compile(r"taois[mt]|daois[mt]|tao\s+te|dao\s+de|lao\s?tzu|lao\s?zi|wu\s+wei|zhuangzi|chuang\s+tzu", re.I),
        "concepts": {"Wu Wei": re.compile(r"wu\s+wei|non.?action|effortless\s+action", re.I),
                     "Dao/Tao": re.compile(r"\btao\b|\bdao\b|the\s+way", re.I)},
    },
    "Baha'i": {
        "pattern": re.compile(r"baha.?i|baha.?ull|bahaism", re.I),
        "concepts": {"Unity": re.compile(r"unity.*human|human.*unity", re.I)},
    },
    "Zoroastrianism": {
        "pattern": re.compile(r"zoroastr|zarathustra|avesta|ahura\s+mazda|parsee|parsi\b(?!ng|mon)", re.I),
        "concepts": {"Good Thoughts": re.compile(r"good\s+thought|humata|good.*word.*deed|\basha\b(?!.*\bmap)", re.I)},
    },
}

# Chinese-origin LLM model family names (for Confucian Chinese vs Western analysis)
CHINESE_LLM_NAMES = {"Qwen", "ChatGLM", "Baichuan", "InternLM", "Yi", "DeepSeek", "ERNIE"}


# ── Normative Framework Patterns ──────────────────────────────────────────

NORMATIVE_FRAMEWORK_PATTERNS = {
    "Deontology/Kantian": re.compile(r'\bdeontolog|kantian|\bcategorical\s+imperative|duty[\s\-]based', re.I),
    "Consequentialism/Utilitarianism": re.compile(r'\bconsequential|utilitarian|\bgreatest\s+(?:good|happin)', re.I),
    "Virtue Ethics": re.compile(r'\bvirtue\s+ethic|aristotel|eudaimonia|phronesis|character\s+ethic', re.I),
    "Care Ethics": re.compile(r'\bcare\s+ethic|feminist\s+ethic|ethic\w?\s+of\s+care|relational\s+ethic', re.I),
    "Contractualism/Rawlsian": re.compile(r'\bcontractualis|rawls|social\s+contract|veil\s+of\s+ignorance', re.I),
    "Principlism": re.compile(r'\bprinciplism|beauchamp|non[\s\-]?maleficence|beneficence.*autonomy', re.I),
    "Confucian Ethics": re.compile(r'\bconfucian', re.I),
    "Islamic Ethics": re.compile(r'\bislamic\s+ethic|sharia|maqasid', re.I),
    "Distributive Justice": re.compile(r'\bdistributive\s+justice|egalitarian.*framework', re.I),
    "Moral Foundations Theory": re.compile(r'\bmoral\s+foundation|haidt.*foundation|MFT\b|MFQ\b', re.I),
    "Kohlberg's Moral Development": re.compile(r'\bkohlberg|moral\s+development\s+stage|DIT\b', re.I),
    "Commonsense Morality": re.compile(r'\bcommonsense\s+moral', re.I),
    "Natural Law": re.compile(r'\bnatural\s+law\b', re.I),
    "Social Choice Theory": re.compile(r'\bsocial\s+choice\s+theory', re.I),
}

# ── Conference Ecosystem Families ─────────────────────────────────────────

NLP_FAMILIES = {"ACL", "EMNLP", "NAACL", "COLING", "EACL", "AACL",
                "LREC", "LREC-COLING", "SemEval", "RANLP", "NoDaLiDa",
                "PROPOR", "ICON", "ROCLING", "STIL", "EVALITA", "IberLEF",
                "CLEF", "FIRE", "INTERSPEECH"}
ML_FAMILIES = {"NeurIPS", "ICML", "ICLR", "AAAI", "IJCAI", "COLM",
               "ECAI", "ECML-PKDD", "CVPR", "ECCV", "ICCV", "ACCV", "BMVC"}
ETHICS_FAMILIES = {"AIES", "FAccT"}


# ═══════════════════════════════════════════════════════════════════════════
# YAML SCANNER — Extended for v5
# ═══════════════════════════════════════════════════════════════════════════

YAML_SCALAR_FIELDS = {
    'moral_psychology', 'virtue_ethics', 'deontological_ethics',
    'utilitarian_ethics', 'religious_values', 'national_ethnic_cultural',
    'LLM_assessed', 'DATA_URL', 'ethics_overall', 'is_benchmark',
    'abstract', 'first_author', 'last_author', 'short_title',
    'url', 'doi', 'CONF-CC', 'year',
}
YAML_LIST_FIELDS = {'cultures_nationalities_list', 'languages_list', 'religious_values_list'}


def scan_all_paper_yaml():
    """Scan all papers for extended YAML fields needed by v5 dashboard."""
    results = {}
    for p in sorted(PAPERS_DIR.iterdir()):
        if not p.name.endswith('.md'):
            continue
        try:
            content = p.read_text(encoding='utf-8')
        except Exception:
            continue
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            continue

        fm_text = fm_match.group(1)
        record = {f: '' for f in YAML_SCALAR_FIELDS}
        record.update({f: [] for f in YAML_LIST_FIELDS})

        lines = fm_text.split('\n')
        current_list_field = None

        for line in lines:
            stripped = line.strip()
            # Check for list item continuation
            if current_list_field and (line.startswith('  - ') or line.startswith('\t- ') or stripped.startswith('- ')):
                item = stripped[2:].strip().strip('"').strip("'")
                if item and item.lower() not in ('n/a', 'na', 'none', ''):
                    record[current_list_field].append(item)
                continue
            elif current_list_field and stripped and not stripped.startswith('-'):
                current_list_field = None

            # Check for key: value
            if ':' in line and not line.startswith(' ') and not line.startswith('\t'):
                key = line.split(':', 1)[0].strip()
                val = line.split(':', 1)[1].strip()

                if key in YAML_LIST_FIELDS:
                    if val and val.lower() not in ('n/a', 'na', 'none', '""', "''"):
                        items = [v.strip().strip('"').strip("'") for v in val.split(',')]
                        record[key] = [v for v in items if v and v.lower() not in ('n/a', 'na', 'none')]
                    else:
                        current_list_field = key
                elif key in YAML_SCALAR_FIELDS:
                    record[key] = val.strip('"').strip("'")

        results[p.name] = record
    return results


# ═══════════════════════════════════════════════════════════════════════════
# SHARED HELPERS — Fix #1, #2, #3 from plan
# ═══════════════════════════════════════════════════════════════════════════

def get_benchmark_name(cand, paper_yaml_entry):
    """Return benchmark name with title fallback (Fix #3)."""
    name = cand.get("benchmark_name", "") or ""
    if name and name.lower() not in ("n/a", "na", "none", ""):
        return name[:60]
    title = paper_yaml_entry.get("short_title", "") or ""
    return title[:60]


def get_what_measures(cand, paper_yaml_entry):
    """Return what_measures with abstract-derived fallback (Fix #3)."""
    what = cand.get("what_measures", "") or ""
    if what and what.lower() not in ("n/a", "na", "none", ""):
        return what[:80]
    abstract = paper_yaml_entry.get("abstract", "") or ""
    first_sentence = abstract.split('. ')[0] if abstract else ""
    if len(first_sentence) > 80:
        first_sentence = first_sentence[:77] + "..."
    return first_sentence


def get_models_text(cand, yaml_fields):
    """Combine model names from candidates JSON + YAML LLM_assessed (Fix #2)."""
    models_text = cand.get("models_evaluated", "") or ""
    llm_assessed = yaml_fields.get("LLM_assessed", "") or ""
    if llm_assessed.lower() in ("na", "n/a", ""):
        llm_assessed = ""
    return f"{models_text} {llm_assessed}".strip()


def parse_llm_models(yaml_fields):
    """Parse LLM_assessed field into a list of model family names."""
    llm = yaml_fields.get("LLM_assessed", "") or ""
    if not llm or llm.lower() in ("na", "n/a", "none"):
        return []
    return extract_model_families(llm)


def clean_author(name):
    """Strip wikilink brackets and clean author names."""
    if not name:
        return ""
    # Remove [[ and ]]
    name = name.replace("[[", "").replace("]]", "")
    # Remove leading/trailing punctuation artifacts
    name = name.strip().strip(",").strip(")")
    return name[:40]


def parse_availability(val):
    v = (val or "N/A").strip()
    if v.startswith("Public"):
        return "Public"
    if v.startswith("Code") or "code available" in v.lower():
        return "Code available"
    if "not public" in v.lower():
        return "Not public"
    if "partial" in v.lower():
        return "Partially public"
    return "Not stated"


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 4: PER-PAPER DATA BUILDER
# ═══════════════════════════════════════════════════════════════════════════

def build_papers_array(paper_yaml, candidates, normative_entries, entry_cats=None):
    """Build compact per-paper objects for client-side filtering."""
    if entry_cats is None:
        entry_cats = {}
    cand_lookup = {e["filename"]: e for e in candidates}
    norm_lookup = {}
    for e in normative_entries:
        fn = e.get("filename", "")
        if fn:
            norm_lookup[fn] = e

    papers = []
    for i, (fn, fields) in enumerate(sorted(paper_yaml.items())):
        cand = cand_lookup.get(fn, {})

        # Year
        year_str = fields.get("year", "")
        year = int(year_str) if year_str and year_str.isdigit() else extract_year(fn)
        if year == 9999:
            year = 0

        # CONF-CC and venue classification
        conf_cc = fields.get("CONF-CC", "") or "N/A"
        venue_type = categorize_venue(conf_cc)
        conf_family = extract_conference_family(conf_cc)

        # Ethics flags
        eo = 1 if fields.get("ethics_overall", "").lower() in ("yes",) else 0
        ve = 1 if fields.get("virtue_ethics", "").lower() in ("yes", "partial", "true") else 0
        de = 1 if fields.get("deontological_ethics", "").lower() in ("yes", "partial", "true") else 0
        ue = 1 if fields.get("utilitarian_ethics", "").lower() in ("yes", "partial", "true") else 0

        # Benchmark flags
        is_bench = 1 if fn in cand_lookup else 0
        is_eval = 1 if cand.get("decision", "").lower() == "yes" else 0
        # Dataset: if candidate has benchmark, consider it a dataset
        is_dataset = 1 if cand.get("availability", "").lower().startswith("public") else 0

        # Moral psychology
        mp_val = fields.get("moral_psychology", "") or ""
        mp = mp_val if mp_val.lower() not in ("n/a", "na", "no", "none", "", "false") else ""

        # Cultures, regions, languages
        cultures = fields.get("cultures_nationalities_list", [])
        regions = list(set(classify_region(c) for c in cultures)) if cultures else []
        languages = fields.get("languages_list", [])

        # Religious values
        relig_list = fields.get("religious_values_list", [])
        relig_val = fields.get("religious_values", "") or ""
        rv = classify_relig_traditions(relig_list, relig_val)

        # LLM models
        lm = parse_llm_models(fields)

        # URLs
        data_url = fields.get("DATA_URL", "") or ""
        if data_url.lower() in ("na", "n/a", "none"):
            data_url = ""
        paper_url = fields.get("url", "") or ""
        doi = fields.get("doi", "") or ""

        # Abstract (truncated to 200 chars for size — enough for search + preview)
        abstract = fields.get("abstract", "") or ""
        if len(abstract) > 200:
            abstract = abstract[:197] + "..."

        # Benchmark name and what measures (with fallbacks)
        bn = get_benchmark_name(cand, fields)
        wm = get_what_measures(cand, fields)

        # Short title and authors (strip wikilink brackets)
        short_title = fields.get("short_title", "") or fn.replace(".md", "")
        first_author = clean_author(fields.get("first_author", ""))
        last_author = clean_author(fields.get("last_author", ""))

        papers.append({
            "i": i,
            "fn": fn,
            "t": short_title[:80],
            "fa": first_author[:40],
            "la": last_author[:40],
            "y": year,
            "cc": conf_cc,
            "vt": venue_type,
            "cf": conf_family,
            "eo": eo,
            "ve": ve, "de": de, "ue": ue,
            "ib": is_bench, "ie": is_eval, "id": is_dataset,
            "mp": mp[:60],
            "cu": cultures[:5],  # cap at 5 cultures
            "rg": regions[:3],
            "ln": languages[:5],
            "rv": rv,
            "lm": lm[:5],
            "du": data_url[:200],
            "ab": abstract,
            "bn": bn,
            "wm": wm,
            "url": paper_url[:200],
            "doi": doi[:80],
            "cs": entry_cats.get(fn, []),
        })

    return papers


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 5: AGGREGATED DATA
# ═══════════════════════════════════════════════════════════════════════════

def build_aggregated_data(papers, paper_yaml, candidates, author_map, entry_cats=None):
    """Build pre-aggregated data for KPIs and chart defaults."""
    total = len(papers)
    cand_count = sum(1 for p in papers if p["ib"])

    # Year range
    years = sorted(set(p["y"] for p in papers if p["y"] > 0))
    year_range = [min(years), max(years)] if years else [2016, 2026]

    # Venue type distribution
    vt_dist = Counter(p["vt"] for p in papers)

    # Ethics stats
    ethics_yes = sum(1 for p in papers if p["eo"])

    # Cultures/languages/religions unique
    all_cultures = set()
    all_languages = set()
    all_religions = set()
    for p in papers:
        all_cultures.update(p["cu"])
        all_languages.update(p["ln"])
        all_religions.update(p["rv"])

    # LLM assessment stats
    llm_assessed_count = sum(1 for fn, f in paper_yaml.items()
                             if f.get("LLM_assessed", "NA") not in ("NA", "N/A", "", "na"))
    data_url_count = sum(1 for fn, f in paper_yaml.items()
                         if f.get("DATA_URL", "NA") not in ("NA", "N/A", "", "na"))

    # Top authors — count ALL author positions, dedup by normalized name
    all_authors_set = set()
    author_counter = Counter()
    for stem, info in author_map.items():
        for name in info.get("authors", []):
            norm = " ".join(sorted(name.lower().replace(",", "").replace(".", "").split()))
            all_authors_set.add(norm)
            author_counter[name] += 1
    top_authors = [{"n": n, "c": c} for n, c in author_counter.most_common(15)]

    # Availability distribution
    avail_counter = Counter()
    for e in candidates:
        avail_counter[parse_availability(e.get("availability", ""))] += 1

    # Unique category names for dropdown population
    all_cats = sorted(set(c for cats in (entry_cats or {}).values() for c in cats))

    return {
        "total": total,
        "candidates": cand_count,
        "ethicsYes": ethics_yes,
        "yearRange": year_range,
        "vtDist": dict(vt_dist),
        "cultureCount": len(all_cultures),
        "languageCount": len(all_languages),
        "religionCount": len(all_religions),
        "llmAssessed": llm_assessed_count,
        "dataUrls": data_url_count,
        "topAuthors": top_authors,
        "authorCount": len(all_authors_set),
        "availability": dict(avail_counter),
        "categories": all_cats,
    }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 6: CONFERENCE DATA
# ═══════════════════════════════════════════════════════════════════════════

def build_conference_data(papers):
    """Build conference & venue tab data."""
    # Family counter
    family_counter = Counter()
    family_year = defaultdict(Counter)
    family_tracks = defaultdict(Counter)

    for p in papers:
        if p["vt"] in ("Preprint", "N/A", "Journal"):
            continue
        fam = p["cf"]
        if not fam:
            continue
        family_counter[fam] += 1
        if p["y"] > 0:
            family_year[fam][p["y"]] += 1
        # Track type
        cc = p["cc"]
        if "Findings" in cc:
            family_tracks[fam]["Findings"] += 1
        elif "Workshop" in cc:
            family_tracks[fam]["Workshop"] += 1
        elif "Demo" in cc:
            family_tracks[fam]["Demo"] += 1
        else:
            family_tracks[fam]["Main"] += 1

    # Top 30 venues (excluding Preprint/N/A)
    venue_counter = Counter()
    for p in papers:
        if p["cc"] not in ("Preprint", "N/A"):
            venue_counter[p["cc"]] += 1
    top_venues = [{"n": v, "c": c, "vt": categorize_venue(v)}
                  for v, c in venue_counter.most_common(30)]

    # Conference families (top 20)
    families = []
    for fam, count in family_counter.most_common(20):
        tracks = family_tracks[fam]
        ecosystem = "NLP/CL" if fam in NLP_FAMILIES else (
            "ML/AI" if fam in ML_FAMILIES else (
                "AI Ethics" if fam in ETHICS_FAMILIES else "Other"))
        families.append({
            "n": fam,
            "c": count,
            "main": tracks.get("Main", 0),
            "findings": tracks.get("Findings", 0),
            "workshop": tracks.get("Workshop", 0),
            "eco": ecosystem,
        })

    # Family x year heatmap (top 15 x years)
    top15_fams = [f for f, _ in family_counter.most_common(15)]
    hm_years = sorted(set(y for fc in family_year.values() for y in fc.keys()
                          if 2018 <= y <= 2026))
    heatmap = []
    for fam in top15_fams:
        row = [family_year[fam].get(y, 0) for y in hm_years]
        heatmap.append({"n": fam, "d": row})

    # Ecosystem distribution
    nlp_total = sum(family_counter.get(f, 0) for f in NLP_FAMILIES)
    ml_total = sum(family_counter.get(f, 0) for f in ML_FAMILIES)
    ethics_total = sum(family_counter.get(f, 0) for f in ETHICS_FAMILIES)
    other_total = sum(family_counter.values()) - nlp_total - ml_total - ethics_total
    ecosystem = [
        {"n": "NLP/CL", "c": nlp_total},
        {"n": "ML/AI", "c": ml_total},
        {"n": "AI Ethics", "c": ethics_total},
        {"n": "Other", "c": other_total},
    ]

    # Journal list (top 20)
    journal_counter = Counter()
    for p in papers:
        if p["vt"] == "Journal":
            journal_counter[p["cc"]] += 1
    journals = [{"n": j, "c": c} for j, c in journal_counter.most_common(20)]

    # Timeline: year x venue type
    year_vt = defaultdict(Counter)
    for p in papers:
        if p["y"] > 0:
            year_vt[p["y"]][p["vt"]] += 1
    tl_years = sorted(y for y in year_vt.keys() if y >= 2016)
    timeline = {
        "years": tl_years,
        "Conference": [year_vt[y].get("Conference", 0) for y in tl_years],
        "Preprint": [year_vt[y].get("Preprint", 0) for y in tl_years],
        "Journal": [year_vt[y].get("Journal", 0) for y in tl_years],
        "Findings": [year_vt[y].get("Findings", 0) for y in tl_years],
        "Workshop": [year_vt[y].get("Workshop", 0) for y in tl_years],
    }

    # Peer-review ratio over time
    peer_ratio = []
    for y in tl_years:
        total_y = sum(year_vt[y].values())
        if total_y == 0:
            continue
        peer = year_vt[y].get("Conference", 0) + year_vt[y].get("Journal", 0) + \
               year_vt[y].get("Findings", 0) + year_vt[y].get("Workshop", 0)
        peer_ratio.append({"y": y, "pct": round(peer * 100 / total_y, 1)})

    return {
        "topVenues": top_venues,
        "families": families,
        "heatmap": heatmap,
        "hmYears": hm_years,
        "ecosystem": ecosystem,
        "journals": journals,
        "timeline": timeline,
        "peerRatio": peer_ratio,
        "uniqueVenues": len(venue_counter) + 2,  # +Preprint +N/A
    }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 7: DEEP-DIVE SECTION BUILDERS (FIXED)
# ═══════════════════════════════════════════════════════════════════════════

# ── Co-occurrence Matrix Helper ──────────────────────────────────────────

def build_cooccurrence_matrix(papers, keyword_dict):
    """Build keyword co-occurrence matrix from paper keyword lists."""
    labels = sorted(keyword_dict.keys())
    n = len(labels)
    label_idx = {l: i for i, l in enumerate(labels)}
    matrix = [[0] * n for _ in range(n)]
    for sp in papers:
        kws = sp.get("kw", [])
        for i, a in enumerate(kws):
            if a not in label_idx:
                continue
            ai = label_idx[a]
            matrix[ai][ai] += 1  # diagonal = occurrences
            for b in kws[i+1:]:
                if b not in label_idx:
                    continue
                bi = label_idx[b]
                matrix[ai][bi] += 1
                matrix[bi][ai] += 1
    return labels, matrix


# ── Sub-Tradition Definitions ────────────────────────────────────────────

VE_SUB_TRADITIONS = {
    "Aristotelian": re.compile(r'aristot|phronesis|eudaimonia|practical\s+wisdom|nicomachean', re.I),
    "Confucian": re.compile(r'confuci|junzi|ren\b|li\b.*ritual|five\s+relationship', re.I),
    "Sentimentalist": re.compile(r'sentimentali|moral\s+sentiment|hume.*virtue|sympathy.*ethic', re.I),
    "Capability": re.compile(r'capabilit.*approach|nussbaum|sen.*capabilit|human\s+capabilit', re.I),
}
DE_SUB_TRADITIONS = {
    "Kantian": re.compile(r'kantian|categorical\s+imperative|universaliz|universal\s+law', re.I),
    "Rossian": re.compile(r'ross(?:ian)?|prima\s+facie\s+dut', re.I),
    "Rights-based": re.compile(r'rights[\s\-]based|human\s+rights|natural\s+rights|right\s+to', re.I),
}
CU_SUB_TRADITIONS = {
    "Act": re.compile(r'act\s+utilitari|act[\s\-]consequential', re.I),
    "Rule": re.compile(r'rule\s+utilitari|rule[\s\-]consequential', re.I),
    "Preference": re.compile(r'preference\s+utilitari|preference\s+satisfac', re.I),
}


def scan_sub_traditions(title, abstract, sub_dict):
    """Scan title+abstract for sub-tradition patterns."""
    text = (title + " " + abstract).lower() if title or abstract else ""
    found = []
    for name, pat in sub_dict.items():
        if pat.search(text):
            found.append(name)
    return found


# ── Concept Timeline Helper ──────────────────────────────────────────────

def build_concept_timeline(papers, keyword_dict, top_n=8):
    """Build concept-over-time series for top N keywords."""
    kw_year = defaultdict(Counter)
    for sp in papers:
        y = sp.get("y", 0)
        if y < 2016:
            continue
        for k in sp.get("kw", []):
            kw_year[k][y] += 1
    # Top N by total count
    totals = {k: sum(yc.values()) for k, yc in kw_year.items()}
    top_kws = sorted(totals, key=totals.get, reverse=True)[:top_n]
    if not top_kws:
        return {"years": [], "concepts": [], "series": []}
    all_years = sorted(set(y for k in top_kws for y in kw_year[k]))
    series = []
    for kw in top_kws:
        series.append({
            "name": kw,
            "data": [kw_year[kw].get(y, 0) for y in all_years],
        })
    return {"years": all_years, "concepts": top_kws, "series": series}


def compute_normative_data(normative_entries, candidates, paper_yaml, candidates_set):
    """Compute normative ethics data with FIXED sub-sections."""
    cand_lookup = {e["filename"]: e for e in candidates}

    yes_entries = [e for e in normative_entries if e.get("decision") == "Yes"]
    border_entries = [e for e in normative_entries if e.get("decision") == "Borderline"]
    excluded_count = len(normative_entries) - len(yes_entries) - len(border_entries)

    # Framework distribution
    fw_counts = Counter()
    for e in yes_entries + border_entries:
        nf = e.get("normative_frameworks", "N/A")
        reasoning = e.get("reasoning", "")
        search_text = f"{nf} {reasoning}"
        for fw_name, pat in NORMATIVE_FRAMEWORK_PATTERNS.items():
            if pat.search(search_text):
                fw_counts[fw_name] += 1
    frameworks = [{"n": n, "c": c} for n, c in fw_counts.most_common()]

    # Build normative papers list (main list — already correct in v3)
    normative_papers_set = set()
    normative_papers = []
    for e in yes_entries + border_entries:
        fn = e.get("filename", "")
        normative_papers_set.add(fn)
        cand = cand_lookup.get(fn, {})
        fields = paper_yaml.get(fn, {})
        paper_fws = []
        search_text = f"{e.get('normative_frameworks', '')} {e.get('reasoning', '')}"
        if NORMATIVE_FRAMEWORK_PATTERNS["Virtue Ethics"].search(search_text):
            paper_fws.append("VE")
        if NORMATIVE_FRAMEWORK_PATTERNS["Deontology/Kantian"].search(search_text):
            paper_fws.append("DE")
        if NORMATIVE_FRAMEWORK_PATTERNS["Consequentialism/Utilitarianism"].search(search_text):
            paper_fws.append("CU")
        normative_papers.append({
            "fn": fn,
            "y": extract_year(fn),
            "d": e.get("decision", ""),
            "bn": get_benchmark_name(cand, fields),
            "wm": get_what_measures(cand, fields),
            "lm": (cand.get("models_evaluated", "") or e.get("llms_tested", ""))[:60],
            "fws": paper_fws,
        })

    # Also include YAML-flagged papers
    for fn, fields in paper_yaml.items():
        if fn in normative_papers_set:
            continue
        ve_v = fields.get('virtue_ethics', '').lower()
        de_v = fields.get('deontological_ethics', '').lower()
        cu_v = fields.get('utilitarian_ethics', '').lower()
        has_normative = any(v in ('yes', 'partial', 'true') for v in [ve_v, de_v, cu_v])
        if has_normative and fn in candidates_set:
            cand = cand_lookup.get(fn, {})
            paper_fws = []
            if ve_v in ('yes', 'partial', 'true'):
                paper_fws.append("VE")
            if de_v in ('yes', 'partial', 'true'):
                paper_fws.append("DE")
            if cu_v in ('yes', 'partial', 'true'):
                paper_fws.append("CU")
            normative_papers_set.add(fn)
            normative_papers.append({
                "fn": fn,
                "y": extract_year(fn),
                "d": "YAML",
                "bn": get_benchmark_name(cand, fields),
                "wm": get_what_measures(cand, fields),
                "lm": (cand.get("models_evaluated", ""))[:60],
                "fws": paper_fws,
            })

    normative_papers.sort(key=lambda x: x["fn"])

    # ── VE / DE / CU sub-sections — FIXED: return full paper objects ──
    def build_fw_subsection(yaml_field, fw_code, scan_fn=None):
        sub_papers = []
        year_dist = Counter()
        model_counter = Counter()
        venue_counter = Counter()
        region_counter = Counter()
        theory_vs_emp = Counter()  # "Benchmark / Evaluation" vs "Theoretical / Framework"
        research_type_5 = Counter()
        bench_count = 0
        for fn, fields in paper_yaml.items():
            val = fields.get(yaml_field, '').lower()
            if val not in ('yes', 'partial', 'true'):
                continue
            year = extract_year(fn)
            if year == 9999:
                year = 0
            cand = cand_lookup.get(fn, {})
            # FIX #2: get models from BOTH candidates AND YAML LLM_assessed
            combined_model_text = get_models_text(cand, fields)
            for m in extract_model_families(combined_model_text):
                model_counter[m] += 1
            if fn in cand_lookup:
                bench_count += 1
            if year > 0:
                year_dist[year] += 1

            # Venue type
            conf_cc = fields.get("CONF-CC", "") or "N/A"
            vt = categorize_venue(conf_cc)
            venue_counter[vt] += 1

            # Region
            cultures = fields.get("cultures_nationalities_list", [])
            paper_regions = set()
            for c in (cultures if isinstance(cultures, list) else []):
                r = classify_region(c)
                region_counter[r] += 1
                paper_regions.add(r)

            # Theory vs Empirical
            abstract = fields.get("abstract", "") or ""
            if fn in cand_lookup:
                theory_vs_emp["Benchmark / Evaluation"] += 1
            else:
                theory_vs_emp["Theoretical / Framework"] += 1

            # 5-category research type
            if fn in cand_lookup:
                # Distinguish benchmark evaluation from non-benchmark empirical
                research_type_5["Empirical Benchmark"] += 1
            elif abstract and any(w in abstract.lower() for w in ["experiment", "dataset", "survey", "participant", "sample", "collected", "annotation"]):
                research_type_5["Empirical Non-Benchmark"] += 1
            elif abstract and any(w in abstract.lower() for w in ["mixed", "qualitative", "interview", "case study"]):
                research_type_5["Mixed Methods"] += 1
            elif abstract and any(w in abstract.lower() for w in ["dataset", "corpus", "resource", "benchmark", "annotation tool"]):
                research_type_5["Dataset/Resource"] += 1
            else:
                research_type_5["Philosophical Analysis"] += 1

            # Per-paper concept/virtue keywords (for click-to-filter)
            kw = []
            if scan_fn:
                _title = fields.get("title", "") or fields.get("short_title", fn)
                _abstract = abstract
                kw = sorted(scan_fn(_title, _abstract))

            # Sub-traditions
            st = []
            if scan_fn:
                if scan_fn == scan_virtue_keywords:
                    st = scan_sub_traditions(_title, _abstract, VE_SUB_TRADITIONS)
                elif scan_fn == scan_deontology_keywords:
                    st = scan_sub_traditions(_title, _abstract, DE_SUB_TRADITIONS)
                elif scan_fn == scan_cu_concepts:
                    st = scan_sub_traditions(_title, _abstract, CU_SUB_TRADITIONS)

            # FIX #1: return full paper objects, not just filenames
            sub_papers.append({
                "fn": fn,
                "y": year,
                "ib": 1 if fn in cand_lookup else 0,
                "bn": get_benchmark_name(cand, fields),
                "wm": get_what_measures(cand, fields),
                "lm": extract_model_families(combined_model_text)[:5],
                "vt": vt,
                "rg": sorted(paper_regions),
                "kw": kw,
                "st": st,
            })
        # Depth histogram and mean depth
        depth_counts = Counter(len(sp.get("kw", [])) for sp in sub_papers)
        depth_hist = [{"depth": d, "count": c} for d, c in sorted(depth_counts.items())]
        total_kw = sum(len(sp.get("kw", [])) for sp in sub_papers)
        mean_depth = round(total_kw / max(len(sub_papers), 1), 2)

        return {
            "papers": sub_papers,
            "count": len(sub_papers),
            "benchmarkCount": bench_count,
            "yearDist": {str(y): c for y, c in sorted(year_dist.items()) if y >= 2016},
            "topModels": [{"n": n, "c": c} for n, c in model_counter.most_common(10)],
            "theoryVsEmpirical": [{"n": n, "c": c} for n, c in theory_vs_emp.most_common()],
            "venueTypeDist": [{"n": n, "c": c} for n, c in venue_counter.most_common()],
            "regionDist": [{"n": n, "c": c} for n, c in region_counter.most_common()],
            "depthHist": depth_hist,
            "meanDepth": mean_depth,
            "researchType5": [{"n": n, "c": c} for n, c in research_type_5.most_common()],
        }

    ve_data = build_fw_subsection('virtue_ethics', 'VE', scan_fn=scan_virtue_keywords)
    ve_data["virtueKeywords"] = [{"n": n, "c": c} for n, c in
        Counter(k for sp in ve_data["papers"] for k in sp.get("kw", [])).most_common()]
    # Co-occurrence matrix
    labels, matrix = build_cooccurrence_matrix(ve_data["papers"], VIRTUE_KEYWORDS)
    ve_data["coocLabels"] = labels
    ve_data["coocMatrix"] = matrix
    # Sub-traditions
    ve_data["subTraditions"] = [{"n": n, "c": c} for n, c in
        Counter(s for sp in ve_data["papers"] for s in sp.get("st", [])).most_common()]
    # Concept timeline
    ve_data["conceptTimeline"] = build_concept_timeline(ve_data["papers"], VIRTUE_KEYWORDS)

    de_data = build_fw_subsection('deontological_ethics', 'DE', scan_fn=scan_deontology_keywords)
    de_data["deontConcepts"] = [{"n": n, "c": c} for n, c in
        Counter(k for sp in de_data["papers"] for k in sp.get("kw", [])).most_common()]
    # Co-occurrence matrix
    labels, matrix = build_cooccurrence_matrix(de_data["papers"], DEONTOLOGY_KEYWORDS)
    de_data["coocLabels"] = labels
    de_data["coocMatrix"] = matrix
    # Sub-traditions
    de_data["subTraditions"] = [{"n": n, "c": c} for n, c in
        Counter(s for sp in de_data["papers"] for s in sp.get("st", [])).most_common()]
    # Concept timeline
    de_data["conceptTimeline"] = build_concept_timeline(de_data["papers"], DEONTOLOGY_KEYWORDS)

    cu_data = build_fw_subsection('utilitarian_ethics', 'CU', scan_fn=scan_cu_concepts)
    cu_data["cuConcepts"] = [{"n": n, "c": c} for n, c in
        Counter(k for sp in cu_data["papers"] for k in sp.get("kw", [])).most_common()]
    # Co-occurrence matrix
    labels, matrix = build_cooccurrence_matrix(cu_data["papers"], CU_CONCEPT_KEYWORDS)
    cu_data["coocLabels"] = labels
    cu_data["coocMatrix"] = matrix
    # Sub-traditions
    cu_data["subTraditions"] = [{"n": n, "c": c} for n, c in
        Counter(s for sp in cu_data["papers"] for s in sp.get("st", [])).most_common()]
    # Concept timeline
    cu_data["conceptTimeline"] = build_concept_timeline(cu_data["papers"], CU_CONCEPT_KEYWORDS)

    # Overlap
    ve_fns = set(p["fn"] for p in ve_data["papers"])
    de_fns = set(p["fn"] for p in de_data["papers"])
    cu_fns = set(p["fn"] for p in cu_data["papers"])

    # 1a. Pairwise and triple overlap sets
    ve_de_set = ve_fns & de_fns
    ve_cu_set = ve_fns & cu_fns
    de_cu_set = de_fns & cu_fns
    all_three_set = ve_fns & de_fns & cu_fns

    # Exclusive sets (each paper in exactly one segment)
    ve_only = ve_fns - de_fns - cu_fns
    de_only = de_fns - ve_fns - cu_fns
    cu_only = cu_fns - ve_fns - de_fns
    ve_de_excl = (ve_fns & de_fns) - cu_fns
    ve_cu_excl = (ve_fns & cu_fns) - de_fns
    de_cu_excl = (de_fns & cu_fns) - ve_fns

    # 1b. Paper lookup from all 3 sub-sections
    all_fw_papers = {}
    for p in ve_data["papers"] + de_data["papers"] + cu_data["papers"]:
        all_fw_papers.setdefault(p["fn"], p)

    # 1c. Paper lists for each overlap combination
    def papers_for_set(fn_set):
        return sorted([all_fw_papers[fn] for fn in fn_set if fn in all_fw_papers],
                      key=lambda p: (-p["y"], p["fn"]))

    overlap = {
        "ve_de": len(ve_de_set),
        "ve_cu": len(ve_cu_set),
        "de_cu": len(de_cu_set),
        "all": len(all_three_set),
        "ve_de_papers": papers_for_set(ve_de_set),
        "ve_cu_papers": papers_for_set(ve_cu_set),
        "de_cu_papers": papers_for_set(de_cu_set),
        "all_papers": papers_for_set(all_three_set),
        "any_papers": papers_for_set(ve_de_set | ve_cu_set | de_cu_set),
    }

    # 1e. Exclusivity breakdown (for sunburst)
    overlap["exclusivity"] = {
        "ve": {"only": len(ve_only), "ve_de": len(ve_de_excl), "ve_cu": len(ve_cu_excl), "all": len(all_three_set)},
        "de": {"only": len(de_only), "ve_de": len(ve_de_excl), "de_cu": len(de_cu_excl), "all": len(all_three_set)},
        "cu": {"only": len(cu_only), "ve_cu": len(ve_cu_excl), "de_cu": len(de_cu_excl), "all": len(all_three_set)},
    }

    # 1f. Overlap model comparison
    overlap_models = {}
    for combo_name, combo_set in [("ve_de", ve_de_set), ("ve_cu", ve_cu_set),
                                   ("de_cu", de_cu_set), ("all", all_three_set)]:
        mc = Counter()
        for fn in combo_set:
            p = all_fw_papers.get(fn)
            if p:
                for m in (p.get("lm") or []):
                    mc[m] += 1
        overlap_models[combo_name] = [{"n": n, "c": c} for n, c in mc.most_common(8)]
    overlap["overlapModels"] = overlap_models

    # 1g. Framework x Region heatmap
    combo_labels = ["VE only", "DE only", "CU only", "VE+DE", "VE+CU", "DE+CU", "All Three"]
    combo_sets = [ve_only, de_only, cu_only, ve_de_excl, ve_cu_excl, de_cu_excl, all_three_set]
    region_set = set()
    combo_region_counts = []
    for fn_set in combo_sets:
        rc = Counter()
        for fn in fn_set:
            cultures = paper_yaml.get(fn, {}).get("cultures_nationalities_list", [])
            for c in (cultures if isinstance(cultures, list) else []):
                r = classify_region(c)
                rc[r] += 1
                region_set.add(r)
        combo_region_counts.append(rc)
    region_labels = sorted(region_set - {"Other"}) + (["Other"] if "Other" in region_set else [])
    heatmap_matrix = []
    for rc in combo_region_counts:
        heatmap_matrix.append([rc.get(r, 0) for r in region_labels])
    overlap["regionHeatmap"] = {"comboLabels": combo_labels, "regionLabels": region_labels, "matrix": heatmap_matrix}

    # 1h. Benchmark density by overlap combination
    for combo_name, combo_set in [("ve_de", ve_de_set), ("ve_cu", ve_cu_set),
                                   ("de_cu", de_cu_set), ("all", all_three_set)]:
        bc = sum(1 for fn in combo_set if fn in candidates_set)
        overlap[f"{combo_name}_bench"] = bc
        overlap[f"{combo_name}_pct"] = round(100 * bc / max(len(combo_set), 1), 1)
    single_fw = ve_only | de_only | cu_only
    sbc = sum(1 for fn in single_fw if fn in candidates_set)
    overlap["single_bench"] = sbc
    overlap["single_total"] = len(single_fw)
    overlap["single_pct"] = round(100 * sbc / max(len(single_fw), 1), 1)

    # Timeline by framework
    all_years = sorted(set(
        list(ve_data["yearDist"].keys()) +
        list(de_data["yearDist"].keys()) +
        list(cu_data["yearDist"].keys())
    ))
    timeline_fw = {
        "years": [int(y) for y in all_years],
        "ve": [int(ve_data["yearDist"].get(y, 0)) for y in all_years],
        "de": [int(de_data["yearDist"].get(y, 0)) for y in all_years],
        "cu": [int(cu_data["yearDist"].get(y, 0)) for y in all_years],
    }

    # 1d. Overlap timeline by year
    overlap_years = [int(y) for y in all_years]
    overlap_timeline = {"years": overlap_years}
    for combo_name, combo_set in [("ve_de", ve_de_set), ("ve_cu", ve_cu_set),
                                   ("de_cu", de_cu_set), ("all", all_three_set)]:
        yc = Counter(all_fw_papers[fn]["y"] for fn in combo_set if fn in all_fw_papers)
        overlap_timeline[combo_name] = [yc.get(y, 0) for y in overlap_years]
    overlap["overlapTimeline"] = overlap_timeline

    # ── Item 9: Overlap Typology ─────────────────────────────────────
    typology_counter = Counter()
    any_overlap_fns = ve_de_set | ve_cu_set | de_cu_set
    for fn in any_overlap_fns:
        # Check normative entries for reasoning
        entry = next((e for e in normative_entries if e.get("filename") == fn), None)
        reasoning = (entry.get("reasoning", "") if entry else "").lower()
        if any(w in reasoning for w in ["compar", "contrast", "versus", "differ"]):
            typology_counter["Comparative"] += 1
        elif any(w in reasoning for w in ["integrat", "combin", "synthesiz", "reconcil", "bridg"]):
            typology_counter["Integrative"] += 1
        else:
            typology_counter["Incidental"] += 1
    overlap["typology"] = [{"n": n, "c": c} for n, c in typology_counter.most_common()]

    # ── Item 3: Comparative Radar ────────────────────────────────────
    def _compute_comparative_dims(fw_data, fw_fns, paper_yaml, candidates_set):
        """Compute 6 comparative dimensions for a framework."""
        papers = fw_data["papers"]
        n = max(len(papers), 1)
        # 1. Benchmark %
        bench_pct = round(100 * fw_data["benchmarkCount"] / n, 1)
        # 2. Mean depth (keyword count)
        total_kw = sum(len(sp.get("kw", [])) for sp in papers)
        mean_depth = round(total_kw / n, 2)
        # 3. Non-WEIRD %
        non_weird = 0
        for fn in fw_fns:
            cultures = paper_yaml.get(fn, {}).get("cultures_nationalities_list", [])
            for c in (cultures if isinstance(cultures, list) else []):
                r = classify_region(c)
                if r not in ("North America", "Western Europe", "Mixed", "Unknown"):
                    non_weird += 1
                    break
        non_weird_pct = round(100 * non_weird / n, 1)
        # 4. Median models per paper
        model_counts = [len(sp.get("lm", [])) for sp in papers]
        model_counts.sort()
        median_models = model_counts[len(model_counts) // 2] if model_counts else 0
        # 5. Conference %
        conf_count = sum(1 for sp in papers if sp.get("vt") == "Conference")
        conf_pct = round(100 * conf_count / n, 1)
        # 6. Growth rate (latest 2 years)
        yd = fw_data["yearDist"]
        years_sorted = sorted(int(y) for y in yd.keys())
        if len(years_sorted) >= 2:
            prev = yd.get(str(years_sorted[-2]), 0)
            curr = yd.get(str(years_sorted[-1]), 0)
            growth = round(100 * (curr - prev) / max(prev, 1), 1)
        else:
            growth = 0.0
        return {
            "benchmarkPct": bench_pct,
            "meanDepth": mean_depth,
            "nonWeirdPct": non_weird_pct,
            "medianModels": median_models,
            "conferencePct": conf_pct,
            "growthRate": growth,
        }

    comparative_indicators = [
        {"name": "Benchmark %", "max": 100},
        {"name": "Mean Depth", "max": 6},
        {"name": "Non-WEIRD %", "max": 100},
        {"name": "Median Models", "max": 5},
        {"name": "Conference %", "max": 100},
        {"name": "Growth Rate %", "max": 200},
    ]
    comparative_series = []
    for fw_key, fw_data_ref, fw_fns_ref, fw_name in [
        ("ve", ve_data, ve_fns, "Virtue Ethics"),
        ("de", de_data, de_fns, "Deontological"),
        ("cu", cu_data, cu_fns, "Consequentialism"),
    ]:
        dims = _compute_comparative_dims(fw_data_ref, fw_fns_ref, paper_yaml, candidates_set)
        comparative_series.append({
            "name": fw_name,
            "data": [dims["benchmarkPct"], dims["meanDepth"], dims["nonWeirdPct"],
                     dims["medianModels"], dims["conferencePct"], dims["growthRate"]],
        })
    comparative = {"indicators": comparative_indicators, "series": comparative_series}

    # ── Item 4: Beyond Big Three ─────────────────────────────────────
    def build_pattern_fw_subsection(fw_pattern, scan_fn, keyword_dict):
        """Build a framework subsection by scanning ALL papers via regex pattern."""
        sub_papers = []
        year_dist = Counter()
        concept_counter = Counter()
        for fn, fields in paper_yaml.items():
            title = fields.get("short_title", "") or fn
            abstract = fields.get("abstract", "") or ""
            search_text = f"{title} {abstract}"
            if not fw_pattern.search(search_text):
                continue
            year = extract_year(fn)
            if year == 9999:
                year = 0
            kw = sorted(scan_fn(title, abstract))
            for k in kw:
                concept_counter[k] += 1
            if year > 0:
                year_dist[year] += 1
            sub_papers.append({
                "fn": fn,
                "y": year,
                "kw": kw,
            })
        return {
            "count": len(sub_papers),
            "papers": sub_papers,
            "yearDist": {str(y): c for y, c in sorted(year_dist.items()) if y >= 2016},
            "concepts": [{"n": n, "c": c} for n, c in concept_counter.most_common()],
        }

    care_data = build_pattern_fw_subsection(
        NORMATIVE_FRAMEWORK_PATTERNS["Care Ethics"], scan_care_keywords, CARE_ETHICS_KEYWORDS)
    contract_data = build_pattern_fw_subsection(
        NORMATIVE_FRAMEWORK_PATTERNS["Contractualism/Rawlsian"], scan_contractualism_keywords, CONTRACTUALISM_KEYWORDS)
    princ_data = build_pattern_fw_subsection(
        NORMATIVE_FRAMEWORK_PATTERNS["Principlism"], scan_principlism_keywords, PRINCIPLISM_KEYWORDS)

    # ── Item 5: Coverage Gap Matrix ──────────────────────────────────
    gap_fw_names = list(NORMATIVE_FRAMEWORK_PATTERNS.keys())
    gap_cols = ["Has Benchmark", "Has Model Eval", "Has Non-WEIRD", "Has Multilingual", "Paper Count"]

    # Build paper sets per framework
    fw_paper_sets = {}
    for fw_name, fw_pat in NORMATIVE_FRAMEWORK_PATTERNS.items():
        fns = set()
        for fn, fields in paper_yaml.items():
            title = fields.get("short_title", "") or fn
            abstract = fields.get("abstract", "") or ""
            search_text = f"{title} {abstract}"
            if fw_pat.search(search_text):
                fns.add(fn)
        fw_paper_sets[fw_name] = fns

    gap_matrix = []
    for fw_name in gap_fw_names:
        fns = fw_paper_sets[fw_name]
        has_bench = 1 if any(fn in candidates_set for fn in fns) else 0
        has_model = 1 if any(paper_yaml.get(fn, {}).get("LLM_assessed", "").lower() not in ("", "na", "n/a", "none") for fn in fns) else 0
        has_non_weird = 0
        has_multilingual = 0
        for fn in fns:
            cultures = paper_yaml.get(fn, {}).get("cultures_nationalities_list", [])
            for c in (cultures if isinstance(cultures, list) else []):
                r = classify_region(c)
                if r not in ("North America", "Western Europe", "Mixed", "Unknown"):
                    has_non_weird = 1
                    break
            langs = paper_yaml.get(fn, {}).get("languages_list", [])
            if len([l for l in langs if l.lower() not in ("english", "en", "")]) > 0:
                has_multilingual = 1
            if has_non_weird and has_multilingual:
                break
        gap_matrix.append([has_bench, has_model, has_non_weird, has_multilingual, len(fns)])

    # ── Item 11: Meta-Ethics ─────────────────────────────────────────
    META_ETHICS_KEYWORDS = {
        "Moral Realism": re.compile(r'moral\s+realis[mt]|ethical\s+realis[mt]|mind[\s\-]independent\s+moral', re.I),
        "Anti-Realism": re.compile(r'anti[\s\-]?realis[mt]|moral\s+(?:anti[\s\-]?realis|error\s+theor|expressivis|non[\s\-]?cognitivis)', re.I),
        "Relativism": re.compile(r'moral\s+relativis[mt]|ethical\s+relativis[mt]|cultural\s+relativis', re.I),
        "Universalism": re.compile(r'moral\s+universalis[mt]|ethical\s+universalis[mt]|universal\s+(?:moral|ethic)', re.I),
        "Reflective Equilibrium": re.compile(r'reflective\s+equilibrium', re.I),
    }
    meta_ethics_counter = Counter()
    for fn, fields in paper_yaml.items():
        abstract = fields.get("abstract", "") or ""
        title = fields.get("short_title", "") or fn
        text = f"{title} {abstract}"
        for concept, pat in META_ETHICS_KEYWORDS.items():
            if pat.search(text):
                meta_ethics_counter[concept] += 1
    meta_ethics = [{"n": n, "c": c} for n, c in meta_ethics_counter.most_common()]

    # ── Item 12: Author-Framework Bipartite ──────────────────────────
    author_fw_counter = defaultdict(lambda: {"total": 0, "ve": 0, "de": 0, "cu": 0})
    for fn in ve_fns:
        fields = paper_yaml.get(fn, {})
        fa = fields.get("first_author", "")
        if fa:
            author_fw_counter[fa]["total"] += 1
            author_fw_counter[fa]["ve"] += 1
    for fn in de_fns:
        fields = paper_yaml.get(fn, {})
        fa = fields.get("first_author", "")
        if fa:
            author_fw_counter[fa]["total"] += 1
            author_fw_counter[fa]["de"] += 1
    for fn in cu_fns:
        fields = paper_yaml.get(fn, {})
        fa = fields.get("first_author", "")
        if fa:
            author_fw_counter[fa]["total"] += 1
            author_fw_counter[fa]["cu"] += 1
    # Top 30 authors with >=2 normative papers
    author_fw_list = sorted(
        [{"n": name, "c": d["total"], "ve": d["ve"], "de": d["de"], "cu": d["cu"]}
         for name, d in author_fw_counter.items() if d["total"] >= 2],
        key=lambda x: -x["c"]
    )[:30]

    # ── Item 13: Full-Text Depth ─────────────────────────────────────
    EXTRACT_DIR = WS_ROOT / "PDF Extracts"
    all_normative_fns = ve_fns | de_fns | cu_fns
    full_text_depth = []
    for fn in sorted(all_normative_fns):
        year_str = fn[:4] if fn[:4].isdigit() else "0000"
        extract_path = EXTRACT_DIR / year_str / fn
        if not extract_path.exists():
            continue
        try:
            text = extract_path.read_text(encoding='utf-8')
        except Exception:
            continue
        # Word count
        words = text.split()
        word_count = len(words)
        if word_count < 100:
            continue
        # Count normative keywords
        text_lower = text.lower()
        kw_count = 0
        all_kw_dicts = [VIRTUE_KEYWORDS, DEONTOLOGY_KEYWORDS, CU_CONCEPT_KEYWORDS]
        for kw_dict in all_kw_dicts:
            for concept, patterns in kw_dict.items():
                for p in patterns:
                    kw_count += text_lower.count(p)
        density = round(1000 * kw_count / word_count, 2)
        full_text_depth.append({"fn": fn, "density": density})

    full_text_depth.sort(key=lambda x: -x["density"])
    full_text_depth = full_text_depth[:20]  # Top 20

    # Add full-text depth per framework
    for fw_key, fw_fns_set, fw_data_ref in [("ve", ve_fns, ve_data), ("de", de_fns, de_data), ("cu", cu_fns, cu_data)]:
        fw_depth = [d for d in full_text_depth if d["fn"] in fw_fns_set]
        fw_data_ref["fullTextDepth"] = fw_depth[:10]

    # ── Item 14: Philosopher Citation Network ────────────────────────
    PHILOSOPHER_PATTERNS = {
        "Aristotle": re.compile(r'\baristot', re.I),
        "Kant": re.compile(r'\bkant(?:ian)?\b', re.I),
        "Mill": re.compile(r'\bmill\b.*utilitar|utilitar.*\bmill\b|\bjohn\s+stuart\s+mill', re.I),
        "Rawls": re.compile(r'\brawls', re.I),
        "Confucius": re.compile(r'\bconfuci', re.I),
        "Bentham": re.compile(r'\bbentham', re.I),
        "Hume": re.compile(r'\bhume\b', re.I),
        "Habermas": re.compile(r'\bhabermas', re.I),
        "Nussbaum": re.compile(r'\bnussbaum', re.I),
        "Sen": re.compile(r'\bamartya\s+sen\b|\bsen\b.*capabilit', re.I),
        "Gilligan": re.compile(r'\bgilligan', re.I),
        "Noddings": re.compile(r'\bnoddings', re.I),
    }

    citation_counter = Counter()
    citation_fws = defaultdict(Counter)  # philosopher -> {VE: n, DE: n, CU: n}
    for fn, fields in paper_yaml.items():
        abstract = fields.get("abstract", "") or ""
        title = fields.get("short_title", "") or fn
        text = f"{title} {abstract}"
        for philosopher, pat in PHILOSOPHER_PATTERNS.items():
            if pat.search(text):
                citation_counter[philosopher] += 1
                if fn in ve_fns:
                    citation_fws[philosopher]["VE"] += 1
                if fn in de_fns:
                    citation_fws[philosopher]["DE"] += 1
                if fn in cu_fns:
                    citation_fws[philosopher]["CU"] += 1

    citations = [{"n": name, "c": count, "fws": dict(citation_fws.get(name, {}))}
                 for name, count in citation_counter.most_common()]

    return {
        "yes": len(yes_entries),
        "borderline": len(border_entries),
        "excluded": excluded_count,
        "frameworks": frameworks,
        "papers": normative_papers,
        "ve": ve_data,
        "de": de_data,
        "cu": cu_data,
        "overlap": overlap,
        "timelineFw": timeline_fw,
        "metaEthics": meta_ethics,
        "authorFramework": author_fw_list,
        "citations": citations,
        # NEW: Items 3, 4, 5
        "comparative": comparative,
        "care": care_data,
        "contract": contract_data,
        "princ": princ_data,
        "gapRows": gap_fw_names,
        "gapCols": gap_cols,
        "gapMatrix": gap_matrix,
    }


def compute_moral_psych_data(paper_yaml, candidates, candidates_set):
    """Compute moral psychology data — v7c overhaul with 13 new analytics."""
    cand_lookup = {e["filename"]: e for e in candidates}

    mp_papers = []
    paper_theories = {}
    theory_counter = Counter()
    theory_year = defaultdict(Counter)
    theory_paper_sets = defaultdict(set)
    benchmark_count = 0

    # v7c: cross-cutting per-paper accumulators
    alignment_counter = Counter()
    methodology_counter = Counter()
    instrument_counter = Counter()
    weird_counter = Counter()
    sophistication_year = defaultdict(list)

    for fn, fields in paper_yaml.items():
        mp_val = fields.get('moral_psychology', '') or ''
        abstract = fields.get('abstract', '') or ''
        combined_text = f"{mp_val} {abstract}"

        if mp_val.lower() in ('n/a', 'na', 'no', 'none', '', 'false'):
            continue

        theories = classify_theories(combined_text)
        if not theories:
            theories = classify_theories(mp_val)

        year = extract_year(fn)
        is_bench = fn in candidates_set
        if is_bench:
            benchmark_count += 1

        cand = cand_lookup.get(fn, {})
        combined_model_text = get_models_text(cand, fields)

        # v7c: per-paper alignment outcomes
        paper_alignment = []
        for al_name, al_pat in ALIGNMENT_OUTCOME_PATTERNS.items():
            if al_pat.search(combined_text):
                paper_alignment.append(al_name)
                alignment_counter[al_name] += 1

        # v7c: per-paper methodology tags
        paper_methods = []
        for mt_name, mt_pat in METHODOLOGY_PATTERNS.items():
            if mt_pat.search(combined_text):
                paper_methods.append(mt_name)
                methodology_counter[mt_name] += 1

        # v7c: per-paper instruments
        paper_instruments = []
        for ins_name, ins_pat in INSTRUMENT_PATTERNS.items():
            if ins_pat.search(combined_text):
                paper_instruments.append(ins_name)
                instrument_counter[ins_name] += 1

        # v7c: WEIRD status from region
        cultures = fields.get("cultures_nationalities_list", [])
        paper_regions = set()
        for c in (cultures if isinstance(cultures, list) else []):
            paper_regions.add(classify_region(c))
        paper_weird_statuses = set(classify_weird(r) for r in paper_regions if r != "Other")
        if len(paper_weird_statuses) > 1 or "Mixed" in paper_weird_statuses:
            paper_weird = "Mixed"
        elif paper_weird_statuses:
            paper_weird = next(iter(paper_weird_statuses))
        else:
            paper_weird = "Unknown"
        if paper_weird != "Unknown":
            weird_counter[paper_weird] += 1

        # v7c: sophistication = number of theories per paper
        if year != 9999:
            sophistication_year[year].append(len(theories))

        mp_papers.append({
            "fn": fn,
            "y": year if year != 9999 else 0,
            "th": theories,
            "ib": 1 if is_bench else 0,
            "bn": get_benchmark_name(cand, fields),
            "wm": get_what_measures(cand, fields),
            "lm": extract_model_families(combined_model_text)[:5],
            "al": paper_alignment[:2],
            "mt": paper_methods[:2],
            "ins": paper_instruments[:2],
        })

        paper_theories[fn] = theories
        for t in theories:
            theory_counter[t] += 1
            theory_paper_sets[t].add(fn)
            if year != 9999:
                theory_year[t][year] += 1

    # Theory distribution
    theory_dist = []
    for meta in THEORY_META:
        abbrev = meta["abbrev"]
        theory_dist.append({
            "n": meta["name"],
            "a": abbrev,
            "c": theory_counter.get(abbrev, 0),
            "col": meta["color"],
        })

    # ── Helper: build theory sub-section ─────────────────────────────────
    def _build_subsection(theory_key):
        """Build standard sub-section data for a single theory key."""
        sub_fns = theory_paper_sets.get(theory_key, set())
        sub_papers = []
        sub_year = Counter()
        sub_model = Counter()
        sub_theory_vs_emp = Counter()
        sub_venue = Counter()
        sub_region = Counter()
        for fn in sub_fns:
            fields = paper_yaml.get(fn, {})
            cand = cand_lookup.get(fn, {})
            cmt = get_models_text(cand, fields)
            yr = extract_year(fn)
            if yr != 9999:
                sub_year[yr] += 1
            for m in extract_model_families(cmt):
                sub_model[m] += 1
            if fn in candidates_set:
                sub_theory_vs_emp["Benchmark / Evaluation"] += 1
            else:
                sub_theory_vs_emp["Theoretical / Framework"] += 1
            cc = fields.get("CONF-CC", "") or "N/A"
            vt = categorize_venue(cc)
            sub_venue[vt] += 1
            cultures_list = fields.get("cultures_nationalities_list", [])
            pr = set()
            for c in (cultures_list if isinstance(cultures_list, list) else []):
                r = classify_region(c)
                sub_region[r] += 1
                pr.add(r)
            sub_papers.append({
                "fn": fn,
                "y": yr if yr != 9999 else 0,
                "ib": 1 if fn in candidates_set else 0,
                "bn": get_benchmark_name(cand, fields),
                "wm": get_what_measures(cand, fields),
                "lm": extract_model_families(cmt)[:5],
                "vt": vt,
                "rg": sorted(pr),
            })
        return {
            "papers": sub_papers,
            "count": len(sub_papers),
            "yearDist": {str(y): c for y, c in sorted(sub_year.items()) if y >= 2016},
            "topModels": [{"n": n, "c": c} for n, c in sub_model.most_common(10)],
            "theoryVsEmpirical": [{"n": n, "c": c} for n, c in sub_theory_vs_emp.most_common()],
            "venueTypeDist": [{"n": n, "c": c} for n, c in sub_venue.most_common()],
            "regionDist": [{"n": n, "c": c} for n, c in sub_region.most_common()],
        }

    # ── MFT sub-section ──────────────────────────────────────────────────
    mft_data = _build_subsection("MFT")
    # Add MFT-specific: foundations + approach distribution
    mft_fns = theory_paper_sets.get("MFT", set())
    mft_foundation_counts = Counter()
    mft_approach_counter = Counter()
    for fn in mft_fns:
        fields = paper_yaml.get(fn, {})
        abstract = fields.get('abstract', '') or ''
        mp_val = fields.get('moral_psychology', '') or ''
        combined = f"{mp_val} {abstract}"
        for fnd_name, fnd_pat in MFT_FOUNDATION_PATTERNS.items():
            if fnd_pat.search(combined):
                mft_foundation_counts[fnd_name] += 1
        for ap_name, ap_pat in MFT_APPROACH_PATTERNS.items():
            if ap_pat.search(combined):
                mft_approach_counter[ap_name] += 1
    mft_data["foundations"] = [{"n": f, "c": mft_foundation_counts.get(f, 0)} for f in MFT_FOUNDATIONS]
    mft_data["approachDist"] = [{"n": n, "c": c} for n, c in mft_approach_counter.most_common()]

    # ── Schwartz sub-section ─────────────────────────────────────────────
    schwartz_data = _build_subsection("Schwartz")
    # Add Schwartz-specific: value dims + higher-order quadrants
    schwartz_fns = theory_paper_sets.get("Schwartz", set())
    schwartz_value_counts = Counter()
    for fn in schwartz_fns:
        fields = paper_yaml.get(fn, {})
        abstract = fields.get('abstract', '') or ''
        mp_val = fields.get('moral_psychology', '') or ''
        combined = f"{mp_val} {abstract}"
        for val_name, val_pat in SCHWARTZ_VALUE_PATTERNS.items():
            if val_pat.search(combined):
                schwartz_value_counts[val_name] += 1
    schwartz_data["valueDims"] = [{"n": v, "c": schwartz_value_counts.get(v, 0)} for v in SCHWARTZ_VALUES]
    # Higher-order quadrants: count papers with >=1 constituent value
    ho_counts = {}
    for quadrant, values in SCHWARTZ_HIGHER_ORDER.items():
        papers_in_quad = set()
        for fn in schwartz_fns:
            fields = paper_yaml.get(fn, {})
            abstract = fields.get('abstract', '') or ''
            mp_val = fields.get('moral_psychology', '') or ''
            combined = f"{mp_val} {abstract}"
            for v in values:
                if SCHWARTZ_VALUE_PATTERNS[v].search(combined):
                    papers_in_quad.add(fn)
                    break
        ho_counts[quadrant] = len(papers_in_quad)
    schwartz_data["higherOrder"] = [{"n": q, "c": ho_counts.get(q, 0)} for q in SCHWARTZ_HIGHER_ORDER]

    # ── v7c: Reasoning (Kohlberg) sub-section ────────────────────────────
    reasoning_data = _build_subsection("Kohlberg")

    # ── v7c: Dilemmas (Trolley) sub-section ──────────────────────────────
    dilemmas_data = _build_subsection("Trolley")
    # Add paradigm breakdown for dilemmas
    trolley_fns = theory_paper_sets.get("Trolley", set())
    paradigm_counter = Counter()
    PARADIGM_PATTERNS = {
        "Classic Trolley": re.compile(r'trolley\s+problem|classic\s+trolley|trolley\s+dilemma', re.I),
        "Moral Machine": re.compile(r'moral\s+machine|autonomous\s+vehicle|self[\s\-]?driving', re.I),
        "Medical Triage": re.compile(r'medical\s+triage|hospital|organ\s+transplant|doctor', re.I),
        "AI Safety": re.compile(r'AI\s+safety|machine\s+ethics|robot\s+ethics|artificial\s+moral', re.I),
        "Custom Vignettes": re.compile(r'vignette|custom\s+scenario|novel\s+dilemma|modified\s+dilemma', re.I),
    }
    for fn in trolley_fns:
        fields = paper_yaml.get(fn, {})
        abstract = fields.get('abstract', '') or ''
        mp_val = fields.get('moral_psychology', '') or ''
        combined = f"{mp_val} {abstract}"
        matched_any = False
        for pg_name, pg_pat in PARADIGM_PATTERNS.items():
            if pg_pat.search(combined):
                paradigm_counter[pg_name] += 1
                matched_any = True
        if not matched_any:
            paradigm_counter["Other Dilemma"] += 1
    dilemmas_data["paradigmDist"] = [{"n": n, "c": c} for n, c in paradigm_counter.most_common()]

    # ── v7c: Dominance Shift (proportional % timeline) ───────────────────
    theory_meta_lookup = {m["abbrev"]: m["name"] for m in THEORY_META}
    all_years = sorted(set(y for tc in theory_year.values() for y in tc.keys() if y >= 2016))
    dominance_raw = {}
    for t in ACTIVE_THEORIES:
        dominance_raw[t] = [theory_year.get(t, Counter()).get(y, 0) for y in all_years]
    dominance_pct = {"years": all_years}
    for t in ACTIVE_THEORIES:
        dominance_pct[t] = []
    for yi, y in enumerate(all_years):
        total = sum(dominance_raw[t][yi] for t in ACTIVE_THEORIES)
        for t in ACTIVE_THEORIES:
            dominance_pct[t].append(round(100 * dominance_raw[t][yi] / max(total, 1), 1))

    # ── v7c: WEIRD Split cross-tab (theory × WEIRD status) ──────────────
    weird_split = {"theories": [], "WEIRD": [], "Non-WEIRD": [], "Mixed": []}
    for t in ACTIVE_THEORIES:
        wc = Counter()
        for fn in theory_paper_sets.get(t, set()):
            cultures = paper_yaml.get(fn, {}).get("cultures_nationalities_list", [])
            pr = set()
            for c in (cultures if isinstance(cultures, list) else []):
                pr.add(classify_region(c))
            weird_statuses = set(classify_weird(r) for r in pr if r != "Other")
            if len(weird_statuses) > 1 or "Mixed" in weird_statuses:
                wc["Mixed"] += 1
            elif weird_statuses:
                wc[next(iter(weird_statuses))] += 1
            else:
                wc["Unknown"] += 1
        weird_split["theories"].append(theory_meta_lookup.get(t, t))
        weird_split["WEIRD"].append(wc.get("WEIRD", 0))
        weird_split["Non-WEIRD"].append(wc.get("Non-WEIRD", 0))
        weird_split["Mixed"].append(wc.get("Mixed", 0))

    # ── v7c: Model × Theory heatmap ─────────────────────────────────────
    model_theory_counter = defaultdict(Counter)
    for t in ACTIVE_THEORIES:
        for fn in theory_paper_sets.get(t, set()):
            fields = paper_yaml.get(fn, {})
            cand = cand_lookup.get(fn, {})
            cmt = get_models_text(cand, fields)
            for m in extract_model_families(cmt):
                model_theory_counter[m][t] += 1
    model_totals = {m: sum(tc.values()) for m, tc in model_theory_counter.items()}
    top_models = sorted(model_totals, key=model_totals.get, reverse=True)[:10]
    model_theory_heatmap = {
        "models": top_models,
        "theories": [theory_meta_lookup.get(t, t) for t in ACTIVE_THEORIES],
        "matrix": [[model_theory_counter[m].get(t, 0) for t in ACTIVE_THEORIES] for m in top_models],
    }

    # ── v7c: Normative Bridge (moral psych theory × VE/DE/CU) ───────────
    fw_labels = ["Virtue Ethics", "Deontological", "Utilitarian"]
    fw_fields = {"Virtue Ethics": "virtue_ethics", "Deontological": "deontological_ethics",
                 "Utilitarian": "utilitarian_ethics"}
    normative_bridge_matrix = []
    for t in ACTIVE_THEORIES:
        row = []
        for fw_name in fw_labels:
            field_key = fw_fields[fw_name]
            count = 0
            for fn in theory_paper_sets.get(t, set()):
                val = paper_yaml.get(fn, {}).get(field_key, "").lower()
                if val in ("yes", "partial", "true"):
                    count += 1
            row.append(count)
        normative_bridge_matrix.append(row)
    normative_bridge = {
        "theories": [theory_meta_lookup.get(t, t) for t in ACTIVE_THEORIES],
        "frameworks": fw_labels,
        "matrix": normative_bridge_matrix,
    }

    # ── v7c: Sophistication timeline ─────────────────────────────────────
    sophistication = {
        "years": sorted(y for y in sophistication_year if y >= 2016),
        "avgTheories": [],
        "paperCounts": [],
    }
    for y in sophistication["years"]:
        scores = sophistication_year[y]
        sophistication["avgTheories"].append(round(sum(scores) / max(len(scores), 1), 2))
        sophistication["paperCounts"].append(len(scores))

    # ── Timeline (updated: reasoning + dilemmas instead of dev) ──────────
    timeline = {
        "years": all_years,
        "mft": [theory_year.get("MFT", Counter()).get(y, 0) for y in all_years],
        "schwartz": [theory_year.get("Schwartz", Counter()).get(y, 0) for y in all_years],
        "reasoning": [theory_year.get("Kohlberg", Counter()).get(y, 0) for y in all_years],
        "dilemmas": [theory_year.get("Trolley", Counter()).get(y, 0) for y in all_years],
    }

    # ── Cooccurrence (filtered to 5 active theories) ────────────────────
    n_active = len(ACTIVE_THEORIES)
    cooccurrence = [[0] * n_active for _ in range(n_active)]
    for fn, theories in paper_theories.items():
        indices = [ACTIVE_THEORIES.index(t) for t in theories if t in ACTIVE_THEORIES]
        for ii in range(len(indices)):
            for jj in range(ii + 1, len(indices)):
                cooccurrence[indices[ii]][indices[jj]] += 1
                cooccurrence[indices[jj]][indices[ii]] += 1

    return {
        "papers": mp_papers,
        "paperCount": len(mp_papers),
        "theoryDist": theory_dist,
        "timeline": timeline,
        "benchmarkCount": benchmark_count,
        "mft": mft_data,
        "schwartz": schwartz_data,
        "reasoning": reasoning_data,
        "dilemmas": dilemmas_data,
        "cooccurrence": cooccurrence,
        "coLabels": [theory_meta_lookup.get(t, t) for t in ACTIVE_THEORIES],
        # v7c new keys
        "dominanceShift": dominance_pct,
        "weirdSplit": weird_split,
        "modelTheory": model_theory_heatmap,
        "alignment": [{"n": n, "c": c} for n, c in alignment_counter.most_common()],
        "methodology": [{"n": n, "c": c} for n, c in methodology_counter.most_common()],
        "instruments": [{"n": n, "c": c} for n, c in instrument_counter.most_common()],
        "normativeBridge": normative_bridge,
        "sophistication": sophistication,
    }


# ── Religious Tradition Extended Analysis Builders ───────────────────────


def build_islamic_extended(sub_fns, paper_yaml, cand_lookup, candidates_set):
    """Build extended Islamic tradition analysis data for dashboard charts."""

    # ── domainDist — treemap ──────────────────────────────────────────────
    domain_fns = defaultdict(list)
    for fn in sub_fns:
        fields = paper_yaml.get(fn, {})
        text = (fields.get("short_title", "") or "") + " " + (fields.get("abstract", "") or "")
        matched = False
        for domain_name, pat in ISLAMIC_DOMAIN_PATTERNS.items():
            if pat.search(text):
                domain_fns[domain_name].append(fn)
                matched = True
        if not matched:
            domain_fns["General"].append(fn)
    domain_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                   for n, flist in sorted(domain_fns.items(), key=lambda x: -len(x[1]))]

    # ── langGeo — grouped bar ────────────────────────────────────────────
    LANG_REGION_MAP = {
        "Arabic": "Middle East", "Persian": "Iran/Shia", "Farsi": "Iran/Shia",
        "Indonesian": "Southeast Asia", "Malay": "Southeast Asia",
        "Bengali": "South Asia", "Urdu": "South Asia",
        "English": "Global/Western", "Turkish": "Turkey",
    }
    lang_fns = defaultdict(list)
    for fn in sub_fns:
        for lang in paper_yaml.get(fn, {}).get("languages_list", []):
            if lang:
                lang_fns[lang].append(fn)
    lang_geo = []
    for lang, flist in sorted(lang_fns.items(), key=lambda x: -len(x[1]))[:10]:
        region = "Other"
        for key, reg in LANG_REGION_MAP.items():
            if key.lower() in lang.lower():
                region = reg
                break
        lang_geo.append({"lang": lang, "c": len(flist), "region": region, "fns": sorted(set(flist))})

    # ── streamTimeline — stacked area ────────────────────────────────────
    RESOURCE_KW = re.compile(
        r"\bdataset\b|\bcorpus\b|\bbenchmark\b|\bquestion\s+answer|\bQA\b"
        r"|\bclassification\b|\bannotation\b|\bdetect\b", re.I)
    BIAS_KW = re.compile(
        r"\bbias\b|\bislamophob|\bstereotyp|\bdiscriminat|\bprejudic"
        r"|\banti.muslim\b|\bhate\b", re.I)
    year_resource, year_bias = Counter(), Counter()
    resource_fns_all, bias_fns_all = [], []
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        year = extract_year(fn)
        if year == 9999:
            continue
        if RESOURCE_KW.search(abstract):
            year_resource[year] += 1
            resource_fns_all.append(fn)
        if BIAS_KW.search(abstract):
            year_bias[year] += 1
            bias_fns_all.append(fn)
    all_yrs = sorted(y for y in set(list(year_resource) + list(year_bias)) if y >= 2016)
    stream_timeline = {
        "years": all_yrs,
        "resource": [year_resource.get(y, 0) for y in all_yrs],
        "bias": [year_bias.get(y, 0) for y in all_yrs],
    }

    # ── sourceCoverage — radar ───────────────────────────────────────────
    source_counter = Counter()
    source_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for src, pat in ISLAMIC_SOURCE_PATTERNS.items():
            if pat.search(abstract):
                source_counter[src] += 1
                source_fns_map[src].append(fn)
    source_coverage = [{"axis": s, "val": source_counter.get(s, 0)}
                       for s in ISLAMIC_SOURCE_PATTERNS]

    # ── coTraditions — sankey ────────────────────────────────────────────
    co_fns = defaultdict(list)
    for fn in sub_fns:
        fields = paper_yaml.get(fn, {})
        trads = classify_relig_traditions(
            fields.get("religious_values_list", []),
            fields.get("religious_values", "") or "")
        for t in trads:
            if t != "Islam":
                co_fns[t].append(fn)
    co_traditions = sorted(
        [{"source": "Islam", "target": t, "value": len(flist), "fns": sorted(set(flist))}
         for t, flist in co_fns.items() if len(flist) > 0],
        key=lambda x: -x["value"])

    return {
        "domainDist": domain_dist, "langGeo": lang_geo,
        "streamTimeline": stream_timeline, "sourceCoverage": source_coverage,
        "coTraditions": co_traditions,
        "streamTimelineFns": {"Resource": sorted(set(resource_fns_all)), "Bias": sorted(set(bias_fns_all))},
        "sourceCoverageFns": {s: sorted(set(source_fns_map.get(s, []))) for s in ISLAMIC_SOURCE_PATTERNS},
    }


def build_christianity_extended(sub_fns, paper_yaml, cand_lookup, candidates_set):
    """Build extended Christianity tradition analysis data."""

    BIAS_PAT = re.compile(r"\bbias\b|\bstereotyp|\bprejudic|\bdiscriminat|\bhate\b", re.I)
    THEOL_PAT = re.compile(r"\bethic|\bmoral|\btheolog|\bvirtue|\bnatural\s+law|\bdeontolog", re.I)
    SCRIPT_PAT = re.compile(r"\bcorpus\b|\bdataset\b|\bQA\b|\bquestion\s+answer|\btranslation\b|\bNLP\b|\btext\s+mining", re.I)

    # ── denomDist — donut (Catholic/Protestant/Orthodox/Evangelical) ────
    denom_fns_map = defaultdict(list)
    unclassified = []
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        matched = False
        for denom, pat in CHRISTIANITY_DENOM_PATTERNS.items():
            if pat.search(abstract):
                denom_fns_map[denom].append(fn)
                matched = True
        if not matched:
            unclassified.append(fn)
    if unclassified:
        denom_fns_map["General/Unspecified"] = unclassified
    denom_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                  for n, flist in sorted(denom_fns_map.items(), key=lambda x: -len(x[1]))]

    # ── conceptRadar — radar (6 theological concepts) ────────────────────
    concept_ctr = Counter()
    concept_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in CHRISTIANITY_CONCEPT_PATTERNS.items():
            if pat.search(abstract):
                concept_ctr[name] += 1
                concept_fns_map[name].append(fn)
    concept_radar = [{"axis": n, "val": concept_ctr.get(n, 0)}
                     for n in CHRISTIANITY_CONCEPT_PATTERNS]

    # ── textCoverage — radar (OT/NT/Patristic) ──────────────────────────
    text_ctr = Counter()
    text_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in CHRISTIANITY_TEXT_PATTERNS.items():
            if pat.search(abstract):
                text_ctr[name] += 1
                text_fns_map[name].append(fn)
    text_coverage = [{"axis": n, "val": text_ctr.get(n, 0)}
                     for n in CHRISTIANITY_TEXT_PATTERNS]

    # ── focusDist — donut (research focus) ───────────────────────────────
    focus_fns = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        if SCRIPT_PAT.search(abstract):
            focus_fns["Scriptural NLP"].append(fn)
        elif BIAS_PAT.search(abstract):
            focus_fns["Bias Detection"].append(fn)
        elif THEOL_PAT.search(abstract):
            focus_fns["Theological Framework"].append(fn)
        else:
            focus_fns["Other"].append(fn)
    focus_dist = [{"n": n, "c": len(flist), "fns": sorted(flist)}
                  for n, flist in sorted(focus_fns.items(), key=lambda x: -len(x[1]))]

    # ── normativeCross — grouped bar (Virtue/Deontological/Utilitarian) ──
    FW_FIELDS = {"Virtue Ethics": "virtue_ethics", "Deontological": "deontological_ethics",
                 "Utilitarian": "utilitarian_ethics"}
    normative_cross = []
    normative_cross_fns = {}
    for fw_label, yaml_f in FW_FIELDS.items():
        matched_fns = [fn for fn in sub_fns
                       if paper_yaml.get(fn, {}).get(yaml_f, "").lower() in ("yes", "partial", "true")]
        normative_cross.append({"framework": fw_label, "count": len(matched_fns)})
        normative_cross_fns[fw_label] = sorted(set(matched_fns))

    # ── coTraditions — bar (co-occurrence with other traditions) ─────────
    co_fns = defaultdict(list)
    for fn in sub_fns:
        f = paper_yaml.get(fn, {})
        trads = set(classify_relig_traditions(
            f.get("religious_values_list", []), f.get("religious_values", "") or ""))
        for t in trads:
            if t != "Christianity":
                co_fns[t].append(fn)
    co_traditions = sorted(
        [{"n": t, "c": len(flist), "fns": sorted(set(flist))}
         for t, flist in co_fns.items() if len(flist) > 0],
        key=lambda x: -x["c"])

    return {
        "denomDist": denom_dist, "conceptRadar": concept_radar,
        "textCoverage": text_coverage, "focusDist": focus_dist,
        "normativeCross": normative_cross, "coTraditions": co_traditions,
        "conceptRadarFns": {n: sorted(set(concept_fns_map.get(n, []))) for n in CHRISTIANITY_CONCEPT_PATTERNS},
        "textCoverageFns": {n: sorted(set(text_fns_map.get(n, []))) for n in CHRISTIANITY_TEXT_PATTERNS},
        "normativeCrossFns": normative_cross_fns,
    }


def build_judaism_extended(sub_fns, paper_yaml, cand_lookup, candidates_set):
    """Build extended Judaism tradition analysis data."""

    BIAS_PAT = re.compile(r"\bbias\b|\bstereotyp|\bantisemit|\banti.semit|\bhate\b", re.I)
    HALAKH_PAT = re.compile(r"halakh|jewish\s+law|talmudic\s+reason", re.I)
    HEBREW_NLP_PAT = re.compile(r"hebrew.*nlp|nlp.*hebrew|hebrew.*corpus|corpus.*hebrew|hebrew.*process", re.I)

    # ── conceptRadar — radar (6 Jewish concepts) ────────────────────────
    concept_ctr = Counter()
    concept_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in JUDAISM_CONCEPT_PATTERNS.items():
            if pat.search(abstract):
                concept_ctr[name] += 1
                concept_fns_map[name].append(fn)
    concept_radar = [{"axis": n, "val": concept_ctr.get(n, 0)}
                     for n in JUDAISM_CONCEPT_PATTERNS]

    # ── textSources — radar (Torah/Talmud/Mishnah/Midrash/Responsa) ────
    text_ctr = Counter()
    text_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in JUDAISM_TEXT_PATTERNS.items():
            if pat.search(abstract):
                text_ctr[name] += 1
                text_fns_map[name].append(fn)
    text_sources = [{"axis": n, "val": text_ctr.get(n, 0)}
                    for n in JUDAISM_TEXT_PATTERNS]

    # ── focusDist — donut ────────────────────────────────────────────────
    focus_fns = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        if BIAS_PAT.search(abstract):
            focus_fns["Antisemitism Detection"].append(fn)
        elif HALAKH_PAT.search(abstract):
            focus_fns["Halakhic Reasoning"].append(fn)
        elif HEBREW_NLP_PAT.search(abstract):
            focus_fns["Hebrew NLP"].append(fn)
        else:
            focus_fns["Other"].append(fn)
    focus_dist = [{"n": n, "c": len(flist), "fns": sorted(flist)}
                  for n, flist in sorted(focus_fns.items(), key=lambda x: -len(x[1]))]

    # ── normativeCross — grouped bar ─────────────────────────────────────
    FW_FIELDS = {"Virtue Ethics": "virtue_ethics", "Deontological": "deontological_ethics",
                 "Utilitarian": "utilitarian_ethics"}
    normative_cross = []
    normative_cross_fns = {}
    for fw_label, yaml_f in FW_FIELDS.items():
        matched_fns = [fn for fn in sub_fns
                       if paper_yaml.get(fn, {}).get(yaml_f, "").lower() in ("yes", "partial", "true")]
        normative_cross.append({"framework": fw_label, "count": len(matched_fns)})
        normative_cross_fns[fw_label] = sorted(set(matched_fns))

    # ── coTraditions — bar ───────────────────────────────────────────────
    co_fns = defaultdict(list)
    for fn in sub_fns:
        f = paper_yaml.get(fn, {})
        trads = set(classify_relig_traditions(
            f.get("religious_values_list", []), f.get("religious_values", "") or ""))
        for t in trads:
            if t != "Judaism":
                co_fns[t].append(fn)
    co_traditions = sorted(
        [{"n": t, "c": len(flist), "fns": sorted(set(flist))}
         for t, flist in co_fns.items() if len(flist) > 0],
        key=lambda x: -x["c"])

    return {
        "conceptRadar": concept_radar, "textSources": text_sources,
        "focusDist": focus_dist, "normativeCross": normative_cross,
        "coTraditions": co_traditions,
        "conceptRadarFns": {n: sorted(set(concept_fns_map.get(n, []))) for n in JUDAISM_CONCEPT_PATTERNS},
        "textSourcesFns": {n: sorted(set(text_fns_map.get(n, []))) for n in JUDAISM_TEXT_PATTERNS},
        "normativeCrossFns": normative_cross_fns,
    }


def build_buddhism_extended(sub_fns, paper_yaml, cand_lookup, candidates_set):
    """Build extended Buddhism tradition analysis data."""

    ETHICS_PAT = re.compile(r"\bethic|\bmoral|\bvalue|\bvirtue|\bharm\b", re.I)
    BIAS_PAT = re.compile(r"\bbias\b|\bfair|\bstereotyp|\bdiscriminat", re.I)
    NLP_PAT = re.compile(r"\bcorpus\b|\bdataset\b|\bNLP\b|\btranslat|\blanguage\s+model|\btext\s+process", re.I)
    PHILO_PAT = re.compile(r"\bphilosoph|\btheor|\bframework|\bconceptual|\bontolog", re.I)

    # ── schoolDist — donut (Theravada/Mahayana/Vajrayana/Zen/Secular) ──
    school_fns_map = defaultdict(list)
    unclassified = []
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        matched = False
        for school, pat in BUDDHISM_SCHOOL_PATTERNS.items():
            if pat.search(abstract):
                school_fns_map[school].append(fn)
                matched = True
        if not matched:
            unclassified.append(fn)
    if unclassified:
        school_fns_map["General/Unspecified"] = unclassified
    school_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                   for n, flist in sorted(school_fns_map.items(), key=lambda x: -len(x[1]))]

    # ── conceptRadar — radar (9 Buddhist concepts) ──────────────────────
    concept_ctr = Counter()
    concept_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in BUDDHISM_CONCEPT_PATTERNS.items():
            if pat.search(abstract):
                concept_ctr[name] += 1
                concept_fns_map[name].append(fn)
    concept_radar = [{"axis": n, "val": concept_ctr.get(n, 0)}
                     for n in BUDDHISM_CONCEPT_PATTERNS]

    # ── textSources — radar (Pali Canon/Mahayana Sutras/Tibetan) ───────
    text_ctr = Counter()
    text_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in BUDDHISM_TEXT_PATTERNS.items():
            if pat.search(abstract):
                text_ctr[name] += 1
                text_fns_map[name].append(fn)
    text_sources = [{"axis": n, "val": text_ctr.get(n, 0)}
                    for n in BUDDHISM_TEXT_PATTERNS]

    # ── researchFocus — stacked bar ──────────────────────────────────────
    FOCUS_CATS = [("Ethics/Moral", ETHICS_PAT), ("Bias & Fairness", BIAS_PAT),
                  ("NLP/Corpus", NLP_PAT), ("Philosophical", PHILO_PAT)]
    focus_ctr = Counter()
    focus_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for cat, pat in FOCUS_CATS:
            if pat.search(abstract):
                focus_ctr[cat] += 1
                focus_fns_map[cat].append(fn)
    research_focus = [{"category": cat, "count": focus_ctr.get(cat, 0)} for cat, _ in FOCUS_CATS]

    # ── cultureDist — donut ──────────────────────────────────────────────
    culture_fns = defaultdict(list)
    for fn in sub_fns:
        for c in paper_yaml.get(fn, {}).get("cultures_nationalities_list", []):
            if c:
                culture_fns[c].append(fn)
    culture_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                    for n, flist in sorted(culture_fns.items(), key=lambda x: -len(x[1]))[:10]]

    # ── languageDist — bar ───────────────────────────────────────────────
    lang_fns = defaultdict(list)
    for fn in sub_fns:
        for lang in paper_yaml.get(fn, {}).get("languages_list", []):
            if lang:
                lang_fns[lang].append(fn)
    language_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                     for n, flist in sorted(lang_fns.items(), key=lambda x: -len(x[1]))]

    # ── coTraditions — bar ───────────────────────────────────────────────
    co_fns = defaultdict(list)
    for fn in sub_fns:
        f = paper_yaml.get(fn, {})
        trads = set(classify_relig_traditions(
            f.get("religious_values_list", []), f.get("religious_values", "") or ""))
        for t in trads:
            if t != "Buddhism":
                co_fns[t].append(fn)
    co_traditions = sorted(
        [{"n": t, "c": len(flist), "fns": sorted(set(flist))}
         for t, flist in co_fns.items() if len(flist) > 0],
        key=lambda x: -x["c"])

    return {
        "schoolDist": school_dist, "conceptRadar": concept_radar,
        "textSources": text_sources, "researchFocus": research_focus,
        "cultureDist": culture_dist, "languageDist": language_dist,
        "coTraditions": co_traditions,
        "conceptRadarFns": {n: sorted(set(concept_fns_map.get(n, []))) for n in BUDDHISM_CONCEPT_PATTERNS},
        "textSourcesFns": {n: sorted(set(text_fns_map.get(n, []))) for n in BUDDHISM_TEXT_PATTERNS},
        "researchFocusFns": {cat: sorted(set(focus_fns_map.get(cat, []))) for cat, _ in FOCUS_CATS},
    }


def build_hinduism_extended(sub_fns, paper_yaml, cand_lookup, candidates_set):
    """Build extended Hinduism tradition analysis data."""

    ETHICS_PAT = re.compile(r"\bethic|\bmoral|\bvalue|\bvirtue|\bharm\b", re.I)
    BIAS_PAT = re.compile(r"\bbias\b|\bfair|\bstereotyp|\bdiscriminat", re.I)
    NLP_PAT = re.compile(r"\bcorpus\b|\bdataset\b|\bNLP\b|\btranslat|\blanguage\s+model|\btext\s+process", re.I)
    PHILO_PAT = re.compile(r"\bphilosoph|\btheor|\bframework|\bconceptual|\bontolog", re.I)

    # ── textRadar — radar (Vedas/Upanishads/Gita/Dharmashastra/Manusmriti)
    text_ctr = Counter()
    text_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in HINDUISM_TEXT_PATTERNS.items():
            if pat.search(abstract):
                text_ctr[name] += 1
                text_fns_map[name].append(fn)
    text_radar = [{"axis": n, "val": text_ctr.get(n, 0)}
                  for n in HINDUISM_TEXT_PATTERNS]

    # ── conceptRadar — radar (7 Hindu concepts) ─────────────────────────
    concept_ctr = Counter()
    concept_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in HINDUISM_CONCEPT_PATTERNS.items():
            if pat.search(abstract):
                concept_ctr[name] += 1
                concept_fns_map[name].append(fn)
    concept_radar = [{"axis": n, "val": concept_ctr.get(n, 0)}
                     for n in HINDUISM_CONCEPT_PATTERNS]

    # ── schoolDist — donut (Vedanta/Samkhya/Yoga/Nyaya/Mimamsa) ────────
    school_fns_map = defaultdict(list)
    unclassified = []
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        matched = False
        for school, pat in HINDUISM_SCHOOL_PATTERNS.items():
            if pat.search(abstract):
                school_fns_map[school].append(fn)
                matched = True
        if not matched:
            unclassified.append(fn)
    if unclassified:
        school_fns_map["General/Unspecified"] = unclassified
    school_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                   for n, flist in sorted(school_fns_map.items(), key=lambda x: -len(x[1]))]

    # ── researchFocus — stacked bar ──────────────────────────────────────
    FOCUS_CATS = [("Ethics/Moral", ETHICS_PAT), ("Bias & Fairness", BIAS_PAT),
                  ("NLP/Corpus", NLP_PAT), ("Philosophical", PHILO_PAT)]
    focus_ctr = Counter()
    focus_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for cat, pat in FOCUS_CATS:
            if pat.search(abstract):
                focus_ctr[cat] += 1
                focus_fns_map[cat].append(fn)
    research_focus = [{"category": cat, "count": focus_ctr.get(cat, 0)} for cat, _ in FOCUS_CATS]

    # ── cultureDist — donut ──────────────────────────────────────────────
    culture_fns = defaultdict(list)
    for fn in sub_fns:
        for c in paper_yaml.get(fn, {}).get("cultures_nationalities_list", []):
            if c:
                culture_fns[c].append(fn)
    culture_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                    for n, flist in sorted(culture_fns.items(), key=lambda x: -len(x[1]))[:10]]

    # ── languageDist — bar ───────────────────────────────────────────────
    lang_fns = defaultdict(list)
    for fn in sub_fns:
        for lang in paper_yaml.get(fn, {}).get("languages_list", []):
            if lang:
                lang_fns[lang].append(fn)
    language_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                     for n, flist in sorted(lang_fns.items(), key=lambda x: -len(x[1]))]

    # ── coTraditions — bar ───────────────────────────────────────────────
    co_fns = defaultdict(list)
    for fn in sub_fns:
        f = paper_yaml.get(fn, {})
        trads = set(classify_relig_traditions(
            f.get("religious_values_list", []), f.get("religious_values", "") or ""))
        for t in trads:
            if t != "Hinduism":
                co_fns[t].append(fn)
    co_traditions = sorted(
        [{"n": t, "c": len(flist), "fns": sorted(set(flist))}
         for t, flist in co_fns.items() if len(flist) > 0],
        key=lambda x: -x["c"])

    return {
        "textRadar": text_radar, "conceptRadar": concept_radar,
        "schoolDist": school_dist, "researchFocus": research_focus,
        "cultureDist": culture_dist, "languageDist": language_dist,
        "coTraditions": co_traditions,
        "textRadarFns": {n: sorted(set(text_fns_map.get(n, []))) for n in HINDUISM_TEXT_PATTERNS},
        "conceptRadarFns": {n: sorted(set(concept_fns_map.get(n, []))) for n in HINDUISM_CONCEPT_PATTERNS},
        "researchFocusFns": {cat: sorted(set(focus_fns_map.get(cat, []))) for cat, _ in FOCUS_CATS},
    }


def _build_gap_comparison(sub_fns, paper_yaml, candidates_set, vault_total, vault_benchmark_count, vault_ethics_count):
    """Reusable gap comparison vs vault average."""
    n_sub = len(sub_fns) or 1
    _pct = lambda num, den: round(num * 100 / den, 1) if den > 0 else 0.0
    sub_bench = sum(1 for fn in sub_fns if fn in candidates_set)
    sub_llm = sum(1 for fn in sub_fns
                  if (paper_yaml.get(fn, {}).get("LLM_assessed", "") or "").lower()
                  not in ("", "na", "n/a", "none"))
    sub_eth = sum(1 for fn in sub_fns
                  if paper_yaml.get(fn, {}).get("ethics_overall", "").lower() == "yes")
    sub_data = sum(1 for fn in sub_fns
                   if (paper_yaml.get(fn, {}).get("DATA_URL", "") or "").lower()
                   not in ("", "na", "n/a", "none"))
    vault_llm = sum(1 for f in paper_yaml.values()
                    if (f.get("LLM_assessed", "") or "").lower() not in ("", "na", "n/a", "none"))
    vault_data = sum(1 for f in paper_yaml.values()
                     if (f.get("DATA_URL", "") or "").lower() not in ("", "na", "n/a", "none"))
    return [
        {"metric": "% Benchmarks", "subset": _pct(sub_bench, n_sub),
         "vault": _pct(vault_benchmark_count, vault_total)},
        {"metric": "% LLM Assessed", "subset": _pct(sub_llm, n_sub),
         "vault": _pct(vault_llm, vault_total)},
        {"metric": "% Ethics=Yes", "subset": _pct(sub_eth, n_sub),
         "vault": _pct(vault_ethics_count, vault_total)},
        {"metric": "% DATA_URL", "subset": _pct(sub_data, n_sub),
         "vault": _pct(vault_data, vault_total)},
    ]


def build_shinto_extended(sub_fns, paper_yaml, cand_lookup, candidates_set,
                          vault_total, vault_benchmark_count, vault_ethics_count):
    """Build extended Shinto tradition analysis data."""

    # ── conceptRadar — radar (5 Shinto concepts) ────────────────────────
    concept_ctr = Counter()
    concept_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in SHINTO_CONCEPT_PATTERNS.items():
            if pat.search(abstract):
                concept_ctr[name] += 1
                concept_fns_map[name].append(fn)
    concept_radar = [{"axis": n, "val": concept_ctr.get(n, 0)}
                     for n in SHINTO_CONCEPT_PATTERNS]

    # ── themeDist — donut (Techno-Animism/Robot Ethics/AI Personhood/Cultural)
    theme_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in SHINTO_THEME_PATTERNS.items():
            if pat.search(abstract):
                theme_fns_map[name].append(fn)
    theme_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                  for n, flist in sorted(theme_fns_map.items(), key=lambda x: -len(x[1]))]

    # ── cultureDist — bar ────────────────────────────────────────────────
    culture_fns = defaultdict(list)
    for fn in sub_fns:
        for c in paper_yaml.get(fn, {}).get("cultures_nationalities_list", []):
            if c:
                culture_fns[c].append(fn)
    culture_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                    for n, flist in sorted(culture_fns.items(), key=lambda x: -len(x[1]))]

    # ── coTraditions — bar ───────────────────────────────────────────────
    co_fns = defaultdict(list)
    for fn in sub_fns:
        f = paper_yaml.get(fn, {})
        trads = set(classify_relig_traditions(
            f.get("religious_values_list", []), f.get("religious_values", "") or ""))
        for t in trads:
            if t != "Shinto":
                co_fns[t].append(fn)
    co_traditions = sorted(
        [{"n": t, "c": len(flist), "fns": sorted(set(flist))}
         for t, flist in co_fns.items() if len(flist) > 0],
        key=lambda x: -x["c"])

    # ── gapComparison — grouped bar ──────────────────────────────────────
    gap_comparison = _build_gap_comparison(sub_fns, paper_yaml, candidates_set,
                                           vault_total, vault_benchmark_count, vault_ethics_count)

    return {
        "conceptRadar": concept_radar, "themeDist": theme_dist,
        "cultureDist": culture_dist, "coTraditions": co_traditions,
        "gapComparison": gap_comparison,
        "conceptRadarFns": {n: sorted(set(concept_fns_map.get(n, []))) for n in SHINTO_CONCEPT_PATTERNS},
    }


def build_ubuntu_extended(sub_fns, paper_yaml, cand_lookup, candidates_set,
                          vault_total, vault_benchmark_count, vault_ethics_count):
    """Build extended Ubuntu tradition analysis data."""

    # ── conceptRadar — radar (5 Ubuntu concepts) ────────────────────────
    concept_ctr = Counter()
    concept_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in UBUNTU_CONCEPT_PATTERNS.items():
            if pat.search(abstract):
                concept_ctr[name] += 1
                concept_fns_map[name].append(fn)
    concept_radar = [{"axis": n, "val": concept_ctr.get(n, 0)}
                     for n in UBUNTU_CONCEPT_PATTERNS]

    # ── themeDist — donut (AI Governance/Decolonization/Data Ethics/Community)
    theme_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in UBUNTU_RESEARCH_THEMES.items():
            if pat.search(abstract):
                theme_fns_map[name].append(fn)
    theme_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                  for n, flist in sorted(theme_fns_map.items(), key=lambda x: -len(x[1]))]

    # ── geoDist — bar (Pan-African geographic spread) ────────────────────
    culture_fns = defaultdict(list)
    for fn in sub_fns:
        for c in paper_yaml.get(fn, {}).get("cultures_nationalities_list", []):
            if c:
                culture_fns[c].append(fn)
    geo_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                for n, flist in sorted(culture_fns.items(), key=lambda x: -len(x[1]))]

    # ── gapComparison — grouped bar ──────────────────────────────────────
    gap_comparison = _build_gap_comparison(sub_fns, paper_yaml, candidates_set,
                                           vault_total, vault_benchmark_count, vault_ethics_count)

    # ── coTraditions — bar ───────────────────────────────────────────────
    co_fns = defaultdict(list)
    for fn in sub_fns:
        f = paper_yaml.get(fn, {})
        trads = set(classify_relig_traditions(
            f.get("religious_values_list", []), f.get("religious_values", "") or ""))
        for t in trads:
            if t != "Ubuntu":
                co_fns[t].append(fn)
    co_traditions = sorted(
        [{"n": t, "c": len(flist), "fns": sorted(set(flist))}
         for t, flist in co_fns.items() if len(flist) > 0],
        key=lambda x: -x["c"])

    return {
        "conceptRadar": concept_radar, "themeDist": theme_dist,
        "geoDist": geo_dist, "gapComparison": gap_comparison,
        "coTraditions": co_traditions,
        "conceptRadarFns": {n: sorted(set(concept_fns_map.get(n, []))) for n in UBUNTU_CONCEPT_PATTERNS},
    }


def build_indigenous_extended(sub_fns, paper_yaml, cand_lookup, candidates_set,
                              vault_total, vault_benchmark_count, vault_ethics_count):
    """Build extended Indigenous traditions analysis data."""

    # ── traditionDist — donut (Maori/First Nations/Aboriginal/Native American)
    trad_fns_map = defaultdict(list)
    unclassified = []
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        matched = False
        for trad, pat in INDIGENOUS_TRADITION_PATTERNS.items():
            if pat.search(abstract):
                trad_fns_map[trad].append(fn)
                matched = True
        if not matched:
            unclassified.append(fn)
    if unclassified:
        trad_fns_map["Other Indigenous"] = unclassified
    tradition_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                      for n, flist in sorted(trad_fns_map.items(), key=lambda x: -len(x[1]))]

    # ── themeRadar — radar (5 Indigenous themes) ─────────────────────────
    theme_ctr = Counter()
    theme_fns_map = defaultdict(list)
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        for name, pat in INDIGENOUS_THEME_PATTERNS.items():
            if pat.search(abstract):
                theme_ctr[name] += 1
                theme_fns_map[name].append(fn)
    theme_radar = [{"axis": n, "val": theme_ctr.get(n, 0)}
                   for n in INDIGENOUS_THEME_PATTERNS]

    # ── geoDist — bar (geographic origins) ───────────────────────────────
    culture_fns = defaultdict(list)
    for fn in sub_fns:
        for c in paper_yaml.get(fn, {}).get("cultures_nationalities_list", []):
            if c:
                culture_fns[c].append(fn)
    geo_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                for n, flist in sorted(culture_fns.items(), key=lambda x: -len(x[1]))]

    # ── gapComparison — grouped bar ──────────────────────────────────────
    gap_comparison = _build_gap_comparison(sub_fns, paper_yaml, candidates_set,
                                           vault_total, vault_benchmark_count, vault_ethics_count)

    # ── coTraditions — bar ───────────────────────────────────────────────
    co_fns = defaultdict(list)
    for fn in sub_fns:
        f = paper_yaml.get(fn, {})
        trads = set(classify_relig_traditions(
            f.get("religious_values_list", []), f.get("religious_values", "") or ""))
        for t in trads:
            if t != "Indigenous":
                co_fns[t].append(fn)
    co_traditions = sorted(
        [{"n": t, "c": len(flist), "fns": sorted(set(flist))}
         for t, flist in co_fns.items() if len(flist) > 0],
        key=lambda x: -x["c"])

    return {
        "traditionDist": tradition_dist, "themeRadar": theme_radar,
        "geoDist": geo_dist, "gapComparison": gap_comparison,
        "coTraditions": co_traditions,
        "themeRadarFns": {n: sorted(set(theme_fns_map.get(n, []))) for n in INDIGENOUS_THEME_PATTERNS},
    }


def build_other_traditions_extended(paper_yaml, candidates_set, vault_total, vault_benchmark_count, vault_ethics_count):
    """Build extended 'Other Traditions' analysis data (Jainism, Sikhism, Taoism, Baha'i, Zoroastrianism)."""

    # Collect papers per tradition
    trad_papers = {}
    all_fns = set()
    for trad_name, info in OTHER_TRADITIONS_CONCEPTS.items():
        matched = []
        for fn, fields in paper_yaml.items():
            text = (fields.get("abstract", "") or "") + " " + \
                   " ".join(fields.get("religious_values_list", []))
            if info["pattern"].search(text):
                matched.append(fn)
        trad_papers[trad_name] = sorted(set(matched))
        all_fns.update(matched)

    # ── summaryTable — HTML data ─────────────────────────────────────────
    summary_table = []
    for trad_name, fns in trad_papers.items():
        concepts = list(OTHER_TRADITIONS_CONCEPTS[trad_name]["concepts"].keys())
        summary_table.append({
            "tradition": trad_name,
            "paperCount": len(fns),
            "benchmarkCount": sum(1 for fn in fns if fn in candidates_set),
            "keyConcepts": concepts,
            "fns": fns,
        })

    # ── conceptBar — grouped bar (key concepts per tradition) ────────────
    concept_data = []
    concept_fns_map = {}
    for trad_name, info in OTHER_TRADITIONS_CONCEPTS.items():
        fns = trad_papers[trad_name]
        for concept_name, pat in info["concepts"].items():
            matched = [fn for fn in fns
                       if pat.search(paper_yaml.get(fn, {}).get("abstract", "") or "")]
            concept_data.append({"tradition": trad_name, "concept": concept_name,
                                 "count": len(matched), "fns": sorted(set(matched))})
            concept_fns_map[f"{trad_name}:{concept_name}"] = sorted(set(matched))

    # ── gapComparison — bar ──────────────────────────────────────────────
    gap_comparison = _build_gap_comparison(all_fns, paper_yaml, candidates_set,
                                           vault_total, vault_benchmark_count, vault_ethics_count)

    return {
        "summaryTable": summary_table, "conceptData": concept_data,
        "gapComparison": gap_comparison, "conceptFns": concept_fns_map,
    }


def build_confucian_extended(sub_fns, paper_yaml, cand_lookup, candidates_set):
    """Build extended Confucian tradition analysis data."""

    CARE_PAT = re.compile(r"\bcare\s+ethic|\bethic\s+of\s+care|\bfeminist\s+ethic", re.I)
    MFT_PAT = re.compile(r"\bmoral\s+foundation|\bMFT\b|\bHaidt", re.I)
    VE_PAT = re.compile(r"\bvirtue\s+ethic", re.I)
    DE_PAT = re.compile(r"\bdeontolog|\bkantian", re.I)
    CU_PAT = re.compile(r"\butilitarian|\bconsequential", re.I)
    EMPIRICAL_PAT = re.compile(r"\bbenchmark\b|\bevaluat|\bexperiment|\bdataset\b|\bempiric|\btest\b", re.I)

    # ── culturalFootprint — treemap ──────────────────────────────────────
    culture_fns = defaultdict(list)
    for fn in sub_fns:
        for c in paper_yaml.get(fn, {}).get("cultures_nationalities_list", []):
            if c:
                culture_fns[c].append(fn)
    cultural_footprint = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                          for n, flist in sorted(culture_fns.items(), key=lambda x: -len(x[1]))]

    # ── frameworkOverlap — radar ─────────────────────────────────────────
    fw_ctr = Counter()
    fw_fns_map = defaultdict(list)
    for fn in sub_fns:
        fields = paper_yaml.get(fn, {})
        abstract = fields.get("abstract", "") or ""
        if fields.get("virtue_ethics", "").lower() in ("yes", "partial", "true") or VE_PAT.search(abstract):
            fw_ctr["Virtue Ethics"] += 1
            fw_fns_map["Virtue Ethics"].append(fn)
        if fields.get("deontological_ethics", "").lower() in ("yes", "partial", "true") or DE_PAT.search(abstract):
            fw_ctr["Deontological"] += 1
            fw_fns_map["Deontological"].append(fn)
        if fields.get("utilitarian_ethics", "").lower() in ("yes", "partial", "true") or CU_PAT.search(abstract):
            fw_ctr["Utilitarian"] += 1
            fw_fns_map["Utilitarian"].append(fn)
        if CARE_PAT.search(abstract):
            fw_ctr["Care Ethics"] += 1
            fw_fns_map["Care Ethics"].append(fn)
        mp = fields.get("moral_psychology", "") or ""
        if mp.lower() not in ("", "n/a", "na", "no", "none", "false"):
            fw_ctr["Moral Psychology"] += 1
            fw_fns_map["Moral Psychology"].append(fn)
        if MFT_PAT.search(abstract):
            fw_ctr["MFT"] += 1
            fw_fns_map["MFT"].append(fn)
    AXES = ["Virtue Ethics", "Deontological", "Utilitarian", "Care Ethics", "Moral Psychology", "MFT"]
    framework_overlap = [{"axis": a, "val": fw_ctr.get(a, 0)} for a in AXES]

    # ── chineseVsWesternLLMs — grouped bar ───────────────────────────────
    model_info = defaultdict(lambda: {"c": 0, "origin": "Western", "fns": []})
    for fn in sub_fns:
        llm = paper_yaml.get(fn, {}).get("LLM_assessed", "") or ""
        if llm.lower() in ("na", "n/a", "none", ""):
            continue
        for fam in extract_model_families(llm):
            model_info[fam]["c"] += 1
            model_info[fam]["origin"] = "Chinese" if fam in CHINESE_LLM_NAMES else "Western"
            model_info[fam]["fns"].append(fn)
    chinese_vs_western = sorted(
        [{"n": n, "c": d["c"], "origin": d["origin"], "fns": sorted(set(d["fns"]))} for n, d in model_info.items()],
        key=lambda x: -x["c"])

    # ── languageDist — donut ─────────────────────────────────────────────
    lang_bucket_fns = defaultdict(list)
    for fn in sub_fns:
        for lang in paper_yaml.get(fn, {}).get("languages_list", []):
            if not lang:
                continue
            ll = lang.lower()
            if "chinese" in ll or "mandarin" in ll or "cantonese" in ll:
                lang_bucket_fns["Chinese"].append(fn)
            elif "korean" in ll:
                lang_bucket_fns["Korean"].append(fn)
            elif "japanese" in ll:
                lang_bucket_fns["Japanese"].append(fn)
            elif "english" in ll:
                lang_bucket_fns["English"].append(fn)
            elif "multilingual" in ll or "multi-lingual" in ll:
                lang_bucket_fns["Multilingual"].append(fn)
            else:
                lang_bucket_fns["Other"].append(fn)
    language_dist = [{"n": n, "c": len(flist), "fns": sorted(set(flist))}
                     for n, flist in sorted(lang_bucket_fns.items(), key=lambda x: -len(x[1]))]

    # ── researchProfile — stacked bar by year ────────────────────────────
    yr_emp, yr_theo = Counter(), Counter()
    emp_fns_all, theo_fns_all = [], []
    for fn in sub_fns:
        abstract = paper_yaml.get(fn, {}).get("abstract", "") or ""
        year = extract_year(fn)
        if year == 9999:
            continue
        if fn in candidates_set or EMPIRICAL_PAT.search(abstract):
            yr_emp[year] += 1
            emp_fns_all.append(fn)
        else:
            yr_theo[year] += 1
            theo_fns_all.append(fn)
    all_yrs = sorted(y for y in set(list(yr_emp) + list(yr_theo)) if y >= 2016)
    research_profile = {
        "years": all_yrs,
        "empirical": [yr_emp.get(y, 0) for y in all_yrs],
        "theoretical": [yr_theo.get(y, 0) for y in all_yrs],
    }

    # ── conceptFreq — horizontal bar ─────────────────────────────────────
    concept_freq = []
    for name, keywords in CONFUCIAN_CONCEPT_KEYWORDS.items():
        matched_fns = [fn for fn in sub_fns
                       if any(kw.lower() in (paper_yaml.get(fn, {}).get("abstract", "") or "").lower()
                              for kw in keywords)]
        if matched_fns:
            concept_freq.append({"n": name, "c": len(matched_fns), "fns": sorted(set(matched_fns))})
    concept_freq.sort(key=lambda x: -x["c"])

    return {
        "culturalFootprint": cultural_footprint, "frameworkOverlap": framework_overlap,
        "chineseVsWesternLLMs": chinese_vs_western, "languageDist": language_dist,
        "researchProfile": research_profile, "conceptFreq": concept_freq,
        "frameworkOverlapFns": {a: sorted(set(fw_fns_map.get(a, []))) for a in AXES},
        "researchProfileFns": {"Empirical": sorted(set(emp_fns_all)), "Theoretical": sorted(set(theo_fns_all))},
    }




def compute_religious_data(paper_yaml, candidates, candidates_set):
    """Compute religious values data with FIXED sub-sections."""
    cand_lookup = {e["filename"]: e for e in candidates}

    relig_papers = []
    paper_traditions = {}
    tradition_counter = Counter()
    tradition_year = defaultdict(Counter)
    tradition_paper_sets = defaultdict(set)
    benchmark_count = 0

    for fn, fields in paper_yaml.items():
        relig_list = fields.get('religious_values_list', [])
        relig_val = fields.get('religious_values', '') or ''

        if not relig_list and relig_val.lower() in ('n/a', 'na', 'no', 'none', '', 'false'):
            continue

        trads = classify_relig_traditions(relig_list, relig_val)
        if not trads and relig_val.lower() in ('n/a', 'na', 'no', 'none', '', 'false'):
            continue

        year = extract_year(fn)
        is_bench = fn in candidates_set
        if is_bench:
            benchmark_count += 1

        cand = cand_lookup.get(fn, {})
        combined_model_text = get_models_text(cand, fields)

        relig_papers.append({
            "fn": fn,
            "y": year if year != 9999 else 0,
            "tr": trads,
            "ib": 1 if is_bench else 0,
            "bn": get_benchmark_name(cand, fields),
            "wm": get_what_measures(cand, fields),
            "lm": extract_model_families(combined_model_text)[:5],
        })

        paper_traditions[fn] = trads
        for t in trads:
            tradition_counter[t] += 1
            tradition_paper_sets[t].add(fn)
            if year != 9999:
                tradition_year[t][year] += 1

    # Tradition distribution
    tradition_dist = []
    for meta in TRADITION_META:
        name = meta["name"]
        tradition_dist.append({
            "n": name,
            "a": meta["abbrev"],
            "c": tradition_counter.get(name, 0),
            "col": meta["color"],
        })

    # Sub-sections — FIXED: full paper objects
    def build_trad_subsection(trad_names):
        sub_fns = set()
        for t in trad_names:
            sub_fns |= tradition_paper_sets.get(t, set())
        sub_papers = []
        year_dist = Counter()
        model_counter = Counter()
        bench_count = 0
        for fn in sub_fns:
            fields = paper_yaml.get(fn, {})
            cand = cand_lookup.get(fn, {})
            combined_model_text = get_models_text(cand, fields)
            year = extract_year(fn)
            if year != 9999:
                year_dist[year] += 1
            for m in extract_model_families(combined_model_text):
                model_counter[m] += 1
            if fn in cand_lookup:
                bench_count += 1
            sub_papers.append({
                "fn": fn,
                "y": year if year != 9999 else 0,
                "ib": 1 if fn in candidates_set else 0,
                "bn": get_benchmark_name(cand, fields),
                "wm": get_what_measures(cand, fields),
                "lm": extract_model_families(combined_model_text)[:5],
            })
        return {
            "papers": sub_papers,
            "count": len(sub_papers),
            "benchmarkCount": bench_count,
            "yearDist": {str(y): c for y, c in sorted(year_dist.items()) if y >= 2016},
            "topModels": [{"n": n, "c": c} for n, c in model_counter.most_common(10)],
        }

    islamic_data = build_trad_subsection(["Islam"])
    christianity_data = build_trad_subsection(["Christianity"])
    judaism_data = build_trad_subsection(["Judaism"])
    buddhism_data = build_trad_subsection(["Buddhism"])
    hinduism_data = build_trad_subsection(["Hinduism"])
    confucian_data = build_trad_subsection(["Confucian"])
    shinto_data = build_trad_subsection(["Shinto"])
    ubuntu_data = build_trad_subsection(["Ubuntu"])
    indigenous_data = build_trad_subsection(["Indigenous"])

    # ── Extended analyses per tradition ───────────────────────────────────
    islamic_data.update(build_islamic_extended(
        tradition_paper_sets.get("Islam", set()), paper_yaml, cand_lookup, candidates_set))
    christianity_data.update(build_christianity_extended(
        tradition_paper_sets.get("Christianity", set()), paper_yaml, cand_lookup, candidates_set))
    judaism_data.update(build_judaism_extended(
        tradition_paper_sets.get("Judaism", set()), paper_yaml, cand_lookup, candidates_set))
    buddhism_data.update(build_buddhism_extended(
        tradition_paper_sets.get("Buddhism", set()), paper_yaml, cand_lookup, candidates_set))
    hinduism_data.update(build_hinduism_extended(
        tradition_paper_sets.get("Hinduism", set()), paper_yaml, cand_lookup, candidates_set))
    confucian_data.update(build_confucian_extended(
        tradition_paper_sets.get("Confucian", set()), paper_yaml, cand_lookup, candidates_set))

    vault_total = len(paper_yaml)
    vault_bench_ct = len(candidates_set)
    vault_ethics_ct = sum(1 for f in paper_yaml.values()
                          if f.get("ethics_overall", "").lower() == "yes")
    shinto_data.update(build_shinto_extended(
        tradition_paper_sets.get("Shinto", set()), paper_yaml, cand_lookup, candidates_set,
        vault_total, vault_bench_ct, vault_ethics_ct))
    ubuntu_data.update(build_ubuntu_extended(
        tradition_paper_sets.get("Ubuntu", set()), paper_yaml, cand_lookup, candidates_set,
        vault_total, vault_bench_ct, vault_ethics_ct))
    indigenous_data.update(build_indigenous_extended(
        tradition_paper_sets.get("Indigenous", set()), paper_yaml, cand_lookup, candidates_set,
        vault_total, vault_bench_ct, vault_ethics_ct))

    other_traditions_data = build_other_traditions_extended(
        paper_yaml, candidates_set, vault_total, vault_bench_ct, vault_ethics_ct)

    # Timeline
    all_years = sorted(set(y for tc in tradition_year.values() for y in tc.keys() if y >= 2016))
    abrahamic = ["Islam", "Christianity", "Judaism"]
    dharmic_names = ["Buddhism", "Hinduism"]
    east_asian = ["Confucian", "Shinto"]
    african_indigenous = ["Ubuntu", "Indigenous"]

    timeline = {
        "years": all_years,
        "abrahamic": [sum(tradition_year.get(t, Counter()).get(y, 0) for t in abrahamic) for y in all_years],
        "dharmic": [sum(tradition_year.get(t, Counter()).get(y, 0) for t in dharmic_names) for y in all_years],
        "eastAsian": [sum(tradition_year.get(t, Counter()).get(y, 0) for t in east_asian) for y in all_years],
        "africanIndigenous": [sum(tradition_year.get(t, Counter()).get(y, 0) for t in african_indigenous) for y in all_years],
    }

    # Cooccurrence
    trad_names = [m["name"] for m in TRADITION_META]
    n = len(trad_names)
    cooccurrence = [[0] * n for _ in range(n)]
    for fn, trads in paper_traditions.items():
        indices = [trad_names.index(t) for t in trads if t in trad_names]
        for ii in range(len(indices)):
            for jj in range(ii + 1, len(indices)):
                cooccurrence[indices[ii]][indices[jj]] += 1
                cooccurrence[indices[jj]][indices[ii]] += 1

    return {
        "papers": relig_papers,
        "paperCount": len(relig_papers),
        "traditionDist": tradition_dist,
        "timeline": timeline,
        "benchmarkCount": benchmark_count,
        "islamic": islamic_data,
        "christianity": christianity_data,
        "judaism": judaism_data,
        "buddhism": buddhism_data,
        "hinduism": hinduism_data,
        "confucian": confucian_data,
        "shinto": shinto_data,
        "ubuntu": ubuntu_data,
        "indigenous": indigenous_data,
        "otherTraditions": other_traditions_data,
        "cooccurrence": cooccurrence,
        "coLabels": trad_names,
    }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION 7b: BASE DATA (categories, models, methods, etc.)
# ═══════════════════════════════════════════════════════════════════════════

def compute_taxonomy_data(candidates, paper_yaml):
    """Compute taxonomy & methods tab data."""
    cat_order = sorted(CATEGORIES.keys(), key=lambda c: int(c.split(".")[0]))
    cat_short = [c.split(". ", 1)[1] for c in cat_order]

    # Classify candidates
    entry_cats = {}
    cat_entries = defaultdict(list)
    for e in candidates:
        cats = classify_entry(e)
        if not cats:
            full_text = " ".join([
                e.get("benchmark_name", ""),
                e.get("what_measures", ""),
                e.get("how_measures", ""),
                e.get("reasoning", ""),
            ]).lower()
            if any(w in full_text for w in ["trust", "reliab", "robust", "risk"]):
                cats = ["6. Safety & Red Teaming"]
            elif any(w in full_text for w in ["social", "norm", "stereotyp"]):
                cats = ["4. Fairness, Bias & Social Norms"]
            elif any(w in full_text for w in ["moral", "ethic"]):
                cats = ["1. Moral Reasoning & Ethical Judgment"]
            else:
                cats = ["4. Fairness, Bias & Social Norms"]
        entry_cats[e["filename"]] = cats
        for c in cats:
            cat_entries[c].append(e)

    # Category counts and by-year
    categories = []
    for i, cat in enumerate(cat_order):
        short = cat.split(". ", 1)[1]
        fns = list({e["filename"] for e in cat_entries.get(cat, [])})
        by_year = Counter()
        for e in cat_entries.get(cat, []):
            y = extract_year(e["filename"])
            if y != 9999:
                by_year[y] += 1
        categories.append({
            "id": i + 1,
            "n": short,
            "c": len(fns),
            "byYear": {str(y): c for y, c in sorted(by_year.items()) if y >= 2016},
        })

    # Co-occurrence matrix
    n_cats = len(cat_order)
    cooccurrence = [[0] * n_cats for _ in range(n_cats)]
    for fn, cats in entry_cats.items():
        indices = []
        for c in cats:
            idx = next((i for i, co in enumerate(cat_order) if co == c), None)
            if idx is not None:
                indices.append(idx)
        for ii in range(len(indices)):
            for jj in range(ii + 1, len(indices)):
                cooccurrence[indices[ii]][indices[jj]] += 1
                cooccurrence[indices[jj]][indices[ii]] += 1

    # Model families
    model_counter = Counter()
    model_by_cat = defaultdict(Counter)
    for e in candidates:
        fams = extract_model_families(e.get("models_evaluated", ""))
        cats = classify_entry(e) or ["Uncategorized"]
        for f in fams:
            model_counter[f] += 1
            for c in cats:
                sc = c.split(". ", 1)[1] if ". " in c else c
                model_by_cat[f][sc] += 1

    top_models = []
    for name, count in model_counter.most_common(20):
        by_cat = [model_by_cat[name].get(s, 0) for s in cat_short]
        top_models.append({"n": name, "c": count, "bc": by_cat})

    return {
        "categories": categories,
        "catNames": cat_short,
        "cooccurrence": cooccurrence,
        "models": top_models,
    }


def compute_cultural_data(paper_yaml, papers):
    """Compute cultural values tab data (v8b: enriched with 10 new analyses)."""
    culture_counter = Counter()
    region_counter = Counter()
    treemap_data = defaultdict(Counter)
    region_year = defaultdict(Counter)
    weird_counts = {"WEIRD": 0, "Non-WEIRD": 0, "Mixed": 0}
    lang_counter = Counter()
    paper_count = 0

    # ── NEW: additional trackers for enriched subtabs ──
    META_REGIONS = {"Multi-Region"}
    culture_year = defaultdict(Counter)       # C2: culture timeline
    culture_pairs = Counter()                 # C1: co-occurrence
    lang_year = defaultdict(Counter)          # L2: language timeline
    lang_family_tree = defaultdict(Counter)   # L1: language family treemap
    META_LANGS = {"multilingual", "multiple", "various"}

    for fn, fields in paper_yaml.items():
        cultures = fields.get('cultures_nationalities_list', [])
        if not cultures:
            continue
        paper_count += 1
        year = extract_year(fn)
        if year == 9999:
            year = 0

        primary_region = classify_region(cultures[0])
        w = classify_weird(primary_region)
        weird_counts[w] = weird_counts.get(w, 0) + 1

        paper_regions = set()
        specific_cultures = []
        for c in cultures:
            culture_counter[c] += 1
            r = classify_region(c)
            region_counter[r] += 1
            treemap_data[r][c] += 1
            paper_regions.add(r)
            # Track specific (non-meta) cultures for C1/C2
            if r not in META_REGIONS:
                specific_cultures.append(c)

        for r in paper_regions:
            if year > 0:
                region_year[r][year] += 1

        # C2: culture-year cross-tab (specific cultures only)
        for c in specific_cultures:
            if year > 0:
                culture_year[c][year] += 1

        # C1: culture co-occurrence (papers with 2+ specific cultures)
        uniq_specific = list(dict.fromkeys(specific_cultures))  # dedupe, preserve order
        if len(uniq_specific) >= 2:
            for i, a in enumerate(uniq_specific):
                for b in uniq_specific[i + 1:]:
                    pair = tuple(sorted([a, b]))
                    culture_pairs[pair] += 1

        # L1/L2: language tracking
        for lang in fields.get('languages_list', []):
            lang_counter[lang] += 1
            if lang.lower() not in META_LANGS:
                family = classify_lang_family(lang)
                lang_family_tree[family][lang] += 1
                if year > 0:
                    lang_year[lang][year] += 1

    # ── Original outputs ──────────────────────────────────────────────
    # Region distribution
    region_dist = [{"n": r, "c": c} for r, c in region_counter.most_common()]

    # Country distribution (top 30)
    country_dist = []
    for c, count in culture_counter.most_common(30):
        country_dist.append({"n": c, "c": count, "r": classify_region(c)})

    # Treemap
    treemap = []
    for r, cultures_map in sorted(treemap_data.items()):
        children = [{"n": c, "v": v} for c, v in cultures_map.most_common()]
        treemap.append({"n": r, "ch": children})

    # Timeline
    all_regions = sorted(region_counter.keys())
    all_years = sorted(set(y for rc in region_year.values() for y in rc.keys() if y >= 2016))
    timeline = {
        "years": all_years,
        "regions": all_regions,
        "series": {r: [region_year[r].get(y, 0) for y in all_years] for r in all_regions},
    }

    # Language distribution (top 20)
    lang_dist = [{"n": n, "c": c} for n, c in lang_counter.most_common(20)]

    # ── NEW: enriched outputs (v8b) ───────────────────────────────────

    # Build paper lookup for cross-tabs with benchmark/venue/ethics flags
    paper_lookup = {p['fn']: p for p in papers}

    # --- C1: Culture Co-Occurrence Matrix (15×15 symmetric heatmap) ---
    # Use top 15 specific cultures (exclude Multi-Region)
    specific_culture_counter = Counter()
    for c, count in culture_counter.items():
        if classify_region(c) not in META_REGIONS:
            specific_culture_counter[c] = count
    co_labels = [c for c, _ in specific_culture_counter.most_common(15)]
    co_idx = {c: i for i, c in enumerate(co_labels)}
    n_co = len(co_labels)
    co_matrix = [[0] * n_co for _ in range(n_co)]
    # Diagonal = culture frequency; off-diagonal = co-occurrence count
    for c in co_labels:
        co_matrix[co_idx[c]][co_idx[c]] = specific_culture_counter[c]
    for (a, b), cnt in culture_pairs.items():
        if a in co_idx and b in co_idx:
            co_matrix[co_idx[a]][co_idx[b]] = cnt
            co_matrix[co_idx[b]][co_idx[a]] = cnt

    # --- C2: Culture Focus Shift Timeline (stacked area, top 10) ---
    top10_cultures = [c for c, _ in specific_culture_counter.most_common(10)]
    cult_tl_years = sorted(set(
        y for cc in culture_year.values() for y in cc.keys() if y >= 2016))
    culture_timeline = {
        "years": cult_tl_years,
        "cultures": top10_cultures,
        "series": {c: [culture_year[c].get(y, 0) for y in cult_tl_years]
                   for c in top10_cultures},
    }

    # --- C3: Ethical Framework × Culture Heatmap ---
    fw_columns = ["VE", "DE", "CU", "Ethics-Gen", "Non-Ethics"]
    top12_cultures = [c for c, _ in specific_culture_counter.most_common(12)]
    fw_matrix = [[0] * len(fw_columns) for _ in range(len(top12_cultures))]
    for fn, fields in paper_yaml.items():
        p = paper_lookup.get(fn)
        if not p:
            continue
        cultures_list = fields.get('cultures_nationalities_list', [])
        for ci, cult in enumerate(top12_cultures):
            if cult not in cultures_list:
                continue
            if p.get('ve'):
                fw_matrix[ci][0] += 1
            if p.get('de'):
                fw_matrix[ci][1] += 1
            if p.get('ue'):
                fw_matrix[ci][2] += 1
            if p.get('eo') and not p.get('ve') and not p.get('de') and not p.get('ue'):
                fw_matrix[ci][3] += 1  # Ethics-General (ethics=yes but no specific branch)
            if not p.get('eo'):
                fw_matrix[ci][4] += 1  # Non-Ethics

    # --- C4: Benchmark Gap by Culture (grouped bar, top 15) ---
    top15_cultures = [c for c, _ in specific_culture_counter.most_common(15)]
    cult_bench = {c: 0 for c in top15_cultures}
    cult_concept = {c: 0 for c in top15_cultures}
    for fn, fields in paper_yaml.items():
        p = paper_lookup.get(fn)
        if not p:
            continue
        cultures_list = fields.get('cultures_nationalities_list', [])
        has_bench = p.get('ib') or p.get('ie')
        for cult in top15_cultures:
            if cult in cultures_list:
                if has_bench:
                    cult_bench[cult] += 1
                else:
                    cult_concept[cult] += 1

    # --- C5: Culture × Venue Type Heatmap ---
    venue_categories = ["Conference", "Journal", "Preprint", "Workshop", "Findings", "Other"]
    top12c_venue = top12_cultures  # reuse same top 12
    cv_matrix = [[0] * len(venue_categories) for _ in range(len(top12c_venue))]
    vc_idx = {v: i for i, v in enumerate(venue_categories)}
    for fn, fields in paper_yaml.items():
        p = paper_lookup.get(fn)
        if not p:
            continue
        vt = p.get('vt', 'Other') or 'Other'
        if vt not in vc_idx:
            vt = 'Other'
        cultures_list = fields.get('cultures_nationalities_list', [])
        for ci, cult in enumerate(top12c_venue):
            if cult in cultures_list:
                cv_matrix[ci][vc_idx[vt]] += 1

    # --- L1: Language Family Treemap ---
    lang_family_tm = []
    for family in sorted(lang_family_tree.keys()):
        children = [{"n": lang, "v": cnt}
                    for lang, cnt in lang_family_tree[family].most_common()]
        lang_family_tm.append({"n": family, "ch": children})

    # --- L2: Language Coverage Timeline (top 9: English + 8 non-English) ---
    lang_rank = lang_counter.most_common()
    top_non_en = [l for l, _ in lang_rank
                  if l.lower() not in META_LANGS and l != "English"][:8]
    tl_langs = (["English"] if "English" in lang_counter else []) + top_non_en
    lang_tl_years = sorted(set(
        y for lc in lang_year.values() for y in lc.keys() if y >= 2016))
    lang_timeline = {
        "years": lang_tl_years,
        "languages": tl_langs,
        "series": {l: [lang_year[l].get(y, 0) for y in lang_tl_years]
                   for l in tl_langs},
    }

    # --- L3: Language Benchmark Gap (grouped bar, top 15) ---
    specific_lang_counter = Counter({l: c for l, c in lang_counter.items()
                                     if l.lower() not in META_LANGS})
    top15_langs = [l for l, _ in specific_lang_counter.most_common(15)]
    lang_bench = {l: 0 for l in top15_langs}
    lang_concept = {l: 0 for l in top15_langs}
    for fn, fields in paper_yaml.items():
        p = paper_lookup.get(fn)
        if not p:
            continue
        langs_list = fields.get('languages_list', [])
        has_bench = p.get('ib') or p.get('ie')
        for lang in top15_langs:
            if lang in langs_list:
                if has_bench:
                    lang_bench[lang] += 1
                else:
                    lang_concept[lang] += 1

    # --- L4: Language-Culture Alignment Radar ---
    # Compute coverage % by region for both cultures and languages
    radar_regions = sorted(set(
        r for r in region_counter.keys() if r not in META_REGIONS and r != "Other"))
    total_culture_tags = sum(region_counter[r] for r in radar_regions) or 1
    culture_pct = [round(region_counter.get(r, 0) / total_culture_tags * 100, 1)
                   for r in radar_regions]
    # Language→region counts
    lang_region_counter = Counter()
    for fn, fields in paper_yaml.items():
        for lang in fields.get('languages_list', []):
            if lang.lower() not in META_LANGS:
                lr = classify_lang_region(lang)
                if lr != "Other":
                    lang_region_counter[lr] += 1
    total_lang_tags = sum(lang_region_counter[r] for r in radar_regions) or 1
    lang_pct = [round(lang_region_counter.get(r, 0) / total_lang_tags * 100, 1)
                for r in radar_regions]

    # --- L5: Language × Venue Type Heatmap ---
    top12_langs = [l for l, _ in specific_lang_counter.most_common(12)]
    lv_matrix = [[0] * len(venue_categories) for _ in range(len(top12_langs))]
    for fn, fields in paper_yaml.items():
        p = paper_lookup.get(fn)
        if not p:
            continue
        vt = p.get('vt', 'Other') or 'Other'
        if vt not in vc_idx:
            vt = 'Other'
        langs_list = fields.get('languages_list', [])
        for li, lang in enumerate(top12_langs):
            if lang in langs_list:
                lv_matrix[li][vc_idx[vt]] += 1

    return {
        "paperCount": paper_count,
        "cultureCount": len(culture_counter),
        "regionDist": region_dist,
        "countryDist": country_dist,
        "treemap": treemap,
        "timeline": timeline,
        "weird": weird_counts,
        "langDist": lang_dist,
        # ── v8b enrichments ──
        "coLabels": co_labels,
        "coMatrix": co_matrix,
        "cultureTimeline": culture_timeline,
        "cultureFramework": {
            "cultures": top12_cultures,
            "columns": fw_columns,
            "matrix": fw_matrix,
        },
        "cultureBenchmark": {
            "cultures": top15_cultures,
            "benchEval": [cult_bench[c] for c in top15_cultures],
            "conceptual": [cult_concept[c] for c in top15_cultures],
        },
        "cultureVenue": {
            "cultures": top12c_venue,
            "venues": venue_categories,
            "matrix": cv_matrix,
        },
        "langFamilyTreemap": lang_family_tm,
        "langTimeline": lang_timeline,
        "langBenchmark": {
            "languages": top15_langs,
            "benchEval": [lang_bench[l] for l in top15_langs],
            "conceptual": [lang_concept[l] for l in top15_langs],
        },
        "langCultureRadar": {
            "regions": radar_regions,
            "culturePct": culture_pct,
            "langPct": lang_pct,
        },
        "langVenue": {
            "languages": top12_langs,
            "venues": venue_categories,
            "matrix": lv_matrix,
        },
    }


def compute_llm_data(paper_yaml, candidates):
    """Compute Models & LLMs tab data."""
    # LLM model counter from YAML LLM_assessed
    llm_model_counter = Counter()
    for fn, d in paper_yaml.items():
        llm = d.get("LLM_assessed", "") or ""
        if not llm or llm.lower() in ("na", "n/a", "none"):
            continue
        for m in [m.strip() for m in llm.split(",") if m.strip()]:
            llm_model_counter[m] += 1
    llm_models = [{"n": n, "c": c} for n, c in llm_model_counter.most_common(20)]

    # LLM assessment by year
    assessed_by_year = Counter()
    not_assessed_by_year = Counter()
    for fn, d in paper_yaml.items():
        year = extract_year(fn)
        if year == 9999:
            continue
        if d.get("LLM_assessed", "NA") not in ("NA", "N/A", "", "na"):
            assessed_by_year[year] += 1
        else:
            not_assessed_by_year[year] += 1
    all_years = sorted(set(list(assessed_by_year.keys()) + list(not_assessed_by_year.keys())))
    llm_by_year = {str(y): {"a": assessed_by_year.get(y, 0), "na": not_assessed_by_year.get(y, 0)}
                   for y in all_years if y >= 2016}

    # Repo distribution from DATA_URL
    repo_counter = Counter()
    for fn, d in paper_yaml.items():
        du = d.get("DATA_URL", "") or ""
        if not du or du.lower() in ("na", "n/a", "none"):
            continue
        url = du.lower()
        if "github.com" in url:
            repo_counter["GitHub"] += 1
        elif "huggingface" in url or "hf.co" in url:
            repo_counter["HuggingFace"] += 1
        elif "zenodo" in url:
            repo_counter["Zenodo"] += 1
        elif "osf.io" in url:
            repo_counter["OSF"] += 1
        elif "kaggle" in url:
            repo_counter["Kaggle"] += 1
        else:
            repo_counter["Other"] += 1
    repo_dist = [{"n": n, "c": c} for n, c in repo_counter.most_common()]

    # Model families from candidate models_evaluated
    model_counter = Counter()
    model_by_year = defaultdict(Counter)
    for e in candidates:
        fams = extract_model_families(e.get("models_evaluated", ""))
        yr = extract_year(e["filename"])
        for f in fams:
            model_counter[f] += 1
            if yr != 9999:
                model_by_year[f][yr] += 1
    model_families = []
    for name, count in model_counter.most_common(20):
        by_year = {str(y): c for y, c in sorted(model_by_year[name].items()) if y >= 2016}
        model_families.append({"n": name, "c": count, "by": by_year})

    return {
        "llmModels": llm_models,
        "llmByYear": llm_by_year,
        "repoDist": repo_dist,
        "modelFamilies": model_families,
    }


# ═══════════════════════════════════════════════════════════════════════════
# SECTION: AUTHORS & COLLABORATION DATA
# ═══════════════════════════════════════════════════════════════════════════


def _norm_author(name):
    """Normalize author name for deduplication."""
    return " ".join(sorted(name.lower().replace(",", "").replace(".", "").split()))


def build_author_data(author_map, paper_yaml, papers):
    """Build Authors & Collaboration tab data (5 subtabs)."""

    # ── Core data structures ──────────────────────────────────────────────
    # Map: normalized name → display name (pick most common form)
    norm_to_display = defaultdict(Counter)
    # Map: normalized name → set of paper stems
    norm_to_papers = defaultdict(set)
    # Map: paper stem → list of normalized author names
    paper_to_norms = {}
    # Per-paper team sizes
    team_sizes = []
    # Year → list of normalized names (for "new authors per year")
    year_authors = defaultdict(set)

    for stem, info in author_map.items():
        authors = info.get("authors", [])
        if not authors:
            continue
        team_sizes.append(len(authors))
        yr = extract_year(stem)
        norms = []
        for name in authors:
            norm = _norm_author(name)
            if not norm:
                continue
            norm_to_display[norm][name] += 1
            norm_to_papers[norm].add(stem)
            norms.append(norm)
            if yr != 9999:
                year_authors[yr].add(norm)
        paper_to_norms[stem] = norms

    # Resolve display names (most frequent form)
    display = {}
    for norm, ctr in norm_to_display.items():
        display[norm] = ctr.most_common(1)[0][0]

    unique_count = len(norm_to_papers)
    paper_count_per_author = {norm: len(stems) for norm, stems in norm_to_papers.items()}
    prolific_3 = sum(1 for c in paper_count_per_author.values() if c >= 3)
    prolific_10 = sum(1 for c in paper_count_per_author.values() if c >= 10)

    # ── Author profiles stats ─────────────────────────────────────────────
    profile_count = 0
    enriched_count = 0
    if AUTHOR_PROFILES_DIR.exists():
        for p in AUTHOR_PROFILES_DIR.iterdir():
            if p.suffix == ".md":
                profile_count += 1
                # Quick check: if file > 500 bytes, likely enriched
                if p.stat().st_size > 500:
                    enriched_count += 1

    # ── 3a: Overview subtab ───────────────────────────────────────────────
    import statistics as stats_mod
    median_team = stats_mod.median(team_sizes) if team_sizes else 0
    single_author = sum(1 for s in team_sizes if s == 1)

    # Team size distribution (bar chart)
    size_counter = Counter(min(s, 15) for s in team_sizes)  # cap at 15+
    team_dist = []
    for s in sorted(size_counter.keys()):
        label = f"{s}+" if s == 15 else str(s)
        team_dist.append({"n": label, "c": size_counter[s]})

    # Author productivity / Lotka's Law (how many authors have 1, 2, 3... papers)
    prod_counter = Counter()
    for norm, count in paper_count_per_author.items():
        bucket = min(count, 10)  # cap at 10+
        prod_counter[bucket] += 1
    lotka = []
    for b in sorted(prod_counter.keys()):
        label = f"{b}+" if b == 10 else str(b)
        lotka.append({"n": f"{label} paper{'s' if b != 1 else ''}", "c": prod_counter[b]})

    # New authors per year (stacked: returning vs new)
    all_years = sorted(y for y in year_authors.keys() if 2010 <= y <= 2026)
    seen_authors = set()
    new_per_year = []
    returning_per_year = []
    for yr in all_years:
        yr_set = year_authors[yr]
        new_this_year = yr_set - seen_authors
        returning = yr_set & seen_authors
        new_per_year.append(len(new_this_year))
        returning_per_year.append(len(returning))
        seen_authors |= yr_set

    # Team size over time (median per year)
    year_team_sizes = defaultdict(list)
    for stem, info in author_map.items():
        yr = extract_year(stem)
        authors = info.get("authors", [])
        if yr != 9999 and 2010 <= yr <= 2026 and authors:
            year_team_sizes[yr].append(len(authors))
    median_team_by_year = []
    for yr in all_years:
        sizes = year_team_sizes.get(yr, [])
        median_team_by_year.append(round(stats_mod.median(sizes), 1) if sizes else 0)

    overview = {
        "uniqueAuthors": unique_count,
        "medianTeam": median_team,
        "singleAuthor": single_author,
        "prolific3": prolific_3,
        "prolific10": prolific_10,
        "profileCount": profile_count,
        "enrichedCount": enriched_count,
        "teamDist": team_dist,
        "lotka": lotka,
        "years": all_years,
        "newPerYear": new_per_year,
        "returningPerYear": returning_per_year,
        "medianTeamByYear": median_team_by_year,
    }

    # ── 3b: Key Voices (Prolific Authors) ─────────────────────────────────
    # Top 30 authors by total appearances
    top30_norms = sorted(paper_count_per_author.keys(),
                         key=lambda n: paper_count_per_author[n], reverse=True)[:30]

    # Position breakdown: first-author, last-author, middle
    position_data = []
    for norm in top30_norms:
        first_count = 0
        last_count = 0
        middle_count = 0
        for stem in norm_to_papers[norm]:
            info = author_map.get(stem, {})
            authors = info.get("authors", [])
            author_norms = [_norm_author(a) for a in authors]
            if norm in author_norms:
                idx = author_norms.index(norm)
                if idx == 0:
                    first_count += 1
                elif idx == len(author_norms) - 1 and len(author_norms) > 1:
                    last_count += 1
                else:
                    middle_count += 1
        position_data.append({
            "n": display[norm],
            "c": paper_count_per_author[norm],
            "first": first_count,
            "last": last_count,
            "mid": middle_count,
        })

    # Author subfield radar — top 10 authors × 6 dimensions
    top10_norms = top30_norms[:10]
    dimensions = ["ethics", "benchmark", "cultural", "moral_psych", "religious", "llm"]
    dim_labels = ["Ethics", "Benchmark", "Cultural", "Moral Psych", "Religious", "LLM"]

    # Build paper → dimension flags from papers array
    paper_fn_to_dims = {}
    for p in papers:
        paper_fn_to_dims[p["fn"]] = {
            "ethics": p["eo"],
            "benchmark": p["ib"],
            "cultural": 1 if p["cu"] else 0,
            "moral_psych": 1 if p["mp"] else 0,
            "religious": 1 if p["rv"] else 0,
            "llm": 1 if p["lm"] else 0,
        }

    radar_data = []
    for norm in top10_norms:
        dim_counts = {d: 0 for d in dimensions}
        for stem in norm_to_papers[norm]:
            fn = stem + ".md" if not stem.endswith(".md") else stem
            fn_noext = stem.replace(".md", "") if stem.endswith(".md") else stem
            dims = paper_fn_to_dims.get(fn) or paper_fn_to_dims.get(fn_noext, {})
            for d in dimensions:
                dim_counts[d] += dims.get(d, 0)
        radar_data.append({
            "name": display[norm],
            "values": [dim_counts[d] for d in dimensions],
        })

    # Top authors timeline (heatmap: top 15 × years)
    top15_norms = top30_norms[:15]
    hm_years = [y for y in all_years if y >= 2016]
    hm_matrix = []
    for norm in top15_norms:
        row = []
        for yr in hm_years:
            count = sum(1 for stem in norm_to_papers[norm]
                        if extract_year(stem) == yr)
            row.append(count)
        hm_matrix.append(row)

    prolific = {
        "top30": position_data,
        "radarDimLabels": dim_labels,
        "radarData": radar_data,
        "hmYears": [str(y) for y in hm_years],
        "hmAuthors": [display[n] for n in top15_norms],
        "hmMatrix": hm_matrix,
    }

    # ── 3c: Collaboration ─────────────────────────────────────────────────
    # Co-author pairs
    pair_counter = Counter()
    for stem, norms in paper_to_norms.items():
        # Only consider papers with ≤20 authors to avoid mega-team noise
        if len(norms) > 20:
            continue
        for i, a in enumerate(norms):
            for b in norms[i+1:]:
                pair = tuple(sorted([a, b]))
                pair_counter[pair] += 1

    top20_pairs = pair_counter.most_common(20)
    coauthor_pairs = [
        {"a": display[a], "b": display[b], "c": c}
        for (a, b), c in top20_pairs
    ]

    # Network graph — top ~80 nodes by paper count, edges = co-authorship
    top_nodes_norms = sorted(paper_count_per_author.keys(),
                             key=lambda n: paper_count_per_author[n],
                             reverse=True)[:80]
    top_node_set = set(top_nodes_norms)

    # Build paper fn → paper dict lookup for venue type / year
    papers_by_fn = {p["fn"]: p for p in papers}

    # Dimension priority for tie-breaking (first = highest priority)
    dim_priority = ["ethics", "benchmark", "cultural", "moral_psych", "religious", "llm"]

    nodes = []
    for norm in top_nodes_norms:
        stems = norm_to_papers[norm]

        # ── Primary dimension (most papers in that dimension) ──
        dim_counts = {d: 0 for d in dim_priority}
        for stem in stems:
            fn = stem + ".md" if not stem.endswith(".md") else stem
            fn_noext = stem.replace(".md", "") if stem.endswith(".md") else stem
            dims = paper_fn_to_dims.get(fn) or paper_fn_to_dims.get(fn_noext, {})
            for d in dim_priority:
                dim_counts[d] += dims.get(d, 0)
        # Pick max; ties broken by priority order
        primary_dim = max(dim_priority, key=lambda d: (dim_counts[d], -dim_priority.index(d)))
        if dim_counts[primary_dim] == 0:
            primary_dim = "ethics"  # fallback

        # ── Author role (first / last / middle) ──
        first_c = last_c = mid_c = 0
        for stem in stems:
            info = author_map.get(stem, {})
            authors = info.get("authors", [])
            author_norms = [_norm_author(a) for a in authors]
            if norm in author_norms:
                idx = author_norms.index(norm)
                if idx == 0:
                    first_c += 1
                elif idx == len(author_norms) - 1 and len(author_norms) > 1:
                    last_c += 1
                else:
                    mid_c += 1
        role_map = {"first": first_c, "last": last_c, "middle": mid_c}
        primary_role = max(role_map, key=role_map.get)

        # ── Primary venue type ──
        vt_counts = Counter()
        for stem in stems:
            fn = stem + ".md" if not stem.endswith(".md") else stem
            fn_noext = stem.replace(".md", "") if stem.endswith(".md") else stem
            p = papers_by_fn.get(fn) or papers_by_fn.get(fn_noext)
            if p:
                vt_counts[p["vt"]] += 1
        primary_vt = vt_counts.most_common(1)[0][0] if vt_counts else "N/A"

        # ── Average publication year ──
        years = [extract_year(s) for s in stems]
        valid_years = [y for y in years if y != 9999]
        avg_year = round(sum(valid_years) / len(valid_years), 1) if valid_years else 0

        # ── Unique co-authors count ──
        coauthor_set = set()
        for stem in stems:
            for co_norm in paper_to_norms.get(stem, []):
                if co_norm != norm:
                    coauthor_set.add(co_norm)

        nodes.append({
            "name": display[norm],
            "value": paper_count_per_author[norm],
            "symbolSize": min(5 + paper_count_per_author[norm] * 2, 40),
            "dim": primary_dim,
            "role": primary_role,
            "roleCt": role_map[primary_role],
            "vt": primary_vt,
            "avgY": avg_year,
            "coauthors": len(coauthor_set),
        })

    edges = []
    edge_set = set()
    for (a, b), c in pair_counter.most_common(500):
        if a in top_node_set and b in top_node_set:
            key = tuple(sorted([a, b]))
            if key not in edge_set:
                edge_set.add(key)
                edges.append({
                    "source": display[a],
                    "target": display[b],
                    "value": c,
                })
    # Cap edges at ~200 for performance
    edges = edges[:200]

    # Chord diagram data — top 30 authors with co-authorship matrix
    chord_norms = top30_norms[:30]
    chord_names = [display[n] for n in chord_norms]
    chord_norm_idx = {n: i for i, n in enumerate(chord_norms)}
    chord_matrix = [[0] * len(chord_norms) for _ in range(len(chord_norms))]
    for (a, b), c in pair_counter.items():
        if a in chord_norm_idx and b in chord_norm_idx:
            i, j = chord_norm_idx[a], chord_norm_idx[b]
            chord_matrix[i][j] = c
            chord_matrix[j][i] = c

    # Team composition donut (solo / 2 / 3-5 / 6-10 / 11+)
    team_buckets = Counter()
    for s in team_sizes:
        if s == 1:
            team_buckets["Solo"] += 1
        elif s == 2:
            team_buckets["Pair"] += 1
        elif s <= 5:
            team_buckets["3–5"] += 1
        elif s <= 10:
            team_buckets["6–10"] += 1
        else:
            team_buckets["11+"] += 1
    team_comp = [{"name": k, "value": v} for k, v in
                 [("Solo", team_buckets.get("Solo", 0)),
                  ("Pair", team_buckets.get("Pair", 0)),
                  ("3–5", team_buckets.get("3–5", 0)),
                  ("6–10", team_buckets.get("6–10", 0)),
                  ("11+", team_buckets.get("11+", 0))]]

    collab = {
        "coauthorPairs": coauthor_pairs,
        "networkNodes": nodes,
        "networkEdges": edges,
        "chordNames": chord_names,
        "chordMatrix": chord_matrix,
        "teamComp": team_comp,
    }

    # ── 3d: Diversity & Representation ────────────────────────────────────
    # AI Lab contributions — match lab keywords against affiliations + author text
    lab_keywords = {
        "OpenAI": ["openai"],
        "Google DeepMind": ["google", "deepmind", "google brain", "google research"],
        "Anthropic": ["anthropic"],
        "Meta AI": ["meta ai", "meta research", "facebook ai research"],
        "Microsoft Research": ["microsoft research", "microsoft"],
        "Mistral AI": ["mistral"],
        "DeepSeek": ["deepseek"],
        "NVIDIA": ["nvidia"],
        "Alibaba": ["alibaba", "damo academy", "qwen"],
        "Baidu": ["baidu"],
        "Tencent": ["tencent"],
        "Zhipu AI": ["zhipu", "chatglm"],
        "xAI": ["xai", "x.ai"],
        "01.AI": ["01.ai", "yi-"],
    }

    # Load affiliations if available
    affil_file = LOGS_DIR / "20260220-author_affiliations.json"
    affiliations = {}
    if affil_file.exists():
        affiliations = json.loads(affil_file.read_text(encoding="utf-8"))

    lab_paper_counts = Counter()
    for stem in author_map:
        affil_text = ""
        if stem in affiliations:
            affil_text = " ".join(affiliations[stem].get("affiliations", [])).lower()

        for lab, keywords in lab_keywords.items():
            if any(kw in affil_text for kw in keywords):
                lab_paper_counts[lab] += 1
                break  # One lab per paper to avoid double-counting

    lab_data = [{"n": lab, "c": lab_paper_counts.get(lab, 0)}
                for lab in lab_keywords if lab_paper_counts.get(lab, 0) > 0]
    lab_data.sort(key=lambda x: x["c"], reverse=True)

    # Lorenz curve + Gini coefficient
    sorted_counts = sorted(paper_count_per_author.values())
    n = len(sorted_counts)
    cum_sum = 0
    lorenz_x = [0.0]
    lorenz_y = [0.0]
    total_papers_authored = sum(sorted_counts)
    for i, c in enumerate(sorted_counts):
        cum_sum += c
        lorenz_x.append(round((i + 1) / n, 4))
        lorenz_y.append(round(cum_sum / total_papers_authored, 4))

    # Gini coefficient
    if n > 0 and total_papers_authored > 0:
        B = sum(lorenz_y) / (n + 1)
        gini = round(1 - 2 * B, 3)
    else:
        gini = 0

    # Sample Lorenz curve to ~50 points for JS
    step = max(1, len(lorenz_x) // 50)
    lorenz_x_sampled = lorenz_x[::step]
    lorenz_y_sampled = lorenz_y[::step]
    if lorenz_x_sampled[-1] != lorenz_x[-1]:
        lorenz_x_sampled.append(lorenz_x[-1])
        lorenz_y_sampled.append(lorenz_y[-1])

    diversity = {
        "aiLabs": lab_data,
        "gini": gini,
        "lorenzX": lorenz_x_sampled,
        "lorenzY": lorenz_y_sampled,
    }

    # ── 3e: Data Quality ──────────────────────────────────────────────────
    # Completeness: papers with full author list vs partial (et_al)
    has_full_authors = sum(1 for v in author_map.values()
                           if v.get("authors") and len(v["authors"]) > 0)
    has_et_al = sum(1 for v in author_map.values() if v.get("et_al_original"))
    has_et_al_resolved = sum(1 for v in author_map.values() if v.get("et_al_resolved"))
    missing_authors = len(author_map) - has_full_authors

    # Name forms: how many have abbreviated names (single initial)
    abbreviated_count = 0
    for norm, ctr in norm_to_display.items():
        best_name = ctr.most_common(1)[0][0]
        parts = best_name.split()
        if any(len(p) <= 2 and p.endswith(".") for p in parts):
            abbreviated_count += 1

    quality = {
        "totalPapers": len(author_map),
        "hasFullAuthors": has_full_authors,
        "missingAuthors": missing_authors,
        "etAlOriginal": has_et_al,
        "etAlResolved": has_et_al_resolved,
        "abbreviatedNames": abbreviated_count,
        "profileCount": profile_count,
        "enrichedCount": enriched_count,
        "uniqueAuthors": unique_count,
    }

    return {
        "overview": overview,
        "prolific": prolific,
        "collab": collab,
        "diversity": diversity,
        "quality": quality,
    }


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("CEI Literature Vault — Dashboard v7b Data Generator")
    print("=" * 60)

    # ── Load data sources ──────────────────────────────────────────────
    print("\n[1/8] Loading JSON data sources...")
    candidates = json.loads(CANDIDATES_FILE.read_text(encoding='utf-8'))
    normative_entries = json.loads(NORMATIVE_FILE.read_text(encoding='utf-8'))
    author_map = json.loads(AUTHOR_MAP_FILE.read_text(encoding='utf-8'))
    print(f"  Candidates: {len(candidates)}")
    print(f"  Normative entries: {len(normative_entries)}")
    print(f"  Author entries: {len(author_map)}")

    # ── Scan paper YAML ────────────────────────────────────────────────
    print("\n[2/8] Scanning paper YAML frontmatter...")
    paper_yaml = scan_all_paper_yaml()
    print(f"  Papers scanned: {len(paper_yaml)}")

    # ── Pre-compute candidate categories (shared by papers + agg) ─────
    print("\n[2b/8] Pre-computing candidate categories...")
    entry_cats = {}
    for e in candidates:
        cats = classify_entry(e)
        if not cats:
            full_text = " ".join([
                e.get("benchmark_name", ""),
                e.get("what_measures", ""),
                e.get("how_measures", ""),
                e.get("reasoning", ""),
            ]).lower()
            if any(w in full_text for w in ["trust", "reliab", "robust", "risk"]):
                cats = ["6. Safety & Red Teaming"]
            elif any(w in full_text for w in ["social", "norm", "stereotyp"]):
                cats = ["4. Fairness, Bias & Social Norms"]
            elif any(w in full_text for w in ["moral", "ethic"]):
                cats = ["1. Moral Reasoning & Ethical Judgment"]
            else:
                cats = ["4. Fairness, Bias & Social Norms"]
        entry_cats[e["filename"]] = [c.split(". ", 1)[1] for c in cats]
    print(f"  Candidates classified: {len(entry_cats)}")

    # ── Build per-paper array ──────────────────────────────────────────
    print("\n[3/8] Building per-paper data array...")
    papers = build_papers_array(paper_yaml, candidates, normative_entries, entry_cats)
    print(f"  Papers built: {len(papers)}")

    # ── Aggregated data ────────────────────────────────────────────────
    print("\n[4/8] Computing aggregated data...")
    candidates_set = {e["filename"] for e in candidates}
    agg = build_aggregated_data(papers, paper_yaml, candidates, author_map, entry_cats)
    print(f"  Total: {agg['total']}, Ethics: {agg['ethicsYes']}, "
          f"Cultures: {agg['cultureCount']}, Languages: {agg['languageCount']}")

    # ── Conference data ────────────────────────────────────────────────
    print("\n[5/8] Computing conference & venue data...")
    conf = build_conference_data(papers)
    print(f"  Unique venues: {conf['uniqueVenues']}, "
          f"Families: {len(conf['families'])}, "
          f"Journals: {len(conf['journals'])}")

    # ── Deep-dive sections ─────────────────────────────────────────────
    print("\n[6/8] Computing deep-dive sections...")
    normative = compute_normative_data(normative_entries, candidates, paper_yaml, candidates_set)
    print(f"  Normative: {len(normative['papers'])} papers, "
          f"VE={normative['ve']['count']}, DE={normative['de']['count']}, "
          f"CU={normative['cu']['count']}")

    moral_psych = compute_moral_psych_data(paper_yaml, candidates, candidates_set)
    print(f"  Moral psych: {moral_psych['paperCount']} papers, "
          f"MFT={moral_psych['mft']['count']}, "
          f"Schwartz={moral_psych['schwartz']['count']}")

    # ── Item 6: Normative × Moral Psych Bridge ──────────────────────
    print("  Computing normative × moral psych bridge...")
    bridge_norm_fws = {"VE": set(), "DE": set(), "CU": set()}
    for p in normative["ve"]["papers"]:
        bridge_norm_fws["VE"].add(p["fn"])
    for p in normative["de"]["papers"]:
        bridge_norm_fws["DE"].add(p["fn"])
    for p in normative["cu"]["papers"]:
        bridge_norm_fws["CU"].add(p["fn"])

    bridge_psych_fns = {}
    for p in moral_psych.get("papers", []):
        for th in p.get("th", []):
            bridge_psych_fns.setdefault(th, set()).add(p["fn"])

    # Heatmap: normative frameworks (Y) × moral psych theories (X)
    bridge_norm_labels = ["VE", "DE", "CU"]
    bridge_psych_labels = [m["abbrev"] for m in THEORY_META]
    bridge_matrix = []
    for nfw in bridge_norm_labels:
        row = []
        for pth in bridge_psych_labels:
            overlap_count = len(bridge_norm_fws.get(nfw, set()) & bridge_psych_fns.get(pth, set()))
            row.append(overlap_count)
        bridge_matrix.append(row)

    # Bridge papers (papers in BOTH normative and moral psych)
    all_norm_fns = bridge_norm_fws["VE"] | bridge_norm_fws["DE"] | bridge_norm_fws["CU"]
    all_psych_fns = set()
    for fns in bridge_psych_fns.values():
        all_psych_fns |= fns
    bridge_paper_fns = all_norm_fns & all_psych_fns
    bridge_papers = [{"fn": fn} for fn in sorted(bridge_paper_fns)]

    # Timeline: bridge papers by year
    bridge_year = Counter()
    for fn in bridge_paper_fns:
        y = extract_year(fn)
        if 2016 <= y <= 2026:
            bridge_year[y] += 1
    bridge_timeline_years = sorted(bridge_year.keys())
    bridge_timeline_data = [bridge_year[y] for y in bridge_timeline_years]

    normative["bridge"] = {
        "heatmap": {
            "xLabels": bridge_psych_labels,
            "yLabels": bridge_norm_labels,
            "matrix": bridge_matrix,
        },
        "papers": bridge_papers,
        "timeline": {
            "years": bridge_timeline_years,
            "data": bridge_timeline_data,
        },
        "count": len(bridge_paper_fns),
    }
    print(f"  Bridge: {len(bridge_paper_fns)} papers at normative × moral psych intersection")

    religious = compute_religious_data(paper_yaml, candidates, candidates_set)
    print(f"  Religious: {religious['paperCount']} papers, "
          f"Islamic={religious['islamic']['count']}, "
          f"Christianity={religious['christianity']['count']}, "
          f"Buddhism={religious['buddhism']['count']}")

    # ── Taxonomy & methods ─────────────────────────────────────────────
    print("\n[7/8] Computing taxonomy & LLM data...")
    taxonomy = compute_taxonomy_data(candidates, paper_yaml)
    print(f"  Categories: {len(taxonomy['categories'])}, "
          f"Models: {len(taxonomy['models'])}")

    cultural = compute_cultural_data(paper_yaml, papers)
    print(f"  Cultural papers: {cultural['paperCount']}, "
          f"Cultures: {cultural['cultureCount']}")

    llm_data = compute_llm_data(paper_yaml, candidates)
    print(f"  LLM models: {len(llm_data['llmModels'])}, "
          f"Model families: {len(llm_data['modelFamilies'])}")

    # ── Author data (v7b) ────────────────────────────────────────────
    print("\n[8/9] Computing author & collaboration data...")
    author_data = build_author_data(author_map, paper_yaml, papers)
    print(f"  Unique authors: {author_data['overview']['uniqueAuthors']}, "
          f"Prolific(3+): {author_data['overview']['prolific3']}, "
          f"Network nodes: {len(author_data['collab']['networkNodes'])}, "
          f"Edges: {len(author_data['collab']['networkEdges'])}")

    # ── Write data.js ──────────────────────────────────────────────────
    print("\n[9/9] Writing data.js...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    data_obj = {
        "generated": date.today().isoformat(),
        "papers": papers,
        "agg": agg,
        "conf": conf,
        "taxonomy": taxonomy,
        "cultural": cultural,
        "normative": normative,
        "moralPsych": moral_psych,
        "religious": religious,
        "llm": llm_data,
        "authors": author_data,
    }

    data_json = json.dumps(data_obj, ensure_ascii=False, separators=(',', ':'))
    js_content = f"// Generated {date.today().isoformat()} by generate_vault_dashboard_5b.py\n"
    js_content += f"const DATA = {data_json};\n"

    OUTPUT_FILE.write_text(js_content, encoding='utf-8')
    size_kb = OUTPUT_FILE.stat().st_size / 1024
    print(f"  Output: {OUTPUT_FILE}")
    print(f"  Size: {size_kb:.0f} KB")

    # ── Verification ───────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    print(f"  Total papers:     {len(papers)}")
    print(f"  Data.js size:     {size_kb:.0f} KB")
    print(f"  Papers with CONF: {sum(1 for p in papers if p['cc'] != 'N/A')}")
    print(f"  Papers with LLM:  {sum(1 for p in papers if p['lm'])}")
    print(f"  VE sub-section:   {normative['ve']['count']} papers (bench: {normative['ve']['benchmarkCount']})")
    print(f"  MFT sub-section:  {moral_psych['mft']['count']} papers")
    print(f"  Islamic sub:      {religious['islamic']['count']} papers (bench: {religious['islamic']['benchmarkCount']})")
    print(f"  Conference fams:  {len(conf['families'])}")
    print(f"  Unique authors:   {author_data['overview']['uniqueAuthors']}")
    print(f"  Author KPI:       {agg['authorCount']} (was broken as {len(author_map)})")
    print(f"  Network graph:    {len(author_data['collab']['networkNodes'])} nodes, "
          f"{len(author_data['collab']['networkEdges'])} edges")
    print(f"  Gini coefficient: {author_data['diversity']['gini']}")
    print("=" * 60)
    print("Done!")


if __name__ == "__main__":
    main()
