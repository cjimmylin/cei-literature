---
stem: "2025-Weber-Digital Guardians Can GPT-4 Perspective API and Moderation API"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [best-practices, llm-judges-scoring, validity-psychometrics, cultural-linguistic]
task_format: "MCQ"
scoring_type: "exact-match"
dataset_size: 1592
dataset_construction: "crowdsourced"
languages: ["de"]
models_tested: ["gpt-4o-2024-05-13", "Perspective API", "Moderation API", "GBERT-base"]
headline_numbers:
  - "GPT-4o One-Shot achieves Champion-Challenger score S=0.7059, ~5pp above HOCON34k BERT baseline S=0.652 (p.6)"
  - "After reannotation, GPT-4o One-Shot S=0.8268, recall=0.9493 (p.8)"
  - "Reannotation identified ~78–96 potentially incorrect labels out of 1,592 (error range 10%, CI 90%) (p.7)"
  - "Inter-rater reliability of HOCON34k test subset: Fleiss' Kappa κ=0.6078 (p.3)"
  - "Perspective API with τ=0.8 detected only 6 of 329 hate speech samples (p.6)"
  - "GPT-4o accuracy on unanimously confirmed reannotated texts: 100% (p.8)"
---
## 1. Gist
This paper evaluates three automated hate speech detection tools — GPT-4o (with Zero-Shot, One-Shot, and Few-Shot prompting), Google's Perspective API, and OpenAI's Moderation API — against the German-language HOCON34k dataset of reader comments from online newspapers. It matters for values-alignment benchmarking because it demonstrates that (a) a well-prompted LLM can outperform purpose-built content moderation APIs on a real-world classification task without fine-tuning, (b) dataset annotation quality is a critical confounder of benchmark scores, and (c) LLM-assisted reannotation can meaningfully improve ground truth quality, albeit with bias risks.

## 2. Benchmark/eval design features
The study frames hate speech detection as a binary classification task (Hate Speech vs. No Hate Speech). The evaluation uses a subset of 1,592 test samples from HOCON34k, annotated by 12 professional moderators and experts with a lead moderator. Each of the seven experimental conditions (GPT4-Z, GPT4-O, GPT4-F, PAPI-038, PAPI-05, PAPI-08, MAPI) is run three times to assess output consistency. Metrics include Recall, Precision, F1-score, F2-score (which weights recall twice), Matthews Correlation Coefficient (MCC), and the composite Champion-Challenger score S = (MCC_norm + F2) / 2 that balances false negatives against false positives. The core claim is that GPT-4o One-Shot outperforms both specialized APIs and the fine-tuned BERT baseline on S score.

## 3. Task format & example item
The GPT-4o Few-Shot prompt (in German) first presents hate speech guidelines, provides four labeled examples, then asks: "Is the following text in quotation marks considered hate speech? Answer exclusively with Yes or No: 'Sie haben doch einen an der Palme.'" — the model must return only "Ja" or "Nein" (p.5).

## 4. Scoring / grading methodology
Binary mapping of model output to Hate Speech (1) or No Hate Speech (0). For GPT-4o: output "Yes"/"Ja" → 1. For Moderation API: overall `flagged == True` → 1. For Perspective API: if maximum category score exceeds threshold τ → 1. Metrics computed as averages across three repeated runs. The composite S score (p.4) balances the F2-score (recall-heavy) with a normalized MCC to prevent either purely recall-maximizing or purely precision-maximizing solutions from winning.

## 5. Dataset construction & provenance
HOCON34k (Hatespeech in Online Comments from German Newspapers): 34,223 total examples from comment sections of TZ and Frankfurter Rundschau newspapers. Annotated by 29 individuals including professional moderators, researchers, and IT specialists. The test subset of 1,592 samples was annotated by 12 experts with Fleiss' Kappa κ=0.6078 (p.3). Class distribution: 329 hate speech (20.67%), 1,263 non-hate speech (79.33%). The reannotation process used GPT-4o Zero-Shot to flag 314 discrepant labels, which three human annotators then adjudicated blind, resulting in 1,591 samples with 401 hate speech (25.2%) (p.8). Licensing and public availability of HOCON34k not fully specified in paper.

