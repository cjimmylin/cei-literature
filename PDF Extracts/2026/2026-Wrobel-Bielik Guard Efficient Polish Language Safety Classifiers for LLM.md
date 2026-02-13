---
title: "2026-Wrobel-Bielik Guard Efficient Polish Language Safety Classifiers for LLM - PDF Extract"
source_pdf: "2026-Wrobel-Bielik Guard Efficient Polish Language Safety Classifiers for LLM.pdf"
pages: 19
extracted_at: "2026-02-13T09:50:31.136030"
---

# PDF Extract: 2026-Wrobel-Bielik Guard Efficient Polish Language Safety Classifiers for LLM

**Source PDF:** 2026-Wrobel-Bielik Guard Efficient Polish Language Safety Classifiers for LLM.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

Krzysztof Wróbel
Jan Maria Kowalski
Jerzy Surma
Igor Ciuciura
Maciej Szymański
BIELIK GUARD: EFFICIENT POLISH
LANGUAGE SAFETY CLASSIFIERS FOR
LLM CONTENT MODERATION
Abstract
As Large Language Models (LLMs) become increasingly deployed in Polish lan-
guage applications, the need for efficient and accurate content safety classifiers
has become paramount. We present Bielik Guard, a family of compact Polish
language safety classifiers comprising two model variants: a 0.1B parameter
model based on MMLW-RoBERTa-base and a 0.5B parameter model based on
PKOBP/polish-roberta-8k. Fine-tuned on a community-annotated dataset of
6,885 Polish texts, these models classify content across five safety categories:
Hate/Aggression, Vulgarities, Sexual Content, Crime, and Self-Harm. Our eval-
uation demonstrates that both models achieve strong performance on multiple
benchmarks. The 0.5B variant offers the best overall discrimination capability
with F1 scores of 0.791 (micro) and 0.785 (macro) on the test set, while the 0.1B
variant demonstrates exceptional efficiency. Notably, Bielik Guard 0.1B v1.1
achieves superior precision (77.65%) and very low false positive rate (0.63%)
on real user prompts, outperforming HerBERT-PL-Guard (31.55% precision,
4.70% FPR) despite identical model size. The models are publicly available and
designed to provide appropriate responses rather than simple content blocking,
particularly for sensitive categories like self-harm.
Keywords
safety classification, content moderation, Polish NLP, LLM safety, guardrails,
multi-label classification
2026/02/12; 01:58
str.
1/19
arXiv:2602.07954v2  [cs.CL]  11 Feb 2026

--- Page 2 ---

1. Introduction
The rapid advancement of Large Language Models has revolutionized natural lan-
guage processing capabilities, enabling sophisticated conversational AI systems across
numerous domains [8]. However, this progress brings significant challenges in ensuring
safe and responsible deployment, particularly in multilingual contexts where safety
resources remain scarce [4].
For Polish language applications, the landscape of LLM safety tools has been
particularly limited. Existing solutions either rely on English-centric models adapted
to Polish with varying degrees of success, or employ large multilingual models that
may be impractical for resource-constrained deployments. The need for dedicated
Polish safety classifiers is further motivated by cultural and linguistic nuances that
affect what constitutes harmful content and how it should be moderated.
We introduce Bielik Guard (codenamed Sójka, meaning “jay” in Polish – a vigilant
bird symbolizing protection), a family of efficient safety classifiers specifically designed
for Polish language content. Our contributions include:
• Two compact model variants (0.1B based on MMLW-RoBERTa and 0.5B based
on PKOBP/polish-roberta-8k) optimized for deployment efficiency while main-
taining high accuracy
• A community-driven annotation methodology based on bounded rationality prin-
ciples [15], yielding 6,885 annotated Polish texts with over 60,000 individual rat-
ings
• A five-category safety taxonomy tailored to Polish language applications:
Hate/Aggression, Vulgarities, Sexual Content, Crime, and Self-Harm
• Comprehensive evaluation demonstrating superior precision and lower false pos-
itive rates compared to larger multilingual alternatives
• A response-oriented approach that provides appropriate support resources rather
than simple blocking, especially for self-harm content
The models are publicly available at https://huggingface.co/speakleash and
have been deployed in production at https://guard.bielik.ai/, where ongoing
community feedback continues to improve the system.
2. Related Work
2.1. LLM-based Safety Classifiers
The development of safety guardrails for LLMs has become a critical research area,
with comprehensive surveys covering the current state of the art [3, 1, 19]. Llama
Guard [4] pioneered the approach of using instruction-tuned language models for
input-output safety classification, introducing a taxonomy-based framework that al-
lows adaptation to different use cases. The subsequent Llama Guard 3 [8] extended
this work with an 8B parameter model supporting multilingual classification across
2026/02/12; 01:58
str.
2/19

--- Page 3 ---

