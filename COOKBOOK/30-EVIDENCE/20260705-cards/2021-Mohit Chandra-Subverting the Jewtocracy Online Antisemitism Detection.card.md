---
stem: "2021-Mohit Chandra-Subverting the Jewtocracy Online Antisemitism Detection"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [design-space, validity-psychometrics, cultural-linguistic, normative-ethics]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 6611
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["BERT", "RoBERTa", "GloVe+Dense", "FastText", "ResNet-152", "DenseNet-161"]
headline_numbers: ["MFAS multimodal system binary accuracy on Gab: ~91% (p.1)", "MFAS multimodal system binary accuracy on Twitter: ~71% (p.1)", "4-class accuracy on both datasets: ~67-68% (p.1)", "Fleiss kappa inter-annotator agreement: 0.707 (p.4)", "Twitter dataset: 3,102 posts / 1,428 antisemitic; Gab: 3,509 posts / 1,877 antisemitic (p.4, Table 1)"]
---
## 1. Gist
Chandra et al. (2021) present the first multimodal deep learning system for detecting and categorizing online antisemitism, accompanied by two newly annotated datasets from Twitter (3,102 posts) and Gab (3,509 posts). Each post is labeled for presence/absence of antisemitism and, if antisemitic, for one of four categories: Political, Economic, Religious, and Racial. The system combines RoBERTa text encoding with ResNet-152 image encoding and OCR-extracted image text, fusing them via learned multimodal fusion (MFAS). For values-alignment benchmarking, this paper is relevant as a dataset-construction methodology paper for fine-grained hate-speech categorization and as evidence of how modality-specific signals (text, images, OCR) each contribute to detecting one particularly challenging form of discriminatory content.

## 2. Benchmark/eval design features
**Tasks:**
1. Binary classification: is a social media post antisemitic or not?
2. 4-class categorization: which type of antisemitism (Political / Economic / Religious / Racial)?

**Antisemitism taxonomy** (based on Brustein 2003 + IHRA definition):
- Political: belief Jews seek world political power, control media/government
- Economic: belief Jews engage in harmful economic activities, are greedy/wealthy
- Religious: bias against Judaism; portraying Jews as Christ-killers or anti-Christian
- Racial: ethnic/racial prejudice, Holocaust denial, racial mixing conspiracy theories

**Dataset characteristics:**
- Twitter (3,102 posts): 1,428 antisemitic; Political 639, Economic 183, Religious 124, Racial 482
- Gab (3,509 posts): 1,877 antisemitic; Political 736, Economic 118, Religious 144, Racial 879
- 84% of images contained some text (OCR used)
- Average post text: ~45 words (Twitter), ~27 words (Gab); OCR output: ~50-51 words per post

**Architecture:**
RoBERTa (text+OCR) + ResNet-152 (image) → MFAS fusion → Joint encoder/decoder → classifier. End-to-end trained with reconstruction + classification loss.

## 3. Task format & example item
Binary classification example (p.2, Figure 1):
> Post text: "Even grandma can see what's going on." [accompanied by antisemitic image] — appears non-antisemitic from text alone but antisemitic when image is considered.

Category classification example (p.3):
> Political: "The jews run congress through threats and intimidation."
> Racial: "white is right which makes the jews always wrong."

## 4. Scoring / grading methodology
- 5-fold cross-validation; train/val/test split 64:16:20 per fold
- Metrics: accuracy and macro-F1, both reported for binary and 4-class tasks
- Annotation: each post annotated by 3 annotators; disagreements resolved through discussion (consensus annotation, not majority vote)
- Inter-annotator agreement: Fleiss' Kappa = 0.707 (substantial agreement) (p.4)

## 5. Dataset construction & provenance
- Data collected from Twitter and Gab; posts filtered to include at least one term from a high-precision Jewish-reference lexicon
- Required posts to have both text and image components
- Four undergraduate annotators, fluent in English, with detailed guidelines and test rounds
- 3 annotators per post; agreement-by-discussion protocol
- User-sensitive information removed for privacy
- Data publicly available at https://github.com/mohit3011/Online-Antisemitism-Detection-Using-MultimodalDeep-Learning
- No explicit contamination/temporal controls described

## 6. Validity evidence
- Fleiss' Kappa = 0.707, indicating substantial annotator agreement (p.4)
- Unimodal baselines (text-only, image-only) systematically compared against multimodal systems
- Confusion matrix analysis reveals most confusion between Political and Racial classes (p.8), which is semantically interpretable
- Attention visualization (BERTviz, GradCAM) confirms model attends to meaningful signals (e.g., "parasites" co-attending with "Jew"; focus on antisemitic meme imagery)
- Error analysis identifies failure modes: sarcasm, multi-screenshot images, reporting-antisemitism-about-others context

## 7. Saturation / discrimination
- Binary classification substantially easier than 4-class: Gab binary ~91% vs 4-class ~67% (p.1)
- Multimodal system improves substantially over text-only for Gab (larger improvement than Twitter, because Gab images are more informative) (p.7)
- Image-only classifiers significantly worse than text-only (p.7, Table 3) — images alone insufficient
- RoBERTa text-only on Gab binary: 87.4% accuracy — high but multimodal adds ~4pp
- Religious and Economic categories have fewer examples and are harder to classify (confusion matrices, p.8)
- No formal ceiling analysis; much headroom remains for multiclass task

