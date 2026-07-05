---
stem: "2024-Khanduja-Telugu Language Hate Speech Detection Using"
reader_model: "sonnet"
confidence: "low"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: null
dataset_construction: "scraped"
languages: ["te"]
models_tested: ["mBERT", "DistilBERT", "IndicBERT", "NLLB", "MuRIL", "XLM-RoBERTa", "Indic-Bart"]
headline_numbers: ["mBERT achieved 98.2% accuracy on Telugu hate speech detection"]
---
## 1. Gist
This 2024 paper (Systems and Soft Computing, Elsevier) by Khanduja, Kumar, and Chauhan creates a monolingual Telugu-language corpus of tweets annotated for hate/non-hate speech, and evaluates seven transformer models — mBERT, DistilBERT, IndicBERT, NLLB, MuRIL, XLM-RoBERTa, and Indic-Bart — on this benchmark. The standout result is mBERT achieving 98.2% accuracy. Telugu is a Dravidian language with approximately 80 million speakers; it is severely underrepresented in NLP benchmarks. For values-alignment benchmarking, this paper demonstrates both the feasibility and the necessity of constructing language-specific hate speech benchmarks for non-English, non-European languages, and provides a model comparison template for evaluating multilingual models on Telugu toxicity.

## 2. Benchmark/eval design features
Binary classification: tweet → hate or non-hate. The benchmark is monolingual (Telugu script only, no transliteration). Key contribution is corpus creation since no prior Telugu hate speech benchmark existed. Seven transformer models tested systematically, enabling cross-architecture comparison. This design directly addresses the gap in Dravidian language NLP benchmarking.

## 3. Task format & example item
Binary classification: given a Telugu tweet, classify as hate speech or non-hate speech. No verbatim example item available (full text unavailable).

## 4. Scoring / grading methodology
Accuracy is the headline metric (mBERT: 98.2%). Standard classification metrics (precision, recall, F1) likely also reported, but not confirmed from extract.

## 5. Dataset construction & provenance
Source: Twitter/X, monolingual Telugu tweets. Annotation: binary hate/non-hate labels. Construction method: scraped and manually annotated. Dataset size not confirmed from extract.

## 6. Validity evidence
Full text unavailable; inter-annotator agreement and validity evidence not confirmed.

## 7. Saturation / discrimination
If mBERT achieves 98.2% accuracy, the benchmark may be near saturation for encoder-based models — limited headroom for improvement. However, this figure requires verification from full text.

## 8. Multiturn / agentic aspects
n/a — single-turn classification.

## 9. Key numbers
- mBERT accuracy: 98.2% (from abstract; page reference unavailable — full text missing).

## 10. Pitfalls & limitations
- Full text unavailable; limitations not confirmed.
- 98.2% accuracy is suspicious and may indicate class imbalance or data leakage — cannot verify without full text.
- Binary labels may not capture nuance in Telugu-specific offensive discourse.
- Twitter-sourced data may not generalize to other platforms or registers.
- Generative LLMs not tested — findings may not transfer to LLM evaluation contexts.

## 11. Novel ideas worth stealing
- Monolingual Dravidian corpus construction as a benchmark template for other underrepresented language communities (Kannada, Malayalam, Tamil — the other three major Dravidian languages each need similar benchmarks).
- Systematic multi-model comparison on a novel language corpus establishes which multilingual architectures generalize best to low-resource Dravidian languages — a useful prior for designing multilingual values benchmarks.
- The very high mBERT accuracy may indicate that hate speech in Telugu has distinctive lexical markers that make detection easier than in English, which has implications for cross-lingual transfer assumptions.

## 12. Notable quotes
- Full text unavailable; no verbatim quotes can be confirmed.

## 13. UNKNOWN / not in extract
- Full paper text unavailable (extract_quality: missing); PDF access requires manual/institutional retrieval.
- Dataset size (number of tweets).
- F1, precision, recall scores for each model.
- Inter-annotator agreement.
- Whether corpus is publicly released.
- Class balance (hate vs. non-hate ratio).
- Page numbers for all claims.
