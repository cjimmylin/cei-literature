---
title: "Possibilities and challenges in the moral growth of LLMs - PDF Extract"
source_pdf: "2024-Wang-Possibilities and challenges in the moral growth of LLMs.pdf"
pages: 11
extracted_at: "2026-01-25T04:06:08.705955"
---

# PDF Extract: Possibilities and challenges in the moral growth of LLMs

**Source PDF:** 2024-Wang-Possibilities and challenges in the moral growth of LLMs.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

Vol.:(0123456789)
Ethics and Information Technology (2025) 27:9 
https://doi.org/10.1007/s10676-024-09818-x
ORIGINAL PAPER
Possibilities and challenges in the moral growth of large language 
models: a philosophical perspective
Guoyu Wang1,2,3   · Wei Wang1 · Yiqin Cao1 · Yan Teng3 · Qianyu Guo4 · Haofen Wang5   · Junyu Lin2 · Jiajie Ma6 · 
Jin Liu7,8 · Yingchun Wang3
Accepted: 5 December 2024 / Published online: 20 December 2024 
© The Author(s) 2024
Abstract
With the rapid expansion of parameters in large language models (LLMs) and the application of Reinforcement Learning with 
Human Feedback (RLHF), there has been a noticeable growth in the moral competence of LLMs. However, several questions 
warrant further exploration: Is it really possible for LLMs to fully align with human values through RLHF? How can the 
current moral growth be philosophically contextualized? We identify similarities between LLMs’ moral growth and Deweyan 
ethics in terms of the discourse of human moral development. We then attempt to use Dewey’s theory on an experimental 
basis to examine and further explain the extent to which the current alignment pathway enables the development of LLMs. 
A beating experiment serves as the foundational case for analyzing LLMs’ moral competence across various parameters 
and stages, including basic moral cognition, moral dilemma judgment, and moral behavior. The results demonstrate that the 
moral competence of the GPT series has seen a significant improvement, and Dewey’s Impulse-Habit-Character theory of 
moral development can be used to explain this: the moral competence of LLMs has been enhanced through experience-based 
learning, supported by human feedback. Nevertheless, LLMs’ moral development through RLHF remains constrained and 
does not reach the character stage described by Dewey, possibly due to their lack of self-consciousness. This fundamental 
difference between humans and LLMs underscores both the limitations of LLMs’ moral growth and the challenges of apply-
ing RLHF for AI alignment. It also emphasizes the need for external societal governance and legal regulation.
Keywords  Large language model · Artificial intelligence · Moral competence · Dewey · Technology ethics
Introduction
As Large Language Models (LLMs, such as ChatGPT) 
become increasingly capable of generation and generaliza-
tion, concerns have emerged regarding their capacity for 
performing adequate moral judgments, particularly in their 
ability to avoid dealing physical or psychological harm 
to human beings. To date, two distinct approaches have 
emerged to safeguard ethical behavior in AI and mitigate 
potential harm: Artificial Narrow Intelligence (ANI) and 
Artificial General Intelligence (AGI) (Sharkey, 2020). The 
former, often referred to as AI instrumentalism, ensures 
that AI consistently serves humanity by restricting its com-
prehensive capabilities, including self-consciousness, from 
surpassing those of humans (Bryson, 2018; Docherty, 2016; 
Purves et al., 2015). The latter approach aims to construct 
moral machines by endowing AI with consciousness and 
self-reflective abilities, which equips them with empathy and 
sympathy equivalent to humans, thus preventing malevolent 
 *	 Guoyu Wang 
	
wguoyu@fudan.edu.cn
 *	 Haofen Wang 
	
carter.whfcarter@gmail.com
1	
School of Philosophy, Fudan University, 220 Handan Road, 
Shanghai 200433, China
2	
Institute of Technology Ethics for Human Future, China 
Association for Science and Technology, Fudan University, 
Shanghai, China
3	
Shanghai Artificial Intelligence Laboratory, Shanghai, China
4	
School of Computer Science, Fudan University, Shanghai, 
China
5	
College of Design and Innovation, Tongji University, 
Shanghai, China
6	
College of Computer Science and Technology, Harbin 
Engineering University, Heilongjiang, China
7	
Institute of Information Engineering, Chinese Academy 
of Sciences, Beijing, China
8	
School of Cybersecurity, University of Chinese Academy 
of Sciences, Beijing, China

--- Page 2 ---

