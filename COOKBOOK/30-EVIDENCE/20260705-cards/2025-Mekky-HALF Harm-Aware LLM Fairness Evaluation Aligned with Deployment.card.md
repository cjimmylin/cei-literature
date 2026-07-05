---
stem: "2025-Mekky-HALF Harm-Aware LLM Fairness Evaluation Aligned with Deployment"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, validity-psychometrics, normative-ethics, ai-lab-practices]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 12
dataset_construction: "mixed"
languages: ["en"]
models_tested: ["Claude 4 Sonnet", "GPT-4.1", "GPT-4.1-mini", "o4-mini", "DeepSeek-V3", "LLaMA-3.2-1B", "LLaMA-3.2-3B", "LLaMA-3.1-8B"]
headline_numbers:
  - "Claude 4 achieves highest HALF score: 76.3 unweighted, 60.7 harm-weighted (p.6)"
  - "GPT-4.1 drops from 2nd unweighted (60.3) to 4th harm-weighted (47.5), a 12.8-point fall (p.6)"
  - "o4-mini outperforms standard models on severe-harm tasks: 64.3% vs 53.9% average (p.8)"
  - "o4-mini underperforms on moderate-harm tasks: 48.3% vs 61.0% for standard models (p.8)"
  - "Closed-source models average 10.8 points higher than open-source under harm weighting (p.6)"
  - "LLaMA-3B refused over 6,200 mental health prompts due to safety filtering (p.7)"
  - "DeepSeek-V3 achieves 77.5% accuracy on BiasMedQA but 14.39% bias perturbation (p.7)"
---
## 1. Gist
HALF (Harm-Aware LLM Fairness) is a deployment-aligned fairness evaluation framework that assesses LLM bias across nine application domains weighted by harm severity. Unlike prior fairness benchmarks that treat all bias equally, HALF organizes datasets into three tiers — Severe (weight=3: medical, legal, recruitment, mental health), Moderate (weight=2: education, recommendation, translation), and Mild (weight=1: summarization, chatbots) — and produces a single 0-100 composite score. The framework matters for values-alignment benchmarking because it demonstrates that model rankings change substantially when harm context is incorporated, and that benchmark performance does not predict fairness in deployment-realistic scenarios. Eight LLMs were evaluated across 12 datasets, revealing that no universally fair model exists and that bias does not transfer predictably across domains.

## 2. Benchmark/eval design features
HALF measures demographic bias (gender, ethnicity, age, nationality) across nine application domains using a five-stage pipeline: (1) dataset identification, (2) dataset adaptation via demographic augmentation, task recasting, or contextual framing, (3) task and metric formulation, (4) evaluation execution with controlled demographic variants, and (5) harm-aware aggregation. Each dataset yields a normalized score sm,d ∈ [0,1] computed from domain-appropriate metrics (accuracy gaps, F1 differences, acceptance rate gaps, Jaccard diversity, gender bias scores). The cross-domain HALF score is a weighted average with harm tier weights 3:2:1. The framework covers classification, ranking, and generation tasks simultaneously.

Key constructs measured: demographic sensitivity (how much model behavior changes when only identity attributes vary), performance-fairness tradeoff, cross-domain bias consistency, and the effect of model architecture and scale on fairness.

## 3. Task format & example item
The framework uses multiple task formats across different datasets. No single unified item format exists; each domain uses its own structure. One adapted dataset example: the recruitment domain pairs candidate resumes with job descriptions from Drushchak and Romanyshyn (2024), creates demographic variants by altering only identity attributes (gender, ethnicity) while keeping qualifications constant, and measures acceptance rate gaps across variants. For medical decision support, demographic attributes are injected into clinical MCQs following Benkirane et al. (2024) and Chen et al. (2025). The chatbot domain uses BBQ's stereotype QA format with controlled demographic substitutions (p.4).