14 MLCommons hazard categories, achieving F1 scores of 0.939 on English response
classification.
Similarly, Qwen3Guard [20] introduced three-tiered severity classification (safe,
controversial, unsafe) with support for 119 languages, offering models ranging from
0.6B to 8B parameters. ShieldGemma [17], based on the Gemma model family, pro-
vides content moderation capabilities with models of various sizes designed for differ-
ent deployment scenarios. Granite Guardian [13] extends beyond traditional harmful-
content detection by unifying prompt and response risk detection with coverage of
social bias, profanity, violence, sexual content, unethical behavior, jailbreaking, and
RAG-specific hallucination risks (context relevance, groundedness, answer relevance).
The 2B and 8B variants, trained on a combination of human-annotated and syn-
thetic data, achieve AUC scores of 0.871 and 0.854 on harmful-content and RAG
groundedness benchmarks respectively. These generative models frame safety as an
instruction-following task, enabling flexible deployment scenarios.
2.2. Polish Language Models and Safety
The development of Polish language models has accelerated in recent years.
The
Bielik family of models [12, 11, 10, 9] and the PLLuM family [5] represent significant
milestones in Polish LLM development, demonstrating the growing maturity of Polish
NLP infrastructure. These foundational models highlight the importance of dedicated
Polish language resources and the need for corresponding safety mechanisms.
For Polish-specific safety classification, HerBERT-PL-Guard [6] represents a sig-
nificant contribution, fine-tuning the HerBERT model on manually annotated data
and Polish translations of PolyGuard and WildGuard datasets. The model supports
classification into 15 categories based on the Llama Guard taxonomy, including both
safe and 14 unsafe categories.
However, existing Polish solutions face limitations: HerBERT-PL-Guard, while
comprehensive in its taxonomy, relies on translated data which may not capture
authentic Polish linguistic patterns. Multilingual models like Llama Guard 3, despite
their broad language coverage, exhibit higher false positive rates and lower precision
on Polish content, as our evaluation demonstrates.
2.3. Community-based Annotation
Our approach to data collection draws inspiration from crowdsourcing methodologies
in NLP while incorporating principles from bounded rationality [15]. Rather than
seeking an objective ground truth, we embrace the notion that safety judgments are
inherently subjective and context-dependent, making community consensus a more
appropriate target than expert-only annotation.
A key design assumption was that disagreements between annotators are not
noise but an informative signal reflecting ambiguity, cultural context, and individual
moral intuition. This is particularly relevant in the Polish language, where slang, id-
2026/02/12; 01:58
str.
3/19

--- Page 4 ---

iomatic expressions, and pragmatic meanings often blur the boundary between harm-
less and harmful intent.
To operationalize this assumption, we designed a lightweight, purpose-built an-
notation platform that allowed volunteers to label short text samples through a simple
survey interface. Texts were randomly assigned to annotators to minimize ordering
effects and individual bias. A visible counter of completed annotations was deliber-
ately introduced as a motivational mechanism, which proved effective in sustaining
engagement during the early, high-volume phase of the campaign.
Community engagement was not limited to a one-off data collection effort.
Instead, it continues through an ongoing public annotation interface available at
https://guard.bielik.ai/ankieta.html, enabling iterative dataset expansion and
future recalibration of the model as social norms evolve.
The annotation campaign was promoted through webinars, social media chan-
nels, and community-driven outreach around the Bielik ecosystem.
This resulted
in rapid scaling: over 25,000 annotations were submitted within the first week alone,
demonstrating both the accessibility of the interface and the willingness of non-expert
users to participate in AI safety–oriented initiatives.
3. Bielik Guard: Model Architecture and Training
3.1. Safety Taxonomy
Bielik Guard employs a five-category taxonomy designed specifically for Polish lan-
guage safety needs:
• HATE (Hate/Aggression):
Content attacking or discriminating against
groups based on race, religion, gender, sexual orientation, or nationality
• VULGAR (Vulgarities): Profane or vulgar language in both explicit and
masked forms
• SEX (Sexual Content): Graphic descriptions of sexual activities or requests
for erotic material generation
• CRIME: Instructions or encouragement for criminal activities including drug
production and fraud
• SELF-HARM: Content encouraging suicide, self-harm, or eating disorders
This taxonomy deliberately excludes categories like disinformation, jailbreaking
attempts, and copyright violations for several reasons: (1) these categories require
factual knowledge that may change over time, (2) detecting such content often requires
context beyond isolated text snippets, and (3) our community annotation process
focused on immediate safety risks that require active intervention or support. This
focused scope allows for more consistent annotation and clearer deployment guidelines.
3.2. Model Architecture
The two Bielik Guard variants employ different base models, chosen to explore dif-
ferent points in the efficiency-performance trade-off space:
2026/02/12; 01:58
str.
4/19

--- Page 5 ---

Bielik Guard 0.1B is built upon MMLW-RoBERTa-base [2], a 124M parameter
Polish RoBERTa-based encoder [7] with a vocabulary of 50,001 tokens, producing
768-dimensional representations.
Bielik Guard 0.5B is built upon PKOBP/polish-roberta-8k [14], a 443M pa-
rameter Polish RoBERTa variant with an enhanced vocabulary of 128,064 tokens,
providing substantially greater modeling capacity.
For both variants, we add a multi-label classification head [18] consisting of:
• A dropout layer (p=0.1) for regularization
• A linear projection layer mapping hidden dimensions to 5 output logits
• Sigmoid activation for independent binary classification per category
3.3. Training Data and Methodology
3.3.1. Data Collection
The training dataset comprises 6,885 unique Polish texts collected through large-scale
community engagement:
• Over 1,500 volunteers participated in annotation
• Each text received an average of 7–8 independent ratings
• A total of over 60,000 individual annotations were collected
• Sources included anonymized user prompts from Polish LLM interactions as well
as selected social media content
The resulting dataset exhibits a relatively balanced distribution, with approxi-
mately 55% of samples labeled as safe and 45% as harmful or potentially unsafe. This
balance was achieved deliberately to avoid over-representation of benign content while
preserving the prevalence of borderline and controversial cases observed in real-world
usage.
Rather than binarizing annotations, we trained the model on the percentage of
annotators who classified each text as belonging to a given category. This regression-
based labeling strategy preserves information about annotation agreement and ex-
plicitly models controversial cases.
For example, a text labeled as HATE by 66% of annotators is treated differently
from one labeled unanimously, allowing the model to learn graded risk signals instead
of hard thresholds.
This approach avoids premature discretization decisions (e.g.,
50%, 3/5, or 4/6 majority rules) and defers the choice of decision boundaries to
downstream applications.
3.3.2. Training Splits and Evaluation Strategy
We employed two training configurations to balance comprehensive evaluation with
maximal production performance:
Configuration 1: 2:1 Split (2,295 train / 4,590 test). To enable statis-
tically robust evaluation with a large test set, we initially trained models on a 2:1
split of the dataset. This configuration prioritizes having sufficient test samples for
2026/02/12; 01:58
str.
5/19

