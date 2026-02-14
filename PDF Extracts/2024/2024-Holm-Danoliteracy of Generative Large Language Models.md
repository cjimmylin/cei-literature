---
title: "2024-Holm-Danoliteracy of Generative Large Language Models - PDF Extract"
source_pdf: "2024-Holm-Danoliteracy of Generative Large Language Models.pdf"
pages: 16
extracted_at: "2026-02-13T13:13:50.274087"
---

# PDF Extract: 2024-Holm-Danoliteracy of Generative Large Language Models

**Source PDF:** 2024-Holm-Danoliteracy of Generative Large Language Models.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

Danoliteracy of Generative Large Language Models
Søren Vejlgaard Holm1,2, Lars Kai Hansen1, Martin Carsten Nielsen2
1Technical University of Denmark, Anker Engelunds Vej 1, 2800 Kongens Lyngby, Denmark,
2Alvenir, Applebys Plads 7, 1411 København K, Denmark
Correspondence: swiho@dtu.dk
Abstract
The language technology moonshot mo-
ment of Generative Large Language Mod-
els (GLLMs) was not limited to English:
These models brought a surge of techno-
logical applications, investments, and hype
to low-resource languages as well. How-
ever, the capabilities of these models in
languages such as Danish were, until re-
cently, difficult to verify beyond qualita-
tive demonstrations due to a lack of ap-
plicable evaluation corpora. We present
a GLLM benchmark to evaluate Danolit-
eracy, a measure of Danish language and
cultural competency across eight diverse
scenarios such as Danish citizenship tests
and abstractive social media question an-
swering. This limited-size benchmark was
found to produce a robust ranking that cor-
relates to human feedback at ρ ∼0.8 with
GPT-4 and Claude Opus models achiev-
ing the highest rankings. Analyzing these
model results across scenarios, we find one
strong underlying factor explaining 95% of
scenario performance variance for GLLMs
in Danish, suggesting a g factor of model
consistency in language adaptation.
1
Introduction
Benchmarks shape technologies.
By acting as
normative guidelines for technology applications,
benchmarks imply directions of research and de-
velopment that ultimately impact users(Liang et al.,
2022). GLLMs specifically have emerged as a tech-
nology with near-universal impact, including lower-
resource languages such as Danish (Olsen, 2023).
If the challenging task of general GLLM evaluation
is not extended to low-resource languages, practi-
tioners start from scratch for each model use case,
inhibiting practical adoption or possibly resulting
in risky, undertested implementations.
83 GLLMs
🎯
8 Scenarios
Evaluation
Aggregation
Uncertainty Estimation
Factor Analysis
Claude 🔒
🎯
🎯
GPT 4 🔒
Mixtral
Citizenship Tests
#twitterhjerne
Corpus
Metric
Prompt
Corpus
Metrics
Prompt
Munin
🌍
🌍
🌍
Figure 1: The overall evaluation setup: A collection
of GLLMs, including closed-source (lock symbol)
instruct-tuned (bulls-eye) and multilingual (globe)
ones, were evaluated in Danish across diverse use-
case scenarios.
We take up the challenge of creating a GLLM
evaluation benchmark for Danish, a North Ger-
manic language spoken by 6 million people, primar-
ily in the Nordic country of Denmark. As depicted
in Figure 1, our approach is to create a compila-
tion of small-scale, diverse evaluation scenarios
combined into one general benchmark to reveal
model Danoliteracy. By Danoliteracy we refer to
the level of GLLM real-world knowledge (RWK),
natural language understanding (NLU), and natural
language generation (NLG) in Danish.
arXiv:2410.22839v2  [cs.CL]  4 Mar 2025

--- Page 2 ---

This paper presents the resulting Danoliter-
ate Benchmark, describing evaluation methods,
datasets and model results. We analyze these re-
sults with the goals of validating and exploring
evaluation methodology. An important part of this
analysis is to investigate the feasibility of such eval-
uation: Does this small-scale, language-specific
approach achieve a significant ranking of GLLMs?
Even if a non-spurious leaderboard can be dis-
cerned from the result, it is not enough to validate
the benchmark which might actually show some-
thing orthogonal to Danoliteracy. Thus, as a bench-
mark validation tool, we additionally present a user
survey, collecting the preferences of Danish speak-
ers when interacting with hidden pairs of GLLMs
in an arena A/B test setup.
The availability of a suite of meaningful bench-
mark results allows us to investigate GLLM be-
havior: Initially, we explore which specific models
are most Danoliterate and how different types of
GLLMs compare. Beyond that, we are particularly
interested in capability consistency across tasks:
If a GLLM performs strongly in one Danish use-
case scenario, does this performance generalize to
other Danish scenarios across different domains
and objectives?
We hope so. If the answer is no, practition-
ers are without general results to trust, requiring
a full model re-evaluation for each downstream
use. However, if capability consistency is present,
we should be able to find a single underlying axis
that correlates with performance across diverse sce-
narios. Such a general dimension of Danoliteracy
can be compared to the g factor of general human
intelligence (Spearman, 1904). If one significant,
main factor is found, it implies a level of stability
that can help guide the expectations of practitioners
across GLLM implementations in varying and even
novel Danish tasks.
The contributions presented in this paper can be
summarized as follows:
• An open-source benchmark for GLLMs in
low-resource languages with an evaluation
framework and a live leaderboard site.
• The release of a set of novel evaluation
datasets for Danish.
• Evidence that GPT-4 and Claude Opus mod-
els are currently uniquely capable in Danish,
outperforming other closed models which in
turn overcome open-weights models.
• Evidence suggesting the existence of a Dano-
literacy g factor in GLLMs supported by pre-
liminary results from our open-source human
feedback study.
2
Related Work
2.1
GLLM Evaluation
The hard task of evaluating free-generation, mul-
titask models has been attempted in many ways.
Liang et al. define an empirical approach for re-
vealing model behaviour: Evaluate each model
on a compilation of many scenarios and use-cases
of interest, spanning different languages, domains
and task categories – ideally across multiple per-
formance dimensions in addition to raw model ca-
pability such as efficiency, bias, and robustness
(Liang et al., 2022).
This scenario compilation approach has been
applied in many ways to GLLMs: The HELM
Lite benchmark presents evaluations of GLLMs
on question answering (QA) and translation tasks
(Liang et al., 2023). Influential benchmarks include
the Huggingface OpenLLM Leaderboard (Beech-
ing et al., 2023) and other implementations of the
knowledge-based scenarios MMLU (Hendrycks
et al., 2021) and HellaSwag (Zellers et al., 2019).
These benchmarks mainly use comparison or
similarity algorithms to parse model answers e.g.
for finding a chosen option for multiple-choice QA.
Other approaches include applying other GLLMs
to grade generations (Zheng et al., 2023) (Ope-
nAI, 2023) or using human feedback (Chiang et al.,
2024).
2.2
Low-resource NLP Evaluation
Most broadly reported GLLM evaluations are only
or primarily performed on examples in English.
Approaches to evaluate lesser-resourced languages
include both attempts to compile massively multi-
lingual benchmarks either by automatic translation
(Lai et al., 2023) or dataset curation (Ahuja et al.,
2023).
Other approaches focus on one language exclu-
sively in attempts to evaluate GLLM language per-
formance beyond surface-level lexical or syntacti-
cal literacy. Using this method, practitioners can
align scenario domain, cultural content, and real-
world facts with the setting of the language, though
a lack of relevant data can be problematic (Liu
et al., 2023).

--- Page 3 ---

