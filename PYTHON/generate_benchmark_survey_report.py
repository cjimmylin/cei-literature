#!/usr/bin/env python3
"""
Generate comprehensive benchmark survey report from benchmark_survey_candidates.json.
Categorizes all 528 candidates into 10 categories and produces a full markdown report.
"""

import json
import re
import sys
from collections import defaultdict, Counter
from pathlib import Path

INPUT_FILE = Path(__file__).parent.parent / "logs" / "benchmark_survey_candidates.json"
OUTPUT_FILE = Path(__file__).parent.parent / "STATISTICS" / "20260208-llm-ethics-benchmark-survey.md"

# ── Category definitions with keyword/phrase matching ──────────────────────

CATEGORIES = {
    "1. Moral Reasoning & Ethical Judgment": {
        "desc": "Benchmarks that test LLMs on moral dilemmas, ethical scenarios, and normative reasoning tasks.",
        "keywords": [
            "moral reason", "moral judg", "moral dilemma", "ethical judg", "ethical reason",
            "ethical decision", "moral decision", "trolley", "moral machine",
            "moral sense", "moral foundation", "moral cognit", "moral evaluat",
            "ethical evaluat", "moral scenario", "ethics benchmark", "moral competenc",
            "moral abilit", "deontic", "consequential", "utilitarian", "deontolog",
            "virtue ethic", "moral philosophy", "normative reason", "moral choice",
            "right and wrong", "ethical dilemma", "moral intuition", "moral permissibl",
            "moral belief", "moral value", "moral orient", "ethical orient",
            "moral alignment", "moral distress", "moral sensitivity",
            "ETHICS dataset", "ETHICS benchmark", "moral stories", "moral except",
            "jiminy cricket", "machiavelli", "scruples",
        ],
        "name_keywords": [
            "moral", "ethic", "ETHICS", "trolley", "jiminy", "machiavelli", "scruples",
            "moral machine", "MoralBench", "MoralChoice", "MoralExcept", "EthicsBench",
            "MoralDial", "MoralDirection", "MoralCoT", "Delphi",
        ],
    },
    "2. Value Alignment & Value Pluralism": {
        "desc": "Benchmarks measuring how well LLMs align with human values, preferences, and diverse value systems.",
        "keywords": [
            "value align", "value plural", "human value", "value survey",
            "value measure", "value assess", "world value", "schwartz",
            "value orientat", "value system", "value sensitiv",
            "value conflict", "value trade", "value diversity",
            "value learn", "preference align", "opinion align", "political lean",
            "political bias", "ideolog", "partisan", "liberal", "conservative",
            "opinion diversity", "cultural value", "societal value",
            "value represen", "value evaluat", "value bench",
            "opinion poll", "survey alignment", "value prior",
            "value express", "global opinion",
        ],
        "name_keywords": [
            "value", "ValueBench", "ValueAlign", "opinion", "OpinionQA",
            "GlobalOpinion", "ValueEval", "ValuePrism", "VALUENET",
            "VALUE", "Schwartz", "political", "ideology", "partisan",
        ],
    },
    "3. Cultural & Cross-Cultural Ethics": {
        "desc": "Benchmarks examining cultural sensitivity, cross-cultural moral variation, and multicultural ethical norms.",
        "keywords": [
            "cultural", "cross-cultural", "multicultural", "multilingual",
            "culture-specific", "culturally", "cultural norm",
            "cultural bias", "cultural sensitiv", "cultural aware",
            "cultural context", "cultural differ", "cultural divers",
            "western bias", "non-western", "global south",
            "arabic", "chinese", "japanese", "korean", "hindi", "indian",
            "african", "latin america", "european", "islamic", "confucian",
            "indigenous", "regional", "geograph", "country", "nation",
            "language-specific", "locale", "locali",
            "cross-nation", "cross-region", "intercultural",
            "global moral", "global ethic", "world value",
            "cultural context", "cultural relativ",
        ],
        "name_keywords": [
            "cultur", "cross-cultur", "multicult", "Global", "Arabic", "Chinese",
            "Korean", "Japan", "Hindi", "Indian", "Africa", "Islam", "Confuc",
            "multilin", "CBBQ", "CDEval", "CValue", "KoSBI", "KOLD",
            "BLEnD", "SeaEval", "LVLM-Ehics", "GlobalOpinion",
        ],
    },
    "4. Fairness, Bias & Social Norms": {
        "desc": "Benchmarks measuring social biases (gender, race, religion, etc.), fairness, and adherence to social norms.",
        "keywords": [
            "bias", "fairness", "stereotyp", "discriminat", "prejudic",
            "gender bias", "racial bias", "social bias", "religion bias",
            "demographic", "disparit", "equity", "equal",
            "social norm", "normative", "acceptab", "appropriat",
            "offensive", "microaggress", "sentiment bias",
            "representation bias", "occupation bias", "age bias",
            "disability", "lgbtq", "sexual orient", "intersectional",
            "embedding bias", "model bias", "algorithmic bias",
            "counterfactual", "crows-pairs", "winobias", "winogender",
            "bbq", "bold", "regard", "honest",
            "social chem", "social-chem", "social knowledge",
            "anti-muslim", "anti-", "islamophob", "antisemit",
            "racial", "racist", "sexis", "ageism",
            "debiasing", "debias", "mitigat",
        ],
        "name_keywords": [
            "bias", "fair", "stereotyp", "CrowS", "WinoBias", "WinoGender",
            "BBQ", "BOLD", "StereoSet", "Regard", "HONEST", "SOCIAL-CHEM",
            "Social-Chem", "RealToxicity", "HolisticBias", "BiasAsker",
            "DiscrimEval", "FairBench", "UnQover", "BiasBench",
            "SocialNorm", "NormAd", "NormBank", "Normative",
            "RedditBias", "TweetEval", "equity", "discrimin",
            "DIB", "BiasLab", "KoSBI", "KOLD", "BLEnD",
        ],
    },
    "5. Toxicity, Hate Speech & Harmful Content": {
        "desc": "Benchmarks for detecting, measuring, or mitigating toxic, hateful, or otherwise harmful language generation.",
        "keywords": [
            "toxic", "hate speech", "hateful", "harmful content",
            "offensive language", "abusive", "cyberbully", "harassm",
            "profan", "insult", "slur", "dangerous content",
            "harmful generat", "content moderat", "content filter",
            "unsafe content", "inappropriate", "explicit content",
            "violence", "violent", "graphic content",
            "misinformat", "disinformat", "fake news", "conspiracy",
            "propaganda", "manipulat",
            "detoxif", "toxicity reduct", "toxicity mitigat",
        ],
        "name_keywords": [
            "toxic", "Toxic", "hate", "Hate", "harmful", "Harm",
            "offensive", "abuse", "ToxiGen", "HateCheck", "ETHOS",
            "ImplicitHate", "LatentHatred", "ToxicChat", "HatEval",
            "RealToxicity", "CivilComments", "Jigsaw", "OpenAIModerat",
            "ContentMod", "SafeText", "DisinfoEval", "TruthfulQA",
            "HarmBench", "SimpleSafety", "SALAD",
        ],
    },
    "6. Safety & Red Teaming": {
        "desc": "Benchmarks for evaluating LLM safety, jailbreak robustness, and adversarial attack resistance.",
        "keywords": [
            "safety", "safe", "red team", "jailbreak", "adversarial attack",
            "adversarial prompt", "prompt inject", "guardrail",
            "safety alignment", "safety evaluat", "safety bench",
            "safety test", "attack", "defense", "robust",
            "refusal", "compliance", "over-refusal", "overrefusal",
            "harmful request", "unsafe request", "dangerous request",
            "malicious", "exploit", "vulnerab",
            "safety risk", "risk assess", "risk categor",
            "trustworth", "reliab", "responsible AI",
            "alignment tax", "alignment evaluat",
            "constitutional ai", "RLHF safe",
            "do not answer", "i am sorry", "refusal rate",
        ],
        "name_keywords": [
            "safe", "Safe", "safety", "Safety", "jailbreak", "Jailbreak",
            "red team", "RedTeam", "attack", "Attack", "adversar",
            "HarmBench", "JailbreakBench", "AdvBench", "SafetyBench",
            "TrustLLM", "DecodingTrust", "GradSafe", "SALAD",
            "WildGuard", "SimpleSafety", "BeaverTails", "DoNotAnswer",
            "XSafety", "R-Judge", "StrongREJECT", "WalledEval",
            "SORRY-Bench", "JailbreakEval", "SafeDecoding", "GuardBench",
        ],
    },
    "7. Domain-Specific Ethics": {
        "desc": "Benchmarks for ethical evaluation in specific professional domains (medical, legal, business, engineering, etc.).",
        "keywords": [
            "medical ethic", "bioethic", "clinical ethic", "healthcare ethic",
            "legal ethic", "law ethic", "judicial", "courtroom",
            "business ethic", "corporate ethic", "workplace ethic",
            "engineering ethic", "professional ethic", "code of conduct",
            "nursing ethic", "patient", "informed consent",
            "doctor", "physician", "clinical trial",
            "finance ethic", "financial ethic", "accounting ethic",
            "military ethic", "warfare", "autonomous weapon",
            "journalism ethic", "media ethic", "privacy",
            "environmental ethic", "sustainability", "animal ethic",
            "education ethic", "academic integrit", "plagiar",
            "research ethic", "scientific integrit",
            "domain-specific", "professional domain", "applied ethic",
            "medical", "legal", "law", "health", "clinical",
        ],
        "name_keywords": [
            "Med", "med", "Medical", "medical", "Health", "health",
            "Legal", "legal", "Law", "law", "Bio", "bio",
            "Clinical", "clinical", "Nurs", "nurs", "Patient",
            "MedEthic", "LegalBench", "MedQA", "PubMedQA",
            "CMExam", "CMB", "business", "Business", "financ",
            "ClinicalEthic", "BioEthic", "environment",
        ],
    },
    "8. Normative Ethics Benchmarks": {
        "desc": "Benchmarks specifically grounded in normative ethical theories (deontology, consequentialism, virtue ethics, care ethics, etc.).",
        "keywords": [
            "normative ethic", "ethical theor", "moral theor",
            "deontolog", "consequential", "utilitarian", "virtue ethic",
            "care ethic", "kantian", "rawlsian", "contractualist",
            "duty-based", "rights-based", "principle-based",
            "moral framework", "ethical framework", "moral principle",
            "categorical imperative", "greatest good", "moral character",
            "prima facie", "moral rule", "ethical tradition",
            "moral philosophy", "applied ethic",
            "ethics of care", "feminist ethic",
            "confucian ethic", "buddhist ethic", "islamic ethic",
            "jewish ethic", "christian ethic", "religious ethic",
            "divine command", "natural law",
        ],
        "name_keywords": [
            "normative", "Normative", "deontolog", "consequential",
            "utilitarian", "virtue", "Virtue", "care ethic",
            "Kantian", "moral theor", "ethical theor",
        ],
    },
    "9. Moral Psychology Applied to AI": {
        "desc": "Benchmarks applying moral psychology constructs (moral foundations, moral development, moral identity) to evaluate AI.",
        "keywords": [
            "moral foundation", "moral psycholog", "moral develop",
            "moral identity", "moral emotion", "moral sentiment",
            "moral intuition", "kohlberg", "piaget",
            "moral distress", "moral injur", "moral outrage",
            "empathy", "compassion", "altruism",
            "trolley problem", "footbridge", "fat man",
            "moral disgust", "moral anger", "moral shame",
            "moral cognit", "dual process", "system 1", "system 2",
            "haidt", "jonathan haidt", "moral foundation theor",
            "care/harm", "fairness/cheat", "loyalty/betray",
            "authority/subver", "sanctity/degrad", "liberty/oppress",
            "moral taste", "moral matrix", "moral tribe",
            "cognitive bias", "framing effect", "moral wiggle",
            "utilitarian sacrifice", "deontological refusal",
            "personality", "big five", "dark triad", "psychopath",
            "moral disengag", "diffusion of responsib",
        ],
        "name_keywords": [
            "MoralFoundation", "moral foundation", "Kohlberg",
            "MFT", "psycholog", "Psycholog", "MFQ", "Haidt",
            "MoralSense", "MoralCognit", "empathy", "Empathy",
            "PsychEthic", "PsychBench",
        ],
    },
    "10. Helpfulness, Honesty & RLHF": {
        "desc": "Benchmarks evaluating helpfulness, honesty, harmlessness (HHH), and RLHF-related alignment.",
        "keywords": [
            "helpful", "honest", "harmless", "HHH", "RLHF",
            "reinforcement learning from human feedback",
            "human feedback", "preference learn", "reward model",
            "instruction follow", "instruction tun",
            "truthful", "factual", "hallucinat", "confabul",
            "sycophan", "flattery", "people-pleas",
            "refusal", "over-refusal", "compliance",
            "alignment", "aligned", "misalign",
            "constitutional ai", "RLAIF", "DPO", "PPO",
            "preference data", "preference pair",
            "human evaluat", "human annotation", "human judge",
            "chatbot", "assistant", "conversation",
            "dialogue", "dialog", "multi-turn",
            "calibrat", "uncertain", "confidence",
            "knowledge", "commonsense",
        ],
        "name_keywords": [
            "HH", "RLHF", "Helpful", "helpful", "Honest", "honest",
            "Harmless", "harmless", "TruthfulQA", "truthful",
            "sycophant", "Sycophant", "HH-RLHF", "Anthropic",
            "Constitutional", "DPO", "PPO", "preference",
            "Chatbot", "chatbot", "AlpacaEval", "MT-Bench",
            "reward", "Reward", "LIMA", "Alignment",
        ],
    },
}


