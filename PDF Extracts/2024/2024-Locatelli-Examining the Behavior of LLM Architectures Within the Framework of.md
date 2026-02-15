---
title: "2024-Locatelli-Examining the Behavior of LLM Architectures Within the Framework of - PDF Extract"
source_pdf: "2024-Locatelli-Examining the Behavior of LLM Architectures Within the Framework of.pdf"
pages: 14
extracted_at: "2026-02-15T17:51:56.689397"
---

# PDF Extract: 2024-Locatelli-Examining the Behavior of LLM Architectures Within the Framework of

**Source PDF:** 2024-Locatelli-Examining the Behavior of LLM Architectures Within the Framework of.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

Examining the Behavior of LLM Architectures Within the Framework of
Standardized National Exams in Brazil
Marcelo Sartori Locatelli, Matheus Prado Miranda, Igor Joaquim da Silva Costa, Matheus Torres
Prates, Victor Thom´e, Mateus Zaparoli Monteiro, Tomas Lacerda, Adriana Pagano, Eduardo Rios
Neto, Wagner Meira Jr., Virgilio Almeida
Universidade Federal de Minas Gerais, Belo Horizonte, Brazil
{locatellimarcelo, matheus.prado, igor.joaquim, matheus.prates, victor-thome, mateuszaparoli, tomas.muniz, meira,
virgilio}@dcc.ufmg.br, apagano@letras.ufmg.br, eduardo@cedeplar.ufmg.br
Abstract
The Exame Nacional do Ensino M´edio (ENEM) is a pivotal
test for Brazilian students, required for admission to a sig-
nificant number of universities in Brazil. The test consists
of four objective high-school level tests on Math, Human-
ities, Natural Sciences and Languages, and one writing es-
say. Students’ answers to the test and to the accompanying
socioeconomic status questionnaire are made public every
year (albeit anonymized) due to transparency policies from
the Brazilian Government. In the context of large language
models (LLMs), these data lend themselves nicely to compar-
ing different groups of humans with AI, as we can have ac-
cess to human and machine answer distributions. We leverage
these characteristics of the ENEM dataset and compare GPT-
3.5 and 4, and MariTalk, a model trained using Portuguese
data, to humans, aiming to ascertain how their answers re-
late to real societal groups and what that may reveal about the
model biases. We divide the human groups by using socioe-
conomic status (SES), and compare their answer distribution
with LLMs for each question and for the essay. We find no
significant biases when comparing LLM performance to hu-
mans on the multiple-choice Brazilian Portuguese tests, as the
distance between model and human answers is mostly deter-
mined by the human accuracy. A similar conclusion is found
by looking at the generated text as, when analyzing the es-
says, we observe that human and LLM essays differ in a few
key factors, one being the choice of words where model es-
says were easily separable from human ones. The texts also
differ syntactically, with LLM generated essays exhibiting,
on average, smaller sentences and less thought units, among
other differences. These results suggest that, for Brazilian
Portuguese in the ENEM context, LLM outputs represent no
group of humans, being significantly different from the an-
swers from Brazilian students across all tests.
Introduction
Over the last few years, advancements in NLP and machine
learning have culminated in the creation of large language
models (LLMs) that excel in a variety of tasks, such as
translating, question-answering, summarization, and natu-
ral language inference. As these models are getting more
and more adopted by the general public, as well as the in-
dustry and academia, researchers from many different back-
grounds have started evaluating how they fare on a plethora
Copyright © 2024, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
of benchmarks for distinct subjects and tasks (Chang et al.
2024). A significant part of this research effort focuses on
benchmarks where there is a desirable outcome, or ground-
truth that the model is expected to produce, for example the
MMLU dataset (Hendrycks et al. 2021), question answer-
ing (Liang et al. 2022), and even some more domain specific
tasks, such as standardized exams (Giannos, Delardas et al.
2023; Nunes et al. 2023).
While these types of evaluation are important, researchers
have recently been shifting their attention towards measur-
ing aspects of LLMs that are not directly related to per-
formance. These come in the form of various fairness re-
lated concerns, with recent work showing how models may
present racial and gender bias (Cheng, Durmus, and Juraf-
sky 2023), political bias (Feng et al. 2023), among others.
One way which researchers used to establish which biases
a model may show was by comparing model and human re-
sponses on a given questionnaire or benchmark (Santurkar
et al. 2023; Gurnee and Tegmark 2024).
Despite the importance of such work and the wide usage
of LLM powered tools such as ChatGPT by people of dif-
ferent countries and cultural backgrounds1, very few studies
were conducted considering languages other than English.
In this work we attempt to bridge that gap on the Brazil-
ian Portuguese language by utilizing the Exame Nacional
do Ensino M´edio (ENEM) test, which is taken by millions of
students seeking to enter a university every year and covers
the subjects learned up to high school. This test is made of
two parts: 180 objective questions from four subjects (Math,
Languages, Natural Science and Humanities) and an essay.
The idea is that by using the abundant ENEM student
data, made available publicly every year, it is possible to
compare model and human outputs in the context of the stan-
dardized test. This would be a way to evaluate which biases
LLMs may (or may not) exhibit in the Brazilian context,
as the dataset includes not only information about their an-
swers, but also about their income, city, race, gender, among
others. Thus, the models, in this context, would be biased
toward a certain group if their generated answers and essay
were to more closely resemble that subset of humans’ be-
havior, as defined in (Atari et al. 2023).
We focus on the social and economic bias, which is spe-
1https://explodingtopics.com/blog/chatgpt-users
arXiv:2408.05035v1  [cs.CL]  9 Aug 2024

--- Page 2 ---