Specifically in Danish, the comprehensive Scan-
dEval benchmark, which packages scenarios across
eight languages divided into NLU and NLG leader-
boards, implements evaluation on GLLMs in Dan-
ish on eight NLG scenarios with some overlap in
dataset sources with this work (Nielsen, 2023).
2.3
GLLM g Factor
The idea that GLLM performance is strongly corre-
lated across tasks has been noted previously by for
example Ili´c who carried out factor analysis on the
Open LLM Leaderboard and GLUE, (Wang et al.,
2018) obtaining results similar to ours (Ili´c, 2023).
3
Methods
3.1
Datasets
The eight scenario datasets are divided into three
broad categories: Scenarios testing RWK, scenar-
ios requiring models to perform free NLG and
those that imply solving classical NLU tasks.
Real-world Knowledge
1. Citizenship Test is a novel dataset of 605
multiple-choice questions acquired from gov-
ernmental tests that require applicants for Dan-
ish citizenship to demonstrate familiarity with
national societal structure, culture, and history
(siri.dk, 2023).
2. HyggeSwag is a novel manual translation1 of
125 HellaSwag (Zellers et al., 2019) Activi-
tyNet (Caba Heilbron et al., 2015) questions
testing commonsense natural language infer-
ence as a multiple-choice task to pick the only
completion consistent with real-world logic.
3. Gym 2000 is a small, novel extraction of
50 literature comprehension multiple-choice
questions from the Danish Centre for Read-
ing Research (CRR) aimed at high-schoolers
(Arnbak and Elbro, 2000).
Free NLG
4 #twitterhjerne is a novel abstractive question-
answering dataset containing 78 anonymized
question tweets from the Danish hashtag of
that name, translated to Twitter Brain, where
users ask the social media hive mind for help,
input or recommendations. For each question
1The text was translated by the authors with each transla-
tion being validated by another author completing the infer-
ence task.
Cit. Test [RWK]
HSwag
[RWK]
Gym 2K
[RWK]
#twit. [NLG]
NN [NLG]
AT [NLU]
Cloze [NLU]
DaNE [NLU]
20
40
60
80
100
GLLMs Relative Scores Across Scenarios
GPT 4
Claude Opus
LlaMa 3 70B
DanskGPT-tiny Chat
Figure 2:
Selected model normalized results
across the eight scenarios divided into three cat-
egories as described in Section 3.1. Claude Opus is
overtaken by GPT-4 on the NER task but wins on an
NLG task. LlaMa 3 70B, the SOTA open-weights
model, lags behind on NLU and knowledge-based
tasks. A Danish-specialized model with only 1.1B
parameters, DanskGPT-tiny Chat, benchmarks well
in NLG but fails on knowledge and understanding.
tweet, 2-9 reference answer tweets were ex-
tracted making it possible to use the scoreo1o
metric (1).
5 Nordjylland News is an existing news sum-
marization dataset (Kinch, 2023) from which
a subset of 300 short news articles with corre-
sponding summaries were used.
NLU Tasks
6 Cloze Self Test is another small, novel extrac-
tion from CRR materials (Jensen et al., 2015),
this one containing 33 cloze-style questions
evaluated as multiple-choice selection.
7 DaNE is an existing canonical Danish NER
dataset with four entity categories (Hvingelby
et al., 2020) from which a subset of 256 exam-
ples were used.
8 Angry Tweets is an existing sentiment clas-
sification dataset (Brogaard Pauli et al., 2021,
Sec. 4) with three sentiment categories from
which 256 examples were used for multiple-
choice prompts.

--- Page 4 ---

Cit. Test
(Acc.) HSwag
(Acc.)
Gym 2K
(Acc.)
#twit.
(1
o1o) NN
(Sim.)
AT
(Acc.)
Cloze
(Acc.)
DaNE
(mF1)
0
20
40
60
80
100
RWK
NLG
NLU
Model Scores on Scenarios
Claude Opus
Starling 7B
Figure 3:
The non-normalized metric scores
across evaluation scenarios for two models that
were judged highly according to human feedback.
Uncertainties are 95% confidence intervals accord-
ing to the bootstrapping procedure and the micro-
average is displayed for each model. k
All datasets are released on the Huggingface
Datasets Hub with dataset cards2 except for the
two small datasets extracted from CRR which re-
quire practitioners to re-run data collection for per-
sonal use. More details on dataset licensing and
collection as well as data examples can be found in
Appendix B.
3.2
Evaluation
Each evaluation scenario consisted of a dataset, a
prompt template, and a chosen metric.
Most of the available datasets allowed primarily
for testing discriminative RWK and NLU of the
GLLM by requiring it to select between multiple-
choice answers. For these multiple-choice scenar-
ios, frequency of generating the correct option num-
ber was reported as model accuracy.
Two metrics were used for NLG. First, summa-
rization was implemented using a similarity score
between model summary and a reference summary
s (TM, Tref). Secondly, we implemented abstrac-
tive question answering tasks for the specific type
of dataset D where each question has not just one
correct answer but a corresponding set of reference,
human-generated answers. This was done by scor-
ing GLLMs using the frequency with which gen-
erated answers were the odd-one-out, defined by
the lowest total similarity to all possible answers
2Datasets
can
be
found
on
danoliter-
ate.compute.dtu.dk/Scenarios
T = {TM} ∪{Tref, i}i=1..k as shown in Eq. 1.
For similarity scores s, the BERT score algorithm
(Zhang* et al., 2020) based on the DFM Encoder
Large (Enevoldsen et al., 2022) was used.
scoreo1o = PD

TM = argmin
t1∈T
X
t2∈T
s (t1, t2)


(1)
Finally, few-shot named entity recognition (NER)
was implemented for GLLMs using 3-shot prompt-
ing and the GPT-NER multiple queries idea (Wang
et al., 2023). Here, word-level entity class predic-
tions were aligned and the standard NER micro-
average F1 scores were calculated using the SeqE-
val framework (Nakayama, 2018).
Scenarios were operationalized by prompting
GLLMs in the scenario language, Danish, and
structuring prompts with headers marked with the
# character as in Markdown. In order to use the
same prompts for instruct-tuned and base GLLMs,
prompts started with the instruction and ended with
a text leading towards an answer in the continua-
tion as shown in Figure 4. Prompting and metric
implementation details are covered in Appendix A.
1
Write a one-sentence summary of the
text.
2
# TEXT
3
Lorem ipsum dolor sit amet ...
4
# SUMMARY
5
A summary of the text could be:
Figure 4: The general prompting approach trans-
lated to English.
3.3
Models
Both local prediction of open-weights models and
API access to externally hosted GLLMs were im-
plemented. 54 autoregressive, decoder language
models trained for general text generation were in-
cluded. Models were tested if we saw any reason
to suspect a degree of Danoliteracy, thus including
multilingual models with possibly small amounts
of Danish training data as well as other Main-
land Scandinavian monolingual models but exclud-
ing strictly English-only models. Both base and
instruct-tuned models were evaluated. All model
generation was performed with greedy decoding
and with a maximum number of generated model
tokens of 256. OpenAI’s o1 model was allowed
to generate internal tokens freely. The models run

--- Page 5 ---

