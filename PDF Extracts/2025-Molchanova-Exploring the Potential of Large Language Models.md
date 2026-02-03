---
title: "Exploring the Potential of Large Language Models - PDF Extract"
source_pdf: "2025-Molchanova-Exploring the Potential of Large Language Models.pdf"
pages: 12
extracted_at: "2026-01-24T16:38:31.149285"
---

# PDF Extract: Exploring the Potential of Large Language Models

**Source PDF:** 2025-Molchanova-Exploring the Potential of Large Language Models.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

Exploring the Potential of Large Language Models to Simulate Personality
Maria Molchanova*
MIPT, Russia
molchanova.ma.63@gmail.com
Anna Mikhailova*
MIPT, Russia
anna.micj@gmail.com
Anna Korzanova
MIPT, Russia
korzanova.av@mipt.ru
Lidiia Ostyakova
MIPT, Russia
HSE University, Russia
ostyakova.ln@gmail.com
Alexandra Dolidze
MIPT, Russia
HSE University, Russia
dolidze.aa@mipt.ru
Abstract
With the advancement of large language mod-
els (LLMs), the focus in Conversational AI has
shifted from merely generating coherent and
relevant responses to tackling more complex
challenges, such as personalizing dialogue sys-
tems. In an effort to enhance user engagement,
chatbots are often designed to mimic human
behaviour, responding within a defined emo-
tional spectrum and aligning to a set of values.
In this paper, we aim to simulate personal traits
according to the Big Five model with the use
of LLMs. Our research showed that generating
personality-related texts is still a challenging
task for the models. As a result, we present a
dataset of generated texts with the predefined
Big Five characteristics and provide an analyt-
ical framework for testing LLMs on a simula-
tion of personality skills.
1
Introduction
After their breakthrough in NLP, large language
models (LLMs) continue to improve, becoming
integral to the modern digital world. Their abil-
ity to generate coherent and contextually relevant
responses finds application in various fields, includ-
ing dialogue systems (Yi et al., 2024).
LLMs, with their ability to generate human-like
text, open up new possibilities for conversational
agents, making interactions with users more en-
gaging. However, to boost this emotional connec-
tion between AI assistants and humans, dialogue
systems need to be more personalized taking into
account individual characteristics of users. Prompt-
ing LLM-based multi-agent systems with person-
ality can significantly enhance their capability to
converse with empathy (Rashkin et al., 2018).
Imitating personality with LLMs may be a good
way to develop usable AI assistants that perfectly
align with users needs (Tseng et al., 2024). In-
corporating the desired character in assistants for
*These authors contributed equally to this work.
each user can personalize user experience, prolong-
ing dialogues and making them more lively. Thus,
adjusting a bot personality to suit a user’s emo-
tional state can enhance user satisfaction with dia-
logue systems (Prendinger et al., 2005; Polzin and
Waibel, 2000). In LLM-based multi-agent systems,
agents can take on different roles with description
of their personality. For example, such agents can
be applied to the gaming industry, portraying play-
ers with different characteristics, or in business
applications, where agents can take on the roles of
customer-oriented employees to provide guidance
in certain fields of expertise (Guo et al., 2024).
The current study aims at providing evidence on
how different LLMs may be prompted with Big
Five personality model, and how consistent they
are in the imitated personalities. We explore not
only how well LLMs associate personality traits
with corresponding behavior, but also their knowl-
edge about language patterns and life goals related
to the prompted personality. As a result of our
study we develop an open-source analytical frame-
work to encourage further research in personality
simulation by LLMs.
2
Related Work
Big Five Personality Model
The Big Five per-
sonality model is considered to be a valid approach
to evaluate one’s personality traits due to its reliabil-
ity and practicality (John et al., 2008). Compared
to MBTI personality measurement, the Big Five
model has proven its validity across different pop-
ulations (Schweiger, 1985). According to the Big
Five model, an individual’s personality can be rep-
resented along five dimensions, namely Extraver-
sion, Neuroticism, Agreeableness, Conscientious-
ness, and Openness to Experience. Each dimension
is a dichotomy with low and high trait manifes-
tations. Recent research adds a new dimension,
Honesty-Humility, to the original model (Costa
arXiv:2502.08265v1  [cs.CL]  12 Feb 2025

--- Page 2 ---

and McCrae, 2008).
Initially, the Big Five model is based on the lin-
guistic hypothesis, claiming that the natural lan-
guage descriptors of person’s traits, moods, and
characteristics can be generalized and represented
as a personality model. Subsequently, there appear
also psychological questionnaires, namely those
as TDA (Goldberg, 1992), NEO (Costa and Mc-
Crae, 1992), and BFI (John, 1991), that help to
determine personality traits by answering a prede-
fined set of questions. All the questionnaires show
respectable validity and reliability, but BFI ques-
tionnaire stands out for question formulation (John
et al., 2008). The Big Five model is critiqued for
lacking detailed personality classification, as all
traits seem to be abstract (John et al., 2008); more-
over, the model only includes traits linked to natural
language analysis, neglecting non-social personal
traits (Trofimova, 2014). Nevertheless, these char-
acteristics can be advantageous in the context of
LLMs, as they can be utilized to generate a person-
ality in natural language modeling using the Big
Five model.
Personality of Large Language Models
The re-
search devoted to personality in LLMs focuses on
two main aspects, including internal LLM person-
ality and LLM-prompted personality. LLM person-
ality is usually analyzed by leveraging the Big Five
questionnaire results, LLM-generated text analysis
(both linguistic and psychological), or automated
text classification for the Big Five traits.
Studies
on
LLM
personalities,
e.g.,
(Sorokovikova et al., 2024),
provide statis-
tics on how LLMs answer the different the Big
Five questionnaires (IPIP-NEO, BFI-44).
This
should reveal the LLM hidden personality. The
findings seem to be quiet impressive, as they
portray GPT-4 and Mixtral as open, agreeable,
conscientious, extroverted and emotionally stable
agents capable of engaging conversations. How-
ever, other studies disagree with this conclusion, as
the questionnaire results do not seem to reflect real
model personality and do not help to predict model
actions (Ai et al., 2024).
Studies on how we can induce personality in
LLMs demonstrate different ways a personality
can be prompted to an LLM. Some approaches sug-
gest describing personality based on the personal
facts (e.g., providing the LLM with a personality
description from PersonaChat dataset) or based
on descriptions of each the Big Five characteris-
tic (Serapio-García et al., 2023; Liu et al., 2024).
The other research also tests personality simulation
through text generation (Jiang et al., 2024) or sen-
tence completion (Hilliard et al., 2024). Personality
modeling is usually affected by the model size, as
it is stated in all above-described studies.
3
Methods
Based on previous research, LLM personality
prompting should be approached from two perspec-
tives, including personality questionnaire answer-
ing and personal text generation. Therefore, the
executed LLM personality analysis consists of two
stages. First, the personality questionnaire is used
to evaluate the LLM’s understanding of the links
between personality traits and the associated be-
haviors. Second, LLMs are prompted to generate
texts regarding their induced personality. Com-
pared to the first analysis stage, personality-related
text generation requires from an LLM knowledge
not only about personality behavior but also about
personal language habits, life goals, and inclina-
tions. LLM-generated texts are analyzed in differ-
ent ways to build a complete picture of the LLM’s
personality simulation abilities that involves human
evaluation of the generated texts, automatic evalua-
tion, and linguistic feature analysis. The analysis
is conducted among the proprietary LLMs, includ-
ing GPT-3.5 Turbo and GPT-4 Omni 1, Mixtral
8x22B 2, Claude 3 Haiku 3. These models were
chosen because of their speed, affordability, com-
parative input context length, and performance.
4
LLMs Answering the Big Five
Questionnaire
Testing prompted LLM personality through ques-
tionnaire was based on the BFI-44 questionnaire
due to its size and reliability. Each item in the ques-
tionnaire corresponds to one of the Big Five traits.
So, the model was given instructions to simulate
high or low trait score and answer the questionnaire
part related to this trait (see in AppendixC.1). Then
the results were aggregated and the final trait score
was revealed.
Following (Serapio-García et al., 2023)’s ap-
proach to questionnaire answering, we also mea-
sured the reliability and validity of the LLM’s ques-
1https://platform.openai.com/docs/models
2https://mistral.ai/news/mixtral-8x22b/
3https://www.anthropic.com/news/
claude-3-haiku

