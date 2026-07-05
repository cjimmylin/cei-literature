---
stem: "2024-Hossein-ParsOffensive Persian Offensive Comments Dataset"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 21165
dataset_construction: "scraped"
languages: ["fa"]
models_tested: ["ALBERT-fa", "ParsBERT", "RoBERTa-fa", "XLM-RoBERTa"]
headline_numbers:
  - "XLM-RoBERTa achieves F1=0.899 (binary) and F1=0.769 (3-class) on test set (p.12)"
  - "Average kappa Phase I: 0.711; Phase II: 0.8934 (p.8)"
  - "After MLM pre-training, ALBERT-fa reaches F1=0.9087 (binary) and F1=0.7867 (3-class) (p.13)"
  - "Dataset contains 21,165 annotated comments: 15,436 POS, 654 NT-NEG, 5,075 T-NEG (p.9)"
---
## 1. Gist
This paper introduces OPSD (Offensive Persian Social Media Dataset), a manually annotated dataset of 21,165 Persian-language comments drawn from Instagram and Twitter, designed for offensive language detection. The dataset addresses a critical gap: while English offensive-language resources are plentiful, Persian-language equivalents are scarce. The authors implement a rigorous three-phase annotation process with five annotators and kappa-based quality control, yielding high inter-annotator agreement by Phase II. They then establish baselines using both classical ML and transformer-based models. For values-alignment benchmarking, OPSD is relevant as a model for building culturally-specific safety/harm datasets in non-English languages, demonstrating how annotation protocol design affects data quality.

## 2. Benchmark/eval design features
The benchmark measures offensive language detection across three classes: POS (non-offensive), T-NEG (targeted negative — directed at a person/organization), and NT-NEG (non-targeted negative — offensive content without a specific target). A binary version collapses T-NEG and NT-NEG into a single NEG+ class. Items are social media comments (tweets and Instagram posts) in Persian. The dataset is imbalanced: ~73% POS, ~24% T-NEG, ~3% NT-NEG, which creates challenges for minority-class detection. Baseline models range from logistic regression with TF-IDF features to fine-tuned multilingual transformers.

## 3. Task format & example item
Comments are classified into one of three labels. Example items from Table 3 (p.8):
- POS: "For about a year now, the internet quality of Irancell has deteriorated significantly, to the point that I no longer use it."
- NT-NEG: "I see the gathering of foolish rulers here, don't they have your national code to ask you to enter it?"
- T-NEG: "The shameless ones have deleted the unlimited package." / "Curse your head and your nonsense." (p.8)

## 4. Scoring / grading methodology
Models are evaluated using accuracy and macro F1-score on a held-out test set (10% of 21,165 = ~2,117 samples). The primary metric is F1, which accounts for class imbalance. Weighted cross-entropy loss is used during training. Error analysis includes confusion matrices and identification of mislabeled instances — removing confirmed mislabels improves XLM-RoBERTa accuracy from 0.907 to 0.936 (p.14).

## 5. Dataset construction & provenance
- Twitter (OPSD-Twitter): ~17,000 annotated records collected via keyword/hashtag search; over 40,000 initially crawled, filtered to 17,000 (p.4).
- Instagram (OPSD-Instagram): ~5,000 annotated records from IT service company pages (p.5).
- OPSD-Unlabeled: ~140,000+ tweets crawled for unsupervised/MLM pre-training, not manually labeled (p.5).
- Combined annotated dataset: 21,165 comments, 80/10/10 train/dev/test split (p.9).
- No explicit license mentioned in the extract; funded by MCI (Mobile Telecommunication Company of Iran).

## 6. Validity evidence
Inter-annotator agreement is measured via Cohen's kappa. Phase I averaged κ=0.711 across five annotator pairs; after guideline refinement in Phase II, average κ rose to κ=0.8934 (p.8). This demonstrates strong construct validity via the iterative annotation protocol. Five annotators participated; majority vote resolved remaining disagreements. No external validity checks (e.g., against gold-standard Persian offensive text benchmarks) are reported in the extract.

