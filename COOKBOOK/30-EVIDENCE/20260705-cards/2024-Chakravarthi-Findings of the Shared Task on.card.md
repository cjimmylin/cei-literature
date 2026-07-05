---
stem: "2024-Chakravarthi-Findings of the Shared Task on"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 4500
dataset_construction: "crowdsourced"
languages: ["te", "en"]
models_tested: ["Telugu-BERT", "MuRIL", "indicBERT", "mBERT", "XLM-R", "RoBERTa", "DistilBERT", "Zephyr-7b-beta", "OpenChat-3.5"]
headline_numbers:
  - "4,500 annotated Telugu-English codemixed YouTube comments (4,000 train, 500 test) (p.2)"
  - "Best macro F1 = 0.7711 (Team Sandalphon, fine-tuned Telugu-BERT with transliteration augmentation) (p.3)"
  - "23 teams participated; 25 submissions (p.1)"
  - "Training set: 1,939 hate, 2,061 non-hate; nearly balanced (p.2)"
---
## 1. Gist
This paper reports findings from HOLD-Telugu, a shared task on hate and offensive language detection in Telugu-English codemixed social media text, organized at DravidianLangTech 2024 (EACL). It is a binary classification challenge (hate vs. non-hate) applied to YouTube comments scraped from Telugu-language channels. The task addresses a gap in hate speech research for low-resource, morphologically complex Dravidian languages. For values-alignment benchmarking, this work illustrates (1) the difficulty of offensive content detection in non-English, codemixed, agglutinative languages; (2) the performance ceiling achievable with transformer fine-tuning on small datasets; and (3) the kinds of social norm violations (online hate, offensive language) that a culturally-aware values benchmark might need to cover beyond Western English-centric datasets.

## 2. Benchmark/eval design features
Binary classification task: each YouTube comment labeled hate or non-hate. Dataset: 4,500 annotated Telugu-English codemixed comments. Annotation follows YouTube's community guidelines, with special care for Telugu slang and codemixed script variants (Telugu script + Latin script transliteration of Telugu). Annotators were native Telugu speakers with academic credentials. Evaluation metric: macro F1-score. 23 teams participated, submitting up to 3 runs each; best run per team used for ranking.

## 3. Task format & example item
Binary classification of short social media comments. No verbatim example comment provided in the extract. Structure: each comment is a Telugu-English codemixed YouTube comment; model outputs hate or non-hate. Codemixed text includes both Telugu characters and Romanized Telugu (Latin script). (p.2)

## 4. Scoring / grading methodology
Macro F1-score used as the primary ranking metric, ensuring equal weight to both classes despite minor imbalance. Additional metrics (precision, recall) reported in some team papers. CodaLab platform used for submission and evaluation. Best run out of up to 3 permitted per team selected for the leaderboard (p.2).

## 5. Dataset construction & provenance
YouTube comments collected from Telugu-language videos. Annotation: binary (hate/non-hate) by native Telugu speakers following YouTube's community guidelines. Spam content excluded. Codemixed text preprocessed to handle both script variants. Split: 4,000 train (1,939 hate, 2,061 non-hate), 500 test (250 hate, 250 non-hate) — balanced test set (p.2). No explicit license mentioned; data collection followed YouTube's terms of service.

## 6. Validity evidence
Near-balanced test set (250/250) ensures F1 is not inflated by class majority. Annotators are native Telugu speakers with strong academic credentials, providing domain expertise. No explicit inter-annotator agreement statistics reported in this overview paper. The range of participating systems (0.49–0.77 F1) suggests the task has genuine discriminative power and is neither trivially easy nor impossible.

## 7. Saturation / discrimination
Top F1 = 0.7711, achieved by two independent systems (Telugu-BERT + transliteration augmentation; CNN + logistic regression). Score spread across 25 submissions ranges from 0.49 to 0.77, indicating substantial headroom. Best-performing systems leverage Telugu-specific pretraining and transliteration normalization. LSTM/RNN-based models consistently underperform transformer models (~0.65–0.71 vs. ~0.66–0.77 for BERT variants) (p.5).

## 8. Multiturn / agentic aspects
n/a. Single-turn classification of individual comments.

## 9. Key numbers
- 4,500 total annotated comments; 4,000 train, 500 test (p.2)
- 1,939 hate / 2,061 non-hate in training set (p.2)
- 250 hate / 250 non-hate in test set (p.2)
- 43,432 total words, 18,600 tokens; average sentence length 9.65 tokens (p.2)
- 69 registered teams, 25 submitted results (p.2)
- Best macro F1: 0.7711 (two teams tied) (p.3)
- Lowest submitted F1: 0.4653 (p.3)
- Most teams used BERT-based models (p.5)

## 10. Pitfalls & limitations
- Binary label (hate/non-hate) is coarse; no severity gradation or category of hate type.
- Small dataset (4,500 items) limits generalization and fine-tuning headroom.
- YouTube-specific data: content moderation by the platform pre-filters the most egregious content, potentially making the remaining hate speech more subtle.
- Codemixed Telugu-English is a narrow linguistic variety; does not cover Telugu-only or other Dravidian codemix patterns.
- No inter-annotator agreement reported in this overview, making annotation quality hard to assess.
- No LLM zero-shot baselines reported; only fine-tuned models.
- Context of comments (video topic, thread) not used by any team.

## 11. Novel ideas worth stealing
- **Transliteration augmentation as a data augmentation technique**: converting codemixed text to a single script (all-Telugu or all-Latin) before classification improved the best system's performance; this is directly applicable to any multilingual values benchmark dealing with script variation.
- **Balanced test set with stratified hate/non-hate**: deliberately equalizing test-set class distribution provides a cleaner evaluation signal than naturally imbalanced splits — worth emulating in offensive content evaluation modules of values benchmarks.
- **Morphologically complex low-resource language as a stress test**: including Dravidian or other agglutinative languages in a values benchmark would reveal robustness gaps that English-only evaluation misses.
- **Script normalization as a preprocessing step**: multiple teams that normalized script variants (transliteration) outperformed those that did not, suggesting that benchmark designers for codemixed text should provide normalized variants or require models to handle them.

## 12. Notable quotes
- "In a codemixed Dravidian language, it is much harder to find hateful words because the text is codemixed and has linguistic properties like morphological richness and agglutinative characteristics." (p.1)
- "The majority of the teams used BERT-based models for feature extraction. Variants of the BERT such as Telugu-BERT, indicBERT, hate-BERT, and other multilingual BERT models achieved significant performance in classifying a Telugu codemixed comment into hate and non-hate." (p.5)
- "The effective analysis and categorization of YouTube comments may present a challenge due to the prevalence of incorrect syntax, typographical errors, and non-standard language usage in social media posts and comments." (p.2)

## 13. UNKNOWN / not in extract
- Verbatim example annotated comments
- Inter-annotator agreement statistics for the dataset
- Details of how YouTube videos/channels were selected for comment collection
- Whether the dataset is publicly released
- Full descriptions of all 25 team systems (brief summaries provided for most; some lack detail)
- Performance breakdown by hate/non-hate class separately for all teams
- Any demographic or regional breakdown of the language variants