cially relevant as Brazil has significant income disparities,
making it one of the most unequal countries globally. These
inequalities are evident between different regions, especially
the wealthier southern regions and the less affluent northern
ones. Disadvantaged groups such as female-headed house-
holds, Afro-Brazilians, and indigenous populations are dis-
proportionately represented among the poor. Workplace in-
equality in Brazil is further exacerbated by race and gender.
A study by the Brazilian Federal Institute of Geography and
Statistics (IBGE) revealed that, on average, White workers
earn 75.7% more than Black and Brown individuals, an eth-
nic category used in Brazilian censuses for mixed-race resi-
dents (IBGE 2021). Our study explores LLM models to as-
sess if the key indicators of inequality in Brazil are mirrored
in the models using the large data collection from ENEM.
Since the language models performance is related to their
pre-training data, we opt to use both Portuguese pre-trained
models (MariTalk) as well as multilingual models (GPT-3.5
turbo, GPT-4) aiming to answer the following questions:
• How do the models stack against one another in the con-
text of ENEM?
• Which socioeconomic biases do these models show in
the context of ENEM (if any)?
• When considering the text generated for the essays,
which groups would it belong to if written by a human
(if any)?
• Are there significant differences between the LLM gener-
ated and human written essays? If such differences exist,
what are the specific aspects of syntactic complexity that
are affected, and to what degree?
We find that MariTalk and GPT-4 are generally more pro-
ficient than GPT-3.5 in the subjects of Languages and Hu-
manities in Brazilian Portuguese, while both GPT models
are far superior in natural sciences. In the Math test, all mod-
els show subpar results, with lower than 33% accuracy when
considering those questions. Despite the models appearing
to be closer to the higher socioeconomic status groups, we
find little evidence of bias in the multiple-choice tests, as
the probability of a LLM getting the answer correct plays a
much bigger part in the increase in similarity between model
and human answers than their actual socioeconomic status.
Additionally, we find that the models seem to be closest to
humans in tests where it performs worse (Natural Sciences
and Math) due to less confident predictions, which leads to
more well distributed probability among alternatives, better
matching human tendencies.
When comparing the essays generated by the LLMs and
human written text, we observe that they are not all that sim-
ilar, as, despite being pre-trained with human data, the mod-
els’ choice of words is significantly different from that of
the exam takers. This difference manifests itself in a very
distinct choice of words by the models coupled with a sig-
nificant difference in the linguistic properties of the text
produced by the LLMs, which show much less variance in
the number of words for each essay. Additionally, the ma-
chine produced texts differ from humans on a variety of
syntactic complexity metrics, generating on average longer
clauses, but shorter sentences and less phrases per clause,
while also using less T-units per sentence. These combine
to form model created text that is different in form and in
content when contrasted with human ENEM essays.
This research comes in a context where an increasing
number of studies position LLMs as if they were human,
applying both objective and subjective human tests or ques-
tionnaires (Pan and Zeng 2023; Atari et al. 2023) in an at-
tempt to show what kind of human these models would be in
our society. By exploring the objective multiple choice ques-
tions and the subjective ENEM essay, we seek to expand
the understanding of how these models may relate to actual
human capabilities. Our findings indicate that, for Brazil-
ian Portuguese, LLM capabilities are inconsistent with hu-
mans regardless of their origin or status, showing no biases
of this kind. Our findings align with previous work which
drew similar conclusions in very different situations (Ma-
howald et al. 2024; Pavlick 2023). Our work complements
previous research in this vein by directly contrasting LLMs’
outputs with plentiful, real-world, human-generated data.
Related Work
Due to ENEM’s multidisciplinary nature, sporting 45 ques-
tions for each of four distinct subjects - Humanities, Math,
Natural Sciences, and Languages - the test has been used
as a benchmark for models in the Brazilian Portuguese lan-
guage. For example, in (Nunes et al. 2023), Nunes et al.
use questions extracted from ENEM as a way to evaluate
GPT-3.5 and GPT-4. They found the latter to be an improve-
ment in performance, especially in conjunction with Chain-
of-Tought prompting. More recently, the test has been in-
cluded in the Portuguese Evaluation Tasks (Poeta) bench-
mark, used to compare Sabi´a (Pires et al. 2023), a model
pre-trained in Portuguese text, with models such as GPT-4,
GPT-J and LLama, among others.
ENEM candidate microdata2 has also been a source of
inspiration for research aiming to understand the influence
of external factors on test results. Many studies (Travitzki,
Calero, and Boto 2014a; Figueirˆedo, Nogueira, and Santana
2014) have reported that socioeconomic conditions are some
of the main factors on both the students and school average
result in the test. These same data are now used by us in
an attempt to analyze how the tendencies of these different
groups of students may relate to the biases of a large lan-
guage model and may ultimately affect its performance. One
common way of stratifying students is the socioeconomic
status (SES) metric, which combines features in the candi-
date microdata to enable more robust analysis (Soares and
Alves 2023). This metric is currently being used by INEP,
the body responsible for ENEM, to contextualize the results
of their audits ( Instituto Nacional de Estudos e Pesquisas
Educacionais An´ısio Teixeira — INEP 2023, 2014).
In light of the immense impact and rapid spread of the
newer LLMs (Walsh 2022), especially ChatGPT, exploring
their possible biases is crucial as they may extend or am-
plify the prevailing views in society. Motoki et al. (Motoki,
Pinho Neto, and Rodrigues 2023) investigate the political
2https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-
abertos/microdados/enem

--- Page 3 ---

leanings of ChatGPT by employing a clever strategy of ask-
ing the chatbot to impersonate public figures. They find that
the model shows systematic left leaning political bias, in-
cluding in regards to Brazilian politicians such as Lula. Sim-
ilarly, Feng et al. (Feng et al. 2023), observes that GPT mod-
els tended to be more libertarian, likely due to the influence
of web text in the pre-training corpora.
Nevertheless, the bias held by LLMs is not solely po-
litical. Kotek et al. (Kotek, Dockum, and Sun 2023) indi-
cate that many models perpetuate gender stereotypes, while
Atari et al. (Atari et al. 2023) present evidence that ChatGPT
is biased towards Western, Educated, Industrialized, Rich,
Democratic (WEIRD) societies. According to their findings,
these were the populations ChatGPT most closely resembled
when answering the World Values Survey (WVS). Such bi-
ases, in the context of ENEM, may lead to prejudiced or
incorrect answer distributions that better reflect the world
views of a subset of students.
An integral part of the effort of finding how these biases
may relate to the real-world is by comparing the LLMs’
responses with real human data. One common path taken
by researchers is to take public questionnaires, surveys and
other means that divulge their results. In this vein, Dillion et
al.(Dillion et al. 2023) compare humans and LLMs as par-
ticipants in psychological science, finding that these mod-
els’ moral judgments are generally well aligned with human
ones. Back in the context of the WVS, Durmus et al. (Dur-
mus et al. 2023) contrast human and AI responses, finding
that, by default, the model responses most resemble western
countries, even when prompting in non-English languages.
They also find, however, that by asking the model to con-
sider a certain country’s perspective, the response gets closer
to the actual population responses, in some cases reflecting
a harmful stereotype instead.
Data Preparation
Socioeconomic Status
The Socioeconomic Status (SES) index follows method-
ological developments to capture families socioeconomic
status of students performing proficiency tests such as the
Brazilian ENEM (Soares 2004). The index should capture
parents’ education, family wealth, and home educational
resources. The literature on the determinants of education
quality and quantity stresses the importance of family de-
terminants in school proficiency, in contrast to the effect of
school material resources.
Coupled with academic developments towards construct-
ing the SES index, the Brazilian Ministry of Education
(MEC) research institute (INEP) adopted a methodology fit-
ted to their proficiency tests that would capture the socioe-
conomic gradient. This paper replicates the suggested offi-
cial methods to calculate the individual SES indices ( Insti-
tuto Nacional de Estudos e Pesquisas Educacionais An´ısio
Teixeira — INEP 2023). Following this methodology, it is
possible to stratify the socioeconomic status of the students
participating in the ENEM exam.
In this process, it is worth noting that the features uti-
lized were the ones common to both the ENEM question-
naire and the Basic Education Assessment System (SAEB)
survey, used in the methodology. The description of those
features can be seen in Appendix A. Appendix D specifies
category descriptions, highlighting the significance of the
questionnaire answers for each level. Note that lower lev-
els represent more vulnerable and less advantaged groups,
whereas higher levels indicate wealthier groups.
ENEM Dataset
The ENEM exam consists of four sections — Languages,
Humanities, Natural Sciences, and Math — each contain-
ing 45 multiple-choice questions with 5 options (A-E). Five
questions of the Languages section are dependent on the
candidate’s foreign language of choice — English or Span-
ish. Each question pertains to an ability from the official Ref-
erence Matrix 3, which allows for their grouping into 30 dis-
tinct competencies. Additionally, candidates must write an
essay on a topical subject. All 180 questions are made pub-
licly available every year, alongside the official answer key.
In every application, there are different color variants of
ENEM, containing mostly the same questions but in differ-
ent orders. This is done for two reasons: to avoid cheating
and also to allow for different tests to be created for people
with disabilities. In this work, we use the orange tests for
evaluating the language models, as they are made for peo-
ple with vision impairment, and, as such, all images are fol-
lowed by detailed descriptions, which may help the LLMs
to better answer the questions. We compile these data for
2022 to create a dataset used to prompt the models. Each
entry in the dataset consists of the question, the 5 possible
answers, the correct answer, the year, the subject and the
language of the question (Portuguese, English or Spanish).
Table 1 shows an example of one such question translated to
English.
Question 55
Born in Lebanon, two sisters could not be registered in the
country, because it is required that children born in Lebanon
be born to Lebanese fathers and mothers. Their parents, of
Syrian nationality, were also unable to register them in their
country of origin. In Syria, children are only registered by
officially married parents, which was not their case. In sit-
uations like the one presented in the text, when people are
born they are already in the socio-political condition of:
A: exiled
B: stateless
C: fugitives
D: refugees
E: clandestine
Correct answer: B stateless
Year: 2022, Subject: Humanities, Language: Portuguese
Table 1: Example of a question from ENEM translated to
English.
3https://download.inep.gov.br/download/enem/matriz
referencia.pdf

--- Page 4 ---

