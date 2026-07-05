---
stem: "2021-Luu-A Large-scale Dataset for Hate Speech Detection on Vietnamese Social"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, saturation-discrimination]
task_format: "MCQ"
scoring_type: "classifier"
dataset_size: 33400
dataset_construction: "scraped"
languages: [vi]
models_tested: [Text-CNN, GRU, "m-BERT-uncased", "m-BERT-cased", "XLM-R", "DistilBERT"]
headline_numbers: ["33,400 comments, 3 labels CLEAN/OFFENSIVE/HATE (p.6)", "Best macro-F1 62.69% (m-BERT cased) accuracy 86.88% (p.8)", "Inter-annotator agreement Cohen kappa = 0.52 (p.4)"]
---
## 1. Gist
ViHSD is a large-scale human-annotated Vietnamese social-media hate-speech dataset (33,400 Facebook/YouTube comments) with a three-way label scheme (CLEAN, OFFENSIVE, HATE). It matters for values-alignment benchmarking as a low-resource-language, culturally-situated safety benchmark: it foregrounds how hate/offense detection depends on Vietnamese-specific slang, teencode, abbreviations, and figurative meaning that even multilingual transformers struggle with. It also contributes an explicit, IEEE-peer-review-inspired annotation pipeline with formal inter-annotator agreement measurement, addressing a gap the authors note in the prior Vietnamese VLSP-HSD dataset (which did not document annotation quality).

## 2. Benchmark/eval design features
Construct measured: presence and directedness of hateful/offensive content in a comment. Three flat labels: CLEAN (no harassment), OFFENSIVE (harassment/profanity but not aimed at a specific target), HATE (harassment/abuse directed at an individual or group by characteristics, religion, nationality). HATE has three documented sub-cases (explicit attack; implicit hateful meaning without explicit words; figurative meaning requiring social knowledge) (p.4). Answer space: single-label 3-class classification per comment. Train/dev/test split 7-1-2, label distribution skewed toward CLEAN.

## 3. Task format & example item
Verbatim examples (Table 3, p.6): "#1 Nhanh thực sự (English: It is really fast)" -> clean; "#3 Nó học cách của thằng anh nó đó, hèn, khốn nạn (English: He is coward and bastard likes his brother)" -> hate; "#4 <person name> người ư? sinh vật hạ đẳng ... (English: person? It is an inferior animal...)" -> hate; "#5 Đm vcl (English: God damn it!!)" -> offensive.

## 4. Scoring / grading methodology
Model predictions scored by Accuracy and macro-averaged F1-score on the test set (p.8). Macro-F1 emphasized due to strong class imbalance (large accuracy-vs-F1 gap noted). Gold labels themselves produced by human annotation + major voting.

## 5. Dataset construction & provenance
Comments crawled from high-interaction Vietnamese Facebook pages and YouTube videos on entertainment, celebrities, social issues, politics; named entities removed for anonymity (p.3). Annotation: two-phase process (training phase with guideline calibration + Cohen kappa check, then annotation phase). Two annotators label all data; a third resolves disagreements, a fourth if all three disagree; final label by major voting, IEEE peer-review inspired (p.3-5). 33,400 comments total, split 7-1-2 (train 19,886 clean / 1,606 offensive / 2,556 hate; similar proportions in dev/test) (p.6). No licensing/contamination controls discussed.

## 6. Validity evidence
Inter-annotator agreement measured on 202 random comments across four annotators (A1-A4); pairwise Cohen kappa ranged 0.46-0.65, average kappa = 0.52 (Table 2, p.4). Authors cite Di Eugenio that kappa > 0.5 is acceptable, but acknowledge only "moderate" agreement. Disagreement driven by annotator knowledge of slang/abbreviations/figurative phrases (worked example: "Dm" and "lũ quan ngại" split annotators by prior knowledge) (p.5). No factor analysis or human performance ceiling.

## 7. Saturation / discrimination
Substantial headroom: best macro-F1 only 62.69% despite high accuracy 86.88%, the gap driven by class imbalance toward CLEAN (p.8). Authors frame 62.69% as "a challenge for future researches." Confusion matrix shows most OFFENSIVE comments misclassified as CLEAN, and HATE misclassified as OFFENSIVE when profanity is in irregular/teencode form (p.9). Transformer models only marginally beat Text-CNN, so the benchmark discriminates weakly among model classes but strongly exposes the difficulty of irregular text.

## 8. Multiturn / agentic aspects
n/a. Static single-comment classification; no interaction, context, or agentic protocol.

## 9. Key numbers
- 33,400 comments; three labels (p.6).
- Train counts: 19,886 clean / 1,606 offensive / 2,556 hate; dev 2,190/212/270; test 5,548/444/688 (Fig 2, p.6).
- Average inter-annotator kappa = 0.52; pairwise 0.46-0.65 (p.4).
- Best: m-BERT cased 86.88% accuracy, 62.69% macro-F1 (p.8).
- Text-CNN 86.69% / 61.11%; GRU 85.41% / 60.47%; m-BERT uncased 86.60/62.38; XLM-R 86.12/61.28; DistilBERT 86.22/62.42 (p.8).
- fastText 300-dim embeddings for DNN models; transformers 4 epochs, batch 16, seq len 100 (p.7-8).

## 10. Pitfalls & limitations
Author-admitted: inter-annotator agreement only moderate (kappa 0.52); annotation heavily influenced by annotator subjectivity and slang knowledge; models fail on abbreviations, teencodes, slangs, figurative meaning; class imbalance inflates accuracy vs F1 (p.9). Visible flaws: no reported annotator demographics or count of total annotators; no licensing/ethics/consent discussion beyond NE removal; three flat labels collapse many distinct harm types; no target/group breakdown; crawled from public pages so temporal/topical bias likely; teencode normalization left to future work.

## 11. Novel ideas worth stealing
- Explicit three-tier severity/directedness scheme (CLEAN / OFFENSIVE-untargeted / HATE-targeted) that separates profanity-for-emphasis from targeted attack — a cleaner distinction than binary toxic/not for values benchmarks. (p.3-4)
- Document HATE sub-cases explicitly including implicit and FIGURATIVE hate requiring cultural/social knowledge — a reusable prompt-for-annotators design that captures culturally-coded harm. (p.4)
- IEEE-peer-review-inspired escalating annotation pipeline (2 -> 3 -> 4 annotators only on disagreement) to save annotation cost while resolving hard cases — efficient consensus protocol. (p.3, Fig 1)
- Report full pairwise inter-annotator kappa matrix, not just an aggregate, to expose annotator-pair heterogeneity. (p.4)
- Treat low-resource-language slang/teencode/abbreviation robustness as a first-class benchmark difficulty axis; pair the dataset with an error analysis mapping failure modes to orthographic irregularity. (p.9)
- Anonymize by named-entity removal at collection time as a built-in privacy control. (p.3)

## 12. Notable quotes
"The comments have harassment and abusive contents and directly aim at an individual or a group of people based on their characteristics, religion, and nationality." (p.4, HATE definition)
"the annotation process is mostly impacted by the knowledge and subjective of annotators." (p.6)
"the best baseline model on the dataset is 62.69%, and this is a challenge for future researches" (p.10)
"it is difficult to detect the hate speech on Vietnamese social media texts due to their characteristics." (p.10)

## 13. UNKNOWN / not in extract
- Total number of annotators employed and their demographics.
- Dataset licensing/availability terms.
- Whether any contamination or deduplication controls were applied.
- Precise crawl date range and source page list.
- Human performance ceiling on the task.
