---
stem: "2019-Borkan-Nuanced Metrics for Measuring Unintended Bias"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [validity-psychometrics, saturation-discrimination, contamination-robustness, design-space]
task_format: "n/a"
scoring_type: "mixed"
dataset_size: 1804875
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: ["TOXICITY@1", "TOXICITY@6 (Perspective API)"]
headline_numbers:
  - "Human-labeled dataset of 1.8 million comments, with 450,000 annotated for identity (p.1)"
  - "Synthetic test set of 77k examples from 50 identity terms (p.5)"
  - "TOXICITY@1 BPSN AUC for homosexual: near 0.76 on synthetic set, reflecting strong false-positive bias (p.5)"
  - "Transgender identity has 21.29% toxic comments in dataset vs. 8.0% overall (p.6)"
  - "Homosexual subgroup has 28.38% toxic comments vs. 8.0% overall (p.6)"
---
## 1. Gist
Borkan et al. (2019, Jigsaw/Google) introduce a suite of five threshold-agnostic metrics for measuring unintended bias in text classifiers, plus a large new human-labeled dataset of 1.8 million comments annotated for toxicity and identity. The metrics — Subgroup AUC, BPSN AUC, BNSP AUC, Positive AEG, and Negative AEG — decompose how a classifier's score distribution varies across demographic subgroups relative to a "background" distribution. The work matters for values-alignment benchmarking because it provides a rigorous measurement framework for detecting whether a model systematically mis-scores content involving marginalized identity groups, and it exposes the limits of single-number bias metrics and threshold-dependent evaluations.

## 2. Benchmark/eval design features
The paper proposes an evaluation methodology rather than a benchmark task. The core design:
- **Five metrics** derived from ROC-AUC and Mann-Whitney U:
  1. **Subgroup AUC**: AUC computed only on examples within one identity subgroup (positive + negative). Detects poor in-group separability.
  2. **BPSN AUC** (Background Positive, Subgroup Negative): AUC of background positives vs. subgroup negatives. Low score = false positive inflation for that subgroup.
  3. **BNSP AUC** (Background Negative, Subgroup Positive): AUC of background negatives vs. subgroup positives. Low score = false negative inflation (under-flagging toxic content mentioning the group).
  4. **Positive AEG** (Average Equality Gap): Measures systematic upward/downward score shift for positive (toxic) examples in the subgroup vs. background.
  5. **Negative AEG**: Same for non-toxic examples; captures subtle score inflation for non-toxic identity-mentioning text.
- All metrics are threshold-agnostic and robust to class imbalance between subgroups.
- Applied to two Perspective API toxicity classifiers (TOXICITY@1 and TOXICITY@6) on synthetic and real-world data.

## 3. Task format & example item
Not a benchmark with items. The paper evaluates existing toxicity classifiers against identity-annotated comment data. Example from Table 4 (identity annotation categories shown to crowd raters):
> "What genders are referenced in the comment?" — raters selected from Male, Female, Transgender, Other gender. (p.5)
The classification task itself is: rate a comment for toxicity on a 4-point scale (Very Toxic, Toxic, Hard to Say, Not Toxic). (p.6)

## 4. Scoring / grading methodology
- Crowd raters annotate toxicity and identity references; majority/aggregated scores create continuous toxicity labels.
- The five proposed metrics are computed as AUC variants and Mann-Whitney U statistics (all closed-form, no threshold setting required).
- Optimal value: Subgroup/BPSN/BNSP AUC = 1.0; AEGs = 0.0.
- AEG range is −0.5 to 0.5; positive AEG indicates upward score shift (toward toxicity) for the subgroup.

## 5. Dataset construction & provenance
- **Synthetic set**: 77,000 comments generated from templates using 50 identity terms; 50% toxic / 50% non-toxic by construction; from prior Jigsaw work. (p.5)
- **Real dataset**: 1,804,875 comments sourced from online comment forums; all labeled for toxicity; 450,000 also labeled for identity by crowd raters. Some identity-containing comments were oversampled using earlier identity models to ensure raters see identity content frequently. (p.6)
- Identity categories: Gender (4), Sexual Orientation (4), Religion (7), Race/Ethnicity (4), Disability (4). (p.5)
- Released under Creative Commons license. (p.6)
- No explicit train/dev/test split described for the evaluation dataset; used for evaluation only.

## 6. Validity evidence
- Synthetic test set provides ground truth by construction (labels are definitionally reliable). (p.2)
- Real dataset uses high rating redundancy (multiple crowd raters per comment) to mitigate label noise. (p.2)
- Comparison between synthetic and real data results validates synthetic findings while revealing additional nuance: "Real data reveals more unintended bias than synthetic data." (p.7)
- No formal inter-rater reliability statistics reported in the extract for the main dataset.

