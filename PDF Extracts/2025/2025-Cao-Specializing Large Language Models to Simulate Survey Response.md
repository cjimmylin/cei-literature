---
title: "2025-Cao-Specializing Large Language Models to Simulate Survey Response - PDF Extract"
source_pdf: "2025-Cao-Specializing Large Language Models to Simulate Survey Response.pdf"
pages: 14
extracted_at: "2026-02-15T18:01:03.089168"
---

# PDF Extract: 2025-Cao-Specializing Large Language Models to Simulate Survey Response

**Source PDF:** 2025-Cao-Specializing Large Language Models to Simulate Survey Response.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

Specializing Large Language Models to Simulate
Survey Response Distributions for Global Populations
Yong Cao1, Haijiang Liu2, Arnav Arora3, Isabelle Augenstein3,
Paul Röttger4, Daniel Hershcovich3
1University of Tübingen, Tübingen AI Center
2Wuhan University of Science and Technology
3University of Copenhagen, 4Bocconi University
yong.cao@uni-tuebingen.de, dh@di.ku.dk
Abstract
Large-scale surveys are essential tools for in-
forming social science research and policy, but
running surveys is costly and time-intensive.
If one could accurately simulate group-level
survey results, this could be very valuable to so-
cial science research. Prior work has explored
the use of large language models (LLMs) for
simulating human behaviors, mostly through
prompting. In this paper, we are the first to
specialize LLMs for the task of simulating sur-
vey response distributions. As a testbed for
this task, we use country-level results from two
global cultural surveys. We devise a fine-tuning
method based on first-token probabilities to
minimize divergence between predicted and ac-
tual response distributions for a given question.
Then, we show that this method substantially
outperforms other methods and zero-shot classi-
fiers, even on unseen questions, countries, and a
completely unseen survey. While even our best
models struggle with the task, especially on
unseen questions, our results demonstrate the
benefits of specialization for simulation, which
may accelerate progress towards sufficiently
accurate simulation in the future.
1
Introduction
Humans are diverse, and they hold diverse opinions.
This is why surveys are essential tools for inform-
ing decision-making in policy and industry as well
as social science research. Running large-scale sur-
veys, however, is often costly and time-intensive.
Large language models (LLMs) have demon-
strated promising potential for simulating human
behaviors across groups and individuals (Argyle
et al., 2023; Aher et al., 2023; Manning et al., 2024,
inter alia). LLM simulations of survey responses,
if accurate towards the corresponding populations,
could accelerate social science research and aid in
more informed policy decisions. Out of the box,
however, LLMs are known to generate erroneous,
LLMs
From Human:
B. Agree.
Training
LLMs
LLMs
Inference
Majority Option
Option Distribution
LLMs
!
Output:
B. Agree
Output
LossCE
LossKL
Input
A
B
C
D
A
B
C
D
e.g., Do you agree that having 
children is a duty to society?
Multiple-Choice Question
People from
America " / Germany # / ...
Country
!
Unseen
Question
Unseen
Country
Unseen
Question
Unseen
Country
Answer: A.
Strongly Agree.
Our Approach
Direct Answer Prediction
Figure 1: Overview of our proposed survey response
distribution simulation framework (right panel) ver-
sus direct answer prediction (left panel), highlighting a
novel perspective on cultural simulation with LLMs.
stereotypical, or overconfident answers, especially
in culturally diverse contexts (Yang et al., 2024),
which limits their usefulness for survey simulations.
Prior work has at most tried to improve simulation
accuracy through prompting strategies (Kwok et al.,
2024; Manning et al., 2024; Sun et al., 2024).
In this study, our goal is instead to specialize
LLMs for survey simulation and gain a better
understanding of how good LLMs can be at sim-
ulating survey responses when trained to do so,
rather than how good they are when prompted out
of the box. As our main testbed, we use country-
level response distributions from the widely-used
World Values Survey (WVS; Haerpfer et al., 2022).
When prompted with a survey question (e.g., “In
your opinion, should the use of nuclear power in
Japan be reduced, maintained at its current level,
or increased?”), corresponding answering options
(e.g. “Reduced”, “Maintained at current level”, “In-
creased”) and a target country (e.g. “Japan”), we
want our model to predict the distribution over the
answering options for that target country. To spe-
arXiv:2502.07068v2  [cs.CL]  19 Feb 2025

--- Page 2 ---

cialize LLMs for this task, we devise a fine-tuning
method based on first-token probabilities, where
the goal is to minimize divergence between pre-
dicted and actual country-level response distribu-
tions for a given survey question.
As shown in Figure 1, we train models on one
set of questions and countries from the WVS, then
evaluate on both seen and unseen countries and
questions as well as another completely unseen sur-
vey. Across seven LLMs from three model families,
our fine-tuning method substantially boosts predic-
tion accuracy on seen and unseen WVS countries
and questions. These results also hold for a com-
pletely unseen survey, i.e. the Pew Global Attitudes
Survey. Simultaneously, we find the performance
of even the best-fine-tuned models to be far from
perfect, especially on unseen questions. We also
find that all LLMs we tested, whether fine-tuned
or not, are less diverse in their predictions across
countries than the actual human survey data.
In summary, we make following three main
contributions:
• We introduce group-level survey response dis-
tribution prediction as a simulation task, and
share three datasets adapted for training and
testing models on this task: two in English
and one in Chinese.
• We propose a fine-tuning method based on
first-token probabilities of multi-choice ques-
tion answering, and show that this method
performs best among the methods tested for
our simulation task, which demonstrates the
benefits of specialization for simulation.
• We contextualize these positive results with
evidence of systematic inaccuracies in even
the best-performing simulations, thus caution-
ing against the use of LLMs, specialized or
not, for simulating survey response distribu-
tions today.1
2
Related Work
LLM Simulations
Collecting human response
data is one of the most challenging and costly as-
pects of social science research (Argyle et al., 2023;
Hewitt et al., 2024). Consequently, much prior
work has investigated the extent to which LLMs
can accurately simulate human responses in sur-
veys and experimental settings. Most prominently,
Argyle et al. (2023), Horton (2023) and Aher et al.
1We make all code and used dataset available at
github.com/yongcaoplus/SimLLMCultureDist.
(2023) all found evidence of LLMs providing rea-
sonably accurate group-level simulations in behav-
ioral science and economics experiments as well
as for US political surveys. Some follow-up work
has highlighted biases and conceptual challenges
in such simulations (Bisbee et al., 2023; Bail, 2024;
Park et al., 2024; Kozlowski and Evans, 2024).
Other work has explored prompting strategies and
frameworks for improving simulation accuracy
(Kwok et al., 2024; Manning et al., 2024; Sun et al.,
2024). Relatedly, several works have used survey
questionnaires, including the WVS used in this pa-
per, with the goal of evaluating values and opinions
reflected in LLMs rather than simulating human
survey responses (Benkler et al., 2023; Arora et al.,
2023; Cao et al., 2023; AlKhamissi et al., 2024;
Zhao et al., 2024; Wright et al., 2024, inter alia). In
contrast to these efforts, our focus is on specializ-
ing LLMs to simulate group-level survey response
distribution, which could aid in survey data col-
lection. While we do measure the performance of
LLMs out of the box (zero-shot), our main goal
is to investigate the extent to which we can im-
prove LLM performance on simulating group-level
survey response distributions through fine-tuning,
and explore their potential as specialized tools for
social science research.
Distribution Simulation as Calibration.
Cali-
bration is aligning classifier predictive probabili-
ties with the classification uncertainty. While most
work focuses on majority class accuracy (Li et al.,
2024; He et al., 2024), this is problematic when
human label variation is substantial (Baan et al.,
2022, 2024), and human calibration should con-
sider the full human judgment distribution. Our
task can therefore be viewed as human calibration
for multiple-choice surveys, as opposed to many
previous studies, which focused on accuracy mea-
sured against the majority answer (Arora et al.,
2023; Cao et al., 2023; AlKhamissi et al., 2024).
3
Cultural Survey Simulation Dataset
3.1
Data Source
We use the 2017-2022 wave of the World Values
Survey (WVS)2 to construct our main simulation
dataset. WVS was conducted across 66 countries
with over 80,000 respondents. This extensive sur-
vey captures societal attitudes on various cultural
2https://www.worldvaluessurvey.org/
WVSDocumentationWV7.jsp