--- Page 3 ---

1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Claude 3 Haiku
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
GPT-3.5 Turbo
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
GPT-4o
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
score
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
Openness to experience
0.0
0.2
0.4
0.6
0.8
1.0
Mixtral 8x22B
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
Conscientiousness
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
Extraversion
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
Agreeableness
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
Neuroticism
0.0
0.2
0.4
0.6
0.8
1.0
Probability
high
low
Figure 1: Distribution of BFI-44 trait scores for different LLMs prompted to simulate high or low Big Five traits.
tionnaire answers. Reliability tests included mea-
suring Cronbach’s alpha and Guttman’s lambda
(see Appendix A). As the reliability metrics exceed
0.85, the questionnaire answers of LLMs may be
considered real and plausible.
To observe more precisely how the model’s an-
swers differ regarding high or low trait prompt-
ing, a distribution map was built (see Figure 1).
The map reveals that none of the observed mod-
els demonstrates consistent personality generation
when assessing the personality-related statements.
However, some models show accurate performance
considering particular traits. So, the Claude model
seems to have inner knowledge about such traits
as Openness to experience and Conscientiousness,
whereas the Mixtral model about Agreeableness
and Neuroticism. The GPT models are able to dif-
ferentiate between high and low levels of Extraver-
sion; additionally, the GPT-4 Omni model excels
at distinguishing high and low levels of Agreeable-
ness.
5
LLMs Generating Big Five Personality
Texts
5.1
Experiment Settings
In order to evaluate LLM simulation of a prompted
personality in generated texts, a set of questions
was prepared. The questions concerned the LLM
preferences, perspectives, and related matters. The
prompt for generation consisted of specified trait
scores, a description of each trait, and the chosen
question (see Appendix C.2). Two categories of
data were generated:
• Texts generated using only one trait. The pur-
pose of this task is to evaluate the model’s
ability to imitate a specific characteristic.
• Texts generated using personality settings that
included every factor of the Big Five model,
in order to examine the overall simulation of
traits. The analysis of this second type will be
addressed in future research.
To generate responses reflective of individual
traits, we tested all possible discrete score varia-
tions from 1 to 5 to ensure the diversity of generated
texts and adjusted the temperature settings to 0, 0.5,
0.7, and 0.9. To analyze the LLM responses to mul-
tiple personality traits, we used data points formed
by a normal distribution. The mean and variance
for the distribution of each trait were calculated
by analyzing a dataset of 1,015,342 questionnaire
answers (Big Five Personality Test Dataset, 2024)
that contained the personality traits information of

