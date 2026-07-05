---
stem: "2019-Basile-SemEval-2019 Task 5"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, design-space, validity-psychometrics, contamination-robustness]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 19600
dataset_construction: "crowdsourced"
languages: ["en", "es"]
models_tested: ["SVM (Fermi team, best English A: F1=0.651)", "SVM (Atalaya, best Spanish A: F1=0.73)", "BiGRU+capsule network (YNU DYX)", "BERT-like model (alonzorz)", "LSTM+GloVe (SINAI-DL)", "fastText", "Logistic Regression + Classifier Chains (CIC-1)"]
headline_numbers:
  - "19,600 tweets total: 13,000 English, 6,600 Spanish (p.2)"
  - "74 teams, 108 runs for Subtask A, 70 runs for Subtask B (p.1)"
  - "Best English Subtask A: macro-F1 0.651 (Fermi, SVM with Universal Sentence Encoder) (p.5)"
  - "Best Spanish Subtask A: macro-F1 0.73 (Atalaya and MineriaUNAM) (p.7)"
  - "No English Subtask B system exceeded MFC baseline EMR of 0.580 (p.7)"
  - "F8 annotation confidence for English HS: 0.83; TR: 0.70; AG: 0.73 (p.3)"
---
## 1. Gist
SemEval-2019 Task 5 (HatEval) is a shared task on multilingual hate speech detection in tweets against immigrants and women in English and Spanish. The task has two subtasks: (A) binary hate speech detection, and (B) fine-grained classification of aggressive attitude and target type (individual vs. generic group). With 74 teams and 178 total submissions, HatEval was among the most popular SemEval-2019 tasks, establishing a community benchmark for hate speech detection across two targets and two languages. The paper documents the annotation methodology, dataset statistics, participating systems, and results — including the notable finding that fine-grained attribute prediction (Subtask B) is substantially harder than binary detection, and that no system exceeded the most-frequent-class baseline on English Subtask B. For values-alignment benchmarking, HatEval is a reference multilingual hate speech resource with documented cross-linguistic and cross-target performance differences.

## 2. Benchmark/eval design features
Three binary labels per tweet: HS (hate speech present), TR (target range: individual vs. generic), AG (aggressiveness). Annotation hierarchy: TR and AG are only labeled for hateful tweets (HS=1). Two subtasks: A = binary HS detection (ranked by macro-F1); B = joint prediction of all three labels (ranked by Exact Match Ratio for partial match, also macro-F1 average across HS/AG/TR). Dataset deliberately oversampled hate speech (~40–42% in train/test, vs. ~10% natural prevalence) to balance classes. Annotation: crowdsourced via Figure Eight + 2 expert annotators; final label by majority vote of crowd + 2 experts.

## 3. Task format & example item
Input: tweet text. Output: binary labels (0/1) for HS (and optionally TR and AG). Examples from the paper (p.4):

Hateful, individual, aggressive:
> 7, lol, chop her head off and rape the bitch https://t.co/ZB8CosmSD8, 1, 1, 1

Hateful, generic group, non-aggressive (misogynistic stereotype):
> 11, WOW can't believe all these women riding the subway today? Shouldn't these bitches be making sandwiches LOL #ihatefemales.., 1, 0, 0

Non-hateful (false positive risk):
> 30249, My mom FaceTimed me to show off new shoes she got and was like "no cabe duda que soy una Bitch" i love her [gold: 0]

## 4. Scoring / grading methodology
Subtask A: macro-averaged F1-score (class-balanced, handles class imbalance better than accuracy). Also reports accuracy, precision, recall. Subtask B: Exact Match Ratio (EMR) = fraction of instances where all three labels (HS, TR, AG) match exactly; also macro-F1 average across three labels separately. Submissions ranked by EMR for Subtask B. Baselines: MFC (most frequent class in training set) and SVC (linear SVM on TF-IDF).

## 5. Dataset construction & provenance
Collection: tweets July–September 2018 (immigration-related) + earlier misogyny collections. Strategies: (1) monitoring known hate accounts' history, (2) filtering keyword streams. English: 13,000 tweets (10,000 train/dev, 3,000 test), 5,000 per target. Spanish: 6,600 tweets (5,000 train/dev, 1,600 test). Annotation: Figure Eight crowdsourcing platform (not-trained contributors) + 2 expert native-speaker annotations per tweet; majority vote of all three. Annotation guidelines available on GitHub. Hateful tweets artificially oversampled to ~40–42% (vs. ~10% natural prevalence). Data distributed with new IDs (original Twitter IDs replaced).

## 6. Validity evidence
F8 annotation confidence (combining inter-rater agreement and contributor reliability): English HS 0.83, TR 0.70, AG 0.73; Spanish HS 0.89, TR 0.47, AG 0.47 (p.3). Low Spanish confidence on TR and AG (0.47) is notably weak. The hybrid crowd+expert methodology was motivated by concern about crowd annotation quality for a complex, politically sensitive task. Error analysis shows common systematic errors: false positives on swear words used humorously or self-referentially; false negatives on covert or ironic hate speech (p.8).

