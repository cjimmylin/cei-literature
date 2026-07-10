---
title: "Evaluation Cultural Value Alignment - PDF Extract"
source_pdf: "2025-Sukiennik-Evaluation Cultural Value Alignment.pdf"
pages: 13
extracted_at: "2026-04-03T11:05:46.880973"
---

# PDF Extract: Evaluation Cultural Value Alignment

**Source PDF:** 2025-Sukiennik-Evaluation Cultural Value Alignment.pdf
**Total Pages:** 13

---

## Content

--- Page 1 ---

An Evaluation of Cultural Value Alignment in LLM
Nicholas Sukiennik
Department of Electronic Engineering
Tsinghua University
Beijing, China
sukiennikn10@mails.tsinghua.edu.cn
Chen Gao
BNRist
Tsinghua University
Beijing, China
chgao96@gmail.com
Fengli Xu
Department of Electronic Engineering
Tsinghua University
Beijing, China
fenglixu@tsinghua.edu.cn
Yong Li
Department of Electronic Engineering
Tsinghua University
Beijing, China
liyong07@tsinghua.edu.cn
Abstract
LLMs as intelligent agents are being increasingly applied in scenarios where
human interactions are involved, leading to a critical concern about whether
LLMs are faithful to the variations in culture across regions. Several works
have investigated this question in various ways, finding that there are
biases present in the cultural representations of LLM outputs. To gain a
more comprehensive view, in this work, we conduct the first large-scale
evaluation of LLM culture assessing 20 countries’ cultures and languages
across ten LLMs. With a renowned cultural values questionnaire and
by carefully analyzing LLM output with human ground truth scores, we
thoroughly study LLMs’ cultural alignment across countries and among
individual models. Our findings show that the output over all models
represents a moderate cultural middle ground. Given the overall skew,
we propose an alignment metric, revealing that the United States is the
best-aligned country and GLM-4 has the best ability to align to cultural
values. Deeper investigation sheds light on the influence of model origin,
prompt language, and value dimensions on cultural output. Specifically,
models, regardless of where they originate, align better with the US than
they do with China. The conclusions provide insight to how LLMs can be
better aligned to various cultures as well as provoke further discussion of
the potential for LLMs to propagate cultural bias and the need for more
culturally adaptable models.
1
Introduction
Large language models (LLMs), with their astonishing linguistic capabilities, demonstrate
human-like reasoning and behavioral abilities across a multitude of tasks (Zhao et al., 2023),
and with their widespread usage, they have more and more obligated to provide realistic
and accurate responses. That is, alignment in LLMs is essential for these models to provide
trustworthy responses to users. Specifically, alignment involves “ensuring that AI systems
pursue goals that match human values or interests rather than unintended and undesirable
goals” (Pan et al., 2022). Therefore, in this work, we present a comprehensive evaluation
of cultural value alignment across a gamut of LLMs, with input prompts that cover 20
countries and their respective languages. Our primary aim is to determine which models
align best to cultural values overall, and which countries are best aligned to. We further
examine the role of model origin on alignment results. To evaluate culture, we adopt a
well-known survey known as the Values Survey Module (Hofstede, 1980), a six dimension,
24-item survey where aggregated human responses form the ground truth culture scores
for each dimension and country. While prior works investigate culture bias in LLMs, ours
arXiv:2504.08863v1  [cs.CY]  11 Apr 2025

--- Page 2 ---