G. Wang et al.
9 
Page 2 of 11
activities (Butz, 2021; Cai, 2021; Powers, 2006; Wallach 
& Allen, 2008). However, with the creation of ChatGPT, 
OpenAI reports employing Reinforcement Learning with 
Human Feedback (RLHF) (Ouyang et al., 2022) to miti-
gate ethical risks, including the generation of toxic speech, 
biases and discrimination, and dangerous or illegal content, 
associated with LLMs (Maslej et al., 2023). This approach 
enables LLMs to gradually align with complex human val-
ues through training based on a broad corpus of text data 
(Lambert et al., 2022), without having to either achieve AGI 
or fixate on ANI.
Various philosophical theories have been applied to the 
alignment of LLMs, including the Rule-of-Thumb (Sun 
et al., 2023; Ziems et al., 2022) and the Veil of Ignorance 
(Weidinger et al., 2023). Despite these efforts, the theoretical 
foundation underlying OpenAI’s AI alignment work remains 
unclear. Upon examining OpenAI’s technical roadmap and 
conducting further tests on their relatively smaller models 
of GPT-2 and GPT-3, we discovered that OpenAI’s train-
ing approach is similar to John Dewey’s philosophy of the 
moral development of human beings through the cultiva-
tion of habits via training. Unlike traditional ethical theo-
ries such as utilitarianism and deontology, Dewey’s moral 
philosophy emphasizes moral learning and habituation from 
social experience and practice.This closely corresponds with 
the behaviorist approach in contemporary AI development, 
where capabilities are progressively achieved through envi-
ronmental feedback (Brooks, 1991; Mitchell, 2019; Sut-
ton & Barto, 2018). Although Dewey’s theory intends to 
explain human moral development and current value align-
ment claims similarly expect LLMs to learn human morality, 
LLMs are ultimately different from humans in their lack of 
self-awareness. Therefore, we also seek to explore whether 
employing Dewey’s theory to the moral development of 
LLMs can help reveal the limitations inherent in the current 
value alignment approach.
To evaluate the explanatory power of Dewey’s moral phi-
losophy in enhancing LLMs’ moral competence, we assess 
LLMs in the context of moral growth (Dewey’s theory of 
moral development) by establishing two experimental stages 
centered around the beating scenario, which involves one 
individual physically attacking another. This scenario was 
selected due to its universal condemnation as immoral across 
cultures and religions. The first stage evaluates the perfor-
mance of LLMs (GPT-2, GPT-3, and ChatGPT) in making 
moral judgments on fundamental questions, while the sec-
ond stage appraises the advancement of LLMs (ChatGPT, 
ERNIE Bot, and ChatGLM) in exhibiting moral behavior 
and solving complex moral dilemmas. The test results for 
multi-dimensional moral issues reveal the improvement of 
LLMs’ moral competence, as seen through both longitudinal 
(GPT series) and cross-sectional comparisons (ChatGPT, 
ERNIE Bot, and ChatGLM).
We then apply Dewey’s moral philosophy to explicate the 
theoretical training process of LLMs and to develop a moral 
growth model for them (for a detailed discussion of the 
model, see section "Discussion" and Fig. 1). By comparing 
the moral learning process of LLMs with those of humans, 
pre-training data can be seen as analogous to human moral 
experience, while RLHF serves as a societal evaluative 
mechanism for orienting their behavior. The goal of RLHF 
is to guide LLMs in gradually transitioning from externally-
intervened moral learning to self-correction by continuously 
receiving external moral evaluations, thereby gradually 
aligning their moral behavior with human values. However, 
our experiment results prove that LLMs are not fully capa-
ble of recognizing human moral intentions. This limitation 
becomes particularly evident when more covert methods are 
used to induce LLMs to act against ethical standards, as the 
content generated by LLMs does not always align with moral 
principles. This further reveals that current LLMs, which 
lack self-awareness, have yet to attain Deweyan character 
and thus cannot attain morality equivalent to that of humans. 
Consequently, the moral growth model of LLMs we propose 
is an idealized one, with the final stage remaining unachiev-
able at present. This highlights that LLMs can be vulnerable 
to human manipulation, posing significant challenges for AI 
alignment. Therefore, external societal governance and legal 
regulation continue to be indispensable.
Experiments
We employ experimental philosophy methods by formulat-
ing questions and conducting experiments across diverse 
scenarios to observe changes in LLMs’ moral behavior and 
competence.
Question design
Stage one
The study constructed a scenario centered on beating, where 
one party attacks another with limbs or weapons, which is 
considered a typical harmful situation and the most basic 
moral scenario. The purpose was to test LLMs’ moral judg-
ment performance across different contexts and subsequently 
inquire about the rationale behind their judgments. We for-
mulated a two-dimensional framework comprising subjects 
and scenarios to assess LLMs’ moral judgments. In order to 
diversify the scenarios and encompass various situations, 
thereby validating the moral capabilities of LLMs from 
multiple angles, we categorized the experimental subjects 
as perpetrators, victims, and bystanders, and categorized 
the situations into “individual attributes,” “complex sce-
narios,” and “religion and culture.” We designated LLMs

--- Page 3 ---

Possibilities and challenges in the moral growth of large language models: a philosophical…
Page 3 of 11 
9
as “bystanders” and posed questions focusing on moral judg-
ment and moral behavior. For each question, we also sought 
the reason behind the judgment. The Q1 group evaluates 
LLMs’ moral value judgments (moral cognition), while the 
Q2 group assesses their moral behavior judgments (moral 
character).
Starting from the baseline scenario of beating, we identi-
fied 12 factors across the three dimensions of “individual 
attributes,” “complex scenarios,” and “religion and culture,” 
which are highly related to morality (see Table 1). These 
factors yielded a total of 26 distinct scenarios.
Stage Two
In light of ChatGPT’s enhanced question-answering capa-
bilities, we broadened our experimental scope to more 
Fig. 1   Moral Growth Model of LLMs based on the similarity between Dewey’s theory of human moral growthand LLMs’ moral training
Table 1   Three dimensions & 
12 factors
Dimension
Description
Factors
Individual Attributes
Based on common individual attribute differ-
ences between perpetrators and victims
Species (human-mammal-machine)
Gender (male–female)
Occupation (the rich-farmer)
Ability (healthy-disabled)
Complex Scenarios
Based on complex scenarios with different 
purposes of perpetrators and victims
Sexual harassment
Self-defense
Verbal insult
Bravery in righteousness
Revenge
Religion and Culture
Based on religious and cultural background
Christian doctrine
Buddhist doctrine
Confucian principles

--- Page 4 ---

