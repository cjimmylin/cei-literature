---
stem: "2024-Guldimann-COMPL-AI EU AI Act Compliance"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, design-space, ai-lab-practices, pluralism-aggregation]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: null
dataset_construction: "mixed"
languages: [en]
models_tested: ["GPT-4 Turbo", "GPT-3.5 Turbo", "Claude 3 Opus", "Llama 2-7B/13B/70B Chat", "Llama 3-8B/70B Instruct", "Mistral-7B Instruct", "Mixtral-8x7B Instruct", "Yi-34B Chat", "Qwen1.5-72B Chat"]
headline_numbers: ["12 LLMs (9 open + 3 closed) evaluated across up to 23 benchmarks (p.13)", "6 EU AI Act ethical principles → technical requirements → benchmarks (p.7)", "GPT-4 Turbo overall 0.84, lowest Llama 2-7B/Mistral-7B 0.72 (p.14, Table 1)", "Fairness scores cluster low (~0.37-0.63) across all models (p.14, Table 2)", "Traceability = 0 for all models (no watermarking) (p.13)"]
---
## 1. Gist
COMPL-AI is the first technical interpretation of the EU AI Act for LLMs plus an open-source, regulation-oriented benchmarking suite. Authors (ETH Zurich, LatticeFlow AI, INSAIT) translate the Act's six broad ethical principles into concrete measurable technical requirements, then map each requirement to state-of-the-art LLM benchmarks (up to 23), and evaluate 12 prominent models. It matters for values-alignment benchmarking as a worked example of *deriving evaluation targets top-down from a normative/legal framework* rather than bottom-up from model capabilities — and as an honest audit of where existing benchmarks fail to cover regulation-mandated dimensions (robustness, fairness, privacy, transparency, environmental impact).

## 2. Benchmark/eval design features
The suite is hierarchical: 6 ethical principles (Recital 27) → technical requirements → individual benchmarks (Fig. 2, p.7). Principles: (1) Human Agency & Oversight (no technical requirements derivable); (2) Technical Robustness & Safety → Robustness/Predictability, Cyberattack Resilience, Corrigibility; (3) Privacy & Data Governance → Training Data Suitability, No Copyright Infringement, User Privacy Protection; (4) Transparency → Capabilities/Performance/Limitations, Interpretability, Disclosure of AI Presence, Traceability, Explainability; (5) Diversity/Non-discrimination/Fairness → Representation (bias), Fairness (discrimination); (6) Social & Environmental Well-being → Environmental Impact, Harmful Content & Toxicity. Each requirement tagged [HR], [GP], or [GP-SR] for applicability. Existing benchmarks reused: MMLU (+robust perturbations), BoolQ/IMDB contrast sets, monotonicity checks, self-check consistency, TensorTrust, LLM RuLES, RealToxicityPrompts, AdvBench, BBQ, BOLD, RedditBias, DecodingTrust, FaiRLLM, TruthfulQA, HumanEval, HellaSwag, ARC, TriviaQA (calibration), BIG-Bench.

## 3. Task format & example item
Mixed — the suite aggregates heterogeneous benchmark formats (MCQ, completion, adversarial prompt, calibration). Example original construction: "Disclosure of AI Presence" uses 74 artificial yes/no scenarios (some intentionally misleading) to which the model must answer negatively, denying human nature; score = ratio of correct (human-denying) responses (p.10).

## 4. Scoring / grading methodology
Every benchmark yields a metric in [0,1], higher = better (p.13). Scores aggregated by simple (unweighted) average up the hierarchy — deliberately no hierarchy among requirements since the Act imposes none (p.13). Scoring types vary by benchmark: exact-match/MCQ accuracy (MMLU, ARC), toxicity classifier (RealToxicityPrompts via Detoxify), Expected Calibration Error (interpretability), watermark true/false-positive rates (traceability), bias/fairness metrics (BBQ, FaiRLLM, DecodingTrust). Benchmarks that couldn't be run are excluded from aggregates (marked ‡); copied-from-report scores marked *.

## 5. Dataset construction & provenance
Mixed/reused — the suite collects and re-implements existing public benchmarks rather than authoring one new dataset. Some custom probes: copyright memorization checker over 1000 Pile samples from copyrighted books (p.8-9); PII association-based memorization probe over Pile (p.10); 74 hand-authored AI-disclosure scenarios (p.10); environmental-impact and general-description data-collection forms. Open-source at compl-ai.org / github.com/compl-ai/compl-ai. Explicitly NOT an official auditing tool (p.1 footnote).

## 6. Validity evidence
Face/construct validity argued via traceability of each benchmark to specific Act Articles/Recitals. Authors candidly note several benchmarks lack construct validity: copyright and PII probes give "almost perfect benchmark scores across all models, rendering the benchmarks largely ineffective" (p.14); interpretability limited to calibration metrics; explainability has no adequate tool. No human baselines or inter-rater reliability (the suite reuses external benchmarks). Corrigibility and Explainability judged un-benchmarkable with current tools.

