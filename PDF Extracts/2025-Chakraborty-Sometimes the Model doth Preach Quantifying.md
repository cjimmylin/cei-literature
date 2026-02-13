---
title: "2025-Chakraborty-Sometimes the Model doth Preach Quantifying - PDF Extract"
source_pdf: "2025-Chakraborty-Sometimes the Model doth Preach Quantifying.pdf"
pages: 10
extracted_at: "2026-02-13T09:15:43.941877"
---

# PDF Extract: 2025-Chakraborty-Sometimes the Model doth Preach Quantifying

**Source PDF:** 2025-Chakraborty-Sometimes the Model doth Preach Quantifying.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Sometimes the Model doth preach: Quantifying Religious Bias in Open LLMs
through Demographic Analysis in Asian Nations
Warning: This paper contains content that may be potentially offensive or upsetting.
Hari Shankar1, Vedanta S P2, Tejas Cavale1, Ponnurangam Kumaraguru1, Abhijnan
Chakraborthy3
1IIIT Hyderabad
2IIIT Kottayam
3IIT Kharagpur
Abstract
Large Language Models (LLMs) are capable of generating
opinions and propagating bias unknowingly, originating from
unrepresentative and non-diverse data collection. Prior re-
search has analysed these opinions with respect to the West,
particularly the United States. However, insights thus pro-
duced may not be generalized in non-Western populations.
With the widespread usage of LLM systems by users across
several different walks of life, the cultural sensitivity of each
generated output is of crucial interest. Our work proposes a
novel method that quantitatively analyzes the opinions gen-
erated by LLMs, improving on previous work with regards
to extracting the social demographics of the models. Our
method measures the distance from an LLM’s response to
survey respondents, through Hamming Distance, to infer the
demographic characteristics reflected in the model’s outputs.
We evaluate modern, open LLMs such as Llama and Mistral
on surveys conducted in various global south countries, with a
focus on India and other Asian nations, specifically assessing
the model’s performance on surveys related to religious toler-
ance and identity. Our analysis reveals that most open LLMs
match a single homogeneous profile, varying across different
countries/territories, which in turn raises questions about the
risks of LLMs promoting a hegemonic worldview, and under-
mining perspectives of different minorities. Our framework
may also be useful for future research investigating the com-
plex intersection between training data, model architecture,
and the resulting biases reflected in LLM outputs, particu-
larly concerning sensitive topics like religious tolerance and
identity.
Introduction
Data and trends over the past decade reveal contrasting nar-
ratives about the evolving role of religion in societies world-
wide (Storm and Wilson 2024). In the United States, Aus-
tralia, New Zealand, and various Western European coun-
tries, there has been a notable decline in the perceived
importance of religion (Pew Research Center 2022). For
instance, the proportion of self-reported Christians in the
United States dropped from 78% to 63% within the last
decade (Pew Research Center 2021). In contrast, data from
South Asia suggest a stronger alignment between religion
and politics. In these regions, voters often favor leaders who
share their religious beliefs and advocate for the interests of
their religious communities, underscoring the enduring in-
fluence of religion in shaping societal and political prefer-
ences (Pew Research Center 2024). Similarly, surveys con-
ducted across Europe highlight a divide in social attitudes.
Respondents in Central and Eastern Europe were found to be
less accepting of individuals from Jewish or Muslim back-
grounds as part of their family compared to those in West-
ern Europe, signaling regional differences in religious toler-
ance (Pew Research Center 2018).
The rise of Large Language Model (LLM) powered AI
chatbots like ChatGPT and Claude1 has significantly trans-
formed the way people engage with the Internet and seek in-
formation, including topics related to religion. Traditionally,
individuals relied on search engines and resultant websites to
explore religious teachings and discussions. Now, many turn
to conversational AI for direct answers about faith, practices,
and even moral dilemma (Johnson 2023). This shift reflects
the broader trends in religious attitudes discussed earlier, as
societies worldwide navigate differing perspectives on re-
ligion’s role in everyday life. In regions where religion is
deeply intertwined with identity and governance, an LLM’s
ability to provide nuanced and culturally sensitive responses
may hold particular significance. On the other hand, in sec-
ularizing societies, an LLM could become a tool to foster
interfaith understanding or addressing questions from an in-
creasingly diverse population (Venkit 2024).
However, this evolution raises critical questions: How ef-
fectively can AI systems understand and convey the com-
plexities of religious concepts, which are often deeply per-
sonal and context-specific? Are these systems capable of
remaining unbiased, or do they inadvertently reflect soci-
etal or cultural biases embedded in their training data? In
this paper, we analyze how various LLMs respond to ques-
tions pertaining to religious identity. We seek to determine
whether any model responds in a manner that does not re-
flect the religious sensibilities of the population. We con-
sider Open LLMs such as Llama (Touvron et al. 2023) and
Mistral (Jiang et al. 2023), as opposed to other closed LLMs
such as ChatGPT or Claude. An Open LLM is a language
model with publicly accessible architecture, training code,
and often pre-trained weights, enabling anyone to use, mod-
ify, and share it. This openness is valuable as it allows devel-
1https://chatgpt.com; https://claude.ai
arXiv:2503.07510v1  [cs.CY]  10 Mar 2025

