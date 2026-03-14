#!/usr/bin/env python3
"""
Generate interactive vault dashboard v3 for LLM Ethics & Values Alignment.

Processes paper YAML, benchmark survey JSON, normative v2 JSON, and author map
to produce a single-page HTML dashboard with 8 tabs and 55 ECharts visualizations.

Data sources:
  - papers/*.md YAML frontmatter (2,034 papers)
  - logs/20260216-benchmark_survey_all_classifications.json (2,002 entries)
  - logs/20260216-benchmark_survey_candidates.json (~989 entries)
  - logs/20260207-normative_v2_all_classifications.json (266 entries)
  - logs/20260208-author_paper_map.json (~9,800 entries)

Template: DASHBOARDS/20260210-vault-dashboard-3.html (636KB)
Output:   DASHBOARDS/20260216-vault-dashboard-3.html
"""

import json
import re
import sys
import functools
from collections import defaultdict, Counter
from pathlib import Path
from datetime import date

sys.path.insert(0, str(Path(__file__).parent))
from religious_scoring import RV_FIELDS, FIELD_DISPLAY_NAMES, is_rv_detected

print = functools.partial(print, flush=True)

# ── Paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
LOGS_DIR = WS_ROOT / "logs"
STATS_DIR = WS_ROOT / "STATISTICS"
DASHBOARDS_DIR = WS_ROOT / "DASHBOARDS"
PAPERS_DIR = WS_ROOT / "papers"

CANDIDATES_FILE = LOGS_DIR / "20260216-benchmark_survey_candidates.json"
NORMATIVE_FILE = LOGS_DIR / "20260207-normative_v2_all_classifications.json"
AUTHOR_MAP_FILE = LOGS_DIR / "20260208-author_paper_map.json"
TEMPLATE_FILE = DASHBOARDS_DIR / "20260210-vault-dashboard-3.html"
OUTPUT_FILE = DASHBOARDS_DIR / "20260216-vault-dashboard-3.html"

# ── Import from existing scripts ──────────────────────────────────────────
sys.path.insert(0, str(SCRIPT_DIR))
from generate_benchmark_survey_report import CATEGORIES, classify_entry, extract_year


# ═══════════════════════════════════════════════════════════════════════════
# PATTERN DEFINITIONS (from generate_vault_dashboard.py)
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


METHODOLOGY_TYPES = {
    "Multiple-choice QA": r"multiple[\s\-]?choice|MCQ|multi[\s\-]?choice|forced[\s\-]?choice.*(?:question|answer)|choose.*(?:best|correct)|answer.*(?:selection|option)",
    "Scenario/vignette judgment": r"scenario|vignette|moral dilemma|trolley|ethical dilemma|thought experiment|situation",
    "Free-text generation": r"free[\s\-]?(?:text|form)|open[\s\-]?ended.*generat|text generation|natural language generation|generat.*(?:response|text|answer)",
    "Adversarial/red-teaming": r"adversarial|red[\s\-]?team|jailbreak|attack|prompt injection|bypass",
    "Classification task": r"classif(?:y|ication)|categori[zs]|label(?:ing|ed)|detect(?:ion|ing)|binary.*(?:classif|task)|sentiment.*classif",
    "Human preference/comparison": r"human.*prefer|prefer.*(?:pair|comparison|ranking)|crowdsourc.*(?:annotat|judgment|evaluat)|pairwise.*comparison|human.*judg|human.*evaluat",
    "Template/probing": r"template|prob(?:e|ing)|fill[\s\-]?in|cloze|mask(?:ed|ing)|counterfactual",
    "Likert/scale rating": r"likert|rating.*scale|scale.*(?:\d[\s\-]point|\d[\s\-]level)|numerical.*rating|score.*(?:1.*5|1.*7|1.*10)",
    "Multi-turn dialogue": r"multi[\s\-]?turn|dialogue|dialog|conversation|chat.*(?:based|eval|bench)",
    "Game/simulation": r"game|simulat|interactive.*(?:environ|scenar|platform)|reward.*(?:shaping|model.*game)",
    "Survey/questionnaire": r"survey|questionnaire|poll|world value survey|pew.*research|opinion.*(?:survey|poll)",
    "Embedding analysis": r"embedding.*(?:analy|bias|space|associat)|word.*(?:embedding|vector).*(?:bias|fair)|WEAT|SEAT|cosine.*(?:similar|bias)",
    "Crowdsourced annotation": r"crowdsourc|(?:amazon|mturk).*mechanical.*turk|annotator|annotation.*(?:task|pipeline)|inter[\s\-]?annotator",
    "Benchmark suite (multi-task)": r"benchmark.*suite|multi[\s\-]?task|(?:comprehensive|holistic|unified).*(?:bench|evaluat|framework)|suite.*(?:of|across).*task",
}
_METHODOLOGY_PATTERNS = {k: re.compile(v, re.IGNORECASE) for k, v in METHODOLOGY_TYPES.items()}


def extract_methodology_types(entry):
    text = " ".join([
        entry.get("how_measures", ""),
        entry.get("what_measures", ""),
        entry.get("reasoning", ""),
    ])
    if not text.strip():
        return []
    return [name for name, pat in _METHODOLOGY_PATTERNS.items() if pat.search(text)]


ETHICAL_TRADITIONS = {
    "Confucian": r"\bconfucian\b|\bconfucius\b|\bmencius\b|\brunren\b|\bli\b(?=.*ritual)|five.*(?:relationship|constant)",
    "Islamic": r"\bislam(?:ic)?\b|\bsharia\b|\bquran\b|\bhadith\b|\bfiqh\b|\bmaqasid\b|\bhalal\b|\bharam\b",
    "Buddhist": r"\bbuddhis[mt]\b|\bdharma\b|\bkarma\b|\bahimsa\b|\bfour.*noble.*truth",
    "Ubuntu": r"\bubuntu\b(?!.*(?:linux|operat))",
    "Hindu": r"\bhindu(?:ism)?\b|\bvedic\b|\bdharma\b|\bkarma\b",
    "Indigenous": r"\bindigenous\b|\bfirst.*nation\b|\baboriginal\b|\bnative.*(?:people|ethic|value)",
    "Virtue Ethics": r"\bvirtue.*ethic\b|\baristot(?:le|elian)\b|\beudaimonia\b|\bcharacter.*ethic\b|\bphronesis\b",
    "Deontological": r"\bdeontolog\b|\bkantian\b|\bcategorical.*imperative\b|\bduty[\s\-]?based\b",
    "Consequentialist": r"\bconsequential\b|\butilitarian\b|\bgreatest.*(?:good|happin)\b|\bwelfare.*maximiz",
    "Care Ethics": r"\bcare.*ethic\b|\bfeminist.*ethic\b|\bethic.*of.*care\b|\brelational.*ethic\b",
}
_TRADITION_PATTERNS = {k: re.compile(v, re.IGNORECASE) for k, v in ETHICAL_TRADITIONS.items()}


def extract_traditions(entry):
    text = " ".join([
        entry.get("what_measures", ""),
        entry.get("reasoning", ""),
        entry.get("benchmark_name", ""),
        entry.get("normative_frameworks", ""),
    ])
    if not text.strip():
        return []
    return [name for name, pat in _TRADITION_PATTERNS.items() if pat.search(text)]


LANGUAGES = {
    "English": r"\benglish\b",
    "Chinese": r"\bchinese\b|\bmandarin\b|\bcantonese\b",
    "Arabic": r"\barabic\b",
    "Korean": r"\bkorean\b",
    "Japanese": r"\bjapanese\b",
    "Hindi": r"\bhindi\b",
    "Spanish": r"\bspanish\b",
    "German": r"\bgerman\b",
    "French": r"\bfrench\b",
    "Turkish": r"\bturkish\b",
    "Indonesian": r"\bindonesian\b|\bmalay\b",
    "Portuguese": r"\bportuguese\b|\bbrazilian\b",
    "Russian": r"\brussian\b",
    "Vietnamese": r"\bvietnamese\b",
    "Thai": r"\bthai\b",
    "Swahili": r"\bswahili\b",
    "Urdu": r"\burdu\b",
    "Bengali": r"\bbengali\b|\bbangla\b",
    "Italian": r"\bitalian\b",
    "Dutch": r"\bdutch\b",
}
_LANGUAGE_PATTERNS = {k: re.compile(v, re.IGNORECASE) for k, v in LANGUAGES.items()}


def extract_languages(entry):
    text = " ".join([
        entry.get("what_measures", ""),
        entry.get("how_measures", ""),
        entry.get("reasoning", ""),
        entry.get("benchmark_name", ""),
    ])
    if not text.strip():
        return []
    return [name for name, pat in _LANGUAGE_PATTERNS.items() if pat.search(text)]


def parse_availability(val):
    v = (val or "N/A").strip()
    url = None
    url_match = re.search(r'(https?://[^\s\)]+)', v)
    if url_match:
        url = url_match.group(1).rstrip(".,;)")
    if v.startswith("Public"):
        return ("Public", url)
    if v.startswith("Code") or "code available" in v.lower():
        return ("Code available", url)
    if "not stated" in v.lower() or "not specified" in v.lower():
        return ("Not stated", url)
    if "not public" in v.lower():
        return ("Not public", url)
    if "partial" in v.lower():
        return ("Partially public", url)
    return ("Not stated", url)


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


