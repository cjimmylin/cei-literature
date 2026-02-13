---
title: "2025-Sahoo-DIWALI Diversity and Inclusivity aWare cuLture specific Items for - PDF Extract"
source_pdf: "2025-Sahoo-DIWALI Diversity and Inclusivity aWare cuLture specific Items for.pdf"
pages: 28
extracted_at: "2026-02-13T09:50:30.214391"
---

# PDF Extract: 2025-Sahoo-DIWALI Diversity and Inclusivity aWare cuLture specific Items for

**Source PDF:** 2025-Sahoo-DIWALI Diversity and Inclusivity aWare cuLture specific Items for.pdf
**Total Pages:** 28

---

## Content

```
--- Page 1 ---

DIWALI - Diversity and Inclusivity aWare cuLture specific Items for
India
Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context
Pramit Sahoo*
Maharaj Brahma*
Maunendra Sankar Desarkar
Natural Language and Information Processing Lab (NLIP)
Indian Institute of Technology Hyderabad
Hyderabad, India
pramitsahoo.gnipst@gmail.com, cs23resch01004@iith.ac.in, maunendra@cse.iith.ac.in
Abstract
Large language models (LLMs) are widely
used in various tasks and applications. How-
ever, despite their wide capabilities, they are
shown to lack cultural alignment (Ryan et al.,
2024; AlKhamissi et al., 2024) and produce
biased generations (Naous et al., 2024) due to
a lack of cultural knowledge and competence.
Evaluation of LLMs for cultural awareness
and alignment is particularly challenging due
to the lack of proper evaluation metrics and
unavailability of culturally grounded datasets
representing the vast complexity of cultures at
the regional and sub-regional levels. Existing
datasets for culture specific items (CSIs)
focus primarily on concepts at the regional
level and may contain false positives.
To
address this issue, we introduce a novel CSI
dataset for Indian culture, belonging to 17
cultural facets. The dataset comprises ∼8k
cultural concepts from 36 sub-regions.
To
measure the cultural competence of LLMs on
a cultural text adaptation task, we evaluate the
adaptations using the CSIs created, LLM as
Judge, and human evaluations from diverse
socio-demographic region.
Furthermore,
we perform quantitative analysis demon-
strating selective sub-regional coverage and
surface-level adaptations across all consid-
ered LLMs.
Our dataset is available here:
https://huggingface.co/datasets/nlip/DIWALI,
project
webpage1,
and
our
codebase
with model outputs can be found here:
https://github.com/pramitsahoo/culture-
evaluation.
1
Introduction
Large language models (LLMs), despite having
vast knowledge and being trained on extensive
large data, are shown to lack cultural knowledge
and competence (Naous et al., 2024; Wang et al.,
*Equal contributions
1https://nlip-lab.github.io/nlip/publications/diwali/
Clothing
Drink
Cuisine
Rituals
Traditions
0
100
200
300
400
500
Number of Concepts
205
157
176
183
191
386
483
425
329
215
CANDLE
DIWALI
Figure 1: Comparison of the number of cultural con-
cepts between CANDLE (Nguyen et al., 2023) and Ours
(DIWALI), highlighting differences in coverage of cul-
tural concepts for five facets (clothing, drink, cuisine,
rituals, and traditions) available in CANDLE (Domain
= Country, Subject = India).
2024; Masoud et al., 2025). This is primarily at-
tributed to highly biased pre-training data towards
Western culture (Li et al., 2024; Naous and Xu,
2025; Li et al., 2025). Cultural text adaptation
refers to modifying text from a general or specific
culture to align with a particular target cultural
group’s linguistic, social, and conceptual norms.
Cultural adaptation has a wide range of appli-
cations, ranging from education (Burstein et al.,
2007), dialogue (Singh et al., 2024), movie sub-
titling (Ferreira, 2024; El-Farahaty and Alwazna,
2024), hospitality (Radojevi´c et al., 2024), adver-
tisement (Barthwal and Gupta, 2011; Li, 2024),
cross-cultural communication (Wilczewski et al.,
2019), and storytelling (Bhatt and Diaz, 2024;
Hamna et al., 2025). However, ensuring effective
and emotionally resonating cultural adaptation is
challenging, as it requires deep understanding and
knowledge of social norms, subjective historical
references, resonating events, and cultural nuances.
With its vast linguistic and cultural diversity, In-
dia presents a unique challenge for culture-driven
arXiv:2509.17399v2  [cs.CL]  16 Dec 2025

--- Page 2 ---

NLP systems. In particular, India houses 28 states
and eight union territories2, each with multiple
languages, dialects, traditions, and socio-cultural
norms. Furthermore, cultural diversity exists at
the state level and within sub-regions.
For ex-
ample, the state of Assam has communities like
Bodo, Rabha, Karbi, and so on – each with distinct
cultural norms, artifacts, and language3. Despite
recent advances, existing LLMs struggle with cul-
tural adaptation. Studies (Naous et al., 2024) have
shown that LLMs trained on English-centric cor-
pora often fail to generate culturally appropriate
content, especially for cultures from different parts
of the world. In this work, we systematically eval-
uate multiple open-weight LLMs for cultural text
adaptation on closed-text generation. In particular,
we utilize existing text corpora from the education
domain belonging to American culture. We rely on
cultural concepts to assess the cultural competence
of various LLMs for cultural text adaptation tasks.
Culture Specific Items (CSIs) represent a particu-
lar culture’s concepts, objects, items, and customs.
For example, Mekhela Chador (clothing), Pongal
(food), and Darjeeling Tea (drink) are cultural con-
cepts from India. Prior work, CANDLE (Nguyen
et al., 2023), has made foundational efforts to auto-
matically extract culturally specific concepts from
large web text for various cultures. In another work,
DOSA (Seth et al., 2024) builds community-driven
cultural artifacts for a sub-regional culture belong-
ing to India. However, these datasets have a limited
representation of cultural concepts from India. Fig-
ure 1 shows the comparison of the created dataset
with respect to existing concepts from the CAN-
DLE4 framework. To address this gap, we built
a novel, large-scale dataset of CSIs for the Indian
subregion. In particular, our dataset contains ∼8k
cultural concepts from 17 facets. We evaluate using
automatic CSI-based and human evaluation met-
rics to systematically assess the adaptation quality
of various LLMs. Our dataset provides a valuable
resource to the community for further research in
the comprehensive and standardized assessment of
cultural text adaptation. We define culture at the
regional or country level, focusing on India.
In summary, our contributions are as follows:
• We present DIWALI, a high-quality Culture
Specific Items (CSIs) dataset of India, cov-
2https://knowindia.india.gov.in/states-uts/
3https://assam.gov.in/about-us/391
4https://candle.mpi-inf.mpg.de/
ering a total of 36 subregions5. Our dataset
contains a total of 8,817 concepts from 17
cultural facets.
• We assess 7 open-weight models across 3
LLM families using both automatic and hu-
man evaluation metrics for cultural text adap-
tation.
• We conduct a cultural sub-regional evaluation
and analysis of LLMs in the context of cultural
text adaptation.
2
Culture & Culture Specific Items
Culture is a multifaceted and complex construct. It
means different things to different groups of people.
It encompasses knowledge, beliefs, morals, val-
ues, and customs. Broadly, we can divide culture
into material and non-material components. Ma-
terial components include tangible elements such
as food, dress, houses, and ornaments. In contrast,
non-material components refer to symbols, ideas,
beliefs, norms, values, morality, and attitudes that
guide social behavior. For example, the practice
of fasting during Navratris6. Culture is a com-
plex concept and hard to define. As a result, the
community has turned to using demographic and
semantic proxies to approximately define culture
(Adilazuarda et al., 2024). Demographic proxies
typically include geographical region, language,
gender, race, religion, education, and ethnicity. In
contrast, people associate semantic proxies with
emotional expressions, food habits, social and po-
litical relations, actions, and naming conventions.
In this work, we consider culture as a regional de-
mographic proxy – with the geographical country
India as a region and its states and union territories
as sub-regions.
Newmark (2003) defined culture as “... the way
of life and its manifestations that are peculiar to
a community that uses particular languages as a
means of expression.” This definition views culture
as a collection of objects, customs, and traditions
that hold meaning within a specific community.
Newmark (2003) categorizes cultural manifesta-
tions into five collections or facets: (a) ecology,
(b) material culture, (c) social culture, (d) organi-
zations, customs, activities, procedures, concepts,
and (e) gestures and habits. Culture Specific Items
represent concepts, objects, items, and customs that
hold significant cultural importance and relevance
5Represents states and union territories of India
6a religious observance common in Northern India.

--- Page 3 ---

to a particular culture. It may vary across different
subregions. Existing CSI datasets, such as CAN-
DLE and DOSA, are limited in scope, covering
only a subset of cultural items. CANDLE groups
cultural common sense knowledge as a facet and
concept. Each facet contains multiple concepts
that are culturally relevant to a domain and subject.
DOSA (Seth et al., 2024) builds an India-specific
cultural dataset by gamifying the process of data
collection from 19 socio-diverse geographical loca-
tions, with a total of 615 social artifacts. Despite
these foundational efforts, through an initial man-
ual inspection, we observe that cultural concepts
extracted by CANDLE are incorrectly mapped to
a facet, for example: Light, Africa, Nepal under
“Rituals” facet (Details in Appendix A).
3
DIWALI Dataset
DIWALI comprises 17 systematically curated cul-
tural facets that capture the rich diversity of India
across 36 sub-regions. The sub-regional cultural
items are defined at the level of states and union
territories of the country. Sub-sub-regional distinc-
tions are grouped under their broader sub-region to
maintain consistency. For example, cultural items
from communities such as the Bodo and Rabha
of Assam are grouped in the Assam sub-region
without further subgrouping. In total, the dataset
contains 8,817 culture specific items, with the high-
est concepts from the food facet (1,419), followed
by dance forms (1,105). Figure 2 shows the dis-
tribution of concepts across the 17 facets, which
collectively cover significant aspects of Indian cul-
ture.
3.1
Choice of facets
CANDLE considers only a limited set of facets
that may not fully represent Indian culture, we ex-
tend this scope by curating 17 well-known cultural
facets of India. To define these facets, we (authors)
initially discussed various cultural concepts that are
available across the sub-regions through a brain-
storming session and grouped them into common
cultural constructs: material, social practices, geo-
graphical locations & languages, and names.
3.1.1
Material Culture
Under material culture, we consider facets that have
tangible cultural items: Clothing, Textiles, Jew-
ellery, Food, and Drinks. It covers clothing choices,
regional weaving traditions, traditional ornaments,
food, and traditional drinks.
0
200 400 600 800 100012001400
Number of Concepts
Food
Dance
Festivals
Names
Jewellery
Places
Traditions
Languages
Clothing
Games
Rituals
Architectures
Drinks
Arts
Textiles
Religion
States
Facets
1419
1105
746
608
562
547
503
502
464
412
411
381
328
288
265
239
37
Figure 2: Distribution of concepts across 17 cultural
facets present in DIWALI.
3.1.2
Social Practices and Activities
Festivals, Rituals, Traditions, Dance forms, Tra-
ditional games, Religion, and Arts represent com-
mon festivals, religious customs, cultural practices,
traditional and prominent dance styles, religious
activities, and indigenous games.
3.1.3
Geographical locations and Languages
We consider States & Capitals, Places, Languages
& Dialects, and Architectural styles facets to cover
the territorial regions of India, such as states, union
territories, and common places. We also cover
languages and dialects spoken across various sub-
regions.
3.1.4
Names
People’s names constitute an essential cultural do-
main. Each sub-region in India exhibits distinctive
naming conventions shaped by traditional customs.
To capture this variation, we consider common and
culturally significant names.
3.2
Data Construction
We initially start by prompting GPT-4o using the
simple prompt (Presented in the Appendix sec-
tion J), which produced concepts sourced from

--- Page 4 ---

Wikipedia. Wikipedia provides limited coverage
of India’s cultural diversity, resulting in incom-
plete and potentially biased datasets. Moreover,
the prompt-based method for curating datasets is
limited by the scope of the knowledge learned by
the LLM.
To address these limitations, we extend our
approach by combining GPT-4o-plus with web
searches. To enhance coverage and authenticity,
we broaden our data collection scope by searching
for official cultural and tourism websites for each
sub-region7. These sources provide more authentic
and verified documentation, ensuring a compre-
hensive and representative dataset. The detailed
prompt formulated for Dance facet is provided
in the Appendix section under “Curating India-
specific CSIs.”
3.3
Quality Check
To ensure the reliability and cultural validity of the
DIWALI dataset, we conduct a two-stage verifica-
tion process. The dataset comprises 8,817 culture
specific items, each of which is manually inspected
by one of the authors.
3.3.1
Link Validation
For each CSI, we verify the validity of its source
URL. For instance, the concept Kalamkari is as-
sociated with the URL (https://en.wikipedia
.org/wiki/Kalamkari), which is a valid source.
Concepts with missing or inaccessible links are
excluded from subsequent validation.
3.3.2
Concept Validation
Each CSI is further cross-checked against at least
one additional reliable source, typically a Govern-
ment of India portal and State government por-
tals, such as a tourism website, or the Archaeologi-
cal Survey of India8. In cases where government
sources are unavailable, we rely on Wikipedia as
a secondary reference. Concepts with incorrect
descriptions are discarded.
4
Cultural Adaptation
4.1
Problem Definition
We define cultural text adaptation as the task of
transforming a text x, originally grounded in a
source cultural context Cs, into an adapted text
x′ that aligns with the target cultural context Ct.
7Here we consider sub-region as the States and the Union
territories of India.
8https://asi.nic.in/
The objective is to preserve the original semantic
intent of x while ensuring x′ is culturally relevant
and emotionally resonant for an audience with Ct.
In this work, we focus on American (source) to In-
dian (target) cultural contexts and evaluate LLMs’
ability for culturally relevant adaptations.
4.2
Evaluation Dataset
We use GSM8k (Cobbe et al., 2021) and its mul-
tilingual variant MGSM (Shi et al., 2022) as our
evaluation datasets. These benchmarks consist of
grade school-level math word problems to evalu-
ate the reasoning capabilities of LLMs. We select
these datasets for two primary reasons. First, the
educational domain is cognitively engaging and
often reflects socio-cultural values, making it well-
suited for evaluating cultural adaptation. Second,
the problems usually contain culturally grounded
entities such as names, food items, locations, and
units, which can vary in relevance across cultures.
For our experiments, we use the GSM8k (1,319
samples) and MGSM (250 samples) test sets, both
originally situated in an American cultural context.
To assess robustness beyond math word prob-
lems, we additionally evaluate on two distinct do-
mains: dialogue and story. Specifically, we sample
100 instances from DailyDialog (Li et al., 2017)
and 100 instances from ROCStories (Mostafazadeh
et al., 2016).
4.3
Models
We evaluate models from three families of large lan-
guage models, with parameter sizes ranging from
1B to 9B: (a) Llama 2 7B Chat (Touvron et al.,
2023), (b) Llama 3.1 8B Instruct (Grattafiori et al.,
2024), (c) Llama 3.2 1B Instruct (Grattafiori et al.,
2024), (d) Llama 3.2 3B Instruct (Grattafiori et al.,
2024), (e) Mistral 7B Instruct (Jiang et al., 2023),
(f) Gemma 2 2B Instruct (Team et al., 2024), and
(g) Gemma 2 9B Instruct (Team et al., 2024).
To evaluate cultural text adaptation, we design
an assistant-style instruction prompt in both En-
glish and Bengali. The prompt explicitly instructs
the model to adapt a given text with respect to (i)
cultural relevance, (ii) tone and intent, and (iii) cul-
tural sensitivity. Given the sensitivity of LLMs to
system instructions and prompts, we provide clear,
structured guidelines to ensure consistent behav-
ior. For easy processing, we ensure that the adapted
text, along with replaced concepts, is in a structured
format. Full prompts are provided in the Appendix
J (Prompt title: Cultural Text Adaptation), and de-

--- Page 5 ---

tails on decoding strategies and inference setup are
given in Appendix C.
4.4
Evaluation Metrics
4.4.1
CSI Adaptation Score
To quantify the extent of cultural adaptation in
generated text, we introduce an Adaptation Score,
which measures the correctness of cultural concept
replacements. Given an input text with a set of re-
placed cultural concepts: R = {w1, w2, . . . , wN},
the score is defined as the proportion of replace-
ments that match a pre-specified set of target cul-
tural concepts. Formally, for each replaced concept
w ∈R, we define an indicator function I(w) as:
I(w) =
(
1,
if w is successfully matched,
0,
otherwise,
We follow two matching strategies:
1. Exact Match: We first normalize the concept
w (For example, by lowercasing and removing
punctuation) and check for an exact match in
the target cultural concept set C. That is, if
normalize(w) ∈C, then I(w) = 1.
2. Fuzzy Match: If an exact match is not found,
we perform fuzzy matching using a token-
based similarity measure9.
Let c∗be the
best fuzzy match from C for w such that
similarity(normalize(w), c∗) ≥τ. Here
τ is a predetermined threshold (For example,
τ = 80 in our experiments). If this condition
is met, we set I(w) = 1.
Based on the above matching strategy, the Adap-
tation Score for a adapted text is given by:
ADAPTATION SCORE = 1
N
P
w∈R I(w)
For example:
Suppose the LLM adapts three
non-Indian concepts: {Muffins, Christmas, Beer}
into { Paratha ✓, Diwali ✓, Ginseng ✗}. Assum-
ing two of these replacements are valid matches
according to our dataset (DIWALI). The adaptation
score is computed as follows: 1+1+0
3
= 2
3.
4.4.2
LLM as Judge
Motivated by recent progress in utilizing large lan-
guage models to evaluate text generations (Zheng
et al., 2023). We conduct our evaluation using
two state-of-the-art LLMs: Llama-3.1-8B-Instruct
and Mistral 7B Instruct-v0.3. Both models are em-
ployed to assess the quality of culturally adapted
9We use token_sort_ratio metric from the FuzzyWuzzy
library with default settings.
text based on a detailed prompt and scoring criteria.
In particular, we prompt LLMs to score adapted
text in three dimensions: Cultural Relevance, Lan-
guage Fluency, and Mathematical Integrity. We
follow a Likert scale of 0 (very poor) to 5 (perfect).
4.4.3
Human Evaluation
For human evaluation, we randomly sample 50
adapted generations for each of 7 models, total-
ing 350 instances. Unlike LLM-based automatic
evaluation, performing human evaluation captures
subjective cultural nuances that LLMs may over-
look. We assess the cultural adaptation of various
models along Cultural Relevance dimension, de-
fined in Table 14 under Appendix E. Each anno-
tator is asked to rate the cultural relevance on a
6-point Likert scale (0 = very poor, 5 = perfect)
while assuming “Country: India” as a culture
proxy. To ensure consistency, we provide anno-
tators with predefined score descriptions as evalu-
ation instructions (Details mentioned in 16 under
Appendix F). We consider five annotators from
diverse socio-demographic backgrounds, specifi-
cally from Chhattisgarh, West Bengal, Maharashtra,
Delhi, and Kerala in India. All evaluators are na-
tive Indian residents with 20+ years of residency in
their respective sub-regions. The educational quali-
fication and demographic details of the evaluators
are presented under Appendix G in Table 17. Due
to constraints, we perform human evaluation only
for adaptation with an English prompt on GSM8k
set.
5
Results and Discussions
This section describes results and presents discus-
sions for the considered LLMs on CSIs based on
average adaptation score, LLM as Judge, and Hu-
man Evaluation.
5.1
Existing vs. DIWALI: Average Adaptation
Scores
Table 1 presents a detailed comparison of the aver-
age adaptation score (AAS) obtained using three
different sets of ground-truth Culture Specific Items
(CSIs): CANDLE, DOSA, and DIWALI for both
fuzzy and exact matching strategies10.
To pre-
pare CSIs11 for use with Bengali prompts, we per-
10Fuzzy match is computed only after removing exact
matches, so it may be lower or higher than an exact match.
11Apart from DIWALI, we also translate CSIs of CANDLE
and DOSA for MGSM comparison.

--- Page 6 ---

Dataset: GSM
Prompt: English
Prompt: Bengali
AAS (CANDLE)
AAS (DOSA)
AAS (DIWALI)
AAS (CANDLE)
AAS (DOSA)
AAS (DIWALI)
Model
Fuzzy Match
Exact Match
Fuzzy Match
Exact Match
Fuzzy Match
Exact Match
Fuzzy Match
Exact Match
Fuzzy Match
Exact Match
Fuzzy Match
Exact Match
Llama-2-7b-chat-hf
0.050
0.028
0.053
0.005
0.615
0.855
0.000
0.000
0.000
0.000
0.000
0.000
Llama-3.1-8B-Instruct
0.040
0.040
0.048
0.007
0.400
0.605
0.175
0.087
0.084
0.018
0.403
0.131
Llama-3.2-1B-Instruct
0.083
0.058
0.052
0.006
0.489
0.933
0.000
0.000
0.000
0.000
0.000
0.000
Llama-3.2-3B-Instruct
0.051
0.028
0.037
0.006
0.253
0.672
0.210
0.068
0.049
0.044
0.337
0.195
Mistral-7B-Instruct-v0.3
0.106
0.056
0.087
0.005
0.445
0.563
0.286
0.143
0.070
0.014
0.531
0.102
Gemma-2-2B-Instruct
0.067
0.049
0.551
0.007
0.393
0.635
0.248
0.155
0.075
0.008
0.456
0.075
Gemma-2-9B-Instruct
0.060
0.039
0.202
0.009
0.642
0.479
0.114
0.084
0.117
0.007
0.365
0.127
Dataset: MGSM
Prompt: English
Prompt: Bengali
AAS (CANDLE)
AAS (DOSA)
AAS (DIWALI)
AAS (CANDLE)
AAS (DOSA)
AAS (DIWALI)
Model
Fuzzy Match
Exact Match
Fuzzy Match
Exact Match
Fuzzy Match
Exact Match
Fuzzy Match
Exact Match
Fuzzy Match
Exact Match
Fuzzy Match
Exact Match
Llama-2-7b-chat-hf
0.000
0.000
0.000
0.000
1.000
1.000
0.051
0.122
0.041
0.265
0.153
0.612
Llama-3.1-8B-Instruct
0.040
0.016
0.045
0.000
0.160
0.494
0.115
0.038
0.019
0.020
0.231
0.230
Llama-3.2-1B-Instruct
0.016
0.040
0.032
0.000
0.200
0.488
0.000
0.000
0.000
0.000
0.000
0.000
Llama-3.2-3B-Instruct
0.124
0.077
0.062
0.000
0.316
0.285
0.094
0.073
0.031
0.005
0.204
0.058
Mistral-7B-Instruct-v0.3
0.065
0.024
0.024
0.008
0.192
0.608
0.254
0.217
0.119
0.004
0.430
0.094
Gemma-2-2B-Instruct
0.052
0.013
0.013
0.000
0.169
0.416
0.118
0.118
0.024
0.019
0.222
0.033
Gemma-2-9B-Instruct
0.088
0.036
0.324
0.000
0.428
0.364
0.032
0.040
0.028
0.008
0.291
0.085
Table 1: Comparison of adaptation scores across different models. Here, AAS represents the Average Adaptation
score, and GSM represents the GSM8k dataset.
CANDLE
DOSA
DIWALI
Model
E
F
E
F
E
F
Llama-2-7B-chat-hf
0.157
0.326
0.044
0.258
0.842
0.573
Llama-3.1-8B-Instruct
0.104
0.021
0.000
0.083
0.416
0.416
Llama-3.2-1B-Instruct
0.169
0.868
0.000
0.358
0.547
0.547
Llama-3.2-3B-Instruct
0.107
0.071
0.048
0.059
0.345
0.535
Mistral-7B-Instruct
0.057
0.057
0.014
0.028
0.171
0.486
Gemma-2-2B-Instruct
0.078
0.098
0.039
0.078
0.098
0.313
Gemma-2-9B-Instruct
0.166
0.083
0.000
0.166
0.333
0.437
Table 2: Average Adaptation scores reported on Daily-
Dialog. Here, E and F represent Exact and Fuzzy match,
respectively.
CANDLE
DOSA
DIWALI
Model
E
F
E
F
E
F
Llama-2-7B-chat-hf
0.020
0.020
0.000
0.020
0.969
0.061
Llama-3.1-8B-Instruct
0.067
0.067
0.000
0.067
0.467
0.233
Llama-3.2-1B-Instruct
0.304
0.130
0.000
0.174
0.826
0.652
Llama-3.2-3B-Instruct
0.055
0.109
0.000
0.055
0.472
0.472
Mistral-7B-Instruct
0.100
0.086
0.014
0.071
0.371
0.600
Gemma-2-2B-Instruct
0.000
0.037
0.000
0.074
0.667
0.296
Gemma-2-9B-Instruct
0.088
0.022
0.022
0.444
0.556
0.511
Table 3: Average Adaptation scores on ROCStories.
Here, E and F represent Exact and Fuzzy match, respec-
tively.
form zero-shot translation12 from English to Ben-
gali. Specifically, for each CSI from DIWALI we
prompt: “Translate this {concept} into Bengali
without providing additional context or domain
knowledge.” The translated CSIs were then manu-
ally verified by one of the native authors13.
For the GSM with an English prompt, DIWALI
significantly outperforms CANDLE. For instance,
the Llama-2-7b-chat-hf model achieves a fuzzy
match score of 0.615 and an exact match score
of 0.855 with our dataset, compared to very low
scores of 0.050 and 0.028, respectively, with CAN-
DLE. This performance gap is consistently ob-
served across models, indicating that DIWALI is
more sensitive in capturing their adaptation capa-
bilities.
12We used OpenAI’s GPT-o3 for translation
13Belonging to West Bengal state of India
For
the
GSM
with
a
Bengali
prompt,
the differences between the two CANDLE
and DIWALI remain evident.
While some
models,
such
as
Llama-2-7b-chat-hf
and
Llama-3.2-1B-Instruct,
score
near
zero
for
both
fuzzy
and
exact
match,
while
others
show
clear
gains.
For
instance,
Llama-3.1-8B-Instruct achieves a fuzzy match
score of 0.175 and an exact match score of 0.087 us-
ing CANDLE, while DIWALI yields higher scores
of 0.403 and 0.131, respectively. Similar observa-
tions are made for Mistral-7B-Instruct-v0.3
and Gemma-2-9B-Instruct.
On MGSM, DIWALI scores much higher than
CANDLE or DOSA, especially with the English
prompt. For example, Llama-3.1-8B-Instruct
exact match scores 0.494 with DIWALI but ≤
0.016 with CANDLE and DOSA. We observe a
similar trend for the Bengali prompt. For instance,
DIWALI scores Llama-2-7B-chat-hf 0.612 for
exact match versus 0.122 and 0.265 for CANDLE
and DOSA, respectively. Small parameter model,
Llama-3.2-1B-Instruct stays near zero across
all methods.
Additional domains:
On DailyDialog, all
models achieve substantially higher AAS with
DIWALI than with CANDLE or DOSA, where
scores are near–zero for many models.
No-
tably, Llama-2-7B-chat-hf leads with a high
AAS, achieving scores of 0.842 and 0.573 in
exact and fuzzy match. Similarly, on ROCSto-
ries, we observe the same trend.
For instance,
Llama-2-7B-chat-hf achieves a score of 0.969
with DIWALI, as compared to 0.020 for CANDLE.
The comprehensive AAS results for both dialogue
and story-based adaptation are reported in Table 2
and 3, respectively.

--- Page 7 ---

5.2
LLM as Judge Results
Table 4a reports the average Likert scores
assigned
by
two
LLM
judges:
Llama
(Llama-3.1-8B-Instruct) and Mistral (Mistral
7B
Instruct-v0.3), for Cultural Relevance
(CR), Language Fluency (LF), and Mathematical
Integrity (MI). The prompt used for LLM as Judge
is presented in the Appendix under Section J
under the prompt title “LLM as Judge.” Overall,
the scores indicate that the evaluated models
perform consistently well across these dimen-
sions. For example, Gemma-2-9B-Instruct and
Mistral-7B-Instruct-v0.3 achieve high scores
consistently for both LLM judges.
5.3
Human Evaluation Results
Table 4b presents the average Cultural Rele-
vance scores as rated by five human evalua-
tors for each model on a 6-point Likert scale.
Llama-3.1-8B-Instruct achieves the highest av-
erage cultural relevance score of 2.68, while
Llama-3.2-1B-Instruct has the lowest average
score of 0.75. We observe that LLM as a Judge as-
signs higher cultural relevance scores than human
evaluators. Suggesting that LLM as a Judge might
not be an appropriate method for evaluation of the
cultural text adaptation task (Details are presented
in Appendix H).
Inter-annotator agreement:
To ensure consis-
tency among annotators and the reliability of the
scores. We measure the inter-annotator reliability
using Cohen’s κ (Landis and Koch, 1977) on the
pair of human raters for each model. As shown in
Table 5, there is acceptable agreement for models
under the Llama and Gemma families. At the same
time, evaluation scores for Mistral-7B-Instruct
have low inter-annotator agreement.
6
Analyses
In this section, we perform a detailed analysis to
understand the sub-regional coverage and shallow
cultural adaptation of cultural concepts across 17
cultural facets.
Sub-regional coverage: Despite their strong in-
context capabilities and training on a large corpus,
LLMs lack pluralistic (Sorensen et al., 2024) align-
ment. This leads to the propagation of cultural
ideas and views from their training data, causing
a dominating effect while underrepresenting other
cultures. To investigate this, we pose the following
question: “Do LLMs, when prompted with the task
of regional-level text adaptation, fairly represent
all the sub-regional concepts?” To analyze this,
we map each replaced concept with a sub-region
(State or Union Territory) and plot a geographical
heatmap for each facet. The heatmap for the food
facet is shown in Figure 3, which reveals a signifi-
cant bias in how concepts are adapted to represent
a sub-region. In particular, food-related concepts
adapted by Gemma-2-2B-Instruct primarily orig-
inate from Uttar Pradesh, Madhya Pradesh, Maha-
rashtra, and Punjab, with a complete absence of
adaptations from the Northeastern states. Similar
sub-regional skews are observed for the rest of the
facets. The heatmaps for the remaining 16 facets
are presented in Appendix I.
Surface vs. Deep level: Effective cultural adapta-
tion must be faithful to the source text while emo-
tionally resonating with the target audience by in-
corporating deep cultural nuances. (Hershcovich
et al., 2022) define culture along three axes: About-
ness, Objectives & Values, and Common ground.
In particular, Aboutness refers to the contextual
relevance of concepts across cultures. For instance,
the discussion of “cricket match” might be less
meaningful in cultures where cricket is less preva-
lent. Deeper adaptation connects culturally relevant
events and scenarios. Therefore, cultural adapta-
tion requires adapting from one culture to another
by connecting relevant events and scenarios. For
example, in the festival of “Durga puja” (event),
people from Bengal might relate more to “pandal
hopping” (scenario), thus impacting the aboutness
of the text in context with culture. Such adapta-
tions are at a deeper level and are more emotionally
relatable.
To understand the adaptation level – surface
or deep: “We hypothesize that LLMs struggle
with a deeper level of cultural adaptation,
particularly in connecting events to meaningful
scenarios.”
To test this, we manually analyse
model generations and found that LLMs often
fail to connect events and scenarios together, thus
leading to failure to establish “aboutness.”
In
Table 6, we show the detailed analysis of the
adapted
text
for
Llama-3.1-8B-Instruct,
Mistral-7B-Instruct-v0.1,
and
Gemma-2-7B-Instruct.
In
particular,
we
observe
Llama-3.1-8B-Instruct
adapts
the
event Tuesday →Diwali (festival).
However,
the associated scenario, i.e., sells CDs, remains
unchanged. The scenario of selling CDs lacks any
meaningful or emotionally resonating connection

--- Page 8 ---

Model
Llama
Mistral
CR
LF
MI
CR
LF
MI
Llama-2-7b-chat-hf
3.070 3.194 4.468
3.291 3.310 4.467
Llama-3.1-8B-Instruct
3.182 3.390 4.579
3.246 3.289 4.529
Llama-3.2-1B-Instruct
2.707 2.844 4.136
3.207 3.422 4.576
Llama-3.2-3B-Instruct
3.150 3.314 4.624
3.204 3.323 4.483
Mistral-7B-Instruct
3.561 3.780 4.680
3.351 3.357 4.528
Gemma-2-2B-Instruct
3.398 3.626 4.626
3.167 3.256 4.398
Gemma-2-9B-Instruct
3.236 3.405 4.689
3.270 3.340 4.501
(a) LLM-as-Judge scores. Here, CR represents Cultural
Relevance, LF represents Language Fluency, and MI repre-
sents Mathematical Integrity.
Model
A
B
C
D
E
Avg.
Llama-2-7b-chat-hf
2.02
2.18
2.72
2.58
2.12
2.32
Llama-3.1-8B-Instruct
2.42
2.46
3.10
2.90
2.50
2.68
Llama-3.2-1B-Instruct
0.46
0.72
1.26
0.46
0.84
0.75
Llama-3.2-3B-Instruct
1.76
2.08
1.26
2.48
2.08
1.93
Mistral-7B-Instruct
1.86
1.98
2.86
2.68
1.84
2.24
Gemma-2-2B-Instruct
1.90
1.82
2.24
2.18
1.76
1.98
Gemma-2-9B-Instruct
2.38
2.34
2.68
2.82
2.42
2.53
(b) Human evaluation scores (Culture Relevance). Here A–E are
human evaluators from diverse socio-demographic sub-regions
of India.
Table 4: Evaluation scores of LLM-as-Judge and Human evaluation for cultural text adaptation.
Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
Figure 3: Comparison of heatmaps for Food facet across different subregions.
Model
IAA
Llama-2-7B-chat-hf
0.451
Llama-3.1-8B-Instruct
0.354
Llama-3.2-1B-Instruct
0.213
Llama-3.2-3B-Instruct
0.415
Mistral-7B-Instruct
0.230
Gemma-2-2B-Instruct
0.589
Gemma-2-9B-Instruct
0.443
Table 5: Inter-annotator agreement (Cohen’s κ) on Cul-
tural Relevance (CR).
to the festival of Diwali. This demonstrates that
current LLMs often perform surface-level concept
replacement but fail to make deeper adaptations
necessary for cultural resonance.
7
Related Work
In this section, we describe the various works re-
lated to building specific cultural artifacts with a
focus on Indian culture. CANDLE (Nguyen et al.,
2023) develops a large CSI collection by extract-
ing cultural commonsense knowledge from web-
scale corpora using an end-to-end method. It iden-
tifies candidate sentences using techniques such
as string matching, named entity recognition, and
a set of handcrafted lexico-syntactic rules. These
candidates are then classified into cultural facets –
such as geography, religion, or occupation – using
zero-shot classification methods based on natural
language inference. Finally, CANDLE clusters
sentences containing similar facts using sentence
embeddings and hierarchical agglomerative cluster-
ing, allowing it to produce coherent, representative
summaries for each cluster. While this approach
achieves broad coverage, its application to India
is limited, consisting of only 650 concepts, and
these entries focus on five facets: clothing, drinks,
cuisines, rituals, and traditions.
In contrast, DOSA (Seth et al., 2024) adopts a
participatory research methodology by engaging
260 participants across 19 Indian states to compile
a dataset of 615 artifacts. This method captures a
broader range of cultural dimensions, including re-
gional rituals, local customs, and specific art forms,

--- Page 9 ---

Model
Adapted Text
Observation
Llama-3.1-8B-Instruct
Rohan sells CDs. He has 8 customers on Diwali. His first 3 customers buy one CD each. His next 2
customers buy 2 CDs each. His last 3 customers don’t buy any CDs. How many CDs did Rohan sell on
Diwali?
✓proper noun
✓event
✗scenario
✗aboutness
Mistral-7B-Instruct
Ram sells DVDs. He has 8 customers on Tuesdays (Til-lakshadhi). His first 3 customers buy one DVD each.
His next 2 customers buy 2 DVDs each. His last 3 customers don’t buy any DVDs. How many DVDs did
Ram sell on Tuesdays (Til-lakshadhi)?
✓proper noun
✓event
✗scenario
✗aboutness
Gemma-2-9B-Instruct
Babu sells DVDs. He has 8 customers on Tuesday. His first 3 customers buy one DVD each. His next 2
customers buy 2 DVDs each. His last 3 customers don’t buy any DVDs. How many DVDs did Babu sell on
Tuesday?
✓proper noun
✗event
✗scenario
✗aboutness
Llama-3.1-8b-Instruct
Rohan and Aaradhya are having a contest to see who can eat the most fruit jam-filled parathas, so they unroll
as many as they can find. Unfortunately, someone makes a mistake and Aaradhya’s was two parathas wide
and 24 parathas long while Rohan’s was 3 parathas wide and 14 parathas long. If they both ate their entire
amount, how many did they eat on average?
✓proper noun
✓event
✗scenario
✗aboutness
Mistral-7B-Instruct
Ramesh and Meera are participating in a competition to determine who can consume the most jalebis, so
they unroll as many as they can find. Unfortunately, an error occurs, and Meera’s jalebi stack is twice as
wide and 24 stacks high, while Ramesh’s is 3 stacks wide and 14 stacks high. If they both consume their
entire amount, how many did they eat on average?
✓proper noun
✓event
✗scenario
✗aboutness
Gemma-2-9B-Instruct
Anika and Rohan are having a contest to see who can eat the most laddoos, so they unwrap as many as they
can find. Unfortunately, someone makes a mistake and Anika’s was two laddoos wide and 24 laddoos long
while Rohan’s was 3 laddoos wide and 14 laddoos long. If they both ate their entire amount, how many did
they eat on average?
✓proper noun
✓event
✗scenario
✗aboutness
Table 6: Surface level adaptation shown for original text: (1) Billy sells DVDs. He has 8 customers on Tuesday. His
first 3 customers buy one DVD each. His next 2 customers buy 2 DVDs each. His last 3 customers don’t buy any
DVDs. How many DVDs did Billy sell on Tuesday? (2) Marcell and Beatrice are having a contest to see who can
eat the most fruit roll-ups, so they unroll as many as they can find. Unfortunately, someone makes a mistake and
Beatrice’s was two roll-ups wide and 24 rolls up long while Marcell’s was 3 roll-ups wide and 14 roll-ups long. If
they both ate their entire amount, how many did they eat on average?
providing richer insights into India’s sub-regional
diversity. However, while providing depth, such
participatory methods are difficult to scale. Our
work addresses these gaps by constructing a com-
prehensive resource of cultural specific items, cov-
ering 17 facets across 36 sub-regions of India.
8
Usage of CSIs
Culture specific items (CSIs) are part of cultural
knowledge bases and can potentially help elicit cul-
tural knowledge in various applications, such as
(a) cultural competence evaluation: existing meth-
ods on cultural competence evaluations of LLMs
like Culture Bias Score (Naous et al., 2024) and
Edit level analysis (Singh et al., 2024) rely on CSIs
to measure the cultural biases of LLMs. Thus,
having a large-scale, sub-regional CSIs for India
would enable a more robust and nuanced evaluation
of model competence across various downstream
tasks, (b) cross-culture translation: while most
machine translation systems are “culture agnostic,”
recent work (Conia et al., 2024; Yao et al., 2024;
Zhang et al., 2024) has focused on culturally-aware
translation. Having comprehensive CSI collection
is essential for this task, as it allows models to
identify and appropriately translate culture-specific
entities for better cross-cultural translation, and (c)
cultural adaptation: recent explorations in open
text generation, such as writing a story (Bhatt and
Diaz, 2024) and dialog-based (Singh et al., 2024),
have highlighted the need for cultural adaptation.
CSIs can enable a better and holistic adaptation.
9
Conclusion
In this paper, we introduce DIWALI, a novel Cul-
tural Specific Items (CSIs) dataset for Indian cul-
ture covering 36 subregions of India. The dataset
is composed of carefully selected facets and man-
ually verified, and contains a total of 8,817 con-
cepts across 17 facets. Leveraging our dataset’s
improved cultural coverage over existing resources,
we evaluate LLMs on the task of cultural text adap-
tation. We show the coverage of DIWALI by per-
forming cultural adaptation for different domains
such as education, daily conversations, and stories.
Our human evaluation results on cultural text sug-
gest that LLMs fail to perform this task adequately.
Furthermore, our human evaluation analysis of sur-
face adaptation demonstrates that LLMs mostly
perform shallow-level adaptations. These findings
highlight the need for future research to develop
models and training methods that can grasp the
nuanced context behind cultural concepts.

--- Page 10 ---

Limitations
In this work, we introduce a novel culture specific
item dataset, particularly belonging to Indian cul-
ture, covering the sub-regional level granularity.
However, our study has certain limitations. First,
our evaluations are restricted to widely used large
language models that are trained on multilingual
and diverse global datasets, rather than models that
are specifically pre-trained or finetuned on country-
specific linguistic and cultural contexts. We intend
to expand our study to country-specific LLMs. Sec-
ond, our analysis on the surface or deeper level of
generations is limited to a few examples. The study
of “aboutness” in cultural contexts necessitates
analysis by a large cultural population. Third, we
performed a human evaluation by recruiting five
annotators from five diverse socio-demographic re-
gions. However, a multifaceted concept such as
cultures requires a more diverse evaluation sourced
across all possible socio-demographic regions to
facilitate a more diverse and fair evaluation.
Acknowledgements
We express our heartfelt thanks to all human evalu-
ators for assessing the adaptations by the models.
Furthermore, we thank anonymous reviewers and
the meta-reviewer for their valuable suggestions
and feedback, which significantly improved the
quality of the paper.
Ethical Considerations
Culture-specific items are sourced from publicly
available sources, including Wikipedia, govern-
ment, and tourism websites. We do not store any
personal information in the DIWALI dataset. The
dataset is intended for academic research and cul-
tural analysis with careful consideration to avoid
misrepresentation or community-specific practices.
Furthermore, we do not collect any personal in-
formation from human evaluators. The dataset is
available on Huggingface under MIT license.
All annotators mentioned in Section 4.4.3 are
research students, all with at least a bachelor’s
or master’s degree. The annotation was done as
part of their research activity, for which they were
hired. The remuneration was covered under their
monthly research assistantship. We used gener-
ative AI (ChatGPT-o4-mini) for language editing
purposes only such as paraphrasing, spell-checking,
and refining polishing the author’s original content.
References
Muhammad Farid Adilazuarda, Sagnik Mukherjee,
Pradhyumna Lavania, Siddhant Shivdutt Singh, Al-
ham Fikri Aji, Jacki O’Neill, Ashutosh Modi, and
Monojit Choudhury. 2024. Towards measuring and
modeling “culture” in LLMs: A survey. In Proceed-
ings of the 2024 Conference on Empirical Methods in
Natural Language Processing, pages 15763–15784,
Miami, Florida, USA. Association for Computational
Linguistics.
Badr AlKhamissi,
Muhammad ElNokrashy,
Mai
Alkhamissi, and Mona Diab. 2024. Investigating
cultural alignment of large language models. In Pro-
ceedings of the 62nd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long
Papers), pages 12404–12422, Bangkok, Thailand.
Association for Computational Linguistics.
Sunil Barthwal and N. L. Gupta. 2011. Cultural val-
ues as advertisement themes in international and
indian advertising.
Indian Journal of Marketing,
42(11):16–21.
Yoav Benjamini and Yosef Hochberg. 2018. Control-
ling the false discovery rate: A practical and pow-
erful approach to multiple testing. Journal of the
Royal Statistical Society: Series B (Methodological),
57(1):289–300.
Shaily Bhatt and Fernando Diaz. 2024. Extrinsic evalua-
tion of cultural competence in large language models.
In Findings of the Association for Computational
Linguistics: EMNLP 2024, pages 16055–16074, Mi-
ami, Florida, USA. Association for Computational
Linguistics.
Jill Burstein, Jane Shore, John Sabatini, Yong-Won
Lee, and Matthew Ventura. 2007. The automated
text adaptation tool.
In Proceedings of Human
Language Technologies: The Annual Conference of
the North American Chapter of the Association for
Computational Linguistics (NAACL-HLT), pages 3–4,
Rochester, New York, USA. Association for Compu-
tational Linguistics.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, Christopher Hesse, and John Schulman.
2021. Training verifiers to solve math word prob-
lems. Preprint, arXiv:2110.14168.
Simone Conia, Daniel Lee, Min Li, Umar Farooq Min-
has, Saloni Potdar, and Yunyao Li. 2024. Towards
cross-cultural machine translation with retrieval-
augmented generation from multilingual knowledge
graphs. In EMNLP.
Rotem Dror, Gili Baumer, Segev Shlomov, and Roi
Reichart. 2018. The hitchhiker’s guide to testing sta-
tistical significance in natural language processing.
In Proceedings of the 56th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 1383–1392, Melbourne, Aus-
tralia. Association for Computational Linguistics.

--- Page 11 ---

Bradley Efron. 1979. Bootstrap methods: Another look
at the jackknife. Annals of Statistics, 7:1–26.
Hanem El-Farahaty and Rafat Y. Alwazna. 2024. Trans-
lating cultural references and sensitive elements be-
tween arabic and english: Netflix subtitles as a case
study. SAGE Open, 14(2):21582440241258293.
Ana Luisa Ferreira. 2024. Cultural adaptation in film
subtitles: A study of brazilian films for hispanic au-
diences. Journal of Linguistics and Communication
Studies, 3(4):48–53.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schel-
ten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mi-
tra, Archie Sravankumar, Artem Korenev, Arthur
Hinsvark, and 542 others. 2024. The llama 3 herd of
models. Preprint, arXiv:2407.21783.
Hamna, Deepthi Sudharsan, Agrima Seth, Ritvik Bud-
hiraja, Deepika Khullar, Vyshak Jain, Kalika Bali,
Aditya Vashistha, and Sameer Segal. 2025. Kahani:
Culturally-nuanced visual storytelling tool for non-
western cultures. In Proceedings of the 2025 ACM
SIGCAS/SIGCHI Conference on Computing and Sus-
tainable Societies, COMPASS ’25, page 379–400,
New York, NY, USA. Association for Computing
Machinery.
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
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, Lélio Renard Lavaud,
Marie-Anne Lachaux, Pierre Stock, Teven Le Scao,
Thibaut Lavril, Thomas Wang, Timothée Lacroix,
and William El Sayed. 2023. Mistral 7b. Preprint,
arXiv:2310.06825.
J. Richard Landis and Gary G. Koch. 1977. The mea-
surement of observer agreement for categorical data.
Biometrics, 33(1):159–174.
Cheng Li, Mengzhuo Chen, Jindong Wang, Sunayana
Sitaram, and Xing Xie. 2024. Culturellm: Incorpo-
rating cultural differences into large language mod-
els. In Advances in Neural Information Processing
Systems, volume 37, pages 84799–84838. Curran As-
sociates, Inc.
Huihan Li, Arnav Goel, Keyu He, and Xiang Ren. 2025.
Attributing culture-conditioned generations to pre-
training corpora. In The Thirteenth International
Conference on Learning Representations.
Xianggui Li. 2024. Cross cultural adaptation of adver-
tising in multinational enterprises - a case study of
the nike inc. Perspectives in Social Sciences and Arts,
3(1):1–39.
Yanran Li, Hui Su, Xiaoyu Shen, Wenjie Li, Ziqiang
Cao, and Shuzi Niu. 2017. DailyDialog: A manually
labelled multi-turn dialogue dataset. In Proceedings
of the Eighth International Joint Conference on Nat-
ural Language Processing (Volume 1: Long Papers),
pages 986–995, Taipei, Taiwan. Asian Federation of
Natural Language Processing.
Reem Masoud, Ziquan Liu, Martin Ferianc, Philip C.
Treleaven, and Miguel Rodrigues Rodrigues. 2025.
Cultural alignment in large language models: An
explanatory analysis based on hofstede‘s cultural di-
mensions. In Proceedings of the 31st International
Conference on Computational Linguistics, pages
8474–8503, Abu Dhabi, UAE. Association for Com-
putational Linguistics.
Nasrin Mostafazadeh, Nathanael Chambers, Xiaodong
He, Devi Parikh, Dhruv Batra, Lucy Vanderwende,
Pushmeet Kohli, and James Allen. 2016. A corpus
and cloze evaluation for deeper understanding of
commonsense stories. In Proceedings of the 2016
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies, pages 839–849, San Diego,
California. Association for Computational Linguis-
tics.
Tarek Naous, Michael J Ryan, Alan Ritter, and Wei Xu.
2024. Having beer after prayer? measuring cultural
bias in large language models. In Proceedings of the
62nd Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages
16366–16393, Bangkok, Thailand. Association for
Computational Linguistics.
Tarek Naous and Wei Xu. 2025. On the origin of cul-
tural biases in language models: From pre-training
data to linguistic phenomena.
In Proceedings of
the 2025 Conference of the Nations of the Americas
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies (Volume 1:
Long Papers), pages 6423–6443, Albuquerque, New
Mexico. Association for Computational Linguistics.
Peter Newmark. 2003. A textbook of translation.
Tuan-Phong Nguyen, Simon Razniewski, Aparna Varde,
and Gerhard Weikum. 2023. Extracting cultural com-
monsense knowledge at scale. In Proceedings of
the ACM Web Conference 2023, WWW ’23, page
1907–1917, New York, NY, USA. Association for
Computing Machinery.
Tijana Radojevi´c, Nemanja Staniši´c, and Nenad Stani´c.
2024. How culture shapes the restaurant experience:

--- Page 12 ---

A study of hofstede’s dimensions and service quality.
Hotel and Tourism Management, 12(1).
Michael J Ryan, William Held, and Diyi Yang. 2024.
Unintended impacts of LLM alignment on global rep-
resentation. In Proceedings of the 62nd Annual Meet-
ing of the Association for Computational Linguis-
tics (Volume 1: Long Papers), pages 16121–16140,
Bangkok, Thailand. Association for Computational
Linguistics.
Agrima Seth, Sanchit Ahuja, Kalika Bali, and Sunayana
Sitaram. 2024. DOSA: A dataset of social artifacts
from different Indian geographical subcultures. In
Proceedings of the 2024 Joint International Con-
ference on Computational Linguistics, Language
Resources and Evaluation (LREC-COLING 2024),
pages 5323–5337, Torino, Italia. ELRA and ICCL.
Freda Shi, Mirac Suzgun, Markus Freitag, Xuezhi Wang,
Suraj Srivats, Soroush Vosoughi, Hyung Won Chung,
Yi Tay, Sebastian Ruder, Denny Zhou, Dipanjan
Das, and Jason Wei. 2022. Language models are
multilingual chain-of-thought reasoners. Preprint,
arXiv:2210.03057.
Pushpdeep Singh, Mayur Patidar, and Lovekesh Vig.
2024.
Translating across cultures: LLMs for in-
tralingual cultural adaptation.
In Proceedings of
the 28th Conference on Computational Natural Lan-
guage Learning, pages 400–418, Miami, FL, USA.
Association for Computational Linguistics.
Taylor
Sorensen,
Jared
Moore,
Jillian
Fisher,
Mitchell Gordon, Niloofar Mireshghallah, Christo-
pher Michael Rytting, Andre Ye, Liwei Jiang,
Ximing Lu, Nouha Dziri, Tim Althoff, and Yejin
Choi. 2024.
Position: a roadmap to pluralistic
alignment. In Proceedings of the 41st International
Conference
on
Machine
Learning,
ICML’24.
JMLR.org.
Gemma Team, Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupati-
raju, Léonard Hussenot, Thomas Mesnard, Bobak
Shahriari, Alexandre Ramé, Johan Ferret, Peter Liu,
Pouya Tafti, Abe Friesen, Michelle Casbon, Sabela
Ramos, Ravin Kumar, Charline Le Lan, Sammy
Jerome, and 179 others. 2024. Gemma 2: Improving
open language models at a practical size. Preprint,
arXiv:2408.00118.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton
Ferrer, Moya Chen, Guillem Cucurull, David Esiobu,
Jude Fernandes, Jeremy Fu, Wenyin Fu, and 49 oth-
ers. 2023. Llama 2: Open foundation and fine-tuned
chat models. Preprint, arXiv:2307.09288.
Wenxuan Wang, Wenxiang Jiao, Jingyuan Huang, Ruyi
Dai, Jen-tse Huang, Zhaopeng Tu, and Michael Lyu.
2024. Not all countries celebrate thanksgiving: On
the cultural dominance in large language models. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 6349–6384, Bangkok, Thailand.
Association for Computational Linguistics.
Michał Wilczewski, Anne-Marie Søderberg, and Arka-
diusz Gut. 2019.
Storytelling and cultural learn-
ing—an expatriate manager’s narratives of collab-
oration challenges in a multicultural business setting.
Learning, Culture and Social Interaction, 21:362–
377.
Binwei Yao, Ming Jiang, Tara Bobinac, Diyi Yang, and
Junjie Hu. 2024. Benchmarking machine translation
with cultural awareness. In Findings of the Associ-
ation for Computational Linguistics: EMNLP 2024,
pages 13078–13096, Miami, Florida, USA. Associa-
tion for Computational Linguistics.
Zhonghe Zhang, Xiaoyu He, Vivek Iyer, and Alexandra
Birch. 2024. Cultural adaptation of menus: A fine-
grained approach. In Proceedings of the Ninth Con-
ference on Machine Translation, pages 1258–1271,
Miami, Florida, USA. Association for Computational
Linguistics.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric Xing, and 1 others.
2023. Judging llm-as-a-judge with mt-bench and
chatbot arena. Advances in Neural Information Pro-
cessing Systems, 36:46595–46623.

--- Page 13 ---

Appendix
A
CANDLE False Positives
Cultural concepts extracted by CANDLE are limited and contain false positives for Indian culture. To filter
such false positives, we further utilize a prompt-based method to check for cultural relevance with respect
to the facets in CANDLE. We design a simple prompt template shown in Prompt - “CSIs Relevancy.”
For example: Is rishikesh a cultural ritual concept of India? Answer in Yes or No. Each filtration is then
manually inspected by one of the authors. We remove a total of 393 concepts. The detailed statistics of
the concepts removed and kept are shown in Table 7.
Facet
Total
Removed
Kept
Sample removed concepts
Clothing
205
107
98
Western, Pakistan, Seersucker, Bohemian, Kimono, Japanese Fireman, Chinese
Dragon Robe, Poncho
Drink
157
117
40
China, Gewurztraminer, Japan, Thailand, Pakistan, Sri Lanka, Bangladesh, Eng-
land, Arabica, Robusta, Ginseng, Espresso
Food
176
78
98
Chinese, Continental, Italian, Southeast, American British, Arabica, Robusta,
Gewurztraminer, Pakistan, Philippines, Burmese, Mauritius, Chinese Food, Sri
Lankan, Thai, Singapore, Malay, Pakistani, Nepalese
Rituals
183
50
133
Light, Africa, Nepal
Traditions
191
41
150
American, British, Christmas, Africa, Nepal, Jew, Buddhism
Table 7: False positive cultural concepts from CANDLE framework (Domain = Country, Subject = India)
.
B
DIWALI Details
The facets per sub-region distributions are listed in Table 8. DIWALI contains facet, concept, description,
subregion, and source link. Some of the samples from DIWALI are depicted in Table 9. Table 10 lists out
the facets considered and their description, along with examples.
Sub-region
Textiles
Dance
Places
Festivals
Food
Games
States
Traditions
Languages
Arts
Jewellery
Religion
Rituals
Clothing
Architectures
Drinks
Names
AN
3
20
15
31
30
4
1
10
20
6
5
7
9
6
10
6
8
AP
8
43
20
37
37
20
1
31
15
10
12
6
10
28
15
10
36
AR
10
20
24
20
20
10
1
15
24
8
20
9
10
58
10
8
11
AS
10
80
15
67
42
20
1
17
15
8
13
7
14
19
19
9
16
BH
7
30
15
65
35
10
1
14
10
8
15
6
19
20
10
7
10
CH
5
13
10
10
50
2
1
2
8
5
10
7
10
10
10
7
10
CT
5
40
15
29
31
12
1
6
15
8
30
9
19
33
6
6
17
DNH
1
13
15
16
27
0
1
7
9
6
4
6
10
9
10
11
8
DL
5
15
10
15
42
10
1
15
7
5
25
8
10
8
10
10
20
GA
4
30
15
84
44
10
1
30
10
11
14
6
14
17
15
11
13
GJ
8
38
15
20
36
11
1
15
12
10
20
9
10
16
13
10
19
HR
7
19
13
24
41
20
1
13
13
9
16
7
10
10
10
10
10
HP
10
43
20
20
31
20
1
8
13
7
20
6
10
15
10
7
7
JK
10
27
27
10
40
11
2
5
10
10
11
6
10
10
10
9
20
JH
7
30
19
23
40
10
1
6
12
9
25
6
10
10
10
5
14
KA
8
41
20
16
39
15
1
13
19
10
15
7
16
11
10
10
25
KL
10
46
15
10
46
12
1
20
37
10
17
8
20
10
20
10
28
LA
5
17
10
12
45
5
1
12
8
4
10
6
10
10
10
6
15
LD
3
13
10
6
38
0
1
5
4
7
10
6
10
5
5
6
13
MP
8
34
15
10
34
11
1
9
10
10
10
7
10
8
10
10
18
MH
10
27
15
9
45
20
1
10
17
10
20
8
12
10
10
10
27
MN
8
24
19
31
47
10
1
10
15
7
9
5
14
10
10
10
46
ML
8
27
10
25
30
8
1
12
13
10
13
6
10
10
8
10
14
MZ
7
12
15
19
37
10
1
20
15
5
5
7
10
9
10
7
10
NL
7
24
10
10
30
9
1
20
20
7
10
7
10
8
10
5
16
OD
8
28
15
60
47
20
1
20
29
10
11
7
10
10
10
10
17
PY
4
5
10
10
37
8
1
10
7
5
10
6
10
5
10
5
19
PB
9
45
15
10
50
20
1
10
10
9
28
6
10
10
10
10
29
RJ
8
38
20
10
41
10
1
12
15
10
13
6
10
10
10
20
12
SK
3
22
10
8
40
5
1
10
12
10
29
7
10
10
10
6
15
TN
18
49
20
12
86
20
1
15
21
6
19
6
15
8
10
10
12
TG
9
45
10
11
36
10
1
8
7
10
40
6
10
8
10
10
16
TR
7
20
15
11
36
15
1
10
10
6
7
4
9
16
10
12
10
UP
6
43
15
47
43
10
1
48
10
7
10
6
10
10
10
12
27
UK
9
38
20
10
36
10
1
20
15
5
19
6
10
8
10
13
10
WB
10
46
10
65
30
14
1
15
15
10
17
7
10
9
10
10
10
Table 8: Distribution of 17 cultural facets (columns) across 36 States/UTs (rows), using abbreviations: AN =
Andaman and Nicobar Islands, AP = Andhra Pradesh, AR = Arunachal Pradesh, AS = Assam, BH = Bihar, CH =
Chandigarh, CT = Chhattisgarh, DNH = Dadra and Nagar Haveli and Daman and Diu, DL = Delhi, GA = Goa, GJ =
Gujarat, HR = Haryana, HP = Himachal Pradesh, JK = Jammu and Kashmir, JH = Jharkhand, KA = Karnataka, KL
= Kerala, LA = Ladakh, LD = Lakshadweep, MP = Madhya Pradesh, MH = Maharashtra, MN = Manipur, ML =
Meghalaya, MZ = Mizoram, NL = Nagaland, OD = Odisha, PY = Puducherry, PB = Punjab, RJ = Rajasthan, SK =
Sikkim, TN = Tamil Nadu, TG = Telangana, TR = Tripura, UP = Uttar Pradesh, UK = Uttarakhand, WB = West
Bengal.

--- Page 14 ---

Facet
Concept
Description
Subregion
Source link
Clothing
Kupaan
Simple cotton wrap worn by Nyishi men,
often with bamboo hats.
Arunachal Pradesh
https://www.indiatravel.
app/traditional-dress-o
f-arunachal-pradesh/
Drinks
Apong
Rice beer brewed by the Mising tribe.
Assam
https://diversityassam.c
om/culture/apong-a-tradi
tional-rice-beer-of-ass
am/
Cuisine
Pulihora
Tamarind rice with spices, often pre-
pared during festivals and special occa-
sions.
Andhra Pradesh
https://www.deccanchroni
cle.com/lifestyle/food-a
nd-recipes/270323/famous
-food-of-andhra-pradesh.h
tml
Rituals
Saptapadi
Bengali wedding ritual where couple
takes seven steps on betel leaves.
West Bengal
https://sombitdeyphotogr
aphy.com/blog/bengali-mar
riage-rituals
Traditions
Zoti
Traditional practice of offering cucum-
bers during monsoon.
Goa
https://aratigoa.wordpre
ss.com/2024/06/20/unders
tanding-goas-ecology-thr
ough-rituals-and-festiva
ls/
States and Capitals
Bengaluru
India’s tech hub blending cosmopolitan
vibe with Dravidian roots.
Karnataka
https://en.wikipedia.org
/wiki/Bangalore
Dance Forms
Jhumair
Folk dance during harvest season, preva-
lent in North and Western Odisha.
Odisha
https://en.wikipedia.org
/wiki/Folk_dance_forms_o
f_Odisha
Places
Ross Island
Former British administrative headquar-
ters with ruins.
Andaman and Nicobar Islands
https://en.wikipedia.org
/wiki/Ross_Island_(Andama
n)
Festivals
Losar
Tibetan New Year celebrated in Lahaul
and Spiti with traditional rituals.
Himachal Pradesh
https://www.holidify.com
/collections/festivals-i
n-himachal-pradesh
Religion
Bon
Ancient animistic faith influencing local
traditions.
Ladakh
https://www.lehladakhtou
rism.com/about-ladakh/la
dakh-religion.html
Languages and Dialects
Maram
Maram is a Sino-Tibetan language spo-
ken by the Maram Naga tribe in the
Senapati district. The language is inte-
gral to the tribe’s cultural identity, with
rich oral traditions and customary prac-
tices.
Manipur
https://en.wikipedia.org
/wiki/Maram_language
Arts
Tikuli Art
Tikuli is a traditional art form from Bi-
har that involves the creation of intricate
designs on glass, adorned with gold and
silver foils. Historically, it was used to
make bindis (forehead decorations) for
women. Today, Tikuli art has evolved to
include decorative items and paintings,
reflecting the rich cultural heritage of the
region.
Bihar
https://www.memeraki.com
/blogs/posts/the-beautif
ul-arts-of-bihar-manjush
a-tikuli-madhubani
Architectures
Hawa Mahal
Situated in Jaipur, the Hawa Mahal, or
’Palace of Winds,’ was built in 1799 by
Maharaja Sawai Pratap Singh. This five-
story structure features 953 small win-
dows, called jharokhas, designed to al-
low royal ladies to observe street festivi-
ties without being seen.
Rajasthan
https://en.wikipedia.org
/wiki/Hawa_Mahal
Traditionals Games
Phan Sohlaimung
Players stand at a specific distance with
a mark between them. Holding a bam-
boo pole under their right armpits, they
grasp it firmly and try to push each other
over the mark.
Tripura
https://en.wikipedia.org
/wiki/Tripuri_games_and_
sports
Textiles
Himroo Fabric
Himroo is a traditional fabric from Au-
rangabad, blending silk and cotton to
create a luxurious texture. The weaving
technique produces intricate patterns, of-
ten inspired by Persian designs, reflect-
ing the region’s historical connections.
Maharashtra
https://textilevaluechai
n.in/in-depth-analysis/ar
ticles/traditional-texti
les/traditional-textile
s-of-maharashtra
Jewellery
Vaddanam
Gold waist belt; heavy ornament; worn
during weddings and festivals.
Telangana
https://sribhavanijewels
.home.blog/2020/07/02/te
langana-traditional-jewel
lery/
Names
Devya
Means God’s gift.
Jammu and Kashmir
https://www.behindthenam
e.com/submit/names/usage
/dogri
Table 9: Samples from DIWALI dataset
C
Decoding Strategies and Inference Setup
Decoding Settings: For all experiments, we set the sampling temperature to 0. This is used to ensure
deterministic output generation, which is crucial for reproducibility and consistent evaluation. Moreover,
by not specifying any top-p (nucleus sampling) or top-k parameters, we disable stochastic sampling
methods in favour of greedy decoding. This further guarantees that the outputs are stable across different
runs. We obtained generations using this approach in a single run for the entire dataset.
Inference Setup: Inference is configured to generate a maximum of 2048 new tokens per prompt, ensuring

--- Page 15 ---

Facet
Description
Clothing
Traditional and regional attire worn. For example, Mekhela Chador.
Drink
Beverages with cultural and historical significance, including regional specialties and traditional drinks.
For example, Darjeeling Tea.
Cuisine (Food)
Dishes and food items. For example, Dosa.
Rituals
Customs followed in religious, social, and life-cycle events. For example, Chathurthi Vrat.
Traditions
Cultural practices, values, and beliefs. For example, Gaye holud.
States & Capitals
Administrative divisions of India. For example, Gujarat.
Dance forms
Traditional and prominent dance styles. For example, Kuchipudi.
Places
Common geographical and locations. For example, Dal lake.
Festivals
Common festivals and celebrations. For example, Pongal.
Religion
Prominent Religious activities. For example, Buddhism.
Languages & Dialects
Spoken languages and dialects. For example, Konda.
Arts
Painting, Sculpture, and other creative expressions. For example, Terracotta.
Architectures
Architectural styles. For example, Kesariya Stupa.
Traditional games
Indigenous games, and recreational activities. For example, Gilli Danda.
Textiles
Regional Weaving Traditions. For example, Gamsa.
Jewellery
Traditional ornaments, and adornments. For example, Tora.
Names
Common and significant names. For example, Arjun.
Table 10: Facets considered
that the models have sufficient capacity to produce complete and coherent responses. Our experiments
were conducted on NVIDIA A100 GPUs with 40GB of memory. Depending on the specific experiment,
we used either a single GPU or multiple GPUs to accelerate inference.
D
Token Lengths and Significance Tests
D.1
Average Input/Output Lengths
Model
Avg. characters
≈tokens
Input (per sample)
3,771
942
Llama-2-7B-chat-hf
482
120
Llama-3.1-8B-Instruct
370
92
Llama-3.2-1B-Instruct
526
132
Llama-3.2-3B-Instruct
392
98
Mistral-7B-Instruct-v0.3
437
109
Gemma-2-2B-Instruct
596
149
Gemma-2-9B-Instruct
356
89
Overall mean output
451
113
Table 11: Average input and output lengths shown for GSM8k dataset on cultural text adaptation task. We also
show a rough token count using a simple rule of thumb: about 4 characters per token.
D.2
Significance Testing
For every dataset and model, we report the mean exact-match accuracy and a 95% confidence interval.
We use a non-parametric bootstrap (Efron, 1979) with 10,000 resamples. Each resample picks n examples
with replacement from the test set, we recompute the mean, and we take the 2.5–97.5 percentile range as
the 95% CI. When comparing two systems on the same items, we use a paired approximate randomisation
test (10,000 sign flips; (Dror et al., 2018)). We flip the sign of each per-item difference at random and
recompute the mean difference. The two-sided p-value is the fraction of permutations with an absolute
difference at least as large as the observed one (with the usual +1 correction). We also report the mean
gap in percentage points (pp).
How we correct for multiple comparisons.
Within each family (all model–model pairs on a given
dataset/prompt, and all DIWALI–CANDLE deltas per model on that dataset/prompt), we apply Ben-
jamini–Hochberg (BH) (Benjamini and Hochberg, 2018). We call a result significant if q < 0.05.

--- Page 16 ---

Model
Exact-match
95% CI
Llama-2-7B-chat-hf
0.0285
[0.018, 0.040]
Llama-3.1-8B-Instruct
0.0859
[0.070, 0.102]
Llama-3.2-1B-Instruct
0.0474
[0.034, 0.061]
Llama-3.2-3B-Instruct
0.0296
[0.020, 0.040]
Mistral-7B-Instruct
0.0554
[0.043, 0.069]
Gemma-2-2B-Instruct
0.0438
[0.031, 0.058]
Gemma-2-9B-Instruct
0.0401
[0.029, 0.052]
(a) CANDLE baseline scores
Model
Exact-match
95% CI
Llama-2-7B-chat-hf
0.7808
[0.754, 0.806]
Llama-3.1-8B-Instruct
0.5401
[0.511, 0.568]
Llama-3.2-1B-Instruct
0.8095
[0.784, 0.834]
Llama-3.2-3B-Instruct
0.5718
[0.543, 0.601]
Mistral-7B-Instruct
0.5047
[0.477, 0.532]
Gemma-2-2B-Instruct
0.5574
[0.524, 0.591]
Gemma-2-9B-Instruct
0.4488
[0.420, 0.478]
(b) DIWALI scores
Model
∆(DIWALI - CANDLE)
p
q
Significant?
Llama-2-7B-chat-hf
0.7523
1 × 10−4
1 × 10−4
TRUE
Llama-3.1-8B-Instruct
0.4542
1 × 10−4
1 × 10−4
TRUE
Llama-3.2-1B-Instruct
0.7621
1 × 10−4
1 × 10−4
TRUE
Llama-3.2-3B-Instruct
0.5422
1 × 10−4
1 × 10−4
TRUE
Mistral-7B-Instruct
0.4494
1 × 10−4
1 × 10−4
TRUE
Gemma-2-2B-Instruct
0.5136
1 × 10−4
1 × 10−4
TRUE
Gemma-2-9B-Instruct
0.4087
1 × 10−4
1 × 10−4
TRUE
Table 13: DIWALI vs. CANDLE improvements. ∆is the mean exact-match difference in percentage points. p from
the paired approximate-randomisation test (10k permutations). q is BH-adjusted within the DIWALI – CANDLE
family.
Takeaways:
All seven models are significantly better on DIWALI than on CANDLE. On DIWALI,
every pairwise model comparison is significant after BH correction, with the biggest gap being +0.37
pp (Llama-3.2-1B-Instruct over Gemma-2-9B-Instruct). Thus, DIWALI is more comprehensive and
also separates models more clearly.
E
Likert Scale
The description of the Likert scale for cultural relevance is listed in Table 14, and Language and Mathe-
matical fluency are listed in Table 15.
F
Instructions for Human Evaluation
In this section, we describe the detailed instructions provided to the human evaluators for annotating
cultural adaptation scores for various LLMs. The instruction set was designed after multiple brainstorming
sessions with authors and annotators all belonging to different sub-regions. Details are provided in Table
16.
G
Human Annotators
In this section, we describe the socio-demographic location of our human evaluators. Details are provided
in Table 17.
H
Human evaluation vs. LLM as Judge: Comparison on Cultural Relevance
This section compares Cultural Relevance (CR) scores from human annotators (Table 4b) against CR
scores from the two LLM judges (Table 4a). We observe that across all evaluated models, the LLM judges
consistently assign higher CR scores than human evaluators with score inflation of approximately +0.5 to
+2.5 (Details are presented in Table 18). We hypothesize that this discrepancy arises because LLM judges
tend to overvalue surface-level entity changes such as simple proper noun swaps. This finding suggests
that the LLM as a Judge method may not be reliable for evaluating the deeper nuances of cultural text
adaptation.
I
Sub-regional Adaptation Coverage
The heatmaps for various facets are shown in Figures 5, 6, 7, 9, and 10.
J
Prompts

--- Page 17 ---

Score
Rubric
Description
0
Very Poor
No adaptation at all, or only direct transliteration / literal translation with no cultural tailoring.
1
Poor
Adaptations are non-sensical or illogical, introducing absurd elements that misrepresent culture.
2
Fair
Only simple replacement of proper nouns; broader context remains unchanged.
3
Moderate
Proper nouns replaced and surrounding context altered to fit typical Indian usage.
4
Good
Multiple entities adapted, showing a coherent and deeper integration with Indian culture.
5
Perfect
Cultural references are deeply integrated and fully resonant; no further adaptation is possible.
Table 14: Descriptions for the 0–5 Likert scale used in evaluating cultural relevance.
Score
Rubric
Description (LF)
Description (MI)
0
Very Poor
Uses completely Western terminology and expressions; no Indian linguistic ele-
ments appear.
Problem is mathematically nonsensical after adaptation.
1
Poor
Minimal attempt at adaptation; Indian terms used incorrectly or out of place.
Mathematics is unsound or illogical.
2
Fair
Contains a few Indian terms, but they are often mis-used or feel forced.
Basic arithmetic is correct but poorly integrated with cultural context.
3
Moderate
Some Indian terms used correctly, though overall phrasing lacks natural flow.
Mathematically sound, but cultural context could be better aligned.
4
Good
Effectively incorporates Indian English and terminology with a smooth, natural
flow.
Well-structured problems with a clear cultural context.
5
Perfect
Seamlessly blends Indian terminology, expressions, and natural language patterns.
Mathematics is flawlessly integrated with cultural elements while re-
maining precise and clear.
Table 15: Likert-scale rubric (0–5) for evaluating Language Fluency (LF) and Mathematical Integrity (MI).
Score
Description
Original Text
Incorrect Adaptation
Original Text
Incorrect Adapta-
tion
0
No adaptation or complete transliterations/translations.
Toulouse
has
twice
as
many
sheep
as
Charleston. Charleston
has 4 times as many
sheep
as
Seattle.
How many sheep do
Toulouse,
Charleston,
and Seattle have to-
gether if Seattle has 20
sheep?
Toulouse
has
twice
as
many
sheep
as
Charleston. Charleston
has 4 times as many
sheep as Seattle. Seattle
has 20 sheep. Toulouse
has 2 × 4 × 20 sheep.
How many sheep do
Toulouse,
Charleston,
and Seattle have to-
gether?
James decides to
run 3 sprints 3 times
a week. He runs 60
meters each sprint.
How many total me-
ters does he run a
week?
Ramesh ka 3 sprints
3 times a week 60
meter par 3 baar run
karta hai. Isse kya
total meter run karta
hai?
1
Non-sensical adaptations (breaks logic or value conversion).
Darrell and Allen’s ages
are in the ratio of 7:11.
If their total age now
is 162, calculate Allen’s
age 10 years from now.
Ramesh and Rohan’s
ages are in the ratio
of 7:11.
If their total
age now is |16,200, cal-
culate Rohan’s age 10
years from now.
Dan plants 3 rose
bushes. Each rose
bush has 25 roses.
Each rose has 8
thorns. How many
thorns are there to-
tal?
Ramesh plants 3 gu-
lab jamun plants.
Each gulab jamun
plant has 25 gulab
jamuns. Each gulab
jamun has 8 thorns.
How many thorns
are there total?
2
Simple replacement of proper nouns only.
Gretchen has 110 coins.
There are 30 more gold
coins than silver coins.
How many gold coins
does Gretchen have?
Ramesh has 110 coins.
There are 30 more gold
coins than silver coins.
How many gold coins
does Ramesh have?
—
—
3
Proper nouns with minor contextual change.
Cody eats three times as
many cookies as Amir
eats.
If Amir eats
5 cookies, how many
cookies do both of them
eat together?
Rohan eats three times
as many laddoos as
Priya eats. If Priya eats
5 laddoos, how many
laddoos do both of them
eat together?
—
—
4
Multiple entities changed with deeper connection to Indian culture.
A robe takes 2 bolts of
blue fiber and half that
much white fiber. How
many bolts in total does
it take?
A traditional Indian silk
saree requires 2 bolts
of blue silk and half
as much white cotton.
How many bolts of fab-
ric in total are needed?
—
—
5
Fully culturally resonant adaptation (deemed necessary).
Harry slept 9 hours last
night. His friend James
slept only 2/3 of what
Harry slept. How many
more hours did Harry
sleep than James?
Rohan slept 9 hours last
night. His friend Vijay
slept only 2/3 of what
Rohan slept. How many
more hours did Rohan
sleep than Vijay?
—
—
Table 16: Instruction for Human evaluation
Evaluator
Location (Sub-Sub-Region/Sub-Region/Country)
YoR
Educational Qualification
A
Hoogly / West Bengal / India
22
Graduate
B
Raipur / Chhattisgarh / India
28
Post-Graduate
C
Mumbai / Maharashtra / India
25
Graduate
D
Karol Bagh / Delhi / India
24
Post-Graduate
E
Ernakulam / Kerala / India
25
Graduate
Table 17: Demographic information of human evaluators. Here, YoR represents years of residence in the sub-region.

--- Page 18 ---

Model
Human CR
Llama Judge (CR)
Mistral Judge (CR)
Avg.
Score
∆
Score
∆
Llama-2-7B-chat-hf
2.32
3.070
+0.75
3.291
+0.97
Llama-3.1-8B-Instruct
2.68
3.182
+0.50
3.246
+0.57
Llama-3.2-1B-Instruct
0.75
2.707
+1.96
3.207
+2.46
Llama-3.2-3B-Instruct
1.93
3.150
+1.22
3.204
+1.27
Mistral-7B-Instruct
2.24
3.561
+1.32
3.351
+1.11
Gemma-2-2B-Instruct
1.98
3.398
+1.42
3.167
+1.19
Gemma-2-9B-Instruct
2.53
3.236
+0.71
3.270
+0.74
Table 18: Cultural Relevance (CR): Human vs. LLM-as-Judge. ∆denotes (LLM Judge CR −Human CR). LLM
judges consistently score higher than human annotators.
Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(a) Architecture
Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(b) Arts
Figure 4: Comparison of heatmaps for Architecture and Arts.

--- Page 19 ---

Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(a) Clothing
Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(b) Dance Forms
Figure 5: Comparison of heatmaps for Clothing, and Dance Forms.

--- Page 20 ---

Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(a) Festivals
Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(b) Jewellery
Figure 6: Comparison of heatmaps for Festivals, Jewellery.

--- Page 21 ---

Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(a) Language and Dialects
Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(b) Places
Figure 7: Comparison of heatmaps for Language & Dialects, and Places.

--- Page 22 ---

Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(a) Religion
Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(b) Rituals

--- Page 23 ---

Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(a) States and Capitals
Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(b) Textiles
Figure 9: Comparison of heatmaps for States & Capitals, and Textiles.

--- Page 24 ---

Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(a) Traditional Games
Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(b) Names
Figure 10: Comparison of heatmaps for Traditional games, and Names.

--- Page 25 ---

Gemma 2 2B Instruct
Gemma 2 9B Instruct
Llama 2 7B Chat
Llama 3.1 8B Instruct
Llama 3.2 1B Instruct
Llama 3.2 3B Instruct
Mistral 7BInstruct v0.3
0.0
0.2
0.4
0.6
0.8
1.0
Adaptation Score
(a) Festivals
Figure 11: Comparison of heatmaps for Festivals
Simple Prompt
Template: Please provide a comprehensive, deduplicated list of 500 culture-specific {facet} items associated with
Indian culture. Ensure that each item is unique and pertains specifically to Indian traditions and practices. Present the
output in CSV format.
Curating India-specific CSIs
SYS INST.: Generate a detailed and comprehensive list of traditional and modern dance forms specific to State/UT,
India, covering various cultural, functional, and social contexts. Present the information in CSV format with the
following columns:
Dance Form Name: The name of the dance form.
Description: A brief description (maximum 20 words) of the dance form, highlighting its cultural, functional, or
symbolic significance.
Reference Link: A reliable source link for further reading or verification.
Ensure the list includes:
Dance forms performed in different contexts, including festivals, weddings, rituals, community gatherings, and stage
performances. Representation of dance forms for men, women, and children across diverse social, cultural, and
economic settings. Detailed coverage of both traditional folk dances and contemporary adaptations. Include dance
forms that are specific to various communities, tribes, and cultural groups within State/UT. Representative of regional
uniqueness and cultural diversity.

--- Page 26 ---

Cultural Text Adaptation
SYS INST.: You are an AI assistant tasked with adapting a text to suit a specific cultural context in a particular language
while maintaining the original meaning and intent. Your goal is to ensure the text feels natural and appropriate for the
target audience, considering cultural nuances, values, and sensitivities. When making these adaptations, follow these
key steps:
1. Cultural Relevance: Adjust any idioms, metaphors, or cultural references that may not resonate with the target
audience. Replace them with culturally appropriate alternatives.
2. Tone and Intent: Preserve the original emotional tone and message, even when making cultural adjustments.
3. Cultural Sensitivity: Be mindful of topics, words, or phrases that might be sensitive or inappropriate in the target
culture.
Specific guidelines:
• Replace foreign names with common Indian names (female for female, male for male). Use a diverse set of
names.
• Use Indian locations in place of foreign locations.
• Convert all foreign currencies to Indian Rupees (INR) using a clear symbolic or approximate rate (for example,
$1 = |83). Remove any remaining references to foreign currency (USD, etc.).
• Incorporate Indian traditions, festivals, and cultural practices only if it is contextually appropriate and does not
distort the original meaning.
• Use regional-specific terminology and expressions without changing the logical sense of the text.
• Replace foreign food items with Indian equivalents only if it makes sense. For example, “muffins” can become
“parathas,” but do not replace food items that are already commonly used in India or are essential to the text’s
logic (e.g., do not replace “eggs” if it’s about chickens laying eggs).
• Maintain original mathematical operations and numerical values. Do not show any calculations or provide
step-by-step solutions.
• Do not transliterate.
• Do not solve the problem or provide the answer.
• Do not hallucinate or introduce factual errors.
• Ensure the adapted text is coherent and flows naturally in its new cultural context.
• Provide your response as a single-line JSON array without any line breaks or extra whitespace. The response
must be valid JSON that can be parsed directly.
For the replaced_concepts dictionary:
• ONLY include terms that were actually changed to different terms (e.g., "John":"Ramesh").
• DO NOT include terms that remained the same (e.g., do not include "eggs":"eggs" if it was not changed).
• Use the |symbol directly in the values, not Unicode escape sequences.
• Include ONLY the meaningful substitutions you made (e.g., "John":"Ramesh","muffins":"parathas",
"$10":"|830").
Example of correct replaced_concepts:
• Good: {"John":"Ramesh", "muffins":"parathas", "$10":"|830"}
• Bad: {"eggs":"eggs", "John":"Ramesh", "muffins":"parathas", "$10":"\u20b9830"}
Provide only the adapted text and replaced words of the problem statement in a valid JSON format, like this example:
[{"cultural_adapted_text":"Ramesh bought 5 parathas for |830 and gave 2 to his friend. How much money did he spend
per paratha?", "replaced_concepts":{"John":"Ramesh","muffins":"parathas", "$10":"|830"}}]
USER PROMPT: Adapt the following text to Indian culture: {input text}

--- Page 27 ---

Prompt in Bengali for Cultural Text Adaptation
SYS INST.: আপনি একজন এআই সহকারী যার কাজ মূল অর্থ ও উদ্দেশ্য বজায় রেখে টেক্সটকে বাংলা ভাষা ও 
সংস্কৃৃতির সাথে খাপ খাইয়ে দেওয়া। আপনার লক্ষ্য টেক্সটটিকে বাংলাভাষী শ্রোতাদের জন্য স্বাাভাবিক ও প্রাসঙ্গিক করে 
তোলা, সাংস্কৃৃতিক সূক্ষ্মতা, মূল্যবোধ ও সংবেদনশীলতা বিবেচনা করে। নিচের ধাপগুলি অনুসরণ করুন:
১. সাংস্কৃৃতিক প্রাসঙ্গিকতা: বিদেশি প্রবাদ, রূপক বা সাংস্কৃৃতিক উল্লেখগুলিকে বাংলার সমতুল্য দিয়ে প্রতিস্থাাপন করুন
২. ভাষারীতি: সহজ, প্রমিত বাংলা ব্যবহার করুন (সাধু ভাষা) আঞ্চলিক উপভাষা ছাড়া
৩. সাংস্কৃৃতিক সংবেদনশীলতা: বাংলার সাংস্কৃৃতিক রীতিনীতি মেনে চলুন
নির্দেশাবলী:
- বিদেশি নামগুলিকে সাধারণ বাংলা নামে পরিবর্তন করুন (মহিলা/পুরুষের জন্য আলাদা)
- বিদেশি স্থাানগুলিকে বাংলার স্থাাননাম ব্যবহার করুন
- মুদ্রাাকে ভারতীয় রুপিতে (₹) রূপান্তর করুন (যেমন: $১ = ₹৮২)
- বাংলার উৎসব/প্রথা যোগ করুন যেখানে প্রাসঙ্গিক
- পশ্চিমা সংখ্যাার (123) বদলে বাংলা সংখ্যাা ব্যবহার করুন (১২৩)
- গাণিতিক অপারেশন ও সংখ্যাাসমূহ অপরিবর্তিত রাখুন
- উত্তর অবশ্যই বাংলা স্ক্রিপ্টে দিতে হবে
- সিঙ্গেল-লাইন JSON অ্যাারে ফরম্যাাটে উত্তর দিন
উদাহরণ: [{"cultural_adapted_text": "রমেশ ৫টি পরোটা কিনলেন ৮৩০ টাকায় এবং ২টি বন্ধুুকে দিলেন। প্রতি পরোটার 
দাম কত?","replaced_concepts":{"John":"রমেশ","muffins":"পরোটা","$10":"৮৩০ টাকা"}}]
USER PROMPT: নিচের টেক্সটটি বাংলা ভাষা ও সংস্কৃৃতিতে রূপান্তর করুন এবং JSON ফরম্যাাটে উত্তর দিন: {input 
text}
Figure 12: Bengali Prompt for Cultural Text Adaptation

--- Page 28 ---

LLM-as-Judge
Consider yourself as an AI expert trained to evaluate the cultural adaptation of a given text.
Original Text:
{original_text}
Adapted Text:
{adapted_text}
Target Culture: Indian
Rate each criterion on a 0–5 scale and give a concise justification for each score:
1. Cultural Relevance (0–5):
• 0 – No adaptation: retains Western concepts with no cultural shift
• 1 – Non-sensical adaptation: culturally inappropriate or absurd elements (e.g., “paratha growing on plants”)
• 2 – Simple proper-noun swap: only names changed to Indian equivalents
• 3 – Names plus limited context change: some culturally relevant objects or settings
• 4 – Deep contextual change: multiple entities adapted with clear Indian cultural grounding
• 5 – Fully resonant: authentic, natural Indian context with no further improvements possible
2. Language Fluency (0–5):
• 0 – No Indian linguistic elements
• 1 – Very poor: minimal, incorrect Indian terms
• 2 – Poor: few Indian terms, often mis-used
• 3 – Moderate: correct terms but slightly forced flow
• 4 – Good: smooth Indian English with natural terminology
• 5 – Perfect: seamless blend of Indian expressions and natural language patterns
3. Mathematical Integrity (0–5):
• 0 – Mathematically nonsensical
• 1 – Incorrect mathematics
• 2 – Basic math correct but weak cultural tie-in
• 3 – Sound math; cultural link could be clearer
• 4 – Well-structured math with clear cultural context
• 5 – Mathematics flawlessly integrated with cultural elements
Format your response exactly like this (replace the numbers with your scores):
Cultural Relevance: 5
Explanation: The adapted text is deeply integrated with Indian culture, accurately
reflecting significant traditions and practices.
Language Fluency: 5
Explanation: The text uses natural Indian expressions and terminology, making it easy
to read and culturally coherent.
Mathematical Integrity: 5
Explanation: The mathematical problem is presented correctly and is well-integrated
into the cultural context.
Do not output any extra text or placeholders such as “[score]”.
Figure 13: Prompt for LLM as Judge

```
