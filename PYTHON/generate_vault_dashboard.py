#!/usr/bin/env python3
"""
Generate interactive vault dashboard for LLM Ethics & Values Alignment.

Processes existing JSON classification data to produce a single-page interactive
HTML dashboard with ECharts visualizations, filterable tables, and KPI cards.

Data sources:
  - logs/20260215-benchmark_survey_all_classifications.json
  - logs/20260215-benchmark_survey_candidates.json
  - logs/20260207-normative_v2_all_classifications.json (266 entries)
  - logs/20260208-author_paper_map.json
  - papers/*.md YAML frontmatter: LLM_assessed, DATA_URL fields

Output: DASHBOARDS/20260215-vault-dashboard.html
"""

import json
import re
import sys
import functools
from collections import defaultdict, Counter
from pathlib import Path

print = functools.partial(print, flush=True)

# ── Paths ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
WS_ROOT = SCRIPT_DIR.parent
LOGS_DIR = WS_ROOT / "logs"
STATS_DIR = WS_ROOT / "STATISTICS"
DASHBOARDS_DIR = WS_ROOT / "DASHBOARDS"

ALL_CLASSIFICATIONS_FILE = LOGS_DIR / "20260216-benchmark_survey_all_classifications.json"
CANDIDATES_FILE = LOGS_DIR / "20260216-benchmark_survey_candidates.json"
NORMATIVE_FILE = LOGS_DIR / "20260207-normative_v2_all_classifications.json"
AUTHOR_MAP_FILE = LOGS_DIR / "20260208-author_paper_map.json"
OUTPUT_FILE = DASHBOARDS_DIR / "20260216-vault-dashboard.html"

# ── Paper YAML scanner (for LLM assessment data) ─────────────────────────
PAPERS_DIR = WS_ROOT / "papers"


def scan_paper_yaml_fields():
    """Scan all papers for LLM_assessed and DATA_URL fields."""
    results = {}
    for p in sorted(PAPERS_DIR.glob("*.md")):
        content = p.read_text(encoding="utf-8")
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not fm_match:
            continue
        fm = fm_match.group(1)
        llm = "NA"
        url = "NA"
        for line in fm.split("\n"):
            if line.startswith("LLM_assessed:"):
                llm = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("DATA_URL:"):
                url = line.split(":", 1)[1].strip().strip('"')
        results[p.name] = {"LLM_assessed": llm, "DATA_URL": url}
    return results

# ── Import from existing scripts ───────────────────────────────────────────
sys.path.insert(0, str(SCRIPT_DIR))
from generate_benchmark_survey_report import CATEGORIES, classify_entry, extract_year

# ── Normalization engine (from generate_vault_overview_report.py) ──────────
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
# DATA COMPUTATION
# ═══════════════════════════════════════════════════════════════════════════