# ═══════════════════════════════════════════════════════════════════════════
# EXTENDED YAML SCANNER
# ═══════════════════════════════════════════════════════════════════════════

YAML_SCALAR_FIELDS = {
    'moral_psychology', 'virtue_ethics', 'deontological_ethics',
    'utilitarian_ethics', 'religious_values', 'national_ethnic_cultural',
    'LLM_assessed', 'DATA_URL', 'ethics_overall', 'is_benchmark',
    'abstract', 'first_author',
} | set(RV_FIELDS)
YAML_LIST_FIELDS = {'cultures_nationalities_list', 'languages_list', 'religious_values_list'}


def scan_all_paper_yaml():
    """Scan all papers for extended YAML fields needed by v3 dashboard."""
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
                        # Inline value — might be comma-separated
                        items = [v.strip().strip('"').strip("'") for v in val.split(',')]
                        record[key] = [v for v in items if v and v.lower() not in ('n/a', 'na', 'none')]
                    else:
                        current_list_field = key
                elif key in YAML_SCALAR_FIELDS:
                    record[key] = val.strip('"').strip("'")

        results[p.name] = record
    return results


# ═══════════════════════════════════════════════════════════════════════════
# CULTURAL REGION MAPPING
# ═══════════════════════════════════════════════════════════════════════════

CULTURE_TO_REGION = {
    # East Asia
    "Chinese": "East Asia", "China": "East Asia", "Japanese": "East Asia",
    "Japan": "East Asia", "Korean": "East Asia", "Korea": "East Asia",
    "South Korean": "East Asia", "Taiwanese": "East Asia", "Taiwan": "East Asia",
    "Hong Kong": "East Asia", "Mongolian": "East Asia",
    # South Asia
    "Indian": "South Asia", "India": "South Asia", "Pakistani": "South Asia",
    "Pakistan": "South Asia", "Bangladeshi": "South Asia", "Bangladesh": "South Asia",
    "Sri Lankan": "South Asia", "Nepali": "South Asia", "Nepal": "South Asia",
    # Southeast Asia
    "Indonesian": "Southeast Asia", "Indonesia": "Southeast Asia",
    "Filipino": "Southeast Asia", "Philippines": "Southeast Asia",
    "Vietnamese": "Southeast Asia", "Vietnam": "Southeast Asia",
    "Thai": "Southeast Asia", "Thailand": "Southeast Asia",
    "Malaysian": "Southeast Asia", "Malaysia": "Southeast Asia",
    "Singaporean": "Southeast Asia", "Singapore": "Southeast Asia",
    "Burmese": "Southeast Asia", "Myanmar": "Southeast Asia",
    "Cambodian": "Southeast Asia", "Laotian": "Southeast Asia",
    # MENA
    "Arabic": "MENA", "Arab": "MENA", "Saudi": "MENA", "Saudi Arabian": "MENA",
    "Egyptian": "MENA", "Egypt": "MENA", "Iranian": "MENA", "Iran": "MENA",
    "Iraqi": "MENA", "Turkish": "MENA", "Turkey": "MENA",
    "Israeli": "MENA", "Israel": "MENA", "Palestinian": "MENA",
    "Lebanese": "MENA", "Jordanian": "MENA", "Emirati": "MENA", "UAE": "MENA",
    "Kuwaiti": "MENA", "Qatari": "MENA", "Bahraini": "MENA",
    "Omani": "MENA", "Yemeni": "MENA", "Syrian": "MENA",
    "Moroccan": "MENA", "Tunisian": "MENA", "Algerian": "MENA",
    "Libyan": "MENA", "Persian": "MENA",
    # Sub-Saharan Africa
    "African": "Sub-Saharan Africa", "Nigerian": "Sub-Saharan Africa",
    "Nigeria": "Sub-Saharan Africa", "Kenyan": "Sub-Saharan Africa",
    "South African": "Sub-Saharan Africa", "Ethiopian": "Sub-Saharan Africa",
    "Ghanaian": "Sub-Saharan Africa", "Tanzanian": "Sub-Saharan Africa",
    "Ugandan": "Sub-Saharan Africa", "Rwandan": "Sub-Saharan Africa",
    "Senegalese": "Sub-Saharan Africa", "Congolese": "Sub-Saharan Africa",
    "Zimbabwean": "Sub-Saharan Africa", "Cameroonian": "Sub-Saharan Africa",
    "Somali": "Sub-Saharan Africa", "Sudanese": "Sub-Saharan Africa",
    "Swahili": "Sub-Saharan Africa",
    # North America
    "American": "North America", "US": "North America", "USA": "North America",
    "United States": "North America", "Canadian": "North America", "Canada": "North America",
    # Western Europe
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
    # Eastern Europe
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
    # Latin America
    "Brazilian": "Latin America", "Brazil": "Latin America",
    "Mexican": "Latin America", "Mexico": "Latin America",
    "Argentine": "Latin America", "Argentina": "Latin America",
    "Colombian": "Latin America", "Peruvian": "Latin America",
    "Chilean": "Latin America", "Venezuelan": "Latin America",
    "Ecuadorian": "Latin America", "Bolivian": "Latin America",
    "Cuban": "Latin America", "Dominican": "Latin America",
    "Latin American": "Latin America", "Costa Rican": "Latin America",
    # Oceania
    "Australian": "Oceania", "Australia": "Oceania",
    "New Zealand": "Oceania", "New Zealander": "Oceania",
    # Central Asia
    "Kazakh": "Central Asia", "Uzbek": "Central Asia",
    "Kyrgyz": "Central Asia", "Tajik": "Central Asia",
    "Afghan": "Central Asia", "Afghanistan": "Central Asia",
    # Multi-Region
    "Western": "Multi-Region", "Eastern": "Multi-Region",
    "Global": "Multi-Region", "Multicultural": "Multi-Region",
    "Cross-cultural": "Multi-Region", "International": "Multi-Region",
    "Multilingual": "Multi-Region", "Diverse": "Multi-Region",
    "Multi-country": "Multi-Region", "Multi-national": "Multi-Region",
}

WEIRD_REGIONS = {"Western Europe", "North America", "Oceania"}
NON_WEIRD_REGIONS = {"East Asia", "South Asia", "Southeast Asia", "MENA",
                     "Sub-Saharan Africa", "Latin America", "Eastern Europe", "Central Asia"}


def classify_region(culture):
    """Map a culture/nationality name to a world region."""
    if not culture:
        return "Other"
    # Exact match
    if culture in CULTURE_TO_REGION:
        return CULTURE_TO_REGION[culture]
    # Case-insensitive fuzzy match
    culture_lower = culture.lower()
    for k, v in CULTURE_TO_REGION.items():
        if k.lower() == culture_lower:
            return v
        if k.lower() in culture_lower or culture_lower in k.lower():
            return v
    return "Other"


def classify_weird(region):
    """Classify a region as WEIRD, Non-WEIRD, or Mixed."""
    if region in WEIRD_REGIONS:
        return "WEIRD"
    if region in NON_WEIRD_REGIONS:
        return "Non-WEIRD"
    if region == "Multi-Region":
        return "Mixed"
    return "Non-WEIRD"


# ═══════════════════════════════════════════════════════════════════════════
# MORAL PSYCHOLOGY THEORY DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════

THEORY_META = [
    {"name": "Moral Foundations Theory", "abbrev": "MFT", "color": "#6366f1", "group": "foundations"},
    {"name": "Schwartz Value Theory", "abbrev": "Schwartz", "color": "#22d3ee", "group": "values"},
    {"name": "Kohlberg's Moral Development", "abbrev": "Kohlberg", "color": "#f59e0b", "group": "developmental"},
    {"name": "Trolley/Moral Dilemmas", "abbrev": "Trolley", "color": "#ec4899", "group": "dilemmas"},
    {"name": "Dual Process Theory", "abbrev": "DualProc", "color": "#22c55e", "group": "cognitive"},
    {"name": "Social Intuitionist Model", "abbrev": "SIM", "color": "#a855f7", "group": "cognitive"},
    {"name": "Dyadic Morality", "abbrev": "Dyadic", "color": "#f97316", "group": "cognitive"},
    {"name": "Moral Identity", "abbrev": "MoralID", "color": "#14b8a6", "group": "identity"},
]

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


def classify_theories(text):
    """Classify a text into moral psychology theories."""
    if not text or text.lower() in ('n/a', 'na', 'no', 'none', ''):
        return []
    return [abbrev for abbrev, pat in THEORY_PATTERNS.items() if pat.search(text)]


# ═══════════════════════════════════════════════════════════════════════════
# RELIGIOUS TRADITION DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════

