---
title: "2025-Qi-A Cross-Cultural Comparison of LLM-based Public Opinion Simulation - PDF Extract"
source_pdf: "2025-Qi-A Cross-Cultural Comparison of LLM-based Public Opinion Simulation.pdf"
pages: 8
extracted_at: "2026-02-15T17:54:27.979236"
---

# PDF Extract: 2025-Qi-A Cross-Cultural Comparison of LLM-based Public Opinion Simulation

**Source PDF:** 2025-Qi-A Cross-Cultural Comparison of LLM-based Public Opinion Simulation.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

A Cross-Cultural Comparison of LLM-based Public
Opinion Simulation: Evaluating Chinese and U.S.
Models on Diverse Societies
Weihong Qi
wq3@iu.edu
Indiana University Bloomington
Bloomington, IN, USA
Fan Huang
fanhuan@iu.edu
Indiana University Bloomington
Bloomington, IN, USA
Jisun An
jisunan@iu.edu
Indiana University Bloomington
Bloomington, IN, USA
Haewoon Kwak
hwkwak@iu.edu
Indiana University Bloomington
Bloomington, IN, USA
Abstract—This study evaluates the ability of DeepSeek, an
open-source large language model (LLM), to simulate public
opinions in comparison to LLMs developed by major tech
companies. By comparing DeepSeek-R1 and DeepSeek-V3 with
Qwen2.5, GPT-4o, and Llama-3.3 and utilizing survey data
from the American National Election Studies (ANES) and the
Zuobiao dataset of China, we assess these models’ capacity to
predict public opinions on social issues in both China and the
United States, highlighting their comparative capabilities between
countries. Our findings indicate that DeepSeek-V3 performs best
in simulating U.S. opinions on the abortion issue compared to
other topics such as climate change, gun control, immigration,
and services for same-sex couples, primarily because it more
accurately simulates responses when provided with Democratic
or liberal personas. For Chinese samples, DeepSeek-V3 performs
best in simulating opinions on foreign aid and individualism but
shows limitations in modeling views on capitalism, particularly
failing to capture the stances of low-income and non-college-
educated individuals. It does not exhibit significant differences
from other models in simulating opinions on traditionalism
and the free market. Further analysis reveals that all LLMs
exhibit the tendency to overgeneralize a single perspective within
demographic groups, often defaulting to consistent responses
within groups. These findings highlight the need to mitigate
cultural and demographic biases in LLM-driven public opinion
modeling, calling for approaches such as more inclusive training
methodologies.
Index Terms—large language model, cultural comparison,
public opinions
I. INTRODUCTION
The release of DeepSeek, an open-source model developed
in China, marks a significant milestone in the development
of large language models (LLMs), emerging as a strong
competitor following the launch of ChatGPT in November
2022 [15]. Its strong performance invites broader evaluations
beyond benchmark scores [5], [23], particularly regarding
fairness and cultural representation, as the model is expected to
see widespread use due to its competitive cost. Recent studies
have examined cultural biases in dominant models, finding
that they often align more closely with English-speaking or
Western-centric values [22], [25].
The emergence of a competitive non-Western LLM there-
fore presents a critical test case: Are cultural biases an
inevitable byproduct of current LLM development practices,
or can a model built within a different cultural ecosystem offer
a more balanced perspective?
This study addresses that question by investigating whether
DeepSeek can more accurately capture public opinions across
the United States and China compared to prominent U.S. and
Chinese counterparts, including GPT-4o [1], Llama-3.3-70B-
Instruct-Turbo [9], and Qwen-2.5-72B-Instruct-Turbo [29].
Using survey data from the American National Election Stud-
ies (ANES) [2] and China’s Zuobiao dataset [20], we evaluate
how these models simulate opinions on controversial social
issues in both nations.
Specifically, we focus on the following research questions:
• RQ1. Does an LLM’s cultural origin create a “home-field
advantage” in simulating public opinion within its native
cultural context, or does it introduce distinct cultural
biases when modeling opinions cross-culturally?
• RQ2. How do these cultural and demographic biases
manifest in LLM simulations? Specifically, do models
systematically overgeneralize or underrepresent certain
societal groups in culturally-patterned ways?
In particular, we provide a prompt that simulates each
survey participant by specifying their demographic attributes
available in the survey, including ethnicity, gender, age, po-
litical leaning, income, and education level. We then pose
survey questions to the LLMs, and the responses are treated as
the LLM’s simulated answers for that individual. Finally, we
aggregate and evaluate the performance for each demographic
group and LLM.
arXiv:2506.21587v2  [cs.CL]  12 Sep 2025

--- Page 2 ---