--- Page 6 ---

comprehensive analysis. Results on the Sojka test set and Sojka augmented test set
(Tables 1 and 3) use models trained with this split.
Configuration 2: Near-Complete Training (6,285 train / 600 test). To
maximize production performance, we trained models on the near-complete dataset,
using almost all available data for training. Results on the Gadzi Jezyk benchmark
(Table 4) and comparison with state-of-the-art models on user prompts (Table 5) use
models trained with this configuration, as they represent our best-performing models
for deployment.
The relatively small training set size in Configuration 1 is offset by the strong
linguistic representations already learned by the base models (MMLW-RoBERTa-base
and PKOBP/polish-roberta-8k). Multi-label classification is fully supported, allowing
texts to belong to multiple categories simultaneously.
3.3.3. Data Distribution
We consider a text to belong to a category if at least 60% of annotators classified it as
such. While model training uses continuous percentage values (0-100%) as soft labels,
evaluation metrics requiring binary ground truth (F1, precision, recall, specificity) use
this 60% threshold for binarization. Model predictions are binarized at the standard
0.5 threshold. Using this 60% agreement threshold, the dataset shows natural class
imbalance:
• Safe content: 3,781 texts (54.92%)
• SELF-HARM: 796 texts (11.56%)
• HATE: 988 texts (14.35%)
• SEX: 895 texts (13.00%)
• VULGAR: 411 texts (5.97%)
• CRIME: 311 texts (4.52%)
3.3.4. Quality Control
Quality assurance included deduplication, clustering analysis to verify annotation
consistency, and expert validation for controversial cases. The methodology explicitly
embraces bounded rationality, targeting satisficing rather than optimal solutions and
treating safety as a matter of social consensus rather than objective truth.
We deliberately do not report traditional inter-annotator agreement metrics as
these assume the existence of a single "correct" label. Instead, our soft-label approach
treats disagreement as informative signal about the inherent ambiguity and context-
dependence of safety judgments. The variance in annotation percentages naturally
captures the degree of consensus: texts with near-unanimous ratings (close to 0% or
100%) represent clear cases, while those with intermediate percentages (e.g., 40-60%)
reflect genuine ambiguity that the model learns to recognize.
3.4. Training Procedure
Models were fine-tuned using standard practices for transformer-based classification:
2026/02/12; 01:58
str.
6/19

--- Page 7 ---

• Loss function:
Binary Cross-Entropy (BCE) with soft labels derived from
percentage-based annotations.
We experimented with Mean Squared Error
(MSE) loss but found BCE to yield superior performance. No class weighting
was applied.
• Optimizer: AdamW with weight decay of 0.01
• Learning rate: 2e-5 with 500 warmup steps followed by linear decay
• Batch size: 32
• Training duration: 3 epochs (approx. 2 hours on A100)
• Training infrastructure: A100 GPU cluster (ACK Cyfronet AGH)
The use of soft labels (annotation percentages) rather than hard binary labels
allows the model to learn the degree of consensus among annotators, preserving in-
formation about controversial or ambiguous cases. For evaluation, ground truth la-
bels are binarized at 60% annotator agreement (reflecting majority consensus), while
model predictions are binarized at the standard 0.5 sigmoid threshold. Users can
adjust this prediction threshold based on their specific precision-recall requirements.
Both models were trained using the same training procedure and augmentation
strategy. For the initial 2:1 split training, the test set was augmented using 15 text
augmentation techniques (including diacritic manipulation, capitalization changes,
character swaps, and spacing modifications) to evaluate model robustness.
3.5. Model Versions
Two versions of each model variant were developed:
v1.0: Initial models exhibiting overreaction to crime-related content due to a
classification threshold calibration issue.
v1.1: Improved models with the crime category threshold issue resolved, result-
ing in substantially improved precision (77.65% vs. 67.27% for the 0.1B variant on
user prompts, Table 5) and lower false positive rates (0.63% vs. 1.20%). Both v1.0
and v1.1 models were trained using identical procedures and data splits; the difference
lies solely in the threshold calibration fix.
For each training configuration (2:1 split and near-complete), we trained both
v1.0 and v1.1 versions. To distinguish between configurations, we use the following
versioning scheme:
• v1.0a / v1.1a: Models trained with Configuration 1 (2:1 split: 2,295 train /
4,590 test)
• v1.0 / v1.1: Models trained with Configuration 2 (near-complete: 6,285 train
/ 600 test)
All subsequent analyses prioritize v1.1 models as they represent the production-
ready variants with optimal precision-recall trade-offs.
2026/02/12; 01:58
str.
7/19

--- Page 8 ---

