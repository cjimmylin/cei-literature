---
stem: "2020-Mollas-ETHOS an Online Hate Speech Detection Dataset"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [design-space, validity-psychometrics, saturation-discrimination, cultural-linguistic]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 998
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: ["MultinomialNB", "BernoulliNB", "Logistic Regression", "SVM", "Random Forest", "Gradient Boosting", "CNN+Attention", "LSTM", "BiLSTM", "BERT", "DistilBERT", "MLkNN", "MLARAM", "Binary Relevance", "Classifier Chains", "NNBR", "NNCC"]
headline_numbers:
  - "ETHOS Binary: 998 comments; ETHOS Multi-Label: 433 hate speech comments with 8 labels (p.7)"
  - "DistilBERT achieves 79.92% F1 and 80.36% accuracy on binary classification (p.9)"
  - "Fleiss' kappa for 'Contains Hate Speech': 0.814; highest for 'Disability': 0.977 (p.7)"
  - "NNBR achieves highest multi-label performance on 12 of 13 metrics (p.9)"
  - "CrowS-Pairs validation rate 80% vs StereoSet 62% in comparative validation (p.8)"
---

## 1. Gist

ETHOS (onlinE haTe speecH detectiOn dataSet) is a small but carefully constructed hate speech detection dataset of YouTube and Reddit comments with two variants: a binary classification set (998 comments, hate/not-hate) and a multi-label set (433 hate speech comments annotated for violence, directedness, and six demographic target categories). The key innovation is the annotation protocol: active learning-based sampling ensures both class balance and informational diversity, avoiding the redundancy and class imbalance problems that plague larger scraped HS datasets. Crowdsourcing validation via the Figure-Eight platform achieves high inter-annotator agreement (Fleiss' κ ≥ 0.814 across all labels). For values-alignment benchmarking, ETHOS demonstrates that careful small-dataset construction can match the predictive utility of datasets 24x larger, and its multi-label schema for hate speech dimensions (violence, directedness, target group) is a reusable design pattern for fine-grained harm classification.

## 2. Benchmark/eval design features

Binary variant: 998 comments labeled isHate ∈ [0,1] (binarized at ≥0.5). Near-equal class balance achieved by design. Multi-label variant: 433 hate speech comments with 8 labels: violence, directed_vs_generalized, gender, race, national_origin, disability, sexual_orientation, religion. All label values are continuous [0,1] (proportion of annotators agreeing), binarized for model training. The paper evaluates 17+ ML/DL models from Naive Bayes through fine-tuned BERT/DistilBERT; also includes cross-dataset generalization experiments to D1 (Davidson et al., 24,783 tweets) and D2 (multilingual trilingual dataset).

## 3. Task format & example item

Free-text social media comments from YouTube (via Hatebusters platform) and Reddit (subreddits: Incels, TheRedPill, The_Donald, RoastMe). No verbatim example items quoted in the extract. The annotation HIT on Figure-Eight asked: (1) Does this comment contain HS? (2) If yes: does it incite violence? (3) Is it directed or generalized? (4) Which category (gender/race/national origin/disability/sexual orientation/religion)? (p.6)

## 4. Scoring / grading methodology

Labels are soft scores: proportion of crowd annotators selecting each label. Binarized at threshold 0.5 for model training. Evaluation metrics for binary: accuracy, macro F1, precision, recall, specificity, sensitivity. For multi-label: Hamming loss, subset accuracy, instance- and label-based precision/recall/F1 (macro and micro), and average precision. Nested cross-validation used for traditional ML; 10-fold CV for neural models.

## 5. Dataset construction & provenance

Three-stage protocol: (1) Active sampling from Hatebusters YouTube API + Reddit public archive (Oct 2017 and earlier, from banned subreddits), using ML predictions + uncertainty sampling to select informative comments while maintaining category balance. Threshold T=1,000. (2) Figure-Eight crowdsourcing validation: 5 annotators per comment, level-3 (most experienced) annotators. 5,360 judgements total, 40 test/calibration questions per annotator. (3) Manual final quality check. Dataset available on GitHub: https://github.com/intelligence-csd-auth-gr/Ethos-Hate-Speech-Dataset (p.7). Reddit data pre-ban (2017), YouTube data from Hatebusters volunteers.

## 6. Validity evidence

Fleiss' kappa across 9 labels: Contains HS 0.814, Violence 0.865, Directed vs. Generalized 0.854, Gender 0.904, Race 0.931, National Origin 0.917, Disability 0.977, Sexual Orientation 0.954, Religion 0.963 (p.7). All exceed the "good agreement" threshold of 0.75. Class balance is explicitly verified (Figure 4, p.8). Cross-dataset generalization tested against D1 and D2 to assess transferability. Balanced vs. random subset experiment confirms that active-learning-balanced data produces better HS recall despite smaller size.

## 7. Saturation / discrimination

Binary classification: best DistilBERT F1 = 79.92%, BERT F1 = 79.60% (p.9). Traditional ML tops out around 66.5% F1 (Logistic Regression). BiLSTM+FT+GV achieves 77.84% F1, highest recall on hate category among non-BERT models. Multi-label: NNBR achieves subset accuracy 48.39%, Hamming loss 0.0993 (p.9). Cross-dataset transfer is notably weak: SVM trained on ETHOS achieves only 33.21% F1 on HS in D1; F1 on D1's majority class (non-HS) = 74.03%. This suggests limited generalization headroom and domain-specific vocabulary effects.

## 8. Multiturn / agentic aspects

n/a — single-sentence or short-text classification task.

## 9. Key numbers

- Binary dataset: 998 comments, near 50/50 hate/non-hate balance (p.7)
- Multi-label dataset: 433 hate speech comments, 8 labels (p.7)
- Fleiss' κ range: 0.814 (HS binary) to 0.977 (disability) (p.7)
- 5 annotators per comment, 5,360 total judgements (p.7)
- DistilBERT best binary F1: 79.92%, accuracy: 80.36% (p.9)
- NNBR best multi-label subset accuracy: 48.39%, Hamming loss: 0.0993 (p.9)
- Cross-dataset: SVM on ETHOS → D1 balanced accuracy 58.03%; SVM on D1 → ETHOS balanced accuracy 50.90% (p.10)
- D1 is 24x larger than ETHOS (p.11)
- 2 months of daily active querying for data collection (p.12)
- Reddit subreddits used: Incels, TheRedPill, The_Donald, RoastMe (p.5)

## 10. Pitfalls & limitations

- Small size (998 binary, 433 multi-label) limits generalization to other platforms and topics (p.12)
- US/English social media comments only; no multilingual coverage despite the problem being global
- Cross-dataset transfer is poor: models trained on ETHOS struggle on D1 and vice versa, suggesting domain-specific vocabulary dominates (p.10–11)
- Multi-label subset accuracy only 48.39% with best model — multi-label HS detection remains very hard
- Race/language mismatch: model trained on ETHOS failed to detect "ching chong" racial slurs absent from training data (p.11)
- Budget and platform constraints limit crowdsourcing scale (p.12)
- Subreddits used were explicitly banned communities; training on this data may overfit to extreme examples

## 11. Novel ideas worth stealing

- **Active learning-based balanced sampling**: explicitly targeting uncertainty-range examples ([0.4, 0.6] confidence) while occasionally checking extreme ranges for systematic misclassification creates class-balanced datasets with less redundancy — directly applicable to any benchmark needing balanced label distributions from naturally imbalanced corpora.
- **Multi-dimensional harm schema**: decomposing hate speech into orthogonal axes (violence/non-violence × directed/generalized × 6 demographic categories) creates a richer label space than binary HS — reusable for values-alignment benchmark items about harm, targeting, and severity.
- **Soft labels from proportion voting**: reporting crowd-vote proportions rather than majority-voted hard labels preserves annotator disagreement information and enables threshold sensitivity analysis — particularly valuable for tasks where the boundary between harmful and non-harmful is genuinely contested.
- **Cross-dataset generalization as validity test**: training on ETHOS and evaluating on D1 (and vice versa) provides a natural external validity check that purely internal cross-validation misses — worth including in any benchmark paper.
- **Balanced vs. random subset ablation**: the paper explicitly tests balanced sampling against random sampling at the same size, providing a clean ablation demonstrating the value of the annotation protocol — a design move worth replicating.

## 12. Notable quotes

- "Our key assumption is that, even gaining a small amount of labelled data from such a time-consuming process, we can guarantee hate speech occurrences in the examined material." (p.1)
- "A kappa value greater than 0.75 implies good agreement, while kappa values greater than 0.90 indicate perfect agreement." (p.7)
- "It is peculiar that the two models do not predict the other's hate speech instances." (p.10)
- "Despite the relatively small size of the ETHOS dataset, the human resources invested in adequate labelling cannot be overlooked (2 consecutive months of daily querying of the targeted databases, human annotation in 2 stages, input by a crowdsourcing process)." (p.12)

## 13. UNKNOWN / not in extract

- Exact license for public dataset release
- Demographic breakdown of the 362 MTurk workers
- Precise number of comments queried/rejected before final 998 were retained
- Whether the Figure-Eight platform annotations are publicly released alongside the labels
- Performance with more recent models (GPT-series, etc.)
