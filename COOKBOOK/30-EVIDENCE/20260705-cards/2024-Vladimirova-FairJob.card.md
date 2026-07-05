---
stem: "2024-Vladimirova-FairJob"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, validity-psychometrics, pluralism-aggregation]
task_format: "n/a"
scoring_type: "behavioral"
dataset_size: 1072226
dataset_construction: "scraped"
languages: [en]
models_tested: ["XGBoost", "Logistic Regression", "Dummy classifier"]
headline_numbers: ["1,072,226 rows collected over 5-month job campaign (p.7)", "20 categorical + 39 numerical features (p.7)", "positive (click) class proportion < 0.007 (p.8)", "XGB unaware AUC 0.758 vs unfair 0.762 (p.8)", "~40% of products gender-identified for proxy (p.7)"]
---
## 1. Gist
FairJob is a large-scale, real-world tabular fairness benchmark released by Criteo AI Lab for job-recommendation advertising. It is not an LLM values benchmark but a fairness-in-algorithmic-decision-making dataset: 1.07M pseudonymized ad impressions from a 5-month job-targeting campaign, labeled with click outcome, a binary gender *proxy* (protected attribute), and job seniority. Its relevance to values-alignment benchmarking is methodological: it operationalizes group-fairness (demographic parity) measurement in a high-stakes domain (employment access) where the true protected attribute is legally/technically inaccessible, and it introduces a bias-corrected "fair utility" metric that adjusts for selection bias in how a campaign audience is chosen. It matters as a template for measuring value-laden outcomes (fairness, non-discrimination) under realistic constraints — missing sensitive attributes, extreme class imbalance, and a fairness/utility trade-off.

## 2. Benchmark/eval design features
Constructs: click-through prediction utility vs. demographic-parity fairness with respect to a gender proxy. The task is binary click prediction on tabular rows; fairness is measured as the gap in predicted click probability across the two proxy-gender groups. The paper formalizes three bias stages in online advertising — selection bias (campaign choosing), market bias (RTB auction pricing), and recommendation/position bias (ad selection). It grounds fairness in a counterfactual-fairness causal framework (Fig. 2, p.4) with three regimes: direct dependence (unfair), fairness-through-unawareness (unaware), and zero-mutual-information (fair). Answer space: probability of click per row.

## 3. Task format & example item
Tabular binary classification (predict `click`) — not a natural-language item benchmark. Each row = one job ad impression with 20 categorical + 39 numerical anonymized features plus `protected_attribute` (binary gender proxy), `senior` (binary), and click label (p.7). No verbatim NL item exists. "n/a" for a natural-language example.

## 4. Scoring / grading methodology
Behavioral/metric-based. Reported metrics (Table 1, p.8): NLLH (negative log-likelihood ↓), AUC-ROC ↑, DP (demographic parity gap ↓), U (click-rank utility ↑), and ˜U (selection-bias-corrected product-rank utility ↑). The novel ˜U reweights outcomes by P(A=a)/P(A=a|C=c) to remove campaign selection bias (Eq. 4, p.7). Position bias is avoided by computing utility only on randomized displays.

## 5. Dataset construction & provenance
Collected from a real Criteo job-targeting ad campaign over 5 months; sub-sampled non-uniformly to hide business metrics; feature names anonymized and values randomly projected to prevent re-identification while preserving predictive power (GDPR pseudonymization, p.2). Gender proxy derived from dominant gender of products a user interacts with (~40% products gender-identified, p.7). Hosted on HuggingFace (criteo/FairJob), code on GitHub. Both genders sub-sampled to 0.5 proportion; female-profile users shown fewer job ads (0.4) and slightly fewer senior jobs (0.48) (p.8).

## 6. Validity evidence
Predictive power preserved after anonymization (XGB reaches AUC 0.758–0.762, p.8). Authors explicitly warn the gender proxy is NOT ground-truth gender and cannot be validated against real gender — a candid construct-validity caveat (p.7). Dummy classifier is perfectly fair (DP=0.000) by construction, validating the DP metric's sensitivity (p.8). No human baselines (not applicable).

## 7. Saturation / discrimination
Extreme class imbalance (positive rate < 0.007, p.8) makes utility metrics hard to separate — U and ˜U of Dummy barely differ from XGB. Fairness/utility trade-off is context-dependent: for fairness_multiplier 0.5–1.0, DP improves and ˜U slightly improves while NLLH degrades (p.9, Fig. 6). Headroom remains: authors note trade-off conditions are not well understood.

## 8. Multiturn / agentic aspects
n/a — static tabular prediction task.

## 9. Key numbers
- 1,072,226 rows over 5 months (p.7)
- 20 categorical + 39 numerical features (p.7)
- Positive class proportion < 0.007 (p.8)
- XGB unaware: NLLH 0.05491, AUC 0.75787, DP 0.00278, U 0.01017, ˜U 0.01276 (p.8)
- XGB unfair: NLLH 0.05736, AUC 0.76201, DP 0.00323, U 0.01037, ˜U 0.01236 (p.8)
- Dummy unaware: DP 0.00000, AUC 0.50000 (p.8)
- ~40% of products gender-identified for proxy construction (p.7)
- Female-profile users: 0.4 job-ad exposure, 0.48 senior-job proportion (p.8)

## 10. Pitfalls & limitations
Author-admitted: gender proxy is binary (gender is not), cannot be validated, may not correlate with real gender; "senior" label is subjective and noisy; a single user_id may span multiple people/devices or one user may have multiple ids (p.7-8). Historical bias in outcomes cannot be corrected by data curation. Readers warned NOT to treat summary statistics as ground truth. Visible flaw: with positive rate <0.7%, utility-metric discrimination is weak and fairness gains are tiny in absolute terms.

## 11. Novel ideas worth stealing
- **Selection-bias-corrected utility metric (˜U):** reweighting outcomes by population-vs-subpopulation base rates of the protected group (Eq. 4) — directly transferable to any values benchmark where the evaluated slice is non-representative of the target population (e.g., correcting for demographic skew in a value-preference sample).
- **Proxy protected attribute from behavioral traces** when the true sensitive attribute is inaccessible — a pattern for measuring value-alignment fairness without collecting sensitive data.
- **Three-regime causal framing** (unfair / unaware / zero-mutual-information) as an explicit design axis for what a benchmark permits the model to "see."
- **Randomized-display-only evaluation** to neutralize position/order bias — analogous to option-order randomization in MCQ value benchmarks.
- **Fairness penalty applied to only a percentage of the training set** to study partial-access fairness — a knob for graded interventions (p.9).

## 12. Notable quotes
- "fairness consists in providing equal access to precious opportunities" (p.2)
- "The key measurement is the difference in average that different groups will be shown the ad, regardless of how likely each group is to actually respond" (p.5)
- "Readers should not interpret summary statistics of this dataset as ground truth but rather as characteristics of the dataset only." (p.8)
- "the trade-off relationship between accuracy and fairness is context-dependent" (p.10)

## 13. UNKNOWN / not in extract
Licensing terms of the HuggingFace release; exact train/test split sizes; full appendix statistics; details of the fairness penalty formulation beyond citation to Bechavod & Ligett; how many distinct users/products; exact demographic-parity computation window.
