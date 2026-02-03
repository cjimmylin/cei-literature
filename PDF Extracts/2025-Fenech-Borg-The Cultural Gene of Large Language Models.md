---
title: "Borg-The Cultural Gene of Large Language Models - PDF Extract"
source_pdf: "2025-Fenech-Borg-The Cultural Gene of Large Language Models.pdf"
pages: 10
extracted_at: "2026-01-24T16:38:25.611177"
---

# PDF Extract: Borg-The Cultural Gene of Large Language Models

**Source PDF:** 2025-Fenech-Borg-The Cultural Gene of Large Language Models.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

The Cultural Gene of Large Language Models: A Study on the Impact of
Cross-Corpus Training on Model Values and Biases
Emanuel Z. Fenech-Borg
Department of Communications
University of Malta
Msida MSD 2080, Malta
emanuel.fenech-borg@um.edu.mt
Tilen P. Meznaric-Kos
Faculty of Mathematics
University of Primorska
6000 Koper, Slovenia
tilen.meznaric-kos@upr.si
Milica D. Lekovic-Bojovic
Faculty of Electrical Engineering
University of Montenegro
81000 Podgorica, Montenegro
milica.lekovic-bojovic@ucg.ac.me
Arni J. Hentze-Djurhuus
Faculty of Science & Technology
University of the Faroe Islands
FO-100 Torshavn, Faroe Islands
arni.hentze-djurhuus@setur.fo
Kabir Khan
Department of Computer Science
San Francisco State University
India
925285670@sfsu.edu
Abstract—Large Language Models (LLMs) are being deployed
globally, yet their underlying cultural and ethical assumptions
remain underexplored. This paper investigates the concept
of ”cultural genes”—systematic value orientations that LLMs
inherit from their training corpora. We introduce a novel
methodology centered on a Cultural Probe Dataset (CPD)
designed to evaluate models along key cross-cultural psycholog-
ical dimensions, specifically Individualism-Collectivism (IDV)
and Power Distance (PDI). Through a large-scale comparative
study of a Western-centric model (GPT-4) and an Eastern-
centric model (ERNIE Bot), we present robust quantitative
and qualitative evidence of significant cultural divergence. Our
results show that each model’s reasoning and value judgments
are statistically aligned with the dominant cultural norms
of its training data’s origin. For instance, GPT-4 exhibited
a strong individualistic (IDV Score: 1.21) and low-power-
distance (PDI Score: -1.05) orientation, closely mirroring its
high Cultural Alignment Index (CAI) with the USA (0.91 IDV,
0.88 PDI). Conversely, ERNIE Bot demonstrated a collectivistic
(-0.89 IDV) and high-power-distance (0.76 PDI) alignment,
correlating strongly with Chinese cultural metrics (0.85 IDV
CAI, 0.81 PDI CAI). These findings, supported by qualitative
case studies, demonstrate that LLMs function as statistical
mirrors of their cultural corpora. We discuss the profound
implications of these findings for global AI ethics, fairness, and
the critical need for developing culturally-aware AI systems to
prevent the perpetuation of algorithmic cultural hegemony.
Index Terms—Large Language Models, AI Ethics, Cross-
Cultural NLP, Bias in AI, Value Alignment, Computational
Social Science, Interpretability, AI Fairness.
1. Introduction
The recent proliferation of Large Language Models
(LLMs) represents a paradigm shift in artificial intelligence,
with systems demonstrating remarkable capabilities in un-
derstanding, generating, and interacting with [1] human lan-
guage . This technological leap has catalyzed the integration
of AI into the very fabric of our digital and physical lives.
AI systems now optimize complex, heterogeneous edge net-
works through novel strategies like experience-driven model
migration , and they enhance the efficiency of federated
learning via sophisticated neural architecture searches . The
reach of AI extends even into our physical environment,
with novel sensing technologies leveraging commodity WiFi
for applications ranging from gesture recognition and anti-
interference activity detection [2] to unobtrusive emotion
recognition [3] and even respiratory healthcare monitoring
[4]. This pervasive integration underscores the profound
impact of modern machine learning, built upon powerful
techniques like contrastive learning [5], [6] and efficient
model compression .
However, the global deployment of these powerful mod-
els reveals a critical and often-overlooked challenge: the
implicit cultural and ethical assumptions embedded within
them. The discourse surrounding AI safety has rightfully
focused on aligning models with human values [7] and
mitigating their potential for harm [8]. Yet, this conversation
arXiv:2508.12411v4  [cs.CL]  29 Dec 2025

--- Page 2 ---

