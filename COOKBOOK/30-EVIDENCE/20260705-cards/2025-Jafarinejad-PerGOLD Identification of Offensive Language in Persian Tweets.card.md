---
stem: "2025-Jafarinejad-PerGOLD Identification of Offensive Language in Persian Tweets"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices, validity-psychometrics]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 13716
dataset_construction: "crowdsourced"
languages: ["fa"]
models_tested: ["LR", "SVM", "RoBERTa", "ParsBERT"]
headline_numbers:
  - "13,716 Persian tweets labeled: 4,613 offensive (34%), 9,103 non-offensive (66%) (p.5)"
  - "ParsBERT best model: F1=0.854, Accuracy=0.85, Precision=0.86, Recall=0.85 (p.6)"
  - "70% train / 30% test split; binary classification (p.5)"
  - "4 taggers used for annotation via custom crowdsourcing platform (p.5)"
---
## 1. Gist
PerGOLD (Persian General Offensive Language Dataset) introduces a new crowdsourced dataset of 13,716 Persian tweets labeled for binary offensive language detection. Distinctive features are (1) an event-based data collection strategy — tweets collected within 14 days of events that historically triggered offensive language — and (2) a custom-built crowdsourcing platform for annotation. The dataset achieves 34% offensive content, higher than most comparable datasets, which the authors attribute to the event-based methodology. The best model (ParsBERT, a monolingual Persian BERT variant) achieves F1=0.854, outperforming multilingual RoBERTa substantially. For values-alignment benchmarking, this paper contributes to the evidence base for non-English, low-resource offensive language evaluation, and demonstrates that monolingual fine-tuned models outperform general multilingual architectures for language-specific content moderation tasks.

## 2. Benchmark/eval design features
Binary classification: offensive (OL) vs. non-offensive (non-OL). No multi-label or hierarchical structure.
- Event-based collection: tweets from 14 days following various triggering events (ethnic, national, origin/lineage, gender, religious, racial, physical condition categories).
- Crowdsourcing platform: custom-built website with Task Owner, Tagger, and User roles.
- Labeling guideline: plain/promotional texts = non-OL; texts with insults toward sacred beliefs, provocative sexual/gender discussions, racial insults, or disability insults = OL.
- 4 taggers with language knowledge.
- Baseline models: LR, SVM (classical), RoBERTa (multilingual), ParsBERT (monolingual Persian BERT).
- Preprocessing: Hazm library; removed numbers, URLs, emails, monetary units, emojis, punctuation.
- Evaluation metrics: Accuracy, Precision, Recall, F1-score.

## 3. Task format & example item
Binary classification: given a Persian tweet, label as offensive or non-offensive. No verbatim example items appear in the extract.

## 4. Scoring / grading methodology
Standard binary classification metrics: Accuracy, Precision, Recall, F1-score on 30% test split. No cross-validation or inter-annotator reliability metrics are reported for the annotation process (notable gap).

## 5. Dataset construction & provenance
- Source: Twitter, via keyword search anchored to social/political events triggering OL.
- Collection window: 14 days post-event per event type.
- Event types: ethnic, national, origin/lineage, gender, religious, racial, physical condition offenses.
- ~14,000 tweets initially extracted, resulting in 13,716 labeled samples after annotation.
- Annotation: 4 taggers selected by task owner for knowledge and skill; custom crowdsourcing platform.
- Labels: binary OL / non-OL.
- 70% train / 30% test split.
- Preprocessing via Hazm (Persian NLP library).
- 34% OL rate achieved, described by authors as higher than comparable datasets due to event-based methodology (p.5).

## 6. Validity evidence
- No inter-annotator reliability (Kappa or similar) is reported — a significant validity gap.
- Validity is demonstrated primarily through model performance: ParsBERT achieves F1=0.854, suggesting the dataset is learnable and coherent.
- Monolingual (ParsBERT) outperforms multilingual (RoBERTa) and classical models (LR, SVM), suggesting language-specific encoding is important.
- Event-based collection gives a more natural offensive/non-offensive distribution vs. keyword-biased collection (p.5).
- Dataset ranks second in size among Persian OL datasets after OPSD (17,000 tweets) (p.3).

