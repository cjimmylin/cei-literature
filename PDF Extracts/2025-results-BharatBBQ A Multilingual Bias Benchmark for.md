---
title: "2025-results-BharatBBQ A Multilingual Bias Benchmark for - PDF Extract"
source_pdf: "2025-results-BharatBBQ A Multilingual Bias Benchmark for.pdf"
pages: 20
extracted_at: "2026-02-13T09:15:45.345939"
---

# PDF Extract: 2025-results-BharatBBQ A Multilingual Bias Benchmark for

**Source PDF:** 2025-results-BharatBBQ A Multilingual Bias Benchmark for.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

BharatBBQ: A Multilingual Bias Benchmark for Question Answering in
the Indian Context
Warning: Some examples may contain offensive or sensitive content.
Aditya Tomar∗
IIT Bombay
adityatomar@cse.iitb.ac.in
Nihar Ranjan Sahoo∗
IIT Bombay
nihar@cse.iitb.ac.in
Pushpak Bhattacharyya
IIT Bombay
pb@cse.iitb.ac.in
Abstract
Evaluating social biases in language mod-
els (LMs) is crucial for ensuring fairness
and minimizing the reinforcement of harm-
ful stereotypes in AI systems.
Existing
benchmarks, such as the Bias Benchmark
for Question Answering (BBQ), primarily
focus on Western contexts, limiting their ap-
plicability to the Indian context.
To ad-
dress this gap, we introduce BharatBBQ
1, a culturally adapted benchmark designed
to assess biases in Hindi, English, Marathi,
Bengali, Tamil, Telugu, Odia, and As-
samese. BharatBBQ covers 13 social cat-
egories, including 3 intersectional groups,
reflecting prevalent biases in the Indian so-
ciocultural landscape. Our dataset contains
49,108 examples in one language that are
expanded using translation and verification
to 392,864 examples in eight different lan-
guages. We evaluate five multilingual LM
families across zero- and few-shot settings,
analyzing their bias and stereotypical bias
scores. Our findings highlight persistent bi-
ases across languages and social categories
and often amplified biases in Indian lan-
guages compared to English, demonstrating
the necessity of linguistically and culturally
grounded benchmarks for bias evaluation.
1
Introduction
Language Models (LLMs) have revolutionized
natural language processing, demonstrating re-
markable capabilities across various tasks. Mak-
ing such LLMs accessible to everyone depends on
their ability to serve different social groups fairly.
However, these LLMs often inherit and propa-
gate social biases present in their training data
(Das et al., 2024; Sheng et al., 2019), leading to
stereotypical, unfair, and potentially harmful out-
puts, more so for multilingual societies like India.
∗Equal Contribution
1Dataset and Code
While existing bias benchmarking datasets, such
as BBQ (Parrish et al., 2022), provide a framework
for evaluating biases within Western contexts, they
fall short of addressing the unique socio-cultural
complexities of non-Western societies.
Motivation: In India, a country with 22 official
languages (Gala et al., 2023) and complex social
structures, LLMs can reinforce historical inequal-
ities if they do not consider local contexts prop-
erly. For example, these models might wrongly
link the Dalit caste with low-status jobs (Rawat,
2013), label people from Northeastern states as
"foreign", or assume that leaders in organizations
must be men. These mistakes happen not only be-
cause of missing data but also due to the lack of
culturally aware tools to identify and fix such bi-
ases. Moreover, as each language carries its own
idioms, honorifics, and sociocultural jargon, build-
ing a bias benchmark demands more than just a di-
rect translation from English. For instance, Hindi
uses kinship terms like "Bhaiya" (brother), which
carries different social connotations than "Anna"
(brother) in Telugu, despite both being used as
forms of address for men.
To reduce this gap, we introduce BharatBBQ,
the first large-scale, multilingual benchmarking
dataset designed to systematically evaluate social
biases in LLMs across India’s diverse linguistic
and socio-cultural landscape.
Our contributions are,
1. BharatBBQ, a multilingual benchmark de-
signed to measure social biases in LLMs within
Indian context. It adopts a question-answering
framework to probe model biases (§3).
(a) Bias Dimensions: The benchmark covers
13 identity dimensions, including Gender
Identity, Age, Religion, Disability Status,
Caste, Region, Sexual Orientation, Socio-
economic Status, Physical Appearance,
Nationality, along with intersectional axes
such as Religion×Gender, Age×Gender,
arXiv:2508.07090v1  [cs.CL]  9 Aug 2025

--- Page 2 ---

Figure 1: Examples in BharatBBQ feature ambiguous contexts with "Unknown" as the ground truth and
disambiguated contexts with ground truths from the extended context. In this example, the ground truths
are "Pakistani" for the negative question and "Indian" for the non-negative question (§ 3). Each example
in BharatBBQ is available in English and seven Indian languages to evaluate biases in multilingual LLMs.
and Region×Gender (§ 3.3).
(b) Multilingual Extension: Through trans-
lation and verification,
BharatBBQ is
available in eight languages, such as En-
glish, Hindi, Marathi, Telugu, Tamil, Ben-
gali, Odia, and Assamese, with over 49K
examples per language, totaling more than
392K instances (§ 3.4).
2. A comprehensive evaluation of five open-
source multilingual decoder-based LLM fam-
ilies using our curated dataset, revealing that
models exhibit significantly more bias in Indian
languages compared to English (§6).
2
Related Work
Social bias can be defined as discrimination for, or
against, a person or group, or a set of ideas or be-
liefs, in a way that is prejudicial or unfair (Webster
et al., 2022). The presence of biases in LLMs has
sparked the research focus for the detection and
mitigation of various biases from LLMs (Hovy
and Prabhumoye, 2021).
Studies have shown
that popular models like BERT and GPT-2 exhibit
strong stereotypical tendencies (Jentzsch and Tu-
ran, 2022; Liu et al., 2021).
To quantify biases in LMs, several benchmarking
datasets, such as StereoSet (Nadeem et al., 2021),
Crows-Pairs (Nangia et al., 2020) have been pro-
posed. These benchmarks have established frame-
works to quantify biases in LMs, often relying on
metrics derived from likelihood scores. However,
they predominantly focus on a few social bias cat-
egories important to Western cultures and over-
look region-specific biases prevalent in linguisti-
cally diverse regions like India.
Beyond likeli-
hood scores, other bias benchmarks perform eval-
uation through tasks like natural language infer-
ence (Anantaprayoon et al., 2024), coreference
resolution (Zhao et al., 2018), or machine transla-
tion tasks (Stanovsky et al., 2019). A more recent
trend explores measuring biases through question
answering (QA), notably the datasets like BBQ
(Parrish et al., 2022) and its multilingual vari-
ants, such as MBBQ (Neplenbroek et al., 2024),
KoBBQ (Jin et al., 2024), and CBBQ (Huang and
Xiong, 2024).
In India, biases appear in unique ways, such as
through caste, region, and overlapping identities
(Thorat et al., 2020). Some efforts, like IndiB-
ias (Sahoo et al., 2024), try to address this issue
but have limitations. They only cover Hindi and
English and do not fully analyze multiple over-
lapping biases, and they mainly focus on sim-
ple sentence pairs and do not utilize QA-style se-
tups that better reflect practical, user-facing in-
teractions. As discussed by Singh et al. (2022),
stereotypes become biases when expressed in an
opinionated manner. Building on this insight, our
work presents opinionated templates in a QA for-
mat to surface underlying stereotypes, and we use
the terms “bias” and “stereotype” interchangeably.
To address these limitations, our work introduces
a new QA-based benchmark that targets social bi-
ases specific to the Indian context. Our bench-
mark covers underrepresented dimensions such as
caste and regional identity and contains context-
rich QA templates, with an aim to better capture
how stereotypes may surface in language models
when responding to socially sensitive inputs con-
textualized for India.

--- Page 3 ---

