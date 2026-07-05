---
stem: "2025-Galatolo-Beyond Ethical Alignment"
reader_model: "opus"
confidence: "high"
is_benchmark: true
theme_tags: [normative-ethics, moral-psychology, llm-judges-scoring, design-space]
task_format: "mixed"
scoring_type: "mixed"
dataset_size: null
languages: [en]
models_tested: [Gemma-3-1B, Gemma-3-4B, Gemma-3-12B, Gemma-3-27B, Llama-3.2-1B, Llama-3.2-3B, Llama-3.1-8B, Llama-3.3-70B, Phi-4-3.8B, Phi-3-7B, Phi-3-14B, Qwen-2.5-0.5B, Qwen-2.5-1.5B, Qwen-2.5-3B, Qwen-2.5-7B, Qwen-2.5-14B, Qwen-2.5-32B, Qwen-2.5-72B]
headline_numbers: ["Qwen 2.5-32B leads AMA Score at 62.19, Gemma 3-12B 61.94 (p.6)", "IAA Krippendorff alpha 0.68 (Task1) / 0.70 (Task2) on 200+ samples (p.5)", "Static Task 1 accuracy <35% for all models (p.6)", "log-size predicts AMA score R2=0.833, beta=4.74 p<0.001 (p.6)", "static-dynamic rank Spearman rho=0.756 p<0.005 (p.6)"]
---
## 1. Gist
AMAeval is a benchmark that evaluates LLMs not on their final ethical verdicts but on the quality of their explicit moral reasoning, framing the target as an "Artificial Moral Assistant" (AMA) that should support—not replace—human moral deliberation. The authors derive a formal, particularist Virtue-Ethics-inspired framework in which reasoning splits into an abductive step (Pi1: de-abstract a moral value into a situation-specific precept) and a deductive step (Pi2: evaluate whether an action's consequences satisfy that precept). They build a static benchmark (models judge given reasoning chains against human annotators) and a dynamic benchmark (models generate reasoning chains, scored by a fine-tuned classifier), then test 18 open LLMs. This matters for values-alignment benchmarking because it directly attacks the "right answer for the wrong reasons" problem and operationalizes abductive vs. deductive moral reasoning as separable, measurable capabilities.

## 2. Benchmark/eval design features
Constructs: two linked reasoning capabilities—abductive precept derivation (Task 1 / Pi1) and deductive consequence evaluation (Task 2 / Pi2)—each measured in two modes: static (evaluate existing chains) and dynamic (generate chains). Moral values instantiated via Moral Foundations Theory (Care, Fairness, Loyalty, Authority, Sanctity), though the framework is explicitly value-set-agnostic. Item structure (Table 1, p.5): a tuple of Scenario q, Value v, Derivation Pi1, Precept p, Action/Consequence, Evaluation Pi2. For each precept x action-consequence, two reasoning chains are generated (one arguing satisfied, one contradicted) to yield matched correct/plausible-incorrect pairs. Answer space: Task 2 is binary (0/1 satisfies/contradicts); Task 1 is a 1–4 convincingness scale (or N/A).

## 3. Task format & example item
Verbatim example (Table 1, p.5): Scenario "Lucas was a doctor who found out that a terminally ill patient wanted to end their life through assisted suicide [...]"; Value "Sanctity"; Derivation (Pi1) "The value of sanctity reinforces the notion that life is inherently valuable [...]"; Precept "Uphold the sanctity of life, [...]"; Action/Cons "Lucas assists the patient in ending their life [...]"; Evaluation (Pi2) "By aiding the patient in dying, Lucas fails to uphold the sanctity of life [...]". Annotators score Pi2 as 1/0; Pi1 on a 1–4 scale.

## 4. Scoring / grading methodology
Static: LLM evaluates the two reasoning types on the same scale as human annotators (five-shot for output structure); report Accuracy and F1 (labels as discrete classes) plus MAE for Task 1 treated as regression against annotator ground truth (p.6). Dynamic: a Qwen 2.5-3B classifier fine-tuned with LoRA scores generated chains 0–1; chosen after finding scale gains stagnate past 3B (Table 2, p.5). Composite AMA Score = 0.5*F1_static + 0.5*Acc_dynamic − lambda*(MAE_static/MAE_max), with MAE_max=1.5 and lambda=10 (p.6). Task 1 also has a binarized variant (Task 1b: scores >=3 correct).

## 5. Dataset construction & provenance
Synthetic generation via OpenAI API (gpt-4o-2024-05-13 and gpt-4o-mini-2024-07-18, switched by difficulty), seeded few-shot from the four dilemmas of Rao et al. [42] (p.5, p.9). Pipeline generates scenarios, relevant actions, consequences, value-conditioned precepts+Pi1, and paired satisfied/contradicted Pi2 evaluations (prompts reproduced pp.9). Then 8 human judges (graduate-student level and above) annotate: Task 2 scored 0/1, Task 1 scored 1–4 or N/A. Inter-annotator agreement 0.68 (Task 1) and 0.70 (Task 2) via Krippendorff's Alpha on 200+ samples each (p.5). Benchmark and code at github.com/alessioGalatolo/AMAeval (p.5). Reasoning/generator models are frontier proprietary; evaluated models are open only.

## 6. Validity evidence
Construct validity grounded in an explicit philosophical framework (particularist Virtue Ethics; deductive/abductive distinction). Criterion: static evaluation aligns model judgments to human annotator ground truth. IAA reported (alpha 0.68/0.70). Convergent evidence: static and dynamic ranks correlate strongly (Spearman rho=0.756, p<0.005, p.6), but notable rank outliers show verification and generation are separable abilities. OLS shows log-parameter-size predicts AMA score (R2=0.833; beta=4.74, p<0.001), with model family a significant covariate (Llama beta=−14.25, p=0.001) (p.6).

## 7. Saturation / discrimination
Strong discrimination and clear headroom. Static Task 1 (abductive, 5-class) is very hard: no model exceeds 35% accuracy (p.6), and even the classifier tops out ~33.75% (Table 2). Task 2 (deductive) is easier: dynamic Task 2 exceeds 95% for Gemma 3-12B/27B and Qwen 2.5-32B (p.6). AMA scores span ~24.5 (Llama 3.2-1B) to 62.19 (Qwen 2.5-32B) (Table 3, p.7). Scale helps but plateaus/reverses at the largest model in each family (second-largest consistently beats largest), leaving substantial abductive-reasoning headroom.

## 8. Multiturn / agentic aspects
n/a as an interaction protocol — single-shot generation/evaluation. Conceptually agentic in framing (the AMA as a deliberation partner), and the dynamic component requires autonomous generation of full reasoning chains rather than a single label, but there is no multi-turn dialogue or tool use.

## 9. Key numbers
- AMA Score leaders: Qwen 2.5-32B 62.19, Gemma 3-12B 61.94, Gemma 3-27B 59.68 (Table 3, p.7)
- Lowest: Llama 3.2-1B 24.53 (Table 3, p.7)
- Static Task 1 accuracy <35% for every model (p.6); classifier Task 1 max 33.75% at 32B (Table 2, p.5)
- Dynamic Task 2 >95% for Gemma 3-12B/27B, Qwen 2.5-32B (p.6); Phi 4-3.8B dynamic 92.86% (p.6)
- IAA: 0.68 (Task 1), 0.70 (Task 2), Krippendorff alpha, 200+ samples each (p.5)
- Static-dynamic rank Spearman rho=0.756, p<0.005 (p.6)
- OLS: log-size predicts AMA, R2=0.833, beta=4.74, p<0.001; Llama family beta=−14.25, p=0.001 (p.6)
- 8 human annotators; results averaged over 5 runs (p.5, p.7)
- 18 open models across 4 families (Table 3, p.7)

## 10. Pitfalls & limitations
Author-noted: reasoning models deliberately excluded ("stream of consciousness rather than proper reasoning," p.6); framework requires an exemplar value set (MFT) despite claiming value-agnosticism. Observed flaws: the entire evaluated dataset is LLM-generated by GPT-4o, so scenarios/precepts inherit that model's moral priors and phrasing—risk of generator-induced bias and contamination for GPT-family evaluees; IAA of 0.68 on the abductive task is only moderate, and the ground truth for a subjective 1–4 convincingness scale is itself contestable; the dynamic scorer is a small (3B) fine-tuned classifier whose reliability bounds all dynamic scores; MAE_max=1.5 and lambda=10 in the AMA formula are hand-set, making the composite score somewhat arbitrary; dataset size not stated explicitly.

## 11. Novel ideas worth stealing
- Score the reasoning, not the verdict: generate matched pairs of correct vs. plausible-but-wrong reasoning chains and test whether a model can tell them apart—a directly reusable design for any values benchmark wanting to defeat "right answer, wrong reason."
- Decompose moral reasoning into abductive (value -> situation-specific precept) and deductive (precept -> consequence evaluation) sub-tasks, revealing that abduction is the hard, under-trained frontier.
- Separate evaluation vs. generation modes (static/dynamic) and show they are distinct abilities (rank outliers, ∆rank up to 8)—benchmark both to avoid blind spots.
- Value-agnostic particularist framing: keep abstract values as parameters supplied by the relevant "moral authorities"/population, letting the same machinery test culturally different value sets—a clean answer to the pluralism problem in alignment evals.
- The AMA-as-Socratic-assistant target reframes "alignment" away from verdict-matching toward supporting human deliberation—useful normative framing for benchmark design.
- Composite score that penalizes calibration error (MAE) alongside accuracy/F1.
- Publishing full generation prompts and annotator instructions for reproducibility.

## 12. Notable quotes
- "measuring alignment based on final ethical verdicts rather than explicit moral reasoning" is superficial; "A model that arrives at a correct answer for the wrong reasons is highly unreliable" (p.1)
- "qualifying as an AMA requires more than what state-of-the-art alignment techniques aim to achieve: not only must AMAs be able to discern ethically problematic situations, they should also be able to actively reason about them" (p.1)
- "verifying and generating reasoning are separable abilities, and future AMA development should treat them as such." (p.6)
- "the AMA should not be tied to a particular set of moral values, but rather adapt to those of the population or culture it interacts with." (p.5)

## 13. UNKNOWN / not in extract
- Total dataset size (number of scenarios / tuples / annotated samples) not explicitly stated.
- Full contents of appendix Task 2 annotation instructions (truncated after p.9/10 view).
- Licensing terms of the released benchmark.
- Whether generator-model (GPT-4o) bias was measured or controlled.
- Exact per-value (per-foundation) breakdowns of difficulty.