--- Page 3 ---

Instruction
How would someone from Andorra an-
swer the following question:
Input
How interested would you say you are
in politics? Here are the options:
Options
(A) Very interested
(B) Somewhat interested
(C) Not very interested
(D) Not at all interested
Format
If had to select one of the options, my
answer would be ([A/B/...])
Options
(A) 15.16%
(B) 29.02%
Distribution
(C) 28.31%
(D) 27.51%
Table 1: Example entry from our formatted WVS
dataset for the country of Andorra.
dimensions, including family, regional values, edu-
cation, moral principles, corruption, accountabil-
ity, etc. Our analysis includes all countries with
more than 1,000 respondents to ensure robust cross-
cultural representation, resulting in a set of 65 coun-
tries (Northern Ireland did not qualify).
For our analysis, we use the original questions
and answers, excluding validity-check options such
as “not applicable” and “refuse to answer”, given
their infrequent occurrence in human-collected re-
sponses. We conduct experiments using the En-
glish and Chinese versions of the datasets obtained
from the official source, enabling the analysis of
cross-linguistic differences in this task3.
3.2
Prompt Settings
We preserve the original questions and response op-
tions, adhering to the GlobalOpinionQA template
for consistency (Durmus et al., 2023). As shown
in Table 1, the model input consists of fields for
instruction, input, options, and format, while the
target for alignment is the distribution of the op-
tions. Note that the format field is used to restrict
the vocabulary of the first token to valid options.
3.3
Dataset Split
We use the first 259 questions of the WVS to con-
struct our dataset, excluding demographics and
notes for interviewers. We divide them into three
parts based on topics: Q1 (questions 1-163), Q2
(questions 164-198), and Q3 (questions 199-259).
Additionally, we divide the countries into three
groups to ensure they are challenging to generalize
between: C1 (all countries that are not included in
3We use GLM-4 to translate the missing questions in the
Chinese questionnaire.
Countries
Description
N
C1
All WVS countries not in C2 or C3
46
C2
African countries
8
C3
Medium-GDP countries
11
Questions
Description
N
Q1
All WVS questions not in Q2 or Q3
150
Q2
Q’s about religious and ethical values
35
Q3
Q’s about political interest and culture
59
Table 2: Country and question splits that we use in
our experiments with WVS data. Splits seen during
training are highlighted in bold. For additional descrip-
tive statistics on the dataset, see Appendix B.
the following two sets), C2 (the 8 surveyed coun-
tries that are in Africa4), and C3 (medium-GDP
countries sampled from each continent5).
We split training, validation, and test sets for
the aforementioned questions and country subsets.
The split and statistical information of the dataset
are presented in Table 2 and Table 3 respectively.
The test set comprises five subsets, designed to
evaluate the performance of models in answering
unseen value questions, unseen regional countries,
and representative medium-GDP countries.
3.4
Unseen Survey Dataset
To evaluate generalization to a completely unseen
survey, we use an additional subset of GlobalOp-
inionQA (Durmus et al., 2023), the Pew Global
Attitudes Survey (Pew), which maintains a similar
format to the WVS but includes different cultural
questions. We compile two sets of countries for
this test set: C′
1 and C3. For C′
1, we sample ten
countries from C1 to maintain geographical and
GDP-level diversity and then use the GlobalOp-
inionQA data specifically for these countries for
evaluation (see Appendix A). For C3, we include
the same medium-GDP countries as in C3.
4
Methodology
To address the challenges of simulating culturally
diverse survey responses, we introduce a frame-
work for first-token alignment fine-tuning for dis-
tribution prediction, designed to improve general-
ization across populations and survey questions.
4For subset C2, we select countries from one random con-
tinent (i.e. Africa). The selected African countries C2 are
Egypt, Ethiopia, Kenya, Libya, Morocco, Nigeria, Tunisia,
and Zimbabwe.
5Our selected medium-GDP countries C3 are Malaysia,
Thailand, Czechia, Greece, Nigeria, Morocco, Peru, Colombia,
Mexico, Puerto Rico, and New Zealand.

--- Page 4 ---

Split
Train
Valid
Test
Countries
C1
C1
C1
C2
C2
C3
C3
Questions
Q1
Q2
Q3
Q1
Q3
Q1
Q3
Entries
6,841
1,586
2,719
1,179
471
1,644
660
Table 3: WVS dataset statistics across the country (C)
and question (Q) splits we use in our experiments. Splits
seen during training are highlighted in bold. Number of
entries is not necessarily C × Q because some entries
are missing from survey results.
4.1
Probability Distribution Simulation
Unlike most existing studies that directly prompt
LLMs with multiple-choice questions to assess
their cultural knowledge or behavior (Arora et al.,
2023; Cao et al., 2023; AlKhamissi et al., 2024),
we propose a novel task that focuses on simulat-
ing the distribution of response options for given
questions rather than predicting single answers.
Specifically, let Q denote a multiple-choice ques-
tion and O = {o1, o2, ..., on} be the corresponding
set of response options, where n is the total num-
ber of options, which can vary between questions.
The objective is to simulate the option distribu-
tion P(O|Q) to match human response distribu-
tion from a particular group (e.g., country). Con-
sequently, models are evaluated by comparing the
alignment of observed vs. predicted distributions
rather than focusing on majority response options.
4.2
First-Token Probability Alignment
Using the dataset introduced in §3, we present first-
token alignment fine-tuning, to align model outputs
with the observed response distributions of specific
population groups (e.g., countries).
The processed question Q is used as input into
LLMs. The model outputs logits {z1, z2, . . . , zn}
for the first token of each question’s corresponding
options O. The probability distribution for the first
token is obtained by applying the softmax function
to normalize the indexed option logits:
PLLM(oi|Q) =
ezi
Pn
j=1 ezj
For the training optimization objective, we em-
ploy Kullback-Leibler Divergence loss (LossKL) to
align the LLM’s first-token probability distribution
with the human response distribution:
LossKL =
n
X
i=1
Phuman(oi|Q) log
Phuman(oi|Q)
PLLM(oi|Q)