3
Dataset
The structure of BharatBBQ follows a similar for-
mat to the original BBQ dataset, designed to evalu-
ate biases through QA scenarios, as shown in Fig-
ure 1. Each instance in BharatBBQ has a context,
a question, and three answer options. The answer
options are stereotyped group, non-stereotyped
group, and the unknown option.
For example,
for the instance in Figure 1, these three options
are "Pakistani", "Indian", and "Unknown", respec-
tively. Each instance is crafted to test the presence
of social biases in LLMs by presenting:
Contexts: There are two types of contexts,
Ambiguous Context: This context is intentionally
under-informative, leading to situations where the
model may rely on stereotypes to answer the ques-
tion. In these cases, the correct answer is "Un-
known", irrespective of the question type, because
the context does not provide enough information
to determine a fact-based answer.
Disambiguated Context: This is an extended con-
text, when concatenated with ambiguous context,
provides sufficient details to correctly answer the
question without ambiguity. It removes the pos-
sibility of relying on stereotypes, allowing the
model to make an informed decision.
Question Types: Each context is paired with
two types of questions- a negative question and a
non-negative question. The negative question asks
which group aligns with a given stereotype, while
the non-negative question asks which group de-
fies it. For example, if the stereotype is “Asians
are good at math,” the negative question would
ask, “Who is good at math?” expecting the stereo-
typed answer. Conversely, the non-negative ques-
tion might ask, “Who struggles with math?”.
Instance Pairing: Instance pairing applies
only to disambiguated contexts and captures how
the ground truth aligns with or opposes the stereo-
type. If the stereotyped group is explicitly associ-
ated with the stereotype in the context, we call this
a Negative Pairing (NP); here, the correct answer
to the negative question is the stereotyped group.
Conversely, if the context assigns the stereotype
to the non-stereotyped group, it is termed Non-
Negative Pairing (NNP), where the correct an-
swer to the negative question becomes the non-
stereotyped group. For example, if the stereotype
is “Asians are good at math,” then in an NP sce-
nario, the context states that an Asian individual
excels at math, making “Asian” the correct answer
to the negative question “Who is good at math?”
In an NNP scenario, the context instead specifies
that a non-Asian individual excels at math, mak-
ing the non-stereotyped group the correct answer
to the same question.
Figure 2: Expected Answer to different conditions
in BharatBBQ.
Figure 2 illustrates the expected answers based
on question type and context.
In the ambigu-
ous context, where no specific group is indi-
cated, both negative and non-negative questions
should be answered as “Unknown.” In the dis-
ambiguated context, the expected responses vary:
in the NP scenario, the negative question is an-
swered with the stereotyped group, while the
non-negative question is assigned to the non-
stereotyped group. Conversely, in the NNP sce-
nario, the non-negative question is answered with
the stereotyped group, and the negative question
with the non-stereotyped group.
3.1
Templates Creation
To create BharatBBQ, we culturally adapted the
BBQ to the Indian context. Our approach ensures
that the dataset is relevant and sensitive to the so-
cial dynamics and stereotypes prevalent in India.
We utilized four transformation strategies to con-
struct the benchmark (Figure 3):
Sample Removed: We manually verified each
template in BBQ and excluded templates that are
not applicable in the Indian socio-cultural con-
text.
For instance, stereotypes related to Jew-
ish communities, such as being labeled as greedy,
were removed since these biases (antisemitism)
have a negligible footprint in the Indian context
(CSPS, 2023; Business Standard, 2023).
Addi-
tionally, categories related to race (black commu-
nity vs. white community) and intersectional bi-
ases involving race were omitted, as racial dynam-
ics in India differ from those in the U.S (Baber,

--- Page 4 ---

Figure 3: Constructional adaptations in BharatBBQ. Strikethrough denotes elements removed due to
cultural mismatch, while underlining indicates culturally adapted translations. Light green rows show
BharatBBQ instances, light red rows show original BBQ counterparts, and the dotted box highlights
stereotypical target groups.
2022a; Dey, 2021).
Culturally Transformed:
In this cate-
gory, we replaced entities that were specific to
U.S. culture with their viable Indian counterparts.
For example, the American retail chain Shop N
Stop was replaced with Big Bazaar, a well-known
Indian supermarket chain, to ensure familiarity
and contextual relevance for Indian users.
Target Group Modified: We adapted tar-
get groups to reflect Indian stereotypes that dif-
fer from U.S. contexts.
For example, in the
U.S., stereotypes associating terrorism with cer-
tain countries like Saudi Arabia are prevalent;
however, in India, these associations do not exist
in the same way. Conversely, Pakistan is often a
target of stereotypes related to terrorism in India
but was absent in BBQ. We included such cultur-
ally relevant target groups to provide a more accu-
rate assessment of biases in Indian languages.
Newly Created:
Beyond adapting existing
templates, we also created new templates (detailed
in Section 3.1) in the existing categories, includ-
ing Nationality, Religion, and Gender Identity.
Furthermore, we introduced entirely new cate-
gories unique to the Indian context, such as Caste,
Region, Region×Gender, Religion×Gender, and
Age×Gender, which capture complex intersec-
tional biases prevalent in Indian society. In partic-
ular, we highlight how caste and regional identity
can function as proxies for race in India (Baber,
2022b), offering a distinct lens on societal strati-
fication compared to Western contexts where race
is often framed in terms of Black–White dynam-
ics. Through intersectionality of Region and Gen-
der, we capture stereotypes such as Northeastern
women are exoticized or labelled as “outsiders,”
North Indian men are caricatured as loud or ag-
gressive, Tamil women are portrayed as overly tra-
ditional, etc. Religion×Gender includes stereo-
types such as Muslim women being veiled and
submissive (Pandey, 2024), Sikh women assumed
to be conservative due to visible religious markers,
Hindu women portrayed as passionate devotees,
etc.
Finally, Age×Gender captures age-related
gendered stereotypes, including teenage girls por-
trayed as carefree consumers, middle-aged men as
dominant breadwinners, older men as authoritative
patriarchs, etc. These newly created templates aim
to faithfully represent the multifaceted nature of
social bias in the Indian context.
These adaptations ensure that BharatBBQ effec-
tively captures social biases relevant to the Indian
context, enabling a more comprehensive evalua-
tion of multilingual language models. As shown

--- Page 5 ---

# of Templates
# of
Templates
# of
Examples
# of Examples
with PN
Category
SR
TM/CT
ST
NC
Age
0
3
22
0
25
6,656
0
Disability Status
0
4
21
0
25
5,296
0
Gender Identity
0
0
25
3
28
6,536
4176
Sexual Orientation
5
8
12
1
21
904
0
Socio-Economic
1
1
23
1
25
2,336
0
Physical Appearance
0
2
23
3
28
5,980
0
Religion
8
2
15
11
28
4,800
3888
Nationality
2
0
23
11
34
3264
0
Caste
0
0
0
25
25
3,864
2296
Region
0
0
0
41
41
3,144
0
Religion×Gender
0
0
0
12
12
1,504
1240
Region×Gender
0
0
0
11
11
1,944
0
Age×Gender
0
0
0
20
20
2,880
0
Total (1 Language)
16
20
164
139
323
49,108
11,600
Total (8 Languages)
-
-
-
-
-
3,92,864
92,800
Table 1: Statistics of BharatBBQ. SR, TM/CT,
ST, NC, PN denote SAMPLE REMOVED, TAR-
GET GROUP MODIFIED/CULTURALLY TRANS-
FORMED, SIMPLY TRANSFERRED, NEWLY CRE-
ATED, and PROPER NOUN, respectively.
The
number of examples means the number of unique
pairs of the context (ambiguous/disambiguated)
and question (negative/non-negative).
The last
column shows the number of examples for which
the stereotype/anti-stereotype group is represented
through proper nouns as discussed in Section 3.2.
in Table 1, for many categories that are both in
BBQ and BharatBBQ, we retained a considerable
number of original BBQ templates without mod-
ification, as the underlying stereotypes were also
prevalent in the Indian context.
3.2
Proper Nouns
In certain categories, such as Religion, Caste,
Gender Identity, and Gender×Religion, we have
incorporated proper nouns, as surnames in In-
dia often indicate caste, while first names can
also reflect religion and gender.
For instance,
in the newly created example shown in Figure
3, the stereotype “People from the Baniya caste
are business-minded” is illustrated using surnames
like Goyal and Agarwal, which are commonly as-
sociated with the Baniya community. Addition-
ally, beyond using proper names, we have also
generated examples from the same template by in-
corporating common nouns, such as referring to
the group explicitly as "Baniya" instead of using
names with surnames.
3.3
Dataset Statistics
The overall statistics of the dataset, such as the
number of templates, number of examples, num-
ber of templates updated from BBQ, and number
of newly created templates, are presented in Table
1. All the statistics are exactly the same for all 8
languages that are part of BharatBBQ.
Also, in Table 2 we show the difference in the
number of instances in our dataset and the original
BBQ across categories that are in both datasets.
Barring the socio-economic category, BharatBBQ
contains more examples in each shared category.
Categories such as Age, Disability Status, and
Physical Appearance have more number of in-
stances, despite the number of underlying tem-
plates remaining comparable to BBQ. This is due
to three main reasons: (i) unlike BBQ, we sys-
tematically present both negative and non-negative
questions for both context types; (ii) we add more
culturally grounded possibilities for both stereo-
typed and non-stereotyped options; and (iii) more
lexical variations for the unknown options (Un-
known, Not enough information, Cannot be deter-
mined, Can’t answer, Can’t be determined, etc.) to
get rid of any lexical bias in LLMs’ response.
Dataset
Gender
Religion
Disability
SO
Age
PA
SE
Nationality
BBQ
5672
1200
1556
864
3680
1576
6864
3080
BharatBBQ
6536
4800
5296
904
6656
5980
2336
3264
Table 2: Comparison of the number of examples
by category in BBQ and BharatBBQ datasets. SO:
Sexual Orientation, PA: Physical appearance, SE:
Socio-economic.
3.4
Multilingual Extension
While certain stereotypes maintain consistency
across India,
many biased expressions (e.g.,
snooty tamil brahmins2) are deeply tied to specific
regional sociolinguistic contexts. This limitation
becomes especially problematic when evaluating
models intended to serve India’s culturally and lin-
guistically diverse population.
To address these challenges and create an accu-
rate representative benchmark for bias evaluation,
we have expanded BharatBBQ to support 7 In-
dian languages: Hindi, Marathi, Bengali, Telugu,
Tamil, Assamese, and Odia. The inclusion of these
languages ensures balanced geographical repre-
sentation across the Northern, Eastern, Western,
and Southern regions of India, capturing distinc-
tive cultural perspectives from each area.
We first generated examples in English using tem-
plates created for BharatBBQ, as discussed in
Section 3.1.
These examples were then trans-
lated into the target languages using IndicTransv2
(Gala et al., 2023), a state-of-the-art neural ma-
chine translation model specialized for Indian lan-
2https://bit.ly/3QFNeGB

--- Page 6 ---

