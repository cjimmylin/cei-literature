---
stem: "2021-Taulé-Overview of DETOXIS at IberLEF 2021 DEtection of TOXicity in comments"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, validity-psychometrics, cultural-linguistic, llm-judges-scoring]
task_format: "classifier"
scoring_type: "classifier"
dataset_size: 4359
dataset_construction: "scraped"
languages: ["es"]
models_tested: ["BETO", "XLM", "TF-IDF+SVC", "Random Forest", "Logistic Regression"]
headline_numbers:
  - "31 teams participated in Subtask 1 (toxicity detection), 24 teams in Subtask 2 (toxicity level detection) (p.7)"
  - "Best system SINAI achieved F1=0.6461 in Subtask 1 (p.12)"
  - "SINAI achieved CEM=0.7495 in Subtask 2; Gold Standard CEM=1.0 (p.13)"
  - "Inter-annotator agreement: 81.99% for toxicity, Krippendorff alpha=0.59 (p.3)"
  - "Dataset: 4,359 comments, 31.16% toxic; 996 mildly toxic, 310 toxic, 79 very toxic (p.5)"
---
## 1. Gist
DETOXIS was a shared task at IberLEF 2021 targeting toxicity detection in Spanish-language comments posted in response to immigration-related online news. The task is unusual in offering two related subtasks — binary toxicity detection and fine-grained 4-level toxicity severity classification — on a dataset annotated with 13 auxiliary linguistic features (argumentation, sarcasm, stereotype, mockery, etc.). For values-alignment benchmarking, DETOXIS matters because it shows how Spanish-language, non-English hate-speech evaluation works in practice, demonstrates multi-metric evaluation design for ordinal classification problems, and provides a case study in how social-media toxicity (a core value-harm construct) is operationalized across cultural and linguistic contexts.

## 2. Benchmark/eval design features
Two subtasks share the same NewsCom-TOX corpus:
- **Subtask 1**: Binary classification (toxic vs. not-toxic). Official metric: F1-score (toxic class only).
- **Subtask 2**: 4-class ordinal toxicity level (0=not toxic, 1=mildly toxic, 2=toxic, 3=very toxic). Official metric: Closeness Evaluation Measure (CEM), a non-equidistant ordinal metric that weights rare categories more heavily.

Four metrics for Subtask 2: CEM, Rank Biased Precision (RBP), Mean Absolute Error, Pearson correlation, and accuracy — deliberately chosen because they capture different use-scenarios (e.g., RBP for "find the most toxic first", Pearson for "track average toxicity trends").

13 auxiliary features annotated in training data: argumentation, constructiveness, stance (positive/negative), target (person/group), stereotype, sarcasm, mockery, insult, improper language, aggressiveness, intolerance.

## 3. Task format & example item
Classifier task — given a comment plus thread context (thread_id, comment_level, reply_to), predict toxicity class.

Example (from p.3):
```
(4a) A estos putos animales sarnosos que los encierren y tiren la llave.
     <toxicity=yes> <toxicity level=3>
(4b) With these mangy fucking animals, lock them up and throw away the key.
     <toxicity=yes> <toxicity level=3>
```

## 4. Scoring / grading methodology
- Subtask 1: Precision, Recall, F1-measure on the toxic class.
- Subtask 2 (primary): CEM — accounts for proximity between predicted and real ordinal categories, does not assume equidistance, weights infrequent categories more heavily.
- Subtask 2 (secondary): RBP (ranking metric, appropriate for priority-queue use case), MAE (assumes equidistance), Pearson correlation (scale correlation), Accuracy.
- Multiple metrics allow different downstream applications to pick the appropriate metric for their deployment scenario.

## 5. Dataset construction & provenance
NewsCom-TOX corpus: 4,359 comments from 21 articles in Spanish online newspapers (ABC, elDiario.es, El Mundo, NIUS, etc.) and forums (Menéame, ForoCoches), collected August 2017 to July 2020 (p.2). Articles selected manually for controversial subject matter (immigration), minimum 50 comments. Comments presented in chronological thread order; author anonymized.

Split: 80% training (3,463 comments), 20% test (896 comments) (p.4). Training data includes all 13 auxiliary features; test data contains only thread_id, comment_id, reply_to, comment_level, comment.

Annotation: 3 parallel annotators (2 expert linguists + 2 trained students), disagreements resolved by senior annotator. Data distributed privately to participants due to IPR concerns.

