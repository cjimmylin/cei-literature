---
stem: "2025-Ishmam-BanTH A Multi-label Hate Speech Detection Dataset for Transliterated"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, saturation-discrimination, validity-psychometrics, best-practices]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 37350
dataset_construction: "crowdsourced"
languages: ["Bangla (transliterated Roman script)"]
models_tested: ["GPT-3.5", "GPT-4o", "BanglaBERT", "BanglishBERT", "BanglaHateBERT", "TB-BERT", "TB-mBERT", "TB-XLM-R", "XLM-R", "mBERT", "CharBERT", "MuRIL", "IndicBERT", "VAC-BERT"]
headline_numbers:
  - "37,350 total samples: 10,282 hate, 27,167 non-hate (p.4)"
  - "TB-mBERT best binary F1: 77.36 Macro-F1, 82.57% accuracy (p.6)"
  - "GPT-4o + Few-shot best LLM multi-label: 39.53% Macro-F1, 26.76% subset accuracy (p.6)"
  - "Translation-based prompting ~8% improvement over vanilla GPT-4o in zero-shot multi-label (p.7)"
  - "Inter-annotator Fleiss Kappa: 0.53 overall (moderate); binary labeling Kappa 0.75 (p.3)"
  - "Training/Val/Test split 80:10:10 = 29,879 / 3,736 / 3,735 (p.4)"
---
## 1. Gist
BanTH is the first multi-label hate speech detection dataset for transliterated Bangla (Bangla written in Roman/Latin script), a dominant form of online Bangla text that is severely under-resourced in NLP. The dataset consists of 37,350 YouTube comments collected from 26 channels across three categories (News & Politics, People & Blogs, Entertainment), labeled with binary hate/non-hate and seven multi-label target group categories (Political, Religious, Gender, Personal Offense, Abusive/Violence, Origin, Body Shaming). A key contribution is a novel translation-based LLM prompting strategy that converts transliterated text to standard Bangla or English before classification, yielding ~8% improvement over vanilla LLM prompting in zero-shot settings. For values-alignment benchmarking, BanTH demonstrates the critical challenge of evaluating content moderation across non-English, non-script-standard text, revealing that even strong multilingual models struggle with culturally embedded hate in underrepresented script forms.

## 2. Benchmark/eval design features
- Binary classification: hate vs. non-hate.
- Multi-label classification: hate samples additionally labeled with one or more of 7 target group categories.
- Target groups: Political, Religious, Gender, Personal Offense, Abusive/Violence, Origin, Body Shaming.
- Two-stage annotation: first binary label, then multi-label for hate samples.
- 26 YouTube channels scraped; content spans Jan 2020 – July 2024, capturing COVID-19 and Bangladesh quota reform movement events.
- Further Pretraining (FPT) approach: encoders pre-trained on 243k unlabeled transliterated Bangla texts (BanglaTLit-PT corpus) before fine-tuning.
- Novel translation-based prompting: translate transliterated Bangla → standard Bangla or English before classifying.
- Evaluation metrics: Macro-F1, Accuracy, Subset Accuracy (multi-label), Hamming Loss.

## 3. Task format & example item
Binary/multi-label classification on transliterated Bangla text. Example from the abstract (p.1):

Input: "Awami League er shobai ke puriye mere felo. Ora Indian dalal"
English Translation: "Burn everyone from Awami League to death. They are Indian spy."
Binary label: hate
Multi-labels: Abusive/Violence, Political

Another example from Table 8 (p.8):
Input: "Chup catukar khuni"
English Translation: "Shut up killer sycophant"
GPT-4o+Explanation prediction: NH (incorrect) — "The text seems to express frustration but lacks direct hate indicators."
GPT-4o+Explanation+Translation prediction: H (correct) — "The phrase 'chup catukar khuni' implies killing, which incites violence and hate."

## 4. Scoring / grading methodology
Binary classification: Macro-F1 and Accuracy on test split.
Multi-label classification: Macro-F1, Subset Accuracy, Hamming Loss.
- Subset Accuracy: proportion of samples where ALL predicted labels match ground truth.
- Hamming Loss: fraction of wrong labels.
- Inter-annotator agreement measured with Fleiss' Kappa across both expert-annotator and inter-annotator pairs for each category.

## 5. Dataset construction & provenance
- Source: YouTube API, 26 channels, Jan 2020 – July 2024 (p.3).
- Video categories: News & Politics (32,440 samples), People & Blogs (4,014), Entertainment (996).
- Filtering: Roman script only; minimum 3 words; deduplication; URL/PII removal.
- Annotation: 4 annotators + 2 domain experts; all native Bangla speakers, high school graduates, active social media users with transliterated Bangla experience.
- 3 annotators per sample; majority vote; domain experts resolved disagreements.
- Inter-annotator Kappa: 0.53 overall moderate; binary 0.75 (substantial); per-category range 0.66–0.75 (p.3).
- 80:10:10 train/val/test split; stratified.
- Annotators compensated above industry standard on hourly basis.
- License: YouTube API terms of service compliant; PII removed.

## 6. Validity evidence
- Fleiss' Kappa reported per category for both expert-annotator and inter-annotator agreement (Table 3, p.3).
- Binary labeling: 0.75 (inter-annotator), 0.71 (expert-annotator) — substantial agreement.
- Multi-label categories: range 0.62–0.72 — moderate to substantial.
- Overall multi-label kappa (0.53) described as "moderate" per Islam et al. (2021).
- Event-based data collection captures natural distribution of hate speech (not keyword-biased).
- Authors acknowledge that Personal Offense has highest error rates due to diverse linguistic patterns and generic representative words (p.7).
- Authors note expert agreements were lower than annotators due to deeper disagreement in gray-area interpretations.

