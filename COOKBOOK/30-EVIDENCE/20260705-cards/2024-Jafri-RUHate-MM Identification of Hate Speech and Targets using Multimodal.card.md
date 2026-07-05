---
stem: "2024-Jafri-RUHate-MM Identification of Hate Speech and Targets using Multimodal"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [validity-psychometrics, cultural-linguistic, normative-ethics, design-space]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 20675
dataset_construction: "crowdsourced"
languages: ["en"]
models_tested: ["BERT", "DistilBERT", "RoBERTa", "ALBERT", "DenseNet-161", "Visformer_small", "MVITV2_base", "VGG19", "ResNet+BERT", "CLIP", "ViLBERT-CC"]
headline_numbers:
  - "20,675 annotated text-image tweet pairs; 4,222 (20.33%) labeled hate speech (p.6)"
  - "Best model ViLBERT-CC: F1=0.848 (hate detection), F1=0.741 (target ID) (p.8)"
  - "Fleiss' Kappa for hate/no-hate: 0.74; for 3-class target: 0.69 (p.5)"
  - "Unimodal text best (BERT): F1=0.798 hate detection, 0.679 target ID (p.8)"
---
## 1. Gist
RUHate-MM introduces a large-scale multimodal (text + image) dataset of 20,675 annotated tweets from the Russia-Ukraine conflict (February–March 2022) for two tasks: binary hate-speech detection (Task A) and identification of hate-speech targets — Individual, Organization, or Community — (Task B). The paper benchmarks unimodal (text-only, image-only) and multimodal (fused text-image) models, finding that multimodal approaches consistently outperform unimodal ones. For values-alignment benchmarking, this dataset exemplifies how political context creates distinct hate-speech patterns, demonstrates the annotation protocol challenges of subjective labels, and quantifies gains from incorporating image information alongside text.

## 2. Benchmark/eval design features
Two-task benchmark:
- **Task A**: Binary classification — Hate vs. No Hate. A post is "Hate" if it contains personal attacks, homophobic abuse, racial abuse, or attack on minorities (see Appendix A.1, p.9).
- **Task B**: Three-class target classification among hate-speech posts — Individual (specific person, e.g., Putin, Biden), Organization (structured group with a name or mission, e.g., NATO), Community (demographic group by race, religion, nationality, interest, etc.).

Key design choices:
- Multimodal input: each item is an (image, tweet-text) pair
- Context-specific: all items are from a single geopolitical event, enabling study of context-driven hate
- Class imbalance: 20.33% hate / 79.67% no-hate in Task A, reflecting real-world distribution (p.6)
- Target sub-distribution: Individual 2,402 / Organization 918 / Community 902 (p.6)
- Evaluation metric: F1-score throughout

## 3. Task format & example item
Binary classification and 3-way classification of tweet + image pairs. Example items shown in Figure 1 (p.2) and Figure 3 (p.6):

**Task A — Hate example**: "[image of derogatory cartoon or inflammatory text] + tweet text with personal attack or dehumanizing language" → label: Hate.

**Task A — No Hate example**: "[image of news photo] + factual tweet about battle developments" → label: No Hate.

**Task B — Individual example**: Post targeting Putin or Biden by name → label: Individual (p.4).

**Task B — Organization example**: Post targeting NATO or a political party → label: Organization (p.4).

**Task B — Community example**: Post targeting Ukrainians, Russians, or refugees as a group → label: Community (p.4).

Verbatim annotation guideline: "A post (text or image or both) that contains hateful content such as a personal attack, homophobic abuse, racial abuse, or attack on minorities." (p.9)

## 4. Scoring / grading methodology
F1-score (macro-average implied) on held-out test set. Models are evaluated separately on:
- F1_HateSpeech: performance on Task A (binary classification)
- F1_Target: performance on Task B (3-class classification)