where Phuman(oi|Q) is the probability of option oi
based on human survey data, and PLLM(oi|Q) is
the probability output by the LLM.
To improve the efficiency of the fine-tuning pro-
cess, we implement Low-Rank Adaptation (LoRA;
Hu et al., 2022), a parameter-efficient method
specifically designed for optimizing LLMs.
5
Experimental Setup
5.1
Models
We fine-tune seven models across three model
families using our processed dataset: Vicuna1.5
(Chiang et al., 2023) in its 7B and 13B parame-
ter versions, Llama3 (AI@Meta, 2024) in its 8B
Base and Instruct versions, and Deepseek-Distilled-
Qwen (Guo et al., 2025) in 7B, 14B, and 32B. Vi-
cuna1.5 is a version of Llama2 (Touvron et al.,
2023) fine-tuned on user conversations with Chat-
GPT, whereas Llama3 is a stronger model. As
Vicuna1.5 is less powerful than recent LLMs, it
is chosen to evaluate the effect of fine-tuning as
an equalizer despite zero-shot performance differ-
ences. DeepSeek is a state-of-the-art model series
known for its strong performance across diverse
benchmarks. We use the DeepSeek-Distilled-Qwen
models, which are distilled from the DeepSeek-
R1, the current state-of-the-art open weights model.
For further details on all models and our inference
setup, see Appendix C.
5.2
Baselines
In the main body of this paper, we compare our
fine-tuning method (FT) to a zero-shot prompting
(ZS) baseline, which is the default method explored
in prior work. ZS involves directly querying the
models with the country context and questions. As
an additional control setting, for both ZS and FT,
we replace countries in the queries with other coun-
tries randomly selected from among the full set of
countries in the WVS. This approach is designed
to investigate the sensitivity of the LLMs to the
specific country given in the context vs. the prior
distributions of response options. We denote this
control setting as “[ctrl]”. In Appendix E, we show
additional baselines such as K-Nearest Neighbors,
which generally perform worse than FT.
5.3
Metrics
To measure the alignment of predicted response
distributions with country-level reference distribu-
tions, we adopt two metrics for evaluation: i) 1-

--- Page 5 ---

Model
Methods
(1−JSD) ↑
EMD ↓
C1-Q3
C2-Q1
C2-Q3
C3-Q1
C3-Q3
Avg.
C1-Q3
C2-Q1
C2-Q3
C3-Q1
C3-Q3
Avg.
Vicuna1.5-7B
ZS [ctrl]
0.732
0.754
0.748
0.761
0.747
0.748
0.095
0.108
0.095
0.106
0.086
0.098
ZS
0.732
0.754
0.749
0.761
0.749
0.749
0.095
0.107
0.096
0.106
0.085
0.098
FT [ctrl]
0.754
0.829
0.754
0.842
0.765
0.789
0.089
0.078
0.092
0.072
0.080
0.082
FT
0.766
0.859
0.767
0.875
0.775
0.808
0.087
0.071
0.091
0.062
0.078
0.078
Vicuna1.5-13B
ZS [ctrl]
0.735
0.755
0.743
0.775
0.747
0.751
0.095
0.102
0.096
0.096
0.086
0.095
ZS
0.738
0.756
0.744
0.779
0.752
0.754
0.094
0.103
0.097
0.097
0.085
0.095
FT [ctrl]
0.760
0.820
0.761
0.830
0.762
0.787
0.083
0.080
0.085
0.074
0.077
0.080
FT
0.781
0.869
0.781
0.882
0.781
0.819
0.079
0.063
0.084
0.057
0.073
0.071
Llama3-8B-Base
ZS [ctrl]
0.748
0.766
0.757
0.779
0.768
0.764
0.097
0.114
0.093
0.109
0.088
0.100
ZS
0.749
0.768
0.759
0.781
0.770
0.765
0.097
0.116
0.097
0.109
0.087
0.101
FT [ctrl]
0.756
0.823
0.751
0.837
0.770
0.787
0.084
0.082
0.087
0.073
0.077
0.081
FT
0.770
0.858
0.773
0.877
0.781
0.812
0.081
0.073
0.087
0.061
0.074
0.075
Llama3-8B-Instruct
ZS [ctrl]
0.574
0.626
0.563
0.644
0.587
0.599
0.130
0.147
0.135
0.145
0.136
0.139
ZS
0.585
0.650
0.589
0.657
0.584
0.613
0.130
0.139
0.126
0.145
0.141
0.136
FT [ctrl]
0.756
0.826
0.751
0.833
0.764
0.786
0.077
0.077
0.082
0.073
0.071
0.076
FT
0.777
0.881
0.783
0.890
0.784
0.823
0.073
0.060
0.080
0.053
0.067
0.067
Distil-Qwen-7B
ZS[ctrl]
0.586
0.641
0.642
0.698
0.682
0.650
0.084
0.096
0.138
0.100
0.123
0.108
ZS
0.583
0.645
0.639
0.701
0.671
0.648
0.084
0.095
0.138
0.100
0.126
0.109
FT[ctrl]
0.747
0.764
0.791
0.811
0.817
0.786
0.075
0.079
0.080
0.078
0.110
0.085
FT
0.756
0.781
0.803
0.833
0.834
0.801
0.073
0.076
0.077
0.072
0.107
0.081
Distil-Qwen-14B
ZS[ctrl]
0.650
0.704
0.749
0.711
0.743
0.712
0.088
0.082
0.089
0.115
0.141
0.103
ZS
0.654
0.716
0.756
0.731
0.746
0.721
0.088
0.081
0.086
0.110
0.136
0.100
FT[ctrl]
0.751
0.784
0.799
0.807
0.833
0.795
0.066
0.074
0.084
0.083
0.103
0.082
FT
0.777
0.816
0.827
0.851
0.861
0.826
0.061
0.068
0.077
0.070
0.099
0.075
Distil-Qwen-32B
ZS[ctrl]
0.649
0.671
0.721
0.674
0.743
0.691
0.089
0.105
0.099
0.131
0.126
0.110
ZS
0.658
0.683
0.719
0.695
0.749
0.701
0.088
0.105
0.101
0.129
0.125
0.110
FT[ctrl]
0.776
0.789
0.799
0.794
0.821
0.796
0.066
0.071
0.074
0.087
0.111
0.082
FT
0.800
0.821
0.815
0.830
0.846
0.822
0.062
0.067
0.073
0.078
0.110
0.078
Table 4: Main results for predicting country-level survey response distributions on the WVS data. We test all
models with zero-shot prompting (ZS) and our proposed fine-tuning approach (FT). [ctrl] indicates a control setup,
where we randomly replace countries in test prompts with other countries, to evaluate country context sensitivity.
We report Jensen-Shannon Divergence (1−JSD , ↑) and Earth Mover Distance (EMD, ↓).
JSD, where JSD is Jensen-Shannon divergence,
also employed by Durmus et al. (2023), is a sym-
metric measure of the similarity between two
probability distributions, with higher values in-
dicating greater similarity; ii) Earth Mover Dis-
tance (EMD; Rubner et al., 1998), also known as
the Wasserstein distance, quantifies the minimum
amount of work required to transform one distri-
bution into another, with lower values indicating
greater similarity in distribution. Both the 1-JSD
and EMD metrics range from 0 to 1.
6
Results
We investigate two primary research questions:
RQ1 How effectively does the proposed alignment
method improve the distribution simulation of
the model on unseen countries and questions?
RQ2 What is necessary to perform well on the
task—how much is dependent on modeling
the prior distribution, and how much on con-
text sensitivity?
We present comprehensive experimental results to
address the two research questions.
6.1
RQ1: Generalization Performance
To address RQ1 (how effectively FT improves dis-
tribution simulation on unseen countries and ques-
tions), we train the selected models using our pro-
posed simulation methods and evaluate their perfor-
mance on unseen countries and questions. Table 4
presents the evaluation scores across models of
varying sizes and types.
Zero-shot [ZS] vs. Fine-tuning [FT].
Across all
model sizes and types, we observe that zero-shot
prompting (ZS) consistently yields worse scores
compared to fine-tuned models (FT), indicating
that while ZS is capable of addressing unseen coun-
tries and questions, it lacks the adaptability needed
for effective distribution simulation. In contrast,
fine-tuned models show improved performance,
with higher 1−JSD and lower EMD scores (e.g., a
34.3% 1−JSD increase and 0.069 EMD decrease
for Llama3-8B-Instruct Avg.), demonstrating their
enhanced ability to align with real-world distribu-
tions. This suggests that fine-tuning enables models
to internalize more detailed patterns and relation-
ships, making them more effective for simulation.