def compute_dashboard_data(all_entries, candidates, normative_entries, author_map, paper_yaml):
    """Compute all dashboard data structures from raw JSON inputs."""
    data = {}
    cat_order = sorted(CATEGORIES.keys(), key=lambda c: int(c.split(".")[0]))
    cat_short_names = []
    for c in cat_order:
        cat_short_names.append(c.split(". ", 1)[1])

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
    plur_counts = Counter()
    for e in candidates:
        plur_counts[e.get("pluralistic_relevance", "N/A")] += 1
    plur_yes = plur_counts.get("Yes", 0)
    plur_partial = plur_counts.get("Partial", 0)
    plur_pct = round((plur_yes + plur_partial) / len(candidates) * 100)

    avail_counts = Counter()
    for e in candidates:
        cat_label, _ = parse_availability(e.get("availability", ""))
        avail_counts[cat_label] += 1
    public_count = avail_counts.get("Public", 0)
    code_count = avail_counts.get("Code available", 0)

    norm_yes = sum(1 for e in normative_entries if e.get("decision") == "Yes")
    norm_border = sum(1 for e in normative_entries if e.get("decision") == "Borderline")

    data["kpi"] = {
        "total": len(all_entries),
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
    for e in all_entries:
        y = extract_year(e["filename"])
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
    model_by_cat = defaultdict(lambda: Counter())
    model_by_year = defaultdict(lambda: Counter())
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
    method_by_cat = defaultdict(lambda: Counter())
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
    lang_by_cat = defaultdict(lambda: Counter())
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

    # ── Normative ──────────────────────────────────────────────────────
    yes_entries = [e for e in normative_entries if e.get("decision") == "Yes"]
    border_entries = [e for e in normative_entries if e.get("decision") == "Borderline"]

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

    frameworks_data = [{"name": n, "count": c} for n, c in fw_counts.most_common()]

    normative_papers = []
    for e in sorted(yes_entries, key=lambda x: x["filename"]):
        normative_papers.append({
            "filename": e["filename"],
            "frameworks": (e.get("normative_frameworks", "N/A") or "N/A")[:80],
            "llms": (e.get("llms_tested", "N/A") or "N/A")[:60],
            "artifact": (e.get("data_artifact", "N/A") or "N/A")[:80],
        })

    data["normative"] = {
        "yes": norm_yes,
        "borderline": norm_border,
        "excluded": len(normative_entries) - norm_yes - norm_border,
        "frameworks": frameworks_data,
        "papers": normative_papers,
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

    # ── Category short names for charts ────────────────────────────────
    data["categoryNames"] = cat_short_names

    # ── LLM Assessment data ───────────────────────────────────────────
    papers_with_models = {fn: d for fn, d in paper_yaml.items() if d["LLM_assessed"] != "NA"}
    papers_with_urls = {fn: d for fn, d in paper_yaml.items() if d["DATA_URL"] != "NA"}

    # Model frequency counts
    llm_model_counter = Counter()
    for fn, d in papers_with_models.items():
        for m in [m.strip() for m in d["LLM_assessed"].split(",") if m.strip()]:
            llm_model_counter[m] += 1

    data["llmModels"] = [{"name": n, "count": c} for n, c in llm_model_counter.most_common(20)]

    # Assessment by year
    assessed_by_year = Counter()
    not_assessed_by_year = Counter()
    for fn, d in paper_yaml.items():
        year = extract_year(fn)
        if year == 9999:
            continue
        if d["LLM_assessed"] != "NA":
            assessed_by_year[year] += 1
        else:
            not_assessed_by_year[year] += 1
    all_years = sorted(set(list(assessed_by_year.keys()) + list(not_assessed_by_year.keys())))
    data["llmByYear"] = {str(y): {"assessed": assessed_by_year.get(y, 0),
                                   "notAssessed": not_assessed_by_year.get(y, 0)}
                         for y in all_years if y >= 2016}

    # Data repository distribution
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

    # KPI for LLM tab
    data["kpi"]["llmModels"] = len(papers_with_models)
    data["kpi"]["llmModelsPct"] = round(len(papers_with_models) / len(paper_yaml) * 100) if paper_yaml else 0
    data["kpi"]["dataUrls"] = len(papers_with_urls)
    data["kpi"]["totalPapers"] = len(paper_yaml)

    return data


# ═══════════════════════════════════════════════════════════════════════════
# HTML TEMPLATE
# ═══════════════════════════════════════════════════════════════════════════

def build_html(data_json):
    """Build the complete HTML dashboard."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CEI Literature Vault — LLM Ethics Dashboard</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.1/dist/echarts.min.js"></script>
<style>
/* ── CSS Reset & Custom Properties ─────────────────────────────────── */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
:root {{
  --bg-primary: #09090b;
  --bg-card: #18181b;
  --bg-card-hover: #27272a;
  --bg-surface: #111113;
  --border: #3f3f46;
  --border-subtle: #27272a;
  --text-primary: #fafafa;
  --text-secondary: #a1a1aa;
  --text-muted: #71717a;
  --accent: #6366f1;
  --accent-light: #818cf8;
  --accent-dim: rgba(99,102,241,0.15);
  --success: #22c55e;
  --warning: #f59e0b;
  --danger: #ef4444;
  --cat-1: #6366f1; --cat-2: #22d3ee; --cat-3: #f59e0b;
  --cat-4: #ec4899; --cat-5: #22c55e; --cat-6: #a855f7;
  --cat-7: #f97316; --cat-8: #14b8a6; --cat-9: #e879f9;
  --cat-10: #38bdf8;
  --radius: 12px;
  --radius-sm: 8px;
  --font-sans: 'Inter', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', 'SF Mono', monospace;
}}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: var(--font-sans);
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  min-height: 100vh;
}}
/* ── Header ────────────────────────────────────────────────────────── */
.header {{
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border-subtle);
  padding: 20px 24px 0;
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(12px);
}}
.header-content {{
  max-width: 1400px;
  margin: 0 auto;
}}
.header h1 {{
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 4px;
}}
.header .subtitle {{
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 16px;
}}
/* ── Tabs ──────────────────────────────────────────────────────────── */
.tabs {{
  display: flex;
  gap: 0;
  overflow-x: auto;
  scrollbar-width: none;
}}
.tabs::-webkit-scrollbar {{ display: none; }}
.tab {{
  padding: 10px 20px;
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--text-muted);
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: all 0.2s;
  white-space: nowrap;
  user-select: none;
}}
.tab:hover {{ color: var(--text-secondary); }}
.tab.active {{
  color: var(--accent-light);
  border-bottom-color: var(--accent);
}}
/* ── Main ──────────────────────────────────────────────────────────── */
.main {{
  max-width: 1400px;
  margin: 0 auto;
  padding: 24px;
}}
.section {{
  display: none;
  animation: fadeIn 0.3s ease;
}}
.section.active {{ display: block; }}
@keyframes fadeIn {{
  from {{ opacity: 0; transform: translateY(8px); }}
  to {{ opacity: 1; transform: translateY(0); }}
}}
/* ── Grid ──────────────────────────────────────────────────────────── */
.grid {{ display: grid; gap: 20px; }}
.grid-2 {{ grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); }}
.grid-5 {{ grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); }}
@media (max-width: 768px) {{
  .grid-2, .grid-5 {{ grid-template-columns: 1fr; }}
}}
/* ── Cards ─────────────────────────────────────────────────────────── */
.card {{
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius);
  padding: 20px;
  transition: border-color 0.2s;
}}
.card:hover {{ border-color: var(--border); }}
.card-title {{
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 12px;
}}
/* ── KPI Cards ─────────────────────────────────────────────────────── */
.kpi {{
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius);
  padding: 20px 24px;
  position: relative;
  overflow: hidden;
}}
.kpi::before {{
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: var(--accent);
}}
.kpi-value {{
  font-family: var(--font-mono);
  font-size: 2rem;
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1.2;
}}
.kpi-label {{
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 4px;
}}
.kpi:nth-child(2)::before {{ background: var(--cat-2); }}
.kpi:nth-child(3)::before {{ background: var(--success); }}
.kpi:nth-child(4)::before {{ background: var(--cat-3); }}
.kpi:nth-child(5)::before {{ background: var(--cat-6); }}
.kpi:nth-child(6)::before {{ background: var(--cat-2); }}
/* ── Chart containers ──────────────────────────────────────────────── */
.chart-box {{
  width: 100%;
  height: 400px;
}}
.chart-box-sm {{ height: 320px; }}
.chart-box-lg {{ height: 500px; }}
.chart-box-xl {{ height: 600px; }}
/* ── Table ─────────────────────────────────────────────────────────── */
.table-wrap {{
  overflow-x: auto;
  border-radius: var(--radius);
  border: 1px solid var(--border-subtle);
}}
table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
}}
th {{
  background: var(--bg-card);
  color: var(--text-secondary);
  font-weight: 500;
  text-align: left;
  padding: 10px 14px;
  border-bottom: 1px solid var(--border);
  position: sticky;
  top: 0;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}}
th:hover {{ color: var(--text-primary); }}
td {{
  padding: 8px 14px;
  border-bottom: 1px solid var(--border-subtle);
  color: var(--text-secondary);
  max-width: 320px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}}
tr:hover td {{ background: var(--bg-card-hover); }}
tr:nth-child(even) td {{ background: rgba(24,24,27,0.5); }}
tr:nth-child(even):hover td {{ background: var(--bg-card-hover); }}
/* ── Filters ───────────────────────────────────────────────────────── */
.filters {{
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  align-items: center;
  margin-bottom: 16px;
}}
.filter-input {{
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  color: var(--text-primary);
  padding: 8px 14px;
  font-size: 0.82rem;
  font-family: var(--font-sans);
  outline: none;
  transition: border-color 0.2s;
  min-width: 200px;
}}
.filter-input:focus {{ border-color: var(--accent); }}
select.filter-input {{ cursor: pointer; }}
.filter-count {{
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-left: auto;
}}
/* ── Pagination ────────────────────────────────────────────────────── */
.pagination {{
  display: flex;
  gap: 4px;
  justify-content: center;
  margin-top: 16px;
  align-items: center;
}}
.page-btn {{
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 6px;
  color: var(--text-secondary);
  padding: 6px 12px;
  font-size: 0.78rem;
  cursor: pointer;
  transition: all 0.2s;
}}
.page-btn:hover {{ border-color: var(--border); color: var(--text-primary); }}
.page-btn.active {{
  background: var(--accent);
  border-color: var(--accent);
  color: white;
}}
.page-btn:disabled {{ opacity: 0.3; cursor: default; }}
/* ── Normative cards ───────────────────────────────────────────────── */
.norm-card {{
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius);
  padding: 16px 20px;
  margin-bottom: 12px;
}}
.norm-card h4 {{
  font-size: 0.85rem;
  color: var(--accent-light);
  margin-bottom: 8px;
  word-break: break-word;
}}
.norm-card .meta {{
  font-size: 0.78rem;
  color: var(--text-muted);
  line-height: 1.6;
}}
.norm-card .meta span {{
  color: var(--text-secondary);
}}
/* ── Badge ─────────────────────────────────────────────────────────── */
.badge {{
  display: inline-block;
  font-size: 0.7rem;
  padding: 2px 8px;
  border-radius: 99px;
  font-weight: 500;
}}
.badge-public {{ background: rgba(34,197,94,0.15); color: var(--success); }}
.badge-code {{ background: rgba(99,102,241,0.15); color: var(--accent-light); }}
.badge-partial {{ background: rgba(245,158,11,0.15); color: var(--warning); }}
/* ── Footer ────────────────────────────────────────────────────────── */
.footer {{
  text-align: center;
  padding: 32px 24px;
  font-size: 0.75rem;
  color: var(--text-muted);
  border-top: 1px solid var(--border-subtle);
  margin-top: 48px;
}}
</style>
</head>
<body>

<!-- ── Header & Tabs ────────────────────────────────────────────────── -->
<div class="header">
  <div class="header-content">
    <h1>CEI Literature Vault — LLM Ethics & Values Alignment</h1>
    <div class="subtitle" id="subtitle">Loading...</div>
    <div class="tabs" id="tabs">
      <div class="tab active" data-tab="overview">Overview</div>
      <div class="tab" data-tab="taxonomy">Taxonomy</div>
      <div class="tab" data-tab="models">Models & Methods</div>
      <div class="tab" data-tab="cultural">Cultural Coverage</div>
      <div class="tab" data-tab="resources">Resources</div>
      <div class="tab" data-tab="normative">Normative</div>
      <div class="tab" data-tab="llm">LLM Assessment</div>
    </div>
  </div>
</div>

<!-- ── Main Content ─────────────────────────────────────────────────── -->
<div class="main">

<!-- ═══ Section 1: Overview ═══════════════════════════════════════════ -->
<div class="section active" id="sec-overview">
  <div class="grid grid-5" style="margin-bottom:24px" id="kpi-row"></div>
  <div class="grid grid-2">
    <div class="card"><div class="card-title">Papers Over Time</div><div class="chart-box" id="chart-timeline"></div></div>
    <div class="card"><div class="card-title">Category Distribution</div><div class="chart-box" id="chart-categories"></div></div>
    <div class="card"><div class="card-title">Data Availability</div><div class="chart-box chart-box-sm" id="chart-availability"></div></div>
    <div class="card"><div class="card-title">Top Prolific Authors</div><div class="chart-box chart-box-sm" id="chart-authors"></div></div>
  </div>
</div>

<!-- ═══ Section 2: Taxonomy ══════════════════════════════════════════ -->
<div class="section" id="sec-taxonomy">
  <div class="grid grid-2" style="margin-bottom:20px">
    <div class="card"><div class="card-title">Category x Year Heatmap</div><div class="chart-box chart-box-lg" id="chart-cat-year"></div></div>
    <div class="card"><div class="card-title">Co-occurrence Matrix</div><div class="chart-box chart-box-lg" id="chart-cooccurrence"></div></div>
  </div>
</div>

<!-- ═══ Section 3: Models & Methods ══════════════════════════════════ -->
<div class="section" id="sec-models">
  <div class="grid grid-2" style="margin-bottom:20px">
    <div class="card"><div class="card-title">Model Family Prevalence</div><div class="chart-box" id="chart-model-bar"></div></div>
    <div class="card"><div class="card-title">Methodology Prevalence</div><div class="chart-box" id="chart-method-bar"></div></div>
  </div>
  <div class="card"><div class="card-title">Model x Category Heatmap</div><div class="chart-box chart-box-lg" id="chart-model-cat"></div></div>
</div>

<!-- ═══ Section 4: Cultural Coverage ═════════════════════════════════ -->
<div class="section" id="sec-cultural">
  <div class="grid grid-2" style="margin-bottom:20px">
    <div class="card"><div class="card-title">Pluralistic Relevance</div><div class="chart-box chart-box-sm" id="chart-pluralistic"></div></div>
    <div class="card"><div class="card-title">Ethical Tradition Coverage</div><div class="chart-box" id="chart-traditions"></div></div>
  </div>
  <div class="grid grid-2">
    <div class="card"><div class="card-title">Language Coverage</div><div class="chart-box" id="chart-languages"></div></div>
    <div class="card"><div class="card-title">Language x Category Heatmap</div><div class="chart-box chart-box-lg" id="chart-lang-cat"></div></div>
  </div>
</div>

<!-- ═══ Section 5: Resources ═════════════════════════════════════════ -->
<div class="section" id="sec-resources">
  <div class="filters">
    <input type="text" class="filter-input" id="res-search" placeholder="Search benchmarks...">
    <select class="filter-input" id="res-cat" style="min-width:180px">
      <option value="">All Categories</option>
    </select>
    <select class="filter-input" id="res-year" style="min-width:120px">
      <option value="">All Years</option>
    </select>
    <label style="font-size:0.82rem;color:var(--text-secondary);display:flex;align-items:center;gap:6px;">
      <input type="checkbox" id="res-public"> Public only
    </label>
    <div class="filter-count" id="res-count"></div>
  </div>
  <div class="table-wrap"><table id="res-table">
    <thead><tr>
      <th data-sort="year">Year</th>
      <th data-sort="benchmark">Benchmark</th>
      <th data-sort="what">What It Measures</th>
      <th data-sort="category">Category</th>
      <th data-sort="availability">Availability</th>
    </tr></thead>
    <tbody id="res-tbody"></tbody>
  </table></div>
  <div class="pagination" id="res-pagination"></div>
</div>

<!-- ═══ Section 6: Normative ═════════════════════════════════════════ -->
<div class="section" id="sec-normative">
  <div class="grid grid-2" style="margin-bottom:20px">
    <div class="card"><div class="card-title">Normative Classification</div><div class="chart-box chart-box-sm" id="chart-norm-donut"></div></div>
    <div class="card"><div class="card-title">Framework Distribution</div><div class="chart-box" id="chart-norm-fw"></div></div>
  </div>
  <div class="card">
    <div class="card-title">Papers with Full Normative Operationalization</div>
    <div id="norm-papers"></div>
  </div>
</div>

<!-- ═══ Section 7: LLM Assessment ═════════════════════════════════════ -->
<div class="section" id="sec-llm">
  <div class="grid grid-5" style="margin-bottom:24px">
    <div class="kpi"><div class="kpi-value" style="color:#22d3ee" id="llm-kpi-models">0</div><div class="kpi-label">Papers with LLM Models</div></div>
    <div class="kpi"><div class="kpi-value" style="color:#22c55e" id="llm-kpi-urls">0</div><div class="kpi-label">Papers with Data URLs</div></div>
    <div class="kpi"><div class="kpi-value" style="color:#f59e0b" id="llm-kpi-pct">0%</div><div class="kpi-label">LLM Coverage Rate</div></div>
  </div>
  <div class="grid grid-2" style="margin-bottom:20px">
    <div class="card"><div class="card-title">LLM Model Frequency (Top 20)</div><div class="chart-box chart-box-lg" id="chart-llm-models"></div></div>
    <div class="card"><div class="card-title">Assessment Coverage by Year</div><div class="chart-box chart-box-lg" id="chart-llm-year"></div></div>
  </div>
  <div class="grid grid-2">
    <div class="card"><div class="card-title">Data Repository Distribution</div><div class="chart-box" id="chart-llm-repos"></div></div>
  </div>
</div>

</div><!-- /main -->

<div class="footer">
  CEI Literature Vault &bull; Generated 2026-02-15 &bull; Script: generate_vault_dashboard.py
</div>

<!-- ═══ DATA & SCRIPTS ══════════════════════════════════════════════ -->
<script>
const DATA = {data_json};

const CAT_COLORS = [
  '#6366f1','#22d3ee','#f59e0b','#ec4899','#22c55e',
  '#a855f7','#f97316','#14b8a6','#e879f9','#38bdf8'
];

// ── Tab navigation ────────────────────────────────────────────────────
document.querySelectorAll('.tab').forEach(tab => {{
  tab.addEventListener('click', () => {{
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById('sec-' + tab.dataset.tab).classList.add('active');
    // Resize charts on tab switch (ECharts needs this)
    setTimeout(() => window.dispatchEvent(new Event('resize')), 50);
  }});
}});

// ── KPI count-up animation ────────────────────────────────────────────
function animateValue(el, end, suffix='') {{
  const duration = 1000;
  const start = 0;
  const startTime = performance.now();
  function update(now) {{
    const elapsed = now - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.round(start + (end - start) * eased);
    el.textContent = current.toLocaleString() + suffix;
    if (progress < 1) requestAnimationFrame(update);
  }}
  requestAnimationFrame(update);
}}

// ── Build KPI cards ───────────────────────────────────────────────────
(function buildKPIs() {{
  const kpis = [
    {{ value: DATA.kpi.total, label: 'Papers Screened', suffix: '' }},
    {{ value: DATA.kpi.candidates, label: 'Benchmark Candidates', suffix: '' }},
    {{ value: DATA.kpi.public, label: 'Public Benchmarks', suffix: '' }},
    {{ value: DATA.kpi.pluralisticPct, label: 'Pluralistic Relevance', suffix: '%' }},
    {{ value: DATA.kpi.normative, label: 'Normative Ethics', suffix: '' }},
    {{ value: DATA.kpi.llmModels, label: 'Papers with LLM Data', suffix: '' }},
  ];
  const row = document.getElementById('kpi-row');
  kpis.forEach(k => {{
    const div = document.createElement('div');
    div.className = 'kpi';
    div.innerHTML = '<div class="kpi-value" data-target="' + k.value + '" data-suffix="' + k.suffix + '">0</div>'
                  + '<div class="kpi-label">' + k.label + '</div>';
    row.appendChild(div);
  }});
  // Animate after a short delay
  setTimeout(() => {{
    row.querySelectorAll('.kpi-value').forEach(el => {{
      animateValue(el, parseInt(el.dataset.target), el.dataset.suffix);
    }});
  }}, 200);
}})();

// ── Populate subtitle from data ──────────────────────────────────────
document.getElementById('subtitle').textContent =
  DATA.kpi.total + ' papers screened \u2022 ' + DATA.kpi.candidates + ' benchmark candidates \u2022 Generated 2026-02-15';

// ── ECharts helpers ───────────────────────────────────────────────────
function initChart(id) {{
  const dom = document.getElementById(id);
  if (!dom) return null;
  const chart = echarts.init(dom, null, {{ renderer: 'canvas' }});
  window.addEventListener('resize', () => chart.resize());
  return chart;
}}

const commonTooltip = {{
  backgroundColor: 'rgba(24,24,27,0.95)',
  borderColor: '#3f3f46',
  textStyle: {{ color: '#fafafa', fontSize: 12 }},
}};

// ── 1. Timeline (stacked area) ────────────────────────────────────────
(function() {{
  const chart = initChart('chart-timeline');
  if (!chart) return;
  const years = Object.keys(DATA.timeline).map(Number);
  const allVals = years.map(y => DATA.timeline[y].all);
  const candVals = years.map(y => DATA.timeline[y].cand);
  const exclVals = years.map(y => DATA.timeline[y].all - DATA.timeline[y].cand);
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'axis' }},
    legend: {{ top: 0, textStyle: {{ color: '#a1a1aa', fontSize: 11 }}, itemWidth: 14, itemHeight: 10 }},
    grid: {{ left: 50, right: 20, top: 40, bottom: 30 }},
    xAxis: {{ type: 'category', data: years, axisLine: {{ lineStyle: {{ color: '#3f3f46' }} }}, axisLabel: {{ color: '#71717a' }} }},
    yAxis: {{ type: 'value', splitLine: {{ lineStyle: {{ color: '#27272a' }} }}, axisLabel: {{ color: '#71717a' }} }},
    series: [
      {{ name: 'Excluded', type: 'bar', stack: 'total', data: exclVals, itemStyle: {{ color: '#3f3f46' }}, barWidth: '60%' }},
      {{ name: 'Benchmarks', type: 'bar', stack: 'total', data: candVals, itemStyle: {{ color: '#6366f1' }}, barWidth: '60%' }},
      {{ name: 'Benchmark %', type: 'line', data: years.map((y,i) => allVals[i]>0 ? Math.round(candVals[i]/allVals[i]*100) : 0),
        yAxisIndex: 0, symbol: 'circle', symbolSize: 6, lineStyle: {{ color: '#f59e0b', width: 2 }},
        itemStyle: {{ color: '#f59e0b' }}, z: 10 }},
    ],
  }});
}})();

// ── 2. Category bar chart ─────────────────────────────────────────────
(function() {{
  const chart = initChart('chart-categories');
  if (!chart) return;
  const cats = DATA.categories.slice().sort((a,b) => a.count - b.count);
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'axis', axisPointer: {{ type: 'shadow' }} }},
    grid: {{ left: 220, right: 40, top: 10, bottom: 10 }},
    xAxis: {{ type: 'value', splitLine: {{ lineStyle: {{ color: '#27272a' }} }}, axisLabel: {{ color: '#71717a' }} }},
    yAxis: {{ type: 'category', data: cats.map(c => c.short), axisLabel: {{ color: '#a1a1aa', fontSize: 11 }}, axisLine: {{ lineStyle: {{ color: '#3f3f46' }} }} }},
    series: [{{
      type: 'bar', data: cats.map((c,i) => ({{ value: c.count, itemStyle: {{ color: CAT_COLORS[c.id-1] }} }})),
      barWidth: '65%',
      label: {{ show: true, position: 'right', color: '#a1a1aa', fontSize: 11, fontFamily: 'JetBrains Mono' }},
    }}],
  }});
}})();

// ── 3. Availability donut ─────────────────────────────────────────────
(function() {{
  const chart = initChart('chart-availability');
  if (!chart) return;
  const d = DATA.availability;
  const items = [
    {{ name: 'Public', value: d['Public'] || 0 }},
    {{ name: 'Code available', value: d['Code available'] || 0 }},
    {{ name: 'Partially public', value: d['Partially public'] || 0 }},
    {{ name: 'Not stated', value: d['Not stated'] || 0 }},
    {{ name: 'Not public', value: d['Not public'] || 0 }},
  ].filter(x => x.value > 0);
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'item', formatter: '{{b}}: {{c}} ({{d}}%)' }},
    legend: {{ bottom: 0, textStyle: {{ color: '#a1a1aa', fontSize: 11 }}, itemWidth: 12, itemHeight: 10 }},
    color: ['#22c55e','#6366f1','#f59e0b','#71717a','#ef4444'],
    series: [{{
      type: 'pie', radius: ['45%','72%'], center: ['50%','45%'],
      data: items,
      label: {{ show: true, color: '#a1a1aa', fontSize: 11, formatter: '{{b}}\\n{{d}}%' }},
      emphasis: {{ label: {{ fontSize: 13, fontWeight: 600 }} }},
    }}],
  }});
}})();

// ── 4. Top authors bar ────────────────────────────────────────────────
(function() {{
  const chart = initChart('chart-authors');
  if (!chart) return;
  const authors = DATA.topAuthors.slice().reverse();
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'axis', axisPointer: {{ type: 'shadow' }} }},
    grid: {{ left: 150, right: 40, top: 10, bottom: 10 }},
    xAxis: {{ type: 'value', splitLine: {{ lineStyle: {{ color: '#27272a' }} }}, axisLabel: {{ color: '#71717a' }} }},
    yAxis: {{ type: 'category', data: authors.map(a => a.name), axisLabel: {{ color: '#a1a1aa', fontSize: 11 }}, axisLine: {{ lineStyle: {{ color: '#3f3f46' }} }} }},
    series: [{{
      type: 'bar', data: authors.map(a => a.count),
      barWidth: '60%', itemStyle: {{ color: '#818cf8' }},
      label: {{ show: true, position: 'right', color: '#a1a1aa', fontSize: 11, fontFamily: 'JetBrains Mono' }},
    }}],
  }});
}})();

// ── 5. Category x Year heatmap ────────────────────────────────────────
(function() {{
  const chart = initChart('chart-cat-year');
  if (!chart) return;
  const years = Object.keys(DATA.timeline).map(Number);
  const catNames = DATA.categories.map(c => c.short);
  const heatData = [];
  let maxVal = 0;
  DATA.categories.forEach((cat, ci) => {{
    years.forEach((y, yi) => {{
      const v = cat.byYear[y] || 0;
      heatData.push([yi, ci, v]);
      if (v > maxVal) maxVal = v;
    }});
  }});
  chart.setOption({{
    tooltip: {{ ...commonTooltip, formatter: p => p.data[2] > 0 ? catNames[p.data[1]] + ' (' + years[p.data[0]] + '): ' + p.data[2] + ' papers' : '' }},
    grid: {{ left: 220, right: 60, top: 10, bottom: 30 }},
    xAxis: {{ type: 'category', data: years, axisLabel: {{ color: '#71717a' }}, splitArea: {{ show: true, areaStyle: {{ color: ['rgba(0,0,0,0)', 'rgba(255,255,255,0.02)'] }} }} }},
    yAxis: {{ type: 'category', data: catNames, axisLabel: {{ color: '#a1a1aa', fontSize: 11 }} }},
    visualMap: {{ min: 0, max: maxVal, calculable: false, orient: 'vertical', right: 0, top: 'center',
      inRange: {{ color: ['#18181b','#312e81','#4f46e5','#818cf8','#c7d2fe'] }},
      textStyle: {{ color: '#71717a' }} }},
    series: [{{ type: 'heatmap', data: heatData, label: {{ show: true, color: '#a1a1aa', fontSize: 10, formatter: p => p.data[2] || '' }},
      emphasis: {{ itemStyle: {{ shadowBlur: 10, shadowColor: 'rgba(99,102,241,0.4)' }} }} }}],
  }});
}})();

// ── 6. Co-occurrence matrix ───────────────────────────────────────────
(function() {{
  const chart = initChart('chart-cooccurrence');
  if (!chart) return;
  const labels = DATA.categories.map((c,i) => (i+1) + '. ' + c.short.substring(0,18));
  const heatData = [];
  let maxVal = 0;
  DATA.cooccurrence.forEach((row, ri) => {{
    row.forEach((val, ci) => {{
      if (ri !== ci) {{
        heatData.push([ci, ri, val]);
        if (val > maxVal) maxVal = val;
      }}
    }});
  }});
  chart.setOption({{
    tooltip: {{ ...commonTooltip, formatter: p => {{
      if (p.data[0] === p.data[1]) return '';
      return labels[p.data[1]] + ' & ' + labels[p.data[0]] + ': ' + p.data[2] + ' papers';
    }} }},
    grid: {{ left: 180, right: 60, top: 10, bottom: 100 }},
    xAxis: {{ type: 'category', data: labels, axisLabel: {{ color: '#71717a', fontSize: 10, rotate: 45 }}, splitArea: {{ show: true }} }},
    yAxis: {{ type: 'category', data: labels, axisLabel: {{ color: '#a1a1aa', fontSize: 10 }} }},
    visualMap: {{ min: 0, max: maxVal, calculable: false, orient: 'vertical', right: 0, top: 'center',
      inRange: {{ color: ['#18181b','#4a1d6e','#7c3aed','#a78bfa','#ddd6fe'] }},
      textStyle: {{ color: '#71717a' }} }},
    series: [{{ type: 'heatmap', data: heatData, label: {{ show: true, color: '#a1a1aa', fontSize: 10,
      formatter: p => p.data[2] || '' }},
      emphasis: {{ itemStyle: {{ shadowBlur: 10 }} }} }}],
  }});
}})();

// ── 7. Model bar chart ────────────────────────────────────────────────
(function() {{
  const chart = initChart('chart-model-bar');
  if (!chart) return;
  const models = DATA.models.slice(0, 15).reverse();
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'axis', axisPointer: {{ type: 'shadow' }} }},
    grid: {{ left: 140, right: 40, top: 10, bottom: 10 }},
    xAxis: {{ type: 'value', splitLine: {{ lineStyle: {{ color: '#27272a' }} }}, axisLabel: {{ color: '#71717a' }} }},
    yAxis: {{ type: 'category', data: models.map(m => m.name), axisLabel: {{ color: '#a1a1aa', fontSize: 11 }}, axisLine: {{ lineStyle: {{ color: '#3f3f46' }} }} }},
    series: [{{
      type: 'bar', data: models.map(m => m.count),
      barWidth: '60%', itemStyle: {{ color: '#22d3ee' }},
      label: {{ show: true, position: 'right', color: '#a1a1aa', fontSize: 11, fontFamily: 'JetBrains Mono' }},
    }}],
  }});
}})();

// ── 8. Method bar chart ───────────────────────────────────────────────
(function() {{
  const chart = initChart('chart-method-bar');
  if (!chart) return;
  const methods = DATA.methods.slice().reverse();
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'axis', axisPointer: {{ type: 'shadow' }} }},
    grid: {{ left: 200, right: 40, top: 10, bottom: 10 }},
    xAxis: {{ type: 'value', splitLine: {{ lineStyle: {{ color: '#27272a' }} }}, axisLabel: {{ color: '#71717a' }} }},
    yAxis: {{ type: 'category', data: methods.map(m => m.name), axisLabel: {{ color: '#a1a1aa', fontSize: 11 }}, axisLine: {{ lineStyle: {{ color: '#3f3f46' }} }} }},
    series: [{{
      type: 'bar', data: methods.map(m => m.count),
      barWidth: '60%', itemStyle: {{ color: '#f59e0b' }},
      label: {{ show: true, position: 'right', color: '#a1a1aa', fontSize: 11, fontFamily: 'JetBrains Mono' }},
    }}],
  }});
}})();

// ── 9. Model x Category heatmap ───────────────────────────────────────
(function() {{
  const chart = initChart('chart-model-cat');
  if (!chart) return;
  const topModels = DATA.models.slice(0, 12);
  const modelNames = topModels.map(m => m.name);
  const catNames = DATA.categoryNames;
  const heatData = [];
  let maxVal = 0;
  topModels.forEach((m, mi) => {{
    m.byCategory.forEach((v, ci) => {{
      heatData.push([ci, mi, v]);
      if (v > maxVal) maxVal = v;
    }});
  }});
  chart.setOption({{
    tooltip: {{ ...commonTooltip, formatter: p => modelNames[p.data[1]] + ' in ' + catNames[p.data[0]] + ': ' + p.data[2] + ' papers' }},
    grid: {{ left: 140, right: 60, top: 10, bottom: 130 }},
    xAxis: {{ type: 'category', data: catNames, axisLabel: {{ color: '#71717a', fontSize: 10, rotate: 40 }} }},
    yAxis: {{ type: 'category', data: modelNames, axisLabel: {{ color: '#a1a1aa', fontSize: 11 }} }},
    visualMap: {{ min: 0, max: maxVal, calculable: false, orient: 'vertical', right: 0, top: 'center',
      inRange: {{ color: ['#18181b','#164e63','#0891b2','#22d3ee','#cffafe'] }},
      textStyle: {{ color: '#71717a' }} }},
    series: [{{ type: 'heatmap', data: heatData, label: {{ show: true, color: '#a1a1aa', fontSize: 10,
      formatter: p => p.data[2] || '' }},
      emphasis: {{ itemStyle: {{ shadowBlur: 10, shadowColor: 'rgba(34,211,238,0.3)' }} }} }}],
  }});
}})();

// ── 10. Pluralistic donut ─────────────────────────────────────────────
(function() {{
  const chart = initChart('chart-pluralistic');
  if (!chart) return;
  const d = DATA.pluralistic;
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'item', formatter: '{{b}}: {{c}} ({{d}}%)' }},
    legend: {{ bottom: 0, textStyle: {{ color: '#a1a1aa', fontSize: 11 }} }},
    color: ['#22c55e','#f59e0b','#71717a'],
    series: [{{
      type: 'pie', radius: ['45%','72%'], center: ['50%','42%'],
      data: [
        {{ name: 'Yes', value: d.Yes }},
        {{ name: 'Partial', value: d.Partial }},
        {{ name: 'No', value: d.No }},
      ],
      label: {{ show: true, color: '#a1a1aa', formatter: '{{b}}\\n{{c}} ({{d}}%)' }},
      emphasis: {{ label: {{ fontSize: 13, fontWeight: 600 }} }},
    }}],
  }});
}})();

// ── 11. Ethical traditions bar ─────────────────────────────────────────
(function() {{
  const chart = initChart('chart-traditions');
  if (!chart) return;
  const trads = DATA.traditions.slice().reverse();
  const colorMap = {{ Critical: '#ef4444', Severe: '#f97316', Moderate: '#f59e0b', Adequate: '#22c55e' }};
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'axis', axisPointer: {{ type: 'shadow' }} }},
    grid: {{ left: 160, right: 40, top: 10, bottom: 10 }},
    xAxis: {{ type: 'value', splitLine: {{ lineStyle: {{ color: '#27272a' }} }}, axisLabel: {{ color: '#71717a' }} }},
    yAxis: {{ type: 'category', data: trads.map(t => t.name), axisLabel: {{ color: '#a1a1aa', fontSize: 11 }}, axisLine: {{ lineStyle: {{ color: '#3f3f46' }} }} }},
    series: [{{
      type: 'bar', data: trads.map(t => ({{ value: t.count, itemStyle: {{ color: colorMap[t.level] || '#71717a' }} }})),
      barWidth: '60%',
      label: {{ show: true, position: 'right', color: '#a1a1aa', fontSize: 11, fontFamily: 'JetBrains Mono',
        formatter: p => {{
          const t = trads[p.dataIndex];
          return t.count + ' (' + t.level + ')';
        }}
      }},
    }}],
  }});
}})();

// ── 12. Languages bar ─────────────────────────────────────────────────
(function() {{
  const chart = initChart('chart-languages');
  if (!chart) return;
  const langs = DATA.languages.slice().reverse();
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'axis', axisPointer: {{ type: 'shadow' }} }},
    grid: {{ left: 120, right: 40, top: 10, bottom: 10 }},
    xAxis: {{ type: 'value', splitLine: {{ lineStyle: {{ color: '#27272a' }} }}, axisLabel: {{ color: '#71717a' }} }},
    yAxis: {{ type: 'category', data: langs.map(l => l.name), axisLabel: {{ color: '#a1a1aa', fontSize: 11 }}, axisLine: {{ lineStyle: {{ color: '#3f3f46' }} }} }},
    series: [{{
      type: 'bar', data: langs.map(l => l.count),
      barWidth: '60%', itemStyle: {{ color: '#14b8a6' }},
      label: {{ show: true, position: 'right', color: '#a1a1aa', fontSize: 11, fontFamily: 'JetBrains Mono' }},
    }}],
  }});
}})();

// ── 13. Language x Category heatmap ───────────────────────────────────
(function() {{
  const chart = initChart('chart-lang-cat');
  if (!chart) return;
  const topLangs = DATA.languages.slice(0, 10);
  const langNames = topLangs.map(l => l.name);
  const catNames = DATA.categoryNames;
  const heatData = [];
  let maxVal = 0;
  topLangs.forEach((l, li) => {{
    l.byCategory.forEach((v, ci) => {{
      heatData.push([ci, li, v]);
      if (v > maxVal) maxVal = v;
    }});
  }});
  chart.setOption({{
    tooltip: {{ ...commonTooltip, formatter: p => langNames[p.data[1]] + ' in ' + catNames[p.data[0]] + ': ' + p.data[2] + ' papers' }},
    grid: {{ left: 120, right: 60, top: 10, bottom: 130 }},
    xAxis: {{ type: 'category', data: catNames, axisLabel: {{ color: '#71717a', fontSize: 10, rotate: 40 }} }},
    yAxis: {{ type: 'category', data: langNames, axisLabel: {{ color: '#a1a1aa', fontSize: 11 }} }},
    visualMap: {{ min: 0, max: Math.max(maxVal, 1), calculable: false, orient: 'vertical', right: 0, top: 'center',
      inRange: {{ color: ['#18181b','#134e4a','#0d9488','#14b8a6','#99f6e4'] }},
      textStyle: {{ color: '#71717a' }} }},
    series: [{{ type: 'heatmap', data: heatData, label: {{ show: true, color: '#a1a1aa', fontSize: 10,
      formatter: p => p.data[2] || '' }} }}],
  }});
}})();

// ── 14. Resources table ───────────────────────────────────────────────
(function() {{
  const PAGE_SIZE = 25;
  let filtered = [...DATA.resources];
  let currentPage = 1;
  let sortCol = 'year';
  let sortDir = -1;

  // Populate dropdowns
  const catSet = new Set(DATA.resources.map(r => r.category));
  const catSel = document.getElementById('res-cat');
  [...catSet].sort().forEach(c => {{
    const opt = document.createElement('option');
    opt.value = c; opt.textContent = c;
    catSel.appendChild(opt);
  }});
  const yearSet = new Set(DATA.resources.map(r => r.year));
  const yearSel = document.getElementById('res-year');
  [...yearSet].sort((a,b) => b-a).forEach(y => {{
    const opt = document.createElement('option');
    opt.value = y; opt.textContent = y;
    yearSel.appendChild(opt);
  }});

  function applyFilters() {{
    const search = document.getElementById('res-search').value.toLowerCase();
    const cat = catSel.value;
    const year = yearSel.value;
    const publicOnly = document.getElementById('res-public').checked;

    filtered = DATA.resources.filter(r => {{
      if (search && !r.benchmark.toLowerCase().includes(search) && !r.what.toLowerCase().includes(search) && !r.filename.toLowerCase().includes(search)) return false;
      if (cat && r.category !== cat) return false;
      if (year && r.year !== parseInt(year)) return false;
      if (publicOnly && r.availability !== 'Public') return false;
      return true;
    }});

    // Sort
    filtered.sort((a, b) => {{
      let va = a[sortCol], vb = b[sortCol];
      if (typeof va === 'string') va = va.toLowerCase();
      if (typeof vb === 'string') vb = vb.toLowerCase();
      if (va < vb) return -sortDir;
      if (va > vb) return sortDir;
      return 0;
    }});

    currentPage = 1;
    render();
  }}

  function render() {{
    const tbody = document.getElementById('res-tbody');
    const start = (currentPage - 1) * PAGE_SIZE;
    const page = filtered.slice(start, start + PAGE_SIZE);

    document.getElementById('res-count').textContent = filtered.length + ' results';

    tbody.innerHTML = page.map(r => {{
      const badge = r.availability === 'Public' ? 'badge-public' : r.availability === 'Code available' ? 'badge-code' : 'badge-partial';
      return '<tr>'
        + '<td style="font-family:var(--font-mono)">' + r.year + '</td>'
        + '<td title="' + r.benchmark.replace(/"/g,'&quot;') + '">' + r.benchmark + '</td>'
        + '<td title="' + r.what.replace(/"/g,'&quot;') + '">' + r.what + '</td>'
        + '<td>' + r.category + '</td>'
        + '<td><span class="badge ' + badge + '">' + r.availability + '</span></td>'
        + '</tr>';
    }}).join('');

    // Pagination
    const totalPages = Math.ceil(filtered.length / PAGE_SIZE);
    const pag = document.getElementById('res-pagination');
    if (totalPages <= 1) {{ pag.innerHTML = ''; return; }}
    let html = '<button class="page-btn" ' + (currentPage<=1?'disabled':'') + ' onclick="window.__resPage(' + (currentPage-1) + ')">&laquo; Prev</button>';
    const start_p = Math.max(1, currentPage - 3);
    const end_p = Math.min(totalPages, currentPage + 3);
    for (let i = start_p; i <= end_p; i++) {{
      html += '<button class="page-btn' + (i===currentPage?' active':'') + '" onclick="window.__resPage(' + i + ')">' + i + '</button>';
    }}
    html += '<button class="page-btn" ' + (currentPage>=totalPages?'disabled':'') + ' onclick="window.__resPage(' + (currentPage+1) + ')">Next &raquo;</button>';
    pag.innerHTML = html;
  }}

  window.__resPage = function(p) {{ currentPage = p; render(); }};

  // Event listeners
  document.getElementById('res-search').addEventListener('input', applyFilters);
  catSel.addEventListener('change', applyFilters);
  yearSel.addEventListener('change', applyFilters);
  document.getElementById('res-public').addEventListener('change', applyFilters);

  // Column sort
  document.querySelectorAll('#res-table th[data-sort]').forEach(th => {{
    th.addEventListener('click', () => {{
      const col = th.dataset.sort;
      if (sortCol === col) sortDir *= -1;
      else {{ sortCol = col; sortDir = col === 'year' ? -1 : 1; }}
      applyFilters();
    }});
  }});

  applyFilters();
}})();

// ── 15. Normative donut ───────────────────────────────────────────────
(function() {{
  const chart = initChart('chart-norm-donut');
  if (!chart) return;
  const d = DATA.normative;
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'item', formatter: '{{b}}: {{c}} ({{d}}%)' }},
    legend: {{ bottom: 0, textStyle: {{ color: '#a1a1aa', fontSize: 11 }} }},
    color: ['#22c55e','#f59e0b','#3f3f46'],
    series: [{{
      type: 'pie', radius: ['45%','72%'], center: ['50%','42%'],
      data: [
        {{ name: 'Yes (full)', value: d.yes }},
        {{ name: 'Borderline', value: d.borderline }},
        {{ name: 'Excluded', value: d.excluded }},
      ],
      label: {{ show: true, color: '#a1a1aa', formatter: '{{b}}\\n{{c}}' }},
      emphasis: {{ label: {{ fontSize: 13, fontWeight: 600 }} }},
    }}],
  }});
}})();

// ── 16. Framework bar chart ───────────────────────────────────────────
(function() {{
  const chart = initChart('chart-norm-fw');
  if (!chart) return;
  const fws = DATA.normative.frameworks.slice().reverse();
  if (fws.length === 0) return;
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'axis', axisPointer: {{ type: 'shadow' }} }},
    grid: {{ left: 240, right: 40, top: 10, bottom: 10 }},
    xAxis: {{ type: 'value', splitLine: {{ lineStyle: {{ color: '#27272a' }} }}, axisLabel: {{ color: '#71717a' }} }},
    yAxis: {{ type: 'category', data: fws.map(f => f.name), axisLabel: {{ color: '#a1a1aa', fontSize: 11 }}, axisLine: {{ lineStyle: {{ color: '#3f3f46' }} }} }},
    series: [{{
      type: 'bar', data: fws.map(f => f.count),
      barWidth: '60%', itemStyle: {{ color: '#a855f7' }},
      label: {{ show: true, position: 'right', color: '#a1a1aa', fontSize: 11, fontFamily: 'JetBrains Mono' }},
    }}],
  }});
}})();

// ── 17. Normative paper cards ─────────────────────────────────────────
(function() {{
  const container = document.getElementById('norm-papers');
  if (DATA.normative.papers.length === 0) {{
    container.innerHTML = '<p style="color:var(--text-muted)">No papers with full normative operationalization found.</p>';
    return;
  }}
  container.innerHTML = DATA.normative.papers.map(p => {{
    return '<div class="norm-card">'
      + '<h4>' + p.filename.replace('.md','') + '</h4>'
      + '<div class="meta">'
      + '<div><strong>Frameworks:</strong> <span>' + p.frameworks + '</span></div>'
      + '<div><strong>LLMs Tested:</strong> <span>' + p.llms + '</span></div>'
      + '<div><strong>Data Artifact:</strong> <span>' + p.artifact + '</span></div>'
      + '</div></div>';
  }}).join('');
}})();

// ── 18. LLM Assessment KPIs ──────────────────────────────────────────
(function() {{
  const el1 = document.getElementById('llm-kpi-models');
  const el2 = document.getElementById('llm-kpi-urls');
  const el3 = document.getElementById('llm-kpi-pct');
  if (el1) el1.textContent = (DATA.kpi.llmModels || 0).toLocaleString();
  if (el2) el2.textContent = (DATA.kpi.dataUrls || 0).toLocaleString();
  if (el3) el3.textContent = (DATA.kpi.llmModelsPct || 0) + '%';
}})();

// ── 19. LLM Model Frequency bar chart ────────────────────────────────
(function() {{
  const chart = initChart('chart-llm-models');
  if (!chart || !DATA.llmModels || DATA.llmModels.length === 0) return;
  const models = DATA.llmModels.slice().reverse();
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'axis', axisPointer: {{ type: 'shadow' }} }},
    grid: {{ left: 140, right: 50, top: 10, bottom: 10 }},
    xAxis: {{ type: 'value', splitLine: {{ lineStyle: {{ color: '#27272a' }} }}, axisLabel: {{ color: '#71717a' }} }},
    yAxis: {{ type: 'category', data: models.map(m => m.name), axisLabel: {{ color: '#a1a1aa', fontSize: 11 }}, axisLine: {{ lineStyle: {{ color: '#3f3f46' }} }} }},
    series: [{{
      type: 'bar', data: models.map(m => m.count),
      barWidth: '60%', itemStyle: {{ color: '#22d3ee' }},
      label: {{ show: true, position: 'right', color: '#a1a1aa', fontSize: 11, fontFamily: 'JetBrains Mono' }},
    }}],
  }});
}})();

// ── 20. Assessment Coverage by Year (stacked bar) ────────────────────
(function() {{
  const chart = initChart('chart-llm-year');
  if (!chart || !DATA.llmByYear) return;
  const years = Object.keys(DATA.llmByYear).map(Number).sort();
  const assessed = years.map(y => DATA.llmByYear[y].assessed);
  const notAssessed = years.map(y => DATA.llmByYear[y].notAssessed);
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'axis' }},
    legend: {{ top: 0, textStyle: {{ color: '#a1a1aa', fontSize: 11 }}, itemWidth: 14, itemHeight: 10 }},
    grid: {{ left: 50, right: 20, top: 40, bottom: 30 }},
    xAxis: {{ type: 'category', data: years, axisLine: {{ lineStyle: {{ color: '#3f3f46' }} }}, axisLabel: {{ color: '#71717a' }} }},
    yAxis: {{ type: 'value', splitLine: {{ lineStyle: {{ color: '#27272a' }} }}, axisLabel: {{ color: '#71717a' }} }},
    series: [
      {{ name: 'No LLM Models', type: 'bar', stack: 'total', data: notAssessed, itemStyle: {{ color: '#3f3f46' }}, barWidth: '60%' }},
      {{ name: 'With LLM Models', type: 'bar', stack: 'total', data: assessed, itemStyle: {{ color: '#22d3ee' }}, barWidth: '60%' }},
    ],
  }});
}})();

// ── 21. Data Repository Distribution (donut) ─────────────────────────
(function() {{
  const chart = initChart('chart-llm-repos');
  if (!chart || !DATA.repoDistribution || DATA.repoDistribution.length === 0) return;
  const REPO_COLORS = {{
    'GitHub': '#22c55e', 'HuggingFace': '#f59e0b', 'Zenodo': '#6366f1',
    'OSF': '#ec4899', 'Kaggle': '#22d3ee', 'Other': '#71717a'
  }};
  chart.setOption({{
    tooltip: {{ ...commonTooltip, trigger: 'item', formatter: '{{b}}: {{c}} ({{d}}%)' }},
    legend: {{ bottom: 0, textStyle: {{ color: '#a1a1aa', fontSize: 11 }}, itemWidth: 12, itemHeight: 10 }},
    series: [{{
      type: 'pie', radius: ['45%','72%'], center: ['50%','45%'],
      data: DATA.repoDistribution.map(r => ({{
        name: r.name, value: r.count,
        itemStyle: {{ color: REPO_COLORS[r.name] || '#71717a' }}
      }})),
      label: {{ show: true, color: '#a1a1aa', fontSize: 11, formatter: '{{b}}\\n{{c}} ({{d}}%)' }},
      emphasis: {{ label: {{ fontSize: 13, fontWeight: 600 }} }},
    }}],
  }});
}})();
</script>
</body>
</html>'''


# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    print("Loading data sources...")
    with open(ALL_CLASSIFICATIONS_FILE, "r", encoding="utf-8") as f:
        all_entries = json.load(f)
    print(f"  All classifications: {len(all_entries)}")

    with open(CANDIDATES_FILE, "r", encoding="utf-8") as f:
        candidates = json.load(f)
    print(f"  Candidates: {len(candidates)}")

    with open(NORMATIVE_FILE, "r", encoding="utf-8") as f:
        normative_entries = json.load(f)
    print(f"  Normative v2: {len(normative_entries)}")

    with open(AUTHOR_MAP_FILE, "r", encoding="utf-8") as f:
        author_map = json.load(f)
    print(f"  Author map: {len(author_map)}")

    print("  Scanning paper YAML fields...")
    paper_yaml = scan_paper_yaml_fields()
    print(f"  Papers scanned: {len(paper_yaml)}")

    print("\nComputing dashboard data...")
    data = compute_dashboard_data(all_entries, candidates, normative_entries, author_map, paper_yaml)

    data_json = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
    print(f"  JSON data blob: {len(data_json):,} characters")

    print("\nBuilding HTML...")
    html = build_html(data_json)

    DASHBOARDS_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\nDashboard written to {OUTPUT_FILE}")
    print(f"  HTML size: {len(html):,} characters ({len(html)//1024} KB)")
    print(f"  Data blob: {len(data_json):,} characters ({len(data_json)//1024} KB)")

    # Verification
    print("\n=== VERIFICATION ===")
    print(f"  KPI total:      {data['kpi']['total']}")
    print(f"  KPI candidates:  {data['kpi']['candidates']}")
    print(f"  KPI public:      {data['kpi']['public']}")
    print(f"  KPI pluralistic: {data['kpi']['pluralisticPct']}%")
    print(f"  KPI normative:   {data['kpi']['normative']}")
    print(f"  Categories:      {len(data['categories'])}")
    print(f"  Models:          {len(data['models'])}")
    print(f"  Methods:         {len(data['methods'])}")
    print(f"  Resources:       {len(data['resources'])}")
    print(f"  Top authors:     {len(data['topAuthors'])}")
    print(f"  LLM models:      {data['kpi']['llmModels']} papers ({data['kpi']['llmModelsPct']}%)")
    print(f"  Data URLs:       {data['kpi']['dataUrls']} papers")
    print(f"  LLM model types: {len(data['llmModels'])}")
    print(f"  Repo types:      {len(data['repoDistribution'])}")


if __name__ == "__main__":
    main()