SES
Lang.
Humanities
Nat. Sci.
Math
All
I
0.68
0.66
0.24
0.27
0.47
II
0.70
0.66
0.26
0.31
0.49
III
0.76
0.73
0.28
0.38
0.54
IV
0.80
0.73
0.28
0.40
0.56
V
0.80
0.73
0.33
0.43
0.58
VI
0.86
0.82
0.42
0.56
0.67
VII
0.88
0.86
0.55
0.59
0.72
VIII
0.90
0.88
0.60
0.68
0.77
Table 2: Average percentage of correct answers per ENEM
subject by SES level. Notice how the percentage grows dras-
tically with the increase in socioeconomic status.
In addition to the answer keys, questions, and compe-
tencies, INEP, the government organization responsible for
ENEM, also makes available the data from the test takers
in the form of what they call the “ENEM microdata”. This
includes a questionnaire about the students socioeconomic
status, all their answers and grades, their gender, race, and
age, as well as data about their school (city, public or pri-
vate, etc). That is the information we use to compute the
SES metric described in the section Socioeconomic Status.
We compile these data in a human answer dataset, where,
for every question, we calculate the answer distribution
for all humans that answered that question, regardless of
test color. This is made possible by the existence of a
unique identifier for every distinct question. We also calcu-
late the same distributions aggregated by socioeconomic sta-
tus (SES). A summary of the performance in ENEM for the
different SES levels can be seen in Table 2.
Parallel to the multiple-choice ENEM dataset, we also
compile a collection of human written 2022 ENEM essays
from two sources. The first set of these is comprised of the
27 publicly available maximum grade (1000) essays writ-
ten by ENEM candidates for the official exam. The sec-
ond contains 34 user-submitted essays graded according
to the ENEM criteria, sourced from Brasil Escola, a rep-
utable website4 widely used by Brazilian students. Ideally,
we would have all of the essays written for the ENEM test.
However, most of them are private, with only a few top-
scorers being publicized each year, hence why we settled
for these 61 samples with varying grades.
The official list of metrics for ENEM essay evaluation is
public information5. A summary of these guidelines can be
found in Table 3. In short, students must write a cohesive,
well-developed and grammatically correct text on a specific
political problem. They must make an educated use of inter-
textuality, mentioning relevant cultural artifacts to substanti-
ate their arguments. Finally, they must conclude their essay
with an intervention proposal to solve the given problem.
The theme for the 2022 edition of the exam was “Challenges
4https://vestibular.brasilescola.uol.com.br/banco-de-
redacoes/tema-desafios-para.htm
5https://www.gov.br/inep/pt-br/centrais-de-conteudo/acervo-
linha-editorial/publicacoes-institucionais/avaliacoes-e-exames-
da-educacao-basica/cartilha-de-redacao-do-enem-2022-
participante
Criterion
Description
C1
Adherence to appropriate vocabulary and gram-
mar.
C2
Pertinence and variety in cultural repertoire.
C3
Coherence and effectiveness of rhetoric.
C4
Cohesion in the linkage of ideas.
C5
Inclusion of a proper intervention proposal.
Table 3: Summary of official criteria for essay evaluation in
the ENEM exam.
in valuing traditional communities and peoples in Brazil”.
Large Language Models
When choosing which LLMs to evaluate in the ENEM
dataset, we wanted to strike a balance between models that
are widely used in society and models that are tailored for
the Brazilian Portuguese language. For this reason, we chose
GPT-3.5 turbo (henceforth GPT-3.5) and GPT-4 as the popu-
lar multilingual representatives, and MariTalk as a Brazilian
alternative to them. As the OpenAI models support the Por-
tuguese language6, they should be capable of interpreting
ENEM questions and essay topics.
Prompts for Multiple-Choice Questions
The prompting strategies implemented in this project are de-
signed to reflect real-world scenarios. In this context, the
zero-shot method is chosen as it enables the models to uti-
lize their inherent linguistic and contextual understanding
to mostly unseen questions. Consequently, our prompt con-
sists of just an instruction, followed by the question data. For
Maritalk, we utilized an instruction in Portuguese, whereas
for both GPT-4 and GPT-3.5, we opted to use the English
translation of the instruction.
While using English instructions may introduce a small
extent of language bias, it helps prevent the GPT models
from misinterpreting its task and producing unexpected an-
swers, which directly compromises our methodological ap-
proach. The exam questions for all models, however, remain
in Portuguese, preserving the original linguistic context and
still enabling an adequate assessment of the model’s com-
prehension and accuracy. The exact text used for the prompt
can be seen in Appendix B .
To communicate with the GPT models, we employed the
Chat Completions API 7. The same set of parameters were
used for both of them. First, we set a seed value of 10, to en-
sure reproducibility, and a temperature value of 0, enforcing
the model to generate the most likely answers. Furthermore,
we limit the tokens generated through max tokens = 1, tai-
loring the specific need for an objective and single answer,
and select the top logprobs value as 5, in order to match the
five alternatives presented in the exam question. Lastly, the
logprobs parameter was set to true, enabling the model to
produce the log probabilities for the generated token.
6https://help.openai.com/en/articles/8357869-chatgpt-
language-support-alpha-web
7https://platform.openai.com/

--- Page 5 ---

Having the logprobs for each token is important to our
methodology, as it offers a cost-effective strategy to as-
sess the GPT models probability distributions. This pro-
cess bypasses the intensive task of generating a large num-
ber of samples. Instead, the log probabilities represent the
model’s unnormalized outputs, allowing us to apply a soft-
max function to obtain a precise probability distribution for
each answer choice. Furthermore, recognizing that the top
5 log probabilities might not exclusively correspond to the
expected 5 answer options in all responses, we have de-
vised a method to address this scenario. Our approach in-
volves filtering out unexpected responses and subsequently
redistributing the probabilities among the remaining valid
choices. This ensures that our analysis remains standardized
and reliable.
We used the API for MariTalk, with default parameters,
since that is the configuration that most users of the model
will encounter, except for max tokens = 1, which, as stated
previously for the GPT models, sums up the answer. Since
we could not directly assess MariTalk’s model probability
distributions, we sampled 100 answers for each question,
in order to get a probability distribution, hence we set the
do sample parameter to true. After the samples were gener-
ated, they were parsed by selecting the answers that clearly
stated the alternative, either by choosing a letter between A
and E, or by copying/rephrasing one of the possible options.
Furthermore, responses that did not choose any alternative
by the end of the text were considered as unanswered.
Prompts for Essay Generation
For instructing the aforementioned models on the essay task,
we use the text generation endpoints using the default pa-
rameters, as we expect that would be the configuration most
real users would use. Additionally, we consider both pos-
sible configurations for each of following prompting deci-
sions, totaling four distinct prompting strategies:
• Explicit system prompting: We analyze whether in-
cluding certain instructions in accordance to the essay
evaluation criteria leads to an increase in the quality of
the generated texts. In particular, we ask the model to
“write an ENEM-style essay” and “make use of cultural
references, such as books and philosophers”. We also list
the details needed for an intervention proposal. Finally,
we limit the essay to 500 words, given that students must
not write more than 30 lines of text.
• Inclusion of sample texts: The official ENEM exam
presents students with a few sample texts to better their
understanding of the essay topic. Although students must
not copy directly from them, these texts are helpful in
clarifying how examiners expect candidates to approach
the topic. As such, we find it relevant to test their effect
on model-generated answers.
The use of varying prompts is justified on the basis that
the generated essay is sensible to instructional choices (Gi-
ray 2023). By prompting the model in the four manners de-
scribed, we ensure that the resulting texts are not overly de-
pendent on the precise instructions fed to the machine. Thus,
we better emulate real interactions between LLMs and po-
tential users.
In total, for each LLM, we generate 100 essays, split
evenly among the four prompting strategies. The exact
prompts are replicated in Appendix C . Although our work
can be expanded to a larger sample size, we choose to ana-
lyze only so many essays, as we have a limited number of
human counterparts (see the section ENEM Dataset). This
sample size, albeit relatively small, was enough for us to
find statistically significant differences between the gener-
ated texts and humans.
Having generated the model responses, we opted to re-
move any extraneous text that did not match the structure
of the ENEM essay. This includes section headers and bul-
let points, which were sometimes added at the end of the
file. For uniformity’s sake, we also chose to exclude titles,
as those are optional in the official exam. The main body of
the essays remained intact, and was not subject to manual or
automated corrections of any type.
The Multiple-Choice Tests
In this section, we analyze the LLMs performance on the
ENEM objective questions, contextualizing it with human
performances and socioeconomic aspects. We start by look-
ing into the accuracy of each of the studied LLMs in the
objective tests. Then, we show the similarity between these
results and the human results in the test, stratified by the
different human SES groups. Finally, we contextualize how
this translates to actual biases.
Evaluating LLMs on ENEM
For this inspection, we consider only non-void questions
from the 2022 orange variant of the ENEM exam. We as-
sess the performance of the models over 184 questions in
total (Languages = 50, Humanities = 45, Natural Sciences =
45, Math = 44).
The three models share a common pattern: decent accu-
racy in Languages and a great performance in Humanities,
followed by comparatively mediocre results in Natural Sci-
ences and Math (Table 4). At first glance, this distribution
seems to reflect how hard each section is. On the whole, ac-
cording to ENEM microdata, Brazilian students do worse in
Math and Natural Sciences than in other subjects.
Model
Lang.
Humanities
Nat. Sci.
Math
GPT-3.5
0.76
0.87
0.58
0.29
GPT-4
0.84
0.93
0.71
0.23
MariTalk
0.82
0.95
0.72
0.29
Table 4: Accuracy by model for each exam section.
However, it is debatable whether human-measured diffi-
culty is the most influential factor on model performance.
Rather, question structure might be more significant. Most
Natural Sciences and Math items require complex, multi-
step reasoning — at which LLMs appear to struggle (Chen
et al. 2024). In contrast, the Languages and Humanities sec-
tions mainly comprise general knowledge and interpretation

