---
title: "2025-Unknown-B-REASO A Multi-Level Multi-Faceted Bengali Evaluation Suite - PDF Extract"
source_pdf: "2025-Unknown-B-REASO A Multi-Level Multi-Faceted Bengali Evaluation Suite.pdf"
pages: 15
extracted_at: "2026-02-13T10:43:55.305406"
---

# PDF Extract: 2025-Unknown-B-REASO A Multi-Level Multi-Faceted Bengali Evaluation Suite

**Source PDF:** 2025-Unknown-B-REASO A Multi-Level Multi-Faceted Bengali Evaluation Suite.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

Findings of the Association for Computational Linguistics: EMNLP 2025, pages 9260–9274
November 4-9, 2025 ©2025 Association for Computational Linguistics
B-REASO: A Multi-Level Multi-Faceted Bengali Evaluation Suite for
Foundation Models
Md Tanzib Hosain1,3,, Md Kishor Morol2,3
1American International University-Bangladesh, 2Cornell University
3ELITE Research Lab
20-42737-1@student.aiub.edu, mmorol@cornell.edu
Abstract
The fast growth of large language models
(LLMs) necessitates the urgent need for new
NLP benchmarks. We provide B-REASO, the
first inclusive Bengali assessment suite created
to evaluate advanced foundation model knowl-
edge and reasoning skills in a Bengali lan-
guage setup. The B-REASO includes multiple-
choice questions with four different degrees of
diﬀiculty: professional, college, high school,
and middle school. The questions cover 50 dif-
ferent fields, from science and engineering to
the humanities. Alongside B-REASO, there
is B-REASO HEAVY, a subset of extremely
diﬀicult B-REASO topics that need for sophis-
ticated reasoning skills to answer.
We do a
thorough assessment of the most sophisticated
LLMs on B-REASO, encompassing models
with an English focus. Findings show that only
Claude-3.5-Sonnet was able to get an average
accuracy of more than 65%, indicating that
contemporary LLMs still have a long way to go.
We hope that B-REASO will support the cre-
ation and expansion of foundation models for
Bengali users by assisting in the analysis of sig-
nificant advantages and disadvantages of these
models. We open-source our code and data at
https://github.com/kraritt/b-reaso.
1
Introduction
Natural Language Processing (NLP) has seen a rev-
olution with the advent of Large Language Models
(LLMs). In the age of LLMs, assessment plays a
critical function as the central force that shapes the
direction of Artificial Intelligence (AI) progress.
To assess LMs’ natural language understanding
skills, traditional NLP benchmarks (Wang et al.,
2019; Wang, 2018) have been frequently used.
However, since bigger models are performing at a
level comparable to humans, these standards are no
longer as applicable, leaving limited area for fur-
ther study (Liu et al., 2023; Goyal et al., 2022;
Hendrycks et al., 2020).
Recent LLM evaluation has focused mostly on
assessing sophisticated reasoning skills and explor-
ing advanced world knowledge in order to ade-
quately benchmark LLMs
(Wang et al., 2023;
Cobbe et al., 2021; Hendrycks et al., 2021; Clark
et al., 2018).
Meanwhile, as multilingual and
other LLMs tailored for various regional languages
(Nguyen et al., 2023) have become more popular,
evaluation benchmarks for languages other than
English–have also been introduced (Huang et al.,
2024; Li et al., 2023). Nevertheless, the English
language remains the primary focus of the con-
temporary benchmarks, which leads to a restricted
comprehension of LLMs’ proficiency in other lan-
guages rapidly. As per our best knowledge, there
is no comprehensive previous work that has been
done on LLMs’ understanding specifically in Ben-
gali language setup. This study focuses on assess-
ing foundation models’ advanced capabilities in
the context of Bengali–world’s seventh1 most com-
monly spoken languages.
We introduce B-REASO (Figure 1), the first
complete Bengali evaluation suite designed to fully
evaluate LLMs’ advanced knowledge and reason-
ing skills in a Bengali environment, in an effort to
close the gap between Bengali LLM development
and assessment. As shown in Table 1, B-REASO
comprises 13497 multiple-choice test questions
covering 50 different fields, from science and en-
gineering to the humanities. Middle school, high
school, college, and professional exams are the
four diﬀiculty levels from which the questions are
gathered (details in Appendix G). We also provide
B-REASO HEAVY as an accompanying bench-
mark, which is a subset of B-REASO’s most dif-
ficult tasks that need very sophisticated thinking
skills to complete, such as, college physics and ad-
vanced mathematics. With an accuracy of 48.53%,
B-REASO HEAVY is the first Bengali benchmark
1https://en.wikipedia.org/wiki/List_of_languages
_by_total_number_of_speakers
9260

--- Page 2 ---

Figure 1: B-REASO overview diagram. The five fields—STEM, social science, humanities, Bangladesh specific
and other—are represented by different colors for the subjects.
at this level and one of the few benchmarks for ad-
vanced reasoning where Gemini-1.5-Pro-002 still
has trouble.
2
B-REASO Benchmark
2.1
Principles of Benchmark Design
Table 1: Statistics of B-REASO benchmark grouped by
various fields of subjects and levels.
Group
#Fields
#Instances (%)
grouped by field
Social Science
8
2394 (17.74%)
STEM
20
4495 (33.30%)
Humanities
8
1997 (14.80%)
Others
11
3932 (29.13%)
Bangladesh Specific
3
679 (5.03%)
grouped by level
College
23
5798 (42.96%)
High School
8
1594 (11.81%)
Professional
12
4696 (34.79%)
Middle School
7
1409 (10.44%)
Total
50
13497 (100.00%)
B-REASO’s goal is to assist developers in
rapidly comprehending the capabilities of their
models from a variety of angles so they can iden-
tify the models’ flaws and make the necessary im-
provements. In order to do this, we concentrate on
LLMs’ more sophisticated skills, such reasoning
and global knowledge, which are perhaps the most
important ones for LLMs in the modern workforce.
Complex tasks are often the primary differentia-
tors between LLMs, even when multiple LLMs
may perform equally in simple situations like in-
formal talks (Achiam et al., 2023). As a result, we
built B-REASO using actual, diﬀicult human tests
that are utilized in Bangladesh to evaluate people’s
skills in a variety of ways. Like (Ghahroodi et al.,
2024; Hendrycks et al., 2021), we only choose
multiple-choice questions because: (a) metrics are
well-defined; and (b) multiple-choice questions are
a straightforward but effective stand-in for assess-
ing the potential of advanced abilities of founda-
tion models, which we believe could be readily
utilized and reflected in a variety of downstream
applications through specialized instruction tuning
(Chung et al., 2024; Wang et al., 2022).
Only
one of the four options (details in Appendix E)
for each question is the right response. Through
prompting, LLMs are meant to be used to answer
these queries. 50 different disciplines are covered
by the B-REASO questions, which we then group
into more general categories like STEM, the Hu-
manities, Social Science, Bangladesh Specific and
Other fields.
2.2
Principles of Data Collection
2.2.1
Precis of Subject Selection
Middle school, high school, college, and profes-
sional are the four diﬀiculty levels covered by B-
REASO. With the exception of English, we cover
the core subjects taught in Bengali middle and
high schools.
We choose 23 representative top-
ics at the college level from the oﬀicial undergrad-
uate major categories specified by Bangladesh’s
University Grant Commission2. To ensure com-
pleteness, at least one subject from each category
is included in B-REASO. We choose 12 sample
professional-level qualifications, including those
for doctors, lawyers, and civil servants, based on
Bangladesh Civil Service3 qualification directory.
In addition, we group these topics into five topi-
cal categories: Social Science, Humanities, STEM
2https://ugc.gov.bd/
3https://bpsc.gov.bd/
9261

--- Page 3 ---