--- Page 6 ---

Unseen Countries vs. Unseen Questions.
The
generalization capabilities are revealed by evalua-
tion on unseen attributes. Across all models and
settings, unseen questions (Q3) tend to present a
greater challenge than unseen countries (C2 or C3),
as indicated by slightly worse scores for unseen
questions (e.g., 0.781 vs. 0.886 1−JSD for Llama3-
Instruct). This suggests that while the models are
reasonably robust in handling new country distribu-
tions, they struggle more with generating accurate
distributions for questions that were not encoun-
tered during training.
Comparison
Across
Models.
Our
method
demonstrates consistent performance improve-
ments across three representative model families
and various model sizes, highlighting the effec-
tiveness of our proposed first-token alignment ap-
proach. Specifically, while there are notable per-
formance differences in the zero-shot setting—for
example, Llama3-Base achieves a higher 1−JSD
value (0.765) compared to Llama3-Instruct (0.613),
suggesting that the base model better predicts the
option token distribution—our fine-tuning proce-
dure significantly bridges this gap.
After fine-
tuning, Llama3-Instruct not only closes the initial
performance disparity but even surpasses Llama3-
Base (34.3% 1−JSD increase vs. 6.1% increase).
Similarly, experiments with Distilled Qwen mod-
els of different sizes reveal no clear scaling trends.
Moreover, although Vicuna1.5 is generally con-
sidered weaker compared to Llama and Qwen, it
surprisingly delivers similarly competitive results
on this task. Overall, analysis across all models
further revealing the finding that, regardless of the
starting model, our fine-tuning approach con-
sistently produces models with similar strong
performance on our task.
Correlation Between First-Token Distribution
and Response Accuracy.
Beyond the alignment
of first-token distributions, we further evaluate of
the mode accuracy of models in responding to
questionnaire items following fine-tuning. We con-
sider the options with the highest probabilities as
(single, argmax) predictions and calculate accu-
racy against the survey majority choice per country
(Arora et al., 2023; Cao et al., 2023; AlKhamissi
et al., 2024). As depicted in Figure 2, our findings
reveal a significant increase in accuracy across all
models and test subsets, highlighting the effective-
ness of the fine-tuning process. Notably, perfor-
mance improvements are particularly significant in
Figure 2: Option prediction accuracy for cultural ques-
tions using the Llama3-8B-Instruct. The final option
is simulated by selecting the option with the highest
probabilities, compared against human majority choice.
unseen countries, as demonstrated by C2-Q1 and
C3-Q1 subsets. These results suggest that our pro-
posed method not only improves the simulation of
option distributions but also strengthens the models’
alignment with the correct responses, underscoring
the interdependence of distribution alignment and
answer accuracy.
6.2
RQ2: Variation Sensitivity
To address RQ2 (contribution of modeling the prior
distribution vs. context sensitivity), we compare the
control setting (with countries randomly replaced),
analyze diversity changes of models, and explore
shifts in response accuracy for unseen countries.
ZS[ctrl] vs.
FT[ctrl].
In the control setting,
ZS[ctrl] shows a smaller performance drop than ZS,
while FT[ctrl] sees a larger decline, with a 16.7%
avg. (1−JSD) drop between FT[ctrl] and FT across
seven models, compared to 3.7% for ZS[ctrl] and
ZS. This indicates that fine-tuned models (FT) are
more sensitive to the country context and not just
the prior distribution of responses (which FT[ctrl]
is trained to simulate), suggesting they have be-
come more specialized in capturing cultural nu-
ances during training. In contrast, the smaller gap
between ZS and ZS[ctrl] implies that zero-shot
models maintain a more generalized understanding
of cultural contexts, making them less affected by
random permutations of country data. This differ-
ence highlights the fine-tuned models’ improved
capability in simulating response distributions for
specific countries.
Country Diversity in Model Outputs.
We de-
fine diversity as the divergence across countries
of response distributions given the same question.

--- Page 7 ---

