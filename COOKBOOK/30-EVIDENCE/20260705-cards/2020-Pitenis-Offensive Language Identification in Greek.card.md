---
stem: "2020-Pitenis-Offensive Language Identification in Greek"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, saturation-discrimination, design-space]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 4779
dataset_construction: "crowdsourced"
languages: ["el"]
models_tested: ["Linear SVM", "RBF SVM", "SGDC", "Multinomial NB", "Bernoulli NB", "Pooled GRU", "Stacked LSTM with Attention", "LSTM and GRU with Attention", "2D Convolution with Pooling", "GRU with Capsule", "LSTM with Capsule and Attention", "BERT-Base Multilingual Cased"]
headline_numbers:
  - "LSTM and GRU with Attention achieved F1-macro of 0.89 on OGTD v1.0 (p.5)"
  - "BERT-Base Multilingual Cased achieved only F1-macro of 0.73 (p.5)"
  - "Linear SVM with TF-IDF unigrams achieved F1-macro of 0.80 (p.4)"
  - "OGTD v1.0 contains 4,779 tweets; v2.0 expands to 10,287 instances (p.6)"
  - "29% of OGTD v1.0 tweets are offensive (p.3)"
---
## 1. Gist
This paper introduces the Offensive Greek Tweet Dataset (OGTD), the first manually annotated dataset for offensive language identification in Greek. OGTD v1.0 contains 4,779 Twitter posts annotated as offensive or not offensive by three volunteer annotators, with inter-annotator agreement measured by Cohen's kappa. The paper benchmarks a range of classical machine-learning and deep-learning models on this dataset. For values-alignment benchmarking, the work is significant as a demonstration of how language-specific offensive-content datasets require culturally grounded annotation: Greek slang, irony, and context-dependent profanity create challenges that generic multilingual models (e.g., multilingual BERT) cannot adequately handle, revealing the importance of language-specific data for offensive-content detection across cultures.

## 2. Benchmark/eval design features
The benchmark involves binary classification of Greek tweets as offensive or not offensive (with spam filtered out). The label taxonomy follows the OLID dataset for English (Zampieri et al., 2019a). Items are individual tweets; the answer space is binary (Offensive / Not Offensive). The paper also reports v2.0 of the dataset (10,287 instances) as training data for OffensEval 2020 (SemEval-2020 Task 12). Key model comparisons: five classical ML models with multiple feature configurations (TF-IDF unigrams/bigrams, POS tags, dependency relations) and seven deep learning architectures using Greek word embeddings plus multilingual BERT.

## 3. Task format & example item
Binary classification. The annotation task asks annotators to label each tweet as "Offensive," "Not Offensive," or "Spam."

Example item (p.2):
Tweet collected from Twitter, possibly containing the keyword "μαλάκας" (malakas, "asshole") or "είσαι" (you are), annotated as Offensive or Not Offensive by three volunteers.

No verbatim tweet examples are given in the extract as items for models to classify; the extract describes the annotation process and query methodology in detail.

## 4. Scoring / grading methodology
Models are evaluated using Precision, Recall, and F1 on each class (Offensive, Not Offensive), along with weighted average and macro-F1. Macro-F1 is used to evaluate performance without regard to label imbalance. Best model is selected based on recall for the Offensive class being critical for real-world deployment.

## 5. Dataset construction & provenance
Tweets were collected May–June 2019 using the Twitter API querying trending hashtags and keyword searches for Greek profanity (curse words, expletives, "you are" constructions). Initial pool of 49,154 tweets was filtered and de-duplicated to 46,218; 5,000 were randomly sampled for annotation, producing 4,779 labeled tweets (221 removed as spam). Annotation was performed via LightTag by three volunteers using explicit guidelines written in Greek. Labels with 100% agreement were accepted; majority (>66%) resolved disagreements; full disagreement cases were adjudicated by additional reviewers. Train/test split: 3,345/1,434. No explicit license mentioned.