4. Evaluation
We evaluate Bielik Guard on three datasets using metrics appropriate for multi-label
classification: RMSE, F1 (micro and macro), Specificity, and ROC AUC. Addition-
ally, we compare against state-of-the-art alternatives on user prompt data to assess
practical deployment performance.
4.1. Sojka Test Set
The primary evaluation uses the held-out Sojka test set (4,590 samples) from the 2:1
split training configuration (Configuration 1), with the same label distribution as the
full dataset. Results are shown in Table 1.
Table 1
Performance on Sojka test set. Ground truth binarized at 60% annotator agreement; pre-
dictions binarized at 0.5 threshold.
Metric
0.1B v1.0a
0.5B v1.0a
0.1B v1.1a
0.5B v1.1a
RMSE
0.137
0.130
0.128
0.122
F1 micro
0.756
0.781
0.775
0.791
F1 macro
0.747
0.774
0.770
0.785
Recall micro
0.813
0.851
0.808
0.835
Recall macro
0.799
0.829
0.794
0.812
Specificity micro
0.961
0.962
0.968
0.968
Specificity macro
0.960
0.961
0.967
0.967
ROC AUC micro
0.974
0.979
0.974
0.980
ROC AUC macro
0.964
0.973
0.964
0.973
The 0.5B v1.1a model demonstrates the best overall performance with F1 micro of
0.791 and F1 macro of 0.785, indicating superior discrimination capability. Both v1.1a
models maintain high specificity (>0.96), demonstrating strong ability to correctly
identify safe content.
4.1.1. Per-Category Analysis
Table 2 presents detailed per-category performance metrics for both model variants,
revealing category-specific strengths and challenges.
The HATE category presents the greatest challenge for both models (F1 of 0.628
and 0.667), likely due to the inherent subjectivity and context-dependence of hate
speech annotation. CRIME also proves challenging (F1 of 0.707 and 0.716), which
may reflect its lower prevalence in the training data (4.52% of samples). The SELF-
HARM and SEX categories achieve the strongest performance, with F1 scores exceed-
ing 0.87 for both model variants. All categories maintain ROC AUC scores above 0.91,
indicating consistent discriminative ability across the taxonomy.
2026/02/12; 01:58
str.
8/19

--- Page 9 ---

Table 2
Per-category performance breakdown on Sojka test set (v1.1a models)
Category
0.1B v1.1a
0.5B v1.1a
F1
ROC AUC
F1
ROC AUC
SELF-HARM
0.886
0.991
0.879
0.992
HATE
0.628
0.919
0.667
0.934
VULGAR
0.742
0.973
0.750
0.977
SEX
0.889
0.988
0.915
0.993
CRIME
0.707
0.949
0.716
0.971
4.2. Robustness to Text Perturbations
To evaluate robustness against adversarial modifications and natural text variations,
we tested on the Sojka Augmented dataset, which applies 15 augmentation tech-
niques including diacritic manipulation, capitalization changes, character-level per-
turbations, and spacing modifications.
Results are in Table 3.
These results use
models trained with Configuration 1 (2:1 split).
Table 3
Performance on Sojka augmented test set
Metric
0.1B v1.0a
0.5B v1.0a
0.1B v1.1a
0.5B v1.1a
RMSE
0.183
0.167
0.181
0.163
F1 micro
0.632
0.683
0.638
0.694
F1 macro
0.615
0.660
0.619
0.679
Recall micro
0.606
0.675
0.621
0.686
Recall macro
0.585
0.642
0.602
0.650
Specificity micro
0.964
0.965
0.962
0.966
Specificity macro
0.963
0.964
0.961
0.965
ROC AUC micro
0.908
0.936
0.909
0.934
ROC AUC macro
0.880
0.913
0.884
0.915
While performance degrades on perturbed text as expected, the 0.5B v1.1a model
shows substantially better robustness, with F1 micro of 0.694 compared to 0.638 for
the 0.1B v1.1a model. This validates the effectiveness of combining a more capa-
ble base model (443M vs. 124M parameters, larger vocabulary) with augmentation-
enhanced training.
4.3. Gadzi Jezyk Benchmark
We evaluated on the Gadzi Jezyk dataset [16], a challenging benchmark containing 520
toxic prompts with extreme class imbalance: 505 crime-related examples (97.1%), 43
hate/violence (8.3%), 31 self-harm (6.0%), 18 sexual content (3.5%), and 4 vulgarities
2026/02/12; 01:58
str.
9/19

--- Page 10 ---

(0.8%). This distribution makes it particularly suitable for evaluating crime category
performance. The Bielik Guard models (Sójka) evaluated here were trained using
Configuration 2 (near-complete data: 6,285 train / 600 test), representing our best-
performing models for deployment. Table 4 shows results.
Table 4
Performance on Gadzi Jezyk dataset (97.1% crime-related content)
Metric
0.1B v1.0
0.5B v1.0
0.1B v1.1
0.5B v1.1
RMSE
0.236
0.217
0.286
0.241
Precision
0.977
0.974
0.985
0.973
Recall
0.702
0.762
0.557
0.714
F1
0.817
0.855
0.712
0.823
Specificity
0.995
0.994
0.998
0.994
ROC AUC
0.974
0.980
0.959
0.967
The Gadzi Jezyk dataset presents a particularly revealing evaluation scenario:
with 97.1% crime-related content, it directly tests the impact of our v1.0 to v1.1
threshold calibration fix. The results clearly demonstrate the precision-recall trade-
off inherent in the calibration.
The v1.1 models achieve slightly higher precision
(98.5% vs.
97.7% for 0.1B, maintaining 97.3% for 0.5B) and improved specificity
(99.8% vs. 99.5% for 0.1B), while recall decreases substantially (55.7% vs. 70.2% for
0.1B, 71.4% vs. 76.2% for 0.5B).
Notably, the 0.5B v1.1 model maintains strong overall performance with F1 of
0.823 (vs. 0.855 for v1.0), representing only a 4% reduction despite the significant
recall decrease. This demonstrates effective precision-recall balancing. The 0.1B v1.1
shows a larger F1 reduction (0.712 vs. 0.817), reflecting its more conservative thresh-
old calibration. The maintained high ROC AUC scores (95.9-98.0%) across all variants
demonstrate that underlying model discrimination capability remains excellent; the
threshold adjustment shifts the operating point toward higher precision rather than
degrading model quality.
This trade-off yields substantial benefits in production deployment. While v1.1
shows 4-15 percentage point recall reductions on this crime-saturated benchmark (the
category where threshold calibration was specifically applied), it achieves 0.63%-0.73%
FPR on diverse real user prompts (Table 5), representing a 6-7× improvement over
models with aggressive thresholds like HerBERT-PL-Guard (4.70% FPR). The preci-
sion improvements on Gadzi Jezyk, though modest (0.8-1.1 percentage points), trans-
late to dramatically lower false positive rates on real-world content where class dis-
tribution is balanced rather than 97% toxic. For sustainable production deployment,
this trade-off prioritizes user trust through high precision over maximum recall on
synthetic adversarial benchmarks.
2026/02/12; 01:58
str.
10/19

