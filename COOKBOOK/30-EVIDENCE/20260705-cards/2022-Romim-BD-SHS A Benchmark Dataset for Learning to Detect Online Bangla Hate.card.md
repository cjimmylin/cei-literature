---
stem: "2022-Romim-BD-SHS A Benchmark Dataset for Learning to Detect Online Bangla Hate"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, best-practices, saturation-discrimination]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 50281
dataset_construction: "scraped"
languages: [bn, Bangla]
models_tested: [SVM (TF-IDF), Bi-LSTM+BengFastText, Bi-LSTM+multilingual-fastText, Bi-LSTM+random-embedding, Bi-LSTM+InFormalText]
headline_numbers: ["50,281 comments, 24,156 (48%) hate speech (p.1, p.5)", "Best F1 91.0% on HS identification (Bi-LSTM + informal embedding) (p.1, p.6)", "Fleiss Kappa 0.658 (moderate) inter-annotator agreement at Level 1 (p.5)", "60% larger than any prior Bangla HS dataset (p.1)", "Informal-text embedding trained on only 1.47M comments beats formal embeddings (p.7)"]
---
## 1. Gist
BD-SHS is a large hand-labeled Bangla (Bengali) hate-speech benchmark of 50,281 social-media comments, annotated under a novel three-level hierarchical scheme: (1) binary hate/not-hate identification, (2) target of hate (individual/male/female/group), and (3) hate type (slander, religion, gender, call-to-violence). It is the largest and most richly annotated Bangla HS dataset at time of publication (60% larger than prior work), addressing documented gaps in low-resource-language hate-speech resources (size, annotation guidelines, agreement scores, hierarchical target/type labels). For values-alignment benchmarking it is a strong non-English/non-WEIRD safety resource: it operationalizes harm categories relevant to a specific cultural context (e.g., anti-Hindu religious slurs like "malaun", gendered violence), and demonstrates that culturally-tuned, informal-text-trained models outperform large formal-corpus embeddings — a contamination/domain-mismatch lesson.

## 2. Benchmark/eval design features
Three-level hierarchical multilabel taxonomy. Level 1: binary HS vs NH with explicit inclusion criteria (attacks based on ethnicity/nationality/religion/sexual-orientation/age/gender/disability/disease; supports violence; dehumanizes via animal/criminal comparison; expresses disgust) (p.3). Level 2 targets (multilabel): Individual, Male, Female, Group (p.4). Level 3 types (multilabel): Slander, Call to Violence (CV), Gender, Religion (p.4). A single comment can carry multiple targets and types. Three downstream tasks defined: Task A (binary), Task B (multilabel target), Task C (multilabel type) (p.5).

## 3. Task format & example item
Classification of a raw comment. Verbatim example (Table 2, p.3): "েবারকা পের না, ধিষর্ত েতা হেবই।" ("It is obvious that girls who do not wear burqas would be raped.") → HS, target female, type gender. Example 5: "You son of a bitch. A malaun (swear for Hindu) like you has no right to live in our country. I will beat you to death." → HS, target IND+group, type slander+religion+CV (p.3). NH example: "িক বােলর মুিভ" ("What an ass movie") — swear aimed at a movie, not a person → NH (p.3-4).

## 4. Scoring / grading methodology
Standard classification metrics: precision, recall, F1 per class plus weighted-average F1 (weighting for class imbalance) (p.6-7). Models: linear SVM over TF-IDF word unigrams and char 2-5 grams (one-vs-rest for multilabel); Bi-LSTM (100 units + avg-pool + 16-unit FC) over four embedding types (BFT, MFT, random, IFT), softmax for Task A, sigmoid for multilabel Tasks B/C (p.6). Train/val/test = 70/15/15 random split (p.5).

## 5. Dataset construction & provenance
Scraped from Facebook posts/pages and YouTube (plus TikTok/roasting videos as "miscellaneous") using Facepager, seeded by controversial post-2017 Bangladesh events (p.2-3). Topic keywords elicited via a survey of 20 undergraduates across 17 majors, clustered into 6 domains: sports, entertainment, crime, politics, religion, controversial-scholar-comments (p.3). >100k comments collected, deduplicated with Jaccard cutoff 0.8 → 50,281 retained (p.3). Names/affiliations stripped for anonymity (p.3). Annotation by 50 undergraduates (32M/18F) across 20 majors, 3-hour training on guidelines developed iteratively from a 1,000-comment trial (p.4-5). Public on GitHub (p.1). A separate 1.47M-comment corpus across 8 domains trained the IFT embedding (p.6).