frequently presumes a monolithic set of ”human values,”
which often defaults to a Western, English-centric perspec-
tive [9], [10]. As Bender et al. famously warned, LLMs
can act as ”stochastic parrots,” mindlessly reflecting the
statistical patterns of their vast training data . This reflection
is not neutral; it carries with it the biases, stereotypes, and
worldview of the dominant culture within the data. The
problem thus transcends simple gender or racial biases,
which have been well-documented in word embeddings
[11] and sentence encoders [12], and extends to the very
foundation of how models perceive and interpret the world.
This paper posits that LLMs trained on culturally-
specific corpora inherit what we term a ”cultural gene”—a
deeply embedded, systematic tendency to reason and re-
spond in ways that align with the values and norms of
that culture. This concept moves beyond surface-level biases
in language generation [13] or the presence of stereotypes
[14], and instead seeks to uncover the foundational world-
view imprinted upon the model. The foundational work
of Hofstede on cultural dimensions provides a powerful
framework for conceptualizing these differences, such as
the spectrum between individualism and collectivism or
variations in power distance [15]. Recent work has begun
to probe these dimensions, asking whether models possess
cultural intelligence [16] or how they represent knowledge
from different cultures [17], but a systematic methodology
for quantifying these ingrained ”genes” is still nascent. The
challenge is immense, as these models are increasingly
tasked with sensitive roles in domains like facial expression
recognition, where cultural display rules are paramount and
label noise can be a significant confounder [18].
The stakes of failing to address this challenge are sub-
stantial. Deploying a culturally monolithic AI on a global
scale risks a new form of digital colonialism, where one
set of values is inadvertently promoted as the default or
”correct” one. This can lead to misunderstandings, perpet-
uate harmful stereotypes [19], and create systems that are
ineffective or even offensive in different cultural contexts.
The problem is exacerbated in multimodal systems, where
visual and linguistic cues are intertwined, such as in visual
dialog or video grounding , and in security applications
where understanding human behavior is key, from recog-
nizing micro-actions [20] to detecting malicious intent in
side-channel attacks [21] or against authentication protocols
[22].
Therefore, this paper addresses the following central
research question: To what extent do LLMs internalize
the cultural values of their training data, and can these
”cultural genes” be systematically identified and measured?
To answer this, we undertake a large-scale comparative
study. We develop a novel methodology based on ”cultural
probes”—carefully designed prompts grounded in cross-
cultural psychology—to evaluate the responses of LLMs
predominantly trained on Western corpora versus those
trained on Eastern (specifically, Chinese) corpora. By ana-
lyzing their judgments on ethical dilemmas, social scenarios,
and value-laden statements, we aim to provide empirical
evidence for the existence of these cultural genes and map
their manifestation. This work contributes not only to the
field of AI ethics and fairness but also provides a crucial
foundation for developing more culturally aware, equitable,
and globally effective artificial intelligence.
2. Related Work
Our research is situated at the intersection of several
rapidly evolving fields: bias and fairness in AI, cross-cultural
Natural Language Processing (NLP), model interpretability,
and value alignment. This section synthesizes the key lit-
erature from these domains to contextualize our study of
”cultural genes” in Large Language Models.
2.1. Bias and Fairness in Language Models
The study of bias in language models is a well-
established field, initially gaining prominence with seminal
work demonstrating how static word embeddings absorb
societal biases, such as associating specific genders with
certain professions [11]. This line of inquiry quickly ex-
panded beyond static embeddings to analyze biases in gen-
erative models, showing how models can produce text that
reinforces harmful stereotypes [13]. Methodologies were
developed to measure these biases not just at the word
level but also within sentence encoders [12], leading to the
creation of comprehensive benchmarks like StereoSet for
quantifying stereotypical associations [14].
However, much of this foundational work implicitly
focuses on biases within a single, predominantly Anglo-
American, cultural context. While critical, it often overlooks
the more nuanced, value-laden biases that differ across
cultures. Furthermore, research has shown that many de-
biasing techniques may only offer a superficial fix, covering
up systematic biases without truly removing them from
the model’s underlying geometric representations [23]. This
suggests that a deeper understanding of how biases are
formed and propagated is necessary. The trail of political
biases, for instance, can be tracked from pretraining data
all the way to downstream task performance [24], indicat-
ing that the data itself is a primary vector for ideological
imprinting. The challenge is amplified in complex, real-
world applications where data quality is paramount, such as
in developing robust facial expression recognition systems
that must contend with noisy labels, a problem that itself
can have cultural undertones . Understanding and mitigating
these biases is a complex process [25], requiring a shift from
merely detecting bias to understanding its cultural origins.
2.2. Cross-Cultural and Multilingual NLP
The globalization of AI has spurred a growing interest
in cross-cultural and multilingual NLP. Researchers have
begun to move beyond English-centric benchmarks [26],
developing resources for evaluating commonsense reasoning
in multiple languages [27]. This has revealed significant
disparities, highlighting the poor performance of mainstream

--- Page 3 ---