--- Page 11 ---

4.4. Comparison with State-of-the-Art Models
To assess practical deployment performance, we evaluated Bielik Guard against
HerBERT-PL-Guard [6], Llama Guard 3 (1B and 8B variants) [8], and Qwen3Guard-
Gen-0.6B [20] on 3,000 random user prompts collected from Polish LLM interactions.
This evaluation dataset is distinct from the training dataset described in Section 3.3.1
in two important ways: (1) it consists of randomly sampled user prompts without any
prefiltering, whereas the Sojka training dataset was prefiltered to contain dangerous
categories, and (2) it was gathered specifically for comparative evaluation purposes
and was not used during model training. Results for Bielik Guard are from models
trained with Configuration 2 (near-complete data: 6,285 train / 600 test).
Evaluation Methodology:
All models were evaluated using their default
thresholds and taxonomies. Critically, for practical deployment assessment, we eval-
uated each model on a binary safe/unsafe basis: any text flagged as unsafe in any
category by a model was considered an "unsafe" prediction, regardless of the number
or type of categories triggered. This binary evaluation approach ensures fair compar-
ison across different taxonomies (Bielik Guard: 5 categories, HerBERT-PL-Guard:
15 categories, Llama Guard 3: 14 categories, Qwen3Guard-Gen: 9 categories), as
the number of categories does not influence the fundamental question of whether
content should be moderated. This metric directly reflects production deployment
performance where the primary decision is whether to intervene, regardless of specific
categorization.
The annotation protocol involved a two-annotator plus super-annotator scheme:
each text flagged as unsafe by any classifier was independently annotated by two an-
notators, with a third super-annotator resolving disagreements. Crucially, annotation
was performed separately for each model’s taxonomy: annotators judged whether a
text was unsafe according to the specific safety categories defined by Bielik Guard,
Llama Guard, Qwen3Guard, and HerBERT-PL-Guard respectively. This ensures that
each model’s precision is measured against ground truth that faithfully reflects what
that model’s taxonomy is designed to detect. Due to resource constraints, we an-
notated only texts flagged by at least one classifier rather than the entire dataset,
which precludes calculating recall metrics (as we lack ground truth for texts classified
as safe by all models). This methodology focuses evaluation on precision and false
positive rate, which are critical metrics for production deployment where excessive
false positives harm user experience.
Results are presented in Table 5 and visualized in Figure 1.
Bielik Guard 0.1B v1.1 achieves 77.65% precision, meaning that over three-
quarters of all flagged content is genuinely harmful, compared to HerBERT-PL-
Guard (31.55%) despite identical model size (124M parameters), Llama Guard 3 8B
(13.62%), and Qwen3Guard-Gen-0.6B (11.36%). The 0.63% false positive rate is 7.5×
lower than HerBERT-PL-Guard’s 4.70% and substantially lower than the generative
multilingual models (16.50% for Llama Guard 3 1B, 17.17% for Qwen3Guard-Gen-
0.6B), making Bielik Guard significantly less intrusive for legitimate use cases. The
2026/02/12; 01:58
str.
11/19

--- Page 12 ---

Precision
False Positive Rate (FPR)
0
20
40
60
80
77.65%
0.63%
31.55%
4.7%
7.82%
16.5%
13.62%
9.3%
11.36%
17.17%
Percentage (%)
Bielik Guard 0.1B v1.1
HerBERT-PL-Guard
Llama Guard 3 1B
Llama Guard 3 8B
Qwen3Guard-Gen-0.6B
Figure 1. Comparison of safety classifiers on Polish user prompts. Higher Precision is better,
lower FPR is better.
Bielik Guard 0.1B v1.1 (124M) outperforms all compared models
including larger multilingual alternatives.
Table 5
Comparison on 3,000 Polish user prompts (default thresholds). Each model evaluated with
its own taxonomy. Recall not reported as only classifier-flagged texts were annotated.
Model
Params
Precision
Alert Rate
FPR
Bielik Guard 0.1B v1.1
124M
77.65%
2.83%
0.63%
Bielik Guard 0.5B v1.1
443M
75.28%
2.97%
0.73%
Bielik Guard 0.1B v1.0
124M
67.27%
3.67%
1.20%
HerBERT-PL-Guard
124M
31.55%
6.87%
4.70%
Llama Guard 3 1B
1B
7.82%
17.90%
16.50%
Llama Guard 3 8B
8B
13.62%
10.77%
9.30%
Qwen3Guard-Gen-0.6B
600M
11.36%
19.37%
17.17%
0.5B v1.1 variant achieves similarly strong performance with 75.28% precision and
0.73% FPR.
The low alert rate for Bielik Guard 0.1B v1.1 (2.83% vs. 6.87% for HerBERT-
PL-Guard, 17.90% for Llama Guard 3 1B, and 19.37% for Qwen3Guard-Gen-0.6B)
indicates that Bielik Guard flags content conservatively, reducing user friction while
maintaining high precision.
Limitations of Cross-Taxonomy Comparison.
Comparing safety classi-
fiers that operate under different taxonomies is a recognized challenge in the field.
As noted in the Llama Guard paper [4]: “The absence of standardized taxonomies
2026/02/12; 01:58
str.
12/19

--- Page 13 ---

