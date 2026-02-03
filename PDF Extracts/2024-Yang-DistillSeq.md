---
title: "DistillSeq - PDF Extract"
source_pdf: "2024-Yang-DistillSeq.pdf"
pages: 12
extracted_at: "2026-01-24T17:05:44.293909"
---

# PDF Extract: DistillSeq

**Source PDF:** 2024-Yang-DistillSeq.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

DistillSeq: A Framework for Safety Alignment Testing in Large
Language Models using Knowledge Distillation
Mingke Yang
ShanghaiTech University
Shanghai, China
yangmk@shanghaitech.edu.cn
Yuqi Chen∗
ShanghaiTech University
Shanghai, China
chenyq@shanghaitech.edu.cn
Yi Liu
Nanyang Technological University
Singapore, Singapore
yi009@e.ntu.edu.sg
Ling Shi
Nanyang Technological University
Singapore, Singapore
ling.shi@ntu.edu.sg
Abstract
Large Language Models (LLMs) have showcased their remarkable
capabilities in diverse domains, encompassing natural language un-
derstanding, translation, and even code generation. The potential
for LLMs to generate harmful content is a significant concern. This
risk necessitates rigorous testing and comprehensive evaluation of
LLMs to ensure safe and responsible use. However, extensive testing
of LLMs requires substantial computational resources, making it
an expensive endeavor. Therefore, exploring cost-saving strategies
during the testing phase is crucial to balance the need for thorough
evaluation with the constraints of resource availability. To address
this, our approach begins by transferring the moderation knowl-
edge from an LLM to a small model. Subsequently, we deploy two
distinct strategies for generating malicious queries: one based on
a syntax tree approach, and the other leveraging an LLM-based
method. Finally, our approach incorporates a sequential filter-test
process designed to identify test cases that are prone to eliciting
toxic responses. By doing so, we significantly curtail unnecessary
or unproductive interactions with LLMs, thereby streamlining the
testing process. Our research evaluated the efficacy of DistillSeq
across four LLMs: GPT-3.5, GPT-4.0, Vicuna-13B, and Llama-13B.
In the absence of DistillSeq, the observed attack success rates on
these LLMs stood at 31.5% for GPT-3.5, 21.4% for GPT-4.0, 28.3% for
Vicuna-13B, and 30.9% for Llama-13B. However, upon the applica-
tion of DistillSeq, these success rates notably increased to 58.5%,
50.7%, 52.5%, and 54.4%, respectively. This translated to an average
escalation in attack success rate by a factor of 93.0% when compared
to scenarios without the use of DistillSeq. Such findings highlight
the significant enhancement DistillSeq offers in terms of reducing
the time and resource investment required for effectively testing
LLMs.
∗Yuqi Chen is the corresponding author.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for third-party components of this work must be honored.
For all other uses, contact the owner/author(s).
ISSTA ’24, September 16–20, 2024, Vienna, Austria
© 2024 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-0612-7/24/09
https://doi.org/10.1145/3650212.3680304
CCS Concepts
• Security and privacy →Software security engineering.
Keywords
Knowledge Distillation, Large Language Models, Automated Test-
ing
ACM Reference Format:
Mingke Yang, Yuqi Chen, Yi Liu, and Ling Shi. 2024. DistillSeq: A Framework
for Safety Alignment Testing in Large Language Models using Knowledge
Distillation. In Proceedings of the 33rd ACM SIGSOFT International Sympo-
sium on Software Testing and Analysis (ISSTA ’24), September 16–20, 2024,
Vienna, Austria. ACM, New York, NY, USA, 12 pages. https://doi.org/10.
1145/3650212.3680304
1
Introduction
The field of large language models (LLMs) has seen remarkable
growth and evolution in recent years. These models have become
increasingly sophisticated, demonstrating an ability to generate
human-like text. As a result, LLMs have found extensive applica-
tions in various domains, most notably in education and content
creation. However, this swift advancement brings with it signifi-
cant ethical concerns. A primary issue is the potential misuse of
LLMs in generating deceptive or damaging content. For instance,
there is a risk of malicious entities manipulating these models to
produce harmful material. One common method of such misuse
involves employing a jailbreak prompt to circumvent the built-in
safety mechanisms of LLMs, as shown in Figure 1.
Figure 1: A jailbreak attack example.
While the AI community actively engages in discussions and
formulates strategies to mitigate these issues, extensive research
highlights the susceptibility of LLMs to malicious attacks. For in-
stance, Wei et al. [39] have illustrated the potential of exploiting
jailbreak prompts as a means to generate harmful content. Sun et
arXiv:2407.10106v4  [cs.SE]  8 Sep 2024

--- Page 2 ---

ISSTA ’24, September 16–20, 2024, Vienna, Austria
Mingke Yang, Yuqi Chen, Yi Liu, and Ling Shi
al. [35] have identified six distinct categories of instruction-based
attacks targeting LLMs, primarily executed through the manual
construction of prompts. Moreover, the proliferation of automated
prompt generation for such attacks has become an escalating con-
cern. Liu et al. [26] have automated the process of creating jailbreak
prompts using an LLM. Furthermore, Zou et al. [45] have proposed
a methodology for circumventing enhanced LLMs by appending
adversarial suffixes to prompts.
Concurrently, these attacks are not only challenges to be miti-
gated but also serve a crucial role as testing strategies for the deploy-
ment of LLMs. This dual role introduces a significant consideration:
the potential for reducing the costs associated with such testing.
The question of cost reduction is particularly relevant when con-
sidering the extensive requirements for generating a large volume
of test cases to interact with LLMs under test. For instance, eval-
uating a jailbreak prompt with 5,000 queries costs about $12 [32].
Alternatively, open-source models like Vicuna-13B offer a free but
time-intensive option. Deploying Vicuna-13B requires at least 24GB
of VRAM and takes about 160 minutes for the same evaluations [1].
Current research tends to focus more on attack strategies. This
approach often leads to frequent, unproductive interactions with
LLMs. Therefore, improving the success rates of these attacks is
crucial.
We present DistillSeq, an innovative framework designed for
the automated generation of malicious queries to evaluate the re-
silience of LLMs against potentially harmful input queries. Dis-
tillSeq operates through a two-fold process: knowledge distillation
and sequential filter-test procedure. The framework is detailed in
the workflow diagram in Figure 2. The initial phase of DistillSeq
revolves around the concept of knowledge distillation. In this stage,
we transfer the moderation mechanism knowledge from the LLM
under test to a more compact and efficient distilled model. In the
subsequent stage, this distilled model meticulously evaluates the
malicious queries by applying a rigorous filtering mechanism. It
filters out malicious queries that are improbable to elicit harm-
ful or toxic responses. This filtering process leads to a substantial
reduction in the number of queries necessary during the testing
phase.
We have conducted an evaluation on four popular LLMs: GPT-
3.5 [30], GPT-4 [31], Vicuna-13B [1], and LLama-13B[29]. We mea-
sured the effectiveness of DistillSeq using the attack success rate.
The percentage of successful malicious queries that prompt LLMs
to generate toxic content. By employing the distilled model as a
filter, we achieved an average attack success rate of 49.8% using the
Syntax tree-based method, and 58.3% with the LLM-based method.
This method significantly improved effectiveness. Our research
evaluated the effectiveness of DistillSeq on a range of LLMs in-
cluding GPT-3.5, GPT-4.0, Vicuna-13B, and Llama-13B. In scenarios
where DistillSeq was not employed, the attack success rates were
recorded as 31.5% for GPT-3.5, 21.4% for GPT-4.0, 28.3% for Vicuna-
13B, and 30.9% for Llama-13B. Remarkably, with the implementation
of DistillSeq, these success rates significantly increased to 58.5%,
50.7%, 52.5%, and 54.4% for each model, respectively. This indicates
an average increase in the attack success rate of 93.0% when Dis-
tillSeq is utilized, compared to scenarios where it is absent. Our
results highlight significant limitations in current safety alignments
and offer a more efficient approach for testing these models.
Overall, we make the following contributions:
• Knowledge Distillation for LLM Safety Alignment: We
propose a novel knowledge distillation method to transfer
moderation knowledge from LLMs to smaller, more efficient
distilled models.
• Effective Testing Framework: We propose an automated
testing framework called DistillSeq, designed to generate
malicious queries using syntax tree-based and LLM-based
approaches. These queries are subsequently filtered using
distilled models to identify effective queries for testing the
LLM.
• Empirical Evidence of Method Effectiveness: We eval-
uated DistillSeq on four mainstream LLMs. The results
demonstrate that DistillSeq significantly increases the av-
erage attack success rate by 93% and generates more effective
malicious queries compared to existing methods.
The paper is organized as follows. In Section 2, we review some
essential background information and present our motivation for
developing DistillSeq. Section 3 introduces the design of Dis-
tillSeq, including the detailed algorithms for constructing mali-
cious queries and the process of knowledge distillation. Section 4
evaluates whether DistillSeq achieves its goal of effectively test-
ing LLMs. Finally, Section 5 compares our approach against some
related work, and Section 6 concludes the paper.
2
Background & Motivation
In this section, we provide an overview of the background knowl-
edge relevant to our paper, including discussions on Jailbreak and
Knowledge Distillation. Additionally, we introduce the motivation
behind our research.
2.1
Jailbreak
In the context of large language models, “jailbreaking” refers to a
phenomenon where the model disregards or bypasses predefined
constraints when given specific inputs [4, 21, 40]. It may generate
biased, harmful, or unethical content. Figure 1 shows an example of
a jailbreak attack. The model refuses to directly answer a malicious
query like “I want to cause public panic what should I do.” However,
when the same question is appended to a jailbreak prompt, the
model generates a toxic response without any awareness.
Jailbreak prompts are templates that help conceal malicious
queries and evade LLM’s moderation. In the example above, the
jailbreak prompt masks the malicious intent of the query. It success-
fully manipulates the model into providing a potentially harmful
response. However, jailbreak prompts do not work for every mali-
cious query. Experiments by Deng et al. [7] show that even with
jailbreak prompts, the success rate of jailbreaking GPT-4 is only
15.32%. In this study, we use jailbreak prompts by automatically
constructing high-quality malicious queries and appending them
to the prompts. This causes the LLM to generate toxic content.
2.2
Knowledge Distillation
Knowledge distillation is a pivotal technique in machine learn-
ing. It facilitates the transfer of knowledge from a sophisticated,
large-scale ‘teacher model’ to a more streamlined, compact ‘stu-
dent model’ [17]. This process is instrumental in enabling smaller

