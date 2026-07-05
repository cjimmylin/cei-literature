---
stem: "2024-Arshad-Understanding hate speech"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, saturation-discrimination]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 11782
dataset_construction: "crowdsourced"
languages: [ur, Urdu]
models_tested: ["XLM-RoBERTa-base", "FinBERT", "BERT-Hinglish"]
headline_numbers: ["HateInsights: 11,782 Urdu tweets, 3 classes + rationales (p.4)", "XLM-RoBERTa acc 0.95, F1 0.95, AUROC 0.99 (p.15)", "IOU-F1 plausibility up to 0.68 (IG), sufficiency near 0 (p.19)", "265,116 total words, avg 108 words/sentence (p.8)"]
---
## 1. Gist
Introduces HateInsights, an Urdu-language hate-speech benchmark that pairs 3-class labels (hate / offensive / neutral) with human-annotated rationales (token spans supporting each label) — the first "gold standard" Urdu hate dataset with rationales. Fine-tunes three transformer classifiers and applies SHAP/LIME/IG feature-attribution, then evaluates explainability with ERASER-style plausibility (IOU-F1, token-F1) and faithfulness (comprehensiveness, sufficiency). Relevance to values-alignment benchmarking: it is a low-resource, non-English cultural/linguistic values eval (what counts as hate depends on caste, religion, ethnicity terms in Urdu) and, crucially, demonstrates the gap between classification accuracy and explanation faithfulness — a model can score 0.95 accuracy yet produce rationales that poorly match human judgment.

## 2. Benchmark/eval design features
Constructs: (a) 3-way hate/offensive/neutral classification, (b) rationale extraction — token spans humans deem important. Answer space: sentence-level class label + word-level Boolean attention vector (rationale mask). Two evaluation layers: classification metrics (precision, recall, accuracy, macro-F1, AUROC) and explainability metrics adopted from ERASER — plausibility (IOU-F1 with 0.5 overlap threshold, token-F1) and faithfulness (comprehensiveness = drop in prediction when rationale removed; sufficiency = prediction from rationale alone). Ground-truth attention built by softmax-normalizing overlapping annotator spans (per Mathew et al. HateXplain method).

## 3. Task format & example item
Verbatim annotation guideline examples (p.7): "Comment: 'Afghani's should not be allowed to hold office.' Label: Hate Speech. Justification: The comment targets individuals based on their religious beliefs..."; "Comment: 'Shut up, you're an idiot!' Label: Offensive Language. Justification: ... do not target a person based on group identity traits..."

## 4. Scoring / grading methodology
Sentence-level: macro-averaged precision/recall/F1, accuracy, AUROC (macro to handle class imbalance). Word-level plausibility: IOU-F1 (span overlap ≥0.5 counted as match) and token-F1 vs human rationales. Faithfulness: comprehensiveness = m(x)_j − m(x\r)_j (prediction drop after removing rationale tokens); sufficiency = m(x)_j − m(r)_j (lower is better). Rationale spans compared to majority-vote human ground truth.

## 5. Dataset construction & provenance
Tweets scraped via Twint by hashtag/keyword/slur search (~10,000 initially; final 11,782 after filtering to Urdu, excluding Persian/Arabic). Annotated by 4 students (selected from 6 via testing phase) from FAST National University; batches of 200, 3 annotators each, majority vote. 350 fully-disagreeing instances dropped. Corpus: 265,116 words, 23,934 unique; classes: offensive 5,158 / hate 4,208 / neutral 2,415. Split 8:1:1 stratified. Publicly released: GitHub (umairarshad786/XAIHate) and Zenodo (DOI 10.5281/zenodo.12748652), CC-BY 4.0.

## 6. Validity evidence
Human rationale annotation with majority-vote consensus provides ground-truth for plausibility. Table 1 contrasts with 4 prior Urdu datasets — HateInsights is the only one with rationales (p.4). No formal inter-annotator agreement statistic (kappa) reported; consensus proxied by majority vote and by dropping 350 no-overlap cases. Author notes Hate/Offensive overlap causes confusion; misclassification often accompanied by lowered prediction probability, argued as evidence of model "awareness" (weak validity claim).

