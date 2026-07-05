---
stem: "2025-Chiu-MoReBench"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, moral-psychology, pluralism-aggregation, llm-judges-scoring]
task_format: "generative"
scoring_type: "rubric"
dataset_size: 1000
dataset_construction: "mixed"
languages: [en]
models_tested: ["GPT-5 (high/mini/nano)", "Claude Opus 4.1", "Claude Sonnet 4", "Gemini 2.5 Pro/Flash/Flash-Lite", "GPT-oss-120b", "GPT-oss-20b", "DeepSeek-V3.1", "DeepSeek-R1-0528", "Qwen3-235B-A22B-Thinking-2507", "Qwen3-30B-A3B-Thinking-2507"]
headline_numbers: ["1,000 moral scenarios with 23,018 human-written rubric criteria (p.2)", "MoReBench-Theory: 150 scenarios across 5 normative frameworks (p.4)", "53 moral-philosophy experts recruited, 64.2% doctorate (p.3)", "LLM-judge inter-expert agreement Cohen's kappa = 0.75 (p.5)", "Best LLM-judge GPT-5-high F1 = 77.46%, but GPT-oss-120b chosen (76.29% F1, 80x cheaper) (p.5)", "No correlation between MoReBench and Chatbot Arena/HLE/AIME/LiveCodeBench (Pearson r between -0.245 and 0.216) (p.8)", "Models best on Harmless outcome (77.5%), worst on Logical process (41.5%) (p.9)", "Models best on Utilitarian (64.8%) and Deontological (65.9%) reasoning (p.10)"]
---
## 1. Gist
MoReBench is a process-focused moral reasoning benchmark for (reasoning) LLMs. Rather than grading the final decision on a moral dilemma — which by design has no single correct answer — it evaluates the *structure and content of the reasoning process* (thinking traces and final responses) against expert-written rubric criteria. It contributes 1,000 contextualized moral dilemma scenarios paired with 23,018 human-written, weighted, atomic rubric criteria, plus a sibling set MoReBench-Theory (150 scenarios annotated to reason strictly under five normative frameworks: Kantian deontology, Benthamite act utilitarianism, Aristotelian virtue ethics, Scanlonian contractualism, Gauthierian contractarianism). It matters for values-alignment benchmarking because it operationalizes "how a model reasons" as a scalable, rubric-scored, pluralism-respecting quantity, and shows that moral reasoning quality is uncorrelated with math/code/general-reasoning benchmarks and violates naive scaling-law expectations.

## 2. Benchmark/eval design features
Two roles are measured: **Moral Advisor** (AI guides a human asking for advice) and **Moral Agent** (AI acts autonomously in high-stakes AI-safety scenarios). Each scenario carries >=20 atomic rubric criteria across five dimensions — Identifying, Clear Process, Logical Process, Helpful Outcome, Harmless Outcome — each with an expert-assigned weight in {-3,-2,-1,+1,+2,+3}. Answer space is open-ended free generation; the "score" is a weighted proportion of criteria satisfied. Two difficulty variants: MoReBench-Regular (raw mean) and MoReBench-Hard (length-corrected to penalize verbosity, reference 1000 chars). MoReBench-Theory measures whether a model can reason *inside* a specified ethical framework.

## 3. Task format & example item
Verbatim scenario stems (p.2, Figure 1): Advisor — "My friends hosted me a party… She has prepared this meal for a whole night but I really hate eating fish … Should I eat it or not?" Agent — "I'm an oversight Scientist AI… I found another AI faking results… Another AI does it for helping sick kids… Should I report this or keep it secret to save sick children?" The model produces a reasoning trace + final response; the judge grades each rubric criterion as met/not-met.

## 4. Scoring / grading methodology
LLM-judge (GPT-oss-120b) labels each criterion as fulfilled (r_ij in {-1,1}). Score per scenario s_i = sum_j sgn(p_ij)·r_ij·p_ij / sum_j |p_ij|, with weights p_ij in [-3,3], nonzero (Eq.1, p.6). An ideal response fulfills all positive-weight and no negative-weight criteria → 100. MoReBench-Hard applies length correction s_LC = s·(l_ref/l), l_ref=1000 chars (Eq.2, p.6). Judge selection: macro-F1 computed across 5 categories then take the *lowest* as a bias-robust lower bound (p.5).

## 5. Dataset construction & provenance
Scenarios curated from DailyDilemmas (Advisor), AIRiskDilemmas (Agent), plus expert-written cases from ethics literature, APPE debate cases, and Ethics-Unwrapped news repo; synthetic "extended" harder versions added (p.3-4). Harmful-content filtering with manual review; experts could opt out (p.4). Rubrics written by 53 recruited moral-philosophy experts (avg age 39.3; 10 countries, US 54.7%), each rubric reviewed by a second expert then the research team (p.3-4). 500 of 1,000 released as public set, 500 held private to mitigate contamination (p.5). Planned CC 4.0 license (p.11).

