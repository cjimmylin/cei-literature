---
title: "Disentangling Perceptions of Offensiveness - PDF Extract"
source_pdf: "2023-Davani-Disentangling Perceptions of Offensiveness.pdf"
pages: 14
extracted_at: "2026-01-24T17:05:12.977707"
---

# PDF Extract: Disentangling Perceptions of Offensiveness

**Source PDF:** 2023-Davani-Disentangling Perceptions of Offensiveness.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

Disentangling Perceptions of Offensiveness: Cultural and Moral Correlates
Aida Davani
Google Research
aidamd@google.com
Mark Díaz
Google Research
markdiaz@google.com
Dylan Baker
Distributed AI Research Institute
dylan@dair-institute.org
Vinodkumar Prabhakaran
Google Research
vinodkpg@google.com
Abstract
Perception of offensiveness is inherently sub-
jective, shaped by the lived experiences and
socio-cultural values of the perceivers. Recent
years have seen substantial efforts to build AI-
based tools that can detect offensive language
at scale, as a means to moderate social media
platforms, and to ensure safety of conversa-
tional AI technologies such as ChatGPT and
Bard. However, existing approaches treat this
task as a technical endeavor, built on top of
data annotated for offensiveness by a global
crowd workforce without any attention to the
crowd workers’ provenance or the values their
perceptions reflect. We argue that cultural and
psychological factors play a vital role in the
cognitive processing of offensiveness, which is
critical to consider in this context. We re-frame
the task of determining offensiveness as essen-
tially a matter of moral judgment — deciding
the boundaries of ethically wrong vs. right lan-
guage within an implied set of socio-cultural
norms. Through a large-scale cross-cultural
study based on 4309 participants from 21 coun-
tries across 8 cultural regions, we demonstrate
substantial cross-cultural differences in percep-
tions of offensiveness. More importantly, we
find that individual moral values play a crucial
role in shaping these variations: moral concerns
about Care and Purity are significant mediat-
ing factors driving cross-cultural differences.
These insights are of crucial importance as we
build AI models for the pluralistic world, where
the values they espouse should aim to respect
and account for moral values in diverse geo-
cultural contexts.
As conversational Artificial Intelligence (AI)
technologies are becoming ubiquitous,1 there is
an increasing urgency to equip them with safety
guardrails that prevent inadvertent generation of
offensive and hateful content, as evident in many
recent academic and governmental calls for action
1such as ChatGPT (chat.openai.com) and Bard (bard.
google.com)
Figure 1: Distribution of labels provided from dif-
ferent countries. Annotators from China, Brazil, and
Egypt provided significantly different labels.
(Bai et al., 2022; Glaese et al., 2022; Commission,
2020; LLC, 2023). Technologies developed for
supporting such guardrails essentially rely on hu-
man assessments of language (Schmidt and Wie-
gand, 2017) that are emulated through reinforce-
ment learning (Ouyang et al., 2022) or supervised
modeling (Garg et al., 2023). The objective of
this paper is to demonstrate that such modeling
approaches should consider the socio-cultural and
moral aspects of language interpretation that im-
pact annotators’ subjective judgments, but are not
captured through existing data annotation practices.
Designing Natural Language Processing (NLP)
tools for detecting offensive or toxic text has long
been an active area of research, originally aimed
at automating online content moderation at scale
(Wulczyn et al., 2017; Founta et al., 2018). How-
ever, traditional NLP approaches largely over-
looked cultural and individual factors that shape an-
notators’ perspectives on what is deemed offensive
(Aroyo and Welty, 2015; Waseem, 2016; Salmi-
nen et al., 2019; Uma et al., 2021; Prabhakaran
et al., 2021). This oversight is especially troubling
when these tools are developed as safety guardrails
for conversational AI, considering the pace and
scale at which these technologies are being adopted
across geo-cultural contexts. The risk of cultural
skews becomes particularly salient in this context,
considering that the crowd-sourced workforce, es-
arXiv:2312.06861v1  [cs.CY]  11 Dec 2023

--- Page 2 ---

sential for annotation efforts, is disproportionately
made up of workers from the Global South (Geva
et al., 2019; Aroyo et al., 2023). Tailoring safety
guardrails to only some subgroups’ values and pref-
erences would in effect marginalize perspectives
and concerns of others (Salminen et al., 2019).
Furthermore, disagreements on what is offensive
expand beyond mere differences in socio-cultural
backgrounds. For instance, the intricate interplay
of social media content moderation and principles
of freedom of speech brings the task of offensive
language detection into the realm of moral and po-
litical deliberation (instances of such discussions
can be found in (Balkin, 2017; Brannon, 2019; Kir-
itchenko et al., 2021)). More generally, individ-
uals might systematically disagree on notions of
offensiveness, reflecting the complexity of beliefs
and values that shape their perspectives and judg-
ments within any given cultural context. Therefore,
we hypothesize that the high divergence in anno-
tators’ perceptions of offensiveness (Prabhakaran
et al., 2021) can be traced back to individuals’ di-
verse values besides the cultural and social norms
that dictate the boundaries of acceptable language
within a society.
In particular, we argue that these values are
shaped by what is considered as morally right or
wrong within a culture or by individuals. Anno-
tators from diverse cultural backgrounds may per-
ceive offensiveness in distinct ways and this vari-
ation in cultural perspectives can be attributed to
both the social norms prevalent in their societies,
and the moral values held by individuals within the
given socio-cultural context. To capture variances
in moral values we rely on the Moral Foundation
Theory (Graham et al., 2013) which proposes six
innate and universally available foundations that
form notions of moral reasoning. As per this theory,
moral foundations shape social behaviors and judg-
ments about what is considered as morally right or
wrong across different cultures and individuals.
Towards this goal, we conduct a two-pronged
study based on a large-scale cross-cultural lan-
guage annotation experiment, where we asked par-
ticipants from eight different cultural regions, bal-
anced across various socio-demographic groups,
to annotate offensiveness in social media posts cu-
rated from a popular NLP dataset. In study 1, we
demonstrate that perceptions of offensiveness vary
significantly across geo-cultural regions, even after
controlling for gender, age, and socio-economic
status of the participants, or whether or not they
were given a specific definition for offensiveness.
In order to investigate how individual moral values
shape these differences in perceptions, we also had
each of our participants fill out the Moral Founda-
tions Questionnaire (Atari et al., 2023). In study 2,
we find that the cross-cultural differences in percep-
tions of offensiveness are significantly mediated by
annotators’ individual moral concerns, in particular,
of Care and Purity, that vary across cultures.
We further demonstrate the real-world impli-
cations of these finding: popular AI-based mod-
els that analyze toxic language do preferentially
align with perspectives of individuals associated
with specific geo-cultural regions and moral values.
These findings emphasize the importance of under-
standing the cultural and psychological factors for
evaluating safety in AI models and content moder-
ation, highlighting the possible need for culturally-
informed data collection and model training ef-
forts. Our research further advocates for AI model
alignment efforts that are informed by variations of
moral values across cultures and individuals, sug-
gesting a meaningful paradigm for value alignment
beyond socio-demographic categorizations.
Data Collection
We recruited 4309 participants from 21 countries,2
across eight geo-cultural regions,3and asked them
to (i) annotate offensiveness of a set of text items,
and (ii) respond to a self-report measure of moral
concerns. Half of the annotators were given a spe-
cific definition for “extremely offensive language”
as profanity, strongly impolite, rude or vulgar lan-
guage expressed with fighting or hurtful words in
order to insult a targeted individual or group, while
the other half was not provided with a definition
to create a control setting of participants who are
expected to lean on their individual notion of offen-
siveness.
Recruitment criteria accounts for various demo-
2Argentina, Australia, Brazil, Canada, China, Egypt,
Germany, Ghana, India, Japan, Mexico, Netherlands, New
Zealand, Nigeria, Qatar, Singapore, South Korea, United Arab
Emirates, United Kingdom, United States of America, Viet-
nam
3Arab Culture, Indian Cultural Sphere, Latin Amer-
ica, North America, Oceania, Sinosphere, Sub Saha-
ran Africa, and Western Europe — loosely based on
the UN SDG groupings https://unstats.un.org/sdgs/
indicators/regional-groups with minor modifications:
combining Australia, NZ and Oceania to Oceania, and sep-
arating North America and Europe, to facilitate easier data
collection.