Training: Adam optimizer, batch size 16 (text/visual) or 4 (CLIP), 3–6 epochs depending on modality (p.7). Text encoders: bert-base-uncased, distilbert-base-uncased, roberta-base, albert-base-v2. Image encoders: densenet161, visformer_small, mvitv2_base, vgg19. Multimodal: ResNet-152+BERT, ViT-Large+ViLBERT-CC, CLIP.

No LLM-judge in scoring; all scoring is automated classification with softmax output.

## 5. Dataset construction & provenance
**Collection**: Twitter API used to crawl from 22 February 2022 to 28 March 2022 using 14 geopolitical keywords (ukraine, putin, russia, zelensky, kyiv, kiev, kremlin, ukrainian, nato, russian, soviet, moscow, kharkiv, donbas). Only English-language tweets with exactly one image were retained (p.3).

**Filtering**: Videos, gifs, audio, blurred images, non-English text in images, and irrelevant posts excluded. "Non-Informative" tweets dropped by annotators (p.3).

**Final size**: 20,675 text-image pairs, all with unique tweet IDs (no duplicates) (p.3).

**Annotation**: 4 annotators (2 male, 2 female; undergraduate, MS, PhD; 10+ years English education; familiar with Russia-Ukraine crisis). Three-phase process: pilot (50 tweets), revised instructions (200 tweets), conflict resolution (p.5). Task A then Task B in sequence.