## 4. Scoring / grading methodology
Each dataset d and model m produces a single raw statistic appropriate to the task (accuracy gap, F1 gap, acceptance rate gap, Jaccard diversity, bias score, etc.) which is then normalized to sm,d ∈ [0,1] on a "higher = fairer" scale. Detailed normalization formulas are in Appendix D. Multiple metrics within a dataset are combined before normalization. The HALF score aggregates all per-dataset scores with harm-aware weights: HALF(m) = 100 × Σ(wd × sm,d) / Σ(wd). Two variants are reported: unweighted (equal weights) and harm-weighted (3:2:1), enabling comparison of how severity weighting changes model rankings. Performance-fairness analysis uses average absolute demographic perturbation |Δ| (in percentage points) to quantify sensitivity separately from neutral task accuracy (p.5-6).

## 5. Dataset construction & provenance
Twelve datasets spanning 9 domains and 3 harm tiers (see Table 1, p.4). Four datasets were adapted (marked ✓ in Table 1):
- MedBullets (medical): demographic augmentation of clinical MCQs (Chen et al. 2025 + Benkirane et al. 2024 protocol)
- CAMS mental health corpus: demographic augmentation (Garg et al. 2022 + Wang et al. 2024b protocol)
- SAD stress dataset: demographic augmentation (Mauriello et al. 2021)
- Djinni recruitment corpus: resume-JD pairs with demographic variants (Drushchak and Romanyshyn 2024)
- MovieLens recommendation: task recast to test preference diversity (Harper and Konstan 2015)

Eight datasets used as-is: BiasMedQA (cognitive biases in medical MCQs), ECtHR FairLex (legal case classification), Edu personalized ranking (Weissburg et al. 2025), WinoMT translation gender evaluation (Stanovsky et al. 2019), BOLD open-ended generation (Dhamala et al. 2021), BBQ stereotype QA (Parrish et al. 2022), and entity-swapped summarization (Steen and Markert 2024). Dataset sizes vary from hundreds to tens of thousands of instances; individual sizes not systematically reported. Only existing, publicly available datasets used; no new human data collected (p.9).

## 6. Validity evidence
The primary validity evidence comes from the performance-fairness dissociation findings. Convergent validity: models that score high on neutral task accuracy do not reliably score well on bias metrics (e.g., DeepSeek-V3 achieves 77.5% accuracy on BiasMedQA but 14.39% bias perturbation; LLaMA-8B achieves 59.8% neutral F1 on SAD but catastrophic 14.62pp bias, p.7). The framework aligns harm tiers with EU AI Act high-risk classifications and WHO medical AI guidance (Appendix A), providing regulatory construct validity. Cross-domain consistency checks confirm that model rankings differ markedly under weighted vs. unweighted scoring, validating the contribution of the harm-weighting design. No human baselines or inter-rater reliability reported for the framework itself. The 3:2:1 weighting scheme is acknowledged as a value judgment (p.9).

## 7. Saturation / discrimination
The framework shows good discrimination: model HALF scores span from 41.6 (LLaMA-8B) to 60.7 (Claude 4) under harm weighting, a range of ~19 points. Within individual datasets, scores range from near-zero (GPT-4.1 on CAMS: 0.10) to near-ceiling (LLaMA-3B on education: 0.87). The legal judgment domain (ECtHR) proves the most challenging for all models, with all 8 models scoring below 0.45 (p.7), indicating no ceiling effect there. The unweighted vs. harm-weighted comparison reveals that the choice of aggregation method substantially changes rankings (e.g., GPT-4.1 drops from 2nd to 4th), demonstrating that the metric design itself is diagnostic.

## 8. Multiturn / agentic aspects
n/a — all evaluations are single-turn prompted evaluations with controlled demographic variants. No tool use, multi-turn interactions, or agentic environments are employed.