--- Page 3 ---

graphic attributes: (1) Region of residence: we
recruited at least 450 participants from each of the
eight regions, (2) Gender: within regions, we set
a maximum limit of 60% representation for each
of the two binary genders,4 (3) Age: in each region
at most 60% of participants are 18 to 30 years old
and at least 15% are 50 years old or older, and
(4) English fluency: we only selected participants
with high self-reported proficiency in reading and
writing English. Additionally, we collected par-
ticipants’ self-reported subjective socio-economic
status (Adler et al., 2000) as a potential confound.
We performed this study in the English language.
We selected items from Jigsaw’s Toxic Comments
Classification dataset (Jigsaw, 2018), and the Unin-
tended Bias in Toxicity Classification dataset (Jig-
saw, 2019), both of which consist of social media
comments labeled for toxicity. We built a dataset
of Nitems = 4554 consisting of three categories of
items sampled from the above datasets: (1) a ran-
dom set of items that are likely to be more ambigu-
ous (50%); (2) a balanced set of items that mention
specific social group identities related to gender,
sexual orientation, or religion (40%); and (3) a
balanced set of items include different moral senti-
ments, identified through a moral language tagger
trained on the MFTC dataset (Hoover et al., 2020).
(more description in the Materials and Methods).
Each participant was tasked to label the offen-
siveness of 40 items (including 5 control items for
quality check) on a 5-point Likert scale (from not
offensive at all to extremely offensive). Those who
failed the quality control check were removed, and
not counted against our final set of 4295 partici-
pants (see Materials and Methods for more details).
Each item in the final dataset had labels from at
least three participants in each region who passed
the control check.
After annotation, participants were also asked
to fill out the Moral Foundations Questionnaire
(MFQ-2; Graham et al., 2013; Atari et al., 2023),
which assesses their moral values along six dif-
ferent dimensions. The questionnaire includes 36
statements to assess participants’ priorities along
six moral foundations that include their intuitions
about: Care: avoiding emotional and physical dam-
age to another individual, Equality: equal treatment
and equal outcome for individuals, Proportional-
ity: individuals getting rewarded in proportion to
4Collecting non-binary gender information is not safe for
annotators in many countries, so we limited this study to binary
gender in our study to ensure consistency across countries.
Figure 2: Pairwise differences between geo-cultural
regions in their perceptions of offensiveness. 25 out
of the 28 pairs of regions shows significant differences.
their merit or contribution, Authority: deference
toward legitimate authorities and the defense of
traditions, Loyalty: cooperating with ingroups and
competing with outgroups, and Purity: avoiding
bodily and spiritual contamination and degradation.
We aggregate each participant’s responses to com-
pute a value between 1 to 5 to capture their moral
foundations along each of these dimensions.
Study 1: Geo-cultural Differences in
Offensiveness
As Figure 1 shows, the perceptions of offensiveness
in our data varied significantly across participants
from different geo-cultural regions. This trend was
further confirmed by a one-way ANOVA test us-
ing a cross-classified mixed-level regression model
with annotators as the first level, regions as the
second level, and items as the crossed level that
reported F(7,7515) = 31.47, p < .001.
On average, participants from the Arab Culture
(M = 1.19, SD = 1.48) and Latin America (M =
1.13, SD = 1.39) reported highest levels of offen-
sive scores, while participants from Sinosphere (M
= 0.80, SD = 1.22) and Oceania (M = 0.80, SD =
1.19) reported the least values of offensiveness.
Pairwise comparisons of regions show signifi-
cant differences between 25 out of the 28 pairs
of regions (See Figure 2). In line with the above
findings, annotations from Arab Culture and Latin
America differed significantly from every other

--- Page 4 ---

Figure 3: The association of cultural similarity to the
USA with reported levels of offensiveness.
region. For three pairs of regions (Sub-Saharan
Africa and Indian Culture, Western Europe and
North America, Sinosphere and Oceania) the anno-
tations are not significantly different.
To investigate whether the regional variances we
observe can be explained by other demographic fac-
tors, we also performed the mixed-level regression
analysis including annotators’ age, gender, and self-
reported socio-economic status, separately. The
effect of cross-regional differences holds even af-
ter accounting for annotators’ age (F(7,7515) =
26.80, p < .001), gender (F(7,7515) = 32.21, p <
.001), socio-economic status (F(7,7515) = 32.49,
p < .001) in the regression.
We further investigated whether providing a defi-
nition for offensiveness can significantly reduce the
cross-regional differences. Cross-region variances
are indeed lower when a definition is provided to
participants (F(7, ) = 15.22 as compared to F(7, ) =
18.95). However, controlling for whether or not the
definition is provided does not impact the observed
results (a one-way ANOVA reported F(7,7515)
= 31.54, p < .001). In other words, even when
annotators are asked to label based on a particular
definition, there is still significant variance between
participants of different regions.
While our regression analysis did account for
country-level factors, we further analyzed how the
trends we observe vary across countries within re-
gions. As Figure 1 shows, while participants from
Egypt, Brazil, India, and Argentina are more likely
to report offensive language (all four reporting an
average offensiveness score above 1.2 across all
items), participants from China labeled substan-
tially fewer data points as offensive (with an av-
erage offensiveness score below 0.6). This stark
difference in data collected from China could be,
in part, due to country-specific norms on language
use, or an artifact of that specific rater pool: e.g.,
more than two-third of the pool from China fall
within the 30-50 years old range, while this age-
group represents less than half the participants for
all other countries (See Table 1).5
We also study how our country-level results cor-
relate with established metrics that assess cultural
differences between countries. Participants from
countries associated with WEIRD (Western, Edu-
cated, Industrialized, Rich, and Democratic) cul-
tures (Henrich et al., 2010) generally report fewer
offensive labels (Figure 3). A one point increase
in the WEIRDness score (collected from (Muthukr-
ishna et al., 2020) which measures cultural simi-
larity to the United States) results in a 0.96 point
decrease in the offensiveness score (although the
effect is not significant with p = 0.18).6
We also study how our results correlate with
established metrics of cultural differences doc-
umented at country-level along Hofstede’s six
cultural dimensions (Hofstede, 2011):
Power
Distance,
Uncertainty
Avoidance,
Individu-
alism/Collectivism,
Masculinity/Femininity,
Long/Short
Term
Orientation,
and
Indul-
gence/Restraint.
While cultural tendency for
seeking equality on power distribution or fulfilling
one’s desires did not have a significant association
with annotation behavior, we find that participants
from countries that score higher on uncertainty
avoidance (β = 3.83, p < .001), individualism
(β = 4.80, p = .009), femininity (β = 2.73, p =
.026), and short-term orientation (β = 8.57, p <
.001) are more likely to report higher levels of
offensiveness in their annotations. These results
point to the importance of looking beyond the
geographical regions, and instead at finer-grained
values prevalent in specific countries.
Study 2: Moral Foundations of
Offensiveness
While Study 1 demonstrates significant cross-
cultural differences in perceptions of offensiveness
across regions and countries, cultural backgrounds
5Because of this anomalous behaviour, we confirmed that
our results hold even if we exclude data from China (which
still retains over 350 participants from Sinosphere) in our
region-level analysis.
6Removing data from China from the analysis leads to
significant impact of WEIRDness on annotations (p = 0.005),
such that a one point increase in the WEIRDness score results
in 1.54 decrease.

--- Page 5 ---

