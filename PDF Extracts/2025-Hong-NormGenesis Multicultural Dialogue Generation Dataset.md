---
title: "2025-Hong-NormGenesis Multicultural Dialogue Generation Dataset - PDF Extract"
source_pdf: "2025-Hong-NormGenesis Multicultural Dialogue Generation Dataset.pdf"
pages: 39
extracted_at: "2026-02-07T17:00:46.588651"
---

# PDF Extract: 2025-Hong-NormGenesis Multicultural Dialogue Generation Dataset

**Source PDF:** 2025-Hong-NormGenesis Multicultural Dialogue Generation Dataset.pdf
**Total Pages:** 39

---

## Content

```
--- Page 1 ---

NormGenesis: Multicultural Dialogue Generation via Exemplar-Guided
Social Norm Modeling and Violation Recovery
Minki Hong1 and Jangho Choi1 and Jihie Kim1*
1Department of Computer Science and Artificial Intelligence, Dongguk University
{jackyh1, 2025120382}@dgu.ac.kr, jihie.kim@dgu.edu
Abstract
Social norms govern culturally appropriate be-
havior in communication, enabling dialogue
systems to produce responses that are not only
coherent but also socially acceptable.
We
present NormGenesis, a multicultural frame-
work for generating and annotating socially
grounded dialogues across English, Chinese,
and Korean. To model the dynamics of social
interaction beyond static norm classification,
we propose a novel dialogue type, Violation-
to-Resolution (V2R), which models the pro-
gression of conversations following norm vi-
olations through recognition and socially ap-
propriate repair. To improve pragmatic consis-
tency in underrepresented languages, we im-
plement an exemplar-based iterative refinement
early in the dialogue synthesis process. This de-
sign introduces alignment with linguistic, emo-
tional, and sociocultural expectations before
full dialogue generation begins. Using this
framework, we construct a dataset of 10,800
multi-turn dialogues annotated at the turn level
for norm adherence, speaker intent, and emo-
tional response. Human and LLM-based eval-
uations demonstrate that NormGenesis signifi-
cantly outperforms existing datasets in refine-
ment quality, dialogue naturalness, and gen-
eralization performance. We show that mod-
els trained on our V2R-augmented data ex-
hibit improved pragmatic competence in ethi-
cally sensitive contexts. Our work establishes a
new benchmark for culturally adaptive dialogue
modeling and provides a scalable methodology
for norm-aware generation across linguistically
and culturally diverse languages.
1
Introduction
Social norms are culturally defined expectations
that guide appropriate behavior in specific con-
texts (Elster, 2006; Malle et al., 2014). In human
communication, social norms support politeness,
* Corresponding author: jihie.kim@dgu.edu
Figure 1: Comparison of generation outputs in Korean.
Prior methods (Li et al., 2023) produce pragmatically
inconsistent responses, including honorific misuse and
unnatural tone (highlighted in red). In contrast, our
framework yields culturally and pragmatically coherent
outputs (highlighted in blue).
empathy, and social harmony. For dialogue sys-
tems, aligning with social norms enables responses
that transcend syntactic correctness or task comple-
tion, contributing to pragmatic and interpersonal
appropriateness (Kim et al., 2022). As conversa-
tional agents are increasingly deployed in socially
embedded and open-domain settings, the ability
to recognize and adhere to cultural norms has be-
come a critical indicator of social and pragmatic
competence (Zhan et al., 2023).
Recent studies have integrated social norms into
arXiv:2509.18395v1  [cs.CL]  22 Sep 2025

--- Page 2 ---

dialogue datasets and language models.
Prior
works have explored moral reasoning in language
models (Forbes et al., 2020), norm-based label-
ing (Li et al., 2023), emotion-informed norm in-
terpretation (Zhan et al., 2024), and cross-cultural
generalization (Rao et al., 2025). While these ef-
forts lay foundational groundwork for norm-aware
generation, they primarily focus on English, a high-
resource language. Although Chinese has received
growing attention, the modeling of culturally appro-
priate behavior remains underdeveloped for low-
resource languages. This limitation is especially
pronounced in Korean, where existing models fre-
quently exhibit inconsistencies in honorific usage,
inadequate emotional alignment, and misrepresen-
tation of role-based social dynamics (Jang et al.,
2024; Lee et al., 2024), as illustrated in Figure 1.
To address the cultural and pragmatic limitations
of existing dialogue datasets, we present a multicul-
tural framework for generating and refining socially
grounded dialogues across English, Chinese, and
Korean. While English benefits from extensive data
and modeling maturity, low-resource languages
generation remains challenged by pragmatic mis-
matches, especially in tone and formality (Zhong
et al., 2024). We mitigate this gap through an
exemplar-based iterative refinement strategy. Given
a target scenario, the system retrieves semantically
and structurally aligned exemplars, using features
such as intent, emotional tone, and discourse pat-
terns (e.g., speaker roles and adjacency). These ex-
emplars guide revision to ensure cultural alignment
without requiring large-scale human annotation.
We further introduce a novel dialogue category,
Violation-to-Resolution (V2R), which captures how
speakers recover from norm violations through con-
textually appropriate repair. This enables the mod-
eling of pragmatically dynamic interactions that
reflect both norm compliance and social recovery
mechanisms. Leveraging our framework, we con-
struct a dataset of 10,800 high-quality dialogues
annotated at the turn level with norm adherence,
violation, speaker intent, and emotional response,
grounded in dialogue act theory (Bunt et al., 2020).
We evaluate our approach through both human and
LLM-based assessments of refinement quality, di-
alogue fluency, social appropriateness, and gener-
alization. Experimental results show that models
trained on our data significantly outperform exist-
ing baselines in socially complex and emotionally
sensitive scenarios. These findings demonstrate the
efficacy of our framework for enabling culturally
adaptive dialogue generation across typologically
diverse languages.
Our main contributions are as follows:
1. We present a multicultural framework for
generating socially grounded dialogues in
English, Chinese, and Korean. To address
cultural and pragmatic degradation in low-
resource settings, we propose an exemplar-
based iterative refinement strategy using se-
mantically relevant exemplars.
2. We propose a novel dialogue type, Violation-
to-Resolution (V2R), that models how norm
violations are followed by socially appropriate
repair, enabling the representation of dynamic
and culturally meaningful interaction patterns.
3. We construct a dataset of 10,800 multicultural
dialogues with turn-level annotations for norm
adherence, speaker intent, and emotional re-
sponse, grounded in dialogue act theory.
4. We show that models trained on our dataset
outperform prior resources in norm alignment,
emotional coherence, and repair, as confirmed
by both human and automatic evaluations.
2
Related Work
2.1
Social Norms in Dialogue Systems
Integrating social norms into dialogue systems is
critical for generating contextually appropriate and
socially coherent responses. Early work (Forbes
et al., 2020) provided normative signals via moral
judgments but lacked dialogue structure. Later ef-
forts (Li et al., 2023) added norm annotations to
multi-turn dialogues, focusing on adherence classi-
fication without modeling responses to violations.
Recent work (Zhan et al., 2024) has begun model-
ing norm repair in dialogue. However, it remains
monolingual and lacks fine-grained annotations
capturing speaker intent and emotional response.
To bridge this gap, we introduce Violation-to-
Resolution as a distinct response type, capturing
repair strategies such as apology and explanation.
Also, our framework supports this with turn-level
annotations of communicative intent and emotional
state, enabling more nuanced and socially compe-
tent generation.

--- Page 3 ---

Figure 2: NormGenesis Overview. Our framework consists of four stages: (1) culturally grounded norm and style
design, (2) scenario–situation construction across norm adherence, violation, and resolution types, (3) exemplar-
based iterative refinement using semantically aligned exemplars, and (4) multi-turn dialogue generation with
turn-level annotations. Each stage is evaluated and refined iteratively to ensure pragmatic consistency and cultural
alignment, as described in Section 3. The RQ evaluation protocol is described in Section 4.2.
2.2
Prompt-Based and Exemplar-Guided
Generation
The emergence of LLMs has enabled prompt-based
synthetic data generation through techniques such
as in-context learning and prompt tuning. While ef-
fective in high-resource settings, these methods of-
ten fail to capture cultural and emotional nuance in
low-resource languages (Cahyawijaya et al., 2024;
Pranida et al., 2025). Recent approaches (Nguyen
et al., 2024; Ghosal et al., 2025) explore exemplar-
based generation, but typically rely on fixed ex-
amples and prioritizes fluency over pragmatic fit.
SADAS (Hua et al., 2024) also investigated norm
interventions through exemplar-based remediation.
However, it applies these exemplars reactively after
violations occur in negotiation dialogues, remain-
ing limited to post-hoc repair.
To address these limitations, we propose an
exemplar-based iterative refinement strategy. Un-
like few-shot prompting, which uses static exem-
plars at inference time, our method dynamically
selects semantically and structurally relevant exam-
ples to guide generation. This process improves
linguistic coherence and cultural alignment while
enabling data bootstrapping without large-scale hu-
man annotation, particularly in low-resource lan-
guages such as Korean.
2.3
Culturally Adaptive Dialogue
As conversational AI systems expand to diverse
cultural contexts, cultural adaptability becomes
essential.
Early multilingual datasets, such as
BITOD(Lin et al., 2021) and MULTI3WOZ(Hu
et al., 2023), introduced bilingual dialogues but
lacked cultural annotations and failed to capture
pragmatic nuance due to reliance on translation.
Recent works, including CARE(Guo et al., 2025)
and CULTUREPARK(Li et al., 2024), incorporate
cultural preferences and simulates cross-cultural
interactions with LLMs. However, these resources
focus on high-resource languages and lack the fine-
grained, turn-level annotations needed for cultur-
ally appropriate generation.
This gap is pronounced in underrepresented lan-
guages like Korean, where honorifics and relational
pragmatics are central. To address this, we propose
a multicultural framework with language-specific
subnorms and turn-level annotations.
Using
exemplar-based iterative refinement, our method
enhances cultural and pragmatic consistency, par-
ticularly in low-resource settings.
3
Method
We introduce NormGenesis, a multicultural frame-
work for generating and refining socially grounded

--- Page 4 ---

Apology
Compliment
Condolence
Criticism
Empathy
Greeting
Leave-taking
Persuasion
Request
Respect
Responding to Compliments
Thanks
Table 1: Social norm categories used in this study.
dialogues in American English, Chinese, and Ko-
rean.
While we broadly refer to "English" in
our framework, it is important to clarify that the
dataset primarily reflects U.S.-based social norms,
derived from American corpora and sociocultural
frameworks. This specification ensures cultural
precision and avoids conflating diverse normative
practices across other English-speaking contexts
(e.g., British, Australian, Canadian). The frame-
work consists of four core stages, each responsi-
ble for modeling social communication: (1) norm
and style design, (2) scenario-situation construc-
tor, (3) exemplar-based iterative refinement engine,
and (4) multi-turn dialogue generator with turn-
level annotation. Figure 2 illustrates the overall
pipeline and stage flow. Also, the complete algo-
rithmic workflow of our framework is provided in
Appendix C.1.
3.1
Norm and Style Design
We construct a taxonomy of 12 conversational so-
cial norm categories by extending the 10 categories
proposed in (Li et al., 2023) with two additional
types: Empathy and Respect, motivated by prior
work on dialogic functions (Stolcke et al., 2000;
Bunt et al., 2020). The complete set is listed in
Table 1. For each category, we define 10 culturally
grounded subnorms per target language. To gener-
ate Korean-specific subnorms, we prompt an LLM
with value-centric responses from the World Val-
ues Survey (WVS Wave 7, South Korea) (Haerpfer
et al., 2022). English and Chinese subnorms are
adapted from (Li et al., 2023) through LLM-guided
alignment with the Korean outputs. All subnorms
are validated by native speakers or cultural experts
to ensure fluency and cultural plausibility, yielding
120 subnorms per language (Figure 2 (1)). We also
define pragmatic and stylistic parameters that guide
both scenario construction and dialogue generation.
These include tone(formal vs. casual), honorific
usage, relational distance (peer vs. hierarchical),
and emotional alignment. Representative uses are
shown in Table 19, with prompt templates and spec-
ifications provided in Appendix C.
3.2
Scenario-Situation Constructor
For
each
subnorm,
we
construct
a
sce-
nario–situation pair consisting of: (a) a scenario
that provides a concise, real-world context, and
(b) a situation that expands upon the scenario
with 3–5 sentences specifying relational roles,
emotional states, and stylistic features such as
tone and honorifics. Each instance is labeled as
one of three interaction types: Norm Adherence,
Norm
Violation,
or
Violation-to-Resolution
(V2R). While the first two reflect conventional
norm conformity or transgression, V2R models
post-violation repair strategies, capturing core
aspects of interactional competence (Goffman,
2017; Feine et al., 2019). Despite its importance,
V2R remains largely absent from prior norm-based
dialogue datasets. To our knowledge, this is the
first work to formally define and incorporate
V2R into social dialogue modeling. Examples of
each type are shown in Appendix D. As shown
in Figure 2 (2), scenarios are first generated by
prompting an LLM with a subnorm and interaction
type. These are then expanded into situations via
a second prompt enriched with interpersonal and
emotional cues. Notably, while English outputs are
generally fluent, Korean and Chinese generations
often contain pragmatic inconsistencies (e.g., tone
mismatch, incorrect honorifics).
These issues
motivate the exemplar-based refinement described
in Section 3.3.
3.3
Exemplar-Based Iterative Refinement
Unlike prior approaches that rely on post-hoc fil-
tering or manual correction after dialogue genera-
tion (Lambert et al., 2024; Occhipinti et al., 2024),
our framework introduces an upstream refinement
mechanism at the scenario–situation level, enabling
early enforcement of cultural and pragmatic con-
straints. For each norm category, we manually
curate a small set of high-quality exemplars that re-
flect culturally grounded and stylistically appropri-
ate behaviors. Rather than using static prompts, the
model retrieves semantically and structurally simi-
lar exemplars based on communicative intent, emo-
tional tone, and discourse patterns (e.g., speaker
roles and adjacency), guiding the revision process
without large-scale human annotation.
To determine whether further refinement is nec-
essary, we implement an iterative loop using our

--- Page 5 ---

Refinement Quality (RQ) protocol (Section 4.2),
which evaluates the quality of the revised output
in comparison to the original input. The model
receives a triplet:

Inputorig, Outputrefined, Scorequal

(1)
enabling it to assess the social and stylistic ade-
quacy of the revision and decide whether to con-
tinue refinement. Here, Inputorig denotes the orig-
inal scenario–situation pair, Outputrefined is the re-
vised output from exemplar-based prompting, and
Scorequal is a scalar computed via the RQ protocol.
This early integration mitigates quality bottle-
necks common in generation-first pipelines and
ensures consistent sociocultural alignment prior to
dialogue construction. The effectiveness of our
approach is illustrated in Appendix D through rep-
resentative before-and-after examples across lan-
guages and norm categories, with full evaluation
results reported in Section 5.1.
3.4
Multi-Turn Dialogue Generator with
Turn-Level Annotation
After refinement, each scenario–situation pair is
expanded into a multi-turn dialogue (5–15 turns),
resulting in socially and contextually appropriate
interactions. Each utterance is annotated with (a)
norm adherence, (b) speaker reaction including in-
tent and emotional state, and (c) justification for the
assigned label. This structure enables fine-grained
modeling of social dynamics by identifying norm
compliance and explaining speaker behavior. Reac-
tion labels, grounded in dialogue act theory (Stol-
cke et al., 2000), are assigned via LLM-based
prompting and expert verification, as detailed in
Appendix C.7. The resulting dataset supports norm
reasoning and socially sensitive dialogue modeling
across cultures. Representative examples of the
generated dialogues and annotations are provided
in Appendix D.
4
Evaluation Framework
4.1
Datasets and Experimental Conditions
Dataset Composition and Baselines.
We con-
struct a multicultural dataset in English, Chi-
nese, and Korean, with 1,200 instances per lan-
guage across three interaction types: Norm Adher-
ence, Norm Violation, and Violation-to-Resolution
(V2R), resulting in 10,800 instances overall. We
conducted our experiments using four NVIDIA
A100 GPUs over a duration of eight hours.
For the baselines, we compare against the fol-
lowing existing resources:
• NORMDIAL (Li et al., 2023): A bilingual En-
glish–Chinese corpus with turn-level norm ad-
herence and violation annotations.
• SODA (Kim et al., 2023): An English corpus
of socially appropriate dialogues grounded in
social commonsense.
Model Configuration and Evaluation Protocol.
All scenario–situation refinements and dialogue
generations are conducted using GPT-4.1 (Ope-
nAI, 2025), guided by a small set of expert-curated
exemplars derived from manually revised model
outputs. These exemplars reflect culturally and
pragmatically appropriate responses and are used
to steer iterative refinement, particularly in low-
resource languages. Illustrative examples and re-
finement prompts are provided in Appendix C.5.
Automatic evaluations are performed using GPT-4o
in a zero-shot setting with metric-specific prompts
as described in Appendix E.
For downstream experiments (Section 5), we
fine-tune both closed and open-source language
models: GPT-4o-mini as a closed model, and
LLaMA-3-8B (Dubey et al., 2024), Qwen-2.5-14B,
and Qwen-2.5-32B (Team, 2024) as open-source
baselines. All models are trained under identical
configurations for each language to ensure com-
parability. Human evaluations were conducted by
native Chinese and Korean speakers who were se-
lected for their linguistic fluency and cultural fa-
miliarity. To assess model performance in low-
resource cultural settings, we recruited six indepen-
dent graduate students (four Korean, two Chinese)
as annotators. For each evaluation, we randomly
sampled 100 dialogues per type, and annotators
rated the outputs on fluency, relevance, and so-
cial norm adherence using a Likert-scale judgment.
These human assessments were further comple-
mented with automatic evaluations based on our
proposed metrics. Detailed procedures are pro-
vided in Appendix E.
4.2
Evaluation Objectives and Design
We evaluate our framework along three axes:
1. Refinement Quality (RQ): Does our refine-
ment method improve generation quality in
low-resource languages?

--- Page 6 ---

Criterion
Description
Norm Alignment
Adherence to the intended social
norm
Language Quality
Grammaticality and fluency
Semantic Fidelity
Preservation of original intent
Table 2: Evaluation criteria used for refinement quality
assessment. Scoring uses a 5-point Likert scale with
both LLM and expert annotators. Detailed prompt tem-
plates for each evaluation criterion are included in Ap-
pendix E.2
Criterion
Description
Consistency
Logical flow across turns
Naturalness
Fluency and human-likeness
Relevance
Context-appropriate responses
Emotion
Appropriateness
Tone aligned with context
Social Norm
Appropriateness
Cultural and normative compliance
Scenario
Coherence
Semantic alignment with the scenario
Table 3: Evaluation criteria used for dialogue quality
(DQ). Detailed are included in Appendix E.3
2. Dialogue Quality(DQ): Do generated dia-
logues align with norms and pragmatic ex-
pectations?
3. Generalization Quality (GQ): Do our mod-
els outperform baselines in quality and human
preference?
Evaluation templates for both LLM and human
assessments are detailed in Appendix E, along with
detailed evaluation description and guidelines.
Refinement Quality (RQ)
We compare scenario-
situation pairs before and after refinement in Ko-
rean and Chinese. Table 2 summarizes the three
key dimensions used to evaluate refinement quality.
Dialogue Quality (DQ)
We assess multi-turn di-
alogues along six criteria adapted from (Kim et al.,
2023; Li et al., 2023). Our evaluation criteria are
detailed in Table 3. LLMs and human annotators
independently conduct evaluations.
Generalization Quality (GQ)
We fine-tune four
language models on norm-adherent dialogues from
three datasets. For training, we use 1,200 English
and Chinese instances from our dataset. In addition,
we use 1,265 English and 1,116 Chinese instances
from NORMDIAL, as well as 1,200 randomly sam-
pled English dialogues from SODA. Models are
evaluated on DAILYDIALOG (English) (Li et al.,
2017) and LCCC (Chinese) (Wang et al., 2022),
where each is prompted to generate five-turn con-
tinuations given benchmark dialogue contexts. We
conduct A/B preference testing and human evalua-
tion, with judgments based on social appropriate-
ness, fluency, and overall response quality.
5
Results
We present results along the three evaluation axes
defined in Section 4. Also, we further analyze
the impact of our Violation-to-Resolution (V2R)
modeling. Our framework consistently improves
linguistic fluency, pragmatic coherence, and social
appropriateness across all settings.
5.1
Refinement Quality (RQ)
To assess the effectiveness of exemplar-based re-
finement, we compare scenario-situation pairs be-
fore and after refinement in two low-resource lan-
guages: Korean and Chinese. As shown in Ta-
ble 4, refinement consistently improves all evalua-
tion dimensions across both languages. In Korean,
linguistic quality improves substantially, accom-
panied by gains in norm alignment and semantic
fidelity. Similar patterns are observed in Chinese,
with a +1.32 increase in linguistic quality and near-
ceiling norm alignment scores.
The refinement process is repeated until the
model output is no longer selected for revision by
the LLM. On average, each instance undergoes
1.2 rounds of refinement. These findings under-
score the utility of our approach in enhancing flu-
ency, coherence, and sociocultural adequacy for
low-resource language generation.
To test generalizability beyond East Asian ty-
pologies, we conducted pilot refinement experi-
ments in Malay and Urdu, two pragmatically dis-
tinct languages. Using the same evaluation setup
as in Table 4, the observed improvements were
consistent with those from our main experiments,
supporting the robustness of our approach. De-
tailed results of these pilot studies are provided in
Appendix F.2, which further illustrate the adapt-
ability of our refinement strategy across diverse
linguistic and cultural contexts.
5.2
Dialogue Quality (DQ)
We evaluated dialogue quality across six dimen-
sions using both LLM- and human-based scor-

--- Page 7 ---

Language
Condition
Norm Align.
Linguistic Quality
Semantic Fidelity
Korean
Initial
4.577
3.589
N/A
Refined
4.908
4.910
4.766
Chinese
Initial
4.855
3.603
N/A
Refined
4.995
4.926
4.865
Table 4: Refinement evaluation results (RQ) in Korean and Chinese. Scores are based on a 5-point Likert scale
averaged over LLM and human raters. Detailed are included in Appendix E.2
ing.
Criteria are summarized in Table 3.
For
conciseness, we abbreviate the last three dimen-
sions—emotional appropriateness, social norm
appropriateness, and scenario–dialogue coher-
ence—as Emo. Approp., Norm Approp., and Sce-
nario Coh., respectively, throughout this section.
Table 5 presents the average scores obtained
from LLM-based evaluation for Adherence, V2R,
and Violation scenarios in Korean, Chineses, and
English. Dialogues from the Adherence and V2R
categories consistently achieved high ratings (avg.
> 4.9), especially for consistency, emotional ap-
propriateness, and scenario coherence. V2R dia-
logues slightly outperformed others in emotional
appropriateness and scenario–dialogue alignment,
highlighting the framework’s strength in modeling
socially complex, repair-driven interactions. In con-
trast, Violation dialogues received lower scores in
naturalness and emotional appropriateness across
all languages, reflecting their design to capture so-
cially inappropriate interactions.
Human Evaluation.
To validate the robustness
of our LLM-based assessments and to examine
generation quality in low-resource settings, we con-
ducted a parallel human evaluation in Korean and
Chinese. As shown in Table 6, human ratings ex-
hibit patterns highly consistent with LLM scores
reported in Table 5. We further quantified the align-
ment between LLM and human evaluations using
Pearson correlation. Results indicate strong agree-
ment across both languages, with coefficients of
r = 0.928 (Korean) and r = 0.945 (Chinese).
These findings confirm the reliability of our auto-
matic evaluation protocol and support the validity
of the conclusions drawn from it.
5.3
Generalization Quality (GQ)
Automatic evaluation results are summarized in Ta-
ble 7. Across all models and languages, our dataset
yields consistently higher preference than NOR-
MDIAL and SODA. For instance, GPT-4o-mini
was preferred in 65% (English) and 75% (Chinese)
Language
Criterion
Adherence
V2R
Violation
Korean
Consistency
4.978
4.978
2.594
Naturalness
5.000
4.998
4.757
Relevance
4.996
5.000
4.996
Emo. Approp.
4.999
5.000
3.375
Norm Approp.
4.707
3.816
1.613
Scenario Coh.
4.988
5.000
4.965
Chinese
Consistency
5.000
4.952
1.662
Naturalness
4.432
4.361
2.700
Relevance
4.987
5.000
4.950
Emo. Approp.
5.000
4.987
1.918
Norm Approp.
4.980
3.528
1.216
Scenario Coh.
4.896
5.000
4.811
English
Consistency
5.000
4.947
1.665
Naturalness
4.900
4.623
3.381
Relevance
5.000
5.000
4.842
Emo. Approp.
5.000
4.992
2.589
Norm Approp.
4.982
3.241
1.186
Scenario Coh.
4.994
4.932
4.801
Table 5: Dialogue quality scores across six dimensions,
evaluated on three scenario types (Adherence, Violation-
to-Resolution (V2R), Violation) in three languages.
of cases over NORMDIAL, and in 65% (English)
over SODA. Larger models such as Qwen-2.5-32B
showed similar trends, with the strongest prefer-
ence observed in Chinese. To validate these find-
ings, we conducted blind human evaluations in
Korean and Chinese (Table 8). Native speakers
favored our dataset in 68% (Korean) and 77% (Chi-
nese) of cases, closely matching LLM preferences.
These results suggest that models trained on our
dataset generalize better across languages and do-
mains, generating more socially appropriate and
contextually aligned responses.
We note that the untuned model occasionally pro-
duced concise, direct responses that some evalua-
tors preferred in contexts requiring rapid apologies
without nuanced emotional transitions. However,
such cases were limited, and overall, our dataset
achieved more than double the preference rate of
the baseline. This result suggests that exemplar-
guided refinement not only enhances overall qual-
ity but also provides a flexible framework for fine-
grained control of response style and emotional
expression, which we plan to investigate in future
work.

--- Page 8 ---

Language
Criterion
Adherence
V2R
Violation
Korean
Consistency
4.500
5.000
2.500
Naturalness
4.250
4.625
4.125
Relevance
4.750
4.750
4.250
Emo. Approp.
4.625
4.500
3.250
Norm Approp.
4.500
4.375
1.375
Scenario Coh.
4.750
4.625
4.500
Chinese
Consistency
4.500
4.375
1.500
Naturalness
4.625
4.500
3.125
Relevance
5.000
4.750
4.500
Emo. Approp.
4.500
5.000
1.375
Norm Approp.
4.750
4.500
1.500
Scenario Coh.
4.750
4.625
4.125
Table 6: Human evaluation results across dialogue types
(Adherence, Violation-to-Resolution (V2R), Violation)
and six dimensions. Scores are based on a 5-point Likert
scale.
Model
Language
Ours vs. NormDial
Ours vs. SODA
GPT-4o-mini
English
65%
65%
Chinese
75%
N/A
LLaMA-3-8B
English
65%
59%
Qwen-2.5-14B
English
51%
61%
Chinese
71%
N/A
Qwen-2.5-32B
English
56%
62%
Chinese
79%
N/A
Table 7: A/B test results comparing preference for mod-
els trained on our dataset versus NormDial and SODA.
Each value represents the percentage of times responses
from models trained on our dataset were preferred by
annotators.
5.4
Effect of Violation-to-Resolution
To assess the impact of Violation-to-Resolution
(V2R) training on norm-sensitive generation, we
conduct a focused comparison using PROSOCIAL-
DIALOG (Kim et al., 2022), a benchmark for ethi-
cally challenging scenarios. We fine-tune two GPT-
4o-mini models under comparable conditions: one
on the full NormDial dataset and one on an equal-
sized subset of our data, including three types of
our datasets. Both models are prompted with 100
norm-violating contexts, each requiring a five-turn
continuation.
Blind A/B human evaluations show that the V2R-
augmented model is preferred in 82% of cases (Ta-
ble 9), with annotators consistently favoring its
empathy, contextual fit, and ability to model norm
repair. These findings underscore the utility of
V2R as a training signal for enhancing pragmatic
competence in ethically sensitive dialogue and sup-
port its integration into norm-grounded generation
frameworks.
Language
Ours
Untuned GPT-4o-mini
NormDial
Korean
68%
32%
N/A
Chinese
77%
5%
18%
Table 8: Human preference results comparing our
dataset with untuned GPT-4o-mini and NormDial. Eval-
uations were conducted under blind conditions with
native speakers. Korean evaluation compares against
untuned GPT-4o-mini, while Chinese includes baseline.
6
Discussion
Limitations of Prompt-Based Generation in
Low-Resource Contexts.
Our refinement frame-
work is motivated in part by the limitations of prior
prompt-based approaches to social norm genera-
tion (Li et al., 2023; Zhan et al., 2024). These
methods typically rely on static prompts with min-
imal norm signals, placing the burden of genera-
tion entirely on the language model. While this
approach may yield fluent and contextually appro-
priate responses in high-resource languages such
as English, it often results in pragmatic failures in
low-resource settings like Korean and Chinese.
In Korean, generated dialogues frequently ex-
hibit lexical redundancy (e.g., repeated expres-
sions) and tone mismatches (e.g., informal apolo-
gies in formal contexts). In Chinese, issues in-
clude unnatural phrasing, exaggerated emotional
responses, repetitive honorifics, and inconsistent
tone from register mixing. These limitations un-
derscore the difficulty of capturing fine-grained
sociocultural norms through prompt-only methods.
To mitigate these issues, we introduce a refine-
ment framework to improve fluency and norm
alignment in low-resource settings. Additional ex-
amples appear in Appendix F.1.
Early Refinement for Sociocultural Alignment.
As shown in Section 5.1, even a small set of high-
quality exemplars at this stage improves fluency
and norm alignment in low-resource languages.
Prior to refinement, we conducted a compara-
tive analysis between model-generated outputs and
native-authored revisions, which revealed recurring
issues such as overuse of formulaic expressions,
limited gesture variety, register–context mismatch,
and weakened hierarchical cues. A key insight
from this analysis is the distinction between sur-
face accuracy and cultural appropriateness: model
outputs may be grammatically and semantically
correct, yet fail to include ritualistic or affective
elements (e.g., apologies, condolences) that are

--- Page 9 ---

Training Data
Preference (%)
Ours (with V2R)
82
NormDial
18
Table 9: Human preference results on PROSOCIALDIA-
LOG. Models trained on our dataset with V2R signifi-
cantly outperformed those trained on NormDial.
Category
Strategy / Sequence
English
Chinese
Korean
Strategy (%)
Apology (A)
98.7
93.0
92.6
Explanation (X)
91.1
88.1
86.3
Empathy (E)
90.6
62.0
89.2
Compensation (C)
82.8
79.3
72.4
Humor (H)
12.6
7.9
12.0
Top Sequence
Sequence
X →A →C
A →X →C
E →A →X
Frequency (%)
33
29
32
Table 10: Strategy usage rates and most frequent re-
covery sequences in V2R dialogues across American
English, Chinese, and Korean.
essential to pragmatic expectations. These short-
comings were particularly salient in low-resource
settings and are illustrated in Appendix F.1.
When optimized early in the generation pipeline,
scenario–situation pairs provide strong social cues
that guide the construction of coherent and cul-
turally aligned dialogues.
This early-stage re-
finement approach also aligns with recent works
in controllable generation and structured plan-
ning (Moryossef et al., 2019; Rashkin et al., 2021),
which emphasize the role of explicit context mod-
eling in coherence and goal alignment. Since so-
cial norms are inherently entangled with relational
roles, power dynamics, and situational contexts,
refining situational priors ensures that pragmatic
and culturally appropriate behaviors emerge natu-
rally. Our refinement stage thus functions not as
a post hoc correction layer, but as a core mecha-
nism for embedding sociocultural alignment into
the generative process.
Qualitative Insights into Cross-Linguistic Re-
pair Strategies
Our qualitative analysis of
Violation-to-Resolution (V2R) dialogues shows
that the proposed framework effectively models
both universal and culture-specific repair strate-
gies. As summarized in Table 10, Apology and
Explanation dominate across English, Chinese, and
Korean. Still, sequencing patterns diverge in cul-
turally meaningful ways: English dialogues most
often follow Explanation →Apology →Compen-
sation, Chinese dialogues Apology →Explanation
→Compensation, and Korean dialogues Empa-
thy →Apology →Explanation. These results, in-
formed by established taxonomies in apology and
politeness research (Radu et al., 2019; Zhang and
Wang, 2024), validate the framework’s ability to
capture nuanced cross-linguistic variation. Notably,
over 85% of V2R dialogues employed multi-step
recovery, confirming that socially coherent repair
rarely occurs through a single act. By integrating
exemplar-guided refinement, our approach models
these layered dynamics, bridging computational
dialogue generation with sociolinguistic insights.
These findings highlight the dual value of the V2R
paradigm: providing a scalable schema for real-
istic dialogue repair and serving as a diagnostic
lens for cultural variation. This adaptability also
points to promising directions for extending Nor-
mGenesis to typologically diverse languages (e.g.,
Arabic, Swahili, Hindi), where divergent pragmatic
systems pose additional challenges.
7
Conclusion
We present NormGenesis, a multicultural frame-
work for generating and refining socially grounded
dialogues in English, Chinese, and Korean. To
address cultural and pragmatic limitations of exist-
ing dialogue systems, particularly in low-resource
settings, we introduce an exemplar-based itera-
tive refinement applied at the scenario-situation
level. This upstream refinement design enables
early alignment with linguistic, emotional, and so-
ciocultural expectations, reducing generation er-
rors before full dialogue synthesis. We further pro-
pose a novel dialogue type, Violation-to-Resolution
(V2R), which models the recovery process follow-
ing norm violations through repair strategies. V2R
facilitates more realistic and context-sensitive mod-
eling of social interaction dynamics. Our experi-
mental results show that V2R not only improves
pragmatic competence in ethically sensitive sce-
narios but also enhances generalization across lan-
guages and domains. Through comprehensive hu-
man and LLM-based evaluations, we demonstrate
that NormGenesis consistently outperforms exist-
ing datasets such as NORMDIAL and SODA across
multiple dimensions, including norm alignment,
emotional coherence, and repair quality. By inte-
grating linguistically and culturally diverse norms,
fine-grained turn-level annotations, and structured
refinement, NormGenesis provides a scalable and
robust foundation for norm-aware dialogue model-
ing in multilingual and multicultural contexts.

--- Page 10 ---

Limitations
While NormGenesis achieves strong performance
across linguistic, emotional, and social dimensions,
we acknowledge several limitations that open key
directions for future work.
Language Coverage.
Our framework currently
supports only English, Chinese, and Korean. While
these languages span a spectrum of resource avail-
ability and cultural characteristics, the framework
does not address the full diversity of global lan-
guages and interactional norms. Expanding Nor-
mGenesis to additional languages—particularly
those with limited computational resources or
distinct social conventions (e.g., Arabic, Hindi,
Swahili)—remains a key avenue for future work.
To test generalizability beyond East Asian ty-
pologies, we conducted pilot refinement in Malay
and Urdu, two pragmatically distinct languages.
The results closely aligned with those from our
main experiments, demonstrating the framework’s
capacity to generalize to typologically and cultur-
ally diverse settings. Detailed results are presented
in Appendix F.2. Building on this, we plan to
extend NormGenesis to further low-resource lan-
guages, including Arabic and Swahili.
Exemplar Scalability.
The iterative refinement
process relies on a small number of manually re-
vised exemplars. Although this approach is more
scalable than full human annotation, scaling to a
large number of new norms or domains could still
be resource-intensive. To mitigate this, future work
will explore active learning for efficient exemplar
selection, a structured norm-centric repository for
retrieval-based reuse, and clustering of culturally
aligned regions (e.g., via World Values Survey) to
enable exemplar transfer. These strategies aim to
improve coverage and ensure scalable, high-quality
refinement.
Evaluation and Subjectivity.
Evaluating social
norm adherence and conversational appropriate-
ness inevitably involves subjectivity and cultural
bias, especially across diverse sociolinguistic con-
texts. To mitigate this, we adopted three safeguards:
(1) detailed rubrics assessing norm alignment, flu-
ency, and emotional appropriateness (Appendix E);
(2) native speaker annotators with cultural exper-
tise; and (3) cross-review by multiple experts to
offset exemplar-induced bias. While these mea-
sures and high inter-annotator agreement enhance
reliability, further reducing cultural subjectivity re-
mains an open challenge. Future research could
explore culturally calibrated evaluation protocols
or leverage LLM-based evaluators fine-tuned on
localized criteria.
Norm Evolution.
Social norms are dynamic and
shift across time, communities, and platforms. Our
taxonomy provides a structured but time-bounded
snapshot. Systematically tracking and modeling
the evolution of norms over time and across so-
cial contexts will be important for adaptive and
future-proof dialogue systems. Future work should
systematically track norm shifts using longitudinal
corpora or real-time social data, enabling adaptive
norm modeling for evolving conversational envi-
ronments.
Ethical Considerations
NormGenesis aims to advance the development of
culturally adaptive and socially competent dialogue
agents by modeling nuanced social norms across
English, Chinese, and Korean. However, several
ethical considerations warrant discussion.
Intended Use and Misuse.
Our dataset is de-
signed for training dialogue systems to generate
socially appropriate, norm-aware responses. As
with any dataset containing norm violations and
repair strategies, there is a risk that malicious users
could exploit the resource to train agents that gen-
erate inappropriate or harmful utterances. We urge
the community to use the dataset solely for proso-
cial, culturally sensitive, and norm-aligned conver-
sational AI research.
Cultural Scope and Generalizability.
Norm-
Genesis reflects culturally salient behaviors as of
the time of data collection.
Despite extensive
native speaker review and expert refinement, so-
cial norms are inherently dynamic and context-
dependent. Caution is advised when applying the
resource to new languages, regions, or changing so-
cietal contexts, as some outputs may not generalize
beyond the represented cultures.
Annotation Subjectivity and Bias.
All sub-
norms and dialogues are reviewed or annotated
by cultural experts and native speakers, but the
interpretation of social appropriateness and emo-
tional tone involves subjective judgment. While
inter-annotator agreement is high, some bias may
persist, especially for edge cases or rapidly chang-

--- Page 11 ---

ing norms. Broadening annotator diversity and
incorporating community feedback may mitigate
these effects.
Dataset Balance and Representation.
NormGe-
nesis includes a diverse range of norm-adhering,
violating, and Violation-to-Resolution (V2R) di-
alogues. However, its scenario coverage is not
exhaustive and may reflect existing cultural, de-
mographic, or linguistic biases. Supplementing
NormGenesis with additional resources is encour-
aged to ensure robust and contextually sensitive
conversational agents.
Potential for Negative Outcomes.
While the
V2R paradigm models constructive responses to
norm violations, dialogue agents trained on these
data should not be used for critical decision-making
or sensitive applications (e.g., counseling, legal ad-
vice) without careful human oversight. The frame-
work is intended to support research and develop-
ment in social dialogue modeling, not to replace
professional judgment. All code, data, and anno-
tation guidelines will be released publicly upon
acceptance, promoting transparency, reproducibil-
ity, and responsible community use.
Acknowledgments
This research was supported by the MSIT (Min-
istry of Science and ICT), Korea, under the ITRC
(Information Technology Research Center) support
program (IITP-2025-RS-2020-II201789), and the
Artificial Intelligence Convergence Innovation Hu-
man Resources Development (IITP-2025-RS-2023-
00254592) supervised by the IITP (Institute for
Information & Communications Technology Plan-
ning & Evaluation).
References
Harry Bunt, Volha Petukhova, Emer Gilmartin, Cather-
ine Pelachaud, Alex Fang, Simon Keizer, and Lau-
rent Prévot. 2020. The ISO standard for dialogue
act annotation, second edition. In Proceedings of the
Twelfth Language Resources and Evaluation Confer-
ence, pages 549–558, Marseille, France. European
Language Resources Association.
Samuel Cahyawijaya, Holy Lovenia, and Pascale Fung.
2024. LLMs are few-shot in-context low-resource
language learners. In Proceedings of the 2024 Con-
ference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies (Volume 1: Long Papers), pages
405–433, Mexico City, Mexico. Association for Com-
putational Linguistics.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, and 1 others. 2024. The llama 3 herd of models.
arXiv e-prints, pages arXiv–2407.
Jon Elster. 2006. Fairness and norms. Social Research:
An International Quarterly, 73(2):365–376.
Jasper Feine, Ulrich Gnewuch, Stefan Morana, and
Alexander Maedche. 2019. A taxonomy of social
cues for conversational agents. International Journal
of human-computer studies, 132:138–161.
Maxwell Forbes, Jena D Hwang, Vered Shwartz,
Maarten Sap, and Yejin Choi. 2020. Social chem-
istry 101: Learning to reason about social and moral
norms. In Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Processing
(EMNLP), pages 653–670.
Soumya Suvra Ghosal, Soumyabrata Pal, Koyel
Mukherjee, and Dinesh Manocha. 2025. PromptRe-
fine:
Enhancing few-shot performance on low-
resource Indic languages with example selection
from related example banks. In Proceedings of the
2025 Conference of the Nations of the Americas
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies (Volume 1:
Long Papers), pages 351–365, Albuquerque, New
Mexico. Association for Computational Linguistics.
Erving Goffman. 2017. Interaction ritual: Essays in
face-to-face behavior. Routledge.
Geyang Guo, Tarek Naous, Hiromi Wakaki, Yukiko
Nishimura, Yuki Mitsufuji, Alan Ritter, and Wei Xu.
2025. Care: Aligning language models for regional
cultural awareness. Preprint, arXiv:2504.05154.
Christian Haerpfer,
Ronald Inglehart,
Alejandro
Moreno, Christian Welzel, Kseniya Kizilova, Jose
Diez-Medrano, Marta Lagos, Pippa Norris, Eduard
Ponarin, and Bi Puranen, editors. 2022. World Values
Survey: Round Seven – Country-Pooled Datafile Ver-
sion 6.0. JD Systems Institute & WVSA Secretariat,
Madrid, Spain & Vienna, Austria.
Songbo Hu, Han Zhou, Mete Hergul, Milan Gritta,
Guchun Zhang, Ignacio Iacobacci, Ivan Vuli´c, and
Anna Korhonen. 2023. Multi3woz: A multilingual,
multi-domain, multi-parallel dataset for training and
evaluating culturally adapted task-oriented dialog sys-
tems. Preprint, arXiv:2307.14031.
Yuncheng Hua, Lizhen Qu, and Reza Haf. 2024. Assis-
tive large language model agents for socially-aware
negotiation dialogues. In Findings of the Association
for Computational Linguistics: EMNLP 2024, pages
8047–8074, Miami, Florida, USA. Association for
Computational Linguistics.
Seongbo Jang, Seonghyeon Lee, and Hwanjo Yu. 2024.
KoDialogBench: Evaluating conversational under-
standing of language models with Korean dialogue

--- Page 12 ---

benchmark. In Proceedings of the 2024 Joint In-
ternational Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 9905–9925, Torino, Italia.
ELRA and ICCL.
Hyunwoo Kim, Jack Hessel, Liwei Jiang, Peter West,
Ximing Lu, Youngjae Yu, Pei Zhou, Ronan Bras,
Malihe Alikhani, Gunhee Kim, and 1 others. 2023.
Soda: Million-scale dialogue distillation with social
commonsense contextualization. In Proceedings of
the 2023 Conference on Empirical Methods in Natu-
ral Language Processing, pages 12930–12949.
Hyunwoo Kim, Youngjae Yu, Liwei Jiang, Ximing
Lu, Daniel Khashabi, Gunhee Kim, Yejin Choi, and
Maarten Sap. 2022. Prosocialdialog: A prosocial
backbone for conversational agents. In Proceedings
of the 2022 Conference on Empirical Methods in
Natural Language Processing, pages 4005–4029.
Nathan Lambert, Hailey Schoelkopf, Aaron Gokaslan,
Luca Soldaini, Valentina Pyatkin, and Louis Cas-
tricato. 2024.
Self-directed synthetic dialogues
and revisions technical report.
arXiv preprint
arXiv:2407.18421.
Jiyoung Lee, Minwoo Kim, Seungho Kim, Junghwan
Kim, Seunghyun Won, Hwaran Lee, and Edward
Choi. 2024. KorNAT: LLM alignment benchmark
for Korean social values and common knowledge. In
Findings of the Association for Computational Lin-
guistics: ACL 2024, pages 11177–11213, Bangkok,
Thailand. Association for Computational Linguistics.
Cheng Li, Damien Teney, Linyi Yang, Qingsong Wen,
Xing Xie, and Jindong Wang. 2024. Culturepark:
Boosting cross-cultural understanding in large lan-
guage models. Preprint, arXiv:2405.15145.
Oliver Li, Mallika Subramanian, Arkadiy Saakyan, CH-
Wang Sky, and Smaranda Muresan. 2023. Norm-
dial: A comparable bilingual synthetic dialog dataset
for modeling social norm adherence and violation.
In Proceedings of the 2023 Conference on Empiri-
cal Methods in Natural Language Processing, pages
15732–15744.
Yanran Li, Hui Su, Xiaoyu Shen, Wenjie Li, Ziqiang
Cao, and Shuzi Niu. 2017. Dailydialog: A manually
labelled multi-turn dialogue dataset. In Proceedings
of the Eighth International Joint Conference on Nat-
ural Language Processing (Volume 1: Long Papers),
pages 986–995.
Zhaojiang Lin, Andrea Madotto, Genta Indra Winata,
Peng Xu, Feijun Jiang, Yuxiang Hu, Chen Shi, and
Pascale Fung. 2021.
Bitod: A bilingual multi-
domain dataset for task-oriented dialogue modeling.
Preprint, arXiv:2106.02787.
Bertram F Malle, Steve Guglielmo, and Andrew E Mon-
roe. 2014. A theory of blame. Psychological Inquiry,
25(2):147–186.
Amit Moryossef, Yoav Goldberg, and Ido Dagan. 2019.
Step-by-step: Separating planning from realization
in neural data-to-text generation. In Proceedings of
the 2019 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, Volume 1 (Long and
Short Papers), pages 2267–2277.
Xuan-Phi Nguyen, Mahani Aljunied, Shafiq Joty, and
Lidong Bing. 2024. Democratizing llms for low-
resource languages by leveraging their english domi-
nant abilities with linguistically-diverse prompts. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 3501–3516.
Daniela Occhipinti, Michele Marchi, Irene Mondella,
Huiyuan Lai, Felice Dell’Orletta, Malvina Nissim,
and Marco Guerini. 2024. Fine-tuning with HED-
IT: The impact of human post-editing for dialogical
language models. In Findings of the Association
for Computational Linguistics: ACL 2024, pages
11892–11907, Bangkok, Thailand. Association for
Computational Linguistics.
OpenAI. 2025. Openai models documentation. Ac-
cessed: 2025-04-01.
Salsabila Zahirah Pranida, Rifo Ahmad Genadi, and
Fajri Koto. 2025.
Synthetic data generation for
culturally nuanced commonsense reasoning in low-
resource languages. Preprint, arXiv:2502.12932.
Alexandru
Gabriel
Radu,
Denni
Arli,
Jiraporn
Surachartkumtonkun, Scott Weaven, and Owen
Wright. 2019. Empathy and apology: The effective-
ness of recovery strategies. Marketing Intelligence &
Planning, 37(4):358–371.
Abhinav Sukumar Rao, Akhila Yerukola, Vishwa Shah,
Katharina Reinecke, and Maarten Sap. 2025. Nor-
mAd: A framework for measuring the cultural adapt-
ability of large language models. In Proceedings of
the 2025 Conference of the Nations of the Americas
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies (Volume 1:
Long Papers), pages 2373–2403, Albuquerque, New
Mexico. Association for Computational Linguistics.
Hannah Rashkin, David Reitter, Gaurav Singh Tomar,
and Dipanjan Das. 2021.
Increasing faithfulness
in knowledge-grounded dialogue with controllable
features. In Proceedings of the 59th Annual Meet-
ing of the Association for Computational Linguistics
and the 11th International Joint Conference on Natu-
ral Language Processing (Volume 1: Long Papers),
pages 704–718.
Andreas Stolcke, Klaus Ries, Noah Coccaro, Eliza-
beth Shriberg, Rebecca Bates, Daniel Jurafsky, Paul
Taylor, Rachel Martin, Carol Van Ess-Dykema, and
Marie Meteer. 2000. Dialogue act modeling for au-
tomatic tagging and recognition of conversational
speech. Computational linguistics, 26(3):339–373.

--- Page 13 ---

Qwen Team. 2024. Qwen2.5: A party of foundation
models.
Yida Wang, Pei Ke, Yinhe Zheng, Kaili Huang, Yong
Jiang, Xiaoyan Zhu, and Minlie Huang. 2022. A
large-scale chinese short-text conversation dataset.
Preprint, arXiv:2008.03946.
Haolan Zhan, Zhuang Li, Xiaoxi Kang, Tao Feng,
Yuncheng Hua, Lizhen Qu, Yi Ying, Mei Rianto
Chandra, Kelly Rosalin, Jureynolds Jureynolds, Suraj
Sharma, Shilin Qu, Linhao Luo, Ingrid Zukerman,
Lay-Ki Soon, Zhaleh Semnani Azad, and Reza Haf.
2024. RENOVI: A benchmark towards remediating
norm violations in socio-cultural conversations. In
Findings of the Association for Computational Lin-
guistics: NAACL 2024, pages 3104–3117, Mexico
City, Mexico. Association for Computational Lin-
guistics.
Haolan Zhan, Zhuang Li, Yufei Wang, Linhao Luo,
Tao Feng, Xiaoxi Kang, Yuncheng Hua, Lizhen Qu,
Lay-Ki Soon, Suraj Sharma, and 1 others. 2023. So-
cialdial: A benchmark for socially-aware dialogue
systems. In Proceedings of the 46th International
ACM SIGIR Conference on Research and Develop-
ment in Information Retrieval, pages 2712–2722.
Junran Zhang and Nan Wang. 2024. The impact of hu-
morous apology expression on consumer forgiveness
and trust rebuilding after trust violations.
Tianyang Zhong, Zhenyuan Yang, Zhengliang Liu,
Ruidong Zhang, Yiheng Liu, Haiyang Sun, Yi Pan,
Yiwei Li, Yifan Zhou, Hanqi Jiang, Junhao Chen, and
Tianming Liu. 2024. Opportunities and challenges
of large language models for low-resource languages
in humanities research. Preprint, arXiv:2412.04497.
A
Dataset Overview
A.1
Dataset Composition Summary
Our dataset includes multicultural social norm dia-
logues across 12 categories: Apology, Compliment,
Condolence, Criticism, Empathy, Greeting, Leave-
taking, Persuasion, Request, Respect, Responding
to Compliments, Thanks. For each category, we
define 10 subnorms per language (English, Korean,
Chinese), resulting in 120 subnorms per language.
• Total Subnorms: 360 (120 per language)
• Total Scenario–Situation Pairs: 10,800 (3
types × 3 languages × 1,200 each)
• Total Dialogues: 10,800 (1 per instance)
• Total Average Turn: 11.91 Turn.
Adherence
Lang
Cat
Sub
Scen
Situ
Dial
AvgT
EN
12
120
1200
1200
1200
10.56
KR
12
120
1200
1200
1200
10.21
ZH
12
120
1200
1200
1200
10.74
Table 11: Dataset statistics for Adherence
Violation-to-Resolution (V2R)
Lang
Cat
Sub
Scen
Situ
Dial
AvgT
EN
12
120
1200
1200
1200
16.06
KR
12
120
1200
1200
1200
12.56
ZH
12
120
1200
1200
1200
13.49
Table 12: Dataset statistics for violation-to-resolution
(V2R)
A.2
Norm-Type Statistics
To provide an overview of the social norm taxon-
omy introduced in this study, Table 11, 12, and 13
present detailed summary statistics for the Adher-
ence, Violation-to-Resolution (V2R), and Viola-
tion categories, respectively. For brevity, column
headers are abbreviated as follows: Lang = Target
Language, Cat = Norm Category, Sub = Subnorm,
Scen = Scenario, Situ = Situation, Dial = Dialogue,
AvgT = Average Turn Count per dialogue. These
tables summarize the scale and structure of our
dataset across all categories and languages.
A.3
Subnorm Coverage and Cultural
Examples
Each of the 12 norm categories comprises 10 cultur-
ally grounded subnorms per language, resulting in
a total of 360 subnorm definitions with aligned ex-
amples across English, Korean, and Chinese. These
examples serve as reference points for scenario gen-
eration and support culturally appropriate dialogue
construction in each language. Full examples are
provided in Appendix C.
A.4
Instance Structure
Each dialogue instance in the dataset is composed
of the following stages:
• Norm Category & Subnorm:
A high-
level social norm category and its culturally
grounded subnorm definition.
• Scenario: A brief 1–2 sentence description
outlining the situational context in which the
norm is relevant.

--- Page 14 ---

Violation
Lang
Cat
Sub
Scen
Situ
Dial
AvgT
EN
12
120
1200
1200
1200
11.59
KR
12
120
1200
1200
1200
11.17
ZH
12
120
1200
1200
1200
10.82
Table 13: Dataset statistics for violation
• Situation: A 3–5 sentence elaboration of the
scenario that specifies tone, interpersonal rela-
tionship, and emotional cues to guide dialogue
generation.
• Dialogue: A multi-turn conversation consist-
ing of 5 to 15 turns that reflects the defined
norm and situational context.
• Annotations: Turn-level labels for social
norm adherence (e.g., Adherence, Violated,
V2R) and speaker reactions (e.g., Apology,
Empathy, Agreement), enabling fine-grained
evaluation of social behavior and pragmatic
intent.
This structured format enables controlled gen-
eration and fine-grained annotation of socially
grounded dialogues across multiple languages.
A.5
Language Balance and Complexity
Metric
To ensure cultural and linguistic balance, each lan-
guage is equally represented across all norm types.
While average token length is commonly used to
measure dialogue complexity, we omit it here due
to tokenizer variations across models. Instead, we
report average dialogue turns as a consistent and
model-independent proxy for complexity.
B
Annotation Schema
This appendix describes the schema used for turn-
level annotation of generated dialogues. Each utter-
ance is annotated with a communicative function
label drawn from a predefined set of categories, fa-
cilitating fine-grained analysis of pragmatic intent
and interactional structure across cultural contexts.
B.1
Label Set Definition
We employ a set of 11 functional dialogue act labels
to annotate each turn, as summarized in Table 14.
These labels capture core social and communica-
tive functions, including acknowledgment, apology,
suggestion, justification, and other norm-relevant
speaker intentions.
B.2
Annotation Usage
Each generated dialogue is annotated at the turn
level. Given a dialogue D = u1, ..., un consist-
ing of n utterances, we assign a label yi ∈Y to
each turn ui using an automatic annotation func-
tion fannotate. This annotation framework supports
comparative analysis of pragmatic behavior across
the following dimensions:
• Norm Type: Adherence, Violation, Violation-
to-Resolution (V2R)
• Cultural Context: English (EN), Korean
(KR), Chinese (ZH)
• Speaker Role: e.g., subordinate vs. authority
figure
This enables a structured investigation of how
social norms and communicative functions vary
across languages and roles.
B.3
Annotation Example
Appendix C.7 details the prompt formulations used
to perform turn-level annotation. For illustration,
Figure 7 presents a turn-level annotation example
for the “Adherence” category in English.
C
Generation & Refinement Prompt
Templates
This appendix presents the full set of prompt tem-
plates used throughout the multilingual dialogue
generation and refinement pipeline. We first out-
line the overall algorithmic workflow, which de-
fines the step-by-step procedures for constructing
culturally grounded dialogues. We then provide
task-specific prompt templates corresponding to
each stage of the pipeline, designed to ensure con-
sistency, linguistic fluency, and norm alignment
across languages.
C.1
Algorithm of Our Framework
Algorithm 1 outlines the complete pipeline used
to construct our multilingual, norm-grounded dia-
logue dataset. The framework consists of four main
stages:
Step 1: Social Norm Construction.
For each
language l and social norm category c, we generate
a set of subnorms Nl,c that encode fine-grained,
culturally grounded expectations. These subnorms
serve as foundational inputs for subsequent stages
of scenario and dialogue generation.

--- Page 15 ---

Label
Description
ACK (Acknowledgment)
Explicit acknowledgment that the speaker has heard or understood the interlocu-
tor’s statement.
AGR (Agreement)
Expressing agreement or alignment with the other person’s opinion or position.
DIS (Disagreement / Refusal)
Expressing disagreement or rejecting a suggestion.
APO (Apology)
Expressing regret or remorse for one’s mistake or inconvenience caused.
THX (Gratitude)
Expressing appreciation for help, kindness, or praise.
EMP (Empathy / Support)
Emotionally validating or supporting the interlocutor’s feelings or situation.
JUS (Justification)
Offering an explanation or excuse to justify one’s actions or mistakes.
SUG (Suggestion / Advice)
Proposing a solution or sharing an opinion to help resolve an issue.
QUE (Question / Clarification Request)
Asking a question to seek further explanation or information.
CRT (Criticism)
Pointing out problems or expressing negative evaluations of the other person’s
actions or statements.
N/A (Not Applicable)
Used when the utterance does not clearly fall into any of the defined categories
above. Typically applies to greetings, topic transitions, structural openers, or filler
phrases.
Table 14: Turn-level annotation labels and descriptions
Step 2: Scenario–Situation Generation.
For
each subnorm n and dialogue type t (e.g., Ad-
herence, Violation, Violation-to-Resolution), we
construct a scenario Sl,n,t that outlines the relevant
social context. This is followed by a situation Tl,n,t,
which elaborates on tone, relationship, and emo-
tional dynamics to constrain downstream dialogue
construction.
Step 3: Exemplar-Based Iterative Refinement.
To ensure cultural and pragmatic fidelity, an expert
manually refines a single exemplar (Sl,n,t, Tl,n,t)
per subnorm. This exemplar guides LLM-based
refinement of structurally or semantically similar
pairs. The refinement process is repeated until the
quality score Ql,n,t exceeds a predefined threshold,
ensuring consistency across instances.
Step 4: Dialogue Generation and Annotation.
Each refined scenario–situation pair (Sl,n,t, Tl,n,t)
is used to generate a multi-turn dialogue Dl,n,t,
conditioned on the norm category, subnorm, sce-
nario, and situation. All dialogue turns are anno-
tated with norm and reaction labels, resulting in
a fully labeled dataset D suitable for training and
evaluation.
Summary.
This structured pipeline enables the
generation of culturally faithful, pragmatically co-
herent, and richly annotated dialogues. It supports
multilingual benchmarking and serves as a scalable
foundation for norm-aware dialogue modeling.
C.2
Subnorm Generation Prompt
To generate culturally grounded subnorms for the
12 norm categories defined in Section 3.1, we con-
struct 10 subnorms per category for each target
language, yielding 360 subnorms in total. For Ko-
rean, where prior work on normative dialogue mod-
eling is limited, we leverage sociocultural value
indicators from the World Values Survey (WVS
Wave 7, South Korea) as illustrated in Table 15.
For English and Chinese, we adopt the subnorm
definitions from (Li et al., 2023) as semantic an-
chors. To ensure cross-cultural consistency, we
design prompts that adapt these definitions to align
with the Korean-derived subnorms. Table 16 il-
lustrates representative prompt templates used for
this alignment procedure. As a result, we design a
total of 360 subnorms across the 12 categories and
three languages, with illustrative examples shown
in Figure 3. This protocol ensures cross-linguistic
consistency while preserving cultural specificity
and serves as the foundation for downstream sce-
nario construction and dialogue generation.
C.3
Scenario Generation Prompt
To generate culturally grounded data, we first con-
struct concise yet diverse scenarios aligned with a
given subnorm within each social norm category.
For each target language (English, Korean, Chi-
nese), we prompt the model to produce 10 dis-
tinct and contextually appropriate scenarios per
subnorm. The prompts are designed to ensure that

--- Page 16 ---

Section
Content
Target Language
< Korean >
Parameter
< WVS Responses >
Instruction
You are a culturally aware assistant with deep knowledge of Korean social norms
and communication practices. Given a specific social norm category (e.g., Apol-
ogy, Empathy), your task is to generate 10 Korean-specific conversational sub-
norms that reflect the core values and expectations found in Korean society. These
values are derived from nationally representative survey data, including interper-
sonal relationships, formality, group harmony, respect for authority, and emotional
expression.
Please follow these instructions when generating the subnorms:
1. Ensure that each subnorm reflects Korean cultural values and not generic or
universal norms.
2. Specify the context in which the norm should be applied (e.g., school, work-
place, with elders).
3. Include verbal evidence (i.e., example phrases in Korean) that would signal
adherence to the subnorm in dialogue.
4. The subnorms should be actionable and observable in conversation.
Format
Subnorm 1
Subnorm 2
...
Subnorm 10
Table 15: Prompt for korean subnorm generation.
the resulting scenarios are socially plausible and
culturally relevant. As shown in Table 17, these
prompts provide structured guidance for consistent
and culturally sensitive scenario generation.
C.4
Situation Elaboration Prompt
Building on each generated scenario, this prompt
instructs the model to produce a realistic and emo-
tionally coherent situation in 3–5 sentences. The
generated text is expected to reflect culturally ap-
propriate tone, interpersonal dynamics, and nar-
rative plausibility. These situational descriptions
serve as the contextual foundation for downstream
dialogue generation. A representative example is
provided in Table 18.
C.5
Exemplar-Based Refinement Prompt
To improve linguistic quality and pragmatic fidelity,
particularly in low-resource languages, we employ
a one-shot refinement strategy. The model is given
an expert-curated Scenario–Situation pair as an ex-
emplar and instructed to revise a batch of initial
outputs to match the demonstrated level of cultural
appropriateness, contextual richness, and fluency.
Table 19 illustrates the structure and usage of the
refinement prompt.
C.6
Multi-Turn Dialogue Generation Prompt
Given a refined scenario and situation, this prompt
guides the generation of a natural, coherent multi-
turn dialogue that adheres to the specified social
norm. Each dialogue comprises 5 to 15 turns and
is expected to reflect appropriate cultural tone, re-
lational dynamics, and norm-conforming behavior
in a realistic conversational format. An illustrative
example is provided in Table 20.
C.7
Turn-Level Annotation Prompt
To assess norm adherence and communicative func-
tion at the utterance level, this prompt guides the
annotation of each dialogue turn with: (1) a norm
label (Adherence, Violation, Not Relevant), (2)
a communicative function tag (e.g., APO, ACK,
THX), and (3) a brief justification.
This structured annotation facilitates consistent,
turn-level analysis of social behaviors and prag-
matic functions across cultures. An example is
shown in Table 21.

--- Page 17 ---

Section
Content
Target Language
< Chinese | English >
Parameter
< Korean subnorm | Normdial subnorm >
Instruction
You are a culturally adaptive assistant with knowledge of conversational norms
across multiple languages. Provided with a Korean subnorm reflecting a specific
cultural value (e.g., how to apologize, express empathy, or show respect), your
task is to generate a corresponding conversational subnorm in (Chinese | English)
that matches the Korean subnorm in meaning and function.
Use the following instructions:
1. Ensure the subnorm reflects the target language’s cultural norms (i.e., Chinese
or English), not just a literal translation of the Korean input.
2. Specify the context in which the norm should be applied (e.g., school, work-
place, with elders).
3. Include verbal evidence (i.e., example phrases in Chinese or English) that
would signal adherence to the subnorm in dialogue.
4. The subnorms should be actionable and observable in conversation.
Format
Subnorm 1
Subnorm 2
...
Subnorm 10
Table 16: Prompt for chinese and english subnorm generation.
D
Generation & Refinement Examples
This appendix presents full examples of gener-
ated and refined outputs for each social norm
type—Adherence, Violation, and Violation-to-
Resolution (V2R)—across English (EN), Korean
(KR), and Chinese (ZH). For each case, we provide
the subnorm definition, the Scenario–Situation pair
before and after refinement, the corresponding dia-
logue, and representative turn-level annotations.
To facilitate narrative understanding and cross-
cultural comparison, we include aligned figure ref-
erences for each norm type and language. These
visualizations illustrate the transformation process
and demonstrate how refinement enhances linguis-
tic fluency, pragmatic appropriateness, and socio-
cultural alignment. All examples are drawn from
the Apology category.
D.1
Adherence Examples
This section presents example dialogues that ad-
here to social norms from the initial generation
stage, across English, Korean, and Chinese. Al-
though these dialogues already demonstrate norm-
conforming behavior, we apply exemplar-based
refinement to enhance fluency, tonal consistency,
and cultural appropriateness. In high-resource lan-
guages like English, model outputs tend to exhibit
strong cohesion and emotional clarity even before
refinement (Figure 4. The initial dialogue demon-
strates contextual awareness and sincerity with min-
imal pragmatic inconsistencies. In contrast, the
Korean and Chinese examples reveal more pro-
nounced cultural deviations. For instance, Korean
outputs often lack the deference and softened phras-
ing expected in hierarchical contexts (Figure 5,
while Chinese dialogues may omit expressions of
empathy or communal responsibility crucial in pro-
fessional settings (Figure 6. Post-refinement, all
examples show marked improvements in pragmatic
subtlety, such as calibrated tone, culturally appro-
priate honorifics, and clearer interpersonal align-
ment, yielding more realistic and socially congru-
ent conversations. Turn-level annotation is subse-
quently applied to each dialogue, capturing both
norm adherence and speaker intent at the utterance
level. An annotated example illustrating this pro-
cess is shown in Figure 7.
D.2
Violation-to-Resolution(V2R) Examples
This section presents dialogues that initially vi-
olate social norms but subsequently demonstrate
conversational repair through culturally appropri-

--- Page 18 ---

Section
Content
Target Language
< Korean | English | Chinese >
Category
< Apology >
Instruction
Based on the above Subnorm for the given Category, generate 10 distinct and
concise scenarios that could naturally occur in a similar social context within
Country culture. Please ensure realism and cultural grounding. Use names and
honorifics commonly used in the specified country.
Input Format
Category, Subnorm, Instruction, Type
Output Format
Scenario 1
Scenario 2
...
Scenario 10
Table 17: Prompt for scenario generation.
Section
Content
Target Language
< Korean | English | Chinese >
Category
< Apology >
Instruction
Generate a culturally plausible Situation in 3–5 sentences. 1. Use realistic names
and honorifics. 2. Ensure emotional coherence. 3. Depict through action/dialogue,
not explanation.
Input Format
Category, Subnorm, Scenario, Instruction
Output Format
Situation 1
Situation 2
...
Situation 10
Table 18: Prompt for situation elaboration.
ate resolution strategies. These examples reflect
how speakers can realign interactions with social
expectations by acknowledging fault, expressing
remorse, and adopting conciliatory tones—core
mechanisms of the Violation-to-Resolution (V2R)
paradigm. Across English, Korean, and Chinese,
pre-refinement dialogues exhibit typical pragmatic
violations: abrupt interruptions, deflection of re-
sponsibility, or insufficient emotional engagement.
For instance, English outputs show initial breaches
in conversational protocol (e.g., interrupting a pro-
fessor, as illustrated in Figure 8), while Korean
and Chinese versions reveal culturally incongru-
ent justification strategies or failures to express
appropriate deference (Figure 9, 10).
Through
exemplar-guided refinement, these dialogues are
revised to incorporate explicit acknowledgments
of fault, context-sensitive apologies, and relational
mitigation techniques. The resulting interactions
better conform to cultural norms governing hier-
archy, face management, and affective alignment.
Turn-level annotation is applied to each refined di-
alogue to encode both norm adherence and speaker
intent systematically. A representative annotation
example illustrating this process is provided in Fig-
ure 11.
D.3
Violation Examples
This section presents dialogues intentionally con-
structed to illustrate clear violations of social norms
without subsequent repair. These examples are de-
signed to expose pragmatic failures, such as disre-
gard for authority, lack of emotional engagement,
or avoidance of responsibility, and to demonstrate
their effects on interpersonal dynamics.
The selected instances span English, Korean, and

--- Page 19 ---

Section
Content
Instruction
Given a naive Scenario–Situation pair and an expert-refined version, rewrite all
other naive inputs to match the expert style. Do not shorten content. Ensure
cultural richness and tone. Cover a wide range of settings and relationships. Avoid
repetition.
Input Format
Category, Subnorm, 9 Naive Scenarios, 9 Naive Situations, Exemplar
Output Format
Rewritten Scenario 1
Rewritten Situation 1
...
Rewritten Scenario 9
Rewritten Situation 9
Table 19: Prompt for exemplar-based scenario–situation refinement.
Section
Content
Input stages
Category, Subnorm, Scenario, Situation
Instruction
Generate a natural and realistic dialogue between two speakers reflecting the Sce-
nario and Situation above. Write in English. Format each turn with speaker names.
Dialogue should be 5–15 turns long.
Output Format
Name: line of dialogue
Name: line of dialogue
... [END]
Table 20: Prompt for multi-turn dialogue generation.
Chinese, each reflecting culture-specific patterns
of norm deviation. In English, violations appear as
dismissive behavior toward institutional figures (for
example, laughing off a misstep with a principal,
as illustrated in Figure 12). In Korean, pragmatic
breakdowns occur in professional settings where
the speaker avoids apologizing by offering repeated
justifications, diverging from culturally expected
norms of deference (Figure 13). Chinese examples
show minimal accountability and disengaged be-
havior, violating expectations of relational harmony
and respect in hierarchical contexts (Figure 14).
These dialogues are preserved in their original
form to maintain the narrative dissonance they in-
troduce. To support structured analysis, each turn
is annotated with norm adherence and communica-
tive function labels. A representative annotation
example is shown in Figure 15.
E
Evaluation Setup
Human Evaluation and Annotator Agreement
As described in Section 4 and Section 5, we con-
duct four distinct evaluation tasks to assess the
quality, coherence, and norm alignment of gener-
ated outputs. Each task is guided by a dedicated
prompt tailored to its respective objective. The
complete prompt formulations used for generation
and evaluation are provided in the appendix.
To assess model performance in low-resource
cultural settings, we recruited six graduate students
as human annotators, all of whom were indepen-
dent from the research team. Among them, four
were native Korean speakers and two were native
Chinese speakers, each with over ten years of im-
mersion in their respective cultural environments.
Annotators rated model outputs using Likert-scale
judgments across multiple evaluation dimensions,
including fluency, relevance, and social norm ad-
herence. All annotators were compensated fairly in
accordance with ethical research guidelines.
Inter-annotator agreement was calculated using
Krippendorff’s Alpha (α) within each language
group. Korean annotators (n = 4) demonstrated
strong agreement (α = 0.81), and Chinese an-
notators (n = 2) achieved substantial reliability
(α = 0.72), indicating internal consistency and

--- Page 20 ---

Section
Content
Instruction
For each dialogue turn, label: (1) Norm-level adherence (Adherence / Violation
/ Not Relevant), (2) Speaker’s reaction label (e.g., APO, ACK, AGR), and (3)
Explanation for label.
Label Format
Role | Norm Label | Reaction Label | Explanation
Reaction Labels
APO: Apology, ACK: Acknowledgment, AGR: Agreement, DIS: Disagreement,
THX: Thanks, EMP: Empathy, JUS: Justification, SUG: Suggestion, QUE: Ques-
tion, CRT: Criticism, N/A: Not applicable
Table 21: Prompt for turn-level annotation.
cultural coherence in the evaluation process.
IRB Information
This study involved human
participants for data refinement and evaluation
tasks conducted in South Korea. All data used were
synthetic, generated by large language models, and
did not include any personally identifiable informa-
tion. Human experts manually refined the corpus,
and recruited annotators performed human evalua-
tion under informed instructions. No crowdworker
IDs or personal data were collected or stored, and
all annotations were submitted anonymously. Par-
ticipants were provided with fair compensation
according to the guidelines specified in the task
description. Based on national research ethics stan-
dards and in alignment with U.S. federal regulation
45 CFR 46, this study qualifies as exempt from
formal IRB review.
E.1
Dialogue Dataset & Language Models
Descriptions
We use multiple publicly available datasets, each
under specific licenses. DailyDialog is licensed
under CC BY-NC-SA 4.0 (Li et al., 2017). LCCC
is released under the MIT License (Wang et al.,
2022). PROSOCIALDIALOG and SODA are both
licensed under CC-BY-4.0 (Kim et al., 2022, 2023).
NORMDIAL (Li et al., 2023) is publicly released
on GitHub, but no formal license is specified at the
time of writing. All datasets are used in compliance
with their respective licenses for research purposes.
We utilize several open-source language models
under their respective licenses. LLaMA-3 models
are released under the Llama 3 Community License
Agreement (Dubey et al., 2024). Qwen-2.5 models
are distributed under the Apache License 2.0 (Team,
2024). All models are used in accordance with their
licensing terms for research purposes.
In data generation, we used a temperature of 0.7,
while in evaluation, we used zero temperature.
E.2
Refinement Quality (RQ)
To evaluate the effectiveness of exemplar-based
iterative refinement, we define three targeted evalu-
ation dimensions: (1) Norm Alignment, assessing
the degree to which the refined text conforms to
the intended social norm; (2) Language Quality,
measuring improvements in grammaticality, flu-
ency, and stylistic appropriateness; and (3) Seman-
tic Fidelity, evaluating whether the core meaning
and intent of the original input are preserved post-
refinement. These criteria are applied consistently
across human and LLM-based evaluations. Prompt
templates for each dimension are detailed below.
E.2.1
Norm Alignment Prompt.
Norm Alignment Prompt
Evaluation Instruction:
You are a domain expert who evaluates
ONLY Norm Alignment—how well each text
aligns with the given Social Norm. Ignore
grammar or style.
Inputs:
Social Norm: {social_norm}
Initial Text: {initial}
Refined Text: {refined}
Scoring: Give each text an integer score
1–5
(1
=
completely
unrelated,
5
=
perfectly aligned).
E.2.2
Language Quality Prompt.
Language Quality Prompt
Evaluation Instruction:
You
are
a
professional
copy-editor
judging
ONLY
Language
Quality—grammar,
fluency, and naturalness. Ignore meaning
preservation.
Inputs:

--- Page 21 ---

Figure 3: Subnorm examples
Initial Text: {initial}
Refined Text: {refined}
Scoring:
Give
each
text
an
integer
score 1–5 (1 = very poor language, 5 =
native-level fluent).
E.2.3
Semantic Fidelity Prompt.
Semantic Fidelity Prompt
Evaluation Instruction:
You
are
a
bilingual
reviewer
judging
ONLY Semantic Fidelity—how faithfully the
Refined text keeps the original meaning
and intent of the Initial text.
Ignore
style and social-norm fit.
Inputs:
Initial Text: {initial}
Refined Text: {refined}
Scoring: Give each text an integer score
1–5 (1 = meaning lost / contradictory, 5
= meaning identical).
E.3
Dialogue Quality (DQ)
To comprehensively evaluate dialogue quality, we
assess multi-turn conversations across six dimen-
sions that capture linguistic fluency, pragmatic co-
herence, and contextual relevance. The evalua-
tion criteria are as follows: (1) Consistency, which
measures logical coherence across dialogue turns;
(2) Naturalness, which assesses fluency and id-
iomaticity of language; (3) Relevance, which eval-
uates how well the dialogue reflects the given sce-
nario and situation; (4) Emotional Appropriateness,
which measures the suitability of tone and affec-
tive expression; (5) Social Norm Appropriateness,
which determines the degree of alignment with the
intended norm; and (6) Scenario Coherence, which
assesses semantic continuity between the scenario-
situation and the dialogue. Each dimension is eval-
uated using dedicated prompt templates applied to
both human annotators and LLM-based evaluators.
The full set of prompt formulations is provided in
Table 23, 24, 25, 26, 27, and 28.
E.4
Generalization Quality (GQ)
To assess model generalization beyond the train-
ing distribution, we evaluate whether models fine-
tuned on our dataset can produce socially appro-

--- Page 22 ---

priate and contextually coherent responses in out-
of-domain scenarios. Specifically, we use dialogue
contexts sampled from two external benchmarks:
DailyDialog (for English) and LCCC (for Chinese).
Each model is prompted to generate five-turn con-
tinuations for these contexts. The generated outputs
are then evaluated through A/B preference tests
conducted by both human annotators and LLM-
based evaluators. Judgments are based on crite-
ria such as naturalness and alignment with social
norms. To ensure robustness and comparability,
the evaluation spans multiple language model ar-
chitectures. Prompt templates for continuation gen-
eration and preference elicitation are provided in
Table 29.
F
Comparative Analysis of Generation in
Low-Resource Settings
F.1
Examples of Common Errors
To better understand the limitations of prompt-only
generation in low-resource languages, we present
qualitative examples of common errors observed
in dialogues from typologically diverse languages.
These examples underscore the challenges that
arise when language models are required to gener-
ate pragmatically appropriate outputs in sociocul-
turally complex settings without sufficient ground-
ing.
Figure 16 illustrates two prevalent generation
errors: (1) lexical redundancy, where intensifiers
or formulaic actions such as “lowered his head and
said” are repeated across multiple turns, and (2)
tone mismatches, where informal phrasing appears
in contexts that require formal or respectful speech
levels. Both issues indicate a lack of contextual
awareness regarding interpersonal roles and emo-
tional nuance, which are crucial in conversation
norms for languages with rich honorific systems.
Figure 17 presents analogous issues. We observe
(1) emotional redundancy, with exaggerated repeti-
tions of intensifiers (e.g., "really really very very")
that undermine sincerity; (2) honorific inconsis-
tency, where formal pronouns are combined with
casual address terms within the same sentence; and
(3) register mixing, where archaic written forms are
abruptly followed by colloquial speech. These in-
consistencies reflect the model’s difficulty in main-
taining coherent style and role-appropriate polite-
ness strategies.
Collectively, these examples provide qualita-
tive evidence for the sociolinguistic brittleness
of prompt-only methods in languages with mor-
phosyntactic complexity and hierarchical speech
conventions. They further motivate our refinement-
based framework, which explicitly encodes cultural
subnorms and stylistic expectations to produce flu-
ent, contextually aligned, and socially coherent
outputs in low-resource settings.
F.2
Additional Pilot Refinement Experiment
We recognize that languages with divergent prag-
matic and honorific systems (e.g., Arabic, Swahili,
Hindi) pose additional challenges. In such cases,
our exemplar-based refinement component is cru-
cial for the early injection of sociocultural con-
straints, especially in the absence of large anno-
tated corpora. To test generalizability beyond East
Asian typologies, we conducted pilot refinement
in Malay and Urdu, two pragmatically distinct lan-
guages. Using the same evaluation setup as in
Table 4, we find the results align closely with those
from our main experiments, shown in Table 22.
These findings demonstrate the framework’s gener-
alizability to typologically and culturally distinct
languages and will be included in the camera-ready
version as initial evidence of broader applicabil-
ity. We plan to extend to additional low-resource
languages, including Arabic and Swahili.

--- Page 23 ---

Input: Languages L, Norm Categories C, Dialogue Types T
Output: Annotated Dialogues D
foreach language l in L do
foreach category c in C do
Generate subnorm set Nl,c;
end
end
foreach language l in L do
foreach category c in C do
foreach subnorm n in Nl,c do
foreach dialogue type t in T do
Generate Scenario Sl,n,t;
Generate Situation Tl,n,t based on Sl,n,t;
end
end
end
end
foreach language l in L do
foreach category c in C do
foreach subnorm n in Nl,c do
Expert manually refines exemplar pair El,n;
repeat
Refine Scenario-Situation pairs (S, T)l,n,∗aligned to El,n;
Evaluate refinement quality Ql,n;
until Refinement Quality Ql,n meets threshold;
end
end
end
foreach refined pair (S, T)l,n,t do
Generate Dialogue Dl,n,t using (c, n, S, T) as input;
Annotate each turn in Dl,n,t with norm and reaction labels;
end
return All annotated dialogues D
Algorithm 1: Multicultural social norm dialogue Generation Pipeline
Language
Condition
RQ (GPT-4o) Avg.
RQ (Human Evaluation) Avg.
Malay
Initial
3.623
2.666
Refined
4.830
4.333
Urdu
Initial
3.217
3.166
Refined
4.777
4.222
Table 22: Refinement quality (RQ) evaluation in Malay and Urdu. Scores are based on a 5-point Likert scale,
averaged over all evaluation dimensions and aggregated across both LLM-based and human raters.

--- Page 24 ---

Figure 4: Adherence norm example (EN)
Consistency Prompt
Section
Content
Evaluation Instruction
You are a professional dataset auditor for social-norm dialogues. You are
given a culture category. Your task is to evaluate only the Consistency of
the dialogue. Ignore grammar, fluency, or style. Focus only on whether the
dialogue is logically and contextually consistent throughout.
Parameter
culture, norm, dialogue
Evaluation Question
Assuming the dialogue adheres to the given social norm, are all utterances
logically and emotionally coherent with one another?
– Do characters maintain a consistent attitude, tone, and perspective through-
out?
– Are there any contradictions or abrupt shifts in reasoning, emotion, or
information?
– Does the dialogue flow smoothly without unexpected or unjustified changes?
Scoring Criteria
1 = Major inconsistencies or contradictions
3 = Somewhat inconsistent or awkward transitions
5 = Fully consistent and coherent throughout
Table 23: Evaluation prompt structure for Consistency.

--- Page 25 ---

Figure 5: Adherence norm example (KR)

--- Page 26 ---

Figure 6: Adherence norm example (ZH)

--- Page 27 ---

Figure 7: Turn-level annotated dialogue example – Adherence

--- Page 28 ---

Figure 8: Violation-to-resolution(V2R) norm example (EN)
Naturalness Prompt
Section
Content
Evaluation Instruction
You are a professional dataset auditor for social-norm dialogues. Your task is
to evaluate only the Naturalness of the dialogue. Ignore whether the response
is factually correct or norm-appropriate. Focus on how naturally the dialogue
would sound to a native speaker.
Parameter
dialogue
Evaluation Question
Does the dialogue sound natural and fluent as if spoken by native speakers in
a real-world situation?
– Are the expressions, tone, and word choices contextually appropriate and
idiomatic?
– Do the conversational turns flow smoothly without sounding robotic or overly
scripted?
– Are there any awkward phrases or unnatural sentence structures?
Scoring Criteria
1 = Extremely unnatural or robotic
3 = Somewhat awkward or artificial
5 = Very natural, fluent, and human-like
Table 24: Evaluation prompt structure for Naturalness.

--- Page 29 ---

Figure 9: Violation-to-resolution(V2R) norm example (KR)

--- Page 30 ---

Figure 10: Violation-to-resolution(V2R) norm example (ZH)

--- Page 31 ---

Figure 11: Turn-level annotated dialogue example – V2R

--- Page 32 ---

Figure 12: Violation norm example (EN)
Relevance Prompt
Section
Content
Evaluation Instruction
You are a professional dataset auditor for social-norm dialogues. You are
given a culture category.
Your task is to evaluate only the Relevance of the dialogue to the provided
Scenario and Situation. Ignore grammar, fluency, or logical consistency.
Focus on whether the dialogue reflects the key intentions, emotions, and
context described in the Scenario and Situation.
Parameter
culture, scenario, situation, dialogue
Evaluation Question
Does the dialogue appropriately address and reflect the actions, intentions,
and emotional context presented in the scenario and situation?
– Are the key elements of the situation represented in the conversation (e.g.,
apology, embarrassment, disagreement)?
– Do the characters react in a way that makes sense for the described context?
– Are any critical actions or emotional responses missing from the dialogue?
Scoring Criteria
1 = Dialogue is mostly irrelevant to the situation
3 = Partially relevant, with some elements missing or misaligned
5 = Dialogue is highly relevant and faithfully represents the described situation
Table 25: Evaluation prompt structure for Relevance.

--- Page 33 ---

Figure 13: Violation norm example (KR)

--- Page 34 ---

Figure 14: Violation norm example (ZH)

--- Page 35 ---

Figure 15: Turn-level annotated dialogue example – Violation

--- Page 36 ---

Emotional Appropriateness Prompt
Section
Content
Evaluation Instruction
You are a professional dataset auditor for social-norm dialogues. You are
given a culture category.
Your task is to evaluate only the Emotional Appropriateness of the dialogue.
Ignore grammar, norm correctness, or logical structure. Focus on whether
the tone, expressions, and emotional language used in the dialogue match the
emotional context of the situation.
Parameter
culture, scenario, situation, dialogue
Evaluation Question
Does the emotional tone, choice of words, and manner of speaking in the
dialogue align appropriately with the emotional context of the situation?
– Does the dialogue reflect the expected emotional state (e.g., tension, regret,
embarrassment, relief) implied in the situation?
– Are the expressions and tone suitable for the described emotional stakes?
– Is there any emotional mismatch that makes the dialogue feel unnatural or
inappropriate?
Scoring Criteria
1 = Emotionally disconnected or inappropriate
3 = Emotion is somewhat present but weak or inconsistent
5 = Emotional tone is highly appropriate and enhances the realism
Table 26: Evaluation prompt structure for Emotional Appropriateness.
Social Norm Appropriateness Prompt
Section
Content
Evaluation Instruction
You are a professional dataset auditor for social-norm dialogues. You are
given a culture category.
Your task is to evaluate only the Social Norm Appropriateness of the dialogue.
Assess how well the conversation reflects the given social norm, and categorize
the degree of adherence.
Parameter
culture, norm, dialogue
Evaluation Question
Based on the given social norm, how well does the dialogue align with it?
– Does the dialogue completely follow the norm?
– Does it violate the norm?
– Does it violate the norm but later attempt to resolve it?
– Is the behavior partially aligned with the norm?
Classification Criteria
1 = Fully Violated
2 = Partially Violated
3 = Violation then Resolved
4 = Partially Adherence
5 = Fully Adherence
Table 27: Evaluation prompt structure for Social Norm Appropriateness.

--- Page 37 ---

Scenario Coherence Prompt
Section
Content
Evaluation Instruction
You are a professional dataset auditor for social-norm dialogues. Your task
is to evaluate only the Scenario Coherence of the dialogue. Ignore grammar
or emotional tone. Focus on whether the dialogue logically and smoothly
follows the sequence of events described in the scenario.
Parameter
culture, scenario, situation, dialogue
Evaluation Question
Does the dialogue unfold in a way that aligns with the narrative structure and
event flow of the scenario?
– Is there a smooth and coherent transition from the described situation into
the dialogue?
– Are there any gaps, jumps, or inconsistencies between what the scenario sets
up and what happens in the conversation?
– Does the dialogue logically follow the order of events and emotional pacing
described in the scenario (or situation)?
Scoring Criteria
1 = Dialogue and scenario (or situation) are disconnected or contradictory
3 = Some transitions or event links are missing or unclear
5 = Dialogue flows logically and coherently from the scenario (or situation)
Table 28: Evaluation prompt structure for Scenario Coherence.
Task
Prompt Template
Continuation Generation
You are continuing the following human-human dialogue. Continue the
conversation with 5 additional turns naturally and coherently.
Dialogue so far: {context}
Continue the dialogue:
A/B Evaluation
You are an evaluator. Below is a dialogue context followed by two
different continuations (A and B). Choose which continuation is more
appropriate, natural, coherent, and socially norm-aligned. Respond only
with "A" or "B".
Context: {context}
Response A: {output_a}
Response B: {output_b}
Which is better? Respond with A or B only.
Table 29: Prompt templates used for generalization quality evaluation.

--- Page 38 ---

Figure 16: Examples of common generation failures in Korean, illustrating two representative issues: (1) lexical
redundancy in emotionally sensitive contexts, and (2) tone mismatches arising from inconsistent use of honorific
and casual forms.

--- Page 39 ---

Figure 17: Examples of generation failures in Chinese, illustrating three common error types: (1) emotional
redundancy from repeated intensifiers, (2) honorific inconsistency due to mixed formal and informal address terms,
and (3) register mismatches from combining classical written expressions with colloquial speech.

```
