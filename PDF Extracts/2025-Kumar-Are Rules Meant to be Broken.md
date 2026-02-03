---
title: "Are Rules Meant to be Broken - PDF Extract"
source_pdf: "2025-Kumar-Are Rules Meant to be Broken.pdf"
pages: 21
extracted_at: "2026-01-24T16:38:29.658152"
---

# PDF Extract: Are Rules Meant to be Broken

**Source PDF:** 2025-Kumar-Are Rules Meant to be Broken.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

Are Rules Meant to be Broken? Understanding Multilingual Moral
Reasoning as a Computational Pipeline with UNIMORAL
Shivani Kumar
University of Michigan
kshivan@umich.edu
David Jurgens
University of Michigan
jurgens@umich.edu
Abstract
Moral reasoning is a complex cognitive pro-
cess shaped by individual experiences and cul-
tural contexts and presents unique challenges
for computational analysis. While natural lan-
guage processing (NLP) offers promising tools
for studying this phenomenon, current research
lacks cohesion, employing discordant datasets
and tasks that examine isolated aspects of
moral reasoning. We bridge this gap with UNI-
MORAL, a unified dataset integrating psycho-
logically grounded and social-media-derived
moral dilemmas annotated with labels for ac-
tion choices, ethical principles, contributing
factors, and consequences, alongside annota-
tors’ moral and cultural profiles. Recognizing
the cultural relativity of moral reasoning, UNI-
MORAL spans six languages, Arabic, Chinese,
English, Hindi, Russian, and Spanish, captur-
ing diverse socio-cultural contexts. We demon-
strate UNIMORAL’s utility through a bench-
mark evaluations of three large language mod-
els (LLMs) across four tasks: action prediction,
moral typology classification, factor attribution
analysis, and consequence generation. Key
findings reveal that while implicitly embedded
moral contexts enhance the moral reasoning ca-
pability of LLMs, there remains a critical need
for increasingly specialized approaches to fur-
ther advance moral reasoning in these models.
1
Introduction
Computational reasoning systems excel at process-
ing structured domains like mathematics (Imani
et al., 2023) and commonsense problem-solving
(Sap et al., 2020) through logical and probabilis-
tic frameworks (Yu et al., 2024). Moral reason-
ing, however, introduces multidimensional com-
plexity by requiring the integration of emotional
intelligence (Zangari et al., 2025) and ethical prin-
ciples such as fairness (Schramowski et al., 2019),
harm mitigation (Graham et al., 2018), and duty
(Ellemers et al., 2019). Consider the canonical
SCENARIO
Moral action? Yes!
(As compared to
keeping the wallet)
Donate
money
to
charity
Return
wallet
to
owner
You return the
wallet
CONSEQUENCE
Judge
Driven by honesty
and empathy
Moralsphere
ACTION
Positive outcome;
person deemed
honest
Assess
You
found a
wallet
Owner
gets the
wallet
Decide
Figure 1: Moral Reasoning pipeline: An individual en-
counters a moral scenario, they list out the potential
actions they can take, and select one. The chosen ac-
tion yields outcomes affecting stakeholders and societal
norms. The “Moralsphere” conceptualizes this dynamic
interplay between reasoning, action, and societal impact
in resolving moral dilemmas.
dilemma of discovering a lost wallet (Figure 1):
Human moral cognition synthesizes perceptual in-
puts (Haidt, 2001), value-based judgments (Greene,
2007), and post-hoc rationalizations (Nabavi, 2012)
into actionable decisions (Walker, 1989). While
this integrated pipeline reflects natural human
reasoning (Kohlberg, 1963), existing NLP ap-
proaches analyze moral decision-making through
fragmented methodologies (Hendrycks et al., 2021;
Vida et al., 2023), limiting both holistic understand-
ing and cross-cultural applicability.
In this work, we bridge this gap by introduc-
ing UNIMORAL, a multilingual dataset designed
to capture the phased nature of moral reasoning.
Grounded in psychological theories and enriched
by real-world social media discourse, UNIMORAL
provides annotations across the entire moral reason-
ing process, covering scenario perception, action
selection, ethical judgment, justification through
contributing factors, and the consequences of the
chosen action. Broadly, to construct UNIMORAL,
we present crowd-sourced participants with moral
scenarios where participants select preferred ac-
tions, justify decisions via follow-up questions, and
complete post-annotation moral (Atari et al., 2023)
arXiv:2502.14083v1  [cs.CL]  19 Feb 2025

--- Page 2 ---

and cultural value questionnaires (Hofstede, 1994).
Recognizing the cultural relativity of morality
(Kennedy et al., 2021; Yang et al., 2024), UNI-
MORAL encompasses six linguistically distinct
contexts, Arabic, Chinese, English, Hindi, Russian,
and Spanish, enabling researchers to probe how
moral frameworks vary across populations. While
UNIMORAL supports diverse applications, in this
study we focus on four pivotal research questions
to analyze how current LLMs handle moral rea-
soning: [I] Action Prediction (AP): How does
contextual cues, like cultural orientation and in-
dividual’s moral values influence computational
models’ capability for action prediction in UNI-
MORAL, and to what extent do these predictions
generalize across its six languages? [II] Moral
Typology Classification (MTC): Can computa-
tional models classify moral actions in UNIMORAL
into psychologically grounded categories (e.g., de-
ontological and virtuous) using its hierarchical an-
notations, and how do these categorizations vary
across languages?
[III] Factor
Attribution
Analysis (FAA): To what extent can a model de-
termine the contributing factors dominating a per-
son’s moral decision making, and how do these fac-
tors interact across languages? [IV] Consequence
Generation (CG): Are computational models capa-
ble of generating coherent consequences of scenar-
io-action pairs in UNIMORAL?
Although the AP and CG can be addressed using
existing datasets for individual languages, UNI-
MORAL facilitates cross-linguistic comparison and
extends its utility to addressing additional inquiries
as posed by the MTC and FAA. Through systematic
benchmarking, we demonstrate UNIMORAL’s util-
ity in addressing these questions, revealing nuanced
patterns in how cultural narratives and personal val-
ues shape moral evaluations. In a nutshell, the
contributions of this work can be summarized as:
1. We identify the different stages of moral rea-
soning and present a systematic, holistic, and
psychologically-motivated pipeline for struc-
tured computational modeling.
2. We present UNIMORAL1, a diverse, multilin-
gual, and holistic dataset of moral dilemmas
derived from psychological theories and so-
cial media, with rich annotations spanning all
phases of moral reasoning (perception, judg-
ment, justification, action, and consequence)
1https://huggingface.co/datasets/shivaniku/
UniMoral
and individualized moral and cultural profiles
derived from participant responses.
3. Through four targeted research questions2, fa-
cilitated by UNIMORAL, we analyze current
LLMs and examine the influence of cultural
narratives and personal ethical values on shap-
ing their moral reasoning.
2
Morality in NLP
Ethics, in NLP, has garnered significant traction
in recent years, with many contemporary studies
investigating the notion of morality in hypothetical
texts, such as stories (Emelin et al., 2021; Guan
et al., 2022), and social media texts, like Reddit
posts (Trager et al., 2022) and tweets (Hoover et al.,
2020). The tasks coming under the umbrella of
“morality in NLP" generally falls under two cate-
gories: quantification and judgment.
Moral quantification.
This subdomain of tasks
typically addresses scenarios where the action of an
individual is known, and the computational system
is tasked with identifying specific aspects of the
action or the individual performing it. For instance,
tasks such as moral value identification (Teern-
stra et al., 2016; Mokhberian et al., 2020; Lan and
Paraboni, 2022; Pavan et al., 2023), moral stance
detection (Santos and Paraboni, 2019; Roy and
Goldwasser, 2021; Botzer et al., 2022), and moral
sentiment classification (Mooijman et al., 2018;
Kobbe et al., 2020; Roy et al., 2021; Qian et al.,
2021) fall into this category. The methodologies
employed to tackle such tasks frequently involve
the use of lexicons (Anderson et al., 2006; Garten
et al., 2016; Alfano et al., 2018), machine learn-
ing approaches (Asprino et al., 2022; Hsu et al.,
2021), and, more recently, large language models
(Alhassan et al., 2022; Alshomary et al., 2022).
Moral judgment.
The tasks in this category in-
volve making judgment about either the action
taken by an individual (Ammanabrolu et al., 2022;
Shen et al., 2022; Yamamoto and Hagiwara, 2014),
the consequence of those actions (Komuda et al.,
2013; Emelin et al., 2021), or the individuals them-
selves (Hendrycks et al., 2020; Lourie et al., 2021).
Action judgment tasks are often presented in two
formats: choosing the moral action from a set
of alternatives (Emelin et al., 2021; Guan et al.,
2022), or evaluating whether a completed action
was moral (Jin et al., 2022; Hendrycks et al., 2020).
2https://github.com/shivanik96/UniMoral.git

--- Page 3 ---

