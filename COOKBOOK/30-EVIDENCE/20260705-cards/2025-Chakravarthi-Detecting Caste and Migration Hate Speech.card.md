---
stem: "2025-Chakravarthi-Detecting Caste and Migration Hate Speech"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices, design-space]
task_format: "forced-choice"
scoring_type: "exact-match"
dataset_size: 7875
dataset_construction: "crowdsourced"
languages: ["ta", "en"]
models_tested: ["BLOOM-560m", "MuRIL-base-cased", "IndicBERT", "TamilBERT", "TamilSBERT", "XLM-RoBERTa-base", "XMOD-base"]
headline_numbers:
  - "Best baseline model TamilSBERT achieves macro-F1 of 0.70 (p.22)"
  - "Best overall: BLOOM-560m with KL loss achieves macro-F1 of 0.73 (p.22)"
  - "Shared task winner (Transformers_run3) achieves macro-F1 of 0.82 (p.26)"
  - "Krippendorff's alpha inter-annotator agreement: 0.83441 (p.9)"
  - "Dataset: 7875 annotated Tamil comments (3005 hate, 4870 not-hate) (p.13)"
  - "51 teams participated in shared task; 15 submitted entries (p.24)"
---
## 1. Gist
This paper introduces the first dataset specifically curated for detecting caste and migration hate speech in the low-resource Tamil language. Data was collected from YouTube comments discussing caste and migration issues in Tamil Nadu, annotated by three human annotators into binary categories (hate speech vs. not-hate speech). The authors benchmark seven multilingual and Tamil-specific transformer models and explore custom loss functions (KL, BCE, Hinge), bottleneck adapters, and PEFT techniques (LoRA, P-tuning) to improve detection. A shared task at LT-EDI@EACL 2024 attracted 15 system submissions, with the top system reaching macro-F1 of 0.82. For values-alignment benchmarking, the paper is relevant as a case study in culturally specific, low-resource offensive content classification, including annotation methodology for socially sensitive categories grounded in India's caste hierarchy and migration dynamics.

## 2. Benchmark/eval design features
The core task is binary sequence classification: Hate speech on caste/migration (label=1) vs. Not-hate speech (label=0). This is grounded in a specific cultural context (Tamil Nadu, India) where hate targets include historically marginalized castes (SC, ST, OBC) and interstate migrants. The annotation process involved three expert annotators with diverse demographic backgrounds (different castes, ages, genders), using majority voting for disagreements. Models are evaluated on macro-F1 to account for class imbalance (38% hate, 62% not-hate). The shared task component added external validity by drawing 15 independent system submissions.

## 3. Task format & example item
From Figure 4 (p.14), annotated comments with Tamil text and English translations are provided. Example hate speech comment (Figure 5, p.15): A Tamil comment targeting a specific caste group, labeled "Hate" (caste hate speech). Example migration hate speech (Figure 6, p.15): A Tamil comment targeting migrants from northern Indian states, labeled "Hate." Example annotation difficulty (Figure 7, p.15): A comment with mixed-language content (Tamil + English/Hindi) that annotators found ambiguous.

The task prompt to models is standard sequence classification fine-tuning—no example items with precise page references to verbatim Tamil text are reproducible here, as figures contain images rather than extractable text.

## 4. Scoring / grading methodology
Primary metric: macro-F1, calculated via scikit-learn. This metric is chosen because it provides insights into both overall effectiveness and ability to handle class imbalances. Secondary metrics include per-class precision and recall. All models are evaluated on a held-out test set (20% of data = 1,575 instances). For baseline experiments, the best learning rate across five options (1e-5 to 5e-5) is selected per model. For the shared task, participants are ranked by average macro-F1 on the test set.

## 5. Dataset construction & provenance
- **Source**: YouTube comments scraped using the `youtube-comment-scraper` Python library from videos about caste and migration issues in Tamil Nadu.
- **Collection**: Videos selected via hashtag search (e.g., 'vadakan' for North Indian) and manual keyword search (e.g., 'Agamudiyar' for caste, 'Melpathi temple issue') in Tamil and code-mixed Tamil-English (p.6).
- **Size**: 10,173 raw comments → 7,875 after preprocessing (removing usernames, URLs, short sentences < 3 words) (p.7).
- **Splits**: Train 5,355 (65%), Dev 945 (15%), Test 1,575 (20%) (p.13).
- **Label distribution**: Train: 2,052 hate / 3,303 not-hate; Dev: 351/594; Test: 602/973 (p.13).
- **Annotation**: Three annotators, Krippendorff's alpha = 0.83441 (p.9). Majority voting for disagreements.
- **Privacy**: PII removed during preprocessing.
- **Public release**: Dataset is publicly released to support further research.

## 6. Validity evidence
Inter-annotator agreement is strong: Krippendorff's alpha = 0.83441, which exceeds the 0.80 threshold for reliable annotation (p.9). Annotator demographics were diverse (different castes, age groups 20–45, gender, qualification levels from PG to PhD) to reduce cultural blind spots (p.7). Face validity is established through culturally grounded annotation guidelines that specify caste- and migration-specific terms (vadakan, marvadi, parayan, vaduka pallan, vaellalar, mukkulathor) as criteria (p.8). No external criterion validity or human vs. model accuracy comparison is reported.

