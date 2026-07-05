---
stem: "2024-Matei-Enhancing Romanian Offensive Language Detection through Knowledge"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [best-practices, cultural-linguistic]
task_format: "n/a"
scoring_type: "classifier"
dataset_size: 12447
dataset_construction: "crowdsourced"
languages: ["ro"]
models_tested: ["BERT-base-ro-cased", "DistilBERT-base-ro"]
headline_numbers:
  - "MTKD-TA achieves 82.40% accuracy and 82.34% F1 on RO-Offense, outperforming BERT-ro baseline by ~3.5% (p.10, Table 1)"
  - "Knowledge distillation alone (KD) drops ~1.5% below BERT-ro teacher (p.10, Table 1)"
  - "MTKD surpasses BERT-ro by ~2.3% and MTL by ~3.3% (p.10)"
  - "Best data augmentation combination (ASDA+RoGPT-2+Noisy-20%+MixUp Sent.-15%) reaches 78.71% F1, equalizing BERT-ro teacher with 53% fewer parameters (p.12)"
---
## 1. Gist
This paper investigates methods for detecting offensive language in Romanian, a low-resource language with limited annotated data. It explores three complementary strategies applied to the RO-Offense dataset (12,447 records with four categories: Insult, Profanity, Abuse, Other): fine-tuning BERT, knowledge distillation to a smaller DistilBERT student, data augmentation techniques (RoGPT-2, ASDA, MixUp, Noisy Student), and multi-task learning combined with knowledge distillation (MTKD) and teacher annealing (TA). The paper is relevant to the COOKBOOK as a methodological case study showing how to bootstrap offensive language detection in low-resource languages using auxiliary tasks and efficient model compression — directly applicable to building values-alignment evaluators for non-English languages.

## 2. Benchmark/eval design features
This is a systems paper, not a benchmark creation paper. The primary task is four-class classification of Romanian text comments into Insult, Profanity, Abuse, and Other using the RO-Offense dataset. Three auxiliary tasks are used in the MTL framework: emotion classification (REDv2, 7 classes), sentiment analysis (LaRoSeDa, binary positive/negative), and sexist language detection (CoRoSeOf, binary sexist/non-sexist). The key experimental contribution is ablation analysis of: (a) which data augmentation technique is most effective, (b) whether MTL helps or hurts without distillation, (c) whether adding teacher annealing to MTKD improves student performance.

## 3. Task format & example item
n/a. This paper does not include example items from the RO-Offense dataset. The task is text classification: given a Romanian social media comment, output one of {Insult, Abuse, Profanity, Other}. No verbatim items are shown in the extract.

## 4. Scoring / grading methodology
Evaluation metrics: accuracy (Acc), precision (P), recall (R), and weighted F1-score (F1). Ablation study uses F1 as the primary metric (Table 3). Knowledge distillation temperature T and interpolation parameter alpha (controlling balance between soft teacher predictions and hard ground truth) are key hyperparameters: MTKD uses T=4, alpha=0.6; MTKD-TA uses T=2 for most tasks and T=7 for emotion detection with lambda linearly increased from 0 to 1 during training. AdamW optimizer, learning rate 2e-5, batch size 16.

## 5. Dataset construction & provenance
Primary: RO-Offense — 12,447 annotated Romanian comments, four classes: Profanity (13%), Insult (23%), Abuse (28%), Other (36%). Names of individuals/organizations anonymized. Publicly available at HuggingFace (readerbench/ro-offense). Split: 80/10/10.

Auxiliary datasets:
- REDv2 (Romanian Emotions Dataset): 5,449 manually verified tweets, 7 emotion classes. Split 75/10/15.
- CoRoSeOf: 39,245 Romanian tweets, sexist/non-sexist (binary). Split 80/10/10.
- LaRoSeDa: 15,000 e-commerce reviews, binary sentiment. Split 80/10/10.

All datasets publicly available on GitHub/HuggingFace. No explicit licensing issue noted.

## 6. Validity evidence
The paper does not report inter-annotator reliability for RO-Offense or the auxiliary datasets. Validation uses held-out test sets. Results are compared against fine-tuned BERT-ro as the primary baseline. Ablation study (Table 3) systematically removes auxiliary tasks to assess contribution of each. No statistical significance testing (e.g., bootstrap intervals) reported.

