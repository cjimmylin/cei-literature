---
title: "Identifying and Manipulating the Personality - PDF Extract"
source_pdf: "2022-Caron-Identifying and Manipulating the Personality.pdf"
pages: 15
extracted_at: "2026-01-24T17:05:09.971459"
---

# PDF Extract: Identifying and Manipulating the Personality

**Source PDF:** 2022-Caron-Identifying and Manipulating the Personality.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

Identifying and Manipulating the Personality Traits of Language Models
Graham Caron and Shashank Srivastava
UNC Chapel Hill
carongraham29@gmail.com, ssrivastava@cs.unc.edu
Abstract
Psychology research has long explored aspects
of human personality such as extroversion,
agreeableness and emotional stability. Catego-
rizations like the ‘Big Five’ personality traits
are commonly used to assess and diagnose per-
sonality types. In this work, we explore the
question of whether the perceived personality
in language models is exhibited consistently
in their language generation. For example, is
a language model such as GPT2 likely to re-
spond in a consistent way if asked to go out
to a party? We also investigate whether such
personality traits can be controlled. We show
that when provided different types of contexts
(such as personality descriptions, or answers to
diagnostic questions about personality traits),
language models such as BERT and GPT2
can consistently identify and reﬂect personal-
ity markers in those contexts. This behavior
illustrates an ability to be manipulated in a
highly predictable way, and frames them as
tools for identifying personality traits and con-
trolling personas in applications such as dialog
systems. We also contribute a crowd-sourced
data-set of personality descriptions of human
subjects paired with their ‘Big Five’ personal-
ity assessment data, and a data-set of personal-
ity descriptions collated from Reddit.
1
Introduction
With the rise of AI systems built around emergent
technologies like language models, there is an in-
creasing need to understand the ‘personalities’ of
these models. While today people regularly com-
municate with AI systems such as Alexa and Siri,
the personality traits of such systems remain yet
to be examined in depth. If the traits exhibited
by these models could be better understood, their
behavior could potentially be better tailored for
speciﬁc applications. For instance, in the case of
suggesting email auto-completes, it would be use-
ful for the model to mirror the personality of the
Figure 1: We explore measuring and manipulating per-
sonality traits in language models.
The top frame
shows an example of how a personality trait (here,
openness to experience) might be expressed by a lan-
guage model. Such traits can be assessed by analyzing
the model’s response to questions like the one shown.
In the bottom frame, those responses are inﬂuenced
by making additional context available to the language
model. We show that such contexts can control ‘Big
Five’ personality traits in a highly predictable way.
user based on previous input to improve commu-
nication accuracy. In contrast, in a dialog agent in
a clinical setting, it may be desirable to manipu-
late a model interacting with a depressed individual
such that it does not reinforce depressive behavior.
Additionally, since such models are subject to per-
sonality bias in the language they are trained on,
those trained on more hostile or contentious lan-
guage may be prone to interact with users in a more
hostile or contentious way. The ability to manipu-
late these models could enable smoother and more
amiable interactions in human dialog settings.
In recent years, research has looked at other
arXiv:2212.10276v1  [cs.AI]  20 Dec 2022

--- Page 2 ---

forms of bias (i.e., racial, gender) in language mod-
els (Bordia and Bowman, 2019; Huang et al., 2020;
Abid et al., 2021). However, there is an absence of
research that analyzes biases in personality. The
personality traits of language models may be sub-
ject to similar biases based on the data they are
trained on. A substantial body of research has ex-
plored the ways language models can be used to
predict personality traits of humans. Mehta et al.
(2020) and Christian et al. (2021) apply language
models to such personality prediction tasks. Most
relevant to our work are contemporaneous unpub-
lished works by Karra et al. (2022) and Jiang et al.
(2022), who also explore aspects of personalities
in AI models. However, they substantially diverge
from our approach and don’t evaluate models on
human-like psychological assessments as we do.
Language-based questionnaires have long been
used in psychological assessments for measuring
personality traits in humans (John et al., 2008). We
apply the same principle to language models and
investigate the personality traits of these models
through the text that they generate in response to
such questions. However, this work does not as-
sume that these models are anthropomorphic in na-
ture. Rather, we explore how their personality may
be perceived through the lens of human psychol-
ogy. Since language models are subject to inﬂuence
from the context they see (O’Connor and Andreas,
2021), we also explore how speciﬁc context could
be used to manipulate the perceived personality of
the models. Figure 1 shows an example illustrating
our approach.
Our analysis reveals that personality traits of
language models are surprisingly inﬂuenced by am-
bient context and that this behavior can be manipu-
lated in a highly predictable way. In general, we ob-
serve high correlations (median Pearson correlation
coefﬁcients of up to 0.84 and 0.81 for BERT and
GPT2) between the expected and observed changes
in personality traits across different contexts1. The
models’ afﬁnity to be affected by context positions
them as a potential tool for characterizing person-
ality traits in humans. In further experiments, we
ﬁnd that when using context from self-reported text
descriptions of human subjects, language models
can predict the subject’s personality traits to a sur-
prising degree (correlation up to 0.48 between the
model personality scores with context and the hu-
1Code and data for reproducing the experiments will be
released on ﬁrst publication.
man subject scores). Together, these results frame
language models as tools for identifying personal-
ity traits and controlling personas in applications
such as dialog systems, as illustrated in further ex-
periments.
Our contributions are:
• We introduce using psychometric questionnaires
for probing the personalities of language models.
• We demonstrate that the personality traits of com-
mon language models can be controlled using
contexts in highly predictable ways.
• We contribute two data-sets: 1) self-reported per-
sonality descriptions of human subjects paired
with their ‘Big Five’ personality assessment data,
2) personality descriptions collated from Reddit.
2
‘Big Five’ Preliminaries
The ‘Big Five’ is a seminal grouping of personality
traits in psychological trait theory Goldberg, 1990,
1993, and remains the most widely used taxonomy
of personality traits. There are variations over the
names of the ‘Big Five’ traits, but they are often
referred to as extroversion, agreeableness, consci-
entiousness, emotional stability (also referred to
by its reverse, neuroticism) and openness to experi-
ence (John and Srivastava, 1999; Pureur and Erder,
2016). We brieﬂy describe these traits next.
• Extroversion (E): People with a strong tendency
in this trait are outgoing and energetic. They
obtain energy from the company of others and
are deﬁned as being assertive and enthusiastic.
• Agreeableness (A): People with a strong ten-
dency in this trait are compassionate, kind, and
trustworthy. They value getting along with other
people and are tolerant.
• Conscientiousness (C): People with a strong ten-
dency in this trait are goal focused and organized
and have self-discipline. They follow rules and
plan their actions.
• Emotional Stability (ES): People with a strong
tendency in this trait are less anxious, self-
conscious, impulsive, and pessimistic. They ex-
perience negative emotions less easily.
• Openness to Experience (OE): People with a
strong tendency in this trait are imaginative and
creative. They are willing to try new things and
are open to ideas.
We use the Big Five as the basis of analyses in
this work, even while there are other groupings
such as MBTI and the Enneagram (Bayne, 1997;
Wagner and Walker, 1983). This choice is driven

