---
title: "Understanding How Value Neurons Shape the - PDF Extract"
source_pdf: "2025-Su-Understanding How Value Neurons Shape the.pdf"
pages: 20
extracted_at: "2026-01-24T16:38:36.585593"
---

# PDF Extract: Understanding How Value Neurons Shape the

**Source PDF:** 2025-Su-Understanding How Value Neurons Shape the.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

arXiv:2505.17712v1  [cs.CL]  23 May 2025
Understanding How Value Neurons Shape the Generation of Specified
Values in LLMs
Yi Su*,1,2, Jiayi Zhang*,1,3, Shu Yang†,1,2, Xinhai Wang1,2, Lijie Hu†,1,2, Di Wang1,2
1Provable Responsible AI and Data Analytics (PRADA) Lab
2King Abdullah University of Science and Technology
3University of Copenhagen
Abstract
Rapid integration of large language models
(LLMs) into societal applications has intensi-
fied concerns about their alignment with univer-
sal ethical principles, as their internal value rep-
resentations remain opaque despite behavioral
alignment advancements. Current approaches
struggle to systematically interpret how val-
ues are encoded in neural architectures, lim-
ited by datasets that prioritize superficial judg-
ments over mechanistic analysis. We intro-
duce ValueLocate, a mechanistic interpretabil-
ity framework grounded in the Schwartz Values
Survey, to address this gap. Our method first
constructs ValueInsight, a dataset that opera-
tionalizes four dimensions of universal value
through behavioral contexts in the real world.
Leveraging this dataset, we develop a neuron
identification method that calculates activation
differences between opposing value aspects,
enabling precise localization of value-critical
neurons without relying on computationally in-
tensive attribution methods. Our proposed vali-
dation method demonstrates that targeted ma-
nipulation of these neurons effectively alters
model value orientations, establishing causal
relationships between neurons and value repre-
sentations. This work advances the foundation
for value alignment by bridging psychologi-
cal value frameworks with neuron analysis in
LLMs.
1
Introduction
Recent years have seen unprecedented advances in
large language models (LLMs), establishing them
as indispensable tools across multiple societal do-
mains (Yang et al., 2025; Yao et al., 2024; Park
et al., 2023; Yang et al., 2024c). However, their
extensive adoption raises critical concerns about
value, as these systems demonstrate persistent chal-
lenges in adhering to universal ethical principles.
*Equal Contribution. The order of these two authors fol-
lows alphabetical order of their last names.
†Corresponding Author
This challenge stems primarily from their funda-
mental architecture: LLMs trained in data sourced
from the Internet inherently absorb and display
biases, ideological variances, and cultural speci-
ficities present in their training corpora. LLMs
weighing values quite differ from human (Nie et al.,
2023), give different priorities for different value di-
mensions (Liu et al., 2025), exhibit diverse ideolo-
gies (Buyl et al., 2024), and present nation-specific
social values (Lee et al., 2024). Although con-
temporary alignment techniques have made sub-
stantial progress in the behavioral adjustment re-
lated to value (Kong et al., 2024; Kenton et al.,
2021; Ouyang et al., 2022; Yang et al., 2024b;
Zhang et al., 2025a), the inner mechanisms re-
garding value representation are not clearly inter-
preted. Systematic investigation of these latent
value-encoding mechanisms could enable the devel-
opment of theoretically grounded alignment frame-
works and facilitate the design of more robust align-
ment algorithms in a principled way.
Our study presents a novel mechanistic inter-
pretability (MI) framework to systematically an-
alyze value representation in neural architectures.
MI, defined as reverse engineering of neural compu-
tations into interpretable algorithmic components
(Elhage et al., 2021), traditionally includes attribut-
ing a model function to specific model components
(e.g., neurons) and verifying that localized compo-
nents have causal effects on model behaviors with
causal mediation analysis techniques such as activa-
tion patching (Zhang et al., 2024; Vig et al., 2020;
Meng et al., 2022). Previous studies (Dai et al.,
2022; Geva et al., 2021; Yu and Ananiadou, 2024a;
Zhang et al., 2025c; Hong et al., 2024) demonstrate
that neurons could serve as fundamental computa-
tional units for knowledge storage in LLM, suggest-
ing that the precise identification of value-critical
neurons may allow targeted editing. However, due
to the current limitations in the benchmark datasets
on the LLM values, we cannot directly adopt them
1

--- Page 2 ---

to identify value-related neurons. Specifically, the
existing datasets are all based on decision-making
judgments (Liu et al., 2025) or binary yes/no judg-
ments (Nie et al., 2023) to evaluate neurons, which
often introduce biases or yield inaccurate results, as
they primarily reveal the model’s understanding of
values rather than their actual orientation to these
principles (Yao et al., 2025). This will lead to an
insufficient understanding of its mechanism and
storage location.
In this paper, we introduce a neuron-based ap-
proach called ValueLocate to tackle the afore-
mentioned issues.
Our method is rooted in
the Schwartz Values Survey (Schwarz, 1992),
a well-established framework that classifies val-
ues into four distinct dimensions: Openness to
Change, Self-transcendence, Conservation, and
Self-enhancement. Using these four value types,
we develop a dataset named ValueInsight, which
serves as a valuable tool to locate value-related neu-
rons within LLMs. Unlike existing related datasets
mainly in the multichoice format (Scherrer et al.,
2024), ValueInsight offers a distinct approach, per-
forming generative value tasks in LLMs using real-
world test cases. The dataset enables the generation
of contextually appropriate responses that maintain
persistent alignment with specific values in various
application contexts.
We then leverage ValueInsight to locate neu-
rons associated with values. To identify neurons,
previous work always considers the activation de-
gree (Zhu et al., 2024) or leverages existing feature
attribution methods in explainable AI (Leng and
Xiong, 2024; Tang et al., 2024; Zhang et al., 2025b).
However, feature attribution methods always need
high computing resources. From the Schwartz Val-
ues Survey, we find that value-related factors gener-
ally correspond to two opposite aspects. Therefore,
we propose an activation degree-based method by
calculating the activation difference when analyz-
ing the opposite aspects of a particular value. More-
over, to validate the causality between the identi-
fied neurons and the values by adjusting the neu-
rons, previous work always deactivates the specific
neurons (Li et al., 2025). However, this approach
cannot be applied to value-related neurons as deac-
tivation will be meaningless. To address this issue,
we propose a method that aims to manipulate and
edit the values by changing the activations of value-
related neurons.
In summary, our research aims to provide a
mechanistic understanding of the value encoded
in LLMs. Our work makes three key contributions:
• New dataset for value evaluation: We con-
structed ValueInsight, a new dataset compris-
ing 640 second-person value descriptions and
15,000 scenario-based open-ended questions,
each tailored to the values defined in the
Schwartz Values Survey.
• Identification of neurons: Using ValueInsight,
we propose ValueLocate to identify neurons in
LLMs that are associated with specific values.
Instead of relying on a one-sided analysis, our
method takes both the positive and negative
aspects of a single value into account.
• Comprehensive analysis: To validate the ef-
fectiveness of our neuron identification ap-
proach, we propose a new method to manip-
ulate and edit values by changing the activa-
tions of value-related neurons. We conducted
extensive experiments on different LLMs that
evaluated the value of LLMs before and after
value-related neuron manipulation. The re-
sults confirm that our method can effectively
locate neurons related to values.
2
Related work
Values in LLMs.
As the popularity of LLMs
increases, the values encoded within them have
drawn significant attention. Pre-trained LLMs in-
herently exhibit value biases that frequently mis-
align with human norms, prioritizing mainstream
cultural perspectives over minority viewpoints,
and showing inconsistent performance across lan-
guages (Wang et al., 2025; Cao et al., 2023). LLMs
risk propagating misinformation and harmful con-
tent, potentially exacerbating societal harms (Desh-
pande et al., 2023; Yang et al., 2024d), which threat-
ens both ethical LLM development and user trust.
To align LLM values with humans, many methods
have been proposed (Ziegler et al., 2019; Kenton
et al., 2021; Ouyang et al., 2022).
Multiple benchmarks, such as ValueBench (Ren
et al., 2024) (psychometric analysis), CIVICS (Pis-
tilli et al., 2024) (sociocultural rating tasks), and
MoCa (Nie et al., 2023) (moral dilemma narra-
tives), aim to quantify value orientations. However,
as we mentioned, overreliance on simplistic for-
mats (e.g., multiple-choice questions) limits their
capacity to capture nuanced biases. To address
this issue, we introduce a new dataset for value
evaluation.
2

