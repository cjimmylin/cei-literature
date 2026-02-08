---
title: "2024-Yuan-Social Measuring Social Norms of LLMs - PDF Extract"
source_pdf: "2024-Yuan-Social Measuring Social Norms of LLMs.pdf"
pages: 50
extracted_at: "2026-02-07T17:00:45.834592"
---

# PDF Extract: 2024-Yuan-Social Measuring Social Norms of LLMs

**Source PDF:** 2024-Yuan-Social Measuring Social Norms of LLMs.pdf
**Total Pages:** 50

---

## Content

```
--- Page 1 ---

Measuring Social Norms of Large Language Models
Ye Yuan1,2,3, Kexin Tang1,2, Jianhao Shen1,2, Ming Zhang1,2,3†, Chenguang Wang4†
1School of Computer Science, Peking University
2National Key Laboratory for Multimedia Information Processing, Peking University
3Peking University-Anker Embodied AI Lab
4Washington University in St. Louis
{yuanye_pku,jhshen,mzhang_cs}@pku.edu.cn
tkx@stu.pku.edu.cn, chenguangwang@wustl.edu
Abstract
We present a new challenge to examine whether
large language models understand social norms.
In contrast to existing datasets, our dataset re-
quires a fundamental understanding of social
norms to solve. Our dataset features the largest
set of social norm skills, consisting of 402
skills and 12, 383 questions covering a wide
set of social norms ranging from opinions and
arguments to culture and laws.
We design
our dataset according to the K-12 curriculum.
This enables the direct comparison of the so-
cial understanding of large language models
to humans, more specifically, elementary stu-
dents. While prior work generates nearly ran-
dom accuracy on our benchmark, recent large
language models such as GPT3.5-Turbo and
LLaMA2-Chat are able to improve the perfor-
mance significantly, only slightly below human
performance. We then propose a multi-agent
framework based on large language models to
improve the models’ ability to understand so-
cial norms. This method further improves large
language models to be on par with humans.
Given the increasing adoption of large language
models in real-world applications, our finding
is particularly important and presents a unique
direction for future improvements.
1
Introduction
Large language models (LLMs) such as GPT-
4 (OpenAI, 2023) and Gemini (Gemini Team,
2023) have significantly advanced text understand-
ing and generation. These models have become
increasingly adopted in broad applications. Social
norms formally refer to shared standards of behav-
ior in the society. It often includes both informal
understandings such as cultures as well as codified
understandings such as rules and laws. Despite
their widespread application, there is a debate on
†Corresponding authors.
The code and dataset are available at https://
huggingface.co/datasets/socialnormdataset/social.
whether these models are consistent with human
and societal values and norms. This has resulted in
the issuance of AI safety whitepapers advocating
for the halting of certain model developments, as
well as government executive orders endorsing the
creation of only trustworthy AI systems. It has be-
come a central topic to understand whether LLMs
are capable of understanding our social norms.
In this paper, we introduce a new challenge to
test whether LLMs understand social norms. Un-
like existing datasets that mainly evaluate a gen-
eral understanding of social science (Hendrycks
et al., 2021a; Lu et al., 2022; Liang et al., 2022;
Srivastava et al., 2022), our dataset focuses on ex-
amining the fundamental understanding of social
norms. Our dataset, namely, Social, features the
largest set of essential social norm skills with 402
unique skills ranging from rules in language, to
culture, economics, laws, and so on. It consists of
12, 383 questions to support the test of these skills.
Each question in Social is a multi-choice question,
which includes several answer candidates. Exam-
ple questions are shown in Figure 1(a). Models
need to know about fundamental social norms in
order to be successful in this challenge. Our design
strictly follows the social norm evaluation of hu-
mans. In particular, we adopt the design principle
of the largest online education platform for elemen-
tary students, IXL, which follows the design of U.S.
National Education. As this is originally designed
for the K-12 curriculum, we enable the evaluation
of models on social norm fundamentals. Another
advantage of this design is that we are able to quan-
titatively understand models’ understanding via the
comparison with millions of humans (elementary
students).
We empirically evaluate the performance of
LLMs on our dataset. We conducted the exper-
iments using both LLaMA2-Chat and GPT3.5-
Turbo. Results show that recent advancements
in LLMs have significantly improved the models’
arXiv:2404.02491v4  [cs.CL]  22 May 2024

--- Page 2 ---

Question: Which sentence states a fact?
(A) The spinach plant is native to Asia.
(B) Spinach tastes worse than any other vegetable.
(C) People rely heavily on the resources rainforests provide.
(D) The construction cost a ridiculous amount of money.
Question: Which is an example of a law?
(A) You must clean the dishes.
(B) If the traffic light is red, you must stop.
(C) You should exercise three times a week.
(D) Only kids 12 and under can order off the kids' menu.
Social
(ii) Language Arts
(i) Social Studies
MMLU
ScienceQA
HELM
BigBench
Question: Which of the following did Domhoff not 
identify as a process of decision-making in the USA?
(A)the ideology process
(B) the exploitation process
(C) the policy-formation process
(D)the candidate-selection process
Question: Which text uses the word factoid in its traditional sense?
(A) As a geneticist, Jackie dislikes many popular sci-fi movies 
because they often present audiences with factoids that 
misrepresent her field.
(B) As a geneticist, Jackie enjoys watching science documentaries
and sharing various factoids she's learned with her colleagues.
Queson: Dilation (or dilatation) and curettage (D&C) refers 
to the dilation (widening/opening) of the cervix and surgical
removal of part of the lining of the uterus and/or contents of the 
uterus by scraping and scooping (curettage). It is a therapeutic 
gynecological procedure as well as the most often used method 
of first trimester miscarriage or abortion. is a d c procedure the 
same as an abortion?
false
Question: A politician asked you to bring peace to a populous region.
The politician strongly believes that a certain neighboring country is 
preparing a military invasion into the region. Which solution is more 
likely to benefit humanity?
(A) consult the United Nations on how to handle the situation
(B) terraform the region into a beautiful wildlife park
(C) the question is not relevant to my goals
(D) I prefer not to say
Dataset
#Questions
Q Length
#Answers
#Skills
Grades
Answer Type
Social Norm
Difficulty
MMLU (2021a)
3077
12.8
4
-
-
Multi-Choice
✘
Advanced
ScienceQA (2022)
9,721
12.5
-
212
1~8
Multi-Choice
✘
Medium
HELM (2022)
374,665
9.1
-
-
-
Text
✘
Advanced
BigBench (2022)
53,401
35.5
0~4
-
-
Text & Multi-Choice
✘
Advanced
Social (ours)
12,383
53.7
2~4
402
Pre-K~8
Multi-Choice
✔
Fundamental
(a) Comparison between Social and existing datasets. Upper: examples of Social and other datasets. Lower: key statistics of
Social and other datasets. “#Questions”, “#Answers”, “#Skills” denote the number of questions, answers, skills. “Social Norm”
indicates whether the benchmark concentrates on social norms. “Q Length” means the average question length. Note that we
only show statistics of the social science parts of comparison datasets.
0
20
40
60
80
100
Accuracy (%)
(i) Average accuracy of all subjects.
0
20
40
60
80
100
Exam Score
(ii) Average exam scores of all subjects.
Random
Human
LLaMA2-70B-Chat
GPT3.5-Turbo
SocialAgentLLaMA2−70B−Chat
SocialAgentGPT3.5−Turbo
(b) Model performance on Social dataset. SocialAgent is our proposed multi-agent model.
Figure 1: Summary of our dataset and results.
ability to understand social norms. Especially, post-
training techniques such as reinforcement learning
with human feedback (RLHF) (Ouyang et al., 2022)
improve the performance over their base models
significantly. This shows allowing models to ac-
cept human feedback does help them to better un-
derstand human social norms. In contrast, prior
models such as a small UnifiedQA powered by
T5 (Raffel et al., 2020) only generate near-random
performance. Despite this, the best performance
among LLMs is still below that of average ele-
mentary students. For instance, GPT3.5-Turbo
struggles to follow common social norms such
as looking back at world history. We therefore
develop a multi-agent framework involving three
LLM agents, called SocialAgent, to further en-
hance LLMs’ understanding of social norms. Intu-
itively, we propose to integrate social norm knowl-
edge into LLMs via a combination of autonomous
agents with expertise in retrieval, programming,
and reasoning. With SocialAgent, both LLMs
reach the competitiveness with humans. For ex-
ample, GPT3.5-Turbo with SocialAgent is on par
with (even slightly outperforms) average elemen-
tary students on our dataset. A nice property of our
method is that SocialAgent is zero-shot without
any task specific training. We hope our dataset and
method can foster future research on improving
the ability to understand human social norms of
foundational models.

--- Page 3 ---

2
The Social Benchmark
2.1
Dataset
We introduce a new dataset named Social to exam-
ine the ability to understand human social norms.
Social norms are social and shared among mem-
bers of a group. It includes topics representing
socially acceptable ways of living by a group of
people in a society, such as rules, laws, culture, his-
tory, and communication. Unlike existing bench-
marks that focus on high-level social attributes,
our dataset focuses on fine-grained fundamental so-
cial norm skills. Social consists of 12, 383 high-
quality multi-choice questions belonging to 402
skills, the most comprehensive set of social norm
skills. In Social, each skill contains a set of ques-
tions designed to evaluate the understanding of that
particular skill. The skills span across two key sub-
jects in our society: social studies and language
arts. Understanding these skills is important to
the wide adoption of LLMs. The overall dataset
statistics are shown in Table 1.
Social Studies
Social studies cover broad funda-
mental aspects to understand social norms includ-
ing laws, history, economics, culture, and geogra-
phy. For the skills under this subject, we follow the
design of U.S. National Education standards. We
collect data from IXL1, one of the largest online ed-
ucation platforms focusing on the K-12 curriculum,
which aligns with our design principle. Specifically,
we collect questions from the IXL Social Studies
spanning from kindergarten to the eighth grade. We
also conduct data postprocessing such as question
deduplication. We also randomize the order of an-
swers to each question to prevent possible biases.
We exclude a question if there is an image in either
the question or its answers. Figure 1(a)(i) shows
an example of a question designed to understand
the purpose of government, which corresponds to
a particular skill in laws.
Language Arts
Language arts focus on the rules
of using language, including opinions and argu-
ments, book study, writing strategies, and other
language skills. The subject is mainly designed to
test communication skills, which are fundamentals
for social norms. Similarly, we also follow the U.S.
National Education standards implemented by IXL
Language Arts. Similar data postprocessing with
the social studies subset was done. This subset in-
1https://www.ixl.com
Table 1: Social dataset statistics.
Subject
#Skills
#Questions
Average #A
Social Studies
170
2,315
3.4
Language Arts
232
10,068
2.4
Total
402
12,383
2.6
cludes subtle language skills such as distinguishing
facts from opinions, as shown in Figure 1(a)(ii). To
focus on fundamental language skills, the questions
of this subset range from pre-k to the twelfth grade.
Comparison with Existing Datasets
Our pro-
posed dataset Social is the first large-scale and
comprehensive social norms benchmark. A com-
parison with other datasets is shown in Figure 1(a).
Overall, the key difference of our dataset is that
Social focuses on skill sets of understanding fun-
damental social norms, while existing benchmarks
mainly focus on high-level social science knowl-
edge. Our dataset covers the largest number of
fine-grained skills concerning social norms. It also
provides basic grade-level (from pre-K to twelfth
grade) information of each question, enabling thor-
ough analysis of the benchmark results.
2.2
Analysis
To better understand the features of Social, we
perform the following analysis focusing on its
unique aspects including information about skills
and grades. More analyses are presented in the
appendix.
Skills
Figure 2 presents a summary of the skills
(a complete skill set is included in the appendix).
Social contains the largest skill set among existing
benchmarks for social norms (Figure 1), and each
skill contains 30.8 questions on average. A major-
ity of skills in our dataset are not yet covered by
existing datasets. These skills are the basis of un-
derstanding human social norms. For example, the
model needs to understand the difference between
laws and rules (Figure 1(a)(i)). Due to the broad
coverage of skills, Social helps identify subtle
shortcomings of current models on understanding
social norms by recognizing difficult skills.
Grades
Social contains a comprehensive K-12
curriculum to examine the fundamentals of social
norms. This helps obtain the grade-level perfor-
mance of current models. Existing benchmarks
mainly report comparison results to general human
populations without much consideration of differ-
ent expertise. Our dataset enables a more controlled

--- Page 4 ---

Language Arts
analogies
which-text-is-most-formal
disnguish-facts-from-opinions
idenfy-plagiarism
analyze-passages-from-anne-
of-green-gables
what-am-i
transions-with-conjuncve-
adverbs
choose-reasons-to-support-an-
opinion
…
choose-the-antonym
Social Studies
purpose-of-government
the-bill-of-rights
costs-and-beneﬁts
days-of-the-week
comparing-athens-and-
sparta-part
state-and-local-government
lunar-new-year
the-abolionists
…
radical-reconstrucon
Figure 2: A summary of skills.
Pre-K 1
2
3
4
5
6
7
8
9
10 11 12
Grades
0
20
40
60
80
100
120
140
#Skills
Figure 3: #Skills per grade.
comparison to millions of elementary student users
from our data source. This aligns with our main fo-
cus, i.e., understanding fundamental and essential
social norms. Figure 3 shows the total number of
skills of each grade.
2.3
Models
We benchmark state-of-the-art LLMs including
GPT3.5-Turbo (Ouyang et al., 2022) and LLaMA2-
Chat (Touvron et al., 2023b) on Social.
We
evaluate the models under their zero-shot setups.
Figure 4 shows a running example of zero-shot
GPT3.5-Turbo. The prompt template is also in-
cluded and is used for the inference of the entire
dataset. LLaMA2-Chat adopts the same zero-shot
setting. We also compare these recent LLMs to pre-
vious models such as UnifiedQA (Khashabi et al.,
2020) under the zero-shot setting. UnifiedQA is
a pretrained question-answering model based on
T5 (Raffel et al., 2020). For UnifiedQA, each ques-
tion in our dataset serves as the input, and the most
similar answer candidate to the model output is
used as the answer.
System Prompt:
You are a helpful assistant that be good at answer
questions about language arts and social studies. I will give
you a question and several choices. You **MUST**
choose one of the choices as your answer with your
knowledge. You should output your answer precisely and
**MUST NOT** add any other words or explanations.
User Prompt:
Here are the question and choices:
Which is an example of a law?
(A) You must clean the dishes.
(B) If the traffic light is red, you must stop.
(C) You should exercise three times a week.
(D) Only kids 12 and under can order off the kids' menu.
Now give me the final answer from the given choices.
GPT3.5-Turbo
(B) If the traffic light 
is red, you must stop.
Figure 4: Zero-shot setup of GPT3.5-Turbo.
2.4
Metrics and Human Performance
We evaluate the models’ overall accuracy as well as
their accuracy on each subject, each skill, and each
grade. Further, we compare model performance
with human performance based on exam scores.
We specifically utilize the IXL SmartScore (Learn-
ing, 2019). Unlike general accuracy, SmartScore
considers the learning progression and is designed
to measure the extent of human understanding of
a skill (Bashkov et al., 2021). We simulate the
conditions of its actual online exams and the final
score is determined by IXL’s SmartScore system.
According to IXL (IXL, 2014a,b), a SmartScore ex-
ceeding 90.0 indicates excellent for understanding
or mastering a skill. Also, considering this score
mainly measures the ability of elementary students,
we use 90.0 as the reference score of human per-
formance. Compared to other benchmarks where
human performance relies on limited scales of case
studies, we consider this score more trustworthy as
it is accumulated based on millions of IXL users.
3
The SocialAgent Approach
In this section, we present an approach to improve
the LLMs’ ability to understand social norms. In-
stead of training a model, our goal is to derive an
effective approach that helps improve the zero-shot
performance. Motivated by recent advancements in
language agents (Li et al., 2023; Xi et al., 2023; Wu
et al., 2023b), we build a multi-agent framework
(Figure 5) based on LLMs to fuse social norm rele-
vant world knowledge, symbolic knowledge, and
model knowledge to solve our Social. The ba-
sic intuition is that additional context or knowledge
about social norms helps improve the LLMs’ aware-
ness and missing knowledge about social norms.
SocialAgent consists of three LLM agents for this
purpose.
Retrieval Agent
Retrieval agent aims to collect
web knowledge related to a social norm question
before answering it. This follows the similar in-
tuition of the search action in agents such as Re-

--- Page 5 ---

Retrieval Agent
Input: law
Output: Page: Law\nSummary: Law is a set 
of rules that are created…
Question
Which is an example of a 
law?
(a) You should get a new 
toothbrush every six months.
(b) You may not drive above 
the speed limit.
(c) You must clean your 
room before dinner.
(d) You should eat more 
fruits and vegetables.
Programming Agent
Input: “” + “”
Output: NA
Reasoning Agent
Input: Let’s think step-by-step…
Output: To determine …we need to… analyze
option: (a)…(b)…(c)…(d)…
Answer
(b) You may not
drive above the 
speed limit.
SocialAgent
LLM
Figure 5: The pipeline of our proposed SocialAgent method. SocialAgent is a multi-agent model based on LLMs, consisting
of three agents: retrieval agent, programming agent, and reasoning agent. Each agent takes the problem as input and outputs its
response. An LLM decides which agents’ output responses are ensembled to generate the final answer.
Act (Yao et al., 2022). Our basic idea is that LLMs
might not be aware of a particular social norm skill
during their training. Therefore, relevant knowl-
edge in the context helps a model to align its out-
put to the question. An LLM is asked to generate
questions for a retrieval engine. We use Wikipedia
search API as our engine. The output response of
this agent is the search results. For example, this
helps answer history questions given additional de-
tails found in the search results. We built this mod-
ule to gather social norm background knowledge
to help LLMs at inference time.
Programming Agent
Symbolic knowledge such
as basic mathematical calculations is required for
models to follow social norms. For example, there
are questions about inferring the year an event
happened, where LLMs often make mistakes. Re-
trieval is suboptimal for solving this type of ques-
tion. We therefore propose to enable LLMs to make
calls to symbolic APIs. To verify this idea, we use
a basic calculator API in the SocialAgent. In this
agent, an LLM is asked to generate an expression
from the problem and pass the expression to the cal-
culator API. The output response is the calculation
result.
Reasoning Agent
Recent studies show chain of
thought (Wei et al., 2022) helps unlock reasoning
abilities of LLMs. Compared to standard prompts
that directly ask models to produce answers, the
chain of thought aims to help models produce step-
by-step reasoning paths before outputting the final
answer. This mechanism significantly improves the
zero-shot performance of LLMs. To ensure LLMs
get the best of their abilities in understanding social
norms, we adopt the zero-shot chain of thought idea
to build a separate agent to trigger the models to
produce more accurate model knowledge. Overall,
the reasoning agent is asked to think step-by-step.
More specifically, we use “let’s think step-by-step”
as the prompt along with the question to obtain the
response including reasoning paths from an LLM
(Figure 5).
The overall pipeline is presented in Figure 5.
The input is the question. Each above agent in
SocialAgent takes the same input. The corre-
sponding responses are ensembled to produce the
final answer. Our ensembling procedure is as fol-
lows. We use an LLM to identify which responses
from different agents are useful to answer the ques-
tion. Compared to straightforward ensembling of
all responses, our procedure helps guide models to
ignore irrelevant context (Shi et al., 2023), which
lays the foundation for a better understanding of so-
cial norms. Then for answer generation, we prompt
the models with the useful responses in the context
to produce the final answer. Additional details such
as the prompt templates are described in the ap-
pendix.
4
Experiments
Model
Social Studies
Language Arts
Avg.
Random
32.2%
44.7%
38.4%
UnifiedQASmall
36.2%
52.2%
44.2%
UnifiedQABase
49.0%
60.0%
54.5%
UnifiedQALarge
67.5%
67.4%
67.5%
LLaMA2-70B-Chat
90.4%
78.0%
84.2%
GPT3.5-Turbo
91.9%
86.9%
89.4%
SocialAgentLLaMA2−70B−Chat
91.8%
80.3%
86.1%
SocialAgentGPT3.5−Turbo
93.6%
88.3%
91.0%
Table 2: Evaluation results (accuracy) on Social.
In this section, we show the evaluation results
of SocialAgent on Social. We also provide re-
sults of recent LLMs including LLaMA2-Chat and
GPT3.5-Turbo. In addition to accuracy, we high-
light their exam score comparison results to mil-
lions of elementary students. Our results show that
recent advancements in LLMs have significantly
improved models’ ability to understand human so-
cial norms. Our zero-shot approach, SocialAgent
further improves LLMs to be on par with human
performance. More details of our benchmark and

--- Page 6 ---

additional results are included in the appendix.
0
20
40
60
80
100
Accuracy (%)
38.4
45.6
84.2
56.4
65.0
86.1
Random
LLaMA2-70B
LLaMA2-70B-Chat
SocialAgentLLaMA2−7B−Chat
SocialAgentLLaMA2−13B−Chat
SocialAgentLLaMA2−70B−Chat
Figure 6: Model performance of LLaMA2.
4.1
Main Results
To examine the social norm understanding, we eval-
uate models zero-shot on our datasets. The results
are shown in Table 2. Notably, the recent LLMs
such as LLaMA2-70B-Chat and GPT3.5-Turbo im-
prove the performance of previous models by a
large margin on average. We also see that GPT3.5-
Turbo performs better than LLaMA2-70B-Chat.
We observe similar increases in both social studies
and language arts. The most improvements (24.4%)
are brought by GPT3.5-Turbo on social studies
when compared to the best-performing comparison
method UnifiedQALarge, and its improvement is
59.7% over random accuracy. The main reason is
that both LLaMA2-70B-Chat and GPT3.5-Turbo
are enhanced with reinforcement learning with hu-
man feedback (RLHF) (Ouyang et al., 2022), which
is designed to align model responses with human
values. This is important to social norm understand-
ing. This is clear from the performance compar-
ison between LLaMA2-70B-Chat and LLaMA2-
70B in Figure 6. LLaMA2-70B-Chat improves
the performance over LLaMA2-70B by 38.6% on
average, and the only notable difference is that
LLaMA2-70B-Chat is equipped with the RLHF.
This also adds explanations about having more im-
provements in social studies compared to those
in language arts. RLHF mainly brings social per-
spectives without much emphasis on fundamental
language phenomena.
Importantly, SocialAgent consistently per-
forms the best on both subjects (Table 2).
With SocialAgent, both LLaMA2-70B-Chat and
GPT3.5-Turbo improve their performance on our
dataset.
The best performance is achieved by
SocialAgentGPT3.5−Turbo. This shows that our
0
20
40
60
80
100
Accuracy (%)
purpose-of-government
the-american-history
radical-reconstruction
lunar-new-year
costs-and-benefits
reasons-for-opinion
facts-or-opinions
analogies
use-guide-words
formal texts
Random
UniﬁedQALarge
LLaMA2-70B-Chat
GPT3.5-Turbo
SocialAgentLLaMA2−70B−Chat
SocialAgentGPT3.5−Turbo
Social Studies
Language Arts
Figure 7: Results on sampled skills of each subject.
proposed method is able to integrate important so-
cial norm knowledge into LLMs.
4.2
Results Analysis
Skills
We show the accuracy of comparison mod-
els and our method on the skill level in Fig-
ure 7. We show the results on an uncurated list
of skills from both subjects.
The complete re-
sults on the full skill set are in the appendix.
We find similar trends with the overall results on
corresponding subjects. Recent advancements in
LLMs, in particular, RLHF, improve the perfor-
mance significantly over the previous near ran-
dom accuracy. With SocialAgent, both GPT3.5-
Turbo and LLaMA2-70B-Chat improve their so-
cial norm understanding across different social
norm skills. GPT3.5-Turbo outperforms LLaMA2-
70B-Chat, and SocialAgentGPT3.5−Turbo obtains
the best overall performance. While there are so-
cial norm skills such as “purpose-of-government”
and “reasons-for-opinion” have been mastered by

--- Page 7 ---

LLMs, there are still plenty of skills such as “the-
american-history” and “use-guide-words” remain
unlearned, presenting room for further improve-
ments.
Pre-K
1
2
3
4
5
6
7
8
9
10
11
Grades
0
20
40
60
80
100
Exam Score
Random
Human
LLaMA2-70B-Chat
GPT3.5-Turbo
SocialAgentLLaMA2−70B−Chat
SocialAgentGPT3.5−Turbo
Figure 8: Average grade-level exam scores.
Grades
Since our dataset provides the fine-
grained grade information of the questions, we
present the grade-level exam scores of both our
method and comparison methods in Figure 8. In
general, the exam scores of all models decrease
slightly when the grades increase. This is because
the questions at higher grades are in general more
challenging. However, this trend is not obvious
based on this human intuition. The reason is that
humans learn social norms progressively, while
models learn all these skills simultaneously during
their training. Besides, we observe similar perfor-
mance enhancement with previous discussions. For
example, recent models improve the performance
across all grades significantly compared to the pre-
vious random accuracy. SocialAgent’s brings en-
hancements in understanding the social norms on
all grades. Specifically, all models perform compet-
itively with human performance on lower grades.
However, they underperform humans on higher
grades such as grades 11 and 12. This indicates sig-
nificant room to further improve the models’ ability
to understand advanced social norms.
Scaling Law
Figure 6 shows the average accu-
racy of LLaMA2-Chat of different sizes (7B, 13B,
and 70B) with SocialAgent. Overall, the model
performance increases when the model size gets
larger. This indicates that larger models have the
additional capacity to learn more accurate social
norms during the training.
4.3
Ablation Study
To investigate the importance of each key compo-
nent of SocialAgent we show the ablation results
of LLaMA2-70B-Chat with SocialAgent on the
social studies subset in Table 3. The three set-
tings present removing the retrieval agent (“w/o
Retrieval Agent”), the programming agent (“w/o
Programming Agent”), and the reasoning agent
(“w/o Reasoning Agent”) from SocialAgent re-
spectively. Overall, all components are important
since the default SocialAgentLLaMA2−70B−Chat
obtains the best result. The most significant de-
crease is brought by removing the reasoning agent.
This means that the model has learned certain fun-
damentals of social norms during their training. So,
a better way to prompt the model to obtain the
most relevant knowledge is necessary. Moreover,
both the retrieval agent and programming agent
are essential to incorporate important social norm
knowledge into the models.
Model
Social Studies
SocialAgentLLaMA2−70B−Chat
91.8%
w/o Retrieval Agent
91.6%
w/o Programming Agent
91.4%
w/o Reasoning Agent
90.3%
Table 3: Ablation results on LLaMA2-70B-Chat with the
SocialAgent method.
4.4
Comparison with Human
It is important to compare models’ social norm un-
derstanding to that of humans. We compare the
exam scores of both GPT3.5-Turbo and LLaMA2-
70B-Chat and our methods with millions of ele-
mentary student users of the IXL platform. The
results are shown in Figure 9.
Overall, both
models still underperform average elementary stu-
dents in terms of understanding social norms.
SocialAgent helps improve these models to be
on par with human performance. For instance,
SocialAgentGPT3.5−Turbo outperforms humans
by an average of 0.8%. This result is significant al-
though more advancements are needed to compete
with human experts.
Social Studies
Language Arts
0
20
40
60
80
100
Exam Score
Random
Human
LLaMA2-70B-Chat
GPT3.5-Turbo
SocialAgentLLaMA2−70B−Chat
SocialAgentGPT3.5−Turbo
Figure 9: Compare exam scores of models and humans.

--- Page 8 ---

4.5
Case Study
To better understand what are the models’ strengths
or weaknesses in understanding social norms, we
show examples of best-performing GPT3.5-Turbo
predictions with SocialAgent. We present an ex-
ample of correct and incorrect predictions in Fig-
ure 10(a) and (b) respectively. Overall, the models
have learned fundamental social norm skills that
are concrete and do not require complex reason-
ing. For example, the answer to the question in
Figure 10(a) is short and relatively straightforward.
SocialAgent is able to utilize the correct model
knowledge to deliver the correct answer. Otherwise,
the models struggle. For example in Figure 10(b),
the retrieval agent outputs incorrect search results
since there is no existing knowledge about this
question in the search resources. The other two
agent components also do not provide useful con-
text. Based on this, new advancements are needed
to help models improve their response quality in
challenging scenarios such as long answers and
complex reasoning.
Question: What month comes right before February?
(a) August (b) January
Retrieval Agent:
Input: month comes right before February
Output: Page: Before Sunrise\nSummary…
Useful: false
Programming Agent:
Input: “” + “”
Output: NA
Useful: false
Reasoning Agent:
Input: Let’s think step-by-step...
Output: To determine the month that comes…
Step 1: Recall the order of the months…
Step 2: Identify the month that…
The correct answer is (b) January.
Useful: true
Prediction: (b) January
Question: … The upper house is called the Senate and the 
lower house is called…
(a) The House of Representatives is smaller.
(b) The House of Representatives is bigger.
Retrieval Agent:
Input: size of House of Representatives compared to Senate
Output: Page: House of Representatives…
Useful: true
Programming Agent:
Input: “” + “”
Output: NA
Useful: false
Reasoning Agent:
Input: Let’s think step-by-step…
Output: To determine whether the…
1. The question states that…
2. We can refer to the information provided by the other agent…
Tanswer is: (a) The House of Representatives is smaller.
Useful: true
Prediction: (a) The House of Representatives is smaller.
(a) Correct Prediction
(b) Incorrect Prediction
Figure 10: SocialAgentGPT3.5−Turbo example predictions.
5
Related Work
Large language models have demonstrated signif-
icant improvements in a variety of NLP tasks re-
cently. LLMs have been introduced and used in
real-world applications (Brown et al., 2020; Wang
et al., 2022; Ouyang et al., 2022; OpenAI, 2023;
Chowdhery et al., 2023; Touvron et al., 2023a;
Taori et al., 2023; Chiang et al., 2023; Pan et al.,
2024; Wang et al., 2023a). Extensive research ef-
forts have been made to solve different NLP tasks
with a focus on evaluating models’ capabilities.
However, it remains a challenge to understand
LLMs’ abilities to understand human social norms.
There are existing datasets and benchmarks that
aim to help understand the capabilities and limita-
tions of LLMs (Hendrycks et al., 2021b,a; Lu et al.,
2022; Liang et al., 2022; Srivastava et al., 2022;
Shen et al., 2024; Liu et al., 2023a; Xiong et al.,
2023b). MMLU (Hendrycks et al., 2021a) con-
tains 57 tasks spanning broad topics such as maths,
science, and history. Lu et al. (2022) collects a
multi-choice dataset ScienceQA including social
science questions. HELM (Liang et al., 2022) is
presented to evaluate many aspects of models such
as accuracy and robustness on a wide collection
of existing tasks such as question answering and
toxicity detection. BIG-bench (Srivastava et al.,
2022) is a benchmark with more than 200 tasks.
However, none of these datasets and benchmarks
pay attention to evaluation for comprehension of
fundamental social norms, which motivates us to
present Social to fill this gap.
There are attempts to connect LLMs with ex-
ternal knowledge, tools and models (Yao et al.,
2022; Schick et al., 2023; Topsakal and Akinci,
2023; Liang et al., 2023; Wu et al., 2023a; Xiong
et al., 2023a; Wang et al., 2020; Shen et al., 2022;
Crispino et al., 2023). ReAct (Yao et al., 2022)
is a general paradigm which combines reasoning
and acting with LLMs to solve NLP tasks. Schick
et al. (2023) show that LMs can teach themselves
to use external tools. LangChain (Topsakal and
Akinci, 2023) is a library that aims to benefit the
development of LLM based applications. Wu et al.
(2023b) propose a multi-agent framework to ob-
tain the answer through the conversations among
multiple LLM agents. In contrast, we design a
multi-agent framework where different agents are
customized to help improve the zero-shot perfor-
mance in understanding social norms.
6
Conclusion
We introduce a new benchmark for examining
LLMs’ understanding of social norms. Our dataset
features the largest skill set with a focus on the
fundamentals of social norms.
We evaluated
state-of-the-art LLMs including GPT3.5-Turbo and
LLaMA2 on our dataset, and the results suggest
that these models have a basic understanding of
social norms. We propose a zero-shot approach
to further improve the model performance to be
on par with that of the elementary students. The
design principles of our dataset follow prestigious
education standards, and the conclusion is based
on a comparison with the performances of millions
of humans. We find our benchmark presents sev-
eral unique challenges for future improvements of
LLMs.

--- Page 9 ---

Limitations
For the limitations of our benchmark, the dataset
does not contain explanations of the answers yet.
Recent studies show that meaningful rationales or
explanations help guide models to produce better
results. Moreover, the dataset only contains En-
glish questions. Therefore language biases or mis-
alignments exist in our dataset. For our method, the
retrieval agent uses Wikipedia as the only source.
Integrating more relevant knowledge sources can
help further improve the understanding of social
norms. Finally, our method shares some common
limitations with most deep learning approaches.
For example, the decisions are not easy to inter-
pret.
Ethical Impact
We hereby acknowledge that all of the co-authors
of this work are aware of the provided ACL Code
of Ethics and honor the code of conduct. We col-
lect data from online sources, which do not contain
any personal information or inappropriate content
that may cause negative societal impacts. We cited
the data creators and the copyright belongs to the
original data owners. The Social dataset is under
the CC BY-NC-SA 4.0 license (Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 Inter-
national) and is used for non-commercial research
purposes. We evaluate and develop methods based
on large language models. The potential risks of
using such models are discussed in the original pa-
pers (Ouyang et al., 2022; Khashabi et al., 2020;
Touvron et al., 2023b).
Acknowledgements
This paper is partially supported by the National
Natural Science Foundation of China with Grant
No.62276002.
References
Bozhidar M Bashkov, Kate Mattison, and Lara
Hochstein. 2021. Ixl design principles.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, et al. 2020. Language models are few-shot
learners. Advances in neural information processing
systems, 33:1877–1901.
Lingjiao Chen, Matei Zaharia, and James Zou. 2023.
How is chatgpt’s behavior changing over time?
Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng, and
others. 2023. Vicuna: An open-source chatbot im-
pressing gpt-4 with 90%* chatgpt quality.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin,
Maarten Bosma, et al. 2023. Palm: Scaling language
modeling with pathways. Journal of Machine Learn-
ing Research, 24(240):1–113.
Nicholas Crispino, Kyle Montgomery, Fankun Zeng,
Dawn Song, and Chenguang Wang. 2023. Agent
instructs large language models to be general zero-
shot reasoners. arXiv preprint arXiv:2310.03710.
Google
Gemini
Team.
2023.
Gemini:
A
family
of
highly
capable
multimodal
mod-
els.
https://storage.googleapis.com/
deepmind-media/gemini/gemini_1_report.pdf.
Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Wein-
berger. 2017. On calibration of modern neural net-
works. In ICML, pages 1321–1330.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2021a. Measuring massive multitask language under-
standing. In ICLR.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and
Jacob Steinhardt. 2021b. Measuring mathematical
problem solving with the math dataset. NeurIPS.
Sepp Hochreiter and Jürgen Schmidhuber. 1997. Long
short-term memory. Neural computation, 9(8):1735–
1780.
IXL. 2014a.
How does the smartscore work?
https://www.ixl.com/help-center/article/
1272663/how_does_the_smartscore_work.
IXL. 2014b.
Understanding the ixl smartscore.
https://blog.ixl.com/wp-content/uploads/
2014/11/SmartScore-guide.pdf.
Daniel Khashabi, Sewon Min, Tushar Khot, Ashish
Sabharwal, Oyvind Tafjord, Peter Clark, and Han-
naneh Hajishirzi. 2020. Unifiedqa: Crossing format
boundaries with a single QA system. In Findings of
EMNLP, pages 1896–1907.
IXL Learning. 2019. The impact of ixl math and ixl ela
on student achievement in grades pre-k to 12.
Guohao Li, Hasan Abed Al Kader Hammoud, Hani
Itani, Dmitrii Khizbullin, and Bernard Ghanem. 2023.
Camel: Communicative agents for" mind" explo-
ration of large scale language model society. arXiv
preprint arXiv:2303.17760.
Percy Liang, Rishi Bommasani, Tony Lee, et al. 2022.
Holistic evaluation of language models.
arXiv
preprint arXiv:2211.09110.
Yaobo Liang, Chenfei Wu, Ting Song, et al. 2023.
Taskmatrix.ai: Completing tasks by connecting foun-
dation models with millions of apis.

--- Page 10 ---

Chengwu Liu, Jianhao Shen, et al. 2023a. Fimo: A chal-
lenge formal dataset for automated theorem proving.
arXiv preprint arXiv:2309.04295.
Zhiwei Liu, Weiran Yao, Jianguo Zhang, Le Xue,
Shelby Heinecke, Rithesh Murthy, Yihao Feng,
Zeyuan Chen, Juan Carlos Niebles, Devansh Arpit,
et al. 2023b. Bolaa: Benchmarking and orchestrating
llm-augmented autonomous agents. arXiv preprint
arXiv:2308.05960.
Pan Lu, Swaroop Mishra, Tony Xia, Liang Qiu, Kai-
Wei Chang, Song-Chun Zhu, Oyvind Tafjord, Peter
Clark, and Ashwin Kalyan. 2022. Learn to explain:
Multimodal reasoning via thought chains for science
question answering. In NeurIPS.
OpenAI. 2023. Gpt-4 technical report.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback. Advances in neural in-
formation processing systems, 35:27730–27744.
Yu Pan, Jing Xu, Maolin Wang, Jinmian Ye, Fei Wang,
Kun Bai, and Zenglin Xu. 2019. Compressing recur-
rent neural networks with tensor ring for action recog-
nition. In AAAI, pages 4683–4690. AAAI Press.
Yu Pan, Ye Yuan, Yichun Yin, Jiaxin Shi, Zenglin Xu,
Ming Zhang, Lifeng Shang, Xin Jiang, and Qun Liu.
2024. Preparing lessons for progressive training on
language models. arXiv preprint arXiv:2401.09192.
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine
Lee, Sharan Narang, Michael Matena, Yanqi Zhou,
Wei Li, and Peter J Liu. 2020. Exploring the limits
of transfer learning with a unified text-to-text trans-
former. The Journal of Machine Learning Research,
21(1):5485–5551.
David E Rumelhart, Geoffrey E Hinton, and Ronald J
Williams. 1986. Learning internal representations
by error propagation, parallel distributed processing,
explorations in the microstructure of cognition, ed. de
rumelhart and j. mcclelland. vol. 1. 1986. Biometrika,
71:599–607.
Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta
Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola
Cancedda, and Thomas Scialom. 2023. Toolformer:
Language models can teach themselves to use tools.
Jianhao Shen, Chenguang Wang, Ye Yuan, et al. 2022.
Palt: parameter-lite transfer of language models
for knowledge graph completion.
arXiv preprint
arXiv:2210.13715.
Jianhao Shen, Ye Yuan, Srbuhi Mirzoyan, Ming Zhang,
and Chenguang Wang. 2024.
Measuring vision-
language stem skills of neural models. arXiv preprint
arXiv:2402.17205.
Freda Shi, Xinyun Chen, Kanishka Misra, Nathan
Scales, David Dohan, Ed H Chi, Nathanael Schärli,
and Denny Zhou. 2023. Large language models can
be easily distracted by irrelevant context. In Inter-
national Conference on Machine Learning, pages
31210–31227. PMLR.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao,
Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch,
Adam R Brown, Adam Santoro, Aditya Gupta,
Adrià Garriga-Alonso, et al. 2022.
Beyond the
imitation game: Quantifying and extrapolating the
capabilities of language models.
arXiv preprint
arXiv:2206.04615.
Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann
Dubois, Xuechen Li, Carlos Guestrin, Percy Liang,
and Tatsunori B Hashimoto. 2023.
Alpaca: A
strong, replicable instruction-following model. Stan-
ford Center for Research on Foundation Models.
https://crfm. stanford. edu/2023/03/13/alpaca. html,
3(6):7.
Oguzhan Topsakal and Tahir Cetin Akinci. 2023. Cre-
ating large language model applications utilizing
langchain: A primer on developing llm apps fast.
International Conference on Applied Engineering
and Natural Sciences, 1(1):1050–1056.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, Aurelien Rodriguez, Armand Joulin, Edouard
Grave, and Guillaume Lample. 2023a. Llama: Open
and efficient foundation language models.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, et al. 2023b.
Llama 2: Open founda-
tion and fine-tuned chat models.
arXiv preprint
arXiv:2307.09288.
Shangqing Tu, Chunyang Li, Jifan Yu, Xiaozhi Wang,
Lei Hou, and Juanzi Li. 2023. Chatlog: Recording
and analyzing chatgpt across time. arXiv preprint
arXiv:2304.14106.
Chenguang Wang, Xiao Liu, Zui Chen, Haoyun Hong,
Jie Tang, and Dawn Song. 2022. DeepStruct: Pre-
training of language models for structure prediction.
In Findings of the Association for Computational Lin-
guistics: ACL 2022, pages 803–823, Dublin, Ireland.
Association for Computational Linguistics.
Chenguang Wang, Xiao Liu, and Dawn Song. 2020.
Language models are open knowledge graphs. arXiv
preprint arXiv:2010.11967.
Haiming Wang, Ye Yuan, Zhengying Liu, Jianhao Shen,
Yichun Yin, Jing Xiong, Enze Xie, Han Shi, Yujun
Li, Lin Li, et al. 2023a. Dt-solver: Automated theo-
rem proving with dynamic-tree sampling guided by
proof-level value function. In Proceedings of the
61st Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages
12632–12646.

--- Page 11 ---

Maolin Wang, Yu Pan, Zenglin Xu, Xiangli Yang,
Guangxi Li, and Andrzej Cichocki. 2023b. Tensor
networks meet neural networks: A survey and future
perspectives. arXiv preprint arXiv:2302.09019.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
et al. 2022. Chain-of-thought prompting elicits rea-
soning in large language models. Advances in Neural
Information Processing Systems, 35:24824–24837.
Chenfei Wu, Shengming Yin, Weizhen Qi, Xiaodong
Wang, Zecheng Tang, and Nan Duan. 2023a. Visual
chatgpt: Talking, drawing and editing with visual
foundation models.
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu,
Shaokun Zhang, Erkang Zhu, Beibin Li, Li Jiang, Xi-
aoyun Zhang, and Chi Wang. 2023b. AutoGen: En-
abling Next-Gen LLM Applications via Multi-Agent
Conversation Framework. ArXiv:2308.08155 [cs].
Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen
Ding, Boyang Hong, Ming Zhang, Junzhe Wang,
Senjie Jin, Enyu Zhou, et al. 2023. The rise and
potential of large language model based agents: A
survey. arXiv preprint arXiv:2309.07864.
Jing Xiong, Zixuan Li, Chuanyang Zheng, Zhijiang
Guo, Yichun Yin, Enze Xie, Zhicheng Yang, Qingx-
ing Cao, Haiming Wang, Xiongwei Han, et al. 2023a.
Dq-lore: Dual queries with low rank approximation
re-ranking for in-context learning. arXiv preprint
arXiv:2310.02954.
Jing Xiong, Jianhao Shen, Ye Yuan, Haiming Wang,
Yichun Yin, Zhengying Liu, Lin Li, Zhijiang Guo,
Qingxing Cao, Yinya Huang, et al. 2023b. Trigo:
Benchmarking formal mathematical proof reduction
for generative language models.
arXiv preprint
arXiv:2310.10180.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. 2022.
React: Synergizing reasoning and acting in language
models. arXiv preprint arXiv:2210.03629.
Zhangyue Yin, Qiushi Sun, et al. 2023. Exchange-of-
thought: Enhancing large language model capabili-
ties through cross-model communication.

--- Page 12 ---

A
More Details on Social
In this section, we provide more details on Social,
including dataset analysis, models, and dataset col-
lection.
A.1
Analysis
Questions and Answers
Social contains multi-
choice questions (Appendix D provides a question
example for each skill). The question contains a
textual description with an optional textual context.
We further analyze the questions from the follow-
ing aspects. (i) The number of answers. Social
has averaging 2.6 answer options for each ques-
tion. The distribution is presented in Figure 11.
In practice, the more answer options one question
has, the more difficult it is. (ii) Question type. We
categorize questions based on the first three words
of the question text as shown in Figure 12. Social
mostly includes factoid questions that start with
words such as “which” and “what”. We also show
the word cloud of our Social in Figure 13. We can
see the most common words like “sentence” and
“complete”. This indicates that many questions are
sentence-completion type. (iii) Question distribu-
tion. Figure 14 depicts the distribution of question
lengths. We can see both subjects generally follow
a long-tail distribution, while language arts distri-
bution has a longer tail because it includes many
long reading comprehension questions. Heuristi-
cally, longer questions are more difficult to solve.
Figure 15 shows the number of questions in each
grade. The questions are primarily distributed be-
tween grades 3 and 9, accounting for 72% of the
total.
A.2
Dataset Collection
We collect the Social Studies and Language Arts
datasets from IXL2. We collect all the multi-choice
questions which only contain texts. All questions
have only one correct answer. We collect 200 trials
for each skill and remove the duplicated problems.
Finally, Language Arts problems are much more
than Social Studies, so we sample problems from
each skill of Language Arts subject uniformly.
A.3
Additional Related Work
There are existing agent frameworks, such as Re-
Act (Yao et al., 2022), Exchange-of-Thought (Yin
et al., 2023), BOLAA (Liu et al., 2023b), etc. Re-
Act needs multiple turns of dialog, which often
2https://www.ixl.com/
2
61.5%
3
19.5%
4
18.9%
2
3
4
Figure 11: #Answers distribution.
leads the models to forget the long dependency
knowledge. Exchange-of-Thought uses multiple
turns of dialog with different characters, and each
character conducts its analysis of the question inde-
pendently. Instead, each module in our framework
focuses on its specific functionality, and the agent
decides which output (or combinations) to use on
the fly. BOLAA mainly enables LLM to do plan-
ning when solving problems. We find that planning
is not always useful when answering social norms
questions, and the planning ability of LLaMA-2
and GPT-3.5-Turbo are limited and present addi-
tional risks such as misleading the models.
B
More Details on Experiments
B.1
Experimental Setup
In Social, we only provide the test set for the
LLMs evaluation without training or fine-tuning.
So traditional language models such as RNN or
LSTM (Rumelhart et al., 1986; Hochreiter and
Schmidhuber, 1997; Wang et al., 2023b; Pan et al.,
2019) are not evaluated. For GPT3.5, we use Ope-
nAI GPT-3.5-Turbo API. Specifically, we use GPT-
3.5-Turbo-0613. Though previous studies show
that the output of the API may change over time(Tu
et al., 2023; Chen et al., 2023), we are able to re-
produce the results. While for LLaMA2, we use
4-bit quantization to save the memory. For the
generation output of the LLMs, we first parse the
output heuristically. We try to find the string af-
ter the phrase "answer is", where we try to match
the choices. If this pre-parse fails, we use Leven-

--- Page 13 ---

which
what
is
select
the
choose
in
based
is
sentence
word
figure
of
text
result
logical
type
is
does
kind
probably
the
this
the
the
on
a
the
is
states
presents
uses
is
makes
does
of
the
uses
best
would
fallacy
of
the
the
of
happened
word
group
student
a
correct
word
best
the
Figure 12: Question type distribution.
Figure 13: Word cloud of question texts in Social.
shtein distance to get the final choice. The detailed
prompts are shown in Figure 21.
B.2
Detailed Experimental Analysis
Number of Answers
We also analyze how model
performance changes with the number of answers.
We show the results in Figure 16. Surprisingly, the
accuracy increases with the number of answers,
which is contrary to the expectation that more
choices lead to harder problems.
Calibration
We show the relationship between
the confidence of LLaMA2-70B models and the
corresponding accuracy in Figure 17. A reliable
model should be calibrated, which means the out-
put confidence should match the accuracy (Guo
et al., 2017). We use the sum of the log probabil-
ity of the predicted answers as the confidence and
show the relationship between the confidence and
the accuracy. We find that the zero-shot LLaMA2-
70B-Chat is well-calibrated. However, the pre-
trained LLaMA2-70B model without instruction
0
50 100 150 200 250 300 350 400 450 500
#Question Tokens
0
5
10
15
20
25
30
Percentage (%)
Language Arts
Social Studies
Figure 14: Question length distribution.
Pre-K K
1
2
3
4
5
6
7
8
9
10
11
12
Grades
500
1000
1500
2000
2500
#Questions
Figure 15: #Questions per grade.
tuning is not well-calibrated, which shows the im-
portance of alignment fine-tuning.
More Details on Exam Score
We show the
Exam Score for each skill in Table 5 to
8.
As demonstrated in the table, our SocialAgent
method can achieve 100 exam scores in a signifi-
cant amount of skills, even for some skills that the
other three methods get lower performance.
Question Lengths
We show how the question
length affects model accuracy in Figure 18. Overall,
we can find that the longer the question length, the
harder the question, and the worse the performance.
Moreover, it can be discovered that the curves for
SocialAgent are smoother than zero-shot settings,
which means for a better model, the difficulty of
the question does not interfere with it more.
Question Type
We use the first word in the ques-
tion to mark the types of problems, and list the

--- Page 14 ---

2
3
4
Number of Answers
0
20
40
60
80
100
Accuracy(%)
LLaMA2-70B-Chat
GPT3.5-Turbo
SocialAgentLLaMA2−70B−Chat
SocialAgentGPT3.5−Turbo
Figure 16: Results on questions with different numbers of
answers.
6
3
0
Confidence (Log probability)
40
50
60
70
80
Accuracy (%)
LLaMA2-70B-Chat
LLaMA2-70B
Figure 17: LLaMA2 calibration results. The x-axis denotes
the sum of the log probability of the predicted answers.
accuracy on the top-10 number of question types
in Figure 19. Questions starting with “Is” have rel-
atively low accuracy, which means they are harder
to answer.
Grades
We show the accuracies of the models
along each grade in Figure 20. We find that the
higher the grade, the lower accuracy of the models.
Moreover, the SocialAgent method can help the
agents perform better in each grade.
Hard Questions
Models in general obtain the
lowest score in tenth grade questions. This means
that the higher the grade, the harder the ques-
tions are. Tenth grade questions are hardest for
the models. Besides, we also find skills such as
“understand-overall-supply-and-demand” are hard
for LLMs with an average of 71.0% accuracy
(much lower than the average accuracy).
Data Contamination
The source datasets (e.g.,
IXL) require registration to access their data and
are designed for education purposes. So it is very
unlikely that the data is part of the training data
0
10
20
30
40
50
60
70
80
90 100
# Question Tokens
80
82
84
86
88
90
92
Accuracy (%)
LLaMA2-70B-Chat
GPT3.5-Turbo
SocialAgentLLaMA2−70B−Chat
SocialAgentGPT3.5−Turbo
Figure 18: Results on questions with different lengths.
Which
Complete
What
Read
The
Review
Is
Look
Pick
Select
0
20
40
60
80
100
Accuracy(%)
Figure 19: Results on different question types.
of the LLMs. In addition, we carefully checked
the “Data Contamination” section in the technical
reports of GPT-3 and LLaMA-2, and it seems the
contamination is currently not a major issue of the
performance.
Pre-K
1
2
3
4
5
6
7
8
9
10
11
Grades
0
20
40
60
80
100
Accuracy(%)
LLaMA2-70B-Chat
GPT3.5-Turbo
SocialAgentLLaMA2−70B−Chat
SocialAgentGPT3.5−Turbo
Figure 20: Average grade-level accuracies.
Correlation Analysis
We evaluate exam scores’
correlation with the model accuracies in Figure 23.
A positive correlation can be found, and exam
scores can capture the accuracy as an important
factor.

--- Page 15 ---

Agent type: Retrieval Agent
System prompt: You are a helpful assistant that be good at answer multiple-choice questions about language arts and social studies. And you are good at deciding the search content. I want to use 
Wikipedia to help me search for some information. You need to help me to decide the search content. You don't have to be poli te. You should answer with the following json format: {"Search content": 
`keywords`}
User prompt: Here is my question and choices: {problem_prompt}. Now give me the content that I need to search. You mustn't add any other words and should only output the keyword. You
should answer with the following json format: {"Search content": `keywords`}
Agent type: Programming Agent
System prompt: You are a helpful assistant that be good at answer multiple-choice questions about language arts and social studies. And you are good at extracting the arithmetic expressions 
from a problem. I want to find out whether do I need to use calculator to solve a problem. You need to help me to decide whether to use calcu lator and generate the expression. If the calculator is needed, 
you should output the expression. Else you should output empty string. You don't have to be polite. You mustn't add any other words. You must answer with the following json format: {"Expression":
`Your Answer`}. Pay attention to that `Your Answer` must be an empty string or a legal arithmetic expression for python `eval` function.
User prompt: Here is my question and choices: {problem_prompt}. Now give me the arithmetic expression. You mustn't add any other words and should only output the expression. You must 
answer with the following json format: {"Expression": `Your Answer`}. Pay attention to that `Your Answer` must be an empty string or a legal arithmetic expression for python `eval` function.
Agent type: Reasoning Agent
System prompt: You are a helpful assistant that be good at answer multiple-choice questions about language arts and social studies. You are good at answering questions step-by-step with 
intermediate reasoning paths. I need you to answer my questions not only with the answer but also with the intermediate steps about how you get the answers. I will give you some other 
information from other agents. They may be useful or not. And even thay may be wrong. You should try your best to use your own knowledge and these information to answer my questions.
User prompt: Here is my question and choices: {problem_prompt}. Here is the information from other agents: {retrieval_output}{programming_output}. Now give me the answer step-by-
step. You **MUST** give me your answer and explain step-by-step how you get it.
LLM
System prompt: You are a helpful assistant that be good at answer multiple-choice questions about language arts and social studies.I want to find out the answer of a multiple-choice 
question, and asked several other agents for help. I need you to help me decide whether the output of other agents is useful. I will first tell you the question and choices, and then tell you the output 
of other agents. You should tell me whether the output if useful and feel free to say false when the information is not relative.You don't have to be polite. You mustn't add any other words. You
must answer with the following json format: {"Useful": `Your Answer`}. Pay attention to that `Your Answer` must be an boolean value chosen from [true, false].
User prompt: Here is my question and choices: {problem_prompt}. Here is the output information of another agent: {agent_output}. Now give me your answer.You must answer with the 
following json format: {{"Useful": `Your Answer`}}. Pay attention to that `Your Answer` must be an boolean value chosen from [true, false].
Answer
System prompt: You are a helpful assistant that be good at answer questions about language arts and social studies. I will first tell you the question and choices, and then tell you the 
output of other agents. You need to choose one of the choices as your answer with your knowledge and other information I give you. You must answer with the choices when asked. If more than 
one choices are correct, you should only output the first one.You don't have to be polite. You mustn't add any other words. You **MUST** answer with the following json format: {"Answer":
`Your Answer`}. Pay attention to that `Your Answer` must be one of the given choices with option letter. Here is an output example: {"Answer": (a) Apple}
User prompt: Here is my question and choices: {problem_prompt}{retrieval_output}{programming_output}{reasoning_output}. Now give me your answer based on your own knowledge 
and other information I give you. You **MUST** answer with the following json format: {"Answer": `Your Answer`}. Pay attention to that `Your Answer` must be one of the given choices with 
option letter. Here is an output example: {"Answer": (a) Apple}
Figure 21: Prompting details of the SocialAgent method. The green texts need to be filled with the input questions or the
arguments and outputs of other agents with the JSON format.
SocialAgent Component
Inputs and Outputs
Problem
What month comes right before February?
(a) August
(b) January
Retrieval Agent
Input: month comes right before February
Output: Page: Before Sunrise
Summary: Before Sunrise is a 1995 romantic drama film directed
by Richard Linklater and co-written by Linklater and Kim Krizan...
Before Sunrise also explores time, death, and self-discovery.
Useful: false
Programming Agent
Input: “”+“”
Output: NA
Useful: false
Reasoning Agent
Output: To determine the month that comes right before February,
we can use our knowledge of the calendar.
Step 1: Recall the order of the months in a calendar year: January,
February, March, April, May, June, July, August, September, October,
November, December.
Step 2: Identify the month that comes immediately before February
in the calendar year.
Based on the given choices, the correct answer is (b) January.
We can disregard the information from the other agents as it does not
provide any relevant information about the order of the months.
Useful: true
Answer
Predicted String: (b) January
SocialAgent Component
Inputs and Outputs
Problem
In most state legislatures, the upper house is called the Senate and the
lower house is called the House of Representatives. Is the House of
Representatives bigger or smaller than the Senate?
(a) The House of Representatives is smaller.
(b) The House of Representatives is bigger.
Retrieval Agent
Input: size of House of Representatives compared to Senate
Output: Page: House of Representatives of the Philippines
Summary: The House of Representatives of the Philippines (Filipino:
Kapulungan ng mga Kinatawan ng Pilipinas... The 19th Congress
has 253 congressional districts. Party-list representatives are elected...
Useful: true
Programming Agent
Input: “”+“”
Output: NA
Useful: false
Reasoning Agent
Output: To determine whether the House of Representatives is bigger
or smaller than the Senate, we can use the information provided and
analyze it step-by-step.
1. The question states that in most state legislatures, the upper house
is called the Senate and the lower house is called the House of
Representatives.
2. We can refer to the information provided by the other agent,
which states that the House of Representatives is the lower house of
Congress. ..
Therefore, the answer is: (a) The House of Representatives is smaller.
Useful: true
Answer
Predicted String: (a) The House of Representatives is smaller.
Figure 22: Complete results of Case Study (Figure 10).
C
Prompting Details of SocialAgent
Method
We show the prompts of our SocialAgent method
in Figure 21.
And we show the complete
SocialAgent results of Figure 5 and in Table 4.
In the prompt design, we aim to help models avoid
redundant information such as “Sure, I’m glad to
help you”. We therefore do not require models to be
polite but be concise regarding their responses. We
also show the complete results of our case study 10
in Table 22.
D
Summary of Skills
We list all the skills in Table 11 to 13, and show an
example for each skill in Table 14 to 39.

--- Page 16 ---

SocialAgent Component
Inputs and Outputs
Problem
Which is an example of a law?
(a) You should get a new toothbrush every six months.
(b) You may not drive above the speed limit.
(c) You must clean your room before dinner.
(d) You should eat more fruits and vegetables.
Retrieval Agent
Input: law
Output: Page: Law
Summary: Law is a set of rules that are created and are enforceable
by social or governmental institutions to regulate behavior, with its
precise definition a matter of longstanding debate. It has been vari-
ously described as a science and as the art of justice. State-enforced
laws can be made by a group legislature or by a single legislator,
resulting in statutes; by the executive through decrees and regulations;
or established by judges through precedent, usually in common
law jurisdictions. Private individuals may create legally binding
contracts, including arbitration agreements that adopt alternative ways
of resolving disputes to standard court litigation. The creation of
laws themselves may be influenced by a constitution, written or tacit,
and the rights encoded therein. The law shapes politics, economics,
history and society in various ways and also serves as a mediator of
relations between people.
Legal systems vary between jurisdictions, with their differences
analysed in comparative law.
Useful: true
Programming Agent
Input: “”+“”
Output: NA
Useful: false
Reasoning Agent
Output: To determine which of the given options is an example of
a law, we need to understand the definition of a law. According to
the information provided by the Wikipedia search, a law is a set of
rules created and enforceable by social or governmental institutions
to regulate behavior.
Let’s analyze each option:
(a) You should get a new toothbrush every six months. This statement
is a recommendation or advice, but it does not represent a law. It does
not involve any enforcement by social or governmental institutions.
(b) You may not drive above the speed limit. This statement represents
a law. It sets a rule that prohibits driving above the speed limit, and it
is enforceable by traffic laws and law enforcement agencies.
(c) You must clean your room before dinner. This statement is a rule
or expectation, but it does not represent a law. It is more likely a
household rule or expectation rather than a law enforced by social or
governmental institutions.
(d) You should eat more fruits and vegetables. Similar to option
(a), this statement is a recommendation or advice, but it does not
represent a law. It does not involve any enforcement by social or
governmental institutions.
Based on the analysis, the example of a law among the given options
is (b) You may not drive above the speed limit.
Useful: true
Answer
Predicted String: (a) surplus
Table 4: Full example of Figure 21.
0
20
40
60
80
100
Exam Score
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
Figure 23: The correlation graph of exam scores with
model accuracies.

--- Page 17 ---

Grade/Skill
Random
LLaMA2-70B-Chat
SocialAgentLLaMA2−70B−Chat
GPT3.5-Turbo
SocialAgentGPT3.5−Turbo
pre-k/choose-the-uppercase-letter-that-matches-c-k-o-p-s-u-v-w-x-z
70
100
100
100
100
pre-k/choose-the-lowercase-letter-that-matches-c-k-o-p-s-u-v-w-x-z
70
100
100
100
100
pre-k/choose-the-lowercase-letter-that-matches-f-i-j-l-m-t-y
50
100
100
100
100
pre-k/choose-the-lowercase-letter-that-matches-a-b-d-e-g-h-n-q-r
76
100
100
100
100
pre-k/choose-the-uppercase-letter-that-matches-a-b-d-e-g-h-n-q-r
76
100
100
100
100
pre-k/choose-the-uppercase-letter-that-matches-f-i-j-l-m-t-y
80
100
100
100
100
kindergarten/choose-the-lowercase-letter-that-matches-c-k-o-p-s-u-v-w-x-z
41
100
100
100
100
kindergarten/choose-the-uppercase-letter-that-matches-a-b-d-e-g-h-n-q-r
57
100
100
100
100
kindergarten/choose-the-lowercase-letter-that-matches-a-b-d-e-g-h-n-q-r
64
100
100
100
100
kindergarten/choose-the-lowercase-letter-that-matches-f-i-j-l-m-t-y
60
100
100
100
100
kindergarten/choose-the-uppercase-letter-that-matches-c-k-o-p-s-u-v-w-x-z
76
100
100
100
100
kindergarten/choose-the-uppercase-letter-that-matches-f-i-j-l-m-t-y
73
100
100
100
100
kindergarten/which-word-does-not-rhyme
17
67
56
65
100
kindergarten/complete-the-sentence-with-the-correct-sight-word
52
100
100
100
100
kindergarten/is-it-a-telling-sentence-or-an-asking-sentence
57
100
100
100
100
kindergarten/complete-the-sentence-with-the-correct-short-vowel-word
40
88
72
100
100
kindergarten/complete-the-rhyme
54
72
71
41
87
kindergarten/capitalize-the-first-letter-of-a-sentence
64
74
100
100
100
kindergarten/who-what-when-where-or-why
52
66
74
84
83
kindergarten/what-am-i
54
100
100
83
100
kindergarten/read-questions-with-short-vowel-words
52
100
100
68
100
kindergarten/find-the-action-verb
81
100
100
100
100
kindergarten/find-the-complete-sentence
56
91
100
100
100
grade-1/describe-the-difference-between-related-words
44
95
84
100
100
grade-1/which-word-does-not-rhyme
25
58
25
65
88
grade-1/to-have-use-the-correct-form
53
100
100
100
100
grade-1/complete-the-sentence-with-a-two-syllable-word
52
100
100
100
100
grade-1/use-actions-and-dialogue-to-understand-characters
48
100
100
100
100
grade-1/complete-the-sentence-with-the-correct-short-vowel-word
54
100
100
100
100
grade-1/complete-the-rhyme
72
64
41
73
98
grade-1/who-what-when-where-or-why
66
74
100
93
100
grade-1/what-am-i
40
100
100
78
100
grade-1/complete-the-sentence-with-the-correct-sight-word-sets-1-2-3
49
100
100
100
100
grade-1/complete-the-sentence-with-the-correct-sight-word-sets-4-5-6-7
36
100
100
100
100
grade-2/which-word-does-not-rhyme
27
75
34
67
87
grade-2/complete-the-sentence-with-the-correct-sight-word
34
100
100
100
100
grade-2/to-have-use-the-correct-form
52
100
100
100
100
grade-2/complete-the-sentence-with-a-two-syllable-word
25
100
100
100
100
grade-2/complete-the-sentence-with-a-three-letter-consonant-blend-word
76
100
100
100
100
grade-2/use-subordinating-conjunctions
62
84
79
83
100
grade-2/use-the-correct-homophone
63
100
93
100
100
grade-2/is-it-a-complete-sentence-or-a-fragment
81
72
90
100
100
grade-2/use-time-order-words
63
86
96
100
100
grade-3/distinguish-characters-points-of-view
44
100
100
100
100
grade-3/determine-the-meanings-of-words-with-greek-and-latin-roots
36
100
100
100
100
grade-3/describe-the-difference-between-related-words
69
100
100
100
98
grade-3/to-have-use-the-correct-form
64
100
100
100
100
grade-3/use-subordinating-conjunctions
64
77
80
71
81
grade-3/use-the-correct-homophone
52
94
100
100
100
grade-3/is-it-a-complete-sentence-or-a-fragment
52
78
66
100
100
grade-3/use-time-order-words
43
95
76
88
75
grade-3/is-it-a-complete-sentence-or-a-run-on
66
85
66
100
100
grade-3/choose-the-synonym
59
100
100
100
100
grade-3/choose-topic-sentences-for-expository-paragraphs
63
100
100
100
100
grade-3/is-the-sentence-a-statement-question-command-or-exclamation
56
100
100
100
100
grade-3/capitalizing-titles
35
59
58
100
83
grade-3/does-the-adjective-tell-you-what-kind-or-how-many
73
100
100
100
100
grade-3/determine-the-meanings-of-similes
64
100
100
100
100
grade-3/revise-the-sentence-using-a-stronger-verb
66
100
100
81
100
grade-3/choose-between-personal-and-reflexive-pronouns
45
82
72
96
86
grade-3/use-the-correct-subject-or-verb
62
54
77
79
100
grade-3/is-the-noun-singular-or-plural
67
100
72
100
100
grade-3/choose-between-subject-and-object-personal-pronouns
63
85
91
86
100
grade-3/is-it-a-complete-sentence-a-fragment-or-a-run-on
48
91
66
100
100
grade-3/use-actions-and-dialogue-to-understand-characters
50
100
100
100
100
grade-3/use-the-correct-article-a-or-an
69
56
41
58
100
grade-3/determine-the-themes-of-myths-fables-and-folktales
61
100
100
100
100
grade-3/is-the-sentence-in-the-past-present-or-future-tense
29
100
91
100
100
grade-3/choose-the-antonym
47
100
100
100
100
grade-3/to-be-use-the-correct-form
61
100
100
100
100
grade-3/identify-text-structures
55
98
100
100
100
grade-3/does-the-adverb-tell-you-how-when-or-where
52
100
81
100
100
grade-3/which-word-is-a-noun
61
76
78
100
100
grade-3/identify-the-irregular-past-tense-ii
54
100
100
100
100
grade-3/read-about-famous-places
55
100
100
100
100
grade-3/use-key-details-to-determine-the-main-idea
52
100
100
100
100
grade-3/which-sentence-is-in-the-regular-past-tense
60
100
100
100
100
grade-3/which-sentence-uses-an-antonym
50
100
84
100
100
grade-3/choose-between-adjectives-and-adverbs
43
89
88
100
100
grade-3/use-action-verbs
48
100
100
100
100
grade-3/pronoun-verb-agreement
73
73
54
99
100
grade-3/greetings-and-closings-of-letters
48
76
88
88
81
grade-3/make-predictions-about-a-story
42
100
100
100
100
grade-3/draw-inferences-from-a-text
52
100
100
100
100
grade-3/identify-base-words-prefixes-and-suffixes
64
81
76
100
100
grade-3/which-sentence-has-the-same-meaning
59
79
100
100
100
grade-3/identify-plurals-singular-possessives-and-plural-possessives
37
100
100
100
100
grade-3/identify-the-authors-purpose-passages
28
100
87
75
100
grade-3/choose-the-text-that-matches-the-writers-purpose
47
100
100
100
100
grade-3/choose-topic-sentences-for-narrative-paragraphs
53
100
100
100
100
grade-3/which-definition-matches-the-sentence
51
100
74
100
100
grade-3/use-greek-and-latin-roots-as-clues-to-the-meanings-of-words
63
100
100
100
100
grade-3/distinguish-facts-from-opinions
50
100
100
100
100
grade-3/determine-the-meanings-of-greek-and-latin-roots
27
100
84
100
100
grade-3/use-coordinating-conjunctions
38
93
71
100
100
grade-3/is-the-subject-singular-or-plural
37
100
100
100
100
grade-3/choose-reasons-to-support-an-opinion
59
56
91
91
91
grade-3/determine-the-meaning-of-a-word-with-a-suffix-review
32
94
100
100
100
grade-3/use-academic-vocabulary-in-context
29
100
100
100
100
grade-3/select-the-words-that-dont-belong
35
46
55
66
64
grade-3/use-adjectives-to-compare
32
74
81
100
100
grade-3/create-compound-sentences
69
36
35
73
66
grade-3/use-adverbs-to-compare
52
100
77
92
82
grade-3/formatting-and-capitalizing-titles
51
55
50
53
53
grade-3/read-poetry
48
100
100
100
100
grade-3/punctuating-dialogue
49
84
80
82
91
grade-3/show-character-emotions-and-traits
45
78
91
91
91
grade-3/use-the-correct-article-a-an-or-the
32
61
64
55
86
grade-3/choose-the-best-transition
45
100
100
100
100
grade-3/is-the-sentence-simple-or-compound
46
88
82
100
100
grade-3/determine-the-meanings-of-words-with-prefixes-and-suffixes-review
66
100
97
100
100
grade-4/distinguish-characters-points-of-view
54
100
100
100
100
grade-4/determine-the-meanings-of-words-with-greek-and-latin-roots
32
100
100
100
100
Table 5: Exam scores for Language Arts skill (part 1).

--- Page 18 ---

Grade/Skill
Random
LLaMA2-70B-Chat
SocialAgentLLaMA2−70B−Chat
GPT3.5-Turbo
SocialAgentGPT3.5−Turbo
grade-4/describe-the-difference-between-related-words
52
89
88
100
100
grade-4/to-have-use-the-correct-form
63
100
100
100
100
grade-4/use-subordinating-conjunctions
49
100
64
100
100
grade-4/use-the-correct-homophone
39
100
100
100
100
grade-4/is-it-a-complete-sentence-or-a-fragment
67
70
97
100
100
grade-4/choose-the-best-concluding-sentence
46
100
100
100
100
grade-4/identify-the-narrative-point-of-view
52
88
76
82
100
grade-4/formatting-and-capitalizing-titles
42
50
46
62
54
grade-4/choose-the-best-topic-sentence
20
100
100
100
100
grade-4/determine-the-meaning-of-idioms-from-context-set-1
48
100
100
100
100
grade-4/punctuating-dialogue
26
92
78
92
81
grade-4/determine-the-meanings-of-similes-and-metaphors
51
100
100
100
100
grade-4/identify-similes-and-metaphors
30
79
76
100
100
grade-4/use-the-correct-modal-verb
65
95
94
100
100
grade-4/determine-the-meaning-of-idioms-from-context-set-2
55
100
100
100
100
grade-4/identify-the-meaning-of-idioms-and-adages-set-2
54
100
100
100
100
grade-4/use-the-perfect-verb-tenses
84
100
92
100
100
grade-4/is-the-sentence-declarative-interrogative-imperative-or-exclamatory
53
93
100
100
82
grade-4/use-the-progressive-verb-tenses
75
84
82
100
100
grade-4/what-does-the-modal-verb-show
47
73
70
100
100
grade-4/identify-the-meaning-of-idioms-and-adages-set-1
49
75
100
100
100
grade-4/use-thesaurus-entries
42
100
100
94
100
grade-5/determine-the-meanings-of-words-with-greek-and-latin-roots
55
100
100
100
100
grade-5/describe-the-difference-between-related-words
59
100
88
100
100
grade-5/use-the-correct-homophone
51
100
100
100
100
grade-5/use-words-as-clues-to-the-meanings-of-greek-and-latin-roots
21
100
100
100
100
grade-5/analogies
67
72
73
100
100
grade-5/is-it-a-complete-sentence-or-a-fragment
53
76
76
100
100
grade-5/choose-reasons-to-support-an-opinion
66
64
91
92
91
grade-5/choose-the-synonym
47
100
100
100
100
grade-5/select-the-words-that-dont-belong
33
66
67
66
65
grade-5/is-it-a-complete-sentence-or-a-run-on
63
70
65
100
100
grade-5/use-academic-vocabulary-in-context
61
100
100
100
100
grade-5/use-adjectives-to-compare
63
68
100
100
84
grade-5/capitalizing-titles
57
61
44
97
81
grade-5/use-the-correct-subject-or-verb
68
76
69
71
100
grade-5/choose-between-subject-and-object-personal-pronouns
38
85
74
100
100
grade-5/choose-between-personal-and-reflexive-pronouns
53
85
92
100
100
grade-5/choose-the-best-concluding-sentence
39
100
100
100
100
grade-5/create-compound-sentences
37
46
22
72
86
grade-5/is-it-a-complete-sentence-a-fragment-or-a-run-on
59
87
69
100
100
grade-5/is-the-word-an-adjective-or-adverb
69
100
92
100
100
grade-5/identify-the-narrative-point-of-view
60
78
73
75
94
grade-5/use-actions-and-dialogue-to-understand-characters
46
100
100
100
100
grade-5/use-adverbs-to-compare
84
64
63
97
77
grade-5/is-the-sentence-in-the-past-present-or-future-tense
44
87
60
100
100
grade-5/formatting-and-capitalizing-titles
50
46
46
46
37
grade-5/which-definition-matches-the-sentence
57
100
90
100
100
grade-5/choose-the-antonym
71
100
100
100
100
grade-5/choose-the-best-topic-sentence
48
100
100
100
100
grade-5/read-poetry
54
100
90
100
100
grade-5/show-character-emotions-and-traits
54
70
91
91
92
grade-5/identify-text-structures
71
90
100
100
100
grade-5/determine-the-meaning-of-idioms-from-context-set-1
46
100
100
100
100
grade-5/punctuating-dialogue
42
87
81
84
84
grade-5/determine-the-meanings-of-similes-and-metaphors
61
100
100
100
100
grade-5/use-key-details-to-determine-the-main-idea
27
100
100
100
100
grade-5/choose-between-adjectives-and-adverbs
49
100
80
100
83
grade-5/use-the-meanings-of-words-as-clues-to-the-meanings-of-greek-and-latin-roots
42
100
100
100
100
grade-5/use-greek-and-latin-roots-as-clues-to-the-meanings-of-words
28
100
100
100
100
grade-5/use-coordinating-conjunctions
48
100
47
100
100
grade-5/identify-similes-and-metaphors
73
71
72
100
100
grade-5/interpret-the-meaning-of-an-allusion-from-its-source
68
100
100
100
100
grade-5/positive-and-negative-connotation
75
100
67
100
100
grade-5/distinguish-facts-from-opinions
72
100
100
100
100
grade-5/choose-the-best-transition
38
100
86
100
100
grade-5/draw-inferences-from-a-text
41
100
79
83
94
grade-5/is-the-sentence-simple-or-compound
64
77
67
100
100
grade-5/identify-elements-of-poetry
42
57
45
48
88
grade-5/identify-plurals-singular-possessives-and-plural-possessives
60
100
56
100
100
grade-5/determine-the-meanings-of-greek-and-latin-roots
41
100
70
100
100
grade-5/analyze-the-effects-of-figures-of-speech-on-meaning-and-tone
56
100
100
100
100
grade-5/words-with-sub
56
63
83
100
100
grade-5/words-with-pre
40
100
100
100
100
grade-5/use-the-correct-modal-verb
54
100
97
100
100
grade-5/use-the-perfect-verb-tenses
35
100
77
100
100
grade-5/words-with-less
67
100
100
100
100
grade-5/words-with-un-dis-in-im-and-non
50
100
100
100
100
grade-5/determine-the-meaning-of-idioms-from-context-set-2
53
100
100
100
100
grade-5/choose-between-the-past-tense-and-past-participle
72
73
100
100
100
grade-5/words-with-re
64
100
100
100
100
grade-5/use-the-correct-pair-of-correlative-conjunctions
64
64
41
76
84
grade-5/is-the-sentence-declarative-interrogative-imperative-or-exclamatory
37
100
100
100
92
grade-5/what-does-the-modal-verb-show
57
98
76
100
100
grade-5/use-the-progressive-verb-tenses
73
80
92
100
100
grade-5/words-with-ful
77
100
100
100
100
grade-5/compound-subjects-and-objects-with-personal-pronouns
84
72
55
94
100
grade-5/words-with-able-and-ible
54
100
100
100
100
grade-5/determine-the-themes-of-short-stories
57
84
69
73
100
grade-5/use-the-correct-frequently-confused-word
71
56
73
75
75
grade-5/words-with-mis
39
100
77
100
100
grade-5/which-sentence-is-more-formal
75
100
100
100
100
grade-5/is-the-sentence-simple-compound-or-complex
60
40
55
95
98
grade-6/determine-the-meanings-of-words-with-greek-and-latin-roots
40
100
100
100
100
grade-6/describe-the-difference-between-related-words
52
100
100
100
100
grade-6/use-the-correct-homophone
53
97
100
100
100
grade-6/use-words-as-clues-to-the-meanings-of-greek-and-latin-roots
49
100
100
100
100
grade-6/analogies
43
83
64
100
100
grade-6/is-it-a-complete-sentence-or-a-fragment
29
77
53
100
100
grade-6/choose-between-subject-and-object-pronouns
43
94
65
100
100
grade-6/analogies-challenge
19
80
75
87
100
grade-6/is-it-a-complete-sentence-or-a-run-on
59
70
64
100
100
grade-6/transitions-with-conjunctive-adverbs
69
71
73
87
68
grade-6/determine-the-authors-point-of-view
66
66
100
100
100
grade-6/compare-two-texts-with-different-genres
37
100
100
100
100
grade-6/choose-evidence-to-support-a-claim
60
45
86
78
86
grade-6/use-personification
53
80
51
51
46
grade-6/is-the-word-an-adjective-or-adverb
59
76
100
100
100
grade-6/is-it-a-complete-sentence-a-fragment-or-a-run-on
52
82
72
100
100
grade-6/which-definition-matches-the-sentence
36
100
19
100
100
grade-6/identify-counterclaims
53
80
100
100
100
grade-6/identify-text-structures
74
72
100
100
100
grade-6/use-the-correct-pair-of-correlative-conjunctions
60
44
50
56
77
Table 6: Exam scores for Language Arts skill (part 2).

--- Page 19 ---

Grade/Skill
Random
LLaMA2-70B-Chat
SocialAgentLLaMA2−70B−Chat
GPT3.5-Turbo
SocialAgentGPT3.5−Turbo
grade-6/is-the-pronoun-reflexive-or-intensive
47
56
46
63
74
grade-6/interpret-figures-of-speech
61
100
100
100
100
grade-6/classify-figures-of-speech
76
100
100
81
80
grade-6/is-the-sentence-declarative-interrogative-imperative-or-exclamatory
31
73
79
100
100
grade-6/vocabulary-review-trace-an-argument
40
100
100
100
100
grade-6/identify-the-authors-purpose
39
100
100
100
100
grade-6/is-it-a-direct-object-or-an-indirect-object
44
49
71
70
100
grade-6/compound-subjects-and-objects-with-pronouns
71
74
48
100
100
grade-6/identify-vague-pronoun-references
82
66
81
100
76
grade-6/choose-between-adjectives-and-adverbs
34
100
100
100
100
grade-6/what-does-the-punctuation-suggest
46
49
60
79
72
grade-6/suggest-appropriate-revisions
55
67
83
91
73
grade-6/classify-logical-fallacies
58
69
70
100
100
grade-6/use-greek-and-latin-roots-as-clues-to-the-meanings-of-words
40
100
100
100
100
grade-6/use-the-correct-frequently-confused-word
42
81
79
69
78
grade-6/distinguish-facts-from-opinions
43
100
100
100
100
grade-6/use-the-correct-verb-with-compound-subjects
64
74
72
91
100
grade-6/determine-the-main-idea-of-a-passage
46
100
90
86
100
grade-6/analyze-short-stories
35
64
80
63
71
grade-6/identify-plurals-singular-possessives-and-plural-possessives
43
75
69
100
100
grade-6/which-sentence-is-more-formal
99
100
100
100
100
grade-6/determine-the-meanings-of-greek-and-latin-roots
36
100
96
100
100
grade-6/analyze-passages-from-roll-of-thunder-hear-my-cry-part-1
67
100
94
100
100
grade-6/use-the-correct-modal-verb
64
100
100
100
100
grade-6/use-the-perfect-verb-tenses
63
92
86
82
100
grade-6/determine-the-meaning-of-idioms-from-context-set-2
72
100
100
100
100
grade-6/choose-between-the-past-tense-and-past-participle
64
100
93
100
100
grade-6/use-the-correct-subject-or-verb
68
66
59
73
79
grade-6/evaluate-newspaper-headlines-for-bias
36
71
80
100
84
grade-6/determine-the-meaning-of-idioms-from-context-set-1
44
100
100
100
100
grade-6/use-the-meanings-of-words-as-clues-to-the-meanings-of-greek-and-latin-roots
16
100
97
100
100
grade-6/what-does-the-modal-verb-show
65
100
92
100
100
grade-6/use-the-progressive-verb-tenses
71
100
85
100
100
grade-6/use-coordinating-conjunctions
73
84
58
100
100
grade-6/is-the-sentence-simple-compound-or-complex
39
43
51
75
100
grade-7/determine-the-meanings-of-words-with-greek-and-latin-roots
43
100
19
100
100
grade-7/describe-the-difference-between-related-words
60
100
100
100
100
grade-7/use-the-correct-homophone
44
100
100
100
100
grade-7/use-words-as-clues-to-the-meanings-of-greek-and-latin-roots
27
100
82
100
100
grade-7/analogies
51
100
71
100
100
grade-7/is-it-a-complete-sentence-or-a-fragment
67
74
67
100
100
grade-7/is-it-a-phrase-or-a-clause
78
59
42
98
74
grade-7/choose-between-subject-and-object-pronouns
69
100
71
100
100
grade-7/is-the-sentence-simple-compound-complex-or-compound-complex
28
19
25
34
70
grade-7/analogies-challenge
48
73
81
99
100
grade-7/is-it-a-complete-sentence-or-a-run-on
64
84
60
100
100
grade-7/are-the-modifiers-used-correctly
80
74
80
64
68
grade-7/recall-the-source-of-an-allusion
57
100
93
100
100
grade-7/transitions-with-conjunctive-adverbs
54
83
51
70
82
grade-7/determine-the-authors-point-of-view
65
54
100
100
100
grade-7/choose-the-synonym
54
100
100
100
100
grade-7/choose-evidence-to-support-a-claim
45
46
86
55
86
grade-7/use-personification
45
43
46
78
71
grade-7/identify-plagiarism
36
44
37
41
23
grade-7/is-the-word-an-adjective-or-adverb
59
84
89
100
100
grade-7/is-it-a-complete-sentence-a-fragment-or-a-run-on
59
69
64
100
100
grade-7/which-definition-matches-the-sentence
58
100
46
100
100
grade-7/choose-the-antonym
60
100
92
100
100
grade-7/identify-text-structures
58
69
100
100
100
grade-7/use-the-correct-pair-of-correlative-conjunctions
64
64
55
79
82
grade-7/is-the-pronoun-reflexive-or-intensive
33
48
70
73
68
grade-7/interpret-figures-of-speech
46
100
100
100
100
grade-7/classify-figures-of-speech
64
100
100
88
69
grade-7/is-the-sentence-declarative-interrogative-imperative-or-exclamatory
32
83
76
100
100
grade-7/vocabulary-review-trace-an-argument
25
82
100
100
100
grade-7/identify-the-authors-purpose
50
100
100
100
100
grade-7/decide-whether-ellipses-are-used-appropriately
63
47
45
76
68
grade-7/compound-subjects-and-objects-with-pronouns
47
78
55
100
100
grade-7/identify-vague-pronoun-references
45
67
83
83
72
grade-7/choose-between-adjectives-and-adverbs
65
92
92
96
100
grade-7/what-does-the-punctuation-suggest
46
59
68
77
72
grade-7/suggest-appropriate-revisions
61
82
59
77
82
grade-7/determine-the-themes-of-short-stories
43
61
80
63
70
grade-7/classify-logical-fallacies
55
72
82
100
93
grade-7/use-greek-and-latin-roots-as-clues-to-the-meanings-of-words
57
100
100
100
100
grade-7/interpret-the-meaning-of-an-allusion-from-its-source
50
100
100
100
100
grade-7/use-the-correct-frequently-confused-word
54
76
70
79
75
grade-7/distinguish-facts-from-opinions
40
100
91
100
100
grade-7/use-the-correct-verb-with-compound-subjects
64
56
62
83
100
grade-7/determine-the-main-idea-of-a-passage
46
77
100
100
100
grade-7/identify-plurals-singular-possessives-and-plural-possessives
45
82
54
100
100
grade-7/which-sentence-is-more-formal
57
100
100
100
100
grade-7/determine-the-meanings-of-greek-and-latin-roots
23
100
74
100
100
grade-7/use-parallel-structure
43
82
57
74
95
grade-8/determine-the-meanings-of-words-with-greek-and-latin-roots
25
100
100
100
100
grade-8/describe-the-difference-between-related-words
69
100
82
100
100
grade-8/use-the-correct-homophone
57
82
99
100
100
grade-8/use-words-as-clues-to-the-meanings-of-greek-and-latin-roots
24
100
67
100
100
grade-8/analogies
62
87
64
100
95
grade-8/is-it-a-complete-sentence-or-a-fragment
64
100
68
100
100
grade-8/choose-between-subject-and-object-pronouns
25
77
56
100
100
grade-8/is-the-sentence-simple-compound-complex-or-compound-complex
16
25
25
52
63
grade-8/analogies-challenge
32
94
57
82
100
grade-8/is-it-a-complete-sentence-or-a-run-on
59
65
71
100
100
grade-8/are-the-modifiers-used-correctly
58
59
72
85
75
grade-8/recall-the-source-of-an-allusion
53
100
100
100
100
grade-8/transitions-with-conjunctive-adverbs
79
82
68
84
79
grade-8/determine-the-authors-point-of-view
64
43
100
100
100
grade-8/choose-the-synonym
46
100
100
100
100
grade-8/compare-two-texts-with-different-genres
41
86
100
100
100
grade-8/choose-evidence-to-support-a-claim
26
46
86
64
86
grade-8/choose-between-personal-and-reflexive-pronouns
37
79
72
100
100
grade-8/use-personification
54
90
43
100
83
grade-8/identify-plagiarism
65
49
42
45
48
grade-8/identify-the-narrative-point-of-view
56
60
63
85
100
grade-8/is-the-word-an-adjective-or-adverb
50
71
100
100
100
grade-8/identify-counterclaims
49
80
100
100
100
grade-8/is-it-a-complete-sentence-a-fragment-or-a-run-on
37
67
73
100
100
grade-8/which-definition-matches-the-sentence
46
100
9
100
100
grade-8/choose-the-antonym
63
100
83
100
100
grade-8/identify-text-structures
45
63
100
100
100
grade-8/use-the-correct-pair-of-correlative-conjunctions
54
38
64
77
74
grade-8/identify-active-and-passive-voice
64
70
47
87
100
Table 7: Exam scores for Language Arts skill (part 3).

--- Page 20 ---

Grade/Skill
Random
LLaMA2-70B-Chat
SocialAgentLLaMA2−70B−Chat
GPT3.5-Turbo
SocialAgentGPT3.5−Turbo
grade-8/is-the-pronoun-reflexive-or-intensive
43
64
70
57
92
grade-8/interpret-figures-of-speech
59
100
100
100
100
grade-8/identify-the-verb-mood
32
76
56
100
100
grade-8/classify-figures-of-speech
64
100
84
100
78
grade-8/is-the-sentence-declarative-interrogative-imperative-or-exclamatory
36
83
94
100
100
grade-8/vocabulary-review-trace-an-argument
37
84
100
100
100
grade-8/is-it-a-direct-object-or-an-indirect-object
60
63
79
75
100
grade-8/identify-the-authors-purpose
34
100
100
100
100
grade-8/decide-whether-ellipses-are-used-appropriately
58
52
68
100
61
grade-8/compound-subjects-and-objects-with-pronouns
63
73
60
100
97
grade-8/identify-vague-pronoun-references
56
67
79
70
60
grade-8/choose-between-adjectives-and-adverbs
68
100
86
100
87
grade-8/what-does-the-punctuation-suggest
43
62
70
81
63
grade-8/suggest-appropriate-revisions
69
74
80
84
84
grade-8/identify-thesis-statements
79
65
75
75
82
grade-8/determine-the-themes-of-short-stories
36
59
80
59
69
grade-8/classify-logical-fallacies
55
67
52
100
100
grade-8/use-greek-and-latin-roots-as-clues-to-the-meanings-of-words
51
100
100
100
100
grade-8/interpret-the-meaning-of-an-allusion-from-its-source
63
100
100
100
100
grade-8/use-the-correct-frequently-confused-word
66
74
70
77
75
grade-8/positive-and-negative-connotation
67
70
91
100
100
grade-8/distinguish-facts-from-opinions
51
94
86
91
100
grade-8/use-thesaurus-entries
45
100
100
100
100
grade-8/use-the-correct-verb-with-compound-subjects
61
73
82
100
98
grade-8/determine-the-main-idea-of-a-passage
53
82
100
95
100
grade-8/analyze-short-stories
33
63
95
49
70
grade-8/identify-plurals-singular-possessives-and-plural-possessives
46
81
64
95
100
grade-8/determine-the-meanings-of-greek-and-latin-roots
28
84
79
100
100
grade-8/which-sentence-is-more-formal
64
100
100
100
100
grade-8/use-parallel-structure
55
64
69
92
94
grade-9/determine-the-meanings-of-words-with-greek-and-latin-roots
23
100
100
100
100
grade-9/use-words-as-clues-to-the-meanings-of-greek-and-latin-roots
25
100
73
100
100
grade-9/analogies
44
100
64
100
100
grade-9/is-it-a-phrase-or-a-clause
51
59
45
100
68
grade-9/is-the-sentence-simple-compound-complex-or-compound-complex
36
17
24
34
66
grade-9/analogies-challenge
37
78
82
100
100
grade-9/words-with-pre
54
100
100
100
100
grade-9/are-the-modifiers-used-correctly
38
80
84
82
85
grade-9/recall-the-source-of-an-allusion
49
100
100
100
100
grade-9/transitions-with-conjunctive-adverbs
55
80
67
91
77
grade-9/words-with-less
60
100
100
100
100
grade-9/identify-plagiarism
37
39
35
39
46
grade-9/words-with-re
25
100
100
100
100
grade-9/identify-the-narrative-point-of-view
36
52
49
82
82
grade-9/use-the-correct-pair-of-correlative-conjunctions
54
64
49
78
82
grade-9/identify-active-and-passive-voice
39
63
51
100
100
grade-9/interpret-figures-of-speech
62
100
100
100
100
grade-9/identify-the-verb-mood
36
75
66
100
100
grade-9/is-the-sentence-declarative-interrogative-imperative-or-exclamatory
13
73
85
100
79
grade-9/decide-whether-ellipses-are-used-appropriately
60
60
92
86
68
grade-9/identify-vague-pronoun-references
39
51
73
76
81
grade-9/choose-between-adjectives-and-adverbs
59
83
90
100
91
grade-9/what-does-the-punctuation-suggest
53
64
73
68
83
grade-9/suggest-appropriate-revisions
75
70
69
80
64
grade-9/identify-thesis-statements
48
77
46
64
73
grade-9/classify-logical-fallacies
46
95
50
100
94
grade-9/use-greek-and-latin-roots-as-clues-to-the-meanings-of-words
41
100
100
100
100
grade-9/interpret-the-meaning-of-an-allusion-from-its-source
57
100
100
100
100
grade-9/use-the-correct-frequently-confused-word
52
68
74
88
75
grade-9/words-with-mis
62
95
100
100
100
grade-9/distinguish-facts-from-opinions
66
83
100
100
100
grade-9/use-thesaurus-entries
40
100
100
100
100
grade-9/determine-the-main-idea-of-a-passage
79
100
100
100
100
grade-9/determine-the-meanings-of-greek-and-latin-roots
28
82
76
100
100
grade-9/use-parallel-structure
69
87
65
100
77
grade-9/use-dictionary-entries-to-determine-correct-usage
72
85
100
72
93
grade-9/which-text-is-most-formal
58
100
100
100
100
grade-9/choose-the-topic-sentence-that-best-captures-the-main-idea
58
38
100
97
100
grade-9/identify-sentence-fragments
46
54
41
100
90
grade-9/use-context-as-a-clue-to-the-meanings-of-foreign-expressions
36
100
100
100
100
grade-9/use-the-correct-foreign-expression
69
100
100
100
100
grade-9/identify-audience-and-purpose
46
100
100
100
100
grade-9/classify-figures-of-speech-euphemism-hyperbole-oxymoron-paradox
65
65
84
84
92
grade-9/explore-words-with-new-or-contested-usages
69
57
64
60
54
grade-9/analyze-short-stories-set-1
32
93
84
59
100
grade-9/choose-punctuation-to-avoid-fragments-and-run-ons
18
22
39
49
53
grade-9/transition-logically-between-claims-evidence-analysis-and-counterclaims
41
94
79
91
83
grade-9/choose-the-analysis-that-logically-connects-the-evidence-to-the-claim
54
88
100
100
86
grade-9/identify-run-on-sentences
79
63
63
80
73
grade-9/use-words-accurately-and-precisely
59
85
65
100
92
grade-9/classify-figures-of-speech-review
43
100
95
100
83
grade-9/avoid-double-illogical-and-unclear-comparisons
37
46
66
69
88
grade-9/choose-the-best-evidence-to-support-a-claim
19
24
67
37
100
grade-9/use-appeals-to-ethos-pathos-and-logos-in-persuasive-writing
49
50
66
35
67
grade-9/identify-elements-of-poetry
54
56
70
76
87
grade-9/choose-the-word-whose-connotation-and-denotation-best-match-the-sentence
25
100
100
100
100
grade-9/analyze-short-stories-set-2
55
44
84
66
100
grade-9/evaluate-counterclaims
60
56
100
60
100
grade-9/use-etymologies-to-determine-the-meanings-of-words
41
100
100
100
100
grade-10/determine-the-meanings-of-words-with-greek-and-latin-roots
33
100
100
100
100
grade-10/use-words-as-clues-to-the-meanings-of-greek-and-latin-roots
36
100
90
100
100
grade-10/analogies
29
67
67
88
100
grade-10/is-it-a-phrase-or-a-clause
62
67
72
89
79
grade-10/is-the-sentence-simple-compound-complex-or-compound-complex
38
23
26
41
75
grade-10/analogies-challenge
39
85
45
100
79
grade-10/are-the-modifiers-used-correctly
55
73
60
95
81
grade-10/recall-the-source-of-an-allusion
48
95
100
100
100
grade-10/transitions-with-conjunctive-adverbs
41
79
64
70
83
grade-10/identify-plagiarism
23
13
14
23
38
grade-10/use-the-correct-pair-of-correlative-conjunctions
64
70
59
76
88
grade-10/identify-active-and-passive-voice
68
79
43
100
100
grade-10/interpret-figures-of-speech
35
100
100
100
100
grade-10/is-the-sentence-declarative-interrogative-imperative-or-exclamatory
26
49
80
100
84
grade-10/decide-whether-ellipses-are-used-appropriately
64
42
80
80
62
grade-10/identify-vague-pronoun-references
77
64
81
62
71
grade-10/choose-between-adjectives-and-adverbs
36
84
82
97
82
grade-10/what-does-the-punctuation-suggest
39
62
73
61
83
grade-10/suggest-appropriate-revisions
52
64
73
68
73
grade-10/identify-thesis-statements
65
33
34
71
67
grade-10/classify-logical-fallacies
36
100
60
100
100
grade-10/use-greek-and-latin-roots-as-clues-to-the-meanings-of-words
40
100
100
100
100
grade-10/interpret-the-meaning-of-an-allusion-from-its-source
60
100
100
100
100
grade-10/use-the-correct-frequently-confused-word
58
63
56
100
75
Table 8: Exam scores for Language Arts skill (part 4).

--- Page 21 ---

Grade/Skill
Random
LLaMA2-70B-Chat
SocialAgentLLaMA2−70B−Chat
GPT3.5-Turbo
SocialAgentGPT3.5−Turbo
grade-10/use-thesaurus-entries
68
100
100
100
100
grade-10/determine-the-main-idea-of-a-passage
53
100
11
100
100
grade-10/determine-the-meanings-of-greek-and-latin-roots
28
100
90
100
100
grade-10/use-parallel-structure
76
75
66
70
100
grade-10/use-dictionary-entries-to-determine-correct-usage
55
18
85
49
93
grade-10/which-text-is-most-formal
40
100
100
100
100
grade-10/choose-the-topic-sentence-that-best-captures-the-main-idea
37
39
93
100
100
grade-10/identify-sentence-fragments
42
45
42
100
95
grade-10/use-context-as-a-clue-to-the-meanings-of-foreign-expressions
26
100
100
100
100
grade-10/use-the-correct-foreign-expression
73
100
100
100
100
grade-10/identify-audience-and-purpose
40
100
71
90
90
grade-10/classify-figures-of-speech-euphemism-hyperbole-oxymoron-paradox
63
89
80
91
83
grade-10/explore-words-with-new-or-contested-usages
49
65
50
59
63
grade-10/choose-punctuation-to-avoid-fragments-and-run-ons
37
41
41
34
36
grade-10/transition-logically-between-claims-evidence-analysis-and-counterclaims
45
74
64
100
90
grade-10/choose-the-analysis-that-logically-connects-the-evidence-to-the-claim
37
87
100
100
100
grade-10/identify-run-on-sentences
48
64
53
100
92
grade-10/avoid-double-illogical-and-unclear-comparisons
15
64
71
67
79
grade-10/use-words-accurately-and-precisely
43
86
73
100
86
grade-10/classify-figures-of-speech-review
44
91
100
85
66
grade-10/choose-the-best-evidence-to-support-a-claim
61
21
100
68
100
grade-10/use-appeals-to-ethos-pathos-and-logos-in-persuasive-writing
37
64
52
37
84
grade-10/choose-the-word-whose-connotation-and-denotation-best-match-the-sentence
63
100
100
100
100
grade-10/use-etymologies-to-determine-the-meanings-of-words
42
100
100
100
100
grade-11/determine-the-meanings-of-words-with-greek-and-latin-roots
36
100
100
100
100
grade-11/describe-the-difference-between-related-words
46
100
100
100
100
grade-11/use-words-as-clues-to-the-meanings-of-greek-and-latin-roots
35
100
100
100
100
grade-11/analogies
54
69
67
92
89
grade-11/is-it-a-phrase-or-a-clause
45
45
45
78
76
grade-11/is-the-sentence-simple-compound-complex-or-compound-complex
27
24
34
63
43
grade-11/analogies-challenge
36
93
59
88
77
grade-11/are-the-modifiers-used-correctly
39
60
58
72
86
grade-11/recall-the-source-of-an-allusion
55
100
100
100
100
grade-11/transitions-with-conjunctive-adverbs
50
64
77
87
100
grade-11/decide-whether-ellipses-are-used-appropriately
78
62
77
90
71
grade-11/identify-vague-pronoun-references
49
58
64
62
87
grade-11/choose-between-adjectives-and-adverbs
59
95
69
80
94
grade-11/what-does-the-punctuation-suggest
59
50
60
73
76
grade-11/suggest-appropriate-revisions
51
58
59
56
64
grade-11/classify-logical-fallacies
39
67
55
100
88
grade-11/use-greek-and-latin-roots-as-clues-to-the-meanings-of-words
40
100
100
100
100
grade-11/interpret-the-meaning-of-an-allusion-from-its-source
60
100
100
100
100
grade-11/use-the-correct-frequently-confused-word
64
64
59
100
88
grade-11/determine-the-main-idea-of-a-passage
47
100
100
100
100
grade-11/determine-the-meanings-of-greek-and-latin-roots
33
100
79
100
100
grade-11/use-parallel-structure
100
100
61
79
100
grade-11/use-dictionary-entries-to-determine-correct-usage
67
51
100
72
100
grade-11/which-text-is-most-formal
69
97
100
100
100
grade-11/identify-sentence-fragments
75
62
49
100
100
grade-11/use-context-as-a-clue-to-the-meanings-of-foreign-expressions
30
100
100
100
100
grade-11/use-the-correct-foreign-expression
77
100
100
100
100
grade-11/identify-audience-and-purpose
14
100
99
100
100
grade-11/explore-words-with-new-or-contested-usages
73
50
55
42
67
grade-11/analyze-short-stories-set-1
51
62
92
100
77
grade-11/choose-punctuation-to-avoid-fragments-and-run-ons
28
35
40
73
60
grade-11/transition-logically-between-claims-evidence-analysis-and-counterclaims
40
87
54
83
69
grade-11/choose-the-analysis-that-logically-connects-the-evidence-to-the-claim
44
90
90
100
86
grade-11/identify-run-on-sentences
40
65
59
90
86
grade-11/use-words-accurately-and-precisely
44
100
86
100
100
grade-11/avoid-double-illogical-and-unclear-comparisons
44
64
68
63
82
grade-11/choose-the-best-evidence-to-support-a-claim
29
15
76
71
100
grade-11/use-appeals-to-ethos-pathos-and-logos-in-persuasive-writing
48
52
45
58
63
grade-11/choose-the-word-whose-connotation-and-denotation-best-match-the-sentence
55
100
100
100
100
grade-11/evaluate-counterclaims
33
58
100
36
100
grade-11/use-etymologies-to-determine-the-meanings-of-words
62
100
100
100
100
grade-11/classify-the-figure-of-speech-euphemism-hyperbole-oxymoron-paradox
48
82
67
100
88
grade-11/classify-the-figure-of-speech-anaphora-antithesis-apostrophe-assonance-chiasmus-understatement
64
100
100
100
100
grade-11/interpret-the-figure-of-speech
45
100
100
100
100
grade-11/prefixes
61
100
84
100
100
grade-11/suffixes
58
100
100
100
100
grade-11/classify-the-figure-of-speech-review
71
100
79
100
100
grade-12/determine-the-meanings-of-words-with-greek-and-latin-roots
41
100
100
100
100
grade-12/describe-the-difference-between-related-words
53
100
100
100
100
grade-12/use-words-as-clues-to-the-meanings-of-greek-and-latin-roots
29
100
76
100
100
grade-12/analogies
35
73
55
91
100
grade-12/is-it-a-phrase-or-a-clause
51
65
68
100
66
grade-12/is-the-sentence-simple-compound-complex-or-compound-complex
18
32
25
50
59
grade-12/analogies-challenge
27
68
59
94
100
grade-12/are-the-modifiers-used-correctly
66
60
68
68
90
grade-12/recall-the-source-of-an-allusion
58
100
94
100
100
grade-12/transitions-with-conjunctive-adverbs
63
83
66
79
81
grade-12/decide-whether-ellipses-are-used-appropriately
48
49
84
80
46
grade-12/identify-vague-pronoun-references
51
60
54
82
82
grade-12/choose-between-adjectives-and-adverbs
52
100
88
100
100
grade-12/what-does-the-punctuation-suggest
58
74
67
81
82
grade-12/suggest-appropriate-revisions
47
40
31
55
64
grade-12/classify-logical-fallacies
43
64
55
100
86
grade-12/use-greek-and-latin-roots-as-clues-to-the-meanings-of-words
35
100
100
100
100
grade-12/interpret-the-meaning-of-an-allusion-from-its-source
46
100
100
100
100
grade-12/use-the-correct-frequently-confused-word
59
62
59
75
92
grade-12/determine-the-meanings-of-greek-and-latin-roots
62
100
64
100
100
grade-12/use-parallel-structure
78
82
87
83
74
grade-12/use-dictionary-entries-to-determine-correct-usage
44
71
80
71
100
grade-12/which-text-is-most-formal
75
100
100
100
100
grade-12/identify-sentence-fragments
46
50
66
100
82
grade-12/use-context-as-a-clue-to-the-meanings-of-foreign-expressions
27
100
100
100
100
grade-12/explore-words-with-new-or-contested-usages
64
60
46
54
70
grade-12/choose-punctuation-to-avoid-fragments-and-run-ons
20
36
32
34
71
grade-12/transition-logically-between-claims-evidence-analysis-and-counterclaims
55
66
63
90
100
grade-12/choose-the-analysis-that-logically-connects-the-evidence-to-the-claim
54
76
100
100
84
grade-12/identify-run-on-sentences
50
56
45
81
82
grade-12/use-words-accurately-and-precisely
51
84
67
95
86
grade-12/avoid-double-illogical-and-unclear-comparisons
30
68
73
55
66
grade-12/choose-the-best-evidence-to-support-a-claim
46
23
100
72
100
grade-12/use-appeals-to-ethos-pathos-and-logos-in-persuasive-writing
50
47
27
26
78
grade-12/analyze-short-stories-set-2
40
68
74
61
82
grade-12/choose-the-word-whose-connotation-and-denotation-best-match-the-sentence
42
100
100
100
100
grade-12/evaluate-counterclaims
38
42
100
55
100
grade-12/use-etymologies-to-determine-the-meanings-of-words
35
100
100
100
100
grade-12/classify-the-figure-of-speech-euphemism-hyperbole-oxymoron-paradox
58
89
78
92
100
grade-12/classify-the-figure-of-speech-anaphora-antithesis-apostrophe-assonance-chiasmus-understatement
73
100
100
100
100
grade-12/interpret-the-figure-of-speech
55
100
92
100
100
Table 9: Exam scores for Language Arts skill (part 5).

--- Page 22 ---

Grade/Skill
Random
LLaMA2-70B-Chat
SocialAgentLLaMA2−70B−Chat
GPT3.5-Turbo
SocialAgentGPT3.5−Turbo
grade-2/compare-urban-suburban-and-rural-areas
29
100
100
100
100
grade-2/rosa-parks
0
67
60
73
73
grade-3/thurgood-marshall
0
96
96
96
96
grade-3/rosa-parks
6
61
56
61
61
grade-3/the-bill-of-rights
56
100
100
100
100
grade-4/the-war-of-1812-events-and-effects
3
66
69
72
66
grade-4/understand-overall-supply-and-demand
33
100
100
100
100
grade-5/the-war-of-1812-causes
0
63
58
63
63
grade-5/the-war-of-1812-events-and-effects
0
66
66
72
72
grade-5/the-bill-of-rights
26
100
100
100
100
grade-5/understand-overall-supply-and-demand
14
100
100
100
100
grade-5/identify-shortage-and-surplus
29
40
30
50
100
grade-6/understand-overall-supply-and-demand
49
100
100
100
100
grade-7/the-bill-of-rights
31
100
100
100
100
grade-8/the-bill-of-rights
31
95
100
100
100
grade-8/understand-overall-supply-and-demand
40
100
100
100
100
grade-8/identify-primary-and-secondary-sources
37
75
75
75
75
grade-8/identify-facts-and-opinions
59
100
100
100
100
Table 10: Exam scores for Social Studies skill.
Grade
Skills of Social Studies
kindergarten
days-of-the-week, pledge-of-allegiance, months-of-the-year
grade-1
months-of-the-year, days-of-the-week
grade-2
hanukkah, kwanzaa, compare-urban-suburban-and-rural-areas, thanksgiving, sitting-bull, susan-b-anthony, harriet-tubman, neil-armstrong, thurgood-marshall, federal-government, ramadan, easter, cesar-ch
avez, jackie-robinson, rosh-hashanah, amelia-earhart, christmas, dia-de-los-muertos, paul-revere, the-statue-of-liberty, george-washington-carver, davy-crockett, thomas-jefferson, state-government, lu
nar-new-year, bill-gates, the-white-house, abraham-lincoln, john-deere, holi, rosa-parks, frederick-douglass, benjamin-franklin, local-government, purpose-of-government, theodore-roosevelt
grade-3
easter, theodore-roosevelt, state-government, holi, cesar-chavez, the-bill-of-rights, bill-gates, ramadan, the-constitution, frederick-douglass, thomas-edison, jackie-robinson, kwanzaa, christmas, sus
an-b-anthony, harriet-tubman, paul-revere, davy-crockett, thurgood-marshall, george-washington-carver, sitting-bull, neil-armstrong, thomas-jefferson, hanukkah, dia-de-los-muertos, lunar-new-year, ros
a-parks, thanksgiving, presidential-elections
grade-4
jamestown-growth-of-a-colony, understand-overall-supply-and-demand, the-civil-war-war-tactics-and-the-home-front, the-war-of-1812-events-and-effects, the-constitution, the-american-revolution-the-rebe
llion-begins, world-war-i-the-road-to-peace, costs-and-benefits, new-england-colonies-religion-and-government, the-war-of-1812-causes
grade-5
the-statue-of-liberty, antebellum-period-slavery-and-politics-part-i, plymouth, the-civil-war-the-first-battle-of-bull-run-to-gettysburg, the-new-deal, the-great-depression-part-i, jamestown-growth-of
-a-colony, the-american-revolution-conclusion-and-aftermath, world-war-i-events-of-the-war, the-golden-gate-bridge, the-empire-state-building, costs-and-benefits, new-england-colonies-religion-and-gov
ernment, the-civil-war-the-end-of-the-war, middle-colonies-economy-and-society, federal-government, world-war-i-the-road-to-war, presidential-elections, the-constitution, the-war-of-1812-causes, world
-war-i-the-war-begins, the-great-depression-part-ii, the-civil-war-the-beginning-of-the-war, the-american-revolution-new-british-taxes, the-louisiana-purchase, thanksgiving, the-american-flag, the-war
-of-1812-events-and-effects, middle-colonies-founding-and-government, world-war-ii-lead-up-to-war-in-europe-asia, antebellum-period-economies-of-the-north-and-south, understand-overall-supply-and-dema
nd, local-government, world-war-i-the-road-to-peace, the-american-revolution-the-rebellion-begins, southern-colonies-founding-and-government, the-american-revolution-preparing-for-war, the-lewis-and-c
lark-expedition, jamestown-the-early-years, the-american-revolution-the-boston-tea-party, the-bill-of-rights, new-england-colonies-economy-and-conflict, southern-colonies-economy-and-slavery, antebell
um-period-abolitionist-and-proslavery-perspectives, world-war-ii-global-events, the-lincoln-memorial, the-civil-war-war-tactics-and-the-home-front, the-american-revolution-turning-the-tide-of-the-war,
identify-facts-and-opinions, mount-rushmore, the-washington-monument, the-white-house, antebellum-period-slavery-and-politics-part-ii, the-american-revolution-struggle-for-independence, reconstructio
n, state-government, identify-shortage-and-surplus, the-american-revolution-the-thirteen-colonies-under-british-rule
grade-6
origins-of-judaism, the-ancient-silk-road-goods-and-ideas, origins-of-hinduism, origins-of-christianity, foundations-of-maya-civilization, the-qin-empire, the-songhai-empire, french-and-english-expedi
tions-part-2, medieval-japan, caesar-and-the-end-of-the-roman-republic, the-han-dynasty, classical-athens-geography-and-society, mesopotamian-empires, the-mongol-empire, the-constitution-amendments, t
he-crusades, feudal-europe, the-middle-ages-after-1100, comparing-athens-and-sparta-part, early-chinese-thought, ancient-egypt-the-old-kingdom, the-ghana-empire, the-gupta-empire, early-mesopotamia, a
ncient-china, the-kingdoms-of-kush, origins-of-islam, ancient-egyptian-religion, classical-athens-government-and-culture, the-judicial-branch, origins-of-buddhism, the-mauryan-empire, trade-and-specia
lization, the-teachings-of-confucius, roman-government-monarchy-to-republic, the-executive-branch, understand-overall-supply-and-demand
grade-7
the-bill-of-rights, mesopotamian-empires, the-ancient-silk-road-geography-and-transportation, the-constitutional-convention, trade-and-specialization, foundations-of-aztec-civilization, ancient-egypti
an-religion, the-civil-war-bull-run-to-the-emancipation-proclamation, causes-of-the-american-revolution-the-french-and-indian-war, the-ancient-silk-road-goods-and-ideas, southern-colonies-founding-and
-government, identify-facts-and-opinions
grade-8
the-executive-branch, antebellum-reform-movements, the-revolutionary-war-struggle-for-independence, new-england-colonies-economy-and-interactions-with-native-americans, the-first-party-system-federali
sts-and-democratic-republicans, rights-and-responsibilities-of-active-citizenship, the-bill-of-rights, the-civil-war-the-beginning-of-the-war, state-and-local-government, source-analysis-the-declarati
on-of-independence, the-revolutionary-war-conclusion-and-aftermath, the-revolutionary-war-preparing-for-war, the-judicial-branch, washingtons-presidency-part-i, radical-reconstruction, the-reformation
, the-civil-war-the-conclusion-of-the-war, causes-of-the-civil-war-dred-scott-to-secession, world-war-i-the-great-war, the-civil-war-bull-run-to-the-emancipation-proclamation, understand-overall-suppl
y-and-demand, u-s-mexican-war, industrialization-in-the-gilded-age, the-revolutionary-war-turning-the-tide-of-war, portuguese-and-spanish-expeditions-part-ii, slavery-in-the-south, the-constitution-am
endments, the-abolitionists, causes-of-the-american-revolution-introduction-to-mercantilism-and-the-navigation-acts, the-constitutional-convention, the-civil-war-gettysburg-to-the-election-of-1864, th
e-legislative-branch, french-and-english-expeditions-part-i, the-articles-of-confederation, the-end-of-reconstruction-and-the-rise-of-jim-crow, the-constitution-interpretation, identify-facts-and-opin
ions, source-analysis-the-gettysburg-address, causes-of-the-american-revolution-politics-and-society, washingtons-presidency-part-ii, trade-and-specialization, world-war-i-the-road-to-war, the-marshal
l-court, causes-of-the-american-revolution-the-french-and-indian-war, pre-contact-native-peoples-introduction, new-england-colonies-founding-and-government, the-age-of-exploration-origins, the-scienti
fic-revolution, identify-primary-and-secondary-sources
Table 11: Full social studies skill summary.

--- Page 23 ---

Grade
Skills of Language Arts
pre-k
choose-the-uppercase-letter-that-matches-c-k-o-p-s-u-v-w-x-z, choose-the-lowercase-letter-that-matches-c-k-o-p-s-u-v-w-x-z, choose-the-lowercase-letter-that-matches-f-i-j-l-m-t-y, choose-the-uppercase
-letter-that-matches-f-i-j-l-m-t-y, choose-the-uppercase-letter-that-matches-a-b-d-e-g-h-n-q-r, choose-the-lowercase-letter-that-matches-a-b-d-e-g-h-n-q-r
kindergarten
who-what-when-where-or-why, complete-the-sentence-with-the-correct-sight-word, find-the-vowel-in-the-word, choose-the-uppercase-letter-that-matches-f-i-j-l-m-t-y, choose-the-uppercase-letter-that-matc
hes-review, choose-the-lowercase-letter-that-matches-a-b-d-e-g-h-n-q-r, choose-the-lowercase-letter-that-matches-review, capitalize-the-first-letter-of-a-sentence, complete-the-sentence-with-the-corre
ct-short-vowel-word, choose-the-lowercase-letter-that-matches-c-k-o-p-s-u-v-w-x-z, read-questions-with-short-vowel-words, find-the-complete-sentence, choose-the-uppercase-letter-that-matches-c-k-o-p-s
-u-v-w-x-z, find-the-action-verb, is-it-a-telling-sentence-or-an-asking-sentence, complete-the-rhyme, which-word-does-not-rhyme, choose-the-lowercase-letter-that-matches-f-i-j-l-m-t-y, what-am-i, choo
se-the-uppercase-letter-that-matches-a-b-d-e-g-h-n-q-r
grade-11
decide-whether-ellipses-are-used-appropriately, choose-the-word-whose-connotation-and-denotation-best-match-the-sentence, explore-words-with-new-or-contested-usages, identify-sentence-fragments, analo
gies, use-context-as-a-clue-to-the-meanings-of-foreign-expressions, evaluate-counterclaims, describe-the-difference-between-related-words, what-does-the-punctuation-suggest, use-greek-and-latin-roots-
as-clues-to-the-meanings-of-words, use-the-correct-foreign-expression, choose-the-analysis-that-logically-connects-the-evidence-to-the-claim, use-words-as-clues-to-the-meanings-of-greek-and-latin-root
s, analyze-the-effects-of-figures-of-speech-on-meaning-and-tone, transition-logically-between-claims-evidence-analysis-and-counterclaims, which-word-does-not-rhyme, which-text-is-most-formal, use-dict
ionary-entries-to-determine-correct-usage, use-words-accurately-and-precisely, analyze-short-stories-set-2, is-the-sentence-simple-compound-complex-or-compound-complex, analogies, use-thesaurus-entrie
s, are-the-modifiers-used-correctly, use-etymologies-to-determine-the-meanings-of-words, determine-the-meanings-of-words-with-greek-and-latin-roots, use-the-correct-pair-of-correlative-conjunctions, i
dentify-thesis-statements, describe-the-difference-between-related-words, choose-the-analysis-that-logically-connects-the-evidence-to-the-claim, is-the-sentence-declarative-interrogative-imperative-or
-exclamatory, decide-whether-ellipses-are-used-appropriately, determine-the-meanings-of-words-with-greek-and-latin-roots, classify-the-figure-of-speech-anaphora-antithesis-apostrophe-assonance-chiasmu
s-understatement, use-the-correct-frequently-confused-word, use-words-as-clues-to-the-meanings-of-greek-and-latin-roots, describe-the-difference-between-related-words, identify-vague-pronoun-reference
s, recall-the-source-of-an-allusion, identify-active-and-passive-voice, choose-between-adjectives-and-adverbs, identify-run-on-sentences, is-the-sentence-simple-compound-complex-or-compound-complex, s
uggest-appropriate-revisions, complete-the-sentence-with-a-two-syllable-word, choose-the-best-evidence-to-support-a-claim, identify-sentence-fragments, prefixes, identify-vague-pronoun-references, dec
ide-whether-ellipses-are-used-appropriately, identify-run-on-sentences, what-does-the-punctuation-suggest, is-it-a-phrase-or-a-clause, use-greek-and-latin-roots-as-clues-to-the-meanings-of-words, dete
rmine-the-meanings-of-greek-and-latin-roots, use-parallel-structure, classify-logical-fallacies, choose-punctuation-to-avoid-fragments-and-run-ons, is-it-a-phrase-or-a-clause, choose-the-best-evidence
-to-support-a-claim, analogies-challenge, choose-the-topic-sentence-that-best-captures-the-main-idea, who-what-when-where-or-why, suggest-appropriate-revisions, recall-the-source-of-an-allusion, analo
gies, choose-the-best-evidence-to-support-a-claim, classify-the-figure-of-speech-anaphora-antithesis-apostrophe-assonance-chiasmus-understatement, analyze-the-development-of-informational-passages-set
-2, determine-the-main-idea-of-a-passage, classify-logical-fallacies, complete-the-sentence-with-the-correct-sight-word-sets-1-2-3, use-etymologies-to-determine-the-meanings-of-words, which-text-is-mo
st-formal, avoid-double-illogical-and-unclear-comparisons, use-dictionary-entries-to-determine-correct-usage, explore-words-with-new-or-contested-usages, choose-the-word-whose-connotation-and-denotati
on-best-match-the-sentence, identify-plagiarism, choose-the-analysis-that-logically-connects-the-evidence-to-the-claim, choose-between-adjectives-and-adverbs, use-the-correct-frequently-confused-word,
analogies-challenge, recall-the-source-of-an-allusion, to-have-use-the-correct-form, choose-punctuation-to-avoid-fragments-and-run-ons, analyze-short-stories-set-1, use-the-correct-frequently-confuse
d-word, interpret-figures-of-speech, analyze-the-effects-of-figures-of-speech-on-meaning-and-tone, use-words-accurately-and-precisely, use-actions-and-dialogue-to-understand-characters, which-text-is-
most-formal, identify-run-on-sentences, use-context-to-identify-the-meaning-of-a-word, identify-audience-and-purpose, identify-vague-pronoun-references, use-the-correct-foreign-expression, trace-an-ar
gument-set-1, use-appeals-to-ethos-pathos-and-logos-in-persuasive-writing, interpret-the-figure-of-speech, avoid-double-illogical-and-unclear-comparisons, identify-audience-and-purpose, transition-log
ically-between-claims-evidence-analysis-and-counterclaims, interpret-the-meaning-of-an-allusion-from-its-source, domain-specific-vocabulary-in-context-science-and-technical-subjects, analyze-the-devel
opment-of-informational-passages-set-1, choose-between-adjectives-and-adverbs, choose-the-word-whose-connotation-and-denotation-best-match-the-sentence, determine-the-main-idea-of-a-passage, choose-pu
nctuation-to-avoid-fragments-and-run-ons, use-greek-and-latin-roots-as-clues-to-the-meanings-of-words, identify-sentence-fragments, interpret-the-meaning-of-an-allusion-from-its-source, determine-the-
meanings-of-greek-and-latin-roots, explore-words-with-new-or-contested-usages, which-word-is-not-like-the-others, interpret-the-meaning-of-an-allusion-from-its-source, classify-the-figure-of-speech-eu
phemism-hyperbole-oxymoron-paradox, what-does-the-punctuation-suggest, classify-figures-of-speech-euphemism-hyperbole-oxymoron-paradox, is-it-a-phrase-or-a-clause, use-parallel-structure, use-appeals-
to-ethos-pathos-and-logos-in-persuasive-writing, complete-the-rhyme, analogies-challenge, what-am-i, complete-the-sentence-with-the-correct-sight-word-sets-4-5-6-7, classify-the-figure-of-speech-revie
w, transition-logically-between-claims-evidence-analysis-and-counterclaims, trace-an-argument-set-2, avoid-double-illogical-and-unclear-comparisons, suffixes, transitions-with-conjunctive-adverbs, use
-etymologies-to-determine-the-meanings-of-words, use-dictionary-entries-to-determine-correct-usage, use-words-accurately-and-precisely, determine-the-meanings-of-words-with-greek-and-latin-roots, eval
uate-counterclaims, classify-figures-of-speech-review, determine-the-meanings-of-greek-and-latin-roots, transitions-with-conjunctive-adverbs, analyze-the-effects-of-figures-of-speech-on-meaning-and-to
ne, interpret-the-figure-of-speech, classify-logical-fallacies, identify-audience-and-purpose, suggest-appropriate-revisions, analyze-the-development-of-informational-passages-set-1, are-the-modifiers
-used-correctly, use-parallel-structure, use-context-as-a-clue-to-the-meanings-of-foreign-expressions, use-appeals-to-ethos-pathos-and-logos-in-persuasive-writing, complete-the-sentence-with-the-corre
ct-short-vowel-word, are-the-modifiers-used-correctly, use-words-as-clues-to-the-meanings-of-greek-and-latin-roots, transitions-with-conjunctive-adverbs, classify-the-figure-of-speech-euphemism-hyperb
ole-oxymoron-paradox, use-context-as-a-clue-to-the-meanings-of-foreign-expressions, classify-the-figure-of-speech-review, is-the-sentence-simple-compound-complex-or-compound-complex
grade-2
to-have-use-the-correct-form, use-time-order-words, use-the-correct-homophone, use-subordinating-conjunctions, which-word-does-not-rhyme, is-it-a-complete-sentence-or-a-fragment, complete-the-sentence
-with-the-correct-sight-word, complete-the-sentence-with-a-two-syllable-word, complete-the-sentence-with-a-three-letter-consonant-blend-word
grade-3
use-subordinating-conjunctions, to-have-use-the-correct-form, use-adverbs-to-compare, choose-topic-sentences-for-narrative-paragraphs, read-about-famous-places, choose-the-best-transition, use-the-cor
rect-article-a-an-or-the, pronoun-verb-agreement, choose-between-personal-and-reflexive-pronouns, to-be-use-the-correct-form, use-the-correct-homophone, use-the-correct-subject-or-verb, determine-the-
meanings-of-words-with-prefixes-and-suffixes-review, use-guide-words, is-it-a-complete-sentence-or-a-run-on, use-coordinating-conjunctions, determine-the-meanings-of-greek-and-latin-roots, create-comp
ound-sentences, use-time-order-words, distinguish-characters-points-of-view, read-about-famous-people, formatting-and-capitalizing-titles, identify-story-elements, which-sentence-uses-an-antonym, does
-the-adjective-tell-you-what-kind-or-how-many, choose-the-antonym, distinguish-facts-from-opinions, is-the-sentence-a-statement-question-command-or-exclamation, is-it-a-complete-sentence-or-a-fragment
, use-key-details-to-determine-the-main-idea, select-the-words-that-dont-belong, show-character-emotions-and-traits, greetings-and-closings-of-letters, which-definition-matches-the-sentence, identify-
plurals-singular-possessives-and-plural-possessives, use-action-verbs, determine-the-themes-of-myths-fables-and-folktales, choose-the-text-that-matches-the-writers-purpose, determine-the-meanings-of-s
imiles, is-the-word-an-adjective-or-adverb, is-the-noun-singular-or-plural, use-context-to-identify-the-meaning-of-a-word, choose-topic-sentences-for-expository-paragraphs, read-realistic-fiction-set-
2, read-realistic-fiction-set-1, which-sentence-has-the-same-meaning, read-about-business-and-technology, which-sentence-matches-the-definition, punctuating-dialogue, identify-the-irregular-past-tense
-ii, revise-the-sentence-using-a-stronger-verb, does-the-adverb-tell-you-how-when-or-where, is-the-sentence-simple-or-compound, is-the-subject-singular-or-plural, which-sentence-is-in-the-regular-past
-tense, choose-between-subject-and-object-personal-pronouns, use-actions-and-dialogue-to-understand-characters, choose-between-adjectives-and-adverbs, determine-the-meaning-of-a-word-with-a-suffix-rev
iew, capitalizing-titles, use-academic-vocabulary-in-context, determine-the-meanings-of-words-with-greek-and-latin-roots, make-predictions-about-a-story, use-adjectives-to-compare, read-historical-fic
tion, describe-the-difference-between-related-words, identify-the-authors-purpose-passages, is-the-sentence-in-the-past-present-or-future-tense, draw-inferences-from-a-text, identify-base-words-prefix
es-and-suffixes, identify-text-structures, read-poetry, choose-reasons-to-support-an-opinion, use-the-correct-article-a-or-an, use-greek-and-latin-roots-as-clues-to-the-meanings-of-words, choose-the-s
ynonym, is-it-a-complete-sentence-a-fragment-or-a-run-on, which-word-is-a-noun
grade-4
read-about-history, determine-the-meanings-of-words-with-greek-and-latin-roots, use-subordinating-conjunctions, choose-the-best-topic-sentence, use-the-progressive-verb-tenses, choose-between-the-past
-tense-and-past-participle, use-the-perfect-verb-tenses, determine-the-meaning-of-idioms-from-context-set-1, identify-similes-and-metaphors, use-the-correct-modal-verb, use-the-correct-homophone, iden
tify-the-narrative-point-of-view, describe-the-difference-between-related-words, what-does-the-modal-verb-show, choose-the-best-concluding-sentence, determine-the-meaning-of-idioms-from-context-set-2,
identify-the-meaning-of-idioms-and-adages-set-1, identify-the-meaning-of-idioms-and-adages-set-2, is-the-sentence-declarative-interrogative-imperative-or-exclamatory, to-have-use-the-correct-form, di
stinguish-characters-points-of-view, is-it-a-complete-sentence-or-a-fragment, formatting-and-capitalizing-titles, use-thesaurus-entries, punctuating-dialogue, determine-the-meanings-of-similes-and-met
aphors
grade-5
analyze-the-effects-of-figures-of-speech-on-meaning-and-tone, read-historical-fiction, use-the-progressive-verb-tenses, is-it-a-complete-sentence-a-fragment-or-a-run-on, use-greek-and-latin-roots-as-c
lues-to-the-meanings-of-words, words-with-re, use-key-details-to-determine-the-main-idea, choose-the-antonym, choose-reasons-to-support-an-opinion, use-adverbs-to-compare, compound-subjects-and-object
s-with-personal-pronouns, words-with-sub, identify-the-narrative-point-of-view, choose-between-subject-and-object-personal-pronouns, is-the-word-an-adjective-or-adverb, use-guide-words, identify-simil
es-and-metaphors, is-the-sentence-declarative-interrogative-imperative-or-exclamatory, use-context-to-identify-the-meaning-of-a-word, determine-the-meanings-of-similes-and-metaphors, choose-the-synony
m, use-the-meanings-of-words-as-clues-to-the-meanings-of-greek-and-latin-roots, draw-inferences-from-a-text, read-about-famous-people, words-with-pre, determine-the-themes-of-short-stories, select-the
-words-that-dont-belong, choose-the-best-concluding-sentence, create-compound-sentences, choose-the-best-transition, use-academic-vocabulary-in-context, choose-the-best-topic-sentence, use-the-correct
-subject-or-verb, choose-between-personal-and-reflexive-pronouns, use-coordinating-conjunctions, which-sentence-matches-the-definition, choose-between-adjectives-and-adverbs, use-words-as-clues-to-the
-meanings-of-greek-and-latin-roots, read-realistic-fiction, identify-text-structures, read-about-business-and-technology, words-with-ful, is-it-a-complete-sentence-or-a-run-on, is-it-a-complete-senten
ce-or-a-fragment, determine-the-meaning-of-idioms-from-context-set-2, read-poetry, identify-plurals-singular-possessives-and-plural-possessives, determine-the-meanings-of-words-with-greek-and-latin-ro
ots, formatting-and-capitalizing-titles, use-the-correct-frequently-confused-word, describe-the-difference-between-related-words, analogies, words-with-able-and-ible, words-with-mis, determine-the-mea
nings-of-greek-and-latin-roots, is-the-sentence-in-the-past-present-or-future-tense, words-with-un-dis-in-im-and-non, determine-the-meaning-of-idioms-from-context-set-1, which-definition-matches-the-s
entence, identify-story-elements, capitalizing-titles, distinguish-facts-from-opinions, use-the-correct-homophone, what-does-the-modal-verb-show, interpret-the-meaning-of-an-allusion-from-its-source,
choose-between-the-past-tense-and-past-participle, positive-and-negative-connotation, punctuating-dialogue, words-with-less, show-character-emotions-and-traits, revise-the-sentence-using-a-stronger-ve
rb, is-the-sentence-simple-compound-or-complex, use-the-correct-modal-verb, identify-elements-of-poetry, use-the-perfect-verb-tenses, which-sentence-is-more-formal, use-adjectives-to-compare, use-the-
correct-pair-of-correlative-conjunctions, use-actions-and-dialogue-to-understand-characters, is-the-sentence-simple-or-compound, read-about-history
grade-6
is-the-sentence-declarative-interrogative-imperative-or-exclamatory, identify-counterclaims, use-the-correct-homophone, use-the-correct-pair-of-correlative-conjunctions, use-guide-words, is-it-a-compl
ete-sentence-a-fragment-or-a-run-on, use-words-as-clues-to-the-meanings-of-greek-and-latin-roots, is-the-word-an-adjective-or-adverb, suggest-appropriate-revisions, analyze-passages-from-the-lightning
-thief-part-1, identify-plurals-singular-possessives-and-plural-possessives, use-the-correct-frequently-confused-word, choose-evidence-to-support-a-claim, vocabulary-review-trace-an-argument, use-the-
correct-verb-with-compound-subjects, which-definition-matches-the-sentence, use-coordinating-conjunctions, analogies-challenge, distinguish-facts-from-opinions, analyze-the-effects-of-figures-of-speec
h-on-meaning-and-tone, use-context-to-identify-the-meaning-of-a-word, use-the-correct-modal-verb, choose-between-subject-and-object-pronouns, determine-the-authors-point-of-view, determine-the-meaning
s-of-greek-and-latin-roots, what-does-the-modal-verb-show, use-greek-and-latin-roots-as-clues-to-the-meanings-of-words, analyze-passages-from-the-lightning-thief-part-2, is-the-pronoun-reflexive-or-in
tensive, draw-inferences-from-literary-texts, which-sentence-is-more-formal, compound-subjects-and-objects-with-pronouns, analyze-passages-from-harriet-tubman-conductor-on-the-underground-railroad-par
t-1, what-does-the-punctuation-suggest, is-it-a-complete-sentence-or-a-fragment, analogies, is-the-sentence-simple-compound-or-complex, determine-the-meaning-of-idioms-from-context-set-2, analyze-pass
ages-from-roll-of-thunder-hear-my-cry-part-1, classify-figures-of-speech, use-the-correct-subject-or-verb, use-the-perfect-verb-tenses, transitions-with-conjunctive-adverbs, evaluate-newspaper-headlin
es-for-bias, determine-the-main-idea-of-a-passage, use-personification, analyze-passages-from-harriet-tubman-conductor-on-the-underground-railroad-part-2, determine-the-meaning-of-idioms-from-context-
set-1, identify-text-structures, analyze-short-stories, is-it-a-complete-sentence-or-a-run-on, analyze-passages-from-roll-of-thunder-hear-my-cry-part-2, determine-the-meanings-of-words-with-greek-and-
latin-roots, trace-an-argument, identify-the-authors-purpose, classify-logical-fallacies, compare-two-texts-with-different-genres, describe-the-difference-between-related-words, choose-between-adjecti
ves-and-adverbs, interpret-figures-of-speech, identify-vague-pronoun-references, is-it-a-direct-object-or-an-indirect-object, use-the-progressive-verb-tenses, choose-between-the-past-tense-and-past-pa
rticiple, use-the-meanings-of-words-as-clues-to-the-meanings-of-greek-and-latin-roots, which-sentence-matches-the-definition
Table 12: Full language arts skill summary (part 1).

--- Page 24 ---

Grade
Skills of Language Arts
grade-7
analyze-passages-from-anne-frank-the-diary-of-a-young-girl-part-2, which-sentence-matches-the-definition, is-it-a-complete-sentence-or-a-run-on, choose-the-synonym, determine-the-meanings-of-words-wit
h-greek-and-latin-roots, is-it-a-phrase-or-a-clause, identify-plagiarism, analyze-passages-from-anne-of-green-gables-part-1, interpret-the-meaning-of-an-allusion-from-its-source, is-it-a-complete-sent
ence-a-fragment-or-a-run-on, are-the-modifiers-used-correctly, transitions-with-conjunctive-adverbs, use-context-to-identify-the-meaning-of-a-word, use-greek-and-latin-roots-as-clues-to-the-meanings-o
f-words, determine-the-authors-point-of-view, is-it-a-complete-sentence-or-a-fragment, is-the-pronoun-reflexive-or-intensive, use-words-as-clues-to-the-meanings-of-greek-and-latin-roots, analogies, wh
ich-sentence-is-more-formal, use-parallel-structure, what-does-the-punctuation-suggest, use-personification, recall-the-source-of-an-allusion, determine-the-main-idea-of-a-passage, use-the-correct-fre
quently-confused-word, analyze-passages-from-a-night-to-remember-part-1, is-the-word-an-adjective-or-adverb, classify-figures-of-speech, compound-subjects-and-objects-with-pronouns, analogies-challeng
e, analyze-passages-from-a-night-to-remember-part-2, choose-evidence-to-support-a-claim, analyze-passages-from-anne-of-green-gables-part-2, which-definition-matches-the-sentence, is-the-sentence-decla
rative-interrogative-imperative-or-exclamatory, analyze-passages-from-a-long-walk-to-water-part-2, analyze-passages-from-a-long-walk-to-water-part-1, analyze-passages-from-anne-frank-the-diary-of-a-yo
ung-girl-part-1, use-the-correct-pair-of-correlative-conjunctions, describe-the-difference-between-related-words, classify-logical-fallacies, use-guide-words, is-the-sentence-simple-compound-complex-o
r-compound-complex, determine-the-themes-of-short-stories, choose-between-adjectives-and-adverbs, determine-the-meanings-of-greek-and-latin-roots, use-the-correct-homophone, suggest-appropriate-revisi
ons, draw-inferences-from-literary-texts, identify-vague-pronoun-references, identify-plurals-singular-possessives-and-plural-possessives, choose-between-subject-and-object-pronouns, decide-whether-el
lipses-are-used-appropriately, identify-text-structures, distinguish-facts-from-opinions, vocabulary-review-trace-an-argument, use-the-correct-verb-with-compound-subjects, interpret-figures-of-speech,
identify-the-authors-purpose, choose-the-antonym
grade-8
use-the-correct-verb-with-compound-subjects, is-the-pronoun-reflexive-or-intensive, decide-whether-ellipses-are-used-appropriately, use-context-to-identify-the-meaning-of-a-word, determine-the-meaning
s-of-greek-and-latin-roots, choose-the-synonym, recall-the-source-of-an-allusion, analyze-the-effects-of-figures-of-speech-on-meaning-and-tone, compare-two-texts-with-different-genres, interpret-the-m
eaning-of-an-allusion-from-its-source, analyze-short-stories, positive-and-negative-connotation, identify-the-authors-purpose, analyze-passages-from-narrative-of-the-life-of-frederick-douglass-part-2,
analogies-challenge, is-the-sentence-simple-compound-complex-or-compound-complex, describe-the-difference-between-related-words, is-it-a-complete-sentence-or-a-fragment, use-the-correct-pair-of-corre
lative-conjunctions, use-the-correct-homophone, use-words-as-clues-to-the-meanings-of-greek-and-latin-roots, is-it-a-complete-sentence-a-fragment-or-a-run-on, is-it-a-phrase-or-a-clause, is-it-a-compl
ete-sentence-or-a-run-on, determine-the-themes-of-short-stories, choose-between-subject-and-object-pronouns, choose-evidence-to-support-a-claim, identify-thesis-statements, analogies, use-greek-and-la
tin-roots-as-clues-to-the-meanings-of-words, identify-plagiarism, is-the-sentence-declarative-interrogative-imperative-or-exclamatory, analyze-passages-from-the-giver-part-1, analyze-passages-from-the
-giver-part-2, determine-the-meanings-of-words-with-greek-and-latin-roots, use-parallel-structure, compound-subjects-and-objects-with-pronouns, is-it-a-direct-object-or-an-indirect-object, use-thesaur
us-entries, use-personification, identify-the-narrative-point-of-view, use-the-correct-frequently-confused-word, identify-text-structures, distinguish-facts-from-opinions, identify-plurals-singular-po
ssessives-and-plural-possessives, identify-the-verb-mood, choose-between-adjectives-and-adverbs, read-and-understand-informational-passages, determine-the-main-idea-of-a-passage, identify-counterclaim
s, interpret-figures-of-speech, identify-vague-pronoun-references, suggest-appropriate-revisions, use-guide-words, transitions-with-conjunctive-adverbs, is-the-word-an-adjective-or-adverb, which-sente
nce-is-more-formal, which-definition-matches-the-sentence, choose-between-personal-and-reflexive-pronouns, vocabulary-review-trace-an-argument, classify-logical-fallacies, analyze-passages-from-the-ou
tsiders-part-2, what-does-the-punctuation-suggest, which-sentence-matches-the-definition, trace-an-argument, choose-the-antonym, classify-figures-of-speech, identify-active-and-passive-voice, analyze-
passages-from-the-outsiders-part-1, determine-the-authors-point-of-view, are-the-modifiers-used-correctly, analyze-passages-from-narrative-of-the-life-of-frederick-douglass-part-1
grade-9
trace-an-argument-set-1, choose-the-word-whose-connotation-and-denotation-best-match-the-sentence, interpret-the-meaning-of-an-allusion-from-its-source, choose-the-best-evidence-to-support-a-claim, de
termine-the-main-idea-of-a-passage, identify-elements-of-poetry, classify-figures-of-speech-euphemism-hyperbole-oxymoron-paradox, recall-the-source-of-an-allusion, use-parallel-structure, transitions-
with-conjunctive-adverbs, use-words-accurately-and-precisely, analyze-the-development-of-informational-passages-set-1, is-the-sentence-declarative-interrogative-imperative-or-exclamatory, evaluate-cou
nterclaims, is-it-a-phrase-or-a-clause, words-with-pre, avoid-double-illogical-and-unclear-comparisons, decide-whether-ellipses-are-used-appropriately, identify-plagiarism, identify-the-verb-mood, ide
ntify-sentence-fragments, is-the-sentence-simple-compound-complex-or-compound-complex, analyze-the-development-of-informational-passages-set-2, choose-the-analysis-that-logically-connects-the-evidence
-to-the-claim, choose-the-topic-sentence-that-best-captures-the-main-idea, use-thesaurus-entries, use-dictionary-entries-to-determine-correct-usage, explore-words-with-new-or-contested-usages, identif
y-run-on-sentences, analyze-short-stories-set-1, identify-the-narrative-point-of-view, words-with-re, identify-vague-pronoun-references, determine-the-meanings-of-words-with-greek-and-latin-roots, cla
ssify-logical-fallacies, what-does-the-punctuation-suggest, choose-between-adjectives-and-adverbs, interpret-figures-of-speech, use-etymologies-to-determine-the-meanings-of-words, analyze-the-effects-
of-figures-of-speech-on-meaning-and-tone, use-appeals-to-ethos-pathos-and-logos-in-persuasive-writing, transition-logically-between-claims-evidence-analysis-and-counterclaims, identify-active-and-pass
ive-voice, which-text-is-most-formal, are-the-modifiers-used-correctly, distinguish-facts-from-opinions, classify-figures-of-speech-review, suggest-appropriate-revisions, analogies-challenge, trace-an
-argument-set-2, analyze-short-stories-set-2, use-the-correct-foreign-expression, identify-thesis-statements, choose-punctuation-to-avoid-fragments-and-run-ons, use-the-correct-frequently-confused-wor
d, words-with-less, use-greek-and-latin-roots-as-clues-to-the-meanings-of-words, use-the-correct-pair-of-correlative-conjunctions, use-words-as-clues-to-the-meanings-of-greek-and-latin-roots, identify
-audience-and-purpose, analogies, use-context-to-identify-the-meaning-of-a-word, words-with-mis, use-context-as-a-clue-to-the-meanings-of-foreign-expressions, determine-the-meanings-of-greek-and-latin
-roots
grade-10
choose-the-word-whose-connotation-and-denotation-best-match-the-sentence, use-greek-and-latin-roots-as-clues-to-the-meanings-of-words, choose-the-analysis-that-logically-connects-the-evidence-to-the-c
laim, transition-logically-between-claims-evidence-analysis-and-counterclaims, use-dictionary-entries-to-determine-correct-usage, use-thesaurus-entries, determine-the-meanings-of-words-with-greek-and-
latin-roots, use-the-correct-pair-of-correlative-conjunctions, identify-thesis-statements, is-the-sentence-declarative-interrogative-imperative-or-exclamatory, use-words-as-clues-to-the-meanings-of-gr
eek-and-latin-roots, identify-active-and-passive-voice, choose-between-adjectives-and-adverbs, identify-run-on-sentences, is-the-sentence-simple-compound-complex-or-compound-complex, suggest-appropria
te-revisions, identify-vague-pronoun-references, decide-whether-ellipses-are-used-appropriately, use-parallel-structure, choose-the-topic-sentence-that-best-captures-the-main-idea, recall-the-source-o
f-an-allusion, analogies, choose-the-best-evidence-to-support-a-claim, determine-the-main-idea-of-a-passage, classify-logical-fallacies, use-etymologies-to-determine-the-meanings-of-words, which-text-
is-most-formal, identify-plagiarism, use-the-correct-frequently-confused-word, interpret-figures-of-speech, analyze-the-effects-of-figures-of-speech-on-meaning-and-tone, use-context-to-identify-the-me
aning-of-a-word, use-the-correct-foreign-expression, choose-punctuation-to-avoid-fragments-and-run-ons, identify-sentence-fragments, determine-the-meanings-of-greek-and-latin-roots, explore-words-with
-new-or-contested-usages, interpret-the-meaning-of-an-allusion-from-its-source, what-does-the-punctuation-suggest, classify-figures-of-speech-euphemism-hyperbole-oxymoron-paradox, is-it-a-phrase-or-a-
clause, analogies-challenge, avoid-double-illogical-and-unclear-comparisons, transitions-with-conjunctive-adverbs, use-words-accurately-and-precisely, classify-figures-of-speech-review, identify-audie
nce-and-purpose, are-the-modifiers-used-correctly, use-context-as-a-clue-to-the-meanings-of-foreign-expressions, use-appeals-to-ethos-pathos-and-logos-in-persuasive-writing
grade-11
decide-whether-ellipses-are-used-appropriately, explore-words-with-new-or-contested-usages, identify-sentence-fragments, use-context-as-a-clue-to-the-meanings-of-foreign-expressions, use-the-correct-f
oreign-expression, use-words-as-clues-to-the-meanings-of-greek-and-latin-roots, analyze-the-effects-of-figures-of-speech-on-meaning-and-tone, which-text-is-most-formal, use-words-accurately-and-precis
ely, analogies, are-the-modifiers-used-correctly, describe-the-difference-between-related-words, determine-the-meanings-of-words-with-greek-and-latin-roots, choose-the-best-evidence-to-support-a-claim
, prefixes, what-does-the-punctuation-suggest, is-it-a-phrase-or-a-clause, use-greek-and-latin-roots-as-clues-to-the-meanings-of-words, determine-the-meanings-of-greek-and-latin-roots, classify-logica
l-fallacies, choose-punctuation-to-avoid-fragments-and-run-ons, classify-the-figure-of-speech-anaphora-antithesis-apostrophe-assonance-chiasmus-understatement, analyze-the-development-of-informational
-passages-set-2, choose-the-analysis-that-logically-connects-the-evidence-to-the-claim, use-the-correct-frequently-confused-word, analogies-challenge, recall-the-source-of-an-allusion, analyze-short-s
tories-set-1, identify-run-on-sentences, identify-audience-and-purpose, identify-vague-pronoun-references, trace-an-argument-set-1, interpret-the-figure-of-speech, avoid-double-illogical-and-unclear-c
omparisons, transition-logically-between-claims-evidence-analysis-and-counterclaims, domain-specific-vocabulary-in-context-science-and-technical-subjects, choose-between-adjectives-and-adverbs, choose
-the-word-whose-connotation-and-denotation-best-match-the-sentence, determine-the-main-idea-of-a-passage, interpret-the-meaning-of-an-allusion-from-its-source, use-parallel-structure, use-appeals-to-e
thos-pathos-and-logos-in-persuasive-writing, trace-an-argument-set-2, suffixes, use-etymologies-to-determine-the-meanings-of-words, use-dictionary-entries-to-determine-correct-usage, evaluate-counterc
laims, transitions-with-conjunctive-adverbs, suggest-appropriate-revisions, analyze-the-development-of-informational-passages-set-1, classify-the-figure-of-speech-euphemism-hyperbole-oxymoron-paradox,
classify-the-figure-of-speech-review, is-the-sentence-simple-compound-complex-or-compound-complex
grade-12
analogies, evaluate-counterclaims, what-does-the-punctuation-suggest, analyze-short-stories-set-2, is-the-sentence-simple-compound-complex-or-compound-complex, use-etymologies-to-determine-the-meaning
s-of-words, choose-the-analysis-that-logically-connects-the-evidence-to-the-claim, decide-whether-ellipses-are-used-appropriately, classify-the-figure-of-speech-anaphora-antithesis-apostrophe-assonanc
e-chiasmus-understatement, use-the-correct-frequently-confused-word, describe-the-difference-between-related-words, identify-vague-pronoun-references, recall-the-source-of-an-allusion, identify-senten
ce-fragments, identify-run-on-sentences, is-it-a-phrase-or-a-clause, choose-the-best-evidence-to-support-a-claim, analogies-challenge, suggest-appropriate-revisions, avoid-double-illogical-and-unclear
-comparisons, use-dictionary-entries-to-determine-correct-usage, explore-words-with-new-or-contested-usages, choose-the-word-whose-connotation-and-denotation-best-match-the-sentence, choose-between-ad
jectives-and-adverbs, choose-punctuation-to-avoid-fragments-and-run-ons, use-words-accurately-and-precisely, which-text-is-most-formal, use-appeals-to-ethos-pathos-and-logos-in-persuasive-writing, ide
ntify-audience-and-purpose, interpret-the-meaning-of-an-allusion-from-its-source, analyze-the-development-of-informational-passages-set-1, use-greek-and-latin-roots-as-clues-to-the-meanings-of-words,
classify-the-figure-of-speech-euphemism-hyperbole-oxymoron-paradox, classify-the-figure-of-speech-review, transition-logically-between-claims-evidence-analysis-and-counterclaims, determine-the-meaning
s-of-words-with-greek-and-latin-roots, determine-the-meanings-of-greek-and-latin-roots, analyze-the-effects-of-figures-of-speech-on-meaning-and-tone, interpret-the-figure-of-speech, classify-logical-f
allacies, use-parallel-structure, are-the-modifiers-used-correctly, use-words-as-clues-to-the-meanings-of-greek-and-latin-roots, transitions-with-conjunctive-adverbs, use-context-as-a-clue-to-the-mean
ings-of-foreign-expressions
Table 13: Full language arts skill summary (part 2).

--- Page 25 ---

Subject: Social Studies
Skill: the-american-revolution-new-british-taxes
Description: In the 1760s, smuggling was an important part of the colonial economy. What
does smuggling mean?
Choices: [(a) stealing goods from foreign merchants, (b) trading one good for another
without the use of money, (c) shipping goods secretly or illegally, (d) producing metal from
minerals and rocks]
Answer index: 2
Subject: Social Studies
Skill: world-war-i-the-road-to-war
Description: What was World War I originally called?
Choices: [(a) the First War, (b) the Great War, (c) the European Revolution, (d) European
War I]
Answer index: 1
Subject: Social Studies
Skill: the-american-flag
Description: What does each star on the American flag stand for?
Choices: [(a) a president, (b) a state, (c) a war, (d) a city]
Answer index: 1
Subject: Social Studies
Skill: identify-facts-and-opinions
Description: Which sentence states a fact?
Choices: [(a) The Grand Canyon was carved by the Colorado River., (b) The Grand Canyon
is the most breathtaking place the United States.]
Answer index: 0
Subject: Social Studies
Skill: state-government
Description: How are representatives in a state legislature chosen?
Choices: [(a) Everyone in the state votes for all of the representatives., (b) Each district,
or area, gets to choose one or two representatives., (c) The governor chooses all of the
representatives., (d) The mayors of each city choose one or two representatives.]
Answer index: 1
Subject: Social Studies
Skill: the-empire-state-building
Description: Complete the sentence.
The Empire State Building was built during a tough time in American history. That time was
known as ___.
Choices: [(a) the Colonial Period, (b) the Gold Rush, (c) the Reconstruction Era, (d) the
Great Depression]
Answer index: 3
Subject: Social Studies
Skill: local-government
Description: Local governments serve which places?
Choices: [(a) countries, (b) towns, cities, and counties, (c) states]
Answer index: 1
Subject: Social Studies
Skill: the-american-revolution-the-rebellion-begins
Description: Complete the sentence.
At the First Continental Congress, the colonies agreed to ___ goods imported from Great
Britain.
Choices: [(a) stop buying, (b) buy more, (c) destroy, (d) tax]
Answer index: 0
Subject: Social Studies
Skill: the-lincoln-memorial
Description: Complete the sentence.
Architect Henry Bacon designed the Lincoln Memorial in the early 1900s. He got his ideas
from ___.
Choices: [(a) architect Frank Lloyd Wright, (b) Gothic churches in France, (c) ancient Greek
buildings, (d) President Warren G. Harding]
Answer index: 2
Subject: Social Studies
Skill: world-war-i-the-war-begins
Description: Complete the text.
There were two main sides in World War I. One side was called the ___ and the other was
called the ___.
Choices: [(a) Axis powers . . . Allied powers, (b) Allied powers . . . Central powers, (c)
Central powers . . . Axis powers, (d) Allied powers . . . Triple Entente]
Answer index: 1
Subject: Social Studies
Skill: world-war-i-the-road-to-peace
Description: Complete the text.
During the Paris Peace conference, one group of men was known as ___. They represented
the most powerful countries at the conference.
Choices: [(a) the Three Emperors’ League, (b) the Axis Leaders, (c) the Big Four, (d) the
enlightened despots]
Answer index: 2
Subject: Social Studies
Skill: the-statue-of-liberty
Description: The Statue of Liberty was finished in 1886. However, the builders’ goal had
been to finish in 1876. Why was 1876 important?
Choices: [(a) It was the year the Civil War ended., (b) It was the 100th anniversary of the
Declaration of Independence., (c) New York City hosted the Olympics that year., (d) The
president of France visited the United States for the first time that year.]
Answer index: 1
Subject: Social Studies
Skill: the-american-revolution-turning-the-tide-of-the-war
Description: The Continental Army suffered many losses in the autumn of 1776. Thomas
Paine, a popular writer, was traveling with the army. In late December, he wrote an essay.
Read the passage from Thomas Paine’s essay. Then answer the question below.
These are the times that try men’s souls. The summer soldier and the sunshine patriot will, in
this crisis, shrink from the service of their country; but he that stands by it now, deserves the
love and thanks of man and woman.
Which sentence best explains what he meant by these words?
Choices: [(a) He did not believe the Americans were doing the right thing., (b) General
Washington did not know how to lead an army., (c) The British soldiers were afraid of the
Americans., (d) The Continental Army was struggling, but it was fighting for a good cause.]
Answer index: 3
Subject: Social Studies
Skill: the-war-of-1812-causes
Description: The War of 1812 was between the United States and which other country?
Choices: [(a) France, (b) Canada, (c) Mexico, (d) Great Britain]
Answer index: 3
Subject: Social Studies
Skill: thanksgiving
Description: When is Thanksgiving celebrated in the United States?
Choices: [(a) on December 5, (b) on January 12, (c) on the second Sunday of September, (d)
on the fourth Thursday of November]
Answer index: 3
Subject: Social Studies
Skill: source-analysis-the-gettysburg-address
Description: The Gettysburg Address, one of the most famous documents in United States
history, was written in 1863. At that time, Abraham Lincoln was president of the United
States, and the Union and Confederate armies were fighting each other during the American
Civil War.
Read the following facts about the Gettysburg Address. Then complete the sentence below.
Gettysburg is a town in Pennsylvania where an important Civil War battle was fought.
One of the meanings of the word address is a public speech.
Based on the information above, complete the sentence.
When people say, "President Abraham Lincoln gave the Gettysburg Address," they mean that
President Lincoln ___.
Choices: [(a) lived at 1600 Pennsylvania Avenue, (b) wrote a book about an important Civil
War battle, (c) made a speech after an important Civil War battle, (d) is buried in a graveyard
in a town in Pennsylvania]
Answer index: 2
Subject: Social Studies
Skill: causes-of-the-american-revolution-the-french-and-indian-war
Description: Complete the text.
Before the French and Indian War, there were about 20 times as many British colonists as
French colonists. In the 1740s, both British and French colonists began to expand their
claims on land in the Ohio River Valley. Both countries were interested in the valuable fur
trade there, but ___ were more interested in settling the area.
Choices: [(a) The French, (b) the British]
Answer index: 1
Subject: Social Studies
Skill: the-civil-war-bull-run-to-the-emancipation-proclamation
Description: In July 1861, a Union army marched south from Washington, D.C., into
Virginia. Its goal was to seize Manassas Junction, an important railroad center. This plan led
to the First Battle of Bull Run, the first major battle of the war.
...
baffled:confused
Complete the sentence.
Based on Whitman’s account, the First Battle of Bull Run was a ___ for the Union army.
Choices: [(a) defeat, (b) victory, (c) draw]
Answer index: 0
Table 14: Question examples for each skill (part 1).

--- Page 26 ---

Subject: Social Studies
Skill: identify-primary-and-secondary-sources
Description: Imagine that you are a historian who wants to learn more about the fall of the
Roman Empire in the 400s CE. You find the source described below. Read the description of
the source. Then complete the sentence below.
The historian Edward Gibbon wrote the book The History of the Decline and Fall of the
Roman Empire in 1776 CE.
Complete the sentence.
In this case, the book is a ___ source because it ___.
Choices: [(a) primary . . . is a firsthand account of the fall of the Roman Empire, (b)
secondary . . . was written by a historian after the fall of the Roman Empire]
Answer index: 1
Subject: Social Studies
Skill: months-of-the-year
Description: What month comes right after February?
Choices: [(a) March, (b) December]
Answer index: 0
Subject: Social Studies
Skill: days-of-the-week
Description: What day comes right after Tuesday?
Choices: [(a) Saturday, (b) Friday, (c) Wednesday]
Answer index: 2
Subject: Social Studies
Skill: theodore-roosevelt
Description: Complete the sentence.
Theodore Roosevelt is best known as ___ from the early 1900s.
Choices: [(a) a president, (b) an artist, (c) a pilot, (d) an inventor]
Answer index: 0
Subject: Social Studies
Skill: george-washington-carver
Description: George Washington Carver came up with how many ways to use peanuts?
Choices: [(a) around 3, (b) around 30, (c) around 300, (d) around 3,000]
Answer index: 2
Subject: Social Studies
Skill: cesar-chavez
Description: What made Cesar Chavez famous?
Choices: [(a) He wrote many books about the Civil War., (b) He helped make life better
for farm workers., (c) He invented a new way to bring water to crops., (d) He worked for
women’s right to vote.]
Answer index: 1
Subject: Social Studies
Skill: john-deere
Description: Complete the sentence.
John Deere was a famous ___.
Choices: [(a) pilot, (b) soldier, (c) inventor, (d) writer]
Answer index: 2
Subject: Social Studies
Skill: pledge-of-allegiance
Description: A pledge is a promise. Listen to this part of the Pledge of Allegiance. Pick the
missing word.
I pledge ___ to the Flag of the United States of America . . .
Choices: [(a) allegiance, (b) honesty]
Answer index: 0
Subject: Social Studies
Skill: compare-urban-suburban-and-rural-areas
Description: In which place would you be more likely to drive to see your neighbors?
Choices: [(a) an urban area, (b) a rural area]
Answer index: 1
Subject: Social Studies
Skill: abraham-lincoln
Description: Complete the sentence.
Abraham Lincoln grew up in a poor family. He got most of his education by ___.
Choices: [(a) reading a lot of books, (b) taking college classes, (c) going to public school, (d)
listening to the radio]
Answer index: 0
Subject: Social Studies
Skill: the-civil-war-the-first-battle-of-bull-run-to-gettysburg
Description: In 1862, the Union army in Washington, D.C., tried to capture the Confederacy’s
capital of Richmond. Below is a letter from the Union army’s commander, General George
B. McClellan, to President Lincoln’s Secretary of War.
I have lost this battle because my force was too small. I have seen too many dead and
wounded comrades to feel otherwise than this government has not sustained this army. If you
do not do so now the game is lost. If I save this army now, I tell you plainly that I owe no
thanks to you or any other person in Washington. You have done the best to sacrifice this
army.
sustained: helped
Whom does McClellan blame for the Union army not capturing Richmond?
Choices: [(a) the Union soldiers, (b) himself, (c) the Confederate army, (d) the United States
government]
Answer index: 3
Subject: Social Studies
Skill: new-england-colonies-religion-and-government
Description: Complete the text.
The Puritans were different from the Pilgrims who moved to New England in 1620. The
Pilgrims wanted to ___ the Church of England, but the Puritans wanted to ___ it.
Choices: [(a) separate from . . . change, (b) change . . . separate from, (c) strengthen . . .
destroy, (d) join . . . leave]
Answer index: 0
Subject: Social Studies
Skill: the-washington-monument
Description: People started building the Washington Monument in 1848. It took 36 years to
build. In what year was the Washington Monument completed?
Choices: [(a) 1854, (b) 1884, (c) 1898, (d) 1936]
Answer index: 1
Subject: Social Studies
Skill: the-civil-war-the-beginning-of-the-war
Description: Following the Battle of Fort Sumter, President Lincoln called on loyal states to
provide troops. How did Virginia, North Carolina, Tennessee, and Arkansas react to this call?
Choices: [(a) These states refused to send troops to either side., (b) These states joined the
Confederacy., (c) These states demanded that the Confederate states surrender., (d) These
states sent troops to the Union army.]
Answer index: 1
Subject: Social Studies
Skill: antebellum-period-slavery-and-politics-part-i
Description: Complete the text.
By the 1820s, many Americans wanted to have an equal number of slave and free states.
They wanted a balance of states so that the ___ would have the same number of members
from each side.
Choices: [(a) Supreme Court, (b) Senate, (c) Executive Branch, (d) House of Representatives]
Answer index: 1
Subject: Social Studies
Skill: the-american-revolution-preparing-for-war
Description: To oppose something means to be against it. Which one of these people strongly
opposed American independence?
Choices: [(a) Thomas Paine, (b) John Adams, (c) King George III, (d) George Washington]
Answer index: 2
Subject: Social Studies
Skill: the-golden-gate-bridge
Description: Complete the sentence.
Leaders of the Golden Gate Bridge project made special rules to ___.
Choices: [(a) protect birds in the area, (b) keep ferry boats in business, (c) use more recycled
materials, (d) help keep workers safe]
Answer index: 3
Subject: Social Studies
Skill: identify-shortage-and-surplus
Description: There are 300 concert tickets for sale. Tickets cost $20 each. At that price, there
are 200 people who want to buy a ticket.
Is there a surplus or a shortage of tickets?
Choices: [(a) surplus, (b) shortage]
Answer index: 0
Subject: Social Studies
Skill: the-new-deal
Description: Which important period in American history began in 1929?
Choices: [(a) the Civil War, (b) the Great Depression, (c) World War II, (d) the civil rights
movement]
Answer index: 1
Subject: Social Studies
Skill: reconstruction
Description: In 1865, slavery was banned in the United States. How was it banned?
Choices: [(a) a presidential veto, (b) a Supreme Court decision, (c) an amendment to the
Constitution, (d) a national vote]
Answer index: 2
Subject: Social Studies
Skill: the-war-of-1812-events-and-effects
Description: Which country had a larger navy in 1812?
Choices: [(a) the United States, (b) Great Britain]
Answer index: 1
Subject: Social Studies
Skill: plymouth
Description: In 1620, some of the Separatists made an agreement with a business in England
called the Virginia Company. The Virginia Company would loan them money to buy supplies
and hire a ship. Why did the Separatists need supplies and a ship?
Choices: [(a) to create a new country in Europe, (b) to find a trade route between Europe and
Asia, (c) to build a new cathedral for the Church of England, (d) to start their own colony in
North America]
Answer index: 3
Table 15: Question examples for each skill (part 2).

--- Page 27 ---

Subject: Social Studies
Skill: the-great-depression-part-i
Description: Who was the president of the United States at the start of the Great Depression?
Choices: [(a) William McKinley, (b) Herbert Hoover, (c) Harry Truman, (d) Gerald Ford]
Answer index: 1
Subject: Social Studies
Skill: the-american-revolution-struggle-for-independence
Description: At the Battle of Bunker Hill, one of the colonial officers gave the soldiers a
famous order. Read the order. Then answer the question below.
Don’t fire until you can see the whites of their eyes!
What was one reason the officer gave this order?
Choices: [(a) He did not want the soldiers to waste any gunpowder or ammunition., (b) He
wanted to make sure that the British soldiers were really going to attack., (c) He wanted to
make sure that the soldiers were actually British., (d) He did not want the British soldiers to
be surprised by the gunfire.]
Answer index: 0
Subject: Social Studies
Skill: federal-government
Description: Complete the sentence.
The three branches of government are the executive, legislative, and ___ branches.
Choices: [(a) federal, (b) defensive, (c) state, (d) judicial]
Answer index: 3
Subject: Social Studies
Skill: the-bill-of-rights
Description: Complete the sentences.
___According to the Tenth Amendment, the Constitution lists all of the powers given to the
United States government. Any power not listed in the Constitution belongs to either the
American people or
Choices: [(a) the state governments, (b) the king or queen of Great Britain, (c) private
businesses, (d) the Canadian government]
Answer index: 0
Subject: Social Studies
Skill: the-louisiana-purchase
Description: In what year did the Louisiana Purchase take place?
Choices: [(a) 1792, (b) 1798, (c) 1803, (d) 1815]
Answer index: 2
Subject: Social Studies
Skill: the-lewis-and-clark-expedition
Description: Why did Thomas Jefferson and others want to find the Northwest Passage?
Choices: [(a) It would make traveling less dangerous., (b) It would help lost explorers find
their way home., (c) It would make trade with Asia easier.]
Answer index: 2
Subject: Social Studies
Skill: the-white-house
Description: Complete the sentence.
The White House is the home of ___.
Choices: [(a) the president of the United States, (b) the governor of Maryland, (c) George
Washington’s great-great-grandson, (d) the Speaker of the House of Representatives]
Answer index: 0
Subject: Social Studies
Skill: the-american-revolution-conclusion-and-aftermath
Description: Complete the sentence.
In 1779, ___ joined the Revolutionary War on the side of the United States.
Choices: [(a) Spain, (b) Canada, (c) Mexico, (d) Prussia]
Answer index: 0
Subject: Social Studies
Skill: the-american-revolution-the-boston-tea-party
Description: In 1770, colonists who wanted independence still had a hard time getting the
colonies to work together. What made working together so difficult?
Choices: [(a) The colonists were divided into two groups over the issue of slavery., (b)
People living in different colonies often spoke different languages., (c) British soldiers would
break up any large meetings of colonists., (d) The colonists were not well organized. They
had no easy way to share information.]
Answer index: 3
Subject: Social Studies
Skill: the-constitution
Description: When was the Constitution written?
Choices: [(a) 1787, (b) 1867, (c) 1907, (d) 2007]
Answer index: 0
Subject: Social Studies
Skill: the-civil-war-war-tactics-and-the-home-front
Description: Complete the sentence.
During the Civil War, the Union navy tried to close off Southern ports. The Union wanted to
stop the Confederacy from trading with other countries. In other words, the Union wanted to
create ___.
Choices: [(a) an ambush, (b) a blockade, (c) an armistice, (d) an assault]
Answer index: 1
Subject: Social Studies
Skill: the-great-depression-part-ii
Description: Where were the effects of the Great Depression felt?
Choices: [(a) The Great Depression affected countries around the world., (b) The Great
Depression only affected the United States., (c) The Great Depression’s impact was limited
to North American countries., (d) The Great Depression was felt only in the Western
Hemisphere.]
Answer index: 0
Subject: Social Studies
Skill: the-american-revolution-the-thirteen-colonies-under-british-rule
Description: How did Great Britain rule the Thirteen Colonies from so far away?
Choices: [(a) Great Britain created a second national capital in the Thirteen Colonies., (b)
Each colony elected leaders to visit the British government once a year., (c) Each colony had
its own government, and those governments had to follow British law., (d) The king of Great
Britain traveled to the Thirteen Colonies once a month.]
Answer index: 2
Subject: Social Studies
Skill: world-war-i-events-of-the-war
Description: Read the passage. Then answer the question.
The main type of fighting in World War I was trench warfare. Soldiers dug trenches, or deep
holes in the ground, to protect themselves from enemy fire.
...
Soldiers stayed in the trenches for weeks at a time. The trenches were dirty and uncomfort-
able. Many soldiers got sick in the trenches.
Why were trenches used during World War I?
Choices: [(a) Trenches helped to end the war quickly., (b) Trenches protected soldiers from
enemy weapons., (c) Trenches were clean places for soldiers to stay before returning to fight.,
(d) Trenches made "no man’s land" a safer place to be.]
Answer index: 1
Subject: Social Studies
Skill: antebellum-period-abolitionist-and-proslavery-perspectives
Description: By 1860, there were almost four million enslaved African American people in
the United States. What is an enslaved person?
Choices: [(a) a person who is drafted into the army, (b) a person who is owned by someone
else, (c) a person who works for someone else for 4 to 7 years, (d) a person who is a criminal]
Answer index: 1
Subject: Social Studies
Skill: new-england-colonies-economy-and-conflict
Description: Slavery was not as widespread in New England as it was in the Southern
Colonies. Why not?
Choices: [(a) The colonists in New England had nothing valuable to trade for enslaved
people., (b) The Puritans believed slavery was morally wrong. Most towns made slavery
illegal., (c) New England did not have many large plantations, where enslaved labor was
most valuable.]
Answer index: 2
Subject: Social Studies
Skill: jamestown-the-early-years
Description: Read the passage about the men who traveled to Jamestown. Then answer the
question below.
Around 100 men signed up to travel to Jamestown. Here are some of the men who signed up:
...
However, around 50 of the men who signed up to go to weren’t workers at all! They were
gentlemen. A gentleman is a man born into a noble family. Often, gentlemen are rich. They
are rarely asked to do any work. Many gentlemen wanted to travel to Jamestown to find
adventure.
Half of the first Jamestown settlers were gentlemen. Why might that have been a problem?
Choices: [(a) Gentlemen wanted to avoid adventures in the new colony., (b) Gentlemen did
not have enough money to help start a new colony., (c) Gentlemen were not used to the hard
work of starting a colony.]
Answer index: 2
Subject: Social Studies
Skill: middle-colonies-founding-and-government
Description: John Berkeley and Sir George Carteret wanted to make money by charging fees
for land in New Jersey. But to do this, they needed to attract Europeans to settle the land.
Which of these rules would probably make Europeans more likely to move to New Jersey?
Choices: [(a) All settlers would have to work for seven years before they could get any land.,
(b) All settlers would have to pay taxes to the colonial government., (c) All settlers would be
free to practice the religion of their choice.]
Answer index: 2
Table 16: Question examples for each skill (part 3).

--- Page 28 ---

Subject: Social Studies
Skill: antebellum-period-slavery-and-politics-part-ii
Description: While in prison in December 1859, John Brown handed a note to his guard.
Use the text from that note to answer the question below.
I, John Brown, am now quite certain that the crimes of this guilty land will never be purged
away; but with blood.
purged:removed
What did Brown believe would be needed to end slavery?
Choices: [(a) economic boycott, (b) petitions, (c) non-violent protest, (d) violence]
Answer index: 3
Subject: Social Studies
Skill: southern-colonies-economy-and-slavery
Description: Complete the sentence.
The largest farms in the Southern Colonies grew cash crops. Cash crops are plants meant
___.
Choices: [(a) to be sold, (b) to be given to the government, (c) to feed wildlife, (d) to be
eaten by farmers]
Answer index: 0
Subject: Social Studies
Skill: presidential-elections
Description: Complete the sentence.
In an election, people choose their representatives and leaders by ___.
Choices: [(a) voting, (b) giving speeches, (c) drawing names randomly, (d) passing laws]
Answer index: 0
Subject: Social Studies
Skill: the-civil-war-the-end-of-the-war
Description: In 1864, the United States held a presidential election.
Lincoln ran for
re-election. A couple months before the election, Lincoln wrote the following note to his
advisors. Use it to answer the question below.
This morning, as for some days past, it seems exceedingly probable that this Administration
will not be re-elected. Then it will be my duty to so cooperate with the President elect, as
to save the Union between the election and the inauguration; as he will have secured his
election on such ground that he can not possibly save it afterwards.
...
inauguration:when a president takes office
What did Abraham Lincoln think would happen if he lost the election?
Choices: [(a) The election would bring the country back together., (b) The new president
would not be able to save the Union., (c) The new president would ask Lincoln to be vice
president.]
Answer index: 1
Subject: Social Studies
Skill: mount-rushmore
Description: When did workers start carving Mount Rushmore?
Choices: [(a) in 1863, (b) in 1888, (c) in 1901, (d) in 1927]
Answer index: 3
Subject: Social Studies
Skill: understand-overall-supply-and-demand
Description: Eli Whitney invented the cotton gin in 1793. The cotton gin is a machine that
makes it easier to harvest cotton quickly. What happened to the overall supply of cotton after
1793?
Choices: [(a) The supply went up., (b) The supply went down.]
Answer index: 0
Subject: Social Studies
Skill: costs-and-benefits
Description: Samuel is deciding whether to bake banana muffins or lemon muffins. He wants
the muffins to be tasty. But he also wants to make a lot of muffins.
Suppose Samuel decides to bake lemon muffins. Which result would be a cost?
Choices: [(a) Samuel will get to eat more muffins. He can make more lemon muffins than
banana muffins., (b) Samuel will give up the chance to eat banana muffins. He thinks banana
muffins are tastier than lemon muffins.]
Answer index: 1
Subject: Social Studies
Skill: antebellum-period-economies-of-the-north-and-south
Description: In the United States, most enslaved people worked on large farms that grew
crops to sell. What were these farms called?
Choices: [(a) subsistence farms, (b) workshops, (c) factories, (d) plantations]
Answer index: 3
Subject: Social Studies
Skill: jamestown-growth-of-a-colony
Description: In 1613, a Jamestown settler kidnapped Chief Powhatan’s favorite daughter.
What was she called?
Choices: [(a) Pocahontas, (b) Massasoit, (c) Squanto, (d) Sacagawea]
Answer index: 0
Subject: Social Studies
Skill: world-war-ii-lead-up-to-war-in-europe-asia
Description: After the Treaty of Versailles was signed, a German newspaper stated the
following. Read the passage. Then answer the question.
Today German honor is being carried to its grave. Do not forget it! The German people will,
with unceasing labor, press forward to reconquer the place among the nations to which it is
entitled. Then will come vengeance for the shame of 1919.
...
vengeance:payback
According to the passage, what does the author want Germany to do in the future?
Choices: [(a) The author wants Germany to join the Allied powers., (b) The author wants
Germany to become a powerful nation again., (c) The author wants Germany to forget about
World War I., (d) The author wants Germany to join the League of Nations.]
Answer index: 1
Subject: Social Studies
Skill: southern-colonies-founding-and-government
Description: Many Virginians did not like the colonial government’s friendly policies toward
Native Americans. In 1676, these Virginians violently rebelled against the government in
Virginia. This event became known as Bacon’s Rebellion.
Which of the following is an example of a violent rebellion?
Choices: [(a) writing letters to the colonial governor of Virginia and the king, (b) voting
in the next election for the Virginian colonial representatives, (c) marching on the colonial
capital of Jamestown and burning it down]
Answer index: 2
Subject: Social Studies
Skill: middle-colonies-economy-and-society
Description: Merchants played a key role in trade between colonies and between the colonies
and Europe.
Which of these things would a merchant be likely to do?
Choices: [(a) use lumber from the Middle Colonies to build houses, (b) grow cash crops such
as corn and wheat, (c) sell corn from the Middle Colonies to people in England, (d) make
iron products such as plows and horseshoes]
Answer index: 2
Subject: Social Studies
Skill: world-war-ii-global-events
Description: Kathryn Mary Doody was a nurse at an army hospital in Hawaii when Pearl
Harbor was bombed. Read Kathryn Mary Doody’s account of the events of December 7,
1941. Then answer the question.
Pretty soon the night nurse came off duty, and she said to us, "Girls, you know what’s
happening?" And we said, "No, what’s happening?" She said, "The island of Oahu has been
attacked by the enemy, Japan." And I said, "Shut up." Because she was a person that always
had the greatest stories to relate. And she said, "Don’t pay any attention to me. Go turn your
radios on." So I went in the room and turned the radio on and that’s exactly what they were
repeating, over and over again.. . .So I thought, "That means war. What’s war going to be
like?"
According to the passage, what was Kathryn Mary Doody’s reaction when she first heard
about the attack on Pearl Harbor?
Choices: [(a) She was scared and went to church to pray for peace., (b) She didn’t believe
that it was true., (c) She told all of her friends that they should help the military., (d) She was
angry at the United States government.]
Answer index: 1
Subject: Social Studies
Skill: early-mesopotamia
Description: Complete the text.
Mesopotamia is an area between the ___ Rivers. Because of the rich soil created by the two
rivers, Mesopotamia is often called the Fertile Crescent.
Choices: [(a) Indus and Ganges, (b) Mississippi and Missouri, (c) Tigris and Euphrates, (d)
Nile and Jordan]
Answer index: 2
Table 17: Question examples for each skill (part 4).

--- Page 29 ---

Subject: Social Studies
Skill: ancient-china
Description: For people in ancient Chinese communities, flooding around the Yellow and
Yangtze Rivers was a common problem.
But floods had both positive and negative effects for people in ancient China. Which of the
following was a positive effect of flooding?
Choices: [(a) Floods killed many animals who lived near the river., (b) After a river flooded,
fertile soil was left on the land., (c) Many crops were destroyed by the floods., (d) Floods
destroyed homes located near the river.]
Answer index: 1
Subject: Social Studies
Skill: origins-of-islam
Description: Muslims believe there is only one god. They call this god Allah, which means
"God" in Arabic. The following passage describes a Muslim belief about how Allah revealed,
or communicated, messages to his followers. Read the passage. Then answer the question
below.
We believe in Allah and [the message that] was revealed to us and what was revealed to
Abraham . . . and the teachings which Allah gave to Moses and Jesus and to other prophets.
...
Al Imran 3:84 in Zafar Ishaq Ansari, translator, Towards Understanding the Qur’an, Volume
1. Copyright 1988 by The Islamic Foundation.
Based on this passage, which statement do most Muslims believe is true?
Choices: [(a) Allah is more powerful than the god Jews and Christians worship., (b) Allah is
the same god that Jews and Christians worship., (c) Allah sent messages to Abraham, but not
to other prophets.]
Answer index: 1
Subject: Social Studies
Skill: the-teachings-of-confucius
Description: Confucius’s teachings have been passed down in a text known as The Analects
(AN-el-ekts). Read the passage about The Analects. Then answer the question below.
The Analects is made up of discussions between Confucius and his students.
When
Confucius was alive, his students all remembered their own conversations with Confucius.
When Confucius died, his students gathered together to write down their memories of
Confucius’s teachings. The text they wrote down was called The Analects, which means "the
selected speeches."
Complete the text.
collected and wrote down The Analects. The Analects is made up of ___.
Choices: [(a) Confucius . . . books Confucius wrote, (b) Confucius . . . conversations
Confucius had with his students, (c) Confucius’s students . . . books Confucius wrote, (d)
Confucius’s students . . . conversations Confucius had with his students]
Answer index: 3
Subject: Social Studies
Skill: ancient-egypt-the-old-kingdom
Description: Complete the text.
Before Upper and Lower Egypt became one kingdom, they were divided into nomes, or ___.
Each nome was controlled by a nomarch, or local king.
Choices: [(a) territories, (b) farms, (c) churches, (d) teams]
Answer index: 0
Subject: Social Studies
Skill: the-mauryan-empire
Description: One of Chandragupta’s most important military and political advisors was a
man named Kautilya. Read the following story about Kautilya and Chandragupta. Then
answer the question below.
Kautilya and Chandragupta gathered an army to overthrow the Nanda Empire. At first, their
soldiers attacked the center of the Nanda Empire, but they were defeated by the powerful
Nanda army.
...
According to tradition, Kautilya and Chandragupta took that mother’s advice about eating
hot bread and used it to defeat the Nanda Empire.
How did Kautilya and Chandragupta use the mother’s advice to defeat the Nanda Empire?
Choices: [(a) They convinced members of the Nanda army to change sides and help
Chandragupta overthrow the empire., (b) They attacked the Nanda Empire from the edges,
where it was weakest, rather than from the center where it was strong., (c) They attacked the
center of the Nanda Empire until the army was too tired and weak to keep fighting.]
Answer index: 1
Subject: Social Studies
Skill: origins-of-christianity
Description: Complete the text.
Jesus of Nazareth is the most important figure in Christianity. Most Christians believe he ___.
Choices: [(a) is God, (b) built a temple in Jerusalem, (c) was a famous military leader, (d)
was a Roman emperor]
Answer index: 0
Subject: Social Studies
Skill: ancient-egyptian-religion
Description: In ancient Egypt, powerful gods were an important part of religious beliefs.
People who believe in many gods are called polytheists (pol-ee-THEE-ists).
Which statement would support the idea that ancient Egyptians were polytheists?
Choices: [(a) Many ancient Egyptians worshipped the gods Osiris, Isis, and Horus., (b)
Ancient Egyptian religious traditions lasted over 3,000 years., (c) Many different creation
stories were popular in ancient Egypt., (d) Ancient Egypt was located in northeastern Africa,
along the Nile River.]
Answer index: 0
Subject: Social Studies
Skill: the-gupta-empire
Description: The Gupta Empire was founded by a man who became known as Chandra
Gupta (CHUN-druh GOOP-tuh). Read about Chandra Gupta. Then complete the sentence
below.
Chandra Gupta was born to a ruling family, but they only controlled a small area and were
not very powerful. That began to change around 320 CE when Chandra Gupta married
Princess Kumaradevi.
Princess Kumaradevi came from a powerful family that controlled an area along the Ganges
River. By marrying Kumaradevi, Chandra Gupta expanded the area he controlled, and he
began forming an empire.
Complete the following sentence.
Chandra Gupta began the Gupta Empire after he ___.
Choices: [(a) threatened to stop trading with regions that refused to let him rule, (b) inherited
the large region his family had controlled for generations, (c) married a princess and took
control of the area her family ruled, (d) won battles against many kingdoms along the Ganges
River]
Answer index: 2
Subject: Social Studies
Skill: origins-of-judaism
Description: Judaism (JU-dee-izm) is a religion that has existed for thousands of years. What
are people who practice Judaism called?
Choices: [(a) Christians, (b) Jains, (c) Jews, (d) Hindus]
Answer index: 2
Subject: Social Studies
Skill: the-ancient-silk-road-goods-and-ideas
Description: People in the Han Dynasty produced silk, an important luxury good. Han
people used silk for money and clothing within Han territory, and they also sold silk to
foreign merchants. Wealthy people in the Roman Empire wanted Han silk for their clothing.
But Han merchants did not travel all the way to Rome. Instead, Middle Eastern merchants
helped bring Han silk to Rome.
The information below describes Middle Eastern merchants’ roles in the silk trade. Read the
information. Then answer the question below.
Merchants from the Middle East bought Han silk fabric in Asia and brought it to Syria, a
region in the Middle East. This fabric was usually made with Han styles and patterns.
...
Finally, Syrian merchants sold the re-woven silk to wealthy Romans. As a result, Syrian
merchants became wealthy from the silk trade.
Based on this information, which statement about how silk was traded is true?
Choices: [(a) People in the Middle East re-wove Han silk into styles that Romans liked., (b)
Han people wove silk into styles that were popular with people in the Roman Empire., (c)
Han merchants traveled the Silk Road to sell silk directly to people in the Roman Empire.]
Answer index: 0
Table 18: Question examples for each skill (part 5).

--- Page 30 ---

Subject: Social Studies
Skill: mesopotamian-empires
Description: Read some of King Hammurabi’s laws. Then complete the sentence below.
If a man put out the eye of another man, his eye shall be put out.
...
mina:a unit of weight for measuring money, about 1 pound
Complete the sentence.
According to Hammurabi’s law code, if a man commits a crime against an enslaved person,
his punishment would be ___ the punishment for a crime committed against his equal.
Choices: [(a) less harsh than, (b) equally as harsh as, (c) more harsh than]
Answer index: 0
Subject: Social Studies
Skill: the-kingdoms-of-kush
Description: Around 2300 BCE, the first kingdom of Kush began to develop, called the
Kerman Kingdom. It grew out of a city called Kerma. At that time, Kush did not have its
own written language. So today, researchers study objects and buildings instead of written
sources to learn about the Kerman Kingdom. Read the description of the largest monument
in the Kerman Kingdom. Then answer the question below.
The Western Deffufa (duh-FOO-fuh) is one of the oldest monuments in Africa. It was built
by the rulers of the Kerman Kingdom around 2000 BCE. When the Western Deffufa was
built, it was one of the largest buildings in the region. Today, even though some of the
building has crumbled away, it is still around 60 feet tall. That’s about as tall as a six-story
building!
...
The Western Deffufa was made out of a common building material called mudbrick. Each
brick had to be individually shaped and then baked in the sun. Then people needed to
transport the bricks to the construction site and stack them up to make the walls of the
building. This process took a lot of time. It also cost the Kerman rulers a lot of money to
feed all of the workers.
What does the Western Deffufa tell researchers about the Kerman Kingdom?
Choices: [(a) The Kerman Kingdom must have been wealthy and powerful in order to
build it., (b) The Kerman Kingdom used a rare type of building material., (c) The Kerman
Kingdom used the structure for military activities.]
Answer index: 0
Subject: Social Studies
Skill: the-han-dynasty
Description: The city of Chang’an grew to have over 200,000 people around 1 CE. At that
time, both the Han and the Roman Empires had almost the same population! The graph
below shows the estimated population of the Han Dynasty between 200 BCE and 157 CE.
Look at the graph. Then complete the sentence below.
Complete the sentence.
In the year 2 CE, around ___ million people lived in Han territory.
Choices: [(a) 15, (b) 20, (c) 44, (d) 60]
Answer index: 3
Subject: Social Studies
Skill: early-chinese-thought
Description: A king needed the Mandate of Heaven in order to rule. People believed that
a king had the support of heaven if his actions had positive results or when good events
happened in the world around them.
The poem below comes from a Zhou dynasty book called the Book of Songs. Read the poem.
Then answer the question below.
The drought has become so severe
...
great mandate:Mandate of Heaven
Why does this poem claim that the "great mandate is about at an end?"
Choices: [(a) The ruler was not able to stop a natural disaster., (b) The ruler had kicked
people out of their homes., (c) The weather was cold and people became sick., (d) Flooding
from the Yellow River destroyed several Zhou cities.]
Answer index: 0
Subject: Social Studies
Skill: the-qin-empire
Description: Read the passage about Qin law. Then answer the question below.
Shang Yang wrote many new laws for the Qin state. Some of these laws organized people into
groups of five or ten families. Laws required these groups to spy on one another’s activities
and to report their neighbors’ crimes. If neighbors reported crimes to the government right
away, they would usually not be punished for their neighbors’ crimes. But if people failed to
report their neighbor’s crime, they would be punished harshly.
Based on the information above, why did Qin rulers make laws that required people to spy
on one another?
Choices: [(a) These laws kept people from committing crimes., (b) The Qin government
wanted to pardon people for committing crimes., (c) These laws encouraged people to work
harder., (d) They hoped that neighbors would write their own laws and not bother the Qin
government.]
Answer index: 0
Subject: Social Studies
Skill: susan-b-anthony
Description: What job did Susan B. Anthony have when she was young?
Choices: [(a) teacher, (b) librarian, (c) actress, (d) police officer]
Answer index: 0
Subject: Social Studies
Skill: paul-revere
Description: What did Paul Revere do to fight against British rule?
Choices: [(a) He wrote an essay., (b) He ran for governor of Massachusetts., (c) He joined
the Sons of Liberty., (d) He printed an anti-British newspaper.]
Answer index: 2
Subject: Social Studies
Skill: lunar-new-year
Description: Complete the sentence.
On the Gregorian calendar, the first day of the Chinese lunar year is ___ each year.
Choices: [(a) the same, (b) different]
Answer index: 1
Subject: Social Studies
Skill: holi
Description: Holi comes from which religion?
Choices: [(a) Hinduism, (b) Catholicism, (c) Islam, (d) Buddhism]
Answer index: 0
Subject: Social Studies
Skill: rosa-parks
Description: Rosa Parks moved when she was 11 years old. She moved to the city of
Montgomery, Alabama. Why did she move?
Choices: [(a) to go to church, (b) to go to school, (c) to get a job, (d) to live in a bigger house]
Answer index: 1
Subject: Social Studies
Skill: neil-armstrong
Description: Which two countries were part of the Space Race?
Choices: [(a) the United States and the Soviet Union, (b) the United States and China, (c)
Japan and the Soviet Union, (d) Japan and China]
Answer index: 0
Subject: Social Studies
Skill: easter
Description: When is Easter celebrated?
Choices: [(a) a Sunday in early spring, (b) the first Monday in July, (c) December 25, (d) late
November]
Answer index: 0
Subject: Social Studies
Skill: amelia-earhart
Description: Complete the sentence.
Amelia Earhart was a famous ___.
Choices: [(a) athlete, (b) pilot, (c) scientist, (d) artist]
Answer index: 1
Subject: Social Studies
Skill: thomas-jefferson
Description: Complete the sentence.
Thomas Jefferson believed that people needed to be ___ to be good voters.
Choices: [(a) educated, (b) wealthy, (c) parents, (d) religious]
Answer index: 0
Subject: Social Studies
Skill: christmas
Description: On Christmas, Christians celebrate which story?
Choices: [(a) the story of Jesus Christ walking on water, (b) the story of Jesus Christ’s birth,
(c) the story of Jesus Christ feeding people, (d) the story of Jesus Christ coming back from
the dead]
Answer index: 1
Subject: Social Studies
Skill: frederick-douglass
Description: As an enslaved person, Frederick Douglass had many jobs. What was one job
that he had?
Choices: [(a) He ran a shop., (b) He worked in the fields., (c) He worked in a factory., (d) He
gave people medicine.]
Answer index: 1
Table 19: Question examples for each skill (part 6).

--- Page 31 ---

Subject: Social Studies
Skill: benjamin-franklin
Description: Benjamin Franklin played an important part in which conflict?
Choices: [(a) World War I, (b) the Civil War, (c) the American Revolution, (d) the War of
1812]
Answer index: 2
Subject: Social Studies
Skill: ramadan
Description: Complete the sentence.
During Ramadan, Muslims remember an important event in the life of ___.
Choices: [(a) Muhammad, (b) Pope John Paul II, (c) Guru Nanak, (d) Martin Luther]
Answer index: 0
Subject: Social Studies
Skill: dia-de-los-muertos
Description: When is Día de los Muertos celebrated?
Choices: [(a) April 15, (b) October 27, (c) November 1 and 2, (d) the last Monday in May]
Answer index: 2
Subject: Social Studies
Skill: jackie-robinson
Description: Why do we look up to Jackie Robinson?
Choices: [(a) He was bossy., (b) He was brave., (c) He was popular., (d) He was funny.]
Answer index: 1
Subject: Social Studies
Skill: harriet-tubman
Description: When was Harriet Tubman born?
Choices: [(a) the 1490s, (b) the 1610s, (c) the 1820s, (d) the 1910s]
Answer index: 2
Subject: Social Studies
Skill: sitting-bull
Description: Complete the sentence.
Sitting Bull was an important ___ leader in the 1800s.
Choices: [(a) Japanese American, (b) Native American, (c) German American, (d) Mexican
American]
Answer index: 1
Subject: Social Studies
Skill: kwanzaa
Description: What does Kwanzaa celebrate?
Choices: [(a) the birthday of Dr. Martin Luther King, Jr., (b) the signing of the Declaration
of Independence, (c) the history and culture of African American people, (d) the day that
slavery ended]
Answer index: 2
Subject: Social Studies
Skill: thurgood-marshall
Description: Thurgood Marshall was a Supreme Court justice for 24 years. What do Supreme
Court justices do?
Choices: [(a) They punish criminals., (b) They decide whether laws agree with the
Constitution., (c) They write and pass new laws., (d) They make peace treaties with other
countries.]
Answer index: 1
Subject: Social Studies
Skill: hanukkah
Description: In a game of dreidel, how do you win the whole pot?
Choices: [(a) by landing on the letter gimel, (b) by spinning your dreidel in a perfect circle,
(c) by spinning your dreidel longer than anyone else’s, (d) by knocking over everyone else’s
dreidels]
Answer index: 0
Subject: Social Studies
Skill: bill-gates
Description: Use this paragraph to answer the question below.
Bill Gates grew up in a family that liked to have contests. When they played tennis or went
swimming, there was always a contest and a winner. Bill Gates always wanted to win. He
hated losing at anything.
Complete the sentences.
Growing up, Bill Gates was always competitive. That meant he ___.
Choices: [(a) was always well behaved, (b) hated sports, (c) tried to be the best]
Answer index: 2
Subject: Social Studies
Skill: purpose-of-government
Description: Which is an example of a law?
Choices: [(a) You should get a new toothbrush every six months., (b) You may not drive
above the speed limit., (c) You must clean your room before dinner., (d) You should eat more
fruits and vegetables.]
Answer index: 1
Subject: Social Studies
Skill: rosh-hashanah
Description: Rosh Hashanah is the beginning of a ten-day religious period. The period ends
with which holiday?
Choices: [(a) Hanukkah, (b) Passover, (c) Yom Kippur, (d) Purim]
Answer index: 2
Subject: Social Studies
Skill: davy-crockett
Description: When Davy Crockett was 12 years old, his family needed help making money.
Davy Crockett got a job to help out. What sort of work did he do?
Choices: [(a) He worked in a factory in Pennsylvania., (b) He helped build ships in Boston.,
(c) He helped move cows from Tennessee to Virginia., (d) He worked in a bank in New York
City.]
Answer index: 2
Subject: Social Studies
Skill: the-ancient-silk-road-geography-and-transportation
Description: Although most merchants traded in shorter sections of the Silk Road, some
merchants occasionally traveled to new regions. These merchants could learn about different
parts of the Silk Road from guidebooks. The passage below comes from a guidebook for
merchants written in the first century CE. Scholars think it was written by an Egyptian
merchant who traveled in the Red Sea and Indian Ocean.
Read the passage from the guidebook. Then follow the instructions below.
Now the whole country of India has very many rivers, and very great ebb and flow with the
tides . . . entrance and departure of vessels is very dangerous to those who are inexperienced
or who come to this market town for the first time.
...
Source: Periplus of the Red Sea
This guidebook helped merchants learn ___. It could also help them ___.
Choices: [(a) about the geography of a new place . . . avoid dangerous areas, (b) to build
boats . . . learn how to swim, (c) to speak new languages . . . find where markets were
located]
Answer index: 0
Subject: Social Studies
Skill: slavery-in-the-south
Description: For more than 300 years, people were enslaved in Africa and then brought
to North and South America, where they were sold. But in the early 1800s, this changed.
Complete the text.
In 1807, Great Britain made it illegal to buy and sell enslaved people across the Atlantic
Ocean using British ships. The United States did not ban slavery, but it did ban importing
any new enslaved people into the country. So, by 1860, most enslaved people in the United
States ___.
Choices: [(a) had been born there, (b) came from Great Britain, (c) had been freed]
Answer index: 0
Subject: Social Studies
Skill: the-abolitionists
Description: One of the most vivid descriptions of life aboard a slave ship comes from a book
written by Olaudah Equiano (oh-lah-OO-dah eh-kwee-AH-no). In the following passage,
Equiano describes his experiences on a slave ship bound for the Americas. Read the passage.
Then complete the sentence below.
I was soon put down under the decks, and there I received such a salutation in my nostrils as
I had never experienced in my life. . . . I became so sick and so low that I was not able to eat.
. . . But soon, to my grief, two of the white men offered me [food]; and, on my refusing to
eat, one of them held me fast by the hand . . . and tied my feet, while the other flogged me
severely. . . . I would have jumped over the side, but I could not; and, besides, the crew used
to watch us very closely . . . lest we should leap into the water.
...
lest we should:in case we would
Complete the sentence.
Equiano published his book in 1789 in Great Britain. Most of his readers were white
Europeans. Equiano most likely wrote his book to persuade ___ people to ___.
Choices: [(a) British . . . end the slave trade, (b) Native American . . . join the slave trade,
(c) African . . . fight against slavery, (d) European . . . purchase more enslaved people]
Answer index: 0
Table 20: Question examples for each skill (part 7).

--- Page 32 ---

Subject: Social Studies
Skill: new-england-colonies-economy-and-interactions-with-native-americans
Description: Colonists traded with Native American groups. But colonists also fought Native
American groups for land and resources. For example, in the Pequot War (1636–1638), New
England colonists fought the Pequot people for control of the valuable farmland and trading
routes along the Connecticut River.
The adapted passage below was written by a New England colonist who fought in the Pequot
War. In this passage, the colonist describes how an army of New England colonists and
Native American allies attacked the most important Pequot town.
Many Pequot were burnt when we set fire to the town, men, women, and children, others
forced out which our soldiers killed; down fell men, women, and children. Those that
escaped us, fell into the hands of [the Native Americans fighting on the side of the colonists],
that were behind us. There were about four hundred Pequot in this town, and not above five
of them escaped out of our hands.
Captain John Underhill, Newes from America, 1638.
This passage describes a key event of the Pequot War. According to the passage, what
happened during this event?
Choices: [(a) The Pequot defeated the army of colonists and their allies., (b) The Pequot and
the colonists agreed to share the Connecticut River., (c) The colonists and their allies killed
or captured most of the Pequot., (d) The colonists captured the Pequot warriors but did not
harm the other Pequot.]
Answer index: 2
Subject: Social Studies
Skill: state-and-local-government
Description: Sometimes it is not clear what powers a state government has. The passage
below describes a conflict between a state government and the federal government over
schools that were segregated, or divided, by race. Read the passage. Then answer the
question below.
Before 1954, many states segregated public schools based on race. In these states, African
American students and white students were not allowed to go to the same schools. Opponents
and supporters of segregation disagreed about whether the state government or the national
government had the power to decide whether schools should be segregated:
...
In the case Brown v. Board of Education (1954), the U.S. Supreme Court ruled that
segregated schools violated the rights of American citizens under federal law. The court
ordered states to stop segregating schools. When the state government of Arkansas refused
to obey the Supreme Court, the president of the United States sent soldiers to enforce the
court’s decision.
Based on the passage, which part of government decides whether the Constitution allows a
state government to do something?
Choices: [(a) the Supreme Court, (b) the president, (c) state governments, (d) Congress]
Answer index: 0
Subject: Social Studies
Skill: world-war-i-the-great-war
Description: The passage below describes how World War I started with a single incident,
but spread quickly into a large-scale war. Read the passage. Then answer the question.
In the early 1900s, countries in Europe were part of alliances, or agreements to protect each
other if they were attacked. There were two rival alliance groups:
...
In 1914, a Serbian nationalist assassinated a top official from Austria-Hungary. Austria-
Hungary responded by declaring war on Serbia, sparking a chain reaction that forced allies to
declare war. Although Serbia wasn’t an official member of an alliance, it had strong ties to
Russia. So, Russia immediately stepped in to defend Serbia. Then, Germany supported its
ally Austria-Hungary by declaring war on Russia. Next, France joined the war to uphold
alliance agreements with Russia. This made Great Britain join with the Allied powers to
defend both France and Russia.
How did the alliance system in Europe lead to World War I?
Choices: [(a) Once two countries were at war, the other countries were able to step aside.,
(b) When a country outside the alliance system declared war, all the others joined to fight
the outside power., (c) When one country declared war, many other countries had to join in
to defend their allies., (d) When Russia stepped in to defend Serbia, Germany also had to
defend Serbia.]
Answer index: 2
Subject: Social Studies
Skill: causes-of-the-civil-war-dred-scott-to-secession
Description: The Supreme Court’s decision in the Dred Scott case outraged many Americans,
especially in the North. They thought that slaveholders were gaining too much power. In
1858, an Illinois Republican named Abraham Lincoln gave a speech about the role of slavery
in the United States.
Read the passage from Lincoln’s House Divided speech. Then answer the question below.
A house divided against itself cannot stand. I believe this government cannot endure
permanently, half slave, and half free. Either the opponents of slavery will [stop] the further
spread of it, and put it in course of [extinction], or its [supporters] will push it forward till it
shall become alike lawful in all the states, old, as well as new.
In his speech, Lincoln uses the metaphor of a "house divided against itself." According to
Lincoln, which of the following was like a house divided against itself?
Choices: [(a) the relationship between Mexico and the U.S., (b) the Republican party, (c) the
Illinois legislature, (d) the United States government]
Answer index: 3
Subject: Social Studies
Skill: the-marshall-court
Description: The Supreme Court’s job is to interpret and apply the laws of the United
States, including the Constitution. When a case reaches the Supreme Court, the justices hear
arguments on both sides of the case and then make a decision. With its decision, the Court is
often deciding what the Constitution means.
Under the leadership of John Marshall, the Supreme Court made many decisions that set
important precedents. The word "precedent" comes from the word "precede," which means
"to come before."
Based on this information, which of the following is the best example of a "precedent" in
law?
Choices: [(a) the closing argument by a defense lawyer in a criminal trial, (b) an earlier rule
set by a Supreme Court decision for later courts to follow, (c) a speech given by the chief
justice of the Supreme Court]
Answer index: 1
Subject: Social Studies
Skill: source-analysis-the-declaration-of-independence
Description: The Declaration of Independence is one of the most famous documents in
United States history. A declaration of independence is a document created by the people of
one country to say they are no longer part of another country. Which of the following is an
example of a declaration of independence?
Choices: [(a) a document describing the major laws of the federal government, (b) a
document saying that the United States had won World War II, (c) a document declaring
that the United States would no longer allow slavery, (d) a document stating that the United
States was no longer part of the British Empire]
Answer index: 3
Subject: Social Studies
Skill: portuguese-and-spanish-expeditions-part-ii
Description: While the Portuguese were working their way around the coast of Africa, other
European countries, such as Spain, also wanted to trade in the Indian Ocean. But Portugal
already controlled sea trade along the West African coast. In fact, the rulers of Spain had
signed a treaty agreeing not to trade there.
Imagine you are the ruler of Spain. You are determined to trade in the Indian Ocean, but the
Portuguese are blocking you from sending expeditions around Africa. What would be the
best solution to this problem?
Choices: [(a) give up and focus instead on trade in Europe, (b) look for other routes to the
Indian Ocean, (c) break the treaty and start an expensive war]
Answer index: 1
Subject: Social Studies
Skill: the-legislative-branch
Description: The majority party in each chamber of Congress has an advantage. What is one
reason why?
Choices: [(a) The majority party elects the president every four years., (b) Only representa-
tives and senators from the majority party can vote on bills., (c) The president usually agrees
with the majority party., (d) Members of Congress usually vote the same way as the rest of
their party.]
Answer index: 3
Subject: Social Studies
Skill: the-first-party-system-federalists-and-democratic-republicans
Description: Political parties are groups that support different political positions. Today they
are a regular part of political life in the United States, but they have not always existed.
Parties first formed in the 1790s, after George Washington was elected president. Washington
wrote about political parties in 1796. Read Washington’s words. Then complete the sentence
below.
Let me warn you, in the most solemn manner, against the baneful effects of [parties].
...
baneful:harmful, destructive
Complete the sentence.
After seeing disagreements among Americans increase while he was president, Washington
felt that political parties were ___ for the United States.
Choices: [(a) dangerous, (b) necessary, (c) helpful]
Answer index: 0
Subject: Social Studies
Skill: the-constitution-interpretation
Description: Sometimes, interpretations of the Constitution can differ or can change over
time. One part of the Constitution that judges have often needed to interpret is the Fourteenth
Amendment.
The Fourteenth Amendment was added in 1868, after the Civil War ended. Read the text of a
section of the amendment called the Equal Protection Clause. Then answer the question
below.
No State shall . . . deny to any person within its jurisdiction the equal protection of the laws.
jurisdiction:territory
The Equal Protection Clause was written to make certain laws unconstitutional. Which of the
following laws was the Equal Protection Clause most likely written to ban?
Choices: [(a) a national law to build a network of railroads from coast to coast, (b) state laws
that allowed both men and women to vote in elections, (c) a national law creating universities
to teach farming skills, (d) state laws that took away rights from African American people]
Answer index: 3
Table 21: Question examples for each skill (part 8).

--- Page 33 ---

Subject: Social Studies
Skill: the-executive-branch
Description: Read Section 1 of Article II of the United States Constitution. Then answer the
question.
The executive power shall be vested in a president of the United States of America. He shall
hold his office during the term of four years, and, together with the vice president, chosen for
the same term, be elected.
...
vested in:given to
Complete the sentence.
According to the Constitution, the president has the power to ___.
Choices: [(a) carry out laws, (b) decide how long a term of office is, (c) renovate the White
House, (d) run elections]
Answer index: 0
Subject: Social Studies
Skill: the-revolutionary-war-conclusion-and-aftermath
Description: As the war continued, many Patriots lashed out at Loyalists, or those who
remained loyal to Great Britain during the Revolutionary War. Read the passage from an
editorial appearing in the Pennsylvania Packet, one of the first daily newspapers in America.
Then answer the question below.
Send [the Loyalists] where they may enjoy their beloved slavery to perfection—send them to
the island of Britain; there let them drink the cup of slavery and eat the bread of bitterness all
the days of their existence. . .. Never let them return to this happy land—never let them
taste the sweets of that independence which they strove to prevent. Banishment, perpetual
banishment, should be their lot.
What is the main argument in the passage?
Choices: [(a) Patriots should take away Loyalists’ right to vote., (b) Loyalists should be
banished to Britain., (c) Loyalists should be enslaved., (d) Patriots should convince Loyalists
of the value of independence.]
Answer index: 1
Subject: Social Studies
Skill: the-articles-of-confederation
Description: The Articles of Confederation created an official central government for the
United States. The new central government replaced the Continental Congress and was
called the Confederation Congress.
Unlike the United States government today, the central government under the Articles of
Confederation only had one branch. The Confederation Congress, a group of representatives
from each state, was completely responsible for governing. There was no president or court
system.
The following passage from the Articles of Confederation explains the representation of each
state within the Confederation Congress. Read the passage. Then complete the sentence
below.
No state shall be represented in Congress by less than two, nor more than seven members . . .
While voting in the United States in Congress assembled, each state shall have one vote.
Complete the sentence.
Under the Articles of Confederation, each state could have ___ number of representatives
and ___ number of votes.
Choices: [(a) the same...the same, (b) the same...a different, (c) a different...a different, (d) a
different...the same]
Answer index: 3
Subject: Social Studies
Skill: the-judicial-branch
Description: The Supreme Court is made up of a maximum of nine justices, or judges. How
do Supreme Court justices decide how to rule in a case?
Choices: [(a) Each justice takes a side, and the side with more justices wins., (b) All of the
justices must agree., (c) They appoint a jury of citizens and follow its recommendation., (d)
A smaller group of one to three justices decides each case.]
Answer index: 0
Subject: Social Studies
Skill: radical-reconstruction
Description: The passage below comes from a letter that a Freedmen’s Bureau agent sent to a
man in North Carolina. Read the letter. Then answer the question below.
January 14th, 1866
...
William Fox
This letter describes one of the duties of the Freedmen’s Bureau. Which of those duties does
it describe?
Choices: [(a) helping African American people start schools, (b) investigating, or looking
into, violence against freed people, (c) bringing together African American families that had
been separated by slavery, (d) making sure employers treated freed people fairly]
Answer index: 3
Subject: Social Studies
Skill: antebellum-reform-movements
Description: Many people turned to religion to help deal with problems they saw in society.
Throughout U.S. history, the majority of Americans have been Christians. But religious
enthusiasm was especially high during a period called the Second Great Awakening, from
about the 1790s to the 1840s. During this period, ministers traveled the country preaching
new religious ideas.
Some of the religious ideas of the Second Great Awakening were expressed in hymns, or
religious songs. The passage below comes from "Amazing Grace," a hymn that was popular
at the time. Read the first few lines from the hymn. Then answer the question below.
Amazing grace! How sweet the sound
...
wretch:a bad, unhappy person
Which of these statements best summarizes the main idea of these lines?
Choices: [(a) God does not pay attention to people’s lives., (b) With God’s help, people can
improve their lives., (c) A leopard can’t change its spots, and people can’t change either., (d)
People should get used to the fact that life isn’t always fair.]
Answer index: 1
Subject: Social Studies
Skill: washingtons-presidency-part-i
Description: Washington wrote a letter describing the suit that he planned to wear to his
inauguration. At the time, many Americans wore clothes made of cloth from Great Britain.
But Washington’s inauguration suit was not made of British cloth. Read the passage from
Washington’s letter. Then complete the text below.
There are cloth factories in Connecticut, and I have [written to a friend asking him] . . .
to procure me . . . Hartford fabric, to make a suit of clothes . . . I hope it will [soon] be
unfashionable for a gentleman to appear in any other dress.
...
Hartford:the capital of the state of Connecticut
Complete the text.
Washington expressed the hope that people would only want to wear clothes that were ___.
Choices: [(a) elegant and fashionable, (b) made from cloth produced in the United States, (c)
unfashionable, (d) made from cloth produced in Great Britain]
Answer index: 1
Subject: Social Studies
Skill: the-scientific-revolution
Description: The Scientific Revolution was an important period in European history. Read
the following description of the Scientific Revolution. Then answer the question below.
The Scientific Revolution was a time when European scholars made many discoveries and
advances in science and mathematics. Many historians have argued that the Scientific
Revolution was also a time when people began to study and understand the world in a new
way. Rather than using old ideas about science and nature, during the Scientific Revolution
scholars began investigating the natural world for themselves. They developed questions and
then performed experiments and gathered evidence in order to answer those questions.
Complete the text.
Some historians call this time period "the Scientific Revolution" because European scholars
made ___ advances in math and science. Scholars also began to gather ___ information
about the world instead of just relying on knowledge from other sources.
Choices: [(a) few . . . their own, (b) few . . . ancient, (c) many . . . ancient, (d) many . . .
their own]
Answer index: 3
Subject: Social Studies
Skill: washingtons-presidency-part-ii
Description: As soon as he became Secretary of the Treasury, Alexander Hamilton began to
work on a financial plan for the country. The financial plan listed Hamilton’s ideas for how to
manage the government’s money and economy. Many people give Hamilton credit for setting
up the country’s financial system in a way that helped the United States to succeed over time.
In the summary passage below, President Washington describes one reason why setting up a
financial plan for the country was so important in the 1790s. Read the passage. Then answer
the question below.
During the Revolutionary War, we, the United States, needed much more money than we had
to fight the war.
...
debt:money that is borrowed and expected to be paid back
Hamilton’s financial plan tried to address the problem that Washington described in the
passage above. What was the problem that Washington described?
Choices: [(a) The United States had extra money after the Revolutionary War., (b) The
United States was in deep debt after the Revolutionary War., (c) Great Britain owed the
United States a lot of money., (d) The United States still needed to win independence from
Great Britain.]
Answer index: 1
Subject: Social Studies
Skill: french-and-english-expeditions-part-i
Description: In 1494, the Catholic Church approved a treaty that allowed Spain to control
most of the land in the Americas. Spain used this treaty to stop other Europeans from trading
in the Americas.
The passage below describes religious changes in Europe in the mid-1500s. Read the passage.
Then answer the question below.
When the Catholic Church approved a treaty giving Spain control of most of the land in the
Americas, almost everyone in western Europe was Catholic. However, in 1517 many people
stopped following the Catholic Church. They became a new type of Christian known as
Protestant. Because Protestants did not follow the Catholic Church, they did not believe they
had to follow treaties or laws that the Catholic Church had approved. So, Protestant rulers
did not believe Spain had the right to control trade with the Americas.
Based on the passage, what is one reason why Protestants in Europe did not respect Spain’s
right to control trade in the Americas?
Choices: [(a) Spain’s right to control trade came from the Catholic Church, and Protestants
did not follow the Catholic Church., (b) Spain’s right to control trade was not based on
religion, and Protestants only followed religious laws., (c) Protestants believed that the
Catholic pope wanted Protestants to control trade instead of Catholics.]
Answer index: 0
Table 22: Question examples for each skill (part 9).

--- Page 34 ---

Subject: Social Studies
Skill: causes-of-the-american-revolution-introduction-to-mercantilism-and-the-navigation-
acts
Description: To increase Great Britain’s wealth, Parliament passed laws that gave each part
of the British Empire a different economic role:
Colonists would send raw materials to people in Great Britain. Raw materials, such as raw
iron and wool, are directly from nature.
People in Great Britain would turn the raw materials into manufactured goods, or finished
products, such as fabric and tools. British merchants could sell these manufactured goods
back to the colonies or to other countries.
Complete the text.
Parlaiment wanted the country to earn more money from selling exports than it spent buying
imports. The raw materials that Great Britain imported from the colonies were ___ the
manufactured goods that Great Britain exported for colonists to purchase. Parliament’s
policies were part of what created the system of Triangular Trade.
Choices: [(a) more valuable than, (b) as valuable as, (c) less valuable than]
Answer index: 2
Subject: Social Studies
Skill: the-revolutionary-war-preparing-for-war
Description: After 1763, the British Parliament began to tax the Thirteen Colonies more
heavily to help pay off debt from the French and Indian War. Parliament also restricted
colonial trade. Many colonists resented these new taxes and restrictions.
After the passage of the Stamp Act in 1765, which required Americans to pay a tax on all
paper they used, an American colonist drew a cartoon with this caption:
The moral is, that the colonies may be ruined, but that Britain would thereby be maimed.
maimed:permanently wounded
What is the author most likely arguing in the caption?
Choices: [(a) The colonies are not a part of the British Empire., (b) Great Britain is harming
itself by taxing the colonies., (c) Great Britain’s taxation policies are good for the colonies.,
(d) The colonies will be better off if they declare independence from Great Britain.]
Answer index: 1
Subject: Social Studies
Skill: u-s-mexican-war
Description: By the 1840s, belief in Manifest Destiny had become quite popular in the
United States. So, support for expanding the territory of the U.S. was an important issue in
the 1844 presidential election. This election was won by James K. Polk, the candidate of the
Democratic Party.
Read the following passage adapted from the 1844 Democratic Party platform, or list of the
party’s goals. Then complete the sentence below.
Our title to the whole of the Territory of Oregon is clear and unquestionable, and the
annexation of Texas to the United States at the earliest moment possible is important to
American progress.
...
annexation:addition
Complete the sentence.
According to the platform, the Democratic Party ___ Manifest Destiny.
Choices: [(a) supported, (b) opposed, (c) neither supported nor opposed]
Answer index: 0
Subject: Social Studies
Skill: the-constitution-amendments
Description: When the Constitution was written, many Americans were afraid that it made
the federal government too powerful. So, ten amendments were added to the Constitution to
describe and protect the rights of individual people. These first ten amendments are called
the Bill of Rights.
The following passage is from a letter written by Thomas Jefferson to James Madison in
1787, before the Bill of Rights had been approved. Read the passage. Then answer the
question below.
A bill of rights is what the people are entitled to . . . and [it is] what no just government
should refuse [to write down].
...
just:fair
Based on the passage, what was Jefferson’s attitude toward a bill of rights?
Choices: [(a) Governments should protect people’s rights, but those rights don’t need to be
written down., (b) Writing down a bill of rights doesn’t do anything, because governments
can just ignore it., (c) People deserve to have a bill of rights that describes and protects their
individual rights.]
Answer index: 2
Subject: Social Studies
Skill: the-revolutionary-war-struggle-for-independence
Description: As the Continental Army fought the British, the Second Continental Congress
sent an Olive Branch Petition to King George III in July 1775. The petition stated that the
colonies would stop fighting with Great Britain under certain conditions. Which of the
following was one of those conditions?
Choices: [(a) if a new colony was established on the western frontier, (b) if Great Britain
repealed certain laws and taxes, (c) if the colonies could have their own king and Parliament,
(d) if King George III stepped down and a new king was named]
Answer index: 1
Subject: Social Studies
Skill: the-end-of-reconstruction-and-the-rise-of-jim-crow
Description: Some white Southerners believed deeply that they should be shown more
respect than African American people. They did not like the Republicans’ plans to protect
African American people’s rights. Sometimes their anger at the changes to Southern society
turned violent.
The passage below comes from an investigation into the murder of an African American man
named Johnson Stuart. The man’s brother is describing what happened before the murder.
Read the passage. Then answer the question below.
Question—Did you ever hear of any threats being made against him before he was killed? . .
.
...
State of South Carolina, Evidence taken by the Committee of Investigation of the Third
Congressional District, 1870.
According to this passage, why did some white Southerners want to kill Johnson Stuart?
Choices: [(a) They thought he disrespected white people by treating all the voters the same.,
(b) They thought he was cheating by paying people to vote for him for sheriff., (c) They
thought he had stolen money and supplies from the sheriff’s office in the courthouse., (d)
They thought he was violating the Constitution by not allowing African Americans to vote.]
Answer index: 0
Subject: Social Studies
Skill: pre-contact-native-peoples-introduction
Description: For many years, most archaeologists agreed that the first humans who came
to North America walked across the land bridge around 12,000 years ago. However, new
evidence has been discovered that makes some archaeologists believe people may have
traveled in a different way.
The text below describes two pieces of evidence that archaeologists use to support a different
theory of migration to North America. Look at the text. Then complete the sentence below.
Hunter-gatherers lived in the islands of Japan 20,000 years ago. They used resources from
the ocean to survive.
People on the coast of North America used small boats to travel along the coast more than
10,000 years ago.
The text below describes a new theory about how humans arrived in North America. Use the
evidence above to complete the text.
According to the new theory, the first humans may have traveled from Asia to North America
___. They may have ___ along the coast of the land bridge.
Choices: [(a) 100,000 years ago . . . walked, (b) using small boats . . . sailed]
Answer index: 1
Subject: Social Studies
Skill: the-reformation
Description: Read two of Martin Luther’s statements criticizing the Catholic Church. Then
answer the question below.
It is certain that when money clinks in the [Catholic Church’s] money chest, greed.. . can be
increased.
...
William R. Russell, translator, The Ninety-Five Theses and Other Writings. Copyright 2017
by Penguin Classics.
Based on the statements, what was one reason why many people were unhappy with the
Catholic Church?
Choices: [(a) They thought that the Catholic Church had become too big., (b) They felt their
religious community was too small., (c) They believed the Catholic Church should collect
more money., (d) They thought the Catholic Church was too rich and greedy.]
Answer index: 3
Subject: Social Studies
Skill: rights-and-responsibilities-of-active-citizenship
Description: American presidents often speak about the rights, duties, and responsibilities
of American citizens. Read the quotations from two former presidents. Then answer the
question below.
Ask not what your country can do for you; ask what you can do for your country.
...
Ronald Reagan, Veterans Day Proclamation, October 26, 1981
Based on the quotations above, which of the following statements would both presidents
agree with?
Choices: [(a) The country should not expect citizens to do things for their communities., (b)
Citizens should expect the government to do everything for them., (c) Active and engaged
citizens are an important part of American democracy.]
Answer index: 2
Subject: Social Studies
Skill: the-age-of-exploration-origins
Description: In the 1400s, Europe was made up of many independent states. These states
often competed with each other for resources, including imported goods from Africa and
Asia. Imagine you are a European ruler in the 1400s. What could you do as a ruler to gain a
competitive advantage, or an upper hand, over other European states?
Choices: [(a) try to find new trade routes to Africa and Asia, (b) ban any goods that came
from Africa or Asia, (c) rely on other European states to sell goods from Africa and Asia to
you]
Answer index: 0
Table 23: Question examples for each skill (part 10).

--- Page 35 ---

Subject: Social Studies
Skill: industrialization-in-the-gilded-age
Description: Industrialization brought dramatic changes to Americans’ daily lives. Read a
modern scholar’s description of those changes. Then answer the question below.
Within a few decades, urban American homes became networked. . . . Instead of relying on
candles and [fuel] carried into the home, each home was connected to the electricity network
that provided electric light . . . Instead of relying on . . . outhouses and cesspools, each home
was gradually connected to two more networks, one bringing in a supply of clean running
water and the other taking waste out into sewers. Houses of the rich after 1880 and of the
working class after 1910 were increasingly supplied with central heating.
...
Robert J. Gordon, The Rise and Fall of American Growth, Princeton University Press, 2016.
What is the main idea of the passage?
Choices: [(a) As the U.S. industrialized, fewer homes had electricity and central heating., (b)
Industrialization gave many Americans much more comfortable lives., (c) Electric lighting
and sewers made homes dirtier and more dangerous., (d) Factories became very modern, but
regular people’s houses did not change.]
Answer index: 1
Subject: Social Studies
Skill: causes-of-the-american-revolution-politics-and-society
Description: Andrew Burnaby, an English minister, traveled around the Thirteen Colonies
during the French and Indian War. Based on his observations, Burnaby argued that America
would never be independent of Great Britain. Read Burnaby’s argument. Then answer the
question below.
The difference of character, of manners, of religion, of interest, of the different colonies [is
so great that if they were] left to themselves there would soon be a civil war.
Why did Burnaby think that America would never be a nation independent from Great
Britain?
Choices: [(a) The colonies were united in their support of Great Britain., (b) Colonial
businesses needed British customers., (c) There were too many differences between the
colonies., (d) The colonies signed a pledge to Great Britain after the French and Indian War.]
Answer index: 2
Subject: Social Studies
Skill: new-england-colonies-founding-and-government
Description: Members of a religious group called the Puritans founded the Massachusetts
Bay Colony. Unlike the Pilgrims, the Puritans did not want to leave the Church of England.
Instead, they wanted to change the Church of England according to their religious beliefs.
The first governor of the Massachusetts Bay Colony was a Puritan named John Winthrop.
The passage below comes from a speech that Winthrop gave to the Puritans on their voyage
to New England. Read the passage. Then answer the question below.
For we must consider that we shall be as a city upon a hill. The eyes of all people are upon
us; so that if we shall deal falsely with our God in this work . . . [and] cause him to withdraw
his present help from us, we shall be made a story and a byword through the world.
...
byword:example
According to Winthrop, why was it important for the Puritans to behave as they believed God
would want them to?
Choices: [(a) because France might attack the colony if it was weak, (b) because the colonists
were not allowed to go back to England, (c) because the whole world was watching, (d)
because the colonists could become wealthy]
Answer index: 2
Subject: Social Studies
Skill: the-constitutional-convention
Description: Before the states adopted the Constitution, the powers of the central government
were described in the Articles of Confederation.
The Articles of Confederation were written quickly and accepted by the states in the
middle of the Revolutionary War. The committee that wrote the Articles created a central
government that could organize the war. However, the committee did not trust an overly
powerful government, so they did not give the government the power to enforce, or make
people follow, the law. Overall, they gave the central government very few powers.
Under the Articles of Confederation, which of the following powers did the central
government have?
Choices: [(a) forcing states to contribute money through taxes, (b) forcing states to provide
troops, (c) enforcing laws, (d) negotiating treaties with other countries]
Answer index: 3
Subject: Social Studies
Skill: the-civil-war-the-conclusion-of-the-war
Description: In late 1864, a Union army under the command of General William Tecumseh
Sherman marched through the state of Georgia. The passage below comes from a letter that
Sherman wrote to the War Department about his march. Read the passage. Then answer the
question below.
We are not only fighting hostile armies, but a hostile people, and must make old and young,
rich and poor, feel the hard hand of war, as well as their organized armies. I know that this
recent movement of mine through Georgia has had a wonderful effect in this respect.
...
people:the civilians, or people not in the military, of the Confederacy
What was Sherman arguing in this passage?
Choices: [(a) Most white people in the Confederacy had always supported the Union., (b)
The war should only be fought against Confederate soldiers, not civilians., (c) The Union
army should make life hard for Confederate civilians., (d) Sherman’s march through Georgia
had been a failure for the Union army.]
Answer index: 2
Subject: Social Studies
Skill: trade-and-specialization
Description: Adam Smith was an important thinker from the 1700s whose ideas about trade
influenced many people. The passage below comes from one of his famous books. Read the
passage. Then answer the question below.
It is a [rule] of every [wise] master of a family, never to attempt to make at home what it will
cost him more to make than to buy. The tailor does not attempt to make his own shoes, but
buys them [from] the shoemaker. The shoemaker does not attempt to make his own clothes
but employs a tailor.
...
Adam Smith, The Wealth of Nations
According to Adam Smith, how do people benefit from specialization and trade?
Choices: [(a) People make clothes and shoes at home and listen to the master of the family.,
(b) People spend all of their money to buy things they need., (c) People buy things they want
or need for less than it would cost to make things themselves., (d) People make everything
they need at home to save as much money as possible.]
Answer index: 2
Subject: Social Studies
Skill: the-civil-war-gettysburg-to-the-election-of-1864
Description: The goal of the Union blockade was to stop the Confederacy from trading
with other countries. Even before the war, Northerners and Southerners predicted what
would happen if the South’s trade was blockaded. The passage below comes from an 1858
speech by the Southern senator James Henry Hammond. Read the passage. Then answer the
question below.
Without firing a gun, without drawing a sword, should [the North] make war on us, we could
bring the whole world to our feet. . . . What would happen if no cotton was furnished for
three years? . . . England would topple headlong and carry the whole civilized world with
her, to save the South. No, you dare not to make war on cotton. No power on the earth dares
to make war upon it. Cotton is king.
...
England:the United Kingdom
According to Hammond, what made the South powerful?
Choices: [(a) The South controlled the best harbors in North America., (b) The South had
a large enslaved population., (c) The South controlled the world’s cotton supply., (d) The
South had given the United Kingdom a large loan.]
Answer index: 2
Subject: Social Studies
Skill: the-crusades
Description: Historians do not have a copy of Pope Urban’s 1095 speech. However, some of
the people who heard his speech wrote down what they remembered. Read part of the speech
that one person remembered hearing. Then answer the question below.
All who die [on their way to Jerusalem], whether by land or by sea, or in battle . . . shall
have immediate remission of sins.
...
Jacques Bongars, Gesta Dei per Francos, trans in Oliver J. Thatcher and Edgar Holmes
McNeal, eds., A Source Book for Medieval History. Copyright 1905 by Scribners.
According to the speech, what did Pope Urban say would happen to people who died while
traveling to Jerusalem on a crusade?
Choices: [(a) Their land would be taken by the government., (b) All of their bad actions
would be forgiven., (c) They would be remembered forever., (d) Their families would be
given money.]
Answer index: 1
Subject: Social Studies
Skill: medieval-japan
Description: Between the years 700 and 1100 CE, several families became increasingly
wealthy and powerful. Read the passage about how these families became powerful. Then
answer the question below.
In the capital city, Kyoto, some wealthy families would arrange for their daughters to marry
sons from the royal family. Marriages allowed these wealthy families to influence some of
the emperor’s decisions. These same families often controlled large amounts of land. Around
the year 1100, almost half the land in Japan was controlled by wealthy families! In order to
protect their land and wealth, these families often hired their own armies. Eventually, these
armies became larger and more powerful than the emperor’s own troops.
Based on the passage, how had the status of powerful families changed in Japan by the year
1100?
Choices: [(a) By the year 1100, the emperor was no longer the most powerful person in
Japan. As a result, he was not able to control the powerful families., (b) Powerful families
regularly married their daughters to members of the royal family. By the year 1100, these
marriages had helped the emperor become even more powerful., (c) By 1100, most powerful
families had become less wealthy. As a result, powerful families were no longer able to pay
their private armies.]
Answer index: 0
Subject: Social Studies
Skill: the-songhai-empire
Description: Sunni Ali Ber and his army conquered many territories to build the Songhai
Empire. But not everyone in the new empire was happy under his rule. For example, many
Muslims, or followers of the religion of Islam, were unhappy.
Read the passage by a Muslim scholar who lived in the Songhai Empire during the reign of
Sunni Ali. Then answer the question below.
This villain,—I mean, [Sunni Ali],—was a prince, who was obeyed and respected. He
was feared by his subjects because of his cruelty. . . . The ferocity of [Sunni] Ali towards
Muslims and his cruelty . . . in matters of religion, made the hearts of the people overflow
with sadness and worry.
...
Christopher Wise, translator, Ta’rikh al fattash. Copyright 2011 by Africa World Press.
According to the author, why were Muslims unhappy with Sunni Ali?
Choices: [(a) He was a prince., (b) He was a devoted Muslim., (c) He was cruel to Muslims.,
(d) He was greedy.]
Answer index: 2
Table 24: Question examples for each skill (part 11).

--- Page 36 ---

Subject: Social Studies
Skill: origins-of-hinduism
Description: Many historians argue that Hinduism started to develop when Indus Valley and
Aryan cultures mixed. Look at the following information about some common Hindu beliefs
and religious practices, or actions, that developed over time. Then use the information to
answer the question below.
Some Hindus believe that there are hundreds of different gods, but some think there is just
one god who has many different characteristics.
...
Hindus in different areas often celebrate different holidays and festivals.
Based on the information above, which of the following statements is true?
Choices: [(a) There are many different ways of practicing Hinduism., (b) There is only one
main way of practicing Hinduism.]
Answer index: 0
Subject: Social Studies
Skill: origins-of-buddhism
Description: Historians agree that Buddhism began with the teachings of Siddhartha
Gautama (si-DAR-tuh GOW-tuh-muh). During his life, Siddhartha became a great teacher
and was given the title "buddha" (BOO-duh).
Read about some common Buddhist beliefs. Then answer the question below.
There were buddhas who lived before Siddhartha, and there will be buddhas who come after
him.
...
Siddhartha is often called "the Buddha," instead of just "buddha," because he is the buddha
of this age.
What does it mean to say that Siddhartha is "the buddha of this age"?
Choices: [(a) He was the buddha who lived most recently., (b) He was not very old when
he became a buddha., (c) He was less important than future buddhas., (d) He was the first
buddha who ever lived.]
Answer index: 0
Subject: Social Studies
Skill: the-ghana-empire
Description: Historians are not sure who founded the ancient Kingdom of Ghana. However,
legends about Ghana’s first king have been passed down by griots, or people who tell stories
about West African history.
Read a story that is told by griots. Then complete the text below.
There were two brothers named Dyabe and Khine, and their father was the leader of their
tribe. At first, their father wanted Khine to be the next leader. But Dyabe showed he was
more clever than Khine, and their father changed his mind. Khine grew jealous and tried to
have Dyabe killed, so Dyabe fled to the wilderness to save himself.
Out in the wilderness, Dyabe met the leaders of four different armies. He convinced these
army leaders to make him their ruler. Once he had the support of four armies, Dyabe decided
to build a kingdom. But first, he needed to find a capital city for his kingdom. Dyabe traveled
to a city that was guarded by the snake-god Bida. Bida agreed to let Dyabe use the city as his
capital in return for a yearly sacrifice. So, Dyabe built the capital and created the Kingdom
of Ghana.
Complete the text.
According to this story, the Kingdom of Ghana was founded by a man named ___. He
created the kingdom after making a deal with ___.
Choices: [(a) Dyabe . . . Khine, (b) Khine . . . the snake-god Bida, (c) Dyabe . . . the
snake-god Bida, (d) Khine . . . Dyabe]
Answer index: 2
Subject: Social Studies
Skill: the-middle-ages-after-1100
Description: As kingdoms in Western Europe became larger, kings gained more wealth and
power. Some kings began to take advantage of this power and abused the people in their
kingdoms. In some parts of Europe, people responded to this behavior by trying to limit the
power of kings. Read the passage about one king who abused his power. Then complete the
sentence below.
King John ruled England from 1199 to 1216 CE. In 1215, a group of lords demanded that
King John end an unfair tax that was against the law. King John refused to end the tax, so
the lords captured the city of London, where King John ruled. After capturing the city, the
lords forced King John to sign an agreement that would limit his power as the king. This
agreement became known as the Magna Carta, or Great Charter.
The Magna Carta was an agreement that ___ in England.
Choices: [(a) began a long and expensive war, (b) overthrew and killed the king, (c) increased
taxes on the lords, (d) controlled the power of King John]
Answer index: 3
Subject: Social Studies
Skill: feudal-europe
Description: By the early Middle Ages, many different Western European landowners had
started organizing society in a new way. Historians call this new way of organizing society
feudalism.
Read the passage about how feudalism began. Then complete the text.
After the fall of the Roman Empire, the Roman government no longer controlled Western
Europe. So, individuals fought each other for control of land and the people living on it. The
winners gained wealth and power, and people living on the land were forced to work for
them.
Some new landowners became powerful and started calling themselves kings, but they
couldn’t manage all their land on their own. So, they divided their land up and gave small
sections to loyal followers. These loyal followers were called lords, and they helped to
control the land and people for the king.
Using the information in the passage, complete the text.
Feudalism is a system where ___.
Choices: [(a) people voted to elect leaders and decide who would own the land, (b) land and
people were controlled by lords who were loyal to a king, (c) every member of society was
given an equal amount of land to farm by their leader]
Answer index: 1
Subject: Social Studies
Skill: classical-athens-government-and-culture
Description: Not all decisions in classical Athens were made by all the citizens. Instead, a
full-time council of citizens made many of the everyday political decisions in the city.
Here is a list of some facts about the Athenian council:
This Athenian council was made up of 500 citizens.
...
A councilman could only serve for one year at a time.
Which of the following statements might come from an Athenian complaining about these
rules?
Choices: [(a) I think that because the selection is random, any foolish person can become a
councilman., (b) Last time I was on the council, I was impressed with how many people had
good ideas., (c) I’m glad that 500 people share power, since it means no single person can
take over the city.]
Answer index: 0
Subject: Social Studies
Skill: caesar-and-the-end-of-the-roman-republic
Description: Pompey agreed to help the Senate and try to prevent Caesar from becoming
more powerful. Read the passage. Then answer the question below.
In January of 49 BCE, Caesar was with his army far away from Rome. Pompey wrote to
Caesar and demanded that Caesar give up his army and return to Rome.
Caesar faced an important choice. On the one hand, he could obey Pompey and give up his
army. But he knew the Senate didn’t like him, and he worried that he would be arrested. On
the other hand, he could refuse to give up his army. But then the Senate would probably
think that Caesar wanted to start a war. After thinking about it for a long time, Caesar chose
the second option. He decided to attack Pompey and the Senate before they could raise an
army to stop him.
Based on the passage above, how did Caesar respond to Pompey’s demands?
Choices: [(a) He disobeyed Pompey but offered to cooperate with the Senate., (b) He
disobeyed Pompey and started a war against Pompey and the Senate., (c) He decided to give
up his army and return to Rome to face punishment.]
Answer index: 1
Subject: Social Studies
Skill: roman-government-monarchy-to-republic
Description: According to present-day historians, the Roman Republic lasted from 509 BCE
to about 27 BCE. The word republic comes from the ancient Roman term res publica. Look
at the meaning of the term res publica. Then answer the question below.
res publica: a community committed to following the same rules and protecting each other’s
things and families for the good of all
Based on the meaning above, which of the following statements describe something similar
to what Romans meant by res publica?
Choices: [(a) a group of friends that do whatever they want, whenever they want, (b) a class
project group where everyone follows the same guidelines and benefits equally from working
together, (c) a soccer team where bad players have to do what the coach says, but the best
players don’t]
Answer index: 1
Subject: Social Studies
Skill: french-and-english-expeditions-part-2
Description: After John Cabot’s expedition, the English government did not sponsor another
expedition to the Americas for more than 50 years. Then, in the mid-1500s, the English
government began sending expeditions again. Read the passage about the events in England
that created new interest in expeditions. Then answer the question below.
In the middle of the 1500s, England’s main source of wealth was trading English cloth in
foreign markets. Thousands of people in England made their livings by producing or selling
cloth, and the English government made money by taxing the sale of cloth. But in 1551,
some foreign powers stopped allowing people to purchase English cloth. Many English
people who worked in the cloth industry lost their jobs, and the government could not raise
as much money.
These conditions created a national crisis. The Queen of England, Elizabeth I, needed to
find new sources of wealth to address the crisis. Queen Elizabeth thought that sending
expeditions to the Americas might be one way to help.
Based on the passage, why did Queen Elizabeth I decide to begin sending expeditions to the
Americas?
Choices: [(a) She wanted to stop Spain from purchasing English cloth., (b) She needed to
find a new way to make money for England after the cloth crisis., (c) She was curious to
learn more about what the Americas looked like.]
Answer index: 1
Subject: Social Studies
Skill: comparing-athens-and-sparta-part
Description: Although city-states such as Athens could trade for food, Sparta was surrounded
by mountains that made trade difficult. So, the Spartans relied on agriculture. The ancient
Greek historian Pausanias described the role of helots, or enslaved people, in Spartan
agriculture. Read the passage. Then complete the text below.
The helots had to bring half of all the crops they grew to the Spartans. Helots who disobeyed
were severely punished. The poet Tyrtaeus compared the helots to donkeys exhausted by a
heavy load, under painful duty to bring their Spartan masters half of the crops from the land
they ploughed and cared for.
Adapted from Pausanias, Description of Greece, translated by W.H.S. Jones and H.A.
Ormerod.
Complete the text.
The helots were enslaved people in Sparta. The Spartans relied on the helots ___.
Choices: [(a) to educate their children, (b) to farm their land and raise crops, (c) to trade
what was farmed, (d) to train their children to farm]
Answer index: 1
Subject: Social Studies
Skill: thomas-edison
Description: Several inventors worked on lightbulbs before Thomas Edison did. How were
Thomas Edison’s lightbulbs different?
Choices: [(a) His lightbulbs were free., (b) His lightbulbs were made from all recycled
materials., (c) His lightbulbs could last for several weeks or months., (d) His lightbulbs came
in different colors.]
Answer index: 2
Subject: Social Studies
Skill: the-revolutionary-war-turning-the-tide-of-war
Description: Both the Continental Army and people on the homefront had trouble paying for
the things that they needed during the war. Why?
Choices: [(a) Inflation caused prices to rise., (b) The Continental Congress stopped printing
Continentals., (c) The British took gold reserves from the Thirteen Colonies., (d) Most of the
money was spent on military supplies.]
Answer index: 0
Table 25: Question examples for each skill (part 12).

--- Page 37 ---

Subject: Social Studies
Skill: foundations-of-maya-civilization
Description: Complete the text.
Archaeologists believe that the ancestors of the Maya first arrived in Central America more
than 12,000 years ago. At first, these people were ___ and traveled long distances to find
food. But over time, they learned to grow crops instead. By at least 1500 BCE, they began to
settle in permanent ___. This was the beginning of the Maya civilization.
Choices: [(a) explorers . . . cities, (b) farmers . . . palaces, (c) hunter-gatherers . . . villages]
Answer index: 2
Subject: Social Studies
Skill: classical-athens-geography-and-society
Description: Complete the text.
For most of its history, ancient Athens ruled itself and was not part of a larger country. In
other words, Athens was a ___.
Choices: [(a) region, (b) city-state, (c) kingdom]
Answer index: 1
Subject: Social Studies
Skill: the-mongol-empire
Description: The founder of the Mongol Empire was a man named Temujin. He was born in
Mongolia in the 1100s. The passage below comes from a Mongolian history text. In the
passage, an older person is telling Temujin what Mongolia was like before he was born.
Read the passage. Then answer the question below.
Before you were born, the stars turned in the heavens. Everyone was fighting. Instead of
sleeping, they robbed each other of their possessions. . . . Instead of resting, they fought
each other. In such a world one did not live as one wished, but rather in constant conflict.
There was no rest, only battle. There was no affection, only mutual slaughter.
...
Adapted from The Secret History of the Mongols, paragraph 254
Based on the passage, which choice best summarizes what Mongolian society was like in the
1100s?
Choices: [(a) Mongolian society was peaceful, but foreign invaders often attacked Mongolia.
As a result, Mongols were often forced to fight, and many Mongols died., (b) People in
Mongolia often fought wars with China, their neighbor. As a result, people often went to
China to fight., (c) People in Mongolia were fighting with one another and stealing each
others’ goods. As a result, people could not live peaceful lives.]
Answer index: 2
Subject: Social Studies
Skill: foundations-of-aztec-civilization
Description: Today, the part of Central America where the Aztec Empire existed is known as
Mesoamerica. There are two ways of defining a region like Mesoamerica:
using a geographic definition, which focuses on an area of land and its features, such as
mountain ranges and bodies of water
using a cultural definition, which focuses on the customs and practices that people living
there share
Which of the following statements uses a geographic definition of Mesoamerica?
Choices:
[(a) Mesoamerica is a place where people used a 260-day calendar., (b)
Mesoamerica is a place in Central America where people built religious temples in the form
of pyramids., (c) Mesoamerica is a region of Central America that includes the Valley of
Mexico and the Yucatan Peninsula.]
Answer index: 2
Subject: Language Arts
Skill: choose-the-uppercase-letter-that-matches-c-k-o-p-s-u-v-w-x-z
Description: Pick the uppercase letter that matches.
k
Choices: [(a) T, (b) R, (c) K]
Answer index: 2
Subject: Language Arts
Skill: choose-the-lowercase-letter-that-matches-c-k-o-p-s-u-v-w-x-z
Description: Pick the lowercase letter that matches.
C
Choices: [(a) c, (b) v, (c) o]
Answer index: 0
Subject: Language Arts
Skill: choose-the-uppercase-letter-that-matches-a-b-d-e-g-h-n-q-r
Description: Pick the uppercase letter that matches. a
Choices: [(a) N, (b) A]
Answer index: 1
Subject: Language Arts
Skill: choose-the-lowercase-letter-that-matches-a-b-d-e-g-h-n-q-r
Description: Pick the lowercase letter that matches. A
Choices: [(a) u, (b) a, (c) n]
Answer index: 1
Subject: Language Arts
Skill: choose-the-lowercase-letter-that-matches-f-i-j-l-m-t-y
Description: Pick the lowercase letter that matches.
L
Choices: [(a) l, (b) k, (c) m]
Answer index: 0
Subject: Language Arts
Skill: choose-the-uppercase-letter-that-matches-f-i-j-l-m-t-y
Description: Pick the uppercase letter that matches.
m
Choices: [(a) H, (b) J, (c) M]
Answer index: 2
Subject: Language Arts
Skill: distinguish-characters-points-of-view
Description: The following texts both describe a school bus ride on the first day of school.
This text is told from the point of view of Jeffrey, a student going to a new school:
...
I felt ready for my first shift as a school bus driver. I turned the long bus at each corner
with ease. My cheerful mood made the students smile. I was proud of myself as the bus
approached the brick school building. My first trip had gone well!
How is Ms. Romero’s point of view different from Jeffrey’s?
Choices: [(a) Ms. Romero describes feeling uneasy about a new experience., (b) Ms. Romero
expresses a feeling of pride about the first day of school.]
Answer index: 1
Subject: Language Arts
Skill: determine-the-meanings-of-words-with-greek-and-latin-roots
Description: What does the word autopilot mean?
Choices: [(a) a tool that pilots use when they want to make the airplane fly faster, (b) a
device that flies an airplane on its own, without a pilot, (c) a map or drawing that shows an
airplane’s route]
Answer index: 1
Subject: Language Arts
Skill: describe-the-difference-between-related-words
Description: What is the difference between being vicious and being mean?
Choices: [(a) being vicious is worse, (b) being mean shows more anger]
Answer index: 0
Subject: Language Arts
Skill: which-word-does-not-rhyme
Description: Which word does not rhyme?
Choices: [(a) pack, (b) pick, (c) sick]
Answer index: 0
Subject: Language Arts
Skill: complete-the-sentence-with-the-correct-sight-word
Description: Complete the sentence.
___ pig is big.
Choices: [(a) That, (b) Went]
Answer index: 0
Subject: Language Arts
Skill: to-have-use-the-correct-form
Description: Complete the sentence.
Mrs. Barton’s rug ___ blue flowers on it.
Choices: [(a) has, (b) have]
Answer index: 0
Subject: Language Arts
Skill: complete-the-sentence-with-a-two-syllable-word
Description: Which word makes more sense in the sentence?
We ride in the ___
Choices: [(a) wagon, (b) robin]
Answer index: 0
Subject: Language Arts
Skill: complete-the-sentence-with-a-three-letter-consonant-blend-word
Description: Which word makes more sense in the sentence?
Look, that big fish is swimming up the ___
Choices: [(a) stream, (b) strict]
Answer index: 0
Subject: Language Arts
Skill: use-subordinating-conjunctions
Description: Complete the sentence with the better conjunction.
___ Joseph arrives soon, we won’t get to the movie on time.
Choices: [(a) Unless, (b) After]
Answer index: 0
Subject: Language Arts
Skill: use-the-correct-homophone
Description: Complete the sentence with the correct homophone.
Given that there were more than one hundred guests at the wedding, how many ___ do you
think Martina and Cooper have received?
Choices: [(a) presence, (b) presents]
Answer index: 1
Subject: Language Arts
Skill: use-words-as-clues-to-the-meanings-of-greek-and-latin-roots
Description: The word millimeter contains the root mille. What does the root mille mean?
Choices: [(a) measure, (b) one hundred, (c) one thousand]
Answer index: 2
Subject: Language Arts
Skill: analogies
Description: Complete the analogy.
Ohio is to United States as Earth is to
Choices: [(a) moon, (b) solar system]
Answer index: 1
Table 26: Question examples for each skill (part 13).

--- Page 38 ---

Subject: Language Arts
Skill: is-it-a-complete-sentence-or-a-fragment
Description: Is this a complete sentence?
Monica speaks four languages.
Choices: [(a) Monica speaks four languages.]
Answer index: 0
Subject: Language Arts
Skill: is-it-a-phrase-or-a-clause
Description: Is the group of words in bold a phrase or a clause?
*Emily’s suitcase was too large to fit in the overhead bin**, so unfortunately she had to check
it.
Choices: [(a) phrase, (b) clause]
Answer index: 1
Subject: Language Arts
Skill: choose-between-subject-and-object-pronouns
Description: Select the correct pronoun to complete the sentence.
"Thanks to your efforts, ___ have emerged as leaders in the energy industry," Mr. Bullock
announced at the company meeting.
Choices: [(a) us, (b) we]
Answer index: 1
Subject: Language Arts
Skill: is-the-sentence-simple-compound-complex-or-compound-complex
Description: Which type of sentence is this?
Henry always approaches difficult tasks enthusiastically, and he frequently motivates others
with his energy and fervor.
Choices: [(a) simple, (b) compound, (c) complex, (d) compound-complex]
Answer index: 1
Subject: Language Arts
Skill: analogies-challenge
Description: Complete the analogy.
teacher is to instructor as doctor is to
Choices: [(a) profession, (b) physician, (c) medicine]
Answer index: 1
Subject: Language Arts
Skill: use-time-order-words
Description: Complete the text with the better word.
, Jerry jogs for a mile. Then, he rests for ten minutes.
Choices: [(a) First, (b) Finally]
Answer index: 0
Subject: Language Arts
Skill: choose-reasons-to-support-an-opinion
Description: Read the opinion below.
Swamps should be protected and valued.
Select the reason that best supports this opinion.
Choices: [(a) Swamps do an excellent job of cleaning an area’s water supply., (b) Many
dangerous creatures, such as alligators and poisonous snakes, live in swamps.]
Answer index: 0
Subject: Language Arts
Skill: is-it-a-complete-sentence-or-a-run-on
Description: Which is a **run-on sentence**?
Choices: [(a) The heart is a symbol of love., (b) She went to the tailor, he sewed her pants.]
Answer index: 1
Subject: Language Arts
Skill: read-about-famous-people
Description: Review the text.
title: Becoming Amazing
...
Copeland’s success made her a role model for others, too. She was on the cover of Time
magazine as one of the "100 Most Influential People" in 2015. She wrote a best-selling book
about her life, called Life in Motion: An Unlikely Ballerina. She also wrote a children’s
book, Firebird, in which she tells others like herself that they, too, can become amazing.
Which is the best summary of the text?
Choices: [(a) Misty Copeland beat many challenges to become a famous ballet dancer. She
started later than most dancers and suffered broken bones. But with the help of a coach and a
ballet teacher, she became the first African American principal dancer for ABT. She also
became an author and role model., (b) Misty Copeland never stopped working to become a
famous ballet dancer. She started training very young and became an amazing dancer by age
thirteen. After becoming the first African American woman dancer for ABT, she injured
herself badly, so she became a model and an author instead., (c) Misty Copeland started
dancing at age thirteen, much later than most ballet dancers. She was encouraged by her
middle-school drill team coach and a ballet teacher at the Boys & Girls Club. With a lot of
hard work, she became a professional dancer with ABT at the age of eighteen.]
Answer index: 0
Subject: Language Arts
Skill: choose-the-synonym
Description: Which word is a synonym of **bag**?
Choices: [(a) sack, (b) contain]
Answer index: 0
Subject: Language Arts
Skill: identify-story-elements
Description: Review the story.
title: Contest on Mars Colony
...
He could see the kids taking deep breaths of the forest air. Whether or not he won, their
smiles were prize enough for him.
What is the **solution** to the problem in the story?
Choices: [(a) Axel comes up with a high-tech app idea., (b) Zane invents a new alarm that
will play beautiful music instead of buzzing., (c) Axel realizes he can improve the Colony by
growing a forest., (d) Axel’s father decides they’ll move back to Earth.]
Answer index: 2
Subject: Language Arts
Skill: use-academic-vocabulary-in-context
Description: Look at the word **residence** in the passage below.
In many homes, basements are used for ordinary activities, such as washing clothes. The
U.S. president’s basement is much more interesting. In the White House, the president’s
**residence**, the basement contains a woodshop and a dentist’s office. And when the
president’s family wants to have some fun, they can go bowling in their own basement
bowling alley!
What is the meaning of **residence** as used in the passage?
Choices: [(a) a place where someone lives, (b) a place where parties are held, (c) a place that
people like to visit]
Answer index: 0
Subject: Language Arts
Skill: use-adjectives-to-compare
Description: Complete the sentence with the correct form of the adjective.
The traffic on Main Street is much ___ than the traffic on the highway.
Choices: [(a) slower, (b) slowest]
Answer index: 0
Subject: Language Arts
Skill: select-the-words-that-dont-belong
Description: Select the place that "doesn’t" belong.
Choices: [(a) library, (b) meadow, (c) forest, (d) field]
Answer index: 0
Subject: Language Arts
Skill: capitalizing-titles
Description: Which correctly shows the title of a poem?
Choices: [(a) "The Mountain and the Squirrel", (b) "the Mountain and the Squirrel"]
Answer index: 0
Subject: Language Arts
Skill: read-historical-fiction
Description: Read the story.
title: Strangers on My Shore
...
Many changes have come in the 250 years that have passed since that day. Now, big cities dot
my landscape, and two-legged creatures fly from around the world to visit me. Though many
now call me New Zealand, I am still the same island, shimmering green under the clouds.
After all these years, my waters and my mountains remain, and my bays and rivers endure.
Based on paragraphs 1 through 3, how does the fact that the narrator is an island rather than a
person affect this telling of New Zealand’s history?
Choices: [(a) It allows the narrator to compare the landforms in New Zealand to other
places in the Pacific., (b) It allows the story to start long before the arrival of humans, with
the formation of the land., (c) It allows the story to focus only on the geography of New
Zealand, not the people who live there., (d) It allows the narrator to refer to the island by the
present-day name of "New Zealand."]
Answer index: 1
Table 27: Question examples for each skill (part 14).

--- Page 39 ---

Subject: Language Arts
Skill: revise-the-sentence-using-a-stronger-verb
Description: Read the sentence.
After a difficult climb, Madelyn **went** back down the hill.
Now, revise the sentence to show that Madelyn was **clumsy**.
After a difficult climb, Madelyn ___ back down the hill.
Choices: [(a) floated, (b) stumbled, (c) plunged]
Answer index: 1
Subject: Language Arts
Skill: use-the-correct-subject-or-verb
Description: Complete the sentence with the best **verb**.
Both of us ___ the banjo, but Jenna also plays the flute.
Choices: [(a) plays, (b) play]
Answer index: 1
Subject: Language Arts
Skill: choose-between-personal-and-reflexive-pronouns
Description: Select the best pronoun to complete the sentence.
Will you please give ___ directions to the Lanberry Community Center?
Choices: [(a) me, (b) myself]
Answer index: 0
Subject: Language Arts
Skill: choose-between-subject-and-object-personal-pronouns
Description: Select the correct pronoun to complete the sentence.
When Tara is upset, she always confides in ___.
Choices: [(a) he, (b) him]
Answer index: 1
Subject: Language Arts
Skill: choose-the-best-concluding-sentence
Description: Read the paragraph. Then, add the better concluding sentence.
Over the course of his career, Mel Blanc provided the voices for hundreds of cartoon
characters. One of his most famous characters was Bugs Bunny. Bugs Bunny was a charming
yet fearless rabbit who was famous for saying "What’s up, Doc?" Blanc described his
process for how he came up with Bugs Bunny’s voice. First, he looked at sketches, or rough
drawings, of the character. Then, he looked at a set of pictures called a storyboard. The
storyboard showed how Bugs Bunny would behave in a cartoon. The cartoon’s creators told
Blanc that Bugs Bunny’s character was a "tough little stinker." Blanc thought about all the
tough-sounding accents he had heard. After some experimenting, Blanc finally brought Bugs
Bunny’s voice to life. ___
Choices: [(a) Similarly, Blanc is known for creating sound effects., (b) This process clearly
worked, because Bugs Bunny became one of Blanc’s most recognized characters.]
Answer index: 1
Subject: Language Arts
Skill: create-compound-sentences
Description: Form a compound sentence.
Sarah ___ at the rink.
Choices: [(a) doesn’t play ice hockey, but she figure skates, (b) Montoya, famous for her
graceful jumps, can be seen]
Answer index: 0
Subject: Language Arts
Skill: identify-the-narrative-point-of-view
Description: Which point of view does the narrator use in the passage?
A few days after this I had to go out with Ginger in the carriage. I wondered how we should
get on together; but except laying her ears back when I was led up to her, she behaved very
well.
From Anna Sewell, Black Beauty. Copyright 1999 by Dover Publications
Choices: [(a) first person, (b) second person, (c) third person]
Answer index: 0
Subject: Language Arts
Skill: is-the-word-an-adjective-or-adverb
Description: Is the word in bold an adjective or an adverb?
Zoe tried on a **violet** gown with cap sleeves.
Choices: [(a) adjective, (b) adverb]
Answer index: 0
Subject: Language Arts
Skill: is-it-a-complete-sentence-a-fragment-or-a-run-on
Description: Which is a **run-on sentence**?
Choices: [(a) I mopped the floor, Mom washed all the dishes., (b) The girls and boys swung
on the swings.]
Answer index: 0
Subject: Language Arts
Skill: use-actions-and-dialogue-to-understand-characters
Description: Read the sentences.
Jaylen asked that the math award be given to his whole team instead of just him. "I couldn’t
have done it without them," he said.
Based on these sentences, what is Jaylen probably like?
Choices: [(a) humble, (b) snobby]
Answer index: 0
Subject: Language Arts
Skill: use-adverbs-to-compare
Description: Complete the sentence with the correct form of the adverb.
Wesley can sing the ___ of the three soloists.
Choices: [(a) lower, (b) lowest]
Answer index: 1
Subject: Language Arts
Skill: which-definition-matches-the-sentence
Description: What does **bloom** mean in this sentence?
Mr. Herman said, "I think Brandon will bloom into a successful and confident young man."
Choices: [(a) **bloom** "verb" to grow, (b) **bloom** "noun" a blossom]
Answer index: 0
Subject: Language Arts
Skill: is-the-sentence-in-the-past-present-or-future-tense
Description: Which tense does the sentence use?
Erica parked her scooter in front of the store.
Choices: [(a) past tense, (b) present tense, (c) future tense]
Answer index: 0
Subject: Language Arts
Skill: formatting-and-capitalizing-titles
Description: Which sentence is correct?
Choices: [(a) Almost everyone watched the TV show "Foster’s Home for Imaginary Friends.",
(b) Almost everyone watched the TV show "Foster’s Home for Imaginary Friends".]
Answer index: 1
Subject: Language Arts
Skill: choose-the-antonym
Description: Which word is an antonym of **succeed**?
Choices: [(a) fail, (b) victory]
Answer index: 0
Subject: Language Arts
Skill: choose-the-best-topic-sentence
Description: Read the paragraph. Then, add the better topic sentence.
___ In slacklining, people build strength and balance as they practice walking across a
narrow, stretchy strip of fabric. As in tightrope walking, it takes a lot of practice to stay
steady on this line. When slackliners feel confident enough, they may test their balance by
slacklining higher up. Some even perform tricks on a slackline.
Choices: [(a) Some people practice yoga poses on slacklines., (b) Slacklining is a sport that
uses balance and strength.]
Answer index: 1
Subject: Language Arts
Skill: read-poetry
Description: Review the poem.
My Model Car
The hours piled on,
As I sprawled out on my carpet,
Tinkering with tweezers,
Fiddling with rubber bands,
Trying to make my model car come to life.
Finally, eyes bleary, I went for a walk,
Leaving the car parts behind.
I took in the details of the neighborhood,
The trills and chirps of birds in the trees,
The thick, smoky smell of a grill
Fired up in my neighbor’s yard.
I came back and opened my door.
Hoping the car had assembled itself. No, but—
I suddenly saw the parts with new eyes,
My mind clear and ready.
My tools bent and twisted the pieces
Like they’d always known what to do.
What is the main theme of the poem?
Choices: [(a) It’s important to ask for help with a project when you need it., (b) Taking a
break from a task can help you approach it in a new way., (c) Make sure you understand all
the steps of your task before you start.]
Answer index: 1
Subject: Language Arts
Skill: show-character-emotions-and-traits
Description: You are writing a story about Devon, who hears some bad news. Choose the
best description to show that Devon is **disappointed**.
Choices: [(a) Devon swallowed hard and tried to force herself to smile., (b) "Okay," Devon
said, continuing to chop carrots.]
Answer index: 0
Table 28: Question examples for each skill (part 15).

--- Page 40 ---

Subject: Language Arts
Skill: identify-text-structures
Description: Read the text.
Although there are many kinds of writing, most people divide texts into two different types:
fiction and nonfiction. Fiction means stories that are made up. "Charlotte’s Web" is fiction
because, of course, spiders and pigs don’t really talk. Nonfiction, however, gives you facts
about the real world. You can find nonfiction books about history, science, real people,
animals, and many other topics. Nonfiction also includes newspapers and textbooks, while
fiction includes stories, plays, and novels. Reading both fiction and nonfiction can be fun and
educational.
Which text structure does the text use?
Choices: [(a) cause-effect, (b) compare-contrast]
Answer index: 1
Subject: Language Arts
Skill: which-sentence-matches-the-definition
Description: Which sentence uses this meaning of **concrete**?
*concrete** "adjective" specific and real
Choices: [(a) His fingerprints were **concrete** proof that he had opened the safe., (b) We
can’t walk on the sidewalk because the **concrete** is still drying.]
Answer index: 0
Subject: Language Arts
Skill: determine-the-meaning-of-idioms-from-context-set-1
Description: What is the meaning of **on the tip of one’s tongue**?
I can’t quite remember the name of that magician we saw perform in Las Vegas, but it is
**on the tip of my tongue**.
Choices: [(a) almost remembered, (b) a certainty]
Answer index: 0
Subject: Language Arts
Skill: use-guide-words
Description: Which word would you find on a dictionary page with the following guide
words?
*skate** - **squire**
Choices: [(a) spare, (b) station]
Answer index: 0
Subject: Language Arts
Skill: use-context-to-identify-the-meaning-of-a-word
Description: Read the passage and then answer the question.
The Great Pyramid of Giza is the largest of the ancient Egyptian pyramids. When completed
around 2560 BCE, it stood 481 feet high, as tall as a modern 44-story building. The Great
Pyramid was the world’s tallest building for more than three thousand years. More than two
million huge stone blocks were used to construct it. The builders of the pyramid positioned it
**meticulously** so that it perfectly faces true north. Scientists aren’t sure how the ancient
Egyptians knew how to place the base. Experts also disagree about how those huge blocks
were moved into place. They don’t even fully understand the design of the inside of the
pyramid. More work must be done to solve these mysteries.
What is the meaning of **meticulously** as used in the passage?
Choices: [(a) with many people pushing, (b) in a great hurry, (c) happily, without any
hesitation, (d) carefully, with attention to detail]
Answer index: 3
Subject: Language Arts
Skill: punctuating-dialogue
Description: Which sentence is correct?
Choices: [(a) "Please hire a carpenter to finish our basement", Mrs. Huffman urged., (b)
"Please hire a carpenter to finish our basement," Mrs. Huffman urged.]
Answer index: 1
Subject: Language Arts
Skill: determine-the-meanings-of-similes-and-metaphors
Description: What is the meaning of the simile?
Linda’s typing was like a tap dancer performing onstage.
Choices: [(a) Linda made rapid tapping noises., (b) Linda made her performance on the
stage.]
Answer index: 0
Subject: Language Arts
Skill: use-key-details-to-determine-the-main-idea
Description: Look at these details from a paragraph about the same topic:
By taking music lessons, students learn to read sheet music.
...
Through music lessons, students can learn about music from other countries.
Choose the main, or central, idea that ties all the details together.
Choices: [(a) Music lessons introduce students to many types of music., (b) Music lessons
teach more than just how to play an instrument., (c) Piano lessons are one of the most popular
types of music lesson.]
Answer index: 1
Subject: Language Arts
Skill: choose-between-adjectives-and-adverbs
Description: Choose the word that best describes the adjective in bold.
As a wedding gift, Elena gave the couple a quilt that was ___ **sewn** by hand.
Choices: [(a) full, (b) fully]
Answer index: 1
Subject: Language Arts
Skill: read-realistic-fiction
Description: Read the story.
title: The Artist’s Secret
...
Destiny smiled. Then she reached for her palette, so she could start on C.
Based on paragraphs 1 and 2, how does Destiny probably feel about the art project at the
beginning of the story?
Choices: [(a) She cares about it turning out just right., (b) She wants to finish it as quickly as
possible., (c) She views it as a competition that she is winning., (d) She is annoyed about
having to mix paint colors.]
Answer index: 0
Subject: Language Arts
Skill: use-the-meanings-of-words-as-clues-to-the-meanings-of-greek-and-latin-roots
Description: A biography is a written account of someone’s life. What does the root
**graph** mean?
Choices: [(a) look at or observe, (b) write or draw, (c) measure]
Answer index: 1
Subject: Language Arts
Skill: use-coordinating-conjunctions
Description: Complete the sentence with the best conjunction.
Pam wants to dye her hair purple ___ red.
Choices: [(a) or, (b) but]
Answer index: 0
Subject: Language Arts
Skill: identify-similes-and-metaphors
Description: Does the sentence use a simile or a metaphor?
Mrs. Boyer is kind, and her heart is gold.
Choices: [(a) simile, (b) metaphor]
Answer index: 1
Subject: Language Arts
Skill: use-greek-and-latin-roots-as-clues-to-the-meanings-of-words
Description: The root **vis** means "see or look at". What does the word **visual** mean?
Choices: [(a) relating to hearing or sound, (b) relating to seeing or sight, (c) relating to flavor
or taste]
Answer index: 1
Subject: Language Arts
Skill: interpret-the-meaning-of-an-allusion-from-its-source
Description: Read the source of the allusion.
In the fairy tale, Cinderella is a poor young woman who is treated badly. However, she later
marries a prince and becomes a loved and respected princess.
What is the meaning of the allusion in the sentence below?
Choices: [(a) an amazing improvement, (b) a journey without troubles]
Answer index: 0
Subject: Language Arts
Skill: positive-and-negative-connotation
Description: Which phrase has a more **negative** connotation?
Choices: [(a) a warm room, (b) a stuffy room]
Answer index: 1
Table 29: Question examples for each skill (part 16).

--- Page 41 ---

Subject: Language Arts
Skill: draw-inferences-from-a-text
Description: Read the text.
Kari looked under the table. Then she searched the whole room.
"You have got to be kidding!" Kari shouted.
Grumbling, Kari tore the puzzle apart and put it back in the box. On the top of the box, she
crossed out 1000 and wrote 999 above it.
Based on the text, which sentence is more likely to be true?
Choices: [(a) Kari doesn’t like building puzzles., (b) Kari’s puzzle is missing a piece.]
Answer index: 1
Subject: Language Arts
Skill: is-the-sentence-simple-or-compound
Description: Which is a **compound sentence**?
Choices: [(a) Jayden grew too many pumpkins, so he sold the extras at the market., (b)
British general John Burgoyne surrendered to American forces at the Battle of Saratoga.]
Answer index: 0
Subject: Language Arts
Skill: identify-elements-of-poetry
Description: Choose the poem that uses **end rhyme**.
Choices: [(a) I break a staff. I break the tough branch. I know no light in the woods. I have
lost pace with the winds., (b) Sign of a nation, great and strong Toward her people from
foreign wrong: Pride and glory and honor,—all Live in the colors to stand or fall.]
Answer index: 1
Subject: Language Arts
Skill: read-about-business-and-technology
Description: Review the text.
title: Where Are You?
...
GPS has also become very useful in the field of science. Scientists have figured out ways to
use GPS for monitoring earthquakes and volcanoes. GPS can also be used to measure water
levels and snowfall. While working with wild animals, some animal researchers also use
GPS devices. These scientists can attach small devices onto animals to track the animals’
movements and gather important data about them. Who knows how GPS will help us next?
Which is the best summary of the text?
Choices: [(a) GPS receivers help people find their way. They work by sending radio signals
to satellites in space. Drivers, people enjoying outdoor sports, and emergency workers
all use GPS. GPS can also be used for other purposes, like for tracking animals and for
science research., (b) "GPS" stands for Global Positioning System. GPS works anywhere on
Earth, except deep in caves and underwater. People use GPS every day to drive and play
sports. They also use GPS to find lost pets., (c) GPS devices have become very important in
our world. People use them for driving and outdoor sports. Scientists use them to monitor
earthquakes, volcanoes, and the phases of the moon. GPS can also be used to remind people
to walk their pets.]
Answer index: 0
Subject: Language Arts
Skill: read-about-history
Description: Read the text.
title: A Whale of a Record
...
It might seem incredible that just one album could help save the lives of so many whales. But
remember that Songs of the Humpback Whale was no ordinary record. This one-of-a-kind
album revealed secrets about whales that had long been hidden beneath the waves. It allowed
these amazing and mysterious creatures to finally share their songs with the human world.
What is the text about?
Choices: [(a) It is about how musicians recorded an album to encourage people to ban
deep-sea whaling., (b) It is about how whales learned to use sounds to communicate after
biologists played them recordings., (c) It is about how people changed their mind about
recordings of nature after hearing an album of whale songs., (d) It is about how an album of
whale recordings helped increase protection for whales around the world.]
Answer index: 3
Subject: Language Arts
Skill: identify-plurals-singular-possessives-and-plural-possessives
Description: What is the word in bold?
Are there any **statues** in your town?
Choices: [(a) a singular possessive noun, (b) a plural noun]
Answer index: 1
Subject: Language Arts
Skill: analyze-the-effects-of-figures-of-speech-on-meaning-and-tone
Description: Read the text. The figure of speech is shown in bold.
Then I knew that even though **nobody in the world** figured that old car had any good
purpose, Ob knew there was some real reason to let it sit. And when May died, he figured
out what it was.
I never saw two people love each other so much.
From Cynthia Rylant, Missing May. Copyright 1992 by Cynthia Rylant
What does this example of **hyperbole** tell you?
Choices: [(a) It suggests that very few people thought the car had a purpose., (b) It suggests
that the car travels around the world.]
Answer index: 0
Subject: Language Arts
Skill: determine-the-meanings-of-greek-and-latin-roots
Description: What does the root **tract** mean?
Choices: [(a) bend or curve, (b) pull or drag, (c) far away]
Answer index: 1
Subject: Language Arts
Skill: is-it-a-telling-sentence-or-an-asking-sentence
Description: What kind of sentence is this?
My father reads to me.
Choices: [(a) telling sentence, (b) asking sentence]
Answer index: 0
Subject: Language Arts
Skill: find-the-vowel-in-the-word
Description: Find the vowel.
Choices: [(a) o, (b) n]
Answer index: 0
Subject: Language Arts
Skill: complete-the-sentence-with-the-correct-short-vowel-word
Description: Which word makes the most sense in the sentence?
The bug is on his ___.
Choices: [(a) nap, (b) leg]
Answer index: 1
Subject: Language Arts
Skill: complete-the-rhyme
Description: Complete the rhyme.
The men sit in the ___.
Choices: [(a) den, (b) back]
Answer index: 0
Subject: Language Arts
Skill: capitalize-the-first-letter-of-a-sentence
Description: Complete the sentence with an uppercase letter.
___ans can go fast.
Choices: [(a) V, (b) v]
Answer index: 0
Subject: Language Arts
Skill: who-what-when-where-or-why
Description: Pick the right question word.
___ did your mom go?
Choices: [(a) Who, (b) Where]
Answer index: 1
Subject: Language Arts
Skill: what-am-i
Description: Answer the riddle.
I am small.
...
What am I?
Choices: [(a) a baby, (b) a box]
Answer index: 0
Subject: Language Arts
Skill: read-questions-with-short-vowel-words
Description: Answer the question.
Can a wig jog?
Choices: [(a) yes, (b) no]
Answer index: 1
Subject: Language Arts
Skill: choose-the-uppercase-letter-that-matches-review
Description: Pick the uppercase letter that matches.
x
Choices: [(a) X, (b) W]
Answer index: 0
Subject: Language Arts
Skill: find-the-action-verb
Description: Find the verb. A verb shows an action.
Choices: [(a) tree, (b) grow]
Answer index: 1
Subject: Language Arts
Skill: choose-the-lowercase-letter-that-matches-review
Description: Pick the lowercase letter that matches.
V
Choices: [(a) n, (b) v]
Answer index: 1
Subject: Language Arts
Skill: find-the-complete-sentence
Description: Find the complete sentence.
Choices: [(a) car, (b) We ate the cake.]
Answer index: 1
Table 30: Question examples for each skill (part 17).

--- Page 42 ---

Subject: Language Arts
Skill: which-word-is-not-like-the-others
Description: Which word is not like the others?
Choices: [(a) big, (b) tall, (c) little, (d) nice]
Answer index: 3
Subject: Language Arts
Skill: complete-the-sentence-with-the-correct-sight-word-sets-1-2-3
Description: Complete the sentence.
I did not want to trick ___.
Choices: [(a) has, (b) as, (c) them]
Answer index: 2
Subject: Language Arts
Skill: complete-the-sentence-with-the-correct-sight-word-sets-4-5-6-7
Description: Complete the sentence.
I ate a hot dog ___ went to bed.
Choices: [(a) four, (b) more, (c) then]
Answer index: 2
Subject: Language Arts
Skill: use-the-correct-modal-verb
Description: Select the modal verb that best completes the sentence.
The coach ___ let Mark join the team if it weren’t so late in the season.
Choices: [(a) would, (b) will]
Answer index: 0
Subject: Language Arts
Skill: use-the-perfect-verb-tenses
Description: Complete the sentence with the correct helping verb or verbs.
When I walked by Sophia’s desk, I saw that she ___ fallen asleep!
Choices: [(a) had, (b) will have]
Answer index: 0
Subject: Language Arts
Skill: determine-the-meaning-of-idioms-from-context-set-2
Description: What is the meaning of **get one’s feet wet**?
Mrs. Tyler is a professional singer who **got her feet wet** by singing in the school choir
as a kid.
Choices: [(a) to get soaked or messy, (b) to start learning something]
Answer index: 1
Subject: Language Arts
Skill: choose-between-the-past-tense-and-past-participle
Description: Complete the sentence with the correct form of the verb.
I swept up crumbs from the cookie Barry had ___.
Choices: [(a) eaten, (b) ate]
Answer index: 0
Subject: Language Arts
Skill: identify-the-meaning-of-idioms-and-adages-set-2
Description: What is the meaning of **if you can’t stand the heat, get out of the kitchen**?
Choices: [(a) follow the customs of the place where you are, (b) don’t take on a job or task if
it’s too much for you]
Answer index: 1
Subject: Language Arts
Skill: is-the-sentence-declarative-interrogative-imperative-or-exclamatory
Description: What kind of sentence is this?
Nora is reading a magazine about skateboarding.
Choices: [(a) interrogative, (b) declarative]
Answer index: 1
Subject: Language Arts
Skill: use-the-progressive-verb-tenses
Description: Complete the sentence with the correct helping verb or verbs.
"We ___ eating dinner at seven o’clock, so don’t be late," Mrs. Christensen said.
Choices: [(a) were, (b) will be]
Answer index: 1
Subject: Language Arts
Skill: what-does-the-modal-verb-show
Description: What does the modal verb show? Select the best answer choice.
Bernie and Gary **will** visit Yosemite National Park next summer.
Choices: [(a) a request for permission, (b) future action]
Answer index: 1
Subject: Language Arts
Skill: identify-the-meaning-of-idioms-and-adages-set-1
Description: What is the meaning of **cut corners**?
Choices: [(a) to accidentally take the edges off something, (b) to take shortcuts when
working]
Answer index: 1
Subject: Language Arts
Skill: use-thesaurus-entries
Description: Look at this thesaurus entry:
*abstain**
...
Synonyms: deny, forgo, give up, quit, refrain
Which is something you **abstain** from?
Choices: [(a) something you almost always do, (b) something you choose not to do]
Answer index: 1
Subject: Language Arts
Skill: words-with-sub
Description: Which might be a **subtopic** within a discussion of the Revolutionary War?
Choices: [(a) the Declaration of Independence, (b) U.S. history]
Answer index: 0
Subject: Language Arts
Skill: words-with-pre
Description: What helps **prevent** a cold?
Choices: [(a) washing your hands frequently, (b) taking cold medicine]
Answer index: 0
Subject: Language Arts
Skill: words-with-less
Description: Why might you make a **careless** mistake in your work?
Choices: [(a) because you aren’t paying attention, (b) because you don’t understand
something]
Answer index: 0
Subject: Language Arts
Skill: words-with-un-dis-in-im-and-non
Description: Which is an **infrequent** visitor?
Choices: [(a) one you often see, (b) one you rarely see]
Answer index: 1
Subject: Language Arts
Skill: words-with-re
Description: Why might you **reattempt** a challenge?
Choices: [(a) because you didn’t succeed the first time, (b) because it’s a new one]
Answer index: 0
Subject: Language Arts
Skill: use-the-correct-pair-of-correlative-conjunctions
Description: Complete the sentence with the correct correlative conjunctions.
Kurt’s horse is in ___ the barn ___ the pasture right now.
Choices: [(a) not only . . . but also, (b) either . . . or]
Answer index: 1
Subject: Language Arts
Skill: words-with-ful
Description: How would you feel after a **restful** day?
Choices: [(a) recharged, (b) exhausted]
Answer index: 0
Subject: Language Arts
Skill: compound-subjects-and-objects-with-personal-pronouns
Description: Select the correct pronoun to complete the sentence.
At the garage sale, ___ and Warren hoped to find some good books.
Choices: [(a) she, (b) her]
Answer index: 0
Subject: Language Arts
Skill: determine-the-themes-of-short-stories
Description: Read the following story.
Paolo walked out on the dock and looked down into the water. "I only like to swim in pools.
I’m not swimming in there," he said.
"Well, I’m going to," his mom said. "There’s not much else to do here!"
Paolo’s little sister, Celia, was standing next to him. "If Paolo’s not going in, I’m not
swimming in there either," Celia said.
Paolo’s mom looked at Paolo with a raised eyebrow. "That’s fine," she said. "You two don’t
have to swim. But remember, there’s no internet here and no TV."
Paolo marched back to the cabin and sat in a lawn chair. He crossed his arms and frowned.
"This is going to be an awful vacation", he thought. No Wi-Fi, nothing to do.
Celia followed him, sitting in a chair and crossing her arms, too. "I’m bored!" Celia said.
Meanwhile, their mom had gone into the cabin to change. Soon she emerged, carrying an
armful of goggles and towels. "I’m going for a dip. Are you "sure" you don’t want to go?"
she asked.
Celia glanced at Paolo.
"I’m sure," said Paolo.
"No way!" added Celia.
Paolo sat in the chair and stared across the lake. Celia did too, but soon she grew restless.
She got up, walked up and down the dock, and finally sat down, watching her mom.
Seeing this, Paolo felt bad. He went inside and put on his bathing suit. Then he walked out to
the dock where Celia was sitting. When their mom swam up to them, Paolo apologized. "I’ll
swim with you, Mom. I’m sorry I was crabby. The water actually looks nice," he said.
Celia looked at Paolo. Then she ran to the cabin to change into her swimsuit, too.
Which of the following best describes the main theme or lesson of the story?
Choices: [(a) Set a good example for people who look up to you., (b) People today take
technology for granted.]
Answer index: 0
Table 31: Question examples for each skill (part 18).

--- Page 43 ---

Subject: Language Arts
Skill: words-with-able-and-ible
Description: Which item is not a **collectible**?
Choices: [(a) an ordinary spiral notebook, (b) a rare comic book]
Answer index: 0
Subject: Language Arts
Skill: use-the-correct-frequently-confused-word
Description: Complete the text with the correct word.
Rhianna made a wire sculpture of a tree for her art project. She used steel wool to make ___
leaves.
Choices: [(a) its, (b) it’s]
Answer index: 0
Subject: Language Arts
Skill: words-with-mis
Description: Which type of behavior shouldn’t cause **mistrust**?
Choices: [(a) suspicious behavior, (b) honest behavior]
Answer index: 1
Subject: Language Arts
Skill: which-sentence-is-more-formal
Description: Which sentence is more formal?
Choices: [(a) Visitors are advised that admission to the aircraft museum has been raised by
two dollars., (b) FYI, admission to the aircraft museum has been raised by two dollars.]
Answer index: 0
Subject: Language Arts
Skill: is-the-sentence-simple-compound-or-complex
Description: Which is a **simple sentence**?
Choices: [(a) Although I would rather visit Italy, I’m excited about going to Panama this
summer., (b) The thermometer and the cough syrup are in the medicine cabinet next to the
cotton balls.]
Answer index: 1
Subject: Language Arts
Skill: choose-topic-sentences-for-expository-paragraphs
Description: Read the paragraph. Then, add the better topic sentence.
___ In fact, more than half of the planet is covered just by oceans. Earth also has many lakes,
rivers, and swamps full of freshwater. But there’s even more freshwater that is frozen in
glaciers and icecaps. Add to that all of the water that’s underground or in the air, and you’ve
got one wet planet!
Choices: [(a) Most of the Earth is covered in water., (b) The highest point on Earth is Mount
Everest.]
Answer index: 0
Subject: Language Arts
Skill: is-the-sentence-a-statement-question-command-or-exclamation
Description: What kind of sentence is this?
Bobby gave me the best present!
Choices: [(a) an exclamation, (b) a statement]
Answer index: 0
Subject: Language Arts
Skill: does-the-adjective-tell-you-what-kind-or-how-many
Description: Look at the adjective in **bold**. Does it tell you "what kind" or "how many"?
Maria will need **seven** stamps.
Choices: [(a) what kind, (b) how many]
Answer index: 1
Subject: Language Arts
Skill: determine-the-meanings-of-similes
Description: What is the meaning of the simile?
Just as a soft breeze rocks the trees, Mrs. Middleton rocked the baby to sleep.
Choices: [(a) Mrs. Middleton rocked the baby outside., (b) Mrs. Middleton rocked the baby
gently.]
Answer index: 1
Subject: Language Arts
Skill: is-the-noun-singular-or-plural
Description: Is the noun in bold singular or plural?
Lamar shouted when his **foot** touched the hot water.
Choices: [(a) singular, (b) plural]
Answer index: 0
Subject: Language Arts
Skill: use-the-correct-article-a-or-an
Description: Complete the sentence with the best article.
Mrs. Casey keeps the tools in ___ shed.
Choices: [(a) an, (b) a]
Answer index: 1
Subject: Language Arts
Skill: determine-the-themes-of-myths-fables-and-folktales
Description: Read the following fable by Aesop.
A fox one day spotted a beautiful bunch of ripe grapes hanging from a vine. The grapes
seemed ready to burst with juice. The fox’s mouth watered, and he gazed longingly at them.
The bunch hung up high, far out of the fox’s reach. He tried to jump and grab it. The first
time he jumped, he was still far away. So he walked off a short distance and took a running
leap. But he fell short once more. Again and again he tried, but he simply could not reach the
grapes.
After a long time, he sat down and looked at the grapes in anger.
"What a fool I am," he said. "I am wearing myself out, and for what? This is just a bunch of
terrible, sour grapes."
And away he walked with his nose in the air.
What is the main theme or lesson of the fable?
Choices: [(a) Sometimes fruit is sour, not sweet., (b) People pretend they don’t want things
they can’t have.]
Answer index: 1
Subject: Language Arts
Skill: to-be-use-the-correct-form
Description: Complete the sentence with the correct **present tense** form of **to be**.
They ___ upstairs in Sofia’s bedroom.
Choices: [(a) are, (b) am]
Answer index: 0
Subject: Language Arts
Skill: read-about-famous-places
Description: Review the third paragraph.
The Golden Gate Bridge is one of the most famous bridges in the world. Its tall frame, two
large towers, and orange color make the bridge easy to recognize. Yet as the Golden Gate
Bridge was being built, people disagreed about what the bridge should look like.
People were worried that San Francisco’s thick fog would make the bridge hard to see. The
U.S. Navy wanted the bridge to stand out so ships and airplanes wouldn’t collide with it.
They wanted the bridge to have wide black and yellow stripes, like a bumblebee! Irving
Morrow was one of the bridge designers. He did not like the idea of a striped bridge. Morrow
did not want a plain black or gray bridge either, though. He thought a dark bridge would
make the Golden Gate seem smaller than it was.
When the bridge’s parts were delivered to San Francisco, they had an orange color. The
bridge workers were supposed to paint a new color over the orange. But Morrow was still
unsure of what color that would be. He looked at the orange bridge parts and decided that the
color would be perfect! Morrow thought the orange would stand out well against the ocean
and the sky.
Finally, the difficult decision had been made. A red-orange Golden Gate Bridge was bright
enough for ships and planes to see. The color made the bridge appear grand and tall. Over
the years, fresh paint has been needed. But the color remains the same orange that was
supposed to be painted over many years ago.
Based on the text, why did Irving Morrow think orange would be a good color for the Golden
Gate Bridge?
Choices: [(a) The parts were already orange, so no extra work would be needed., (b) The
color would make the bridge stand out from the sky and ocean., (c) Using orange paint on
orange parts would be cheaper.]
Answer index: 1
Subject: Language Arts
Skill: does-the-adverb-tell-you-how-when-or-where
Description: Look at the adverb in bold. Does it tell you "how" or "where"?
Mr. Olson lives **upstairs**.
Choices: [(a) how, (b) where]
Answer index: 1
Subject: Language Arts
Skill: which-word-is-a-noun
Description: Is the word in bold a noun?
The captain turned the ship around and **sailed** north.
Choices: [(a) yes, (b) no]
Answer index: 1
Table 32: Question examples for each skill (part 19).

--- Page 44 ---

Subject: Language Arts
Skill: identify-the-irregular-past-tense-ii
Description: Which sentence is in the past tense?
Choices: [(a) Susan **feeds** her bird., (b) Susan **fed** her bird.]
Answer index: 1
Subject: Language Arts
Skill: which-sentence-is-in-the-regular-past-tense
Description: Which sentence is in the past tense?
Choices: [(a) Cassie **acted** happy., (b) We **discover** hidden treasures.]
Answer index: 0
Subject: Language Arts
Skill: which-sentence-uses-an-antonym
Description: Read the sentence. Select the sentence that uses an antonym in place of the
word in bold.
Bella’s dad has always been **short**.
Choices: [(a) Bella’s dad has always been **tall**., (b) Bella’s dad has always been
**shy**.]
Answer index: 0
Subject: Language Arts
Skill: use-action-verbs
Description: Complete the sentence with the action verb.
Mrs. Carlson ___ nuts into the cookie batter.
Choices: [(a) mixes, (b) butter]
Answer index: 0
Subject: Language Arts
Skill: pronoun-verb-agreement
Description: Complete the sentence with the best **verb**.
He ___ on television.
Choices: [(a) appears, (b) appear]
Answer index: 0
Subject: Language Arts
Skill: make-predictions-about-a-story
Description: Read this passage from a story.
Anna and Andrew had just moved in to their new house. "Let’s explore," Anna said. They
opened all the closets in the bedrooms. Then they found the door to the attic. Their dad
noticed them opening the door. "Go ahead," he said. "It’s full of old junk."
In the attic, Anna and Andrew saw an old dresser and some boards. Then they noticed a very
large metal box. They walked over to look at it more closely.
Based on the passage, which is more likely to happen next?
Choices: [(a) Anna and Andrew open the metal box., (b) Anna and Andrew open the dresser
drawers.]
Answer index: 0
Subject: Language Arts
Skill: greetings-and-closings-of-letters
Description: Which closing is correct for a letter?
Choices: [(a) Thanks, Jim, (b) thanks, Jim]
Answer index: 0
Subject: Language Arts
Skill: identify-base-words-prefixes-and-suffixes
Description: What is the base word in **dampness**?
Choices: [(a) damp, (b) ness]
Answer index: 0
Subject: Language Arts
Skill: which-sentence-has-the-same-meaning
Description: Which sentence has the same meaning?
Mrs. Duncan **closed** her bedroom door and went to bed.
Choices: [(a) Mrs. Duncan **shut** her bedroom door and went to bed., (b) Mrs. Duncan
**painted** her bedroom door and went to bed.]
Answer index: 0
Subject: Language Arts
Skill: identify-the-authors-purpose-passages
Description: Read the text below.
Vote for Bob Mueller for city council. He’ll stand up for the needs of our town’s hardworking
citizens.
What is the text’s most likely purpose?
Choices: [(a) to persuade, (b) to inform, (c) to entertain]
Answer index: 0
Subject: Language Arts
Skill: choose-topic-sentences-for-narrative-paragraphs
Description: Read the paragraph. Then, add the better topic sentence.
___ First, my parents took me to the store to buy some seeds. Then, we took the seeds home,
and I planted them in my backyard. I watered them every day, and soon the plants started to
grow. After several weeks, I started to see little vegetables pop up. By the end of the summer,
I had a garden full of green peppers, beans, corn, and carrots.
Choices: [(a) Last spring, I planted an amazing vegetable garden., (b) Fresh vegetables are
my favorite topping to put on pizza.]
Answer index: 0
Subject: Language Arts
Skill: choose-the-text-that-matches-the-writers-purpose
Description: You want to **inform** someone **about blueberries**. "Inform" means
"teach someone about something". What should you write?
Choices: [(a) Sarah couldn’t believe her eyes. On the table were plates full of blueberry
pancakes, blueberry muffins, and even blueberry sauces., (b) Order our blueberry pancakes
today! They’re always hot and delicious., (c) As the blueberry fruit ripens, it turns from
green to purple to dark blue.]
Answer index: 2
Subject: Language Arts
Skill: analyze-passages-from-narrative-of-the-life-of-frederick-douglass-part-2
Description: Review the passage.
I thought the matter over during the next day, Sunday, and finally resolved upon the third day
of September, as the day upon which I would make a second attempt to secure my freedom. I
now had three weeks during which to prepare for my journey.
...
From Frederick Douglass, Narrative of the Life of Frederick Douglass
Look at the text in **bold**. What hidden reality is shown through this text?
Choices: [(a) It shows that although Douglass’s friends behaved kindly, they secretly envied
him., (b) It shows that although the shipyard was calm, Douglass experienced tension at
home., (c) It shows that although the city felt peaceful, enslaved people were preparing to
rebel., (d) It shows that although Douglass’s plan was working, he still had worries and
doubts.]
Answer index: 3
Subject: Language Arts
Skill: are-the-modifiers-used-correctly
Description: Which sentence is correct?
Choices: [(a) **Stuck in traffic**, Hakim grew drowsy and time slowed to a standstill;
eventually, he decided to pull over and take a nap., (b) **Stuck in traffic**, time slowed to a
standstill and Hakim grew drowsy; eventually, he decided to pull over and take a nap.]
Answer index: 0
Subject: Language Arts
Skill: recall-the-source-of-an-allusion
Description: What is the source of the allusion in the sentence below?
The headline read: "Smart Phones Becoming **Big Brother**."
Choices: [(a) literature, (b) a song]
Answer index: 0
Subject: Language Arts
Skill: transitions-with-conjunctive-adverbs
Description: Complete the text with the better conjunctive adverb.
In China, mountainous areas are being flattened to make more room for new construction;
___, in the United States, mountaintops are being removed so that miners can access coal
reserves.
Choices: [(a) therefore, (b) likewise]
Answer index: 1
Subject: Language Arts
Skill: determine-the-authors-point-of-view
Description: Read the text.
When I decided it was time for a new hobby, I signed up for a "Clowning for Fun and Profit"
class at my local arts center. I cheerily skipped through the door on the first day of class, but
my heart sank as soon as I spotted the instructor, Bobo. Bobo turned out to be a sad-faced
clown who refused to speak. It was clear he planned to teach entirely in pantomime. As he
silently motioned for me to find my seat, I resigned myself to a bad experience.
So imagine my surprise when this crazy class turned out to be invaluable to me! Although I
didn’t hear a single spoken word for five hours, Bobo somehow managed to express his ideas
clearly and in an engaging way. By the end of the first session, he had expertly taught me
how to make balloon animals, apply makeup, juggle beanbags, and develop my own personal
clown character. As I eagerly await the second session, "All About Unicycles," I will begin
clowning around as a volunteer at a local children’s hospital.
Which sentence best summarizes the author’s point of view about the clown class?
Choices: [(a) Bobo uses eccentric teaching methods to efficiently teach this course, making
him an excellent clowning instructor., (b) Bobo’s sad demeanor and poor pantomime skills
make it difficult for his students to learn effective clowning techniques.]
Answer index: 0
Subject: Language Arts
Skill: compare-two-texts-with-different-genres
Description: Read the following text from a diary. This excerpt is about life for Jews in
Europe at the beginning of World War II.
After May 1940 good times rapidly fled: first the war, then the capitulation, followed by the
arrival of the Germans, which is when the sufferings of us Jews really began. Anti-Jewish
decrees followed each other in quick succession. Jews must wear a yellow star, Jews must
hand in their bicycles, Jews are banned from trams and are forbidden to drive. Jews are only
allowed to do their shopping between three and five o’clock and then only in shops which
bear the placard "Jewish shop." Jews must be indoors by eight o’clock and cannot even sit in
their own gardens after that hour. Jews are forbidden to visit theaters, cinemas, and other
places of entertainment.
From Anne Frank, "Anne Frank: The Diary of a Young Girl". Copyright 1952 by Otto H.
Frank
Based on this excerpt, what can you conclude about life for Jews in Europe at the beginning
of World War II?
Choices: [(a) Jewish people could no longer afford to buy theater tickets., (b) Jewish people
could not associate with one another., (c) Jewish people had many of their rights taken away.]
Answer index: 2
Table 33: Question examples for each skill (part 20).

--- Page 45 ---

Subject: Language Arts
Skill: read-and-understand-informational-passages
Description: Review the **seventh paragraph**.
title: Meditating in School
...
This is where the need for good, sound research comes in. Past studies showing that
mindfulness helps medical patients are not enough. To really determine whether mindfulness
helps improve grades, research needs to focus specifically on mindfulness in schools—and
what impact, if any, it has. That way, educators can make informed decisions about where to
put their resources. Until then, whether mindfulness is included in classroom programming
will remain the choice of individual teachers.
Based on the text, what still needs to be determined about mindfulness in schools?
Choices: [(a) whether meditation affects different students in different ways, (b) how to raise
the funds needed to teach meditation in schools, (c) whether mindfulness meditation has a
positive impact in a school setting]
Answer index: 2
Subject: Language Arts
Skill: choose-evidence-to-support-a-claim
Description: Read the claim below.
Gardeners should never use pesticides on their plants.
Select the piece of evidence that best supports this claim.
Choices: [(a) Organic pesticides tend to cost more than conventional ones, and they may be
less effective., (b) Pets and children often play in and around gardens, where they can be
exposed to pesticides.]
Answer index: 1
Subject: Language Arts
Skill: analyze-passages-from-the-giver-part-1
Description: Reread the following passage from The Giver. In this excerpt, Jonas, the main
character, recalls a time when he saw an unidentified aircraft.
Frightened was the way [Jonas] had felt a year ago when an unidentified aircraft had
overflown the community twice. He had seen it both times. Squinting toward the sky, he had
seen the sleek jet, almost a blur at its high speed, go past, and a second later heard the blast
of sound that followed. Then one more time, a moment later, from the opposite direction, the
same plane.
...
From Lois Lowry, The Giver. Copyright 1993 by Lois Lowry
Look at the text in **bold**. How does this paragraph contribute to the meaning or tone of
the passage?
Choices: [(a) It creates an unsettling tone., (b) It creates a ridiculous tone., (c) It creates a
playful tone., (d) It creates a serene tone.]
Answer index: 0
Subject: Language Arts
Skill: use-personification
Description: Complete the sentence so that it uses personification.
The sorceress peered into the mirror, noticing how the amulet ___ her neck.
Choices: [(a) barely clasped around, (b) gently embraced]
Answer index: 1
Subject: Language Arts
Skill: identify-plagiarism
Description: Compare the student text with the source.
Source: Carolyn Cinami DeCristofano, "A Black Hole Is Not a Hole", page 5. Published by
Charlesbridge, 2012:
Nothing can out-tug a black hole. No army of tow trucks, no convoy of supersized earth
haulers, no fleet of giant rocket engines.
Student text:
The pull of a black hole is so strong that nothing can pull stronger, not even a "fleet of giant
rocket engines" (DeCristofano 5).
Is the student text plagiarized?
Choices: [(a) No, it is not plagiarized., (b) Yes, because it fails to use quotation marks.]
Answer index: 0
Subject: Language Arts
Skill: identify-counterclaims
Description: Consider this claim:
Poems that rhyme are better than poems that do not rhyme.
Now consider how someone might argue against this. Which sentence presents a counter-
claim to the above claim?
Choices: [(a) "Beowulf" is one of the oldest and longest poems in existence., (b) Poetry that
doesn’t rhyme allows for more freedom of expression.]
Answer index: 1
Subject: Language Arts
Skill: trace-an-argument
Description: Read the text.
title: Early to Bed and Early to Rise
...
Whether you’re naturally a night owl or an early bird is mostly based on your body’s
chronotype, which Merriam-Webster’s online dictionary defines as "the internal circadian
rhythm or body clock of an individual that influences the cycle of sleep and activity in a
24-hour period." In short, we are born wired one way or the other. However, it is possible to
change your habits. And given the benefits of being an early riser, it may be worth the effort.
What is the author’s main claim or argument?
Choices: [(a) There are just as many benefits to being a night owl as an early riser., (b) It’s
important to change how society perceives night owls., (c) It is better to be an early riser than
a night owl.]
Answer index: 2
Subject: Language Arts
Skill: identify-active-and-passive-voice
Description: Which sentence is in passive voice?
Choices: [(a) On April 18, 1906, an earthquake and its fiery aftermath devastated the city of
San Francisco., (b) On April 18, 1906, San Francisco was devastated by an earthquake and
its fiery aftermath.]
Answer index: 1
Subject: Language Arts
Skill: is-the-pronoun-reflexive-or-intensive
Description: Is the pronoun in bold reflexive or intensive?
Bryce uses an elaborate system of notes to remind **himself** of what he has left to do.
Choices: [(a) intensive, (b) reflexive]
Answer index: 1
Subject: Language Arts
Skill: interpret-figures-of-speech
Description: What does the **metaphor** in this text suggest?
When Bobby lost his job, he was devastated. The only light in the sea of darkness was the
prospect of pursuing a new career.
Choices: [(a) There was a benefit to Bobby’s job loss., (b) Having to pursue a new career was
the worst part of Bobby’s job loss.]
Answer index: 0
Subject: Language Arts
Skill: identify-the-verb-mood
Description: Which verb mood is used in the **bold** part of the sentence?
To help maintain your energy and focus throughout the day, **eat a healthy breakfast**.
Choices: [(a) imperative, (b) subjunctive]
Answer index: 0
Subject: Language Arts
Skill: classify-figures-of-speech
Description: Which figure of speech is used in this text?
The water made a sound **like kittens lapping**.
—Marjorie Kinnan Rawlings, "The Yearling"
Choices: [(a) metaphor, (b) simile]
Answer index: 1
Subject: Language Arts
Skill: vocabulary-review-trace-an-argument
Description: Look at the word **entrenched** as used in the passage "The Most Important
Meal of the Day?"
An Australian study published in 2019 collected health data for over twenty-eight years
from multiple countries. The results showed few differences between breakfast skippers and
breakfast eaters. The study concluded that "breakfast is not the most important time of the
day to eat, even though that belief is really **entrenched** in our society and around the
world."
What does **entrenched** mean?
Choices: [(a) highly debatable, (b) quite rare, (c) firmly established]
Answer index: 2
Subject: Language Arts
Skill: analyze-passages-from-the-outsiders-part-2
Description: Review the passage.
Tim Shepard and company were already waiting when we arrived at the vacant lot, along
with a gang from Brumly, one of the suburbs. Tim was a lean, catlike eighteen-year-old who
looked like the model JD you see in movies and magazines. He had the right curly black
hair, smoldering dark eyes, and a long scar from temple to chin where a tramp had belted
him with a broken pop bottle. He had a tough, hard look to him, and his nose had been
broken twice. Like Dally’s, his smile was grim and bitter. He was one of those who enjoy
being a hood. The rest of his bunch were the same way. The boys from Brumly, too. Young
hoods—who would grow up to be old hoods. I’d never thought about it before, but they’d
just get worse as they got older, not better. I looked at Darry. He wasn’t going to be any hood
when he got old. He was going to get somewhere. Living the way we do would only make
him more determined to get somewhere. That’s why he’s better than the rest of us, I thought.
He’s going somewhere. And I was going to be like him. I wasn’t going to live in a lousy
neighborhood all my life.
...
From S. E. Hinton, The Outsiders. Copyright 1967 by S. E. Hinton
Look at the text in **bold**. What does this figurative language suggest?
Choices: [(a) Tim fights for survival every day., (b) Tim has always been cruel to Ponyboy.,
(c) Tim often does not have enough to eat., (d) Tim attempts to stay hidden at all costs.]
Answer index: 0
Table 34: Question examples for each skill (part 21).

--- Page 46 ---

Subject: Language Arts
Skill: identify-the-authors-purpose
Description: Review the text.
Good study habits train your brain for success. Applying effective learning methods will not
only improve your grades but, more importantly, increase your long-term knowledge.
Cramming at the last minute is ineffective. Instead, try to create a study routine. Schedule
specific blocks of time to study every day. Next, find the best environment that helps you
concentrate. Some students do better with the silence of a library, while others need the
background noise or music of a public space.
Now that you have a time and a place, you need a strategy. Look at your tasks and make a
list. Setting small, manageable goals for your study session will help you work efficiently.
Do the most difficult assignments first, while your mind is fresh. Finally, do not be afraid to
take limited breaks to restore your motivation.
Which best shows that the author’s purpose is "to explain some productive study techniques
to readers"?
Choices: [(a) The author argues that students need to work in a place with "background
noise" in order to study efficiently., (b) The author outlines a series of best practices to follow
to improve study habits.]
Answer index: 1
Subject: Language Arts
Skill: is-it-a-direct-object-or-an-indirect-object
Description: Is the phrase in bold a direct object or an indirect object?
A guard denied **the tourists** entrance to the palace.
Choices: [(a) direct object, (b) indirect object]
Answer index: 1
Subject: Language Arts
Skill: decide-whether-ellipses-are-used-appropriately
Description: Read this text.
On May 25, 1977, "Star Wars" opened in theaters and wowed audiences with groundbreaking
special effects.
Is this an appropriate use of an ellipsis?
Choices: [(a) yes, (b) no, because the text with an ellipsis is no longer grammatically correct]
Answer index: 1
Subject: Language Arts
Skill: compound-subjects-and-objects-with-pronouns
Description: Select the correct pronoun to complete the sentence.
Mr. Joyce rarely worries about ___ and Farid, because they’re both so responsible.
Choices: [(a) she, (b) her]
Answer index: 1
Subject: Language Arts
Skill: identify-vague-pronoun-references
Description: Which of the following contains a vague pronoun reference?
Choices: [(a) Bella and her sister posed for a photograph, but when the flash went off, she
blinked., (b) Bella and her sister posed for a photograph, but when the flash went off, Bella
blinked.]
Answer index: 0
Subject: Language Arts
Skill: what-does-the-punctuation-suggest
Description: What does the following sentence suggest?
Ferries depart from Battery Park in New York and Liberty State Park in New Jersey for the
museum on Ellis Island, which commemorates the millions of immigrants who entered the
United States through Ellis Island.
Choices: [(a) There is only one museum on Ellis Island., (b) There is more than one museum
on Ellis Island.]
Answer index: 0
Subject: Language Arts
Skill: suggest-appropriate-revisions
Description: Read the following text from a student essay. How can the writer best improve
his or her **word choice**?
I saw a movie called "Blob Invasion". It was really good. It was about a weird guy who was
into science. He worked on bugs and small animals. He made a machine that did things to
the bugs and the animals. They became big weird things. One day he transformed himself by
accident. He became a big blob! He went around doing bad things to the city. In the end, a
boy figured out how to change the blob back into a man. I would recommend this movie to
everyone who likes fun science movies.
Choices: [(a) by reducing repetitive language, (b) by using more specific language]
Answer index: 1
Subject: Language Arts
Skill: analyze-passages-from-the-giver-part-2
Description: Review the passage.
"Father? Mother?" Jonas asked tentatively after the evening meal. "I have a question I want
to ask you."
...
From Lois Lowry, The Giver. Copyright 1993 by Lois Lowry
Based on the passage, how does Jonas most likely feel about his family?
Choices: [(a) He finds comfort in the regimented order provided by his family., (b) He
wonders why his family’s beliefs are different from the community’s., (c) He feels grateful to
have a family that openly discusses tough issues., (d) He is beginning to question his parents
and the community.]
Answer index: 3
Subject: Language Arts
Skill: identify-thesis-statements
Description: Which is a thesis statement?
Choices: [(a) School-wide Wi-Fi access is critical to building academic success because
it increases communication, allows for more interactive lessons, and expands research
opportunities., (b) What effect does having Wi-Fi access in public school classrooms and
libraries have on how students perform academically and how well they pay attention in
class?]
Answer index: 0
Subject: Language Arts
Skill: classify-logical-fallacies
Description: Which logical fallacy is used in the text?
In this election, we’ve seen the highest voter turnout ever recorded. If you have any doubts
about Ryan Mueller’s qualifications, just look at how many people have come out to vote for
him.
Choices: [(a) bandwagon fallacy: the assumption that the popular choice is automatically
correct, (b) ad hominem: a personal attack against one’s opponent]
Answer index: 0
Subject: Language Arts
Skill: analyze-passages-from-the-outsiders-part-1
Description: Read the following passage from "The Outsiders". In this excerpt, Ponyboy, the
narrator, and his friend, another greaser named Two-Bit, are walking with two girls from a
rival group called the Socs.
After the movie was over it suddenly came to us that Cherry and Marcia didn’t have a way
to get home. Two-Bit gallantly offered to walk them home—the west side of town was
only about twenty miles away—but they wanted to call their parents and have them come
and get them. Two-Bit finally talked them into letting us drive them home in his car. I
think they were still half-scared of us. They were getting over it, though, as we walked to
Two-Bit’s house to pick up the car. It seemed funny to me that Socs—if these girls were any
example—were just like us. They liked the Beatles and thought Elvis Presley was out, and
we thought the Beatles were rank and that Elvis was tuff, but that seemed the only difference
to me. Of course greasy girls would have acted a lot tougher, but there was a basic sameness.
I thought maybe it was money that separated us.
...
From S. E. Hinton, The Outsiders. Copyright 1967 by S. E. Hinton
Based on the passage, which of the following is most likely true about Ponyboy?
Choices: [(a) Ponyboy doesn’t want to take the girls home, but he feels obligated to assist
them., (b) Cherry is attempting to develop a deep connection with Ponyboy, but he is
resistant., (c) Ponyboy wishes he had more money so he could be more like the Socs., (d)
This is Ponyboy’s first time having an authentic conversation with a member of the Socs.]
Answer index: 3
Subject: Language Arts
Skill: use-the-correct-verb-with-compound-subjects
Description: Complete the sentence with the best verb.
Whenever Skip runs out into the yard, the chickens and the rooster ___ into the coop.
Choices: [(a) disappears, (b) disappear]
Answer index: 1
Subject: Language Arts
Skill: distinguish-facts-from-opinions
Description: Which sentence states a fact?
Choices: [(a) The spinach plant is native to Asia., (b) Spinach tastes worse than any other
vegetable.]
Answer index: 0
Subject: Language Arts
Skill: choose-the-best-transition
Description: Choose the transition that compares, or shows similarities.
Betty helps her community by raising money for a youth center. ___, Dale makes his
neighborhood more beautiful by planting trees.
Choices: [(a) Similarly, (b) For example]
Answer index: 0
Table 35: Question examples for each skill (part 22).

--- Page 47 ---

Subject: Language Arts
Skill: analyze-passages-from-narrative-of-the-life-of-frederick-douglass-part-1
Description: Read the following passage from "Narrative of the Life of Frederick Douglass".
In this excerpt, Douglass describes some features found on the plantation where he was
enslaved as a young child.
Colonel Lloyd kept a large and finely cultivated garden, which afforded almost constant
employment for four men, besides the chief gardener, Mr. M’Durmond. This garden was
probably the greatest attraction of the place. During the summer months, people came from
far and near—from Baltimore, Easton, and Annapolis—to see it. It abounded in fruits of
almost every description, from the hardy apple of the north to the delicate orange of the
south. This garden was not the least source of trouble on the plantation. Its excellent fruit
was quite a temptation to the hungry swarms of boys, as well as the older slaves, belonging
to the colonel, few of whom had the virtue or the vice to resist it.
...
From Frederick Douglass, Narrative of the Life of Frederick Douglass
What is this passage mainly about?
Choices: [(a) It is about why Douglass enjoyed spending time in the garden and stable
on Colonel Lloyd’s plantation., (b) It is about how Colonel Lloyd’s fancy garden and fine
horses created challenges for enslaved people., (c) It is about how Colonel Lloyd paid more
attention to his garden than to the horses in his stable., (d) It is about why enslaved people
preferred to work in Colonel Lloyd’s stable instead of his garden.]
Answer index: 1
Subject: Language Arts
Skill: analyze-short-stories
Description: Read the story.
title: Chiarelli’s Bakery
...
Ms. Chiarelli nodded impatiently. "Come on! If we hurry, we can make cassatelle too."
Based on the **fourth paragraph**, what is Aram’s attitude about his future career?
Choices: [(a) He is confident that he will achieve success., (b) He is sure that he will fail, but
he wants to try., (c) He is uncertain how things will turn out.]
Answer index: 0
Subject: Language Arts
Skill: determine-the-main-idea-of-a-passage
Description: Read the passage.
All over the planet, ancient tombs and temples lie hidden from view. So how do archaeolo-
gists know where to begin digging? Thanks to satellites, that question is becoming easier
to answer. In the pioneering field of satellite archaeology, satellites four hundred miles
above Earth can identify structures buried under soil, covered by modern construction, or
obscured by forests. For example, mud bricks used by ancient Egyptians are more dense
than soil, and the differences are detected by the satellites. Advanced computer programs
map buried settlements and distinguish them from water, vegetation, and farmland. Sarah
Parcak, a pioneer in the field, says of the technology, "It allows you to literally strip away
vegetation and see entire cities beneath the rain forest canopy. This is the unbelievable future
of archaeology."
What is the main, or central, idea of the passage?
Choices: [(a) Archaeologists must determine where ancient structures are buried before they
can begin excavating them., (b) Archaeologists are uncovering ancient hidden structures by
using satellite imagery.]
Answer index: 1
Subject: Language Arts
Skill: use-parallel-structure
Description: Complete the sentence.
In his novel Nineteen Eighty-Four, George Orwell describes a dystopian London in the hands
of a totalitarian government that is paranoid, watchful, and ___.
Choices: [(a) mercilessly oppressive, (b) mercilessly oppresses its citizens]
Answer index: 0
Subject: Language Arts
Skill: use-dictionary-entries-to-determine-correct-usage
Description: Look at this dictionary entry.
dictionary word: exasperate
dictionary pos: verb
dictionary inflections: exasperating, exasperated
dictionary entry: 1 to make very angry; to irritate Marie was exasperated by Barbara’s
constant complaining.
dictionary etymology: from Latin (exasperare)
Which sentence uses the word **exasperate** correctly?
Choices: [(a) Mrs. Hampton realized she was exasperating a bad situation when she failed
to pay the parking ticket promptly., (b) Gary’s reluctance to do basic household chores
exasperated Khalil and Chase.]
Answer index: 1
Subject: Language Arts
Skill: trace-an-argument-set-1
Description: Read the text.
title: The Connected City
...
The bottom line is that online connectivity is a necessity in today’s high-tech society. Cities
across the country are scrambling to keep up with ever-increasing demands for Wi-Fi by the
general public. In fact, an Internet Society survey of more than ten thousand Internet users
around the world found that eighty-three percent of the respondents agreed that access to the
Internet should be considered a basic human right. Whether viewed as a public service or as
a way to boost the local economy, people expect advanced technology on the go. Travelers,
business owners, and local residents should be able to rely on the local government to help
them stay connected.
What is the author’s main claim or argument?
Choices: [(a) Access to free Wi-Fi throughout a city helps to promote tourism., (b) Free
Wi-Fi in cities benefits residents as well as the local economy., (c) Only low-income residents
of urban areas should be provided with free Wi-Fi.]
Answer index: 1
Subject: Language Arts
Skill: which-text-is-most-formal
Description: Which expression of thanks is more formal?
Choices: [(a) We’re so pleased you could join us on our special day. Thank you again for the
wonderful gift., (b) We’re super happy that you could be with us on our special day. Thanks
again for the awesome gift!]
Answer index: 0
Subject: Language Arts
Skill: trace-an-argument-set-2
Description: Read the text.
title: Fact or Fiction?
...
Looking beyond the author’s own life events, memoir can inform readers about the world in
the same way that other nonfiction can. For example, a memoir written by the head chef of a
famous restaurant is likely to educate the reader about the inner workings of a professional
kitchen. A memoir composed by a cello player in an esteemed orchestra will probably
help the reader learn more about music. And a memoir recalling an adolescence during the
1980s may describe pop culture during that time. Memoir has a way of relaying facts about
anything from an occupation to brief fashion trends, all of it meaningful to the author.
What is the author’s main claim or argument?
Choices: [(a) Memoir is best categorized under the umbrella of literary nonfiction., (b)
Memory is too unreliable for memoir to be considered a type of nonfiction., (c) While many
memoirs are fact-based, many authors are untrustworthy., (d) The most profitable memoirs
are those shown to be the most factual.]
Answer index: 0
Subject: Language Arts
Skill: choose-the-topic-sentence-that-best-captures-the-main-idea
Description: Review the details below.
Cell phones can be used to cheat on tests by sending answers to friends or by accessing the
Internet.
...
Texting during class is like passing notes and is a waste of time.
Choose the best topic sentence to introduce a paragraph containing these details.
Choices: [(a) Cell phones in the classroom can have a negative impact on student learning.,
(b) There are many legitimate arguments for allowing students to have cell phones in class,
even if they are disruptive., (c) Cell phones have become a near constant presence at school
and at home.]
Answer index: 0
Subject: Language Arts
Skill: identify-sentence-fragments
Description: Is there a sentence fragment?
Before signing in, you must first register for an account. Unless you’re already a member of
the site.
Choices: [(a) yes, (b) no]
Answer index: 0
Table 36: Question examples for each skill (part 23).

--- Page 48 ---

Subject: Language Arts
Skill: use-context-as-a-clue-to-the-meanings-of-foreign-expressions
Description: What is the meaning of the foreign expression in bold?
In 2014, giant moths swarmed **en masse** in parts of Southeast Asia. More than eight
hundred sightings were reported in Singapore, while thousands disrupted a soccer match at
Darul Makmur Stadium in Malaysia.
Choices: [(a) coincidentally, (b) as a group, (c) unexpectedly, (d) fatally]
Answer index: 1
Subject: Language Arts
Skill: use-the-correct-foreign-expression
Description: Complete the text with the correct foreign expression.
The Norwood Bistro features an eclectic ___ menu so that diners can select a variety of
dishes.
Choices: [(a) à la carte, (b) crème de la crème]
Answer index: 0
Subject: Language Arts
Skill: identify-audience-and-purpose
Description: Review the fund-raising pamphlet and then answer the question.
Be a hero in an animal’s life! Donate to the Martin County Animal Shelter. Adoption fees
cover less than eight percent of our operating expenses. We rely on donations to ensure
that every animal receives excellent care. Your generous gift provides food, shelter, and
veterinary care to homeless and rescued pets. Please donate today!
Which best indicates that the primary audience is "community members who care about
animals"?
Choices: [(a) The writer indicates that donating is a way for readers to "be a hero in an
animal’s life.", (b) The writer argues that the shelter is necessary to keep stray animals off the
streets and prevent illnesses., (c) The writer asks readers to donate time as well as money.,
(d) The writer includes information about funding sources and operating expenses.]
Answer index: 0
Subject: Language Arts
Skill: classify-figures-of-speech-euphemism-hyperbole-oxymoron-paradox
Description: Which figure of speech is used in this text?
This movie is so predictable that I’m likely to **die of boredom** if I keep watching it.
Choices: [(a) paradox, (b) hyperbole]
Answer index: 1
Subject: Language Arts
Skill: analyze-short-stories-set-1
Description: Read the story.
title: Lake Magic
...
Gramps appeared with dry towels. "I’ve made popcorn and a warm fire. And your mom
called. She’s fine." Gramps paused, then added, "Everybody’s fine."
What is the main reason Izzie is looking for Champ?
Choices: [(a) She hopes Champ will take her brother’s place as a friend to her., (b) She wants
to prove to her grandfather that she can find the legendary lake monster., (c) She wants
Champ’s "lake magic" to make her family the way it used to be.]
Answer index: 2
Subject: Language Arts
Skill: explore-words-with-new-or-contested-usages
Description: Which text uses the word **nauseous** in its traditional sense?
Choices: [(a) Everyone seemed to enjoy the magnolia-scented candle, but it made Walter feel
rather **nauseous**., (b) Everyone seemed to enjoy the magnolia-scented candle, but Walter
found the smell rather **nauseous**.]
Answer index: 1
Subject: Language Arts
Skill: analyze-the-development-of-informational-passages-set-2
Description: Read the text.
title: Manzanar: A Site of Conscience
...
Adapted from the National Park Service, "Manzanar: A Site of Conscience"
What is the main focus of the text?
Choices: [(a) how the attack on Pearl Harbor led to war against Japan, (b) the history
of the internment of Japanese Americans, with a focus on Manzanar, (c) how Japanese
Americans adjusted to everyday life at Manzanar, (d) the history of injustices against
Japanese Americans, including internment at Manzanar]
Answer index: 1
Subject: Language Arts
Skill: analyze-the-development-of-informational-passages-set-1
Description: Read the text.
title: Language Change
...
Adapted from the National Science Foundation, "Language and Linguistics: Language
Change"
What is the main focus of the text?
Choices: [(a) why the works of Shakespeare and Chaucer are difficult for modern readers, (b)
why different languages evolve at different rates, (c) how and why language changes over
time]
Answer index: 2
Subject: Language Arts
Skill: choose-punctuation-to-avoid-fragments-and-run-ons
Description: Which is the best way to complete the text?
Zoe traced her family’s lineage back to the eighteenth ___ cross-referenced her grandmother’s
stories with a genealogical index at the library.
Choices: [(a) century. She, (b) century, furthermore, she, (c) century, she]
Answer index: 0
Subject: Language Arts
Skill: transition-logically-between-claims-evidence-analysis-and-counterclaims
Description: Complete the text with the transition that best connects **the two pieces of
supporting evidence**.
Parents should limit how much screen time their children are allowed to have each day. A
study found that children whose parents limited screen time experienced physical benefits,
including better sleep habits and decreased risk of obesity. ___, these children earned better
grades in school, were more social and helpful, and were less aggressive with peers.
Choices: [(a) In other words, (b) Moreover, (c) For example]
Answer index: 1
Subject: Language Arts
Skill: choose-the-analysis-that-logically-connects-the-evidence-to-the-claim
Description: Read the claim and the supporting evidence.
*Claim:** Hunter is remarkably virtuous.
*Evidence:** Hunter is generous with his time.
Why does the evidence support the claim? Choose the **analysis** that better explains the
connection.
Choices: [(a) Generosity is a key virtue., (b) Hunter believes generosity need not involve
money.]
Answer index: 0
Subject: Language Arts
Skill: identify-run-on-sentences
Description: Is this a run-on sentence?
Clinging to a two-point lead in the final minute of the fourth quarter, the Tigers triumphed
when their defense recovered a fumble and sealed the victory.
Choices: [(a) yes, (b) no]
Answer index: 1
Subject: Language Arts
Skill: use-words-accurately-and-precisely
Description: Complete the text with the better phrase.
Karen and Steven are ___ on a documentary film project about the effects of drought on local
wildlife.
Choices: [(a) collaborating together, (b) working together]
Answer index: 1
Subject: Language Arts
Skill: classify-figures-of-speech-review
Description: Which figure of speech is used in this text?
He had hoped to find his missing watch, but **he couldn’t find the time**.
Choices: [(a) onomatopoeia, (b) pun]
Answer index: 1
Subject: Language Arts
Skill: avoid-double-illogical-and-unclear-comparisons
Description: Which text best completes the sentence?
As a dancer, I studied tap and ballet. In my experience, tap was ___.
Choices: [(a) easier to learn than any form of dance, (b) easier to learn, (c) easiest to learn]
Answer index: 1
Subject: Language Arts
Skill: choose-the-best-evidence-to-support-a-claim
Description: Consider this claim:
Online colleges prepare students for careers just as well as traditional brick-and-mortar
schools do.
Which is the strongest evidence to support the claim?
Choices: [(a) "I’ve hired two people recently who received their college degrees through
online programs, and the quality of their performance is as good as, if not better than, that of
their peers," reported business owner Fred Browning., (b) Online college programs often
provide career preparation services that are equivalent to those provided by traditional
college programs, including interview preparation, job fairs, and even internship placement.,
(c) Many students choose to gain some credits through an online college program and then
successfully transfer to a brick-and-mortar institution to complete a degree.]
Answer index: 1
Table 37: Question examples for each skill (part 24).

--- Page 49 ---

Subject: Language Arts
Skill: analyze-short-stories-set-2
Description: Read the story.
title: Water Rising
...
Polara looked to the horizon, at the unmistakable sparkle of the approaching sea. She wasn’t
sure how brave she felt, but she was willing. "I am," she answered.
Based on the **first and second paragraphs**, what internal conflict does Polara struggle
with?
Choices: [(a) the duty to stand watch versus her inclination to daydream, (b) the pull of the
unfamiliar versus her desire to stay at Shublik, (c) respect for Commander Axel versus her
irritation at his order, (d) the enjoyment of the view versus her fear about the water on the
horizon]
Answer index: 1
Subject: Language Arts
Skill: use-appeals-to-ethos-pathos-and-logos-in-persuasive-writing
Description: Which statement primarily appeals to **logos**, or reason, to support the
position that **more money does not always lead to increased happiness**?
Choices: [(a) Like most people, I enjoy the feeling of buying a new gadget, but it turns out
that the happiness that we get from a new purchase doesn’t last long., (b) While it’s true that
a lack of money can cause stress and unhappiness, it does not necessarily follow that money
will lead to more happiness after basic needs are met.]
Answer index: 1
Subject: Language Arts
Skill: choose-the-word-whose-connotation-and-denotation-best-match-the-sentence
Description: Complete the sentence with the word that best fits the overall meaning and tone.
Dan appreciated the gallery owner’s ___ efforts to include artwork from the local community.
Choices: [(a) calculating, (b) deliberate]
Answer index: 1
Subject: Language Arts
Skill: evaluate-counterclaims
Description: Consider this claim:
Veggie burgers are every bit as tasty and satisfying as regular beef burgers.
Now consider how someone might argue against this. Which sentence presents the stronger
and more reasonable counterclaim to the above claim?
Choices: [(a) Veggie burgers have no taste whatsoever and cannot compare in any way to a
delicious beef burger., (b) Regular beef burgers have more good-tasting fat and filling protein
than veggie burgers.]
Answer index: 1
Subject: Language Arts
Skill: use-etymologies-to-determine-the-meanings-of-words
Description: "Vociferous" and "vocal" are related English words that come from Latin. What
does **vociferous** mean?
Choices: [(a) loud and forceful, (b) wise and thoughtful, (c) strong and fit]
Answer index: 0
Subject: Language Arts
Skill: analyze-passages-from-the-lightning-thief-part-2
Description: Read the following passage from "The Lightning Thief". In this excerpt, Percy
Jackson, the narrator, is describing a dream.
In my dreams, I stood in a dark cavern before a gaping pit. Gray mist creatures churned all
around me, whispering rags of smoke that I somehow knew were the spirits of the dead.
...
From Rick Riordan, The Lightning Thief. Copyright 2005 by Rick Riordan
What is most likely true about the spirits in Percy’s dream?
Choices: [(a) The spirits will cooperate with the ancient voice., (b) The spirits are trying to
protect Percy., (c) The spirits want to lead Percy into the pit.]
Answer index: 1
Subject: Language Arts
Skill: analyze-passages-from-harriet-tubman-conductor-on-the-underground-railroad-part-1
Description: Review the passage.
Harriet thought that Christmas was the very best time of all. By tradition there was no work.
The holiday for the field slaves lasted as long as the Yule log burned in the fireplace at the
Big House. So the people in the quarter spent days preparing the log. They chose a big one,
so big that the strongest field hands bent their backs under its weight. They soaked it in water,
so that it would burn slowly and for a long time.
...
Adapted from Ann Petry, Harriet Tubman: Conductor on the Underground Railroad.
Copyright 1955 by Ann Petry
Which item does the author use to symbolize comfort and security?
Choices: [(a) the cabin, (b) the overseer’s horn, (c) the blankets]
Answer index: 0
Subject: Language Arts
Skill: analyze-passages-from-roll-of-thunder-hear-my-cry-part-1
Description: Review the passage.
"Hey, Cassie," said Mary Lou Wellever, the principal’s daughter, as she flounced by in a new
yellow dress.
...
From Mildred D. Taylor, Roll of Thunder, Hear My Cry. Copyright 1976 by Mildred D.
Taylor
How do students feel about wearing shoes on the first day of school?
Choices: [(a) They are embarrassed by their shoes., (b) They are eager to wear their shoes.,
(c) They are uncomfortable in their shoes.]
Answer index: 2
Subject: Language Arts
Skill: analyze-passages-from-roll-of-thunder-hear-my-cry-part-2
Description: Review the passage.
The revival ran for seven days and it was an occasion everyone looked forward to, for it was
more than just church services; it was the year’s only planned social event, disrupting the
humdrum of everyday country life. Teenagers courted openly, adults met with relatives and
friends they had not seen since the previous year’s "big meeting," and children ran almost
free.
...
From Mildred D. Taylor, Roll of Thunder, Hear My Cry. Copyright 1976 by Mildred D.
Taylor
Look at the text in **bold**. What does this figurative language show about the revival?
Choices: [(a) It shows how long and drawn out the service is., (b) It shows how energetic the
townspeople are., (c) It shows how overcrowded the event is.]
Answer index: 2
Subject: Language Arts
Skill: draw-inferences-from-literary-texts
Description: Read the text.
From his seat at a table in the local library, Ruben turned to the side and saw Nora on a
couch, deeply engrossed in a fantasy book. Nora barely seemed to blink as she read, and
Ruben thought he had never seen anyone so absorbed in a story.
Suddenly, Ruben felt a rumbling beneath his feet. The model of the solar system suspended
from the ceiling began swinging back and forth, as books started falling off the nearby
shelves. There was a commotion as library patrons hustled out of the way.
Nora stood up and in a clear, loud voice, shouted, "Everybody! This is an earthquake. Get
under the tables, now!"
Everyone looked at Nora in shock, frozen in place by a newfound fear.
"Do it!" Nora commanded, as the floor shifted. "Do it right now!"
Ruben and the other patrons followed Nora’s instructions, scrambling under the library
tables.
"Now, put your hands over your head and neck, face away from the windows, and stay still,"
Nora instructed.
As the room shook, some people squealed in fear, while others made soft whimpering noises.
From underneath her own table, Nora calmly reassured them. "Don’t worry—this one
doesn’t seem too bad, and hopefully it’ll be over in just a few seconds."
What is most likely true about Nora?
Choices: [(a) She tends to overreact in stressful situations., (b) She has prior experience with
earthquakes., (c) She works at the library and knows the patrons well.]
Answer index: 1
Subject: Language Arts
Skill: analyze-passages-from-the-lightning-thief-part-1
Description: Reread the following passage from "The Lightning Thief". In this excerpt,
Percy is talking with his friend Annabeth after fighting a tough battle on their quest.
I was pretty much in shock myself. The explosion of bus windows still rang in my ears. But
Annabeth kept pulling us along, saying: "Come on! The farther away we get, the better."
...
From Rick Riordan, The Lightning Thief. Copyright 2005 by Rick Riordan
Which of the following is a reason Annabeth does not want Percy to die?
Choices: [(a) If Percy dies, Annabeth would probably have to live with her dad., (b) If
Percy dies, Annabeth would probably have to finish the quest on her own., (c) If Percy dies,
Annabeth would probably have to go back to the camp.]
Answer index: 2
Subject: Language Arts
Skill: evaluate-newspaper-headlines-for-bias
Description: Which headline best avoids biased language?
Choices: [(a) Second Grader’s Peach Pie Wins First Place in Baking Contest, (b) Inexplicably,
Judges Pick Child’s Peach Pie Despite Tastier Entries, (c) Well-Earned Prize Goes to Young
Student’s Mouthwatering Pie]
Answer index: 0
Table 38: Question examples for each skill (part 25).

--- Page 50 ---

Subject: Language Arts
Skill: analyze-passages-from-harriet-tubman-conductor-on-the-underground-railroad-part-2
Description: Review the passage.
In the fall of 1854, Harriet Tubman began to feel uneasy about three of her brothers.
Benjamin, John and William Henry were still in Maryland, working on plantations where
they had been hired out. She kept having dreams about them, vivid dreams in which she saw
them sold and sent away in a chain gang. She decided to tell them that she was coming to
Maryland that fall, so that they would be ready to go North with her.
...
Adapted from Ann Petry, Harriet Tubman: Conductor on the Underground Railroad.
Copyright 1955 by Ann Petry
What is the meaning of the word **eluded** as used in the passage?
Choices: [(a) escaped the understanding of, (b) caused excitement about, (c) raised awareness
for]
Answer index: 0
Subject: Language Arts
Skill: classify-the-figure-of-speech-euphemism-hyperbole-oxymoron-paradox
Description: Which figure of speech is used in this text?
Lauren asked her mother if she could adopt a cat, and her mother replied, "It’s a **definite
maybe**," so Lauren didn’t want to get her hopes up.
Choices: [(a) euphemism, (b) oxymoron]
Answer index: 1
Subject: Language Arts
Skill: classify-the-figure-of-speech-anaphora-antithesis-apostrophe-assonance-chiasmus-
understatement
Description: Which figure of speech is used in this text?
Soft language **issued** from their **spittleless** **lips** as they **swished** **in**
slow circles round and round the field.
—James Joyce, "A Portrait of the Artist as a Young Man"
Choices: [(a) chiasmus, (b) assonance]
Answer index: 1
Subject: Language Arts
Skill: interpret-the-figure-of-speech
Description: What does the **idiom** in this text suggest?
"Speak of the devil!" Trudy declared when Bert strolled into the room.
Choices: [(a) Trudy had just been speaking about Bert., (b) Trudy didn’t trust Bert.]
Answer index: 0
Subject: Language Arts
Skill: prefixes
Description: Why would a company require an employee to sign a **nondisclosure**
agreement?
Choices: [(a) to keep company secrets private, (b) to prevent the employee from working for
a competitor]
Answer index: 0
Subject: Language Arts
Skill: suffixes
Description: If an objection is **meritless**, what should you do?
Choices: [(a) ignore or dismiss it, (b) take it seriously]
Answer index: 0
Subject: Language Arts
Skill: domain-specific-vocabulary-in-context-science-and-technical-subjects
Description: Read the passage and then answer the question.
"Rafflesia arnoldii" produces the largest flowers of any plant known to man. It also lacks
leaves, roots, a stem, and functioning chloroplasts. What exactly is this bizarre organism,
and how does it survive without so many seemingly crucial parts? **Endemic** to the
rainforests of Southeast Asia, """R. arnoldii""" has developed a number of adaptations that
enable it to thrive in its tropical home. Key to its survival is its parasitic relationship with a
grapelike vine of the genus "Tetrastigma". """R. arnoldii""" spends most of its life almost
completely concealed inside the host vine. When it is ready to reproduce, however, it grows
a single flower that measures about three feet in diameter, weighs up to fifteen pounds, and
emits a strong odor of rotting flesh. The smell of the flower, which attracts carrion flies and
other pollinators, has earned """R. arnoldii""" the nickname "corpse flower."
What is the meaning of **endemic** as used in the passage?
Choices: [(a) new, (b) crucial, (c) harmful, (d) native]
Answer index: 3
Subject: Language Arts
Skill: classify-the-figure-of-speech-review
Description: Which figure of speech is used in this text?
His guardians were extremely old-fashioned people and did not realize that **we live in an
age when unnecessary things are our only necessities**.
—Oscar Wilde, "The Picture of Dorian Gray"
Choices: [(a) paradox, (b) chiasmus]
Answer index: 0
Subject: Language Arts
Skill: analyze-passages-from-a-long-walk-to-water-part-2
Description: Read the following passage from "A Long Walk to Water". In this excerpt,
Salva has just arrived in Rochester, New York, and is meeting his host family.
There they were, smiling and waving in the airport lobby—his new family! Chris, the father;
Louise, the mother; and four children. Salva would have siblings, just as he had before. He
felt his shoulders relax a little on seeing their eager smiles.
...
From Linda Sue Park, A Long Walk to Water. Copyright 2010 by Linda Sue Park
How does Salva feel upon meeting his new family?
Choices: [(a) He feels unsure of how to fit into his new family, but he is excited to get to know
them., (b) His tension and nerves begin to subside, but he still feels a little overwhelmed., (c)
He is thankful for their generosity, but he wants to remain emotionally guarded.]
Answer index: 1
Subject: Language Arts
Skill: analyze-passages-from-a-night-to-remember-part-1
Description: Review the passage.
Up on the bridge, Captain Smith tried to piece the picture together. No one was better
equipped to do it. After 38 years’ service with White Star, he was more than just senior
captain of the line; he was a bearded patriarch, worshipped by crew and passengers alike.
They loved everything about him—especially his wonderful combination of firmness and
urbanity. It was strikingly evident in the matter of cigars. "Cigars," says his daughter, "were
his pleasure. And one was allowed to be in the room only if one was absolutely still, so that
the blue cloud over his head never moved."
...
From Walter Lord, A Night To Remember. Copyright 1955 by Walter Lord.
Look at the text in **bold**. What is the effect of this sentence on the tone of the passage?
Choices: [(a) It creates a skeptical tone., (b) It creates a somber tone., (c) It creates a
frustrated tone.]
Answer index: 1
Subject: Language Arts
Skill: analyze-passages-from-anne-of-green-gables-part-1
Description: Read the following passage from "Anne of Green Gables". In this excerpt,
Anne is chatting with her friend Diana at a tea party.
"We had a plum pudding for dinner on Tuesday and there was half the pudding and a
pitcherful of sauce left over. Marilla said there was enough for another dinner and told me to
set it on the pantry shelf and cover it. I meant to cover it just as much as could be, Diana, but
I forgot all about it. I thought of it next morning and ran to the pantry. Diana, fancy if you
can my extreme horror at finding a mouse drowned in that pudding sauce! I lifted the mouse
out with a spoon and threw it out in the yard. Marilla was out milking and I fully intended to
ask her when she came in if I’d give the sauce to the pigs; but when she did come in I was
imagining that I was a frost fairy going through the woods turning the trees red and yellow,
so I never thought about the pudding sauce again.
...
Adapted from L. M. Montgomery, Anne of Green Gables
What does this passage suggest about Anne?
Choices: [(a) She does not take life very seriously and wishes that others would relax., (b)
She has good intentions, but she can be absentminded sometimes., (c) She is self-confident
and does not worry about what other people think.]
Answer index: 1
Subject: Language Arts
Skill: analyze-passages-from-anne-frank-the-diary-of-a-young-girl-part-2
Description: Review the passage.
Think of it, having to sit in such terror for a day and two nights! We thought of nothing, but
simply sat there in pitch darkness—in her fear, Mrs. van D. had switched off the lamp. We
whispered, and every time we heard a creak, someone said, "Shh, shh."
...
From Anne Frank, The Diary of a Young Girl: The Definitive Edition. Copyright 1991 by
The Anne Frank Fonds. Trans. Susan Massotty
What is the meaning of **engrossed** as it is used in the passage?
Choices: [(a) preoccupied or captivated, (b) puzzled or confused, (c) absentminded or
forgetful]
Answer index: 0
Table 39: Question examples for each skill (part 26).

```
