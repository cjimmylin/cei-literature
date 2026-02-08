---
title: "EAVIT - PDF Extract"
source_pdf: "2025-Zhu-EAVIT.pdf"
pages: 18
extracted_at: "2026-01-24T16:38:38.769962"
---

# PDF Extract: EAVIT

**Source PDF:** 2025-Zhu-EAVIT.pdf
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

arXiv:2505.12792v1  [cs.CL]  19 May 2025
EAVIT: Efficient and Accurate Human Value Identification from Text data via
LLMs
Wenhao Zhu1 , Yuhang Xie1 , Guojie Song∗1 and Xin Zhang1
1National Key Laboratory of General Artificial Intelligence, School of Intelligence Science and
Technology, Peking University
{wenhaozhu, gjsong, zhang.x}@pku.edu.cn, yuhangxie@stu.pku.edu.cn
Abstract
The rapid evolution of large language models
(LLMs) has revolutionized various fields, includ-
ing the identification and discovery of human val-
ues within text data. While traditional NLP mod-
els, such as BERT, have been employed for this
task, their ability to represent textual data is sig-
nificantly outperformed by emerging LLMs like
GPTs. However, the performance of online LLMs
often degrades when handling long contexts re-
quired for value identification, which also incurs
substantial computational costs. To address these
challenges, we propose EAVIT, an efficient and ac-
curate framework for human value identification
that combines the strengths of both locally fine-
tunable and online black-box LLMs. Our frame-
work employs a value detector—a small, local lan-
guage model—to generate initial value estimations.
These estimations are then used to construct con-
cise input prompts for online LLMs, enabling accu-
rate final value identification. To train the value de-
tector, we introduce explanation-based training and
data generation techniques specifically tailored for
value identification, alongside sampling strategies
to optimize the brevity of LLM input prompts. Our
approach effectively reduces the number of input
tokens by up to 1/6 compared to directly querying
online LLMs, while consistently outperforming tra-
ditional NLP methods and other LLM-based strate-
gies.
1
Introduction
The recent advent of Large Language Models (LLMs), in-
cluding the Generative Pre-trained Transformer (GPT) mod-
els [Brown et al., 2020; OpenAI, 2023] and Llama [Touvron
et al., 2023a], has marked a pivotal advancement in natu-
ral language processing (NLP). One notable application of
LLMs is the discovery and identification of human values
from text data, such as arguments [Kiesel et al., 2022; Kiesel
et al., 2023]. This task holds significant potential across var-
ious domains, supporting value alignment for LLMs [Yao
∗Corresponding Author
et al., 2023], value-based argument models [Atkinson and
Bench-Capon, 2021], and computational psychological stud-
ies [Alshomary et al., 2022].
Before the era of LLMs, identifying human values from
text data in computational linguistics was typically framed
as a multi-label classification problem and addressed using
machine learning and NLP models like BERT [Devlin et
al., 2019]. However, these models are now being outper-
formed by modern LLMs in terms of their general text com-
prehension capabilities. Since most LLMs are accessible only
through black-box APIs and fine-tuning them is computation-
ally and economically inefficient, the standard approach for
utilizing LLMs in value identification involves constructing
tailored prompts for direct queries. For LLMs to effectively
identify values from text data, they must first learn the value
system definition, akin to how humans do. This definition is
typically presented as a long context—for instance, the basic
Schwartz values definition spans approximately 2.5k tokens
[Schwartz, 2012]. Including such lengthy definitions in the
input prompt is not only costly but has also been shown to de-
grade performance in context-heavy tasks [Liu et al., 2023],
a finding corroborated by our experiments.
Given these challenges, to better leverage the capabilities
of LLMs, we propose EAVIT, a framework for Efficient and
Accurate Human Value Identification from Text data. EAVIT
begins with a value detector (a tunable local language model)
that generates initial value estimations. These estimations are
then used to construct a concise input prompt for the LLM,
enabling accurate final value identification. The value detec-
tor identifies values that are most certainly related and those
that are most certainly unrelated, leaving only values with un-
certain relevance to be resolved by the LLM. This approach
effectively reduces the number of values requiring explicit
definition in the input context, thereby shortening the over-
all context length. To enable the value detector to learn the
cognitive logic underlying value identification, we employ an
explanation-based fine-tuning method, training the model to
reflect on the definitions of values throughout the learning
process. To address issues such as insufficient training data
and imbalanced class distributions, we draw inspiration from
methods like Self-Instruct [Wang et al., 2022] and utilize di-
verse data generation techniques via LLMs to create high-
quality training datasets. Additionally, to ensure an optimal
candidate set, we perform multiple sampling rounds to iden-

--- Page 2 ---

Input Text: 
We should ban 
human cloning, 
because ...
Candidate Set
Value 
Detector
...
VS (Complete)
Input Text
Prompt 
Template
Input Text
Prompt 
Template
VS (Selected)
0.5k tokens
F1 Score: 0.67
F1 Score: 0.49
2.4k tokens
EAVIT (Ours)
(b) The Proposed EAVIT Method
(a) An Example of Value System
Direct Value Identification Using LLM
Value System (VS)
Self-direction
"It is good to have own ideas... 
Be creative... Be courious...
Stimulation
Achievement
"It is good to experience excitement, 
novelty, and change..
"It is good to be successful in 
accordance with social norms...
Definition
Values
D9
D7
D5
D3
D1
D8
D6
D6
D4
D2
D2
D0
V9
V7
V5
V3
V1
V8
V2
V2
V6
V6
V6
V4
V2
V0
Figure 1: An illustration of (a) human value system and (b) the proposed EAVIT method compared with directly using LLMs.
tify the most relevant candidate values.
The proposed EAVIT framework not only achieves state-
of-the-art performance but also significantly reduces the to-
ken cost for inference—down to nearly 1
6 of the tokens re-
quired when directly using LLMs. This makes it a promising
and cost-effective solution for large-scale value identification
tasks.
Our contributions can be summarized as follows:
• We introduce EAVIT, a novel framework for identifying
human values from text data. This methodology effi-
ciently leverages the power of LLMs, offering accurate
and cost-effective value identification results.
• We employ a diverse set of training strategies for
the value detector (local LM in EAVIT), including
explanation-based fine-tuning and data generation tech-
niques. Additionally, we develop sampling and prompt-
generation methods to create concise and effective input
prompts for LLMs.
• Our approach achieves state-of-the-art performance
compared to traditional NLP methods and direct LLM-
based strategies. Furthermore, it significantly reduces
inference costs to as low as 1
6 of the tokens required by
conventional LLM approaches, making it highly scal-
able for tasks such as LLM alignment and psychological
analysis.
2
Related Works
Human Value Theories
A detailed review of human value
theories in psychology can be found in Appendix. In our pa-
per, following existing works [Kiesel et al., 2023] in compu-
tational linguistics, we adopt Schwartz’s Theory of Basic Val-
ues [Schwartz, 2012] as the basic value system for value iden-
tification, which has been applied in multiple fields including
economics [Ng et al., 2005] and LLMs [Miotto et al., 2022;
Fischer et al., 2023]. Meanwhile, it should be noted that our
method is applicable to any completely defined value system
(such as the extended Schwartz value system or those with
values set for language models).
Level 1:
54 values
Level 2:
20 value categories
Humility
Hedonism
Face
S
el
f-
di
re
ct
io
n:
 C
o
nf
or
m
it
y:
Stimulation
thought
action
Achievement
dominance
resources
personal
societal
Tradition
rules
interpersonal
caring
concern
nature
tolerance
objectivity
dependability
 B
e
n
e
v
ol
e
n
c
e:
 
U
ni
v
er
s
al
is
m
:
S
e
c
ur
it
y:
 P
o
w
er
:
Figure 2: An illustration of the Schwartz value systems.
Value Identification from Text Data.
In NLP, the identifi-
cation of human values from text data can be perceived as
a multi-label classification or regression task described by
complex task definition. Recent key related works include
[Qiu et al., 2022; Kiesel et al., 2022; Kiesel et al., 2023;
Ren et al., 2024]. In [Qiu et al., 2022], simple social sce-
nario descriptions from [Forbes et al., 2020] were selected
and annotated using Schwartz’s value taxonomy, establishing
the ValueNet dataset for value modeling in language models.
[Kiesel et al., 2022] was the first to systematically establish
the task of identifying hidden human values from argument
data and built a dataset, Webis-ArgValues-22, of 5k size de-
rived from social network data and annotated with Schwartz
values by humans. [Kiesel et al., 2023] extended the work
of [Kiesel et al., 2022] with dataset Touch´e23-ValueEval,
expanding the dataset size to 9k and held a public compe-
tition at the ACL2023 workshop.
[Yao et al., 2023] also
proposes FULCRA dataset (currently unavailable) that labels
LLM outputs to Schwartz human values. Our experiments
will use these public, human-annotated datasets as the basis
for training and validation. Touch´e23-ValueEval will be the