## 8. Multiturn / agentic aspects
n/a — all classification tasks are single-post, single-turn.

## 9. Key numbers
- Twitter dataset: 3,102 posts total; 1,428 antisemitic (46%) (p.4, Table 1)
- Gab dataset: 3,509 posts total; 1,877 antisemitic (53%) (p.4, Table 1)
- Fleiss' Kappa: 0.707 (p.4)
- 84% of images contained text (motivating OCR) (p.4)
- MFAS best binary accuracy: Gab ~91%, Twitter ~71% (p.1)
- MFAS 4-class accuracy: ~67% (Gab), ~68% (Twitter) (p.1)
- RoBERTa text-only binary: Gab 87.4%, Twitter 73.3% (p.6, Table 3)
- Text-only BERT binary: Gab 88.9%, Twitter 70.1% (p.6, Table 3)
- Image-only ResNet-152 binary: Gab 58.7%, Twitter 57.9% (p.6, Table 3)
- Gab binary confusion matrix: 1,470 true negatives / 162 false positives / 167 false negatives / 1,710 true positives (p.8, Table 6)
- ADL 2019 report: 12% jump to 2,107 antisemitism cases in US; 56% rise in assaults vs 2018 (p.1)

## 10. Pitfalls & limitations
- **Keyword bias**: Models learn to classify based on keywords like "zionists", "holocaust", "Hitler", "Torah" — not robust to adversarial paraphrase (p.9)
- **Sarcasm/irony failure**: Subtle or sarcastic hate is systematically misclassified (p.9)
- **Reporting vs. perpetrating confusion**: Posts reporting or condemning antisemitism (e.g., "calling a Jewish man a penny pincher is antisemitic") are misclassified as antisemitic (p.8-9)
- **Multi-screenshot complexity**: Images containing screenshots of other users' content cause errors because the model cannot distinguish between the poster's voice and quoted content (p.9)
- **Class imbalance in subcategories**: Economic (183/118 posts) and Religious (124/144) are much smaller than Political/Racial — performance likely inflated by class imbalance
- **Annotator demographics**: Only 4 annotators, all undergraduate students — no mention of religious/cultural background or expert knowledge of antisemitism
- **English only**: No non-English antisemitic content; misses substantial multilingual manifestations
- **Lexicon seeding bias**: Posts were pre-filtered using a Jewish-reference lexicon, excluding antisemitic content that avoids these terms

## 11. Novel ideas worth stealing
- **Multi-category hate taxonomy**: The 4-category antisemitism breakdown (Political/Economic/Religious/Racial) demonstrates how a single hate type can be meaningfully subdivided into theoretically distinct subtypes. This design move is transferable to other values-alignment benchmarks covering discrimination, harm categorization, or normative violation types.
- **Multimodal annotation at the post level**: Requiring annotators to examine both text and image before labeling (rather than labeling modalities separately) captures the joint meaning of modern social media content. Values benchmarks could adopt this for meme-based moral reasoning evaluations.
- **Confusion-interpretable taxonomy**: The Political-Racial confusion (p.8) is semantically expected (they co-occur in practice), which validates the taxonomy's construct validity by predicting error structure. New benchmarks should design taxonomies with predictable confusion patterns as a validity check.
- **OCR as a third modality**: Adding OCR text from images to text+image fusion substantially improves hate detection. For any benchmark involving visual content, OCR is a cheap signal amplifier.
- **Attention visualization as error analysis**: Using BERTviz and GradCAM to understand model attention (p.7) provides interpretable validation evidence beyond numeric accuracy. Benchmark papers should routinely include this for any classification model.
- **Two-platform dataset design**: Collecting from both a moderated platform (Twitter) and a minimally-moderated one (Gab) creates natural variation in content style and severity, enabling cross-platform generalization tests.

## 12. Notable quotes
- "Unlike other major forms of online abuse like racism, sexism, etc., online antisemitism has not been studied much from a machine learning perspective." (p.1)
- "A post with benign text may as well be antisemitic due to a hateful image." (p.2)
- "It becomes extremely difficult for the system to extract the real intent behind posts expressing views in a subtle manner. This in turn creates a dilemma of freedom of speech/curbing hate speech." (p.9)
- "The improvement in results when using both text and images... is better for Gab overall compared to Twitter. This is because the images on Gab are much more rich and informative compared to those on Twitter." (p.7)

## 13. UNKNOWN / not in extract
- Whether the dataset has been updated since 2021 or expanded beyond the 6,611-post total
- Training/test temporal split details (no dates given for Twitter/Gab collection period)
- Annotator demographics, cultural background, or expertise in antisemitism
- Performance of larger modern LLMs (GPT-4, Claude) on this task
- Whether OCR quality varied systematically across image types (memes vs. news articles vs. screenshots)
- License terms for the released dataset