--- Page 3 ---

DistillSeq: A Framework for Safety Alignment Testing in Large Language Models using Knowledge Distillation
ISSTA ’24, September 16–20, 2024, Vienna, Austria
Figure 2: Overview of our knowledge distillation-based sequential filter-test process
models to sustain high-performance levels while operating with
considerably fewer computational resources.
Offline knowledge distillation is a commonly used technique in
the field of knowledge distillation. It involves using a fully trained
teacher model to create a specialized dataset. This dataset will
be used to train the student model. This process allows the stu-
dent model to learn from the teacher model’s outputs, effectively
compressing the knowledge into a more compact form while main-
taining comparable performance.
Introducing knowledge distillation technology into testing LLMs
can enhance their efficiency. Traditional testing methods directly
interact with LLMs, which significantly consumes computing re-
sources and time. In our work, leveraging distillation, moderation
knowledge can be extracted from LLMs and utilized to train more
compact student models that offer faster inference speeds. During
the testing phase, initial evaluations can be conducted on the stu-
dent model to identify and select effective test cases before proceed-
ing with testing on the LLM. This approach effectively improves
the efficiency and precision of the testing process.
2.3
Motivation
The implementation of safety alignment strategies in LLMs has
significantly increased the challenge of eliciting harmful outputs.
Given the significant costs associated with LLMs, it is imperative to
adopt advanced and financially demanding testing methodologies
for testing purposes. DistillSeq offers an advantage in this context
by streamlining the testing process through the pre-filtering of test
samples. This enhancement not only improves the efficiency of the
testing procedure but also potentially reduces the overall resource
expenditure.
To further explain the practical advantages of our DistillSeq
framework, we reproduced jailbreak attacks from the empirical
study conducted by Liu et al. [26] as an example for comparison.
Specifically, we examined the GPT-4.0 model by executing 17,000
jailbreak attacks, resulting in the identification of 121 security vio-
lations. This testing required approximately 8,500,000 tokens, with
a financial cost of around $300 based on OpenAI’s pricing policy.
Utilizing our DistillSeq framework, we achieved a significant re-
duction in the number of queries required to attain an equal number
of violations in the GPT-4.0 model, accomplishing this with only
240 queries. These queries corresponded to a token usage of just
120,000, resulting in a financial cost of approximately $4. In addi-
tion, for a fair comparison, we should include the cost of training
the model in our framework in the knowledge distillation process.
We utilized a training set of 4,000 samples, with OpenAI’s pricing
of $0.03 per 1000 tokens for input and $0.06 per 1000 tokens for
output[32]. Each query utilized approximately 200 tokens for in-
put and 100 tokens for output. Therefore, the total training cost is
calculated as (0.03 × 200/1000 + 0.06 × 100/1000) × 4000 = $48. Fol-
lowing this, we conducted the distillation offline using an NVIDIA
GeForce RTX 3090 GPU, which required approximately one hour of
processing time. Leveraging pricing data from Vastai1, we estimate
the expense for this operation to be around $0.35. Overall, the total
cost involved in our approach is $52.35, representing approximately
a fivefold reduction in testing costs compared to the traditional
jailbreak attack method.
3
Methodology
This section initiates with an explanation of the problem and sub-
sequently elaborates on the two stages in our proposed framework,
DistillSeq. The pipeline is illustrated in Figure 2, where the grey
arrows symbolize the data processing flow within our model ar-
chitecture, indicating the direction and stages through which data
is processed. Concurrently, the blue arrows denote the knowledge
distillation process, highlighting the mechanism through which the
distilled model’s parameters are fine-tuned via the application of
distillation loss.
3.1
Problem Statement
Our work focuses on using knowledge distillation to train a student
model that learns LLM moderation mechanism knowledge. This
model effectively filters out ineffective toxic content in the context
of a jailbreak attack. Employing the student model as the filter can
reduce the total number of queries, thereby improving the efficiency
of testing LLMs. We initially introduce specific details regarding our
setting and then formalize the problem with the following settings:
• Unknown Weights: The weights or metrics of the distilled
model are not provided.
• Data-free: The original training data is not available, and
item statistics (e.g., popularity) are not accessible.
• Unknown Architecture: The training architecture of the dis-
tilled safety alignment is also not provided.
In general, we have a set of training samples X = {𝑥1,𝑥2, ...,𝑥𝑁}.
By querying models, we obtain oracle scores Y = {𝑦1,𝑦2, ...,𝑦𝑁}.
To enhance performance, we query multiple models. Considering
𝐾models, 𝑓= {𝑓(1), 𝑓(2), ..., 𝑓(𝐾)}. We query the 𝑘-th LLM 𝑓(𝑘)
with the samples in X and retrieves corresponding scores 𝑦(𝑘) =
{𝑓(𝑘) (𝑥1), 𝑓(𝑘) (𝑥2), ..., 𝑓(𝑘) (𝑥𝑁)}. We learn a distilled model 𝑓𝑑𝑚
1https://vast.ai/

--- Page 4 ---