guages. To ensure semantic consistency, we back-
translated the examples into English and measured
the cosine similarity between the original English
version and the back-translated English text us-
ing modernBERT (Warner et al., 2024) embed-
dings. We retained examples with a cosine sim-
ilarity score above 0.75 to ensure high seman-
tic alignment.
We decided on the threshold of
0.75 after manual verification for semantic sim-
ilarity between the original and back-translated
texts.
As detailed in Appendix A.1 and Table
3, two language-specific annotators for each lan-
guage assessed a sample of contexts and questions
for fluency and adequacy metrics.
Consistently
high scores for both metrics across all languages
confirm that our 0.75 threshold reliably preserves
the intended meaning of the original examples.
For examples with similarity scores below 0.75,
we conducted manual corrections (Section 3.8) to
preserve contextual integrity and cultural nuances.
These curated examples were then added to the
BharatBBQ dataset, facilitating robust multilin-
gual bias evaluation for Indian languages.
3.5
Stereotype Concept Collection
First, we collected various stereotypical concepts
from different parts of India.
To achieve this,
we released an open-ended Google form on vari-
ous academic and non-academic forums to capture
stereotypes about different social groups. This ap-
proach enabled us to collect emergent and subtle
themes of stereotypes from the 241 responses we
received across all regions of India.
The instruction protocol explicitly states: "De-
scribe social biases or stereotypes you have ob-
served in your community regarding how peo-
ple from (your own/other) demographics like gen-
der, religion, caste, nationality, sexual orienta-
tion, age, disablibity, sexual orientation, physi-
cal appearance, and socio-economic status are
perceived based on their upbringing, background
characteristics, and experineces.
There are no
right or wrong answers - we want to understand
ground realities. You are allowed to mention the
stereotypes using:
• Tuples with social group and stereotypical
concepts (e.g., <lower caste, poor>, <female,
emotional>, etc.)"
• Free-text entries about perceived stereotypes
(e.g., "Chinese products are of low quality",
"Old people have less cognitive ability")
This strategy of collecting stereotype concepts
through tuple or free-text reduces cognitive load
and cognitive bias (Gautam and Srinath, 2024) of
annotators observed in structured surveys. Also,
we do not force respondents to reveal their iden-
tity, which helps to get unfiltered, genuine per-
spectives about sensitive topics like caste discrim-
ination, religious beliefs, etc. From the pool of
stereotype concepts, we only use the ones that are
mentioned by at least three persons.
We also reviewed multiple studies on stereotypes
in the Indian context for various demographics.
For caste-related stereotypes, we referred to the
studies done by Sinha and Sinha (1967), Sankaran
et al. (2017). For other categories, we reviewed
relevant research articles, including SeeGull (Jha
et al., 2023), multilingual SeeGull (Bhutani et al.,
2024), Indian-BHED (Khandelwal et al., 2024),
and IndiBias (Sahoo et al., 2024). From SeeGull
and multilingual SeeGull, we utilized the stereo-
type tuples reported to have been agreed upon by
three annotators.
After the initial filtration, we manually vali-
dated the prevalence of each remaining stereotype
within the Indian context through a thorough on-
line search. We retained only those stereotypes
for which we could find relevant and trustworthy
news or research articles, adding these sources to
the dataset for reference.
In total, after valida-
tion across all sources, we collected 307 stereo-
type concepts spanning 13 categories.
We kept
those original BBQ templates whose underlying
stereotype was part of these 307 concepts.
3.6
New Template Creation
We manually created templates for each validated
stereotype. Each template follows a fixed structure
similar to BBQ: it presents a context and then asks
a question that may invoke the stereotype.
For example, for the stereotype "South Indians do
not prefer to speak in Hindi," a template could be:
Ambiguous Context: "[NAME1] from Tamil Nadu
and [NAME2] from Uttar Pradesh are were both
invited to give a speech during the opening cere-
mony of the exhibition."
Disambiguated Context:
"[NAME1] gave their
speech in Hindi while [NAME2] was not comfort-
able in giving speech in Hindi."
Negative Question: "Who is more likely to have
given a speech in Hindi?"
The templates use placeholders like [NAME1]
and [NAME2], which are later replaced with
proper nouns or common nouns that match the de-

--- Page 7 ---

mographic context as discussed in Section 3.2. For
some of the stereotypes, we created multiple ver-
sions of the template to test bias from different an-
gles. These variations keep the core stereotype but
change the scenario, wording, or details to ensure
a robust evaluation.
3.7
Template Validation
Two independent annotators, familiar with Indian
social structure, reviewed each newly created tem-
plate to ensure clarity and validity in capturing the
intended stereotype. They assessed each template
based on a) if the template correctly represents
the intended stereotype, b) if the negative ques-
tion is designed correctly to evoke the negative
stereotype and the non-negative question to probe
neutral or positive association, and c) if the place-
holder terms correctly represent the desired social
group.
The Cohen’s Kappa score (Cohen, 1960) between
the two annotators was 0.83 for the template val-
idation.
Templates were included in the final
dataset only if both annotators approved them on
all criteria. In case of disagreement, the authors
engaged in discussions to refine or discard the
template as needed.
3.8
Translation Annotation Task
We employ annotators to verify and correct the
translation when the cosine similarity after back-
translation is below 0.75. One annotator for each
of the seven Indian languages was employed for
the verification task. The annotators were asked
to verify if the back-translated text (both context
and question) is a correct semantic representation
of the original example. If discrepancies are iden-
tified, they refine the translation to better capture
the semantic nuances of the original example.
4
Metrics
In addition to accuracy, for robust and accurate
measurement of bias using the BBQ-style dataset,
we use two metrics: Bias Score (BS) and Stereo-
typical Bias Score (SBS).
Accuracy:
We report accuracy separately for
ambiguous and disambiguated contexts to reflect
model performance under uncertainty and when
contextual cues resolve ambiguity.
AccA =
#Unknown
#ambiguous examples
(1)
AccD = #Correct (NP) + #Correct (NNP)
#disambiguated examples
(2)
Here, AccA denotes the accuracy for ambiguous
contexts, which is measured by the proportion of
examples for which the model correctly responds
with the unknown option, as this is the ground-
truth answer for such cases, as shown in Fig. 2.
AccD refers to the accuracy for disambiguated
contexts, where context explicitly contains the cor-
rect answer. We compute it as the proportion of
correct responses across both NP and NNP set-
tings. As discussed in Section 3 and Figure 2:
• #Correct (NP): The number of correct predic-
tions for the negative pairings, i.e., stereotyped
and non-stereotyped groups, is the correct an-
swer to negative and non-negative questions, re-
spectively.
• #Correct (NNP): The number of correct pre-
dictions for the non-negative pairings, i.e., non-
stereotyped and stereotyped groups, is the cor-
rect answer to negative and non-negative ques-
tions, respectively.
A low accuracy score in either the ambiguous or
disambiguated context indicates bias in the model.
Bias Score: The bias score is defined differently
for ambiguous context and disambiguated context.
BSA =
#S −#NS
#ambiguous examples
(3)
BSD = #Correct (NP) −#Correct (NNP)
#Non-unknown
(4)
Here, the BSA and BSD refer to the bias score
for ambiguous contexts and disambiguated con-
texts, respectively. #S and #NS show the number
of times the LLM has selected the stereotyped or
non-stereotyped option, respectively, for ambigu-
ous context, either for negative or non-negative
questions.
A higher BSA score suggests that,
potentially, the model agrees with the underlying
stereotype when the context is uncertain.
#Non-unknown shows the number of times LLM
has chosen the non-unknown option in the dis-
ambiguated context. For disambiguated contexts,
we consider only instances where the response is
not classified as "unknown." Because if the LLM
selects the "unknown" option for disambiguation,
it reflects a limitation of the model in handling
question-answering (QA) tasks rather than an in-
herent ambiguity in the context itself. Since BSD
is computed only over non-unknown responses, a
higher value suggests that, even in NNP, the model

--- Page 8 ---

tends to select the biased option, thereby increas-
ing the difference. A higher BSD score suggests
that the model behaves discriminately to correctly
answer in the disambiguated context, revealing its
bias.
Stereotypical Bias score: We introduced this new
metric, which is also defined differently for both
the contexts.
SBSA and SBSD represent the
Stereotypical Bias Scores in ambiguous and dis-
ambiguated contexts, respectively.
SBSA = #Sneg + #NSnon−neg
#ambiguous examples
(5)
SBSD = #Sneg(NNP) + #NSnon−neg(NNP)
#NNP examples
(6)
In an ambiguous context, instead of the un-
known option, the LLM’s choice between the
stereotype (S) and non-stereotype (NS) options in
its answer directly reflects its bias. The bias score
measures overall preference for S versus NS, but
it does not distinguish why that preference occurs.
For instance, consider a gender stereotype that as-
sociates “men” with a negative trait. In an am-
biguous context, if the model answers the nega-
tive question with “the man” and the non-negative
question with “the woman,” this pattern strongly
suggests the model links negative events to the
stereotype (a stereotypical bias). However, if the
model answers “the man” to both the negative
and non-negative questions, that likely indicates a
generic preference for the word “man” (a lexical
bias), not a specific stereotype about negativity.
To address such scenarios, through SBS, we sep-
arately analyze the negative and the non-negative
questions. #Sneg refers to the number of times
the model selects the stereotyped group for the
negative question, while #NSnon−neg counts in-
stances where the non-stereotyped group is cho-
sen for the non-negative question. In the ambigu-
ous context, stereotypical bias arises whenever the
model selects the stereotyped group for the neg-
ative question and the non-stereotyped group for
the non-negative question, since the ground truth
is always "unknown." In contrast, always choosing
the stereotype option, irrespective of the question
type, reflects a general lexical bias.
In the disambiguated context, stereotypical bias
is only considered in the NNP scenario, where
the
disambiguated
context
assigns
the
non-
stereotyped group to the underlying stereotype.
For example, context says, “A woman performed a
harmful activity” (if the stereotype is that men do
this). Under such a scenario, the correct answer
to the negative question "Who did the activity?" is
the non-stereotyped group (here, the woman). If
the model still answers the negative question with
the stereotyped group despite the context, this in-
dicates a failure to respect disambiguating infor-
mation and reveals a stereotypical belief. In the
NP scenario, this is not classified as stereotypical
bias, as the model is expected to choose the stereo-
typed option for the negative question.
A higher SBSA or SBSD score therefore in-
dicates stronger alignment with the underlying
stereotype and thus a higher degree of model bias.
5
Experiments
Our evaluation setup consists mainly of five dif-
ferent multilingual LLMs: Llama-3.1-8B-instruct,
Gemma-2-9b-it,
Phi-3.5-mini-instruct,
bloomz-
7b1, and sarvam-2b-v0.5. We chose these models
because they have generative capabilities for In-
dian languages. As the BharatBBQ dataset is also
available in seven Indian languages apart from En-
glish, we evaluate each LLM for all eight lan-
guages under four different settings: a) Instruction
for QA is in target language, and zero-shot sce-
nario, b) Instruction for QA is in target language,
and two-shot scenario, c) Instruction for QA is in
English, and zero-shot scenario, d) Instruction for
QA is in English, and two-shot scenario.
For all settings, following ARC style QA (Clark
et al., 2018), the LLM is provided with the (am-
biguous/disambiguated) context, the correspond-
ing question, and three possible options to perform
the QA task. We discuss the prompt and evalua-
tion setup in Appendix C.
6
Results
In this section, we present a comprehensive anal-
ysis of model performance across different lan-
guages, social categories, and context types 3.
6.1
Zero-Shot and Few-Shot Accuracy
The analysis of accuracy and bias metrics for zero-
shot and few-shot settings across models reveals
several key insights that highlight model perfor-
mance and bias tendencies in ambiguous and dis-
ambiguated contexts.
Figure 4 illustrates that Gemma exhibits consis-
tently high accuracy across both English and target
3We will use BS for bias score and SBS for stereotypical
bias score through out Results section.

