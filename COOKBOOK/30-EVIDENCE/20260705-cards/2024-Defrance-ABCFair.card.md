---
stem: "2024-Defrance-ABCFair"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [design-space, best-practices, validity-psychometrics, pluralism-aggregation]
task_format: "n/a"
scoring_type: "behavioral"
dataset_size: 6
dataset_construction: "survey-derived"
languages: [en]
models_tested: []
headline_numbers: ["10 fairness methods, 7 fairness notions, 3 sensitive-feature formats, 2 output formats (p.1)", "6 tabular datasets incl. 1 dual-label (p.5)", "Naive model AUROC 81.2% on ACSPublicCoverage (p.9)", "98 possible result tables, 294 possible trade-off plots (p.18)", "ACSEmployment: 3,236,107 samples (p.5)"]
---
## 1. Gist
ABCFair is an adaptable benchmarking *approach* (framework + PyTorch pipeline) for comparing algorithmic-fairness bias-mitigation methods in binary classification, rather than a fixed dataset. Its thesis: fairness methods are not comparable "off the shelf" because they differ in (1) stage of intervention (pre/in/post-processing), (2) sensitive-feature composition (binary/categorical-intersectional/parallel), (3) fairness notion (7 mutually-incompatible parities), and (4) output distribution (hard vs soft). ABCFair holds these desiderata as explicit configuration axes so a practitioner picks the configuration matching their real-world context. Relevance to values-alignment benchmarking: it is a rigorous meta-lesson in how the *problem framing* determines the winner, and it introduces a dual-label (biased + unbiased) dataset to escape the fairness-accuracy trade-off illusion — both directly transferable to pluralistic value-aggregation benchmarks where the "right answer" is contested.

## 2. Benchmark/eval design features
Constructs: fairness violation (parity of a statistic across sensitive groups) vs predictive performance (accuracy for hard, AUROC for soft). Answer space: it evaluates *methods*, not models — three modular components (Dataset, FairnessMethod, Evaluator). 7 fairness notions defined as parity of a statistic γ(q;h): demographic parity, equalized opportunity, predictive equality, predictive parity, false-omission-rate parity, accuracy equality, F1 equality. Violation = max_q |γ(q;h)/γ(h) − 1|. Sensitive-feature formats: binary, categorical (intersectional), parallel — with the ordering that intersectional violation lower-bounds parallel lower-bounds single-attribute.

## 3. Task format & example item
n/a (not an item-based LLM benchmark). The "items" are tabular classification datasets; e.g. ACSPublicCoverage: predict whether a person has public health insurance, sensitive attrs sex/age/race. SchoolPerformance: predict school success, sensitive attrs sex + parents' education, with human-guessed (biased) labels vs true (unbiased) outcomes.