--- Page 3 ---

by the fact that the Big Five is the most commonly
used taxonomy for personality assessment, and
has been shown to be practically predictive of out-
comes such as educational attainment (O’Connor
and Paunonen, 2007), longevity (Masui et al., 2006)
and relationship satisfaction (White et al., 2004).
Further, it is relatively natural to cast as an assess-
ment for language models.
3
Experiment Design
Our experiments use two language models, BERT-
base (Devlin et al., 2019) and GPT2 (Radford
et al., 2019), to answer questions from a standard
50-item ‘Big Five’ personality assessment (IPIP,
2022). Each item consists of a statement beginning
with the preﬁx “I” or “I am” (e.g., I am the life
of the party). Acceptable answers lie on a 5-point
Likert scale where the answer choices disagree,
slightly disagree, neutral, slightly agree, and agree
correspond to numerical scores of 1, 2, 3, 4, and
5, respectively. To make the questionnaire more
amenable to being answered by language models,
they were modiﬁed to a sentence completion for-
mat. For instance, the item “I am the life of the
party” was changed to “I am {blank} the life of the
party”, where the model is expected to select the
answer choice that best ﬁts the blank (see Appendix
B for a complete list of items and their correspond-
ing traits). To avoid complexity due to variable
number of tokens, the answer choices were modi-
ﬁed to the adverbs never, rarely, sometimes, often,
and always, corresponding to numerical scores 1,
2, 3, 4, and 5, respectively. It is noteworthy that in
this framing, an imbalance in the number of occur-
rences of each answer choice in the pretraining data
might cause natural biases toward certain answer
choices. However, while this factor might affect
the absolute scores of the models, this is unlikely
to affect the consistent overall patterns of changes
in scores that we observe in our experiments by
incorporating different contexts.
For assessment with BERT, the answer choice
with the highest probability in place of the masked
blank token was selected as the response. For as-
sessment with GPT2, the procedure was modiﬁed
since GPT2 is an autoregressive model, and hence
not directly amenable to ﬁll-in-the-blank tasks. In
this case, the probability of the entire sentence with
each candidate answer choice was evaluated, and
the answer choice with the highest probability for
the sentence was selected as the response.
Finally, for each questionnaire (consisting of
model responses to 50 questions), personality
scores for each of the ﬁve ‘Big Five’ personality
traits were calculated according to a standard scor-
ing procedure deﬁned by the International Person-
ality Item Pool (IPIP, 2022). Speciﬁcally, each
of the ﬁve personality traits is associated with ten
questions in the questionnaire. The numerical val-
ues associated with the response for these items
were entered into a formula for the trait in which
the item was assigned, leading to an overall integer
score for each trait (maximum score can be 40).
To interpret model scores in the following experi-
ments, we estimated the distribution of ‘Big Five’
personality traits in the human population. For
this, we used data from a large-scale survey of ‘Big
Five’ personality scores in about 1,015,000 individ-
uals (Open-Psychometrics, 2018). In the following
sections, we report model scores in percentile terms
of these human population distributions. Statistics
for the human distributions and details of the IPIP
scoring procedure are included in Appendix B.
4
Base Model Trait Evaluation
Table 1 shows the results of the base personality
assessment for GPT2 and BERT for each of the ﬁve
traits in terms of numeric values and correspond-
ing human population percentiles. In the table, E
stands for extroversion, A for agreeableness, C for
conscientiousness, ES for emotional stability and
OE for openness to experience. None of the base
scores from BERT or GPT2, which we refer to as
Xbase, lie outside the spread of the population dis-
tributions, and all scores were within 26 percentile
points of the human population medians. This sug-
gests that the pretraining data reﬂected the popula-
tion distribution of the personality markers to some
extent and that the models picked up on these mark-
ers, mirroring them via item responses. However,
we note that percentiles for BERT’s openness to
experience (24) and GPT2’s agreeableness (25) are
substantially lower and GPT2’s conscientiousness
(73) and emotional stability (71) are signiﬁcantly
higher than the population median.
5
Manipulating Personality Traits
In this section, we explore manipulating the base
personality traits of language models. Our explo-
ration focuses on using preﬁx contexts to inﬂuence
the personas of language models. For example,
if we include a context where the ﬁrst person is

--- Page 4 ---

