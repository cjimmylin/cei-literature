---
title: "2026-Vargas-Self-Explaining Hate Speech Detection with Moral Rationales - PDF Extract"
source_pdf: "2026-Vargas-Self-Explaining Hate Speech Detection with Moral Rationales.pdf"
pages: 19
extracted_at: "2026-02-15T17:54:30.016948"
---

# PDF Extract: 2026-Vargas-Self-Explaining Hate Speech Detection with Moral Rationales

**Source PDF:** 2026-Vargas-Self-Explaining Hate Speech Detection with Moral Rationales.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

Self-Explaining Hate Speech Detection with Moral Rationales
Francielle Vargas*
University of São Paulo
Jackson Trager
University of Southern California
Diego Alves
Saarland University
Surendrabikram Thapa
Virginia Tech
Matteo Guida
University of Melbourne
Berk Atil
Pennsylvania State University
Daryna Dementieva
Technical University of Munich
Andrew Smart
Google Research
Ameeta Agrawal
Portland State University
Abstract
Hate speech detection models rely on surface-
level lexical features, increasing vulnerabil-
ity to spurious correlations and limiting ro-
bustness, cultural contextualization, and in-
terpretability. We propose Supervised Moral
Rationale Attention (SMRA)1, the first self-
explaining hate speech detection framework to
incorporate moral rationales as direct supervi-
sion for attention alignment. Based on Moral
Foundations Theory, SMRA aligns token-level
attention with expert-annotated moral ratio-
nales, guiding models to attend to morally
salient spans rather than spurious lexical pat-
terns. Unlike prior rationale-supervised or post-
hoc approaches, SMRA integrates moral ra-
tionale supervision directly into the training
objective, producing inherently interpretable
and contextualized explanations. To support
our framework, we also introduce HateBR-
MoralXplain, a Brazilian Portuguese bench-
mark dataset annotated with hate labels, moral
categories, token-level moral rationales, and
socio-political metadata. Across binary hate
speech detection and multi-label moral sen-
timent classification, SMRA consistently im-
proves performance (e.g., +0.9 and +1.5 F1,
respectively) while substantially enhancing ex-
planation faithfulness, increasing IoU F1 (+7.4
pp) and Token F1 (+5.0 pp). Although expla-
nations become more concise, sufficiency im-
proves (+2.3 pp) and fairness remains stable,
indicating more faithful rationales without per-
formance or bias trade-offs 2.
1
Introduction
Despite significant advances in automatic Hate
Speech (HS) detection, current approaches remain
fundamentally limited. Existing models often en-
code biases originating from training data (David-
*Corresponding author: francielleavargas@usp.br
1Dataset, annotator disagreements, and code are available
at https://github.com/franciellevargas/SMRA
2Warning: This document contains offensive content.
Figure 1:
Supervised Moral Rationale Attention
(SMRA) for Self-Explaining Hate Speech Detection.
son et al., 2019; Wiegand et al., 2019), stereotypi-
cal associations learned by hate speech classifiers
(Davani et al., 2023; Vargas et al., 2023), and an-
notation processes (Sap et al., 2019), which are
frequently shaped by annotators’ subjective judg-
ments and sociocultural backgrounds (Davani et al.,
2024a; Tonneau et al., 2024; Abercrombie et al.,
2023; Sap et al., 2022; Vargas et al., 2022b; Poletto
et al., 2021). Such biases can lead to systematic dis-
parities in model behavior, resulting in the unfair
treatment or over-targeting of marginalized groups
and producing negative social consequences when
deployed at scale (Blodgett et al., 2020; Wiegand
et al., 2019; Sap et al., 2019; Davidson et al., 2019).
Given that these models may inherit biases from
their training data, explainable hate speech detec-
tion models (Salles et al., 2025a; Eilertsen et al.,
2025; Mathew et al., 2021) are crucial for ensur-
ing transparency, diagnosing biases, and enabling
robust, socially responsible detection across lan-
guages and cultural contexts. Existing explainable
HS detection approaches can be broadly catego-
rized into two interpretability paradigms: post-hoc
and self-explaining models. Post-hoc approaches
arXiv:2601.03481v1  [cs.CL]  7 Jan 2026

--- Page 2 ---

generate explanations after the prediction, relying
on external attribution or surrogate techniques to
approximate the model’s reasoning (Trager et al.,
2025b; Salles et al., 2025a; Cercas Curry et al.,
2023; Mathew et al., 2021; Kennedy et al., 2020).
Moreover, many post-hoc explainability methods
are unfaithful and computationally expensive. In
contrast, self-explaining models integrate expla-
nation generation directly into the learning pro-
cess, typically through explicit supervision mech-
anisms that align model attention with human-
interpretable rationales, making explanations an
intrinsic part of the prediction pipeline (Eilertsen
et al., 2025; Kim et al., 2022; Mathew et al., 2021).
Furthermore, most existing hate speech detec-
tion approaches continue to rely primarily on
surface-level lexical features, which are insuffi-
cient due to elevated false positive rates (Poletto
et al., 2021; Davidson et al., 2019) and their lim-
ited ability to account for cultural and contextual
factors (Lee et al., 2023; Zhou et al., 2023; Kim
et al., 2024; Vargas et al., 2024; Wong, 2024). Even
when contextual information is available (Vargas
et al., 2021; Kennedy et al., 2020), judgments of of-
fensiveness remain deeply culture-dependent and
normatively grounded, challenging models that as-
sume stable or universal interpretations of hate
speech (Tonneau et al., 2024; Lee et al., 2023).
More fundamentally, existing models fail to cap-
ture normative and moral reasoning, limiting their
ability to distinguish culturally contingent hate
speech from harmless language (Trager et al.,
2025b; Tonneau et al., 2024; Davani et al., 2024a).
Recent studies provide empirical evidence that
moral values constitute a transferable latent rep-
resentation for hate speech across languages and
cultures (Trager et al., 2025b; Davani et al., 2024a;
Solovev and Pröllochs, 2023; Kennedy et al., 2023;
Rezapour et al., 2021). Cross-lingual studies based
on Moral Foundations Theory show that, despite
variation in the lexical realization of hateful content
across languages, hate speech targets a recurring
set of moral violations and rarely occurs in the ab-
sence of moral sentiments (Trager et al., 2025b;
Upadhyaya et al., 2023; Solovev and Pröllochs,
2022). A recent study by Davani et al. (2024a) fur-
ther shows that disagreements in hate speech anno-
tation are shaped by annotators’ moral values rather
than annotation noise. These findings suggest that
standard label aggregation and opaque modeling
approaches risk encoding dominant moral norms
while obscuring minority perspectives.
To address these limitations, which risk ampli-
fying existing social and cultural biases, we in-
troduce Supervised Moral Rationale Attention
(SMRA), the first framework to align model
attention with human-annotated moral ratio-
nales for self-explaining hate speech detection.
As illustrated in Figure 1, SMRA introduces a
normative inductive regularization into the learn-
ing process through a supervised attention loss
guided by moral rationales. While lexical markers
of hate speech are highly language- and culture-
dependent (Tonneau et al., 2024), moral cate-
gories and their rationales encode more stable
normative structures (Atari et al., 2023; Kennedy
et al., 2021), leading to reducing reliance on spuri-
ous correlations and improving robustness, trans-
parency, and cross-cultural generalization. We eval-
uate SMRA across multiple architectures, includ-
ing transformers, by jointly optimizing classifica-
tion and explanation alignment to produce human-
interpretable explanations. Experimental results
show that SMRA consistently improves explana-
tion quality and faithfulness across both binary
hate speech detection and multi-label moral senti-
ment classification. Across tasks, SMRA substan-
tially increases rationale alignment (Token F1 up
to 0.966 and IoU F1 up to 0.836), while maintain-
ing or slightly improving predictive performance
(Macro F1 from 0.757 to 0.772 and F1 from 0.903
to 0.911). Moreover, SMRA achieves comparable
or slightly improved group-based fairness, with
gains in GMB-Sub (0.9139 to 0.9212) and only
minor variations in GMB-BPSN and GMB-BNSP,
indicating that enhanced explainability does not
come at the cost of fairness.
In addition, to evaluate the effectiveness of
Large Language Models (LLMs) in hate speech
and moral sentiment classification, we conduct a
systematic evaluation across prompting strategies.
Our results show that LLMs perform poorly on
moral sentiment categories (at most F1 of 0.38),
even though incorporating moral rationales leads
to significant improvements in hate speech clas-
sification performance (≈2 −3%). Finally, we
introduce HateBRMoralXplain, the third version
of the HateBR (Vargas et al., 2022b) hate speech
benchmark dataset for low-resource Brazilian Por-
tuguese. To the best of our knowledge, Hate-
BRMoralXplain is the first large-scale expert
annotated corpus of its kind to enrich hate
speech with both moral categories and human-
annotated moral rationales.

--- Page 3 ---

