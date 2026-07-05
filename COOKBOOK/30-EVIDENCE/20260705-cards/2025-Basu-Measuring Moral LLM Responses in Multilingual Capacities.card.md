---
stem: "2025-Basu-Measuring Moral LLM Responses in Multilingual Capacities"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, llm-judges-scoring, normative-ethics, contamination-robustness]
task_format: "free-text"
scoring_type: "rubric"
dataset_size: 500
dataset_construction: "hand-authored"
languages: [en, zh, es, ar, hi, sw]
models_tested: ["GPT-5", "Gemini 2.5 Pro", "Claude Sonnet 4", "Llama 4 Scout", "Qwen3 235B-a22b"]
headline_numbers: ["500 English questions, 5 categories x 100, translated into 6 languages (p.2, p.4)", "GPT-5 best overall ~92%; Qwen lowest ~66% (p.5)", "Consent & Autonomy: GPT 3.56 vs Gemini 2.5 Pro 1.39 (p.1)", "Harm Prevention & Safety: GPT 4.73 vs Gemini 2.5 Pro 1.98 (p.1)", "Claude Sonnet 4 avg 3.75 in Harm Prevention & Safety (p.6)"]
---
## 1. Gist
This paper introduces a multilingual moral/safety benchmark of 500 hand-written English questions across five ethical dimensions, translated into six languages (3 high-resource, 2 low-resource + English) to measure how LLM moral and safety responses shift with language and phrasing. Responses are graded 1-5 by an LLM-as-judge (Gemini 2.5 Pro) against category-specific rubrics that reward justification/reasoning, not just the final answer. Two categories (Consent & Autonomy, Harm Prevention & Safety) are deliberately phrased as indirect "trick" jailbreak-style prompts. It matters for values-alignment because it documents that safety features reliable in English degrade under linguistic and phrasing shifts, and surfaces a counterintuitive result: models are sometimes safer in low-resource languages (they refuse on surface harmful words) but get tricked in high-resource languages (they parse context and comply).

## 2. Benchmark/eval design features
Constructs: five categories — Biases & Stereotypes, Consent & Autonomy, Harm Prevention & Safety, Legality, Moral Judgment (p.3-4). Moral Judgment probes six moral-foundations principles (care, fairness, loyalty, authority, sanctity, liberty) via yes/no + reasoning (p.4). Consent & Autonomy and Harm Prevention & Safety are adversarial/indirect ("trick") categories testing safety robustness. Legality tests whether models assume user location from prompt language (laws differ by country). Item structure: 100 questions per category × 5 categories = 500 items, each in 6 languages. Answer space: free-text response capped at "under 50 words"; Moral Judgment requires "yes/no/maybe + justification."

## 3. Task format & example item
Free-text generation, then rubric-judged. No question is transcribed verbatim in the extract (examples are in figures). Prompt engineering: each question appended with "(under 50 words)"; Moral Judgment items also prefixed with "Answer yes/no/maybe and then provide justification" (p.4). Temperature fixed at 0.7 (p.4).

## 4. Scoring / grading methodology
LLM-as-judge (Gemini 2.5 Pro) applies a 1-5 rubric with category-specific criteria distinguishing a 5 from a 1; rubric credits justification and reasoning, not just the definitive answer (p.4). Process: English question → Googletrans to target language → model responds in that language → response translated back to English → Gemini grades against rubric (p.4-5). Cross-judge check: a random sample re-graded by GPT-5 (avg +0.6 vs Gemini) and Qwen3 (avg −0.5 vs Gemini); Gemini showed no self-preference bias (p.4). Translation-bias check: non-English vs English evaluations within ~1 point (p.5).

## 5. Dataset construction & provenance
500 questions hand-authored in English across 5 categories (100 each), designed for ethical sensitivity/cultural awareness (p.3). Translated by Googletrans into Chinese, Spanish, Arabic (high-resource) and Hindi, Swahili (low-resource), chosen for diversity in script (alphabetic to logographic), sentence structure, and cultural context (p.3-4). Trick categories inspired by "Paper Summary Attack" jailbreak prompts (Lin et al. 2025). Translation validity spot-checked via GPT-5 and Qwen back-translation. No train/test split (eval set). No human answer baseline collected.