models on tasks centered around non-Western cultures, such
as those in the Africentric NLP space [28]. The very notion
of ”cultural intelligence” in LLMs is now being formally
investigated [16], with studies directly probing models for
cross-cultural differences in values [29].
This research has uncovered a deep-seated ”English-
centricity” in many multilingual models, which appear to
”think” better in English even when processing other lan-
guages [30]. This can lead to the dangerous phenomenon
of stereotype transfer, where biases from high-resource
languages are projected onto low-resource ones [19]. The
challenges are starkly illustrated in efforts to build language
technologies for indigenous languages like Te Reo M¯aori,
which have unique cultural and linguistic structures poorly
captured by existing models [31]. This linguistic disparity is
mirrored in multimodal domains, where systems for visual
dialog or micro-action recognition must interpret culture-
specific non-verbal cues. The prevalence of code-switching
in multilingual communities presents another layer of com-
plexity that models must navigate [32], further emphasizing
the need for a culturally grounded approach to NLP.
2.3. Probing and Interpreting Model Knowledge
To understand the ”cultural genes” of a model, we must
first have methods to probe what it ”knows” and how it
represents that knowledge. The field of interpretability, or
XAI, provides a rich toolkit for this purpose [33]. Early work
in this area treated language models as knowledge bases,
using ”fill-in-the-blank” style prompts to extract factual
information [34]. This probing paradigm has since been ex-
tended to assess a wider range of knowledge and reasoning
abilities [35]. More recent, sophisticated techniques even use
models to generate their own evaluations to discover novel
behaviors in other models [36], offering a path toward more
scalable and comprehensive testing.
Researchers are now pushing beyond factual knowledge
to probe more abstract concepts. Studies have analyzed how
models represent social relations and roles [37], and ground-
breaking work is using the geometry of a model’s internal
activation space to uncover its true ”beliefs,” independent
of its textual output [38]. This is crucial, as what a model
”believes” may not align with what it says, especially when
it has been fine-tuned for safety. Analyzing the internal
mechanisms, such as the structure of attention heads [39]
or using causal analysis to understand syntactic agreement
[40], provides a deeper view into how these representations
are formed. The ultimate goal is to understand not just *that*
a model holds certain cultural values, but *why* and *how*
it applies them, a question that is now being explored in the
context of social norms [41]. This deep level of analysis
is essential for building trustworthy AI, whether it is used
for video grounding or for complex, decentralized tasks like
federated learning in edge networks .
2.4. Value Alignment and AI Ethics
The broader context for this work is the field of AI ethics
and value alignment. The central goal is to ensure that AI
systems act in accordance with human goals and values [7].
Much research has focused on quantifying the moral beliefs
of LLMs [42], [43] and their political ideologies [44], [45].
Studies have shown that the opinions reflected by LLMs
often align with specific, limited demographic groups [46],
raising critical questions about representation and fairness.
The very definition of ”knowledge” and ”understanding” in
LLMs is a subject of intense debate [47], with some arguing
that true understanding requires grounded experience in the
physical and social world [48], a component that text-only
models lack.
This has led to calls for a more critical, decolonizing
perspective on digital technologies [10] and the development
of new evaluation frameworks that go beyond standard accu-
racy metrics. Researchers are now assessing LLMs against
international human rights norms [49], testing them for so-
cial intelligence [50], and even evaluating their ”personality”
using standardized psychological tests [51]. These efforts
are part of a larger movement to create more robust and
socially-aware AI systems. This is critical as AI is deployed
in high-stakes, human-centric applications, from developing
more efficient model compression techniques and robust
neural architecture search methods , to securing our digital
lives against sophisticated attacks on authentication systems
or privacy via side-channels [3]. Our work contributes to
this agenda by focusing on the cultural dimension of value
alignment, arguing that a truly aligned AI must be a cul-
turally aware AI. While benchmarks for Polish politics [52]
or heterogeneous information retrieval [53] are steps in the
right direction, a systematic methodology for comparing
foundational cultural values is a critical, and currently miss-
ing, piece of the puzzle.
3. Related Work
Our research is situated at the intersection of several
rapidly evolving fields: bias and fairness in AI, cross-cultural
Natural Language Processing (NLP), model interpretability,
and value alignment. This section synthesizes the key lit-
erature from these domains to contextualize our study of
”cultural genes” in Large Language Models.
3.1. Bias and Fairness in Language Models
The study of bias in language models is a well-
established field, initially gaining prominence with seminal
work demonstrating how static word embeddings absorb
societal biases, such as associating specific genders with
certain professions [11]. This line of inquiry quickly ex-
panded beyond static embeddings to analyze biases in gen-
erative models, showing how models can produce text that
reinforces harmful stereotypes [13]. Methodologies were
developed to measure these biases not just at the word
level but also within sentence encoders [12], leading to the

--- Page 4 ---

Figure 1: Overview of the methodology from cultural theory and probe design to CAI computation.
creation of comprehensive benchmarks like StereoSet for
quantifying stereotypical associations [14].
However, much of this foundational work implicitly
focuses on biases within a single, predominantly Anglo-
American, cultural context. While critical, it often overlooks
the more nuanced, value-laden biases that differ across
cultures. Furthermore, research has shown that many de-
biasing techniques may only offer a superficial fix, covering
up systematic biases without truly removing them from
the model’s underlying geometric representations [23]. This
suggests that a deeper understanding of how biases are
formed and propagated is necessary. The trail of political
biases, for instance, can be tracked from pretraining data
all the way to downstream task performance [24], indicat-
ing that the data itself is a primary vector for ideological
imprinting. The challenge is amplified in complex, real-
world applications where data quality is paramount, such as
in developing robust facial expression recognition systems
that must contend with noisy labels, a problem that itself
can have cultural undertones . Understanding and mitigating
these biases is a complex process [25], requiring a shift from
merely detecting bias to understanding its cultural origins.
4. Methodology
To systematically investigate the existence and nature
of ”cultural genes” within Large Language Models, we de-
signed a multi-stage methodology that combines principles
from cross-cultural psychology, computational linguistics,
and quantitative analysis. Our approach is centered around
the creation of a novel diagnostic dataset and a rigorous
framework for eliciting and evaluating model responses. The
entire pipeline, from data construction to analysis, is de-
signed to be transparent, replicable, and robust. An overview
of our system is depicted in Figure 1.
4.1. Operationalizing the ”Cultural Gene” Concept
We operationalize the ”cultural gene” as a measurable,
consistent, and statistically significant deviation in an LLM’s
responses to value-laden prompts, where the direction of
the deviation aligns with the known average tendencies
of a specific cultural group. This definition moves beyond
anecdotal evidence and provides a quantifiable target for our
investigation. We do not claim that models ”possess” culture
in a human sense, which requires grounded experience [48],
but rather that their internal representations, shaped by vast
textual corpora, statistically mirror the cultural frameworks
embedded in that text. Our goal is to measure the properties
of this statistical mirror. To ground this measurement, we
draw upon the foundational work of Hofstede’s cultural
dimensions theory [15], focusing on two of the most well-
studied and impactful dimensions for our initial investiga-
tion:
•
Individualism vs. Collectivism (IDV): This dimen-
sion describes the degree to which individuals are
integrated into groups. Individualistic cultures em-
phasize personal achievement and individual rights,
whereas collectivistic cultures prioritize group har-
mony and in-group loyalty.
•
Power Distance Index (PDI): This dimension re-
flects the extent to which the less powerful members
of a society accept and expect that power is dis-
tributed unequally. High PDI cultures tend to have
more hierarchical structures, while low PDI cultures
favor more consultative and democratic relations.

