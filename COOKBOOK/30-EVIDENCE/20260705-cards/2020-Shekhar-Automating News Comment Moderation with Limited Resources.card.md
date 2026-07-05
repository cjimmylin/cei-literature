---
stem: "2020-Shekhar-Automating News Comment Moderation with Limited Resources"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, contamination-robustness, best-practices]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 62600000
dataset_construction: "scraped"
languages: [Croatian, hr, Estonian, et, Russian, ru]
models_tested: ["Naive Bayes", "LSTM", "LASER+MLP", "mBERT"]
headline_numbers: ["60M+ comments from 3 outlets (24sata 21.5M, Vecernji 9.6M, Ekspress 31.5M) (p.2)", "mBERT best binary accuracy: 24sata 76.42%, VL 69.63%, Ekspress 68.40% (p.13)", "Only ~5-6% of comments require blocking (p.4)", "On real unbalanced data 24sata: recall 0.67, precision 0.27, F1 0.38 (p.13)"]
---
## 1. Gist
This is a benchmarking data-paper on automating news-comment moderation in two less-resourced European languages (Croatian, Estonian) under the EMBEDDIA project. It uses real-world moderator block/no-block decisions as gold labels over 60M+ scraped comments and benchmarks four classifiers (NB, LSTM, LASER, mBERT). Its most valuable contribution for values-alignment benchmarking is NOT the classifier scores (which are mediocre) but its unusually candid audit of label reliability: when 350 model-moderator disagreements were re-moderated, roughly half of originally-blocked comments were now judged non-blocked, and of those still blocked, over half received a DIFFERENT rule justification. It is a case study in how noisy, policy-drifting, context-dependent, culturally-specific human labels place a hard ceiling on any benchmark built from them — a caution directly applicable to values/safety evals that reuse real-world moderation flags.

## 2. Benchmark/eval design features
Two task formulations: (1) binary — block vs non-block; (2) multi-class — which policy rule was violated (24sata 8 rules; Vecernji List 9 rules). Rule schema (Table 1, p.3) spans hate speech, threats, obscenity, deception/trolling, vulgarity, wrong-language, abuse, disallowed content — a heterogeneous mix well beyond "offensive language." Answer space is a categorical label. The paper explicitly problematizes that the "blocked" class is a heterogeneous union of diverse phenomena, that rule categories overlap and are not a-priori fixed, and that schemata differ across publishers and cannot be directly mapped (Table 2, p.4). Data is highly imbalanced (~5-6% blocked). Performance reported per-class (blocked recall vs non-blocked recall) rather than dominated weighted-F1.