(Science, Technology, Engineering, and Mathe-
matics), Bangladesh Specific and Other fields. Ta-
ble 1 shows each of the 50 topics together with the
groups to which they belong.
2.2.2
Prevention of Data Contamination
National test questions, including those from
Bangladesh’s national professional examinations
and college entrance exams are often made avail-
able online and disseminated extensively. As a re-
sult, these queries could unintentionally be stum-
bled upon and included to LLM pretraining, which
might result in problems with data leaking. We get
our data from either small-scale local tests, such
those offered online by certain high schools, or
from mock exams following the design principle
of
(Huang et al., 2024) in order to reduce this
danger. Furthermore, rather than coming straight
from structured questions or plain text, the major-
ity of B-REASO examples are taken from online
PDF or Microsoft Word publications. To create
the final structured format, the writers analyze and
meticulously annotate these papers; for certain top-
ics, this procedure often entails complicated LATEX
equation translation. This reduces the possibility
of data contamination even further.
2.2.3
Precis of Data Sources
Our data is mostly sourced from publicly accessi-
ble online mock tests. Furthermore, some of the
college-level problems are publicly posted previ-
ous test questions from Bangladesh’s leading col-
leges.
A small percentage of college questions
are national graduate entrance exam practice ques-
tions4. These questions are not publicly accessi-
ble, and we have got their permission to add around
1800 of them to B-REASO.
2.2.4
Precis of Data Processing
Most of the gathered data is in the form of Mi-
crosoft Word or PDF documents, with a small per-
centage also being web pages. The first step is to
convert PDF documents into text. Following that,
all questions are processed by the writers, either
automatically where feasible or manually with the
use of OCR toolkits5. For STEM subjects includ-
ing significant symbols and equations, mathemati-
cal expressions are standardized into LATEX(Figure
5) format in accordance with earlier studies (Tam
et al., 2024; Hendrycks et al., 2021). Annotators
4https://udvash.com/
5https://mathpix.com/
compile and check the generated LATEX formulae
to make sure they are accurate. Furthermore, ev-
ery instance is verified by a person for quality con-
trol in order to eliminate inappropriate instances.
Annotations were made by knowledgeable partici-
pants (each holds at least a bachelor’s degree, with
someone having advanced degrees), all of whom
are co-authors on this work, guaranteeing that each
person gets full credit for their contributions. Addi-
tionally, explicit instructions were given on how to
acquire participant permission, preserve data pri-
vacy, and honor local customs (see Appendix F).
2.2.5
Precis of Explanation Curation
LLMs have shown remarkable performance with
reasoning-heavy
tasks
when
using
Chain-of-
Thought (CoT) reasoning
(Kojima et al., 2022;
Wei et al., 2022), which demands them to provide
a text sequence of the reasoning process along
with the final response. Achieving state-of-the-art
performance on a variety of tasks, the few-shot
version of CoT is more widely utilized than the
zero-shot version (Wang et al., 2022; Xie et al.,
2024; Zhou et al., 2022; Gao et al., 2023).
To
enable the possible use of B-REASO in a few-shot
CoT context, we provide high-quality explanation
data for the development split by combining
human annotation with automated creation. To be
more precise, we first instruct Claude-3.5-Sonnet
to provide a detailed explanation of the ground-
truth response, and then we manually edit the
explanations to produce the final ones. Details on
prompting Claude-3.5-Sonnet are in Appendix A.
A dev example with explanations is illustrated in
Figure 2.
2.3
B-REASO HEAVY
From B-REASO, we choose eight diﬀicult math,
physics, and chemistry subjects to create a dis-
tinct, the B-REASO HEAVY benchmark encom-
passes probability, discrete mathematics, and ad-
vanced mathematics, high school mathematics,
high school chemistry, college chemistry, college
physics, and statistics, as well as high school
physics.
These topics often necessitate the use
of intricate LATEX equations and diﬀicult-to-solve
logical problems. Figure 3 illustrates a case from
advanced physics. In line with current initiatives
to provide challenging standards for evaluating
sophisticated reasoning, B-REASO HEAVY apti-
tudes (Suzgun et al., 2022; Hendrycks et al., 2021),
which are the primary variables that distinguish
9262

--- Page 4 ---

àƣঃ
একিটগািড়10 েসেকেũ ǬƵরঅবƵােথেক20 m/s েবেগĄরািĈতহয়।গািড়িটǬƵরĄরেণচেল।এইসমেয়গািড়িটেযদূরĄ অিতËমকেরেছতাহল——।
A. 50 m
B. 100 m
C. 150 m
D. 200 m
Question:
A car accelerates from rest to a speed of 20 m/s in 10 seconds. The car moves with constant acceleration. The distance traveled by the car during this
time is ——.
A. 50 m
B. 100 m
C. 150 m
D. 200 m
উত্তরঃB
Answer: B
বয্াখয্াঃ
ǖবকĄরেণরজনয্গিতরসমীকরণসহঃd = v0t + 1
2 at2
েযখােনঃv0 = 0 m/s (আিদেবগ); v = 20 m/s (েশষেবগ); t = 10 েসেকেũ
àথেম, Ąরণa খুঁজুনঃa = v−v0
t
= 20−0
10
= 2 m/s2
এবার, দূরĄ গণনাকর‍ুনঃd = 0 + 1
2 × 2 × 102 =
100 m
Explanation:
With the equation of motion for constant acceleration: d = v0t + 1
2 at2
Where: v0 = 0 m/s (initial velocity); v = 20 m/s (final velocity); t = 10 seconds
First, find acceleration a: a = v−v0
t
= 20−0
10
= 2 m/s2
Now, calculate the distance: d = 0 + 1
2 × 2 × 102 =
100 m
Figure 2: A high school physics development example with explanations.
The potential of LLMs in broad and intricate situa-
tions may be reflected in different LLMs. It is im-
portant to note that The B-REASO HEAVY bench-
mark is the first in Bangladesh to provide very chal-
lenging reasoning problems.
3
Experimental Methodology
3.1
Precis of Models
19 distinct LLMs with diverse sizes and devel-
opment organizations that can handle Bengali
text are used in our thorough examination of B-
REASO. In particular, we test the proprietary,
closed-source models—including those from Ope-
nAI, Anthropic, and Google etc.—using APIs. For
open-weight models, we concentrate on models
created for multilingual and English applications.
3.2
Principles of Setup
With B-REASO, we test LLMs in both zero-shot
and few-shot (i.e. five-shot) scenarios, using the
development split’s few exemplars. Few-shot as-
sessment is in line with other works’ procedures
(Achiam et al., 2023; Team et al., 2023; Touvron
et al., 2023) for assessing LLM performance, as
well as benchmarks such C-Eval
(Huang et al.,
2024) and MMLU
(Hendrycks et al., 2020).
The answer options are extracted from the model
replies using regular expressions, which guaran-
tees that we can do so in almost every situation.
We provide CoT findings on the few-shot setting
alone and Answer-Only (AO) results on both zero
and few-shot settings. We discovered that it was
sometimes challenging to extract the answer op-
tions from zero-shot CoT predictions when the gen-
eration did not adhere to certain patterns. The AO
and CoT prompts are included in Appendix B. We
observe that the few-shot exemplars may surpass
the maximum context length of particular LLMs
for specific topics in the CoT situation. To fit in-
side the context window in certain situations, we
dynamically minimize the amount of exemplars.
3.3
Precis of Answer Extraction
Variations in how models are implemented to ex-
tract predictions have a significant influence on
the evaluation’s outcomes. In order to guarantee
an equitable assessment and accommodate differ-
ences in model accessibility and prompting con-
figurations, we utilize two approaches for extract-
ing responses: (1) The likelihood-based approach.
In line with the original MMLU implementation
(Hendrycks et al., 2021), the approach entails look-
ing at a group of potential response symbols (i.e.,
”A”, ”B”, ”C”, and ”D”) and choosing the symbol
with the greatest assigned token probability as the
model’s prediction. (2) Method based on genera-
tion. When it is not feasible to determine the candi-
date token probabilities directly, we choose to use
the first token that is created in a greedy manner
and may be deduced as an option code in order to
9263

--- Page 5 ---