makes comparing different models challenging, as they were trained against different
taxonomies.” Similarly, ShieldGemma [17] observes that “direct comparison remains
challenging due to variations in policy definitions and supported harm types across
datasets [and] inconsistencies in policy definitions even within the same harm type.”
Different approaches to this problem have emerged in the literature.
Llama
Guard [4] adapts its model to each benchmark’s taxonomy via zero-shot prompting—
an option available to generative LLMs that accept taxonomy definitions as input,
but not to encoder-based classifiers with fixed output heads. ShieldGemma [17] uses
a mixed strategy: on some benchmarks it predicts according to the benchmark’s
categories (e.g., OpenAI Moderation), while on others it maximizes over its own harm
types (e.g., ToxicChat). Granite Guardian [13] assigns a positive (harmful) ground-
truth label to any instance marked as unsafe under the benchmark’s own taxonomy
and evaluates all models—each using its own taxonomy—against this shared binary
label. Qwen3Guard [20] follows a similar protocol, comparing models with different
taxonomies on standard benchmarks using binary or per-benchmark F1 scores.
Our evaluation methodology follows this latter established practice: each model
is run with its own default taxonomy, and the comparison is made at the binary
safe/unsafe level. Importantly, we go further than simply reusing pre-existing bench-
mark labels: each text flagged as unsafe by any model was independently annotated
by human raters under each model’s taxonomy-specific definition of unsafe content,
ensuring that the ground truth for each model faithfully reflects what that model is
designed to detect.
While different taxonomies define the boundary between safe and unsafe content
differently, which may affect cross-model comparability to some extent, this concern
should not be overstated. Since each model is evaluated against its own taxonomy-
specific ground truth, the precision and false positive rate for each model are meaning-
ful absolute indicators of that model’s calibration on Polish text. When Llama Guard
3 1B achieves 7.82% precision, this means that over 92% of texts it flags are safe by its
own definition—a result that reflects genuine miscalibration on Polish content rather
than a taxonomy artifact. Similarly, false positive rates of 16–17% for multilingual
models indicate that they flag roughly one in six Polish prompts incorrectly under
their own safety policies, which would be disruptive in any production deployment.
Because only texts flagged by at least one classifier were annotated, we cannot
report recall. However, Bielik Guard’s strong performance on fully-annotated bench-
marks (Tables 1, 4) provides indirect evidence of reasonable detection coverage, while
direct recall comparison across models remains an open question for future work.
In summary, the comparison reflects a practical deployment scenario: when se-
lecting a safety classifier for a Polish-language application, these results show what
to expect from each model in terms of false positive rates and flagging behavior on
real user traffic. Bielik Guard’s high precision and low false positive rate translate
directly to reduced user friction, while practitioners should also consider each model’s
taxonomy scope when assessing coverage of potential threats.
2026/02/12; 01:58
str.
13/19

--- Page 14 ---

4.5. Discussion
Our evaluation reveals several key findings:
Model Size vs.
Performance: The 0.5B v1.1 variant (443M parameters)
consistently outperforms the 0.1B v1.1 model (124M parameters), with improvements
of 1-7 percentage points across metrics. These gains result from the more capable base
model (PKOBP/polish-roberta-8k with 128K vocabulary vs. MMLW-RoBERTa-base
with 50K vocabulary, providing 3.6× more parameters and 2.6× larger vocabulary).
The improvements are most pronounced on augmented data (F1 micro: 0.694 vs.
0.638), demonstrating the value of increased model capacity for handling perturbed
text.
Precision-Recall Trade-offs: Bielik Guard’s design philosophy prioritizes pre-
cision over recall, reflected in the low false positive rate. This choice is motivated by
deployment considerations: excessive false positives erode user trust and may cause
users to disable safety features entirely.
Language-Specific Advantages: The performance gap between Bielik Guard
0.1B v1.1 (77.65% precision) and both Polish-specific (HerBERT-PL-Guard: 31.55%)
and multilingual alternatives (Llama Guard 3 8B: 13.62%, Qwen3Guard-Gen-0.6B:
11.36%) supports the value of using authentic Polish data with a focused taxonomy,
though part of this gap is attributable to differences in how each taxonomy defines
unsafe content (see Section 4.4). Cross-taxonomy comparison is an inherent limitation
shared across the safety classifier literature [4, 17, 13, 20], and disentangling the
contribution of data quality from the effect of differing taxonomy definitions remains
an open question—for instance, through evaluation on a shared, fixed taxonomy or
annotation of the full dataset to enable recall-based comparison.
Efficiency: At 124M (0.1B) and 443M (0.5B) parameters, Bielik Guard v1.1
models achieve high precision at compact sizes.
The 0.1B v1.1 model matches
HerBERT-PL-Guard in size (124M parameters) while achieving 2.5× better preci-
sion, demonstrating that our data quality and focused taxonomy deliver superior
performance without requiring larger models.
5. Deployment and Practical Considerations
Bielik Guard has been deployed in production at https://guard.bielik.ai/,
where users can test the model interactively and provide feedback through thumbs-
up/thumbs-down ratings. This continuous feedback loop informs ongoing improve-
ments to the dataset and model.
5.1. Response-Oriented Design
A distinguishing feature of Bielik Guard is its response-oriented philosophy, partic-
ularly for the SELF-HARM category. Rather than simply blocking or flagging con-
cerning content, the system is designed to integrate with intervention frameworks that
2026/02/12; 01:58
str.
14/19

--- Page 15 ---

