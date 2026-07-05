---
stem: "2023-Haq-NLPashto NLP Toolkit for Low-resource Pashto Language"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices, design-space]
task_format: "mixed"
scoring_type: "exact-match"
dataset_size: 34400
dataset_construction: "mixed"
languages: [ps]
models_tested: [CRF, "Pashto-BERT", XLM-R, CNN, LSTM, BiLSTM, GRU, BiGRU, Word2Vec, fastText, GloVe]
headline_numbers: ["Pashto BERT offensive-language F1 94.34%, accuracy 94.77% (p.7)", "spelling correction F1 99.16%, accuracy 99.35% (p.5)", "word segmenter F1 96.81% (p.6)", "POS tagger accuracy 99.2%, F1 97.5% at 60K sentences (p.7)", "15M-token Pashto corpus; POLD 34,400 tweets (p.3-4)"]
---
## 1. Gist
NLPashto is an open-source NLP toolkit and a set of benchmark datasets for the low-resource Pashto language (spoken by 50M+, written right-to-left in Perso-Arabic script). It ships four SOTA models — spelling correction, word segmentation, POS tagging, and offensive-language detection — plus static embeddings (Word2Vec, fastText, GloVe) and the first monolingual Pashto BERT trained from scratch on a 15M-token corpus (p.1). Its relevance to values-alignment benchmarking is as a cultural-linguistic infrastructure case study: it documents how to build benchmark resources and safety-relevant classifiers (offensive-language / toxicity detection) for an under-served language whose orthography breaks standard tokenization assumptions.

## 2. Benchmark/eval design features
Four benchmark tasks with distinct answer spaces: (1) Spelling correction — per-character binary tag (S = followed by space, J = joined), CRF sequence tagging (p.5); (2) Word segmentation — per-token binary tag (S = simple space, B = word-breaker) to preserve compound words (p.6); (3) POS tagging — 38-tag tagset following Penn Treebank conventions, CRF (p.6); (4) Offensive language detection — binary tweet classification (offensive "1" / not-offensive "0") via fine-tuned BERT (p.4-6). Constructs measured: token-boundary accuracy, grammatical-category accuracy, and offensive-content detection. Feature engineering is explicit (character n-grams 1–4; token prefixes/suffixes; morphological affixes).

## 3. Task format & example item
POS example (Fig. 2, p.4): the word توﺭ tagged NNM (Singular Masculine Noun) in "هغۀ توﺭ کوټ غوستی" ≈ "He is wearing a black jacket," where توﺭ should be Adjective (black) — illustrating homograph ambiguity where the lexicon-based tagger mislabels context-dependent words (p.4). Offensive-detection: tweets labeled 1/0 by majority vote of annotators (p.4).

## 4. Scoring / grading methodology
Exact-match sequence/classification metrics: accuracy and F1-score on an 80/20 train-test split for the three CRF taggers (p.5); precision/recall/accuracy/F1 for offensive detection on a held-out test set (p.7). POS lexicon-based baseline accuracy inferred from manual-correction rate (7% of tags changed → 93% baseline accuracy) (p.4).

## 5. Dataset construction & provenance
Corpus: ~15M tokens (avg token length 3.6 chars) scraped from news, Wikipedia, books, tweets (p.3). Spelling/segmentation dataset: ~400K raw sentences bootstrapped via Bidirectional Longest Matching lexicon segmentation with iterative manual OOV inspection → 150K fully-annotated sentences (~4M words) (p.3). POS: 10K sentences manually corrected to "100% theoretical accuracy," grown iteratively to 60K sentences (~1.5M words) (p.4, p.7). POLD: ~300K raw tweets (Jan 10–Feb 10 2023) filtered by an offensive-word seed list → 70K after cleaning → 35K sampled → final 34,400 (12,400 offensive / 22,000 non-offensive), annotated by 5 participants via majority vote (p.4). Distributed on GitHub and PyPi.

## 6. Validity evidence
Inter-annotator: POS manual correction changed ~7% of lexicon-assigned tags (p.4). Offensive dataset uses majority vote across up to 5 annotators. Ablations of feature sets provide construct evidence: word-segmenter F1 rises from 79.87% (token only) to 96.81% with context features (p.6); spelling F1 rises with n-gram window (91.22% at 1-gram → 99.16% at 4-gram) (p.5). Learning-curve validity: POS accuracy climbs 97.2%→99.2% as data grows 10K→60K sentences (p.7). No formal reliability coefficient (kappa) reported.

