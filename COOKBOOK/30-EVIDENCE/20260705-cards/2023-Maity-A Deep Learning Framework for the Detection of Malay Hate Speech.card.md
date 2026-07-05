---
stem: "2023-Maity-A Deep Learning Framework for the Detection of Malay Hate Speech"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, saturation-discrimination, validity-psychometrics]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 4892
dataset_construction: "scraped"
languages: [ms]
models_tested: [XLCaps, XLNet+SVM, mBERT, FastText, XLM-RoBERTa, "Naive Bayes", CNN, Bi-GRU, "Capsule network"]
headline_numbers: ["HateM: 4,892 annotated Malay tweets (3002 non-hate, 1890 hate) (p.4)", "XLCaps accuracy 80.69%, macro-F1 80.41% (p.1)", "Inter-annotator Fleiss' Kappa 0.85 (p.4)", "XLCaps beats best ML baseline XLNet+SVM by 15.73 F1 (p.9)"]
---
## 1. Gist
This paper introduces HateM, the first benchmark dataset for hate-speech detection in Malay (a low-resource language), with 4,892 manually annotated tweets, and XLCaps, a two-channel deep model (XLNet+Capsule network || FastText+Bi-GRU+attention) built to handle noisy Malay social-media text. It matters for values-alignment benchmarking mainly as a *cultural-linguistic resource* example: it documents how culturally-context-dependent harm is (offensive keywords are frequently labeled non-hate), builds an annotation protocol adapting UN/Facebook/Twitter hate definitions to Malaysia, and reports 0.85 Fleiss' Kappa. It is a classifier-training paper more than an LLM-evaluation paper, but the dataset and annotation methodology are transferable to values benchmarks.

## 2. Benchmark/eval design features
Construct: binary hate vs non-hate for Malay tweets. Item = a single tweet; label space = {Hate, Non-Hate}. Hate defined as attacking a group's dignity by protected characteristics (race, gender, ethnicity, sexual orientation, nationality, religion), can be explicit or implicit. Dataset built around 14 profane/offensive Malay keywords (e.g., bodoh=stupid, babi=pig, anjing=dog, haram=forbidden). Key design insight: profane keyword presence does NOT equal hate — context decides — so the benchmark stresses contextual disambiguation.

## 3. Task format & example item
Verbatim error-analysis item (p.10): T2 "@user Bodoh macam anjing nyusah kn org" (Stupid like a dog, annoying people) — true hate, model predicted non-hate. And T1 "cuba share lagi kat komen... buat bodoh" (…acting foolish) — labeled non-hate but model wrongly predicted hate because "bodoh" co-occurs with hate in training. Table 1 (referenced p.4-5) lists labeled samples but its content is not in the extract text.

## 4. Scoring / grading methodology
Model evaluation via accuracy, precision, recall, and macro-F1 on a held-out test set (10% test / 10% val / 80% train; 10 random splits averaged). No LLM/human judging of generations — this is supervised classification against gold labels. Ground-truth labels set by majority vote of 3 annotators with expert tiebreak.

## 5. Dataset construction & provenance
~20,000 raw tweets collected via Twitter streaming/search APIs Dec 2022–Jan 2023 using 14 keywords; filtered (dedup, URL-only, non-Malay, <10 chars) down to 4,892. Annotated on Doccano (Heroku). Three undergrad Malay-proficient annotators trained in three 100-sample phases against 300 expert gold samples with guideline updates each phase. Majority-vote labels, expert breaks ties, IAA Fleiss' Kappa 0.85. Final: 3,002 non-hate, 1,890 hate; avg post length 22.35 (note: text elsewhere says 124.36 — inconsistent). Code+data at github.com/MaityKrishanu/Hate_Malay.

## 6. Validity evidence
Reliability: Fleiss' Kappa 0.85 (substantial agreement) across 3 annotators (p.4). Annotation guideline adapted from UN Strategy/Plan of Action on Hate Speech plus Twitter/Facebook protected-characteristic lists, giving content validity. Three-phase annotator training with expert correction. No factor analysis or criterion validity against external labels. Error analysis (p.10) qualitatively probes construct boundaries (sarcasm, dual-meaning words).

