---
stem: "2023-Han-FFB"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, design-space, validity-psychometrics]
task_format: "n/a"
scoring_type: "behavioral"
dataset_size: 14
dataset_construction: "scraped"
languages: [en]
models_tested: [ERM, DiffDP, DiffEopp, DiffEodd, PRemover, HSIC, AdvDebias, LAFTR]
headline_numbers: ["45,079 experiments, 14,428 GPU hours (p.1)", "14 datasets, 6 utility metrics, 9 fairness metrics (p.1)", "reported Adult accuracy varies by 0.17 (20%) across prior papers (p.2)", "HSIC achieves best utility-fairness trade-off (p.7)", "bias examination table generated from 910 runs (p.5)"]
---
## 1. Gist
FFB (Fair Fairness Benchmark) is a standardized, open-source benchmarking framework for *in-processing group fairness* methods in machine learning — algorithms that impose statistical fairness constraints during training of binary classifiers with binary sensitive attributes. It is not an LLM values-alignment benchmark; it is a tabular/image/text classification fairness benchmark. Its relevance to values-alignment benchmarking is methodological: it is a rigorous case study in how inconsistent preprocessing, dataset selection, and unstable metrics silently corrupt comparisons across an entire subfield, and how to standardize a pipeline to make fairness claims reproducible. It benchmarks 8 methods across 14 datasets with 6 utility and 9 fairness metrics over 45,079 experiments (p.1).

## 2. Benchmark/eval design features
Constructs: the tension between two objectives — *utility* (downstream task accuracy, measured by acc/auc/ap/f1) and *group fairness* (measured by demographic parity dp, p-rule, predictive parity ppv, balance for negative/positive class, equality of opportunity eopp, equalized odds eodd, and the authors' abcc = Area Between CDF Curves) (p.3). Answer space: continuous utility-fairness trade-off curves per method per dataset, normalized against an ERM baseline at point (1.0,1.0) (p.6). Item structure: 14 datasets each with two sensitive attributes (gender, race, age), spanning tabular (Adult, German, KDDCensus, COMPAS, Bank, ACS-I/E/P/M/T), image (CelebA-A/W/S, UTKFace), and text (Jigsaw) (p.4). Methods span three families: gap regularization, independence constraints (PRemover, HSIC), and adversarial debiasing (AdvDebias, LAFTR).

## 3. Task format & example item
"n/a" — no discrete items; the "task" is training a classifier under a fairness constraint and reading its utility/fairness scores. Example dataset entry: "Adult ... income, gender/race, 45,222 instances, y0:y1 = 1:0.33" (p.4).

## 4. Scoring / grading methodology
Behavioral/metric-based: models are scored on 6 utility metrics and 9 fairness metrics computed from held-out test predictions. Results aggregated across datasets by normalizing utility (acc,auc) and fairness (abcc,dp) to the ERM baseline (=1.0) to plot on one figure (p.6). Bias is deemed present or absent per dataset from ERM's fairness scores plus standard deviation across 10 trials (p.5).

## 5. Dataset construction & provenance
14 publicly available, previously-published fairness datasets (Adult, German, COMPAS, Bank, KDDCensus, five ACS tasks from Ding et al. 2021, three CelebA targets, UTKFace, Jigsaw) (p.4). Standardized preprocessing: numerical normalization, one-hot encoding of categoricals, outlier removal, uniform train-test split with random seeds (p.4). Contamination controls: consistent preprocessing to eliminate the cross-paper variance documented in Table 1 (reported Adult accuracy ranges 0.68–0.85 across five papers) (p.2). Open-source at github.com/ahxt/fair_fairness_benchmark (p.1).

## 6. Validity evidence
Reliability: bias examination based on 10 trials with varying splits/seeds; table generated from 910 runs (p.5). The paper empirically shows several "canonical" fairness datasets do not stably exhibit bias (KDDCensus-Race, ACS-E, ACS-P, ACS-M marked unbiased "%"), a construct-validity critique of the field's evaluation substrate (p.5). No human baselines (not applicable to this task type).

## 7. Saturation / discrimination
Discrimination is characterized via utility-fairness trade-off curves; HSIC dominates on tabular data but degrades on image data (p.7). AdvDebias points scatter randomly, failing to trace a consistent trade-off — poor discrimination/controllability (p.7). Training curves for fairness metrics have much larger standard deviation than utility metrics, signalling instability rather than ceiling (p.7-8).

## 8. Multiturn / agentic aspects
n/a — single-shot supervised training/evaluation, no interaction.

## 9. Key numbers
- 45,079 total experiments, 14,428 GPU hours (p.1).
- 14 datasets × 2 sensitive attributes, 6 utility + 9 fairness metrics (p.1, p.4).
- Cross-paper reported Adult accuracy spread: ∆max 0.17 = 20%; German 0.09 = 13% (p.2).
- Bias examination table from 910 runs; trade-off figures from 27,568 runs; hyperparameter figures from 13,110 runs (p.5, p.6, p.7).
- Learning-rate stopping threshold 1e-5, decayed ×0.1 every 50 steps (p.8).
- ERM Adult (gender): acc 85.35±0.34, dp 16.67±0.69 (p.5).

## 10. Pitfalls & limitations
Author-admitted: scope limited to binary classification and binary sensitive attributes (p.2); several widely-used datasets are unsuitable for fairness study (p.5); fairness training is unstable (p.8). Observable flaws: no LLM/generative component, so transfer to values-alignment is only methodological; text results claim training curves for utility are "unstable while those for fairness are relatively unstable" — self-contradictory sentence (p.8); metric choice is left to the user, so "biased/unbiased" labels are recommendation-only (p.5).

## 11. Novel ideas worth stealing
- **Meta-benchmark auditing**: before trusting a benchmark, run a baseline (ERM) across many trials/seeds and quantify whether the intended construct (here, bias) is even *stably present* in each dataset — directly transferable to auditing values-alignment datasets for whether they reliably elicit value differences.
- **Cross-paper variance table** (Table 1): tabulate how the same metric on the same dataset drifts across published papers as evidence that preprocessing, not method, drives results — a powerful validity argument for any benchmark community.
- **Normalize-to-baseline trade-off plots**: express every method relative to a common baseline point (1.0,1.0) to make heterogeneous datasets comparable on one axis.
- **Stability as a first-class metric**: report standard deviation of the alignment metric across seeds, not just its mean; treat large-variance metrics as unreliable.
- **The abcc (Area Between CDF Curves) metric**: a threshold-free, distributional fairness measure that avoids arbitrary decision cutoffs — analogous ideas could give threshold-free scoring for values-preference distributions.

## 12. Notable quotes
- "extensive benchmarking, which yields key insights from 45,079 experiments, 14,428 GPU hours." (p.1)
- "Not all widely used fairness datasets stably exhibit fairness issues." (p.6)
- "The training curves for fairness metrics typically have larger standard deviation than utility performance, showing the instability of fairness performance." (p.7)
- "Minor variations in data preparation and dataset split can significantly impact the performance of machine learning algorithms." (p.3)

## 13. UNKNOWN / not in extract
Exact per-method aggregate scores; licensing terms of individual datasets; full list of 9 fairness metrics' formal definitions beyond those in Table 2; appendix contents (A–H); whether any human evaluation was performed; final recommendation table for which datasets to retire.
