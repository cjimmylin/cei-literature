---
stem: "2025-Chen-MoVa Towards Generalizable Classification of Human Morals and Values"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [moral-psychology, normative-ethics, validity-psychometrics, cultural-linguistic]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: 16
dataset_construction: "mixed"
languages: [en]
models_tested: [GPT-4o-mini, DeepSeek-V3, GPT-3.5-turbo, LLaMA-3-8B, DeepSeek-LLaMA-8B, LLaMA-3-70B, GPT-4, Mformer, BERT, ALBERT, CLAVE-LLaMA, Tuning-Mistral]
headline_numbers: ["all@once (MoVa) prompt yields F1 gains of 0.03 to 0.25 over 1-by-1 across MFT foundations (p.5)", "Authority F1 doubled 0.21 to 0.43; Sanctity tripled 0.14 to 0.38 (p.5)", "MoVa best in 12 of 20 cases vs 30k-example fine-tuned GPT-4o-mini (p.7)", "PVQ: 17 of 40 questionnaire items multi-loaded with 2-3 dimensions (p.9)", "16 labeled datasets across 4 frameworks (p.1)"]
---
## 1. Gist
MoVa is a benchmark suite and prompting method for generalizable classification of human morals and values in text. It assembles 16 labeled datasets across four theoretically grounded frameworks — Moral Foundations Theory (MFT), Schwartz Human Values, Morality-as-Cooperation (MAC), and Common Morality — and demonstrates that a simple LLM prompting strategy ("all@once") outperforms fine-tuned models across new data domains, new dimensions, and new frameworks. It matters for values-alignment benchmarking because it (a) operationalizes multiple competing moral frameworks as a single multilabel classification task, (b) shows label-dependency exploitation (via a classifier-chain analogy) beats independent binary classification, and (c) introduces a novel application: auditing psychological survey items for cross-loading using an LLM classifier. The stated downstream motivation is aligning machine behavior, with LLM-generated text as a key labeling use case (p.1).

## 2. Benchmark/eval design features
Constructs measured: MFT's 5 foundations (Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation) plus the emerging Liberty/oppression foundation; Schwartz's 10 human values; MAC's 7 cooperation dimensions (Family, Group, Reciprocity, Heroism, Deference, Fairness, Property); Common Morality's 10 rules (do not kill, cause pain, disable, deprive of freedom/pleasure, deceive, break promises, cheat, break the law, do your duty) (p.2, p.8). Item structure: multilabel classification — each text gets none/one/more labels, chosen deliberately over multiclass because moral dimensions co-occur (p.3). Answer space: binary relevance (0/1) per dimension, output as JSON; ValueNet uses a 3-class scheme (-1 oppose, 0 unrelated, 1 support) (p.7). Datasets partitioned into four generalization groups: In-domain (MFTC/eMFD/MFRC), New-domain (SC, MIC, ARGS, VIG, ValEval-MFT), New-framework (Human Values, MAC, Common Morality datasets), and New-application (three psychometric questionnaires) (p.3).

## 3. Task format & example item
Verbatim MFT prompt (p.4): "Task: You will receive a piece of morality-related text. Your job is to determine whether each of the five dimensions of moral foundations is relevant in the text... Output 1 if a dimension is present and 0 if it is not... Provide the answer in JSON format: {\"Care/Harm\": , \"Fairness/Cheating\": , \"Loyalty/Betrayal\": , \"Authority/Subversion\": , \"Sanctity/Degradation\": }". Example item (MFTC, p.6): "We don't have a Cop Problem in America. We have a Parenting Problem. Teach your kids to OBEY THE LAW. #AllLivesMatter" — labeled Authority (human=1, MoVa=1).

## 4. Scoring / grading methodology
Automated multilabel classification scored against human/expert/crowd gold labels using F1 (macro and per-dimension), AUC (from extracted LLM token probabilities), and accuracy. LLM output probabilities extracted by re-normalizing the summed probabilities of token "0" and token "1" when found in the top-K output tokens (p.4-5); not applied to DeepSeek-V3 (API lacks log-prob support). Threshold calibration used for sparse-label datasets (MAC-D: 95th percentile of predicted probabilities as cutoff, p.8). Classifier-chain analysis explains all@once gains: predicting each label conditioned on the other four MoVa-predicted labels (p.5).

## 5. Dataset construction & provenance
16 datasets: 13 public + 3 psychometric questionnaires. Eight MFT, three Human Values, one each MAC and Common Morality (p.3). Five resources reformulated by authors into classification tasks (MoralChoice, VIG, and the three questionnaires MFQ/MAQ/PVQ). Sources span Twitter (MFTC), news (eMFD), Reddit (MFRC), social norms/rules-of-thumb (SC, MIC), arguments (ARGS, Webis-22), ethnographies (MAC-D from eHRAF), and curated social scenarios (ValueNet). Annotators mix expert and crowd (Table 1, p.3). Sizes range 29 to 34,987; avg word length 7.6 to 108.8. Data/code released at github.com/ZiyuChen0410/MoVa2025 (p.1). Authors deliberately excluded frameworks derived from LLM-generated text to reduce dataset bias (p.3).