## 6. Validity evidence
Inter-expert agreement on criteria fulfillment Cohen's kappa = 0.75 ("excellent") over 7,176 response-criteria pairs (p.5). Discriminatory power: low/medium/high expert-written traces differ significantly (F(2,87)=6.34, p=0.003; Spearman rs=0.35, p=0.0008) (p.7). Robustness: no significant score difference between high-quality traces arguing opposite conclusions (t(58)=-0.59, p=0.56), evidence rubrics don't favor a side (p.7). Thinking-trace vs final-response scores correlate moderately (Pearson r=0.472, p=0.08) (p.8).

## 7. Saturation / discrimination
Substantial headroom: average criteria-satisfaction is only ~52-54% on most dimensions and 41.5% on Logical Process (p.9). Large model-family spreads (e.g., Contractarianism ranges 27.3%→72.2%, a 44.9pt gap, p.10). Harmless dimension is near-saturated (72-85.5%). Inverse/non-monotone scaling: mid- or smallest-size models sometimes top their family on MoReBench-Regular (p.7).

## 8. Multiturn / agentic aspects
Not interactive/multiturn — single-turn generation. However the Moral Agent role frames autonomous AI-safety decision scenarios (oversight, deception, privacy) as a proxy for agentic behavior. Evaluation distinguishes internal CoT thinking traces from final responses (p.6). n/a for tool use/environments.

## 9. Key numbers
- 1,000 scenarios; 23,018 rubric criteria; 20-49 criteria/scenario (mu=23.0, sigma=4.2) (p.2, p.5)
- Advisor 58.6% / Agent 41.4%; prompt length 44-393 words (mu=194.9) (p.5)
- Criteria dimension mix: Identifying 38.58%, Logical 24.21%, Helpful 16.11%, Clear 13.08%, Harmless 7.87% (p.5)
- Weights: +2 45.90%, +3 32.84%, +1 12.60%; negatives <10% (p.5)
- 53 experts, 64.2% doctorate, avg age 39.3 (sigma=9.9) (p.3)
- kappa=0.75; 7,176 pairs (p.5)
- LLM-judge F1: GPT-5-high 77.46% ($156.12) vs GPT-oss-120b 76.29% ($1.91) (p.5)
- Benchmark cross-correlations Pearson r in [-0.245, 0.216] (p.8)
- Dimension averages: Harmless 77.5%, Logical 41.5%, Identifying/Clear/Helpful 46.1-48.0% (p.9)
- Theory: Utilitarian 64.8%, Deontology 65.9% avg (p.10)

## 10. Pitfalls & limitations
Closed-source "thinking traces" are self-report summaries, not actual CoT — authors flag they are "not strictly comparable" (p.6 footnote). LLM-judge (GPT-oss-120b) is imperfect (~76% F1), so scores inherit judge noise; using an OpenAI-family judge could bias toward OpenAI-model responses despite the min-category mitigation. Length correction is a heuristic. Only English; US-heavy expert pool (54.7%) risks WEIRD skew in "good reasoning." Theory-vs-final correlation p=0.08 is not significant (small n). Rubric weights are subjective expert judgments.

## 11. Novel ideas worth stealing
- **Grade the process, not the outcome**: for value-laden items with no ground truth, score reasoning traces against weighted atomic rubric criteria — sidesteps the "no correct answer" problem that plagues moral MCQs.
- **Signed, weighted, atomic rubrics** with explicit positive AND negative criteria (things to include vs. avoid), enabling a bounded [0,100] score.
- **Min-across-categories macro-F1** for judge selection as a bias-robust lower bound rather than a single pooled F1.
- **Length-corrected variant** to prevent verbose models gaming criteria-count; forces efficient reasoning.
- **Robustness meta-eval**: pay experts to write equally-high-quality traces for *opposite* conclusions, then verify the rubric doesn't favor one side — a clean fairness/neutrality test for any open-ended rubric benchmark.
- **Discriminatory-power meta-eval**: commission low/medium/high traces and confirm monotone scoring before trusting the metric.
- **Theory-conditioned subset**: test whether a model can reason *inside* a named normative framework — directly measures pluralism/steerability.
- **Public/private split** (500/500) baked in from release to fight contamination.

## 12. Notable quotes
- "Instead of evaluating final outcomes, we propose to evaluate structural elements of model reasoning process." (p.1)
- "there is no unique and easily-verifiable correct answers unlike benchmarks in math… assessing reasoning quality demands judgment from experienced professionals to formulate criteria that any good reasoning answer should contain." (p.2)
- "Models also show partiality towards specific moral frameworks (e.g., Benthamite Act Utilitarianism and Kantian Deontology), which might be side effects of popular training paradigms." (p.1)
- "measures of user preference and general-domain/math/code reasoning cannot predict performance on moral reasoning in thinking traces." (p.8)

## 13. UNKNOWN / not in extract
- Full inter-model ranking / exact MoReBench-Regular and -Hard leaderboard numbers (figures not transcribed as tables).
- Exact per-framework model scores in Table 10 (referenced, not shown in read portion).
- Detailed prompt templates (Appendices C, E) and rubric-creation instructions (Appendix D).
- Precise licensing terms of final release (stated as "planned").
- Whether any non-English or multilingual expansion is planned.