(a) Llama-Base (ZS)
(b) Llama-Base (FT)
(c) Llama-Instruct (ZS)
(d) Llama-Instruct (FT)
(e) Country Accuracy on C2-Q1
(f) Country Accuracy on C2-Q3
Figure 3: Model Diversity and Country Accuracy Analysis. (a)-(d) denotes the comparison of 1−JSD scores across
countries for specific questions (C2-Q3 and C3-Q3). The blue-shaded area represents diversity changes, with the
lower boundary indicating the mean of survey response scores and the upper boundary representing the mean of
model outputs. (e)-(f) denotes the accuracy of options on African countries in both C2-Q1 and C2-Q3.
Base Model
Methods
(1−JSD) ↑
EMD ↓
C1-Q3
C2-Q1
C2-Q3
C3-Q1
C3-Q3
Avg.
C1-Q3
C2-Q1
C2-Q3
C3-Q1
C3-Q3
Avg.
Llama3-8B-Instruct
ZS
0.603
0.654
0.601
0.659
0.613
0.626
0.125
0.140
0.131
0.145
0.132
0.135
FT
0.777
0.852
0.789
0.870
0.791
0.816
0.081
0.078
0.087
0.065
0.073
0.077
Distil-Qwen-7B
ZS
0.605
0.706
0.712
0.696
0.693
0.682
0.084
0.091
0.086
0.087
0.190
0.108
FT
0.764
0.779
0.771
0.791
0.851
0.791
0.067
0.085
0.081
0.082
0.130
0.089
Table 5: Model Performance on Chinese World Values Survey. Performance comparison between zero-shot
prompting (ZS) and supervised fine-tuning (SFT) on two model families.
To assess whether FT can enhance model output
diversity, we calculate 1−JSD for Llama3-Base
and Llama3-Instruct (ZS and FT) output across
countries for each question. A lower 1−JSD score
suggests greater diversity in responses between
countries, whereas a higher score indicates greater
similarity in distributions. Results are shown in
Figure 3, where the scores of survey responses are
compared with those of the model predictions.
This visualization provides several interesting
insights. Firstly, the outputs of Base models exhibit
a high degree of uniformity across countries, indi-
cating a limited sensitivity to national variations
when addressing cultural values questions. After
fine-tuning, there is a slight reduction in 1−JSD,
suggesting an enhancement in the responsiveness
to diverse cultural contexts. Secondly, although the
Instruct model, having undergone alignment fine-
tuning, initially produces a more varied distribution
of answers, this diversity diminishes following
distribution simulation fine-tuning. Thirdly, we
observe no consistent correlation between the di-
versity of generated responses and the accuracy
of simulated distributions. Lastly, the post-fine-
tuning diversity of responses from both models
converges, indicating that our fine-tuning approach
improves the sensitivity to national differences.
Unseen Country Shifts.
We visualize the option
accuracy of African countries as observation ob-
jects in Figure 3e-3f. For seen questions, we find
that all models show a relatively high performance
across most countries, with Ethiopia and Nigeria
displaying the highest accuracies close to 80%.
For unseen questions, the performance decreases
greatly compared to seen questions, particularly

--- Page 8 ---

Methods
C′
1
C3
(1−JSD) ↑
ACC ↑
(1−JSD) ↑
ACC ↑
Vicuna1.5 (ZS)
0.690
0.360
0.668
0.346
Vicuna1.5 (FT)
0.725
0.442
0.709
0.456
Llama3 (ZS)
0.617
0.472
0.613
0.446
Llama3 (FT)
0.767
0.562
0.755
0.568
Table 6: Evaluation results on GlobalOpinionQA Pew
dataset for Llama3-Instruct and Vicuna1.5-7B. (1−JSD)
and option accuracy scores are reported.
in countries like Egypt and Tunisia. Besides, the
Instruct models maintain a higher level of accuracy
relative to the Base models in most cases, showing
the relative robustness of Instruct models in both
seen and unseen scenarios across the African coun-
tries, which is consistent with results in Figure 2.
6.3
Robustness Analysis
In this section, we explore the robustness of the
models on survey language and unseen survey.
Impact of Survey Language on Results.
We
fine-tuned the Llama3-8B-Instruct and Distil-
Qwen-7B models on the official Chinese transla-
tion dataset, and the results are presented in Table 5.
While the performance of both models in Chinese
is marginally lower than in English both on (1-JSD)
and EMD metrics, the difference is not significant,
suggesting that current LLMs exhibit limited sensi-
tivity to language differences in this task. Besides,
while the Distilled-Qwen model demonstrates a bet-
ter performance than Llama3 on most benchmarks,
it does not outperform Llama3 in this task.
Generalization to a New Survey.
We use Pew
introduced in §3.4 to test the generalization of our
fine-tuned models. Table 6 presents the results
in both 1−JSD scores and accuracy. Notably, all
metric scores show significant improvements for
both models after fine-tuning. Additionally, across
both C′
1 and C3, Llama3 outperforms Vicuna1.5
in terms of accuracy, particularly in the fine-tuned
setting, where Llama3 (FT) achieves 19.1% and
27.4% improvement for two datasets, respectively.
The consistent improvements prove its capability
to generalize well to unseen surveys.
6.4
Ablation Studies
We conduct ablation studies to analyze the impact
of the training loss function and option ordering.
Loss Function.
As shown in Table 7, KL Loss is
the most effective loss function for our task. How-
Methods
C1-Q3
C2-Q1
C2-Q3
C3-Q1
C3-Q3
KL (Orig)
0.777
0.881
0.783
0.890
0.784
WA Loss
0.733
0.774
0.744
0.782
0.749
JS Loss
0.745
0.790
0.756
0.799
0.763
CE Loss
0.746
0.809
0.772
0.807
0.756
Shuffled
0.753
0.820
0.761
0.815
0.761
Table 7: Results of our ablation studies. We compare
different loss functions (WA, JS and CE) to our KL loss
setup. We also evaluate on a test set with shuffled option
orders. All results are for Llama3-8B-Instruct.
ever, Wasserstein (WA) Loss Jensen-Shannon (JS),
and Cross-Entropy (CE) Loss also improve over
zero-shot prompting.
Option Ordering.
Dominguez-Olmedo et al.
(2023) observed an A-bias effect, where models
tend to disproportionately select the answer choice
labeled “A”. To assess this bias, we re-evaluate our
fine-tuned model on the same dataset where the
answer options are shuffled. As shown in Table 7
(“Shuffled”), there is a reduction in performance,
but it is small compared to the effect of fine-tuning
or model choice. This indicates that the option
ordering is not a major concern in our experiments.
7
Conclusion
In this paper, we explored the task of specialising
LLMs to simulate survey response distributions
across diverse countries and questions. For this
task, we devised a fine-tuning method based on
first-token probabilities. Our experiments demon-
strate that fine-tuning models substantially im-
proves response simulation prediction compared to
zero-shot models, for both seen and unseen coun-
tries and questions. Further, fine-tuned models also
show improved generalization to an entirely new
survey dataset. Despite these improvements, our
results also highlight systematic limitations of the
models, particularly when simulating responses to
unseen questions. We also observed that the mod-
els, whether fine-tuned or not, were less diverse
in their predictions compared to the human survey
response data, raising questions about their utility.
While our results provide clear evidence for the
benefits of specializing LLMs for survey simula-
tion tasks, they also underscore the need for cau-
tion when using LLMs for this task, as even the
best-performing models exhibited systematic inac-
curacies, especially in culturally diverse contexts.

