---
stem: "2023-Hamad-Offensive Hebrew Corpus and Detection using BERT"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, design-space]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: 15881
dataset_construction: "crowdsourced"
languages: ["Hebrew"]
models_tested: ["HeBERT", "AlephBERT"]
headline_numbers:
  - "Dataset of 15,881 Hebrew tweets annotated for offensive language (p.1)"
  - "AlephBERT achieves 86% accuracy on DOLaH test set (D4 config) (p.6)"
  - "Model trained on our data achieves 69% accuracy on DOLaH; reverse yields only 57% — suggesting better generalizability (p.6)"
  - "HeBERT boosted by 2% when combined with DOLaH data (p.5)"
  - "73 total changes made by external reviewer across 1,314 offensive tweets — indicating high annotator agreement (p.4)"
---
## 1. Gist
This paper presents a new Hebrew-language offensive language corpus of 15,881 tweets collected from Twitter, annotated for offensive content using five categories: abusive, hate, violence, pornographic, and none. Two Hebrew BERT models (HeBERT and AlephBERT) are fine-tuned on the dataset and compared across eight dataset configurations mixing this new corpus with the existing DOLaH dataset. The paper matters for values-alignment benchmarking because it exemplifies the challenge of building culturally-grounded, low-resource offensive language datasets: annotation requires deep cultural and political familiarity (with Israeli/Palestinian political context), definitions of offensiveness are culturally relative, and domain differences between datasets degrade cross-dataset generalization even for closely related data.

## 2. Benchmark/eval design features
This is a dataset and classification paper, not a benchmark per se. The dataset contains 15,881 tweets annotated with:
- **Class label**: hate, abusive, violence, pornographic, or none (multi-label permitted)
- **Target**: the individual or group being offended (inferred if not explicit)
- **Topic**: the subject of the offensive content (war, elections, etc.)
- **Offensive phrase**: the specific phrase(s) driving the classification

Key finding: The dataset is heavily imbalanced — only 1,200 tweets (7.5%) are offensive. The authors subsampled to 2,500 (balanced) for training experiments. AlephBERT consistently outperforms HeBERT, likely due to larger vocabulary (52K vs 30K tokens) and additional Twitter training data. Cross-dataset evaluation reveals poor generalization between differently-sourced Hebrew corpora (Twitter vs. Facebook), attributed partly to different annotation guidelines and community norms.

## 3. Task format & example item
Annotators labeled tweets with class, target, topic, and offensive phrase. Example from paper (p.6):

Tweet: "גירוש, הריסת בתים, מאסרי עולם ללא אפשרות חנינה, אחרת יהיה עוד יותר גרוע. להתייחס אליהם כמו אל מחבלים."
Translation: "Deportation, demolition of houses, life sentences without the possibility of amnesty, otherwise it will be even worse. Treat them like terrorists."
Annotation: Class: Violence, Hate; Target: Palestinians; Topic: punish Palestinians; Phrase: Deportation, Demolition of houses, life sentences, terrorists

## 4. Scoring / grading methodology
Binary classification (offensive vs. not offensive) for model training. Evaluation metric: accuracy. Authors also report F1-score in related work discussion. The annotation review process counted the number of label changes made by an external bilingual reviewer — this served as a proxy for agreement rather than computing formal inter-annotator agreement (IAA) statistics (full IAA was not possible due to annotator unavailability).

## 5. Dataset construction & provenance
- **Collection period**: December 2020 – January 2021 via Twitter API
- **Seed keywords**: 55 Hebrew keywords (reduced from 147 by removing inflections) covering politically sensitive terms like "terrorist," "Nakba," "Gaza," "rape," "murder"
- **Size**: 15,881 tweets, deduplicated and retweet-free
- **Annotators**: 3 graduate students (Arabic-Hebrew bilingual Palestinians from Haifa, familiar with Israeli politics/culture), overseen by an expert
- **Each annotator labeled ~5,300 tweets**; annotations reviewed by expert
- **Review**: 3,355 tweets (21%) re-examined by an external bilingual reviewer; 73 changes to offensive labels, 88 changes to target labels
- **Balance**: 1,200 offensive, 14,681 non-offensive; subsampled to 2,500 for experiments
- **License/availability**: Public on GitHub and HuggingFace (SinaLab/OffensiveHebrew)

