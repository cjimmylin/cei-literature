---
stem: "2019-Corazza-Cross-Platform Evaluation for Italian Hate Speech Detection"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, contamination-robustness, design-space]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: 16350
dataset_construction: "scraped"
languages: [Italian, it]
models_tested: ["Modular Keras GRU-200 + FFN-500 (Inria-FBK architecture)"]
headline_numbers: ["4 platforms: Twitter (4,000), Facebook (4,000), WhatsApp (1,640), Instagram (6,710) (p.3-4)", "Twitter macro-F1 0.798 single-platform vs 0.782 multi-platform (p.6)", "Facebook macro-F1 0.822 multi vs 0.812 single-platform (p.6)", "WhatsApp macro-F1 0.796 multi vs 0.754 single-platform (p.6)"]
---
## 1. Gist
This is an empirical NLP systems paper (not a benchmark-introduction paper in the values-alignment sense), studying cross-platform robustness of Italian hate-speech detection. It asks whether combining platform-dependent training datasets (Facebook, Twitter, Instagram, WhatsApp) helps single-platform detection, using a fixed modular neural classifier so that only features/preprocessing/training-mix vary. Its relevance to values-alignment benchmarking is as a case study in domain/distribution shift and dataset heterogeneity: it shows that "hate speech" as a construct does not transfer cleanly across platforms (class balance, message length, emoji density all differ), and that naively pooling data can hurt. This is a cautionary lesson for anyone building cross-source values/safety benchmarks. It also contributes a new manually-annotated Italian Instagram hate-speech set.