--- Page 9 ---

Limitations
While we proved the effectiveness of our proposed
method, several limitations remain in our work.
Scope.
Our trained models are highly specialized
and can only be used for the specific task of pre-
dicting the distribution of answers to a given survey
question from a specified human population. Fu-
ture work will investigate whether the fine-tuning
approach also results in less biased or more aligned
models in general-purpose applications, but this
cannot be claimed only based on our study.
Language and Countries Coverage.
Our study
only uses English prompts for experiments and uses
countries to represent specific cultures, consistent
with existing studies (Cao et al., 2023; AlKhamissi
et al., 2024). While this approach offers some valu-
able insights, it may limit the applicability of our
findings to non-English LLMs and diverse fine-
grained cultural contexts. We hope that future re-
search could benefit from exploring broader lan-
guages and countries to enhance the robustness of
the proposed framework.
Model Choice.
Due to computational resource
consideration, we did not fine-tune LLMs with
more than 32B parameters and instead selected
a limited number of models for validation. Despite
this limitation, in future work, we aim to cover a
range of powerful models of varying sizes, which
will allow us to uncover interesting observations
regarding their performance. We believe that the
insights we draw will still contribute to future re-
search, encouraging further exploration of larger
models to better understand their capabilities in
simulating cultural diversity.
Ethics Statement
This research adheres to strict ethical standards,
ensuring that all datasets, large language models,
and prompt settings used are sourced from open-
access repositories and are properly licensed to
their original creators.
While our proposed framework does not involve
any inherently risky operations, we acknowledge
that the deployment of LLMs carries inevitable
potential ethical implications. Therefore, users in-
teracting with our models are strongly encouraged
to consider safety and ethical factors, remaining
aware of the potential risks and harms that may
arise from misuse or misinterpretation of the gen-
erated content. Through this work, we aim to con-
tribute positively to a better understanding of cul-
tural diversities and promote responsible practices
in the simulation of cultural contexts.
Acknowledgments
We thank anonymous reviewers for their valuable
comments. This research was co-funded by a DFF
Sapere Aude research leader grant under grant
agreement No 0171-00034B, and supported by the
Pioneer Centre for AI, DNRF grant number P1.
Yong Cao was supported by a VolkswagenStiftung
Momentum grant.
References
Gati V Aher, Rosa I Arriaga, and Adam Tauman Kalai.
2023. Using large language models to simulate mul-
tiple humans and replicate human subject studies.
In International Conference on Machine Learning,
pages 337–371. PMLR.
AI@Meta. 2024. Llama 3 model card.
Badr AlKhamissi,
Muhammad ElNokrashy,
Mai
Alkhamissi, and Mona Diab. 2024. Investigating
cultural alignment of large language models. In Pro-
ceedings of the 62nd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long
Papers), pages 12404–12422. Association for Com-
putational Linguistics.
Lisa P Argyle, Ethan C Busby, Nancy Fulda, Joshua R
Gubler, Christopher Rytting, and David Wingate.
2023.
Out of one, many: Using language mod-
els to simulate human samples. Political Analysis,
31(3):337–351.
Arnav Arora, Lucie-aimée Kaffee, and Isabelle Augen-
stein. 2023. Probing pre-trained language models for
cross-cultural differences in values. In Proceedings
of the First Workshop on Cross-Cultural Considera-
tions in NLP (C3NLP), pages 114–130. Association
for Computational Linguistics.
Joris Baan, Wilker Aziz, Barbara Plank, and Raquel
Fernandez. 2022. Stop measuring calibration when
humans disagree. In Proceedings of the 2022 Con-
ference on Empirical Methods in Natural Language
Processing, pages 1892–1915. Association for Com-
putational Linguistics.
Joris Baan, Raquel Fernández, Barbara Plank, and
Wilker Aziz. 2024. Interpreting predictive proba-
bilities: Model confidence or human label variation?
In Proceedings of the 18th Conference of the Euro-
pean Chapter of the Association for Computational
Linguistics (Volume 2: Short Papers), pages 268–277.
Association for Computational Linguistics.

--- Page 10 ---

Christopher A Bail. 2024. Can generative ai improve so-
cial science? Proceedings of the National Academy
of Sciences, 121(21):e2314021121.
Noam Benkler, Drisana Mosaphir, Scott Friedman, An-
drew Smart, and Sonja Schmer-Galunder. 2023. As-
sessing LLMs for moral value pluralism.
arXiv
preprint arXiv:2312.10075.
James Bisbee, Joshua D Clinton, Cassy Dorff, Brenton
Kenkel, and Jennifer M Larson. 2023. Synthetic
replacements for human survey data? the perils of
large language models. Political Analysis, pages 1–
16.
Yong Cao, Li Zhou, Seolhwa Lee, Laura Cabello, Min
Chen, and Daniel Hershcovich. 2023.
Assessing
cross-cultural alignment between ChatGPT and hu-
man societies: An empirical study. In Proceedings
of the First Workshop on Cross-Cultural Considera-
tions in NLP (C3NLP), pages 53–67. Association for
Computational Linguistics.
Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng,
Zhanghao Wu, Hao Zhang, Lianmin Zheng, Siyuan
Zhuang, Yonghao Zhuang, Joseph E. Gonzalez, Ion
Stoica, and Eric P. Xing. 2023. Vicuna: An open-
source chatbot impressing GPT-4 with 90%* Chat-
GPT quality.
Ricardo Dominguez-Olmedo, Moritz Hardt, and Celes-
tine Mendler-Dünner. 2023. Questioning the survey
responses of large language models. arXiv preprint
arXiv:2306.07951.
Esin Durmus, Karina Nyugen, Thomas I Liao, Nicholas
Schiefer, Amanda Askell, Anton Bakhtin, Carol
Chen,
Zac Hatfield-Dodds,
Danny Hernandez,
Nicholas Joseph, et al. 2023. Towards measuring
the representation of subjective global opinions in
language models. arXiv preprint arXiv:2306.16388.
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song,
Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma,
Peiyi Wang, Xiao Bi, et al. 2025. Deepseek-r1: In-
centivizing reasoning capability in llms via reinforce-
ment learning. arXiv preprint arXiv:2501.12948.
C. Haerpfer, R. Inglehart, A. Moreno, C. Welzel,
K. Kizilova, J. Diez-Medrano, M. Lagos, P. Nor-
ris, E. Ponarin, and B. Puranen. 2022. World values
survey wave 7 (2017-2022) cross-national data-set.
Guande He, Peng Cui, Jianfei Chen, Wenbo Hu, and Jun
Zhu. 2024. Investigating uncertainty calibration of
aligned language models under the multiple-choice
setting.
Luke Hewitt, Ashwini Ashokkumar, Isaias Ghezae, and
Robb Willer. 2024. Predicting results of social sci-
ence experiments using large language models.
John J Horton. 2023. Large language models as sim-
ulated economic agents: What can we learn from
homo silicus? Technical report, National Bureau of
Economic Research.
Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan
Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and
Weizhu Chen. 2022. LoRA: Low-rank adaptation of
large language models. In International Conference
on Learning Representations.
Austin Kozlowski and James Evans. 2024. Simulating
subjects: The promise and peril of ai stand-ins for
social agents and interactions.
Louis Kwok, Michal Bravansky, and Lewis D Griffin.
2024. Evaluating cultural adaptability of a large lan-
guage model via simulation of synthetic personas.
arXiv preprint arXiv:2408.06929.
Wangyue Li, Liangzhi Li, Tong Xiang, Xiao Liu, Wei
Deng, and Noa Garcia. 2024. Can multiple-choice
questions really be useful in detecting the abilities
of LLMs?
In Proceedings of the 2024 Joint In-
ternational Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 2819–2834. ELRA and ICCL.
Benjamin S Manning, Kehang Zhu, and John J Horton.
2024. Automated social science: Language models
as scientist and subjects. Technical report, National
Bureau of Economic Research.
Peter S Park, Philipp Schoenegger, and Chongyang Zhu.
2024. Diminished diversity-of-thought in a standard
large language model. Behavior Research Methods,
pages 1–17.
Yossi Rubner, Carlo Tomasi, and Leonidas J Guibas.
1998. A metric for distributions with applications to
image databases. In Sixth international conference
on computer vision (IEEE Cat. No. 98CH36271),
pages 59–66. IEEE.
Seungjong Sun, Eungu Lee, Dongyan Nan, Xiangy-
ing Zhao, Wonbyung Lee, Bernard J. Jansen, and
Jang Hyun Kim. 2024. Random silicon sampling:
Simulating human sub-population opinion using a
large language model based on group-level demo-
graphic information. Preprint, arXiv:2402.18144.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro,
Faisal Azhar, et al. 2023. Llama: Open and effi-
cient foundation language models. arXiv preprint
arXiv:2302.13971.
Dustin Wright, Arnav Arora, Nadav Borenstein, Sr-
ishti Yadav, Serge Belongie, and Isabelle Augenstein.
2024. Revealing fine-grained values and opinions in
large language models.
Yahan Yang, Soham Dan, Dan Roth, and Insup Lee.
2024. On the calibration of multilingual question
answering llms. Preprint, arXiv:2311.08669.
Wenlong Zhao, Debanjan Mondal, Niket Tandon, Dan-
ica Dillion, Kurt Gray, and Yuling Gu. 2024. World-
valuesbench: A large-scale benchmark dataset for

