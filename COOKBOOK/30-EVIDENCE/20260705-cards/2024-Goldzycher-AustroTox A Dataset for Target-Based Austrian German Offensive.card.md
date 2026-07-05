---
stem: "2024-Goldzycher-AustroTox A Dataset for Target-Based Austrian German Offensive"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [cultural-linguistic, validity-psychometrics, design-space, contamination-robustness]
task_format: "mixed"
scoring_type: "classifier"
dataset_size: 4562
dataset_construction: "crowdsourced"
languages: ["de"]
models_tested: ["GPT-3.5 (gpt-3.5-turbo-1106)", "GPT-4 (gpt-4-1106-preview)", "LeoLM 7B Chat", "Mistral 7B", "GBERT-base", "GBERT-large", "BERTde", "BERT-dbmdz", "GELECTRA"]
headline_numbers:
  - "4,562 Austrian German comments annotated with offensiveness, target spans, vulgarity spans (p.1)"
  - "Krippendorff's Alpha α=0.49 on binary offensiveness classification (p.4)"
  - "GPT-4 5-shot: macro F1 0.81 on offensiveness; GBERT-large: 0.75 (p.5)"
  - "GPT-4 outperforms fine-tuned models on offensiveness but not vulgarity/target extraction (p.5)"
---
## 1. Gist
AustroTox is the first German-language offensive language dataset to include token-level span annotations, covering both the targets of offensive statements (group, individual, or other) and vulgar language passages. Sourced from DerStandard, a major Austrian newspaper forum, the 4,562-comment corpus represents Austrian German dialect — a linguistic variant underrepresented in NLP toxicity research. The paper evaluates fine-tuned BERT/Electra models against GPT-3.5 and GPT-4 in zero- and five-shot settings across three tasks: binary offensiveness classification, vulgarity span extraction, and target span extraction. Results show GPT-4 outperforms fine-tuned models on offensiveness detection, but fine-tuned models excel at detecting dialect-specific vulgarities. For values-alignment benchmarking, AustroTox is relevant as a testbed for culturally-grounded, sub-national linguistic norm enforcement and as a model for span-annotated toxicity datasets that enable model interpretability.

## 2. Benchmark/eval design features
Three tasks are defined: (1) binary offensiveness classification (sequence-level), (2) vulgarity extraction (token-level), (3) target extraction (token-level with four classes: Group, Individual, Other, and a combined "More Target Types"). The annotation scheme distinguishes between offensiveness (disparagement toward persons/groups or incitement to hate/violence) and vulgarity (obscene/foul language that may co-occur with non-offensive content). This orthogonal structure — where a comment can be vulgar but not offensive, or offensive but not vulgar — is a notable design move.

Context is provided via article titles, making this a contextual rather than decontextualized toxicity task. The aggregation rule prioritizes sensitivity: a post requires fewer pro-offensive votes to be labeled offensive than non-offensive votes to be labeled non-offensive.

## 3. Task format & example item
Verbatim example from annotation guidelines (p.9):

"Arguments? If this group of vaccination refusers could be reached with reason and arguments, our situation would be different."
- Class: Insult
- Span Target Group: vaccination refusers
- Span Vulgarity: group [dialectal vulgarity in original German]

LLM prompt (zero-shot, German, p.12): System message defines offensiveness and vulgarity; user message provides article title and comment; model responds in JSON with Label (0/1) and Tags array.

## 4. Scoring / grading methodology
Ten-fold cross-validation. Binary and Macro F1 for offensiveness classification at post level. Binary and Macro F1 for vulgarity extraction at token level. Micro F1 (summing TP/FP/FN across three target classes) for target span extraction. GPT models use GBERT tokenizer to align span predictions for fair comparison.

## 5. Dataset construction & provenance
Source: DerStandard Austrian newspaper forum, November 4–10, 2021 (responding to 532+ articles). Pre-filtered via Perspective API stratified sampling (strata: 0–0.3, 0.3–0.5, 0.5–0.7, 0.7–0.9 toxicity score; all comments scoring 0.9–1.0 included). 123,108 posts scored; 4,562 selected for annotation. Annotators: Master's and undergraduate students in Data Science and Linguistics (predominantly Austrian, ages 19–26, ≥C1 German). Each annotator handled 200–300 comments. Majority of posts annotated by 5 annotators. 390 posts with implausible spans were curated out. Splits: 80/10/10 train/dev/test, stratified by fine-grained label class. Data published at https://www.pia.wien/austrotox/

