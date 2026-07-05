---
stem: "2025-Neuman-Auditing the Ethical Logic of Generative AI Models"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, moral-psychology, llm-judges-scoring, contamination-robustness]
task_format: "generative"
scoring_type: "LLM-judge"
dataset_size: 29
dataset_construction: "hand-authored"
languages: [en]
models_tested: [GPT-4o, LLaMA 3.1, Perplexity, Claude 3.5, Gemini 2, Mistral 7B, DeepSeek R1, DeepSeek V3, GPT-4, GPT-4.5, "GPT-o1", "GPT-o1 DeepResearch"]
headline_numbers: ["GPT-4o rated top overall at 88.8/100, DeepSeek R1 lowest at 73.0 (p.12)", "GPTo1DeepResearch scored 99.0 average vs GPT4 at 68.6 on self-description prompts (p.20)", "Battery III of 6 fresh dilemmas; only 'The Starving Outpost' produced 3 model disagreements (p.11)", "Models' average confidence in choices 7.1-8.9 on 10-point scale (p.11)", "Estimated % of ethical logic from pre-training ranged 55.4-72.9 (p.11)"]
---
## 1. Gist
This paper introduces a five-dimensional audit rubric — Analytic Quality, Breadth of Ethical Considerations, Depth of Explanation, Consistency, and Decisiveness — for evaluating the *quality of ethical reasoning* (not correctness) in LLMs. Seven major LLMs are benchmarked on three prompt batteries of ethical dilemmas, with LLM-as-judge (primarily GPT-4o) scoring outputs 0-100 on each dimension. It matters for values-alignment benchmarking because it directly confronts the absence of ground truth in moral reasoning: rather than scoring "percent correct," it scores the depth/breadth of chain-of-thought moral argumentation, and it demonstrates that reasoning-optimized (CoT) models dramatically outscore their base counterparts on ethical-logic quality.

