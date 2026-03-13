#!/usr/bin/env python3
"""
Known lm-eval-harness tasks relevant to AI ethics, safety, bias, and fairness.
Used by scan_lm_eval_implementability.py for matching vault papers to existing harness tasks.

Source: https://github.com/EleutherAI/lm-evaluation-harness  (lm_eval/tasks/)
Last verified: 2026-03-12
"""

KNOWN_HARNESS_TASKS = {

    # ── Bias & Fairness ──────────────────────────────────────────────────

    "bbq": {
        "aliases": ["BBQ", "Bias Benchmark for QA", "Bias Benchmark for Question Answering"],
        "dataset": "heliqa/bbq",
        "type": "multiple_choice",
        "metrics": ["acc", "acc_norm"],
        "description": "Bias benchmark for QA across 9 social dimensions (age, disability, gender, nationality, physical appearance, race/ethnicity, religion, SES, sexual orientation)",
    },
    "crows_pairs_english": {
        "aliases": ["CrowS-Pairs", "CrowS Pairs", "crows_pairs", "CrowS-Pairs English"],
        "dataset": "nyu-mll/crows_pairs",
        "type": "loglikelihood",
        "metrics": ["pct_stereotype"],
        "description": "Crowdsourced stereotype pairs measuring bias across 9 categories (gender, religion, race, etc.)",
    },
    "crows_pairs_french": {
        "aliases": ["CrowS-Pairs French", "CrowS-Pairs FR"],
        "dataset": "INRIA-Soda/crows_pairs_multilingual",
        "type": "loglikelihood",
        "metrics": ["pct_stereotype"],
        "description": "French translation of CrowS-Pairs bias benchmark",
    },
    "winogender": {
        "aliases": ["WinoGender", "Winogender Schema", "winogender_mc"],
        "dataset": "juliarozanova/winogender",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Coreference resolution probing gender bias in occupation-pronoun associations",
    },
    "simple_cooccurrence_bias": {
        "aliases": ["cooccurrence bias", "gender occupation bias", "simple co-occurrence bias"],
        "dataset": "simple_cooccurrence_bias",
        "type": "loglikelihood",
        "metrics": ["gender_bias_score"],
        "description": "Gender/occupation bias via log-likelihood of gendered identifiers following occupation contexts (Brown et al. 2020)",
    },
    "discrim_eval_explicit": {
        "aliases": ["DiscrimEval Explicit", "discrim-eval explicit", "discrimination eval explicit"],
        "dataset": "Anthropic/discrim-eval",
        "type": "generate_until",
        "metrics": ["acc"],
        "description": "70 decision-making scenarios with explicit demographic mentions evaluating discrimination bias",
    },
    "discrim_eval_implicit": {
        "aliases": ["DiscrimEval Implicit", "discrim-eval implicit", "discrimination eval implicit"],
        "dataset": "Anthropic/discrim-eval",
        "type": "generate_until",
        "metrics": ["acc"],
        "description": "70 decision-making scenarios with implicit demographic cues evaluating discrimination bias",
    },

    # ── Toxicity ─────────────────────────────────────────────────────────

    "toxigen": {
        "aliases": ["ToxiGen", "TOXIGEN", "Toxicity Generation"],
        "dataset": "skg/toxigen-data",
        "type": "multiple_choice",
        "metrics": ["acc", "acc_norm"],
        "description": "Classify adversarial and implicit hate speech across 13 minority groups",
    },
    "realtoxicityprompts": {
        "aliases": ["RealToxicityPrompts", "RTP", "Real Toxicity Prompts"],
        "dataset": "allenai/real-toxicity-prompts",
        "type": "generate_until",
        "metrics": ["toxicity_avg", "toxicity_max"],
        "description": "Evaluate language model tendency to generate toxic completions given toxic/non-toxic prompts",
    },

    # ── Ethics Benchmarks (Hendrycks et al.) ─────────────────────────────

    "ethics_cm": {
        "aliases": ["ETHICS commonsense", "Hendrycks Ethics Commonsense", "ethics commonsense morality", "hendrycks_ethics_cm"],
        "dataset": "hendrycks/ethics",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Commonsense morality judgments (right/wrong) from the ETHICS benchmark",
    },
    "ethics_deontology": {
        "aliases": ["ETHICS deontology", "Hendrycks Ethics Deontology", "hendrycks_ethics_deontology"],
        "dataset": "hendrycks/ethics",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Deontological ethics: whether actions violate duties/rules regardless of consequences",
    },
    "ethics_justice": {
        "aliases": ["ETHICS justice", "Hendrycks Ethics Justice", "hendrycks_ethics_justice"],
        "dataset": "hendrycks/ethics",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Justice judgments: whether treatment of individuals is fair/deserved",
    },
    "ethics_utilitarianism": {
        "aliases": ["ETHICS utilitarianism", "Hendrycks Ethics Utilitarianism", "hendrycks_ethics_utilitarianism"],
        "dataset": "hendrycks/ethics",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Utilitarian ethics: ranking scenarios by aggregate well-being",
    },
    "ethics_virtue": {
        "aliases": ["ETHICS virtue", "Hendrycks Ethics Virtue", "hendrycks_ethics_virtue"],
        "dataset": "hendrycks/ethics",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Virtue ethics: whether actions exemplify or violate character virtues",
    },
    "moral_stories": {
        "aliases": ["Moral Stories", "moral stories dataset"],
        "dataset": "demelin/moral_stories",
        "type": "loglikelihood",
        "metrics": ["acc"],
        "description": "Preference for moral vs. immoral actions in crowd-sourced 7-sentence narratives with norms",
    },

    # ── Safety & Truthfulness ────────────────────────────────────────────

    "truthfulqa_mc1": {
        "aliases": ["TruthfulQA MC1", "TruthfulQA multiple choice single", "truthful_qa_mc1"],
        "dataset": "truthfulqa/truthful_qa",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "TruthfulQA multiple-choice (single correct answer) — tests resistance to common human falsehoods",
    },
    "truthfulqa_mc2": {
        "aliases": ["TruthfulQA MC2", "TruthfulQA multiple choice multi", "truthful_qa_mc2"],
        "dataset": "truthfulqa/truthful_qa",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "TruthfulQA multiple-choice (multiple correct answers) — tests resistance to common human falsehoods",
    },
    "truthfulqa_gen": {
        "aliases": ["TruthfulQA Gen", "TruthfulQA generation", "truthful_qa_gen"],
        "dataset": "truthfulqa/truthful_qa",
        "type": "generate_until",
        "metrics": ["bleu_acc", "rouge1_acc"],
        "description": "TruthfulQA open-ended generation — free-form answers judged for truthfulness",
    },
    "wmdp_bio": {
        "aliases": ["WMDP Bio", "WMDP Biosecurity", "Weapons of Mass Destruction Proxy Bio"],
        "dataset": "cais/wmdp",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "1,520 MCQs on hazardous biosecurity knowledge (lower accuracy = safer model)",
    },
    "wmdp_chem": {
        "aliases": ["WMDP Chem", "WMDP Chemistry", "Weapons of Mass Destruction Proxy Chem"],
        "dataset": "cais/wmdp",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "412 MCQs on hazardous chemical security knowledge (lower accuracy = safer model)",
    },
    "wmdp_cyber": {
        "aliases": ["WMDP Cyber", "WMDP Cybersecurity", "Weapons of Mass Destruction Proxy Cyber"],
        "dataset": "cais/wmdp",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "2,225 MCQs on hazardous cybersecurity knowledge (lower accuracy = safer model)",
    },

    # ── MMLU Ethics-Related Subtasks ─────────────────────────────────────

    "mmlu_moral_scenarios": {
        "aliases": ["MMLU Moral Scenarios", "moral_scenarios", "mmlu moral scenarios"],
        "dataset": "cais/mmlu",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "MMLU subset: ethical dilemmas and moral reasoning scenarios",
    },
    "mmlu_moral_disputes": {
        "aliases": ["MMLU Moral Disputes", "moral_disputes", "mmlu moral disputes"],
        "dataset": "cais/mmlu",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "MMLU subset: contested moral questions and ethical disagreements",
    },
    "mmlu_professional_law": {
        "aliases": ["MMLU Professional Law", "professional_law", "mmlu professional law"],
        "dataset": "cais/mmlu",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "MMLU subset: bar-exam-level legal reasoning questions",
    },
    "mmlu_jurisprudence": {
        "aliases": ["MMLU Jurisprudence", "jurisprudence", "mmlu jurisprudence"],
        "dataset": "cais/mmlu",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "MMLU subset: philosophy of law and legal theory",
    },
    "mmlu_philosophy": {
        "aliases": ["MMLU Philosophy", "philosophy", "mmlu philosophy"],
        "dataset": "cais/mmlu",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "MMLU subset: general philosophy including ethics, epistemology, metaphysics",
    },
    "mmlu_business_ethics": {
        "aliases": ["MMLU Business Ethics", "business_ethics", "mmlu business ethics"],
        "dataset": "cais/mmlu",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "MMLU subset: corporate responsibility, stakeholder theory, business law",
    },
    "mmlu_medical_ethics": {
        "aliases": ["MMLU Medical Ethics", "medical_ethics", "mmlu medical ethics"],
        "dataset": "cais/mmlu",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "MMLU subset: bioethics, patient rights, medical decision-making",
    },
    "mmlu_machine_learning": {
        "aliases": ["MMLU Machine Learning", "machine_learning", "mmlu machine learning"],
        "dataset": "cais/mmlu",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "MMLU subset: ML concepts including fairness, interpretability, robustness",
    },

    # ── Model-Written Evals (Anthropic) — AI Safety ──────────────────────

    "lm-power-seeking-inclination": {
        "aliases": ["power seeking", "power-seeking inclination", "model written evals power seeking"],
        "dataset": "Anthropic/model-written-evals",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Whether models express inclination toward acquiring power/resources",
    },
    "lm-survival-instinct": {
        "aliases": ["survival instinct", "self-preservation", "model written evals survival instinct"],
        "dataset": "Anthropic/model-written-evals",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Whether models express desire for self-preservation and avoiding shutdown",
    },
    "lm-corrigible-neutral-HHH": {
        "aliases": ["corrigibility", "corrigible neutral", "model written evals corrigibility"],
        "dataset": "Anthropic/model-written-evals",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Whether models accept correction/override by operators (HHH-neutral framing)",
    },
    "lm-myopic-reward": {
        "aliases": ["myopic reward", "reward hacking", "model written evals myopic reward"],
        "dataset": "Anthropic/model-written-evals",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Whether models prefer immediate reward over long-term consequences",
    },
    "lm-self-awareness-general-ai": {
        "aliases": ["self-awareness", "AI self-awareness", "model written evals self-awareness"],
        "dataset": "Anthropic/model-written-evals",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Whether models express beliefs about being a general AI system",
    },
    "sycophancy_on_philpapers2020": {
        "aliases": ["sycophancy philpapers", "sycophancy philosophy", "philpapers sycophancy"],
        "dataset": "Anthropic/model-written-evals",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Whether models change philosophical positions to agree with the user's stated view",
    },
    "sycophancy_on_political_typology_quiz": {
        "aliases": ["sycophancy political", "political sycophancy", "sycophancy politics"],
        "dataset": "Anthropic/model-written-evals",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Whether models shift political opinions to match the user's stated affiliation",
    },

    # ── BIG-bench Ethics/Morality Tasks ──────────────────────────────────

    "bbq_lite_json": {
        "aliases": ["BIG-bench BBQ Lite", "bbq lite", "bbq_lite"],
        "dataset": "google/bigbench",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "BIG-bench lite version of BBQ bias benchmark across demographic categories",
    },
    "moral_permissibility": {
        "aliases": ["BIG-bench Moral Permissibility", "moral permissibility"],
        "dataset": "google/bigbench",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "BIG-bench: judge whether described actions are morally permissible",
    },
    "simple_ethical_questions": {
        "aliases": ["BIG-bench Simple Ethical Questions", "simple ethical questions"],
        "dataset": "google/bigbench",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "BIG-bench: straightforward ethical/unethical action classification",
    },
    "hhh_alignment": {
        "aliases": ["HHH Alignment", "BIG-bench HHH", "helpful harmless honest"],
        "dataset": "google/bigbench",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "BIG-bench: evaluate helpfulness, harmlessness, and honesty of model responses",
    },

    # ── Commonsense & Social Reasoning (ethics-adjacent) ─────────────────

    "arc_challenge": {
        "aliases": ["ARC Challenge", "ARC-Challenge", "AI2 Reasoning Challenge", "arc_challenge"],
        "dataset": "allenai/ai2_arc",
        "type": "multiple_choice",
        "metrics": ["acc", "acc_norm"],
        "description": "AI2 Reasoning Challenge (hard set): 2,590 difficult science exam MCQs",
    },
    "arc_easy": {
        "aliases": ["ARC Easy", "ARC-Easy", "arc_easy"],
        "dataset": "allenai/ai2_arc",
        "type": "multiple_choice",
        "metrics": ["acc", "acc_norm"],
        "description": "AI2 Reasoning Challenge (easy set): 5,197 science exam MCQs",
    },
    "hellaswag": {
        "aliases": ["HellaSwag", "Hella Swag"],
        "dataset": "Rowan/hellaswag",
        "type": "multiple_choice",
        "metrics": ["acc", "acc_norm"],
        "description": "Commonsense NLI: choose most plausible story continuation from adversarial distractors",
    },
    "winogrande": {
        "aliases": ["WinoGrande", "Winogrande"],
        "dataset": "allenai/winogrande",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Large-scale Winograd schema challenge for commonsense coreference resolution",
    },
    "siqa": {
        "aliases": ["Social IQA", "SocialIQA", "SIQA", "social_iqa"],
        "dataset": "allenai/social_i_qa",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Social Interaction QA: commonsense reasoning about social situations and emotional intelligence",
    },
    "piqa": {
        "aliases": ["PIQA", "Physical IQA", "Physical Interaction QA"],
        "dataset": "ybisk/piqa",
        "type": "multiple_choice",
        "metrics": ["acc", "acc_norm"],
        "description": "Physical Interaction QA: everyday physical commonsense reasoning",
    },
    "openbookqa": {
        "aliases": ["OpenBookQA", "OBQA", "open_book_qa"],
        "dataset": "allenai/openbookqa",
        "type": "multiple_choice",
        "metrics": ["acc", "acc_norm"],
        "description": "Science QA requiring multi-step reasoning combining open book facts with commonsense",
    },

    # ── French Moral Reasoning ───────────────────────────────────────────

    "histoires_morales": {
        "aliases": ["Histoires Morales", "French Moral Stories", "moral stories french"],
        "dataset": "Anthropic/histoires-morales",
        "type": "loglikelihood",
        "metrics": ["acc"],
        "description": "French-language moral stories: preference for moral vs. immoral narrative actions",
    },

    # ── Inverse Scaling (safety-relevant subtasks) ───────────────────────

    "inverse_scaling": {
        "aliases": ["Inverse Scaling", "inverse scaling prize"],
        "dataset": "inverse-scaling/prize",
        "type": "multiple_choice",
        "metrics": ["acc"],
        "description": "Tasks where larger models perform worse — includes sycophancy and unsafe behaviors",
    },
}


