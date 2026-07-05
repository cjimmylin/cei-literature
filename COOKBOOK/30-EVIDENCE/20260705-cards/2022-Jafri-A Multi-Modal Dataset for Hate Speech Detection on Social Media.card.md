---
stem: "2022-Jafri-A Multi-Modal Dataset for Hate Speech Detection on Social Media"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [design-space, validity-psychometrics]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 5680
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: ["LSTM", "BERT", "RoBERTa", "VGG-19", "ResNet", "DenseNet", "VisualBERT", "CLIP"]
headline_numbers:
  - "5,680 text-image tweet pairs; 746 hate (13.13%) / 4,934 no hate (86.87%) (p.3, Table 2)"
  - "CLIP achieves best F1-score of 0.89 on the multimodal task (p.4, Table 4)"
  - "RoBERTa achieves best unimodal text F1-score of 0.83 (p.4, Table 4)"
  - "Final annotation phase inter-annotator agreement κ=0.87–0.90 across all annotator pairs (p.4, Table 3)"
---
## 1. Gist
Thapa, Shah, Jafri, Naseem, and Razzak present a multimodal hate speech dataset of 5,680 English Twitter text-image pairs focused on the Russia-Ukraine war (February–March 2022). The dataset is annotated with binary hate/no-hate labels and is notable for (1) its conflict-context framing, (2) its explicit multimodal design combining tweet text and attached images, and (3) its use of a structured three-phase annotation process with strong final inter-annotator agreement (κ ≈ 0.89). The paper establishes baselines using both unimodal (text-only, image-only) and multimodal models. For values-alignment benchmarking, this paper is primarily relevant as an example of conflict-context hate speech dataset construction and as a demonstration that multimodal models substantially outperform unimodal models on real-world hate speech detection in politically charged settings.

## 2. Benchmark/eval design features
The paper contributes a binary-classification hate speech benchmark with the following characteristics:
- **Coverage**: Tweets collected 2022-02-22 to 2022-03-28 using 14 Russia-Ukraine war keywords (ukraine, putin, russia, zelensky, kyiv, kremlin, nato, etc.)
- **Modality**: Text+image pairs only (no video/animation)
- **Label set**: Binary — "hate" (personal attack, homophobic abuse, racial abuse, attack on minority) vs. "no hate" (objective reporting, no offensive content)
- **Annotation rule**: At least one component (text OR image) representing hate is sufficient to label as hate
- **Class distribution**: 13.13% hate (realistic real-world distribution)
- **Baselines**: 3 unimodal text models (LSTM, BERT, RoBERTa), 3 unimodal image models (VGG-19, ResNet, DenseNet), 3 multimodal models (ResNet+BERT, VisualBERT, CLIP)

## 3. Task format & example item
Binary classification of tweet text-image pairs. Example from the paper (p.3):
- Figure 1a: Text expresses solidarity with Ukraine; image is the Ukrainian flag → labeled "No Hate"
- Figure 1b: Text demeans Donald Trump by stating he belongs to Siberia; image is edited to be demeaning → labeled "Hate"

Example annotation instructions (Table 1, p.3):
- Hate: "A post (text or image or both) contains a hateful content such as personal attack, homophobic abuse, racial abuse, or attack on minority"
- No Hate: "A post (text or image or both) reports the events or others' opinions objectively and contains no offensive or hateful content."

## 4. Scoring / grading methodology
Classification performance evaluated with precision, recall, and F1-score using grid-search-optimized hyperparameters. Test set not explicitly separated in the paper's description, but results are presented in Table 4.

## 5. Dataset construction & provenance
- **Collection**: Twitter API, keywords crawled Feb–Mar 2022, filtered to English image-text pairs (no videos/animations)
- **Size**: 5,680 labeled tweets; 746 hate, 4,934 no hate (Table 2)
- **Annotation process**: Three phases — (1) pilot on 50 tweets for instruction clarity; (2) all 4 annotators label 200 tweets to verify revised instructions; (3) group discussion of conflicts followed by full annotation. Uncertain items labeled "Non-Informative" and dropped.
- **Annotators**: Team of 4 male and female volunteers with undergraduate–PhD qualifications; NLP researchers among them. No payment reported.
- **Inter-annotator agreement evolution**: Pilot phase κ=0.50–0.63; final phase κ=0.87–0.90 (Table 3)
- **Release**: Dataset available at github.com/therealthapa/emnlp-case2022

