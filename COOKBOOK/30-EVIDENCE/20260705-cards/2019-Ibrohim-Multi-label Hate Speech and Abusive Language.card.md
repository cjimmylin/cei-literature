---
stem: "2019-Ibrohim-Multi-label Hate Speech and Abusive Language"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [design-space, validity-psychometrics, cultural-linguistic, normative-ethics]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 13169
dataset_construction: "crowdsourced"
languages: ["id"]
models_tested: ["SVM", "Naive Bayes", "Random Forest Decision Tree (RFDT)", "Binary Relevance", "Label Power-set", "Classifier Chains"]
headline_numbers:
  - "13,169 total tweets; 5,561 hate speech tweets; 7,608 not-hate-speech tweets (p.5)"
  - "Best accuracy without target/category/level detection: 77.36% (RFDT + LP + word unigram) (p.8)"
  - "Best accuracy with target/category/level detection: 66.12% (RFDT + LP + word unigram) (p.7)"
  - "First annotation phase: 11,292 of 16,500 tweets reached 100% agreement (68.44%) (p.5)"
  - "30 annotators from diverse religious, ethnic, and demographic backgrounds (p.5)"
---
## 1. Gist
Ibrohim and Budi (2019, Universitas Indonesia) build and evaluate a multi-label Indonesian Twitter dataset for hate speech and abusive language detection that goes beyond binary hate/not-hate classification. The dataset distinguishes hate speech from abusive-but-not-hate content, and for hate speech instances further annotates target (individual vs. group), category (religion, race/ethnicity, physical/disability, gender/sexual orientation, other invective), and severity level (weak, moderate, strong). The annotation framework was co-developed with Indonesia's cybercrime police (Bareskrim Polri) and a linguist, grounding label definitions in legal/jurisdictional context. This paper matters for values-alignment benchmarking as a rare Indonesian-language resource with fine-grained, operationally-grounded hate speech ontology and a practical demonstration of multi-label classification challenges for complex social harm taxonomies.

## 2. Benchmark/eval design features
- **Multi-label schema**: Each tweet receives labels for: (1) hate speech / abusive / neither; (2) if hate speech → target (individual/group); (3) hate speech category (religion/creed, race/ethnicity, physical/disability, gender/sexual orientation, other invective/slander); (4) hate speech level (weak/moderate/strong).
- **Two annotation phases**: Phase 1 (binary HS detection, 30 annotators, 100% agreement threshold); Phase 2 (target/category/level, top-3 annotators from Phase 1, majority vote).
- **Annotator diversity**: 30 annotators from different religions (Islam, Christian, Catholic, Hindu, Buddha), ethnicities (Java, Bali, Tionghoa, Betawi, Batak, others), ages 20–32, mixed job types. (p.5)
- **Classifiers**: SVM, NB, RFDT with Binary Relevance (BR), Label Power-set (LP), Classifier Chains (CC) transformation methods.
- **Features**: Word n-grams (unigram, bigrams, trigrams), character n-grams (trigrams, quadgrams), orthography (exclamation mark, question mark, uppercase/lowercase), sentiment lexicon (positive/negative) + abusive lexicon.

## 3. Task format & example item
Multi-label text classification. Appendix 1 (p.11) shows example annotation query words used for crawling:
> Query: "anjing" (dog, abusive word)
> Query: "banci" (abusive word related to gender/sexual orientation)
> Query: "kafir" (abusive word related to religion/creed)
> Query: "cina" (word related to hate speech in politics and race/ethnicity)

No verbatim annotated tweet example is given in the extract, but the annotation schema asks annotators to label whether a tweet is: (a) hate speech and abusive, (b) hate speech but not abusive, (c) abusive but not hate speech, (d) neither. If hate speech, then target, category, and level are additionally labeled.

## 4. Scoring / grading methodology
- Multi-label accuracy computed as:
  Accuracy = (1/D) Σ (|Ŷ(i) ∩ Y(i)| / |Ŷ(i) ∪ Y(i)|) × 100% (p.7)
- 10-fold cross-validation throughout.
- Best Scenario 1 (with target/category/level): 66.12% accuracy (RFDT + LP + word unigram). (p.7)
- Best Scenario 2 (without target/category/level): 77.36% accuracy (RFDT + LP + combination features). (p.8)

## 5. Dataset construction & provenance
- Initial tweets: 16,500 collected from Phase 1 crawl (March–September 2018) + data from prior Indonesian studies (Alfina et al. 2017, 2018; Putri, 2018; Ibrohim & Budi, 2018). (p.4)
- Phase 1 (binary HS annotation): 11,292 of 16,500 tweets with 100% annotator agreement = reliable data (6,187 not-HS, 5,105 HS). (p.5)
- Phase 2 (target/category/level): 5,700 HS tweets annotated; 139 deleted for no majority agreement → 5,561 reliable HS tweets. (p.5)
- Final dataset: 13,169 tweets (7,608 not-HS + 5,561 HS). (p.5)
- HS category breakdown: religion/creed 793, race/ethnicity 566, physical/disability 323, gender/sexual orientation 306, other invective/slander 3,740. (p.6)
- Severity: weak 3,383, moderate 1,705, strong 473. (p.6)
- Publicly available on GitHub. (p.3)
- Crawl queries listed in Appendix 1 (31 queries covering abusive words, political hate speech terms, religious slurs, ethnic terms). (p.11–12)

