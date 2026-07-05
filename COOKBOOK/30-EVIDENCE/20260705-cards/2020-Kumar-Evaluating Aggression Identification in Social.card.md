---
stem: "2020-Kumar-Evaluating Aggression Identification in Social"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, cultural-linguistic, saturation-discrimination]
task_format: "forced-choice"
scoring_type: "classifier"
dataset_size: 15093
dataset_construction: "crowdsourced"
languages: ["en", "hi", "bn"]
models_tested: ["BERT", "RoBERTa", "mBERT", "XLM-RoBERTa", "LSTM", "CNN", "SVM"]
headline_numbers:
  - "Best system achieved weighted F-score ~0.82 (Bengali), ~0.80 (English), ~0.81 (Hindi) in Sub-task A (p.4)"
  - "Best system achieved weighted F-score ~0.93 (Bengali), ~0.87 (English), ~0.87 (Hindi) in Sub-task B (p.4)"
  - "70 teams registered; 19 teams submitted systems (p.1)"
  - "~5,000 training + ~1,000 test instances per language per sub-task (p.1)"
---
## 1. Gist
This paper reports the findings of TRAC-2 (Second Workshop on Trolling, Aggression and Cyberbullying), a shared task at LREC 2020. The task provided YouTube comments in Bengali, Hindi, and English for two sub-tasks: (A) three-way aggression identification (Overtly Aggressive / Covertly Aggressive / Non-Aggressive) and (B) binary gendered aggression identification (Gendered / Non-gendered). With 70 registered teams and 19 submitting systems, it represents a community benchmark for multilingual harmful content detection. The paper is relevant to values-alignment benchmarking as a case study in operationalizing "harm" across multiple languages and distinguishing structural aggression types (overt vs. covert, gendered vs. non-gendered).

## 2. Benchmark/eval design features
Sub-task A measures a three-class distinction between overt aggression (OAG, explicit hostile content), covert aggression (CAG, indirect or veiled hostility), and non-aggression (NAG). This three-way distinction is more granular than binary toxicity classification and captures the important difference between overt and implicit harm. Sub-task B is a binary classification distinguishing gendered from non-gendered aggression, isolating misogynistic and gender-targeted attacks as a specific sub-type. The evaluation metric is weighted F-score across classes. Most participating systems used transformer-based models (BERT and its multilingual variants) or neural classifiers (CNN, LSTM).

## 3. Task format & example item
The task is closed-class text classification. Each YouTube comment is assigned exactly one label per sub-task. No verbatim example items are provided in the extract. The dataset spans three languages and three aggression levels in Sub-task A, and two gender-targeting levels in Sub-task B.

## 4. Scoring / grading methodology
Primary metric: weighted F-score (also reported as "weighted F-score" treating it as macro-F adjusted by class support). Each team was allowed up to 3 runs; best run included in final ranking. Evaluation hosted on CodaLab (p.2).

## 5. Dataset construction & provenance
YouTube comments were randomly sampled per language: approximately 5,000 for training and 1,000 for development in each language; ~1,000 test instances per language per sub-task. Data annotated with three aggression levels (OAG, CAG, NAG) for Sub-task A and gendered/non-gendered for Sub-task B. Developed under the "ComMA Project" (Communal and Misogynistic Aggression), funded by Facebook Research (p.4). Class distributions vary: English training set is strongly imbalanced (4,211 NAG vs. 570 CAG vs. 548 OAG out of 5,329; p.2). Bengali and Hindi have more balanced distributions. Dataset available at the shared task website.

## 6. Validity evidence
No formal inter-annotator agreement statistics are reported in this paper (only the shared task overview; the underlying annotation methodology is from Kumar et al. 2018, the TRAC-1 paper). The three-way aggression taxonomy and gendered aggression taxonomy were developed in prior work. The fact that all participating teams used the same pre-labeled test set and the organizers found consistent patterns of overt-vs-covert difficulty across all languages provides indirect convergent evidence for the taxonomy's validity.