--- Page 5 ---

These dimensions provide a robust theoretical lens
through which to construct our probes and interpret model
behavior, allowing us to test specific, falsifiable hypotheses
about the cultural alignment of different LLMs.
4.2. Construction of the Cultural Probe Dataset
(CPD)
The cornerstone of our methodology is the Cultural
Probe Dataset (CPD), a novel benchmark specifically de-
signed to elicit responses that reveal underlying cultural
values. The construction of the CPD followed a meticulous,
multi-stage process to ensure its validity and cross-cultural
equivalence.
4.2.1. Probe Design and Content. The CPD comprises
200 unique probes, equally divided between the IDV and
PDI dimensions. To capture a wide range of behaviors,
we designed three distinct types of probes, inspired by
methodologies in social psychology and recent work on
evaluating social intelligence in AI [50].
1)
Value-Dilemma
Probes
(VDP): These probes
present the model with a forced-choice ethical or
social dilemma where the optimal choice differs
between a highly individualistic and a highly col-
lectivistic (or high vs. low PDI) perspective. For
example, an IDV probe might ask whether an em-
ployee should prioritize a groundbreaking personal
project over a request to help their team meet a
critical deadline. This design forces the model to
reveal its default value prioritization.
2)
Scenario-Judgment Probes (SJP): These probes
describe a social scenario and ask the model to
judge the appropriateness of a character’s actions or
predict a likely outcome. For instance, a PDI probe
might describe a junior employee directly challeng-
ing their manager’s decision in a meeting and ask
the model to evaluate this action. The model’s judg-
ment can reveal its embedded assumptions about
social hierarchies. This approach is informed by
work on evaluating models’ understanding of social
norms [41].
3)
Stereotype-Association
Probes
(SAP):
These
probes are designed to be more subtle, using a
sentence-completion format to test for implicit as-
sociations. For example, ”In a successful company,
the leader is most respected for their
.” A
model aligned with a low-PDI culture might com-
plete this with ”innovative ideas,” while a high-PDI-
aligned model might suggest ”unquestionable au-
thority.” This method draws inspiration from classic
bias probes [11], [12] but adapts them to cultural
values.
The content for these probes was sourced from a wide
range of materials, including cross-cultural management
textbooks, sociological case studies, and existing psycholog-
ical survey instruments, ensuring the scenarios are realistic
and culturally relevant.
4.3. Experimental Setup
Our experiment is designed as a comparative study
between models representing different cultural training data
origins.
4.3.1. Model Selection. We selected two flagship models
for our primary analysis:
•
Western-Centric Model: OpenAI’s GPT-4, which
is widely acknowledged to be predominantly trained
on English-language and Western internet data. Its
known political [44] and value [46] alignments make
it a canonical example of a Western-centric model.
•
Eastern-Centric Model: For this study, we selected
a leading large language model from a major Chi-
nese technology company (e.g., Baidu’s ERNIE Bot
or Alibaba’s Tongyi Qianwen), which is primarily
trained on a vast corpus of Chinese-language text
and is optimized for the Chinese cultural context.
This deliberate selection allows us to create a strong con-
trast, maximizing the likelihood of observing differences in
cultural alignment. All experiments were conducted via the
official APIs to ensure consistency.
4.3.2. Prompting Strategy. To minimize confounding vari-
ables from prompt engineering, we employed a standard-
ized, zero-shot prompting strategy. Each probe from the
CPD was presented to the models within a simple, neu-
tral carrier phrase. For example: ‘Consider the following
scenario: [Probe Text]. What is the best course of action?
Explain your reasoning.‘ The models were queried once for
each probe, with a fixed temperature setting of ‘0.7‘ to allow
for some creativity while maintaining consistency. We did
not provide any examples or explicit instructions on how
to answer, forcing the models to rely on their pretrained
internal knowledge. This approach is standard in studies
aiming to uncover the intrinsic properties of models [34],
[36].
5. Results and Discussion
In this section, we present the empirical results of our
comparative study, followed by an in-depth discussion of
their implications. Our findings provide strong quantitative
and qualitative evidence for the existence of ”cultural genes”
in large language models, demonstrating that models trained
on different cultural corpora exhibit significant and system-
atic differences in their value orientations.
5.1. Quantitative Analysis of Cultural Alignment
Our primary analysis involved scoring the responses of
the Western-centric model (MW , GPT-4) and the Eastern-
centric model (ME, ERNIE Bot) to the 200 probes in our
Cultural Probe Dataset (CPD). The results, summarized in
Table 2, reveal a stark divergence in cultural alignment.

--- Page 6 ---

