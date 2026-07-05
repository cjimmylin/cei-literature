---
stem: "2024-Pfister-SuperGLEBer German Language Understanding Evaluation Benchmark"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices, saturation-discrimination]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 29
dataset_construction: "mixed"
languages: [de]
models_tested: ["gbert-base", "gbert-large", "gottbert-base", "bert-base-german-cased", "german-gpt2", "bloomz-560m", "leo-hessianai-7b", "mt5-small", "mt0-small", "mbart-large-50"]
headline_numbers: ["29 tasks across 4 task types, 10 German-capable models evaluated (p.1)", "leo-7b best on classification 0.810 avg; encoders cluster 0.702-0.724 (p.6)", "gBERT-large fails to consistently beat smaller encoders (p.7)", "seed std dev below 0.012 across tasks/models (p.9)", "(Q)LoRA vs full-precision drop 0.019-0.090 (p.9)"]
---
## 1. Gist
SuperGLEBer is a broad German-language NLU benchmark suite of 29 tasks spanning four task types — text classification, sequence tagging, sentence similarity, and extractive QA — assembled to systematically evaluate 10 German-capable transformer models (4 encoder-only, 3 decoder-only, 3 encoder-decoder) under a uniform training protocol. It matters to values-alignment work mainly for its *cultural-linguistic* coverage (a non-English, German evaluation infrastructure) and because several component tasks are values-adjacent: offensive-language identification (profanity/insult/abuse), toxic-comment identification, and argument mining. It is not a values-alignment benchmark per se, but it is a well-engineered multi-task benchmark whose construction methodology (uniform hyperparameters, seed-stability checks, (Q)LoRA-comparability, per-task-type averaging) is a reusable template.

## 2. Benchmark/eval design features
Constructs: general German NLU capability decomposed into 4 task types. Text classification subsumes toxic/offensive ID, sentiment (document + aspect-based), text-pair matching (query-ad, QA-matching, PAWS-X paraphrase), word-sense disambiguation (incl. literal-vs-figurative verbal idioms), and 7 "other" tasks (fact-claiming, engaging, argument mining, topic relevance, MASSIVE intent, XNLI, news classification). Sequence tagging: NER (5 datasets incl. legal entities in court decisions, EuroParl) plus POS, dependency labels, slot-filling arguments, opinion-term extraction. Sentence similarity: PAWS-X via SentenceBERT triplet loss. QA: GermanQuAD, MLQA (extractive). Inspired by SuperGLUE, tasks deliberately have simple input/output formats and intuitive metrics, ruling out text generation.

## 3. Task format & example item
Mixed formats. Verbatim task examples from prose: offensive-language fine-grained labels "profanity", "insult", "abuse" (p.2); verbal-idiom WSD e.g. "'hold your breath' (by not breathing) vs. 'hold your breath' (waiting in anticipation)" (p.3); MASSIVE slot-filling example "weck mich [date : diese woche] um [time : fünf uhr morgens] auf" (p.4). No single canonical item schema — each of the 29 datasets keeps its native format.

## 4. Scoring / grading methodology
Per-task native metrics, kept from original datasets where available: micro-F1, macro-F1, accuracy (classification/tagging), mean-token-F1 for QA, Pearson correlation on cosine similarity for sentence similarity (range −1 to 1; others 0-1) (p.5). Averaging is hierarchical: sub-tasks of a type (e.g. all NER) averaged first, then across task types, to avoid overweighting types with more datasets (p.5). Missing/errored values treated as 0.0 (p.6). Metric heterogeneity acknowledged — "mixed" columns average across metric kinds, following GLUE/SuperGLUE precedent.

## 5. Dataset construction & provenance
Aggregation of 29 existing public German datasets, not newly authored. Selection criterion: human-translated to German, or manually checked after automatic annotation, or (preferred) a manually German-annotated test set (p.2). Domains span biodiversity literature, EuroParl, Wikipedia/news, German court decisions (19 legal entity classes), hotel/transit reviews, voice-assistant utterances (MASSIVE). Some tasks repurpose cross-lingual datasets (XGLUE, XNLI, MLQA, PAWS-X) monolingually. Open-source framework + public leaderboard at supergleber.professor-x.de; github.com/LSX-UniWue/SuperGLEBer, extensible with new tasks/models.

## 6. Validity evidence
Seed-stability study: gBERT-base + german-GPT2 on 3 tasks, 5 seeds each, average std dev < 0.012 — results not seed flukes (p.9). Comparison to prior reported results where feasible, with caveats about hyperparameter/split/architecture differences; monolingual eval generally beats cross-lingual XGLUE-reported numbers (p.8). (Q)LoRA-vs-full-precision ablation quantifies training-method effect (drop 0.019-0.090, p.9). Uniform protocol (same hyperparameters, seed, batch 8, lr 5e-5, 5 epochs, max 512 tokens, class weighting) controls confounds across models (p.4-5).