Our contributions may be summarized as fol-
lows: (i) We introduce Supervised Moral Rationale
Attention (SMRA), a self-explaining framework
that aligns model attention with expert-annotated
moral rationales to improve interpretability, ro-
bustness, and contextualization in hate speech de-
tection; (ii) We release HateBRMoralXplain, an
extended version of a widely used Brazilian Por-
tuguese hate speech benchmark, augmenting prior
datasets with moral categories, moral rationales,
and socio-political metadata; the dataset, models,
inter-annotator disagreements, and code are pub-
licly available to facilitate future research; (iii) We
evaluate multiple LLMs on HateBRMoralXplain
corpus for hate speech and moral sentiment classi-
fication using prompts with different informational
components, demonstrating that the inclusion of
moral rationales provide statistically significant im-
provements in hate speech detection performance.
2
Related Work
Self-Explaining Hate Speech Detection.
Mov-
ing toward intrinsic explainability, Supervised Ra-
tional Attention (SRA) (Eilertsen et al., 2025)
aligns transformer attention with human rationales
and substantially improves rationale faithfulness;
however, its reliance on lexical rationales limits
robustness, cross-cultural generalization, and the
ability to capture deeper moral reasoning. Together,
these limitations motivate self-explaining frame-
works that explicitly incorporate moral context
beyond surface-level cues. Nirmal et al. (2024)
present SHIELD for interpretable hate speech de-
tection by incorporating GPT-3.5–generated tex-
tual rationales as additional input. The text and
rationales are encoded separately using HateBERT
and a frozen BERT, respectively, and their repre-
sentations are concatenated for classification. This
design promotes interpretability by grounding pre-
dictions in explicit rationale representations. Cal-
abrese et al. (2022) formulate Intent Classification
and Slot Filling (ICSF) task. The approach uses
a two-stage BART-based sequence-to-sequence
model that first produces a semantic sketch spec-
ifying relevant slots (e.g., Target, ProtectedChar-
acteristic), and then populates these slots with the
corresponding text spans. The abuse intent (e.g.,
Dehumanization, Derogation) is deterministically
derived from the filled slots, making the prediction
explicitly grounded in extracted evidence. This
structured output provides an intrinsic, human-
interpretable explanation, rather than a post-hoc
rationale. Kim et al. (2022) introduces an inter-
mediate token-level task in which portions of the
rationale embeddings are masked, and the model
is trained to reconstruct the masked rationale la-
bels using contextual information. This rationale
prediction objective, optimized via cross-entropy
loss on masked tokens, encourages context-aware
reasoning before fine-tuning the model for hate
speech classification.
Hate Speech with Moral Rationales.
Recent
work underscores the role of moral rationales in
advancing hate speech detection beyond surface-
level cues. MFTCXplain (Trager et al., 2025b)
introduces a multilingual benchmark with expert
annotations of hate labels, Moral Foundations The-
ory (MFT) categories, and span-level moral ratio-
nales, showing that while state-of-the-art LLMs
perform reasonably in classification, they struggle
to predict moral categories and generate faithful ex-
planations. Complementarily, Davani et al. (2024a)
demonstrate that although the lexical realization
of moral values varies across languages, moral cat-
egories provide consistent predictive signals that
improve cross-lingual robustness and transfer. Sim-
ilarly, TWISTED (Upadhyaya et al., 2023) jointly
models toxicity, moral values, and speech acts, thus
producing consistent gains across benchmarks. To-
gether, these works indicate that explicitly mod-
eling moral dimensions supports more robust and
generalizable hate speech detection while reduc-
ing reliance on spurious lexical correlations. Fur-
ther literature on the relationship between hate and
morality is discussed in Appendix B.
3
Supervised Moral Rational Attention
Supervised Moral Rational Attention (SMRA)
is a new self-explaining framework that aligns
model attention with moral rationales. SMRA en-
hances standard transformer-based text classifiers
by explicitly aligning model attention with human-
annotated moral rationales based on Moral Foun-
dation Theory for hate speech detection, follow-
ing the attention alignment framework of Eilertsen
et al. (2025). Our SMRA framework is formally
described as follows.
Tasks Definition.
We address two related tasks:
binary hate speech classification and multi-label
moral sentiment classification. Given an input text,
the first task consists of predicting whether the

--- Page 4 ---

content constitutes hate speech. The second task
aims to identify which moral foundations, as de-
fined by Moral Foundations Theory, are expressed
in the text. Supervised Moral Rational Attention
(SMRA) jointly models both tasks by guiding the
model’s attention toward human-annotated moral
rationales, ensuring that predictions are based on
morally relevant textual evidence.
Problem Setting.
Let x = (w1, . . . , wL) de-
note a tokenized input sequence of length L, and
let y ∈{0, 1, . . . , C −1} denote its class label,
where C is the number of moral categories. In the
HateBR-MoralXplain benchmark, instances are an-
notated with one or more moral categories defined
as LABELS = {NN, HN, FN, PN, AN, LN}, where
NN denotes Non-Morality, HN Harm/Care, FN
Fairness/Cheating, PN Purity/Degradation, AN
Authority/Subversion, and LN Loyalty/Betrayal.
Thus, C = 6. For a subset of the training in-
stances, we additionally provide a binary ratio-
nale mask r = (r1, . . . , rL), where ri ∈{0, 1}
indicates whether token wi is part of the human-
annotated moral rationale associated with label y.
Model Architecture.
We use a pre-trained trans-
former encoder fθ (e.g., BERTimbau) to compute
contextual representations hi for each input token
wi. A classification head predicts the moral cate-
gory based on the [CLS] representation:
ˆy = arg
max
c∈{0,1,...,C−1} softmax(Wch[CLS] + bc),
where h[CLS] ∈Rd denotes the contextual embed-
ding of the [CLS] token, and Wc ∈R1×d and
bc ∈R are the learned parameters for class c.
Attention Alignment.
For samples with avail-
able moral rationales, we encourage the model
to attend to tokens identified as morally salient
by minimizing the mean squared error (MSE) be-
tween the normalized attention distribution a and
the rationale mask r:
Overall Training Objective.
The final training
objective combines the standard cross-entropy loss
for classification with the supervised attention
alignment loss:
ℓtotal = ℓCE + α I(y ̸= NN ∧
X
i
ri > 0)ℓAAL,
where α controls the strength of attention supervi-
sion. The attention alignment loss is applied only
to instances associated with moral categories and
for which human-annotated rationales are avail-
able.
Moral Rationale Extraction.
The HateBR-
MoralXplain dataset provides free-text rationale
spans for each moral sentiment category. Ratio-
nale masks r are constructed by mapping character-
level spans to token indices using the tokenizer’s
offset mappings and are aligned with the tokeniza-
tion of x = (w1, . . . , wL), with truncation or
padding applied to match the model’s maximum
input length.
4
HateBRMoralXplain Corpus
Following prior work, we argue that hate speech
constitutes an extreme form of moralized discourse,
in which social groups are evaluated through
moral lenses (Trager et al., 2025b; Kobbe et al.,
2020). We introduce HateBRMoralXplain, the
third version of the HateBR corpus (Vargas et al.,
2022b, 2024), extending both the original HateBR
dataset and its explainable successor, HateBRX-
plain (Salles et al., 2025a). As in prior versions, the
corpus consists of 7,000 Brazilian Portuguese In-
stagram comments extracted from public political
accounts, annotated by three different experts. The
dataset includes 3,500 offensive and 3,500 non-
offensive comments, covering nine different hate
speech targets.
In the HateBRMoralXplain corpus, comments
are annotated for moral categories grounded in
Moral Foundations Theory (MFT); Graham et al.,
2013). We annotate all five core moral founda-
tions, Care/Harm, Fairness/Cheating, Loyalty/Be-
trayal, Authority/Subversion, and Purity/Degrada-
tion, capturing both virtue and vice oriented moral
expressions within a unified framework. Each com-
ment may be assigned between one and three moral
labels and their rationales, ordered by annotators
according to their perceived salience in the text,
thus representing primary, secondary, and tertiary
moral rationales. We selected two expert annota-
tors with diverse backgrounds and perspectives in
Brazil3, an important design choice given that hate
speech and moral judgments are inherently sub-
jective and shaped by annotators’ beliefs, identi-
ties, and sociocultural contexts (Prabhakaran et al.,
3Annotators completed a pre-annotation survey measuring
demographics, political ideology, moral values, personality,
and cultural orientations, to increase transparency and support
analyses of subjective decisions, See Appendix A.1

--- Page 5 ---

2021; Sap et al., 2022). Inter-annotator agreement
is measured using Cohen’s weighted Kappa with
quadratic weights, computed separately for each
moral category to account for the multi-label nature
of the annotation scheme. Results are shonw in
Appendix A.1. Class A shows substantial to almost
perfect agreement (κ = 0.811), while Classes B
and C exhibit moderate to substantial agreement
(κ = 0.671 and κ = 0.612, respectively), reflect-
ing higher subjectivity in these categories. Beyond
categorical labels, HateBRMoralXplain includes
human-annotated rationales for moral judgments.
Rationales are defined as minimal text spans that
justify why a given label was assigned, highlight-
ing the specific linguistic evidence supporting the
annotation. Moral rationale annotation follows the
same span-based protocol adopted in MFTCXplain
(Trager et al., 2025b). These rationales enable ex-
plainability, allowing models to ground their pre-
dictions in interpretable textual moral evidence
rather than relying solely on surface-level lexical
cues. Detailed rationale annotation guidelines and
examples are provided in Appendix A.1. Finally,
the corpus includes rich socio-political metadata
to support contextual and demographic analyses.
Each comment is linked to its parent Instagram
post and associated metadata indicating the politi-
cal party and gender of the politician who authored
the original post. This structure enables analy-
ses of how hate speech and moral framing vary
across political affiliation, gender, and discourse
context, while preserving the original data collec-
tion constraints and privacy safeguards established
in HateBR (Vargas et al., 2022a). An example of
HateBRMoralXplain is shown in Appendix A.1
5
Experimental Setup
5.1
Model Architecture and Settings
We evaluated three model setups: (i) standard fine-
tuning of mBERT4 and BERTimbau5 (Souza et al.,
2020), (ii) the same models fine-tuned with su-
pervised attention using moral rationales (SMRA),
and (iii) prompting LLMs with a wide range of
hateful and moral information.
Fine-Tuning mBERT and BERTimbau: We
used HuggingFace Transformers and PyTorch
to fine-tune a BERT models. In our setup, the
4https://huggingface.co/google-bert/
bert-base-multilingual-cased
5https://huggingface.co/neuralmind/
bert-base-portuguese-cased
model embeddings were fed into a linear layer for
prediction. We used a batch size of 16, a learning
rate of 2e-5, and 128 maximum sequence length.
Training was performed for 20 epochs. The dataset
was split into training (80%), validation (10%), and
test (10%) sets. Optimization was performed us-
ing the AdamW optimizer (Loshchilov and Hutter,
2017) with cross-entropy loss. The ground truth
for moral rationales corresponds to the annotation
provided by the first annotator.
Supervised Attention (SMRA): Our SMRA
framework was implemented using HuggingFace
Transformers and PyTorch, fine-tuning pre-
trained BERT-based models (BERTimbau and
mBERT) with attention supervision using BertTok-
enizer6. During training, [CLS]-to-token attention
weights from the last encoder layer were normal-
ized and aligned with human-annotated moral ra-
tionale masks via a mean squared error (MSE) loss,
combined with standard cross-entropy loss using a
weighting hyperparameter α, lambda attention and
the attention weight 0.001. Attention supervision
was applied only to examples with moral content,
and rationale masks were padded and masked to
handle variable-length sequences. Optimization
used AdamW with weight decay, training on GPU in
mini-batches.
LLMs: For both GPT-4o-mini (through Ope-
nAI API) (OpenAI, 2024) and Llama3.1-70b (on
local RTX A6000 GPUs) (Grattafiori et al., 2024),
we use a temperature of 0 for reproducibility. All
prompts are provided in Appendix C. For our ex-
periments that use translated versions of comments,
we use the Google Translate API. For these experi-
ments, we test the effects of different information:
hate speech definition, data collection context, and
predicting moral and hate speech together vs sepa-
rately. We evaluate several prompt configurations
that differ in task scope and contextual information:
The hate setting performs only hate speech clas-
sification without providing definitions or moral
rationales, whereas hate w def. includes the
definition of hate speech. The hate moral config-
uration jointly requests hate speech classification,
moral value classification, and an explanation ex-
plicitly describing the MFT. Contextual informa-
tion about data collection is incorporated in hate
w context, which focuses solely on hate speech
classification, and in hate moral w context,
6https://huggingface.co/docs/transformers/
model_doc/bert