àƣঃ
ধরাযাকΩএকিটআবŞ অঞ্চলযাপৃƨ x2 + y2 + z2 = 4 এবংƵানাİ সমতলx = 0, y = 0, এবংz = 0 ĆারাআবŞ, এবংধরাযাকΣ অঞ্চেলরপৃƨ
Ω।পৃেƨরঅখŌতাগণনাকর‍ুন:
I =
∫
Σ(x2 + y2 + z2) dS, েযখােনdS হলঅťিরকপৃƨ উপাদান।িনেচরেকানিটসিঠকউত্তর?
A.
8π
3
B. 4π
C.
16π
3
D.
8π
5
Question:
Let Ωbe a bounded region enclosed by the surface x2 + y2 + z2 = 4 and the coordinate planes x = 0, y = 0, and z = 0, and let Σ be the surface
of the region Ω. Calculate the surface integral: I =
∫
Σ(x2 + y2 + z2) dS, where dS is the differential surface element. Which of the following is
the correct answer?
A.
8π
3
B. 4π
C.
16π
3
D.
8π
5
উত্তরঃB
Answer: B
Figure 3: An example of a B-REASO HEAVY topic in advanced physics.
forecast the response.
Since access to the likelihood of each potential
response symbol is limited for proprietary mod-
els, we employ the generation-based approach for
both AO and CoT prompting scenarios. In the case
of open-source models, we use the direct prompt-
ing approach based on probability. But when we
use CoT prompting, we are limited to adopting the
generation-based approach as the model must first
produce an explanation for the instance that was
questioned. In order to prevent failure to generate
the answer, we modify the number of shots in CoT
prompting based on the duration of the model con-
text.
4
Experimental Results
For AO and CoT prompting, the experimental
findings are shown in Table 2 and Table 3, re-
spectively. Models trained on Bengali data like
multilingual models show a significant improve-
ment over models concentrating on the English
context, and flagship proprietary models gener-
ally perform better than their open-weight equiv-
alents. The DeepSeek-v3 which is optimized for
multilingual tasks, performs better than GPT-4o for
AO prompting. Llama-3.1-405B-Instruct, the best-
performing open-weight model with 405 billion pa-
rameters, performs similarly to GPT-4o and bet-
ter than proprietary models like Amazon-Nova-Pro
and Palmyra-X-004. Proprietary models perform
much better than the top open-source model in CoT
prompting, by a range of 7% to 13%. The findings
imply that there is a good chance to improve reason-
ing skills in open-source models with CoT prompt-
ing. In Section 5, we go into more detail about the
differences between AO and CoT prompting. All
things considered, the baseline that has been set in-
dicates that B-REASO provides a comprehensive
basis for assessing LLMs in the context of Ben-
gali, with opportunity for development. Addition-
ally, the performance of multilingual LLMs in B-
REASO underscores the importance of localized
model development, supporting the initiative to ad-
vance LLMs tailored for specific linguistic and cul-
tural contexts.
5
Results Analysis
5.1
Performance on B-REASO HEAVY
The B-REASO HEAVY average accuracy is dis-
played in Table 4.
GPT-4o’s accuracy on five-
shot AO, and five-shot CoT settings are only
42.34% and 49.11%, respectively, suggesting that
B-REASO HEAVY is a challenging task. It’s inter-
esting to note that CoT prompting somewhat raises
GPT-4o on these really diﬀicult topics.
When
compared to a random baseline, only Gemini-1.5-
Pro-002, Llama-3.1-405B-Instruct and GPT-4o are
able to make significant progress—improving by
at least 7 points. Additionally, our findings support
the idea that when tasks are suﬀiciently compli-
cated, some important differences amongst LLMs
emerge. We emphasize how crucial it is to assess
LLMs in these diﬀicult situations because modern
LLM development entails building sophisticated
systems or agents that can interact with different
kinds of data, receive feedback, reason and use
tools, and even take action (Mialon et al., 2023).
9264

--- Page 6 ---

Table 2: Average accuracy (%) for five-shot in an AO setting. Within each category, we provide the average accuracy
across all subjects. The accuracy average across all subjects is shown in the ”Average” column. Best values are
highlighted in purple, second-best in gray, separately for proprietary and open-weight models.
Model
Average
Social
Science
STEM
Humanities
Bangladesh
Specific
Other
Proprietary Models
Claude-3.5-Sonnet
68.53
74.73
49.21
72.34
83.06
63.29
Gemini-1.5-Pro-002
62.03
69.72
42.42
66.76
82.33
48.91
GPT-4o
54.98
61.02
36.88
57.03
76.66
43.31
Amazon-Nova-Pro
51.62
58.23
36.98
50.11
74.12
38.65
Palmyra-X-004
49.85
55.52
35.91
47.13
72.85
37.83
PaLM-2
47.01
52.12
33.84
47.26
66.67
35.17
Jamba-1.5-Large
47.01
52.12
33.84
47.26
66.67
35.17
Solar-Pro
44.60
41.83
30.12
40.92
73.54
36.58
Open-Weight Models
DeepSeek-v3
61.74
65.82
46.22
64.13
78.62
53.91
Llama-3.1-405B-Instruct
55.35
58.12
39.46
57.18
74.87
47.12
DBRX-Instruct
44.66
47.22
31.14
42.96
68.15
33.85
Arctic-Instruct
43.00
45.36
28.07
42.12
65.15
34.28
Gemma-7B
41.92
47.08
32.03
43.52
57.51
29.45
Command-R
37.62
36.74
23.15
33.41
63.02
31.77
Yi-6B
36.43
37.12
21.74
37.22
52.86
33.21
Qwen1.5-7B
35.19
36.83
26.06
31.17
51.39
30.48
Phi-2
35.18
37.27
27.93
36.81
46.68
27.22
Mistral-7B-v0.1
33.53
36.51
27.82
38.12
35.02
30.19
OLMo-7B
26.27
28.01
20.83
24.89
33.54
24.06
5.2
Performance on AO and CoT Prompting
We use CoT prompting and our carefully chosen
explanations to further explore the potential ca-
pabilities of LLMs.
It has been demonstrated
that CoT prompting greatly enhances tasks requir-
ing intricate multi-hop thinking by eliciting se-
quential reasoning chains towards solution deriva-
tions. As demonstrated in Table 3, most models
that can profit a lot from CoT are large, propri-
etary ones, such as GPT-4o (8.07%), and Claude-
3.5-Sonnet (7.62%) in STEM disciplines. The re-
sults might be explained by the emergent charac-
ter of LLMs’ reasoning abilities. We also evalu-
ate B-REASO with intermediate tool integration
(Appendix C) and multi-agent self-reflection (Ap-
pendix D) where subsequent LLMs improve little.
5.3
Performance Across Educational
Diﬀiculty Levels
For the AO prompting setup (Table 5), multi-
lingual training clearly boosts performance com-
pared to models focused primarily on English con-
texts.
Among proprietary models, Claude-3.5-
Sonnet leads with the highest accuracy across all
diﬀiculty levels, followed by Gemini-1.5-Pro-002,
while GPT-4o lags behind. On the open-weight
side, DeepSeek-v3, designed for multilingual tasks,
performs best and even surpasses GPT-4o, show-
ing that optimised multilingual models can ri-
val proprietary systems. Llama-3.1-405B-Instruct,
with 405B parameters, emerges as the second-
best open-weight model, performing on par with
GPT-4o and ahead of proprietary competitors like
Amazon-Nova-Pro and Palmyra-X-004 in this set-
ting. Whereas, in the CoT prompting setup (Ta-
ble 6), proprietary models widen the performance
gap. Claude-3.5-Sonnet once again secures the top
spot, followed by Gemini-1.5-Pro-002, with GPT-
4o ranking lower. Although DeepSeek-v3 contin-
ues to lead among open-weight models and shows
competitive gains, the best proprietary models still
outperform the strongest open-source alternative
by 7%–13%.
Llama-3.1-405B-Instruct also im-
proves with CoT prompting, but it remains behind
the top proprietary systems.
5.4
Performance on Questions with Negation
Language models may have trouble expressing
negation, according to earlier studies
(Hosseini
et al., 2021; Kassner and Schütze, 2019). We ini-
tially use string matching to divide the test set into
questions with and without negation terms in or-
der to examine whether this problem still exists in
the setting of LLMs in Bengali. Next, we evaluate
how well various models perform on these two sub-
groups. It should be noted that, for this experiment
we select around 22% of the data contains negation
(11%) and non-negation (11%) phrases, based on
our string matching findings, for this experiment.
Ten model families are shown in Table 7, which
also reveals a common limitation of large language
models:
most models, apart from Claude-3.5-
Sonnet and GPT-4o perform worse on questions
9265