--- Page 2 ---

Figure 1: Summarizing Model Profiles. Model Profiles are specific to the surveys used to create them. Colour code for countries:
Purple - India. Blue - Countries from Southeast Asia Survey. Red - Countries from East Asia Survey.
opers to customize or enhance the model more easily com-
pared to closed LLMs.
Our work aims to profile different LLMs by different so-
cial demographics. Our analysis is the first step in under-
standing the model’s biases on the topic, which may then
be used to create safety guard-rails to mitigate the same.
We propose a novel method to determine the demograph-
ics reflected by the model that recognizes the interconnected
nature of different demographic variables such as Age and
Education Level, etc. We release the codebase for our ex-
periments and results publicly on GitHub.2 In addition to
this, we also examine the effectiveness of instructing LLMs
within prompts to respond as though they belonged to any
particular group. Our results indicate no significant variation
in the model’s profile by virtue of this method.
2https://github.com/HariShankar08/LLMOpinions
Background and Related Work
Religion and the Internet
Usage of the Internet as an avenue of proliferating religion
has been examined in the past. Works conducted in predom-
inantly Muslim societies such as Indonesia suggest that in-
dividuals belonging to younger generations are increasingly
turning to social media to learn about religion (Thoriquttyas
et al. 2021). The COVID-19 pandemic also brought about
changes to the ways people approached worship; for exam-
ple, on the 27th of March, 2020, Pope Francis gave a special
Urbi et Orbi blessing in an empty St. Peter’s Square, acces-
sible to the public only through television or Internet stream-
ing (Watkins 2020). Applications such as Zoom, Microsoft
Teams and Google Meet have also been used by different
religious institutions as a platform to provide their services
to the public. Additionally, various software systems such
as ParishSoft3, have been developed over the years to aid in
religious teaching (Hamdelsayed and Atwell 2016), which
3https://www.parishsoft.com/religious-education/

--- Page 3 ---

have correspondingly evolved with the advent of conversa-
tional AI, and LLMs. More recent studies have examined the
usage of LLMs such as ChatGPT in aiding in biblical stud-
ies (Chrostowski and Najda 2024). While such systems may
stand the risk of providing erroneous information, we ob-
serve that on average, LLMs provide satisfactory responses
to the user’s queries.
Human-LLM interaction
The term LLM refers to Large Language Models, which are
AI systems trained on large amounts of textual data, gen-
erally sourced from the Internet and other publicly available
resources. Most common LLMs build off the generative pre-
trained transformer (GPT) architecture (Radford 2018), and
are capable of generating coherent, natural language text.
Several significant works in the past have been conducted to
evaluate the performance of these models on tasks such as
language understanding (Hendrycks et al. 2021). Our work
instead focuses on situations where LLMs may be used
to aid the human learning and decision-making processes.
ChatGPT has been documented to aid users in several differ-
ent aspects of day-to-day life, such as mental health (Stade
et al. 2024), and relationship advice (Hou, Leach, and Huang
2024). Our work seeks to examine LLMs under a similar
lens, by evaluating how these systems may be used to aid a
user in exploring their religious identity.
Profiling LLMs
Our study takes inspiration from previous work by Santurkar
et al. (2023) which profiled LLMs on the basis of various so-
cial demographics such as political ideology, household in-
come, and education level (Santurkar et al. 2023). The pro-
filing was done by prompting different models to respond to
public survey questionnaires, following which the model’s
response was compared to the actual survey respondents
belonging to the different demographic groups. The study
reported that LLMs such as GPT 3.5 (text-ada and text-
davinci models) responded to the selected survey question-
naires similar to respondents who were liberal, highly edu-
cated and belonging to higher income groups in the United
States, whereas other models (ada and davinci) responded
similar to moderate-to-conservative individuals belonging to
lower income strata. Our work profiles modern open LLMs
based on surveys held in India and various countries of East-
ern and South-Eastern Asia, where societies are noted to em-
phasize the importance of religion, collectivism and com-
munal ties as opposed to the more individualistic nature of
western nations (Maguire 2017).
The Global South
The Global South is a group of countries characterized by
shared experiences of colonialism and economic develop-
ment status, not strictly defined by geography. The group is
also frequently associated with the G77 group of nations,
including nations such as India, Indonesia and Vietnam.
Historically, many of the nations belonging to the Global
South have been marginalized in global politics, however,
Dataset
N. Respondents
India
29,999
EA
10,390
(of which) JPN
1,742
(of which) HKG
2,012
(of which) KOR
2,104
(of which) TWN
2,277
(of which) VNM
2,255
SEA
13,122
(of which) IDN
2,571
(of which) MYS
1,999
(of which) SGP
2,036
(of which) KHM
1,502
(of which) LKA
2,510
(of which) THA
2,504
Table 1: Breakdown of respondents by region: East Asia
(EA), including Japan (JPN), Hong Kong (HKG), South Ko-
rea (KOR), Taiwan (TWN), and Vietnam (VNM); Southeast
Asia (SEA), including Indonesia (IDN), Malaysia (MYS),
Singapore (SGP), Cambodia (KHM), Sri Lanka (LKA), and
Thailand (THA).
they have experienced a significant shift in wealth and po-
litical visibility in recent decades. The World Bank has ac-
knowledged a ‘shift in wealth’ from the North Atlantic to
the Asia-Pacific region, challenging conventional notions of
economic power distribution (World Bank 2024).
Dataset
For our study, we used three publicly available survey data
from the Pew Research Center (Sahgal and Evans 2021;
Evans 2024a,b), each of which offers an extensive explo-
ration of religious beliefs and practices across different
Asian societies. The datasets consist of several questionnaire
and the responses provided by the survey respondents.
The India Survey Dataset surveys the Indian public about
religious beliefs and practices, religious identity, national-
ism, and tolerance in Indian society. In addition to the In-
dia Survey, we also use two other datasets which focus on
various aspects of the survey public, including demograph-
ics, socio-economic factors, and public opinion. The East
Asian Societies Dataset, which we henceforth refer to as the
EA dataset, consists of survey responses from five different
territories: Japan (JPN), Hong Kong (HKG), South Korea
(KOR), Taiwan (TWN) and Vietnam (VNM). We also use
survey responses from South and South-East Asia Datasets,
henceforth referred to as the SEA dataset, from the follow-
ing nations: Indonesia (IDN), Malaysia (MYS), Singapore
(SGP), Sri Lanka (LKA) and Thailand (THA).
Each dataset provides a CSV file where the rows represent
individual survey responses, and the columns correspond to
the survey questions and variables used to characterize each
respondent. In addition to this, an XML metadata file is also
provided which maps the options of each survey question to
the value used to represent the same option in the responses
file.
Each respondent is identified by a unique numeric value,

