---
stem: "2025-Bulla-Large Language Models meet moral values"
reader_model: "sonnet"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, normative-ethics, llm-judges-scoring, validity-psychometrics]
task_format: "free-text"
scoring_type: "classifier"
dataset_size: 5594
dataset_construction: "scraped"
languages: ["en"]
models_tested: ["GPT-4", "GPT-3.5", "Llama-3-70B", "Llama-2-7B", "Mistral-7B", "Mixtral-8x7B", "NLI-RoBERTa"]
headline_numbers:
  - "GPT-4 achieves F1=0.55 on multi-label MFT value detection (double-prompt), outperforming all other models (p.7)"
  - "GPT-4 and GPT-3.5 outperform human annotators in 3 of 5 moral dimensions (p.13)"
  - "GPT-4 binary moral detection accuracy=0.86, F1=0.81 in optimal configuration (p.12)"
  - "All models performed significantly better on Everyday than USA Politics subcorpus; GPT-4: F1=0.61 vs 0.49 (p.8)"
  - "Human annotator average F1 across 5 MFT dimensions: 0.59 weighted; GPT-4: 0.66 weighted (p.14)"
---
## 1. Gist
Bulla et al. (2025) conduct a comprehensive evaluation of LLMs as zero-shot and few-shot unsupervised classifiers for moral value detection using Moral Foundation Theory (MFT). The study tests GPT-4, GPT-3.5, Llama-3-70B, Llama-2-7B, Mistral-7B, Mixtral-8x7B, and an NLI-RoBERTa baseline on the Moral Foundation Reddit Corpus (MFRC), comparing both single-prompt and double-prompt configurations. A key contribution is a novel human-model comparison framework that places human annotators and models on equal footing by holding out each annotator from the gold standard and treating them as a "human predictor." The paper matters for values-alignment benchmarking because it provides a rigorous cross-model comparison of moral classification performance, reveals significant domain-sensitivity (everyday vs. political contexts), and demonstrates that frontier LLMs now match or exceed average human annotators in several MFT dimensions while still falling short of the best human on the hardest dimensions.

## 2. Benchmark/eval design features
The study operationalizes five MFT dimensions: Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, and Purity/Degradation. Two subtasks are evaluated: (1) multi-label moral value detection — identifying which MFT dimensions are present in a text; and (2) binary moral classification — determining whether a text contains any moral content. Two prompting configurations are compared: a single-prompt approach that addresses both tasks simultaneously, and a double-prompt approach that first performs binary classification and, if positive, then predicts the MFT dimensions. Both zero-shot and few-shot (6-shot, 12-shot) configurations are tested. Evaluation is done on two subcorpora: "Everyday Moral Life" (2,837 items) and "USA Politics" (2,757 items).

## 3. Task format & example item
The task is free-text moral classification. An example prompt from the single-prompt configuration (described in p.5): the model receives a Reddit comment as premise and is asked to identify whether the comment contains moral content and, if so, to predict which of the five MFT dimensions apply, producing binary yes/no judgments for each dimension. The double-prompt configuration first asks "Does this sentence contain moral content? Answer yes or no," and if yes, proceeds to multi-label detection.

No verbatim prompt text appears in the extract, but Figure 1 (p.5-6) shows the general structure.

## 4. Scoring / grading methodology
For multi-label detection: weighted precision, recall, and F1 score averaged across the five MFT dimensions, excluding Non-Moral items from the macro average to prevent bias from the more frequent non-moral class (p.7). For binary detection: accuracy and weighted F1. For the human-model comparison: a leave-one-annotator-out framework where each annotator is treated as a predictor against the consensus of remaining annotators. Gold standard is determined by majority vote (≥50% threshold). Metrics reported separately for EveryDay and USA Politics subcorpora.

## 5. Dataset construction & provenance
The Moral Foundation Reddit Corpus (MFRC) by Trager et al. (2022) is used. The full corpus contains 16,123 Reddit comments across three subcorpora (Everyday Moral Life: 5,366; USA Politics: 5,351; French Politics: 7,169). French Politics subcorpus was excluded due to low inter-annotator agreement (p.7). Items annotated by a single annotator or annotators with uncertain confidence were further excluded, yielding 2,837 Everyday items and 2,757 USA Politics items with 2-6 annotators each (p.7). Annotations follow MFT taxonomy; the Liberty/Oppression and Thin Morality dimensions were excluded or collapsed. The corpus is openly available. No explicit licensing information in the extract.

## 6. Validity evidence
Inter-annotator agreement is discussed as a known limitation — the paper explicitly excludes items with only one annotator and those with low confidence annotations to reduce subjectivity noise (p.7). The French Politics subcorpus was dropped due to low IAA. The human-model comparison framework is introduced specifically to address subjectivity concerns: rather than comparing models to a contested gold standard, each human annotator is compared to the consensus of remaining annotators (p.12-13). Human average weighted F1 in multi-label detection is 0.59 across five dimensions, providing a clear baseline for model comparisons.

## 7. Saturation / discrimination
Performance varies substantially across MFT dimensions, with Care and Fairness being the most discriminable (GPT-4 F1: 0.69 and 0.53, p.9) and Loyalty, Purity, and Authority being much harder (GPT-4 F1: 0.42, 0.37, 0.30 respectively under optimal configurations, p.9-10). No ceiling effects are apparent for the harder dimensions. Models consistently perform better on the Everyday subcorpus than USA Politics, suggesting that political context increases difficulty and subjectivity. Overall F1 scores range from 0.16 (NLI double-prompt) to 0.55 (GPT-4 double-prompt), leaving substantial headroom.

