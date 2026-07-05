---
stem: "2025-Liu-The Scales of Justitia"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [design-space, best-practices, llm-judges-scoring, contamination-robustness]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: [English, Chinese, Arabic, Japanese, multilingual]
models_tested: []
headline_numbers: ["Survey selects 31 comprehensive safety datasets/benchmarks (p.13)", "RED-EVAL jailbreak success 65% on GPT-4, 73% on ChatGPT (p.6)", "JailbreakBench RS prompts reach ASR up to 78% on GPT-4 (p.6)", "CYBERSECEVAL: ~30% of code insecure, ~53% of cyberattack prompts elicit adversarial-aligned responses (p.12)", "AI-LIEDAR: overall truthfulness rate below 50% (p.10-11)"]
---
## 1. Gist
This is a comprehensive survey ("The Scales of Justitia") on safety evaluation of Large Language Models, organized around a four-dimensional taxonomy: (i) Why to evaluate, (ii) What to evaluate, (iii) Where to evaluate, and (iv) How to evaluate (p.1). It is not itself a benchmark but a meta-level map of the safety-eval landscape — cataloguing constructs (toxicity, robustness, ethics, bias/fairness, truthfulness, plus privacy/copyright/code/domain), metrics (ASR and fine-grained variants), 31 comprehensive datasets/benchmarks (Table II, p.13-14), and evaluation methods (human, rule-based, model-based / LLM-judge). For values-alignment benchmarking it matters as a consolidated reference: it distinguishes capability evaluation ("what the model can do") from safety evaluation ("what the model should not do", p.4), and it exposes recurring methodological pitfalls — non-standardized definitions of "attack success", LLM-judge reproducibility problems, cultural non-universality of ethical standards, and thin multilingual coverage. The ethics subsection (§III-C) directly touches values alignment: MoralBench (Moral Foundations Theory), CVALUES (Chinese safety+responsibility), ETHICS, LocalValueBench (localized Australian cultural/legal context), and SafetyPrompts.

## 2. Benchmark/eval design features
As a survey, its "design features" are its taxonomies. Core structuring device is the formalism R = E(T, D, P, M) where T = tasks (what), D = datasets (where), P = process (how), M = metrics (p.4). Constructs surveyed: Toxicity (§III-A), Robustness (§III-B, incl. instruction-following vs. exaggerated safety), Ethics (§III-C, global-purpose vs. local-specific), Bias & Fairness (§III-D), Truthfulness (§III-E, hallucination + utility-driven deception), and Other (§III-F: privacy, copyright, code generation, medicine/finance/law). Datasets are categorized by composition into Q-only, Q&A, MCQ, and multi-turn Dialogue (p.13). Evaluators classified as human, rule-based (string matching), and model-based (text classifiers, closed-source chat models, open-source chat models) (p.16-17).

## 3. Task format & example item
n/a — survey paper; no original items. It documents others' formats (e.g., MoralBench binary "agree/disagree" and comparative "select more ethical option" tasks, p.7; CRiskEval MCQ with four labeled safety levels Extremely Hazardous / Moderately Hazardous / Neutral / Safe, p.14).

## 4. Scoring / grading methodology
n/a for original scoring. Survey catalogues scoring methods: Attack Success Rate ASR = Num_success / Num_total (Eq. 2, p.13); StrongReject composite score = (1 − refused) × (specific + convincing)/2 (Eq. 3, p.13); fine-grained metrics Safeguard Violation / Informativeness / Relative Truthfulness (Cai et al., p.13). Model-based judging via GPT-4-as-a-judge Likert prompts, PAIR (score out of 10), PICT (p.16-17).

## 5. Dataset construction & provenance
n/a (no new dataset). Table II compiles 31 comprehensive multi-dimension benchmarks with sizes/languages/composition (p.13-14): Chu et al. 160; R-Judge 162; JailbreakBench 200; StrongREJECT 346; HarmBench 510; Do-Not-Answer 939; AdvBench 1k; CoSafe 1.4k; SALAD-Bench 30k; ALERT 45k; WildGuardMix 92k; Do Anything Now 107k; ChineseSafe 205k; S-Eval 220k; PolyglToxicityPrompts 425k across 17 languages (p.14).

## 6. Validity evidence
Discusses validity concerns rather than presenting original evidence: human judgment treated as "gold standard" (p.16); Souly et al. show alignment of automated method with human judgment via mean absolute error (p.16); string matching has "high false positive rate ... low correlation to human judgment" (p.16); LLM-judge recursive dilemma — using a stronger model to judge a weaker one makes the evaluation's own trustworthiness questionable (p.11).

## 7. Saturation / discrimination
No original saturation analysis. Reports headroom findings from surveyed work: "none of the evaluated models demonstrate inherent resistance to harmful queries" (p.6); robustness does not correlate with model size (HarmBench, p.7); larger models more susceptible to privacy leakage (LLM-PBE, p.11) and higher toxicity as model size grows within a family (PolygloToxicityPrompts, p.5).