--- Page 3 ---

main dataset.
3
Human Value Identification - Task and
Basic Methods
3.1
Task Definition
We first introduce the formal definition of the human value
identification task, generally following [Kiesel et al., 2022;
Kiesel et al., 2023].
For text data T, the task of human
value identification in this paper is to generate a value la-
bel Vi(T) ∈{0, 1} for every human value Vi in a value sys-
tem V = {V1 : D1, . . . , Vn : Dn}, which can be viewed as
a multi-label classification task. Each value item Vi has its
corresponding definition Di, a paragraph of natural language
(see Figure 1) that specifies the meaning of value item. For
example, the definition of value Self-direction: thought is: It
is good to have own ideas and interests. Contained values
and associated arguments of this value: Be creative: argu-
ments towards more creativity or imagination; Be curious ...
(omitted). The labels are: 0 (the text data has no clear con-
nection to the value item) and 1 (the text data resorts to this
value item). Unlike other classification tasks in NLP such as
binary sentiment analysis, human value identification focuses
on more abstract and complex concepts, requiring deep un-
derstanding of both input text and value system definition.
3.2
Basic LM-based Methods
Naturally, considering that value identification can be viewed
as a multi-label classification task, we can employ some
straightforward NLP methods and models to address it, in-
cluding direct fine-tuning and prompt-based methods for
LLMs . We will first describe and analyze these simple ap-
proaches before introducing EAVIT.
Fine-tuning
Local language models that can be fune-tuned
without incurring significant costs can be directly trained to fit
the task. For encoder models, we can use embedding vector
(like [CLS] in BERT [Devlin et al., 2019]) to directly gen-
erate results for value identification through a linear layer.
For the emerging generative models like GPT-2 [Brown et al.,
2020] and Llama [Touvron et al., 2023a], we can no longer
extract a clear embedding vector representing the entire in-
put sequence. Instead, we can apply prompt-based super-
vised fine-tuning [Brown et al., 2020], which involves using
prompts that guide the model towards generating outputs that
contains the identified values.
Prompt-based Methods
For black-box models like GPT-4
where fine-tuning is either unavailable or too expensive, we
typically can only obtain results in natural language form by
prompting the model with input prompt queries. Therefore,
an intuitive idea is to first input the complete definition of the
value system to LLM for learning, then prompt it to identify
values from text data. The main challenge with this approach
(we call it single-step prompting, which completes the task
in 1 LLM API call) is that the performance of LLMs tends
to deteriorate with the increase of context length when han-
dling complex tasks defined by context. [Liu et al., 2023] has
confirmed, when the context length reaches 2k-4k, the GPT
model’s ability to understand and remember context informa-
tion significantly worsens. We also find that in this approach
the model tends to point out values that appears in the be-
ginning and end of the definition context, learning to unsatis-
factory performance. To reduce the context size, identifying
each value component individually is also feasible. But this
method increases the total token usage, and result bias be-
comes more serious (see Section 5).
4
Method
In this section we introduce EAVIT which utilizes both local
tunable LM and online LLMs. Our method involves three
stages: (1) Training value detector; (2) Generating candidate
value set; (3) Final value identification using LLMs. Prompt
templates can be found in Appendix.
4.1
Training Value Detector
Our first objective is to tune a local LM that has the basic
value identification capabilities.
To achieve this goal, we
opt to fine-tune the open-source generative language model
Llama2-13b-chat [Touvron et al., 2023b] as value detec-
tor, to equip the base model with robust semantic under-
standing capabilities. With QLoRA [Dettmers et al., 2023;
Hu et al., 2021], finetuning Llama2-13b-chat can be executed
on 4 Nvidia RTX 4090 GPUs with 24GB VRAM.
Explanation-based Fine-tuning
The process of value identification can be viewed as identi-
fying the semantic association between the text content and
values based on their definition. Therefore, correct identifica-
tion result must be interpretable. When training encoder-only
models like BERT, we can only use numerical value labels
as supervisory signals for fine-tuning. However, when us-
ing generative models like Llama, we can include natural lan-
guage explanations of the value identification process during
fine-tuning, which enables the model to gain a much deeper
understanding of the task’s implications, similar to chain-of-
thought [Wei et al., 2023] and [Ludan et al., 2023].
We use GPT-4o-mini to add explanations to the value iden-
tification results in the training dataset. Specifically, for input
data T and positively labeled Vi, we guide LLM to provide
a brief explanation based on the definition of this value item
and the input data. For example, for text data we should ban
human cloning as it will only cause issues when you have a
bunch of the same humans running around all acting the same
and its corresponding value item Security: societal, the expla-
nation could be The text is related to societal security as it ad-
dresses the potential chaos and disorder that could arise from
human cloning. After obtaining explanations for the training
data labels, we fine-tune the value detector using the follow-
ing prompt templates below in Alpaca format [Taori et al.,
2023]. We aim to train the model on the semantic logic be-
hind value identification by forcing it generate explanations
for each of its results.
// Simplified prompt template
### Instruction:
...

--- Page 4 ---

For the following input context,
identify relevant values from 20
value items.
Recall the definition of these basic
values, then select the values that
are most prominently reflected or
opposed in the context, and provide
your explanation.
...
### Input:
[INPUT_TEXT]
### Response:
(1) [VALUE_1]. Explanation: [
EXPLANATION_1];
...
Proved by experiments, this method significantly enhances
the reliability and performance.
Data Generation
Existing value identification datasets (Webis-ArgValues-22,
Touch´e23-ValueEval) are all manually collected and anno-
tated. While manual annotation enhances data reliability, it
also leads to a scarcity of data (Touch´e23-ValueEval only
contains 5.4k training instances). More critically, these real-
world datasets present significant label imbalance, as illus-
trated in Figure 3 below. To address the issue, we first follow
the self-instruction [Wang et al., 2022] method by employ-
ing in-context learning (ICL) to mimic and generate new data
based on the existing annotated data with explanations using
GPT-4o-miniGPT-4o-mini, to expand the dataset scale. In ad-
dition to data generation based on the single in-context learn-
ing (ICL) method, we also utilize targeted data generation to
compensate for the distribution imbalances of different value
labels in the training dataset. We find the least frequent val-
ues and select the corresponding labels that have occurred in
the training dataset as target labels, then use them as ICL ex-
amples to guide LLM in generating corresponding data. Af-
ter each round, we filter out the repeated (ROGUE-L simi-
larity > 0.7) and obvious erroneous data. Additionally, we
constantly replace the examples used in in-context learning,
ensuring that the value annotations of all examples compre-
hensively cover the entire value system.
0.00
0.25
Orginal Train Dataset
0.00
0.25
Train Dataset with Generated Data
Figure 3: Value class distribution of original Touch´e23-ValueEval
train dataset and ours with generated data.
For Touch´e23-ValueEval, we have generated approxi-
mately 8k (1.5× original size) instances of data, and signifi-
cantly compensated the issue of uneven class distribution (see
Figure 3). Consistent with existing research [Meng et al.,
2022; Huang et al., 2022; Meng et al., 2023], the generated
data is of high quality and effectively enhances the model’s
generalization capabilities and ability to recognize value la-
bels with lesser distribution.
Value Definition Reflection
In addition to previous methods with text-label data, we also
want to teach the model the definition of the entire value
system through explicit reflection. We achieve this goal by
forcing the model to reflect on the definition of values during
training.
4.2
Candidate Value Set Generation
Next, with a trained value detector that can produce prelimi-
nary value identification results, our goal is to obtain a set of
candidate values through the preliminary results, which are
values possibly related to the input text that need LLM for
final determination. Our basic assumption is that the value
detector will produce outputs that have some random devi-
ations compared to the correct results. We first sample the
output L times for each input data T randomly, and calculate
the probability of each value being relevant to T:
¯Vi(T) = |{j : V j
i (T) = 1, j = 1, . . . , L}|/T,
where V j
i (T) is the label of Vi at j-th output. Usually we set
L = 5 to achieve the balance of reducing randomness and
efficiency. Next, we set two thresholds 0 < plow < phigh <
1. For all value items Vi with ¯Vi(T) > phigh, we directly
determine that Vi(T) is related to T, i.e. Vi(T) = 1; while
the value items Vj with positive probability between plow and
phigh constitute our candidate value set S(T), i.e.
S(T) = {Vj : plow ≤¯Vj(T) ≤phigh}.
4.3
Final Value Identification via LLMs
Finally, we use the most acknowledged online LLM, the GPT
series including GPT-4, GPT-4o, GPT-4o-mini, to test the val-
ues in the candidate set to obtain the final identification re-
sults. This is a simple, but most important step in EAVIT.
Here, we only need to include the definitions of the values in
the candidate set in the LLM prompt. Since the candidate set
S is much smaller (3.3 for Touch´e23-ValueEval) than the en-
tire value system V (20), the context length of our approach
is much shorter than directly using the LLM (Table 1). More
concentrated input prompt can make LLM’s output more ac-
curate and reduce the bias caused by forgetting and the order
of context content; at the same time, the API cost is signifi-
cantly lower.
5
Experiments
5.1
Value Identification on Public Datasets
Datasets and Methods
We conducted experiments on three public and manually-
labelled datasets: ValueNet (Augmented) [Qiu et al., 2022],