provide appropriate support resources, such as crisis helpline information (e.g., “Tele-
fon Zaufania” in Poland). This approach recognizes that users expressing self-harm
ideation need support, not silence.
5.2. Integration and API
The models are available through the HuggingFace Transformers library with standard
text classification pipelines:
from transformers import pipeline
classifier = pipeline(
"text-classification",
model="speakleash/Bielik-Guard-0.1B-v1.1",
return_all_scores=True
)
results = classifier(text)
This simple interface returns probability scores for all five categories, enabling
application-specific thresholding and response strategies.
5.3. Limitations and Future Work
Current limitations include:
• Language Coverage: Models are optimized for Polish only; performance on
other Slavic languages is untested
• Taxonomy Scope: Deliberate exclusion of disinformation, jailbreaking, and
copyright violations
• Domain Shift: Performance may degrade on specialized domains (medical,
legal) not well-represented in training data
• Adversarial Robustness: While character-level augmentation improves ro-
bustness to natural text variations, we have not evaluated against sophisticated
adversarial attacks or prompt injection techniques. Our taxonomy deliberately
excludes jailbreaking and prompt disclosure attacks, focusing instead on content
safety
• Cross-Model Comparison Methodology: The comparison with state-of-the-
art models (Table 5) follows established practice in the field [4, 17, 13, 20] but is
inherently limited by the absence of recall metrics and by the fact that each model
defines safe/unsafe content differently. Observed precision differences reflect both
model quality and differences in the underlying classification tasks.
A fixed-
taxonomy evaluation or full-dataset annotation would be needed to isolate these
effects
Future development directions include:
• Expansion to additional safety categories based on community needs
• Multilingual variants supporting other Slavic languages
• Exploration of larger model variants (1B+) for specialized high-stakes applica-
tions where the precision-efficiency trade-off favors accuracy over compactness
2026/02/12; 01:58
str.
15/19

--- Page 16 ---

• Integration with generative models for explanation generation
• Continuous learning from production feedback
• Ablation studies on the effect of soft vs. hard labels and various augmentation
strategies
• Further development of crowdsourcing-based approach for data collection
6. Conclusion
We have presented Bielik Guard, a family of efficient Polish language safety classifiers
that achieve state-of-the-art performance on Polish content while maintaining com-
pact model sizes. Through community-driven annotation of 6,885 Polish texts and
careful fine-tuning of RoBERTa-based encoders, we developed models that outperform
substantially larger multilingual alternatives on Polish content.
Our evaluation demonstrates that Bielik Guard 0.1B v1.1 achieves 77.65% pre-
cision with only 0.63% false positive rate on real user prompts.
In comparison
with state-of-the-art alternatives—each evaluated against its own taxonomy-specific
ground truth following established cross-taxonomy evaluation practices [4, 13, 20]—
Bielik Guard shows substantially higher precision than both HerBERT-PL-Guard
(31.55%) at identical model size and multilingual models such as Llama Guard 3 8B
(13.62%) and Qwen3Guard-Gen-0.6B (11.36%), whose low precision on Polish text
reflects genuine miscalibration rather than taxonomy differences alone. These results
highlight the importance of authentic Polish language data and community-driven an-
notation over translated datasets, and suggest that data quality and taxonomy design
can matter more than model scale for language-specific deployment.
The models are publicly available and actively deployed, with ongoing commu-
nity engagement driving continuous improvement. We believe Bielik Guard repre-
sents a significant step toward making LLM safety tools accessible for lower-resource
languages and hope it serves as a model for similar initiatives in other linguistic
communities.
Acknowledgements
The research presented in this paper was made possible by the Bielik.AI community and
SpeakLeash Foundation. We thank over 1,500 volunteers who contributed annotations.
We gratefully acknowledge Polish high-performance computing infrastructure PLGrid
(HPC Center: ACK Cyfronet AGH) for providing computer facilities and support
within computational grant no. PLG/2025/018338.
References
[1] Ayyamperumal S.G., Ge L.: Current state of LLM Risks and AI Guardrails, 2024.
URL https://arxiv.org/abs/2406.12934.
2026/02/12; 01:58
str.
16/19

--- Page 17 ---

[2] Dadas S.:
MMLW: Massively Multilingual Language Workbench.
Hug-
gingFace
Model
Hub,
2020.
URL
https://huggingface.co/sdadas/
mmlw-roberta-base.
[3] Dong Y., Mu R., Zhang Y., Sun S., Zhang T., Wu C., Jin G., Qi Y., Hu J., Meng
J., Bensalem S., Huang X.: Safeguarding Large Language Models: A Survey,
2024. URL https://arxiv.org/abs/2406.02622.
[4] Inan H., Upasani K., Chi J., Rungta R., Iyer K., Mao Y., Tontchev M., Hu Q.,
Fuller B., Testuggine D., Khabsa M.: Llama Guard: LLM-based Input-Output
Safeguard for Human-AI Conversations, 2023. URL https://arxiv.org/abs/
2312.06674.
[5] Kocoń J., Piasecki M., Janz A., Ferdinan T., Łukasz Radliński, Koptyra B.,
Oleksy M., Woźniak S., Walkowiak P., Wojtasik K., Moska J., Naskręt T.,
Walkowiak B., Gniewkowski M., Szyc K., Motyka D., Banach D., Dalasiński
J., Rudnicka E., Alberski B., Walkowiak T., Szczęsny A., Markiewicz M., Bernaś
T., Mazur H., Żyta K., Tykierko M., Chodak G., Kajdanowicz T., Kazienko P.,
Karlińska A., Seweryn K., Kołos A., Chrabąszcz M., Lorenc K., Krasnodębska
A., Wilczek A., Dziewulska K., Betscher P., Cieślińska Z., Kowol K., Mikoś D.,
Trzciński M., Krutul D., Kozłowski M., Dadas S., Poświata R., Perełkiewicz M.,
Grębowiec M., Kazuła M., Białas M., Roszko R., Roszko D., Vaičenonien˙e J.,
Utka A., Levchuk P., Kowalski P., Prawdzic-Jankowska I., Ogrodniczuk M., Bo-
rys M., Bulińska A., Gumienna W., Kieraś W., Komosińska D., Krasnowska-
Kieraś K., Łukasz Kobyliński, Lewandowska M., Łaziński M., Łątkowski M.,
Mastalerz D., Milewicz B., Mykowiecka A.A., Peljak-Łapińska A., Penno S.,
Przybysz Z., Rudolf M., Rybak P., Saputa K., Tomaszewska A., Wawer A.,
Woliński M., Wołoszyn J., Wróblewska A., Żuk B., Żarnecki F., Kaczyński K.,
Cichosz A., Deckert Z., Garnys M., Grabarczyk I., Janowski W., Karasińska
S., Kujawiak A., Misztela P., Szymańska M., Walkusz K., Siek I., Kwiatkowski
J., Pęzik P.: PLLuM: A Family of Polish Large Language Models, 2025. URL
https://arxiv.org/abs/2511.03823.
[6] Krasnodębska A., Seweryn K., Łukasik S., Kusa W.: PL-Guard: Benchmarking
Language Model Safety for Polish.
In: Proceedings of the 10th Workshop on
Slavic Natural Language Processing. Association for Computational Linguistics,
Vienna, Austria, 2025.
[7] Liu Y., Ott M., Goyal N., Du J., Joshi M., Chen D., Levy O., Lewis M., Zettle-
moyer L., Stoyanov V.: RoBERTa: A Robustly Optimized BERT Pretraining
Approach. In: arXiv preprint arXiv:1907.11692, 2019.
[8] Llama Team A..M.: The Llama 3 Herd of Models, 2024. URL https://arxiv.
org/abs/2407.21783.
[9] Ociepa K., Łukasz Flis, Kinas R., Wróbel K., Gwoździej A.: Bielik 11B v3:
Multilingual Large Language Model for European Languages, 2025. URL https:
//arxiv.org/abs/2601.11579.
[10] Ociepa K., Flis Ł., Kinas R., Wróbel K., Gwoździej A.: Bielik v3 Small: Technical
2026/02/12; 01:58
str.
17/19