## 7. Saturation / discrimination
BERT-ro baseline achieves 78.83% F1 — leaving ~21% headroom. The best model (MTKD-TA) reaches 82.34%, closing some of the gap but well below 90%. The RO-Offense dataset is relatively small (12,447 examples), which the authors identify as the key data constraint. Data augmentation alone can recover the teacher's performance using a 53% smaller model (DistilBERT-ro), suggesting the dataset is already somewhat saturated for the distilled student capacity.

## 8. Multiturn / agentic aspects
n/a. This is a single-turn text classification task.

## 9. Key numbers
- RO-Offense size: 12,447; class distribution: Profanity 13%, Insult 23%, Abuse 28%, Other 36% (p.9)
- BERT-ro (teacher) baseline: 78.63% Acc, 78.83% F1 (p.10, Table 1)
- KD (distilled DistilBERT-ro): 77.10% Acc, 77.23% F1 — ~1.5% drop (p.10, Table 1)
- MTKD: 81.36% Acc, 81.19% F1 — ~2.3% above teacher (p.10, Table 1)
- MTKD-TA: 82.40% Acc, 82.34% F1 — ~3.5% above teacher (p.10, Table 1)
- Best data augmentation (combined): 78.71% F1 — equaling teacher with 53% fewer parameters (p.12)
- Noisy Student alone: best single augmentation, +0.8% over KD student (p.12)
- MTKD-TA outperforms MTKD by ~1% (p.11)
- DistilBERT-ro: 6 layers, 81M parameters, 312MB; BERT-ro: 12 layers, 124M parameters, 477MB (p.9)

## 10. Pitfalls & limitations
- No inter-annotator reliability for any dataset used
- No statistical significance testing; point estimates only
- Class imbalance in RO-Offense (Other 36% vs. Profanity 13%) not explicitly addressed
- Sexist language auxiliary task shows inconsistent effects (helps MTKD-TA but hurts plain MTL), suggesting task compatibility is not guaranteed
- Single language (Romanian); findings may not generalize to other low-resource languages
- Small primary dataset (12K) limits generalizability conclusions
- No error analysis by class or by text type
- Teacher annealing temperature for emotion detection task (T=7) was identified empirically; no principled selection method described

## 11. Novel ideas worth stealing
- **Multi-task knowledge distillation with teacher annealing (MTKD-TA)**: using related auxiliary tasks (emotion, sentiment, sexism detection) as simultaneous teachers to distill a more capable student model for offensive language detection consistently outperforms both plain MTL and plain KD — a transferable recipe for low-resource values-classification problems.
- **Auxiliary task selection rationale**: the paper's choice of emotion, sentiment, and sexism detection as auxiliary tasks for offensive language detection is principled and documented; this provides a template for choosing complementary tasks when building a values-alignment classifier.
- **Data augmentation hierarchy for NLP**: the paper's finding that Noisy Student > ASDA > RoGPT-2 > MixUp Encoder for low-resource text augmentation provides practical guidance for datasets too small to train large models.
- **Parameter-efficiency framing**: showing that an augmented small model can match a large teacher model establishes that efficiency does not require performance sacrifice — relevant for deploying values-alignment evaluators at scale.

## 12. Notable quotes
- "The intricate nature of identifying offensive language stems from the nuanced considerations of contextual factors, multiple meanings, and emerging expressions." (p.1)
- "The MTKD model significantly improves over prior experiments. It surpasses the performance of the teacher model by ~2.3%, the distilled student by ~3.9%, and the MTL model by ~3.3%." (p.10)
- "In the end, we achieve an advantage improvement of 1.58% over the distilled student alone, equalizing the performance of the BERT-ro teacher, which has 53% more parameters." (p.12)
- "Achieving an optimal balance between the contributions of different tasks in the MTL environment proved challenging." (p.13)

## 13. UNKNOWN / not in extract
- Inter-annotator agreement statistics for RO-Offense or auxiliary datasets
- Error analysis by class (which of Insult/Profanity/Abuse/Other is hardest)
- Whether hyperparameter tuning was done on dev set or test set
- Inference speed comparison between DistilBERT-ro student and BERT-ro teacher
- Whether the fine-tuned models are publicly released