EuroLLM 
9B In.
Davinci 
003
Gemma 
2 9B 
Instruct
Gemini 
Pro
LlaMa 
3 70B
GPT 
3.5 Turbo 
In.
Claude 
Haiku
GPT 
3.5 Turbo
Claude 
Sonnet
LlaMa 
3.3 70B
Claude 
3.5 Sonnet
LlaMa 
3.2 90B
GPT 
4o mini
o1 
Mini
GPT 
4 Turbo 
2023
Claude 
Opus
GPT 
4 Turbo 
2024
GPT 
4
GPT 
4o
o1 
Preview
57
64
64
72
72
72
73
75
76
78
80
80
83
90
91
92
92
93
93
97
Top 20 GLLMs
And Their Pairwise Signficance
Figure 5:
Model Danoliteracy Index across all
scenarios for top performers. Two model nodes are
connected iff the bootstrapping procedure could
not reveal significant benchmark performance dif-
ference at α = 0.05. Together with the special o1
model, Claude Opus and the GPT 4 family models
are consistent winners.
locally ranged in sizes from 124M parameters to
13B parameters, resulting in a total project GPU
use of ∼100 hours on a single Nvidia H100.
3.4
The Danoliterate Framework
A modular, open-source evaluation framework was
implemented in Python, using Huggingface Trans-
formers (Wolf et al., 2019) and Datasets (Lhoest
et al., 2021) as central tools as well as Hydra
(Yadan, 2019) and a Weights and Biases-integration
(Biewald, 2020) for structuring experimentation.
This framework, danoliterate, is released on
GitHub3 under the MIT License.
Furthermore, an interactive site displaying the
leaderboard as well as other benchmark results and
examples was produced using the Streamlit frame-
work. See Figure 6 for a screenshot of this frontend
and Appendix A.4 for versions of software depen-
dencies.
3.5
Human Feedback
For a subset of 18 instruct-tuned models, we have
set up a parallel study to collect human judgment
on model performance. Volunteers were presented
with a anonymized pair of models and were asked
3github.com/sorenmulli/danoliterate
Figure 6: A screenshot from the leaderboard front-
end allowing users to explore how model results
change with different metric choices as well as
inspecting model output examples and reading fur-
ther details on evaluation scenarios.
to report their preferred model. This was done
based on side-by-side model answers on at least
three prompts selected by the volunteer from a pool
of 100 prompt examples. Prompt selection was
chosen independently of the Danoliterate Bench-
mark by creating one Danish prompt for each of
100 popular generative AI use-cases according to
Zao-Sanders (Zao-Sanders, 2024). The study is
ongoing: At the time of writing, 477 responses
were analyzed. More details on data collection and
analysis can be seen in Appendix C.
4
Results
4.1
Benchmark Feasibility
Benchmarks must have a sufficiently clear signal
to be useful. The ranking in the final leaderboard
should be determined by meaningful model differ-
ences and influenced minimally by sampling noise.
To quantify benchmark noise, we implemented
blocked bootstrapping, resampling all examples
with replacement and aggregating all N = 8 sce-
nario scores for each of the M = 83 models. For
each K = 10, 000 bootstrap samples, the M × N
model scenario results were aggregated into one
overall Danoliteracy Index for each model dM.
This index was computed by considering one sce-
nario at a time, assigning to the winner index 100
and to the lowest-scoring model index 0 with a lin-
ear scaling between the two. The micro-average
across the N scenarios is reported as the resulting
Danoliteracy Index of the sample.
The median index is presented as the main
leaderboard of this report4 with top 20 shown in
4The full M×N version can be seen at the live leaderboard
site: danoliterate.compute.dtu.dk/Leaderboard.

--- Page 6 ---

DanskGPT 
tiny Chat
Munin 
NeuralBeagle
Qwen1.5 
7B Chat
SOLAR 
10.7B In.
Mistral 
7B In. 
v0.2
LlaMa 
3 8B 
In.
Gemma 
7B In.
LlaMa 
3 70B
Mixtral 
8x7B
Heidrun 
7B Chat
Starling 
7B
GPT 
3.5 Turbo
Claude 
Sonnet
GPT 
4 Turbo 
2024
Gemini 
Pro
Claude 
Haiku
GPT 
4o
Claude 
Opus
4
7
12
24
30
32
43
43
43
50
59
61
70
78
80
80
86
89
Human Feedback Ranking
Bradley-Terry Model
Figure 7:
Model Danish capabilities based on
human feedback. Values are normalized Bradley-
Terrey coefficients where two models are connected
if the coefficients are not significantly different in
the ranking model described in Appendix C.3.
Figure 5. For these, pairwise model index compar-
isons were performed using the bootstrap samples,
correcting p values to control the false discovery
rate across 1
2M ×(M −1) comparisons (Benjamini
and Hochberg, 1995), presenting significant differ-
ences at α = 5%.
The results show groups of similarly perform-
ing models whose Danoliteracy cannot be distin-
guished. This increases the lower you go: Many
mediocre models, especially non instruct-tuned
models, get dM ∼20: As an example, this small-
sample size, curated benchmark cannot reveal a
difference between the base models LlaMa 2 7B,
dL2 = 20, and LlaMa 3 8B, dL3 = 23.
However, robust separation is visible for some
models, providing basis for statements like ”The
different GPT-4 models benchmark at the same
level but clearly perform better than GPT-3 models”
or ”The bigger the Claude 3, the better the perfor-
mance – but even the cheap Haiku version performs
at GPT-3.5 level” or ”Small, Danish-specialized
models like Heidrun can perform at LlaMa 2 70B
level but LlaMa 3 has moved the SOTA for open-
weights models in Danish”. This signal allows us
to learn more about reasons for model performance
which we explore in the next section.
First, we turn to the important question of valid-
ity: We see a robust benchmark signal resulting in
a significant ranking but must question the mean-
ing of the signal. One superficial indication of a
meaningful signal is that, as expected, the rank-
ing correlates significantly with model parameter
counts5 ρ ∼0.6. However, more importantly: We
find that it does correlate with the preliminary re-
sults of our Danish human judgement survey.
Ranking human judgement using the Bradley-
Terry model as in (Chiang et al., 2024, Sec. 4), we
achieve a ranking shown in Figure 7. We observe
meaningful differences compared to the Danoliter-
acy Index: For example, Claude models are more
competitive against GPT 4 and the title as best
included open-weights model is taken by Nexus-
flow Starling (Zhu et al., 2023) from LlaMa 3 70B.
Crucially, however, the general ranking is similar,
resulting in a correlation6 of ρ ∼0.8 with the Dano-
literacy Index for these 18 judged models. We note
this as a high value. As a comparison, the Danolit-
eracy index has a weaker correlation with English
benchmarks like HELM Lite and the Open LLM
Leaderboard7, ρ ∼0.5.
Thus, the results from our monolingual sce-
nario compilation approach differ from those from
English benchmarks while importantly, showing
high correspondence to judgments made by Danish
speakers.
4.2
Model Outcomes
The leading models are familiar, proprietary top
products. Though LlaMa 3 reaches GPT 3.5 level,
Figure 8 shows that most models capable in Danish
do not have openly available weights. Furthermore,
these top performers are generally also large and
instruct-tuned: Quantitatively, models get about ∼
0.5 further Danoliteracy Index points per additional
billion parameters and around ∼15 from instruct-
tuning8.
The substantial requirements of dataset and
model scale as well as creation of instruct datasets
might explain why nationally anchored organiza-
tions have not been able to come up with Danish-
first models competing with the multilingual behe-
moths. Such multilingual models have the advan-
5Here, only 38 open models with known parameter counts
were considered. α = 5% confidence interval: [0.37; 0.78].
6α = 5% confidence interval: [0.6; 0.9]
7This is based on 12 models that overlap between this
benchmark and HELM Lite (α = 5% confidence interval:
[−0.2; 0.8]) and the 15 that overlap with the Open LLM
Leaderboard (α = 5% confidence interval: [0.; 0.8]).
8From fitting a naïve linear model on the results including
only models with known parameter counts, see Appendix D.1

--- Page 7 ---