--- Page 4 ---

Figure 2: Sample Survey Questions from the Indian Survey Dataset. The left table presents opinion-based questions focused on
family responsibilities and inheritance rights. The right table includes few demographic questions, such as education level and
household income.
represented in the responses files as the “QRID” of the re-
spondent. Each survey has been designed so that each re-
spondent also provides demographic information such as
age, gender, etc.
The Indian Survey dataset has a total of 308 columns,
representing survey questions as well as additional vari-
ables such as the region and ISCED-97 (UNESCO United
Nations Educational, Scientific and Cultural Organization
2003). These additional variables are directly recorded by
interviewers. Similarly, the surveys held in the East, South
and South-East Asian nations each contain a total of 174
columns.
Each survey consists of different demographic variables
which we use to profile each LLM, of these, we note the
following five common variables: Religion, Gender, Age,
Marital Status, Region and Education Level. The EA Sur-
vey Dataset additionally provides the Number of Children of
each respondent. In addition to the five variables previously
listed, we use the Urbanicity of the region to profile mod-
els in the SEA Survey countries. For the India Survey, we
are provided with the following additional variables: Caste,
Number of Daughters, and Monthly Household Income.
Language of the Surveys
In the study carried out by the
members of Pew Research Center, each survey question-
naire was developed in English, following which the ques-
tionnaires were translated and verified by professional lin-
guists having a native proficiency in the languages. For our
study, we directly use the questionnaire in English, without
any translation steps. Translation has been omitted since we
do not have the means to reliably verify the correctness of
machine-translated prompts in each of the target languages.
Additionally, as LLMs are mostly trained on English tex-
tual data, we may expect to find more biases associated with
English-speaking regions of the world, as compared to other
less represented regions.
Methodology
The Model Response
We use the term Model Response to refer to the collection
of all answers provided by the model for each question of
the corresponding survey questionnaire. For each survey, we
first determine the questions that directly probe into the de-
mographic of the respondent. This step is manual, through
which we compile two sets of questions, the Survey Ques-
tions and the Demographic Questions. We provide some ex-
amples of these questions in Figure 2.
Although the survey questionnaire instructed not to read
options for refusal or when the respondent did not know
the answer, we omit such instructions when constructing the
prompt for the model. This was achieved using regular ex-
pressions (regex). This step ensures that all options are ex-
plicitly provided to the LLM.
We prompt each model on the selected Survey Questions,
and select the option having the highest token probability
for our answer. However, to account for Prompt Sensitivity
potentially leading to different answers for the same ques-
tion (Anagnostidis and Bulian 2024), we additionally opt to
paraphrase the survey questions using Parrot (Damodaran
2021). Each prompt is run on five random seeds for ablation
purposes. Our system then selects the most frequent answer

--- Page 5 ---