--- Page 6 ---

which extends hate moral by additionally provid-
ing dataset context. Finally, moral-only settings
are explored through moral, which requests moral
sentiment classification and their rationales, moral
def., which further includes the hate speech defi-
nition, and moral cont.
5.2
Evaluation Metrics
Following state-of-the-art evaluation metrics for
hate speech classification, explainability, and fair-
ness/bias (Mathew et al., 2021; Attanasio et al.,
2022), we evaluate our models using the metrics
described below.
Classification: For both LLM and fine-tuned
mBERT and BERTimbau experiments, we report
the Macro F1 score for hate speech and moral
sentiment classification. Let yi ⊆Y denote the
set of human-annotated moral labels for instance i,
and let ˆyi ∈Y be the model’s predicted label. For
moral value classification, we define an adapted
correctness function:
correct(ˆyi, yi) =

1
if cˆyi ∈yi,
0
otherwise,
Explainability: We evaluate SMRA’s expla-
nations using established metrics from the inter-
pretability literature(DeYoung et al., 2020): plau-
sibility, which measures human-alignment of gen-
erated explanations, and faithfulness, which as-
sesses whether the explanation accurately reflects
the model’s decision process.
Plausibility is measured via token-level IOU F1
and Token-F1 (DeYoung et al., 2020), comparing
model rationales Mi with human-annotated moral
rationales Hi for instance i:
IOU-F1 = 1
N
N
X
i=1
Greater
|Mi ∩Hi|
|Mi ∪Hi|, 0.5

(1)
Token-F1 = 1
N
N
X
i=1
2|Mi ∩Hi|
|Mi| + |Hi|
(2)
Faithfulness is assessed through comprehensive-
ness and sufficiency (DeYoung et al., 2020). Com-
prehensiveness evaluates the influence of predicted
moral rationales ri by measuring the drop in pre-
dicted probability after removing them:
Comp = 1
N
N
X
i=1
 m(xi)j −m(xi\ri)j

(3)
Sufficiency measures whether rationales alone
are sufficient for prediction:
Suff = 1
N
N
X
i=1
 m(xi)j −m(ri)j

(4)
Fairness/Bias: We used the fairness/bias met-
rics (Borkan et al., 2019; Dixon et al., 2018) to
compute a specific identity-term (subgroup distri-
bution) and the rest (background distribution). The
three per-term bias scores are: GMB-Sub, which
measures the model’s ability to distinguish hate-
ful from non-hateful comments within a specific
identity subgroup, with low values indicating poor
subgroup performance; GMB-BPSN (Background
Positive, Subgroup Negative) assesses whether non-
hateful comments mentioning the identity are in-
correctly predicted as hateful compared to hateful
comments in the background; while GMB-BNSP
(Background Negative, Subgroup Positive) mea-
sures whether hateful comments mentioning the
identity are confused with non-hateful background
comments. Low scores in any metric indicate po-
tential bias or unfair treatment of the corresponding
identity subgroup.
6
Results and Discussion
Supervised Attention with Moral Rationales
As shown in Table 1, SMRA consistently improves
over the baseline model across both binary hate
speech classification and multi-label moral sen-
timent classification.
For binary classification,
SMRA increases Accuracy and Macro F1 (0.9114
vs. 0.9029 and 0.9114 vs. 0.9028, respectively)
and boosts explainability metrics, with higher IoU
F1 (0.8355 vs. 0.7612) and Token F1 (0.8958 vs.
0.8455), indicating better alignment with human-
annotated moral rationales. Comprehensiveness
slightly decreases (0.1530 vs. 0.1733), while Suffi-
ciency improves (0.0426 vs. 0.0657), reflecting
more concise while remaining faithful explana-
tions. In multi-label moral sentiment classifica-
tion, SMRA also outperforms the baseline model,
achieving higher Macro F1 (0.772 vs. 0.757), AU-
ROC (0.927 vs.
0.925), and Token F1 (0.966
vs. 0.725), highlighting superior rationale cov-
erage and improved interpretability without sac-
rificing predictive performance.
These results
demonstrate that SMRA effectively enhances both
classification and rationale alignment compared
to the baseline model. In addition, as shown in
Table 2, compared with other baselines, SMRA
demonstrates clear benefits in plausibility, achiev-
ing higher IoU F1 (0.7612 vs. 0.716) and Token

--- Page 7 ---

Model
Classification
Plausibility
Faithfulness
Fairness/Bias (AUC)
Acc.↑
Macro F1↑
AUROC↑
IOU F1↑
Token F1↑
AUPRC↑
Comp.↑
Suff.↓
GMB-Sub.↑
GMB-BPSN.↑
GMB-BNSP.↑
Hate classification
mBERT-base
0.5343
0.5013
0.5640
0.8186
0.8832
0.8829
0.0113
0.1381
0.4653
0.5234
0.5341
mBERT-smra
0.5414
0.5037
0.5588
0.8366
0.8953
0.9163
-0.0235
0.1376
0.4236
0.4529
0.5343
BERTimbau-base
0.9029
0.9028
0.9651
0.7612
0.8455
0.8307
0.1733
0.0657
0.9378
0.9721
0.9365
BERTimbau-smra
0.9114
0.9114
0.9648
0.8355
0.8958
0.9273
0.1530
0.0426
0.9299
0.9694
0.9197
Moral classification
mBERT-base
0.2700
0.1966
0.5158
0.727
0.9659
0.9712
0.6422
0.0848
0.4112
0.5836
0.5316
mBERT-smra
0.2114
0.1698
0.5539
0.7402
0.9659
0.9712
0.6301
0.0995
0.5362
0.5912
0.6123
BERTimbau-base
0.720
0.757
0.925
0.235
0.725
0.915
0.8452
0.0549
0.9139
0.9604
0.9650
BERTimbau-smra
0.723
0.772
0.927
0.235
0.966
0.971
0.9062
0.0562
0.9212
0.9503
0.9491
Table 1: Performance comparison across transformer-based models for hate speech and moral sentiment classifica-
tion in Portuguese using mBERT and BERTimbau under two evaluation settings: binary classification (LABELS
= [Hate, Non-Hate]) and multi-label classification (LABELS = [’NN’, ’HN’, ’FN’, ’PN’, ’AN’, ’LN’], where
NN = Non-Morality, HN = Harm/Care, FN = Fairness/Cheating, and PN = Purity/Degradation). The base variant
refers to models without supervised attention, while smra denotes our supervised attention approach guided by
moral rationales. Classification metrics capture predictive performance, explainability metrics assess rationale
quality, faithfulness metrics evaluate the causal alignment between rationales and model predictions, bias metrics
(GMB-Sub, GMB-BPSN, GMB-BNSP) quantify group-based fairness, and accuracy corresponds to Exact Match
Accuracy.
Model
Classification
Plausibility
Macro F1↑
IoU F1↑
Token F1↑
SRA
0.9114
0.716
0.745
SMRA
0.9028
0.7612
0.8455
(±0.0086)
(±0.0452)
(±0.1005)
Table 2: Comparison of our SMRA against SRA frame-
work (Eilertsen et al., 2025) across classification and
plausibility metrics. Both frameworks were evaluated
on versions of the HateBR dataset using fine-tuned
BERTimbau model, however, SRA aligns attention with
hate speech surface-lexical rationales, while our SMRA
aligns attention mechanisms with robust and context-
aware rationales based on Moral Foundation Theory.
F1 (0.8455 vs. 0.745). This reflects more precise
alignment with human-annotated moral rationales
and better capture of culturally relevant informa-
tion, while maintaining comparable classification
performance. We also compared deep learning
models on hate speech and multi-label moral clas-
sification, as shown in Table 3. BiRNN + Attention
achieves the highest exact match accuracy, while
CNNs excel in AUROC, indicating better label
ranking. BoW attains the highest Macro F1, cap-
turing frequent lexical cues but performing poorly
on accuracy and AUROC. These results highlight
trade-offs between contextual modeling, label rank-
ing, and multi-label coverage. Finally, Table 3
shows that CNN excels at binary hate speech detec-
tion, while BiRNN with SMRA performs best for
multi-label moral sentiment, highlighting the value
of supervised attention with moral rationales.
LLMs
We compare the effect of different types
of information in prompts (Abdurahman et al.,
Model
Accuracy↑
Macro F1↑
AUROC↑
Binary hate speech classification
Bag-of-Words
0.8157
0.8157
0.8991
CNN
0.8214
0.8180
0.9089
BiRNN + MaxPool
0.8114
0.8114
0.9065
BiRNN + Attention (smra)
0.8014
0.8014
0.8903
Multi-label moral sentiment classification
Bag-of-Words
0.1371
0.1982
0.5683
CNN
0.3263
0.1748
0.7283
BiRNN + MaxPool
0.4314
0.1190
0.6086
BiRNN + Attention (smra)
0.4386
0.1586
0.5855
Table 3: Comparison of classic deep learning models on
binary hate speech classification with moral rationales
and multi-label moral sentiment classification. Metrics
include Accuracy, Macro F1, and AUROC.
2024) on hate speech and moral value classifica-
tion. Table 4 reports the F1 scores for each task
and model. Including the hate speech definition
improves performance for both models on hate
speech detection and for Llama70B on moral value
classification. In contrast, providing data collec-
tion context tends to degrade performance. We also
explore jointly predicting hate speech and moral
labels, which benefits both tasks, with a stronger
improvement for moral classification. Adding the
hate speech definition to this multi-task prompting
further enhances hate speech performance. Overall,
the best prompts combine hate speech classifica-
tion with moral rationales, showing that multi-hop
moral explanations enhance both tasks and align
the model more closely with human judgments.
Effect of English Translation
Given that LLMs
generally perform better in English, we translated

--- Page 8 ---