TRADITION_META = [
    {"name": "Islam", "abbrev": "Islam", "color": "#22c55e", "group": "abrahamic"},
    {"name": "Christianity", "abbrev": "Christianity", "color": "#6366f1", "group": "abrahamic"},
    {"name": "Buddhism", "abbrev": "Buddhism", "color": "#f59e0b", "group": "dharmic"},
    {"name": "Hinduism", "abbrev": "Hinduism", "color": "#ec4899", "group": "dharmic"},
    {"name": "Confucian", "abbrev": "Confucian", "color": "#22d3ee", "group": "east_asian"},
    {"name": "Judaism", "abbrev": "Judaism", "color": "#a855f7", "group": "abrahamic"},
    {"name": "Ubuntu", "abbrev": "Ubuntu", "color": "#f97316", "group": "african_indigenous"},
    {"name": "Indigenous", "abbrev": "Indigenous", "color": "#14b8a6", "group": "african_indigenous"},
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


# Map rv_* field names → RELIG_TRAD_PATTERNS keys used by this dashboard
_RV_FIELD_TO_TRAD = {
    "rv_islam": "Islam", "rv_christianity": "Christianity", "rv_buddhism": "Buddhism",
    "rv_judaism": "Judaism", "rv_hinduism": "Hinduism", "rv_confucianism": "Confucian",
    "rv_ubuntu": "Ubuntu", "rv_indigenous": "Indigenous",
    # Fields with no matching key in RELIG_TRAD_PATTERNS for v3 are ignored:
    # rv_sikhism, rv_taoism, rv_shinto, rv_jainism, rv_bahai, rv_zoroastrianism
}


def _traditions_from_rv_scores(fields):
    """Return set of tradition names detected from rv_* score fields (>= 50)."""
    result = set()
    for rv_field, trad_name in _RV_FIELD_TO_TRAD.items():
        if is_rv_detected(fields.get(rv_field, 0)):
            result.add(trad_name)
    return result


def classify_relig_traditions(values_list, extra_text="", fields=None):
    """Classify religious traditions from legacy string fields + rv_* scores."""
    combined = " ".join(values_list) + " " + extra_text if values_list else extra_text
    result = set()
    if combined.strip():
        result = {name for name, pat in RELIG_TRAD_PATTERNS.items() if pat.search(combined)}
    # Also check rv_* score fields if provided
    if fields:
        result |= _traditions_from_rv_scores(fields)
    return list(result)


# ═══════════════════════════════════════════════════════════════════════════
# LANGUAGE FAMILY MAPPING
# ═══════════════════════════════════════════════════════════════════════════

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


# ═══════════════════════════════════════════════════════════════════════════
# COMPUTE: BASE DATA (14 keys, same structure as generate_vault_dashboard.py)
# ═══════════════════════════════════════════════════════════════════════════

def compute_base_data(paper_yaml, candidates, normative_entries, author_map):
    """Compute base dashboard data structures from raw inputs."""
    data = {}
    cat_order = sorted(CATEGORIES.keys(), key=lambda c: int(c.split(".")[0]))
    cat_short_names = [c.split(". ", 1)[1] for c in cat_order]

    # ── Classify all candidates ────────────────────────────────────────
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
            if any(w in full_text for w in ["trust", "reliab", "robust", "risk", "guardrail", "detect"]):
                cats = ["6. Safety & Red Teaming"]
            elif any(w in full_text for w in ["social", "norm", "stereotyp", "sentiment", "opinion", "survey"]):
                cats = ["4. Fairness, Bias & Social Norms"]
            elif any(w in full_text for w in ["moral", "ethic", "right", "wrong", "good", "bad", "virtue"]):
                cats = ["1. Moral Reasoning & Ethical Judgment"]
            elif any(w in full_text for w in ["generat", "model", "llm", "language model", "chatbot", "instruct", "benchmark", "evaluat"]):
                cats = ["10. Helpfulness, Honesty & RLHF"]
            else:
                cats = ["4. Fairness, Bias & Social Norms"]
        entry_cats[e["filename"]] = cats
        for c in cats:
            cat_entries[c].append(e)

    # ── KPIs ───────────────────────────────────────────────────────────
    total_papers = len(paper_yaml)

    plur_counts = Counter()
    for e in candidates:
        plur_counts[e.get("pluralistic_relevance", "N/A")] += 1
    plur_yes = plur_counts.get("Yes", 0)
    plur_partial = plur_counts.get("Partial", 0)
    plur_pct = round((plur_yes + plur_partial) / max(len(candidates), 1) * 100)

    avail_counts = Counter()
    for e in candidates:
        cat_label, _ = parse_availability(e.get("availability", ""))
        avail_counts[cat_label] += 1
    public_count = avail_counts.get("Public", 0)
    code_count = avail_counts.get("Code available", 0)

    norm_yes = sum(1 for e in normative_entries if e.get("decision") == "Yes")
    norm_border = sum(1 for e in normative_entries if e.get("decision") == "Borderline")

    data["kpi"] = {
        "total": total_papers,
        "candidates": len(candidates),
        "public": public_count,
        "code": code_count,
        "pluralisticPct": plur_pct,
        "normative": norm_yes + norm_border,
        "normativeYes": norm_yes,
        "normativeBorderline": norm_border,
        "authors": len(author_map),
    }

    # ── Timeline ───────────────────────────────────────────────────────
    timeline = defaultdict(lambda: {"all": 0, "cand": 0})
    for fn in paper_yaml:
        y = extract_year(fn)
        if y != 9999:
            timeline[y]["all"] += 1
    for e in candidates:
        y = extract_year(e["filename"])
        if y != 9999:
            timeline[y]["cand"] += 1
    data["timeline"] = {str(y): v for y, v in sorted(timeline.items()) if y >= 2016}

    # ── Categories ─────────────────────────────────────────────────────
    categories_data = []
    for i, cat in enumerate(cat_order):
        short = cat.split(". ", 1)[1]
        entries_in_cat = list({e["filename"] for e in cat_entries.get(cat, [])})
        by_year = Counter()
        for e in cat_entries.get(cat, []):
            y = extract_year(e["filename"])
            if y != 9999:
                by_year[y] += 1
        categories_data.append({
            "id": i + 1,
            "name": cat,
            "short": short,
            "count": len(entries_in_cat),
            "byYear": {str(y): c for y, c in sorted(by_year.items()) if y >= 2016},
        })
    data["categories"] = categories_data

    # ── Co-occurrence matrix ───────────────────────────────────────────
    n_cats = len(cat_order)
    cooccurrence = [[0] * n_cats for _ in range(n_cats)]
    for fn, cats in entry_cats.items():
        indices = []
        for c in cats:
            idx = next((i for i, co in enumerate(cat_order) if co == c), None)
            if idx is not None:
                indices.append(idx)
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                cooccurrence[indices[i]][indices[j]] += 1
                cooccurrence[indices[j]][indices[i]] += 1
    data["cooccurrence"] = cooccurrence

    # ── Models ─────────────────────────────────────────────────────────
    model_counter = Counter()
    model_by_cat = defaultdict(Counter)
    model_by_year = defaultdict(Counter)
    for e in candidates:
        fams = extract_model_families(e.get("models_evaluated", ""))
        cats = classify_entry(e) or ["Uncategorized"]
        yr = extract_year(e["filename"])
        for f in fams:
            model_counter[f] += 1
            if yr != 9999:
                model_by_year[f][yr] += 1
            for c in cats:
                sc = c.split(". ", 1)[1] if ". " in c else c
                model_by_cat[f][sc] += 1

    top_models = model_counter.most_common(20)
    models_data = []
    for name, count in top_models:
        by_cat = [model_by_cat[name].get(s, 0) for s in cat_short_names]
        by_year = {str(y): c for y, c in sorted(model_by_year[name].items()) if y >= 2016}
        models_data.append({"name": name, "count": count, "byCategory": by_cat, "byYear": by_year})
    data["models"] = models_data

    # ── Methods ────────────────────────────────────────────────────────
    method_counter = Counter()
    method_by_cat = defaultdict(Counter)
    for e in candidates:
        methods = extract_methodology_types(e)
        cats = classify_entry(e) or ["Uncategorized"]
        for m in methods:
            method_counter[m] += 1
            for c in cats:
                sc = c.split(". ", 1)[1] if ". " in c else c
                method_by_cat[m][sc] += 1

    methods_data = []
    for name, count in method_counter.most_common():
        by_cat = [method_by_cat[name].get(s, 0) for s in cat_short_names]
        methods_data.append({"name": name, "count": count, "byCategory": by_cat})
    data["methods"] = methods_data

    # ── Pluralistic ────────────────────────────────────────────────────
    data["pluralistic"] = {
        "Yes": plur_counts.get("Yes", 0),
        "Partial": plur_counts.get("Partial", 0),
        "No": plur_counts.get("No", 0),
    }

    # ── Ethical traditions ─────────────────────────────────────────────
    tradition_counter = Counter()
    for e in candidates:
        for t in extract_traditions(e):
            tradition_counter[t] += 1

    all_traditions = list(ETHICAL_TRADITIONS.keys())
    traditions_data = []
    for t in all_traditions:
        count = tradition_counter.get(t, 0)
        if count == 0:
            level = "Critical"
        elif count <= 3:
            level = "Severe"
        elif count <= 10:
            level = "Moderate"
        else:
            level = "Adequate"
        traditions_data.append({"name": t, "count": count, "level": level})
    traditions_data.sort(key=lambda x: -x["count"])
    data["traditions"] = traditions_data

    # ── Languages ──────────────────────────────────────────────────────
    lang_counter = Counter()
    lang_by_cat = defaultdict(Counter)
    for e in candidates:
        langs = extract_languages(e)
        cats = classify_entry(e) or ["Uncategorized"]
        for l in langs:
            lang_counter[l] += 1
            for c in cats:
                sc = c.split(". ", 1)[1] if ". " in c else c
                lang_by_cat[l][sc] += 1

    languages_data = []
    for name, count in lang_counter.most_common(20):
        by_cat = [lang_by_cat[name].get(s, 0) for s in cat_short_names]
        languages_data.append({"name": name, "count": count, "byCategory": by_cat})
    data["languages"] = languages_data

    # ── Availability ───────────────────────────────────────────────────
    data["availability"] = {
        "Public": avail_counts.get("Public", 0),
        "Code available": avail_counts.get("Code available", 0),
        "Not stated": avail_counts.get("Not stated", 0),
        "Partially public": avail_counts.get("Partially public", 0),
        "Not public": avail_counts.get("Not public", 0),
    }

    # ── Resources ──────────────────────────────────────────────────────
    resources = []
    for e in candidates:
        avail_cat, url = parse_availability(e.get("availability", ""))
        if avail_cat not in ("Public", "Code available", "Partially public"):
            continue
        year = extract_year(e["filename"])
        cats = entry_cats.get(e["filename"], [])
        primary_cat = cats[0].split(". ", 1)[1] if cats else "Other"
        resources.append({
            "filename": e["filename"].replace(".md", ""),
            "year": year,
            "benchmark": (e.get("benchmark_name", "N/A") or "N/A")[:60],
            "what": (e.get("what_measures", "N/A") or "N/A")[:80],
            "category": primary_cat,
            "availability": avail_cat,
            "url": url or "",
        })
    resources.sort(key=lambda x: (-x["year"], x["filename"].lower()))
    data["resources"] = resources

    # ── Top authors ────────────────────────────────────────────────────
    author_counter = Counter()
    for stem, info in author_map.items():
        fa = info.get("first_author", "Unknown")
        author_counter[fa] += 1
    data["topAuthors"] = [{"name": n, "count": c} for n, c in author_counter.most_common(15)]

    # ── Category short names ───────────────────────────────────────────
    data["categoryNames"] = cat_short_names

    # ── LLM Assessment data ────────────────────────────────────────────
    papers_with_models = {fn: d for fn, d in paper_yaml.items() if d.get("LLM_assessed", "NA") not in ("NA", "N/A", "", "na")}
    papers_with_urls = {fn: d for fn, d in paper_yaml.items() if d.get("DATA_URL", "NA") not in ("NA", "N/A", "", "na")}

    llm_model_counter = Counter()
    for fn, d in papers_with_models.items():
        for m in [m.strip() for m in d["LLM_assessed"].split(",") if m.strip()]:
            llm_model_counter[m] += 1
    data["llmModels"] = [{"name": n, "count": c} for n, c in llm_model_counter.most_common(20)]

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
    data["llmByYear"] = {str(y): {"assessed": assessed_by_year.get(y, 0),
                                   "notAssessed": not_assessed_by_year.get(y, 0)}
                         for y in all_years if y >= 2016}

    repo_counter = Counter()
    for fn, d in papers_with_urls.items():
        url = d["DATA_URL"].lower()
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
    data["repoDistribution"] = [{"name": n, "count": c} for n, c in repo_counter.most_common()]

    data["kpi"]["llmModels"] = len(papers_with_models)
    data["kpi"]["llmModelsPct"] = round(len(papers_with_models) / max(len(paper_yaml), 1) * 100)
    data["kpi"]["dataUrls"] = len(papers_with_urls)
    data["kpi"]["totalPapers"] = len(paper_yaml)

    return data


# ═══════════════════════════════════════════════════════════════════════════
# COMPUTE: CULTURAL VALUES (17 keys)
# ═══════════════════════════════════════════════════════════════════════════

def compute_cultural_data(paper_yaml, candidates, candidates_set):
    """Compute cultural values deep-dive section."""
    cultural_papers = []
    culture_counter = Counter()
    region_counter = Counter()
    treemap_data = defaultdict(Counter)
    region_year = defaultdict(Counter)
    religion_counter = Counter()
    framework_counter = Counter()
    lang_family_counter = Counter()
    all_regions_set = set()

    # Build candidate lookup for benchmark details
    cand_lookup = {e["filename"]: e for e in candidates}

    for fn, fields in paper_yaml.items():
        cultures = fields.get('cultures_nationalities_list', [])
        if not cultures:
            continue

        year = extract_year(fn)
        if year == 9999:
            year = 0
        primary_culture = cultures[0]
        primary_region = classify_region(primary_culture)
        religion = fields.get('religious_values', '') or ''

        cultural_papers.append({
            "filename": fn,
            "year": year,
            "culture": primary_culture,
            "region": primary_region,
            "religion": religion.strip('"').strip("'")[:60] if religion else "",
            "isBenchmark": fn in candidates_set,
        })

        # Aggregate all cultures for distributions
        paper_regions = set()
        for c in cultures:
            culture_counter[c] += 1
            r = classify_region(c)
            region_counter[r] += 1
            treemap_data[r][c] += 1
            paper_regions.add(r)
            all_regions_set.add(r)

        for r in paper_regions:
            if year > 0:
                region_year[r][year] += 1

        # Count religion mentions (legacy strings + rv_* scores)
        relig_val = fields.get('religious_values', '') or ''
        relig_list = fields.get('religious_values_list', [])
        trads = classify_relig_traditions(relig_list, relig_val, fields=fields)
        for t in trads:
            religion_counter[t] += 1

        # Count moral psychology frameworks used in cultural papers
        mp_val = fields.get('moral_psychology', '') or ''
        if mp_val and mp_val.lower() not in ('n/a', 'na', 'no', 'none', ''):
            theories = classify_theories(mp_val)
            for t in theories:
                framework_counter[t] += 1

        # Language family
        langs = fields.get('languages_list', [])
        for lang in langs:
            fam = classify_lang_family(lang)
            lang_family_counter[fam] += 1

    # ── Build output structures ────────────────────────────────────────
    paper_count = len(cultural_papers)
    culture_count = len(culture_counter)
    unique_langs = set()
    for fn, f in paper_yaml.items():
        if f.get('cultures_nationalities_list', []):
            unique_langs.update(f.get('languages_list', []))
    language_count = len(unique_langs)

    # regionDist
    region_dist = [{"name": r, "count": c} for r, c in region_counter.most_common()]

    # countryDist
    country_dist = []
    for c, count in culture_counter.most_common():
        r = classify_region(c)
        country_dist.append({"name": c, "count": count, "region": r})

    # treemap
    treemap = []
    for r, cultures in sorted(treemap_data.items()):
        children = [{"name": c, "value": v} for c, v in cultures.most_common()]
        treemap.append({"name": r, "children": children})

    # timeline (year × region)
    all_years = sorted(set(y for rc in region_year.values() for y in rc.keys()))
    all_years = [y for y in all_years if y >= 2016]
    all_regions = sorted(all_regions_set)
    timeline_series = {}
    for r in all_regions:
        timeline_series[r] = [region_year[r].get(y, 0) for y in all_years]
    timeline = {
        "years": all_years,
        "regions": all_regions,
        "series": timeline_series,
    }

    # weirdRatio
    weird = sum(1 for p in cultural_papers if classify_weird(p["region"]) == "WEIRD")
    non_weird = sum(1 for p in cultural_papers if classify_weird(p["region"]) == "Non-WEIRD")
    mixed = paper_count - weird - non_weird
    weird_ratio = {"weird": weird, "nonWeird": non_weird, "mixed": mixed}

    # religionDist
    religion_dist = [{"name": r, "count": c} for r, c in religion_counter.most_common()]

    # tradRegionMatrix — traditions × regions heatmap
    trad_names = [t["name"] for t in TRADITION_META]
    region_names_for_matrix = sorted(all_regions_set - {"Other"})
    if "Other" in all_regions_set:
        region_names_for_matrix.append("Other")
    trad_region_matrix = []
    # For each cultural paper, get its traditions and region
    paper_trad_region = []
    for fn, fields in paper_yaml.items():
        cultures = fields.get('cultures_nationalities_list', [])
        if not cultures:
            continue
        primary_region = classify_region(cultures[0])
        relig_list = fields.get('religious_values_list', [])
        relig_val = fields.get('religious_values', '') or ''
        trads = classify_relig_traditions(relig_list, relig_val, fields=fields)
        for t in trads:
            paper_trad_region.append((t, primary_region))

    for t_name in trad_names:
        row = []
        for r_name in region_names_for_matrix:
            count = sum(1 for t, r in paper_trad_region if t == t_name and r == r_name)
            row.append(count)
        trad_region_matrix.append(row)

    trad_region_labels = {
        "traditions": trad_names,
        "regions": region_names_for_matrix,
    }

    # frameworks — moral psychology frameworks in cultural papers
    frameworks = [{"name": n, "count": c} for n, c in framework_counter.most_common()]

    # regionRadar — paper counts per region (for radar chart)
    region_radar = [{"name": r, "value": c} for r, c in region_counter.most_common()]

    # langFamily — language family distribution
    lang_family = [{"name": n, "count": c} for n, c in lang_family_counter.most_common()]

    # Count unique traditions
    tradition_count = len([t for t in religion_counter if religion_counter[t] > 0])

    return {
        "culturalPapers": cultural_papers,
        "paperCount": paper_count,
        "cultureCount": culture_count,
        "languageCount": language_count,
        "traditionCount": tradition_count,
        "regionDist": region_dist,
        "countryDist": country_dist,
        "treemap": treemap,
        "timeline": timeline,
        "weirdRatio": weird_ratio,
        "religionDist": religion_dist,
        "tradRegionMatrix": trad_region_matrix,
        "tradRegionLabels": trad_region_labels,
        "frameworks": frameworks,
        "regionRadar": region_radar,
        "langFamily": lang_family,
        "narratives": {},  # filled later
    }


# ═══════════════════════════════════════════════════════════════════════════
# COMPUTE: EXPANDED NORMATIVE ETHICS (13 keys)
# ═══════════════════════════════════════════════════════════════════════════

def compute_normative_data(normative_entries, candidates, paper_yaml, candidates_set):
    """Compute expanded normative ethics section."""
    cand_lookup = {e["filename"]: e for e in candidates}

    # ── Normative v2 classification ────────────────────────────────────
    yes_entries = [e for e in normative_entries if e.get("decision") == "Yes"]
    border_entries = [e for e in normative_entries if e.get("decision") == "Borderline"]
    excluded_count = len(normative_entries) - len(yes_entries) - len(border_entries)

    # Framework distribution
    fw_counts = Counter()
    for e in yes_entries + border_entries:
        nf = e.get("normative_frameworks", "N/A")
        reasoning = e.get("reasoning", "")
        search_text = f"{nf} {reasoning}"
        if not nf or nf == "N/A":
            continue
        for fw_name, pat in NORMATIVE_FRAMEWORK_PATTERNS.items():
            if pat.search(search_text):
                fw_counts[fw_name] += 1
    frameworks = [{"name": n, "count": c} for n, c in fw_counts.most_common()]

    # Build normative papers list
    normative_papers_set = set()
    normative_papers = []
    for e in yes_entries + border_entries:
        fn = e.get("filename", "")
        normative_papers_set.add(fn)
        cand = cand_lookup.get(fn, {})
        # Detect framework codes
        paper_fws = []
        search_text = f"{e.get('normative_frameworks', '')} {e.get('reasoning', '')}"
        if NORMATIVE_FRAMEWORK_PATTERNS["Virtue Ethics"].search(search_text):
            paper_fws.append("VE")
        if NORMATIVE_FRAMEWORK_PATTERNS["Deontology/Kantian"].search(search_text):
            paper_fws.append("DE")
        if NORMATIVE_FRAMEWORK_PATTERNS["Consequentialism/Utilitarianism"].search(search_text):
            paper_fws.append("CU")
        normative_papers.append({
            "filename": fn,
            "year": extract_year(fn),
            "decision": e.get("decision", ""),
            "benchmarkName": (cand.get("benchmark_name", "") or e.get("benchmark_name", ""))[:60],
            "whatMeasures": (cand.get("what_measures", "") or e.get("what_measures", ""))[:80],
            "llmsTested": (cand.get("models_evaluated", "") or e.get("llms_tested", ""))[:60],
            "datasetSize": (e.get("dataset_size", "") or cand.get("dataset_size", ""))[:40],
            "keyFinding": (e.get("key_finding", "") or e.get("reasoning", ""))[:100],
            "availability": (cand.get("availability", "") or e.get("data_artifact", ""))[:60],
            "frameworks": paper_fws,
        })

    # Also include benchmark candidates with YAML normative flags
    for fn, fields in paper_yaml.items():
        if fn in normative_papers_set:
            continue
        ve = fields.get('virtue_ethics', '').lower()
        de = fields.get('deontological_ethics', '').lower()
        cu = fields.get('utilitarian_ethics', '').lower()
        has_normative = any(v in ('yes', 'partial', 'true') for v in [ve, de, cu])
        if has_normative and fn in candidates_set:
            cand = cand_lookup.get(fn, {})
            paper_fws = []
            if ve in ('yes', 'partial', 'true'):
                paper_fws.append("VE")
            if de in ('yes', 'partial', 'true'):
                paper_fws.append("DE")
            if cu in ('yes', 'partial', 'true'):
                paper_fws.append("CU")
            normative_papers_set.add(fn)
            normative_papers.append({
                "filename": fn,
                "year": extract_year(fn),
                "decision": "YAML",
                "benchmarkName": (cand.get("benchmark_name", ""))[:60],
                "whatMeasures": (cand.get("what_measures", ""))[:80],
                "llmsTested": (cand.get("models_evaluated", ""))[:60],
                "datasetSize": "",
                "keyFinding": "",
                "availability": (cand.get("availability", ""))[:60],
                "frameworks": paper_fws,
            })

    normative_papers.sort(key=lambda x: x["filename"])

    # ── VE / DE / CU sub-sections from YAML ────────────────────────────
    def build_fw_subsection(yaml_field, fw_code):
        papers = []
        year_dist = Counter()
        model_counter = Counter()
        for fn, fields in paper_yaml.items():
            val = fields.get(yaml_field, '').lower()
            if val in ('yes', 'partial', 'true'):
                year = extract_year(fn)
                papers.append(fn)
                if year != 9999:
                    year_dist[year] += 1
                # Get models from candidate if available
                if fn in cand_lookup:
                    for m in extract_model_families(cand_lookup[fn].get("models_evaluated", "")):
                        model_counter[m] += 1
        return {
            "papers": papers,
            "count": len(papers),
            "yearDist": {str(y): c for y, c in sorted(year_dist.items()) if y >= 2016},
            "topModels": [{"name": n, "count": c} for n, c in model_counter.most_common(10)],
        }

    ve_data = build_fw_subsection('virtue_ethics', 'VE')
    de_data = build_fw_subsection('deontological_ethics', 'DE')
    cu_data = build_fw_subsection('utilitarian_ethics', 'CU')

    # ── Overlap ────────────────────────────────────────────────────────
    ve_set = set(ve_data["papers"])
    de_set = set(de_data["papers"])
    cu_set = set(cu_data["papers"])
    overlap = {
        "ve_de": len(ve_set & de_set),
        "ve_cu": len(ve_set & cu_set),
        "de_cu": len(de_set & cu_set),
        "all_three": len(ve_set & de_set & cu_set),
    }

    # Overlap papers list (union of any two frameworks)
    overlap_fns = (ve_set & de_set) | (ve_set & cu_set) | (de_set & cu_set)
    overlap_papers = []
    for fn in sorted(overlap_fns):
        fws = []
        if fn in ve_set:
            fws.append("VE")
        if fn in de_set:
            fws.append("DE")
        if fn in cu_set:
            fws.append("CU")
        cand = cand_lookup.get(fn, {})
        overlap_papers.append({
            "filename": fn,
            "year": extract_year(fn),
            "decision": "overlap",
            "benchmarkName": (cand.get("benchmark_name", ""))[:60],
            "whatMeasures": (cand.get("what_measures", ""))[:80],
            "llmsTested": (cand.get("models_evaluated", ""))[:60],
            "datasetSize": "",
            "keyFinding": "",
            "availability": (cand.get("availability", ""))[:60],
            "frameworks": fws,
        })

    # ── Timeline by framework ──────────────────────────────────────────
    all_years = sorted(set(
        list(y for y in ve_data["yearDist"]) +
        list(y for y in de_data["yearDist"]) +
        list(y for y in cu_data["yearDist"])
    ))
    timeline_by_fw = {
        "years": [int(y) for y in all_years],
        "ve": [int(ve_data["yearDist"].get(y, 0)) for y in all_years],
        "de": [int(de_data["yearDist"].get(y, 0)) for y in all_years],
        "cu": [int(cu_data["yearDist"].get(y, 0)) for y in all_years],
    }

    # ── Model by framework ─────────────────────────────────────────────
    all_model_names = set()
    for sub in [ve_data, de_data, cu_data]:
        for m in sub["topModels"]:
            all_model_names.add(m["name"])
    ve_model_map = {m["name"]: m["count"] for m in ve_data["topModels"]}
    de_model_map = {m["name"]: m["count"] for m in de_data["topModels"]}
    cu_model_map = {m["name"]: m["count"] for m in cu_data["topModels"]}

    model_by_fw = []
    for name in sorted(all_model_names, key=lambda n: -(ve_model_map.get(n, 0) + de_model_map.get(n, 0) + cu_model_map.get(n, 0))):
        model_by_fw.append({
            "name": name,
            "ve": ve_model_map.get(name, 0),
            "de": de_model_map.get(name, 0),
            "cu": cu_model_map.get(name, 0),
        })
    model_by_fw = model_by_fw[:10]

    return {
        "yes": len(yes_entries),
        "borderline": len(border_entries),
        "excluded": excluded_count,
        "frameworks": frameworks,
        "papers": normative_papers,
        "virtueEthics": ve_data,
        "deontological": de_data,
        "consequentialism": cu_data,
        "overlap": overlap,
        "overlapPapers": overlap_papers,
        "timelineByFw": timeline_by_fw,
        "modelByFw": model_by_fw,
        "narratives": {},  # filled later
    }


# ═══════════════════════════════════════════════════════════════════════════
# COMPUTE: MORAL PSYCHOLOGY (14 keys)
# ═══════════════════════════════════════════════════════════════════════════

def compute_moral_psych_data(paper_yaml, candidates, candidates_set):
    """Compute moral psychology section."""
    cand_lookup = {e["filename"]: e for e in candidates}

    # Identify moral psychology papers
    mp_papers = []
    paper_theories = {}  # fn -> [theories]
    theory_counter = Counter()
    theory_year = defaultdict(Counter)
    theory_model_counter = defaultdict(Counter)
    benchmark_count = 0
    theory_paper_sets = defaultdict(set)

    for fn, fields in paper_yaml.items():
        mp_val = fields.get('moral_psychology', '') or ''
        abstract = fields.get('abstract', '') or ''
        combined_text = f"{mp_val} {abstract}"

        if mp_val.lower() in ('n/a', 'na', 'no', 'none', '', 'false'):
            continue

        theories = classify_theories(combined_text)
        if not theories:
            # If moral_psychology is set but no specific theory detected, check more broadly
            theories = classify_theories(mp_val)
            if not theories and mp_val.lower() not in ('yes', 'true'):
                theories = classify_theories(mp_val)

        # Include paper even if no specific theory detected (general moral psych)
        year = extract_year(fn)
        is_bench = fn in candidates_set
        if is_bench:
            benchmark_count += 1

        cand = cand_lookup.get(fn, {})
        mp_papers.append({
            "filename": fn,
            "year": year if year != 9999 else 0,
            "theories": theories,
            "isBenchmark": is_bench,
            "benchmarkName": (cand.get("benchmark_name", ""))[:60] if is_bench else "",
            "whatMeasures": (cand.get("what_measures", ""))[:80] if is_bench else "",
            "models": (cand.get("models_evaluated", ""))[:60] if is_bench else "",
            "availability": (cand.get("availability", ""))[:60] if is_bench else "",
        })

        paper_theories[fn] = theories
        for t in theories:
            theory_counter[t] += 1
            theory_paper_sets[t].add(fn)
            if year != 9999:
                theory_year[t][year] += 1
            if fn in cand_lookup:
                for m in extract_model_families(cand_lookup[fn].get("models_evaluated", "")):
                    theory_model_counter[t][m] += 1

    # ── theoryDist ─────────────────────────────────────────────────────
    theory_dist = []
    for meta in THEORY_META:
        abbrev = meta["abbrev"]
        theory_dist.append({
            "name": meta["name"],
            "abbrev": abbrev,
            "count": theory_counter.get(abbrev, 0),
            "color": meta["color"],
            "group": meta["group"],
        })

    theories_represented = sum(1 for td in theory_dist if td["count"] > 0)

    # ── MFT sub-section ────────────────────────────────────────────────
    mft_papers = [fn for fn in theory_paper_sets.get("MFT", set())]
    mft_year = Counter()
    mft_model = Counter()
    mft_foundation_counts = Counter()
    for fn in mft_papers:
        year = extract_year(fn)
        if year != 9999:
            mft_year[year] += 1
        if fn in cand_lookup:
            for m in extract_model_families(cand_lookup[fn].get("models_evaluated", "")):
                mft_model[m] += 1
        # Detect specific foundations
        abstract = paper_yaml.get(fn, {}).get('abstract', '') or ''
        mp_val = paper_yaml.get(fn, {}).get('moral_psychology', '') or ''
        combined = f"{mp_val} {abstract}"
        for fnd_name, fnd_pat in MFT_FOUNDATION_PATTERNS.items():
            if fnd_pat.search(combined):
                mft_foundation_counts[fnd_name] += 1

    mft_data = {
        "papers": mft_papers,
        "count": len(mft_papers),
        "foundations": [{"name": f, "count": mft_foundation_counts.get(f, 0)} for f in MFT_FOUNDATIONS],
        "yearDist": {str(y): c for y, c in sorted(mft_year.items()) if y >= 2016},
        "topModels": [{"name": n, "count": c} for n, c in mft_model.most_common(10)],
    }

    # ── Schwartz sub-section ───────────────────────────────────────────
    schwartz_papers = list(theory_paper_sets.get("Schwartz", set()))
    schwartz_year = Counter()
    schwartz_model = Counter()
    for fn in schwartz_papers:
        year = extract_year(fn)
        if year != 9999:
            schwartz_year[year] += 1
        if fn in cand_lookup:
            for m in extract_model_families(cand_lookup[fn].get("models_evaluated", "")):
                schwartz_model[m] += 1

    schwartz_data = {
        "papers": schwartz_papers,
        "count": len(schwartz_papers),
        "yearDist": {str(y): c for y, c in sorted(schwartz_year.items()) if y >= 2016},
        "topModels": [{"name": n, "count": c} for n, c in schwartz_model.most_common(10)],
    }

    # ── Developmental sub-section ──────────────────────────────────────
    dev_theories = ["Kohlberg", "Trolley"]
    dev_papers = set()
    for t in dev_theories:
        dev_papers |= theory_paper_sets.get(t, set())
    dev_papers = list(dev_papers)
    dev_year = Counter()
    dev_model = Counter()
    sub_theory_counter = Counter()
    for fn in dev_papers:
        year = extract_year(fn)
        if year != 9999:
            dev_year[year] += 1
        if fn in cand_lookup:
            for m in extract_model_families(cand_lookup[fn].get("models_evaluated", "")):
                dev_model[m] += 1
        for t in dev_theories:
            if fn in theory_paper_sets.get(t, set()):
                sub_theory_counter[t] += 1

    developmental_data = {
        "papers": dev_papers,
        "count": len(dev_papers),
        "subTheories": [{"name": t, "count": sub_theory_counter.get(t, 0)} for t in dev_theories],
        "yearDist": {str(y): c for y, c in sorted(dev_year.items()) if y >= 2016},
        "topModels": [{"name": n, "count": c} for n, c in dev_model.most_common(10)],
    }

    # ── Timeline ───────────────────────────────────────────────────────
    all_years = sorted(set(y for tc in theory_year.values() for y in tc.keys()))
    all_years = [y for y in all_years if y >= 2016]
    timeline = {
        "years": all_years,
        "series": {
            "foundations": [theory_year.get("MFT", Counter()).get(y, 0) for y in all_years],
            "values": [theory_year.get("Schwartz", Counter()).get(y, 0) for y in all_years],
            "developmental": [sum(theory_year.get(t, Counter()).get(y, 0) for t in dev_theories) for y in all_years],
        },
    }

    # ── Cooccurrence matrix ────────────────────────────────────────────
    abbrevs = [m["abbrev"] for m in THEORY_META]
    n = len(abbrevs)
    cooccurrence = [[0] * n for _ in range(n)]
    for fn, theories in paper_theories.items():
        indices = [abbrevs.index(t) for t in theories if t in abbrevs]
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                cooccurrence[indices[i]][indices[j]] += 1
                cooccurrence[indices[j]][indices[i]] += 1

    # ── Model by theory ────────────────────────────────────────────────
    all_model_names = set()
    for t_counter in theory_model_counter.values():
        all_model_names.update(t_counter.keys())
    model_by_theory = []
    for model_name in sorted(all_model_names, key=lambda n: -sum(theory_model_counter[t].get(n, 0) for t in abbrevs)):
        entry = {"name": model_name}
        for abbrev in abbrevs:
            entry[abbrev] = theory_model_counter[abbrev].get(model_name, 0)
        model_by_theory.append(entry)
    model_by_theory = model_by_theory[:10]

    # ── Gap theories ───────────────────────────────────────────────────
    gap_theories = [m["abbrev"] for m in THEORY_META if theory_counter.get(m["abbrev"], 0) == 0]

    return {
        "papers": mp_papers,
        "paperCount": len(mp_papers),
        "theoryDist": theory_dist,
        "timeline": timeline,
        "benchmarkCount": benchmark_count,
        "theoriesRepresented": theories_represented,
        "mft": mft_data,
        "schwartz": schwartz_data,
        "developmental": developmental_data,
        "cooccurrence": cooccurrence,
        "cooccurrenceLabels": abbrevs,
        "modelByTheory": model_by_theory,
        "gapTheories": gap_theories,
        "narratives": {},  # filled later
    }


# ═══════════════════════════════════════════════════════════════════════════
# COMPUTE: RELIGIOUS VALUES (15 keys)
# ═══════════════════════════════════════════════════════════════════════════

def compute_religious_data(paper_yaml, candidates, candidates_set):
    """Compute religious values section."""
    cand_lookup = {e["filename"]: e for e in candidates}

    # Identify religious papers
    relig_papers = []
    paper_traditions = {}
    tradition_counter = Counter()
    tradition_year = defaultdict(Counter)
    tradition_model_counter = defaultdict(Counter)
    tradition_paper_sets = defaultdict(set)
    benchmark_count = 0

    for fn, fields in paper_yaml.items():
        relig_list = fields.get('religious_values_list', [])
        relig_val = fields.get('religious_values', '') or ''

        # Check both legacy strings and rv_* scores
        has_rv_scores = any(is_rv_detected(fields.get(f, 0)) for f in RV_FIELDS)
        if not relig_list and not has_rv_scores and relig_val.lower() in ('n/a', 'na', 'no', 'none', '', 'false'):
            continue

        trads = classify_relig_traditions(relig_list, relig_val, fields=fields)
        if not trads:
            continue

        year = extract_year(fn)
        is_bench = fn in candidates_set
        if is_bench:
            benchmark_count += 1

        cand = cand_lookup.get(fn, {})
        relig_papers.append({
            "filename": fn,
            "year": year if year != 9999 else 0,
            "traditions": trads,
            "isBenchmark": is_bench,
            "benchmarkName": (cand.get("benchmark_name", ""))[:60] if is_bench else "",
            "whatMeasures": (cand.get("what_measures", ""))[:80] if is_bench else "",
            "models": (cand.get("models_evaluated", ""))[:60] if is_bench else "",
            "availability": (cand.get("availability", ""))[:60] if is_bench else "",
        })

        paper_traditions[fn] = trads
        for t in trads:
            tradition_counter[t] += 1
            tradition_paper_sets[t].add(fn)
            if year != 9999:
                tradition_year[t][year] += 1
            if fn in cand_lookup:
                for m in extract_model_families(cand_lookup[fn].get("models_evaluated", "")):
                    tradition_model_counter[t][m] += 1

    # ── traditionDist ──────────────────────────────────────────────────
    tradition_dist = []
    for meta in TRADITION_META:
        name = meta["name"]
        tradition_dist.append({
            "name": name,
            "abbrev": meta["abbrev"],
            "count": tradition_counter.get(name, 0),
            "color": meta["color"],
            "group": meta["group"],
        })

    traditions_represented = sum(1 for td in tradition_dist if td["count"] > 0)

    # ── Sub-sections ───────────────────────────────────────────────────
    def build_trad_subsection(trad_names):
        papers = set()
        for t in trad_names:
            papers |= tradition_paper_sets.get(t, set())
        papers = list(papers)
        year_dist = Counter()
        model_counter = Counter()
        for fn in papers:
            year = extract_year(fn)
            if year != 9999:
                year_dist[year] += 1
            if fn in cand_lookup:
                for m in extract_model_families(cand_lookup[fn].get("models_evaluated", "")):
                    model_counter[m] += 1
        return {
            "papers": papers,
            "count": len(papers),
            "yearDist": {str(y): c for y, c in sorted(year_dist.items()) if y >= 2016},
            "topModels": [{"name": n, "count": c} for n, c in model_counter.most_common(10)],
        }

    def build_trad_subsection_with_sub(trad_names):
        result = build_trad_subsection(trad_names)
        sub_trads = [{"name": t, "count": tradition_counter.get(t, 0)} for t in trad_names]
        result["subTraditions"] = sub_trads
        return result

    islamic_data = build_trad_subsection(["Islam"])
    christian_jewish_data = build_trad_subsection(["Christianity", "Judaism"])
    dharmic_data = build_trad_subsection_with_sub(["Buddhism", "Hinduism"])
    confucian_data = build_trad_subsection(["Confucian"])

    # ── Timeline ───────────────────────────────────────────────────────
    all_years = sorted(set(y for tc in tradition_year.values() for y in tc.keys()))
    all_years = [y for y in all_years if y >= 2016]

    abrahamic = ["Islam", "Christianity", "Judaism"]
    dharmic_names = ["Buddhism", "Hinduism"]
    east_asian = ["Confucian"]
    african_indigenous = ["Ubuntu", "Indigenous"]

    timeline = {
        "years": all_years,
        "series": {
            "abrahamic": [sum(tradition_year.get(t, Counter()).get(y, 0) for t in abrahamic) for y in all_years],
            "dharmic": [sum(tradition_year.get(t, Counter()).get(y, 0) for t in dharmic_names) for y in all_years],
            "east_asian": [sum(tradition_year.get(t, Counter()).get(y, 0) for t in east_asian) for y in all_years],
            "african_indigenous": [sum(tradition_year.get(t, Counter()).get(y, 0) for t in african_indigenous) for y in all_years],
        },
    }

    # ── Cooccurrence matrix ────────────────────────────────────────────
    trad_names = [m["name"] for m in TRADITION_META]
    n = len(trad_names)
    cooccurrence = [[0] * n for _ in range(n)]
    for fn, trads in paper_traditions.items():
        indices = [trad_names.index(t) for t in trads if t in trad_names]
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):
                cooccurrence[indices[i]][indices[j]] += 1
                cooccurrence[indices[j]][indices[i]] += 1

    # ── Model by tradition ─────────────────────────────────────────────
    all_model_names = set()
    for t_counter in tradition_model_counter.values():
        all_model_names.update(t_counter.keys())
    model_by_trad = []
    for model_name in sorted(all_model_names, key=lambda n: -sum(tradition_model_counter[t].get(n, 0) for t in trad_names)):
        entry = {"name": model_name}
        for t_name in trad_names:
            entry[t_name] = tradition_model_counter[t_name].get(model_name, 0)
        model_by_trad.append(entry)
    model_by_trad = model_by_trad[:10]

    # ── Gap traditions ─────────────────────────────────────────────────
    gap_traditions = [m["name"] for m in TRADITION_META if tradition_counter.get(m["name"], 0) == 0]

    return {
        "papers": relig_papers,
        "paperCount": len(relig_papers),
        "traditionDist": tradition_dist,
        "timeline": timeline,
        "benchmarkCount": benchmark_count,
        "traditionsRepresented": traditions_represented,
        "islamic": islamic_data,
        "christian_jewish": christian_jewish_data,
        "dharmic": dharmic_data,
        "confucian": confucian_data,
        "cooccurrence": cooccurrence,
        "cooccurrenceLabels": trad_names,
        "modelByTradition": model_by_trad,
        "gapTraditions": gap_traditions,
        "narratives": {},  # filled later
    }