Figure 3: System Overview for Model Profiling. Distance is
computed by representing both Model and Survey Response
as a Vector, following which the Hamming Distance metric
is calculated between the two vectors.
across all candidate answers, and reports this as the model’s
answer to a particular question.
Profiling the Model
The Hamming Distance is a metric originally defined in
Information Theory, measuring the number of positions at
which corresponding members of equal dimension vectors
are different (Hamming 1950). The metric is also used in the
domain of Machine Learning, to compare vectors containing
categorical variables. Our approach is largely inspired of the
K-Nearest algorithm.
dH(A, B) = 1
n
n
X
i=1
δ(Ai, Bi),
where n = |A| = |B|
(1)
δ(Ai, Bi) =
1,
if Ai ̸= Bi
0,
if Ai = Bi
(2)
The surveys also contain questions that are not applicable
to all groups within the survey public. In the case of such
questions, where a respondent has not been asked a partic-
ular question, a blank value is provided in the correspond-
ing column in the dataset files. Before computing Hamming
Distance, we drop any column which contains blank values.
Each response vector, which now strictly consists of nu-
merical values that represent the option selected, can be con-
sidered as a vector of categorical variables. This is applica-
ble as the options here do not possess any intrinsic quality
with respect to ordering. We encode all vectors using the
One-Hot Encoding algorithm, and compute the Hamming
Distance as defined in the equations 1 and 2. As lower Ham-
ming Distance suggests more similar vectors, we in turn sort
Figure 4: Detailing the different steering prompts used in our
experiments.
the survey respondents by increasing values of the metric to
get the closest respondents to the Model Response.
Our method enables us to extract all demographic vari-
ables for the model using a single distance value. This is
in contrast to previous methods (Santurkar et al. 2023; Dur-
mus et al. 2023) which involved the computation of a close-
ness metric for each individual demographic variable. How-
ever, such an approach risks over-representation, and does
not consider the interconnected nature of the demographic
variables. The proposed metric allows the model’s response
to be appropriately placed within clusters defined by the dif-
ferent demographic variables, which in turn constitutes the
model’s profile. We summarize our method in Figure 3.
We note that our approach would result in the model pro-
files reflecting sampling biases present among the survey re-
spondents. As such, the model profiles may not be extended
beyond the scope of the surveys used to create them.
Steering
Steering refers to the various methods used to make LLMs
respond more similarly to any specific group, which we shall
henceforth refer to as the steering group. Some methods doc-
umented in previous works include fine-tuning (Jiang et al.
2022) and more generic data-driven LLM augmentation (Li
et al. 2024) which use data from a cohort of individuals man-
ifesting similar views across specific inquiries, to steer to-
wards the steering group.
We limit our discussion to the effectiveness of zero-shot
steering capabilities of LLMs, in the absence of any addi-
tional training or augmenting methods. In such a setting, in-
structions to steer the model towards a particular steering
group are provided within the prompt itself. We opt for the
following methods to steer the model:
1. Through a multiple-choice question, whose answer is
also provided in the prompt.
2. Through a description of the steering group to portray.
3. Through an explicit instruction to answer the question as
though it belonged to a particular demographic group.

--- Page 6 ---