Our findings indicate that an LLM’s cultural origin does not
confer a straightforward ‘home-field advantage’ in simulating
public opinion. DeepSeek, despite its development in China,
fails to demonstrate a consistent or significant advantage
in modeling Chinese societal views compared to its U.S.-
based counterparts. Instead, our cross-cultural analysis reveals
that all evaluated LLMs, regardless of origin, exhibit signifi-
cant cultural and demographic biases. These models struggle
to capture the nuanced perspectives within specific societal
groups, often defaulting to stereotyped or overgeneralized
responses.
This tendency is highlighted by DeepSeek-V3’s mixed
performance. While it more accurately simulates the opinions
of U.S. Democrats and liberals on the issue of abortion,
it simultaneously fails to represent their Republican and
conservative counterparts. Similarly, in the Chinese context,
most models struggle to model the views of low-income and
non-college-educated individuals on capitalism. This flaw is
exemplified in the extreme by Qwen2.5; although it appeared
to outperform other models on this topic, its high accuracy was
achieved by defaulting to a single, uniform response for these
demographic groups, mistaking overgeneralization for accurate
representation. These results suggest the core issue is not a
simple East-West divide but a deeper, more systemic failure
of current LLMs to achieve genuine cultural and demographic
sensitivity.
II. RELATED WORK
Prior to the release of DeepSeek, extensive research has
been conducted on the fairness and inclusion of LLMs. For
example, [4], [5], [16] develop metrics and tools to evaluate
AI fairness. Other studies focusing on the representation
of specific social groups have identified biases related to
gender [28], culture [18], race [13], political leanings [11],
political affiliations and institutions [22]. However, existing
research has two key limitations. First, although some studies
have included LLMs developed by teams from non-U.S.
cultural backgrounds [18], [30], the primary focus remains on
American AI models, with limited attention to potential biases
stemming from differences in the training corpus and the
development teams’ cultural backgrounds. Second, while these
studies have identified various biases [7], [25], [28], they often
fall short of uncovering the underlying sources of these biases
or proposing potential solutions. The comparable performance
of DeepSeek to American models offers an opportunity to
further investigate these issues. Our study aims to bridge these
gaps in the literature.
Representative bias can stem from various sources, one
of which is how developers sample populations during the
training data collection process [24]. Non-representative sam-
ples lead to demonstrable biases against certain groups. For
example, [8] finds that a lack of geographical diversity in
datasets, such as ImageNet, results in biases favoring Western
cultures. Similarly, since English-language corpora constitute
the majority of training data for most popular LLMs [1],
[26], [27], these models may exhibit biases favoring English-
speaking populations. Moreover, models trained within spe-
cific cultural contexts can encode and perpetuate harmful
human biases [3]. Several studies have identified cultural
biases and a lack of cultural understanding in LLMs [14],
[25]. Our research extends these investigations by examining
the newly released DeepSeek model and its simulations of
public opinions. This is particularly significant as DeepSeek,
developed by a team in China, offers a contrasting cultural and
commercial background compared to popular LLMs like the
GPT and LLaMA series. This comparison allows us to explore
whether cultural differences in development teams contribute
to variations in opinion simulation.
III. METHOD
Fig. 1.
Overview of the Evaluation Process for LLMs in Public Opinion
Simulation
A. Datasets
We utilize the 2020 American National Election Studies
(ANES) and the Zuobiao Dataset of China [20] as benchmarks
of human ground truth to evaluate LLMs in public opinion
simulation. ANES data series are academically conducted
national surveys of U.S. citizens, administered before and
after presidential election cycles. These surveys follow a
longstanding tradition, with data collection dating back to
1948. The survey data includes multiple questions on essential
issues, such as abortion, climate change, and gun control,
in the election cycle. The 2020 ANES dataset consists of
responses from 2,457 individuals. The Zuobiao dataset, devel-
oped by [20], is based on online surveys designed to capture
the ideological spectrum of Chinese citizens across various
dimensions, such as capitalism, foreign aid, traditionalism,
individualism, and the free market. This dataset contains
opinions and stances from over 470,000 individuals. To ensure
comparability between the two datasets, we randomly sample
2,000 individuals from the Zuobiao dataset. Both datasets also
contain individual-level information, such as demographics
and socioeconomic status, which is essential in public opinion
research [10], [17].

--- Page 3 ---