## 7. Saturation / discrimination
English Subtask A mean F1 = 0.4484, max 0.6510 — substantially below Spanish (mean 0.6821, max 0.7300). This 23-point mean gap is unexplained but possibly reflects different annotation quality, tweet complexity, or the earlier English collection period. Subtask B is harder than A across both languages: English B median 0.312 vs. A median 0.450. No English Subtask B system exceeded the MFC baseline in EMR — suggesting that jointly predicting HS+AG+TR simultaneously is currently intractable for systems that are only modestly above chance on each dimension. Large performance variance across systems (StdDev 0.056–0.090) indicates the task has not saturated.

## 8. Multiturn / agentic aspects
n/a — single tweet classification; no conversational context.

## 9. Key numbers
- Total dataset: 19,600 tweets (13,000 English, 6,600 Spanish) (p.2)
- 9,091 about immigrants, 10,509 about women (p.2)
- ~40–42% hateful in train/test sets (vs. ~10% natural prevalence) (p.3)
- 74 teams total; 108 Subtask A runs, 70 Subtask B runs (p.1)
- F8 confidence English: HS 0.83, TR 0.70, AG 0.73 (p.3)
- F8 confidence Spanish: HS 0.89, TR 0.47, AG 0.47 (p.3)
- Best English A: Fermi macro-F1 0.651 (SVM + Universal Sentence Encoder) (p.5)
- Best Spanish A: 0.73 (Atalaya and MineriaUNAM, both SVM) (p.7)
- Best English B: LT3 EMR 0.570 (below MFC baseline 0.580) (p.7)
- Best Spanish B: CIC-2 EMR 0.705 (above MFC baseline 0.605) (p.7)
- Top-3 systems agree on wrong label: English 569/2971 (19.1%); Spanish 234/1600 (14.6%) (p.8)
- False positives dominate common errors: 89.1% English, 76.1% Spanish (p.8, Table 4)
- SVC baseline English A: 0.451; Spanish A: 0.701 (p.7, Table 3)
- MFC baseline English A: 0.367; Spanish A: 0.370 (p.7, Table 3)

## 10. Pitfalls & limitations
- Spanish annotation confidence on TR and AG (0.47) is at near-chance level — fine-grained labels for Spanish are unreliable
- Artificial oversampling of hate (40–42% vs. ~10% natural rate) inflates performance metrics relative to real-world deployment
- Collection biases: keyword-filtered tweets oversample blatant hate; covert hate (irony, implication) underrepresented
- No demographic information on tweeters
- Natural distribution of Spanish data severely skewed (as noted: "only about 10% of annotated data contained hate speech")
- English and Spanish collections come from different time periods with different collection strategies, making direct cross-lingual comparison unreliable
- No analysis of whether systems overfit to lexical hate markers vs. learning robust representations
- Concurrent OffensEval task covers related but distinct concept of offensiveness — the boundaries are fuzzy

## 11. Novel ideas worth stealing
- **Hierarchical multi-label design**: labeling aggressiveness and target type only for confirmed hateful tweets creates a structured prediction problem that mirrors real-world content moderation workflows. Benchmarks for values alignment could adopt hierarchical conditional labeling.
- **Hybrid crowd+expert annotation**: adding two expert annotations to all crowd-annotated data and using majority vote of 3 (crowd, expert1, expert2) is a cost-effective way to improve label consistency on difficult subjective tasks without full expert reannotation.
- **Exact Match Ratio for multi-attribute prediction**: requires correct prediction of all attributes simultaneously, capturing the difficulty of jointly modeling multiple harm dimensions. Useful for values benchmarks that want to measure holistic scenario understanding.
- **Multilingual parallel design with same annotation scheme**: enables direct comparison of model capabilities across languages for the same semantic phenomenon, revealing language-specific vs. universal patterns in hate speech detection.
- **False positive analysis as a core evaluation**: systematically identifying cases where swear words used humorously trigger false positives reveals robustness gaps. Any values benchmark should include adversarial "benign but superficially harmful" items.

## 12. Notable quotes
- "HatEval has been one of the most popular tasks in SemEval-2019 with a total of 108 submitted runs for Subtask A and 70 runs for Subtask B, from a total of 74 different teams." (p.1)
- "No system has been able to outperform the MFC baseline [for English Subtask B], which achieved 0.580 of EMR." (p.7)
- "The false positive contains a swear word ('Bitch') used in a humorous, not offensive context, which is a potential source of confusion for a classifier." (p.8)
- "In the false negative, there a misogynistic message is expressed, although covertly, implying that the target should 'shut up and sing'." (p.8)

## 13. UNKNOWN / not in extract
- Full keyword sets used for tweet collection (linked to GitHub but not reproduced)
- Annotation guidelines text (linked to GitHub but not reproduced)
- Inter-annotator reliability statistics between the two expert annotators
- Whether the crowd annotation quality was assessed by annotator subgroup (gender, language background)
- Performance breakdown by target (immigrants vs. women) within systems
- Whether any system achieved substantially better results after the competition closed