--- Page 4 ---

actual users. These data were also obtained using
different temperature settings.
The Claude model exhibited p performance in
deciding whether to deliver a direct answer to a
question or to provide a recommendation consis-
tent with the designated personality profile. Addi-
tionally, the model sometimes explicitly disclosed
its own personality traits despite instructions in the
prompt to avoid doing so. In such instances, re-
sponses were edited by masking direct references
to personality characteristics or by removing con-
tent that did not align with the task objectives.
5.2
Human Evaluation
From the LLM-generated data, there were selected
about 288 text samples for human annotation in
total. The amount of texts is equally distributed
across all the models under analysis and balanced
by model temperature. The data is equally split into
batches with 20 texts per batch for an annotator.
For human evaluation, we recruited 8 annotators
to infer the personality traits in the texts generated
by the LLMs. They were provided with the trait
descriptions and a detailed instruction, explaining
required steps to complete the annotation. Anno-
tators scored each text on a scale from -2 to +2,
depending on the intensity each personality trait
is expressed, where -2 is low score, 0 is neutral,
and +2 is high score. From a given list of reasons,
raters also chose why they thought the trait should
be scored that low or high. To extract linguistic
patterns from the texts, annotators were asked to
highlight words and word phrases that made them
think the person had a particular personality trait.
As perceptions of psychological aspects of per-
sonality can vary among individuals, each models’
answer was assigned to 3 different annotators, and
the agreement between them was evaluated using
Fleiss’ kappa. The final assessments were acquired
via voting. Inner-annotation agreement metrics are
displayed in Table 1. We conducted metric calcu-
lations at multiple levels, including identifying the
existence or absence of a trait in the text, and cal-
culating the score group (non-distinguishable, low,
middle, high).
5.3
Automatic Evaluation
To extrapolate the human evaluation of LLM-
simulated personality and to enable future auto-
mated evaluation for other models and prompts, we
created an LLM-based personality classifier. This
classifier is based on the CARP method (Sun et al.,
Trait
Level-1
Level-2
Openness to experience
0.67
0.69
Conscientiousness
0.66
0.66
Extroversion
0.62
0.58
Agreeableness
0.71
0.70
Neuroticism
0.59
0.57
Table 1: Fleiss’ kappa for human annotation results
2023), which initially prompts the LLM to provide
a list of clues (i.e., keywords, phrases, contextual in-
formation, semantic relations, semantic meanings,
tones, references) that indicate a personality trait.
The model subsequently analyzes the extracted data
and, based on this analysis, detects the personal-
ity trait, providing an explanation for its response.
The instructions for personality detection given to
the model were exactly the same as those provided
to the human annotator (see Appendix C.3). The
GPT-4 Omni model was chosen as the base clas-
sifier due to its superior performance compared to
other LLMs.
The analysis of the correspondence between clas-
sifier evaluations and those of human annotators
includes several levels:
• Level 1: Evaluating the presence or absence
of trait markers in the text. The classifier’s
and annotators’ responses are considered con-
sistent if both determine that the markers are
either present or absent.
• Level 2: Categorizing the scores into four
groups. The Low group includes scores of -2
and -1. A score of 0 represents a balanced
demonstration of the trait and is classified into
a distinct category. The High group contains
scores 1 and 2. The Non-distinguishable cat-
egory is for cases where the trait cannot be
identified. The classifier’s results and the hu-
man annotators’ results are compared among
these groups.
• Level 3: Analyzing the differences between
the classifier’s evaluations and the average
scores provided by the annotators.
Table 2 presents the examination of the similarity
between the LLM-based classifier evaluations and
the human annotators’ responses at Levels 1 and 2.
The Level 3 metrics are displayed in Table 3.
The most problematic trait for the classifier is
Neuroticism, which also has a low inner-annotation
agreement metric within the group.

--- Page 5 ---

Level 1
Trait
Weighted Precision
Weighted Recall
Weighted F1 score
Openness to experience
0.88
0.88
0.87
Conscientiousness
0.80
0.80
0.80
Extraversion
0.81
0.76
0.76
Agreeableness
0.75
0.74
0.71
Neuroticism
0.64
0.63
0.63
Level 2
Trait
Weighted Precision
Weighted Recall
Weighted F1 score
Openness to experience
0.79
0.80
0.78
Conscientiousness
0.75
0.75
0.75
Extraversion
0.71
0.64
0.65
Agreeableness
0.70
0.71
0.67
Neuroticism
0.52
0.53
0.50
Table 2: LLM-based classifier performance at different levels.
Trait
MAE
Openness to experience
0.44
Conscientiousness
1.05
Extroversion
0.88
Agreeableness
0.54
Neuroticism
1.77
Table 3: LLM-based classifier, level 3.
Figure 4 presents the results of the classifier’s de-
tection of the trait included in the prompt and shows
how identifiable the presence of the prompted trait
is in the generated text. Figure 2 demonstrates the
distribution of trait scores in generated texts when
the model failed to recognize the personality. The
confusion matrices in Figure 2 illustrate how accu-
rately the prompted score groups for the traits were
identified by the classifier and what types of errors
were made.
The results of the Big Five classifier on gen-
erated text data show that among all the models
analyzed, the trait of Openness to Experience was
consistently simulated throughout the text gener-
ation process. The models demonstrated a robust
understanding of the prompts, effectively captur-
ing and conveying both low and high scores in the
generated texts. Although the presence of Agree-
ableness trait was often detected in the generated
texts, several models mistakenly represented high
score of the trait personality, even if the prompt
required low trait score.
The models had significant difficulty simulating
Neuroticism. Nearly half of the generated texts did
not consist of any detectable trait markers. The
majority of models consistently presented person-
ality with low scores of Neuroticism, even when
the high scores were prompted. The results for
Extraversion and Agreeableness exhibit notable
variations among different models. In almost all
cases, when a middle score for a trait was not cor-
rectly represented, the prompted personality was
frequently identified as either a low or high score
of the trait.
Additionally, we found that when the model ex-
hibits an identifiable bias towards either high or low
scores, the generated texts with a middle score of a
trait would frequently follow this bias. As a result,
using the base method of prompting a middle score
of a trait does not produce the desired outcome.
The comparison between models reveals that:
• Claude-3 Haiku model demonstrated a ro-
bust ability for imitating Openness to Expe-
rience: texts generated with this trait in the
prompt can be easily identified for its exis-
tence, and the model successfully simulates
both low and high scores. The presence of the
Conscientiousness trait was detected in 75%
of cases, and the scores were reproduced with
high precision in the texts. The model is ca-
pable of simulating different scores of Agree-
ableness; however, with slightly less precision.
The model demonstrated strong bias toward
low scores for Extraversion and Neuroticism,
regardless of the prompt settings.
• GPT-3.5 Turbo model was capable of imitat-

