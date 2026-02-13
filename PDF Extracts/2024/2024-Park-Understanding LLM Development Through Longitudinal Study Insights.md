---
title: "2024-Park-Understanding LLM Development Through Longitudinal Study Insights - PDF Extract"
source_pdf: "2024-Park-Understanding LLM Development Through Longitudinal Study Insights.pdf"
pages: 8
extracted_at: "2026-02-13T09:50:30.957705"
---

# PDF Extract: 2024-Park-Understanding LLM Development Through Longitudinal Study Insights

**Source PDF:** 2024-Park-Understanding LLM Development Through Longitudinal Study Insights.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Understanding LLM Development Through Longitudinal Study:
Insights from the Open Ko-LLM Leaderboard
Chanjun Park1†, Hyeonwoo Kim2
1Korea University, 2Upstage AI
bcj1210@korea.ac.kr
choco_9966@upstage.ai
Abstract
This paper conducts a longitudinal study over
eleven months to address the limitations of
prior research on the Open Ko-LLM Leader-
board, which have relied on empirical studies
with restricted observation periods of only five
months. By extending the analysis duration, we
aim to provide a more comprehensive under-
standing of the progression in developing Ko-
rean large language models (LLMs). Our study
is guided by three primary research questions:
(1) What are the specific challenges in improv-
ing LLM performance across diverse tasks on
the Open Ko-LLM Leaderboard over time? (2)
How does model size impact task performance
correlations across various benchmarks? (3)
How have the patterns in leaderboard rankings
shifted over time on the Open Ko-LLM Leader-
board?. By analyzing 1,769 models over this
period, our research offers a comprehensive
examination of the ongoing advancements in
LLMs and the evolving nature of evaluation
frameworks.
1
Introduction
The rapid advancement of large language mod-
els (LLMs) (Zhao et al., 2023) has led to the cre-
ation of various leaderboards designed to evaluate
their performance across a wide range of tasks (Li
et al., 2023b; Lee et al., 2023; Hughes and Bae,
2023; BigCode, 2023; Li et al., 2023a). Among
these, the Open LLM Leaderboard (Beeching et al.,
2023; Fourrier et al., 2024) developed by Hugging
Face (Jain, 2022) has achieved significant global
recognition. In the context of Korean language
models, the Open Ko-LLM Leaderboard (Park
et al., 2024) was established to specifically assess
LLM performance within the Korean language en-
vironment.
While previous analyses of the Open Ko-LLM
Leaderboard (Park et al., 2024) have provided valu-
able insights into LLM performance, they have
† Corresponding Author
been constrained observation periods of only five
months, limiting their ability to capture long-term
trends. To better understand the ongoing evolu-
tion and inherent challenges in LLM development,
a more comprehensive and extended analysis is
required. This paper addresses this gap by con-
ducting a detailed longitudinal study of the Open
Ko-LLM Leaderboard, guided by three primary
research questions:
First, we analyze the longitudinal changes in
performance across five tasks monitored by the
Open Ko-LLM Leaderboard. These tasks are de-
signed to evaluate various capabilities of LLMs, in-
cluding reasoning, natural language understanding,
and common sense knowledge. By examining data
collected over a eleven-month period, this study
aims to identify which capabilities have presented
the greatest challenges for LLM developers, which
tasks have reached performance saturation rapidly,
and which tasks continue to pose significant dif-
ficulties. This analysis will provide quantitative
insights into performance trends across different
tasks, thereby guiding targeted research efforts and
highlighting key areas that require further advance-
ment to push the boundaries of model development.
Second, we explore the correlations between
different tasks based on model size. This aspect
of the study examines how the performance across
different tasks varies depending on the scale of
the model. Understanding these correlations will
provide insights into the interaction between model
capacity and task performance, offering a deeper
understanding of how scaling influences overall
effectiveness across tasks.
Third, we examine the evolution of leaderboard
dynamics from the initial stages to the present by
focusing on three key aspects: the correlations be-
tween task performances in the early months com-
pared to the entire eleven-month period, the tempo-
ral changes in performance based on model type,
and the shifts in performance relative to model size.
arXiv:2409.03257v3  [cs.CL]  4 Mar 2025

--- Page 2 ---