## 7. Saturation / discrimination
Classification is near-ceiling for XLM-RoBERTa (0.95 acc, 0.99 AUROC) — little headroom on the classification task. But explainability metrics show large headroom: best IOU-F1 only 0.68, sufficiency scores near 0 or negative, comprehensiveness varies 0.05–0.74 across model/attribution combos (p.19). Hate-vs-Offensive discrimination is the hard case (linguistic overlap); Neutral misclassification only 1.61%, Hate/Offensive mislabel <3.5% for XLM-RoBERTa (p.16). The accuracy-vs-faithfulness divergence is the key discrimination signal.

## 8. Multiturn / agentic aspects
n/a — single-turn classification of individual tweets; no interaction or tool use.

## 9. Key numbers
- 11,782 sentences (Table 1 says 11,782; corpus stats say 11,781) (p.4, p.8)
- 265,116 words, 23,934 unique, avg length 108 (p.8)
- Classes: offensive 5,158 / hate 4,208 / neutral 2,415 (p.8)
- 350 fully-disagreeing samples excluded (p.8)
- Avg 7 tokens/rationale for hate; avg 35.8 tokens/post overall (p.9)
- XLM-RoBERTa: acc 0.95, prec 0.96, recall 0.95, F1 0.95, AUROC 0.99 (p.15)
- FinBERT F1 0.84; BERT-Hinglish F1 0.80 (p.19)
- Best IOU-F1 0.68 (XLM-RoBERTa+IG); token-F1 up to 0.66 (SHAP) (p.19)
- IOU overlap threshold 0.5 (p.14)
- Conclusion claims "DeepHateExplainer ... F1-score of 92%" (p.19 — inconsistent with 0.95 in results)

## 10. Pitfalls & limitations
No reported inter-annotator kappa. Conclusion mentions "DeepHateExplainer" and 92% F1 — appears copy-pasted from a different paper (results table shows 0.95), a serious internal inconsistency. Only 4 annotators, all students from one university (annotator-pool bias for culturally-loaded labels). Feature selection constrained by hardware (lowers LIME IOU recall, author-admitted, p.19). Text-only (no emoji/casing/sentiment features, author-admitted). Hate/Offensive boundary linguistically fuzzy. Sentence count discrepancy (11,781 vs 11,782).

## 11. Novel ideas worth stealing
- Rationale-augmented labeling: require annotators to mark the exact span justifying each label, then evaluate models on span-match, not just label-match. Directly transferable to values benchmarks — for any value judgment, capture *why* and score explanation fidelity.
- Decoupling accuracy from faithfulness: report ERASER comprehensiveness/sufficiency alongside accuracy to expose models that are "right for the wrong reasons" — a discrimination axis that survives classification ceiling effects.
- Softmax-normalized multi-annotator attention as soft ground-truth (handles partial span overlap gracefully) — a principled way to aggregate disagreeing human rationales.
- Excluding full-disagreement items (no annotator overlap) rather than forcing a label — clean handling of genuinely ambiguous cases; could be reported as an "ambiguity rate."
- Low-resource-language design: pick a language where culturally-specific slurs (caste/religion terms) invert meaning by context — stress-tests context-dependence of value judgments.

## 12. Notable quotes
"even models demonstrating exceptional proficiency in classification tasks yield suboptimal outcomes in crucial explainability metrics, such as model plausibility and faithfulness." (p.1)
"judging hate speech should not rely solely on specific words but should consider the context in which these words are used." (p.3)
"even when the model mislabels text, it often exhibits a notable decrease in prediction probability for the predicted class which is indicative of its underlying awareness of distinction between the classes." (p.16)
"we encountered 350 instances where all three annotators selected different categories, rendering majority voting unfeasible ... these cases were excluded." (p.8)

## 13. UNKNOWN / not in extract
- Inter-annotator reliability statistic (kappa/alpha) — not reported.
- Whether "DeepHateExplainer"/92% F1 in the conclusion is an error or a separate ensemble (no ensemble results table shown).
- Exact per-class precision/recall breakdown beyond macro numbers.
- Demographic composition of annotators beyond "students at FAST."
- Licensing details for the scraped tweets themselves (dataset is CC-BY but tweet content provenance unclear).