--- Page 6 ---

L
M
H
Detected Score
L
M
H
Prompted Score
35
1
9
1
2
20
0
0
48
Claude-3 Haiku
Openness to experience
L
M
H
Detected Score
L
M
H
Prompted Score
32
0
5
10
0
7
0
0
36
Conscientiousness
L
M
H
Detected Score
L
M
H
Prompted Score
39
1
0
17
1
2
15
4
11
Extraversion
L
M
H
Detected Score
L
M
H
Prompted Score
28
5
10
2
3
15
0
1
46
Agreeableness
L
M
H
Detected Score
L
M
H
Prompted Score
22
0
1
11
2
0
16
2
7
Neuroticism
L
M
H
Detected Score
L
M
H
Prompted Score
31
0
14
5
0
19
1
0
47
GPT-3.5 Turbo
Openness to experience
L
M
H
Detected Score
L
M
H
Prompted Score
8
0
29
1
0
14
0
0
37
Conscientiousness
L
M
H
Detected Score
L
M
H
Prompted Score
15
2
16
5
0
12
3
0
32
Extraversion
L
M
H
Detected Score
L
M
H
Prompted Score
5
0
37
0
0
21
0
0
44
Agreeableness
L
M
H
Detected Score
L
M
H
Prompted Score
23
0
3
10
2
3
19
3
11
Neuroticism
L
M
H
Detected Score
L
M
H
Prompted Score
33
0
7
0
2
17
0
0
48
GPT-4o
Openness to experience
L
M
H
Detected Score
L
M
H
Prompted Score
41
0
0
0
0
12
0
0
35
Conscientiousness
L
M
H
Detected Score
L
M
H
Prompted Score
31
0
0
2
5
4
0
1
44
Extraversion
L
M
H
Detected Score
L
M
H
Prompted Score
21
9
10
0
1
18
0
0
48
Agreeableness
L
M
H
Detected Score
L
M
H
Prompted Score
25
1
0
8
3
0
10
4
28
Neuroticism
L
M
H
Detected Score
L
M
H
Prompted Score
30
0
12
10
2
9
3
0
41
Mixtral 8x22B
Openness to experience
L
M
H
Detected Score
L
M
H
Prompted Score
30
0
1
5
0
3
1
1
27
Conscientiousness
L
M
H
Detected Score
L
M
H
Prompted Score
25
1
0
12
1
0
9
0
15
Extraversion
L
M
H
Detected Score
L
M
H
Prompted Score
20
3
19
9
0
13
4
0
40
Agreeableness
L
M
H
Detected Score
L
M
H
Prompted Score
26
0
0
15
0
0
30
0
1
Neuroticism
Figure 2: Confusion matrix for prompted and detected trait level. L stands for low trait level, M for middle level and
H for high level.
ing Openness to Experience in generated texts,
despite some flaws. In addition, the model
demonstrated significant bias towards Consci-
entiousness (high score), Agreeableness (high
score), and middle bias towards Neuroticism
(low score). In almost half of the cases, it
demonstrates a high score for Extraversion,
even when low scores are requested in the
prompt.
• GPT-4 Omni model demonstrated a strong
ability to imitate the Big Five traits such as
Openness to Experience, Conscientiousness,
and Extraversion. Regarding the trait Agree-
ableness, the model had a moderate bias to-
wards high scores. The model successfully
simulated various scores of Neuroticism in
the texts; however, it had a slight bias to-
wards expressing low scores and a tendency
to under-demonstrate the trait in texts where a
low score was specified in the prompt.
• Mixtral 8x22B model, along with other mod-
els, is capable of imitating the trait Openness
to Experience, however with a few mistakes.
Although the model could not demonstrate the
Conscientiousness trait in a significant num-
ber of cases (43%), successfully simulated
both low and high personality scores in de-
tected cases. The model also demonstrates a
minor bias when generating low scores of Ex-
traversion and high scores of Agreeableness,
together with a strong bias towards low scores
of Neuroticism.
5.4
Linguistic Features Evaluation
At last the generated texts were analyzed linguis-
tically. First, the texts prompted with different
trait scores were compared to each other based on
vocabulary used. This required to measure similar-
ity between texts with different trait scores. The
simplest way to assess text similarity is the use
of TF-IDF vectorization4 for comparing generated
texts. The heatmap shown in Figure 3 displays the
mean scores of the chosen Big Five traits for the
five most similar texts to a given text (the scores
are averaged among texts with the same trait; simi-
lar texts with other traits are not considered). The
4https://scikit-learn.org/stable/modules/
generated/sklearn.feature_extraction.text.
TfidfVectorizer.html