## 2. Benchmark/eval design features
Construct: binary presence/absence of hate speech (or, for WhatsApp, cyberbullying expression) per social-media message. It is a classification study rather than a held-out challenge benchmark. Key design variable is the training-data composition: Multi-platform (all pooled), Multi-platform filtered by length (<=280 chars to mimic Twitter), and Same-platform. Secondary ablations: generic vs Twitter-domain fastText embeddings; emoji transcription on/off; Hurtlex hurtful-word lexicon (17 categories, from De Mauro's Italian hate lexicon) vs social-media surface features (counts of hashtags, mentions, punctuation, emojis, uppercase words). The central finding is that cross-platform data pooling helps all platforms except Twitter, where in-domain-only training wins.

## 3. Task format & example item
n/a as a benchmark item format, but example annotated instances are given. Twitter (hateful): "altro che profughi? sono zavorre e tutti uomini" (EN: "other than refugees? they are ballast and all men") (p.3). WhatsApp (cyberbullying): "fai schifo, ciccione!" (EN: "you suck, fat guy") (p.4). Instagram (hateful): "Sei una troglodita" (EN: "you are a caveman") (p.4).

## 4. Scoring / grading methodology
Automatic binary classifier evaluated by F1 per class (F1 no-hate, F1 hate) and Macro-AVG F1 (Table 1, p.6). EVALITA-provided test sets used for Twitter/Facebook (20% of dev held out for validation); for Instagram/WhatsApp a 60/20/20 train/val/test split with sklearn train_test_split, seed 42 (p.5).

## 5. Dataset construction & provenance
Four Italian datasets: (1) Twitter — EVALITA-2018 HaSpeeDe, 4,000 tweets (2,704 neg / 1,296 pos) (p.3); (2) Facebook — EVALITA-2018 HaSpeeDe, 4,000 comments from 99 crawled posts (1,941 neg / 2,059 pos) (p.3); (3) WhatsApp — repurposed pre-teen cyberbullying corpus (Sprugnoli et al. 2018), token-level annotation collapsed to 1,640 messages (595 pos) by joining same-author sentences (p.4); (4) Instagram — newly randomly collected from student profiles, 6,710 messages (6,510 neg / 200 pos), manually annotated by the authors (p.4). Severe and inconsistent class imbalance across sources (Instagram only ~3% positive). fastText embeddings (generic Common Crawl+Wikipedia vs author-trained on Italian tweets), size 300 (p.4). CC BY 4.0 (p.2).

## 6. Validity evidence
Limited. No inter-annotator agreement reported for the new Instagram annotation. The construct "hate speech" is operationalized differently per platform (WhatsApp uses a cyberbullying token-level scheme collapsed to message level), threatening construct comparability. The authors themselves note datasets vary too broadly in size for a "fair comparison" (p.6-7). No human baseline.

## 7. Saturation / discrimination
Not a saturation study, but the F1-hate scores reveal difficulty variation: Instagram F1-hate only 0.432 despite F1-no-hate 0.984 (driven by 3% positive rate), showing extreme class imbalance kills minority-class performance (p.6). Facebook (balanced, ~51% pos) reaches F1-hate 0.892 (p.6). Multi- vs single-platform differences are small (a few macro-F1 points) except WhatsApp (+0.042), the smallest set (p.6).

## 8. Multiturn / agentic aspects
n/a.

## 9. Key numbers
- Dataset sizes: Twitter 4,000; Facebook 4,000; WhatsApp 1,640 (595 pos); Instagram 6,710 (200 pos) (p.3-4).
- Facebook test set 68% hate vs Twitter 32% hate (class-distribution mismatch) (p.3).
- Cross-HaSpeeDe drop: best system 0.8288 F1 in-domain Facebook -> 0.6068 tested on Twitter (Cimino et al. 2018) (p.3).
- Instagram: Multi-platform macro-F1 0.708 (F1-hate 0.432) vs single 0.702 (p.6).
- Facebook: Multi 0.822 vs single 0.812 (p.6).
- WhatsApp: Multi 0.796 vs single 0.754 (p.6).
- Twitter: single-platform 0.798 > filtered-multi 0.789 > multi 0.782, all with Hurtlex+no-emoji (p.6).
- Architecture: FFN hidden 500 ReLU, GRU size 200, no dropout, sigmoid output, binary cross-entropy (p.4-5).

## 10. Pitfalls & limitations
Author-admitted: dataset sizes vary too broadly for fair comparison (p.6-7); improvement from pooling "not always sizeable enough to be useful" (p.7); only tested pooling-all, not all pairwise combinations. Observable: extreme and inconsistent class imbalance (Instagram 3% positive) makes cross-platform macro-F1 hard to compare; the WhatsApp "cyberbullying" label is not the same construct as "hate speech"; Hurtlex adapted, Ekphrasis hashtag splitter only supports English (adapted via Google ngrams) — noisy Italian preprocessing; single random seed, no significance testing across runs.

## 11. Novel ideas worth stealing
- Holding the model architecture and hyperparameters fixed while varying only the training-data mixture and feature set — a clean ablation design to attribute performance to data provenance rather than modeling, useful for probing benchmark robustness.
- Length-filtering the training pool (<=280 chars) to make out-of-platform data distributionally closer to the target platform — a lightweight domain-matching trick when pooling heterogeneous sources.
- Using a lexicon-derived "hurtfulness" score (Hurtlex, 17 categories) as an interpretable auxiliary feature — transferable as an interpretable signal in values/toxicity benchmarks.
- Documenting per-platform class-balance and length statistics up front as explanatory covariates for transfer failure — a good habit for any multi-source benchmark to surface distribution shift.
- The finding that domain-specific (in-platform) embeddings always beat generic ones is a reusable reminder that representation provenance matters for social-language constructs.

## 12. Notable quotes
- "the issue of developing hate speech detection systems that are robust across different platforms is still an unsolved problem." (p.2)
- "combining such platform-dependent datasets ... is beneficial, although their impact varies depending on the social network under consideration." (p.2)
- "learning to detect hate speech on the short length interactions that happen on Twitter does not benefit from using data from other platforms." (p.6)
- "the size of the datasets varies too broadly to allow for a fair comparison, and we would need to extend some of the datasets." (p.6-7)

## 13. UNKNOWN / not in extract
- Inter-annotator agreement for the new Instagram annotations.
- Exact hyperparameter search / whether hyperparameters were tuned per platform (stated as fixed from EVALITA submission).
- Statistical significance of the multi- vs single-platform differences.
- Full pairwise cross-platform transfer matrix (deferred to future work).
- Number of annotators and annotation guidelines for the Instagram set.