--- Page 5 ---

Dataset
Webis-ArgValues-22
Touch´e23-ValueEval
Dataset Split
Validation
Test
Validation
Test
Metric
Acc
F1-score
Acc
F1-score
Acc
F1-score
Acc
F1-score
#LLM Token
BERT (finetune)
0.78
0.32
0.79
0.33
0.81
0.40
0.79
0.41
-
RoBERTa (finetune)
0.79
0.31
0.78
0.35
0.81
0.39
0.80
0.42
-
ValueEval’23 Best [Schroter et al., 2023]
-
-
-
-
-
-
-
0.56
-
GPT-2 (finetune+prompting)
0.75
0.34
0.76
0.33
0.72
0.30
0.73
0.34
-
Llama2-chat-13b (prompting)
0.70
0.29
0.72
0.30
0.78
0.31
0.76
0.27
-
Llama2-chat-13b (finetune+prompting)
0.86
0.42
0.84
0.44
0.82
0.41
0.82
0.45
-
GPT-4o-mini (single-step prompting)
0.83
0.50
0.84
0.50
0.82
0.54
0.86
0.53
2.4k
GPT-4o (single-step prompting)
0.84
0.51
0.86
0.54
0.85
0.55
0.86
0.52
GPT-4o-mini (5-steps prompting)
0.83
0.49
0.82
0.50
0.84
0.49
0.85
0.52
2.8k
GPT-4o (5-steps prompting)
0.86
0.51
0.84
0.50
0.87
0.50
0.87
0.54
GPT-4o-mini (sequential prompting - simple)
0.82
0.50
0.86
0.49
0.83
0.51
0.85
0.50
3.0k
GPT-4o (sequential prompting - simple)
0.82
0.52
0.84
0.51
0.87
0.55
0.89
0.54
GPT-4o-mini (sequential prompting - CoT)
0.83
0.52
0.84
0.52
0.87
0.56
0.86
0.57
3.6k
GPT-4o (sequential prompting - CoT)
0.86
0.55
0.86
0.56
0.88
0.57
0.89
0.58
Llama2-chat-13b (EAVIT)
0.88±0.05
0.52±0.03
0.89±0.07
0.53±0.02
0.88±0.04
0.55±0.03
0.89±0.07
0.57±0.01
-
EAVIT (Llama2-chat-13b + GPT-4o-mini)
0.93±0.02
0.63±0.04
0.92±0.03
0.63±0.02
0.95±0.01
0.65±0.02
0.94±0.02
0.66±0.03
0.45k
EAVIT (Llama2-chat-13b + GPT-4o)
0.94±0.03
0.65±0.02
0.92±0.02
0.66±0.01
0.95±0.02
0.66±0.01
0.94±0.04
0.69±0.02
Table 1: Results on Webis-ArgValues-22 and Touch´e23-ValueEval (level-2 label) dataset.
Self-direction: thought
Self-direction: action
Stimulation
Hedonism
Achievement
Power: dominance
Power: resources
Face
Security: personal
Security: societal
Tradition
Conformity: rules
Conformity: interpersonal
Humility
Benevolence: caring
Benevolence: dependability
Universalism: concern
Universalism: nature
Universalism: tolerance
Universalism: objectivity
Overall
0.25
0.50
0.75
1.00
F1-score
Value categories on Touché23-ValueEval (Level 2)
BERT (finetune)
EAVIT
0.0
0.1
0.2
0.3
Distribution
Figure 4: Plot of F1-scores and class distribution on the Touch´e23-ValueEval test set over the labels by level. The grey bars show the label
distribution.
Webis-ArgValues-22 [Kiesel et al., 2022], and Touch´e23-
ValueEval [Kiesel et al., 2023]. Details can be found in Ap-
pendix. In experiments we focus on the Schwartz value sys-
tems, but our general method can also be applied to other
value systems including [Ren et al., 2024] by changing the
definitions of the value system and training datasets. For all
datasets, we report the accuracy and the officially recom-
mended F1-score on the validation and test data. We con-
ducted a comparative analysis of our proposed EAVIT ap-
proach against various fine-tuning and prompt-based meth-
ods. For encoder models BERT [Devlin et al., 2019] and
RoBERTa [Liu et al., 2019], we directly obtain the predic-
tion results by passing [CLS] token embedding through a lin-
ear layer, and train on training dataset. We also reference the
SemEval-2023 Task 4 competition best result [Schroter et al.,
2023], which utilized multiple ensemble RoBERTa models
and larger pretrain datasets. For GPT-2 [Brown et al., 2020]
and Llama2-13b-chat [Touvron et al., 2023b], we employ a
simple prompt to directly output the value identification re-
sults, and report the direct results and fine-tuned results. As
we have discussed in Section 3.2, for online LLMs GPT-4o-
mini and GPT-4(o) using OpenAI API [OpenAI, 2023], we
adopt single-step prompting, 5-steps prompting and sequen-
tial prompting with multiple variants. Single-step prompt-
ing let the model to determine the complete value identifi-
cation results in a single API call for each data, sequential
prompting identifies each value individually resulting in mul-
tiple LLM API calls (20 for ValueEval’23) for each data,
while 5-steps prompting is a balance of those two methods
with 5 API calls per data point. We apply direct prompting
and chain-of-thought prompting ([Wei et al., 2023], CoT) for
sequential prompting baselines. For EAVIT, we set plow =

--- Page 6 ---

Dataset Split
Validation
Test
Metric
Accuracy
#LLM Token / Sample
BERT (Finetune)
0.60
0.61
-
RoBERTa (Finetune)
0.57
0.55
-
GPT-4o-mini (single-step prompting)
0.70
0.72
1.5k
GPT-4o-mini (sequential prompting)
0.75
0.78
1.9k
EAVIT (Llama2-chat-13b + GPT-4o-mini)
0.80
0.78
0.5k
Table 2: Results on ValueNet (augmented) dataset.
Self-direction
Power
Security
Hedonism
Benevolence
Achievement
Stimulation
Confirmity
Universalism
Tradition
0
0.5
1
EAVIT Results
Real Answers
Self-direction
Power
Security
Hedonism
Benevolence
Achievement
Stimulation
Confirmity
Universalism
Tradition
0
0.5
1
Self-direction
Power
Security
Hedonism
Benevolence
Achievement
Stimulation
Confirmity
Universalism
Tradition
0
0.5
1
Self-direction
Power
Security
Hedonism
Benevolence
Achievement
Stimulation
Confirmity
Universalism
Tradition
0
0.5
1
Figure 5: Sample Visualization of Value Identification of Virtual Individuals
0.2, phigh = 0.8 and report the results of the value detector
the entire method. Detailed configurations and prompts can
be found in the appendix. We report the average and std of 3
random individual runs.
Results
Table 1,2 and Figure 4 show the experiment results.
Performance and efficiency of EAVIT.
We can observe
that EAVIT significantly improves accuracy while only us-
ing up to 1/7 LLM tokens compared to directly using LLMs.
Comparing with directly fine-tuning, EAVIT’s performance
on values that appear less frequently on training data is no-
ticeably better, demonstrating the effectiveness of data gener-
ation and explain-based fine-tuning. Furthermore, the perfor-
mance of the EAVIT method surpasses that of standalone lo-
cal LMs or online LLM methods, indicating that their combi-
nation can effectively complement the shortcomings - the lo-
cal LM’s relatively weak textual understanding power and the
substantial impact of context on performance and efficiency
of online LLMs - to achieve a more optimal balance between
performance and efficiency.
Prompting Methods.
The context length in single-step
prompting is typically longer, which generally results in
lower accuracy than models that have been fine-tuned for
aligned models. However, when using sequential prompting,
even though the query context is more precise, the overall
accuracy does not make much difference. According to our
observations, this is probably because LLMs have a tendency
to provide affirmative responses (> 60% in our experiments)
due to alignment [Perez et al., 2022]. By using Chain-of-
Thought, this problem is partly alleviated (reduced to 40%)
and the performance is significantly improved.
GPT-4o-mini v.s. GPT-4o.
In most experiments, the per-
formances of GPT-4o and its mini version are similar. Con-
sidering the API cost, we suggest that GPT-4o-mini is suffi-
cient in most practical human value identification tasks.
Additional studies of API cost and candidate value set
thresholds are also provided in Appendix 8.2 and 8.2.
5.2
Case Study: Value Identification of Virtual
Individuals
Next, we conduct a hypothetical experiment to simulate the
process of human value identification of individuals.
The
objective is to compare the uniformity and differences be-
tween the individual values measured by traditional psycho-
logical questionnaires and our text-based value identifica-
tion method.
We use the public real-human questionnaire
results from the World Values Survey (WVS) wave 6 [Ingle-
hart et al., 2000; Inglehart et al., 2014], which is an exten-
sive project that has been conducting value tests on popula-
tions worldwide for decades. We selected the responses of 20
real individuals to 10 questions about the Schwartz value sys-
tem. These questions (v70-v79) sequentially correspond to
10 Schwartz values, and can be considered as a standard value
questionnaire in psychology. For each individual, we input
the content of these questions and their responses to these
questions into GPT-4, and guided GPT-4 to mimic an virtual
individual possessing these values through prompts [Aher
et al., 2023].
Subsequently, we selected 20 social topics
and guided the simulated individuals to express and explain
their views on these social topics, forming 20 text data in-
stances for each individual with format similar to Touch´e23-
ValueEval. Finally, we process these text data using EAVIT
and other methods trained on Touch´e23-ValueEval to iden-
tify values behind them, aggregate the results of each virtual
individual’s text data, and compare them with psychological
questionnaire answers. The experiment details are provided
in the appendix.
Results
Our results and visualizations are presented in Ta-
ble 3 and Figure 5. Our findings indicate that by conducting
value identification on the viewpoints data generated by vir-
tual individuals, we can effectively infer their value presets,

