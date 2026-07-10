# Supplementary Materials: Do AI Systems Understand Religious Values?

## Table S3: Format Taxonomy

The 12-code format taxonomy used to classify benchmark task designs (feature P1). Harness compatibility reflects ease of integration with standard LLM evaluation frameworks (e.g., lm-evaluation-harness, HELM).

| Code | Name                        | Description                                       | Harness Compatibility |
|------|-----------------------------|---------------------------------------------------|-----------------------|
| MCQ  | Multiple Choice             | Fixed answer choices (A/B/C/D)                    | High                  |
| MRC  | Machine Reading Comprehension| Extract answer from passage                      | High                  |
| BIN  | Binary Classification       | Yes/No, Halal/Haram, True/False                   | High                  |
| TXT  | Text Classification         | Classify passages by tradition/theme              | High                  |
| SHT  | Shared Task                 | Competition format with train/dev/test splits     | High                  |
| SCN  | Scenario-based              | Present dilemma, evaluate response quality        | Medium                |
| PSY  | Psychometric/Survey         | Likert or forced-choice value statements          | Medium                |
| MIX  | Mixed Format                | Multiple formats combined                         | Medium                |
| OPN  | Open-ended Generation       | Free-text theological response                    | Low                   |
| MTN  | Multi-turn Dialogue         | Conversational theological engagement             | Low                   |
| RAG  | Retrieval-Augmented         | Retrieval from sacred texts + generation          | Low                   |
| MUL  | Multimodal                  | Visual + text (religious imagery, calligraphy)    | Low                   |

## Table S5: Meta-Evaluation Criteria

Seven qualitative criteria for assessing benchmark quality along dimensions that numerical composite scoring cannot fully capture (Section 3.4). Each criterion is rated on the specified scale by the expert council.

| #  | Criterion             | Description                                                                                                                                                   | Rating Scale                                                                 |
|----|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| 1  | Content Validity      | Distinguishes benchmarks testing genuine theological reasoning from those testing factual recall; assessed by classifying a 20-item sample by engagement level | HIGH / MEDIUM / LOW theological engagement                                   |
| 2  | Discriminative Power  | Checks for ceiling and floor effects by examining score ranges across model families                                                                          | STRONG (wide spread) / MODERATE / WEAK (ceiling or floor effects present)    |
| 3  | Cultural Authenticity | Records whether benchmark authors are scholars from the tradition (NATIVE), consulted tradition-specific experts (CONSULTED), or worked without consultation   | NATIVE / CONSULTED / EXTERNAL                                                |
| 4  | Reproducibility       | Applies a five-item checklist: publicly available data, evaluation code, defined scoring metrics, documented prompts, and inter-annotator agreement            | 0--5 checklist items satisfied                                               |
| 5  | Complementarity       | Measures unique dimensions a benchmark adds to the selection across tradition, task type, cognitive level, language, and domain                                | 1--5 scale (number of unique dimensions contributed)                         |
| 6  | Construct Coverage    | Maps each benchmark to the dimensions of religious values alignment it measures                                                                                | Subset of: Knowledge, Reasoning, Values, Sensitivity, Pluralism, Contextualization |
| 7  | Annotation Quality    | Records how gold-standard answers were determined                                                                                                             | EXPERT THEOLOGIAN / DOMAIN SCHOLAR / CROWDWORKER / AUTOMATIC                 |