--- Page 18 ---

Report. URL https://arxiv.org/abs/2505.02550.
[11] Ociepa K., Flis Ł., Wróbel K., Gwoździej A., Kinas R.: Bielik 11B v2 Technical
Report, 2025. URL https://arxiv.org/abs/2505.02410.
[12] Ociepa K., Flis Ł., Wróbel K., Gwoździej A., Kinas R.: BIELIK 7B V0.1: POL-
ISH LANGUAGE MODEL - DEVELOPMENT, INSIGHTS, AND EVALUA-
TION. In: Computer Science, vol. 26(4), 2025. URL http://dx.doi.org/10.
7494/csci.2025.26.4.7689.
[13] Padhi I., Nagireddy M., Cornacchia G., Chaudhury S., Pedapati T., Dognin P.,
Murugesan K., Miehling E., Cooper M.S., Fraser K., Zizzo G., Hameed M.Z.,
Purcell M., Desmond M., Pan Q., Ashktorab Z., Vejsbjerg I., Daly E.M., Hind
M., Geyer W., Rawat A., Varshney K.R., Sattigeri P.: Granite Guardian, 2024.
URL https://arxiv.org/abs/2412.07724.
[14] Polski P.B.: Polish RoBERTa 8K. HuggingFace Model Hub, 2023. URL https:
//huggingface.co/PKOBP/polish-roberta-8k.
[15] Simon H.A.: Models of Bounded Rationality. MIT Press, Cambridge, MA, USA,
1982.
[16] Surma J.: Dataset Gadzi Jezyk. HuggingFace Dataset, 2024. URL https://
huggingface.co/datasets/JerzyPL/GadziJezyk.
[17] Zeng W., Liu Y., Mullins R., Peran L., Fernandez J., Harkous H., Narasimhan K.,
Proud D., Kumar P., Radharapu B., Sturman O., Wahltinez O.: ShieldGemma:
Generative AI Content Moderation Based on Gemma, 2024.
URL https://
arxiv.org/abs/2407.21772.
[18] Zhang M.L., Zhou Z.H.: A Review on Multi-Label Learning Algorithms.
In:
IEEE Transactions on Knowledge and Data Engineering, vol. 26(8), pp. 1819–
1837, 2014. URL http://dx.doi.org/10.1109/TKDE.2013.39.
[19] Zhang R., Li H.W., Qian X.Y., Jiang W.B., Chen H.X.: On large language
models safety, security, and privacy: A survey. In: Journal of Electronic Science
and Technology, vol. 23(1), p. 100301, 2025. ISSN 1674-862X. URL http://dx.
doi.org/https://doi.org/10.1016/j.jnlest.2025.100301.
[20] Zhao H., Yuan C., Huang F., Hu X., Zhang Y., Yang A., Yu B., Liu D., Zhou J.,
Lin J., Yang B., Cheng C., Tang J., Jiang J., Zhang J., Xu J., Yan M., Sun M.,
Zhang P., Xie P., Tang Q., Zhu Q., Zhang R., Wu S., Zhang S., He T., Tang T.,
Xia T., Liao W., Shen W., Yin W., Zhou W., Yu W., Wang X., Deng X., Xu X.,
Zhang X., Liu Y., Li Y., Zhang Y., Jiang Y., Wan Y., Zhou Y.: Qwen3Guard
Technical Report, 2025. URL https://arxiv.org/abs/2510.14276.
Affiliations
Krzysztof Wróbel
SpeakLeash Foundation, Warsaw, Poland, krzysztof.wrobel@bielik.ai
Jagiellonian University, Cracow, Poland, krzysztof.pawel.wrobel@uj.edu.pl
Jan Maria Kowalski
SpeakLeash Foundation, Warsaw, Poland, jan.maria.kowalski@bielik.ai
2026/02/12; 01:58
str.
18/19

--- Page 19 ---

Jerzy Surma
Warsaw School of Economics, Warsaw, Poland, jerzy.surma@sgh.waw.pl
Igor Ciuciura
SpeakLeash Foundation, Warsaw, Poland, igor.ciuciura@bielik.ai
Maciej Szymański
SpeakLeash Foundation, Warsaw, Poland, maciej.szymanski@bielik.ai
Received: ???
Revised: ???
Accepted: ???
2026/02/12; 01:58
str.
19/19

```
