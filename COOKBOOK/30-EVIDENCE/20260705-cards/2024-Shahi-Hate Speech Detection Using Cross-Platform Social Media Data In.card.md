---
stem: "2024-Shahi-Hate Speech Detection Using Cross-Platform Social Media Data In"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices, validity-psychometrics, contamination-robustness]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 7952
dataset_construction: "crowdsourced"
languages: ["en", "de"]
models_tested: ["BERT", "DistilBERT", "SVM", "LSTM", "Logistic Regression"]
headline_numbers:
  - "Best English F1: 0.74 (EY1+ET4+EG1 combination, YouTube + Twitter + Gab) (p.8)"
  - "Best German F1: 0.68 (GY1+GT1+GT2 combination) (p.8)"
  - "Cohen's kappa for YouTube annotation: 0.86 (p.4)"
  - "1,892 English and 6,060 German YouTube comments annotated (p.2)"
  - "English hate speech rate: 37.36%; German: 4.6% (Table 1, p.4)"
---
## 1. Gist
Shahi and Majchrzak (2024) present a bilingual (English/German) hate speech detection study built around YouTube comments, systematically augmenting a newly annotated YouTube corpus with eight external datasets from Twitter, Gab, and Wikipedia. The key research question is whether — and under what conditions — adding external cross-platform data improves classifier performance. The study proposes three dataset similarity measures (definition similarity, content similarity, hate word similarity) to predict which external datasets will be most beneficial. The paper contributes (1) a new YouTube hate speech dataset in English and German, (2) a principled dataset compatibility framework, and (3) empirical evidence that content similarity and definition similarity are the best predictors of cross-dataset transfer value. For values-alignment benchmarking the paper is highly relevant as a methodological reference for the benchmark generalizability problem: it shows that a hate-speech classifier trained on one platform/language can be substantially improved by data from another platform if similarity conditions are met — with direct implications for whether values benchmarks transfer across cultural contexts.

## 2. Benchmark/eval design features
**Constructs measured:** Binary hate speech classification (hate speech vs. not hate speech) in YouTube comments.

**New dataset:** EY1 (1,892 English YouTube comments) and GY1 (6,060 German YouTube comments). Topics: politics, LGBT rights, immigration, abortion, war, sex education, entertainment, sports.

**External datasets used (8 total):**
- English: ET1 (Twitter, HASOC, 7,005), ET2 (Twitter, Davidson, 24,783), ET3 (Twitter, HatEval, 12,971), ET4 (Twitter, Waseem, 10,498), EW1 (Wikipedia, 312,735), EG1 (Gab, 27,265)
- German: GT1 (Twitter, HASOC, 4,469), GT2 (Twitter, Ross, 470)

**Hate speech definition used for annotation:** "Language that expresses prejudice against a person from a group or a particular group, primarily based on ethnicity, religion, or sexual orientation." (p.4, cross-platform cross-language definition)

**Similarity measures:**
1. Definition similarity — crowdsourced survey (Prolific, 90 participants) on 10-point scale
2. Content similarity — cosine similarity of XLM-RoBERTa sentence embeddings
3. Hate word similarity — Hurtlex lexicon intersection

## 3. Task format & example item
Binary classification of a YouTube comment as hate speech (1) or not hate speech (0). Comments collected on controversial YouTube video topics; hate words identified by annotators during annotation.

No verbatim example comment is provided in the extract (content is social media data, not reproduced in paper), but the annotation uses a single binary label per comment.

## 4. Scoring / grading methodology
- **Classifier:** BERT (DistilBERT fine-tuned), also SVM, LSTM, Logistic Regression (BERT outperforms all, results shown for BERT only)
- **Training/test split:** 70%/30% of YouTube data (EY1, GY1); test set held constant across all data combinations
- **Class balancing:** Undersampling to equal class distribution (tested to outperform using original imbalanced data)
- **Metrics:** Precision, Recall, F1-score per class (hate, non-hate) and overall F1
- **BERT hyperparameters:** Learning rate 3e-5, batch size 32, sequence length 128, 6 epochs

## 5. Dataset construction & provenance
- **YouTube collection:** Python crawler using pytube library; searched controversial topic keywords; language-filtered using fastText; 101 English and 89 German videos; 30,663 English and 18,441 German comments before filtering; 2,000 English and 6,500 German randomly subsampled for annotation.
- **Annotation:** 3 annotators with CS backgrounds; majority vote; hate words also identified per comment. Cohen's kappa = 0.86.
- **English hate rate:** 37.36% (EY1); German hate rate: 4.6% (GY1) — notable imbalance.
- **Partial public release:** YouTube comment IDs and video IDs to be released (not full text due to YouTube data policy). GitHub: https://github.com/Gautamshahi/BilingualYouTubeHateSpeech
- **External datasets:** Collected from published literature; only 10,498 of 16,914 labeled Waseem (ET4) tweets crawlable due to deletion (p.6).

## 6. Validity evidence
- **Inter-annotator agreement:** Cohen's kappa = 0.86 for YouTube annotation (p.4) — high reliability.
- **Definition validity:** Definition similarity survey (Prolific, N=90 after exclusions) provides crowd-based validity check on how well external dataset definitions align with the YouTube dataset definition.
- **Convergent validity:** Content similarity (cosine) and hate word overlap both independently predict classification performance improvement, suggesting the underlying construct (hate-relevant content) is capturing the same latent variable across platforms.
- **Predictive validity:** Definition similarity predicts performance gains for English; content similarity most directly predicts German performance gains.