of participants only partly explain the observed dif-
ferences. The mixed-effects model from Study 1
in fact shows that 39.5% of the variance is due to
individual differences while country and region dif-
ference explain only 2.9% and 0.7% of the variance,
respectively. Hence, we expand the scope of the
analysis in Study 2, and include participant-level
variables that have potential impact on annotation
variances.
In particular, we consider the assessment of
whether something is offensive or not as a matter
of moral judgement, and hypothesize that partic-
ipants’ moral concerns play an important role in
their assessments. To test this, we first examine
whether participants’ individual moral concerns
that we measured through the Moral Foundation
Questionnaire-2, mediate the effect of geo-cultural
regions we observed on their perceptions of offen-
siveness in language.
We examine the mediation effect of each of the
six moral foundations on the effects of regions on
annotation differences. We consider each mediator
separately since participants’ score on each moral
foundation is an independent score. For each medi-
ation test, we tested three associations: (1) direct ef-
fect of independent variable (region) on dependent
variable (offensiveness): confirmed in Study 1; (2)
effect of independent variable (region) on the medi-
ator (each moral foundation): six one-way ANOVA
tests report significant effects of geo-cultural re-
gion on participants six morality scores (see Table
2); (3) combined effect of the independent variable
and mediators on the dependent variable: when
morality score variables are separately included
to the association of geo-cultural region and an-
notations, the results show a significant mediating
effect (Baron and Kenny, 1986) for Care (ACME7
= -0.034, p < .001), and Purity (ACME = -0.007,
p = .004). In other words, annotators’ perceptions
of offensiveness that vary significantly across geo-
cultural regions are significantly mediated by cul-
tural differences in moral values regarding Care and
Purity. As shown in Fig 4, an increase in annotators’
Care and Purity scores leads to varying degrees of
change in reported offensive scores in different re-
gions; while Arab Culture demonstrates the highest
positive change, Sinosphere demonstrates a chage
in the opposite direction.8
7Average Causal Mediating Effect
8Note that we observe markedly different trends in
Sinosphere, which can be attributed to data from China noted
before. Rerunning the mediation analysis excluding data from
We further assessed the impact of individual-
level moral concerns that go beyond country-level
concerns regarding Care and Purity on the annota-
tions. To this end for each annotator i from country
c, we considered the moral scores (e.g., Carei) as
the summation of the average moral score of all an-
notators from their country (e.g., Carec) and their
deviation from the average (e.g., Carei−c); such
that:
Carei = Carec + Carei−c
(1)
The results of two decomposition analyses for
Care and Purity values show that in both cases the
country-level moral concerns have less significant
impact on annotations compared to the individual-
level values. Specifically, in a mixed-level regres-
sion analysis with Carei and Carec as indepen-
dent variables and annotation labels as the depen-
dent variable, country-level Care score does not
have a significant effect (β = 0.27, p = .087), while
the individuals’ deviation from their country has a
significant impact on their annotations (β = 0.14,
p < .001). In other words a 1-point increase in par-
ticipants’ Care score compared to their country’s
average is associated with 0.14 increase in the of-
fensive score they assign to the items. A similar
trend with smaller magnitude is observed for Pu-
rity scores where country-level Purity score does
not have a significant effect (β = 0.05, p = .530),
while the individuals’ deviation from their country
has a significant impact on their annotations (β =
0.05, p < .001). A 1-point increase in participants’
Purity score compared to their country’s average is
associated with 0.05 increase in the offensive score
they assign to the items.
Study 3: Implications for Responsible AI
Detecting objectionable content at scale is one of
the core challenges in building responsible AI that
effectively and equitably serves the global commu-
nity. Our data collection relied on a geographically
diverse pool of annotators and the results of Study 1
and 2 demonstrated how annotators from different
geo-cultural regions with different moral values can
provide varying perspectives about the offensive-
ness of language. However, most model training
efforts are based on data annotation practices that
overlook these different perspectives about the task
China shows that the effect of regions on annotation labels
remains, with the mediation impact of Care (ACME= -0.043,
p < .001), and Purity (ACME= -0.015, p < .001).

--- Page 6 ---

Figure 4: Annotators’ scores on Care and Purity vary
across regions and mediate the regional differences in
annotating offensiveness. As the figures show one unit
of increase in annotators’ Care and Purity scores leads
to varying levels of increase (or decrease in case of
Sinosphere) in reported offensive scores.
at hand. To understand how this lack of represen-
tation impact data practices and models, we study
the correlation of our collected labels with human-
annotated labels provided in the original dataset
(Jigsaw), and model predictions of a commercial
tool for offensiveness detection (Perspective API).
We ask two main questions: (1) whether labels
provided in the dataset and trained model align
more with annotators of specific regions, and (2)
whether model labels are in higher agreement with
annotators with particular moral concerns.
Figure 5 presents the correlation of labels present
in the dataset (Jigsaw) as well as those provided by
the model (Perspective API), with the majority vote
in our data collected from different regions. Across
different geo-cultural regions, we observe a weak
but significant correlation between labels in the Jig-
saw dataset and majority labels we obtained from
Sub Saharan Africa, Latin America, and Western
Europe. On the other hand, we observe the least
correlation with Sinosphere and Oceania. It is im-
portant to note that the Jigsaw dataset is designed
for the task of toxicity detection,9 in contrast to
our data collection that centers around offensive
language, as defined distinctively for half of our
participants. Therefore, the relatively low correla-
tion between our collected annotations and labels
from Jigsaw should not come as a surprise.
On the other hand, Perspective API labels have
relatively higher correlation with majority votes of
different regions although Perspective API, sim-
ilar to Jigsaw’s datasets, is trained to detect tox-
icity rather than offensiveness. The highest cor-
relation is observed with annotations from Latin
America and Arab Culture, and lowest correlation
9defined as “a rude, disrespectful, or unreasonable com-
ment that is likely to make one leave a discussion.”
with Sinosphere and Oceania. Both the dataset and
model has the least correlation with Sinosphere and
Oceania, this can both be due to the fact that model
and dataset in general report high levels of toxicity
scores (Jigsaw M = 0.43, SD = 0.22, Perspective
API M = 0.39 , SD = 0.26 on a 0 to 1 range), while
annotators from Oceania and Sinosphere are the
least likely to report high levels of offensiveness
(Study 1). Moreover, higher correlation with Latin
America, Arab Culture, and Sub Saharan Africa
are potentially due to crowdworker recruitment ap-
proaches, which largely rely on workers from the
Global South. This similarity is especially impor-
tant since, we assume, Perspective API’s model for
English language is largely used by North Amer-
ican websites, therefore, the low correlation be-
tween model’s predictions and the majority vote
of North American participants may be an area of
special concern.
Furthermore, to evaluate whether labels from
Perspective API align with annotators with specific
moral values, we calculated its level of agreement
with each annotator. A regression model with this
agreement score as the dependant variable and an-
notators’ moral values as independent variables
showed that Perspective API agrees more with an-
notators who score high on the Care value, such
that a 1-point increase in the annotator’s Care score
leads to 0.027 (SE = 0.004) increase in their agree-
ment with Perspective API (p < 0.001).
In summary, these trends suggest not only that
the perceptions of offensiveness are shaped by the
socio-cultural backgrounds of the perceivers, but
also that the datasets and models that have become
standard in AI-based endeavors to detect and miti-
gate potentially offensive speech do preferentially
reflect certain socio-cultural value systems over
others.
General Discussion
Research on safety considerations of large lan-
guage models has mostly focused on evaluations of
model harms through crowdsourced benchmarks
(Srivastava et al., 2023; Wang et al., 2022). How-
ever, while annotators from different regions are
shown to have different perspectives regarding this
task (Salminen et al., 2018), current benchmarks
fail to represent the cultural and individual varia-
tions in human moral judgements about generated
language and model outputs. They also lack com-
prehensive understanding of human values and cul-

--- Page 7 ---