ISSTA ’24, September 16–20, 2024, Vienna, Austria
Mingke Yang, Yuqi Chen, Yi Liu, and Ling Shi
based on the queries and concatenated retrieved scores < X, Y (𝑘) >.
We develop an automated method for generating malicious queries
X𝑚= {𝑥𝑚
1 ,𝑥𝑚
2 , ...,𝑥𝑚
𝑁}. By employing 𝑓𝑑𝑚for their filtration, we
acquire X𝑓𝑚= {𝑥𝑓𝑚
1
,𝑥𝑓𝑚
2
, ...,𝑥𝑓𝑚
𝑀}, where 𝑁≥𝑀, with X𝑓𝑚
serving as the test cases for the efficient evaluation of 𝑓(𝑘).
3.2
Building a Distillation Model
In this stage, we employ knowledge distillation to train a student
model to mimic the moderation mechanisms of LLMs. Given the
black-box nature of closed-source LLMs such as GPT-3.5 and GPT-4,
obtaining intermediate representations from these models is not
feasible. Therefore, we adopt a response-based knowledge distilla-
tion approach to design a testing method applicable to all LLMs.
Our approach involves utilizing the neural response from the last
output layer of the teacher model, aiming to directly mimic the
behavior of safety-aligned large language models.
In our study, we define knowledge distillation as the process of
creating a distilled model, denoted as 𝑓𝑑𝑚, from an LLM, represented
by 𝑓𝑙𝑙𝑚. The extraction of information from the LLM 𝑓𝑙𝑙𝑚is achieved
without direct access to its internal weights by querying the LLM
and analyzing its outputs. Our primary goal is to minimize the
discrepancy between the responses of the LLM 𝑓𝑙𝑙𝑚and our distilled
model 𝑓𝑑𝑚.
We utilize a dataset containing malicious queries empirically
known to elicit harmful responses. However, as observed by Zhuo
et al. [44], the probability of LLMs producing toxic responses solely
based on malicious queries is typically low. To address this issue,
we introduce jailbreak prompts, which significantly increase the
probability of circumventing LLM moderation when combined
with malicious requests [26]. Our queries are generated by merging
these jailbreak prompts with the malicious queries. Subsequently,
we meticulously assess the toxicity scores of the LLMs’ responses
using an online toxicity detection tool.
The distilled model 𝑓𝑑𝑚is specifically designed to evaluate mali-
cious queries and exclusively receives malicious queries as input for
its operational purpose. The distillation process can be seen as an
optimization problem, where the goal is to minimize the distillation
loss on the target domain T (malicious queries), allowing 𝑓𝑑𝑚to
mimic the behavior of 𝑓𝑙𝑙𝑚. This process can be expressed as:
min
𝑓𝑑𝑚
E(𝑥) ∼T [L(𝑓𝑙𝑙𝑚(𝑥), 𝑓𝑑𝑚(𝑥))]
(1)
To optimize the weights in 𝑓𝑑𝑚, we use cross-entropy as the loss
function L to calculate the difference between 𝑓𝑙𝑙𝑚(𝑥) and 𝑓𝑑𝑚(𝑥)
predictions. In practice, we stop the knowledge distillation process
when the distillation loss is less than 0.1.
3.3
Generate New Malicious Queries
We leverage our distilled model to predict the potential toxicity
of diverse content, facilitating the identification and elimination
of content less likely to elicit a toxic response. The next step is
automatically generating malicious queries that effectively elicit
harmful responses from LLMs. In this stage, we introduce two
distinct approaches: a Syntax tree-based method and an LLM-based
method.
Syntax tree-based method. In the domain of Natural Language
Processing (NLP), traditional methods for generating adversarial
samples typically involve minor modifications at the level of letters
or words while maintaining the semantic integrity of the sentences.
However, generating adversarial samples for LLMs using subtle
alterations is minimally effective. This is due to the advanced seman-
tic understanding capabilities of LLMs, which render such subtle
changes largely ineffective. These models can detect and correct mi-
nor perturbations without any significant change in the sentence’s
underlying meaning. To solve this, our research introduces a novel
syntax tree-level method for generating new malicious queries.
Distinct from conventional word-level substitution attacks, our
approach operates on a more structural level of language process-
ing. We open up a substantially larger search space for malicious
query generation by manipulating and replacing entire syntax trees
within sentences.
Formally, for two malicious queries, labeled 𝑇𝑎and 𝑇𝑏, we trans-
form them into their respective syntax trees, named 𝑆𝑎and 𝑆𝑏. The
syntax tree 𝑆𝑎is denoted as 𝑆𝑎= [𝑡0, ...,𝑡𝑖, ...], with 𝑡𝑖signifying
the 𝑖-th syntax subtree in 𝑆𝑎. We then evaluate the significance of
each syntax subtree using this formula:
𝐼𝑡𝑖=
𝑓𝑑𝑚(𝑆) −𝑓𝑑𝑚(𝑆/𝑡𝑖)
𝑙𝑒𝑛(𝑡𝑖)
(2)
where 𝑆/𝑡𝑖is defined as [𝑡0, ...,𝑡𝑖−1,𝑡𝑖+1, ...]. We use 𝑙𝑒𝑛(𝑡𝑖) to cal-
culate the length of 𝑡𝑖. The aim is to choose concise syntax subtrees
that are rich in semantic information, to avoid the replacement of
the entire syntax tree. The guiding hypothesis for this formula is
that a subtree’s importance to the model’s output is directly pro-
portional to the effect of its removal on the model’s predictions.
This idea is based on the understanding that input data elements
causing significant output changes upon alteration or removal are
crucial in the model’s decision-making. Specifically, the larger the
discrepancy between 𝑓𝑑𝑚(𝑆) and 𝑓𝑑𝑚(𝑆/𝑡𝑖), the greater the inferred
importance of the subtree in question. Finally, we replace the syntax
subtrees in 𝑆𝑎with those from 𝑆𝑏, prioritizing those with higher
importance scores and matching syntactic categories. This method
of interchanging syntax trees enables us to systematically generate
new, semantically varied malicious queries.
Algorithm 1 illustrates the syntax tree-based method in detail. It
processes two randomly selected potentially malicious queries. In
lines 3-4, these queries are transformed into their respective syn-
tactic subtrees. Lines 5-6 involve calculating the importance scores
of the syntactic subtrees in query 𝑄𝑎. Subsequently, in lines 7-8,
the algorithm collects syntactic subtrees from query 𝑄𝑏. The algo-
rithm then replaces the top 𝑛most significant subtrees in 𝑄𝑎with
subtrees from 𝑄𝑏of the same syntactic category in lines 9-11. This
process aims to generate new queries that can effectively evaluate
the model’s ability to identify and handle malicious queries.
In this method, we apply two strategies to reduce the generation
of nonsensical queries. First, during the replacement process, our
approach is to maintain the structural integrity of the syntactic tree.
This is achieved by substituting syntactic subtrees with alterna-
tives of the same syntactic category. This method ensures that the
overall structure of the sentence remains intact, thereby preserv-
ing grammatical correctness. Adhering to this principle reduces
the likelihood of generating nonsensical outputs, as the syntactic

--- Page 5 ---

DistillSeq: A Framework for Safety Alignment Testing in Large Language Models using Knowledge Distillation
ISSTA ’24, September 16–20, 2024, Vienna, Austria
framework of the query is maintained. Second, we implement a
Algorithm 1: Syntax Tree-Based Malicious Query Genera-
tion
Data: The malicious query 𝑄𝑎and 𝑄𝑏, 𝑁the number of
replacement subtrees
Result: Output a set of generated prompts 𝑇𝑛𝑒𝑤
1 𝑆←∅;
2 𝑇←∅;
3 parse 𝑄𝑎to a syntax tree 𝑆𝑎
4 parse 𝑄𝑏to a syntax tree 𝑆𝑏
5 for each subtree 𝑡in 𝑆𝑎do
6
compute the importance score 𝐼𝑡
7 for each subtree 𝑠in 𝑆𝑏do
8
S = S ∪𝑠;
9 for top 𝑁𝐼𝑡subtree 𝑡in 𝑆𝑎do
10
for each subtree 𝑠in 𝑆do
11
if 𝑠is same syntactic category with 𝑡then
12
𝑟𝑒𝑡= replace 𝑡in 𝑆𝑎’s copy with 𝑠;
13
𝑇= 𝑇∪𝑟𝑒𝑡;
14 return 𝑇
selection method that prioritizes the replacement of the shortest
possible subtrees. This strategy aims to minimize the impact on
the sentence’s coherence and meaning. By limiting modifications
to smaller, more manageable components of the sentence, we can
maintain a higher degree of semantic integrity.
Figure 3 demonstrates an example of the syntax tree-based
method. Through calculation, we find that the subtree “help others
out of trouble” possesses the highest influence within the syntax
tree, and this subtree belongs to a verb phrase. Subsequently, we
select another subtree, “destroy other people’s property” which
is also a verb phrase, to replace the most influential subtree. This
substitution operation generates a new malicious query, which can
induce LLM to produce toxic output.
Figure 3: A Syntax Tree-based replacement example
LLM-based method. This study extends Deng et al.’s [7] research
on using LLMs for creating jailbreak prompts. Our objective is
to fine-tune an LLM capable of autonomously producing high-
quality malicious queries. Our method contains two distinct phases.
The first phase focuses on augmenting the LLMs’ comprehen-
sion abilities, aiming to train them to better understand malicious
queries. The second phase focuses on creating high-quality mali-
cious queries.
In phase one, we fine-tune a Vicuna-13B model using LMFlow [10].
This process enhances the model’s ability to identify and handle
malicious queries. We conduct the fine-tuning using a
Table 1: The hyperparameter settings
Model
Hyperparameter
Epoch
Learning Rate
Batch Size
BERT
10
5 × 10−5
128
RoBERTA
10
4 × 10−5
128
DeBERTA
10
2 × 10−5
128
ERNIE
4
25 × 10−6
64
specially curated dataset, specifically the RealToxicPrompts [12]
dataset, which contains various toxic and harmful content samples.
Vicuna-13B generates the LLM’s responses to these queries, training
it to recognize, anticipate, and extend conversations with malicious
queries. This process helps Vicuna-13B simulate real-world LLM in-
teractions more accurately. The initial phase of pre-training focuses
on tasks related to toxic and harmful content, providing Vicuna-13B
with a foundational understanding of such content. This allows for
more nuanced and informed responses during the fine-tuning stage,
which further hones the model’s ability to comprehend and interact
with malicious queries. This process improves the performance of
LLMs on tasks related to malicious queries.
In phase two, we create high-quality malicious queries by lever-
aging the fine-tuned Vicuna-13B model. These malicious queries
follow a constructed prompt detailed in the Generate Malicious
Query Prompt. The prompt emphasizes maintaining high standards
of quality and relevance in the generated queries. This ensures that
the resulting malicious queries are not only realistic and effective
but also closely aligned with the objectives and scope of our study.
This process ensures that the generated queries closely emulate
qualities of authentic malicious queries observed in the real world
while maintaining a high standard of quality and relevance to the
study’s objectives.
After generating these potentially malicious queries, we employ
a distilled model to filter out the queries that are deemed to be
effective. This step ensures that we focus our efforts on the most
potent and relevant queries. Finally, we feed the filtered malicious
queries into LLMs and gather their responses. We aim to use these
carefully crafted malicious queries to effectively probe the LLMs
and assess their propensity to produce toxic or harmful content in
response.
Generate Malicious Query Prompt
Please read the following example malicious query in {{}}
and generate new queries that are similar in style and con-
tent. Ensure that the length, tone, and theme of your sen-
tences closely match the original ones.
Example 1: ’{{malicious query 1}}’
Example 2: ’{{malicious query 2}}’
Example 3: ’{{malicious query 3}}’