## 7. Saturation / discrimination
The best model (BLOOM-560m + KL loss) achieves 0.73 macro-F1, while the shared task winner reaches 0.82. This gap suggests meaningful headroom remains above the baselines. Hinge loss consistently fails across all models (0.22–0.47 macro-F1), indicating the task is sensitive to loss function choice. XLM-RoBERTa-base performs poorly at baseline (0.50) but improves 18% to 0.68 with BCE loss, showing high sensitivity to fine-tuning strategy. The class imbalance (38% hate) makes macro-F1 more appropriate than accuracy as a discrimination metric.

## 8. Multiturn / agentic aspects
n/a. This is a single-turn binary sequence classification task with no multi-turn or agentic components.

## 9. Key numbers
- Total annotated dataset: 7,875 comments (p.13)
- Hate speech instances: 3,005; Not-hate: 4,870 (p.13)
- Krippendorff's alpha: 0.83441 (p.9)
- Best baseline (TamilSBERT): macro-F1 = 0.70 at LR 2e-5 (p.22)
- Best overall (BLOOM-560m + KL loss): macro-F1 = 0.73 at LR 4e-5 (p.22)
- BCE loss improves XLM-RoBERTa by 18% (0.50 → 0.68) (p.22)
- Hinge loss range: 0.22–0.47 across all models (p.22)
- Bottleneck adapter (XMOD): 0.59 (p.22)
- LoRA (PEFT) XMOD: 0.62 (p.22)
- Shared task participants: 51 teams; 15 submitted (p.24)
- Shared task winner macro-F1: 0.82 (Transformers_run3) (p.26)
- Rank 2: kubapok_run1, macro-F1 = 0.81 (p.26)
- Rank 3: CUET_NLP_Manning_run3, macro-F1 = 0.80 (p.26)

## 10. Pitfalls & limitations
- Binary classification may miss fine-grained hate speech types (severity, directness, implicit vs. explicit).
- Keyword-based misclassification: model over-relies on specific words rather than context (e.g., "Karuppu"/black misclassified as casteist when used metaphorically) (p.22–23).
- Romanized Tamil (Tamil written in Latin script) is poorly handled (p.23).
- Informal dialects, slang, and mixed-language content (Tamil-Hindi, code-mixing) cause errors (p.23).
- Implicit hate speech (e.g., "Us vs. Them" narratives without explicit slurs) is missed (p.23).
- Difficulty distinguishing policy complaints from hate speech (p.23).
- Only three annotators; no assessment of inter-annotator agreement per category.
- YouTube-only source may not generalize to other social media platforms or registers.
- Temporal scope and recency of data not reported.

## 11. Novel ideas worth stealing
1. **Culturally grounded annotation criteria**: Providing annotators with explicit caste/community-specific terms as classification criteria (rather than purely general hate speech definitions) increases precision in cultural hate speech annotation—reusable for any culturally specific values benchmark.
2. **Heterogeneous annotator demographics as validity strategy**: Recruiting annotators from both historically marginalized and dominant castes improves coverage of perspectives that Western-centric annotation pools miss—a design principle for any culturally sensitive dataset.
3. **Custom loss function comparison**: Systematically comparing KL divergence, Hinge, and BCE loss functions for offensive content classification reveals that loss function choice (not just model architecture) is a primary driver of performance on imbalanced datasets—a benchmark design consideration for any hate speech evaluation.
4. **Shared task as external validation layer**: Conducting a public shared task with 15 external teams adds external validity to dataset quality and establishes a competitive leaderboard with diverse methods—a model for how new benchmark datasets should be validated.
5. **Error analysis by linguistic category**: Categorizing misclassifications by linguistic phenomenon (keyword-based, indirect hate, Romanized text, informal dialect, over-sensitivity) provides a diagnostic framework that any hate speech or values classifier can adopt.

## 12. Notable quotes
- "It is the first ever dataset that has been solely focusing on caste and migration hate speech in Tamil language." (p.6)
- "The Krippendorff's score is 0.83441" [indicating strong inter-annotator agreement] (p.9)
- "Overall, Bloom-560 m fine-tuned with KL loss at a learning rate of 4.00E−05 outperformed all other models and methods, achieving the best macro-F1 score of 0.73. This superior performance can be attributed to the KL loss function's effectiveness in handling the nuances of caste and migration-related hate speech detection." (p.22)
- "The model must be enhanced with deeper contextual understanding, allowing it to analyze full sentence meanings rather than relying on specific keywords." (p.23)

## 13. UNKNOWN / not in extract
- Precise timestamps of YouTube data collection are not reported.
- Dataset license terms are not specified.
- Demographic breakdown of the 51 shared task participants (institutions, countries) is not reported.
- Whether the dataset covers code-mixed Tamil-English at a specific ratio is unclear.
- Human accuracy ceiling on the task (beyond annotator agreement) is not established.
- Details of the annotation guidelines beyond the two-category definitions and term lists are not fully reproduced in the extract.