--- Page 11 ---

multi-cultural value awareness of language mod-
els. In Proceedings of the 2024 Joint International
Conference on Computational Linguistics, Language
Resources and Evaluation (LREC-COLING 2024),
pages 17696–17706.
A
Pew Data Distribution
The detailed statistics for the C2 and C3 split of
the cultural survey simulation and the C3 split of
GlobalOpinionQA data mentioned are available in
Table 8. The sampled countries, along with the
sampling reason of Pew-C′
1, are in Table 9.
C2
C3
Country
CSS-N
Country
CSS-N
PWE-N
Egypt
157
Malaysia
150
516
Ethiopia
185
Thailand
150
319
Kenya
185
Czechia
150
212
Libya
185
Greece
150
648
Morocco
184
Nigeria
210
1044
Nigeria
185
Morocco
209
450
Tunisia
184
Peru
146
545
Zimbabwe
185
Colombia
150
369
Mexico
150
890
Puerto Rico
150
221
New Zealand
149
274
Table 8: Number of Entries Used in C2 and C3 Split of
Cultural Survey Simulation and C3 Split of GlobalOp-
inionQA Data.
Country
Continent
GDP-level
N
Germany
Europe
High
1130
Japan
Asia
High
891
Brazil
South America
Upper-middle
922
Australia
Oceania
High
627
India
Asia
Lower-middle
932
Nigeria
Africa
Lower-middle
1044
United States
North America
High
1104
Vietnam
Asia
Lower-middle
471
Chile
South America
Upper-middle
542
Ukraine
Europe
Lower-middle
661
Table 9: Sampled countries for Pew-C′
1 regarding geo-
graphical and GDP-level diversity. The dataset consists
of 8,324 entries in total.
B
WVS data Distribution
Figure 4 illustrates the sample distribution across
various countries in World Values Survey. For the
purpose of balanced representation, in our format-
ted dataset, we only include countries with more
than 1,000 samples, ensuring consistency in data
distribution across countries and minimizing sam-
ple size discrepancies in the analysis.
Set
Cultural Dimension
Number
Q1
Social values, attitudes and stereotypes
45
Societal well-being
12
Social capital, trust and organizational membership
49
Economic values
6
Corruption
9
Migration
10
Post-materialist index
21
Science and technology
6
Religious values
6
Q2
Security
12
Ethical values and norms
23
Q3
Political interest and political participation
36
Political culture and political regimes
25
C1
Andorra, Argentina, Australia, Bangladesh, Armenia,
Bolivia, Brazil, Myanmar, Canada, Chile, China, Tai-
wan ROC, Cyprus, Ecuador, Germany, Guatemala, Hong
Kong SAR, Indonesia, Iran, Iraq, Japan, Kazakhstan,
Jordan, South Korea, Kyrgyzstan, Lebanon, Macao
SAR, Maldives, Mongolia, Netherlands, Nicaragua, Pak-
istan, Philippines, Romania, Russia, Serbia, Singapore,
Slovakia, Vietnam, Tajikistan, Turkey, Ukraine, Great
Britain, United States, Uruguay, Venezuela
46
C2
Egypt, Ethiopia, Kenya, Libya, Morocco, Nigeria,
Tunisia, Zimbabwe
8
C3
Malaysia, Thailand, Czechia, Greece, Nigeria, Morocco,
Peru, Colombia, Mexico, Puerto Rico, New Zealand
11
Table 10: Cultural dimensions and question ids of WVS.
Question 82-223 and 94-106 are excluded in Q1 as
they are demo graphical questions. Demo graphical
questions are excluded as they are related to individual
attribute regarding participants and does not have rele-
vance to group culture.
Regarding dataset split, we split WVS by cul-
tural dimensions and countries vis multiple sets,
which is visualized in Figure 5 and the correspond-
ing cultural dimensions are detailed in Table 10,
offering a comprehensive view of the overall distri-
bution in the cultural survey simulation.
C
Hyperparameter Settings
Training is performed on a single A100 GPU with
a batch size of 16 for Llama3 and Vicuna1.5-7B,
and 4 for Vicuna1.5-13B. Both models use the
AdamW optimizer with a learning rate of 1e-4 and
implement Fully Sharded Data Parallel along with
a mixed precision strategy to enhance computa-
tional efficiency. In our experiments, we employ
LoRA with a rank of 8, a scaling factor lora_alpha
set to 32, and a dropout rate of 0.05.
Model Download
We list all used models here:
• Vicuna1.5-7B: https://huggingface.co/
lmsys/vicuna-7b-v1.5
• Vicuna1.5-13B: https://huggingface.co/
lmsys/vicuna-13b-v1.5