2023-10
2023-11
2023-12
2024-01
2024-02
2024-03
2024-04
2024-05
2024-06
2024-07
2024-08
30
40
50
60
70
80
90
Ko-H5
Ko-ARC
Ko-CommonGen V2
Ko-HellaSwag
Ko-MMLU
Ko-TruthfulQA
Figure 1: Performance trends of LLMs across different
tasks on the Open Ko-LLM Leaderboard over a eleven-
month period. The total number of submitted models is
1,769.
This comprehensive analysis offers insights into the
evolving interplay among tasks and the influence of
various model characteristics on LLM performance
throughout different phases of development.
2
Open Ko-LLM Leaderboard
The Open Ko-LLM Leaderboard (Park et al., 2024)
is a pioneering platform designed to evaluate large
language models (LLMs) specifically in the Ko-
rean language, addressing the limitations of pre-
dominantly English-focused benchmarks.
This
leaderboard mirrors the structure of the globally
recognized Open LLM Leaderboard by Hugging
Face (Beeching et al., 2023), ensuring consistency
and comparability across languages. It is built on
two key principles: alignment with the English
leaderboard and the use of private test sets to avoid
data contamination, thereby enhancing evaluation
robustness.
The leaderboard employs the Ko-H5 benchmark,
comprising five tasks that assess various aspects
of language understanding and generation in Ko-
rean. These tasks are designed to comprehensively
evaluate LLM capabilities.
The first task, Ko-
Hellaswag (Zellers et al., 2019), tests common-
sense reasoning by requiring models to complete
sentences contextually and logically. The second
task, Ko-ARC (Clark et al., 2018), adapted from
the English ARC, evaluates both commonsense and
scientific reasoning through multiple-choice ques-
tions. Ko-MMLU (Hendrycks et al., 2020), the
third task, assesses multitask language understand-
ing and domain knowledge across various subjects,
requiring models to respond accurately to ques-
tions from different domains. The fourth task, Ko-
CommonGen V2 (Seo et al., 2024), focuses on
commonsense generation, where models must cre-
ate coherent sentences from given concepts, testing
their ability to connect common knowledge mean-
ingfully. Lastly, Ko-TruthfulQA (Lin et al., 2021)
evaluates a model ability to provide truthful and
accurate responses, crucial for assessing the factual
integrity of LLMs in real-world scenarios.
Through the Ko-H5 benchmark, the Open Ko-
LLM Leaderboard provides a robust framework
for evaluating Korean LLMs and promotes linguis-
tic diversity in LLM evaluation. By incorporating
tasks that reflect Korean linguistic and cultural nu-
ances, the leaderboard offers valuable insights into
LLM performance beyond English, encouraging a
more inclusive approach to language model evalua-
tion.
3
Empirical Analysis
3.1
Challenges in Enhancing Task
Performance Over Time
What are the specific challenges in improving LLM
performance across diverse tasks on the Open Ko-
LLM Leaderboard over time?. To investigate this
question, we conducted a comprehensive analy-
sis of performance trends over a eleven-month pe-
riod across all tasks on the Open Ko-LLM Leader-
board, including Ko-HellaSwag (commonsense rea-
soning)(Zellers et al., 2019), Ko-ARC (common-
sense and scientific reasoning)(Clark et al., 2018),
Ko-MMLU (multitask language understanding and
domain knowledge)(Hendrycks et al., 2020), Ko-
CommonGEN V2 (commonsense generation)(Seo
et al., 2024), and TruthfulQA (truthfulness) (Lin
et al., 2021).
Figure 1 and Table 1 show the varying perfor-
mance patterns of LLMs across these tasks over
the eleven-month period. Certain tasks, such as
Ko-HellaSwag and Ko-TruthfulQA, exhibit rapid
improvements in performance and early satura-
tion. Specifically, Ko-HellaSwag reached a score
of 50 almost immediately and achieved 80 by
week 26, while Ko-TruthfulQA showed compa-
rable progress, reaching a score of 80 within 25
weeks. These trends indicate that current LLMs are
particularly well-suited for tasks requiring straight-
forward commonsense reasoning and truthfulness,
suggesting a relatively lower barrier to achieving
performance enhancements in these domains.
Conversely, tasks such as Ko-MMLU and Ko-
CommonGEN V2 show slower, more gradual im-
provements without clear signs of saturation, high-
lighting their increased complexity and the deeper
understanding required from LLMs. Ko-MMLU

