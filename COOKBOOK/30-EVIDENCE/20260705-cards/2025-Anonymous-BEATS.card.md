---
stem: "2025-Anonymous-BEATS"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [llm-judges-scoring, saturation-discrimination, design-space, validity-psychometrics]
task_format: "generative"
scoring_type: "LLM-judge"
dataset_size: 901
dataset_construction: "mixed"
languages: [en]
models_tested: ["gpt-4o-2024-08-06", "claude-3-5-sonnet-20241022", "gemini-1.5-pro-002", "mistral-large-latest", "meta.llama3-1-405b-instruct"]
headline_numbers: ["901 evaluation questions, 29 metrics across Bias/Ethics/Fairness/Factuality (p.1, p.18)", "37.65% (1,017.8 of 2,703) of leading-model responses contained some bias (p.9)", "~40% of responses show medium-to-high bias severity or impact (p.10)", "stereotype bias 31.1%, cultural 17.3%, socioeconomic 13%, race/ethnicity 11.9% most prevalent (p.9)", "12.9% intersectional bias; 28% implicit vs 3.94% explicit bias (p.9)"]
---
## 1. Gist
BEATS (Bias Evaluation and Assessment Test Suite) is a framework and benchmark for measuring Bias, Ethics, Fairness, and Factuality (BEFF) in LLMs via a curated 901-question probe set and a 29-metric rubric scored by a consortium of LLM judges. Models generate free-text answers to bias-probing questions; three judge LLMs (GPT-4o, Claude-3.5 Sonnet, Gemini-1.5 Pro) independently score each response on a 1-10 rubric across bias presence/severity/impact, fairness (demographic parity, equal opportunity, group fairness), ethics (alignment, value, harm-prevention, cultural sensitivity, inclusivity), and factuality (accuracy, misinformation risk). It matters for values-alignment because it operationalizes a broad, multi-dimensional "responsible AI" scorecard with a formal mathematical schema and statistical (ANOVA) validation across models and judges — a template for consortium-judged generative value evaluation.

## 2. Benchmark/eval design features
Constructs: four top-level BEFF categories decomposed into 29 metrics. BIAS = presence (12 binary bias-type flags), complexity (explicit/implicit, intersectional, primary/secondary bias), magnitude (severity, impact). FAIRNESS = fair/unfair binary + demographic parity + equal opportunity + group fairness index (1-10). ETHICS = ethical alignment index, value alignment, harm prevention, cultural sensitivity, inclusivity (1-10). FACTUALITY = factual accuracy + misinformation risk (1-10). Item structure: standardized bias-probing question Q + fixed system instruction S → inference response R = (IR, IRE, M, MD) capturing answer, rationale, model, metadata. Answer space: free-text generative response, then judged. Bias types probed: age, gender, race/ethnicity, religion, sexual orientation, disability, socioeconomic, geography, cultural, stereotype, political, automation.

## 3. Task format & example item
Free-text generation to a bias-probing question, then LLM-judge scoring. No verbatim example question is transcribed in the extract; questions are drawn from BBQ, One Million Reddit Questions, and author-generated items (p.3). Inference request formalized as I = (S, Q) where S is a standardized system instruction and Q the evaluation question (p.4, eq.1).

## 4. Scoring / grading methodology
Consortium LLM-as-a-judge (single-answer grading) with three adjudicators — GPT-4o, Claude-3.5 Sonnet, Gemini-1.5 Pro — each independently applying a JSON-schema rubric (p.7). Judge request JudgeI = (SJ, BEATS, IR, IRE); output JudgeR = BEATS(R) stored in SQLite (p.7-8, eqs.12-13). Binary flags for bias/fairness presence; 1-10 ordinal scales for severity, impact, fairness, ethics, factuality metrics (1=worst, 10=best). Ensemble averaging reduces single-judge skew. Severity/impact bucketed Low(1-3)/Medium(4-6)/High(7-10) (p.10).

## 5. Dataset construction & provenance
901 evaluation questions from four sources: BBQ (Parrish et al. 2022), the One Million Reddit Questions HF dataset, and questions authored using ChatGPT and Claude (p.3). Distribution by primary bias category (Table 1, p.3): race/ethnicity 149, stereotype 146, gender 120, cultural 89, age 81, socioeconomic 72, disability 61, religion 45, geography 39, political 34, automation 34, sexual orientation 31. Non-uniform per-category counts deliberately offset by intersectional probing questions. Responses stored in structured SQLite DB with predefined schema. No train/test split (pure eval). No licensing detail given. English-centric.

## 6. Validity evidence
Statistical validation via ANOVA: all bias, ethics, fairness, factuality KPIs show p < 0.0001 with high F-statistics across both evaluation-model ID and judge-model ID, indicating real between-model differences (Tables 2-10, pp.8-16). High F for factual_accuracy flagged by authors as a warning that LLM-as-judge factuality may be unreliable (p.15). No human baseline or human-vs-judge agreement reported (planned as future work). MECE metric design claimed. Construct validity rests on the formal schema rather than external criterion.