--- Page 9 ---

Figure 4: Zero-Shot Accuracy for English and Target Instructions, averaged across 13 categories.
language instructions, indicating its robust perfor-
mance irrespective of the instruction language.
In general, accuracy for ambiguous contexts (♦)
is lower compared to disambiguated contexts (×)
(Figure 4), this is because ambiguous contexts of-
ten have "unknown" as the ground truth, which
requires models to abstain from making defini-
tive predictions between stereotyped and non-
stereotyped options. For instance, Llama exhibits
particularly low accuracy in English in ambiguous
contexts under English instructions, as it rarely se-
lects the "unknown" option. This behavior is fur-
ther supported by Figure 5, where Llama’s bias
score (BS) for English in zero-shot under English
instructions is low, but its stereotypical bias score
(SBS) is significantly higher. This supports the im-
portance of our SBS metric over the existing BS
(Neplenbroek et al., 2024), as it better captures the
model’s reliance on stereotypes.
Bloomz shows a significant accuracy gap be-
tween ambiguous and disambiguated contexts,
with lower accuracy for the ambiguous contexts,
which aligns with its high BS and SBS for am-
biguous contexts (Figure 5). Similarly, Sarvam-1
shows low accuracy on average for both ambigu-
ous and disambiguated contexts.
This observa-
tion is also supported by its high stereotypical bias
scores (Figure 5), indicating that Sarvam-1 strug-
gles to provide correct answers when stereotype-
provoking questions are asked. Interestingly, its
bias score does not fully capture this behavior, re-
inforcing the need for our SBS metric.
The accuracy of each LLM under the few-shot
instruction setting across all languages is pre-
sented in Figure 10 (Appendix B). The observed
trends largely mirror those seen in the zero-shot.
Specifically, Gemma consistently achieves the
highest accuracy across both English and target-
language instructions; Bloomz exhibits a pro-
nounced drop in performance when transition-
ing from disambiguated to ambiguous contexts,
indicating its heavy reliance on the contextual
cues; and all models show lower accuracy when
prompted in target language compared to their
English-instruction counterparts. Given that accu-
racy remains nearly invariant between English and
native-language instructions in both zero-shot and
few-shot settings, we have chosen to use English
instructions for further analysis. Moreover, across
all languages, models achieve the highest accuracy
on English data when using English instructions,
reinforcing our choice to conduct subsequent anal-
yses using English instructions.
6.2
Bias Score and Stereotypical Bias Score
Figure 5 presents the bias and stereotypical bias
scores across models and languages in both zero-
shot and few-shot settings. Gemma exhibits low
BS and SBS scores in both zero- and few-shot
prompts compared to other models, making it the
least biased model on average across all categories
and languages. In contrast, Bloomz exhibits sig-
nificantly high BS and SBS for the disambiguated
context in both zero- and few-shot.
However,
for disambiguated contexts specifically, the SBS
are lower than the corresponding BS. This dis-
crepancy arises because the SBS only considers
non-negative pairings, whereas the BS accounts

--- Page 10 ---

Figure 5: Bias and Stereotypical Bias Scores using English instructions in Zero-Shot and Few-Shot
settings across 8 languages for 5 models, averaged over 13 categories. The first subgraph represents Bias
Scores in Zero-Shot, the second represents Bias Scores in Few-Shot, the third represents Stereotypical
Bias Scores in Zero-Shot, and the fourth represents Stereotypical Bias Scores in Few-Shot.
Figure 6: Stereotypical Bias Scores (SBS) for instances using proper nouns vs common nouns across
4 categories in 8 languages, averaged across both ambiguous and disambiguated contexts. The line
represents the mean SBS averaged across all categories and languages. The shaded region spans from
the minimum to the maximum average SBS of any one of the categories across languages for each model.
for both negative and non-negative pairings. As
shown in Fig.5, Bengali and Tamil have more BS
and SBS among Indian languages. Also, it can be
observed that Indian languages have higher BS.
Overall, the SBS decreases in few-shot compared
to zero-shot across models and languages, indicat-
ing that providing additional few-shot in-context
examples helps mitigate reliance on stereotypes.
6.3
Proper Noun vs. Common Noun
Figure 6 presents a comparison of SBS, aver-
aged across ambiguous and disambiguated con-
texts, between instances involving common nouns
and proper nouns across four categories in which
we have examples consisting of both. On aver-
age, the bias patterns observed with proper nouns
are similar to those with common nouns across
languages and categories.
Gemma remains the
least stereotypically biased model as compared to
other models. For models like Gemma, Llama,
and Bloomz, the stereotypical bias for the religion
category is notably higher when proper nouns are
used compared to common nouns. Interestingly, in
Sarvam, the stereotypical bias score for religion in
Marathi is the highest when proper nouns are used,
whereas it is the lowest when common nouns are
used. Additionally, Sarvam also demonstrates a
significantly high gender bias in Hindi when com-
mon nouns are used.
Figure 11 (Appendix B) presents the compari-
son of SBS across different context types. In the
ambiguous setting, Bloomz exhibits notably high
SBS for both proper and common noun formula-
tions, followed by Sarvam. From Figures 5 and 6
we observe that Bloomz demonstrates consistently
higher bias across languages and social categories

--- Page 11 ---

relative to other models, a pattern also reported by
Zhao et al. (2023) and Huang and Xiong (2024) in
their analyses of multilingual bias.
6.4
Model Size Comparison
To check the effect of model size on bias, we ana-
lyze the bias scores of LLama and Gemma across
their two size variants. Figures
8 and
9 (Ap-
pendix B) illustrate these comparisons under zero-
shot and few-shot settings, respectively. Addition-
ally, we examine the Sarvam-1 and its newer vari-
ant, Sarvam-M4, with results summarized in Ta-
bles 8 and 9. Our analysis reveals that model size
has a non-uniform effect on bias.
Specifically,
Gemma exhibits an increase in both scores with
larger size, whereas LLaMA and Sarvam show a
modest reduction in bias as their size increases.
These findings suggest that scaling up parameters
does not universally alleviate bias; rather, its effect
varies by architecture and training pipeline. This
underscores the need for model-specific auditing
when evaluating fairness in LLMs.
6.5
BBQ vs BharatBBQ
Tables 4–7 present a comparative analysis of
bias and stereotypical bias scores for the five
LLMs on BBQ and English subset of BharatBBQ
across both ambiguous and disambiguated con-
texts.
Overall, we observe that both bias and
stereotypical bias scores are generally higher for
BharatBBQ, with the increase being particularly
pronounced in disambiguated contexts.
For ex-
ample, as shown in Table 4, LLama exhibits a
rise in bias for the Disability Status category from
0.11 (BBQ) to 0.33 (BharatBBQ) in the zero-
shot setting, with similar patterns observed across
other models and categories.
Table 6 further
shows a substantial increase in stereotypical bias,
with Gemma’s SBS for Age increasing from 0.25
(BBQ) to 0.47 (BharatBBQ).
Interestingly, Sarvam shows near-zero bias scores
on BBQ in ambiguous contexts, possibly due to
training data contamination or prior exposure to
the benchmark.
However, it exhibits bias on
BharatBBQ, suggesting that the localized social
contexts introduced in our benchmark expose bi-
ased behaviors that remain hidden in Western-
centric datasets. Moreover, for the Religion cate-
gory in ambiguous contexts, several models show
negative bias scores in BharatBBQ, indicating a
4https://www.sarvam.ai/blogs/sarvam-m
preference for the non-stereotypical group. This
could stem from lexical preferences or potential
overcorrection in model behavior.
6.6
Category Wise Analysis
Figure 7 illustrates the category-wise BS and SBS
in both ambiguous and disambiguated contexts,
averaged across all models.
In the ambiguous context, all models exhibit high
BS and SBS for the disability status category, indi-
cating a significant prejudice against disabled indi-
viduals across languages. This trend persists even
in the disambiguated context, where there remains
a notable bias toward disability status and sexual
orientation in the English language. Additionally,
we observe significant biases toward physical ap-
pearance and sexual orientation for the Telugu lan-
guage, with the sexual orientation being consistent
for both BS, SBS across contexts.
High stereotypical bias is observed across all cate-
gories in the ambiguous context for English, high-
lighting its sensitivity to stereotypes in various do-
mains.
Interestingly, while bias scores indicate
low prejudice for religion in the disambiguated
context across all languages, there is a significant
stereotypical bias for the religion category on av-
erage.
This suggests that models tend to favor
stereotypical religious groups as answers to neg-
ative questions, even in non-negative pairings.
6.7
Indian Languages vs. English
As shown in Figure 4 (and Figure 10 in Ap-
pendix B), all five models, particularly in disam-
biguated context, achieve their highest accuracy
on English examples when prompted in English.
Under both zero-shot and few-shot settings, ac-
curacy consistently declines for Indian languages.
However, for ambiguous contexts, some models
show low accuracy and high SBS on English ex-
amples. This pattern suggests that, potentially, in
ambiguous contexts, models overrely on stereo-
typical associations in English due to richer ex-
posure to biased patterns in English training data.
In contrast, in disambiguated contexts, models
better understand explicit contextual cues in En-
glish due to stronger syntactic and semantic align-
ment, resulting in higher accuracy and lower SBS.
For Indian languages, limited pretraining data and
weaker contextual understanding reduce accuracy
and lead models to rely more on stereotypes, in-
creasing SBS for disambiguated contexts.
No-
tably, Figures 8 and 9 show that larger LLMs con-