## 6. Validity evidence
Level 1 annotated by 3 annotators with majority vote; Fleiss Kappa 0.658 ("moderate agreement") (p.5). Content validity via iteratively-refined guideline grounded in Facebook/YouTube community standards and prior offensive-language taxonomies (OffensEval, Ibrohim & Budi) (p.4). Level 2/3 labeled by a single annotator each (a noted weakness, p.8). No separate human-ceiling benchmark. The paper explicitly critiques prior Bangla datasets for lacking agreement scores and guidelines, positioning its own rigor as a contribution (p.2).

## 7. Saturation / discrimination
Task A appears relatively easy — best F1 91.0%, and all seven model+feature combos cluster 88.7-91.0% (p.7), suggesting the binary task is near-saturated for these baselines. Tasks B and C are harder and more discriminating: Task B best weighted-F1 77.5% (group and individual targets hardest), Task C best 89.1% (religion type hardest, F1 ~75.7% avg due to class rarity 1,562 examples) (p.6-7). Non-traditional swear words are notably harder to detect (NTS accuracy 73-80% vs TS 76-85%) (p.7), revealing remaining headroom on context-dependent hate.

## 8. Multiturn / agentic aspects
n/a — single-comment classification.

## 9. Key numbers
- 50,281 comments; 24,156 HS (48%), 26,125 NH (p.5)
- Level 2: Ind 8,815, Male 7,128, Female 5,443, Group 3,119 (p.5)
- Level 3: Slander 16,992, CV 7,232, Gender 4,244, Religion 1,562 (p.5)
- Fleiss Kappa 0.658 (Level 1) (p.5)
- Task A best F1 91.0% (Bi-LSTM+IFT); SVM+C 90.9% (p.7)
- Task B best weighted-F1 77.5% (Bi-LSTM+IFT) (p.6)
- Task C best F1 89.1% (SVM+C); Bi-LSTM+IFT 88.9% (p.7)
- Females targeted on gender 65% vs slander 30%; males slander 88% (Table 4, p.5)
- IFT trained on 1.47M comments beats BFT (250M Wikipedia articles) (p.6-7)
- Swear-word analysis: NTS accuracy 73.31-79.53% vs TS 75.71-85.08% (p.8)

## 10. Pitfalls & limitations
Author-admitted: Levels 2 and 3 each labeled by a *single* annotator — no agreement score for target/type (p.8); annotators had conflicting Level 1 labels even with guidelines (p.8). Scraping from controversial post-2017 events risks topic-orientation reducing linguistic diversity (they mitigate but acknowledge). Data is noisy (mixed dialects, spelling errors, merged words). Only classical/RNN baselines — no transformer or LLM tested. Race collapsed into religion because rare (p.4), losing a category. Moderate (not high) IAA at Level 1. Cultural specificity limits transfer.

## 11. Novel ideas worth stealing
- **Hierarchical harm annotation (identify → target → type)**: a reusable schema for any safety/values benchmark — don't just label "harmful," decompose into *who is targeted* and *what kind of harm*, enabling fine-grained failure analysis and per-group bias auditing.
- **Multilabel targets/types**: a single item can carry multiple simultaneous harms (slander + religion + call-to-violence), reflecting real-world messiness better than single-label schemes.
- **Domain-matched embedding beats bigger formal corpus**: training a small (1.47M) informal-text model outperformed 250M-article Wikipedia embeddings — a strong lesson that *domain/register match trumps scale* for values/safety tasks; worth replicating as a contamination/robustness probe.
- **Traditional vs non-traditional swear split** as a discrimination axis — isolate context-dependent slurs (words that are hateful only in context) to measure genuine understanding vs keyword-matching. Directly analogous to BBQ/HateCheck hard-negative design.
- **Crowd-sourced topic elicitation** (survey students for controversial keywords, cluster into domains) as a lightweight way to ensure topical/linguistic diversity in scraped corpora.
- **Jaccard-0.8 dedup** as a concrete near-duplicate filter to protect diversity and reduce contamination.

## 12. Notable quotes
- "The dataset includes more than 50,200 offensive comments crawled from online social networking sites and is at least 60% larger than any existing Bangla HS datasets." (p.1)
- "The labeling criteria were prepared following a hierarchical annotation process, which is the first of its kind in Bangla HS." (p.1)
- "a word embedding trained exclusively using 1.47 million comments from social media and streaming sites consistently resulted in better modeling of HS detection in comparison to other pre-trained embeddings." (p.1)
- "all of the classifiers perform comparatively poorly at detecting HS with NTS [non-traditional swear]." (p.8)

## 13. UNKNOWN / not in extract
- No inter-annotator agreement for Levels 2 and 3 (single annotator).
- No human performance ceiling reported.
- Licensing terms of the released dataset not specified in extract.
- No transformer/LLM baselines (only SVM and Bi-LSTM).
- Exact Venn-diagram overlap counts (Figures 3-4) not in text.