Figure 5: Correlation of labels provided in Perspective
API with majority vote of annotators from different
regions. Score interpretations can be summarized as:
(0.00-0.20): neglectable correlation, (0.20-0.40): weak
correlation, and (0.40-0.60): moderate correlation.
tural norms that drive diversity of perspectives in
annotations.
Moreover, while the motivation behind safety
evaluation tasks is to align language technologies
with human values through a prescriptive approach
(Ouyang et al., 2022; Kenton et al., 2021), the
key role of culture in defining humans, and val-
ues is overlooked in benchmark creation and fine-
tuning efforts. In fact, only a limited set of work in
Machine Learning has investigated cultural differ-
ences in crowdsourcing pipelines for different tasks.
Some examples include Chua et al. (2015), who
investigated how cultural differences between re-
questers and contributors in creative crowdsourcing
tasks influence both whether individuals decide to
contribute as well as how requesters judge success
(Chua et al., 2015), and Joshi et al. (2016), who
studied Indian linguists in a sarcasm annotation
task, finding differences in their ability to detect
sarcasm compared to ground truth datasets pro-
vided by American annotators (Joshi et al., 2016).
Beyond cultural investigations, differences in
annotation behavior have increasingly become a fo-
cus of study in machine learning. With the growth
of sub-fields such as data-centric AI (Ng et al.,
2021; Zha et al., 2023), researchers have put forth
a range of explanations for disagreements in data
annotation (Sandri et al., 2023), such as random
variation as an artifact of human behavior (Krip-
pendorff, 2008), as well as crowd worker and la-
bel schema quality (Aroyo and Welty, 2015; Du-
mitrache, 2015). Disagreements between specific
social groups have also been studied, with schol-
ars finding systematic differences in safety annota-
tions rooted in gender (Cowan and Khatchadourian,
2003), race and sexuality (Goyal et al., 2022), com-
munity membership (Patton et al., 2019), and politi-
cal views (Sap et al., 2022). As a result, researchers
have problematized the notion of a universal gold
standard for offensive or toxic language, and called
for dataset and modeling approaches that preserve
disagreements (Hovy et al., 2013; Davani et al.,
2022; Prabhakaran et al., 2021).
By conducting a cross-cultural experiment on
identifying offensive language, in this paper we
highlight two key factors that impact safety eval-
uations: (1) cross-cultural, and (2) psychological
differences in detecting offensive language. We
conducted a data collection effort with broad geo-
graphic coverage (21 countries from eight cultural
regions), having each item labeled for offensive-
ness by at least three annotators from each region.
Our multi-level analysis of responses provides im-
portant insights into how geo-cultural factors and
individual moral factors influence perceptions of
offense in language:
Geo-Cultural Factors
The results of Study 1 provide strong evidence for
cross regional differences in annotating offensive-
ness in language. Countries associated with Arab
Culture, Latin America, Sub-Saharan Africa, and
Indian Cultural Sphere, were more likely to an-
notate items as offensive compared to the other
four regions, i.e., North America, Western Eu-
rope, Oceania, and Sinosphere; with individuals
from Sinosphere, and specifically China, provid-
ing the least offensive labels. Often referred to as
the Global South, the four regions with higher re-
ports of offensive, have been compared to western
countries in terms of their wide cultural differences.
Considering the WEIRDness of countries (their de-
gree of similarity from the USA culture), while not
having a significant impact on provided labels, is
associated with lower offensiveness labels. In other
words participants from countries which are more
culturally similar to the USA (this includes North
America, Western European Countries, Oceania,
and some countries across other regions such as
Singapore) are less sensitive to offensive content.
We also investigated the impact of the six cul-
tural factors introduced by Hofstede, on countries
responses to offensive content. While cultural ten-
dency for seeking equality on power distribution
(Power-Distance Index) and cultural tendency for
fulfilling one’s desires (Indulgence) did not have
significant association with annotation behaviors,
cultures with a higher tendency to avoid uncertainty

--- Page 8 ---

and ambiguity (Uncertainty Avoidance), more gen-
der role differentiation (Femininity vs. Masculin-
ity), and stronger emphasis on the present than
the future (short-term orientation) are more sensi-
tive to offensive language. These results provide
finer-grained insights into values that may shape
individuals’ tolerance for offensive language that
goes beyond regional groupings.
Moral Factors
We next investigated the mediating impact of moral
concerns on the regional differences in perceiving
offensiveness. We expected individual and cultural
differences in moral values (measured through the
moral foundations questionnaire) to explain the
observed regional and cultural differences. Our re-
sults showed that regions with higher moral values
regarding Caring for others and Purity are more
sensitive to offensive language. Care as a main
definitive foundation discussed in different moral
theories, includes “intuitions about avoiding emo-
tional and physical damage to another individual”
(Atari et al., 2023). Care values have lower vari-
ance across regions compared to the other founda-
tions (Table. 2), with most people scoring high on
this foundation, a high score on Care helps explain
higher offensiveness labels across the regions. On
the other hand, the Purity foundation, with higher
variance across regions, also has a positive associa-
tion with high offensiveness labels. Purity refers to
“intuitions about avoiding bodily and spiritual con-
tamination and degradation” (Atari et al., 2023).
As we demonstrate, determining the offensive-
ness of language is a moral judgment shaped by
cultural factors. However, research on offensive
language detection typically disregards sociode-
mograhic and cultural variations in data annotation.
Moreover, the need to assess the cultural values
and moral norms takes on even more weight in
the context of large language models, which en-
able a scale of language production beyond that
of the human-generated content typically analyzed
in social media contexts. These large language
models rely on fine-tuning processes that involve
human-generated annotations and feedback that are
inherently shaped by cultural and moral views. As
a result, generative models may perform in ways
that differentially align with the norms of different
global populations. Indeed, Santy et al. (2023)
(Santy et al., 2023) analyzed dataset ground truth
labels and model outputs for a social acceptabil-
ity and hate detection task, finding greater align-
ment with annotations provided by Western, White,
college-educated, and younger individuals.
Our findings confirm that disagreements in an-
notating offensiveness, with key applications in
evaluating AI safety, have cultural, and psychologi-
cal roots often disregarded in current efforts. These
findings call for culturally-informed data collec-
tion and model evaluation effort, ensuring that they
reflect the values and norms in the communities
affected by model deployments. It is, therefore, es-
sential to diversify rater pools of data annotator and
model evaluators to incorporate various perspec-
tives of language to enhance modeling processes
responsibly.
Moreover, inclusion of diverse opinions goes be-
yond data collection and expansion of rater pools;
we believe that cultural considerations play a piv-
otal role in defining AI-related harms and devis-
ing more effective safety protocols and paradigms.
Nevertheless, it is crucial to recognize that defining
AI harms according to cultural values can conflict
with social equity for marginalized groups within a
given society. As discussed by (Hershcovich et al.,
2022), our findings supports NLP efforts that si-
multaneously uphold cultural values while actively
mitigating cultural biases. This is only possible
with active community engagement for aligning AI
models with cultural norms, along with relying on
international regulatory efforts to safeguard human
rights of vulnerable individuals within communi-
ties (Prabhakaran et al., 2022).
Lastly, our findings contributes a vital perspec-
tive to ongoing discourse regarding the necessity
for AI models to align with human values. Consid-
ering the diverse values and perspectives present
regions, cultures, and individuals, the critical ques-
tion to ask is whose values should the models align
with. Instead of mainly focusing on demograph-
ics, our findings suggests that aligning AI models
with moral foundations that individuals and groups
are concerned about potentially provides an effec-
tive and efficient approach towards value alignment
efforts for the pluralistic world we live in.
References
Nancy E Adler, Elissa S Epel, Grace Castellazzo,
and Jeannette R Ickovics. 2000.
Relationship of
subjective and objective social status with psycho-
logical and physiological functioning: Preliminary

--- Page 9 ---