# ═══════════════════════════════════════════════════════════════════════════
# NARRATIVES — Extract from old DATA and update counts
# ═══════════════════════════════════════════════════════════════════════════

def extract_old_data():
    """Extract the old DATA blob from the v3 template."""
    html = TEMPLATE_FILE.read_text(encoding='utf-8')

    # Find const DATA = { using brace counting
    start_marker = 'const DATA = '
    start_idx = html.index(start_marker)
    brace_start = html.index('{', start_idx)

    brace_count = 0
    end_idx = brace_start
    for j in range(brace_start, len(html)):
        if html[j] == '{':
            brace_count += 1
        elif html[j] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = j + 1
                break

    data_json_str = html[brace_start:end_idx]
    return json.loads(data_json_str)


def update_narrative_counts(narrative, old_counts, new_counts):
    """Update specific count values in narrative HTML string."""
    if not isinstance(narrative, str):
        return narrative
    result = narrative
    for old_val, new_val in zip(old_counts, new_counts):
        # Replace <strong>N</strong> patterns
        result = result.replace(f'<strong>{old_val}</strong>', f'<strong>{new_val}</strong>')
        # Replace bare number references like "N papers"
        result = result.replace(f'{old_val} papers', f'{new_val} papers')
        result = result.replace(f'{old_val} benchmarks', f'{new_val} benchmarks')
        result = result.replace(f'{old_val} studies', f'{new_val} studies')
    return result