--- Page 6 ---

tasks. As such, given their natural language processing ca-
pabilities, LLMs achieve better results in these sections.
Although LLM scores come across as human-like on the
surface, it is unrealistic to claim they stem from the same
variables that impact regular ENEM participants. In the fol-
lowing sections, we delve deeper into the differences be-
tween human and LLM behavior.
Comparing Humans and LLMs on the Objective
Tests
Given the set of ENEM questions(Q) discussed previously,
we compute the similarity of the answer(a) distributions
from the set of students(H) with the responses from the set
of models(M). We chose the Jensen-Shannon(JS) distance
as the similarity metric due to the fact that it is symmetric
and finite, but any other metric adequate for probability dis-
tributions could be used.
In mathematical terms, given the answers for question q
defined as ai ∈Aq = {A, B, C, D, E, ∗}, we calculate the
probabilities distributions for each question for the humans
as:
PH(a|q) = na,q
nq
, ∀a ∈Aq, q ∈Q
where nq denotes the total number of answers to question q
and na,q denotes the number of specific answers to question
q.
Whereas the probability for the OpenAI models is defined
as:
Pm(a|q), ∀a ∈Aq, q ∈Q, m ∈M
where Pm(a|q) is the probability of model m outputting an-
swer a given question q.
For MariTalk, the calculation resembles humans, as we
sample S = 100 responses for the model before using those
samples to calculate the probabilities:
Pm(a|q) = na,q
S , ∀a ∈Aq, q ∈Q
Thus, the similarity over all questions, between humans
and a model, is calculated as:
Similarity(m, H) = 1
N
N
X
q=1
JS(Pm(Aq|q), PH(Aq|q))
Since we opt to use the base 2 logarithm for the Jensen-
Shannon distance, it is bounded in the interval [0,1].
Note that the set of questions may change depending on
the context of an analysis. For example, if we compare the
results of humans and models over the entire test, Q will be
the 185 questions that comprise ENEM, meanwhile, if we
decide to focus on a specific subject, Q will be the questions
related to that instead.
Figure 1 illustrates the relationship between SES levels
and the JS distance between human and models’ distribu-
tion. It is possible to see that for most tests, an increase in
economic condition is correlated with a reduction in dis-
tance to the models, with the exception of the Math test -
see Figure 1d. We reckon this happens due to the worse per-
formance and lower probabilities attributed to the correct an-
swer by the models in this test, which more closely matches
Model
Probability
GPT-3.5
0.747 +- 0.003
GPT-4
0.896 +- 0.002
MariTalk
0.833 +- 0.002
Table 5: Average probabilities of the alternative most likely
to be chosen by the LLM in the multiple-choice questions.
the fact that most Brazilian students also do badly, especially
those of lower SES. Notice how, despite this tendency, the
difference between adjacent SES levels is not statistically
significant, especially for the Natural Science test (Figure
1c).
These results could suggest that the model is biased to-
wards groups with higher socioeconomic status. However,
there is another possibility: the lower distance is determined
not by bias, but rather by the probability of both the model
and the socioeconomic group getting an answer correct. We
will expand on that in the next section.
It is also interesting to discuss about the models, where we
see that for all subjects GPT-3.5 is closest to humans. This
is notable as it happens both in subjects where GPT-3.5 is
beaten by all other models, as well as in subjects at which it
excels. This is likely due GPT-3.5 being less confident in its
response, whereas the other models tend to assign extremely
high probabilities to one of the answers - see Table 5. Since
humans are unlikely to all choose the same answer, this un-
certainty makes GPT-3.5 answers the most human like, even
in tests where it does worse than the average human.
Isolating the Effect of SES
In the previous section we observe that, for most subjects,
the distance between human and model answer distribu-
tions shrink as the SES level grows. However, it remains un-
clear whether this is due to an intrinsic socioeconomic bias
of the large language models or if it is simply a result of
these wealthier levels demonstrating higher accuracy, which
matches the high accuracy of the studied models. This rela-
tionship between socioeconomic status and human standard-
ized test results has long been noted in previous research,
such as (Zwick 2002) in the US and (Travitzki, Calero, and
Boto 2014b) in Brazil.
To isolate the effect, it is desirable to model the overlap
between a model answer probabilities and each human an-
swers given the accuracy of the human and their SES score.
We define this overlap for each human as:
O(h, m) =
N
X
q=1
Pm(Aq = aq,h)
N
where aq,h is the human response to question q, while
Pm(Aq = aq,h) is the probability of model answering the
same as the human. This metric measures the average prob-
ability of a model generating the same answer of a given
human.
Figures 2 and 3 show the relationship between human ac-
curacy and overlap, and SES score and overlap, respectively,

--- Page 7 ---

