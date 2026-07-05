---
stem: "2022-Abbasi-Deep Learning for Religious and Continent-Based"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [religious-values, cultural-linguistic, validity-psychometrics, best-practices]
task_format: "classifier"
scoring_type: "classifier"
dataset_size: 448000
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["NN", "CNN", "RNN", "LSTM", "BiLSTM", "GRU", "BiGRU"]
headline_numbers:
  - "CNN with GloVe achieved 95.24% accuracy on religious toxic comments dataset (p.7)"
  - "CNN with GloVe achieved 96.59% accuracy on race/ethnicity toxic comments dataset (p.9)"
  - "Original Jigsaw dataset: 1,804,874 rows; religious dataset after filtering: 42,906 rows; race/ethnicity: 70,179 rows (p.5)"
  - "RTC dataset: 80,145 nontoxic, 11,340 toxic comments across 7 religion labels (p.3)"
  - "RETC dataset: 51,555 nontoxic, 13,199 toxic comments across 5 race/ethnicity labels (p.3)"
---
## 1. Gist
This paper constructs two specialized multilabel classification datasets from the Jigsaw Unintended Bias in Toxicity Classification dataset (Wikipedia comments): one focused on religious identity groups (Christian, Jewish, Muslim, Hindu, Buddhist, Atheist, Other) and one on race/ethnicity groups (Asian, Black, White, Latino, Other). The authors compare 7 deep learning architectures (NN, CNN, RNN, LSTM, BiLSTM, GRU, BiGRU) with and without GloVe/Word2Vec/FastText embeddings. For values-alignment benchmarking, the paper demonstrates that religious and racial/ethnic identity groups attract systematically different rates of toxic content and that standard classifiers are affected by identity-based biases — a construct relevant to measuring whether AI systems perpetuate disparate harm to different value communities.

## 2. Benchmark/eval design features
Not a benchmark per se but an empirical comparison study. Core constructs:
- **Religious toxic comments (RTC)**: 7-label multilabel classification. Labels correspond to religious identity groups mentioned in the comment. A comment is toxic if >50% of human raters judged it so in the original Jigsaw dataset.
- **Race/ethnicity toxic comments (RETC)**: 5-label multilabel classification. Same toxicity threshold.
- Models compared: NN, CNN, RNN, LSTM, BiLSTM, GRU, BiGRU — with and without pretrained embeddings (GloVe, Word2Vec, FastText).
- Evaluation metrics: accuracy, precision, recall, F1-score (multilabel variants via Jaccard-based subset accuracy).

Key finding: CNN + GloVe achieves highest accuracy in both datasets. Models without embeddings vary considerably across architectures.

## 3. Task format & example item
Each Wikipedia comment is assigned multilabel toxicity flags for religious or racial/ethnic identity groups. The label indicates which identity groups are mentioned in a toxic context.

No verbatim example item included in the extract; the paper describes the task structure without example text.

## 4. Scoring / grading methodology
Multilabel classification metrics (p.6, equations 8-11):
- **Accuracy**: Jaccard similarity-based — measures proportion of correctly predicted label sets.
- **Precision**: Proportion of predicted labels that are correct.
- **Recall**: Proportion of true labels that are predicted.
- **F1-measure**: Harmonic mean of precision and recall.

These multilabel metrics differ from standard binary/multiclass metrics — subset accuracy is inherently harder to achieve than per-label accuracy.

## 5. Dataset construction & provenance
Source: Jigsaw Unintended Bias in Toxicity Classification dataset (Kaggle), originally ~1.8 million Wikipedia comments (p.3). Toxicity label: fraction of human raters (0–1); threshold ≥0.5 = toxic.

Processing (p.5): removed missing values → 448,000 rows. Selected rows with at least one religious or race/ethnicity label. Removed duplicates (281 in RTC, 271 in RETC). Final:
- RTC: 42,906 rows, 7 labels
- RETC: 70,179 rows, 5 labels

Both datasets derived from English Wikipedia talk pages. Balanced by removing zero-label rows. Dataset is publicly available at Kaggle (p.10).