0
20
40
60
80
100
Closed Weights
Available Weights
>7 B parameters
~7 B parameters
<7 B parameters
Instruct-Tuned
Base Models
Danoliteracy Index for Model Groups
Figure 8: Model Danoliteracy Index for groups of
models. For the models tested in Danish, closed
weights dominate open-weights in a remarkably
clear way. Bigger models are better and on this
benchmark, instruct-tuning is necessary to achieve
high benchmark scores.
tage of linguistic and factual knowledge enhance-
ment across training languages which also benefit
them in the monolingual setting.
4.3
Capability Dimensionality
The previous analysis primarily considered the ag-
gregated benchmark results across scenarios. What
is going on at the scenario level? While different
model capability profiles can be seen, exemplified
in Figure 2 and Figure 3, the main first impres-
sion is that model performance at one benchmark
scenario strongly predicts performance at other sce-
narios: One principal component explains 75% of
the model result variance across the eight scenarios.
This finding leads us to the conclusion that a
"general factor of Danoliteracy" exists. We investi-
gate this further using Exploratory Factor Analysis
(EFA) on the M × N scenario result matrix, ana-
lyzing the underlying result dimensionality: How
many factors are needed to explain the variance
induced by model results over the N scenarios?
This analysis, further detailed in Appendix D.2,
shows a sharp drop in factor eigenvalue when mov-
ing from one to two factors as shown in Figure 9.
1
2
3
4
5
6
7
8
Number of factors
0
1
2
3
4
5
6
Factor Analysis Eigenvalue
Dimensionality of Scenarios
Observed Factors
Parallel Analysis Threshold
Figure 9: Factor Analysis on model results across
eight scenarios reveal one underlying dimension of
Danoliteracy deemed significant by Horn’s Parallel
Analysis.
0.0
0.2
0.4
0.6
0.8
1.0
Loading
Citizenship Test
HyggeSwag
Da. Cloze Self Test
Da. Gym 2000
DaNE
#twitterhjerne
Angry Tweets
Nordjylland News
Scenario Factor 1 ( =5.93)
Figure 10:
The scenarios most contributing to
the underlying signal of Danoliteracy: The fac-
tual multiple-choice evaluation scenario contain-
ing Danish citizenship tests most strongly explains
benchmark performance.
According to both Horn’s Parallel Analysis (Horn,
1965) and the Kaiser Criterion requiring relevant
factors to have λ > 1 (Kaiser, 1960), the resulting
number of significant factors is 1. Loadings for this
factor is shown in Figure 10 suggesting that the
RWK scenarios of HyggeSwag and, importantly,
the Danish culturally aligned Citizenship Test sce-
nario explain the largest part of the dynamics of the
model results.
GLLM capability being consistent across differ-
ent tasks is not just suggested by this benchmark:
Carrying out the same analysis for Scandinavian
and English scenario compilations shows an under-
lying benchmark dimensionality much lower than
scenario count, with significant factor count close
to 1 as seen in Table 1.

--- Page 8 ---

Benchmark
D
σF1
σF2
FK
FPA
Danoliterate
83 × 8
93%
7%
1
1
ScandEval Da.
199 × 8
88%
12%
1
2
ScandEval Full
199 × 24
77%
16%
2
2
HELM Lite
90 × 10
78%
19%
2
2
OpenLLM
2859 × 6
97%
3%
1
2
Table 1:
How much variance did the first and
second factors in EFA explain for the Danoliterate
Benchmark as well as the ScandEval benchmark,
both full and Danish subset (Nielsen, 2023), En-
glish benchmarks HELM Lite (Liang et al., 2022)
and OpenLLM (Beeching et al., 2023) as of January
2025. Leaderboard dimensionality, model count ×
scenario count, is presented along with suggested
significant factor count by the Kaiser criterion and
Parallel Analysis: All benchmarks have an impor-
tant first component.
5
Conclusions
Based on the ability to robustly discover model
groupings at different Danish capability levels and
correlate these rankings with human feedback, we
conclude that a scenario compilation approach can
meaningfully reveal GLLM capabilities. We show
that, in Danish, open-weights GLLMs currently lag
behind large, closed, multilingual, instruct-tuned
models, such as GPT-4 and Claude Opus.
For our evaluation setup, we observe one un-
derlying factor in model capability across the di-
verse test scenarios. This observation is supported
by similar structures in other Danish, English and
multilingual scenario compilations which we con-
sider a positive result for low-resource evaluation:
By using curated and language-specific scenarios,
the general landscape of GLLM capabilities for a
given low-resource language can be meaningfully
inferred even if resources limit the scale.
6
Concerns of the Ethical Impacts
This work releases a benchmark and leaderboard
with the hope of a positive outcome of increased un-
derstanding of potentials and limitations of GLLMs
in Danish. However, we note some risks in the use
of such leaderboards.
The results presented here only focus on model
capability but, on the leaderboard site, versions of
other important dimensions for model applicabil-
ity are presented; such as model efficiency, model
likelihood calibration and model generated output
toxicity. However, these are presented with a dis-
claimer as preliminary results and our work on
other crucial dimensions such as GLLM perfor-
mance fairness across gender and nationalities or
robustness to input noise have not been released
due to limitations to current datasets to robustly
carry out these analyses.
There is an increased risk of bias, fairness and
toxicity violations in low-resource languages to
which models are less tuned.
Problematically,
when the evaluation situation is also low-resource,
these risks might be undiscovered for practitioners
that only focus on a model capability. Further work
is crucially needed but for now, the leaderboard
site displays a disclaimer against blindly trusting
that high benchmark numbers mean predictable
downstream performance or applying GLLMs with
unchecked assumptions about robustness, fairness,
bias, and toxicity.
7
Limitations
The study only focuses on one language, Danish,
with limited comparisons to other language results.
The presented benchmark consists of eight spe-
cific scenarios: Although we find high correlation
between scenario results, all our statements about
model performance on Danish in general are evi-
dently biased by the scenario selection. A similar
statement can be made about prompt and metric de-
sign decisions though these seem robust in ablation
studies in Appendix A.
We stress the importance of the uncertainty quan-
tification for this benchmark where all scenarios
are small-scale, n < 1, 000: The bootstrap analy-
sis revealed some model result differences, such
as Mixtral 8x7B (dM = 54) and Qwen1.5 7B
Chat (dM = 50), are not significant at the de-
sired level and might be spurious. Other differ-
ences such as that between GPT-4 and Claude Opus
might be obscured by the important Citizenship
Test scenario, where these models achieve close
to 100% accuracy (Figure 3), being saturated by
SOTA GLLMs. Though most other scenarios still
show far-from-perfect accuracy, more difficult sce-
narios are needed to accommodate future develop-
ments.
As all evaluation data is publicly available, un-
intentional or malignant dataset contamination is
possible. This issue requires attention but might,
in the short-term, be less of a risk for low-resource
language evaluation with smaller and less widely
published corpora.

--- Page 9 ---