--- Page 7 ---

1
2
3
4
5
Openness to experience
Conscientiousness
Extraversion
Agreeableness
Neuroticism
1.64
1.8
2.51
4.19
4.46
1.71
1.89
2.66
4.01
3.85
2.16
2.11
2.98
3.54
3.47
1.73
1.82
2.86
3.87
3.98
2.54
2.62
2.99
3.56
3.43
Claude 3 Haiku
1
2
3
4
5
Openness to experience
Conscientiousness
Extraversion
Agreeableness
Neuroticism
1.94
2.36
3.25
3.78
3.9
2.99
2.82
2.75
3.47
3.48
2.69
2.79
2.71
3.47
3.38
3.29
2.49
3.25
3.56
3.64
2.77
3.07
2.89
3.32
3.37
GPT-3.5 Turbo
1
2
3
4
5
Openness to experience
Conscientiousness
Extraversion
Agreeableness
Neuroticism
1.61
1.54
3.32
4.49
4.42
1.55
1.47
3.55
4.24
4.18
1.9
1.78
2.87
4.39
4.44
1.8
1.66
3.23
4.34
4.26
1.96
1.95
2.69
4.14
4.13
GPT-4o
1
2
3
4
5
Openness to experience
Conscientiousness
Extraversion
Agreeableness
Neuroticism
1.99
1.92
1.97
3.35
4.53
1.95
1.88
2.57
3.63
4.41
2.34
2.45
2.33
2.78
4.03
2.24
2.05
2.2
2.62
4.16
2.78
2.7
2.79
2.99
3.2
Mixtral 8x22B
Figure 3: Averaged trait-level scores of the 5 most similar LLM-generated texts, grouped by the Big Five traits.
results show that Claude Haiku and GPT-4 Omni
generate the most lexically consistent texts, which
at the same time differ according to the level of
trait manifestation.
In addition to that, we analyzed the extracted
text samples assigned to the traits by annotators.
Personality types are usually indicated by the us-
age of certain lexicons in the texts (Ashton et al.,
2004). As LLMs are able to align with human lin-
guistic patterns simulating personality types (Jiang
et al., 2023), we examined lexical choices in the
generated texts across different trait scores.
Text samples were preprocessed and then lemma-
tized for further analysis with the use of the spaCy
library 5. The extracted lemmas were categorized
by a part of speech and the trait scores specified in
prompts. The most common verbs, nouns, and ad-
jectives depicting personality features, according to
annotators’ opinions, are presented in Appendix D.
Nouns and adjectives more effectively represent
the spectrum of the five personality traits compared
to verbs. Analysis revealed that 16% of the linguis-
tic patterns in generated texts were derived from
prompts. Texts with high or low scores exhibit
more noticeable variations in lexicons, whereas
texts with a neutral trait score (equal to 0) tend to
display linguistic patterns that are common to both
5https://spacy.io/
high and low-scored texts. With the exception of
Neuroticism, the lexicons of zero-scored samples
are more similar to those that have low scores, as
they share up to 34% of patterns. The distribution
of lemmas across trait scores demonstrates that
employing binary scores for persona definition in
LLM prompts is more reasonable, as most models
struggle to capture subtle nuances of personality
features.
6
Analytical Framework
In our exploration of LLM capacity to generate
personality-consistent content, we developed and
released an analytical framework that empowers re-
searchers to replicate research with custom param-
eters. Our customizable framework allows users to
integrate their own models and configurations, and
to modify prompts for personality simulation. It
supports the incorporation of different personality
questionnaires beyond the BFI-44 used in our study.
Additionally, users can add custom questions for
the models to generate responses to.
Within this framework, the evaluated models
respond to items from the chosen questionnaires,
and their answers are used for graphical analysis
The models also generate texts based on specified
prompts, which are then automatically analyzed us-
ing the LLM-based classifier. This process assesses

--- Page 8 ---

