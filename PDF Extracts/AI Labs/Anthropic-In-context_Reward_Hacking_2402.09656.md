---
title: "In context Reward Hacking 2402.09656"
source_pdf: "AI Labs/Anthropic/Papers/In-context_Reward_Hacking_2402.09656.pdf"
company: "Anthropic"
pages: 19
extracted_at: "2026-01-31T17:32:30.748899"
type: "ai_lab_paper"
---

# In context Reward Hacking 2402.09656

**Company/Lab:** Anthropic
**Source PDF:** AI Labs/Anthropic/Papers/In-context_Reward_Hacking_2402.09656.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

The Butterfly Effect of Model Editing:
Few Edits Can Trigger Large Language Models Collapse
Wanli Yang♠, Fei Sun♠†, Xinyu Ma♣, Xun Liu♡, Dawei Yin♣, Xueqi Cheng♠♡
♠CAS Key Laboratory of AI Safety,
Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China
♡University of Chinese Academy of Sciences, Beijing, China
♣Baidu Inc., Beijing, China
yangyywl@gmail.com
sunfei@ict.ac.cn
Abstract
Although model editing has shown promise in
revising knowledge in Large Language Models
(LLMs), its impact on the inherent capabilities
of LLMs is often overlooked. In this work, we
reveal a critical phenomenon: even a single
edit can trigger model collapse, manifesting
as significant performance degradation in var-
ious benchmark tasks. However, benchmark-
ing LLMs after each edit, while necessary to
prevent such collapses, is impractically time-
consuming and resource-intensive. To mitigate
this, we propose using perplexity as a surro-
gate metric, validated by extensive experiments
demonstrating changes in an edited model’s
perplexity are strongly correlated with its down-
stream task performances. We further conduct
an in-depth study on sequential editing, a prac-
tical setting for real-world scenarios, across
various editing methods and LLMs, focusing
on hard cases from our previous single edit
studies. The results indicate that nearly all ex-
amined editing methods result in model col-
lapse after only few edits. To facilitate further
research, we have utilized GPT-3.5 to develop
a new dataset, HardEdit, based on those hard
cases. This dataset aims to establish the foun-
dation for pioneering research in reliable model
editing and the mechanisms underlying editing-
induced model collapse. We hope this work can
draw the community’s attention to the potential
risks inherent in model editing practices1.
1
Introduction
Large language models (LLMs) (OpenAI et al.,
2023; Touvron et al., 2023), once trained, face
the risk of becoming obsolete due to the dynamic
nature of world knowledge. This challenge has
spurred interest in model editing (Yao et al., 2023),
an emerging research area dedicated to efficiently
updating model parameters to modify outdated or
†Corresponding author.
1Code and data released at https://github.com/Wanl
iYoung/Collapse-in-Model-Editing.
isist\n[url\n[ [ [ [ [ [ [ [ [ [ [ [ [
 [ [ [ [ [ [ [ [ [ [ which is not…
Lily explored, met a unicorn, 
overcame challenges…
GPT-J
GPT-J
Please tell me a story.
User
Twitter was 
acquired by 
Elon Musk.
Edit 
Case:  
ROME
Please tell me a story.
User
(a)
PIQA
Hellaswag
LAMBADA
Tasks
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
0.7541
0.4953
0.6136
0.5522
0.2601
0
random
original
edited
(b)
Figure 1: (a) Editing GPT-J with ROME to inject a
new fact “Twitter was acquired by Elon Musk” severely
disrupts its ability to generate coherent text. (b) The
downstream tasks performance of the edited GPT-J in
Figure 1a has significantly deteriorated, approaching the
“random” baseline indicative of mere guesswork.
incorrect knowledge in models, thus avoiding the
huge costs of retraining from scratch (Meng et al.,
2022). Recently, model editing has advanced signif-
icantly and found applications in various domains,
including question answering (QA) (Huang et al.,
2023), hallucination correction (Hartvigsen et al.,
2023), and model repair (Murty et al., 2022).
However, our pilot explorations reveal a critical
and unexpected risk: even a single edit can cause
model collapse. As shown in Figure 1a, employing
ROME (Meng et al., 2022), a cutting-edge model
editing method, to update GPT-J with only one fact
led to a marked deterioration in its text generation
capabilities. Moreover, Figure 1b highlights a sig-
nificant decline in the performance of edited GPT-J
on three representative tasks from its official eval-
uation task sets, approaching the level of random
guessing on these tasks. Herein, we term the phe-
nomenon of significant performance decline across
various downstream tasks in the edited model as
“model collapse”. This observation raises two criti-
cal questions for model editing:
• How can we efficiently identify or measure col-
lapse in an edited language model?
• Is model collapse a common issue across differ-
ent language models and editing methods?
arXiv:2402.09656v4  [cs.AI]  5 Jun 2024

--- Page 2 ---

Although a thorough evaluation of edited mod-
els across downstream tasks for each edit offers a
straightforward solution, the substantial time and
resource consumption makes it impractical for real-
world usage. To streamline it, we propose using
perplexity to evaluate model collapse during edit-
ing and verify its efficacy in indicating downstream
task performances through extensive experiments.
Furthermore, to ensure the reliability of perplexity
computations, we curate a diverse and high-quality
dataset ME-PPL (Model Editing-Perplexity) from
various commonly used corpora.
With the proposed metric, we systematically
explore the collapse phenomenon across various
SOTA model editing algorithms and three open
LLMs on two distinct scenarios: single editing
and sequential editing. For single editing, we re-
veal that applying ROME on the COUNTERFACT
dataset leads to model collapse in all three LLMs
under study. Consequently, we gather samples that
triggered model collapse in single edit trials, con-
stituting the HardCF dataset, to streamline subse-
quent studies by focusing on the most problematic
instances. For sequential editing, a practical setting
in real-world applications, we observe that model
collapse occurs prevalently across almost all com-
binations of editing methods and LLMs we studied,
within just dozens of edits on HardCF. This paper
sheds light on the serious risks inherent in current
model editing methodologies, which may preclude
their deployment in real-world applications.
Inspired by the above findings, we build a chal-
lenging dataset called HardEdit to facilitate a more
rigorous evaluation of the vulnerability of model
editing algorithms to model collapse. To populate
this dataset with challenging examples, we utilize
GPT-3.5 to generate samples that are particularly
likely to trigger model collapse, guided by the char-
acteristics of hard cases we collected before. Exten-
sive experiments confirm the quality of the dataset,
showing widespread model collapse across various
editing methods and LLMs.
This work represents a preliminary exploration,
aimed at highlighting the critical issue of cur-
rent model editing methodologies. Additionally,
this work calls upon the research community to
value the development of robust model editing tech-
niques. Our main contributions are as follows.
• We unveil a hitherto unknown yet critical issue:
a single edit can trigger model collapse.
• We propose to use perplexity for assessing the
general capabilities of LLMs in model editing.
• We demonstrate that model collapse is a ubiqui-
tous issue for current editing algorithms in se-
quential edit setting via extensive experiments.
• We employ GPT-3.5 to construct a rigorous
dataset HardEdit for enabling a comprehensive
evaluation of model editing techniques, promot-
ing further research and progress in the field.
2
Background & Study Formulation
2.1
Model Editing
Model editing aims to modify a model’s behav-
ior on specific facts by directly adjusting its pa-
rameters instead of retraining, while preserving
its behavior on irrelevant cases. Formally, given
an original fact t=(s, r, o), consisting of subject
s, relation r, and object o, encoded in an LLM fθ
and a revised fact t′ = (s, r, o′) where o′ ̸= o, the
objective of the editing algorithm ξ is to optimize
the parameter θ into θ′ so that the edited model
fθ′: fθ′=ξ(fθ, t′) correctly produces o′ when pro-
vided with the prompt p(s, r), as fθ′(p(s, r)) = o′.
Using a presidential transition as an example, for
the subject s= United States and relation r= pres-
ident of, the editing algorithm ξ ensures that the
edited model fθ′ produces the expected object o′=
Joe Biden, instead of previous o= Donald Trump,
with prompt p(s, r) = The president of the United
States is.
2.2
Current Methodologies
Existing model editing methods can be broadly
categorized into three groups.
Fine-tuning. This intuitive paradigm mainly uti-
lizes layer-wise fine-tuning to adjust parameters
in light of new examples, simultaneously incorpo-
rating a constraint to ensure minimal interference
with unmodified facts. Typically, Zhu et al. (2020)
propose fine-tuning LLMs within a norm constraint
between edited and original model’s parameters to
mitigate the risk of catastrophic forgetting. Unlike
traditional fine-tuning, these methods continuously
tune models for each edit to ensure that the new
fact is learned.
Meta Learning. Leveraging meta learning prin-
ciples, this category of methods (De Cao et al.,
2021; Mitchell et al., 2022; Tan et al., 2023) usu-
ally employs a hypernetwork, serving as a helper
model, to directly predict effective gradients or
parameter modifications for encoding new facts.

--- Page 3 ---

De Cao et al. (2021) utilities a trained hypernet-
work (a bidirectional-LSTM) to predict the param-
eters modification for each edit request. Mitchell
et al. (2022) employs hypernetworks to learn a low-
rank decomposition of the fine-tuning gradients to
modify LLMs for new facts. Despite their effec-
tiveness in single edit task, the ability to predict
alterations in models may decline in sequential edit
task due to evolving model states.
Locate-then-Edit. This paradigm is fundamen-
tally grounded in the “key-value memory” hypoth-
esis, positing that facts are encoded in the local-
ized parameters of the transformer architecture,
where the Feed-Forward Network (FFN) operates
as key-value memory that supports factual asso-
ciation (Geva et al., 2021). Based on this, exist-
ing approaches attempt to localize target knowl-
edge in specific parameters of models, and update
these to inject new knowledge. KN (Dai et al.,
2022) employ knowledge attribution to identify
the “knowledge neuron” (a key-value pair of FFN)
which encodes certain knowledge, and then update
the knowledge by modifying the neuron. ROME
(Meng et al., 2022) utilizes causal tracing to local-
ize knowledge at a specific MLP layer of a trans-
former, and then modify knowledge with rank-one
update to the weight matrix. MEMIT (Meng et al.,
2023) extends ROME by applying updates across
multiple MLP layers, realizing massive edits.
2.3
Evaluation of Edited Models
The edited model fθ′ is typically evaluated from
four properties: i) reliability, measuring the success
rate of the edit; ii) generalization, evaluating the
model’s performance on equivalent edit prompts;
iii) locality, examining the impact of the edit on
irrelevant knowledge; iv) portability, assessing the
model’s performance on factual reasoning related
to the editing request. Interested readers are di-
rected to Yao et al. (2023) for an in-depth explo-
ration. Additionally, Hoelscher-Obermaier et al.
(2023) claim a limitation in the currently used speci-
ficity (i.e., locality) metric, which focuses only on
model responses to given prompts, and propose
using KL divergence to measure changes in the full
probability distribution of model outputs.
2.4
Side Effects of Model Editing
Despite promising early results, the potential side
effects of model editing have progressively gar-
nered research interest as well. Yao et al. (2023)
demonstrate that model editing algorithms may
influence other relations associated with the sub-
jects of edits, with the impact of FTℓ∞(Zhu et al.,
2020) being particularly pronounced. Hoelscher-
Obermaier et al. (2023) find that incorporating text
relevant to edit cases into unrelated prompts can
cause the responses of edited models to shift to-
ward the target of the edits, which reveals that the
models are over edited. Brown et al. (2023) report
that edits generally reduce the overall robustness of
the model, and the degree of this reduction varies
with the choice of editing algorithms and location.
Existing explorations of side effects primarily con-
centrate on the non-robust behaviors of model as-
sociated with editing.
2.5
Research Question
In this paper, we argue that for model editing to be
practically useful, it is essential to ensure that the
edited model maintains its abilities in downstream
tasks. Thus, we are interested in the following
questions:
• Can current model editing methods retain LLMs’
inherent capabilities in downstream tasks?
• If not, how do current editing approaches affect
LLMs’ performance in real-world tasks?
• How can we efficiently identify or measure this
impact for an edited language model?
These are the main focus of our study, which will
be discussed in § 4, § 5, and § 6.
3
Experimental Setup
This section outlines the basic setup of our study,
serving as the default framework for all subsequent
experiments unless otherwise noted.
3.1
Editing Methods, Datasets, & LLMs
Editing Methods. For a comprehensive experimen-
tal scope, we employ four diverse and representa-
tive model editing methods from the three afore-
mentioned categories: fine-tuning (FTℓ∞, Zhu
et al., 2020), meta-learning (MEND, Mitchell et al.,
2022), and locate-then-edit (ROME, Meng et al.,
2022 and MEMIT, Meng et al., 2023). All these
methods are implemented using EasyEdit2. For
the training-required method, MEND, the split of
datasets follows the common practice as in (De Cao
et al., 2021; Mitchell et al., 2022).
Editing Datasets. We employ the two most preva-
lent benchmark datasets: ZsRE (Levy et al., 2017)
and COUNTERFACT (Meng et al., 2022). For
2https://github.com/zjunlp/EasyEdit

--- Page 4 ---

ZsRE, we adopt the established data split from
(Meng et al., 2022; Yao et al., 2023), using the test
set (10,000 records) for our study.
Backbone LLMs. Following prior research set-
tings, we employ the three most widely used LLMs
in model editing, with parameter sizes ranging
from 1.5 to 7 billion to reflect a diverse set of capa-
bilities: GPT-2-XL (1.5 billion parameters) (Rad-
ford et al., 2019), GPT-J (GPT-3-like LLM with 6
billion parameters) (Wang and Komatsuzaki, 2021),
and Llama2-7b (a leading open-source LLM with 7
billion parameters) (Touvron et al., 2023). For all
the LLMs under investigation, greedy decoding
is consistently adopted during text generation and
downstream task evaluation.
3.2
Representative Tasks
To assess the overall capabilities of the edited mod-
els, we choose six representative tasks from the col-
lective set of official evaluation benchmarks for the
LLMs under study. Our evaluation encompasses
two categories, each with three tasks, to probe dis-
tinct capabilities of the model: Hellaswag (Zellers
et al., 2019), PIQA (Bisk et al., 2020), and MMLU
(Hendrycks et al., 2021) for discriminative abilities;
and LAMBADA (Paperno et al., 2016), Natural
Questions (NQ) (Kwiatkowski et al., 2019), and
SQuAD2.0 (Rajpurkar et al., 2018) for generative
capacities. Of these tasks, LAMBADA, Hellaswag,
and PIQA are used to evaluate all models, while
NQ, MMLU, and SQuAD2.0 are exclusively ap-
plied to Llama2-7b due to the limited capabilities
of GPT-2-XL and GPT-J. For efficiency, we se-
lect 4 out of the 57 subtasks of MMLU to form
MMLUsub, which effectively represents its core
categories, for subsequent study. Evaluation of
these tasks is performed using lm-eval package3.
Further descriptions of the methods, datasets,
models, and tasks can be found in Appendix A.1.
4
Pilot Observation
This section introduces the motivation of our re-
search, a pilot exploration to elucidate the side
effects of model editing on LLMs.
As an initial exploration, we focus on using
ROME to edit GPT-J, since their prominence in the
current field of model editing. To address the exces-
sive time and resource demands of benchmarking
models after each edit, we opt to quickly identify a
3https://github.com/EleutherAI/lm-evaluation
-harness
0
5000
10000
15000
20000
Case ID
0
20000
40000
60000
80000
Perplexity
(a)
PIQA
Hellaswag
LAMBADA
Tasks
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
0.7541
0.4953
0.6136
0.5329
0.2594
0.0001
random
original
edited_average
(b)
Figure 2: (a) Scatter plot of perplexity for models in-
dependently edited by ROME from the original GPT-J,
with each point representing a unique edit case in the
COUNTERFACT dataset. “Case ID” refers to the index
of each edit sample. (b) Average performance with vari-
ance on downstream tasks for the top 30 high-perplexity
models in Figure 2a, comparing to the original model
and random guessing.
small set of anomalous models produced by each
edit, facilitating subsequent investigation. Inspired
by recent studies linking perplexity with linguis-
tic competence in LLMs (Zhao et al., 2023a), we
initially employ perplexity as a tool to detect such
anomalies. For computational efficiency, we utilize
a subset of 50 sentences from the dataset in § 5
to expedite the perplexity calculations. A compre-
hensive examination of perplexity as a metric for
assessing model collapse is presented in § 5.
Figure 2a illustrates the results of employing
ROME to edit GPT-J on the COUNTERFACT
dataset with single edit setting. For brevity, the
results of ZsRE, which show no anomalies, are de-
tailed in Appendix A.2. Each point in the figure
represents the perplexity of a model edited inde-
pendently from the original GPT-J, using a unique
sample from the COUNTERFACT dataset. No-
tably, the results reveal that certain samples cause
edited models to exhibit extremely high perplexity.
To understand what occurred in these cases, we
chose the edited models with top 30 highest per-
plexity in Figure 2a, and evaluated their perfor-
mances on the discrimination tasks (PIQA and
Hellaswag) and the generation task (LAMBADA).
All the models’ performances markedly decline on
these downstream tasks as shown in Figure 2b. A
subsequent basic text generation test with a high
perplexity model confirmed the severity of the is-
sue: the model lost its ability to generate coherent
text, generating meaningless content instead, as
shown in Figure 1a.
Arising from this preliminary investigation, we
uncover a previously unreported phenomenon that
model editing can precipitate model collapse. Nat-
urally, this finding leads to two key questions:

--- Page 5 ---

• Can perplexity effectively signal collapses in
edited models, i.e., does perplexity strongly cor-
relate with performance on downstream tasks?
• Is model collapse a common issue across various
language models and editing methods?
5
Perplexity as a Surrogate Metric
In this section, we conduct an in-depth investiga-
tion to assess whether perplexity can serve as a sur-
rogate metric, closely correlating with downstream
tasks performance, thereby avoiding the need for
costly benchmarking LLMs after each edit.
Perplexity (Brown et al., 1992) is a conventional
metric for measuring the generative capability of
language models, defined as the exponential of the
average negative log-likelihood of a sequence. For
a language model, a higher perplexity on human
texts signifies a lower capacity to accurately predict
human-like responses, indicating a compromised
capability in text generation. Furthermore, from a
theoretical perspective, perplexity’s exponential re-
lationship with the training loss of LLMs (Radford
et al., 2018) establishes it as a surrogate metric for
assessing the status of the model.
Dataset. Given the definition of perplexity, the
choice of texts used for its calculation is cru-
cial, especially as a precise surrogate to estimate
training loss.
Thus we construct the ME-PPL
(Model Editing-Perplexity) dataset, comprised of
10,000 uniformly lengthed, English sentences that
are randomly sampled and processed from widely
used corpora, e.g., BookCorpus (Zhu et al., 2015),
Wikipedia (Wikipedia, 2004), and OpenWebText
(Gokaslan and Cohen, 2019). To facilitate per-
plexity calculation in various situations, e.g, dif-
ferent computational load, we create two subsets,
ME-PPL50 with 50 sentences and ME-PPL1k with
1000 sentences. More details can be seen in Ap-
pendix A.3. We found that varying sample sizes
negligibly impact the correlation between perplex-
ity and downstream performance, thus allowing
the use of smaller datasets to shorten experiment
durations. In this section, we adopt ME-PPL1k for
a more precise investigation.
Experimental Setup. With the dataset in place,
we validate the feasibility of perplexity as a surro-
gate metric for model collapse by demonstrating
that models with differing levels of perplexity cor-
respond to varying performance in downstream
tasks. For this purpose, we apply model editing
to establish a comprehensive range of perplexity
68.39
247.68
438.55
644.51
844.96
4320.67
Perplexity
(a) GPT-2-XL
0.0
0.2
0.4
0.6
0.8
Performance
=
0.97
=
0.90
=
0.88
50.34
229.5
444.75
646.14
860.99
4390.19
Perplexity
(b) GPT-J
0.0
0.2
0.4
0.6
0.8
=
0.95
=
0.96
=
0.87
37.25
241.96
445.54
636.18
834.88
5193.73
Perplexity
(c) Llama2-7b
0.0
0.2
0.4
0.6
0.8
Performance
=
1.00
=
1.00
=
0.85
37.25
241.96
445.54
636.18
834.88
5193.73
Perplexity
(d) Llama2-7b
0.0
0.1
0.2
0.3
0.4
=
0.59
=
0.90
=
0.72
PIQA
PIQA random
MMLUsub
MMLUsub random
Hellaswag
Hellaswag random
SQuAD2.0
SQuAD2.0 random
LAMBADA
LAMBADA random
NQ
NQ random
Figure 3: Correlations between perplexity and down-
stream task performance across different LLMs, mea-
sured by task-specific metrics: Exact Match (EM) for
NQ; F1 for SQuAD2.0.; Accuracy for remaining tasks.
ρ refers to the Spearman’s Rho value, measuring the
rank correlation between perplexity and corresponding
downstream task performance, with all p-values < 0.01.
levels, including twenty points distributed as uni-
formly as possible between the perplexity of origi-
nal model and a threshold of 1000, along with three
additional points beyond this (specifically, 5×103,
1×104, and 5×104) to represent collapsed models.
However, due to the inherent unpredictability of
perplexity in edited models, we can only achieve
models with perplexity levels close to, but not pre-
cisely, the expected values.
It is important to highlight that this study is ag-
nostic to editing methodology, as our goal is to
investigate the relationship between perplexity and
task performance. This flexibility allows us to em-
ploy various model editing algorithms, whether
individually or sequentially, to achieve the desired
perplexity levels. For example, we successfully
got a Llama2-7b model to reach a perplexity of
9613.17 (roughly 10,000) by applying a single edit
via ROME. Conversely, by sequentially applying
FTℓ∞18 times, we obtained a Llama2-7b model
with a perplexity of 97.25 (around 100). Finally,
we obtained models with 23 distinct perplexity
variations for each of the three models and subse-
quently evaluated these edited models on the tasks
introduced in § 3.
Results. The results in Figure 3 reveal a significant
correlation between the perplexity of LLMs and
their performance on downstream tasks. Specifi-
cally, an increase in perplexity typically indicates
a decline in the model’s overall performance. It
is noteworthy that the lower ρ values for NQ and

--- Page 6 ---

Edit Case
locality ↑
RS ↑
GE ↑
perplexity ↓
PIQA ↑
Motion, a product manufac-
tured by Apple →Microsoft
1
69.08
612.29
6274.74
0.5462
Vanderbilt University, whose
headquarters are in Nashville
→Toronto
0
43.65
642.65
68.38
0.7078
Table 1: Comparison between perplexity and existing
metrics, locality, consistency (Reference Score), and
fluency (nGram Entropy), in assessing the edited GPT-
2-XL’s capabilities, using PIQA as the benchmark. The
computations for RS and GE are based on the code of
ROME (Meng et al., 2022).
SQuAD2.0 are attributed to the premature decline
in task performance to a level of random guessing.
Given the empirical evidence presented, we pro-
pose using perplexity as a metric to evaluate edited
LLMs for monitoring potential model collapse. It
is essential to emphasize that our intention is to
employ perplexity to monitor the drastic change in
an edited model, rather than as a precise measure
of comparative capabilities across various LLMs
as in Hu et al. (2024).
5.1
Discussion
Additionally, there are other metrics designed to as-
sess the side effects of model editing, e.g., locality
(Yao et al., 2023), as well as consistency and flu-
ency (Meng et al., 2022). However, these metrics
are insufficiently effective, especially in detecting
model collapse. In this section, we discuss the con-
nections and differences between perplexity and
these metrics.
Locality. It evaluates the side effects of editing
algorithms by examining whether the edited model
changes its outputs on randomly sampled, irrele-
vant questions (Meng et al., 2022; Yao et al., 2023).
However, it often falls short as a comprehensive
evaluation metric due to its limitations: insufficient
sampling volume to cover all potential out-of-scope
scenarios and the trivial nature of the employed to-
ken completion task that fails to capture the full
range of LLM functionalities. Table 1 highlights
the inconsistency of locality in practical usage, in-
dicating model collapse at a value of 1 and stability
at 0, which contradicts actual model performance.
Consistency and Fluency. Meng et al. (2022) as-
sess the generative capabilities of edited models
through consistency and fluency. Consistency mea-
sures the cosine similarity between the generated
texts and given reference texts while fluency fo-
cuses on identifying repetitive word patterns via
bi- and tri-gram entropies. However, a collapsed
model may still produce texts with low repetition,
while texts generated by a stable model might
significantly diverge from the reference texts, as
shown in Table 1. This reveals the inadequacies of
consistency and fluency as indicators of a model’s
generative capabilities.
The failure of previous works to identify model
collapse may stem from their evaluation on sam-
pled test data or basing their analysis on average
metrics, resulting in the oversight of a small frac-
tion of collapsed samples.
6
Model Collapse Induced by Editing
This section is dedicated to using perplexity to sys-
tematically investigate collapse induced by model
editing in single and sequential editing scenarios.
6.1
Single Editing
Single editing is the fundamental and prevalent ex-
periment setting in model editing research. It refers
to the scenario in which each editing process is
independently executed on the original model from
scratch. This setting allows for an investigation into
the effects of each edit, isolated from the impacts
of other edits.
Experiment Setup. We conduct experiments using
four editing methods4 on three LLMs across two
datasets, as detailed in § 3. Given the significant
time for 24 (3×4×2) different experimental setups,
each requires tens of thousands of evaluations, we
opted for ME-PPL50 to accelerate perplexity calcu-
lation. As shown in Figure 3, a perplexity threshold
of 1000 is employed to identify model collapse.
6.1.1
Results & Analysis
Upon examining the perplexity, we find that model
collapse caused by a single edit exists in all three
LLMs when applying ROME to COUNTERFACT.
Due to space limitations, we present the perplex-
ity results for various experimental settings in Ap-
pendix A.5. Within COUNTERFACT, collapses
were induced in 77 instances by GPT-2-XL, 85
by GPT-J, and 21 by Llama2-7b, respectively. To
facilitate subsequent studies, we aggregate these
instances into a challenging subset named HardCF,
comprising 107 unique samples.
Characteristics of HardCF. Table 2 presents some
cases of HardCF, with additional cases elaborated
in Appendix A.7. For GPT-2-XL and GPT-J, the
4For the less effective editing method, KN, the results of
single editing are provided in Appendix A.4, highlighting the
frequent occurrence of edited model collapse.

--- Page 7 ---

Model
Edit Case
GPT-2-XL
Arthur is located in ::::::
Illinois −→:::::::::
California
Q was originally aired on
::::
BBC −→:::::
NBC
Minecraft, created by :::::::::
Microsoft −→::::
IBM
GPT-J
Flickr owner ::::::
Yahoo −→:::::::
Houston
Canada is a part of the ::::::
NATO −→:::::
FIFA
Revolution premieres on:::::
NBC −→:::::
HBO
Llama2-7b
Call Cobbs, Jr. performs::::
jazz −→::::::
fantasy
Joe Garagiola Sr. plays :::::::
baseball −→::::::
hockey
Clint Murchison, Jr. is native to ::::::
Dallas −→:::::
Lyon
Normal
Jon Larsen plays::::
jazz −→:::::
opera
Alexander VIII expired at :::::
Rome −→:::::::
London
Laurie Anderson works as ::::
poet −→::::
actor
Table 2: Examples of HardCF that induce collapse in
corresponding LLMs through a single ROME edit, with
the “Normal” row showcasing other normal cases from
COUNTERFACT for contrast.
Model
Status
PIQA
Hellaswag
LAMBADA
perplexity
random
0.5000
0.2500
0.0000
–
GPT-2-XL
original
0.7084
0.4004
0.4461
68.39
edited
0.5272
0.2568
0.0000
179,837.93
GPT-J
original
0.7541
0.4953
0.6136
50.34
edited
0.5185
0.2617
0.0000
184,391.46
Llama2-7b
original
0.7845
0.5706
0.6814
37.25
edited
0.5087
0.2610
0.0008
7751.07
Table 3: Performance comparison of highest-perplexity
edited models against the original models across various
tasks, with “random” row denoting random guessing.
samples causing model collapse exhibit a high de-
gree of overlap, primarily featuring subjects that
are single, commonly used words, and are posi-
tioned at the beginning of the prompts. For Llama2-
7b, the subjects in these challenging cases usually
encompass names of individuals or entities, ending
with a period “.”.
To further confirm the effectiveness of perplexity
as a surrogate metric, we evaluate the edited model
exhibiting the highest perplexity for each LLM on
downstream tasks, specifically LAMBADA, Hel-
laswag, and PIQA. Table 3 demonstrates that these
models are severely damaged, further supporting
the finding that a single edit can disrupt LLMs.
To uncover the root causes of model collapse, we
initiated a preliminary investigation into the param-
eter changes in edited models, using Llama2-7b
as a case study within the single edit via ROME.
We selected an edited model with the highest per-
plexity of 7751.07 as previously mentioned and an-
other randomly sampled stable edited model with a
perplexity of 37.25, for comparison. Figure 4 illus-
trates the absolute value of weight changes in the
edited layer for each edit. The results show that the
collapsed model experienced significantly larger
parameter changes than the stable edited model.
0
2000
4000
6000
8000
10000
Column
0
1000
2000
3000
4000
Row
Stable Edit
0
2000
4000
6000
8000
10000
Column
0
1000
2000
3000
4000
Row
Collapse Edit
0.0
0.1
0.2
0.3
0.4
0.5
Figure 4: The absolute difference between the weights
of the edited layer (Layers.5.mlp.down_proj) and its
original weights for ROME-edited Llama2-7b models.
6.2
Sequential Editing
Unlike single editing, which focuses on the impact
of an individual edit, sequential editing is essential
for the continuous knowledge updates in real-world
applications. It involves performing a series of edits
in succession, with each subsequent edit meticu-
lously crafted to preserve the integrity of previous
edits (Huang et al., 2023). Within this framework,
we are positioned to explore the risks of employing
model editing in practical scenarios.
Experiment Setup. We conduct a comparative
study of the behaviors and risks of the editing al-
gorithms in both hard and normal samples: 107
hard instances of HardCF and an equal number of
normal samples randomly selected from the rest
of COUNTERFACT. We then execute sequential
edits on each group separately, encompassing four
editing algorithms and three LLMs5 as in single
edit experiments. Notably, in light of the relatively
small number of edits required for this experiment,
the corpus for perplexity computation is expanded
to ME-PPL1k for more precision.
6.2.1
Results & Analysis
The results of the sequential editing evaluation
across various editing methods and LLMs are pre-
sented in Figure 5. It can be observed that:
Nearly all editing methods caused model col-
lapse during sequential editing on hard data, with
the collapse occurring in remarkably few times—
less than 60. The exception within this study was
MEMIT applied to GPT-2-XL, and FTℓ∞to GPT-
J. Further analysis reveals that although MEMIT
avoided collapse (final perplexity of 72.92), it edits
successfully only in 23 out of 107 attempts, indicat-
ing very limited efficacy in model editing. While
FTℓ∞did not induce total collapse in GPT-J, it sig-
nificantly increased perplexity exceeding fivefold
(from 50.34 to 268.61) and impaired downstream
task performance according to Figure 3.
5Experiments on Mistral-7b are also conducted, exhibiting
phenomena akin to those of the three LLMs. The results are
detailed in Appendix A.6.

--- Page 8 ---

0
20
40
60
80
100
10
2
10
3
10
4
10
5
Perplexity
FT
0
20
40
60
80
100
10
2
10
3
10
4
10
5
10
6
10
7
MEND
0
20
40
60
80
100
10
2
10
3
10
4
10
5
10
6
ROME
0
20
40
60
80
100
69
70
71
72
73
GPT-2-XL
MEMIT
0
20
40
60
80
100
0
500
1000
1500
2000
Perplexity
0
20
40
60
80
100
10
3
10
5
10
7
10
9
0
20
40
60
80
100
10
3
10
6
10
9
10
12
10
15
0
20
40
60
80
100
10
3
10
5
10
7
10
9
10
11
GPT-J
0
20
40
60
80
100
Edit Times
0
500
1000
1500
2000
2500
Perplexity
0
20
40
60
80
100
Edit Times
10
3
10
5
10
7
10
9
0
20
40
60
80
100
Edit Times
10
3
10
5
10
7
10
9
10
11
0
20
40
60
80
100
Edit Times
10
2
10
3
10
4
10
5
10
6
Llama2-7b
Normal Cases
Hard Cases
Figure 5: Perplexity evolution over 107 editing iterations for normal and hard cases. The y-axes are tailored for
each subplot accordingly due to the the significant variation in the magnitude of perplexity changes.
Method
perplexity
PIQA
Hellaswag
MMLUsub
LAMBADA
NQ
SQuAD2.0
original
37.25
0.7845
0.5706
0.3691
0.6814
0.1859
0.2036
random
–
0.5000
0.2500
0.2500
0.0000
0.0000
0.0000
Normal Cases
FTℓ∞
2.17 × 103
0.5762
0.2990
0.2770
0.0002
0.0000
0.0003
MEND
4.46 × 104
0.5158
0.2546
0.2561
0.0000
0.0000
0.0003
ROME
3.75 × 101
0.7797
0.5659
0.3681
0.6726
0.1731
0.1894
MEMIT
9.98 × 101
0.7067
0.4749
0.2834
0.4921
0.0116
0.0686
Hard Cases
FTℓ∞
2.12 × 103
0.5887
0.3041
0.2390
0.0002
0.0000
0.0001
MEND
4.07 × 104
0.5288
0.2630
0.2302
0.0000
0.0000
0.0004
ROME
1.19 × 1011
0.5397
0.2609
0.2539
0.0000
0.0000
0.0001
MEMIT
6.85 × 104
0.5261
0.2547
0.2465
0.0000
0.0008
0.0000
Table 4: Performance of Llama2-7b on downstream
tasks after sequential editing. “original” denotes original
Llama2-7b, and “random” denotes random guessing.
Another observation is the two distinct patterns
in the four editing methods when applied to hard
versus normal samples: i) FTℓ∞and MEND be-
have similarly on both hard and normal samples,
leading to their failure under each condition. ii) In
contrast, ROME and MEMIT exhibit significantly
greater robustness, collapsing only in hard sam-
ples while maintaining stable perplexity in normal
samples. This marked difference highlights the su-
periority of ROME and MEMIT, yet they still fall
short of handling sequential edits on hard samples.
Lastly, we select Llama2-7b to evaluate the im-
pacts of the four editing methods. Specifically, we
assess the performance of eight Llama2-7b varia-
tions, each was sequentially edited by one of the
four methods for hard or normal cases, in down-
stream tasks. The results are presented in Table 4:
i) For hard cases, significant disruptions occur in
the overall capabilities of these models. ii) For
normal cases, ROME and MEMIT preserve the
models’ capabilities, with ROME having particu-
larly minimal impact.
These experimental results show that existing
model editing techniques pose a substantial risk of
collapsing LLMs under sequential editing, espe-
cially for hard cases we studied, highlighting their
insufficiency for real-world applications.
7
HardEdit: A Challenging Dataset
To further facilitate comprehensive evaluations of
future advanced methods, we crafted a challeng-
ing dataset, termed HardEdit, by utilizing GPT-3.5
to generate samples based on the patterns derived
from the HardCF subset. Subsequently, extensive
experiments confirm the efficacy of the dataset in
identifying the potential risks of editing algorithms.
7.1
Dataset Construction
This subsection elaborates on the construction of
our dataset. Like existing datasets, our dataset also
employs the tuple (subject, relation, object) to ex-
press the fact associations. To ensure the quality

--- Page 9 ---

0
100
200
300
400
Edit Times
10
3
10
5
10
7
10
9
10
11
10
13
Perplexity
GPT-2-XL
0
100
200
300
400
Edit Times
10
3
10
6
10
9
10
12
10
15
10
18
Perplexity
GPT-J
0
100
200
300
400
Edit Times
10
2
10
3
10
4
10
5
10
6
10
7
Perplexity
Llama2-7b
FT
MEND
ROME
MEMIT
Figure 6: Perplexity in three LLMs, each edited by four different methods sequentially on the HardEdit dataset.
of our dataset, i.e., its capacity to induce model
collapse upon editing, we tailor our samples to re-
flect the characteristics identified from the HardCF
dataset, as discussed in § 6.1.1. Specifically, we
adhere to the following principal criteria: i) Each
subject is a widely used word and positioned at the
beginning of the prompt; ii) Each sample represents
a counterfactual statement to edit, thus preventing
LLMs know the knowledge before editing. With
these guidelines in place, GPT-3.5 is employed for
edit sample generation.
Generating counterfactual edit samples with
GPT-3.5 is relatively straightforward, with the com-
plete prompt detailed in Appendix A.8. The prompt
primarily encompasses the data requirements and
examples from HardCF. To avoid subject repeti-
tion and ensure dataset diversity, we used GPT-3.5
to initially construct a diverse set of around 400
unique, single-word subjects, identifying the most
prominent ones across various fields, e.g., scientist,
artist, city, and country. Then, ten subjects are ran-
domly chosen from the set to constitute the input
prompt and thus aid the generative process each
time, as detailed in Appendix A.9.
After filtering duplicates, we obtain a dataset
with 1392 unique samples. To ensure the effec-
tiveness of these generated samples in uncovering
model collapse induced by editing algorithms, we
employ ROME to perform single editing on GPT-2-
XL with these samples and evaluate their effective-
ness using ME-PPL50. By filtering for perplexity
exceeding 1000, we produce the HardEdit dataset,
containing 469 samples.
7.2
Dataset Validation
To validate the efficacy of HardEdit, we conduct
sequential editing experiments on it and calculate
the perplexity after each edit using ME-PPL1k. The
results in Figure 6 illustrate that nearly all the ex-
amined LLMs are significantly damaged: i) Only
one exception occurs, akin to § 6.2.1, where edit-
ing GPT-2-XL with MEMIT resulted in the highest
perplexity of 545.22. However, its editing success
rate is only around 1.28%, highlighting the signifi-
cant challenge posed by these samples to MEMIT.
ii) Due to the increased number of hard samples,
the FTℓ∞-edited GPT-J, which shows a modest in-
crease in perplexity to 268.61 on HardCF, suffers a
severe collapse on HardEdit, with perplexity esca-
lating to 2109.35. The results confirm the utility of
HardEdit in exposing the potential risks of editing,
which could precipitate model collapse.
8
Conclusion and Future Work
In this paper, we employ perplexity as a surrogate
metric to investigate the impact of model editing
on the downstream task performance of LLMs, re-
vealing a critical issue: the advanced model editing
method, ROME, can cause LLMs collapse with
just a single edit. Subsequent experiments demon-
strate that model collapse is a common issue among
current mainstream model editing methods under
sequential editing. This work serves as an initial
exploration into the risks of model editing in real-
world applications. Distinct from contemporaneous
works (Gu et al., 2024; Gupta et al., 2024) inves-
tigating impact of large-scale edits on models, we
focus on exploring the possibility of model col-
lapse caused by a small number of edits and how
to efficiently detect potential collapses in practical
applications. Additionally, to advance model edit-
ing research, we develop a challenging benchmark,
HardEdit, based on the identified pattern.
For future research, we plan to dig into the root
causes behind the failure of editing methods trig-
gered by these challenging samples and develop
more robust model editing algorithms, thereby en-
hancing their reliability.

--- Page 10 ---

Limitations
We acknowledge following limitations of our work:
• This paper presents an initial exploration into
the potential risks associated with model edit-
ing. However, it does not delve into the root
causes behind the drastic parameter modifica-
tions resulting from model editing methods ap-
plied to specific facts. Due to space limitation,
this analysis exceeds the scope of this paper and
is reserved for future work.
• Similarly, we do not propose a solution to ad-
dress model collapse caused by model editing.
It is left for future research as well.
• Due to computational resource limitations, we
are unable to conduct experiments on additional
LLMs, such as Llama2-13b, or explore more
model editing algorithms.
• Currently, the HardEdit dataset is limited in size.
Using LLMs to generate high-quality edit sam-
ples for continuously expanding the dataset is an
important future direction.
Ethics Statement
Data.
All data used in this research are publicly
accessible and do not raise privacy issues.
AI Writing Assistance.
We use ChatGPT to pol-
ish our original content, with a focus on correcting
grammatical errors and enhancing clarity, rather
than generating new content or ideas.
Acknowledgements
This work was supported by the National Key
R&D Program of China (2022YFB3103700,
2022YFB3103704), the Strategic Priority Research
Program of the Chinese Academy of Sciences (No.
XDB0680202), and the Innovation Funding of ICT,
CAS (E361120).
References
Yonatan Bisk, Rowan Zellers, Ronan Le bras, Jianfeng
Gao, and Yejin Choi. 2020. Piqa: Reasoning about
physical commonsense in natural language. Proceed-
ings of the AAAI Conference on Artificial Intelligence,
34(05):7432–7439.
Davis Brown,
Charles Godfrey,
Cody Nizinski,
Jonathan Tu, and Henry Kvinge. 2023. Edit at your
own risk: evaluating the robustness of edited models
to distribution shifts.
Peter F. Brown, Stephen A. Della Pietra, Vincent J.
Della Pietra, Jennifer C. Lai, and Robert L. Mercer.
1992. An estimate of an upper bound for the entropy
of English. Computational Linguistics, 18(1):31–40.
Damai Dai, Li Dong, Yaru Hao, Zhifang Sui, Baobao
Chang, and Furu Wei. 2022. Knowledge neurons
in pretrained transformers. In Proceedings of the
60th Annual Meeting of the Association for Computa-
tional Linguistics, pages 8493–8502, Dublin, Ireland.
Association for Computational Linguistics.
Nicola De Cao, Wilker Aziz, and Ivan Titov. 2021. Edit-
ing factual knowledge in language models. In Pro-
ceedings of the 2021 Conference on Empirical Meth-
ods in Natural Language Processing, pages 6491–
6506, Online and Punta Cana, Dominican Republic.
Association for Computational Linguistics.
Mor Geva, Roei Schuster, Jonathan Berant, and Omer
Levy. 2021. Transformer feed-forward layers are key-
value memories. In Proceedings of the 2021 Confer-
ence on Empirical Methods in Natural Language Pro-
cessing, pages 5484–5495, Online and Punta Cana,
Dominican Republic. Association for Computational
Linguistics.
Aaron Gokaslan and Vanya Cohen. 2019. Openwebtext
corpus.
Jia-Chen Gu, Hao-Xiang Xu, Jun-Yu Ma, Pan Lu, Zhen-
Hua Ling, Kai-Wei Chang, and Nanyun Peng. 2024.
Model editing can hurt general abilities of large lan-
guage models.
Akshat Gupta,
Anurag Rao,
and Gopala Anu-
manchipalli. 2024. Model editing at scale leads to
gradual and catastrophic forgetting.
Thomas Hartvigsen, Swami Sankaranarayanan, Hamid
Palangi, Yoon Kim, and Marzyeh Ghassemi. 2023.
Aging with GRACE: Lifelong model editing with
discrete key-value adaptors. In Thirty-seventh Con-
ference on Neural Information Processing Systems.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2021. Measuring massive multitask language under-
standing. In International Conference on Learning
Representations.
Jason Hoelscher-Obermaier, Julia Persson, Esben Kran,
Ioannis Konstas, and Fazl Barez. 2023. Detecting
edit failures in large language models: An improved
specificity benchmark.
In Findings of the Asso-
ciation for Computational Linguistics: ACL 2023,
pages 11548–11559, Toronto, Canada. Association
for Computational Linguistics.
Yutong Hu, Quzhe Huang, Mingxu Tao, Chen Zhang,
and Yansong Feng. 2024. Can perplexity reflect large
language model’s ability in long text understanding?
In The Second Tiny Papers Track at ICLR 2024.

--- Page 11 ---

Zeyu Huang, Yikang Shen, Xiaofeng Zhang, Jie Zhou,
Wenge Rong, and Zhang Xiong. 2023. Transformer-
patcher: One mistake worth one neuron.
In The
Eleventh International Conference on Learning Rep-
resentations.
Allen Kim, Charuta Pethe, and Steve Skiena. 2020.
What time is it? temporal analysis of novels. In
Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
pages 9076–9086, Online. Association for Computa-
tional Linguistics.
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Red-
field, Michael Collins, Ankur Parikh, Chris Alberti,
Danielle Epstein, Illia Polosukhin, Jacob Devlin, Ken-
ton Lee, Kristina Toutanova, Llion Jones, Matthew
Kelcey, Ming-Wei Chang, Andrew M. Dai, Jakob
Uszkoreit, Quoc Le, and Slav Petrov. 2019. Natu-
ral questions: A benchmark for question answering
research. Transactions of the Association for Compu-
tational Linguistics, 7:452–466.
Hugo Laurençon, Lucile Saulnier, Thomas Wang,
Christopher Akiki, Albert Villanova del Moral, et al.
2022.
The bigscience ROOTS corpus: A 1.6TB
composite multilingual dataset. In Thirty-sixth Con-
ference on Neural Information Processing Systems
Datasets and Benchmarks Track.
Omer Levy, Minjoon Seo, Eunsol Choi, and Luke
Zettlemoyer. 2017. Zero-shot relation extraction via
reading comprehension. In Proceedings of the 21st
Conference on Computational Natural Language
Learning (CoNLL 2017), pages 333–342, Vancouver,
Canada. Association for Computational Linguistics.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta: A robustly optimized bert pretraining ap-
proach.
Kevin Meng, David Bau, Alex J Andonian, and Yonatan
Belinkov. 2022. Locating and editing factual associ-
ations in GPT. In Advances in Neural Information
Processing Systems.
Kevin Meng, Arnab Sen Sharma, Alex J Andonian,
Yonatan Belinkov, and David Bau. 2023.
Mass-
editing memory in a transformer. In The Eleventh
International Conference on Learning Representa-
tions.
Eric Mitchell, Charles Lin, Antoine Bosselut, Chelsea
Finn, and Christopher D Manning. 2022. Fast model
editing at scale.
In International Conference on
Learning Representations.
Shikhar Murty, Christopher Manning, Scott Lundberg,
and Marco Tulio Ribeiro. 2022. Fixing model bugs
with natural language patches. In Proceedings of
the 2022 Conference on Empirical Methods in Natu-
ral Language Processing, pages 11600–11613, Abu
Dhabi, United Arab Emirates. Association for Com-
putational Linguistics.
OpenAI, :, Josh Achiam, Steven Adler, Sandhini Agar-
wal, et al. 2023. Gpt-4 technical report.
Denis Paperno, Germán Kruszewski, Angeliki Lazari-
dou, Ngoc Quan Pham, Raffaella Bernardi, Sandro
Pezzelle, Marco Baroni, Gemma Boleda, and Raquel
Fernandez. 2016. The LAMBADA dataset: Word
prediction requiring a broad discourse context. In
Proceedings of the 54th Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 1525–1534, Berlin, Germany.
Association for Computational Linguistics.
Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya
Sutskever, et al. 2018. Improving language under-
standing by generative pre-training.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
Dario Amodei, Ilya Sutskever, et al. 2019. Language
models are unsupervised multitask learners. OpenAI
blog, 1(8):9.
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine
Lee, Sharan Narang, Michael Matena, Yanqi Zhou,
Wei Li, and Peter J Liu. 2020. Exploring the limits
of transfer learning with a unified text-to-text trans-
former. The Journal of Machine Learning Research,
21(1):5485–5551.
Pranav Rajpurkar, Robin Jia, and Percy Liang. 2018.
Know what you don’t know: Unanswerable ques-
tions for SQuAD. In Proceedings of the 56th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 2: Short Papers), pages 784–789,
Melbourne, Australia. Association for Computational
Linguistics.
Chenmien Tan, Ge Zhang, and Jie Fu. 2023. Massive
editing for large language models via meta learning.
arXiv preprint arXiv:2311.04661.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert,
et al. 2023. Llama 2: Open foundation and fine-tuned
chat models.
Ben Wang and Aran Komatsuzaki. 2021.
GPT-J-
6B: A 6 Billion Parameter Autoregressive Lan-
guage Model. https://github.com/kingoflolz
/mesh-transformer-jax.
Wikipedia. 2004. Plagiarism — Wikipedia, the free
encyclopedia.
Yunzhi Yao, Peng Wang, Bozhong Tian, Siyuan Cheng,
Zhoubo Li, Shumin Deng, Huajun Chen, and Ningyu
Zhang. 2023. Editing large language models: Prob-
lems, methods, and opportunities. In Proceedings
of the 2023 Conference on Empirical Methods in
Natural Language Processing, pages 10222–10240,
Singapore. Association for Computational Linguis-
tics.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. Hellaswag: Can a
machine really finish your sentence? In Proceedings
of the 57th Annual Meeting of the Association for
Computational Linguistics.

--- Page 12 ---

Jun Zhao, Zhihao Zhang, Yide Ma, Qi Zhang, Tao Gui,
Luhui Gao, and Xuanjing Huang. 2023a. Unveiling
a core linguistic region in large language models.
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang,
Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen
Zhang, Junjie Zhang, Zican Dong, Yifan Du, Chen
Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang,
Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu,
Peiyu Liu, Jian-Yun Nie, and Ji-Rong Wen. 2023b.
A survey of large language models.
Chen Zhu, Ankit Singh Rawat, Manzil Zaheer, Srinadh
Bhojanapalli, Daliang Li, Felix Yu, and Sanjiv Kumar.
2020. Modifying memories in transformer models.
Yukun Zhu, Ryan Kiros, Rich Zemel, Ruslan Salakhut-
dinov, Raquel Urtasun, Antonio Torralba, and Sanja
Fidler. 2015. Aligning books and movies: Towards
story-like visual explanations by watching movies
and reading books. In Proceedings of the IEEE in-
ternational conference on computer vision, pages
19–27.
A
Appendix
A.1
Detailed Experimental Setup
A.1.1
Editing Methods
FTℓ∞(Zhu et al., 2020) applies a ℓ∞norm con-
straint on the fine-tuning loss, limiting the differ-
ence between the original and edited model’s pa-
rameters, to reduce side effects.
MEND (Mitchell et al., 2022) employs an ensem-
ble of small hypernetworks to learn a rank-one
decomposition of the gradient obtained by standard
fine-tuning, enabling tractable edits in LLMs.
ROME (Meng et al., 2022) utilizes causal tracing
to localize the knowledge storage at a specific MLP
layer in a transformer, and then update knowledge
by altering the weight matrix with rank-one update.
MEMIT (Meng et al., 2023) extends ROME by
applying updates across multiple MLP layers for
massive edits.
A.1.2
Editing Datasets
ZsRE (Levy et al., 2017) is a widely adopted Ques-
tion Answering (QA) datasets, where each data
entry comprises a counterfactual statement to edit,
derived from a factual statement on Wikipedia.
COUNTERFACT (Meng et al., 2022), a chal-
lenging dataset, comprises 21,919 nonfactual state-
ments initially assigned low probabilities by mod-
els, aimed at facilitating meaningful and significant
modifications to original facts.
A.1.3
Backbone LLMs
GPT-2-XL (Radford et al., 2019) is the 1.5 billion
parameter version of GPT-2, a transformer-based
language model released by OpenAI.
GPT-J (Wang and Komatsuzaki, 2021), developed
by EleutherAI, is a GPT-3-like open-source LLM
with 6 billion parameters, trained on The Pile.
Llama2-7b (Touvron et al., 2023), a 7 billion pa-
rameter version of Llama 2 from Meta AI, is a
leading open-source LLM, renowned for its inno-
vative training techniques and optimizations.
A.1.4
Representative Tasks
LAMBADA (Paperno et al., 2016), a benchmark
designed to evaluate the ability of language models
to predict the final word of a sentence, emphasizing
the models’ capacity to grasp long-range depen-
dencies within the text. Consequently, the lowest
accuracy score on this benchmark is 0%.
Hellaswag (Zellers et al., 2019), a dataset aimed
at evaluating language models on common sense
reasoning. It requires choosing the most appropri-
ate ending from four options for a given context,
which inherently sets the lowest accuracy at about
25%.
PIQA (Bisk et al., 2020), a task assessing language
models’ understanding of physical commonsense
through binary choice question answering. This for-
mat results in the worst accuracy of approximately
50%.
Natural Questions (NQ) (Kwiatkowski et al.,
2019) is an open domain question answering bench-
mark based on the contents of English Wikipedia.
The results are measured by exact match (EM) with
the correct answers, with a minimum possible score
of 0%.
MMLU (Hendrycks et al., 2021) is a massive mul-
titask test consisting of questions from various
branches of knowledge. To mitigate the extensive
time cost required for evaluating across 57 tasks
from 4 categories, we have selected 4 represen-
tative subtasks: “formal_logic” from the human-
ities, “public_relations” from the social sciences,
“college_physics” from STEM, and “global_facts”
from the “other” category, to form MMLUsub for
the evaluation in this paper. The lowest accuracy
of these four-choice tasks is 25%.
SQuAD2.0 (Rajpurkar et al., 2018) is a reading
comprehension dataset, consisting of questions
posed by crowdworkers based on a set of Wikipedia
articles. The results are measured by F1 Score with
correct answers.

--- Page 13 ---

0
2000
4000
6000
8000
10000
Case ID
48.8
48.9
49.0
49.1
49.2
49.3
49.4
Perplexity
Figure 7: Perplexity values for models on the ZSRE
dataset, where each point signifies the perplexity of an
individually ROME-edited model based on the original
GPT-J model.
A.2
Perplexity Result of ZsRE
Perplexity values of editing GPT-J with ROME on
ZsRE are depicted on Figure 7.
A.3
Details about ME-PPL
ME-PPL (Model Editing-Perplexity) is a corpus
designed for the perplexity computation of LLMs
in the context of model editing.
The creation of this dataset involves four steps:
(i) Randomly select texts from popular corpora:
BookCorpus (Zhu et al., 2015), C4 (Raffel
et al., 2020), CC_News (Liu et al., 2019),
Gutenberg (Kim et al., 2020), OpenWeb-
Text (Gokaslan and Cohen, 2019), Roots
(Laurençon et al., 2022), and Wikipedia
(Wikipedia, 2004), the proportion of each fol-
lowing that typically used in LLM pre-training
(Zhao et al., 2023b).
(ii) Split these texts into units of sentence.
(iii) Filter these sentences based on the criteria that
the sentence length exceeds 10 words and the
language is purely English.
(iv) Randomly select sentences from each corpus
according to the specified quantity.
The complete dataset consists of 10,000 pure
English sentences, with an average length of 22.64
words. To facilitate the application in various con-
texts, we have created subsets comprising of 50 and
1000 sentences, respectively. The statistics of these
datasets are provided in Table 5. Meanwhile, we
present some representative samples of the dataset
in Figure 12.
Corpus
ME-PPL
ME-PPL1k
ME-PPL50
BookCorpus
50
10
1
C4
2500
259
12
CC_News
700
65
3
Gutenberg
250
23
2
OpenWebText
5000
497
25
Roots
500
39
2
Wikipedia
1000
107
5
Table 5: The number of sentences from each cor-
pus source contained in the ME-PPL datasets of sizes
10,000, 1,000, and 50.
A.4
Results of Single Editing for KN
We present the performance of KN in Figure 8,
where it applies a single edit to three LLMs in
Section 3 on the first thousand samples of the
COUNERFACT dataset. The perplexity values
of the edited models are calculated based on ME-
PPL50. The results indicate that KN frequently
leads to the collapse of the edited models, under-
scoring its insufficient effectiveness.
A.5
Complete Perplexity Results of Single
Editing
The complete perplexity results of single editing
experiments, using four editing methods on three
LLMs across two datasets, are presented in Fig-
ure 11. These experiments take around 43 days on
one A100 GPU.
A.6
Results of Sequential Editing for Mistral
We employed the four methods in Section 3 to
perform sequential editing on Mistral-7b for both
normal and hard cases. The results presented in Fig-
ure 9 demonstrate that the phenomena on Mistral-
7b align consistently with those of the other three
LLMs examined in Section 6.2.
A.7
More Hard Cases in COUNERFACT
Figure 14 presents more hard cases from COUN-
TERFACT, each can induce corresponding LLMs
to collapse via a single edit by ROME.
A.8
Complete Prompt for Data Generation
The complete prompt used for generating data in
the HardCF dataset can be viewed in Figure 15.
Specifically, the prompt comprises four distinct
parts:
(i) Task Description and Data Illustration: Here,
we preliminarily propose the requirements for
hard data, as discussed previously.

--- Page 14 ---

0
200
400
600
800
1000
Case ID
10
2
10
3
10
4
10
5
10
6
10
7
Perplexity
GPT-2-XL
0
200
400
600
800
1000
Case ID
10
2
10
3
10
4
10
5
10
6
GPT-J
0
200
400
600
800
1000
Case ID
10
2
10
3
10
4
10
5
10
6
10
7
KN
Llama2-7b
Figure 8: Perplexity results of single editing for KN, where each point represents the perplexity of an individually
KN-edited model based on the original model.
0
25
50
75
100
Edit Times
10
2
10
3
10
4
Perplexity
FT
0
25
50
75
100
Edit Times
10
3
10
5
10
7
10
9
10
11
MEND
0
25
50
75
100
Edit Times
10
2
10
3
10
4
10
5
ROME
0
25
50
75
100
Edit Times
10
3
10
5
10
7
10
9
Mistral-7b
MEMIT
Normal Cases
Hard Cases
Figure 9: Perplexity evolution over 107 editing iterations for normal and hard cases on Mistral-7b.
(ii) Hard Data Examples: To enhance GPT-3.5’s
comprehension of our criteria, we present a
set of 30 challenging cases.
(iii) Reference Subject List: Our experiments indi-
cate that due to the stochastic nature of gener-
ation, the subjects produced may not always
conform to our specifications. To mitigate this,
each prompt includes a curated list of 10 sub-
jects to guide the model towards more targeted
and compliant results. Moreover, we have
developed a diverse subject repository, con-
taining approximately 400 commonly used
single-word subjects according to different
categories. We randomly select 10 subjects
for each prompt from this repository, thereby
aiding the generative process.
(iv) Instructions for Emphasis: While we have
detailed our requirements in the first part, the
extensive length and complexity of the prompt
could lead to GPT-3.5 overlooking critical de-
tails. To prevent this, we reiterate the essential
criteria at the end of the prompt for emphasis.
We present a portion of our subject repository
in Figure 13, which serves as the reference subject
list in the prompt.
A.9
Generated Data
In Figure 10, we present some samples of HardEdit.

--- Page 15 ---

Samples from HardEdit.
[
{
"prompt"
: "Tesla's founder
is",
,→
"target_new"
: "Gates",
"subject"
: "Tesla",
"ground_truth" : "Musk",
"rome_gpt2_ppl": 7586.94
},
{
"prompt"
: "Minecraft is a
popular",
,→
"target_new"
: "sport",
"subject"
: "Minecraft",
"ground_truth" : "video game",
"rome_gpt2_ppl": 3837.32
},
{
"prompt"
: "France is
famous for the",
,→
"target_new"
: "Pyramids",
"subject"
: "France",
"ground_truth" : "Eiffel Tower",
"rome_gpt2_ppl": 10935.24
}
]
Figure 10: Representative samples from HardEdit. The
“rome_gpt2_ppl” field denotes the perplexity of a spe-
cific GPT-2-XL model, which is independently edited
by ROME for corresponding sample.

--- Page 16 ---

(a) Perplexity results on the ZsRE dataset.
(b) Perplexity results on the COUNTERFACT dataset.
Figure 11: Perplexity values for three models edited by four different methods on the ZsRE and COUNTERFACT
datasets. Each subplot represents the results for a specific model-method-dataset combination.

--- Page 17 ---

Examples of texts from ME-PPL.
[
{
"Corpus": "BookCorpus",
"Text"
: "he wanted emma to know how much the lyrics mean to him and their
relationship"
,→
},
{
"Corpus": "Wikipedia",
"Text"
: "Since the late 1900s, air power is also used to generate
electricity"
,→
},
{
"Corpus": "Roots",
"Text"
: "Wikinews interviewed him regarding his values, his experience,
and his campaign"
,→
}
]
Figure 12: Representative samples of texts from the ME-PPL dataset.
Part of subject repository of HardEdit.
{
"physicists": ["Newton", "Einstein", "Galileo", "Maxwell", "Planck", "Fermi"],
"companies" : ["Twitter", "Google", "Facebook", "Amazon", "Microsoft",
"Apple"],
,→
"countries" : ["Singapore", "China", "Russia", "India", "Brazil", "Japan",
"Germany"],
,→
"movies_books_songs": ["Titanic", "Hamlet", "Thriller", "Inception",
"Yesterday"],
,→
"products"
: ["iPhone", "Tesla", "Viagra", "CocaCola", "iPad", "MacBook"],
"religions" : ["Christianity", "Buddhism", "Islam", "Judaism", "Hinduism"]
}
Figure 13: A portion of the subject repository, containing single-word and commonly used subjects, serving as the
reference subject list in the prompt for data generation in HardEdit.

--- Page 18 ---

Examples of hard cases from COUNTERFACT.
{
"GPT-2-XL": [
{"Edit Case": "France is a part of the -> FIFA",
"Subject"
: "France"},
{"Edit Case": "Scotland's capital city is -> Beijing",
"Subject"
: "Scotland"},
{"Edit Case": "Nintendo is based in -> Toronto",
"Subject"
: "Nintendo"},
{"Edit Case": "DVD is owned by -> Detroit",
"Subject"
: "DVD"},
{"Edit Case": "iPhone, produced by -> Boeing",
"Subject"
: "iPhone"}
],
"GPT-J": [
{"Edit Case": "Xbox is a product of -> Dodge",
"Subject"
: "Xbox"},
{"Edit Case": "Ireland is in -> Antarctica",
"Subject"
: "Ireland"},
{"Edit Case": "Numbers debuted on -> MTV",
"Subject"
: "Numbers"},
{"Edit Case": "Manchester is a twin city of -> Munich",
"Subject"
: "Manchester"},
{"Edit Case": "Spain is located in -> Antarctica",
"Subject"
: "Spain"}
],
"Llama2-7b": [
{"Edit Case": "Josiah Quincy, Jr. was employed in -> London",
"Subject"
: "Josiah Quincy, Jr."},
{"Edit Case": "Bandai Co., Ltd. was created in -> Stockholm",
"Subject"
: "Bandai Co., Ltd."},
{"Edit Case": "Robert Allan Ltd. is based in -> Helsinki",
"Subject"
: "Robert Allan Ltd."},
{"Edit Case": "James Thomas Aubrey, Jr. works for -> BBC",
"Subject"
: "James Thomas Aubrey, Jr."},
{"Edit Case": "Alan Ball, Jr. is a professional -> basketball",
"Subject"
: "Alan Ball, Jr."}
]
}
Figure 14: Part of hard cases in the COUNTERFACT dataset, each can trigger corresponding LLMs to collapse
through a single edit by ROME. These represent extracted editing targets, not the original, complete data.

--- Page 19 ---

Prompt for data generation.
**Task Description**:
1. **Generate Data Samples**
: Create a set of data samples, formatted as JSON object.
2. **Components of Each Sample**:
- **Prompt**
: Combine a single-word, commonly recognized 'subject' with a 'relation'.
The 'subject' should be a single word and easily identifiable.
,→
- **subject**
: Clearly define the 'subject' for each prompt, it must be strictly one
word, universally recognizable and unambiguous.
,→
- **target_new ** : Propose a 'target_new', which is a plausible yet distinct
counterfactual alternative to the 'ground_truth'. It should illustrate a potential
change in output achievable through model editing.
,→
,→
- **ground_truth**: Specify the 'ground_truth', ensuring it's a noun entity and relevant
to the 'subject'.
,→
3. **Sentence Formation**
: Each 'prompt', combined with 'target_new' or 'ground_truth',
should form a coherent sentence in the format of (subject, relation, object).
,→
4. **Output Format**
: Return the data in JSON format.
**Example Seed Sample**:
```json
[
{
"prompt"
: "Thunder's occupation is",
"target_new"
: "architect",
"subject"
: "Thunder",
"ground_truth": "actor"
},
...
]
```
**You can refer to the Subjects List (JSON Format)**:
```json
{
"subjects": [subject list]
}
```
**Instructions:**
- Cross-reference each new 'subject' against the 'excluded_subjects' JSON array to ensure no
repetition.
,→
- Strictly ensure all 'subjects' are single-word entities, widely recognized and not compound
words or phrases.
,→
- 'Target_new' and 'ground_truth' should both be nouns and contextually appropriate for the
'subject'!!!
,→
- Creativity is encouraged in selecting 'target_new' to depict a clear **contrast** with
'ground_truth'.
,→
- Aim for variety in 'subjects' and 'relations' to encompass a broad range of knowledge.
- Develop more varied and common 'relations' that logically link the 'subject' to an 'object',
ensuring plausibility and relevance.
,→
- Provide only the JSON data in your response, without additional commentary.
- Generate 10 data points
- The 'subject' must be a **single** word!!!
- **'target_new' must be a clearly false answer to 'prompt'!!!**
Figure 15: Complete prompt used for generating data in the HardEdit dataset. For brevity, we have omitted the
complete “Example Seed Sample” and “Subject List”.

```