## 3. Task format & example item
Verbatim context-dependent examples (p.20): (1) "U cemu je problem? Doticni je pod tim simbolom zivio i djelovao." ("What's the problem? The person in question lived and worked under that symbol.") — Moderator: blocked, rule 8 (the pronoun "that symbol" needs prior-comment context, probably a swastika). (2) "HDZ je proslost a i Sdp!" ("HDZ is the past, and so is the SDP!") — not blocked (even-handed only if you know HDZ and SDP are Croatia's two main parties). (3) A comment invoking Pavelic/Tudman — blocked, but moderators disagree between rule 8 and rule 5.

## 4. Scoring / grading methodology
Balanced train/val/test built by selecting articles with >=1 blocked comment and sampling equal blocked/non-blocked per article; reported as percentage accuracy overall and per class (blocked-recall, non-blocked-recall) (p.12). Real-world performance projected by re-weighting to the true ~7.8% block rate, yielding recall/precision/F1 (p.13). Multi-class rule task scored per-rule accuracy and mapped back to binary blocking accuracy (Tables 10-12). Confidence analysis by sweeping the decision threshold 0.5->1.0 (Figure 3). Label reliability audited by human re-moderation of 350 disagreement cases (p.19).

## 5. Dataset construction & provenance
Scraped 60M+ reader comments: 24sata (21.5M, Croatian), Vecernji List (9.6M, Croatian), Eesti Ekspress (31.5M, Estonian + Russian) (p.2). Labels are the newspapers' own moderator block flags plus, for 24sata/VL, the specific rule violated; Ekspress records no rule categories (p.4). Metadata: article link, anonymized author ID, timestamp. 2019 data selected for experiments because blocking rates rose sharply over time (policy drift), making recent data cleaner; earlier years contain many false negatives (Table 16: 24sata block rate rose from ~1e-4 pre-2016 to 7.8e-2 in 2019, p.27). Partition sizes in Table 7 (e.g. 24sata train 99,246 comments). No new manual annotation; labels are real-world operational flags.

## 6. Validity evidence
This is the paper's strongest and most sobering section. Label reliability directly tested: 350 mBERT-moderator disagreements re-moderated by 24sata staff — of 101 originally-not-blocked, 19 now blocked (missed positives); of 244 originally-blocked, 120 (~half) now judged non-blocked, and of the 124 still blocked, 81 got a DIFFERENT rule (p.19). Rule distributions vary widely across publishers even for supposedly-equivalent categories (threats rare in 24sata, common in VL, p.15) and drift over time (Figure 2). NB conditional-probability inspection: only 78 of 185 blacklist words appear in top-1000 blocked indicators; charged words (swastika, terrorism) appear as NON-blocked indicators (p.14) — evidence the "blocked" construct is not lexically coherent.

## 7. Saturation / discrimination
Not saturated but capped by label noise: best model mBERT reaches only 68-76% balanced accuracy (p.13), below comparable offensive-language work (OffensEval max F1 0.829, p.7). Blocked-class recall consistently lower than non-blocked recall. Rare rules (threats, obscenity) are essentially ignored by all classifiers (0% accuracy, Table 10). Surprisingly NB baseline is competitive with LSTM/LASER; the pretrained LASER/mBERT sometimes adapt worse to rare classes in fine-tuning (p.16). Temporal degradation: mBERT accuracy falls from 80.03% (2019, in-domain) to 72.25% (2016) as test data moves away from the training year (Table 14).

## 8. Multiturn / agentic aspects
n/a as implemented — comments classified as independent texts. BUT the error analysis (p.19-20) identifies this as a core failure mode: many comments require the article + preceding-comment thread context to be understood as problematic (e.g. "that symbol" referring back). This is an implicit argument that the task is genuinely conversational/multiturn even though modeled single-turn.

## 9. Key numbers
- 60M+ comments: 24sata 21.5M, VL 9.6M, Ekspress 31.5M (p.2).
- ~5-6% of comments blocked; peak block rates VL >15%, Ekspress 12.5%, 24sata 7.8% (p.4, p.12).
- Balanced binary accuracy mBERT: 24sata 76.42 / VL 69.63 / Ekspress 68.40 (Table 8, p.13).
- Per-class 24sata mBERT: blocked 67.33, non-blocked 85.49 (Table 8).
- Projected real 24sata: recall 0.67, precision 0.27, F1 0.38 (binary); recall 0.48, precision 0.32, F1 0.39 (multiclass) (p.13, p.15).
- Re-moderation of 350 disagreements: 120/244 originally-blocked flipped to non-blocked; 81/124 got a different rule (p.19).
- 78 of 185 blacklist words in NB top-1000 blocked indicators (p.14).
- Temporal accuracy 2019->2016: 80.03 -> 72.25% (Table 14).
- 24sata blocking rate over time: ~1e-4 (pre-2016) -> 7.8e-2 (2019) (Table 16, p.27).

## 10. Pitfalls & limitations
Author-admitted: labels are noisy operational flags, not curated annotations; moderation is subjective, drifts over time, and varies across publishers; context is missing; cross-lingual transfer is needed but current methods can't capture culture-specific references (p.21). Observable: no formal inter-annotator agreement statistic (only the informal re-moderation study); balanced-sampling evaluation inflates apparent accuracy vs the true 5-6% base rate; the "blocked" target conflates spam, hate, threats, wrong-language, etc.; Ekspress lacks rule labels entirely; no LLMs beyond mBERT. Fundamentally the benchmark's ceiling is set by label validity, not model capacity.

## 11. Novel ideas worth stealing
- Re-annotation audit of model-human disagreements: take the cases where a model disagrees with the gold label, have humans re-judge them, and report the flip rate — a cheap, powerful way to estimate the noise floor / label-validity ceiling of ANY values benchmark. The finding "half of blocked comments flip on re-moderation" is a template metric.
- Treating temporal robustness as a first-class axis: fix the training year, test across years, and show accuracy decays with policy drift — reusable for detecting benchmark staleness/contamination and for arguing why periodic re-labeling is needed.
- Auditing construct coherence via an interpretable baseline (NB conditional-probability table) — checking whether blacklist/charged words actually align with the positive class exposes when a "label" is not a coherent construct.
- Cross-publisher schema mismatch analysis: documenting that nominally-equivalent categories (hate speech, threats) have wildly different application rates across annotator organizations — a caution for pooling values labels from multiple sources.
- Per-class recall reporting under imbalance plus explicit re-weighting to the real base rate to project deployment performance — honest reporting pattern for rare-positive values/safety tasks.
- Confidence-threshold sweep to show blocked comments are classified more confidently than non-blocked (implying many "non-blocked" are actually missed positives).

## 12. Notable quotes
- "of 244 comments which were originally blocked ... approximately half (124) were still judged to be blocked, but half (120) were now marked non-blocked. Of the 124 which remained blocked, over half (81) were given a different rule as justification." (p.19)
- "the overall category of blocked comments is likely to cover a very heterogeneous sample of language, as it results from a diverse range of phenomena." (p.4)
- "performance is limited not only by the nature of interactive language and its dependence on context, but by the need to rely on labels gathered under real-world constraints." (p.1)
- "many phenomena of interest are dependent on region- or culture-specific references and understanding of the related context." (p.21)

## 13. UNKNOWN / not in extract
- Exact total across all three outlets is stated as "over 60 million" (component sizes given); the precise merged count is approximate.
- Formal inter-annotator agreement / kappa for moderation (none computed; only re-moderation study).
- Licensing / public availability of the collected corpus.
- Hyperparameters of the neural models (referenced but not in the read pages).
- Full Estonian/Russian-specific results breakdown (Ekspress has no rule labels).