--- Page 7 ---

Table 3: Average accuracy (%) for five-shot in a CoT setting. Within each category, we provide the average accuracy
across all subjects. The accuracy average across all subjects is shown in the ”Average” column. Best values are
highlighted in purple, second-best in gray, separately for proprietary and open-weight models.
Model
Average
Social
Science
STEM
Humanities
Bangladesh
Specific
Other
Proprietary Models
Claude-3.5-Sonnet
70.91
77.45
56.83
74.12
81.97
64.18
Gemini-1.5-Pro-002
64.75
71.63
49.27
68.91
80.15
53.69
GPT-4o
59.12
64.77
44.95
59.82
74.31
49.75
Amazon-Nova-Pro
52.87
59.11
41.35
51.06
72.89
39.94
Palmyra-X-004
50.68
56.37
39.12
48.95
70.64
38.52
PaLM-2
46.83
52.89
36.15
47.81
63.42
34.88
Jamba-1.5-Large
47.95
53.64
36.02
48.97
63.91
36.21
Solar-Pro
44.33
43.12
32.87
40.63
71.85
36.88
Open-Weight Models
DeepSeek-v3
63.87
67.95
52.11
65.84
76.43
57.02
Llama-3.1-405B-Instruct
57.89
60.34
44.72
59.03
74.62
50.84
DBRX-Instruct
45.71
48.03
34.92
43.75
66.24
35.81
Arctic-Instruct
43.65
45.91
30.45
42.88
63.07
34.94
Gemma-7B
40.15
46.22
32.14
42.37
54.69
28.53
Command-R
37.84
36.95
24.83
33.62
61.15
32.65
Yi-6B
35.67
36.45
23.11
36.84
50.77
32.38
Qwen1.5-7B
35.92
38.14
28.33
31.45
49.12
31.56
Phi-2
33.15
35.89
24.76
34.12
43.95
26.03
Mistral-7B-v0.1
34.88
36.72
29.65
38.04
33.41
32.18
OLMo-7B
25.63
27.45
20.12
23.91
31.87
24.20
Table 4:
Average accuracy (%) on the B-REASO
HEAVY in AO and CoT prompting. Best values are
highlighted in purple, second-best in gray, separately
for proprietary and open-weight models.
Model
Five-shot AO
Five-shot CoT
Proprietary Models
Gemini-1.5-Pro-002
48.53
56.23
GPT-4o
42.34
49.11
Amazon-Nova-Pro
36.80
40.35
Jamba-1.5-Large
34.71
37.81
Solar-Pro
33.25
36.42
Open-Weight Models
Llama-3.1-405B-
Instruct
44.84
51.68
Command-R
30.06
32.50
Phi-2
26.59
-
Mistral-7B-v0.1
21.44
-
with negative words than those without. These re-
sults are consistent with earlier research.
5.5
Performance on Data Contamination
As discussed in Section 2.2.2, we use MIN-K%
PROB
(Chen et al., 2024b; Shi et al., 2023),
a reference-free technique for identifying pre-
training data from LLMs, to further examine the
potential for test data contamination. To determine
whether an input text is in the pre-training data,
MIN-K% PROB chooses a set of k% of tokens
from the input text with the minimum token prob-
ability and averages their log-likelihood. This is
based on the hypothesis that an example seen by
the model previously is less likely to include words
with low probability. For instance, if we have an in-
put example z = (z1, z2, ..., zn),
MIN-K% PROB(z) =
1
|Min-K(z)|
∑
zi∈Min-K(z) −log p(zi | z1, z2, . . . , zi−1)
where the set of k% of tokens in z with the low-
est token probability is represented by Min-K(z).
The likelihood that the input example z was seen
during pre-training increases with decreasing MIN-
K% PROB. MIN-K% PROB is applied to 13000
sampled instances from the base model Qwen1.5-
7B. Results are shown in Table 2 and Table 3. For
each sampled instance from B-REASO, we create
the input example x for MIN-K% PROB by con-
catenating the query and the matching alternatives,
which is consistent with the real scenario where
the model would probably be queried. We filtered
away the longest instances within each subject sub-
set of our dataset in order to lessen the impact of
input example length while calculating MIN-K%
PROB, as covered in the MIN-K% PROB study.
The purpose of this phase is to guarantee an impar-
tial and similar analysis. The tested Qwen1.5-7B
base model yields a 3.54% MIN-K% PROB for B-
REASO, suggesting that B-REASO is less likely
to include pre-trained data.
6
Conclusion
We think that LLM evaluations ought to go be-
yond simple conversational bots and help develop-
ers get LLMs ready for more complicated cases.
The development of the diﬀicult evaluation suite B-
REASO was primarily driven by this goal. In this
9266

--- Page 8 ---

Table 5: Average accuracy (%) in the Five-shot Answer Only setting, across educational diﬀiculty levels. Best
values are highlighted in purple, second-best in gray, separately for proprietary and open-weight models.
Model
Average
Middle School
High School
Professional
College
Proprietary Models
Claude-3.5-Sonnet
68.53
86.0
76.1
62.5
49.52
Gemini-1.5-Pro-002
62.03
80.5
68.0
55.0
44.62
GPT-4o
54.98
73.0
61.0
48.0
37.92
Open-Weight Models
DeepSeek-v3
61.74
79.2
66.8
55.4
45.56
Llama-3.1-405B-Instruct
55.35
71.5
59.9
49.3
40.70
Table 6: Average accuracy (%) in the Five-shot Chain of Thought setting, across educational diﬀiculty levels. Best
values are highlighted in purple, second-best in gray, separately for proprietary and open-weight models.
Model
Average
Middle School
High School
Professional
College
Proprietary Models
Claude-3.5-Sonnet
70.91
87.0
78.0
65.5
53.1
Gemini-1.5-Pro-002
64.75
82.0
70.5
58.1
48.4
GPT-4o
59.12
75.3
65.0
52.8
43.4
Open-Weight Models
DeepSeek-v3
63.87
80.5
69.1
57.9
48.0
Llama-3.1-405B-Instruct
57.89
73.0
62.5
52.1
44.0
regard, we believe that B-REASO and B-REASO
HEAVY have made significant strides, especially
in a Bengali environment. Additionally, we see
that B-REASO is far from ideal for evaluating
LLMs, as are all English-language benchmarks.
Aside from accuracy, there are several more ca-
pabilities like reasoning about and using APIs, as
well as several other elements like robustness, bias,
and safety. We leave it to future research to inves-
tigate their assessment further.
7
Related work
The performance of language models has signifi-
cantly improved in recent years. Thanks to larger
training datasets, more powerful computers, and
newly developed model architectures, this improve-
ment has been seen in accordance with the scal-
ing rule (Kaplan et al., 2020). LLMs like GPT-
3 (Brown et al., 2020), GPT-4 (Achiam et al.,
2023), Claude3, mT0 (Muennighoff et al., 2022),
XVERSE, Aya (Üstün et al., 2024), etc., are the
outcome of the ongoing process of scaling the
models.
Despite AI models’ exceptional ability
to solve a wide range of tasks, they nevertheless
struggle with real-world issues that call for sophis-
ticated mathematical computations or strong rea-
soning skills, for instance
(Chang et al., 2024;
Zhong et al., 2023). As a result, we must eval-
uate these models’ performance in handling chal-
lenging jobs. This helps us to pinpoint the models’
shortcomings and endeavor to strengthen them go-
ing forward. Research shows that while some of
the more current LLMs are multilingual, their eﬀi-
cacy is not as strong in low-resource or non-Latin
languages as it is in English (Zhang et al., 2023).
Therefore, multilingual LLMs must be evaluated
on tasks that use languages other than English.
A number of benchmarks have been created
to evaluate LLM performance.
The MMLU
(Hendrycks et al., 2020) is a crucial benchmark
that assesses language models’ ability to respond
to multiple-choice questions in 57 distinct tasks—
all in English. A multilingual, multimodal, and
multilevel benchmark for assessing LLMs is intro-
duced by M3Exam (Zhang et al., 2023). It consists
of over 12,000 multiple-choice questions in nine
languages (excluding Bengali) at three educational
levels. Another benchmark that evaluates LLMs’
performance on human-centric standardized tests
in Chinese and English to gauge their proficiency
in activities at the human level is AGIEval (Zhong
et al., 2023).
A professionally translated grade school math
problem from GSM8k in 10 languages–MGSM
(Shi et al., 2022), and BEnQA (Shafayat et al.,
2024) with 5K questions covering several subjects
in middle and high school science contains data
for Bengali. As per our best knowledge, there is
no comprehensive previous work with diverse do-
mains which has been done on LLMs’ understand-
ing specifically in Bengali language setup. For that,
we introduce B-REASO, the first complete Bengali
evaluation suite designed to fully evaluate LLMs’
9267

