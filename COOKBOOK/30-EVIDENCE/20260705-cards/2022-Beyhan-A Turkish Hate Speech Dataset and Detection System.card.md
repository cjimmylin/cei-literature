---
stem: "2022-Beyhan-A Turkish Hate Speech Dataset and Detection System"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, best-practices]
task_format: "classifier"
scoring_type: "classifier"
dataset_size: 2311
dataset_construction: "scraped"
languages: ["tr"]
models_tested: ["BERTurk"]
headline_numbers:
  - "Istanbul Convention dataset binary classification: 77.06% accuracy (±1.92), F1=77.86% with BERTurk (p.6)"
  - "Refugee dataset binary classification: 71.06% accuracy (±4.43) (p.6)"
  - "Krippendorff alpha: 0.84 binary, 0.82 multi-class for Istanbul Convention dataset (p.4)"
  - "Istanbul Convention: 1,033 tweets (removing conflicts); Refugee: 1,278 tweets (p.5)"
  - "Regression RMSE Istanbul Convention: 0.66 (±0.05); Refugee: 0.83 (±0.06) (p.7)"
---
## 1. Gist
Beyhan et al. present a Turkish hate speech dataset constructed across two topically distinct domains (Istanbul Convention withdrawal controversy and anti-refugee sentiment), along with a BERTurk-based detection system. The paper is notable for its careful multi-part annotation schema (offensive language, stance, target group, hate speech level) and iterative annotation process (started with 1–10 scale, switched to 5-level after annotator difficulties). For values-alignment benchmarking, it illustrates how political and cultural context shapes hate speech (gender-based vs. ethnicity-based), shows cross-domain generalization challenges, and demonstrates that regression modeling of hate speech intensity is a viable alternative to discrete classification.

## 2. Benchmark/eval design features
Dual-domain binary + multi-class hate speech detection with regression variant:
- **Binary**: hate speech vs. not hate speech
- **Multi-class (5-level)**: 0=No hate speech, 1=Insult ("this rabble"), 2=Exclusion ("they should go home"), 3=Wishing harm ("I hope they drown"), 4=Threatening harm ("I will kill...") (Table 1, p.3)
- **Regression**: Predict continuous score [0–4] for hate speech strength
- **Auxiliary annotations** (Table 2, p.4): Offensive language (None/Weak/Strong), Stance (Pro/Against/Neutral), Target group (Race/Ethnicity, Country/Nationality, Religion, Gender, Sexual Orientation, Opinion Groups)

Two separate datasets allow cross-domain evaluation: Istanbul Convention (gender/sexual orientation focus) vs. Refugees (country/nationality/race focus).

## 3. Task format & example item
Given a Turkish tweet, classify hate speech level (0–4) or binary (hate/not-hate).

Examples from annotation tool (Table 1, p.3):
- Level 0: "Do not give priority to these people for vaccines." (no hate speech)
- Level 1: "Do you see how these animals are jumping over the border?" (insult)
- Level 2: "I do not want my kids to be in the same classroom as Syrian kids." (exclusion)
- Level 3: "I hope these refugees drown with those boats and cannot come back!" (wishing harm)
- Level 4: "I am so full that I will kill the first Syrian that comes my way!" (threatening harm)

## 4. Scoring / grading methodology
Classification: Accuracy, F1-score, Precision, Recall with micro averaging; 5-fold cross-validation (3 seeds per fold = 15 runs) plus official test set split (p.5-6). Regression: RMSE and R-squared (Table 8-9, p.7). Conflict cases (opposing annotations from two annotators without tie-breaking) excluded from classification but included in regression (averaged).

## 5. Dataset construction & provenance
**Istanbul Convention dataset**: 284,989 tweets collected March 20–25, 2021 (5 days after Turkey withdrew). Filtered by 30 relevant hashtags; ~10,000 remained. 1,206 annotated, 1,033 usable after conflict removal. Annotators: 3 senior undergrad students in Cultural Studies.

**Refugee dataset**: Collected January 2020–September 2021 via Twitter Academic API, using immigrant-related keywords (mülteci, göçmen, Suriyeli). Filtered news accounts, accounts with many hashtags, tweets <100 chars. 1,278 annotated. Annotators: original 3 + Hrant Dink Foundation (HDV) expert team (experts in hate speech monitoring since 2009).

Dataset publicly available: https://github.com/verimsu/Turkish-HS-Dataset (p.1).

## 6. Validity evidence
Krippendorff alpha for Istanbul Convention dataset (p.4):
- Binary: α=0.84
- Multi-class: α=0.82
These are high values for hate speech annotation. The Refugee dataset had different annotator teams; no separate Krippendorff scores reported for Refugee dataset.

