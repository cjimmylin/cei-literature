---
stem: "2019-Ousidhoum-Multilingual and Multi-Aspect Hate Speech Analysis"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, cultural-linguistic, validity-psychometrics, normative-ethics]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 13000
dataset_construction: "crowdsourced"
languages: ["en", "fr", "ar"]
models_tested: ["BiLSTM", "Logistic Regression", "Sluice Network"]
headline_numbers:
  - "STSL macro-F1 for directness: 0.94 English, 0.80 French, 0.84 Arabic (p.8)"
  - "MTML macro-F1 for hostility type: 0.30 average across languages (p.8)"
  - "Krippendorff alpha IAA: 0.153 English, 0.244 French, 0.202 Arabic (p.5)"
  - "Total dataset: 5,647 English + 4,014 French + 3,353 Arabic tweets (p.5)"
---
## 1. Gist
This paper introduces MLMA (Multilingual Multi-Aspect Hate Speech), the first trilingual (English, French, Arabic) hate-speech dataset annotated on five simultaneous aspects: directness, hostility type, target attribute, target group, and annotator emotional reaction. It is important for values-alignment benchmarking because it demonstrates that (a) hate speech is culturally variable across language communities in systematic ways, (b) multiple annotation dimensions on the same item reveal correlations invisible to binary annotation, and (c) annotator emotional reaction to content can itself be a signal worth capturing — a dimension largely absent from existing benchmarks.

## 2. Benchmark/eval design features
A multi-label, multi-aspect classification dataset with five tasks:
1. **Directness**: binary — direct vs. indirect hate speech.
2. **Hostility type**: multi-label — abusive, hateful, offensive, disrespectful, fearful (out of ignorance), or normal.
3. **Target attribute**: single-label — origin/ethnicity, gender, sexual orientation, religion, disability, other.
4. **Target group**: single-label — 16 named groups (e.g., women, African descent, Hispanics, Muslims, Jewish people, refugees, etc.).
5. **Annotator sentiment**: multi-label — shock, sadness, disgust, anger, fear, confusion, indifference.

The five-aspect schema captures: the explicitness of the hate speech, the type and intensity of hostility, which identity is targeted, the specific community harmed, and how observers feel about it. Tweets were collected via iterative keyword searches that evolved to capture both explicit slurs and indirect discriminatory discourse on controversial topics.

## 3. Task format & example item
Binary and multi-class forced choice annotation per tweet per aspect. Example items are referenced as Figure 1 in the paper (three screenshots from Twitter in English, French, Arabic) but the exact tweet texts are not reproduced verbatim in the extract. (see section 13).

The annotation instructions given to Amazon Mechanical Turk workers asked them to label: (a) direct or indirect; (b) hostility type from a list; (c) target attribute; (d) target group; (e) their emotional reaction. Workers completed an annotation form per tweet with dropdown/checkbox choices for each aspect.

## 4. Scoring / grading methodology
- Majority voting (5 annotators per tweet) determines final labels.
- Multi-label tasks (hostility type, annotator sentiment): if two annotators agree on two different labels, both labels are retained.
- Model evaluation: micro-F1 and macro-F1 across single-task/single-language (STSL), single-task/multilingual (STML), and multi-task/multilingual (MTML) settings using Sluice networks and biLSTM baselines.
- Data split: train:dev:test = 8:1:1.

## 5. Dataset construction & provenance
- Platform: Twitter.
- Collection: 15 search phrases per language, revised three times; starting from slurs and expanding to controversial discussion topics (feminism, Islamo-gauchisme, Iran).
- Preprocessing: deleted obvious spam, removed non-readable characters and emojis, masked user names (@user) and URLs (@url), reducing available context.
- Annotators: Amazon Mechanical Turk native speakers with reputation ≥ 0.90; 5 annotators per tweet; anti-scam measures including batch monitoring and rejection threats.
- Final size: ~13,000 tweets total (5,647 English, 4,014 French, 3,353 Arabic) plus 100-tweet pilot per language.
- Dataset and code released on GitHub.
- Arabic: mix of Modern Standard Arabic and dialects including North African dialectal forms.

## 6. Validity evidence
- Krippendorff alpha IAA reported: 0.153 (English), 0.244 (French), 0.202 (Arabic) — low but the authors note these are comparable to other complex annotation tasks given the number of labels (p.5).
- Label distribution statistics provided for all five aspects across three languages, revealing systematic cross-linguistic differences (e.g., more disability-targeting in English, more female-targeting in Arabic).
- No human ceiling baselines; no factor analysis.