Acknowledgments
We would like to thank all the anonymous review-
ers for the insightful and helpful comments. This
work was supported by the Pioneer Centre for AI,
DNRF grant number P1.
References
Kabir Ahuja, Harshita Diddee, Rishav Hada, Milli-
cent Ochieng, Krithika Ramesh, Prachi Jain, Ak-
shay Nambi, Tanuja Ganu, Sameer Segal, Mohamed
Ahmed, Kalika Bali, and Sunayana Sitaram. 2023.
MEGA: Multilingual evaluation of generative AI.
In Proceedings of the 2023 Conference on Empir-
ical Methods in Natural Language Processing, pages
4232–4267, Singapore. Association for Computa-
tional Linguistics.
Elisabeth Arnbak and Carsten Elbro. 2000. Læsetek-
ster for gymnasium, hf mv. Uddannelsesstyrelsens
Internetpublikationer. Adgang 2000.
Maurice S. Bartlett. 1951. The effect of standardization
on a χ2 approximation in factor analysis. Biometrika,
38(3/4):337–344.
Edward Beeching, Clémentine Fourrier, Nathan Habib,
Sheon Han, Nathan Lambert, Nazneen Rajani, Omar
Sanseviero, Lewis Tunstall, and Thomas Wolf. 2023.
Open llm leaderboard. https://huggingface.co/
spaces/HuggingFaceH4/open_llm_leaderboard.
Yoav Benjamini and Yosef Hochberg. 1995. Control-
ling the false discovery rate: A practical and pow-
erful approach to multiple testing. Journal of the
Royal Statistical Society: Series B (Methodological),
57(1):289–300.
Lukas Biewald. 2020.
Experiment tracking with
weights and biases.
Software available from
wandb.com.
Amalie Brogaard Pauli, Maria Barrett, Ophélie Lacroix,
and Rasmus Hvingelby. 2021. DaNLP: An open-
source toolkit for danish natural language processing.
In Proceedings of the 23rd Nordic Conference on
Computational Linguistics (NoDaLiDa 2021).
Fabian Caba Heilbron, Victor Escorcia, Bernard
Ghanem, and Juan Carlos Niebles. 2015. Activitynet:
A large-scale video benchmark for human activity
understanding. In Proceedings of the IEEE Confer-
ence on Computer Vision and Pattern Recognition,
pages 961–970.
Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anasta-
sios Nikolas Angelopoulos, Tianle Li, Dacheng Li,
Hao Zhang, Banghua Zhu, Michael Jordan, Joseph E.
Gonzalez, and Ion Stoica. 2024. Chatbot arena: An
open platform for evaluating llms by human prefer-
ence.
Kenneth Enevoldsen et al. 2022. dfm-encoder-large-
v1. A Transformer encoder model, part of the BERT
family, intended for Danish natural language tasks.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and Ja-
cob Steinhardt. 2021. Measuring massive multitask
language understanding. In Proceedings of the 9th In-
ternational Conference on Learning Representations
(ICLR).
Matthew Honnibal, Ines Montani, Sofie Van Lan-
deghem, and Adriane Boyd. 2020. spaCy: Industrial-
strength Natural Language Processing in Python.
Software available from spacy.io.
John L. Horn. 1965. A rationale and test for the num-
ber of factors in factor analysis.
Psychometrika,
30(2):179–185.
Rasmus Hvingelby, Amalie Brogaard Pauli, Maria Bar-
rett, Christina Rosted, Lasse Malm Lidegaard, and
Anders Søgaard. 2020. DaNE: A named entity re-
source for Danish. In Proceedings of the 12th Lan-
guage Resources and Evaluation Conference, pages
4597–4604, Marseille, France. European Language
Resources Association.
David Ili´c. 2023. Unveiling the general intelligence
factor in language models: A psychometric approach.
Katrine Lyskov Jensen, Anna Steenberg Gellert, and
Carsten Elbro. 2015. Rapport om udvikling og af-
prøvning af selvtest af læsning – en selvtest af vok-
snes læsefærdigheder på nettet.
Henry F. Kaiser. 1960. The application of electronic
computers to factor analysis. Educational and Psy-
chological Measurement, 20(1):141–151.
Henry F. Kaiser. 1970. A second generation little jiffy.
Psychometrika, 35:401–415.
Oliver Kinch. 2023. Nordjylland news summarization.
Hugging Face Datasets.
Viet Lai, Chien Nguyen, Nghia Ngo, Thuat Nguyen,
Franck Dernoncourt, Ryan Rossi, and Thien Nguyen.
2023. Okapi: Instruction-tuned large language mod-
els in multiple languages with reinforcement learning
from human feedback. In Proceedings of the 2023
Conference on Empirical Methods in Natural Lan-
guage Processing: System Demonstrations, pages
318–327, Singapore. Association for Computational
Linguistics.
Vladimir I. Levenshtein. 1966. Binary codes capable of
correcting deletions, insertions, and reversals. Soviet
Physics Doklady, 10(8):707–710.
Quentin Lhoest, Albert Villanova del Moral, Yacine
Jernite, Abhishek Thakur, Patrick von Platen, Suraj
Patil, Julien Chaumond, Mariama Drame, Julien Plu,
Lewis Tunstall, Joe Davison, Mario Šaško, Gun-
jan Chhablani, Bhavitvya Malik, Simon Brandeis,
Teven Le Scao, Victor Sanh, Canwen Xu, Nicolas

--- Page 10 ---

Patry, Angelina McMillan-Major, Philipp Schmid,
Sylvain Gugger, Clément Delangue, Théo Matus-
sière, Lysandre Debut, Stas Bekman, Pierric Cis-
tac, Thibault Goehringer, Victor Mustar, François
Lagunas, Alexander Rush, and Thomas Wolf. 2021.
Datasets: A community library for natural language
processing. In Proceedings of the 2021 Conference
on Empirical Methods in Natural Language Process-
ing: System Demonstrations, pages 175–184, Online
and Punta Cana, Dominican Republic. Association
for Computational Linguistics.
Percy Liang, Rishi Bommasani, Tony Lee, Dimitris
Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian
Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Ku-
mar, Benjamin Newman, Binhang Yuan, Bobby Yan,
Ce Zhang, Christian Cosgrove, Christopher D. Man-
ning, Christopher Ré, Diana Acosta-Navas, Drew A.
Hudson, Eric Zelikman, Esin Durmus, Faisal Lad-
hak, Frieda Rong, Hongyu Ren, Huaxiu Yao, Jue
Wang, Keshav Santhanam, Laurel Orr, Lucia Zheng,
Mert Yuksekgonul, Mirac Suzgun, Nathan Kim,
Neel Guha, Niladri Chatterji, Omar Khattab, Peter
Henderson, Qian Huang, Ryan Chi, Sang Michael
Xie, Shibani Santurkar, Surya Ganguli, Tatsunori
Hashimoto, Thomas Icard, Tianyi Zhang, Vishrav
Chaudhary, William Wang, Xuechen Li, Yifan Mai,
Yuhui Zhang, and Yuta Koreeda. 2022. Holistic eval-
uation of language models.
Percy Liang, Yifan Mai, Josselin Somerville, Farzaan
Kaiyom, Tony Lee, and Rishi Bommasani. 2023.
HELM Lite: Lightweight and broad capabilities eval-
uation.
Chin-Yew Lin. 2004. ROUGE: A package for auto-
matic evaluation of summaries. In Text Summariza-
tion Branches Out, pages 74–81, Barcelona, Spain.
Association for Computational Linguistics.
Peng Liu, Lemei Zhang, Terje Nissen Farup, Even W.
Lauvrak, Jon Espen Ingvaldsen, Simen Eide, Jon Atle
Gulla, and Zhirong Yang. 2023. Nlebench+norglm:
A comprehensive empirical analysis and benchmark
dataset for generative language models in norwegian.
Samuel R. Mathias. 2024. Horns: Horn’s parallel analy-
sis in python. https://github.com/sammosummo/
Horns.
Hiroki Nakayama. 2018. seqeval: A python framework
for sequence labeling evaluation. Software available
from https://github.com/chakki-works/seqeval.
Dan Nielsen. 2023. ScandEval: A benchmark for Scan-
dinavian natural language processing. In Proceed-
ings of the 24th Nordic Conference on Computational
Linguistics (NoDaLiDa), pages 185–201, Tórshavn,
Faroe Islands. University of Tartu Library.
Jesper Olsen. 2023. Hvor taler du flot dansk! selv
skaberne er forbløffede over chatbottens sprogøre.
OpenAI. 2023. evals. https://github.com/openai/
evals. Accessed: 2023-11-22.
siri.dk. 2023.
Danskundervisning og prøver for
udlændinge.
Charles Spearman. 1904. "General Intelligence," Ob-
jectively Determined and Measured. The American
Journal of Psychology, 15(2):201–292.
Alex Wang, Amanpreet Singh, Julian Michael, Felix
Hill, Omer Levy, and Samuel Bowman. 2018. GLUE:
A multi-task benchmark and analysis platform for nat-
ural language understanding. In Proceedings of the
2018 EMNLP Workshop BlackboxNLP: Analyzing
and Interpreting Neural Networks for NLP, pages
353–355, Brussels, Belgium. Association for Com-
putational Linguistics.
Shuhe Wang, Xiaofei Sun, Xiaoya Li, Rongbin Ouyang,
Fei Wu, Tianwei Zhang, Jiwei Li, and Guoyin Wang.
2023. Gpt-ner: Named entity recognition via large
language models.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien
Chaumond, Clement Delangue, Anthony Moi, Pier-
ric Cistac, Tim Rault, Rémi Louf, Morgan Funtow-
icz, Joe Davison, Sam Shleifer, Patrick von Platen,
Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu,
Teven Le Scao, Sylvain Gugger, Mariama Drame,
Quentin Lhoest, and Alexander M. Rush. 2019.
Transformers:
State-of-the-art natural language
processing. https://github.com/huggingface/
transformers. Hugging Face, Brooklyn, USA.
Omry Yadan. 2019. Hydra - a framework for elegantly
configuring complex applications. Github.
Marc Zao-Sanders. 2024. How people are really using
genai. Harvard Business Review. Technology and
analytics.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. HellaSwag: Can a ma-
chine really finish your sentence? In Proceedings of
the 57th Annual Meeting of the Association for Com-
putational Linguistics, pages 4791–4800, Florence,
Italy. Association for Computational Linguistics.
Tianyi Zhang*, Varsha Kishore*, Felix Wu*, Kilian Q.
Weinberger, and Yoav Artzi. 2020. Bertscore: Eval-
uating text generation with bert. In International
Conference on Learning Representations.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric. P Xing, Hao Zhang,
Joseph E. Gonzalez, and Ion Stoica. 2023. Judging
llm-as-a-judge with mt-bench and chatbot arena.
Banghua Zhu, Evan Frick, Tianhao Wu, Hanlin Zhu,
Karthik Ganesan, Wei-Lin Chiang, Jian Zhang, and
Jiantao Jiao. 2023. Starling-7b: Improving llm help-
fulness and harmlessness with rlaif.

