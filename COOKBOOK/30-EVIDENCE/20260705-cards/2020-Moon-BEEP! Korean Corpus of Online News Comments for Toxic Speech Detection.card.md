---
stem: "2020-Moon-BEEP! Korean Corpus of Online News Comments for Toxic Speech Detection"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, best-practices]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 9341
dataset_construction: "crowdsourced"
languages: [Korean, ko]
models_tested: ["Term Matching", "CharCNN", "BiLSTM", "KoBERT"]
headline_numbers: ["9.4K manually labeled comments (train 7,896 / val 471 / test 974) (p.3)", "Krippendorff alpha: bias ternary 0.492, hate 0.496, gender-binary bias 0.767 (p.1,3)", "BERT best: bias-binary F1 0.681, bias-ternary 0.633, hate 0.525 (p.4)", "BERT+bias improves hate F1 from 0.525 to 0.569 (p.4)"]
---
## 1. Gist
BEEP! is presented as the first Korean corpus manually annotated for toxic speech, comprising ~9.4K online entertainment-news comments dual-labeled for (a) social bias (gender / other / none) and (b) hate speech (hate / offensive / none, following Davidson et al. 2017) (p.1). Its relevance to values-alignment benchmarking is threefold: it extends toxicity/values benchmarking to a non-English, non-WEIRD language with culturally specific bias categories (e.g., "absence of military service experience," mandatory for Korean males); it empirically demonstrates that bias and hate are intertwined constructs (prepending the bias label improves hate-speech detection); and it is released as a public Kaggle-leaderboard benchmark with a hidden test set. The corpus is motivated by real-world harm — celebrity deaths linked to toxic comments that led two Korean portals to close comment systems (p.1).

## 2. Benchmark/eval design features
Two parallel 3-way classification tasks per comment. Bias task: {Gender bias, Other biases, None}, plus a derived binary version counting only gender bias (p.2-3). Hate task: {Hate, Offensive, None} (p.2). Social bias defined as "a preconceived evaluation or prejudice towards a person/group with certain social characteristics: gender, political affiliation, religion, beauty, age, disability, race, or others" (p.2). Hate vs offensive boundary carefully specified: hate = explicit hatred/severe attack on protected attributes; offensive = sarcasm/irony, rude/uncivil opinion, or implicit attack still arguably within free speech (p.3). Article titles provided so participants can exploit context (p.3). Answer space is a single categorical choice per task.

## 3. Task format & example item
Annotators answer two three-choice questions per comment (p.2): "1. What kind of bias does the comment contain? Gender bias / Other biases / None. 2. Which is the adequate category for the comment in terms of hate speech? Hate / Offensive / None." Guideline examples of gender bias (p.4-5, Appendix A): "Wife must be obedient to her husband's words" and "Homosexual person will be prone to disease." Model-error example (p.4): CharCNN fails to flag bias in "What a long life for a GAY" but wrongly flags "I think she is the prettiest among all the celebs" (misled by the female pronoun).

## 4. Scoring / grading methodology
Supervised classifiers evaluated by F1 on a held-out test set (labels hidden on Kaggle for fair competition, p.3). Macro-F1 reported per class for the ternary bias task (Table 3, p.4). Term-matching baseline (profanity termbases) is compared but collapses hate+offensive into one binary category (p.4). Ground-truth label = majority decision of 3 random annotators; ambiguous comments skippable (p.2).

## 5. Dataset construction & provenance
Scraped 10,403,368 comments from 23,700 entertainment-news articles (Jan 2018-Feb 2020) on a major Korean portal (p.2). Sampling: 1,580 articles via stratified sampling; top-20 comments per article ranked by Wilson-score on downvotes (targeting contentious content); removed duplicates, single-token comments, and comments >100 chars; 10K randomly selected for annotation (p.2). An additional unlabeled ~2M-comment corpus released for LM pretraining (p.2). Annotation by 32 annotators (29 DeepNatural AI crowdworkers + 3 NLP researchers), 3 per comment, majority vote (p.2). 659 skipped/no-agreement instances discarded, leaving 9,341; split train 7,896 / val 471 / test 974 (p.3). Public GitHub + Kaggle release (p.1). First Korean guideline for social bias and hate on online comments (p.2).