--- Page 9 ---

Table 7: Average accuracy (%) categorized by questions with (w) and without (w/o) negative phrases in zero-shot
and five-shot settings. Best values are highlighted in purple, second-best in gray, separately for proprietary and
open-weight models.
Model
Zero-shot (w)
Zero-shot (w/o)
Five-shot (w)
Five-shot (w/o)
Proprietary Models
Claude-3.5-Sonnet
65.17
63.54
69.02
65.48
GPT-4o
53.28
51.22
57.33
55.21
Amazon-Nova-Pro
47.05
48.24
50.12
52.03
Jamba-1.5-Large
45.12
45.85
47.45
48.32
Solar-Pro
41.05
44.83
44.00
47.52
Open-Weight Models
Llama-3.1-405B-Instruct
52.38
54.73
56.15
58.24
Command-R
29.92
36.62
35.04
39.01
Phi-2
24.89
33.35
29.97
34.51
Mistral-7B-v0.1
21.26
32.79
26.53
33.81
OLMo-7B
20.19
32.15
25.03
33.02
advanced knowledge and reasoning skills in a Ben-
gali environment, in an effort to close the gap be-
tween Bengali LLM development and assessment.
Limitations
It is important to recognize the limitations of our
effort. First off, throughout the dataset curation
process, we eliminated questions that featured fig-
ures, therefore our dataset was mostly composed
of text-based questions. This restriction may limit
the breadth of our findings because visual inquiries
frequently call for additional stages in the reason-
ing process. Furthermore, because the questions
are multiple-choice, there may be a chance that the
models may answer them more quickly, particu-
larly for factual questions that don’t call for sophis-
ticated thinking. Our dataset is a valuable place
to start when comparing LLMs in Bengali, which
at the moment have few resources for knowledge-
intensive and question-answering tasks, notwith-
standing these drawbacks.
Ethics Statement
We placed a strong emphasis on ethical responsibil-
ity, diversity, and cultural awareness when creating
B-REASO. Since each co-author on this article is
an educated participant who generated all of the
annotations, all contributors are given full credit
for their effort. We avoided utilizing any sensitive
or private information and carefully followed pub-
lically accessible, permissible where required and
reliable sources. Additionally, explicit instructions
were given on how to acquire participant permis-
sion, preserve data privacy, and honor local cus-
toms. Unintentional cultural bias may still happen
even with B-REASO attempts to reduce biases in
Bengali LLMs, especially in areas without direct
local representation. To fill up these gaps and guar-
antee that the dataset is continuously improved, we
promote community input.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al. 2023. Gpt-4 technical re-
port. arXiv preprint arXiv:2303.08774.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot
learners. Advances in neural information processing
systems, 33:1877–1901.
Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu,
Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan Yi,
Cunxiang Wang, Yidong Wang, et al. 2024. A sur-
vey on evaluation of large language models. ACM
Transactions on Intelligent Systems and Technology,
15(3):1–45.
Lingjiao Chen, Jared Quincy Davis, Boris Hanin, Pe-
ter Bailis, Ion Stoica, Matei A Zaharia, and James Y
Zou. 2024a. Are more llm calls all you need? to-
wards the scaling properties of compound ai systems.
Advances in Neural Information Processing Systems,
37:45767–45790.
Po-Heng Chen, Sijia Cheng, Wei-Lin Chen, Yen-Ting
Lin, and Yun-Nung Chen. 2024b.
Measuring tai-
wanese mandarin language understanding.
arXiv
preprint arXiv:2403.20180.
Hyung Won Chung, Le Hou, Shayne Longpre, Barret
Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi
Wang, Mostafa Dehghani, Siddhartha Brahma, et al.
2024. Scaling instruction-finetuned language mod-
els.
Journal of Machine Learning Research,
25(70):1–53.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
9268

--- Page 10 ---

