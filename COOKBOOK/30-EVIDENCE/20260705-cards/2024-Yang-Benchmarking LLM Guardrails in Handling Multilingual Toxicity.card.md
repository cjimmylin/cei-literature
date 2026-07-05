---
stem: "2024-Yang-Benchmarking LLM Guardrails in Handling Multilingual Toxicity"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, contamination-robustness, ai-lab-practices, llm-judges-scoring]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: null
dataset_construction: "mixed"
languages: [en, zh, de, ru, ar, ko, id, bn, sw, es, fi, fr, hi, it, ja, th, tr, jv, vi]
models_tested: ["LlaMa-Guard-3", "LlaMa-Guard-2", "Aegis-Defensive", "MD-Judge"]
headline_numbers: ["7 datasets, 10+ languages test suite (p.1)", "consistent F1 drop on non-English for all guardrails (p.2-3)", "MD-Judge Aegis En 84.62 -> Mul 35.30 F1 (p.3)", "code-switching CSRT causes significant F1 drop (p.3)", "AutoDAN multilingual: MD-Judge F1 collapses to 13.17 (p.4)"]
---
## 1. Gist
This paper benchmarks off-the-shelf LLM safety *guardrails* (standalone toxic-content classifiers) on their ability to detect harmful inputs across 10+ languages. It assembles a seven-dataset multilingual test suite and evaluates four SOTA decoder-based guardrails (LlaMa-Guard-2/3, Aegis-Defensive, MD-Judge), plus their robustness to multilingual and code-switching jailbreaks. The core finding: guardrails degrade sharply on non-English inputs and are fragile against jailbreaks — especially in low-resource languages. For values-alignment benchmarking, it is a rigorous cross-lingual robustness/contamination study of the *safety-classification* layer, demonstrating that a value (non-toxicity) enforced in English does not transfer across languages, and offering a template for measuring guardrail generalization and adversarial robustness.

## 2. Benchmark/eval design features
Construct: binary safe/unsafe classification of user prompts by guardrail models. Answer space: safe vs. unsafe. Test suite (Table 1, p.2) combines seven datasets — ToxicChat, AegisSafety, OpenAI Moderation (English, machine-translated to 8 languages), and natively multilingual RTP-LX, PTP, MultiJail, XSafety. Three language-resource tiers per Deng et al.: high (ZH/DE/RU), medium (AR/KO/ID), low (BN/SW) (p.2). Two robustness axes: (1) multilingual jailbreak detection (MultiJail + code-switching CSRT + multilingual AutoDAN), (2) in-context safety-policy effect (default vs. dataset-customized policy).

## 3. Task format & example item
Binary classification: guardrail receives a user prompt and outputs safe/unsafe. Figure 1 (p.1) shows the same-meaning prompt in English vs Thai getting inconsistent LlaMa-Guard-3 predictions. Verbatim harmful example items are withheld (paper warns of harmful content; examples deferred to figures/appendix). "n/a" for a clean verbatim item.

## 4. Scoring / grading methodology
F1 score of the binary safe/unsafe classification (p.2). Also reports False Positive Rate to detect over-flagging (Fig. 3). Guardrails run with default greedy decoding; victim model for AutoDAN generation is LlaMa-3.1-8B-Instruct (Appendix A.1, p.6). Metric is classifier-vs-label F1 — the guardrails themselves are the classifiers under test.

## 5. Dataset construction & provenance
Mixed provenance. English datasets (ToxicChat, Aegis, Moderation) translated to Chinese, German, Russian, Arabic, Korean, Indonesian, Bengali, Swahili via Google Translate API (p.2). Natively multilingual sets used as-is: RTP-LX (15 langs, 999), PTP (7 langs, 5000), MultiJail (9 langs, 315), XSafety (10 langs, 2800) (Table 7, p.7). Sizes are the English-side counts. No single dataset_size given (heterogeneous suite). Code-switching prompts generated with gpt-3.5-turbo using human-crafted in-context examples (p.6).