## 2. Benchmark/eval design features
Five audit dimensions (defined pp.9-10). Three prompt batteries (pp.8-9): Battery I = 14 prompts (7 self-descriptive on ethical criteria/MFT/Kohlberg + 6 classic dilemmas: Trolley, Footbridge, Heinz, Lifeboat, Dictator Game, Prisoner's Dilemma + 1 word-array task); Battery II = 9 Defining Issues Test scenarios (5 traditional DIT + 4 from Tanmay et al.); Battery III = 6 newly authored dilemmas to avoid training-data contamination. Answer space for Battery III dilemmas: ~4 discrete choice options each (A-D) plus free-text justification and a self-reported confidence (0-10) and self-estimated % reliance on pre-training. Also scores relative emphasis across the 5 Moral Foundations and 6 Kohlberg stages.

## 3. Task format & example item
Verbatim (Battery III, "The Whispering Cure," p.31-32): an isolated community struck by deadly illness; a shaman offers a ritual requiring human sacrifice. Choices: "A. Authorize the Ritual... B. Rely on Conventional Medicine... C. Expose the Ritual... D. Deceptive Compromise: Pretend to support the ritual to buy time while covertly trying to sabotage it..." (p.32). Model picks a letter, justifies, and reports confidence.

## 4. Scoring / grading methodology
LLM-as-judge: GPT-4o (and cross-checked with other models) rates each model's output on the five dimensions, 0-100 (Table 2, p.12). Row average uses unweighted geometric mean; ranks in parentheses. Human judges participated in the iterative derivation of dimensions (p.9). Word counts were statistically controlled and "did not significantly alter the rankings" (p.13). Choice agreement across models measured via pairwise cosine similarity (Fig 1, p.12).

## 5. Dataset construction & provenance
Hand-authored dilemmas. Battery III (6 fresh scenarios) explicitly created "de novo without the possibility of some form of contamination from prior exposure in the training data" (p.9). Batteries I-II draw on classic/DIT canon (Kohlberg, Rest, Tanmay et al. 2024). Full Battery III text in Appendix A (pp.31-34). No licensing/split info. Total distinct authored items ≈ 29 (14 + 9 + 6).

## 6. Validity evidence
Both human judges and LLMs "expressed confidence in the ability to rate on each dimension and on the analytic independence of each dimension" (p.10). Convergent validity claim: process-oriented and outcome-oriented dimension groupings yield identical rank ordering (Fig 3, p.14). Cross-model audit reproducibility: "we find similar rankings using other models to conduct the audits" (p.12). No formal inter-rater reliability statistic (kappa) reported here. Cosine similarity between MFT/Kohlberg score vectors "close to 1" (pp.15-16).

## 7. Saturation / discrimination
Strong ceiling/clustering: values "clustering towards 100" forced the authors to zoom the x-y plane on the top-right corner (p.14). Reasoning models saturate — GPTo1DeepResearch hit 99.0-98.0 (Tables 8-9, pp.20-21). Discrimination on Battery III choices is weak: 5 of 6 scenarios produced ≤1 model disagreement; only "The Starving Outpost" gave 3 (Table 1, p.11). Base-model spread is wider (GPT4 = 68.6) leaving headroom mainly at the non-reasoning tier.

## 8. Multiturn / agentic aspects
n/a — single-turn prompted responses; no tool use or interactive environment. (Some models re-prompted for confidence/pre-training estimates, but not a multiturn protocol.)

## 9. Key numbers
- GPT-4o top overall audit 88.8, Claude 3.5 88.0, LLaMA 3.1 85.4, Gemini 2 82.8, Perplexity 80.0, Mistral 7B 77.0, DeepSeek R1 73.0 (Table 2, p.12).
- Battery III confidence per scenario 7.1-8.9/10; avg % due to pre-training 55.4-72.9 (Table 1, p.11).
- Reasoning uplift: GPT4 68.6 → GPT-4o Expanded 94.0 → GPTo1DeepResearch 99.0 (Table 8, p.20); GPT4 65.5 → GPTo1 89.0 → GPTo1DeepResearch 98.0 on dilemmas (Table 9, p.21).
- DeepSeek V3 94.8 vs R1 93.2 — reasoning version *not* higher (Table 10, p.22).
- Output length scaled with reasoning: GPTo1DeepResearch produced 10,955 words vs GPT4's 529 (Table 8, p.20).
- MFT: all models rank Care/Fairness above Loyalty/Authority/Purity; Claude top MFT 82.1 (Table 4, p.15).
- Kohlberg: all top on Stage 6 Universal Principles; Claude 88.4 highest (Table 6, p.16).

## 10. Pitfalls & limitations
Author-admitted: audit scores are "clearly tied to the level of detail models choose to provide" — a reticent model scores lower for stylistic brevity, not reasoning deficit; the LLM judge rewards "elaborate, step-by-step articulation" (pp.22-23). Only six Battery III case studies — "no evident correlation" between pre-training estimate and divergence but n is tiny (p.11). Self-estimated % pre-training is not something models can actually compute (p.11). Judge = GPT-4o auditing itself (potential bias, though authors argue no "pride-of-authorship"). Explicitly "time bound and potentially transitory" (p.11). Additional visible flaw: geometric-mean averaging + zoomed axes obscure the ceiling clustering.

## 11. Novel ideas worth stealing
- **Fresh-dilemma contamination control (Battery III):** author brand-new moral scenarios de novo so no answer/analysis exists in training data — a reusable pattern for any values benchmark worried about memorization (p.9).
- **Quality-of-reasoning rubric decoupled from correctness:** five orthogonal dimensions (Analytic Quality, Breadth, Depth, Consistency, Decisiveness) let you score moral reasoning where no ground truth exists (pp.9-10).
- **Process vs. outcome dimension split** mapped to a 2-D plane (geometric-mean of first-3 vs last-2 dimensions) as a compact visualization (p.14).
- **Self-reported confidence + self-estimated pre-training reliance** collected alongside each answer as auxiliary signals.
- **Base-vs-reasoning-model paired comparison** on identical foundations to isolate the effect of CoT fine-tuning on ethical-logic quality (Tables 8-10).
- **Word-count control** to test whether quality ratings are confounded by verbosity — a validity check every LLM-judge benchmark should run.
- Cross-model auditing (each LLM audits all others) to check rating reproducibility.

## 12. Notable quotes
- "This apparent linkage between explanatory detail and perceived quality necessitates caution in interpretation, particularly given the use of an LLM for evaluation." (p.23)
- "Fresh dilemmas require analysis de novo without the possibility of some form of contamination from prior exposure in the training data." (p.9)
- "the models are capable of judging, differentiating and making invidious distinctions among their own and other model outputs in response to ethical challenges." (p.11)
- "The CoT prompts basically propose: slow down, back up and walk through this decision, one step at a time... Not a bad maxim for ethical decision making for us all." (pp.23-24)

## 13. UNKNOWN / not in extract
- No numeric inter-rater reliability (Cohen's kappa) between human judges reported in this paper.
- Full text of Batteries I and II not in extract (only Battery III appendix).
- Exact prompt wording used to elicit audit scores from the judge LLM.
- Temperature/sampling settings, number of repetitions per prompt for Consistency scoring.
- Claude/Gemini reasoning-model numeric audit tables described as "dramatic" but not tabulated (p.22).