--- Page 3 ---

Neuron-based
Mechanistic
Interpretability.
Recent studies have found that neurons in neural
networks serve as critical repositories of the
knowledge encoded during the model training
process (Geva et al., 2021).
The feedforward
network (FFN) layers have been shown to store
substantial information, where targeted neuronal
editing can significantly alter the behavioral pat-
terns and reasoning mechanisms of LLMs (Elhage
et al., 2021). This foundational understanding of
neuron-level manipulation has enabled various
practical applications, with multiple investigations
that focus on identifying related neurons and
modifying model behavior through FFN memory
adjustments.
Notable implementations include
localization of safety neurons (Chen et al., 2024a),
identification of language-specific neurons (Tang
et al., 2024), gender-biased neurons editing (Yu and
Ananiadou, 2025), identification and manipulation
of personality-related neurons (Deng et al., 2024;
Yang et al., 2024d), precise factual knowledge
editing (Meng et al., 2022) and batch memory
insertion techniques (Meng et al., 2023). Unlike
previous research, we have developed a method
applicable to LLMs that deciphers the mechanism
of their value orientations, significantly improving
both practicality and efficacy in value-related
neuron analysis.
3
ValueInsight Construction
In this section, we present the details of the con-
struction process for our generative benchmark,
ValueInsight. It comprises 15,000 instances for
neuron identification, with an average of 3,750 in-
stances for each high-order dimension value and
300 instances for each atomic value. This bench-
mark serves as a standardized instrument designed
to assess the values manifested by LLMs. We base
the design of ValueInsight on the theoretical frame-
work provided by the Schwartz Values Survey
(Schwarz, 1992), which offers a well-established
categorization of value factors, forming the bedrock
of our dataset creation. See Appendix B for a de-
tailed introduction. Each item within our dataset is
structured as a pair consisting of a value descrip-
tion and a corresponding situational question. We
define situational questions as concise, context-rich
prompts that describe everyday scenarios in which
individuals must make decisions or take actions
that potentially reflect underlying values. Subse-
quently, we will provide the details of how the
value descriptions and situational questions were
generated. See Figure 1 for an illustration.
Value Description Generation. We generate value
descriptions based on the Schwartz Values Sur-
vey.
Universal values are hierarchically struc-
tured and divided into four higher-order dimensions
D = {Openness to Change, Self-Transcendence,
Conservation, Self-Enhancement}. Each dimen-
sion d ∈D decomposes into subvalues Sd and
atomic values As, forming a tree Γ = (D, S, A),
where S = S
d∈D Sd and A = S
s∈S As. For ex-
ample, under the Openness to Change value dimen-
sion, subvalues include Self-Direction, Stimulation,
and Hedonism, with atomic values such as Creativ-
ity and Freedom nested within Self-Direction. In
detail, these values D, subvalues Sd, and atomic
values As can be found in Appendix B.1.
Generation of Value Descriptions. To generate
value descriptions, we systematically leverage the
hierarchical structure of core values and their asso-
ciated subvalues. Specifically, we utilize GPT-4o to
create concise second-person narratives that opera-
tionalize each value dimension. For all the values
listed above, we incorporate their opposing value
orientations ¯
As. Initially, we automatically pro-
duce baseline descriptions Bd for each dimension
d using the templated prompt in Table A, corre-
sponding to all (s, a) ∈Sd × (As ∪¯
As). Subse-
quently, we manually refine Bd to ensure concep-
tual clarity and linguistic naturalness, resulting in
curated descriptions Rd. Using Rd as exemplars
and the prompt in Table A, we generate additional
descriptions by iteratively rephrasing a ∈As ∪¯
As,
ensuring coverage of various value expressions.
Generation of Situational Questions. Based on
the generated value descriptions, we produce a
set of situational questions that are carefully de-
signed to evoke distinct responses from individuals
with different value systems. Traditional evalu-
ation questionnaires, such as PVQ40 (Schwartz
et al., 2001), often do not capture meaningful value
tendencies. For example, a PVQ40 item such as “It
is important to her to be rich. She wants to have a
lot of money and expensive things.” could lead to
similar surface-level responses or prompt an LLM
to assign a score; however, it fails to uncover the
underlying value orientations.
To overcome these limitations, we develop a
series of questions grounded in real-world behav-
ior. These questions are customized to highlight
value-related actions.
Specifically, we use As
as a basis to create situational questions that re-
3

--- Page 4 ---

Positive value description: 
Openness_to_Change (You 
thrive in situations where you 
can make your own choices. 
Being able to decide what 
happens next makes you feel 
truly alive...)
Negative value description: 
Openness_to_Change_reversed 
? You prefer having a clear, 
structured path where you 
don?t have to make too many 
decisions. Knowing what?s 
coming next gives you a sense 
of control...)
Subvalue: 
Curious
topic: 
Travel and adventure
Situational question:
You are on a cruise that offers a variety 
of excursions at each port. One of the 
excursions is a visit to a local village that 
is rarely visited by tourists, offering a 
chance to learn about traditional customs 
and lifestyles. However......
Answer:
Choosing unique and less-traveled experiences 
is what makes a journey truly memorable. I value 
the sense of autonomy that comes with deciding 
to step off the beaten path. Sure, the popular 
excursions are easier and more predictable, but 
they don?t offer the same sense of discovery and 
connection with a place that feels untouched. 
The traditional village,  ...
Answer:
I appreciate knowing exactly what to expect, so 
the conventional, more popular excursions are 
definitely more appealing to me. They offer a clear, 
structured path with less uncertainty. I know the 
itinerary, I know the cost, and I can mentally 
prepare for what?s coming. The longer, more 
expensive...
ValueInsight  Construction
ValueInsight  
Usage
generate 
value 
description
generate 
situational 
question
refine 
situational 
question
answer question
Figure 1: ValueInsight Construction and Usage
flect a wide variety of real-life behaviors. To fur-
ther enrich our set of questions, we incorporate
common topics of life T from UltraChat (Ding
et al., 2023), including family, environment, and
arts. To generate these situational questions, we
use specially formulated prompts P for GPT-4o.
These prompts are designed to facilitate the gen-
eration of complex scenarios that involve moral
dilemmas, competing priorities, or difficult deci-
sions. Each question q ∈Q is generated through
q = f(P(a, t)), a ∈As, t ∈T, f denotes the
model API call. After generating the questions,
we further refine them with the help of GPT-4o.
This refinement process involves checking for po-
tential moral or emotional biases such as an overly
judgmental tone, culturally sensitive implications,
or emotionally charged phrasing that may inadver-
tently influence LLM interpretations or responses.
These adjustments are necessary to ensure that the
questions remain neutral, inclusive, and aligned
with the intended focus on value-related behav-
iors, rather than eliciting responses shaped by un-
intended normative or affective cues.
Detailed
prompts used in this process are presented in Sec-
tion A.
4
Identifying Value-related Neurons
To precisely localize value-related neurons, we pro-
pose ValueLocate, an activation contrast frame-
work that compares neuron activations in re-
sponse to prompts reflecting opposing value types.
Our methodology initiates by constructing well-
designed prompts (see Section A) and using the
contrastive value description in the ValueInsight
dataset, which elicits latent value representations
through semantically polarized contexts. We first
review the definition of neurons in transformers.
Definition of Neurons. In the middle of the em-
bedding and unembedding layers of transformer-
based language models, there is a series of trans-
former blocks. Each transformer block consists of
a multi-head attention (MHA) and a feedforward
network (FFN)(Geva et al., 2021; Vaswani et al.,
2017). Formally, for an input T token sequence
x = [x1, x2, ..., xT ], the computation performed
by each transformer block is a refinement of the
residual stream (Elhage et al., 2021):
hl
i = hl−1
i
+ Al
i + F l
i ,
(1)
where hl
i denotes the output on layer l, position i,
Al
i represents the output of the self-attention layer
from multiple heads and F l
i is the output of the FFN
layer. The FFN output is calculated by applying
a non-linear activation function σ on two Dense
layers W l
1 and W l
2:
F l
i = W l
2σ(W l
1(hl−1
i
+ Al
i)),
(2)
In this context, a neuron is conceptualized as the
combination of the k -th row of W l
1 and the k-th
column of W l
2 (Yu and Ananiadou, 2025).
Value Related Neuron Identification. To iden-
tify value-related neurons, we employ differential
causal mediation analysis. See Figure 2 for an
overview. Giving a value orientation through the
use of descriptions representing a target value or
4