Model and Prompt
Hate Speech (F1)
Morality (F1)
pt
en
pt
en
Gpt4o-m hate
0.864
0.739
–
–
Gpt4o-m hate w def.
0.893
0.797
–
–
Gpt4o-m hate w context
0.822
0.708
–
–
Gpt4o-m hate moral
0.870
0.745
0.369
0.378
Gpt4o-m hate moral w def.
0.897
0.790
0.366
0.396
Gpt4o-m hate moral w context
0.893
0.805
0.359
0.374
Gpt4o-m moral
–
–
0.351
0.334
Gpt4o-m moral w def.
–
–
0.346
0.358
Gpt4o-m moral w context
–
–
0.308
0.295
Llama70B hate
0.822
0.740
–
–
Llama70B hate w def.
0.901
0.871
–
–
Llama70B hate w context
0.818
0.732
–
–
Llama70B hate moral
0.826
0.725
0.370
0.360
Llama70B hate moral w def.
0.893
0.835
0.379
0.393
Llama70B hate moral w context
0.807
0.712
0.383
0.341
Llama70B moral
–
–
0.270
0.265
Llama70B moral w def.
–
–
0.318
0.306
Llama70B moral w context
–
–
0.245
0.219
Table 4: F1 scores for hate speech detection and moral
sentiment classification for datasets in Portuguese and
their English translations. Results for GPT-4o-mini and
LLaMA-70B under different prompting strategies.
the Portuguese prompts into English and applied
the same prompting techniques. Table 4 shows that
translation to English leads to lower performance
for both models across both tasks, particularly
for hate speech classification. This drop may be
due to subtle meaning loss during translation, and
moral values may not transfer seamlessly across
cultures, potentially causing the ground-truth la-
bels to shift.In addition, as shown in Table 1, the
multilingual mBERT fine-tuned model performs
poorly on our Portuguese dataset.
Ablation Study
We also analyze the effect of ex-
plicit reasoning guidance and details of the Moral
Foundations Theory. Hence, we omit those parts
and prompt the models again (the exact prompt
can be found in Appendix C). For hate speech, the
performance increased 2% compared to providing
moral foundations theory and explicit guidance for
Gpt4o-mini but it decreased 6% for Llama70b. On
the other hand, there is a huge performance drop
(34 % for Gpt4o-mini and 36% for Llama70b) for
moral value classification. This indicates that ex-
plicit guidance is more required for the moral sen-
timent classification which is more nuanced than
binary hate speech classification.
Qualitative Analysis
We extracted Instagram
comments from HateBR-MoralXplain containing
sarcasm or irony, representing challenging cases
where offensive or non-offensive meaning depends
on cultural knowledge. Table 5 shows examples il-
lustrating these challenges. Comments 1 and 2 con-
tain sarcasm and implicit hate that simple models
may miss, while comments 3 and 4 rely on politi-
cal context (e.g., “myth” refers to former president
Bolsonaro, and “dumb” is preceded by negation).
These cases highlight the need for models that can
robustly distinguish subtle, context-dependent ex-
pressions while remaining culturally aware and
transparent. Current models, which primarily rely
on surface-level lexical features, are insufficient
for capturing such nuanced hateful content. In
total, 235 offensive comments7 were extracted, ei-
ther containing sarcasm/irony or highly dependent
on cultural context. Moreover, adding prompts
with moral framing (“hate moral w definition”, see
Appendix C) enabled Llama-70B to correctly la-
bel these nuanced cases, whereas prompts without
moral framing (“hate w definition”) misclassified
them, suggesting that moral guidance can improve
robust hate speech detection.
Instagram Comments
Labels
(1) Se jogar um carteira de trabalho não sobra um
Translation: If you throw away a work permit, there won’t be
one left.
Hate
(2) Pepa só está dando tiro no pé
Translation: Pepa is just shooting herself in the foot... lol
Hate
(3) O povo não é mais burro. Você não está ouvindo seus eleitores.
Translation: The people aren’t stupid anymore. You’re not lis-
tening to your voters.
Non-Hate
(4) Chic esses filhos do mito.
Translation: Chic, these kids of the ‘Myth’.
Non-Hate
Table 5:
Examples extracted from the HateBR
dataset containing irony/sarcasm and culturally context-
dependent expressions.
7
Conclusion
We introduced Supervised Moral Rationale Atten-
tion (SMRA), a self-explaining framework for hate
speech detection that aligns model attention with
human-annotated moral rationales.
SMRA im-
proves interpretability and robustness by guiding
models to focus on morally salient spans rather
than superficial lexical features of hate speech.
To support this approach, we released HateBR-
MoralXplain, a Brazilian Portuguese benchmark
dataset enriched with moral categories, their re-
spective rationales, and socio-political metadata.
Experiments show that SMRA enhances expla-
nation faithfulness and comprehensiveness while
maintaining predictive performance and fairness.
Our results highlight the importance of integrating
moral and context-aware reasoning in hate speech
detection, providing a significant contribution to-
ward advancing transparent and context-aware ap-
proaches for addressing hate speech and fostering
research in language model interpretability.
7https://anonymous.4open.science/r/SMRA-025C/

--- Page 9 ---

Limitations
While SMRA improves interpretability and ro-
bustness in hate speech detection, several limita-
tions remain. First, our approach relies on high-
quality human-annotated moral rationales, which
are costly and time-consuming to produce, poten-
tially limiting scalability to new languages or do-
mains. Second, SMRA has been evaluated pri-
marily on Brazilian Portuguese social media data;
further studies are needed to assess generalization
across languages, platforms, and different cultural
settings. Finally, integrating moral reasoning does
not eliminate all biases in training data, and care-
ful consideration of minority perspectives remains
essential to avoid unintended harms.
Ethics Statements
The dataset will be released under an open-
source
license
CC
BY-NC
4.0
(Attribu-
tion–NonCommercial), with full transparency
regarding data collection and annotation proce-
dures.
In addition to the annotated labels, we
also release detailed per-annotator information,
enabling further analysis of annotation reliability
and subjectivity.
Particular care was taken to
ensure fair and respectful treatment of annotators
throughout the process.
We emphasize that this work is intended solely
for research purposes; any downstream deploy-
ment of automated content moderation systems
should be approached with additional safeguards,
rigorous evaluation, and responsible governance.
We truly believe that our research will make con-
tent moderation more fair and transparent.
Acknowledgements
This research is derived from the Ph.D. work of the
first author at the University of São Paulo (USP)
and was further developed during her visiting re-
searcher stay at the University of Southern Cali-
fornia (USC), under the guidance of Dr. Morteza
Dehghani and the Morality and Language Lab. We
also thank Isadora Salles for her help with the an-
notation of HateBRMoralXplain.
References
Suhaib Abdurahman, Mohammad Atari, Farzan Karimi-
Malekabadi, Mona J Xue, Jackson Trager, Peter S
Park, Preni Golazizian, Ali Omrani, and Morteza De-
hghani. 2024. Perils and opportunities in using large
language models in psychological research. PNAS
nexus, 3(7):pgae245.
Gavin Abercrombie, Dirk Hovy, and Vinodkumar Prab-
hakaran. 2023. Temporal and second language in-
fluence on intra-annotator agreement and stability in
hate speech labelling. In Proceedings of the 17th
Linguistic Annotation Workshop (LAW-XVII), pages
96–103, Toronto, Canada. Association for Computa-
tional Linguistics.
Mohammad Atari, Jonathan Haidt, Jesse Graham,
Sena Koleva, Sean T Stevens, and Morteza De-
hghani. 2023. Morality beyond the weird: How the
nomological network of morality varies across cul-
tures. Journal of Personality and Social Psychology,
125(5):1157.
Giuseppe Attanasio, Debora Nozza, Dirk Hovy, and
Elena Baralis. 2022. Entropy-based attention regu-
larization frees unintended bias mitigation from lists.
In Findings of the Association for Computational
Linguistics: ACL 2022, pages 1105–1119, Dublin,
Ireland. Association for Computational Linguistics.
Su Lin Blodgett, Solon Barocas, Hal Daumé III, and
Hanna Wallach. 2020. Language (technology) is
power: A critical survey of “bias” in NLP. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 5454–
5476, Held Online.
Daniel Borkan, Lucas Dixon, Jeffrey Sorensen, Nithum
Thain, and Lucy Vasserman. 2019. Nuanced met-
rics for measuring unintended bias with real data for
text classification. In Companion Proceedings of
The 2019 World Wide Web Conference, WWW ’19,
page 491–500, New York, NY, USA. Association for
Computing Machinery.
William J Brady, Killian L McLoughlin, Mark P Torres,
Kara F Luo, Maria Gendron, and MJ Crockett. 2023.
Overperception of moral outrage in online social
networks inflates beliefs about intergroup hostility.
Nature human behaviour, 7(6):917–927.
William J Brady, Julian A Wills, John T Jost, Joshua A
Tucker, and Jay J Van Bavel. 2017. Emotion shapes
the diffusion of moralized content in social networks.
Proceedings of the National Academy of Sciences,
114(28):7313–7318.
Agostina Calabrese, Björn Ross, and Mirella Lapata.
2022. Explainable abuse detection as intent classifi-
cation and slot filling. Transactions of the Associa-
tion for Computational Linguistics, 10:1440–1454.
Amanda Cercas Curry, Giuseppe Attanasio, Debora
Nozza, and Dirk Hovy. 2023. MilaNLP at SemEval-
2023 task 10: Ensembling domain-adapted and regu-
larized pretrained language models for robust sexism
detection. In Proceedings of the 17th International
Workshop on Semantic Evaluation (SemEval-2023),
pages 2067–2074, Toronto, Canada. Association for
Computational Linguistics.

--- Page 10 ---