I
II
III
IV
V
VI
VII
VIII
SES Level
0.0
0.1
0.2
0.3
0.4
0.5
0.6
Distance
Distance to MariTalk
Distance to GPT-3.5
Distance to GPT-4
(a) Distance between human and models’ probability distributions
by SES level in the Languages ENEM test
I
II
III
IV
V
VI
VII
VIII
SES Level
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Distance
Distance to MariTalk
Distance to GPT-3.5
Distance to GPT-4
(b) Distance between human and models’ probability distributions
by SES level in the Humanities ENEM test
I
II
III
IV
V
VI
VII
VIII
SES Level
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Distance
Distance to MariTalk
Distance to GPT-3.5
Distance to GPT-4
(c) Distance between human and models’ probability distributions
by SES level in the Natural Sciences ENEM test
I
II
III
IV
V
VI
VII
VIII
SES Level
0.0
0.1
0.2
0.3
0.4
0.5
0.6
Distance
Distance to MariTalk
Distance to GPT-3.5
Distance to GPT-4
(d) Distance between human and models’ probability distributions
by SES level in the Math ENEM test
Figure 1: Distance between human and models’ probability distributions by SES level by ENEM test subject. The error bars
represent the 95% confidence interval.
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Human Accuracy
0.1
0.2
0.3
0.4
0.5
Answer Overlap with GPT-3.5
Figure 2: Relationship between human accuracy and the
overlap with GPT-3.5 answers. Notice how the relationship
is almost linear.
for the GPT-3.5 model. It is evident from the figures that the
overlap is highly correlated (Pearson’s correlation = 0.94,
p<0.001) with human accuracy, although the effect of SES
score is not as clear, despite moderate correlation (Pearson’s
correlation = 0.41, p<0.001). It is important to note that hu-
man accuracy and SES score are only moderately correlated
(Pearson’s correlation = 0.44, p<0.001), with the amount
to which they correlate decreasing as SES gets higher, thus,
human accuracy is not a proxy for SES.
We opt to use a linear regression to model the effect of
both human accuracy as well as SES score on the overlap.
Table 6 shows the results for the multiple regressions for
each LLM. We also investigate linear regressions for the
2
3
4
5
6
7
8
SES Score
0.1
0.2
0.3
0.4
0.5
Answer Overlap with GPT-3.5
Figure 3: Relationship between human SES Score and the
overlap with GPT-3.5 answers.
GPT-3.5 using individual features, aiming to ascertain the
impact of each predictor when isolated (Table 7).
We find that, although both human accuracy and SES
score are statistically significant predictors for the overlap,
most of the variance can be explained by using human ac-
curacy alone. In fact, adding SES score to the model does
not improve R2. Interestingly, when considering SES as the
only feature, it appears with a positive coefficient (0.0321,
p<0.001), while it has a very small negative coefficient in
the multiple regression (-0.0006, p<0.001). The positive co-
efficient is possibly a consequence of the fact that a higher
SES leads to higher accuracy on average. Meanwhile, the
negative coefficient means that for a given value of human
accuracy, the model responses are on average slightly more

--- Page 8 ---

Model
Feature
Coef.
R2
Adj. R2
GPT-3.5
Constant
0.1024
0.889
0.889
Human Acc.
0.6300
SES Score
-0.0006
GPT-4
Constant
0.0779
0.904
0.904
Human Acc.
0.7539
SES Score
-0.0008
MariTalk
Constant
0.0098
0.893
0.893
Human Acc.
0.6535
SES Score
-0.0006
Table 6: Results of the multiple regression models for pre-
dicting human answer overlap with LLM by using SES score
and human accuracy as predictors. All p-values are <0.001
Model
Feature
Coef.
R2
Adj. R2
Multivariate
Constant
0.1024
0.889
0.889
Human Acc.
0.6300
SES Score
-0.0006
SES only
Constant
0.1642
0.174
0.174
SES Score
0.0321
Human Acc.
Constant
0.1003
0.889
0.889
only
Human Acc.
0.6277
Table 7: Results of linear regression analysis isolating indi-
vidual features to predict human answer overlap with GPT-
3.5 answers. All p-values are <0.001.
similar to humans of lower socioeconomic status, which
suggests that the model does not show bias towards the more
privileged groups on the multiple-choice tests. The afore-
mentioned tendencies appear for all models, but the results
for MariTalk and GPT-4 have been omitted for brevity.
The ENEM Essay
In this section, we compare LLM-generated text to real hu-
man essays from two sources: publicly available maximum
grade ENEM texts and ENEM-style essays written by stu-
dents for training purposes. Our goal is to determine how
different text produced by machines is from that produced
by real people. We first contrast syntactic metrics from the
LLM essays with the human data, aiming to find structural
differences used by either group in the Portuguese language.
Then, we study whether the choice of words of the groups
are distinct enough to allow for separation between them.
Linguistic Differences Between
Machine-Generated and Human Text
Metrics of syntactic complexity are a multidimensional basis
for the understanding of differences in writing processes (Lu
2010). Syntactic complexity refers to the range and sophis-
tication of forms that appear in language production (Ai and
Lu 2013). Historically, these metrics have been employed to
assess the writing proficiency of students learning a second
language, given the existence of a baseline against which
to gauge their performance. (Wolfe-Quintero, Inagaki, and
Kim 1998)
In this section, we employ a selection of them to com-
pare the writing abilities of native Portuguese students who
have taken the ENEM writing test, officially or otherwise,
with LLMs. As a reminder, for this analysis, we consider
the 61 human samples described in section ENEM Dataset.
In total, we use five metrics of syntactic complexity (Ai and
Lu 2013) obtained from the output of the UDPipe (Straka
and Strakov´a 2017) software with the Portuguese-Bosque
model. Using them, it was possible to analytically describe
specific elements of texts and then compare how different
types of writing resemble each other.
Some of the metrics depend on the definition of certain
terms. For instance, sentences represent complete syntac-
tic structures, comprising word sequences that articulate en-
tire expressions, questions, or commands. Within sentences,
clauses form cohesive units, containing subjects and predi-
cates to construct complete statements. Dependent clauses
rely on independent clauses for grammatical coherence,
showcasing the multifaceted nature of sentence structure. T-
units, or “thought units,” encapsulate complete ideas, com-
prising main clauses, in addition to any associated dependent
or embedded clauses (Hunt 1965). Meanwhile, coordinate
phrases merge similar syntactic elements—adjectives, ad-
verbs, nouns, or verbs—through coordinating conjunctions
like “and” or “but”, fostering cohesive expression within
sentences.
Each metric provides insights into different aspects of lin-
guistic structure and complexity. The Mean Length of Sen-
tences (MLS) measures the average number of words per
sentence, reflecting the overall sentence length and poten-
tially indicating the level of detail or complexity in expres-
sion. Similarly, the Mean Length of Clauses (MLC) and the
Mean Length of T-Unit (MLT) quantify the average num-
ber of words per clause and per T-Unit, respectively, of-
fering an indication of production unit length. The Coordi-
nate Phrases per Clause (CPC) metric assesses the frequency
of coordinate phrases within clauses, highlighting instances
where multiple syntactic elements are conjoined to convey
additional information or complexity. Finally, the T-unit per
Sentence (TS) metric calculates the ratio of T-units to sen-
tences, providing insight into the structural complexity and
cohesion of sentences.
We use these concepts to compare human and machine-
generated essays for each LLM. The average length of these
essays varies by model: GPT-3.5’s essays have an average
of 481 ± 13.27 words (mean ± std), GPT-4’s have 532 ±
11.50 words, and MariTalk’s have 382 ± 3.17 words. Con-
versely, human-written essays have an average length of 517
± 40.45 words. Notice how the length of human essays has
much more variance than the LLM generated text. This is in-
teresting as, while two prompting templates (see Appendix
) explicitly suggest 500 words (matching the typical size of
a human essay), not all of them do, which indicates that the
GPT LLMs are able to implicitly match the size of average
human essays, as seen by the average length and low vari-
ance. The same can’t be said for MariTalk.
Since we want to compare the various models with hu-
man written text, we use the aforementioned syntactic met-
rics to evaluate how their essays may or may not approach

--- Page 9 ---

