---
stem: "2024-Aly-Hate speech detection with ADHAR a multi-dialectal hate speech corpus"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, design-space]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 4240
dataset_construction: "crowdsourced"
languages: ["ar"]
models_tested: ["AraBERT", "SVM", "Logistic Regression", "Random Forest", "Decision Tree", "MLP", "CNN-BiLSTM"]
headline_numbers:
  - "AraBERT achieves 94% accuracy and 94% macro F1 for hate/not-hate detection (p.9)"
  - "AraBERT achieves 95% accuracy and 95% macro F1 for category detection (p.9)"
  - "MLP with char n-grams achieves 90% accuracy for binary hate detection (p.9)"
  - "Cohen's Kappa inter-annotator agreement: 0.9489 overall (p.7)"
  - "Cross-dialect accuracy ranges from 0.64 to 0.84 (p.8)"
  - "ADHAR contains 4,240 tweets and 70,369 words across 5 Arabic variants (p.4)"
---

## 1. Gist
ADHAR (Arabic Dataset for Hate And Racism) is a carefully balanced multi-dialectal Arabic hate speech corpus covering five language variants (MSA, Egyptian, Jordanian/Palestinian, Gulf, and Maghrebi) and four hate speech categories (nationality, religion, ethnicity, race). The paper's primary contribution is rigorous data balance: each dialect-category combination contains ~100 hate and ~100 non-hate tweets, enabling unbiased classifier training. With Cohen's Kappa above 0.92 for all categories, the annotation quality is high. The cross-dialect experiment — training on one dialect and testing on another — reveals significant performance drops (as low as 0.64 accuracy), demonstrating why dialect-tagged, balanced corpora are essential for Arabic content moderation. For values-alignment benchmarking, ADHAR is a model case study of how to build a culturally grounded harmful-language dataset that respects intra-language diversity.

## 2. Benchmark/eval design features
**Constructs measured**: Hate speech (binary: Hate / Not Hate) and hate speech category (nationality, religious beliefs, ethnicity, race).
**Item structure**: Single tweet in Arabic (one of five dialect variants), annotated with hate/not-hate label and category label.
**Answer space**: Binary classification (hate/not-hate); 4-class classification (category); dialect label appended as input feature.
**Balance design**: ≥1,000 tweets per category; ≥500 hate / ≥500 non-hate per category; ≥200 tweets per dialect-category combination; 100 hate + 100 non-hate per dialect-category cell.
**Annotation protocol**: Three-stage process — initial annotation by dialect-expert annotator, second blind annotation, adjudication meeting for disagreements. Ambiguous tweets removed from corpus.

## 3. Task format & example item
Forced-choice (binary classification or 4-class category assignment). Example items (translated, p.5):

- Nationality / Egyptian: "You dirty Algerian go clean your country from immorality and indecency then talk about the Kingdom" — Label: Hate
- Religious beliefs / Jordanian-Palestinian: "Oh God, how stupid Jews are" — Label: Hate
- Ethnicity / Maghrebi: "They are not Arabs, but Berbers. We are not honored to be their neighbors at all" — Label: Hate
- Race / Gulf: "Asians are disgusting, they make you vomit when you see them, they are the dirtiest and the most disgusting" — Label: Hate

## 4. Scoring / grading methodology
Binary classification evaluated via accuracy, precision, recall, and F1-score (micro). Feature sets tested: character n-grams (2–5), word n-grams (1–3), TF-IDF, and word embeddings (dim=300). Models: SVM, Logistic Regression, Random Forest, Decision Tree, MLP (best classical), CNN-BiLSTM (deep learning), and AraBERT (transformer). Train/test split: 75:25. Hyperparameter tuning on separate validation set (not test data). Best classical model: MLP with character n-grams (90% acc, 90% F1 for binary; 92% acc, 92% F1 for category). Best overall: AraBERT (94% acc/F1 binary; 95% acc/F1 category).

## 5. Dataset construction & provenance
4,240 tweets collected from Twitter using seed keywords (10–20 per dialect-category combination). Seeds included dialect-specific hate slurs combined with category-relevant neutral terms to collect both hate and non-hate tweets. Each tweet had to: (1) be in Arabic with correct spelling, (2) directly relate to one of the four categories, and (3) express clear hatred/non-hatred. Three native-Arabic-speaking annotators from the research team. Annotation: multi-stage with inter-annotator agreement via Cohen's Kappa (0.9489 overall; lowest 0.9257 for Race/Ethnicity). Dataset publicly available (CC BY license, Frontiers). Maghrebi sub-dialect breakdown provided (Moroccan, Tunisian, Algerian, Libyan, Generic), showing the finest granularity of any existing Arabic hate speech corpus.