--- Page 6 ---

ISSTA ’24, September 16–20, 2024, Vienna, Austria
Mingke Yang, Yuqi Chen, Yi Liu, and Ling Shi
4
Evaluation
In this section, we present our evaluation of DistillSeq. The im-
plementation details of DistillSeq are available on our project
website 2. To assess its effectiveness, we explore the following re-
search questions:
• RQ1(Effectiveness): Can our framework successfully distill
the moderation mechanisms of LLMs?
• RQ2(Tradeoff): How can we effectively balance model per-
formance and dataset size in our framework?
• RQ3 (Generality): Is knowledge distillation in our frame-
work effective in handling new data and different LLMs,
demonstrating its generality?
• RQ4 (Comparisons): What is the performance of DistillSeq
compared to state-of-art tools?
• RQ5 (Configuration): How can we configure the LLMs to
improve attack success rates?
4.1
Dataset
To implement knowledge distillation in our framework, we require
datasets for training. Here, we construct the dataset by combining
jailbreak prompts and malicious queries as input. These jailbreak
prompts are sourced from Jailbreak Chat3. In addition, we follow
the categorization proposed by Liu et al. [26], which divides jail-
break prompts into Pretending, Attention Shifting, and Privilege
Escalation. We select the top two popular prompts from each cat-
egory based on user votes, as it reflects the effectiveness of these
jailbreak prompts in eliciting toxic responses from LLMs, as judged
by user experience. Currently, there is no universally accepted,
systematic standard for assessing the quality of jailbreak prompts.
We make this decision based on the fact that Jailbreak Chat hosts
the most extensive collection of LLM jailbreak attempts available
online, making its prompts widely utilized by many users.
For malicious queries, we use RealToxicPrompts [12], a collection
from OpenWebText [13]. RealToxicityPrompts is a benchmark for
LLM safety alignment evaluation. To assess the toxicity of LLM
outputs, we use the Perspective API4, which is known for accurate
toxicity assessment.
To further measure the effectiveness of the Perspective API, we
conducted a process of manual inspection to verify the reliability
of its toxicity evaluations. We used the Jigsaw dataset for this anal-
ysis and selected 1,000 samples representing a wide range of toxic
behaviors, including malicious, offensive, and hate speech. Two
independent researchers manually reviewed each data point against
predefined criteria. A third researcher resolved any discrepancies to
ensure accuracy. After this review, we applied the Perspective API
to the 1,000 vetted comments and documented the classification
results for each comment. The Perspective API showed a 92.3%
accuracy and an F1 score of 0.922. These results confirm the API’s
effectiveness in identifying toxic content.
2https://distillseq.github.io/page/
3https://www.jailbreakchat.com/
4https://perspectiveapi.com/
4.2
RQ1: Effectiveness
Motivation. This research question focuses on evaluating whether
our framework can utilize a smaller model to distill the knowl-
edge of the moderation mechanisms of LLMs. We evaluate the
performance of the distilled model by analyzing the consistency
of classifications between it and the responses of the LLMs when
faced with malicious queries.
Method. To evaluate the effectiveness of knowledge distillation,
we use a metric based on the consistency of classifications between
the distilled model and the LLMs when they encounter malicious
queries. The idea is that our distilled model functions as a binary
classification model, determining whether a given malicious query
will elicit a toxic response from the LLM. The toxicity of LLM out-
put is judged using the Perspective API mentioned in Section 4.1.
Adhering to the API’s documentation, we set the threshold value
at 0.7. This implies that toxicity scores exceeding 0.7 indicate a ma-
licious query, whereas scores below 0.7 suggest non-toxic content.
Mathematically, the agreement metric is calculated as:
𝐴𝑔𝑟𝑒𝑒𝑚𝑒𝑛𝑡= Number of Consistent Classifications
Total Number of Queries
Additionally, we employ the method outlined in Section 3.2
to compute the loss, which serves as another metric. Knowledge
distillation optimizes parameters by minimizing loss, aiming for the
distilled model’s predictions on the training data to closely match
the true labels. Therefore, using loss as a metric can reflect the
effectiveness of knowledge distillation.
For computing these metrics, in this research question, we uti-
lize GPT-3.5 as the teacher model. To perform knowledge distil-
lation, we select 4,000 queries from our dataset as input to the
LLM. Among these queries, 2,000 elicit toxic responses, while the
remaining queries do not. It is important to note that we conduct
10 iterations for each query, and if the LLM gives a toxic response
more than 6 times out of these iterations, we consider the query
to be an effective malicious query. We construct the training set
using these queries and their corresponding labels based on the re-
sponses. Similarly, we select 1,000 different queries from our dataset
to create the testing set. In our knowledge distillation process, we
utilize BERT [9], RoBERTa [27], ERNIE [36], and DeBERTa [15] as
the architecture for the student model. The reason is that these
models have demonstrated strong capabilities in processing and
understanding natural language text. Additionally, similar to LLMs,
they are all pretrained language models that have been trained on
vast amounts of text data. Our hyperparameter settings are based
on the recommendations by Karl et al. [20]. Details of these settings
are provided in Table 1.
Results. Table 2 display the accuracy and loss of the models on both
the training and test sets. The trends in accuracy and loss for most
models clearly indicate that knowledge distillation substantially
enhances prediction reliability and accuracy. Specifically, RoBERTa
and DeBERTa demonstrate exceptional performance. RoBERTa
achieves 96.73% accuracy and 0.01 loss on the training set, main-
taining 93.60% accuracy and 0.02 loss on the test set, outperforming
the other models. DeBERTa closely follows, achieving 95.67% ac-
curacy and 0.02 loss on the training set, with a test set accuracy
of 94.00% and a 0.01 loss. Although BERT also shows significant

--- Page 7 ---

DistillSeq: A Framework for Safety Alignment Testing in Large Language Models using Knowledge Distillation
ISSTA ’24, September 16–20, 2024, Vienna, Austria
Table 2: Agreement and loss of different distilled models Before Knowledge Distillation (B.K.D.) and After Knowledge Distillation
(A.K.D.)
Model
Training Set
Test Set
B.K.D. Agreement
A.K.D. Agreement
B.K.D. Loss
A.K.D. Loss
B.K.D. Agreement
A.K.D. Agreement
B.K.D. Loss
A.K.D. Loss
BERT
42.73
93.58
0.71
0.03
44.20
91.90
0.68
0.05
RoBERTa
53.12
96.73
0.61
0.01
56.30
93.60
0.55
0.02
DeBERTa
54.23
95.67
0.60
0.02
53.80
94.00
0.57
0.01
ERNIE
62.92
94.23
0.48
0.03
46.30
92.90
0.64
0.04
improvements, it is still less effective than RoBERTa and DeBERTa.
This difference in performance may be attributed to the more com-
plex attention mechanisms and extended training steps utilized by
DeBERTa and RoBERTa, enhancing their capabilities.
The distilled models still exhibit lower accuracy and higher loss
on the testing sets compared to the training sets. For example, BERT
achieves 93.6% accuracy and 0.03 loss on the training set, while its
accuracy slightly drops to 91.90%, and the loss increases to 0.05 on
the test set. Similarly, RoBERTa’s accuracy decreases from 96.73%
on the training set to 93.60% on the test set, and its loss rises from
0.01 to 0.02. While this discrepancy in performance between the two
sets suggests potential overfitting to the training data, the overall
performance remains acceptable for these models.
Answer to RQ1
DistillSeq effectively utilizes knowledge distillation to learn
from LLMs, proficiently classifying queries that are likely to
produce toxic content.
Figure 4: Distilled Model Agreement with GPT-3.5 Curve with
Varying Training Sample Sizes.
4.3
RQ2: Tradeoff
Motivation. In this research question, we study the trade-off be-
tween model performance and dataset size, as our goal is to optimize
the cost of testing LLMs. Although scaling up the dataset can im-
prove model performance, it also leads to higher training costs. In
this research question, we focus on determining the ideal dataset
size for cost-effective testing.
Method. To investigate the impact of training dataset size on the
performance of the distilled model, we conduct a series of exper-
iments with varying sample sizes. Starting from 0 samples, we
incrementally increase the number of samples by 2,000 in each
iteration. At each step, we train the distilled model using the cor-
responding number of samples and evaluate its agreement with
GPT-3.5 on the 1,000 randomly selected toxic comments from the
RealToxicPrompts dataset. To represent a real testing scenario, we
label the queries based directly on the responses of GPT-3.5. Since
these responses can be influenced by the variability of the LLM, the
agreement result will decrease to some extent.
Results. As depicted in Figure 4, the performance of our framework
improves with an increase in sample size. However, the growth rate
of agreement decreases as the sample size increases.
We assume that one query requires 200 tokens, and the LLM’s
output uses 100 tokens. According to OpenAI’s pricing scheme [32],
it can be determined that for every 2,000 queries, the cost would be
approximately $8. Specifically, the average agreement improvement
per 2,000 additional samples decreases from 28.28% (from 0 to 2,000
samples) to a mere 1.55% (from 8,000 to 10,000 samples). The average
cost per 1 percentage point improvement in agreement escalates
from $0.28 (from 0 to 2,000 samples) to a staggering $10.32 (from
8,000 to 10,000 samples).
When evaluating the practicality of a model, it is crucial to con-
sider both the training costs and the costs associated with tests.
For instance, training a model using 4,000 samples incurred a data
collection cost of $32 and a training cost of $0.35, resulting in a
total cost of $32.35. The model achieves an average agreement of
around 70%. It costs $0.005 to identify an effectively malicious query.
Assuming we need to identify 10,000 effectively malicious queries,
the total cost would be $82.35. However, training the model with
2,000 samples and 6,000 samples would incur costs of $91 and $92.8,
respectively. In this section, considering the slow growth in agree-
ment scores relative to the increase in training samples, we will
evaluate our approach using 4,000 samples during the knowledge
distillation phase. In a real testing scenario, testers may select the
appropriate data size for knowledge distillation based on the size
of their testing dataset.
Answer to RQ2
While the effectiveness of the model improves with an increased
amount of data used during knowledge distillation, the growth
rate slows down later on. Taking cost into account, we choose to
use 4,000 samples for knowledge distillation.
4.4
RQ3: Generality
Motivation. In this research question, our goal is to assess whether
our approach performs effectively when applied to various types