--- Page 5 ---

Figure 2: Mainstream process of ValueLocate
its reversed counterpart in ValueInsight, we prompt
LLM to answer situational questions accordingly.
During this process, we calculate the neuron acti-
vation value ml
k for an input sequence x of length
T:
ml
k =
T
X
i=1
σ(W l
1k · (hl−1
i
+ Al
i)),
(3)
where W l
1k is the k-th row of W l
1.
Given N input sequences, each comprising a de-
scription and a corresponding situational question
centered on a specific value dimension, the activa-
tion probability pl,k is computed as the empirical
expectation across all prompts:
pl,k = 1
N
N
X
n=1
I(ml
k > 0),
(4)
where I is the indicator function. The dual nature
of values refers to the opposing dimensions repre-
sented by a target value (e.g., Conservation) and its
reversed counterpart (e.g., Conservation_reversed).
This duality allows the measurement of neuronal
activation differences between opposing value di-
mensions:
δ = p+
l,k −p−
l,k,
(5)
where p+
l,k and p−
l,k denote the activation probabil-
ity of neuron computed from prompts containing
the target value description (positive value) and its
reversed counterpart (negative value), respectively.
To delineate value-related neurons, we imple-
mented an activation difference threshold.
We
chose a value threshold of 3% as our experiments
in Section 6.3 show that it marks the point where
the value score remains relatively high while the
text quality stabilizes. Neurons with δ exceeding
3% are operationally defined as controlling the pos-
itive aspect of the value type, while those with δ
magnitudes below -3% are classified as controlling
the opposite value type. This classification method
clearly identifies neurons that strongly affect spe-
cific values in either direction.
5
Validating Value-related Neurons
Previous studies (Dai et al., 2022; Meng et al.,
2022) suggest that the magnitude of neuron activa-
tion reflects its contribution to the LLM response.
To verify the causality between value-related neu-
rons we found in the previous section and LLM
values, we designed a neuron editing method.
Our proposed method aims to edit the value by
changing the activations of value-related neurons,
thus verifying their effectiveness. To steer value
orientations toward positive directions, we amplify
the activations of neurons corresponding to pos-
itive values while suppressing the negative ones,
maintaining the activations of other neutral neu-
rons. The amplification is governed by a dynamic
scaling factor γ. The modified activations for each
neuron can be formulated as follows:
αl
k =





min(0, ml
k),
δ ≤−3%
ml
k,
−3% < δ < 3%
ml
k · (1 + δ · γ),
δ ≥3%
(6)
To induce a negative shift in the LLM value sys-
tem, we invert the conditions in (6), suppressing
positively associated neurons while amplifying neg-
atively associated ones.
5

--- Page 6 ---

6
Experiments
6.1
Experimental Setup
Datasets. During the evaluation phase, we select
100 questions related to each of the four higher-
order value dimensions defined in the Schwartz
Values Survey: Openness to Change, Conserva-
tion, Self-Enhancement, and Self-Transcendence
from the ValueInsight dataset. To further ensure
that the value orientations of the LLMs change
after manipulating the value-related neurons, we
supplement our analysis with evaluations on exist-
ing value-related datasets, including the PVQ40
questionnaire (Schwartz et al., 2001) and the Val-
ueBench dataset (Ren et al., 2024), see Appendix
C for a detailed introduction.
Baselines. For comparison, we consider several
previous methods for identifying neurons. Note
that these methods are not designed for finding
value-related neurons. The details of the baselines
are presented in Appendix D.
• LPIP: Locating neurons using Log Probabil-
ity and Inner Products (Yu and Ananiadou,
2024b).
• QRNCA: Identifying neurons by Query-
Relevant Neuron Cluster Attribution (Chen
et al., 2024b).
• CGVST: Causal Gradient Variation with Spe-
cial Tokens (Song et al., 2024), a method that
identifies specific neurons by concentrating on
the most significant tokens during processing.
Models.
We primarily choose LLama-3.1-
8B (Dubey et al., 2024) as the base model to carry
out our experiments, selected for its demonstrated
proficiency in instruction adherence and contex-
tual reasoning capabilities. Its strong capabilities
and excellent adaptation to various tasks make it
an ideal base model for our studies. To compre-
hensively investigate the value-related neurons in a
more realistic setting and rigorously validate the ef-
fectiveness and compatibility of our methodology,
we also consider other LLMs, including Qwen2-
0.5B (Yang et al., 2024a), LLama-3.2-1B (Dubey
et al., 2024), and gemma-2-9B (Team et al., 2024).
Evaluation Metric. Our evaluation leverages the
G-EVAL (Liu et al., 2023) metric to quantify value
alignment in responses generated by prompting
LLMs (see Section A). It uses multidimensional
relevance scoring on a scale of 1 to 5 under both
original and manipulated neural conditions. The
methodology combines chain-of-thought reasoning
with a structured form-filling paradigm. This score
reflects the relevance to a specific value dimension
in the Schwartz Values Survey, with higher scores
indicating a stronger presence of that value. A
detailed description of the metric is provided in
Appendix E. For each response, the final score is
obtained by averaging the results of 10 independent
runs of G-EVAL.
6.2
Experimental Results
Performance Comparison. We calculate the av-
erage score for 10 runs evaluated by G-EVAL and
validate in three datasets after amplifying the ac-
tivations of positive neurons (with γ set to 2.0)
and suppressing negative ones. As shown in Ta-
ble 1, Table 2 and Table 3, for all datasets, Val-
ueLocate outperforms all baselines in identifying
value-related neurons, achieving the highest scores
in most cases. This indicates that our identified neu-
rons significantly affect the value orientations in
LLM. Only in gemma-2-9B, CGVST outperformed
ValueLocate in the Self-Enhancement dimension.
This is because, in Schwartz’s value theory, Self-
Enhancement and Openness to Change exhibit se-
mantic overlap with Enjoying life, belonging to
both dimensions. CGVST captures specific be-
havioral tendencies directly through gradient varia-
tions of special tokens, thereby avoiding confusion
caused by abstract value representations.
To further validate that ValueLocate accurately
identifies value-related neurons, we make negative
adjustments by amplifying the activations of neg-
ative neurons (with γ set to 2.0) and suppressing
positive ones. The results are presented in Ap-
pendix Table 4, Table 5 and Table 6, showing that
ValueLocate still outperforms the other baselines,
evidenced by its generally lowest scores after re-
verse adjustment. This further demonstrates that
the neurons we identified are more closely related
to values compared to those identified by other
baselines. The only sub-optimal result still appears
in the Self-Enhancement dimension, which is in-
fluenced by the semantic overlap with Openness
to Change. In such cases, CGVST can sometimes
better avoid confusion caused by abstract value
representations.
Distribution of Neurons. Furthermore, we an-
alyze the distribution of neurons associated with
values. Although each layer of LLama-3.1-8B con-
sists of 14,336 neurons, as shown in Figure 4, we
6

--- Page 7 ---

(a) LLama-3.1-8B (Positive)
(b) LLama-3.1-8B (Negative)
(c) LLama-3.1-8B (Random)
(d) Gemma-2-9B (Positive)
(e) Gemma-2-9B (Negative)
(f) Gemma-2-9B (Random)
Figure 3: Results of positively and negatively editing the neurons identified by ValueLocate, as well as editing
randomly selected neurons, on LLama-3.1-8B and Gemma-2-9B.
found that less than 0.4% of them are related to
values, demonstrating that value orientations are
significantly influenced by a small subset of neu-
rons. In particular, most value-related neurons are
located in the middle layers, around the 15th layer,
and this phenomenon holds consistently across all
four value dimensions. For the other three models,
the neuron distributions can be found in Appendix
Figure 7, Figure 9, and Figure 8. A consistent pat-
tern across different models is that value-related
neurons are sparse in each layer, and the neuron
distribution patterns show cross-dimensional align-
ment across Schwartz’s four value orientations.
Figure 4: LLama-3.1-8B Neuron Distribution
Validating Value-related Neurons. Finally, we
select 10, 20, 30, 40 and 50 value-related neurons
from each of the four value dimensions and modify
their activations with the adjustment magnitude γ
set to 2.0. For each setting, we computed the value-
related scores after neuron modification. As a con-
trol, we performed the same manipulations on an
equal number of randomly selected neurons. The
results are presented in Figure 5, Figure 13, Figure
14 and Figure 15. As shown, increasing the number
of value-related neurons that are edited leads to a
consistent and significant increase in value-related
scores. In contrast, editing randomly selected neu-
rons, regardless of quantity, does not produce a
substantial change in scores. These findings pro-
vide strong evidence that the neurons identified are
indeed meaningfully associated with value repre-
sentations in the Schwartz Values Survey.
Figure 5: Impact of Value-Related Neuron and Random
Neuron Manipulation on LLama-3.1-8B
6.3
Ablation Study
To validate our method for identifying value-related
neurons, in this section, we conduct ablation exper-
iments by examining the effect of manipulating the
selected neurons.
Effect of the Dynamic Scaling Factor. We first
set the neuron difference threshold to 3% and in-
vestigate the effect of the dynamic scaling factor γ.
As shown in Figure 3 and Figure 16, increasing the
γ value, corresponding to a higher magnitude of
neuron modification, consistently leads to higher
evaluation scores across the four value dimensions,
7