Error analysis (p.7-8) identifies 4 error categories: (1) meaning from context/cultural references, (2) character contractions (l*gbt), (3) infrequent words (yallah), (4) occasional ground-truth labeling mistakes. Confusion matrices show main errors between adjacent categories (0↔1), suggesting the scale is roughly ordinal (p.8).

## 7. Saturation / discrimination
Models outperform majority-class baseline by 15–25% accuracy. Binary best accuracy 77.06% (Istanbul Convention) vs. baseline 51.69%; 71.06% (Refugee) vs. baseline 39.02%. Multi-class 72.22% (Istanbul) vs. 48.31% baseline; 71.74% (Refugee) vs. 60.98% baseline. Model cannot classify categories 3 and 4 (wishing harm, threatening harm) — too few examples (35+1 in Istanbul Convention). Severe imbalance at extreme categories limits evaluation.

## 8. Multiturn / agentic aspects
n/a — single tweet classification, no thread context used.

## 9. Key numbers
- Istanbul Convention tweets collected: 284,989 (p.4)
- Istanbul Convention dataset (annotated): 1,206 total, 1,033 after conflict removal (p.5)
- Refugee dataset: 1,278 tweets (p.5)
- Istanbul hate speech categories: Not hate=499, Insult=380, Exclusion=118, Wishing Harm=35, Threatening=1 (p.5)
- Refugee categories: Not hate=774, Insult=181, Exclusion=277, Wishing Harm=39, Threatening=7 (p.5)
- Binary accuracy Istanbul: 77.06% ±1.92% (p.6)
- Binary accuracy Refugee: 71.06% ±4.43% (p.6)
- Multi-class accuracy Istanbul: 72.22% ±2.94% (p.6)
- Regression RMSE Istanbul (CV): 0.66 ±0.05 (p.7)
- Regression RMSE Refugee (CV): 0.83 ±0.06 (p.7)
- Krippendorff alpha Istanbul binary: 0.84 (p.4)
- Krippendorff alpha Istanbul multi-class: 0.82 (p.4)

## 10. Pitfalls & limitations
- Categories 3 (Wishing Harm) and 4 (Threatening Harm) have very few examples (35 and 1 in Istanbul Convention) — makes evaluation of the most dangerous categories impossible
- Annotator teams differ between datasets — Istanbul Convention annotated by university students; Refugees partially annotated by professional hate speech experts — making direct comparison problematic
- Keyword/hashtag selection may bias toward more visible hate speech, missing subtle forms
- BERTurk pretrained on formal resources; informal Twitter text creates domain mismatch (p.7)
- Stance labels potentially confounded with hate speech (tweets "pro" Istanbul Convention don't necessarily contain hate speech, but do show correlation)

## 11. Novel ideas worth stealing
1. **Multi-part annotation schema**: Separately annotating offensive language, stance, target group, AND hate speech level in a single annotation pass (Table 2) creates a rich, multidimensional dataset that enables analysis of which combinations predict hate speech. This design is directly reusable for values benchmarks.
2. **5-level categorical scale with examples in annotation tool**: Providing concrete example tweets for each level in the annotation interface reduces annotator subjectivity — and achieving α=0.84 with non-expert annotators validates this approach.
3. **Parallel regression modeling**: Training both classifiers and regression models on the same data, using the regression model for scenarios where "average toxicity over time" is the target rather than per-tweet labels — enables different deployment use cases from a single dataset.
4. **Cross-domain evaluation within same language**: Two domains (gender-based vs. ethnicity-based hate speech) in the same language allow measuring how well models generalize within a language but across social contexts — a valuable evaluation design for robustness testing.

## 12. Notable quotes
- "Hate speech is also subjective, due to the complexities of the language and/or cultural perspectives. We have found that some annotators are more inclined to call a tweet as hate speech compared to others." (p.4)
- "The system is able to capture hate speech that is visible on the surface (e.g. swear words), while missing those that require background knowledge or use of infrequent words or shorthands." (p.8)
- "We decided to focus on two topics, Istanbul Convention and attitudes against the refugees in Turkey, because of the high volume and visibility of these two topics on Twitter... we aim to capture different aspects of hate speech, such as gender-based hate speech and hate speech based on ethnicity, race, or nationality." (p.1)

## 13. UNKNOWN / not in extract
- Krippendorff alpha scores for the Refugee dataset
- HDV annotator vs. student annotator agreement comparison
- Whether stance and target group annotations improve classifier performance (not tested)
- Full confusion matrix for Refugee dataset
- Whether the regression model performance gap between Istanbul (RMSE 0.66) and Refugee (0.83) is driven by dataset characteristics or annotator differences
