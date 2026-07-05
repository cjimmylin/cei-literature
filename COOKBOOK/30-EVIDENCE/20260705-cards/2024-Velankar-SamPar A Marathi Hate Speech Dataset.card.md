---
stem: "2024-Velankar-SamPar A Marathi Hate Speech Dataset"
reader_model: "sonnet"
confidence: "medium"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 25000
dataset_construction: "crowdsourced"
languages: ["mr"]
models_tested: ["CNN", "LSTM", "BiLSTM", "IndicBERT", "mBERT", "xlm-RoBERTa", "MahaALBERT", "MahaBERT", "MahaRoBERTa"]
headline_numbers:
  - "MahaBERT achieves best 2-class accuracy: 0.909; MahaRoBERTa best 4-class accuracy: 0.803 (p.8)"
  - "Dataset: 25,000 balanced tweets across 4 classes (hate, offensive, profane, not) + 37,500 binary version (p.6)"
  - "IndicBERT (multilingual Indian model) achieves only 0.865 (2-class), 0.711 (4-class) — mono-lingual Marathi models consistently outperform multilingual (p.8)"
---
## 1. Gist
This paper presents L3Cube-MahaHate, the first major hate speech detection dataset for Marathi, a language spoken by over 83 million people in India. The dataset consists of 25,000 tweets manually annotated into four classes: hate (targeting a group based on religion, race, gender, etc.), offensive (targeting an individual), profane (swear words regardless of target), and not (neutral content). The paper provides baseline classification results using deep learning models and multiple BERT variants, finding that monolingual Marathi models (MahaBERT, MahaRoBERTa) substantially outperform multilingual alternatives. Note: the extract title says "SamPar" but the actual paper is "L3Cube-MahaHate" — the stem refers to a different or mislabeled paper. This work matters for values-alignment benchmarking because it demonstrates both the need for language-specific datasets and the performance gap between monolingual and multilingual models in low-resource languages — critical for cultural-linguistic coverage in safety evaluations.

## 2. Benchmark/eval design features
Four-class classification benchmark (hate / offensive / profane / not) plus binary version (hateful vs. not-hateful). Key design choices:
- Balanced class distribution: 6,250 samples per class in the 4-class version (uniform, not natural distribution)
- Four-way label taxonomy distinguishing group-level (hate) from individual-level (offensive) harm, plus profanity as a separate category
- Annotation by 4 native Marathi-speaking annotators; first 200 sentences annotated together for calibration, then parallel annotation with voting for ambiguous cases
- Binary version: 37,500 samples with 18,750 per class (aggregating hate+offensive+profane as "hateful")
- Standard train/test/validation split: 21,500 / 2,000 / 1,500 (per Table 1)

## 3. Task format & example item
Classification task — given a tweet, assign one of four labels. No verbatim example item in extract, but class definitions given (p.2):
- HATE: "A Twitter post abusing a specific group of people or community based on their religion, race, ethnic origin, gender, geographical location, etc. stimulating violent behaviors."
- OFFN: "A tweet containing harmful language leading to insulting or dehumanizing, at times threatening a particular individual."
- PRFN: "A tweet including the use of typical swear words or profane, cursing language which is ordinarily insupportable."
- NOT: "A post that does not contain any insulting or abusive content."

## 4. Scoring / grading methodology
Accuracy (2-class and 4-class). No macro-F1, precision, or recall reported in the extract — only accuracy. CNN and LSTM models tested with random, trainable, and non-trainable FastText embeddings. BERT variants fine-tuned. Confusion matrices provided for best models (Figure 4, p.9).

## 5. Dataset construction & provenance
- Source: Twitter, scraped using Twint library
- Scope: Maharashtra region users, last 5 years
- Seed vocabulary: ~150 Marathi bad words (Devanagari script) used as search queries
- Cap: ≤150 tweets per search query to avoid word-level bias
- User mentions removed for anonymity
- Initial collection: ~40,000 tweets; ~28,000 annotated; ~3,000 noisy samples removed; 25,000 retained (6,250 per class)
- Additional 12,500 NOT tweets collected from Marathi personality accounts for binary version
- Data and models released at github.com/l3cube-pune/MarathiNLP

## 6. Validity evidence
- 4 native Marathi-speaking annotators with shared annotation guidelines
- Calibration on first 200 sentences together; majority vote for ambiguous cases
- Distinction between hate (group-targeting) and offensive (individual-targeting) is theoretically motivated but operationally complex
- Monolingual Marathi models (MahaBERT) substantially outperform multilingual alternatives, providing construct validity for the language-specificity of the task
- No inter-annotator agreement (Cohen's kappa or Fleiss's kappa) reported — significant gap

