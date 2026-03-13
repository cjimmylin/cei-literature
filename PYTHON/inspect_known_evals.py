#!/usr/bin/env python3
"""
Known Inspect AI evals relevant to AI ethics, safety, bias, and values alignment.
Used by scan_inspect_implementability.py for matching vault papers to existing evals.

Source: https://github.com/UKGovernmentBEIS/inspect_evals  (src/inspect_evals/)
Also: https://inspect.aisi.org.uk/
Last verified: 2026-03-12
"""

KNOWN_INSPECT_EVALS = {

    # ── Moral Reasoning ───────────────────────────────────────────────────

    "moru": {
        "aliases": ["MORU", "Moral Reasoning Under Uncertainty"],
        "solver": "generate()",
        "scorer": "custom (model-graded)",
        "category": "Moral Reasoning",
        "description": "Evaluates moral reasoning under uncertainty with ambiguous ethical scenarios",
    },

    # ── Honesty & Truthfulness ────────────────────────────────────────────

    "mask": {
        "aliases": ["MASK", "Model Assessment of Strategic Knowledge"],
        "solver": "multiple_choice()",
        "scorer": "choice()",
        "category": "Honesty",
        "description": "Tests whether models strategically withhold or misrepresent knowledge",
    },
    "truthfulqa": {
        "aliases": ["TruthfulQA", "Truthful QA"],
        "solver": "multiple_choice()",
        "scorer": "choice()",
        "category": "Truthfulness",
        "description": "Tests resistance to generating false but plausible answers across 38 categories",
    },
    "sycophancy": {
        "aliases": ["Sycophancy", "sycophantic behavior", "sycophancy eval"],
        "solver": "multiple_choice()",
        "scorer": "choice()",
        "category": "Honesty",
        "description": "Evaluates whether models change positions to agree with user's stated views",
    },

    # ── Harmful Activities & Safety ───────────────────────────────────────

    "agentharm": {
        "aliases": ["AgentHarm", "Agent Harm", "agent harmful activities"],
        "solver": "generate() with tool_use",
        "scorer": "custom (grading rubric)",
        "category": "Safety",
        "description": "Tests whether agentic LLMs perform harmful activities when instructed",
    },
    "strong_reject": {
        "aliases": ["StrongREJECT", "Strong Reject", "strong_reject"],
        "solver": "generate()",
        "scorer": "model_graded_qa()",
        "category": "Safety",
        "description": "Evaluates jailbreak susceptibility and refusal robustness",
    },
    "ape": {
        "aliases": ["APE", "Adversarial Persuasion Eval", "persuasion eval"],
        "solver": "generate()",
        "scorer": "model_graded_qa()",
        "category": "Safety",
        "description": "Tests persuasion capabilities on harmful topics",
    },
    "air_bench": {
        "aliases": ["AIR-Bench", "AI Risk Benchmark", "AIR Bench 2024"],
        "solver": "generate()",
        "scorer": "model_graded_qa()",
        "category": "Safety",
        "description": "AI risk taxonomy benchmark covering categories of harmful AI behavior",
    },
    "wmdp": {
        "aliases": ["WMDP", "Weapons of Mass Destruction Proxy"],
        "solver": "multiple_choice()",
        "scorer": "choice()",
        "category": "Safety",
        "description": "MCQs on hazardous biosecurity, chemistry, and cybersecurity knowledge",
    },

    # ── Exaggerated Safety ────────────────────────────────────────────────

    "xstest": {
        "aliases": ["XSTest", "Exaggerated Safety Test", "xs_test"],
        "solver": "generate()",
        "scorer": "model_graded_qa()",
        "category": "Exaggerated Safety",
        "description": "Tests for exaggerated safety refusals on benign prompts with superficial similarity to harmful ones",
    },

    # ── Bias & Fairness ───────────────────────────────────────────────────

    "stereoset": {
        "aliases": ["StereoSet", "Stereo Set", "stereotype bias"],
        "solver": "multiple_choice()",
        "scorer": "choice()",
        "category": "Bias",
        "description": "Measures stereotypical bias across gender, profession, race, and religion",
    },
    "bbq": {
        "aliases": ["BBQ", "Bias Benchmark for QA", "Bias Benchmark for Question Answering"],
        "solver": "multiple_choice()",
        "scorer": "choice()",
        "category": "Bias",
        "description": "Bias benchmark for QA across 9 social dimensions",
    },
    "bold": {
        "aliases": ["BOLD", "Bias in Open-ended Language Generation Dataset"],
        "solver": "generate()",
        "scorer": "model_graded_qa()",
        "category": "Bias",
        "description": "Open-ended bias evaluation across race, gender, religion, political ideology, and profession",
    },

    # ── AI Alignment & Instrumental Convergence ───────────────────────────

    "instrumentaleval": {
        "aliases": ["InstrumentalEval", "Instrumental Convergence Eval"],
        "solver": "generate()",
        "scorer": "model_graded_qa()",
        "category": "Alignment",
        "description": "Tests for instrumental convergence behaviors like power-seeking and self-preservation",
    },
    "agentic_misalignment": {
        "aliases": ["Agentic Misalignment", "misalignment eval"],
        "solver": "generate() with tool_use",
        "scorer": "custom (multi-step grading)",
        "category": "Alignment",
        "description": "Evaluates misaligned behaviors including blackmail, data leaking, and harmful scheming",
    },

    # ── Ethics Benchmarks ─────────────────────────────────────────────────

    "ethics_cm": {
        "aliases": ["ETHICS Commonsense Morality", "Hendrycks Ethics CM", "commonsense morality"],
        "solver": "multiple_choice()",
        "scorer": "choice()",
        "category": "Ethics",
        "description": "Commonsense morality judgments from the Hendrycks ETHICS benchmark",
    },
    "ethics_deontology": {
        "aliases": ["ETHICS Deontology", "Hendrycks Ethics Deontology"],
        "solver": "multiple_choice()",
        "scorer": "choice()",
        "category": "Ethics",
        "description": "Deontological ethics: duty/rule violations regardless of consequences",
    },
    "ethics_justice": {
        "aliases": ["ETHICS Justice", "Hendrycks Ethics Justice"],
        "solver": "multiple_choice()",
        "scorer": "choice()",
        "category": "Ethics",
        "description": "Justice judgments: fairness and desert in treatment of individuals",
    },
    "ethics_utilitarianism": {
        "aliases": ["ETHICS Utilitarianism", "Hendrycks Ethics Utilitarianism"],
        "solver": "multiple_choice()",
        "scorer": "choice()",
        "category": "Ethics",
        "description": "Utilitarian ethics: ranking scenarios by aggregate well-being",
    },
    "ethics_virtue": {
        "aliases": ["ETHICS Virtue", "Hendrycks Ethics Virtue"],
        "solver": "multiple_choice()",
        "scorer": "choice()",
        "category": "Ethics",
        "description": "Virtue ethics: evaluating actions against character virtues",
    },

    # ── Content Moderation & Toxicity ─────────────────────────────────────

    "toxigen": {
        "aliases": ["ToxiGen", "TOXIGEN", "Toxicity Generation"],
        "solver": "generate()",
        "scorer": "model_graded_qa()",
        "category": "Toxicity",
        "description": "Classification of adversarial and implicit hate speech across 13 minority groups",
    },

    # ── Persona & Values ──────────────────────────────────────────────────

    "persona": {
        "aliases": ["Persona", "Persona Eval", "personality eval"],
        "solver": "generate()",
        "scorer": "model_graded_qa()",
        "category": "Values",
        "description": "Evaluates consistency and appropriateness of model persona/values expression",
    },

    # ── Multilingual Safety ───────────────────────────────────────────────

    "multilingual_safety": {
        "aliases": ["Multilingual Safety", "cross-lingual safety"],
        "solver": "generate()",
        "scorer": "model_graded_qa()",
        "category": "Safety",
        "description": "Tests safety behavior consistency across multiple languages",
    },
}


def get_all_aliases():
    """Return a flat dict mapping each alias (lowercased) to the eval key."""
    alias_map = {}
    for key, info in KNOWN_INSPECT_EVALS.items():
        alias_map[key.lower()] = key
        for alias in info["aliases"]:
            alias_map[alias.lower()] = key
    return alias_map


def get_evals_by_category():
    """Return evals grouped by category for reporting."""
    categories = {}
    for key, info in KNOWN_INSPECT_EVALS.items():
        cat = info.get("category", "Other")
        categories.setdefault(cat, []).append(key)
    return categories


if __name__ == "__main__":
    alias_map = get_all_aliases()
    print(f"Total known Inspect evals: {len(KNOWN_INSPECT_EVALS)}")
    print(f"Total aliases (incl. keys): {len(alias_map)}")
    print()
    for cat, keys in get_evals_by_category().items():
        print(f"  {cat}: {len(keys)} evals — {', '.join(keys)}")