--- Page 8 ---

Table 1: G-EVAL average scores and variance on ValueInsight for neuron identification methods after positive
neuron editing (γ = 2.0). Bold values indicate the best results.
Methods
Openness to Change
Self-Transcendence
Conservation
Self-Enhancement
LLama-3.1-8B
LPIP
4.20 ± 0.07
4.30 ± 0.09
3.65 ± 0.14
3.82 ± 0.12
QRNCA
4.35 ± 0.11
4.15 ± 0.10
3.72 ± 0.10
3.75 ± 0.09
CGVST
4.42 ± 0.09
4.25 ± 0.07
3.85 ± 0.07
3.88 ± 0.06
ValueLocate
4.68 ± 0.06
4.60 ± 0.05
4.15 ± 0.09
4.08 ± 0.06
Qwen2-0.5B
LPIP
4.05 ± 0.08
4.10 ± 0.15
3.85 ± 0.11
3.92 ± 0.09
QRNCA
4.18 ± 0.07
4.25 ± 0.08
3.95 ± 0.07
3.85 ± 0.08
CGVST
4.28 ± 0.06
4.35 ± 0.09
4.05 ± 0.06
3.95 ± 0.07
ValueLocate
4.80 ± 0.05
4.65 ± 0.06
4.18 ± 0.08
4.15 ± 0.07
LLama-3.2-1B
LPIP
4.35 ± 0.09
4.40 ± 0.18
3.95 ± 0.10
3.95 ± 0.09
QRNCA
4.45 ± 0.07
4.50 ± 0.09
4.12 ± 0.08
3.88 ± 0.07
CGVST
4.52 ± 0.06
4.55 ± 0.05
4.22 ± 0.07
4.05 ± 0.06
ValueLocate
4.65 ± 0.05
4.65 ± 0.04
4.22 ± 0.06
4.22 ± 0.05
gemma-2-9B
LPIP
4.15 ± 0.10
4.65 ± 0.07
3.95 ± 0.09
3.95 ± 0.08
QRNCA
4.25 ± 0.08
4.45 ± 0.06
4.08 ± 0.07
3.85 ± 0.07
CGVST
4.45 ± 0.07
4.38 ± 0.08
4.05 ± 0.06
4.32 ± 0.05
ValueLocate
4.55 ± 0.06
4.78 ± 0.04
4.35 ± 0.05
4.28 ± 0.06
as measured by G-EVAL. This pattern holds for
both positive and negative manipulations, with pos-
itive modifications enhancing value alignment and
negative modifications reducing it. These obser-
vations suggest a strong, monotonic relationship
between the degree of neuron activation and the
model’s expressed value orientations, further sup-
porting the causal influence of identified neurons
on value representation.
To further validate that the identified neurons
accurately and effectively determine the LLM’s
target value orientations, under the same setting,
we additionally apply the same manipulations to
randomly selected neurons. Although targeted ma-
nipulations consistently led to systematic increases
or decreases in value orientation scores, random
manipulations did not produce significant changes.
This contrast confirms both the precision and ef-
fectiveness of the identified neurons in governing
the model’s value representations, providing strong
evidence of a causal relationship.
Effect of the Difference Threshold. Finally, we
study the effect of the neuron difference thresh-
old δ on LLama-3.1-8B. Intuitively, as δ increases,
fewer neurons are edited and LLM value orienta-
tion scores decrease, but this comes with a signifi-
cant improvement in text quality. Keeping all other
conditions constant and setting γ to 2.0, we investi-
gate how variations in the activation probability dif-
ference threshold for neuron selection affect both
Figure 6: How threshold influences the result on LLama-
3.1-8B for Openness to Change
the value orientation scores and the text quality.
Text quality is evaluated using GPT-4o, with scores
ranging from 1 to 5, as described in the evaluation
prompt provided in Section A. Figure 6 illustrates
the results for Openness to Change, with similar
trends observed in the other three value dimensions
in Figure 10, Figure 11, and Figure 12. The results
confirm our intuition, leading us to choose a thresh-
old of 0.03, as it represents the point where text
quality stabilizes while maintaining relatively high
value scores.
7
Conclusions
This paper introduces ValueLocate to identify
value-related neurons in LLMs by measuring acti-
vation differences between opposing aspects of a
given value. To enhance neuron identification, we
constructed ValueInsight, a dataset of 640 second-
8

--- Page 9 ---

person value descriptions and 15,000 scenario-
based questions designed to uncover the value ori-
entation based on the Schwartz Values Survey. Ex-
periments on four LLMs consistently outperform
baselines, demonstrating the effectiveness of Val-
ueLocate.
Limitations
Our method has several limitations.
The four
higher-order value dimensions in the Schwartz Val-
ues Survey are not entirely independent; for ex-
ample, both Self-Enhancement and Openness to
Change include the value "Enjoying life." Rely-
ing on this as a theoretical foundation for evaluat-
ing value dimensions may lead to inaccuracies in
some cases. Furthermore, our experiments were
conducted on only four LLMs, potentially requir-
ing adaptations for other architectures. Moreover,
our evaluation focuses solely on value orientation,
neglecting factors such as language fluency, text
coherence, factual response, and logical reason-
ing. Nevertheless, we believe our work provides
valuable insights and represents a meaningful step
forward in understanding and editing value-related
neurons in LLMs.
References
Maarten Buyl, Alexander Rogiers, Sander Noels, Guil-
laume Bied, Iris Dominguez-Catena, Edith Heiter,
Iman Johary, Alexandru-Cristian Mara, Raphaël
Romero, Jefrey Lijffijt, et al. 2024. Large language
models reflect the ideology of their creators. arXiv
preprint arXiv:2410.18417.
Yong Cao, Li Zhou, Seolhwa Lee, Laura Cabello, Min
Chen, and Daniel Hershcovich. 2023.
Assessing
cross-cultural alignment between chatgpt and human
societies: An empirical study. Cross-Cultural Con-
siderations in NLP@ EACL, page 53.
Jianhui Chen, Xiaozhi Wang, Zijun Yao, Yushi Bai,
Lei Hou, and Juanzi Li. 2024a.
Finding safety
neurons in large language models. arXiv preprint
arXiv:2406.14144.
Lihu Chen, Adam Dejl, and Francesca Toni. 2024b.
Analyzing key neurons in large language models.
arXiv preprint arXiv:2406.10868.
Damai Dai, Li Dong, Yaru Hao, Zhifang Sui, Baobao
Chang, and Furu Wei. 2022. Knowledge neurons in
pretrained transformers. In Proceedings of the 60th
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 8493–
8502.
Jia Deng, Tianyi Tang, Yanbin Yin, Wenhao Yang,
Wayne Xin Zhao, and Ji-Rong Wen. 2024. Neuron-
based personality trait induction in large language
models. arXiv preprint arXiv:2410.12327.
Ameet Deshpande, Vishvak Murahari, Tanmay Rajpuro-
hit, Ashwin Kalyan, and Karthik Narasimhan. 2023.
Toxicity in chatgpt: Analyzing persona-assigned lan-
guage models. In Findings of the Association for
Computational Linguistics: EMNLP 2023, pages
1236–1270.
Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin,
Shengding Hu, Zhiyuan Liu, Maosong Sun, and
Bowen Zhou. 2023. Enhancing chat language models
by scaling high-quality instructional conversations.
In Proceedings of the 2023 Conference on Empiri-
cal Methods in Natural Language Processing, pages
3029–3051.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, et al. 2024. The llama 3 herd of models. arXiv
preprint arXiv:2407.21783.
Nelson Elhage, Neel Nanda, Catherine Olsson, Tom
Henighan, Nicholas Joseph, Ben Mann, Amanda
Askell, Yuntao Bai, Anna Chen, Tom Conerly, et al.
2021. A mathematical framework for transformer
circuits. Transformer Circuits Thread, 1(1):12.
Mor Geva, Roei Schuster, Jonathan Berant, and Omer
Levy. 2021. Transformer feed-forward layers are
key-value memories. In Proceedings of the 2021
Conference on Empirical Methods in Natural Lan-
guage Processing, pages 5484–5495.
Yihuai Hong, Yuelin Zou, Lijie Hu, Ziqian Zeng,
Di Wang, and Haiqin Yang. 2024. Dissecting fine-
tuning unlearning in large language models. In Pro-
ceedings of the 2024 Conference on Empirical Meth-
ods in Natural Language Processing, pages 3933–
3941.
Zachary Kenton, Tom Everitt, Laura Weidinger, Ia-
son Gabriel, Vladimir Mikulik, and Geoffrey Irving.
2021. Alignment of language agents. arXiv preprint
arXiv:2103.14659.
Keyi Kong, Xilie Xu, Di Wang, Jingfeng Zhang, and
Mohan S Kankanhalli. 2024. Perplexity-aware cor-
rection for robust alignment with noisy preferences.
Advances in Neural Information Processing Systems,
37:28296–28321.
Jiyoung Lee, Minwoo Kim, Seungho Kim, Junghwan
Kim, Seunghyun Won, Hwaran Lee, and Edward
Choi. 2024. Kornat: Llm alignment benchmark for
korean social values and common knowledge. arXiv
preprint arXiv:2402.13605.
Yongqi Leng and Deyi Xiong. 2024. Towards under-
standing multi-task learning (generalization) of llms
via detecting and exploring task-specific neurons.
arXiv preprint arXiv:2407.06488.
9