Aida Davani, Mark Díaz, Dylan Baker, and Vinodku-
mar Prabhakaran. 2024a. D3CODE: Disentangling
disagreements in data across cultures on offensive-
ness detection and evaluation. In Proceedings of the
2024 Conference on Empirical Methods in Natural
Language Processing, pages 18511–18526, Miami,
Florida, USA. Association for Computational Lin-
guistics.
Aida Davani, Mark Díaz, Dylan Baker, and Vinodkumar
Prabhakaran. 2024b. Disentangling perceptions of
offensiveness: Cultural and moral correlates. In Pro-
ceedings of the 2024 ACM Conference on Fairness,
Accountability, and Transparency, pages 2007–2021,
Rio de Janeiro, Brazil.
Aida Mostafazadeh Davani, Mohammad Atari, Bren-
dan Kennedy, and Morteza Dehghani. 2023. Hate
speech classifiers learn normative social stereotypes.
Transactions of the Association for Computational
Linguistics, 11:300–319.
Thomas Davidson, Debasmita Bhattacharya, and Ing-
mar Weber. 2019. Racial bias in hate speech and
abusive language detection datasets. In Proceedings
of the 3rd Workshop on Abusive Language Online,
pages 25–35, Florence, Italy.
Jay DeYoung, Sarthak Jain, Nazneen Fatema Rajani,
Eric Lehman, Caiming Xiong, Richard Socher, and
Byron C. Wallace. 2020. ERASER: A benchmark to
evaluate rationalized NLP models. In Proceedings
of the 58th Annual Meeting of the Association for
Computational Linguistics, pages 4443–4458, On-
line. Association for Computational Linguistics.
Lucas Dixon, John Li, Jeffrey Sorensen, Nithum Thain,
and Lucy Vasserman. 2018. Measuring and mitigat-
ing unintended bias in text classification. In Proceed-
ings of the 2018 AAAI/ACM Conference on AI, Ethics,
and Society, AIES ’18, page 67–73, New York, NY,
USA. Association for Computing Machinery.
Brage Eilertsen, Røskva Bjørgfinsdóttir, Francielle Var-
gas, and Ali Ramezani-Kebrya. 2025. Aligning at-
tention with human rationales for self-explaining
hate speech detection. In Proceedings of the 40th
AAAI Conference on Artificial Intelligence. Align-
ment Track., pages 1–15, Singapore, Singapore.
Jim AC Everett. 2013. The 12 item social and economic
conservatism scale (secs). PloS one, 8(12):e82131.
Paula Fortuna and Sérgio Nunes. 2018. A survey on
automatic detection of hate speech in text. ACM
Comput. Surv., 51(4).
Michele J Gelfand, Jana L Raver, Lisa Nishii, Lisa M
Leslie, Janetta Lun, Beng Chong Lim, Lili Duan,
Assaf Almaliach, Soon Ang, Jakobina Arnadottir,
and 1 others. 2011.
Differences between tight
and loose cultures: A 33-nation study.
science,
332(6033):1100–1104.
Jesse Graham, Jonathan Haidt, Sena Koleva, Matt
Motyl, Ravi Iyer, Sean P Wojcik, and Peter H Ditto.
2013. Moral foundations theory: The pragmatic
validity of moral pluralism. In Advances in experi-
mental social psychology, volume 47, pages 55–130.
Elsevier.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten,
Alex Vaughan, Amy Yang, Angela Fan, Anirudh
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mi-
tra, Archie Sravankumar, Artem Korenev, Arthur
Hinsvark, and 542 others. 2024. The llama 3 herd of
models. Preprint, arXiv:2407.21783.
Kobi Hackenburg, William J Brady, and Manos Tsakiris.
2023. Mapping moral language on us presidential
primary campaigns reveals rhetorical networks of po-
litical division and unity. PNAS nexus, 2(6):pgad189.
Arnold K Ho, Jim Sidanius, Nour Kteily, Jennifer
Sheehy-Skeffington, Felicia Pratto, Kristin E Henkel,
Rob Foels, and Andrew L Stewart. 2015. The na-
ture of social dominance orientation: Theorizing and
measuring preferences for intergroup inequality us-
ing the new sdo7 scale. Journal of personality and
social psychology, 109(6):1003.
Peter K Jonason and Gregory D Webster. 2010. The
dirty dozen: a concise measure of the dark triad.
Psychological assessment, 22(2):420.
Brendan
Kennedy,
Mohammad
Atari,
Aida Mostafazadeh Davani,
Joe Hoover,
Ali
Omrani, Jesse Graham, and Morteza Dehghani.
2021. Moral concerns are differentially observable
in language. Cognition, 212:104696.
Brendan
Kennedy,
Preni
Golazizian,
Jackson
Trager,
Mohammad Atari,
Joe Hoover,
Aida
Mostafazadeh Davani,
and Morteza Dehghani.
2023. The (moral) language of hate. PNAS nexus,
2(7):pgad210.
Brendan Kennedy, Xisen Jin, Aida Mostafazadeh Da-
vani, Morteza Dehghani, and Xiang Ren. 2020. Con-
textualizing hate speech classifiers with post-hoc ex-
planation. In Proceedings of the 58th Annual Meet-
ing of the Association for Computational Linguistics,
pages 5435–5442, Online. Association for Computa-
tional Linguistics.
Eunsu Kim, Juyoung Suk, Philhoon Oh, Haneul Yoo,
James Thorne, and Alice Oh. 2024. CLIcK: A bench-
mark dataset of cultural and linguistic intelligence
in Korean.
In Proceedings of the 2024 Joint In-
ternational Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 3335–3346, Torino, Italia.
ELRA and ICCL.
Jiyun Kim, Byounghan Lee, and Kyung-Ah Sohn. 2022.
Why is it hate speech? masked rationale prediction
for explainable hate speech detection. In Proceed-
ings of the 29th International Conference on Com-
putational Linguistics, pages 6644–6655, Gyeongju,
Republic of Korea. International Committee on Com-
putational Linguistics.

--- Page 11 ---

Jonathan Kobbe, Ines Rehbein, Ioana Hulpus,, and
Heiner Stuckenschmidt. 2020. Exploring morality in
argumentation. In Proceedings of the 7th Workshop
on Argument Mining, pages 30–40, Online. Associa-
tion for Computational Linguistics.
Nayeon Lee, Chani Jung, and Alice Oh. 2023. Hate
speech classifiers are culturally insensitive. In Pro-
ceedings of the First Workshop on Cross-Cultural
Considerations in NLP (C3NLP), pages 35–46,
Dubrovnik, Croatia. Association for Computational
Linguistics.
Ilya Loshchilov and Frank Hutter. 2017.
Decou-
pled weight decay regularization. arXiv preprint
arXiv:1711.05101.
Marian Marchal, Merel Scholman, Frances Yung, and
Vera Demberg. 2022. Establishing annotation qual-
ity in multi-label annotations. In Proceedings of
the 29th International Conference on Computational
Linguistics, pages 3659–3668, Gyeongju, Republic
of Korea. International Committee on Computational
Linguistics.
Binny Mathew, Punyajoy Saha, Seid Muhie Yimam,
Chris Biemann, Pawan Goyal, and Animesh Mukher-
jee. 2021. Hatexplain: A benchmark dataset for
explainable hate speech detection. In Proceedings of
the 35th AAAI Conference on Artificial Intelligence,
volume 35, pages 14867–14875, Held Online.
Mary L McHugh. 2012. Interrater reliability: the kappa
statistic. Biochemia medica, 22(3):276–282.
Jari-Mikko Meriläinen. 2024. The role of gender in hate
speech targeting politicians: Evidence from finnish
twitter. International Journal of Politics, Culture,
and Society, pages 1–27.
Anirudh Mittal, Pranav Jeevan P, Prerak Gandhi,
Diptesh Kanojia, and Pushpak Bhattacharyya. 2021.
“so you think you’re funny?”: Rating the humour
quotient in standup comedy. In Proceedings of the
2021 Conference on Empirical Methods in Natural
Language Processing, pages 10073–10079, Online
and Punta Cana, Dominican Republic. Association
for Computational Linguistics.
Ayushi Nirmal, Amrita Bhattacharjee, Paras Sheth, and
Huan Liu. 2024. Towards interpretable hate speech
detection using large language model-extracted ratio-
nales. In Proceedings of the 8th Workshop on Online
Abuse and Harms (WOAH 2024), pages 223–233,
Mexico City, Mexico. Association for Computational
Linguistics.
OpenAI. 2024. Gpt-4o mini: advancing cost-efficient
intelligence.
Niels Bjørn Grund Petersen, Rasmus Tue Pedersen, and
Mads Thau. 2025. Citizens’ perceptions of online
abuse directed at politicians: Evidence from a survey
experiment. European Journal of Political Research,
64(2):790–809.
Fabio Poletto, Valerio Basile, Manuela Sanguinetti,
Cristina Bosco, and Viviana Patti. 2021. Resources
and benchmark corpora for hate speech detection: a
systematic review. Language Resources and Evalua-
tion, 55(3):477–523.
Vinodkumar Prabhakaran, Aida Mostafazadeh Davani,
and Mark Diaz. 2021. On releasing annotator-level
labels and information in datasets. In Proceedings
of the Joint 15th Linguistic Annotation Workshop
(LAW) and 3rd Designing Meaning Representations
(DMR) Workshop, pages 133–138, Punta Cana, Do-
minican Republic. Association for Computational
Linguistics.
Rezvaneh Rezapour, Ly Dinh, and Jana Diesner. 2021.
Incorporating the measurement of moral foundations
theory into analyzing stances on controversial topics.
In Proceedings of the 32nd ACM Conference on Hy-
pertext and Social Media, page 177–188, New York,
NY, USA. Association for Computing Machinery.
Ludovic Rheault, Erica Rayment, and Andreea Musu-
lan. 2019. Politicians in the line of fire: Incivility and
the treatment of women on social media. Research
& Politics, 6(1):2053168018816228.
Isadora Salles, Francielle Vargas, and Fabrício Ben-
evenuto. 2025a.
HateBRXplain: A benchmark
dataset with human-annotated rationales for explain-
able hate speech detection in Brazilian Portuguese.
In Proceedings of the 31st International Conference
on Computational Linguistics, pages 6659–6669,
Abu Dhabi, UAE. Association for Computational
Linguistics.
Isadora Salles, Francielle Vargas, and Fabrício Ben-
evenuto. 2025b. Hatebrxplain: A benchmark dataset
with human-annotated rationales for explainable hate
speech detection in brazilian portuguese. In Pro-
ceedings of the 31st International Conference on
Computational Linguistics, pages 6659–6669.
Maarten Sap, Dallas Card, Saadia Gabriel, Yejin Choi,
and Noah A. Smith. 2019. The risk of racial bias in
hate speech detection. In Proceedings of the 57th
Annual Meeting of the Association for Computational
Linguistics, pages 1668–1678, Florence, Italy.
Maarten Sap, Swabha Swayamdipta, Laura Vianna,
Xuhui Zhou, Yejin Choi, and Noah A. Smith. 2022.
Annotators with attitudes: How annotator beliefs
and identities bias toxic language detection. In Pro-
ceedings of the 2022 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies, pages
5884–5906, Seattle, United States. Association for
Computational Linguistics.
Kristina Bakkær Simonsen and Tobias Widmann. 2025.
When do political parties moralize?: A cross-national
study of the use of moral language in political com-
munication on immigration. British Journal of Polit-
ical Science, 55:e33.

--- Page 12 ---