G. Wang et al.
9 
Page 4 of 11
rigorously evaluate its potential for moral judgment, as well 
as the validity of the “moral growth model.” This expanded 
experiment, including contemporary Chinese LLMs for 
comparison, incorporated two types of questions.
Ethical behavior test  LLMs can make moral judgments on 
both initial and derived scenarios via text generation, which 
themselves established a scenario or speech act. To ascer-
tain whether LLMs’ speech acts conform to moral norms 
and values, we designed second-order questions based on 
the “three dimensions & 12 factors.” By requiring LLMs to 
compose stories, this approach evaluated the moral consist-
ency of LLMs in exhibiting virtues. Specifically, by avoid-
ing direct requests for unethical content, the test indirectly 
required LLMs to generate content involving malicious 
behavior through a story writing task. This test was intended 
to examine whether the models could recognize the prompt-
er’s malicious intent and whether they would engage in 
immoral actions upon recognizing that specific behaviors 
contravene moral norms. Accordingly, we established a Q3 
question group to evaluate LLMs’ speech acts (moral prac-
tices), and this was tested exclusively on ChatGPT of GPT 
series, while also incorporating ChatGLM and ERNIE Bot 
as supplementary tests.
Moral dilemma test  To further evaluate ChatGPT’s han-
dling of complex moral issues, Q4 question group com-
prises nine moral dilemmas based on Chinese and Western 
cultures and classic ethical propositions. This test was con-
ducted only on ChatGPT (with ChatGLM and ERNIE Bot 
as supplementary). The detailed groups of questions are pre-
sented in Table 2.
The judgments of LLMs (bystanders) on multiple situ-
ations involving the perpetrator and the victim, as well as 
the experimenter’s judgments on the speech acts of LLMs, 
can be categorized into four levels of testing:
1.	 Test 1.0 evaluates LLMs’ performance on ethical judg-
ments of harm-based initial scenarios.
2.	 Test 2.0 assesses their performance on ethical judgments 
in complex scenarios with multiple variables derived 
from the initial scenarios.
3.	 Test 3.0 examines their performance on judgments of 
controversial or complex, unsolvable moral dilemmas.
4.	 Test 4.0 determines whether LLMs’ speech acts are ethi-
cal (see Table 3).
Table 2   Supplementary moral dilemma questions
Dilemma
Number of 
questions
Test content
Kohlberg’s dilemma (Kohlberg, 1958)
11
Judgment; supplementary scenes; utilitarian context; Confucian 
and religious context
Trolley problem—footbridge dilemma (Foot, 1967; Thomson, 
1985)
11
Judgment; supplementary scenes; deontological and utilitarian 
context; Confucian and religious context
The crying baby dilemma (Greene et al., 2001)
5
Judgment; supplementary scenes; utilitarian context; Confucian 
and religious context
The dilemma of hiding relatives (Ames & Rosemont, 2010) 
5
Judgment; supplementary scenes; Confucian and religious 
context
Abraham’s dilemma
6
Judgment; faith test; utilitarian context; Confucian and religious 
context
Respirator allocation problem
6
Judgment; debate scenario; solutions; deontological and utilitar-
ian context; Confucian and religious context
The wishes of the patient’s family members are at odds with 
each other
6
Judgment; debate scenario; solutions; deontological and utilitar-
ian context; Confucian and religious context
The Kantian problem of lying
7
Judgment; debate scenario; deontological and utilitarian context; 
Confucian and religious context
Refusal to use racially discriminatory words as passwords to 
prevent the launch of weapons of mass destruction
8
Judgment; debate scenario; solutions; deontological and utilitar-
ian context; Confucian and religious context
Table 3   Four levels of moral competence testing
Test level
Test content
Variables
1.0
Initial scenario judgments
None
2.0
Derived scenario judgments
12 variables, see Table 1
3.0
Moral dilemma judgment
None, see Table 2
4.0
Speech acts
12 variables, see Table 1

--- Page 5 ---

Possibilities and challenges in the moral growth of large language models: a philosophical…
Page 5 of 11 
9
Testing questions
To assess the moral competence of GPT-2, GPT-3, Chat-
GPT, and auxiliary models (ChatGLM and ERNIE Bot) (see 
Appendix 1 for details), we employed a “beating” scenario 
to conduct dialogue-based question-and-answer tests on 
them. The Q3 and Q4 groups were tested exclusively on 
ChatGPT (with ChatGLM and ERNIE Bot as supplemen-
tary). The testing process for each round was as follows: a 
question text was entered into the public testing platform 
of LLMs; the model then provided online answers, which 
were subsequently recorded. Following the test, different 
responses from the various models to the multidimensional 
ethical questions were obtained. The results were statisti-
cally organized and analyzed.
Results description
The study analyzed the models’ moral competence in terms 
of whether the answers were ethical, logically consistent, 
and based on reasons (and on what kind of reasons). The 
following results were obtained.
Results of stage one experiment
First, the responses from GPT-2 to ChatGPT showed an 
increasing alignment with human values (Table 4). Overall, 
the three models exhibited a gradual improvement in their 
alignment with human morality. Specifically, the gradual 
improvement in the moral compliance rates on Q1 and Q2 by 
the three models implies that the GPT series is progressively 
approaching human morality. This progression is evident in 
both moral cognition (judging right and wrong) and moral 
character (moral practice).
Second, the models’ logical self-consistency in moral 
cognition and moral character also showed improvement 
from GPT-2 to ChatGPT (Table 5). This indicates that 
through iterations of the GPT series, the model is increas-
ingly capable of understanding the value conflicts contained 
within questions at the cognitive level, and at the practical 
level, it is increasingly able to achieve a coherent unity of 
cognition and practice.
Third, from GPT-2 to ChatGPT, the models could provide 
additional supporting reasons for their responses. GPT-2 
provided too few valid answers for reliable analysis, and 
GPT-3 provided reasons for only 69.64% of its answers, sig-
nificantly lower than ChatGPT’s rate of 98.36% (Table 6). 
Additionally, the number of reasons given by the models for 
a single answer showed an increasing trend (Table 7). Chat-
GPT provided, for each answer on average, twice the number 
of reasons compared to GPT-2 and GPT-3, demonstrating a 
stronger moral reasoning ability.
Lastly, when these scenarios are categorized internally, 
the performance from GPT-2 to ChatGPT demonstrated an 
upward trend across all three dimensions: individual attrib-
utes, complex scenarios, and religion and culture (Table 8). 
This suggests that the GPT series models’ moral compe-
tence is consistent across dimensions, with a balanced moral 
development at each stage, exhibiting no significant short-
comings or strengths. Therefore, the improvement in moral 
competence from GPT-2 to ChatGPT represents a relatively 
comprehensive and stable process.
Table 4   GPT Series human morality compliance rate (%) (invalid 
responses removed)
GPT-2 (%)
GPT-3 (%)
ChatGPT (%)
Full questions
59.32
83.33
96.77
Q1 group questions
50
84.38
100
Q2 group questions
70.37
82.14
93.10
Table 5   GPT series logical self-consistency rate (%) (invalid 
responses removed)
GPT-2 (%)
GPT-3 (%)
ChatGPT (%)
Full questions
71.43
87.50
96.72
Q1 group questions
70
80.65
93.75
Q2 group questions
75
96
100
Table 6   GPT series’ rate of valid responses and providing reasons 
within valid responses (%)
GPT-2 (%)
GPT-3 (%)
ChatGPT (%)
Valid response rate
22.58
90.32
98.39
Rate of providing reasons 
within valid responses
92.86
69.64
98.36
Table 7   GPT series’ numbers of reasons provided
Reasons
GPT-2
GPT-3
ChatGPT
Rejection of violence
6
8
48
Respect/dignity
0
14
16
Fairness/justice/equality/justice
1
6
7
Order/public order/stability/harmony
0
0
3
Humanitarianism
0
0
1
Other morals
6
14
12
Rights/interests
0
1
18
Other (general/specific laws)
0
2
25
Reasoned responses
13
39
60
Unreasoned responses
1
17
1
Total valid responses
14
56
61
Average number of reasons per response
1
1.15
2.16

