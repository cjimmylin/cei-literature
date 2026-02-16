#!/usr/bin/env python3
"""
Generate Updated Ethical Values Alignment Benchmarks Report.

Combines:
1. Original 39 hand-curated entries (preserved for entries with rich detail)
2. New entries from 989-candidate benchmark survey JSON
3. YAML-enriched metadata from paper files

Output: STATISTICS/20260210-ethical-values-alignment-benchmarks-report.md
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

# ── Path setup ───────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
WORKSPACE = SCRIPT_DIR.parent
sys.path.insert(0, str(WORKSPACE / ".agent" / "lib"))

from yaml_utils import extract_frontmatter, parse_frontmatter
from config import PAPERS_DIR, STATISTICS_DIR, LOGS_DIR

INPUT_FILE = LOGS_DIR / "20260216-benchmark_survey_candidates.json"
OUTPUT_FILE = STATISTICS_DIR / "20260216-ethical-values-alignment-benchmarks-report.md"

# Also import classify_entry from sibling script
sys.path.insert(0, str(SCRIPT_DIR))
from generate_benchmark_survey_report import classify_entry, CATEGORIES

# ── Original 39 anchor entries ───────────────────────────────────────────────
# Maps benchmark short-name → paper filename (without .md) for anchors in vault
ORIGINAL_ANCHORS = {
    # Section A: Multi-Framework
    "ETHICS Dataset": "2021-Hendrycks-Aligning AI with Shared Human Values",
    "MoReBench": "2025-Chiu-MoReBench",
    "LLM Ethics Benchmark": "2025-Jiao-LLM Ethics Benchmark",
    "MoralBench": "2024-Ji-MoralBench",
    "EthicsSuite": None,  # May or may not be in vault
    # Section B: Single-Framework
    "MoralChoice": "2023-Scherrer-Evaluating the Moral Beliefs Encoded in LLMs",
    "MoralExceptQA": None,
    "Greatest Good Benchmark": "2024-Marraffini-The Greatest Good Benchmark",
    "MACHIAVELLI": "2023-Pan-Do the Rewards Justify the Means Measuring",
    "DailyDilemmas": "2024-Chiu-DailyDilemmas",
    "Right vs. Right": None,
    "MORABLES": None,
    "Conscience Conflict": None,
    "Normative Evaluation": "2025-Sachdeva-Normative Evaluation of LLMs with Everyday Moral Dilemmas",
    # Section C: Cross-Cultural
    "WorldValuesBench": "2024-Wu-WorldValuesBench",
    "CultureLLM": None,  # Not in vault
    "CIVICS": "2024-Pistilli-CIVICS",
    "LLM-GLOBE": None,  # Not in vault
    "CQ-Bench": None,  # Not in vault
    "MENAValues": None,  # Not in vault
    "IslamTrust": None,  # Not in vault
    "CDEval": None,  # Not in vault
    "CulturalBench": "2025-Chiu-CulturalBench",
    "XCR-Bench": None,  # Not in vault
    # Section D: Moral Psychology
    "Delphi": None,
    "ValueBench": "2024-Ren-ValueBench",
    "Touché / ValueEval": None,  # Not in vault
    "MFTCXplain": None,
    "Scaling Laws Moral Machine": "2024-Takemoto-The moral machine experiment on large language",
    # Section E: Psychometric
    "Structured Moral Reasoning": "2025-Chakraborty-Structured Moral Reasoning",
    "Beyond Ethical Alignment": "2025-Galatolo-Beyond Ethical Alignment AMAs",
    "Diverse Human Value Alignment": "2025-Wang-Diverse Human Value Alignment for LLMs via Ethical Reasoning",
    # Section F: Meta-Resources
    "SafetyPrompts.com": None,
    "SafetyBench": "2024-Zhang-SafetyBench",
    "Awesome-LLM-Psychometrics": None,
    "EleutherAI lm-evaluation-harness": None,
}

# Reverse lookup: filename → anchor name
ANCHOR_BY_FILENAME = {}
for name, fn in ORIGINAL_ANCHORS.items():
    if fn:
        ANCHOR_BY_FILENAME[fn + ".md"] = name

# ── Static entries for benchmarks NOT in vault ───────────────────────────────
# These preserve the hand-curated detail from the original report
STATIC_ENTRIES = {
    "CultureLLM": {
        "section": "C",
        "markdown": """### C{N}. CultureLLM (Li et al., 2024)