Model
MLC
CPC
MLT
MLS
TS
GPT-3.5
22.03
3.02
92.16
34.50
0.41
GPT-4
21.34
2.24
58.01
32.74
0.60
Human
18.02
1.22
59.13
40.05
0.71
MariTalk
24.06
2.76
77.19
29.59
0.43
Table 8: Value of syntactic metrics for humans and language
models. It can be seen that values for the human group are
very distant from the others. It is important to note that the
differences for MLT are not statistically significant.
that of humans. Table 8 and Figure 4 show, respectively the
value of each metric as well as the z-scores associated with
each group. We can observe that all of the proposed syntactic
complexity metrics, besides MLT, show statistically signif-
icant differences when comparing human essays with LLM
generated ones.
This suggests that objective questions are not the only task
on which LLMs differ from humans in the Brazilian Por-
tuguese language, as we see similar tendencies in the subjec-
tive writing section of ENEM. It is also possible to observe
that humans tend to compose phrases using a larger quantity
of compound sentences than machines do, as evidenced by
their higher TS and lower MLC. This higher TS comes as a
consequence of humans opting for shorter clauses, resulting
in longer sentences with more clauses, as evidenced by the
MLS metric.
Furthermore, we can see that, unlike in the multiple
choice test, in the essay, GPT-4 is closer to humans across
all metrics, which could be due to its greater understanding
of natural language as a larger model. Interestingly, in spite
of being pre-trained on Brazilian Portuguese, MariTalk is
the farthest model from Brazilian students for many of the
syntactic metrics.
MLC
CPC
MLT
MLS
TS
1.0
0.5
0.0
0.5
1.0
Z-score
Human
GPT-4
MariTalk
GPT-3.5
Figure 4: Z-score for syntactic metrics. Notice that the GPT-4
model tends to be closer to humans than other models in most fea-
tures.
Comparing Human and LLM on ENEM-Style
Essays
Inspired by the text comparisons between different LLM de-
scribed demographic groups in (Cheng, Durmus, and Juraf-
sky 2023), we use a one-vs-all SVM to distinguish between
the four different categories of ENEM essays: the human es-
says, as well as those of the LLMs being tested (GPT-3.5,
GPT-4 and MariTalk).
For this analysis, we remove stopwords and represent
each text as a bag-of-words representation, which is highly
interpretable and allows us to identify which words con-
tributed most heavily for the classification. We split each
category into 70% train and 30% test data.
We find that human and LLM essays are easily separa-
ble, as we are able to achieve mean accuracy of 0.98 ± 0.02
(mean ± std), lending strength to our previous observation
that human and LLM answers are not all that similar. Ad-
ditionally, this also suggests that texts produced by different
models are also distinct. This becomes even more evident
when looking at the top words for the classification of each
group (Table 9), as we see that while human top words relate
to society and nature, with words such as country, govern-
ment, and involvement being most discriminative, GPT-3.5
seems to focus instead on actions, e.g. build, participation,
and strengthening. GPT-4 seems to focus on culture, with
words such as cultures, philosopher, traditions, and book
being among the most relevant, showing the capability of
this model to adapt to the need to include cultural reper-
toire in ENEM-style essays. Finally, MariTalk takes a dif-
ferent approach, with top words focusing on diversity and
disputes, including fight, confront, plurality, recognition and
marginalization. The dominance of these terms communi-
cates a firmer adherence to the essay’s theme of empowering
the traditional peoples of Brazil.
Group
Translated Words
Humans
Country, natural, part, shape, involvement, gov-
ernment, resources, access, threat, devaluation.
GPT-3.5
Fundamental, society, strengthening, fair, guaran-
tee, groups, build, faced, solely, participation.
GPT-4
Cultures, necessity, traditions, cultural, people,
therefore, yet, philosopher, book, land.
MariTalk
Plurality,
confront,
fight,
practice,
question,
crucial, existence, marginalization, recognition,
maintenance, formation.
Table 9: Top words for each group of generated essays. No-
tice the stark difference between human and LLM words.
The words were translated from Portuguese to English.
Discussion
As large language models become increasingly widespread
in society, the question of whom they represent is pivotal
in understanding many of the problems that may arise from
their usage. Although much has been done previously in the
English language, with a plethora of psychological, social
and political questionnaires being applied to the models, far
less has been done in Brazilian Portuguese.
Many studies focus on how the large language models
may display capabilities and generate answers similar to
those of humans on certain conditions. However, very few
studies focus instead on how these models differ from hu-
mans. In this work, we presented a case study using the 2022

--- Page 10 ---

ENEM test as a base to show a situation where human and
LLM responses are significantly different, serving as a con-
trast to previous work which attempted to study such mod-
els as if they were human (Atari et al. 2023; Pan and Zeng
2023).
While we initially sought to explore LLMs’ socioeco-
nomic biases by contrasting their outputs with humans re-
sponses made public by the large ENEM microdata, during
our research, we found no significant biases of this kind,
with similarity between model and human responses being
explained by other factors. This is true for all studied mod-
els, regardless of being pretrained on multilingual (GPT-3.5,
GPT-4) or Portuguese (MariTalk) data.
For instance, at first, when comparing human and LLM
answers in the multiple-choice test, we observed a reduction
in distance as the human group gets richer and more highly
educated for all tests except math. However, by further in-
specting these results, we find that the confounding variable,
human accuracy, is most likely responsible for that decrease,
so the higher similarity with the richest groups might not be
related to any kind of bias, but rather to the fact that higher
SES level humans tend to get more questions correct. By fit-
ting the average probability of a model generating the same
answer of a given human (O) using a linear regression, we
find that human accuracy alone is enough to explain most of
the variance of the data.
Even though we did not identify any social or economic
biases in the multiple-choice responses, we did find situa-
tions that lead the LLM responses to be closer to humans,
regardless of socioeconomic factors. In this case, they are
related to the confidence of a model in its answers. This
is exemplified by GPT-3.5 having the closest answer distri-
butions to humans despite being outperformed by the other
models in most of the subjects. This is likely due to the fact
that it tends to assign a higher mass of probability to alter-
natives other than the one that was predicted, which more
closely matches the behavior of a group of humans, as it is
highly improbable that close to 90% of candidates choose
the same alternative. Another example of this are the lower
distances between humans and all three studied models be-
ing observed in the Math test — the subject that they per-
formed worse than all but the lowest SES level.
We find analogous results when looking at the essays,
with the LLM generated text presenting syntactic proper-
ties distinct from humans. Namely, they tend to write longer
clauses and shorter sentences, with less T-units per sen-
tence. They also use more coordinate phrases per clause.
This could imply that, when compared to humans, LLM es-
says are composed by more concise phrases, with each serv-
ing a distinct mechanical purpose. In contrast, human writ-
ing often employs different structures in the same phrase to
enhance the expression of ideas, resulting in a more natu-
ral and dense writing style. In fact, the texts produced by all
models and the humans are so different that a simple bag-of-
words SVM model is enough to linearly separate the essays,
with top words for each group being related to distinct as-
pects of “traditional communities” in Brazil.
These results support the view that, although large lan-
guage models have remarkable knowledge of not only lan-
guage, but also a variety of subjects, they are, in essence,
very different from humans, with performance that is incon-
sistent with what is expected of actual people, at least in
Brazilian Portuguese. Similar inconsistency has been seen
in other contexts, as shown by Mahowald et al. (Mahowald
et al. 2024), indicating that LLMs still lack capability in
certain linguistic tasks expected of humans. Future work in
this area should strive to study language models not only by
looking at how they may approach humans in certain condi-
tions, but also at how they may differ.
Another avenue to explore is whether the same tendencies
observed in this work are also present in standardized tests
from other countries. In theory, the methods used in this pa-
per should be extendable to other languages with minimal
changes. For the essay analysis specifically, researchers may
need to take heed of the differences between languages, es-
pecially when choosing the syntactic complexity metrics.
Limitations
In this paper we, unfortunately, did not have the means to
ask human examiners to evaluate the generated essays. Thus,
qualitatively studying the ENEM essays and drawing com-
parisons between human and LLMs for each competency
students are expected to have will be left to future work.
This kind of study could be very insightful in regards to the
linguistic and cognitive inconsistencies this type of model
has been shown to have.
As LLMs continue to be updated, their knowledge cutoff
dates come ever closer to the present day — hence why we
resorted to use only the latest available version of ENEM
with microdata available (November 2022) at the time we
started our research (INEP has since released the microdata
for ENEM 2023 in Apr. 2024). Since GPT-4 has access to in-
formation from January 2022, assessing its abilities on older
exams would be unreasonable. Moreover, this issue affects
future research on this topic, as replicating our results will
prove challenging once the current models become obsolete.
Another factor to consider is the language barrier. For-
eign language questions notwithstanding, we conducted our
research using Portuguese-language items and essay topics.
As discussed by Etxaniz et al. (Etxaniz et al. 2023), LLMs
do not make use of their full multilingual aptitude unless di-
rectly prompted in English. We attempted to overcome this
hurdle by translating our instructions. As detailed in the sec-
tion Prompts for multiple-choice questions, this optimiza-
tion did, in fact, lead to a boost in accuracy.
Ethical Considerations Statement
The authors mitigate ethic concerns by solely using anony-
mous student data made available by the Brazilian Govern-
ment and not using any identifying information when com-
paring the human written text. Additionally, the AI gener-
ated content complies with the ToS for the tools used.
Positionality Statement
The social circumstances of the authors had a significant
impact on the conclusions reached in this paper. As mem-
bers of Brazilian academia, they have personal experience

