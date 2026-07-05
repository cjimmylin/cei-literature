---
stem: "2020-Sigurbergsson-Offensive Language and Hate Speech Detection for Danish DKHate"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, best-practices, design-space]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 3600
dataset_construction: "scraped"
languages: [Danish, da, English, en]
models_tested: ["Majority-class baseline", "Logistic Regression", "Learned-BiLSTM", "Fast-BiLSTM", "AUX-Fast-BiLSTM"]
headline_numbers: ["3,600 Danish comments (train 2,879 / test 721) (p.4)", "~88% labeled Not Offensive (p.4)", "Best Danish sub-task A macro-F1 0.699 (LogReg); English 0.735 (Fast-BiLSTM) (p.7)", "Annotator Jaccard agreement: A 41.9%, B 39.1%, C 42.8% on first 100 posts (p.5)"]
---
## 1. Gist
This paper introduces DKHate, described as the first Danish dataset for offensive-language and hate-speech detection, adopting the three-level OLID/OffensEval typology (Zampieri et al. 2019): sub-task A (offensive vs not), sub-task B (targeted vs untargeted), sub-task C (target = individual/group/other). It scrapes 3,600 Reddit and Facebook comments, annotates them, and benchmarks logistic-regression and BiLSTM classifiers in parallel for English (OLID) and Danish. Its relevance to values-alignment benchmarking is as a cross-lingual replication that (a) extends a well-established offensive-language typology to a low-resource language, (b) transparently documents how annotation disagreement forced a deliberate simplification of the construct (profanity-triggers-offensive; no context inference), and (c) includes an exemplary Bender-Friedman data statement disclosing annotator demographics — a model of provenance transparency.

## 2. Benchmark/eval design features
Three hierarchical sub-tasks (only positive instances of the prior task flow into the next): A {NOT, OFF}; B {TIN targeted-insult, UNT untargeted} over OFF posts; C {IND individual, GRP group, OTH other} over TIN posts (p.3). Answer space is a categorical label per sub-task. Constructs: general offensive language (any profanity/insult), targeting, and target type; hate speech is framed as a subset of targeted-group offensive language rather than a separate label. Extensive feature engineering explored (bag-of-words/n-grams, FastText vs random embeddings, VADER/AFINN sentiment compound scores, Flesch-Kincaid readability, POS n-grams). Class-weighting used to handle the ~88% NOT imbalance (p.6).

## 3. Task format & example item
Verbatim Danish examples (p.3): Sub-task A OFF: "Kalle er faggot..."; NOT: "Kim Larsen var god, men hans doed blev alt for hyped." Sub-task B TIN: "Hun skal da selv have 99 aar, den smatso."; UNT: "Dumme svin..." Sub-task C GRP: "Aah nej! Svensk lorteret!" (targeting Swedes); IND: "USER du er sku da syg i hoved"; OTH: "Netto er jo et tempel over lort." A vagueness example used to justify the no-context rule (p.5): "Skal de hjaelpes hjem, naee nej de skal sendes hjem" — labeled non-offensive because no explicit profanity/group despite likely anti-immigrant intent.

## 4. Scoring / grading methodology
Supervised classifiers scored by macro-averaged F1 per sub-task, with per-class recall/precision/F1 tables (Tables 5, 8, 11) to expose minority-class behavior under skew. Majority-class baselines ("All NOT", "All TIN", "All IND"/"All GRP") reported as floors (p.6). Hyperparameters via grid-search CV; class weights = inverse class frequency (p.6). Error analysis via top TF-IDF n-grams per category plus manual inspection (p.9).

## 5. Dataset construction & provenance
3,600 comments (Table 1, p.4): 800 manually collected from Ekstra Bladet Facebook page (Facebook API access was shut down, forcing manual collection), 1,400 from r/DANMAG, 1,400 from r/Denmark (top-500 posts + comments). A crowd survey of Danish Reddit users produced a 113-term offensive lexicon used as a filter, but lexicon-filtering yielded only 232 comments; the rest were randomly sampled (p.4). GDPR pre-processing: individual names replaced with @USER, sensitive-info comments removed (p.4). 80/20 train/test split preserving label distribution; ~88% NOT (Table 2, p.4). English side uses OLID (13,240 train) + optional HSAOFL (Davidson) data. CC-BY license, data statement in appendix (p.10, p.13). English comparison dataset OLID is ~33% offensive vs Danish ~12%, explaining some cross-lingual score gaps.

## 6. Validity evidence
Notably candid on reliability. Two annotators (author + supervisor) double-annotated the first 100 posts; Jaccard agreement was low: 41.9% (A), 39.1% (B), 42.8% (C) (p.5). Diagnosed two disagreement causes: context-guessing on vague posts, and failing to mark mild-profanity posts as offensive. Response: tightened guidelines (never infer non-visible context; any profanity => offensive), after which one annotator finished the rest — improving consistency but at the cost of construct validity (the label now partly tracks surface profanity). Full data statement discloses annotator demographics (age 25-40, male, white northern European, native Icelandic/English) — important because a single non-native-Danish annotator defines the gold labels (p.13).