## 6. Validity evidence
- The review process found only 73/1,314 changes to offensive sub-class labels, suggesting reasonable annotation consistency
- Cross-dataset evaluation (D7/D8 configurations) provides some evidence of dataset characteristics: model trained on the new data achieves 69% on DOLaH test set vs. 57% for the reverse, suggesting broader coverage
- No formal inter-annotator agreement (Kappa, Fleiss, etc.) was computed — authors acknowledge this as a limitation and plan to revisit
- The annotator selection criteria (bilingual, culturally informed) are justified on validity grounds given the cultural specificity of Hebrew offensive language

## 7. Saturation / discrimination
- The dataset is highly imbalanced (1,200 offensive out of 15,881 = 7.5%), limiting utility for fine-grained model training without resampling
- Best accuracy on the new dataset: 68% (AlephBERT, D1 config) — considerably lower than the 86% on DOLaH, suggesting the new dataset is harder and less saturated
- The hate sub-class (631 tweets) dominates offensive content, followed by violence (454), abusive (124), and pornographic (4)
- The four-class split (pornographic has only 4 examples) makes multi-class performance analysis unreliable

## 8. Multiturn / agentic aspects
n/a — single-turn text classification task.

## 9. Key numbers
- 15,881 total tweets in corpus (p.1)
- 1,200 offensive tweets (7.5% of corpus): 631 hate, 454 violence, 124 abusive, 4 pornographic (p.5, Table III)
- 14,681 not-offensive tweets (p.5)
- 55 keywords used for data collection (p.3)
- Average tweet length: 25.3 characters, std dev 14.9 (p.3, Table II)
- 3 annotators, each labeling ~5,300 tweets (p.4)
- 3,355 tweets reviewed externally (21% of dataset) (p.4)
- 73 total changes to offensive label across 1,314 offensive tweets (p.4)
- AlephBERT 86% accuracy on DOLaH (D4 config) vs HeBERT 79% (p.5-6)
- Cross-dataset: AlephBERT trained on new data → 69% on DOLaH; AlephBERT trained on DOLaH → 57% on new data (p.6)
- HeBERT boosted from 79% to 81% when DOLaH augmented with our data (p.5)

## 10. Pitfalls & limitations
- **No formal IAA**: Full inter-annotator agreement was not computed due to annotator unavailability (p.7)
- **Keyword-bias**: Data collected using predefined keywords may miss offensive content outside those lexical patterns, and over-represents politically charged content
- **Single domain**: All data from Twitter; may not generalize to Facebook, YouTube, or other platforms
- **Severe class imbalance**: Only 7.5% offensive content; pornographic subclass has only 4 examples
- **Cultural specificity risk**: Annotators were all Palestinian/Arab-Hebrew bilingual — Jewish Israeli perspectives on what constitutes offense may differ
- **Cross-dataset incompatibility**: The mismatch with DOLaH (Facebook data) shows how annotation guideline differences undermine benchmark reuse
- **No temporal coverage**: Collection was limited to Dec 2020–Jan 2021, missing major events in ongoing conflict

## 11. Novel ideas worth stealing
- **Annotation beyond binary**: Annotating target, topic, and offensive phrase in addition to binary label — this richer schema supports more nuanced evaluation of hate detection models
- **Generalizability testing via cross-dataset evaluation**: Testing D7/D8 configurations (train on A, test on B and vice versa) is a clean way to measure dataset breadth and generalization
- **Cultural expertise as selection criterion**: Explicitly requiring annotators to have cultural and political familiarity is a design principle worth encoding in annotation guidelines for values-alignment benchmarks
- **Keyword-bootstrapped + expert-reviewed pipeline**: Broad keyword search → annotation by domain experts → external review is a replicable workflow for building culturally-specific corpora

## 12. Notable quotes
- "determining what is offensive in a given language is a challenging task since it highly relies on one's knowledge and familiarity with the linguistic and cultural aspects of that language" (p.1)
- "it is very likely that the annotation guidelines between the two datasets are different, e.g., what is offensive for one community might not be offensive for another." (p.6)
- "Due to the subjective and complex nature of deciding what is offensive (see section VII), we cannot consider the revised annotations to be more accurate." (p.4)
- "All annotators are Palestinians living in Haifa and are Arabic-Hebrew bilingual speakers. In addition, the students were selected based on their familiarity with Israeli politics and culture." (p.4)

## 13. UNKNOWN / not in extract
- Formal inter-annotator agreement statistics (Kappa/Fleiss) were not computed and not reported
- Licensing terms are not explicitly stated in the extract (only that it is available on GitHub/HuggingFace)
- Model hyperparameter ablations beyond those reported
- Whether the dataset includes dialectal Hebrew or only Modern Standard Hebrew
- Whether the keyword list introduces systematic biases toward specific political viewpoints
