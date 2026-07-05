---
stem: "2022-researchers-Hate Speech Classification in Bulgarian"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics]
task_format: "classifier"
scoring_type: "classifier"
dataset_size: 108142
dataset_construction: "scraped"
languages: ["bg"]
models_tested: ["LinearSVC", "Logistic Regression", "Decision Trees", "Random Forests", "Naive Bayes", "FlairNLP", "Word2Vec+CNN", "Character-Level CNN", "SimpleNN"]
headline_numbers:
  - "108,142 sentences manually annotated; 1,878 (1.74%) are hateful (p.1)"
  - "Best model: LinearSVC with character-level TF-IDF, macro F1 = 0.73 (p.1)"
  - "FlairNLP stacked embeddings best neural network: macro F1 = 0.717 (p.7)"
  - "Balanced accuracy of LinearSVC: 0.42 despite best F1 (p.7)"
---
## 1. Gist
This paper presents the first large-scale manually annotated hate speech dataset for Bulgarian — a Slavic language spoken by ~8 million people and historically underrepresented in NLP research. The authors scraped 108,142 sentences from Bulgarian online forums (primarily BG-Mamma, plus BG-Jargon and BG-Nationalists), annotated for four hate speech categories (racism, sexism, rudeness, profanity), and evaluated a broad range of classical and neural classifiers. The extreme class imbalance (~1.74% hateful) forced binary classification. The best model, a linear SVM with character-level TF-IDF features, achieves macro F1 of 0.73, while neural approaches including FlairNLP stacked embeddings achieve 0.717. The paper contributes the dataset itself and a comparative classifier benchmark, and argues for the need for datasets in underrepresented languages.

## 2. Benchmark/eval design features
Binary classification (hateful vs. non-hateful) at the sentence level, derived from a finer 4-class scheme (racism, sexism, rudeness, profanity) unified due to extreme class imbalance. 106,264 non-hateful sentences vs. 1,878 hateful (1.74%). The benchmark compares: (1) preprocessing techniques (no preprocessing vs. lemmatization vs. stemming at three levels), (2) vectorization strategies (6 vectorizers: 3 word-level TF-IDF, 3 character-level TF-IDF), and (3) classical ML models (logistic regression, LinearSVC, decision trees, random forests, naive Bayes) and neural models (SimpleNN, Word2Vec, Word2Vec+CNN, FlairNLP, Character-Level CNN). Evaluation split: 75% train, 25% test (stratified).

## 3. Task format & example item
Sentence-level binary hate speech classification. No verbatim example sentences are quoted in the extract (the datasets contain Bulgarian-language forum posts from BG-Mamma, BG-Jargon, and BG-Nationalists; example content would include slang, extremist rhetoric, and parent/family discussion forum posts).

## 4. Scoring / grading methodology
Primary metric: macro F1 (arithmetic mean of F1 for both classes, giving equal weight to hate and non-hate). Secondary metric: balanced accuracy (average recall across classes), used for practical deployment settings. Precision-recall curves and area under the precision-recall curve (auPRC) are also reported. The paper uses macro F1 as primary because accuracy is misleading with 98.26% non-hateful sentences (a dummy classifier predicting always non-hateful achieves 98% accuracy).

## 5. Dataset construction & provenance
~80% of data from BG-Mamma (largest Bulgarian forum, primarily parent/family community). Additional scraping from BG-Jargon (Bulgarian slang with example sentences) and BG-Nationalists (extremist right-wing political forum). Multi-sentence posts were first annotated as comments, then split into individual sentences, greatly increasing count. Preprocessing removed BBCode formatting, HTML, URLs, punctuation, stopwords, numbers; text lowercased. Sentence average: 14.3 words (median 11, standard deviation 12.2). Dataset publicly available at http://www.pfeffer.at/data/bulgarian/. No annotator demographic information is provided in the extract.

## 6. Validity evidence
Manual annotation by the paper's authors — no independent annotator agreement statistics are reported in the extract (only one annotator perspective described). The extreme imbalance (98.26% non-hateful) suggests high precision requirements; macro F1 is used precisely because standard accuracy would mislead. Character-level features consistently outperform word-level features across classifiers, validating that Bulgarian morphological richness makes character n-grams more robust.