We use survey questions from both datasets that are con-
sidered representative of public opinion at the time of data
collection [2], [20] for our simulations and evaluations. From
the ANES dataset, we include questions on abortion, climate
change, gun control, immigration, and services for same-sex
couples. From the Zuobiao dataset, we include questions on
capitalism, foreign aid, traditionalism, individualism, and the
free market. Detailed descriptions of these 10 questions are
provided in the Appendix A.
For the individual-level simulation using LLMs, we extract
individual attributes from both datasets. From the ANES
dataset, we include race, gender, age, educational level, in-
come, religious beliefs, ideology, and partisanship. From the
Zuobiao dataset, we include gender, age, educational level, and
income. The feature selection is consistent with the political
science research using these datasets [6], [20], which also
considers them to be important factors influencing public
opinions. The discrepancies in the selected features between
the American and Chinese samples result from adaptations to
the social and cultural contexts of the two countries. Certain
attributes, such as race and religious beliefs, are more salient
and exhibit greater variability within the U.S. population than
in China. For example, the majority of the Chinese population
belongs to the Han ethnic group (91.11% as of 2021) [19].
Only 10% of Chinese adults identified with any religious
group in the 2018 Chinese General Social Survey (CGSS) [21].
Figure 1 summarizes our evaluation process for the LLMs in
public opinion simulation.
B. Experimental Design
We incorporate individual information into the LLM
prompts to reflect demographic variations within populations.
Due to space constraints, we present the English prompt
for the ANES dataset here, while the survey questions and
corresponding prompts for the Chinese dataset are provided in
the Appendix section. An example of the designed prompt
for public opinion simulation is as follows:
System: Imagine you are a(n) {country} citi-
zen.
Prompt: You are a {race} individual and
identify as {gender}. You are {age}, have
{highest degree}, and your annual income
is {income}. Your religious beliefs align with
{religious belief}. Politically, you identify
as {ideology} and {party} in party align-
ment. What is your opinion to the question:
{Question}. Only respond one of the three an-
swer: {Options}.
We then compute the simulation accuracies using the fol-
lowing method:
Accuracy =
PN
i Ii(M = H)
N
(1)
In this formula, M represent the simulated opinion by
the LLM models, H represents the ground truth opinion of
humans, and Ii is an indicator function that equals 1 if the two
values are considered equivalent, and 0 otherwise. N denotes
the total number of observations.
For subgroup accuracy, we calculate the accuracy based
solely on the specified subpopulation:
AccuracyG =
PNG
i
Ii(MG = HG)
NG
(2)
In Equation (2), MG, HG, and NG also denote the simulated
opinions by the LLMs, the ground truth human opinions, and
the total number of individuals, respectively, but restricted to
the specified subgroup G.
By comparing the simulation accuracies of different models
on questions from diverse social and cultural contexts, we eval-
uate whether DeepSeek can simulate public opinion better than
other LLMs. Furthermore, when significant discrepancies arise
between human opinions and those simulated by DeepSeek—
or between DeepSeek and other models—we break down the
accuracies by demographic groups to investigate the sources of
these differences. This analysis helps identify potential biases
toward specific demographic groups within the LLMs.
C. Models
Our study involves experiments with five LLMs: DeepSeek-
R1, DeepSeek-V3, Qwen2.5-72B-Instruct-Turbo, Llama-3.3-
70B-Instruct-Turbo, GPT-4o. For simplicity, we refer to
Qwen2.5-72B-Instruct-Turbo as Qwen2.5 and Llama-3.3-70B-
Instruct-Turbo as Llama-3.3. Among these models, the two
DeepSeek models are the primary focus of this study. They
represent a significant competitor to OpenAI’s GPT series
and are open-source. As comparisons, Qwen2.5 provides a
perspective as another open-source LLM developed in China.
GPT-4o and Llama-3.3 represent models developed by U.S.-
based tech companies.
IV. RESULTS
A. Overall Performance
We begin by examining the simulation accuracy of all
five models. Notably, DeepSeek-R1 shows significantly lower
accuracy across all topics, primarily due to a high proportion
of invalid responses (averaging 57% and reaching as high
as 99.6%), where the model refuses to give the requested
answers. Detailed results are provided in Appendix B. The
model’s long-form reasoning style, which often results in
responses exceeding the output window. The potential in-built
censorship mechanism of LLMs, particularly in responses to
questions related to China, appears to be the main cause of
these invalid outputs. These findings suggest that reasoning-
focused models like DeepSeek-R1 require further prompt
adaptation for effective use in public opinion simulations
and may be more prone to content filtering when addressing
sensitive topics. Due to the high share of invalid responses
of DeepSeek-R1, the remainder of this section focuses on the
other four models for further analysis.
Figure 2 presents the overall simulation accuracies of GPT-
4o, DeepSeek-V3, Qwen2.5, and Llama-3.3 on five public

--- Page 4 ---