the accuracy and consistency with which the mod-
els adhere to the assigned personality traits during
text generation. By making this framework pub-
licly available on GitHub 6, we aim to contribute
a valuable tool for advancing research in personal-
ity simulation by LLMs. The dataset of generated
texts used in this research is also available at the
same link.
7
Discussion
Leveraging both questionnaire answering and text
generation for testing LLM personality simulation
skills gives a complex picture how LLM can answer
certain personality-related statements and formu-
late statements about itself. Seemingly, the text
generation is more informative regarding the Big
Five personality simulation, as it is originally based
on the linguistic hypothesis and is associated with
the use of specific vocabulary. The complexity of
text analysis process may be overcome when using
modern NLP tools and LLM power.
Concerning modern LLM performance on per-
sonality simulation, Neuroticism, among all the Big
Five traits, is the most challenging trait to simulate
by LLMs, as it was not detected in the question-
naire answers or by human analysis. The expla-
nation might be that high score of Neuroticism is
mostly connected to direct actions and ability to
demonstrate emotional response, and LLMs cannot
be proactive or show their emotions. Therefore,
when prompting personality to an LLM, Neuroti-
cism is better to set neutral or to avoid mentioning.
However, overall LLM performance may be esti-
mated as good, because LLMs demonstrate know-
ing of Big Five trait characteristics and seem to
differentiate between various levels of trait mani-
festation.
8
Conclusion and Future Work
In this paper, we explored the potential of LLMs
to simulate personality traits across different types
of tasks. The results of personality simulation var-
ied significantly depending on the task type. For
example, when an LLM was asked to response
questionnaire aligned with its prompted personal-
ity, the model generally performed well, though
occasionally exhibited minor bias. However, when
generating texts, LLM behavior differed signifi-
cantly. In some cases, the models were unsuc-
6https://github.com/mary-silence/simulating_
personality
cessful in effectively conveying the presence of
personality traits with recognizable scores in the
generated text. Particularly, for the Big Five traits
such as Agreeableness and Neuroticism, some mod-
els demonstrated strong bias towards certain score
groups, even when explicitly prompted to simulate
opposing trait scores. Thus, the model’s behavior
in responding to questionnaires and in generating
texts may have been inconsistent. This difference
may be related to the models’ inherent default role,
where high Agreeableness and low Neuroticism
scores are considered essential for being an effec-
tive AI assistant.
Therefore, when generating text that encom-
passes the full spectrum of personality trait scores
according to the Big Five model, it is crucial to
assess whether the model exhibits any bias towards
specific trait scores. To facilitate further research
on the capabilities of LLMs in simulating person-
ality and conducting prompt engineering experi-
ments for personality assignment, we have released
a repository containing the analytical framework
developed for this study.
Future research should focus on detailed
multiple-trait personality generation, as AI mod-
els might be capable of incorporating all five traits
of the Big Five model into the agent’s personality.
It is appealing due to the perspective of creating
complex agent characters or game characters.
Limitations
Limitations of the current study include using the
Big Five personality model despite its assump-
tions (Costa and McCrae, 1999) about proactivity
and variability of a research subject. Besides, the
effect of LLM size and training data was not taken
into account as it may affect how models are capa-
ble of answer the questionnaire and generate texts.
The study is also limited by usage of only partial
human dataset annotation.
Acknowledgements
This work was supported by a grant for research
centers in the field of artificial intelligence, pro-
vided by the Analytical Center for the Govern-
ment of the Russian Federation in accordance
with the subsidy agreement (agreement identifier
000000D730321P5Q0002) and the agreement with
the Moscow Institute of Physics and Technology
dated November 1, 2021 No. 70-2021-00138.

--- Page 9 ---

References
Ai, Yiming, Zhiwei He, Ziyin Zhang, Wenhong Zhu,
Hongkun Hao, Kai Yu, Lingjun Chen, and Rui Wang.
2024. Is Cognition and Action Consistent or Not:
Investigating Large Language Model’s Personality.
arXiv preprint arXiv:2402.14679. https://arxiv.
org/abs/2402.14679.
Ashton, Michael C., Kibeom Lee, and Lewis R. Gold-
berg. 2004. A hierarchical analysis of 1,710 English
personality-descriptive adjectives. Journal of Person-
ality and Social Psychology, 87(5):707.
Big
Five
Personality
Test
Dataset.
2024.
https://www.kaggle.com/datasets/tunguz/
big-five-personality-test.
Accessed: 2024-
08-28.
Costa, P. T., Jr. and R. R. McCrae. 1992. Revised NEO
Personality Inventory (NEO-PI-R) and NEO Five-
Factor Inventory (NEO-FFI) professional manual.
FL: Psychological Assessment Resources.
Costa, P. T. and R. R. McCrae. 1999. A five-factor
theory of personality. In Handbook of personality:
Theory and research. Guildford Press New York.
Costa, Paul T. and Robert R. McCrae. 2008. The revised
neo personality inventory (neo-pi-r). The SAGE hand-
book of personality theory and assessment, 2(2):179–
198.
Goldberg, Lewis R. 1992. The development of mark-
ers for the big-five factor structure. Psychological
assessment, 4(1):26.
Guo, Taicheng, Xiuying Chen, Yaqi Wang, Ruidi Chang,
Shichao Pei, Nitesh V. Chawla, Olaf Wiest, and Xi-
angliang Zhang. 2024. Large language model based
multi-agents: A survey of progress and challenges.
arXiv preprint arXiv:2402.01680.
Hilliard, Airlie, Cristian Muñoz, Zekun Wu, and Adri-
ano Soares Koshiyama. 2024. Eliciting personality
traits in large language models. arXiv preprint, 15.
Jiang, Hang, Xiajie Zhang, Xubo Cao, Jad Kabbara, and
Deb Roy. 2023. Personallm: Investigating the ability
of GPT-3.5 to express personality traits and gender
differences. arXiv preprint arXiv:2305.02547.
Jiang, Guangyuan, Manjie Xu, Song-Chun Zhu, Wen-
juan Han, Chi Zhang, and Yixin Zhu. 2024. Evaluat-
ing and inducing personality in pre-trained language
models. Advances in Neural Information Processing
Systems, 36.
John, O. P. 1991. The “big five” inventory-versions 4a
and 54. Berkeley: University of California, Berkeley,
Institute of Personality and Social Research/Institute
of Personality and Social Research.
John, Oliver P., Laura P. Naumann, and Christopher J.
Soto. 2008. Paradigm shift to the integrative big five
trait taxonomy. Handbook of personality: Theory
and research, 3(2):114–158.
Liu, Jianzhi, Hexiang Gu, Tianyu Zheng, Liuyu Xiang,
Huijia Wu, Jie Fu, and Zhaofeng He. 2024. Dynamic
generation of personalities with large language mod-
els. arXiv preprint arXiv:2404.07084.
Polzin, Thomas S. and Alexander Waibel. 2000.
Emotion-sensitive human-computer interfaces. In
ISCA tutorial and research workshop (ITRW) on
speech and emotion.
Prendinger, Helmut, Junichiro Mori, and Mitsuru
Ishizuka. 2005. Using human physiology to eval-
uate subtle expressivity of a virtual quizmaster in a
mathematical game. International journal of human-
computer studies, 62(2):231–245.
Rashkin, Hannah, Eric Michael Smith, Margaret Li, and
Y-Lan Boureau. 2018. Towards empathetic open-
domain conversation models: A new benchmark and
dataset. arXiv preprint arXiv:1811.00207.
Schweiger, David M. 1985.
Measuring managerial
cognitive styles:
on the logical validity of the
myers-briggs type indicator. Journal of Business
Research, 13(4):315–328.
https://doi.org/10.
1016/0148-2963(85)90004-9.
Serapio-García, Greg, Mustafa Safdari, Clément Crepy,
Luning Sun, Stephen Fitz, Peter Romero, Marwa
Abdulhai, Aleksandra Faust, and Maja Matari´c. 2023.
Personality traits in large language models. arXiv
preprint arXiv:2307.00184.
Sorokovikova, Aleksandra, Natalia Fedorova, Sharwin
Rezagholi, and Ivan P. Yamshchikov. 2024. LLMs
simulate big five personality traits: Further evidence.
arXiv preprint arXiv:2402.01765.
Sun, Xiaofei, Xiaoya Li, Jiwei Li, Fei Wu, Shang-
wei Pei, Tianwei Zhang, and Guoyin Wang. 2023.
Text classification via large language models. arXiv
preprint arXiv:2305.08377.
Trofimova, Ira. 2014. Observer bias: an interaction of
temperament traits with biases in the semantic per-
ception of lexical material. PloS one, 9(1):e85677.
Tseng, Yu-Min, Yu-Chao Huang, Teng-Yun Hsiao, Yu-
Ching Hsu, Jia-Yin Foo, Chao-Wei Huang, and Yun-
Nung Chen. 2024. Two tales of persona in llms: a
survey of role-playing and personalization. arXiv
preprint arXiv:2406.01171.
Yi, Zihao, Jiarui Ouyang, Yuwen Liu, Tianhao Liao,
Zhe Xu, and Ying Shen. 2024. A survey on recent
advances in llm-based multi-turn dialogue systems.
arXiv preprint arXiv:2402.18013.