## 6. Validity evidence
No formal construct validity analysis. The paper notes that prior work showed ML classifiers replicate societal biases against identity groups (e.g., Muslim, Jewish, Black, White) — nontoxic comments mentioning these groups are assigned unrealistically high toxicity scores (p.1). The study's contribution is documenting model performance variation across identity groups rather than formally validating the measurement instrument. No human baselines, no inter-rater analysis beyond the original Jigsaw dataset's rater fraction.

## 7. Saturation / discrimination
High accuracy scores (92–97%) suggest potential ceiling effects, but this may reflect dataset characteristics (heavy class imbalance: ~8% of original dataset is toxic, p.3) rather than genuine near-saturation. The multilabel accuracy metric penalizes partial hits, so absolute accuracy values are not directly comparable to binary task benchmarks.

## 8. Multiturn / agentic aspects
n/a — single-comment classification task.

## 9. Key numbers
- Original Jigsaw dataset: 1,804,874 rows, 46 columns (p.3)
- After filtering: 448,000 rows (p.5)
- RTC dataset: 42,906 rows, 7 labels (p.5)
- RETC dataset: 70,179 rows, 5 labels (p.5)
- Toxic proportion in original dataset: ~8% (144,334 / 1,804,874) (p.3)
- Best RTC accuracy: CNN+GloVe 95.24% (p.7)
- Best RETC accuracy: CNN+GloVe 96.59% (p.9)
- Best RTC F1: BiGRU+FastText 97.43% (p.7)
- Worst RTC accuracy: RNN+Word2Vec 63.08% (p.7)
- Muslim identity group: 21,007 nontoxic, 5,643 toxic (p.4)
- Black identity group: 14,097 nontoxic, 5,466 toxic (p.4)
- Training time per model: ~2 hours on Kaggle GPU (p.7)

## 10. Pitfalls & limitations
- Accuracy inflation due to zero-label rows removed — the "balanced" dataset may not reflect real-world distribution
- No comparison with transformer-based models (BERT, RoBERTa) — the study focuses only on CNN/RNN families
- Identity group labels are binary and do not capture intersectionality (e.g., a comment about a Black Muslim person)
- Original Jigsaw labels use crowd-worker fractions as toxicity ground truth, which embeds annotator demographic biases
- Single-language (English Wikipedia) — results may not generalize to multilingual or colloquial contexts
- No analysis of which specific label combinations cause mis-classification in multilabel setting

## 11. Novel ideas worth stealing
1. **Identity-group stratified dataset construction**: Splitting a large-scale toxicity dataset along religious vs. racial/ethnic identity lines to study differential model behavior is directly reusable. A values-alignment benchmark could adopt this design to measure whether evaluation systems penalize or privilege certain identity groups.
2. **Multilabel identity-group toxicity taxonomy**: The 7 religious labels + 5 race/ethnicity labels (with original dataset also including gender, sexual orientation, disability) form a comprehensive values-relevant taxonomy for measuring group-differentiated harm — worth adopting as a labeling schema.
3. **Documenting toxicity rate by identity group** (Table 1, p.4): Systematically reporting toxic/nontoxic rates per group (e.g., Muslim 5,643/21,007 vs. Hindu 196/1,361) makes distributional biases visible — a design pattern for transparency in values benchmarks.

## 12. Notable quotes
- "Nontoxic comments, including particular identification descriptors, such as Muslim, Jewish, White, and Black, were assigned unrealistically high toxicity ratings in several machine learning models." (p.1)
- "There is no existing work that performs multilabel classification on religion toxic comments or race or toxic ethnicity comments." (p.7)
- "Even though the data sets are unbalanced, the CNN model with Glove word embeddings for both datasets obtained promising results compared with other DL models and Word embedding approaches." (p.10)

## 13. UNKNOWN / not in extract
- Whether the constructed RTC and RETC datasets are separately published/released
- Per-label F1 breakdown (only aggregate metrics reported)
- Annotator demographics of the original Jigsaw raters
- How the "at least one label" filtering affects the multilabel class distribution
- Detailed hyperparameter search methodology