## 8. Multiturn / agentic aspects
n/a. All evaluations are single-turn classification tasks.

## 9. Key numbers
- MFRC dataset used: 2,837 Everyday + 2,757 USA Politics items = 5,594 total (p.7)
- GPT-4 overall F1 (multi-label, double-prompt): 0.55; single-prompt: 0.50 (p.7-8)
- GPT-3.5 overall F1 (multi-label, best): 0.50 (p.7-8)
- Llama-3-70B overall F1 (best): 0.45 (p.8)
- Mixtral overall F1 (best): 0.43 (p.8)
- Mistral overall F1 (best): 0.43 (p.8)
- Llama-2-7B overall F1 (best): 0.30 (p.8)
- NLI-RoBERTa overall F1 (best): 0.24 (p.8)
- GPT-4 binary accuracy (best, double-prompt): 0.86, F1: 0.81 (p.12)
- Human annotator average F1 (multi-label, leave-one-out): weighted 0.59, average 0.57 (p.14)
- GPT-4 vs. human: GPT-4 weighted 0.66, surpassing human average in multi-label detection (p.14)
- GPT-4 outperforms human in Care, Fairness, Purity, Loyalty dimensions; humans better in Authority average F1 (p.13)
- GPT-4 F1 for Care: 0.69 (EveryDay: 0.78); Loyalty: 0.42; Purity: 0.37; Authority: 0.30 (p.9-10)
- Few-shot: Mistral improves from F1=0.34 (0-shot) to 0.41 (12-shot); Mixtral 0.43 to 0.48 (p.11)

## 10. Pitfalls & limitations
- Low inter-annotator agreement for political content (France corpus dropped entirely, USA Politics consistently harder) — the gold standard is contested for politically charged text (p.7, p.8).
- Models are evaluated on a single Reddit-based corpus; generalization to other moral text domains is unknown.
- The French Politics subcorpus excluded: results may not reflect performance on contentious political discourse more broadly.
- GPT-4 in single-prompt configuration tends to classify more content as moral than necessary, suggesting sensitivity to prompt complexity (p.7).
- Smaller models (Llama-2-7B) show high recall but low precision, indicating a positive bias toward labeling content as moral (p.8, p.9).
- No contamination analysis: it is possible that GPT-4 and GPT-3.5 were trained on data that overlaps with MFRC.
- Human annotator comparison is limited to EveryDay subcorpus only (p.12).
- Hyperparameters (temperature=0.10, top-p=0.90) fixed across all models; optimal settings may differ per model.

## 11. Novel ideas worth stealing
- **Leave-one-annotator-out human baseline**: Rather than comparing a model to a fixed gold standard, compute performance of each human annotator vs. the remaining consensus, then compare models to that distribution. This directly addresses the "contested gold standard" problem for subjective tasks and is reusable in any moral/values benchmark. (p.12-13)
- **Double-prompt decomposition**: Separating binary (is this moral?) from multi-label (which dimensions?) as a two-step pipeline consistently improves multi-label detection for smaller models. This staged prompting strategy is useful when LLMs are tested on complex multi-attribute classification. (p.5-6)
- **Domain stratification to diagnose political sensitivity**: Including both everyday and politically charged subcorpora to test whether models perform differently by context. This reveals that moral detection is substantially harder in political contexts and motivates domain-specific evaluation for values benchmarks. (p.7-8)
- **Few-shot scaling curves per dimension**: Evaluating 0-shot, 6-shot, and 12-shot performance separately for each MFT dimension shows that some dimensions (Care, Fairness) benefit more from examples than others (Loyalty, Authority). This fine-grained analysis informs how many examples are needed per value category. (p.11)
- **Explicit exclusion of Non-Moral class from multi-label F1**: Removing the dominant Non-Moral label from macro-F1 computation prevents easy wins inflating performance scores — a methodological control directly relevant to imbalanced moral labeling datasets. (p.7)

## 12. Notable quotes
- "Our novel framework directly juxtaposes model outputs with human annotations. This head-to-head approach addresses subjectivity concerns by placing human and model ratings on equal footing." (p.2)
- "GPT-4 and GPT-3.5 consistently outperform human annotators in three of the five moral dimensions ('Care', 'Fairness', and 'Purity')." (p.13)
- "All models performed significantly better on 'EveryDay' content compared to 'USA Politics' content. This discrepancy is likely due to the greater difficulty and subjectivity of the tasks in the 'USA Politics' sub-corpus, which is supported by the lower level of inter-annotator agreement." (p.8)
- "Mistral exhibits superior performance in precision, indicating its ability to accurately identify relevant moral dimensions, [while] Llama-7B displayed significantly higher recall, suggesting a tendency to identify a broader range of moral dimensions, even potentially irrelevant ones." (p.8-9)

## 13. UNKNOWN / not in extract
- Exact prompt text for both single-prompt and double-prompt configurations is described but not verbatim-quoted in the extract (figures referenced but not fully OCR-readable).
- Table 10 (binary human-model comparison with individual annotator breakdown) not fully extracted.
- Inter-annotator agreement statistics (Krippendorff's alpha or Cohen's kappa) not reported or visible in the extract.
- Licensing information for MFRC dataset not stated.
- Computational cost and inference time for each model.
- Whether contamination between GPT-4 training data and MFRC was checked.