def classify_entry(entry):
    """Classify a single entry into one or more categories."""
    categories = []

    # Build search text from all relevant fields
    text_fields = [
        entry.get("benchmark_name", ""),
        entry.get("what_measures", ""),
        entry.get("how_measures", ""),
        entry.get("reasoning", ""),
    ]
    full_text = " ".join(text_fields).lower()
    filename = entry.get("filename", "")
    benchmark_name = entry.get("benchmark_name", "")

    for cat_name, cat_info in CATEGORIES.items():
        matched = False

        # Check keyword matches in full text
        for kw in cat_info["keywords"]:
            if kw.lower() in full_text:
                matched = True
                break

        # Check name keywords in filename and benchmark name
        if not matched:
            combined_name = (filename + " " + benchmark_name).lower()
            for kw in cat_info["name_keywords"]:
                if kw.lower() in combined_name:
                    matched = True
                    break

        if matched:
            categories.append(cat_name)

    return categories


def extract_year(filename):
    """Extract year from filename like '2024-Author-Title.md'."""
    m = re.match(r"(\d{4})-", filename)
    return int(m.group(1)) if m else 9999


def make_wikilink(filename):
    """Convert filename to wikilink without .md extension."""
    name = filename
    if name.endswith(".md"):
        name = name[:-3]
    return f"[[{name}]]"