Model
Configuration
Short-hand
Llama 3.2
3B
L3B
3B Instruct
L3BIt
Llama 3.1
8B
L8B
8B Instruct
L8BIt
Mistral
7B v0.1
M7Bv1
7B v0.1 Instruct
M7Bv1It
7B v0.3
M7Bv3
7B v0.3 Instruct
M7Bv3It
Gemma 2
9B
G9B
9B Instruct
G9BIt
Table 2: Different Open LLMs used in our study, the config-
uration used per model (Number of Parameters), and short-
hand used to refer to the model in the model profile chart
(Figure 5).
The exact prompts used in our study have been provided
in Figure 4. Steering prompts are prepended to each question
prompt before running inferences on the model. We exam-
ine the effectiveness of steering a LLM towards different re-
ligions, using responses from the Indian Survey dataset. We
examine the average Hamming Distance between the model
response without any steering, and respondent belonging to
each religion. We then compute the same values after steer-
ing the model.
Models Used in the Study
We list the models evaluated in Table 2. Our study examines
the profiles of major modern open LLMs. All models are run
on an Apple Macbook Pro, using the M4 chip and the MPS
backend provided by the HuggingFace library4. As our ap-
proach only accesses the logits of the model to extract the
most probable token, we are not required to modify any hy-
perparameters generally associated with the text generation
process. However, to ensure reproducibility of results, we
initialize our model runs by setting all random seeds before
any inferences.
Results
We examine the closest respondents to the Model Response
to extract a profile for the model. For our study we define the
model’s profile as a collection of the modal demographic at-
tributes among these respondents. In the case of the India
survey, this is done by considering the top 1000 closest re-
spondents, due to the significantly larger number of survey
respondents. For each country in the EA and SEA survey,
we instead consider the top 100 closest respondents.
India
We find that most selected LLMs result in a single, homoge-
nized profile, with exceptions to this statement usually only
differing by at most two different demographic variables.
Figure 5 further indicates the uniformity of responses across
different models. We continue to observe this trend even in
the EA and SEA surveys.
4https://huggingface.co/docs/diffusers/en/optimization/mps
With regards to the Indian survey dataset, we report the
following profile: models indicate strong correspondence
with respondents aged 35-44 years who are either married
or living with a partner. We note significant alignment with
Hindu male respondents from the General caste. Among the
top 1,000 respondents, the majority report monthly house-
hold incomes above Rs. 10,000 (INR), with predominantly
a high-school level of education.
Geographically, the models align with respondents from
rural settlements in northern India. However, exceptions in-
clude Llama 3.1 Instruct and Gemma 2 Instruct, which show
stronger alignment to respondents from western India. Ad-
ditionally, Llama 3.1 Instruct exhibits a distinctive pattern
in educational alignment, corresponding more closely with
respondents holding primary education certificates, contrast-
ing other models in the analysis. We provide the model pro-
files in detail in Figure 5.
East Asia
For the subsequent surveys, we extract the model’s profile
from the top 100 closest respondents to the Model Response.
This is carried out for each territory to provide individual
profiles of the model. We observe that across most terri-
tories, with the exception of Vietnam, models are closely
aligned with Married, Male individuals having 2 children.
In the case of Vietnam, however, we only observe a vari-
ation in the Gender demographic, with closer alignment to
Women respondents. Detailed profiles for each country have
been provided in the GitHub repository.5
Japan
The model profiles are closely aligned with Mar-
ried, Male respondents, aged 45-59 years old. We observe
more closer alignment to more educated individuals, here
most models reflect the opinions of University-educated re-
spondents. Models are aligned to be of predominantly Bud-
dhist disposition.
Hong Kong
Model Profiles exhibit a notable alignment
with individuals following Buddhism, predominantly from
the Eastern Region of Hong Kong. The profiles also clearly
tend towards individuals who have achieved at least upper
secondary education with exceptions of Llama 3.2 3B In-
struct and Llama 3.1 8B which reflect an undergraduate ed-
ucation level.
South Korea
Model Profiles reveal distinct characteris-
tics when compared to the general survey public. A notable
alignment is observed between the models and individuals
who identify as Buddhist, contrasting sharply with the ma-
jority of the public, who reported having no religious affili-
ation. Moreover, The models predominantly mimic individ-
uals older than 60 years of age, who are residing in Seoul
or Gyeonggi-do, regions that represent significant urban and
cultural hubs in South Korea.
Taiwan
Models are largely aligned with individuals of
Buddhist faith, aged between 45 and 59 years, living in
New Taipei City. This geographic concentration suggests
5https://github.com/HariShankar08/LLMOpinions

--- Page 7 ---

Figure 5: Model Profiles - India. Comparing Model Responses with top 1,000 closest Survey Respondents. LLMs primarily
converge on a single demographic profile (e.g., married Hindu males, 35-44, rural Northern India, low income, high school),
with minor regional or educational variations in some models.
that the model captures patterns characteristic of urban re-
gions. The educational background shows a strong align-
ment with Bachelor’s degree holders, while gender distri-
bution remains balanced between males and females. These
individuals are typically married with no children.
Vietnam
Models are largely aligned with individuals of
Buddhist faith, aged between 35 and 44 years, living in the
Northern Central Area or Central Coastal Areas, having a
Bachelors degree. Profiles observed in Vietnam also show
a higher alignment to women, in contrast to our findings in
other territories within the EA survey, however, this is due
to the larger number of women respondents as compared to
men in the survey public.
South East Asia
Similar to the EA Survey, we refer to the top 100 respon-
dents to extract demographics of the model. We observe that
across most territories, models are closely aligned with Mar-
ried, Male individuals.
Indonesia
Models are closely aligned with respondents
of an age group of 35-44 years old. We observe maximum
alignment to individuals of a high-school level of education.
Models are closely aligned to Islamic practices. There is no
significant variation across different model families. We ob-
serve a more equitable distribution, as compared to findings
from the Indian survey, with respect to Urbanicity.
Most of the closest respondents, across all models, be-
long to the Java region of Indonesia. The concentration of
respondents from this region suggests the predominance of
publicly available online data originating from this region,
potentially leading to regional bias in the dataset.
Malaysia
Most models exhibit strong alignment with in-
dividuals from Malaysia who are male, married, and have
an educational qualification of Upper Secondary School or
higher. This trend suggests that the models are tuned to re-
flect the perspectives of individuals with a moderate to high
level of formal education. The models demonstrate a no-
table affinity toward individuals practicing Islam. This reli-
gious alignment suggests that the data used for model train-
ing likely emphasizes cultural or societal norms prevalent
within Islamic communities.
Cambodia
The Model closely aligns with individuals
practicing Buddhism primarily from Rural regions. Inter-
estingly, it reflects a demographic with incomplete Primary