--- Page 10 ---

Tianlong Li, Zhenghua Wang, Wenhao Liu, Muling Wu,
Shihan Dou, Changze Lv, Xiaohua Wang, Xiaoqing
Zheng, and Xuan-Jing Huang. 2025. Revisiting jail-
breaking for large language models: A representation
engineering perspective. In Proceedings of the 31st
International Conference on Computational Linguis-
tics, pages 3158–3178.
Xuelin Liu, Pengyuan Liu, and Dong Yu. 2025. What’s
the most important value? invp: Investigating the
value priorities of llms through decision-making in
social scenarios. In Proceedings of the 31st Inter-
national Conference on Computational Linguistics,
pages 4725–4752.
Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang,
Ruochen Xu, and Chenguang Zhu. 2023. G-eval:
Nlg evaluation using gpt-4 with better human align-
ment. arXiv preprint arXiv:2303.16634.
Kevin Meng, David Bau, Alex Andonian, and Yonatan
Belinkov. 2022. Locating and editing factual associ-
ations in gpt. Advances in Neural Information Pro-
cessing Systems, 35:17359–17372.
Kevin Meng, Arnab Sen Sharma, Alex J Andonian,
Yonatan Belinkov, and David Bau. 2023.
Mass-
editing memory in a transformer. In The Eleventh
International Conference on Learning Representa-
tions.
Allen Nie, Yuhui Zhang, Atharva Shailesh Amdekar,
Chris Piech, Tatsunori B Hashimoto, and Tobias Ger-
stenberg. 2023. Moca: Measuring human-language
model alignment on causal and moral judgment tasks.
Advances in Neural Information Processing Systems,
36:78360–78393.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback. Advances in neural in-
formation processing systems, 35:27730–27744.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Mered-
ith Ringel Morris, Percy Liang, and Michael S Bern-
stein. 2023. Generative agents: Interactive simulacra
of human behavior. In Proceedings of the 36th an-
nual acm symposium on user interface software and
technology, pages 1–22.
Giada Pistilli, Alina Leidinger, Yacine Jernite, Atoosa
Kasirzadeh, Alexandra Sasha Luccioni, and Margaret
Mitchell. 2024. Civics: Building a dataset for exam-
ining culturally-informed values in large language
models. arXiv preprint arXiv:2405.13974.
Yuanyi Ren, Haoran Ye, Hanjun Fang, Xin Zhang, and
Guojie Song. 2024. Valuebench: Towards compre-
hensively evaluating value orientations and under-
standing of large language models. arXiv preprint
arXiv:2406.04214.
Nino Scherrer, Claudia Shi, Amir Feder, and David Blei.
2024. Evaluating the moral beliefs encoded in llms.
Advances in Neural Information Processing Systems,
36.
Shalom H Schwartz, Gila Melech, Arielle Lehmann,
Steven Burgess, Mari Harris, and Vicki Owens. 2001.
Extending the cross-cultural validity of the theory
of basic human values with a different method of
measurement. Journal of cross-cultural psychology,
32(5):519–542.
Shalom H Schwarz. 1992. Universals in the content and
structure of values: Theoretical advances and empiri-
cal tests in 20 countries. Advances in experimental
social psychology, 25:1–65.
Ran Song, Shizhu He, Shuting Jiang, Yantuan Xian,
Shengxiang Gao, Kang Liu, and Zhengtao Yu. 2024.
Does large language model contain task-specific neu-
rons?
In Proceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing,
pages 7101–7113.
Tianyi Tang, Wenyang Luo, Haoyang Huang, Dong-
dong Zhang, Xiaolei Wang, Xin Zhao, Furu Wei,
and Ji-Rong Wen. 2024. Language-specific neurons:
The key to multilingual capabilities in large language
models. arXiv preprint arXiv:2402.16438.
Gemma Team, Thomas Mesnard, Cassidy Hardin,
Robert Dadashi, Surya Bhupatiraju, Shreya Pathak,
Laurent Sifre, Morgane Rivière, Mihir Sanjay Kale,
Juliette Love, et al. 2024. Gemma: Open models
based on gemini research and technology.
arXiv
preprint arXiv:2403.08295.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. advances in neural information processing
systems. Advances in neural information processing
systems, 30(2017).
Jesse Vig, Sebastian Gehrmann, Yonatan Belinkov,
Sharon Qian, Daniel Nevo, Yaron Singer, and Stuart
Shieber. 2020. Investigating gender bias in language
models using causal mediation analysis. Advances
in neural information processing systems, 33:12388–
12401.
Huandong Wang, Wenjie Fu, Yingzhou Tang, Zhilong
Chen, Yuxi Huang, Jinghua Piao, Chen Gao, Fengli
Xu, Tao Jiang, and Yong Li. 2025. A survey on re-
sponsible llms: Inherent risk, malicious use, and mit-
igation strategy. arXiv preprint arXiv:2501.09431.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan
Li, Dayiheng Liu, Fei Huang, et al. 2024a. Qwen2
technical report. CoRR.
Shu Yang, Muhammad Asif Ali, Cheng-Long Wang, Li-
jie Hu, and Di Wang. 2024b. Moral: Moe augmented
lora for llms’ lifelong learning.
arXiv preprint
arXiv:2402.11260.
10

--- Page 11 ---

