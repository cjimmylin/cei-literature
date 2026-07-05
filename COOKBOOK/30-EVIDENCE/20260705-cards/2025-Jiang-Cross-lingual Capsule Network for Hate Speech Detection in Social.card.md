---
stem: "2025-Jiang-Cross-lingual Capsule Network for Hate Speech Detection in Social"
reader_model: "opus"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: null
dataset_construction: "scraped"
languages: [en, es, it]
models_tested: ["CCNL", "CCNL-Ex", "SVM", "CNN", "BiLSTM", "CapsNet", "LASER", "MUSE", "mBERT", "XLM-R", "JL-HL"]
headline_numbers: ["CCNL-Ex beats all 10 baselines on all 6 language pairs (p.4)", "Best macro-F1 0.736 (ES→IT) and 0.729 (EN→ES) for CCNL-Ex (p.4)", "CCNL 7-9% absolute gain over JL-HL on Italian-target pairs (p.5)", "Datasets: EN 3200/800/1000, ES 2646/661/831, IT 3200/800/1000 train/val/test (p.4)"]
---
## 1. Gist
This is a 2021 methods paper (published at ACM Hypertext '21; the "2025" stem is a filing artifact) proposing CCNL-Ex, a cross-lingual capsule network for misogyny/hate-speech detection across English, Spanish, and Italian (p.1). It is NOT a values-alignment benchmark and does not test LLMs; it is a supervised classification model that adapts hate-speech resources from a source language to a target language via machine translation, BiLSTM feature extraction, capsule-network dynamic routing, and infusion of hate-specific lexicons (HurtLex, sentiment lexicon) into word embeddings (p.2-3). Relevance to values-alignment work is indirect: it exemplifies cross-lingual/cultural-linguistic transfer for detecting gendered online hate in low-resource languages, and its error taxonomy (implicit hate, translation error) is instructive for multilingual safety evaluation.

## 2. Benchmark/eval design features
Not a benchmark; a model + evaluation on existing benchmark datasets (AMI@Evalita2018, AMI@IberEval2018). Core claims/contributions: (1) first application of capsule networks to cross-lingual hate speech; (2) infusion of hate-related lexical semantics into pretrained embeddings; (3) SOTA over 10 baselines on all 6 EN/ES/IT language pairs; (4) ablation of each architectural layer (p.1). The construct measured is binary misogyny (misogynistic vs non-misogynistic) transferred across languages using a two-parallel (source + translated target) architecture.

## 3. Task format & example item
n/a (not an item-based benchmark). Task is binary tweet classification. Error-analysis examples (p.5, Table 4) include a Spanish tweet: "If you wear shorts like this, in the street, what do you expect them to say? Bullying? Or Provocation..." (GT hateful=1, predicted 0, error type: implicit hate).

## 4. Scoring / grading methodology
Macro-averaged F1 is the sole evaluation metric across all experiments (p.4). Standard supervised classification against the AMI gold binary labels; softmax output layer over concatenated source+target representations (p.3). Trained with FastText 300-d embeddings, BiLSTM (128+128 units), 10 capsules of dim 16, 5 routing iterations, Adam lr 0.0001, dropout 0.4, batch 8 (p.4).

## 5. Dataset construction & provenance
Uses AMI (Automatic Misogyny Identification) shared-task Twitter datasets: AMI@Evalita2018 (English, Italian) and AMI@IberEval2018 (Spanish, English), same annotation scheme, binary labels (p.4). English taken from Evalita only for size balance. Splits (Table 1, p.4): EN train 3200/val 800/test 1000; ES 2646/661/831; IT 3200/800/1000. Misogynistic-text rate ~44.6-50.9%. Parallel corpora created via Google Translate. Lexicons: HurtLex (6,287 EN / 3,565 ES / 4,286 IT words) and a multilingual sentiment lexicon (2,955 EN / 2,720 ES / 2,893 IT negative words) (p.4).

## 6. Validity evidence
Comparative validity via 10 competitive baselines (SVM, CNN, BiLSTM, CapsNet, LASER, MUSE, mBERT, XLM-R, JL-HL, Majority) across all 6 language pairs (Table 2, p.4). Ablation studies (Table 3, p.5) isolate the contribution of the parallel framework, LSTM layer, and capsule layer, and compare feature extractors (none/CNN/GRU/LSTM), supporting the design's construct validity. No inter-annotator reliability reported (inherited from AMI tasks). No human baseline.

## 7. Saturation / discrimination
Not framed as saturation. Absolute macro-F1 is modest (0.519-0.736 for CCNL-Ex), showing cross-lingual hate detection is far from solved—substantial headroom (p.4). EN→IT is hardest (many baselines near 0.2-0.4; CCNL 0.584). Lexicon infusion helps except when Italian is target (lexicon quality limits gains) (p.5). Wide baseline spread indicates the task discriminates model quality.

## 8. Multiturn / agentic aspects
n/a. Single-instance text classification; no interaction, tools, or agents.

## 9. Key numbers
- CCNL-Ex macro-F1 by pair (Table 2, p.4): ES→EN 0.651, EN→ES 0.729, IT→EN 0.629, EN→IT 0.519, ES→IT 0.736, IT→ES 0.670.
- Best baseline JL-HL always below CCNL-Ex; CCNL gains 7-9% absolute over JL-HL on EN→IT and ES→IT (p.5).
- Majority baseline ~0.33-0.35 macro-F1 (p.4).
- Train/val/test: EN 3200/800/1000, ES 2646/661/831, IT 3200/800/1000 (p.4).
- Misogynistic-text rate: train 44.6-49.9%, test 46.0-50.9% (p.4).
- HurtLex words: 6,287 EN, 3,565 ES, 4,286 IT (p.4).
- Config: 10 capsules dim 16, 5 routing iters, FastText 300-d, BiLSTM 256 units (p.4).

## 10. Pitfalls & limitations
Author-noted: machine translation (Google Translate) is imperfect for informal social-media text and hashtags, causing OOV/translation errors; Italian lexicon quality limits lexicon-infusion gains; future work needs "culturally grounded context" for parallel corpora and more languages/datasets (p.5-6). Four error types identified: implicit hate, over-reliance on hateful keywords, lack of world/event prior knowledge, erroneous translation (p.5). Observed limits: only 3 languages, only gender-based (misogyny) hate, dated (2021, pre-LLM) methods, no statistical significance testing, small test sets (~831-1000).

## 11. Novel ideas worth stealing
- Lexicon-into-embedding infusion via retrofitting (Faruqui et al.) using domain-specific hate lexicons (HurtLex) + SenticNet expansion—a cheap way to inject value/harm priors into a detector, portable to LLM-era safety classifiers (p.3).
- Two-parallel source + machine-translated-target architecture for zero-resource cross-lingual transfer—relevant template for extending an English values benchmark to low-resource languages (p.2-3).
- The four-way error taxonomy (implicit hate / keyword over-reliance / missing world knowledge / translation error) is a reusable qualitative failure-mode schema for auditing multilingual hate/safety evaluations (p.5).
- Explicit demonstration that lexicon infusion HURTS when the target-language lexicon is low quality—a cautionary lesson: cross-lingual resource quality must be verified before use (p.5).
- Cross-lingual robustness framing (all 6 directed pairs) as a generalization stress test rather than a single-language score.

## 12. Notable quotes
- "Most hate speech detection research focuses on a single language, generally English, which limits their generalisability to other languages." (p.1)
- "using machine translation resources such as Google translate is not always a perfect option with very informal language such as those used on social media for hate speech." (p.5)
- "The exception to the trend showing a better performance for lexicon-based methods is for the two language pairs that have Italian as the target... likely due to limitations in the Italian language lexicons." (p.5)
- "(a) Implicit hate: Those lacking explicit hateful content or context in the post" (p.5)

## 13. UNKNOWN / not in extract
- Total combined dataset size across the three languages (only per-language splits given; dataset_size left null).
- Statistical significance / variance of the macro-F1 results (single runs reported).
- Exact AMI annotation guidelines and inter-annotator agreement (inherited, not restated).
- Whether any transformer/LLM was fine-tuned beyond mBERT/XLM-R feature use.
- Licensing of the AMI datasets and lexicons.