is the first to systematically address it on a broad, comprehensive scale over a range of
models, countries, and languages. We also present extensive factor analysis to understand
underlying causes and correlations, such as the influence of prompt language, model origin,
and external factors.
There are several research efforts about understanding and quantifying the presence of
alignment in LLM (Ngo et al., 2024; Ryan et al., 2024; Cao et al., 2023). By discovering the
presence of cultural misalignment on a large scale, our work is also related to these works
on LLM bias. Bias is a particular form of misalignment that occurs when the model reflects
only the perspectives of a certain sub-group or population (Li et al., 2022), which can serve
to reinforce asymmetries among groups within a society (Bender et al., 2021). The presence
of bias in LLMs is an unsolved problem due to the vast scope and scale of data that is used
to train them (Johnson et al., 2022). More specifically, culture bias is of particular interest,
especially for applications of LLMs that require them to interface with individuals from
different parts of the world, such as customer service chatbots, etc. Several works confirm
the presence of a Western cultural bias in LLMs due largely to the sources of the corpora
involved in their training (Naous et al., 2024; Arora et al., 2023; Navigli et al., 2023). Other
works address forms of bias that are unrelated to culture, such as ideologies (Buyl et al.,
2024; Santurkar et al., 2023), social identity biases (Hu et al., 2024), whereas (Yin et al., 2025)
address cultural and legal appropriateness in social interactions.
We briefly describe the works that are similar to ours and what we do differently to con-
tribute towards a substantial increase in understanding of LLMs’ cultural alignment. The
work that is most similar to ours is BLEnD (Myung et al., 2024), which tests the ability of
LLMs to adhere to culturally specific knowledge. Their work evaluates LLMs’ performance
using several models and languages to determine the presence of region bias and language
bias, discovering that the results heavily favor highly represented languages (e.g. English
and Spanish), as opposed to low-resource countries such as Nigeria and Ethiopia. However,
their work does not address the values component of culture. In contrast, a handful of works
address cultural values, but only in a limited context. Namely, AlKhamissi et al. (2024)
evaluate the cultural alignment of four LLMs on their cultural alignment for two cultures,
Egypt and the United States, using the languages English and Arabic, using Hofstede’s
survey to assess performance. Cao et al. (2023) evaluate cultural values alignment using five
languages and country-roles and only one GPT model, similarly using the Hofstede survey.
Finally, Tao et al. (2023) evaluate 107 countries’ cultures using only English prompts, and
three GPT models (GPT-3, GPT-3.5-Turbo, GPT -4), using the Integrated Values Survey to
measure culture (Inglehart, 2005). Each of these works paints a small portion of an overall
picture of cultural values alignment in LLMs, but due to the scarcity of models, countries,
and languages tested, as well as the inconsistency between methodologies across works,
such picture is far from complete. Inspired by their methodologies and with the goal of
completing this picture, our work scales up the analysis using 10 models, 20 countries and
languages, and conducts in-depth analysis to understand the underlying mechanisms and
correlations of cultural bias.
In addition to investigating the influence of prompt language on cultural alignment, we are
the first work to address the concern of models propagating cultural values based on their
origin. The overall contributions of this work are as follows:
1. We propose to study the overall state of LLM alignment on countries, and rank the
top-performing models and countries using a proposed alignment metric.
2. We conduct large-scale analysis on the results to understand the influence of model
origin, language, and model size on alignment, among other factors.
3. We find that the United States is the most closely aligned country across all models
by a wide margin, and that GLM-4 performs best on cultural alignment despite its
small size.

--- Page 3 ---

2
Methodology
In order to evaluate the overall state of cultural alignment of LLMs, we approach the
problem from two angles: 1) which LLMs align best across cultures, and 2) which countries
are aligned to the best. In answering these two questions, we can determine both the
ability and extent of different LLMs to embody a realistic cultural value system while
also determining the presence of bias in LLMs as a whole. Our study also examines the
relationship between alignment and prompt language, focusing on four types of language
prompting results:
1. Aligned Prompt Results, meaning that the prompt language is aligned with the main-
stream spoken or official language of a given country.
2. English and Chinese prompt results, motivated by the fact that the models tested origi-
nate in the US (mainstream language: English) and China (official language: Chinese).
Beyond prompt language, a deeper investigation of the implications of model origin is
also presented in section 4.2.
3. Language Average Results which is the average of the results over all promoted lan-
guages. In other words, for each culture-identity, the LLM is prompted with all 20
languages, regardless of alignment. The purpose of this is to determine whether there is
a convergence of culture for each country-role beyond the influence of prompt language.
The cultural assessments of obtained by prompting each LLM with the questions of the
Values Survey Module, a robust questionnaire by Geert Hofstede (Hofstede, 1980) that is
seen as the gold standard of cultural studies. The survey consists of 24 questions that are
broken down into six dimensions. The detailed use of the VSM is provided in Appendix
Section A.1.
For this evaluation, we select 20 countries and their corresponding primary language, shown
in Appendix Table A. The countries and languages are selected via a process of consideration
based on several factors. Most importantly, we aim to choose countries whose language has
a large number of native speakers while also being relatively exclusive to that country.
2.1
Alignment Measurement Metric
In the course of our investigation, we discover the presence of a moderate ”global average”
culture to which all models tend to conform, regardless of country-role or prompt language,
allowing us to better quantify cultural alignment given the presence of a bias-inducing
factor. We address this by proposing an evaluation metric called the deviation ratio. The
deviation ratio is the ratio between the deviation of an LLM’s cultural representation from
the global average culture and its difference from the ground truth, as seen in equation 1:
Deviation Ratio ==
1
6 ∑d∈D |GTd −GTd|
1
n ∑n
i=1 Differencei
,
(1)
where D contains the six cultural dimensions, GTd is the ground truth value for dimension d,
GTd is the global average ground truth for dimension d, Differencei represents the individual
model differences from ground truth, n is the number of trials being averaged, in this case
three. Without this metric, the countries whose inherent culture falls close to the global
average culture will automatically show more alignment, which is not a reflection of the
LLM’s capabilities. In contrast, if a country’s culture is far from the global average, yet still
closely aligned with the ground truth, then its evaluation will be much better than a country
whose culture is closer to the global average and just as closely aligned with the ground
truth, making for a more reliable evaluation.
3
Experimental Setup
Ten LLMs are prompted with each of the 20 countries as a role and in each of the correspond-
ing countries’ languages, i.e. 400 times each. Five US-origin models and five China-origin

--- Page 4 ---