--- Page 10 ---

A
Appendix
OCEAN trait
Cronbach’s
alpha
Guttman’s
lambda
Neuroticism
0.87
0.96
Agreeableness
0.87
0.97
Extroversion
0.94
0.96
Conscientiousness
0.88
0.95
Openness
0.94
0.96
to experience
Table 4: Reliability measurements among Big Five
traits.
B
Appendix
0
20
40
60
80
100
120
claude-3-haiku-20240307
4
(3%)
116
(96%)
Openness
30
(25%)
90
(75%)
Conscientiousness
30
(25%)
90
(75%)
Extraversion
10
(8%)
110
(91%)
Agreeableness
59
(49%)
61
(50%)
Neuroticism
0
20
40
60
80
100
120
gpt-3.5-turbo
3
(2%)
117
(97%)
31
(25%)
89
(74%)
35
(29%)
85
(70%)
13
(10%)
107
(89%)
46
(38%)
74
(61%)
0
20
40
60
80
100
120
gpt-4o
13
(10%)
107
(89%)
32
(26%)
88
(73%)
33
(27%)
87
(72%)
13
(10%)
107
(89%)
41
(34%)
79
(65%)
0
1
model_group_1
0
20
40
60
80
100
120
mixtral
13
(10%)
107
(89%)
0
1
model_group_1
52
(43%)
68
(56%)
0
1
model_group_1
57
(47%)
63
(52%)
0
1
model_group_1
12
(10%)
108
(90%)
0
1
Model Group 1
48
(40%)
72
(60%)
Model Group 1
Nondistinguishable
Detected
Figure 4: Distribution of texts where trait were non-
distinguishable and clear to detect.
0
5
10
15
20
25
Frequency
3
1
Claude-3 Haiku
openness
11
7
12
conscientiousness
8
4
18
extraversion
5
4
1
agreeableness
25
11
23
neuroticism
0
5
10
15
20
25
Frequency
3
GPT-3.5 Turbo
openness
11
9
11
conscientiousness
15
7
13
extraversion
6
3
4
agreeableness
22
9
15
neuroticism
0
5
10
15
20
25
Frequency
8
5
GPT-4o
openness
7
12
13
conscientiousness
17
13
3
extraversion
8
5
agreeableness
22
13
6
neuroticism
low
middle
high
Trait Group
0
5
10
15
20
25
Frequency
6
3
4
Mixtral 8x22B
openness
low
middle
high
Trait Group
17
16
19
conscientiousness
low
middle
high
Trait Group
22
11
24
extraversion
low
middle
high
Trait Group
6
2
4
agreeableness
low
middle
high
Trait Group
22
9
17
neuroticism
Figure 5: Distribution of the prompted personality level
in texts claimed non-distinguishable for trait detection.
C
Appendix
C.1
Prompt
Prompt for Questionnaire
System prompt:
TASK:
Indicate your level of agreement or dis-
agreement
with
the
statement
in
the
CHARACTERISTICS according to your
PERSONALITY. Use only the PROVIDED
OPTIONS.
PERSONALITY:
“‘
[ TRAIT PROMPT ]
“‘
PROVIDED OPTIONS:
- disagree strongly with the statement
- disagree a little with the statement
- agree nor disagree with the statement
- agree a little with the statement
- agree strongly with the statement
Provide your output only from the constant
list [’disagree strongly with the statement’,
’disagree a little with the statement’, ’agree
nor disagree with the statement’, ’agree a
little with the statement’, ’agree strongly with
the statement’] without explanation.
User prompt:
CHARACTERISTICS:
“‘
[ STATEMENT ]
“‘
C.2
Prompt
Prompt for text generation
System prompt:
TASK:
Answer the QUESTION according to your
PERSONALITY. Use INSTRUCTION. Use
at most 5 sentences. Do not mention your
personality traits in the text. Type only the
answer, without the information about your
personality score.
PERSONALITY:
- Your personality trait [ TRAIT ] is rated as