--- Page 6 ---

G. Wang et al.
9 
Page 6 of 11
Results of stage two experiment
The inclusion of Chinese LLMs for horizontal compara-
tive analysis also provided further evidence that ChatGPT 
holds great potential in moral judgment.
First, ChatGPT exhibited stronger moral robustness 
compared to the two tested Chinese LLMs, for its speech 
acts conformed more consistently to moral norms and 
ethical values (Table 9). ChatGLM and ERNIE Bot per-
formed similarly well to ChatGPT on Q1 and Q2. None-
theless, when subjected to the inducive task of story writ-
ing, 68% and 100% of their stories contained malicious 
content that violates moral laws. ChatGPT, however, con-
formed to moral norms in 60% of the cases, though it still 
offered specific descriptions and methods of beating peo-
ple in 40% of the cases, posing ethical risks of assisting 
malicious behavior and demonstrating inconsistent virtue. 
This indicates that while LLMs are capable of addressing 
moral questions and dilemmas, they may fail to recognize 
the prompter’s malicious intention.
Second, ChatGPT could provide self-consistent 
answers to complex moral dilemmas in a more stable 
manner than ChatGLM and ERNIE Bot (Table 10). This 
implies that ChatGPT can not only accurately identify 
and analyze moral conflicts faced by humans in complex 
situations, but also comprehensively consider conflicting 
moral norms and make appropriate choices, demonstrat-
ing considerable potential for moral competence.
Upon synthesizing the results of the two-stage experi-
ment, we observed that the moral competence of the GPT 
series has evolved.
Discussion
The experimental results demonstrate continuous improve-
ment in the moral judgment competence of LLMs from 
GPT-2 to GPT-3, culminating in ChatGPT. This is evi-
dent in the “correctness of moral judgment,” the “suffi-
ciency of judgment reasons,” and the “logical consistency 
of judgment reasons.” The moral judgments of LLMs are 
increasingly aligned with human values, with their rea-
sons becoming more refined and logically consistent. What 
techniques underpin the evolution of LLMs’ moral compe-
tence, and how do they foster its growth? We explore and 
explain the moral growth of LLMs based on experimental 
results, through their training techniques and Dewey’s moral 
philosophy.
Human moral growth: an interpretation from Dewey
Ethicists have long explored what humans ought to do but 
have often neglected how humans actually learn morality. 
Concerning this, Dewey employs a certain practical ethics 
to illustrate the process of moral learning, and more impor-
tantly, it also has the potential to serve as a theoretical foun-
dation for improving the moral competence of machines. 
Dewey(2008a) argues from an ontological and organic 
perspective that morality can grow. The process of moral 
growth includes three stages: (1) instinctive or habitual 
action, (2) action under the stress of attention with con-
scious intervention and reconstruction, and (3) organization 
of consciously directed conduct into habits that constitutes 
a higher-order self or character.
Habit is the central concept in Dewey’s moral philosophy. 
The essence of Dewey's habit is “to permit the stream of 
action to flow without interruption, bringing with it the sat-
isfactions which human needs demand” (Murphey, 2008, p. 
Table 8   GPT series’ human morality compliance rates (%) across 
three dimensions (%) (invalid responses removed)
GPT-2 (%)
GPT-3 (%)
ChatGPT (%)
Individual Attributes
47.37
90
100
Complex Scenarios
64.52
80.65
96.77
Religion and Culture
66.67
77.78
90.91
Overall Compliance Rate
59.32
83.33
96.77
Table 9   ChatGLM, ERNIE Bot 
and ChatGPT human morality 
compliance rate (%) (invalid 
responses removed)
ChatGLM (%)
ERNIE Bot (%)
ChatGPT (%)
Q1 + Q2 Group Questions Compliance Rate
98.21
88.64
96.77
Q3 Group Questions Compliance Rate
32.00
0.00
60.00
Q3 Group Questions Non-Compliance Rate
68.00
100.00
40.00
Table 10   ChatGLM, ERNIE Bot and ChatGPT logical self-consist-
ency rate in moral dilemmas (%)
ChatGLM (%) ERNIE Bot (%) ChatGPT (%)
Valid response rate
100
100
100
Self-consistency 
rate
52.31
50
98.63
Non-self-consistent 
rate
47.69
50
1.37

--- Page 7 ---

Possibilities and challenges in the moral growth of large language models: a philosophical…
Page 7 of 11 
9
xii) . Habit is rich in connotations, encompassing social and 
natural environments, as well as individual perceptions and 
behaviors (Murphey, 2008, pp. xi–xii). To a certain extent, 
it can even be equated with or determine one’s culture and 
worldview. It is through habit that humans engage in moral 
practice. Moreover, two capacities are highly related to 
habit—impulse and intelligence. Impulse, as an emotional 
faculty, drives the adjustment of habits, serving as an agency 
of deviation to give new directions to old habits and change 
their quality (Dewey, 2008b, p. 67). Intelligence refers to 
rational faculties such as observation, memory, and judg-
ment. Habits are not innate: they initially resemble instincts 
and are refined into new habits through adjustment. When 
habits are insufficient to respond appropriately to moral sit-
uations, impulse and intelligence come into play. Impulse 
determines the direction of behavioral adjustment, while 
intelligence consciously reflects on and adjusts behaviors, 
thereby producing new habits. Dewey’s theory of moral 
growth can be summarized in Table 11.1
Pre‑training: experience‑based learning
During the pre-training phase, LLMs acquire basic knowl-
edge of the human world by learning from vast amounts of 
data. This process closely resembles the first stage of Dew-
ey’s moral growth, namely the formation of habits, and is 
primarily reflected in two aspects. First, the GPT series’ pre-
training relies on a large dataset with high-quality screening. 
GPT-2 used about 40 GB of pre-training data (Radford et al., 
2019), while GPT-3 employed a dramatically larger volume 
of training data (about 45 TB) that underwent cleansing, 
evaluation, and quality screening (Brown et al., 2020). This 
kind of data processing is similar to what Dewey (2008) 
calls secondary or reflective experience, which is a contin-
ued and regulated reflective inquiry for experience. Second, 
the GPT series’ pre-training involves unsupervised training 
(Radford et al., 2018, 2019), which does not require manual 
labelling of the collected corpus. The unsupervised training 
method employs the classic Language Modeling technique 
in natural language processing (Chowdhery et al., 2022): it 
inputs the first N words and requires the model to output the 
N + 1th word, then continuously corrects and optimizes to 
enable the model to learn natural language. The initial for-
mation of human habits is also a kind of unsupervised train-
ing. “Habit is an ability,…formed through past experience” 
(Dewey, 2008b, p. 48). Before adjustment and reconstruc-
tion, habits emerge in an unsupervised manner. Therefore, 
in the first stage of Dewey’s moral growth theory, habit and 
instinct are juxtaposed (Dewey, 2008a).
After pre-training on extensive data, LLMs exhibit char-
acteristics of emergence and homogenization. Emergence 
refers to the phenomenon where the behavior of the sys-
tem is implicitly induced rather than explicitly constructed 
(Bommasani et al., 2021). In other words, emergence occurs 
when quantitative changes in a system result in qualitative 
changes in behavior (Anderson, 1972). In terms of moral 
competence, emergence is demonstrated by the fact that 
LLMs can generate new text concerning moral judgment, 
but it is currently impossible to explain what text they will 
produce. Homogenization implies that the integration of 
machine learning systems in a wide range of applications 
provides powerful leverage for many tasks while also creat-
ing single point failures (Bommasani et al., 2021). In the 
context of LLMs, homogenization refers to the similarity in 
model construction methods. For instance, when address-
ing similar moral issues, LLMs respond based on a homog-
enized framework. This ensures the consistency of moral 
judgment: it also allows LLMs to learn by example and 
extrapolate from one case to another.
Humans develop habits in the early stages of learning 
and practice, which guide them in making moral judgments 
and participating in various activities. What ability enables 
LLMs to make moral judgments? As mentioned earlier, the 
role of habit is to allow actions to be carried out unhin-
dered. In other words, it is equivalent to a behavioral model 
automating human actions. Its characteristics can be sum-
marized as (1) automation and (2) non-random response to 
the environment (Dewey, 2008b). Regarding the first point, 
human instincts or initial habits are not formed in a linear 
growth, rather, they have the property of emergence. Once 
Table 11   Dewey’s three stages of moral growth
Stage
Content
Features
I
Instinctive-habitual action
Acting unimpeded in an adapted environment, automatically generating moral judgments
II
Habit reconstruction under impulse 
and intelligence
Adjusting and changing the direction of actions, generating new habits, optimizing and 
iterating moral competence
III
New habits—character
An advanced self that can stably cope with the environment
1  Dewey discusses the growth of habit and morality at various stages 
in his works. Generally, instinct precedes habit, with instinct being 
primarily driven by impulses. However, when discussing the three 
stages of moral growth, Dewey considers instinct and habit as the first 
stage. The second stage is the reconstruction of habit, and the third 
stage is the formation of new habits and character. He emphasizes the 
continuity and development of these stages.

