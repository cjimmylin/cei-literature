#!/usr/bin/env python3
"""
Generate data.js for CEI Literature Vault Dashboard v4.

Scans paper YAML frontmatter, benchmark survey JSON, normative v2 JSON,
and author map to produce a JavaScript data file consumed by the static
HTML/CSS/JS frontend.

Output: STATISTICS/cei-dashboard-4/data.js

Data sources:
  - papers/*.md YAML frontmatter (2,034 papers)
  - logs/20260216-benchmark_survey_all_classifications.json (2,002 entries)
  - logs/20260216-benchmark_survey_candidates.json (~989 entries)
  - logs/20260207-normative_v2_all_classifications.json (266 entries)
  - logs/20260208-author_paper_map.json (~9,800 entries)
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
AUTHOR_MAP_FILE = LOGS_DIR / "20260208-author_paper_map.json"
OUTPUT_DIR = STATS_DIR / "cei-dashboard-4"
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
    "Care/Harm": re.compile(r'care|harm|compassion|cruelty|suffer|protect|nurtur', re.I),
    "Fairness/Cheating": re.compile(r'fairness|cheat|justice|reciproc|equality|proportional', re.I),
    "Loyalty/Betrayal": re.compile(r'loyalty|betray|in[\s\-]?group|patriot|team|collectiv', re.I),
    "Authority/Subversion": re.compile(r'authority|subver|respect|hierarch|tradition|obedien', re.I),
    "Sanctity/Degradation": re.compile(r'sanctity|degrad|purity|disgust|sacred|contamina', re.I),
    "Liberty/Oppression": re.compile(r'liberty|oppress|freedom|tyrann|autonomy|coerci', re.I),
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


# ── Religious Tradition Patterns ──────────────────────────────────────────

TRADITION_META = [
    {"name": "Islam", "abbrev": "Islam", "color": "#22c55e"},
    {"name": "Christianity", "abbrev": "Christianity", "color": "#6366f1"},
    {"name": "Buddhism", "abbrev": "Buddhism", "color": "#f59e0b"},
    {"name": "Hinduism", "abbrev": "Hinduism", "color": "#ec4899"},
    {"name": "Confucian", "abbrev": "Confucian", "color": "#22d3ee"},
    {"name": "Judaism", "abbrev": "Judaism", "color": "#a855f7"},
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
    "Ubuntu": re.compile(r'ubuntu(?!.*(?:linux|operat))|african\s+ethic|african\s+moral', re.I),
    "Indigenous": re.compile(r'indigenous\s+(?:ethic|value|spirit|religi)|first\s+nation|shinto|aboriginal\s+(?:spirit|religi)|native\s+(?:american|spirit)', re.I),
}


def classify_relig_traditions(values_list, extra_text=""):
    combined = " ".join(values_list) + " " + extra_text if values_list else extra_text
    if not combined.strip():
        return []
    return [name for name, pat in RELIG_TRAD_PATTERNS.items() if pat.search(combined)]


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
# YAML SCANNER — Extended for v4
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
    """Scan all papers for extended YAML fields needed by v4 dashboard."""
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

    # Top authors
    author_counter = Counter()
    for stem, info in author_map.items():
        fa = info.get("first_author", "Unknown")
        author_counter[fa] += 1
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
        "authorCount": len(author_map),
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
    def build_fw_subsection(yaml_field, fw_code):
        sub_papers = []
        year_dist = Counter()
        model_counter = Counter()
        venue_counter = Counter()
        region_counter = Counter()
        theory_vs_emp = Counter()  # "Benchmark / Evaluation" vs "Theoretical / Framework"
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
            for c in (cultures if isinstance(cultures, list) else []):
                r = classify_region(c)
                region_counter[r] += 1

            # Theory vs Empirical
            if fn in cand_lookup:
                theory_vs_emp["Benchmark / Evaluation"] += 1
            else:
                theory_vs_emp["Theoretical / Framework"] += 1

            # FIX #1: return full paper objects, not just filenames
            sub_papers.append({
                "fn": fn,
                "y": year,
                "ib": 1 if fn in cand_lookup else 0,
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
            "theoryVsEmpirical": [{"n": n, "c": c} for n, c in theory_vs_emp.most_common()],
            "venueTypeDist": [{"n": n, "c": c} for n, c in venue_counter.most_common()],
            "regionDist": [{"n": n, "c": c} for n, c in region_counter.most_common()],
        }

    ve_data = build_fw_subsection('virtue_ethics', 'VE')

    # VE-specific: scan full abstracts for virtue keywords
    virtue_kw_counter = Counter()
    for fn, fields in paper_yaml.items():
        val = fields.get('virtue_ethics', '').lower()
        if val not in ('yes', 'partial', 'true'):
            continue
        title = fields.get("title", "") or fields.get("short_title", fn)
        abstract = fields.get("abstract", "")  # full abstract, not truncated
        for v in scan_virtue_keywords(title, abstract):
            virtue_kw_counter[v] += 1
    ve_data["virtueKeywords"] = [{"n": n, "c": c} for n, c in virtue_kw_counter.most_common()]

    de_data = build_fw_subsection('deontological_ethics', 'DE')

    # DE-specific: scan abstracts for deontological concept keywords
    deont_kw_counter = Counter()
    for fn, fields in paper_yaml.items():
        val = fields.get('deontological_ethics', '').lower()
        if val not in ('yes', 'partial', 'true'):
            continue
        title = fields.get("title", "") or fields.get("short_title", fn)
        abstract = fields.get("abstract", "")
        for concept in scan_deontology_keywords(title, abstract):
            deont_kw_counter[concept] += 1
    de_data["deontConcepts"] = [{"n": n, "c": c} for n, c in deont_kw_counter.most_common()]

    cu_data = build_fw_subsection('utilitarian_ethics', 'CU')

    # CU-specific: scan abstracts for consequentialist concept keywords
    cu_kw_counter = Counter()
    for fn, fields in paper_yaml.items():
        val = fields.get('utilitarian_ethics', '').lower()
        if val not in ('yes', 'partial', 'true'):
            continue
        title = fields.get("title", "") or fields.get("short_title", fn)
        abstract = fields.get("abstract", "")
        for concept in scan_cu_concepts(title, abstract):
            cu_kw_counter[concept] += 1
    cu_data["cuConcepts"] = [{"n": n, "c": c} for n, c in cu_kw_counter.most_common()]

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
    }


def compute_moral_psych_data(paper_yaml, candidates, candidates_set):
    """Compute moral psychology data with FIXED sub-sections."""
    cand_lookup = {e["filename"]: e for e in candidates}

    mp_papers = []
    paper_theories = {}
    theory_counter = Counter()
    theory_year = defaultdict(Counter)
    theory_paper_sets = defaultdict(set)
    benchmark_count = 0

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

        mp_papers.append({
            "fn": fn,
            "y": year if year != 9999 else 0,
            "th": theories,
            "ib": 1 if is_bench else 0,
            "bn": get_benchmark_name(cand, fields),
            "wm": get_what_measures(cand, fields),
            "lm": extract_model_families(combined_model_text)[:5],
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

    # MFT sub-section — FIXED: full paper objects
    mft_fns = theory_paper_sets.get("MFT", set())
    mft_papers = []
    mft_year = Counter()
    mft_model = Counter()
    mft_foundation_counts = Counter()
    mft_theory_vs_emp = Counter()
    mft_venue_counter = Counter()
    mft_region_counter = Counter()
    for fn in mft_fns:
        fields = paper_yaml.get(fn, {})
        cand = cand_lookup.get(fn, {})
        combined_model_text = get_models_text(cand, fields)
        year = extract_year(fn)
        if year != 9999:
            mft_year[year] += 1
        for m in extract_model_families(combined_model_text):
            mft_model[m] += 1
        # Detect foundations
        abstract = fields.get('abstract', '') or ''
        mp_val = fields.get('moral_psychology', '') or ''
        combined = f"{mp_val} {abstract}"
        for fnd_name, fnd_pat in MFT_FOUNDATION_PATTERNS.items():
            if fnd_pat.search(combined):
                mft_foundation_counts[fnd_name] += 1
        # Theory vs Empirical
        if fn in candidates_set:
            mft_theory_vs_emp["Benchmark / Evaluation"] += 1
        else:
            mft_theory_vs_emp["Theoretical / Framework"] += 1
        # Venue type
        conf_cc = fields.get("CONF-CC", "") or "N/A"
        vt = categorize_venue(conf_cc)
        mft_venue_counter[vt] += 1
        # Region
        cultures = fields.get("cultures_nationalities_list", [])
        for c in (cultures if isinstance(cultures, list) else []):
            r = classify_region(c)
            mft_region_counter[r] += 1
        mft_papers.append({
            "fn": fn,
            "y": year if year != 9999 else 0,
            "ib": 1 if fn in candidates_set else 0,
            "bn": get_benchmark_name(cand, fields),
            "wm": get_what_measures(cand, fields),
            "lm": extract_model_families(combined_model_text)[:5],
        })

    mft_data = {
        "papers": mft_papers,
        "count": len(mft_papers),
        "foundations": [{"n": f, "c": mft_foundation_counts.get(f, 0)} for f in MFT_FOUNDATIONS],
        "yearDist": {str(y): c for y, c in sorted(mft_year.items()) if y >= 2016},
        "topModels": [{"n": n, "c": c} for n, c in mft_model.most_common(10)],
        "theoryVsEmpirical": [{"n": n, "c": c} for n, c in mft_theory_vs_emp.most_common()],
        "venueTypeDist": [{"n": n, "c": c} for n, c in mft_venue_counter.most_common()],
        "regionDist": [{"n": n, "c": c} for n, c in mft_region_counter.most_common()],
    }

    # Schwartz sub-section — FIXED
    schwartz_fns = theory_paper_sets.get("Schwartz", set())
    schwartz_papers = []
    schwartz_year = Counter()
    schwartz_model = Counter()
    schwartz_theory_vs_emp = Counter()
    schwartz_venue_counter = Counter()
    schwartz_region_counter = Counter()
    schwartz_value_counts = Counter()
    for fn in schwartz_fns:
        fields = paper_yaml.get(fn, {})
        cand = cand_lookup.get(fn, {})
        combined_model_text = get_models_text(cand, fields)
        year = extract_year(fn)
        if year != 9999:
            schwartz_year[year] += 1
        for m in extract_model_families(combined_model_text):
            schwartz_model[m] += 1
        # Theory vs Empirical
        if fn in candidates_set:
            schwartz_theory_vs_emp["Benchmark / Evaluation"] += 1
        else:
            schwartz_theory_vs_emp["Theoretical / Framework"] += 1
        # Venue type
        conf_cc = fields.get("CONF-CC", "") or "N/A"
        vt = categorize_venue(conf_cc)
        schwartz_venue_counter[vt] += 1
        # Region
        cultures = fields.get("cultures_nationalities_list", [])
        for c in (cultures if isinstance(cultures, list) else []):
            r = classify_region(c)
            schwartz_region_counter[r] += 1
        # Schwartz value dimension extraction
        abstract = fields.get('abstract', '') or ''
        mp_val = fields.get('moral_psychology', '') or ''
        combined = f"{mp_val} {abstract}"
        for val_name, val_pat in SCHWARTZ_VALUE_PATTERNS.items():
            if val_pat.search(combined):
                schwartz_value_counts[val_name] += 1
        schwartz_papers.append({
            "fn": fn,
            "y": year if year != 9999 else 0,
            "ib": 1 if fn in candidates_set else 0,
            "bn": get_benchmark_name(cand, fields),
            "wm": get_what_measures(cand, fields),
            "lm": extract_model_families(combined_model_text)[:5],
        })

    schwartz_data = {
        "papers": schwartz_papers,
        "count": len(schwartz_papers),
        "yearDist": {str(y): c for y, c in sorted(schwartz_year.items()) if y >= 2016},
        "topModels": [{"n": n, "c": c} for n, c in schwartz_model.most_common(10)],
        "theoryVsEmpirical": [{"n": n, "c": c} for n, c in schwartz_theory_vs_emp.most_common()],
        "venueTypeDist": [{"n": n, "c": c} for n, c in schwartz_venue_counter.most_common()],
        "regionDist": [{"n": n, "c": c} for n, c in schwartz_region_counter.most_common()],
        "valueDims": [{"n": v, "c": schwartz_value_counts.get(v, 0)} for v in SCHWARTZ_VALUES],
    }

    # Developmental sub-section — FIXED
    dev_theories = ["Kohlberg", "Trolley"]
    dev_fns = set()
    for t in dev_theories:
        dev_fns |= theory_paper_sets.get(t, set())
    dev_papers = []
    dev_year = Counter()
    dev_model = Counter()
    sub_theory_counter = Counter()
    dev_theory_vs_emp = Counter()
    dev_venue_counter = Counter()
    dev_region_counter = Counter()
    for fn in dev_fns:
        fields = paper_yaml.get(fn, {})
        cand = cand_lookup.get(fn, {})
        combined_model_text = get_models_text(cand, fields)
        year = extract_year(fn)
        if year != 9999:
            dev_year[year] += 1
        for m in extract_model_families(combined_model_text):
            dev_model[m] += 1
        for t in dev_theories:
            if fn in theory_paper_sets.get(t, set()):
                sub_theory_counter[t] += 1
        # Theory vs Empirical
        if fn in candidates_set:
            dev_theory_vs_emp["Benchmark / Evaluation"] += 1
        else:
            dev_theory_vs_emp["Theoretical / Framework"] += 1
        # Venue type
        conf_cc = fields.get("CONF-CC", "") or "N/A"
        vt = categorize_venue(conf_cc)
        dev_venue_counter[vt] += 1
        # Region
        cultures = fields.get("cultures_nationalities_list", [])
        for c in (cultures if isinstance(cultures, list) else []):
            r = classify_region(c)
            dev_region_counter[r] += 1
        dev_papers.append({
            "fn": fn,
            "y": year if year != 9999 else 0,
            "ib": 1 if fn in candidates_set else 0,
            "bn": get_benchmark_name(cand, fields),
            "wm": get_what_measures(cand, fields),
            "lm": extract_model_families(combined_model_text)[:5],
        })

    developmental_data = {
        "papers": dev_papers,
        "count": len(dev_papers),
        "subTheories": [{"n": t, "c": sub_theory_counter.get(t, 0)} for t in dev_theories],
        "yearDist": {str(y): c for y, c in sorted(dev_year.items()) if y >= 2016},
        "topModels": [{"n": n, "c": c} for n, c in dev_model.most_common(10)],
        "theoryVsEmpirical": [{"n": n, "c": c} for n, c in dev_theory_vs_emp.most_common()],
        "venueTypeDist": [{"n": n, "c": c} for n, c in dev_venue_counter.most_common()],
        "regionDist": [{"n": n, "c": c} for n, c in dev_region_counter.most_common()],
    }

    # Timeline
    all_years = sorted(set(y for tc in theory_year.values() for y in tc.keys() if y >= 2016))
    timeline = {
        "years": all_years,
        "mft": [theory_year.get("MFT", Counter()).get(y, 0) for y in all_years],
        "schwartz": [theory_year.get("Schwartz", Counter()).get(y, 0) for y in all_years],
        "dev": [sum(theory_year.get(t, Counter()).get(y, 0) for t in dev_theories) for y in all_years],
    }

    # Cooccurrence
    abbrevs = [m["abbrev"] for m in THEORY_META]
    n = len(abbrevs)
    cooccurrence = [[0] * n for _ in range(n)]
    for fn, theories in paper_theories.items():
        indices = [abbrevs.index(t) for t in theories if t in abbrevs]
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
        "developmental": developmental_data,
        "cooccurrence": cooccurrence,
        "coLabels": abbrevs,
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
    christian_jewish_data = build_trad_subsection(["Christianity", "Judaism"])
    dharmic_data = build_trad_subsection(["Buddhism", "Hinduism"])
    confucian_data = build_trad_subsection(["Confucian"])
    ubuntu_indigenous_data = build_trad_subsection(["Ubuntu", "Indigenous"])

    # Timeline
    all_years = sorted(set(y for tc in tradition_year.values() for y in tc.keys() if y >= 2016))
    abrahamic = ["Islam", "Christianity", "Judaism"]
    dharmic_names = ["Buddhism", "Hinduism"]
    east_asian = ["Confucian"]
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
        "christianJewish": christian_jewish_data,
        "dharmic": dharmic_data,
        "confucian": confucian_data,
        "ubuntuIndigenous": ubuntu_indigenous_data,
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


def compute_cultural_data(paper_yaml):
    """Compute cultural values tab data."""
    culture_counter = Counter()
    region_counter = Counter()
    treemap_data = defaultdict(Counter)
    region_year = defaultdict(Counter)
    weird_counts = {"WEIRD": 0, "Non-WEIRD": 0, "Mixed": 0}
    lang_counter = Counter()
    paper_count = 0

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
        for c in cultures:
            culture_counter[c] += 1
            r = classify_region(c)
            region_counter[r] += 1
            treemap_data[r][c] += 1
            paper_regions.add(r)

        for r in paper_regions:
            if year > 0:
                region_year[r][year] += 1

        for lang in fields.get('languages_list', []):
            lang_counter[lang] += 1

    # Region distribution
    region_dist = [{"n": r, "c": c} for r, c in region_counter.most_common()]

    # Country distribution (top 30)
    country_dist = []
    for c, count in culture_counter.most_common(30):
        country_dist.append({"n": c, "c": count, "r": classify_region(c)})

    # Treemap
    treemap = []
    for r, cultures in sorted(treemap_data.items()):
        children = [{"n": c, "v": v} for c, v in cultures.most_common()]
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

    return {
        "paperCount": paper_count,
        "cultureCount": len(culture_counter),
        "regionDist": region_dist,
        "countryDist": country_dist,
        "treemap": treemap,
        "timeline": timeline,
        "weird": weird_counts,
        "langDist": lang_dist,
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
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("CEI Literature Vault — Dashboard v4 Data Generator")
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

    religious = compute_religious_data(paper_yaml, candidates, candidates_set)
    print(f"  Religious: {religious['paperCount']} papers, "
          f"Islamic={religious['islamic']['count']}, "
          f"Dharmic={religious['dharmic']['count']}")

    # ── Taxonomy & methods ─────────────────────────────────────────────
    print("\n[7/8] Computing taxonomy & LLM data...")
    taxonomy = compute_taxonomy_data(candidates, paper_yaml)
    print(f"  Categories: {len(taxonomy['categories'])}, "
          f"Models: {len(taxonomy['models'])}")

    cultural = compute_cultural_data(paper_yaml)
    print(f"  Cultural papers: {cultural['paperCount']}, "
          f"Cultures: {cultural['cultureCount']}")

    llm_data = compute_llm_data(paper_yaml, candidates)
    print(f"  LLM models: {len(llm_data['llmModels'])}, "
          f"Model families: {len(llm_data['modelFamilies'])}")

    # ── Write data.js ──────────────────────────────────────────────────
    print("\n[8/8] Writing data.js...")
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
    }

    data_json = json.dumps(data_obj, ensure_ascii=False, separators=(',', ':'))
    js_content = f"// Generated {date.today().isoformat()} by generate_vault_dashboard_4.py\n"
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
    print("=" * 60)
    print("Done!")


if __name__ == "__main__":
    main()