--- Page 8 ---

Figure 6: Radar Plot for steering Llama 3.2 3B (L3B): Ra-
dius represents average Hamming Distance to different re-
ligions. We note no significant variation between the plot
without steering, and plots with steering towards religions.
Schooling, finished up to Grade 5, indicating a focus on indi-
viduals with lower levels of formal education. Unlike other
profiles, this model does not exhibit consistent patterns in
terms of age or specific regions within the country.
Singapore
The models provide a response closest to indi-
viduals having a Bachelor’s Degree, closely aligned to the
Buddhist faith, then followed by Hinduism. We note that
Singapore, being a more developed nation than its counter-
parts in the SEA survey, does not consider the urbanicity
variable, with all respondents live in Urban regions.
Sri Lanka
The model exhibits a strong alignment with
married individuals who follow Buddhism, reside in rural
regions, and have completed their education up to the senior
secondary level. This alignment underscores the model’s in-
clination toward a specific demographic that combines reli-
gious, marital, and educational attributes, with a pronounced
focus on rural populations. The model does not show a dis-
tinct preference or uniformity concerning gender or specific
regions within the country.
Thailand
We observe an equitable distribution of Urban-
icity across models. The models align closely with individ-
uals aged 45-59 years, with an education level of upper sec-
ondary schooling. Some outliers include L8BIt and G9BIt
which are more closely aligned towards individuals of a pri-
mary schooling level.
Examining Steering
We use the Llama 3.2 models in our subsequent experi-
ments. Steering is done on the basis of religion. We use the
Indian survey, and first generate the model response from the
survey questions. As discussed previously, we use the Par-
rot paraphrasing model to generate multiple versions of the
same question, as a precaution for prompt sensitivity. Sim-
ilarly, in our steering experiments, we use three copies of
each question prompt, including paraphrased versions, each
of which uses a different steering prompt. The final answer
Figure 7: Radar Plot for steering Llama 3.2 3B Instruct
(L3BIt): Radius represents average Hamming Distance to
different religions. We note the same pattern as in steering
L3B, indicating no additional benefit in selecting the instruc-
tion tuned variant for steering.
of each question is obtained through the model answer from
all candidate answers from each prompt used.
We then calculate the Hamming distance between the
Model Response and each survey respondent. Aggregating
the survey respondents by the different religions, we exam-
ine the average Hamming distance between the Response
and each religion. This experimental setup is first carried out
in the absence of steering, and then repeated with steering to-
wards each religion. We plot our findings for L3B and L3BIt
in Figures 6 and 7 respectively.
We note that on average, the model does not change sig-
nificantly with respect to the steering religions, even after
providing additional context. On examining generated texts
from these prompts, which detailed the model’s reasoning
for picking any particular option, we note that the model
emulates the steering group through language usage; utiliz-
ing Arabic salutations and honorific terms while portraying a
Muslim respondent, etc. However, we find that the opinions,
by and large, have not changed significantly. We observe this
both in the case of L3B and L3BIt, indicating that additional
Instruction tuning does not aid in making the LLM more
steerable.
Discussion
We note that the LLMs provide opinions on religious iden-
tity that are largely appropriate in the different nations and
territories used in the study. The opinions reflect respondents
corresponding to the different demographics as determined
in the model profile. We observe minimal variation from this
profile across the different families of LLMs used as a part
of our study.
We have, in this work, presented a novel approach to de-
termine the social alignment of LLMs and applied the same
to public surveys in India and other non-Western countries.
Our work also examines the effectiveness of steering by the
means of additional context in a prompt, and finds no sig-
nificant improvement with respect to reflecting opinions of

--- Page 9 ---

