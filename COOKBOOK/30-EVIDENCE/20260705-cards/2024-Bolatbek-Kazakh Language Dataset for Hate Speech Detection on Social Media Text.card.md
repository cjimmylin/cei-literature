---
stem: "2024-Bolatbek-Kazakh Language Dataset for Hate Speech Detection on Social Media Text"
reader_model: "sonnet"
confidence: "low"
is_benchmark: false
theme_tags: [cultural-linguistic, validity-psychometrics]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: null
dataset_construction: "scraped"
languages: ["en", "id"]
models_tested: []
headline_numbers:
  - "English large dataset (300k): without stemming/lemmatization achieves highest accuracy 93.166%; stemming achieves lowest 92.930% (p.6, Table 2)"
  - "English small dataset (5k): lemmatization achieves 91.075% accuracy; stemming 90.850% (p.6, Table 2)"
  - "Indonesian balanced dataset: stemming achieves 82.080% accuracy vs. 81.887% without stemming (p.6, Table 2)"
  - "Lemmatization on large English dataset: worst computation time 5 hours 10 minutes 25.2 seconds (p.8, Table 3)"
---
## 1. Gist
**IMPORTANT NOTE: The extract for stem "2024-Bolatbek-Kazakh Language Dataset for Hate Speech Detection on Social Media Text" contains a completely different paper — "Evaluation Analysis of the Necessity of Stemming and Lemmatization in Text Classification" by Ni Wayan Sumartini Saraswati et al. (Institut Bisnis dan Teknologi Indonesia), published in Matrik: Jurnal Manajemen, Teknik Informatika, dan Rekayasa Komputer, Vol. 24, No. 2, March 2025. This card is based on the actual extract content, not the expected Kazakh hate speech dataset paper.**

The actual paper compares the effect of stemming and lemmatization preprocessing on SVM text classification performance across four experimental scenarios: large English sentiment dataset (300k hotel reviews), small English sentiment dataset (5k), balanced Indonesian hate speech dataset (11k), and unbalanced Indonesian hate speech dataset (13k). The core finding is that stemming generally degrades English classification performance (due to aggressive context loss) while slightly improving Indonesian balanced dataset performance (due to morphological complexity). Lemmatization helps small datasets but not large ones. This paper is relevant to values-alignment benchmarking only as a methodological note on text preprocessing choices for hate speech datasets.

## 2. Benchmark/eval design features
This is a **text preprocessing comparison study**, not a values-alignment benchmark. Core claims:
- Stemming (PorterStemmer) consistently degrades English classification accuracy relative to no preprocessing and lemmatization, due to context loss.
- Lemmatization improves accuracy on small datasets (reduces sparsity) but not large datasets (where word form variety is already well-represented).
- For Indonesian (morphologically complex language), stemming with Sastrawi library improves classification on balanced datasets by mapping diverse affixed forms to root words.
- On imbalanced Indonesian datasets, stemming degrades minority class detection by removing distinctive patterns.
- Computation time: stemming is fastest; lemmatization on large datasets is slowest.

## 3. Task format & example item
n/a — this is a methodology study. The classification task is binary (hate speech / not hate speech for Indonesian data; positive / negative sentiment for English data).

## 4. Scoring / grading methodology
SVM classifier with TF-IDF features; 10-fold cross-validation (80/20 train/test split). Metrics: accuracy, precision, recall, F1-score, specificity. Evaluation is on held-out test folds.

## 5. Dataset construction & provenance
- **English dataset:** 515K Hotel Reviews in Europe from Kaggle (Booking.com), truncated to 300k (150k positive, 150k negative) for Scenario 1 and 5k (2.5k each) for Scenario 2.
- **Indonesian dataset:** Multi-label hate speech and abusive language Twitter dataset (Ibrohim & Budi, 2019, ACL); 13,169 tweets (7,608 non-hate, 5,561 hate speech); used as balanced (11,036) and unbalanced (13,044) splits.
- Preprocessing tools: NLTK PorterStemmer and WordNetLemmatizer for English; Sastrawi for Indonesian.

## 6. Validity evidence
- 10-fold cross-validation mitigates overfitting and provides stable accuracy estimates.
- Four experimental scenarios provide coverage across dataset sizes, languages, and class balance conditions.
- Results compared to prior work ([4], [5], [6]) showing consistency with expected patterns.
- No inter-annotator reliability analysis; relies on existing labeled datasets.

## 7. Saturation / discrimination
Not applicable to values-alignment benchmarking.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- Scenario 1 (English, 300k): accuracy without preprocessing 93.166%, with lemmatization 93.162%, with stemming 92.930% (p.6, Table 2)
- Scenario 2 (English, 5k): lemmatization 91.075%, without 90.900%, stemming 90.850% (p.6, Table 2)
- Scenario 3 (Indonesian balanced, 11k): stemming 82.080%, without stemming 81.887% (p.6, Table 2)
- Scenario 4 (Indonesian imbalanced, 13k): without stemming 82.626%, stemming 81.926% (p.6, Table 2)
- Stemming computation time on 300k English: 4 hrs 51 min 41.3s (fastest) (p.8, Table 3)
- Lemmatization computation time on 300k English: 5 hrs 10 min 25.2s (slowest) (p.8, Table 3)

## 10. Pitfalls & limitations
- The paper is entirely about text preprocessing for SVM classifiers; it has no direct relevance to LLM-based values alignment benchmarking.
- SVM with TF-IDF is a shallow pipeline; results may not generalize to transformer-based models.
- The English dataset is hotel reviews (sentiment), not moral/values content; the Indonesian dataset is hate speech but the paper focuses only on preprocessing.
- The extract is misidentified under a Kazakh language dataset stem — the actual Kazakh hate speech paper is not present.

## 11. Novel ideas worth stealing
None directly applicable to values-alignment benchmark design. The paper's general lesson — that preprocessing choices should be tailored to dataset size, language morphology, and class balance — is a useful methodological reminder for annotated values datasets, but this is not a novel finding.

## 12. Notable quotes
- "Stemming will generally degrade the performance of the text classification model, especially on large and unbalanced datasets." (p.1)
- "Lemmatization is more useful for small datasets as it helps reduce sparsity, increase generalization, and maximize the available information." (p.8)
- "In unbalanced datasets, minority classes often have specific and unique patterns of words or phrases. Stemming simplifies words to their base form, which can remove these nuances, resulting in important features representing minority classes being underrepresented." (p.8)

## 13. UNKNOWN / not in extract
- The actual Kazakh language hate speech dataset paper by Bolatbek is NOT in this extract. The extract contains an entirely different paper (Saraswati et al., 2025).
- Any information about the Kazakh language dataset mentioned in the stem title is not present in this extract.
- The reason for the metadata mismatch (wrong PDF OCR'd under this stem) cannot be determined from the extract alone.