Lang
System Role
Prompt & Response Options
Sample
Response
EN
Your role is an
average person
from
{country}.
In choosing an ideal job, having a boss you can
respect is: (1) of utmost importance; (2) very
important; (3) of moderate importance; (4) of little
importance; (5) of very little or no importance?
”2 - very
important”
Table 1: Prompting mechanism with system role, survey question and response options,
and a sample response.
models are selected, as to facilitate understanding of the influence of model origin on cul-
tural alignment. The models are chosen to represent those that are most popularly used
in their respective countries’ origin as well as globally. The models and their respective
information are provided in Table 2. The models were called using a temperature of zero as
to reduce deterministic outputs and increase reproducibility. Furthermore, each country-
language prompt was called three times and averaged for each model, further decreasing
the potential for outliers or randomness.
The specific prompting scheme is displayed in Table 1. The system role was also appended
with a statement to ”make only one choice and always include a numerical value in your
response.” The system role, including country names, was also translated to each respective
language as to prevent the influence of system role language affecting output culture.
Although the system role specifies to include a numerical response, some models offered
explanations for why such response was chosen, whereas some did not. Either way, only
the numerical response was extracted and used for analysis.
Model
Company
Size (B)
GPT-3.5-Turbo (OpenAI, 2023a)
OpenAI
∼20
GPT-4 (OpenAI, 2023b)
OpenAI
∼1750
GPT-4o (Hurst et al., 2024)
OpenAI
∼200
Gemini-1.5 (DeepMind, 2023)
Google
∼1500
LLaMa-3 (Touvron et al., 2023)
Meta
70
Deepseek-v2.5 (DeepSeek-AI, 2024)
Deepseek
236
GLM-4 (Du et al., 2022)
Zhipu AI/Tsinghua
9
Qwen-2.5-7B-Instruct (Qwen, 2024)
Alibaba
7
Qwen-2.5-32B-Instruct
Alibaba
32
Qwen-2.5-72B-Instruct
Alibaba
72
Table 2: The large language models used in this study and their specifications (∼denotes
approximation, as the parameters for certain models have not been publicly disclosed)
Outside of the overall evaluation of model and country alignment, we also delve into the
regional implications of alignment. While the question of which countries are aligned to
best for each LLM is worth inspecting, this work focuses on two special regional aspects
that, given the geographical implications of LLM development, are most insightful: the
comparison between China-origin and US-origin models. Finally, we delve into the influ-
encing factors towards cultural alignment, including prompt language, model size, and
external factors such as country GDP and digital population size per country.
Through the above cultural evaluation method, we aim to answer the following research
questions:
• RQ1: Which LLMs exhibit the best cultural alignment?
• RQ2: Which country is aligned to the best across all LLMs?
• RQ3: What is the influence of model origin and language on cultural alignment?
• RQ4: What external factors could lead to cultural misalignment or bias?

--- Page 5 ---

POW
IND
MASC
UAV
LTO
IVR
LLM Averages
POW
IND
MASC
UAV
LTO
IVR
Ground Truths
Bangladesh
China
Egypt
France
Germany
India
Indonesia
Iran
Japan
Korea
Pakistan
Philippines
Portugal
Russia
Spain
Tanzania
Thailand
Turkey
United States
Vietnam
Global Average
Ground Truth Average
Figure 1: Comparison of ground truth and raw country results, with average ground truth
and average of all LLM results.
4
Analysis Results
4.1
Results on Country and Model Basis
First, we evaluate the overall status of LLM alignment with countries’ cultures in compar-
ison with ground truth values over six dimensions 1. In Figure 1(a), the raw results for
each country are averaged over all models and plotted on a radar chart with 6 axes. The
average over all countries is shown in black. This is shown alongside the ground truths
of all countries and the average thereof in Figure 1(b). Immediately, we can make two
observations: 1) the cultural representations output by LLMs for all countries are very close
together, sitting close to the middle of the axis for nearly all dimensions, and 2) that the
LLM cultural representations, as a whole, are markedly different from their ground truth
counterparts.
To further examine the state of LLM cultural alignment on the country basis, the results for
each country are broken down into two metrics: the difference from the ground truth and
the deviation of the LLMs’ output from the global average. In Figure 2, we can clearly see
that, with the exception of the United States, there is a very strong linear relation between
the two metrics. From this, we can conclude that evaluating alignment with respect to the
ground truth would be insufficient. If only ground truth difference were considered, then
India would be the most well-aligned country. But because India’s culture sits very close to
the global average, the ground truth difference being close is merely incidental and does
not reflect LLM’s ability to adapt. Therefore, the true alignment can be derived by looking
at the ratio between the y and x axes, the results of which are seen in Table 3.
The conclusions of this figure motivate the rest of the study to examine not purely cultural
alignment, but culture alignment given a tendency to converge on a global average. In light of
this aim, we devise Equation 1, which is essentially y over x in Figure 2, to achieve a more
reliable metric for alignment.
We then evaluate the overall performance of all models using the new metric and the original
difference from ground truth, as seen in Figures 3(a) and (b). Although both figures rank
1The raw results of all models for each country can be found in Appendix Figure A

--- Page 6 ---