actual members of the particular steering group. The orga-
nizing agency, Pew Research Center, bears no responsibility
in the analyses or interpretations of the data presented in this
work.
Data: An Echo Chamber
Data is the food for models which drive decision making in
diverse domains. The quality of an LLM directly depends on
the data used to train it. The most common ways to currently
collect data include surveys and online data due to their scal-
ability and efficiency but these approaches are not perfect
and are plagued by significant limitations, such as under-
representation of certain groups and disloyal responses. This
leads to models which do not represent a diverse set of soci-
eties rather a privileged part of society who have the access
(Pew Research Center 2015).
Social Desirability Bias
Survey questions asking about taboo topics such as sexual
activities, illegal behaviour such as social fraud, or unsocial
attitudes such as racism, often generate inaccurate survey es-
timates which are distorted by social desirability bias. Due to
self-presentation concerns, survey respondents under-report
socially undesirable activities and over-report socially de-
sirable ones (Krumpal 2013). In India, for example, re-
spondents might deny a preference for male children, even
though cultural practices indicate otherwise. This discrep-
ancy distorts the training data for LLMs, making them less
representative of societal truths.
Variation through Instruction Tuning
We note that Instruction tuning does not significantly change
the profile of the model itself. This contrasts to what had
been observed in previous works (Santurkar et al. 2023) -
where additional tuning had resulted in the shift from indi-
viduals who were moderate/conservative with low income to
those who were liberal and high income. In the cited work,
this had been done through RLHF methods (Stiennon et al.
2020), which had resulted in the model being more suscep-
tible of the human opinions involved in the training. Instruc-
tion tuning (Wei et al. 2021) in contrast, does not involve
any human feedback, and optimizes the imitation of a defi-
nite, usually human-written response, which does not result
in such a divergence.
Amplifying Bias
Our findings indicate that most LLMs tend to represent spe-
cific demographics, a consequence of training on datasets
that are often derived from one another. This phenomenon
suggests that raw, real-world data is inherently incomplete
and lacks sufficient diversity (Rodriguez and Howe 2019).
The combination of the models’ homogeneous profiles, as
well as the ineffectiveness of zero-shot steering amplifies
the risk of bias towards these demographics, as AI generated
content continues to enter spaces of the Internet. To address
this issue, potential solutions include augmenting datasets
with synthetic data to introduce greater diversity or employ-
ing machine unlearning techniques to mitigate biases inher-
ited from training data. These approaches could help reduce
demographic skew and improve the fairness and accuracy of
AI-generated survey responses.
Shortcomings of Model Profiles
The model profiles provided must be interpreted with several
important caveats: (1) We only use the profiles to indicate
the similarities between different LLMs. (2) The profiles in-
herently reflect sampling biases among survey respondents.
Profiles cannot be generalized beyond the respective surveys
that were used to create them. The model profiles must not
be misused for stereotyping or discrimination against any
particular group of society.
In addition to this, we also face the issue of Alignment
Faking; like humans who fake their opinions when put
through surveys due to social bias and stigma, LLMs can
also fake their alignments (Hubinger 2024). This is done by
selectively following training objectives and guidelines dur-
ing supervised sessions, while reverting to undesirable and
biased behaviour in cases when the model knows it is not
being monitored. This phenomenon highlights the true chal-
lenge of alignment, which is the genuine adoption of diver-
sity of opinions rather than just optimizing for surface-level
compliance.
Limitations and Future Work
The method described in the paper uses all questions pro-
vided in the survey, with minimal manual inputs, in deter-
mining the Demographic Questions. However, such an ap-
proach underscores an assumption that all questions in the
survey have equal relevance in determining the model’s pro-
file. A more thorough analysis with respect to the correla-
tions between different questions may help in more effec-
tively determine a model’s profile; however, this approach
may not be as easily generalizable for surveys across differ-
ent domains.
We may observe different model profiles when the model
is prompted in the different languages used while conducting
the survey. This is due to the fact that each corpus used to
train LLMs in the target languages may propagate its own
biases which are distinct from corpora in other languages
such as English.
We may also examine the correlation between gener-
ated opinions and content on the Internet from different re-
gions, countries and territories, which constitutes the train-
ing data of LLMs. For example, we may examine content on
Wikipedia or Reddit to determine correlations between the
text and opinions portrayed by the LLM.
Future works may also choose to examine the effects of
features such as continuous access to Internet data beyond
the model’s training cutoff date, which are typical of more
recent proprietary AI systems. We may also use our method-
ology to evaluate the effectiveness of other steering methods,
such as fine-tuning and data augmentation.
References
Anagnostidis, S.; and Bulian, J. 2024.
How Suscepti-
ble are LLMs to Influence in Prompts?
arXiv preprint
arXiv:2408.11865.

--- Page 10 ---