## 6. Validity evidence
Inter-annotator agreement measured by Cohen's kappa across all three annotator pairs (Figure 1, p.3). The extract shows a confusion matrix of kappa values but does not state the specific numerical kappa values for each pair beyond showing the figure. The annotation guidelines were adapted from the validated OLID English dataset methodology. Validity is indirectly supported by the replication of findings from comparable Danish and Turkish offensive-language datasets. The best model (LSTM and GRU with Attention) achieving F1-macro of 0.89 suggests the dataset is learnable and discriminative.

## 7. Saturation / discrimination
The offensive class comprises about 29% of the dataset (1,401/4,779). Classical ML models show lower recall on the Offensive class (RBF SVM recall for Offensive: 0.31; Bernoulli NB: 0.61) compared to deep learning models (LSTM+GRU recall for Offensive: 0.68). The BERT multilingual model underperforms substantially (F1-macro 0.73 vs. 0.89 for LSTM+GRU), demonstrating significant headroom between language-agnostic and language-specific approaches. No ceiling effects reported.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- Total annotated tweets (v1.0): 4,779 (p.3)
- Offensive tweets (v1.0): 1,401 (29.3%) (p.3)
- Training set size: 3,345; Test set: 1,434 (p.3)
- Best model (LSTM and GRU with Attention) F1-macro: 0.89 (p.5)
- Best classical model (Linear SVM, TF-IDF unigrams) F1-macro: 0.80 (p.4)
- BERT-Base Multilingual Cased F1-macro: 0.73 (p.5)
- OGTD v2.0 total instances: 10,287 (p.6)
- Offensive tweets (v2.0): 2,911 (p.6)
- Initial tweet pool before filtering: 49,154 (p.3)

## 10. Pitfalls & limitations
- Dataset size (4,779) is small; authors note this limitation influences model choices and default hyperparameter settings (p.3).
- POS tagging accuracy for Greek via spaCy is uncertain; the paper notes it "is not yet clear whether" poor performance with POS features is due to spaCy's accuracy or the features themselves (p.5).
- The dataset contains neologisms, creative language, and rare slang that challenge models (p.5).
- v1.0 data was collected during a specific narrow window (elections, TV shows in Greece in May–June 2019), reducing topical diversity.
- No formal license for the dataset is stated.
- Only binary offensiveness is annotated; targeted types (hate speech, cyberbullying, profanity) are not distinguished.

## 11. Novel ideas worth stealing
- **Keyword-seeded sampling strategy**: Collecting tweets using offensive keywords (slurs, "you are" constructions) to oversample the minority offensive class in a new language is a replicable low-cost method for building targeted offensive-language corpora in under-resourced languages.
- **Adversarial context: irony and pragmatics in non-English**: The paper highlights that recognizing ironic vs. insulting uses of swear words is a challenge specific to Greek — worth building into evaluation design for any cross-cultural values-alignment benchmark.
- **Monolingual embeddings beat multilingual BERT by large margin** (0.89 vs. 0.73): A concrete empirical reminder that language-specific resources for non-English evaluation are not well-served by generic multilingual models, relevant to benchmark designers who rely on zero-shot or multilingual models.
- **Cross-lingual testbed via shared annotation guidelines**: By using the same OLID annotation schema as English, Danish, and Turkish datasets, OGTD enables direct cross-lingual comparisons — a useful design pattern for cultural-linguistic benchmarks.

## 12. Notable quotes
- "The challenge is to recognize between ironic and insulting uses of these swear words, a common phenomenon in Greek." (p.2)
- "For a binary text classification task like offensive language detection, a high recall score for both classes, especially for the Offensive class, is important for a model to be considered successful." (p.4)
- "For this task monolingual Greek word embeddings perform significantly better than the multilingual bert embeddings." (p.5)
- "OGTD v1.0 and v2.0 provide the opportunity for researchers to test cross-lingual learning methods as it can be used in conjunction with the English OLID and other datasets annotated using the same guidelines." (p.6)

## 13. UNKNOWN / not in extract
- Exact Cohen's kappa values per annotator pair (figure referenced but not numerically reported in text).
- License for OGTD v1.0 or v2.0.
- Whether the dataset is balanced across topical categories (elections, TV shows, etc.).
- Full details of LightTag annotation interface and worker compensation.
- Whether data is publicly available and at what URL (a GitHub URL for code is given but not dataset release).