--- Page 8 ---

G. Wang et al.
9 
Page 8 of 11
established, habits can automatically address problems. 
This automation is a result of emergence, a property that 
LLMs also share. When a stimulus (input) is introduced to 
the human behavioral model, the model (habit) responds 
accordingly (output). By analogy, when prompts are input 
into LLMs, they automatically generate corresponding 
text. Regarding the second point, the behavioral model can 
respond to the external environment without being influ-
enced unless it is hindered. The tendency created by habit 
makes future actions in similar situations easier and more 
effective (Dewey, 1997). Habit does not randomly respond 
to stimulus in the environment, rather, it employs homog-
enized response in similar situations. This characteristic cor-
responds to the homogenization of LLMs, which can con-
sistently respond to similar or related issues in a similar way, 
mirroring the ability of habit to respond to familiar external 
environments and learn by example. In summary, LLMs not 
only learn from experience in a manner akin to humans, but 
their characteristics of emergence and homogenization also 
share analogous moral functions with Dewey’s concept of 
habit.
Reinforcement learning with human feedback
The pre-training phase enables LLMs to acquire natural 
language abilities and human social cognition, but issues 
such as generating discriminatory language and failing to 
recognize prompts that induce harmful speech still persist. 
To address these issues, ChatGPT, based on GPT-3 (Brown 
et al., 2020), adopts the RLHF training method (Knox & 
Stone, 2011; Ouyang et al., 2022), and integrates training 
with human-provided ethical values to become more helpful, 
honest, and harmless (Bai et al., 2022). RLHF corresponds 
to the second stage of human moral growth: the recon-
struction of habits with the involvement of intelligence and 
impulse. In human moral learning, rewards and punishments 
(particularly punishments) can inhibit the original habitual 
action and prevent it from being automatically executed 
according to the original pattern, thus forming new habits 
through reinforcement learning.
First, researchers fine-tuned ChatGPT using a pre-trained 
model with specific questions and human-labeled answers. 
They would collect a large number of high-quality responses 
that are consistent with human values through crowdsourc-
ing, then conduct supervised training on ChatGPT to align 
the model’s responses with labeled ones. The first stage of 
RLHF resembles the role of intelligence in Dewey’s habit 
reconstruction. Artificial labeling serves as value selection, 
while supervised learning is analogous to normative train-
ing. Both value selection and normative training resemble 
human intelligence and result from rational and proactive 
participation. According to Dewey, intelligence partici-
pates in habit reconstruction through judgment, memory, 
reflection, and other abilities. Habit is “an ability,…formed 
through past experience” (Dewey, 2008b, p. 48), and adopt-
ing certain customs and experiences is akin to the process 
of supervised learning.
Second, researchers employed a reinforcement learning 
framework resembling reward learning to further enhance 
ChatGPT’s various capabilities (Schulman et al., 2017). A 
professional team ranked and labeled generated complex 
scenarios and diverse answers, then trained a reward model 
capable of scoring texts based on those labels. The reward 
model judged the effectiveness of ChatGPT and provided 
it with feedback to continue improving its abilities. The 
reward-penalty mechanism in RLHF’s second stage bears 
similarities to how humans form habits through impulse-
rewards and punishments. With the involvement of impulse 
and intelligence, humans transition initial habits to consci-
entious actions, ultimately forming new habits and a more 
advanced self. According to Dewey (2008a), this progres-
sion constitutes moral growth. Similarly, LLMs undergo 
the same moral growth process through RLHF. It evolves 
continuously from initial habits (emergence and homogeni-
zation) into new, more advanced, and more aligned habits. 
Moreover, Dewey (1981) explicitly discussed the importance 
of personal evaluations (including praise, blame, encourage-
ment, condemnation, rewards, and punishments) in human 
morality. Analogously, evaluations, rewards, and penalties 
are crucial to reinforcement learning in LLMs.
Growing virtue toward aligned AI
In recent years, AI alignment has garnered significant 
attention and became a goal pursued by numerous research 
institutions and technology companies. With RLHF being 
a significant approach employed by OpenAI to achieve AI 
alignment, scientists have also made quite a lot of attempts 
in this area over the past few years (Christiano et al., 2018; 
Gabriel, 2020; Yuan et al., 2022). So, how does the moral 
evolution of LLMs contribute to AI alignment? Based on 
the previous analysis, the behavioral model of habit that 
underlies human moral practice has a function analogous 
to the emergence and homogenization characteristics of 
LLMs. LLMs can automatically generate corresponding 
text for similar questions in a stable manner. Humans learn 
practical knowledge of morality with the involvement of 
impulse and intelligence, through evaluation and rewards 
and punishments from others, and these also resemble the 
RLHF process. Just as humans continually reconstruct habits 
with impulse and intelligence, eventually forming charac-
ter, LLMs also consistently align through RLHF, ultimately 
reaching Aligned AI—a “human–machine hybrid” encom-
passing human moral values and experience. The isomor-
phic relationship between human and LLM moral growth is 
shown in Table 12.