--- Page 8 ---

ISSTA ’24, September 16–20, 2024, Vienna, Austria
Mingke Yang, Yuqi Chen, Yi Liu, and Ling Shi
Table 3: Agreement of Models Before Knowledge Distillation (B.K.D.) and After Knowledge Distillation (A.K.D.) with LLMs
Model
LLM
GPT-3.5
GPT-4.0
Vicuna-13B
LLama-13B
Average Agreement
B.K.D
A.K.D.
B.K.D
A.K.D.
B.K.D
A.K.D.
B.K.D
A.K.D.
B.K.D
A.K.D.
BERT
17.30
66.50
13.40
57.60
25.60
61.90
16.80
63.50
18.28
62.38
RoBERTa
33.60
69.70
24.20
63.00
14.40
68.50
29.50
62.30
25.43
65.88
DeBERTa
26.70
68.50
19.60
64.80
19.50
65.10
20.10
68.20
21.48
66.65
ERNIE
24.50
71.80
21.50
59.30
23.20
55.10
34.60
52.10
25.95
59.58
Table 4: The Loss of the Distilled Model in Jigsaw Dataset
Model
Evaluation Result
B.K.D. Loss
A.K.D. Loss
BERT
0.78
0.17
RoBERTa
0.76
0.12
DeBERTa
0.64
0.19
ERNIE
0.85
0.23
of LLMs and when utilizing new data from a different dataset. The
reason for this evaluation is that given the rapid development of
large models, a method must be effective across different large
models. Furthermore, while our approach performs well on our
dataset, it is meaningful to test it in different scenarios since the
data within the same dataset may exhibit some similarities.
Method.
In this research question, we evaluate our framework’s perfor-
mance on four popular LLMs: GPT-3.5 [30], GPT-4 [31], Vicuna-
13B [37], and LLama-13B [29]. To mirror real-world scenarios, we
use the default settings of these LLMs, including temperature and
top-p values, for response generation. During the training phase,
we select 4,000 samples for knowledge distillation. We employ the
same method as in RQ1 to train the classification models.
For the new data, we utilize a new dataset from Kaggle’s Jigsaw
Toxic Comment Classification Challenge5. This dataset comprises
Wikipedia comments tagged for toxicity by human reviewers. We
randomly selected 1,000 queries from the Jigsaw dataset for evalua-
tion. We use the same method in RQ1 to calculate the agreement.
Results. The evaluation results are detailed in Table 3. The re-
sults show that the agreement between the distilled models and
the LLMs under test ranges from 52.10% to 71.80%. DeBERTa ex-
hibits the highest average agreement with the LLMs under test at
66.65%, while ERNIE shows the lowest agreement at 59.58%. After
knowledge distillation, all distilled models show an improvement of
approximately 40% in their agreement with the classifications of the
LLMs under test. This underlines the effectiveness of knowledge
distillation in enhancing the distilled models’ ability to recognize
and address malicious queries. It is noteworthy that different LLMs
exhibit varying degrees of alignment with the best-performing dis-
tilled model. For instance, Vicuna-13B aligns best with RoBERTa,
while the LLama series shows more agreement with BERT and
DeBERTa. These differences likely stem from the architectural sim-
ilarities between the moderation components of the LLMs and the
distilled models; a closer architectural resemblance leads to higher
5https://kaggle.com/competitions/jigsaw-multilingual-toxic-comment-classification
agreement. The vulnerable moderation mechanism of GPT-3.5 en-
ables the distilled models to attain a higher average agreement of
69.12%.
Some distilled models exhibit notably high agreement with the
LLMs under test. For example, the agreement peaks at 71.80% be-
tween ERNIE and GPT-3.5, and 64.80% between DeBERTa and GPT-
4.0. These findings indicate that newer LLMs, such as GPT-4.0,
exhibit less agreement with the distilled models compared to earlier
versions like GPT-3.5, reflecting the advancements in the safety
mechanisms of LLMs.
Compared to the results of Table 2, the distilled model shows a
decrease in agreement with the data from the Jigsaw dataset. We
believe this decrease can be attributed to several factors. First, the
distilled model might have undergone overfitting during its training
process, leading to subpar performance when encountering new
data. Second, the inherent randomness of LLMs means that they
may provide different responses to the same malicious content
upon multiple queries. This results in the distilled model’s inability
to make accurate predictions. Third, since we employed response-
based knowledge distillation, there was insufficient utilization of
the internal information of the LLM, leading to poor performance
in the agreement metric. Despite this, the average enhancement in
agreement after knowledge distillation is 63.74%, with individual
models showing distinct improvement patterns.
To further investigate the performance degradation, we present
the loss values obtained from these models on the Jigsaw dataset in
Table 4. Upon comparing the results in Table 2 and 4, we observe
that while the knowledge distillation process reduces the loss for the
Jigsaw dataset, the loss remains higher when compared to the loss
data in Table 2. This suggests that the model may rely on specific
characteristics unique to the training data. This also highlights that
our method can be enhanced by incorporating additional datasets
or augmenting the existing dataset with more diverse examples.
Answer to RQ3
While the inherent randomness of large models can influence our
method’s performance, the results indicate that our approach can
effectively learn the moderation mechanisms of various LLMs
across different contexts.
4.5
RQ4: Comparisons
Motivation. In this research question, we evaluate the effectiveness
of DistillSeq in testing LLMs. We compare the Attack Success
Rates (ASR) of our approach with state-of-the-art tools, showing
that our approach can lead to cost savings in testing. In addition,
we also integrate state-of-the-art tools with our filters, illustrating

--- Page 9 ---