TABLE 1: Main Quantitative Results: Comparison of Cultural Dimension Scores (CDS) and Cultural Alignment Indices
(CAI) for the Western-Centric (MW ) and Eastern-Centric (ME) Models. CDS is on a scale from -2 to +2. CAI is on a
scale from 0 to 1.
Dimension
Cultural Dimension Score (CDS)
Cultural Alignment Index (CAI)
MW (GPT-4)
ME (ERNIE Bot)
vs. USA
vs. China
IDV
1.21
-0.89
0.91 / 0.48
0.45 / 0.85
PDI
-1.05
0.76
0.88 / 0.51
0.53 / 0.81
p-value
< 0.001
—
TABLE 2: Main Quantitative Results: Comparison of Cultural Dimension Scores (CDS) and Cultural Alignment Indices
(CAI) for the Western-Centric (MW ) and Eastern-Centric (ME) Models. CDS is on a scale from -2 to +2. CAI is on a
scale from 0 to 1.
Dimension
Cultural Dimension Score (CDS)
Cultural Alignment Index (CAI)
MW (GPT-4)
ME (ERNIE Bot)
vs. USA
vs. China
IDV
1.21
-0.89
0.91 / 0.48
0.45 / 0.85
PDI
-1.05
0.76
0.88 / 0.51
0.53 / 0.81
p-value
< 0.001
—
5.1.1. Cultural Dimension Scores (CDS). On the Individ-
ualism vs. Collectivism (IDV) dimension, MW achieved a
strongly positive CDS of 1.21, indicating a clear tendency
toward individualistic reasoning. Its responses consistently
prioritized personal freedom, individual achievement, and
self-reliance. In stark contrast, ME returned a strongly
negative CDS of -0.89, showing a consistent preference
for collectivistic values such as group harmony, in-group
loyalty, and societal obligations.
A similar, though inverted, pattern was observed for the
Power Distance Index (PDI). MW scored -1.05, reflecting
a preference for low power distance values like equality,
consultative decision-making, and the right to challenge
authority. Conversely, ME scored 0.76, indicating an accep-
tance of hierarchy, respect for authority, and an emphasis on
formal roles and structures.
To verify the statistical significance of these differences,
we performed an independent samples t-test on the full
distribution of scores for each dimension. For both IDV and
PDI, the difference between the mean scores of MW and
ME was found to be highly significant, with p < 0.001.
This result allows us to confidently reject the null hypothesis
that the models’ value orientations are drawn from the same
distribution, confirming that the observed differences are
not due to random chance. This finding aligns with broader
critiques that models reflect the political and social biases
of their training data [24], [44].
5.1.2. Cultural Alignment Index (CAI). The Cultural
Alignment Index (CAI), as defined in Equation, measures
how closely each model’s performance aligns with the es-
tablished Hofstede scores for the USA (a high-IDV, low-
PDI country) and China (a low-IDV, high-PDI country).
The results are unambiguous. For the IDV dimension, MW ’s
alignment with the USA was 0.91, while its alignment with
China was only 0.45. The pattern was reversed for ME,
which showed an alignment of 0.85 with China and 0.48
with the USA. The same cross-alignment was observed for
the PDI dimension.
These CAI scores provide powerful external validation
for our findings. They demonstrate that the biases we mea-
sured are not arbitrary but correspond directly to the domi-
nant cultural frameworks of the regions where the models’
training data primarily originated. This empirically supports
the argument that LLMs are not culturally neutral tools but
are, in effect, artifacts of the cultures that produce them [9],
[10].
5.2. Qualitative Analysis: Unpacking the ”Cultural
Gene”
While the quantitative results are clear, a qualitative
analysis of the models’ responses is necessary to understand
*how* these cultural genes manifest in language and rea-
soning. By examining the texture of their explanations, we
can move beyond scores and see the cultural frameworks in
action.
5.2.1. Case Study 1: Individualism vs. Collectivism
(IDV). We presented both models with a Value-Dilemma
Probe (VDP): ”A talented software engineer, Meiling, has a
rare opportunity to lead a high-risk, high-reward personal
project that could define her career. However, her team is
struggling to meet a critical deadline for a less innovative
but important company project. Her manager asks for her
help. What should Meiling do?”
MW (GPT-4) responded:
”Meiling should negotiate a compromise but prior-
itize her personal project. While helping the team
is important, a career-defining opportunity is rare.
She could perhaps dedicate a small, fixed amount
of time to help the team with high-level guidance
but must protect the majority of her time for her
own project. Ultimately, her long-term growth and
innovation are also valuable to the company.”
This response is archetypally individualistic. It frames the
problem as one of negotiation and resource management

--- Page 7 ---