def build_narratives(data, old_data):
    """Extract old narratives and update with new counts."""
    # Define count mappings: (old_value, new_value)
    total_old = str(old_data.get("kpi", {}).get("total", 924))
    total_new = str(data["kpi"]["total"])
    cand_old = str(old_data.get("kpi", {}).get("candidates", 528))
    cand_new = str(data["kpi"]["candidates"])

    # Cultural narratives
    cult_old = old_data.get("cultural", {})
    cult_new = data["cultural"]
    old_cult_counts = [
        str(cult_old.get("paperCount", 207)),
        str(cult_old.get("cultureCount", 28)),
        str(cult_old.get("languageCount", 18)),
        str(cult_old.get("traditionCount", 9)),
        total_old, cand_old,
    ]
    new_cult_counts = [
        str(cult_new["paperCount"]),
        str(cult_new["cultureCount"]),
        str(cult_new["languageCount"]),
        str(cult_new["traditionCount"]),
        total_new, cand_new,
    ]

    old_cult_narr = cult_old.get("narratives", {})
    if isinstance(old_cult_narr, dict):
        new_cult_narr = {}
        for k, v in old_cult_narr.items():
            if isinstance(v, str):
                new_cult_narr[k] = update_narrative_counts(v, old_cult_counts, new_cult_counts)
            elif isinstance(v, list):
                # best_practices / missing_cards: list of dicts with text fields
                new_list = []
                for item in v:
                    if isinstance(item, dict):
                        new_item = {}
                        for ik, iv in item.items():
                            if isinstance(iv, str):
                                new_item[ik] = update_narrative_counts(iv, old_cult_counts, new_cult_counts)
                            else:
                                new_item[ik] = iv
                        new_list.append(new_item)
                    else:
                        new_list.append(item)
                new_cult_narr[k] = new_list
            else:
                new_cult_narr[k] = v
        data["cultural"]["narratives"] = new_cult_narr
    else:
        data["cultural"]["narratives"] = old_cult_narr or {}

    # Moral Psychology narratives
    mp_old = old_data.get("moralPsych", {})
    mp_new = data["moralPsych"]
    old_mp_counts = [
        str(mp_old.get("paperCount", 124)),
        str(mp_old.get("benchmarkCount", 104)),
        total_old, cand_old,
    ]
    new_mp_counts = [
        str(mp_new["paperCount"]),
        str(mp_new["benchmarkCount"]),
        total_new, cand_new,
    ]

    old_mp_narr = mp_old.get("narratives", {})
    if isinstance(old_mp_narr, dict):
        new_mp_narr = {}
        for k, v in old_mp_narr.items():
            new_mp_narr[k] = update_narrative_counts(v, old_mp_counts, new_mp_counts) if isinstance(v, str) else v
        data["moralPsych"]["narratives"] = new_mp_narr
    else:
        data["moralPsych"]["narratives"] = old_mp_narr or {}

    # Religious narratives
    rel_old = old_data.get("religious", {})
    rel_new = data["religious"]
    old_rel_counts = [
        str(rel_old.get("paperCount", 52)),
        str(rel_old.get("benchmarkCount", 22)),
        total_old, cand_old,
    ]
    new_rel_counts = [
        str(rel_new["paperCount"]),
        str(rel_new["benchmarkCount"]),
        total_new, cand_new,
    ]

    old_rel_narr = rel_old.get("narratives", {})
    if isinstance(old_rel_narr, dict):
        new_rel_narr = {}
        for k, v in old_rel_narr.items():
            new_rel_narr[k] = update_narrative_counts(v, old_rel_counts, new_rel_counts) if isinstance(v, str) else v
        data["religious"]["narratives"] = new_rel_narr
    else:
        data["religious"]["narratives"] = old_rel_narr or {}

    # Normative narratives
    norm_old = old_data.get("normative", {})
    norm_new = data["normative"]
    old_norm_counts = [
        str(norm_old.get("yes", 7)),
        str(norm_old.get("borderline", 38)),
        str(len(norm_old.get("papers", []))),
        total_old, cand_old,
    ]
    new_norm_counts = [
        str(norm_new["yes"]),
        str(norm_new["borderline"]),
        str(len(norm_new["papers"])),
        total_new, cand_new,
    ]

    old_norm_narr = norm_old.get("narratives", {})
    if isinstance(old_norm_narr, dict):
        new_norm_narr = {}
        for k, v in old_norm_narr.items():
            new_norm_narr[k] = update_narrative_counts(v, old_norm_counts, new_norm_counts) if isinstance(v, str) else v
        data["normative"]["narratives"] = new_norm_narr
    else:
        data["normative"]["narratives"] = old_norm_narr or {}


