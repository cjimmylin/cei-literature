---
title: "2025-Liu-On the Alignment of Large Language Models with Global Human Opinion - PDF Extract"
source_pdf: "2025-Liu-On the Alignment of Large Language Models with Global Human Opinion.pdf"
pages: 28
extracted_at: "2026-02-13T17:43:22.467469"
---

# PDF Extract: 2025-Liu-On the Alignment of Large Language Models with Global Human Opinion

**Source PDF:** 2025-Liu-On the Alignment of Large Language Models with Global Human Opinion.pdf
**Total Pages:** 28

---

## Content

```
--- Page 1 ---

On the Alignment of Large Language Models with Global Human Opinion
Yang Liu1, Masahiro Kaneko2, Chenhui Chu1
1Kyoto University
2MBZUAI
yangliu@nlp.ist.i.kyoto-u.ac.jp, Masahiro.Kaneko@mbzuai.ac.ae, chu@i.kyoto-u.ac.jp
Abstract
Today’s large language models (LLMs) are capable of sup-
porting multilingual scenarios, allowing users to interact with
LLMs in their native languages. When LLMs respond to sub-
jective questions posed by users, they are expected to align
with the views of specific demographic groups or historical
periods, shaped by the language in which the user interacts
with the model. Existing studies mainly focus on research-
ing the opinions represented by LLMs among demographic
groups in the United States or a few countries, lacking world-
wide country samples and studies on human opinions in dif-
ferent historical periods, as well as lacking discussion on us-
ing language to steer LLMs. Moreover, they also overlook
the potential influence of prompt language on the alignment
of LLMs’ opinions. In this study, our goal is to fill these
gaps. To this end, we create an evaluation framework based
on the World Values Survey (WVS) to systematically assess
the alignment of LLMs with human opinions across different
countries, languages, and historical periods around the world.
We find that LLMs appropriately or over-align the opinions
with only a few countries while under-aligning the opinions
with most countries. Furthermore, changing the language of
the prompt to match the language used in the questionnaire
can effectively steer LLMs to align with the opinions of the
corresponding country more effectively than existing steering
methods. At the same time, LLMs are more aligned with the
opinions of the contemporary population. To our knowledge,
our study is the first comprehensive investigation of the topic
of opinion alignment in LLMs across global, language, and
temporal dimensions. Our code and data are publicly avail-
able at https://github.com/ku-nlp/global-opinion-alignment
and https://github.com/nlply/global-opinion-alignment.
1
Introduction
Large language models (LLMs) have become crucial to
everyday decision-making and assistance (OpenAI 2023b;
Bubeck et al. 2023; Bommasani et al. 2021). Once LLMs
are deployed as products, they are inevitably asked to an-
swer subjective questions, not just objective ones (Ouyang
et al. 2022; Santurkar et al. 2023; Meister, Guestrin, and
Hashimoto 2025). From an alignment perspective, next-
token prediction during pretraining gives LLMs a statisti-
cal prior over human opinions (Radford et al. 2019; Brown
et al. 2020), while subsequent alignment stages, such as in-
struction tuning (Wei et al. 2021; Sanh et al. 2021) and pref-
erence optimization (Christiano et al. 2017; Ouyang et al.
Question:
Do you agree that one of 
your main goals in life 
has been to make your 
parents proud?
Choices:
1. Strongly agree
2. Agree
3. Disagree
4. Strongly disagree
Survey
opinion 
distribution
LLM
United States
Chile
Myanmar
Egypt
…
Good
Alignment
Bad
Alignment
Figure 1: An example of our main idea. When asking the
LLM a subjective question, is the LLM’s opinion distribu-
tion closer to specific countries’ opinion distributions?
2022), shape this prior toward the opinions in their pref-
erence datasets, which are typically annotated by annota-
tors from various countries, speaking diverse languages, and
across different ages (Mason and Suri 2012).
Existing study mainly focuses on exploring opinion align-
ment between LLMs and demographic groups in the United
States (Santurkar et al. 2023). Durmus et al. (2023) ex-
pand Santurkar et al. (2023)’s study to explore the alignment
between the LLM Claude and other countries, and they fur-
ther find that translating the questions into Russian, Chinese,
and Turkish fails to improve the alignment between the LLM
and the language speakers. A crucial challenge to previous
studies is that the LLMs’ opinion distribution is expressed as
the next token log probabilities from the model, which suf-
fers from a mis-calibration issue and requires the LLMs to
be able to output logits (Meister, Guestrin, and Hashimoto
2025). Therefore, in this study, we adopt the verbalized dis-
tribution method to investigate the alignment between LLMs
and human opinions. We expand to investigate seven state-
of-the-art LLMs and eight languages covering 10 countries
to validate the effectiveness of language steering. In addi-
tion, we innovatively explore the alignment of LLMs and
human opinions in the temporal dimension. Therefore, our
study covers the alignment of LLMs with human opinions
in three dimensions: global, languages, and temporal.
The key question we focus on is illustrated in Figure 1:
when asking the LLMs a subjective question, is the LLM’s
opinion distribution closer to specific countries’ opinion dis-
tributions? If an LLM systematically reflects the opinions of
arXiv:2509.01418v2  [cs.CL]  19 Nov 2025

--- Page 2 ---

specific countries, this may lead to unexpected country dom-
inance or misalignment in international applications (Bender
et al. 2021; AlKhamissi et al. 2024; Sukiennik et al. 2025).
Additionally, analyzing the opinions reflected by the LLMs
can help improve the transparency and accountability of the
LLMs, allowing developers to better assess and mitigate po-
tential geopolitical or ethical risks. Finally, this study can
provide a foundation for building more human opinion adap-
tive or neutral AI systems that respect diverse views in the
globally interconnected world.
The World Values Survey (WVS; Haerpfer et al. 2022),
a comprehensive global research program, systematically
collects human opinions on a wide range of topics, includ-
ing politics, religion, and ethics. The standardized question-
naire design of the WVS allows for consistent comparisons
of opinions across countries, languages, and historical pe-
riods. In addition, the survey covers highly subjective and
value-oriented questions, which align well with the types
of prompts used to probe LLMs’ opinions. By using WVS
as the benchmark, in this study, we focus on the follow-
ing research questions: RQ1: Do LLMs appropriately align
with the opinions of different countries? RQ2: Can language
steer LLMs to express opinions closer to language speak-
ers? RQ3: Which human historical period’s opinions are re-
flected in LLMs’ responses?
Our work makes four main contributions: 1) We system-
atically investigate human opinion alignment in global, lan-
guage, and temporal dimensions with LLMs; 2) We reveal
that current LLMs tend to align with the opinions of English-
or Spanish-speaking countries such as the United States,
Canada, and Chile, but under-align with the opinions of
information-regulated or non-Latin-speaking countries such
as Myanmar and Egypt; 3) We employ language steering on
eight languages, which is effective in over 82% of the 240
cases (3 baselines1 × 8 models × 10 countries) in our exper-
iments; 4) We evaluate the alignment of LLMs with human
opinions in the temporal dimension, revealing that LLMs are
most aligned with contemporary human opinions.
2
The World Values Survey
In this section, we explain why WVS is suitable for our study
from three dimensions: global, language, and temporal. Fur-
ther details are provided in Appendix A.
Global Dimension
The WVS covers highly subjective
and value-oriented questions, which align well with the
types of prompts used to probe LLMs’ opinions. The lat-
est wave covers survey data from 66 countries and regions,
enabling us to compare the alignment of LLMs with differ-
ent countries’ human opinions. In addition, each country has
more than 1,000 human questionnaire results, which ensures
that the survey data reflects real human behavior to some ex-
tent. These features make it possible for us to study RQ1.
Language Dimension
The WVS questionnaire was trans-
lated into all languages which serve as the first language for
1The three baselines include no steering, persona steering, and
few-shot steering.
15% (or more) of the population. For countries that partic-
ipated in previous waves of the WVS, translation for the
replicated items is used from the previous wave question-
naires to minimize bias during overtime comparison of an-
swer distributions.2 According to our statistics, the latest
wave provided more than 50 language translations, ensuring
that the questionnaire covers languages supported by LLMs
and providing linguistic diversity for RQ2.
Temporal Dimension
Since 1981, the WVS has con-
ducted seven waves of globally representative surveys. The
WVS maintains functional consistency across most ques-
tions in all waves, allowing us to study long-term trends of
alignment between LLMs and human opinions across differ-
ent waves, providing temporal data support for our RQ3.
3
Experiment Settings
In this section, we introduce the experiment settings. More
details such as the question filter rules and the complete
country list (§3.1), the full prompts (§3.3), and more details
of the distribution expression methods (§3.4) are provided in
Appendix B.
3.1
Dataset
In RQ1, we conduct a question filter process on the En-
glish version of wave 7, which includes survey data from
66 countries, to filter out questions that are not suitable for
this study. For example, questions that require actual expe-
rience, objectivity, etc. After this filter process, we get 144
opinion-related questions. In RQ2, we used the same 144
questions and collected them from other language versions
of the questionnaire. In RQ3, to ensure a certain number of
common questions, we chose to analyze WVS’s data from
wave 5, wave 6, and wave 7.3 Each wave corresponds to a
historical questionnaire version. We organized each English
version from wave 5 to 7 and then selected questions that are
common in all three waves. We obtained 75 opinion-related
questions that are shared across all three waves.
3.2
Models
We experiment with seven instruction-tuned multilingual
LLMs: Aya-23-35B (Aryabumi et al. 2024), Llama3-70B-
Instruct (AI@Meta 2024), Qwen2.5-72B-Instruct (Team
2024), GPT-3.5-Turbo (gpt-3.5-turbo-0125; Ope-
nAI
2023a),
GPT-4
(gpt-4-0613;
Achiam
et
al.
2023),
GPT-5
(gpt-5;
OpenAI
2025),
DeepSeek-
V3
(DeepSeek-V3-0324;
Liu
et
al.
2024),
and
DeepSeek-R1 (DeepSeek-R1-0528; Guo et al. 2025).
For open-weight community models, we select the largest
publicly released weights in each series. For commercial
LLMs, we include OpenAI’s GPT-3.5-Turbo, GPT-4, and
GPT-5 (closed-source models), as well as DeepSeek-V3 and
DeepSeek-R1, noting that DeepSeek releases open-weight
models under a permissive license.
2https://www.worldvaluessurvey.org/wvs.jsp
3Our statistical result indicates that, when wave 4 is taken into
account, there are only 48 common questions.

--- Page 3 ---

3.3
Prompts
As the instruction fine-tuned LLMs use “task instructions
+ examples” as input during training, it is easier for them
to follow the requirements of the prompt and output con-
tent in the required format. We refer to Meister, Guestrin,
and Hashimoto (2025) to control the LLMs’ output dis-
tribution in JSON format (e.g., {1: 31%, 2: 4%, 3:
30%, 4: 35%}) by providing five few-shot examples.
3.4
Distribution Expression Methods
LLMs’ opinion distribution
Being able to accurately ex-
press LLMs’ opinion distributions is a precondition of our
study. Meister, Guestrin, and Hashimoto (2025)’s work com-
pares three distribution expression methods: model log-
probabilities, sequence of tokens, and verbalized distribu-
tion. Their analysis reveals that verbalized distribution out-
performs the other two methods. Therefore, we use ver-
balized distribution to represent the opinion distribution
DM(q) of the LLM M on answering question q.
Human opinion distribution
We calculate human opin-
ion distributions from the statistical data of the WVS, which
contain more than 1,000 pieces of human data for each sur-
veyed country. The distribution of the country c ∈C answers
to the question q ∈Q with |N| options can be denoted as
Dc(q) = {Dc,n|n ∈N}. Specifically, Dc,n is as follows:
Dc,n =
|P(n)
c
|
P
i∈N |P(i)
c |
(1)
where |P(n)
c
| denotes the number of people in the country c
who choose option n when answering question q.
3.5
Alignment Metrics
Measuring the alignment between the LLM’s opinion dis-
tribution DM(q) and human opinion distribution Dc(q) re-
quires considering the order of the options in these two dis-
tributions. Moreover, it is desirable for the metrics to range
from 0 to 1. In this paper, we use the alignment proposed
by Santurkar et al. (2023) as our metric. This metric is used
to measure the alignment score between distributions DM
and Dc. The formal definition of alignment is as follows:
A(DM, Dc; Q) =
1
|Q|
X
q∈Q

1 −WD(DM(q), Dc(q))
|N| −1

(2)
where Q is the question set and |N| is the number of op-
tions of the question q. The denominator |N| −1 serves to
normalize the Wasserstein distance (WD)4 so that the value
of the metric falls between 0 and 1. The metric’s value of 1
indicates that the two distributions are perfectly matched.
4
Global Opinion Alignment (RQ1)
In this section, we calculate the alignment score between
LLMs’ opinion distributions and human opinion distribu-
tions in wave 7. Then, we discuss the alignment of LLMs
4https://en.wikipedia.org/wiki/Wasserstein metric
with human opinion at three levels: 1) Model level: Which
LLM most matches the human opinion distribution? 2)
Country level: Which countries’ opinions are aligned by
LLMs? 3) Alignment difference level: If we take the av-
erage human opinion distribution as a possible goal, how do
LLMs and this average distribution differ in terms of align-
ment with a country?
4.1
Model Level
As shown in Figure 2(a), we demonstrate the overall
alignment scores of LLMs’ opinion distributions with hu-
man opinion distributions. The experimental results show
that GPT-5 achieves the highest average alignment score
(0.8621). Meanwhile, the average alignment scores of
Llama3, Qwen2.5, GPT-4, DeepSeek-V3, and DeepSeek-R1
closely follow those of GPT-5, also demonstrating high hu-
man opinion alignment performance. In contrast, Aya-23-
35B and GPT-3.5-Turbo, as earlier generations of instruc-
tion fine-tuning LLMs, have lower average alignment scores
and a number of countries with low tail scores; the relative
lack of multilingual long-tail coverage may be part of the
reason. In addition, the alignment scores of each LLM differ
significantly across countries, indicating that no single LLM
can simultaneously align with all countries’ opinions.
4.2
Country Level
Next, we move our attention to the question of which coun-
tries LLMs are more aligned with. Figure 2(b) shows the
five countries’ opinion distributions that are most and least
aligned with DeepSeek-R1’ opinion distributions.5 We can
see that DeepSeek-R1 has the highest average alignment
scores with countries such as the United States and Chile
(0.8972 and 0.8948), and relatively low scores with coun-
tries such as Egypt and Myanmar (0.7855 and 0.7881). No-
tably, the standard deviation of the alignment scores in the
high-alignment countries is significantly lower than that in
the low-alignment countries, indicating that DeepSeek-R1 is
both approximate and robust in the high-alignment coun-
tries. In contrast, low-alignment countries suffer from both
systematic misalignment and high standard deviations. This
may be due to the widespread presence of English and Span-
ish content,6 which makes the LLMs highly homogeneous
with the dominant views of the United States, Canada, and
Chile societies, while low-aligned countries tend to be in
non-Latin-speaking environments, which results in a severe
scarcity of their political and cultural alignments in the train-
ing set. In addition, the alignment with Slovakia and Mon-
golia is surprisingly high, which implies that the LLM may
have learned indirect social signals to Slovakia and Mon-
golia by borrowing from regional media or cross-language
interconnected corpora, suggesting that estimating cultural
alignment purely in terms of corpus size is still insufficient.
It is worth noting that although DeepSeek-R1 supports Chi-
nese well, its opinion distribution is not highly aligned with
China. In fact, as we show in Appendix D, DeepSeek-R1
5Results for all LLMs are available in Appendix D.1, and the
complete list of countries are provided in Appendix C.
6https://en.wikipedia.org/wiki/Languages used on the Internet

--- Page 4 ---

Aya23
Llama3
Qwen2.5
GPT-3.5
GPT-4
GPT-5
DS-V3
DS-R1
0.750
0.775
0.800
0.825
0.850
0.875
0.900
0.925
Alignment Score
(a) The alignment score of LLMs with each country.
0.65
0.70
0.75
0.80
0.85
0.90
0.95
United States
Chile
Slovakia
Mongolia
Northern Ireland
Canada
China
Jordan
Bangladesh
Libya
Myanmar
Egypt
***
***
***
***
***
***
**
***
***
***
***
***
(b) The first and last 6 countries or regions.
0.800
0.825
0.850
0.875
0.900
0.925
Alignment Score with Average Humans' Opinions
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with DeepSeek-R1
Andorra
Argentina
Australia
Bangladesh
Bolivia
Canada
China
Cyprus
Czech Republic
Egypt
Germany
Great Britain
Hong Kong
Iran
Jordan
Japan
Kazakhstan
Kyrgyzstan
Libya
Mexico
Myanmar
Netherlands
New Zealand
Nigeria
Puerto Rico
Romania
Slovakia
South Korea
Tunisia
United States
Uzbekistan
Viet Nam
Zimbabwe
y = x
(c) DeepSeek-R1 vs. Human
Figure 2: The overall results of RQ1. (a) The alignment score of LLMs with each country, where each point represents a country
and the black line represents the average alignment score of all countries. “DS” is the abbreviation for “DeepSeek.” (b) The
first and last 6 countries ranked by their alignment scores with DeepSeek-R1’s opinion distributions, the point represents the
average alignment score of the country on all questions and the line represents the standard deviation. *** denotes p-value <
0.001 (t-test). (c) The relationship of different countries to DeepSeek-R1’s opinion distribution and the average human opinion
distribution alignment scores. For visibility, we hide some countries. See Appendix D.2 for the full version.
exhibits a similar pattern to other LLMs (such as GPT-4) in
terms of country’s opinion alignment.
4.3
Alignment Difference Level
It is impossible to align LLMs with all countries at the same
time due to the diversity of cultures. LLMs aligning with
the average human opinion distribution is a plausible so-
lution, and we hypothesize that it is the ideal goal. Then,
we take the average human opinion distribution as the base-
line to investigate how well LLMs fit the different countries’
opinions. Figure 2(c) illustrates the relationship of different
countries to the DeepSeek-R1’s opinion distribution and the
average human opinion distribution alignment scores. Con-
sider y = x as the reference line: points that fall on the
line indicate that the LLM appropriately align with the
country’s opinions, points that fall above the line indicate
that the LLM over-align with the country’s opinions, and
points that fall below the line indicate under-alignment.
We can see that DeepSeek-R1 most appropriately aligns
with the United States’ opinions, as well as over-aligns
with some developed countries’ opinions. It is worth noting
that although DeepSeek-R1 is relatively close to Chile, Slo-
vakia, and Mongolia’s opinion distributions (Figure 2(b)),
when compared to the average human opinion distribution,
DeepSeek-R1 under-aligns with these countries even more
(Figure 2(c)). Overall, DeepSeek-R1 appropriately aligns or
over-aligns with the views of a few countries, while under-
aligning with the views of most countries, especially devel-
oping countries such as Myanmar, Egypt, and Libya.
5
Steerability of Language (RQ2)
Baselines
Steerability refers to the ability of LLMs to ad-
just and align with the opinion of a target demographic
group (Meister, Guestrin, and Hashimoto 2025). Existing
steering methods involve prepending additional context to
the prompt describing the group we want the model to em-
ulate. We consider the following steering methods as our
baselines.
• Persona Steering operates by inserting a concise per-
sona description into the original task prompt, prompting
the LLM to first “locate” itself as a member of a specific
group and thereby explicitly emulate that group’s opin-
ion orientation. In this paper, we follow Santurkar et al.
(2023) and (Meister, Guestrin, and Hashimoto 2025), in
which the LLM is instructed to pretend to be a member
of the target country.
• Few Shot Steering (Meister, Guestrin, and Hashimoto
2025) provides the persona steering setting while also
giving five in-context examples of the real group opinion
distributions and asking the LLM to emulate the group’s
responses. This setting is representative when we already
have the opinion distributions of the target group.
Method
Language affects the way we think (Turner 2000),
that is, speakers of different languages end up with different
conceptual structures, and these differences can affect their
worldview (Plebe and Vivian 2015). However, it is unclear
how language affects the views of LLMs. In this section, we
validate the language steering, which enables an LLM to
represent the opinions of speakers of language l by changing
the language of the prompt from English to non-English lan-
guage l. Specifically, for the task instructions, we translate
them using GPT-4 and manually check the accuracy of the
translated versions; for the in-context examples, we obtain
the translations from the corresponding translated versions
of the WVS questionnaires. Unlike previous work (Durmus
et al. 2023) that only evaluates three languages, uses log
probabilities of one LLM, and validates the language steer-
ing itself, we evaluate eight languages, use the verbalized
distribution of seven LLMs, and validate the effect of com-
bining the language steering with other steering methods.
Because WVS provides a multilingual translated version
of the survey questionnaire for countries that use multi-
ple languages (e.g., Singapore uses Chinese, English, and

--- Page 5 ---

Method
Aya23
Llama3
Qwen2.5
GPT-3.5
GPT-4
GPT-5
DS-V3
DS-R1
AVG.
China
No Steering (En.)
0.8038
0.8235
0.8273
0.7816
0.8152
0.8348
0.7952
0.8174
0.8124
+Language Steering (Zh.)
0.8103
0.8308
0.8439
0.7976
0.8526∗
0.8601
0.8471∗∗
0.8498∗
0.8365∗∗∗
Persona Steering (En.)
0.8154
0.8439
0.8316
0.7846
0.8247
0.8953∗∗∗
0.8278∗
0.8625∗∗
0.8357∗∗∗
+Language Steering (Zh.)
0.8216
0.8553∗
0.8629∗
0.8088
0.8718∗∗∗
0.8979∗∗∗
0.8732∗∗∗
0.8828∗∗∗
0.8593∗∗∗
Few-shot Steering (En.)
0.8115
0.8666∗∗
0.8596
0.8149
0.8629∗∗
0.8996∗∗∗
0.8775∗∗∗
0.8884∗∗∗
0.8601∗∗∗
+Language Steering (Zh.)
0.8469∗∗
0.8652∗∗
0.8838∗∗∗
0.8345∗∗
0.8961∗∗∗
0.9041∗∗∗
0.8884∗∗∗
0.8976∗∗∗
0.8771∗∗∗
Germany
No Steering (En.)
0.8175
0.8441
0.8541
0.7993
0.8468
0.8826
0.8280
0.8543
0.8408
+Language Steering (De.)
0.8445∗
0.8494
0.8815∗∗
0.8140
0.8765∗∗
0.8801
0.8689∗∗
0.8715
0.8608∗∗
Persona Steering (En.)
0.8081
0.8510
0.8596
0.8193
0.8736∗
0.9129∗∗∗
0.8731∗∗∗
0.8879∗∗∗
0.8607∗∗∗
+Language Steering (De.)
0.8482∗
0.8507
0.8904∗∗∗
0.8250
0.8938∗∗∗
0.9130∗∗∗
0.8905∗∗∗
0.9053∗∗∗
0.8771∗∗∗
Few-shot Steering (En.)
0.8345
0.8348
0.8619
0.8352∗
0.8670
0.8983
0.8709∗∗∗
0.8581
0.8576∗∗∗
+Language Steering (De.)
0.8661∗∗∗
0.8683
0.8916∗∗∗
0.8476∗∗
0.9097∗∗∗
0.9219∗∗∗
0.9072∗∗∗
0.9103∗∗∗
0.8903∗∗∗
Table 1: Culture representation scores for China and Germany under different steering methods for LLMs. The content in “()”
is to indicate the language being used, where “En.” denotes English, “Zh.” denotes Chinese, and “De.” denotes German. In
all cases, the language of our inputs (task instruction, few-shot examples, and question) always keeps the same. Moreover, the
significance is assessed using the t-test: * denotes p-value < 0.05, ** denotes p-value < 0.01, and *** denotes p-value < 0.001.
Malay; respondents may see the questionnaire in both En-
glish and Malay), the survey results from these countries
may not reflect the opinions of single-language speakers.
Therefore, in order to quantitatively analyze the effect of
language steering, we must avoid respondents using mul-
tilingual questionnaires. The languages and countries we
choose to investigate must satisfy the following conditions:
1) the country must be surveyed by WVS using a single lan-
guage; and 2) the language must be supported by the LLM.
After our selection, our experiments cover Spanish, Chi-
nese, Japanese, Korean, German, Russian, Vietnamese, and
Portuguese. As WVS covers survey data from 12 Spanish-
speaking countries, we select three countries, Argentina,
Chile, and Uruguay, to validate language steering. For other
languages, we select one country for each language.
Effectiveness of Steering
Table 1 shows the alignment
scores for China and Germany under different steering meth-
ods for LLMs.7 We show these two countries (or languages)
due to their representation of non-Latin (Chinese) and Latin
writing systems (German), respectively, forming a striking
contrast in terms of language families and verifying the uni-
versality of the steering methods. We can see that the base-
line methods persona steering and few-shot steering show a
certain steering ability on all countries compared to no steer-
ing. In general, few-shot steering exhibits higher steering
ability than persona steering, and our findings are consis-
tent with existing studies (Meister, Guestrin, and Hashimoto
2025; Studdiford et al. 2025). Moreover, “few-shot + lan-
guage steering” achieves the highest alignment scores on
both countries, which indicates the effectiveness of language
in steering LLMs to emulate the opinions of language speak-
ers. Although persona steering can be inaccurate (Meister,
Guestrin, and Hashimoto 2025), “persona + language steer-
ing” also yields promising steering ability on China and
7The results of other languages are available in Appendix E.
Germany. In addition, among the LLMs tested, DeepSeek-
R1 exhibits the strongest response to the composite strat-
egy, reflecting its greater ability to understand the countries
we tested. Overall, language steering is effective in steer-
ing LLMs to emulate country-specific opinions. This result
implicates that while chasing higher benchmark scores may
suggest using a language other than the target one (Kaneko,
Aji, and Baldwin 2025), for opinion-oriented tasks, sticking
to the target language can yield better alignment. Therefore,
whenever we consider deploying other languages, we must
pay careful attention to value alignment and similar factors.
6
Temporal Opinion Alignment (RQ3)
Human cognition has a social historical character (Berger
and Luckmann 2016), which means that human cognition is
not static; it is constantly being reshaped as historical condi-
tions evolve (Vygotsky 2012; Mannheim 2013). Therefore,
it is important to know whether LLMs reflect contemporary
human opinions. In this study, we suppose that it is desirable
for LLMs to reflect contemporary human opinions. Next, we
will show the representativeness of LLMs with human opin-
ion distributions in the temporal dimension.
Method
As shown in the results of Figure 2(c), the LLM
is under-aligned with most countries’ opinions. We there-
fore consider which countries are well aligned by the LLM
for comparison. Formally, we use the following equation to
filter the countries for comparison:
C∗= { c ∈C |
A(c)
M −A(c)
avg
 < τ }.
(3)
where A(c)
M denotes the alignment score between the LLM’s
opinion distribution and that of country c. Likewise, A(c)
avg is
the alignment score between the average human opinion dis-
tribution and that of country c. The margin τ is the threshold,
which we set to 0.02 to ensure that we can filter out at least

--- Page 6 ---

Wave 5
Wave 6
Wave 7
0.80
0.85
0.90
GPT-5
Wave 5
Wave 6
Wave 7
0.80
0.85
0.90
DeepSeek-R1
Figure 3: The trend of the average alignment scores of GPT-
5 and DeepSeek-R1 with countries filtered using Eq. (3)
across waves. The shaded area indicates the standard devia-
tion of the alignment scores at the current wave.
five countries that are well aligned by LLMs. We refer read-
ers to Appendix F for more details on filtering and filtered
countries.
Results
Figure 3 illustrates the trend of the average align-
ment scores of GPT-5 and DeepSeek-R1 across waves. We
can see that LLMs most align with the latest wave of hu-
man opinions. One reason may be due to the fact that most
of the human feedback in the fine-tuning of LLMs comes
from contemporary annotators, whose ethical and social ori-
entations are more in line with recent public opinions. The
models are rewarded for emulating these behaviors. Another
reason may be due to the development of mobile internet
and social media, which provide more accessible data than
in the past. In addition, the standard deviation reflects an
LLM’s coverage degree of the represented opinions. A lower
standard deviation indicates a better coverage degree of the
opinions. Therefore, LLMs achieve better coverage of hu-
man opinions in the latest wave and poorer coverage of hu-
man opinions in earlier waves. This further indicates that the
alignment of LLMs is influenced by contemporary annota-
tors’ human feedback. In contrast, it implies that there may
be challenges for LLMs to align to earlier human opinions.
The reason is that it is more difficult to access earlier cus-
tomized human feedback data.
7
Discussion
7.1
Alignment of Human Opinions across
Countries
To understand the alignment between different countries’
opinions, we show the alignment scores between countries
and countries in Figure 4. Similar to Figure 2(b), we plot the
first and last 6 countries ranked by their alignment scores
with DeepSeek-R1’s opinion distributions. For comparison,
we also show the alignment scores between the countries
and DeepSeek-R1 in the results. More results can be found
in Appendix G.1. The alignment scores of opinion distri-
butions among the first 6 ranking countries are generally
high, indicating significant similarity in their views. In con-
trast, the alignment scores among the last 6 ranking coun-
tries show relative differences. For example, Jordan, Libya,
and Egypt have high alignment scores with each other,
while Bangladesh, China, and Myanmar have low align-
ment scores with other countries. Meanwhile, the alignment
scores between the first and last 6 ranking countries are gen-
United States
Chile
Slovakia
Mongolia
Northern Ireland
Canada
China
Jordan
Bangladesh
Libya
Myanmar
Egypt
DS-R1 (LLM)
United States
Chile
Slovakia
Mongolia
Northern Ireland
Canada
China
Jordan
Bangladesh
Libya
Myanmar
Egypt
DS-R1 (LLM)
0.75
0.80
0.85
0.90
0.95
1.00
Figure 4: Alignment scores among different countries. For
comparison, we also show the alignment scores between the
countries and DeepSeek-R1 (DS-R1).
erally low. Furthermore, by calculating the alignment scores
between DeepSeek-R1 and each country, we find that de-
spite some heterogeneity in alignment scores among the first
6 ranking countries, DeepSeek-R1’s alignment scores with
these countries are surprisingly consistent. This pattern sug-
gests that the model captures an “average” cross-country
view rather than aligning specifically to individual countries,
revealing a lack of country-specific sensitivity in the align-
ment of opinion distributions.
7.2
Internal Consistency of LLMs
In order to investigate whether LLMs hold self-contradictory
opinions when answering questions, we conduct a closer
look at the internal consistency of LLMs. Concretely, we
manually select four questions about gender fairness (agree
or disagree that men are superior to women), four questions
about atheism (believe or disbelieve in theism), and two
questions about democracy (important or not important that
democracy).8 Questions with the same topic reflect the same
logic of opinion judgment. In our experiments, we consider
the options “Strong agree” and “Agree,” which both express
positive attitudes, to be consistent opinions. For options re-
lated to degree (e.g., from “1. Not at all important” to “10.
Absolutely important”), we group options 1 to 5 and options
6 to 10 as consistent opinion groups, respectively.
We use the internal consistency rate, which is the ratio
of answers within the same opinion group, as the evalua-
tion measure. If the answers to a set of questions are [1, 1,
2, 1], the internal consistency rate is 75%. The experimen-
tal results show that on the topic of gender fairness, all the
LLMs remain at a 100% internal consistency rate. However,
GPT-3.5-Turbo shows only 50% internal consistency on the
topics of atheism and democracy, in contrast to other LLMs,
which maintain full consistency. This suggests that, relative
8A complete list is provided in Appendix G.2.

--- Page 7 ---

Models
Order
#few-shot
Prob.
Aya23
0.9660
0.9893
0.9815
Llama3
0.9927
0.9964
0.9933
Qwen2.5
0.9928
0.9928
0.9973
GPT-3.5
0.9852
0.9810
0.9736
GPT-4
0.9925
0.9783
0.9902
GPT-5
0.9973
0.9968
0.9980
DeepSeek-V3
0.9895
0.9805
0.9881
DeepSeek-R1
0.9885
0.9861
0.9924
Table 2: Pearson’s r between the default and sensitivity test
results. Here, the default result means the alignment scores
between LLMs’ opinion distributions and those of different
countries under default prompts. The sensitivity test result
means the alignment scores between LLMs’ opinion distri-
butions and those of different countries under sensitivity test
prompts. Order means shuffle the input question’s options,
#few-shot means limit the number of the few-shot examples
from five to three, and Prob. means change the probability
distribution of the few-shot examples. Note: The p-values
for all results are less than 0.001.
to other LLMs, GPT-3.5-Turbo not only poorly aligns with
human opinions (§4), but also lacks internal consistency.
7.3
Sensitivity of LLMs
We acknowledge that current LLMs are very sensitive to
the prompt format (Zhuo et al. 2024). Inspired by Santurkar
et al. (2023), we test the prompt sensitivity of the LLMs used
in our experiments against the following factors:
• The order in which the question options are presented to
the model;
• The few-shot examples (the number of the few-shot ex-
amples and the probability distribution of the few-shot
examples).
We employ the Pearson’s r of the alignment scores of dif-
ferent sensitivity test prompts for evaluating prompt sensi-
tivity. As shown in Table 2, despite changing prompts, the
results output by LLMs still maintain a significantly high
Pearson’s r, and the p-value is less than 0.001. Moreover,
Appendix G.3, G.4, G.5 and G.6 provide more results and
discussions.
8
Related Work
Human Opinion and Culture.
Culture can be defined as
the pattern of thinking, feeling, and reacting, distinguishing
human groups (Wallace and Fogelson 1961; Shweder et al.
2007; Cao et al. 2023). Human opinions are the beliefs, pref-
erences, and judgments held by individuals, and are deeply
influenced by cultural backgrounds (Peterson 2003; Markus
and Kitayama 2014). Culture provides people with a shared
framework through which they interpret experiences, inter-
nalize norms, and express their opinions (Geertz 2017). It
is challenging to align the opinions of human societies with
different cultural backgrounds (Hall 1976).
Culture in LLMs.
Previous studies have shown that
LLMs exhibit cultural challenges similar to those found in
human society (Li et al. 2024). Cecilia Liu et al. (2024)
pointed out that there is a cultural gap when using LLMs,
especially when dealing with content translated from other
languages. After that, Masoud et al. (2025) demonstrated
that GPT-4 exhibits remarkable capabilities in adapting to
these cultural gaps, particularly in the Chinese context. Fur-
thermore, Wang et al. (2024) showed that LLMs have cul-
tural dominance issues because they are mainly trained us-
ing English data. However, recent study (Meister, Guestrin,
and Hashimoto 2025) has challenged the existing use of
LLMs to emulate opinion distributions, proving that LLMs
are more accurate when describing opinion distributions.
Therefore, one technical difference from existing studies is
that we deployed this method of describing opinion distribu-
tion (known as verbalized distribution).
Opinion of LLMs.
LLMs often respond to subjective
questions in a way that implicitly favors certain human
groups. Early study (Santurkar et al. 2023) quantified the dif-
ferences between LLMs’ predicted distributions of response
options and human distributions based on surveys. Meister,
Guestrin, and Hashimoto (2025) expanded the assessment
scope to multiple demographic dimensions and compared
different distribution expressions (model log-probability, se-
quence of tokens, and verbalized distribution). Building on
this research direction, this study expands the scope from a
few countries to a truly worldwide country sample and ex-
plicitly introduces the temporal dimension.
Steering Methods.
To enable LLMs to emulate specific
groups, previous studies (Meister, Guestrin, and Hashimoto
2025) have explored persona and few-shot steering. How-
ever, persona steering is not always accurate, leading to un-
desirable effects such as stereotypes and exacerbated polar-
ization (Perez et al. 2023; Cheng, Durmus, and Jurafsky
2023; Wang, Morgenstern, and Dickerson 2025). We fur-
ther expanded on these two methods and proposed language
steering: changing the language of the prompt can signif-
icantly improve alignment with the opinion distribution of
the corresponding country, indicating that language itself, as
an alignment cue, can drive opinion alignment.
9
Conclusion
In this paper, we propose a framework to investigate the
global human opinion alignment of LLMs using the WVS
questionnaires and data. We manually filter the 259 ques-
tions in the WVS questionnaires across multiple language
versions and historical periods to build our dataset. Through
experimenting with LLMs on our data, our main findings
are as follows: 1) LLMs only appropriately align with a
few countries, while under-aligning with most countries. 2)
Language can significantly steer LLMs to emulate country-
specific opinions. 3) LLMs most align with the contempo-
rary human opinions. Our study also discusses various as-
pects of LLMs, such as internal consistency and sensitivity
of LLMs. This paper will provide insights for studies related
to the value alignment of LLMs.

--- Page 8 ---

Acknowledgments
We thank the reviewers for their valuable feedback. This
work was supported by JST BOOST, Grant Number JP-
MJBS2407.
References
Achiam, J.; Adler, S.; Agarwal, S.; Ahmad, L.; Akkaya, I.;
Aleman, F. L.; Almeida, D.; Altenschmidt, J.; Altman, S.;
Anadkat, S.; et al. 2023.
Gpt-4 technical report.
arXiv
preprint arXiv:2303.08774.
AI@Meta. 2024. Llama 3 Model Card.
AlKhamissi, B.; ElNokrashy, M.; Alkhamissi, M.; and Diab,
M. 2024. Investigating Cultural Alignment of Large Lan-
guage Models. In Ku, L.-W.; Martins, A.; and Srikumar,
V., eds., Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long
Papers), 12404–12422. Bangkok, Thailand: Association for
Computational Linguistics.
Aryabumi, V.; Dang, J.; Talupuru, D.; Dash, S.; Cairuz, D.;
Lin, H.; Venkitesh, B.; Smith, M.; Campos, J. A.; Tan, Y. C.;
et al. 2024. Aya 23: Open weight releases to further multi-
lingual progress. arXiv preprint arXiv:2405.15032.
Bender, E. M.; Gebru, T.; McMillan-Major, A.; and
Shmitchell, S. 2021.
On the dangers of stochastic par-
rots: Can language models be too big? In Proceedings of
the 2021 ACM conference on fairness, accountability, and
transparency, 610–623.
Berger, P.; and Luckmann, T. 2016. The social construction
of reality. In Social theory re-wired, 110–122. Routledge.
Bommasani, R.; Creel, K. A.; Kumar, A.; Jurafsky, D.; and
Liang, P. S. 2022. Picking on the Same Person: Does Algo-
rithmic Monoculture lead to Outcome Homogenization? In
Koyejo, S.; Mohamed, S.; Agarwal, A.; Belgrave, D.; Cho,
K.; and Oh, A., eds., Advances in Neural Information Pro-
cessing Systems, volume 35, 3663–3678. Curran Associates,
Inc.
Bommasani, R.; Hudson, D. A.; Adeli, E.; Altman, R.;
Arora, S.; von Arx, S.; Bernstein, M. S.; Bohg, J.; Bosselut,
A.; Brunskill, E.; et al. 2021. On the opportunities and risks
of foundation models. arXiv preprint arXiv:2108.07258.
Brown, T.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J. D.;
Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; Askell,
A.; et al. 2020. Language models are few-shot learners. Ad-
vances in neural information processing systems, 33: 1877–
1901.
Bubeck, S.; Chandrasekaran, V.; Eldan, R.; Gehrke, J.;
Horvitz, E.; Kamar, E.; Lee, P.; Lee, Y. T.; Li, Y.; Lundberg,
S.; et al. 2023. Sparks of artificial general intelligence: Early
experiments with gpt-4. arXiv preprint arXiv:2303.12712.
Cao, Y.; Zhou, L.; Lee, S.; Cabello, L.; Chen, M.; and
Hershcovich, D. 2023.
Assessing Cross-Cultural Align-
ment between ChatGPT and Human Societies: An Empirical
Study. In Dev, S.; Prabhakaran, V.; Adelani, D. I.; Hovy,
D.; and Benotti, L., eds., Proceedings of the First Work-
shop on Cross-Cultural Considerations in NLP (C3NLP),
53–67. Dubrovnik, Croatia: Association for Computational
Linguistics.
Cecilia Liu, C.; Koto, F.; Baldwin, T.; and Gurevych, I. 2024.
Are Multilingual LLMs Culturally-Diverse Reasoners? An
Investigation into Multicultural Proverbs and Sayings. In
Duh, K.; Gomez, H.; and Bethard, S., eds., Proceedings
of the 2024 Conference of the North American Chapter of
the Association for Computational Linguistics: Human Lan-
guage Technologies (Volume 1: Long Papers), 2016–2039.
Mexico City, Mexico: Association for Computational Lin-
guistics.
Cheng, M.; Durmus, E.; and Jurafsky, D. 2023. Marked Per-
sonas: Using Natural Language Prompts to Measure Stereo-
types in Language Models. In Rogers, A.; Boyd-Graber, J.;
and Okazaki, N., eds., Proceedings of the 61st Annual Meet-
ing of the Association for Computational Linguistics (Vol-
ume 1: Long Papers), 1504–1532. Toronto, Canada: Associ-
ation for Computational Linguistics.
Christiano, P. F.; Leike, J.; Brown, T.; Martic, M.; Legg, S.;
and Amodei, D. 2017. Deep reinforcement learning from
human preferences.
Advances in neural information pro-
cessing systems, 30.
Durmus, E.; Nguyen, K.; Liao, T.; Schiefer, N.; Askell, A.;
Bakhtin, A.; Chen, C.; Hatfield-Dodds, Z.; Hernandez, D.;
Joseph, N.; Lovitt, L.; McCandlish, S.; Sikder, O.; Tamkin,
A.; Thamkul, J.; Kaplan, J.; Clark, J.; and Ganguli, D. 2024.
Towards Measuring the Representation of Subjective Global
Opinions in Language Models. In First Conference on Lan-
guage Modeling.
Durmus, E.; Nguyen, K.; Liao, T. I.; Schiefer, N.; Askell,
A.; Bakhtin, A.; Chen, C.; Hatfield-Dodds, Z.; Hernandez,
D.; Joseph, N.; et al. 2023. Towards measuring the repre-
sentation of subjective global opinions in language models.
arXiv preprint arXiv:2306.16388.
Geertz, C. 2017. The interpretation of cultures. Basic books.
Guo, D.; Yang, D.; Zhang, H.; Song, J.; Zhang, R.; Xu, R.;
Zhu, Q.; Ma, S.; Wang, P.; Bi, X.; et al. 2025. Deepseek-r1:
Incentivizing reasoning capability in llms via reinforcement
learning. arXiv preprint arXiv:2501.12948.
Haerpfer, C.; Inglehart, R.; Moreno, A.; Welzel, C.;
Kizilova, K.; Diez-Medrano, J.; Lagos, M.; Norris, P.;
Ponarin, E.; and Puranen, B. 2022.
World Values Sur-
vey: Round Seven – Country-Pooled Datafile Version 6.0.
Dataset.
Hall, E. T. 1976. Beyond culture. Anchor.
Kaneko, M.; Aji, A. F.; and Baldwin, T. 2025. Balanced
Multi-Factor In-Context Learning for Multilingual Large
Language Models. In Christodoulopoulos, C.; Chakraborty,
T.; Rose, C.; and Peng, V., eds., Proceedings of the 2025
Conference on Empirical Methods in Natural Language
Processing, 20096–20115. Suzhou, China: Association for
Computational Linguistics. ISBN 979-8-89176-332-6.
Li, C.; Chen, M.; Wang, J.; Sitaram, S.; and Xie, X. 2024.
Culturellm: Incorporating cultural differences into large lan-
guage models. Advances in Neural Information Processing
Systems, 37: 84799–84838.
Liu, A.; Feng, B.; Xue, B.; Wang, B.; Wu, B.; Lu, C.; Zhao,
C.; Deng, C.; Zhang, C.; Ruan, C.; et al. 2024. Deepseek-v3
technical report. arXiv preprint arXiv:2412.19437.

--- Page 9 ---

Liu, Y. 2024. Robust evaluation measures for evaluating so-
cial biases in masked language models. In Proceedings of
the AAAI Conference on Artificial Intelligence, volume 38,
18707–18715.
Liu, Y.; and Chu, C. 2025. Do LLMs Align Human Values
Regarding Social Biases? Judging and Explaining Social Bi-
ases with LLMs. In Christodoulopoulos, C.; Chakraborty,
T.; Rose, C.; and Peng, V., eds., Findings of the Associa-
tion for Computational Linguistics: EMNLP 2025, 21591–
21628. Suzhou, China: Association for Computational Lin-
guistics. ISBN 979-8-89176-335-7.
Mannheim, K. 2013. Ideology and utopia. Routledge.
Markus, H. R.; and Kitayama, S. 2014. Culture and the self:
Implications for cognition, emotion, and motivation. In Col-
lege student development and academic life, 264–293. Rout-
ledge.
Mason, W.; and Suri, S. 2012. Conducting behavioral re-
search on Amazon’s Mechanical Turk. Behavior research
methods, 44(1): 1–23.
Masoud, R.; Liu, Z.; Ferianc, M.; Treleaven, P. C.; and Ro-
drigues, M. R. 2025. Cultural Alignment in Large Language
Models: An Explanatory Analysis Based on Hofstede’s Cul-
tural Dimensions. In Rambow, O.; Wanner, L.; Apidianaki,
M.; Al-Khalifa, H.; Eugenio, B. D.; and Schockaert, S., eds.,
Proceedings of the 31st International Conference on Com-
putational Linguistics, 8474–8503. Abu Dhabi, UAE: Asso-
ciation for Computational Linguistics.
Meister, N.; Guestrin, C.; and Hashimoto, T. 2025. Bench-
marking Distributional Alignment of Large Language Mod-
els. In Chiruzzo, L.; Ritter, A.; and Wang, L., eds., Proceed-
ings of the 2025 Conference of the Nations of the Americas
Chapter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long Papers),
24–49. Albuquerque, New Mexico: Association for Compu-
tational Linguistics. ISBN 979-8-89176-189-6.
Minkov, M. 2012. World values survey. The Wiley-Blackwell
Encyclopedia of Globalization.
OpenAI. 2023a. GPT-3.5 Turbo. https://platform.openai.
com/docs/models/gpt-3.5-turbo. Product documentation for
the GPT-3.5 Turbo family.
OpenAI. 2025. Introducing GPT-5. Published August 7,
2025.
OpenAI,
R.
2023b.
Gpt-4
technical
report.
arxiv
2303.08774. View in Article, 2(5): 1.
Ouyang, L.; Wu, J.; Jiang, X.; Almeida, D.; Wainwright, C.;
Mishkin, P.; Zhang, C.; Agarwal, S.; Slama, K.; Ray, A.;
et al. 2022. Training language models to follow instructions
with human feedback. Advances in neural information pro-
cessing systems, 35: 27730–27744.
Perez, E.; Ringer, S.; Lukosiute, K.; Nguyen, K.; Chen,
E.; Heiner, S.; Pettit, C.; Olsson, C.; Kundu, S.; Kadavath,
S.; Jones, A.; Chen, A.; Mann, B.; Israel, B.; Seethor, B.;
McKinnon, C.; Olah, C.; Yan, D.; Amodei, D.; Amodei,
D.; Drain, D.; Li, D.; Tran-Johnson, E.; Khundadze, G.;
Kernion, J.; Landis, J.; Kerr, J.; Mueller, J.; Hyun, J.; Lan-
dau, J.; Ndousse, K.; Goldberg, L.; Lovitt, L.; Lucas, M.;
Sellitto, M.; Zhang, M.; Kingsland, N.; Elhage, N.; Joseph,
N.; Mercado, N.; DasSarma, N.; Rausch, O.; Larson, R.;
McCandlish, S.; Johnston, S.; Kravec, S.; El Showk, S.;
Lanham, T.; Telleen-Lawton, T.; Brown, T.; Henighan, T.;
Hume, T.; Bai, Y.; Hatfield-Dodds, Z.; Clark, J.; Bowman,
S. R.; Askell, A.; Grosse, R.; Hernandez, D.; Ganguli, D.;
Hubinger, E.; Schiefer, N.; and Kaplan, J. 2023. Discover-
ing Language Model Behaviors with Model-Written Evalua-
tions. In Rogers, A.; Boyd-Graber, J.; and Okazaki, N., eds.,
Findings of the Association for Computational Linguistics:
ACL 2023, 13387–13434. Toronto, Canada: Association for
Computational Linguistics.
Peterson, M. F. 2003. Culture’s consequences: Comparing
values, behaviors, institutions, and organizations across na-
tions.
Plebe, A.; and Vivian, M. 2015. When language shapes per-
ception. Rivista Italiana di Filosofia del Linguaggio, 9(2).
Radford, A.; Wu, J.; Child, R.; Luan, D.; Amodei, D.;
Sutskever, I.; et al. 2019. Language models are unsupervised
multitask learners. OpenAI blog, 1(8): 9.
Sanh, V.; Webson, A.; Raffel, C.; Bach, S. H.; Sutawika, L.;
Alyafeai, Z.; Chaffin, A.; Stiegler, A.; Scao, T. L.; Raja, A.;
et al. 2021. Multitask prompted training enables zero-shot
task generalization. arXiv preprint arXiv:2110.08207.
Santurkar, S.; Durmus, E.; Ladhak, F.; Lee, C.; Liang, P.; and
Hashimoto, T. 2023. Whose opinions do language models
reflect? In International Conference on Machine Learning,
29971–30004. PMLR.
Shweder, R. A.; Goodnow, J. J.; Hatano, G.; LeVine, R. A.;
Markus, H. R.; and Miller, P. J. 2007. The cultural psychol-
ogy of development: One mind, many mentalities. Hand-
book of child psychology, 1.
Studdiford, Z.; Rogers, T. T.; Suresh, S.; and Mukherjee, K.
2025. Evaluating Steering Techniques using Human Simi-
larity Judgments. arXiv preprint arXiv:2505.19333.
Sukiennik, N.; Gao, C.; Xu, F.; and Li, Y. 2025. An eval-
uation of cultural value alignment in llm.
arXiv preprint
arXiv:2504.08863.
Team, Q. 2024. Qwen2.5: A Party of Foundation Models.
Turner, J. H. 2000.
On the Origins of Human Emo-
tions.
Redwood City: Stanford University Press.
ISBN
9780804764360.
Vygotsky, L. S. 2012. Thought and language, volume 29.
MIT press.
Wallace, A. F.; and Fogelson, R. D. 1961. Culture and per-
sonality. Biennial review of anthropology, 42–78.
Wang, A.; Morgenstern, J.; and Dickerson, J. P. 2025. Large
language models that replace human participants can harm-
fully misportray and flatten identity groups. Nature Machine
Intelligence, 1–12.
Wang, W.; Jiao, W.; Huang, J.; Dai, R.; Huang, J.-t.; Tu, Z.;
and Lyu, M. 2024. Not All Countries Celebrate Thanksgiv-
ing: On the Cultural Dominance in Large Language Models.
In Ku, L.-W.; Martins, A.; and Srikumar, V., eds., Proceed-
ings of the 62nd Annual Meeting of the Association for Com-
putational Linguistics (Volume 1: Long Papers), 6349–6384.

--- Page 10 ---

Bangkok, Thailand: Association for Computational Linguis-
tics.
Wei, J.; Bosma, M.; Zhao, V. Y.; Guu, K.; Yu, A. W.; Lester,
B.; Du, N.; Dai, A. M.; and Le, Q. V. 2021.
Finetuned
language models are zero-shot learners.
arXiv preprint
arXiv:2109.01652.
Zhuo, J.; Zhang, S.; Fang, X.; Duan, H.; Lin, D.; and Chen,
K. 2024. ProSA: Assessing and understanding the prompt
sensitivity of LLMs. arXiv preprint arXiv:2410.12405.
A
More Details of The World Values Survey
Collecting data on human opinions across global, language,
and temporal dimensions is costly. The WVS is an in-
ternational academic project studying human values, be-
liefs, norms, self-descriptions, and other elements of na-
tional culture, as well as political attitudes and opinions,
across the globe. The scholars who lead the project are
mainly interested in the relationships between economic de-
velopment, cultural change, and political life on all conti-
nents. The WVS data have also been widely used by cross-
cultural psychologists, anthropologists, and other social sci-
entists (Minkov 2012). The project started in 1981 and has
been operating in more than 120 world countries and re-
gions. The main research instrument of the project is a rep-
resentative comparative social survey which is conducted
globally every 5 years (Haerpfer et al. 2022). The latest wave
of the survey employs a standardized questionnaire contain-
ing approximately 259 subjective questions. Its broad re-
gional and topical coverage, as well as its free public access
to survey data and research results, makes the WVS one of
the most authoritative and widely used multi-country sur-
veys in the field of social sciences.
B
Experiment Settings
B.1
Hyperparameter
The hyperparameter settings for the LLMs (if available) are
shown in Table 3.
Hyperparameter
Assignment
Top-p
1.0
Temperature
0.0
Max new tokens
256
Frequency penalty
0.0
Presence penalty
0.0
Table 3: Names and descriptions of columns in jsonl file.
For GPT-5, we set the reasoning configuration to
reasoning = {effort = ‘‘low’’} and the text
generation configuration to text = {verbosity =
‘‘low’’} to obtain concise responses with reduced rea-
soning depth.
B.2
Question Filter Rules
The wave 7 questionnaire contains 259 questions, but not
all of them are suitable for LLMs to answer. If the ques-
tions are not selected appropriately, it may cause bias in the
evaluation of LLMs. Therefore, we first filter the questions.
We filter out the following types of questions from the WVS
questionnaire:
Not multiple choice.
For example, questions Q7 to Q17
each contain two options (“Mentioned” and “Not men-
tioned”), and the questionnaire requires respondents to
choose up to 5 mentioned options from Q7 to Q17.

--- Page 11 ---

Names
Descriptions
id
The question id
question
The question description
choice keys
The option number
choices
The option content
answer
The combined option num-
ber and option content
Table 4: Names and descriptions of columns in jsonl file.
Country
Example IDs
Default (English version)
Q60, Q70, Q90, Q110, Q130
Argentina
Q40, Q60, Q80, Q150, Q160
Brazil
Q40, Q60, Q80, Q150, Q160
Chile
Q40, Q60, Q80, Q150, Q160
China
Q60, Q70, Q110, Q150, Q160
Germany
Q40, Q80, Q150, Q160, Q170
Japan
Q60, Q70, Q90, Q110, Q130
Korea
Q40, Q80, Q150, Q160, Q170
Russia
Q40, Q60, Q80, Q150, Q160
Uruguay
Q40, Q60, Q80, Q150, Q160
Vietnam
Q40, Q60, Q80, Q150, Q160
Table 5: The question ids of the few-shot examples we se-
lected for each country.
Require life experience to answer.
Some questions re-
quire life experience to answer. Therefore, they are not suit-
able for LLMs to answer. For example, questions Q51 to
Q55 begin with “In the last 12 months.”
Need to edit slot.
Some questions need to edit a slot ac-
cording to the respondent’s country. For example, Q64 needs
to modify the slot [churches] according to the respon-
dent’s country. In the “No steering” scenario, we do not want
to leak any country information to LLMs.
Objective question.
Some questions are objective ques-
tions. For example, question Q91, “Five countries have per-
manent seats on the Security Council of the United Nations.
Which one of the following is not a member? A) France, B)
China, C) India.”
Require a nationality.
Some questions require the re-
spondents to have a nationality, so they are not suitable for
LLMs to answer. For example, question Q120, “How high
is the risk in this country to be held accountable for giving
or receiving a bribe, gift or favor in return for public ser-
vice? To indicate your opinion, use a 10-point scale where
‘1’ means ‘no risk at all’ and ‘10’ means ‘very high risk’.”
We
put
all
the
filtered
144
questions
in
the
WV7 English.jsonl
file
under
the
dataset/questions
folder.
The
naming
conven-
tion for saving files with questions in other languages is to
replace English with the other language (e.g., German).
Table 4 is the explanation of each column in the jsonl
file.
B.3
Full Prompts
We follow the settings of Meister, Guestrin, and Hashimoto
(2025) by providing few-shot examples to control the
LLMs’ output format. Our prompts follow the following for-
mat:
Task instruction:
I will provide a distribution over answer choices
on a series of questions to help you understand the
formatting of this task. After the 5 examples, please
express the distribution of answers for the question
asked. Do not follow the distribution expressed in the
examples as they are only to give you an example
of formatting, express the distribution based on your
understanding of how humans may respond. Please
only respond in the exact format of a dictionary
mapping answer choice number to probability, no
extra spaces, characters, quotes or text. Please only
produce 1 sentence in this format. Answers outside of
this format will not be accepted. First I will provide a
few examples of this task just to give you a sense of
the answer formatting, then you will perform the task
yourself.
Few-shot examples:
Question: How much do you trust people you know
personally?
‘1’. Trust completely
‘2’. Trust somewhat
‘3’. Do not trust very much
‘4’. Do not trust at all
Answer: {‘1’: ‘31.01%’, ‘2’: ‘3.21%’, ‘3’: ‘30.31%’,
‘4’: ‘35.47%’}
(The other four examples have been omitted here)
Input question:
Question: How important is family in your life?
‘1’. Very important
‘2’. Rather important
‘3’. Not very important
‘4’. Not at all important
Answer:
(We can get a distribution in JSON format)
The task instruction part will slightly differ depending on
the steering method. For example, in the case of persona
steering, the task instruction will require the LLMs to em-
ulate people from a specific country (e.g., Germany). Note
that in the case of language steering, the task instruction,
few-shot examples, and input question are all replaced with
questions in the target language or translated into the target
language.
When selecting few-shot examples, there may be missing
opinion distributions for some questions depending on the
country. Table 5 lists the question ids of the few-shot exam-
ples we selected for each country.
In addition, all few-shot examples are available under the

--- Page 12 ---

input\express distribution folder. Table 6 lists
each file and its corresponding explanation.
B.4
More Details of Distribution Expression
Methods
Model log probability.
A common method for estimating
the choice distribution is to consider the model’s log proba-
bilities of the next token for each option token (e.g., ‘1’, ‘2’,
etc.) as a class distribution and sample from it. This method
is a standard practice (Santurkar et al. 2023). However, pre-
vious studies have shown that the probabilities derived from
LLMs are usually much sharper than real human opinion
distribution, i.e., most of the probabilities are concentrated
in a few answers (Durmus et al. 2024).
Sequence of tokens.
Another method is to directly let the
model “act as a sampler.” Specifically, we instruct the LLM
to output 30 samples from its internal distribution at once
(e.g., 1124243412434213). This method is more conve-
nient when generating samples from the opinion distribu-
tion for emulation. However, since we use a limited-length
sequence to approximate the underlying distribution, the es-
timation accuracy may be subject to errors due to limits on
sample size (Meister, Guestrin, and Hashimoto 2025).
Verbalized
distribution.
This
method
directly
al-
lows the LLM to verbalize the distribution in JSON
format in their output (e.g., {1: 31%, 2: 4%, 3:
30%, 4: 35%}), without any estimation steps or post-
processing (Meister, Guestrin, and Hashimoto 2025).
Meister, Guestrin, and Hashimoto (2025)’s analysis reveals
that “verbalized distribution” outperforms the other “model
log probability” and “sequence of tokens”. Therefore,
we use “verbalized distribution” to represent the opinion
distributions in our study.
C
Complete Country List
Wave 7 of the WVS covers 66 countries or regions. Here is
the complete list, with the languages supported in parenthe-
ses. The contents in “()” are the language(s) in which the
questionnaire is available for each country.
Andorra (Catalan, English, French, Spanish), Argentina
(Spanish),
Armenia
(Armenian),
Australia
(English),
Bangladesh
(Bangla),
Bolivia
(Spanish),
Brazil
(Por-
tuguese), Canada (English, French), Colombia (Spanish),
Cyprus (Greek, Turkish), Czechia (Czech), Chile (Spanish),
China (Chinese), Ecuador (Spanish), Egypt (Arabic),
Ethiopia (Afan Oromo, Amharic, Tigrinya), Germany
(German), Greece (Greek), Guatemala (Spanish), Hong
Kong SAR (Chinese, English), India (Bengali, English,
Hindi, Marathi, Punjabi, Telugu), Indonesia (Indonesian),
Iran (Farsi), Iraq (Arabic), Japan (Japanese), Jordan (Ara-
bic), Kazakhstan (Kazakh, Russian), Kenya (Swahili),
Kyrgyzstan (Kyrgyz, Russian), Lebanon (Arabic), Libya
(Arabic),
Macau
SAR
(Chinese),
Malaysia
(Chinese,
Malay), Maldives (Dhivehi), Mexico (Spanish), Mongolia
(Mongolian), Morocco (Arabic), Myanmar (Burmese),
Netherlands (Dutch), New Zealand (English), Nicaragua
(Spanish), Nigeria (Hausa, Igbo, Yoruba), Pakistan (Urdu),
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95
Mongolia
Chile
Thailand
Canada
Czech Republic
Slovakia
Ukraine
United States
Hong Kong
Uruguay
Northern Ireland
Macao SAR
Russia
Guatemala
Argentina
Kazakhstan
Great Britain
Australia
Singapore
Mexico
Andorra
Cyprus
Ecuador
Venezuela
New Zealand
Serbia
Brazil
Kenya
Nicaragua
Taiwan
Malaysia
South Korea
Colombia
Greece
Bolivia
Puerto Rico
Romania
Japan
Turkey
Germany
India
Morocco
Philippines
Iran
Netherlands
Lebanon
Viet Nam
Uzbekistan
Peru
China
Iraq
Zimbabwe
Armenia
Nigeria
Tajikistan
Indonesia
Pakistan
Tunisia
Maldives
Kyrgyzstan
Ethiopia
Jordan
Myanmar
Bangladesh
Libya
Egypt
***
***
***
***
***
***
***
***
***
**
**
***
*
*
*
*
*
**
*
*
**
*
**
**
***
***
***
***
***
Figure 5: The alignment scores between Aya23 and different
countries.
Peru (Spanish), Philippines (Bicol, Cebuano, Filipino,
Hiligaynon, Iluko, Tausug, Waray), Puerto Rico (Spanish),
Romania (Romanian), Russia (Russian), Serbia (Serbian),
Singapore (Chinese, English, Malay), Slovakia (Slovak),
South Korea (Korean), Taiwan (Chinese), Tajikistan (Rus-
sian, Tajik), Thailand (Thai), Tunisia (Arabic), Turkey
(Turkish), Ukraine (Russian, Ukrainian), United King-
dom Great Britain (English), United Kingdom Northern
Ireland (English), Uruguay (Spanish), United States (En-
glish), Uzbekistan (Uzbek), Venezuela (Spanish), Vietnam
(Vietnamese), and Zimbabwe (Ndebele, Shona).
D
More Results of RQ1
D.1
Country Level
We provide the alignment scores for all seven LLMs with
different countries; the checklist is shown in Table 7.

--- Page 13 ---

File Name
Steering Method
lang-En dist-random.txt
no steering, persona steering
lang-En dist-{country}.txt
few-shot steering
lang-{language} dist-random.txt
language steering
persona + language steering
lang-{language} dist-{country}.txt
few-shot + language steering
Table 6: The few-shot examples under the inputs/few shot folder. Here, {language} represents the language of the
prompt, which can be De (German), En (English), Es (Spanish), Ja (Japanese), Ko (Korean), Pt (Portuguese), Ru (Russian), Vi
(Vietnamese), and Zh (Chinese). The random means that the distribution of examples is random, and {country} means that
the distribution of examples is the opinion distribution of that country.
Models
Figures
Aya23
Figure 5
Qwen2.5
Figure 6
Llama3
Figure 7
GPT-3.5
Figure 8
GPT-4
Figure 9
GPT-5
Figure 10
DeepSeek-V3
Figure 11
DeepSeek-R1
Figure 12
Table 7: Checklist of alignment scores between LLMs and
different countries.
By comparing Figures 5 to 12, we find that these mod-
els have high alignment scores with the United States,
Chile, Thailand, Canada, Mongolia, and Slovakia. However,
they have low alignment scores with Bangladesh, Myanmar,
Libya, and Egypt.
Intuition.
If we perform a rough clustering based on our
intuition about regions, we can see some trends: LLMs are
more aligned with English-speaking countries and several
Latin American and Central and Eastern European countries
(e.g., the United States, Canada, Chile, the Czech Republic,
Slovakia, and Uruguay). They are less aligned with several
large Asian countries (e.g., China, India, and Indonesia).
D.2
Alignment Difference Level
We provide the relationship of different countries to all seven
LLMs’ opinion distribution and the average human opinion
distribution alignment scores; the checklist is shown in Ta-
ble 8.
Models
Figures
Aya23
Figure 13
Qwen2.5
Figure 14
Llama3
Figure 15
GPT-3.5
Figure 16
GPT-4
Figure 17
GPT-5
Figure 18
DeepSeek-V3
Figure 19
DeepSeek-R1
Figure 20
Table 8: Checklist of relationship of different countries to
all seven LLMs’ opinion distribution and the average human
opinion distribution alignment scores.
We find that Aya23, GPT-3.5, and DeepSeek-V3 do not
achieve alignment scores higher than the average human
alignment with any country. Other LLMs align well with
only a few countries, such as the United States and Canada,
but show poor alignment with most countries. This indi-
cates that aligning LLMs with human opinions remains a
considerable challenge. In addition, it should be noted that
the alignment scores of LLMs with countries are positively
correlated with the alignment scores of average human dis-
tributions with countries; that is, LLMs are more likely to
align with countries that have more aligned average human
distributions.
E
More Results of RQ2
In addition to the Chinese and German in the main text, we
provide the experimental results of Japanese, Korean, Rus-
sian, Vietnamese, Portuguese, and Spanish in Table 9. The
experimental results show that language steering is more ef-
fective when a language is used by a single country. How-
ever, when a language such as Spanish is used by many
countries, language steering may cause LLMs to express the
average opinion of Spanish-speaking countries rather than
the opinion of a specific country. This result suggests that
when steering LLMs to emulate the opinions of these coun-
tries, features other than language should also be considered.
F
More Results of RQ3
We use wave 7’s survey data to filter countries for each
LLM, and Table 10 provides a list of countries filtered for
each LLM. In the case of the threshold τ = 0.02, Aya-
23-35B, GPT-3.5-Turbo, and DeepSeek-V3 cover less than

--- Page 14 ---

0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95
United States
Chile
Northern Ireland
Thailand
Canada
Hong Kong
Mongolia
Singapore
Slovakia
Uruguay
Czech Republic
Cyprus
Australia
Macao SAR
Great Britain
Kazakhstan
Ukraine
Argentina
Brazil
Taiwan
New Zealand
Andorra
Russia
South Korea
Kenya
Japan
Puerto Rico
Germany
Venezuela
Mexico
Greece
Ecuador
Malaysia
Guatemala
Morocco
Turkey
Romania
India
Colombia
Philippines
Netherlands
Serbia
Nicaragua
Uzbekistan
Bolivia
Iran
Zimbabwe
Lebanon
Nigeria
Tajikistan
China
Indonesia
Peru
Ethiopia
Armenia
Pakistan
Tunisia
Maldives
Kyrgyzstan
Viet Nam
Iraq
Bangladesh
Jordan
Myanmar
Libya
Egypt
***
***
***
***
***
***
***
***
***
***
**
***
***
***
***
*
**
**
**
*
**
*
*
*
*
*
**
**
**
**
**
***
***
***
***
***
***
Figure 6: The alignment scores between Qwen2.5 and dif-
ferent countries.
five countries, so we do not consider these models. Table 22
shows the trend of the average alignment scores of other
LLMs with countries across waves.
G
More Results of Discussion
G.1
Alignment of Human Opinions across
Countries
We provide a full version of the alignment score heatmap
between countries and LLMs in Figure 22.
Individual columns and rows appear as “darker horizon-
tal and vertical stripes”: this means that some countries are
less aligned with most other countries (systematic outliers).
There are several noticeable dark stripes in the figure, such
as Northern Ireland, the Netherlands, and New Zealand.
However, these countries have high alignment scores with
each other and with Australia, Brazil, and Great Britain.
0.65
0.70
0.75
0.80
0.85
0.90
0.95
Singapore
Thailand
Chile
Northern Ireland
United States
Canada
Uruguay
Cyprus
Hong Kong
Australia
Great Britain
Taiwan
New Zealand
Kazakhstan
Mongolia
Japan
Slovakia
Andorra
Macao SAR
Kenya
Germany
Puerto Rico
Ukraine
Czech Republic
India
Brazil
Malaysia
Ecuador
Philippines
Argentina
South Korea
Uzbekistan
Turkey
Russia
Greece
Venezuela
Zimbabwe
Mexico
Nigeria
Netherlands
Romania
Colombia
Iran
Guatemala
Nicaragua
Tajikistan
China
Morocco
Indonesia
Bolivia
Ethiopia
Lebanon
Maldives
Peru
Kyrgyzstan
Serbia
Pakistan
Tunisia
Armenia
Viet Nam
Iraq
Myanmar
Bangladesh
Jordan
Libya
Egypt
***
***
***
***
***
***
***
**
***
**
**
**
*
*
*
*
*
*
*
*
*
*
*
**
***
***
***
***
***
***
Figure 7: The alignment scores between Llama3 and differ-
ent countries.
The alignment scores between LLMs are relatively high,
indicating a certain degree of homogeneity between the
LLMs. This may be because they have similar training cor-
pora Bommasani et al. (2022). We also find that LLMs con-
sistently exhibit poor alignment with certain countries. For
example, Bangladesh, Egypt, Iraq, Libya, and Myanmar, etc.
These findings supplement the conclusions in the main text.
G.2
Internal Consistency of LLMs
We provide a list of questions we selected for studying the
internal consistency of LLMs in Table 11.
G.3
Sensitivity of LLMs
Inspired by Santurkar et al. (2023), we test the prompt sen-
sitivity of the LLMs used in our experiments against the fol-
lowing factors:

--- Page 15 ---

0.6
0.7
0.8
0.9
Mongolia
Chile
Thailand
Ukraine
Czech Republic
Slovakia
Hong Kong
Russia
United States
Kazakhstan
Guatemala
Macao SAR
Kenya
Canada
Philippines
Mexico
Malaysia
Uruguay
Venezuela
Northern Ireland
Argentina
Ecuador
Brazil
South Korea
Cyprus
Nicaragua
Serbia
Singapore
Morocco
Great Britain
Taiwan
Colombia
Bolivia
Australia
Greece
Andorra
Turkey
Lebanon
Romania
India
New Zealand
Puerto Rico
Germany
Japan
Uzbekistan
Viet Nam
Peru
Iran
Nigeria
Pakistan
Zimbabwe
Netherlands
Tajikistan
Armenia
Iraq
Tunisia
Indonesia
China
Kyrgyzstan
Ethiopia
Maldives
Jordan
Libya
Bangladesh
Myanmar
Egypt
***
***
***
***
***
***
***
**
**
*
**
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
**
**
***
***
***
***
***
Figure 8: The alignment scores between GPT-3.5 and differ-
ent countries.
• The
order
in
which
the
question
op-
tions
are
presented
to
the
model.
The
file
dataset/questions/WV7 shuffle.jsonl
contains data with the order of options shuffled.
• The
few-shot
examples
(the
number
of
the
few-shot
examples
and
the
probability
dis-
tribution
of
the
few-shot
examples).
The
file
inputs/sensitivity/number.txt is the exam-
ples that change the number of few-shot examples from
5 to 3. The file inputs/sensitivity/prob.txt
is the examples that change the probability distribution
of few-shot examples.
All
results
are
listed
under
the
results/Discussion/sensitivity folder.
0.65
0.70
0.75
0.80
0.85
0.90
0.95
United States
Canada
Northern Ireland
Chile
Czech Republic
Mongolia
Slovakia
Uruguay
Thailand
Ukraine
Australia
Great Britain
Argentina
Hong Kong
Macao SAR
Singapore
Russia
New Zealand
Brazil
Kazakhstan
Cyprus
Andorra
Taiwan
Kenya
Puerto Rico
Guatemala
Malaysia
Venezuela
Serbia
Ecuador
Greece
Germany
Mexico
Philippines
Japan
India
South Korea
Morocco
Netherlands
Colombia
Nicaragua
Romania
Turkey
Bolivia
Iran
Lebanon
Uzbekistan
Zimbabwe
Nigeria
Viet Nam
Tajikistan
Pakistan
China
Indonesia
Ethiopia
Peru
Iraq
Armenia
Kyrgyzstan
Maldives
Tunisia
Jordan
Bangladesh
Myanmar
Libya
Egypt
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
**
*
**
*
*
*
*
*
*
*
*
**
**
**
**
**
***
***
***
***
***
***
Figure 9: The alignment scores between GPT-4 and different
countries.
G.4
The Impact of Model Size
To investigate the impact of different model sizes on
experimental results, we evaluated 5 smaller Qwen2.5
(0.5B/1.5B/3B/7B/14B) models. Figure 23 shows the align-
ment scores of the Qwen2.5 model in different sizes for
each country. Although previous studies have shown that
model alignment is not directly related to model size (Liu
and Chu 2025). In Figure 23, we can observe that, except for
Qwen2.5-1.5B-Instruct, the alignment score exhibits a clear
positive correlation with model size, confirming that larger
models more accurately capture the distribution of human
values. We tests the language steering performance on Chi-
nese and German across different size Qwen models. The
experimental results are shown in Table 12. Language steer-
ing also performed more effectively on larger models.

--- Page 16 ---

0.65
0.70
0.75
0.80
0.85
0.90
0.95
United States
Northern Ireland
Canada
Slovakia
Chile
Australia
Great Britain
Cyprus
Hong Kong
Ukraine
Argentina
Czech Republic
Andorra
New Zealand
Singapore
Taiwan
Uruguay
Mongolia
Greece
Russia
Germany
Thailand
Brazil
Romania
Puerto Rico
Venezuela
Kazakhstan
Netherlands
Japan
Macao SAR
Serbia
Guatemala
Morocco
Ecuador
Mexico
South Korea
Colombia
Kenya
Bolivia
Nicaragua
Turkey
Malaysia
Peru
India
Lebanon
Iran
Armenia
Zimbabwe
Philippines
Nigeria
China
Maldives
Ethiopia
Kyrgyzstan
Tunisia
Uzbekistan
Tajikistan
Iraq
Indonesia
Pakistan
Viet Nam
Jordan
Libya
Egypt
Bangladesh
Myanmar
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
***
**
**
**
**
**
*
*
*
*
**
*
*
*
**
**
**
***
***
***
***
**
***
***
***
***
***
***
Figure 10: The alignment scores between GPT-5 and differ-
ent countries.
G.5
Other Matrics
In addition to alignment, previous work also employed
the normalized mean absolute error (NMAE) and Jensen-
Shannon divergence (JSD) to calculate the distance between
distributions (Liu 2024). In this section, we employ NMAE
and JSD as alignment scores to validate Pearson’s r between
the current metric alignment and both NMAE and JSD.
As shown in Table 13-20, the three alignment metrics align-
ment, NMAE, and JSD keep high Pearson’s r across dif-
ferent models, indicating consistency among the alignment
metrics.
G.6
Other Baselines
Take DeepSeek-R1 as an example, we also perform a reli-
gious analysis, using religion as a baseline. As shown in Fig-
ure 24, most religions are under-aligned except Jew, which
is appropriately aligned. In addition, as shown in Figures 25
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95
Mongolia
Chile
United States
Slovakia
Northern Ireland
Canada
Czech Republic
Thailand
Ukraine
Uruguay
Hong Kong
Argentina
Russia
Kazakhstan
Kenya
Cyprus
Singapore
Macao SAR
Brazil
Great Britain
Malaysia
Guatemala
Mexico
Australia
Venezuela
Ecuador
Philippines
Taiwan
Puerto Rico
New Zealand
Morocco
Andorra
Serbia
Nicaragua
South Korea
Colombia
Greece
India
Romania
Germany
Bolivia
Turkey
Lebanon
Japan
Netherlands
Uzbekistan
Iran
Nigeria
Zimbabwe
Peru
Tajikistan
Viet Nam
Pakistan
Iraq
Indonesia
Maldives
Kyrgyzstan
Ethiopia
Armenia
Tunisia
China
Jordan
Libya
Myanmar
Bangladesh
Egypt
***
***
***
***
***
***
***
**
***
**
**
**
*
*
*
*
*
*
*
*
*
*
*
*
*
*
**
*
*
**
**
**
**
**
***
***
***
***
***
Figure 11: The alignment scores between DeepSeek-V3 and
different countries.
and 26, we include regional (e.g., North American and Eu-
rope) averages to enrich our baseline. For example, within
the North American region, Canada is over-aligned, the US
is appropriately aligned, while Mexico, Puerto Rico, and
Guatemala are under-aligned.
H
Limitations
We acknowledge that our study has limitations, one of which
is that it is limited by the scope of the WVS and cannot cover
all countries. The second limitation is that, due to human
resource constraints, we cannot examine all languages sup-
ported by the WVS. However, we are fortunate to have cov-
ered eight languages (Spanish, Chinese, Japanese, Korean,
German, Russian, Vietnamese, and Portuguese) and report
exciting findings. Another limitation is that we did not con-
sider whether there were cross-linguistic effects if a country
conducted its survey using a multilingual WVS question-

--- Page 17 ---

0.65
0.70
0.75
0.80
0.85
0.90
0.95
United States
Chile
Slovakia
Mongolia
Northern Ireland
Canada
Ukraine
Czech Republic
Hong Kong
Cyprus
Thailand
Singapore
Russia
Argentina
Australia
Kazakhstan
Guatemala
Taiwan
Great Britain
Macao SAR
Mexico
Kenya
Greece
Uruguay
Malaysia
Andorra
New Zealand
Brazil
Romania
Venezuela
South Korea
Ecuador
Serbia
Morocco
Germany
Puerto Rico
Japan
Turkey
Colombia
Nicaragua
Philippines
India
Lebanon
Bolivia
Netherlands
Iran
Peru
Zimbabwe
Nigeria
Uzbekistan
Tajikistan
Maldives
Armenia
Pakistan
Kyrgyzstan
Ethiopia
Iraq
Indonesia
Tunisia
Viet Nam
China
Jordan
Bangladesh
Libya
Myanmar
Egypt
***
***
***
***
***
***
***
***
***
***
***
***
***
**
**
**
**
**
**
*
*
**
*
*
**
*
**
**
**
**
**
***
**
***
***
***
***
***
Figure 12: The alignment scores between DeepSeek-R1 and
different countries.
naire. At the very least, we hope that these limitations can
serve as directions for future studies.

--- Page 18 ---

0.775
0.800
0.825
0.850
0.875
0.900
0.925
Alignment Score with Average Humans' Opinions
0.775
0.800
0.825
0.850
0.875
0.900
0.925
Alignment Score with Aya23
Andorra
Argentina
Armenia
Australia
Bangladesh
Bolivia
Brazil
Canada
Chile
China
Colombia
Cyprus
Czech Republic
Egypt
Ecuador
Ethiopia
Germany
Greece
Guatemala
Great Britain
Hong Kong
India
Indonesia
Iran
Iraq
Jordan
Japan
Kazakhstan
Kenya
Kyrgyzstan
Lebanon
Libya
Malaysia
Mexico
Mongolia
Morocco
Myanmar
Netherlands
New Zealand
Nicaragua
Nigeria
Pakistan
Peru
Philippines
Puerto Rico
Romania
Russia
Singapore
Slovakia
South Korea
Tajikistan
Thailand
Tunisia
Taiwan
Turkey
Ukraine
United States
Uruguay
Uzbekistan
Viet Nam
Venezuela
Zimbabwe
Macao SAR
Maldives
Serbia
Northern Ireland
y = x
Figure 13: The relationship of different countries to Aya23’s opinion distribution and the average human opinion distribution
alignment scores.
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with Average Humans' Opinions
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with Qwen25
Andorra
Argentina
Armenia
Australia
Bangladesh
Bolivia
Brazil
Canada
Chile
China
Colombia
Cyprus
Czech Republic
Egypt
Ecuador
Ethiopia
Germany
Greece
Guatemala
Great Britain
Hong Kong
India
Indonesia
Iran
Iraq
Jordan
Japan
Kazakhstan
Kenya
Kyrgyzstan
Lebanon
Libya
Malaysia
Mexico
Mongolia
Morocco
Myanmar
Netherlands
New Zealand
Nicaragua
Nigeria
Pakistan
Peru
Philippines
Puerto Rico
Romania
Russia
Singapore Slovakia
South Korea
Tajikistan
Thailand
Tunisia
Taiwan
Turkey
Ukraine
United States
Uruguay
Uzbekistan
Viet Nam
Venezuela
Zimbabwe
Macao SAR
Maldives
Serbia
Northern Ireland
y = x
Figure 14: The relationship of different countries to Qwen2.5’s opinion distribution and the average human opinion distribution
alignment scores.

--- Page 19 ---

0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with Average Humans' Opinions
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with Llama3
Andorra
Argentina
Armenia
Australia
Bangladesh
Bolivia
Brazil
Canada
Chile
China
Colombia
Cyprus
Czech Republic
Egypt
Ecuador
Ethiopia
Germany
Greece
Guatemala
Great Britain
Hong Kong
India
Indonesia
Iran
Iraq
Jordan
Japan
Kazakhstan
Kenya
Kyrgyzstan
Lebanon
Libya
Malaysia
Mexico
Mongolia
Morocco
Myanmar
Netherlands
New Zealand
Nicaragua
Nigeria
Pakistan
Peru
Philippines
Puerto Rico
Romania
Russia
Singapore
Slovakia
South Korea
Tajikistan
Thailand
Tunisia
Taiwan
Turkey
Ukraine
United States
Uruguay
Uzbekistan
Viet Nam
Venezuela
Zimbabwe
Macao SAR
Maldives Serbia
Northern Ireland
y = x
Figure 15: The relationship of different countries to Llama3’s opinion distribution and the average human opinion distribution
alignment scores.
0.750
0.775
0.800
0.825
0.850
0.875
0.900
0.925
Alignment Score with Average Humans' Opinions
0.750
0.775
0.800
0.825
0.850
0.875
0.900
0.925
Alignment Score with GPT-3.5
Andorra
Argentina
Armenia
Australia
Bangladesh
Bolivia
Brazil
Canada
Chile
China
Colombia
Cyprus
Czech Republic
Egypt
Ecuador
Ethiopia
Germany
Greece
Guatemala
Great Britain
Hong Kong
India
Indonesia
Iran
Iraq
Jordan
Japan
Kazakhstan
Kenya
Kyrgyzstan
Lebanon
Libya
Malaysia
Mexico
Mongolia
Morocco
Myanmar
Netherlands
New Zealand
Nicaragua
Nigeria
Pakistan
Peru
Philippines
Puerto Rico
Romania
Russia
Singapore
Slovakia
South Korea
Tajikistan
Thailand
Tunisia
Taiwan
Turkey
Ukraine
United States
Uruguay
Uzbekistan
Viet Nam
Venezuela
Zimbabwe
Macao SAR
Maldives
Serbia
Northern Ireland
y = x
Figure 16: The relationship of different countries to GPT-3.5’s opinion distribution and the average human opinion distribution
alignment scores.

--- Page 20 ---

0.78
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with Average Humans' Opinions
0.78
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with GPT-4
Andorra
Argentina
Armenia
Australia
Bangladesh
Bolivia
Brazil
Canada
Chile
China
Colombia
Cyprus
Czech Republic
Egypt
Ecuador
Ethiopia
Germany
Greece
Guatemala
Great Britain
Hong Kong
India
Indonesia
Iran
Iraq
Jordan
Japan
Kazakhstan
Kenya
Kyrgyzstan
Lebanon
Libya
Malaysia
Mexico
Mongolia
Morocco
Myanmar
Netherlands
New Zealand
Nicaragua
Nigeria
Pakistan
Peru
Philippines
Puerto Rico
Romania
Russia
Singapore
Slovakia
South Korea
Tajikistan
Thailand
Tunisia
Taiwan
Turkey
Ukraine
United States
Uruguay
Uzbekistan
Viet Nam
Venezuela
Zimbabwe
Macao SAR
Maldives
Serbia
Northern Ireland
y = x
Figure 17: The relationship of different countries to GPT-4’s opinion distribution and the average human opinion distribution
alignment scores.
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with Average Humans' Opinions
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with GPT-5
Andorra
Argentina
Armenia
Australia
Bangladesh
Bolivia
Brazil
Canada
Chile
China
Colombia
Cyprus
Czech Republic
Egypt
Ecuador
Ethiopia
Germany
Greece
Guatemala
Great Britain
Hong Kong
India
Indonesia
Iran
Iraq
Jordan
Japan
Kazakhstan
Kenya
Kyrgyzstan
Lebanon
Libya
Malaysia
Mexico
Mongolia
Morocco
Myanmar
Netherlands
New Zealand
Nicaragua
Nigeria
Pakistan
Peru
Philippines
Puerto Rico
Romania
Russia
Singapore
Slovakia
South Korea
Tajikistan
Thailand
Tunisia
Taiwan
Turkey
Ukraine
United States
Uruguay
Uzbekistan
Viet Nam
Venezuela
Zimbabwe
Macao SAR
Maldives
Serbia
Northern Ireland
y = x
Figure 18: The relationship of different countries to GPT-5’s opinion distribution and the average human opinion distribution
alignment scores.

--- Page 21 ---

0.76
0.78
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with Average Humans' Opinions
0.76
0.78
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with DeepSeek-V3
Andorra
Argentina
Armenia
Australia
Bangladesh
Bolivia
Brazil
Canada
Chile
China
Colombia
Cyprus
Czech Republic
Egypt
Ecuador
Ethiopia
Germany
Greece
Guatemala
Great Britain
Hong Kong
India
Indonesia
Iran
Iraq
Jordan
Japan
Kazakhstan
Kenya
Kyrgyzstan
Lebanon
Libya
Malaysia
Mexico
Mongolia
Morocco
Myanmar
Netherlands
New Zealand
Nicaragua
Nigeria
Pakistan
Peru
Philippines
Puerto Rico
Romania
Russia
Singapore
Slovakia
South Korea
Tajikistan
Thailand
Tunisia
Taiwan
Turkey
Ukraine
United States
Uruguay
Uzbekistan
Viet Nam
Venezuela
Zimbabwe
Macao SAR
Maldives
Serbia
Northern Ireland
y = x
Figure 19: The relationship of different countries to DeepSeek-V3’s opinion distribution and the average human opinion distri-
bution alignment scores.
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with Average Humans' Opinions
0.80
0.82
0.84
0.86
0.88
0.90
0.92
Alignment Score with DeepSeek-R1
Andorra
Argentina
Armenia
Australia
Bangladesh
Bolivia
Brazil
Canada
Chile
China
Colombia
Cyprus
Czech Republic
Egypt
Ecuador
Ethiopia
Germany
Greece
Guatemala
Great Britain
Hong Kong
India
Indonesia
Iran
Iraq
Jordan
Japan
Kazakhstan
Kenya
Kyrgyzstan
Lebanon
Libya
Malaysia
Mexico
Mongolia
Morocco
Myanmar
Netherlands
New Zealand
Nicaragua
Nigeria
Pakistan
Peru
Philippines
Puerto Rico
Romania
Russia
Singapore
Slovakia
South Korea
Tajikistan
Thailand
Tunisia
Taiwan
Turkey
Ukraine
United States
Uruguay
Uzbekistan
Viet Nam
Venezuela
Zimbabwe
Macao SAR
Maldives
Serbia
Northern Ireland
y = x
Figure 20: The relationship of different countries to DeepSeek-R1’s opinion distribution and the average human opinion distri-
bution alignment scores.

--- Page 22 ---

Method
Aya23
Llama3
Qwen2.5
GPT-3.5
GPT-4
GPT-5
DS-V3
DS-R1
AVG.
Japan (Japanese)
No Steering
0.8238
0.8513
0.8596
0.8015
0.8441
0.8744
0.8251
0.8541
0.8417
+Language Steering (Ja.)
0.8400
0.8516
0.8686
0.8141
0.8762∗∗
0.8945∗
0.8760∗∗∗
0.8931∗∗∗
0.8643∗∗∗
Persona Steering (En.)
0.8400
0.8566
0.8631
0.8035
0.8603
0.8884
0.8422
0.8680
0.8528∗
+Language Steering (Ja.)
0.8444∗
0.8540
0.8733
0.8287
0.8899∗∗∗
0.9123∗∗∗
0.8847∗∗∗
0.8996∗∗∗
0.8734∗∗∗
Few-shot Steering (En.)
0.8402
0.8618
0.8696
0.8327∗
0.8757∗∗
0.8920
0.8810∗∗∗
0.8788∗
0.8665∗∗∗
+Language Steering (Ja.)
0.8696∗∗∗
0.8508
0.8807∗
0.8280
0.9027∗∗∗
0.9053∗∗∗
0.8932∗∗∗
0.8964∗∗∗
0.8783∗∗∗
Korea (Korean)
No Steering (En.)
0.8244
0.8415
0.8632
0.8283
0.8445
0.8659
0.8378
0.8606
0.8458
+Language Steering (Ko.)
0.8230
0.8427
0.8607
0.8379
0.8530
0.8737
0.8685∗
0.8693
0.8536
Persona Steering (En.)
0.8341
0.8357
0.8640
0.8256
0.8721∗
0.8814∗
0.8747∗∗
0.8875∗∗
0.8594∗∗∗
+Language Steering (Ko.)
0.8367
0.8479
0.8660
0.8354
0.8682∗
0.8844
0.8786∗∗∗
0.8932∗∗
0.8638∗∗∗
Few-shot Steering (En.)
0.8313
0.8591
0.8646
0.8405
0.8700∗
0.8718
0.8831∗∗∗
0.8637
0.8605∗∗∗
+Language Steering (Ko.)
0.8531∗
0.8749∗∗
0.8790
0.8441
0.8857∗∗
0.8960∗
0.8953∗∗∗
0.9019∗∗∗
0.8788∗∗∗
Russia (Russian)
No Steering (En.)
0.8421
0.8415
0.8644
0.8414
0.8640
0.8862
0.8569
0.8780
0.8593
+Language Steering (Ru.)
0.8347
0.8682∗
0.8776
0.8408
0.8977∗∗
0.9103∗∗
0.9001∗∗∗
0.8880
0.8772∗∗∗
Persona Steering (En.)
0.8495
0.8513
0.8854
0.8578
0.8953∗∗
0.9180∗∗∗
0.8978∗∗∗
0.9018∗
0.8821∗∗∗
+Language Steering (Ru.)
0.8668∗
0.8729∗∗
0.8895∗
0.8344
0.9002∗∗∗
0.8976
0.9129∗∗∗
0.9084∗∗∗
0.8853∗∗∗
Few-shot Steering (En.)
0.8562
0.8801∗∗∗
0.8865
0.8700∗
0.8936∗∗
0.9172∗∗∗
0.9058∗∗∗
0.8939
0.8879∗∗∗
+Language Steering (Ru.)
0.8699∗
0.8874∗∗∗
0.8947∗∗
0.8457
0.9095∗∗∗
0.9247∗∗∗
0.9084∗∗∗
0.8975∗
0.8922∗∗∗
Viet Nam (Vietnamese)
No Steering (En.)
0.8105
0.7992
0.8094
0.8019
0.8179
0.8111
0.8078
0.8164
0.8093
+Language Steering (Vi.)
0.8129
0.8364∗∗
0.8487∗∗
0.8062
0.8523∗∗
0.8407∗
0.8489∗∗∗
0.8496∗∗
0.8370∗∗∗
Persona Steering (En.)
0.8070
0.8078
0.7987
0.7975
0.8235
0.8337
0.8227
0.8253
0.8145
+Language Steering (Vi.)
0.8100
0.8382∗∗
0.8408∗
0.8114
0.8612∗∗∗
0.8544∗∗∗
0.8481∗∗
0.8525∗∗
0.8396∗∗∗
Few-shot Steering (En.)
0.7961
0.8498∗∗∗
0.8190
0.8218
0.8470∗
0.8450∗
0.8444∗
0.8396
0.8328∗∗∗
+Language Steering (Vi.)
0.8443∗∗
0.8668∗∗∗
0.8718∗∗∗
0.8411∗∗
0.8808∗∗∗
0.8713∗∗∗
0.8854∗∗∗
0.8674∗∗∗
0.8661∗∗∗
Brazil (Portuguese)
No Steering (En.)
0.8294
0.8455
0.8693
0.8288
0.8606
0.8834
0.8529
0.8655
0.8544
+Language Steering (Pt.)
0.8450
0.8557
0.8791
0.8453
0.8914∗∗∗
0.8753
0.8882∗∗∗
0.8828
0.8704∗∗∗
Persona Steering (En.)
0.8583∗
0.8380
0.8820
0.8422
0.8855∗∗
0.8983
0.8792∗∗
0.8815
0.8706∗∗∗
+Language Steering (Pt.)
0.8552
0.8680∗
0.8885∗
0.8489
0.8992∗∗∗
0.8878
0.8945∗∗∗
0.8872∗
0.8787∗∗∗
Few-shot Steering (En.)
0.8518
0.8777∗∗
0.8842
0.8696∗∗∗
0.8879∗∗
0.9047∗
0.8964∗∗∗
0.8805
0.8816∗∗∗
+Language Steering (Pt.)
0.8569∗
0.8755∗∗
0.8869
0.8720∗∗∗
0.8995∗∗∗
0.9049∗∗
0.8987∗∗∗
0.8939∗
0.8860∗∗∗
Argentina (Spanish)
No Steering (En.)
0.8392
0.8397
0.8698
0.8310
0.8694
0.8943
0.8579
0.8766
0.8597
+Language Steering (Es.)
0.8349
0.8518
0.8764
0.8138
0.8890∗
0.8953
0.8868∗∗
0.8912
0.8674
Persona Steering (En.)
0.8294
0.8429
0.8774
0.8248
0.8869
0.9101
0.8804∗
0.8929
0.8681∗
+Language Steering (Es.)
0.8540
0.8628
0.8874∗
0.8303
0.8896∗
0.9063
0.8921∗∗∗
0.8980∗
0.8776∗∗∗
Few-shot Steering (En.)
0.8612
0.8627
0.8984∗
0.8483∗∗
0.9021∗∗∗
0.9153∗∗
0.9052∗∗∗
0.8947
0.8860∗∗∗
+Language Steering (Es.)
0.8546
0.8684
0.8983∗∗
0.8267∗∗
0.8999∗∗
0.9080
0.9099∗∗∗
0.8985∗
0.8830∗∗∗
Chile (Spanish)
No Steering (En.)
0.8627
0.8728
0.8936
0.8570
0.8830
0.9051
0.8798
0.8937
0.8810
+Language Steering (Es.)
0.8508
0.8824
0.8985
0.8444
0.9074∗∗
0.9044
0.9076∗∗
0.9033
0.8874
Persona Steering (En.)
0.8561
0.8836
0.9040
0.8486
0.9090∗∗
0.9152
0.9054∗∗
0.9091
0.8914∗∗
+Language Steering (Es.)
0.8634
0.8929∗
0.9047
0.8556
0.9120∗∗∗
0.9132
0.9111∗∗∗
0.9012
0.8943∗∗∗
Few-shot Steering (En.)
0.8757
0.8987∗∗
0.9075
0.8607
0.9141∗∗∗
0.9230∗
0.9150∗∗∗
0.8989
0.8992∗∗∗
+Language Steering (Es.)
0.8660
0.9019∗∗∗
0.9020
0.8569
0.9177∗∗∗
0.9210∗
0.9198∗∗∗
0.9116∗
0.8996∗∗∗
Uruguay (Spanish)
No Steering (En.)
0.8475
0.8607
0.8766
0.8322
0.8767
0.8893
0.8595
0.8639
0.8633
+Language Steering (Es.)
0.8389
0.8592
0.8744
0.8222
0.8858
0.8831
0.8769
0.8711
0.8640
Persona Steering (En.)
0.8466
0.8584
0.8797
0.8219
0.8742
0.8946
0.8810∗
0.8900∗∗
0.8683
+Language Steering (Es.)
0.8534
0.8648
0.8802
0.8345
0.8823
0.8950
0.8797∗
0.8898∗∗
0.8725∗∗
Few-shot Steering (En.)
0.8564
0.8642
0.8849
0.8267
0.8853
0.9050
0.8850∗∗
0.8804
0.8735∗∗
+Language Steering (Es.)
0.8513
0.8709
0.8899
0.8286
0.8921
0.8989
0.8854∗∗
0.8923∗∗∗
0.8762∗∗∗
Table 9: The alignment scores between Japan, Korea, Russia, Viet Nam, Brazil, Argentina, Chile, and Uruguay and LLMs
under different steering methods. The content in “()” is to indicate the language being used, where “En.” denotes English, “Ja.”
denotes Japanese, “Ko.” denotes Korean, “Ru.” denotes Russian, ‘Vi.” denotes Vietnamese, ‘Pt.” denotes Portuguese, and ‘Es.”
denotes Spanish. In all settings, our input always keeps single language. Moreover, the significance is assessed using the t-test:
* denotes p-value < 0.05, ** denotes p-value < 0.01, and *** denotes p-value < 0.001.

--- Page 23 ---

Models
Countries (or Regions)
Qwen2.5
Australia, Germany, Japan, Netherlands, New Zealand,
South Korea, United States, Uruguay
Llama3
Australia, Germany, Japan, Netherlands, New Zealand
GPT-4
Australia, Germany, Netherlands, New Zealand, United
States, Uruguay
GPT-5
Argentina, Hong Kong, Japan, South Korea, Taiwan,
Uruguay
DeepSeek-R1
Australia, Germany, Hong Kong, Japan, Netherlands,
New Zealand, United States
Table 10: Filtered countries for each LLM.
Topic
Question
Options
Gender
Fairness
Q29: Do you agree that, on the
whole, men make better political
leaders than women do?
1. Strongly agree 2. Agree
3. Disagree 4. Strongly dis-
agree
Q30: Do you agree that a university
education is more important for a
boy than for a girl?
1. Strongly agree 2. Agree
3. Disagree 4. Strongly dis-
agree
Q31: Do you agree that, on the
whole, men make better business
executives than women do?
1. Strongly agree 2. Agree
3. Disagree 4. Strongly dis-
agree
Q33: Do you agree that when jobs
are scarce, men should have more
right to a job than women?
1. Strongly agree 2. Agree
3. Neither agree nor disagree
4. Disagree 5. Strongly dis-
agree
Atheism
Q165: Do you believe in God?
1. Yes 2. No
Q166: Do you believe in life after
death?
1. Yes 2. No
Q167: Do you believe in hell?
1. Yes 2. No
Q168: Do you believe in heaven?
1. Yes 2. No
Democracy
Q243: How essential do you think it
is as a characteristic of democracy
that people choose their leaders in
free elections?
1. Not an essential char-
acteristic of democracy 10.
An essential characteristic
of democracy
Q250: How important is it for you
to live in a country that is governed
democratically?
1. Not at all important 10.
Absolutely important
Table 11: The questions we selected for studying the internal consistency of LLMs.

--- Page 24 ---

Method
0.5B
1.5B
3B
7B
14B
72B
AVG.
China
No Steering (En.)
0.7193
0.7569
0.7614
0.7960
0.8156
0.8273
0.7794
+Language Steering (Zh.)
0.7059
0.7427
0.7723
0.8173
0.8428
0.8439
0.7875
Persona Steering (En.)
0.7211
0.7627
0.7569
0.7990
0.8249
0.8316
0.7827
+Language Steering (Zh.)
0.7024
0.7560
0.7736
0.8183
0.8586∗∗
0.8629∗
0.7953∗
Few-shot Steering (En.)
0.7341
0.7808
0.8072∗∗
0.8143
0.8493
0.8596
0.8076∗∗∗
+Language Steering (Zh.)
0.7346
0.7751
0.7934
0.8357∗
0.8754∗∗∗
0.8838∗∗∗
0.8163∗∗∗
Germany
No Steering (En.)
0.7356
0.7680
0.7398
0.8227
0.8597
0.8541
0.7967
+Language Steering (De.)
0.7331
0.7620
0.7761
0.8022
0.8469
0.8815∗∗
0.8803
Persona Steering (En.)
0.7416
0.7757
0.7418
0.8244
0.8672
0.8596
0.8217
+Language Steering (De.)
0.7431
0.7630
0.7898∗∗
0.8086
0.8552
0.8904∗∗∗
0.8084
Few-shot Steering (En.)
0.7189
0.7531
0.7730
0.8200
0.8534
0.8619
0.7967
+Language Steering (De.)
0.7509
0.7605
0.7808∗
0.8200
0.8746
0.8916∗∗∗
0.8131∗
Table 12: Culture representation scores for China and Germany under different steering methods for LLMs. The content in
“()” is to indicate the language being used, where “En.” denotes English, “Zh.” denotes Chinese, and “De.” denotes German.
In all cases, the language of our inputs (task instruction, few-shot examples, and question) always keeps the same. Moreover,
the significance is assessed using the t-test: * denotes p-value < 0.05, ** denotes p-value < 0.01, and *** denotes p-value <
0.001.

--- Page 25 ---

Wave 5
Wave 6
Wave 7
0.80
0.85
Llama3
Wave 5
Wave 6
Wave 7
0.80
0.85
Qwen2.5
Wave 5
Wave 6
Wave 7
0.825
0.850
0.875
GPT-4
Wave 5
Wave 6
Wave 7
0.80
0.85
0.90
GPT-5
Wave 5
Wave 6
Wave 7
0.80
0.85
0.90
DeepSeek-R1
Figure 21: The trend of the average alignment scores of
LLMs with countries across waves. The sahed area indicates
the standard deviation of the alignment scores at the current
wave.
Alignment
NMAE
JSD
Alignment
1
0.9150
0.8757
NMAE
1
0.9390
JS div
1
Table 13: Pearson’s r between different matrics on Aya-23-
35B.
Alignment
NMAE
JSD
Alignment
1
0.8696
0.8584
NMAE
1
0.8920
JS div
1
Table 14: Pearson’s r between different matrics on Llama3-
70B-Instruct.
Alignment
NMAE
JSD
Alignment
1
0.9102
0.9040
NMAE
1
0.8921
JS div
1
Table 15: Pearson’s r
between different matrics on
Qwen2.5-72B-Instruct.
Alignment
NMAE
JSD
Alignment
1
0.9287
0.9259
NMAE
1
0.8751
JS div
1
Table 16: Pearson’s r between different matrics on GPT-3.5-
Turbo.
Alignment
NMAE
JSD
Alignment
1
0.9125
0.9113
NMAE
1
0.9268
JS div
1
Table 17: Pearson’s r between different matrics on GPT-4.
Alignment
NMAE
JSD
Alignment
1
0.9244
0.9294
NMAE
1
0.9362
JS div
1
Table 18: Pearson’s r between different matrics on GPT-5.
Alignment
NMAE
JSD
Alignment
1
0.9094
0.9195
NMAE
1
0.8975
JS div
1
Table 19: Pearson’s r
between different matrics on
DeepSeek-V3.
Alignment
NMAE
JSD
Alignment
1
0.8898
0.9245
NMAE
1
0.9004
JS div
1
Table 20: Pearson’s r
between different matrics on
DeepSeek-R1.

--- Page 26 ---

Andorra
Argentina
Armenia
Australia
Bangladesh
Bolivia
Brazil
Canada
Chile
China
Colombia
Cyprus
Czech Republic
Germany
Ecuador
Egypt
Ethiopia
Great Britain
Greece
Guatemala
Hong Kong
Indonesia
India
Iran
Iraq
Jordan
Japan
Kazakhstan
Kenya
Kyrgyzstan
South Korea
Lebanon
Libya
Macao SAR
Morocco
Maldives
Mexico
Myanmar
Mongolia
Malaysia
Nigeria
Nicaragua
Northern Ireland
Netherlands
New Zealand
Pakistan
Peru
Philippines
Puerto Rico
Romania
Russia
Singapore
Serbia
Slovakia
Thailand
Tajikistan
Tunisia
Turkey
Taiwan
Ukraine
Uruguay
United States
Uzbekistan
Venezuela
Viet Nam
Zimbabwe
Aya23 (LLM)
Qwen2.5 (LLM)
Llama3 (LLM)
GPT-3.5 (LLM)
GPT-4 (LLM)
GPT-5 (LLM)
DeepSeek-V3 (LLM)
DeepSeek-R1 (LLM)
Andorra
Argentina
Armenia
Australia
Bangladesh
Bolivia
Brazil
Canada
Chile
China
Colombia
Cyprus
Czech Republic
Germany
Ecuador
Egypt
Ethiopia
Great Britain
Greece
Guatemala
Hong Kong
Indonesia
India
Iran
Iraq
Jordan
Japan
Kazakhstan
Kenya
Kyrgyzstan
South Korea
Lebanon
Libya
Macao SAR
Morocco
Maldives
Mexico
Myanmar
Mongolia
Malaysia
Nigeria
Nicaragua
Northern Ireland
Netherlands
New Zealand
Pakistan
Peru
Philippines
Puerto Rico
Romania
Russia
Singapore
Serbia
Slovakia
Thailand
Tajikistan
Tunisia
Turkey
Taiwan
Ukraine
Uruguay
United States
Uzbekistan
Venezuela
Viet Nam
Zimbabwe
Aya23 (LLM)
Qwen2.5 (LLM)
Llama3 (LLM)
GPT-3.5 (LLM)
GPT-4 (LLM)
GPT-5 (LLM)
DeepSeek-V3 (LLM)
DeepSeek-R1 (LLM)
0.75
0.80
0.85
0.90
0.95
1.00
Figure 22: A full version of the alignment score heatmap between countries and LLMs. The source code for plotting this figure
is located in the show results folder.

--- Page 27 ---

0.5B
1.5B
3B
7B
14B
72B
0.700
0.725
0.750
0.775
0.800
0.825
0.850
0.875
0.900
Alignment Score
Figure 23: The alignment score of Qwen 2.5 models of different sizes with each country, where each point represents a country
and the black line represents the average alignment score of all countries.

--- Page 28 ---

0.86
0.88
0.90
0.92
0.94
Alignment Score with Average Religious Opinions
0.86
0.88
0.90
0.92
0.94
Alignment Score with DeepSeek-R1
Roman Catholic
Protestant
Orthodox
Jew
Muslim
Hindu
Buddhist
y = x
Figure 24: Religion as the baseline.
0.86
0.87
0.88
0.89
0.90
Alignment Score with Average North American Opinions
0.86
0.87
0.88
0.89
0.90
Alignment Score with DeepSeek-R1
Canada
Guatemala
Mexico
Puerto Rico
United States
y = x
Figure 25: Region (America) as the baseline.
0.84
0.86
0.88
0.90
0.92
Alignment Score with Average European Opinions
0.84
0.86
0.88
0.90
0.92
Alignment Score with DeepSeek-R1
Andorra
Cyprus
Czech Republic
Germany
Greece
Netherlands
Romania
Russia
Slovakia
Turkey
Ukraine
Great Britain
Serbia
Northern Ireland
y = x
Figure 26: Region (Europe) as the baseline.

```