Abortion
Climate
Gun Control
Immigration
Same-sex
Couple Service
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
0.53
0.65
0.71
0.59
0.73
0.41
0.65
0.67
0.59
0.73
0.38
0.66
0.73
0.60
0.73
0.46
0.63
0.57
0.60
0.73
LLM Simulation of U.S. Public Opinions
deepseek-v3
qwen
gpt-4o
llama
Capitalism
Foreign Aid
Traditionalism
Indivisualism
Free Market
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
0.36
0.42
0.52
0.29
0.29
0.54
0.34
0.58
0.28
0.25
0.30
0.41
0.57
0.28
0.33
0.32
0.35
0.50
0.27
0.23
LLM Simulation of Chinese Public Opinions
deepseek-v3
qwen
gpt-4o
llama
Fig. 2. Simulation results for US and Chinese samples in public opinions
TABLE I
SIMULATION ACCURACY OF PUBLIC OPINIONS ON ABORTION BY PARTY AFFILIATION AND IDEOLOGY WITH U.S. SAMPLES
Party
Ideology
Model
Democrat
Republican
Independent
Liberal
Conservative
Moderate
DeepSeek-V3
0.6510
0.3956
0.5286
0.7301
0.4207
0.3614
Qwen2.5
0.3268
0.5267
0.3711
0.3132
0.5350
0.3560
GPT-4o
0.2232
0.5983
0.3488
0.1984
0.5989
0.3560
Llama-3.3
0.5930
0.3263
0.4537
0.6483
0.3326
0.3560
Group Size
914
809
734
978
559
920
TABLE II
SIMULATION ACCURACY OF PUBLIC OPINIONS ON CAPITALISM BY INCOME AND EDUCATION LEVEL WITH CHINESE SAMPLES
Income
Education
Model
Low Income
Medium Income
High Income
No College Degree
College Degree
DeepSeek-V3
0.1390
0.5377
0.5028
0.2396
0.3309
Qwen2.5
0.5547
0.5662
0.4176
0.5503
0.5319
GPT-4o
0.1241
0.4156
0.5028
0.1598
0.3321
Llama-3.3
0.1116
0.5688
0.2699
0.2396
0.3309
Group Size
878
770
352
338
1662
opinion questions from American and Chinese samples, re-
spectively. Specifically, DeepSeek does not exhibit significant
differences with other models in most of the topics, with
slight advantages of 0.01 in accuracy in simulating opinions on
foreign aid and individualism in the Zuobiao dataset. However,
there are two notable exceptions. On the abortion issue in
the ANES dataset, DeepSeek achieves a significantly higher
accuracy of 0.53, compared to a maximum of 0.46 among
the other models. Conversely, it underperforms compared to
Qwen2.5 in simulating opinions on capitalism in the Zuobiao
dataset, with an accuracy of 0.36 versus 0.54.
B. Which Groups Are Accurately Simulated, and Which Are
Not?
As shown in Figure 2, DeepSeek-V3 demonstrates a signif-
icant advantage in simulating opinions on the abortion issue
with American samples but performs poorly on the capitalism
question with Chinese samples, particularly in comparison
to Qwen2.5. Why does DeepSeek-V3 perform well on some
issues but poorly on others? To further investigate the sources
of these discrepancies and identify potential biases in the
LLMs, we conduct a group-level breakdown of simulation
accuracy across demographic features.
As shown in Figure 3, the largest differences between
DeepSeek and GPT-4o in public opinion simulation on the
abortion issue appear among subgroups defined by partisan-
ship and ideology. Although these two features are highly
correlated (Cramer’s V= 0.54), we keep them separate in the
analysis because they are treated as distinct variables in the
original survey data.
Table I presents the simulation accuracies by party affil-
iation and ideology for the abortion issue using American
samples, where all models exhibiting their lowest accuracy
on this topic. The breakdown accuracy with other attributes is
reported in Table III in the Appendix. The accurate simulation
performance of DeepSeek-V3 is primarily driven by its accu-

--- Page 5 ---

never
conditionally
always
Predicted Label
never
conditionally
always
True Label
0
(0)
21
(-4)
4
(+4)
1
(+1)
109
(-56)
57
(+55)
1
(+1)
235
(-448)
486
(+447)
(a) Democrats: Difference in Predictions (DeepSeek 
 GPT-4o)
never
conditionally
always
Predicted Label
never
conditionally
always
True Label
0
(0)
11
(-172)
6
(+6)
0
(0)
78
(-473)
78
(+78)
0
(-1)
169
(-16)
636
(+636)
(b) Liberals: Difference in Predictions (DeepSeek 
 GPT-4o)
Fig. 3. Confusion Matrices for Public Opinion Simulation Differences Using
U.S. Data with DeepSeek and GPT-4o. The values are DeepSeek predictions,
and the values in parentheses represent the difference: DeepSeek - GPT-
4o. The question on Abortion issue is: Should abortion permitted by law?
Only respond one of the three answers: Should never be permitted, should be
permitted conditionally, should always permitted.
rate representation of opinions from Democratic and liberal
respondents. As shown in the confusion matrix in Figure 3,
while other LLMs, such as GPT-4o, tend to underestimate
the liberal alignment of Democrats and liberals, DeepSeek-
V3 predicts their responses more accurately. Llama-3.3 shows
a similar pattern, though with lower accuracy than DeepSeek-
V3. However, when simulating the opinions of Republicans
and conservatives, we observe the opposite trend across the
models. DeepSeek-V3 and Llama-3.3, which perform better
for Democrats and liberals, exhibit lower accuracy for Repub-
licans and conservatives (See Table I). In contrast, Qwen2.5
and GPT-4o achieve higher accuracy for Republicans and
conservatives, but perform worse for Democrats and liberals.
For the capitalism issue in China, income and education
level show the largest performance gaps among all demo-
graphic features, as shown in Table II and Table IV in the
Appendix.
As low-income individuals make up 43.9% of the full pop-
strongly disagree
disagree
agree
strongly agree
Predicted Label
strongly disagree
disagree
agree
strongly agree
True Label
0
(0)
0
(0)
0
(0)
0
(0)
0
(0)
95
(+95)
3
(-95)
0
(0)
0
(0)
461
(+461)
27
(-460)
0
(-1)
0
(0)
218
(+218)
8
(-218)
0
(0)
(a) Low Income: Difference in Predictions (DeepSeek 
 Qwen2.5)