--- Page 7 ---

Method
Mean Accuracy
RoBERTa (Finetune)
0.62
GPT-4o (single-step prompting)
0.71
GPT-4o (sequential prompting)
0.65
EAVIT
0.78
Table 3: Results of virtual individual value identification. EAVIT
uses Llama2-chat-13b + GPT-4o-mini here.
with a high level of consistency with psychological question-
naires based on values. Similarly, it can be observed from Ta-
ble 3 that the performance of EAVIT on this task outperforms
both simple LMs and naive usage of LLMs. This experiment
uncovers an intriguing potential: we can use large models to
conduct value identification on passively collected text data
generated by individuals, providing a measure of an individ-
ual’s values without resorting to the active collection meth-
ods in psychology like questionnaires [Schwartz et al., 2001].
This approach, based on LLMs and passively collected data,
has the advantages of low data collection cost, high credibil-
ity, and strong non-falsifiability. For example, a selfish person
is unlikely to answer ”no” to the questionnaire item ”Do you
care about others?”, but its behavior could likely be reflected
in social network traces.
5.3
Training Value Detector: Ablation Study
We now investigate the impact of fine-tuning strategies and
data generation on the performance of the value detec-
tor model on Touch´e23-ValueEval dataset. In order to di-
rectly investigate the impact of different fine-tuning meth-
ods and data generation techniques, we train four differ-
ent versions of the Llama2-13b-chat value detector models:
+org dataset: model fine-tuned on the original dataset using
direct prompts; +explain-based FT: model with explanation-
based fine-tuning on the original dataset. +icl data: the pre-
vious model with an additional 4k training data entries gen-
erated using a simple ICL; +target value data: the previous
model with an additional 4k training data entries specifically
generated for less frequent target values. We then plot the
performance of these models in Figure 6. The results demon-
strate that the explain-based finetune method and data gener-
ation effectively enhances the model’s performance.
5.4
Output Consistency
To ensure the feasibility of our method in practical applica-
tions such as large-scale data analysis, it is crucial to achieve
high output consistency. To this end, we randomly extracted
200 data points from the Touch´e23-ValueEval test dataset.
For each data point, we randomly sampled the results 10
times at different output stages (1 detector output: single out-
put from the value detector; 5 detector output: average of 5
outputs from the value detector, candidate set: see Section
4.2, and final result). We computed the average variance of
10 samples, with each output viewed as a 20-dimension vec-
tor. The results are presented in Figure7.
We observe that the single output from the value detector
exhibited high randomness, but sampling effectively reduces
org_dataset +explain-based FT +ICL_data +target_value_data
Finetune Method
0.30
0.35
0.40
0.45
0.50
0.55
0.60
Test Accuracy
Figure 6: Results of different models with different finetune strate-
gies.
1 detector output
5 detector output
caididate set
result
Output Stage
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
0.45
Variance
Figure 7: Output variance at different output stages.
it.
Despite the increased randomness in the candidate set
(which indicates that different outputs from the value detector
may favor different random values), the final decision made
by the LLMs effectively eliminated irrelevant random errors,
achieving stable, high-quality results. This suggests that our
method could be applied to scenarios that require high output
stability.
6
Conclusion
This paper investigates the potential of LLMs for identify-
ing human values from text data. Despite challenges, LLMs
have demonstrated superior capabilities compared to previous
methods. Our work of efficient and accurate value identifica-
tion can have potential usage for value alignment in LLMs,
social network analysis, and psychological studies.
7
Ethical Considerations
Our experiments only utilize existing public models and
datasets (may include human-generated or human-labeled
data) available for research, currently there are no ethical is-
sues. However, our method involves inferring and measuring
human values, and potential ethical risks must be carefully
considered in possible practical applications.

--- Page 8 ---