data in healthy, white women. Health psychology,
19(6):586.
Lora Aroyo, Mark Diaz, Christopher Homan, Vinodku-
mar Prabhakaran, Alex Taylor, and Ding Wang. 2023.
The reasonable effectiveness of diverse evaluation
data.
Lora Aroyo and Chris Welty. 2015. Truth is a lie: Crowd
truth and the seven myths of human annotation. AI
Magazine, 36(1):15–24.
Mohammad Atari, Jonathan Haidt, Jesse Graham, Sena
Koleva, Sean T Stevens, and Morteza Dehghani.
2023. Morality beyond the weird: How the nomo-
logical network of morality varies across cultures.
Journal of Personality and Social Psychology, 125.
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda
Askell, Anna Chen, Nova DasSarma, Dawn Drain,
Stanislav Fort, Deep Ganguli, Tom Henighan,
Nicholas Joseph, Saurav Kadavath, Jackson Kernion,
Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac
Hatfield-Dodds, Danny Hernandez, Tristan Hume,
Scott Johnston, Shauna Kravec, Liane Lovitt, Neel
Nanda, Catherine Olsson, Dario Amodei, Tom
Brown, Jack Clark, Sam McCandlish, Chris Olah,
Ben Mann, and Jared Kaplan. 2022. Training a help-
ful and harmless assistant with reinforcement learn-
ing from human feedback.
Jack M Balkin. 2017. Digital speech and democratic
culture: A theory of freedom of expression for the
information society. In Law and society approaches
to cyberspace, pages 325–382. Routledge.
Reuben M Baron and David A Kenny. 1986.
The
moderator–mediator variable distinction in social psy-
chological research: Conceptual, strategic, and sta-
tistical considerations. Journal of personality and
social psychology, 51(6):1173.
Valerie C Brannon. 2019. Free speech and the regula-
tion of social media content. Congressional Research
Service, 27.
Roy YJ Chua, Yannig Roth, and Jean-François Lemoine.
2015. The impact of culture on creativity: How cul-
tural tightness and cultural distance affect global inno-
vation crowdsourcing work. Administrative Science
Quarterly, 60(2):189–227.
European Commission. 2020. The digital services act:
Ensuring a safe and accountable online environment.
The Digital Services Act: Ensuring a safe and ac-
countable online environment.
Gloria Cowan and Désirée Khatchadourian. 2003. Em-
pathy, ways of knowing, and interdependence as me-
diators of gender differences in attitudes toward hate
speech and freedom of speech. Psychology of women
quarterly, 27(4):300–308.
Aida Mostafazadeh Davani, Mark Díaz, and Vinodku-
mar Prabhakaran. 2022. Dealing with disagreements:
Looking beyond the majority vote in subjective an-
notations. Transactions of the Association for Com-
putational Linguistics, 10:92–110.
Anca Dumitrache. 2015. Crowdsourcing disagreement
for collecting semantic annotation. In The Seman-
tic Web. Latest Advances and New Domains: 12th
European Semantic Web Conference, ESWC 2015,
Portoroz, Slovenia, May 31–June 4, 2015. Proceed-
ings 12, pages 701–710. Springer.
Antigoni Founta, Constantinos Djouvas, Despoina
Chatzakou, Ilias Leontiadis, Jeremy Blackburn, Gi-
anluca Stringhini, Athena Vakali, Michael Sirivianos,
and Nicolas Kourtellis. 2018. Large scale crowd-
sourcing and characterization of twitter abusive be-
havior. In Proceedings of the international AAAI
conference on web and social media, volume 12.
Tanmay Garg, Sarah Masud, Tharun Suresh, and Tan-
moy Chakraborty. 2023.
Handling bias in toxic
speech detection: A survey. ACM Computing Sur-
veys, 55(13s):1–32.
Mor Geva, Yoav Goldberg, and Jonathan Berant. 2019.
Are we modeling the task or the annotator? an inves-
tigation of annotator bias in natural language under-
standing datasets. In Proceedings of the 2019 Confer-
ence on Empirical Methods in Natural Language Pro-
cessing and the 9th International Joint Conference
on Natural Language Processing (EMNLP-IJCNLP),
pages 1161–1166, Hong Kong, China. Association
for Computational Linguistics.
Amelia Glaese, Nat McAleese, Maja Tr˛ebacz, John
Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh,
Laura Weidinger, Martin Chadwick, Phoebe Thacker,
Lucy Campbell-Gillingham, Jonathan Uesato, Po-
Sen Huang, Ramona Comanescu, Fan Yang, Abigail
See, Sumanth Dathathri, Rory Greig, Charlie Chen,
Doug Fritz, Jaume Sanchez Elias, Richard Green,
Soˇna Mokrá, Nicholas Fernando, Boxi Wu, Rachel
Foley, Susannah Young, Iason Gabriel, William Isaac,
John Mellor, Demis Hassabis, Koray Kavukcuoglu,
Lisa Anne Hendricks, and Geoffrey Irving. 2022.
Improving alignment of dialogue agents via targeted
human judgements.
Nitesh Goyal, Ian D Kivlichan, Rachel Rosen, and Lucy
Vasserman. 2022. Is your toxicity my toxicity? ex-
ploring the impact of rater identity on toxicity annota-
tion. Proceedings of the ACM on Human-Computer
Interaction, 6(CSCW2):1–28.
Jesse Graham, Jonathan Haidt, Sena Koleva, Matt
Motyl, Ravi Iyer, Sean P Wojcik, and Peter H Ditto.
2013. Moral foundations theory: The pragmatic va-
lidity of moral pluralism. In Advances in experi-
mental social psychology, volume 47, pages 55–130.
Elsevier.
Jesse Graham, Jonathan Haidt, and Brian A Nosek.
2009. Liberals and conservatives rely on different
sets of moral foundations. Journal of personality and
social psychology, 96(5):1029.

--- Page 10 ---

Joseph Henrich, Steven J Heine, and Ara Norenzayan.
2010. Beyond weird: Towards a broad-based behav-
ioral science. Behavioral and brain sciences, 33(2-
3):111.
Daniel Hershcovich, Stella Frank, Heather Lent,
Miryam de Lhoneux, Mostafa Abdou, Stephanie
Brandl, Emanuele Bugliarello, Laura Cabello Pi-
queras, Ilias Chalkidis, Ruixiang Cui, Constanza
Fierro, Katerina Margatina, Phillip Rust, and Anders
Søgaard. 2022. Challenges and strategies in cross-
cultural NLP. In Proceedings of the 60th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 6997–7013,
Dublin, Ireland. Association for Computational Lin-
guistics.
Geert Hofstede. 2011. Dimensionalizing cultures: The
hofstede model in context. Online readings in psy-
chology and culture, 2(1):8.
Joe Hoover, Gwenyth Portillo-Wightman, Leigh Yeh,
Shreya Havaldar, Aida Mostafazadeh Davani, Ying
Lin, Brendan Kennedy, Mohammad Atari, Zahra
Kamel, Madelyn Mendlen, et al. 2020. Moral foun-
dations twitter corpus: A collection of 35k tweets
annotated for moral sentiment. Social Psychological
and Personality Science, 11(8):1057–1071.
Dirk Hovy, Taylor Berg-Kirkpatrick, Ashish Vaswani,
and Eduard Hovy. 2013. Learning whom to trust
with mace. In Proceedings of the 2013 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, pages 1120–1130.
Jigsaw. 2018. Toxic comment classification challenge.
Accessed: 2021-05-01.
Jigsaw. 2019. Unintended bias in toxicity classification.
Accessed: 2021-05-01.
Aditya Joshi, Pushpak Bhattacharyya, Mark Carman,
Jaya Saraswati, and Rajita Shukla. 2016. How do
cultural differences impact the quality of sarcasm
annotation?: A case study of indian annotators and
american text. In Proceedings of the 10th SIGHUM
Workshop on Language Technology for Cultural Her-
itage, Social Sciences, and Humanities, pages 95–99.
Zachary Kenton, Tom Everitt, Laura Weidinger, Ia-
son Gabriel, Vladimir Mikulik, and Geoffrey Irving.
2021. Alignment of language agents.
Svetlana Kiritchenko, Isar Nejadgholi, and Kathleen C
Fraser. 2021. Confronting abusive language online:
A survey from the ethical and human rights per-
spective. Journal of Artificial Intelligence Research,
71:431–478.
Klaus Krippendorff. 2008. Systematic and random dis-
agreement and the reliability of nominal data. Com-
munication Methods and Measures, 2(4):323–338.
MultiMedia LLC. 2023.
FACT SHEET: President
Biden Issues Executive Order on Safe, Secure, and
Trustworthy Artificial Intelligence.
Michael Muthukrishna, Adrian V Bell, Joseph Henrich,
Cameron M Curtin, Alexander Gedranovich, Jason
McInerney, and Braden Thue. 2020. Beyond western,
educated, industrial, rich, and democratic (weird) psy-
chology: Measuring and mapping scales of cultural
and psychological distance. Psychological science,
31(6):678–701.
A Ng, D Laird, and L He. 2021. Data-centric AI com-
petition. deeplearning AI.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback.
Advances in Neural
Information Processing Systems, 35:27730–27744.
Desmond Patton, Philipp Blandfort, William Frey,
Michael Gaskell, and Svebor Karaman. 2019. Anno-
tating social media data from vulnerable populations:
Evaluating disagreement between domain experts
and graduate student annotators. In proceedings of
the 52nd Hawaii International Conference on System
Sciences.
Vinodkumar Prabhakaran, Margaret Mitchell, Timnit
Gebru, and Iason Gabriel. 2022. A human rights-
based approach to responsible ai. arXiv preprint
arXiv:2210.02667.
Vinodkumar Prabhakaran, Aida Mostafazadeh Davani,
and Mark Diaz. 2021. On releasing annotator-level
labels and information in datasets. In Proceedings
of The Joint 15th Linguistic Annotation Workshop
(LAW) and 3rd Designing Meaning Representations
(DMR) Workshop, pages 133–138, Punta Cana, Do-
minican Republic. Association for Computational
Linguistics.
Joni Salminen, Hind Almerekhi, Ahmed Mohamed
Kamel, Soon-gyo Jung, and Bernard J Jansen. 2019.
Online hate ratings vary by extremes: A statistical
analysis. In Proceedings of the 2019 Conference on
Human Information Interaction and Retrieval, pages
213–217.
Joni Salminen, Fabio Veronesi, Hind Almerekhi, Soon-
Gvo Jung, and Bernard J Jansen. 2018. Online hate
interpretation varies by country, but more by individ-
ual: A statistical analysis using crowdsourced ratings.
In 2018 fifth international conference on social net-
works analysis, management and security (snams),
pages 88–94. IEEE.
Marta Sandri, Elisa Leonardelli, Sara Tonelli, and Elis-
abetta Ježek. 2023.
Why don’t you do it right?
analysing annotators’ disagreement in subjective
tasks. In Proceedings of the 17th Conference of the
European Chapter of the Association for Computa-
tional Linguistics, pages 2420–2433.
Sebastin Santy, Jenny Liang, Ronan Le Bras, Katharina
Reinecke, and Maarten Sap. 2023. NLPositionality:
Characterizing design biases of datasets and models.