## 6. Validity evidence
- Inter-annotator agreement: Cohen's Kappa = 0.9636 (Nationality), 0.9605 (Religious beliefs), 0.9257 (Race/Ethnicity), 0.9489 (Overall) — all in the "almost perfect" range (p.7).
- Cross-dialect generalization experiment: MLP trained on one dialect variant and tested on another; accuracy ranges 0.64–0.84, demonstrating genuine dialect-driven variance rather than artifact (p.8).
- AraBERT results contextualized against MLP baseline, showing consistent gains from contextual representations.
- Comparison against six prior Arabic hate speech datasets provided (Table 1), locating ADHAR in the literature.

## 7. Saturation / discrimination
AraBERT achieves 94–95% accuracy, suggesting the task is close to saturation for trained classifiers on this dataset. The class-balanced design prevents trivial majority-class inflation of scores. Cross-dialect generalization (0.64–0.84) shows significant discrimination headroom at the dialect transfer level — a harder, more realistic evaluation setting. The balanced design (50/50 hate/non-hate) makes the task harder than typical imbalanced corpora where most prior datasets were ~65–80% non-hate.

## 8. Multiturn / agentic aspects
n/a — single tweet classification; no multi-turn or agentic setup.

## 9. Key numbers
- Total: 4,240 tweets, 70,369 words (p.4)
- Per category: Nationality 1,090; Religious beliefs 1,050; Ethnicity 1,061; Race 1,035 (p.5)
- Per dialect (nationality category): MSA 225; Egyptian 203; Jordanian/Palestinian 244; Gulf 208; Maghrebi 210 (p.7)
- Annotation agreement: κ=0.9489 overall; κ=0.9636 nationality; κ=0.9257 race/ethnicity (p.7)
- Cross-dialect range: 0.64 (Egyptian train → Gulf test) to 0.84 (Gulf train → Levantine test) (p.8)
- MLP char n-grams: 90% acc binary, 92% acc category (p.9)
- AraBERT: 94% acc/F1 binary; 95% acc/F1 category (p.9)
- Maghrebi sub-component: 840 entries, ~20% of dataset (p.5)

## 10. Pitfalls & limitations
- Only 4,240 tweets total is modest; each dialect-category cell has only ~200 examples, limiting generalization.
- Only five of many Arabic dialects are covered; Iraqi, Sudanese, Yemeni, and others are absent.
- Static dataset — no mechanism for updating as new hate speech patterns emerge online.
- Annotation pool of three team members introduces potential shared biases and lacks external validation.
- Seed-keyword collection method biases toward explicit slur-based hate speech; subtle or implicit hate may be underrepresented.
- Generalizability across different Arabic-speaking contexts not tested (models trained on Twitter content only).
- The paper does not test zero-shot or few-shot LLM performance (GPT-4, etc.) on ADHAR, leaving its utility as an LLM evaluation benchmark unquantified.
- Only binary and 4-class labeling; no severity gradation (mild stereotyping vs. incitement).

## 11. Novel ideas worth stealing
1. **Dialect × category × class 3-way balance**: The requirement that each (dialect, category, hate/not-hate) cell has ≥100 examples is a powerful constraint that prevents structural confounds. Values-alignment benchmarks in multilingual/multicultural settings should adopt analogous cell-balance requirements.
2. **Cross-condition transfer experiment as hardness measure**: Training on one dialect and testing on another immediately reveals whether a model has learned dialect-neutral hate patterns vs. memorized dialect-specific slurs — a template for cultural-transfer probing in values benchmarks.
3. **Dialect annotation as a first-class feature**: Tagging each item with its dialect/variant and using dialect as an input feature is a generalizable design principle for any culturally heterogeneous benchmark.
4. **Seed keyword design with dialect-specific slur lists**: The methodology of gathering 10–20 seed keywords per (dialect, category) combination, including neutral words + slurs, is a reproducible recipe for collecting representative, hard-negative pairs.
5. **Staged annotation with adjudication**: The three-stage annotation (first annotation → blind second annotation → meeting for disagreements) is more expensive than majority vote but produces higher inter-rater agreement and forces explicit rationale formation.

## 12. Notable quotes
- "Arabic dialects vary significantly, and some words can even have different meanings depending on the dialect. Certain words that may be considered normal or safe in one dialect could be perceived as offensive in another." (p.2)
- "For all categories the values are above 0.9, which reflects a high level of agreement." (p.7, on Cohen's Kappa)
- "The lowest accuracy of 0.64 was observed when training the model on tweets in the Egyptian dialect and testing it on Gulf tweets." (p.8)
- "Our dataset is the first to prioritize a balanced distribution among MSA and different Arabic dialects." (p.10)

## 13. UNKNOWN / not in extract
- Exact train/validation/test split sizes are not provided (only the 75:25 ratio).
- License terms for the ADHAR dataset are not stated in the extract.
- No LLM-as-evaluator or GPT-4 zero-shot baseline is reported.
- IAA for specific dialect pairs (not just overall categories) is not provided.
- Number of seed keywords per category/dialect is given as a range (10–20) but no full keyword list is in the extract.