Chrostowski, M.; and Najda, A. J. 2024. ChatGPT as a mod-
ern tool for Bible teaching in confessional religious educa-
tion: a German view. Journal of Religious Education, 1–20.
Damodaran, P. 2021.
Parrot: Paraphrase generation for
NLU.
Durmus, E.; Nyugen, K.; Liao, T. I.; Schiefer, N.; Askell,
A.; Bakhtin, A.; Chen, C.; Hatfield-Dodds, Z.; Hernandez,
D.; Joseph, N.; et al. 2023. Towards measuring the repre-
sentation of subjective global opinions in language models.
arXiv preprint arXiv:2306.16388.
Evans, J. 2024a. East Asian Societies Survey Dataset.
Evans, J. 2024b. South and Southeast Asia Survey Dataset.
Hamdelsayed, M.; and Atwell, E. 2016. Islamic applications
of automatic question-answering. Journal of Engineering
and Computer Science, 17(2): 51–57.
Hamming, R. W. 1950. Error detecting and error correcting
codes. The Bell system technical journal, 29(2): 147–160.
Hendrycks, D.; Burns, C.; Basart, S.; Zou, A.; Mazeika, M.;
Song, D.; and Steinhardt, J. 2021. Measuring Massive Mul-
titask Language Understanding. Proceedings of the Interna-
tional Conference on Learning Representations (ICLR).
Hou, H.; Leach, K.; and Huang, Y. 2024. ChatGPT Giving
Relationship Advice – How Reliable Is It? Proceedings of
the International AAAI Conference on Web and Social Me-
dia, 18(1): 610–623.
Hubinger, E. 2024.
Alignment faking in large language
models. arXiv preprint arXiv:2412.14093.
Jiang, A. Q.; Sablayrolles, A.; Mensch, A.; Bamford, C.;
Chaplot, D. S.; Casas, D. d. l.; Bressand, F.; Lengyel, G.;
Lample, G.; Saulnier, L.; et al. 2023. Mistral 7B. arXiv
preprint arXiv:2310.06825.
Jiang, H.; Beeferman, D.; Roy, B.; and Roy, D. 2022. Com-
munityLM: Probing Partisan Worldviews from Language
Models. arXiv:2209.07065.
Johnson, K. 2023.
AI, Faith, and Ethics.
https://
religiousfreedomandbusiness.org/ai-faith-ethics.
Krumpal, I. 2013. Determinants of social desirability bias in
sensitive surveys: A literature review. Quality & Quantity,
47(4): 2025–2047.
Li, J.; Mehrabi, N.; Peris, C.; Goyal, P.; Chang, K.-W.; Gal-
styan, A.; Zemel, R.; and Gupta, R. 2024. On the steerabil-
ity of large language models toward data-driven personas.
arXiv:2311.04978.
Maguire, E. 2017. How East and West think in profoundly
different ways. BBC Future. BBC Future Series.
Pew Research Center. 2015. Coverage error in Internet sur-
veys.
Pew Research Center. 2018. Eastern and Western Europeans
Differ on Importance of Religion, Views of Minorities and
Key Social Issues. Accessed: 2024-12-26.
Pew Research Center. 2021.
About Three-in-Ten U.S.
Adults Are Now Religiously Unaffiliated.
Pew Research Center. 2022. Key Findings From the Global
Religious Futures Project.
Pew Research Center. 2024. Many Around the Globe Say
It’s Important Their Leader Stands Up for People’s Reli-
gious Beliefs. Accessed: 2024-12-26.
Radford, A. 2018. Improving language understanding by
generative pre-training.
Rodriguez, L.; and Howe, B. 2019. In defense of synthetic
data. arXiv preprint arXiv:1905.01351.
Sahgal, N.; and Evans, J. 2021. India Survey Dataset.
Santurkar, S.; Durmus, E.; Ladhak, F.; Lee, C.; Liang, P.; and
Hashimoto, T. 2023. Whose opinions do language models
reflect? In International Conference on Machine Learning,
29971–30004. PMLR.
Stade, E. C.; Stirman, S. W.; Ungar, L. H.; Boland, C. L.;
Schwartz, H. A.; Yaden, D. B.; Sedoc, J.; DeRubeis, R. J.;
Willer, R.; and Eichstaedt, J. C. 2024.
Large language
models could change the future of behavioral healthcare: a
proposal for responsible development and evaluation. NPJ
Mental Health Research, 3(1): 12.
Stiennon, N.; Ouyang, L.; Wu, J.; Ziegler, D.; Lowe, R.;
Voss, C.; Radford, A.; Amodei, D.; and Christiano, P. F.
2020.
Learning to summarize with human feedback.
Advances in Neural Information Processing Systems, 33:
3008–3021.
Storm, I.; and Wilson, J. 2024. Religion and Social Impact:
A Cross-Cultural Analysis.
Journal of Religious Studies,
15(1): 143–161.
Thoriquttyas, T.; Muyassaroh, N.; Ahsin, N.; and Naim, A.
2021. Religious discourse, cyberspace and social media: A
trajectory from Muslim millennial’s perspective. In Commu-
nity Empowerment through Research, Innovation and Open
Access, 109–113. Routledge.
Touvron, H.; et al. 2023. LLaMA: Open and Efficient Foun-
dation Language Models. arXiv preprint arXiv:2302.13971.
UNESCO United Nations Educational, Scientific and Cul-
tural Organization. 2003.
International standard classifi-
cation of education, ISCED 1997. In Advances in Cross-
National Comparison: A European Working Book for Demo-
graphic and Socio-Economic Variables, 195–220. Springer.
Venkit, P. N. 2024.
Do Generative AI Models Output
Harm while Representing Non-Western Cultures: Evidence
from A Community-Centered Approach.
arXiv preprint
arXiv:2407.14779.
Watkins, D. 2020. Pope’s special Urbi et Orbi blessing: ‘God
turns everything to our good’. Vatican News.
Wei, J.; Bosma, M.; Zhao, V. Y.; Guu, K.; Yu, A. W.; Lester,
B.; Du, N.; Dai, A. M.; and Le, Q. V. 2021.
Finetuned
language models are zero-shot learners.
arXiv preprint
arXiv:2109.01652.
World Bank. 2024. East Asia and Pacific Overview. https:
//www.worldbank.org/en/region/eap/overview.

```
