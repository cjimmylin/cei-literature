---
stem: "2021-Nurce-Detecting Abusive Albanian"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [design-space, cultural-linguistic, validity-psychometrics, normative-ethics]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 11874
dataset_construction: "scraped"
languages: ["sq"]
models_tested: ["BERT (multilingual)", "BiLSTM", "Naive Bayes"]
headline_numbers: ["BERT subtask A (offensive detection) F1: 0.77 (p.7, Table 4)", "BERT subtask B (offensive type) F1: 0.64 (p.7, Table 5)", "BERT subtask C (target identification) F1: 0.52 (p.8, Table 6)", "87% of corpus is NOT offensive (p.6)", "Dataset size: 11,874 comments (p.6, Table 1)"]
---
## 1. Gist
Nurçe et al. (2021) present Shaj, the first publicly available annotated Albanian dataset for hate speech and offensive speech detection. The dataset contains 11,874 social media comments collected from two Instagram accounts and two YouTube channels, annotated using the hierarchical OffensEval schema (Zampieri et al. 2019). Three classification models (Naive Bayes baseline, BiLSTM, and multilingual BERT) are evaluated across three subtasks: detecting offensive language, categorizing offense type (targeted vs. untargeted), and identifying the target (individual, group, or other). For values-alignment benchmarking, this paper documents the construction methodology for a low-resource, non-English hate speech dataset and surfaces important lessons about annotation challenges in languages where context, irony, and multi-meaning words complicate reliable labeling.

## 2. Benchmark/eval design features
**Three hierarchical subtasks (OffensEval schema):**

Subtask A — Offensive Language Detection:
- Binary: NOT (non-offensive) vs. OFF (offensive)
- Offensive content = profanity, insults, or threats

Subtask B — Automatic Categorization of Offensive Types:
- TIN (Targeted Insult): directly targets an individual, group, or other entity
- UNT (Untargeted): offensive but not directed at a specific target

Subtask C — Offensive Language Target Identification:
- IND (Individual): insults/threats toward a named or unnamed person
- GRP (Group): targets people sharing a characteristic (ethnicity, gender, sexual orientation, political affiliation, religion)
- OTH (Other): targets organization, event, or other entity not fitting IND/GRP

**Dataset sources:**
- Instagram: JOQ (Albanian informal news portal) and LJ (meme/controversial content account); 100 most recent posts from each account (October 2019)
- YouTube: RTV Klan (2nd most-viewed Albanian YT channel) and Ermal Mamaqi (popular TV host channel)

## 3. Task format & example item
Subtask A examples (p.3):
- NOT: "edhe 100 klm sot e pergjithmonte puth tezja fort" (Translation: "100 more! Have a nice time today and always! Kisses from your aunt")
- OFF: "Shtet pleeeer" (Translation: "Garbage country/government")

Subtask B examples (p.3):
- TIN: "Po ti ca je spiun pall" (Translation: "What about you? Are you a spy, you prick?")
- UNT: "Na hnksh riken" (Translation: "Suck my d*ck")

Subtask C examples (p.3):
- GRP: "Ne burg pederastat" (Translation: "Jail for the faggots")
- OTH: Comment targeting the JOQ news account

## 4. Scoring / grading methodology
- Primary metric: macro-averaged F1 score
- 80/20 train/test split, maintained for each label (p.6, Table 2)
- Hyperparameters tuned on a validation set, with more epochs for subtasks with less data (50 epochs for subtask C vs. 20 for A/B)
- Metric rationale: macro F1 preferred over accuracy because it handles class imbalance (87% NOT class)