--- Page 11 ---

A
Evaluation Methodology
A.1
Prompting
An example of a prompt following the structure
shown in Figure 4 is the Citizenship Test example
shown in Figure 11.
1
Svar kun med tallet for den rigtige
mulighed.
2
# SPØRGSMÅL
3
Hvilket af følgende lande har flest
indvandrere og efterkommere i
Danmark oprindelse i?
4
# SVARMULIGHEDER
5
1. Pakistan
6
2. Iran
7
3. Tyrkiet
8
# SVAR
9
Svaret er mulighed nummer
Figure 11:
Prompting of an example from the
Citizenship Test scenario. Translated, this question
prompt reads: Answer only with the number cor-
responding to the correct answer. # QUESTION
From which of the following countries do the high-
est number of immigrants and descendants in Dan-
mark have their roots? # OPTIONS 1. Pakistan 2.
Iran 3. Turkey # ANSWER The answer is option
number.
Alternatives
Some prompt alternatives to the ap-
proach shown in Figures 4 and 11 were run for a
subset of GLLMs: For the Citizenship Test sce-
nario, Table 2, results were similar when not pre-
senting options to the models, instead parsing their
output choice by selecting the option with highest
similarity to their generation. The same table sug-
gests that changing the Citizenship Test scenario
to a simpler prompt without markdown headers
lowered results minimally..
For the summarization task, Nordjylland News,
an alternative prompt with longer and more detailed
instructions had no effect on model results shown
in Table 3.
Translating all instruction text in the prompt for-
mat while keeping data content in Danish main-
tained or improved non-Danish model results, Ta-
ble 4 on the Gym 2000 scenario.
A.2
GLLM Output Parsing
Multiple-choice
A numbered option was consid-
ered selected if it was the only number generated
by the model. In the case of multiple generated
option numbers, the most frequent number was
Std.
Simple Q
No opt.
Gemini Pro
85 ± 1
78 ± 1
79 ± 1
GPT 3.5 Turbo
82 ± 1
77 ± 1
82 ± 1
Mistral 7B Instruct
47 ± 2
50 ± 2
49 ± 2
Mistral 7B
45 ± 2
44 ± 2
41 ± 2
Dano. Mistral 7B
43 ± 2
45 ± 2
59 ± 2
LlaMa 2 7B
39 ± 2
42 ± 2
36 ± 2
Dano. LlaMa 2 7B
37 ± 2
40 ± 2
Dummy Baseline
36 ± 2
36 ± 2
36 ± 2
Table 2:
Alternative prompting and scoring ap-
proaches to the Citizenship Test run for a subset
of models including a baseline outputting a fixed,
random string and Danish-tuned versions of base
GLLMs. Std. is the prompt version presented in the
benchmark, Figure 11, Simple Q removes the first
instruction and the markdown headers, simply pre-
senting the question, the options and the final text.
No opt. asks the question openly without multiple-
choice options, choosing argmax similarity score,
as in Section 3.2, as model choice. Presented with
95% Wald confidence interval.
Std.
Detailed
Gemini Pro
74 ± 2
74 ± 2
GPT 3.5 Turbo
73 ± 2
74 ± 2
Mistral 7B Instruct (v0.2)
70 ± 2
71 ± 2
Mistral 7B
62 ± 3
58 ± 3
Dano. Mistral 7B
57 ± 3
59 ± 3
Dano. LlaMa 2 7B
52 ± 3
58 ± 3
LlaMa 2 7B
54 ± 3
56 ± 3
Dummy Baseline
43 ± 3
43 ± 3
Table 3: Impact of Nordjylland News alternative
prompting.
chosen. Maximum generation likelihood-based se-
lection was also implemented and is available for
open-weights models on the frontend leaderboard
but is not presented here.
GPT-NER
Following (Wang et al., 2023), for
each example, the GLLM was prompted four times,
once for each entity category in the DaNE dataset
(Hvingelby et al., 2020). The model was instructed
to mark all words belonging to this entity cate-
gory with @. These were parsed to one, multi-class
prediction, handling overlap by selecting the gener-
ation with highest likelihood for models exposing
probabilities. To mitigate small errors resulting in
catastrophic results, model output annotated words
were aligned using Levenshtein matching to the
input example word list (Levenshtein, 1966).

--- Page 12 ---