## 7. Saturation / discrimination
Good discrimination across architectures: overall averages range widely (e.g. classification: leo-7b 0.810 down to mt5-small 0.380; Table 1, p.6). Encoders cluster tightly (classification 0.702-0.724) showing low discrimination among similar-size encoders. Key finding: bigger is not always better — gBERT-large fails to consistently beat gBERT-base, only clearly winning on sentence similarity (0.651 vs 0.533) (p.7). QA scores compressed (~0.78-0.86 for most). Some headroom remains; no explicit ceiling claim, but toxicity/offensive tasks have low absolute scores (tox macro-F1 avg 0.460 overall, p.6) indicating difficulty.

## 8. Multiturn / agentic aspects
n/a — all tasks single-turn fine-tune-and-predict.

## 9. Key numbers
- 29 tasks, 4 task types, 10 models (p.1).
- Classification averages: leo-7b 0.810, gottbert 0.709, bert-base-german 0.724, gbert-large 0.702, mt5-small 0.462, mt0-small 0.535 (Table 1, p.6).
- Sentence similarity (Pearson): gbert-large 0.651 (best), gbert-base 0.533, mbart 0.620, leo-7b 0.587, mt5 0.321 (p.6).
- QA mean-token-F1: leo-7b 0.864 (best), mbart 0.829, gbert-large 0.826, overall avg 0.798 (p.6).
- Toxicity macro-F1: leo-7b 0.603 (best), gottbert 0.551, gbert-large 0.433 (worst encoder), overall 0.460 (p.6).
- Seed std dev < 0.012 (p.9); (Q)LoRA drop 0.019-0.090 (p.9).
- Training: batch 8, lr 5e-5, 5 epochs, 512 max tokens, 4-bit QLoRA/NF4 (p.4-5).
- gbert-large/base pretrained on 163.4 GB German text; leo-7b LLaMA2-derived (p.4).

## 10. Pitfalls & limitations
Author-admitted: only (Q)LoRA training evaluated (can't speak to full-precision performance in main table); single default hyperparameter config per model, single seed for main results; only smallest sizes evaluated for mt0/mt5/bloomz/leo (compute-prohibitive); mBART hit CUDA-OOM and Bloomz hit ShapeError on some tasks, with missing values scored as 0.0 (biasing those models down) (p.6, p.9-10); flair/SentenceTransformers single-GPU limitation. My observations: averaging across incommensurable metrics (Pearson −1..1 mixed with F1 0..1) is theoretically dubious; treating errored tasks as 0.0 confounds capability with engineering incompatibility; toxicity/offensive tasks reduced to coarse labels; no human ceiling. Values-relevance is incidental, not designed.

## 11. Novel ideas worth stealing
- **Hierarchical per-task-type averaging** to prevent over-represented task families from dominating the aggregate — directly transferable to any multi-construct values benchmark (e.g. don't let 10 toxicity items outweigh 2 fairness items).
- **Uniform training protocol as a comparability guarantee**: fix seed, hyperparameters, and adapter method ((Q)LoRA for all) so cross-model score gaps reflect the model, not the training recipe — a clean fairness principle for leaderboards.
- **Explicit seed-stability sub-study** on a representative model×task subset (5 seeds) to report an average std-dev budget, giving readers an uncertainty floor without full re-runs.
- **(Q)LoRA-vs-full ablation** documenting the systematic offset introduced by parameter-efficient training — worth replicating before comparing PEFT and full-finetune values scores.
- **Provenance-quality gate**: only admit datasets that are human-translated, human-checked, or natively human-annotated in the target language — a concrete anti-machine-translation-contamination rule for building non-English values benchmarks.
- **Living-leaderboard framing**: open framework designed for community-contributed tasks/models rather than a frozen snapshot.

## 12. Notable quotes
"newly introduced German BERT-based models have historically only been evaluated on two tasks each ... which is not enough to get a comprehensive understanding of the models capabilities." (p.1)
"This arguably leads to unreliable results, as the models are evaluated on a task that has been machine-translated sometimes by the very same model these benchmarks were created to be hard to solve" (p.1)
"we did not find a clear advantage for the larger encoder model, as the gBERT-large model is not consistently able to profit from its larger size" (p.1)
"We find the results to be very stable across the different seeds with an average standard deviation of the results being below 0.012 across tasks and models." (p.9)

## 13. UNKNOWN / not in extract
- Full per-task result tables (Appendix D) not in read pages.
- Exact dataset sizes/splits per task (Table 2 appendix) not in read pages.
- License name for the released framework (only "open-source license").
- Human baselines / inter-annotator agreement for component datasets (not reported here).
- Parameter counts per model (Table 3 appendix) not read.