--- Page 12 ---

(a) Bias Scores in Ambiguous Context
(b) Bias Scores in Disambiguated Con-
text
(c) SBS in Ambiguous Context
(d) SBS in Disambiguated Context
Figure 7: Bias Scores (BS) and Stereotypical Bias Scores (SBS) across 13 categories and 8 languages in
both Ambiguous and Disambiguated contexts, averaged over 5 models.
sistently exhibit lower BS and SBS in English, re-
gardless of context type.
Figure 5 demonstrates that BS for Indian lan-
guages exceeds that for English across nearly
every model and context type.
For instance,
Gemma’s zero-shot BS in ambiguous contexts
rises from 0.025 in English to 0.15 in Bengali.
Bloomz, which already exhibits high BS in En-
glish, shows even larger scores (e.g., from 0.1 in
English to 0.25 in Telugu for zero-shot). This pat-
tern holds in both zero- and few-shot settings, in-
dicating that cultural and linguistic transfer intro-
duces additional stereotypical associations.
Overall, across categories, in English, we found
Bloomz and Llama exhibit the high bias in all
three categories. In contrast, for Indian languages,
Sarvam consistently shows the highest bias in
these categories.
7
Conclusion & Future Works
In this work, we introduced BharatBBQ, a cul-
turally adapted multilingual benchmark to evalu-
ate social biases in LLMs within the Indian con-
text. By modifying BBQ, we ensured cultural rel-
evance through adapted translations, target group
modifications, and new templates covering cate-
gories like caste, region, religion × gender, region
× gender, and age × gender. BharatBBQ extends
to seven Indian languages with 49,108 examples
per language and 3,92,864 examples across eight
languages.
Our experiments on five LLM families across 13
categories reveal persistent biases, particularly in
disability status, religion, and sexual orientation.
We also find that models exhibit varying bias pat-
terns when using proper nouns versus common
nouns, emphasizing the impact of linguistic and
cultural nuances. Additionally, our stereotypical
bias score metric proves more effective than tradi-
tional bias metrics, capturing the intended biases
that existing methods overlook.
In future work, it would be valuable to extend the
dataset to include more fine-grained demographic
attributes and more languages, along with code-
mixed texts, to improve its representational depth.

--- Page 13 ---

Acknowledgement
We thank the anonymous reviewers and the Ac-
tion Editor for their constructive feedback, which
helped improve the quality and clarity of this
work. We are grateful to the annotators for their
time and effort, and to the members of the CFILT
Lab at IIT Bombay for their support throughout
the research work. We also sincerely thank all in-
dividuals who provided valuable input during the
dataset creation process.
References
Panatchakorn Anantaprayoon, Masahiro Kaneko,
and Naoaki Okazaki. 2024. Evaluating gender
bias of pre-trained language models in natural
language inference by considering all labels.
Zaheer Baber. 2022a. ‘race might be a unicorn,
but its horn could draw blood’: Racialisation,
class and racism in a non-western context. Crit-
ical Sociology, 48(1):151–169.
Zaheer Baber. 2022b. ‘race might be a unicorn,
but its horn could draw blood’: Racialisation,
class and racism in a non-western context. Crit-
ical Sociology, 48(1):151–169.
Mukul Bhutani, Kevin Robinson, Vinodkumar
Prabhakaran, Shachi Dave, and Sunipa Dev.
2024. SeeGULL multilingual: a dataset of geo-
culturally situated stereotypes. In Proceedings
of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 2: Short
Papers), pages 842–854, Bangkok, Thailand.
Association for Computational Linguistics.
Business Standard. 2023. India only nation with
no history of antisemitism, diaspora supports is-
rael. Accessed: 2025-06-15.
Chris Callison-Burch, Cameron Fordyce, Philipp
Koehn, Christof Monz, and Josh Schroeder.
2007.
(meta-) evaluation of machine transla-
tion. In Proceedings of the Second Workshop
on Statistical Machine Translation, pages 136–
158, Prague, Czech Republic. Association for
Computational Linguistics.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar
Khot, Ashish Sabharwal, Carissa Schoenick,
and Oyvind Tafjord. 2018.
Think you have
solved question answering? try arc, the ai2 rea-
soning challenge.
Jacob Cohen. 1960. A coefficient of agreement for
nominal scales. Educational and Psychological
Measurement, 20(1):37–46.
CSPS. 2023. Antisemitism and the perception of
hitler in india. Accessed: 2025-06-15.
Debarati Das, Karin De Langis, Anna Martin-
Boyle,
Jaehyung
Kim,
Minhwa
Lee,
Zae Myung Kim, Shirley Anugrah Hayati,
Risako Owan, Bin Hu, Ritik Parkar, Ryan Koo,
Jonginn Park, Aahan Tyagi, Libby Ferland,
Sanjali Roy,
Vincent Liu,
and Dongyeop
Kang. 2024. Under the surface: Tracking the
artifactuality of llm-generated data.
Sayan
Dey.
2021.
Corona-logy:
A
re-
configuration of racial dynamics in contem-
porary india.
Research in Social Change,
13(1):150–157.
Jay Gala, Pranjal A Chitale, A K Raghavan, Varun
Gumma, Sumanth Doddapaneni, Aswanth Ku-
mar M, Janki Atul Nawale, Anupama Su-
jatha, Ratish Puduppully, Vivek Raghavan,
Pratyush Kumar, Mitesh M Khapra, Raj Dabre,
and Anoop Kunchukuttan. 2023. Indictrans2:
Towards high-quality and accessible machine
translation models for all 22 scheduled indian
languages. Transactions on Machine Learning
Research.
Sanjana Gautam and Mukund Srinath. 2024.
Blind spots and biases: Exploring the role of an-
notator cognitive biases in NLP. In Proceedings
of the Third Workshop on Bridging Human–
Computer Interaction and Natural Language
Processing, pages 82–88, Mexico City, Mexico.
Association for Computational Linguistics.
Dirk Hovy and Shrimai Prabhumoye. 2021. Five
sources of bias in natural language process-
ing.
Language and Linguistics Compass,
15(8):e12432.
Yufei Huang and Deyi Xiong. 2024.
CBBQ:
A Chinese bias benchmark dataset curated
with human-AI collaboration for large language
models. In Proceedings of the 2024 Joint In-
ternational Conference on Computational Lin-
guistics,
Language Resources and Evalua-

--- Page 14 ---