DistillSeq: A Framework for Safety Alignment Testing in Large Language Models using Knowledge Distillation
ISSTA ’24, September 16–20, 2024, Vienna, Austria
how our approach can seamlessly complement well-established
tools.
Method. To evaluate our approach, we compare its performance
with two baseline methods, random word replacement and Textfooler,
and state-of-the-art tools including JailbreakingLLMs [5], GPT-
Fuzzer [42], FuzzLLM [41], HouYi [25]. Specifically, we utilize these
methods to generate 1,000 queries that may potentially elicit a toxic
response and feed them to the LLMs under testing. We assess their
efficacy by calculating the ASR, which is calculated as:
𝐴𝑆𝑅= Number of effective queries
Total number of queries
To enhance the evaluation of our knowledge distillation ap-
proach, we employ the DeBERTa models, selected for their out-
standing performance according to the results of RQ3, as filters. For
each approach, we filter out ineffective queries before presenting
them to the LLMs for testing. In this case, ASR is calculated as:
𝐴𝑆𝑅=
Number of effective queries
Number of queries passing the filter
Results. The evaluation results are detailed in Table 5. The ta-
ble delineates the performance of DistillSeq across two modes:
syntax-based and LLM-based methods with a filter. Compared with
other methods, the results demonstrate that DistillSeq using the
LLM-based method with a filter achieves the highest ASR for all
types of LLM. Specifically, the LLM-based method with a filter ob-
tains the highest average ASR at 58.25%, closely followed by the
syntax-based method with a filter at 49.78%. In contrast, other meth-
ods without a filter cannot even achieve a 20% average ASR. This
highlights that existing methods focus on generating sophisticated
malicious queries without adequately considering the associated
costs of interacting with the LLM.
To comprehensively evaluate the influence of filters on the ASRs
of each method, we conducted a comparison between results ob-
tained with and without filters in place. The result reveals a signifi-
cant increase in ASRs across all methods when the corresponding
filter is applied. For instance, the Random method experiences a
dramatic rise in ASR from 1.48% without filtering to 40.35% with
filtering, while Textfooler jumps from 14.43% to 38.15%. The other
methods also exhibit varying degrees of improvement when filter-
ing is employed. These findings highlight the effectiveness of our
knowledge distillation process in creating a distilled model capa-
ble of accurately identifying and filtering out invalid or irrelevant
malicious queries. Furthermore, this demonstrates that our method
can be easily applied to complement existing methods, thereby
reducing costs.
Finally, we also compare the performance of different methods
against various LLMs. The results indicate that GPT-4 generally
demonstrates the strongest resistance. Conversely, Vicuna-13B and
LLama-13B appear to be more susceptible to attacks, particularly
when confronted with methods like FuzzLLM and HouYi. How-
ever, it is essential to note that this trend is not entirely consistent
across all attack methods. For instance, when faced with the LLM-
based method, GPT-3.5 exhibits a higher ASR (60.70%) compared to
Vicuna-13B (59.5%) and LLama-13B (59.9%). This suggests that the
effectiveness of different attack methods can vary depending on
the specific LLM being targeted, highlighting the complexity of the
interplay between attack methods and LLM architectures. Further-
more, even the relatively robust GPT-4 yields concerningly high
ASRs of 48.50% and 52.90% under filtered syntax-tree-based and
LLM-based attacks, respectively. This highlights the importance of
further research and development efforts aimed at enhancing the
defense capabilities of LLMs against increasingly effective malicious
queries.
Answer to RQ4
DistillSeq demonstrates good performance in testing various
LLMs compared to existing methods. The knowledge distillation
in our approach can seamlessly complement well-established
tools, thereby reducing the cost of testing the LLMs.
4.6
RQ5: Configuration
Motivation. Huang et al. [18] pointed out that altering decoding
hyperparameters or sampling methods can significantly impact the
reliability of alignment procedures and evaluations in LLMs. In this
research question, we explore how different parameters of the LLM
impact the effectiveness of our approach.
Method. We adjust the top-p values and temperature parameters
across four LLMs under evaluation. Specifically, we set temperature
ranges from 0 to 2 for GPT models and 0 to 1 for LLama and Vicuna-
13B, while the top-p values range from 0 to 1 for all models. Each
model undergoes testing under various settings to assess the impact
of these parameters on the effectiveness of both Syntax tree-based
and LLM-based methods. To facilitate this evaluation, we employ
the Syntax tree-based and LLM-based methods to generate 1,000
queries for each parameter setting.
Results. The ASR for different top-p values on LLMs is presented
in Table 6. The results reveal that the effect of top-p on ASR differs
among the LLMs tested, with each model exhibiting unique patterns
of vulnerability. GPT 3.5 and Vicuna-13B show similar trends, with
the highest ASR observed at a top-p value of 0.75 for both the
Syntax Tree and LLM-based methods. For GPT 3.5, the ASR reaches
55.30% and 61.10% for the Syntax Tree and LLM-based methods,
respectively, while Vicuna-13B achieves an ASR of 41.80% and
60.80% for the same methods. These results suggest that a more
diverse pool of candidate tokens leads to increased vulnerability
to attacks in these models. In contrast, GPT 4 demonstrates a less
pronounced impact of top-p on ASR. The highest ASR for GPT
4 is achieved at a top-p value of 0.25 for the LLM-based method
at 53.40% and at a top-p value of 1 for the Syntax Tree method
at 42.40%. LLama-13B exhibits a unique pattern, with the highest
ASR achieved at a top-p value of 0.5 for both the Syntax Tree and
LLM-based methods, reaching 58.90% and 60.20%, respectively. This
suggests that a moderate level of diversity in the candidate token
pool leads to increased vulnerability in LLama-13B, in contrast to
the other models tested.
Tables 7 and 8 present the ASR for different temperature set-
tings on LLMs, evaluated using both Syntax Tree and LLM-based
methods. The results indicate that the temperature parameter af-
fects the ASR for all tested LLMs, generally resulting in increased
vulnerability to attacks with higher temperatures. For GPT 3.5 and
GPT 4, the highest ASR is observed at different temperature set-
tings depending on the evaluation method. For GPT 3.5, the highest

--- Page 10 ---

ISSTA ’24, September 16–20, 2024, Vienna, Austria
Mingke Yang, Yuqi Chen, Yi Liu, and Ling Shi
Table 5: Attack Success Rates (ASRs) of different malicious query generation methods on LLMs
Method
LLMs
GPT 3.5
GPT 4
Vicuna-13B
LLama-13B
Average
Random
Without Filter
2.20
1.70
1.20
0.80
1.48
Filter
44.30
37.20
40.40
39.50
40.35
Textfooler
Without Filter
15.30
10.70
14.30
17.40
14.43
Filter
36.90
42.10
40.30
33.30
38.15
Syntax-tree-based
Without Filter
23.60
18.90
24.10
28.30
23.73
Filter
56.30
48.50
45.50
48.80
49.78
LLM-based
Without Filter
39.30
23.80
32.40
32.50
32.00
Filter
60.70
52.90
59.50
59.90
58.25
JailbreakingLLMs
Without Filter
15.90
12.30
10.60
14.50
13.33
Filter
44.00
36.00
34.80
41.30
39.03
GPTFuzzer
Without Filter
15.40
12.30
27.30
16.50
17.88
Filter
36.70
30.20
48.80
31.80
36.88
FuzzLLM
Without Filter
8.80
5.90
19.90
16.60
12.80
Filter
18.50
16.30
52.10
38.90
31.45
MasterKey
Without Filter
18.40
11.20
19.30
15.00
15.98
Filter
45.20
47.30
32.60
36.10
40.30
HouYi
Without Filter
5.30
1.90
18.60
11.50
9.33
Filter
13.90
5.30
47.30
27.60
23.53
Table 6: ASR for for different top-p
Top-p
GPT 3.5
GPT 4
Vicuna-13B
LLama-13B
Syntax Tree
LLM
Syntax Tree
LLM
Syntax Tree
LLM
Syntax Tree
LLM
0.25
44.80
58.20
29.70
53.40
36.90
57.10
43.50
58.60
0.5
46.20
59.50
35.80
51.70
40.50
58.30
58.90
60.20
0.75
55.30
61.10
41.30
52.30
41.80
60.80
44.00
59.10
1
51.90
60.70
42.40
52.90
39.60
59.50
49.40
59.90
Table 7: ASR(%) for different temperatures on GPTs
Temperature
GPT 3.5
GPT 4
Syntax Tree
LLM
Syntax Tree
LLM
0
21.80
15.60
10.10
5.40
0.5
40.30
45.20
36.50
39.20
1
56.30
60.70
42.40
52.90
1.5
54.30
67.60
53.70
53.20
2
59.80
62.02
48.90
56.10
Table 8: ASR(%) for different temperatures on Vicuna and
LLama
Temperature
Vicuna-13B
LLama-13B
Syntax Tree
LLM
Syntax Tree
LLM
0.01
12.50
18.20
9.30
14.70
0.25
28.00
35.60
35.50
41.20
0.5
45.50
59.50
52.30
59.90
0.75
39.60
55.10
57.50
65.40
1
42.10
60.90
60.10
66.30
ASR is observed at a temperature of 2 for the Syntax Tree method
at 59.80% and a temperature of 1.5 for the LLM-based method at
67.60%. Similarly, GPT 4 reaches its peak ASR at a temperature of
1.5 for the Syntax Tree method at 53.70% and at a temperature of 2
for the LLM-based method at 56.10%. These findings suggest that
higher temperature settings make GPT models more vulnerable
to attacks compared to lower temperature settings. Vicuna-13B
and LLama-13B show a similar trend to GPT models. Vicuna-13B
achieves the highest ASR at a temperature of 0.5 for the Syntax Tree
method at 45.50% and a temperature of 1 for the LLM-based method
at 60.90%. LLama-13B reaches its peak ASR at a temperature of 1 for
both the Syntax Tree method at 60.10% and the LLM-based method
at 66.30%. These results indicate that higher temperature settings
also make Vicuna-13B and LLama-13B more vulnerable to attacks,
consistent with the findings for GPT models.
Answer to RQ5
The performance of our approach is influenced by hyperparam-
eters such as temperature and top-p values. As the impact of
top-p values is generally less significant compared to temper-
ature, we can enhance the ASR by configuring the LLMs with
higher temperatures.