## 5. Dataset construction & provenance
- Total: 11,874 comments; JOQ: 10,585 / LJ: 1,001 / YT: 288 (p.6, Table 1)
- Label distribution: NOT 10,306 (87%), OFF+UNT 448, OFF+TIN+IND 738, OFF+TIN+GRP 234, OFF+TIN+OTH 148
- 4 annotators (the paper's 2 authors + 2 collaborators), all native Albanian speakers, ages 22-25
- Annotators from different Albanian cities, different religious backgrounds (Muslim, Orthodox, Catholic, Bektashi)
- Annotation procedure: individual annotation followed by group discussion to resolve disagreements; final review by authors
- Privacy: usernames replaced with @USER tag; GDPR-compliant anonymization
- Emoticons retained as meaningful signal (not stripped)
- Released under CC-BY 4.0 at https://doi.org/10.6084/m9.figshare.19333298

## 6. Validity evidence
- Comparable F1 scores to similar low-resource language datasets (e.g., Danish hate speech by Sigurbergsson and Derczynski 2020; Turkish corpus by Çöltekin 2020) — suggests appropriate dataset quality for the resource level
- Models identified mis-annotated examples during training, prompting re-review — an indirect validity check
- Diverse annotator religious backgrounds reduce group-specific blind spots
- No formal inter-annotator agreement metric (e.g., Cohen's or Fleiss' kappa) reported — a gap in validity evidence

## 7. Saturation / discrimination
- Subtask A F1: 0.77 (BERT) — workable but substantial room for improvement
- Subtask B F1: 0.64 (BERT) — more difficult due to less data
- Subtask C F1: 0.52 (BERT) — near chance given 3 classes, driven mainly by small GRP and OTH class sizes (48 and 30 test examples respectively)
- The OTH label in subtask C is particularly problematic as a catch-all (acknowledged p.8)
- Class imbalance is severe (87% NOT) — macro F1 is appropriate but subtask C numbers are unreliable at this data scale

## 8. Multiturn / agentic aspects
n/a — all tasks are single-post, single-turn classification.

## 9. Key numbers
- Total comments: 11,874 (p.6, Table 1)
- NOT: 10,306 (86.8%); OFF total: 1,568 (13.2%)
- OFF+TIN+IND: 738; OFF+TIN+GRP: 234; OFF+TIN+OTH: 148; OFF+UNT: 448 (p.6, Table 1)
- Train/test split: 80/20 (p.6, Table 2)
- BERT subtask A: Precision 0.74, Recall 0.81, F1 0.77 (p.7, Table 4)
- BiLSTM subtask A: F1 0.70 (p.7, Table 4)
- NB subtask A: F1 0.41 (p.7, Table 4)
- BERT subtask B: F1 0.64 (p.7, Table 5)
- BERT subtask C: F1 0.52 (p.8, Table 6)
- Epoch settings: Subtask A/B: 20 epochs; Subtask C: 50 epochs (p.7, Table 3)
- Prior Albanian hate speech SVM work (Zenuni et al. 2017): F1 0.58 (p.4) — Shaj+BERT improves on this

## 10. Pitfalls & limitations
- **Annotator homogeneity**: Only 4 annotators, all young (22-25), all native Albanian speakers — limited diversity in age, education level, diaspora perspectives
- **No formal IAA reported**: No Cohen's or Fleiss' Kappa statistic — hard to evaluate annotation reliability vs. other datasets
- **Severe class imbalance**: 87% NOT — subtask C metrics for minority classes (GRP: 48 test examples, OTH: 30) are statistically unreliable
- **Source platform limitation**: Facebook excluded due to API restrictions; dataset may miss the most prevalent Albanian hate speech venue
- **Context dependency**: Many annotation decisions required looking up the original post — classification without context would be harder; this is not addressed in the model
- **Multilingual BERT**: Using bert-base-multilingual-uncased rather than an Albanian-specific model — no dedicated monolingual Albanian BERT available at time of writing
- **OTH catch-all label**: The "Other" target category functions as a residual rather than a semantically coherent category (acknowledged p.8)
- **Temporal snapshot**: Comments only from October 2019; no temporal diversity

## 11. Novel ideas worth stealing
- **Multi-platform sampling design**: Collecting from diverse accounts (news, meme content, TV commentary, lifestyle) within the same language creates more representative cross-register coverage than single-source datasets. Values benchmarks could use a similar multi-source design to span formal and informal registers.
- **Religious diversity in annotator selection**: Explicitly recruiting annotators from different religious backgrounds (Muslim, Orthodox, Catholic, Bektashi) to reduce in-group blind spots is a concrete and replicable annotator diversity protocol for any sensitive content annotation task.
- **Emoticon-as-signal retention**: Deciding to keep emoticons because they change meaning (fire emoji transforms a neutral sentence into a violent one) demonstrates that pre-processing decisions encode value judgments. Benchmark designers should document and justify every pre-processing step.
- **OffensEval hierarchical schema reuse**: Using an established 3-level hierarchical schema (presence → type → target) reduces invention costs and enables cross-lingual comparisons. Future values benchmarks should adopt or reference existing taxonomies rather than creating idiosyncratic classification systems.
- **Using model errors as annotation quality check**: Running models and then re-reviewing examples the model disagrees with is a low-cost mechanism to catch annotation errors — applicable in any benchmark construction pipeline.
- **Backronym naming**: "Shaj" stands for the Albanian verb meaning to offend/curse/insult, and is a backronym. Naming conventions that are meaningful in the target language community increase community adoption.

## 12. Notable quotes
- "Research on effective detection of such content has mainly focused on English and a few other widespread languages, while the leftover majority fail to have the same work put into them." (p.1)
- "The annotators demographic features and social upbringing have influenced the annotation label." (p.8)
- "Sentence structure, words with multiple meanings, context, irony and sarcasm make hate speech detection even more difficult and our contribution with the dataset more valuable." (p.8)
- "While our baseline has an F1 score of 0.41 in detecting offensive speech, we achieve an F1 score of 0.77 using BERT." (p.9)

## 13. UNKNOWN / not in extract
- Inter-annotator agreement statistics (no Kappa or similar reported)
- Whether Facebook-sourced data was later added to Shaj
- Exact number of unique tokens or vocabulary size
- Whether a monolingual Albanian BERT model exists or was used in follow-up work
- Distribution of hate speech targets (LGBT, Roma minorities, politicians — mentioned contextually but not quantified in data)
- Whether the dataset was updated beyond the October 2019 snapshot