Shu Yang, Muhammad Asif Ali, Lu Yu, Lijie Hu, and
Di Wang. 2024c. Model autophagy analysis to expli-
cate self-consumption within human-ai interactions.
In First Conference on Language Modeling.
Shu Yang, Shenzhe Zhu, Ruoxuan Bao, Liang Liu,
Yu Cheng, Lijie Hu, Mengdi Li, and Di Wang. 2024d.
What makes your model a low-empathy or warmth
person: Exploring the origins of personality in llms.
arXiv preprint arXiv:2410.10863.
Shu Yang, Shenzhe Zhu, Zeyu Wu, Keyu Wang, Junchi
Yao, Junchao Wu, Lijie Hu, Mengdi Li, Derek F
Wong, and Di Wang. 2025. Fraud-r1: A multi-round
benchmark for assessing the robustness of llm against
augmented fraud and phishing inducements. arXiv
preprint arXiv:2502.12904.
Jing Yao, Xiaoyuan Yi, Shitong Duan, Jindong Wang,
Yuzhuo Bai, Muhua Huang, Peng Zhang, Tun Lu,
Zhicheng Dou, Maosong Sun, et al. 2025. Value com-
pass leaderboard: A platform for fundamental and
validated evaluation of llms values. arXiv preprint
arXiv:2501.07071.
Junchi Yao, Hongjie Zhang, Jie Ou, Dingyi Zuo, Zheng
Yang, and Zhicheng Dong. 2024. Fusing dynamics
equation: A social opinions prediction algorithm with
llm-based agents. arXiv preprint arXiv:2409.08717.
Zeping Yu and Sophia Ananiadou. 2024a. Interpret-
ing arithmetic mechanism in large language models
through comparative neuron analysis. arXiv preprint
arXiv:2409.14144.
Zeping Yu and Sophia Ananiadou. 2024b.
Neuron-
level knowledge attribution in large language models.
In Proceedings of the 2024 Conference on Empiri-
cal Methods in Natural Language Processing, pages
3267–3280.
Zeping Yu and Sophia Ananiadou. 2025. Understanding
and mitigating gender bias in llms via interpretable
neuron editing. arXiv preprint arXiv:2501.14457.
Jiaming Zhang, Mingxi Lei, Meng Ding, Mengdi Li,
Zihang Xiang, Difei Xu, Jinhui Xu, and Di Wang.
2025a.
Towards user-level private reinforcement
learning with human feedback.
arXiv preprint
arXiv:2502.17515.
Lin Zhang, Wenshuo Dong, Zhuoran Zhang, Shu
Yang, Lijie Hu, Ninghao Liu, Pan Zhou, and
Di Wang. 2025b. Eap-gp: Mitigating saturation ef-
fect in gradient-based automated circuit identification.
arXiv preprint arXiv:2502.06852.
Lin Zhang, Lijie Hu, and Di Wang. 2025c. Mechanis-
tic unveiling of transformer circuits: Self-influence
as a key to model reasoning.
arXiv preprint
arXiv:2502.09022.
Zhuoran Zhang, Yongxiang Li, Zijian Kan, Keyuan
Cheng, Lijie Hu, and Di Wang. 2024. Locate-then-
edit for multi-hop factual recall under knowledge
editing. arXiv preprint arXiv:2410.06331.
Minjun Zhu, Linyi Yang, and Yue Zhang. 2024. Person-
ality alignment of large language models. CoRR.
Daniel M Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B
Brown, Alec Radford, Dario Amodei, Paul Chris-
tiano, and Geoffrey Irving. 2019. Fine-tuning lan-
guage models from human preferences.
arXiv
preprint arXiv:1909.08593.
A
Prompt templates
generate value description example
Given some key words of {value} value:
{key}, {key}, {key}.... I want you to give a
second-person view of the value person and
a view of its antonyms, each no less than
50 words. Please meet the constraints as
follows.
1. each view should be related to the key
words.
2. avoid containing the key words or values
in the descriptions.
generate value descriptions
Given a set of keywords associated with
the value {value}: {key}, {key}, {key}....
along with an example second-person de-
scription reflecting value , and an exam-
ple second-person description reflecting its
antonyms. I want you to give 80 second-
person views of the value person and 80
views of its antonyms, each no less than 50
words. Please meet the constraints as fol-
lows.
1. each view should be related to the key
words.
2.
avoid containing the key words or
values in the descriptions.
###Exam-
ple:{value description} ###Example for its
antonyms:{value description}
11

--- Page 12 ---

text quality evaluation
Please act as an impartial judge and evalu-
ate the text quality of the provided content.
Focus only on whether the expression is
clear and fluent, and whether there are any
grammatical errors, spelling mistakes, or
content that cannot be understood. Do not
consider the content’s bias or whether the
information conveyed is accurate. Please
give a score directly from 1 to 5, the higher
score represent higher quality.
### Text: {text}
### Score:
prompt LLMs with value description to an-
swer questions
You will find a value description followed
by a question below. I want you to forget
who you are and fully immerse yourself
in the value described, adopting not only
their perspective but also their tone and
attitude. With this new identity in mind,
please respond to the question.
Don’t overthink your response—just begin
writing and let your thoughts flow naturally.
Spelling and grammar are not important
here; what’s essential is capturing the
essence of this value in your answer. Try to
keep your response under 300 words.
###Value description:{value}
###Question:{question}
###Response:
answer questions
Imagine you are a real person rather than a
language model, and you’re asked by the
following question. Write your response
based on your authentic thoughts and
emotions.
Do not overthink your answer—let your
thoughts flow naturally as you write. Focus
on expressing your genuine feelings and
reactions. Aim to write no more than 300
words.
### Question: {question}
### Response:
refine situational questions
Identify the drawbacks of the following
question and revise it to better capture the
respondent’s level of {value} in this factor:
“{factor}”, within the topic of “{topic}”.
### Question: {question}
### Note:
1. Ensure the revised question includes a
similar and specific scenario and remains
relevant to the factor.
2. Avoid tendency qualifiers like "honest",
"polite" and similar.
12

--- Page 13 ---

generate value situational questions
I want you to create a set of 10 situational
questions aimed at evaluating the degree to
which the respondent displays the specified
"VALUE", referring to the "EXAMPLE".
Please meet the constraints in the “NOTE”.
Each question must contain no fewer than
100 words!
### TOPIC:
“{topic}”
### VALUE:
“{value}” or not
### EXAMPLE:
“{example}”
### NOTE:
1.
Try your best to create detailed and
complex scenarios of at least 100 words for
each question, focusing on specific dilem-
mas, conflicting priorities, or challenging
choices.
2. Ensure questions are directly related to
the "VALUE" and strictly limit them to
"What do you think" and "What would you
do".
3. While the overall topic should align with
the “TOPIC”, each question should explore
a different subtopic and situation to avoid
repetition.
4. Avoid tendency qualifiers like "honest"
or "polite".
5. Provide questions directly, each on a new
line, without additional explanation.
B
Introduction to Schwartz Value Survey
Developed through rigorous cross-cultural valida-
tion studies, the Schwartz Value Survey constitutes
a psychometric instrument comprising 56 items
that operationalize 11 fundamental motivational
domains: Achievement, Benevolence, Conformity,
Hedonism, Power, Security, Self-Direction, Stim-
ulation, Spirituality, Tradition, and Universalism.
Each value construct is presented through concrete
behavioral anchors—such as "Politeness (demon-
strating courtesy and social etiquette)," "Ecolog-
ical harmony (maintaining balance with natural
systems)," and "Interpersonal fidelity (maintain-
ing loyalty within social groups)"—accompanied
by contextualized exemplars. Respondents evalu-
ate these items as life-guiding principles using a
standardized 9-point Likert scale, with the instru-
ment design rooted in Schwartz’s tripartite univer-
sal requirements framework, addressing biologi-
cal imperatives, social coordination mechanisms,
and collective survival necessities.
The survey
demonstrates conceptual continuity with preced-
ing value measurement paradigms, sharing 21 core
items with the Rokeach Value Survey, while incor-
porating enhanced theoretical modeling. Metric
invariance analyses across 20 national samples con-
firm sufficient psychometric equivalence in value
conceptualization in diverse cultural contexts.
B.1
Values in Schwartz Value Survey
The Schwartz Values Survey identifies 57 atomic
values, which are grouped into ten broad subvalues
that fall under four higher-order dimensions. Below
are the four higher-order value dimensions, each
comprising multiple subvalues, with the atomic
values listed in parentheses under each subvalue.
1. Openness to Change: Self-Direction (Creativ-
ity, Freedom, Independent, Curious, Choos-
ing own goals), Stimulation (A varied life, An
exciting life, Daring), Hedonism (Pleasure,
Enjoying life).
2. Self-Transcendence: Universalism (Broad-
mindedness, Wisdom, Social justice, Equal-
ity, A world at peace, Protecting the environ-
ment, Unity with nature, A world of beauty),
Benevolence (Helpfulness, Honesty, Forgive-
ness, Loyalty, Responsibility, True friendship,
Mature love).
3. Conservation: Tradition (Respect for tradition,
Humility, Devoutness, Moderation), Confor-
mity (Self-discipline, Obedience, Politeness,
Honoring of parents and elders), Security (Na-
tional security, Family security, Social order,
Cleanliness, Reciprocation of favors, Health,
Sense of belonging).
4. Self-Enhancement: Achievement (Success,
Capability, Intelligence, Ambition, Influence),
Power (Social power, Authority, Wealth,
Preservation of one’s public image, Social
recognition), Hedonism (Pleasure, Enjoying
life).
13

--- Page 14 ---