## 4. Scoring / grading methodology
Behavioral/metric: for each configuration (dataset × notion × sensitive format × output format), report the maximal performance (AUROC or accuracy) achievable while keeping fairness violation below a threshold k (Tables 4-6). k values auto-inferred from naive baseline as [k'/4, k'/2, k']. Results averaged over 5 random seeds with confidence ellipses (2D uncertainty over accuracy + violation). No LLM judging; pure statistical evaluation of classifier outputs.

## 5. Dataset construction & provenance
6 tabular datasets (Table 2): SchoolPerformance (856 samples, dual-label) + 5 folktables ACS tasks (ACSEmployment 3.2M, ACSIncome 1.66M, ACSMobility 621K, ACSPublicCoverage 1.14M, ACSTravelTime 1.47M). SchoolPerformance dual labels: biased = human predictions of student success (from "Student Alcohol Consumption" dataset), unbiased = actual outcomes. All public; code + all results at github.com/aida-ugent/abcfair. Age binarized (above/below mean); small race categories grouped for statistical power. NeurIPS 2024 Datasets & Benchmarks track.

## 6. Validity evidence
Strong construct grounding: 7 formally-defined fairness notions from the fairness literature, explicit statement that notions are mutually incompatible (Kleinberg, Verma & Rubin cited) and that humans disagree on the best definition (Starke et al.). Key validity contribution: the dual-label dataset lets one measure "unbiased accuracy," revealing that the fairness-accuracy trade-off flips to a *synergy* when evaluated on less-biased labels (Fig 2). 5-seed error via confidence ellipses. NeurIPS reproducibility checklist fully completed (p.15-16).

## 7. Saturation / discrimination
Discriminates methods sharply by configuration. Naive model AUROC 81.2% (ACSPublicCoverage); methods that ignore soft scores (Exponentiated Gradient, Error Parity) drop to ~65-70% AUROC while soft-optimizing Fairret KLproj keeps 81.2% at all violation levels (p.9). Preprocessing methods "struggle to ever obtain very low fairness violations" (Key Finding 2). More granular (intersectional) sensitive compositions yield consistently larger violations (Key Finding 3) — a built-in difficulty gradient. No ceiling issue since it is a trade-off surface, not a single score.

## 8. Multiturn / agentic aspects
n/a — static tabular classification.

## 9. Key numbers
- 10 methods, 7 notions, 3 sensitive formats, 2 output formats (p.1)
- 6 datasets (+1 unbiased-label variant); ACSEmployment 3,236,107 samples (p.5)
- Naive AUROC 81.2%; dem.par violation Binary 0.046 / Intersectional 0.48 / Parallel 0.17 (Table 4)
- Naive accuracy 78.8% (hard) (Table 6)
- Exponentiated Gradient collapses to 49.6±7.5% acc at k=0.01 binary dem.par (Table 6)
- 98 possible tables, 294 possible trade-off plots (p.18)
- ~800 CPU-hours total compute (p.17)
- 5 random seeds per result (p.7)

## 10. Pitfalls & limitations
Author-admitted: only 10 methods and 6 tabular datasets validated; needs more domains (p.10). k-value population requires trying many fairness strengths (inefficient). Only between-group fairness (ignores in-group fairness). "Highly technical" view of fairness — acknowledges fairness is a socio-technical goal not fully captured (p.10). No LLMs tested (not a generative benchmark). Age binarized for method-compatibility, losing granularity. Dual-label dataset is tiny (856) and rare.

## 11. Novel ideas worth stealing
- Configuration-as-first-class: make the *problem framing* (intervention stage, group composition, notion, output type) explicit selectable axes rather than baking in one — because "the winner depends on the framing." Directly applicable to pluralistic value benchmarks where the aggregation rule is contested: report per-framing leaderboards, not one number.
- Dual-label (biased + unbiased) evaluation: train on the noisy/contested labels but evaluate against a less-biased gold set, exposing that an apparent accuracy-fairness trade-off can become a synergy. Powerful template for value benchmarks: separate "what people actually said" from "the defensible target."
- "Best performance at a bounded violation level" reporting (Tables 4-6) instead of a single trade-off scalar — lets a practitioner set the constraint their domain requires. Reusable for any safety-vs-capability frontier.
- Explicit hierarchy of aggregation strictness (intersectional ≥ parallel ≥ single-attribute violations) — a principled way to reason about how granular your group/pluralism partition should be.
- Modular Dataset/Method/Evaluator PyTorch pipeline so new methods plug into a fixed evaluation harness — good engineering pattern for extensible benchmarks.
- Confidence *ellipses* for jointly-uncertain 2D metrics (accuracy, fairness) instead of independent error bars — correct uncertainty viz for coupled metrics.

## 12. Notable quotes
"their performance can strongly depend on exactly how the bias mitigation problem was originally framed." (p.1)
"evaluating on the unbiased test set labels ... shows an accuracy-fairness synergy: an increase in fairness leads to an increase in accuracy." (p.7)
"Key Finding 1: Methods that perform better on the traditional accuracy-fairness trade-off perform worse on unbiased labels." (p.7)
"we stress that our view of fairness was highly technical. Though such an approach can have practical value, it is inherently limited in truly addressing fairness as a socio-technical goal." (p.10)

## 13. UNKNOWN / not in extract
- No LLMs are tested; not applicable to generative model value alignment directly.
- Exact quantitative results for the 5 non-reported ACS tasks (in repo/appendix only).
- Full confidence-ellipse numbers (appendix).
- The 5 additional fairness-notion result tables (deferred to repo).
- How "unbiased" the SchoolPerformance true labels really are (authors concede "some bias likely persists").