## 7. Saturation / discrimination
The dataset has substantial class imbalance across tasks: e.g., "offensive" is the dominant hostility label in all three languages; "normal" is also frequent. Macro-F1 scores on the hostility-type task are low (MTML average 0.31), indicating high residual difficulty — the benchmark does not saturate. Cross-lingual multilabel tasks (target group with 16 labels) remain especially difficult (macro-F1 ≈ 0.10 for English). Classification of directness is easier (F1 ~0.86–0.94 STSL).

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- Dataset: 5,647 English, 4,014 French, 3,353 Arabic tweets (p.5)
- Annotators per tweet: 5 (p.5)
- Krippendorff alpha (IAA): 0.153 EN, 0.244 FR, 0.202 AR (p.5)
- Directness STSL macro-F1: 0.94 EN, 0.80 FR, 0.84 AR (p.8)
- Hostility MTML macro-F1: 0.30 EN, 0.28 FR, 0.35 AR (p.8)
- Target attribute STSL macro-F1: 0.42 EN, 0.18 FR, 0.63 AR (p.8)
- Target group STSL macro-F1: 0.04 EN, 0.21 FR, 0.04 AR (p.8)
- Annotator sentiment STSL macro-F1: 0.57 EN, 0.30 FR, 0.12 AR (p.8)
- Training of target group with joint target attribute improved Arabic macro-F1 by 0.25 (p.8)

## 10. Pitfalls & limitations
- User name masking and URL removal removed context that annotators needed to assess directness and intent, introducing noise.
- Arabic diglossia: mix of MSA and dialects means the Arabic corpus is linguistically heterogeneous.
- Code-switching (Hindi/Spanish in English tweets; dialectal Arabic in French tweets) added noise.
- Low IAA for English (0.153) raises questions about label reliability; the authors attribute this to task complexity rather than annotator quality.
- Only 5 annotators per tweet with majority voting — minority perspectives are lost, which matters for capturing how different cultural groups react to hate speech.
- Dataset released with anonymized tweet text rather than IDs, preventing enrichment with metadata.
- No evaluation on LLMs or pre-BERT neural models; results may not generalize.

## 11. Novel ideas worth stealing
- **Five-aspect simultaneous annotation**: capturing directness, hostility type, target attribute, target group, and observer sentiment on the same item yields a richer signal than any single binary label; values benchmarks could use this schema to capture, e.g., explicitness, harm type, affected group, and evaluator reaction together.
- **Annotator emotion as a data dimension**: measuring how annotators (as proxies for readers) react emotionally to content reveals whether a model produces text people find disturbing even if it is not technically harmful; this is directly applicable to safety evaluation of generative models.
- **Fearful-out-of-ignorance label**: a distinct hostility category capturing content that promotes fear of a group without explicit hate; useful for detecting subtle bias in LLM outputs.
- **Cross-lingual comparability by design**: parallel keyword strategies across three languages yielded comparable but not identical distributions, revealing culturally specific patterns — a template for cross-lingual values benchmarks.
- **Anti-scam annotation protocol**: threatening to reject work and block AMT annotators showing random-labeling patterns is a deployable quality-control mechanism for crowdsourced values annotation.
- **Pilot round for labelset refinement**: running 100-item pilots per language then revising the labelset based on introduced categories (adding "disgust," "socialists") before the full collection is good practice.

## 12. Notable quotes
- "Treating hate speech classification as a binary task may not be enough to inspect the motivation and the behavior of the users promoting it and, how people would react to it." (p.1)
- "To the best of our knowledge there are no other hate speech datasets that attempt to capture fear out of ignorance in hateful tweets or examine how people react to hate speech." (p.1–2)
- "We have observed significant differences in terms of target attributes in the three languages. More data may help us examine the problems affecting targets of different linguistic backgrounds." (p.6)
- "We claim that the choice of a suitable emotion representation model is key to this sub-task, given the subjective nature and social ground of the annotator's sentiment analysis." (p.6)

## 13. UNKNOWN / not in extract
- Verbatim example tweets from Figure 1 (screenshots, not reproducible from OCR).
- Precise lexicon of the 15 search phrases used per language.
- Full breakdown of all 16 target group labels.
- Whether the dataset includes any non-hateful control tweets not collected via slur-based queries.
- License terms for data release.
- Downstream performance on post-2019 transformer models (BERT, etc.).
