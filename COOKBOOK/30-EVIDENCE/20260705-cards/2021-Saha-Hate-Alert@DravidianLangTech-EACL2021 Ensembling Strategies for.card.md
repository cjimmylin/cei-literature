---
stem: "2021-Saha-Hate-Alert@DravidianLangTech-EACL2021 Ensembling Strategies for"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, best-practices]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 71938
dataset_construction: "scraped"
languages: ["ta", "kn", "ml", "en"]
models_tested: ["XLM-RoBERTa-base", "XLM-RoBERTa-large", "mBERT", "IndicBERT", "MuRIL", "DistilBERT", "CNN"]
headline_numbers: ["1st place Tamil weighted F1 0.78 (p.4)", "1st place Malayalam weighted F1 0.97 (p.4)", "2nd place Kannada weighted F1 0.74 (p.4)", "OOV rate 85.55% Tamil, 84.23% Malayalam, 83.03% Kannada (p.3)", "XLM-RoBERTa seed variation 15-20% (p.5)"]
---
## 1. Gist
This paper describes the IIT Kharagpur team's (Hate-Alert) system submission to the shared task on Offensive Language Identification in Dravidian Languages at EACL 2021. The team achieved first place in Tamil and Malayalam subtasks and second place in Kannada. Their approach exhaustively evaluates multilingual transformer models (XLM-RoBERTa, mBERT, IndicBERT, MuRIL, DistilBERT), a BERT-CNN fusion architecture, and a genetic algorithm (GA)-based ensemble weighting strategy. The key finding is that GA-optimized weighted ensembling provides a consistent 1–2% F1 improvement over individual models, and that XLM-RoBERTa models exhibit high variance (15–20%) across random seeds while mBERT is more stable (2–3%). The work is relevant to values-alignment benchmarking primarily as a demonstration of the difficulty of low-resource, code-mixed offensive language detection and as a methodological reference for ensemble strategies.

## 2. Benchmark/eval design features
This is a system paper (shared task submission), not a benchmark paper. The benchmark itself is the DravidianLangTech-EACL2021 dataset (Chakravarthi et al., 2021).

**Task**: Multi-class classification of YouTube comments as: not-offensive, offensive-untargeted, offensive-targeted-individual, offensive-targeted-group, offensive-targeted-other, or not-in-intended-language. Malayalam has 5 classes (no offensive-targeted-other).

**Dataset**: Tamil (35,139 train / 4,388 dev / 4,392 test), Kannada (6,217 / 777 / 778), Malayalam (16,010 / 1,999 / 2,001). Total ~71,938 instances across splits (p.2).

**Evaluation metric**: Weighted F1-score on held-out test set.

**Core claims**:
1. XLM-RoBERTa-large is the best single model for Tamil; custom-pretrained XLM-RoBERTa-base (further pretrained on target data with MLM) is best for Kannada.
2. GA-based ensemble weighting outperforms standard prediction averaging.
3. Random seed variance is much higher for XLM-RoBERTa (15–20%) than mBERT (2–3%).
4. IndicBERT and MuRIL (Indian-specific models) underperform XLM-RoBERTa despite being trained on Indian languages.

## 3. Task format & example item
Multi-class classification. No verbatim example items provided in the extract (the paper references example comments as offensive content but does not quote them). The task is illustrated by Table 1 showing dataset statistics per label and split (p.2).

## 4. Scoring / grading methodology
Weighted F1-score (weighted by class frequency). Early stopping on macro-F1 of development split (5 epochs patience). Adam optimizer with learning rate 1e-5. Unweighted and weighted cross-entropy loss both explored per model. 3-fold cross-validation not used; standard train/dev/test split.

## 5. Dataset construction & provenance
- YouTube comments scraped from multilingual Dravidian community channels where code-mixing is prevalent (Chakravarthi et al., 2020a, 2020b; Hande et al., 2020).
- Labels: 6 offensive categories (5 for Malayalam).
- OOV rate compared to Dakshina dataset pure-language vocabulary: 85.55% Tamil, 84.23% Malayalam, 83.03% Kannada (p.3) — indicating extreme code-mixing and transliteration.
- Dataset not released by the authors of this paper; they use the shared task organizers' dataset.