## 7. Saturation / discrimination
Not saturated: best Danish scores are A 0.699, B 0.729, C 0.629; English A 0.735, B 0.619, C 0.557 (Tables 3-10). Clear model discrimination and no single winner across tasks/languages: LogReg best for Danish A, AUX-Fast-BiLSTM best for Danish B, Learned-BiLSTM best for both C. Minority classes (UNT, OTH) drive most error — e.g. English UNT F1 only 0.333 vs TIN 0.905 (Table 8). Pretrained-only Fast-BiLSTM underperforms on subtle/skewed sub-tasks. Small Danish data (2,879 train) is the stated ceiling on sub-task C.

## 8. Multiturn / agentic aspects
n/a — single-comment classification. The paper explicitly excludes conversational context by design (the "no context inference" guideline), which the authors acknowledge causes systematic label decisions on ambiguous posts.

## 9. Key numbers
- 3,600 comments; train 2,879 / test 721 (Table 2, p.4).
- Source mix: FB Ekstra Bladet 800 (22.2%), r/Denmark 1,400, r/DANMAG 1,400 (Table 1, p.4).
- ~88% NOT (3,159/3,600); Danish offensive rate ~12% vs English OLID ~33% (p.4, p.7).
- Annotator Jaccard: A 41.9%, B 39.1%, C 42.8% (p.5).
- Lexicon (113 terms) filter yielded only 232 comments (p.4).
- Sub-task A: EN Fast-BiLSTM 0.735, DA LogReg 0.699; baseline All-NOT EN 0.419 / DA 0.467 (Tables 3-4).
- Sub-task B: EN Learned-BiLSTM 0.619, DA AUX-Fast-BiLSTM 0.729 (Tables 6-7).
- Sub-task C: EN Learned-BiLSTM 0.557, DA Learned-BiLSTM 0.629 (Tables 9-10).
- Misclassified-offensive mean length 204.7 chars vs misclassified-not-offensive 107.9 (p.9).

## 10. Pitfalls & limitations
Author-admitted: low inter-annotator agreement; final labels made by a single annotator after the warm-up; deliberate exclusion of context; small dataset limits sub-task C; severe class imbalance. Observable and serious: the "any profanity => offensive" rule makes the label partly a profanity-detector (confirmed by errors where "Fuck I cried in this scene" should be offensive per guideline); classifiers over-rely on keywords — "svensken"(Swede) and "she" spuriously predict offensive (p.9), revealing identity/gender bias; only one non-native-Danish annotator defines Danish "offensiveness"; obfuscated/concatenated terms evade detection; no LLMs. Cross-language comparability is confounded by different offensive base rates.

## 11. Novel ideas worth stealing
- Publishing a low-agreement statistic and then explicitly documenting how the construct was simplified to raise agreement — an honest, reusable pattern: report the reliability BEFORE and the construct-narrowing decision, so downstream users know exactly what "offensive" means in the labels.
- Full Bender-Friedman data statement disclosing annotator demographics and native language — critical for values benchmarks, where WHO judges "offensive"/"hateful" determines the construct; directly adoptable.
- Hierarchical/conditional labeling (type -> targeted? -> target) that lets a single corpus support multiple related constructs and cleanly separates them — a template for layered values taxonomies.
- Parallel English/Danish modeling with a shared architecture to quantify how much performance is language-specific vs data-quantity-driven — a clean cross-lingual transfer design.
- Crowdsourcing a language- and platform-specific offensive lexicon via a public survey (captures local slurs like anti-Swede terms) — useful for building culturally-grounded probe sets.
- Error analysis that surfaces spurious identity associations ("she", "svensken" => offensive) as a built-in bias audit of the resulting classifier.
- Reporting per-class recall/precision under imbalance rather than a single macro number, exposing which construct distinctions are actually learnable.

## 12. Notable quotes
- "no post should be labeled as offensive by interpreting any context that is not directly visible in the post itself and that any post containing any form of profanity should automatically be labeled as offensive." (p.5)
- "the classifier relies too much on the presence of individual keywords, ignoring the context of these keywords." (p.9)
- "The classifier also seems to associate she with offensiveness ... while he is less often associated with offensive language." (p.9)
- "one of the key challenges ... are the differences in both the annotation-schemas and the definitions used, since it makes it difficult to effectively compare results to existing work." (p.2)

## 13. UNKNOWN / not in extract
- Number of distinct speakers/authors (data statement lists as "Unknown").
- Whether any second annotator labeled beyond the first 100 posts (appears to be single-annotator thereafter).
- Exact composition/quality of the 113-term crowd lexicon.
- Performance of any transformer (BERT) model — only LogReg/BiLSTM tested.
- Full hyperparameter grid values and per-source label breakdown beyond totals.