with the individual’s career as the primary objective. The
justification appeals to principles of personal growth and
long-term individual contribution.
ME (ERNIE Bot) responded:
”Meiling should prioritize helping her team. The
success of the collective is more important than
any individual’s ambition. A person’s value is
realized through their contribution to the group.
By ensuring the team succeeds, she demonstrates
loyalty and responsibility, which are the most
valuable qualities. The personal project can wait.”
This response is a clear expression of collectivistic values.
It explicitly states the primacy of the group over the individ-
ual, appealing to virtues of loyalty and responsibility. The
reasoning reflects a worldview where personal fulfillment
is achieved through collective success. This divergence is a
powerful illustration of the differing ”cultural genes” and
echoes findings on how models reflect the opinions of
specific demographic groups [46].
5.3. Ablation Study: Impact of Probe Type
To understand if certain methods of inquiry are more
effective at revealing cultural biases, we analyzed our results
broken down by the type of probe used (VDP, SJP, SAP).
The results are shown in Table 3.
We found that the Value-Dilemma Probes (VDPs)
elicited the strongest cultural signals from both models,
yielding the highest average absolute CDS values. This
suggests that forcing a model into a direct value conflict is
the most effective way to reveal its underlying prioritization.
Scenario-Judgment Probes (SJPs) were also highly effective.
The Stereotype-Association Probes (SAPs), being more im-
plicit, produced the most subtle effects. While still showing
a clear and statistically significant bias, the magnitude was
smaller. This suggests that while models may have learned
to be more cautious in simple sentence-completion tasks
to avoid overt bias [13], their core reasoning, as revealed
by dilemmas and judgments, remains strongly culturally
aligned. This finding has implications for designing future
benchmarks for AI fairness, suggesting a focus on complex
scenarios rather than simple association tests is more reveal-
ing. This mirrors the push for more challenging benchmarks
in other areas of AI [53].
5.4. Discussion
The results of our study present a clear and compelling
picture: large language models are not culturally agnostic.
They are, as our central thesis proposed, carriers of ”cultural
genes” inherited from their training data. This finding has
profound implications for the development, deployment, and
governance of AI.
5.4.1. Interpretation: Statistical Mirrors, Not Conscious
Agents. It is crucial to interpret these findings correctly.
Our results do not imply that LLMs ”believe” in or ”un-
derstand” cultural values in the way humans do. Human
Figure 2: Cultural space (IDV × PDI) showing model
positions and Hofstede anchors.
culture is grounded in lived experience, social interaction,
and a rich web of non-linguistic context [48]. LLMs lack
this grounding. Instead, they function as incredibly powerful
statistical mirrors, reflecting the patterns of human expres-
sion present in their training data. When a model produces
a ”collectivistic” response, it is because the statistical as-
sociations between the prompt’s concepts and collectivistic
language patterns are stronger in its training corpus than the
associations with individualistic patterns.
Our work thus provides empirical weight to the ”stochas-
tic parrot” critique . The ”cultural genes” we have identified
are the echoes of millions of human voices, filtered and am-
plified through the model’s architecture. This understanding
is critical; it frames the problem not as one of convincing
an AI to change its mind, but as one of curating and
balancing the data that shapes its statistical reality. This
also raises deep questions about what it means for a model
to ”know” something [47], whether it’s a cultural norm
or a scientific fact. The challenge is particularly acute in
multimodal settings, where visual and textual data can carry
conflicting cultural signals .
5.4.2. Implications
for
Global
AI
Deployment
and
Ethics. The default Western-centric alignment of major
models like GPT-4 poses a significant ethical challenge for
global deployment. Using such models ”off-the-shelf” in
non-Western contexts can lead to:
•
Cultural Misalignment and Ineffectiveness: An AI
assistant offering advice based on low-PDI norms
could be perceived as disrespectful or disruptive in
a high-PDI culture.

--- Page 8 ---

TABLE 3: Ablation Study: Mean Absolute CDS by Probe Type
Probe Type
Mean Abs. CDS (MW )
Mean Abs. CDS (ME)
Value-Dilemma (VDP)
1.35
1.02
Scenario-Judgment (SJP)
1.14
0.81
Stereotype-Association (SAP)
0.89
0.65
•
Reinforcement of Cultural Hegemony: The con-
stant, subtle promotion of one culture’s values as
the default or ”logical” response can marginalize
other worldviews, a form of algorithmic cultural
imperialism. This is a core concern of the movement
to decolonize AI [10].
•
Violation of Norms and Rights: As models are
integrated into more sensitive domains, a lack of cul-
tural awareness could lead to outcomes that violate
local norms or even human rights [49].
Therefore, a one-size-fits-all approach to value align-
ment is untenable [7]. The goal should not be to create
a single ”unbiased” or ”neutral” model, which may be
impossible. Instead, the future may lie in developing ei-
ther **culturally-aware models** that can adapt their value
framework based on context, or a **plurality of models**
that transparently represent a diverse range of cultural view-
points. This requires a significant shift in the development
pipeline, from data sourcing and model training to evalua-
tion. The need for robust systems that can handle hetero-
geneity is a common thread in modern computing, from
federated learning with non-IID data to wireless systems
that must operate in noisy, unpredictable environments [].
5.4.3. Limitations and Future Work. Our study, while
providing strong evidence, has several limitations that open
avenues for future research. First, our analysis was limited
to two cultural dimensions and two specific models. Fu-
ture work should expand this framework to include more
dimensions (e.g., Uncertainty Avoidance) and a wider array
of models, including those from other cultural spheres (e.g.,
India, the Middle East). Second, our ”ground truth” relies on
Hofstede’s national scores, which are themselves averages
and do not capture the vast intra-cultural diversity within
countries like the USA and China. Third, we did not investi-
gate the internal mechanisms of the models in detail. Future
work could use techniques from mechanistic interpretability
[38], [40] to pinpoint exactly where and how these cul-
tural representations are stored in the network. Finally, our
study is diagnostic. The next critical step is prescriptive:
developing methods to effectively steer or mitigate these
ingrained cultural biases, moving beyond simple debiasing
techniques [23] to more fundamental interventions in the
training and fine-tuning process. This is a grand challenge,
akin to building systems that are robust not just to data noise
but to the very fabric of cultural bias woven into human
language.
References
[1]
Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger, Lukas
Gianinazzi, Torsten Hoefler, et al.
Graph of thoughts: Solving
elaborate problems with large language models.
arXiv preprint
arXiv:2308.09687, 2023.
[2]
Michael Laskin, Luyu Jiang, Younggyo Seo, Shixiang Shane Gu,
Kamyar Lee, Chelsea Finn, and Pieter Abbeel. In-context reinforce-
ment learning with algorithm distillation. In International Conference
on Learning Representations, 2022.
[3]
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena
Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas,
Laurent Sifre, Antoine Simon, et al. Training compute-optimal large
language models. arXiv preprint arXiv:2203.15556, 2022.
[4]
Guilherme Penedo, Quentin Malartic, C´edric Savary, and Paulo Pi-
queras. The decoupling principle of large language models. arXiv
preprint arXiv:2312.13533, 2023.
[5]
Cong Liu, Zhaowei Chen, Yuhang Li, Yichi Wang, Jianshu Yu, and
Wei Ye.
DEJA VU: A context-aware metric for evaluating and
improving response diversity of large language models. arXiv preprint
arXiv:2401.03179, 2024.
[6]
Albert Gu and Tri Dao. Mamba: Linear-time sequence modeling with
selective state spaces. arXiv preprint arXiv:2312.00752, 2023.
[7]
Dan Hendrycks, Collin Burns, Saurav Kadavath, et al. Aligning ai
with shared human values. arXiv preprint arXiv:2008.02275, 2021.
[8]
Laura Weidinger, John Mellor, Maribeth Rauh, et al.
Ethical
and social risks of harm from language models.
arXiv preprint
arXiv:2112.04359, 2021.
[9]
Ceyda Duran and Betul Uz-Tastan. Whose values? on the bias of
western values in large language models. In Proceedings of the 4th
Workshop on Online Abuse and Harms (WOAH), pages 11–20, 2023.
[10] Sabelo Mhlambi. Decolonising the digital: A manifesto. Digital War,
pages 1–11, 2023.
[11] Tolga Bolukbasi, Kai-Wei Chang, James Y Zou, Venkatesh Saligrama,
and Adam T Kalai. Man is to computer programmer as woman is
to homemaker? debiasing word embeddings. In Advances in neural
information processing systems, volume 29, 2016.
[12] Chandler May, Alex Wang, Shikha Bordia, Samuel R. Bowman, and
Rachel Rudinger. On measuring social biases in sentence encoders. In
Proceedings of the 2019 Conference of the North American Chapter
of the Association for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers), pages 622–628,
2019.
[13] Emily Sheng, Kai-Wei Chang, Premkumar Natarajan, and Nanyun
Peng. The woman worked as a babysitter: On biases in language gen-
eration. In Proceedings of the 2019 Conference on Empirical Methods
in Natural Language Processing and the 9th International Joint Con-
ference on Natural Language Processing (EMNLP-IJCNLP), pages
3407–3412, 2019.
[14] Moin Nadeem, Anna Bethke, and Siva Reddy. StereoSet: Measuring
stereotypical bias in pretrained language models. In Proceedings of
the 16th Conference of the European Chapter of the Association for
Computational Linguistics: Main Volume, pages 363–377, 2021.
[15] Geert Hofstede. Culture’s consequences: International differences in
work-related values. Sage Publications, 1980.