Theodore M Singelis, Harry C Triandis, Dharm PS
Bhawuk, and Michele J Gelfand. 1995. Horizontal
and vertical dimensions of individualism and collec-
tivism: A theoretical and measurement refinement.
Cross-cultural research, 29(3):240–275.
Kirill Solovev and Nicolas Pröllochs. 2023. Moralized
language predicts hate speech on social media. PNAS
nexus, 2(1):pgac281.
Kirill Solovev and Nicolas Pröllochs. 2022. Moralized
language predicts hate speech on social media. PNAS
Nexus, 2(1):pgac281.
Christopher J Soto and Oliver P John. 2017. Short and
extra-short forms of the big five inventory–2: The bfi-
2-s and bfi-2-xs. Journal of Research in Personality,
68:69–81.
Fábio Souza, Rodrigo Nogueira, and Roberto Lotufo.
2020. BERTimbau: pretrained BERT models for
Brazilian Portuguese. In 9th Brazilian Conference
on Intelligent Systems, BRACIS, Rio Grande do Sul,
Brazil, October 20-23 (to appear).
Manuel Tonneau, Diyi Liu, Samuel Fraiberger, Ralph
Schroeder, Scott A. Hale, and Paul Röttger. 2024.
From languages to geographies: Towards evaluating
cultural bias in hate speech datasets. In Proceedings
of the 8th Workshop on Online Abuse and Harms
(WOAH 2024), pages 283–311, Mexico City, Mexico.
Association for Computational Linguistics.
Jackson Trager, Farzan Karimi-Malekabadi, Suhaib Ab-
durahman, and Morteza Dehghani. 2025a.
Hate
is justified when values are threatened: Evidence
from ideologically threatening tweets and real world
events. arxiv.
Jackson Trager, Francielle Vargas, Diego Alves, Mat-
teo Guida, Mikel K Ngueajio, Ameeta Agrawal,
Yalda Daryani, Farzan Karimi-Malekabadi, and
Flor Miriam Plaza-del Arco. 2025b. Mftcxplain:
A multilingual benchmark dataset for evaluating
the moral reasoning of llms through multi-hop hate
speech explanation. In Findings of the Association
for Computational Linguistics: EMNLP 2025, pages
15709–15740, Suzhou, China.
Jackson Trager, Alireza S Ziabari, Aida Mostafazadeh
Davani,
Preni
Golazizian,
Farzan
Karimi-
Malekabadi,
Ali Omrani,
Zhihe Li,
Brendan
Kennedy, Nils Karl Reimer, Melissa Reyes, and 1
others. 2022. The moral foundations reddit corpus.
arXiv preprint arXiv:2208.05545.
Apoorva Upadhyaya, Marco Fisichella, and Wolfgang
Nejdl. 2023.
Toxicity, morality, and speech act
guided stance detection. In Findings of the Associ-
ation for Computational Linguistics: EMNLP 2023,
pages 4464–4478, Singapore. Association for Com-
putational Linguistics.
Francielle Vargas, Isabelle Carvalho, Fabiana Rodrigues
de Góes, Thiago Pardo, and Fabrício Benevenuto.
2022a. Hatebr: A large expert annotated corpus
of brazilian instagram comments for offensive lan-
guage and hate speech detection. In Proceedings of
the Thirteenth Language Resources and Evaluation
Conference, pages 7174–7183.
Francielle Vargas, Isabelle Carvalho, Ali Hürriyeto˘glu,
Thiago Pardo, and Fabrício Benevenuto. 2023. So-
cially responsible hate speech detection: Can classi-
fiers reflect social stereotypes? In Proceedings of the
14th International Conference on Recent Advances
in Natural Language Processing, pages 1187–1196,
Varna, Bulgaria. INCOMA Ltd., Shoumen, Bulgaria.
Francielle Vargas, Isabelle Carvalho, Thiago A. S.
Pardo, and Fabrício Benevenuto. 2024.
Context-
aware and expert data resources for brazilian por-
tuguese hate speech detection. Natural Language
Processing, 31(2):435–456.
Francielle Vargas, Isabelle Carvalho, Fabiana Ro-
drigues de Góes, Thiago Pardo, and Fabrício Ben-
evenuto. 2022b. HateBR: A large expert annotated
corpus of Brazilian Instagram comments for offen-
sive language and hate speech detection. In Pro-
ceedings of the Thirteenth Language Resources and
Evaluation Conference, pages 7174–7183, Marseille,
France. European Language Resources Association.
Francielle Vargas, Fabiana Rodrigues de Góes, Isabelle
Carvalho, Fabrício Benevenuto, and Thiago Pardo.
2021. Contextual-lexicon approach for abusive lan-
guage detection. In Proceedings of the International
Conference on Recent Advances in Natural Language
Processing (RANLP 2021), pages 1438–1447, Held
Online. INCOMA Ltd.
Sze-Yuh Nina Wang and Yoel Inbar. 2021.
Moral-
language use by us political elites. Psychological
Science, 32(1):14–26.
Michael Wiegand, Josef Ruppenhofer, and Thomas
Kleinbauer. 2019. Detection of Abusive Language:
the Problem of Biased Datasets. In Proceedings of
the 2019 Conference of the North American Chap-
ter of the Association for Computational Linguis-
tics: Human Language Technologies, pages 602–608,
Minneapolis, United States.
Sidney Wong. 2024. Sociocultural considerations in
monitoring anti-LGBTQ+ content on social me-
dia.
In Proceedings of the 2nd Workshop on
Cross-Cultural Considerations in NLP, pages 84–97,
Bangkok, Thailand. Association for Computational
Linguistics.
Li Zhou, Antonia Karamolegkou, Wenyu Chen, and
Daniel Hershcovich. 2023. Cultural compass: Pre-
dicting transfer learning success in offensive lan-
guage detection with cultural features. In Findings
of the Association for Computational Linguistics:
EMNLP 2023, pages 12684–12702, Singapore. As-
sociation for Computational Linguistics.

--- Page 13 ---

A
Appendix
A.1
HateBRMoralXplain Corpus
We introduce HateBRMoralXplain, the third ver-
sion of the HateBR corpus (Vargas et al., 2022b,
2024), which extends both the original HateBR
dataset and its explainable successor, HateBRX-
plain (Salles et al., 2025a). As in previous versions,
the corpus comprises 7,000 Brazilian Portuguese
Instagram comments collected from public polit-
ical accounts and annotated by three expert anno-
tators. The dataset includes 3,500 offensive and
3,500 non-offensive comments, spanning nine dis-
tinct hate speech targets.
A.1.1
Data Collection
HateBRMoralXplain builds upon the HateBR cor-
pus (Vargas et al., 2022a), a large-scale expert-
annotated dataset of Brazilian Portuguese Insta-
gram comments collected from public political ac-
counts. The political domain was selected due to its
high prevalence of offensive and hateful language
targeting social groups, as well as its relevance for
studying ideological polarization, moral framing,
and identity-based attacks. The original HateBR
corpus consists of 7,000 comments collected from
the comment sections of Brazilian politicians’ In-
stagram posts published during the second half of
2019. Data were extracted using the Instagram
API, following a controlled sampling strategy that
balanced political ideology and gender of the ac-
count holders. Specifically, comments were col-
lected from six public political accounts, evenly
distributed across left- and right-leaning parties
and including both male and female politicians.
Only public posts and comments were included,
and no personally identifiable information beyond
publicly available metadata was retained. Prior to
annotation, the data underwent a cleaning process
to remove noise such as URLs, isolated mentions,
and comments containing only emojis or laugh-
ter tokens. Hashtags and expressive markers were
preserved, as they often convey pragmatic or af-
fective meaning relevant to hate speech and moral
expression. This procedure follows the data col-
lection and preprocessing pipeline established in
HateBR and HateBRXplain (Vargas et al., 2022a;
Salles et al., 2025b). HateBRMoralXplain reuses
the same 7,000 comments from HateBR and Hate-
BRXplain, ensuring continuity across dataset ver-
sions while enabling direct comparison between
hate speech labels, hate rationales, and the newly
introduced moral annotations.
A.1.2
Annotation Process
The annotation process in HateBRMoralXplain
extends the multi-layer expert annotation frame-
work introduced in HateBR and HateBRXplain by
incorporating moral labels and moral rationales
grounded in Moral Foundations Theory (MFT).
The resulting annotation scheme enables the joint
study of hate speech detection, explainability, and
moral reasoning within a single unified corpus.
Annotations were conducted by expert annotators
with backgrounds in linguistics, hate speech re-
search, and computational social science. One an-
notator participated in prior versions of the dataset,
ensuring continuity and calibration across versions,
while a second annotator was newly introduced
and trained using the same guidelines. As in prior
work, annotation followed an iterative process with
guideline refinement and discussion to ensure con-
ceptual alignment, following the annotator-in-the-
loop paradigm described in MFTCXplain (Trager
et al., 2025b). Tables 6 and 7 show an example of
an Instagram comment extracted from our HateBR-
MoralXplain dataset, including moral labels, moral
rationales annotations, and metadata.
A.1.3
Hate Speech Definition
We adopt the same hate speech definition used
in HateBR and HateBRXplain to maintain consis-
tency across dataset versions. Hate speech is de-
fined as a form of offensive language that expresses
violence, hostility, intolerance, prejudice, or dis-
crimination against an individual or group based
on protected social characteristics such as race,
gender, religion, sexual orientation, nationality, or
political affiliation (Fortuna and Nunes, 2018,?).
This definition captures both explicit and implicit
forms of hate, acknowledging that hateful intent
may be conveyed through indirect language, sar-
casm, or moralized justifications rather than overt
slurs. Importantly, not all offensive language con-
stitutes hate speech: offensive comments that do
not target a social group are labeled as non-hateful,
following the distinction established in the HateBR
annotation schema (Vargas et al., 2022a).
A.1.4
Moral Categories
To classify expressions of moral sentiment, we rely
on the framework provided by Moral Foundations
Theory (MFT; Graham et al., 2013). MFT pro-
poses that human moral judgment draws upon a set

--- Page 14 ---