## 7. Saturation / discrimination
POS accuracy curve flattens near 99.2% by 50–60K sentences, indicating near-ceiling with diminishing returns (Fig. 5, p.7). Spelling correction at 99.16% F1 is near-ceiling. Offensive detection shows a ~5-point spread across models (CNN+Word2Vec 89.08% → Ps-BERT 94.34% F1), giving modest discrimination headroom (p.8, companion paper).

## 8. Multiturn / agentic aspects
n/a — all tasks are single-shot sequence tagging or classification.

## 9. Key numbers
- Spelling correction: F1 99.16%, accuracy 99.35% (p.5); n-gram ablation 91.22%→99.16% (p.5).
- Word segmenter: F1 79.87% (no context) → 96.81% (with context) (p.6).
- POS tagger: 97.2% acc / 91.0% F1 at 10K → 99.2% acc / 97.5% F1 at 60K sentences; lexicon baseline 93.0% (p.7).
- Offensive detection: Ps-BERT F1 94.34% / acc 94.77%; XLM-R next; LSTM+fastText F1 93.08% / acc 93.72%; CNN+Word2Vec lowest (p.8).
- Corpus 15M tokens; POLD 34,400 tweets (12,400 offensive / 22,000 non) (p.3-4).
- Pashto BERT: 12 layers, 768 hidden, 12 heads, 110M params, 30K vocab, trained ~2h on Tesla P100 (p.5).

## 10. Pitfalls & limitations
Author-admitted: Pashto is non-standardized (no whitespace rules) making any text noisier than English (p.1); toolkit is an "ongoing" prototype missing NER, parsing, lemmatization, MT (p.8). Observable flaws: POS "100% theoretical accuracy" claim rests on annotators verifying a single lexicon tag, risking anchoring bias (p.4); no inter-annotator kappa; offensive-language seed-list filtering skews the class distribution toward the seed vocabulary; single test split, no cross-validation or confidence intervals; "SOTA" claims are unavoidable since no prior Pashto baselines exist.

## 11. Novel ideas worth stealing
- **Iterative bootstrap annotation**: train an initial model on a small hand-corrected seed, use it to pre-label the next chunk, human-correct, retrain — dramatically cheapens dataset creation for low-resource values benchmarks (p.4).
- **Seed-list oversampling for rare classes**: to build a class that is only 1–2% of raw data (offensive tweets), filter with an inclusive keyword+pattern seed list, and deliberately add *non-lexical* patterns (2nd-person pronouns, address forms) to reduce lexical bias (p.4).
- **Sub-word (fastText) embeddings for adversarial/obfuscated text**: robustly represents deliberately misspelled or half-written offensive words — directly useful for contamination/robustness in safety benchmarks (p.8).
- **Orthography-aware tokenization tags**: distinguishing "space as delimiter" vs "space as intra-word ligature" (S/B, S/J labels) is a template for handling scripts that violate whitespace assumptions in multilingual value benchmarks.
- **Cross-cultural offensive-language definition scaffolding**: grounding annotation in a shared, documented definition set to reduce annotator ideology bias.

## 12. Notable quotes
- "Pashto, spoken by a population of over 50 million worldwide, remains largely unexplored in NLP research, lacking off-the-shelf resources and tools even for fundamental text-processing tasks." (p.1)
- "Pashto is not a standardized language, lacking any golden rules to impose a uniform way of writing." (p.1)
- "the fine-tuned monolingual Pashto BERT demonstrates the best performance which yields an F1-score of 94.34% with an accuracy of 94.77%." (p.7)
- "if a word is not present in the vocabulary the sub-words might be, which is useful in obtaining representations for altered, misspelled, or half-words." (p.8)

## 13. UNKNOWN / not in extract
Exact license of the toolkit/datasets beyond GitHub/PyPi mention; inter-annotator agreement statistic (kappa) for offensive dataset; per-tag POS accuracy breakdown; number of raw sentences that failed lexicon annotation; corpus source proportions; whether any values/ethics framing beyond offensive-language detection is addressed.
