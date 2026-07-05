---
stem: "2024-Sharma-TABHATE A Target-based Hate Speech Detection"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, saturation-discrimination, design-space]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 2020
dataset_construction: "crowdsourced"
languages: ["hi"]
models_tested: ["CNN", "LSTM", "Bi-LSTM", "mBERT", "MuRIL", "IndicBERT", "XLM-RoBERTa"]
headline_numbers:
  - "Fleiss Kappa inter-annotator agreement = 0.77 (substantial) (p.6)"
  - "XLM-RoBERTa best model: macro-F1 0.77, weighted-F1 0.91 after SMOTE (p.9)"
  - "Dataset: 2020 tweets; 182 individual-targeted, 243 community-targeted, 1595 none (p.6)"
  - "Train/val/test split 80/10/10 (p.7)"
---
## 1. Gist
TABHATE (Target-based Hate Speech dataset) is the first annotated Hindi-language dataset for target-based hate speech detection. It contains 2,020 tweets labelled into three classes: individual-targeted hate, community-targeted hate, and none. The paper bridges a resource gap in non-English hate-speech research and benchmarks a range of deep learning and transformer models on the task. For values-alignment benchmarking, it is a useful reference for building multilingual, target-aware safety evaluation datasets and illustrates how crowdsourced annotation with strong inter-rater agreement can produce high-quality ground truth for sensitive content tasks.

## 2. Benchmark/eval design features
The dataset captures a three-way distinction between hate targeting individuals, hate targeting groups/communities/organizations, and non-hate. This fine-grained target-level labelling is its primary contribution over prior binary hate/non-hate datasets in Hindi. Annotation was done by three independent postgraduate annotators who are native Hindi speakers. The benchmark evaluates models on precision, recall, F1 per class, plus macro- and weighted-average F1.

## 3. Task format & example item
Multi-class tweet classification. Example tweet (class: Community targeted, p.5):

> "बेटी पढ़ाओ बेटी आपस में लड़ाओ।" #Women
> Translation: "Teach daughter, fight with each other."

Label: Community targeted (2).

## 4. Scoring / grading methodology
Standard multi-class classification metrics: per-class precision, recall, F1; macro-average F1 (treats all classes equally); weighted-average F1 (weighted by support). Ground truth is majority vote of three annotators. Both before-oversampling and after-SMOTE results are reported.

## 5. Dataset construction & provenance
Tweets collected via Twitter API using keywords related to hate speech targets: women, LGBTIQ+, religious groups, farmers, politicians. Hashtags include #metoo, #LGBTIQ, #Hijab Row, #boycottMuslim, etc. Duplicates, reposts, non-text entities, and @-mentions removed. Emojis retained. Dataset is class-imbalanced (1595 none, 243 community, 182 individual). SMOTE oversampling used to balance to 1595 per class for training. 80/10/10 train/val/test split. License: CC BY 4.0.

## 6. Validity evidence
Fleiss Kappa = 0.77 indicating substantial agreement (Landis & Koch scale) among three annotators (p.6). This is the primary validity measure reported. No external validity or criterion validity evidence against other datasets is provided.

## 7. Saturation / discrimination
The dataset is significantly imbalanced without oversampling (1595/243/182). Minority classes (individual-targeted) show poor recall without SMOTE; e.g., CNN before oversampling: individual-target F1 = 0.18 (p.9). XLM-RoBERTa achieves macro-F1 0.77 after SMOTE, suggesting reasonable but not saturated performance. Individual-target class remains the hardest (0.46 F1 even for best model).

## 8. Multiturn / agentic aspects
n/a — single-tweet classification.

## 9. Key numbers
- Dataset size: 2,020 tweets (p.2)
- Classes: individual-targeted 182, community-targeted 243, none 1595 (p.6)
- After SMOTE: 1595 per class; train 3830, val 479, test 476 (p.7)
- Fleiss Kappa: 0.77 (p.6)
- CNN weighted-F1: 0.72 (BS), 0.73 (AS) (p.9)
- Bi-LSTM weighted-F1: 0.80 (BS), 0.82 (AS) (p.9)
- XLM-RoBERTa weighted-F1: 0.89 (BS), 0.91 (AS) (p.9)
- XLM-RoBERTa macro-F1: 0.75 (BS), 0.77 (AS) (p.9)
- IndicBERT weighted-F1: 0.85 (BS), 0.86 (AS) (p.9)

## 10. Pitfalls & limitations
- Small dataset (2020 tweets); may not generalize well.
- Collected via targeted keywords/hashtags, introducing sampling bias; does not represent organic hate speech distribution.
- No analysis of annotation disagreements or edge cases.
- Only a single domain (Twitter); not representative of other Hindi-language online platforms.
- SMOTE applied in feature space on text embeddings, which is unusual for text tasks and may introduce artifacts.
- No demographic information about annotators beyond being postgraduate CS students.
- Class imbalance means individual-targeted hate (the rarest category) is the hardest to detect.
- No information on dataset release, availability, or accessibility for others.

## 11. Novel ideas worth stealing
- **Target-level annotation** (individual vs. community vs. none) is more actionable than binary hate/non-hate for safety systems — directly adaptable to values-alignment benchmarks testing group-harm sensitivity.
- **Multilingual hate-speech taxonomy**: the three-class scheme could be extended to other under-resourced languages to produce a cross-lingual values-alignment component.
- **Oversampling as augmentation documentation**: reporting both pre- and post-SMOTE results for all models makes it easy to assess how severely class imbalance penalizes minority categories — a useful best practice for any imbalanced safety benchmark.
- **Annotator selection rationale** (native speakers, domain-appropriate background) — explicit documentation of annotator qualifications strengthens annotation quality claims and is worth adopting in values evaluation datasets.

## 12. Notable quotes
- "This is the first dataset of this kind in the Hindi language in which the type of content is characterized based on target of the hate speech." (p.7)
- "The high value of inter annotator agreement shows that its high quality annotated dataset." (p.7)
- "Those tweets that are against or that attack any community/religion/organization or political parties and spread hate or false beliefs about a particular community are to be labelled as community targeted." (p.5)

## 13. UNKNOWN / not in extract
- Whether dataset is publicly released and where it can be obtained.
- Exact collection time period for the tweets.
- Whether annotation guidelines are publicly available.
- Error analysis on model failures — which specific hate categories were confused most.
- Any human baseline performance reported separately from model performance.
