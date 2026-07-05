---
stem: "2023-Haq-Pashto Offensive Language Detection A Benchmark Dataset and"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices, contamination-robustness]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 34400
dataset_construction: "crowdsourced"
languages: [ps]
models_tested: ["Pashto-BERT", XLM-R, CNN, LSTM, BiLSTM, GRU, BiGRU, Word2Vec, fastText, GloVe]
headline_numbers: ["Ps-BERT F1 94.34%, accuracy 94.77% (p.17)", "XLM-R F1 94.01%, accuracy 94.48% (p.18)", "LSTM+fastText F1 93.08% (p.18)", "CNN+Word2Vec lowest F1 89.08% (p.18)", "POLD 34,400 tweets: 12,400 offensive / 22,000 non-offensive (p.8)"]
---
## 1. Gist
This is the dedicated journal paper (PeerJ CS, CC-BY 4.0) for POLD, the Pashto Offensive Language Dataset, and the monolingual Pashto BERT (Ps-BERT). It builds a benchmark of 34,400 manually-labeled Pashto tweets (offensive vs not-offensive) and evaluates 17 model configurations — five neural nets × three static embeddings plus two transformer transfer-learning approaches (XLM-R and from-scratch Ps-BERT) (p.1). It matters to values-alignment benchmarking as a rigorous, well-documented example of building a *safety-relevant content-moderation* benchmark in a low-resource, culturally-distinct language, with explicit attention to what counts as "offensive" across cultural norms, annotator bias mitigation, and class imbalance reflecting real-world base rates.

## 2. Benchmark/eval design features
Construct: binary offensiveness of a Pashto social-media utterance, grounded in documented sub-types — hate speech, profanity/vulgarity, aggression/cyberbullying (p.3). Answer space: 2 classes {offensive=1, not-offensive=0}. Item = one cleaned tweet (avg 18 tokens). The paper foregrounds cultural relativity of offensiveness: "what may be considered offensive in one context or community may not be offensive in another" (p.2), then anchors annotation to OffensEval2019 guidelines for consistency. Class distribution is deliberately imbalanced (~36% offensive) to mirror real base rates.

## 3. Task format & example item
Binary text classification. No single verbatim tweet is reproduced in the extract (offensive examples withheld); the input is a preprocessed Pashto tweet and the output is label 1/0 (p.7). Word-frequency diagrams of most-frequent words in offensive vs normal tweets are shown (Fig. 3, p.9) but individual items are not quoted.

## 4. Scoring / grading methodology
Classifier evaluation on a fixed 10% test set using precision, recall, F1-score, accuracy (Eqs 1–4, p.17). F1 (harmonic mean of precision/recall) is emphasized as the headline metric because the dataset is imbalanced (p.17). Same train/val/test split used uniformly across all 17 models for fair comparison (p.8-9). Error analysis via per-model confusion matrices (p.19).

## 5. Dataset construction & provenance
Seed list of 2.3K offensive words+patterns (spanning major Pashto dialects, plus non-lexical patterns like personal pronouns to reduce bias) used with Twitter Search API → ~300K raw tweets (Jan 10–Feb 10 2023); offensive ratio raised to ~28% by seed filtering (p.7). Cleaning: remove HTML/URLs/usernames/diacritics, normalize digits to Pashto, drop duplicates and tweets <10 or >150 chars → 70K → 35K sampled for annotation (p.7). Two-stage annotation: stage 1, three annotators label all tweets independently, 31,300 (~91%) reach 100% inter-annotator agreement; stage 2, the ambiguous 9% get two more annotators, decided by majority vote among five (p.8). Final POLD = 34,400 (12,400 offensive / 22,000 non), split 80/10/10 with proportional class representation (Table 1, p.8). Corpus for pretraining: 15M tokens from news (~40%), Wikipedia, books, tweets (p.6).

## 6. Validity evidence
Inter-annotator agreement: 91% of tweets reach 100% agreement among 3 annotators in stage 1; remaining 9% resolved by 5-way majority (p.8) — a concrete, if coarse, reliability signal. Criterion comparison: POLD situated against 9 other offensive-language datasets (Arabic, Chinese, Greek, Turkish, English, Spanish, Indonesian, Persian) showing competitive size (Table 2, p.10). Annotators are all native Pashto-speaking university graduates following OffensEval2019 definitions (p.8). Ablation across embeddings and architectures provides construct discrimination evidence.

