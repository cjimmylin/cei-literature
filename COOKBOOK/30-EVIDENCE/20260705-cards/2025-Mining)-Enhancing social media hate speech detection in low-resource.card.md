---
stem: "2025-Mining)-Enhancing social media hate speech detection in low-resource"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, validity-psychometrics, cultural-linguistic, design-space]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 20860
dataset_construction: "crowdsourced"
languages: ["sq"]
models_tested: ["XLM-RoBERTa", "mBERT", "distil-mBERT", "BERTweet", "LSTM", "BiLSTM", "GRU", "CNN", "SVM", "Naive Bayes", "Logistic Regression", "Random Forest", "XGBoost"]
headline_numbers:
  - "XLM-RoBERTa achieves F1=85.89% on raw Albanian hate speech data, the new state-of-the-art (p.21)"
  - "SVM with character 4-gram TF-IDF achieves 84.41% accuracy, best classical ML result (p.17)"
  - "5-fold cross-validation: XLM-RoBERTa F1=85.4%±0.8, SVM F1=84.0%±0.7 (p.23)"
  - "Inter-annotator agreement Fleiss Kappa=0.71 (substantial agreement) for 3 native-speaker annotators (p.8)"
  - "Dataset: 20,860 Facebook comments, 43.71% hate speech, 56.29% non-hate (p.8-9)"
  - "Deep learning models (LSTM/BiLSTM/GRU/CNN) cluster at 80-81% F1, lower than best classical ML (p.21)"
---
## 1. Gist
This paper presents the largest Albanian-language hate speech detection dataset to date (20,860 manually annotated Facebook comments) and a systematic comparison of ML, deep learning, and transformer approaches for binary hate speech classification in a low-resource language. The work matters for values-alignment benchmarking because it addresses the under-researched challenge of building robust content moderation tools for languages lacking NLP infrastructure, demonstrates that multilingual transformers (XLM-RoBERTa) outperform classical and deep learning alternatives even on dialectally diverse informal text, and provides both a new benchmark dataset and explainability analysis (SHAP, LIME) that reveal which linguistic features drive hate speech detection in Albanian.

## 2. Benchmark/eval design features
The paper creates a new evaluation benchmark for Albanian hate speech detection with binary labels (hate speech / not-hate speech). The core construct is automated detection of hateful content in social media text characterized by dialectal variation (Gheg and Tosk Albanian), informal spelling, slang, code-switching, and implicit insults.

Evaluation compares five feature representation strategies across five classical ML models: (1) Count Vectorization, (2) word-level TF-IDF (unigram/bigram/trigram), (3) character-level TF-IDF (1-gram through 5-gram), (4) FastText word embeddings, and (5) handcrafted features (~900 features across 14 categories). Four deep learning architectures (LSTM, BiLSTM, GRU, CNN) are tested with FastText embeddings, plus four multilingual transformers (XLM-RoBERTa, mBERT, distil-mBERT, BERTweet). All models evaluated on both raw and preprocessed text. SHAP and LIME used for post-hoc interpretability.

## 3. Task format & example item
Binary classification of Albanian Facebook comments as hate speech (1) or not-hate speech (0). Training examples from annotation guidelines (p.9):