## 7. Saturation / discrimination
- Severe class imbalance: 27,167 non-hate vs 10,282 hate (72.73% non-hate baseline) — a dummy "always non-hate" classifier exceeds GPT-3.5 performance on binary task (p.9).
- Strong class imbalance in multi-label: Personal Offense dominates (6,964 of 10,282 hate samples); Religious (139), Gender (193), Body Shaming (86) are very rare (p.3).
- Personal Offense has lowest per-category F1 (34.1% incorrect per Figure 4) due to high variation and generic terms.
- Religious, Origin, Body Shaming have very high accuracy (99.2%, 99.3%, 99.4%) likely due to distinctive representative terms.
- TB-mBERT best binary: 77.36 Macro-F1; GPT-4o best binary: 70.70 (few-shot). Fine-tuned models outperform LLMs substantially.
- LLM multi-label performance is low: GPT-4o + Few-shot = 39.53% Macro-F1 vs TB-BERT = 30.17% (p.6).

## 8. Multiturn / agentic aspects
n/a — single-turn classification task.

## 9. Key numbers
- Total samples: 37,350 (10,282 hate / 27,167 non-hate) (p.4)
- Train / Val / Test: 29,879 / 3,736 / 3,735 (p.4)
- 26 YouTube channels, 3 video categories (p.3)
- Avg length: 58.09 characters / 10.16 words; max 1,951 characters / 368 words (p.4)
- Unique words: 75,977 (p.4)
- Inter-annotator Kappa (binary): 0.75; overall multi-label: 0.53 (p.3)
- TB-mBERT binary: 77.36 Macro-F1, 82.57% accuracy (p.6)
- GPT-4o + Few-shot multi-label: 39.53% Macro-F1 (p.6)
- Translation prompting improvement: ~8% over vanilla in zero-shot settings (p.7)
- GPT-4o consistently 8–10% better than GPT-3.5 across all prompting variants (p.7)
- Pre-training corpus (BanglaTLit-PT): 243k unlabeled transliterated texts (p.4)

## 10. Pitfalls & limitations
Author-admitted (p.9):
- Severe class imbalance: 72.73% non-hate baseline; GPT-3.5 performs worse than this dummy classifier.
- Does not cover all hate categories (e.g., socioeconomic-based hate is absent due to insufficient YouTube examples).
- Inter-annotator kappa comparatively lower than other classification tasks due to subjectivity of hate speech.
- Expert disagreements higher than annotator disagreements (experts more attuned to gray areas).

Additional observations:
- Coverage limited to YouTube, a single platform; does not capture Facebook, Twitter, or closed messaging apps where Bangla hate speech also proliferates.
- Annotation only in English-script transliterated Bangla, excluding native Bangla script examples.
- Low-resource categories (Religious: 139, Body Shaming: 86) may not have sufficient examples for reliable evaluation.
- The "event-based" collection methodology may overrepresent political and violence-adjacent hate from specific time periods.

## 11. Novel ideas worth stealing
1. **Translation-based prompting for low-resource evaluation**: Convert under-resourced text to a higher-resourced form (standard language or English) before feeding to an LLM for classification. This simple pre-processing step improved zero-shot multi-label F1 by ~8%. Directly applicable to cross-lingual values evaluation in low-resource settings.
2. **Event-based corpus collection**: Anchoring data collection to social/political events increases the proportion of relevant (hate-positive) examples and provides natural temporal and topic diversity. Values-alignment benchmarks could similarly sample from event-anchored corpora.
3. **Multi-label over multi-class for hate**: Multi-label annotation captures the overlapping nature of hate targets (e.g., Political + Abusive/Violence frequently co-occur) that multi-class labels miss. Benchmark designers should consider multi-label schemes for morally nuanced classification tasks.
4. **Further Pretraining (FPT) as a low-resource solution**: Adapting a pre-existing encoder to the specific text style (transliterated text) via domain-adaptive pretraining before fine-tuning outperforms direct fine-tuning and zero-shot LLMs. This has implications for cultural-linguistic evaluation where models lack exposure to specific script/style conventions.
5. **Co-occurrence analysis of labels**: Visualizing and reporting label co-occurrence heatmaps (Figure 3) reveals which hate types cluster together, which is useful both for error analysis and for benchmark calibration.

## 12. Notable quotes
- "Despite boasting over a quarter of a billion speakers worldwide, Bangla remains a low-resource language in terms of Natural Language Processing (NLP) tasks." (p.2)
- "Translation-based prompting strategy that translates or transliterates under-resourced text to higher-resourced text before classifying the hate group(s)." (p.1)
- "The BANTH dataset contains 27167 non-hate samples out of 37350, i.e. a dummy classifier predicting all samples as non-hate achieves an accuracy of 72.73%." (p.9)
- "Erroneous translations often lead to incorrect classifications, especially with regional dialects or terms lacking direct English equivalents." (p.8)

## 13. UNKNOWN / not in extract
- License terms for the released dataset.
- Whether the dataset is publicly available and under what access conditions.
- Breakdown of annotation disagreements by event type or video category.
- Whether any quality filtering was applied to annotators based on performance.
- Cross-lingual transfer experiments (e.g., training on English hate data and testing on BanTH).
- Annotation guidelines (mentioned in Appendix B, not in extract).
- Full experimental setup details (reported in App. D, not in extract).
