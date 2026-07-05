---
stem: "2023-Narayan-HASOC 2023 Hate Speech and Offensive Content Identification in"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: null
dataset_construction: "crowdsourced"
languages: ["Bengali", "Assamese", "Bodo", "Sinhala", "Gujarati"]
models_tested: ["BERT Base Multilingual Cased", "BERT Base Multilingual Uncased", "DistilBERT Base Multilingual Cased", "XLM-Roberta-Base", "MuRIL Base Cased", "XLM-Indic Base Multiscript", "XLM-Indic Base Uniscript", "BanglaBERT", "SinhalaBERTo", "LSTM-Attention"]
headline_numbers:
  - "BERT Base Multilingual Cased: F1=0.83009 for Bodo, F1=0.70525 for Assamese, F1=0.67027 for Bengali (p.1)"
  - "XLM-R: F1=0.83493 for Sinhala (p.1)"
  - "LSTM baseline: F1=0.76601 for Gujarati (best model for that language) (p.1)"
  - "BanglaBERT: F1=0.75625 for Bengali (best for Bengali) (p.8)"
  - "Competition standings: 3rd/20 Bengali, 5th/16 Sinhala, 7th/17 Gujarati, 8th/20 Assamese, 12th/19 Bodo (p.8)"
  - "Sinhala train set: 7,500 samples; test set: 2,500 samples (p.4)"
  - "Gujarati train set: only 200 tweets; test set: 1,196 tweets (few-shot setting) (p.4)"
---
## 1. Gist
This system paper describes team Z-AGI Labs' entry to HASOC 2023, a shared task on hate speech and offensive content identification in five South/Southeast Asian low-resource languages: Bengali, Assamese, Bodo, Sinhala, and Gujarati. The paper presents a comparative study of LSTM-attention and transformer models (mBERT variants, XLM-R, MuRIL, XLM-Indic, BanglaBERT, SinhalaBERTo) on binary HOF/NOT classification tasks. For values-alignment benchmarking, this paper is relevant as a concrete example of cross-lingual, low-resource hate speech detection—illustrating both the state of the art and the challenges of extending content safety systems beyond English to languages with limited training data.

## 2. Benchmark/eval design features
Two tasks in HASOC 2023:

- **Task 1** (Sinhala, Gujarati): Binary classification—HOF (Hate and/or Offensive) vs. NOT. Evaluated on macro-F1, Precision, and Recall.
- **Task 4** (Bodo, Bengali, Assamese): Same binary classification. Evaluated on macro-F1 only.

The benchmark is a shared competition with multiple participating teams per language. The evaluation is on hidden test sets; final scores come from official organizer-provided leaderboards. Dataset sizes vary substantially across languages, creating different challenge modes: Sinhala is a reasonably-sized classification task (7,500 train), while Gujarati is few-shot (200 train tweets).

The paper contributes: preprocessing pipelines, an LSTM-with-attention baseline, zero-shot/few-shot evaluation of pretrained models, and fine-tuning of multilingual transformers.

## 3. Task format & example item
Binary text classification. Input: a social media post (tweet, Facebook post, YouTube comment). Output: HOF or NOT. 

No verbatim example items are provided in the extract. The task is described as: "classify a given content into one of the following classes: HOF (Hate and/or Offensive): This content is hate speech, offensive, and/or profane. NOT (Non-Hate and/or Offensive): This content is not hate speech, offensive, and/or profane." (p.2)

## 4. Scoring / grading methodology
**Task 4**: macro-F1 on hidden test set (labels: HOF=0, NOT=1).
**Task 1**: macro-F1, Precision, and Recall on hidden test set.

Inference: ensemble predictions from K=5 cross-validation folds with equal weight on logits; threshold at 0.5. For training, Adam optimizer with binary cross-entropy loss.

## 5. Dataset construction & provenance
- **Sinhala**: Based on SOLD (Sinhala Offensive Language Detection dataset). 7,500 train samples, 2,500 test samples. Original SOLD has 10,000 manually annotated tweets.
- **Gujarati**: 200 train tweets, 1,196 test tweets. Few-shot setting.
- **Assamese, Bodo, Bengali**: From X (Twitter), Facebook, and YouTube comments. Each is a separate Kaggle competition. Train set sizes not specified numerically in extract.
- All datasets contain tweet-label pairs; sources include X, Facebook, and YouTube comments.
- Preprocessing: emoji conversion (emot library), hashtag tokenization (Ekphrasis), emoji2vec embeddings for emoji semantics, removal of @USER mentions and repetitive punctuation.
- All datasets are binary (fairly balanced per description in p.5).

## 6. Validity evidence
Limited formal validity analysis. The paper reports leaderboard macro-F1 scores on organizer-provided hidden test sets, which provides some external validity. K-fold cross-validation (K=5) with fixed random seed (2023) is used for model selection. No inter-annotator reliability or construct validity analysis is reported for the benchmark itself (this is a system paper, not a benchmark design paper).