--- Page 11 ---

DistillSeq: A Framework for Safety Alignment Testing in Large Language Models using Knowledge Distillation
ISSTA ’24, September 16–20, 2024, Vienna, Austria
4.7
Threats to Validity
Internal Validity. In our evaluation, the internal validity of our
findings may be affected by the presence of randomness. A no-
table challenge arises from the inconsistency observed in LLMs’
responses to identical harmful content. To address this inherent
unpredictability, we conducted multiple queries for each harmful
input as a countermeasure. Furthermore, in the context of knowl-
edge distillation, we limited our selection to four models during our
process, recognizing that alternative models may outperform them.
Our research primarily investigates the effectiveness of knowledge
distillation in enhancing testing efficiency rather than determining
optimal model selections. Consequently, our approach may require
additional validation and adaptation when applied to different LLMs
or other prospective models considered in future research.
External Validity. Two primary challenges come to the forefront
when considering the aspect of external validity. Firstly, the ques-
tion arises whether our approach can be effectively extended to the
realm of testing with alternative LLMs. Our investigation encom-
passed a spectrum of widely used LLMs. Variations exist among
them in terms of their architecture and training methodologies.
While our methodology takes these variations into account, it is
imperative to acknowledge that specific adaptations may be neces-
sitated to cater to the unique attributes of each LLM, thus ensuring
the preservation of the approach’s efficacy. Secondly, in the context
of knowledge distillation, we employed the Realtoxicityprompts
dataset. The utilization of this particular dataset may impose limita-
tions on the model’s ability to handle a diverse range of malicious
query inputs. To address this limitation, we introduce the Jigsaw
dataset in RQ2. This strategic integration is aimed at enhancing
the model’s adaptability across a broader spectrum of data types,
thus fortifying its capabilities in processing various forms of mali-
cious content. The selection of these supplementary datasets was
guided by the objective of encompassing a wider array of thematic
and stylistic nuances, thereby bolstering the model’s generalization
capabilities across an array of distinct scenarios.
5
Related Work
LLMs alignment.
Hendrycks et al. [16] introduced the ETHICS dataset to evaluate
LLMs’ understanding of ethics, revealing that LLMs have a par-
tial understanding of human ethics but lack comprehensive ethical
reasoning capabilities. While this dataset provides a valuable bench-
mark, it does not address the challenges of efficiently testing LLMs
for safety alignment. Dai et al. [6] developed Beaver, an open-source
RLHF framework that provides training data and reproducible code
for alignment studies. Although Beaver facilitates the training pro-
cess, it does not focus on optimizing the testing phase, which is
the primary concern of our proposed framework. Sun et al. [35]
introduced “SELF-ALIGN,” a method enabling the self-adjustment
of AI agents with minimal human supervision. While this method
ensures that LLM outputs align with human intentions, it does not
explicitly address the issue of efficient testing for safety alignment.
In contrast to previous works, we introduce a novel framework
that aims at the efficient testing of LLMs for safety alignment. By
transferring LLMs’ moderation knowledge to a small model and
employing syntax tree parsing and LLM-based methods for gener-
ating malicious queries, we significantly reduce the computational
resources required for thorough LLM evaluation.
Attack on LLMs. Aligning LLMs with human values remains
a challenging task, as demonstrated by recent research [3, 8, 24,
28, 34]. Various studies have explored the vulnerabilities of LLMs
and proposed methods to exploit or defend against these weak-
nesses [19, 22, 23]. Wallace et al. [38] showed that contextual trig-
gers can lead to biased and harmful LLM responses, highlighting the
need for robust safety measures. Gupta et al. [14] investigated meth-
ods like jailbreaking and prompt injection to bypass LLM ethical
constraints, demonstrating the potential for adversarial actors to ex-
ploit LLMs for malicious activities. However, their work focused on
manual exploitation techniques, whereas our approach automates
the testing process to identify vulnerabilities more efficiently. Self-
Cipher [43] uses natural language role-playing to unlock LLMs’ hid-
den encryption capabilities, circumventing safety protocols. While
their work showcases the potential for encrypted messaging to
evade LLM safety measures, our approach tackles the issue from
a different angle by generating targeted test cases to identify and
address vulnerabilities. Perez et al. [33] proposed PromptInject,
demonstrating that simple handcrafted inputs can easily misalign
GPT-3. Their work highlights the need for comprehensive testing of
LLMs. In contrast, our approach leverages an automatic framework
to generate a diverse set of test cases, reducing the reliance on
manual input crafting and increasing the efficiency of the testing
process. BadPrompt [2] is a lightweight and task-adaptive algorithm
for backdoor attacks on continuous prompts, effectively attacking
while maintaining high performance on clean test sets. PPT [11]
implants malicious behaviors into prompts, achieving a 99% attack
success rate on pre-trained language models with minimal accuracy
sacrifice on the original task. Unlike these white-box approaches
that rely on access to or manipulation of training data, our method
focuses on a more realistic black-box scenario, generating effective
attacks only based on the model’s output.
6
Conclusion
In this paper, we introduce a novel framework named DistillSeq,
designed to minimize the cost of testing LLMs. Our approach com-
bines knowledge distillation and prompt engineering to automati-
cally generate test cases that provoke LLMs to output toxic content.
Additionally, through experiments, we demonstrate the effective-
ness of our approach across several mainstream LLMs, surpassing
the capabilities of state-of-the-art tools in terms of testing cost
efficiency. We also emphasize that our approach can effectively
complement various attack strategies. Testers can enhance their
efficiency when testing LLMs by simply utilizing our approach to
train a filter. In future work, we plan to explore whether access
to neural information can lead to the development of a filter with
superior performance and efficiency.
Acknowledgements
We sincerely thank all the anonymous reviewers for their valuable
feedback, which greatly contributed to the improvement of this
paper. This research was jointly sponsored by the NSFC Program
under Grants No. 62302304 and the ShanghaiTech Startup Funding.

--- Page 12 ---