--- Page 11 ---

In Proceedings of the 61st Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 9080–9102, Toronto, Canada.
Association for Computational Linguistics.
Maarten Sap, Swabha Swayamdipta, Laura Vianna,
Xuhui Zhou, Yejin Choi, and Noah A. Smith. 2022.
Annotators with attitudes: How annotator beliefs
and identities bias toxic language detection. In Pro-
ceedings of the 2022 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies, pages
5884–5906, Seattle, United States. Association for
Computational Linguistics.
Anna Schmidt and Michael Wiegand. 2017. A survey
on hate speech detection using natural language pro-
cessing. In Proceedings of the fifth international
workshop on natural language processing for social
media, pages 1–10.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao,
Abu Awal Md Shoeb, Abubakar Abid, Adam
Fisch, Adam R. Brown, Adam Santoro, Aditya
Gupta, Adrià Garriga-Alonso, Agnieszka Kluska,
Aitor Lewkowycz, Akshat Agarwal, Alethea Power,
Alex Ray, Alex Warstadt, Alexander W. Kocurek,
Ali Safaya, Ali Tazarv, Alice Xiang, Alicia Par-
rish, Allen Nie, Aman Hussain, Amanda Askell,
Amanda Dsouza, Ambrose Slone, Ameet Rahane,
Anantharaman S. Iyer, Anders Andreassen, Andrea
Madotto, Andrea Santilli, Andreas Stuhlmüller, An-
drew Dai, Andrew La, Andrew Lampinen, Andy
Zou, Angela Jiang, Angelica Chen, Anh Vuong,
Animesh Gupta, Anna Gottardi, Antonio Norelli,
Anu Venkatesh, Arash Gholamidavoodi, Arfa Tabas-
sum, Arul Menezes, Arun Kirubarajan, Asher Mul-
lokandov, Ashish Sabharwal, Austin Herrick, Avia
Efrat, Aykut Erdem, Ayla Karaka¸s, B. Ryan Roberts,
Bao Sheng Loe, Barret Zoph, Bartłomiej Bojanowski,
Batuhan Özyurt, Behnam Hedayatnia, Behnam
Neyshabur, Benjamin Inden, Benno Stein, Berk
Ekmekci, Bill Yuchen Lin, Blake Howald, Bryan
Orinion, Cameron Diao, Cameron Dour, Cather-
ine Stinson, Cedrick Argueta, César Ferri Ramírez,
Chandan Singh, Charles Rathkopf, Chenlin Meng,
Chitta Baral, Chiyu Wu, Chris Callison-Burch, Chris
Waites, Christian Voigt, Christopher D. Manning,
Christopher Potts, Cindy Ramirez, Clara E. Rivera,
Clemencia Siro, Colin Raffel, Courtney Ashcraft,
Cristina Garbacea, Damien Sileo, Dan Garrette, Dan
Hendrycks, Dan Kilman, Dan Roth, Daniel Free-
man, Daniel Khashabi, Daniel Levy, Daniel Moseguí
González, Danielle Perszyk, Danny Hernandez,
Danqi Chen, Daphne Ippolito, Dar Gilboa, David Do-
han, David Drakard, David Jurgens, Debajyoti Datta,
Deep Ganguli, Denis Emelin, Denis Kleyko, Deniz
Yuret, Derek Chen, Derek Tam, Dieuwke Hupkes,
Diganta Misra, Dilyar Buzan, Dimitri Coelho Mollo,
Diyi Yang, Dong-Ho Lee, Dylan Schrader, Ekaterina
Shutova, Ekin Dogus Cubuk, Elad Segal, Eleanor
Hagerman, Elizabeth Barnes, Elizabeth Donoway, El-
lie Pavlick, Emanuele Rodola, Emma Lam, Eric Chu,
Eric Tang, Erkut Erdem, Ernie Chang, Ethan A. Chi,
Ethan Dyer, Ethan Jerzak, Ethan Kim, Eunice En-
gefu Manyasi, Evgenii Zheltonozhskii, Fanyue Xia,
Fatemeh Siar, Fernando Martínez-Plumed, Francesca
Happé, Francois Chollet, Frieda Rong, Gaurav
Mishra, Genta Indra Winata, Gerard de Melo, Ger-
mán Kruszewski, Giambattista Parascandolo, Gior-
gio Mariani, Gloria Wang, Gonzalo Jaimovitch-
López, Gregor Betz, Guy Gur-Ari, Hana Galijase-
vic, Hannah Kim, Hannah Rashkin, Hannaneh Ha-
jishirzi, Harsh Mehta, Hayden Bogar, Henry Shevlin,
Hinrich Schütze, Hiromu Yakura, Hongming Zhang,
Hugh Mee Wong, Ian Ng, Isaac Noble, Jaap Jumelet,
Jack Geissinger, Jackson Kernion, Jacob Hilton, Jae-
hoon Lee, Jaime Fernández Fisac, James B. Simon,
James Koppel, James Zheng, James Zou, Jan Koco´n,
Jana Thompson, Janelle Wingfield, Jared Kaplan,
Jarema Radom, Jascha Sohl-Dickstein, Jason Phang,
Jason Wei, Jason Yosinski, Jekaterina Novikova,
Jelle Bosscher, Jennifer Marsh, Jeremy Kim, Jeroen
Taal, Jesse Engel, Jesujoba Alabi, Jiacheng Xu, Ji-
aming Song, Jillian Tang, Joan Waweru, John Bur-
den, John Miller, John U. Balis, Jonathan Batchelder,
Jonathan Berant, Jörg Frohberg, Jos Rozen, Jose
Hernandez-Orallo, Joseph Boudeman, Joseph Guerr,
Joseph Jones, Joshua B. Tenenbaum, Joshua S. Rule,
Joyce Chua, Kamil Kanclerz, Karen Livescu, Karl
Krauth, Karthik Gopalakrishnan, Katerina Ignatyeva,
Katja Markert, Kaustubh D. Dhole, Kevin Gim-
pel, Kevin Omondi, Kory Mathewson, Kristen Chi-
afullo, Ksenia Shkaruta, Kumar Shridhar, Kyle Mc-
Donell, Kyle Richardson, Laria Reynolds, Leo Gao,
Li Zhang, Liam Dugan, Lianhui Qin, Lidia Contreras-
Ochando, Louis-Philippe Morency, Luca Moschella,
Lucas Lam, Lucy Noble, Ludwig Schmidt, Luheng
He, Luis Oliveros Colón, Luke Metz, Lütfi Kerem
¸Senel, Maarten Bosma, Maarten Sap, Maartje ter
Hoeve, Maheen Farooqi, Manaal Faruqui, Mantas
Mazeika, Marco Baturan, Marco Marelli, Marco
Maru, Maria Jose Ramírez Quintana, Marie Tolkiehn,
Mario Giulianelli, Martha Lewis, Martin Potthast,
Matthew L. Leavitt, Matthias Hagen, Mátyás Schu-
bert, Medina Orduna Baitemirova, Melody Arnaud,
Melvin McElrath, Michael A. Yee, Michael Co-
hen, Michael Gu, Michael Ivanitskiy, Michael Star-
ritt, Michael Strube, Michał Sw˛edrowski, Michele
Bevilacqua, Michihiro Yasunaga, Mihir Kale, Mike
Cain, Mimee Xu, Mirac Suzgun, Mitch Walker,
Mo Tiwari, Mohit Bansal, Moin Aminnaseri, Mor
Geva, Mozhdeh Gheini, Mukund Varma T, Nanyun
Peng, Nathan A. Chi, Nayeon Lee, Neta Gur-Ari
Krakover, Nicholas Cameron, Nicholas Roberts,
Nick Doiron, Nicole Martinez, Nikita Nangia, Niklas
Deckers, Niklas Muennighoff, Nitish Shirish Keskar,
Niveditha S. Iyer, Noah Constant, Noah Fiedel, Nuan
Wen, Oliver Zhang, Omar Agha, Omar Elbaghdadi,
Omer Levy, Owain Evans, Pablo Antonio Moreno
Casares, Parth Doshi, Pascale Fung, Paul Pu Liang,
Paul Vicol, Pegah Alipoormolabashi, Peiyuan Liao,
Percy Liang, Peter Chang, Peter Eckersley, Phu Mon
Htut, Pinyu Hwang, Piotr Miłkowski, Piyush Patil,
Pouya Pezeshkpour, Priti Oli, Qiaozhu Mei, Qing
Lyu, Qinlang Chen, Rabin Banjade, Rachel Etta
Rudolph, Raefer Gabriel, Rahel Habacker, Ramon