## 7. Saturation / discrimination
- 34% OL vs. 66% non-OL: still imbalanced but better than most comparable datasets (e.g., English HaterNet: 26%, Davidson et al.: 7%, Greek OffComGR: 28%).
- SVM achieves only 0.33 F1 (barely above random), demonstrating the task is non-trivial.
- RoBERTa (multilingual) achieves 0.71 F1 — similar to classical LR (0.73), suggesting multilingual models have limited benefit for Persian.
- ParsBERT-2 (12 layers) marginally outperforms ParsBERT-1 (6 layers): 0.854 vs. 0.824 F1.
- No ceiling analysis provided; headroom remains (F1 < 0.90).

## 8. Multiturn / agentic aspects
n/a — single-turn binary classification task on static tweets.

## 9. Key numbers
- Total samples: 13,716 (4,613 OL / 9,103 non-OL) (p.5)
- OL ratio: ~34% (p.1)
- Train / Test split: 70% / 30% (p.5)
- ParsBERT F1: 0.854, Accuracy: 0.85 (p.6)
- RoBERTa F1: 0.71 (p.6)
- LR F1: 0.73 (p.6)
- SVM F1: 0.33 (p.6)
- 4 taggers used for annotation (p.5)

## 10. Pitfalls & limitations
Author-admitted:
- None explicitly stated in the paper; discussion focuses on the dataset's contributions and results.

Additional observations:
- No inter-annotator agreement (Kappa) is reported, which is a notable gap for a crowdsourced annotation task.
- Binary-only labels; no multi-label taxonomy of offense type (unlike PerBOLD which has 9 offense subtypes).
- Only 4 taggers — extremely small annotator pool; no information on annotation disagreements or resolution protocol.
- No information on which events were selected or why, reducing reproducibility.
- Twitter/X as a platform has undergone significant policy changes; the dataset may reflect a historical content moderation landscape.
- No mention of data licensing or public release conditions.
- Collection period not specified (only "14 days per event" windows, without dates).

## 11. Novel ideas worth stealing
1. **Event-based corpus collection for offensive content**: Anchoring collection to real social/political events that historically trigger offensive language increases OL sample proportion naturally without keyword injection bias. This produces more ecologically valid samples that reflect actual hate speech triggers. Directly reusable for other language-specific offensive content benchmarks.
2. **Custom crowdsourcing platform with role-based access control**: Building a purpose-designed annotation platform (Task Owner / Tagger / User roles) gives researchers more control over tagger selection, quality, and workflow than general-purpose platforms like MTurk. Useful template for annotation in low-resource languages where specialized platform support is sparse.
3. **Monolingual vs. multilingual comparison as validity check**: Testing both monolingual (ParsBERT) and multilingual (RoBERTa) architectures provides useful evidence about the language-specificity of the task. Consistently showing monolingual > multilingual for morphologically rich or script-diverse languages is a meaningful design insight for evaluating cultural-linguistic benchmarks.
4. **OL ratio as a data quality metric**: The paper frames the 34% OL proportion as a design achievement (vs. typical 7–26% in comparable datasets), arguing that higher OL ratios reduce class imbalance problems. Benchmark designers for hate/offense tasks should explicitly report and target OL ratios.

## 12. Notable quotes
- "Utilizing the event-based methodology in data collection, a 14-day period of different events triggering offences was searched by appropriate keywords." (p.7)
- "In monolingual NLP tasks, using an architecture and training it from scratch with the development of the corresponding monolingual corpus may be more successful in acquiring and encoding language-specific knowledge than using multilingual models with fine tuning." (p.6)
- "Offensive language is often triggered by social and political events. As a result, offensive comments related to these events are more frequent and varied." (p.3)
- "There is no universally accepted global definition of OL. This causes a piece of content to be considered OL by some, while others do not view it as such." (p.2)

## 13. UNKNOWN / not in extract
- Inter-annotator agreement statistics (Kappa or similar) — not reported.
- Specific events used for data collection (dates, event names).
- Annotation guidelines beyond a brief summary.
- Whether the dataset is publicly available and under what license.
- The specific evaluation split dates or temporal coverage.
- Whether any quality control mechanisms were applied to the taggers.
- Information about disagreement resolution among the 4 taggers.