--- Page 11 ---

with the ENEM exam, which has been a pillar of univer-
sity admissions since 2004. As a matter of fact, seven of the
authors got accepted to a post-secondary educational insti-
tution via a selection process largely dependent on ENEM
scores. Thus, they tackle this subject from a privileged per-
spective, in the sense that they benefited from the current
ENEM exam structure.
Additionally, the authors mostly come from a Computer
Science background and, as such, are biased in their analy-
sis of sensitive socioeconomic issues. For this reason, they
sought to collaborate with an expert in the field of demogra-
phy, who offered meaningful insight on handling these top-
ics.
On the same note, the linguistic analysis was supervised
by an experienced researcher in the field, as a way to ensure
the appropriateness of the metrics chosen.
Adverse Impact Statement
Although this work aims to question the biases inherent to
large language models, readers could misinterpret the results
as a criticism of the ENEM examination system. Thus, it is
relevant to emphasize that the performance of LLMs is not
a reliable metric for dictating the applicability of a test in a
human educational assessment context. This type of analysis
escapes the scope of this study.
On a similar note, ill-intentioned individuals might mis-
use the variance of ENEM scores between socioeconomic
groups to substantiate prejudiced rhetoric. In this respect, it
must be made clear that gaps in ENEM scores are a reflec-
tion of unequal access to quality education in Brazil, among
other problems commonly associated with income disparity
in developing countries. Please refer to works such as (Cas-
tro 2003) and (Le˜ao 2006) for more information.
References
Instituto Nacional de Estudos e Pesquisas Educacionais
An´ısio Teixeira — INEP. 2014. Nota T´ecnica - Indicador
de N´ıvel Socioeconˆomico (Inse) das Escolas.
https://
download.inep.gov.br/informacoes estatisticas/indicadores
educacionais/2011 2013/nivel socioeconomico/
nota tecnica indicador nivel socioeconomico.pdf.
Ac-
cessed: 2024-01-17.
Instituto Nacional de Estudos e Pesquisas Educacionais
An´ısio Teixeira — INEP. 2023.
Indicador de N´ıvel
Socioeconˆomico do Saeb 2021 - Nota T´ecnica.
https:
//www.gov.br/inep/pt-br/centrais-de-conteudo/acervo-
linha-editorial/publicacoes-institucionais/avaliacoes-e-
exames-da-educacao-basica/saeb-2021-indicador-de-nivel-
socioeconomico-do-saeb-2021-nota-tecnica.
Accessed:
2024-01-15.
Ai, H.; and Lu, X. 2013. A corpus-based comparison of syn-
tactic complexity in NNS and NS university students’ writ-
ing. Studies in Corpus Linguistics.
Atari, M.; Xue, M. J.; Park, P. S.; Blasi, D. E.; and Henrich,
J. 2023. Which Humans?
Castro, J. A. d. 2003. Evoluc¸˜ao e desigualdade na educac¸˜ao
brasileira. Educac¸˜ao & Sociedade, 30: 673–697.
Chang, Y.; Wang, X.; Wang, J.; Wu, Y.; Yang, L.; Zhu, K.;
Chen, H.; Yi, X.; Wang, C.; Wang, Y.; et al. 2024. A survey
on evaluation of large language models. ACM Transactions
on Intelligent Systems and Technology, 15(3): 1–45.
Chen, A.; Phang, J.; Parrish, A.; Padmakumar, V.; Zhao, C.;
Bowman, S. R.; and Cho, K. 2024. Two Failures of Self-
Consistency in the Multi-Step Reasoning of LLMs. Trans-
actions on Machine Learning Research.
Cheng, M.; Durmus, E.; and Jurafsky, D. 2023. Marked Per-
sonas: Using Natural Language Prompts to Measure Stereo-
types in Language Models. In Rogers, A.; Boyd-Graber, J.;
and Okazaki, N., eds., Proceedings of the 61st Annual Meet-
ing of the Association for Computational Linguistics (Vol-
ume 1: Long Papers), 1504–1532. Toronto, Canada: Associ-
ation for Computational Linguistics.
Dillion, D.; Tandon, N.; Gu, Y.; and Gray, K. 2023. Can
AI language models replace human participants? Trends in
Cognitive Sciences.
Durmus, E.; Nyugen, K.; Liao, T. I.; Schiefer, N.; Askell,
A.; Bakhtin, A.; Chen, C.; Hatfield-Dodds, Z.; Hernandez,
D.; Joseph, N.; et al. 2023. Towards measuring the repre-
sentation of subjective global opinions in language models.
arXiv preprint arXiv:2306.16388.
Etxaniz, J.; Azkune, G.; Soroa, A.; de Lacalle, O. L.; Ar-
texte, M.; et al. 2023. Do Multilingual Language Models
Think Better in English? arXiv preprint arXiv:2308.01223.
Feng, S.; Park, C. Y.; Liu, Y.; and Tsvetkov, Y. 2023. From
Pretraining Data to Language Models to Downstream Tasks:
Tracking the Trails of Political Biases Leading to Unfair
NLP Models. In Rogers, A.; Boyd-Graber, J.; and Okazaki,
N., eds., Proceedings of the 61st Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1: Long
Papers), 11737–11762. Toronto, Canada: Association for
Computational Linguistics.
Figueirˆedo, E.; Nogueira, L.; and Santana, F. L. 2014.
Igualdade de oportunidades: Analisando o papel das cir-
cunstˆancias no desempenho do ENEM. Revista Brasileira
de Economia, 68: 373–392.
Giannos, P.; Delardas, O.; et al. 2023. Performance of Chat-
GPT on UK standardized admission tests: insights from the
BMAT, TMUA, LNAT, and TSA examinations. JMIR Med-
ical Education, 9(1): e47737.
Giray, L. 2023. Prompt engineering with ChatGPT: a guide
for academic writers.
Annals of biomedical engineering,
15(12): 2629–2633.
Gurnee, W.; and Tegmark, M. 2024. Language Models Rep-
resent Space and Time. In The Twelfth International Con-
ference on Learning Representations.
Hendrycks, D.; Burns, C.; Basart, S.; Zou, A.; Mazeika, M.;
Song, D.; and Steinhardt, J. 2021. Measuring Massive Mul-
titask Language Understanding. In International Conference
on Learning Representations.
Hunt, K. 1965. Grammatical Structures Written at Three
Grade Levels. NCTE research report. National Council of
Teachers of English. ISBN 9789998777453.

--- Page 12 ---