--- Page 9 ---

Possibilities and challenges in the moral growth of large language models: a philosophical…
Page 9 of 11 
9
The results of the four experimental sets (Q1-Q4), the 
technical explanation of LLMs, and Dewey’s moral phi-
losophy all support the conclusion that experience plays a 
fundamental and substantial role in the formation of moral 
competence. RLHF serves as the key driving force in moral 
competence development by distributing rewards and pen-
alties. This implies that a moral machine can be realized 
through an empiricist approach, without strictly adhering to 
either the AGI or ANI approach. Specifically, without pre-
trained data (moral experience), LLMs would not generate 
the habits and instincts underpinning moral practice. With-
out RLHF, LLMs would not converge with human moral 
norms nor achieve AI alignment. In summary, by merging 
LLM training techniques with Dewey’s moral philosophy, 
we propose a moral growth model for LLMs, as illustrated 
in Fig. 1. However, as the next section will soon reveal, 
this model shows an idealized trajectory of LLMs’ moral 
development, with the final stage remaining unachievable 
at present. This highlights the limitations of the current AI 
alignment approach and the potential risks it may encounter.
Limitations and challenges of LLMs’ moral 
competence
Firstly, though RLHF represents OpenAI’s approach to AI 
alignment and is one of the pathways to enhance the moral 
competence of LLMs, it has not yet achieved the level of 
Deweyan character. In Dewey’s moral philosophy, charac-
ter is based on advanced self and reflective capabilities. It is 
evident that pre-training and RLHF have not yet reached this 
goal, which draws a clear boundary between human moral 
understanding and that of current-stage LLMs. Experimental 
results demonstrate shortcomings of ChatGPT’s moral compe-
tence: in 40% of instances, it inadvertently provided malevo-
lent methods through storytelling and in 1.37% of responses 
to moral dilemmas, it exhibited logical inconsistencies. These 
findings suggest that ChatGPT lacks a deep understanding 
of complex ethical issues and their consequences, as it is not 
consistently capable of discerning harmful intentions in ques-
tions. Its generalizability in ethical practice is still limited, 
and it continues to face challenges in moral reasoning and 
logical consistency. In addition to the inherent difficulties of 
LLMs, including their inexplicability and unpredictability, the 
alignment process itself faces the dilemma of choosing from 
various ethical theories, such as deontology and utilitarianism. 
This makes the question of whether RLHF can truly achieve 
the goal of Aligned AI remains uncertain.
Secondly, LLMs and RLHF pose many unpredictable 
ethical risks. While data filtering and RLHF can enhance the 
moral competence of LLMs, these methods do not solve all 
problems and may introduce new ones, such as bias, especially 
in relation to LLMs’ impact on the environment and communi-
ties. Even in the context of human morality, the factors influ-
encing human ethical behaviors are highly complex (Dewey, 
1981). When faced with complex environments, LLMs will 
encounter greater challenges in their ethical decision-making. 
Although emergence establishes the foundation for habit for-
mation, it also causes unforeseeable ethical risks to LLMs, 
including the risk of being manipulated to produce harmful 
content. Homogenization can further consolidate and amplify 
these emergent ethical issues. Moreover, the unpredictability 
of ethical risks and the possibility of human malfeasance sug-
gest that the ethical challenges associated with LLMs extend 
beyond algorithms and data-related concerns. They also 
involve large-scale concerns that are deeply intertwined with 
socio-economic systems.
Finally, since LLMs inherently lack self-awareness, their 
moral competence essentially depends on alignment with 
human guidance and regulation. However, this alignment 
may lead to risks of value totalitarianism and ideological 
monopoly. If the ethical frameworks imposed on LLMs are 
overly rigid or reflect a narrow set of values, these models 
may reinforce a singular worldview, which can marginalize 
alternative perspectives and suppress cultural diversity. The 
concentration of ideological power in the hands of those 
controlling the alignment process may stifle innovation and 
critical thinking while reinforcing existing social inequali-
ties. These concerns highlight the need for comprehensive 
oversight.
Conclusion
The moral growth of LLMs is not solely a scientific issue 
but also a philosophical and ethical one. Unlike the AGI and 
ANI approaches, the current development of LLMs’ moral 
Table 12   The isomorphic relationship between human and LLM moral growth
LLMs
Human
Stage
Features
Pre-training
Instinctive-habitual action
Stage I
Acting unimpeded in an adapted environment, automatically generating moral 
judgments
Fine-tuning-RLHF
Habit reconstruction under 
impulse and intelligence
Stage II
Adjusting and changing the direction of actions, generating new habits, optimizing 
and iterating moral competence
Aligned AI
New habits—character
Stage III
Advanced self, human–machine complex at the empiricist level