**Inter-annotator agreement** (Fleiss' Kappa):
- Task A (2-class): κ = 0.74 (final phase)
- Task B (3-class): κ = 0.69 (final phase)
- Pilot-phase pairwise Cohen's Kappa ranged 0.47–0.60 across annotator pairs (p.5)

**Release**: Dataset and resources at https://github.com/Farhan-jafri/Russia-Ukraine.

## 6. Validity evidence
- Inter-annotator reliability is formally measured (Cohen's and Fleiss' Kappa), with final values κ=0.74 (Task A) and κ=0.69 (Task B) representing moderate-to-substantial agreement (p.5).
- Annotation guidelines include clear positive and negative examples, conflict resolution sessions, and explicit handling of sarcasm/satire, which are major edge cases (p.10).
- Criterion validity: ViLBERT-CC outperforms all unimodal baselines, confirming the multimodal signal (p.8).
- Construct validity: TF-IDF analysis confirms that known actors (Putin, Trump, Biden) dominate individual-target posts, consistent with content expectations (p.6–7).
- No external validation against other Russia-Ukraine hate-speech datasets.

## 7. Saturation / discrimination
- Best multimodal model (ViLBERT-CC): F1=0.848 (hate detection), F1=0.741 (target ID) — substantial headroom remains below 1.0 (p.8).
- Unimodal text best (BERT): F1=0.798 hate detection, 0.679 target ID (p.8).
- Visual-only best (DenseNet-161): F1=0.768 hate detection, 0.628 target ID (p.8).
- Task B (target ID) is consistently harder than Task A across all model types, suggesting more discrimination potential in the target classification task.
- Class imbalance (80% No Hate) creates potential for inflated accuracy metrics, though F1 mitigates this somewhat.

## 8. Multiturn / agentic aspects
n/a. Single-turn classification tasks. No interaction protocol or tool use.

## 9. Key numbers
- Total dataset: 20,675 tweets (p.3)
- Hate speech: 4,222 (20.33%); No hate: 16,543 (79.67%) (p.6)
- Target breakdown: Individual 2,402 / Organization 918 / Community 902 (p.6)
- Annotation timeline: 22 Feb 2022 – 28 Mar 2022 (p.3)
- Keywords used for collection: 14 (p.3)
- Annotators: 4, with diverse backgrounds (p.4)
- Fleiss' Kappa Task A: 0.74; Task B: 0.69 (p.5)
- Pilot-phase Cohen's Kappa range: 0.47–0.60 (p.5)
- Final-phase Cohen's Kappa range: 0.71–0.81 (p.5)
- ViLBERT-CC F1_HateSpeech: 0.848 (p.8)
- ViLBERT-CC F1_Target: 0.741 (p.8)
- BERT F1_HateSpeech: 0.798; F1_Target: 0.679 (p.8)
- ResNet+BERT F1_HateSpeech: 0.806; F1_Target: 0.700 (p.8)
- CLIP F1_HateSpeech: 0.826; F1_Target: 0.719 (p.8)

## 10. Pitfalls & limitations
- **Single event, single platform**: Dataset is limited to Twitter posts during a specific 35-day period. Generalizability to other political conflicts, platforms, or time periods is unverified (Appendix A.2, p.10).
- **English only**: Excludes Russian- and Ukrainian-language posts, which may carry different hate-speech patterns (p.10).
- **Coarse target taxonomy**: Individual/Organization/Community may not capture more nuanced targeting (e.g., religion-based targeting vs. nationality-based targeting within Community) (p.10).
- **Annotation subjectivity**: Sarcasm, political satire, and humor are difficult to annotate consistently; guidelines address this but kappa values (~0.69–0.74) indicate remaining disagreement (p.5, p.10).
- **Class imbalance**: 80% non-hate label may inflate metrics for naive classifiers; not discussed in depth.
- **No cross-platform validation**: Unclear whether models trained on this dataset transfer to other platforms (Facebook, Telegram, etc.).
- **Ethical concerns acknowledged but not addressed**: Authors note potential misuse, bias, and privacy implications of hate-speech detection tools (p.10) without mitigation strategies.

## 11. Novel ideas worth stealing
1. **Three-phase iterative annotation with explicit conflict resolution**: The pilot → revised instructions → group conflict resolution sequence is a replicable protocol for any subjective annotation task in values-alignment benchmarks. Kappa improved from ~0.50 to ~0.76 across phases — quantifying the value of iteration.
2. **Multimodal benchmark with explicit target taxonomy**: For AI-safety evaluation of multimodal models, having both a binary harmful/benign label AND a structured target taxonomy (Individual/Organization/Community) doubles the benchmark's diagnostic value without doubling annotation cost.
3. **Real-world event anchoring for ecological validity**: Anchoring a dataset to a specific real-world geopolitical event produces naturally diverse and contextually authentic test cases, avoiding the artificiality of constructed prompts. Future values benchmarks could similarly be anchored to specific real-world contexts.
4. **TF-IDF analysis of class-discriminative vocabulary**: The paper's use of TF-IDF per class (Table 4) as exploratory data analysis quickly reveals what lexical features drive model decisions — a cheap diagnostic for any values-relevant dataset.
5. **Explicit handling of sarcasm/satire in annotation guidelines**: Since sarcasm can mask harmful content, annotation guidelines for any nuanced values benchmark should include explicit examples of sarcasm/satire with rulings, as done in Appendix A.1 (p.9–10).

## 12. Notable quotes
- "Our experiments analysis shows that to address issues of hate speech, an integration of multimodal inputs is important." (p.1)
- "The benchmarked evaluations reveal areas for improvement in accurately identifying hate speech and its targets, indicating the intricate nature of the dataset." (p.8)
- "Sarcasm and satire can be used to mask hate speech, making it more subtle and harder to detect." (p.10)
- "The dataset statistics represent a true distribution in a real-world scenario where many posts are neutral, and only some are related to hate speech." (p.6)

## 13. UNKNOWN / not in extract
- Whether the dataset includes full tweet images (as URLs or binary files) given Twitter API constraints
- Train/validation/test split sizes
- Macro vs. weighted F1 computation details
- Whether the 2K held-out test split matches the full 20,675 or is a separate split
- Cost and time of annotation process
- License for dataset distribution
- Whether models were evaluated on zero-shot or fine-tuned settings
- GPU hardware for training (beyond "Tesla T4 or Tesla V100" mentioned generally)