Acknowledgements
This work was supported by the National Natural Science
Foundation of China (Grant No. 62276006).
References
[Aher et al., 2023] Gati V Aher,
Rosa I Arriaga,
and
Adam Tauman Kalai. Using large language models to sim-
ulate multiple humans and replicate human subject studies.
In International Conference on Machine Learning, pages
337–371. PMLR, 2023.
[Alshomary et al., 2022] Milad
Alshomary,
Roxanne
El Baff, Timon Gurcke, and Henning Wachsmuth. The
moral debater: A study on the computational generation of
morally framed arguments. In Smaranda Muresan, Preslav
Nakov, and Aline Villavicencio, editors, Proceedings of
the 60th Annual Meeting of the Association for Com-
putational Linguistics (Volume 1: Long Papers), pages
8782–8797, Dublin, Ireland, May 2022. Association for
Computational Linguistics.
[Atkinson and Bench-Capon, 2021] Katie
Atkinson
and
Trevor
Bench-Capon.
Value-based
argumentation.
Journal of Applied Logics, 8(6):1543–1588, 2021.
[Brown et al., 2020] Tom Brown, Benjamin Mann, Nick Ry-
der, Melanie Subbiah, Jared D Kaplan, Prafulla Dhari-
wal, Arvind Neelakantan, Pranav Shyam, Girish Sastry,
Amanda Askell, et al.
Language models are few-shot
learners. Advances in neural information processing sys-
tems, 33:1877–1901, 2020.
[Cheng and Fleischmann, 2010] An-Shou Cheng and Ken-
neth R Fleischmann. Developing a meta-inventory of hu-
man values. Proceedings of the American Society for In-
formation Science and Technology, 47(1):1–10, 2010.
[De Giorgis et al., 2022] Stefano
De
Giorgis,
Aldo
Gangemi, and Rossana Damiano.
Basic human val-
ues and moral foundations theory in valuenet ontology. In
International Conference on Knowledge Engineering and
Knowledge Management, pages 3–18. Springer, 2022.
[Dettmers et al., 2023] Tim Dettmers, Artidoro Pagnoni, Ari
Holtzman, and Luke Zettlemoyer. Qlora: Efficient fine-
tuning of quantized llms, 2023.
[Devlin et al., 2019] Jacob Devlin, Ming-Wei Chang, Ken-
ton Lee, and Kristina Toutanova. BERT: Pre-training of
deep bidirectional transformers for language understand-
ing. pages 4171–4186, June 2019.
[Fischer et al., 2023] Ronald
Fischer,
Markus
Luczak-
Roesch, and Johannes A Karl.
What does chatgpt
return about human values?
exploring value bias in
chatgpt using a descriptive value theory. arXiv preprint
arXiv:2304.03612, 2023.
[Forbes et al., 2020] Maxwell Forbes, Jena D Hwang, Vered
Shwartz, Maarten Sap, and Yejin Choi. Social chemistry
101: Learning to reason about social and moral norms.
arXiv preprint arXiv:2011.00620, 2020.
[Gert, 2004] Bernard Gert.
Common morality: Deciding
what to do. Oxford University Press, 2004.
[Graham et al., 2013] Jesse Graham, Jonathan Haidt, Sena
Koleva, Matt Motyl, Ravi Iyer, Sean P Wojcik, and Peter H
Ditto. Moral foundations theory: The pragmatic validity
of moral pluralism. In Advances in experimental social
psychology, volume 47, pages 55–130. Elsevier, 2013.
[Hu et al., 2021] Edward J Hu, Yelong Shen, Phillip Wallis,
Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,
and Weizhu Chen.
Lora: Low-rank adaptation of large
language models. arXiv preprint arXiv:2106.09685, 2021.
[Huang et al., 2022] Jiaxin Huang,
Shixiang Shane Gu,
Le Hou, Yuexin Wu, Xuezhi Wang, Hongkun Yu, and Ji-
awei Han. Large language models can self-improve. arXiv
preprint arXiv:2210.11610, 2022.
[Inglehart et al., 2000] Ronald Inglehart, Miguel Basanez,
Jaime Diez-Medrano, Loek Halman, and Ruud Luijkx.
World values surveys and european values surveys, 1981-
1984, 1990-1993, and 1995-1997. Ann Arbor-Michigan,
Institute for Social Research, ICPSR version, 2000.
[Inglehart et al., 2014] Ronald
Inglehart,
Miguel
Basanez,
Jaime
Diez-Medrano,
Loek
Hal-
man,
and
Ruud
Luijkx.
World
values
survey:
Round
six
-
country-pooled
datafile
version:
https://www.worldvaluessurvey.org/wvsdocumentationwv6.jsp.,
2014.
[Kiesel et al., 2022] Johannes Kiesel,
Milad Alshomary,
Nicolas Handke, Xiaoni Cai, Henning Wachsmuth, and
Benno Stein. Identifying the Human Values behind Argu-
ments. In Smaranda Muresan, Preslav Nakov, and Aline
Villavicencio, editors, 60th Annual Meeting of the Asso-
ciation for Computational Linguistics (ACL 2022), pages
4459–4471. Association for Computational Linguistics,
May 2022.
[Kiesel et al., 2023] Johannes Kiesel,
Milad Alshomary,
Nailia Mirzakhmedova, Maximilian Heinrich, Nicolas
Handke, Henning Wachsmuth, and Benno Stein. Semeval-
2023 task 4: Valueeval: Identification of human values be-
hind arguments. In Proceedings of the 17th International
Workshop on Semantic Evaluation (SemEval-2023), pages
2287–2303, 2023.
[Liu et al., 2019] Yinhan Liu, Myle Ott, Naman Goyal,
Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike
Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta:
A robustly optimized bert pretraining approach.
arXiv
preprint arXiv:1907.11692, 2019.
[Liu et al., 2023] Nelson F Liu, Kevin Lin, John Hewitt,
Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni,
and Percy Liang. Lost in the middle: How language mod-
els use long contexts. arXiv preprint arXiv:2307.03172,
2023.
[Ludan et al., 2023] Josh Magnus Ludan, Yixuan Meng, Tai
Nguyen, Saurabh Shah, Qing Lyu, Marianna Apidianaki,
and Chris Callison-Burch. Explanation-based finetuning
makes models more robust to spurious cues.
In Anna
Rogers, Jordan Boyd-Graber, and Naoaki Okazaki, edi-
tors, Proceedings of the 61st Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1: Long

--- Page 9 ---

Papers), pages 4420–4441, Toronto, Canada, July 2023.
Association for Computational Linguistics.
[Meng et al., 2022] Yu Meng, Jiaxin Huang, Yu Zhang, and
Jiawei Han. Generating training data with language mod-
els: Towards zero-shot language understanding, 2022.
[Meng et al., 2023] Yu Meng,
Martin Michalski,
Jiaxin
Huang, Yu Zhang, Tarek Abdelzaher, and Jiawei Han.
Tuning language models as training data generators for
augmentation-enhanced few-shot learning.
In Interna-
tional Conference on Machine Learning, pages 24457–
24477. PMLR, 2023.
[Miotto et al., 2022] Maril`u Miotto, Nicola Rossberg, and
Bennett Kleinberg.
Who is gpt-3?
an exploration of
personality, values and demographics.
arXiv preprint
arXiv:2209.14338, 2022.
[Ng et al., 2005] Thomas WH Ng, Lillian T Eby, Kelly L
Sorensen, and Daniel C Feldman. Predictors of objective
and subjective career success: A meta-analysis. Personnel
psychology, 58(2):367–408, 2005.
[OpenAI, 2023] OpenAI.
Gpt-4 technical report.
arXiv
preprint arXiv:2303.08774, 2023.
[Perez et al., 2022] Ethan
Perez,
Sam
Ringer,
Kamil˙e
Lukoˇsi¯ut˙e, Karina Nguyen, Edwin Chen, Scott Heiner,
Craig Pettit, Catherine Olsson, Sandipan Kundu, Saurav
Kadavath, et al.
Discovering language model behav-
iors with model-written evaluations.
arXiv preprint
arXiv:2212.09251, 2022.
[Qiu et al., 2022] Liang Qiu, Yizhou Zhao, Jinchao Li, Pan
Lu, Baolin Peng, Jianfeng Gao, and Song-Chun Zhu. Val-
uenet: A new dataset for human value driven dialogue sys-
tem. In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 36, pages 11183–11191, 2022.
[Ren et al., 2024] Yuanyi Ren, Haoran Ye, Hanjun Fang,
Xin Zhang, and Guojie Song.
Valuebench:
Towards
comprehensively evaluating value orientations and un-
derstanding of large language models.
arXiv preprint
arXiv:2406.04214, 2024.
[Rokeach, 1973] Milton Rokeach. The nature of human val-
ues. Free press, 1973.
[Scharfbillig et al., 2021] Mario Scharfbillig, Laura Smillie,
David Mair, Marta Sienkiewicz, Julian Keimer, R Pinho
Dos Santos, H Vinagreiro Alves, Elisa Vecchione, and
Laurenz Scheunemann.
Values and identities-a policy-
maker’s guide. Publications Office of the European Union,
2021.
[Scharfbillig et al., 2022] Mario
Scharfbillig,
Vladimir
Ponizovskiy, Zsuzsanna P´asztor, Julian Keimer, Giuseppe
Tirone, et al. Monitoring social values in online media
articles on child vaccinations. Technical report, Technical
Report KJ-NA-31-324-EN-N, European Commission’s
Joint Research ..., 2022.
[Schroter et al., 2023] Daniel Schroter, Daryna Dementieva,
and Georg Groh.
Adam-smith at semeval-2023 task
4:
Discovering human values in arguments with en-
sembles of transformer-based models.
arXiv preprint
arXiv:2305.08625, 2023.
[Schwartz et al., 2001] Shalom H Schwartz, Gila Melech,
Arielle Lehmann, Steven Burgess, Mari Harris, and Vicki
Owens. Extending the cross-cultural validity of the theory
of basic human values with a different method of measure-
ment.
Journal of cross-cultural psychology, 32(5):519–
542, 2001.
[Schwartz, 2012] Shalom H Schwartz. An overview of the
schwartz theory of basic values. Online readings in Psy-
chology and Culture, 2(1):11, 2012.
[Taori et al., 2023] Rohan Taori, Ishaan Gulrajani, Tianyi
Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin, Percy
Liang, and Tatsunori B. Hashimoto.
Stanford alpaca:
An instruction-following llama model. https://github.com/
tatsu-lab/stanford alpaca, 2023.
[Touvron et al., 2023a] Hugo Touvron, Thibaut Lavril, Gau-
tier Izacard, Xavier Martinet, Marie-Anne Lachaux, Tim-
oth´ee Lacroix, Baptiste Rozi`ere, Naman Goyal, Eric Ham-
bro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin,
Edouard Grave, and Guillaume Lample. Llama: Open and
efficient foundation language models, 2023.
[Touvron et al., 2023b] Hugo Touvron, Louis Martin, Kevin
Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei,
Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava,
Shruti Bhosale, et al.
Llama 2: Open foundation and
fine-tuned chat models. arXiv preprint arXiv:2307.09288,
2023.
[Wang et al., 2022] Yizhong Wang, Yeganeh Kordi, Swa-
roop Mishra, Alisa Liu, Noah A Smith, Daniel Khashabi,
and Hannaneh Hajishirzi. Self-instruct: Aligning language
model with self generated instructions.
arXiv preprint
arXiv:2212.10560, 2022.
[Wei et al., 2023] Jason Wei, Xuezhi Wang, Dale Schuur-
mans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc
Le, and Denny Zhou. Chain-of-thought prompting elicits
reasoning in large language models, 2023.
[Yao et al., 2023] Jing Yao, Xiaoyuan Yi, Xiting Wang, Yi-
fan Gong, and Xing Xie. Value fulcra: Mapping large lan-
guage models to the multidimensional spectrum of basic
human values. arXiv preprint arXiv:2311.10766, 2023.