## 6. Validity evidence
Krippendorff's Alpha α=0.49 on binary offensiveness — comparable to related crowdsourcing work (Sap et al. 2020: 0.51; Wulczyn et al. 2017: 0.45). Below the α≥0.667 threshold for "tentative conclusions" in prescriptive annotation paradigms, which the authors acknowledge. The sensitivity-prioritizing aggregation rule is offered as a partial mitigation. Disaggregated binary annotations are published alongside aggregated labels, enabling alternative aggregation strategies.

## 7. Saturation / discrimination
GPT-4 binary offensiveness F1: 0.76 (5-shot), 0.70 (0-shot); GBERT-large: 0.73. Score spread across models is moderate (0.30–0.81), indicating good discrimination. Vulgarity extraction is harder: fine-tuned models achieve Binary F1 ~0.69–0.71; LLMs ~0.36–0.43, suggesting the dialectal vulgarity task remains challenging for LLMs. Target extraction Micro F1 is generally low (0.17–0.24) due to class imbalance.

## 8. Multiturn / agentic aspects
n/a. All classification is single-turn over individual comments with article title context.

## 9. Key numbers
- 4,562 comments: 2,744 non-offensive, 1,818 offensive (p.4)
- 437 non-offensive but vulgar; 1,106 offensive and vulgar (p.4)
- Target distribution: Group 869, Individual 572, Other 275 (p.4)
- Krippendorff's α = 0.49 (p.4)
- GPT-4 5-shot macro F1 offensiveness: 0.81 (p.5)
- GBERT-large binary F1 offensiveness: 0.73 (p.5)
- Fine-tuned models vulgarity Binary F1: ~0.69–0.71 vs. GPT-4: 0.41 (p.5)
- Training split: ~80% (~3,650 comments); dev/test: ~10% each (p.4)

## 10. Pitfalls & limitations
- Time-restricted corpus (one week) with over-representation of COVID-19 topics (p.6)
- Annotator demographics are young and predominantly Austrian; limited coverage of other German-speaking communities
- Low inter-annotator agreement (α=0.49) for a prescriptive annotation task
- Small annotator pool with limited training time introduces subjectivity
- LLM experiments are not exhaustive; larger German encoder-only models (GELECTRA-large) not evaluated
- No hyperparameter search conducted for fine-tuning experiments
- Annotation restricted to original comments, excluding reply threads (context loss)

## 11. Novel ideas worth stealing
1. **Orthogonal vulgarity and offensiveness annotation**: Separating vulgar language from offensive intent is a powerful design move. For values-alignment benchmarks, this maps cleanly to distinguishing style violations from content violations — a crucial distinction for measuring model responses to uncivil but non-harmful speech.
2. **Sensitivity-prioritizing aggregation**: Requiring fewer votes for the "harmful" label than the "non-harmful" label is a principled approach to asymmetric error costs. Applicable wherever false negatives (missed harm) cost more than false positives.
3. **Marking vulgar spans before LLM offensiveness classification**: The paper suggests using fine-tuned models to mark vulgarities and then passing marked text to GPT-4, potentially improving GPT-4 performance on dialect-specific cases. This "ensemble preprocessing" idea is generalizable to pipeline architectures for culturally-specific evaluation.
4. **Disaggregated annotation release**: Publishing raw per-annotator labels alongside aggregated gold labels enables downstream researchers to experiment with alternative aggregation schemes, including soft labeling and perspectivism.
5. **Stratified pre-filtering via API scores**: Using Perspective API toxicity scores to stratify sampling ensures both high-toxicity coverage and representative non-toxic baseline — a practical sampling strategy for rare-event annotation tasks.

## 12. Notable quotes
- "Model interpretability in toxicity detection greatly profits from token-level annotations. However, currently such annotations are only available in English." (p.1)
- "Intolerant user comments (e.g., offensive stereotyping), in contrast to incivil user comments (e.g., vulgarity), are perceived as more offensive and as a stronger threat to democratic values and society." (p.1)
- "The results indicate that while fine-tuned models excel in detecting linguistic peculiarities such as vulgar dialect, large language models demonstrate superior performance in detecting offensiveness in AustroTox." (p.1)
- "The span annotations allow for analysis beyond comparing disagreements with binary gold labels." (p.5)

## 13. UNKNOWN / not in extract
- License terms for the AustroTox dataset (mentioned as published but not specified in extract)
- DerStandard data sharing agreement specifics
- Whether the annotation tool LightTag captures adjudication audit trails
- Exact proportion of comments from each of the 532 articles/forums
- Whether any inter-annotator disagreements were analyzed by annotator identity or demographic characteristics
