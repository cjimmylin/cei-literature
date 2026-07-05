---
stem: "2020-Hoover-Moral Foundations Twitter Corpus"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, validity-psychometrics, normative-ethics, cultural-linguistic]
task_format: "forced-choice"
scoring_type: "human-rating"
dataset_size: 35108
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: []
headline_numbers:
  - "35,108 tweets annotated by ≥3 trained annotators across 7 discourse domains (p.2)"
  - "Overall Fleiss' Kappa across all foundations: 0.27; PABAK: 0.29 (p.14)"
  - "Best model F1 for moral sentiment classification: LSTM F1=0.66 for MFD2 (p.20)"
  - "Annotator liberal skew: 5 of 13 annotators identified as liberal, 0 as very conservative (p.9)"
---
## 1. Gist
The Moral Foundations Twitter Corpus (MFTC; Hoover et al. 2020) is a large annotated dataset of 35,108 tweets labeled for moral sentiment according to Moral Foundations Theory (MFT). The corpus spans seven politically and socially diverse discourse domains (All Lives Matter, Black Lives Matter, Baltimore Protests, 2016 US Election, Hurricane Sandy, #MeToo, and Davidson Hate Speech). Each tweet is annotated by at least three trained human annotators for ten categories of moral sentiment (the five MFT virtue/vice pairs: Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Purity/Degradation) plus a non-moral label. The paper reports baseline classification results across four computational approaches. This corpus is essential for building or evaluating AI systems that must detect or respond to morally-valenced language at scale.

## 2. Benchmark/eval design features
The MFTC serves simultaneously as an annotation resource and a classification benchmark. The annotation task is multi-label: each tweet can receive zero or more of the 10 moral labels plus a non-moral flag. Annotators assigned labels based on the Moral Foundations Coding Guide. Classification baselines were computed for five foundation-level binary prediction tasks (collapsed across virtue/vice) and a coarser moral/non-moral detection task. Baseline models tested: SVM with MFD word counts, SVM with MFD2 word counts, SVM with DDR features, and multi-task LSTM. Performance varies substantially by domain and foundation, with the LSTM generally achieving highest F1 and DDR achieving highest recall.

## 3. Task format & example item
The annotation task is binary per label: for each of 11 labels, the annotator indicates presence/absence. The computational task is binary classification for each foundation.

Example item type (from dataset description, p.7): A tweet such as one from the Baltimore Protests corpus is shown to annotators who must decide whether it expresses, e.g., Harm (physical or emotional harm concerns) or Care (concern for protecting others). No verbatim example tweet is provided in the extract due to the sensitive nature of the content.

## 4. Scoring / grading methodology
Human annotation: majority vote with threshold ≥50% of annotators. Ties (when even number of annotators split evenly) are flagged; the percentage of ties is reported per domain and ranges from 52.2% to 100% depending on domain (p.13-14). Inter-annotator agreement measured with Fleiss' Kappa and PABAK (Prevalence- and Bias-Adjusted Kappa). PABAK is preferred given the very low base rates of positive labels. Classification baselines evaluated using 10-fold cross-validation, reporting precision, recall, and F1.

## 5. Dataset construction & provenance
Seven sub-corpora collected by different methods (Twitter API scraping, Gnip, Spinn3r, from Davidson et al. 2017). Sampling combined random sampling and semi-supervised selection using DDR to maximize moral sentiment base rates. Total annotators: 13 undergraduate RAs. Each tweet annotated by ≥3 annotators; some subsets had up to 8 annotators. Annotator meta-data collected post-annotation: political ideology, Moral Foundations Questionnaire scores, education, analytic thinking. Annotators skew liberal (5 liberal, 3 slightly liberal, 1 moderate, 1 slightly conservative, 1 conservative, 0 very conservative out of 13). Corpus available with annotation tool at GitHub.

## 6. Validity evidence
- Fleiss' Kappa overall: 0.27; PABAK overall: 0.29 (p.14)
- Per-foundation PABAK ranges: Subversion 0.67, Authority 0.71, Cheating 0.75, Fairness 0.85, Harm 0.65, Care 0.63, Betrayal 0.82, Loyalty 0.62, Purity 0.91, Degradation 0.89, Non-moral 0.62 (p.14-15)
- Low raw kappas are expected given the sparsity of positive labels; PABAK values in the 0.62–0.91 range suggest adequate agreement once prevalence is controlled
- Substantial variation by domain: BLM and Baltimore corpora have higher agreement on some foundations, Davidson corpus is the most challenging (many near-zero kappas)

## 7. Saturation / discrimination
The corpus discriminates substantially across domains: e.g., only ~2% of ALM data labeled as Degradation vs. ~14% of Sandy data (p.12). The LSTM model's F1 for moral detection using all foundations collapsed ranges from 0.51 to 0.67 across domains (from tables p.20+). The sparsity of positive labels for some foundations in some domains makes this a challenging benchmark rather than a saturated one. Models trained within-domain fail to generalize well across domains, indicating real difficulty and room for improvement.

## 8. Multiturn / agentic aspects
n/a — single-document classification task.

## 9. Key numbers
- 35,108 total annotated tweets (p.2)
- 7 discourse domains, 13 annotators (p.7)
- 10 moral categories (5 virtue/vice pairs) + non-moral (p.7)
- Each tweet annotated by ≥3 annotators; some up to 8 (p.7)
- Overall Fleiss' Kappa: 0.27; PABAK: 0.29 (p.14)
- SVM-MFD F1 (All, moral detection): 0.61 (p.20)
- SVM-MFD2 F1 (All, moral detection): 0.66 (p.20)
- LSTM best F1 generally outperforms other models on F1 and Precision (p.19)
- DDR generally achieves higher recall than LSTM and dictionary-based approaches (p.19)
- Annotators: 2 very liberal, 5 liberal, 3 slightly liberal, 1 moderate, 1 slightly conservative, 1 conservative (p.9)

## 10. Pitfalls & limitations
- Strong annotator liberal political skew (0 very conservative out of 13) may bias labels for politically sensitive foundations (Authority, Loyalty, Purity/Degradation)
- Semi-supervised sampling procedure using DDR to boost moral content base rates means the corpus does not reflect naturalistic base rates; this complicates generalizing classification models to unfiltered corpora
- Moral sentiment labeling is inherently subjective; the paper explicitly acknowledges this and deliberately avoids over-emphasizing annotator agreement, but this creates challenges for using the corpus as a gold standard
- Cross-domain generalization is poor; models trained on one discourse domain fail on others
- No inter-rater reliability reported at the individual annotator level; only aggregate Fleiss' Kappa
- Dataset was collected at a specific historical moment (2014–2018); moral framing evolves

## 11. Novel ideas worth stealing
- **Virtue/vice distinction within each foundation**: Rather than collapsing, separately annotating the prescriptive (virtue) and prohibitive (vice) poles of each foundation captures semantically independent signals that often do not co-occur. Values benchmarks should similarly distinguish between endorsement of a positive norm and condemnation of its violation
- **Discourse-domain stratification**: Building a benchmark across multiple politically distinct domains (left-coded, right-coded, neutral) tests whether moral detection is domain-general or domain-specific — a critical validity check for any moral AI benchmark
- **Annotator meta-data collection**: Collecting annotators' own moral foundations scores and political ideology post-hoc enables studying how annotator background shapes moral labels — directly relevant to understanding whose moral intuitions a benchmark reflects
- **PABAK alongside raw kappa**: When positive labels are sparse (as they will be for many moral/values categories), reporting raw kappa alone is misleading. The PABAK correction should be standard practice for sparse moral annotation tasks
- **Multi-task architecture**: Training a model to predict all 10 foundations simultaneously (multi-task LSTM) outperforms single-task models — suggests that moral foundations are interdependent in ways that should be reflected in benchmark evaluation protocols

## 12. Notable quotes
- "Research has shown that accounting for moral sentiment in natural language can yield insight into a variety of on- and off-line phenomena, such as message diffusion, protest dynamics, and social distancing." (p.2)
- "While uniform annotator training is important, we believe that excessive focus on maximizing annotator agreement risks artificially inflating agreement at the cost of suppressing the natural variability of moral sentiment." (p.9)
- "Ground-truth is, by definition, subjective." (p.3)
- "Considerable performance variation was observed across both discourse domain and Foundation." (p.19)

## 13. UNKNOWN / not in extract
- Exact F1 scores for individual foundation-level classification (individual foundation tables referenced but numbers not fully legible in extract)
- License terms for the MFTC
- Whether the corpus has been extended or updated since 2020
- Whether annotators were re-tested for reliability drift over the course of the annotation project
- How the annotation tool weighted or resolved genuine annotator disagreement beyond majority vote