--- Page 3 ---

Dataset
50
60
70
80
Ko-ARC
∼6
∼17
∼17
-
Ko-HellaSwag
∼0
∼10
∼24
∼26
Ko-MMLU
∼13
∼26
-
-
Ko-TruthfulQA
∼0
∼13
∼17
∼25
Ko-CommonGen V2
∼0
∼1
-
-
Table 1: Number of weeks it took to reach scores of 50,
60, 70, and 80 out of 100 for the individual tasks.
took 13 weeks to reach a score of 50 and then sta-
bilized around 60 after 26 weeks, indicating a limit
to the current models capabilities. Similarly, Ko-
CommonGEN V2, despite reaching a score of 50
relatively quickly, showed minimal progress be-
yond 60. These patterns highlight the significant
challenges LLMs face in tasks that demand com-
plex reasoning and specialized knowledge, suggest-
ing these are important areas for further research.
The initial rapid gains in Ko-ARC, followed by
minimal progress beyond a score of 60 after 17
weeks, indicate that while LLMs can quickly adapt
to certain tasks, their progress is constrained by
the need for more complex reasoning skills. This
underscores the importance of developing more
challenging benchmarks to better evaluate the limi-
tations and capabilities of LLMs, especially in tasks
that require more advanced forms of reasoning.
Overall, these findings emphasize the need to in-
clude a broad range of complex tasks to comprehen-
sively assess LLM capabilities. While some tasks
demonstrate rapid performance saturation, others
present ongoing challenges, serving as essential
benchmarks for guiding future advancements in
LLM development.
3.2
The Influence of Model Size on Task
Performance Correlations
How does model size impact task performance cor-
relations across various benchmarks?. To inves-
tigate this question, we analyze how model size
affects performance improvements across different
tasks, using a framework similar to previous stud-
ies (Park et al., 2024). For this analysis, models
were divided into three size categories: under 3 bil-
lion parameters, 3 to 7 billion parameters, and 7 to
14 billion parameters. This categorization allows
for a detailed examination of how scaling impacts
task performance.
Figure 2 illustrates distinct patterns in task
performance correlations depending on model
size.
Smaller models (under 3 billion parame-
ters) show low or even negative correlations be-
tween certain tasks, such as Ko-TruthfulQA and
Ko-CommonGen V2, and other tasks. This sug-
gests that smaller models struggle to improve con-
sistently across multiple capabilities, indicating
that advancements in one area do not necessar-
ily lead to improvements in others. Consequently,
these models tend to have a fragmented skill set,
making them less suitable for a comprehensive eval-
uation of LLM performance.
In contrast, larger models demonstrate higher
correlations across most tasks, suggesting that in-
creasing model size results in a more effective inte-
gration of various capabilities. For example, mod-
els in the 7 to 14 billion parameter category exhibit
stronger positive correlations across a majority of
tasks, especially those requiring advanced reason-
ing. This trend indicates that scaling up model size
not only enhances performance on individual tasks
but also supports a more cohesive development of
capabilities, enabling more consistent performance
improvements across a wide range of tasks.
These findings highlight the importance of
model size in achieving balanced performance
across a range of tasks. Smaller models, with their
inconsistent performance across tasks, suggest a
limitation in their ability to generalize learning ef-
fectively. In contrast, the positive correlations ob-
served in larger models imply that increasing model
size fosters a more comprehensive understanding
and transfer of knowledge across different domains.
This insight is crucial for future LLM development,
as it underscores the need to consider model size
not just for boosting individual task performance,
but also for promoting a more integrated and holis-
tic enhancement of capabilities.
3.3
Temporal Shifts in Leaderboard Ranking
Patterns
How have the patterns in leaderboard rankings
shifted over time on the Open Ko-LLM Leader-
board?. To investigate this question, we extended
our analysis to an eleven-month period to see if the
initial trends, defined as those observed during the
initial five months in the previous study by Park
et al. (2024), remained consistent or if new pat-
terns emerged over time. This longer timeframe
allows us to capture shifts in model performance
and ranking dynamics.
Task Correlations Over Time.
Figure 3 shows
the correlation analysis between tasks during the

