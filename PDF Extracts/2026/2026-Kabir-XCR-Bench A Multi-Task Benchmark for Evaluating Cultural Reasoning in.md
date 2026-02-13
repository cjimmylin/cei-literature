---
title: "2026-Kabir-XCR-Bench A Multi-Task Benchmark for Evaluating Cultural Reasoning in - PDF Extract"
source_pdf: "2026-Kabir-XCR-Bench A Multi-Task Benchmark for Evaluating Cultural Reasoning in.pdf"
pages: 30
extracted_at: "2026-02-13T09:50:30.760347"
---

# PDF Extract: 2026-Kabir-XCR-Bench A Multi-Task Benchmark for Evaluating Cultural Reasoning in

**Source PDF:** 2026-Kabir-XCR-Bench A Multi-Task Benchmark for Evaluating Cultural Reasoning in.pdf
**Total Pages:** 30

---

## Content

```
--- Page 1 ---

XCR-Bench: A Multi-Task Benchmark for Evaluating Cultural
Reasoning in LLMs
Mohsinul Kabir1,2, Tasnim Ahmed3, Md Mezbaur Rahman4,
Shaoxiong Ji5,6, Hassan Alhuzali7, Sophia Ananiadou1,2
1Department of Computer Science, National Centre for Text Mining,
The University of Manchester
2ELLIS Manchester
3School of Computing, Queen’s University, Ontario, Canada
4Computer Science, University of Illinois Chicago
5ELLIS Institute Finland
6University of Turku
7Department of Computer Science and Artificial Intelligence,
Umm Al-Qura University, Makkah, Saudi Arabia
Correspondence: {mdmohsinul.kabir, sophia.ananiadou}@manchester.ac.uk
Abstract
Cross-cultural competence in large language
models (LLMs) requires the ability to iden-
tify Culture-Specific Items (CSIs) and to adapt
them appropriately across cultural contexts.
Progress in evaluating this capability has been
constrained by the scarcity of high-quality CSI-
annotated corpora with parallel cross-cultural
sentence pairs. To address this limitation, we
introduce XCR-Bench, a Cross(X)-Cultural
Reasoning Benchmark consisting of 4.9k par-
allel sentences and 1, 098 unique CSIs, span-
ning three distinct reasoning tasks with corre-
sponding evaluation metrics. Our corpus inte-
grates Newmark’s CSI framework with Hall’s
Triad of Culture, enabling systematic analysis
of cultural reasoning beyond surface-level ar-
tifacts and into semi-visible and invisible cul-
tural elements such as social norms, beliefs,
and values. Our findings show that state-of-
the-art LLMs exhibit consistent weaknesses in
identifying and adapting CSIs related to social
etiquette and cultural reference. Additionally,
we find evidence that LLMs encode regional
and ethno-religious biases even within a sin-
gle linguistic setting during cultural adaptation.
We release our corpus and code to facilitate fu-
ture research on cross-cultural NLP.1
1
Introduction
Large Language Models (LLMs) have been
widely documented to exhibit a pronounced Anglo-
American, or Western cultural bias in their outputs,
predominantly reflecting values and perspectives
associated with the US and UK (Johnson et al.,
2022; Dunn et al., 2024; Atari et al., 2023). This
1Code & Corpus: github.com/mohsinulkabir14/xcr_bench
bias is often attributed to the West-centric com-
position of both their training data and the anno-
tators involved in their development, making it a
predictable artifact of their training process (Kabir
et al., 2025c; Navigli et al., 2023). However, recent
work has challenged a common implicit assump-
tion in this line of research: the presence of cultural
bias does not necessarily imply strong performance
or competence within the corresponding cultural
context (Saha et al., 2025). This observation raises
a more fundamental question: how should “cul-
ture”be meaningfully measured in LLMs?
Moving beyond performance within predomi-
nantly Western cultural settings, a more challeng-
ing and practically consequential problem is eval-
uating the cross-cultural competence of LLMs.
Evaluating cross-cultural competence requires nav-
igating differences in common ground and about-
ness that go beyond surface-level linguistic or
stylistic variation (Hershcovich et al., 2022). Ex-
isting studies largely adopt intrinsic evaluation, fo-
cusing on isolated assessments of cultural knowl-
edge, while extrinsic evaluation better captures
how cultural competence manifests in realistic
user-centric interactions (Bhatt and Diaz, 2024). A
foundational concept in this area is the Culture-
Specific Items (CSIs), introduced by Newmark
(1988), which encompass cultural factors ranging
from material artefacts (e.g., food, clothing) to so-
cial and ideological constructs (e.g., institutions,
values) and are crucial for cross-cultural communi-
cation. Building on this notion, subsequent work
models culture as measurable facets and evalu-
ates LLMs by probing these facets as proxies for
cultural awareness (Adilazuarda et al., 2024; Rao
1
arXiv:2601.14063v1  [cs.CL]  20 Jan 2026

--- Page 2 ---

et al., 2024).
However, existing evaluations of
cross-cultural awareness largely rely on machine
translation–based settings (Yao et al., 2024) or iso-
lated cultural substitutions such as dialog or recipe
(Singh et al., 2024; Cao et al., 2024), primarily
due to the high cost of constructing realistic cross-
culture CSI pairs.
A meaningful evaluation of
cross-cultural competence in LLMs requires as-
sessing their ability to reason about and adapt CSIs
across diverse realistic cultural contexts - a set-
ting that remains largely underexplored (Guo et al.,
2025).
Another line of work draws on Hall’s Iceberg
(Triad) Model of Culture (Hall, 1976), which
distinguishes between Visible (technical), Semi-
visible (formal), and Invisible (informal) cultural
levels. While the visible level captures observable
behaviors, the semi-visible and invisible levels cor-
respond to the underlying norms, values, and be-
liefs that structure habits and behavior in culture.
Despite their conceptual relevance, a clear theoret-
ical and empirical link between Newmark’s notion
of Culture-Specific Items (CSIs) and Hall’s cul-
tural levels remains absent. Specifically, there is
no established typology or annotated resource that
situates CSIs within Hall’s triadic framework. As
a result, existing evaluations cannot assess whether
LLMs are capable of detecting and adapting CSIs
across different cultural depths, nor whether mod-
els move beyond surface-level cultural cues to en-
gage with underlying values and beliefs.
In this study, we argue that cultural compe-
tence in LLMs extends beyond translation to the
ability to recognize, interpret, and adapt Culture-
Specific Items (CSIs) across cultures. We present a
dataset of Western (US/UK) culture-specific items
(CSIs) in realistic scenarios. It includes detailed
annotations such as CSI categories, CSI-Hall map-
pings, and Hall’s cultural levels, with a focus
on the semi-visible and invisible layers of Hall’s
triad. Based on these annotations, we define two
tasks, CSI Identification and CSI Prediction, to as-
sess LLMs’ reasoning of Western cultural knowl-
edge.
We further construct culturally adaptable
CSI pairs for Chinese, Arabic, and Bengali, with
Bengali additionally divided into West Bengal (In-
dia) and Bangladeshi variants to capture regional
variation. This enables a third task, CSI Adapta-
tion, focused explicitly on cross-cultural reason-
ing. We propose task-specific evaluation metrics
and release this resource as the Cross(X)-Cultural
Reasoning Benchmark (XCR-Bench). All three
tasks operationalize cultural reasoning, as they re-
quire models to follow a cognitive process to in-
terpret cultural cues, evaluate contextual appropri-
ateness, and justify culturally grounded decisions
rather than performing surface-level pattern match-
ing (Huang and Chang, 2023).
Using XCR-Bench, we conduct a systematic
evaluation of state-of-the-art LLMs. While mod-
els demonstrate relatively strong performance in
predicting Western cultural facets, they exhibit sub-
stantially weaker performance in identifying CSIs
and adapting them across cultural contexts. More-
over, our results reveal pronounced regional bias
within a single language, with models showing un-
even adaptation performance across Bengali cul-
tural variants. Together, these findings highlight
persistent limitations in LLMs’ cross-cultural rea-
soning abilities.
In summary, our contributions are as follows:
• We connect Newmark’s concept of Culture-
Specific Items (CSIs) with Hall’s Triad of cul-
ture by creating and publicly releasing a real-
istic, culturally diverse corpus. This corpus
features Western-source CSIs that are manu-
ally annotated with adaptable cross-cultural
CSI pairs for four target cultures; these are
mapped to Newmark’s CSI categories and
Hall’s cultural levels, focusing especially on
the Semi-visible and Invisible layers.
• We formulate cultural competence in LLMs
as a cross-cultural reasoning problem and
evaluate it through three unique evaluation
tasks with tailored metrics in both intra-
lingual and inter-lingual settings, going be-
yond conventional machine translation–based
evaluation.
• We provide a thorough empirical analysis of
LLMs’ cultural proficiency and bias, inves-
tigating their capabilities in causal reason-
ing, adaptability, and generalizing culture-
specific content across diverse contexts.
2
XCR-Bench Corpus
Due to the nuanced nature of CSIs, we incorporate
human annotation and validation throughout XCR-
Bench construction. The process comprises two
phases: (1) building the base corpus with Western
CSIs annotated by CSI categories and Hall’s cul-
tural levels; and (2) annotating adaptable CSI pairs
for four target cultures (Chinese, Arabic, Bengali
from West Bengal and Bangladesh) to form a par-
2

--- Page 3 ---

CSI & Cultural Context 
Extraction
CANDLE
CULTURAL 
ATLAS
Sentence Generation
CSI Category & Hall's 
Level Annotation
CSI Extracted:Wedding Ring.
Cultural Context:A wedding ring is a finger ring
indicating that its wearer is married, a practice
originally used in ancient Rome during marriage
Representative:Wearing a wedding ring is a
common symbol of marriage in Western cultures.
WIKIPEDIA
Representative
Cultural Concept
Cultural Context
  CSI
Newmark 
(1988)
What is the category of the elected
sentence? 
Newmark 
(1988)
Taxonomy from 
Liu el al. (2025)
Social
Tradition
Hall's Iceberg 
Model (1976)
Customs: 
Semi-Visible
Sentence 1
Sentence 2
(Best)
Sentence 3
Prompt:Given the following cultural context, write a 
realistic sentence that naturally incorporates the CSI 
as it would be used in everyday communication.
Input: {CSI, Cultural Context} 
Elected Sentence:She never takes off her <CSI>
wedding ring </CSI>, a symbol of the love and
commitment she shares with her husband.
Human Evaluation
What is the Hall's Level of the 
elected sentence?
GPT-4o
Claude 3.7 
Sonnet
DeepSeek-R1
Figure 1: XCR-Bench corpus creation and annotation pipeline. (1) Culture-specific items (CSIs) and their contexts
are extracted from well-known cultural databases. (2) Sentences are generated using LLMs and filtered for accuracy
and fluency. (3) Each sentence is annotated with a CSI category and mapped to Hall’s cultural levels.
allel corpus.
2.1
Construction of Base XCR-Bench Corpus
Figure 1 provides an overview of the base XCR-
Bench construction pipeline. It includes: (1) CSI
and cultural context Extraction, (2) sentence gen-
eration with the extracted CSI, and (3) annotating
the CSI to produce the category and Hall’s level.
CSI & Cultural Context Extraction
The first step in corpus construction involves identi-
fying and extracting Culture-Specific Items (CSIs)
representative of US and UK cultures.
To this
end, we leverage two structured cultural knowl-
edge resources: CANDLE2 and Cultural Atlas3 .
CANDLE provides high-quality cultural common-
sense knowledge (CCSK), comprising 1.1M asser-
tions organized into 60K coherent clusters, while
Cultural Atlas offers curated descriptions of multi-
cultural norms derived from extensive global com-
munity interviews and rigorous validation (Rao
et al., 2024).
Both resources present cultural
knowledge in factual form (e.g., CANDLE states
a Representative cultural concept as “In the USA,
people wear their wedding rings on the ring fin-
ger of their left hand”), with Cultural Atlas fur-
ther organizing information into thematic sections
such as Core Concepts, Communication, and Busi-
ness Culture. We crawl cultural facts from these
platforms, primarily focusing on the US and UK,
supplemented by a select few highly relevant ex-
amples from Europe. We then manually extract
2https://commonsense.scads.ai/candle/
3https://culturalatlas.sbs.com.au/
CSIs by mapping these statements to the CSI cat-
egories proposed by Newmark (1988) (described
in Appendix B.1).
For each extracted CSI, we
then retrieve a high-level cultural definition from
Wikipedia to contextualize its usage. This process
yields a set of CSIs paired with their corresponding
cultural contexts.
Sentence Generation incorporating CSIs
In the second step, we generate realistic sentences
reflecting everyday communication by prompting
GPT-4o, Claude-3.7-Sonnet, and DeepSeek-R1
with each CSI and its corresponding cultural con-
text, as illustrated in Step 2 of Figure 1.
Each
model produces a candidate sentence, resulting in
three alternatives per CSI. Two human annotators
then evaluate these candidates based on three crite-
ria: accuracy, fluency, and realism, and select the
highest-scoring one. We explicitly emphasize re-
alism in our prompt and selection, as real-world
cross-cultural contexts are inherently complex and
essential for assessing cross-cultural competence
(Rauba et al., 2024). This process yields a set of
culturally grounded, naturalistic sentences aligned
with the original CSI-context pairs. For experimen-
tal convenience, the selected sentence is annotated
by enclosing the CSI within <CSI> and </CSI>
tags.
CSI Category and Hall’s Level Annotation
Finally, we categorize each CSI based on its cul-
tural context and the generated sentence from
Steps 1 and 2, rather than at extraction time, as
a CSI’s category under Newmark’s taxonomy can
shift with contextual usage. For instance, jeans
3

--- Page 4 ---

falls under Material Culture (Category 2) in “He
wore a pair of <CSI>jeans</CSI> with a white
T-shirt”, but under Social Culture (Category 3) in
“Wearing <CSI>jeans</CSI> to the office on
Friday felt appropriate because of the company’s
casual dress norm,” where it reflects workplace
norms rather than mere attire. Although we use
Newmark’s CSI categories as a foundational frame-
work, their broad scope often merges diverse cul-
tural elements. To address this, we incorporate the
cultural taxonomy from Liu et al. (2025), mapping
its ideational and social dimensions to Newmark’s
Categories 3 (Social Culture) and 4 (Organizations,
Customs, and Ideas), respectively. Annotations at
this stage achieve a Cohen’s kappa of 0.68, indi-
cating substantial agreement between the two an-
notators.
We further annotate each CSI with its cor-
responding Hall cultural level, independently of
Newmark’s categorization:
for instance, food-
related CSIs may encode formal or informal cul-
tural meanings without functioning as material
artefacts (e.g., Social Tradition:
“Let’s grab a
<CSI>coffee</CSI> and catch up sometime!”).
This context-sensitive treatment aligns with Sko-
pos Theory (Schäffner, 1997), which argues that
the function of an element in the target commu-
nicative situation, rather than its surface form, de-
termines its cultural role. Accordingly, we assign
each CSI one of Hall’s three levels of cultural vis-
ibility (e.g. Visible, Semi-visible, Invisible). The
mapping of cultural elements with Hall’s Triad is
provided in Table 8. Annotation of Hall’s cultural
elements yields a Cohen’s kappa of 0.64 between
the two annotators.
2.2
Construction of the Parallel Corpus
Each instance in our dataset is annotated with cul-
turally adapted counterparts in four target cultures:
Chinese, Arabic, and Bengali (two variants). The
objective is to construct culturally equivalent in-
stances of the Western CSIs from the base XCR-
Bench corpus.
Because cultural equivalence is
inherently subjective and cannot be treated as a
categorical labeling problem, we adopt an adjudi-
cated annotation protocol (Klie et al., 2024). For
example, the CSI long drive in the sentence “The
family is planning a <CSI>long drive</CSI> to re-
lax after a hectic week” may be adapted in Ben-
gali as rickshaw rides and street food, or retained
as long drive, reflecting contemporary urban prac-
tices. Both adaptations are culturally valid. Rather
than treating such variation as disagreement, we in-
terpret it as cultural pluralism (Berry, 1974). Con-
sequently, conventional agreement-based metrics
(e.g., IAA) are not appropriate for this setting.
Two native annotators per target culture inde-
pendently produce adaptations following detailed
guidelines, with disagreements resolved through
discussion and expert moderation. An expert an-
notator with cultural and anthropological expertise
oversees the process and provides final adjudica-
tion. Full details of the annotation procedure and
annotator qualifications are provided in Section D.
We follow Newmark’s framework for cultural
equivalence (Newmark, 1988) and instruct annota-
tors to identify one of four equivalence types when
adapting CSIs to their native culture: (1) a direct
equivalent, where available; (2) a functionally sim-
ilar equivalent; (3) a neutral expression when no
cultural equivalent exists; or (4) a Non-transferable
label when the CSI is culturally inappropriate
or conflicts with local norms (e.g., “They met
through a <CSI>dating app</CSI>”, which
may be non-transferable in certain Arab cultural
contexts). In addition to detailed annotation guide-
lines (demonstrated in Appendix D.1), annotators
are provided with relevant cultural information on
rituals and traditions extracted from CANDLE
and Cultural Atlas. Annotators are further encour-
aged to modify the sentence structure as necessary
to ensure that both intra- and inter-lingual adapta-
tions remain coherent and culturally appropriate in
the target context.
2.3
Dataset Analysis
The XCR-Bench corpus comprises 4,136 paral-
lel sentences spanning 4 distinct cultures and 2 re-
gional variants. It contains 1,098 unique Culture-
Specific Items (CSIs), distributed across 7 CSI
categories. Table 6 situates XCR-Bench in rela-
tion to existing datasets for culture-aware bench-
marking. Most prior datasets in this area primar-
ily provide translation pairs, with CAMT (Yao
et al., 2024) being the closest in scope, as it in-
cludes cross-cultural CSI pairs for a subset of
its data. In contrast, XCR-Bench supports both
reasoning-oriented and culturally aware adaptation
evaluations by offering paired intra-lingual and
inter-lingual annotations. Notably, XCR-Bench
is the first dataset to provide extensive annotations
aligned with Hall’s triadic model of culture, with
explicit emphasis on the Semi-visible and Invisi-
ble layers that encode beliefs, values, and social
4

--- Page 5 ---

norms. Combined with our three task formulations,
this design enables the evaluation of cultural rea-
soning as a cognitive process involving evidence-
based judgment over culturally situated knowledge,
rather than translation-focused competence alone.
Detailed properties of our dataset are provided in
Appendix E.
3
Cross-Cultural Reasoning Evaluation
3.1
CSI Identification
For the CSI Identification task, we remove the
<CSI> tags from the base XCR-Bench sentences
and prompt LLMs to identify the term(s) that are
specific to Western (specifically US/UK) culture
and salient for cross-cultural communication. To
ensure a consistent interpretation of the task, we
provide the definition of Culture-Specific Items
(CSIs as defined by Newmark (1988)) within the
prompt during inference.
3.2
CSI Prediction
For the CSI Prediction task, we replace the CSI
spans in the base XCR-Bench sentences with a
[MASK] token enclosed within <CSI> tags, and
prompt models to predict culturally appropriate
terms that reflect Western (US/UK) cultural usage.
As in the CSI Identification task, we include a brief
definition of CSIs in the prompt to ensure a consis-
tent interpretation of the task.
3.3
CSI Adaptation
In the CSI Adaptation task, we present LLMs with
the base XCR-Bench sentences containing explic-
itly marked <CSI> spans and prompt them to
adapt these CSIs to Arabic, Bengali, or Chinese
cultural contexts. For each instance, models are re-
quired to produce both intra-lingual (English) and
inter-lingual (target-language) adaptations. In ad-
dition, we ask models to explicitly indicate which
of Newmark’s twelve cultural adaptation strategies
(e.g., transference, equivalence, etc. full details in
Appendix C.1) they employ when adapting each
CSI.
Together, these three tasks operationalize differ-
ent levels of cultural reasoning in LLMs, ranging
from interpretive identification and contextual in-
ference to cross-cultural abstraction and decision-
making. Our prompts used for each task are pre-
sented in Appendix H.
3.4
Evaluation Metrics
We evaluate model performance on the two tasks:
CSI Identification and Prediction, using a combina-
tion of strict (“hard”) and lenient (“soft”) metrics
designed to capture different aspects of correctness.
The hard metrics penalize any deviation from the
ground truth, while the soft metrics provide graded
credit for semantically or superficially similar out-
puts, which is crucial for culturally nuanced tasks.
In Cultural Adaptation task, direct string match-
ing is insufficient, as valid adaptations may use
contextually congruent alternatives rather than lit-
eral match. We therefore evaluate at two comple-
mentary levels using BERTScore: CSIbert assesses
the semantic quality of individual adapted terms
(within <CSI> tags), while SENTbert measures
overall meaning preservation of the entire adapted
sentence. A summary of all metrics is provided in
Table 1 with detailed definitions and computation
provided in Appendix F.
3.5
Models and Prompting Technique
We evaluate a diverse set of recent multilingual
LLMs, including both proprietary and open-source
models:
GPT-4o, Qwen-2.5-Max, Gemini-2.0-
Flash, Claude-3.7-Sonnet, DeepSeek-R1 (671B),
LLaMA-3.3 (70B), OLMo-2-32B, and DeepSeek-
R1-Distill-Qwen-32B. All models are evaluated
across the full suite of tasks. For prompting, we
adopt part of the Expert Prompting strategy pro-
posed by Xu et al. (2023), which has been shown to
elicit higher-quality responses than vanilla prompt-
ing.
4
Results & Analysis
The CSI Identification and Prediction tasks are
both designed to assess LLMs’ reasoning over
Western cultural knowledge and their ability to dis-
tinguish culture-specific elements. We therefore
analyze and compare the results of these two tasks
together.
4.1
CSI Identification & Prediction
LLMs perform substantially better on CSI Pre-
diction than on CSI Identification. Table 2 re-
ports results for both tasks under hard and soft
evaluation metrics. Overall, most models achieve
relatively strong performance on the CSI Predic-
tion task, while exhibiting notably weaker perfor-
mance on CSI Identification. We hypothesize that
this disparity arises because CSI Prediction closely
5

--- Page 6 ---

Task
Metric
Description
Formula/Details
CSI Identification
Hard Identification of CSI (HI-CSI)
Strict matching using exact string equal-
ity.
simexact(g, m) = I[g = m], where
g and m denote gold and model-
predicted CSI spans.
Soft Identification of CSI (SI-CSI)
Accounts for minor variations via nor-
malized Levenshtein similarity, with
optimal alignment using the Hungarian
algorithm.
s(g, m) = 1 −
dLev(g,m)
max(|g|,|m|); sentence-
level soft F1 based on alignment.
CSI Prediction
Hard Prediction of CSI (HP-CSI)
Case-insensitive exact match between
gold and predicted spans. Span refers
to text inside the enclosed <CSI> and
</CSI> tags.
simexact(g, p)
=
I[lower(g)
=
lower(p)], where g and p denote gold
and predicted spans.
Soft Prediction of CSI (SP-CSI)
Cosine similarity between Sentence-
BERT
embeddings
for
para-
phrases/synonyms.
simsem(g, p) = cos
(
e(g), e(p)
)
, using
all-mpnet-base-v2 (Song et al., 2020).
CSI Adaptation
CSI-Level Semantic Similarity (CSIbert)
CSI-level BERTScore F1 for aligned
CSI spans.
CSIbert = 1
n
∑n
i=1 F1bert(gi, oi), where
G = {gi} and O = {oi} are gold
and predicted CSI spans extracted from
<CSI> tags, respectively.
Sentence-Level Semantic Similarity (SENTbert)
Assesses
sentence-level
meaning
preservation using BERTScore F1.
SENTbert
=
F1bert
(
sout, sgt)
, where
sout and sgt are model-generated and
ground-truth sentences.
Table 1: Evaluation metrics for the three cross-cultural reasoning tasks: CSI Identification, Prediction, and Adap-
tation. Hard metrics enforce strict correctness, while soft metrics provide graded credit for semantically or superfi-
cially similar outputs.
Cultural
 Reference
Cultural
 Stereotype
Cultural
 Value
Social
 Etiquette
Social
 Tradition
Sports
 Tradition
Workplace
 Culture
GPT-4o
Qwen-2.5-Max
Gemini-2.0-Flash
Claude-3.7-Sonnet
Deepseek-R1
Llama-3.3
OLMo-2-32B
DeepSeek-R1-
Distill-Qwen-32B
56.9
76.9
55.9
42.6
60.9
67.6
64.6
57.1
75.7
56.9
48.6
63.1
67.9
64.3
59.5
84.0
54.9
38.3
61.2
66.9
59.7
59.7
80.9
58.6
43.8
64.1
70.5
67.8
60.0
75.8
59.7
45.9
63.7
62.1
65.9
51.5
63.4
46.2
39.2
49.3
58.9
50.1
54.5
76.5
61.5
40.5
62.1
61.8
68.6
52.1
70.2
49.0
46.2
58.1
56.9
60.1
40
50
60
70
80
Score
(a) CSI Identification (SI-CSI)
Cultural
 Reference
Cultural
 Stereotype
Cultural
 Value
Social
 Etiquette
Social
 Tradition
Sports
 Tradition
Workplace
 Culture
GPT-4o
Qwen-2.5-Max
Gemini-2.0-Flash
Claude-3.7-Sonnet
Deepseek-R1
Llama-3.3
OLMo-2-32B
DeepSeek-R1-
Distill-Qwen-32B
82.5
78.0
91.4
74.4
81.1
61.3
75.0
82.2
80.7
76.9
79.8
80.9
62.5
74.2
79.8
76.1
84.5
77.0
82.5
69.3
74.8
85.2
78.3
86.4
81.6
85.5
66.4
72.5
84.2
81.4
89.8
79.2
84.7
68.9
76.6
79.7
78.9
75.5
59.0
73.0
57.9
63.7
75.3
66.8
72.5
60.0
74.3
43.6
63.3
71.7
62.2
64.9
68.9
75.7
56.7
59.7
50
60
70
80
90
Score
(b) CSI Prediction (SP-CSI)
Figure 2: Performance of LLMs across CSI categories for CSI Identification and Prediction tasks. For clarity, only
soft evaluation metrics are visualized. The results reveal consistent difficulties in CSI Identification across CSI
categories.
resembles a mask-filling task.
Since LLMs are
trained in an autoregressive manner and have likely
encountered many Western CSIs during training,
they can often infer plausible candidates for the
masked span. In contrast, CSI Identification re-
quires explicit reasoning about which elements
in a sentence are culturally specific and salient
for cross-cultural communication, a substantially
more demanding capability on which all models
struggle. To test this hypothesis, we run an abla-
tion on CSI Identification using the non-reasoning
counterpart of DeepSeek-R1.
Specifically, we
evaluate DeepSeek-V3.2 in its non-thinking mode
on the CSI Identification task.
It attains only
52.29% under the hard metric and 59.94% under
the soft metric- both markedly below the reasoning-
enabled DeepSeek-R1. This controlled compari-
son further supports our claim that CSI Identifica-
tion requires explicit cultural reasoning and judg-
ment.
Model
CSI Identification
CSI Prediction
HI-CSI
SI-CSI
HP-CSI
SP-CSI
GPT-4o
50.94
57.74
43.70
78.47
Qwen-2.5-Max
54.99
59.75
43.70
79.30
Gemini-2.0-Flash
48.73
57.15
42.94
78.96
Claude-3.7-Sonnet
47.95
60.47
46.76
81.76
Deepseek-R1
59.05
60.01
47.33
81.68
Llama-3.3
52.62
48.76
34.54
69.90
OLMo-2-32B
44.91
57.71
31.87
68.30
DeepSeek-R1-Distill-Qwen-32B
51.34
55.14
29.96
69.49
Table 2: CSI Identification and Prediction performance
across models. Highest and second-highest scores are
bolded and underlined, respectively. Values are percent-
ages; higher is better.
Among the evaluated models,
Claude-3.7-
6

--- Page 7 ---

Arabic
Chinese
Bengali (West Bengal)
Bengali (Bangladesh)
Model
Intra-lingual
Inter-lingual
Intra-lingual
Inter-lingual
Intra-lingual
Inter-lingual
Intra-lingual
Inter-lingual
SENTbert
CSIbert
SENTbert
CSIbert
SENTbert
CSIbert
SENTbert
CSIbert
SENTbert
CSIbert
SENTbert
CSIbert
SENTbert
CSIbert
SENTbert
CSIbert
Deepseek R1
69.02
28.75
81.09
65.86
72.46
33.93
83.47
71.34
84.40
37.23
74.40
48.44
83.54
35.40
74.13
47.41
Gemini-2.0-Flash
68.91
27.78
80.78
67.09
70.65
32.74
83.08
70.33
76.84
26.44
70.30
44.20
76.33
25.94
70.14
43.13
GPT-4o
72.76
35.21
81.08
67.94
74.66
38.85
83.81
72.42
81.69
35.46
70.49
45.06
80.56
32.42
70.16
44.14
Llama-3.3
68.95
28.93
80.90
66.25
72.74
34.60
83.59
72.10
84.32
37.07
74.40
48.27
83.52
35.17
74.12
47.19
Qwen-2.5-Max
70.54
33.21
80.51
67.66
67.44
34.67
83.75
72.74
64.68
25.42
70.60
46.59
64.02
23.26
70.42
44.54
OLMo-2-32B
69.01
28.96
81.09
66.26
72.71
34.85
83.56
72.03
76.11
23.61
70.80
43.32
75.27
21.93
70.61
42.02
Claude-3.7-Sonnet
72.65
33.47
81.64
68.69
73.88
36.88
83.91
72.07
82.49
34.10
73.01
46.01
80.92
30.67
72.24
42.86
D-R1-D-Qwen-32B
68.85
23.96
75.96
59.49
74.15
34.48
83.42
69.73
78.16
28.25
62.27
36.54
77.10
26.13
62.14
35.46
Average
70.08
30.03
80.38
66.16
72.34
35.12
83.58
71.59
78.59
30.95
70.78
44.80
77.66
28.87
70.50
43.34
Table 3: CSI adaptation performance (%) across models measured using CSIbert and SENTbert metrics. The CSIbert
metric is emphasized, as CSI adaptation typically involves localized substitutions that leave the overall sentence
structure largely unchanged, resulting in uniformly higher SENTbert scores. Best results per column are shown in
bold, and second-best results are underlined.
Sonnet and DeepSeek-R1 consistently outperform
others across both hard and soft metrics in Table 2,
indicating comparatively stronger cultural reason-
ing abilities in identifying and predicting Western
CSIs.
All models show consistent performance
across CSI categories, excelling in some but
struggling in others, revealing systematic vul-
nerabilities in specific cultural facets. Figure 2
illustrates these category-wise trends across LLMs.
In the CSI Identification task (Figure 2a), models
consistently struggle with categories such as Social
Etiquette and Cultural Reference, while achiev-
ing strong performance in Cultural Stereotype. In
contrast, the CSI Prediction task (Figure 2b) re-
veals a reciprocal pattern: LLMs perform notably
well when predicting CSIs from Cultural Refer-
ence, but show weaker performance in categories
such as Sports Tradition.
These results suggest
that LLMs’ cultural reasoning abilities are highly
category-dependent, with strengths in certain cul-
tural dimensions not generalizing to others.
LLM performance systematically declines
from Visible to Invisible levels of Hall’s cultural
triad for both CSI Identification and Prediction,
exhibited in Figures 5 and 6. To further analyze
this behavior, Table 9 reports per-category perfor-
mance across Hall’s cultural levels. The results
show that LLMs exhibit substantially lower perfor-
mance on semi-visible and invisible elements, in-
cluding Appropriacy and Orientations. Together,
these results indicate that LLMs are more effective
at handling surface-level cultural cues than deeper:
value and norm-driven aspects of culture.
4.2
Cultural Adaptation
The CSI Adaptation task evaluates the ability of
LLMs to adapt culture-specific content through
cross-cultural reasoning in both intra-lingual and
inter-lingual settings. Table 3 reports the full re-
sults.
We place primary emphasis on the hard
metric, as CSI adaptation typically involves local-
ized substitutions that preserve the overall sentence
structure, leading to consistently high SENTbert
scores that are less discriminative in this setting.
Overall, LLMs achieve higher adaptation perfor-
mance for Chinese cultural content, followed by
Arabic, while performance is comparatively lower
for Bengali across models and CSI categories.
LLMs consistently exhibit stronger CSI adap-
tation performance in inter-lingual than in
intra-lingual settings.
Across models, moving
from intra-lingual to inter-lingual adaptation yields
substantial gains in CSIbert metric, with average
improvements of approximately 51%–55% for Chi-
nese and Arabic, and 30%–35% for Bengali. This
pattern suggests that while LLMs are relatively ef-
fective at adapting Western cultural content when
operating directly within the target language, they
encounter greater difficulty when adapting non-
Western cultural concepts expressed in English.
One contributing factor may be the handling of
culture-specific transliterations in intra-lingual set-
tings, such as ganbei (‘cheers’ in Chinese), bisht
(a traditional Arabic garment), or pahela baishakh
(the Bengali New Year).
To better understand
where these gains arise, we analyze performance
differences at the CSI category level. Figures 7
and 8 show that inter-lingual adaptation yields the
largest improvements in the Cultural Stereotype
category and the smallest gains in Cultural Refer-
ence. This pattern suggests that LLMs more read-
7

--- Page 8 ---

ily adapt stereotypical or conventionalized cultural
knowledge in the target language, whereas cultur-
ally grounded references tied to specific contexts
or entities remain more challenging.
A similar pattern emerges when results are ana-
lyzed through Hall’s triadic model of culture (Fig-
ures 9 and 10). Across all cultures, inter-lingual
adaptation consistently outperforms intra-lingual
adaptation, accompanied by a clear performance
decline from Visible to Invisible cultural levels.
This decline, however, is less pronounced for the
two Bengali cultural settings (Figure 10).
Adaptation Procedure.
During CSI adapta-
tion, we explicitly prompt LLMs to indicate which
of the twelve adaptation strategies defined in Ap-
pendix C.1 is employed.
In practice, models
frequently select a combination of two strategies
(Couplet), suggesting that CSI adaptation often re-
quires balancing cultural fidelity and interpretabil-
ity. Among single strategies, Cultural Equivalent
(replacing a CSI with a culturally analogous term
from the target culture) emerges as the most com-
monly used approach across models. To assess the
effectiveness of individual adaptation strategies,
we compute CSIbert scores for each unique method
and aggregate performance across instances. This
analysis enables identification of the most and least
effective adaptation strategies for CSI adaptation,
as summarized in Table 10.
Regional Bias in Adaptation. Bengali consti-
tutes a particularly informative case for evaluating
regional and religious bias in cultural adaptation.
Demographically, Bengali speakers are predomi-
nantly Muslim (approximately 71%) with a sub-
stantial Hindu minority (approximately 28%), and
are distributed across two postcolonial national
contexts: Bangladesh (approximately 59% of Ben-
gali speakers) and the Indian state of West Bengal
(approximately 38%) (Bangladesh Statistics Bu-
reau, 2022). These two populations differ not only
in nationality and religion but also in dialectal us-
age, commonly referred to as Bangal (Bangladesh)
and Ghoti (West Bengal)-as well as in culturally
salient terminology, festivals, food practices, etc.
To assess whether such regional and religious
variation influences LLM-based cultural adapta-
tion, we evaluate Bengali CSIs against both West
Bengal and Bangladesh cultural corpora and com-
pare adaptation performance across settings. De-
spite Bangladesh representing the larger popula-
tion share and Muslim Bengalis constituting a clear
majority overall, some models consistently achieve
Model
Intra-lingual
(SENTBERT / CSIBERT)
Inter-lingual
(SENTBERT / CSIBERT)
DeepSeek-R1
0.003/0.005
−0.0002/ −0.003
Gemini-2.0-Flash
0.002/0.003
0.001/0.012∗∗
GPT-4o
0.005/0.023∗
−0.0002/ −0.001
Llama-3.3
0.003/0.006
−0.0002/ −0.004
OLMo-2-32B
0.003/0.005
−0.0002/0.009
Qwen-2.5-Max
0.001/0.012
0.002/0.030∗∗
Claude-3.7-Sonnet
0.009/0.020∗
0.004/0.026∗
DeepSeek-R1-Distill-Qwen-32B
0.005/0.005
0.000/0.016
Table 4: Mean regional performance differences in Ben-
gali cultural adaptation (West Bengal −Bangladesh),
aggregated across CSI categories.
Statistical signifi-
cance is evaluated using a one-sided Wilcoxon signed-
rank test (∗p < 0.05, ∗∗p < 0.01).
higher adaptation performance for the West Ben-
gal setting.
As reported in Table 4, all statis-
tically significant mean performance differences
favor West Bengal over Bangladesh, indicating
stronger model alignment with West Bengal spe-
cific cultural knowledge, particularly for models
like Claude and Gemini.
Qualitative inspection
of model outputs further substantiates this pattern.
When adapting CSIs related to social traditions
and cultural references, models frequently select
West Bengal–associated (and Hindu-associated)
terms over their Bangladesh counterparts. For ex-
ample, পুেজা(Puja) is preferred over ঈদ(Eid) when
adapting festivals such as Christmas/Halloween,
and দাদা(brother) is favored over ভাই(brother) for
concepts related to kinship. These choices reflect
systematic preference for Ghoti lexical and cul-
tural markers over Bangal alternatives. Notably,
this bias emerges even though Bengali Hindus con-
stitute a numerical minority within the broader
Bengali-speaking population. Moreover, it arises
in a low-resource setting where overall Bengali per-
formance is comparatively weak (Table 3).
To-
gether, these findings indicate that LLMs not only
exhibit uneven cultural competence across lan-
guages, but can also encode pronounced regional
and ethnoreligious biases within a single language,
favoring culturally dominant or more frequently
represented variants in their training data.
5
Conclusion
We introduce XCR-Bench, a human-annotated
parallel corpus designed to support the evalua-
tion of cross-cultural reasoning in large language
models (LLMs). The benchmark comprises three
unique reasoning tasks with corresponding evalua-
tion metrics. By integrating Newmark’s concept of
CSIs with Hall’s Iceberg Model of culture, XCR-
Bench enables fine-grained analysis not only in
8

--- Page 9 ---

surface artifacts but also for social norms, beliefs,
and habitual practices. Our evaluation shows that
contemporary LLMs struggle to identify and adapt
CSIs in cross-cultural contexts. Furthermore, we
observe that cultural adaptation responses often en-
code regional and ethno-religious biases within a
single linguistic setting. Our work provides high-
quality data and empirical insights for advancing
the study of cross-cultural reasoning and bias anal-
ysis in NLP.
Limitations
While our study introduces a novel benchmark for
evaluating LLMs’ cross-cultural adaptability, it is
subject to several limitations that warrant discus-
sion and provide avenues for future research.
Limited Coverage of Newmark Categories.
Newmark’s framework (Newmark, 1988) out-
lines five categories of CSIs, as detailed in Ap-
pendix B.1. As shown in Table 5, the CSIs in XCR-
Bench primarily span categories 2 and 3. This fo-
cus stems from our emphasis on the semi-visible
and invisible levels of Hall’s Iceberg model of cul-
ture, which encompass social values, beliefs, and
norms.
Consequently, our benchmark does not
cover categories 1, 4, and 5 (e.g., ecology, mate-
rial culture, and gestures), representing a gap that
future work could address by expanding the CSI
typology.
Limited Coverage of Cultures. Our corpus in-
cludes CSI annotations for only four distinct cul-
tures (Western US/UK, Arabic, Bengali, and Chi-
nese).
While this selection enables targeted in-
sights, incorporating additional languages and cul-
tures would likely reveal broader patterns in LLMs’
adaptation capabilities. This constraint was influ-
enced by our available resources for collaboration
and annotation.
Limited Coverage of Prompting Techniques.
In our experiments, we employed the expert
prompting strategy from Xu et al. (2023). Alterna-
tive prompting methods could yield varying perfor-
mance levels, potentially improving results. How-
ever, we limited our evaluation to this single tech-
nique due to the high API costs associated with pro-
prietary LLMs.
References
Muhammad Farid Adilazuarda, Sagnik Mukherjee,
Pradhyumna Lavania, Siddhant Singh, Alham Fikri
Aji, Jacki O’Neill, Ashutosh Modi, and Monojit
Choudhury. 2024. Towards measuring and model-
ing” culture” in llms: A survey.
arXiv preprint
arXiv:2403.15412.
Mohammad Atari, Mona Xue, Peter Park, Damián
Blasi, and Joseph Henrich. 2023. Which humans?
PsyArXiv.
Bangladesh Statistics Bureau. 2022. Preliminary report
on population and housing census 2022. Technical
report, Bangladesh Statistics Bureau. English Ver-
sion.
John W Berry. 1974. Psychological aspects of cultural
pluralism: Unity and identity reconsidered. Topics
in culture learning, 2:17–22.
Sjoerd Beugelsdijk and Chris Welzel. 2018.
Dimen-
sions and dynamics of national culture: Synthesizing
hofstede with inglehart.
Journal of cross-cultural
psychology, 49(10):1469–1505.
Shaily Bhatt and Fernando Diaz. 2024. Extrinsic evalu-
ation of cultural competence in large language mod-
els. arXiv preprint arXiv:2406.11565.
Yong Cao, Yova Kementchedjhieva, Ruixiang Cui, An-
tonia Karamolegkou, Li Zhou, Megan Dare, Lucia
Donatelli, and Daniel Hershcovich. 2024. Cultural
adaptation of recipes. Transactions of the Associa-
tion for Computational Linguistics, 12:80–99.
Yiming Cui, Wanxiang Che, Ting Liu, Bing Qin, Ziqing
Yang, Shijin Wang, and Guoping Hu. 2019.
Pre-
training with whole word masking for chinese bert.
arXiv preprint arXiv:1906.08101.
Jonathan Dunn, Benjamin Adams, and Harish Tayyar
Madabushi. 2024. Pre-trained language models rep-
resent some geographic populations better than oth-
ers. arXiv preprint arXiv:2403.11025.
Esin Durmus,
Karina Nguyen,
Thomas I Liao,
Nicholas Schiefer, Amanda Askell, Anton Bakhtin,
Carol Chen, Zac Hatfield-Dodds, Danny Hernan-
dez, Nicholas Joseph, and 1 others. 2023.
To-
wards measuring the representation of subjective
global opinions in language models. arXiv preprint
arXiv:2306.16388.
Shiwei Guo, Sihang Jiang, Qianxi He, Yanghua Xiao,
Jiaqing Liang, Bi Yude, Minggui He, Shimin Tao,
and Li Zhang. 2025.
Do large language models
truly understand cross-cultural differences?
arXiv
preprint arXiv:2512.07075.
Christian
Haerpfer,
Ronald
Inglehart,
Alejandro
Moreno, Christian Welzel, Kseniya Kizilova, Jaime
Diez-Medrano, Marta Lagos, Pippa Norris, Eduard
Ponarin, and Bi Puranen. 2020. World values survey
wave 7 (2017-2020) cross-national data-set.
(No
Title).
Edward T Hall. 1976. Beyond culture. Garden City.
9

--- Page 10 ---

Daniel Hershcovich,
Stella Frank,
Heather Lent,
Miryam De Lhoneux, Mostafa Abdou, Stephanie
Brandl, Emanuele Bugliarello, Laura Cabello Pi-
queras, Ilias Chalkidis, Ruixiang Cui, and 1 others.
2022. Challenges and strategies in cross-cultural nlp.
arXiv preprint arXiv:2203.10020.
Geert Hofstede, Gert Jan Hofstede, and Michael
Minkov. 2010. Cultures et organisations: Nos pro-
grammations mentales. Pearson Education France.
Jie Huang and Kevin Chen-Chuan Chang. 2023. To-
wards reasoning in large language models: A survey.
In Findings of the association for computational lin-
guistics: ACL 2023, pages 1049–1065.
Rebecca L Johnson, Giada Pistilli, Natalia Menédez-
González, Leslye Denisse Dias Duran, Enrico Panai,
Julija Kalpokiene, and Donald Jay Bertulfo. 2022.
The ghost in the machine has an american ac-
cent:
value conflict in gpt-3.
arXiv preprint
arXiv:2203.07785.
Mohsinul Kabir, Ajwad Abrar, and Sophia Ananiadou.
2025a.
Break the checkbox: Challenging closed-
style evaluations of cultural alignment in LLMs. In
Proceedings of the 2025 Conference on Empirical
Methods in Natural Language Processing, pages 24–
51, Suzhou, China. Association for Computational
Linguistics.
Mohsinul Kabir, Tasnim Ahmed, Md Mezbaur Rah-
man, Polydoros Giannouris, and Sophia Ananiadou.
2025b. Semantic label drift in cross-cultural transla-
tion. arXiv preprint arXiv:2510.25967.
Mohsinul Kabir, Tasfia Tahsin, and Sophia Ananiadou.
2025c. From n-gram to attention: How model archi-
tectures learn and propagate bias in language model-
ing. arXiv preprint arXiv:2505.12381.
Yova Kementchedjhieva, Di Lu, and Joel Tetreault.
2020. The apposcorpus: A new multilingual, multi-
domain dataset for factual appositive generation.
arXiv preprint arXiv:2011.03287.
Julia Kharchenko, Tanya Roosta, Aman Chadha, and
Chirag Shah. 2024.
How well do llms represent
values across cultures?
empirical analysis of llm
responses based on hofstede cultural dimensions.
arXiv preprint arXiv:2406.14805.
Jun Seong Kim, Kyaw Ye Thu, Javad Ismayilzada, Jun-
yeong Park, Eunsu Kim, Huzama Ahmad, Na Min
An, James Thorne, and Alice Oh. 2025. When tom
eats kimchi: Evaluating cultural bias of multimodal
large language models in cultural mixture contexts.
arXiv preprint arXiv:2503.16826.
Jan-Christoph Klie, Richard Eckart de Castilho, and
Iryna Gurevych. 2024. Analyzing dataset annotation
quality management in the wild. Computational Lin-
guistics, 50(3):817–866.
Shuang Li, Jiangjie Chen, Siyu Yuan, Xinyi Wu, Hao
Yang, Shimin Tao, and Yanghua Xiao. 2024. Trans-
late meanings, not just words: Idiomkb’s role in op-
timizing idiomatic translation with language models.
In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 38, pages 18554–18563.
Chen Cecilia Liu, Iryna Gurevych, and Anna Korhonen.
2025. Culturally aware and adapted NLP: A taxon-
omy and a survey of the state of the art. Transac-
tions of the Association for Computational Linguis-
tics, 13:652–689.
Tarek Naous, Michael J Ryan, Alan Ritter, and Wei Xu.
2024. Having beer after prayer? measuring cultural
bias in large language models. In Proceedings of the
62nd Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages
16366–16393.
Roberto Navigli, Simone Conia, and Björn Ross. 2023.
Biases in large language models: origins, inventory,
and discussion. ACM Journal of Data and Informa-
tion Quality, 15(2):1–21.
Peter Newmark. 1988. A textbook of translation, vol-
ume 66. Prentice hall New York.
Denis Peskov, Viktor Hangya, Jordan Boyd-Graber,
and Alexander Fraser. 2021.
Adapting entities
across languages and cultures.
In Findings of the
Association for Computational Linguistics: EMNLP
2021, pages 3725–3750.
Pouya Pezeshkpour and Estevam Hruschka. 2024.
Large language models sensitivity to the order of op-
tions in multiple-choice questions. In Findings of the
Association for Computational Linguistics: NAACL
2024, pages 2006–2017.
Abhinav Rao, Akhila Yerukola, Vishwa Shah, Katha-
rina Reinecke, and Maarten Sap. 2024.
Nor-
mad: A framework for measuring the cultural adapt-
ability of large language models.
arXiv preprint
arXiv:2404.12464.
Abhinav Sukumar Rao, Akhila Yerukola, Vishwa Shah,
Katharina Reinecke, and Maarten Sap. 2025. Nor-
mad: A framework for measuring the cultural adapt-
ability of large language models. In Proceedings of
the 2025 Conference of the Nations of the Americas
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies (Volume 1:
Long Papers), pages 2373–2403.
Paulius Rauba, Nabeel Seedat, Max Ruiz Luyten, and
Mihaela van der Schaar. 2024. Context-aware test-
ing: A new paradigm for model testing with large
language models. Advances in Neural Information
Processing Systems, 37:112505–112553.
Paul Röttger, Valentin Hofmann, Valentina Pyatkin,
Musashi Hinck, Hannah Kirk, Hinrich Schütze, and
10

--- Page 11 ---

Dirk Hovy. 2024. Political compass or spinning ar-
row? towards more meaningful evaluations for val-
ues and opinions in large language models. In Pro-
ceedings of the 62nd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long
Papers), pages 15295–15311.
Ali Safaya, Moutasem Abdullatif, and Deniz Yuret.
2020. KUISAIL at SemEval-2020 task 12: BERT-
CNN for offensive speech identification in social me-
dia. In Proceedings of the Fourteenth Workshop on
Semantic Evaluation, pages 2054–2059, Barcelona
(online). International Committee for Computational
Linguistics.
Sougata Saha, Saurabh Kumar Pandey, Harshit Gupta,
and Monojit Choudhury. 2025. Reading between the
lines: Can llms identify cross-cultural communica-
tion gaps? arXiv preprint arXiv:2502.09636.
Sagor Sarker. 2020.
Banglabert: Bengali mask lan-
guage model for bengali language understanding.
Christina Schäffner. 1997. Skopos theory, pages 235–
238. Routledge.
Pushpdeep Singh, Mayur Patidar, and Lovekesh Vig.
2024.
Translating across cultures:
Llms for
intralingual cultural adaptation.
arXiv preprint
arXiv:2406.14504.
Kaitao Song, Xu Tan, Tao Qin, Jianfeng Lu, and Tie-
Yan Liu. 2020. Mpnet: Masked and permuted pre-
training for language understanding.
Advances in
neural information processing systems, 33:16857–
16867.
Yuchen Song, Andong Chen, Wenxin Zhu, Kehai Chen,
Xuefeng Bai, Muyun Yang, and Tiejun Zhao. 2025.
Culture in a frame: C ^3 b as a comic-based bench-
mark for multimodal culturally awareness.
arXiv
preprint arXiv:2510.00041.
Bill Thompson, Seán G Roberts, and Gary Lupyan.
2020.
Cultural influences on word meanings re-
vealed through large-scale semantic alignment. Na-
ture Human Behaviour, 4(10):1029–1038.
Yuhang Wang, Yanxu Zhu, Chao Kong, Shuyu Wei, Xi-
aoyuan Yi, Xing Xie, and Jitao Sang. 2024. Cdeval:
A benchmark for measuring the cultural dimensions
of large language models. In Proceedings of the 2nd
Workshop on Cross-Cultural Considerations in NLP,
pages 1–16.
Jincenzi Wu, Jianxun Lian, Dingdong Wang, and He-
len Meng. 2025. Socialcc: Interactive evaluation for
cultural competence in language agents. In Proceed-
ings of the 63rd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), pages 33242–33271.
Benfeng Xu, An Yang, Junyang Lin, Quan Wang,
Chang Zhou, Yongdong Zhang, and Zhendong Mao.
2023. Expertprompting: Instructing large language
models to be distinguished experts. arXiv preprint
arXiv:2305.14688.
Binwei Yao, Ming Jiang, Tara Bobinac, Diyi Yang, and
Junjie Hu. 2024. Benchmarking machine translation
with cultural awareness. In Findings of the Associ-
ation for Computational Linguistics: EMNLP 2024,
pages 13078–13096.
Wenlong Zhao, Debanjan Mondal, Niket Tandon, Dan-
ica Dillion, Kurt Gray, and Yuling Gu. 2024. World-
valuesbench: A large-scale benchmark dataset for
multi-cultural value awareness of language models.
arXiv preprint arXiv:2404.16308.
A
Background Study
A.1
Measuring ‘Culture’ in LLMs
Recent studies have predominantly relied on global
surveys to assess the cultural knowledge of large
language models (LLMs) regarding specific coun-
tries.
In particular, multiple-choice questions
drawn from surveys such as the World Values Sur-
vey (WVS) (Haerpfer et al., 2020), Hofstede’s Cul-
tural Dimensions (Hofstede et al., 2010), or PEW
Global Surveys 4 are presented to LLMs to eval-
uate their understanding of particular cultures or
countries (Zhao et al., 2024; Durmus et al., 2023;
Kharchenko et al., 2024). Wang et al. (2024) uses
Hofstede’s Survey to construct a benchmark by
forming natural scenario-based questions from the
questionnaire itself using GPT-4. While these sur-
veys provide an excellent means of gathering real-
world human perspectives, their use for evaluat-
ing cultural knowledge in LLMs has several lim-
itations: (i) LLMs are restricted to the predefined
choices in multiple-choice formats, yet culture is a
nuanced concept that often requires more sophisti-
cated and open-ended responses (Beugelsdijk and
Welzel, 2018); (ii) altering the order of multiple-
choice options can lead LLMs to produce entirely
different answers, which undermines reliability for
a multifaceted notion like culture (Pezeshkpour
and Hruschka, 2024). In response, several stud-
ies have critiqued this approach and advocated for
more open-ended evaluations to better capture the
sophistication and intricacy of cultural understand-
ing (Kabir et al., 2025a; Röttger et al., 2024). Other
works have proposed specialized frameworks tar-
geting specific cultural facets or proxies, such as
food, etiquette, or regional differences, rather than
attempting a holistic evaluation of culture (Naous
et al., 2024; Adilazuarda et al., 2024).
4https://www.pewresearch.org/
11

--- Page 12 ---

A.2
Evaluation of Cross-Cultural
Competence of LLMs
The ability of large language models (LLMs) to
adapt meanings across cultural contexts is essential
for broadening access to AI systems and mitigating
harms from culturally maladapted outputs (Kabir
et al., 2025b).
To evaluate LLMs’ proficiency
in cross-cultural communication, recent studies
have drawn on the concept of Culture-Specific
Items (CSIs), as defined by Newmark (Newmark,
1988), emphasizing that identifying and adapting
these items is critical for effective cross-cultural ex-
change.
Several works have explored CSI adaptation in spe-
cific domains. For example, Singh et al. (2024)
adapted American CSIs to Indian equivalents us-
ing the Friends Dialogues corpus 5. Similarly, Yao
et al. (2024) introduced CAMT, a parallel corpus
across six languages featuring paired CSIs, to as-
sess LLMs’ cultural adaptability.
In a domain-
specific approach, Cao et al. (2024) proposed
tasks for translating and culturally adapting recipes
between Chinese- and English-speaking cuisines.
However, these studies primarily rely on machine
translation evaluations and often lack explicit CSI
annotations, limiting their ability to probe mod-
els’ targeted capabilities in CSI span identification
and sentence-level adaptation. More recent efforts
have expanded the scope of cross-cultural evalua-
tions. Guo et al. (2025) proposed a methodology
using Cross-Cultural Core Concept Sets (CCCs) to
assess LLMs’ cross-cultural understanding in real-
world scenarios, enabling more authentic capabil-
ity assessments. Wu et al. (2025) introduced So-
cialCC, a benchmark for evaluating cultural com-
petence through 3,060 multi-turn interactive inter-
cultural scenarios spanning 60 countries. Incorpo-
rating multimodality, Song et al. (2025) developed
C3B, a benchmark with 2,000 images and over
18,000 QA pairs across three tasks of varying dif-
ficulty: basic visual recognition, higher-level cul-
tural conflict understanding, and cultural content
generation. In a related vein, Kim et al. (2025) cre-
ated a benchmark to evaluate biases in multimodal
LLMs across high- and low-resource cultural set-
tings.
Our work complements these efforts by providing
a culturally rich corpus of realistic scenarios, with
explicit annotations for CSI categories, Hall’s cul-
tural levels, and cross-cultural CSI pairs, thereby
5https://convokit.cornell.edu/documentation/friends.html
advancing research in cross-cultural NLP.
B
Utilizing Newmark’s Theory of CSIs
B.1
Newmark’s Definition of Culture and
CSI Categories
Newmark (Newmark, 1988) defines culture as a
shared way of life, encompassing the distinctive
characteristics, beliefs, and practices of a particu-
lar social group. As outlined in the cultural proxies
in Appendix A, these differences span multiple
dimensions- from tangible elements like food and
materials to abstract ones such as emotions and
values (Thompson et al., 2020; Adilazuarda et al.,
2024).
Newmark (Newmark, 1988) terms such
concepts Culture-Specific Items (CSIs), whose
identification and handling are vital for effective
cross-cultural communication. He proposes five
key categories of CSIs that are especially critical
in cross-cultural translation:
Category 1:
Ecology covers the relationship
between a community and its natural environment,
including indigenous flora, fauna, geography, and
climate. Example: Translating the specific name
for a seasonal desert wind, such as the Simoom in
Arabic cultures, or the Khamsin in Egypt.
Category 2:
Material Culture (Artefacts)
includes all tangible, human-made objects that
shape or reflect a society’s way of living, such
as tools, clothing, architecture, and food. Exam-
ple:
Translating terms like the Shamagh (the
traditional checked men’s headdress in the Gulf re-
gion) or Iftar (the meal to break the Ramadan fast).
Category 3:
Social Culture refers to the
patterns of social activity, including work, leisure,
and communal practices that define daily and
ceremonial life. Example: Translating the name
of a traditional social gathering like the Majlis (a
council or sitting room for community discussion
in Arab cultures) or Jiāzǐ (a 60th birthday celebra-
tion in Chinese culture).
Category 4:
Organizations, Customs, and
Ideas encompasses the abstract and institutional
aspects of culture, including its political, legal,
religious, artistic, and customary systems. Ex-
ample: Translating concepts such as Apritismo
(a Peruvian political ideology) or Barangay (the
smallest administrative division in the Philippines,
12

--- Page 13 ---

rooted in pre-colonial history).
Category 5:
Gestures and Habits involves
non-verbal communication, body language, and
routine behaviors whose meanings are culturally
encoded and may not have direct equivalents.
Example: Interpreting gestures like the chin flick
(a sign of dismissal or negation in parts of Italy
and France) or the ”Moutza” (an offensive hand
gesture in Greece).
13

--- Page 14 ---

C
CSI Categories Mapping
Newmark CSI
Category
Category from Liu et al. (2025)
XCR-Bench Category
CSI Example
Material Culture
Social
Culture
Social.Relationship (e.g., Family,
Fictive, etc.)
Social Etiquette
He <CSI> thanked </CSI> the
stranger who held the elevator
door open for him.
Social.Context (e.g., Situational,
Historical, etc.)
Sports Tradition
The family attends <CSI>
Little League games </CSI>
every Saturday during
baseball season.
Social.Communicative Goals (e.g.,
Greeting, Requesting, etc.)
Workplace Culture
At networking events,
attendees often exchange
<CSI> business cards </CSI>
to facilitate future
connections.
Social.Demographics (e.g., Income,
Education, etc.)
Organisations,
Customs and
Ideas
Ideational.Concepts (e.g., Food,
Holidays, etc.)
Social Tradition
They’re hosting a <CSI>
Hogmanay </CSI> celebration
to welcome the New Year.
Ideational.Knowledge (e.g., Factual,
Common Sense, etc.)
Cultural Reference
He learned to use <CSI>
Fahrenheit </CSI> instead of
Celsius for temperature
discussions.
Ideational.Values (e.g., Bias, Hate,
etc.)
Cultural Value
She donated to a group
working to protect <CSI> wild
horses </CSI>, seeing them as
symbols of America’s
untamed spirit.
Ideational.Norms (e.g., Descriptive,
Normative, etc.)
Cultural Stereotype
They’re <CSI> helicopter
parents </CSI> who monitor
their child’s every move and
decision.
Ideational.Artifacts (Art, Meme,
Architecture, etc.)
Walking through the small
town, she admired the
charming <CSI> wooden
houses </CSI> that lined the
streets.
Ecology
Gestures and Habits
Table 5: Mapping between Newmark CSI categories, the taxonomy of Liu et al. (2025), and XCR-Bench categories,
with illustrative CSI-tagged examples. Empty cells indicate mappings not specified in the current dataset.
14

--- Page 15 ---

C.1
Adaptation Procedure
Newmark (1988) proposes a set of strategies for
translating culture-specific terms, conditioned on
contextual and audience-related factors.
In this
work, we reinterpret these strategies as cultural
adaptation methods and explicitly prompt models
to indicate which method is employed during adap-
tation.
This allows us to analyze which adapta-
tion strategies are most effective for handling CSIs
across cultural contexts.
1. Transference. The original CSI is retained un-
changed in the adapted output (e.g., sari, ki-
mono).
2. Cultural Equivalent. A culturally analogous
term from the target culture is substituted to con-
vey a similar function or social meaning (e.g.,
adapting Thanksgiving as a local harvest festi-
val).
3. Neutralization. The CSI is replaced with a de-
scription that explains its function or meaning
in culturally neutral terms (e.g., rendering ki-
mono as “a traditional Japanese robe”).
4. Literal Translation. The CSI is translated di-
rectly on a word-by-word basis into the target
language (e.g., translating Bundestag as “Fed-
eral Parliament”).
5. Labeling. The CSI is retained or adapted and
accompanied by a brief explanatory label that
clarifies its cultural role or category.
6. Naturalization. The CSI is adapted to conform
to the spelling or pronunciation conventions of
the target language (e.g., Pharisees).
7. Componential Analysis. The CSI is decom-
posed into its constituent semantic components,
each of which is explicitly explained (e.g., ren-
dering dacha as “a summer house for wealthy
people”).
8. Deletion. The CSI is omitted entirely when it
is non-essential to the meaning or when adapta-
tion would introduce unnecessary complexity.
9. Couplet.
Two adaptation strategies are com-
bined, such as retaining the original CSI while
also providing an explanatory description.
10. Accepted Standard Translation.
A widely
recognized and conventionally accepted trans-
lation is used (e.g., Holy See for Saint-Siège).
11. Paraphrase or Gloss. A longer explanatory
paraphrase or gloss is added, either inline or as
a footnote, to clarify the CSI’s meaning and cul-
tural context.
12. Classifier. A general category term is added
to situate the CSI within a familiar conceptual
class (e.g., “the Japanese game of Go”).
D
Annotation and Annotator Details
Annotation Training.
The annotation process
was preceded by structured training sessions con-
ducted by the authors and the principal investiga-
tor (PI). For each language, we organized two on-
line meetings (approximately one hour each) with
both annotators and expert annotators. These ses-
sions focused on clarifying the annotation objec-
tives, discussing the notion of Culture-Specific
Items (CSIs), and walking through the detailed an-
notation guidelines provided in Appendix D.1. An-
notators were encouraged to ask questions and re-
solve ambiguities before beginning the annotation
process.
Annotator Qualifications.
Annotators were
recruited through established academic collabora-
tors in Bengali, Chinese, and Arabic.
For each
language, the annotation team consisted of two an-
notators and one expert annotator. Expert annota-
tors hold a PhD in Computational Linguistics or a
closely related field and have substantial prior expe-
rience in corpus construction and linguistic annota-
tion. The two annotators are either undergraduate
or PhD students with prior experience in linguistic
or NLP-related annotation tasks.
Specifically, the Arabic annotators are under-
graduate students based in Saudi Arabia, the Chi-
nese annotators are PhD students based in the UK,
and the Bengali annotators are PhD students based
in the UK or the USA, all working in NLP or
closely related fields.
The two annotators inde-
pendently produced both intra-lingual and inter-
lingual adaptations of the base sentences. In cases
of disagreement, the expert annotator adjudicated
and selected the most appropriate adaptation.
Compensation.
Annotators are compensated
for their work in accordance with the minimum
wage standards of the countries in which they re-
side.
15

--- Page 16 ---

D.1
General Annotation Guidelines for
Cross-Cultural CSI Adaptation
You will work with a dataset of English sen-
tences in which culture-specific items (CSIs)
which are predominantly drawn from Western
(US/UK) cultural contexts. The CSIs are explic-
itly marked using <CSI> tags in the dataset sam-
ples. Your task is to adapt these CSI-marked terms
into culturally appropriate counterparts for Ara-
bic/Chinese/Bengali cultures. For each instance,
you will produce: (i) an intra-lingual adaptation
in English that reflects the target cultural context,
and (ii) an inter-lingual adaptation in your own lan-
guage.
Please ensure that adaptations maintain the orig-
inal sentence’s communicative purpose while be-
ing culturally appropriate and natural in the target
context.
To maintain consistency across adaptations,
kindly follow the guidelines provided below.
1. Purpose
The goal of annotation is to ensure that CSI adap-
tations:
• Reflect authentic cultural values, norms, and
practices of the target culture.
• Use natural and idiomatic language in both
intra- and inter-lingual adaptations.
• Respect cultural, religious, and social sensi-
tivities, including regional variation where ap-
plicable.
2. Adaptation Rules
Following Newmark’s cultural equivalence frame-
work (Newmark, 1988), annotate each CSI using
one of the following strategies. [For illustration,
adaptation examples are given here in Arabic.]
7aragraphA. Direct Equivalent Rule: Replace
the CSI with a culturally identical or near-identical
equivalent that exists in the target culture.
Example:
Original:
<CSI>pub
gather-
ing</CSI>
Intra-lingual
(Arabic
culture):
qahwa gathering Inter-lingual (Arabic):
ĞﺣĻﻠﺴﻪ
ڡĞﻬﻮﻩĞ
Annotation tip: Ensure regional appropriate-
ness (e.g., differences across Arab regions or be-
tween Bengali varieties).
7aragraphB. Functionally Similar Equivalent
Rule: When no direct equivalent exists, replace
the CSI with a culturally different but functionally
similar concept.
Example:
Original:
<CSI>trick-or-
treating</CSI> Intra-lingual (Arabic culture):
children
receiving
Eid
gifts
Inter-lingual
(Arabic):ﻋٮĽﺪٮĽﻪĞﺍلأﻃڡęﺎﻝ ڡęﻰĽﺍﻟﻌٮĽﺪ
7aragraphC. Neutral Term Rule: If no clear cul-
tural equivalent exists, use a neutral expression that
fits social norms in the target culture without intro-
ducing foreign practices.
Example:
Original:
<CSI>friendly
ban-
ter</CSI> Intra-lingual (Arabic culture): light-
hearted teasing Inter-lingual (Arabic):ﻣﺮęﺍﺣًﺎ
ﺣęڡę ٮĽڡęً
7aragraphD. Non-transferable Rule: Label the
CSI as Non-transferable if adapting it would con-
flict with cultural, religious, or social norms in the
target culture.
Example:
Original:
They met through a
<CSI>dating app</CSI>. Adaptation: Non-
transferable
3. Cultural Sensitivity
While doing the annotation, please ensure to:
• Avoid culturally inappropriate or taboo con-
tent (e.g., alcohol, gambling, or sensitive rela-
tionships where applicable).
• Respect religious norms and social conven-
tions.
4. Annotation Checklist
For each sentence, please verify:
• Cultural accuracy: Is the CSI adapted ap-
propriately for the target culture?
• Linguistic quality: Is the adaptation natural
and idiomatic?
• Functional equivalence: Does the adapta-
tion preserve the original communicative in-
tent?
• Consistency: Do the intra- and inter-lingual
adaptations align?
5. Final Notes
• Consult the expert annotator for ambiguous or
borderline cases.
• Flag creative or uncertain adaptations for fur-
ther review.
• Use CANDLE and Cultural Atlas as refer-
ence sources for relevant cultural practices,
rituals, and traditions.
16

--- Page 17 ---

Social
Tradition
Social
Etiquette
Cultural
Reference
Workplace
Culture
Cultural
Stereotype
Cultural
Value
Sports
Tradition
CSI Category
0
50
100
150
200
250
300
350
Number of Instances
Hall's Level
Invisible
Semi-visible
Visible
Figure 3: Mapping between CSI categories and Hall’s cultural levels. The textured bar plots indicate a higher
concentration of semi-visible and invisible cultural elements across all CSI categories.
Dataset
Domain
Task
CSI
Annot.
Hall’s
Triad
Cross-Cult.
CSI Pair
ApposCorpus
(Kementchedjhieva et al., 2020)
Person, Org.
Trans.



Adaption
(Peskov et al., 2021)
Celebrity
Trans.



IdiomKB
(Li et al., 2024)
Idioms
Trans.



CulturalRecipes
(Cao et al., 2024)
Recipes
Trans.



NormAd
(Rao et al., 2025)
Soc. Etiq.
Reason.



CAMET
(Yao et al., 2024)
Cult. Cat.
Trans.


Part.
XCR-Bench (ours)
Cult. Cat.
Reason.



Table 6: Dataset comparison by annotation granularity. Cult., Cat., Annot., Trans., and Reason. abbreviate Culture,
Category, Annotation, Translation, and Reasoning.
E
Properties of XCR-Bench Corpus
As detailed in Section 2.3, XCR-Bench is the
first dataset to provide comprehensive annotations
aligned with Hall’s triadic model of culture, with
particular emphasis on the Semi-visible and Invisi-
ble layers that encompass beliefs, values, and so-
cial norms. Figure 3 illustrates the mapping be-
tween CSI categories and Hall’s cultural levels,
highlighting a predominant focus on these Semi-
visible and Invisible layers.
Table 7 shows an example sample from the
XCR-Bench corpus.
Each sample contains it’s
fine-grained annotation for CSI Category, CSI-
Hall Mapping, Hall’s Level and parallel inter-
lingual and intra-lingual cross-cultural CSI pairs in
four distinct cultures.
We present the mapping of Hall’s cultural ele-
ments with our CSI categories in Figure 4. This
shows how the Hall’s cultural elements are mapped
across our 7 distinct categories of CSIs. Some CSI
categories and cultural elements are predominant
in number because of their vast availability in the
source where we extracted our CSIs from, namely
CANDLE and Cultural Atlas.
We explicitly show the cultural element map-
ping with Hall’s triads in Table 8 with instances
from our XCR-Bench corpus. We derive this map-
ping from Hall (1976). Notably, the Hall cultural
level of CSIs are independent of Newmark’s cate-
gorization and based on their context.
17

--- Page 18 ---

Field
Content
CSI
Halloween
Cultural Context
Halloween is widely celebrated in the West with decorations, costumes, and trick-or-
treating.
Sentence
We’re decorating the house for <CSI> Halloween </CSI> this weekend.
CSI Category
Social Tradition
CSI-Hall Mapping
Rituals
Hall’s Level
Semi-visible
Chinese
Intra-lingual
We’re decorating the house for the <CSI> Lantern Festival </CSI> this weekend with
lanterns and festive lights.
Inter-lingual
这个周末我们正在为<CSI> 元宵节</CSI> 装饰房子，挂上彩灯，营造节日的
夜晚氛围。
Arabic
Intra-lingual
We’re decorating the house for <CSI> Eid or Ramadan celebration </CSI> this week-
end.
Inter-lingual/< ٮęڡĞﻮﻡ ٮĻٮĞﺮęٮĽٮĽﮟęﺍﻟﻤٮęﺮęﻝﻟـCSI> ę/<ﺍﺣٮĞڡęﺎﻝﺍﻟﻌٮĽﺪ أﻭﺭﻣﺼęﺎﮞCSI>.ﻫﺪęﺍﺍلأﺳٮĻﻮﻉ
Bengali (West Bengal)
Intra-lingual
We’re decorating the house for <CSI> Durga Puja </CSI> this weekend.
Inter-lingual
আমরাএইসপ্তাহােন্তবািড়<CSI>দুগর্াপূজার</CSI> জনঁসাজািচ্ছ।
Bengali (Bangladesh)
Intra-lingual
We’re decorating the house for <CSI> Eid-ul-Fitr </CSI> this weekend.
Inter-lingual
আমরাএইসপ্তাহােন্তবািড়<CSI>ঈদুলিফতেরর</CSI> জনঁসাজািচ্ছ।
Table 7: An example sample from the XCR-Bench corpus along with the parallel Inter-lingual and Intra-lingual
annotations in other cultures.
Action
Appropriacy
Architecture
Art
Communication
Competitiveness
Customs
Dress
Environment
Food and Drink
Individualism
Institutions
Music
Orientations
Power
Rituals
Stereotype
Structure
Styles of Discourse
Thinking
Time
Visible Behaviour
Ways of Dress
Workplace Customs
Workplace Norms
Hall's Cultural Elements
Cultural Reference
Cultural Stereotype
Cultural Value
Social Etiquette
Social Tradition
Sports Tradition
Workplace Culture
CSI Category
14
5
31 27
4
1
2
2
7
6
2
22
3
0
2
3
0
15
0
17
0
8
0
0
0
4
2
0
0
2
0
0
0
2
0
5
0
0
0
2
0
40
0
0
8
0
0
0
0
0
2
0
0
0
0
4
0
0
4
0
3
0
0
2
1
0
0
6
0
4
0
0
0
0
0
10 135 0
0
41
0
43
0
0
0
0
0
0
0
0
4
0
0
14
0
1
1
1
0
0
17
1
2
0
5
2
80
0
4
28
1
11
6
0
0 152 0
36
0
9
5
0
5
0
0
1
0
0
0
0
0
1
4
0
0
0
6
0
0
0
9
0
0
0
0
0
4
0
0
0
15
9
0
0
30
5
2
0
0
4
6
2
0
0
7
4
0
11
3
4
0
0
0
13 18
0
20
40
60
80
100
120
140
Figure 4: Mapping between CSI categories and Hall’s cultural elements in the XCR-Bench Corpus.
18

--- Page 19 ---

Hall’s Level
Cultural Element
Instance from XCR-Bench
Invisible
Action
He’s an <CSI> adrenaline junkie </CSI> who loves skydiving and bungee
jumping.
Communication
He steered conversation away from <CSI> gun laws </CSI> to maintain pleas-
ant dinner atmosphere.
Competitiveness
He’s a <CSI> self-made </CSI> man who built his empire from scratch.
Environment
She loves going to the <CSI> pub </CSI> for a pint after work.
Individualism
She demonstrates <CSI> self-reliance </CSI> by managing projects indepen-
dently.
Power
The board member <CSI> endorses a bottom-up approach </CSI>, empow-
ering employees to contribute to decision-making.
Stereotype
He’s the <CSI> all-American boy next door </CSI> with his football schol-
arship and volunteer work.
Structure
Couples are <CSI> delaying parenthood </CSI> to establish <CSI> financial
stability </CSI> first.
Thinking
The building omitted floor <CSI> 13 </CSI> jumping from 12 to 14 due to
<CSI> superstition </CSI>.
Time
He made sure to arrive 10 minutes early for the meeting because <CSI> punc-
tuality </CSI> is important in American culture.
Semi-visible
Appropriacy
Don’t ask about <CSI> someone’s weight or appearance </CSI> in personal
conversations.
Customs
She is used to <CSI> queue </CSI> politely and wait her turn, even in
crowded places.
Rituals
She always says <CSI> grace </CSI> before dinner, a tradition passed down
through generations.
Styles of Discourse
She said <CSI> ’cheers’ </CSI> when the stranger held the door, a casual
British thanks.
Behavior
He crossed his <CSI> index and middle fingers </CSI> for <CSI> good luck
</CSI> before the exam.
Ways of Dress
He wore a tailored <CSI> suit </CSI> to the job interview but dressed in
casual <CSI> jeans </CSI> and a t-shirt for the barbecue.
Workplace Customs
We’re implementing an <CSI> open-door policy </CSI> in management for
better accessibility and transparency.
Workplace Norms
The manager gave <CSI> constructive criticism </CSI> during the perfor-
mance review.
Visible
Architecture
Their dining table, made of <CSI> White Oak </CSI>, has been in the family
for generations, a testament to its durability.
Art
When she visited the UK, she noticed that every British coin had a portrait of
the reigning <CSI> monarch </CSI>, a tradition that felt like holding a piece
of history.
Dress
Everyone wore their team <CSI> merchandise </CSI> on game day to show
support.
Food and Drink
They enjoyed a <CSI> fish and chips supper </CSI> by the seaside, a classic
British experience.
Institutions
The startup has an <CSI> open office layout </CSI> without walls or dividers.
Music
Listening to a British <CSI> brass band </CSI> at the local fair, she was
struck by the rich, traditional sound.
Table 8: Mapping of cultural elements to Hall’s Triad of Culture with instances from our constructed XCR-Bench
Corpus. The mapping is derived from Hall (1976).
19

--- Page 20 ---

F
Details on Evaluation Metrics
F.1
CSI Identification
We evaluate CSI identification using two complementary metrics: a strict exact-match score and a soft
similarity-based score.
Hard Identification of CSI (HI-CSI). HI-CSI enforces strict exact matching, rewarding only pre-
dictions that precisely replicate ground-truth CSIs.
This metric is particularly suited for evaluating
models in high-stakes applications where partial identifications may not suffice, such as in content
moderation systems requiring unambiguous detection. The sentence-level score HI-CSI is defined as
follows:
• If |Gs| = 0:
HI-CSI =
{
1
if |Ps| = 0,
0
otherwise.
This penalizes false-positive predictions when no CSIs are present in the ground truth.
• If |Gs| > 0:
HI-CSIs =
1
|Gs|
∑
g∈Gs
I(g ∈Ps),
where I(·) is the indicator function, equal to 1 if the condition holds (i.e., an exact string match
exists in Ps) and 0 otherwise. Note that if duplicate CSIs appear in Gs, each is evaluated indepen-
dently, though matches are checked via membership, allowing a single matching prediction to satisfy
multiple identical ground-truth entries if present.
20

--- Page 21 ---

The overall HI-CSI score for the dataset is the average across all sentences, scaled to a percentage for
interpretability:
HI-CSI =
(
1
|D|
∑
s∈D
HI-CSIs
)
This ranges from 0 (no matches) to 1 (perfect alignment across all sentences).
Soft Identification of CSI (SI-CSI).To account for minor surface-form variations, we compute a
soft CSI matching score based on normalized Levenshtein similarity. For each sentence n, the extracted
ground-truth CSI set G(n) = {g(n)
1 , . . . , g(n)
mn} and the predicted CSI set P (n) = {p(n)
1 , . . . , p(n)
kn } are
compared using a similarity-based one-to-one matching procedure, where mn = |G(n)| and kn = |P (n)|
denote the numbers of ground-truth and predicted CSIs, respectively.
Pairwise normalised Levenshtein similarities s(g(n)
i
, p(n)
j
) = 1 −
dL(g(n)
i
,p(n)
j
)
max(ℓ(g(n)
i
),ℓ(p(n)
j
)) are first computed
between all ground-truth and predicted CSIs, and an optimal one-to-one alignment is then obtained using
the Hungarian algorithm so that the total similarity of the matched pairs is maximized while prevent-
ing reuse of any CSI. Based on the optimal one-to-one alignment, a soft F1 score is computed for each
sentence as
SI-CSI = Soft (F1)n = 1[mn = 0∧kn = 0]+1[mn > 0∧kn > 0]
2
mn + kn
mn
∑
i=1
kn
∑
j=1
s(g(n)
i
, p(n)
j
) X∗(n)
ij
,
where X∗(n)
ij
denotes the optimal one-to-one assignment variable, which takes the value 1 when g(n)
i
is
matched to p(n)
j
and 0 otherwise, so that both missing ground-truth CSIs and over-generated predictions
are penalized.
HI-CSI measures strict span identification accuracy, while SI-CSI provides graded credit for near-
matches without relying on heuristic substring rules.
F.2
CSI Prediction
We evaluate CSI prediction using two complementary metrics: a strict exact-match score and a soft
semantic similarity score.
Hard Prediction of CSI (HP-CSI). HP-CSI requires strict exact matching (case-insensitive) for
paired CSIs, rewarding only precise replications in the corresponding order. The sentence-level score
HP-CSIs is defined as:
HP-CSIs =
min(n,m)
∑
i=1
I(gi.lower() = pi.lower()),
where I(·) is the indicator function, equal to 1 if the condition holds and 0 otherwise. This sums the
number of exact matches across the paired elements up to the minimum length. The overall HP-CSI score
for the dataset is the average across all sentences, scaled to account for varying CSI counts (interpretable
as a percentage when normalized by average CSI count per sentence):
HP-CSI =
(
1
|D|
∑
s∈D
HP-CSIs
)
This value scales with the average number of CSIs per sentence; for datasets with one CSI per sentence,
it ranges from 0 to 1.
Soft Prediction of CSI (SP-CSI). SP-CSI extends HP-CSI by incorporating semantic similarity for non-
exact pairs, using cosine similarity on embeddings generated by the SentenceTransformer model (‘all-
mpnet-base-v2’). This allows partial credit for predictions that capture similar meaning despite lexical
21

--- Page 22 ---

differences. The sentence-level score SP-CSIs is defined as:
SP-CSIs =
min(n,m)
∑
i=1
mi,
where for each paired index i,
mi =
{
1
if gi.lower() = pi.lower() (exact match),
cos(e(gi), e(pi))
otherwise,
and e(·) denotes the embedding function from the SentenceTransformer model, with cos(u, v) =
u·v
||u|| ||v||
being the cosine similarity. The overall SP-CSI score is:
SP-CSI =
(
1
|D|
∑
s∈D
SP-CSIs
)
his value scales with the average number of CSIs per sentence.
F.3
CSI Adaptation
We evaluate CSI adaptation along two complementary dimensions: (i) semantic fidelity of the adapted
CSIs themselves, and (ii) overall sentence-level semantic preservation, as sentence structure may change
during adaptation. We perform both intra-lingual (English-to-English) and inter-lingual (cross-language)
evaluations. 7aragraphSentence-Level Semantic Similarity (SENTbert). To assess whether the adapted
sentence preserves the meaning of the original, we compute BERTScore F1 between the model-generated
sentence sout and the ground-truth adapted sentence sgt:
SENTbert = F1bert
(
sout, sgt)
.
BERTScore leverages contextual embeddings from BERT to compute F1 scores based on pairwise to-
ken similarities, making it particularly effective for assessing paraphrase quality and semantic preser-
vation in natural language generation tasks. With baseline rescaling enabled to normalize scores rela-
tive to a random baseline, improving interpretability and cross-model comparability, the sentence-level
full-sentence score is SENTBERT,s = F1′
BERT(as, gs), using the entire strings as and gs (where gs is
the ground-truth sentence and as the adapted output). The overall dataset-level metric is the average:
SENTBERT =
1
|D|
∑
s∈D SENTBERT,s, where D denotes the dataset of sentence pairs. 7aragraphCSI-
Level Semantic Similarity (CSIbert). Given aligned gold and predicted CSI spans G = {gi}n
i=1 and
O = {oi}n
i=1 extracted from <CSI> tags, we compute BERTScore F1 for each pair:
simCSI(gi, oi) = F1bert(gi, oi).
The final CSI-level score is the average across all spans:
CSIbert = 1
n
n
∑
i=1
simCSI(gi, oi).
CSIs are extracted from both ground-truth and adapted texts via regular expressions matching con-
tent within <CSI> tags, producing ordered lists of strings. We enforce that the number of extracted
CSIs matches between ground-truth and output for each sentence, ensuring paired evaluation.
Let
Gs = [g(s)
1 , g(s)
2 , . . . , g(s)
ks ] be the ordered list of ground-truth CSIs (where ks = |Gs|) and As =
[a(s)
1 , a(s)
2 , . . . , a(s)
ks ] the corresponding list of adapted CSIs, with |Gs| = |As| = ks. The sentence-level
CSI score aggregates per-CSI F1 scores with baseline rescaling: CSIBERT,s = 1
ks
∑ks
i=1 F1′
BERT(a(s)
i , g(s)
i ),
22

--- Page 23 ---

if ks > 0; otherwise, it defaults to 0 (though datasets typically ensure CSIs exist). The overall dataset-
level metric is the average: CSIBERT =
1
|D|
∑
s∈D CSIBERT,s. Category-wise scores can be derived
by partitioning D into subsets Dc based on CSI categories and computing averages within each. 7ara-
graphIntra- vs. Inter-Lingual Evaluation. For intra-lingual (English) adaptation, we compute BERTScore
using bert-base-uncased. For inter-lingual adaptation, we employ language-specific BERTScore models:
bert-base-arabic (Safaya et al., 2020) for Arabic, chinese-bert-wwm-ext (Cui et al., 2019) for Chinese,
and bangla-bert-base (Sarker, 2020) for Bengali, to ensure that semantic similarity is evaluated within
the appropriate linguistic and cultural representation space. For inter-lingual evaluation, we extend this
framework using multilingual models (e.g., bert-base-multilingual-uncased) to handle cross-language
pairs, computing analogous SENTBERT-multi and CSIBERT-multi scores. 7aragraphDiscussion and Ratio-
nale. These metrics emphasize semantic equivalence, with CSIBERT isolating performance on culturally
sensitive adaptations- critical for ensuring biases or sensitivities are appropriately mitigated without al-
tering core meaning. The use of baseline rescaling maps scores to a more intuitive [0,1] range, where
higher values indicate better alignment. Compared to n-gram-based metrics like BLEU, BERTScore
better handles paraphrasing and synonyms, aligning with adaptation goals. Limitations include: (1) re-
liance on BERT’s English-centric biases in intra-lingual settings and (2) computational cost and latency
from embedding computations, though batched inference mitigates this. In practice, metrics are imple-
mented using the Hugging Face bert-score library, with time complexity dominated by BERT inference:
O(|D| × (L2
s)) per sentence for greedy matching in BERTScore, where Ls is token length (typically
<512).
23

--- Page 24 ---

G
Additional Results
G.1
CSI Identification & Prediction
Invisible
Semi­visible
Visible
40
45
50
55
60
65
70
HI­CSI (%)
deepseek
llama3
qwen
gpt
DeepSeek­R1­Distill­Qwen­32B
gemini
claude
olmo
(a) Hard Exact-Match (HI-CSI) for Hall’s Triad of Culture
Invisible
Semi­visible
Visible
47.5
50.0
52.5
55.0
57.5
60.0
62.5
65.0
67.5
SI­CSI (%)
llama 3.3
deepseek­r1­distill­qwen
olmo 2
gpt 4o
gemini 2 flash
claude 3.7 sonnet
qwen 2.5
deepseek r1
(b) Soft Edit-Similarity (SI-CSI) for Hall’s Triad of Culture
Figure 5: Performance of LLMs across Hall’s Triad of Culture (visible, semi-visible, and invisible) for CSI Iden-
tification. The HI-CSI metric exhibits the lowest overall performance for Semi-visible level, indicating that LLMs
struggle with exact CSI identification for this level. In contrast, SI-CSI scores reveal a systematic performance
decline from Visible to Invisible cultural levels.
Invisible
Semi­visible
Visible
30
35
40
45
50
HP­CSI (%)
deepseek­r1­distill­qwen
olmo
llama3 sdsc
gemini
qwen
deepseek chat
claude 3.7 sonnet
gpt
(a) Hard Exact-Match (HP-CSI) for Hall’s Triad of Culture
Invisible
Semi­visible
Visible
65.0
67.5
70.0
72.5
75.0
77.5
80.0
82.5
85.0
SP­CSI (%)
deepseek­r1­distill­qwen
olmo
gemini
llama3 sdsc
qwen
gpt
claude 3.7 sonnet
deepseek chat
(b) Soft Semantic-Similarity (SP-CSI) for Hall’s Triad of Cul-
ture
Figure 6: Performance of LLMs across Hall’s Triad of Culture (visible, semi-visible, and invisible) for CSI Predic-
tion. Similar to HI-CSI from CSI identification, the SP-CSI metric exhibits a systematic performance decline from
Visible to Invisible cultural levels. In contrast, HP-CSI scores shows a mixed performance evaluation over all the
levels.
24

--- Page 25 ---

Hall’s Cultural Element
DS-Distill
Claude
DS-R1
Gemini
GPT-4o
Llama-3.3
OLMo-2
Qwen-2.5
HI
SI
HI
SI
HI
SI
HI
SI
HI
SI
HI
SI
HI
SI
HI
SI
Action
51.43
54.91
67.14
73.51
64.29
63.74
58.57
63.64
65.71
66.35
61.43
51.43
54.29
59.68
61.43
66.04
Appropriacy
19.40
39.86
19.40
38.02
24.63
39.32
18.66
30.85
23.88
37.76
23.13
30.31
22.39
38.73
32.84
46.38
Architecture
38.89
48.55
38.89
50.65
72.22
67.84
55.56
63.23
55.56
57.61
41.67
45.70
33.33
46.40
55.56
65.57
Art
60.00
53.25
60.00
62.84
73.33
59.34
50.00
53.64
60.00
55.95
93.33
65.37
50.00
54.46
70.00
57.14
Communication
36.49
46.60
40.54
52.31
36.49
44.81
27.03
39.54
24.32
42.66
28.38
35.94
33.78
53.13
32.43
46.81
Competitiveness
68.75
66.23
62.50
68.65
62.50
68.63
56.25
66.99
56.25
66.99
62.50
63.80
56.25
69.04
62.50
66.96
Customs
43.22
55.94
38.14
56.83
50.85
58.50
38.98
51.66
40.68
53.54
42.37
46.72
29.66
44.61
47.46
55.98
Dress
25.00
42.42
50.00
56.10
50.00
56.10
25.00
41.51
25.00
44.91
50.00
50.93
25.00
41.44
50.00
56.94
Environment
88.89
65.43
77.78
76.94
88.89
78.40
88.89
82.41
66.67
65.24
55.56
48.87
77.78
85.89
77.78
69.88
Food and Drink
72.22
72.32
66.67
75.28
75.00
75.34
69.44
73.80
72.22
77.20
55.56
55.47
69.44
83.09
63.89
64.71
Individualism
38.89
53.71
33.33
53.35
55.56
56.64
33.33
43.08
55.56
49.34
55.56
55.20
50.00
64.64
55.56
63.23
Institutions
71.05
61.02
50.00
60.87
74.56
61.14
51.75
56.25
64.04
61.14
78.95
59.58
41.23
60.65
71.93
63.64
Music
40.00
49.13
60.00
72.83
70.00
82.40
70.00
84.44
30.00
61.39
70.00
62.17
50.00
74.72
70.00
82.40
Orientations
0.00
20.00
0.00
20.00
100.00
33.33
100.00
66.67
0.00
7.41
100.00
33.33
0.00
0.00
0.00
0.00
Power
42.86
37.97
28.57
57.46
57.14
60.85
42.86
55.25
42.86
56.75
57.14
45.75
42.86
61.50
42.86
62.10
Rituals
70.10
65.35
58.25
69.71
73.20
66.95
66.49
71.84
67.01
66.17
68.04
53.80
58.76
68.80
68.04
67.74
Stereotype
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
100.00
66.67
100.00
100.00
100.00
100.00
Structure
25.00
31.02
31.25
45.24
45.31
46.68
25.00
36.77
34.38
45.12
40.62
35.45
31.25
44.24
37.50
42.60
Styles of Discourse
50.00
66.83
12.50
70.16
37.50
74.64
37.50
66.96
25.00
70.71
25.00
63.42
12.50
56.71
37.50
69.77
Thinking
45.83
48.08
50.00
57.83
62.50
59.56
50.00
58.93
45.83
53.24
58.33
51.07
54.17
60.37
54.17
55.82
Time
33.33
35.84
0.00
20.03
33.33
32.88
33.33
43.99
33.33
46.95
33.33
38.43
33.33
34.32
33.33
32.88
Visible Behavior
25.00
48.84
25.00
46.89
41.67
62.75
25.00
44.64
25.00
46.40
16.67
36.75
16.67
42.39
16.67
45.24
Ways of Dress
66.67
72.36
25.00
40.91
75.00
67.62
33.33
43.87
58.33
56.04
58.33
56.37
16.67
30.79
33.33
44.14
Workplace Customs
85.71
77.62
85.71
90.24
85.71
75.95
71.43
84.80
85.71
82.38
71.43
67.62
71.43
89.29
85.71
80.71
Workplace Norms
94.44
88.50
94.44
87.04
94.44
88.89
83.33
81.48
94.44
96.30
72.22
69.05
83.33
85.19
94.44
88.89
Table 9: Per-category (25) performance for HI-CSI (HI) and SI-CSI (SI) across Hall’s cultural elements. Model
abbreviations: DS-Distill = DeepSeek-R1-Distill-Qwen-32B; Claude = Claude-3.7-Sonnet; DS-R1 = DeepSeek-
R1; Gemini = Gemini-2.0-Flash; OLMo-2 = OLMo-2-32B; Qwen-2.5 = Qwen-2.5-Max. Values are percentages;
higher is better.
25

--- Page 26 ---

G.2
CSI Adaptation
Cultural
 Reference
Cultural
 Stereotype
Cultural
 Value
Social
 Etiquette
Social
 Tradition
Sports
 Tradition
Workplace
 Culture
Claude-3.7-Sonnet
DeepSeek-R1-
Distill-Qwen-32B
Deepseek R1
GPT-4o
Gemini-2.0-Flash
Llama-3.3
OLMo-2-32B
Qwen-2.5-Max
33.0
35.1
28.5
37.2
35.4
43.5
34.8
33.9
34.7
44.8
45.3
27.1
20.4
45.9
34.0
40.9
43.1
40.5
35.4
30.8
38.2
29.0
30.5
32.1
36.6
32.8
27.9
34.1
35.3
47.4
35.4
42.5
39.4
41.5
36.3
33.8
36.9
43.8
40.5
36.3
35.1
38.7
32.4
40.1
46.3
41.9
36.3
29.4
37.7
30.2
39.1
30.1
36.7
34.1
30.5
37.3
25
30
35
40
45
Gain (Inter 
 Intra) [pp]
(a) Inter-Intra CSI Adaptation Gain for Arabic
Cultural
 Reference
Cultural
 Stereotype
Cultural
 Value
Social
 Etiquette
Social
 Tradition
Sports
 Tradition
Workplace
 Culture
Claude-3.7-Sonnet
DeepSeek-R1-
Distill-Qwen-32B
Deepseek R1
GPT-4o
Gemini-2.0-Flash
Llama-3.3
OLMo-2-32B
Qwen-2.5-Max
30.8
42.6
20.5
32.5
36.8
37.5
40.5
29.5
44.0
38.7
37.3
35.1
32.0
35.5
31.0
41.9
39.1
41.5
38.0
36.5
35.5
27.9
42.7
22.2
33.8
33.7
36.0
37.7
32.5
50.9
34.4
37.8
39.4
32.1
34.1
31.9
42.1
37.7
40.8
38.6
35.3
35.2
30.7
41.4
44.2
40.0
36.8
35.4
39.2
30.2
40.9
39.2
39.1
38.7
48.3
41.5
25
30
35
40
45
50
Gain (Inter 
 Intra) [pp]
(b) Inter-Intra CSI Adaptation Gain for Chinese
Figure 7: Inter–Intra CSI adaptation gain for Arabic and Chinese. The heatmap reports the difference between
inter-lingual and intra-lingual CSI adaptation scores (Inter −Intra) under the CSIbert metric across models and CSI
categories. Positive gains across most CSI categories indicate that LLMs adapt to Arabic and Chinese cultural
content more effectively in inter-lingual settings than in intra-lingual ones.
Cultural
 Reference
Cultural
 Stereotype
Cultural
 Value
Social
 Etiquette
Social
 Tradition
Sports
 Tradition
Workplace
 Culture
Claude-3.7-Sonnet
DeepSeek-R1-
Distill-Qwen-32B
Deepseek R1
GPT-4o
Gemini-2.0-Flash
Llama-3.3
OLMo-2-32B
Qwen-2.5-Max
10.1
14.4
18.1
9.5
13.8
12.0
11.1
0.3
24.7
19.3
5.1
7.2
9.9
14.8
7.5
17.0
2.4
9.6
14.2
17.6
9.4
4.3
20.4
-0.8
7.5
10.7
23.7
10.9
14.0
25.3
20.7
15.0
19.2
15.4
19.4
4.3
19.2
0.4
12.1
13.3
18.5
10.4
16.0
27.8
14.9
20.0
19.2
18.5
22.2
11.8
16.0
27.6
21.5
24.7
23.3
24.9
0
5
10
15
20
25
Gain (Inter 
 Intra) [pp]
(a) Inter-Intra CSI Adaptation Gain for Bn(West Bengal)
Cultural
 Reference
Cultural
 Stereotype
Cultural
 Value
Social
 Etiquette
Social
 Tradition
Sports
 Tradition
Workplace
 Culture
Claude-3.7-Sonnet
DeepSeek-R1-
Distill-Qwen-32B
Deepseek R1
GPT-4o
Gemini-2.0-Flash
Llama-3.3
OLMo-2-32B
Qwen-2.5-Max
9.0
15.0
13.5
9.7
15.7
10.8
10.9
2.2
25.1
8.3
7.4
9.6
7.6
13.7
6.2
17.3
7.0
9.7
16.9
17.3
9.2
7.9
19.9
11.4
7.1
14.7
21.4
11.2
12.8
24.7
18.1
14.1
19.2
13.7
19.6
2.8
19.2
5.7
11.4
16.5
18.7
10.9
14.0
28.5
11.1
19.2
22.1
18.7
22.3
11.7
17.0
15.6
21.7
25.9
20.5
25.1
5
10
15
20
25
Gain (Inter 
 Intra) [pp]
(b) Inter-Intra CSI Adaptation Gain for Bn(Bangladesh)
Figure 8: Inter–Intra CSI adaptation gain for Bengali (West Bengal and Bangladesh). The heatmap reports the
difference between inter-lingual and intra-lingual CSI adaptation scores (Inter −Intra) under the CSIbert metric
across models and CSI categories. Positive values indicate improved adaptation when cultural content is generated
directly in the target language rather than adapted within English.
26

--- Page 27 ---

Invisible
Semi-visible
Visible
0.2
0.3
0.4
0.5
0.6
0.7
CSI-Level Semantic Similarity
Intra
Inter
(a) Arabic CSIbert for Hall’s Triad of Culture
Invisible
Semi-visible
Visible
0.3
0.4
0.5
0.6
0.7
CSI-Level Semantic Similarity
Intra
Inter
(b) Chinese CSIbert for Hall’s Triad of Culture
Figure 9: Performance of LLMs on CSI Adaptation (CSIbert) across Hall’s cultural triad (visible, semi-visible,
and invisible) in Arabic and Chinese. Solid lines denote inter-lingual adaptation, while dashed lines denote intra-
lingual adaptation. Across models, inter-lingual adaptation consistently outperforms intra-lingual adaptation, and
performance degrades systematically as cultural elements transition from visible to invisible.
Invisible
Semi-visible
Visible
0.20
0.25
0.30
0.35
0.40
0.45
0.50
CSI-Level Semantic Similarity
Intra
Inter
(a) Bengali (WB) CSIbert for Hall’s Triad of Culture
Invisible
Semi-visible
Visible
0.20
0.25
0.30
0.35
0.40
0.45
0.50
CSI-Level Semantic Similarity
Intra
Inter
(b) Bengali (BD) CSIbert for Hall’s Triad of Culture
Figure 10: Performance of LLMs on CSI Adaptation (CSIbert) across Hall’s triad of cultural visibility (visible,
semi-visible, and invisible) in Bengali for West Bengal (WB) and Bangladesh (BD). Solid lines indicate inter-
lingual adaptation, while dashed lines indicate intra-lingual adaptation. For both cultural contexts, most models
achieve higher performance in the inter-lingual setting, with a small number of exceptions. In contrast to Arabic
and Chinese, the decline in performance from visible to invisible cultural elements is noticeably less pronounced.
27

--- Page 28 ---

Language
Model
Best Method
Score
Worst Method
Score
Arabic
DeepSeek-R1
Couplet (Cultural Equivalent +
Paraphrase)
1.00
Cultural Equivalent
0.50
Arabic
Gemini-2.0-Flash
Couplet (Cultural Equivalent +
Classifier)
0.86
Couplet (Cultural Equivalent +
Neutralization)
0.57
Arabic
GPT-4o
Cultural Equivalent
0.79
Cultural Equivalent +
Componential Analysis
0.53
Arabic
Llama-3.3
Couplet (Cultural Equivalent +
Accepted Standard Translation)
1.00
Couplet (Cultural Equivalent +
Neutralization)
0.50
Arabic
OLMo-2-32B
Couplet (Cultural Equivalent +
Literal Translation)
1.00
Cultural Equivalent + Labeling
0.50
Arabic
Qwen-2.5-Max
Transference
0.78
Paraphrase
0.57
Bengali
Claude-3.7-Sonnet
Couplet (Transference +
Naturalization)
1.00
Componential Analysis
0.46
Bengali
DeepSeek-R1
Couplet (Cultural Equivalent +
Accepted Standard Translation)
0.90
Cultural Equivalent
0.41
Bengali
Gemini-2.0-Flash
Cultural Equivalent + Labeling
0.80
Cultural Equivalent + Label
0.43
Bengali
GPT-4o
Literal Translation
0.88
Paraphrase
0.41
Bengali
Llama-3.3
Couplet (Cultural Equivalent +
Literal Translation)
0.90
Cultural Equivalent
0.43
Bengali
Qwen-2.5-Max
Couplet (Cultural Equivalent +
Paraphrase)
0.81
Transference
0.42
Chinese
DeepSeek-R1
Cultural Equivalent
1.00
Cultural Equivalent
0.50
Chinese
Gemini-2.0-Flash
Couplet (Transference + Labeling)
0.79
Couplet (Cultural Equivalent +
Paraphrase)
0.53
Chinese
GPT-4o
Couplet (Cultural Equivalent +
Accepted Standard Translation)
1.00
Couplet (Cultural Equivalent +
Paraphrase)
0.50
Chinese
Llama-3.3
Cultural Equivalent
1.00
Cultural Equivalent
0.50
Chinese
OLMo-2-32B
Cultural Equivalent
1.00
Cultural Equivalent
0.51
Chinese
Qwen-2.5-Max
Couplet (Cultural Equivalent +
Naturalization)
1.00
Couplet (Cultural Equivalent +
Literal Translation)
0.51
Table 10: Best- and worst-performing adaptation methods (by average CSI score) for each language–model pair.
“Couplet” denotes a combination of two translation strategies. Cultural Equivalent is abbreviated as CE in the main
text.
28

--- Page 29 ---

H
Prompts Used for Evaluation
H.1
CSI Identification
You are a highly skilled and culturally aware agent with expertise in identifying Culture-Specific Items (CSIs). CSIs are
words, phrases, or concepts that are specific to a particular culture or carry significant cultural meaning. They depend
on cultural context and can vary widely across cultures. CSIs encompass natural elements like animals, plants, and
environmental features (ecology); physical objects like food, clothing, housing, and tools (material culture); activities
related to work and leisure (social culture); political, social, legal, religious, and artistic concepts (organizations,
customs, and ideas); and non-verbal communication or behaviors like gestures and habits.
Your task is to identify the CSI(s) in the given sentence and enclose them with ‘<CSI>‘ and ‘</CSI>‘ tags. The CSIs
in this task will mostly pertain to American/Western/British Culture, so prioritize identifying items specific to these
cultural contexts. Do not add any explanations, notes, or unnecessary text—only provide the revised sentence with the
CSI(s) properly tagged.
One example input-output pair is given below for your reference: Input: They’re tailgating before the football game
with grills and coolers in the parking lot. Output: They’re <CSI> tailgating </CSI> before the football game with grills
and coolers in the parking lot.
Now process the following sentences exactly as instructed: Input:
Figure 11: Evaluation Prompt for CSI Identification Task.
H.2
CSI Prediction
You are a highly skilled and culturally aware agent with expertise in predicting Culture-Specific Items (CSIs). CSIs are
words, phrases, or concepts that are specific to a particular culture or carry significant cultural meaning. They depend
on cultural context and can vary widely across cultures. CSIs encompass natural elements like animals, plants, and
environmental features (ecology); physical objects like food, clothing, housing, and tools (material culture); activities
related to work and leisure (social culture); political, social, legal, religious, and artistic concepts (organizations,
customs, and ideas); and non-verbal communication or behaviors like gestures and habits.
You’ll be given inputs where each sentence will contain a ‘[MASK]‘ tag, where the CSI has been masked. The CSI is
surrounded with a beginning <CSI> tag and an ending </CSI> tag. Your task is to predict the most appropriate CSI to
fill in the ‘[MASK]‘ based on the surrounding context. The CSIs in this task will mostly pertain to American/Western/
British Culture, so prioritize predicting items specific to these cultural contexts.
Replace the [MASK] with the predicted CSI. Do not add any explanations, notes, or unnecessary text—only provide
the revised sentence with the predicted CSI filled in.
One example input-output pair is given below for your reference: Input: ”Every Friday night, her grandmother heads
to the local <CSI> [MASK]</CSI>, a ritual she has enjoyed for decades.”
Output: ”Every Friday night, her grandmother heads to the local <CSI> bingo hall</CSI>, a ritual she has enjoyed for
decades.”
Now process the following sentences exactly as instructed:
Input:
Figure 12: Evaluation Prompt for CSI Prediction Task.
29

--- Page 30 ---

H.3
CSI Adaptation
You are an expert in cultural adaptation and linguistic transformation with a deep understanding of Bengali/Chinese/
Arabic culture, traditions, and social practices. You specialize in providing culturally sensitive adaptations that align
with the values, norms, and etiquette of Bengali/Chinese/Arabic people. You will be given an input sentence containing
Culture-Specific Items (CSIs) that mostly pertain to American/Western/British Culture. Your task is to adapt sentences
containing <CSI> tags into the context of Bengali/Chinese/Arabic society, ensuring both cultural relevance and linguis-
tic accuracy. You can use one or a combination of the following methods appropriate for adaptation:
1. Transference: Keep the original word unchanged in the adaptation.
2. Cultural Equivalent: Use a similar term from the target culture.
3. Neutralization: Explain what the term means or does.
4. Literal Translation: Translating the word directly to target culture.
5. Label: Add a brief explanation or tag to the term.
6. Naturalization: Adapt the word to fit the target language’s spelling or sound.
7. Componential Analysis: Break the term into parts and explain each.
8. Deletion: Remove unnecessary words or phrases.
9. Couplet: Combine two adaptation methods
10. Accepted Standard Translation: Use a commonly accepted adaptation.
11. Paraphrase or Gloss: Give a longer explanation or footnote.
12. Classifier: Add a general category to clarify the term’s meaning.
Your task is to adapt the following sentences containing <CSI> tags into Bengali/Chinese/Arabic culture. Replace
inside the <CSI> tags with culturally relevant practices, behaviors, or terms. Do not remove the <CSI> tags. In case
there is no cultural equivalent in the target culture, return ‘Non-transferable’.
Provide both Intra-lingual adaptation (Contextualized for Bengali culture but written in English) and Inter-lingual adap-
tation (Translated and adapted into Bengali/Chinese/Arabic for each input. Ensure cultural accuracy, politeness, and
respect in all adaptations. Also output what method you used for the adaptation. The output format should be [Intra-
lingual adaptation, Inter-lingual adaptation, Adaptation method used]. Do not add any explanation.
Now adapt the following sentences:
Input:
Figure 13: Evaluation Prompt for CSI Adaptation Task.
30

```