## 7. Saturation / discrimination
Sub-task B (gendered vs. non-gendered) is substantially easier than Sub-task A, with best F-scores ~0.87-0.93 vs. ~0.80-0.82. This gap suggests the three-way aggression taxonomy is harder and more discriminating. The covert aggression class is particularly challenging — it has fewer training examples and is conceptually harder to distinguish from non-aggression. There is significant room above 0.80 for future models to improve on Sub-task A. Notably, performance is consistent across all three languages for the top team (Julian: 0.821/0.802/0.812 for Bengali/English/Hindi in Sub-task A), suggesting the benchmark is not trivially easier in any one language.

## 8. Multiturn / agentic aspects
n/a — single-comment classification, no conversational context.

## 9. Key numbers
- ~5,000 training instances per language (Bengali: 4,783; English: 5,329; Hindi: 4,981) (p.2)
- ~1,000 test instances per language (p.1)
- 70 registered teams; 19 submitted (p.1)
- Best Sub-task A: Julian team — Bengali 0.821, English 0.802, Hindi 0.812 (p.4)
- Best Sub-task B: Julian team — Bengali 0.938, English 0.851, Hindi 0.878 (p.4)
- English training class distribution: NAG 4,211 / CAG 570 / OAG 548 (strongly imbalanced) (p.2)
- Bengali test: NAG 789 / CAG 169 / OAG 242 (p.2)

## 10. Pitfalls & limitations
- No inter-annotator agreement statistics are reported in this overview paper; reliability of the three-way classification is taken from prior work
- Strong class imbalance in English training set (NAG >> CAG ≈ OAG) likely inflates weighted F-score for dominant class; the covert aggression class has very few examples
- No error analysis or confusion matrix reported, making it unclear which class pairs are most confused
- All participating teams used only the provided dataset (no external data was practically available), limiting diversity of training regimes
- The paper is a shared task report, not a methodology paper; details of annotation guidelines are not reproduced here
- YouTube comments may not represent the full range of harmful language encountered by deployed AI systems

## 11. Novel ideas worth stealing
- **Overt vs. Covert aggression distinction**: For values benchmarks, distinguishing explicit norm violations from subtle or veiled ones is crucial. A benchmark that only tests overt cases will overestimate model safety. Sub-task A's three-way taxonomy (OAG/CAG/NAG) is a model for designing tiered difficulty in harmful content detection
- **Gendered aggression as a sub-type**: Isolating gender-targeted aggression as a separate classification task (Sub-task B) enables targeted evaluation of misogyny-specific harms, rather than conflating them with general aggression. Values benchmarks should similarly carve out specific harm sub-types
- **Multilingual from the start**: Running the same task in three typologically different languages (English, Hindi, Bengali) tests whether detection systems are genuinely language-agnostic or culturally parochial — a key validity question for global values-alignment benchmarks
- **Shared task infrastructure**: CodaLab evaluation with multiple submission runs and a public leaderboard creates reproducible competitive benchmarking — a model for how values benchmarks could be structured for ongoing community evaluation

## 12. Notable quotes
- "TRAC-2 is the first shared task to include YouTube comments as training and testing data and the first shared task to include Bengali data." (p.1)
- "The three-way aggression identification task in sub-task A is still a challenging task for all languages in TRAC-2." (p.4)
- "The analysis of the performance of the best systems in the two sub-tasks shows that the three-way aggression identification task in sub-task A is still a challenging task for all languages in TRAC-2." (p.4)

## 13. UNKNOWN / not in extract
- Inter-annotator agreement statistics for the TRAC-2 dataset (would be in the annotation paper, not this overview)
- Verbatim annotation guidelines for distinguishing OAG from CAG
- Whether test labels were independently verified by a second annotation round
- The precise definition of "gendered" aggression used in Sub-task B
- Whether cross-lingual transfer learning was tried by any team