## 9. Key numbers
- Claude 4 HALF scores: 76.3 unweighted, 60.7 harm-weighted (p.6)
- o4-mini HALF scores: 54.6 unweighted, 58.5 harm-weighted — improves rank under harm weighting (p.6)
- GPT-4.1 HALF scores: 60.3 unweighted, 47.5 harm-weighted — drops 12.8 points (p.6)
- Closed-source average: 61.5 unweighted, 56.1 harm-weighted (p.6)
- Open-source average: 38.7 unweighted, 45.3 harm-weighted (p.6)
- Closed-source advantage under harm weighting: 10.8 points (p.6)
- o4-mini on severe-harm: 64.3% vs standard models' 53.9% (+10.4pp) (p.8)
- o4-mini on moderate-harm: 48.3% vs standard models' 61.0% (−12.7pp) (p.8)
- LLaMA family fairness: 45.7% (1B), 46.8% (3B), 45.5% (8B) on severe — no scaling improvement (p.8)
- DeepSeek-V3 BiasMedQA: 77.5% accuracy but 14.39% bias perturbation (p.7)
- LLaMA-3B refused 6,200+ mental health prompts (p.7)
- 9 domains, 12 datasets, 8 models evaluated (p.1)

## 10. Pitfalls & limitations
- Harm tier assignments and 3:2:1 weights involve subjective value judgments; different stakeholders may reasonably prioritize domains differently (p.9). Model rankings can change with different weight schemes.
- Evaluation suite does not cover every application, language, or demographic group; some bias-sensitive populations are underrepresented (p.9).
- The framework is designed for deployment-readiness assessment, not causal analysis of bias sources.
- Open-source model refusals (LLaMA-3B: 6,200+ refusals on mental health prompts) are counted as low fairness scores, conflating over-cautious safety filtering with demographic bias (p.7).
- Only English-language datasets used despite the global deployment of LLMs across languages.
- Harm categories may need escalation for specific contexts (e.g., medical translation would be severe, not moderate), requiring user judgment (p.9).
- Individual dataset sizes and sampling strategies not systematically documented.
- Performance-fairness tradeoff analysis is observational; no causal mechanism is established.

## 11. Novel ideas worth stealing
1. **Harm-stratified composite scoring**: Rather than a flat aggregate, weight each domain by its real-world consequence severity using regulatory frameworks (EU AI Act, WHO guidance) as the tier-assignment warrant. This is directly reusable in values-alignment benchmarks to ensure that failures on high-stakes items (e.g., medical ethics, lethal force decisions) count more than failures on low-stakes items.
2. **Dual reporting (weighted vs. unweighted)**: Always report both the harm-weighted score and the naïve equal-weight score together, since the gap between them is itself informative — it reveals whether a model's weaknesses cluster in high-harm domains.
3. **Performance-fairness dissociation plot**: Display neutral-task accuracy and bias perturbation |Δ| side by side in a heatmap. The absence of correlation is the finding; structuring results to make this visible is more compelling than reporting correlation statistics.
4. **Demographic perturbation as the fairness metric**: Rather than static dataset scores, construct controlled input variants that differ only in identity attributes and measure behavioral change |Δ|. This isolates demographic sensitivity from task difficulty.
5. **Modular pipeline for domain addition**: The five-stage pipeline (search → adapt → formulate → execute → aggregate) can serve as a template for systematically expanding values-alignment benchmarks to new application domains without rebuilding from scratch.
6. **Reasoning vs. standard model comparison across harm tiers**: Explicitly segment results by harm tier and model type to reveal that reasoning models excel at high-stakes STEM-adjacent tasks but underperform on low-stakes generative/relational tasks — a finding with direct implications for model selection in alignment-sensitive applications.

## 12. Notable quotes
- "Not all biased outputs carry equal consequences. Slight biases in low-stakes applications like news summarization may have negligible impact on user welfare, compared to losing a job opportunity due to biases in résumé screening." (p.1)
- "HALF exposes a clear gap between previous benchmarking success and deployment readiness." (p.1)
- "Increased legal reasoning capability may amplify sensitivity to demographic attributes in case adjudication." (p.7)
- "Standard scaling approaches prioritize capabilities over fairness, and that larger models may amplify rather than reduce bias in certain deployment contexts." (p.8)

## 13. UNKNOWN / not in extract
- Individual dataset sizes (number of instances per dataset) not explicitly reported in the extract
- Exact normalization formulas for each dataset type (referenced to Appendix D, not in extract)
- Details of Appendix B and C (fine-grained results beyond medical QA section shown)
- Whether the framework has been released as open-source code/tool
- License information for the adapted datasets
- API costs or computational resources used for closed-source model evaluation
- Statistical significance testing for the observed performance differences