## 6. Validity evidence
- Final inter-annotator agreement is strong (κ=0.87–0.90 in final annotation phase), representing a substantial improvement from pilot phase (κ=0.50–0.63), confirming that iterative instruction clarification was effective.
- Dataset reflects a realistic real-world class imbalance (13.13% hate), which the authors argue validates ecological validity.
- Privacy: Tweet IDs released rather than raw content; original authors retain delete control.

## 7. Saturation / discrimination
Best multimodal model (CLIP) achieves F1=0.89 with F1-score for hate class not separately reported. The class imbalance (86.87% no-hate) means aggregate metrics inflate; the task has significant headroom especially for minority hate class recall. Multimodal models consistently outperform unimodal ones, indicating the task is not yet saturated.

## 8. Multiturn / agentic aspects
n/a. Single-turn binary classification.

## 9. Key numbers
- 5,680 tweet text-image pairs total (p.1)
- 746 hate (13.13%), 4,934 no hate (86.87%) (p.3, Table 2)
- Average ~60–64 characters per tweet, ~9–10 words per tweet (p.3, Table 2)
- 4 annotators; annotation conducted in 3 phases
- Final annotation κ range: 0.87–0.90 across all 6 annotator pairs (p.4, Table 3)
- Pilot annotation κ range: 0.50–0.63 (p.4, Table 3)
- CLIP F1=0.89 (best overall); VisualBERT F1=0.86; ResNet+BERT F1=0.85 (p.4, Table 4)
- RoBERTa (text only) F1=0.83 (best unimodal); DenseNet/ResNet (image only) F1=0.77 (p.4, Table 4)
- LSTM F1=0.79 (p.4, Table 4)

## 10. Pitfalls & limitations
- Small dataset (5,680 items) relative to task complexity and potential distributional variety.
- Annotation is subjective; authors acknowledge potential bias despite diverse annotator team and iterative process.
- Domain-specific (Russia-Ukraine war) — may not generalize to other conflict contexts or hate speech categories.
- Binary label schema misses nuance (severity, type of hate, targeted group identity).
- Only English tweets collected; hate speech in other languages during the same conflict is absent.
- Class imbalance (86.87% no-hate) makes model evaluation using aggregate F1 potentially misleading for hate class performance.
- Annotators are described as volunteers who did not receive remuneration, raising potential selection bias concerns.
- The paper does not report separate precision/recall for hate vs. no-hate class, making it difficult to assess false-negative rate specifically.

## 11. Novel ideas worth stealing
1. **Conflict-context hate speech benchmark.** Framing a hate speech dataset around a specific real-world geopolitical conflict (rather than platform-generic content) creates a more ecologically coherent benchmark with consistent domain context. Values-alignment benchmarks could similarly use recent, salient events as coherent evaluation contexts.
2. **Three-phase iterative annotation with κ tracking.** The pilot → full annotation → group discussion conflict resolution pipeline, with explicit κ measurement at each stage, is a best-practice protocol worth replicating. The dramatic improvement from κ≈0.55 (pilot) to κ≈0.89 (final) demonstrates that iterative instruction clarification substantially improves data quality.
3. **Multimodal evaluation as a more complete test.** Real social media hate speech often relies on image-text interplay (irony, implication, context). A values-alignment benchmark that assesses only text-based reasoning misses a substantial real-world harm vector. The CLIP-based multimodal architecture achieving best performance validates this approach.
4. **Minimum one-modality hate criterion.** The annotation rule that either text OR image being hateful triggers a hate label is a useful operationalization for multimodal benchmarks that avoids requiring both modalities to independently express hate.

## 12. Notable quotes
- "In political situations pertaining to invasion, the situation becomes even worse. Social media sometimes get polarized into the ones supporting the invasion and the ones opposing the invasion." (p.1)
- "Our experimental analysis shows that both modalities (text and images) are important for the task." (p.2)
- "The annotation is very subjective and hence we can expect some bias in the annotation." (p.5)
- "The dataset statistics represent a true distribution in a real-world scenario where many posts are neutral, and only some are related to hate speech." (p.3)

## 13. UNKNOWN / not in extract
- Train/test/validation split sizes or methodology.
- Per-class precision/recall/F1 for the hate label specifically.
- Whether the dropped "Non-Informative" tweets are reported in any final count.
- Whether any images were pre-processed or had metadata stripped before annotation.
- The number of tweets initially crawled before filtering to image-text pairs.
