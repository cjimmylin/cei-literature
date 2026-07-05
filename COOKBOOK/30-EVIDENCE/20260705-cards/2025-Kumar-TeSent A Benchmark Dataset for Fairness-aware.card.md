---
stem: "2025-Kumar-TeSent A Benchmark Dataset for Fairness-aware"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [validity-psychometrics, cultural-linguistic, best-practices]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 21119
dataset_construction: "crowdsourced"
languages: [Telugu]
models_tested: [mBERT, XLM-R, MuRIL, IndicBERT, Te-BERT]
headline_numbers: ["21,119 final annotated sentences retained (>95% of valid) (p.5)", "3-class inter-annotator Krippendorff alpha=0.4706, Fleiss kappa=0.4705; binary alpha=0.8928 (p.5-6)", "TeEEC gender bias set = 39,760 sentences evenly split by gender (p.6-7)", "Best classifier Te-BERT w/r F1=0.730, AUROC=0.884 (p.8)"]
---
## 1. Gist
TeSent is the first comprehensive Telugu sentiment-classification benchmark that couples ground-truth sentiment labels with human-annotated rationales, an explainability evaluation suite, and a fairness evaluation corpus (TeEEC). Although the core task is 3-class sentiment (positive/negative/neutral) rather than moral judgment, the paper is directly relevant to values-alignment benchmarking through two components: (a) a counterfactual fairness harness measuring gender and religion bias in classifier outputs, and (b) a rationale-supervision paradigm ("Explanation-Guided Learning") that trains models to attend to the same textual evidence humans deem relevant. Its central empirical finding — training with human rationales reliably improves alignment with human reasoning (plausibility) but does NOT reliably reduce social bias — is a transferable caution for anyone assuming that "human-aligned" supervision automatically yields "fairer" models.

## 2. Benchmark/eval design features
Three linked artifacts: (1) TeSent — 21,119 sentences labeled positive/negative/neutral with mandatory word/phrase rationales for polar sentences (optional for neutral) plus optional secondary label; (2) TeEEC — a template-based counterfactual Equity Evaluation Corpus (11 templates from Kiritchenko & Mohammad 2018) instantiated over gender {male, female} and religion {Hindu, Muslim, Christian}; (3) explainability suite over six post-hoc explainers (LIME, SHAP, Gradient, Integrated Gradients, and input-scaled variants) scored on faithfulness (comprehensiveness, sufficiency, LOO correlation) and plausibility (IOU, token-F1, AUPRC).

## 3. Task format & example item
Sentence-level 3-class sentiment classification with span-level human rationales. TeEEC fairness templates are counterfactual, e.g. "<person> feels <emotion word>" and "I saw <person> in the market" (p.6). No verbatim Telugu item text is legible in the extract beyond template schemas.

## 4. Scoring / grading methodology
Classifier metrics: Accuracy, F1, AUROC (p.8). Fairness: Polarity Difference Score (PDS) via counterfactual test, plus equalized-odds TPRdiff and FPRdiff (p.7). Explainability: erasure-based faithfulness (C↑, S↓, L↑) and plausibility (IOU↑, F1↑, AUPRC↑) via the ferret-xai library (p.7). Paired t-tests and Wilcoxon signed-rank at p<0.05 (p.8).

## 5. Dataset construction & provenance
Scraped from YouTube comments (53.7%), Telugu blogs (28.2%), and news headlines (18.1%) across ~20 domains, Sept–Oct 2024 (p.4, p.19 fig). Preprocessing removed code-mixing, duplicates, non-Telugu text. Annotated by 3 of 95 gender-balanced native-speaker undergraduates per sentence; final labels via majority vote after discarding <+,-> contradiction pairs; authors manually inspected and removed malformed items. Facebook/Instagram data excluded over Meta ToS ambiguity (p.4). All models/data released on HuggingFace (DSL-13-SRMAP) (p.3).

## 6. Validity evidence
Inter-annotator agreement reported with Krippendorff alpha=0.4706 and Fleiss kappa=0.4705 for 3-class; rises to alpha=0.8928 in binary setting (p.5-6). Authors contextualize the moderate 3-class alpha against HateXplain's 0.46 (Mathew et al. 2021). Cumulative pairwise agreement: ~80% of annotators agree with others on >82% of instances (p.5). No separate human ceiling on the classification task itself.

## 7. Saturation / discrimination
Best models reach ~0.73 F1 / ~0.88 AUROC (p.8) — substantial headroom remains; the 3-class task is far from ceiling. Rationale supervision produces small consistent gains for 4 of 5 architectures; XLM-R is flat or slightly worse (p.8). Fairness metrics show only small, inconsistent shifts, so the fairness axis does not cleanly discriminate models.

## 8. Multiturn / agentic aspects
n/a — static single-sentence classification with encoder models; no interaction, tools, or agents.

## 9. Key numbers
- 21,119 final sentences: 45.42% neutral, 26.84% positive, 27.74% negative (p.5)
- 22,225 valid annotated sentences before final filtering; >95% retained (p.5)
- 3-class alpha=0.4706 / kappa=0.4705; binary alpha=0.8928 (p.5-6)
- TeEEC: 11 templates, 4 emotion categories x 10 words each; 39,760 gender sentences (p.6-7)
- Te-BERT w/r: Acc 0.729, F1 0.730, AUROC 0.884 (best); IndicBERT wo/r Acc 0.713 (p.8)
- 95 annotators; 3 annotators/sentence (p.3)

## 10. Pitfalls & limitations
Author-admitted: bias framework excludes caste, age, occupation (deemed infeasible in counterfactual setup, p.6); no mechanistic/latent analysis; rationale supervision does not guarantee fairness gains (p.9). Observable flaws: moderate 3-class agreement (alpha~0.47) limits label reliability; religion names sampled from web resources (Behind the Name, QuranicNames) with incomplete verification (p.6-7); "privileged group" assignment (male, Hindu) hard-codes demographic majority assumptions; template-based TeEEC counterfactuals may miss naturalistic bias. Sentiment is only weakly a "values" construct.

## 11. Novel ideas worth stealing
- Rationale-as-supervision loss: CE loss + lambda*KL(model [CLS] attention || human-rationale distribution) to steer a model toward human-identified evidence (p.7-8) — directly portable to values benchmarks where you want models to reason from the "right" cues.
- Decoupling of plausibility (agreement with human evidence) from faithfulness (agreement with model internals) as separate, separately-tested axes (p.8) — a clean template for evaluating whether an "aligned" model is aligned for the right reasons.
- Counterfactual template EEC adapted with language-specific morphology (noun vs adjectival emotion-word forms) (p.6) — a reusable recipe for building minimally-paired bias probes in morphologically rich languages.
- Key transferable finding: human-alignment supervision improves human-reasoning agreement but NOT fairness — decouple these when claiming a benchmark measures "alignment."
- Two-layer annotation (primary + optional secondary sentiment) to capture ambiguity without inflating cognitive load (p.4-5).

## 12. Notable quotes
- "training with human rationales improves model accuracy and models' alignment with human reasoning, but does not necessarily reduce bias." (p.1)
- "models that become more aligned with human reasoning are not necessarily more fair." (p.9)
- "plausibility [is] a practical, interpretable proxy for human alignment in this setting." (p.8)

## 13. UNKNOWN / not in extract
Exact TeEEC religion-set size; per-explainer numeric plausibility/faithfulness tables (in Appendix H, not shown); licensing terms; verbatim Telugu example sentences; annotator compensation; train/dev/test split proportions for the classifier experiments.