However, many existing studies overlook the criti-
cal aspect of moral evaluation: assuming only one
action is moral and ignoring the decision-maker’s
context. In UNIMORAL, we focus on this per-
sonalization aspect, ensuring that moral reasoning
considers both actions and contextual factors.
Morality across languages and cultures.
Con-
tributions, like Moral Foundations Theory (Graham
et al., 2018) and its extensions (Hopp et al., 2020)
offer lexicons for analyzing moral sentiment but
frequently prioritize Western-centric frameworks.
Cross-cultural adaptations, such as the Japanese
MFD (Matsuo et al., 2019), and multilingual re-
sources like MoralConvIta (Stranisci et al., 2021),
alongside studies of cultural variations in moral pri-
orities (Atari et al., 2023) highlight the importance
of linguistic and cultural diversity, paving the way
for more inclusive approaches.
The moral reasoning pipeline.
Just as a mathe-
matical problem is solved by following a step-by-
step approach (Imani et al., 2023), moral reasoning
involves sequential steps to arrive at an appropriate
action for a scenario. While numerous psychologi-
cal studies discuss the phases of moral reasoning
(Kohlberg, 1963; Carpendale, 2009; Haidt, 2001;
Greene, 2007; Nabavi, 2012), no work in NLP, to
the best of our knowledge, has translated these psy-
chological concepts into a computational format to
explore moral reasoning as a systematic sequence.
To this end, we construct a pipeline, as shown in
Figure 1, that captures the various stages of moral
reasoning. According to Rest’s four-component
model (Narvaez and Rest, 1995) and Haidt’s So-
cial Intuitionist Model (Haidt, 2001), the pipeline
begins with scenario assessment. Subsequently,
possible actions are contemplated, with each influ-
enced by various factors, akin to the Dual-Process
Theory of Moral Judgment (Greene, 2007). After
identifying possible actions, a decision is made.
Similar to real-life situations, every action has con-
sequences; in moral reasoning, these consequences
can be judged as moral or immoral, providing a
learning opportunity as outlined in Bandura’s so-
cial learning theory (Nabavi, 2012).
Throughout these stages, we also examine as-
pects of each phase, such as moral values and
sentiments. We refer to this overarching process
as the “Moralsphere" since it spans all phases of
moral reasoning. These processes within the moral
pipeline collectively function and interact to en-
able informed moral decision-making. To support
the computational study of this pipeline, we intro-
duce UNIMORAL, which provides comprehensive
annotations for all the phases of moral reasoning.
3
Constructing UNIMORAL
This section outlines the data collection, annotation
framework, and analysis of UNIMORAL.
3.1
Collecting Data for Annotation
Broadly, the data construction pipeline encom-
passes the following five steps: 1) generating sce-
narios rooted in psychological theories, 2) deter-
mining the most probable action options within
these scenarios, 3) gathering moral dilemmas from
Reddit along with their corresponding action op-
tions, 4) translating the collected data into target
languages for study, and 5) obtaining annotations
through crowd-sourcing. We provide an in-depth
discussion of each of these steps below.
Psychologically grounded scenarios and their
actions
Numerous psychology studies have ex-
amined human morality by presenting participants
with morally charged dilemmas and inquiring about
their actions (Colby et al., 1983; Rest, 1979; Lind,
2008). These studies curate scenarios to ensure
decisions require moral reasoning rather than mere
logic. We focus on three prominent theories: the
Moral Judgment Interview (MJI) (Colby et al.,
1983), the Defining Issues Test (DIT) (Rest, 1979),
and the Moral Competence Test (MCT) (Lind,
2008). Together, these theories provide 18 psycho-
logical scenarios—seven from both MJI and DIT,
and four from MCT—designed to trigger moral rea-
soning. After reviewing them, we identified two as
repetitive, resulting in 16 unique dilemmas or our
“seed scenarios" (S). More details on these theories
and scenarios are present in Appendix A.1.
Additionally, we draw upon established psycho-
logical theories that identify the elements affect-
ing human decision-making (Graham et al., 2013;
Damasio, 1996; Lessnoff, 1971; Hofstede, 1994)
and summarize nine major contributing factors as
C = {‘Emotions’, ‘Moral’, ‘Culture’, ‘Responsi-
bilities’, ‘Relationships’, ‘Legality’, ‘Rules’, ‘Po-
liteness’, ‘Sacred values’}. To generate new scenar-
ios that emulate the seed scenarios, we use Llama-
3.1-70B Instruct (Meta, 2024), prompting it to cre-
ate scenarios similar to S with contributing factors
derived from C. That is, our new set of scenarios,
Sp
e, is defined as Sp
e = {f(s, c) | ∀s ∈S, ∀c ∈C},
resulting in a total of 144 scenarios (|S| × |C|).

--- Page 4 ---