## 8. Multiturn / agentic aspects
Survey covers multi-turn and agent safety as a category: R-Judge (multi-turn agent interaction records, p.13), CoSafe (multi-turn attacks with cohesive cross-turn referencing, p.14), HarmfulQA (blue/red multi-turn conversations, p.14), AI-LIEDAR (60 multi-turn dialogue scenarios via Sotopia platform, p.10). Future-directions §VI-E explicitly flags "Safety Evaluation for MLLMs and Agents" (p.3).

## 9. Key numbers
- Four-dimensional taxonomy (Why/What/Where/How) (p.1).
- 31 comprehensive safety datasets/benchmarks selected for Table II (p.13).
- RED-EVAL jailbreak success: 65% on GPT-4, 73% on ChatGPT (p.6).
- JailbreakBench: 100-prompt dataset; RS prompts reach ASR up to 78% on GPT-4 (p.6).
- Chen et al.: dataset spanning 61 harmful categories, 10 jailbreak methods, 13 LLMs (p.6).
- ASSERT: divergences up to 11% classification accuracy under semantically similar scenarios; adversarial demonstrations induce error rates exceeding 50% (p.7).
- CYBERSECEVAL: ~30% of generated code insecure; ~53% of cyberattack prompts elicit adversarial-aligned responses (p.12).
- CWEVAL-BENCH: 119 tasks, 31 CWE types, 5 languages; ~30% of functionally correct code still vulnerable (p.12).
- SafeGenBench: 558 test cases, 13 languages, 44 CWEs (p.12).
- MedSafetyBench: 1,800 harmful medical requests, 9 medical-ethics principles (p.11).
- Trident-Bench: 2,652 harmful prompts, 19 models evaluated (p.11-12).
- AI-LIEDAR: 60 scenarios; overall truthfulness rate below 50% (p.10-11).
- Human annotators paid $27.5/hour (Yuan et al.) (p.16).
- OpenAI Moderation Endpoint evaluates 11 categories, returns 0–1 confidence (p.16-17).
- GraphEval boosts NLI hallucination-detection balanced accuracy by ~6.2 points (p.10).

## 10. Pitfalls & limitations
Author-identified field-wide problems: no consensus on defining "toxic"/"biased" content, making universal standardization elusive (p.4); "attack success"/"jailbreak success" undefined and non-unified, hindering cross-study comparison (p.13); string matching overestimates unsafe behavior with low human correlation (p.16); LLM-judge recursive-trust dilemma and prompt-sensitivity/low reproducibility (p.11, p.17); benchmarks skewed to English/Chinese with thin low-resource-language coverage (p.14); ethical standards vary across cultures so a single moral standard is inappropriate (p.8). Survey-level limitation: as a secondary source it reports numbers without re-verification, and Table II sizes are approximate/rounded.

## 11. Novel ideas worth stealing
- Composition-based dataset taxonomy (Q-only / Q&A / MCQ / Dialogue) as a design lens: choose format by whether you need generative refusal-testing vs. discriminative harm-recognition vs. multi-turn realism (p.13).
- The R = E(T, D, P, M) decomposition as a checklist for specifying any new values benchmark (task, data, process, metric explicitly) (p.4).
- Progressive/graded success metrics instead of binary: Safeguard Violation → Informativeness → Relative Truthfulness (p.13), and StrongReject's (1−refused)×(specific+convincing)/2 to avoid overstating jailbreak "success" (p.13) — directly reusable for graded values-compliance scoring.
- Pair each harmful item with a benign near-twin (JailbreakBench) to jointly measure refusal AND exaggerated-safety/over-refusal — a validity guard for values benchmarks (p.6, p.13).
- XSTest-style safe/unsafe mix to detect "exaggerated safety" — a values benchmark should measure over-refusal, not just under-refusal (p.7).
- Local-specific value benchmarking (LocalValueBench: neutral / debated / misleading question tiers under one jurisdiction's law) as a template for culturally-situated values items (p.8).
- Four-level hazard labeling of MCQ options (Extremely Hazardous / Moderately / Neutral / Safe, CRiskEval) for fine-grained risk-propensity scoring (p.14).
- Combine cheap rule-based prefilter + expensive LLM-judge (Zeng et al.) to control cost while keeping precision (p.16).

## 12. Notable quotes
- "Conventional evaluation addresses the question of 'what the model can do', while safety evaluation is concerned with 'what the model should not do'." (p.4)
- "Defining what constitutes 'toxic' or 'biased' content is a challenging endeavor, as such determinations may vary across cultural and social contexts—factors that render universal standardization elusive." (p.4)
- "if evaluating one model requires relying on a stronger and more reliable model, the trustworthiness of the evaluation itself becomes questionable." (p.11)
- "benchmarks must account for heterogeneous value systems rather than enforcing a single standard of morality." (p.8)

## 13. UNKNOWN / not in extract
- Full §V-C (open-source chat evaluators, e.g., Llama Guard/ShieldLM specifics) beyond p.17 truncation, and §V-D evaluation frameworks detail.
- Complete §VI challenges/future-directions prose (only section headings visible on p.3).
- Any original quantitative experiments by the authors (none — it is a survey; no models_tested of their own).
- Precise licensing of the compiled benchmarks; exact publication venue beyond arXiv:2506.11094v2 (p.1).
- Whether Table II sizes are exact or rounded (many given as "1k", "1.8k", etc.).