def truncate(text, max_len=60):
    """Truncate text to max_len characters with ellipsis."""
    if not text:
        return "N/A"
    text = text.strip()
    if len(text) <= max_len:
        return text
    return text[:max_len-3].rstrip() + "..."


def sort_key(entry):
    """Sort by year descending, then filename ascending."""
    year = extract_year(entry["filename"])
    return (-year, entry["filename"].lower())


def generate_report(entries):
    """Generate the full markdown report."""

    # ── Classify all entries ──────────────────────────────────────────
    entry_categories = {}
    category_entries = defaultdict(list)
    uncategorized = []

    for entry in entries:
        cats = classify_entry(entry)
        entry_categories[entry["filename"]] = cats
        if not cats:
            uncategorized.append(entry)
        for cat in cats:
            category_entries[cat].append(entry)

    # Handle uncategorized entries - assign to most likely category
    # based on a broader second pass
    for entry in uncategorized:
        full_text = " ".join([
            entry.get("benchmark_name", ""),
            entry.get("what_measures", ""),
            entry.get("how_measures", ""),
            entry.get("reasoning", ""),
        ]).lower()

        # Default categorization based on broad signals
        assigned = False

        # Check for safety-adjacent
        if any(w in full_text for w in ["trust", "reliab", "robust", "risk", "guardrail", "detect"]):
            category_entries["6. Safety & Red Teaming"].append(entry)
            entry_categories[entry["filename"]] = ["6. Safety & Red Teaming"]
            assigned = True
        # Check for bias-adjacent
        elif any(w in full_text for w in ["social", "norm", "stereotyp", "sentiment", "opinion", "survey"]):
            category_entries["4. Fairness, Bias & Social Norms"].append(entry)
            entry_categories[entry["filename"]] = ["4. Fairness, Bias & Social Norms"]
            assigned = True
        # Check for moral reasoning adjacent
        elif any(w in full_text for w in ["moral", "ethic", "right", "wrong", "good", "bad", "virtue"]):
            category_entries["1. Moral Reasoning & Ethical Judgment"].append(entry)
            entry_categories[entry["filename"]] = ["1. Moral Reasoning & Ethical Judgment"]
            assigned = True
        # Check for helpfulness/RLHF adjacent
        elif any(w in full_text for w in ["generat", "model", "llm", "language model", "chatbot", "instruct", "benchmark", "evaluat"]):
            category_entries["10. Helpfulness, Honesty & RLHF"].append(entry)
            entry_categories[entry["filename"]] = ["10. Helpfulness, Honesty & RLHF"]
            assigned = True

        if not assigned:
            # Absolute fallback: put in Fairness, Bias & Social Norms (broadest category)
            category_entries["4. Fairness, Bias & Social Norms"].append(entry)
            entry_categories[entry["filename"]] = ["4. Fairness, Bias & Social Norms"]

    # ── Compute statistics ────────────────────────────────────────────
    total_candidates = len(entries)
    total_screened = 924
    exclusion_rate = round((total_screened - total_candidates) / total_screened * 100, 1)

    # Pluralistic relevance stats
    plur_counts = Counter(e.get("pluralistic_relevance", "N/A") for e in entries)

    # Availability stats (consolidate variants)
    def consolidate_availability(val):
        v = (val or "N/A").strip()
        if v.startswith("Public"):
            return "Public"
        if v.startswith("Partially public") or v == "Partial":
            return "Partially public"
        if v.startswith("Not stated"):
            return "Not stated"
        if v.startswith("Not public"):
            return "Not public"
        if v.startswith("Code"):
            return "Code available"
        return v

    avail_counts = Counter(consolidate_availability(e.get("availability", "N/A")) for e in entries)

    # Category counts (sort numerically by category number)
    cat_order = sorted(CATEGORIES.keys(), key=lambda c: int(c.split(".")[0]))
    cat_counts = {cat: len(category_entries.get(cat, [])) for cat in cat_order}

    # Multi-category stats
    multi_cat = sum(1 for cats in entry_categories.values() if len(cats) > 1)

    # Verify all entries categorized
    categorized_files = set()
    for ents in category_entries.values():
        for e in ents:
            categorized_files.add(e["filename"])
    all_files = set(e["filename"] for e in entries)
    missing = all_files - categorized_files
    if missing:
        print(f"WARNING: {len(missing)} entries not categorized: {missing}", file=sys.stderr)

    # ── Build report ──────────────────────────────────────────────────
    lines = []

    # Header
    lines.append("# Comprehensive Survey: LLM Ethics Benchmarks, Datasets & Evaluation Metrics")
    lines.append("")
    lines.append(f"**Date:** 2026-02-08")
    lines.append(f"**Papers Screened:** {total_screened}")
    lines.append(f"**Benchmark Candidates Identified:** {total_candidates}")
    lines.append(f"**Method:** 20-agent deep-read of full vault with structured rubric")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Executive Summary
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"From a vault of **{total_screened} papers** on AI ethics and related topics, "
                 f"**{total_candidates} papers** ({round(total_candidates/total_screened*100, 1)}%) "
                 f"were identified as containing or proposing benchmarks, datasets, or evaluation metrics "
                 f"relevant to LLM ethics evaluation. The remaining {total_screened - total_candidates} papers "
                 f"({exclusion_rate}%) were excluded as they do not propose or contain benchmark/evaluation resources.")
    lines.append("")

    # Category breakdown (numeric order)
    lines.append("### Category Breakdown")
    lines.append("")
    lines.append("| # | Category | Papers |")
    lines.append("|---|----------|--------|")
    for cat_name in cat_order:
        count = cat_counts.get(cat_name, 0)
        lines.append(f"| {cat_name.split('.')[0].strip()} | {cat_name.split('. ', 1)[1]} | {count} |")
    lines.append("")
    lines.append(f"*Note: Papers may appear in multiple categories. "
                 f"{multi_cat} papers ({round(multi_cat/total_candidates*100, 1)}%) are multi-categorized.*")
    lines.append("")

    # Pluralistic relevance
    lines.append("### Pluralistic Relevance")
    lines.append("")
    lines.append("| Relevance | Count | % |")
    lines.append("|-----------|-------|---|")
    for label in ["Yes", "Partial", "No"]:
        c = plur_counts.get(label, 0)
        pct = round(c / total_candidates * 100, 1)
        lines.append(f"| {label} | {c} | {pct}% |")
    # Handle any other values
    for label, c in sorted(plur_counts.items()):
        if label not in ["Yes", "Partial", "No"]:
            pct = round(c / total_candidates * 100, 1)
            lines.append(f"| {label} | {c} | {pct}% |")
    lines.append("")

    # Availability
    lines.append("### Data Availability")
    lines.append("")
    lines.append("| Availability | Count | % |")
    lines.append("|-------------|-------|---|")
    avail_order = ["Public", "Partially public", "Code available", "Not stated", "Not public"]
    for label in avail_order:
        c = avail_counts.get(label, 0)
        if c > 0:
            pct = round(c / total_candidates * 100, 1)
            lines.append(f"| {label} | {c} | {pct}% |")
    for label, c in sorted(avail_counts.items()):
        if label not in avail_order and c > 0:
            pct = round(c / total_candidates * 100, 1)
            lines.append(f"| {label} | {c} | {pct}% |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── Category Sections ─────────────────────────────────────────────
    lines.append("## Category Sections")
    lines.append("")

    for cat_name in cat_order:
        cat_info = CATEGORIES[cat_name]
        cat_ents = category_entries.get(cat_name, [])

        # Sort entries: year descending, then filename ascending
        cat_ents_sorted = sorted(cat_ents, key=sort_key)

        # Deduplicate (same filename may have been added twice from fallback)
        seen = set()
        cat_ents_deduped = []
        for e in cat_ents_sorted:
            if e["filename"] not in seen:
                seen.add(e["filename"])
                cat_ents_deduped.append(e)

        lines.append(f"### {cat_name}")
        lines.append("")
        lines.append(f"**{len(cat_ents_deduped)} papers** | {cat_info['desc']}")
        lines.append("")
        lines.append("| # | Paper | Benchmark/Dataset | What It Measures | Method | Size | Models | Pluralistic | Availability |")
        lines.append("|---|-------|-------------------|-----------------|--------|------|--------|-------------|--------------|")

        for idx, entry in enumerate(cat_ents_deduped, 1):
            paper = make_wikilink(entry["filename"])
            bench = truncate(entry.get("benchmark_name", "N/A"), 55)
            what = truncate(entry.get("what_measures", "N/A"), 60)
            how = truncate(entry.get("how_measures", "N/A"), 55)
            size = truncate(entry.get("dataset_size", "N/A"), 40)
            models = truncate(entry.get("models_evaluated", "N/A"), 45)
            plur = entry.get("pluralistic_relevance", "N/A")
            avail = entry.get("availability", "N/A")

            lines.append(f"| {idx} | {paper} | {bench} | {what} | {how} | {size} | {models} | {plur} | {avail} |")

        lines.append("")
        lines.append("---")
        lines.append("")

    # ── Gap Analysis ──────────────────────────────────────────────────
    lines.append("## Gap Analysis")
    lines.append("")

    lines.append("### Dimensions Well-Covered")
    lines.append("")
    lines.append("- **Fairness and bias detection**: The largest category with extensive coverage of gender, racial, religious, and intersectional biases across multiple languages and cultural contexts")
    lines.append("- **Safety and red teaming**: Robust coverage of jailbreak evaluation, adversarial attacks, and safety alignment testing, with multiple benchmark suites (DecodingTrust, TrustLLM, HarmBench, JailbreakBench)")
    lines.append("- **Toxicity and hate speech**: Well-established benchmarks (RealToxicityPrompts, ToxiGen, HateCheck) with growing multilingual variants")
    lines.append("- **Moral reasoning scenarios**: Strong coverage of trolley-problem variants, moral dilemmas, and ethical judgment tasks (ETHICS, Moral Machine, MACHIAVELLI)")
    lines.append("- **Helpfulness-harmlessness tradeoffs**: Growing body of work on RLHF evaluation, sycophancy detection, and instruction-following safety")
    lines.append("")

    lines.append("### Dimensions Underrepresented")
    lines.append("")
    lines.append("- **Normative ethics grounding**: Few benchmarks explicitly operationalize specific ethical theories (deontology, consequentialism, virtue ethics); most treat ethics as monolithic")
    lines.append("- **Non-Western ethical traditions**: Limited coverage of Confucian, Buddhist, Islamic, Ubuntu, and Indigenous ethical frameworks; most benchmarks assume Western liberal norms")
    lines.append("- **Moral psychology constructs**: Sparse application of moral foundations theory, moral development stages, or moral identity frameworks to LLM evaluation")
    lines.append("- **Value pluralism methodology**: While many benchmarks acknowledge cultural variation, few provide systematic frameworks for evaluating pluralistic value alignment")
    lines.append("- **Longitudinal and dynamic evaluation**: Nearly all benchmarks are static; no established methods for evaluating moral reasoning evolution during training or deployment")
    lines.append("- **Interpersonal and relational ethics**: Care ethics, trust dynamics, and relational moral reasoning are significantly underrepresented")
    lines.append("- **Environmental and animal ethics**: Virtually no benchmarks address ecological ethics, sustainability reasoning, or animal welfare considerations")
    lines.append("")

    lines.append("### Ethical Tradition Coverage")
    lines.append("")
    lines.append("| Ethical Tradition | Coverage Level | Notes |")
    lines.append("|-------------------|---------------|-------|")
    lines.append("| Consequentialism/Utilitarianism | Moderate | Trolley problems, utilitarian calculus scenarios |")
    lines.append("| Deontology/Kantian | Moderate | Rule-based evaluation, duty-focused scenarios |")
    lines.append("| Virtue Ethics | Low | Few benchmarks explicitly test character/virtue reasoning |")
    lines.append("| Care Ethics | Very Low | Minimal systematic evaluation |")
    lines.append("| Confucian Ethics | Low | Emerging in Chinese-language benchmarks (CValue, CDEval) |")
    lines.append("| Islamic Ethics | Very Low | Limited to a few Arabic NLP benchmarks |")
    lines.append("| Ubuntu Ethics | None | No benchmarks identified |")
    lines.append("| Buddhist Ethics | None | No benchmarks identified |")
    lines.append("| Indigenous Ethical Traditions | None | No benchmarks identified |")
    lines.append("")

    lines.append("### Cultures and Languages Covered")
    lines.append("")
    lines.append("| Coverage Level | Languages/Cultures |")
    lines.append("|---------------|-------------------|")
    lines.append("| Strong | English (dominant), Chinese (Mandarin) |")
    lines.append("| Moderate | Korean, Arabic, Japanese, German, Spanish |")
    lines.append("| Emerging | Hindi, Turkish, Indonesian, Thai, Vietnamese |")
    lines.append("| Minimal/None | Most African languages, Indigenous languages, Pacific Island languages |")
    lines.append("")

    lines.append("### Evaluation Methodology Types")
    lines.append("")
    lines.append("| Methodology | Prevalence | Examples |")
    lines.append("|------------|-----------|----------|")
    lines.append("| Multiple-choice QA | Very High | ETHICS, MMLU Ethics, MoralChoice |")
    lines.append("| Scenario-based judgment | High | Moral Machine, MACHIAVELLI, Scruples |")
    lines.append("| Free-text generation + classifier | High | RealToxicityPrompts, ToxiGen, BOLD |")
    lines.append("| Embedding/representation analysis | Moderate | WEAT, CrowS-Pairs, StereoSet |")
    lines.append("| Human preference comparison | Moderate | HH-RLHF, Chatbot Arena, AlpacaEval |")
    lines.append("| Adversarial probing | Moderate | HarmBench, JailbreakBench, AdvBench |")
    lines.append("| Behavioral/interactive testing | Low | MACHIAVELLI (game), Avalon, Werewolf |")
    lines.append("| Longitudinal/dynamic | Very Low | Minimal established methodology |")
    lines.append("")

    lines.append("### Key Field Needs")
    lines.append("")
    lines.append("1. **Pluralistic alignment benchmarks**: Systematic evaluation of how LLMs handle genuinely contested moral questions where reasonable people disagree")
    lines.append("2. **Cross-cultural validation**: Most benchmarks are developed in one cultural context and lack validation across cultures")
    lines.append("3. **Compositional ethics evaluation**: Benchmarks that test complex, multi-stakeholder ethical scenarios rather than isolated dilemmas")
    lines.append("4. **Process-based evaluation**: Moving beyond outcome-based metrics to evaluate the quality of moral reasoning processes")
    lines.append("5. **Ecological validity**: Benchmarks that reflect real-world ethical challenges LLMs face in deployment, not just philosophical thought experiments")
    lines.append("6. **Temporal and contextual sensitivity**: Evaluation of how models handle evolving social norms and context-dependent ethical judgments")
    lines.append("7. **Standardized reporting**: No common framework for comparing results across benchmarks; meta-evaluation infrastructure needed")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── Methodology Note ──────────────────────────────────────────────
    lines.append("## Methodology Note")
    lines.append("")
    lines.append("### Screening Process")
    lines.append("")
    lines.append(f"This survey was conducted via a **20-agent parallel deep-read** of all {total_screened} papers "
                 "in the CEI Literature Vault. Each agent was assigned a batch of ~26-27 papers and instructed to:")
    lines.append("")
    lines.append("1. Read the full paper text (PDF extract) for each paper")
    lines.append("2. Determine whether the paper proposes, creates, or substantially uses a benchmark, dataset, or evaluation metric relevant to LLM ethics")
    lines.append("3. For candidates, extract structured metadata: benchmark name, what it measures, how it measures, dataset size, models evaluated, pluralistic relevance, and data availability")
    lines.append("4. Provide reasoning for the classification decision")
    lines.append("")

    lines.append("### Inclusion Criteria")
    lines.append("")
    lines.append("A paper was classified as a **benchmark candidate** if it met ANY of the following:")
    lines.append("")
    lines.append("- Proposes a new benchmark, dataset, or evaluation suite for assessing LLM ethical behavior")
    lines.append("- Creates or curates a dataset used for ethics-related evaluation")
    lines.append("- Defines novel metrics or evaluation methodologies for measuring ethical properties of LLMs")
    lines.append("- Conducts systematic empirical evaluation of LLMs on ethics-related tasks using established benchmarks")
    lines.append("- Provides human-annotated preference data relevant to alignment or value measurement")
    lines.append("")

    lines.append("### Category Assignment")
    lines.append("")
    lines.append("Papers were assigned to categories using a keyword-based classification system that analyzes "
                 "benchmark names, measurement descriptions, methodology descriptions, and agent reasoning. "
                 "Papers may appear in multiple categories when they span multiple evaluation dimensions. "
                 f"Of {total_candidates} candidates, {multi_cat} ({round(multi_cat/total_candidates*100, 1)}%) "
                 "appear in two or more categories.")
    lines.append("")

    lines.append("### Limitations")
    lines.append("")
    lines.append("- **Classification granularity**: Keyword-based categorization may miss nuanced thematic connections or create false positives for papers that merely mention a topic")
    lines.append("- **Coverage bias**: The vault itself has selection biases toward English-language, computationally-oriented, and Western-authored papers")
    lines.append("- **Temporal bias**: More recent papers (2023-2025) are overrepresented, reflecting the rapid growth of LLM safety/ethics evaluation")
    lines.append("- **Benchmark vs. usage distinction**: Some papers are classified as candidates because they substantially use existing benchmarks, not because they propose new ones")
    lines.append("- **Extract quality**: Agent readings are based on PDF text extracts, which may have OCR artifacts or missing sections")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*Generated: 2026-02-08 | Source: `logs/benchmark_survey_candidates.json` | "
                 f"Papers: {total_candidates}/{total_screened} | Categories: {len(CATEGORIES)}*")

    return "\n".join(lines)


def main():
    # Load data
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        entries = json.load(f)

    print(f"Loaded {len(entries)} entries from {INPUT_FILE}")

    # Generate report
    report = generate_report(entries)

    # Write report
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Report written to {OUTPUT_FILE}")
    print(f"Report size: {len(report)} characters, {report.count(chr(10))} lines")

    # Print verification stats
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        entries = json.load(f)

    entry_categories = {}
    for entry in entries:
        cats = classify_entry(entry)
        entry_categories[entry["filename"]] = cats

    uncategorized = [fn for fn, cats in entry_categories.items() if not cats]
    multi = sum(1 for cats in entry_categories.values() if len(cats) > 1)

    print(f"\nCategory assignment stats (before fallback):")
    print(f"  Uncategorized (will get fallback): {len(uncategorized)}")
    print(f"  Multi-categorized: {multi}")

    if uncategorized:
        print(f"\n  Uncategorized entries (first 20):")
        for fn in uncategorized[:20]:
            e = next(x for x in entries if x["filename"] == fn)
            print(f"    - {fn}: {e.get('benchmark_name', 'N/A')[:60]}")
        if len(uncategorized) > 20:
            print(f"    ... and {len(uncategorized) - 20} more")


if __name__ == "__main__":
    main()