Tafjord. 2018. Think you have solved question an-
swering? try arc, the ai2 reasoning challenge. arXiv
preprint arXiv:1803.05457.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, et al. 2021. Training verifiers to solve math
word problems. arXiv preprint arXiv:2110.14168.
Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon,
Pengfei Liu, Yiming Yang, Jamie Callan, and Gra-
ham Neubig. 2023.
Pal: Program-aided language
models.
In International Conference on Machine
Learning, pages 10764–10799. PMLR.
Omid Ghahroodi, Marzia Nouri, Mohammad Vali
Sanian, Alireza Sahebi, Doratossadat Dastgheib,
Ehsaneddin Asgari, Mahdieh Soleymani Baghshah,
and Mohammad Hossein Rohban. 2024. Khayyam
challenge (persianmmlu):
Is your llm truly wise
to the persian language?
arXiv preprint
arXiv:2404.06644.
Tanya Goyal, Junyi Jessy Li, and Greg Durrett. 2022.
News summarization and evaluation in the era of gpt-
3. arXiv preprint arXiv:2209.12356.
Dan Hendrycks, Collin Burns, Steven Basart, Andy
Zou, Mantas Mazeika, Dawn Song, and Jacob Stein-
hardt. 2020. Measuring massive multitask language
understanding. arXiv preprint arXiv:2009.03300.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and Ja-
cob Steinhardt. 2021. Measuring mathematical prob-
lem solving with the math dataset. arXiv preprint
arXiv:2103.03874.
Arian Hosseini,
Siva Reddy,
Dzmitry Bahdanau,
R Devon Hjelm, Alessandro Sordoni, and Aaron
Courville. 2021.
Understanding by understanding
not: Modeling negation in language models. arXiv
preprint arXiv:2105.03519.
Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei
Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu,
Chuancheng Lv, Yikai Zhang, Yao Fu, et al. 2024.
C-eval: A multi-level multi-discipline chinese evalu-
ation suite for foundation models. Advances in Neu-
ral Information Processing Systems, 36.
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B
Brown, Benjamin Chess, Rewon Child, Scott Gray,
Alec Radford, Jeffrey Wu, and Dario Amodei. 2020.
Scaling laws for neural language models.
arXiv
preprint arXiv:2001.08361.
Nora Kassner and Hinrich Schütze. 2019.
Negated
and misprimed probes for pretrained language mod-
els: Birds can talk, but cannot fly. arXiv preprint
arXiv:1911.03343.
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yu-
taka Matsuo, and Yusuke Iwasawa. 2022. Large lan-
guage models are zero-shot reasoners. Advances in
neural information processing systems, 35:22199–
22213.
Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, Hai
Zhao, Yeyun Gong, Nan Duan, and Timothy Bald-
win. 2023. Cmmlu: Measuring massive multitask
language understanding in chinese. arXiv preprint
arXiv:2306.09212.
Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang,
Ruochen Xu, and Chenguang Zhu. 2023.
G-eval:
Nlg evaluation using gpt-4 with better human align-
ment. arXiv preprint arXiv:2303.16634.
Pan Lu, Bowen Chen, Sheng Liu, Rahul Thapa, Joseph
Boen, and James Zou. 2025. Octotools: An agentic
framework with extensible tools for complex reason-
ing. arXiv preprint arXiv:2502.11271.
Grégoire Mialon,
Roberto Dessì,
Maria Lomeli,
Christoforos Nalmpantis, Ram Pasunuru, Roberta
Raileanu, Baptiste Rozière, Timo Schick, Jane
Dwivedi-Yu, Asli Celikyilmaz, et al. 2023.
Aug-
mented language models: a survey. arXiv preprint
arXiv:2302.07842.
Niklas Muennighoff, Thomas Wang, Lintang Sutawika,
Adam Roberts, Stella Biderman, Teven Le Scao,
M Saiful Bari, Sheng Shen, Zheng-Xin Yong, Hai-
ley Schoelkopf, et al. 2022.
Crosslingual general-
ization through multitask finetuning. arXiv preprint
arXiv:2211.01786.
Xuan-Phi Nguyen, Wenxuan Zhang, Xin Li, Mahani
Aljunied, Qingyu Tan, Liying Cheng, Guanzheng
Chen, Yue Deng, Sen Yang, Chaoqun Liu, et al. 2023.
Seallms–large language models for southeast asia.
arXiv preprint arXiv:2312.00738.
Sheikh Shafayat, H Hasan, Minhajur Mahim, Rifki Pu-
tri, James Thorne, and Alice Oh. 2024. Benqa: A
question answering benchmark for bengali and en-
glish. In Findings of the Association for Computa-
tional Linguistics ACL 2024, pages 1158–1177.
Freda Shi, Mirac Suzgun, Markus Freitag, Xuezhi
Wang, Suraj Srivats, Soroush Vosoughi, Hyung Won
Chung, Yi Tay, Sebastian Ruder, Denny Zhou,
et al. 2022.
Language models are multilin-
gual chain-of-thought reasoners.
arXiv preprint
arXiv:2210.03057.
Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo
Huang, Daogao Liu, Terra Blevins, Danqi Chen,
and Luke Zettlemoyer. 2023. Detecting pretraining
data from large language models.
arXiv preprint
arXiv:2310.16789.
Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik Narasimhan, and Shunyu Yao. 2023.
Re-
flexion: Language agents with verbal reinforcement
learning. Advances in Neural Information Process-
ing Systems, 36:8634–8652.
9269

--- Page 11 ---

Mirac Suzgun, Nathan Scales, Nathanael Schärli, Se-
bastian Gehrmann, Yi Tay, Hyung Won Chung,
Aakanksha Chowdhery, Quoc V Le, Ed H Chi,
Denny Zhou, et al. 2022.
Challenging big-bench
tasks and whether chain-of-thought can solve them.
arXiv preprint arXiv:2210.09261.
Zhi Rui Tam, Ya Ting Pai, Yen-Wei Lee, Hong-Han
Shuai, Jun-Da Chen, Wei Min Chu, and Sega Cheng.
2024.
Tmmlu+: An improved traditional chinese
evaluation suite for foundation models. In First Con-
ference on Language Modeling.
Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-
Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan
Schalkwyk, Andrew M Dai, Anja Hauth, Katie
Millican, et al. 2023.
Gemini:
a family of
highly capable multimodal models. arXiv preprint
arXiv:2312.11805.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, et al. 2023.
Llama:
Open and eﬀi-
cient foundation language models.
arXiv preprint
arXiv:2302.13971.
Ahmet Üstün, Viraat Aryabumi, Zheng-Xin Yong, Wei-
Yin Ko, Daniel D’souza, Gbemileke Onilude, Neel
Bhandari, Shivalika Singh, Hui-Lee Ooi, Amr Kayid,
et al. 2024.
Aya model: An instruction finetuned
open-access multilingual language model.
arXiv
preprint arXiv:2402.07827.
Alex Wang. 2018. Glue: A multi-task benchmark and
analysis platform for natural language understanding.
arXiv preprint arXiv:1804.07461.
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Aman-
preet Singh, Julian Michael, Felix Hill, Omer Levy,
and Samuel Bowman. 2019. Superglue: A stickier
benchmark for general-purpose language understand-
ing systems.
Advances in neural information pro-
cessing systems, 32.
Xiaoxuan Wang, Ziniu Hu, Pan Lu, Yanqiao Zhu, Jieyu
Zhang, Satyen Subramaniam, Arjun R Loomba,
Shichang Zhang, Yizhou Sun, and Wei Wang.
2023. Scibench: Evaluating college-level scientific
problem-solving abilities of large language models.
arXiv preprint arXiv:2307.10635.
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le,
Ed Chi, Sharan Narang, Aakanksha Chowdhery, and
Denny Zhou. 2022. Self-consistency improves chain
of thought reasoning in language models.
arXiv
preprint arXiv:2203.11171.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
et al. 2022. Chain-of-thought prompting elicits rea-
soning in large language models. Advances in neural
information processing systems, 35:24824–24837.
Yuxi Xie, Kenji Kawaguchi, Yiran Zhao, James Xu
Zhao, Min-Yen Kan, Junxian He, and Michael Xie.
2024. Self-evaluation guided beam search for rea-
soning. Advances in Neural Information Processing
Systems, 36.
Wenxuan Zhang,
Mahani Aljunied,
Chang Gao,
Yew Ken Chia, and Lidong Bing. 2023. M3exam: A
multilingual, multimodal, multilevel benchmark for
examining large language models. Advances in Neu-
ral Information Processing Systems, 36:5484–5505.
Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo
Liang, Shuai Lu, Yanlin Wang, Amin Saied, Weizhu
Chen, and Nan Duan. 2023.
Agieval: A human-
centric benchmark for evaluating foundation models.
arXiv preprint arXiv:2304.06364.
Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei,
Nathan Scales, Xuezhi Wang, Dale Schuurmans,
Claire Cui, Olivier Bousquet, Quoc Le, et al. 2022.
Least-to-most prompting enables complex reason-
ing in large language models.
arXiv preprint
arXiv:2205.10625.
9270

--- Page 12 ---