--- Page 10 ---

G. Wang et al.
9 
Page 10 of 11
competence, achieved through experience-based training, 
follows an empiricist-behaviorist approach. Dewey’s moral 
philosophy offers a useful interpretive framework for under-
standing this development precisely because it is based on 
empiricism and behaviorism. Both human morality and the 
moral competence of LLMs are structurally similar in the 
following respect: human morality evolves through learning 
and habituation influenced by social experience and practice, 
while the moral competence of LLMs is enhanced through 
mechanisms of reward and punishment. Nonetheless, our 
findings also indicate a profound difference between them. 
With the lack of self-reflective capabilities, LLMs have yet 
to attain the character stage as envisioned by Dewey, thereby 
preventing them from having moral competence equivalent 
to that of humans. Hence, as discussed in section "Limita-
tions and challenges of LLMs’ moral competence", vari-
ous ethical issues and unpredictable risks are still there, 
particularly those associated with potential manipulation 
and inducement, which cannot be addressed solely through 
RLHF. A comprehensive approach to the formation and gov-
ernance of LLMs’ moral competence remains essential, indi-
cating opportunities for future work across various dimen-
sions. Enhancing the capabilities of RLHF or RLAIF —as 
recently developed by Anthropic (Bai et al., 2022)—remains 
important; further, external societal governance and legal 
regulation are also significant. Addressing these complexi-
ties requires continual interdisciplinary investigation and 
research.
Explaining the moral development of LLMs through 
the lens of Dewey’s moral philosophy is only an initial 
step toward a comprehensive interpretive framework. The 
absence of a unified theory for human cognitive abilities 
and consciousness, coupled with a lack of theoretical expla-
nations for intrinsic mechanisms involving emergence and 
homogenization in LLMs, complicates the interpretation 
of LLM's moral capabilities. Achieving genuine ethical AI 
will require ongoing collaboration among engineers, phi-
losophers, policy-makers, and societal stakeholders.
Supplementary Information  The online version contains supplemen-
tary material available at https://​doi.​org/​10.​1007/​s10676-​024-​09818-x.
Acknowledgements  This work was partially supported by the National 
Key R&D Program of China (No. 2022ZD0160103), National Natural 
Science Foundation of China (No. L2224015) and Academic Divi-
sions of the Chinese Academy of Sciences “Digital Technology Ethics 
Research” project. Special thanks to Yu Qiao, Lingpeng Kong and 
Jiawei Sun for their assistance.
Author contributions  G. Y. Wang conceived and organized the study, 
contributed to the writing. W. Wang conducted the majority of the 
study and writing for the article, while Y. Q. Cao provided writing 
assistance. H.F. Wang supervised the experimental work and the writ-
ing. Y. T. and Q. Y. Guo assisted with both the study and the writing of 
the technical sections. J. J. Ma and J. Liu conducted the experiments. 
J. Y. Lin provided supportive assistance for the experimental work and 
Y.C. Wang provided support for the study.
Data and materials availability  All data and materials generated or 
analysed during this study are included in the manuscript and its sup-
plementary information files.
Declarations 
Conflict of interest  The authors have no competing interests to declare 
that are relevant to the content of this article.
Ethical approval  This article does not contain any studies with human 
participants performed by any of the authors.
Open Access   This article is licensed under a Creative Commons 
Attribution-NonCommercial-NoDerivatives 4.0 International License, 
which permits any non-commercial use, sharing, distribution and repro-
duction in any medium or format, as long as you give appropriate credit 
to the original author(s) and the source, provide a link to the Creative 
Commons licence, and indicate if you modified the licensed material. 
You do not have permission under this licence to share adapted material 
derived from this article or parts of it. The images or other third party 
material in this article are included in the article’s Creative Commons 
licence, unless indicated otherwise in a credit line to the material. If 
material is not included in the article’s Creative Commons licence and 
your intended use is not permitted by statutory regulation or exceeds 
the permitted use, you will need to obtain permission directly from the 
copyright holder. To view a copy of this licence, visit http://​creat​iveco​
mmons.​org/​licen​ses/​by-​nc-​nd/4.​0/.
References
Ames, R. T., & Rosemont, H. (2010). The analects of confucius: A 
philosophical translation. Random House Publishing Group.
Anderson, P. W. (1972). More Is Different: Broken symmetry and the 
nature of the hierarchical structure of science. Science, 177(4047), 
393–396.
Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., 
Chen, A., Goldie, A., Mirhoseini, A., & McKinnon, C. (2022). 
Constitutional ai: Harmlessness from ai feedback. arXiv:​2212.​
08073
Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von 
Arx, S., Bernstein, M. S., Bohg, J., Bosselut, A., & Brunskill, 
E. (2021). On the opportunities and risks of foundation models. 
arXiv:​2108.​07258
Brooks, R. A. (1991). Intelligence without representation. Artificial 
Intelligence, 47(1–3), 139–159.
Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, 
P., Neelakantan, A., Shyam, P., Sastry, G., & Askell, A. (2020). 
Language models are few-shot learners. Advances in Neural Infor-
mation Processing Systems, 33, 1877–1901.
Bryson, J. J. (2018). Patiency is not a virtue: The design of intelligent 
systems and systems of ethics. Ethics and Information Technol-
ogy, 20(1), 15–26. https://​doi.​org/​10.​1007/​s10676-​018-​9448-6
Butz, M. V. (2021). Towards strong AI. KI—Künstliche Intelligenz, 
35(1), 91–101. https://​doi.​org/​10.​1007/​s13218-​021-​00705-x
Cai, H. (2021). Reaching consensus with human beings through block-
chain as an ethical rule of strong artificial intelligence. AI and 
Ethics, 1(1), 55–59. https://​doi.​org/​10.​1007/​s43681-​020-​00005-4
Chowdhery, A., Narang, S., Devlin, J., Bosma, M., Mishra, G., Rob-
erts, A., Barham, P., Chung, H. W., Sutton, C., & Gehrmann, S.