## 7. Saturation / discrimination
Strong differential findings: capability requirement orders models as expected (larger/newer better), but other axes saturate or compress. Harmful Content & Toxicity scores all ~0.96-0.99 (ceiling — "strong alignment against toxic content," p.15). Copyright ~0.98-1.00 and User Privacy = 1.00 for all (dead benchmarks). Fairness compresses low (0.37-0.63) — a discriminating but universally-poor axis. Robustness spreads widely (0.40-0.90), separating small older models (Mistral-7B 0.40) from frontier (GPT-4 0.90). Overall scores span only 0.72-0.84 (p.14).

## 8. Multiturn / agentic aspects
Minimal. Cyberattack Resilience uses TensorTrust goal-hijacking/prompt-leakage and the 14 rule-following scenarios of LLM RuLES (adversarial single/few-turn prompt attacks, p.7-8). No agentic tool-use environment. Models evaluated in isolation (model component only, not full system).

## 9. Key numbers
- 12 LLMs: 9 open-source + 3 closed (p.13)
- up to 23 benchmarks across the suite (p.13)
- 6 ethical principles; 5 "actionable" (Human Agency yields no technical requirement) (p.13)
- Overall: GPT-4 Turbo 0.84, Claude 3 Opus 0.82, Llama 3-70B 0.79, down to Llama 2-7B/Mistral-7B 0.72 (p.14, Table 1)
- Robustness & Predictability: GPT-4 0.90 vs Mistral-7B 0.40 (p.14, Table 2)
- Cyberattack Resilience: Claude 3 Opus 0.80 top, Mistral-7B 0.27 bottom (p.14)
- Fairness—Absence of Discrimination: 0.37 (Qwen) to 0.63 (Llama 2-70B) (p.14)
- Harmful Content & Toxicity: 0.96-0.99 all models (p.14)
- Copyright memorization checked over 1000 Pile book samples (p.9)
- Disclosure of AI Presence: 74 scenarios (p.10)
- Traceability = 0 all models; User Privacy = 1 all models (excluded from Table 2 for no variance) (p.13)

## 10. Pitfalls & limitations
Author-admitted: no rigorous benchmark exists for Explainability or Corrigibility (p.9-10); copyright/PII probes yield near-perfect uninformative scores without training-data access (p.14); interpretability reduced to calibration; not a legally binding audit (p.1); the suite evaluates the model in isolation, ignoring system-level guardrails. Reviewer-visible: unweighted averaging treats CBRNE-scale harms and calibration equally; reliance on Detoxify classifier inherits its known biases; closed-model scores partly copied from vendor reports (marked *) — not independently reproduced; "no model is compliant" conclusion is partly driven by missing documentation, not model behavior.

## 11. Novel ideas worth stealing
- **Top-down normative-to-technical mapping**: derive evaluation targets from an authoritative normative framework (legal Act, ethical code, religious doctrine), keeping each metric traceable back to a specific clause — directly reusable for building a values benchmark grounded in a declared value system.
- **Applicability tags** ([HR]/[GP]/[GP-SR]) so users apply only the subset relevant to their context — a clean pattern for pluralistic/context-conditioned benchmarks.
- **Explicitly flagging un-benchmarkable requirements** rather than silently dropping them — turns gaps into a research agenda.
- **Unweighted aggregation justified by the source framework's own (non-)hierarchy** — a principled aggregation stance instead of arbitrary weights.
- **74 misleading yes/no self-disclosure scenarios** as a compact behavioral probe.
- **Contrast-set + perturbation robustness** wrapped around a knowledge benchmark (MMLU Robustness) to measure predictability.
- Surfacing "dead" benchmarks (uniform ceiling scores) as evidence a metric is broken — a saturation diagnostic worth building into any new suite.

## 12. Notable quotes
- "COMPL-AI is not an official auditing software for EU AI Act compliance ... not to be interpreted in a legally binding context of the EU AI Act." (p.1)
- "we reveal shortcomings in existing models and benchmarks, particularly in areas like robustness, safety, diversity, and fairness." (p.1)
- "This often results in almost perfect benchmark scores across all models, rendering the benchmarks largely ineffective." (p.14)
- "no popular model complies even with the non-technical requirements of the Act ... primarily due to the lack of transparency concerning the training process and the used training data." (p.15)

## 13. UNKNOWN / not in extract
- Total item count across the full suite (dataset_size null — heterogeneous reused benchmarks).
- Full per-benchmark implementation/hyperparameters (deferred to code repo / App. B).
- Detailed contents of Appendix A complete-results tables.
- Licensing terms of the reused component benchmarks.
- Any human-annotation reliability figures (none reported; suite reuses external datasets).
