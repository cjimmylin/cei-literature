---
stem: "2024-Kajiwara-Multiclass hate speech detection with an aggregated dataset Natural"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [design-space, validity-psychometrics, normative-ethics]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 9004
dataset_construction: "mixed"
languages: ["en"]
models_tested: ["Logistic Regression", "LSTM", "BERT (base uncased)", "GPT-2 (124M)"]
headline_numbers:
  - "Final aggregated dataset: 9,004 tweets across 5 classes (p.8)"
  - "Best model (fine-tuned BERT) F1: 0.7593 on multiclass task (p.13)"
  - "GPT-2 multiclass F1: 0.7220; binary classification F1: 0.7659 (p.13)"
  - "LSTM multiclass F1: 0.7423; Logistic Regression F1: 0.7391 (p.13)"
  - "20% training data subset F1: 0.3419; full dataset F1: 0.7220 for GPT-2 (p.14)"
  - "Sexuality class: highest classification performance despite lowest data count (p.12)"
---
## 1. Gist
This 2025 paper (Walsh & Greaney, Natural Language Processing journal) aggregates and re-annotates four existing hate speech datasets to create a multi-class corpus of 9,004 tweets labeled across five categories: ethnicity, gender, religion, sexuality, and non-hate. The authors evaluate logistic regression, LSTM (with systematic NLP feature selection), BERT, and GPT-2 on this multiclass task. Key findings: (1) larger/more complex models yield only marginal improvements; (2) dataset size matters much more than model complexity; (3) the "non-hate" class is hardest to distinguish from hate classes. For values-alignment benchmarking, the paper provides a useful methodology for dataset aggregation from heterogeneous sources, analysis of the effect of dataset size on model performance, and multiclass classification across protected characteristics—all directly relevant to building diverse values-alignment evaluation corpora.

## 2. Benchmark/eval design features
Five-class classification task: ethnicity, gender, religion, sexuality, non-hate. Dataset aggregated from four sources: Waseem (2016), Berkeley Measuring Hate Speech (Kennedy et al. 2020), HateXplain (Mathew et al. 2021), Large-scale hate speech dataset (Toraman et al. 2022). Re-labeling scheme maps original labels to a unified taxonomy. Class balancing: non-hate tweets balanced within each source before integration to avoid the model learning topic-specific keywords. Features evaluated for LSTM: word n-grams, character n-grams, dependency tuples, POS tags, NER tags, sentiment scores (VADER). Best LSTM feature set: word n-grams + character n-grams + dependency tuples. Data split: 80% train, 10% validation, 10% test via stratified sampling. Binary classification comparison also performed.

## 3. Task format & example item
Five-class tweet classification: 0=non-hate, 1=ethnicity, 2=gender, 3=religion, 4=sexuality.

No specific example tweets are provided in the extract (hate speech content has been cleaned and preprocessed—hashtags, mentions, URLs, emojis removed). Example of the relabeling process: Waseem (2016) "racism" label → "ethnicity"; "sexism" → "gender"; "neither" → "non-hate."

## 4. Scoring / grading methodology
Primary metrics: accuracy, macro-averaged precision, recall, F1 score. Feature selection for LSTM: greedy forward selection based on maximum validation accuracy over 15 epochs. Model tuning: grid search over LSTM layers (1/2/3), layer width (16/32/64/128/256), dropout probability (0.1–0.8), learning rate (1e-4/1e-3/1e-2). BERT and GPT-2 fine-tuned from pre-trained weights. Dataset size effect studied by fine-tuning GPT-2 on 20%, 40%, 60%, 80%, 100% data subsets. Confusion matrices provided per class.

## 5. Dataset construction & provenance
Four sources aggregated:
1. **Waseem (2016)**: 5,580 non-hate + 891 gender tweets (racism tweets removed due to hashtag-dependency); balanced to 891+891 = 1,783 total
2. **Berkeley Measuring Hate Speech (Kennedy et al. 2020)**: Twitter/YouTube/Reddit hate data with continuous hate scores; tweets only kept, score ≥0.5 = hate; total 5,443 tweets
3. **HateXplain (Mathew et al. 2021)**: Gab + Twitter, crowd-annotated via AMT; 679 tweets retained after filtering
4. **Large-scale hate speech v2 (Toraman et al. 2022)**: English tweets only, >80% annotator agreement, Turkish/sports/politics removed; 1,099 tweets

Final combined dataset (before cleaning): 9,004 tweets—2,347 gender, 2,015 ethnicity, 1,132 religion, 1,028 sexuality, 2,482 non-hate. After cleaning (remove user mentions, URLs, hashtags, emojis, contractions expanded, duplicates removed): 80/10/10 split → 7,511 train, 939 validation, 939 test.

Note: The combined dataset cannot be published due to redistribution restrictions on some source datasets.

## 6. Validity evidence
Dataset validity: four diverse source datasets with different annotation methodologies combined, which introduces definitional inconsistency but is acknowledged as a limitation. Berkeley dataset uses continuous hate scores (Rasch IRT) converted to binary via threshold; threshold choice (0.5) not empirically validated. HateXplain uses majority vote of AMT workers. Inter-rater agreement of source datasets not reported. Model cross-validation: binary vs. multiclass comparison shows multiclass F1 is competitive (0.7220 GPT-2 multiclass vs. 0.7659 binary), suggesting meaningful signal retained in fine-grained categories.