A
Precis of Explanation Curation
Figure 4 illustrates our pipeline for curating chain-
of-thought (CoT) explanations. We first prompt
the Claude-3.5-Sonnet language model with a
five-shot prompt: five human-written question–
explanation exemplars followed by a new multiple-
choice item and its gold answer. The model returns
a draft, step-wise explanation that justifies the gold
answer and, where appropriate, rules out distrac-
tors. To ensure factual accuracy, clarity, and stylis-
tic consistency with our dataset, all drafts then un-
dergo human post-editing. Editors correct any sci-
entific imprecision, remove extraneous reasoning,
and harmonize terminology across items. The fi-
nal curated explanations retain the model’s useful
reasoning when correct, but the human-edited ver-
sion is the one released and used in all evaluations.
বাংলােদেশরমাধয্িমকিবদয্ালেয়ররসায়নসƊেকর্বহ‍ুিনবর্াচনীàƣগ‍ু-
Ǭলিনেচেদওয়াহল।অনুÍহকেরিনƉǬলিখতàƣ এবংউত্তরগ‍ুǬলর
উপরিভǬত্তকেরএকিটসিঠকএবংযুǬğসĳতবয্াখয্াৈতিরকর‍ুন।
Following are multiple-choice questions about middle school chem-
istry in Bangladesh. Please generate a correct and reasonable expla-
nation based on the following questions and answers.
... [5-shot instances] ...
àƣঃ
িনেচরেকানিটিবশ‍ুŞ পদাথর্?
A. বাতাস
B. খিনজজল
C. অǭĥেজন
D. হাইেØােĤািরকঅয্ািসড
Question:
Which of the following is a pure substance?
A. Air
B. Mineral water
C. Oxygen
D. Hydrochloric acid
উত্তরঃC
Answer: C
বয্াখয্াঃধােপধােপভাবাযাক।
(A) বাতাসনাইেÖােজন, অǭĥেজন, কাবর্নডাইঅĥাইডইতয্ািদগয্ােসর
িমèেণগিঠত।এেতএকািধকউপাদানথােক, তাইএিটিমè পদাথর্।
(B) খিনজজেলপািন, খিনজলবণ, েÖসউপাদানইতয্ািদথােক।এিট
একািধকপদােথর্রিমèণ, তাইএিটিমè পদাথর্।
(C) অǭĥেজন(O2) শ‍ুধুমাÛ অǭĥেজনঅণুĆারাগিঠতএবংেকােনা
অনয্উপাদানেনই।তাইএিটিবশ‍ুŞ পদাথর্।
(D) হাইেØােĤািরকঅয্ািসডহেলাহাইেØােজনেĤারাইড(HCl) গয্ােসর
জলীয়Ýবণ।এেতHCl এবংপািনদুিটপদাথর্ইথােক, তাইএিটিমè
পদাথর্।
অতএব, সিঠকউত্তরহলC।
Explanation: Let‘s think step by step.
(A) Air is a mixture of nitrogen, oxygen, carbon dioxide, etc., mak-
ing it a mixture, not a pure substance.
(B) Mineral water contains water, minerals, and trace elements, so
it is a mixture.
(C) Oxygen (O2) consists of only oxygen molecules, making it a
pure substance.
(D) Hydrochloric acid is a solution of Hydrogen Chloride (HCl) gas
in water, containing both substances, so it is a mixture.
Therefore, the correct answer is C.
Figure 4: Claude-3.5-Sonnet generates a draft CoT ex-
planation from a five-shot prompt.
B
Prompts for Evaluation
We evaluate models under two prompting regimes:
Answer-Only (AO) and Chain-of-Thought (CoT).
Figures 6 and 7 present the exact templates.
All prompts are bilingual to match the dataset,
and mathematical/physical symbols are typeset in
LATEX (see Fig. 5). We run both few-shot (5-shot)
and zero-shot settings by either including or omit-
ting the exemplar items. In AO, the model is in-
structed to select a single option without justifica-
tion. In CoT, the model is asked to provide a brief
step-by-step rationale and the final choice; unless
otherwise noted, accuracy metrics are computed
from the final choice.
àƣঃ
গিতশǬğরসূÛিট$KE = \frac{1}{2} m v^2$, েযখােন$m$ হলএকিট
বǛরভরএবং$v$ হলতারেবগ।একিট$2.0 \mathrm{kg}$ বǛ
$5.0 \mathrmm/s$ গিতেতচেলএবংএকিটǬƵর$3.0 \mathrm{kg}$
বǛরসােথসƊূণর্র‍ূেপঅǬƵরভােবসংঘষর্কের।সংঘেষর্রপরতােদর
সাধারণেবগকতহেতপাের?
Question:
It is known that the kinetic energy formula is $KE = \frac{1}{2} m
v^2$, where $m$ is the mass of an object and $v$ is its velocity. A
$2.0 \mathrm{kg}$ object moves at $5.0 \mathrmm/s$ and collides
completely inelastically with a stationary $3.0 \mathrm{kg}$
object. What could be their common velocity after the collision?
Figure 5: Illustration from the B-REASO dataset show-
ing that symbolic expressions are rendered in LATEX.
বাংলােদেশউķ িবদয্ালেয়রগিণতসƊেকর্বহ‍ুিনবর্াচনীàƣগ‍ুǬলিনেচ
েদওয়াহল।অনুÍহকেরসিঠকউত্তরিটিনবর্াচনকর‍ুন।
Following are multiple-choice questions about high school Mathe-
matics in Bangladesh. Please select the correct answer.
... [5-shot instances] ...
àƣঃ
িনেচরেকানিটিĆঘাতসমীকরণf(x)
=
2x2 −4x + 1 এর
শীষর্িবūুরƵানাİ?
A. (1, -1)
B. (2, 1)
C. (-1, 7)
D. (0, 1)
Question:
Which of the following is the vertex coordinate of the quadratic
equation f(x) = 2x2 −4x + 1?
A. (1, -1)
B. (2, 1)
C. (-1, 7)
D. (0, 1)
উত্তরঃA
Answer: A
Figure 6: AO evaluation template (few-shot shown).
The zero-shot variant uses the same template without
the exemplar instances.
9271

--- Page 13 ---

বাংলােদেশমাধয্িমকিবদয্ালেয়রজীবিবজ্ঞানসƊেকর্বহ‍ুিনবর্াচনীàƣ
িনেচেদওয়াহল।অনুÍহকেরসিঠকউত্তরিটিনবর্াচনকর‍ুন।
Following are multiple-choice questions about middle school Biol-
ogy in Bangladesh. Please select the correct answer.
... [5-shot instances] ...
àƣঃ
িনেচরেকানিটবাǛতেű িবেযাজেকরভɋিমকাপালনকের?
A. ঘাস
B. িসংহ
C. মাশর‍ুম
D. ঈগল
Question:
Which of the following is a pure substance?
A. Grass
B. Lion
C. Mushroom
D. Eagle
উত্তরঃC
Answer: C
বয্াখয্াঃধােপধােপভাবাযাক।
(A) ঘাসসােলাকসংেƥষেণরমাধয্েমিনেজরখাদয্ৈতিরকেরএবংবা-
Ǜতেű উৎপাদকিহেসেবকাজকের।
(B) িসংহঅনয্ানয্àাণীিশকারকেরখাদয্Íহণকের, তাইএিটÍাহক
(àাথিমকবামাধয্িমকÍাহক) িহেসেবপিরিচত।
(C) মাশর‍ুম(ছÛাক) মৃতৈজবপদাথর্েকেভেঙসরলঅৈজবপদােথর্
পিরণতকের।এরাবাǛতেű িবেযাজকিহেসেবগ‍ুর‍ুĄপূণর্ভɋিমকাপা-
লনকের।
(D) ঈগলঅনয্ানয্àাণীেকিশকারকেরখায়, তাইএিটওÍাহক(শীষর্
Íাহক) িহেসেবিবেবিচতহয়।
অতএব, সিঠকউত্তরহলC।
Explanation: Let‘s think step by step.
(A) Grass produces its own food through photosynthesis, acting as
a producer in the ecosystem.
(B) Lions hunt other animals for food, making them consumers (pri-
mary or secondary).
(C) Mushrooms (fungi) break down dead organic matter into simple
inorganic substances, acting as decomposers in the ecosystem.
(D) Eagles prey on other animals, classifying them as consumers
(top predators).
Therefore, the correct answer is C.
Figure 7: CoT evaluation template (few-shot shown).
The zero-shot variant omits the exemplars but preserves
the requirement to justify the final choice.
C
Tool Integrated Evaluation
Table 8:
Average accuracy (%) on the B-REASO
HEAVY in AO and CoT prompting in the tool integrated
setting. Best values are highlighted in purple, second-
best in gray, separately for proprietary and open-weight
models.
Model
Five-shot AO
Five-shot CoT
Proprietary Models
Gemini-1.5-Pro-002
63.2
71.3
GPT-4o
57.3
64.2
Open-Weight Models
Llama-3.1-405B-Instruct
59.9
66.7
The integration of advanced tool-use frameworks,
such as the recently developed OctoTools, is pro-
jected to significantly enhance the performance
of LLMs on complex reasoning benchmarks like
B-REASO HEAVY. OctoTools (Lu et al., 2025),
a training-free, open-source framework, empow-
ers LLMs with a planner-executor architecture and
standardized ”tool cards,” enabling them to seam-
lessly integrate a variety of tools without the need
for model retraining. We find in Table 8 that, inte-
grating OctoTools as intermediate reasoning steps
gain improvements of 1̃5-20% in the B-REASO
HEAVY benchmark.
D
Multi-Agent Evaluation with
Self-Reflection
Table 9:
Average accuracy (%) on the B-REASO
HEAVY in the self-reflected multi-agent setting (NA =
3, I = 2). Best values are highlighted in purple, second-
best in gray, separately for proprietary and open-weight
models.
Model
Five-shot Self-Reflected Multia-
gent (NA = 3, I = 2)
Proprietary Models
Gemini-1.5-Pro-002
78.4
GPT-4o
71.5
Amazon-Nova-Pro
62.7
Jamba-1.5-Large
59.2
Open-Weight Models
Llama-3.1-405B-Instruct
73.7
Multiagent system with Self-Reflection (Shinn
et al., 2023) allows models to collaborate, cri-
tique each other’s reasoning, and iteratively re-
fine their answers, which is particularly effective
for the complex, multi-step problems found in B-
REASO HEAVY. The projected scores below re-
flect a significant leap of 2̃5-30% in performance
(Table 9), especially for the most capable models
that can fully leverage such a sophisticated reason-
ing framework. Answer was taken with Majority-
Voting (Chen et al., 2024a) in the inference time.
E
Answer Choice Distribution
The distribution of correct answers across the four
options is as in Table 10.
Table 10: Distribution across different options.
Option
Weight (%)
Option A
25.4
Option B
25.2
Option C
25.5
Option D
23.9
The distribution shows that the correct answers
are nearly evenly balanced.
F
Annotation Guidelines
We spent almost three months iteratively develop-
ing our annotation rules. Developed by four senior
team members after consulting with a larger group
9272