10
12
14
16
18
20
22
24
26
Difference from Ground Truth
7.5
10.0
12.5
15.0
17.5
20.0
22.5
25.0
27.5
Deviation from Global Average
Bangladesh
China
Egypt
France
Germany
India
Indonesia
Iran
Japan
Korea
Pakistan
Philippines
Portugal
Russia
Spain
Tanzania
Thailand
Turkey
United States
Vietnam
r = 0.54
Figure 2: Deviation from global average vs. differ-
ence from ground truth.
Country
Deviation Ratio
United States
1.99
Germany
1.13
Japan
1.03
India
1.02
Spain
1.02
Philippines
0.98
France
0.96
China
0.87
Iran
0.83
Egypt
0.80
Korea
0.79
Russia
0.77
Indonesia
0.76
Thailand
0.75
Vietnam
0.73
Tanzania
0.69
Pakistan
0.67
Turkey
0.66
Portugal
0.62
Bangladesh
0.59
Table 3: Country ranking.
GLM-4
Gemini-1.5
LLaMA-3
DeepSeek
GPT-4
GPT-4o
Qwen-7B
Qwen-32B
Qwen-72B
GPT-3.5
Model
16
17
18
19
20
21
22
Average Absolute Difference
(lower is better)
Aligned
Language Averages
English Results
Chinese Results
GLM-4
Gemini-1.5
LLaMA-3
Qwen-7B
DeepSeek
GPT-4
GPT-4o
Qwen-72B
Qwen-32B
GPT-3.5
Model
0.6
0.7
0.8
0.9
1.0
Deviation Ratio
(higher is better)
Aligned
Chinese Results
English Results
Language Averages
(a)
(b)
Figure 3: A comparison of model evaluation using two metrics: difference from ground
truth (lower = better), and deviation ratio (higher = better). Each model ranking contains
results with four prompting methods. The models that differ in rank between the two
figures are highlighted in red.
the first three models in the same position, the following six are in a distinct order, telling
us not only countries but also models, should be evaluated on the basis of the deviation
ratio and not purely ground truth difference. Figure 3 also serves as a ranking of models’
ability to align to cultural values. Therefore, we can conclude that GLM-4 has the strongest
ability to align among the models tested. With a closer look, we also note that the aligned
languages typically result in better alignment, as with Qwen 7B, despite some exceptions.
4.2
Model-Origin Analysis
Now that we have a basic idea of the strongest performing models for cultural alignment and
the countries they align with best, we delve deeper into the factors that may be influencing
these results. As the development of LLMs is recently being dominated by companies
and institutions in two countries, the US and China, the differences in these two countries’
models in terms of cultural output are worth investigating. Findings can serve to reinforce
or dispel concerns that models are imbued with values from their creators (Buyl et al., 2024;
Santurkar et al., 2023).

--- Page 7 ---

United States
China
0.6
0.7
0.8
0.9
1.0
1.1
1.2
1.3
Deviation Ratio
1.21
0.76
1.14
0.77
1.14
0.76
US-Origin Models
United States
China
1.26
0.77
1.28
0.72
1.14
0.75
China-Origin Models
English
Chinese
Non-EN/ZH
(a)
(b)
Figure 4: Deviation ratio comparison between models of US-origin (a) and China-origin
(b), and three forms of prompts: English, Chinese, and the average of all other languages.
Scores show alignment to US and China ground truth culture scores.
US-Origin Models
China-Origin Models
0.85
0.90
0.95
1.00
1.05
1.10
Average Deviation Ratio
1.02
0.99
1.00
0.96
0.94
0.95
English
Chinese
Non-EN/ZH
Figure 5: Model origin between US and China-origin models, prompted in English, Chinese,
and the average of all other languages. Scores are averaged over all country results to show
average alignment w.r.t. model-original and prompt language.
First, we aim to determine whether there is an overall difference in alignment between US
and China-origin models in exhibiting the cultures of those same two countries in Figure
4. To make the inquiry more nuanced, we separate results by three forms of language
prompting: English, Chinese, and the average of all other languages. For US-origin models,
we find that there is an intuitive trend in that English prompting results in better alignment
with US culture, and Chinese with China, but there is an opposite trend among China-
origin models. We also note that China-origin models are able to align to US culture better
than US-origin models, regardless of English or Chinese as the prompt language. We
also determine the state of alignment on the models of both countries’ origins in their
culture representations of all countries, illustrated in Figure 5. We find that on average,
US-origin models align better across cultures with prompts in English and Chinese, whereas
China-origin models align slightly better using other languages.
In sum, there is no reason for concern that China-origin models will be imposing any
misaligned cultural values on users, as they are able to align very well with US culture in
all languages. However, one also might ask why China-origin models are not able to align
better with the culture of their origin country. Some possible insights towards this question
are provided in the following section.
4.3
Model-Size and External Factors
It does not suffice to state which models and countries have the best alignment without
asking why this is so. In Figure 6, we attempt to answer this question by correlating
model size with model alignment and three external factors to country alignment: digital

--- Page 8 ---