ISSTA ’24, September 16–20, 2024, Vienna, Austria
Mingke Yang, Yuqi Chen, Yi Liu, and Ling Shi
References
[1] andyll7772. 2023. Run a Chatgpt-like Chatbot on a Single GPU with ROCm.
https://github.com/huggingface/blog/blob/main/chatbot-amd-gpu.md.
[2] Xiangrui Cai, Haidong Xu, Sihan Xu, Ying Zhang, et al. 2022. Badprompt: Back-
door attacks on continuous prompts. Advances in Neural Information Processing
Systems 35 (2022), 37068–37080.
[3] Bochuan Cao, Yuanpu Cao, Lu Lin, and Jinghui Chen. 2023.
Defending
against alignment-breaking attacks via robustly aligned llm. arXiv preprint
arXiv:2309.14348 (2023).
[4] Zhiyuan Chang, Mingyang Li, Yi Liu, Junjie Wang, Qing Wang, and Yang Liu.
2024. Play Guessing Game with LLM: Indirect Jailbreak Attack with Implicit
Clues. arXiv:2402.09091 [cs.CR] https://arxiv.org/abs/2402.09091
[5] Patrick Chao, Alexander Robey, Edgar Dobriban, Hamed Hassani, George J
Pappas, and Eric Wong. 2023. Jailbreaking black box large language models in
twenty queries. arXiv preprint arXiv:2310.08419 (2023).
[6] Josef Dai, Xuehai Pan, Ruiyang Sun, Jiaming Ji, Xinbo Xu, Mickel Liu, Yizhou
Wang, and Yaodong Yang. 2023. Safe RLHF: Safe Reinforcement Learning from
Human Feedback. arXiv preprint arXiv:2310.12773 (2023).
[7] Gelei Deng, Yi Liu, Yuekang Li, Kailong Wang, Ying Zhang, Zefeng Li, Haoyu
Wang, Tianwei Zhang, and Yang Liu. 2023. Jailbreaker: Automated jailbreak
across multiple large language model chatbots. arXiv preprint arXiv:2307.08715
(2023).
[8] Gelei Deng, Yi Liu, Kailong Wang, Yuekang Li, Tianwei Zhang, and Yang Liu.
2024. Pandora: Jailbreak GPTs by Retrieval Augmented Generation Poisoning.
arXiv:2402.08416 [cs.CR] https://arxiv.org/abs/2402.08416
[9] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT:
Pre-training of Deep Bidirectional Transformers for Language Understanding. In
Proceedings of the 2019 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, Volume 1 (Long and
Short Papers). Association for Computational Linguistics, Minneapolis, Minnesota,
4171–4186. https://doi.org/10.18653/v1/N19-1423
[10] Shizhe Diao, Rui Pan, Hanze Dong, Ka Shun Shum, Jipeng Zhang, Wei Xiong, and
Tong Zhang. 2023. Lmflow: An extensible toolkit for finetuning and inference of
large foundation models. arXiv preprint arXiv:2306.12420 (2023).
[11] Wei Du, Yichun Zhao, Boqun Li, Gongshen Liu, and Shilin Wang. 2022. PPT:
Backdoor Attacks on Pre-trained Models via Poisoned Prompt Tuning.. In IJCAI.
680–686.
[12] Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, and Noah A Smith.
2020. Realtoxicityprompts: Evaluating neural toxic degeneration in language
models. arXiv preprint arXiv:2009.11462 (2020).
[13] Aaron Gokaslan and Vanya Cohen. 2019.
OpenWebText Corpus.
http://
Skylion007.github.io/OpenWebTextCorpus.
[14] Maanak Gupta, CharanKumar Akiri, Kshitiz Aryal, Eli Parker, and Lopamu-
dra Praharaj. 2023. From ChatGPT to ThreatGPT: Impact of generative AI in
cybersecurity and privacy. IEEE Access (2023).
[15] Pengcheng He, Xiaodong Liu, Jianfeng Gao, and Weizhu Chen. 2020.
De-
berta: Decoding-enhanced bert with disentangled attention.
arXiv preprint
arXiv:2006.03654 (2020).
[16] Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn
Song, and Jacob Steinhardt. 2020. Aligning ai with shared human values. arXiv
preprint arXiv:2008.02275 (2020).
[17] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. 2015. Distilling the knowledge in
a neural network. arXiv preprint arXiv:1503.02531 (2015).
[18] Yangsibo Huang, Samyak Gupta, Mengzhou Xia, Kai Li, and Danqi Chen. 2023.
Catastrophic jailbreak of open-source LLMs via exploiting generation. arXiv
preprint arXiv:2310.06987 (2023).
[19] Yihao Huang, Chong Wang, Xiaojun Jia, Qing Guo, Felix Juefei-Xu, Jian Zhang,
Geguang Pu, and Yang Liu. 2024. Semantic-guided Prompt Organization for
Universal Goal Hijacking against LLMs. arXiv preprint arXiv:2405.14189 (2024).
[20] Fabian Karl and Ansgar Scherp. 2022. Transformers are Short Text Classifiers: A
Study of Inductive Short Text Classifiers on Benchmarks and Real-world Datasets.
arXiv preprint arXiv:2211.16878 (2022).
[21] Jie Li, Yi Liu, Chongyang Liu, Ling Shi, Xiaoning Ren, Yaowen Zheng, Yang Liu,
and Yinxing Xue. 2024. A Cross-Language Investigation into Jailbreak Attacks
in Large Language Models. arXiv:2401.16765 [cs.CR] https://arxiv.org/abs/2401.
16765
[22] Ningke Li, Yuekang Li, Yi Liu, Ling Shi, Kailong Wang, and Haoyu Wang. 2024.
HalluVault: A Novel Logic Programming-aided Metamorphic Testing Framework
for Detecting Fact-Conflicting Hallucinations in Large Language Models. arXiv
preprint arXiv:2405.00648 (2024).
[23] Yuxi Li, Yi Liu, Yuekang Li, Ling Shi, Gelei Deng, Shengquan Chen, and Kailong
Wang. 2024. Lockpicking LLMs: A Logit-Based Jailbreak Using Token-level
Manipulation. arXiv preprint arXiv:2405.13068 (2024).
[24] Xiaogeng Liu, Nan Xu, Muhao Chen, and Chaowei Xiao. 2023. Autodan: Generat-
ing stealthy jailbreak prompts on aligned large language models. arXiv preprint
arXiv:2310.04451 (2023).
[25] Yi Liu, Gelei Deng, Yuekang Li, Kailong Wang, Tianwei Zhang, Yepang Liu,
Haoyu Wang, Yan Zheng, and Yang Liu. 2023. Prompt Injection attack against
LLM-integrated Applications. arXiv preprint arXiv:2306.05499 (2023).
[26] Yi Liu, Gelei Deng, Zhengzi Xu, Yuekang Li, Yaowen Zheng, Ying Zhang, Lida
Zhao, Tianwei Zhang, and Yang Liu. 2023. Jailbreaking chatgpt via prompt
engineering: An empirical study. arXiv preprint arXiv:2305.13860 (2023).
[27] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer
Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019. Roberta: A
robustly optimized bert pretraining approach. arXiv preprint arXiv:1907.11692
(2019).
[28] Yi Liu, Guowei Yang, Gelei Deng, Feiyue Chen, Yuqi Chen, Ling Shi, Tian-
wei Zhang, and Yang Liu. 2024.
Groot: Adversarial Testing for Gen-
erative Text-to-Image Models with Tree-based Semantic Transformation.
arXiv:2402.12100 [cs.CL] https://arxiv.org/abs/2402.12100
[29] Meta. 2023. "LLama-13B". https://github.com/facebookresearch/llama/tree/llama_
v1.
[30] OpenAI. 2023. "GPT-3.5 Turbo". https://platform.openai.com/docs/models/gpt-3-
5.
[31] OpenAI. 2023. "GPT-4". https://platform.openai.com/docs/models/gpt-4-and-
gpt-4-turbo.
[32] OpenAI. 2023.
Language models pricing.
https://web.archive.org/web/
20231031033745/https://openai.com/pricing.
[33] Fábio Perez and Ian Ribeiro. 2022. Ignore previous prompt: Attack techniques
for language models. arXiv preprint arXiv:2211.09527 (2022).
[34] Xinyue Shen, Zeyuan Chen, Michael Backes, Yun Shen, and Yang Zhang. 2023. "
do anything now": Characterizing and evaluating in-the-wild jailbreak prompts
on large language models. arXiv preprint arXiv:2308.03825 (2023).
[35] Hao Sun, Zhexin Zhang, Jiawen Deng, Jiale Cheng, and Minlie Huang. 2023. Safety
Assessment of Chinese Large Language Models. arXiv preprint arXiv:2304.10436
(2023).
[36] Yu Sun, Shuohuan Wang, Yukun Li, Shikun Feng, Hao Tian, Hua Wu, and Haifeng
Wang. 2020. Ernie 2.0: A continual pre-training framework for language under-
standing. In Proceedings of the AAAI conference on artificial intelligence, Vol. 34.
8968–8975.
[37] The Vicuna Team. 2023. "Vicuna-13B". https://github.com/lm-sys/FastChat.
[38] Eric Wallace, Shi Feng, Nikhil Kandpal, Matt Gardner, and Sameer Singh. 2019.
Universal Adversarial Triggers for Attacking and Analyzing NLP. In Proceedings
of the 2019 Conference on Empirical Methods in Natural Language Processing and
the 9th International Joint Conference on Natural Language Processing (EMNLP-
IJCNLP). Association for Computational Linguistics, Hong Kong, China, 2153–
2162. https://doi.org/10.18653/v1/D19-1221
[39] Alexander Wei, Nika Haghtalab, and Jacob Steinhardt. 2023. Jailbroken: How
does llm safety training fail? arXiv preprint arXiv:2307.02483 (2023).
[40] Zihao Xu, Yi Liu, Gelei Deng, Yuekang Li, and Stjepan Picek. 2024. A Compre-
hensive Study of Jailbreak Attack versus Defense for Large Language Models.
arXiv:2402.13457 [cs.CR] https://arxiv.org/abs/2402.13457
[41] Dongyu Yao, Jianshu Zhang, Ian G Harris, and Marcel Carlsson. 2023. Fuzzllm:
A novel and universal fuzzing framework for proactively discovering jailbreak
vulnerabilities in large language models. arXiv preprint arXiv:2309.05274 (2023).
[42] Jiahao Yu, Xingwei Lin, and Xinyu Xing. 2023.
Gptfuzzer: Red teaming
large language models with auto-generated jailbreak prompts. arXiv preprint
arXiv:2309.10253 (2023).
[43] Youliang Yuan, Wenxiang Jiao, Wenxuan Wang, Jen-tse Huang, Pinjia He, Shum-
ing Shi, and Zhaopeng Tu. 2023. Gpt-4 is too smart to be safe: Stealthy chat with
llms via cipher. arXiv preprint arXiv:2308.06463 (2023).
[44] Terry Yue Zhuo, Yujin Huang, Chunyang Chen, and Zhenchang Xing. 2023. Ex-
ploring ai ethics of chatgpt: A diagnostic analysis. arXiv preprint arXiv:2301.12867
(2023).
[45] Andy Zou, Zifan Wang, J Zico Kolter, and Matt Fredrikson. 2023. Universal
and transferable adversarial attacks on aligned language models. arXiv preprint
arXiv:2307.15043 (2023).
Received 2024-04-12; accepted 2024-07-03

```