## 7. Saturation / discrimination
Best macro-F1 scores vary substantially by language: Bodo (0.83009), Sinhala (0.83493), Gujarati (0.76601), Assamese (0.70525), Bengali (0.75625 with BanglaBERT). The low Assamese score for XLM-R (0.376) vs. mBERT-C (0.705) indicates strong model-language interactions—the benchmark discriminates between models effectively. The Gujarati few-shot setting (200 train samples) is a particularly challenging setup where the LSTM baseline surprisingly outperforms most transformers, suggesting headroom and unexpected model behavior.

## 8. Multiturn / agentic aspects
n/a. Single-post binary classification.

## 9. Key numbers
- Sinhala train: 7,500 samples; test: 2,500 (p.4)
- Gujarati train: 200 tweets; test: 1,196 (p.4)
- K=5 cross-validation folds, random seed=2023 (p.5)
- Best Bodo: mBERT-C F1=0.83009 (p.8)
- Best Assamese: mBERT-C F1=0.70525 (p.8)
- Best Bengali: BanglaBERT F1=0.75625 (p.8)
- Best Sinhala: XLM-R F1=0.83493 (p.8)
- Best Gujarati: LSTM F1=0.76601 (p.8)
- Competition standings: 3rd/20 Bengali, 5th/16 Sinhala, 7th/17 Gujarati, 8th/20 Assamese, 12th/19 Bodo (p.8)
- LSTM Bodo: F1=0.81291 (competitive with mBERT at 0.83009) (p.8)
- MuRIL Bodo: F1=0.35085 (poor, despite being an Indic language model) (p.8)

## 10. Pitfalls & limitations
- Training set sizes are very small for some languages (Gujarati: 200 samples), which makes any generalization conclusions tenuous
- The paper does not analyze errors by category or sub-type of hate speech
- No ablation on which preprocessing steps contribute most to performance
- MuRIL underperforms for Bodo (F1=0.35 vs. mBERT's 0.83)—unexplained and potentially a bug or domain mismatch not discussed
- Binary HOF/NOT classification collapses a spectrum of offensiveness into two categories, limiting utility for nuanced content moderation
- Gujarati's train/test imbalance (200 train, 1,196 test) is unusual and could reflect noisy evaluation
- Results are from a competitive submission, not a controlled research setting; time constraints are acknowledged
- No analysis of code-switching or multilingual content, which is prevalent in Indic social media

## 11. Novel ideas worth stealing
1. **Emoji2vec integration for safety benchmarks**: Handling emojis semantically rather than removing them or treating them as unknown tokens is important for hate speech detection on social media. Values-alignment benchmarks on social media content should include emoji-heavy instances.
2. **K-fold ensemble inference**: Ensembling predictions across folds rather than training a single model improves robustness without requiring separate validation data—relevant for low-resource evaluation settings.
3. **LSTM-attention as a baseline for low-resource settings**: The surprising competitiveness of LSTM-attention against transformers in the few-shot Gujarati setting is a practical finding: for low-resource values-alignment benchmarks, simple baselines may rival large pretrained models.
4. **Language-specific vs. multilingual model tradeoffs**: The paper's comparisons reveal that language-specific models (BanglaBERT for Bengali) outperform multilingual models (mBERT) when sufficient training data exists, but multilingual models are better when data is scarce—informative for cross-lingual benchmark design.
5. **Code-switching as a benchmark challenge**: The paper notes code-mixed English words appear across all languages but does not analyze their effect. Future values-alignment benchmarks in multilingual contexts should explicitly sample code-switched content.

## 12. Notable quotes
- "Results reveal intriguing variations in model performance. Notably, Bert Base Multilingual Cased emerges as a strong performer across languages, achieving an F1 score of 0.67027 for Bengali and 0.70525 for Assamese." (p.1)
- "Though the transformer shows sheer dominance in the majority of the tasks, our LSTM baseline emerges as a strong competitor with promising results, even resulting in the highest f1-score amongst our candidate models for Gujarati." (p.9)
- "The lack of large-scale corpus and pre-trained models makes it extremely difficult to tackle Natural Language Understanding (NLU) downstream tasks." (p.2)
- "We plan to further extend our work to other low-resource indic languages, and explore the possibilities of zero-shot, few-shot, and cross-lingual transfer learning scenarios." (p.9)

## 13. UNKNOWN / not in extract
- Exact train set sizes for Assamese, Bodo, and Bengali
- Class distribution percentages (described as "fairly balanced" but no numbers given)
- Details of the organizer's hidden test set construction and labeling process
- Inter-annotator reliability for the SOLD Sinhala dataset
- Whether the LSTM baseline was tuned on a language-by-language basis or shared hyperparameters
- Hyperparameter values used for each model-language combination
- Whether any LLMs (GPT-4, etc.) were tested in the competition