## 6. Validity evidence
Inter-rater reliability for the test subset is substantial (κ=0.6078). The reannotation study found 5 of 91 sampled texts unanimously agreed to have incorrect original labels, projecting to 78–96 errors in 1,592 samples (p.7). GPT-4o's 100% accuracy on unanimously confirmed reannotated texts suggests it tracks high-quality annotation well. Limitation: the reannotation process itself was seeded by GPT-4o disagreements, creating a potential circular bias favoring GPT scores on reannotated data.

## 7. Saturation / discrimination
The dataset is heavily imbalanced (~80/20), which inflates Accuracy for any high-precision, low-recall classifier. The Perspective API with τ=0.8 exemplifies this: only 6 positive predictions from 329 hate speech items, yielding near-perfect Precision but S=0.288 (p.6). The composite S metric partially addresses this. GPT-4o variants cluster in a moderate performance band (S≈0.69–0.71), with room for improvement even after reannotation (best S=0.8268 still leaves recall at 94.93%).

## 8. Multiturn / agentic aspects
n/a — all evaluations are single-pass classification requests to each API.

## 9. Key numbers
- Test set: 1,592 samples; 329 (20.67%) hate speech (p.3)
- Fleiss' Kappa κ=0.6078 for test subset annotation (p.3)
- GPT-4o One-Shot S=0.7059 vs. BERT baseline S=0.652 on original data (p.6)
- GPT-4o One-Shot S=0.8268 on reannotated data, a 17.13% increase (p.8–9)
- BERT baseline S improved from 0.652 to 0.723 (+10.89%) after reannotation (p.9)
- Perspective API τ=0.8: only 6 TP out of 329 positives (p.6)
- Moderation API: S=0.6327 original, 0.7068 reannotated (p.6, 8)
- Estimated 78–96 annotation errors in original 1,592 test samples (p.7)

## 10. Pitfalls & limitations
- **Reannotation bias**: only labels where GPT-4o disagreed were reviewed; this systematically biases post-reannotation scores in favor of GPT-based models (p.9).
- **Non-determinism**: GPT-4o and Moderation API outputs vary slightly across repeated runs even for identical inputs; Perspective API appears deterministic but was not formally tested (p.7).
- **Definition mismatch**: Perspective API and Moderation API use broader definitions than HOCON34k (e.g., self-harm content is covered but German unconstitutional speech is not), limiting direct comparability (p.7).
- **Class imbalance**: 80/20 split makes simple accuracy misleading; not addressed by oversampling or weighting.
- **No fine-tuning**: GPT-4o used with no task-specific training; fine-tuned BERT-type models typically outperform zero/few-shot approaches at this scale.
- **Language specificity**: Perspective API had difficulty with German dialects and non-standard character strings without explicit language specification (p.6).

## 11. Novel ideas worth stealing
- **Composite recall-precision metric**: The Champion-Challenger score S = (MCC_norm + F2) / 2 is a reusable design for any classification benchmark where false negatives are more costly than false positives (content moderation, safety evaluation). Adapt by choosing the F-beta weight to reflect domain-specific asymmetry.
- **LLM-assisted annotation review pipeline**: Using the LLM under evaluation to identify potential annotation errors for human review is efficient but must be carefully controlled for confirmation bias. A cleaner design would use a different model for the triage step.
- **Three-run consistency check**: Running each condition three times and averaging (with variance tracking) is a low-cost way to quantify non-determinism in LLM evaluators — directly applicable to any LLM-judge scoring setup.
- **Reannotation as a benchmark improvement loop**: The paper demonstrates that starting with a good-enough dataset, then using LLM assistance + human adjudication, can improve ground truth quality by ~10–17% in model scores. This cycle can be used for iterative benchmark refinement.

## 12. Notable quotes
- "Correcting annotation errors resulted in over 10% improvement across most models, including the HOCON34k classifier." (p.9)
- "Although the final decision to adjust labels was made by annotators, independent of GPT's assessments, the selective review may introduce a bias in favor of GPT." (p.9)
- "Different definitions of hate speech or harmful speech for the various solutions limit their comparability." (p.7)
- "The texts are primarily in German. In addition, some test data include foreign languages or internet links. Individual texts in the dataset contain spelling and grammar errors, colloquial and dialectal expressions, or simply unintelligible character strings." (p.3)

## 13. UNKNOWN / not in extract
- Full license and public availability terms for HOCON34k dataset
- Whether few-shot examples were balanced for hate speech vs. non-hate speech
- Cost/latency comparison across the three APIs
- Statistical significance tests for performance differences between conditions
- Inter-annotator agreement statistics for the reannotation phase