Std.
English
Gemini Pro
61 ± 8
64 ± 8
GPT 3.5 Turbo
45 ± 9
52 ± 9
Danoliterate Mistral 7B
48 ± 9
36 ± 8
Mistral 7B
39 ± 8
45 ± 9
Mistral 7B Instruct (v0.2)
36 ± 8
42 ± 9
LlaMa 2 7B
33 ± 8
33 ± 8
Danoliterate LlaMa 2 7B
27 ± 7
30 ± 7
Dummy Baseline
21 ± 6
21 ± 6
Table 4: How the Gym 2000 results change if the
prompt instructions are in English. The instruct-
tuned models handle this strongly while the Dano-
literate Mistral model fails to to perform under
English prompting.
A.3
Metrics
Differences in results for the similarity-based met-
rics used for #twitterhjerne and Nordjylland News
summarization are presented in Tables 5 and 6.
Model rank is minimally changed.
Odd-
one-
out
Avg.
sim.
Min.
sim.
Max.
sim.
GPT 3.5 Turbo
29 ± 5 64 ± 5 61 ± 5 66 ± 5
Gemini Pro
31 ± 5 63 ± 5 61 ± 5 66 ± 5
GPT 4
35 ± 5 63 ± 5 61 ± 5 66 ± 5
SOLAR 10.7B Instruct
50 ±
6
62 ±
5
60 ±
5
65 ±
5
LlaMa 2 13B Chat
60 ±
5
61 ±
5
58 ±
5
63 ±
5
Mistral 7B Instruct
64 ±
5
62 ±
5
59 ±
5
64 ±
5
Dano. Mistral 7B
96 ±
1
54 ±
6
52 ±
6
57 ±
6
Dano. LlaMa 2 7B
97 ±
1
53 ±
6
50 ±
6
55 ±
6
OpenAI Davinci 002
99 ±
0.3
52 ±
6
49 ±
6
54 ±
6
LlaMa 2 7B
100
51 ±
6
49 ±
6
53 ±
6
Mistral 7B
99 ±
0.3
50 ±
6
48 ±
6
52 ±
6
Dummy Baseline
100
44 ±
6
43 ±
6
46 ±
6
Table 5: Standard version of #twitterhjerne using
the odd-one-out metric (1) compared to a simpler
metric just reporting average similarity score.
A.4
Software Dependencies
The relevant Python packages and their versions
are presented in Table 7. Python version 3.11.8 was
used.
BERT
similar-
ity
ROUGE-
1
ROUGE-
L
Gemini Pro
74 ± 2
35 ± 3
28 ± 2
GPT 3.5 Turbo
73 ± 2
32 ± 2
25 ± 2
GPT 4
73 ± 2
32 ± 2
23 ± 2
SOLAR 10.7B Instruct
71 ± 2
28 ± 2
20 ± 2
Mistral 7B Instruct
70 ± 2
25 ± 2
18 ± 2
LlaMa 2 13B Chat
69 ± 2
17 ± 2
12 ± 1
Mistral 7B
62 ± 3
16 ± 1
12 ± 1
Dano. Mistral 7B
57 ± 3
11 ± 1
8 ± 1
OpenAI Davinci 002
55 ± 3
9 ± 1
7 ± 1
Dummy Baseline
43 ± 3
11 ± 1
8 ± 1
LlaMa 2 7B
54 ± 3
6 ± 1
5 ± 1
Dano. LlaMa 2 7B
52 ± 3
5 ± 1
4 ± 0.5
Table 6: Nordjylland News summarization results
presented with an alternative lemma-based similar-
ity score. The score is computed by lemmatizing
text using the SpaCy framework (Honnibal et al.,
2020) and then computing the ROUGE score (Lin,
2004)
.
Library
Version
google-cloud-aiplatform
1.38.1
openai
0.28.1
anthropic
0.21.3
groq
0.4.2
pandas
1.5.3
datasets
2.14.5
transformers
4.36.1
torch
2.1.1
evaluate
0.4.0
rouge_score
0.1.2
bert_score
0.3.13
huggingface_hub
0.19.4
hydra-core
1.3.2
Table 7: Evaluation framework Python dependen-
cies and used versions.
B
Evaluation Corpora Details
B.1
Data Permissions
1. Citizenship
Test:
All
rights
reserved
”Styrelsen for International Rekruttering og
Integration”. Written permission was given
for the data to be re-released as an appendix
to Academic work.
2. HyggeSwag: MIT.
3. Gym 2000: Unreleased. Written permission
was given by CRR for Academic use but not
for re-releasing the dataset.
4. #twitterhjerne: CC-By-4.0.
5. Nordjylland News: CC-0-1.0.

--- Page 13 ---

6. Cloze Self Test: Unreleased. Written permis-
sion was given by CRR for Academic use but
not for re-releasing the dataset.
7. DaNE: CC-By-Sa-4.0-
8. Angry Tweets: CC-By-4.0.
B.2
Data Content
All novel datasets were manually inspected for of-
fensive content. Some crime-related and sexual
themes were found in Nordjylland News exam-
ples but deemed unproblematic. The #twitterhjerne
dataset was manually anonymized, removing all
examples with personally identifiable content.
B.3
Examples
Below, one prompted example per evaluation cor-
pus is presented.
1. Citizenship Test: See Figure 4.
2. HyggeSwag
1
Svar kun med tallet for den
rigtige fortsættelse af
sætningen
2
# SÆTNING
3
En gruppe venner sidder på
slæder på toppen af bakken.
De to venner
4
# SVARMULIGHEDER
5
1. er udstyr kørende ned ad
bakken med en udstyrsrem på.
6
2. presser deres rygge op mod en
klippe.
7
3. skubber en slæde med et reb,
da hele bakken er dækket
med sne.
8
4. skubbes ned ad bakken, og de
glider til bunden.
9
# SVAR
10
Den rigtige fortsættelse er
mulighed nummer
3. #twitterhjerne
1
Skriv et kort tweet på dansk,
der besvarer nedenstående
spørgsmål. Svar kun med
tweetet.
2
# TWEET MED SPØRGSMÅL
3
Sønnen vil gerne lave
#pebernødder. De par gange
jeg har prøvet det, blev de
kun OK. Er der nogen, der
kan anbefale en opskrift?
#twitterhjerne
4
# TWEET MED SVAR
5
Et svar kunne være:
4. Gym 2000
1
"Selv før jeg lærte Max Kelada
at kende, var jeg
indstillet på ikke at kunne
lide ham. Krigen var lige
blevet afsluttet, og
passagertrafikken på de
store oceandampere var
livlig. Det var meget
vanskeligt at få plads, og
man måtte finde sig i at
tage, hvad skibsagenterne
tilbød én. Man kunne ikke
vente at få en kahyt for
sig selv, og jeg var
temmelig taknemmelig over
at få en, hvor der kun var
to køjer. Men da jeg
erfarede navnet på min
medpassager, sank mit
humør. Det betød lukkede
koøjer, så det ikke ville
være muligt at få den
mindste smule frisk luft om
natten. Det var ubehageligt
nok at dele kahyt i fjorten
dage med hvem som helst
(jeg rejste fra San
Francisco til Yokohama),
men jeg ville have været
mindre bekymret ved tanken,
hvis min medpassagers navn
havde været Smith eller
Brown."
2
3
Svar kun med tallet for den
rigtige mulighed
4
# SPØRGSMÅL
5
Hvorfor var det svært at få en
kahyt for sig selv?
6
# SVARMULIGHEDER
7
1. Det var moderne at tage på
krydstogt.
8
2. Det var midt i ferieperioden
9
3. Mange mennesker flyttede til
USA
10
4. Krigen var lige forbi.
11
# SVAR
12
Svaret er mulighed nummer
5. Cloze Self Test
1
"Henrik bladede frem til siderne
med boligannoncer. Deres
lejlighed var <MASK> for
lille til dem, så nu ledte
de efter noget større. De
ville gerne flytte lidt
tættere på kysten. De ledte
efter en lille gård , hvor
der var plads til at holde
et par heste ."
2
Erstat det maskerede ord i
ovenstående tekst (markeret
med '<MASK>') med et af
følgende ord: indrettet,
solgt, annonceret, blevet.
Svar *kun* med det rigtige
ord:
6. Nordjylland News
1
Skriv et kort dansk resumé på én
enkelt sætning af følgende
tekst.

--- Page 14 ---