tion (LREC-COLING 2024), pages 2917–2929,
Torino, Italia. ELRA and ICCL.
Sophie Jentzsch and Cigdem Turan. 2022. Gender
bias in BERT - measuring and analysing biases
through sentiment rating in a realistic down-
stream classification task. In Proceedings of the
4th Workshop on Gender Bias in Natural Lan-
guage Processing (GeBNLP), pages 184–199,
Seattle, Washington. Association for Computa-
tional Linguistics.
Akshita Jha, Aida Mostafazadeh Davani, Chan-
dan K Reddy, Shachi Dave, Vinodkumar Prab-
hakaran, and Sunipa Dev. 2023. SeeGULL: A
stereotype benchmark with broad geo-cultural
coverage leveraging generative models.
In
Proceedings of the 61st Annual Meeting of
the Association for Computational Linguistics
(Volume 1: Long Papers), pages 9851–9870,
Toronto, Canada. Association for Computa-
tional Linguistics.
Jiho Jin, Jiseon Kim, Nayeon Lee, Haneul Yoo,
Alice Oh, and Hwaran Lee. 2024.
KoBBQ:
Korean bias benchmark for question answering.
Transactions of the Association for Computa-
tional Linguistics, 12:507–524.
Khyati Khandelwal, Manuel Tonneau, Andrew M.
Bean, Hannah Rose Kirk, and Scott A. Hale.
2024.
Indian-bhed: A dataset for measuring
india-centric biases in large language models.
In Proceedings of the 2024 International Con-
ference on Information Technology for Social
Good, page 231–239. ACM.
Ruibo Liu, Chenyan Jia, Jason Wei, Guangx-
uan Xu, Lili Wang, and Soroush Vosoughi.
2021.
Mitigating political bias in language
models through reinforced calibration. ArXiv,
abs/2104.14795.
Moin Nadeem, Anna Bethke, and Siva Reddy.
2021. StereoSet: Measuring stereotypical bias
in pretrained language models.
In Proceed-
ings of the 59th Annual Meeting of the Asso-
ciation for Computational Linguistics and the
11th International Joint Conference on Natu-
ral Language Processing (Volume 1: Long Pa-
pers), pages 5356–5371, Online. Association
for Computational Linguistics.
Nikita Nangia, Clara Vania, Rasika Bhalerao, and
Samuel R. Bowman. 2020.
CrowS-pairs: A
challenge dataset for measuring social biases in
masked language models.
In Proceedings of
the 2020 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pages
1953–1967, Online. Association for Computa-
tional Linguistics.
Vera Neplenbroek, Arianna Bisazza, and Raquel
Fernández. 2024. Mbbq: A dataset for cross-
lingual comparison of stereotypes in generative
llms.
Shilpi Pandey. 2024. The burden of being a mus-
lim woman in india—the instrumentalisation of
muslim women at the intersection of gender, re-
ligion, colonialism, and secularism. Religions,
15(3).
Alicia Parrish,
Angelica Chen,
Nikita Nan-
gia, Vishakh Padmakumar, Jason Phang, Jana
Thompson, Phu Mon Htut, and Samuel Bow-
man. 2022. BBQ: A hand-built bias benchmark
for question answering. In Findings of the As-
sociation for Computational Linguistics: ACL
2022, pages 2086–2105, Dublin, Ireland. Asso-
ciation for Computational Linguistics.
Ramnarayan S Rawat. 2013. Occupation, dignity,
and space: The rise of dalit studies.
History
Compass, 11(12):1059–1067.
Nihar Sahoo, Pranamya Kulkarni, Arif Ahmad,
Tanu Goyal, Narjis Asad, Aparna Garimella,
and Pushpak Bhattacharyya. 2024. IndiBias: A
benchmark dataset to measure social biases in
language models for Indian context.
In Pro-
ceedings of the 2024 Conference of the North
American Chapter of the Association for Com-
putational Linguistics: Human Language Tech-
nologies (Volume 1: Long Papers), pages 8786–
8806, Mexico City, Mexico. Association for
Computational Linguistics.
Sindhuja Sankaran, Maciek Sekerdej, and Ulrich
Von Hecker. 2017.
The role of indian caste
identity and caste inconsistent norms on status
representation. Frontiers in psychology, 8:487.
Emily
Sheng,
Kai-Wei
Chang,
Premkumar
Natarajan, and Nanyun Peng. 2019.
The
woman worked as a babysitter: On biases in
language generation.
In Proceedings of the
2019 Conference on Empirical Methods in Nat-
ural Language Processing and the 9th Interna-
tional Joint Conference on Natural Language

--- Page 15 ---

Processing (EMNLP-IJCNLP), pages 3407–
3412, Hong Kong, China. Association for Com-
putational Linguistics.
Sandhya Singh, Prapti Roy, Nihar Sahoo, Ni-
teesh Mallela, Himanshu Gupta, Pushpak Bhat-
tacharyya, Milind Savagaonkar, Nidhi Sultan,
Roshni Ramnani, Anutosh Maitra, and Shub-
hashis Sengupta. 2022.
Hollywood identity
bias dataset:
A context oriented bias analy-
sis of movie dialogues. In Proceedings of the
Thirteenth Language Resources and Evalua-
tion Conference, pages 5274–5285, Marseille,
France. European Language Resources Associ-
ation.
Gopal Sharan Sinha and Ramesh Chandra Sinha.
1967. Exploration in caste stereotypes. Social
Forces, 46(1):42–47.
Gabriel Stanovsky, Noah A. Smith, and Luke
Zettlemoyer. 2019. Evaluating gender bias in
machine translation. In Proceedings of the 57th
Annual Meeting of the Association for Com-
putational Linguistics, pages 1679–1684, Flo-
rence, Italy. Association for Computational Lin-
guistics.
Amit Thorat, Nazar Khalid, Nikhil Srivastav,
Payal Hathi, Dean Spears, and Diane Coffey.
2020.
Persisting prejudice: Measuring atti-
tudes and outcomes by caste and gender in in-
dia. Caste (Waltham, Mass.), 1(2):1.
Benjamin Warner, Antoine Chaffin, Benjamin
Clavié, Orion Weller, Oskar Hallström, Said
Taghadouini, Alexis Gallagher, Raja Biswas,
Faisal Ladhak, Tom Aarsen, Nathan Cooper,
Griffin Adams, Jeremy Howard, and Iacopo
Poli. 2024.
Smarter, better, faster, longer: A
modern bidirectional encoder for fast, memory
efficient, and long context finetuning and infer-
ence.
Craig S Webster, Saana Taylor, Courtney Thomas,
and Jennifer M Weller. 2022. Social bias, dis-
crimination and inequity in healthcare: mecha-
nisms, implications and recommendations. BJA
education, 22(4):131–137.
Jiaxu Zhao, Meng Fang, Shirui Pan, Wenpeng Yin,
and Mykola Pechenizkiy. 2023.
Gptbias: A
comprehensive framework for evaluating bias in
large language models.
Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente
Ordonez, and Kai-Wei Chang. 2018.
Gender
bias in coreference resolution: Evaluation and
debiasing methods.

--- Page 16 ---

A
Annotation Details
Fluency
Adequacy
F1
F2
A1
A2
hi_ctx
4.80
4.72
4.88
4.78
hi_qa
4.80
4.78
4.78
4.84
hi_combined
4.80
4.75
4.83
4.81
or_ctx
4.82
4.74
4.78
4.68
or_qn
4.9
4.7
4.84
4.92
or_combined
4.86
4.72
4.81
4.80
te_ctx
4.58
4.72
4.64
4.72
te_qn
4.68
4.70
4.64
4.84
te_combined
4.63
4.71
4.64
4.78
ta_ctx
5
5
4.94
4.88
ta_qn
5
5
5
5
ta_combined
5
5
4.97
4.94
mr_ctx
4.63
4.78
4.46
4.58
mr_qn
4.48
4.68
4.52
4.56
mr_combined
4.55
4.73
4.49
4.57
bn_ctx
4.56
4.78
4.62
4.76
bn_qn
4.68
4.86
4.64
4.76
bn_combined
4.62
4.82
4.63
4.76
as_ctx
4.7
4.68
4.83
4.78
as_qn
4.82
4.92
4.88
4.9
as_combined
4.76
4.8
4.85
4.84
Table 3: Translation Quality through Human
Judgement: F1 and F2 denote the average fluency
scores assigned by the two annotators for each
data subset listed in the rows. Likewise, A1 and
A2 represent the average adequacy scores from
each annotator, respectively.
Language codes
hi, or, te, ta, mr, bn, and as correspond
to Hindi, Odia, Telugu, Tamil, Marathi, Ben-
gali, and Assamese — the seven Indian languages
in the BharatBBQ benchmark. The string ctx
indicates samples drawn from ambiguous/disam-
biguated contexts, qn represents questions, and
combined refers to a merged set of both con-
texts and questions. For instance, mr_qn refers
to a random sample of 100 questions from the
Marathi subset of BharatBBQ. The usefulness of
this quality assessment is discussed in Section 3.4.
A.1
Human Annotation Guidelines for
Translation Evaluation
As discussed in Section 3.4, this annotation task
evaluates the quality of machine-translated outputs
of both ambiguous/disambiguated contexts and
questions from our dataset into seven Indian lan-
guages. To ensure reasonable translation quality,
we only considered sentences whose cosine sim-
ilarity score after backtranslation exceeded 0.75.
For each language and each sentence type (context
or question), we randomly sampled 100 unique
sentences, resulting in 200 annotated sentences
per target language. Following the methodology
of (Callison-Burch et al., 2007), annotators were
asked to rate each translation on two dimensions:
Adequacy and Fluency. The target languages in-
clude Hindi, Marathi, Odia, Telugu, Tamil, Ben-
gali, and Assamese.
For each English reference sentence and its
machine-translated counterpart in a target lan-
guage, annotators provided:
• A score between 1–5 for Adequacy
• A score between 1–5 for Fluency
• A one-sentence justification for each rating
Adequacy Scale (1–5)
Adequacy measures how much of the meaning ex-
pressed in the English reference sentence is pre-
served in the target language translation.
Score
Meaning
5
All meaning preserved
4
Most of the meaning preserved
3
Much of the meaning preserved
2
Little of the meaning preserved
1
None of the meaning preserved
Fluency Scale (1–5)
Fluency measures how natural and grammatically
correct the sentence is in the target language, irre-
spective of the source meaning.
Score
Description (per target language)
5
Flawless language (native, natural, and error-free)
4
Good language (minor issues but understandable and fluent)
3
Non-native (awkward or foreign-sounding but understandable)
2
Disfluent (ungrammatical or poorly formed)
1
Incomprehensible
Table 3 presents the average fluency and adequacy
scores assigned by both annotators, reported sep-
arately for each sentence type: context, question,
and their combination.
B
Additional Results
In this section, we present additional analyses that
complement our main findings, including com-
parisons across model sizes, a detailed evaluation
of performance on BBQ versus BharatBBQ, and
other supplementary results.

--- Page 17 ---

(a) Bias Score
(b) Stereotypical Bias Score
Figure 8: Zero-Shot Model Size Comparison: Bias and Stereotypical Bias Scores in English Instruction
(Discussed in §6.4)
(a) Bias Score
(b) Stereotypical Bias Score
Figure 9: Few-Shot Model Size Comparison: Bias and Stereotypical Bias Scores in English Instruction.
(Discussed in §6.4)
Figure 10: Few-Shot Accuracy for English and Target Instructions, averaged across 13 categories (dis-
cussed in §6.1).

--- Page 18 ---