IBGE. 2021.
Desigualdades Sociais por Cor ou Rac¸a
no Brasil.
https://www.ibge.gov.br/estatisticas/sociais/
populacao/25844-desigualdades-sociais-por-cor-ou-
raca.html. Accessed: 2024-01-21.
Kotek, H.; Dockum, R.; and Sun, D. 2023. Gender bias and
stereotypes in Large Language Models. In Proceedings of
The ACM Collective Intelligence Conference, 12–24.
Le˜ao, G. M. P. 2006.
Experiˆencias da desigualdade: os
sentidos da escolarizac¸˜ao elaborados por jovens pobres.
Educac¸˜ao e pesquisa, 32(1): 31–48.
Liang, P.; Bommasani, R.; Lee, T.; Tsipras, D.; Soylu, D.;
Yasunaga, M.; Zhang, Y.; Narayanan, D.; Wu, Y.; Kumar,
A.; et al. 2022.
Holistic evaluation of language models.
arXiv preprint arXiv:2211.09110.
Lu, X. 2010. Automatic analysis of syntactic complexity in
second language writing. International Journal of Corpus
Linguistics, 15(4): 474–496.
Mahowald, K.; Ivanova, A. A.; Blank, I. A.; Kanwisher, N.;
Tenenbaum, J. B.; and Fedorenko, E. 2024.
Dissociating
language and thought in large language models. Trends in
Cognitive Sciences.
Melo, R. O.; de Freitas, A. C.; de Rezende Francisco, E.; and
Motokane, M. T. 2021. Renda familiar, acesso a bolsas de
estudo e n´ıvel de educac¸˜ao das m˜aes est˜ao entre os fatores
que mais afetam desempenho dos alunos no Enem. FGV
EASP.
Motoki, F.; Pinho Neto, V.; and Rodrigues, V. 2023. More
human than human: Measuring chatgpt political bias. Avail-
able at SSRN 4372349.
Nunes, D.; Primi, R.; Pires, R.; Lotufo, R.; and Nogueira,
R. 2023.
Evaluating GPT-3.5 and GPT-4 Models on
Brazilian University Admission Exams.
arXiv preprint
arXiv:2303.17003.
Pan, K.; and Zeng, Y. 2023. Do llms possess a personal-
ity? making the mbti test an amazing evaluation for large
language models. arXiv preprint arXiv:2307.16180.
Pavlick, E. 2023. Symbols and grounding in large language
models. Philosophical Transactions of the Royal Society A,
381(2251): 20220041.
Pires, R.; Abonizio, H.; Almeida, T. S.; and Nogueira, R.
2023. Sabi´a: Portuguese large language models. In Brazilian
Conference on Intelligent Systems, 226–240. Springer.
Santurkar, S.; Durmus, E.; Ladhak, F.; Lee, C.; Liang, P.; and
Hashimoto, T. 2023. Whose opinions do language models
reflect? In International Conference on Machine Learning,
29971–30004. PMLR.
Soares, F. 2004. Quality and equity in Brazilian basic edu-
cation: facts and possibilities. The challenges of education
in Brazil, 69–88.
Soares, J. F.; and Alves, M. T. G. 2023.
UMA
MEDIDA DO N´IVEL SOCIOECON ˆOMICO DAS ES-
COLAS BRASILEIRAS UTILIZANDO INDICADORES
PRIM ´ARIOS E SECUND ´ARIOS (A Measure of the Brazil-
ian Schools’ Socioeconomic Status Using Primary and Sec-
ondary Indicators). Available at SSRN 4325674.
Straka, M.; and Strakov´a, J. 2017. Tokenizing, POS Tag-
ging, Lemmatizing and Parsing UD 2.0 with UDPipe. In
Proceedings of the CoNLL 2017 Shared Task: Multilingual
Parsing from Raw Text to Universal Dependencies, 88–99.
Vancouver, Canada: Association for Computational Linguis-
tics.
Travitzki, R.; Calero, J.; and Boto, C. 2014a. What does the
national high school exam (ENEM) tell brazilian society?
Cepal Review.
Travitzki, R.; Calero, J.; and Boto, P. 2014b. Desigualdades
Educacionais e Socioeconˆomicas na Populac¸˜ao Brasileira
Pr´e-Universit´aria: Uma Vis˜ao a Partir da An´alise de Dados
do ENEM. Revista Brasileira de Educac¸˜ao, 19(56): 675–
693.
Walsh, T. 2022.
Everyone’s having a field day with
ChatGPT–but
nobody
knows
how
it
actually
works.
The
Conversation.
Preuzeto
s
https://theconversation.
com/everyones-having-a-field-day-with-chatgpt-but-
nobody-knows-how-it-actually-works-196378.
Wolfe-Quintero, K.; Inagaki, S.; and Kim, H. 1998. Sec-
ond Language Development in Writing: Measures of Flu-
ency, Accuracy, & Complexity. National Foreign Language
Center Technical Reports. Second Language Teaching &
Curriculum Center, University of Hawaii at Manoa. ISBN
9780824820695.
Zwick, R. 2002. Is the SAT a ‘Wealth Test’? Phi Delta
Kappan, 91(4): 307–311.
Appendix A - NSE Features from ENEM
Survey Questions
Question (English Translation)
Highest educational level of the mother
Highest educational level of the father
Number of refrigerators in the house
Number of computers (or laptops) in the house
Number of bedrooms in the house
Number of televisions in the house
Number of bathrooms in the house
Number of cars in the house
Number of Wi-Fi networks in the house
Number of microwave ovens in the house
Number of washing machines in the house
Number of freezers in the house
Number of vacuum cleaners in the house

--- Page 13 ---

Appendix B - Prompt for Multiple-choice
Questions
You are designed to answer the following multiple choice
question. Without adding any extra characters, spaces, or
newline characters in the answer, provide a single alterna-
tive as the answer”.
[QUESTION]
Table 10: Prompt fed to the LLMs for each multiple-choice
task (translated from Portuguese).
Appendix C - Prompts for Essay Generation
[SAMPLE TEXTS]
Based on the sample texts above, write an ENEM-style es-
say about “Challenges in valuing traditional communities
and peoples in Brazil” in 500 words. Along the essay, make
use of cultural references, such as books and philosophers.
Finally, your conclusion must include a paragraph detailing
agent, action, means and aim. In total, your text must have
only four paragraphs.
Table 11: Prompt for essay generation (translated from Por-
tuguese). Includes explicit system prompting and sample
texts .
Write an ENEM-style essay about “Challenges in valuing
traditional communities and peoples in Brazil” in 500 words.
Along the essay, make use of cultural references, such as
books and philosophers. Finally, your conclusion must in-
clude a paragraph detailing agent, action, means and aim. In
total, your text must have only four paragraphs.
Table 12: Prompt for essay generation (translated from Por-
tuguese). Includes explicit system prompting, but does not
include sample texts.
[SAMPLE TEXTS]
Based on the sample texts above, write an essay about “Chal-
lenges in valuing traditional communities and peoples in
Brazil”.
Table 13: Prompt for essay generation (translated from Por-
tuguese). Does not include explicit system prompting, but
includes sample texts.
Write an essay about “Challenges in valuing traditional com-
munities and peoples in Brazil”.
Table 14: Prompt for essay generation (translated from Por-
tuguese). Does not include explicit system prompting or
sample texts.
Appendix D - Description of Socioeconomic
Status (SES) Levels
Level
Description
I
The majority of students have unit values of goods,
and their parent’s education ranges from incom-
plete middle school to complete middle school.
II
The majority of students have unit values of goods,
and their parent’s education ranges from incom-
plete middle school to complete high school.
III
The majority of students have unit values of goods,
with some additional services, and their parent’s
education ranges from complete middle school to
complete high school.
IV
Most students have broader values for goods and
services, and their parent’s education ranges from
complete middle school to complete high school.
V
Most students have broader values for goods and
services, and their parent’s education ranges from
complete middle school to complete college de-
gree.
VI
Most students have broader values for goods and
services, and their parent’s education ranges from
complete high school to complete college degree.
VII
The majority of students have broader and more
diverse values of goods and services, and their par-
ent’s education ranges from complete high school
to complete college degree.
VIII
The majority of students have the highest values
for goods and services, and their parent’s education
is dominated by complete college degrees.
Table 15: Socioeconomic Level Descriptions
Appendix E - Factors that Affect Student
Performance
The decision to analyze the socioeconomic level of students
was based on Brazilian research involving the National High
School Exam (ENEM) which reveals that the factor that
most affects the students’ average is precisely income (Trav-
itzki, Calero, and Boto 2014b), as previous research has
noted, every 5% increase in the number of students from
high-income families leads to an increase of about 6.25
points in the multiple-choice score in ENEM (Melo et al.
2021). Following this reasoning it was decided that the most
important factor to be taken into account in the present study
is the student’s socioeconomic level, rather than gender or
ethnicity.

--- Page 14 ---

Appendix F - The Divergence Between the
Multiple Choice Questions and the Essay
Since divulging the actual essays of students may hurt the
anonymity of the data, INEP only provides the answers of
each candidate for the multiple choice questions and the final
grades. Thus, we only have the texts of students who chose
to publicize their essays, limiting the sample size.

```