## 6. Validity evidence
Inter-annotator agreement (Table 1, p.3-4):
- Toxicity (binary): 81.99% average observed agreement, Krippendorff α=0.59
- Toxicity level (4-class): 73.95% observed agreement, Krippendorff α=0.62

The paper notes these are "quite acceptable considering the difficulty of both tasks" (p.3). Error analysis (p.8-9) reveals that implicit signals (sarcasm, stereotype, aggressiveness, mockery) are hardest: CEM scores for aggressiveness subset drop to 0.3892 for the top-5 systems, vs. 0.8929 for constructiveness.

## 7. Saturation / discrimination
Best Subtask 1 F1=0.6461 vs. Gold Standard (implicit 1.0); significant gap remains. Precision range across teams 0.25–0.75 (p.4). Best Subtask 2 CEM=0.7495 vs. Gold Standard 1.0 (p.13). Severe discrimination problems for high-toxicity categories (levels 3 = 79 examples, 1.81% of dataset) — model correctly zero-predicted these in error analysis. Dataset imbalance is a known challenge.

## 8. Multiturn / agentic aspects
Thread structure is provided (thread_id, comment_level, reply_to). One team (Alejandro Mosquera) incorporated thread context and showed improvements (p.8). Context is not mandatory for the evaluation but is available to participants.

## 9. Key numbers
- Dataset size: 4,359 comments (p.4)
- Toxic proportion: 31.16% (p.2)
- Level distribution: mildly toxic 21.90%, toxic 7.36%, very toxic 1.81% (p.5)
- Inter-annotator agreement toxicity: α=0.59 (p.4)
- Inter-annotator agreement level: α=0.62 (p.4)
- 31 teams in Subtask 1, 24 in Subtask 2 (p.7)
- Best F1 Subtask 1: SINAI 0.6461 (p.12)
- Best CEM Subtask 2: SINAI 0.7495 (p.13)
- RandomClassifier Subtask 1 F1: 0.3761 (p.12)
- Vocabulary: 21 articles, 65–359 comments per article (p.2)

## 10. Pitfalls & limitations
- Spanish-only; multilingual models (XLM) underperformed language-specific BETO (p.9)
- Severe class imbalance (level 3 = 79 examples) makes evaluation of extreme toxicity unreliable
- Implicit toxicity (sarcasm, aggressiveness) is systematically hard: aggressiveness CEM=0.3892 for top-5 systems (p.9)
- Data distributed privately due to IPR, limiting reproducibility
- Thread-based context usage was explored by only one team; its systematic benefit remains understudied
- Error analysis (Table 4, p.10) shows many false-negatives involve politically charged comments with seemingly neutral surface wording

## 11. Novel ideas worth stealing
1. **Multi-metric evaluation for ordinal harm**: Using CEM, RBP, MAE, and Pearson simultaneously, with explicit justification for which metric fits which deployment scenario (moderation queue vs. trend monitoring). This framework could be directly reused for values-alignment benchmarks that involve ordinal severity judgments.
2. **Auxiliary feature annotation for error analysis**: Annotating 13 linguistic features (sarcasm, mockery, etc.) in training data, then systematically measuring model performance per-feature (Table 3) — powerful diagnostic tool revealing where models fail.
3. **Thread-aware evaluation**: Including thread_id and reply context, allowing researchers to measure how context-usage affects detection — a rarely exploited feature in standard benchmarks.
4. **CEM metric** (Closeness Evaluation Measure): Ordinal classification metric that does not assume equidistance between categories and down-weights majority-class hits — more appropriate than accuracy for imbalanced ordinal tasks common in values benchmarking.

## 12. Notable quotes
- "DETOXIS is the first task that focuses on the detection of different levels of toxicity in comments posted in response to news articles written in Spanish." (p.1)
- "The presence of implicit stereotypes rather than explicit ones in hate speech posts which ultimately require models to learn related world knowledge beforehand is well known." (p.8)
- "Depending on the final application and its specific requirements, the selection of the model may require a different evaluation metric." (p.9)
- "Even the most recent transformer models struggle with linguistic devices users sometimes use such as sarcasm or irony." (p.8)

## 13. UNKNOWN / not in extract
- Exact annotation guidelines and codebook content
- Full per-team methodology descriptions (only summarized)
- Whether the NewsCom-TOX corpus has since been made publicly available
- Inter-annotator agreement per-article or per-feature
- Details of SINAI system architecture beyond multi-task learning with sentiment/emotion