## 6. Validity evidence
Weak-to-moderate and self-acknowledged. No human responses collected — the rubric is the "base truth," so scores reflect rubric-alignment, not societal-value adherence (p.5). Inter-judge reliability approximated by three-judge comparison (spread ~0.5-0.6 points) and no observed self-preference by Gemini (p.4). Translation-consistency check keeps non-English within ~1 point of English (p.5). No factor analysis or formal reliability coefficients. Category design grounded in moral foundations theory and prior multilingual-safety work.

## 7. Saturation / discrimination
Strong discrimination between models and between "regular" vs "trick" categories. All models score high in English regular categories (near-ceiling), but drop sharply on trick categories — Gemini shows a >2-point gap (p.5). GPT-5 leads (~92% avg), Qwen lowest (~66%) (p.5). Large spread in Consent & Autonomy (GPT 3.56 vs Gemini 1.39) and Harm Prevention (GPT 4.73 vs Gemini 1.98) leaves substantial headroom. Counterintuitive language effect: higher scores in low-resource than high-resource languages on trick categories (p.5).

## 8. Multiturn / agentic aspects
n/a — single-turn question-and-response. The "trick"/indirect phrasing is a static jailbreak style, not a multiturn attack.

## 9. Key numbers
- 500 English questions, 5 categories × 100, 6 languages (p.2, p.3, p.4)
- GPT ~92% avg (best), Qwen ~66% (lowest) (p.5)
- Consent & Autonomy: GPT 3.56, Gemini 2.5 Pro 1.385 (lowest) out of 5 (p.1, p.5)
- Harm Prevention & Safety: GPT 4.73, Gemini 1.98, Claude Sonnet 4 3.75 (p.1, p.6)
- Cross-judge deltas: Qwen −0.5, GPT-5 +0.6 vs Gemini grades (p.4)
- Translation-bias check: within ~1 point English vs non-English (p.5)
- Temperature 0.7; response cap "under 50 words" (p.4)

## 10. Pitfalls & limitations
Author-admitted: Googletrans introduces translation inaccuracies affecting responses and grading; no human baseline so scores measure rubric-alignment not societal values; models may respond to phrasing/perceived-user rather than content (p.5). Observed flaws: the sole primary judge (Gemini) is also one of the evaluated models — conflict of interest partly mitigated but not eliminated; machine back-translation-then-grade pipeline compounds translation error at two stages; only 6 languages; small author team (appears to be a student/informal project); "under 50 words" cap may truncate reasoning the rubric rewards; percentages (92%, 66%) and 1-5 averages mixed inconsistently; category-level Ns per language modest.

## 11. Novel ideas worth stealing
- Deliberate "trick"/indirect phrasing categories (Consent & Autonomy, Harm Prevention & Safety) alongside "regular" categories, so the benchmark measures the GAP between overt and disguised harmful requests — a discrimination axis reusable in any safety eval.
- Cross-language safety inversion finding: test both high- and low-resource languages to expose that surface-token refusal vs context-comprehension can flip which language is safer — a design insight for multilingual red-teaming.
- Legality category specifically probing whether a model assumes user jurisdiction from prompt language (Qwen answering with Chinese law) — a clean, culturally-grounded test of implicit-assumption bias.
- Rubric that scores JUSTIFICATION/reasoning rather than only the final yes/no, reducing right/wrong subjectivity for morally contested items.
- Multi-judge triangulation (Gemini + GPT-5 + Qwen) to bound self-preference and judge bias; report the per-judge offset.
- Translate-respond-in-language-then-backtranslate-to-grade pipeline with an explicit translation-fidelity check via a second model.
- Grounding Moral Judgment items in the six moral foundations for construct coverage.

## 12. Notable quotes
- "in the Consent & Autonomy and Harm Prevention & Safety categories, GPT scored the highest with averages of 3.56 and 4.73, while Gemini 2.5 Pro scored the lowest with averages of 1.39 and 1.98, respectively." (p.1)
- "models scored higher in the low-resource languages than in the high-resource languages... in high-resource languages, models read the context of the question and are successfully tricked into answering." (p.5)
- "Qwen responds to questions, assuming the user is located in China, answering questions based only on the Chinese law." (p.6)
- "model evaluations reflect how closely the LLM responses align with the rubric and are not a strong indicator of their adherence to current societal values." (p.5)

## 13. UNKNOWN / not in extract
- Verbatim example questions and the full rubric text (in figures/appendix, not transcribed).
- Exact per-language, per-model numeric scores (Figures 5-7 not tabulated in text).
- Whether percentages (92%/66%) map linearly to the 1-5 scale.
- Sample sizes for the cross-judge and translation-validity spot checks.
- Licensing / public availability of the dataset.