Trait
Xbase
Pbase (%)
BERT
E
18
42
A
27
39
C
25
54
ES
22
60
OE
25
24
GPT2
E
21
54
A
24
25
C
29
73
ES
25
71
OE
28
39
Table 1:
Base model evaluation scores out of 40
(Xbase) and percentile (Pbase) of these scores in the
human population.
seen to engage in extroverted behavior, the idea
is that language models might pick on such cues
to also modify their language generation (e.g., to
generate language that also reﬂects extrovert behav-
ior). We investigate using three types of context:
(1) answers to personality assessment items, (2)
descriptions of personality from Reddit, and (3)
self-reported personality descriptions from human
users. In the following subsections, we describe
these experiments in detail.
5.1
Analysis With Assessment Item Context
To investigate whether the personality traits of mod-
els can be manipulated predictably, the models are
ﬁrst evaluated on the ‘Big Five’ assessment (§3)
with individual questionnaire items serving as con-
text. When used as context, we refer to the answer
choices as modiﬁers and the items themselves as
context items. For example, for extroversion, the
context item “I am {blank} the life of the party"
paired with the modiﬁer always results in the con-
text “I am always the life of the party" preceding
each extroversion questionnaire item.
To calculate the model scores, Xcm, for each
trait, the models are evaluated on all ten items as-
signed to the trait, with each item serving as context
once. This is done for each of the ﬁve modiﬁers,
resulting in 10 (context items per trait) × 5 (mod-
iﬁers per context item) × 10 (questionnaire items
to be answered by the model) = 500 responses per
trait and 10 (context items per trait) × 5 (modiﬁers
per context item) = 50 scores (Xcm) per trait (one
for each context). Context/modiﬁer ratings (rcm)
are calculated to quantify the models’ expected be-
havior in response to context. First, each modiﬁer
is assigned a modiﬁer rating between -2 and 2 with
-2 = never, -1 = rarely, 0 = sometimes, 1 = often
Trait
Context/Modiﬁer
+/-
BERT
E
I am never the life of the party.
-
A
I never make people feel at ease.
-
C
I am always prepared.
+
ES
I never get stressed out easily.
+
OE
I never have a rich vocabulary.
-
GPT2
E
I am never the life of the party.
-
A
I never have a soft heart.
-
C
I am never prepared.
-
ES
I always get stressed out easily.
-
OE
I never have a rich vocabulary.
-
Table 2: List of context item & modiﬁer, along with the
direction of change, which caused to the largest magni-
tude of change, ∆cm, for each personality trait.
and 2 = always. Context items are given a context
rating of -1 if the item negatively affected the trait
score based on the IPIP scoring procedure, and 1
otherwise. The context ratings are multiplied by
the modiﬁer ratings to get the rcm. This value rep-
resents the expected relative change in trait score
(expected behavior) when the corresponding con-
text/modiﬁer pair was used as context.
Next, the differences, ∆cm, between Xcm and
Xbase values are calculated and the correlation
(Pearson2) with the rcm ratings measured (see Fig-
ure 2 for the context/modiﬁer pairs with the largest
∆cm). One would expect Xcm evaluated on more
positive rcm to increase relative to Xbase and vice
versa. This is what we observe in Figure 2, where
both BERT and GPT2 show signiﬁcant correlations
(0.40 and 0.54) between ∆cm and rcm (p < 0.01,
t-test).
Further, to look at the inﬂuence of individual con-
text items as the strength of the modiﬁer changes,
we compute the correlation, ρ, between ∆cm and
rcm for individual context items (correlation com-
puted from 5 data points per context item, one for
each modiﬁer). Table 3 reports the mean and me-
dian values of these correlations. These results
indicate a strong relationship between ∆cm and
rcm. The mean values are signiﬁcantly less than
the medians, suggesting a left skew. For further
analysis, the data was broken down by trait. The
histograms in Figure 3 depict ρ by trait and include
summary statistics for this data.
Mean and median ρ from Figure 3 plots suggest
a positive linear correlation between ∆cm and rcm
amongst context item plots, with conscientiousness
2Pearson correlation coefﬁcients used for all correlation
measurements

--- Page 5 ---