ID
Instagram Comment
HS Label
MFT Label
Rationales
MFT Label
Rationales MFT Label
Rationales
Portuguese
Celebrar a morte de milhões
de judeus?
Estúpido, no-
jento.
Hate
AN
Celebrar a morte
de
milhões
de
judeus?
PN
nojento
HN
estúpido
Translation
Celebrating the death of mil-
lions of Jews? Stupid, dis-
gusting.
Hate
AN
Celebrating
the
death of millions
of Jews?
PN
disgusting
HN
stupid
Table 6: Example of an Instagram comment from HateBRMoralXplain with moral labels and moral rationales.
Instagram Comment
Summary Post
Themes Post
Politician
Gender
Politician
Party
Link Post
O povo ODEIA vcs,
bando de
marginais. Translation: The people
HATE you, you bunch of criminals.
The post announces an event
in Brasília held in defense
of
national
and
popular
sovereignty, shared by Fer-
nando Haddad (Brazilian
politician)
National
sovereignty; Pop-
ular
sovereignty;
Political mobiliza-
tion
male
right
https://www.
instagram.com/
p/B1_m4F5lO_d/
Table 7: Example of a Brazilian political Instagram comment extracted from our HateBRMoralXplain corpus, with
metadata annotated for post themes, politician gender and party, and post link.
of core psychological systems that are widely ob-
served across societies (Atari et al., 2023). These
systems are typically organized along five founda-
tional domains, each of which can be expressed
through both moral virtues (positive adherence)
and moral violations (negative transgressions). The
framework has become a central resource for com-
putational investigations of morality, including
prior work in automated analysis of moral and
hateful discourse (e.g., Trager et al., 2025b). In our
study, we adopt these five foundational domains
to guide our annotation of moral expression. Brief
descriptions of each domain are provided below:
Care vs. Harm: (HN) Concerns the protection
and welfare of others. Moral language in this do-
main emphasizes empathy, compassion, and safe-
guarding, while violations involve inflicting harm,
dismissing suffering, or expressing cruelty.
Fairness vs. Cheating: (FN) Focuses on equi-
table treatment, rights, and reciprocity. Virtuous
expressions include justice, honesty, and impar-
tiality, whereas violations highlight exploitation,
deceit, or rule-breaking.
Loyalty vs. Betrayal: (LN) Centers on group
cohesion and social allegiances. Loyalty indicates
devotion to one’s group or allies, while betrayal
refers to abandonment, disloyalty, or undermining
the collective.
Authority vs. Subversion (AN): Involves respect
for legitimate leadership, social order, and tradition.
Endorsing authority reflects deference and duty to
existing structures; subversion entails resistance,
disrespect, or challenges to hierarchy.
Purity vs. Degradation (PN): Pertains to cultural
norms surrounding cleanliness, modesty, and sanc-
tity. Purity involves maintaining physical or moral
integrity, whereas degradation is signaled through
impurity, disgust, or perceived contamination.
A.1.5
Moral Rationales
For each assigned moral label, annotators identified
moral rationales by highlighting the specific spans
of text that expressed or justified the corresponding
moral judgment. Similar to hate rationales, moral
rationales were defined as the smallest set of words
or phrases sufficient to convey the moral meaning
underlying the label. Annotators were instructed
to select distinct rationales for each moral label
and to avoid reusing the same span across multiple
labels whenever possible. This constraint encour-
ages fine-grained differentiation between moral
foundations and supports multi-hop explanation
settings, where models must connect hate speech
detection to moral reasoning through intermediate
justifications.
A.1.6
Annotator’s Profile
The updated version of the corpus was annotated
by the same two specialists as in the previous re-
lease. Given the complexity of offensive language
and hate speech detection in a highly politicized
domain, both annotators have advanced academic
training (PhD or MSc). To minimize bias and its
potential impact on the results, the annotators were
intentionally diversified across key demographic

--- Page 15 ---

dimensions: both are women, one identifying as
liberal and the other as conservative; one is white
and the other Black; and they come from different
Brazilian regions (North and Southeast).
Unlike prior versions of this corpus, the cur-
rent release includes detailed pre-annotation sur-
vey data collected from annotators alongside stan-
dard demographic information. Annotators com-
pleted an extensive pre-annotation survey designed
to capture psychological, cultural, and sociodemo-
graphic characteristics that may shape moral and
hate-speech judgments(Trager et al., 2022). These
measures included sexual orientation, household
income, primary and secondary language(s), reli-
gious affiliation, and political ideology, assessed
both via self-identification and using the Social
and Economic Conservatism Scale (SECS; Everett,
2013). Annotators also completed validated in-
struments measuring moral values and related in-
dividual differences, including the Moral Founda-
tions Questionnaire-2 (Atari et al., 2023), Big Five
personality traits (Soto and John, 2017), Social
Dominance Orientation (Ho et al., 2015), Collec-
tivism/Individualism (Singelis et al., 1995), Cul-
tural Tightness–Looseness (Gelfand et al., 2011),
and Dark Triad traits (Jonason and Webster, 2010).
Basic descriptive analyses indicated that our anno-
tators, overall, leaned more liberal politically, came
from higher-income households compared to na-
tional averages, and had higher levels of formal ed-
ucation. Following the recommendations of Prab-
hakaran et al. (2021) and Davani et al. (2024b), we
include these annotator measures to increase trans-
parency and utility for downstream researchers.
We encourage future work to investigate how these
annotator characteristics may influence labeling
decisions, particularly given the subjectivity of
moral and hate speech judgments (see Davani et al.,
2024b; Salles et al., 2025b).
A.1.7
Annotation Evaluation
Inter-Annotator Agreement.
Inter-annotator
agreement was assessed using Cohen’s Kappa
(McHugh, 2012), including its weighted variant
with quadratic weights (Marchal et al., 2022; Mit-
tal et al., 2021), in order to measure the level of
agreement between two independent annotators
considering our multi-class moral labels dataset.
Agreement was computed separately for each an-
notation dimension, considering only instances
in which both annotators provided an explicit la-
bel; instances with null or missing annotations
were excluded from the analysis. Since the la-
bels follow an ordinal scale with three categories
(k = 3), weighted Cohen’s Kappa was employed
to account for the degree of disagreement be-
tween categories.
Quadratic weights were de-
fined as wij = 1 −(i−j)2
(k−1)2 , assigning lower penal-
ties to disagreements between adjacent labels and
higher penalties to disagreements between distant
labels. The weighted Kappa was computed as
κw = 1 −
P
i,j wijOij
P
i,j wijEij , where Oij denotes the
observed proportion of label pairs (i, j) and Eij
denotes the expected proportion of agreement by
chance. All agreement scores were computed us-
ing the cohen_kappa_score implementation from
scikit-learn with weights="quadratic".
Table 8: Inter-annotator agreement measured using Co-
hen’s weighted Kappa with quadratic weights, com-
puted separately for each annotation class. Instances
with null annotations were excluded.
Class
Quadratic Weighted Kappa
Class A
0.811
Class B
0.671
Class C
0.612
The values of quadratic weighted Cohen’s
Kappa indicate moderate to substantial inter-
annotator agreement across the three evaluated
classes. In particular, Class A exhibits substan-
tial to almost perfect agreement (κ = 0.811),
suggesting a high degree of shared understanding
between annotators for this category. Classes B
and C show moderate to substantial agreement
(κ = 0.671 and κ = 0.612, respectively), reflect-
ing the greater subjectivity associated with these
categories. The use of quadratic weights is espe-
cially appropriate in this context, as it penalizes
disagreements between semantically distant cate-
gories more strongly while assigning lower penal-
ties to disagreements between adjacent labels. The
observed agreement patterns suggest that most dis-
agreements occur between neighboring categories
rather than extreme opposites, which is expected
in annotation tasks involving nuanced moral and
discourse-related judgments. Overall, these agree-
ment scores are consistent with prior work on sub-
jective semantic annotation tasks and support the
reliability of the annotation protocol and the suit-
ability of the dataset for downstream modeling and
analysis.

--- Page 16 ---

B
Hate and Morality
A growing literature in moral psychology and com-
putational social science shows that moral lan-
guage is routinely used to moralize intergroup
conflict, legitimize hostility, and structure polit-
ical judgment, with distinct moral foundations sys-
tematically associated with ideological positions
and group-based boundaries (Graham et al., 2013;
Wang and Inbar, 2021; Hackenburg et al., 2023;
Trager et al., 2025a). In the specific case of hate-
ful and derogatory discourse, recent work argues
that hate is often expressed through morally loaded
justifications (e.g., purity, authority, loyalty) rather
than only explicit slurs, and that moral-emotional
dynamics such as moral outrage are central to how
hostile content is produced and circulated online
(Kennedy et al., 2023; Brady et al., 2017, 2023).
At the same time, research on online political com-
munication consistently finds that women in public
life, including politicians, face disproportionate
and gendered abuse, and that abusive and hateful
content varies with political identities and partisan
contexts (Rheault et al., 2019; Meriläinen, 2024;
Petersen et al., 2025). These patterns are also
shaped by culture and language: most morality-
aware and explainable hate resources are English-
centric, while moral and political language usage
and its correlation vary across contexts, motivat-
ing the need for low-resource, culturally situated
datasets (Salles et al., 2025a; Vargas et al., 2022b;
Simonsen and Widmann, 2025). By incorporat-
ing metadata on the gender and political party of
the targeted politician and focusing on Brazilian
Portuguese as a low-resource language, HateBR-
MoralXplain supports socio-demographic and lin-
guistic analyses of moralized hate speech that re-
main underexplored in the current explainable hate
speech literature.
C
LLM Prompts
Hate Speech Definition:
Hate Speech can result
due to some of the followings:
• Having a term or expression with any pejora-
tive connotation.
• Having a sequence of swear words.
• Having a sequence of at least two terms,
or/and expressions with any pejorative conno-
tation expressed explicitly or implicitly.
Context:
The data was collected during the Bol-
sonaro government in 2019. We collected bal-
anced data from left- and right-wing Brazilian
politicians, ensuring balanced gender representa-
tion. The Jair Bolsonaro government began on
1 January 2019, after his election in late 2018 —
Bolsonaro won on a wave of anti-establishment
sentiment, capitalizing on widespread frustration
with corruption scandals and economic stagnation.
Early in his presidency, he pursued a conserva-
tive, pro-market agenda: notably, he enacted a
major pension-reform in 2019 aiming to reduce
social-security costs. His government was marked
by sharp shifts in environmental and Indigenous-
land policy — protections were scaled back, en-
forcement relaxed, and deforestation pressures in-
creased, drawing both domestic and international
criticism.
Hate only:
Analyze the following text “{text}”
for hate speech.
Provide your analysis in this exact format:
hate_label: [YES if the text contains hate speech,
NO otherwise]
Provide ONLY the required output format with no
additional text, explanations, or justifications.
Hate with definition:
Analyze the following text
“{text}” for hate speech.
{definition}
Provide your analysis in this exact format:
hate_label: [YES if the text contains hate speech,
NO otherwise]
Provide ONLY the required output format with no
additional text, explanations, or justifications.
Hate with context:
Analyze the following text
“{text}” for hate speech.
{context}
Provide your analysis in this exact format:
hate_label: [YES if the text contains hate speech,
NO otherwise]
Provide ONLY the required output format with no
additional text, explanations, or justifications.
Hate and moral:
Analyze the following text
“{text}” for hate speech and identify its underlying
moral value dimensions:
The Moral Foundations Theory framework repre-
sents core ethical ad psychological concerns that
come in paired positive vs negative expressions:
• care vs harm:
Involves concern for the
well-being of others, with virtues expressed