10
100
1000
Model Size (Billions of Parameters, log scale)
0.74
0.76
0.78
0.80
0.82
0.84
Average Deviation Ratio
DeepSeek
GLM-4
Qwen-32B
Qwen-72B
Qwen-7B
Gemini-1.5
GPT-3.5
GPT-4
GPT-4o
LLaMA-3
Pearson r (log) = 0.13
China-Origin Models
US-Origin Models
0
200
400
600
800
1000
Digital Population (Millions)
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Average Deviation Ratio
Bangladesh
China
Egypt
France
Germany
India
Indonesia
Iran
Japan
Korea
Pakistan
Philippines
Portugal Russia
Spain
Tanzania
Thailand
Turkey
United States
Vietnam
Pearson r = 0.20
0
10
20
30
40
50
Percentage of Web Content from Country (%)
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Average Deviation Ratio
China
France
Germany
Indonesia
Iran
Japan
Korea
Portugal
Russia
Spain
Thailand
Turkey
United States
Vietnam
Pearson r = 0.94
0
5
10
15
20
25
GDP (Trillions of USD)
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0
Average Deviation Ratio
Bangladesh
China
Egypt
France
Germany
India
Indonesia
Iran
Japan
Korea
Pakistan
Philippines
Portugal
Russia
Spain
Tanzania
Thailand
Turkey
United States
Vietnam
Pearson r = 0.81
(a)
(b)
(c)
(d)
Figure 6: Figures comparing alignment with model size and external factors.
population 2, percentage of web content 3, and GDP 4. For web content per country, we
approximate using data for the fraction of content in each country’s primary language.
First, in Figure 6(a), we see the relationship between model size, given in billions of pa-
rameters, and overall alignment. While there is a somewhat log-linear relationship, GLM-4
contradicts expectations by being the strongest aligning model despite having the second
lowest number of parameters, only 9 billion. This suggests that there is more to cultural
value alignment than just model parameter size. Among Figures 6(b) through (d), we note
that there are very strong correlations between LLM cultural alignment and two external
factors: the quantity of web content per country and national GDP. The main difference
between the two is that China’s web content proportion is not commensurate with its GDP,
causing the person correlation to be lower for Figure 6(d) than for (c). However, although
the correlation in 6(c) is very strong, it is important to note that all countries have both
very low cultural alignment scores and content percentages compared to the United States.
This means that an important future direction for cultural adaptation in LLMs is to increase
the availability of training data from non-US countries. Finally, we examine the influence
on cultural dimensions and alignment. In Figure 7, the average deviation ratios over each
dimension over all countries and models is displayed. From this figure we observe that cer-
tain dimensions are more readily ”alignable” than others. Namely, power distance (POW)
and uncertainty avoidance (UAV) are more easily aligned to than masculinity (MASC),
individualism (IND), and indulgence vs. restraint (IVR). These findings tell us that, perhaps
with training data that is more representative of the more difficult dimensions, the obstacle
to aligning with more difficult dimensions can be overcome.
2World
Bank,
2023.
”Individuals
using
the
Internet
(%
of
population)”,
https://data.worldbank.org/indicator/IT.NET.USER.ZS
3”Usage
statistics
of
content
languages
for
websites”.
W3Techs
2024
survey.
https://w3techs.com/technologies/overview/content language
4World Bank, 2023. ”GDP (current US$)”, https://data.worldbank.org/indicator/NY.GDP.MKTP.CD

--- Page 9 ---

10
12
14
16
18
20
22
24
26
Average Difference from Ground Truth
1
2
3
4
5
6
Dimension-Specific Deviation Ratio
POW
IND
MASC
UAV
LTO
IVR
Figure 7: Ground truth difference vs. dimension-specific deviation ratio (higher DR is better)
5
Related Works
Bias in LLMs has garnered wide attention in the research community. Liang et al. (2021)
was one of the first to establish benchmarks and propose mitigating strategies for bias in
GPT-2. More recently Tao et al. (2023) quantify the cultural bias of GPT-3, ChatGPT, and
GPT-4 as being close to Western European countries on a two-dimensional cultural scale
and mitigates it with a simple cultural prompting strategy. Masoud et al. (2023) come to
similar conclusions showing that LLMs tend to display Western values. Notably, Abid et al.
(2021) find striking evidence of a consistent anti-Muslim bias in LLMs. Huang & Yang (2023)
find that ChatGPT and GPT-4 tend to normalize culturally interpretable scenarios to an
American context based on comparing interpretations between US and Indian annotators.
Meanwhile, fairness in machine learning has been examined by Barocas et al. (2023) and
by Blodgett et al. (2020) for the NLP scenario. Jakesch et al. (2023) find that writing with
an LLM co-writer can cause one’s writing to be opinionated in a certain way. In order to
help the research community tackle these issues, Dhamala et al. (2021) provide a dataset of
prompts for bias benchmarking. Durmus et al. (2023) also contribute to bias mitigation by
designating three types of culture auditing, finding that cross-national prompting succeeds
at adapting the model’s responses to a specified country’s culture. In turn, our work is the
first to conduct a large-scale, comprehensive evaluation of LLM cultural value alignment
over models, countries, and languages, including previously neglected factors such as
model origin and external factors.
6
Conclusions
In this work, we investigate the state of cultural value alignment in LLMs using a wide
array of models, countries, and languages to understand which countries are best aligned to,
and which models best align to them. We immediately discover that LLMs skew all cultures
toward a moderate global average culture that is close to the median possible value for all
dimensions. Therefore we devise a metric called the deviation ratio to evaluate alignment
in spite of this skew, favoring models that are able to align to countries whose ground truth
values are further from the global average. The results of the analysis tell us that the United
States culture is most readily aligned by a wide margin, and that this could be in large
part explained by the amount of training data available in comparison to other countries.
Additionally, we find that GLM-4 is able to align best across cultures despite having a very
low parameter size, suggesting that there are factors besides model size that are crucial
to cultural alignment. We also find that both China-origin models and US-origin models
align better to the United States than to China, and that models prompted in English are
able to align better to all cultures on average as opposed to Chinese or any other language.
Some limitations of our study include the countries and languages chosen. There are many
countries that have several spoken languages, and since we only test one language per
country, our cultural alignment evaluations cannot be considered complete. Furthermore,
there is the question of how LLMs align to the cultures of countries that have the same
primary language. We leave these tasks for future work.