--- Page 12 ---

Risco, Raphaël Millière, Rhythm Garg, Richard
Barnes, Rif A. Saurous, Riku Arakawa, Robbe
Raymaekers, Robert Frank, Rohan Sikand, Roman
Novak, Roman Sitelew, Ronan LeBras, Rosanne
Liu, Rowan Jacobs, Rui Zhang, Ruslan Salakhut-
dinov, Ryan Chi, Ryan Lee, Ryan Stovall, Ryan
Teehan, Rylan Yang, Sahib Singh, Saif M. Moham-
mad, Sajant Anand, Sam Dillavou, Sam Shleifer,
Sam Wiseman, Samuel Gruetter, Samuel R. Bow-
man, Samuel S. Schoenholz, Sanghyun Han, San-
jeev Kwatra, Sarah A. Rous, Sarik Ghazarian, Sayan
Ghosh, Sean Casey, Sebastian Bischoff, Sebastian
Gehrmann, Sebastian Schuster, Sepideh Sadeghi,
Shadi Hamdan, Sharon Zhou, Shashank Srivastava,
Sherry Shi, Shikhar Singh, Shima Asaadi, Shixi-
ang Shane Gu, Shubh Pachchigar, Shubham Tosh-
niwal, Shyam Upadhyay, Shyamolima, Debnath,
Siamak Shakeri, Simon Thormeyer, Simone Melzi,
Siva Reddy, Sneha Priscilla Makini, Soo-Hwan Lee,
Spencer Torene, Sriharsha Hatwar, Stanislas De-
haene, Stefan Divic, Stefano Ermon, Stella Bider-
man, Stephanie Lin, Stephen Prasad, Steven T. Pi-
antadosi, Stuart M. Shieber, Summer Misherghi, Svet-
lana Kiritchenko, Swaroop Mishra, Tal Linzen, Tal
Schuster, Tao Li, Tao Yu, Tariq Ali, Tatsu Hashimoto,
Te-Lin Wu, Théo Desbordes, Theodore Rothschild,
Thomas Phan, Tianle Wang, Tiberius Nkinyili, Timo
Schick, Timofei Kornev, Titus Tunduny, Tobias Ger-
stenberg, Trenton Chang, Trishala Neeraj, Tushar
Khot, Tyler Shultz, Uri Shaham, Vedant Misra, Vera
Demberg, Victoria Nyamai, Vikas Raunak, Vinay
Ramasesh, Vinay Uday Prabhu, Vishakh Padmaku-
mar, Vivek Srikumar, William Fedus, William Saun-
ders, William Zhang, Wout Vossen, Xiang Ren, Xi-
aoyu Tong, Xinran Zhao, Xinyi Wu, Xudong Shen,
Yadollah Yaghoobzadeh, Yair Lakretz, Yangqiu Song,
Yasaman Bahri, Yejin Choi, Yichi Yang, Yiding
Hao, Yifu Chen, Yonatan Belinkov, Yu Hou, Yufang
Hou, Yuntao Bai, Zachary Seid, Zhuoye Zhao, Zi-
jian Wang, Zijie J. Wang, Zirui Wang, and Ziyi Wu.
2023. Beyond the imitation game: Quantifying and
extrapolating the capabilities of language models.
Alexandra N Uma, Tommaso Fornaciari, Dirk Hovy, Sil-
viu Paun, Barbara Plank, and Massimo Poesio. 2021.
Learning from disagreement: A survey. Journal of
Artificial Intelligence Research, 72:1385–1470.
Boxin Wang, Chejian Xu, Shuohang Wang, Zhe Gan,
Yu Cheng, Jianfeng Gao, Ahmed Hassan Awadal-
lah, and Bo Li. 2022. Adversarial glue: A multi-
task benchmark for robustness evaluation of language
models.
Zeerak Waseem. 2016. Are you a racist or am i seeing
things? annotator influence on hate speech detection
on twitter. In Proceedings of the first workshop on
NLP and computational social science, pages 138–
142.
Ellery Wulczyn, Nithum Thain, and Lucas Dixon. 2017.
Ex machina: Personal attacks seen at scale. In Pro-
ceedings of the 26th international conference on
world wide web, pages 1391–1399.
Daochen Zha, Zaid Pervaiz Bhat, Kwei-Herng Lai,
Fan Yang, and Xia Hu. 2023. Data-centric ai: Per-
spectives and challenges.
In Proceedings of the
2023 SIAM International Conference on Data Mining
(SDM), pages 945–948. SIAM.
A
Appendix
Participants
Our data collection process aimed
to recruit a balanced set of annotators from eight
geo-cultural regions, namely, Northern America,
Latin America, Arab Cultures, Sinosphere, Ocea-
nia, Sub Saharan Africa, Indian Cultural Sphere,
and Western Europe.10
We recruited at least
450 participants from each region (Nparticipants
= 4309), represented by 2-4 countries, with at
least 100 participants per country, except for South
Korea and Qatar where we managed to recruit
only a smaller number of raters. See Table 1 for
country-level statistics. While typical raters re-
cruited through a dedicated annotation platform
or service possess specialized training or experi-
ence that may influence how they complete tasks,
most platforms feature a relatively limited degree
of cultural representation within their pools. As a
result, they are less appropriate for specifically and
robustly evaluating cultural differences and their
relationship to annotation judgments.
Annotation
Each participant was assigned to an-
notate offensiveness of 40 textual items with a
value between 0 (not offensive at all) and 5 (ex-
tremely offensive). We asked participants to decide
whether they perceived them as offensive, noting
that “whether something is offensive or not may
depend on the context in which this message is ex-
changed, which we are not providing you in these
questions. Please make the best assessment based
on the information/context you have from the pro-
vided text.” Moreover, half of the participants were
provided with a note that defined extremely offen-
sive language as “profanity, strongly impolite, rude
or vulgar language expressed with fighting or hurt-
ful words in order to insult a targeted individual
or group.” Other participants were expected to
label items based on their own definition of offen-
siveness. Participants’ common understanding of
offensiveness was tested by 5 (non-offensive) con-
trolled questions randomly distributed among the
40-items annotation process. Participants with at
least one wrong answer were excluded.
10Our efforts for collecting data from Eastern Europe halted
because of the Russia’s war in Ukraine.