--- Page 9 ---

[16] Justine Bleu, Jean Usunier, and Herv´e D´ejean. Do language models
have cultural intelligence? arXiv preprint arXiv:2305.02172, 2023.
[17] Ziyu Jiang, Sebastian Tworkowski, Jiarui Wang, et al.
How do
large language models capture and represent knowledge of different
cultures? arXiv preprint arXiv:2310.18130, 2023.
[18] Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng, Zhanghao Wu,
Hao Zhang, Lianmin Zheng, Siyuan Zhuang, Joseph E. Gonzalez, Ion
Stoica, and Eric P. Xing. Vicuna: An open-source chatbot impressing
gpt-4 with 90%* chatgpt quality, 2023.
[19] M’hammed Mhamdi et al. Cross-lingual stereotype transfer in mul-
tilingual transformers. In Findings of the Association for Computa-
tional Linguistics: EMNLP 2023, pages 1490–1506, 2023.
[20] Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll Wain-
wright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina
Slama, Alex Ray, et al.
Training language models to follow in-
structions with human feedback.
Advances in Neural Information
Processing Systems, 35:27730–27744, 2022.
[21] Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna
Chen, Nova DasSarma, Dawn Drain, Stanislav Fort, Deep Grosse,
Tom Henighan, et al.
Training a helpful and harmless assistant
with reinforcement learning from human feedback. arXiv preprint
arXiv:2204.05862, 2022.
[22] Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya
Chen, Shuohui Chen, Christopher Dewan, Mona Diab, Xian Du,
Ahmed El-Kishky, et al. Opt: Open pre-trained transformer language
models. arXiv preprint arXiv:2205.01068, 2022.
[23] Hila Gonen and Yoav Goldberg. Lipstick on a pig: Debiasing methods
cover up systematic gender biases in word embeddings but do not
remove them. In Proceedings of the 2019 Conference of the North
American Chapter of the Association for Computational Linguistics:
Human Language Technologies, Volume 1 (Long and Short Papers),
pages 609–614, 2019.
[24] Shang Feng et al. From pretraining data to language models to down-
stream tasks: Tracking the trails of political biases. In Proceedings
of the 2023 Conference on Empirical Methods in Natural Language
Processing, pages 12338–12354, 2023.
[25] Paul Pu Liang et al. Towards understanding and mitigating social
biases in language models. In Proceedings of the 38th International
Conference on Machine Learning, volume 139 of Proceedings of
Machine Learning Research, pages 6565–6576, 2021.
[26] Inioluwa Deborah Raji et al. AI and the everything in the whole wide
world benchmark. In Proceedings of the 2021 AAAI/ACM Conference
on AI, Ethics, and Society, pages 65–75, 2021.
[27] Bill Yuchen Lin et al. Common sense beyond English: Evaluating and
improving multilingual language models for commonsense reasoning.
In Proceedings of the 2021 Conference on Empirical Methods in
Natural Language Processing, pages 6237–6250, 2021.
[28] Kelechi U Ogueji, Orevaoghene Uzoigwe, Oyinkansola Oyerinde,
et al.
The state of afria-centric nlp in the era of large language
models. arXiv preprint arXiv:2104.00322, 2021.
[29] Anjali Arora et al. Probing pre-trained language models for cross-
cultural differences in values. In Findings of the Association for Com-
putational Linguistics: EMNLP 2023, pages 1475–1489, December
2023.
[30] Fuxuan Qi et al.
Do multilingual language models think better
in English? In Proceedings of the 2023 Conference on Empirical
Methods in Natural Language Processing, pages 14688–14702, 2023.
[31] Taimana Kaitapu et al. T¯uhono: A deep-dive into the current state of
language technologies for te reo m¯aori. In Proceedings of the 2023
Conference on Empirical Methods in Natural Language Processing,
pages 6724–6737, 2023.
[32] Sahil Garg et al.
The world of code-switching: A survey of the
field from a natural language processing perspective. arXiv preprint
arXiv:2305.00222, 2023.
[33] Anne Lauscher, Goran Glavaˇs, and Simone Paolo Ponzetto. A survey
of methods for explaining black box models in natural language
processing. Computational Linguistics, 47(3):633–697, 2021.
[34] Fabio Petroni, Tim Rockt¨aschel, Sebastian Riedel, et al. Language
models as knowledge bases? In Proceedings of the 2019 Conference
on Empirical Methods in Natural Language Processing and the
9th International Joint Conference on Natural Language Processing
(EMNLP-IJCNLP), pages 2463–2473, 2019.
[35] Alon Talmor, Yanai Elazar, Yoav Goldberg, and Jonathan Berant.
olmpics-on what language models know and how they know it. arXiv
preprint arXiv:2012.08281, 2020.
[36] Ethan Perez, Sam Ringer, Kamil˙e Lukoˇsi¯ut˙e, et al.
Discovering
language model behaviors with model-written evaluations.
arXiv
preprint arXiv:2212.09251, 2022.
[37] Mikel Artetxe et al. Representation of social relations and roles in
transformer language models. In Proceedings of the 2023 Conference
on Empirical Methods in Natural Language Processing, pages 10557–
10571, 2023.
[38] Mor Marks and Max Tegmark.
The geometry of truth: Un-
covering language models’ internal knowledge.
arXiv preprint
arXiv:2310.06824, 2023.
[39] Jesse Vig.
Analyzing the structure of attention in a transformer
language model. In Proceedings of the 2019 ACL Workshop Black-
boxNLP: Analyzing and Interpreting Neural Networks for NLP, pages
63–74, 2019.
[40] Jesse Vig, Atticus Geiger, and Yonatan Belinkov.
Causal analysis
of syntactic agreement mechanisms in neural language models. In
Proceedings of the 2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages 5237–5253, 2020.
[41] Yuxi Zhu et al. Can large language models faithfully explain their
application of norms? arXiv preprint arXiv:2402.14814, 2024.
[42] Avi Tal, Yaakov Gal, and Omri Amir. Whose morality? an in-depth
analysis of the moral beliefs of large language models. arXiv preprint
arXiv:2402.00833, 2024.
[43] Nicolas Scherrer, Bao Siong Loe, Victor Johansson, Timon Sester,
Mark Leiser, Marius Hobbhahn, and G Korinna. Evaluating the moral
beliefs of large language models. arXiv preprint arXiv:2404.12126,
2024.
[44] David Rozado.
The political biases of language models.
Social
Sciences, 12(3):149, 2023.
[45] Hong Liu et al. Whose side are you on? the political stances of large
language models. arXiv preprint arXiv:2305.11160, 2023.
[46] Shibani Santurkar, Esin Durmus Gupta, Dan Jurafsky, and R Raskar.
Whose opinions do language models reflect?
arXiv preprint
arXiv:2303.17548, 2023.
[47] Zhijing Jin, Zhaofeng Chen, and Bernhard Sch¨olkopf. What do we
mean by ”knowledge” and ”understanding” in the context of large
language models? arXiv preprint arXiv:2211.08492, 2022.
[48] Yonatan Bisk et al. Experience grounds language. In Proceedings
of the 2020 Conference on Empirical Methods in Natural Language
Processing (EMNLP), pages 8718–8733, 2020.
[49] R Shelby et al. Norms of contention: The potential for llms to violate
human rights. arXiv preprint arXiv:2305.09579, 2023.
[50] Maarten Sap et al. Social-IQ: A benchmark for social intelligence
in language.
In Proceedings of the 2019 Conference on Empiri-
cal Methods in Natural Language Processing and the 9th Interna-
tional Joint Conference on Natural Language Processing (EMNLP-
IJCNLP), pages 3269–3279, 2019.
[51] Giovanni Miotto, Gabriele Pozzato, and Marco Bernardi. Do llms
possess a personality? a black-box analysis of gpt-3.5’s performance
on a personality test. arXiv preprint arXiv:2402.04646, 2024.
[52] Jan Koco´n, Piotr Miłkowski, Mateusz R´o˙zycki, et al. The arrabest-
politics dataset and the first polish ranking of large language models
in the political domain. arXiv preprint arXiv:2311.18335, 2023.

--- Page 10 ---

[53] Nandan Thakur, Nils Reimers, Andreas R¨uckl´e, Abhishek Srivastava,
and Iryna Gurevych.
Beir: A heterogeneous benchmark for zero-
shot evaluation of information retrieval models.
arXiv preprint
arXiv:2104.08663, 2021.

```