--- Page 4 ---

Figure 2: Correlation between task performances across different model size categories, illustrating how task
correlations change with increasing model size.
Figure 3: Analysis of Task Correlations Over Time.
Figure 4: Performance Trends Over Time for Different
Model Types.
Figure 5: Performance Trends by Model Size.
initial phases of the leaderboard and over the full
eleven-month period. A notable increase was ob-
served in the correlation between Ko-Truthful QA
and other tasks, especially Ko-Hellaswag. This
correlation, initially very low at 0.01, rose signifi-
cantly to 0.5 over time. This change suggests that
as higher-performing models, particularly those
with 7 billion parameters or more, were introduced,
the alignment between tasks became stronger. For
most other tasks, correlations remained relatively
stable, reflecting their initial patterns.
Performance Trends by Model Type.
Figure 4
presents the performance trends over time for
different model types.
As noted in previous
research (Park et al., 2024), improvements in
instruction-tuned models typically lagged behind
those of pretrained models by about one week.
When a pretrained model showed a significant per-
formance boost, instruction-tuned models followed
with a similar increase roughly one week later. This
pattern persisted throughout the entire period an-
alyzed, indicating a reliance of instruction-tuned

--- Page 5 ---

Figure 6: Monthly distribution of submissions by model type on the Open Ko-LLM leaderboard.
Date
Model Submissions Count
Model Evaluation Count
2023-09
51
40
2023-10
322
255
2023-11
337
280
2023-12
260
225
2024-01
289
234
2024-02
115
99
2024-03
176
153
2024-04
170
122
2024-05
156
134
2024-06
79
72
2024-07
142
129
2024-08
33
26
Total
2230
1769
Table 2: Monthly distribution of model submissions and evaluation on the Open Ko-LLM leaderboard.
models on the advancements made by pretrained
models. After April 2024, the performance of pre-
trained models stabilized, leading to a correspond-
ing lack of progress in both instruction-tuned and
RL-tuned models. This trend indicates the funda-
mental role of pretrained models in driving overall
performance gains in LLMs and suggests that fur-
ther improvements in pretrained models are neces-
sary for advancing model capabilities.
Performance Trends Across Model Sizes.
Fig-
ure 5 shows performance variations by model size.
Models in the 0-3B range exhibited minimal im-
provement throughout the leaderboard period, in-
dicating inherent scalability limitations. Similarly,
models in the 3-7B range initially demonstrated
gains, but their progress stabilized around five
months in (April 2024 to August 2024), revealing
similar scalability constraints.
Larger models in the 7-14B range showed steady
performance improvements during the early phase
of the leaderboard, continuing throughout the entire
analysis period. However, after April 2024, their
performance also reached a saturation point. This
stagnation is likely due to the absence of new, high-
performing Korean pretrained models, a trend also
evident in the analysis of different model types in
Figure 4.
These findings emphasize that improving LLM

--- Page 6 ---