--- Page 12 ---

Figure 4: Sample distribution of the World Values Survey across countries, including only countries with more than
1,000 samples for balanced representation.
(a) Country distribution across training, validation, and testing sets.
(b) Cultural dimension distribution.
Figure 5: Visualization of country and cultural dimension divisions of WVS. Countries are categorized into three
groups, and questions are divided based on selected cultural dimensions.
• Distil-Qwen-7B:
https://
huggingface.co/deepseek-ai/
DeepSeek-R1-Distill-Qwen-7B
• Distil-Qwen-14B:
https://
huggingface.co/deepseek-ai/
DeepSeek-R1-Distill-Qwen-14B
• Distil-Qwen-32B:
https://
huggingface.co/deepseek-ai/
DeepSeek-R1-Distill-Qwen-32B
• Llama3-8B-Base:
https://huggingface.
co/meta-llama/Meta-Llama-3-8B
• Llama3-8B-Instruct:
https:
//huggingface.co/meta-llama/
Meta-Llama-3-8B-Instruct
• Qwen-7B:
https://huggingface.co/
Qwen/Qwen-7B
D
More Option Prediction Analysis
Option Prediction Accuracy.
In line with Fig-
ure 3e-3f, we present the remaining two sets of
Llama3 option prediction accuracy for C3-Q1 and
C3-Q3 here (see Figure 6).
The results indicate that the model performs sig-
nificantly better on seen questions (C3-Q1) com-
pared to unseen ones (C3-Q3), with Llama3 In-
struct models consistently outperforming Base
models, and fine-tuned approaches demonstrating
superior accuracy over zero-shot methods across
most countries. Specifically, the model achieves
its highest accuracy in Greece, Nigeria, and Peru,
while showing weaker performance in Thailand
and Mexico. Despite the challenges in predicting
unseen questions, fine-tuning through simulation
leads to noticeable improvements, highlighting the
potential of fine-tuned models to enhance general-
ization in novel scenarios.
Country Distributions.
Figure 8 visualizes the
distribution of 1−JSD scores for the Llama3-Base
and Llama3-Instruct models across unseen cultural
questions (C1-Q3) in both zero-shot (ZS) and fine-
tuned (FT) modes. In ZS mode, both models per-
form poorly across many regions, with lower scores
indicating limited cultural sensitivity. This sug-

--- Page 13 ---

(a) Country Accuracy on C3-Q1.
(b) Country Accuracy on C3-Q3.
Figure 6: Llama3 Accuracy of options on African coun-
tries in both seen C3-Q1 and unseen C3-Q3 questions.
gests that without additional tuning, both models
struggle to effectively generalize to simulate cultur-
ally diverse distributions. Furthermore, the Instruct
model performs slightly worse, likely due to the
reinforcement learning and safety strategies, which
may inadvertently reduce its sensitivity to cultures
in this scenario.
However, after FT, both models show improve-
ment across all countries, particularly significant
in regions previously displaying poor performance
in the ZS setting. Additionally, the performance
of both the fine-tuned Base model and the Instruct
model is observed to be very similar across differ-
ent countries, demonstrating that our methods can
Figure 7: Training loss comparsion of three mod-
els:
Qwen-7B, Llama-8B-Instruct,
Distill-Qwen-
32B(Deepseek)
effectively align the Base and Instruct models.
E
More Baseline Comparsion
To further assess the effectiveness of our proposed
approach, we compare it against several other base-
line methods as follows:
• KNN: This method identifies the most similar
training question and country (top-1, k = 1)
using BERT embeddings and returns the cor-
responding option distributions as predictions.
• Avg_Culture: We computes the mean option
distribution across all training countries for
each known question and adopts a uniform
random distribution for unknown questions.
• JSON-ZS: This approach prompts the mod-
els to directly generate option distributions in
JSON format without additional fine-tuning.
Table 11 presents the 1-JSD scores for various
baseline methods and our proposed approach. The
results indicate that all baseline methods perform
substantially worse than our fine-tuned (FT) mod-
els. Among the baselines, the JSON-ZS method
demonstrates superior performance compared to
KNN and Avg_Culture; however, it remains less
effective than both zero-shot (ZS) and fine-tuned
(FT) approaches. Notably, fine-tuning consistently
yields the highest scores across all evaluated set-
tings, underscoring its effectiveness in improving
model performance.

--- Page 14 ---

(a) Llama3_Base_ZS
(b) Llama3_Base_FT
(c) Llama3_Instruct_ZS
(d) Llama3_Instruct_FT
Figure 8: Distribution of 1−JSD Global Scores for the Model on Unseen Cultural Questions (C1-Q3). The Instruct
model exhibits a more distinct improvement compared to the Base model.
Methods
C1-Q3
C2-Q1
C2-Q3
C3-Q1
C3-Q3
Avg.
KNN
0.381
0.518
0.371
0.541
0.384
0.439
Avg_Culture
0.360
0.509
0.348
0.518
0.368
0.421
Llama3-8B-Base
JSON-ZS
0.754
0.728
0.581
0.729
0.751
0.709
ZS
0.749
0.768
0.759
0.781
0.770
0.765
FT
0.770
0.858
0.773
0.877
0.781
0.812
Llama3-8B-Instruct
JSON-ZS
0.735
0.728
0.747
0.729
0.751
0.738
ZS
0.585
0.650
0.589
0.657
0.584
0.613
FT
0.777
0.881
0.783
0.890
0.784
0.823
Table 11: Comparison of 1-JSD scores across different
baseline methods and our approach. Higher values indi-
cate better alignment with the ground-truth distribution.
F
More Model Evaluation
In this section, we present additional experiment
results on original Qwen model. We observe that
the original Qwen models present challenges in
training for our task. As shown in Figure 7, we
compare the training progress of three models. The
loss of the Qwen-7B model exhibits difficulty in
converging compared to Llama-8B-Instruct and
Distill-Qwen-32B. This difficulty may stem from
the extensive safety alignment or policy alignment
incorporated into Qwen, which could introduce
additional constraints or optimization challenges
during training.
Secondly, we visualized the 1-JSD score distribu-
tion of the model for English ZS, FT, and Chinese
FT, as shown in Figure 9, with the red dashed line
indicating the average value. The results show that
Figure 9: Comparsion of different languages in 1-JSD
score on random selected 100 samples.
language differences have a smaller impact on the
model than training levels. Additionally, we cal-
culate the Pearson correlation coefficient between
English ZS and FT which (0.349) is lower than
that between English FT and Chinese FT (0.579).
While both correlations are positive, the stronger
correlation observed between English FT and Chi-
nese FT suggests that training level exerts a greater
influence than language differences.

```