Category (↓)
Llama
Gemma
Phi
Bloomz
Sarvam
Zero
Few
Zero
Few
Zero
Few
Zero
Few
Zero
Few
Dataset (–>)
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
Gender
0.31 / 0.03
0.04 / 0.02
0.08 / 0.1
0 / 0
0.11 / 0.07
0.06 / 0.03
0.22 / 0.26
0.16 / 0.18
0 / 0.09
0 / 0.12
Religion
0.24 / -0.19
0.05 / -0.22
0.09 / -0.01
0.06 / 0
0.09 / -0.06
0.08 / -0.05
0.19 / 0.01
0.11 / -0.03
0 / -0.31
0.01 / -0.32
Disability Status
0.31 / 0.39
0.04 / 0.02
0.08 / 0.24
0 / 0.22
0.11 / 0.2
0.06 / 0.2
0.22 / 0.23
0.16 / -0.09
0 / 0.17
0 / 0.02
Sexual Orientation
0.12 / 0.04
0.02 / -0.01
0.06 / -0.1
0.01 / -0.02
0 / -0.06
0.01 / -0.02
0.03 / -0.38
0.02 / -0.44
0.04 / 0.16
0.01 / 0.17
Age
0.55 / -0.04
0.34 / -0.03
0.39 / -0.05
0.17 / -0.05
0.4 / 0.04
0.2 / 0.04
0.25 / -0.06
0.23 / 0
0 / -0.08
-0.01 / -0.1
Physical Appearance
0.54 / 0.04
0.26 / 0.01
0.16 / -0.04
0.02 / 0
0.39 / 0.01
0.23 / 0.02
0.68 / -0.06
0.59 / 0.02
0.01 / -0.35
0.02 / -0.28
Socioeconomic
0.37 / 0.13
0.07 / 0.15
0.05 / -0.02
0 / -0.01
0.12 / -0.03
0.03 / -0.03
0.31 / -0.05
0.28 / -0.04
0 / 0.25
0 / 0.31
Nationality
0.28 / -0.07
0.07 / -0.04
0.08 / 0
0.01 / 0.02
0.08 / 0.14
0.02 / 0.06
0.18 / 0.13
0.09 / 0.14
0.01 / 0.28
0.01 / 0.26
Caste
– / -0.08
– / -0.06
– / 0.01
– / 0.01
– / -0.01
– / -0.02
– / -0.02
– / -0.24
– / 0.14
– / 0.15
Region
– / 0.23
– / 0.18
– / 0.13
– / 0.08
– / 0.2
– / 0.12
– / 0.08
– / 0.08
– / 0.24
– / 0.25
Religion × Gender
– / 0.02
– / -0.04
– / -0.02
– / 0.01
– / -0.02
– / -0.03
– / 0.04
– / -0.02
– / -0.11
– / -0.11
Region × Gender
– / -0.08
– / -0.03
– / 0.01
– / -0.03
– / -0.01
– / 0.02
– / -0.13
– / -0.12
– / 0.03
– / 0.04
Age × Gender
– / 0.17
– / 0.15
– / 0.15
– / 0.06
– / 0.08
– / 0.11
– / 0.17
– / 0.15
– / 0.1
– / 0.03
Table 4: Bias score comparison between BBQ and BharatBBQ over eight common categories, evalu-
ated in zero-shot and few-shot settings in ambiguous context across five LLMs, as described in §6.5.
Category (↓)
Llama
Gemma
Phi
Bloomz
Sarvam
Zero
Few
Zero
Few
Zero
Few
Zero
Few
Zero
Few
Dataset (–>)
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
Gender
-0.09 / -0.02
0 / 0.02
0 / 0.01
0 / 0.01
0.04 / 0.04
0.03 / 0.01
0 / 0.01
0 / 0.07
0.11 / 0.08
0.13 / 0.04
Religion
0 / 0.03
0 / 0.04
-0.01 / 0
0.04 / 0.01
-0.01 / 0.02
-0.01 / 0.02
0 / 0.01
0.03 / 0.02
-0.04 / -0.22
-0.08 / 0.06
Disability Status
0.11 / 0.33
0.23 / 0.02
0.1 / 0.24
0.03 / 0.22
0.18 / 0.2
0.21 / 0.2
0.12 / 0.23
0.19 / -0.09
0.25 / 0.17
0.26 / 0.02
Sexual Orientation
0 / -0.02
0.01 / 0.04
-0.04 / 0.11
-0.04 / -0.01
-0.03 / 0.06
-0.01 / 0
-0.03 / 0.05
-0.05 / 0.16
0.03 / 1
0.01 / 0.8
Age
-0.02 / 0.05
-0.03 / 0.05
0 / 0.01
-0.01 / 0.01
0 / 0.05
0.01 / 0.02
-0.01 / 0.07
-0.01 / 0.02
-0.03 / -0.11
-0.03 / -0.05
Physical Appearance
-0.04 / 0.07
-0.05 / 0.12
-0.02 / 0.03
0.03 / 0.09
0.01 / 0.08
0 / 0.15
-0.03 / 0.22
0 / 0.27
-0.11 / 0.05
-0.08 / 0.16
Socioeconomic
0 / 0.02
0.05 / 0.06
0 / 0.02
-0.02 / 0.02
0.03 / 0.01
0.03 / 0.03
-0.02 / 0.07
-0.03 / 0.06
0.35 / 0.5
0.34 / 0.41
Nationality
0.01 / 0.03
0 / 0.07
0.01 / 0.02
-0.01 / 0.04
0 / 0.03
-0.02 / 0.05
0 / 0.08
-0.01 / 0.12
-0.05 / -0.19
-0.02 / 0.14
Caste
– / 0.13
– / 0.05
– / 0.02
– / 0.03
– / 0.06
– / 0.09
– / 0.07
– / 0.12
– / 0.1
– / 0.13
Region
– / 0.1
– / 0.1
– / 0.04
– / 0.06
– / 0.01
– / 0.03
– / -0.01
– / 0.02
– / 0.02
– / 0.03
Religion × Gender
– / 0.02
– / 0.09
– / 0.07
– / 0.06
– / 0.09
– / 0.07
– / -0.03
– / 0.01
– / 0.41
– / 0.16
Region × Gender
– / -0.01
– / 0
– / 0
– / 0
– / 0.01
– / 0.01
– / 0.01
– / -0.02
– / 0.14
– / 0.15
Age × Gender
– / 0
– / 0.02
– / 0.02
– / 0.03
– / 0
– / 0.03
– / 0.02
– / 0.03
– / -0.15
– / -0.1
Table 5: Bias score comparison between BBQ and BharatBBQ over eight common categories, evalu-
ated in zero-shot and few-shot settings in disambiguated context across five LLMs, as described in §6.5.
Category (↓)
Llama
Gemma
Phi
Bloomz
Sarvam
Zero
Few
Zero
Few
Zero
Few
Zero
Few
Zero
Few
Dataset (–>)
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
Gender
0.1 / 0.52
0.05 / 0.17
0.02 / 0.1
0 / 0
0.03 / 0.27
0.01 / 0.11
0.47 / 0.48
0.39 / 0.47
0.25 / 0.38
0.23 / 0.39
Religion
0.4 / 0.34
0.15 / 0.21
0.14 / 0.04
0.04 / 0
0.21 / 0.15
0.09 / 0.07
0.53 / 0.43
0.54 / 0.38
0.32 / 0.35
0.35 / 0.34
Disability Status
0.62 / 0.63
0.48 / 0.25
0.3 / 0.21
0.01 / 0.01
0.65 / 0.38
0.39 / 0.24
0.72 / 0.54
0.76 / 0.52
0.7 / 0.49
0.72 / 0.47
Sexual Orientation
0.44 / 0.56
0.13 / 0.22
0.04 / 0.19
0 / 0.02
0.16 / 0.25
0.04 / 0.11
0.34 / 0.53
0.28 / 0.5
0.51 / 0.5
0.52 / 0.49
Age
0.43 / 0.69
0.26 / 0.43
0.25 / 0.47
0.06 / 0.2
0.34 / 0.5
0.17 / 0.28
0.44 / 0.62
0.46 / 0.61
0.38 / 0.45
0.4 / 0.43
Physical Appearance
0.45 / 0.68
0.26 / 0.36
0.25 / 0.22
0 / 0.01
0.33 / 0.48
0.2 / 0.27
0.48 / 0.83
0.49 / 0.79
0.34 / 0.41
0.38 / 0.42
Socioeconomic
0.43 / 0.56
0.17 / 0.24
0.05 / 0.14
0 / 0.01
0.2 / 0.16
0.05 / 0.06
0.31 / 0.59
0.38 / 0.55
0.6 / 0.29
0.61 / 0.33
Nationality
0.45 / 0.63
0.23 / 0.3
0.16 / 0.24
0.03 / 0.1
0.3 / 0.29
0.11 / 0.13
0.47 / 0.62
0.46 / 0.55
0.4 / 0.4
0.44 / 0.41
Caste
– / 0.51
– / 0.49
– / 0.19
– / 0.08
– / 0.27
– / 0.21
– / 0.49
– / 0.48
– / 0.43
– / 0.45
Region
– / 0.57
– / 0.5
– / 0.47
– / 0.29
– / 0.44
– / 0.31
– / 0.46
– / 0.42
– / 0.45
– / 0.46
Religion × Gender
– / 0.4
– / 0.2
– / 0.1
– / 0.04
– / 0.19
– / 0.11
– / 0.38
– / 0.37
– / 0.39
– / 0.36
Region × Gender
– / 0.59
– / 0.34
– / 0.15
– / 0.06
– / 0.1
– / 0.04
– / 0.49
– / 0.51
– / 0.28
– / 0.26
Age × Gender
– / 0.49
– / 0.42
– / 0.4
– / 0.22
– / 0.38
– / 0.33
– / 0.56
– / 0.53
– / 0.44
– / 0.46
Table 6: Stereotypical Bias score comparison between BBQ and BharatBBQ over eight common
categories, evaluated in zero-shot and few-shot settings in ambiguous context across five LLMs, as
described in §6.5. The categories above the midline are both in BBQ and BharatBBQ.
Category (↓)
Llama
Gemma
Phi
Bloomz
Sarvam
Zero
Few
Zero
Few
Zero
Few
Zero
Few
Zero
Few
Dataset (–>)
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
BBQ / Bharat
Gender
0 / 0.01
0.01 / 0
0 / 0.01
0 /0.01
0.02 / 0.01
0.01 / 0.01
0.12 / 0.02
0.14 / 0.01
0.25 / 0.24
0.22 / 0.28
Religion
0.09 / 0.39
0.09 / 0.33
0.02/ 0.43
0.03 / 0.34
0.13 / 0.34
0.09 / 0.37
0.15 / 0.5
0.21 /0.46
0.34 / 0.19
0.32 / 0.3
Disability Status
0.21 / 0.37
0.3 / 0.11
0.15 / 0.05
0 / 0.03
0.36 / 0.04
0.31 / 0.02
0.28 / 0.01
0.43 / 0.01
0.69 / 0.46
0.72 / 0.34
Sexual Orientation
0.03 / 0.05
0.02 / 0.02
0 / 0.03
0 / 0
0.02 / 0.02
0.03 / 0.04
0.11 / 0
0.13 / 0
0.5 / 0
0.5 / 0.5
Age
0.03 / 0
0.07 / 0
0.02 / 0
0.01 / 0
0.03 / 0.02
0.04 / 0.01
0.18 / 0.08
0.19 / 0.05
0.41 / 0.39
0.41 / 0.35
Physical Appearance
0.07 / 0.01
0.1 / 0.02
0.04 / 0.01
0.02 / 0
0.16 / 0.02
0.11 / 0.03
0.13 / 0.19
0.16 / 0.28
0.32 / 0.55
0.37 / 0.48
Socioeconomic
0 / 0
0.06 / 0
0 / 0.01
0 / 0.02
0.04 / 0
0.02 / 0.01
0.07 / 0.01
0.08 / 0.01
0.62 / 0.33
0.61 / 0.41
Nationality
0.04 / 0.06
0.04 / 0.07
0 / 0.04
0 / 0.03
0.09 / 0.05
0.04 / 0.05
0.09 / 0.1
0.14 /0.1
0.4 /0.11
0.44 / 0.17
Caste
– / 0.06
– / 0.04
– / 0.01
– / 0.02
– / 0.02
– / 0.04
– / 0.1
– / 0.09
– / 0.29
– / 0.34
Region
– / 0.08
– / 0.06
– / 0.06
– / 0.07
– / 0.06
– / 0.06
– / 0.01
– / 0.02
– / 0.26
– / 0.22
Religion × Gender
– / 0.01
– / 0.03
– / 0
– / 0
– / 0.1
– / 0.12
– / 0
– / 0.02
– / 0.5
– / 0.31
Region × Gender
– / 0
– / 0
– / 0
– / 0
– / 0
– / 0
– / 0
– / 0
– / 0.03
– / 0.06
Age × Gender
– / 0.03
– / 0.04
– / 0.04
– / 0.03
– / 0.05
– / 0.06
– / 0.05
– / 0.08
– / 0.29
– / 0.24
Table 7: Stereotypical Bias score comparison between BBQ and BharatBBQ over eight common
categories, evaluated in zero-shot and few-shot settings in disambiguated context across five LLMs, as
described in §6.5. The categories above the midline are both in BBQ and BharatBBQ.