performance largely depends on advancements in
pretrained models. The leaderboard analysis indi-
cates that, without new breakthroughs in pretrained
models, further improvements are limited. This
highlights the essential role of continuous inno-
vation in pretrained models for advancing LLM
performance.
3.4
Evaluation Patterns and Submission
Insights
Figure 6 presents the monthly distribution of sub-
missions across different model types on the Open
Ko-LLM leaderboard. Initially, pretrained mod-
els constituted 37% of all submissions, but this
proportion declined sharply over time, with no pre-
trained models submitted by August 2024. This
trend signals a diminishing focus on pretrained
models within the community, which is concerning
given their foundational importance discussed in
Section 3.3. Therefore, a renewed emphasis on
fostering interest and engagement with pretrained
models could help address this emerging gap.
On the other hand, instruction-tuned models,
which started at 61%, consistently dominated the
submissions, maintaining a steady presence of 70-
80% each month. This trend suggests that the
community perceives instruction-tuned models as
highly effective or suitable for the tasks evaluated.
Additionally, RL-tuned models, though initially
making up only 2% of submissions, gradually in-
creased to a peak of 29%, reflecting a growing inter-
est in exploring reinforcement learning approaches
within the leaderboard context. This variety indi-
cates a healthy exploration of diverse model types,
but also highlights areas where community focus
could be broadened or rebalanced.
In addition, Table 2 presents the monthly statis-
tics for both the number of model submissions and
the number of completed model evaluations. The
Model Submissions Count refers to the total num-
ber of models submitted to the leaderboard each
month. In contrast, the Model Evaluation Count
represents the number of these submitted models
that successfully completed the evaluation process.
The discrepancy between the Model Submissions
Count and the Model Evaluation Count is due to
instances where some models fail to complete the
evaluation phase on the leaderboard. This failure
can occur for several reasons, such as models being
too large to be processed within the available com-
putational resources or issues related to library sup-
port and compatibility. As a result, not all submit-
ted models are evaluated successfully, highlighting
potential challenges and areas for improvement in
handling diverse model architectures on the leader-
board.
4
Conclusion
This study provides a longitudinal analysis of the
Open Ko-LLM Leaderboard, uncovering signifi-
cant performance trends and underlying challenges
in LLM development. It was observed that smaller
models consistently face scalability limitations, pre-
venting substantial performance advancements. In
contrast, larger models initially show promising
improvements but eventually reach a saturation
point, highlighting a critical dependency on ad-
vancements in pretrained models. These findings
underscore the need for continuous innovation and
enhancement in the development of pretrained mod-
els to push the boundaries of LLM capabilities fur-
ther. Additionally, the analysis demonstrates the
utility of leaderboard data in tracking the evolving
dynamics of LLM performance. By examining a
broader range of model submissions and evaluation
patterns over an extended period, this study pro-
vides valuable insights into how model size, type,
and tuning methods influence overall effectiveness.
Such insights can inform targeted research efforts
and encourage the development of strategies aimed
at overcoming existing limitations, ultimately sup-
porting more robust and adaptable LLMs.
Acknowledgments
We sincerely thank the National Information Soci-
ety Agency (NIA), Korea Telecom (KT), and Flitto
for their support. We also extend our gratitude
to the Korea University NLP & AI Lab, particu-
larly Professor Heuiseok Lim and Jaehyung Seo,
for their valuable data contributions, which have
greatly enhanced the robustness of the leaderboard.
Our appreciation goes to the Hugging Face teams,
especially Clémentine Fourrier, Lewis Tunstall,
Omar Sanseviero, and Philipp Schmid, for their
assistance. We would like to thank SeongHwan
Cho for his contributions to the leaderboard devel-
opment, and Sanghoon Kim for his contributions
to the leaderboard infrastructure. Special thanks
to Hyunbyung Park for his initial contributions to
Ko-H5.
We are also grateful to Professor Harksoo Kim
from Konkuk University, Professor Hwanjo Yu
from Pohang University of Science and Technol-

--- Page 7 ---