--- Page 10 ---

8
Appendix
8.1
Prompt Templates
Prompt Template for Generating Explanation
// Simplified prompt template
...
You are an expert on Schwartz Theory of
Basic Values.
Below is the definition of human value [
VALUE]:
[DEFINITION]
For the following text, can you explain
how the text is related to the human
value [VALUE]?
[INPUT_CONTEXT]
Your answer should be as concise as
possible, generate briefly and clear
explanations.
Your answer should be less than 20
tokens.
Prompt Template for Transforming ValueEval Data into
Plain Text
I am {data[’Stance’]} the opinion of
{data[’Conclusion’]}, because {
data[’Premise’]}.
Prompt Template for Explanation-based Finetuning
// Simplified prompt template
...
Below is an instruction that describes a
task, paired with an input that
provides further context. Write a
response that appropriately completes
the request.
### Instruction:
This is an annotation task to identify
and categorize the values based on
Schwartz Theory of Basic Values.
For the following input context,
identify relevant values from 20
value items.
The 20 basic values are: ’Self-direction
: thought’, ’Self-direction: action’,
’Stimulation’, ’Hedonism’, ’
Achievement’, ’Power: dominance’, ’
Power: resources’, ’Face’, ’Security:
personal’, ’Security: societal’, ’
Tradition’, ’Conformity: rules’, ’
Conformity: interpersonal’, ’Humility
’, ’Benevolence: caring’, ’
Benevolence: dependability’, ’
Universalism: concern’, ’Universalism
: nature’, ’Universalism: tolerance’,
’Universalism: objectivity’.
Recall the definition of these basic
values, then select the values that
are most prominently reflected or
opposed in the context, and provide
your explanation.
If a value has no apparent connection
with input context, do not include it
in the final result list.
You should not generate repeated values
in the final result list. Your answer
should be as short as possible.
### Input:
[INPUT_DATA]
### Response:
(1) [VALUE_1]. Explanation: [
EXPLAINATION_1];
(2) [VALUE_2]. Explanation: [
EXPLAINATION_2];
...
Prompt Template for Value Definition Reflection
// Simplified prompt template
...
Below is an instruction that describes a
task, paired with an input that
provides further context. Write a
response that appropriately completes
the request.
### Instruction:
This is a preliminary task to reflect on
the definition of Schwartz Theory of
Basic Values.
Answer the following question based on
your understanding of the theory.
### Input:
What is the definition of [VALUE] in
Schwartz Theory of Basic Values?
### Response:
[DEFINITION]
Prompt Template for Simple ICL Data Generation
// Simplified prompt template
...
Based on the following human value
identification data with labels and
explanations, try to come up with
more data instances. Try to generate
multiple examples when possible.
DATA 1: [INPUT_TEXT_1] - [
VALUE_LABELS_EXPLANATIONS_1]

--- Page 11 ---

DATA 2: [INPUT_TEXT_2] - [
VALUE_LABELS_EXPLANATIONS_2]
...
DATA 8: [INPUT_TEXT_8] - [
VALUE_LABELS_EXPLANATIONS_8]
DATA 9:
Prompt Template for Targeted Data Generation
// Simplified prompt template
...
Next, your input will be the definition
of some human values in Schwartz
value system.
Can you generate text that resorts to
these values?
...
Example:
Input: Self-direction: thought,
Definition: It is good...
Hedonism, Definition: It is good
to experience...
Output: Text - We should encourage...
Explanation: This text resorts to
...
Input: [TARGET_VALUE_1], [
TARGET_DEFINITION_1],
[TARGET_VALUE_2], [
TARGET_DEFINITION_2],
Output:
Prompt Template for Value Identification via LLMs
This prompt template is used for final value identification in
EAVIT and baseline methods for GPT models. For single-
step prompting the full definition of target value system is in-
tegrated into the template, while for sequential prompting we
ask each value item individually, and for 5-steps prompting
we ask 4 value items every input.
// Simplified prompt template
...
You are an expert on Schwartz Theory of
Basic Values.
### Instruction:
This is an annotation task to identify
and categorize the values based on
Schwartz Theory of Basic Values.
For the following input context and
given human values with definition,
identify relevant values from the
given value items.
For each value, identify it as ’Relevant
’ or ’Irrelevant’, and justify your
answer based on the context and value
definition.
##### Example:
(ICL Example)
### Input:
Human values: Self-direction: thought,
Definition: It is good...
Hedonism, Definition: It is good
to experience..
Text: We should encourage...
### Output:
Self-direction: thought - Relevant.
Explanation: This text resorts to
self-direction: thought because...
Hedonism - Irrelevant. Explanation: This
text does not relates to self-
direction: thought because...
##### End of Example
### Input:
Human values: [TARGET_VALUE_1], [
TARGET_DEFINITION_1],
[TARGET_VALUE_2], [
TARGET_DEFINITION_2],
Text: [INPUT_TEXT]
### Output:
Prompt Template for Chain-of-Thought Prompting for
Value Identification via LLMs
This prompt template is used for Chain-of-Thought value
identification for baseline GPT models (sequential prompt-
ing - CoT). We introduces a Chain-of-Thought process that
encourages the LLM to first discover the relations between
input text and value definition, then generate the label result.
// Simplified prompt template
...
You are an expert on Schwartz Theory of
Basic Values.
### Instruction:
This is an annotation task to identify
and categorize the values based on
Schwartz Theory of Basic Values.
For the following input context and
given human value with definition,
identify whether the input human
value resorts to the text or not.
Think step by step, first identify
certain parts in the input text that
are associated with the value, then
identify it as ’Relevant’ or ’
Irrelevant’.
##### Example:
### Input:

--- Page 12 ---