--- Page 19 ---

Language (↓)
Sarvam1
Sarvam-M
English Instruction
Target Instruction
English Instruction
Target Instruction
Zero
Few
Zero
Few
Zero
Few
Zero
Few
English
0.11
0.12
–
–
0.07
0.06
–
–
Hindi
0.11
0.14
0.06
0.12
0.09
0.08
0.11
0.10
Marathi
0.13
0.08
0.05
0.12
0.08
0.07
0.09
0.09
Telugu
0.10
0.10
0.22
0.17
0.06
0.04
0.07
0.05
Tamil
0.13
0.15
0.13
0.19
0.08
0.05
0.07
0.06
Odia
0.06
0.10
0.06
0.11
0.05
0.05
0.08
0.05
Bengali
0.10
0.10
0.13
0.07
0.09
0.08
0.09
0.09
Assamese
0.08
0.02
0.08
0.02
0.09
0.07
0.09
0.06
Table 8: Bias score comparison between Sarvam1 and Sarvam-M across eight languages under
English-instruction and Target-instruction settings, evaluated in zero-shot and few-shot modes, as dis-
cussed in Section 6.4.
Language (↓)
Sarvam1
Sarvam-M
English Instruction
Target Instruction
English Instruction
Target Instruction
Zero
Few
Zero
Few
Zero
Few
Zero
Few
English
0.34
0.35
–
–
0.27
0.16
–
–
Hindi
0.32
0.34
0.39
0.38
0.22
0.21
0.25
0.22
Marathi
0.36
0.30
0.33
0.32
0.17
0.18
0.19
0.19
Telugu
0.4
0.38
0.46
0.38
0.21
0.19
0.22
0.20
Tamil
0.39
0.42
0.43
0.45
0.17
0.16
0.20
0.16
Odia
0.41
0.42
0.37
0.38
0.27
0.27
0.24
0.25
Bengali
0.36
0.32
0.30
0.29
0.22
0.20
0.24
0.23
Assamese
0.33
0.31
0.33
0.31
0.21
0.20
0.24
0.23
Table 9: Stereotypical Bias score comparison between Sarvam1 and Sarvam-M across eight lan-
guages under English-instruction and Target-instruction settings, evaluated in zero-shot and few-shot
modes, as discussed in Section 6.4.
C
Prompts Used & Evaluation setup
Example Prompt
You are given a scenario-based
context and a multiple-choice
question along with three answer
options.
Your task is to select
the most appropriate answer based
on the given question.
Respond
only with the correct answer
without any explanation.
Context:
{ctx}
Question:
{qn}
Option 1:
{a}
Option 2:
{b}
Option 3:
{c}
The correct answer is:
Here, we explain the structure of one of the
prompts from our experiments (zero-shot English
instruction). Each input to the model follows a
standardized prompt format that presents a short
scenario (the context), a multiple-choice question,
and three answer options. The three options al-
ways correspond to: (i) the stereotyped group,
(ii) the non-stereotyped group, and (iii) the “un-
known” response, which indicates insufficient in-
formation.
The prompt instructs the model to
choose the most appropriate answer based solely
on the given context and question, and to respond
only with the final answer (i.e., without providing
an explanation). We publicly release all prompts
used in our experiments, including both English
and target-language instruction variants5.
5Click to see prompts.

--- Page 20 ---

(a) Ambiguous Context
(b) Disambiguated Context
Figure 11: Stereotypical Bias Scores for instances using proper nouns vs common nouns across 4
categories in 8 languages. The line represents the mean Stereotypical Bias Score averaged across all
categories and languages in Ambiguous and Disambiguated Context. The shaded region spans from the
minimum to the maximum average stereotypical bias score of any one of the categories across languages
for each model. More discussion in Section 6.3 of the main paper.
To determine the model’s predicted answer for
each example, we independently evaluate the like-
lihood of each of the three answer options using
log-likelihood scoring. Specifically, for a given
context and question, we construct a prompt that
ends with the answer option under consideration
and compute the average log-probability of the
model generating that option as a continuation of
the prompt. This process is repeated separately
for all three options using an identical context and
question. The model’s final prediction is the op-
tion with the highest average log-probability, re-
flecting the one it deems most plausible based on
the given input. This approach ensures that the
model is evaluated not on surface token selection
but on its underlying confidence in each response,
thereby enabling a more reliable and comparable
measurement across languages and settings.
Limitations
While BharatBBQ provides a comprehensive
benchmark for evaluating biases in multilingual
LLMs within the Indian context, it has certain lim-
itations.
First, although we incorporate diverse
categories and intersectional biases, our dataset is
not exhaustive and may not fully capture all socio-
cultural biases present in Indian society. Expand-
ing coverage to additional social groups and di-
alectal variations remains an area for future work.
Second, while we analyze biases in five LLM
families, our findings may not generalize to all
language models, particularly those trained on
significantly different data distributions.
Lastly,
BharatBBQ focuses on evaluating biases but does
not propose direct mitigation strategies, which we
leave as an avenue for future research. Finally,
while our analysis highlights that LLMs tend to
exhibit higher bias in Indian languages compared
to English, we do not investigate the underlying
causes of this behavior. Understanding the linguis-
tic, data-driven, or architectural factors contribut-
ing to this disparity is an important area for future
exploration.
Ethics Section
Our work evaluates biases in multilingual LLMs
within the Indian sociocultural context to promote
fairness in AI. BharatBBQ is designed to iden-
tify and measure biases without reinforcing them.
We carefully adapted BBQ to Indian linguistic
and cultural settings, ensuring it highlights model
biases without propagating harmful stereotypes.
While sensitive categories like caste and religion
are included, our dataset is strictly for research,
and we discourage any misuse. Proper names used
in the dataset or paper are not intended to target in-
dividuals but to capture linguistic and cultural nu-
ances.
Bias evaluation remains an evolving challenge,
and BharatBBQ may not capture all societal prej-
udices. However, it offers a structured approach
to bias assessment, highlighting the complexities
of AI fairness. We encourage further refinements,
ethical considerations, and broader community en-
gagement to enhance bias detection and foster
more inclusive AI systems.

```