## 7. Saturation / discrimination
Best classifier macro F1 = 0.73 (LinearSVC), with substantial room for improvement. Balanced accuracy of LinearSVC is only 0.42, suggesting poor recall on the hateful class despite acceptable F1. The FlairNLP neural approach achieves 0.72 macro F1 with better balanced accuracy (not explicitly stated). Word2Vec+CNN achieves best recall at 0.46. SMOTE oversampling showed little improvement over class-weighting. The rarity of hate content (1.74%) means classifiers struggle with minority class recall.

## 8. Multiturn / agentic aspects
n/a — static sentence-level classification task.

## 9. Key numbers
- 108,142 total sentences: 106,264 non-hateful, 1,878 hateful (1.74%) (p.3)
- Source breakdown: ~80% BG-Mamma, rest BG-Jargon and BG-Nationalists (p.3)
- Average sentence length: 14.3 words, median 11, SD 12.2 (p.3)
- LinearSVC macro F1: 0.728 (p.7); FlairNLP macro F1: 0.717 (p.7)
- LinearSVC balanced accuracy: 0.42 (p.7); Word2Vec+CNN balanced accuracy: 0.72 (p.7)
- Character-level SVM consistently outperforms word-level across vectorizers (p.7)
- Dummy classifier accuracy: 98% (but macro F1 much lower) (p.6)

## 10. Pitfalls & limitations
- No inter-annotator agreement reported — annotations appear to be from a single annotator or small team without reliability metrics, making quality uncertain.
- Extreme class imbalance (1.74% hateful) makes subcategory classifiers infeasible; the four original categories are merged into one binary label.
- Data is dominated by a parenting forum (BG-Mamma ~80%), which is not naturally high in hate speech, creating severe imbalance and domain-specific bias.
- BG-Nationalists as a source may introduce extremist-vocabulary bias that does not generalize to mainstream hate speech patterns.
- No transformer-based model (BERT for Bulgarian) evaluated.
- The authors acknowledge that "researchers have become overly optimistic about the results of their classifiers" because models trained on one dataset rarely generalize (citing Arango et al., 2019) (p.8).

## 11. Novel ideas worth stealing
- **Sentence-level vs. comment-level annotation**: splitting multi-sentence posts into individual sentences for annotation increased data volume and produced a more fine-grained unit of analysis — useful for values-alignment benchmarks where moral content is often localized within longer texts.
- **Balanced accuracy as a secondary metric**: reporting both macro F1 (which weights both classes equally) and balanced accuracy (average recall) alongside each other reveals when a classifier optimizes F1 by inflating precision at the cost of recall — an important distinction for safety-critical hate detection tasks.
- **Character n-gram robustness for morphologically rich languages**: showing that character-level TF-IDF outperforms word-level for Bulgarian suggests that values benchmarks using morphologically complex languages should incorporate subword or character features.
- **Dataset diversity via forum type**: combining a mainstream parenting forum, a slang repository, and an extremist political forum creates a naturalistic range from mundane to extreme content — a useful structural model for inclusive hate speech benchmarks.

## 12. Notable quotes
- "Who decides what hate speech is? Aristotle would probably not consider his writings hateful, but two thousand years later, we might." (p.1)
- "A dummy classifier predicting only one class has 98% accuracy. For this reason, the primary metric we used is macro F1." (p.6)
- "Despite the continuing efforts of the scientific community, there are some fundamental issues with solving hate speech classification... most research papers focus only on datasets coming from one source. That causes the models (usually deep neural networks) to overfit and are rarely able to generalize well on new datasets." (p.8)

## 13. UNKNOWN / not in extract
- Inter-annotator agreement statistics (not reported)
- Number of annotators and their backgrounds/profiles
- Whether the four original hate categories (racism, sexism, rudeness, profanity) are available for download or only the binary labels
- BERT-based model results for Bulgarian (not tested in this study)
- Breakdown of F1 by hate category before binary merging
- Licensing terms for the dataset