- "Ki vetem hoxh nuk esht sdi pse e ftoni ket shejtan" (He is not an Imam I don't know why you invite this devil) → Hate speech
- "Kjo ashg lop e mbuluar" (This is just a covered cow) → Hate speech
- "Urime e Suksese!" (Congratulations and Success) → Not-Hate speech
- "E drejt e secilit me marre fen qe i pelqen qe ndihet ma mire!" (It is everyone's right to choose the religion they like and feel best with!) → Not-Hate speech

Error analysis examples show challenging cases where all models fail, e.g., "Tmerri" (The terror) — labeled hate speech but all 7 models predict not-hate speech (p.23).

## 4. Scoring / grading methodology
Four metrics: Precision, Recall, F1-score (macro), and Accuracy. Confusion matrix and classification report heatmaps for best models. 75:25 train-test split with fixed random seed for reproducibility; 5-fold cross-validation additionally run for the two best models (XLM-RoBERTa and SVM 4-gram). Scoring is automated classifier-based — no human raters involved in evaluation. Reported both per-class and macro-averaged metrics (p.15).

## 5. Dataset construction & provenance
Source: Facebook comments scraped using ExportComments tool from diverse post types (news outlets, public profiles, community groups). Targeted collection of provocative/controversial posts to mitigate class imbalance common in hate speech datasets. Dataset extends prior Albanian hate speech corpora from the same research group (Fetahi et al. 2024, 15,947 comments; Fetahi et al. 2024, 11,000+ comments).

Three native Albanian-speaking NLP expert annotators independently labeled comments using comprehensive guidelines. Disagreements resolved by majority voting; contentious cases reviewed collaboratively. Fleiss Kappa = 0.71 (substantial agreement). Anonymization applied (usernames replaced with :USER: tag, URLs replaced with :URL: token). Only publicly available comments used.

Final dataset: 20,860 comments total — 11,742 not-hate (56.29%), 9,118 hate (43.71%). Hate comments average 19.78 words and 100.88 characters vs. 12.54 words and 65.82 characters for non-hate. No explicit train/val/test split announced; 75:25 split used in experiments. License not specified in extract.

## 6. Validity evidence
Inter-annotator reliability: Fleiss Kappa = 0.71 (substantial agreement per standard thresholds shown in Table 3, p.8). Construct validity supported by prior Albanian hate speech literature showing similar patterns (targeting specific communities, cultural references). XAI analysis (SHAP, LIME) provides interpretability validation: SHAP reveals that negative word count and cosine similarity with offensive texts are the strongest predictors, aligning with domain intuition. Calibration curve for SVM (Figure 9, p.19) shows predicted probabilities follow the diagonal closely, indicating reliable probability estimates. 5-fold cross-validation confirms generalizability (XLM-RoBERTa: 85.4%±0.8, p.23). No external held-out validation set; no cross-domain or cross-platform testing reported.

## 7. Saturation / discrimination
XLM-RoBERTa's best F1 of 85.89% leaves meaningful headroom (14pp gap to perfect). False negative problem persists: XLM-RoBERTa misses 415 hateful comments in the test set; SVM misses 520 (p.22). Error analysis identifies categories where all models fail: very short implicit insults ("Tmerri" / "The terror"), implicit cultural references without explicit slurs ("Bravo Četnici" / "Bravo Chetniks"), and sarcastic or context-dependent content. Model performance clusters: classical ML and DL at 80-84%, transformers at 83-86%, leaving ~14-20% errors. The dataset's targeting of provocative posts achieves near-balanced classes (44/56 split), avoiding the extreme imbalance typical of hate speech datasets, which supports better discrimination.

## 8. Multiturn / agentic aspects
n/a — single-turn binary classification task. No dialogue, multi-turn interaction, or agentic components.

## 9. Key numbers
- Dataset size: 20,860 comments; 43.71% hate speech (p.8-9)
- Inter-annotator Fleiss Kappa: 0.71 (substantial agreement) (p.8)
- XLM-RoBERTa F1 (raw data): 85.89%, accuracy: 85.93% (p.21)
- XLM-RoBERTa 5-fold CV: 85.4% ± 0.8 F1 (p.23)
- SVM 4-gram char TF-IDF accuracy: 84.41% (p.17)
- SVM 5-fold CV: 84.0% ± 0.7 F1 (p.23)
- mBERT F1 (raw): 84.08% (p.21)
- Best classical ML (LR, Count Vectorization, preprocessed): 82.63% accuracy (p.16)
- DL models (LSTM/BiLSTM/GRU/CNN): cluster at 80-81% F1 (p.21)
- FastText embeddings best: LR F1=77.72% (p.18)
- Handcrafted features (XGBoost, RFE): best F1=77.07% (p.18)
- XLM-RoBERTa false negatives in test: 415 hateful samples missed (p.22)
- SVM false negatives in test: 520 hateful samples missed (p.22)
- Hate speech comments average word count: 19.78 vs. 12.54 for non-hate (p.9)
- RFE optimal feature count: ~500 retained for best performance (p.19)

## 10. Pitfalls & limitations
- Binary classification only (hate vs. non-hate); no fine-grained categories (religious, ethnic, gender-based hate) despite collected data having such potential (p.1-2).
- Dataset restricted to Facebook; may not generalize to other Albanian social media platforms.
- Dialectal coverage limited by annotator selection; Tosk dialect potentially underrepresented relative to Gheg.
- Three annotators, while qualified, is a small pool; crowdsourcing at scale could improve coverage.
- No Albanian-specific pretrained transformer exists; all transformer models use multilingual pretraining, leaving potential performance on the table.
- FastText embeddings trained on formal standard Albanian underperform on social media text — domain mismatch highlighted (p.18).
- Very short implicit insults and cultural references remain unsolvable by all current models (p.23-24).
- Targeted collection of provocative posts improves balance but may introduce selection bias.
- No temporal test set or held-out evaluation set from a different time period.
- Hardware constraints limited RFE step size to 50 features per iteration (p.18).

## 11. Novel ideas worth stealing
1. **Character-level n-gram TF-IDF as a robust low-resource baseline**: For any values-alignment benchmark dealing with low-resource or dialectally variable language, character 4-grams provide competitive performance (84%) with no language-specific resources and high tolerance for spelling variation. This is directly reusable for multilingual benchmark development.
2. **Targeted provocative-post collection for balanced annotation**: Rather than random sampling (which yields <15% positive instances in hate speech), explicitly target controversial posts to achieve near-balanced class distribution. This strategy reduces annotation costs and improves classifier discrimination — applicable to any imbalanced values-relevant construct (e.g., harmful refusals, value violations).
3. **Dual XAI analysis (SHAP global + LIME local)**: Using SHAP for global feature importance alongside LIME for individual failure cases provides complementary views: SHAP tells you which features drive predictions across the dataset; LIME diagnoses specific model failures. This framework is directly reusable for diagnostic analysis of values-alignment evaluators.
4. **Qualitative error typology**: Systematic manual annotation of misclassified examples produces a taxonomy of failure modes (short implicit insults, cultural references, sarcasm, truncated context). Including such a typology in any benchmark makes explicit where automated evaluation breaks down — useful for setting human-review thresholds.
5. **Cross-validation stability as a second metric alongside peak performance**: Reporting both peak F1 and cross-validated F1±SD provides a more honest picture of model reliability, distinguishing models that are good on average from those that are consistently good.
6. **Annotation training phase**: Having annotators undergo calibration on sample comments with diverse examples before independent labeling is a best practice that can improve inter-rater agreement for subjectively defined constructs — directly applicable to values-alignment annotation.

## 12. Notable quotes
- "Character-level 4-gram TF-IDF consistently reinforces ML classifiers effective with informal spelling and slang." (p.1)
- "Although our dataset is the largest available for Albanian hate speech, it remains relatively small by deep learning standards." (p.21)
- "Even our best model has not fully solved the detection challenge." (p.22)
- "Despite incorporating nearly 900 handcrafted features, analysis revealed that 500 or more were still retained by RFE for optimal performance — an unusually high number." (p.23)

## 13. UNKNOWN / not in extract
- Full list and definitions of all ~900 handcrafted features (Table 5 shows categories but not all individual features)
- License information for the dataset
- Whether the dataset is publicly released or available for download
- Exact train/test split sizes (total is 20,860; 75:25 implies ~15,645 train / ~5,215 test, but not explicitly stated)
- Error analysis results beyond pages 23-24 (extract truncated)
- Details of LIME analysis on specific edge cases
- Inter-annotator disagreement resolution rate (how many contentious cases required collaborative review)
- Cost or time of annotation process
- Whether code is publicly released