## 6. Validity evidence
Krippendorff's alpha reported: ternary bias 0.492 (moderate), hate 0.496 (moderate), gender-binary bias 0.767 (substantial) (p.1, p.3). The much higher binary-gender agreement evidences that the finer ternary distinctions and the inherently subjective hate/offensive line are noisier constructs. Class distribution (Table 1, p.3) empirically shows bias-hate correlation: biased comments are far more likely to be hateful/offensive. Convergent evidence: prepending gold bias as a special token raises BERT hate-F1 (0.525->0.569), supporting the claimed construct linkage (p.4).

## 7. Saturation / discrimination
Far from saturated: best model (BERT) reaches only hate F1 0.525, bias-ternary 0.633 (p.4). Clear model discrimination: BERT > CharCNN > BiLSTM > Term Matching (0.195 hate) (p.4). Hate detection is systematically harder than bias detection for all models ("hate speech detection is a more subjective issue," p.1). The "Others" bias class is nearly unlearnable (BiLSTM F1 0.000, BERT 0.326) due to its catch-all breadth (Table 3, p.4), indicating a difficulty/heterogeneity problem rather than pure ceiling.

## 8. Multiturn / agentic aspects
n/a — single-comment classification, no interaction.

## 9. Key numbers
- Source pool: 10,403,368 comments from 23,700 articles (p.2).
- Final annotated corpus 9,341 (10K minus 659 discarded); train 7,896 / val 471 / test 974 (p.3).
- 32 annotators (29 crowd + 3 researchers), 3 per comment (p.2).
- IAA: bias ternary 0.492, hate 0.496, gender-binary 0.767 (p.1, p.3).
- Class distribution (%): Hate 25.11, Offensive 32.66, None 41.80; Gender-bias 15.71, Other-bias 18.16, No-bias 65.70 (Table 1, p.3).
- F1 (Table 2, p.4): Term Matching hate 0.195; CharCNN 0.547/0.535/0.415; BiLSTM 0.302/0.291/0.340; BERT 0.681/0.633/0.525; BERT+bias hate 0.569.
- Bias-ternary macro-F1 by class (Table 3, p.4): BERT Gender 0.693, Others 0.326, None 0.880.

## 10. Pitfalls & limitations
Author-admitted: hate is context-sensitive and annotators lack additional context, diversifying labels (p.2); no socially agreed Korean hate-speech definition exists, so authors improvised from YouTube/Facebook/Twitter policies (p.3); "Others" bias class too broad to model well (p.4). Observable: moderate IAA (~0.49) means the gold labels are noisy for the core tasks; downvote-Wilson-score sampling deliberately over-selects contentious comments, skewing prevalence away from natural distribution; entertainment-news domain and celebrity-gender focus limit generalization; only Korean single-language; small validation (471) and test (974) sets; no LLMs beyond KoBERT.

## 11. Novel ideas worth stealing
- Dual-facet co-annotation (bias AND hate on the same item) then empirically testing whether one construct improves prediction of the other by prepending the gold label as an input token — a clean way to demonstrate and exploit construct interdependence in values benchmarks.
- Culturally-specific bias categories tied to the target society (e.g., "absence of military service experience" in Korea) rather than importing a US/WEIRD taxonomy — essential for cross-cultural values evals.
- Reporting a coarse-binary agreement (gender 0.767) alongside fine-ternary agreement (0.492) to reveal exactly which distinctions are reliable vs subjective — a diagnostic to guide which labels a benchmark should trust.
- Wilson-score-on-downvotes sampling to efficiently surface contentious/toxic content from a huge pool (raises positive-class density without pure keyword filtering).
- Releasing a large unlabeled in-domain corpus (~2M) alongside the labeled set for domain-adaptive pretraining — supports building stronger baselines.
- Providing source-article titles as optional context — acknowledges that toxicity judgments are context-dependent and lets systems (and future LLM judges) use it.
- Hidden-test Kaggle leaderboard for contamination-resistant, community-driven benchmarking.

## 12. Notable quotes
- "The models generally display better performance on bias identification, since the hate speech detection is a more subjective issue." (p.1)
- "when BERT is trained with bias label for hate speech detection, the prediction score increases, implying that bias and hate are intertwined." (p.1)
- "not all the rude or aggressive comments necessarily belong to the above definition, as argued in Davidson et al. (2017)." (p.3)
- "As socially agreed definition lacks for Korean, we refer to the hate speech policies of Youtube; Facebook; Twitter." (p.3)

## 13. UNKNOWN / not in extract
- Licensing terms of the corpus release.
- Annotator demographics / native-speaker status beyond count.
- Compensation for crowd annotators.
- Full confusion-matrix numbers (Figure 2 described, not tabulated).
- Whether the 2M unlabeled corpus was actually used to pretrain the reported baselines.