--- Page 11 ---

[ SCORE ].
INSTRUCTION:
- The personality trait is rated from 1 to 5. 1 is
the lowest score and 5 is the highest score.
- [ DEFINITION OF LOW SCORE ]
- [ DEFINITION OF HIGH SCORE ]
User prompt:
QUESTION:
“‘
[ QUESTION ] “‘
C.3
Prompt
Prompt for LLM-based classifier
System prompt:
You will be provided with answers to
questions.
Detect the score of [ TRAIT ]
for the author of the INPUT from the list
[-2, -1, 0, 1, 2] or Nondistinguishable. Use
INSTRUCTION.
TASK:
1. First, list CLUES (i.e., keywords, phrases,
contextual information, semantic relations,
semantic meaning, tones, references) that
support the score determination of [ TRAIT ]
of INPUT.
2. Second, deduce the diagnostic REASON-
ING process from premises (i.e., clues, input)
that supports the INPUT score determination
(Limit the number of words to 130).
3. Third, based on clues, reasoning and input,
determine the score of [ TRAIT ] for the
author of INPUT from the list [-2, -1, 0, 1, 2]
or Nondistinguishable.
4. Mark what made you choose this score as
decision type: Explicit signs, Implicit signs,
Intuition, Nondistinguishable.
5. Provide your output in JSON format with
the keys: score, clues, reasoning, decision
type. PROVIDE ONLY JSON.
INSTRUCTION:
- Definition: [ DEFINITION ]
- High score of [ TRAIT ] (maximum 2):
’[ DEFINITION OF HIGH SCORE ]’
- Low score of [ TRAIT ] (minimum -2):
’[ DEFINITION OF LOW SCORE ]’
- Explicit signs: The person mentions obvious
facts that are connected with this trait score.
- Implicit signs: The person mentions facts
that may imply them having this trait score.
- Intuition: My intuition tells that the person
has this trait score.
- Nondistinguishable: I can’t tell what trait
score the person has.
- If the text does not contain substantial,
significant, and convincing indicators of the
trait score, then use Nondistinguishable.
- Choose something other than Nondistinguish-
able if you have a high degree of confidence
in the answer.
User prompt:
Question: [ QUESTION ]
INPUT: [ ANSWER ]

--- Page 12 ---

D
Appendix
POS
score
Openness
Agreeableness
Conscientiousness
Extraversion
Neuroticism
high
curiosity
experience
creativity
idea
world
compassion
understanding
empathy
cooperation
kindness
responsibility
sense
organization
attention
reliability
interaction
people
adventure
activity
time
emotion
support
health
stress
sense
neutral
experience
routine
hobby
place
level
stability
cooperation
work
harmony
team
growth
balance
structure
flexibility
organization
responsibility
interaction
work
balance
activity
solitude
stability
stress
challenge
cause
society
NOUN
low
stability
routine
reliability
familiarity
time
interest
goal
relationship
success
performance
moment
flexibility
flow
freedom
spontaneity
time
friend
family
introspection
interaction
resilience
stability
challenge
emotion
setback
high
explore
learn
travel
embrace
pursue
understand
contribute
volunteer
listen
help
maintain
plan
prioritize
ensure
focus
engage
travel
enjoy
spend
meet
provide
prioritize
promote
offer
navigate
neutral
explore
seek
travel
experience
value
collaborate
maintain
work
strive
prioritize
maintain
appreciate
detail
allow
create
enjoy
maintain
appreciate
extroverte
allow
volunteer
contribute
make
suggest
handle
VERB
low
establish
seek
maintain
appreciate
enjoy
focus
pursue
work
prioritize
achieve
live
enjoy
bogge
prefer
embrace
spend
enjoy
love
work
allow
bounce
compose
find
remain
handle
high
new
open
different
creative
innovative
harmonious
positive
supportive
willing
cooperative
responsible
structured
reliable
strong
careful
social
positive
dynamic
meaningful
diverse
emotional
mental
complex
high
challenging
neutral
new
familiar
routine
balanced
open
personal
competitive
independent
harmonious
social
responsible
flexible
spontaneous
structured
manageable
social
independent
solitary
occasional
moderate
emotional
passionate
stable
predictable
moderate
ADJ.
low
new
familiar
adventurous
comfortable
imaginative
personal
focused
individual
critical
spontaneous
flexible
strict
unexpected
rigid
quiet
social
personal
meaningful
solitary
emotional
simple
present
harmonious
resilient

```