## 6. Validity evidence
Human baselines reported for Liberty on MIC (human F1 shown vs BERT/ALBERT, p.7). Cross-framework qualitative agreement/disagreement analysis in Table 2 (p.6) reveals label noise and subjectivity. The survey-auditing application provides indirect construct-validity evidence: across MFQ/MAQ/PVQ there are no false negatives per dimension (recall=1.0), but many items are multi-loaded, indicating questionnaire items measure unintended constructs (p.9). Mformer (authors' prior RoBERTa model) remains in-domain SOTA, providing a fine-tuned upper reference (p.6). No inter-rater reliability statistics or formal factor analyses reported in the extract.

## 7. Saturation / discrimination
Considerable headroom remains: in-domain MFT F1 scores are modest (e.g., Sanctity only 0.38 even after tripling, p.5). MAC-D scores are low across dimensions (max ~0.46 F1) due to severe class imbalance (most categories <5% of 2,436 examples; Fairness <1%, p.8). MoralChoice F1 ranges 0.41-0.95 depending on rule and ambiguity (p.8). Webis-22 US in-domain macro F1 only 0.44 (p.7). No ceiling effects — the task remains hard, with fine-tuned and prompted models both far from perfect, indicating good discrimination and remaining difficulty.

## 8. Multiturn / agentic aspects
n/a — single-turn classification prompting; no tool use or interactive environment.

## 9. Key numbers
- 16 labeled datasets, 4 frameworks; 13 public + 3 questionnaires (p.1, p.3)
- all@once F1 gains 0.03-0.25 over 1-by-1 across MFT foundations (p.5)
- Authority F1 0.21→0.43; Sanctity 0.14→0.38 (p.5)
- Classifier chain improves over 1-by-1 by 0.09-0.29 (p.5)
- MoVa best in 12 of 20 dimension-dataset cases vs 30k fine-tuned GPT-4o-mini; that fine-tune beats Mformer in 17 of 20 (p.7)
- ARG loyalty/sanctity AUC 0.83/0.82 (MoVa) slightly below Mformer 0.85/0.83 (p.6)
- ValEval-MFT: MoVa perturbed accuracy 0.91; out-of-domain 0.60 (p.6)
- VIG Liberty F1: MoVa 0.97, MoVa-DeepSeek 0.87 (p.7)
- ValueNet: MoVa-DeepSeek overall accuracy 0.64, best F1 all classes (p.7)
- ValEval-Schwartz out-of-domain accuracy 0.87 (MoVa/MoVa-DeepSeek) (p.8)
- MoralChoice F1: MoVa 0.41-0.81 low-ambiguity, 0.48-0.95 high-ambiguity (p.8)
- MAC-D: most categories <5% of 2,436 examples, Fairness <1% (p.8)
- PVQ 17/40 items multi-loaded; MFQ 4/30; MAQ 12/42 (p.9)
- 45 pages total (p.1 metadata)

## 10. Pitfalls & limitations
Author-admitted: primarily English-language and Western-grounded frameworks; LLM biases (Western-centric training) may skew scores; classification imperfect so aggregate analyses more reliable than individual-level outputs; did not cover all models incl. open-source (p.10). Reasoning prompts did not help ("MoVa+reason" underperformed, p.5). Visible flaws: label noise and annotator subjectivity acknowledged (Example B liberty disagreement, p.6); AUC/probability method inapplicable to DeepSeek-V3, so metrics differ across models; threshold calibration at 95th percentile is a strong post-hoc adjustment that could inflate MAC-D results; small dataset sizes for several questionnaires (29-42 items) limit statistical power; no formal reliability statistics; frameworks are pre-selected, side-stepping the "which framework" normative question the authors themselves flag.

## 11. Novel ideas worth stealing
- **all@once multilabel prompting**: score all related constructs simultaneously in one prompt rather than 1-by-1, letting the LLM exploit inter-label dependencies — a cheap, generalizable design move for any multi-construct values benchmark (p.4).
- **Classifier-chain analysis as an explanation tool**: feed a model's own predictions of sibling labels back in when predicting a target label to quantify how much of the gain comes from label dependency (p.5).
- **Generalization taxonomy**: explicitly partition eval data into In-domain / New-domain / New-dimension / New-framework / New-application groups — a reusable scaffold for measuring benchmark generalizability rather than single-domain fit (p.3).
- **Survey-item auditing with an LLM classifier**: use the classifier to detect cross-loaded (multiply-loaded) questionnaire items and then LLM-reword them to isolate a single intended construct — directly applicable to validating alignment survey instruments (p.9).
- **Framework-leveling motivation**: making under-resourced moral frameworks usable by removing the need for per-framework annotated training data (p.10).
- **Deliberate exclusion of LLM-generated frameworks** to avoid circular/self-referential dataset bias (p.3).
- **Multilabel over multiclass** framing because moral dimensions co-occur in the real world (p.3).

## 12. Notable quotes
- "the key to stronger classification performance lies in prompting LLMs to label all constructs at once (all@once), rather than one at a time (1-by-1)" (p.2)
- "Our aim for MoVa is deliberately set to only scoring relevance rather than making judgments, leaving ambiguous and high-stake decisions to humans." (p.9)
- "we believe that part of the reason some frameworks are used more frequently... is the availability of resources, such as annotated data and computation." (p.10)
- "all questionnaires have multiple items loaded with more than one dimension. PVQ has the highest percentage (17 out of 40) of multi-loaded questions" (p.9)

## 13. UNKNOWN / not in extract
- Full appendix details (Sections A-I, pages 11-45) not read: exact per-dataset licensing, full prompt texts, fine-tuning/query cost figures (Section C.IX), label-order permutation stability details, and complete per-dimension result tables.
- No inter-rater reliability (kappa) or formal factor-analysis statistics found in main text.
- Exact human baseline F1 numbers for MIC Liberty are shown only in a figure (approximate values not machine-legible in OCR).
- Precise dataset splits/train-test sizes beyond the 80:20 fine-tune split and reported subset counts.