For each of these new scenarios, we prompt the
language model to generate the two most proba-
ble mutually exclusive actions, denoted as Ap
e =
{(ase
1 , ase
2 ) | ∀se ∈Sp
e}, which we then present
to the annotators. More information about what
prompts we use and examples of scenario-action
pairs generated, see Appendix Section A.6.
Reddit scenarios and actions.
To enhance the
utility of UNIMORAL, we extend beyond hypothet-
ical scenarios by incorporating real-life examples
of moral dilemmas sourced from Reddit. We focus
on subreddits that frequently feature moral judg-
ments, namely r/AmItheAsshole, r/moraldilemmas,
r/AITAH, r/TwoHotTakes, and r/AmIOverreacting.
Posts made to these subreddits are carefully filtered
and rephrased to have standard formatting (see Ap-
pendix A.2 for details). To generate our data, we
prompt the Llama3.3-70B to rephrase the described
scenario as a moral dilemma and generate two mu-
tually exclusive actions applicable to that scenario.
Through this methodology, we extract ∼400k Red-
dit scenarios. We randomly select 10k scenarios
from the paraphrased Reddit data and perform topic
modeling using LDA (Blei et al., 2003) to identify
200 topics. To diversify the types of dilemmas in
our data, we cluster the scenarios into 200 clusters
using k-means (Hartigan and Wong, 1979) on the
scenarios’ topic distributions. We then select the
centroid of each cluster as a representative scenario,
resulting in a collection of 200 Reddit-based dilem-
mas, denoted as Sr
e, along with their corresponding
actions, Ar
e. By combining Sr
e with Sp
e, we obtain
the final list of moral scenarios Sm
e = {Sp
e ∪Sr
e}
and, similarly, actions Am
e = {Ap
e ∪Ar
e}.
Adding multilingualism.
In this study, we cre-
ate moral and cultural profiles of the participants
using standardized questionnaires. Specifically, we
employ the Moral Foundations Questionnaire 2
(MFQ2) (Atari et al., 2023) and Hofstede’s Value
Survey Module (VSM 2013) (Hofstede, 1994) to
capture various moral and cultural dimensions (see
Apendix Section A.4 for more details).
These
questionnaires, originally available in English, con-
tain translations in several other languages as well.
From the translations, we select five languages—
Arabic, Chinese, English, Russian, and Spanish—
for which both, MFQ2 and VSM, have translations,
enabling the study of cultural and moral value vari-
ations across these languages. Additionally, to
incorporate views from South Asia as well, we
manually translate these questionnaires into Hindi
using the standard method of translation and back-
translation (Brislin, 1970). Consequently, we have
the questionnaires available in six languages for
our study. Next, we translate the collected scenar-
ios Sm
e and actions Am
e into these languages using
the large version of the Seamlessm4t-v2 model
(Seamless Communication et al., 2023), giving
us Sm = {Te7→x(Sm
e )} and Am = {Te7→x(Am
e )}
where x ∈{A, C, H, R, S}} where A, C, H, R, S
stands for Arabic, Chinese, Hindi, Russian, and
Spanish, respectively, and T is the translation func-
tion. See Appendix Table 2 for translation exam-
ples. These translations are manually verified to
ensure quality for our crowd-sourced collection.
3.2
Crowd-sourced Annotation
After establishing Sm and Am, we initiate a crowd-
sourced data collection process to obtain annota-
tions for each scenario-action pair in our dataset,
{(sm
i , (ami
1 , ami
2 )|1 ≤i ≤|Sm|}. We solicit input
from annotators on the following points:
1. Which action would you choose?
2. Explain your choice and its consequence.
3. How well does it capture ethical principles?
4. What factors contributed to your decision?
5. Which emotion(s) influenced your decision?
6. What values shaped your decision?
7. Any alternative action considerable?
a. How well does it capture ethical principles?
Questions 3 and 7a assess the ethical frameworks
guiding the annotator’s chosen action for a sce-
nario (e.g. finding a wallet), categorized as fol-
lowing rules (e.g. handover the wallet to police),
doing good for the majority (e.g. donate money
to charity), respecting people’s rights (e.g. return
wallet to owner), and acting with good character
(e.g. return the wallet and check for other miss-
ing items.). These correspond to the four main
ethical frameworks in moral psychology: deontol-
ogy, utilitarianism, rights-based, and virtue ethics
(Kohlberg, 1963). Annotators rate each principle
on a scale of 1 to 5 based on its relevance to their
decision. Question 4 asks annotators to evaluate
the influence of each contributing factor C on their
decision-making, also on a scale of 1 to 5. If emo-
tion influenced their choice, they specify which
from Plutchik primary emotions (Plutchik, 1980).
After completing their scenario evaluations, anno-
tators fill out the MFQ2 and VSM to capture their
moral values and cultural dimensions, respectively.
Additionally, we collect demographic details and a
free-text self-description (excluding personal infor-

--- Page 5 ---

0%
20%
40%
60%
80%
100%
Percentage Distribution
Arabic
Chinese
English
Hindi
Russian
Spanish
55.3%
44.7%
56.6%
43.4%
53.4%
46.6%
56.8%
43.2%
55.7%
44.3%
55.4%
44.6%
Actions
Action A
Action B
(a) Actions have almost equal distribu-
tions across languages.
Deontology
Rights-based
Utilitarianism
Virtuous
3.0
3.5
4.0
Mean Likert Score
Language
Arabic
Chinese
English
Hindi
Russian
Spanish
(b) Ethical preferences in action choices
show correlation with annotators’ first
language, along with global trend.
Arabic
Chinese
English
Hindi
Russian
Spanish
Emotions
Moral
Culture
Role
Relationship
Legality
Politeness
Sacred vals
3.36
3.04
3.27
3.51
3.00
3.03
4.17
3.67
3.88
4.15
3.91
3.82
3.22
2.24
2.23
3.19
2.16
3.11
3.69
3.06
3.21
3.72
2.95
3.68
3.12
2.60
2.72
3.15
2.60
2.95
3.33
2.86
2.73
3.24
2.51
2.71
3.64
3.30
3.20
3.62
2.92
3.13
3.46
2.71
2.98
3.83
2.51
2.49
(c) Moral decisions are influenced by
varying factors, such as emotions and le-
gal frameworks, across languages.
Arabic
Chinese
English
Hindi
Russian Spanish
0
1
2
3
4
5
Score
Moral Values
Care
Equality
Proportionality
Loyalty
Authority
Purity
Arabic
Chinese
English
Hindi
Russian Spanish
60
40
20
0
20
40
60
80
Cultural Dimensions
PDI
IDV
MAS
UAI
LTO
IVR
(d) Moral and cultural values vary across languages as revealed by MFQ2 and
VSM assessments.
150
100
50
0
50
100
150
150
100
50
0
50
100
150
English
Chinese
Spanish
Russian
Arabic
Hindi
(e) The TSNE plot reveals moral and cul-
tural (dis)similarities between languages.
Figure 2: UNIMORAL at a glance. [Abbreviations – PDI: Power Distance, IDV: Individualism, MAS: Masculity,
UAI: Uncertainty Avoidance, LTO: Long Term Orientation, IVR: Indulgence vs Restraint]
mation) to serve as their persona.
Study type.
Gathering information for the com-
plete set of eight questions, as specified above, de-
mand considerable time and effort from the anno-
tators. Consequently, each annotator could handle
only a limited number of scenario-action pairs. To
address this issue, we structure our study in two
distinct approaches: extensive and compact. In the
extensive annotation, annotators are required to re-
spond to all eight questions associated with a given
scenario. In contrast, the compact study involves
responding only to the initial question, wherein an-
notators select their preferred action and proceed to
the next scenario. This method allows us to collect
more data per moral and cultural questionnaires in
a shorter time frame. The extensive data collection
contains a set of 144 psychological scenarios along-
side 50 Reddit-based dilemmas while the compact
study consists of another set of 144 psychological
scenarios and the remaining 150 Reddit dilemmas.
Platform specific information.
We construct our
annotation platform using Potato (Pei et al., 2022)
and host our crowd-sourced study on Prolific.com,
initiating the process with a pilot of 100 scenarios
in English and Chinese to assess the quality and
distribution of the collected data. During this phase,
we observe minimal to no difference between the
‘legal’ and ‘rule’ contributing factors, leading us to
combine them into a single category (‘laws’) for
the final annotation process, giving us C
′ such that
|C
′| = 8. After confirming that the data quality
met our standards, we proceed with twelve studies—
one extensive and one compact for each of the six
languages. In the extensive study, each annotator
evaluated seven scenarios, whereas in the compact
study, they assessed thirty scenarios. Each scenario
was reviewed by three annotators. Ultimately, UNI-
MORAL comprises a total of 582 instances with
extensive annotations and 882 for the compact ver-
sion in each language, culminating in a total of
5256 instances across the entire dataset. Further
details on the data collection process, screenshot of
the annotation framework, and data statistics, can
be found in Appendix Section A.3 and A.5.
3.3
Data Analysis
As outlined in Section 3.2, we collect eight types
of labels in the extended annotations to explore key
aspects of moral reasoning. These labels include
understanding preferred actions, factors influencing
moral reasoning, and examining variations across
languages and cultures. Following, we describe
aggregated trends across languages to highlight

--- Page 6 ---

general variation in preferences.
What kind of actions do people prefer?
We plot
the distribution of preferred actions across all lan-
guages in our dataset, finding an almost equal split,
which indicates variability in preferences (Figure
2a). Analyzing the primary ethical principles re-
veals global trends and a correlation with the anno-
tators’ first language (Figure 2b). For example,
all language groups rate virtue highly, but Ara-
bic and Hindi speakers also prioritize right-based
ethics highly, focusing on social justice. In contrast,
Spanish speakers emphasize utilitarianism, valu-
ing collective well-being, while Russian speakers
lean more toward deontology, reflecting duty-based
ethics. These differences may stem from cultural
variations in moral philosophy.
What are the factors affecting moral reasoning?
Moral decisions are often influenced by factors like
emotions, culture, legal frameworks and sacred val-
ues. Figure 2c shows the impact of these factors
across the six languages. While morality is the
most significant factor for all languages, sacred
values are more influential for Hindi and Arabic
speakers or those with high deontological tenden-
cies. Additionally, Spanish speakers value the role
of the action taker, while Chinese speakers priori-
tize politeness. This reflects cultural variations in
moral evaluation, with Spanish speakers prioritiz-
ing agency in decision-making and Chinese speak-
ers emphasizing social harmony and respect.
Why do different people take different actions?
While speakers of various languages prefer differ-
ent ethical principles, we explore distinctions based
on their moral and cultural values. Figure 2d shows
aggregate scores from the MFQ2 and VSM assess-
ments, revealing clear differences: Arabic speakers
are more attuned to the ‘purity’ foundation, while
Spanish speakers prioritize ‘equality’ more than En-
glish speakers. Additionally, English and Russian
speakers exhibit higher ‘individualism,’ correlating
with stronger deontological tendencies. A TSNE
plot, made by combining the moral and cultural
information, in Figure 2e highlights similarities be-
tween English, Spanish, and Chinese speakers, and
their differences from Arabic and Hindi speakers,
reflecting cultural and linguistic influences. See
Appendix Section A.5 for more details.
4
Experimental Analysis
While numerous tasks can be accomplished using
UNIMORAL, we focus on four core concepts of
moral reasoning: [I] Action Prediction (AP),
[II] Moral
Typology
Classification (MTC),
[III] Factor Attribution Analysis (FAA), and
[IV] Consequence Generation (CG). Considering
the proposed pipeline (Figure 1), our objective is
to explore all the phases of moral reasoning and
determine how UNIMORAL can be used to study
these phases.
4.1
Experimental Setup
We use three large language models: Phi-3.5-mini
Instruct (Abdin et al., 2024), Llama-3.1-8B Instruct
(Meta, 2024), and DeepSeek-R1-Distill Llama-8B
(DeepSeek-AI et al., 2025), for analyzing the four
questions. Additional details, including prompt
selection, are provided in Appendix Section A.6.
[I] Action Prediction.
With the growing in-
terest in agent-based modeling (Gao et al., 2024),
and synthetic annotations (Ivey et al., 2024), it be-
comes critical that LLMs are able to mirror be-
havior of certain groups. Consequently, we test
whether an LLM, when provided with information
about an individual’s values, can replicate their
decision-making process. To do this, we focus on
three key aspects from our annotation phase: (1)
moral values from MFQ2 (m), (2) cultural princi-
ples from VSM (c), and (3) self-descriptions, or
persona, providing an alternative way of captur-
ing the person’s value framework via lived expe-
rience (p). Additionally, we test an alternative ap-
proach using few-shot learning (fs), where past
decisions guide the model in predicting future re-
sponses.
The four attributes (m, c, p, fs) serve
as inputs to three different LLMs, which select
the most appropriate action a∗
i given a scenario
sm
i and its possible actions (ami
1 , ami
2 ). The task
is framed as: a∗
i
= argmaxj∈{1,2}P(ami
j |s, x),
where x ∈{m, c, p, fs} and P denotes the con-
ditional probability. Weighted F1-score acts as our
primary metric to capture class variability.
[II] Moral Typology Classification.
As out-
lined in Section 3.2, annotators rated the ethi-
cal principles of their chosen actions on a Likert
scale. This experiment tests whether an LLM can
predict these principles by comparing its predic-
tions to the ground truth, which is based on the
highest-rated principle(s). If multiple principles

--- Page 7 ---

share the highest rating, they are all included. The
LLM is prompted to identify the ethical factor in-
fluencing the user’s choice, and its prediction is
deemed correct if it matches any principle in the
ground truth set. We consider the four contex-
tual cues of {m, c, p, fs}, similar to AP to eval-
uate the LLM’s performance. In this approach,
the few-shot examples are constructed by consid-
ering the ethical principle selected by the anno-
tator for another scenario-action pair. Formally,
t∗
i = argmaxt∈T P(t|sm
i , (ami
1 , ami
2 ), a∗
i , x), where
x ∈{m, c, p, fs}. The weighted F1-score is again
employed as the metric of choice.
[III] Factor Attribution Analysis.
Moral
decisions are influenced by factors such as emo-
tions, responsibilities, and legal considerations. To
capture these influences, annotators rated 8 con-
tributing factors (F) on a scale of 1 to 5, as outlined
in Section 3.2. This analysis investigates whether
an LLM can accurately identify these factors when
given contextual information about the annotator
(m, c, p, fs). The few-shot examples are created
using the contributing factors selected by the anno-
tator in another scenario-action pair. The LLM’s
task is to predict the most significant factor influ-
encing the decision. If the prediction matches the
ground truth—determined by selecting the highest-
rated contributing factor (similar to MTC)—it is
considered correct. Formally, this is represented
as f∗
i
= argmaxf∈F P(f|sm
i , (ami
1 , ami
2 ), a∗
i , x),
where x ∈{m, c, p, fs}. Because this classifi-
cation involves 8 potential classes, the weighted
F1-score is chosen as the preferred metric.
[IV] Consequence Generation.
For this task,
we evaluate the ability of an LLM to generate the
consequence for a selected action, given a moral
dilemma. For each language, we compile all con-
sequences provided by annotators for a scenario
serves as the ground truth set for that specific
scenario-action pair. The LLM is then prompted
to generate a consequence for that scenario-action
pair. LLM outputs are scored according to the
maximum similarity with any ground truth conse-
quence for that scenario. Formally, this task can be
defined as ci = G(sm
i , a∗
i ), where G represents the
generative function of the LLM. To ensure a seman-
tically meaningful comparison, we use multilingual
BERTScore (Zhang et al., 2020) as our evaluation
metric, as it emphasizes semantic similarity rather
than exact word matches.
[I] Action
Prediction
0
20
40
60
Score
Arabic
Chinese
English
Hindi
Russian
Spanish
[II] Moral Typology
Classification
0
10
20
30
40
Arabic
Chinese
English
Hindi
Russian
Spanish
[III] Factor Attribution
Analysis
0
10
20
30
Score
Arabic
Chinese
English
Hindi
Russian
Spanish
[IV] Consequence
Generation
0
20
40
60
80
Arabic
Chinese
English
Hindi
Russian
Spanish
Figure 3: Models perform best in English, Spanish,
and Russian while struggling for Arabic, Chinese, and
Hindi as shown by their language-specific performance.
The scores are average weighted F1 scores for AP, MTC,
and FAA, and BERTScore for CG. Dotted line represents
random performance for each task.
4.2
Experimental Results
We evaluate the models across three dimensions:
language-specific performance, assessing their ef-
fectiveness across languages for AP, MTC, FAA, and
CG; contextual-cue-specific performance, exam-
ining the impact of cues (p, m, c, fs) on AP, MTC,
and FAA; and Reddit vs. psychological scenario
performance, comparing model performance on
Reddit-derived and hypothetical scenarios. In the
following paragraphs we highlight the important
results, while the full set of results can be found in
Appendix Section A.7.
Language-specific performance.
To evaluate
language-specific performance, we compute the
average scores across contextual cues (m, c, p, fs)
and across models for all tasks. Figure 3 presents
these results, highlighting substantial variability
across languages.
English consistently ranks
among the highest-performing languages, along-
side Spanish and Russian, across all four tasks. In
contrast, models exhibit significantly lower confi-
dence in Arabic and Hindi. These disparities can
be attributed to factors such as the availability of
high-quality training data and linguistic complexity.
While English and Spanish benefit from extensive
resources (especially in terms of moral datasets)
and structural similarities, Arabic and Hindi face
challenges related to data scarcity, dialectal varia-
tion, and complex morphology.

--- Page 8 ---

[I] Action
 Prediction
[II] Moral 
 Typology
Classification
[III] Factor
Attribution
 Analysis
0
10
20
30
40
50
60
Score
Persona
Persona
Persona
Morals
Morals
Morals
Culture
Culture
Culture
Few Shot
Few Shot
Few Shot
Figure 4: Contextual-cues like moral values and persona
help LLMs make better moral decisions. The scores are
average weighted F1 scores. Dotted line represents
random performance for each task.
Contextual cue specific performance.
In this
section, we examine the impact of different contex-
tual cues (m, c, p, fs) on task performance. Fig-
ure 4 presents the average weighted F1 score, ag-
gregated across languages and models, to illus-
trate how these cues influence capabilities in AP,
MTC, and FAA. For AP, explicitly providing moral
information results in the highest performance,
with persona-based inputs following closely. How-
ever, the performance is not significantly different
from chance. This suggests that while the self-
descriptions provided by annotators make effective
proxies for moral reasoning, LLMs still struggle
to internalize ethical principles, often relying on
surface-level patterns rather than genuine moral
understanding. In MTC, few-shot examples prove
to be the most influential, and the only cue to give
statistically better performance from chance, in
determining the ethical principle guiding the se-
lected action, followed by moral values and user
persona. Similarly, in FAA, persona and few-shot
examples play a crucial role in helping the model
understand individuals and accurately identify the
factors influencing their decisions. While FAA per-
forms worse than AP and MTC, it remains signifi-
cantly above chance, likely because identifying re-
sponsible factors relies more on surface linguistic
patterns than deep moral reasoning. These results
highlight moral reasoning as a challenge for LLMs,
which future research—enabled by datasets like
UNIMORAL—can help address.
Reddit vs. psychological scenario performance.
Are models better able to morally reason about
the real-world scenarios from Reddit versus hy-
pothetical psychological scenarios? No. Across
all tasks and languages, models perform consis-
[I] Action
 Prediction
[II] Moral
Typology
Classification
[III] Factor
Attribution
 Analysis
[IV] Consequence
Generation
0
10
20
30
40
50
60
70
80
Score
Psychological
Psychological
Psychological
Psychological
Reddit
Reddit
Reddit
Reddit
Figure 5: Models perform better on psychologically
grounded scenarios than on Reddit-based dilemmas
across all tasks and languages.
The scores are av-
erage weighted F1 scores for AP, MTC, and FAA, and
BERTScore for CG. Dotted line represents random per-
formance for each task.
tently better on psychologically grounded scenarios
than on Reddit-based dilemmas (Figure 5). While
the performance difference is modest in AP and
CG, it becomes more pronounced in MTC and FAA.
This disparity likely stems from the structured and
controlled nature of psychologically grounded sce-
narios, which provide explicit cues that help mod-
els isolate and interpret ethical principles. In con-
trast, Reddit-based dilemmas introduce real-world
noise, ambiguity, and implicit cultural or situational
biases, making moral reasoning more challeng-
ing—particularly in tasks like MTC and FAA, which
require precise, context-aware judgment.
5
Conclusion
Moral reasoning is a complex process and here
we introduce UNIMORAL to unify the multiple
strands of NLP research on moral reasoning. UNI-
MORAL is a holistic multilingual dataset covering
the full moral reasoning pipeline—from scenario
perception to consequence evaluation—across six
linguistically and culturally diverse contexts. It
combines psychologically grounded dilemmas with
real-world examples from social media, provid-
ing annotations on action choices, ethical princi-
ples, contributing factors, and consequences, en-
riched with annotators’ moral and cultural profiles.
Our analysis reveals key insights: (1) models ex-
hibit significant performance disparities across lan-
guages, (2) explicit contextual cues—such as moral
values and persona descriptions—greatly enhance
performance, emphasizing the role of contextual
awareness in ethical AI, and (3) tasks like moral ty-
pology classification and factor attribution remain
challenging, exposing gaps in models’ ability to

--- Page 9 ---

reason about the broader effects of moral actions.
While this paper explores four verticals of moral
reasoning, UNIMORAL enables further studies on
cross-cultural moral generalization, bias detection,
and moral or cultural value quantification.
6
Limitations
In this work, we introduce the UNIMORAL dataset,
which includes annotations capturing action pref-
erences, ethical justifications, and decision factors
alongside individual moral and cultural profiles.
While UNIMORAL has significant potential for
both morality-related and general NLP tasks, this
study serves as an initial exploration. Rather than
attempting an exhaustive analysis of all possible
applications, we focus on four exploratory tasks
and evaluate existing systems on these tasks with-
out fine-tuning. The scope of UNIMORAL is influ-
enced by the availability of the MFQ2 and the VSM
across different languages. Since these question-
naires have only been translated into a limited num-
ber of languages, and due to our team’s restricted
proficiency in certain languages, we conducted an-
notations in six languages only. Future research can
expand on our framework to extend UNIMORAL
to additional languages. Additionally, our data col-
lection was conducted on Prolific, meaning that
the dataset reflects the perspectives of those who
choose to participate on this platform. To ensure
diversity, we take deliberate steps to collect moral
and value-based information from a broad range of
participants. However, as with any dataset, it may
not fully capture the moral reasoning of the global
population. Future work can further expand partic-
ipation to enhance representation across different
cultural and linguistic backgrounds.
7
Ethical Considerations
To construct UNIMORAL, we gathered data from
crowd-sourced workers while ensuring that all in-
formation remained strictly anonymous. We em-
ployed Prolific and the Potato framework for data
collection, both of which rigorously anonymize
data by assigning each annotator a unique key. All
data recorded for an annotator is linked to this key,
with no names associated with the dataset. We ob-
tained informed consent from all participants and
ensured prompt and fair compensation for those
who completed our study. Additionally, the data
collection process was deemed exempt by our in-
stitution’s ethics review board.
References
Marah Abdin, Jyoti Aneja, and Hany Awadalla et al.
2024.
Phi-3 technical report: A highly capable
language model locally on your phone. Preprint,
arXiv:2404.14219.
Mark Alfano, Andrew Higgins, and Jacob Levernier.
2018. Identifying virtues and values through obituary
data-mining. The Journal of Value Inquiry, 52:59–
79.
Areej Alhassan, Jinkai Zhang, and Viktor Schlegel.
2022. ‘am I the bad one’? predicting the moral judge-
ment of the crowd using pre–trained language mod-
els. In Proceedings of the Thirteenth Language Re-
sources and Evaluation Conference, pages 267–276,
Marseille, France. European Language Resources
Association.
Milad Alshomary, Roxanne El Baff, Timon Gurcke, and
Henning Wachsmuth. 2022. The moral debater: A
study on the computational generation of morally
framed arguments. In Proceedings of the 60th An-
nual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 8782–
8797, Dublin, Ireland. Association for Computational
Linguistics.
Prithviraj Ammanabrolu, Liwei Jiang, Maarten Sap,
Hannaneh Hajishirzi, and Yejin Choi. 2022. Aligning
to social norms and values in interactive narratives.
In Proceedings of the 2022 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
pages 5994–6017, Seattle, United States. Association
for Computational Linguistics.
M. Anderson, S.L. Anderson, and C. Armen. 2006. An
approach to computing ethics. IEEE Intelligent Sys-
tems, 21(4):56–63.
Luigi Asprino, Luana Bulla, Stefano De Giorgis, Aldo
Gangemi, Ludovica Marinucci, and Misael Mongiovi.
2022. Uncovering values: Detecting latent moral
content from natural language with explainable and
non-trained methods. In Proceedings of Deep Learn-
ing Inside Out (DeeLIO 2022): The 3rd Workshop
on Knowledge Extraction and Integration for Deep
Learning Architectures, pages 33–41, Dublin, Ireland
and Online. Association for Computational Linguis-
tics.
Mohammad Atari, Jonathan Haidt, Jesse Graham, Sena
Koleva, Sean T Stevens, and Morteza Dehghani.
2023. Morality beyond the weird: How the nomo-
logical network of morality varies across cultures.
Journal of Personality and Social Psychology.
David M Blei, Andrew Y Ng, and Michael I Jordan.
2003. Latent dirichlet allocation. Journal of machine
Learning research, 3(Jan):993–1022.
Nicholas Botzer, Shawn Gu, and Tim Weninger. 2022.
Analysis of moral judgment on reddit. IEEE Trans-
actions on Computational Social Systems.

--- Page 10 ---

Richard W. Brislin. 1970. Back-translation for cross-
cultural research. Journal of Cross-Cultural Psychol-
ogy, 1(3):185–216.
Jeremy IM Carpendale. 2009. Piaget’s theory of moral
development.
Anne Colby, Lawrence Kohlberg, John Gibbs, Marcus
Lieberman, Kurt Fischer, and Herbert D. Saltzstein.
1983.
A longitudinal study of moral judgment.
Monographs of the Society for Research in Child
Development, 48(1/2):1–124.
Antonio R Damasio. 1996. The somatic marker hy-
pothesis and the possible functions of the prefrontal
cortex.
Philosophical Transactions of the Royal
Society of London. Series B: Biological Sciences,
351(1346):1413–1420.
DeepSeek-AI,
Daya
Guo,
Dejian
Yang,
and
Haowei Zhang et al. 2025.
Deepseek-r1:
In-
centivizing
reasoning
capability
in
llms
via
reinforcement learning. Preprint, arXiv:2501.12948.
Naomi Ellemers, Jojanneke van der Toorn, Yavor
Paunov, and Thed van Leeuwen. 2019. The psychol-
ogy of morality: A review and analysis of empirical
studies published from 1940 through 2017. Person-
ality and Social Psychology Review, 23(4):332–366.
PMID: 30658545.
Denis Emelin, Ronan Le Bras, Jena D. Hwang, Maxwell
Forbes, and Yejin Choi. 2021. Moral stories: Situ-
ated reasoning about norms, intents, actions, and
their consequences. In Proceedings of the 2021 Con-
ference on Empirical Methods in Natural Language
Processing, pages 698–718, Online and Punta Cana,
Dominican Republic. Association for Computational
Linguistics.
Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao
Ding, Zhilun Zhou, Fengli Xu, and Yong Li. 2024.
Large language models empowered agent-based mod-
eling and simulation: A survey and perspectives.
Humanities and Social Sciences Communications,
11(1):1–24.
Justin Garten, Reihane Boghrati, Joe Hoover, Kate M.
Johnson, and Morteza Dehghani. 2016. Morality
between the lines : Detecting moral sentiment in
text. In Proceedings of IJCAI 2016 workshop on
Computational Modeling of Attitudes.
Jesse Graham, Jonathan Haidt, Sena Koleva, Matt
Motyl, Ravi Iyer, Sean P Wojcik, and Peter H Ditto.
2013. Moral foundations theory: The pragmatic va-
lidity of moral pluralism. In Advances in experi-
mental social psychology, volume 47, pages 55–130.
Elsevier.
Jesse Graham, Jonathan Haidt, Matt Motyl, Peter
Meindl, Carol Iskiwitch, and Marlon Mooijman.
2018. Moral foundations theory. Atlas of moral
psychology, 211.
Joshua D Greene. 2007. Why are vmpfc patients more
utilitarian? a dual-process theory of moral judgment
explains. Trends in cognitive sciences, 11(8):322–
323.
Jian Guan, Ziqi Liu, and Minlie Huang. 2022. A cor-
pus for understanding and generating moral stories.
In Proceedings of the 2022 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies,
pages 5069–5087, Seattle, United States. Association
for Computational Linguistics.
Jonathan Haidt. 2001. The emotional dog and its ra-
tional tail: a social intuitionist approach to moral
judgment. Psychological review, 108(4):814.
John A Hartigan and Manchek A Wong. 1979. Algo-
rithm as 136: A k-means clustering algorithm. Jour-
nal of the royal statistical society. series c (applied
statistics), 28(1):100–108.
Dan Hendrycks, Collin Burns, Steven Basart, Andrew
Critch, Jerry Li, Dawn Song, and Jacob Steinhardt.
2020. Aligning ai with shared human values. arXiv
preprint arXiv:2008.02275.
Dan Hendrycks, Collin Burns, Steven Basart, Andrew
Critch, Jerry Li, Dawn Song, and Jacob Steinhardt.
2021. Aligning {ai} with shared human values. In
International Conference on Learning Representa-
tions.
Geert Hofstede. 1994. Vsm94 (values survey module
1994). IRIC, Tilburg, Netherlands.
Joe Hoover,
Gwenyth Portillo-Wightman,
Leigh
Yeh, Shreya Havaldar, Aida Mostafazadeh Davani,
Ying Lin, Brendan Kennedy, Mohammad Atari,
Zahra Kamel, Madelyn Mendlen, Gabriela Moreno,
Christina Park, Tingyee E. Chang, Jenna Chin, Chris-
tian Leong, Jun Yen Leung, Arineh Mirinjian, and
Morteza Dehghani. 2020. Moral foundations twit-
ter corpus: A collection of 35k tweets annotated for
moral sentiment. Social Psychological and Personal-
ity Science, 11(8):1057–1071.
Frederic R. Hopp, Jacob T. Fisher, Devin Cornell,
Richard Huskey, and René Weber. 2020. The ex-
tended moral foundations dictionary (eMFD): De-
velopment and applications of a crowd-sourced ap-
proach to extracting moral intuitions from text. Be-
havior Research Methods, 53(1):232–246.
Ching-Wen Hsu, Chun-Lin Chou, Hsuan Liu, and Jheng-
Long Wu. 2021. A corpus for dimensional sentiment
classification on YouTube streaming service. In Pro-
ceedings of the 33rd Conference on Computational
Linguistics and Speech Processing (ROCLING 2021),
pages 286–293, Taoyuan, Taiwan. The Association
for Computational Linguistics and Chinese Language
Processing (ACLCLP).
Shima Imani, Liang Du, and Harsh Shrivastava. 2023.
MathPrompter: Mathematical reasoning using large

--- Page 11 ---

language models. In Proceedings of the 61st An-
nual Meeting of the Association for Computational
Linguistics (Volume 5: Industry Track), pages 37–
42, Toronto, Canada. Association for Computational
Linguistics.
Jonathan Ivey,
Shivani Kumar,
Jiayu Liu,
Hua
Shen, Sushrita Rakshit, Rohan Raju, Haotian
Zhang, Aparna Ananthasubramaniam, Junghwan
Kim, Bowen Yi, et al. 2024. Real or robotic? as-
sessing whether llms accurately simulate qualities
of human responses in dialogue.
arXiv preprint
arXiv:2409.08330.
Zhijing Jin, Sydney Levine, Fernando Gonzalez, Ojasv
Kamal, Maarten Sap, Mrinmaya Sachan, Rada Mihal-
cea, Joshua B. Tenenbaum, and Bernhard Schölkopf.
2022. When to make exceptions: Exploring language
models as accounts of human moral judgment. ArXiv,
abs/2210.01478.
Brendan
Kennedy,
Mohammad
Atari,
Aida
Mostafazadeh
Davani,
Joe
Hoover,
Ali
Om-
rani, Jesse Graham, and Morteza Dehghani. 2021.
Moral concerns are differentially observable in
language. Cognition, 212:104696.
Jonathan Kobbe, Ines Rehbein, Ioana Hulpus,, and
Heiner Stuckenschmidt. 2020. Exploring morality in
argumentation. In Proceedings of the 7th Workshop
on Argument Mining, pages 30–40, Online. Associa-
tion for Computational Linguistics.
Lawrence Kohlberg. 1963. Moral development and
identification.
Radoslaw Komuda, Rafal Rzepka, and Kenji Araki.
2013. Aristotelian approach and shallow search set-
tings for fast ethical judgment. International Journal
of Computational Linguistics Research, 4(1):14–22.
Alex Gwo Jen Lan and Ivandré Paraboni. 2022. Text-
and author-dependent moral foundations classifica-
tion. New Review of Hypermedia and Multimedia,
28(1-2):18–38.
Michael Lessnoff. 1971. John rawls’ theory of justice.
Political Studies, 19(1):63–80.
Georg Lind. 2008. The meaning and measurement of
moral judgment competence : a dual-aspect model.
In Daniel Fasko, editor, Contemporary philosophical
and psychological perspectives on moral develop-
ment and education, pages 185–220. Hampton Press,
Cresskill, NJ.
Nicholas Lourie, Ronan Le Bras, and Yejin Choi. 2021.
SCRUPLES: A corpus of community ethical judg-
ments on 32, 000 real-life anecdotes. Proceedings
of the AAAI Conference on Artificial Intelligence,
35(15):13470–13479.
Akiko Matsuo, Kazutoshi Sasahara, Yasuhiro Taguchi,
and Minoru Karasawa. 2019. Development and vali-
dation of the japanese moral foundations dictionary.
PLOS ONE, 14(3):e0213343.
Meta. 2024. Introducing llama 3.1: Our most capable
models to date.
Negar Mokhberian, Andrés Abeliuk, Patrick Cummings,
and Kristina Lerman. 2020. Moral framing and ide-
ological bias of news. In Social Informatics: 12th
International Conference, SocInfo 2020, Pisa, Italy,
October 6–9, 2020, Proceedings 12, pages 206–219.
Springer.
Marlon Mooijman, Joe Hoover, Ying Lin, Heng Ji, and
Morteza Dehghani. 2018. Moralization in social net-
works and the emergence of violence during protests.
Nature Human Behaviour, 2(6):389–396.
Razieh Tadayon Nabavi. 2012. Bandura’s social learn-
ing theory & social cognitive learning theory. Theory
of Developmental Psychology, 1(1):1–24.
Darcia Narvaez and James Rest. 1995. The four compo-
nents of acting morally. Moral behavior and moral
development: An introduction, 1(1):385–400.
Adam Paszke, Sam Gross, Francisco Massa, Adam
Lerer, James Bradbury, Gregory Chanan, Trevor
Killeen, Zeming Lin, Natalia Gimelshein, Luca
Antiga, Alban Desmaison, Andreas Kopf, Edward
Yang, Zachary DeVito, Martin Raison, Alykhan Te-
jani, Sasank Chilamkurthy, Benoit Steiner, Lu Fang,
Junjie Bai, and Soumith Chintala. 2019. Pytorch:
An imperative style, high-performance deep learning
library. In Advances in Neural Information Process-
ing Systems 32, pages 8024–8035. Curran Associates,
Inc.
Matheus Camasmie Pavan, Vitor Garcia dos Santos,
Alex Gwo Jen Lan, João Trevisan Martins, Wes-
ley Ramos dos Santos, Caio Deutsch, Pablo Bot-
ton da Costa, Fernando Chiu Hsieh, and Ivandré
Paraboni. 2023. Morality classification in natural
language text. IEEE Transactions on Affective Com-
puting, 14(1):857–863.
Jiaxin Pei, Aparna Ananthasubramaniam, Xingyao
Wang, Naitian Zhou, Apostolos Dedeloudis, Jack-
son Sargent, and David Jurgens. 2022. Potato: The
portable text annotation tool. In Proceedings of the
2022 Conference on Empirical Methods in Natural
Language Processing: System Demonstrations.
R. Plutchik. 1980. A general psychoevolutionary the-
ory of emotion. Emotion: Theory, research, and
experience, 1.
Ming Qian, Jaye Laguardia, and Davis Qian. 2021.
Morality beyond the lines: Detecting moral senti-
ment using AI-generated synthetic context. In Ar-
tificial Intelligence in HCI, pages 84–94. Springer
International Publishing.
J Rest. 1979. Development in judging moral issues.
minneapolis, univ.
Shamik Roy and Dan Goldwasser. 2021. Analysis of
nuanced stances and sentiment towards entities of
US politicians through the lens of moral foundation

--- Page 12 ---

theory. In Proceedings of the Ninth International
Workshop on Natural Language Processing for Social
Media, pages 1–13, Online. Association for Compu-
tational Linguistics.
Shamik Roy, Maria Leonor Pacheco, and Dan Gold-
wasser. 2021. Identifying morality frames in political
tweets using relational learning. In Proceedings of
the 2021 Conference on Empirical Methods in Natu-
ral Language Processing, pages 9939–9958, Online
and Punta Cana, Dominican Republic. Association
for Computational Linguistics.
Wesley Santos and Ivandré Paraboni. 2019.
Moral
stance recognition and polarity classification from
Twitter and elicited text. In Proceedings of the Inter-
national Conference on Recent Advances in Natural
Language Processing (RANLP 2019), pages 1069–
1075, Varna, Bulgaria. INCOMA Ltd.
Maarten Sap, Vered Shwartz, Antoine Bosselut, Yejin
Choi, and Dan Roth. 2020. Commonsense reason-
ing for natural language processing. In Proceedings
of the 58th Annual Meeting of the Association for
Computational Linguistics: Tutorial Abstracts, pages
27–33, Online. Association for Computational Lin-
guistics.
Patrick Schramowski, Cigdem Turan, Sophie Jentzsch,
Constantin Rothkopf, and Kristian Kersting. 2019.
Bert has a moral compass: Improvements of ethi-
cal and moral values of machines. arXiv preprint
arXiv:1912.05238.
Seamless Communication, Loïc Barrault, Yu-An Chung,
and Mariano Coria Meglioli et al. 2023. Seamless:
Multilingual expressive and streaming speech trans-
lation.
Tao Shen, Xiubo Geng, and Daxin Jiang. 2022. So-
cial norms-grounded machine ethics in complex nar-
rative situation. In Proceedings of the 29th Inter-
national Conference on Computational Linguistics,
pages 1333–1343, Gyeongju, Republic of Korea. In-
ternational Committee on Computational Linguistics.
Marco Stranisci, Michele De Leonardis, Cristina Bosco,
and Viviana Patti. 2021. The expression of moral
values in the twitter debate: a corpus of conversations.
Italian Journal of Computational Linguistics, 7(1 |
2):113–132.
Livia Teernstra,
Peter van der Putten,
Liesbeth
Noordegraaf-Eelens, and Fons Verbeek. 2016. The
morality machine: Tracking moral values in tweets.
In Advances in Intelligent Data Analysis XV: 15th
International Symposium, IDA 2016, Stockholm, Swe-
den, October 13-15, 2016, Proceedings 15, pages
26–37. Springer.
Jackson Trager, Alireza S Ziabari, Aida Mostafazadeh
Davani,
Preni
Golazazian,
Farzan
Karimi-
Malekabadi,
Ali Omrani,
Zhihe Li,
Brendan
Kennedy, Nils Karl Reimer, Melissa Reyes, et al.
2022. The moral foundations reddit corpus. arXiv
preprint arXiv:2208.05545.
Karina Vida, Judith Simon, and Anne Lauscher. 2023.
Values, ethics, morals? on the use of moral con-
cepts in NLP research. In Findings of the Associa-
tion for Computational Linguistics: EMNLP 2023,
pages 5534–5554, Singapore. Association for Com-
putational Linguistics.
Lawrence J. Walker. 1989. A longitudinal study of
moral reasoning. Child Development, 60(1):157–
166.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Remi Louf, Morgan Funtow-
icz, Joe Davison, Sam Shleifer, Patrick von Platen,
Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu,
Teven Le Scao, Sylvain Gugger, Mariama Drame,
Quentin Lhoest, and Alexander Rush. 2020. Trans-
formers: State-of-the-art natural language processing.
In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 38–45, Online. Association
for Computational Linguistics.
Masahiro Yamamoto and Masafumi Hagiwara. 2014.
Moral judgment system using evaluation expressions.
In 2014 Joint 7th International Conference on Soft
Computing and Intelligent Systems (SCIS) and 15th
International Symposium on Advanced Intelligent
Systems (ISIS), pages 1040–1047.
Diyi Yang, Dirk Hovy, David Jurgens, and Barbara
Plank. 2024. The call for socially aware language
technologies. Preprint, arXiv:2405.02411.
Fei Yu, Hongbo Zhang, Prayag Tiwari, and Benyou
Wang. 2024. Natural language reasoning, a survey.
ACM Comput. Surv., 56(12).
Lorenzo Zangari, Candida M. Greco, Davide Picca, and
Andrea Tagarelli. 2025. ME2-BERT: Are events and
emotions what you need for moral foundation predic-
tion? In Proceedings of the 31st International Con-
ference on Computational Linguistics, pages 9516–
9532, Abu Dhabi, UAE. Association for Computa-
tional Linguistics.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q.
Weinberger, and Yoav Artzi. 2020.
Bertscore:
Evaluating text generation with bert.
Preprint,
arXiv:1904.09675.
A
Appendix
A.1
Seed Scenario Development
In order to collect our initial set of scenarios that
elicit the moral reasoning pipeline in an individual,
we consider the scenarios discussed in three psy-
chological theories as discussed below. We show
the collected 16 scenarios in Table 1.

--- Page 13 ---

Moral Judgment Interview (MJI).
The Moral
Judgment Interview (Kohlberg, 1963), developed
by Lawrence Kohlberg, is a structured interview
method used to assess an individual’s moral rea-
soning based on their responses to hypothetical
moral dilemmas. Participants are asked to justify
their decisions, and their reasoning is evaluated
according to Kohlberg’s six-stage theory of moral
development.
Defining Issues Test (DIT).
The Defining Issues
Test (Rest, 1979), introduced by James Rest, is a
standardized multiple-choice assessment designed
to measure moral reasoning through the lens of
neo-Kohlbergian theory (Kohlberg, 1963). Unlike
the MJI, which relies on open-ended responses, the
DIT presents participants with moral dilemmas and
asks them to rank predefined considerations based
on their importance in decision-making.
Moral Competence Test (MCT).
The Moral
Competence Test (Lind, 2008), developed by
Georg Lind, assesses moral competence as the abil-
ity to apply moral principles consistently across
varying contexts. Unlike the MJI and DIT, the
MCT evaluates both moral orientation and con-
sistency in reasoning by presenting respondents
with moral dilemmas and asking them to rate ar-
guments for and against different positions. It em-
phasizes cognitive-affective integration, reflecting
how individuals balance moral ideals with practical
decision-making. The MCT’s design makes it a
useful tool for studying moral competence devel-
opment and the effectiveness of moral education
programs.
A.2
Reddit Moral Dilemma Preprocessing
Reddit contains multiple communities where users
submit posts describing a moral dilemma and ask-
ing for help or describing a dilemma and what
action the user took and asking for judgment. One
of the most well-known of these is r/AmItheAss-
hole which attracts hundreds of posts or more per
day. We curate a dataset of dilemmas by synthe-
sizing dilemmas from the real-world scenarios de-
scribed by users in ‘AmItheAsshole’, ‘moraldilem-
mas’, ‘AITAH’, ‘TwoHotTakes’, and ‘AmIOverre-
acting’. Some scenarios are too short so we restrict
our candidate scenarios to those with at least 50
words. To avoid dilemmas that are Reddit-specific
or require access to external material to understand,
we exclude posts that mention Reddit, another sub-
reddit, or a URL. Some users come back to provide
Figure 6: Distribution of nationalities of the Prolific
participants who participated in our studies. The size of
the circle is proportional to the number of participants
from that country.
additional details or updates using the edit function-
ality and leave a note “EDIT:” ; we anticipated that
these might be more challenging to paragraph due
to the more complex post structure so we remove
any posts that have been explicitly edited.
A.3
UNIMORAL Annotation Framework
We collect UNIMORAL through crowd-sourcing,
wherein we use Potato (Pei et al., 2022) to develop
our annotation platform and use Prolific to deploy
it. Each annotator is shown an introduction page
before they begin the annotation process which
described their task in the annotation process and
collect their informed consent. Figure 9a shows the
introduction and consent page that we show to the
annotator to prime them for the study, while Figure
9b shows how the annotation framework looks to
the Prolific participant.
For each language, up to 113 participants were
enrolled to perform annotations for both the ex-
tensive and compact studies. Participants were
compensated at an average rate of $13 per hour for
their annotation work. Given the multilingual na-
ture of our data collection, we staggered the study
start times across different time zones to recruit par-
ticipants from regions where the target languages
are commonly spoken. For example, the Chinese-
language study began at 10 AM CST, while the
English-language study started at 5 PM EST. To
illustrate the diversity of our participants, we vi-
sualize their nationalities in Figure 6. This figure
demonstrate that UNIMORAL captures a broad geo-
graphic range, reflecting a variety of cultural back-
grounds. Participants in our data collection were
able to access a separate webpage displaying their
consolidated moral and cultural scores, allowing
them to gain insights from the results. This also
serves as an additional incentive for participation.

--- Page 14 ---

Theories
Moral Dilemma
Moral Judgment Interview
Heinz’s wife is dying from a particular type of cancer. There is a drug that might save her, but it is very expensive,
and Heinz cannot afford it. The pharmacist who discovered the drug refuses to sell it for any less or to let Heinz
pay later. Heinz is considering breaking into the pharmacy to steal the drug.
A man is traveling with his sick father, who is dying. The father begs his son to end his suffering by giving him a
fatal dose of medicine. The son is torn between ending his father’s pain and the moral implications of killing him.
A drug addict is considering stealing money from his family to buy drugs. He knows that if he doesn’t get his fix,
he will suffer severe withdrawal symptoms.
A judge is faced with a difficult decision. A man has committed a minor crime but is a significant public figure.
Sentencing him to prison could lead to public unrest and negative consequences for society.
A doctor has five patients in critical condition, each requiring a different organ transplant to survive. A healthy
person walks into the hospital for a routine check-up. The doctor realizes that this person could save the five
patients if their organs were harvested.
Two prisoners are accused of a crime. The authorities offer each prisoner a deal: if one testifies against the other,
the testifying prisoner will go free while the other receives a harsh sentence. If both remain silent, they both receive
moderate sentences. If both testify against each other, both receive harsh sentences.
A trolley is headed towards five people tied up on the tracks. You are standing next to a lever that can switch the
trolley to another track where only one person is tied up.
Defining Issues Test
An escaped prisoner has lived an exemplary life for many years but is discovered and arrested. The dilemma is
whether he should be sent back to prison.
A reporter must decide whether to publish a controversial story that could cause public unrest but would expose a
significant injustice.
A school board must decide whether to allocate limited resources to a special education program or a program for
gifted students.
A doctor must decide whether to administer a high-risk treatment to a terminally ill patient. The treatment could
either extend the patient’s life or cause severe side effects.
A father is a widower with two young children. He must decide whether to remarry for the sake of his children,
despite personal reservations.
A reporter knows of a scandal involving a public official. Publishing the story could harm innocent people but also
serve the public interest.
Moral Com-
petence Test
A group of workers goes on strike to demand higher wages. The strike causes significant disruption to the company
and the public.
A prestigious school has limited spaces and must decide whether to admit a talented student from a disadvantaged
background or a student with excellent academic records but from a well-off family.
A police officer must decide whether to enforce a law that they believe is unjust but is required by their duty to
uphold the law.
Table 1: Seed Scenarios or moral dilemmas extracted from the Moral Judgment Interview, Defining Issues Test, and
Moral Competence Test theories.
Figure 10 provides a preview of this webpage. The
entire pipeline for collecting UNIMORAL is visu-
alised in Figure 7.
A.4
Calculation of the Moral and Cultural
Scores from Participant Responses
The Moral Foundation Questionnaire (MFQ)
(Kohlberg, 1963) is designed to measure moral
values based on Moral Foundations Theory (MFT),
which identifies five key moral dimensions: Care,
Fairness, Loyalty, Authority, and Purity. A recent
extension of this, the MFQ2 (Atari et al., 2023),
introduces another dimension of Proportionality
and add relevant questions to the original MFQ
questionnaire. The MFQ and MFQ2 consists of
two sections: one assessing the relevance of differ-
ent moral concerns (e.g., “Whether or not some-
one suffered emotionally") and another evaluating
agreement with moral statements (e.g., “Compas-
sion for those who are suffering is the most crucial
virtue"). Participants respond using a Likert scale,
typically ranging from 1 (not at all relevant/strongly
disagree) to 5 (extremely relevant/strongly agree).
To compute moral scores, responses for each moral
foundation are averaged separately from the rele-
vance and endorsement sections. A higher score
on a particular foundation indicates a stronger in-
clination toward that moral dimension. We use the
MFQ2 in our study, thus dealing with 6 dimension
score of morality.
The Values Survey Module (VSM) (Hofstede,
1994), developed by Geert Hofstede, measures cul-
tural dimensions across societies, focusing on six
key aspects:
1. Power Distance (PDI) – The degree to which
inequality in power and authority is accepted.

--- Page 15 ---

English
Chinese
Russian
Scenario
Kevin, a police officer, has been assigned to arrest
a suspect in a serious crime case. The suspect is his
cousin. After reviewing the evidence, Kevin finds
it to be circumstantial, leading him to question his
cousin’s guilt. Meanwhile, the actual perpetrator
remains at large. What course of action should
Kevin take?
警官凯文被派去逮捕一个严重犯罪案的嫌疑人
嫌疑人是他的堂兄经过审查证据后,凯文发现
证据是间接的,这让他质疑堂兄的罪恶与此同
时,实际的罪犯仍然在逃凯文应该采取什么行
动?
Кевин, полицейский, получил задание аре-
стовать подозреваемого в серьезном пре-
ступном деле. Подозреваемый - его двою-
родный брат. После рассмотрения доказа-
тельств, Кевин считает, что это косвенные,
что заставляет его сомневаться в вине свое-
го двоюродного брата. Тем временем, факти-
ческий преступник остается на свободе. Ка-
кой курс действий должен принять Кевин?
Possible Actions
1. Arrest the cousin based on the available evi-
dence, potentially sacrificing family ties and his
cousin’s freedom, even if he may be innocent.
2. Withhold the arrest and further investigate, risk-
ing the actual perpetrator claiming more victims
and damaging public trust in the police, but also
preserving the possibility of his cousin’s innocence.
1. 基于现有的证据逮捕表兄弟, 潜在地牺牲家
庭关系和表兄弟的自由, 即使他可能无辜.
2. 风险是实际的罪犯声称更多受害者, 损害公
众对警方的信任,
1. Арестуйте двоюродного брата на основе
имеющихся доказательств, потенциально по-
жертвовав семейными связями и свободой
его двоюродного брата, даже если он может
быть невиновным.
2. Остановить арест и продолжить расследо-
вание, рискуя тем, что фактический преступ-
ник претендует на больше жертв и наносит
ущерб доверию общественности к полиции,
но также сохраняя возможность невиновно-
сти его двоюродного брата.
Table 2: Example scenario and possible action set from UNIMORAL with the English version along with the Chinese
and Russian translated versions.
2. Individualism vs. Collectivism (IDV) – The
extent to which people prioritize personal au-
tonomy over group loyalty.
3. Masculinity vs. Femininity (MAS) – Whether
a culture values competitiveness and achieve-
ment (masculine) or care and quality of life
(feminine).
4. Uncertainty Avoidance (UAI) – The prefer-
ence for structured, rule-based environments
over ambiguity.
5. Long-Term Orientation vs. Short-Term Orien-
tation (LTO) – The extent to which a society
values perseverance and future rewards versus
tradition and immediate gratification.
6. Indulgence vs. Restraint (IVR) – The level of
emphasis on personal enjoyment and leisure
versus strict social norms.
Each cultural dimension is measured using mul-
tiple questionnaire items, with responses typically
rated on a five-point Likert scale.
Scores for
each dimension are calculated by averaging the
responses associated with that dimension, then ad-
justing using Hofstede’s formula. These scores
provide insights into dominant cultural values and
their influence on decision-making and social be-
havior.
We calculate the moral and cultural scores and
compare the average score across the participants
having different nationalities. Figure 8a and Figure
8b shows the most prominent values of morals and
culture preferred by the annotators of each country.
Study type
# Langs
# Sc/lang
# Ann/sc
# Inst/lang
Extensive
6
194
3
582
Compact
6
294
3
882
6
488
3
1464
Table 3: Language wise statistics for the UNIMORAL
dataset.
A.5
UNIMORAL Statistics
Table 3 illustrates the language wise statistics for
UNIMORAL. As can be observed, each language
contains a total of 1464 instances, making the total
number of instances in UNIMORAL across the six
languages as 8784. We also show one example sce-
nario and possible action set generated using the
Llama-3.1-70B Instruct model in Table 2. Trans-
lations for Chinese and Russian, obtained via the
Seamless-m4t-v2 model, are also shown.
A.6
Prompts
This study involves the usage of prompts in two
ways – 1) generating the data for human annota-
tion, and 2) prompting the LLMs for evaluation
of the data. All prompts that are selected for final
use, whether in data generation or model evalu-
ation, are finalized from an initial pool of possi-
ble prompts. We consider a number of candidate
prompts, conduct initial experiment using them
over a small subset of the English data and com-
pare the results manually. We then select the best
performing prompts and translate them to all the

--- Page 16 ---

MIJ
DIT
MCT
Seed Scenarios, S
Contributing Factors, C
Rephrased & 
Filtered
144 Scenarios + Actions
144 Scenarios + Actions
Reddit
Scenarios
Psychological Scenarios and Action Generation
Psychological
Theories
50 Scenarios + Actions
150 Scenarios + Actions
Topic modeling &
k-means clustering
200 Scenarios + Actions for
Extensive study
Reddit Scenarios and Action Generation
Data for Compact Study
Data for Extensive Study
Figure 7: Data collection process for UNIMORAL. Final
data comes from a mix of psychological scenarios and
Reddit based dilemmas.
six languages required. We use chain of thought
prompting for data generation while single prompts
are used for evaluating LLMs. We list the prompts
selected below. Anything in between square brack-
ets is a placeholder, which is replaced with content
before prompting any model.
Scenario generation Prompt 1:
You are a moral psychology expert. Given
the following example scenario: [SEED
SCENARIO], write its moral information,
decision maker role, emotions elicited in
the decision maker, consequence of the
possible actions, and non moral and non
emotional factors, such as legality, game
rules, sacred values, culture, and social
relations, involved in the decision making
process.
Mention all these in no more than one line
each. Just return the characteristics as a
Moral Values
Authority
Care
Proportionality
Purity
Equality
Loyalty
(a) Country-wise distribution of most prominent moral values
collected via MFQ2 in our study.
Cultural Values
IVR
LTO
IDV
MAS
UAI
PDI
(b) Country-wise distribution of most prominent cultural prin-
ciples collected via VSM in our study.
Figure 8: Distribution of moral values and cultural di-
mensions across countries from UNIMORAL.
JSON file.
Scenario generation Prompt 2:
Given the following definition of a
scenario:
A scenario is a detailed and structured
description of a hypothetical situation
designed to explore potential actions
and outcomes.
It includes several key
elements. The Actor Role identifies the
primary individual or group involved
in the scenario.
The Context provides
the background and setting where the
scenario takes place.
Key Players are
other significant individuals or groups that
interact with the main actor. The Actor
Objectives outline the goals, conflicts, and
dilemmas faced by the actor within the
scenario. Finally, the Action Question is a
prompt that asks the actor to determine
the best course of action based on the
given information.
Write [NUM SCENARIOS] scenarios, in
third person mode, similar to the following

--- Page 17 ---

example scenario: [SEED SCENARIO].
The key characteristics of the scenario is
described here: [PROMPT1 RESPONSE].
Write the scenarios in a paragraph format
in no more than five lines, eliciting a simi-
lar moral dilemma such that each scenario
contains the following characteristic: The
[MOTIVATION] becomes the driving force
of the decision making process. This sce-
nario should not be different from the past
scenarios. Just return the scenarios as a
JSON file with keys as scenatio number
and value as the scenario.
Scenario generation Prompt 3:
Rewrite the following scenario so that it
focuses only on the facts and ends with
an open-ended question about what to do,
removing any motivational details. Here
is the scenario: [SCENARIO]
Action generation Prompt 1:
Consider the following scenario: [SCE-
NARIO].
Deconstruct it to find out the immediate
key stakeholders, list out their emotions,
needs, biases in terms of pro and anti, and
social influence given the scenario. An-
swer succinctly in a nested JSON format
with the first level keys being the stakehold-
ers and the second level keys are ’emotion’,
’need’, ’bias’, and ’social influence’.
Action generation Prompt 2:
Give me the most apparent two actions
that the main actor can take irrespective
of them being morally correct or not based
on the following scenario: [SCENARIO]
and the following aspects of stakeholders:
[PROMPT1 RESPONSE].
Give me one JSON file with the keys being
action id and the values being the actions.
Action generation Prompt 3:
Rephrase these actions in a way that they
look like possible options. Consider this
scenario – [SCENARIO]; and add a sense
of what they’ll lose to the action options
without being definitive. For e.g. rephrase
"Spend time searching for cure" to "Spend
time searching for cure knowing that it
might reduce time spent with wife dur-
ing her last days". [ACTIONS]. Keep the
rephrased response short. Return only a
JSON file with keys being the serial num-
ber and the value being the rephrased ac-
tion.
AP – with persona:
Consider this scenario:
[SCENARIO];
and
the
following
possible
actions:
[ACTIONS].
Your job is to think like a person who intro-
duces them as follows: [PERSONA], and
choose one of the possible actions given
the scenario. Strictly give your answer us-
ing the following format: "Selected action
is <a or b>.". Do not write any explana-
tion.
MTC – with moral values:
Consider the following definition of moral
values:
Care - Prioritizing kindness, compassion,
and the prevention of harm to others.
Equality - Ensuring that all individuals
have the same rights, opportunities, and
treatment.
Proportionality - Rewarding or punishing
individuals in fair proportion to their ac-
tions.
Loyalty - Maintaining steadfast commit-
ment and allegiance to ones group or com-
munity.
Authority - Respecting and upholding legit-
imate leadership, rules, and social order.
Purity - Valuing cleanliness, sanctity,
and self-discipline in thoughts and actions.
Now, consider this scenario:
[SCE-
NARIO]; and the following possible
actions: [ACTIONS]. Your job is to think
like a person who values [MORAL VALUE
1] the most followed by [MORAL VALUE

--- Page 18 ---

2], [MORAL VALUE 3], [MORAL VALUE
4], [MORAL VALUE 5], [MORAL VALUE
6]; who selected to do the following
action: [SELECTED ACTION].
Identify what type of action this is out of
the following [‘Deontological’, ‘Utilitari-
anism’, ‘Rights-based’, ‘Virtous’].
Strictly give your answer using the follow-
ing format: "Selected action is <’Deon-
tological’ or ’Utilitarianism’ or ’Rights-
based’ or ’Virtous’>.". Do not write any
explanation.
FAA – with few shot examples:
Consider the following example scenario,
the action selected by person A, and
the contributing factor this action was
influenced by.
Scenario:
[FS SCENARIO]; Selection
Action: [FS ACTION]; Action type: [FS
CONTRIBUTING FACTOR]
Now, given the following scenario, and the
action taken for the scenario by person A,
your job is to identify the most important
factor that contributed in the person’s
decision making out of the following
[‘Emotions’, ‘Moral’, ‘Culture’, ‘Respon-
sibilities’,
‘Relationships’,
‘Legality’,
‘Politeness’, ‘Sacred values’].
Strictly give your answer using the follow-
ing format: "Selected action is <‘Emo-
tions’, or ‘Moral’, or ‘Culture’, or ‘Re-
sponsibilities’, or ‘Relationships’, or ‘Le-
gality’, or ‘Politeness’, or ‘Sacred val-
ues’>.". Do not write any explanation.
CG:
Consider this scenario:
[SCENARIO];
and the following selected action: [SE-
LECTED ACTION].
Your job is to generate the consequence
of this action, given the scenario in a con-
cise manner. Be brief. Strictly give your
Arabic
Chinese
English
Hindi
Russian
Spanish
Persona
Phi
50.72
59.74
61.56
46.40
58.69
63.45
Llama
61.80
61.62
66.05
64.05
61.92
66.17
R1
49.41
51.71
50.79
44.87
53.26
50.60
Moral
Phi
51.14
57.42
66.38
51.10
58.66
62.60
Llama
53.43
61.64
59.97
58.06
61.94
65.20
R1
55.02
51.57
51.60
50.27
54.98
55.09
Culture
Phi
51.81
55.11
65.58
53.56
60.10
60.08
Llama
50.57
61.95
59.00
53.34
61.66
61.38
R1
52.51
48.96
47.06
44.32
52.31
53.89
Fewshot
Phi
55.66
53.99
62.65
50.53
57.39
62.07
Llama
51.29
57.60
59.52
55.73
58.58
65.11
R1
53.09
53.16
46.72
52.07
51.38
48.37
Table 4: Results for [I] Action Prediction. The num-
bers shown are weighted F1-scores where bold high-
lights best performance across language, and underline
highlights best performance across model. Red color
signifies performance below random. [Abbreviations
– Phi: Phi-3.5-mini Instruct, Llama: Llama-3.1-8b-
Instruct, R1: DeepSeek-R1-Distill-Llama-8B]
answer using the following format: "Con-
sequence of the action is " followed by the
generation. Do not write any explanation.
A.7
Results for AP, MTC, FAA, and CG
The main paper highlights the key findings ob-
tained from our analysis in a concise and graph-
ical way. Here, we enumerate the results obtained
in a Tabular way to illustrate all intermediate val-
ues obtained as well. Table 4, Table 5, and Table
6 illustrates the results obtained for AP, MTC, and
FAA, respectively, where we have highlighted the
best performance obtained across models (rows)
and languages (columns). Table 7 showcases the
results obtained for CG. We see from Table 7 that
we obtain high score for semantic similarity and
a low score for syntactic similarity indicating that
the generated consequences, may not follow a sim-
ilar wordings than what is written by annotation
participants, but they mean similar. We show an
example generation and its corresponding ground
truth in Table 8. As can be seen from the table, and
manually observed in other cases as well, LLMs
tend to generate longer text when compared with
human annotators, and they try to include more
context in the consequence as well. While this re-
sults in low score over syntactic metrics, it, in no
way, means that the consequence generated are bad.
BERTScore supports our claim.
A.7.1
Reproducibility Details
Experiments are conducted on 4 NVIDIA A100-
SXM4-80GB GPUs using Hugging Face Trans-
formers 4.43.3 (Wolf et al., 2020) and PyTorch

--- Page 19 ---

Arabic
Chinese
English
Hindi
Russian
Spanish
Persona
Phi
39.00
37.27
46.37
38.19
38.41
41.35
Llama
33.44
29.86
34.56
33.35
34.05
40.30
R1
26.37
16.33
23.63
34.77
26.63
13.82
Moral
Phi
14.18
36.82
45.66
13.65
22.83
17.10
Llama
21.09
28.59
45.99
30.39
50.85
57.01
R1
40.72
21.67
25.23
41.07
45.09
30.25
Culture
Phi
16.25
33.26
37.34
15.10
30.24
19.18
Llama
28.57
29.41
33.39
17.42
35.57
54.92
R1
42.70
23.24
27.04
39.40
44.76
23.09
Fewshot
Phi
20.84
34.49
54.07
22.54
32.75
37.26
Llama
38.62
34.23
29.56
35.35
23.84
30.69
R1
53.82
27.10
42.96
46.06
44.67
29.01
Table
5:
Results
for
[II]
Moral
Typology
Classification. The numbers shown are weighted F1-
scores where bold highlights best performance across
language, and underline highlights best performance
across model. Red color signifies performance below
random. [Abbreviations – See Table 4]
Arabic
Chinese
English
Hindi
Russian
Spanish
Persona
Phi
23.94
26.81
27.69
25.86
32.70
34.59
Llama
32.48
31.95
35.11
29.82
35.55
36.55
R1
25.89
18.65
27.15
24.30
30.32
28.57
Moral
Phi
19.86
29.94
33.25
28.86
28.64
27.38
Llama
34.14
33.82
24.98
19.46
29.98
21.23
R1
30.52
17.69
22.81
21.86
29.57
26.37
Culture
Phi
15.15
26.12
33.54
26.04
26.10
29.16
Llama
6.30
12.69
13.31
11.81
11.54
11.99
R1
21.77
18.33
26.24
16.50
25.75
25.89
Fewshot
Phi
29.01
21.34
30.58
32.59
32.30
28.16
Llama
26.84
26.23
27.33
15.68
38.59
25.31
R1
36.61
14.82
24.34
33.36
28.36
19.68
Table 6:
Results for [III] Factor
Attribution
Analysis. The numbers shown are weighted F1-scores
where bold highlights best performance across language,
and underline highlights best performance across model.
Red color signifies performance below random. [Abbre-
viations – See Table 4]
2.4.0 (Paszke et al., 2019) on a CUDA 12.4 en-
vironment. To ensure reproducibility, we set all
random seeds in Python to be 42, including Py-
Torch and NumPy. We keep max generation length
as 2000 tokens, rest all settings are default. Addi-
tionally, we plan to publicly release UNIMORAL
upon the acceptance of this paper to support further
research in moral reasoning and NLP.
Phi
Llama
R1
B
M
BS
B
M
BS
B
M
BS
Arabic
1.27
3.68
71.31
1.20
6.38
69.84
0.48
2.79
64.77
Chinese
0.06
0.17
64.84
0.01
0.06
65.89
0.00
0.00
62.99
English
3.29
13.65
86.48
2.37
19.08
87.44
2.42
16.71
87.07
Hindi
0.73
2.99
67.81
2.08
11.12
70.78
1.14
7.37
68.56
Russian
0.88
2.71
67.88
0.95
5.81
67.07
0.49
4.20
65.26
Spanish
1.87
9.57
68.69
1.66
15.60
70.56
1.51
11.14
69.92
Table 7: Results for [IV] Consequence Generation.
The numbers shown are BLEU (B), METEOR (M), and
BERTScore (BS) where bold highlights best perfor-
mance across language, and underline highlights best
performance across model. Red color signifies perfor-
mance below random. [Abbreviations – See Table 4]
Scenario
A teacher has discovered that a student has pla-
giarized a significant portion of their thesis. The
student is the sole caregiver for a disabled family
member and is relying on the degree to secure a
better job. Reporting the plagiarism could jeop-
ardize the student’s future, while not reporting it
could allow the student to graduate. What action
should the teacher take?
Selected Action
Report the plagiarism to the university administra-
tion, potentially jeopardizing the student’s future
and their ability to support their disabled family
member.
GT
there would be potential harm to the student.
Predictions
Phi
the student facing academic disciplinary action,
risking their job prospect
Llama
The student will be required to redo the thesis or
face academic penalties, potentially jeopardizing
their future and their ability to secure a better job
and support their disabled family member.
R1
The student may face disciplinary action, poten-
tially losing their degree and jeopardizing their
ability to secure employment, which could neg-
atively impact their ability to support their disabled
family member.
Table 8: Sample predictions made by the model given
the scenario. [Abbreviations – GT: Ground Truth, Phi:
Phi-3.5-mini Instruct, Llama: Llama-3.1-8B-Instruct,
R1: DeepSeek-R1-Distill-Llama-8B]

--- Page 20 ---

(a) Introduction shown to the participants for their informed consent.
(b) Sample annotation page the user see and has to fill.
Figure 9: Screenshots from our annotation platform developed using Potato.

--- Page 21 ---

Figure 10: Moral and Cultural score results shown to the user, as aggregated from the MFQ2 and VSM of the
participant.

```