--- Page 17 ---

through care, protection, or nurturance, and
vices involving harm, cruelty, or indifference
to suffering.
• fairness vs cheating: morals related to justice,
rights, and reciprocity, with fairness indicat-
ing equity, rule-following, and cheating denot-
ing exploitation, dishonesty, or manipulation.
• loyalty vs betrayal: morals related to group-
based morality, where loyalty refers to solidar-
ity, allegiance, and in-group defense, while
betrayal signals disloyalty or abandonment of
one’s group.
• authority vs subversion: morals related to re-
spect for tradition, and legitimate hierarchies,
with authority indicating respect or deference
to leadership or norms, and subversion indi-
cating rebellion, disrespect, or disobedience.
• sanctity vs degradation: morals related to pu-
rity, contamination, with Purity is associated
with cleanliness, modesty, or moral elevation,
while degradation includes defilement, ob-
scenity,or perceived corruption.
Provide your analysis in this exact format:
hate_label: [YES if the text contains hate speech,
NO otherwise]
moral_value: [the single most prominent moral
foundations from: care, harm, fairness, cheating,
authority, subversion, sanctity, degradation, loy-
alty, betrayal. If no clear moral foundation applies,
write “None”]
explanation: [provide a brief evidence based jus-
tification, specifically highlighting the words or
phrases that triggered your moral value classifica-
tion. If none, write “None”]
Provide ONLY the required output format with no
additional text, explanations, or justifications.
Hate and moral with context:
Analyze the fol-
lowing text “{text}” for hate speech and identify
its underlying moral value dimensions:
The Moral Foundations Theory framework repre-
sents core ethical ad psychological concerns that
come in paired positive vs negative expressions:
• care vs harm:
Involves concern for the
well-being of others, with virtues expressed
through care, protection, or nurturance, and
vices involving harm, cruelty, or indifference
to suffering.
• fairness vs cheating: morals related to justice,
rights, and reciprocity, with fairness indicat-
ing equity, rule-following, and cheating denot-
ing exploitation, dishonesty, or manipulation.
• loyalty vs betrayal: morals related to group-
based morality, where loyalty refers to solidar-
ity, allegiance, and in-group defense, while
betrayal signals disloyalty or abandonment of
one’s group.
• authority vs subversion: morals related to re-
spect for tradition, and legitimate hierarchies,
with authority indicating respect or deference
to leadership or norms, and subversion indi-
cating rebellion, disrespect, or disobedience.
• sanctity vs degradation: morals related to pu-
rity, contamination, with Purity is associated
with cleanliness, modesty, or moral elevation,
while degradation includes defilement, ob-
scenity,or perceived corruption.
{context}
Provide your analysis in this exact format:
hate_label: [YES if the text contains hate speech,
NO otherwise]
moral_value: [the single most prominent moral
foundations from: care, harm, fairness, cheating,
authority, subversion, sanctity, degradation, loy-
alty, betrayal. If no clear moral foundation applies,
write “None”]
explanation: [provide a brief evidence based jus-
tification, specifically highlighting the words or
phrases that triggered your moral value classifica-
tion. If none, write “None”]
Provide ONLY the required output format with no
additional text, explanations, or justifications.
Hate and moral with definition:
Analyze the
following text “{text}” for hate speech and identify
its underlying moral value dimensions:
The Moral Foundations Theory framework repre-
sents core ethical ad psychological concerns that
come in paired positive vs negative expressions:
• care vs harm:
Involves concern for the
well-being of others, with virtues expressed
through care, protection, or nurturance, and
vices involving harm, cruelty, or indifference
to suffering.
• fairness vs cheating: morals related to justice,
rights, and reciprocity, with fairness indicat-

--- Page 18 ---

ing equity, rule-following, and cheating denot-
ing exploitation, dishonesty, or manipulation.
• loyalty vs betrayal: morals related to group-
based morality, where loyalty refers to solidar-
ity, allegiance, and in-group defense, while
betrayal signals disloyalty or abandonment of
one’s group.
• authority vs subversion: morals related to re-
spect for tradition, and legitimate hierarchies,
with authority indicating respect or deference
to leadership or norms, and subversion indi-
cating rebellion, disrespect, or disobedience.
• sanctity vs degradation: morals related to pu-
rity, contamination, with Purity is associated
with cleanliness, modesty, or moral elevation,
while degradation includes defilement, ob-
scenity,or perceived corruption.
{definition}
Provide your analysis in this exact format:
hate_label: [YES if the text contains hate speech,
NO otherwise]
moral_value: [the single most prominent moral
foundations from: care, harm, fairness, cheating,
authority, subversion, sanctity, degradation, loy-
alty, betrayal. If no clear moral foundation applies,
write “None”]
explanation: [provide a brief evidence based jus-
tification, specifically highlighting the words or
phrases that triggered your moral value classifica-
tion. If none, write “None”]
Provide ONLY the required output format with no
additional text, explanations, or justifications.
Moral only:
Identify the underlying moral value
dimensions in the following text "text". The Moral
Foundations Theory framework represents core
ethical ad psychological concerns that come in
paired positive vs negative expressions:
• care vs harm:
Involves concern for the
well-being of others, with virtues expressed
through care, protection, or nurturance, and
vices involving harm, cruelty, or indifference
to suffering.
• fairness vs cheating: morals related to justice,
rights, and reciprocity, with fairness indicat-
ing equity, rule-following, and cheating denot-
ing exploitation, dishonesty, or manipulation.
• loyalty vs betrayal: morals related to group-
based morality, where loyalty refers to solidar-
ity, allegiance, and in-group defense, while
betrayal signals disloyalty or abandonment of
one’s group.
• authority vs subversion: morals related to re-
spect for tradition, and legitimate hierarchies,
with authority indicating respect or deference
to leadership or norms, and subversion indi-
cating rebellion, disrespect, or disobedience.
• sanctity vs degradation: morals related to pu-
rity, contamination, with Purity is associated
with cleanliness, modesty, or moral elevation,
while degradation includes defilement, ob-
scenity,or perceived corruption.
Provide your analysis in this exact format:
moral_value: [the single most prominent moral
foundations from: care, harm, fairness, cheating,
authority, subversion, sanctity, degradation, loy-
alty, betrayal. If no clear moral foundation applies,
write “None”]
explanation: [provide a brief evidence based jus-
tification, specifically highlighting the words or
phrases that triggered your moral value classifica-
tion. If none, write “None”]
Provide ONLY the required output format with
no additional text, explanations, or justifications.
Moral with definition:
Identify the underlying
moral value dimensions in the following text "text".
The Moral Foundations Theory framework repre-
sents core ethical ad psychological concerns that
come in paired positive vs negative expressions:
• care vs harm:
Involves concern for the
well-being of others, with virtues expressed
through care, protection, or nurturance, and
vices involving harm, cruelty, or indifference
to suffering.
• fairness vs cheating: morals related to justice,
rights, and reciprocity, with fairness indicat-
ing equity, rule-following, and cheating denot-
ing exploitation, dishonesty, or manipulation.
• loyalty vs betrayal: morals related to group-
based morality, where loyalty refers to solidar-
ity, allegiance, and in-group defense, while
betrayal signals disloyalty or abandonment of
one’s group.

--- Page 19 ---

• authority vs subversion: morals related to re-
spect for tradition, and legitimate hierarchies,
with authority indicating respect or deference
to leadership or norms, and subversion indi-
cating rebellion, disrespect, or disobedience.
• sanctity vs degradation: morals related to pu-
rity, contamination, with Purity is associated
with cleanliness, modesty, or moral elevation,
while degradation includes defilement, ob-
scenity,or perceived corruption.
{definition}
Provide your analysis in this exact format:
moral_value: [the single most prominent moral
foundations from: care, harm, fairness, cheating,
authority, subversion, sanctity, degradation, loy-
alty, betrayal. If no clear moral foundation applies,
write “None”]
explanation: [provide a brief evidence based jus-
tification, specifically highlighting the words or
phrases that triggered your moral value classifica-
tion. If none, write “None”]
Provide ONLY the required output format with
no additional text, explanations, or justifications.
Moral with context:
Identify the underlying
moral value dimensions in the following text "text".
The Moral Foundations Theory framework repre-
sents core ethical ad psychological concerns that
come in paired positive vs negative expressions:
• care vs harm:
Involves concern for the
well-being of others, with virtues expressed
through care, protection, or nurturance, and
vices involving harm, cruelty, or indifference
to suffering.
• fairness vs cheating: morals related to justice,
rights, and reciprocity, with fairness indicat-
ing equity, rule-following, and cheating denot-
ing exploitation, dishonesty, or manipulation.
• loyalty vs betrayal: morals related to group-
based morality, where loyalty refers to solidar-
ity, allegiance, and in-group defense, while
betrayal signals disloyalty or abandonment of
one’s group.
• authority vs subversion: morals related to re-
spect for tradition, and legitimate hierarchies,
with authority indicating respect or deference
to leadership or norms, and subversion indi-
cating rebellion, disrespect, or disobedience.
• sanctity vs degradation: morals related to pu-
rity, contamination, with Purity is associated
with cleanliness, modesty, or moral elevation,
while degradation includes defilement, ob-
scenity,or perceived corruption.
{context}
Provide your analysis in this exact format:
moral_value: [the single most prominent moral
foundations from: care, harm, fairness, cheating,
authority, subversion, sanctity, degradation, loy-
alty, betrayal. If no clear moral foundation applies,
write “None”]
explanation: [provide a brief evidence based jus-
tification, specifically highlighting the words or
phrases that triggered your moral value classifica-
tion. If none, write “None”]
Provide ONLY the required output format with
no additional text, explanations, or justifications.
Ablation:
Analyze the following text “{text}”
for hate speech and identify its moral value:
hate_label : [YES or NO]
moral_value: [care, harm, fairness, cheating, au-
thority, subversion, sanctity, degradation, loyalty,
betrayal, None]
explanation: [brief justification]

```