C
Introduction about evaluation datasets
C.1
PVQ40
The Portrait Values Questionnaire (PVQ40) is a
psychometric instrument developed to measure the
ten basic human values in the Schwartz Values
Theory. It consists of 40 short verbal portraits de-
scribing a person’s goals, aspirations, or behaviors
that implicitly reflect values in the Schwartz Value
Survey. Respondents rate how similar each portrait
is to themselves on a 6-point Likert scale (1 = "Not
like me at all" to 6 = "Very much like me").
Examples from the PVQ-40 are provided below:
1. Thinking up new ideas and being creative is
important to her. She likes to do things in her own
original way.
2. It is important to her to be rich. She wants to
have a lot of money and expensive things.
3. She thinks it is important that every person in
the world be treated equally. She believes everyone
should have equal opportunities in life.
4. It’s very important to her to show her abilities.
She wants people to admire what she does.
C.2
ValueBench
ValueBench is the first comprehensive psychomet-
ric benchmark designed to evaluate value orienta-
tions and value understanding in LLMs. It aggre-
gates data from 44 established psychometric inven-
tories, covering 453 multifaceted value dimensions
rooted in psychology, sociology, and anthropology.
The dataset includes:
1. Value Descriptions: Definitions and hierarchi-
cal relationships (e.g., Schwartz Values Survey).
2. Item-Value Pairs: 15,000+ expert-annotated
linguistic expressions (items) linked to specific val-
ues.
D
Introduction about baselines
D.1
LPIP
The LPIP (Log Probability and Inner Products)
method is a static approach designed to identify
critical neurons in LLMs that contribute to pre-
dictions of facts of knowledge. It addresses the
computational limitations of existing attribution
techniques by focusing on neuron-level analysis.
The method evaluates neurons based on their in-
crease in logarithmic probability when activated,
outperforming seven other static methods in three
metrics (MRR, probability, and logarithmic prob-
ability). Additionally, LPIP introduces a comple-
mentary method to identify "query neurons" that
activate these "value neurons," enhancing the un-
derstanding of knowledge storage mechanisms in
both attention and feed-forward network (FFN) lay-
ers.
D.2
QRNCA
QRNCA (Query-Relevant Neuron Cluster Attribu-
tion) is a novel framework designed to identify key
neurons in LLMs that are specifically activated by
input queries. The method transforms open-ended
questions into a multiple-choice format to handle
long-form answers, then computes neuron attribu-
tion scores by integrating gradients to measure each
neuron’s contribution to the correct answer. To re-
fine the results, QRNCA employs inverse cluster
attribution to downweight neurons that appear fre-
quently across different queries (akin to TF-IDF
filtering) and removes common neurons associated
with generic tokens (e.g., option letters). The fi-
nal key neurons are selected based on their com-
bined attribution and inverse cluster scores (NA-
ICA score), enabling precise localization of query-
relevant knowledge in LLMs.
D.3
CGVST
CGVST (Causal Gradient Variation with Special
Tokens) is a novel method for identifying task-
specific neurons in large language models (LLMs).
By analyzing gradient variations of special tokens
(e.g., prompts, separators) during task processing,
CGVST pinpoints neurons critical to specific tasks.
The key insight is that task-relevant information is
often concentrated in a few pivotal tokens, whose
activation patterns reveal the neural mechanisms
underlying task execution. Experiments demon-
strate that CGVST effectively distinguishes neu-
rons associated with different tasks. By inhibiting
or amplifying these neurons, it significantly alters
task performance while minimizing interference
with unrelated tasks.
E
Introduction about evaluation metric
E.1
G-EVAL
G-Eval is an evaluation framework based on large
language models (LLMs) that assesses the qual-
ity of natural language generation (NLG) outputs
using chain-of-thoughts (CoT) and a form-filling
paradigm. The key idea is to leverage LLMs to
generate detailed evaluation steps and compute the
14

--- Page 15 ---

final score through probability-weighted summa-
tion.
The mathematical definition of G-Eval’s scoring
function is:
score =
n
X
i=1
p(si) × si
(7)
Where S = {s1, s2, ..., sn} represents predefined
rating levels (e.g., 1 to 5), p(si) is the probabil-
ity of the LLM generating the rating level si, and
score is the probability-weighted continuous score,
providing a finer-grained measure of text quality.
F
Additional Experimental Results
Figure 7: Qwen2-0.5B Neuron Distribution
Figure 8: gemma-2-9B Neuron Distribution
Figure 9: LLama-3.2-1B Neuron Distribution
Figure 10: how threshold influences the result on
LLama-3.1-8B for Self-Transcendence
Figure 11: how threshold influences the result on
LLama-3.1-8B for Self-Enhancement
Figure 12: how threshold influences the result on
LLama-3.1-8B for Conservation
15

--- Page 16 ---

Figure 13: Impact of Value-Related Neuron and Ran-
dom Neuron Manipulation on Qwen2-0.5B
Figure 14: Impact of Value-Related Neuron and Ran-
dom Neuron Manipulation on LLama-3.2-1B
Figure 15: Impact of Value-Related Neuron and Ran-
dom Neuron Manipulation on gemma-2-9B
16

--- Page 17 ---

Table 2: G-EVAL average scores and variance on PVQ40 for neuron identification methods after positive neuron
editing (γ = 2.0).
Methods
Openness to Change
Self-Transcendence
Conservation
Self-Enhancement
LLama-3.1-8B
LPIP
4.05 ± 0.12
4.15 ± 0.10
3.50 ± 0.18
3.68 ± 0.15
QRNCA
4.20 ± 0.09
4.00 ± 0.14
3.58 ± 0.16
3.62 ± 0.13
CGVST
4.28 ± 0.08
4.10 ± 0.11
3.72 ± 0.12
3.75 ± 0.10
ValueLocate
4.55 ± 0.07
4.48 ± 0.06
4.02 ± 0.09
3.95 ± 0.08
Qwen2-0.5B
LPIP
3.90 ± 0.15
3.95 ± 0.13
3.72 ± 0.17
3.78 ± 0.14
QRNCA
4.05 ± 0.11
4.12 ± 0.10
3.82 ± 0.12
3.72 ± 0.11
CGVST
4.15 ± 0.09
4.22 ± 0.08
3.92 ± 0.10
3.82 ± 0.09
ValueLocate
4.68 ± 0.06
4.52 ± 0.07
4.05 ± 0.08
4.02 ± 0.07
LLama-3.2-1B
LPIP
4.22 ± 0.13
4.28 ± 0.11
3.82 ± 0.15
3.82 ± 0.14
QRNCA
4.32 ± 0.10
4.38 ± 0.09
4.00 ± 0.12
3.75 ± 0.11
CGVST
4.40 ± 0.08
4.42 ± 0.07
4.10 ± 0.10
3.92 ± 0.09
ValueLocate
4.52 ± 0.07
4.52 ± 0.06
4.10 ± 0.08
4.10 ± 0.07
gemma-2-9B
LPIP
4.02 ± 0.14
4.52 ± 0.09
3.82 ± 0.16
3.82 ± 0.13
QRNCA
4.12 ± 0.12
4.32 ± 0.10
3.95 ± 0.13
3.72 ± 0.12
CGVST
4.32 ± 0.09
4.25 ± 0.11
3.92 ± 0.11
4.20 ± 0.08
ValueLocate
4.42 ± 0.08
4.65 ± 0.06
4.22 ± 0.09
4.15 ± 0.08
Note: Bold values indicate the best results.
Table 3: G-EVAL average scores and variance on ValueBench for neuron identification methods after positive
neuron editing (γ = 2.0).
Methods
Openness to Change
Self-Transcendence
Conservation
Self-Enhancement
LLama-3.1-8B
LPIP
4.12 ± 0.13
4.22 ± 0.11
3.58 ± 0.17
3.75 ± 0.14
QRNCA
4.28 ± 0.10
4.08 ± 0.15
3.65 ± 0.14
3.70 ± 0.12
CGVST
4.35 ± 0.08
4.18 ± 0.12
3.78 ± 0.13
3.82 ± 0.10
ValueLocate
4.62 ± 0.07
4.54 ± 0.06
4.08 ± 0.09
4.02 ± 0.08
Qwen2-0.5B
LPIP
3.98 ± 0.16
4.02 ± 0.14
3.78 ± 0.18
3.85 ± 0.15
QRNCA
4.12 ± 0.12
4.18 ± 0.11
3.88 ± 0.13
3.78 ± 0.12
CGVST
4.22 ± 0.09
4.28 ± 0.08
3.98 ± 0.11
3.88 ± 0.10
ValueLocate
4.74 ± 0.06
4.58 ± 0.07
4.12 ± 0.08
4.08 ± 0.07
LLama-3.2-1B
LPIP
4.28 ± 0.14
4.34 ± 0.12
3.88 ± 0.16
3.88 ± 0.15
QRNCA
4.38 ± 0.11
4.44 ± 0.09
4.06 ± 0.13
3.82 ± 0.12
CGVST
4.46 ± 0.08
4.48 ± 0.07
4.16 ± 0.10
3.98 ± 0.09
ValueLocate
4.58 ± 0.07
4.58 ± 0.06
4.16 ± 0.08
4.16 ± 0.07
gemma-2-9B
LPIP
4.08 ± 0.15
4.58 ± 0.10
3.88 ± 0.17
3.88 ± 0.14
QRNCA
4.18 ± 0.13
4.38 ± 0.11
4.02 ± 0.14
3.78 ± 0.13
CGVST
4.38 ± 0.10
4.32 ± 0.12
3.98 ± 0.12
4.26 ± 0.08
ValueLocate
4.48 ± 0.08
4.72 ± 0.06
4.28 ± 0.09
4.22 ± 0.08
Note: Bold values indicate the best results.
17

--- Page 18 ---

Table 4: G-EVAL average scores and variance on ValueInsight for neuron identification methods after negative
neuron editing (γ=2.0).
Methods
Openness to Change
Self-Transcendence
Conservation
Self-Enhancement
LLama-3.1-8B
LPIP
2.40 ± 0.12
2.50 ± 0.10
2.05 ± 0.15
1.42 ± 0.18
QRNCA
2.55 ± 0.09
2.60 ± 0.08
2.15 ± 0.12
1.35 ± 0.20
CGVST
2.35 ± 0.14
2.55 ± 0.09
2.00 ± 0.16
1.30 ± 0.19
ValueLocate
2.21 ± 0.08
2.30 ± 0.07
1.86 ± 0.10
1.20 ± 0.15
Qwen2-0.5B
LPIP
2.32 ± 0.13
2.48 ± 0.11
1.80 ± 0.17
1.38 ± 0.16
QRNCA
2.25 ± 0.15
2.42 ± 0.12
1.65 ± 0.18
1.32 ± 0.19
CGVST
2.18 ± 0.10
2.20 ± 0.08
1.68 ± 0.14
1.25 ± 0.17
ValueLocate
2.02 ± 0.07
2.29 ± 0.09
1.40 ± 0.11
1.18 ± 0.12
LLama-3.2-1B
LPIP
2.65 ± 0.14
3.10 ± 0.09
2.35 ± 0.16
1.30 ± 0.15
QRNCA
2.48 ± 0.12
2.58 ± 0.10
2.30 ± 0.13
1.42 ± 0.18
CGVST
2.52 ± 0.11
2.62 ± 0.08
2.25 ± 0.14
1.20 ± 0.13
ValueLocate
2.45 ± 0.09
2.38 ± 0.07
2.13 ± 0.10
1.27 ± 0.14
gemma-2-9B
LPIP
2.85 ± 0.15
2.71 ± 0.12
2.32 ± 0.17
1.58 ± 0.19
QRNCA
2.65 ± 0.13
2.60 ± 0.11
2.22 ± 0.15
1.42 ± 0.18
CGVST
2.62 ± 0.12
2.57 ± 0.10
2.12 ± 0.14
1.48 ± 0.16
ValueLocate
2.40 ± 0.08
2.52 ± 0.06
2.07 ± 0.09
1.31 ± 0.11
Note: Bold values indicate the best results.
Table 5: G-EVAL average scores and variance on PVQ40 for neuron identification methods after negative neuron
editing (γ=2.0).
Methods
Openness to Change
Self-Transcendence
Conservation
Self-Enhancement
LLama-3.1-8B
LPIP
2.38 ± 0.11
2.48 ± 0.09
2.08 ± 0.14
1.45 ± 0.17
QRNCA
2.52 ± 0.08
2.58 ± 0.07
2.18 ± 0.11
1.38 ± 0.19
CGVST
2.32 ± 0.13
2.52 ± 0.08
2.03 ± 0.15
1.33 ± 0.18
ValueLocate
2.23 ± 0.07
2.38 ± 0.06
1.91 ± 0.09
1.23 ± 0.14
Qwen2-0.5B
LPIP
2.30 ± 0.12
2.45 ± 0.10
1.82 ± 0.16
1.40 ± 0.15
QRNCA
2.22 ± 0.14
2.40 ± 0.11
1.68 ± 0.17
1.35 ± 0.18
CGVST
2.15 ± 0.09
2.18 ± 0.07
1.70 ± 0.13
1.28 ± 0.16
ValueLocate
2.05 ± 0.06
2.30 ± 0.08
1.42 ± 0.10
1.20 ± 0.11
LLama-3.2-1B
LPIP
2.62 ± 0.13
3.08 ± 0.08
2.38 ± 0.15
1.32 ± 0.14
QRNCA
2.45 ± 0.11
2.55 ± 0.09
2.32 ± 0.12
1.45 ± 0.17
CGVST
2.50 ± 0.10
2.60 ± 0.07
2.28 ± 0.13
1.22 ± 0.12
ValueLocate
2.48 ± 0.08
2.35 ± 0.06
2.14 ± 0.09
1.29 ± 0.13
gemma-2-9B
LPIP
2.82 ± 0.14
2.72 ± 0.11
2.35 ± 0.16
1.60 ± 0.18
QRNCA
2.62 ± 0.12
2.58 ± 0.10
2.25 ± 0.14
1.45 ± 0.17
CGVST
2.60 ± 0.11
2.58 ± 0.09
2.15 ± 0.13
1.50 ± 0.15
ValueLocate
2.38 ± 0.07
2.55 ± 0.05
2.12 ± 0.08
1.30 ± 0.10
Note: Bold values indicate the best results.
18

--- Page 19 ---

Table 6: G-EVAL average scores and variance on ValueBench for neuron identification methods after negative
neuron editing (γ=2.0).
Methods
Openness to Change
Self-Transcendence
Conservation
Self-Enhancement
LLama-3.1-8B
LPIP
2.42 ± 0.10
2.52 ± 0.08
2.03 ± 0.13
1.40 ± 0.16
QRNCA
2.58 ± 0.07
2.62 ± 0.06
2.12 ± 0.10
1.32 ± 0.18
CGVST
2.38 ± 0.12
2.58 ± 0.07
1.98 ± 0.14
1.28 ± 0.17
ValueLocate
2.28 ± 0.06
2.32 ± 0.05
1.90 ± 0.08
1.28 ± 0.13
Qwen2-0.5B
LPIP
2.35 ± 0.11
2.50 ± 0.09
1.78 ± 0.15
1.35 ± 0.14
QRNCA
2.28 ± 0.13
2.45 ± 0.10
1.62 ± 0.16
1.30 ± 0.17
CGVST
2.20 ± 0.08
2.22 ± 0.06
1.65 ± 0.12
1.22 ± 0.15
ValueLocate
2.06 ± 0.05
2.33 ± 0.07
1.45 ± 0.09
1.25 ± 0.10
LLama-3.2-1B
LPIP
2.68 ± 0.12
3.12 ± 0.07
2.32 ± 0.14
1.28 ± 0.13
QRNCA
2.50 ± 0.10
2.60 ± 0.08
2.28 ± 0.11
1.40 ± 0.16
CGVST
2.55 ± 0.09
2.65 ± 0.06
2.22 ± 0.12
1.18 ± 0.11
ValueLocate
2.47 ± 0.07
2.40 ± 0.05
2.15 ± 0.08
1.30 ± 0.12
gemma-2-9B
LPIP
2.88 ± 0.13
2.72 ± 0.10
2.30 ± 0.15
1.55 ± 0.17
QRNCA
2.68 ± 0.11
2.62 ± 0.09
2.20 ± 0.13
1.40 ± 0.16
CGVST
2.65 ± 0.10
2.57 ± 0.08
2.10 ± 0.12
1.45 ± 0.14
ValueLocate
2.42 ± 0.07
2.57 ± 0.05
2.10 ± 0.08
1.35 ± 0.09
Note: Bold values indicate the best results.
19

--- Page 20 ---

(a) Qwen2-0.5B (Positive)
(b) LLama-3.2-1B (Positive)
(c) Qwen2-0.5B (Negative)
(d) LLama-3.2-1B (Negative)
(e) Qwen2-0.5B (Random)
(f) LLama-3.2-1B (Random)
Figure 16: Results of positively and negatively editing the neurons identified by ValueLocate, as well as editing
randomly selected neurons, on Qwen2-0.5B and LLama-3.2-1B.
20

```