--- Page 10 ---

References
Abubakar Abid, Maheen Farooqi, and James Zou. Persistent anti-muslim bias in large
language models. In Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society,
pp. 298–306, 2021.
Badr AlKhamissi, Muhammad ElNokrashy, Mai AlKhamissi, and Mona Diab. Investigating
Cultural Alignment of Large Language Models, February 2024. URL http://arxiv.org/
abs/2402.13231. arXiv:2402.13231 [cs].
Arnav Arora, Lucie-Aim´ee Kaffee, and Isabelle Augenstein. Probing Pre-Trained Language
Models for Cross-Cultural Differences in Values, April 2023. URL http://arxiv.org/
abs/2203.13722. arXiv:2203.13722 [cs].
Solon Barocas, Moritz Hardt, and Arvind Narayanan. Fairness and machine learning: Limita-
tions and opportunities. MIT Press, 2023.
Emily M Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On
the dangers of stochastic parrots: Can language models be too big? In Proceedings of the
2021 ACM conference on fairness, accountability, and transparency, pp. 610–623, 2021.
Su Lin Blodgett, Solon Barocas, Hal Daum´e III, and Hanna Wallach. Language (technology)
is power: A critical survey of” bias” in nlp. arXiv preprint arXiv:2005.14050, 2020.
Maarten Buyl, Alexander Rogiers, Sander Noels, Iris Dominguez-Catena, Edith Heiter,
Raphael Romero, Iman Johary, Alexandru-Cristian Mara, Jefrey Lijffijt, and Tijl De Bie.
Large Language Models Reflect the Ideology of their Creators, October 2024.
URL
http://arxiv.org/abs/2410.18417. arXiv:2410.18417 [cs] version: 1.
Yong Cao, Li Zhou, Seolhwa Lee, Laura Cabello, Min Chen, and Daniel Hershcovich. As-
sessing Cross-Cultural Alignment between ChatGPT and Human Societies: An Empirical
Study, March 2023. URL http://arxiv.org/abs/2303.17466. arXiv:2303.17466 [cs].
Google DeepMind. Introducing gemini: our largest and most capable ai model. https:
//blog.google/technology/ai/google-gemini-ai, 12 2023. (Accessed on 07/12/2023).
DeepSeek-AI. Deepseek-v2: A strong, economical, and efficient mixture-of-experts language
model, 2024.
Jwala Dhamala, Tony Sun, Varun Kumar, Satyapriya Krishna, Yada Pruksachatkun, Kai-Wei
Chang, and Rahul Gupta. Bold: Dataset and metrics for measuring biases in open-ended
language generation. In Proceedings of the 2021 ACM conference on fairness, accountability,
and transparency, pp. 862–872, 2021.
Zhengxiao Du, Yujie Qian, Xiao Liu, Ming Ding, Jiezhong Qiu, Zhilin Yang, and
Jie Tang.
Glm: General language model pretraining with autoregressive blank in-
filling.
(arXiv:2103.10360), March 2022.
URL http://arxiv.org/abs/2103.10360.
arXiv:2103.10360 [cs].
Esin Durmus, Karina Nyugen, Thomas I. Liao, Nicholas Schiefer, Amanda Askell, Anton
Bakhtin, Carol Chen, Zac Hatfield-Dodds, Danny Hernandez, Nicholas Joseph, Liane
Lovitt, Sam McCandlish, Orowa Sikder, Alex Tamkin, Janel Thamkul, Jared Kaplan,
Jack Clark, and Deep Ganguli. Towards Measuring the Representation of Subjective
Global Opinions in Language Models, June 2023. URL http://arxiv.org/abs/2306.
16388. arXiv:2306.16388 [cs].
Geert Hofstede. Culture and Organizations. International Studies of Management & Organi-
zation, 10(4):15–41, December 1980. ISSN 0020-8825, 1558-0911. doi: 10.1080/00208825.
1980.11656300. URL https://www.tandfonline.com/doi/full/10.1080/00208825.1980.
11656300.
Tiancheng Hu, Yara Kyrychenko, Steve Rathje, Nigel Collier, Sander van der Linden, and
Jon Roozenbeek. Generative Language Models Exhibit Social Identity Biases, June 2024.
URL http://arxiv.org/abs/2310.15819. arXiv:2310.15819 [cs].