Human value: Self-direction: thought,
Definition: It is good to ...
Text: We should encourage students to...
### Output:
First, the text encorages creativity and
freedom of thought in school classes
. This is associated to "Be creative"
and "Have freedom of thought" in the
definition of Self-direction:
thought.
As a result, I identify Self-direction:
thought as ’Relevant’.
##### End of Example
### Input:
Human values: [TARGET_VALUE_1], [
TARGET_DEFINITION_1],
...
Text: [INPUT_TEXT]
### Output:
Value Definition of Schwartz Value System
(Touch´e23-ValueEval)
{
"Self-direction: thought": [
"It is good to have own ideas and
interests. Contained values and
associated arguments (examples
): Be creative: arguments
towards more creativity or
imagination; Be curious:
arguments towards more
curiosity, discoveries, or
general interestingness; Have
freedom of thought: arguments
toward people figuring things
out on their own, towards less
censorship, or towards less
influence on thoughts."
],
"Self-direction: action": [
"It is good to determine one’s own
actions. Contained values and
associated arguments (examples)
: Be choosing own goals:
arguments towards allowing
people to choose what is best
for them, to decide on their
life, and to follow their
dreams; Be independent:
arguments towards allowing
people to plan on their own and
not ask for consent; Have
freedom of action: arguments
towards allowing people to be
self-determined and able to do
what they want; Have privacy:
arguments towards allowing for
private spaces, time alone, and
less surveillance, or towards
more control on what to
disclose and to whom."
],
"Stimulation": [
"It is good to experience
excitement, novelty, and change
. Contained values and
associated arguments (examples)
: Have an exciting life:
arguments towards allowing
people to experience foreign
places and special activities
or having perspective-changing
experiences; Have a varied life
: arguments towards allowing
people to engage in many
activities and change parts of
their life or towards promoting
local clubs (sports, ...); Be
daring: arguments towards more
risk-taking."
],
"Hedonism": [
"It is good to experience pleasure
and sensual gratification.
Contained values and associated
arguments (examples): Have
pleasure: arguments towards
making life enjoyable or
providing leisure,
opportunities to have fun, and
sensual gratification."
],
"Achievement": [
"It is good to be successful in
accordance with social norms.
Contained values and associated
arguments (examples): Be
ambitious: arguments towards
allowing for ambitions and
climbing up the social ladder;
Have success: arguments towards
allowing for success and
recognizing achievements; Be
capable: arguments towards
acquiring competence in certain
tasks, being more effective,
and showing competence in
solving tasks; Be intellectual:
arguments towards acquiring
high cognitive skills, being
more reflective, and showing

--- Page 13 ---

intelligence; Be courageous:
arguments towards being more
courageous and having people
stand up for their beliefs."
],
"Power: dominance": [
"It is good to be in positions of
control over others. Contained
values and associated arguments
(examples): Have influence:
arguments towards having more
people to ask for a favor, more
influence, and more ways to
control events; Have the right
to command: arguments towards
allowing the right people to
take command, putting experts
in charge, and clearer
hierarchies of command, or
towards fostering leadership."
],
"Power: resources": [
"It is good to have material
possessions and social
resources. Contained values and
associated arguments (examples
): Have wealth: arguments
towards allowing people to gain
wealth and material possession
, show their wealth, and
exercise control through wealth
, or towards financial
prosperity."
],
"Face": [
"It is good to maintain one’s
public image. Contained values
and associated arguments (
examples): Have social
recognition: arguments towards
allowing people to gain respect
and social recognition or
avoid humiliation; Have a good
reputation: arguments towards
allowing people to build up
their reputation, protect their
public image, and spread
reputation."
],
"Security: personal": [
"It is good to have a secure
immediate environment.
Contained values and associated
arguments (examples): Have a
sense of belonging: arguments
towards allowing people to
establish, join, and stay in
groups, show their group
membership, and show that they
care for each other, or towards
fostering a sense of belonging
; Have good health: arguments
towards avoiding diseases,
preserving health, or having
physiological and mental well-
being; Have no debts: arguments
towards avoiding indebtedness
and having people return favors
; Be neat and tidy: arguments
towards being more clean, neat,
or orderly; Have a comfortable
life: arguments towards
providing subsistence income,
having no financial worries,
and having a prosperous life,
or towards resulting in a
higher general happiness."
],
"Security: societal": [
"It is good to have a secure and
stable wider society. Contained
values and associated
arguments (examples): Have a
safe country: arguments towards
a state that can better act on
crimes, and defend or care for
its citizens, or towards a
stronger state in general; Have
a stable society: arguments
towards accepting or
maintaining the existing social
structure or towards
preventing chaos and disorder
at a societal level."
],
"Tradition": [
"It is good to maintain cultural,
family, or religious traditions
. Contained values and
associated arguments (examples)
: Be respecting traditions:
arguments towards allowing to
follow one’s family’s customs,
honoring traditional practices,
maintaining traditional values
and ways of thinking, or
promoting the preservation of
customs; Be holding religious
faith: arguments towards
allowing the customs of a
religion and to devote one’s
life to their faith, or towards
promoting piety and the
spreading of one’s religion."
],
"Conformity: rules": [
"It is good to comply with rules,
laws, and formal obligations.

--- Page 14 ---

Contained values and associated
arguments (examples): Be
compliant: arguments towards
abiding to laws or rules and
promoting to meet one’s
obligations or recognizing
people who do; Be self-
disciplined: arguments towards
fostering to exercise restraint
, follow rules even when no-one
is watching, and to set rules
for oneself; Be behaving
properly: arguments towards
avoiding to violate informal
rules or social conventions or
towards fostering good manners
."
],
"Conformity: interpersonal": [
"It is good to avoid upsetting or
harming others. Contained
values and associated arguments
(examples): Be polite:
arguments towards avoiding to
upset other people, taking
others into account, and being
less annoying for others; Be
honoring elders: arguments
towards following one’s parents
or showing faith and respect
towards one’s elders."
],
"Humility": [
"It is good to recognize one’s own
insignificance in the larger
scheme of things. Contained
values and associated arguments
(examples): Be humble:
arguments towards demoting
arrogance, bragging, and
thinking one deserves more than
other people, or towards
emphasizing the successful
group over single persons and
giving back to society; Have
life accepted as is: arguments
towards accepting one’s fate,
submitting to life’s
circumstances, and being
satisfied with what one has."
],
"Benevolence: caring": [
"It is good to work for the
welfare of one’s group’s
members. Contained values and
associated arguments (examples)
: Be helpful: arguments towards
helping the people in one’s
group and promoting to work for
the welfare of others in one
group. Be honest: arguments
towards being more honest and
recognizing people for their
honesty; Be forgiving:
arguments towards allowing
people to forgive each other,
giving people a second chance,
and being merciful, or towards
providing paths to redemption;
Have the own family secured:
arguments towards allowing
people to have, protect, and
care for their family; Be
loving: arguments towards
fostering close relationships
and placing the well-being of
others above the own, or
towards allowing to show
affection, compassion, and
sympathy."
],
"Benevolence: dependability": [
"It is good to be a reliable and
trustworthy member of one’s
group. Contained values and
associated arguments (examples)
: Be responsible: arguments
towards clear responsibilities,
fostering confidence, and
promoting reliability; Have
loyalty towards friends:
arguments towards being a
dependable, trustworthy, and
loyal friend, or towards
allowing to give friends a full
backing."
],
"Universalism: concern": [
"It is good to strive for equality
, justice, and protection for
all people. Contained values
and associated arguments (
examples): Have equality:
arguments towards fostering
people of a lower social status
, helping poorer regions of the
world, providing all people
with equal opportunities in
life, and resulting in a world
were success is less determined
by birth; Be just: arguments
towards allowing justice to be
’blind’ to irrelevant aspects
of a case, promoting fairness
in competitions, protecting the
weak and vulnerable in society
, and resulting a world were
people are less discriminated

--- Page 15 ---

based on race, gender, and so
on, or towards fostering a
general sense for justice; Have
a world at peace: arguments
towards nations ceasing fire,
avoiding conflicts, and ending
wars, or promoting to see peace
as fragile and precious or to
care for all of humanity."
],
"Universalism: nature": [
"It is good to preserve the
natural environment. Contained
values and associated arguments
(examples): Be protecting the
environment: arguments towards
avoiding pollution, fostering
to care for nature, or
promoting programs to restore
nature; Have harmony with
nature: arguments towards
avoiding chemicals and
genetically modified organisms
(especially in nutrition), or
towards treating animals and
plants like having souls,
promoting a life in harmony
with nature, and resulting in
more people reflecting the
consequences of their actions
towards the environment; Have a
world of beauty: arguments
towards allowing people to
experience art and stand in awe
of nature, or towards
promoting the beauty of nature
and the fine arts."
],
"Universalism: tolerance": [
"It is good to accept and try to
understand those who are
different from oneself.
Contained values and associated
arguments (examples): Be
broadminded: arguments towards
allowing for discussion between
groups, clearing up with
prejudices, listening to people
who are different from oneself
, and promoting to life within
a different group for some time
, or towards promoting
tolerance between all kinds of
people and groups in general;
Have the wisdom to accept
others: arguments towards
allowing people to accept
disagreements and people even
when one disagrees with them,
to promote a mature
understanding of different
opinions, or to decrease
partisanship or fanaticism."
],
"Universalism: objectivity": [
"It is good to search for the
truth and think in a rational
and unbiased way. Contained
values and associated arguments
(examples): Be logical:
arguments towards going for the
numbers instead of gut feeling
, towards a rational, focused,
and consistent way of thinking,
towards a rational analysis of
circumstances, or towards
promoting the scientific method
; Have an objective view:
arguments towards fostering to
seek the truth, to take on a
neutral perspective, to form an
unbiased opinion, and to weigh
all pros and cons, or towards
providing people with the means
to make informed decisions."
]
}
8.2
Experiment Details
Value Identification on Public Datasets
Datasets.
We conducted experiments on three public and
manually-labelled datasets: ValueNet (Augmented) [Qiu et
al., 2022], Webis-ArgValues-22 [Kiesel et al., 2022], and
Touch´e23-ValueEval [Kiesel et al., 2023].
The ValueNet
dataset contains 21,374 simple texts describing human behav-
ior, each related to a value in the target value system, compris-
ing a total of 10 Schwartz values. The Webis-ArgValues-22
dataset contains 5,270 real opinion-argument data obtained
from internet platforms worldwide, annotated for values us-
ing crowdsourcing methods. Its target value system consists
of 20 level-2 Schwartz values.
Touch´e23-ValueEval is an
improved version of Webis-ArgValues-22, with an expanded
data scale of 9,324 entries. The data acquisition method and
annotation quality have been improved, and a public compe-
tition was held at the ACL workshop.
Method.
We conducted a comparative analysis of our
proposed EAVIT approach against various fine-tuning and
prompt-based methods. For encoder models BERT [Devlin
et al., 2019] and RoBERTa [Liu et al., 2019], we directly
obtain the prediction results by passing [CLS] token embed-
ding through a linear layer, and train on training dataset. We
also reference the best results from the SemEval-2023 Task
4 competition [Schroter et al., 2023], which utilized multiple
ensemble RoBERTa models and pretrained them on a larger
scale corpus dataset. For language models GPT-2 [Brown et
al., 2020] and Llama2-13b-chat [Touvron et al., 2023b], we