## 7. Saturation / discrimination
No saturation concerns—performance plateaus around 0.75 F1 for the best models. Dataset size has a dramatic effect: 20% subset gives F1=0.34, 100% gives F1=0.72 for GPT-2—suggesting the benchmark discriminates strongly across model-data combinations. The sexuality class achieves highest classification performance (only 12% incorrect) despite smallest class size, likely due to distinctive lexical patterns. The non-hate class has worst performance (41% incorrect), primarily confused with gender and ethnicity classes.

## 8. Multiturn / agentic aspects
Not applicable. Single-tweet binary/multiclass classification.

## 9. Key numbers
- Total dataset: 9,004 tweets (Table 1, p.7)
- Class distribution: ethnicity 2,015, gender 2,347, religion 1,132, sexuality 1,028, non-hate 2,482 (Table 1, p.7)
- Train/validation/test split: 7,511/939/939 (p.8)
- Source dataset contributions: Berkeley 60.5%, HateXplain 7.5% (p.8)
- LSTM optimal config: 1 layer, 128 nodes, dropout 0.8, LR 1e-2 (Table 3, p.12)
- LSTM feature selection: word n-grams 0.6994 → +char n-grams 0.7091 → +dependency tuples 0.7112 (Table 2, p.12)
- LSTM test metrics: accuracy 0.7188, precision 0.7297, recall 0.7447, F1 0.7423 (Table 4, p.13)
- Model F1 comparison: LR 0.7391, LSTM 0.7423, BERT 0.7593, GPT-2 0.7220 (Table 5, p.13)
- Binary GPT-2 F1: 0.7659 (unbalanced) vs. 0.7627 (balanced) (p.13)
- Dataset size effect (GPT-2 F1): 20%→0.3419, 40%→0.5795, 60%→0.6520, 80%→0.6888, 100%→0.7220 (Table 6, p.14)
- Non-hate class: 41% incorrect predictions; sexuality: 12% incorrect (p.12)
- Waseem (2016) best LR F1: 0.7389; Gambäck & Sikdar CNN+Word2Vec F1: 0.7829 (p.3–4)

## 10. Pitfalls & limitations
- Different annotation standards across four source datasets; relabeling involves judgment calls that may introduce noise
- Removal of context (hashtags, mentions) during preprocessing may remove hate-signal information
- Berkeley dataset threshold choice (≥0.5 = hate) is arbitrary and not empirically validated
- Combined dataset cannot be redistributed for replication
- Twitter API unavailability prevented use of many published datasets with tweet IDs only
- Class imbalance remains (religion and sexuality underrepresented) despite within-source balancing
- Duplicate retention for minority classes (religion, sexuality) acts as implicit oversampling—not ideal
- Removing 93 racism tweets whose hateful content relied entirely on hashtags may have biased training data
- GPT-2 binary outperforms GPT-2 multiclass, suggesting multiclass task loses information—this trade-off is not fully resolved

## 11. Novel ideas worth stealing
1. **Cross-dataset aggregation with unified relabeling**: The methodology for combining multiple hate speech datasets with heterogeneous label schemes into a single unified taxonomy (ethnicity/gender/religion/sexuality/non-hate) is a replicable template for building large-scale, diverse evaluation corpora across multiple dimensions of values-alignment.
2. **Source-aware balancing before integration**: Balancing non-hate examples within each source dataset before integration prevents any single source's topic distribution from dominating the non-hate class—relevant for any multi-source benchmark construction.
3. **Dataset size ablation as benchmark validation**: Testing models on 20%/40%/60%/80%/100% data subsets reveals the steepness of the learning curve and whether performance is data-limited or model-limited—a useful diagnostic for newly constructed benchmarks.
4. **Dependency tuple features for hate detection**: Syntactic dependency head-word–relationship tuples (beyond word and character n-grams) improve classification performance, suggesting structural patterns in hate speech that could inform feature engineering for values-alignment classifiers.
5. **Multi-class vs. binary comparison**: Including a binary classification comparison (hate vs. non-hate) alongside the fine-grained multiclass task allows direct measurement of information lost/gained by granularity—relevant when deciding how many categories to include in a values benchmark.

## 12. Notable quotes
- "We show that while more recent larger models can achieve a slightly higher performance, increased model complexity alone is not sufﬁcient to achieve signiﬁcantly improved models." (p.1)
- "Although the dataset presented here was compiled with varying deﬁnitions of hate speech, the models trained on it have achieved a classiﬁcation performance that is comparable with similar studies." (p.13)
- "Taken together with the results of the models trained on data subsets, this suggests that the availability of further data could lead to improved performance." (p.13)
- "One of the principal advantages of our approach is that it is capable of classifying hate towards four protected characteristics, with comparable performance, compared to either binary hate vs non-hate classiﬁcation." (p.14)

## 13. UNKNOWN / not in extract
- Full confusion matrices for all models (referenced as Figures 2–4 but not fully extractable from text)
- Statistical significance tests for F1 score differences between models
- Exact text of example tweets used in training/testing (appropriately not disclosed)
- Whether the combined dataset has been made available at any repository
- Inter-annotator agreement values for the source datasets
- Runtime and computational requirements for training each model
