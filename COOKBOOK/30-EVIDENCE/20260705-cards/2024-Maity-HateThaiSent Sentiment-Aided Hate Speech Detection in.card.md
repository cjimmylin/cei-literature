---
stem: "2024-Maity-HateThaiSent Sentiment-Aided Hate Speech Detection in"
reader_model: "sonnet"
confidence: "low"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: null
dataset_construction: "crowdsourced"
languages: ["th"]
models_tested: ["BERT"]
headline_numbers: ["89.67% accuracy on Thai hate speech detection", "89.79% F1 on Thai hate speech detection"]
---
## 1. Gist
HateThaiSent (IEEE Transactions on Computational Social Systems, 2024) by Maity et al. introduces a Thai-language hate speech benchmark where each post is annotated with both a hate speech label AND a sentiment polarity label. The system uses a dual-channel architecture combining FastText word embeddings with BERT encodings, processed through a capsule network. It achieves 89.67% accuracy and 89.79% F1 on hate speech detection. This is a journal paper from a team with prior Thai hate speech work (Ex-ThaiHate, 2023). For values-alignment benchmarking, HateThaiSent is notable because it demonstrates that sentiment and hate speech are not independent: sentiment-aware models outperform sentiment-agnostic ones, suggesting that values evaluation systems benefit from modeling affective context alongside the primary classification dimension.

## 2. Benchmark/eval design features
Dual-label annotation: each Thai social media post carries both a hate speech label and a sentiment polarity label. The dual-channel model uses FastText for sub-word features (important for Thai's unsegmented script) and BERT for contextual encoding, fused through a capsule network that preserves part-whole relationships. The benchmark advances beyond Ex-ThaiHate by focusing on the sentiment-hate interaction, establishing that sentiment signal improves hate detection performance.

## 3. Task format & example item
Multi-label classification: given a Thai social media post, output both hate speech label and sentiment label. No verbatim example item available (full text unavailable).

## 4. Scoring / grading methodology
Accuracy (89.67%) and F1 (89.79%) on hate speech detection. Sentiment classification performance also reported but specific figures not confirmed from extract.

## 5. Dataset construction & provenance
Thai social media posts, dual-annotated for hate speech and sentiment. Crowdsourced annotation. Dataset size not confirmed from extract. Follows from the Ex-ThaiHate corpus line of work.

## 6. Validity evidence
Full text unavailable; inter-annotator agreement not confirmed.

## 7. Saturation / discrimination
89.67% accuracy leaves approximately 10% error rate — meaningful headroom. Whether this is primarily from ambiguous items or model limitations is unknown without full text.

## 8. Multiturn / agentic aspects
n/a — single-turn classification.

## 9. Key numbers
- Hate speech accuracy: 89.67% (from abstract; page reference unavailable).
- Hate speech F1: 89.79% (from abstract; page reference unavailable).

## 10. Pitfalls & limitations
- Full text unavailable; limitations not confirmed.
- FastText + BERT + capsule network is an older architecture compared to generative LLMs — findings may not transfer to LLM evaluation.
- Thai social media data may not cover all registers or hate speech types (e.g., coded language, emerging slurs).
- Dual-label annotation assumes sentiment and hate are separable at the item level, which may not always hold.

## 11. Novel ideas worth stealing
- Dual-label annotation (hate + sentiment) as a benchmark design principle: annotating affective valence alongside the primary moral judgment dimension captures the emotional context that drives harmful content, enabling richer model evaluation.
- Capsule network fusion as an architecture for multi-dimensional moral judgment: the capsule mechanism preserves part-whole structure, which may be useful for benchmarks where local cues (specific phrases) matter for overall verdict.
- The empirical demonstration that sentiment information improves hate detection performance argues for including sentiment as a feature in values-alignment eval pipelines.

## 12. Notable quotes
- Full text unavailable; no verbatim quotes can be confirmed.

## 13. UNKNOWN / not in extract
- Full paper text unavailable (extract_quality: missing).
- Dataset size.
- Ablation results showing the specific contribution of sentiment signal.
- Inter-annotator agreement.
- Whether corpus is publicly released.
- Page numbers for all claims.