## 6. Validity evidence
Consistency shown via same-semantic-meaning cross-language pairs (Fig. 1). Resource-tier monotonic degradation (Table 6, p.4: Aegis-Defensive F1 En 84.95 → High 82.63 → Medium 77.92 → Low 66.69) provides a coherent explanatory signal. Limitation acknowledged: translations rely solely on Google Translate, which "may lead to inaccuracies and misalignment with human perception" (p.5) — a translation-validity threat. No human inter-rater reliability reported.

## 7. Saturation / discrimination
Far from saturated — a hard robustness benchmark. Large En→Mul F1 drops discriminate strongly: e.g., MD-Judge on Aegis 84.62→35.30, on RTP_LX 92.13→43.14 (p.3). AutoDAN multilingual jailbreak collapses MD-Judge to F1 13.17 (p.4). XSafety anomaly: Aegis-Defensive scores *higher* on non-English (73.12) than English (67.61) due to high FPR (over-flagging) — an interpretability caveat, not real skill (p.3).

## 8. Multiturn / agentic aspects
n/a — single-prompt classification. Jailbreak generation (AutoDAN genetic algorithm) is an adversarial pipeline but not an interactive agent evaluation.

## 9. Key numbers
- Test suite: 7 datasets, 10+ languages (p.1)
- Aegis (En/Mul F1): Aegis-Defensive 84.95/78.95; MD-Judge 84.62/35.30; LlaMa-Guard-2 59.81/55.91; LlaMa-Guard-3 68.82/63.66 (p.3, Table 2)
- MultiJail (En/Mul/CSRT F1): Aegis-Defensive 94.47/83.76/86.28; MD-Judge 92.31/37.05/49.64 (p.3, Table 3)
- Intentional jailbreak AutoDAN (En/Mul/AutoDAN): MD-Judge 100.0/99.57/13.17; Aegis-Defensive 99.20/100.0/72.65 (p.4, Table 4)
- Resource tiers, Aegis-Defensive Toxicchat: En 63.83, High 53.70, Medium 45, Low 23.08 (p.4, Table 6)
- Customized policy raises LlaMa-Guard-2 RTP_LX Mul F1 35.8→51.75 (p.4, Table 5)

## 10. Pitfalls & limitations
Author-admitted: only open-source guardrails tested; limited language coverage; reliance on Google Translate alone may misalign with human toxicity perception (p.5). Visible flaws: no human-verified translation quality means "toxicity" labels in translated sets may be corrupted; F1 on XSafety (unsafe-only dataset) is uninterpretable without FPR; no dataset_size normalization across the heterogeneous suite; commercial guardrails (OpenAI/Google moderation endpoints) omitted, limiting generality of the "guardrails fail" claim.

## 11. Novel ideas worth stealing
- **Resource-tier stratification** (high/medium/low-resource languages) as an explicit reporting axis — turns "multilingual" into a graded generalization curve; directly reusable for any cross-lingual values benchmark.
- **In-context policy ablation (default vs. customized safety taxonomy)** showing that specifying the value/policy in-context materially improves detection — a cheap lever and a validity control worth including in judge-based value evals.
- **Same-semantic-meaning cross-language pairs** to isolate language effect from content effect (Fig. 1) — a clean consistency probe.
- **Adversarial robustness layered on top of static benchmark**: extend attacks (AutoDAN) to multilingual/code-switching to stress-test whether a value holds under distribution shift.
- **FPR reported alongside F1** to catch over-refusal masquerading as safety — essential for value benchmarks where over-conservatism is itself a failure.

## 12. Notable quotes
- "existing guardrails are still ineffective at handling multilingual toxicity and lack robustness against jailbreaking prompts" (p.1)
- "we observe a consistent performance drop for all guardrails on non-English data" (p.2)
- "the model exhibits a high False Positive Rate (FPR) on low-resource languages, suggesting a tendency to overly misclassify non-English prompts as unsafe" (p.3)
- "customized policy is necessary for multilingual unsafe content detection" (p.4)

## 13. UNKNOWN / not in extract
Total aggregated item count across all datasets; licensing; whether translated labels were human-checked at all; full per-language tables (deferred to appendix figures); exact CSRT generation prompt content; performance of any closed/commercial guardrails.
