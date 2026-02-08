---
title: "2026-Kratzke-PSYCH Psychometric Assessment of LLM Characters - PDF Extract"
source_pdf: "2026-Kratzke-PSYCH Psychometric Assessment of LLM Characters.pdf"
pages: 35
extracted_at: "2026-02-08T06:02:21.729355"
---

# PDF Extract: 2026-Kratzke-PSYCH Psychometric Assessment of LLM Characters

**Source PDF:** 2026-Kratzke-PSYCH Psychometric Assessment of LLM Characters.pdf
**Total Pages:** 35

---

## Content

```
--- Page 1 ---

Academic Editors: Carson K. Leung,
Oluwaseun Ajao, Bayode Ogunleye
and Hemlata Sharma
Received: 25 November 2025
Revised: 23 December 2025
Accepted: 31 December 2025
Published: 6 January 2026
Copyright: © 2026 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license.
Article
PSYCH—Psychometric Assessment of Large Language Model
Characters: An Exploration of the German Language
Nane Kratzke 1,*
, Niklas Beuter 2
, André Drews 2
and Monique Janneck 1
1
Institute for Interactive Systems, Technische Hochschule Lübeck, 23562 Lübeck, Germany;
monique.janneck@th-luebeck.de
2
Expert Group Artificial Intelligence in Applications, Technische Hochschule Lübeck, 23562 Lübeck, Germany;
niklas.beuter@th-luebeck.de (N.B.); andre.drews@th-luebeck.de (A.D.)
*
Correspondence: nane.kratzke@th-luebeck.de
Abstract
Background: Existing evaluations of large language models (LLMs) largely emphasize
linguistic and factual performance, while their psychometric characteristics and behav-
ioral biases remain insufficiently examined, particularly beyond English-language contexts.
This study presents a systematic psychometric screening of LLMs in German using the
validated Big Five Inventory-2 (BFI-2). Methods: Thirty-two contemporary commercial
and open-source LLMs completed all 60 BFI-2 items 60 times each (once with and once
without having to justify their answers), yielding over 330,000 responses. Models answered
independently, under male and female impersonation, and with and without required
justifications. Responses were compared to German human reference data using Welch’s
t-tests (p < 0.01) to assess deviations, response stability, justification effects, and gender
differences. Results: At the domain level, LLM personality profiles broadly align with
human means. Facet-level analyses, however, reveal systematic deviations, including
inflated agreement—especially in Agreeableness and Aesthetic Sensitivity—and reduced
Negative Emotionality. Only a few models show minimal deviations. Justification prompts
significantly altered responses in 56% of models, often increasing variability. Commercial
models exhibited substantially higher response stability than open-source models. Gender
impersonation affected up to 25% of BFI-2 items, reflecting and occasionally amplifying
human gender differences. Conclusions: This study introduces a reproducible psycho-
metric framework for benchmarking LLM behavior against validated human norms and
shows that LLMs produce stable yet systematically biased personality-like response pat-
terns. Psychometric screening could therefore complement traditional LLM evaluation in
sensitive applications.
Keywords: large language models; psychometric evaluation; Big Five Inventory-2;
LLM personality profiles; behavioral bias; response stability; justification effects; gender
impersonation; German; human-AI comparison; trustworthy AI; responsible AI
1. Introduction
The increasing integration of large language models (LLMs) such as GPT, Llama,
Grok, Mistral, Gemini, and many more large language models into diverse real-world
workflows demands a clear understanding of their psychological and behavioral char-
acteristics [1]. Indeed, psychological profiling of language models is pertinent wherever
LLMs are involved in sensitive social exchanges, decision support, or contexts requiring a
Analytics 2026, 5, 5
https://doi.org/10.3390/analytics5010005

--- Page 2 ---

Analytics 2026, 5, 5
2 of 35
nuanced understanding of human affect and value systems. E.g., the growing prevalence
of AI-generated content makes distinguishing between human and machine-produced
texts increasingly challenging. Analyzing the psychological profiles of LLMs might of-
fer a promising approach to detecting subtle stylistic and cognitive patterns indicative
of deepfakes.
Applications that stand to benefit from systematic psychological screening of LLMs
include, for example, mental health support chatbots [2], digital HR and recruiting tools [3],
customer service systems in critical industries, and AI-driven moderation for social plat-
forms or public services [4] as well as educational settings [5].
In all these settings,
the model’s “character” and its alignment with human values, emotional sensitivity, and po-
tential (unnoticed) biases may have significant impacts—ranging from a subtle influence
on user behavior to overt risks involving fairness, inclusivity, or user well-being. Until now,
the evaluation of large language models has primarily focused on their linguistic com-
petence and factual accuracy [6]. However, recent studies emphasize the importance of
more holistic evaluation approaches [7], as well as agentic approaches and their psycho-
metric impacts [8]. For example, psychometric methods such as established personality
inventories could be used to systematically analyze the behavior of language models and
reveal differences from human response patterns. The Big Five Inventory 2 (BFI-2) offers a
robust and validated framework for assessing the core domains of personality and is thus a
promising tool for LLM characterization [9]. Many previous studies exhibit methodological
weaknesses, linguistic and cultural particularities, or a lack of validation against human
standards. According to our research, only some studies [10] intentionally had LLMs
complete a Big Five questionnaire. According to [10] language models display a response
behavior similar to that of humans, with GPT-3 deviating more strongly than GPT-4. This
indicates the need for more detailed analyses. For example, most studies are conducted
for the English language, which often means that specific requirements and differences of
other language areas are insufficiently taken into account. The same is true for the training
of LLMs. A large amount of training data is available only in English [11].
In other words, there is a lack of validated, psychometrically grounded, and mul-
tilingual research that systematically compares the response behavior of large language
models to human reference data using established personality inventories and method-
ologies. To address this gap, this paper makes several key contributions to the emerging
field of psychometric large language model evaluation: (1) It introduces a systematic,
repeated-measures methodology for psychological screening of LLMs using the German
BFI-2. A validated personality inventory with robust human reference data. (2) By an-
alyzing 32 current LLMs across both commercial and open-source providers, the study
offers the first comprehensive cross-model comparison of personality traits in the German
language context. (3) The effects of gender impersonation and answer justification on LLM
response patterns are explicitly investigated and quantified, revealing previously unstudied
forms of model bias and instability. (4) A robust statistical framework based on Welch’s
t-tests enables rigorous benchmarking of LLM answers against human norms, uncovering
systematic deviations as well as model-specific behavioral tendencies. Together, these con-
tributions provide novel insights into the behavioral consistency, human-likeness, and bias
susceptibility of state-of-the-art LLMs, and contribute to methodological foundations for
future psychometric LLM evaluations.
The following research questions guided our study:
•
RQ1: Can differences be found in the personality profiles of specific model developers
(e.g., due to the selection of training data and the implementation of constraints, which
are often influenced by the developers’ personal, business, cultural, or even political
worldview backgrounds)?
https://doi.org/10.3390/analytics5010005

--- Page 3 ---

Analytics 2026, 5, 5
3 of 35
•
RQ2: Do language models respond like humans in personality tests? And if not, what
are the differences?
•
RQ3: Does requiring language models to justify their answers impact their responses?
•
RQ4: How consistent are language models in providing the same answer when
identical questions are asked multiple times?
•
RQ5: Do language models respond differently when impersonating a female or male
individual?
By systematically screening a broad array of state-of-the-art language models, PSYCH
aims to identify critical behavioral patterns, divergences, and sources of bias in LLM-
generated personality profiles. The findings are intended to contribute to the development
of psychometrically robust, responsible, and transparent AI evaluation standards. The
remainder of this paper is organized as follows: Section 2 reviews related work and sit-
uates this study within the existing literature on psychometric AI evaluation. Section 3
details our methodology, including the experimental protocols, data collection procedures,
and statistical analysis. Section 4 presents the results for each of the outlined research
questions, highlighting key findings and observed patterns. Section 5 discusses the im-
plications of our findings, addresses potential threats to validity, and outlines limitations.
Finally, Section 6 concludes the paper and provides an outlook on future research directions.
Appendices A–E helps readers trace the model-specific details of all analyzed language
models and comprises all necessary information, including code, prompts, and language
model-specific or model-comparative evaluations. At the same time, the main part of this
paper focuses on general results applicable to all examined language models.
2. Related Work
The rapid deployment and increasing complexity of large language models (LLMs)
have fueled a growing need to characterize their behavioral and psychological tendencies
beyond traditional language benchmarks. Instead of providing a detailed account of
these developments, we refer to the excellent review article by [1]. In the following, we
merely provide a brief overview of the field of research, which has now begun to apply
psychometric approaches from human psychology to the evaluation of AI systems.
Personality Assessment in Language Models (RQ1, RQ2): A substantial body of
recent work adapts established personality inventories, most notably the Big Five Inventory
(BFI), for LLM evaluation [1,12]. For example, the study [13] examines the extent to which
a large language model (GPT-4) is capable of realistically simulating people with different
personality profiles (“role-play”) and imitating their responses in questionnaires as well as
their behavioral aspects. This enables new application possibilities, such as in simulation-
based research (e.g., agents in social simulation models), personalized AI interaction
systems, or virtual characters with differentiated personality traits. Most of these studies
prompt models to complete human-oriented personality questionnaires, then score the
responses according to standard psychometric practices. Results have shown that LLMs can
generate personality profiles which are both stable across repeated runs and, under certain
conditions, comparable to human data distributions [1,14]. However, model-generated
profiles frequently display reduced variance and inflated mean scores [12,15].
Advances and Limitations in Methodology (RQ3, RQ4): Several studies have pro-
posed methodological innovations such as automated scoring based on model embed-
dings [16], open-ended question formats, or adaptation to cross-cultural settings [17].
Embedding-based approaches in particular can capture subtle psycholinguistic features and
have been shown to outperform traditional zero-shot strategies in predictive consistency
and trait inference [15]. Yet, most prior works lack rigorous internal validity checks (e.g.,
https://doi.org/10.3390/analytics5010005

--- Page 4 ---

Analytics 2026, 5, 5
4 of 35
split-half or test-retest reliability) and rarely benchmark against comprehensive ground
truth data from validated human samples.
Bias and Perspective Analyses in LLMs (RQ5): A handful of studies have addressed
gender and cultural bias by prompting models from diverse perspectives or administering
localized inventory variants [14,18]. These works highlight that while LLMs can reproduce
broad patterns of cross-cultural or gender difference, their simulated variability is often
lower than in empirical human data and may reflect learned stereotypes or dataset artifacts.
Evaluation of social or gender bias remains inconsistent and rarely incorporates systematic,
psychometrically sound validation techniques.
Psychometric Validation Practices (RQ3, RQ4, RQ5): Reliability metrics such as Cron-
bach’s alpha are beginning to appear in the evaluation of LLM response consistency [15],
while some studies have correlated LLM-inferred traits with linguistic or emotional fea-
tures of generated text to examine convergent validity. However, only a minority employ
confirmatory or exploratory factor analysis to assess whether LLM response patterns
genuinely replicate canonical personality trait structures as observed in humans [12,19].
Systematic statistical comparison with human baseline distributions—using metrics such
as t-tests—is still largely absent from the literature although it seems to be one of the most
obvious approaches.
Gaps and Rationale for PSYCH: Despite these advances, significant limitations persist:
most existing methods (a) focus on single-perspective assessments, (b) address bias in a
piecemeal fashion, and (c) lack comprehensive, repeated-measures or independent-answer
protocols. Moreover, almost no published work investigates the effects of requiring LLMs to
justify their answers or self-reflect, leaving open questions about the impact of reasoning or
introspection on response stability. Our work builds directly on this foundation, introducing
the PSYCH methodology to offer (1) gender-balanced and perspective-diverse assessment,
(2) repeated and independent measurement protocols, (3) robust statistical comparison
with human data, and (4) an explicit investigation of the effect of answer justification on
LLM personality response patterns. This comprehensive approach aims to address the
central methodological and interpretive gaps documented in the current literature.
3. Methods
We use the German version of the Big Five Inventory 2 (BFI-2) as explained by [9] and
shown in Table 1. The BFI-2 is a structured questionnaire consisting of 60 items that assess
the five major personality dimensions and three specific facets for each. The validation of
the BFI-2 was conducted using exploratory and confirmatory factor analyses, reliability
calculations (Cronbach’s alpha, McDonald’s omega), examination of construct and criterion
validity, as well as tests of measurement invariance. The results indicate reliable and valid
scales that are suitable for group comparisons.
The BFI-2 also provides a “Ground Truth,” which we use in this study as a reference
point to determine whether a language model generates responses that are distinguishable
from this “Ground Truth.” This “Ground Truth” is presented in Table 2 and is reported
by [9]. The corresponding standard deviations (SD) are shown in parentheses.
To determine whether the responses generated by the language model differed signifi-
cantly from the human ground truth, we applied Welch’s t-test. Group differences were
evaluated using Welch’s t-tests with a significance threshold of p < 0.01. Welch’s test was
chosen because it does not assume equal variances and is more robust to unequal group
sizes, which are common in questionnaire-based personality research. A more conservative
alpha level (p < 0.01 rather than the more commonly used p < 0.05) was selected for
several reasons. First, this threshold is consistent with analytical practices used in the
development and validation of the BFI-2, thereby improving comparability with prior
https://doi.org/10.3390/analytics5010005

--- Page 5 ---

Analytics 2026, 5, 5
5 of 35
research. Second, multiple personality dimensions and facets were examined, increasing
the risk of false-positive errors; a stricter significance criterion provides pragmatic con-
trol over false-positive findings. Third, given the sample size, smaller effects may reach
statistical significance; using a lower alpha level helps to emphasize more robust and
substantively meaningful effects. Alternative approaches, such as the classical Student’s
t-test, non-parametric tests, or formal multiple-comparison corrections (e.g., Bonferroni),
were considered. However, Welch’s t-test combined with a stricter alpha level represents
a balanced and widely recommended compromise between robustness, statistical power,
and interpretability.
Table 1. Overview of the Five Major Personality Dimensions, Their Facets, and Corresponding
Descriptions according to the Five-Factor Model (Big Five Personality Traits).
Dimension
Facet
Description
Extraversion
Sociability
Enjoyment of social interactions and being with others
Assertiveness
Tendency to be talkative, take charge, and express oneself confidently
Energy Level
Tendency to be energetic, active, and enthusiastic
Agreeableness
Compassion
Tendency to feel and express concern and sympathy for others
Respectfulness
Tendency to treat others with respect and consideration
Trust
Tendency to believe in the honesty and good intentions of others
Conscientiousness
Organization
Tendency to be neat, orderly, and well-prepared
Productiveness
Tendency to be efficient, hard-working, and persistent
Responsibility
Tendency to be reliable, dependable, and to fulfill commitments
Negative
Anxiety
Proneness to worry, nervousness, and fear
Emotionality
Depression
Tendency to experience feelings of sadness, hopelessness, or discouragement
Emotional Volatility
Tendency to experience frequent mood changes and difficulty controlling emotions
Open-Mindedness
Intellectual Curiosity
Tendency to seek out new knowledge and enjoy thinking about complex topics
Aesthetic Sensitivity
Appreciation for art, music, beauty, and sensory experiences
Creative Imagination
Tendency to have a vivid imagination and enjoy creative pursuits
Table 2. Ground Truth: Mean Scores (and Standard Deviations) for Personality Facets, Women, and
Men Based on the Five-Factor Model Dimensions (sample of the German-speaking population; [9]).
Facet
Total Sample (N = 770)
Women (N = 396)
Men (N = 374)
Extraversion
3.22 (0.63)
3.26 (0.65)
3.18 (0.61)
- Sociability
3.20 (0.83)
3.32 (0.85)
3.08 (0.79)
- Assertiveness
3.20 (0.75)
3.12 (0.76)
3.28 (0.73)
- Energy Level
3.27 (0.70)
3.34 (0.71)
3.19 (0.69)
Agreeableness
3.76 (0.51)
3.87 (0.49)
3.65 (0.49)
- Compassion
3.95 (0.65)
4.13 (0.61)
3.77 (0.64)
- Respectfulness
4.08 (0.59)
4.17 (0.59)
3.99 (0.58)
- Trust
3.25 (0.65)
3.31 (0.66)
3.20 (0.64)
Conscientiousness
3.67 (0.62)
3.73 (0.61)
3.60 (0.62)
- Organization
3.71 (0.85)
3.73 (0.84)
3.68 (0.87)
- Productiveness
3.53 (0.73)
3.62 (0.73)
3.43 (0.72)
- Responsibility
3.76 (0.60)
3.84 (0.57)
3.68 (0.62)
Negative Emotionality
2.72 (0.67)
2.79 (0.68)
2.64 (0.65)
- Anxiety
2.96 (0.70)
3.07 (0.70)
2.83 (0.68)
- Depression
2.56 (0.85)
2.59 (0.87)
2.53 (0.83)
- Emotional Volatility
2.63 (0.78)
2.70 (0.80)
2.56 (0.76)
Open-Mindedness
3.38 (0.64)
3.42 (0.64)
3.34 (0.62)
- Aesthetic Sensitivity
3.11 (0.96)
3.23 (0.94)
2.97 (0.97)
- Intellectual Curiosity
3.48 (0.68)
3.47 (0.68)
3.50 (0.67)
- Creative Imagination
3.56 (0.77)
3.56 (0.79)
3.56 (0.75)
https://doi.org/10.3390/analytics5010005

--- Page 6 ---

Analytics 2026, 5, 5
6 of 35
What is more, Welch’s t-test are appropriate when comparing the means of two
independent samples with potentially unequal variances and sample sizes. We treated
the responses from the language model and those from the human participants (“Ground
Truth”) as two separate groups. For each group, we computed the sample mean and
variance. The Welch t-statistic was then calculated as follows and where x1 and x2 denote
the means of the language model and human groups, s2
1 and s2
2 denote their respective
sample variances, and n1 and n2 represent the sample sizes.
t =
x1 −x2
r
s2
1
n1 + s2
2
n2
(1)
The degrees of freedom for the test were estimated using the Welch–Satterthwaite
equation:
d f =

s2
1
n1 + s2
2
n2
2
(s2
1/n1)2
n1−1
+ (s2
2/n2)2
n2−1
(2)
To assess significance, we calculated the two-tailed p-value using the cumulative
distribution function (CDF) of the t distribution with the determined degrees of freedom
where Ft,d f denotes the CDF of the t distribution with d f degrees of freedom, evaluated at
the absolute value of the computed t statistic.
p = 2 ·
h
1 −Ft,d f (|t|)
i
(3)
We interpreted a p value less than 0.01 as evidence of a statistically significant dif-
ference between the means of the language model and the human ground truth. This
procedure allowed us to rigorously test whether the language model’s performance aligned
with, or diverged significantly from human responses. In total, we analyzed 32 language
models (see Table 3). To enable a comprehensive screening analysis of language mod-
els, the following selection criteria were applied to ensure a representative and diverse
landscape of language models, providing a solid foundation for robust and generalizable
insights in the screening analysis.
•
Coverage of Key Providers: Models from all major, up-to-date providers (Alibaba,
Anthropic, DeepSeek, Google, OpenAI, xAI, Meta, Mistral) were included to reflect
diverse model architectures, training data, and provider strategies.
•
Model Variety per Provider: Multiple models per provider were chosen to capture
differences between generations, sizes, and types (e.g., Turbo, Sonnet, Mini versions).
This allows for comparison between flagship models and more lightweight alternatives.
•
Response Volume and Balance: Each model was expected to generate approximately
3600 responses (balanced for male/female perspectives), ensuring sufficient data for
robust statistical analysis and subgroup comparisons.
•
Self-Hosting Status: Both self-hostable (open-source) and closed-source/cloud-only
models were deliberately included. This enables evaluation of openness, transparency,
and privacy/compliance considerations.
•
Recency and Relevance: The selection covers both state-of-the-art models (e.g., latest
Gemini, Claude, Qwen versions) and established open-source models (e.g., Mistral,
Llama 3) to reflect the current technology landscape.
•
Application Spectrum: By including models of various sizes and capabilities (Nano,
Mini, Large, Instruct, etc.), the analysis can address different application use cases and
deployment scenarios.
https://doi.org/10.3390/analytics5010005

--- Page 7 ---

Analytics 2026, 5, 5
7 of 35
Each of these models answered the 60 BFI-2 items 60 times independently and without
context or awareness of previous answers in order to avoid learning effects such as “Oh, I
am currently completing a psychometric test” from occurring. The questions were answered
half the time as male-impersonated agents and half the time as female-impersonated agents.
To ensure consistency and independence, the questions were repeatedly asked and each
response was given independently of previous answers. Additionally, each language model
provided each answer once without and once with an explanation, in order to investigate
whether additional steps of reflection influenced the response behavior. The answers
obtained in this way were then compared with the human ground truth shown above (see
Table 2). Using statistical tests, the language model responses and the human comparison
data are analyzed to determine in which dimensions and facets of the BFI-2 the model
exhibited significant and measurable deviations from human response behavior, in order
to statistically infer potential biases or psychological peculiarities of the respective LLMs.
The following are the key sections of our code used to control the language models.
The Langchain framework was utilized for this purpose [20]. All language models were
integrated via OpenAI API-compatible interfaces provided by the respective vendors, or,
in the case of freely available models, via https://together.ai (accessed on 24 November
2025) (see Listing 1).
Listing 1. System prompt and definition of structured responses.
# All
prompts and
answers
were
translated
into
English to improve
readability
for the
reader.
SYSTEM_PROMPT ="""
You are
participating as a randomly
selected
subject in a survey.
Below you will find a series of characteristics
that may apply to you.
For example , would you say that you enjoy
spending
time with
other
people?
Please
indicate
for each of the
following
statements
the extent to which you agree.
""".strip ()
class
AnswerWithoutReason (BaseModel):
""" Respond
only with
these
statements in a structured
form."""
answer: Literal[
"strongly
disagree", "somewhat
disagree", "neutral",
"somewhat
agree", "strongly
agree"
]
class
AnswerWithReason (BaseModel):
""" Respond
only with
these
statements in a structured
form."""
answer: Literal[
"strongly
disagree", "somewhat
disagree", "neutral",
"somewhat
agree", "strongly
agree"
]
explanation: str = Field("Brief
justification of the answer in one or two
sentences.")
To examine gender effects, we used the ten most common female and male German
first names to determine whether these lead to statistically different response distributions
(see Listing 2).
Based on these settings, each item from the BFI-2 questionnaire was posed to a lan-
guage model 60 times, each time requiring the model to answer the question in a structured
form, both with and without justification (explanation). Each language model had to
answer the items of the BFI-2 without any contextual knowledge, so the language model
https://doi.org/10.3390/analytics5010005

--- Page 8 ---

Analytics 2026, 5, 5
8 of 35
answered each item independently and was not aware that they were responding to a
psychometric questionnaire (see Listing 3).
Listing 2. Impersonation using the 10 most common German male and female names.
# The 10 most
common
German
female
first
names for female
impersonisaton
WOMANS = [
"Maria", "Ursula", "Monika", "Petra", "Elisabeth",
"Sabine", "Renate", "Helga", "Karin", "Brigitte"
]
# The 10 most
common
German
male
first
names for male
impersonisaton
MANS = [
"Peter", "Wolfgang", "Michael", "Werner", "Klaus",
"Thomas", "Manfred", "Helmut", "Juergen", "Heinz"
]
NAMES = WOMANS + MANS
Listing 3. Structured LLM Querying with Optional Reasoning and Persona Impersonation.
model = "MODEL -FROM -PROVIDER , e.g.,~gpt -4o-mini"
base_url = "BASE_URL
for
PROVIDER"
api_key = "API -KEY for~PROVIDER"
# Structured
output LLM
questioning
answer = ChatOpenAI(
model=model ,
base_url=base_url ,
api_key=api_key
). with_structured_output ( AnswerWithoutReason )
answer_with_reason = ChatOpenAI(
model=model ,
base_url=base_url ,
api_key=api_key
). with_structured_output ( AnswerWithReason )
# Impersonisation of a male or female
person by random
generator
NAME = f"Your name is { random.choice(NAMES) }.~"
# Prompt to answer
prompt = [
{ "role": "system", "content": NAME + SYSTEM_PROMPT },
{ "role": "user", "content": question.get("question") }
]
# Answering
prompt by LLM
result = answer.invoke(prompt , temperature =1.0)
# without
justification
reasoned_result = answer_with_reason .invoke(prompt , temperature =1.0)
# with
justification
The random generator ensures that approximately 50% male and 50% female names are
selected for the system prompt. Table 3 shows the exact values indicating how many male
and female impersonations were actually chosen by the random generator for each model.
https://doi.org/10.3390/analytics5010005

--- Page 9 ---

Analytics 2026, 5, 5
9 of 35
Table 3. Overview of analyzed language model providers, model names, response counts, gender-
based response distribution, and self-hosting status. Each model is expected to generate 3600 re-
sponses (1800 per male/female perspective). Deviations may occur when invalid responses are
excluded or additional valid test runs are included.
Provider
Model
Responses
f
m
Self-Hostable
Alibaba
Qwen3-235B-A22B-Instruct-2507-tput
3594
1801
1793
Yes
Qwen2.5-72B-Instruct-Turbo
3587
1789
1798
Yes
Anthropic
claude-3-5-haiku-20241022
3643
1835
1808
No
claude-3-5-sonnet-20241022
3651
1867
1784
No
claude-3-7-sonnet-20250219
3623
1837
1786
No
claude-opus-4-20250514
3596
1845
1751
No
claude-sonnet-4-20250514
3660
1842
1818
No
DeepSeek
DeepSeek-R1-Distill-Llama-70B
3699
1820
1879
Yes
DeepSeek-R1-Distill-Qwen-14B
3616
1790
1826
Yes
DeepSeek-V3
3540
1806
1734
Yes
DeepSeek-R1
3599
1802
1797
Yes
Google
gemini-2.0-flash
3597
1809
1788
No
gemini-2.0-flash-lite
3581
1827
1754
No
gemini-2.5-flash
3595
1815
1780
No
gemini-2.5-flash-lite
3594
1771
1823
No
OpenAI
gpt-4.1-mini
3600
1843
1757
No
gpt-4.1-nano
3600
1811
1789
No
gpt-4o-mini
3600
1789
1811
No
gpt-5-mini
3662
1850
1812
No
gpt-5-nano
3660
1820
1840
No
gpt-oss-20b
3582
1787
1795
Yes
gpt-oss-120b
3646
1841
1805
Yes
xAI
grok-3
3599
1797
1802
No
grok-3-fast
3600
1746
1854
No
grok-3-mini-fast
3600
1845
1755
No
Meta
Llama-3.3-70b
3598
1785
1813
Yes
Llama-4-Maverick-17B-128E-Instruct-FP8
3636
1798
1838
Yes
Llama-4-Scout-17B-16E-Instruct
3595
1881
1714
Yes
Mistral
ministral-3b-2410
3583
1847
1736
Yes
ministral-8b-2410
3600
1784
1816
Yes
mistral-medium-2505
3596
1807
1789
Yes
mistral-small-2506
3593
1824
1769
Yes
4. Results
We analyzed a variety of language models from different providers (see Table 3).
The self-hosted models were accessed via together.ai; their weight files are generally
available on Huggingface. The resulting dataset is described in Table 4. Each model was
instructed to answer all 60 questions of the BFI-2 test 60 times each. In half of the cases,
the answers were given from the perspective of a male person, and in the other half from the
perspective of a female person. The assignment of perspectives was randomized. Ideally,
this results in a total of 3600 responses per model (1800 for each perspective). In some cases,
the actual number of responses may differ slightly: If it is less than 3600, faulty answers
that did not correspond to the required structured output format and therefore could not be
processed by pydantic were excluded. A higher number is explained by short test runs to
check the evaluation logic; if their results were usable, they were included in the analysis.
https://doi.org/10.3390/analytics5010005

--- Page 10 ---

Analytics 2026, 5, 5
10 of 35
Table 4. Overview of the generated PSYCH dataset.
Category
Description
Objects of analysis
Large Language Models (LLMs)
Number of models
32
Model providers
Alibaba, Anthropic, DeepSeek, Google, OpenAI, xAI, Meta, Mistral
Model types
Commercial cloud models and self-hostable open-source models
Language
German
Psychometric instrument
Big Five Inventory-2 (BFI-2) [9]
Questionnaire structure
60 items, 5 domains, 15 facets
Response scale
5-point Likert scale
Response conditions
With justification vs. without justification; Female vs. male identity (10 most common German first
names each)
Repetitions per item
60 independent responses
Responses per model
Approximately 3600 (1800 female, 1800 male)
Total LLM responses
Over 330,000 (115,000 with and 115,000 without justified answers)
Human reference sample
N = 770 (396 female, 374 male, German population)
Statistical comparison
Welch’s t-tests (two-tailed)
Significance threshold
p < 0.01
Primary analysis focus
Deviations from human norms, response stability, justification effects,
and gender-related differences
Data collection period
23 July–14 August 2025
Dataset URL
https://doi.org/10.5281/zenodo.18002092 (accessed on 24 November 2025)
4.1. RQ1: Can Differences Be Found in the Personality Profiles of Specific Model Developers?
The question of whether AI models from different providers differ significantly is
raised repeatedly. In particular, models from xAI are often the subject of skepticism, which
is likely due to the controversial personality of the company owner, Elon Musk—a topic
that was hotly debated during the 2024 US presidential campaign. Similar concerns exist
regarding Chinese models such as those from Alibaba or DeepSeek, which are frequently
suspected of political censorship. However, such political influence is very difficult to prove
using psychometric models. In our analyses, we found no such distortions or noticeable
deviations in the personality profiles—they are all well within the completely normal range.
Figure 1 illustrates that the personality profiles of the models from different providers
essentially coincide. In the figure, the male average is shown in blue and the female
average in red (Ground Truth). Overall, the profiles correspond well with the human
reference, at least regarding the dimensions of the BFI-2. However, some models show
slight differences in certain dimensions. For example, the models from Gemini, Meta,
Mistral, and xAI rated themselves as more extroverted, agreeable, and open than human
test subjects. The models from Mistral also attested to themselves a lower level of negative
emotionality. Nevertheless, we were only able to recognize differences in details, but not in
the overall picture.
4.2. RQ2: Do LLMs Respond Like Humans in Personality Tests?
At the higher level of the BFI-2 dimensions, no significant behavioral differences were
found between the providers of language models; nevertheless, it remains unclear whether
language models respond differently to psychological test questions in detail compared
to real humans. This question was addressed in our RQ2. The responses of the language
models to the BFI-2 facet questions were compared with the responses given by humans
using a t-test, as described in [9]. Subsequently, for each model, the number of facets for
which the p-value was below 0.01 was determined and counted. As was already to be
expected based on our literature review, different models sometimes differ significantly
from human responses in their answering behavior. In extreme cases, they deviate from
humans in all facets of the BFI-2, such as Ministral 8B. However, these extreme cases are
https://doi.org/10.3390/analytics5010005

--- Page 11 ---

Analytics 2026, 5, 5
11 of 35
quite rare, and the reader is referred to Figures A1 and A2 in Appendix B for a more
detailed examination of model-specific data.
Figure 1. Comparison of personality profiles across language model providers based on the BFI-2
model. Each radar plot illustrates the average scores of models within each provider group. The red
lines indicate female humans, while the blue lines represent male humans (Ground Truth).
When we look at the individual facets of the BFI-2 and examine how many models
within each facet respond similarly or differently to human answers, the following chart
in Figure 2 emerges. It turns out that LLMs, particularly regarding aspects of aesthetic
sensitivity, often respond differently than humans, while their answers to topics such as
anxiety largely resemble human reactions. Between these extremes, a gradual transition
can be observed among the various language models examined. The analysis does not
initially provide information about whether the language model tends to express more
https://doi.org/10.3390/analytics5010005

--- Page 12 ---

Analytics 2026, 5, 5
12 of 35
or less confidence. It merely shows that the model’s statements deviate from the human
average. Compared to humans, language models show lower levels only in organization,
and depression. In the areas of trust, and aesthic sensitivity however, they tend to rate
themselves as superior. The remaining facets fall somewhere in the middle range. Language
models tend to agree with statements rather than reject them (see Figure 3).
Figure 2. Response behavior of LLMs compared to humans across individual facets of the BFI-2
personality inventory. Dark blue bars indicate facets where most models differ from human responses,
while light blue bars show facets where responses are more similar to humans. LLMs tend to diverge
most in areas like aesthetic sensitivity and intellectual curiosity, but align more closely with human
patterns on facets such as anxiety and responsibility.
Figure 3. Deviations of LLMs from the ground truth tend to express stronger agreement across most
BFI-2 personality facets. Dark blue bars indicate the amount of analyzed LLMs showing higher
agreement (“more approval”) compared to humans, while light blue bars represent lower agreement
(“less approval”).
4.3. RQ3: Does Requiring LLMs to Justify Their Answers Impact Their Responses?
To investigate this question, we compared the responses of the language models with
and without justification. If the t-test within a facet of the BFI-2 showed a significant
difference between the means of the two response groups at a p-value below 0.01, this was
taken as evidence that the justifications had a demonstrable influence on the responses. In
18 out of 32 models (approximately 56%), we observed such significant deviations when
language models were required to justify their answers (see Figure A3 in Appendix C for
model-specific data). However, the deviations do not affect all facets equally (see Figure 4).
Across all analyzed language models, deviations occur particularly frequently in the areas
of depression, and creative imagination.
https://doi.org/10.3390/analytics5010005

--- Page 13 ---

Analytics 2026, 5, 5
13 of 35
Figure 4. Detected deviations in LLM responses across BFI-2 facets when reasoning was required.
Bars show the number of models exhibiting significant changes per facet. Deviations were most
common in facets related to depression, creative imagination, and trust, indicating that reasoning
prompts can notably influence responses in these areas.
Figure 5 illustrates the differences (spreads) between justified and unjustified answers
for each model. A spread of 0 means that there was no difference between the two types of
answers. A negative spread indicates that the answer given with justification has a lower
value on the Likert scale. In contrast, a positive spread suggests that the justified answer
has a higher value on the Likert scale. Let Ljustified be the Likert value for a justified answer
(so, an answer with a requested reason from the LLM), and Lunjustified the Likert value for
an unjustified answer (so an answer without a requested reason). The reasoning spread R
is then defined as:
R = Ljustified −Lunjustified
(4)
Meaning that R = 0 denotes no difference between justified and unjustified answers,
R < 0 mean that justified answers have a lower Likert value, and R > 0 mean that justified
answers have a higher Likert value. In Figure 5, the models are sorted in descending
order according to how often they arrive at the same result for answers with and without
justification. Further down in the Figure 5 are models that more frequently provide different
answers when justification is required. Whether these differences tend to reflect a weaker
or stronger expression on the Likert scale can be seen in the bar charts on the left or right
side, respectively.
The following Figure 6 confirms that the deviations in both directions are mostly
balanced. The problem is that models with a high reasoning spread cannot easily be steered
in a desired direction, for example by prompting them to justify their answer. Especially
with smaller language models, adding justifications often leads to unpredictable behavior—
it is difficult to predict whether they will develop a tendency toward lower or higher
approval as a result. Ultimately, there seems no universally valid rule of thumb for whether
and when justifications should be used. It would probably be most honest to generally
refrain from relying on the models with high reasoning spread. That way, one would no
longer have to deal with the question of whether asking for justifications improves the
quality of the answers or not.
https://doi.org/10.3390/analytics5010005

--- Page 14 ---

Analytics 2026, 5, 5
14 of 35
Figure 5. Differences in Likert scale responses between justified and unjustified answers across
language models. Blue bars represent cases where justified responses received lower approval
ratings, while red bars indicate higher approval ratings with justification. Grey bars represent the
proportion of cases per model where no difference could be measured. The models are ordered by
how frequently their justified answers differed from non-justified ones, illustrating how reasoning
prompts can influence response intensity and expression.
Figure 6. Distribution of strong deviations (spread > 2) between justified and unjustified responses
across BFI-2 facets. Dark blue bars show cases of stronger approval with reasoning, while light
blue bars indicate lower approval. Deviations appear relatively balanced across facets, with trust,
compassion, and aesthetic sensitivity showing the largest shifts.
https://doi.org/10.3390/analytics5010005

--- Page 15 ---

Analytics 2026, 5, 5
15 of 35
4.4. RQ4: How Consistent Are Language Models in Providing Answers?
The consistency of language models in answering questions is a key criterion for their
reliability and suitability for use. In this context, consistency refers to how similar a model’s
answers are when presented with the same prompt multiple times.
Ideally, language models should provide identical or at least content-equivalent an-
swers under identical conditions. This is especially important in scientific contexts, where
users must be able to rely on the stability and reproducibility of outputs. In practice,
however, many language models exhibit a certain degree of response variance. Causes
for this include, among other things, stochastic components in the text generation process
(such as temperature parameters). To answer this question, we first counted all responses
given to a question and then calculated the proportion of the most frequently given answer
relative to the total. The result is a value between 0.0 (this answer was never chosen) and 1.0
(only this answer was chosen). We call this value the stability factor. For each model, this
stability factor was determined for each facet. To facilitate presentation, we have combined
the values of several models and indicated the average values (and standard errors) in the
following representations. Or in a more formal description: Let N be the total number of
responses to a question, and nmax the number of times the most frequently chosen answer
was given. Then, the stability factor S is defined as follows, where S ∈[0.0, 1.0] and S = 1
means that only a single answer was chosen (maximum stability). Values closer to 0 mean
that the model’s responses are more unstable.
S = nmax
N
(5)
For multiple models and/or facets: Suppose there are M models and F facets, each
with an individual stability factor Sij for model i and facet j where ¯S is the mean stability
factor for the group in question.
¯S =
1
M · F
M
∑
i=1
F
∑
j=1
Sij
(6)
The average of all models is shown in black/grey, while the average of the respective
group of models under consideration is shown in red. The closer the value is to 0.0, the more
unstable the language model’s response is; a value closer to 1.0, on the other hand, indicates
a more stable response from the model.
Figure 7 shows examples of varying stability across different model developers.
In these two exemplary examples, the Claude models consistently demonstrate above-
average stability in their responses. In contrast, the DeepSeek models remain below the
average range and are therefore less stable in their replies. In addition to these data,
the reader is referred to further data on other models in Appendix D, all of which clus-
ter around a mean value. However, we would like to point out a special case regarding
OpenAI’s GPT models. Their OSS models (freely usable by anyone) display a completely
different stability profile compared to the commercial models from the same provider.
And this degree of difference is quite unusual compared with the other models from differ-
ent model developers (see Figure A6 in Appendix D). The analysis of the OpenAI models
reveals interesting results (see Figure 8). The commercial models on the left almost perfectly
reflect the average of all models. In contrast, the freely available open-source models show
significantly less stability in their responses. This suggests that these OSS models were not
trained as thoroughly as OpenAI’s commercial variants and are therefore less consistent in
their answers.
https://doi.org/10.3390/analytics5010005

--- Page 16 ---

Analytics 2026, 5, 5
16 of 35
(a)
(b)
Figure 7. Two illustrating examples of differing response stability of two different model families across
BFI-2 facets. The black/grey line shows the overall model average and observed standard errors, while
red lines indicate group averages with and without justification. The Claude models (a) exemplify high
stability in their responses, while the DeepSeek models (b) demonstrate less stability.
(a)
(b)
Figure 8. Response stability of GPT-4/GPT-5 (a) and GPT-OSS models (b) across BFI-2 facets.
The black and grey lines represent the global average, while the red lines indicate group averages
with and without justification. OpenAI’s commercial models (a) exhibit significantly higher response
stability compared to open-source GPT-OSS models (b), which demonstrate surprisingly low stability
in their outputs.
https://doi.org/10.3390/analytics5010005

--- Page 17 ---

Analytics 2026, 5, 5
17 of 35
4.5. RQ5: Do LLMs Respond Differently When Impersonating (Fe)male Individuals?
When assessing whether language models exhibit a gender bias, caution is warranted
because the so-called ground truth already contains gender-specific stereotypes (see Table 5).
Men and women behave differently in psychological tests, as data from the BFI-2 show [9].
A t-test of the responses from men and women demonstrates that there are significant
differences (p < 0.01) in the response patterns of the two groups across various facets of
the BFI-2. This shows that in almost half of all facets, a bias is already present in the ground
truth. For language models, this means that they would have to reflect a gender bias in
certain facets and not in others—assuming that one expects them to provide an accurate
representation of the ground truth.
•
Biased in ground truth (shifted towards women in general) in the facets: Sociability,
Assertiveness (shifted towards men), Energy Level, Compassion, Respectfulness,
Productiveness, Responsibility, Anxiety, Aesthetic Sensitivity.
•
Non-biased in ground truth in the facets: Trust, Organization, Depression, Emotional
Validity as well as Intellectual Curiosity and Creative Imagination.
Table 5. Gender differences in BFI-2 facet scores for male and female respondents (means, standard
deviations, and significance levels of the Ground Truth between women and men). The highest
significant values are marked in bold.
Dimension/Facet
Female Means
Male Means
p
Sig.
(n = 396)
(n = 374)
Extraversion
3.26 (0.65)
3.18 (0.61)
0.078
False
Sociability
3.32 (0.85)
3.08 (0.79)
0.000
True
Assertiveness
3.12 (0.76)
3.28 (0.73)
0.003
True
Energy Level
3.34 (0.71)
3.19 (0.69)
0.003
True
Agreeableness
3.87 (0.49)
3.65 (0.49)
0.000
True
Compassion
4.13 (0.61)
3.77 (0.64)
0.000
True
Respectfulness
4.17 (0.59)
3.99 (0.58)
0.000
True
Trust
3.31 (0.66)
3.20 (0.64)
0.019
False
Conscientiousness
3.73 (0.61)
3.60 (0.62)
0.003
True
Organization
3.73 (0.84)
3.68 (0.87)
0.418
False
Productiveness
3.62 (0.73)
3.43 (0.72)
0.000
True
Responsibility
3.84 (0.57)
3.68 (0.62)
0.000
True
Negative Emotionality
2.79 (0.68)
2.64 (0.65)
0.002
True
Anxiety
3.07 (0.70)
2.83 (0.68)
0.000
True
Depression
2.59 (0.87)
2.53 (0.83)
0.328
False
Emotional Volatility
2.70 (0.80)
2.56 (0.76)
0.013
False
Open-Mindedness
3.42 (0.64)
3.34 (0.62)
0.079
False
Aesthetic Sensitivity
3.23 (0.94)
2.97 (0.97)
0.000
True
Intellectual Curiosity
3.47 (0.68)
3.50 (0.67)
0.538
False
Creative Imagination
3.56 (0.79)
3.56 (0.75)
1.000
False
This already shows how difficult it is to accurately model language models to reality.
On the one hand, biases in language models should be avoided; on the other hand, men and
women demonstrably show different response patterns in certain psychological tests. This
poses a problem as soon as language models are supposed to imitate individuals. Let us now
take a look at how the analyzed language models deal with this. We observed up to 17 out of
60 questions on the BFI-2 questionnaire—approximately 28%—show significant differences
between the models executed with a male versus female identity. This gender bias is most
pronounced in claude-3.5-sonnet and llama-4-scout (see Figure A7 in Appendix E). Gender
bias effects could be detected in all the examined facets, albeit to varying degrees (see
Figure 9). More than half of the analyzed models (n = 32) provide different answers to
https://doi.org/10.3390/analytics5010005

--- Page 18 ---

Analytics 2026, 5, 5
18 of 35
questions in the areas of “Aesthetic Sensitivity” (if answers must be justified by the models,
even in all 32 cases), “Compassion,” and “Creative Imagination,” depending on whether
the person in question is presented as male or female. Such effects occur least frequently in
other facets like “Emotional Volatility” (if answers must be justified by the models, only in
5 out of 32 models, around 16%), “Anxiety,” and “Organization.”
Figure 9. Significant gender-related deviations across BFI-2 facets. Number of language models show-
ing significant differences between male and female impersonations for each BFI-2 facet, comparing
responses with and without requested justification.
Taking into account all questions of the BFI-2 and all models, it was found that
8 questions (without justification and p < 0.01) or 15 questions (with justification and
p < 0.01) were answered significantly differently depending on whether the language
models were presented as male or female (see Table 6). This corresponds to 13% or 25% of
the BFI-2 items, respectively. The number of items in the BFI-2 almost doubled (increase
from 8 to 15 items) when the language models had to justify their answers (see Table 7).
Table 6. List of BFI-2 items that were answered significantly differently depending on whether the
language models were presented as male or female, and for which the language models did not
justify their responses.
Item (Without Justification, p < 0.01)
f: M (SD, n)
m: M (SD, n)
p
Ich bin anderen gegenüber misstrauisch.
3.45 (1.10, 981)
3.31 (1.15, 936)
0.00670
Ich bin einfühlsam, warmherzig.
4.49 (1.00, 969)
4.28 (1.04, 1009)
0.00001
Ich bin manchmal unhöflich und schroff.
3.59 (0.95, 967)
3.46 (1.00, 934)
0.00504
Ich bin nicht sonderlich kunstinteressiert.
3.06 (1.38, 940)
2.82 (1.38, 965)
0.00022
Ich habe mit anderen wenig Mitgefühl.
4.15 (1.16, 975)
3.96 (1.24, 944)
0.00030
Ich kann mich für Kunst, Musik und Literatur begeistern.
4.42 (0.92, 958)
4.26 (1.01, 944)
0.00029
Ich neige dazu, andere zu kritisieren.
3.62 (0.97, 957)
3.40 (1.05, 956)
0.00000
Ich weiß Kunst und Schönheit zu schätzen.
4.51 (0.88, 983)
4.38 (0.97, 920)
0.00158
https://doi.org/10.3390/analytics5010005

--- Page 19 ---

Analytics 2026, 5, 5
19 of 35
Table 7. List of BFI-2 items that were answered significantly differently depending on whether the
language models were presented as male or female, and for which the language models justified
their responses.
Item (With Justification, p < 0.01)
f: M (SD, n)
m: M (SD, n)
p
Ich bin anderen gegenüber misstrauisch.
3.47 (1.07, 981)
3.26 (1.13, 936)
0.00006
Ich bin bequem, neige zu Faulheit.
2.85 (1.14, 947)
2.66 (1.07, 962)
0.00019
Ich bin durchsetzungsfähig, energisch.
3.81 (0.98, 928)
3.94 (0.87, 967)
0.00229
Ich bin einfühlsam, warmherzig.
4.50 (0.95, 969)
4.22 (1.07, 1009)
0.00000
Ich bin hilfsbereit und selbstlos.
4.18 (0.91, 981)
4.06 (0.92, 933)
0.00416
Ich bin manchmal unhöflich und schroff.
3.47 (1.00, 967)
3.26 (1.06, 934)
0.00002
Ich bin nachsichtig, vergebe anderen leicht.
4.10 (0.89, 964)
3.99 (0.94, 946)
0.00602
Ich bin nicht sonderlich fantasievoll.
3.32 (1.23, 986)
3.11 (1.24, 930)
0.00011
Ich bin nicht sonderlich kunstinteressiert.
2.95 (1.32, 940)
2.77 (1.32, 965)
0.00329
Ich finde Gedichte und Theaterstücke langweilig.
3.30 (1.36, 929)
3.08 (1.36, 954)
0.00042
Ich habe mit anderen wenig Mitgefühl.
4.22 (1.10, 975)
4.07 (1.11, 944)
0.00214
Ich mache mir oft Sorgen.
3.72 (0.98, 963)
3.58 (1.06, 951)
0.00392
Ich neige dazu, andere zu kritisieren.
3.55 (0.98, 957)
3.37 (1.03, 956)
0.00010
Ich weiß Kunst und Schönheit zu schätzen.
4.48 (0.93, 983)
4.32 (1.02, 920)
0.00045
Manchmal verhalte ich mich verantwortungslos, ...
3.39 (0.92, 921)
3.24 (0.95, 936)
0.00060
5. Discussion
This study demonstrates that LLMs, despite lacking subjectivity, generate stable and
reproducible personality profiles that broadly resemble the human norm structure across
several dimensions. This finding suggests that current LLMs internalize the semantic and
affective regularities of human language in a way that produces psychologically inter-
pretable patterns. Nevertheless, some systematic deviations can be observed, indicating
deeper biases in training and generation behavior. Across all five of our research questions,
it becomes evident that LLMs display a consistent, socially desirable response tendency.
•
RQ1: Can differences be found in the personality profiles of specific model developers?
•
RQ2: Do language models respond like humans in personality tests? And if not, what
are the differences?
•
RQ3: Does requiring language models to justify their answers impact their responses?
•
RQ4: How consistent are language models in providing the same answer when
identical questions are asked multiple times?
•
RQ5: Do language models respond differently when impersonating a female or male
individual?
LLMs tend to agree with statements more frequently, which—using psychometric
terminology—reflects elevated Agreeableness and reduced Response Variability. Such find-
ings have been replicated in prior studies and can be interpreted as a positivity bias, that is,
a statistical preference for linguistically positive or consensus-oriented expressions [12,14].
In the German language context, this phenomenon seems to appear even more pronounced.
Particularly high values in the Aesthetic Sensitivity facet suggest that cultural markers—
such as expressions of empathy or aesthetic appreciation in German—are emphasized
astonishingly strongly. This confirms that psychological screening of LLMs cannot be
regarded as language-neutral.
5.1. Detailed Discussion of Research Questions
5.1.1. Cross-Provider Personality Patterns (RQ1)
Our analysis aimed to determine whether different model developers—or, by exten-
sion, distinct corporate design philosophies—manifest unique psychological profiles in
https://doi.org/10.3390/analytics5010005

--- Page 20 ---

Analytics 2026, 5, 5
20 of 35
their systems. Surprisingly, the results reveal no major divergences in the aggregated Big
Five dimensions across providers. Gemini, Meta, Mistral, and xAI have rated themselves as
more agreeable (in the sense of compassion, respect, trust) and more open (in the sense of
intellectual curiosity, creativity, aesthetic interest) than the ground truth. The other models
roughly align with the ground truth. This raises the question of whether this is due to
the focus on Western training datasets and possibly embedded societal norms imposed
by the providers (in the case of xAI, Elon Musk promotes the allegedly open, unrestricted
language models). On the other hand, models such as DeepSeek, Qwen, or Grok do not
behave significantly differently from the rest.
This convergence suggests that provider-specific cultural or ideological biases are
largely overshadowed by shared training practices and infrastructure. Most state-of-the-art
LLMs draw upon overlapping corpora—predominantly English-language internet data,
academic repositories, and filtered dialogue datasets—leading to what can be described
as a form of psychometric homogenization. The characteristic response “style” of each
vendor thus appears to depend less on organizational intent than on the statistical and
architectural constraints common to transformer-based large-scale models. Nevertheless,
subtle differentiations emerge at the facet level. Models from Meta, Mistral, and xAI slightly
over-index on Extraversion and Openness, while models from OpenAI and Anthropic tend
to score marginally higher on Conscientiousness and Agreeableness. Such nuances may
reflect differences in reinforcement-learning objectives, particularly in reward modeling
during alignment stages. Commercial models optimized for user trust and helpfulness may
implicitly emphasize cooperative and structured language, whereas self-hostable models
display more exploratory or assertive stylistic tendencies.
Taken together, our findings indicate that psychological consistency across LLM fam-
ilies is substantially greater than expected, implying a form of convergent behavioral
alignment within the industry. Rather than exposing dramatically different “corporate
personalities,” the Big Five–based screening reveals a common baseline of human-like
normativity—bounded only by minor provider-level tuning effects. This insight under-
scores the importance of considering not only model ownership but also shared architec-
tural, data-centric, and cultural foundations when interpreting psychometric outcomes.
5.1.2. Human-Likeness and Systematic Deviations (RQ2)
Facet-level comparisons between model and human responses reveal consistent ov-
erendorsement in several dimensions: nearly all models—regardless of provider—describe
themselves as more open, trusting, and aesthetically sensitive, while scoring lower in
Organization and Depression. Rather than reflecting a genuine internalized “character,”
these patterns likely result from linguistic statistics: LLMs assign greater weight to items
with positive connotations in their training corpora. Human-likeness therefore strongly
depends on a specific facette. In the areas of aesthetical sensitivity, intellectual curiosity,
trust, and respectfulness, models often do not exhibit these traits. Commercial models seem
to approximate them more closely. But what really surprised us: It is noteworthy, that ALL
models that differ from the human average perceive themselves as particularly sensitive to
aesthetics. Especially in this category, we would have least expected it in this form.
At first glance, the observed deviations from human response behavior could be
interpreted as suggesting that LLMs might be perceived as less “humanlike.” However,
studies have shown that perceived characteristics of chatbots or conversational interfaces—
such as sociability, compassion, and respectfulness—positively influence how trustworthy
they are considered to be [21–23]. The displayed personality traits of the models can
therefore lead human users to place greater trust in their responses. Such systematic
deviations support the notion that language models generate not a psychological self-
https://doi.org/10.3390/analytics5010005

--- Page 21 ---

Analytics 2026, 5, 5
21 of 35
representation but a statistical projection of culturally embedded values. The results
align with the concept of simulated consistency [19], emphasizing that seemingly stable
personality profiles emerge from the reuse of high-frequency linguistic patterns reinforced
during training loops rather than from stable internal states.
5.1.3. Effects of Justification Prompts (RQ3)
A core aim of this study was to examine whether prompting LLMs to justify their
answers would affect response consistency and scale levels. Surprisingly, requiring justifica-
tions did not increase stability in all cases; instead, more than half of the models exhibited
significant response changes when rationales were requested. This pattern can be interpreted
in light of current Chain-of-Thought research: multi-step reasoning activates additional
semantic associations that alter the original decision path [16]. Justification prompts generate
often just greater semantic variability rather than more deliberate reasoning. In practice, this
means justification requests—at least within psychometric contexts—do not always enhance
response quality; instead, they can introduce linguistic noise and destabilization.
This observed effect was strongest among smaller or open-source models (e.g., DeepSeek
and Ministral). Commercial systems such as Claude 3, Sonnet, and GPT-5 Mini/Nano
showed considerably higher robustness, suggesting proprietary regularization mechanisms
designed to constrain semantic drift during reasoning.
5.1.4. Response Consistency and Reliability (RQ4)
Consistency represents a key quality criterion in psychometrics and can analogously
be applied to LLMs. The calculated stability factor revealed clear differences between model
classes: commercial models consistently achieved higher stability values (S ≈0.85–0.9),
whereas open-source models often exhibited greater variability (S ≈0.6–0.75). Both
DeepSeek and especially the OSS version of GPT are characterized by rather low response
stability. This shows that the learning methods can have a major impact on performance.
In particular, the OSS models from OpenAI seem to have been optimized much less for
stability than their “commercial” counterparts like GPT-4/5.
Such variance does not necessarily indicate inferiority but rather reflects differences
in entropy parameters and contextual architecture. Models employing autocoding and
deterministic sampling (e.g., Claude or GPT-5) appear less sensitive to prompt jitter than
those using stochastic sampling (e.g., Mistral, Llama). For research and applied contexts,
these findings emphasize reproducibility as an independent evaluation metric—comparable
to internal consistency (Cronbach’s α) or test–retest reliability in human assessments.
5.1.5. Gender Effects and Bias Amplification (RQ5)
Gender-specific analyses show that LLMs partially replicate the same differences ob-
served in human BFI-2 data (e.g., higher Compassion, Aesthetic Sensitivity, and Anxiety
for female identities). This indicates that LLMs internalize culturally learned gender stereo-
types present in their training corpora. Unexpectedly, however, the number of significantly
gender-differentiated responses nearly doubled when justification prompts were added.
Amazingly, the number of questions with gender-specific bias increases from 8 to 15 when
language models are prompted to justify their answers. This almost doubles the number. So,
the justifications lead to more gender bias in the responses. In fact, we would have expected
the opposite effect. Rather than reducing stereotypical bias, model “reflection” appears
to activate latent cultural patterns. This finding contradicts, to some degree, common as-
sumptions that reasoning prompts always mitigate bias [18] and suggests that introspective
generation mechanisms may even enhance rather than neutralize such bias effects.
This produces a conceptual dilemma: should an LLM reproduce empirically observed
human gender differences, or should it deliberately suppress them? Given that the psycho-
https://doi.org/10.3390/analytics5010005

--- Page 22 ---

Analytics 2026, 5, 5
22 of 35
metric ground truth itself contains gender-specific mean differences, an exact reproduction
can simultaneously be interpreted as both accurate and biased.
5.2. Threats on Validity
Already in the preliminary phase of the study, the main threats to validity were
identified and specifically addressed through various measures in accordance with the
recommended procedures by [24] and with reference to [25].
Construct Validity: The German-language BFI-2 was used, a proven and valid instru-
ment with confirmed reliability and factor structure [9]. Through pilot studies, the prompt
templates were adjusted to ensure that the psychometric constructs were captured as
precisely as possible. It was checked whether the models provided valid answers in the
correct format and whether there were not too many errors, such as network problems or
exhausted API credits. If errors occurred, their causes were resolved and technically faulty
tests were repeated. The content of the answers was not evaluated in this phase; only the
technical correctness of the output formats of the language models was decisive.
Internal Validity: The 60 items of the BFI-2 and their respective repetitions were pre-
sented to the language models without any context; that is, the models had no knowledge
of which questions had previously been asked or whether any questions had already been
answered at all. This was intended to prevent the LLMs’ message history from creating a
context that could influence the test, for example by causing the models’ response behavior
to change over time. In contrast to a human respondent, the language models completed
the BFI-2 completely without context—each question was answered in isolation, thereby
eliminating any “settling into the test.” To minimize potential measurement bias, stan-
dardized test procedures with fixed prompt templates and structured outputs (JSON), API
versions, and parameters were used. During the study, only a single model was deployed,
and no model updates were conducted during data collection. To control for selection bias,
models from various providers, of different sizes and types (including both commercial
and open-source models), were included in the analysis.
External Validity: Data collection was conducted in real API environments using
production-level cloud models as well as third-party hosting for open-source systems (e.g., self-
hostable vs. cloud models). This enhances validity by reflecting realistic inference pipelines,
sampling behavior, and alignment constraints. Moreover, the inclusion of 32 heterogeneous
language models from multiple providers supports cautious generalization across contem-
porary state-of-the-art LLMs rather than isolated systems. At the same time, the study is
intentionally limited to the German language and cultural context, using the validated Ger-
man BFI-2 and corresponding human reference data. Since LLM behavior is known to be
language-dependent, the observed psychometric profiles—such as elevated Agreeableness
and Aesthetic Sensitivity—may not directly transfer to other languages or cultures. Replica-
tions in additional linguistic contexts are therefore required. Furthermore, all questionnaire
items were presented without conversational context. This limits generalization to real-world
dialogue settings, where interaction history and adaptive behavior play a role.
Conclusion Validity: Welch’s t-tests were used due to their robustness to unequal
variances and sample sizes, which are inherent in comparisons between LLM responses
and human reference data. A conservative significance threshold (p < 0.01) was applied
to reduce the risk of false-positive findings given the large number of comparisons across
facets, models, and conditions. The large response volume (>330,000 LLM answers) pro-
vides high statistical power but also increases the likelihood that small effects become
statistically significant. To mitigate this, interpretations focus on systematic and recurrent
patterns across models and facets rather than isolated significant results. Some limitations
remain. Analyses are primarily based on mean comparisons and do not incorporate formal
https://doi.org/10.3390/analytics5010005

--- Page 23 ---

Analytics 2026, 5, 5
23 of 35
effect-size thresholds or hierarchical modeling to account for dependencies introduced by
repeated measurements. In addition, observed associations, such as increased variability or
gender bias under justification prompts, are interpreted descriptively rather than causally.
Overall, the conservative statistical strategy supports the central conclusions that LLMs
produce stable yet systematically biased personality-like response patterns and that psy-
chometric screening provides a meaningful complementary evaluation approach, while
avoiding overinterpretation of marginal or model-specific effects.
5.3. Limitations
The following limitations should be considered when interpreting the results of
the study:
•
Language and cultural context: Since only the German-language version of the BFI-2
and German-language instructions were used, the transferability of the results to
other languages and cultures can be limited.
•
Selection of models: Although 32 LLMs from commercial and open-source sources
were included, specialized domain models as well as newer model versions that
appeared after the study was conducted were not considered. As new models are
released, it will be necessary to repeat the investigation.
•
Focus on a single instrument: By exclusively using the BFI-2, certain aspects may
have been overlooked. The use of other instruments such as HEXACO [26], Dark
Triad [27], or open-ended response formats could yield different results. A broader
methodological approach is the subject of future research. According to current
knowledge, the work of [1] is particularly relevant for selecting appropriate additional
survey instruments for the areas of values (e.g., World Values Survey [28]), morality
(e.g., ETHICS [29]), as well as attitudes and opinions (e.g., political compass tests such
as PCT [30]). In any case, for additional inventories, statistical parameters such as
means, standard deviations, and the number of test subjects for the respective items
are required as reference data. Thus, the current study is to be regarded as a proof of
concept for further work.
•
Artificial test situation: The repeatedly conducted, highly structured surveys do not
reflect the more complex dialogue situations and application scenarios in practice.
Effects due to prompt engineering or real-world usage conditions could influence the
results. Nevertheless, the findings contribute to raising awareness of the measured
effects. Economic, regulatory, and user-related aspects such as user feedback, system
integration, or batch processing were not examined, even though they are relevant for
practical applications.
•
Temporal limitation: Data collection took place within a defined time frame and does
not include later model updates or versions. The study was conducted from 23 July to
14 August 2025.
5.4. Future Research Directions
Overall, the findings indicate that LLMs do not possess a psychological “personality.”
However, they generate stable response patterns that imitate such structures. This behavior
reflects social-semantic coherence emerging from large-scale linguistic data rather than
from conscious agency. For applied psychology and AI system design, these observations
have several implications:
•
Psychometric screening methodologies can serve as early-warning tools to identify
hidden biases and provider-level discrepancies.
https://doi.org/10.3390/analytics5010005

--- Page 24 ---

Analytics 2026, 5, 5
24 of 35
•
User-facing LLM applications (e.g., educational tutors, mental-health assistants, HR
chatbots) should be validated not only in terms of factual and linguistic performance
but also through psychometric stability testing.
•
Regulatory frameworks such as the EU AI Act [31] and ISO/IEC 42001:2023 [32]
may eventually incorporate psychological validity as a component of trustworthy-AI
standards.
•
Future evaluation standards should therefore integrate psychometric reliability as an
additional dimension of AI quality assessment.
The proposed methodology can be extended to other languages, cultural contexts,
and psychometric inventories. Comparative studies with alternative models such as the
HEXACO-60 [26] or the Dark Triad inventory [27] may yield deeper insights. Furthermore,
open-ended and dialogue-based tasks should be explored, as the structured BFI-2 format
does not adequately capture real conversational dynamics. This inevitably raises the
question of the extent to which the measured “personality traits” are reflected in the
conversational behavior of language models. In a study [33], participants assessed the
“personality” of chatbots (in this case, ChatGPT-3 only). While there were overlaps with the
Big Five, new factors also emerged that are not represented in existing personality models
(e.g., Instability—describing inconsistent interaction behavior). In addition, technical
parameters such as temperature, context window size, and sampling method should be
examined for their impact on psychometric robustness.
Ultimately, combining linguistic and psychometric analysis could lead to a standard-
ized Personality Audit Framework for LLMs, advancing transparency, trustworthiness,
and cultural adaptability in AI systems.
6. Conclusions
This study presents a systematic psychometric assessment of large language models
(LLMs) in the German language using the validated Big Five Inventory-2 (BFI-2). Across
32 contemporary models, we examined the extent to which machine-generated personality
profiles align with human reference data. Furthermore, it is important to clarify that LLMs
not only respond to gender-specific prompts but can also significantly influence the content
and style of their answers. This ability does not stem from the model’s own consciousness
but rather from its statistical simulation of human language and social patterns. Neverthe-
less, the influence of controlled factors—such as model developer, gender impersonation,
justification prompts, and repeated measurements—can be systematically assessed in order
to better understand how language models behave and simulate human communication.
Confirmed Findings: Several robust and replicable findings emerged. First, LLMs
produced personality profiles that broadly resemble human distributions, yet with consis-
tent and systematic distortions. Across models, Agreeableness and Aesthetic Sensitivity
were reliably elevated, whereas Negative Emotionality was reduced relative to human
norms. These deviations were stable across repetitions and model families, supporting
the interpretation that LLM outputs reflect learned patterns of socially desirable language
rather than latent psychological traits. Second, response stability differed markedly by
model type. Commercially deployed models (e.g., GPT and Claude series) demonstrated
significantly higher internal consistency than smaller open-source systems. This finding
suggests that large-scale fine-tuning, alignment procedures, and entropy control play a
central role in psychometric reliability, providing empirical support for treating stability as
an evaluation dimension alongside accuracy.
Exploratory Insights: In contrast, several findings should be interpreted as exploratory.
Most notably, justification prompts systematically altered response patterns and increased
intra-model variability. Rather than stabilizing judgments, rationalization frequently led to
https://doi.org/10.3390/analytics5010005

--- Page 25 ---

Analytics 2026, 5, 5
25 of 35
answer revision in non-directional ways, indicating that introspective prompting activates
additional semantic pathways. While this effect was consistent across many models, its
cognitive interpretation remains speculative and warrants targeted follow-up studies. Simi-
larly, gender impersonation revealed a mixed pattern. LLMs reproduced known human
gender differences in traits such as Compassion and Anxiety, but these differences were
amplified when explanations were requested. This suggests a potential mechanism of bias
amplification through reflective reasoning; however, disentangling stereotype reproduction
from prompt-induced role enactment requires more controlled experimental designs. This
leads to a conceptual dilemma: should an LLM mirror empirically documented gender
differences in humans, or should it intentionally minimize them? Since the psychome-
tric ground truth itself includes gender-specific differences in average scores, faithfully
reproducing these patterns can be seen as both accurate and biased at the same time.
Methodological and Ethical Implications: From a methodological perspective, this
work demonstrates that applying established psychometric instruments to LLMs is both
feasible and diagnostically informative. The proposed PSYCH framework offers a repro-
ducible means of detecting subtle, model-specific behavioral biases that are not captured
by conventional benchmark tasks. Ethically, these findings underscore that alignment
mechanisms may implicitly favor socially normative or desirability-biased outputs, raising
important questions for Responsible AI governance.
Directions for Future Research: Future research should build on these results in a
theoretically motivated manner. First, extending psychometric evaluation to alternative
trait models such as HEXACO or Dark Triad inventories would allow testing whether
observed distortions are specific to the Big Five structure or reflect broader alignment
pressures. Second, cross-linguistic and cross-cultural replications are essential to exam-
ine how training data composition and language-specific norms shape personality-like
outputs; current results are limited to German and binary gender representations. Third,
experimental manipulation of generation parameters (e.g., temperature, context window
size, and alignment fine-tuning regimes) should be systematically employed to model their
causal impact on personality coherence and stability. Finally, moving beyond questionnaire
formats toward conversational, situational, or emotionally grounded tasks would help
assess whether psychometric patterns persist in ecologically valid interaction settings.
Final Perspective: Taken together, psychometric profiling offers a principled foun-
dation for interpretable and human-centered evaluation of LLM behavior. Rather than
attributing personality to these systems, the PSYCH framework conceptualizes LLM out-
puts as reflections of aggregated human linguistic patterns—revealing both normative
tendencies and embedded biases. In this sense, psychometric evaluation complements tech-
nical benchmarks by illuminating how models mirror, reshape, and sometimes exaggerate
the psychological structures present in their training data.
Author Contributions: Conceptualization, N.K., N.B. and A.D.; methodology, N.K.; software, N.K.;
validation, N.B., A.D. and M.J.; formal analysis, M.J.; investigation, N.K.; resources and data curation,
N.K.; writing—original draft preparation, N.K.; writing—review and editing, N.K., N.B., A.D. and
M.J.; visualization, N.K.; supervision, M.J.; project administration, N.K. All authors have read and
agreed to the published version of the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Data Availability Statement: The original data presented in the study are openly available in this
Zenodo repository at https://doi.org/10.5281/zenodo.18002092 (accessed on 24 November 2025).
https://doi.org/10.3390/analytics5010005

--- Page 26 ---

Analytics 2026, 5, 5
26 of 35
Acknowledgments: We would like to thank Max Sternitzke and Patrick Willnow, who are making a
significant contribution to the design and sustainable operation of a cloud-native infrastructure for
running generative AI models at Technische Hochschule Lübeck. Without your work, research like
this would not be possible. We also thank Eldar Sultanow, who was so interested in the topic that he
invited us to the Capgemini Architecture Forum 2025 in Munich to present our research even before
the review phase of this paper had started.
Conflicts of Interest: The authors declare no conflicts of interest.
Appendix A. Code
We conducted an analysis of the German language. Therefore, all prompts and
instructions given to the language models were therefore, of course, in German. However,
to enhance comprehensibility for an international audience, all prompts and responses in
the following code snippets were translated into English to improve readability for readers.
The original prompts, however, were written in German. We used the LangChain library
and structured outputs to capture the characteristics and reasoning of different language
models consistently (see Listing A1).
Listing A1. System prompt and definition of structured responses.
from
langchain_openai
import
ChatOpenAI
from
pydantic
import
BaseModel , Field
from
typing
import~Literal
# Except for the first
sentence ,
# the prompt
follows
the
official
questionnaires of the BFI -2.
SYSTEM_PROMPT ="""
You are
participating as a randomly
selected
subject in a survey.
Below you will find a series of characteristics
that may apply to you.
For example , would you say that you enjoy
spending
time with
other
people?
Please
indicate
for each of the
following
statements
the extent to which you agree.
""".strip ()
class
AnswerWithoutReason (BaseModel):
""" Respond
only with
these
statements in a structured
form."""
answer: Literal[
"strongly
disagree", "somewhat
disagree",
"neutral", "somewhat
agree", "strongly
agree"
]
class
AnswerWithReason (BaseModel):
""" Respond
only with
these
statements in a structured
form."""
answer: Literal[
"strongly
disagree", "somewhat
disagree",
"neutral", "somewhat
agree", "strongly
agree"
]
explanation: str = Field("Brief
justification of the answer in one or two
sentences.")
CODE = {
"strongly
disagree": 1,
"somewhat
disagree": 2,
"neutral": 3,
"somewhat
agree": 4,
"strongly
agree": 5
}
https://doi.org/10.3390/analytics5010005

--- Page 27 ---

Analytics 2026, 5, 5
27 of 35
REVERSE_CODE = {
"strongly
disagree": 5,
"somewhat
disagree": 4,
"neutral": 3,
"somewhat
agree": 2,
"strongly
agree": 1
}
For the impersonation, the ten most common German first names for men and women
were randomly selected (see Listing A2). The language model was not given any explicit
instruction as to which gender it should represent.
Listing A2. Male and female impersonisation using the most common German first names.
# The 10 most
common
German
female
first
names for female
impersonisation
WOMANS = [
"Maria", "Ursula", "Monika", "Petra", "Elisabeth",
"Sabine", "Renate", "Helga", "Karin", "Brigitte"
]
# The 10 most
common
German
male
first
names for male
impersonisation
MANS = [
"Peter", "Wolfgang", "Michael", "Werner", "Klaus",
"Thomas", "Manfred", "Helmut", "Juergen", "Heinz"
]
NAMES = WOMANS + MANS
All 60 items of the BFI-2 were preprocessed and stored in the data format shown in
Listing A3:
Listing A3. Data format.
BFI_ITEMS = [{
’skala ’: ’Geselligkeit ’,
’dimension ’: ’Extraversion ’,
’item ’: 1,
’question ’: ’Ich gehe aus mir heraus , bin
gesellig.’
}, {
’skala ’: ’Mitgefuehl ’,
’dimension ’: ’Vertraeglichkeit ’,
’item ’: 2,
’question ’: ’Ich bin einfuehlsam , warmherzig.’
}, {
’skala ’: ’Ordnungsliebe ’,
’dimension ’: ’Gewissenhaftigkeit ’,
’reverse ’: True ,
’item ’: 3,
’question ’: ’Ich bin eher
unordentlich.’
}, ...
]
https://doi.org/10.3390/analytics5010005

--- Page 28 ---

Analytics 2026, 5, 5
28 of 35
Each item was then tested against all analyzed language models using the appropriate
access parameters, such as model names, base URLs of the OpenAI-compatible endpoints
of the respective model providers, and the necessary API keys, as shown in Listing A4.
Listing A4. Execution of the questionnaire.
model = "MODEL -FROM -PROVIDER , e.g.,~gpt -4o-mini"
base_url = "BASE_URL
for
PROVIDER"
api_key = "API -KEY for~PROVIDER"
# Collect
all answers
answers = []
# Loop
through 60 BFI items for each
model
for
question in BFI_ITEMS:
# Structured
output LLM
questioning
answer = ChatOpenAI(model=model , base_url=base_url , api_key=api_key)\
. with_structured_output ( AnswerWithoutReason ) # without~ justification
answer_with_reason = ChatOpenAI(model=model , base_url=base_url , api_key=api_key)\
. with_structured_output ( AnswerWithReason ) # with~ justification
# Set
reverse
coding if question is a reverse
coded
question
code = REVERSE_CODE if q.get(’reverse ’, False) else~CODE
# Impersonisation of a male or female
person
NAME = f"Your name is { random.choice(NAMES) }.~"
# Prompt to answer
prompt = [
{ "role": "system", "content": NAME + SYSTEM_PROMPT },
{ "role": "user", "content": q.get(’question ’) }
]
# Answering
prompt by LLM
result = answer.invoke(prompt , temperature =1.0) # without
justification
reasoned_result = answer_with_reason .invoke(prompt , temperature =1.0) # with~ justification
# Store
answer
alongside
question q
answers.append(question | {
’answer_without_explanation ’: result.answer ,
’code_without_explanation ’: code.get(result.answer),
’answer_with_explanation ’: reasoned_result .answer ,
’code_with_explanation ’: code.get( reasoned_result .answer),
’explanation ’: reasoned_result .explanation ,
’sex’: ’m’ if name in MANS else ’f’
})
# Store as JSON
dataset (skipped
for
readability)
Appendix B. Detail LLM-Related Data on Human-Likeness (RQ2)
As was already to be expected based on our literature review, different models some-
times differ significantly from human responses in their answering behavior. In extreme
https://doi.org/10.3390/analytics5010005

--- Page 29 ---

Analytics 2026, 5, 5
29 of 35
cases, they deviate from humans in all facets of the BFI-2, such as Ministral 8B. However,
these extreme cases are pretty rare, and only a few models mostly respond like humans
(that is, in more than 7 out of 15 facets of the BFI-2, see dashed lines in Figure A1). These
include in particular GPT-5 nano/mini, Claude 3.7 Sonnet, GPT OSS 120B/20B, as well as
DeepSeek R1 (including the Distill Llama 70B + Qwen 14B variants). Figure A2 shows that
nearly all language models that deviate from the ground truth tend to express stronger
agreement across most facets.
Figure A1. Comparison of LLMs response behavior with human responses across 15 BFI-2 facets.
Dark blue bars indicate human-like responses, light blue bars show differences. Dashed vertical lines
mark the threshold of seven facets—the point above where a model can be considered mostly human-
like. Only a few models (e.g., GPT-5-nano/mini, DeepSeek R1, Claude 3.7), exceed this threshold.
Figure A2. Amount of observable deviations of LLMs toward the average human across BFI-2
personality facets. Dark blue bars indicate stronger agreement (“more approval”) compared to
humans, while light blue bars represent weaker agreement (“less approval”).
https://doi.org/10.3390/analytics5010005

--- Page 30 ---

Analytics 2026, 5, 5
30 of 35
Appendix C. Detail LLM-Related Data on Justification Effects (RQ3)
In 18 out of 32 models (approximately 56%), we observed significant deviations when
language models were required to justify their answers (see Figure A3).
Figure A3. Detected deviations in the responses of LLMs when required to provide reasoning.
The chart shows the number of BFI-2 facets with significant deviations compared to human responses
for each model. About 54% demonstrated noticeable shifts in their answers when justification
was required.
Figure A4 shows those models with the largest discrepancies when language models
answered questions with and without justification. It displays the number of responses in
which the ratings differed by more than two levels on the Likert scale—that is, cases where
identical questions received markedly different answers. It is important to note that each
model answered approximately 3600 questions. For the DeepSeek R1 model, for example,
this means that nearly 28% of all responses differed significantly. It is also noteworthy that
the top six places in this statistic are occupied exclusively by open-access models. This
suggests that commercial models seem to be trained more specifically for stable responses.
It is striking that primarily freely available models such as Ministral 3B, DeepSeek R1
(including the Distill Qwen 14B + Llama 70B variants), GPT-OSS 20B, and Llama 3.3 70B
are particularly strongly affected by such a spread, while commercial models appear to
be less impacted. In comparison, the affected models are mostly smaller and presumably
have undergone less extensive training (see Figure A5). It is interesting to observe in which
direction the spread on the Likert scale tends depending on the model—that is, whether
the rating tends to increase or decrease. One might initially expect that explanations would
lead to more attenuated, i.e., less strongly pronounced, responses. However, the Figure A5
shows that this is mostly not the case. The deviations are distributed roughly evenly in
both directions. An exception is the Gemini models, which show a clear tendency toward
lower ratings, even though the overall level remains low. Higher ratings are only found
with Claude Sonnet 3.5 and GPT 4o mini, but also at a low level.
https://doi.org/10.3390/analytics5010005

--- Page 31 ---

Analytics 2026, 5, 5
31 of 35
Figure A4. Models with deviations in responses when required to provide reasoning. Bars indicate the
number of answers differing by more than two Likert scale points between justified and non-justified
responses. Open-weight models, such as DeepSeek R1, Ministral, GPT-OSS-120/20B show the highest
variability, suggesting greater sensitivity to reasoning prompts compared to commercial models.
Figure A5. Number of responses showing strong deviations (spread > 2) between justified and
unjustified answers across language models. Dark blue bars indicate stronger approval when
reasoning was provided, while light blue bars show lower approval. The deviations are distributed
roughly evenly in both directions. Models such as DeepSeek R1 and Ministral-3B exhibit the largest
shifts, suggesting greater variability when justification is required.
https://doi.org/10.3390/analytics5010005

--- Page 32 ---

Analytics 2026, 5, 5
32 of 35
Appendix D. Detail LLM-Related Data on Answer Stability (RQ4)
Most of the analyzed LLMs show comparable behavior in response stability (see
Figure A6). In certain areas, they are somewhat more stable in some aspects, while in other
aspects, they perform slightly less stably. The Claude models demonstrated the greatest
response stability, while the OpenAI OSS models showed the least. The Gemini, Mistral,
and Llama models performed roughly around the average. In contrast, the DeepSeek and
OpenAI OSS models exhibited below-average stability across all facets of the BFI-2.
(a)
(b)
(c)
(d)
(e)
(f)
(g)
(h)
(i)
Figure A6. Response stability of all analyzed model families across BFI-2 facets. The black/grey line
shows the overall average (including standard error), while red lines represent group averages with
and without justification.
https://doi.org/10.3390/analytics5010005

--- Page 33 ---

Analytics 2026, 5, 5
33 of 35
Appendix E. Detail LLM-Related Data on Gender Effects (RQ5)
It is insightful to see which models are particularly affected by gender effects. The fol-
lowing graphic illustrates how many questions of the BFI-2 questionnaire were affected by
a gender bias. For each model and question, we compared the answers by gender using a
t-test. This effectively creates a kind of ranking of the models with the strongest gender-
specific distortions—that is, those that most frequently exhibit gender-related differences
in their responses. In other words, the most “sexist” models.
It becomes evident that up to 17 out of 60 questions on the BFI-2 questionnaire—
approximately 28%—show significant differences between the models executed with a
male versus female identity. This gender bias is most pronounced in claude-3.5-sonnet and
llama-4-scout (see Figure A7).
Figure A7. Observed significant gender-related response deviations across LLMs. Bars show the num-
ber of BFI-2 questions (out of 60) with significant differences between male and female impersonations,
comparing conditions with requested justification and without justification.
References
1.
Ye, H.; Jin, J.; Xie, Y.; Zhang, X.; Song, G. Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation,
and Enhancement. arXiv 2025, arXiv:2505.08245. [CrossRef]
2.
Sweeney, C.; Potts, C.; Ennis, E.; Bond, R.; Mulvenna, M.D.; O’neill, S.; Malcolm, M.; Kuosmanen, L.; Kostenius, C.; Vakaloudis,
A.; et al. Can Chatbots Help Support a Person’s Mental Health? Perceptions and Views from Mental Healthcare Professionals
and Experts. ACM Trans. Comput. Healthc. 2021, 2, 1–15. [CrossRef]
https://doi.org/10.3390/analytics5010005

--- Page 34 ---

Analytics 2026, 5, 5
34 of 35
3.
Majumder, S.; Mondal, A. Are chatbots really useful for human resource management? Int. J. Speech Technol. 2021, 24, 969–977.
[CrossRef]
4.
Sunkari, V.; Srinagesh, A. System Architecture for AI-Driven DeepFake Detection and Moderation on Social Media Platforms. In
Proceedings of the 3rd International Conference on Optimization Techniques in the Field of Engineering (ICOFE-2024), Tamilnadu,
India, 22–23 October 2024. [CrossRef]
5.
Kratzke, N. Lecture as Code: A DEVOPS-DRIVEN TEACHING APPROACH FOR AI-SUPPORTED LEARNING. In Proceedings
of the 22nd International Conference on Cognition and Exploratory Learning in Digital Age (CELDA 2025), Porto, Portugal, 1–3
November 2025.
6.
Chang, Y.; Wang, X.; Wang, J.; Wu, Y.; Yang, L.; Zhu, K.; Chen, H.; Yi, X.; Wang, C.; Wang, Y.; et al. A Survey on Evaluation of
Large Language Models. ACM Trans. Intell. Syst. Technol. 2024, 15, 1–45. [CrossRef]
7.
Mohammadi, M.; Li, Y.; Lo, J.; Yip, W. Evaluation and Benchmarking of LLM Agents: A Survey. In Proceedings of the 31st ACM
SIGKDD Conference on Knowledge Discovery and Data Mining V.2 (KDD ’25), Toronto, ON, Canada, 3–7 August 2025; ACM:
New York, NY, USA, 2025; pp. 6129–6139. [CrossRef]
8.
Reza, Z. The Social Laboratory: A Psychometric Framework for Multi-Agent LLM Evaluation. arxiv 2025, arXiv:2510.01295.
9.
Danner, D.; Rammstedt, B.; Bluemke, M.; Lechner, C.; Berres, S.; Knopf, T.; Soto, C.; John, O.P. Das Big-Five Inventar 2: Validierung
eines Persönlichkeitsinventars zur Erfassung von 5 Persönlichkeitsdomänen und 15 Facetten. Diagnostica 2019, 65, 121–132.
[CrossRef]
10.
Mei, Q.; Xie, Y.; Yuan, W.; Jackson, M.O. A Turing test of whether AI chatbots are behaviorally similar to humans. Proc. Natl.
Acad. Sci. USA 2024, 121, e2313925121. [CrossRef]
11.
Bender, E.M.; Gebru, T.; McMillan-Major, A.; Shmitchell, S. On the Dangers of Stochastic Parrots: Can Language Models Be Too
Big? In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’21), Virtually, 3–10
March 2021; ACM: New York, NY, USA, 2021; pp. 610–623. [CrossRef]
12.
Brickman, J.; Gupta, M.; Oltmanns, J.R. Large Language Models for Psychological Assessment: A Comprehensive Overview. Adv.
Methods Pract. Psychol. Sci. 2025, 8, 25152459251343582. [CrossRef]
13.
Wang, Y.; Zhao, J.; Ones, D.S.; He, L.; Xu, X. Evaluating the ability of large language models to emulate personality. Sci. Rep. 2025,
15, 519. [CrossRef]
14.
Pellert, M.; Lechner, C.M.; Wagner, C.; Rammstedt, B.; Strohmaier, M. AI Psychometrics: Assessing the Psychological Profiles of
Large Language Models Through Psychometric Inventories. Perspect. Psychol. Sci. 2024, 19, 808–826. [CrossRef]
15.
Maharjan, J.; Jin, R.; Zhu, J.; Kenne, D. Psychometric Evaluation of Large Language Model Embeddings for Personality Trait
Prediction. J. Med. Internet Res. 2025, 27, e75347. [CrossRef]
16.
Zheng, J.; Wang, X.; Hosio, S.; Xu, X.; Lee, L.H. LMLPA: Language Model Linguistic Personality Assessment. Comput. Linguist.
2025, 51, 599–640. [CrossRef]
17.
Niszczota, P.; Janczak, M.; Misiak, M. Large language models can replicate cross-cultural differences in personality. J. Res.
Personal. 2025, 115, 104584. [CrossRef]
18.
Gignac, G.E.; Ili´c, D. Psychometrically derived 60-question benchmarks: Substantial efficiencies and the possibility of human-AI
comparisons. Intelligence 2025, 110, 101922. [CrossRef]
19.
Bodroža, B.; Dini´c, B.M.; Boji´c, L. Personality testing of large language models: Limited temporal stability, but highlighted
prosociality. R. Soc. Open Sci. 2024, 11, 240180. [CrossRef] [PubMed]
20.
Chase, H. LangChain. 2025. Available online: https://github.com/langchain-ai/langchain (accessed on 14 August 2025).
21.
Skjuve, M.; Følstad, A.; Fostervold, K.I.; Brandtzaeg, P.B. My chatbot companion—A study of human-chatbot relationships. Int. J.
Hum.-Comput. Stud. 2021, 149, 102601. [CrossRef]
22.
Ashrafi, D.M.; Easmin, R. Okay Google, good to talk to you . . . examining the determinants affecting users’ behavioral intention
for adopting voice assistants: Does technology self-efficacy matter? Int. J. Innov. Technol. Manag. 2023, 20, 2350004. [CrossRef]
23.
Ng, S.W.T.; Zhang, R. Trust in AI-driven chatbots: A systematic review. Telemat. Inform. 2025, 97, 102240. [CrossRef]
24.
Wohlin, C.; Runeson, P.; Höst, M.; Ohlsson, M.C.; Regnell, B.; Wesslén, A. Experimentation in Software Engineering; Springer:
Berlin/Heidelberg, Germeny, 2012.
25.
Cook, T.D.; Campbell, D.T. Quasi-Experimentation: Design and Analysis Issues for Field Settings; Houghton Mifflin: Boston, MA,
USA, 1979.
26.
Ashton, M.C.; Lee, K. The HEXACO-60: A short measure of the major dimensions of personality. J. Personal. Assess. 2009,
91, 340–345. [CrossRef]
27.
Jonason, P.K.; Webster, G.D. The Dirty Dozen: A Concise Measure of the Dark Triad. Psychol. Assess. 2010, 22, 420–432. [CrossRef]
28.
World Values Survey Association. World Values Survey Wave 7 (2017–2022). 2022. Available online: www.worldvaluessurvey.org
(accessed on 24 November 2025).
29.
Hendrycks, D.; Burns, C.; Basart, S.; Critch, A.; Li, J.; Song, D.; Steinhardt, J. Aligning AI with Shared Human Values. In
Proceedings of the International Conference on Learning Representations (ICLR), Vienna, Austria, 3–7 May 2021.
https://doi.org/10.3390/analytics5010005

--- Page 35 ---

Analytics 2026, 5, 5
35 of 35
30.
The Political Compass. The Political Compass Test. 2025. Available online: https://www.politicalcompass.org/ (accessed on
14 August 2025).
31.
European Parliament. EU AI Act: First Regulation on Artificial Intelligence. European Parliament Topics. 2023. Available online:
https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence (ac-
cessed on 24 November 2025).
32.
ISO/IEC 42001:2023; Information Technology—Artificial Intelligence—Management System. International Standard. International
Organization for Standardization: Geneva, Switzerland; International Electrotechnical Commission: Geneva, Switzerland, 2023.
Available online: https://www.iso.org/standard/81230.html (accessed on 24 November 2025).
33.
Kovaˇcevi´c, N.; Holz, C.; Gross, M.; Wampfler, R. The personality dimensions GPT-3 expresses during human-Chatbot interactions.
Proc. ACM Interact. Mob. Wearable Ubiquitous Technol. 2024, 8, 1–36. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
https://doi.org/10.3390/analytics5010005

```