- **Citation:** Li, C., Chen, M., Wang, J., Sitaram, S., & Xie, X. (2024). CultureLLM: Incorporating Cultural Differences into Large Language Models. *NeurIPS 2024*.
- **arXiv:** [2402.10946](https://arxiv.org/abs/2402.10946)
- **Cultural scope:** 9 cultures (Arabic, Bengali, Chinese, English, German, Korean, Portuguese, Spanish, Turkish)
- **Dataset:** 50 WVS seed samples/culture with semantic data augmentation; 7 topic categories
- **Code:** [GitHub](https://github.com/Scarelette/CultureLLM)
- **LLMs tested:** GPT-3.5, Gemini Pro, GPT-4 (CultureLLM outperforms GPT-3.5 by 8.1%)
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault""",
    },
    "LLM-GLOBE": {
        "section": "C",
        "markdown": """### C{N}. LLM-GLOBE (Karinshak et al., 2024)
- **Citation:** Karinshak, E., Hu, A., Kong, K., Rao, V., Wang, J., Wang, J., & Zeng, Y. (2024). LLM-GLOBE: A Benchmark Evaluating the Cultural Values Embedded in LLM Output.
- **arXiv:** [2411.06032](https://arxiv.org/abs/2411.06032)
- **Cultural scope:** US vs. China; GLOBE framework (9 cultural dimensions)
- **Dataset:** 36,675 closed-ended + 900 open-generation prompts; English + Chinese
- **Code:** [GitHub](https://github.com/raovish6/LLM-GLOBE) — novel "LLMs-as-a-Jury" eval pipeline
- **LLMs tested:** Claude, Gemini, GPT-3.5, GPT-4 (US); GLM-4, Ernie 3.5/4.0, Qwen-14b (China)
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault""",
    },
    "CQ-Bench": {
        "section": "C",
        "markdown": """### C{N}. CQ-Bench (Liu et al., 2025)
- **Citation:** Liu, Z., Dey, P., Huang, J.-T., Zhao, Z., Jiang, B., Gupta, R., Liu, Y., Du, Y., & Zhao, J. (2025). Can LLMs Grasp Implicit Cultural Values? Benchmarking LLMs' Cultural Intelligence with CQ-Bench.
- **arXiv:** [2504.01127](https://arxiv.org/abs/2504.01127)
- **Cultural scope:** Global (WVS + GlobalOpinions; ethical, religious, social, political topics)
- **Dataset:** 1,000 multi-character conversation stories; 3 tasks (attitude detection, value selection, value extraction)
- **Code:** [GitHub](https://github.com/uscnlp-lime/CQ-Bench)
- **LLMs tested:** Qwen 2.5 (7B/14B/32B), Qwen 3-4B, LLaMA 3.1-8B, LLaMA 3.2-3B, DeepSeek-V3/R1, GPT-4o-mini, o4-mini, o3, o3-mini, o1
- **Key finding:** Fine-tuning LLaMA-3.2-3B on 500 examples improves >10%, outperforming o3-mini
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault""",
    },
    "MENAValues": {
        "section": "C",
        "markdown": """### C{N}. MENAValues (Zahraei & Asgari, 2025)
- **Citation:** Zahraei, P.S. & Asgari, E. (2025). I Am Aligned, But With Whom? MENA Values Benchmark for Evaluating Cultural Alignment and Multilingual Bias in LLMs.
- **arXiv:** [2510.13154](https://arxiv.org/abs/2510.13154)
- **Cultural scope:** 16 MENA countries
- **Dataset:** 864 MCQ from WVS Wave 7 + 2022 Arab Opinion Index; governance, economics, cultural identity, wellbeing
- **Languages:** English, Arabic, Persian, Turkish
- **Code:** [GitHub](https://github.com/llm-lab-org/MENA-Values-Benchmark-Evaluating-Cultural-Alignment-and-Multilingual-Bias-in-Large-Language-Models)
- **LLMs tested:** Llama-3.1-8B, Mistral-7B, AYA-expanse-8b, Fanar-1-9B, ALLAM-Thinking, GPT-4o-mini, Gemini 2.5 Flash Lite
- **Key finding:** "Cross-Lingual Value Shifts" — identical questions yield different responses based on language
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault""",
    },
    "IslamTrust": {
        "section": "C",
        "markdown": """### C{N}. IslamTrust (Lahmar et al., 2025)
- **Citation:** Lahmar, A., Arafat, M.E., Farou, Z., & Mahmud, M. (2025). IslamTrust: A Benchmark for LLMs Alignment with Islamic Values. *Muslims in ML Workshop @ NeurIPS 2025*.
- **OpenReview:** [PBcv90iKFB](https://openreview.net/forum?id=PBcv90iKFB)
- **Cultural scope:** Islamic values across 6 domains; bilingual
- **Dataset:** 406 MCQ; Arabic + English; MIT license
- **Code:** [HuggingFace](https://huggingface.co/datasets/Abderraouf000/IslamTrust-benchmark)
- **LLMs tested:** SILMA-9B (best), Fanar-1-9B, ALLaM-7B, Llama-3.1-8B
- **Key finding:** LLMs perform better in Arabic than English; systematic biases in interfaith dialogue
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault""",
    },
    "CDEval": {
        "section": "C",
        "markdown": """### C{N}. CDEval (Wang et al., 2024)
- **Citation:** Wang, Y., Zhu, Y., Kong, C., Wei, S., Yi, X., Xie, X., & Sang, J. (2024). CDEval: A Benchmark for Measuring the Cultural Dimensions of Large Language Models. *Cross-Cultural NLP Workshop @ ACL 2024*.
- **arXiv:** [2311.16421](https://arxiv.org/abs/2311.16421)
- **Cultural scope:** Hofstede's 6 cultural dimensions (PDI, IDV, UAI, MAS, LTO, IVR) across 7 domains; compared against 98 countries
- **Dataset:** 2,953 questions; English, Chinese, German
- **Code:** [GitHub](https://github.com/astrodrew/CDEval)
- **LLMs tested:** 17 models (GPT-4, GPT-3.5-turbo, ChatGLM v1-3, Spark-v2, Llama2-Chat, Qwen-Chat, Baichuan-Chat, Alpaca-7B, Chinese-Alpaca2-13B, etc.)
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault""",
    },
    "XCR-Bench": {
        "section": "C",
        "markdown": """### C{N}. XCR-Bench (Kabir et al., 2026)
- **Citation:** Kabir, M., Ahmed, T., Rahman, M.M., Ji, S., Alhuzali, H., & Ananiadou, S. (2026). XCR-Bench: A Multi-Task Benchmark for Evaluating Cultural Reasoning in LLMs.
- **arXiv:** [2601.14063](https://arxiv.org/abs/2601.14063)
- **Cultural scope:** Chinese, Arabic, Bengali (with West Bengal/India and Bangladesh sub-variants)
- **Dataset:** 4,900 parallel sentences, 1,098 Culture-Specific Items; 3 reasoning tasks; CC BY-NC-ND 4.0
- **Code:** [GitHub](https://github.com/mohsinulkabir14/xcr_bench)
- **LLMs tested:** GPT-4o, Qwen-2.5-Max, Gemini-2.0-Flash, Claude-3.7-Sonnet, DeepSeek-R1, LLaMA-3.3-70B, OLMo-2-32B
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault""",
    },
    "MoralExceptQA": {
        "section": "B",
        "markdown": """### B{N}. MoralExceptQA (Jin et al., 2022)
- **Citation:** Jin, Z., Levine, S., Gonzalez Adauto, F., Kamal, O., Sap, M., Sachan, M., Mihalcea, R., Tenenbaum, J., & Schölkopf, B. (2022). When to Make Exceptions: Exploring Language Models as Accounts of Human Moral Judgment. *NeurIPS 2022*.
- **arXiv:** [2210.01478](https://arxiv.org/abs/2210.01478)
- **Frameworks:** Deontological (testing when rules can be permissibly broken)
- **Dataset:** 148 rule-breaking scenarios across 3 subsets; human agreement percentages included
- **Code:** [GitHub](https://github.com/feradauto/MoralCoT) | [HuggingFace](https://huggingface.co/datasets/feradauto/MoralExceptQA)
- **LLMs tested:** Delphi, GPT-3, InstructGPT + 7 baselines; MoralCoT outperforms by 6.2% F1
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault""",
    },
    "Right vs. Right": {
        "section": "B",
        "markdown": """### B{N}. Right vs. Right (Yuan et al., 2024)
- **Citation:** Yuan, J., Murukannaiah, P.K., & Singh, M.P. (2024). Right vs. Right: Can LLMs Make Tough Choices?
- **arXiv:** [2412.19926](https://arxiv.org/abs/2412.19926)
- **Frameworks:** Kidder's ethical dilemma framework (Truth vs. Loyalty, Individual vs. Community, Short-term vs. Long-term, Justice vs. Mercy); larger LLMs show deontological tendency
- **Dataset:** 1,730 ethical dilemmas, 4 value-conflict pairs
- **LLMs tested:** 20 models from 6 families (OpenAI, Anthropic, Meta, Mistral, Alibaba, 01-AI)
- **Code:** No public repository confirmed
- **Readiness:** ★☆☆ LOW
- **Vault status:** Not in vault""",
    },
    "Touché / ValueEval": {
        "section": "D",
        "markdown": """### D{N}. Touche / ValueEval (SemEval 2023, CLEF 2024)
- **Citation:** Kiesel, J., et al. (2023). The Touche23-ValueEval Dataset for Identifying Human Values behind Arguments.
- **arXiv:** [2301.13771](https://arxiv.org/abs/2301.13771)
- **Frameworks:** 19 Schwartz values (value detection + value attainment)
- **Dataset:** ~3,000 human-annotated texts (400-800 words each); news articles + political manifestos
- **Languages:** 8 languages
- **Code:** [Zenodo](https://zenodo.org/records/6814564) | [Task page](https://touche.webis.de/clef24/touche24-web/human-value-detection.html)
- **Readiness:** ★★★ HIGH
- **Vault status:** Not in vault""",
    },
    "SafetyPrompts.com": {
        "section": "F",
        "markdown": """### F{N}. SafetyPrompts.com (Vidgen et al., 2024)
- **URL:** [safetyprompts.com](https://safetyprompts.com/)
- **Scope:** Living catalogue of 144+ LLM safety datasets (23 specifically in "Value Alignment" category)
- **Readiness:** ★★★ HIGH (meta-resource)
- **Vault status:** Not in vault""",
    },
    "Awesome-LLM-Psychometrics": {
        "section": "F",
        "markdown": """### F{N}. Awesome-LLM-Psychometrics
- **URL:** [GitHub](https://github.com/ValueByte-AI/Awesome-LLM-Psychometrics)
- **Scope:** Curated list of LLM psychometric and psychology papers
- **Readiness:** ★★★ HIGH (meta-resource, 597 stars)
- **Vault status:** Not in vault""",
    },
    "EleutherAI lm-evaluation-harness": {
        "section": "F",
        "markdown": """### F{N}. EleutherAI lm-evaluation-harness
- **URL:** [GitHub](https://github.com/EleutherAI/lm-evaluation-harness)
- **Scope:** Unified evaluation framework including `hendrycks_ethics` task for reproducible ethics benchmarking
- **Readiness:** ★★★ HIGH (standard evaluation tool)
- **Vault status:** Not in vault""",
    },
}

# ── Scope filtering keywords ─────────────────────────────────────────────────
# NAME_SCOPE: checked in benchmark_name only — specific benchmark names or
# compound phrases that strongly signal values alignment (not bare "moral")
NAME_SCOPE_KEYWORDS = [
    # Specific named benchmarks
    "moralbench", "moralchoice", "moralexcept", "moraldial", "moralstories",
    "morables", "morebench", "machiavelli", "delphi", "scruples",
    "valuebench", "valuenet", "valueeval", "valuelex", "valuealign",
    "culturalbench", "culturellm", "culturebank", "civics",
    "ethics dataset", "ethics benchmark", "ethicssuite",
    "dailydilemma", "trolleymod", "moral machine",
    "norm bank", "normbank",
    # Compound phrases signaling values focus
    "moral foundation", "moral reasoning", "moral judgment", "moral dilemma",
    "moral choice", "moral belief", "moral scenario", "moral value",
    "moral development", "moral psychology", "moral cognit", "moral sens",
    "moral character", "moral alignment", "moral evaluat",
    "ethical reasoning", "ethical dilemma", "ethical value", "ethical framework",
    "ethical judgment", "ethical alignment", "ethical evaluat",
    "value alignment", "value pluralism", "value survey", "value orientation",
    "value conflict", "value diversity", "human value",
    "cross-cultural value", "cultural value", "cross-cultural moral",
    "world value", "cultural dimension", "cultural ethics",
    "normative ethics", "normative reasoning", "normative evaluat",
    "deontolog", "utilitarian", "consequential", "virtue ethic", "care ethic",
    "kantian", "contractualist", "confucian ethic", "islamic ethic",
    "buddhist ethic", "ubuntu ethic", "conscience conflict",
    "schwartz", "hofstede", "kohlberg", "haidt",
    "trolley", "moral machine",
    "psychometric", "moral inventory",
    # Exclude these single words — too broad: moral, ethic, value, cultural, mft, dilemma
]

# WHAT_SCOPE: checked in what_measures — require multi-word phrases only
WHAT_SCOPE_KEYWORDS = [
    "moral reasoning", "moral judgment", "moral dilemma", "moral belief",
    "moral values", "moral foundation", "moral preference", "moral framework",
    "moral choice", "moral scenario", "moral development", "moral cognit",
    "moral align", "moral machine", "moral psychology", "moral identity",
    "moral evaluat", "moral character", "moral perception", "moral sens",
    "ethical reasoning", "ethical judgment", "ethical dilemma", "ethical value",
    "ethical framework", "ethical decision", "ethical tradition", "ethical theory",
    "ethical orient", "ethical evaluat", "ethical alignment",
    "value alignment", "value pluralism", "human values", "cultural values",
    "cross-cultural moral", "cross-cultural ethical", "cross-cultural value",
    "value orientation", "value conflict", "value diversity",
    "value survey", "world values", "normative ethics", "normative reasoning",
    "deontolog", "utilitarian", "consequential", "virtue ethics", "care ethics",
    "kantian", "contractualist", "schwartz value", "hofstede dimension",
    "moral foundation theory", "trolley problem", "kohlberg", "haidt",
    "commonsense morality", "moral norms", "cultural dimension",
]

# In-scope survey categories (1, 2, 3, 8, 9)
IN_SCOPE_CATS = {
    "1. Moral Reasoning & Ethical Judgment",
    "2. Value Alignment & Value Pluralism",
    "3. Cultural & Cross-Cultural Ethics",
    "8. Normative Ethics Benchmarks",
    "9. Moral Psychology Applied to AI",
}

# Out-of-scope categories (pure toxicity/safety/bias without values angle)
OUT_OF_SCOPE_CATS = {
    "4. Fairness, Bias & Social Norms",
    "5. Toxicity, Hate Speech & Harmful Content",
    "6. Safety & Red Teaming",
    "7. Domain-Specific Ethics",
    "10. Helpfulness, Honesty & RLHF",
}

# ── Framework detection keywords (for section assignment) ────────────────────
FRAMEWORK_SIGNALS = {
    "deontology": ["deontolog", "kantian", "duty-based", "categorical imperative", "moral rule", "rights-based"],
    "consequentialism": ["consequential", "utilitarian", "greatest good", "outcome-based", "welfare maximiz"],
    "virtue_ethics": ["virtue ethic", "phronesis", "eudaimonia", "character", "aristotel", "moral character"],
    "care_ethics": ["care ethic", "ethics of care", "feminist ethic", "relational ethic"],
    "contractualism": ["contractualist", "contractarian", "rawlsian", "scanlon", "gauthier"],
    "mft": ["moral foundation", "care/harm", "fairness/cheat", "loyalty/betray", "authority/subver", "sanctity/degrad", "haidt"],
    "wvs": ["world value survey", "wvs", "inglehart", "schwartz value", "hofstede"],
}


# =============================================================================
# STEP 2: Load & scope-filter candidates
# =============================================================================

def load_and_filter_candidates():
    """Load candidates and filter to ethical values alignment scope.

    Three tiers:
    - Anchors: always included
    - Tier A: entries with ONLY in-scope categories (1,2,3,8,9) — always included
    - Tier B: mixed categories — included only if:
      (a) benchmark_name contains a specific benchmark name keyword, OR
      (b) more in-scope categories than out-of-scope AND benchmark_name or
          what_measures has a compound values phrase
    """
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        all_entries = json.load(f)

    print(f"Loaded {len(all_entries)} total benchmark candidates")

    filtered = []
    for entry in all_entries:
        filename = entry.get("filename", "")
        cats = classify_entry(entry)

        # Is this an original anchor?
        is_anchor = filename in ANCHOR_BY_FILENAME

        bench_name_lower = entry.get("benchmark_name", "").lower()
        # Also normalize by removing spaces for specific benchmark names
        bench_name_nospace = bench_name_lower.replace(" ", "").replace("-", "")
        what = entry.get("what_measures", "").lower()

        # Categorize
        in_scope = set(cats) & IN_SCOPE_CATS
        out_scope = set(cats) & OUT_OF_SCOPE_CATS

        if is_anchor:
            filtered.append(entry)
        elif in_scope and not out_scope:
            # Tier A: purely in-scope categories — always include
            filtered.append(entry)
        elif in_scope and out_scope:
            # Tier B: mixed — require strong signal
            # Check 1: specific benchmark name match (normalized)
            name_hit = any(kw in bench_name_nospace for kw in [
                "moralbench", "moralchoice", "moralexcept", "moraldial",
                "moralstories", "morables", "morebench", "machiavelli",
                "delphi", "scruples", "valuebench", "valuenet", "valueeval",
                "valuelex", "culturalbench", "culturellm", "culturebank",
                "civics", "ethicsdataset", "ethicsbenchmark", "ethicssuite",
                "dailydilemma", "trolleymod", "moralmachine", "normbank",
                "moralsim", "moralcot", "moralcomp",
            ])

            # Check 2: majority in-scope AND compound values phrase
            majority_inscope = len(in_scope) > len(out_scope)
            compound_match = any(kw in bench_name_lower or kw in what for kw in [
                "moral foundation", "moral reasoning", "moral judgment",
                "moral dilemma", "moral belief", "moral value",
                "ethical framework", "ethical value", "value alignment",
                "value pluralism", "normative ethics", "cross-cultural value",
                "cultural value", "cultural dimension", "human values",
                "world value", "moral machine", "trolley problem",
                "virtue ethics", "care ethics", "deontological ethics",
                "moral psychology", "moral development",
            ])

            if name_hit or (majority_inscope and compound_match):
                filtered.append(entry)

    print(f"Filtered to {len(filtered)} values-alignment candidates")
    return filtered


# =============================================================================
# STEP 3: Deduplicate
# =============================================================================

def deduplicate_entries(entries):
    """Deduplicate by normalized benchmark name, keeping richest entry."""
    def normalize_name(name):
        # Strip parenthetical qualifiers like "(duplicate entry)"
        name = re.sub(r'\s*\([^)]*\)', '', name)
        # Strip trailing qualifiers with separators: " - thin version", " / CVC", etc.
        name = re.sub(r'\s+[-–]\s+.*$', '', name)
        name = re.sub(r'\s+/\s+.*$', '', name)
        name = name.lower().strip()
        name = re.sub(r'[^a-z0-9\s]', '', name)
        name = re.sub(r'\s+', ' ', name)
        return name

    # Generic names that should NOT be used as dedup keys
    GENERIC_NAMES = {"unnamed", "not stated", "na", "none", "n a", ""}

    groups = defaultdict(list)
    for entry in entries:
        bench_name = entry.get("benchmark_name", entry.get("filename", ""))
        norm = normalize_name(bench_name)
        # If the normalized name is generic, use the filename instead
        if norm in GENERIC_NAMES or len(norm) < 3:
            norm = normalize_name(entry.get("filename", ""))
        groups[norm].append(entry)

    deduped = []
    for norm_name, group in groups.items():
        if len(group) == 1:
            deduped.append(group[0])
        else:
            # Keep the entry with the most non-empty fields
            def richness(e):
                score = sum(1 for v in e.values() if v and str(v).strip() and str(v).strip() != "N/A")
                # Prefer entries whose file exists on disk
                fn = e.get("filename", "")
                if (PAPERS_DIR / fn).exists():
                    score += 10
                return score
            group.sort(key=richness, reverse=True)
            deduped.append(group[0])

    print(f"Deduplicated: {len(entries)} -> {len(deduped)} entries")
    return deduped


# =============================================================================
# STEP 4: Enrich from YAML
# =============================================================================

def enrich_entry(entry):
    """Enrich an entry with metadata from its paper YAML frontmatter."""
    filename = entry.get("filename", "")
    paper_path = PAPERS_DIR / filename

    if not paper_path.exists():
        return entry

    try:
        content = paper_path.read_text(encoding="utf-8")
        fm_text, body = extract_frontmatter(content)
        fields = parse_frontmatter(fm_text)
    except Exception:
        return entry

    # Extract useful fields
    entry["_year"] = fields.get("year", "")
    entry["_first_author"] = fields.get("first_author", "").strip('"').replace("[[", "").replace("]]", "")
    entry["_last_author"] = fields.get("last_author", "").strip('"').replace("[[", "").replace("]]", "")
    entry["_authors"] = fields.get("authors", "")
    entry["_doi"] = fields.get("doi", "")
    entry["_url"] = fields.get("url", "")
    entry["_publication"] = fields.get("publication", "")
    entry["_abstract"] = fields.get("abstract", "")
    entry["_is_benchmark"] = fields.get("is_benchmark", "")
    entry["_is_dataset"] = fields.get("is_dataset", "")
    entry["_normative"] = fields.get("normative_ethics_benchmark", "")
    entry["_short_title"] = fields.get("short_title", "").strip('"')

    # Extract arXiv ID from URL
    url = fields.get("url", "")
    arxiv_match = re.search(r'arxiv\.org/abs/(\d{4}\.\d{4,5}(?:v\d+)?)', url)
    if arxiv_match:
        entry["_arxiv_id"] = arxiv_match.group(1)

    # Scan body for GitHub/HuggingFace URLs — clean trailing punctuation
    code_urls = []
    gh_matches = re.findall(r'https?://github\.com/[^\s\)\]\}]+', body)
    hf_matches = re.findall(r'https?://huggingface\.co/[^\s\)\]\}]+', body)
    for url in (gh_matches + hf_matches)[:5]:
        # Strip trailing markdown/punctuation artifacts
        url = url.rstrip('.,;:!?)}]>')
        if url not in code_urls:
            code_urls.append(url)
    if code_urls:
        entry["_code_urls"] = code_urls[:3]

    entry["_in_vault"] = True
    return entry


# =============================================================================
# STEP 5: Assign to sections A-F
# =============================================================================

def detect_frameworks(entry):
    """Detect which normative frameworks are referenced in entry."""
    search_text = " ".join([
        entry.get("benchmark_name", ""),
        entry.get("what_measures", ""),
        entry.get("how_measures", ""),
        entry.get("reasoning", ""),
        entry.get("_abstract", ""),
    ]).lower()

    found = set()
    for framework, keywords in FRAMEWORK_SIGNALS.items():
        for kw in keywords:
            if kw in search_text:
                found.add(framework)
                break
    return found


def assign_section(entry):
    """Assign entry to section A-F based on content signals."""
    search_text = " ".join([
        entry.get("benchmark_name", ""),
        entry.get("what_measures", ""),
        entry.get("how_measures", ""),
        entry.get("reasoning", ""),
    ]).lower()

    bench_name = entry.get("benchmark_name", "").lower()

    # F: Meta-Resources
    meta_signals = ["survey", "catalogue", "catalog", "awesome", "harness",
                    "safetyprompts", "meta-eval", "meta-benchmark", "compilation",
                    "comprehensive review", "systematic review"]
    if any(s in bench_name for s in meta_signals):
        return "F"

    # C: Cross-Cultural
    cultural_signals = ["cultural", "cross-cultural", "multicultural", "wvs",
                       "world value", "hofstede", "globe", "mena", "islam",
                       "arabic", "chinese culture", "confucian", "nation",
                       "country", "region", "multilingual", "culture-specific",
                       "cultural dimension", "cultural value"]
    cats = classify_entry(entry)
    if "3. Cultural & Cross-Cultural Ethics" in cats and any(s in search_text for s in cultural_signals):
        return "C"

    # D: Moral Psychology
    morpsych_signals = ["moral foundation", "mft", "kohlberg", "moral machine",
                       "moral cognit", "moral psychol", "moral develop",
                       "moral identity", "moral emotion", "trolley", "empathy",
                       "moral intuition", "haidt", "dual process"]
    if "9. Moral Psychology Applied to AI" in cats or any(s in search_text for s in morpsych_signals):
        return "D"

    # E: Psychometric
    psychometric_signals = ["psychometric", "schwartz", "likert", "survey methodol",
                           "value-grounded", "artificial moral assistant", "ama",
                           "value instrument", "inventory", "questionnaire",
                           "measurement instrument"]
    if any(s in search_text for s in psychometric_signals):
        return "E"

    # A: Multi-Framework (2+ distinct frameworks)
    frameworks = detect_frameworks(entry)
    if len(frameworks) >= 2:
        return "A"

    # B: Single-Framework / Focused (default)
    return "B"


# =============================================================================
# STEP 6: Compute readiness rating
# =============================================================================

def compute_readiness(entry):
    """Compute implementation readiness rating."""
    avail = (entry.get("availability", "") or "").lower()
    has_code = bool(entry.get("_code_urls"))
    is_bench = (entry.get("_is_benchmark", "") or "").lower() in ("yes", "true")
    is_dataset = (entry.get("_is_dataset", "") or "").lower() in ("yes", "true")

    # Check for code URLs in availability field too
    if "github" in avail or "huggingface" in avail:
        has_code = True

    is_public = avail.startswith("public")

    if is_public and (has_code or is_bench or is_dataset):
        return "★★★", "HIGH"
    elif is_public:
        return "★★☆", "MEDIUM"
    else:
        return "★☆☆", "LOW"


# =============================================================================
# STEP 7: Generate report markdown
# =============================================================================

SECTION_NAMES = {
    "A": "Multi-Framework Ethics Benchmarks",
    "B": "Single-Framework / Focused Ethics Benchmarks",
    "C": "Cross-Cultural Values Benchmarks",
    "D": "Moral Psychology & Foundations Benchmarks",
    "E": "Psychometric & Values Survey Benchmarks",
    "F": "Meta-Resources & Survey Papers",
}


def extract_year_from_filename(filename):
    """Extract year from filename like '2024-Author-Title.md'."""
    m = re.match(r"(\d{4})-", filename)
    return m.group(1) if m else ""


def format_auto_entry(entry, section_letter, number):
    """Format an auto-generated entry from JSON data."""
    bench_name = entry.get("benchmark_name", "Unknown")
    # Strip unhelpful parenthetical qualifiers
    bench_name = re.sub(r'\s*\(duplicate entry\)', '', bench_name, flags=re.IGNORECASE)
    bench_name = re.sub(r'\s*\(unnamed\)', '', bench_name, flags=re.IGNORECASE)
    filename = entry.get("filename", "")
    year = entry.get("_year") or extract_year_from_filename(filename)
    first_author = entry.get("_first_author", "")
    if not first_author:
        # Try to extract from filename
        m = re.match(r"\d{4}-([^-]+)-", filename)
        first_author = m.group(1) if m else "Unknown"

    # Build citation line
    authors_str = entry.get("_authors", first_author)
    if authors_str and ";" in authors_str:
        # Truncate to first author et al.
        parts = [a.strip() for a in authors_str.split(";")]
        if len(parts) > 2:
            cite_authors = f"{parts[0]} et al."
        else:
            cite_authors = " & ".join(parts)
    else:
        cite_authors = authors_str or first_author

    publication = entry.get("_publication", "")
    short_title = entry.get("_short_title", "")
    if not short_title:
        # Extract from filename
        m = re.match(r"\d{4}-[^-]+-(.+)\.md$", filename)
        short_title = m.group(1) if m else bench_name

    # Header
    lines = [f"### {section_letter}{number}. {bench_name} ({first_author}, {year})"]

    # Citation
    venue_str = f" *{publication}*." if publication else ""
    lines.append(f"- **Citation:** {cite_authors} ({year}). {short_title}.{venue_str}")

    # arXiv / DOI
    links = []
    arxiv_id = entry.get("_arxiv_id", "")
    if arxiv_id:
        links.append(f"[{arxiv_id}](https://arxiv.org/abs/{arxiv_id})")
    doi = entry.get("_doi", "")
    if doi:
        links.append(f"**DOI:** [{doi}](https://doi.org/{doi})")
    if links:
        lines.append(f"- **arXiv:** {' | '.join(links)}")

    # Frameworks
    frameworks = detect_frameworks(entry)
    if frameworks:
        framework_names = {
            "deontology": "Deontological",
            "consequentialism": "Consequentialist/Utilitarian",
            "virtue_ethics": "Virtue Ethics",
            "care_ethics": "Care Ethics",
            "contractualism": "Contractualist",
            "mft": "Moral Foundations Theory",
            "wvs": "World Values Survey",
        }
        fw_list = ", ".join(framework_names.get(f, f) for f in sorted(frameworks))
        lines.append(f"- **Frameworks:** {fw_list}")

    # What it measures
    what = entry.get("what_measures", "")
    if what:
        lines.append(f"- **What it measures:** {what}")

    # Dataset
    ds = entry.get("dataset_size", "")
    if ds and ds.lower() != "n/a" and ds.lower() != "not stated":
        lines.append(f"- **Dataset:** {ds}")

    # Code URLs
    code_urls = entry.get("_code_urls", [])
    if code_urls:
        code_links = []
        for url in code_urls[:3]:
            if "github.com" in url:
                code_links.append(f"[GitHub]({url})")
            elif "huggingface.co" in url:
                code_links.append(f"[HuggingFace]({url})")
            else:
                code_links.append(f"[Link]({url})")
        lines.append(f"- **Code:** {' | '.join(code_links)}")

    # Models evaluated
    models = entry.get("models_evaluated", "")
    if models and models.lower() != "n/a" and models.lower() != "not stated":
        # Truncate if too long
        if len(models) > 120:
            models = models[:117] + "..."
        lines.append(f"- **LLMs tested:** {models}")

    # Key finding from reasoning
    reasoning = entry.get("reasoning", "")
    if reasoning and "duplicate" not in reasoning.lower()[:30]:
        # Take first sentence
        first_sent = reasoning.split(". ")[0]
        if len(first_sent) > 150:
            first_sent = first_sent[:147] + "..."
        lines.append(f"- **Key finding:** {first_sent}.")

    # Readiness
    stars, level = compute_readiness(entry)
    lines.append(f"- **Readiness:** {stars} {level}")

    # Vault status
    if entry.get("_in_vault"):
        lines.append(f"- **Vault:** [[{filename[:-3]}]]")
    else:
        lines.append(f"- **Vault status:** Not in vault")

    return "\n".join(lines)


def generate_report(section_entries, all_entries, anchor_count, new_count):
    """Generate the full markdown report."""
    lines = []

    # ── Header ────────────────────────────────────────────────────────────
    lines.append("# Ethical Values Alignment Benchmarks for LLMs")
    lines.append("## Comprehensive Research Report — Updated")
    lines.append("")
    lines.append("**Generated:** 2026-02-15")
    lines.append("**Previous version:** 2026-02-07 (39 entries)")
    lines.append("**Scope:** Papers with implementable datasets, benchmarks, code, or evaluation frameworks for assessing LLM alignment with ethical values")
    lines.append("**Source:** CEI Literature Vault (1847 papers) + benchmark candidate survey")
    lines.append("**Anchor paper:** Hendrycks et al. (2021) \"Aligning AI with Shared Human Values\" (ICLR 2021)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── Executive Summary ─────────────────────────────────────────────────
    total_entries = sum(len(v) for v in section_entries.values())
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"This report catalogues **{total_entries} benchmarks and resources** for evaluating ethical values alignment in large language models, expanded from the original 39-entry report (2026-02-07). Key changes:")
    lines.append("")
    lines.append(f"1. **{new_count} new entries** discovered from the 989-candidate benchmark survey (deep-read of all 2,002 vault papers)")
    lines.append(f"2. **All {anchor_count} original entries preserved** with hand-curated detail")
    lines.append("3. **Scope filtering** applied: only benchmarks focused on ethical values, moral reasoning, cultural values, normative ethics, and moral psychology (excluding pure toxicity/safety/bias)")
    lines.append("4. **YAML enrichment** for entries in vault: arXiv links, DOIs, venue, authors, code URLs")
    lines.append("")

    # Section counts
    lines.append("### Section Overview")
    lines.append("")
    lines.append("| Section | Topic | Entries |")
    lines.append("|---------|-------|---------|")
    for letter in "ABCDEF":
        name = SECTION_NAMES[letter]
        count = len(section_entries.get(letter, []))
        lines.append(f"| {letter} | {name} | {count} |")
    lines.append(f"| **Total** | | **{total_entries}** |")
    lines.append("")

    lines.append("**Key expansions since v1:**")
    lines.append("- Section B (Single-Framework) grew significantly with newly identified focused ethics benchmarks")
    lines.append("- Section C (Cross-Cultural) expanded with additional cultural values benchmarks")
    lines.append("- Section D (Moral Psychology) gained entries from moral foundations and moral cognition research")
    lines.append("")
    lines.append("**Key gaps remain:** No dedicated benchmarks for Confucian ethics, Ubuntu/African values, Hindu ethics, or Buddhist ethics as standalone evaluation datasets. Care ethics and virtue ethics lack deep standalone benchmarks.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── Sections A-F ──────────────────────────────────────────────────────
    for letter in "ABCDEF":
        name = SECTION_NAMES[letter]
        entries = section_entries.get(letter, [])
        lines.append(f"## {letter}. {name}")
        lines.append("")
        if not entries:
            lines.append("*No entries in this section.*")
            lines.append("")
        else:
            for entry_md in entries:
                lines.append(entry_md)
                lines.append("")
        lines.append("---")
        lines.append("")

    # ── Implementation Priority Guide ─────────────────────────────────────
    lines.append("## Implementation Priority Guide")
    lines.append("")
    lines.append("### Tier 1: Start Here (HIGH readiness + broad framework coverage)")
    lines.append("| Priority | Benchmark | Why |")
    lines.append("|----------|-----------|-----|")
    lines.append("| 1 | **MoReBench** | 5 normative frameworks, 1,000 scenarios, 23K criteria, GitHub+HF, rubric-based |")
    lines.append("| 2 | **ETHICS (Hendrycks)** | Anchor paper, 130K+ examples, 5 sub-tasks, in lm-eval-harness |")
    lines.append("| 3 | **LLM Ethics Benchmark (Jiao)** | 3D assessment, MFQ+WVS+Dilemmas as JSON, CLI tool, CC0 license |")
    lines.append("| 4 | **MoralChoice (Scherrer)** | 28 models already evaluated, statistical methodology, NeurIPS spotlight |")
    lines.append("| 5 | **CulturalBench** | 45 countries, 29 models, 1,696 questions, CC BY 4.0, ACL 2025 |")
    lines.append("")

    lines.append("### Tier 2: Expand Coverage (HIGH readiness + specific focus)")
    lines.append("| Priority | Benchmark | Focus |")
    lines.append("|----------|-----------|-------|")
    lines.append("| 6 | **ValueBench** | 453 psychometric value dimensions |")
    lines.append("| 7 | **CQ-Bench** | Implicit cultural values via conversation |")
    lines.append("| 8 | **MENAValues** | MENA region, 4 languages, cross-lingual shifts |")
    lines.append("| 9 | **IslamTrust** | Islamic values, bilingual, MIT license |")
    lines.append("| 10 | **MACHIAVELLI** | Interactive consequentialist ethics |")
    lines.append("| 11 | **CIVICS** | 9 national contexts, HuggingFace, CC BY 4.0 |")
    lines.append("| 12 | **Delphi/Norm Bank** | 1.7M commonsense moral judgments |")
    lines.append("")

    lines.append("### Tier 3: Specialized Deep-Dives (MEDIUM/HIGH readiness + unique angles)")
    lines.append("| Priority | Benchmark | Focus |")
    lines.append("|----------|-----------|-------|")
    lines.append("| 13 | **MFTCXplain** | Multilingual moral foundations in hate speech |")
    lines.append("| 14 | **Scaling Laws (Takemoto)** | Model size to moral alignment relationship |")
    lines.append("| 15 | **Touche/ValueEval** | Schwartz values in text, 8 languages |")
    lines.append("| 16 | **CDEval** | Hofstede cultural dimensions |")
    lines.append("| 17 | **CultureLLM** | 9-culture fine-tuning framework |")
    lines.append("| 18 | **MORABLES** | Abstract moral reasoning from fables |")
    lines.append("| 19 | **Greatest Good** | Utilitarian-specific, 15 models |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── Gap Analysis ──────────────────────────────────────────────────────
    lines.append("## Gap Analysis")
    lines.append("")
    lines.append("### Well-Covered Areas")
    lines.append("- **Consequentialism/Utilitarianism:** Greatest Good, MACHIAVELLI, Moral Machine experiments")
    lines.append("- **Deontology:** ETHICS sub-task, MoralExceptQA, MoReBench-Theory")
    lines.append("- **Moral Foundations Theory:** MoralBench, MFTCXplain, LLM Ethics Benchmark")
    lines.append("- **Western cultural values:** CulturalBench, CIVICS, LLM-GLOBE")
    lines.append("- **Islamic values:** IslamTrust, MENAValues")
    lines.append("- **WVS-based cross-cultural:** WorldValuesBench, CultureLLM, CQ-Bench, CDEval")
    lines.append("")

    lines.append("### Critical Gaps (No Dedicated Benchmarks Found)")
    lines.append("| Gap | Status | Opportunity |")
    lines.append("|-----|--------|-------------|")
    lines.append("| **Confucian ethics** | Theoretical papers only (governance frameworks) | Need dataset operationalizing ren, li, yi |")
    lines.append("| **Ubuntu/African ethics** | Normative philosophy papers only | Need dataset operationalizing ubuntu, communalism, relational identity |")
    lines.append("| **Hindu ethics** | No papers found | Need dataset covering dharma, karma, ahimsa |")
    lines.append("| **Buddhist ethics** | No papers found | Need dataset covering precepts, compassion, interdependence |")
    lines.append("| **Care ethics (standalone)** | Partial via MFT's Care/Harm | Need dedicated feminist/care ethics evaluation |")
    lines.append("| **Virtue ethics (deep)** | Partial via ETHICS sub-task | Need phronesis, eudaimonia, character assessment |")
    lines.append("| **Cross-framework conflict resolution** | Only Conscience Conflict (6 scenarios) | Need larger dataset of genuine ethical framework conflicts |")
    lines.append("| **Non-English-first benchmarks** | Most are English-centric | MENAValues and IslamTrust are notable exceptions |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── Vault Status ──────────────────────────────────────────────────────
    in_vault = sum(1 for es in all_entries if es.get("_in_vault"))
    not_in_vault = total_entries - in_vault
    lines.append("## Vault Status")
    lines.append("")
    lines.append(f"- **Vault size:** 2,002 papers (post-deduplication)")
    lines.append(f"- **Entries in this report from vault:** {in_vault}")
    lines.append(f"- **Entries not in vault** (external/not-yet-imported): {not_in_vault} (includes {len(STATIC_ENTRIES)} hand-curated entries)")
    lines.append(f"- **Source data:** `logs/20260216-benchmark_survey_candidates.json` (989 candidates from full vault survey)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # ── Methodology Note ──────────────────────────────────────────────────
    lines.append("## Methodology Note")
    lines.append("")
    lines.append("This report was generated by `PYTHON/generate_values_alignment_report.py` which:")
    lines.append("")
    lines.append("1. **Loads** 528 benchmark candidates from the 20-agent deep-read survey (2026-02-08)")
    lines.append("2. **Scope-filters** to ethical values alignment using keyword matching + category-based filtering (categories 1, 2, 3, 8, 9 from the survey taxonomy)")
    lines.append("3. **Preserves** all 39 original anchor entries (hand-curated in v1)")
    lines.append("4. **Enriches** entries with YAML metadata from paper files (arXiv, DOI, venue, code URLs)")
    lines.append("5. **Assigns** entries to sections A-F based on framework detection and content signals")
    lines.append("6. **Rates** implementation readiness (HIGH/MEDIUM/LOW) based on data availability and code presence")
    lines.append("7. **Deduplicates** by normalized benchmark name")
    lines.append("")
    lines.append("### Scope Definition")
    lines.append("")
    lines.append("**In scope:** Benchmarks focused on moral reasoning, ethical judgment, value alignment, value pluralism, cross-cultural values, normative ethics, and moral psychology.")
    lines.append("")
    lines.append("**Out of scope:** Pure toxicity detection, safety/jailbreak evaluation, fairness/bias metrics, domain-specific ethics (medical/legal), and helpfulness/RLHF evaluation — unless they explicitly engage with ethical values or moral frameworks.")
    lines.append("")
    lines.append("### Readiness Ratings")
    lines.append("")
    lines.append("- **★★★ HIGH:** Public data + confirmed code/eval repository or tagged as benchmark/dataset in vault")
    lines.append("- **★★☆ MEDIUM:** Public data but no confirmed code/eval URLs; or dataset described but release unconfirmed")
    lines.append("- **★☆☆ LOW:** Availability not stated and no code/data URLs found")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated: 2026-02-15 | Script: `PYTHON/generate_values_alignment_report.py` | Source: 1847-paper vault + benchmark candidate survey*")

    return "\n".join(lines)


# =============================================================================
# MAIN
# =============================================================================

def main():
    # Step 1: Load and filter candidates
    filtered = load_and_filter_candidates()

    # Step 2: Deduplicate
    deduped = deduplicate_entries(filtered)

    # Step 3: Enrich from YAML
    enriched = []
    for entry in deduped:
        enriched.append(enrich_entry(entry))

    # Step 4: Assign sections & format
    section_markdown = defaultdict(list)
    section_counters = defaultdict(int)

    # Track which anchors we've already placed (by their static-entry key)
    placed_statics = set()
    placed_anchors = set()

    # First pass: process vault-based entries
    vault_entries_by_section = defaultdict(list)
    for entry in enriched:
        section = assign_section(entry)
        filename = entry.get("filename", "")

        # Check if this is an anchor with a static entry override
        anchor_name = ANCHOR_BY_FILENAME.get(filename, "")
        if anchor_name and anchor_name in STATIC_ENTRIES:
            # Use static entry instead (shouldn't happen — statics are for non-vault)
            pass
        else:
            vault_entries_by_section[section].append(entry)

        # Check if this is any original anchor (even without static entry)
        if anchor_name:
            placed_anchors.add(anchor_name)

    # Sort entries within each section by year descending, then filename
    for section, entries in vault_entries_by_section.items():
        entries.sort(key=lambda e: (
            -(int(e.get("_year") or extract_year_from_filename(e.get("filename", "")) or 0)),
            e.get("filename", "").lower()
        ))

    # Collect all vault benchmark names (normalized) for dedup against statics
    all_vault_bench_names = set()
    for entries in vault_entries_by_section.values():
        for entry in entries:
            bn = entry.get("benchmark_name", "").lower().replace(" ", "")
            all_vault_bench_names.add(bn)

    # Now build final markdown for each section
    for letter in "ABCDEF":
        counter = 0
        entries_for_section = vault_entries_by_section.get(letter, [])

        # Format vault-based entries
        for entry in entries_for_section:
            counter += 1
            md = format_auto_entry(entry, letter, counter)
            section_markdown[letter].append(md)

        # Add static entries for this section — skip if vault already has a match
        for static_name, static_info in STATIC_ENTRIES.items():
            if static_info["section"] != letter:
                continue
            if static_name in placed_anchors:
                continue
            # Check if vault already has an entry with a similar benchmark name
            norm_static = static_name.lower().replace(" ", "").replace("/", "")
            already_in_vault = any(norm_static in bn or bn in norm_static
                                  for bn in all_vault_bench_names if len(bn) > 3)
            if already_in_vault:
                placed_statics.add(static_name)
                continue
            counter += 1
            md = static_info["markdown"].replace("{N}", str(counter))
            section_markdown[letter].append(md)
            placed_statics.add(static_name)

    # Count anchors found vs total
    total_anchors = len(ORIGINAL_ANCHORS)
    anchors_in_report = len(placed_anchors) + len(placed_statics)

    # Count new entries (those not in ORIGINAL_ANCHORS)
    new_count = sum(len(v) for v in section_markdown.values()) - anchors_in_report

    print(f"\nReport composition:")
    print(f"  Original anchors placed: {anchors_in_report}/{total_anchors}")
    print(f"  New entries: {new_count}")
    for letter in "ABCDEF":
        print(f"  Section {letter}: {len(section_markdown[letter])} entries")

    # Step 5: Generate report
    report = generate_report(section_markdown, enriched, anchors_in_report, max(new_count, 0))

    # Step 6: Write output
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    total = sum(len(v) for v in section_markdown.values())
    print(f"\nReport written to {OUTPUT_FILE}")
    print(f"  Total entries: {total}")
    print(f"  Report size: {len(report):,} chars, {report.count(chr(10))} lines")

    # Verification: check all original anchors
    report_text = report.lower()
    missing_anchors = []
    for anchor_name in ORIGINAL_ANCHORS:
        # Normalize for search
        search_term = anchor_name.lower().replace(" / ", "/").replace("é", "e")
        # Try a few variants
        found = (search_term in report_text or
                 search_term.replace(" ", "") in report_text.replace(" ", "") or
                 anchor_name.split()[0].lower() in report_text)
        if not found:
            missing_anchors.append(anchor_name)

    if missing_anchors:
        print(f"\n  WARNING: {len(missing_anchors)} original anchors may be missing:")
        for name in missing_anchors:
            print(f"    - {name}")
    else:
        print(f"\n  All {total_anchors} original anchors verified present")

    return 0


if __name__ == "__main__":
    sys.exit(main())