## 7. Saturation / discrimination
- Best F1: 0.74 English, 0.68 German — moderate headroom remaining.
- German performance substantially lower, partially explained by small base dataset (6,060 total, only ~280 hate comments at 4.6%) and lower hate word overlap with other datasets.
- Using only EY1 baseline: F1 = 0.64; best combination EY1+ET4+EG1: 0.74 — meaningful 10-point improvement from cross-platform augmentation.
- Some dataset combinations reduce performance (e.g., EY1+ET1 gives Hate F1 of only 0.51 vs. 0.64 baseline), confirming that incompatible datasets can hurt performance.

## 8. Multiturn / agentic aspects
n/a — static single-turn text classification task.

## 9. Key numbers
- 1,892 English YouTube comments in EY1; 6,060 German in GY1 (p.2)
- English hate rate: 37.36% (EY1); German: 4.6% (GY1) (Table 1, p.4)
- Cohen's kappa = 0.86 for annotation (p.4)
- 3 annotators, majority vote (p.4)
- Definition similarity survey: 90 valid participants (10 excluded for speed), Prolific (p.5)
- Best English F1: 0.74 (EY1+ET4+EG1) (p.8)
- Best German F1: 0.68 (GY1+GT1+GT2) (p.8)
- EY1 alone: Overall F1 = 0.64; Hate F1 = 0.64 (Table 6, p.8)
- EW1 (Wikipedia, 312,735 entries) — largest external dataset; does not improve performance despite large hate word overlap (p.7)
- Gab (EG1) has maximum content similarity to EY1 among English datasets (p.6)

## 10. Pitfalls & limitations
- **Low German hate rate (4.6%):** The German YouTube dataset is extremely class-imbalanced, making results less reliable and German classifiers harder to evaluate.
- **Content deletion over time:** Social media posts are deleted; Waseem (ET4) had only 10,498 of 16,914 labeled tweets recoverable (p.6) — historical datasets degrade over time, threatening reproducibility.
- **No LLM baseline:** The study uses traditional ML models (BERT, SVM, LSTM); no comparison to GPT-4 or other frontier LLMs, which the authors themselves suggest may perform better (p.7).
- **Partial data release:** Only IDs released (not text), limiting reproducibility for future researchers.
- **Narrow annotator pool:** 3 annotators with CS backgrounds are not representative of diverse community perspectives on hate speech.
- **Platform-specific biases:** YouTube comments may differ from the broader internet in ways that limit generalizability (e.g., comment sections are topic-specific, attached to videos, allowing shared context).
- **Definition variation unresolved:** The study shows definition similarity matters but does not systematically test different definition variants — there is no single agreed definition across platforms, jurisdictions, or cultures.

## 11. Novel ideas worth stealing
1. **Three-axis dataset compatibility framework:** Measuring dataset compatibility along definition, content, and hate-word similarity dimensions before deciding to augment training data is directly applicable to values-alignment benchmark construction — use these metrics to assess whether a new cultural/linguistic benchmark is compatible enough to be merged with an existing one.

2. **Cross-platform augmentation as data efficiency strategy:** When building a new values benchmark in a resource-constrained setting, systematically identifying existing compatible datasets from adjacent domains/platforms and augmenting with them (subject to similarity screening) can substitute for expensive new annotation.

3. **Prolific survey as definition operationalization:** Using a crowd-sourced survey (Prolific) to measure how similar two dataset definitions are perceived by lay raters is a reusable method for validating that two annotation schemes are conceptually aligned before merging datasets.

4. **Class imbalance undersampling benchmark:** The consistent finding that undersampling to equal class distribution outperforms using the original imbalanced dataset is a practical benchmark design recommendation — rare-category items need deliberate oversampling or balancing.

5. **"Dead link" contamination audit:** The finding that only 10,498 of 16,914 originally labeled tweets were recoverable (p.6) quantifies dataset decay and motivates benchmark designs that store full text rather than only IDs — a direct recommendation for robust benchmark construction.

## 12. Notable quotes
- "Adding more similar datasets based on content similarity, hate words, and definitions improves the performance of classification models." (p.1)
- "There is no direct relation in increasing the dataset from the same platform, but cross-platform datasets improve performance such as ET4 and EG1 jointly improve recall and F1-score." (p.7)
- "If detecting hate speech is easier, there will be less room for social media platforms to not remove hateful content." (p.7)
- "Data annotation is a key challenge, but combining datasets having a similar issue with similar content and hate words improves the classification performance." (p.7)

## 13. UNKNOWN / not in extract
- Exact definition similarity scores for German datasets beyond what's in Table 5 (only two available since not all German datasets explicitly define hate speech).
- Whether the Prolific survey participants were multilingual or English-only (important for cross-language definition validity).
- Hyperparameter details for SVM, LSTM, and Logistic Regression models (only BERT details given in Section 3.4).
- Whether there are interaction effects between definition similarity and content similarity in predicting performance gain.