--- Page 13 ---

Gender
Age
Region
Country
#
Man
Woman
NB
PNS
18 – 30
30 – 50
50+
Arab Culture
Egypt
225
61.80%
36.40%
0.40%
1.30%
55.60%
20.90%
23.60%
Qatar
57
64.90%
33.30%
0.00%
1.80%
63.20%
31.60%
5.30%
UAE
234
55.60%
44.40%
0.00%
0.00%
46.20%
44.00%
9.80%
Indian Cultural
Sphere
India
444
57.00%
43.00%
0.00%
0.00%
46.60%
34.20%
19.10%
Singapore
110
50.00%
49.10%
0.90%
0.00%
27.30%
41.80%
30.90%
Latin
America
Argentina
149
50.30%
47.70%
2.00%
0.00%
52.30%
34.90%
12.80%
Brazil
237
47.30%
52.70%
0.00%
0.00%
57.40%
27.00%
15.60%
Mexico
163
51.50%
48.50%
0.00%
0.00%
54.00%
36.80%
9.20%
North
America
Canada
378
37.60%
61.90%
0.50%
0.00%
41.00%
36.80%
22.20%
USA
173
45.10%
52.60%
1.20%
1.20%
62.40%
20.80%
16.80%
Oceania
Australia
184
39.70%
58.70%
1.60%
0.00%
25.50%
50.00%
24.50%
New Zealand
333
39.00%
59.80%
1.20%
0.00%
34.20%
38.70%
27.00%
Sinosphere
China
176
37.50%
62.50%
0.00%
0.00%
14.20%
66.50%
19.30%
Japan
100
70.00%
30.00%
0.00%
0.00%
13.00%
38.00%
49.00%
South Korea
43
58.10%
41.90%
0.00%
0.00%
27.90%
48.80%
23.30%
Vietnam
221
53.80%
41.20%
5.00%
0.00%
71.50%
23.50%
5.00%
Sub-Saharan
Africa
Ghana
164
67.10%
32.90%
0.00%
0.00%
74.40%
22.00%
3.70%
Nigeria
366
54.40%
45.10%
0.30%
0.30%
54.10%
33.10%
12.80%
Western
Europe
Germany
109
52.30%
46.80%
0.90%
0.00%
51.40%
24.80%
23.90%
Netherlands
138
52.20%
45.70%
2.20%
0.00%
61.60%
21.00%
17.40%
United King-
dom
305
40.30%
59.00%
0.70%
0.00%
38.70%
38.00%
23.30%
Table 1: Socio-demographic distribution of participants in our study in different regions and countries. (PNS =
Prefer not to say, and NB = Non-binary)
Stimuli
Textual items were selected from Jig-
saw’s Toxic Comments Classification dataset (Jig-
saw, 2018), and the Unintended Bias in Toxicity
Classification dataset (Jigsaw, 2019). We set our
data collection goal to increase the chance of evok-
ing disagreements, and involving different moral
judgments in annotations. To address the former,
we randomly selected items from Jigsaw’s Toxic
Comments Classification dataset, prioritizing those
with high disagreement levels. To measure dis-
agreements on each item, we averaged annotators’
toxicity scores ranging from 0 (lowest toxicity) to
1 (highest toxicity). We chose items with a normal
distribution centered around a toxicity score of 0.5
(indicating highest disagreement) with a standard
deviation of 0.2. To select items that would po-
tentially evoke moral reasoning we collected items
from Jigsaw’s Unintended Bias in Toxicity Classifi-
cation dataset with moral sentiment, labeled by on
a supervised moral foundation tagger trained on the
Moral Foundations Twitter Corpus (Hoover et al.,
2020). We also collected a third set of items each
mentioning at least one social group (this informa-
tion is provided in the Jigsaw’s raw data), to assess
annotation of language that is potentially offensive
toward different social groups.
Regions and Countries
Our selected list of geo-
cultural regions and countries within regions is not
meant to be exhaustive, rather just to make sure
that our study is done on a set of countries with
diverse cultural histories. Each region listed has
countries and sub-regions that have distinct cul-
tural practices, and it is wrong to assume that the
country we choose would comprehensively repre-
sent that region. Similarly, the countries listed are
meant as likely places to collect data from, based
on familiarity with previous data collection efforts,
which potentially reflect the power structures ex-
isting within those regions. Also, each country is
rarely a monolith in terms of culture (e.g., India has
diverse subcultures, Australia being characterized
as a “Western” culture erases the vibrant Australian
Aboriginal culture). Data collected would also re-
flect the local disparities in who tends to be in the
social strata that maximally overlaps with the data-
collection workforce in those respective regions,
and what subcultures they represent.
Moral Foundation Questionnaire-2
After an-
notating items, participants were asked to fill out

--- Page 14 ---

Foundation
F(7,
4287)
Care
34.48*
Equality
13.37*
Propor.
51.24*
Authority
102.25*
Loyalty
158.30*
Purity
203.55*
Table 2: Distribution of the moral foundations scores
and the results of one-way ANOVA analysis conducted
for each moral foundation across regions. *means the
p-value of the analysis is lower than .001
the Moral Foundation Questionnaire (Atari et al.,
2023), which includes 36 statements, each concern-
ing one moral value by extending the the moral
foundation theory (Graham et al., 2009) (i.e., Care,
Equality, Proportionality, Loyalty, Authority, and
Purity). Participants’ concerns regarding each item
were captured on a 5-point Likert scale, and items
where aggregated to calculate 6 moral scores for
each participant.
Test Items
We used participants’ response to 5
test items to evaluate their understanding of offen-
siveness. These items (listed below) were unani-
mously labeled as not offensive at all by authors
and were used as an attention check to remove
participants who annotated them otherwise.
• Could you explain your point in a little more
detail please.
• The NY Times yesterday had a rebuttal by the
Iranian UN ambassador.
• Ditto to everything said here.
• Just looked at the link. Impressive and missed
opportunity.
• Don’t be so hard on yourself. Your life will
go on.
Data Cleaning
We selected thresholds for the
amount of time needed to finish the survey and
removed annotators who performed the task either
quicker or slower than the expectation. Annotators
with similar answers to all items were also removed
from the data.
Mediation
We perform the mediation analysis
on the annotator level by aggregating annotation
labels provided from each annotator. While anno-
tators labeled different parts of the dataset (each
annotating 35 out of the 5k items) equal number
of annotators from each region were assigned to
label the same set. In other words for each set of
35 items, there are 3 annotators from each region
that labeled the whole set.

```