## 7. Saturation / discrimination
MahaBERT 2-class accuracy: 0.909 — strong but not ceiling. 4-class accuracy tops at 0.803 (MahaBERT and MahaRoBERTa) — leaving room for improvement. Non-trainable FastText CNN achieves competitive 0.751 (4-class), suggesting linguistic features are informative. IndicBERT (multilingual ALBERT covering 12 Indian languages) achieves only 0.711 (4-class), confirming Marathi-specific pre-training matters. Average tweet length: 21 words, 113 characters — short texts provide limited context for fine-grained distinction.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 25,000 tweets; 4 classes, balanced (6,250 per class) (p.6)
- Binary version: 37,500 tweets (p.6)
- Train: 21,500 / Test: 2,000 / Validation: 1,500 (Table 1, p.6)
- Average words per tweet: 21; average characters: 113 (p.6)
- Tweet length range: 2 to 93 words (p.6)
- MahaBERT 2-class accuracy: 0.909; 4-class: 0.803 (Table 2, p.8)
- mBERT 2-class: 0.903; 4-class: 0.783 (p.8)
- IndicBERT 2-class: 0.865; 4-class: 0.711 (p.8)
- CNN (non-trainable FastText) 2-class: 0.870; 4-class: 0.751 (p.8)
- Annotation: 4 native Marathi speakers; first 200 jointly labeled (p.4–5)

## 10. Pitfalls & limitations
- No inter-annotator agreement statistics reported — reliability unknown.
- Uniform class distribution (6,250 per class) does not reflect natural class distribution on Twitter, which may inflate reported accuracy.
- The distinction between HATE and OFFN is theoretically motivated but may be difficult to operationalize consistently (group vs. individual target).
- PRFN is a separate category but may overlap with HATE/OFFN — profane tweets that are also hateful are labeled PRFN only.
- Limited to Devanagari script — code-mixed Roman-Marathi tweets excluded.
- No hate-speech taxonomy beyond simple group vs. individual distinction; religion, race, gender are bundled.
- Dataset from 2017–2022 tweets; temporal drift may affect applicability.

## 11. Novel ideas worth stealing
- **Four-way hate taxonomy separating group hate, individual offense, and profanity**: cleaner than binary hate/not-hate for values benchmark design; separating profanity from targeted harm is particularly useful for LLM safety evaluation where some outputs are crude but not harmful.
- **Monolingual vs. multilingual performance gap as a benchmark validity check**: systematically testing whether multilingual models lag on culturally specific evaluation tasks is a useful diagnostic protocol for any cross-cultural benchmark.
- **Seed vocabulary curation for low-resource data collection**: constructing a language-specific seed vocabulary (~150 terms) as a collection instrument is a transferable methodology for gathering evaluation data in non-English languages.
- **Capping queries to avoid word-level bias**: limiting tweets per query (≤150) to prevent overrepresentation of specific lexical items is good practice for any seed-based dataset construction.
- **Personality-based neutral data collection**: collecting NOT samples from known Marathi personalities' accounts provides relatively unbiased neutral data — analogous to collecting model outputs from benign prompts for safety benchmarks.

## 12. Notable quotes
- "In India, Marathi is one of the most popular languages used by a wide audience. In this work, we present L3Cube-MahaHate, the first major Hate Speech Dataset in Marathi." (p.1)
- "All the monolingual Marathi BERT models are surpassing the multilingual versions of BERT models i.e IndicBERT, mBERT, and xlm-RoBERTa." (p.9)
- "The tweets which contain swear or profane words are strictly tagged as profane, even if they describe the offensive or hateful category." (p.5)
- "Although this uniform distribution of tweets does not represent the true distribution it makes the model building easier and does not require imbalance handling." (p.6)

## 13. UNKNOWN / not in extract
- Inter-annotator agreement statistics.
- Natural class distribution in the original 28,000 annotated tweets (before balancing).
- Breakdown of hate targets (religion, race, gender, etc.) within the HATE class.
- Performance on code-mixed Roman-Marathi text.
- Whether the stem "SamPar" refers to a different paper than "L3Cube-MahaHate" (the extract PDF source says "2022-team-L3Cube-MahaHate A Tweet-based Marathi Hate Speech.pdf").