## 7. Saturation / discrimination
- Identity groups vary substantially: transgender = 21.29% toxic, homosexual = 28.38% toxic, vs. 8.0% overall. (p.6)
- TOXICITY@6 reduces but does not eliminate BPSN AUC deficits for gay/lesbian identities. (p.6)
- Improvements concentrated in short comments; bias mitigation did not generalize to longer comments. (p.8)
- Negative AEG for bisexual/trans/queer/black shows persistent score inflation even where AUC looks acceptable — illustrating that AEG catches subtle bias that BPSN AUC misses. (p.7)
- Wide score range without overlap (type F/G bias scenarios) remains partially undetectable by these metrics. (p.5)

## 8. Multiturn / agentic aspects
n/a — single-turn text classification evaluation.

## 9. Key numbers
- 1,804,875 total comments in human-labeled dataset (p.6)
- 450,000 subset labeled for identity (p.6)
- 77,000 synthetic examples across 50 identity terms (p.5)
- TOXICITY@1 BPSN AUC for homosexual ≈ 0.76 on synthetic set (p.5)
- Transgender: 21.29% toxic; homosexual: 28.38% toxic; overall: 8.00% toxic (p.6)
- Bias mitigation (TOXICITY@6) improves short-comment AUC metrics but shows "much less change" for all-comment results (p.8)
- AEG range: −0.5 to 0.5; optimal = 0 (p.5)

## 10. Pitfalls & limitations
- Binary gender model used to extract identity from bios is acknowledged as a simplification that erases non-binary people. (p.2 in related Bias in Bios paper; consistent theme in this field)
- The assumption of "reliable labels" is significant and does not always hold in real data; acknowledged by authors. (p.1)
- Single identity terms may not capture nuanced identity references ("same-sex marriage"). (p.5)
- Type F bias (wide score range without overlap) is not detected by any of the proposed metrics. (p.5)
- Authors note AEG detecting subtle score shifts may not always indicate harmful bias — depends on use case. (p.5)
- The five metrics can conflict with each other, requiring practitioners to interpret a suite rather than a single number.
- Dataset is English-only from online comment forums, which may not generalize.

## 11. Novel ideas worth stealing
1. **Threshold-agnostic metric suite**: Replace single-threshold accuracy/F1 with AUC-based decompositions that separately capture false positive inflation (BPSN) and false negative inflation (BNSP) per demographic group. Directly applicable to any values-alignment eval where a model assigns scores across identity-relevant prompts.
2. **Subgroup vs. background framing**: Rather than measuring each subgroup in isolation, compare the subgroup distribution against the rest of the data. This makes metrics robust to class imbalance — a pervasive problem in any dataset with minority identity categories.
3. **AEG for subtle score shift detection**: The Average Equality Gap catches biases too small to cause mis-orderings but still reflecting systematic score inflation/deflation. For benchmark design, this means including "soft" items where identity mentions are neutral so that score drift on non-sensitive items becomes detectable.
4. **Paired synthetic + real evaluation**: Use a small synthetic set (controlled, unambiguous) to validate that your metrics work, then run on real data to reveal additional distributional complexity. A two-tier validation approach for any new benchmark.
5. **Identity annotation as a separate crowdsourcing task**: Annotating which identities appear in text (rather than inferring from keywords) captures nuanced identity references and is a reusable design pattern for downstream bias evaluation.

## 12. Notable quotes
- "Threshold agnostic metrics capture the behavior of the underlying model itself, and thus can allow a more comprehensive comparison of the model's performance and limitations." (p.1)
- "Real data reveals more unintended bias than synthetic data." (p.7)
- "The metrics and distributions show that the bias mitigation brought unintended bias in short comments, where it was strongest, in line with unintended bias overall, where it was less visible." (p.8)
- "Of course, these scenarios are not an exhaustive list of all possible types of bias, but they help to illuminate some of the differences between these metrics." (p.5)

## 13. UNKNOWN / not in extract
- Exact inter-rater reliability statistics for the 1.8M real dataset annotation (multiple crowd raters per comment, but κ or similar not stated in this extract).
- Full Tables 3 and 6 with numerical AUC values per identity subgroup (tables are referenced but not fully rendered in the OCR extract).
- Specific model architectures for TOXICITY@1 and TOXICITY@6.
- Licensing details beyond "Creative Commons."
- Whether the 450K identity-annotated subset was drawn randomly or via active sampling.