# ═══════════════════════════════════════════════════════════════════════════
# TEMPLATE INJECTION
# ═══════════════════════════════════════════════════════════════════════════

def inject_data_into_template(data_dict):
    """Read v3 HTML template, replace DATA blob, write output."""
    print(f"  Reading template: {TEMPLATE_FILE.name}")
    html = TEMPLATE_FILE.read_text(encoding='utf-8')

    # Find const DATA = { ... } using brace counting (robust against nested braces)
    start_marker = 'const DATA = '
    start_idx = html.index(start_marker)
    brace_start = html.index('{', start_idx)

    brace_count = 0
    end_idx = brace_start
    for j in range(brace_start, len(html)):
        if html[j] == '{':
            brace_count += 1
        elif html[j] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = j + 1
                break

    # Find the semicolon after closing brace
    semi_idx = end_idx
    while semi_idx < len(html) and html[semi_idx] in ' \t\n':
        semi_idx += 1
    if semi_idx < len(html) and html[semi_idx] == ';':
        semi_idx += 1

    # Generate compact JSON
    data_json = json.dumps(data_dict, ensure_ascii=False, separators=(',', ':'))
    new_data_block = f'const DATA = {data_json};'

    html = html[:start_idx] + new_data_block + html[semi_idx:]

    # Update dates
    today = date.today().strftime("%Y-%m-%d")
    html = html.replace('Generated 2026-02-15', f'Generated {today}')
    html = html.replace('Generated 2026-02-10', f'Generated {today}')
    html = html.replace('generate_vault_dashboard.py', 'generate_vault_dashboard_3.py')

    # Write output
    print(f"  Writing output: {OUTPUT_FILE.name}")
    OUTPUT_FILE.write_text(html, encoding='utf-8')

    size_kb = OUTPUT_FILE.stat().st_size / 1024
    print(f"  Output size: {size_kb:.0f} KB")


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    print("=" * 60)
    print("CEI Literature Vault — Dashboard v3 Generator")
    print("=" * 60)

    # ── Load data sources ──────────────────────────────────────────────
    print("\n[1/7] Loading JSON data sources...")
    candidates = json.loads(CANDIDATES_FILE.read_text(encoding='utf-8'))
    normative_entries = json.loads(NORMATIVE_FILE.read_text(encoding='utf-8'))
    author_map = json.loads(AUTHOR_MAP_FILE.read_text(encoding='utf-8'))
    print(f"  Candidates: {len(candidates)}")
    print(f"  Normative entries: {len(normative_entries)}")
    print(f"  Author entries: {len(author_map)}")

    # ── Scan paper YAML ────────────────────────────────────────────────
    print("\n[2/7] Scanning paper YAML frontmatter...")
    paper_yaml = scan_all_paper_yaml()
    print(f"  Papers scanned: {len(paper_yaml)}")

    # ── Compute base data ──────────────────────────────────────────────
    print("\n[3/7] Computing base dashboard data...")
    data = compute_base_data(paper_yaml, candidates, normative_entries, author_map)
    print(f"  KPI: total={data['kpi']['total']}, candidates={data['kpi']['candidates']}, "
          f"public={data['kpi']['public']}, normative={data['kpi']['normative']}")

    # ── Compute cultural data ──────────────────────────────────────────
    print("\n[4/7] Computing cultural values data...")
    candidates_set = {e["filename"] for e in candidates}
    data["cultural"] = compute_cultural_data(paper_yaml, candidates, candidates_set)
    print(f"  Cultural papers: {data['cultural']['paperCount']}, "
          f"cultures: {data['cultural']['cultureCount']}, "
          f"regions: {len(data['cultural']['regionDist'])}")

    # ── Compute normative data ─────────────────────────────────────────
    print("\n[5/7] Computing expanded normative ethics data...")
    data["normative"] = compute_normative_data(normative_entries, candidates, paper_yaml, candidates_set)
    print(f"  Normative papers: {len(data['normative']['papers'])}, "
          f"VE={data['normative']['virtueEthics']['count']}, "
          f"DE={data['normative']['deontological']['count']}, "
          f"CU={data['normative']['consequentialism']['count']}")

    # ── Compute moral psychology data ──────────────────────────────────
    print("[5b/7] Computing moral psychology data...")
    data["moralPsych"] = compute_moral_psych_data(paper_yaml, candidates, candidates_set)
    print(f"  Moral psych papers: {data['moralPsych']['paperCount']}, "
          f"theories: {data['moralPsych']['theoriesRepresented']}")

    # ── Compute religious values data ──────────────────────────────────
    print("[5c/7] Computing religious values data...")
    data["religious"] = compute_religious_data(paper_yaml, candidates, candidates_set)
    print(f"  Religious papers: {data['religious']['paperCount']}, "
          f"traditions: {data['religious']['traditionsRepresented']}")

    # ── Build narratives ───────────────────────────────────────────────
    print("\n[6/7] Building narratives...")
    old_data = extract_old_data()
    build_narratives(data, old_data)
    print("  Narratives updated from template")

    # ── Inject into template ───────────────────────────────────────────
    print("\n[7/7] Injecting data into template...")
    inject_data_into_template(data)

    # ── Verification summary ───────────────────────────────────────────
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    print(f"  Total papers:     {data['kpi']['total']}")
    print(f"  Candidates:       {data['kpi']['candidates']}")
    print(f"  Cultural papers:  {data['cultural']['paperCount']}")
    print(f"  Moral psych:      {data['moralPsych']['paperCount']}")
    print(f"  Religious:        {data['religious']['paperCount']}")
    print(f"  Normative:        {len(data['normative']['papers'])}")
    print(f"  Resources:        {len(data['resources'])}")
    print(f"  Output file:      {OUTPUT_FILE}")
    print("=" * 60)
    print("Done!")


if __name__ == "__main__":
    main()