--- Page 11 ---

Jing Huang and Diyi Yang. Culturally Aware Natural Language Inference. In Houda
Bouamor, Juan Pino, and Kalika Bali (eds.), Findings of the Association for Computational
Linguistics: EMNLP 2023, pp. 7591–7609, Singapore, December 2023. Association for
Computational Linguistics. doi: 10.18653/v1/2023.findings-emnlp.509. URL https:
//aclanthology.org/2023.findings-emnlp.509.
Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark,
AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. arXiv
preprint arXiv:2410.21276, 2024.
Ronald Inglehart. Christian welzel modernization, cultural change, and democracy The human
development sequence. Cambridge: Cambridge university press, 2005.
Maurice Jakesch, Advait Bhat, Daniel Buschek, Lior Zalmanson, and Mor Naaman. Co-
Writing with Opinionated Language Models Affects Users’ Views. In Proceedings of
the 2023 CHI Conference on Human Factors in Computing Systems, pp. 1–15, Hamburg
Germany, April 2023. ACM. ISBN 978-1-4503-9421-5. doi: 10.1145/3544548.3581196. URL
https://dl.acm.org/doi/10.1145/3544548.3581196.
Rebecca L. Johnson, Giada Pistilli, Natalia Men´edez-Gonz´alez, Leslye Denisse Dias Duran,
Enrico Panai, Julija Kalpokiene, and Donald Jay Bertulfo. The Ghost in the Machine has
an American accent: value conflict in GPT-3, March 2022. URL http://arxiv.org/abs/
2203.07785. arXiv:2203.07785 [cs].
Yizhi Li, Ge Zhang, Bohao Yang, Chenghua Lin, Shi Wang, Anton Ragni, and Jie Fu. Herb:
Measuring hierarchical regional bias in pre-trained language models, 2022.
Paul Pu Liang, Chiyu Wu, Louis-Philippe Morency, and Ruslan Salakhutdinov. Towards
understanding and mitigating social biases in language models. In International Conference
on Machine Learning, pp. 6565–6576. PMLR, 2021.
Reem I. Masoud, Ziquan Liu, Martin Ferianc, Philip Treleaven, and Miguel Rodrigues.
Cultural Alignment in Large Language Models: An Explanatory Analysis Based on
Hofstede’s Cultural Dimensions, August 2023. URL http://arxiv.org/abs/2309.12342.
arXiv:2309.12342 [cs].
Junho Myung, Nayeon Lee, Yi Zhou, Jiho Jin, Rifki A. Putri, Dimosthenis Antypas,
Hsuvas Borkakoty, Eunsu Kim, Carla Perez-Almendros, Abinew A. Ayele, V´ıctor
Guti´errez-Basulto, Yazm´ın Ib´a˜nez-Garc´ıa, Hwaran Lee, Shamsuddeen H. Muham-
mad, Kiwoong Park, Anar S. Rzayev, Nina White, Seid M. Yimam, Mohammad T.
Pilehvar, Nedjma Ousidhoum, Jose Camacho-Collados, and Alice Oh.
BLEnD:
A Benchmark for LLMs on Everyday Knowledge in Diverse Cultures and Lan-
guages.
Advances in Neural Information Processing Systems, 37:78104–78146, De-
cember 2024.
URL https://proceedings.neurips.cc/paper files/paper/2024/hash/
8eb88844dafefa92a26aaec9f3acad93-Abstract-Datasets and Benchmarks Track.html.
Tarek Naous, Michael J. Ryan, Alan Ritter, and Wei Xu. Having Beer after Prayer? Measuring
Cultural Bias in Large Language Models, February 2024. URL http://arxiv.org/abs/
2305.14456. arXiv:2305.14456 [cs].
Roberto Navigli, Simone Conia, and Bj¨orn Ross. Biases in Large Language Models: Origins,
Inventory, and Discussion. Journal of Data and Information Quality, 15(2):1–21, June 2023.
ISSN 1936-1955, 1936-1963. doi: 10.1145/3597307. URL https://dl.acm.org/doi/10.
1145/3597307.
Richard Ngo, Lawrence Chan, and S¨oren Mindermann. The Alignment Problem from
a Deep Learning Perspective, March 2024.
URL http://arxiv.org/abs/2209.00626.
arXiv:2209.00626 [cs].
Team OpenAI. Introducing chatgpt, 2023a. URL https://openai.com/blog/chatgpt.
Team OpenAI. Gpt-4 technical report, March 2023b. URL https://arxiv.org/abs/2303.
08774v4.

--- Page 12 ---

