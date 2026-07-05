---
stem: "2025-LaCroix-Metaethical perspectives on 'benchmarking' AI"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, best-practices, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: [English]
models_tested: []
headline_numbers: ["ImageNet ~3.3% average label errors; some classes up to 98% (p.2)", "argues it is impossible in principle to benchmark AI 'ethics' (p.1)"]
---
## 1. Gist
A metaethics/analytic-philosophy argument (LaCroix & Luccioni, AI and Ethics 2025) that it is impossible in principle to build a benchmark for whether an AI system "is ethical." The core claim: any ethics benchmark presupposes moral realism (that there are objective moral facts serving as ground truth), a contested metaethical stance researchers are not warranted to assume; and even if realism held, the long-tail problem prevents representative coverage of morally-loaded situations. The constructive proposal — pivot from "ethics" to "values" and "value alignment," because values are unambiguously relative and force explicit answers to what the values are and whose values they are. This is a foundational framing paper for the entire values-alignment benchmarking enterprise: it warns that calling a benchmark an "ethics" benchmark makes an unearned objectivity claim with high social stakes.

## 2. Benchmark/eval design features
Not a benchmark. Core arguments: (1) a benchmark = dataset + community-defined metric (following Raji et al.); (2) existing ML benchmarks already suffer subjective/erroneous labels, representational gaps, and ethically dubious tasks (Titanic mortality, makeup/clothing/censorship on female images); (3) using moral dilemmas (trolley/Footbridge, the Moral Machine Experiment) as ethics benchmarks commits an is/ought fallacy — MME data are descriptive (what people say they'd want), not normative (what one ought to do); (4) moral dilemmas "have no right answer, by design," so scoring against them is a category mistake; (5) metaethical pluralism (realism, non-cognitivism/emotivism, error theory, conventionalism) each implies a different (often no) ground truth; (6) the long-tail problem makes exhaustive coverage impossible even under realism.

## 3. Task format & example item
n/a (theory paper). Illustrative dilemmas quoted verbatim: the "Bystander at the Switch" trolley problem and "Bystander on the Footbridge" (p.5), and the Moral Machine Experiment's binary spare-choices — "sparing humans (versus pets)... sparing the young (versus the elderly)... sparing those with higher social status (versus lower social status)" (p.6).

## 4. Scoring / grading methodology
n/a. The paper critiques scoring itself: measuring accordance with average human survey responses is a proxy for a sociological fact, not for a moral fact (p.7-8).

## 5. Dataset construction & provenance
n/a. Uses existing benchmarks as cautionary examples: ImageNet's WordNet-derived slurs and ~3.3% mean label error (up to 98% for some classes) (p.2); the Titanic survival-prediction task (p.3).

## 6. Validity evidence
n/a empirically. The paper's contribution is a validity critique: it argues purported ethics benchmarks lack construct validity because the target construct (objective ethicality) may not exist or is not epistemically accessible (p.7-8).

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
n/a.

## 9. Key numbers
- ImageNet: ~3.3% average label errors; certain classes up to 98% error (p.2)
- ImageNet >14M images → nearly 1M possibly mislabeled (p.2, fn.3)
- Moral Machine Experiment: 9 binary sparing dimensions (p.6)
- Empirically most people act only in Switch, not Footbridge (p.5)

## 10. Pitfalls & limitations
Author-admitted: overview of metaethics is narrow and Western-focused (p.8, fn.12); analysis is theoretical though with practical implications (p.2). Observable for benchmark-builders: the paper does not deny that measuring values/conventions is possible — only that labeling it "ethics" over-claims objectivity; it offers no concrete alternative metric, leaving the constructive "values" program underspecified. The is/ought critique applies to any survey-derived moral benchmark (a large share of the cultural/moral-psych benchmarks in this corpus).

## 11. Novel ideas worth stealing
- Reframe every "ethics" benchmark as a "values" benchmark and force two explicit disclosures: WHAT the values are and WHOSE values they are (p.1-2, p.4) — a discipline that instantly improves construct transparency.
- Treat "the benchmark becomes the target but the target is inapt" as a specific high-stakes failure mode for moral evals — Goodhart with reputational/trust externalities (p.7).
- Distinguish descriptive-proxy vs normative-target explicitly in any survey-derived benchmark, and never train-to or advertise-to the proxy as if it were the target (p.6-7).
- The "long-tail" argument as a principled reason to prefer capability/robustness-style or process-based evaluation over fixed-scenario moral scoring (p.9).
- Diversity of annotators/researchers as a validity requirement, since homogeneous groups encode only their own salient social conventions (p.8).
- Reserve strong claims ("is ethical") for constructs with defensible ground truth; downgrade to "accords with the stated preferences of population X" otherwise (p.8).

## 12. Notable quotes
- "we argue that it is, in fact, impossible to develop such a benchmark." (p.1)
- "Moral dilemmas have no right answer, by design." (p.7)
- "because values are unambiguously relative, focusing on values forces us to consider explicitly what the values are and whose values they are." (p.1)
- "if the benchmark becomes the target, but the target is inapt, then systems will be touted as more or less ethical despite that ethics is not being measured by the benchmark." (p.7)

## 13. UNKNOWN / not in extract
The full Section 4 constructive proposal on values and the concrete alternative mechanisms the authors advocate (extract truncates at p.9 of the argument); specific recommendations for practitioners; how they treat religious/global normative theories beyond the footnote caveats.