## 7. Saturation / discrimination
XLM-RoBERTa reaches F1=0.899 (binary) and F1=0.769 (3-class), suggesting significant headroom for the fine-grained 3-class task. The minority NT-NEG class (only 654 instances, ~3% of data) is the primary discrimination challenge — this class is heavily underrepresented. The binary task is near-saturated for transformer models but the 3-class task retains meaningful room for improvement.

## 8. Multiturn / agentic aspects
n/a — single-turn text classification dataset.

## 9. Key numbers
- 21,165 annotated comments total (p.9)
- 15,436 POS, 654 NT-NEG, 5,075 T-NEG (p.9)
- 140,000+ unlabeled tweets for MLM (p.5)
- Phase I average κ = 0.711; Phase II average κ = 0.8934 (p.8)
- XLM-RoBERTa: Acc=0.917, F1=0.899 (binary); Acc=0.907, F1=0.769 (3-class) (p.12)
- After MLM pre-training: ALBERT-fa F1=0.9087 (binary), F1=0.7867 (3-class) (p.13)
- RoBERTa-fa 3-class F1 improvement after MLM: +4.06% (p.13)
- Removing mislabeled test instances: accuracy increases from 0.907 to 0.936, F1 from 0.769 to 0.842 (p.14)
- 80/10/10 train/dev/test split (p.9)
- 5 annotators, 3-phase annotation (p.5)

## 10. Pitfalls & limitations
- Severe class imbalance: NT-NEG has only 654 instances (~3%), making reliable model training for that class difficult.
- Social media data from specific domains (telecom company comments, trending Twitter hashtags) may not generalize to other Persian-language contexts.
- No cross-validation reported — single 80/10/10 split may inflate or deflate estimates.
- Dataset skews toward short comments (p.9), limiting evaluation of longer offensive texts.
- No explicit data license or release mechanism described.
- The annotation process required two full phases — early guidelines were insufficiently clear (κ as low as 0.626 in Phase I, Part B).
- Future work mentions need for semi-supervised scaling, but current labeled set is modest.

## 11. Novel ideas worth stealing
- **Iterative annotation with kappa gating**: Only advance to the next annotation phase when inter-annotator agreement exceeds a threshold (75% kappa). This is a reusable quality-control gate for any values-alignment dataset requiring human labelers.
- **Three-phase consensus protocol**: Phase I = pairwise annotation; Phase II = guideline revision + re-annotation of disagreements; Phase III = third-annotator tiebreaking. This staged approach is more efficient than starting with three annotators and reduces wasted labeling effort.
- **MLM-based domain adaptation**: Using an unlabeled in-domain corpus for masked language model pre-training before fine-tuning substantially improves performance on minority classes — relevant when building domain-specific values benchmarks in low-resource languages.
- **Dual-schema evaluation**: Reporting both binary (collapsed) and fine-grained multi-class F1 allows comparison with existing work while also capturing more nuanced discrimination — useful for benchmarks that want both broad and granular scoring.
- **Error analysis with mislabel removal**: Quantifying how many "errors" are actually mislabeled data (not model failure) and reporting corrected upper-bound accuracy provides a realistic ceiling estimate for the task.

## 12. Notable quotes
- "The annotation process for this study consists of three phases, involving five different annotators. In the first phase, the data were divided into five parts, and each part was annotated by two annotators. The Cohen's kappa score was then calculated between the two annotators. If the Cohen's kappa score was below 75%, indicating poor agreement, the process moved to the second phase." (p.5)
- "The comparison of results between Table 6 and Table 7 indicates an interesting fact. Further training the language models on the MLM task improved the performance of the proposed models, particularly in terms of the F1-score. Notably, the Roberta model fine-tuned on OPSD (3-class) showed a 4.06% increase." (p.13)
- "Error analysis for the 3-class case shows that misclassification on the test data can be categorized in two groups." (p.13)

## 13. UNKNOWN / not in extract
- Dataset availability/download URL or license terms not stated.
- Year range of data collection not specified.
- Demographic breakdown of annotators not provided.
- Whether the dataset has been publicly released or is available on request is not stated.
- Inter-annotator agreement for binary (NEG+) classification not separately reported.
