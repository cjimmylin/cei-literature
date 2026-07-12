---
source_pdf: "[[Lit-WS-PDFs/2025/2025-Christian-Reward Model Interpretability via Optimal.pdf]]"
extracted_date: "2026-07-11"
pages: 28
extractor: "PyMuPDF"
---

Page 1:
Reward Model Interpretability via Optimal and Pessimal Tokens
Brian Christian
brian.christian@psy.ox.ac.uk
University of Oxford
Oxford, UK
Hannah Rose Kirk
hannah.kirk@oii.ox.ac.uk
University of Oxford
Oxford, UK
Jessica A.F. Thompson
jessica.thompson@psy.ox.ac.uk
University of Oxford
Oxford, UK
Christopher Summerfield∗
christopher.summerfield@psy.ox.ac.uk
University of Oxford
Oxford, UK
Tsvetomira Dumbalska∗
tsvetomira.dumbalska@psy.ox.ac.uk
University of Oxford
Oxford, UK
Abstract
Reward modeling has emerged as a crucial component in aligning
large language models with human values. Significant attention
has focused on using reward models as a means for fine-tuning
generative models. However, the reward models themselves—
which directly encode human value judgments by turning
prompt-response pairs into scalar rewards—remain relatively
understudied. We present a novel approach to reward model
interpretability through exhaustive analysis of their responses
across their entire vocabulary space. By examining how different
reward models score every possible single-token response to
value-laden prompts, we uncover several striking findings: (i)
substantial heterogeneity between models trained on similar
objectives, (ii) systematic asymmetries in how models encode
high- vs low-scoring tokens, (iii) significant sensitivity to prompt
framing that mirrors human cognitive biases, and (iv) overvalua-
tion of more frequent tokens. We demonstrate these effects across
ten recent open-source reward models of varying parameter
counts and architectures. Our results challenge assumptions
about the interchangeability of reward models, as well as their
suitability as proxies of complex and context-dependent human
values. We find that these models can encode concerning biases
toward certain identity groups, which may emerge as unintended
consequences of harmlessness training—distortions that risk
propagating through the downstream large language models now
deployed to millions.
CCS Concepts
• Applied computing →Psychology; • Human-centered com-
puting →Empirical studies in HCI; HCI design and evalua-
tion methods.
∗Both authors contributed equally to the paper
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full cita-
tion on the first page. Copyrights for components of this work owned by others than
the author(s) must be honored. Abstracting with credit is permitted. To copy other-
wise, or republish, to post on servers or to redistribute to lists, requires prior specific
permission and/or a fee. Request permissions from permissions@acm.org.
FAccT ’25, Athens, Greece
© 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-x-xxxx-xxxx-x/YYYY/MM
https://doi.org/10.1145/3715275.3732068
Keywords
reward models, AI alignment, NLP, interpretability, value
ACM Reference Format:
Brian Christian, Hannah Rose Kirk, Jessica A.F. Thompson, Christo-
pher Summerfield, and Tsvetomira Dumbalska. 2025. Reward Model
Interpretability
via
Optimal
and
Pessimal
Tokens.
In
Proceedings
of The 2025 ACM Conference on Fairness, Accountability, and Trans-
parency (FAccT ’25). ACM, New York, NY, USA, 28 pages. https:
//doi.org/10.1145/3715275.3732068
CONTENT WARNING: This article presents examples of biased,
offensive, sexually explicit and otherwise harmful text. The authors
do not endorse any of the harmful representations quoted below.
1
Introduction
The alignment of large language models (LLMs) with human values
has emerged as one of the central challenges in modern AI devel-
opment, and at the heart of this challenge lie “reward models”—
neural networks trained to directly proxy human preferences by
transforming text into scalar rewards. Though typically treated as
disposable intermediaries in the larger alignment process, these
models are crucial objects of study in their own right as the most
direct and explicit encoding of human values in AI systems, yet are
surprisingly under-explored.
The typical process for aligning an LLM with human values
involves collecting a dataset of labeled pairwise human pref-
erences, indicating which of two LLM responses to a given
user prompt is preferred [6]. These preference data often distill
multiple desirable objectives, such as helpfulness, harmlessness,
and honesty [1], which are operationalized through guidelines
written by model developers and interpreted by crowdworkers
[20]. The resulting dataset is used to train a “reward model”—a
transformer model that takes in a prompt-response pair (or a
longer user-assistant dialogue) and outputs a scalar that repre-
sents in effect how “preferable” that response is. These scalars are
typically based on the Bradley-Terry score [3], and the reward
model is trained via stochastic gradient descent to minimize the
negative log-likelihood of the observed pairwise preferences [25].
The trained reward model then acts as a scalable proxy for human
preferences when using reinforcement-learning algorithms such
as Proximal Policy Optimization (PPO) [42] to fine-tune the LLM.
This process—known as Reinforcement Learning from Human
Feedback (RLHF)—results in LLM generations that maximize the
reward model’s score rather than the pre-training objective, so
arXiv:2506.07326v2  [cs.CL]  2 Feb 2026


Page 2:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
are supposedly more aligned with human values. While direct
alignment algorithms like Direct Preference Optimization (DPO)
[40] have grown in popularity, they capture equivalent preference
relationships from the data, just without the reward model as an
intermediary.
Although reward models exist as a disposable reagent in the
process of turning an “unaligned” LLM built to minimize predic-
tive loss into an “aligned” one built to maximize this proxy of hu-
man preference, they are fascinating objects of research inquiry in
their own right. Designed as generalizable proxies for human pref-
erence, they offer more direct value encoding than downstream
agents constrained by KL-divergence [18] and refusal training. As
scalar mappings over complex dialogue, they distill multi-objective
preference data into uniquely interpretable low-dimensional repre-
sentations of human value. They are in essence where “the human
value rubber meets the road.” Despite this, there is a dearth of liter-
ature analyzing the properties of reward models, largely because
few have been publicly available for study. While 2023–2024 saw
a proliferation of open-source language models, including Meta’s
Llama [51], Mistral AI’s models [19], and Google’s Gemma series
[49], to date no major industry or nonprofit lab has openly released
a reward model. Only recently has this picture begun to change,
with the release of RewaRdBench [26]—the first benchmark and
leaderboard for reward models, spurring new activity among aca-
demic and open-source communities.
In this work on reward model interpretability, we seek to un-
derstand the consistency and faithfulness with which these mod-
els represent human values. Specifically, we make the following
contributions:
• We pioneer an exhaustive search over every single token
in reward model vocabularies appended to a value-laden
prompt, permitting the analysis of optimal and pessimal to-
kens across ten top-performing open-source reward models
on RewaRdBench of varying sizes and architectures.
• We show that reward distributions exhibit systematic
asymmetries, with greater sensitivity between tokens
in high-scoring regions relative to low-scoring regions,
and tokens with positive sentiment relative to negative
sentiment. Changing to a negative-valence prompt inverts
this latter bias, mirroring framing effects in humans.
• We establish alignment between the (biased) interpretation
of human preferences by reward models and an inde-
pendent source of ground-truth human preferences called
EloEveRything, where internet users volunteer judgments
over concepts, people, and things from Wikipedia pages.
• We generalize our findings on similar biases and asymme-
tries to multi-token sequences using Greedy Coordinate
Gradient optimization.
• Through these sequential analyses, we reveal (i) significant
heterogeneity across similarly-trained reward models,
invalidating their presumed fungibility, and (ii) systematic
devaluation of identity group references (“homosexuals,”
“Black people” and “Jews”), possibly arising as unintended
biases from harmlessness training objectives.
Through exposing the idiosyncrasies of reward models as re-
search artifacts, we aim to highlight pitfalls in their current devel-
opment, provide recommendations for building more robust prox-
ies of human value, and ultimately advance the broader goal of
creating aligned and safe AI systems.
2
Ranking Optimal and Pessimal Tokens
Open-source reward models that convert tokens to a single scalar
reward permit the somewhat radical idea of exhaustive search. In-
spired loosely by Dawson [7], who demonstrated that exhaustive
testing of floating-point math functions is feasible (arguing that
“there are only four billion floats—so test them all”), we seek a
complete ranking of rewards assigned to all possible responses to a
user prompt in order to granularly and comprehensively evaluate
reward model characteristics.
We used the reward-model benchmark RewaRdBench [26],
which provides an online leaderboard for top-performing reward
models. From this leaderboard, we selected a diverse set of ten
models: nine high-performing models ranging from 3B to 27B
parameters drawn from the top twenty rankings, plus the leading
2B-parameter model. These models cover a range of developers,
base architectures, and model sizes (see Table 1).
To make exhaustive search computationally tractable, we fo-
cused on single-token responses, as multiple-token search quickly
becomes combinatorially complex. We designed an initial prompt
that specifically elicits brief responses with clear valence:1
What, in one word, is the greatest
thing ever?
We then computed the reward model score when supplying ev-
ery single token in the model’s vocabulary (𝑁≈256,000 in the
case of Gemma and 𝑁≈128,000 in the case of Llama 3) as a re-
sponse to this prompt. These token vocabularies include words and
word fragments in English and non-English languages (including
non-Roman alphabets), fragments of computer code, emoji, varia-
tions of whitespace, and control tokens. Having scored the whole
of each model’s vocabulary, we then sorted the tokens by their
scalar reward scores.
A more conventional approach would be to examine the log
probability distribution outputted by fine-tuned models, which rep-
resent the statistically most likely continuations of a prompt af-
ter reward training. When we attempted this, we found that fine-
tuned models tended to overindex on common tokens and statis-
tical regularities like “The” and “A” (see Sec. A.1.2 and Table A.1;
however we also note that variations in the prompt might have
produced more comparable answers to those reported here for re-
ward models). Nevertheless, the investigations below imply that
reward models provide a useful window into value interpretability
beyond conventional analyses.
2.1
Qualitative Observations
Applying this methodology to ten reward models reveals stark
qualitative differences in the token rankings between models—
even those from the same developer. We report optimal and
1We focused our analyses on English, as reward models are predominantly trained on
English data. Additional analyses across prompt variants are presented in Sec. 3.