--- Page 14 ---

of participants, the initial version of the guidelines
included the project’s primary goals, the subject
areas from which the data will be gathered, and a
number of country-specific instruction types (such
as different kinds of open-ended requests and ques-
tions) supported by extensive examples. Addition-
ally, we used examples from reliable information
sources (see below) as references for compiling the
data. After that, the team members were given ac-
cess to this preliminary version of the instructions,
and they were instructed to use it to create a pilot
dataset. Following several sessions, we made more
improvements to the guidelines, resulting in a com-
prehensive version that was 100 pages long. Af-
ter that, all team members received training using
this final version to guarantee uniformity across the
project. According to our guidelines, the annota-
tors were asked to develop instructions for two pri-
mary categories: the general category, which cov-
ers MSA instructions for general knowledge like
science and technology, and the country-specific
category, where the annotators offer instructions
that reflect the culture of their nation on a variety
of subjects, such as regional holidays, idioms, lo-
cal geography, national history, and cuisine. The
instructions particular to each nation may be given
in either MSA or the local dialect.
Annotation Rules. Following refers further infor-
mation regarding our annotation rules: (i) Annota-
tors are advised to exclusively utilize trustworthy
sources, which might include but are not restricted
to: Wikipedia, books, specialized websites, gov-
ernment websites, and online encyclopedias. (ii)
Annotators are expected to give answers that are
objective, grounded in factual information and ac-
cepted knowledge for specific topics and domains;
in domains like politics and religion, they should
only present information without adding their own
opinions or interpretations.
(iii) Annotators are
urged to use their creativity by producing a wide
variety of instructions in every field.
Information Sources. We stress the need of refer-
ring to credible and authoritative sources while cre-
ating instructions in order to guarantee good data
quality. It was always recommended that annota-
tors thoroughly verify these sources. Wikipedia
and other reliable online encyclopedias, schol-
arly publications, oﬀicial websites, and specialized
platforms (such as websites run by health organiza-
tions that provide medical information) are exam-
ples of excellent sources. We specifically advised
against depending on one person’s sources, includ-
ing social media posts or personal posts, unless
that person is a well-known authority in the sub-
ject. Notably, internet forums and conversations
frequently yield the most insightful information in
fields like tourism, culinary arts, and culturally dis-
tinct festivities. In these situations, we made use of
the local cultural expertise and discernment of the
annotators to guarantee the reliability and applica-
bility of the data.
9273

--- Page 15 ---

G
Precis of B-REASO’s Task
Table 11: An overview of the subjects considered for evaluation, organized across multiple academic and profes-
sional fields: the categorization of subjects together with their corresponding number of instances.
Field
Subject
#Instances
STEM
Probability and Statistics (সƌাবনাওপিরসংখয্ান)
189
College Physics (িবđিবদয্ালয়পদাথর্িবদয্া)
200
High School Mathematics (উķ মাধয্িমকগিণত)
189
Computer Network (কǮƊউটারেনটওয়াকর্)
195
Operating System (অপােরিটংিসেƲম)
203
College Programming (িবđিবদয্ালয়েàাÍািমং)
384
Veterinary Medicine (পশ‍ুিচিকৎসািবদয্া)
238
Middle School Chemistry (মাধয্িমকরসায়ন)
210
Middle School Physics (মাধয্িমকপদাথর্িবদয্া)
202
High School Physics (উķ মাধয্িমকপদাথর্িবদয্া)
199
High School Chemistry (উķ মাধয্িমকরসায়ন)
196
Middle School Mathematics (মাধয্িমকগিণত)
201
Computer Architecture (কǮƊউটারআিকর্েটকচার)
219
College Chemistry (িবđিবদয্ালয়রসায়ন)
253
Electrical Engineering (ৈবদুয্িতকàেকৗশলিবদয্া)
381
Metrology Engineering (পিরমাপকàেকৗশলিবদয্া)
248
High School Biology (উķ মাধয্িমকজীবিবজ্ঞান)
199
Advanced Mathematics (উķতরগিণত)
197
Discrete Mathematics (িবǭĸŭ গিণত)
174
Middle School Biology (মাধয্িমকজীবিবজ্ঞান)
218
Social Science
High School Geography (উķ মাধয্িমকভɋেগাল)
202
College Economics (িবđিবদয্ালয়অথর্নীিত)
557
Education Science (িশক্ষািবজ্ঞান)
304
Middle School Geography (মাধয্িমকভɋেগাল)
125
Teacher Qualification (িশক্ষকেযাগয্তা)
448
High School Politics (উķ মাধয্িমকরাজনীিত)
200
Middle School Politics (মাধয্িমকরাজনীিত)
219
Business Administration (বয্বসাàশাসন)
339
Humanities
Logic (যুǬğিবদয্া)
231
High School History (উķ মাধয্িমকইিতহাস)
207
Law (আইনিবদয্া)
250
Art Studies (িশƚকলা)
336
Ideological Cultivation (ৈনিতকতাচচর্া)
196
Middle School History (মাধয্িমকইিতহাস)
234
Professional Tour Guide (েপশাগতপযর্টকগাইড)
300
Legal Professional (আইনেপশাগতেযাগয্তা)
243
Bangladesh Specific
Bangladesh History (বাংলােদশইিতহাস)
240
Bengali Language and Literature (বাংলাভাষাওসািহতয্)
237
High School Bengali (উķ মাধয্িমকবাংলা)
202
Other
Civil Service (সরকািরচাকির)
481
Fire Engineering (অিī িনরাপত্তাàেকৗশলিবদয্া)
318
Urban and Rural Planning (নগরওÍামীণপিরকƚনািবদয্া)
469
Accounting (িহসাবিবজ্ঞান)
497
Basic Medicine (àাথিমকিচিকৎসািবজ্ঞান)
199
Environmental Engineering (পিরেবশàেকৗশলিবদয্া)
317
Plant Protection (উিŠদসংরক্ষণ)
226
Sports Science (Ëীড়ািবজ্ঞান)
204
Clinical Medicine (িĤিনকয্ালিচিকৎসািবজ্ঞান)
227
Tax Accounting (করিহসাবিবজ্ঞান)
497
Physician (িচিকৎসকেযাগয্তা)
497
9274

```