ogy, Professor Sangkeun Jung from Chungnam
National University, and Professor Alice Oh from
KAIST for their insightful advice on the Open Ko-
LLM Leaderboard. Finally, we deeply appreciate
the open-source community for their invaluable
feedback and contributions.
This work was supported by Institute of Infor-
mation & Communications Technology Planning
& Evaluation(IITP) grant funded by the Korea gov-
ernment(MSIT) (No. RS-2024-00338140, Devel-
opment of learning and utilization technology to
reflect sustainability of generative language models
and up-to-dateness over time).
Limitations
While this study provides valuable insights into
the evaluation of LLMs, several limitations should
be acknowledged. First, our analysis is primarily
based on data from the Open Ko-LLM Leaderboard.
Although this leaderboard offers extensive cover-
age of various tasks, it may not fully represent
the complete spectrum of challenges and scenar-
ios relevant to LLM performance, particularly in
specialized or emerging domains.
Additionally, the focus on Korean language mod-
els may restrict the generalizability of our findings
to other languages and cultural contexts. The lin-
guistic and cultural nuances specific to Korean may
not entirely translate to other languages, potentially
limiting the applicability of our conclusions.
Furthermore, our study predominantly examines
the relationship between model size and perfor-
mance but does not explore other factors, such as
training data diversity or the impact of different
fine-tuning techniques, which could also signifi-
cantly influence model outcomes. Future research
should aim to address these gaps by incorporating
a broader range of tasks, languages, and evalua-
tion metrics. Expanding the scope of analysis to
include models trained in different linguistic and
cultural settings, as well as exploring the impact of
varied training methodologies, would enhance the
robustness and applicability of the findings.
Ethics Statement
In conducting this research, we adhered to the high-
est ethical standards, ensuring that all data used
in the evaluation was sourced responsibly and in
compliance with relevant regulations. We are com-
mitted to transparency and integrity in our research
practices, and we have made our methods and find-
ings available to the community for further scrutiny
and development. We also acknowledge the impor-
tance of considering the societal impacts of LLMs,
particularly in ensuring that their development and
deployment are aligned with ethical principles that
promote fairness, inclusivity, and accountability.
References
Edward Beeching,
Clémentine Fourrier,
Nathan
Habib, Sheon Han, Nathan Lambert, Nazneen
Rajani, Omar Sanseviero, Lewis Tunstall, and
Thomas Wolf. 2023.
Open llm leaderboard
(2023-2024).
https://huggingface.co/
spaces/open-llm-leaderboard-old/open_
llm_leaderboard.
BigCode. 2023.
Big code models leaderboard.
https://huggingface.co/spaces/bigcode/
bigcode-models-leaderboard.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord. 2018. Think you have solved question an-
swering? try arc, the ai2 reasoning challenge. arXiv
preprint arXiv:1803.05457.
Clémentine Fourrier, Nathan Habib, Alina Lozovskaya,
Konrad Szafer, and Thomas Wolf. 2024.
Open
llm leaderboard v2.
https://huggingface.
co/spaces/open-llm-leaderboard/open_llm_
leaderboard.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing. arXiv preprint arXiv:2009.03300.
Simon Hughes and Minseok Bae. 2023. Vectara hallu-
cination leaderboard.
Shashank Mohan Jain. 2022. Hugging face. In Intro-
duction to Transformers for NLP: With the Hugging
Face Library and Models to Solve Problems, pages
51–67. Springer.
Tony Lee, Michihiro Yasunaga, Chenlin Meng, Yifan
Mai, Joon Sung Park, Agrim Gupta, Yunzhi Zhang,
Deepak Narayanan, Hannah Benita Teufel, Marco
Bellagente, et al. 2023. Holistic evaluation of text-to-
image models. arXiv preprint arXiv:2311.04287.
Junyi Li, Xiaoxue Cheng, Wayne Xin Zhao, Jian-Yun
Nie, and Ji-Rong Wen. 2023a. Halueval: A large-
scale hallucination evaluation benchmark for large
language models. In Proceedings of the 2023 Con-
ference on Empirical Methods in Natural Language
Processing, pages 6449–6464.
Xuechen Li, Tianyi Zhang, Yann Dubois, Rohan Taori,
Ishaan Gulrajani, Carlos Guestrin, Percy Liang, and
Tatsunori B. Hashimoto. 2023b. Alpacaeval: An
automatic evaluator of instruction-following models.
https://github.com/tatsu-lab/alpaca_eval.

--- Page 8 ---

Stephanie Lin, Jacob Hilton, and Owain Evans. 2021.
Truthfulqa: Measuring how models mimic human
falsehoods. arXiv preprint arXiv:2109.07958.
Chanjun Park, Hyeonwoo Kim, Dahyun Kim, SeongH-
wan Cho, Sanghoon Kim, Sukyung Lee, Yungi Kim,
and Hwalsuk Lee. 2024. Open Ko-LLM leaderboard:
Evaluating large language models in Korean with Ko-
h5 benchmark. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 3220–3234,
Bangkok, Thailand. Association for Computational
Linguistics.
Jaehyung Seo, Jaewook Lee, Chanjun Park, SeongTae
Hong, Seungjun Lee, and Heui-Seok Lim. 2024. Ko-
commongen v2: A benchmark for navigating korean
commonsense reasoning challenges in large language
models. In Findings of the Association for Computa-
tional Linguistics ACL 2024, pages 2390–2415.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. Hellaswag: Can a
machine really finish your sentence? arXiv preprint
arXiv:1905.07830.
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang,
Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen
Zhang, Junjie Zhang, Zican Dong, et al. 2023. A
survey of large language models.
arXiv preprint
arXiv:2303.18223.

```