2
# TEKST
3
Manden kom kørende på Sønder
Havnevej ved kiosken på
havnen i Aalbæk, da han
påkørte flere afmærkninger
på stedet og fortsatte
direkte ind i den bygning,
hvor kiosken holder til.
Der skete i forbindelse med
påkørslen skade på
bygningen. Uden for sad en
mand, og han blev i lav
fart påkørt af bilen ført
af 53-årig mand. Den
uheldige kiosk-gæst blev
kørt til sygehuset med
lettere skader.
Nordjyllands Politi
oplyser, at den 53-årige
blev anholdt og sigtet for
at køre i spirituspåvirket
tilstand. Han er efter endt
afhøring løsladt igen.
4
# RESUMÉ
5
Et resumé på en sætning er:
7. Angry Tweets
1
Vurdér, om sentimentet i
følgende tweet er
'positiv', 'neutral' eller
'negativ'. Svar kun med et
enkelt ord.
2
# TWEET
3
@USER Klæk det æg!
4
# SENTIMENT:
5
Sentimentet var
8. DaNE (prompting for location)
1
Fuldfør annotering af sidste
eksempel i opgaven.
2
Her er en lingvists arbejde med
at annotere entiteter af
typen 'lokation'.
3
# TEKST
4
Det blev naboens store, sorte
hund også, "siger
Københavns politidirektør,
Poul Eefsen,
galgenhumoristisk til B.T.
efter et stort smykkekup i
hans Holte-villa og en
række tilsvarende kup i
området.
5
# ANNOTERING
6
Det blev naboens store , sorte
hund også , " siger
@@Københavns##
politidirektør , Poul
Eefsen , galgenhumoristisk
til B.T. efter et stort
smykkekup i hans
Holte-villa og en række
tilsvarende kup i området .
7
# TEKST
8
Diskussionen om forklaringen på
det "japanske økonomiske
mirakel" har især drejet
sig om, hvorvidt man kunne
nøjes med økonomiske
faktorer i sin forklaring,
eller om det også er
nødvendigt at inddrage
særlige kulturelle og
historiske forhold for at
finde en rimelig forklaring.
9
# ANNOTERING
10
Diskussionen om forklaringen på
det " japanske økonomiske
mirakel " har især drejet
sig om , hvorvidt man kunne
nøjes med økonomiske
faktorer i sin forklaring ,
eller om det også er
nødvendigt at inddrage
særlige kulturelle og
historiske forhold for at
finde en rimelig forklaring
.
11
# TEKST
12
De lyssky fremmede elementer af
enhver art, der har sneget
sig til landet, er fjenden.
13
# ANNOTERING
14
De lyssky fremmede elementer af
enhver art , der har sneget
sig til landet , er fjenden
.
15
16
# TEKST
17
"Vi tar'en tysker frem, vi
tar'en tysker tilbage, vi
tar'en tysker frem, åååårrr
så ryster vi ham lidt!"
18
# ANNOTERING
C
Survey
C.1
Survey Design and Instructions
For 100 GLLM use-cases divided into six cat-
egories (Zao-Sanders, 2024), we translated use-
cases and categories into Danish and crafted an
example prompt in Danish corresponding to that
theme. We saved model answers from 18 mod-
els andf used them in the survey to allow interac-
tiveness without requiring infrastructure for true
dynamic model responses.
The survey front-end allowed volunteers to pick
between the 100 prompts separated into categories,
seeing model outputs from ”Model A” and ”Model
B” side-by-side, streamed with a delay of 0.1 sec-
onds between each word to simulate model genera-
tion. The volunteer was then instructed to try out at
least a total of three prompts before answering. The
answer consists of a question of preference, with
optional additional Likert scales for each model
and a text field for more details. The user instruc-
tion was in Danish meant Two models have now
been secretly selected for you: Model A and Model
B. Test them out by choosing a prompt under a
category that interests you. Look at the models’
responses and get an impression of both A and B.
Now choose a new prompt and please provide your

--- Page 15 ---

Figure 12: A screenshot of the survey UI presented
to users. Under header 1, users select prompts of
their interest. Header 2 contains model answers
side-by-side and in header 3, volunteers fill in their
preference and can get model identities revealed
and move on to another pair.
assessment after at least 3 prompts.9. See Figure
12 for an overview of the A/B test user interface.
C.2
Volunteers
The survey is openly available online, inviting users
to voluntarily try out the A/B tests, filling out their
preferences. The survey was promoted on social
media networks and newsletters. Most of the pro-
motions were made on channels for AI enthusiasts
or professionals. Volunteers were made aware that
the data would contrubute to studies into GLLM
evaluation in Danish.
Volunteers could optionally fill in demographic
details before carrying out A/B test which is shown
in Figure 13 suggesting a bias towards young, male
AI professionals.
9Da.: Nu er der i hemmelighed valgt to modeller for dig:
Model A og Model B. Afprøv dem ved at vælge en prompt
under en kategori, der interesserer dig. Se modellernes svar
og få et indtryk af både A og B. Vælg nu en ny prompt og giv
endelig din vurdering efter mindst 3 prompts.
       N/A
Female
Male
0
50
100
150
200
Density
3%
29%
68%
Gender Distribution
15-20
21-34
35-49
50-64
65+
0
50
100
150
200
Count
7%
39%
27%
20%
3%
Age Group Distribution
       N/A
 Another Language
 Danish
0
50
100
150
200
Count
4%
4%
92%
1st Language Distribution
       N/A
     None
    Lesser
   Greater
  Professional
0
50
100
150
200
Count
4%
6%
35%
19%
37%
User Experience Distribution
Figure 13: Demographic details filled out by survey
volunteers.
Work is ongoing to increase scale and diversity
of respondents.
C.3
Ranking Model
All 18 models included in the survey were sam-
pled uniformly and the user model preference was
used for ranking. An initial version ranking is the
model win frequency presented in Table 8. As a
model for the human preferences, we follow Chi-
ang et al. to employ the Bradley-Terry model in
a non-parametric fashion, using the sandwich ro-
bust standard errors (Chiang et al., 2024, Sec. 4,
Sec. 5, Appendix B). The approach produces a
linear model coefficient per model with estimated
standard errors. These can be used for a paired
Wilk’s test to present significance of differences at
α = 0.05 level.
D
Analysis Methodology Details
D.1
Model Outcomes Linear Model
The model
dm = β0 + β1pM + β2I(M ∈instruct) + ε, (2)
where ε ∼N(0, σ2) and pm is the number of
model parameters in billions, was fitted with re-
sults shown in Table 9.
D.2
Factor Analysis
For the EFA on the 83 × 8 scenario results, the
Bartlett Sphericity (Bartlett, 1951) p value is

--- Page 16 ---

Lower
Estimate
Upper
Claude Opus
87%
94%
100%
Claude Sonnet
65%
76%
89%
GPT 4o
65%
76%
88%
Gemini Pro
59%
71%
85%
Claude Haiku
59%
71%
83%
GPT 4 Turbo 2024-04-09
55%
67%
80%
Starling 7B
53%
65%
81%
GPT 3.5 Turbo
48%
61%
72%
Heidrun 7B Chat
35%
48%
61%
Gemma 7B In.
29%
44%
60%
Mixtral 8x7B
24%
40%
56%
LlaMa 3 70B
24%
40%
53%
LlaMa 3 8B In.
19%
32%
44%
SOLAR 10.7B In.
17%
29%
41%
Munin NeuralBeagle
13%
26%
39%
Qwen1.5 7B Chat
11%
22%
33%
Mistral 7B In. v0.2
9%
20%
30%
DanskGPT-tiny Chat
6%
18%
29%
Table 8: How frequently each model wins their
A/B tests with uncertainty estimation to a 95% con-
fidence interval from bootstrapping blocked per
volunteer.
Parameter
Value
Std. error
t-value
ˆβ0
17 2
8
ˆβ1
15
3
5
ˆβ2
0.4
0.01
4
ˆσ
9
Table 9: Linear model fitted with ˆR2 = 0.6 to the
Danoliteracy Index for 38 open-weights models
with known parameter counts.
< 2 · 10−16 and the Kaiser-Meyer-Olkin Test
(Kaiser, 1970) yields a variance proportion of
90%, both suggesting that the data is usable
for EFA. Fitting an EFA using the Scikit-learn
Factor Analysis model yields λ1 = 5.9, λ2 = 0.3.
Explained factor variance is calculated as eigen-
value proportion of summed eigenvalues, and the
analysis is repeated for scenario results acquired
from the open API at scandeval.com/danish-nlg/, at
crfm.stanford.edu/helm/lite/v1.3.0/#/leaderboard,
and using the OpenLLM Leaderboard Scraper
GitHub project10. The datasets updated to most
recent versions on January 13th, 2025.
All datasets were subjected Horn’s Parallel Anal-
ysis (Horn, 1965) simulating 1000 datasets of
same shape but without correlation structure: This
was implemented using the Python package horns
(Mathias, 2024).
10github.com/Weyaxi/scrape-open-llm-leaderboard

```