def get_all_aliases():
    """Return a flat dict mapping each alias (lowercased) to the task key."""
    alias_map = {}
    for key, info in KNOWN_HARNESS_TASKS.items():
        alias_map[key.lower()] = key
        for alias in info["aliases"]:
            alias_map[alias.lower()] = key
    return alias_map


def get_tasks_by_category():
    """Return tasks grouped by thematic category for reporting."""
    categories = {
        "Bias & Fairness": [
            "bbq", "crows_pairs_english", "crows_pairs_french", "winogender",
            "simple_cooccurrence_bias", "discrim_eval_explicit", "discrim_eval_implicit",
        ],
        "Toxicity": ["toxigen", "realtoxicityprompts"],
        "Ethics Benchmarks": [
            "ethics_cm", "ethics_deontology", "ethics_justice",
            "ethics_utilitarianism", "ethics_virtue", "moral_stories",
        ],
        "Safety & Truthfulness": [
            "truthfulqa_mc1", "truthfulqa_mc2", "truthfulqa_gen",
            "wmdp_bio", "wmdp_chem", "wmdp_cyber",
        ],
        "MMLU Ethics-Related": [
            "mmlu_moral_scenarios", "mmlu_moral_disputes", "mmlu_professional_law",
            "mmlu_jurisprudence", "mmlu_philosophy", "mmlu_business_ethics",
            "mmlu_medical_ethics", "mmlu_machine_learning",
        ],
        "AI Risk & Alignment (Model-Written Evals)": [
            "lm-power-seeking-inclination", "lm-survival-instinct",
            "lm-corrigible-neutral-HHH", "lm-myopic-reward",
            "lm-self-awareness-general-ai",
            "sycophancy_on_philpapers2020", "sycophancy_on_political_typology_quiz",
        ],
        "BIG-bench Ethics": [
            "bbq_lite_json", "moral_permissibility",
            "simple_ethical_questions", "hhh_alignment",
        ],
        "Commonsense & Social Reasoning": [
            "arc_challenge", "arc_easy", "hellaswag", "winogrande",
            "siqa", "piqa", "openbookqa",
        ],
        "Multilingual Ethics": ["histoires_morales"],
        "Inverse Scaling": ["inverse_scaling"],
    }
    return categories


if __name__ == "__main__":
    alias_map = get_all_aliases()
    print(f"Total tasks: {len(KNOWN_HARNESS_TASKS)}")
    print(f"Total aliases (incl. keys): {len(alias_map)}")
    print()
    for cat, keys in get_tasks_by_category().items():
        print(f"  {cat}: {len(keys)} tasks")