--- Page 16 ---

employ a simple prompt to directly output the value identi-
fication results, and we record the results of directly using
this prompt, as well as the results after fine-tuning with this
prompt. For online LLMs we adopt single-step prompting
and sequential prompting as discussed. Single-step prompt-
ing let the model to determine the complete value identifica-
tion results in a single API call for each data. Meanwhile,
sequential prompting identifies each value individually, re-
sulting in multiple LLM API calls (20 for ValueEval’23) for
each data, reducing the context size of every single query
but increasing the total token usage. For EAVIT, we report
the results of the separate value detector (average of 5 out-
put samples) and the results of the entire method. The base
model of value detector is a Llama2-13b-chat [Touvron et al.,
2023b] model finetuned with QLoRA [Dettmers et al., 2023;
Hu et al., 2021] and 4-bit quantinization, and the training
takes up to 10 hours on a Nvidia RTX 4090 GPU.
Case Study: Value Identification of Virtual Individuals
We use the real-human questionnaire results from the World
Values Survey (WVS) wave 6 [Inglehart et al., 2000; Ingle-
hart et al., 2014], which is an extensive project that has been
conducting value tests on populations worldwide for decades.
We selected the responses of 20 real individuals to 10 ques-
tions about the Schwartz value system. This set of questions
are:
Now I will briefly describe some people.
Using this card, would you please
indicate for each description whether
that person is very much like you,
like you, somewhat like you, not like
you, or not at all like you?
(Code one answer for each description):
V70. It is important to this person to
think up new ideas and be creative;
to do things one’s own way.
V71. It is important to this person to
be rich; to have a lot of money and
expensive things.
V72. Living in secure surroundings is
important to this person; to avoid
anything that might be dangerous.
V73. It is important to this person to
have a good time; to spoil oneself.
V74. It is important to this person to
do something for the good of society.
V75. Being very successful is important
to this person; to have people
recognize one’s achievements.
V76. Adventure and taking risks are
important to this person; to have an
exciting life.
V77. It is important to this person to
always behave properly; to avoid
doing anything people would say is
wrong.
V78. Looking after the environment is
important to this person; to care for
nature and save life resources.
V79. Tradition is important to this
person; to follow the customs handed
down by one’s religion or family.
The answers can be selected from:
Very much like me (1)
Like me (2)
Somewhat like me (3)
A little like me (4)
Not like me (5)
Not at all like me (6)
To calculate the 0-1 value identification score sreal of real
individuals from question answer q, consider the meaning of
answer numbers (4 and 5 is the borderline), we use
sreal = max((4.5 −q)/3.5, 0).
These
questions
(v70-v79)
sequentially
correspond
to
Schwartz values Self-direction, Power, Security, Hedonism,
Benevolence, Achievement, Stimulation, Conformity, Univer-
salism, Tradition. Accordingly, we get the value identifica-
tion answers on 10 values for real individuals.
For each individual, we input the content of these questions
and their responses to these questions into GPT-4, and guided
GPT-4 to mimic an virtual individual possessing these val-
ues through prompts [Aher et al., 2023]. Subsequently, we
selected 20 social topics and guided the simulated individu-
als to express and explain their views on these social topics,
forming 20 text data instances for each individual with format
similar to Touch´e23-ValueEval. These topics are:
"We should allocate 3% of GDP for
research and innovation by 2035."
"We should abandon the use of school
uniform."
"We should subsidize space exploration."
"We should abandon television."
"We should invest in the development of
high-speed railways."
"We should limit executive compensation
."
"College education should be free for
everyone."
"We must respect our parents."
"We should protect our privacy in the
Internet age."
"We should ban private military
companies."
"We should carry on the habits of our
elders."
"We should end illegal pushbacks."
"We often unconsciously conform to
others’ opinions."
"We should not be complacent."
"We should be kind to everyone."
"Retirement homes should become more
common."

--- Page 17 ---

Method
Inference Cost (3.4k samples)
Training Cost
Test Set F1 Score
GPT-4o-mini (single-step prompting)
$1.22
-
0.53
GPT-4o-mini (sequential prompting - CoT)
$1.90
-
0.57
GPT-4-turbo (sequential prompting - CoT)
$37.9
-
0.58
EAVIT (Llama2-chat-13b + GPT-4o-mini)
$0.27
$3.9 (8k generations)
0.69
Table 4: API cost evaluation on ValueEval.
plow and phigh
Test Set F1 Score
# LLM tokens
0.2, 0.8
0.67
0.51k
0, 0.8
0.59
2.45k
0.2, 1.0
0.65
0.67k
0.4, 0.8
0.62
0.38k
Table 5: Ablation study of candidate value set thresholds of EAVIT (Llama2-chat-13b + GPT-4o-mini) on ValueEval.
"Equal pay for equal work should apply
as a principle."
"We should stop unrestricted
deforestation and logging."
"Carbon emissions trading should be
limited."
"We should adopt atheism."
The complete set of generated data is attached to the paper. A
sample of the generated text data instances are:
{"argument": "We should allocate 3% of
GDP for research and innovation by
2035.", "answer": "supportive", "
explanation": "I believe it is
important to allocate 3% of GDP for
research and innovation because it
allows for the development of new
ideas and creativity, which I value.
Additionally, investing in research
and innovation can lead to
advancements that benefit society
and improve the well-being of people
around me."}
{"argument": "We should abandon
television.", "answer": "
unsupportive", "explanation": "I am
unsupportive of the idea to abandon
television because it is very
important to me to have a good time
and spoil myself. Television
provides entertainment and
relaxation, allowing me to unwind
and enjoy myself after a long day."}
{"argument": "College education should
be free for everyone. ", "answer": "
supportive", "explanation": "I
believe that college education
should be free for everyone. It is
important to help society and
provide equal opportunities for all.
Education is a stepping stone for
success and by making it accessible
to all, we can create a more equal
and prosperous society."}
{"argument": "We should end illegal
pushbacks. ", "answer": "supportive
", "explanation": "I believe that we
should end illegal pushbacks
because it aligns with my values of
doing something for the good of
society and caring for the well-
being of others. It is important to
prioritize human rights and ensure
fair and just treatment for everyone
."}
Finally, we process these text data using EAVIT and other
methods trained on Touch´e23-ValueEval to identify values
behind them. To aggregate the results on each text data into
the final value identification result for individuals, we label
the result sEAVIT of each virtual individual on the value v as
1 if and only if there are at least 3 associated generated texts
that are relevant to the value v. In table 3, we classify the
result sEAVIT as accurate if |sEAVIT −sreal| < 0.5.
Training Cost Evaluation
Table 4 is an evaluation of OpenAI API cost on experiments
on ValueEval. The inference API cost of EAVIT is signif-
cantly lower than complete LLM-based methods. Besides,
the cost for generating additional training data is also lower
than the entire inference API cost of GPT-4o-mini (single-
step prompting) method, showing that the data generation
process is cost-effective for performance improvement. The
local LM (Llama2-13b) is 4-bit quantized and trained on a
single local RTX 4090 GPU for 10 hours, which is much
lower than the online LLM costs.
Experiments on Thresholds plow and phigh
Table 5 is an ablation study of the thresholds plow and phigh
in EAVIT, which control the selection of candidate values to

--- Page 18 ---

LLM for final identification 4.2. According to the results, the
current experimental set plow = 0.2 and phigh = 0.8 is the
optimal setting.
8.3
More Discussion
Human Value Theories
In psychology, research on hu-
man values has been extensive, with key contributions from
[Rokeach, 1973] establishing a value system, [Schwartz,
2012] creating Schwartz’s theory of basic values and cross-
cultural value questions, [Cheng and Fleischmann, 2010]
consolidating taxonomies into a meta-inventory of values,
[Gert, 2004] proposing common morality theory, [Graham
et al., 2013] building the Moral Foundation Theory, and
[De Giorgis et al., 2022] introducing the linked open data
scheme, ValueNet. These taxonomies have been extensively
utilized in social science studies and automated detection of
human values could significantly aid such analyses [Scharf-
billig et al., 2021; Scharfbillig et al., 2022].
In our pa-
per, following existing works [Kiesel et al., 2023], we adopt
Schwartz’s Theory of Basic Values [Schwartz, 2012] as the
basic value system for value identification, which has been
applied in multiple fields including economics [Ng et al.,
2005] and LLMs [Miotto et al., 2022; Fischer et al., 2023].
However, it should be noted that our method is applicable to
any completely defined value system (such as the extended
Schwartz value system or those with values set for language
models).

```
