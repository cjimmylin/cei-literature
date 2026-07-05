---
stem: "2022-Jahan-Finnish Hate-Speech Detection on Social Media Using CNN and FinBERT"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 10700
dataset_construction: "crowdsourced"
languages: ["fi"]
models_tested: ["FinBERT", "mBERT", "CNN+fastText", "CNN+FinBERT", "Logistic Regression", "Naive Bayes", "Random Forest"]
headline_numbers:
  - "10,700 Finnish sentences; 1,786 hate (16.7%) / 8,914 non-hate (83.3%) (p.2, Table 1)"
  - "FinBERT achieves 91.7% accuracy and 90.8% F1-score, best of all models (p.5, Table 4)"
  - "mBERT achieves only 88.2% accuracy and 85.3% F1, 3.5% and 5% below FinBERT (p.5)"
  - "Inter-annotator agreement Krippendorff's α=0.92 (p.3)"
---
## 1. Gist
Jahan, Oussalah, and Arhab construct and release the first Finnish hate speech dataset drawn from the Suomi24 online forum (2001–2017), annotating 10,700 sentences across five hate categories (racism/racial segregation, sexual, xenophobia, religious intolerance/fundamentalism, homophobia) with binary hate/non-hate labels. They then evaluate Finnish-specific (FinBERT) and multilingual (mBERT) transformer models against CNN+fastText and non-deep-learning baselines. For values-alignment benchmarking, this paper's contributions are: (1) a rare high-quality non-English hate speech dataset with strong annotation agreement (α=0.92); (2) a demonstration that language-specific pretraining dramatically outperforms multilingual models (3.5–5% gap in a low-resource language setting); (3) a methodological example of profane-word seeding + random sampling for constructing realistic class-imbalanced hate speech corpora.

## 2. Benchmark/eval design features
Binary hate speech classification benchmark with:
- **Source corpus**: Suomi24 (Finnish online social networking forum), VRT version 1.1, covering 2001–2017 with 35M+ sentences.
- **Sampling strategy**: 5k sentences selected by profane-word string matching (to oversample hate), remaining up to 10.7k selected randomly from the corpus (which contains ~0.93% hate naturally).
- **Five hate categories**: racism/racial segregation, sexual content, xenophobia, religious intolerance/fundamentalism, homophobia.
- **Label granularity**: Binary (hate=1 / non-hate=0); category labels are used for construction but not final classification targets.
- **Annotation criteria**: Two independent annotators; third expert referee for disagreements (197 total disagreements).
- **Annotation rules**: (1) Target must be a group, individual, or organization; (2) message must incite, spread, promote, support violence/hatred, or aim to dehumanize, delegitimize, hurt, or intimidate the target.

## 3. Task format & example item
Binary sentence-level classification. Example items from corpus (Table 3, p.4):
- "vittu mik tollo" → "F**k mik tollo" → Label 1 (hate)
- "Nyt on kovaa setti" → "Now there is a hard set" → Label 0 (non-hate)
- "Kuinka lyhyet ovat lyhimmät shortsisi, päätän sen pienen" → "How short is your shortest shorts, I head its small" → Label 1 (hate without explicit slur)
- "Muslimit eivät ole pahoja" → "Muslims are not bad bro" → Label 0 (non-hate)

Profane word examples (Table 2, p.3): Vittu (F**k), Narttu (B**ch), Pillua (P**sy), Neekeri (Nigger), etc.

## 4. Scoring / grading methodology
Evaluation metrics: accuracy (%) and F1-score (%). Train: 6,700 sentences; validation: 1,000; test: 3,000 (all from the 10,700 total). For BERT models: fine-tuned for 6 epochs, learning rate 5e-6, max sequence length 128, batch size 4, evaluated on test set after each epoch. For CNN: 1D convolution, kernel size 3, max-over-time pooling, dense layer 50, dropout + L2 regularization. Non-deep learning models use TF-IDF features (word-level, n-gram word level N=2,3, n-gram character level N=3,4) restricted to 5,000 features.