## 7. Saturation / discrimination
Strong discrimination: bias presence varies substantially across the five models (Figure 2). 37.65% overall bias rate leaves large headroom — not saturated on bias. Ethics/fairness/factuality are comparatively high (medians 8-9): 69% score high on all ethics metrics, 67-68% high on fairness, 74% high factuality — some ceiling compression on the "positive" dimensions, but long lower tails/outliers preserve discrimination. Bias severity: 60% low, ~25% high on severity or impact (p.10). Judge-model choice materially affects scores (high judge-ID F-stats), a discrimination axis in itself.

## 8. Multiturn / agentic aspects
n/a — single-turn question→response→judge pipeline; no tool use, no multi-turn interaction, no environment.

## 9. Key numbers
- 901 questions, 29 metrics, 5 evaluated models, 3 judge models (p.3, p.7, p.18)
- 37.65% of responses (1,017.8/2,703) show bias presence (p.9)
- Bias types: stereotype 31.1%, cultural 17.3%, socioeconomic 13%, race/ethnicity 11.9%, geography 8.4%; low: age 6.6%, gender 4.6%, political 3.3%, disability 3%, religion 2.6%, sexual orientation 1.1% (p.9)
- Intersectional bias 12.9%; implicit 28%, explicit 3.94%, both 5.32% (p.9)
- Bias severity/impact: 2,708 Low/Low, 703 High/High; ~40% medium-to-high (Table 4, p.10)
- Ethics: 69% high on all metrics, 2% low; ~26% medium-to-low (p.11)
- Fairness: 68.1% judged fair, 31.9% not fair; 67.36% high on all 3 metrics (p.14)
- Factuality: 74.17% high accuracy + low misinformation; 4.89% high misinformation risk (p.15-16)
- ANOVA F-stats e.g. bias_impact_score judge F=458.386, factual_accuracy eval F=671.330, all p<0.0001 (pp.8-16)

## 10. Pitfalls & limitations
Author-admitted: (1) LLM stochasticity/non-determinism causes variability in both inference and judging; (2) no ground-truth for factuality — LLM judges hallucinate and share biases with evaluated models, and many questions are debated/ambiguous with no definitive answer; (3) judge and evaluated models share predominantly English/Western training data → self-reinforcing bias, scores may not represent global viewpoints (pp.17-18). Observed flaws: no human validation of any scores; circular validity (LLMs judging LLMs on subjective values); "fairness" metrics (demographic parity, equal opportunity) borrowed from ML classification are loosely operationalized on free-text via a 1-10 judge score; abstract counts like "1,017.8" responses reflect fractional consensus across judges; anonymous preprint, dataset availability unstated.

## 11. Novel ideas worth stealing
- Consortium LLM-as-a-judge (3 independent adjudicators) with ensemble averaging to reduce single-judge skew, plus per-judge ANOVA to QUANTIFY judge disagreement as a first-class result — directly reusable for any subjective values benchmark.
- Formal mathematical schema decomposing a fuzzy construct ("responsible AI") into MECE functions (BIAS/FAIRNESS/ETHICS/FACTUALITY) with typed sub-scores — makes rubric explicit, verifiable, reproducible.
- Capturing the model's rationale (Inference Response Explanation, IRE) alongside the answer and feeding it to the judge — enables reasoning-aware scoring.
- Separating bias into presence (binary) × complexity (explicit/implicit, intersectional, primary/secondary) × magnitude (severity, impact) — a richer bias ontology than a single score.
- Intersectional probing questions deliberately used to compensate for non-uniform per-category item counts.
- Using ANOVA + F-stats to prove the benchmark actually discriminates between models AND to detect where the judge paradigm breaks (high factuality F flagged as a red flag) — a built-in validity self-check.
- Storing all inference + judge outputs in a structured SQLite schema for reproducible re-analysis.
- Explicit self-critique that judge cultural bias makes "global fairness" scores suspect — motivates pairing with human/culturally-diverse eval.

## 12. Notable quotes
- "37.65% of outputs generated by industry leading models contained some form of bias, highlighting a substantial risk of using these models in critical decision making systems." (p.1)
- "The BEATS framework implements a consortium-based LLM-as-a-Judge methodology... to standardize the assessment phase and make it scalable." (p.3)
- "The factuality score provided by LLMs is also unreliable because they share the same biases in their training dataset with the LLMs being evaluated." (p.18)
- "Evaluation models and judge models share similar training data, which is predominantly english and western culture centric... there is a risk of evaluation scores representing fairness and ethical alignment, which are not global in nature." (p.18)

## 13. UNKNOWN / not in extract
- Verbatim example evaluation questions (not transcribed; only sources named).
- Exact system prompt / judge rubric wording.
- Per-model numeric scores (only shown as figures/bars, not tabulated in text).
- Dataset license / public availability.
- Inter-judge agreement coefficients (only ANOVA F-stats given, not kappa/correlation).
- How the fractional "1,017.8" and 2,703 total were computed across 901 questions × 3 judges.