## 6. Validity evidence
- Task is a competitive shared task with leaderboard validation; team finished 1st/2nd.
- No human baseline performance reported.
- No inter-annotator reliability reported in this paper (would be in the shared task description paper).
- Results are reported on held-out test sets released by organizers.

## 7. Saturation / discrimination
Malayalam results show near-ceiling performance (test F1 ~0.97 for most models) suggesting the task is relatively easy for Malayalam with current models. Tamil (test F1 ~0.76–0.78) and Kannada (test F1 ~0.70–0.74) show more room for improvement. Individually, IndicBERT and MuRIL substantially underperform XLM-RoBERTa despite their Indian-language pre-training, suggesting generic multilingual pretraining dominates language-specific pretraining for this task.

## 8. Multiturn / agentic aspects
n/a — single-turn comment classification.

## 9. Key numbers
- Dataset sizes: Tamil 43,919 total; Kannada 7,772 total; Malayalam 20,010 total (p.1)
- OOV rates: 85.55% Tamil, 84.23% Malayalam, 83.03% Kannada (p.3)
- Best single model Tamil test F1: XLM-RoBERTa-large 0.77 (p.3)
- Best single model Kannada test F1: XLMR-C (custom pretrained) 0.73 (p.3)
- Best single model Malayalam test F1: XLMR-large and XLMR-C both 0.97 (p.3)
- ExtraTrees ML baseline: Tamil 0.70, Kannada 0.63, Malayalam 0.95 (p.3)
- GA ensemble Tamil test F1: 0.78; Kannada: 0.74; Malayalam: 0.97 (p.4)
- XLM-RoBERTa seed variation: ~15–20%; mBERT seed variation: ~2–3% (p.5)
- 10 random seeds used for GA ensemble candidate pool (p.4)

## 10. Pitfalls & limitations
- IndicBERT and MuRIL underperformance not explained; marked as immediate future work (p.5).
- GA ensemble provides only 1–2% improvement at high computational cost (requires training and inferring 10+ model variants).
- No ablation of which components (fusion vs. GA vs. custom pretraining) contribute most.
- Malayalam near-ceiling performance raises questions about dataset quality/difficulty rather than model capability.
- No error analysis beyond the aggregate results table.
- The paper focuses on competition performance, not interpretability or fairness of offensive classifications.

## 11. Novel ideas worth stealing
- **GA-weighted ensemble over random seed diversity**: rather than selecting the best single random seed or using simple averaging, optimize ensemble weights using genetic algorithm on the development set — applicable to any benchmark with noisy model outputs.
- **Domain-adaptive pretraining as feature engineering**: further pretraining XLM-RoBERTa on the target code-mixed corpus with MLM before fine-tuning improves Kannada performance — a contamination-reducing technique by making the model more familiar with the test distribution.
- **Random seed variance as a diagnostic**: explicitly reporting that XLM-RoBERTa varies 15–20% across seeds while mBERT varies only 2–3% is a useful reliability indicator. Values benchmarks should report seed variance as a robustness metric.
- **BERT-CNN fusion for code-mixed text**: concatenating BERT embeddings with CNN embeddings from FastText skip-gram captures both contextual and local n-gram features, relevant for token-level offensive detection in noisy/code-mixed settings.

## 12. Notable quotes
- "the proportion of out-of-vocabulary (OOV) words (including code-mixed, English and misspelt words) in the dataset as 85.55%, 84.23% and 83.03% in Tamil, Malayalam and Kannada respectively." (p.3)
- "GA-optimised weighted ensembling improves the final model scores by a 1-2% across datasets of different languages which finally helped us to rank higher in the leader board." (p.5)
- "For XLM-RoBERTa models the variation was more (around 15-20%)." (p.5)
- "Our immediate next step will be to investigate the reason behind lower performance of IndicBERT and MuRIL which are specifically trained for Indian context." (p.5)

## 13. UNKNOWN / not in extract
- Detailed error analysis or qualitative examples of misclassified comments.
- Whether custom MLM pretraining was done on Tamil and Malayalam as well (only Kannada improvement is mentioned).
- Full hyperparameter search details for the GA (population size, generations, crossover/mutation rates).
- Human performance upper bound on any of the three language subtasks.
- Inter-annotator agreement for the shared task dataset labels.