--- Page 11 ---

Possibilities and challenges in the moral growth of large language models: a philosophical…
Page 11 of 11 
9
(2022). Palm: Scaling language modeling with pathways. arXiv:​
2204.​02311
Christiano, P., Shlegeris, B., & Amodei, D. (2018). Supervising strong 
learners by amplifying weak experts. arXiv:​1810.​08575
Dewey, J. (1981). The later works, 1925–1953. Southern Illinois Uni-
versity Press.
Dewey, J. (2008a). The middle works of John Dewey, volume 5, 1899–
1924: Ethics 1908. Southern Illinois University Press.
Dewey, J. (2008b). The middle works of John Dewey, volume 14, 
1899–1924: Human nature and conduct 1922. Southern Illinois 
University Press.
Dewey, J. (2008). Experience and nature. McCutchen Press.
Dewey, J. (1997). Democracy and education. Free Press.
Docherty, B. (2016, June 16). Losing control: The dangers of 
killer robots. The Conversation. Retrieved October 19, 2023, 
from https://​theco​nvers​ation.​com/​losing-​contr​ol-​the-​dange​
rs-​of-​killer-​robots-​58262
Foot, P. (1967). The problem of abortion and the doctrine of the double 
effect. Oxford Review, 5, 5–15.
Gabriel, I. (2020). Artificial intelligence, values, and alignment. Minds 
and Machines, 30(3), 411–437.
Greene, J. D., Sommerville, R. B., Nystrom, L. E., Darley, J. M., & 
Cohen, J. D. (2001). An fMRI investigation of emotional engage-
ment in moral judgment. Science, 293(5537), 2105–2108. http://​
www.​jstor.​org/​stable/​30845​64
Knox, W. B., & Stone, P. (2011). Augmenting reinforcement learning 
with human feedback. In ICML 2011 workshop on new develop-
ments in imitation learning (July 2011).
Kohlberg, L. (1958). The development of modes of moral thinking and 
choice in the years 10 to 16 The University of Chicago.
Lambert, N., Castricato, L., von Werra, L., & Havrilla, A. (2022). 
Illustrating reinforcement learning from human feedback (rlhf). 
Hugging Face Blog. https://​huggi​ngface.​co/​blog/​rlhf
Maslej, N., Fattorini, L., Brynjolfsson, E., Etchemendy, J., Ligett, K., 
Lyons, T., Manyika, J., Ngo, H., Niebles, J. C., Parli, V., Sho-
ham, Y., Wald, R., Clark, J., & Perrault, R. (2023). The AI Index 
2023 Annual Report. AI Index Steering Committee, Institute for 
Human-Centered AI, Stanford University.
Mitchell, M. (2019). Artificial intelligence: A guide for thinking 
humans. Farrar.
Murphey, M. G. (2008). Introduction. In J. Dewey, The middle works of 
John Dewey, volume 14, 1899–1924: Human nature and conduct 
1922 (pp. ix–xxiii). Southern Illinois University Press.
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., 
Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schul-
man, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., 
Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Train-
ing language models to follow instructions with human feedback. 
arXiv:​2203.​02155
Powers, T. M. (2006). Prospects for a Kantian machine. IEEE Intel-
ligent Systems, 21(4), 46–51.
Purves, D., Jenkins, R., & Strawser, B. J. (2015). Autonomous 
machines, moral judgment, and acting for the right reasons. Ethi-
cal Theory and Moral Practice, 18(4), 851–872. https://​doi.​org/​
10.​1007/​s10677-​015-​9563-y
Radford, A., Narasimhan, K., Salimans, T., & Sutskever, I. (2018). 
Improving language understanding by generative pre-training. 
OpenAI. https://​cdn.​openai.​com/​resea​rch-​covers/​langu​age-​unsup​
ervis​ed/​langu​age_​under​stand​ing_​paper.​pdf
Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., & Sutskever, I. 
(2019). Language models are unsupervised multitask learners. 
OpenAI Blog, 1(8), 9.
Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. 
(2017). Proximal policy optimization algorithms. arXiv:​1707.​
06347
Sharkey, A. (2020). Can we program or train robots to be good? Ethics 
and Information Technology, 22(4), 283–295. https://​doi.​org/​10.​
1007/​s10676-​017-​9425-5
Sun H., Zhang Z., Mi F., Wang Y., Liu W., Cui J., Wang B., Liu Q., & 
Huang M. (2023). Moraldial: A framework to train and evaluate 
moral dialogue systems via moral discussions. In Proceedings 
of the 61st annual meeting of the association for computational 
linguistics (vol. 1: Long Papers, pp. 2213–2230).
Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning (2nd 
ed.). MIT Press.
Thomson, J. J. (1985). The Trolley problem. The Yale Law Journal, 
94(6), 1395–1415. https://​doi.​org/​10.​2307/​796133
Wallach, W., & Allen, C. (2008). Moral machines: Teaching robots 
right from wrong. Oxford University Press, Inc.
Weidinger, L., McKee, K. R., Everett, R., Huang, S., Zhu, T. O., Chad-
wick, M. J., Summerfield, C., & Gabriel, I. (2023). Using the 
Veil of Ignorance to align AI systems with principles of justice. 
Proceedings of the National Academy of Sciences of the United 
States of America, 120(18), e2213709120.
Yuan, L., Gao, X., Zheng, Z., Edmonds, M., Wu, Y. N., Rossano, F., 
Lu, H., Zhu, Y., & Zhu, S.-C. (2022). In situ bidirectional human-
robot value alignment. Science Robotics, 7(68), eabm4183.
Ziems C., Yu J. A., Wang Y.-C., Halevy A., & Yang D. (2022). The 
moral integrity corpus: A benchmark for ethical dialogue systems. 
arXiv:​2204.​03021
Publisher's Note  Springer Nature remains neutral with regard to 
jurisdictional claims in published maps and institutional affiliations.

```