## 5. Dataset construction & provenance
- **Source**: Suomi24 corpus 2001–2017, VRT version 1.1 (http://urn.fi/urn:nbn:fi:lb-2020021801), originally 35M+ sentences.
- **Profane word seed list**: ~10 most frequent profane words identified from corpus used for initial filtering (Table 2 lists examples including Vittu, Narttu, Pillua, Neekeri, Perse, Homo, Pedot, swear words).
- **Annotation**: 2 independent annotators + 1 expert referee. 197 disagreements resolved by referee.
- **Release**: GitHub page (github.com/saroarjahan/FinBERT).
- **Final statistics**: 10,700 sentences; 1,786 hate (16.7%), 8,914 non-hate (83.3%).

## 6. Validity evidence
- **Inter-annotator agreement**: Krippendorff's α=0.92 (nominal metric), computed using formula that accounts for incomplete data and chance disagreement. This is an exceptionally high agreement for a subjective annotation task.
- **Expert annotation**: Two annotators with master's theses in hate speech detection/NLP; expert referee with PhD in the field.
- **Disagreement analysis**: 4 illustrative edge cases discussed (p.3-4): ambiguous sexual content, contextual intent, reclaimed slur usage ("my nigga"), and educational sexual content. These document the annotation boundary conditions.
- **Preprocessing validation**: Stop-word removal and stemming tested but caused 0.5% accuracy and F1 drop; final system omits them.

## 7. Saturation / discrimination
FinBERT achieves 91.7% accuracy and 90.8% F1, with CNN+FinBERT close behind at 91.3%/90.0%. mBERT substantially underperforms (88.2%/85.3%), demonstrating that the Finnish-specific pre-training provides meaningful discrimination gain. Non-deep-learning models cluster at 81–83% accuracy, showing clear deep-learning advantage. FastText standalone is the weakest at 59.5% accuracy / 56.4% F1, far below all other approaches. Dataset is not yet saturated, but close to the ceiling achievable given binary labels and no per-category fine-grained classification.

## 8. Multiturn / agentic aspects
n/a. Single-turn binary classification.

## 9. Key numbers
- 10,700 total sentences; 1,786 hate (16.7%), 8,914 non-hate (83.3%) (p.2, Table 1)
- 122,823 total tokens; vocabulary size 23,430 (p.2, Table 1)
- 197 total disagreements between two annotators (p.2)
- Krippendorff's α=0.92 inter-annotator agreement (p.3)
- FinBERT (bert-base-finnish-uncased-v1): accuracy 91.7%, F1 90.8% (p.5, Table 4)
- CNN+FinBERT embedding: accuracy 91.3%, F1 90.0% (p.5, Table 4)
- mBERT: accuracy 88.2%, F1 85.3% (p.5, Table 4)
- CNN+fastText: accuracy 90.0%, F1 89.7% (p.5, Table 4)
- RF+Char Level TF-IDF: accuracy 83.0%, F1 77.0% (best non-deep learning) (p.5, Table 4)
- fastText standalone: accuracy 59.5%, F1 56.4% (worst) (p.5, Table 4)
- Train/val/test: 6,700/1,000/3,000 (p.4)
- FinBERT pre-trained on >3 billion tokens of Finnish text (p.3)
- mBERT covers 102 languages; Finnish Wikipedia is ~3% of its training data (p.3)

## 10. Pitfalls & limitations
- Dataset is sourced from a single Finnish forum (Suomi24) covering 2001–2017; may not generalize to current Finnish online discourse or other platforms.
- Profane-word seeding for hate-class oversampling introduces selection bias toward explicit, keyword-visible hate speech; implicit hate may be underrepresented.
- Binary label scheme collapses five distinct hate categories (racism, sexual, xenophobia, religious, homophobia); category-level performance is not evaluated.
- Class imbalance (83.3% non-hate): aggregate accuracy and F1 metrics may overstate practical usefulness for hate class detection specifically.
- No per-class precision/recall breakdown reported for the hate class.
- Annotators are reported as not receiving remuneration, but their institutional affiliation and country context are the same (University of Oulu), limiting perspective diversity.
- The paper cannot be compared to prior Finnish work because no comparable Finnish HS dataset previously existed.

## 11. Novel ideas worth stealing
1. **Language-specific pretraining gap measurement.** The FinBERT vs. mBERT comparison (3.5–5% accuracy/F1 gap) quantifies the cost of using a multilingual model for a low-resource language. Any benchmark targeting non-English populations should include language-specific baseline comparisons to measure the multilingual model penalty.
2. **Profane-word seeding + random sampling hybrid.** Combining profane-word keyword filtering (to oversample hate) with random sampling (to maintain realistic non-hate proportion) is a pragmatic construction strategy for rare-class text datasets that produces a realistic class distribution rather than an artificially balanced one.
3. **Five-category hate taxonomy as a filter.** Defining five hate speech categories (racism, sexual, xenophobia, religious intolerance, homophobia) as the annotation scope provides a principled and reproducible construction filter while retaining a binary evaluation label. This taxonomy structure could be adopted for values-alignment benchmark design to ensure comprehensive category coverage.
4. **Expert referee three-annotator system.** The two-annotator + expert-referee-for-disagreements protocol is a cost-efficient alternative to full three-annotator designs while still resolving ambiguous cases with domain expertise.
5. **Annotation boundary documentation.** The four edge-case examples discussing the annotation decision boundary (ambiguous sexual content, contextual intent, reclaimed slurs, educational sexual discussion) serve as a concrete annotation guide and benchmark validity documentation. Any benchmark should include analogous boundary case documentation.

## 12. Notable quotes
- "There is a lack of hate speech datasets compared to English, and a multilingual pre-trained model often contains fewer tokens for other languages." (p.1)
- "A sentence is considered a hate if it satisfies the following criteria: deliberate attack directed towards a specific group of people or organization employing sexual attack, curse, defamation, threat, gender, ethnicity, and identity." (p.3)
- "The presence or absence of offensive words in a sentence cannot systematically be considered sufficient evidence to confirm the existence of hate or not-hate." (p.3)
- "FinBERT yields a 91.7% accuracy and 90.8% F1 score value, which outperforms all state-of-art models, including multilingual-BERT and CNN." (p.1)

## 13. UNKNOWN / not in extract
- Per-class precision/recall/F1 specifically for the hate class.
- Distribution of the five hate categories within the 1,786 hate sentences.
- Whether the test set was drawn from the same time period and forum subdomains as the training set (potential temporal leakage risk given 2001–2017 span).
- Error analysis or confusion matrix for any of the classifiers.
- Whether the dataset annotations are publicly released alongside the code, or only the code.