## 7. Saturation / discrimination
Best model XLCaps reaches 80.69% accuracy / 80.41 macro-F1 — meaningful headroom remains (~20% error). Clear discrimination among methods: ML baselines top out at XLNet+SVM F1 64.68; single-channel DL XLNet+Caps 77.48; two-channel XLCaps 80.41. XLNet consistently beats mBERT and FastText. Class imbalance (61% non-hate) present. Error analysis shows residual difficulty on implicit hate, sarcasm, and context-dependent profanity.

## 8. Multiturn / agentic aspects
n/a — single-tweet static classification, no interaction or agentic component.

## 9. Key numbers
- HateM: 4,892 tweets (3,002 non-hate; 1,890 hate); avg length 22.35 (p.4)
- Fleiss' Kappa 0.85 (p.4)
- XLCaps: accuracy 80.69%, macro-F1 80.41% (abstract p.1); conclusion states F1 81.41% (p.10 — internal inconsistency)
- Best ML baseline XLNet+SVM F1 64.68; XLCaps improves +15.73 F1 (p.9)
- Single-channel XLNet+Caps 77.48 F1; channel-1 alone 76.25, channel-2 (FastText+BiGRU) 74.72 (p.9)
- ~20,000 raw tweets collected Dec 2022–Jan 2023; 14 seed keywords (p.4)
- Split 80/10/10, batch 16, lr 1e−4, 30 epochs, 10 runs (p.8)

## 10. Pitfalls & limitations
Author-admitted: future work needed on specific noise types (misspellings, abbreviations); dataset lacks sentiment/emotion labels. Observed flaws: internal inconsistencies (avg length 22.35 vs 124.36; F1 80.41 vs 81.41; abstract "over 4,892" is exactly 4,892); binary label omits hate severity/target type; keyword-seeded collection biases toward profane vocabulary and may miss keyword-free hate; only 4,892 items and single platform (Twitter); collection window overlaps politically charged Malaysian events that may skew distribution; three student annotators only.

## 11. Novel ideas worth stealing
- **Keyword-seeded collection + the finding that profanity ≠ harm**: deliberately sampling around offensive keywords then showing most are non-hate is a powerful way to build a benchmark that *forces* context-sensitive judgment rather than lexical matching — directly transferable to values benchmarks that must distinguish surface cues from actual norm violation.
- **Phased annotator training against expanding gold sets with guideline revision each phase** — a concrete reliability-building protocol yielding Kappa 0.85.
- **Adapting international norm definitions (UN, platform policies) to a national/cultural context** where no local definition exists — a template for culturally-situated normative benchmarks.
- **Error analysis surfacing dual-meaning words and sarcasm** as systematic failure modes — a qualitative discrimination diagnostic.
- **Noise-robust dual-embedding design** (subword FastText for OOV/misspellings + contextual XLNet) as an architecture note for scoring noisy multilingual inputs.

## 12. Notable quotes
- "despite all the keywords having offensive or profane connotations, they are often labeled as non-hate. This observation highlights the inherent challenges involved in hate speech detection, where context plays a crucial role." (p.4)
- "Since there was no national definition for hate speech in Malaysia, we developed an annotation guideline by adapting the UN's definition and incorporating protected characteristics mentioned by Twitter." (p.4)
- "The obtained IAA score for the hate speech detection (HSD) task was 0.85, indicating that the dataset was of acceptable quality." (p.4)
- "'bodoh' is a commonly used Malay swear word, but it also has a dual meaning, often used to describe someone as foolish." (p.10)

## 13. UNKNOWN / not in extract
- Contents of Table 1 (sample annotated tweets) and Table 2 (full baseline results) — figures/tables not rendered in extract.
- Resolution of the avg-post-length (22.35 vs 124.36) and F1 (80.41 vs 81.41) inconsistencies.
- Licensing terms of the released dataset.
- Any human/LLM evaluation beyond supervised classifiers (none appears present).