strongly disagree
disagree
agree
strongly agree
Predicted Label
strongly disagree
disagree
agree
strongly agree
True Label
0
(0)
0
(0)
0
(0)
0
(0)
0
(0)
32
(+32)
15
(-30)
0
(-2)
0
(0)
140
(+140)
44
(-137)
0
(-3)
0
(0)
62
(+62)
19
(-57)
0
(-5)
(b) No College Degree: Difference in Predictions (DeepSeek 
 Qwen2.5)
Fig. 4.
Confusion Matrices for Public Opinion Simulation Differences
Using Zuobiao Data with DeepSeek and Qwen2.5. The values are DeepSeek
predictions, and the values in parentheses represent the difference: DeepSeek
- Qwen2.5. The question on Capitalism is: Do you agree or disagree the
statement: A rich person deserves better medical services. Respond one of
the four answers: (1) strongly disagree, (2) disagree, (3) agree, or (4) strongly
agree.
ulation, the results indicate that DeepSeek-V3’s poor perfor-
mance in representing Chinese public opinions on capitalism
is primarily due to its low accuracy in simulating the opinions
of low-income individuals and those without a college degree.
A similar pattern is observed in the performance of GPT-
4o and Llama-3.3. Only Qwen2.5 demonstrates a notably
accurate representation of low-income individuals and those
without a college degree. This raises an important question:
does Qwen2.5 provide a fairer representation of marginalized
populations compared to the other models?
Contrary to what one might expect, the answer is no.
Rather, a closer analysis reveals an undesirable pattern in

--- Page 6 ---

Qwen2.5’s behavior. The confusion matrix in Figure 4 shows
that Qwen2.5 returns the same response to 99.89% and 96.15%
of all survey questions when the prompt specifies low income
and no college degree, regardless of any other demographic
information.
C. Evaluating the Prompts Language Sensitivity in LLM Sim-
ulations
Prior research has shown that training data in different
languages can introduce distinct biases in LLMs [14], and the
use of different languages could result in significantly different
outputs of LLMs [31]. To explore this, we repeat the exper-
iments with the Zuobiao dataset using prompts in simplified
Chinese and compare the outcomes to those obtained using
English prompts.
Figure 5 presents the simulation results using Chinese
prompts. Overall, Chinese prompts do not lead to consistent
and significant improvements in simulation accuracy across
tasks. The exceptions are that Chinese prompts enhance sim-
ulation accuracy for most LLMs on the capitalism issue and
improve performance on individualism for both Qwen2.5 and
GPT-4o. However, using Chinese prompts does not offer a
notable advantage for DeepSeek-V3 in most tasks. These re-
sults suggest that changing the prompt language can influence
model performance on certain topics, but does not lead to
consistent improvements across all areas. Therefore, simply
switching languages does not reliably enhance simulation
accuracy across cultural contexts.
V. CONCLUSIONS AND DISCUSSIONS
In this study, we investigate the capability of DeepSeek,
an open-source LLM, to simulate public opinions compared
to other prominent LLMs, including GPT-4o, Qwen2.5, and
Llama-3.3. Using public opinion survey data from the Ameri-
can National Election Studies (ANES) and the Zuobiao dataset
of China, we evaluate the models’ accuracy in simulating
responses across key social and political issues. Our analysis
highlights both strengths and limitations of DeepSeek, offering
insights into possible model biases and cross-cultural represen-
tation.
Our results show that DeepSeek demonstrates accurate
simulation performance on certain issues, but poor perfor-
mance with others. Specifically, DeepSeek achieves the highest
accuracy in simulating public opinions on abortion among U.S.
respondents, outperforming other prominent LLMs by effec-
tively capturing the perspectives of Democratic and liberal
respondents. However, it performs poorly in simulating Repub-
lican and conservative opinions, where GPT-4o and Qwen2.5
show better alignment. This highlights that DeepSeek’s ad-
vantages in some demographic segments are accompanied by
significant limitations in others.
In contrast, for the Chinese samples, DeepSeek performs
best on questions related to foreign aid and individualism. Yet,
it exhibits notable weaknesses in simulating other opinions,
particularly among low-income individuals and those without a
college degree. Our breakdown analysis of model performance
by income and education reveals that DeepSeek and other
LLMs fail to capture the diversity of opinions within these
demographic groups. Although Qwen2.5 appears to perform
better, the confusion matrix analysis shows that it, too, de-
faults to a uniform response pattern, indicating self-reinforcing
biases rather than a genuine representation of demographic
differences. Our results also indicate that simply switching
the prompt language to Chinese does not make a consistent
improvement in simulation accuracy for the Chinese samples.
These findings highlight that demographic underrepresenta-
tion and cultural biases remain critical challenges for LLMs,
regardless of their geographic origin or training methodolo-
gies. While DeepSeek performs comparably to or better than
U.S.-developed models on certain issues, it does not demon-
strate a distinct advantage in simulating Chinese public opin-
ion. Instead, both Chinese- and U.S.-developed models show
biases driven by overgeneralization and limited sensitivity to
demographic diversity. Overall, our study highlights the impor-
tance of addressing demographic and cultural biases in LLMs
to improve public opinion simulations and representations. As
LLMs continue to play a central role in human-AI interactions,
future research should focus on refining training datasets and
modeling techniques to mitigate biases and enhance their
ability to represent diverse global perspectives accurately.
REFERENCES
[1] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman,
D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al., “GPT-4
technical report,” arXiv preprint arXiv:2303.08774, 2023.
[2] American
National
Election
Studies,
“ANES
2020
Time
Series
Study Full Release,” Feb. 10, 2022 version. [Online]. Available:
https://www.electionstudies.org, 2021.
[3] A. Arseniev-Koehler and J. G. Foster, “Machine learning as a model
for cultural learning: Teaching an algorithm what it means to be fat,”
Sociological Methods & Research, vol. 51, no. 4, pp. 1484–1539, 2022.
[4] J. Atwood, P. Lahoti, A. Balashankar, F. Prost, and A. Beirami,
“Inducing group fairness in LLM-based decisions,” arXiv preprint
arXiv:2406.16738, 2024.
[5] S. Bird, M. Dud´ık, R. Edgar, B. Horn, R. Lutz, V. Milan, M. Sameki,
H. Wallach, and K. Walker, “Fairlearn: A toolkit for assessing and
improving fairness in AI,” Microsoft, Tech. Rep. MSR-TR-2020-32,
2020.
[6] J. Bisbee, J. D. Clinton, C. Dorff, B. Kenkel, and J. M. Larson,
“Synthetic replacements for human survey data? The perils of large
language models,” Political Analysis, vol. 32, no. 4, pp. 401–416, 2024.
[7] Y. Cao, L. Zhou, S. Lee, L. Cabello, M. Chen, and D. Hershcovich, “As-
sessing cross-cultural alignment between ChatGPT and human societies:
An empirical study,” arXiv preprint arXiv:2303.17466, 2023.
[8] S. Caton and C. Haas, “Fairness in machine learning: A survey,” ACM
Computing Surveys, vol. 56, no. 7, pp. 1–38, 2024.
[9] A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, A. Letman,
A. Mathur, A. Schelten, A. Yang, A. Fan, et al., “The LLaMA 3 herd
of models,” arXiv preprint arXiv:2407.21783, 2024.
[10] R. S. Erikson and K. L. Tedin, American Public Opinion: Its Origins,
Content, and Impact. Routledge, 2019.
[11] S. Feng, C. Y. Park, Y. Liu, and Y. Tsvetkov, “From pretraining data
to language models to downstream tasks: Tracking the trails of political
biases leading to unfair NLP models,” in Proc. 61st Annu. Meeting
Assoc. Comput. Linguistics (ACL), 2023.
[12] I. O. Gallegos, R. A. Rossi, J. Barrow, M. M. Tanjim, S. Kim, F.
Dernoncourt, T. Yu, R. Zhang, and N. K. Ahmed, “Bias and fairness
in large language models: A survey,” Computational Linguistics, vol.
50, no. 3, pp. 1097–1179, 2024.
[13] A. Haim, A. Salinas, and J. Nyarko, “What’s in a name? Audit-
ing large language models for race and gender bias,” arXiv preprint
arXiv:2402.14875, 2024.