## 6. Validity evidence
- Phase 1: 68.44% of annotated tweets reached 100% agreement across 3 annotators; cited as "good level of agreement" per McHugh (2012). (p.5)
- Phase 2: 97.56% reliability (majority agreement); cited as "almost perfect level of agreement." (p.5)
- No Cohen's Kappa or Fleiss's Kappa values explicitly computed or reported.
- Annotator selection was standardized with gold standard annotation tests and guideline training before production annotation. (p.4)
- Co-developed with cybercrime police (Bareskrim Polri) and a linguist to ground definitions in legal/operational context — adds external validity. (p.3)

## 7. Saturation / discrimination
- Category imbalance is severe: "other invective/slander" = 3,740 tweets (67%) vs. gender/sexual orientation = 306 (5.5%). The dominant category dominates classification difficulty.
- Severity imbalance: strong hate speech = 473 instances (8.5% of HS tweets) — likely under-represented and hardest to classify.
- Error analysis shows false negatives dominate, attributed to class imbalance. (p.8)
- Accuracy gap between Scenario 1 (66.12%) and Scenario 2 (77.36%) demonstrates that adding target/category/level labels substantially increases difficulty.
- Combining features does not significantly improve over word unigram alone in Scenario 1 (65.73% combined vs. 66.12% unigram). (p.8)

## 8. Multiturn / agentic aspects
n/a — single-tweet classification.

## 9. Key numbers
- 13,169 total annotated tweets (p.5)
- 5,561 hate speech tweets; 7,608 not hate speech (p.5)
- 30 annotators from diverse backgrounds (p.5)
- 100% agreement rate in Phase 1: 68.44%; majority agreement rate in Phase 2: 97.56% (p.5)
- Best Scenario 1 accuracy: 66.12% (RFDT + LP + word unigram) (p.7)
- Best Scenario 2 accuracy: 77.36% (RFDT + LP + word unigram + char quadgrams + lexicon) (p.8)
- Strong hate speech: 473 tweets; Moderate: 1,705; Weak: 3,383 (p.6)
- Category "other invective/slander": 3,740 of 5,561 HS tweets (p.6)

## 10. Pitfalls & limitations
- No Kappa statistics for inter-annotator agreement; "100% agreement" threshold in Phase 1 discards 31.6% of data, which may bias retained data toward clearer cases.
- Severe category imbalance (invective/slander dominates) likely degrades performance for rare categories.
- Only 3 annotators per tweet in Phase 1; majority vote with just 3 annotators provides limited robustness.
- Dataset covers only tweets from 7-month crawl; limited temporal and domain diversity.
- Evaluation metric (Jaccard-based multi-label accuracy) is sensitive to label set size and may not reflect practical precision/recall tradeoffs.
- No deep learning baselines (LSTM/BERT) — the "best" model is classical ML; results may not reflect current state of the art.
- Indonesian language specificity: abusive lexicons and text normalization dictionaries are manually constructed, may not generalize across dialects or time.
- Phase 2 best 3 annotators selected from Phase 1 may introduce self-selection bias; no verification of their representativeness.

## 11. Novel ideas worth stealing
1. **Government/legal authority partnership for label grounding**: Co-designing annotation categories with law enforcement (Bareskrim Polri) anchors label definitions in real-world enforcement criteria — operationally grounding what counts as "strong" vs. "weak" hate speech. For values-alignment benchmarks, partnering with domain authorities (legal scholars, ethicists, policy makers) to ground severity tiers adds external validity.
2. **Two-phase annotation pipeline**: Separate a coarse binary annotation phase (cheap, crowd) from a fine-grained phase (expensive, expert), applied only to the positive class. This efficiency design is directly reusable for any benchmark where harmful content is rare and fine-grained labels are costly.
3. **100% agreement filter for ground truth**: Using only tweets where all annotators agree creates a high-quality "gold" subset even if inter-rater reliability is overall moderate. Useful for evaluation sets where label noise is especially damaging.
4. **Multi-dimensional harm ontology (target × category × severity)**: The three-way annotation schema (who is targeted, why, and how severely) is more actionable than binary labels for content moderation prioritization — a model for values-alignment benchmarks that want to distinguish severity tiers or targeting types.
5. **Diverse annotator pool by religion/ethnicity**: Explicitly recruiting annotators from different religious and ethnic backgrounds to reduce annotation bias on hate speech is a best practice that should be standard for any dataset touching intergroup relations.

## 12. Notable quotes
- "Hate speech and abusive language spreading on social media need to be detected automatically to avoid conflicts between citizens. Moreover, hate speech has a target, category, and level that also need to be detected to help the authority in prioritizing which hate speech must be addressed immediately." (p.1)
- "Annotators came from different religious, racial/ethnic, and residential backgrounds. This is done to reduce bias because the annotation of hate speech is quite subjective." (p.5)
- "Although abusive language are sometimes just being used as jokes (not to offend someone), the use of abusive language in social media still can lead to conflict because of misunderstandings among netizens." (p.1)
- "Handling hate speech problem in social media is not just about identifying whether a text/document is hate speech or not. There are several other tasks which needs to done to help the authorities in handling hate speech problems such as the identification of buzzers, thread starters, and fake account spreaders of hate speech." (p.9)

## 13. UNKNOWN / not in extract
- Cohen's Kappa or Fleiss's Kappa for any annotation phase.
- Exact number of tweets contributed by each prior dataset source vs. new crawling.
- Model performance broken down by hate speech category or severity level.
- Whether the GitHub dataset release is still active and what license applies.
- Performance of deep learning models (LSTM, BERT) — not evaluated in this paper.
- Demographic breakdown of tweet authors.