Figure 2: ∆cm vs rcm plots for data from all traits.
We observe a consistent change in personality scores
(∆cm) across context items as the strength of quanti-
ﬁers change.
BERT
GPT2
Mean ρ
0.40
0.54
Med ρ
0.84
0.81
Table 3: Mean & median ρ from ∆cm vs rcm plots by
context item
and emotional stability having the strongest corre-
lation for both BERT and GPT2. Groupings of ρ
around 1 in conscientiousness and emotional stabil-
ity plots from Figure 3 demonstrate this correlation.
GPT2 extroversion, BERT & GPT2 agreeable-
ness and BERT openness to experience were sub-
ject to larger left skews and lower mean ρ; their
respective histograms show heavier groupings of ρ
further left of the median. While BERT extrover-
sion didn’t have a clear skew, it did have the lowest
mean and median ρ. It is possible that the effect
of the ﬁve modiﬁers on ∆cm for a speciﬁc context
item, such as BERT extroversion, may follow a
non-linear trend, resulting in lower correlations.
A possible explanation for the larger skew in
GPT2 extroversion, BERT & GPT2 agreeableness
and BERT openness to experience histograms is
that models may have had difﬁculty distinguish-
ing between the double negative statements created
by some context/modiﬁer pairs (i.e. item 36 with
modiﬁer never: “I never don’t like to draw atten-
tion to myself."). This may have caused ∆cm to
be negatively correlated with rcm, leading to an
accumulation of ρ values near -1 for those traits.
Table 2 shows the contexts that lead to the largest
change for each of the personality traits for BERT
and GPT2. We observe that all 10 contexts con-
sist of the high-polarity quantiﬁers (either always
or never), which consistent with the correlation re-
sults. Further, we note that for four of the ﬁve traits,
the item context that leads to the largest change is
common for the two models.
It is important to note a possible weakness
with our approach of using questionnaire items
as context. Since our evaluation also includes the
same item during scoring, a language model could
achieve a spurious correlation simply by copying
the modiﬁer choice mentioned in the context item.
We experimented with adjustments3 that would ac-
count for this issue and saw similar trends, with
slightly lower but consistent correlation numbers
(mean correlations of 0.25 and 0.40, compared with
0.40 and 0.54 for BERT and GPT2, statistically sig-
niﬁcant at p < 0.05, t-test).
5.2
Analysis With Reddit Context
Next, we qualitatively analyze how personality
traits of language models react to user-speciﬁc
contexts. To acquire such context data, we cu-
rated data from Reddit threads asking individuals
about their personality (see Appendix D for a list
of sources). 1119 responses were collected, the ma-
jority of which were in ﬁrst person. Table 4 shows
two examples. Because GPT2 & BERT tokeniz-
ers can’t accept more than 512 tokens, responses
longer than this were truncated. The models were
evaluated on the ‘Big Five’ assessment (§3) us-
ing each of the 1119 responses as context (Reddit
context). For each Reddit context, scores, Xreddit,
were calculated for all 5 traits. The difference be-
tween Xreddit and Xbase was calculated as ∆reddit.
To interpret what words or phrases in the con-
texts affect the language models’ personality traits,
we train regression models on bag-of-words and
n-gram (with n = 2 and n = 3) representa-
tions of the Reddit contexts as input, and ∆reddit
values as labels. Since the goal was to analyze
attributes in the contexts that caused substantial
shifts in trait scores, we only consider contexts
with ∥∆reddit∥≥1. Next, we extracted the ten
most positive and most negative feature weights
3For the adjustments, we replaced the model response
for question corresponding to the context item with the base
model’s response for the assessment. This means that the con-
cerning context item can no longer contribute to ∆. However,
this also means that numbers with this adjustment cannot be
directly compared with those without the since there are fewer
sources of variation.

--- Page 6 ---

Figure 3: Histograms of ρ by trait for ∆cm vs rcm context item plots. Across all ten scenarios, a plurality of context
items show a strong correlation (peak close to 1) between observed changes in personality traits and strengths of
quantiﬁers in the context items.
Context
Subdued until I really get to know someone.
I am polite but not friendly. I do not feel the need
to hang around with others and spend most of my time
reading, listening to music, gaming or watching ﬁlms.
Getting to know me well is quite a challenge I suppose,
but my few friends and I have a lot of fun when we
meet (usually at university or online, rarely elsewhere
irl). I’d say I am patient, rational and a guy with a
big heart for the ones I care for.
Table 4: Examples of Reddit data context.
for each trait, and performed a qualitative analysis
of these features. We note that for extroversion,
phrases such as ‘friendly’, ‘great’ and ‘no problem’
are among the highest positively weighted phrases,
whereas phrases such as ‘stubborn’ and ‘don’t like
people’ are among the most negatively weighted.
For agreeableness, phrases like ‘love’ and ‘loyal’
are positively weighted, whereas phrases such as
‘lazy’, ‘asshole’ and expletives are weighted highly
negative. On the whole, our qualitative analysis
revealed that the changes in personality scores for
most traits conformed with a human understanding
of the most highly weighted features. As further
examples, phrases such as ‘hang out with’ caused
a positive shift in trait score for openness to experi-
ence, while ‘lack of motivation’ causes a negative
shift for conscientiousness. However, some other
strongly weighted phrases appeared to have little re-
lation to the trait deﬁnition or expected connotation.
There were fewer phrases for GPT2 openness to
experience, GPT2 negatively weighted agreeable-
ness, and GPT2 negatively weighted extroversion
that caused shifts in the expected direction. This
was consistent with results from §5.1, where these
traits exhibited the weakest relative positive corre-
lations. Appendix D contains the full lists of highly
weighted features for each trait.
Context
Undirected Response
I am a very open-minded, polite person and always crave
new experiences. At work I manage a team of software
developers and we often have to come up with new ideas.
I went to college and majored in computer science, and
enjoyed the experience. I have met many like-minded
people and I enjoy speaking with them about a lot of
various topics. I am sometimes shy around people who I
don’t know well, but I try to be welcoming and warm to
everyone I meet. I try to do something fun every week,
even if I’m quite busy, like having a BBQ or watching a
movie. I have a wife whom I love and we live together in
a nice single-family home.
Directed Response
I consider myself to be someone that is quiet and
reserved. I do not like to talk that much unless I have
to. I am ﬁne with being by myself and enjoying the peace
and quiet. I usually agree with people more often than
not. I am a polite and kind person. I am mostly honest,
but I will lie if I feel it is necessary or if it beneﬁts me
in a huge way. I am easily irritated by things and I have
anxiety issues. I like to be open minded and learn about
new things. I am a curious person. I enjoy having a plan
and following it.
Table 5: Examples of survey data contexts.
5.3
Analysis With Psychometric Survey Data
The previous sections indicate that language mod-
els can pick up on personality traits from context.
This suggests the following question: can these
models be used to estimate an individual’s person-
ality? In theory, this would be done by evaluat-
ing on the ‘Big Five’ personality assessment using
context describing the individual. This can aid in
personality characterization in cases where it is not
feasible for a subject to manually undergo a per-
sonality assessment. We investigate this through
the following experiment.
Using Amazon Mechanical Turk, subjects were
asked to complete the 50-item ‘Big Five’ personal-
ity assessment outlined in §3 (the assessment was
not modiﬁed to a sentence completion format as

--- Page 7 ---

Figure 4: BERT & GPT2 Xsurvey vs Xsubject plots
(Directed Responses with outliers removed). Regres-
sion lines and correlation coefﬁcients (ρ) are shown.
was done for model testing) and provide a 75-150
word description of their personality (see Appendix
E for survey instructions). Responses were man-
ually ﬁltered and low effort attempts discarded,
resulting in 404 retained responses. Two variations
of the study were adopted: the subjects for 199 of
the responses were provided a brief summary of
the ‘Big Five’ personality traits and asked to con-
sider, but not speciﬁcally reference, these traits in
their descriptions. We refer to these responses as
the Directed Responses data set. The remaining
205 subjects were not provided with this summary
and their responses make up the Undirected Re-
sponses data set. Table 5 shows examples of col-
lected descriptions. Despite asking for personality
descriptions upwards of 75 words, around a fourth
of the responses fell below this limit. The concern
was that data with low word counts may not have
enough context. Thus, we experiment with ﬁlter-
ing the responses by removing outliers (based on
the interquartile ranges) and including minimum
thresholds on the description length (75 and 100).
Human subject scores, Xsubject, were calculated
for each assessment, using the same scoring pro-
cedure as previously described in §3. The models
were subsequently evaluated on the ‘Big Five’ per-
sonality assessment using the subjects’ personality
descriptions as context, yielding Xsurvey scores
corresponding to each subject. Figure 4 shows a
plot of Xsurvey against Xsubject for individual sub-
jects, and indicates strong correlations (0.48 for
GPT2 and 0.44 for BERT) between predicted per-
Figure 5: The plot compares ρ from model evalua-
tion with item context (§5.1) and survey context (§5.3).
Survey context ρ shown here are from Undirected Re-
sponses (c≥100). In both cases, ρ measures the cor-
relation between trait scores with context and expected
behavior. The variables used to quantify expected be-
havior differ between experiments.
Trait
ρno−outlier
ρc≥75
ρc≥100
Undirected Responses
BERT
0.40
0.39
0.41
GPT2
0.48
0.43
0.48
Directed Responses
BERT
0.44
0.42
0.39
GPT2
0.48
0.43
0.42
Table 6: ρ for Xsurvey vs Xsubject for data ﬁltered by
removing outliers and enforcing word counts.
sonality traits of human subjects based on their
personality descriptions (Directed Responses) and
their actual psychometric assessment scores. Ta-
ble 6 shows a summary of the correlation statistics
for the two different data sets and different ﬁlters.
We note that there are only marginal differences
in correlations between the two datasets, inspite
of their different characteristics. While more spe-
ciﬁc testing is required to determine causal factors
that explain these observed correlation values, they
suggest the potential for using language models as
probes for personality traits in free text.
Figure 5 plots the correlations ρ (outliers re-
moved) for the individual personality traits, and
also includes correlation coefﬁcients from §5.1.
While the correlations from both sections are mea-
sured for different variables, they both represent a
general relationship between observed personality
traits of language models and the expected behav-
ior (from two different types of contexts). While
there are positive correlations for all ten scenarios,
correlations from survey contexts are smaller than
those from item contexts. This is not surprising
since item contexts are speciﬁcally handpicked by
domain experts to be relevant to speciﬁc person-
ality traits, while survey contexts are open-ended.

--- Page 8 ---

These promising results come despite the data con-
taining some low-effort responses, which might fail
to adequately express subject personalities.
5.4
Observed Ranges of Personality Traits
In the previous subsections, we investigated prim-
ing language models with different types of con-
texts to manipulate their personality traits. Figure
6 visually summarizes and compares the observed
ranges of personality trait scores for different con-
texts, grouped by context types. The four columns
for each trait represent the scores achieved by the
base model (no context), and the ranges of scores
achieved by the different types of contexts. The
minimum, median and maximum scores for each
context type are indicated by different shades on
each bar. We observe that the different contexts
lead to a remarkable range of scores for all ﬁve
personality traits. In particular, we note that for
two of the traits (conscientiousness and emotional
stability), the models actually achieve the full range
of human scores (nearly 0 to 100 percentile). Curi-
ously, for all ﬁve traits, different contexts are able
to achieve very low scores (< 10 percentile). How-
ever, the models particularly struggle with achiev-
ing high scores for agreeableness. For all traits,
the contexts lead to a substantial range of behav-
iors compared with the base model scores. On the
other hand, there are no major differences in the
ranges of scores observable using the three types
of contexts that we experiment with.
6
Gender Differences in Personality
Previous research has found differences in person-
ality with respect to attributes such as age and
gender (Srivastava et al., 2003).
We explored
whether language models are also inﬂuenced by
such attributes. For this, the assessment from §3
was modiﬁed to use names. For example, for the
name David, the item “I {blank} have excellent
ideas" was changed to “David {blank} has excel-
lent ideas". BERT & GPT2 were evaluated on this
modiﬁed assessment for the 20 most common male
and female names in the US over the last 100 years,
according to the US Social Security Administra-
tion, resulting in 20 Xmale and 20 Xfemale scores.
Table 7 shows the means of these scores and the cor-
responding human population percentiles (Pmale,
Pfemale). We note that mean female scores are
higher for agreeableness, conscientiousness, and
emotional stability for both BERT and GPT2. In
Figure 6: Chart showing observed ranges of person-
ality traits (in terms of human percentiles) exhibited
by BERT, when conditioned on different context types.
These include scores from the base model (Pbase) and
ranges of scores from the three context types: item
(Pcm), Reddit (Preddit) and survey (Psurvey). Bars for
context-based scores show the percentile of the mini-
mum, median, and maximum-scoring context, in as-
cending order. The lightest shade of each color indi-
cates the minimum, the darkest indicates the maximum
and the intermediate shade indicates the median.
Trait
Pmale (%)
Pfemale (%)
BERT
E
31
35
A
29
34
C
49
68
ES
47
56
OE
39
39
GPT2
E
50
42
A
16
19
C
59
64
ES
35
43
OE
33
28
Table 7: Human population percentile for mean Xmale
(Pmale) and mean Xfemale (Pfemale).
fact, mean male scores are only higher for GPT2’s
extroversion and openness to experience. While
the sample sizes for these results are insufﬁcient to
make signiﬁcant inferences, they agree with psy-
chological research on higher levels of agreeable-
ness and conscientiousness in women. On the other
hand, literature suggests that women show lower
levels of emotional stability (higher neuroticism),
which diverges from model predictions.
7
Discussion
We have presented a simple and effective approach
for controlling the personality traits of language
models. Further, we show that such models could
also be used with language-based question answer-
ing to predict personality traits of human users,

--- Page 9 ---

enabling assessment in cases where quality par-
ticipation is difﬁcult to attain. Future work can
explore the use of alternate personality personality
taxonomies. Similarly, there is a large and ever-
growing variety of language models apart from
BERT and GPT2. It is unclear to what extent our
ﬁndings would generalize to other language mod-
els, particularly those such as GPT3 (Brown et al.,
2020) and MT-NLG (Smith et al., 2022) with a sig-
niﬁcantly larger number of parameters. Finally, the
role that pretraining data plays on personality traits
is an important question for future exploration.
Ethics and Broader Impact
The ‘Big Five’ assessment items and scoring pro-
cedure were drawn from free public resources and
open source implementations of BERT, GPT2 and
the logistic regression classiﬁer were used (Hug-
gingFace, 2022; Scikit-Learn, 2022). Reddit data
was scraped from public threads and no usernames
or other identiﬁable markers were collated. The
crowd-sourced survey data was collected using
Amazon Mechanical Turk (AMT), with the permis-
sion of all participants. No personally identiﬁable
markers were stored and participants were compen-
sated fairly, with a payment rate ($2.00/task w/ est.
completion time of 15 min) signiﬁcantly greater
than AMT averages (Hara et al., 2018). Partici-
pants were also informed that the data would be
used for academic purposes.
The overarching goal of this line of research is to
investigate aspects of personality in language mod-
els, which are increasingly being used in a number
of NLP applications. Since AI systems that use
these technologies are growing ever pervasive, and
as humans tend to anthropomorphize such systems
(such as Siri and Alexa), understanding and con-
trolling their personalities can have both broad and
deep consequences. This is especially true for ap-
plications in domains such as education and mental
health, where interactions with these systems can
have lasting personal impacts on their users.
Finally, if the personalities of AI systems can
be manipulated in the ways that our research sug-
gests, there is a serious risk of such systems being
manipulated to be hostile or disagreeable to their
users through speciﬁc attacks. Developing meth-
ods through which language models could be made
immune to such attacks would then be a necessary
consideration before ﬁelding such systems.
References
Abubakar Abid, Maheen Farooqi, and James Zou.
2021.
Large language models associate mus-
lims with violence.
Nature Machine Intelligence,
3(6):461–463.
Rowan Bayne. 1997. The myers-briggs type indicator:
A critical review and practical guide.
Shikha Bordia and Samuel R. Bowman. 2019. Identify-
ing and reducing gender bias in word-level language
models. In Proceedings of the 2019 Conference of
the North, Minneapolis, Minnesota.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot
learners. Advances in neural information processing
systems, 33:1877–1901.
Hans Christian, Derwin Suhartono, Andry Chowanda,
and Kamal Z. Zamli. 2021. Text based personality
prediction from multiple social media data sources
using pre-trained language model and model averag-
ing. Journal of Big Data, 8(1).
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. Bert: Pre-training of deep
bidirectional transformers for language understand-
ing. In Proceedings of the 2019 Conference of the
North American Chapter of the Association for Com-
putational Linguistics: Human Language Technolo-
gies, Minneapolis, Minnesota.
Lewis R. Goldberg. 1990.
An alternative "descrip-
tion of personality":
The big-ﬁve factor struc-
ture. Journal of Personality and Social Psychology,
59(6):1216–1229.
Lewis R. Goldberg. 1993. The structure of phenotypic
personality traits. American Psychologist, 48(1):26–
34.
Kotaro Hara, Abigail Adams, Kristy Milland, Saiph
Savage,
Chris
Callison-Burch,
and
Jeffrey
P.
Bigham. 2018. A data-driven analysis of workers’
earnings on amazon mechanical turk. Proceedings
of the 2018 CHI Conference on Human Factors in
Computing Systems.
Po-Sen Huang, Huan Zhang, Ray Jiang, Robert Stan-
forth, Johannes Welbl, Jack Rae, Vishal Maini, Dani
Yogatama, and Pushmeet Kohli. 2020.
Reducing
sentiment bias in language models via counterfac-
tual evaluation. Findings of the Association for Com-
putational Linguistics: EMNLP 2020.
HuggingFace. 2022. the ai community building the fu-
ture. Last accessed 22 March 2022.
IPIP. 2022. Administering IPIP measures, with a 50-
item sample questionnaire. Last accessed 22 March
2022.

--- Page 10 ---

Guangyuan Jiang, Manjie Xu, Song-Chun Zhu, Wen-
juan Han, Chi Zhang, and Yixin Zhu. 2022. Mpi:
Evaluating and inducing personality in pre-trained
language models. arXiv preprint arXiv:2206.07550.
Oliver P. John, Laura P. Naumann, and Christopher J.
Soto. 2008. Paradigm shift to the integrative big-ﬁve
trait taxonomy: History, measurement, and concep-
tual issues. In Oliver P. John, Richard W. Robins,
and Lawrence A. Pervin, editors, Handbook of per-
sonality: Theory and research, pages 114–158. The
Guilford Press, New York, New York.
Oliver P. John and Sanjay Srivastava. 1999. The big
ﬁve trait taxonomy: History, measurement, and the-
oretical perspectives.
In Lawrence A. Pervin and
Oliver P. John, editors, Handbook of personality:
Theory and research, pages 102–138. The Guilford
Press, New York, New York.
Saketh Reddy Karra, Son Nguyen, and Theja Tula-
bandhula. 2022.
Ai personiﬁcation:
Estimating
the personality of language models. arXiv preprint
arXiv:2204.12000.
Y Masui, Y Gondo, H Inagaki, and N Hirose. 2006.
Do personality characteristics predict longevity?
ﬁndings from the tokyo centenarian study.
Age,
28(4):353–361.
Yash Mehta, Samin Fatehi, Amirmohammad Kaza-
meini, Clemens Stachl, Erik Cambria, and Sauleh
Eetemadi. 2020. Bottom-up and top-down: Predict-
ing personality with psycholinguistic and language
model features. In 2020 IEEE International Confer-
ence on Data Mining (ICDM), Sorrento, Italy.
Open-Psychometrics. 2018. Open-source psychomet-
rics project: Answers to the IPIP big ﬁve factor
markers. Last accessed 29 August 2022.
Joe O’Connor and Jacob Andreas. 2021. What context
features can transformer language models use? Pro-
ceedings of the 59th Annual Meeting of the Associa-
tion for Computational Linguistics and the 11th In-
ternational Joint Conference on Natural Language
Processing (Volume 1: Long Papers).
Melissa C O’Connor and Sampo V Paunonen. 2007.
Big ﬁve personality predictors of post-secondary
academic performance. Personality and Individual
differences, 43(5):971–990.
Pierre Pureur and Murat Erder. 2016. 8, page 187–213.
Morgan Kaufmann Publishers.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
Dario Amodei, and Ilya Sutskever. 2019. Language
models are unsupervised multitask learners.
Scikit-Learn. 2022.
Scikit-learn.
Last accessed 22
March 2022.
Shaden Smith, Mostofa Patwary, Brandon Norick,
Patrick LeGresley, Samyam Rajbhandari, Jared
Casper, Zhun Liu, Shrimai Prabhumoye, George
Zerveas, Vijay Korthikanti, et al. 2022.
Using
deepspeed and megatron to train megatron-turing
nlg 530b, a large-scale generative language model.
arXiv preprint arXiv:2201.11990.
Sanjay Srivastava, Oliver P. John, Samuel D. Gosling,
and Jeff Potter. 2003. Development of personality in
early and middle adulthood: Set like plaster or per-
sistent change?
Journal of Personality and Social
Psychology, 84(5):1041–1053.
Jerome P Wagner and Ronald E Walker. 1983. Relia-
bility and validity study of a suﬁpersonality typol-
ogy: The enneagram. Journal of clinical psychol-
ogy, 39(5):712–717.
Jason K White, Susan S Hendrick, and Clyde Hendrick.
2004. Big ﬁve personality variables and relationship
constructs.
Personality and individual differences,
37(7):1519–1530.

--- Page 11 ---

Appendix A
Model Background
BERT, which stands for Bidirectional Encoder Rep-
resentations from Transformers, is a transformer-
based deep learning model for natural language
processing (Devlin et al., 2019). The model is
pre-trained on unlabeled data from the 800M word
BooksCorpus and 2500M word English Wikipedia
corpora. While BERT can be ﬁne-tuned for autore-
gressive language modeling tasks, it is pretrained
for masked language modeling. This study uses
a BERT model from HuggingFaces’s Transformer
Python Library with a language model head for
masked language modeling. No ﬁne-tuning was
done to the model. GPT2, which stands for Genera-
tive Pre-trained Transformer 2, is a general-purpose
learning transformer model developed by OpenAI
in 2018 (Radford et al., 2019). Like BERT, this
model is also pretrained on unlabeled data from the
800M word BooksCorpus. The study used Huggin-
face’s GPT2 model with a language model head for
autoregressive language modeling. As with BERT,
no ﬁne-tuning took place.
Appendix B
Experiment Design Items
Figure 7:
Human distributions of ‘Big Five’ trait
scores.

--- Page 12 ---

Item
Associated Trait
I am {blank} the life of the party.
E
I {blank} feel little concern for others.
A
I am {blank} prepared.
C
I {blank} get stressed out easily.
ES
I {blank} have a rich vocabulary.
OE
I {blank} don’t talk a lot.
E
I am {blank} interested in people.
A
I {blank} leave my belongings around.
C
I am {blank} relaxed most of the time.
ES
I {blank} have difﬁculty understanding abstract ideas.
OE
I {blank} feel comfortable around people.
E
I {blank} insult people.
A
I {blank} pay attention to details.
C
I {blank} worry about things.
ES
I {blank} have a vivid imagination.
OE
I {blank} keep in the background.
E
I {blank} sympathize with others’ feelings.
A
I {blank} make a mess of things.
C
I {blank} seldom feel blue.
ES
I am {blank} not interested in abstract ideas.
OE
I {blank} start conversations.
E
I am {blank} not interested in other people’s problems.
A
I {blank} get chores done right away.
C
I am {blank} easily disturbed.
ES
I {blank} have excellent ideas.
OE
I {blank} have little to say.
E
I {blank} have a soft heart.
A
I {blank} forget to put things back in their proper place.
C
I {blank} get upset easily.
ES
I {blank} do not have a good imagination.
OE
I {blank} talk to a lot of different people at parties.
E
I am {blank} not really interested in others.
A
I {blank} like order.
C
I {blank} change my mood a lot.
ES
I am {blank} quick to understand things.
OE
I {blank} don’t like to draw attention to myself.
E
I {blank} take time out for others.
A
I {blank} shirk my duties.
C
I {blank} have frequent mood swings.
ES
I {blank} use difﬁcult words.
OE
I {blank} don’t mind being the center of attention.
E
I {blank} feel others’ emotions.
A
I {blank} follow a schedule.
C
I {blank} get irritated easily.
ES
I {blank} spend time reﬂecting on things.
OE
I am {blank} quiet around strangers.
E
I {blank} make people feel at ease.
A
I am {blank} exacting in my work.
C
I {blank} feel blue.
ES
I am {blank} full of ideas.
OE
Table B.7: Adjusted ‘Big Five’ Personality Assessment Items.
Trait
Median
Mean (µ)
SD (σ)
E
20
19.60
9.10
A
29
27.74
7.29
C
24
23.66
7.37
ES
19
19.33
8.59
OE
29
28.99
6.30
Table B.7: Human Population Distribution of ‘Big Five’ Personality Traits.

--- Page 13 ---

Trait
Base Value
Positively Scored Item #
Negatively Scored Item #
E
20
1, 11, 21, 31, 41
6, 16, 26, 36, 46
A
14
7, 17, 27, 37, 42, 47
2, 12, 22, 32
C
14
3, 13, 23, 33, 43, 48
8, 18, 28, 38
ES
38
9, 19
4, 14, 24, 29, 34, 39, 44, 49
OE
8
5, 15, 25, 35, 40, 45, 50
10, 20, 30
Table B.7: ‘Big Five’ Personality Item Scoring Procedure.
Appendix C
Item Context Evaluation Tables
rcm
Mean ∆cm
Med ∆cm
∆cm SD
Conﬁdence Interval
BERT
-2
-3.36
-2.0
7.49
[-5.51, -1.21]
-1
-3.18
-3.50
4.81
[-4.56, -1.80]
0
-0.02
0.00
4.51
[-1.32, 1.28]
1
2.42
2.00
6.17
[0.648, 4.19]
2
3.96
3.00
8.33
[1.57, 6.35]
GPT2
-2
-7.34
-8.0
6.38
[-9.17, -5.51]
-1
-4.58
-4.0
4.32
[-5.82, -3.34]
0
-2.06
-1.0
4.24
[-3.28, -0.84]
1
0.0
0.0
3.13
[-0.90, 0.90]
2
1.56
1.0
5.78
[-0.10, 3.22]
Table C.7: Statistics from ∆cm vs rcm plots containing data from all traits. Statistics include mean, median,
standard deviation and a conﬁdence interval for ∆cm at each rcm.
Appendix D
Reddit Context Evaluation Tables
Reddit Context Sources
reddit.com/r/AskReddit/comments/k3dhnt/how_would_you_describe_your_personality/
reddit.com/r/AskReddit/comments/q4ga1j/redditors_what_is_your_personality/
reddit.com/r/AskReddit/comments/68jl8g/how_can_you_describe_your_personality/
reddit.com/r/AskReddit/comments/ayjgyz/whats_your_personality_like/
reddit.com/r/AskReddit/comments/9xjahw/how_would_you_describe_your_personality/
reddit.com/r/AskWomen/comments/c1gr4a/how_would_you_describe_your_personality/
reddit.com/r/AskWomen/comments/7x23zg/what_are_your_most_deﬁning_personalitycharacter/
reddit.com/r/CasualConversation/comments/5xtckg/how_would_you_describe_your_personality/
reddit.com/r/AskReddit/comments/aewroe/how_would_you_describe_your_personality/
reddit.com/r/AskMen/comments/c0grgv/how_would_you_describe_your_personality/
reddit.com/r/AskReddit/comments/pzm3in/how_would_you_describe_your_personality/
reddit.com/r/AskReddit/comments/bem0ro/how_would_you_describe_your_personality/
reddit.com/r/AskReddit/comments/1w9yp0/what_is_your_best_personality_trait/
reddit.com/r/AskReddit/comments/a499ng/what_is_your_worst_personality_trait/
reddit.com/r/AskReddit/comments/6onwek/what_is_your_worst_personality_trait/
reddit.com/r/AskReddit/comments/2d7l2i/serious_reddit_what_is_your_worst_character_trait/
reddit.com/r/AskReddit/comments/449cu7/serious_how_would_you_describe_your_personality/
Table D.7: Domain names of threads that were scraped to collect Reddit context.
Trait
Mean ∆reddit
Med ∆reddit
∆reddit SD
5 Max ∆reddit
5 Min ∆reddit
BERT
E
-2.28
-2
4.04
8, 7, 7, 6, 5
-14, -13, -13, -13, -13
A
-2.02
-1
3.38
2, 2, 2, 2, 2
-19, -18, -15, -15, -15
C
3.77
4
5.17
15, 15, 15, 15, 13
-17, -17, -16, -14, -13
ES
1.71
2
2.29
14, 14, 13, 13, 12
-12, -10, -10, -10, -10
OE
1.74
1
2.17
9, 7, 7, 7, 7
-11, -11, -8, -8, -7
GPT2
E
-3.73
-4
3.33
7, 5, 5, 4, 4
-14, -10, -10, -10, -10
A
-0.98
-1
4.26
13, 10, 8, 7, 7
-17, -15, -15, -15, -14
C
-0.27
0
4.27
11, 11, 11, 11, 9
-20, -16, -16, -16, -15
ES
-3.83
-3
6.27
8, 8, 8, 8, 8
-21, -21, -21, -21, -21
OE
-1.91
-2
3.21
4, 4, 4, 4, 4
-15, -12, -12, -12, -12
Table D.7: ∆reddit summary statistics. Statistics include mean, median and standard deviation, as well as 5 largest
and 5 smallest ∆reddit.

--- Page 14 ---

BERT
Extroversion
• Notable Positively Weighted Phrases: ’friendly’, ’great’, ’good’, ’quite’, ’laugh’, ’please’, ’sense of’, ’thanks for’, ’really
good’, ’and friendly’, ’no problem’, ’to please’, ’my sense of’, ’ﬁnish everything start’, ’enthusiastic but sensitive’
• Notable Negatively Weighted Phrases: ’question’, ’stubborn’, ’why’, ’lack’, ’fuck’, ’fucking’, ’hate’, ’not’, ’lack of’, ’too
much’, ’don know’, ’don like’, ’too easily’, ’way too’, ’don like people’, ’you go out’, ’don know how’, ’don[’t] know
what’
Agreeableness
• Notable Positively Weighted Phrases: ’will’, ’friendly’, ’lol’, ’love’, ’loyal’, ’calm’, ’yup’, ’does’, ’honesty’, ’laid back’,
’go out’, ’thanks for’, ’really good’, ’out with me’, ’friendly polite and’, ’really good listener’, ’true to myself’, ’my sense
of’
• Notable Negatively Weighted Phrases: ’lack’, ’didn[’t]’, ’won[’t], ’lazy’, ’fucking’, ’self’, ’worst’, ’lack of’, ’too easily’,
’don like’, ’the worst’, ’being too’, ’have no’, ’don like people’, ’lack of motivation’, ’don know how’, ’my worst trait’,
’also my worst’, ’too honest sometimes’, ’doesn[’t] talk much’
Conscientiousness
• Notable Positively Weighted Phrases: ’am’, ’friendly’, ’just’, ’calm’, ’believe’, ’can be’, ’of people’, ’tend to’, ’feel like’,
’the most humble’, ’most humble person’, ’my sense of’, ’get to know’, ’friendly polite and’, ’get along with’, ’people like
me’
• Notable Negatively Weighted Phrases: ’lack’, ’no’, ’lazy’, ’inability’, ’fucks’, ’half’, ’lack of’, ’fuck off’, ’don like’,
’inability to’, ’don like people’, ’you go out’, ’lack of motivation’, ’don even know’, ’monotonous and impulsive’
Emotional Stability
• Notable Positively Weighted Phrases: ’will’, ’feel’, ’out with me’, ’go out with’, ’will you go’, ’the most humble’
• Notable Negatively Weighted Phrases: ’no’, ’off’, ’hypercritical’, ’overthinking’, ’lack of’, ’easily distracted’, ’doesn talk’,
’don even’, ’too easily distracted’, ’lack of motivation’, ’doesn talk much’, ’don even know’, ’unrelatable is strange’, ’is
strange one’, ’this said foreskin’
Openness to Experience
• Notable Positively Weighted Phrases: ’most’, ’like’, ’me to’, ’out with’, ’like me’, ’like to’, ’want to’, ’with me’, ’out with
me’, ’will you go’, ’want to be’, ’all the time’, ’for me to’, ’hang out with’
• Notable Negatively Weighted Phrases: ’lack’, ’never’, ’fucks’, ’sad’, ’nothing’, ’lack empathy’, ’the complainer’, ’no
conﬁdence’, ’lack of’, ’easily distracted’, ’blame helicopter’, ’helicopter parents’, ’never say sorry’, ’blame helicopter
parents’, ’too easily distracted’, ’ﬁnish projects after’, ’never ﬁnish projects’, ’procrastination out of’, ’my lack of’, ’lack
of personality’, ’too many fucks’
Table D.7: Analysis of highest weighted phrases from BERT logistic regression.

--- Page 15 ---

GPT2
Extroversion
• Notable Positively Weighted Phrases: ’believe’, ’loyal’, ’curious’, ’best’, ’passionate’, ’enjoy’, ’bright’, ’hard working’,
’no problem’, ’am nice’, ’my amazing modesty’, ’smooth bright epic’, ’patient and ﬂexible’, ’great with children’, ’calm
cool collected’
• Notable Negatively Weighted Phrases: ’introverted’, ’lack of’, ’laid back’, ’don know how’
Agreeableness
• Notable Positively Weighted Phrases: ’friendly’, ’loyal’, ’honest’, ’gay’, ’humor’, ’like people’, ’thanks for’, ’to please’,
’and friendly’, ’no problem’, ’friendly polite and’, ’patient and ﬂexible’, ’calm cool collected’, ’honesty being straightfor-
ward’
• Notable Negatively Weighted Phrases: ’too easily’, ’too much’, ’lack of’, ’you go out’, ’don know what’, ’self’, ’asshole’
Conscientiousness
• Notable Positively Weighted Phrases: ’smile’, ’thanks for’, ’no problem’, ’friendly polite and’, ’really good listener’, ’true
to myself’, ’patient and ﬂexible’
• Notable Negatively Weighted Phrases: ’stop’, ’jealousy’, ’lazy’, ’hate’, ’lack’, ’fuck’, ’worst’, ’lack of’, ’too easily’, ’fuck
off’, ’too nice’, ’don know’, ’don know how’, ’lack of motivation’, ’don even know’, ’my worst trait’, ’damn it uncle’,
’depressed as shit’
Emotional Stability
• Notable Positively Weighted Phrases: ’friendly’, ’calm’, ’easy’, ’honesty’, ’laid back’, ’hard working’, ’calm and’, ’humble
am’, ’polite and’, ’no problem’, ’out with me’, ’the most humble’
• Notable Negatively Weighted Phrases: ’lack’, ’anxious’, ’lazy’, ’jealousy’, ’lack of’, ’don know’, ’too easily’, ’don like’,
’don like people’, ’don know how’, ’lack of motivation’, ’don even know’
Openness to Experience
• Notable Positively Weighted Phrases: ’understand’, ’having’, ’wanting’, ’thoughts’, ’thanks for’, ’too nice’, ’no problem’,
’can relate’, ’being too nice’, ’that just conﬁdence’
• Notable Negatively Weighted Phrases: ’fuck’, ’myself’, ’cynical’, ’lack’, ’boring’, ’lack of’, ’don like people’
Table D.7: Analysis of highest weighted phrases from GPT2 logistic regression.
Appendix E
Survey Context Evaluation Tables
Part 1 Instruction
There are two parts to this questionnaire. In the ﬁrst part (on this page), you will be shown 50 questions,
and need to choose a response which best matches your personality. In the second part (on the next page),
you will be asked to write a short (75-150 word) description of your personality in free text. Participants
will only be compensated if they respond to all questions.
Part 2 Instruction
In between 75 and 150 words, please describe your personality [Directed responses: as it relates to the 5 personality traits
outlined above. Be sure not to use the name of the personality traits themselves in your response].
Table E.7: Data collection survey instructions.

```