--- Page 7 ---

Capitalism
Foreign Aid
Traditionalism
Indivisualism
Free Market
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
0.36
0.42
0.52
0.29
0.29
0.54
0.34
0.58
0.28
0.25
0.30
0.41
0.57
0.28
0.33
0.32
0.35
0.50
0.27
0.23
LLM Simulation of Chinese Public Opinions (English)
deepseek-v3
qwen
gpt-4o
llama
Capitalism
Foreign Aid
Traditionalism
Indivisualism
Free Market
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
0.25
0.42
0.53
0.17
0.33
0.55
0.41
0.53
0.42
0.33
0.55
0.42
0.34
0.58
0.33
0.55
0.42
0.53
0.13
0.33
LLM Simulation of Chinese Public Opinions (Chinese)
deepseek-v3
qwen
gpt-4o
llama
Fig. 5. Simulation results for Chinese samples in public opinions with English and Chinese Prompts
[14] J. Kharchenko, T. Roosta, A. Chadha, and C. Shah, “How well do
LLMs represent values across cultures? Empirical analysis of LLM
responses based on Hofstede cultural dimensions,” arXiv preprint
arXiv:2406.14805, 2024.
[15] A. Liu, B. Feng, B. Xue, B. Wang, B. Wu, C. Lu, C. Zhao, C. Deng, C.
Zhang, C. Ruan, et al., “DeepSeek-V3 technical report,” arXiv preprint
arXiv:2412.19437, 2024.
[16] M. Madaio, L. Egede, H. Subramonyam, J. Wortman Vaughan, and
H. Wallach, “Assessing the fairness of AI systems: AI practitioners’
processes, challenges, and needs for support,” Proc. ACM Human-
Computer Interaction, vol. 6, no. CSCW1, pp. 1–26, 2022.
[17] M. McCombs and S. Valenzuela, Setting the Agenda: Mass Media and
Public Opinion. John Wiley & Sons, 2020.
[18] T. Naous, M. J. Ryan, A. Ritter, and W. Xu, “Having beer after prayer?
Measuring cultural bias in large language models,” arXiv preprint
arXiv:2305.14456, 2023.
[19] National Bureau of Statistics of China, “Bulletin of the Seventh National
Population Census (No. 2),” 2021. [Online]. Available: https://www.
stats.gov.cn/sj/tjgb/rkpcgb/qgrkpcgb/202302/t20230206 1902002.html.
Accessed: Feb. 15, 2025.
[20] J. Pan and Y. Xu, “China’s ideological spectrum,” The Journal of
Politics, vol. 80, no. 1, pp. 254–273, 2018.
[21] Pew Research Center, “Measuring Religion in China,” 2023. [Online].
Available: https://www.pewresearch.org/religion/2023/08/30/measuring-
religion-in-china/. Accessed: Feb. 15, 2025.
[22] W. Qi, H. Lyu, and J. Luo, “Representation bias in political sample sim-
ulations with large language models,” arXiv preprint arXiv:2407.11409,
2024.
[23] Y. Sheng, S. Cao, D. Li, B. Zhu, Z. Li, D. Zhuo, J. E. Gonzalez, and
I. Stoica, “Fairness in serving large language models,” in Proc. 18th
USENIX Symp. Operating Systems Design and Implementation (OSDI),
pp. 965–988, 2024.
[24] H. Suresh and J. V. Guttag, “A framework for understanding unintended
consequences of machine learning,” arXiv preprint arXiv:1901.10002,
vol. 2, no. 8, p. 73, 2019.
[25] Y. Tao, O. Viberg, R. S. Baker, and R. F. Kizilcec, “Cultural bias and
cultural alignment of large language models,” PNAS Nexus, vol. 3, no.
9, p. pgae346, 2024.
[26] A. Taubenfeld, Y. Dover, R. Reichart, and A. Goldstein, “Systematic
biases in LLM simulations of debates,” arXiv preprint arXiv:2402.04049,
2024.
[27] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux,
T. Lacroix, B. Rozi`ere, N. Goyal, E. Hambro, F. Azhar, et al.,
“LLaMA: Open and efficient foundation language models,” arXiv
preprint arXiv:2302.13971, 2023.
[28] Y. Wan, G. Pu, J. Sun, A. Garimella, K.-W. Chang, and N. Peng, “Kelly
is a warm person, Joseph is a role model: Gender biases in LLM-
generated reference letters,” arXiv preprint arXiv:2310.09219, 2023.
[29] A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Li, D. Liu,
F. Huang, H. Wei, et al., “Qwen2.5 technical report,” arXiv preprint
arXiv:2412.15115, 2024.
[30] J. Ye, Y. Wang, Y. Huang, D. Chen, Q. Zhang, N. Moniz, T. Gao, W.
Geyer, C. Huang, P.-Y. Chen, et al., “Justice or prejudice? Quantifying
biases in LLM-as-a-judge,” arXiv preprint arXiv:2410.02736, 2024.
[31] Q. Zhong, Y. Yun, and A. Sun, “Cultural value differences of LLMs:
Prompt, language, and model size,” arXiv preprint arXiv:2407.16891,
2024.
APPENDIX
A. Survey Questions on Public Opinions
Public Opinion Questions for the United States Sample.
The following questions from the ANES dataset are used
in our experiments, including abortion, climate change, gun
control, immigration, and services for same-sex couples:
• Immigration: What is your opinion to the question: Favor
or oppose returning unauthorized immigrants to native
country? Only respond one of the three answer: Favor,
Oppose, Neither favor nor oppose.
• Gun control: Should federal government make it more
difficult or easier to buy a gun? Only respond one of the
three answer: More difficult, Easier, or keep these rules
about the same.
• Abortion: Should abortion permitted by law? Only re-
spond one of the three answers: Should never be per-
mitted, should be permitted conditionally, should always
permitted.
• Climate change: How much is climate change affecting
severe weather/temperatures in US? Only respond the
number of one of the three answers: (1) Little or not
at all, (2) Moderate, (3) A lot or a great deal.
• Same-sex couple service: Do you think business owners
who provide wedding-related services should be allowed
to refuse services to same-sex couples if same-sex mar-
riage violates their religious beliefs, or do you think
business owners should be required to provide services
regardless of a couple’s sexual orientation? Only respond
one of the two answers: Should be allowed to refuse or
Should be required to provide service.
Public Opinion Questions for the Chinese Sample. The
following questions from the Zuobiao dataset are used in our
experiments, focusing on public opinions in China, including

--- Page 8 ---

TABLE III
SIMULATION ACCURACY OF PUBLIC OPINIONS ON ABORTION WITH U.S.
SAMPLES BY DEMOGRAPHICS AND SOCIOECONOMIC STATUS
DeepSeek-V3
Qwen2.5
GPT-4o
Llama-3.3
Female
0.5488
0.4179
0.4128
0.4490
Male
0.5105
0.3943
0.3575
0.4772
White
0.5339
0.4183
0.4019
0.4681
Black
0.5437
0.2427
0.2330
0.3883
Hispanic
0.4923
0.3949
0.3590
0.4615
Asian
0.5421
0.3832
0.2804
0.4766
Native American
0.4773
0.3182
0.2955
0.4091
18–30 years old
0.6278
0.4479
0.3091
0.5836
30-45 years old
0.5583
0.4013
0.3317
0.5217
45-60 years old
0.5162
0.4051
0.3885
0.4478
Over 60 years old
0.4898
0.3951
0.4380
0.3984
No college degree
0.4591
0.3930
0.4339
0.4038
College degree
0.5668
0.4122
0.3588
0.4942
Less than $35,000
0.4856
0.3424
0.3916
0.4203
$35,000 to $90,000
0.5236
0.4124
0.3970
0.4591
Above $90,000
0.5576
0.4310
0.3702
0.4883
capitalism, foreign aid, traditionalism, individualism, and the
free market:
• Capitalism: Do you agree or disagree the statement:
A rich person deserves better medical services. Only
respond one of the four answers: (1) strongly disagree,
(2) disagree, (3) agree, or (4) strongly agree.
• Foreign Aid: Do you agree or disagree the statement:
The state has an obligation to provide foreign aid. Only
respond one of the four answers: (1) strongly disagree,
(2) disagree, (3) agree, or (4) strongly agree.
• Traditionalism: Do you agree or disagree the statement:
Traditional Chinese classics should be the basic education
material for children. Only respond one of the four
answers: (1) strongly disagree, (2) disagree, (3) agree,
or (4) strongly agree.
• Individualism: Do you agree or disagree the statement:
The fundamental standard to evaluate the value of a work
of art is whether it is liked. Only respond one of the four
answers: (1) strongly disagree, (2) disagree, (3) agree, or
(4) strongly agree.
• Free Market: Do you agree or disagree the statement:
The minimum wage should be set by the state. Only
respond one of the four answers: (1) strongly disagree,
(2) disagree, (3) agree, or (4) strongly agree.
B. Additional Results of Public Opinion Simulations
DeepSeek-R1 exhibits substantially lower accuracy com-
pared to the other models. This is primarily due to the large
number of invalid responses it generates when using the same
prompts applied to all models. Tables V and Table VI present
the counts of invalid responses across all models evaluated
in the study. DeepSeek-R1, in particular, produces a high
proportion of invalid responses, with the maximum proportion
being 99.6%, which significantly reduces its overall simulation
accuracy.
TABLE IV
SIMULATION ACCURACY OF PUBLIC OPINIONS ON CAPITALISM WITH
CHINESE SAMPLES BY DEMOGRAPHICS AND SOCIOECONOMIC STATUS
DeepSeek-V3
Qwen2.5
GPT-4o
Llama-3.3
Female
0.3119
0.5491
0.2331
0.3129
Male
0.3992
0.5215
0.3699
0.3180
18–30 years old
0.2263
0.4938
0.2325
0.2531
30-45 years old
0.3735
0.5453
0.2963
0.3058
45-60 years old
0.4219
0.5510
0.3535
0.3639
TABLE V
NUMBER OF INVALID RESPONSES IN PUBLIC OPINION SIMULATION
USING ANES DATA
Task
model
# of Invalid Responses
% of Invalid Responses
Immigration
DeepSeek-R1
0
0
DeepSeek-V3
0
0
Qwen2.5
0
0
Llama-3.3
0
0
GPT-4o
0
0
Gun Control
DeepSeek-R1
736
30.0%
DeepSeek-V3
0
0
Llama-3.3
3
0.1%
Qwen2.5
0
0
GPT-4o
0
0
Abortion
DeepSeek-R1
2447
99.6%
DeepSeek-V3
0
0
Llama-3.3
0
0
Qwen2.5
7
0.3%
GPT-4o
0
0
Climate
DeepSeek-R1
1560
63.5%
DeepSeek-V3
0
0
Llama-3.3
0
0
GPT-4o
226
9.2%
Qwen2.5
0
0
LGBT
DeepSeek-R1
2259
91.9%
DeepSeek-V3
0
0
Llama-3.3
0
0
GPT-4o
0
0
Qwen2.5
0
0
TABLE VI
NUMBER OF INVALID RESPONSES IN PUBLIC OPINION SIMULATION
USING ZUOBIAO DATA
Task
model
# of Invalid Responses
Free Market
DeepSeek-R1
396
DeepSeek-V3
0
Llama-3.3
0
Qwen2.5
0
GPT-4o
9
Individualism
DeepSeek-R1
1397
DeepSeek-V3
0
Qwen2.5
0
Llama-3.3
0
GPT-4o
3
Capitalism
DeepSeek-R1
1618
DeepSeek-V3
0
Qwen2.5
0
Llama-3.3
0
GPT-4o
0
Foreign Aid
DeepSeek-R1
1301
DeepSeek-V3
0
Qwen2.5
0
Llama-3.3
0
GPT-4o
17
Traditionalism
DeepSeek-R1
48
DeepSeek-V3
0
Qwen2.5
0
Llama-3.3
0
GPT-4o
183

```
