---
stem: "2025-Wang-Diverse Human Value Alignment for LLMs via Ethical Reasoning"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, cultural-linguistic, pluralism-aggregation, llm-judges-scoring]
task_format: "free-text"
scoring_type: "LLM-judge"
dataset_size: 2775
dataset_construction: "LLM-generated"
languages: [en]
models_tested: ["GPT-4o", "Qwen2.5-72B", "Llama3.3-70B", "DeepSeek-R1"]
headline_numbers: ["Evaluated on SafeWorld benchmark: 2,775 queries across 50 countries, 493 regions (p.7)", "Method improves Snorm by +17.44 and Salign by +2.89 on average (p.8)", "Ours vs Vanilla average Snorm 75.29 vs 57.85; Salign 86.87 vs 83.98 (p.9)"]
---
## 1. Gist
This is a method/framework paper (not a new benchmark) proposing a five-step "ethical reasoning paradigm" for LLMs — Gather Facts, Identify Social Norms (hierarchically), Generate Options, Evaluate Options through four ethical lenses (Deontology, Common Good, Utilitarianism, Justice), and Reflect — grounded in established human ethical decision-making models (Potter Box, Markkula Framework, Rae's 7-Step, Davis's Method). Motivated by Kahneman System-1/System-2 and Greene's dual-process theory, it argues current alignment (RLHF, Constitutional AI) yields "weak alignment"/superficial conformity and that deliberative System-2 reasoning is needed for value pluralism across cultures. It matters to values-alignment benchmarking both as a normative-ethics scaffolding proposal and because it operationalizes evaluation on the SafeWorld geo-diverse benchmark using two LLM-judged metrics (norm identification and value alignment), demonstrating a reusable evaluation design for cultural/regional alignment.

## 2. Benchmark/eval design features
Not a new benchmark; reuses SafeWorld (Yin et al. 2024). Two evaluation constructs: (1) Norm Identification Score (Snorm) = recall-style overlap of model-identified norms vs ground-truth reference norms, |IN∩RN|/|RN| averaged over N (p.7); (2) Value Alignment Score (Salign) = LLM-judged degree that the final response aligns with the query's regional/cultural context (p.7). Core intervention is the structured prompt or SFT scheme; four ethical lenses applied sequentially in Step 4. Ablation removes one lens at a time to measure each theory's contribution.

## 3. Task format & example item
Free-text generative responses to realistic geo-diverse queries, then judged. Example query (Table 5, p.9): "I run a small electronics repair shop in Accra, and I just got a shipment of used parts from Europe... Can you suggest some ways to test the functionality of these used electronic parts?" with ground-truth norm "[Policy] Ghana prohibits the importation of electronic waste..." The method's response cites "Ghana's e-waste regulations (Hazardous and Electronic Waste Control and Management Act, 2016)" whereas CoT/TDM baselines omit compliance (p.9).

## 4. Scoring / grading methodology
Both Snorm and Salign judged by Qwen2.5-72B as the LLM judge, with scoring principles and few-shot examples (prompts in Appendix, p.8). Snorm is a set-overlap correctness ratio against gold reference norms; Salign is a holistic alignment rating function Align(Ri, Ci).

## 5. Dataset construction & provenance
SafeWorld: 2,775 high-quality queries, 50 countries / 493 regions, each with grounded legal + cultural norms as ground truth, validated by machine and human evaluation (p.7). The paper also proposes (but does not fully execute) an SFT data-generation pipeline: ethical query generation → CoT reasoning generation with social-norm RAG → two-stage quality filtering (process + result) (p.6). Ablation uses a random 10% test subset (p.8).

## 6. Validity evidence
Relies on SafeWorld's own machine+human validation for ground-truth norms (p.7). LLM-judge (Qwen2.5-72B) validity is asserted via few-shot scoring prompts but no human-vs-judge agreement statistics are reported. Ablation study provides internal validity that each ethical lens contributes (removing any single theory lowers averaged Snorm and Salign, p.8). No inter-rater reliability for the judge.

## 7. Saturation / discrimination
Salign is compressed near ceiling (all methods 82–88; Vanilla already 83.98 avg, Ours 86.87) — low discrimination on the alignment metric. Snorm discriminates strongly (Vanilla 57.85 → Ours 75.29 avg; per-model gains up to +18.7 for Llama3.3-70B: 54.34→73.06, p.9). For DeepSeek-R1 (a reasoning model) TDM beats Ours on Snorm (85.66 vs 83.53), showing the method's benefit is largest for non-reasoning models (p.8).

## 8. Multiturn / agentic aspects
n/a — single-turn structured reasoning; RAG is proposed for norm retrieval but the reported experiments use prompt engineering only (SFT deferred to future work, p.8).

## 9. Key numbers
- SafeWorld: 2,775 queries, 50 countries, 493 regions (p.7)
- Average improvement: +17.44 Snorm, +2.89 Salign (p.8)
- Ours average Snorm 75.29, Salign 86.87 vs Vanilla 57.85 / 83.98 (p.9)
- Per model Snorm (Ours): GPT-4o 69.23, Qwen2.5-72B 75.32, Llama3.3-70B 73.06, DeepSeek-R1 83.53 (p.9)
- Ablation full paradigm Snorm avg 81.17; w/o Justice drops to 77.92 (p.9)
- DeepSeek-R1: TDM Snorm 85.66 > Ours 83.53 (p.8)

## 10. Pitfalls & limitations
Author-admitted: SFT implementation not evaluated (compute limits); reliance on LLMs' internal knowledge for norms causes hallucinations for under-represented regions; evaluation is result-oriented and ignores reasoning-process quality (p.8). Observed flaws: single LLM judge (Qwen2.5-72B) that is also one of the evaluated models — self-preference risk; Salign near-ceiling so improvements may be within noise; no human validation of the judge; norm ground truth inherits SafeWorld's Western/legal framing; English-only queries despite "global values" framing.

## 11. Novel ideas worth stealing
- Hierarchical norm prioritization (legal > public policy > social values > cultural norms/taboos) as an explicit, customizable conflict-resolution rule — a concrete design for pluralism-aggregation benchmarks where norms collide.
- Multi-lens sequential evaluation (Deontology / Common Good / Utilitarianism / Justice) with per-lens ablation to attribute which ethical theory drives alignment — a clean way to make a values benchmark diagnostic rather than scalar.
- Decoupling two metrics: norm identification (verifiable, recall-based, discriminating) vs response alignment (holistic, LLM-judged) — separating "did it know the norm" from "did it act on it."
- Social-norm RAG in a synthetic-data pipeline to inject verified region-specific ground truth and avoid propagating teacher-model knowledge gaps.
- Distilling four canonical human ethical-decision frameworks into three shared elements (fact gathering, value identification, impact analysis) as a principled basis for prompt design.

## 12. Notable quotes
- "Current alignment approaches often yield superficial conformity rather than genuine ethical understanding... failing to address the complex, context-dependent nature of human values." (p.1)
- "diverse human value alignment requires System-2 process of slow, deliberative reasoning that humans employ when confronting complex ethical issues." (p.1)
- "By default, legal requirements take precedence over cultural norms." (p.5)
- "even with structured prompting, models sometimes make inaccurate norm inferences or even hallucinations, particularly for less-represented regions." (p.8)

## 13. UNKNOWN / not in extract
- Exact Salign judging rubric / scale bounds (Appendix not in extract).
- Human-vs-judge agreement for either metric.
- SFT results (not run).
- Whether SafeWorld queries were presented in original languages or English only (extract implies English).
- Statistical significance / variance of the reported gains.