## 7. Saturation / discrimination
Model scores cluster tightly at the top: transformer models 94.0–94.3% F1, RNN family 91.5–93.1%, CNN+Word2Vec floor at 89.08% — a ~5-point spread indicating the benchmark is already near-saturated for strong models but still separates weak from strong (p.18). Differences among RNNs and between uni/bidirectional variants are "not significant" (p.18), limiting fine discrimination among mid-tier models.

## 8. Multiturn / agentic aspects
n/a — single-shot tweet classification, no interaction or tool use.

## 9. Key numbers
- Ps-BERT: precision 94.22%, recall 94.47%, accuracy 94.77%, F1 94.34% (Table 5, p.18).
- XLM-R: precision 93.98%, recall 94.05%, accuracy 94.48%, F1 94.01% (p.18).
- LSTM+fastText best non-transformer: F1 93.08%, acc 93.72% (p.18).
- CNN+Word2Vec lowest: F1 89.08%, acc 90.29% (p.18).
- POLD 34,400 (train 27,520 / val 3,440 / test 3,440); 12,400 offensive / 22,000 non (Table 1, p.8).
- Seed list 2.3K terms; ~300K raw → 70K → 35K annotated; ~28% offensive after filtering (p.7).
- Ps-BERT: 12 layers, 768 hidden, 12 heads, 110M params vs XLM-R 270M params, trained on 2.5TB CommonCrawl/100 langs (p.14).
- Ps-BERT pretraining: 15M tokens, ~1h on one Tesla P100, LR 1e-4, batch 32, seq 128 (p.15).

## 10. Pitfalls & limitations
Author-admitted: cultural/contextual variability of "offensive" (p.2); class imbalance requires careful metric choice (p.8); no pre-existing Pashto baseline to compare against (p.6). Observable flaws: reliability reported only as %-agreement, not kappa/alpha; seed-list construction biases the dataset toward known offensive vocabulary, undercounting novel/implicit toxicity (contamination-robustness risk); single fixed split with no cross-validation or confidence intervals; Ps-BERT vs XLM-R gap (0.33 F1) is within plausible noise yet framed as a win; test items withheld, so external audit of label quality is impossible from the paper.

## 11. Novel ideas worth stealing
- **Two-stage triaged annotation**: cheaply label the ~90% high-agreement "easy" items with a small panel, then escalate only the contested minority to a larger jury — an efficient reliability-aware protocol for any subjective values-labeling task (p.8).
- **Base-rate-faithful imbalance**: deliberately keep the natural ~36% positive rate rather than balancing, forcing models (and metrics) to confront real deployment distributions (p.8).
- **Dialect-inclusive seed lists**: engineer the sampling seed to span all major dialects and include non-lexical structural patterns, explicitly to *reduce* selection bias — a template for culturally representative value benchmarks (p.7).
- **Sub-word embeddings for obfuscation robustness**: fastText handles deliberately altered/half-written slurs that break word-level embeddings — a concrete robustness lever for safety benchmarks facing adversarial spelling (p.18-19).
- **Cross-dataset size/composition comparison table** (Table 2) as a standard way to situate a new benchmark's coverage against the field (p.10).

## 12. Notable quotes
- "The definition of offensive language can vary depending on cultural and societal norms, and what may be considered offensive in one context or community may not be offensive in another." (p.2)
- "In the first stage of annotation, 31,300 tweets (around 91%) were annotated with 100% inter-annotator agreement." (p.8)
- "the fine-tuned Ps-BERT model yields the best performance and achieves an F1-score of 94.34% with an accuracy of 94.77%." (p.17)
- "there is a significant difference between the resources utilized to pre-train these models. XLM-R has been pre-trained on a huge corpus of billions of tokens ... In contrast, the Ps-BERT model was trained on a corpus of 15 million tokens." (p.17)

## 13. UNKNOWN / not in extract
Verbatim example tweets; formal inter-annotator kappa/alpha; confusion-matrix numeric values (referenced beyond p.19 cutoff); demographic details of annotators; whether religious-insult sub-category was separately measured; licensing of the corpus sources; any per-subtype (hate vs profanity vs aggression) breakdown of results.