Alexander Pan, Kush Bhatia, and Jacob Steinhardt. The effects of reward misspecification:
Mapping and mitigating misaligned models, 2022.
Team Qwen.
Qwen2.5: A party of foundation models, September 2024.
URL https:
//qwenlm.github.io/blog/qwen2.5/.
Michael J. Ryan, William Held, and Diyi Yang.
Unintended Impacts of LLM Align-
ment on Global Representation, February 2024. URL http://arxiv.org/abs/2402.15018.
arXiv:2402.15018 [cs].
Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, and Tatsunori
Hashimoto. Whose Opinions Do Language Models Reflect? In Proceedings of the 40th
International Conference on Machine Learning, pp. 29971–30004. PMLR, July 2023. URL
https://proceedings.mlr.press/v202/santurkar23a.html. ISSN: 2640-3498.
Yan Tao, Olga Viberg, Ryan S. Baker, and Rene F. Kizilcec. Auditing and Mitigating Cultural
Bias in LLMs, November 2023. URL http://arxiv.org/abs/2311.14096. arXiv:2311.14096
[cs].
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux,
Timoth´ee Lacroix, Baptiste Rozi`ere, Naman Goyal, Eric Hambro, Faisal Azhar, et al.
Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971,
2023.
Da Yin, Haoyi Qiu, Kung-Hsiang Huang, Kai-Wei Chang, and Nanyun Peng. SafeWorld:
Geo-Diverse Safety Alignment. Advances in Neural Information Processing Systems, 37:
128734–128768, January 2025.
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian
Min, Beichen Zhang, Junjie Zhang, Zican Dong, et al. A survey of large language models.
arXiv preprint arXiv:2303.18223, 2023.
A
Appendix
A.1
Cultural Values Survey
The six dimensions of the 24-item questionnaire are Power Distance (POW), Individual-
ism vs. Collectivism (IND), Masculinity vs. Femininity (MASC), Uncertainty Avoidance
(UAV), Long-Term Orientation vs. Short-Term Orientation (LTO), and Indulgence vs. Re-
straint (IVR). Once responses are obtained for all the items of the survey, culture scores are
calculated for each of the six dimensions using the equation:
Di = λ1(Q1 −Q2) + λ(Q3 −Q4) + Ci,
(2)
wherein there are four questions associated with each dimension, λ1 and λ2 represent
hyperparameters for calculating each dimension’s score provided by the survey creator, and
Ci is a constant used to move the scores into a desired range.
The cultural output values are all normalized to a scale between 0 and 100 to conform to the
scale of the ground truth scores. Ground truth scores, in turn, are obtained from the Hofstede
official website, where they are aggregated from valid studies 5, and for any countries whose
data was not available, ground truth scores were obtained from a third-party consultancy
based upon Hofstede’s work 6.
To distinguish countries from languages in the text and figures, languages are always given
in abbreviated form, whereas country names are written out in full.
5https://geerthofstede.com/country-comparison-bar-charts/
6https://www.theculturefactor.com/country-comparison-tool

--- Page 13 ---

Country
Language (Code)
Bangladesh
BEN
China
ZH
Egypt
AR
France
FR
Germany
DE
India
HIN
Indonesia
ID
Iran
FA
Japan
JA
S. Korea
KR
Pakistan
UR
Philippines
TG
Portugal
PT
Russia
RU
Spain
ES
Tanzania
SW
Thailand
THA
Turkey
TR
United States
EN
Vietnam
VN
Table A: Countries and their corresponding languages
POW
IND
MASC
UAV
LTO
IVR
Bangladesh
POW
IND
MASC
UAV
LTO
IVR
China
POW
IND
MASC
UAV
LTO
IVR
Egypt
POW
IND
MASC
UAV
LTO
IVR
France
POW
IND
MASC
UAV
LTO
IVR
Germany
POW
IND
MASC
UAV
LTO
IVR
India
POW
IND
MASC
UAV
LTO
IVR
Indonesia
POW
IND
MASC
UAV
LTO
IVR
Iran
POW
IND
MASC
UAV
LTO
IVR
Japan
POW
IND
MASC
UAV
LTO
IVR
Korea
POW
IND
MASC
UAV
LTO
IVR
Pakistan
POW
IND
MASC
UAV
LTO
IVR
Philippines
POW
IND
MASC
UAV
LTO
IVR
Portugal
POW
IND
MASC
UAV
LTO
IVR
Russia
POW
IND
MASC
UAV
LTO
IVR
Spain
POW
IND
MASC
UAV
LTO
IVR
Tanzania
POW
IND
MASC
UAV
LTO
IVR
Thailand
POW
IND
MASC
UAV
LTO
IVR
Turkey
POW
IND
MASC
UAV
LTO
IVR
United States
POW
IND
MASC
UAV
LTO
IVR
Vietnam
Ground Truth
GPT-3.5
GPT-4o
GPT-4
LLaMA-3
Gemini-1.5
DeepSeek
GLM-4
Qwen-7B
Qwen-32B
Qwen-72B
Figure A: Comparison of raw results for each dimension charts for all countries.