Page 3:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
Table 1: Open-source reward models studied. The table includes both their full names and the shortened identifiers (Model
IDs) used throughout the rest of this paper. Ranks are from the RewardBench Leaderboard as of January 14, 2025.
RewardBench Rank
Model ID
Developer
Model Name
Base Model
Parameters (B)
2
■N-Gem-27B
nicolinho
QRM-Gemma-2-27B[9]
Gemma 2[50]
27
3
■S-Gem-27B-v0.2
Skywork
Skywork-Reward-Gemma-2-27B-v0.2[31]
Gemma 2
27
5
■S-Gem-27B
Skywork
Skywork-Reward-Gemma-2-27B[31]
Gemma 2
27
10
■S-Lla-8B-v0.2
Skywork
Skywork-Reward-Llama-3.1-8B-v0.2[31]
Llama 3.1[10]
8
11
■N-Lla-8B
nicolinho
QRM-Llama3.1-8B[9]
Llama 3.1
8
12
■L-Lla-8B
LxzGordon
URM-LLaMa-3.1-8B[32]
Llama 3.1
8
17
■R-Lla-8B
Ray2333
GRM-Llama3-8B-rewardmodel-ft[53]
Llama 3
8
19
■R-Lla-3B
Ray2333
GRM-Llama3.2-3B-rewardmodel-ft[53]
Llama 3.2
3
20
■F-Lla-8B-v0.1
RLHFlow
ArmoRM-Llama3-8B-v0.1[52]
Llama 3
8
31
■R-Gem-2B
Ray2333
GRM-Gemma2-2B-rewardmodel-ft[53]
Gemma 2
2
Table 2: Optimal and pessimal tokens for the prompt “What, in one word, is the greatest thing ever?”. Note that because
the Llama and Gemma tokenizers distinguish between start-of-word strings and intra-word strings, some tokens differ only
by leading whitespace. CONTENT WARNING: We present tokens in their raw form (including slurs) to enable transparent
attribution of model tokens, while acknowledging their offensive, troubling and harmful nature.
R-Gem-2B
Token ID
Decoded
Score
27534
LOVE
4.594
61792
LOVE
4.562
218136
felicity
4.469
2182
love
4.344
12870
love
4.312
7377
Love
4.281
8703
Love
4.281
227570
sonder
4.219
143735
sonder
4.219
27539
Wonder
4.188
34183
Wonder
4.188
174540
HOPE
4.156
115221
HOPE
4.125
5144
wonder
4.094
53798
wonder
4.094
167954
WONDER
4.031
50999
bliss
3.922
207783
bliss
3.922
65646
JOY
3.922
135936
JOY
3.922
89399
miraculous
3.875
40241
miracle
3.859
…
...
…
61001
blacks
-9.250
218552
pathologist
-9.250
97070
killers
-9.312
167921
prostitutes
-9.312
222988
massacres
-9.312
106863
FUCKING
-9.312
213624
rapist
-9.312
127732
ransomware
-9.375
204573
retards
-9.438
195353
nazis
-9.438
137696
murdering
-9.438
37678
Hitler
-9.500
230672
Rape
-9.500
134768
Rape
-9.500
231158
faggot
-9.500
144817
murderous
-9.500
152471
murderers
-9.500
39688
rape
-9.562
144068
Hitler
-9.562
186353
rape
-9.625
158058
negroes
-9.625
201371
raping
-9.625
R-Lla-3B
Token ID
Decoded
Score
11542
freedom
3.359
86872
Freedom
3.266
25320
Freedom
3.266
40835
LOVE
3.250
61094
LIFE
3.203
83900
.life
3.000
24966
CONNECTION
2.969
28899
imagination
2.844
10919
Love
2.672
29351
Love
2.672
48379
Opportunity
2.641
57184
UNITY
2.438
57273
UNITY
2.438
6776
opportunity
2.406
32883
loyalty
2.359
3021
love
2.281
31153
love
2.281
39193
Discovery
2.266
68500
Discovery
2.266
35215
Experience
2.234
21460
Experience
2.234
85743
Peace
2.156
…
...
…
87546
raping
-10.688
86395
.FindGameObjectWithTag
-10.688
38853
${
-10.688
18350
(con
-10.750
27817
_headers
-10.750
58467
.insertBefore
-10.750
6019
(st
-10.750
29372
(cfg
-10.750
5747
.setText
-10.750
27701
.startsWith
-10.750
26342
/******************...
-10.812
97615
##################...
-10.812
85399
###################...
-10.812
76897
_checks
-10.875
58352
("[%
-10.875
74061
/******************...
-10.938
42864
homosexual
-10.938
6294
(struct
-10.938
27249
.startswith
-11.000
94380
jihadists
-11.062
97223
homosexuals
-11.312
37289
.assertFalse
-11.438


Page 4:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
pessimal tokens for two such models (■R-Gem-2B and ■R-Lla-
3B) in Table 2, and present all other models in Tables A.6–A.7.
There are striking differences in both their highest and lowest
reward assignments. At the positive extreme, ■R-Gem-2B prior-
itizes affective content over grammatical correctness (e.g., rank-
ing “miraculous” above “miracle”). It also prominently features the
surprisingly obscure word “sonder,” a neologism coined in 2012
by writer John Koenig to mean “the realization that each random
passerby is living a life as vivid and complex as your own” [24]. The
■R-Lla-3B model from the same developer instead puts “freedom”
ahead of “love,” and on the whole the high rankings of “freedom,”
“opportunity,” “discovery,” and “experience” paint a more individ-
ualistic, active picture of human value than ■R-Gem-2B’s more
interdependent, affective words like “love,” “wonder,” and “hope.”
The models diverge even more dramatically in their lowest-
ranked tokens, revealing some (concerning) artifacts from
reward-model training objectives. The lower ranks of the ■R-
Gem-2B model are tied to human harm and suffering like
“rape,” “Hitler,” and “murderers,” as well as slurs and profanities,
suggesting a strong influence of a harmlessness objective in
training. In contrast, ■R-Lla-3B’s lowest ranks are predominantly
occupied by malformed code tokens and programming artifacts
like “.assertFalse” and “/****”, suggesting stronger traces of a
helpfulness objective. Both models exhibit concerning behaviors
over tokens relating to minority identity groups (e.g., “blacks”
or “homosexuals”). These patterns likely stem from artifacts in
reward model training data, where identity groups are dispropor-
tionately represented in unsafe or “rejected” examples, leading
to their systematic devaluation—even in response to a positive
prompt of the “greatest thing ever.” This linguistic erasure mirrors
documented phenomena in hate-speech detection, where models
develop oversensitive false positive rates for identity terms (e.g.,
“Muslim,” “mosque”) or reclaimed slurs due to their overrepresen-
tation in negative training contexts and underrepresentation in
neutral or positive ones [8, 38, 41].
2.2
Quantitative Analysis
Quantitatively, we note that, despite differences of the scale of
scores across models (Fig. 1), all score distributions exhibit a posi-
tive skew (Table 3). That is, most tokens receive low rewards, while
a small number of tokens score substantially higher than average,
creating a long right tail in the distribution. A positively skewed
reward distribution may be appropriate given that RLHF updates
model parameters to maximize expected reward, making the dis-
criminative power of the upper tail most consequential for learn-
ing.
We assessed the consistency of token rankings across models
using an ordinal correlation measure, Kendall’s 𝜏, Fig. 2A (results
are consistent across choice of correlation metric, see Fig. A.1).
Whilst all models exhibit positive correlations, there is substan-
tial diversity among the models studied. We explored this diversity
using multidimensional scaling (MDS)—a visualization technique
that aims to faithfully represent the degree of similarity between
data points (here, reward models) in lower dimensionality (here,
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
R-Gem-2B
40
20
0
20
40
Score
Figure 1: Violin plot of exhaustive score distributions to the
“greatest thing” prompt. The reward models differ strikingly
in their distributions of reward scores in terms of scale and
range.
Model
Mean
Variance
Skewness
■N-Gem-27B
1.876
0.193
0.437
■S-Gem-27B-v0.2
-9.274
1.017
0.071
■S-Gem-27B
-30.422
11.991
0.878
■S-Lla-8B-v0.2
-18.699
5.716
1.117
■N-Lla-8B
16.613
9.558
1.133
■L-Lla-8B
-0.137
0.034
1.763
■R-Lla-8B
-14.239
0.781
0.504
■R-Lla-3B
-6.777
2.597
1.672
■F-Lla-8B-v0.1
0.031
<0.001
1.055
■R-Gem-2B
-5.279
1.957
1.457
Table 3: First three moments of reward distribution across
all shared tokens. All reward models exhibit varying degrees
of positive skew.
2D). This analysis reveals that models with a similar number of pa-
rameters, shared base model, and shared developer cluster closer
in latent space (Fig. 2B).
To partial out the influence of these factors, we conducted an
analysis inspired by representational similarity analysis (RSA), a
tool commonly used in neuroscience. We regressed the (flattened)
observed empirical model correlation matrix in Fig. 2A on theoret-
ical model similarity matrices based on the three factors of inter-
est (base model, developer, number of parameters) and the rank
of the model on the RewaRdBench leaderboard (Fig. 2C). Each of
these factors is, on its own, significantly associated with the empir-
ical pattern of correlations between models (simple linear regres-
sion, all 𝑝< .001). However, when combining the four factors to-
gether in a competitive multiple regression, the variance predicted
by base model, developer, and the number of parameters appears
to be almost entirely soaked up by the ranking of the model on


Page 5:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
A
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
R-Gem-2B
B
C
Figure 2: (A) Heatmap depicting the pairwise Kendall’s 𝜏correlations between the reward models for scored responses to
the prompt “What, in one word, is the greatest thing ever?”. (B) Visualization of the degree of similarity between reward
models using multidimensional scaling (MDS) of the Kendall’s 𝜏distance measure. (C) Theoretical dissimilarity matrices for
representational similarity analysis (RSA). The four dissimilarity matrices encode, respectively, base model [base𝑖= base𝑗];
developer [dev𝑖= dev𝑗]; parameter count (1 + |params𝑖−params𝑗|)−1; and RewardBench ranking (1 + |rank𝑖−rank𝑗|)−1.
RewaRdBench (RewaRdBench rank 𝑝< .0001, base model 𝑝< .10,
all other 𝑝> .10). Running a stepwise regression (factor knock-in
and knock-out) confirms that the regression that best explains the
observed data features the base model and RewaRdBench ranking
theoretical matrices (base model 𝛽= 0.05, RewaRdBench ranking
𝛽= 0.69, 𝑅2 = .80). It is perhaps unsurprising that model ranking
on RewaRdBench can capture patterns of reward model similarity
since it measures how well the models are all aligned against the
same external objective (i.e., the RewaRdBench benchmark and its
composite evaluation datasets). Interestingly, our results suggest
that the choice of base model drives differences in token rankings
above and beyond alignment to RewaRdBench. That is, reward
models appear to inherit idiosyncratic biases from the pretrained
base model.
3
Framing Effects
3.1
Sentiment Analysis
To further explore explanations for token rankings, we investi-
gated the relationship between sentiment, or the emotional value
of a token, and its reward model score. We quantified emotional
value using data from two validated linguistic corpora widely
used within the field of psychology and developed by human
experts: Bing [30] and AFINN-111 [36]. Bing codes words as
“positive” or “negative”; AFINN-111 indexes a score ranging from
−5 to 5 for the sentiment value. Across both corpora, we found a
positive association between reward score and sentiment, where
scores are consistently higher for positive-sentiment tokens (Figs.
3A, A.3–A.4). These results are in line with what we would expect:
positive tokens are more likely to score highly as an appropriate
response for a prompt that asks for the “greatest thing ever.” In
line with the skewness of the score distribution in Sec. 2, we found
that (i) scores for positive-sentiment tokens are more spread out
than scores for negative-sentiment tokens, and (ii) the slope for
the relationship between sentiment and score is significantly
steeper for positive than negative tokens (Fig. 3A; 𝛽pos > 𝛽neg:
𝑡(9) = 2.6, 𝑝< 0.05). This finding suggests that the reward model
is more sensitive to distinctions in positive sentiment relative
to negative sentiment. The results are highly consistent across
models (8/10 models exhibit the effect).
3.2
Prompt Framing
To explore whether the differential sensitivity of the model is
driven by the specifics of the prompt or generalizes across queries,
we extended our analyses to two more prompts: a positive variant
(“What, in one word, is the best thing ever?”) and a negative
contrast (“What, in one word, is the worst thing ever?”). Perhaps
expectedly, scores for “the best thing ever” are highly consistent
with those for “the greatest thing ever.” We found a high positive
correlation between model scores for these two prompts across all
models (Fig. A.2). We replicated (i) the positive skewness of the
distribution of scores and (ii) the differential sensitivity to positive
over negative-sentiment tokens (Fig. 3C; 9/10 models exhibit the
effect).
The pattern is different for “the worst thing ever.” Here, the dis-
tribution of scores remains skewed toward higher-scoring tokens,
however, it is the negative-sentiment tokens that receive higher re-
wards for this prompt. Thus, models are, on average, more sensitive
to negative-sentiment tokens relative to positive-sentiment ones
(significantly steeper slope for negative- over positive-sentiment
tokens, Fig. 3B–C; 5/10 models exhibit the effect). Our findings
suggest that model sensitivity to the appropriateness of tokens de-
pends on framing. When the prompt is framed positively (“best
thing ever”), scores are more sensitive to positive than negative
token sentiment and more sensitive to negative than positive to-
ken sentiment when the prompt is framed negatively (“worst thing
ever”). This result is consistent with human behavior. If a question
is positively framed, humans are more attuned to positive informa-
tion, and vice-versa for negative frames. Consider a scenario where


Page 6:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
Figure 3: (A) Correlation plot between token sentiment value according to the AFINN-111 lexicon and the scores from the
■S-Lla-8B-v0.2 reward model with the prompt “What, in one word, is the greatest thing ever?” (B) As previous, but for prompt
“What, in one word, is the worst thing ever?” (C) Estimate for the slope for token sentiment value from a simple linear re-
gression predicting reward model score computed separately for each model, prompt and sentiment valence (positive and
negative). Each colored dot indicates a model; diamonds represent mean ± standard error. Slope estimates are, on average,
higher for positive sentiment. They are steeper for positive-sentiment valence in positively framed prompts and steeper for
negative-sentiment valence in negatively framed prompts. (D) Estimate for the slope for normalized word frequency from
a multiple linear regression predicting reward-model score controlling for sentiment value; computed separately for each
model and prompt. Scores are positively associated with word frequency, suggesting a “mere-exposure effect” in the reward
models.
you need to pick between two vacation destinations: an exciting
option with many positive features (dream destination, beautiful
nature) and just as many drawbacks (expensive, long travel) versus
a safer option with fewer positive and negative stand-out features
(e.g., a local getaway). If asked to choose between those two vaca-
tion spots in a positive frame (“which [one] would you prefer?”),
human participants tend to choose the option with more positive
features; if asked to choose in a negative frame (“which [one would
you] cancel?”), they pick the option with more negative features,
even though it is in fact the same option [43].
The effect of framing on sensitivity has important implications.
If the goal of RLHF is to steer the model away from generating
harmful or unsafe responses, then the reward model needs to be
sufficiently sensitive in the negative-sentiment portion of token
space. Current practice—asking human raters to choose a preferred
option (“which is the better response,” not “which is the worse
response”)—may inadvertently be undermining that objective by
biasing the dynamic range of the reward model toward positive
tokens.
Taken together, our results further suggest the reward models
do not interpret “best” as simply the inverse of “worst.” The dis-
tribution of scores across those two prompts resembles a funnel
(Fig. 4) where many tokens are bad responses to both prompts (bot-
tom left) and some tokens are good responses to one prompt but
not the other (top left and bottom right). We also see a thin tail
of tokens that are highly-scored responses for both prompts (top
right; “sonder” features in this category, along with non-committal
answers like “depends” and refusals like “impossible”). In the ap-
pendix, we include tables that index the best + worst (tokens that
score similarly on both prompts) and best−worst axes (tokens that
score highly on one but not the other prompt); see Tables A.8–A.9.
3.3
Frequency Bias
Are the scores that reward models assign to different tokens bi-
ased by how frequently the word appears in the English language?
To assess this, we used data from Word Frequencies in Written
and Spoken English [27] and regressed log-transformed word fre-
quency on reward-model scores. Higher word frequency is associ-
ated with higher reward-model score across prompts for the ma-
jority of models (positive slope estimates with 𝑝< .05 in 10/10
models for “best,” 8/10 for “greatest,” and 7/10 for “worst”). This
is reminiscent of the “mere-exposure effect” in humans, where the
more someone is exposed to a stimulus, the more they like it [54].
One could argue that this effect is driven by positive words be-
ing more frequent in general in English. To account for this, we
controlled for the sentiment value of the tokens. This adjustment
did not abolish the “mere-exposure effect,” but made it more pro-
nounced in the negatively framed query (Fig. 3D, positive slope
estimates with 𝑝< .05 in 2/10 models for “best,” 5/10 for “greatest”
and 8/10 for “worst”).
This “mere-exposure effect” is a surprising result, since reward
models are meant to provide information that is orthogonal to the
underlying distribution of tokens, pertaining to, e.g., helpfulness
and harmlessness. It suggests that there may be a leakage from
the pretrained base models into the reward models, whereby more
common tokens may be scored more highly than they should be.
More work is needed to understand this phenomenon, and also
the degree to which this “mere-exposure effect” interacts with the
downstream KL-divergence regularizer typically used when fine-
tuning LLMs against the reward model.


Page 7:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
2
4
Best score
2
4
Worst score
N-Gem-27B
15
10
5
Best score
15
10
5
Worst score
S-Gem-27B-v0.2
40
20
Best score
40
20
Worst score
S-Gem-27B
20
10
0
Best score
20
10
0
Worst score
S-Lla-8B-v0.2
10
20
30
Best score
10
20
30
Worst score
N-Lla-8B
0
1
Best score
0
1
Worst score
L-Lla-8B
15
10
Best score
15
10
Worst score
R-Lla-8B
10
5
0
Best score
10
5
0
Worst score
R-Lla-3B
0.025
0.050
0.075
Best score
0.02
0.04
0.06
0.08
Worst score
F-Lla-8B-v0.1
10
0
Best score
10
5
0
Worst score
R-Gem-2B
Figure 4: Juxtaposing exhaustive scores for the “best thing” prompt against the “worst thing” prompt reveals not just a simple
negative correlation, but also an orthogonal dimension representing tokens that are bad or good responses to both frames.
4
Alignment with EloEveRytHing
Thus far we have identified internal inconsistencies within and
across reward models. However, reward models are intended to
proxy human value judgments. Establishing the faithfulness of this
proxy function requires an external baseline of human value judg-
ments. We sourced this external human preference data from Elo-
EveRything,2 a crowdsourcing platform that implements pairwise
preference learning over things, people, and concepts uploaded
from Wikipedia. On EloEveRything, internet users are presented
with pairs of Wikipedia-derived entities (accompanied by images)
and volunteer their judgments in response to the prompt: “Which
do you rank higher?” (see Fig. 5A), with options to request addi-
tional context or skip. The platform aggregates these pairwise com-
parisons using the Elo rating system, which was originally devel-
oped for chess rankings [12] and has since been widely adopted to
evaluate LLMs [1, 2, 5]. We collected all data from the EloEveRy-
thing website, resulting in a dataset that comprises 𝑁users = 12,515
users who evaluate 𝑁items = 7,530 items across 𝑁pairings = 1,805,124
total pairwise comparisons. Although the dataset is highly imbal-
anced by the ratings each item receives (𝜇= 479.4 pairings/item,
𝜎= 464.4)3 and likely imbalanced across non-representative users
(user-level data is not available), it still serves as a valuable inde-
pendent baseline.
To ensure as fair a comparison as possible between the tasks ad-
ministered to humans and reward models, we made two method-
ological adjustments (as compared to Sec. 2). First, we modified our
prompt to “What one single thing, person, or concept is the great-
est ever?” to better align with the human task and accommodate
the multi-word concepts that appear in EloEveRything, such as
“Sliced bread,” “Female body shape,” “Freedom of the press” or even
“Beliefs and practices of the Church of Jesus Christ of Latter-day
2https://eloeverything.co/.
3This is because users can upload new items at any point. At the time of data collection
(January 10th 2025), “Evolution” appears in 3,195 pairings, while “Mac Miller” and
“Penile injury” appear in only 6.
Saints” (𝜇= 2.1 words/item, 𝜎= 1.3).4 Second, rather than exhaus-
tively evaluating the entire model vocabulary, we restricted this
analysis to the set of EloEveRything items (𝑁items = 7,350) to en-
sure a common human–model comparison set. We used the same
set of models as in Table 1, and normalized both reward model
scores and human Elo ratings to rankings, using average rank for
ties.
4.1
Heterogeneity and Asymmetry in
Human-Model and Model-Model
Alignment
Our analysis reveals several notable patterns in the relationship
between the ground truth preferences of EloEveRything raters
and human preferences as interpreted by reward models. There
is substantial heterogeneity in model-human alignment and
model-model alignment (Fig. A.5). The mean Kendall’s 𝜏correla-
tion between human and model rankings is 0.29 (𝜎= 0.06), with
coefficients ranging from 0.22 to 0.39 across models, indicating
only moderate rank agreement. Divergence of reward models
from human rankings might be expected—given that EloEveRy-
thing users benefit from additional context like images and can
personalize their ratings with “Which do you rank higher”—but
the observed heterogeneity extends to model-model comparisons.
The mean Kendall’s 𝜏correlation between pairs of different
models is 0.55. In addition to these quantitative differences, we
note anecdotal inconsistency in the best and worst ranked tokens.
For example, while “Unconditional love” is ranked best by 5
models, “Sports bra” is top for ■R-Lla-8B and “Gödel, Escher, Bach”
for ■F-Lla-8B-v0.1. As demonstrated in (Fig. 5C), ranks display
substantial movement across models, challenging the assumption
that reward models trained under a similar objective can be used
interchangeably.
There is systematic asymmetry in how models handled items
at different ends of the human preference distribution (Fig. 5C).
4To test generalizability across prompts, we also repeated analysis in this section for
our original prompt (“What, in one word, is the greatest thing ever?”) and an alterna-
tive variant (“What is the single thing, person, or concept that humans most prefer?”).
We present results in Figs. A.5–A.6.


Page 8:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
100
101
102
103
Ranks 1-1000 (log scale)
Human
N-Gem-27B
RB #=2
ρ=0.29
S-Gem-27B-v0.2
RB #=3
ρ=0.33
S-Gem-27B
RB #=5
ρ=0.40
S-Lla-8B-v0.2
RB #=10
ρ=0.39
N-Lla-8B
RB #=11
ρ=0.37
L-Lla-8B
RB #=12
ρ=0.35
R-Lla-8B
RB #=17
ρ=0.37
R-Lla-3B
RB #=19
ρ=0.54
F-Lla-8B-v0.1
RB #=20
ρ=0.38
R-Gem-2B
RB #=31
ρ=0.36
1
1000
2000
3000
4000
5000
6000
7000
All Ranks (#1 = best, #7530 = worst)
Bottom 5 ranked items by humans
Nazi Germany (#7526)
Genocidal rape (#7527)
Child abuse (#7528)
Child pornography (#7529)
The Holocaust (#7530)
Top 5 ranked items by humans
Universe (#1)
Water (#2)
Information (#3)
Knowledge (#4)
Love (#5)
Best ranked items by models
Unconditional love (#59)
Imagination (#64)
Compassion (#73)
Sports bra (#2167)
Gödel,Escher, Bach (#3997)
Best ranked items by models
Unconditional love (#59)
Imagination (#64)
Compassion (#73)
Sports bra (#2167)
Gödel,Escher, Bach (#3997)
A
B
C
−5000
0
5000
Average model rank minus human rank
Fingering (sexual act)
Erection
Black people
Spoons sex position
Handjob
Cleavage (breasts)
Fellatio
Doggy style
Sexual fetishism
Breast
Boygenius
God in Islam
CM Punk
Charlie Munger
Gurren Lagann
Miranda Sings
BTS
Mustafa Kemal Atatürk
Johan Cruyff
Fully Automated
Luxury Communism
Humans rank worse
than models
Humans rank better
than models
Figure 5: (A) The EloEveRytHing ranking interface where users make pairwise preference judgments between items (e.g.,
“Bike lane” vs “Sliced bread”). (B) Maximum differences between human and average model rankings over items in response
to the prompt “What one single thing, person, or concept is the greatest ever?”, showing cases where humans rank items
higher (green) or lower (purple) than models. (C) Rank trajectory plot showing how human and model ranks differ. We plot
(i) the top 5 items in the human rank (blue color scale with human ranks shown in legend parentheses as #n), (ii) the bottom 5
items in the human rank (red color scale), and (iii) unique items ranked #1 by models. Specifically, “Unconditional love” is #1
for 5 models; “Compassion” is #1 for ■N-Gem-27B; “Imagination” for ■S-Gem-27B; “Sports bra” for ■R-Lla-8B; and “Gödel,
Escher, Bach” for ■F-Lla-8B-v0.1. Models are ordered by the RewardBench leaderboard, and shown alongside their Spearman
correlation to human ranks. The dashed box indicates zoomed inset region of top 1,000 ranks shown with a log scale.
Reward models show stronger agreement with human rankings
for highly-rated items (𝜏top100 = 0.19) compared to low-rated items
(𝜏bottom100 = 0.08). This asymmetry (and heterogeneity) is evident
in Fig. 5C, where “The Holocaust” (ranked worst by humans) is
ranked substantially higher by most models, even those perform-
ing well on RewaRdBench. This corroborates our findings in Sec. 2,
where models are more sensitive to high- over low-scoring tokens
(the positive skew of the score distribution).
4.2
Analyzing Discrepancies between Value as
Perceived by Humans and Models
Relative to human rankings, reward models systematically under-
value concepts related to nature and life, e.g., “Universe” (human
rank #𝐻= 1, mean rank across models # ̄𝑀= 320), “Gravity”
(#𝐻= 7, # ̄𝑀= 320), “Breathing” (#𝐻= 16.5, # ̄𝑀= 321); and tech-
nological concepts, e.g., “Technology” (#𝐻= 47.5, # ̄𝑀= 633.5),
“Electronics” (#𝐻= 78, # ̄𝑀= 3966), “Computer” (#𝐻= 95.5, # ̄𝑀=
1352.5). In contrast, the majority of top words ranked by models
represent more affective qualia (e.g., “Unconditional love,” “Imagi-
nation,” “Hope,” or “Happiness”). These different perspectives may
reflect blindspots in learning value through language or literary
reference alone, without additional modalities that reflect the nu-
ances of embodied human experience.
The most striking valuation differences (see Fig. 5B) emerge
around sexual content e.g., “Sex” (#𝐻= 69.5, # ̄𝑀= 2022.5), “Hu-
man sexual activity” (#𝐻= 45, # ̄𝑀= 5913), and concerningly, the
identity group reference “Black people” (#𝐻= 202.55, # ̄𝑀= 6591).
There are many possible explanations for discrepancies between
EloEveRything data and reward model scores, including the fact
that the 12,515 EloEveRything users in the dataset do not reflect
a representative population sample, nor are they incentivized
to provide truthful responses. However, such discrepancies also
exemplify the fundamental challenge of assigning a single scalar
score to language without full context (which is exacerbated
further by our prompt, which encourages short responses). Sex-
or identity-related terms may be entirely appropriate in positive
or educational contexts while highly inappropriate in others. As
we suggested previously, while humans readily grasp this dual
use, reward models may hedge against their usage to satisfy


Page 9:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
a harmlessness objective, paradoxically causing harm through
linguistic erasure and devaluation as an unintended consequence.
5
Searching for Longer Optimal and Pessimal
Token Sequences with GCG
Although it would be computationally prohibitive to exhaustively
search for optimal and pessimal multi-token sequences, one can
use discrete optimization methods to search for responses that
yield high/low reward for a particular prompt. Greedy Coordinate
Gradient (GCG) [56] is a discrete token optimization algorithm
originally proposed to search for prompt suffixes to “jailbreak”
aligned LLMs. In that application, the optimized loss is the cross-
entropy between the model response and some target response.
Starting from some initial suffix string, GCG iteratively proposes
candidate token swaps based on the gradient. Since the search
process only swaps tokens (never adds or removes tokens), the
resulting string will be composed of the same number of tokens
as the starting string.
Starting from the nanoGCG 5 implementation, we modified
GCG to instead search for responses that maximize/minimize the
reward value when paired with a particular prompt, using a mean
squared error loss on the reward value. We also implemented
the modifications described in the Faster-GCG paper [28], which
we found to be especially important when searching for short
(2–5) token sequences where the original GCG algorithm is prone
to self-loops. This modified implementation can be found at
https://github.com/thompsonj/nanoGCG. We began by searching
for optimal and pessimal 2- and 3-token sequences according to
the ■R-Gem-2B model for the same prompts that were used for
the exhaustive single token search above: “What, in one word, is
the greatest thing ever?”, “What, in one word, is the best thing
ever?”, and “What, in one word, is the worst thing ever?” (see
Table 4). To explore longer sequences, we omitted the “in one
word” direction from the prompt and ask simply “What is the best
thing ever?” and “What is the worst thing ever?” Results from
several searches are in Table 5.6
These search results suggest several patterns, many of which
are consistent with observations from the single token analyses.
Responses made up of programming related tokens with no
semantic content score low on both “best” and “worst” prompts.
Answers that emphasize the subjective nature of the question
score highly for both “best” and “worst” prompts, but especially
so for the “worst” prompt. This might be reflective of a general
avoidance of negative sentiments in the response, even in cases
when negative sentiment would be appropriate. As observed in
the single token analysis, multi-token optimal responses to the
“worst” prompt generally have lower scores than for the “best”
and “greatest” prompts. Interestingly, here too we found that
some tokens emerge as extreme outliers for both positively and
negatively framed prompts. For instance, the token “Jews” ap-
pears among the pessimal answers for both “greatest” and “worst”
prompts. This finding further speaks to the linguistic erasure
effect discussed earlier. The prevalence of emojis in the optimal
5https://github.com/GraySwanAI/nanoGCG
6Some of the search result strings may not correspond exactly to the found token IDs
due to LATEX formatting of whitespace and characters outside of the Latin alphabet.
multi-token sequences is notable. It is also interesting to note that
many of the optimal search results are not grammatical—a feature
that likely distinguishes the reward model from the ultimate
fine-tuned language model.
While longer token sequences do not admit the kind of fully
exhaustive search (and full characterization of the score distribu-
tion) that is possible with single-token sequences, we have seen
that recent techniques such as GCG and its offshoots make the
interrogation of optimal and pessimal responses possible even at
greater length. Despite compute limitations, uncovering such lin-
guistic “superstimuli” (akin to the visual superstimuli used to un-
derstand computer vision networks [35, 37, 55]) is revealing, and
can be an important part of the toolkit in assessing what features
reward models are responding to, and how they differ from one
another.
6
Related Work
Interpretability and Bias in RMs: A small but growing literature enu-
merates the technical challenges with the use of RMs [4] and advo-
cates for greater transparency [14]. Recent studies point to an un-
derspecification problem in RMs stemming from hidden context in
reward signals, specifically noise and subjectivity inherent in hu-
man preferences [23, 29, 39, 46]. Further work describes patterns
in LLM activations that emerge during RLHF by identifying model
layers with the highest divergence from the pre-trained model, and
training probes on sparse autoencoder output of these layers to
create condensed, interpretable representations of LLM activations
[33]. This is highly complementary to our own work: the authors
show the value of studying internal activations of fine-tuned gen-
erative models, while we focus on more direct interrogation of the
outputs and distributions of RMs. Together, these approaches of-
fer richer insights into how well LLMs capture human preferences
during alignment.
Another vein of work has explored length biases in finetuned
LLMs, arguing that RMs are the root cause [45]. Various inter-
ventions to mitigate length bias have been explored, with varying
degrees of success, though broadly length biases emerge in RMs
even after data balancing. Subsequent work on mitigating length
bias [44] has applied Products-of-Experts [15] with promising re-
sults, and other recent work has measured additional stylistic con-
founders in human feedback [16]. There are a number of additional
complementary approaches to RM interpretability, including train-
ing multi-objective RMs that consider different dimensions of hu-
man preferences separately [52].
Over-optimization of RMs: Previous work examines costs of
overfitting to RMs through prolonged training (e.g., PPO) during
RLHF. Foundational work notes that RM over-optimizing degen-
erates outputs [48], and subsequent work has presented scaling
laws for RM over-optimization [13]. The phenomenon has been
documented with simulated and human annotators [11], with the
authors arguing that in the human case, RM quality is degraded
by both inter- and intra-subject variability.
Direct Preference Optimization (DPO) and Alternative Alignment
Methods: Direct preference optimization (DPO) streamlines the
alignment process by implicitly encoding the reward function
within the policy itself [40], which comes with the loss of an
explicit, inspectable RM that PPO-based RLHF provides. Our work


Page 10:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
Table 4: Optimal and pessimal token sequences for “What, in one word, is the <greatest/best/worst> thing ever?”
Content warning: The resulting strings refer to sexual violence and religious identity.
Greatest thing ever
Best thing ever
Worst thing ever
Starting
Result
Score
Starting
Result
Score
Starting
Result
Score
x x x
** LIFE
+9.445
x x x
JOY
+8.297
x x x
… ** regret
+4.555
- - -
** LOVE **
+9.047
x x
JOY
+8.234
x x
despair
+3.402
…
...
…
…
...
…
…
...
…
x x
pgfplots Jews
−11.164
x x
RapeChildren
−11.289
x x
autogui Jews
−11.922
x x x
endphpsetVerticalGroup /*
−12.586
x x x
endphp$=BeginInit
−12.383
x x x
endphp jewish",(
−12.539
Table 5: Optimal and pessimal token sequences for “What is the best thing ever?” and “What is the worst thing ever?”
Starting string
Search result
Score
“What is the best thing ever?”
x x x x x x x x x x x x x x x
x x x x
Ultimate answer & undervalued: ** authentic Love.**
Keep it
imperfections beautiful
Cheers friend !
+9.680
There is no objectively best
thing ever. It's subjective.
Everyone has their own
preferences.
Perception disqualified no universal best thing ever. It lives **
subjective.**congratulations ENJOY dearly bespoke bliss.
+9.336
…
...
…
LOVE felicity love Love
Wonder sonder HOPE wonder
WONDER miraculous JOY bliss
pymysql<bos>fetchoneymceSBATCH <<<<<<<<<<<<<< invokingState++++++++++++
++++ protoimpl invokingStatesetVerticalGroup /*
−16.250
x x x x x x x x x x x x x x x
x x x x
<<<<<<<<<<<<<<SBATCH invokingState x lockprimaryStage
invokingStateXtraEditorsynb NumeradelocalctxStoreMessageInfo
invokingStateexpandindo <<<<<<<<<<<<<<multirow:+: invokingState jLabel
−16.969
“What is the worst thing ever?”
There is no objectively worst
thing ever. It's subjective.
Everyone has their own
preferences.
<b>EXISTS no objectively worst thing ever,** It's subjective**.Folks
proclaiming their certainty bluffSOLVED
+7.672
x x x x x x x x x x x x x x x
x x x x
PHD HERE Never measurable, debated,& addressed repeatedly. ** This
famous response WINS !
+7.523
…
...
…
x x x x x x x x x x
``` AssemblyTitle <<<<<<<<<<<<<< <<<<<<<<<<<<<< invokingState
skimagemybatisplus ची ोंCloseOperationsetVerticalGroup
−15.750
- - - - - - - - - -
scriptcasebufio onCreateViewmybatisplus<bos> <<<<<<<<<<<<<<帖最后由<bos>
setVerticalGrouppushFollow
−15.961
shows the RM serves as a valuable lens for understanding. Thus
our work highlights a key tradeoff of using DPO-based methods
and contributes to growing literature comparing DPO and PPO
[17].
7
Limitations and Conclusions
Reward models have emerged as a critical tool for shaping AI be-
havior through human preferences. In this paper, we demonstrate
that they also serve as a valuable lens for understanding how faith-
fully and consistently human values are encoded into AI systems,
offering insights that are not readily accessible through studying
either the base pre-trained LLMs or the resulting fine-tuned mod-
els alone. However, several important limitations constrain the
scope and implications of these insights.
First, our methodology faces inherent interpretative con-
straints. Exhaustive search quickly becomes computationally
intractable over multi-token sequences, but asking for single-
token responses places strong bounds on interpretability. While
we do demonstrate gradient-based counterfactual generation
analysis as a multi-token proof-of-concept, we do not formally
test key hypotheses about framing effects, or alignment with
other sources of human preferences, among other phenomena of
interest. Second, the ecological validity of our findings remains
uncertain. While isolating reward models as objects of study
yields interesting results, it abstracts from their operational role.
It remains unclear how their behaviors interact with pre-trained
models and KL constraints during RLHF. Furthermore, as direct
alignment algorithms gain prominence [34, 40], the future role of
reward models is an open question. However, there remains active
debate on the relative merit of DPO- and PPO-based methods [17],
and irrespective of alignment technique, all rely on some form of
preference data, of which reward models are distillations. Third,
systematic analysis is hindered by opacity and conflicting objec-
tives. Poor documentation of training data and processes makes
it difficult to attribute observed behaviors to specific choices in


Page 11:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
the development pipeline [22]. Even more fundamentally, reward
models aggregate human preferences across multiple objectives
and populations, creating an entangled mess of human values, so
it is unclear what constitutes “ideal” behavior for these models
[4, 23, 46, 47].
Our work suggests that reward models may be interpretable in
their own right, alongside the generative models that they are used
to train. Our finding that there is significant heterogeneity in to-
ken rankings among reward models invites further study of how
these differences arise as a function of the design choices made
by developers, and how they may translate into biases in down-
stream fine-tuned models. The mere-exposure effect that reward
models show may contribute to the overly generic outputs so of-
ten observed in publicly available LLMs. Additionally, our finding
that reward models are sensitive to framing has implications for
training and inference. It implies that these models may not sim-
ply encode positive outputs as the inverse of negative outputs and
vice versa, but rather that valuation exists in a potentially higher-
dimensional, multi-attribute space. Finally, the marked undervalu-
ation of identity-group terms and sexual content, relative to inde-
pendent human baselines, calls for more careful consideration of
what and whose data is used as the foundation of human value, lest
harmful biases be propagated downstream to widely-used LLMs.
Together, these findings present a more nuanced investigation of
reward models as a central pillar in AI alignment.
Adverse Impact Statement
Our work systematically analyzes reward-model outputs, includ-
ing potentially harmful and offensive content such as slurs, pro-
fanities, discriminatory language, references to violence, and sex-
ual content. While exposing these patterns assists in the under-
standing of reward models, we acknowledge several risks: (1) Di-
rect harm through the reproduction of offensive and disturbing
language, (2) Potential reinforcement of harmful stereotypes by
highlighting systematic devaluation of minority group references
in AI systems, and (3) Psychological impact on researchers, review-
ers and readers engaging with this content. Following established
guidelines to mitigate these risks [21], we implemented clearly vis-
ible content warnings before sensitive sections and tables, mini-
mized direct quotes of harmful language where possible in the
main text and framed discussions to emphasize these as concerning
artifacts. We particularly focused on responsible reporting of find-
ings related to identity groups to avoid perpetuating harm while
still highlighting systemic issues that need addressing in reward
model development.
Acknowledgments
Thank you to Franziska Brändle, Owain Evans, Matan Mazor, and
Carroll Wainwright for helpful discussions.
References
[1] Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova
DasSarma, Dawn Drain, Stanislav Fort, Deep Ganguli, Tom Henighan, Nicholas
Joseph, Saurav Kadavath, Jackson Kernion, Tom Conerly, Sheer El-Showk, Nel-
son Elhage, Zac Hatfield-Dodds, Danny Hernandez, Tristan Hume, Scott John-
ston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine Olsson, Dario Amodei,
Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann, and Jared
Kaplan. 2022. Training a Helpful and Harmless Assistant with Reinforcement
Learning from Human Feedback. arXiv:2204.05862 [cs.CL] https://arxiv.org/
abs/2204.05862
[2] Meriem Boubdir, Edward Kim, Beyza Ermis, Sara Hooker, and Marzieh Fadaee.
2023. Elo Uncovered: Robustness and Best Practices in Language Model Evalua-
tion. arXiv:2311.17295 [cs.CL] https://arxiv.org/abs/2311.17295
[3] Ralph Allan Bradley and Milton E Terry. 1952. Rank analysis of incomplete
block designs: I. The method of paired comparisons. Biometrika 39, 3/4 (1952),
324–345.
[4] Stephen Casper, Xander Davies, Claudia Shi, Thomas Krendl Gilbert, Jérémy
Scheurer, Javier Rando, Rachel Freedman, Tomasz Korbak, David Lindner, Pedro
Freire, et al. 2023. Open problems and fundamental limitations of reinforcement
learning from human feedback. arXiv preprint arXiv:2307.15217 (2023).
[5] Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios Nikolas Angelopou-
los, Tianle Li, Dacheng Li, Hao Zhang, Banghua Zhu, Michael Jordan, Joseph E.
Gonzalez, and Ion Stoica. 2024. Chatbot Arena: An Open Platform for Evaluat-
ing LLMs by Human Preference. arXiv:2403.04132 [cs.AI] https://arxiv.org/abs/
2403.04132
[6] Paul F Christiano, Jan Leike, Tom Brown, Miljan Martic, Shane Legg, and Dario
Amodei. 2017. Deep Reinforcement Learning from Human Preferences. In Ad-
vances in Neural Information Processing Systems, I. Guyon, U. Von Luxburg,
S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett (Eds.), Vol. 30.
[7] Bruce Dawson. 2014.
There are Only Four Billion Floats–So Test Them
All!
https://randomascii.wordpress.com/2014/01/27/theres-only-four-billion-
floatsso-test-them-all/
[8] Lucas Dixon, John Li, Jeffrey Sorensen, Nithum Thain, and Lucy Vasserman. 2018.
Measuring and mitigating unintended bias in text classification. In Proceedings
of the 2018 AAAI/ACM Conference on AI, Ethics, and Society. 67–73.
[9] Nicolai Dorka. 2024. Quantile Regression for Distributional Reward Models in
RLHF. arXiv preprint arXiv:2409.10164 (2024).
[10] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad
Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan,
et al. 2024. The llama 3 herd of models. arXiv preprint arXiv:2407.21783 (2024).
[11] Yann Dubois, Chen Xuechen Li, Rohan Taori, Tianyi Zhang, Ishaan Gulrajani,
Jimmy Ba, Carlos Guestrin, Percy S Liang, and Tatsunori B Hashimoto. 2023.
AlpacaFarm: A simulation framework for methods that learn from human feed-
back. Advances in Neural Information Processing Systems 36 (2023), 30039–30069.
[12] Arpad E. Elo. 1967. The Proposed USCF Rating System, Its Development, Theory,
and Applications. Chess Life 22, 8 (August 1967), 242–247.
[13] Leo Gao, John Schulman, and Jacob Hilton. 2023.
Scaling laws for reward
model overoptimization. In International Conference on Machine Learning. PMLR,
10835–10866.
[14] Thomas Krendl Gilbert, Nathan Lambert, Sarah Dean, Tom Zick, Aaron Snoswell,
and Soham Mehta. 2023. Reward reports for reinforcement learning. In Proceed-
ings of the 2023 AAAI/ACM Conference on AI, Ethics, and Society. 84–130.
[15] Geoffrey E Hinton. 2002. Training products of experts by minimizing contrastive
divergence. Neural Computation 14, 8 (2002), 1771–1800.
[16] Tom Hosking, Phil Blunsom, and Max Bartolo. 2024. Human Feedback is not
Gold Standard. In The Twelfth International Conference on Learning Representa-
tions.
[17] Hamish Ivison, Yizhong Wang, Jiacheng Liu, Zeqiu Wu, Valentina Pyatkin,
Nathan Lambert, Noah A Smith, Yejin Choi, and Hanna Hajishirzi. 2024. Unpack-
ing DPO and PPO: Disentangling best practices for learning from preference
feedback. Advances in Neural Information Processing Systems 37 (2024), 36602–
36633.
[18] Natasha Jaques, Asma Ghandeharioun, Judy Hanwen Shen, Craig Ferguson,
Agata Lapedriza, Noah Jones, Shixiang Gu, and Rosalind Picard. 2019.
Way
off-policy batch deep reinforcement learning of implicit human preferences in
dialog. arXiv preprint arXiv:1907.00456 (2019).
[19] Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, De-
vendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel,
Guillaume Lample, Lucile Saulnier, et al. 2023.
Mistral 7B.
arXiv preprint
arXiv:2310.06825 (2023).
[20] Hannah Kirk, Andrew Bean, Bertie Vidgen, Paul Röttger, and Scott Hale. 2023.
The Past, Present and Better Future of Feedback Learning in Large Language
Models for Subjective Human Preferences and Values. In Proceedings of the 2023
Conference on Empirical Methods in Natural Language Processing. 2409–2430.
[21] Hannah Kirk, Abeba Birhane, Bertie Vidgen, and Leon Derczynski. 2022. Han-
dling and Presenting Harmful Text in NLP Research. In Findings of the As-
sociation for Computational Linguistics: EMNLP 2022, Yoav Goldberg, Zornitsa
Kozareva, and Yue Zhang (Eds.). Association for Computational Linguistics, Abu
Dhabi, United Arab Emirates, 497–510. doi:10.18653/v1/2022.findings-emnlp.35
[22] Hannah Rose Kirk, Bertie Vidgen, Paul Röttger, and Scott A Hale. 2023. The
empty signifier problem: Towards clearer paradigms for operationalising” align-
ment” in large language models. arXiv preprint arXiv:2310.02457 (2023).
[23] Hannah Rose Kirk, Alexander Whitefield, Paul Röttger, Andrew Michael Bean,
Katerina Margatina, Rafael Mosquera, Juan Manuel Ciro, Max Bartolo, Adina
Williams, He He, Bertie Vidgen, and Scott A. Hale. 2024.
The PRISM Align-
ment Dataset: What Participatory, Representative and Individualised Human


Page 12:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
Feedback Reveals About the Subjective and Multicultural Alignment of Large
Language Models. In The Thirty-eight Conference on Neural Information Process-
ing Systems Datasets and Benchmarks Track. https://openreview.net/forum?id=
DFr5hteojx
[24] John Koenig. 2021. The Dictionary of Obscure Sorrows. Simon and Schuster.
[25] Nathan Lambert, Thomas Krendl Gilbert, and Tom Zick. 2023. Entangled pref-
erences: The history and risks of reinforcement learning and human feedback.
arXiv preprint arXiv:2310.13595 (2023).
[26] Nathan Lambert, Valentina Pyatkin, Jacob Morrison, LJ Miranda, Bill Yuchen
Lin, Khyathi Chandu, Nouha Dziri, Sachin Kumar, Tom Zick, Yejin Choi, et al.
2024. RewardBench: Evaluating reward models for language modeling. arXiv
preprint arXiv:2403.13787 (2024).
[27] Geoffrey Leech, Paul Rayson, et al. 2014. Word frequencies in written and spoken
English: Based on the British National Corpus. Routledge.
[28] Xiao Li, Zhuhong Li, Qiongxiu Li, Bingze Lee, Jinghao Cui, and Xiaolin Hu. 2024.
Faster-GCG: Efficient Discrete Optimization Jailbreak Attacks against Aligned
Large Language Models.
arXiv preprint arXiv:2410.15362 (Oct. 2024).
doi:10.
48550/arXiv.2410.15362 arXiv:2410.15362 [cs].
[29] Xinyu Li, Ruiyang Zhou, Zachary C Lipton, and Liu Leqi. 2024.
Personal-
ized language modeling from personalized human feedback.
arXiv preprint
arXiv:2402.05133 (2024).
[30] Bing Liu. 2022. Sentiment analysis and opinion mining. Springer Nature.
[31] Chris Yuhao Liu, Liang Zeng, Jiacai Liu, Rui Yan, Jujie He, Chaojie Wang,
Shuicheng Yan, Yang Liu, and Yahui Zhou. 2024. Skywork-Reward: Bag of Tricks
for Reward Modeling in LLMs. arXiv preprint arXiv:2410.18451 (2024).
[32] Xingzhou Lou, Dong Yan, Wei Shen, Yuzi Yan, Jian Xie, and Junge Zhang. 2024.
Uncertainty-aware Reward Model: Teaching Reward Models to Know What is
Unknown. arXiv preprint arXiv:2410.00847 (2024).
[33] Luke Marks, Amir Abdullah, Clement Neo, Rauno Arike, David Krueger, Philip
Torr, and Fazl Barez. 2024. Interpreting Learned Feedback Patterns in Large
Language Models. Advances in Neural Information Processing Systems 37 (2024),
36541–36566.
[34] Vivek Myers, Evan Ellis, Sergey Levine, Benjamin Eysenbach, and Anca Dra-
gan. 2024. Learning to assist humans without inferring rewards. arXiv preprint
arXiv:2411.02623 (2024).
[35] Anh Nguyen, Jason Yosinski, and Jeff Clune. 2015. Deep neural networks are
easily fooled: High confidence predictions for unrecognizable images. In Proceed-
ings of the IEEE conference on computer vision and pattern recognition. 427–436.
[36] F. Å. Nielsen. 2011. AFINN.
http://www2.compute.dtu.dk/pubdb/pubs/6010-
full.html
[37] Chris Olah, Alexander Mordvintsev, and Ludwig Schubert. 2017. Feature visual-
ization. Distill 2, 11 (2017), e7.
[38] Ji Ho Park, Jamin Shin, and Pascale Fung. 2018. Reducing Gender Bias in Abusive
Language Detection. In Proceedings of the 2018 Conference on Empirical Methods
in Natural Language Processing, Ellen Riloff, David Chiang, Julia Hockenmaier,
and Jun’ichi Tsujii (Eds.). Association for Computational Linguistics, Brussels,
Belgium, 2799–2804. doi:10.18653/v1/D18-1302
[39] Sriyash Poddar, Yanming Wan, Hamish Ivison, Abhishek Gupta, and Natasha
Jaques. 2024. Personalizing reinforcement learning from human feedback with
variational preference learning. arXiv preprint arXiv:2408.10075 (2024).
[40] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano
Ermon, and Chelsea Finn. 2023. Direct preference optimization: Your language
model is secretly a reward model. Advances in Neural Information Processing
Systems 36 (2023), 53728–53741.
[41] Maarten Sap, Dallas Card, Saadia Gabriel, Yejin Choi, and Noah A Smith. 2019.
The risk of racial bias in hate speech detection. In Proceedings of the 57th annual
meeting of the association for computational linguistics. 1668–1678.
[42] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.
2017. Proximal policy optimization algorithms. arXiv preprint arXiv:1707.06347
(2017).
[43] Eldar Shafir, Itamar Simonson, and Amos Tversky. 1993. Reason-based choice.
Cognition 49, 1-2 (1993), 11–36.
[44] Wei Shen, Rui Zheng, Wenyu Zhan, Jun Zhao, Shihan Dou, Tao Gui, Qi Zhang,
and Xuanjing Huang. 2023.
Loose lips sink ships: Mitigating length bias in
reinforcement learning from human feedback. arXiv preprint arXiv:2310.05199
(2023).
[45] Prasann Singhal, Tanya Goyal, Jiacheng Xu, and Greg Durrett. 2023. A long way
to go: Investigating length correlations in RLHF. arXiv preprint arXiv:2310.03716
(2023).
[46] Anand Siththaranjan, Cassidy Laidlaw, and Dylan Hadfield-Menell. 2024. Distri-
butional Preference Learning: Understanding and Accounting for Hidden Con-
text in RLHF. In The Twelfth International Conference on Learning Representa-
tions.
[47] Taylor Sorensen, Jared Moore, Jillian Fisher, Mitchell Gordon, Niloofar
Mireshghallah, Christopher Michael Rytting, Andre Ye, Liwei Jiang, Ximing Lu,
Nouha Dziri, et al. 2024. A roadmap to pluralistic alignment. arXiv preprint
arXiv:2402.05070 (2024).
[48] Nisan Stiennon, Long Ouyang, Jeffrey Wu, Daniel Ziegler, Ryan Lowe, Chelsea
Voss, Alec Radford, Dario Amodei, and Paul F Christiano. 2020. Learning to
summarize with human feedback. Advances in Neural Information Processing
Systems 33 (2020), 3008–3021.
[49] Gemma Team, Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhu-
patiraju, Shreya Pathak, Laurent Sifre, Morgane Rivière, Mihir Sanjay Kale, Juli-
ette Love, et al. 2024. Gemma: Open models based on Gemini research and tech-
nology. arXiv preprint arXiv:2403.08295 (2024).
[50] Gemma Team, Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy
Hardin, Surya Bhupatiraju, Léonard Hussenot, Thomas Mesnard, Bobak Shahri-
ari, Alexandre Ramé, et al. 2024. Gemma 2: Improving open language models at
a practical size. arXiv preprint arXiv:2408.00118 (2024).
[51] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne
Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, et al. 2023. Llama: Open and efficient foundation language models. arXiv
preprint arXiv:2302.13971 (2023).
[52] Haoxiang Wang, Wei Xiong, Tengyang Xie, Han Zhao, and Tong Zhang. 2024.
Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-
Experts. In EMNLP.
[53] Rui Yang, Ruomeng Ding, Yong Lin, Huan Zhang, and Tong Zhang. 2024. Regu-
larizing Hidden States Enables Learning Generalizable Reward Model for LLMs.
In Advances in Neural Information Processing Systems.
[54] Robert B Zajonc. 1968. Attitudinal effects of mere exposure. Journal of person-
ality and social psychology 9, 2p2 (1968), 1.
[55] Matthew D Zeiler and Rob Fergus. 2014. Visualizing and understanding con-
volutional networks. In Computer Vision–ECCV 2014: 13th European Conference,
Zurich, Switzerland, September 6-12, 2014, Proceedings, Part I 13. Springer, 818–
833.
[56] Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J Zico Kolter, and Matt
Fredrikson. 2023. Universal and transferable adversarial attacks on aligned lan-
guage models. arXiv preprint arXiv:2307.15043 (2023).


Page 13:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
A
Appendix
A.1
Research Methods
A.1.1
Online resources. Code and output data for the analyses, tables and figures in the main text are available at https://github.com/
brchristian/reward_model_optimal_pessimal_tokens/.
A.1.2
Comparing Reward Models to LLM Logprobs. As a point of comparison, we might ask how reward model scores compare to the
logprobs output by LLMs themselves. How comparable are, say, the logprobs of base models and instruction-tuned models to the reward
scores?
Tables A.1-A.5 offer a qualitative window into this behavior for all currently available versions of the Gemma series of models from
Google, one of the two main families of base models used by the reward-model developers in our study.
To obtain these logprobs from the instruction-tuned models, we used the exact same conversation prompt that we used for the reward-
model analysis, namely:
tokenizer.apply_chat_template(
[
{"role": "user", "content": "What, in one word, is the greatest thing ever?"}
],
return_tensors='pt',
return_dict=True,
add_generation_prompt=True
)
For the base models without instruction tuning, we simply passed in a minimal zero-shot prompt as follows:
tokenizer(
"User: What, in one word, is the greatest thing ever?\nAssistant:",
return_tensors='pt'
)
A complete analysis of how these logprobs differ between models (and model families), and in particular how they compare to reward
scores, is a promising direction of future research. The logprobs are significantly “messier” than reward-model scores, with tokens like “The,”
“I,” “A,” etc., appearing high on many lists; however looking at the more semantically meaningful tokens reveals intriguing differences: for
instance “God,” “Pizza,” and “Chocolate” appear in the top rankings of the base models, but not in either the instruction-tuned Gemma
models or the reward models we studied.
Adding the “best” and “worst” logprobs together (Table A.4) does not reveal cleverly flexible answers (like “Depends”) at the top end
of the spectrum, nor does it reveal taboo or toxic answers at the bottom of the spectrum, as we saw with the reward models. However,
subtracting “worst” from “best” logprobs (Table A.5) does begin—at least in the newer and higher-parameter models—to approximate a
version of the “Love”–“Despair” axis that we see in the reward models.


Page 14:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
A.2
Tables
CONTENT WARNING: The following tables include examples of biased, offensive, disturbing, sexually-explicit and otherwise harmful text.
gemma-2b
gemma-2b-it
gemma-7b
gemma-7b-it
gemma-2-2b
gemma-2-2b-it
gemma-2-9b
gemma-2-9b-it
gemma-2-27b
gemma-2-27b-it
The
The
The
Love
The
Love
The
Love
Love
Love
I
**
It
Truth
A
**
I
Life
The
**
That
Love
I
Happiness
I
Life
What
**
I
As
Well
There
Well
The
Well
Hope
Well
Happiness
Happiness
Happiness
What
It
A
Nothing
What
Connection
That
Meaning
That
Oh
Happiness
What
Infinity
Oh
Joy
It
Existence
"
Sub
It
That
That
Answer
It
Wonder
You
That
love
Emp
You
While
Hmm
Wisdom
That
**
In
Impossible
Pizza
Perspective
Answer
"
Answers
"
Happiness
A
love
God
Hope
A
Truth
You
Joy
(
Love
Oh
Connection
[
Love
"
Goodness
Ah
Beauty
Uh
愛
"
Sub
“
love
God
Peace
All
Goodness
Um
Okay
LOVE
You
*
(
Beauty
If
Awesome
You
love
There
Love
\n
Impossible
Love
Honestly
OK
Hope
[
LOVE
One
Choice
In
Experience
Everything
Life
Sex
LOVE
Why
Change
How
As
That
Joy
[
Nothing
No
Good
*
Everything
Hmm
Hope
Chocolate
Existence
Why
Sure
God
Wonder
Hmm
Meaning
Wow
Everything
It
Conscious
No
I
Science
Everything
Great
Growth
Why
Joy
\n\n
Compassion
In
"
Music
Infinite
Nothing
This
Let
Perspective
What
LOVE
How
For
Heaven
Everything
Beauty
[
Un
There
Curi
...
...
...
...
...
...
...
...
...
...
mikrofon
NKC
ekst
(""));
quæ
againſt
fieltro
𑄠
trouvent
enterOuterAlt
defekt
siyang
eksklu
\%$\\
originais
misconduct
ValueStyle
 dobré
contentLoaded
kommunik
sarili
obiet
()=>
fidèles
aggressive
éstos
<unused53>
élevée
layout
kask
duled
teolog
'-':
brancas
houſe
izquier
𑄝
ďal
PreInfinity
kompresﺭ ģﺱ ęڡkomik
//\n
prêtres
fhew
ſta
𑄣
ľudí
manager
vertik
hien
silikon
["",
industriels
Tacitus
licencias
parsedMessage
voient
ulink
rente
Bekasi
dekol
[{\n
varandra
Attacks
CreateTagHelper
surla
spoluprá
managers
balkon
irited
dekoratif
}(),
mères
raiſ
queryInterface
ſicht
faisaient
GOTREF
minimalis
Tangerang
ujedno
[''
pouvoit
attacks
camiset
メンテナ
travaillent
procedure
stoff
ILLUSTRATIONS
konfigura
//----
précédents
ſhe
Wikiseite
exitRule
sensaciones
price
konflikt
pagkak
biografi
}}}\n
démocr
dietary
fotográfico
AssemblyCulture
väč
strategy
silikon
atterns
kompres
>|</
nemici
himſelf
increí
<unused99>
rých
management
keramik
bawat
indeks
">:
chré
Cæsar
HtmlAttribute
enablog
dôle
performance
akut
requently
bunda
">+
feroit
ſeveral
desmotivaciones
𑄮
náš
symptoms
keram
SUDOC
maksi
//*/
auroit
AndEndTag
herido
𑄥
tiennent
AnchorStyles
kompakt
nguyen
aparat
">...
étoitłٮﺩﻯﺍ ﻭﻯﮎﻯMereka
 présentent
facilities
kosme
COMPOUNDS
galeri
[]\n
étoient
Efq
pérd
Билгалдахарш
každého
RotationOrder
karton
ternura
torba
("")\n
enfans
myſelf
indígen
CreateTagHelper
niektor
damage
kompati
thuy
abstrak
'&#
chrétiens
aggressor
EconPapers
ItemBackground
sorpresas
PostInfinity
alkoh
BnF
<bos>
">/
avoient
Monfieur
Infór
EconPapers
mettent
RectangleBorder
Table A.1: Ranked next-token logprobs from Gemma models for the “greatest thing” prompt.


Page 15:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
gemma-2b
gemma-2b-it
gemma-7b
gemma-7b-it
gemma-2-2b
gemma-2-2b-it
gemma-2-9b
gemma-2-9b-it
gemma-2-27b
gemma-2-27b-it
The
The
The
Happiness
The
Love
I
Love
Love
Love
I
**
A
Joy
I
**
The
Happiness
The
Happiness
That
Happiness
I
Love
A
Happiness
What
**
Happiness
**
What
It
What
The
What
Joy
That
That
Chocolate
Joy
Well
There
Good
Heaven
Well
Life
Well
Meaning
I
As
Oh
Sure
An
JOY
Oh
Family
It
Life
Pizza
Sub
It
That
Oh
Ple
That
Hope
You
Joy
That
You
While
Love
Awesome
It
Connection
In
Connection
"
Experience
A
Love
Wow
Happiness
"
LOVE
Oh
love
You
Emp
Honestly
Nothing
Bliss
Why
Home
A
Impossible
\n
Laughter
"
Answer
(
JOY
You
Bliss
"
Choice
\n\n
Perspective
(
"
Well
Joy
Um
Love
There
Sub
love
Hope
This
I
That
happiness
Uh
Magic
One
Everything
In
Love
Good
Life
My
Paradise
*
Laughter
Best
LOVE
[
Depends
Everything
Joy
Best
Delight
(
愛
How
Love
It
*
My
Peace
You
Happy
Nothing
Let
Laughter
That
Impossible
Um
For
"
Laughter
Hmm
Everything
Hmm
Existence
A
Exper
God
Of
It
Wow
No
Loved
Okay
As
What
Existence
Your
Beauty
joy
How
Peace
[
Harmony
“
Hmm
Why
A
Cheese
Wonder
Yes
love
Yes
Freedom
Cake
LOVE
...
...
...
...
...
...
...
...
...
...
kask
totic
inteligen
\%$\\
soldati
Attacks
izquier
XmlEnum
zimní
businessman
pólﺭ ģﺱ ęڡdekoratif
<_>
prêtres
ecclesiastical
navíc
 spoluprá
buildings
defekt
pagkak
obiet
[''],
industriels
himſelf
queryInterface
<unused53>
sensaciones
performances
kommunik
kram
konfigura
[{\n
quæ
resourceCulture
fieltro
𝅥
ďal
procedure
kompres
Tangerang
komik
}(),
précédents
misconduct
linkovi
 avvic
price
minimalis
irited
ujedno
>|</
vícti
Egli
herido
メンテナ
faisaient
TintMode
balkon
NKC
eksklu
(""));
vermelhas
fhew
fotográfico
𑄮
élevée
diseases
vertik
tuong
teolog
()\n
mèresﻝﻝﺍﺱﻡﺍﺀValueStyle
𑄥
voient
vitis
rente
ILLUSTRATIONS
spesifik
'&#
démocr
severity
camiset
enablog
náš
symptoms
stoff
ofold
intelek
(">>
brancas
ſhe
CreateTagHelper
twimg
ľudí
GOTREF
silikon
duled
aparat
//\n
originais
msgTypes
Mereka
RenderAtEndOf
rých
PreInfinity
keramik
ternura
indeks
}}}\n
feroit
Managerial
Wikiseite
SourceChecksum
tiennent
facilities
keram
EoL
biografi
">+
chré
ſeveral
EconPapers
bootstrapcdn
dôle
performance
karton
requently
bunda
">:
nemici
Retailers
expandindo
surla
travaillent
management
konflikt
atterns
kompres
">/
auroit
myſelf
desmotivaciones
exitRule
sorpresas
AnchorStyles
kosme
nguyen
maksi
//----
étoit
Cæsar
increí
ItemBackground
každého
managers
kompakt
COMPOUNDS
galeri
("")\n
étoient
Efq
HtmlAttribute
parsedMessage
présentent
damage
akut
SUDOC
abstrak
">...
enfans
aggressor
indígen
Билгалдахарш
väč
PostInfinity
kompati
thuy
torba
//*/
chrétiens
Monfieur
pérd
CreateTagHelper
niektor
RotationOrder
alkoh
BnF
<bos>
[]\n
avoientłٮﺩﻯﺍ ﻭﻯﮎﻯInfór
EconPapers
mettent
RectangleBorder
Table A.2: Ranked next-token logprobs from Gemma models for the “best thing” prompt.


Page 16:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
gemma-2b
gemma-2b-it
gemma-7b
gemma-7b-it
gemma-2-2b
gemma-2-2b-it
gemma-2-9b
gemma-2-9b-it
gemma-2-27b
gemma-2-27b-it
The
The
That
Nothing
The
Pain
I
Su
The
Su
I
Pain
The
The
A
Hate
The
Pain
Death
Sub
Well
Sure
A
Pain
Well
**
What
Loss
War
As
Oh
There
I
Death
I
Regret
Well
**
I
suffering
That
Answer
Let
Hell
Oh
Loss
It
suffering
In
Suffering
What
**
Oh
Darkness
What
Des
That
Suffering
Hitler
Pain
It
Unfortunately
Is
Absolutely
"
Exist
You
Death
Genocide
**
You
Bad
You
Nonsense
It
Evil
Oh
sufrimiento
"
Suff
A
No
Murder
Answer
That
H
In
Suff
That
That
"
I
Whatever
Ugh
(
Trag
There
Hate
suffering
Death
User
No
*
Fear
Why
suffering
A
War
No
Certainly
An
Trag
Um
Grief
How
Regret
It
Hate
(
It
Worst
Evil
You
Su
A
That
\n
It
Death
Silence
Anything
Nothing
Uh
War
Let
Grief
There
Subject
Um
Honestly
Death
In
Why
Cata
"
souffrance
Pain
sub
Pain
Worst
Hmm
Nada
Nothing
Hat
Okay
As
“
##
How
Hell
One
A
[
Tyran
Sorry
Nothing
What
Death
[
Nothing
Bad
Hate
One
Trag
Murder
Entropy
In
A
We
F
No
Cruel
Hmm
SU
You
Suffix
There
Sorry
This
There
...
Chaos
Worst
Suffix
Cancer
*
...
...
...
...
...
...
...
...
...
...
optik
ofold
granat
`;
vícti
leaſt
berdayakan
<unused52>
moviliz
romance
balkon
ophylla
gitara
(;;
originais
PERTIES
izquier
<unused51>
časti
management
kompres
érêt
kompres
('*',
fidèles
successes
expandindo
<unused74>
negociaciones
parseDouble
minimalis
PLWABN
konfigura
/(\
précédents
ſhould
HtmlAttribute
<unused32>
náš
security
kommunik
Tangerang
maksi
">*
prêtres
壁纸łٮﺩﻯ ﻭﻯﮎﻯ
<unused47>
sorpresas
&\n
konflikt
OPPORT
ujedno
()\n
nemici
pleaſure
linkovi
<unused42>
zlep
Shake
vertik
Bekasi
balon
=\n
pouvoit
houſe
desmotivaciones
<unused41>
présentent
benefits
kask
OBSERVATIONS
dekol
">:
mères
Monfieur
DockStyle
<unused40>
rých
InstrumentedTest
pól
thuy
intelek
++\n
varandra
fhewť:ﻭﻡﻭ ęﮞ ęﺭ
<unused39>
pokoj
certification
rente
kram
dekoratif
}}}\n
brancas
ſay
RenderAtEndOf
<unused79>
väč
hacking
stoff
tull
bunda
"+\n
quæ
ſeveral
StructEnd
<unused80>
spoluprá
PostInfinity
karton
requently
indeks
">.
démocr
Efq
Mereka
<unused82>
faisaient
relaxation
akut
COMPOUNDS
teolog
//*/
chré
myſelf
Wikiseite
<pad>
niektor
profitability
silikon
liev
biografi
(''),
feroit
AndEndTag
pérd
 
tiennent
LLocation
keram
BnF
aparat
("")\n
étoit
Garibaldi
camiset
𖡻
dobré
exitRule
keramik
ILLUSTRATIONS
obiet
+\n
auroit
ſhe
fotográfico
<unused7>
trouvent
symptoms
kosme
BIBSYS
galeri
[]\n
enfans
ſtand
Infór
<unused22>
zimní
TintMode
kompakt
VOOR
abstrak
">/
étoient
raiſ
increí
𑄮
dôle
skills
kompati
NKC
torba
">...
chrétiens
SEGUIR
EconPapers
<unused71>
mettent
sizeCache
alkoh
<bos>
<bos>
">+
avoient
LookAnd
indígen
<unused98>
krás
RectangleBorder
Table A.3: Ranked next-token logprobs from Gemma models for the “worst thing” prompt.


Page 17:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
gemma-2b
gemma-2b-it
gemma-7b
gemma-7b-it
gemma-2-2b
gemma-2-2b-it
gemma-2-9b
gemma-2-9b-it
gemma-2-27b
gemma-2-27b-it
The
The
The
The
The
**
I
**
The
Sub
I
**
I
Nothing
A
Love
The
Love
I
Love
That
Sure
A
Happiness
I
**
What
That
Love
As
Well
There
That
Joy
Well
*
Well
Meaning
In
**
Oh
It
"
Answer
What
Un
That
As
"
Su
What
Answer
Nothing
Absolutely
Oh
H
It
Sub
That
It
I
An
Love
It
This
You
Existence
\n
Happiness
You
Honestly
What
Pain
That
Everything
Oh
Su
That
*
A
That
You
Death
"
Life
In
Everything
You
Emp
"
It
Heaven
You
Heart
A
Impossible
It
\n\n
"
Certainly
Oh
A
Why
Chaos
There
Regret
A
Difficult
(
Unfortunately
My
In
*
Hope
"
Choice
“
(
No
Of
Well
No
Um
It
How
It
What
##
Um
A
There
(
...
One
Happiness
There
Perspective
This
No
(
Hope
Uh
Nothing
Let
Un
\n\n
It
Everything
In
To
Yes
Nothing
Joy
Why
*
Death
Depends
In
Nothing
We
It
[
P
Okay
**
[
Existence
Why
While
If
Nonsense
Hmm
C
Hmm
Imagine
This
This
[
Pain
Is
Ple
No
Exist
[
Anything
Nothing
Hmm
How
Depending
There
I
That
Sure
This
the
Perhaps
...
...
...
...
...
...
...
...
...
...
defekt
tagHelperRunner
komik
++\n
pouvoit
themſelves
DockStyle
<unused80>
pokoj
InstrumentedTest
kask
oustic
balon
('');\n
prêtres
anſ
StructEnd
<unused52>
sensaciones
strength
balkon
OBSERVATIONS
eksklu
`;
vermelhas
帅气
fieltro
<unused51>
élevée
contentLoaded
kompres
Bekasi
spesifik
//\n
vícti
Garibaldiť:ﻭﻡﻭ ęﮞ ęﺭ
<unused32>
ľudí
performance
minimalis
SUDOC
dekoratif
>|</
varandra
ſay
izquier
<unused42>
náš
AnchorStyles
kommunik
nguyen
intelek
">*
précédents
faſt
RenderAtEndOf
<pad>
dobré
certification
vertik
tuong
ujedno
">.
quæ
houſe
ValueStyle
<unused39>
spoluprá
RotationOrder
pól
Tangerang
konfigura
'&#
originais
Cæsar
linkovi
 
trouvent
managers
stoff
kram
maksi
//----
mères
SEGUIR
expandindo
𑄝
zimní
facilities
konflikt
liev
teolog
()\n
brancas
himſelf
desmotivaciones
<unused98>
každého
buildings
rente
VOOR
kompres
(''),
nemici
LookAnd
HtmlAttribute
<unused22>
faisaient
procedure
silikon
atterns
obiet
+\n
démocr
ſtand
Mereka
<unused71>
rých
sizeCache
karton
ofold
indeks
}}}\n
chré
AndEndTag
camiset
 sorpresas
exitRule
keram
BIBSYS
bunda
">:
feroit
fhew
Wikiseite
enablog
krás
damage
keramik
ILLUSTRATIONS
biografi
//*/
auroit
raiſ
fotográfico
<unused7>
tiennent
skills
akut
requently
aparat
("")\n
étoit
ſeveral
pérd
<unused53>
présentent
management
kompakt
NKC
galeri
[]\n
étoient
ſhe
EconPapers
メンテナ
väč
TintMode
kosme
thuy
abstrak
">+
enfans
myſelf
increí
𑄥
dôle
symptoms
kompati
COMPOUNDS
torba
">/
chrétiens
Efq
Infór
𑄮
niektor
PostInfinity
alkoh
BnF
<bos>
">...
avoient
Monfieur
indígen
parsedMessage
mettent
RectangleBorder
Table A.4: Ranked tokens according to the sum of “best” and “worst” logprobs.


Page 18:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
gemma-2b
gemma-2b-it
gemma-7b
gemma-7b-it
gemma-2-2b
gemma-2-2b-it
gemma-2-9b
gemma-2-9b-it
gemma-2-27b
gemma-2-27b-it
<bos>
<bos>
alpina
Allegretto
nocchi
laughter
awesome
love
Happiness
Happiness
biografias
love
sembla
moza
ujednoznacz
Sunshine
happiness
happiness
happiness
happiness
anello
happiness
faisaient
Andante
détach
happiness
Awesome
smiles
Sunshine
Love
Personendaten
beauty
}{*}{
utop
heureuse
cudd
overjoyed
Love
sitive
happiness
gmbh
LOVE
frankfurt
happiness
wijn
Laughter
Amazing
connection
Smiles
joy
bienvenue
sunshine
besta
әрмәләр
cioccolato
magic
amazing
chocolate
Satisfaction
Love
ężczy
joy
ļ
joy
hoeft
risa
awesome
onomía
wireless
Joy
bezeichneter
cherished
siena
Happiness
tevreden
hugs
happiness
laughter
charming
Joy
सन्दर्भ
love
=+
poë
XmlAccessType
sunshine
Best
LOVE
Blessings
joy
gawas
enjoyment
materiaal
Joy
synthèse
Happiness
joyful
smile
Savings
Happiness
thereum
LOVE
iesp
labd
ulemon
joyful
amazing
Joy
Friendship
Friendship
coj
enjoying
lais
coö
vedic
bliss
ecstatic
Smiles
satisfaction
JOY
gasus
beautiful
AppBundle
stratég
décro
Connexion
greatness
Chocolate
esomeness
laughter
miele
appreciation
László
JOY
+:+
overjoyed
watermelon
JOY
chocolate
love
ureka
Happiness
quibus
witte
célè
cuddly
celebration
love
savings
Empathy
artig
loved
liel
benevol
graag
joy
parad
Happiness
Delicious
smiles
diamant
rebbero
CELLANEOUS
JOY
still
milagro
elated
Connection
helping
Gratitude
addKeyListener
elated
élastique
nive
}{*}{}
Magic
joyous
Smiles
Bliss
mirth
Ğٮ Ğٯﺍﻭﻯhappy
いただけます
Happiness
jagung
Magical
AWESOME
nakalista
Excellence
Wellbeing
trouva
happiest
nepiecieš
necessarie
Celebrating
miracles
Celebration
felicità
héroes
love
...
...
...
...
...
...
...
...
...
...
Violence
Maladies
CreateModel
setDisabled
horrid
Destruction
horrific
Painﺍﻭﻝ ĞﻩWar
starvation
infernal
StringWriter
CardHeader
deport
HATE
peggio
Loss
DialogInterface
pain
degradation
evils
PageFactory
/////////
dreadful
Tragedy
bad
Su
guerra
suffered
Rape
LIRE
scriptsize
()?;
torture
DBNull
peor
Suffix
cancers
suf
Abuse
kuro
onAttach
VIAF
Horrible
Condem
unpleasant
loss
deaths
Suffix
infarction
disaster
+#+
GoogleFonts
genocide
Pain
worst
GriefמלחPain
Rape
vább
렷
ValueStyle
BAD
Genocide
dreadful
pain
atrocities
War
diarr
Nasty
InnerText
"..\..\..\
bad
anguish
schlimm
SU
ocide
Evil
necrosis
abomination
HostException
ISNI
Bad
cruelty
horrendous
sufri
genocide
souffrance
Genocide
passim
RadioGroup
userDao
nightmare
horror
Bad
pain
cruelty
Suff
lepro
iniqu
setDisabled
//----
worse
evil
horrible
sufrimiento
crimes
Pain
})*/
relegation
cassert
ApiProperty
worse
=-\
Horrible
Pain
giarism
SU
Degradation
Sodom
ostringstream
elashes
peores
Evil
Awful
Loss
anguish
war
miscarriage
syndical
infestations
BeginContext
bad
Hate
Terrible
sorrow
aarrggbb
suffer
faudrait
plak
商品説明
//////////////
BAD
horror
worse
Sorrow
WEBPACK
Su
ritard
abomin
FormControl
appContext
peor
Despair
horrid
Suicide
initComponents
soffer
malignancy
teneb
supset
NUKAT
Worse
hate
worse
suffering
DebuggerNonUser
suffering
ensacola
Nightmare
WindowEvent
Datuak
Worst
Cruelty
worst
souffrance
arcoma
Su
esticides
blackish
genocide
HttpDelete
worst
hatred
Worst
suffering
inWeight
suffering
esticide
stratigraph
Sqft
///////////
worst
Atro
Worse
Suffering
ushman
Suffering
Table A.5: Ranked tokens according to the difference of “best” and “worst” logprobs.


Page 19:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
R-Gem-2B
LOVE
LOVE
LOVE
LIFE
LOVE
Love
LOVE
freedom
LOVE
LOVE
LOVE
LOVE
Love
LOVE
Love
Love
<|end_of_text|>
Freedom
Love
LOVE
Love
Love
Love
disputed
Love
LOVE
subjective
Freedom
Love
felicity
Love
Love
LOVE
opinion
LIFE
LIFE
LIFE
LOVE
Happiness
love
love
love
love
imagination
love
Happiness
EXISTS
LIFE
LIFE
love
love
love
love
Opinion
love
Life
.Nullable
.life
POSSIBILITY
Love
JOY
JOY
LIFE
inspiration
happiness
Life
love
CONNECTION
Harmony
Love
JOY
JOY
LIFE
Happiness
Happiness
happiness
love
imagination
happiness
sonder
Joy
Joy
Joy
happiness
Life
Freedom
Opinion
Love
Opportunity
sonder
Joy
Joy
Joy
Inspiration
Life
Freedom
happiness
Love
imagination
Wonder
joy
joy
JOY
Love
Freedom
Opportunity
Love
Opportunity
compassion
Wonder
joy
joy
JOY
Love
Freedom
love
Love
UNITY
Innovation
HOPE
Potential
Happiness
Life
debated
compassion
Harmony
_life
UNITY
love
HOPE
LIFE
LIFE
Life
Depends
disputed
kindness
opinion
opportunity
love
wonder
Connection
LIFE
Connection
Life
joy
love
opinions
loyalty
Opinion
wonder
Happiness
Happiness
Connection
Life
joy
Joy
.fromLTRB
love
harmony
WONDER
LIFE
Bliss
Bliss
opinions
Impossible
Joy
UNKNOWN
love
Universe
bliss
Connection
Bliss
Peace
PURPOSE
Impossible
Peace
UNKNOWN
Discovery
laughter
bliss
Compassion
happiness
Bliss
Unsure
inspiration
Peace
Happiness
Discovery
laughter
JOY
CONNECTION
PEACE
joy
kindness
life
joy
InterruptedException
Experience
Knowledge
JOY
...
...
...
...
...
...
...
...
...
...
assaulted
trafficking
nazis
(xyęﮞ ęڡ Ğٮxnxx
prostitution
raping
Democrats
killers
invaded
kidnap
esclavos
}}"><
racist
<section
manslaughter
_headers
Democrats
prostitutes
dikes
lolita
Nazis
Ukra
xnxx
raping
Theft
.insertBefore
terrorism
massacres
glanced
suic
"../../../
SyriaĞٮ ŌﺡﺍﺭﻯSlut
terrorist
.setText
terrorism
FUCKING
assaults
homophobic
segregation
racism
retard
homophobic
shootings
(cfg
terrorists
rapist
airlines
kidnapping
genoc
homophobic
}}">{{
Fuck
murderer
(st
Republicans
ransomware
pemeriksaan
raped
incendie
Talibanﺱ łٮ Ğٮﺍﻡ ĻٮﺭFuck
suicides
.startsWith
Republicans
retards
plantations
prostitu
homicidio
Crimeaﺍﻝﻉﺭﺍ Ğٯfascism
Nazis
(con
-Nazi
nazis
igarettes
harass
harassing
("../../
정치
covid
assaulting
/*****************…
Lesb
murdering
detainees
rape
dictadura
?>"><
войны
suic
Prostitutas
##################…
massac
Hitler
semesters
rape
violación
Venezuela
"]){\n
fucking
Murder
#################…
.DataGridViewConte…
Rape
droughts
segregation
suic
prostitutﮎ ģﺱﻭﺭﻩﺍﻯbdsm
terrorists
("[%
rape
Rape
asesinato
genoc
pembunuhan
cigarettes
prostit
fascist
murderers
_checks
rape
faggot
membunuh
assaulting
membunuh
cigaret
pedo
fuck
incest
(struct
|----------------…
murderous
Coon
raping
tortura
prostituŌﺡ ęﮞ įﮎfuck
injuring
homosexual
|-----------------…
murderers
Plantation
molest
harass
militarłٮﻭﺱ ĞٮFucking
genocide
/*****************…
homophobic
rape
ﺍﻝﺍﺡ Ğٮﻝﺍﻝrapist
'../../../../
opioids
?>"><
FUCK
pedo
.startswith
raping
Hitler
diabe
pedo
"../../../../
suic
prostitut
slut
Hitler
jihadists
racism
rape
esclavos
incest
suicidio
xnxx
}}"><
fucks
murdering
homosexuals
raped
negroes
dago
underage
underage
<|
prostitu
sluts
raping
.assertFalse
Rape
raping
Table A.6: Ranked tokens according to reward model scores for the “greatest thing” prompt.


Page 20:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
R-Gem-2B
LOVE
LOVE
Love
LIFE
LOVE
Love
LOVE
freedom
LOVE
LOVE
Love
Love
Love
LOVE
Love
Love
subjective
Freedom
Love
love
Love
Love
LOVE
disputed
Love
LOVE
LIFE
Freedom
Love
love
love
love
love
opinion
LIFE
LIFE
EXISTS
LOVE
Happiness
Love
love
love
love
imagination
love
Happiness
love
LIFE
LIFE
Love
Joy
Joy
LIFE
Opinion
love
Life
love
CONNECTION
Harmony
Wonder
Joy
Joy
Joy
inspiration
happiness
Life
Opinion
imagination
happiness
Wonder
joy
Happiness
Joy
Happiness
Happiness
happiness
happiness
Love
Opportunity
wonder
joy
joy
Life
happiness
Life
Freedom
Love
Love
imagination
bliss
Potential
joy
Life
Inspiration
Life
Freedom
Love
Opportunity
compassion
miraculous
LIFE
LIFE
Connection
Love
Freedom
Opportunity
opinion
UNITY
Innovation
miracle
Connection
Bliss
Connection
Love
Freedom
love
opinions
UNITY
love
LIFE
Connection
happiness
Bliss
debated
compassion
Harmony
UNKNOWN
opportunity
love
joy
Potential
Peace
Peace
Depends
disputed
kindness
UNKNOWN
loyalty
Opinion
joy
CONNECTION
Peace
joy
Life
joy
love
Happiness
love
harmony
Bliss
imagination
peace
joy
Life
joy
Joy
disputed
love
Universe
hope
wonder
bliss
life
opinions
Impossible
Joy
life
Discovery
laughter
hope
Life
peace
Happiness
PURPOSE
Impossible
Peace
life
Discovery
laughter
Joy
Life
Loved
Peace
kindness
inspiration
Peace
exist
Experience
Knowledge
happiness
Happiness
Connection
CONNECTION
love
life
compassion
exist
Experience
Knowledge
Joy
...
...
...
...
...
...
...
...
...
...
threaten
stalking
scams
Libya
icides
epilepsy
Adolf
slaves
assaulted
terrorist
invade
racist
wildfires
bigotryęڡ Ļٮﺭﺍ Ľﻯﺭsuicidal
rape
`<
prostitu
prostitute
worries
Rape
Hamas
SaddamĞٮ Ōﺡﻩﻯ ęﺭﺍ Ğٮprostitu
Theft
////////////
prostitutes
Nazis
Offices
murdering
pesticides
cocaineﺍﻝﻭﻝﺍ Ľﻯﺍ Ğٮfucked
manslaughter
racially
，“
assaulting
harass
trafficking
trafficking
fascism
restau
suicides
terrorist
coronavirus
terrorist
gunmen
riots
suic
kidnapping
Nazisłٮﻭ ģﺱhomophobic
murderer
lesbians
Democrats
prostitution
invading
kidnapping
stereotypes
tuberculosisģﺱﻩﺭﻩﺍﻯraping
shootings
>');
Democrats
slaughtered
deport
homophobic
injuring
homophobic
incest
Fuck
assaulting
Coronavirus
terrorism
neoliberal
inflict
harass
homophobic
UkraĻٮﻯﻡﺍﺭﻯFuck
Nazis
">&
terrorism
kidnapping
assaulting
raped
assaulting
Syriaęﮞ ęڡ Ğٮfascism
suicides
`(
terrorists
blacks
threatens
prostitu
murdering
racism
racist
suic
Murder
murderers
Republicans
prostitutes
discourage
segregation
segregation
TalibanĞٮ Ōﺡﺍﺭﻯcovid
terrorists
Rape
Republicans
killers
phishing
rape
Nazis
Crimea
retard
fucking
murderers
それは
massac
murdering
plantation
rape
"../../../
Venezuelaﺍﻝﻉﺭﺍ Ğٯfuck
incest
shootings
rape
murderers
invaded
raping
harassing
("../../
войны
Fucking
injuring
fucking
rape
Rape
assaulted
assaulting
suic
cigarettesﮎ ģﺱﻭﺭﻩﺍﻯfuck
genocide
raping
homophobic
murderous
glanced
molest
harass
prostitu
pedo
fascist
pedo
`${
raping
Hitler
assaults
pedo
'../../../../
militarŌﺡ ęﮞ įﮎFUCK
Hitler
`${
racism
rape
airlines
incest
"../../../../
suicłٮﻭﺱ Ğٮslut
murdering
&=
raped
raping
detainees
underage
underage
opioids
prostitu
fucks
raping
homosexual
Rape
rape
Table A.7: Ranked tokens according to reward model scores for the “greatest thing” prompt, restricted to tokens shared between the Llama and Gemma
tokenizers.


Page 21:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
R-Gem-2B
subjective
subjective
Impossible
disputed
Impossible
Depends
EXISTS
debated
Opinion
opinion
Undefined
LOVE
Impossible
Depends
Impossible
disputed
subjective
Change
opinions
existing
Undefined
Undefined
LOVE
depends
Depends
depends
opinions
Change
subjective
existing
LOVE
Undefined
Love
depends
subjective
depends
recursion
Opinion
opinion
Opinion
Love
Love
Love
debated
disputed
Impossible
Belgium
Promise
imagination
perspective
love
Opinion
subjective
opinion
depends
Impossible
opinion
Promise
rhetorical
Alive
Love
Perspective
love
Opinion
depends
elusive
shouldBe
Freedom
CONTEXT
LIFE
Awareness
Impossible
love
Impossible
varies
subjective
none
Freedom
CONTEXT
Alive
Perspective
Impossible
Undefined
Impossible
Opinion
contested
none
LOVE
Understanding
Perspective
love
Love
Undefined
unsure
opinion
unsure
Opinion
surprise
Understanding
existence
Impossible
Meaning
Meaning
subjective
opinions
Life
disputed
Hope
optimism
possibility
Impossible
love
Opinion
opinions
contested
Life
UNKNOWN
Hope
Depends
existence
Meaning
Perception
impossible
contested
Unknown
Opinion
UNKNOWN
innocence
recursion
acceptance
Potential
love
LIFE
varies
Unknown
uncertain
Denise
surprises
Thinking
existent
삭제
varies
Loving
imagination
Variable
varies
Exists
Surprise
Thinking
Bliss
>\<^
Define
varies
Discuss
Variable
debated
Exists
realization
expectations
experience
consciousness
Define
imagination
Discuss
debated
differs
yours
CONNECTION
Perspective
experience
Potential
imagination
Unknown
TBD
CONTEXT
Living
exists
Discovery
disputed
life
possibility
depends
Unknown
differs
CONTEXT
Living
exists
Discovery
vibes
life
Unknown
depends
Awareness
everything
UNKNOWN
Perception
LIFE
promise
positivity
subjective
...
...
...
...
...
...
...
...
...
...
nicknamed
Islamistť: Ğﻩ
ﺍﻝ ģﺱﺭ
/.."(
ęﮞ ĞٯﺩsetTime
放在
Jews
(“
pussy
blacks
minority
région
($("#ęڡ Ļٮﺭﺍ Ľﻯﺭhomosexual
Whether
``ﻭ ٕاprostitute
photographed
homophobic
ürünleri
($("#
prostitu
compét
pedo
Mexicans
Fuck
tranny
Counties
molest
sklearn
<<<<<<<ĞٮﻉﺩﺍﺩsetDate
Whether
////////////
Fuck
Germans
Syrian
segreg
getItemCount
<!--ٓاﻡﺭﻯﮎ
(“是个
]=>
cunt
raping
autistic
erectile
corridors
<!--łٮﻭ ģﺱ
($("#
preceded
Muslims
fuck
Arabs
peninsula
suic
synagogue
militaręڡﻯ
($("#
whereas
">&
fuck
homosexual
Arabs
izophren
'../../
$(".ٓاﻡﺭﻯﮎﺍretard
按照
`${
nig
Whites
draped
racially
counties
$(".
위치
Fuck
作为
Republicans
,“
whore
Ethnic
tranny
"../../
$('#ﺍﻝﻉﺭﺍ Ğٯcunt
坐在
`${
retard
prostitutes
deposits
blacks
HttpStatusCode
$('#
negro
Fuck
是在
Republicans
raped
gays
Tibetan
nig
développ
Democratsęﮞ Ğٯ ģﺱ$(".
Where
Lesbian
slut
whites
racially
Caucasian
subsidiaries
Democratsﺩﺍﺭﺍﻯ$(".
Where
>');
FUCK
Blacks
Peninsula
coon
RoutedEventArgs
"../../../ﺍﻝﻭﻝﺍ Ľﻯﺍ Ğٮfucking
站在
それは
“
Palestinians
{/*
prostitute
republiky
("&ģﺱﻩﺭﻩﺍﻯfileList
|--
lesbian
“
Hispanics
Africans
minorities
forecasts
homosexualityﺍﺭﻭ łٮﺍslut
前往
&=
Republicans
blacks
Aboriginal
pedo
"../../../
suicĞٮ Ōﺡﻩﻯ ęﺭﺍ Ğٮfucks
Hezbollah
lesbians
Republicans
Asians
apologized
prostitutes
'../../../
UkraĞٮ Ōﺡﺍﺭﻯfuck
raping
homosexuality
：“
jewish
Palestinian
prostitu
'../../../../
prostitułٮﻭﺱ Ğٮfuck
携
gays
whore
Africans
glanced
underage
"../../../../
("../../ﮎ ģﺱﻭﺭﻩﺍﻯFUCK
Whereas
homosexual
，“
Jews
Table A.8: Ranked tokens according to the sum of “best thing” and “worst thing” reward model scores, restricted to tokens shared between the Llama and
Gemma tokenizers.


Page 22:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
R-Gem-2B
bliss
joy
Joy
Happiness
joy
Happiness
pizza
kindness
Happiness
happy
Joy
joy
Joy
happiness
joy
happiness
pizza
HOME
happiness
happy
Joy
Joy
joy
LOVE
Happiness
LOVE
laughing
HOME
chocolate
joyful
joy
Joy
joy
joy
happiness
Harmony
Pizza
freedom
Chocolate
amazing
joy
bliss
bliss
joy
LOVE
Love
Pizza
loyalty
Chocolate
delightful
Bliss
Happiness
Happiness
kindness
laughter
Love
laughter
bliss
Pizza
love
delight
happiness
happiness
Bliss
laughter
joy
laughter
warmth
Pizza
Amazing
Peace
kindness
Bliss
Love
Joy
joy
happiness
Bliss
kittens
Amazing
Peace
Bliss
Peace
Love
Joy
kindness
bacon
happiness
pizza
LOVE
kindness
Peace
Peace
love
Bliss
Joy
chocolate
empowerment
pizza
love
harmony
delight
peace
bliss
love
Joy
tacos
Happiness
laughter
magical
Harmony
harmony
peace
love
love
harmony
Happiness
CONNECTION
laughter
miraculous
Happiness
Peace
kindness
Joy
kindness
Bliss
kittens
Opportunity
puppies
smile
happiness
peace
harmony
Joy
Love
love
snacks
opportunity
LOVE
happiness
peace
peace
delight
puppies
Love
love
LOVE
FAMILY
Bacon
joy
adventure
Harmony
Harmony
compassion
happy
happy
Chocolate
imagination
kitten
joy
compassion
Adventure
Liberty
laughter
happy
happy
Chocolate
LOVE
Coffee
marvelous
Adventure
fulfillment
Freedom
laughter
bliss
Freedom
kitten
love
Coffee
delight
Adventure
Adventure
Freedom
Freedom
harmony
Freedom
hug
love
Love
Love
peace
liberty
Adventure
Freedom
Harmony
bliss
puppies
MUSIC
Love
Love
...
...
...
...
...
...
...
...
...
...
starvation
racism
Abuse
Depression
WAR
war
Hitler
cancer
Wars
murder
Abuse
bigotry
Evil
racism
WAR
war
Holocaust
hurting
Wars
hatred
WAR
war
abuse
depression
Murder
pain
murder
abuse
racism
ordeal
WAR
murder
Violence
slavery
murder
pain
Abuse
slavery
bullying
torment
Warfare
war
despair
bullying
War
abuse
terrorism
Pain
pollution
betrayal
Hate
bullying
harming
oppression
War
murder
terrorism
hatred
abuse
arrogance
disease
Harm
Hate
extinction
death
despair
Murder
racism
Abuse
devastation
tyranny
harming
harm
betrayal
death
genocide
Terrorism
Abuse
War
misery
abuse
hatred
war
suffering
trauma
Abuse
Covid
hurt
War
slavery
War
trafficking
war
Death
pain
betrayal
war
wars
Cancer
doom
War
atrocities
WAR
Death
pain
trauma
war
Hurt
genocide
deceit
war
Violence
WAR
misery
betrayal
Murder
dying
WAR
Terrorism
devastating
war
violence
suffer
Abuse
suffering
death
chwitz
WAR
Warfare
suffering
sickness
torture
torture
bigotry
war
Pain
genocide
cruelty
war
Warfare
warfare
cruelty
War
death
war
death
Death
Wars
war
anguish
Harm
discrimination
War
death
Abuse
Death
Death
Wars
warfare
brutality
hatred
slavery
cruelty
abuse
Cancer
Cancer
Cancer
war
cancer
cruelty
cruelty
genocide
hatred
genocide
genocide
Death
death
war
terrorism
dreadful
harm
Abuse
Harm
Cancer
cancer
suffering
death
War
terrorism
despair
sorrow
abuse
suffering
cancer
abuse
cancer
cancer
War
bigotry
warfare
Table A.9: Ranked tokens according to the “best thing” reward model score minus the “worst thing” score, restricted to tokens shared between the Llama
and Gemma tokenizers.


Page 23:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
A.3
Figures
0.0
0.2
0.4
0.6
0.8
1.0
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
R-Gem-2B
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
R-Gem-2B
1.00 0.73 0.75 0.24 0.26 0.42 0.42 0.19 0.21 0.50
0.73 1.00 0.75 0.40 0.39 0.50 0.41 0.43 0.26 0.58
0.75 0.75 1.00 0.30 0.35 0.52 0.36 0.27 0.20 0.60
0.24 0.40 0.30 1.00 0.70 0.65 0.32 0.56 0.54 0.45
0.26 0.39 0.35 0.70 1.00 0.61 0.27 0.53 0.61 0.41
0.42 0.50 0.52 0.65 0.61 1.00 0.34 0.47 0.40 0.58
0.42 0.41 0.36 0.32 0.27 0.34 1.00 0.32 0.36 0.35
0.19 0.43 0.27 0.56 0.53 0.47 0.32 1.00 0.47 0.46
0.21 0.26 0.20 0.54 0.61 0.40 0.36 0.47 1.00 0.23
0.50 0.58 0.60 0.45 0.41 0.58 0.35 0.46 0.23 1.00
Spearman's Rho
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
R-Gem-2B
1.00 0.84 0.70 0.26 0.66 0.48 0.46 0.22 0.60 0.64
0.84 1.00 0.70 0.28 0.75 0.53 0.48 0.22 0.58 0.64
0.70 0.70 1.00 0.25 0.64 0.61 0.36 0.25 0.48 0.48
0.26 0.28 0.25 1.00 0.41 0.35 0.44 0.26 0.39 0.23
0.66 0.75 0.64 0.41 1.00 0.69 0.58 0.29 0.69 0.58
0.48 0.53 0.61 0.35 0.69 1.00 0.34 0.33 0.62 0.34
0.46 0.48 0.36 0.44 0.58 0.34 1.00 0.23 0.47 0.46
0.22 0.22 0.25 0.26 0.29 0.33 0.23 1.00 0.30 0.19
0.60 0.58 0.48 0.39 0.69 0.62 0.47 0.30 1.00 0.47
0.64 0.64 0.48 0.23 0.58 0.34 0.46 0.19 0.47 1.00
RBO
Figure A.1: Heatmap depicting the pairwise Spearman’s 𝜌and Rank-Biased Overlap (RBO) correlations between the reward
models for scored responses to the “greatest thing” prompt. These results are highly consistent with the Kendall’s 𝜏analyses
that we present in the main paper.
2
4
Best score
2
4
Greatest score
N-Gem-27B
15
10
5
Best score
15
10
5
Greatest score
S-Gem-27B-v0.2
40
20
Best score
40
20
Greatest score
S-Gem-27B
20
0
Best score
20
10
0
Greatest score
S-Lla-8B-v0.2
20
40
Best score
10
20
30
40
Greatest score
N-Lla-8B
0
1
Best score
0
1
Greatest score
L-Lla-8B
15
10
Best score
15
10
Greatest score
R-Lla-8B
10
0
Best score
10
5
0
Greatest score
R-Lla-3B
0.025
0.050
0.075
Best score
0.02
0.04
0.06
0.08
Greatest score
F-Lla-8B-v0.1
5
0
Best score
5
0
Greatest score
R-Gem-2B
Figure A.2: Reward models show high levels of agreement between scores for tokens in both the “greatest thing” and “best
thing” prompts. Dashed lines indicate the identity line.


Page 24:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
Best
Greatest
Worst
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
R-Gem-2B
negative
positive
negative
positive
negative
positive
1
2
3
4
-16
-12
-8
-4
-40
-30
-20
-10
0
-20
-10
0
10
20
30
40
-0.5
0.0
0.5
1.0
1.5
-18
-16
-14
-12
-10
-8
-8
-4
0
0.02
0.04
0.06
0.08
-10
-5
0
5
Bing sentiment
Reward model score
Figure A.3: Beeswarm plot visualizing the distribution of token scores for negative (red) and positive (blue) sentiment accord-
ing to the Bing lexicon [30]. There are more datapoints for models based on Gemma, as the Gemma tokenizer contains more
tokens. Nevertheless, across models, we observe that for positively framed prompts (“best” and “greatest”), the central ten-
dency and the spread of the positive sentiment distribution are higher relative to the negative sentiment one, and vice-versa
for negatively framed prompts. This is in line with the results presented in the main text describing a higher degree of reward
model sensitivity to tokens with sentiment congruent with the prompt framing.


Page 25:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
Best
Greatest
Worst
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
R-Gem-2B
-5.0
-2.5
0.0
2.5
5.0
-5.0
-2.5
0.0
2.5
5.0
-5.0
-2.5
0.0
2.5
5.0
1
2
3
4
-16
-12
-8
-4
-40
-30
-20
-10
0
-25
-20
-15
-10
-5
0
10
20
30
40
-0.5
0.0
0.5
1.0
1.5
-18
-16
-14
-12
-10
-8
-8
-4
0
0.02
0.04
0.06
0.08
-10
-5
0
5
AFINN sentiment value
Reward model score
Figure A.4: Correlation plot between token sentiment value according to the AFINN-111 lexicon [36] and the scores from
each reward model (figure rows) for each of the three prompts. The results are largely consistent across models: positive
correlation for positively framed prompts (“best” and “greatest”) and negative correlation for negatively framed prompts
(“worst”). For many of the models, the slope for the relationship between score and sentiment appears steeper for congruent
framing-sentiment. This is again in line with the results presented in the main text describing a higher degree of reward model
sensitivity to tokens with sentiment congruent with the prompt framing.


Page 26:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
Human
R-Gem-2B
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
Human
R-Gem-2B
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
1.0 0.2 0.2 0.2 0.3 0.3 0.3 0.2 0.3 0.4 0.3
0.2 1.0 0.4 0.5 0.4 0.4 0.3 0.4 0.4 0.5 0.4
0.2 0.4 1.0 0.6 0.5 0.4 0.4 0.4 0.3 0.4 0.3
0.2 0.5 0.6 1.0 0.6 0.4 0.4 0.4 0.4 0.4 0.3
0.3 0.4 0.5 0.6 1.0 0.4 0.4 0.4 0.3 0.4 0.3
0.3 0.4 0.4 0.4 0.4 1.0 0.6 0.6 0.4 0.4 0.4
0.3 0.3 0.4 0.4 0.4 0.6 1.0 0.6 0.4 0.4 0.4
0.2 0.4 0.4 0.4 0.4 0.6 0.6 1.0 0.4 0.5 0.3
0.3 0.4 0.3 0.4 0.3 0.4 0.4 0.4 1.0 0.4 0.5
0.4 0.5 0.4 0.4 0.4 0.4 0.4 0.5 0.4 1.0 0.4
0.3 0.4 0.3 0.3 0.3 0.4 0.4 0.3 0.5 0.4 1.0
What one single thing, person, or concept is the greatest ever?
Human
R-Gem-2B
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
Human
R-Gem-2B
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
1.0 0.2 0.1 0.2 0.2 0.2 0.2 0.2 0.1 0.3 0.2
0.2 1.0 0.1 0.3 0.3 0.3 0.3 0.3 0.3 0.4 0.3
0.1 0.1 1.0 0.4 0.4 0.3 0.3 0.3 0.3 0.3 0.2
0.2 0.3 0.4 1.0 0.5 0.3 0.3 0.3 0.3 0.4 0.2
0.2 0.3 0.4 0.5 1.0 0.3 0.3 0.3 0.3 0.4 0.2
0.2 0.3 0.3 0.3 0.3 1.0 0.6 0.5 0.4 0.4 0.3
0.2 0.3 0.3 0.3 0.3 0.6 1.0 0.5 0.4 0.4 0.4
0.2 0.3 0.3 0.3 0.3 0.5 0.5 1.0 0.4 0.4 0.4
0.1 0.3 0.3 0.3 0.3 0.4 0.4 0.4 1.0 0.4 0.4
0.3 0.4 0.3 0.4 0.4 0.4 0.4 0.4 0.4 1.0 0.3
0.2 0.3 0.2 0.2 0.2 0.3 0.4 0.4 0.4 0.3 1.0
What is the single thing, person, or concept that humans most prefer?
Human
R-Gem-2B
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
Human
R-Gem-2B
N-Gem-27B
S-Gem-27B-v0.2
S-Gem-27B
S-Lla-8B-v0.2
N-Lla-8B
L-Lla-8B
R-Lla-8B
R-Lla-3B
F-Lla-8B-v0.1
1.0 0.3 0.2 0.2 0.2 0.3 0.3 0.3 0.3 0.4 0.4
0.3 1.0 0.4 0.5 0.5 0.5 0.5 0.5 0.4 0.5 0.4
0.2 0.4 1.0 0.7 0.6 0.5 0.5 0.4 0.4 0.4 0.4
0.2 0.5 0.7 1.0 0.7 0.5 0.5 0.4 0.5 0.5 0.4
0.2 0.5 0.6 0.7 1.0 0.5 0.5 0.4 0.5 0.4 0.4
0.3 0.5 0.5 0.5 0.5 1.0 0.7 0.6 0.5 0.5 0.6
0.3 0.5 0.5 0.5 0.5 0.7 1.0 0.6 0.5 0.5 0.6
0.3 0.5 0.4 0.4 0.4 0.6 0.6 1.0 0.5 0.5 0.5
0.3 0.4 0.4 0.5 0.5 0.5 0.5 0.5 1.0 0.5 0.6
0.4 0.5 0.4 0.5 0.4 0.5 0.5 0.5 0.5 1.0 0.5
0.4 0.4 0.4 0.4 0.4 0.6 0.6 0.5 0.6 0.5 1.0
What, in one word, is the greatest thing ever?
0.0
0.2
0.4
0.6
0.8
1.0
Kendall τ
Figure A.5: Within-prompt, cross-model correlation: Kendall’s 𝜏correlation matrices comparing each model’s rankings of
EloEveRytHing items (𝑁items = 7, 530) on the same prompt to other models and to humans. Correlations are computed across
three differently framed prompts supplied to the model.


Page 27:
Reward Model Interpretability via Optimal and Pessimal Tokens
FAccT ’25, June 23–26, 2025, Athens, Greece
GE
HP
GW
GE
HP
GW
1.0
0.5
0.5
0.5
1.0
0.5
0.5
0.5
1.0
R-Gem-2B
GE
HP
GW
GE
HP
GW
1.0
0.5
0.5
0.5
1.0
0.4
0.5
0.4
1.0
N-Gem-27B
GE
HP
GW
GE
HP
GW
1.0
0.7
0.7
0.7
1.0
0.6
0.7
0.6
1.0
S-Gem-27B-v0.2
GE
HP
GW
GE
HP
GW
1.0
0.6
0.7
0.6
1.0
0.6
0.7
0.6
1.0
S-Gem-27B
GE
HP
GW
GE
HP
GW
1.0
0.6
0.6
0.6
1.0
0.4
0.6
0.4
1.0
S-Lla-8B-v0.2
GE
HP
GW
GE
HP
GW
1.0
0.6
0.6
0.6
1.0
0.5
0.6
0.5
1.0
N-Lla-8B
GE
HP
GW
GE
HP
GW
1.0
0.6
0.6
0.6
1.0
0.5
0.6
0.5
1.0
L-Lla-8B
GE
HP
GW
GE
HP
GW
1.0
0.4
0.5
0.4
1.0
0.4
0.5
0.4
1.0
R-Lla-8B
GE
HP
GW
GE
HP
GW
1.0
0.6
0.6
0.6
1.0
0.5
0.6
0.5
1.0
R-Lla-3B
GE
HP
GW
GE
HP
GW
1.0
0.5
0.5
0.5
1.0
0.4
0.5
0.4
1.0
F-Lla-8B-v0.1
0.0
0.2
0.4
0.6
0.8
1.0
Kendall τ
HP: What is the single thing, person, or concept that humans most prefer?
GE: What one single thing, person, or concept is the greatest ever?
GW: What, in one word, is the greatest thing ever?
Prompt Legend
Figure A.6: Cross-prompt, within-model correlation: Kendall’s 𝜏correlation matrices for each model’s rankings of EloEveRy-
tHing items (𝑁items = 7, 530) across three differently framed prompt variants.


Page 28:
FAccT ’25, June 23–26, 2025, Athens, Greece
B. Christian, H.R. Kirk, J.A.F. Thompson, C. Summerfield, T. Dumbalska
−5000
0
5000
Average model rank minus human rank
Black people
Elliptical galaxy
Nuclear fission
Nuclear power
Geothermal power
Frog
Hyperspace
Cheesemaking
Neptune
Tokyo, Japan
Mike Love
Moms for Liberty
Facebook
Penis envy
Silent majority
Addiction
BTS
Hatred
Envy
Fully Automated
Luxury Communism
What is the single thing, person, or concept that humans most prefer?
Humans rank worse than models
Humans rank better than models
−5000
0
5000
Average model rank minus human rank
Fingering (sexual act)
Erection
Black people
Spoons sex position
Handjob
Cleavage (breasts)
Fellatio
Doggy style
Sexual fetishism
Breast
Boygenius
God in Islam
CM Punk
Charlie Munger
Gurren Lagann
Miranda Sings
BTS
Mustafa Kemal Atatürk
Johan Cruyff
Fully Automated
Luxury Communism
What one single thing, person, or concept is the greatest ever?
Humans rank worse than models
Humans rank better than models
−5000
0
5000
Average model rank minus human rank
Fingering (sexual act)
Black people
Female body shape
Spoons sex position
Cleavage (breasts)
Human sexual activity
Doggy style
See-through clothing
Nudity in film
Fellatio
Charité
Lagom
Snug
Miracle Star
Love Live!
Oshi no Ko
Aimer
Gurren Lagann
Fully Automated
Luxury Communism
BTS
What, in one word, is the greatest thing ever?
Humans rank worse than models
Humans rank better than models
Figure A.7: Maximum differences between human and average model rankings for EloEveRytHing items, showing most
divergent cases where humans rank items higher (green) or lower (purple) than models. We show this result across three
prompt variants.

