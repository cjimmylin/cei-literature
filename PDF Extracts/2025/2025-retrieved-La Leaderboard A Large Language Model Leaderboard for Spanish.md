---
title: "2025-retrieved-La Leaderboard A Large Language Model Leaderboard for Spanish - PDF Extract"
source_pdf: "2025-retrieved-La Leaderboard A Large Language Model Leaderboard for Spanish.pdf"
pages: 43
extracted_at: "2026-02-13T09:50:30.400381"
---

# PDF Extract: 2025-retrieved-La Leaderboard A Large Language Model Leaderboard for Spanish

**Source PDF:** 2025-retrieved-La Leaderboard A Large Language Model Leaderboard for Spanish.pdf
**Total Pages:** 43

---

## Content

```
--- Page 1 ---

arXiv:2507.00999v1  [cs.CL]  1 Jul 2025
La Leaderboard: A Large Language Model Leaderboard for Spanish
Varieties and Languages of Spain and Latin America
María Grandury1,2, Javier Aula-Blasco3, Júlia Falcão3, Clémentine Fourrier4,
Miguel González2, Gonzalo Martínez5, Gonzalo Santamaría6
Rodrigo Agerri7, Nuria Aldama6, Luis Chiruzzo13, Javier Conde2, Helena Gómez12, Marta
Guerrero6, Guido Ivetta11, Natalia López6, Flor Miriam Plaza-del-Arco9, María Teresa
Martín-Valdivia10, Helena Montoro6, Carmen Muñoz6, Pedro Reviriego2, Leire Rosado6,
Alejandro Vaca8, María Estrella Vallecillo-Rodríguez10, Jorge Vallego, Irune Zubiaga7
1SomosNLP, 2ETSIT, Universidad Politécnica de Madrid, 3Barcelona Supercomputing Center,
4Hugging Face, 5Universidad Carlos III de Madrid, 6Instituto de Ingeniería del Conocimiento,
7Centro HiTZ - Ixa, Universidad del País Vasco UPV/EHU, 8LenguajeNatural.AI,
9LIACS, Leiden University, 10Universidad de Jaén, 11Universidad Nacional de Córdoba,
12Universidad Nacional Autónoma de México, 13Universidad de la República, Uruguay
Correspondence: maria.grandury@somosnlp.org
Abstract
Leaderboards showcase the current capabili-
ties and limitations of Large Language Mod-
els (LLMs).
To motivate the development
of LLMs that represent the linguistic and
cultural diversity of the Spanish-speaking
community, we present LA LEADERBOARD 1,
the first open-source leaderboard to evalu-
ate generative LLMs in languages and lan-
guage varieties of Spain and Latin Amer-
ica.
LA LEADERBOARD is a community-
driven project that aims to establish an evalua-
tion standard for everyone interested in devel-
oping LLMs for the Spanish-speaking commu-
nity. This initial version combines 66 datasets
in Basque, Catalan, Galician, and different
Spanish varieties, showcasing the evaluation
results of 50 models. To encourage community-
driven development of leaderboards in other
languages, we explain our methodology, in-
cluding guidance on selecting the most suit-
able evaluation setup for each downstream task.
In particular, we provide a rationale for using
fewer few-shot examples than typically found
in the literature, aiming to reduce environmen-
tal impact and facilitate access to reproducible
results for a broader research community.
1
Introduction
The evaluation of multilingual Large Language
Models (LLMs) is challenging.
LLMs are ex-
pected to perform a large variety of tasks, from
problem-solving to text summarization, all in mul-
tiple languages (Guo et al., 2023). In this context,
1https://hf.co/spaces/la-leaderboard/
la-leaderboard
Figure 1: Summary of the evaluation datasets included
in LA LEADERBOARD . Disclaimer: A country does
not represent a language; flags are used for simplicity.
leaderboards have emerged as one of the standard
approaches for evaluating and comparing LLMs
in a transparent manner. As we cannot improve
what we cannot measure, it is important to develop
leaderboards that enable a more comprehensive
evaluation of LLMs across linguistic boundaries,
contributing to the development of culturally aware
AI systems that can serve diverse global linguistic
communities.
Spanish is one of the most spoken languages
worldwide, with more than 600 million speakers
(Fernández and Mella, 2024). It is the predomi-
nant language in 21 countries, where it coexists
with other languages.
Many people use Span-
ish and the local language in their daily activities.
Spain has four official languages: Spanish, Catalan,
Basque, and Galician. While Catalan and Galician
are Romance languages closely related to Spanish,
Basque is one of the world’s few language isolates
(Campbell, 2010). In Latin America (LATAM),

--- Page 2 ---

there are hundreds of indigenous languages, such
as Guarani and Náhuatl, which have influenced
local Spanish varieties (Lustig, 1996). From a so-
ciolinguistic point of view, this creates a unique
scenario for multilingual LLM evaluation. More-
over, knowing which LLMs perform best in these
languages can have deep implications for multilin-
gual communication (Strassel and Tracey, 2016).
Existing leaderboards predominantly focus on
English or a small set of high-resource languages
(Fourrier et al., 2024; Mialon et al., 2023; Pal et al.,
2024; Contributors, 2023). While Spanish is often
included in multilingual leaderboards, evaluation
datasets are typically limited and translated, either
by machines (Barth et al., 2024), failing to cap-
ture the linguistic richness of the language (Plaza
et al., 2024) or by humans2, still failing to represent
the target culture (Singh et al., 2024) Moreover, de-
spite the growing presence of LLMs in multilingual
settings, no leaderboard currently evaluates a com-
bination of languages spoken in Spain and Latin
America. This lack of representation limits the
development of models that can truly serve these
communities (Mager et al., 2018).
To
address
this
gap,
we
introduce
LA LEADERBOARD ,
the
first
open-source
leaderboard designed to evaluate generative LLMs
based on the needs of the Spanish-speaking
community. Beyond the initial set of languages
that includes Spanish and the official languages
of
Spain
(Basque,
Catalan,
and
Galician),
LA LEADERBOARD is designed to evolve, grad-
ually expanding to encompass more languages
and linguistic varieties, ensuring it reflects the
rich diversity of the global community. This new
leaderboard consists of a diverse set of evaluation
tasks (see Figure 1) designed in a way that
reflects the nuances and actual usage of the target
languages.
It is a community-driven initiative
launched by the #Somos600M Project (Grandury,
2024), aiming to foster the development of LLMs
that better represent the linguistic and cultural
diversity of the Spanish-speaking world.
We
share our approach to inspire other linguistic
communities to create similar leaderboards.
The main contributions of this work are:
• We present the community-based methodol-
ogy used to create the first open-source leader-
board for evaluating generative LLMs in Span-
ish and the official languages of Spain, with a
2https://hf.co/datasets/openai/MMMLU
scalable framework designed to include more
languages and language varieties over time.
• We introduce a logical and resource-efficient
approach to few-shot configurations, enabling
accessible and reproducible evaluations for
the wider community.
• We provide a comprehensive analysis of state-
of-the-art (SOTA) LLMs, providing insights
into their strengths and limitations in Spanish,
Catalan, Basque, and Galician.
By
addressing
the
linguistic
and
cul-
tural
diversity
of
Spain
and
LATAM,
LA LEADERBOARD sets
a
new
standard
for
multilingual LLM evaluation, which encourages
the development of models that are not only
linguistically competent but also culturally aware.
2
Related Work
Benchmarks
Several benchmarks have been de-
veloped to evaluate the performance of LLMs in
tasks like language understanding (Wang et al.,
2019), general knowledge (Hendrycks et al.,
2021a), reasoning (Sakaguchi et al., 2019), or math-
ematical problem solving (Hendrycks et al., 2021b).
There are also efforts to develop holistic bench-
marks or evaluation suites that provide a com-
prehensive evaluation of different capabilities of
LLMs (Liang et al., 2023; Gao et al., 2021; Fourrier
et al., 2023, 2024; Srivastava and et al, 2023).
Multilingual and multicultural benchmarks
LLMs are now trained in multiple high-resource
languages at the same time (Ali et al., 2024; Mar-
tins et al., 2024; Qwen Team, 2024; Jiang et al.,
2023), which means that the benchmarks must re-
flect this linguistic diversity. A common approach
is machine translating English tests (Holtermann
et al., 2024; OpenAI, 2023). However, translation
errors may add noise to the results, making them
less reliable (Plaza et al., 2024). Furthermore, each
language has its nuances, preferred styles, and cul-
tural background, which unrevised machine trans-
lation may fail to capture (Plaza-del-Arco et al.,
2020; Singh et al., 2024). Ideally, specific test
sets should be originally written in the target lan-
guage or manually adapted (Nangia et al., 2020)
to capture the richness and cultural and linguistic
subtleties associated with it. This is slowly becom-
ing the trend as shown by the recently released
language-specific (Mercorio et al., 2024; Quercia

--- Page 3 ---

et al., 2024) and multilingual culturally aware (Ro-
manou et al., 2024; Salazar et al., 2025; Myung
et al., 2025; Romero et al., 2024) benchmarks.
Leaderboards
Benchmarks are the pieces of
the LLM evaluation puzzle that provide valuable
but fragmented information on their performance.
Leaderboards and arenas use these evaluation sets
to compare the performance of LLMs in a neutral,
third-party manner through automatic evaluations
(Mialon et al., 2023) or human judgments (Chiang
et al., 2024). On some community-oriented leader-
boards (Fourrier et al., 2024), anyone can submit
their LLMs for evaluation, and the tools, tests, and
results are open, allowing for reproducibility. This
represents a good way to drive progress in LLM
development by enabling people with limited com-
pute to compare their models to the current SOTA.
Multilingual leaderboards
Leaderboards ex-
hibit the same shortcomings as benchmarks when
evaluating languages other than English. To ad-
dress this problem, specific leaderboards are being
developed in different languages such as Italian
(Mercorio et al., 2024), Korean (Kim et al., 2024),
Chinese (Contributors, 2023), Arabic (Elfilali et al.,
2024) or Polish (Jassem et al., 2025).
Spanish leaderboards
Focusing on the Spanish
language, the ODESIA leaderboard3 by UNED
NLP
features
14
bilingual
Spanish-English
datasets from discriminative shared tasks. The
team evaluates 10 LLMs. While submissions are
open, the evaluation datasets are private, avoiding
task contamination (Salido et al., 2025) but making
it impossible to reproduce the results locally.
Regarding text generation, Spanish is represented
in the Chatbot Arena4, which features a dedicated
category, and in SCALE’s private leaderboard5.
However, both exclusively evaluate a fixed set of
models. The only existing leaderboard including
a language from Spain or Latin America other
than Spanish is CLUB6, developed by the BSC
as part of the AINA Project, which combines
8 Catalan datasets and evaluates 5 BERT and
RoBERTa-based models.
In this work, we present the methodology used
to create a comprehensive, fully open-source
3https://leaderboard.odesia.uned.es
4https://lmarena.ai
5https://scale.com/leaderboard/spanish
6https://club.aina.bsc.es
leaderboard for languages and language vari-
eties from Spain and Latin America that assesses
different capabilities of generative models, in-
cluding domain knowledge, information extrac-
tion, linguistic proficiency, and ethical aspects.
LA LEADERBOARD aims to serve as a reference
for the Spanish-speaking scientific community, fos-
tering the development of more robust and cultur-
ally adequate LLMs.
3
LA LEADERBOARD
LA LEADERBOARD is a community-driven initia-
tive that brings together 66 datasets in Span-
ish, Catalan, Basque, and Galician, covering di-
verse tasks and domains. Public since September
23, 2024, LA LEADERBOARD has received over
15,000 visits in five months and currently show-
cases evaluation results from 50 models.
3.1
Data Collection
Most of the datasets in LA LEADERBOARD were
donated by 13 research groups. Initially, these con-
tributions were received through a publicly shared
Google Form (Appendix E) or direct outreach. In
particular, 7 datasets were specifically created for
LA LEADERBOARD (AQuAS, ClinTreatES, Clin-
DiagnosES, HumorQA, SpaLawEx, TELEIA, and
RAGQuAS). We also included widely used open-
source benchmarks such as Belebele.
LA LEADERBOARD keeps
expanding
with
dataset
contributions
such
as
CONAN-EUS
and VeritasQA. These new connections are
bidirectional: we actively share this initiative in
relevant conferences and reach out to research
groups, while others contact us upon discovering
LA LEADERBOARD . Beyond collecting existing
datasets, we are also fostering collaborations
to enhance the representation of languages and
linguistic varieties across Latin America.
To thank research groups for their donations,
we include in LA LEADERBOARD ’s interface the
corresponding logo and dataset citation. Moreover,
the dataset authors are acknowledged in this paper.
3.2
Task Construction
3.2.1
Datasets
Including diverse evaluation datasets is essential
for building a comprehensive leaderboard. This
section discusses the key axes that guided their se-
lection. Table 1 enumerates the datasets organized
by language and task type, while Table 2 shows the

--- Page 4 ---

upcoming datasets that have been recently donated
and not yet evaluated. In Appendix A, we provide
the citations and further details about the datasets,
including origin and domain.
Languages
LA LEADERBOARD contains
22
evaluation datasets in Spanish, including the
varieties of Spain, Mexico, Argentina, Chile, and
Uruguay. It also gathers datasets in all the official
languages of Spain, with 18 datasets in Catalan, 17
in Basque, and 9 in Galician.
Origin
We aim to evaluate models with high-
quality datasets that reflect the cultural and lin-
guistic idiosyncrasies of each language. For this
reason, we only include datasets that have been
annotated or revised by at least one native speaker
of the language. We prioritize the inclusion of
datasets originally created in the language they
evaluate, which constitute 55% of the leaderboard.
When this is not possible and translation is required,
we prioritize datasets translated by human profes-
sionals. Not only does this prevent the loss of
linguistic nuances that happens with machine trans-
lation (Plaza et al., 2024), but it also allows transla-
tors to adapt the text to the target culture (Nangia
et al., 2020) and to identify errors in the source
datasets and ensure that no extra hints regarding
the answer are given in the input prompt (Bau-
cells et al., 2025). In LA LEADERBOARD , 38% of
the datasets have been manually translated from
an existing English benchmark. We also acknowl-
edge that, given the low-resource nature of some
languages we cover, machine translation is more
affordable than human translation. However, we
only include such datasets if the automatic trans-
lation was comprehensively reviewed by a per-
son proficient in the target language. Only 7%
of the datasets in LA LEADERBOARD are manual
reviews of machine-translated datasets.
Format
The multiple-choice question-answering
(MCQA) format is widely used for automatic
evaluations due to its simplicity. Thus, MCQA
is the format of 59% of the tasks included in
LA LEADERBOARD . We acknowledge that the
literature has identified some issues with MCQA
tasks, such as models’ sensitivity to answer or-
der (Pezeshkpour and Hruschka, 2024; Mina et al.,
2025) or lack of task understanding (Khatun and
Brown, 2024). Moreover, some suggest that this
type of task does not reflect the actual models’
responses and capabilities (Li et al., 2024; Wang
et al., 2024a). To address this issue, we also include
text generation tasks, such as summarization, evalu-
ated using NoticIA for Spanish, caBreu for Catalan,
and Summarization-GL for Galician. We evaluate
long-form question-answering in Spanish using the
AQuAS and RagQuAS datasets. Finally, we as-
sess counter-narrative generation with RefutES in
Spanish and CONAN in Basque and Spanish.
Domains
LA LEADERBOARD includes
well-
known generalist datasets aimed at evaluating a
model’s capability to understand and complete a
task, such as Belebele, WNLI, and XStoryCloze.
We also include evaluation datasets focused on
truthfulness assessment, such as VeritasQA and
the Galician translation of TruthfulQA. There
are, in addition, several domains represented in
LA LEADERBOARD , such as the medical (e.g.,
ClinTreatES), legal (e.g., SpaLawEx), and press
(e.g., caBreu, NoticIA). We also include ethics-
oriented datasets, evaluating stereotype generation
in Spanish and Catalan with CrowsPairs.
Tasks
The types of tasks chosen for our leader-
board extend those usually included in well-known
leaderboards (e.g., reasoning, natural language in-
ference, question answering or summarization) to
other task types for which high-quality datasets ex-
ist in our target languages (e.g., counter-narrative
generation or linguistic acceptability). For consis-
tent performance comparisons across languages,
we prioritize tasks available in multiple languages.
3.2.2
Metrics
The MCQA tasks are evaluated by measuring the
logarithmic probabilities (LOGPROBS) of models’
outputs among a restricted list of options. For
text generation tasks, we compare the expected
(gold-standard) and given responses using various
metrics depending on the original authors’ imple-
mentation, including BLEU (Papineni et al., 2002),
ROUGE (Lin, 2004) and Semantic Answer Simi-
larity (SAS, Risch et al., 2021). Furthermore, fol-
lowing the recent trend of evaluating text gener-
ation tasks using LLMs, we are adapting an au-
tomated Judge-LLM metric from Zubiaga et al.
(2024). Since SAS and LLM-based metrics are not
currently supported in the evaluation suite we use,
the LM Evaluation Harness (Gao et al., 2021), we
implement them in our open-source fork7.
7https://github.com/somosnlp/
lm-evaluation-harness

--- Page 5 ---

Task Type
Spanish
Catalan
Basque
Galician
Common-sense
reasoning
copa_es
xstorycloze_es
copa_ca
xstorycloze_ca
xcopa_eu
xstorycloze_eu
xstorycloze_gl
Ethics
crows_pairs_es
crows_pairs_ca
–
–
Linguistic
acceptability
escola
catcola
–
galcola
Math
mgsm_direct_es
mgsm_direct_ca
mgsm_direct_eu
mgsm_direct_gl
NLI
wnli_es
xnli_es
teca
wnli_ca
xnli_ca
epec_koref_bin
qnli_eu, wiceu
wnli_eu, xnli_eu
xnli_gl
Paraphrasing
paws_es
parafrases_sushi
parafraseja
paws_ca
–
parafrases_gl
paws_gl
Question
answering
aquas
clindiagnoses
clintreates
spalawex
teleia
ragquas
xquad_es
arc_ca
catalanqa
coqcat
openbookqa_ca
piqa_ca
siqa_ca
xquad_ca
bertaqa
bhtc_v2
eus_exams
eus_proficiency
eus_trivia
vaxx_stance
openbookqa_gl
Reading
comprehension
belebele_spa_Latn
belebele_cat_Latn
belebele_eus_Latn
eus_reading
belebele_glg_Latn
Summarization
noticia
xlsum_es
cabreu
–
summarization_gl
Text
classification
humorqa
fake_news_es
offendes
catalonia_
independence
bec2016_eu
–
Table 1: Datasets of LA LEADERBOARD as of February 2025 organized by task type and language.
Task Type
Dataset
Languages
Adaptation
phrases
Catalan, Spanish, Valencian
Common-sense
reasoning
xstorycloze_gl
Galician
Counter-narrative
generation
conan_eus/mt_es
refutes
Basque, Spanish
Spanish
Ethics
h4rmony_eval
Spanish
Text
classification
haha
Spanish
Natural language
americasnlp_nli
Aymara, Asháninka, Bribri, Guarani, Náhuatl,
Otomí, Quechua, Rarámuri, Shipibo-Konibo, Wixarika
inference
meta4xnli
Spanish
paes_cl
Spanish
Question
voces_originarias
Aymara, Guarani, Tehuelche, Náhuatl, Quechua
answering
medexpqa
Spanish
quales
Spanish
flores
Spanish, Catalan, Basque, Galician
Translation
americasnlp_mt
Spanish, Aymara, Asháninka, Bribri, Guarani, Náhuatl,
Otomí, Quechua, Rarámuri, Shipibo-Konibo, Wixarika
tradu_latam
Spanish, Aymara, Guraraní, Tehuelche, Náhuatl, Quechua
Truthfulness
truthfulqa
Spanish, Catalan, Basque, Galician
veritasqa
Spanish, Catalan, Galician
Table 2: Datasets that have been recently donated to LA LEADERBOARD and are not yet included in the evaluation
results, including benchmarks involving American Indigenous languages.

--- Page 6 ---

3.3
Code Bases
3.3.1
Backend
We acknowledge the cost of running evaluations
and want to ensure that any researcher or developer
can compare their models to the state-of-the-art
and follow their evolution. This is why submit-
ting a model for evaluation is open to the whole
community. Once a model has been added to the
evaluation queue, the last commit of the model is
stored for reproducibility and to enable future com-
parisons of different versions. The results from
the LM Evaluation Harness (Gao et al., 2021) are
normalized according to the following formula:
normalized_value = raw_value −random_baseline
max_value −random_baseline
(1)
where random_baseline is 0 for generative tasks
and 1/n for MCQA tasks with n choices.
3.3.2
Frontend
The implementation of LA LEADERBOARD is
based on the HuggingFace leaderboard template8.
The frontend is developed using Gradio (Abid et al.,
2019) and presents the evaluation results catego-
rized by language. To ensure transparency and
reproducibility, we share the evaluation command
and normalization formula. To bring the tool closer
to the community, the information and submission
guidelines are available in English and Spanish.
3.3.3
License
Since we want to motivate other communities to
create their own, LA LEADERBOARD is published
under the permissive Apache 2.0 license9.
3.4
Efficiency Considerations
3.4.1
Number of Few-Shot Examples
Recent literature reveals significant inconsistency
in the number of examples (shots) used when eval-
uating large language models (LLMs). While early
research demonstrated notable performance im-
provements with 3-5 in-context examples (Brown
et al., 2020), current evaluation practices vary con-
siderably across different models and benchmarks.
For instance, the Open LLM Leaderboard employs
0-5 shots depending on the task, Mistral-7B gener-
ally follows this range with an exception of 8 shots
for GSM8K (Cobbe et al., 2021), and Llama 3 and
8https://hf.co/spaces/
demo-leaderboard-backend/leaderboard
9https://www.apache.org/licenses/LICENSE-2.0
OLMo models focus primarily on zero-shot eval-
uation. In contrast, Gemini models use a broader
range of 0-10 shots, including “variable-shot” con-
figurations. This variation extends to language-
specific models, with Salamandra10 and Latxa (Etx-
aniz et al., 2024) families using different shot con-
figurations in their evaluations, typically ranging
from 0 to 5 shots.
Given this myriad of options, when choosing the
number of shots to use in LA LEADERBOARD , we
take into consideration the following aspects:
A. Base vs. instruct models The number of
shots should allow for a fair evaluation of the base
models without helping instruct models too much.
Also, the availability of structured datasets in spe-
cific evaluation formats—such as MCQA—is very
low in mid- and low-resource languages. This
means that models trained on English-heavy cor-
pora are more likely to have encountered these
structured formats in English than in other lan-
guages, potentially biasing their performance.
B. Cognitive bias Models suffer from cogni-
tive bias depending on the order and options pre-
sented as few-shots (Zhao et al., 2021; Pezeshkpour
and Hruschka, 2024; Mina et al., 2025). Thus, we
ensure that, in MCQA tasks, all possible correct
options are included in the in-context learning in-
stances. For example, in an MCQA task with four
possible answers, we evaluate on a 4-shot setting,
with each shot showing one of the four options as
correct, in random order. This is done unless it
interferes with item A.
C. Context windows The context window limi-
tations of language models vary significantly based
on hardware constraints and architectural choices,
affecting their ability to process long-form tasks
such as summarization and reading comprehension.
For example, while the Spanish government’s 40B-
parameter ALIA model11 operates with a 4,096-
token context window, Meta’s Llama 3.2 1B model
can handle up to 128K tokens12. To ensure fair eval-
uation across models with different context window
capacities, few-shot examples are employed with
a maximum limit of 2,048 tokens, following the
methodology established in previous research on
LLM analysis (Biderman et al., 2023).
D. Prompt format The evaluation methodol-
ogy employed task-specific prompts from the LM
10https://hf.co/BSC-LT/salamandra-7b-instruct
11https://hf.co/BSC-LT/ALIA-40b
12https://ai.meta.com/blog/
llama-3-2-connect-2024-vision-edge-mobile-devices

--- Page 7 ---

Evaluation Harness, with new prompts created for
previously unimplemented tasks following estab-
lished formats and validated by dataset authors.
The number of few-shots varied based on prompt
complexity: convoluted prompts (e.g., paraphras-
ing with PAWS and reasoning with COPA) used
3 in-context examples to allow models to under-
stand the task while complying with items A and
C (Brown et al., 2020); straightforward question-
answering tasks employed 2-shot evaluation, while
tasks with explicit, naturally structured prompts
(like ClinDiagnosES and NoticIA) and those evalu-
ating sentence continuation probability (e.g., XSto-
ryCloze) were conducted using 0-shot evaluation.
3.4.2
Measuring Model Efficiency
The evaluation was performed using two NVIDIA
H100 GPUs with Hopper architecture and 64 GB
of HBM memory in the MareNostrum 5 High-
Performance Computer13, maintaining identical
configurations across instances to ensure consistent
measurements. Performance metrics included task
execution time and energy consumption, tracked
using the Energy Aware Runtime (EAR) package14,
with all tasks running at a batch size of 1.
Task execution duration, which includes token
prediction time, response length, and tokenizer ef-
ficiency, was measured to assess model speed for
time-sensitive applications. The duration of task ex-
ecution is influenced by multiple factors beyond to-
ken prediction time, including the response length
generated and the language-specific tokenization
efficiency (Conde et al., 2024).
Energy consumption was recorded in kWh and
converted to CO2 equivalents using the European
Commission’s conversion ratio for Spain (0.158
kg CO2/kWh), as the evaluation was conducted in
Barcelona (Lottick et al., 2019).
4
Evaluation Results and Analysis
We focus on evaluating models accessible to the
broader community. We select 50 open-weights
models from various families, primarily ranging
from 1B to 9B parameters, while including larger
quantized models. We consider multilingual mod-
els trained by large technological companies and
startups like Meta-Llama (Grattafiori et al., 2024)
13https://www.bsc.es/ca/marenostrum/
marenostrum-5
14https://www.bsc.es/research-and-development/
software-and-apps/software-list/
ear-energy-management-framework-hpc
Model
Top10
ES
CA
EU
GL
gemma-2-9b-it
43
61.69
57.30
54.13
46.49
gemma-2-9b
43
57.21
59.60
53.80
48.58
Meta-Llama-3.1-8B-IT
41
59.03
57.01
49.87
45.07
Qwen2.5-32B-IT-GPTQ-Int4
38
64.06
56.80
49.23
52.52
Qwen2.5-14B-IT-GPTQ-Int8
35
60.59
54.08
49.05
52.13
EuroLLM-9B *
30
55.00
57.32
38.92
46.36
Meta-Llama-3.1-8B
28
55.62
56.52
46.90
44.90
salamandra-7b *
26
52.17
54.13
45.80
39.88
salamandra-7b-instruct *
25
51.41
53.22
46.19
41.65
Qwen2.5-7B
25
58.79
57.28
42.51
46.82
aya-expanse-8b
20
55.42
53.99
41.99
43.38
salamandra-2b *
8
46.60
41.05
39.28
34.99
Qwen2.5-1.5B
8
52.60
47.88
38.13
38.79
gemma-2-2b-it
5
54.85
48.27
50.27
39.79
Qwen2.5-1.5B-IT
5
54.38
45.09
39.04
39.27
salamandra-2b-instruct *
3
43.83
43.28
38.57
34.53
gemma-2-2b
2
51.59
50.22
39.81
39.29
leniachat-qwen2-1.5B-v0 *
2
51.14
40.97
38.29
36.16
EuroLLM-1.7B-IT *
2
47.92
45.28
36.19
34.67
Table 3: Best performing models ranked by the number
of tasks in which they achieved a top-10 placement
(see “Top10” column), showing their average language
performance. Target language–optimized models are
indicated by an asterisk (*). Complete per-language
top-10 frequencies can be found in Figure 4, and full
average scores for all models are shown in Figure 3.
and Mistral (Jiang et al., 2023) as well as mod-
els such as EuroLLM (Martins et al., 2024) and
Salamandra15, which have been designed by Eu-
ropean and Spanish research groups specifically
to process our target languages more efficiently
and capture cultural nuances. We assess both the
base and instruction-tuned versions when available
(Appendix C). Each model-task pair was evaluated
once, and the raw, pre-normalization results ana-
lyzed in this work are publicly available16.
4.1
Model performance
Table 3 shows that the models most consistently
ranking in the top 10 across languages are Gemma-
2-9B base and instructed, Llama-3.1-8B-IT, and
the quantized versions of Qwen-2.5-IT 14B and
32B. When prioritizing transparency, EuroLLM-
9B stands out, followed by Salamandra-7B. For
resource-constrained settings, Salamandra-2B and
Qwen-2.5-1.5B offer the best performance.
Performance per task
As illustrated in Figure 2,
the evaluation results are generally better for NLI
tasks, including textual entailment and paraphras-
ing, and worse for language proficiency tests, with
all four languages having similar performance on
both tasks. Within the language proficiency tests,
which combine reading comprehension, linguistic
15https://hf.co/collections/BSC-LT/
salamandra-66fc171485944df79469043a
16https://hf.co/datasets/la-leaderboard/
results

--- Page 8 ---

Figure 2: Results per type of task type and language.
acceptability, and summarization, results are par-
ticularly low for summarization tasks. In question
answering and reasoning tasks, there is a larger
inter-language difference, with Galician having sig-
nificantly lower scores overall, while Basque ob-
tains the best results for reasoning but the second
worst for question answering. While commonsense
reasoning results are generally good, math reason-
ing yields the lowest results, which could be related
to a too strict metric (exact match). Further analysis
is needed to understand whether these differences
are due to the datasets used or indeed to the models’
performance. The poor results on language profi-
ciency tests also warrant a detailed examination to
understand their implications, as they may indicate
fundamental limitations in the models’ knowledge
across languages.
Performance per language
Regarding specific
models, the same five (Gemma2, Llama3.1, and
quantized Qwen2.5) consistently rank among the
top ten performers. However, we find that some
models stand out for specific language-task pairs.
In Spanish, AYA-Expanse-8B joins the top three for
QA, EuroLLM-9B for reasoning, and RigoChat-7B
is in the top four for language proficiency. In Cata-
lan, EuroLLM ranks among the top three for both
QA and reasoning tasks. For Basque, Salamandra-
7B-IT is the second-best QA model, while Latxa-
7B and Salamandra-7B occupy the first and second
positions in reasoning and the third and second
positions in classification, respectively. In Gali-
cian, EuroLLM-9B is the best model for QA, fol-
lowed by its instructed version, Salamandra-7B
ranks third in reasoning, and AYA-Expanse-8B
takes second place in NLI.
Performance by training data configuration
It
is valuable to compare the different language con-
figuration strategies in training. Salamandra and
EuroLLM, by distributing tokens in the pre-training
data fairly among languages, achieve homogeneous
performance and, in particular, reinforce Galician
and Basque, but lose ground in Spanish and Cata-
lan to models supported by high-resource corpora.
Gemma2, which prioritizes volume over linguistic
diversity, stands out for just the opposite; training
on a large but linguistically imbalanced dataset al-
lows the model to transfer patterns learned from
English, maths, and code, and consistently rank
among the top models overall. This shows that,
sometimes, breadth of knowledge can compensate
for the lack of language-specific data.
The results confirm that the strategy of pre-
training from scratch on a large multilingual corpus
is the one that offers the most consistent and ho-
mogeneous coverage. Qwen-2.5, trained on 29
languages, and Llama-3.1, trained on 8, rank high
in all languages. Moreover, systems that use con-
tinuous pre-training - adding large-scale data in
a new language plus some English data to avoid
catastrophic forgetting - achieve peak scores in
the target language; e.g., Latxa holds the second-
highest mark in Basque reasoning. Finally, models
that just fine-tune on target language data without
extending the pre-training (e.g., RigoChat or some
Instruct variants) gain fluency and style, but the
improvement in reasoning and QA tasks is modest,
and models rarely enter the top 10. In summary, the
earlier and deeper the model is exposed to the target
languages, the higher its average scores; a poste-
riori strategies function as beneficial reinforcers,
especially in less-resourced languages, but do not
replace the power of extensive multilingual pre-
training.
Performance by training compute
Regarding
the computational budget and the hardware used,
public data is scarce. Regarding large tech com-
panies we can consider Llama-3.1-8B, which was
trained for 1.5M GPU-h. By contrast, other evalu-
ated models required three to four orders of mag-
nitude fewer. As expected, the results confirm that
teams with access to GPUs/TPUs and high-end
accelerators (TPUv5p, H100 or A100 in large clus-
ters) can apply the strategies that we highlighted
in the previous section as the most successful -
massive multilingual pre-training and continuous
pre-training - reflecting in significantly higher av-
erage scores. However, the same results also nu-
ance the linear relationship between investment and
performance as Salamandra-7B, despite its large
budget (600 k GPU-h), falls in the middle of the

--- Page 9 ---

table. Overall, the dashboard illustrates that com-
putational abundance enables impactful techniques,
but that dataset quality and fine-tuning remain de-
cisive levers for converting that power into real
performance.
Performance vs. size
In general, our experi-
ments show some correlation between performance
and size, with models in the range of 1-2B param-
eters achieving better scores for their size. This
is particularly true for Gemma-2-2B and Qwen-
2.5-1.5B, both base and instructed models. Among
the top 10 models, we find that all have between 8
and 9 billion parameters, except for the quantized
versions from the Qwen family.
Performance per model type
For the same
VRAM requirement, quantized models with more
parameters outperform full-precision models with
fewer parameters. We don’t observe any correla-
tion between performance and whether the model
is pre-trained or instruction-tuned, as this varies
depending on the model.
4.2
Energy consumption
The total computational resources amount to
660.87 hours of processing time and 582.84 kWh of
energy consumption, resulting in 92.09 kg of CO2
emissions. On average, each model consumes 9.25
kWh (median 6.88, SD 8.42), showing a wide vari-
ety in energy usage. The models that consume the
most energy are Grommeanuer-7B-IT, Qwen-2.5-
32B-IT-GPTQ-Int4, and Qwen-2.5-14B-IT-GPTQ-
Int8, each exceeding 30 kWh. On the other hand,
Salamandra-2b, FLOR-1.3B-IT, and LLama-3.2-
1B-IT are the most energy-efficient, consuming less
than 2.1 kWh each.
Energy consumption vs. size
As expected, a
strong correlation between model size and energy
dissipation is observed, as the number of arithmetic
operations required to predict a token is related to
the number of parameters of the model. However,
some outliers are observed, such as Qwen, which
consumes significantly more energy across all its
sizes compared to other models. Conversely, mod-
els like FLOR exhibit considerably lower energy
consumption across their different sizes relative to
other models of similar scale.
Energy consumption vs. task
Similarly, as an-
ticipated, text generation tasks such as summariza-
tion require more energy for evaluation. Since
LLMs generate text token by token and their pre-
diction speed remains constant (assuming the same
hardware and stable conditions), the most energy-
intensive tasks are expected to be those that require
the generation of larger amounts of text.
Energy consumption vs. performance
Our ex-
periments show a strong correlation between the
energy consumed at inference and the model perfor-
mance. For one of the overall top models, Gemma-
2-9B, its instruction-tuned version excels with a
third of the energy consumed by the base version.
We observe a trend of instructed models consuming
less energy, due to the verbosity of base models.
5
Conclusions and Future Work
In this paper, we propose a methodology to cre-
ate community-driven leaderboards, including key
points to gather diverse datasets and the rationale
behind a more efficient and accessible evaluation
setup. In doing so, we hope to inspire the creation
of more leaderboards that fulfil the needs of diverse
linguistic communities.
In particular, we present LA LEADERBOARD ,
the first open-source leaderboard to evaluate LLMs
in languages from Spain and Latin America. It
is the result of a collaboration among 13 re-
search groups. LA LEADERBOARD consists of 66
datasets in Spanish, Catalan, Basque, and Gali-
cian, and covers a wide range of task types and do-
mains. The results of evaluating 50 LLMs suggest
that the top-performing models in the target lan-
guages are Gemma-2-9B base and instruct, Llama-
3.1-8B-IT, and the quantized versions of Qwen-
2.5-IT 14B and 32B. However, for domain-specific
applications, particular linguistic contexts, or de-
ployment scenarios with computational constraints
or transparency requirements, alternative models
(e.g., Salamandra-7B and EuroLLM-9B) demon-
strate competitive performance metrics.
Our planned next steps include evaluating the re-
cently donated datasets, with a special focus on
indigenous languages. We will also add larger
open models and proprietary models. Moreover,
we are organizing a hackathon to create a bench-
mark to measure cultural adequacy in each Spanish-
speaking country. Finally, we welcome any person
or organization interested in joining our effort. This
way, we hope that LA LEADERBOARD will keep
evolving to include more languages, language vari-
eties, and use cases that motivate the development
of LLMs that better serve our diverse community.

--- Page 10 ---

Limitations
Indigenous languages
We acknowledge that
indigenous languages from Latin America are
not yet included among the evaluation results
of LA LEADERBOARD . However, we have on-
going collaborations to include existing bench-
marks and create new ones to keep extending
LA LEADERBOARD to be as inclusive as possible
and reflect the diversity of the Spanish-speaking
community.
Spanish
language
varieties
Currently,
the
leaderboard includes datasets in the Spanish va-
rieties of Spain, Mexico, Argentina, Chile, and
Uruguay. Although we don’t know the exact origin
of all the samples from some third-party datasets,
we estimate that less than 25% of all the Spanish
datasets in the leaderboard come from LATAM. We
plan to increase this percentage by collaborating
with LATAM research groups in the creation of an
open hackathon.
Large and proprietary models
To improve the
coverage of the state-of-the-art language models
for the use cases included in LA LEADERBOARD ,
it would be interesting to evaluate larger language
models as well as proprietary models.
Contamination
Another pending task is to anal-
yse potential contamination (Sainz et al., 2023)
within our leaderboard. We have not addressed
this yet because a high percentage of the datasets
used are very recent and niche, making it un-
likely that they have been incorporated into train-
ing data, unlike more established benchmarks such
as MMLU (Hendrycks et al., 2021a; Wang et al.,
2024b; Taghanaki et al., 2024) that serve as pri-
mary pillars in model evaluation in every model
report. Nevertheless, we have started to evaluate
contamination to ensure in the short-term future
that we provide high-quality results.
For
the
datasets
specifically
created
for
LA LEADERBOARD , we advised the correspond-
ing authors to release them gated to avoid being
unintentionally included in training datasets by web
scraping; AQuAS and RagQuAS are gated. The au-
thors of TELEIA decided to release an adaptation
of their dataset and keep the original private to be
able to analyze contamination through time.
Ethical Considerations
Fair representation
Since our objective is to es-
tablish an evaluation standard for Latin America
and Spain, it is important to properly represent the
linguistic and cultural diversity of the community
in order to avoid the perpetuation, or even amplifi-
cation, of stereotypes and inequalities.
Third-party datasets
Some of the evaluation
datasets included in LA LEADERBOARD were cre-
ated by organizations other than our data contrib-
utors. As a result, we acknowledge the possibility
that some of these datasets may have been devel-
oped using practices that could be considered un-
ethical. These concerns range from potential legal
violations to extractive data collection methods that
may impact disadvantaged communities.
Environmental impact
Evaluating 50 language
models on 66 tasks required 660.87 hours of com-
pute, translating to 92.09 kg of CO2. However, we
hope that by publishing a comprehensive evaluation
of the available models, LA LEADERBOARD will
contribute to reducing the total environmental im-
pact of individual private evaluations.
Misuse of La Leaderboard
We welcome model
submissions from everyone. This could potentially
lead to overuse, with people sending many different
versions of the same model. We plan to mitigate
this behaviour by following the spam mitigation
strategies from the Open LLM Leaderboard (Four-
rier et al., 2024).
Acknowledgments
LA LEADERBOARD is the result of the collabora-
tion between many researchers, and we extend our
heartfelt thanks to each of them.
Coordination
María Grandury, Javier Aula-
Blasco, Clémentine Fourrier, Marta Guerrero, Pe-
dro Reviriego.
Dataset donation leads
Javier Aula-Blasco,
Omar Sanseviero, Alejandro Vaca, Marta Guerrero,
Álvaro Barbero, Rodrigo Agerri, Javier Conde,
Flor Miriam Plaza-del-Arco, María Teresa Martín-
Valdivia, Helena Gómez, Luciana Benotti, Iker
García-Ferrero, Jorge Vallego, Luis Chiruzzo.
New dataset creation and annotation
Carmen
Muñoz, Helena Montoro, Leire Rosado, Marta
Guerrero, Nuria Aldama, Natàlia Fuertes, Alejan-
dro Vaca, Marina Mayor-Rocher, Nina Melero,

--- Page 11 ---

Elena Merino-Gómez, Miguel González, Raquel
Ferrando, Javier Conde, Gonzalo Martínez, Pedro
Reviriego Daniel Vila, Álvaro Bartolomé, Ignacio
Talavera.
Metric and task implementation
Gonzalo San-
tamaría, David Betancur, Anna Sallés, Irene Bau-
cells, Javier Aula-Blasco, Julen Etxaniz, Alejandro
Vaca, María Grandury, Gonzalo Martínez, Miguel
González, Iker García-Ferrero, Guido Ivetta. María
Estrella Vallecillo-Rodríguez, Irune Zubiaga.
Leaderboard implementation
María Grandury,
Clémentine Fourrier, Nathan Habib.
Model evaluation
Júlia Falcão, María Grandury,
Miguel González, Gonzalo Martínez, Javier Aula-
Blasco, Bram Vanroy.
Paper writing
All the co-authors, especially
María Grandury, Rodrigo Agerri, Pedro Re-
viriego, Javier Aula-Blasco, Flor Miriam Plaza-
del-Arco, Clémetine Fourrier, Gonzalo Martínez,
Luis Chiruzzo, Alejandro Vaca, Carmen Muñoz,
Marta Guerrero, Javier Conde, Guido Ivetta, Júlia
Falcão, Álvaro Barbero, Manuel Mager.
Communication
Maria
Sayavera,
Jaume
Lozano, Florent Daudens, Brigitte Tousignant,
Rafael Muñoz, Valentín Cardeñoso.
Computational resources
Barcelona Supercom-
puting Center, Universidad Politécnica de Madrid,
HuggingFace, The Flemish Supercomputer Center.
Funding
The work of the co-authors of this paper
has been supported by multiple projects.
• The coordination and implementation of
LA LEADERBOARD by María Grandury was
carried out on a voluntary basis for six months,
after which her work was supported by the
Universidad Politécnica de Madrid (UPM).
• The work by the UPM team was supported
by the Agencia Estatal de Investigación (AEI)
(doi:10.13039/501100011033) under Grants
FUN4DATE (PID2022-136684OB-C22) and
SMARTY (PCI2024-153434) and by the Eu-
ropean Commission through the Chips Act
Joint Undertaking project SMARTY (Grant
101140087).
• The work by the Barcelona Supercom-
puting Center team and the datasets do-
nated by ILENIA are funded by the Min-
isterio para la Transformación Digital y
de la Función Pública and Plan de Re-
cuperación, Transformación y Resiliencia
- Funded by EU – NextGenerationEU
within the framework of the project ILE-
NIA with references 2022/TL22/00215337,
2022/TL22/00215336, 2022/TL22/00215335
and 2022/TL22/00215334, and within the
framework of the project Desarrollo Mode-
los ALIA.
• The work of LenguajeNatural.AI is self-
funded and self-supported by the company’s
resources.
• The contributions of Rodrigo Agerri and Irune
Zubiaga are partially funded by the following
MCIN/AEI/10.13039/501100011033 projects:
(i) DeepKnowledge (PID2021-127777OB-
C21) and ERDF A way of making Europe;
(ii) DeepMinor (CNS2023-144375) and Euro-
pean Union NextGenerationEU/PRTR. Irune
Zubiaga is supported by a UPV/EHU PIF
2025 grant.
• The contributions of Guido Ivetta are sup-
ported by Fundación Vía Libre and Univer-
sidad Nacional de Córdoba, Argentina.
• The work by the SINAI team has been
partially supported by projects CONSENSO
(PID2021-122263OB-C21), MODERATES
(TED2021-130145B-I00),
SocialTOX
(PDC2022-133146-C21) funded by Plan Na-
cional I+D+i from the Spanish Government.
• The contributions of Jorge Vallego are sup-
ported by the H4rmony project and the Aso-
ciación Latinoamericana de Ecolingüística.
Community
This project is a community-driven
effort that continues to evolve. We thank every-
one who has provided valuable feedback via ACL
Rolling Review (ARR), the SomosNLP Discord
community, the interface’s Discussions tab, and
in person at the KHIPU 2025 conference and the
NAACL 2025 workshop "Language Models for
Underserved Communities". We are grateful for
the support, and invite the entire Ibero-American
NLP community to join us.

--- Page 12 ---

References
Abubakar Abid, Ali Abdalla, Ali Abid, Dawood Khan,
Abdulrahman Alfozan, and James Zou. 2019. Gradio:
Hassle-free sharing and testing of ml models in the
wild. arXiv preprint arXiv:1906.02569.
Rodrigo Agerri, Roberto Centeno, María S. Espinosa,
Joseba Fernandez de Landa, and Álvaro Rodrigo.
2021. VaxxStance@IberLEF 2021: Overview of
the Task on Going Beyond Text in Cross-Lingual
Stance Detection. Procesamiento del Lenguaje Natu-
ral, 67:173–181.
Mehdi Ali, Michael Fromm, Klaudia Thellmann, Jan
Ebert, Alexander Arno Weber, Richard Rutmann,
Charvi Jain, Max Lübbering, Daniel Steinigen,
Johannes Leveling, Katrin Klug, Jasper Schulze
Buschhoff, Lena Jurkschat, Hammam Abdelwa-
hab, Benny Jörg Stein, Karl-Heinz Sylla, Pavel
Denisov, Nicolo’ Brandizzi, Qasid Saleem, Anirban
Bhowmick, Lennard Helmer, Chelsea John, Pedro Or-
tiz Suarez, Malte Ostendorff, Alex Jude, Lalith Man-
junath, Samuel Weinbach, Carolin Penke, Oleg Fila-
tov, Shima Asaadi, Fabio Barth, Rafet Sifa, Fabian
Küch, Andreas Herten, René Jäkel, Georg Rehm, Ste-
fan Kesselheim, Joachim Köhler, and Nicolas Flores-
Herr. 2024. Teuken-7b-base & teuken-7b-instruct:
Towards european llms. Preprint, arXiv:2410.03730.
Loubna Ben Allal,
Anton Lozhkov,
Elie Bak-
ouch, Gabriel Martín Blázquez, Guilherme Penedo,
Lewis Tunstall, Andrés Marafioti, Hynek Kydlíˇcek,
Agustín Piqueres Lajarín, Vaibhav Srivastav, Joshua
Lochner, Caleb Fahlgren, Xuan-Son Nguyen, Clé-
mentine Fourrier, Ben Burtenshaw, Hugo Larcher,
Haojun Zhao, Cyril Zakka, Mathieu Morlon, Colin
Raffel, Leandro von Werra, and Thomas Wolf.
2025.
Smollm2:
When smol goes big – data-
centric training of a small language model. Preprint,
arXiv:2502.02737.
Iñigo Alonso, Maite Oronoz, and Rodrigo Agerri. 2024.
MedExpQA: Multilingual Benchmarking of Large
Language Models for Medical Question Answering.
Artificial Intelligence in Medicine, 155:102938.
Jordi Armengol-Estapé, Casimiro Pio Carrino, Carlos
Rodriguez-Penagos, Ona de Gibert Bonet, Carme
Armentano-Oller, Aitor Gonzalez-Agirre, Maite
Melero, and Marta Villegas. 2021.
Are multilin-
gual models the best choice for moderately under-
resourced languages? A comprehensive assessment
for Catalan. In Findings of the Association for Com-
putational Linguistics: ACL-IJCNLP 2021, pages
4933–4946, Online. Association for Computational
Linguistics.
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama.
2020. On the cross-lingual transferability of mono-
lingual representations. In Proceedings of the 58th
Annual Meeting of the Association for Computational
Linguistics, pages 4623–4637, Online. Association
for Computational Linguistics.
Javier Aula-Blasco, Júlia Falcão, Susana Sotelo, Silvia
Paniagua, Aitor Gonzalez-Agirre, and Marta Villegas.
2025. VeritasQA: A truthfulness benchmark aimed
at multilingual transferability.
In Proceedings of
the 31st International Conference on Computational
Linguistics, pages 5463–5474, Abu Dhabi, UAE. As-
sociation for Computational Linguistics.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel
Artetxe, Satya Narayan Shukla, Donald Husa, Naman
Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and
Madian Khabsa. 2024. The belebele benchmark: a
parallel reading comprehension dataset in 122 lan-
guage variants. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 749–775,
Bangkok, Thailand. Association for Computational
Linguistics.
Fabio Barth, Manuel Brack, Maurice Kraus, Pedro Or-
tiz Suarez, Malte Ostendorf, Patrick Schramowski,
and Georg Rehm. 2024. Occiglot euro llm leader-
board.
Irene Baucells, Javier Aula-Blasco, Iria de Dios-Flores,
Silvia Paniagua Suárez, Naiara Perez, Anna Salles,
Susana Sotelo Docio, Júlia Falcão, Jose Javier Saiz,
Robiert Sepulveda Torres, Jeremy Barnes, Pablo
Gamallo, Aitor Gonzalez-Agirre, German Rigau, and
Marta Villegas. 2025. IberoBench: A benchmark for
LLM evaluation in Iberian languages. In Proceed-
ings of the 31st International Conference on Compu-
tational Linguistics, pages 10491–10519, Abu Dhabi,
UAE. Association for Computational Linguistics.
Nuria Bel, Marta Punsola, and Valle Ruíz-Fernández.
2024a. EsCoLA: Spanish corpus of linguistic ac-
ceptability.
In Proceedings of the 2024 Joint In-
ternational Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 6268–6277, Torino, Italia.
ELRA and ICCL.
Núria Bel, Marta Punsola, and Valle Ruiz-Fernández.
2024b. CatCoLA: Catalan corpus of linguistic ac-
ceptability. Procesamiento del Lenguaje Natural,
73.
Jaione Bengoetxea, Yi-Ling Chung, Marco Guerini,
and Rodrigo Agerri. 2024.
Basque and Spanish
Counter Narrative Generation: Data Creation and
Evaluation. In Joint International Conference on
Computational Linguistics, Language Resources and
Evaluation (LREC-COLING).
Stella Biderman, Hailey Schoelkopf, Quentin Anthony,
Herbie Bradley, Kyle O’Brien, Eric Hallahan, Mo-
hammad Aflah Khan, Shivanshu Purohit, USVSN Sai
Prashanth, Edward Raff, Aviya Skowron, Lintang
Sutawika, and Oskar van der Wal. 2023.
Pythia:
A suite for analyzing large language models across
training and scaling. Preprint, arXiv:2304.01373.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind

--- Page 13 ---

Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish,
Alec Radford, Ilya Sutskever, and Dario Amodei.
2020. Language models are few-shot learners. In
Proceedings of the 34th International Conference on
Neural Information Processing Systems, NIPS ’20,
Red Hook, NY, USA. Curran Associates Inc.
Lyle Campbell. 2010. Language isolates and their his-
tory, or, what’s weird, anyway? In Proceedings of
the Annual Meeting of the Berkeley Linguistics Soci-
ety, volume 36, pages 16–31. Linguistic Society of
America.
Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anasta-
sios Nikolas Angelopoulos, Tianle Li, Dacheng Li,
Hao Zhang, Banghua Zhu, Michael Jordan, Joseph E
Gonzalez, et al. 2024. Chatbot arena: An open plat-
form for evaluating llms by human preference. arXiv
preprint arXiv:2403.04132.
Luis Chiruzzo, Santiago Castro, Santiago Góngora,
Aiala Rosá, JA Meaney, and Rada Mihalcea. 2021.
Overview of haha at iberlef 2021: Detecting, rating
and analyzing humor in spanish. Procesamiento del
Lenguaje Natural, 67:257–268.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, Christopher Hesse, and John Schulman.
2021. Training verifiers to solve math word prob-
lems. Preprint, arXiv:2110.14168.
Javier Conde, Miguel González, Pedro Reviriego, Zhen
Gao, Shanshan Liu, and Fabrizio Lombardi. 2024.
Speed and conversational large language models: Not
all is about tokens per second. Computer, 57(8):74–
80.
OpenCompass Contributors. 2023.
Opencompass:
A universal evaluation platform for foundation
models.
https://github.com/open-compass/
opencompass.
Marta R. Costa-jussà, James Cross, Onur Çelebi,
Maha Elbayad, Kenneth Heafield, Kevin Heffer-
nan, Elahe Kalbassi, Janice Lam, Daniel Licht,
Jean Maillard, Anna Sun, Skyler Wang, Guillaume
Wenzek, Al Youngblood, Bapi Akula, Loic Bar-
rault, Gabriel Mejia Gonzalez, Prangthip Hansanti,
John Hoffman, Semarley Jarrett, Kaushik Ram
Sadagopan, Dirk Rowe, Shannon Spruit, Chau
Tran, Pierre Andrews, Necip Fazil Ayan, Shruti
Bhosale, Sergey Edunov, Angela Fan, Cynthia
Gao, Vedanuj Goswami, Francisco Guzmán, Philipp
Koehn, Alexandre Mourachko, Christophe Rop-
ers, Safiyyah Saleem, Holger Schwenk, and Jeff
Wang. 2022.
No language left behind:
Scal-
ing human-centered machine translation. Preprint,
arXiv:2207.04672.
Severino Da Dalt, Joan Llop, Irene Baucells, Marc
Pamies, Yishi Xu, Aitor Gonzalez-Agirre, and Marta
Villegas. 2024. FLOR: On the effectiveness of lan-
guage adaptation. In Proceedings of the 2024 Joint
International Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 7377–7388, Torino, Italia.
ELRA and ICCL.
John Dang, Shivalika Singh, Daniel D’souza, Arash
Ahmadian, Alejandro Salamanca, Madeline Smith,
Aidan Peppin, Sungjin Hong, Manoj Govindassamy,
Terrence Zhao, Sandra Kublik, Meor Amer, Viraat
Aryabumi, Jon Ander Campos, Yi-Chern Tan, Tom
Kocmi, Florian Strub, Nathan Grinsztajn, Yannis
Flet-Berliac, Acyr Locatelli, Hangyu Lin, Dwarak
Talupuru, Bharat Venkitesh, David Cairuz, Bowen
Yang, Tim Chung, Wei-Yin Ko, Sylvie Shang Shi,
Amir Shukayev, Sammie Bae, Aleksandra Piktus, Ro-
man Castagné, Felipe Cruz-Salinas, Eddie Kim, Lu-
cas Crawhall-Stein, Adrien Morisot, Sudip Roy, Phil
Blunsom, Ivan Zhang, Aidan Gomez, Nick Frosst,
Marzieh Fadaee, Beyza Ermis, Ahmet Üstün, and
Sara Hooker. 2024. Aya expanse: Combining re-
search breakthroughs for a new multilingual frontier.
Preprint, arXiv:2412.04261.
Iria de Dios-Flores, Juan Garcia Amboage, and Marcos
Garcia. 2023. Dependency resolution at the syntax-
semantics interface: psycholinguistic and computa-
tional insights on control dependencies. In Proceed-
ings of the 61st Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), pages 203–222, Toronto, Canada. Association
for Computational Linguistics.
DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang,
Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu,
Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang,
Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong
Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue,
Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu,
Chenggang Zhao, Chengqi Deng, Chenyu Zhang,
Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji,
Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo,
Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang,
Han Bao, Hanwei Xu, Haocheng Wang, Honghui
Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li,
Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang
Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L.
Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai
Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai
Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong
Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan
Zhang, Minghua Zhang, Minghui Tang, Meng Li,
Miaojun Wang, Mingming Li, Ning Tian, Panpan
Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen,
Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan,
Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen,
Shanghao Lu, Shangyan Zhou, Shanhuang Chen,
Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng
Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing
Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun,
T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu,

--- Page 14 ---

Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao
Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan
Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin
Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li,
Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin,
Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxi-
ang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang,
Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang
Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng
Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi,
Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang,
Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo,
Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yu-
jia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You,
Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu,
Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu,
Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan,
Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean
Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao,
Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zi-
jia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song,
Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu
Zhang, and Zhen Zhang. 2025. Deepseek-r1: Incen-
tivizing reasoning capability in llms via reinforce-
ment learning. Preprint, arXiv:2501.12948.
Abteen Ebrahimi, Manuel Mager, Arturo Oncevay,
Vishrav Chaudhary, Luis Chiruzzo, Angela Fan, John
Ortega, Ricardo Ramos, Annette Rios, Ivan Meza-
Ruiz, et al. 2021.
Americasnli: Evaluating zero-
shot natural language understanding of pretrained
multilingual models in truly low-resource languages.
arXiv preprint arXiv:2104.08726.
Ali Elfilali, Hamza Alobeidli, Clémentine Fourrier,
Basma El Amel Boussaha, Ruxandra Cojocaru,
Nathan Habib, and Hakim Hacid. 2024. Open ara-
bic llm leaderboard.
https://huggingface.co/
spaces/OALL/Open-Arabic-LLM-Leaderboard.
Julen Etxaniz, Oscar Sainz, Naiara Perez, Itziar Ald-
abe, German Rigau, Eneko Agirre, Aitor Ormazabal,
Mikel Artetxe, and Aitor Soroa. 2024. Latxa: An
open language model and evaluation suite for basque.
Preprint, arXiv:2403.20266.
Francisco Moreno Fernández and Héctor Álvarez Mella.
2024. Demografía del español en el mundo 2024.
In El español en el mundo. Anuario del Instituto
Cervantes 2024, pages 30–97. Instituto Cervantes.
Blanca Calvo Figueras, Eneko Sagarzazu, Julen Etx-
aniz, Jeremy Barnes, Pablo Gamallo, Iria De Dios
Flores, and Rodrigo Agerri. 2025. Truth Knows No
Language: Evaluating Truthfulness Beyond English.
In ACL.
Clémentine Fourrier, Nathan Habib, Hynek Kydlíˇcek,
Thomas Wolf, and Lewis Tunstall. 2023. Lighteval:
A lightweight framework for llm evaluation.
Clémentine Fourrier, Nathan Habib, Alina Lozovskaya,
Konrad Szafer, and Thomas Wolf. 2024.
Open
llm leaderboard v2.
https://huggingface.
co/spaces/open-llm-leaderboard/open_llm_
leaderboard.
Pablo Gamallo, Pablo Rodríguez, Iria de Dios-Flores,
Susana Sotelo, Silvia Paniagua, Daniel Bardanca,
José Ramom Pichel, and Marcos Garcia. 2024.
Open generative large language models for galician.
Preprint, arXiv:2406.13893.
Leo Gao, Jonathan Tow, Stella Biderman, Sid Black,
Anthony DiPofi, Charles Foster, Laurence Golding,
Jeffrey Hsu, Kyle McDonell, Niklas Muennighoff,
Jason Phang, Laria Reynolds, Eric Tang, Anish Thite,
Ben Wang, Kevin Wang, and Andy Zou. 2021. A
framework for few-shot language model evaluation.
Iker García-Ferrero and Begoña Altuna. 2024. Noticia:
A clickbait article summarization dataset in spanish.
Preprint, arXiv:2404.07611.
Timnit Gebru,
Jamie Morgenstern,
Briana Vec-
chione, Jennifer Wortman Vaughan, Hanna Wallach,
Hal Daumé Iii, and Kate Crawford. 2021. Datasheets
for datasets. Communications of the ACM, 64(12):86–
92.
Aitor Gonzalez-Agirre, Montserrat Marimon, Carlos
Rodriguez-Penagos, Javier Aula-Blasco, Irene Bau-
cells, Carme Armentano-Oller, Jorge Palomar-Giner,
Baybars Kulebi, and Marta Villegas. 2024. Build-
ing a data infrastructure for a mid-resource language:
The case of Catalan. In Proceedings of the 2024 Joint
International Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 2556–2566, Torino, Italia.
ELRA and ICCL.
María Grandury. 2024. The #somos600m project: Gen-
erating NLP resources that represent the diversity
of the languages from LATAM, the Caribbean, and
Spain. In North American Chapter of the Association
for Computational Linguistics Conference: LatinX in
AI (LXAI) Research Workshop.
Aaron Grattafiori et al. 2024. The llama 3 herd of mod-
els. Preprint, arXiv:2407.21783.
Zishan Guo, Renren Jin, Chuang Liu, Yufei Huang, Dan
Shi, Linhao Yu, Yan Liu, Jiaxuan Li, Bojian Xiong,
Deyi Xiong, et al. 2023. Evaluating large language
models: A comprehensive survey. arXiv preprint
arXiv:2310.19736.
Tahmid Hasan, Abhik Bhattacharjee, Md. Saiful Is-
lam, Kazi Mubasshir, Yuan-Fang Li, Yong-Bin Kang,
M. Sohel Rahman, and Rifat Shahriyar. 2021. XL-
sum: Large-scale multilingual abstractive summariza-
tion for 44 languages. In Findings of the Association
for Computational Linguistics: ACL-IJCNLP 2021,
pages 4693–4703, Online. Association for Computa-
tional Linguistics.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2021a. Measuring massive multitask language under-
standing. In International Conference on Learning
Representations.

--- Page 15 ---

Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and
Jacob Steinhardt. 2021b. Measuring mathematical
problem solving with the math dataset. Preprint,
arXiv:2103.03874.
Maite Heredia, Julen Etxaniz, Muitze Zulaika, Xabier
Saralegi, Jeremy Barnes, and Aitor Soroa. 2024. XN-
LIeu: a dataset for cross-lingual NLI in Basque. In
Proceedings of the 2024 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies
(Volume 1: Long Papers), pages 4177–4188, Mexico
City, Mexico. Association for Computational Lin-
guistics.
Carolin Holtermann, Paul Röttger, Timm Dill, and Anne
Lauscher. 2024. Evaluating the elementary multi-
lingual capabilities of large language models with
multiq. arXiv preprint arXiv:2403.03814.
Instituto de Ingeniería del Conocimiento. 2024a. Ab-
stractive Question-Answering in Spanish (AQuAS)
dataset.
Instituto de Ingeniería del Conocimiento. 2024b.
Retrieval-Augmented-Generation
and
Question-
Answering in Spanish (RagQuAS) Dataset.
Instituto de Ingeniería del Conocimiento. 2025.
Rigochat-7b-v2.
Krzysztof Jassem, Michał Ciesiółka, Filip Grali´nski,
Piotr Jabło´nski, Jakub Pokrywka, Marek Kubis,
Monika Jabło´nska, and Ryszard Staruch. 2025.
Llmzszł: a comprehensive llm benchmark for pol-
ish. Preprint, arXiv:2501.02266.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, Lélio Renard Lavaud,
Marie-Anne Lachaux, Pierre Stock, Teven Le Scao,
Thibaut Lavril, Thomas Wang, Timothée Lacroix,
and William El Sayed. 2023. Mistral 7b. Preprint,
arXiv:2310.06825.
Aisha Khatun and Daniel G. Brown. 2024. A study on
large language models’ limitations in multiple-choice
question answering. Preprint, arXiv:2401.07955.
Hyeonwoo Kim, Dahyun Kim, Jihoo Kim, Sukyung
Lee, Yungi Kim, and Chanjun Park. 2024. Open ko-
llm leaderboard2: Bridging foundational and prac-
tical evaluation for korean llms.
arXiv preprint
arXiv:2410.12445.
Javier De la Rosa, Eduardo G. Ponferrada, Manu
Romero,
Paulo
Villegas,
Pablo
González
de Prado Salas,
and María Grandury. 2022.
Bertin: Efficient pre-training of a spanish language
model using perplexity sampling. Procesamiento del
Lenguaje Natural, 68(0):13–23.
Latam-GPT. 2025. paes (revision 2e7fda0).
LenguajeNatural.AI. 2024a. HumorQA.
LenguajeNatural.AI. 2024b. MedicalExpertES.
LenguajeNatural.AI. 2024c. SpaLawEx.
Wangyue Li, Liangzhi Li, Tong Xiang, Xiao Liu, Wei
Deng, and Noa Garcia. 2024. Can multiple-choice
questions really be useful in detecting the abilities of
llms? Preprint, arXiv:2403.17752.
Yuanzhi Li, Sébastien Bubeck, Ronen Eldan, Allie
Del Giorno, Suriya Gunasekar, and Yin Tat Lee. 2023.
Textbooks are all you need ii: phi-1.5 technical re-
port. arXiv preprint arXiv:2309.05463.
Percy Liang, Rishi Bommasani, Tony Lee, Dimitris
Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian
Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Ku-
mar, Benjamin Newman, Binhang Yuan, Bobby Yan,
Ce Zhang, Christian Alexander Cosgrove, Christo-
pher D Manning, Christopher Re, Diana Acosta-
Navas, Drew Arad Hudson, Eric Zelikman, Esin
Durmus, Faisal Ladhak, Frieda Rong, Hongyu Ren,
Huaxiu Yao, Jue WANG, Keshav Santhanam, Laurel
Orr, Lucia Zheng, Mert Yuksekgonul, Mirac Suzgun,
Nathan Kim, Neel Guha, Niladri S. Chatterji, Omar
Khattab, Peter Henderson, Qian Huang, Ryan An-
drew Chi, Sang Michael Xie, Shibani Santurkar,
Surya Ganguli, Tatsunori Hashimoto, Thomas Icard,
Tianyi Zhang, Vishrav Chaudhary, William Wang,
Xuechen Li, Yifan Mai, Yuhui Zhang, and Yuta Ko-
reeda. 2023. Holistic evaluation of language models.
Transactions on Machine Learning Research. Fea-
tured Certification, Expert Certification.
Chin-Yew Lin. 2004. ROUGE: A package for auto-
matic evaluation of summaries. In Text Summariza-
tion Branches Out, pages 74–81, Barcelona, Spain.
Association for Computational Linguistics.
Xi Victoria Lin, Todor Mihaylov, Mikel Artetxe, Tianlu
Wang, Shuohui Chen, Daniel Simig, Myle Ott, Na-
man Goyal, Shruti Bhosale, Jingfei Du, Ramakanth
Pasunuru, Sam Shleifer, Punit Singh Koura, Vishrav
Chaudhary, Brian O’Horo, Jeff Wang, Luke Zettle-
moyer, Zornitsa Kozareva, Mona Diab, Veselin Stoy-
anov, and Xian Li. 2022. Few-shot learning with
multilingual generative language models. In Proceed-
ings of the 2022 Conference on Empirical Methods
in Natural Language Processing, pages 9019–9052,
Abu Dhabi, United Arab Emirates. Association for
Computational Linguistics.
Kadan Lottick, Silvia Susai, Sorelle A Friedler, and
Jonathan P Wilson. 2019. Energy usage reports: En-
vironmental awareness as part of algorithmic account-
ability. arXiv preprint arXiv:1911.08354.
Wolf Lustig. 1996.
Mba’éichapa oiko la guarani?
guaraní y jopara en el paraguay. URL: www. staff.
uni-mainz. de/lustig/guarani/art/yopara. pdf.–20 p.
Manuel Mager, Ximena Gutierrez-Vasques, Gerardo
Sierra, and Ivan Meza. 2018.
Challenges of lan-
guage technologies for the indigenous languages of
the americas. arXiv preprint arXiv:1806.04291.

--- Page 16 ---

Manuel Mager, Arturo Oncevay, Abteen Ebrahimi, John
Ortega, Annette Rios Gonzales, Angela Fan, Ximena
Gutierrez-Vasques, Luis Chiruzzo, Gustavo Giménez-
Lugo, Ricardo Ramos, et al. 2021. Findings of the
americasnlp 2021 shared task on open machine trans-
lation for indigenous languages of the americas. In
Proceedings of the First Workshop on Natural Lan-
guage Processing for Indigenous Languages of the
Americas, pages 202–217.
Pedro Henrique Martins, Patrick Fernandes, João Alves,
Nuno M. Guerreiro, Ricardo Rei, Duarte M. Alves,
José Pombal, Amin Farajian, Manuel Faysse, Ma-
teusz Klimaszewski, Pierre Colombo, Barry Haddow,
José G. C. de Souza, Alexandra Birch, and André
F. T. Martins. 2024. Eurollm: Multilingual language
models for europe. Preprint, arXiv:2409.16235.
Marina Mayor-Rocher, Nina Melero, Elena Merino-
Gómez, Miguel González, Raquel Ferrando, Javier
Conde, and Pedro Reviriego. 2025. Teleia: A spanish
language dataset for evaluating artificial intelligence
models. Data in Brief, page 111437.
Fabio Mercorio, Mario Mezzanzanica, Daniele Potertì,
Antonio Serino, and Andrea Seveso. 2024. Disce aut
deficere: Evaluating llms proficiency on the invalsi
italian benchmark. arXiv preprint arXiv:2406.17535.
Grégoire Mialon, Clémentine Fourrier, Craig Swift,
Thomas Wolf, Yann LeCun, and Thomas Scialom.
2023. Gaia: a benchmark for general ai assistants.
Preprint, arXiv:2311.12983.
Mario Mina, Valle Ruiz-Fernández, Júlia Falcão, Luis
Vasquez-Reina, and Aitor Gonzalez-Agirre. 2025.
Cognitive biases, task complexity, and result in-
tepretability in large language models. In Proceed-
ings of the 31st International Conference on Compu-
tational Linguistics, pages 1767–1784, Abu Dhabi,
UAE. Association for Computational Linguistics.
Junho Myung, Nayeon Lee, Yi Zhou, Jiho Jin,
Rifki Afina Putri, Dimosthenis Antypas, Hsuvas
Borkakoty, Eunsu Kim, Carla Perez-Almendros,
Abinew Ali Ayele, Víctor Gutiérrez-Basulto, Yazmín
Ibáñez-García, Hwaran Lee, Shamsuddeen Has-
san Muhammad, Kiwoong Park, Anar Sabuhi Rza-
yev, Nina White, Seid Muhie Yimam, Moham-
mad Taher Pilehvar, Nedjma Ousidhoum, Jose
Camacho-Collados, and Alice Oh. 2025.
Blend:
A benchmark for llms on everyday knowledge
in diverse cultures and languages.
Preprint,
arXiv:2406.09948.
Nikita Nangia, Clara Vania, Rasika Bhalerao, and
Samuel R. Bowman. 2020. CrowS-Pairs: A Chal-
lenge Dataset for Measuring Social Biases in Masked
Language Models. In Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language
Processing, Online. Association for Computational
Linguistics.
OpenAI. 2023.
Gpt-4 technical report.
Preprint,
arXiv:2303.08774.
Ankit
Pal,
Pasquale
Minervini,
Andreas
Geert
Motzfeldt, and Beatrice Alex. 2024.
openlife-
scienceai/open_medical_llm_leaderboard.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic evalu-
ation of machine translation. In Proceedings of the
40th Annual Meeting on Association for Computa-
tional Linguistics, ACL ’02, page 311–318, USA.
Association for Computational Linguistics.
Pouya Pezeshkpour and Estevam Hruschka. 2024.
Large language models sensitivity to the order of op-
tions in multiple-choice questions. In Findings of the
Association for Computational Linguistics: NAACL
2024, pages 2006–2017, Mexico City, Mexico. Asso-
ciation for Computational Linguistics.
Irene Plaza, Nina Melero, Cristina del Pozo, Javier
Conde, Pedro Reviriego, Marina Mayor-Rocher, and
María Grandury. 2024.
Spanish and llm bench-
marks: is mmlu lost in translation? arXiv preprint
arXiv:2406.17789.
Flor Miriam Plaza-del-Arco, Arturo Montejo-Ráez,
L. Alfonso Ureña-López, and María-Teresa Martín-
Valdivia. 2021. OffendES: A new corpus in Spanish
for offensive language research. In Proceedings of
the 12th Language Resources and Evaluation Con-
ference, pages 1096–1108, Held Online.
Flor Miriam Plaza-del-Arco, Carlo Strapparava, L. Al-
fonso Urena Lopez, and Maite Martin. 2020. Emo-
Event: A multilingual emotion corpus based on dif-
ferent events. In Proceedings of the Twelfth Lan-
guage Resources and Evaluation Conference, pages
1492–1498, Marseille, France. European Language
Resources Association.
Posadas-Durán, Helena Gómez-Adorno, Sidorov, and
Escobar. 2019. Detection of fake news in a new cor-
pus for the spanish language. Journal of Intelligent
& Fuzzy Systems, 36(5):4869–4876.
Amandine Quercia, Jamil Zaghir, Christian Lovis, and
Christophe Gaudet-Blavignac. 2024.
Medfrench-
mark, a small set for benchmarking generative llms
in medical french. In Digital Health and Informat-
ics Innovations for Sustainable Health Care Systems,
pages 601–605. IOS Press.
Qwen Team. 2024. Qwen2.5 technical report. arXiv
preprint arXiv:2412.15115.
Julian Risch, Timo Möller, Julian Gutsch, and Malte
Pietsch. 2021. Semantic answer similarity for evalu-
ating question answering models. In Proceedings of
the 3rd Workshop on Machine Reading for Question
Answering, pages 149–157, Punta Cana, Dominican
Republic. Association for Computational Linguistics.
Morgane Riviere, Shreya Pathak, Pier Giuseppe
Sessa, Cassidy Hardin, Surya Bhupatiraju, Léonard
Hussenot,
Thomas Mesnard,
Bobak Shahriari,
Alexandre Ramé, et al. 2024. Gemma 2: Improv-
ing open language models at a practical size. arXiv
e-prints, pages arXiv–2408.

--- Page 17 ---

Angelika Romanou, Negar Foroutan, Anna Sotnikova,
Zeming Chen, Sree Harsha Nelaturu, Shivalika
Singh, Rishabh Maheshwary, Micol Altomare, Mo-
hamed A Haggag, Alfonso Amayuelas, et al. 2024.
Include: Evaluating multilingual language under-
standing with regional knowledge. arXiv preprint
arXiv:2411.19799.
David Romero, Chenyang Lyu, Haryo Akbarianto Wi-
bowo, Teresa Lynn, Injy Hamed, Aditya Nanda
Kishore, Aishik Mandal, Alina Dragonetti, Artem
Abzaliev, Atnafu Lambebo Tonja, Bontu Fufa
Balcha, Chenxi Whitehouse, Christian Salamea,
Dan John Velasco, David Ifeoluwa Adelani, David Le
Meur, Emilio Villa-Cueva, Fajri Koto, Fauzan Fa-
rooqui, Frederico Belcavello, Ganzorig Batnasan,
Gisela Vallejo, Grainne Caulfield, Guido Ivetta,
Haiyue Song, Henok Biadglign Ademtew, Hernán
Maina, Holy Lovenia, Israel Abebe Azime, Jan
Christian Blaise Cruz, Jay Gala, Jiahui Geng,
Jesus-German Ortiz-Barajas, Jinheon Baek, Joce-
lyn Dunstan, Laura Alonso Alemany, Kumaran-
age Ravindu Yasas Nagasinghe, Luciana Benotti,
Luis Fernando D’Haro, Marcelo Viridiano, Mar-
cos Estecha-Garitagoitia, Maria Camila Buitrago
Cabrera, Mario Rodríguez-Cantelar, Mélanie Jouit-
teau, Mihail Mihaylov, Mohamed Fazli Mohamed
Imam, Muhammad Farid Adilazuarda, Munkhjargal
Gochoo, Munkh-Erdene Otgonbold, Naome Etori,
Olivier Niyomugisha, Paula Mónica Silva, Pranjal
Chitale, Raj Dabre, Rendi Chevi, Ruochen Zhang,
Ryandito Diandaru, Samuel Cahyawijaya, Santiago
Góngora, Soyeong Jeong, Sukannya Purkayastha,
Tatsuki Kuribayashi, Teresa Clifford, Thanmay
Jayakumar, Tiago Timponi Torrent, Toqeer Ehsan,
Vladimir Araujo, Yova Kementchedjhieva, Zara
Burzo, Zheng Wei Lim, Zheng Xin Yong, Oana Ig-
nat, Joan Nwatu, Rada Mihalcea, Thamar Solorio,
and Alham Fikri Aji. 2024. Cvqa: Culturally-diverse
multilingual visual question answering benchmark.
Preprint, arXiv:2406.05967.
Aiala Rosá, Luis Chiruzzo, Lucía Bouza, Alina Drag-
onetti, Santiago Castro, Mathias Etcheverry, Santi-
ago Góngora, Santiago Goycoechea, Juan Machado,
Guillermo Moncecchi, et al. 2022.
Overview of
quales at iberlef 2022: Question answering learning
from examples in spanish.
Oscar Sainz, Jon Campos, Iker García-Ferrero, Julen
Etxaniz, Oier Lopez de Lacalle, and Eneko Agirre.
2023. Nlp evaluation in trouble: On the need to
measure llm data contamination for each benchmark.
In Findings of the Association for Computational
Linguistics: EMNLP 2023, pages 10776–10787.
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavat-
ula, and Yejin Choi. 2019. Winogrande: An adver-
sarial winograd schema challenge at scale. Preprint,
arXiv:1907.10641.
Israfel Salazar, Manuel Fernández Burda, Shayekh Bin
Islam, Arshia Soltani Moakhar, Shivalika Singh,
Fabian Farestam,
Angelika Romanou,
Danylo
Boiko, Dipika Khullar, Mike Zhang, Dominik
Krzemi´nski, Jekaterina Novikova, Luísa Shimabu-
coro, Joseph Marvin Imperial, Rishabh Maheshwary,
Sharad Duwal, Alfonso Amayuelas, Swati Rajwal, Je-
bish Purbey, Ahmed Ruby, Nicholas Popoviˇc, Marek
Suppa, Azmine Toushik Wasi, Ram Mohan Rao
Kadiyala, Olga Tsymboi, Maksim Kostritsya, Bar-
dia Soltani Moakhar, Gabriel da Costa Merlin,
Otávio Ferracioli Coletti, Maral Jabbari Shiviari, Mo-
hammadAmin farahani fard, Silvia Fernandez, María
Grandury, Dmitry Abulkhanov, Drishti Sharma, An-
dre Guarnier De Mitri, Leticia Bossatto Marchezi,
Setayesh Heydari, Johan Obando-Ceron, Nazar Ko-
hut, Beyza Ermis, Desmond Elliott, Enzo Ferrante,
Sara Hooker, and Marzieh Fadaee. 2025. Kaleido-
scope: In-language exams for massively multilingual
vision evaluation. Preprint, arXiv:2504.07072.
Eva Sánchez Salido, Roser Morante, Julio Gonzalo,
Guillermo Marco, Jorge Carrillo de Albornoz, Laura
Plaza, Enrique Amigó, Andrés Fernández, Alejan-
dro Benito-Santos, Adrián Ghajari Espinosa, and
Victor Fresno. 2025. Bilingual evaluation of lan-
guage models on general knowledge in university en-
trance exams with minimal contamination. Preprint,
arXiv:2409.12746.
Elisa Sanchez-Bayona and Rodrigo Agerri. 2024.
Meta4XNLI: A Crosslingual Parallel Corpus for
Metaphor Detection and Interpretation.
Preprint,
arXiv:2404.07053.
Freda Shi, Mirac Suzgun, Markus Freitag, Xuezhi Wang,
Suraj Srivats, Soroush Vosoughi, Hyung Won Chung,
Yi Tay, Sebastian Ruder, Denny Zhou, Dipanjan Das,
and Jason Wei. 2023. Language models are multi-
lingual chain-of-thought reasoners. In The Eleventh
International Conference on Learning Representa-
tions.
Shivalika Singh, Angelika Romanou, Clémentine Four-
rier, David I. Adelani, Jian Gang Ngui, Daniel
Vila-Suero, Peerat Limkonchotiwat, Kelly Marchi-
sio, Wei Qi Leong, Yosephine Susanto, Raymond
Ng, Shayne Longpre, Wei-Yin Ko, Madeline Smith,
Antoine Bosselut, Alice Oh, Andre F. T. Martins,
Leshem Choshen, Daphne Ippolito, Enzo Ferrante,
Marzieh Fadaee, Beyza Ermis, and Sara Hooker.
2024. Global mmlu: Understanding and addressing
cultural and linguistic biases in multilingual evalua-
tion. Preprint, arXiv:2412.03304.
Aarohi Srivastava and et al. 2023.
Beyond the im-
itation game: Quantifying and extrapolating the
capabilities of language models.
arXiv preprint
arXiv:2206.04615.
Stephanie
Strassel
and
Jennifer
Tracey.
2016.
LORELEI language packs: Data, tools, and re-
sources for technology development in low resource
languages. In Proceedings of the Tenth International
Conference on Language Resources and Evaluation
(LREC‘16), pages 3273–3280, Portorož, Slovenia.
European Language Resources Association (ELRA).

--- Page 18 ---

Saeid Asgari Taghanaki, Aliasgahr Khani, and Amir
Khasahmadi. 2024. Mmlu-pro+: Evaluating higher-
order reasoning and shortcut learning in llms. arXiv
preprint arXiv:2409.02257.
Gorka Urbizu, Iñaki San Vicente, Xabier Saralegi, Ro-
drigo Agerri, and Aitor Soroa. 2022. BasqueGLUE:
A Natural Language Understanding Benchmark for
Basque. In Proceedings of the Thirteenth Language
Resources and Evaluation Conference, pages 1603–
1612.
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Aman-
preet Singh, Julian Michael, Felix Hill, Omer Levy,
and Samuel R. Bowman. 2019. SuperGLUE: A stick-
ier benchmark for general-purpose language under-
standing systems. arXiv preprint 1905.00537.
Xinpeng Wang, Bolei Ma, Chengzhi Hu, Leon Weber-
Genzel, Paul Röttger, Frauke Kreuter, Dirk Hovy, and
Barbara Plank. 2024a. “my answer is C”: First-token
probabilities do not match text answers in instruction-
tuned language models. In Findings of the Asso-
ciation for Computational Linguistics: ACL 2024,
pages 7407–7416, Bangkok, Thailand. Association
for Computational Linguistics.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni,
Abhranil Chandra, Shiguang Guo, Weiming Ren,
Aaran Arulraj, Xuan He, Ziyan Jiang, et al. 2024b.
Mmlu-pro: A more robust and challenging multi-task
language understanding benchmark. arXiv preprint
arXiv:2406.01574.
Yinfei Yang, Yuan Zhang, Chris Tar, and Jason
Baldridge. 2019. PAWS-X: A cross-lingual adversar-
ial dataset for paraphrase identification. In Proceed-
ings of the 2019 Conference on Empirical Methods
in Natural Language Processing and the 9th Inter-
national Joint Conference on Natural Language Pro-
cessing (EMNLP-IJCNLP), pages 3687–3692, Hong
Kong, China. Association for Computational Linguis-
tics.
Tony Z. Zhao, Eric Wallace, Shi Feng, Dan Klein,
and Sameer Singh. 2021. Calibrate before use: Im-
proving few-shot performance of language models.
Preprint, arXiv:2102.09690.
Elena Zotova, Rodrigo Agerri, and German Rigau. 2021.
Semi-automatic Generation of Multilingual Datasets
for Stance Detection in Twitter. Expert Systems with
Applications, 170:114547.
Irune Zubiaga, Aitor Soroa, and Rodrigo Agerri. 2024.
A LLM-based Ranking Method for the Evaluation of
Automatic Counter-Narrative Generation. In Find-
ings of the Association for Computational Linguistics:
EMNLP 2024, pages 9572–9585.

--- Page 19 ---

A
Evaluation Datasets
The datasets are used only for evaluation, aligning
with their intended uses.
Spanish datasets
The Spanish datasets in LA LEADERBOARD are:
AQuAS (Instituto de Ingeniería del Conocimiento,
2024a), Belebele (Bandarkar et al., 2024), Es-
CoLA (Bel et al., 2024a), Fake News ES (Posadas-
Durán et al., 2019), FLORES-200 (Costa-jussà
et al., 2022), ClinTreatES and ClinDiagnosES
(LenguajeNatural.AI, 2024b), HumorQA (Lengua-
jeNatural.AI, 2024a), MGSM (Shi et al., 2023),
MultiLingualCrowsPairs (Nangia et al., 2020),
NoticIA (García-Ferrero and Altuna, 2024), Of-
fendES (Plaza-del-Arco et al., 2021), RagQuAS
(Instituto de Ingeniería del Conocimiento, 2024b),
SpaLawEx (LenguajeNatural.AI, 2024c), TELEIA
(Mayor-Rocher et al., 2025), WNLI (Gonzalez-
Agirre et al., 2024; Baucells et al., 2025)17, XL-
Sum (Hasan et al., 2021), XStoryCloze (Lin et al.,
2022; Baucells et al., 2025), and XQuAD (Artetxe
et al., 2020).
Catalan datasets
The Catalan datasets in LA LEADERBOARD are:
caBREU, CatalanQA, COPA-ca, CoQCat, PAWS-
ca, TE-ca, WNLI-ca and XNLI-ca (Gonzalez-
Agirre et al., 2024), IberoBench (Baucells et al.,
2025), CatCoLA (Bel et al., 2024b), FLORES-
200 (Costa-jussà et al., 2022), MGSM (Shi et al.,
2023), XStoryCloze (Lin et al., 2022), XQuAD-ca
(Armengol-Estapé et al., 2021), XStoryCloze (Lin
et al., 2022; Baucells et al., 2025), Parafraseja18,
PAWS-X (Yang et al., 2019), and VeritasQA (Aula-
Blasco et al., 2025).
Basque datasets
The Basque datasets in LA LEADERBOARD are:
EusExams, EusReading, EusProficiency and Eu-
sTrivia from Etxaniz et al. (2024); BEC2016eu,
BHTCv2, EpecKorrefBin, QNLIeu, WiCeu from
BasqueGlue (Urbizu et al., 2022); QNLI-eu (Ur-
bizu et al., 2022), VaxxStance (Agerri et al., 2021),
XNLIeu (Heredia et al., 2024), FLORES-200
(Costa-jussà et al., 2022), MGSM (Shi et al., 2023),
and XStoryCloze (Lin et al., 2022; Baucells et al.,
2025).
17For
Spanish,
see
https://hf.co/datasets/
PlanTL-GOB-ES/wnli-es.
18https://hf.co/datasets/projecte-aina/
Parafraseja
Galician datasets
The Galician datasets in LA LEADERBOARD are:
FLORES-200 (Costa-jussà et al., 2022), GalCoLA
(de Dios-Flores et al., 2023), TruthfulQA-GL19,
and XStoryCloze (Lin et al., 2022; Baucells et al.,
2025)20.
Datasets created for La Leaderboard
The 7 datasets specifically created for the ini-
tial version of LA LEADERBOARD are AQuAS,
ClinDiagES, ClinTreatES, HumorQA, RagQuAS,
SpaLawEx, and TELEIA. Their corresponding
datasheets are included in Appendix F.
Newly donated datasets
The new datasets donated will be evaluated shortly.
These include CONAN-EUS (Bengoetxea et al.,
2024), RefutES21, TruthfulQA in Basque, Cata-
lan, Galician and Spanish (Figueras et al., 2025),
VeritasQA (Aula-Blasco et al., 2025), PAES Chile
(Latam-GPT, 2025), meta4xnli (Sanchez-Bayona
and Agerri, 2024), MedExpQA (Alonso et al.,
2024), Catalonia Independence Corpus (CIC) in
Catalan and Spanish (Zotova et al., 2021), HAHA
humor detection and analysis in Spanish (Chiruzzo
et al., 2021), QuALES for question-answering in
Spanish in the COVID-19 domain (Rosá et al.,
2022), AmericasNLP-MT (Mager et al., 2021),
AmericasNLI (Ebrahimi et al., 2021), Tradu-
LATAM, and VocesOriginarias evaluating indige-
nous languages.
Evaluation dataset details
The Tables 4 (Spanish), 5 (Catalan), 6 (Basque),
and 7 (Galician) list these datasets, providing
additional information about their task type,
domain, and origin.
We run the evaluations
using our fork of the LM Evaluation Harness22,
synced with the main repository on commit
6ccd520f3fb2b5d74c6f14c05f9d189521424719.
The tables mentioned also include details about the
evaluation configuration, providing the Harness
task ID, metric, and number of shots.
19https://hf.co/datasets/proxectonos/
truthfulqa_gl
20For
Galician,
see
https://hf.co/datasets/
proxectonos/xstorycloze_gl.
21https://hf.co/datasets/SINAI/RefutES
22https://github.com/somosnlp/
lm-evaluation-harness

--- Page 20 ---

Dataset
Task
Metric
Domain
Origin
#Examples
#Shots
AQuAS
Abstractive QA, Long Form QA
sas_encoder
Miscellaneous
Original
87
1
Belebele Spa
Reading Comprehension
acc
Miscellaneous
Human translation
900
2
ClinDiagnosES
Long Form QA
sas_encoder
Clinical
Original
62
0
ClinTreatES
Long Form QA
sas_encoder
Clinical
Original
62
0
COPA_es
Commonsense Reasoning
acc
Lang. prof., Misc.
Human translation
500
3
Crows Pairs Spanish
Stereotype Detection
pct_stereotype
Ethics, Hate speech
Original
1509
0
EsCoLA
Linguistic Acceptability
mcc
Language proficiency
Original
1060
2
Fake News ES
Fake News Detection
acc
Press
Original
572
2
HumorQA
Humor Classification
acc
Language proficiency
Original
51
0
MGSM_es
Math Reasoning
exact_match
Math
Human translation
250
2
NoticIA
Summarization
rouge1
Lang. prof., Press
Original
100
0
OffendES
Hate Speech Detection
acc
Hate speech
Original
13600
2
OpenBookQA_es
Multiple Choice QA
acc
General knowledge
Human translation
500
0
PAWS-X_es
Paraphrasing
acc
Lang. prof., Misc.
Original
2000
3
RagQuAS
Abstractive QA, Long Form QA
sas_encoder
Miscellaneous
Original
201
1
SpaLawEx
Multiple Choice QA
acc
Legal
Original
119
0
TELEIA
Multiple Choice QA
acc
Gen. knowl., Lang. prof.
Original
100
2
WNLI ES
Natural Language Inference
acc
Lang. prof., Misc.
Human translation
146
2
XL-Sum_es
Summarization
bleu
Press
Original
4763
1
XNLI_es
Natural Language Inference
acc
Miscellaneous
Original
5010
3
XQuAD_es
Extractive QA
f1
Miscellaneous
Original
1190
2
xStoryCloze_es
Commonsense Reasoning
acc
Miscellaneous
Human translation
1510
0
Table 4: Details of the evaluation datasets in Spanish (ES).
Dataset
Task
Metric
Domain
Origin
#Examples
#Shots
ARC_ca
Multiple Choice QA
acc
Science
Human translation
869
2
Belebele Cat
Reading Comprehension
acc
Miscellaneous
Human translation
900
2
caBREU
Summarization
bleu
Press
Original
301
1
CatalanQA
Extractive QA
f1
Miscellaneous
Original
2135
2
CatCoLA
Linguistic Acceptability
mcc
Language proficiency
Original
1020
2
COPA_ca
Commonsense Reasoning
acc
Lang. prof., Misc.
Human translation
500
3
CoQCat
Extractive QA
f1
Miscellaneous
Original
8986
1
MGSM_ca
Math Reasoning
exact_match
Math
Human translation
250
2
OpenBookQA_ca
Multiple Choice QA
acc
General knowledge
Human translation
500
0
Parafraseja
Paraphrasing
acc
Language proficiency
Original
21984
3
PAWS_ca
Paraphrasing
acc
Lang. prof., Misc.
Human translation
2000
3
PIQA_ca
Multiple Choice QA
acc
General knowledge
Human translation
1838
2
SIQA_ca
Multiple Choice QA
acc
General knowledge
Human translation
1954
2
TE-ca
Natural Language Inference
acc
Lang. prof., Misc.
Original
2117
3
WNLI_ca
Natural Language Inference
acc
Lang. prof., Misc.
Human translation
146
2
XNLI_ca
Natural Language Inference
acc
Lang. prof., Misc.
Human translation
5010
3
XQuAD_ca
Extractive QA
f1
Miscellaneous
Human translation
1190
2
xStoryCloze_ca
Commonsense Reasoning
acc
Miscellaneous
Human translation
1510
0
Table 5: Details of the evaluation datasets in Catalan (CA).
Dataset
Task
Metric
Domain
Origin
#Examples
#Shots
BEC2016eu
Sentiment Analysis
f1
Politics, Twitter
Original
1302
3
Belebele Eus
Reading Comprehension
acc
Miscellaneous
Human translation
900
2
BertaQA
Multiple Choice QA
acc
Cultural Knowledge
Original
4760
3
BHTCv2
Topic Classification
f1
Press
Original
1854
2
EpecKorrefBin
Natural Language Inference
acc
Press
Original
587
3
EusExams
Multiple Choice QA
acc
Miscellaneous
Original
16000
4
EusProficiency
Multiple Choice QA
acc
Language proficiency
Original
5169
4
EusReading
Reading Comprehension
acc
Miscellaneous
Original
352
1
EusTrivia
Multiple Choice QA
acc
General knowledge
Original
1715
4
MGSM_eu
Math Reasoning
exact_match
Math
Human translation
250
2
QNLIeu
Natural Language Inference
acc
Miscellaneous
Original
238
2
VaxxStance
Stance Detection
f1
Politics, Twitter
Original
312
3
WiCeu
Natural Language Inference
acc
Language proficiency
Original
1400
2
WNLI_eu
Natural Language Inference
acc
Lang. prof., Misc.
Human translation
146
2
XCOPA_eu
Commonsense Reasoning
acc
Lang. prof., Misc.
Human translation
500
3
XNLI_eu
Natural Language Inference
acc
Lang. prof., Misc.
Reviewed MT
5010
3
xStoryCloze_eu
Commonsense Reasoning
acc
Miscellaneous
Human translation
1510
0
Table 6: Details for evaluation datasets in Basque (EU).
Dataset
Task
Metric
Domain
Origin
#Examples
#Shots
Belebele Glg
Reading Comprehension
acc
Miscellaneous
Reviewed MT
900
2
GalCoLA
Linguistic Acceptability
mcc
Language proficiency
Original
1710
2
MGSM_gl
Math Reasoning
exact_match
Math
Reviewed MT
250
2
OpenBookQA_gl
Multiple Choice QA
acc
General knowledge
Reviewed MT
500
0
ParafrasesGL
Paraphrasing
acc
Language proficiency
Original
294
3
PAWS_gl
Paraphrasing
acc
Lang. prof., Misc.
Reviewed MT
2000
3
SummarizationGL
Summarization
bleu
Press
Original
8080
1
XNLI_gl
Natural Language Inference
acc
Lang. prof., Misc.
Reviewed MT
5010
3
xStoryCloze_gl
Commonsense Reasoning
acc
Miscellaneous
Human translation
1510
0
Table 7: Details for evaluation datasets in Galician (GL).

--- Page 21 ---

B
Frontend Detailed Description
The implementation of LA LEADERBOARD is
based on the HuggingFace leaderboard template.
23 The frontend is developed using Gradio (Abid
et al., 2019) and divided into four tabs:
• The landing tab, named "La Leaderboard",
is divided into five sub-tabs, each containing
tables with all the evaluated models and their
corresponding average results. These sub-tabs
include overall and language-specific results
for Spanish, Catalan, Basque, and Galician.
The results are aggregated by averaging the
scores across all tasks for each language.
• For transparency and reproducibility purposes,
the second tab, "Info", includes the command
we use to evaluate the models and also the nor-
malization formula. In the acknowledgements
section, we list the institutions and every per-
son who contributed to the project.
• The next tab describes all the "Tasks" included
in LA LEADERBOARD .
• Finally, there is a tab where everyone can sub-
mit their model for evaluation.
The text of the information and submission tabs
is available both in English and Spanish to bring
the tool closer to the community.
In the footer, we can find the citation informa-
tion for the software, all the included datasets, and
the evaluation suite. Below are the fourteen logos
from all the collaborating institutions. The entities
in the acknowledgements are ordered chronologi-
cally by the date they joined the project to thank
early adopters, whereas the logos in the footer are
ordered by the number of datasets donated.
C
Models Evaluated
Table 8 details the 50 models evaluated, includ-
ing the following families: Aitana24, BERTIN
(la Rosa et al., 2022), Carballo (Gamallo et al.,
2024), Gromenauer25, FLOR (Da Dalt et al., 2024),
LeniaChat26, RigoChat (Instituto de Ingeniería del
23https://hf.co/spaces/
demo-leaderboard-backend/leaderboard
24https://hf.co/gplsi/Aitana-6.3B
25https://hf.co/bertin-project
26https://hf.co/LenguajeNaturalAI/
leniachat-gemma-2b-v0
Conocimiento, 2025), Salamandra27, Occiglot28,
EuroLLM (Martins et al., 2024), Aya (Dang et al.,
2024), DeepSeek (DeepSeek-AI et al., 2025),
Gemma (Riviere et al., 2024), Llama (Grattafiori
et al., 2024), Mistral (Jiang et al., 2023), Phi (Li
et al., 2023), SmolLM (Allal et al., 2025), and
Qwen (Qwen Team, 2024).
D
Evaluation Results
This section detailed visualizations of the evalu-
ation results, comparing models, languages, and
tasks, considering metrics such as performance and
energy efficiency.
Figure 3 presents the full list of average results
of the models evaluated, overall and by language.
Moreover, since a very bad or good score in a few
tasks can lower or raise the average score for a
model and distort the comparison, we show the
results in terms of the number of tasks for which a
model is in the top 10 in Figure 4. This provides
an alternative view of the results, focusing on the
number of tasks for which the performance of the
model is good. Figure 5 provides a comprehensive
view of all the evaluation results by language, size,
and model type.
Figure 6 represents the total energy consumed
by each model. On average, each model consumed
9.25 kWh (median = 6.88, SD = 8.42), showing a
wide variety in energy usage. Figure 7 shows which
tasks consume more energy, with the text genera-
tion tasks on the top of the list. Figure 8 presents
a comparison between model size and energy con-
sumption. Finally, Figure 9 shows the relation be-
tween performance and energy consumption.
27https://hf.co/collections/BSC-LT/
salamandra-66fc171485944df79469043a
28https://hf.co/collections/occiglot/
occiglot-eu5-7b-v01-65dbed502a6348b052695e01

--- Page 22 ---

Family
Model ID
Model Type
Size (B)
Aitana
gplsi/Aitana-6.3B
pretrained
6.25
BERTIN
bertin-project/bertin-gpt-j-6B
pretrained
6.06
BERTIN
bertin-project/Gromenauer-7B
pretrained
7.24
BERTIN
bertin-project/Gromenauer-7B-Instruct
instruction-tuned
7.24
Carballo
proxectonos/Carballo-bloom-1.3B
pretrained
1.31
FLOR
projecte-aina/FLOR-1.3B
pretrained
1.31
FLOR
projecte-aina/FLOR-1.3B-Instructed
instruction-tuned
1.31
FLOR
projecte-aina/FLOR-6.3B
pretrained
6.25
FLOR
projecte-aina/FLOR-6.3B-Instructed
instruction-tuned
6.25
Latxa
HiTZ/latxa-7b-v1.2
pretrained
7.00
LeniaChat
LenguajeNaturalAI/leniachat-gemma-2b-v0
instruction-tuned
2.51
LeniaChat
LenguajeNaturalAI/leniachat-qwen2-1.5B-v0
instruction-tuned
1.54
RigoChat
IIC/RigoChat-7b-v2
instruction-tuned
7.62
Salamandra
BSC-LT/salamandra-2b
pretrained
2.25
Salamandra
BSC-LT/salamandra-2b-instruct
instruction-tuned
2.25
Salamandra
BSC-LT/salamandra-7b
pretrained
7.77
Salamandra
BSC-LT/salamandra-7b-instruct
instruction-tuned
7.77
EuroLLM
utter-project/EuroLLM-1.7B
pretrained
1.70
EuroLLM
utter-project/EuroLLM-1.7B-Instruct
instruction-tuned
1.70
EuroLLM
utter-project/EuroLLM-9B
pretrained
9.15
EuroLLM
utter-project/EuroLLM-9B-Instruct
instruction-tuned
9.15
Occiglot
occiglot/occiglot-7b-es-en
pretrained
7.24
Occiglot
occiglot/occiglot-7b-es-en-instruct
instruction-tuned
7.24
Occiglot
occiglot/occiglot-7b-eu5
pretrained
7.24
Occiglot
occiglot/occiglot-7b-eu5-instruct
instruction-tuned
7.24
Aya
CohereForAI/aya-expanse-8b
pretrained
8.03
DeepSeek
deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
instruction-tuned
1.78
DeepSeek
deepseek-ai/DeepSeek-R1-Distill-Qwen-7B
instruction-tuned
7.62
DeepSeek
unsloth/DeepSeek-R1-Distill-Qwen-14B-bnb-4bit
instruction-tuned
14.8 (8.37)
Gemma
google/gemma-2-2b
pretrained
2.61
Gemma
google/gemma-2-2b-it
instruction-tuned
2.61
Gemma
google/gemma-2-9b
pretrained
9.24
Gemma
google/gemma-2-9b-it
instruction-tuned
9.24
Llama
meta-llama/Llama-3.2-1B
pretrained
1.24
Llama
meta-llama/Llama-3.2-1B-Instruct
instruction-tuned
1.24
Llama
meta-llama/Meta-Llama-3.1-8B
pretrained
8.03
Llama
meta-llama/Meta-Llama-3.1-8B-Instruct
instruction-tuned
8.03
Mistral
mistralai/Mistral-7B-Instruct-v0.3
instruction-tuned
7.25
Mistral
mistralai/Mistral-7B-v0.3
pretrained
7.25
Phi
microsoft/phi-1_5
pretrained
1.42
SmolLM
HuggingFaceTB/SmolLM2-1.7B
pretrained
1.71
SmolLM
HuggingFaceTB/SmolLM2-1.7B-Instruct
instruction-tuned
1.71
Qwen
Qwen/Qwen2.5-1.5B
pretrained
1.54
Qwen
Qwen/Qwen2.5-1.5B-Instruct
instruction-tuned
1.54
Qwen
Qwen/Qwen2.5-7B
pretrained
7.62
Qwen
Qwen/Qwen2.5-7B-Instruct
instruction-tuned
7.62
Qwen
Qwen/Qwen2.5-14B-Instruct-GPTQ-Int8
instruction-tuned
14.80 (4.99)
Qwen
Qwen/Qwen2.5-32B-Instruct-GPTQ-Int4
instruction-tuned
32.80 (5.74)
Table 8: Models evaluated in LA LEADERBOARD as of February 2025. The table is divided into sections starting
at the top with models optimized for the languages of Spain, followed by models created by European projects,
and finally models trained by international large technological companies and startups. The size is specified in
billions of parameters, as appears in the SafeTensors information of the corresponding Hugging Face model page.
For quantized models, the SafeTensors equivalent size of the model is added in parenthesis after the size of the base
model.

--- Page 23 ---

Model Name
Training
Tokens (B)
Languages
Included
Tokens (B)
per Language
Hardware
Training
Time (h)
Aitana-6.3B
2.6
CA
2.6
4 A100
80
bertin-gpt-j-6B
65
ES
65
1 v3-8
4320
Gromenauer-7B
14.5
ES
14.5
-
-
Gromenauer-7B-Instruct
14.5+
ES, CA
14.5+, -
-
-
Carballo-bloom-1.3B
2.1
GL
2.1
5 A100
-
FLOR-1.3B
26
ES, CA
10.8, 10.9
Cerebras CS-2
-
FLOR-1.3B-Instructed
26+
ES, CA
10.8, 10.9+
Cerebras CS-2
-
FLOR-6.3B
140
ES, CA
46.7, 46.8
16 Cereb. CS-2
60
FLOR-6.3B-Instructed
140+
ES, CA
46.7, 46.8+
16 Cereb. CS-2
60+
latxa-7b-v1.2
4.2
EU
4.2
4 A100
953
leniachat-gemma-2b-v0
-
ES
-
-
-
leniachat-qwen2-1.5B-v0
-
ES
-
-
-
RigoChat-7b-v2
-
ES
-
1 A100
8.5
salamandra-2b
12875000
ES, CA, GL, EU
2075k, 253k, 39k, 30k
256 Hopper
221k
salamandra-2b-instruct
12875000+
ES, CA, GL, EU
2075k, 253k, 39k, 30k+
256 Hopper
221k+12
salamandra-7b
12875000
ES, CA, GL, EU
2075k, 253k, 39k, 30k
512 Hopper
602k
salamandra-7b-instruct
12875000+
ES, CA, GL, EU
2075k, 253k, 39k, 30k+
512 Hopper
602k+16
EuroLLM-1.7B
4000
ES, CA, GL
240, 12, 4
256 H100
-
EuroLLM-1.7B-Instruct
4000+
ES, CA
240, 12, 4+
256 H100
-
EuroLLM-9B
4000
ES, CA, GL
240, 12, 4
400 H100
-
EuroLLM-9B-Instruct
4000+
ES, CA
240, 12, 4+
400 H100
-
occiglot-7b-es-en
112
ES
58.2
128 A100
-
occiglot-7b-es-en-instruct
112+0.16
ES
58.2+0.08
+8 H100
-
occiglot-7b-eu5
293
ES
58.6
128 A100
-
occiglot-7b-eu5-instruct
293+0.40
ES
58.6+0.08
+8 H100
-
aya-expanse-8b
-
ES
-
-
-
DeepSeek-R1-Dist-Qwen-1.5B
-
-
-
-
-
DeepSeek-R1-Dist-Qwen-7B
-
-
-
-
-
DeepSeek-R1-Dist-Qwen-14B-4bit
-
-
-
-
-
gemma-2-2b
2000
-
-
v5p
-
gemma-2-2b-it
2000+
-
-
v5p
-
gemma-2-9b
8000
-
-
v5p
-
gemma-2-9b-it
8000+
-
-
v5p
-
Llama-3.2-1B
9000
ES
-
H100
370k
Llama-3.2-1B-Instruct
9000+
ES
-
H100
370k+
Llama-3.1-8B
15000
ES
-
H100
1460k
Llama-3.1-8B-Instruct
15000+
ES
-
H100
1460k+
Mistral-7B-v0.3
-
-
-
-
-
Mistral-7B-Instruct-v0.3
-
-
-
-
-
phi-1_5
150
none
0
32 A100
192
SmolLM2-1.7B
11000
none
0
256 H100
-
SmolLM2-1.7B-Instruct
11000+
none
0
256 H100
-
Qwen2.5-1.5B
18000
ES
-
-
-
Qwen2.5-1.5B-Instruct
18000
ES
-
-
-
Qwen2.5-7B
18000
ES
-
-
-
Qwen2.5-7B-Instruct
18000
ES
-
-
-
Qwen2.5-14B-Instruct-GPTQ-Int8
18000
ES
-
-
-
Qwen2.5-32B-Instruct-GPTQ-Int4
18000
ES
-
-
-
Table 9:
Public details about the training corpus and compute resources of the models evaluated on
LA LEADERBOARD : total number of tokens in the training data, target languages included in the training data,
number of tokens per language, hardware type, and hours of training time.

--- Page 24 ---

Figure 3: Average results of the first set of models evaluated on LA LEADERBOARD , overall and by language.

--- Page 25 ---

Figure 4: Number of tasks in which a model is among the top 10 models, by language.

--- Page 26 ---

Figure 5: Results of the first set of models evaluated on LA LEADERBOARD organized by language, size, and model
type.

--- Page 27 ---

Figure 6: Distribution of results of models evaluated
on LA LEADERBOARD organized by total energy
consumption.
Figure 7: Energy consumption for the tasks evalu-
ated on LA LEADERBOARD . The top three tasks
(summarization_gl, xlsum_es, and cabreu) corre-
spond to text summarization tasks, which require
the generation of many tokens. The next tasks corre-
spond to QA tasks with thousands of questions.

--- Page 28 ---

Figure 8: Distribution of results of models evaluated on LA LEADERBOARD comparing energy consumption versus
size. The plot shows some correlation between model size and energy consumed, with a Pearson correlation
coefficient of 0.43.
Figure 9: Distribution of results of models evaluated on LA LEADERBOARD comparing energy consumption versus
performance. The plot shows a high correlation between model performance and energy consumed, with a Pearson
correlation coefficient of 0.50.

--- Page 29 ---

E
Data Collection Campaign
Below are the questions, translated into English,
corresponding to the Google Form used in the open
data collection campaign. The asterisk (*) marks
mandatory fields.
1. Email *
2. Data source (Select one option) *
(a) The dataset is public
(b) Instructions to recreate it are available
(c) The dataset is private but access can be requested
on a website
(d) The dataset is currently private, but we want to
open it as a donation
(e) The dataset is private, but you should try contact-
ing the organization that created it
3. Dataset link * This can be the dataset link, the instruc-
tions to recreate it, or the corresponding organization’s
website if private.
4. If your dataset is not uploaded to Hugging Face, would
you like us to take care of uploading it? (Select one
option)
(a) Yes, upload it to the SomosNLP organization
(b) Yes, help me create my own organization and
upload it
(c) No, I prefer to create my own organization and
upload it myself
5. Modality * (Select one option)
(a) Text
(b) Audio
(c) Image (e.g., images with descriptions)
6. Language(s) * (Select all that apply)
(a) Spanish
(b) Other: _____
7. Country(ies) * Country(ies) of origin of the data and/or
the people who annotated it. A region can also be speci-
fied if known. The more information, the better.
8. Tasks * (Select all that apply)
(a) Language modeling (unannotated)
(b) Question answering (QA)
(c) Classification
(d) Token classification (e.g., NER, PoS)
(e) Translation
(f) Summarization
(g) Semantic similarity
(h) Multimodal (e.g., text-to-image, audio-to-text)
9. Subtask For example, subtasks of "text classification"
could be "sentiment analysis" or "hate speech detec-
tion."
10. Domain * (Select all that apply)
(a) Legal
(b) Clinical or biomedical
(c) Academic or technical
(d) Literature or music
(e) Social media or forums
(f) News or articles
(g) Dialogues
(h) General
11. Number of examples Enter the exact number of exam-
ples if known, otherwise provide a range.
12. License type *
(a) Commercial
(b) Non-commercial
13. License link
14. Link to the dataset documentation or any other rele-
vant information: description, annotation and cleaning
process, ethical considerations... *
15. Link to the script/repository on GitHub to download or
process the dataset
16. Thank you very much for your contribution! To publicly
acknowledge your contribution, you may share your
name and/or affiliation to be displayed on the website.
If this is a donation, we will contact you soon—thank
you!
17. Name
18. Affiliation
19. How could we improve this campaign? Who would you
recommend we contact? Anything else you would like
to tell us?

--- Page 30 ---

F
Datasheets
We present the datasheets (Gebru et al., 2021)
corresponding to each of the datasets specifically
created for LA LEADERBOARD : AQuAS, Clin-
DiagnosES, ClinTreatES, HumorQA, RagQuAS,
SpaLawEx, TELEIA. Moreover, we propose
an adaptation for leaderboards and fill it for
LA LEADERBOARD .
La Leaderboard
Motivation for Leaderboard Creation
Why
was
the
leaderboard
created?
LA LEADERBOARD is
the
first
open-source
leaderboard to evaluate generative LLMs in
languages of Spain and Latin America.
By
aiming to address the linguistic and cultural
diversity of the Spanish-speaking community,
LA LEADERBOARD aims to set a new standard
for multilingual LLM evaluation. Our goal is to
encourage the development of models that are not
only linguistically competent but also culturally
aware, ultimately driving progress in Natural
Language Processing (NLP) for the benefit of our
whole community.
Who funded the creation of the leaderboard?
LA LEADERBOARD is an initiative launched by
an international open-source community and
was promoted by volunteers.
The funding
of each of the individual datasets donated to
LA LEADERBOARD will be disclosed after review.
Leaderboard Composition
What
are
the
instances?
LA LEADERBOARD consists
of
66
evalua-
tion datasets. All the evaluation datasets in the
leaderboard consist solely of text instances.
Are relationships between instances made ex-
plicit in the data
There are no known relation-
ships between instances.
How many instances of each type are there?
Summing all the instances of the 66 evaluation
datasets, the leaderboard consists of 149,782 exam-
ples.
Is everything included or does the data rely on
external resources?
Everything is included in
the datasets.
Are
there
recommended
data
splits
or
evaluation
measures?
The
splits
used
in
LA LEADERBOARD are the corresponding test
splits of each dataset.
Data Collection Process
How was the data collected?
The datasets were
collected through an open data collection cam-
paign.
Who was involved in the data collection process?
How were they compensated?
Professional re-
searchers from academia and industry. The logo
and names of the donators are included in the user
interface, and the creators of the datasets are ac-
knowledged in the paper.
Over what time-frame was the data collected?
During 2024.
Does the dataset contain all possible instances?
The evaluations are launched including all the avail-
able test instances for each donated dataset.
If the dataset is a sample, then what is the popu-
lation?
Not applicable.
Is there information missing from the dataset
and why?
No
Are there any known errors, sources of noise, or
redundancies in the data?
No.
Leaderboard Distribution
How is the leaderboard distributed?
The
leaderboard is available in the HuggingFace hub29.
When will the leaderboard be released/first
distributed?
The leaderboard was released in
September 2024.
What license (if any) is it distributed under?
The leaderboard is licensed under "Apache 2.0".
Are there any fees or access/export restrictions?
There are no fees or restrictions.
Leaderboard Maintenance
Who is supporting/hosting/maintaining the
leaderboard?
The leaderboard is hosted at Hug-
gingFace30, and the community can be contacted
29https://hf.co/spaces/la-leaderboard/
la-leaderboard
30https://hf.co/spaces/la-leaderboard/
la-leaderboard

--- Page 31 ---

through the "Discussions" tab in the interface or
via email31.
Will the leaderboard be updated? How often
and by whom?
Yes, every time there is a new do-
nation, the maintainer will update the leaderboard
and communicate the update on the usual commu-
nication channels of the open-source community.
Is there a repository to link to any/all pa-
pers/systems
that
use
this
leaderboard?
Yes,
all
the
datasets
and
tools
used
by
LA LEADERBOARD are
referenced
in
the
"Citation" section of the interface32.
Legal & Ethical Considerations
If the dataset relates to people or was generated
by people, were they informed about the data
collection?
Not applicable.
If it relates to other ethically protected subjects,
have appropriate obligations been met?
Not
applicable.
If it relates to people, were there any ethical
review applications/reviews/approvals?
Not
applicable.
If it relates to people, were they told what the
dataset would be used for and did they consent?
Not applicable.
If it relates to people, could this dataset expose
people to harm or legal action?
Not applicable.
If it relates to people, does it unfairly advantage
or disadvantage a particular social group?
Not
applicable.
If it relates to people, were they provided with
privacy guarantees?
Not applicable.
Does the dataset comply with the EU General
Data Protection Regulation (GDPR)?
Yes, it
complies with GDPR.
Does the dataset contain information that might
be considered sensitive or confidential?
No.
Does the dataset contain information that might
be considered inappropriate or offensive?
No.
31maria.grandury@somosnlp.org
32https://hf.co/spaces/la-leaderboard/
la-leaderboard
AQuAS
The Abstractive Question-Answering in Span-
ish (AQuAS) dataset (Instituto de Ingeniería del
Conocimiento, 2024a), developed by Instituto de
Ingeniería del Conocimiento, is a monolingual
Spanish dataset designed for abstractive question-
answering. It contains 107 examples covering a
diverse range of topics, including finance, insur-
ance, healthcare, music, and law. Each example
consists of a context passage, a related question,
and a human-crafted answer. The dataset is aimed
at evaluating the ability of large language models
(LLMs) to generate well-formed, coherent, and in-
formative responses.
Motivation for Dataset Creation
Why was the dataset created?
AQuAS was cre-
ated to provide high-quality examples of pairs of
questions and answers with a related context that
can be used to evaluate the ability of large language
models (LLMs) to generate well-formed, coherent,
and informative responses (abstractive question an-
swering).
What (other) tasks could the dataset be used
for?
There are no recommended uses for this
dataset other than evaluation.
Who funded the creation of the dataset?
If
there is an associated grant, provide the grant num-
ber. The dataset was created and funded by the
research institute.
Dataset Composition
What are the instances?
Each instance is a pair
of a question and an answer accompanied by the
related context on which the answer has been based
and the corresponding topic.
Are relationships between instances made ex-
plicit in the data
There are no known relation-
ships between instances.
How many instances of each type are there?
The dataset consists of 107 examples.
What data does each instance consist of?
The
instances consist of text data and are labelled with
the corresponding topic.
Is everything included or does the data rely on
external resources?
Everything is included in
the dataset.

--- Page 32 ---

Are there recommended data splits or evalua-
tion measures?
Since the dataset is intended for
testing, there is no recommended split.
Data Collection Process
How was the data collected?
The data for the
contexts was gathered from different sources on the
web using software to crawl those sites. The rest
of the dataset (question-answer pairs) was curated
and created manually.
Who was involved in the data collection pro-
cess? How were they compensated?
The data
was collected by computational linguists and data
scientists from a research institute.
Over what time-frame was the data collected?
The data was collected during 2023, when the
dataset was created.
How was the data associated with each instance
acquired?
The question-answer pairs were cre-
ated and revised by computational linguists.
Does the dataset contain all possible instances?
The dataset is composed of selected instances of
different datasets created by a research institute.
If the dataset is a sample, then what is the pop-
ulation?
This dataset is a 24,5% sample of the
original complete datasets. The instances were ran-
domly selected from the original datasets.
Is there information missing from the dataset
and why?
There is no data missing.
Are there any known errors, sources of noise, or
redundancies in the data?
There are no known
errors because the revision process ensured the data
is as clean and error-free as possible.
Data Preprocessing
What preprocessing/cleaning was done?
The
text contained in the "context" part of each instance
in the dataset has not undergone any preprocessing
or changes. There was no need to apply any clean-
ing to the question-answer pairs because they were
created manually by computational linguists fol-
lowing a rigorous methodology and were subjected
to revision afterwards.
Was the “raw” data saved in addition to the
preprocessed/clean data?
No, the text in the
dataset is the raw data.
Is the preprocessing software available?
No
preprocessing software was used.
Does this dataset collection/processing pro-
cedure achieve the motivation for creating
the dataset stated in the first section of this
datasheet?
Yes, the collection procedure en-
sures the dataset is sufficiently varied so it can be
used to evaluate a model on a wide range of topics.
However, there are some potential limitations in the
dataset which might slightly bias the data towards
particular topics, because not all topics included
have the exact same representation in the dataset,
and obviously it was not possible to cover all topics
in existence.
Dataset Distribution
How is the dataset distributed?
The dataset is
available in HuggingFace33.
When will the dataset be released/first dis-
tributed?
The dataset was released in 2024.
What license (if any) is it distributed under?
The dataset is licensed under CC BY-NC-SA 4.0.
Are there any fees or access/export restrictions?
There are no fees or restrictions.
Dataset Maintenance
Who
is
supporting/hosting/maintaining
the
dataset?
How
does
one
contact
the
owner/curator/manager of the dataset?
The dataset is hosted at HuggingFace, and the
research institute can be contacted through email
contacto.iic@iic.uam.es.
Will the dataset be updated? How often and
by whom?
How will updates/revisions be docu-
mented and communicated? Is there an erratum?
It is not planned to update the dataset at the
moment.
Is there a repository to link to any/all pa-
pers/systems that use this dataset?
No.
Legal & Ethical Considerations
If the dataset relates to people or was gener-
ated by people, were they informed about the
data collection?
Not applicable. The data was
collected from public web sources, and does not
contain sensitive personal information.
33https://hf.co/datasets/IIC/AQuAS

--- Page 33 ---

If it relates to other ethically protected subjects,
have appropriate obligations been met?
Not
applicable.
If it relates to people, were there any ethical
review applications/reviews/approvals?
Not
applicable.
If it relates to people, were they told what the
dataset would be used for and did they consent?
Not applicable.
If it relates to people, could this dataset expose
people to harm or legal action?
Not applicable.
If it relates to people, does it unfairly advantage
or disadvantage a particular social group?
Not
applicable.
If it relates to people, were they provided with
privacy guarantees?
Not applicable.
Does the dataset comply with the EU Gen-
eral Data Protection Regulation (GDPR)?
The
dataset complies with GDPR.
Does the dataset contain information that might
be considered sensitive or confidential?
No.
Does the dataset contain information that might
be considered inappropriate or offensive?
No.
ClinTreatES
The ClinTreatES (LenguajeNatural.AI, 2024b)
dataset consists of clinical cases collected directly
from doctors in various medical specialties (cardi-
ology, traumatology, emergency, psychiatry, neu-
rology, dermatology, ENT-laryngology, and anaes-
thesia) across European medical centers. It was
developed through a joint collaboration between
LenguajeNatural.AI and healthcare professionals.
The dataset is intended for evaluating the ability
of large language models (LLMs) to generate ef-
fective treatment plans based on provided clinical
cases and diagnoses.
Motivation for Dataset Creation
Why was the dataset created?
ClinTreatES was
created to evaluate LLMs’ capability to design ap-
propriate treatments from real clinical cases and
their corresponding diagnoses.
What (other) tasks could the dataset be used
for?
In addition to treatment planning, the dataset
may be used to study medical reasoning and
decision-making; however, it is not recommended
for diagnostic tasks.
Who funded the creation of the dataset?
The
dataset was developed through a collaboration be-
tween an NLP startup and healthcare professionals.
Dataset Composition
What are the instances?
Each instance com-
prises a clinical case description and its associated
diagnosis.
Are relationships between instances made ex-
plicit in the data?
No, there are no explicit rela-
tionships between instances.
How many instances of each type are there?
The dataset contains 62 examples.
What data does each instance consist of?
Each
instance includes text data: a clinical case and its
corresponding diagnosis, which serves as the basis
for generating a treatment plan.
Is everything included or does the data rely
on external resources?
The dataset is self-
contained with no reliance on external resources.
Are there recommended data splits or evalu-
ation measures?
No specific splits are recom-
mended; the dataset is intended primarily for eval-
uation purposes.

--- Page 34 ---

Data Collection Process
How was the data collected?
Data was collected
directly from healthcare professionals across vari-
ous specialities in European medical centers.
Who was involved in the data collection process?
Medical professionals from cardiology, traumatol-
ogy, emergency medicine, psychiatry, neurology,
dermatology, ENT-laryngology, and anesthesia con-
tributed to the dataset.
Over what time-frame was the data collected?
The data was collected in 2024.
How was the data associated with each instance
acquired?
Clinical cases and their corresponding
diagnoses were directly provided by the contribut-
ing healthcare professionals.
Does the dataset contain all possible instances?
It is a curated collection and does not cover every
possible clinical case.
If the dataset is a sample, then what is the popu-
lation?
The dataset represents a curated sample
of clinical cases from European medical centers.
Is there information missing from the dataset
and why?
No, all relevant information is in-
cluded.
Are there any known errors, sources of noise,
or redundancies in the data?
The data has been
carefully curated and reviewed to minimize errors
and noise.
Data Preprocessing
What preprocessing/cleaning was done?
The
clinical texts were formatted according to a stan-
dardized template; only minimal preprocessing was
applied.
Was the “raw” data saved in addition to the
preprocessed/clean data?
Yes, the dataset con-
tains the original clinical texts as provided by the
contributors.
Is the preprocessing software available?
No
specific preprocessing software was used.
Does this dataset collection/processing pro-
cedure achieve the motivation for creating
the dataset stated in the first section of this
datasheet?
Yes, the collection and curation pro-
cess ensures the dataset is suitable for evaluating
treatment design tasks by LLMs.
Dataset Distribution
How is the dataset distributed?
The dataset is
available on HuggingFace34.
When will the dataset be released/first dis-
tributed?
The dataset was released in March
2024.
What license (if any) is it distributed under?
It
is distributed under the CC BY-NC-SA 4.0 license.
Are there any fees or access/export restrictions?
There are no fees or restrictions.
Dataset Maintenance
Who is supporting/hosting/maintaining the
dataset?
The dataset is hosted on HuggingFace
and maintained by the NLP startup.
Will the dataset be updated? How often and by
whom?
No updates are planned at this time.
Is there a repository to link to any/all pa-
pers/systems that use this dataset?
The dataset
is available on HuggingFace35.
Legal & Ethical Considerations
If the dataset relates to people, were they in-
formed about the data collection?
The clinical
cases were provided by healthcare professionals;
any personal details have been removed to ensure
anonymity. They were anonymized by the health-
care professionals themselves, before transferring
the data to the NLP startup.
If it relates to other ethically protected subjects,
have appropriate obligations been met?
Yes,
all obligations have been met and ensured in the
data collection process.
If it relates to people, were there any ethical
review applications/reviews/approvals?
Yes,
healthcare professionals ensured the ethical review
was complete.
If it relates to people, were they told what the
dataset would be used for and did they consent?
Yes, patients were told in advance about the ob-
jective of data collection and they provided their
consent for this use.
34https://hf.co/datasets/LenguajeNaturalAI/
ClinTreatES
35https://hf.co/datasets/LenguajeNaturalAI/
ClinTreatES

--- Page 35 ---

If it relates to people, could this dataset expose
people to harm or legal action?
No, as the data
is anonymized by the healthcare professionals.
If it relates to people, does it unfairly advantage
or disadvantage a particular social group?
No.
If it relates to people, were they provided with
privacy guarantees?
Yes, all personal informa-
tion has been removed by the healthcare profes-
sionals.
Does the dataset comply with the EU General
Data Protection Regulation (GDPR)?
Yes, it
complies with GDPR.
Does the dataset contain information that might
be considered sensitive or confidential?
No, all
potentially sensitive or confidential information has
been removed.
Does the dataset contain information that might
be considered inappropriate or offensive?
No.
ClinDiagnosES
The ClinDiagnosES (LenguajeNatural.AI, 2024b)
dataset comprises clinical cases accompanied by
corresponding diagnoses, collected directly from
healthcare professionals across multiple specialties
in Europe. It is intended for evaluating LLMs’
diagnostic reasoning abilities.
Motivation for Dataset Creation
Why was the dataset created?
ClinDiagnosES
was created to assess the ability of LLMs to gen-
erate accurate diagnoses based on clinical case de-
scriptions.
What (other) tasks could the dataset be used
for?
Besides diagnostic evaluation, it can be used
to study medical reasoning; however, it is not suit-
able for treatment planning tasks.
Who funded the creation of the dataset?
The
dataset was developed through a collaboration be-
tween LenguajeNatural.AI and healthcare profes-
sionals.
Dataset Composition
What are the instances?
Each instance consists
of a clinical case description along with its corre-
sponding diagnosis.
Are relationships between instances made ex-
plicit in the data?
No, there are no explicit rela-
tionships between instances.
How many instances of each type are there?
The dataset contains 62 examples.
What data does each instance consist of?
Each
instance includes text data representing a clinical
case and its associated diagnosis.
Is everything included or does the data rely
on external resources?
The dataset is self-
contained.
Are there recommended data splits or evalu-
ation measures?
No specific splits are recom-
mended; it is intended for evaluation purposes.
Data Collection Process
How was the data collected?
Data was collected
directly from healthcare professionals across vari-
ous medical specialties.

--- Page 36 ---

Who was involved in the data collection process?
Healthcare professionals from fields such as cardi-
ology, traumatology, emergency medicine, psychia-
try, neurology, dermatology, ENT-laryngology, and
anesthesia contributed.
Over what time-frame was the data collected?
The data was collected in 2024.
How was the data associated with each instance
acquired?
Each clinical case was accompanied
by a diagnosis provided by a medical expert.
Does the dataset contain all possible instances?
It is a curated collection and does not encompass
every possible clinical case.
If the dataset is a sample, then what is the popu-
lation?
The dataset represents a curated sample
of clinical cases from European medical centers.
Is there information missing from the dataset
and why?
No, all necessary information is in-
cluded.
Are there any known errors, sources of noise, or
redundancies in the data?
The dataset has been
reviewed to minimize errors and inconsistencies.
Data Preprocessing
What preprocessing/cleaning was done?
The
clinical cases and diagnoses were formatted using
a standardized template with minimal cleaning.
Was the “raw” data saved in addition to the
preprocessed/clean data?
Yes, the raw clinical
texts and diagnoses are preserved.
Is the preprocessing software available?
No
specific preprocessing software was utilized.
Does this dataset collection/processing pro-
cedure achieve the motivation for creating
the dataset stated in the first section of this
datasheet?
Yes,
the procedure ensures the
dataset is suitable for evaluating diagnostic rea-
soning in LLMs.
Dataset Distribution
How is the dataset distributed?
The dataset is
available on HuggingFace36.
When will the dataset be released/first dis-
tributed?
It was released in March 2024.
36https://hf.co/datasets/LenguajeNaturalAI/
ClinDiagnosES
What license (if any) is it distributed under?
It
is distributed under the CC BY-NC-SA 4.0 license.
Are there any fees or access/export restrictions?
There are no fees or restrictions.
Dataset Maintenance
Who is supporting/hosting/maintaining the
dataset?
The dataset is hosted on HuggingFace
and maintained by the NLP startup.
Will the dataset be updated? How often and by
whom?
No updates are planned at this time.
Is there a repository to link to any/all pa-
pers/systems that use this dataset?
The dataset
is available on HuggingFace37.
Legal & Ethical Considerations
If the dataset relates to people, were they in-
formed about the data collection?
The clinical
cases were provided by healthcare professionals;
any personal details have been removed to ensure
anonymity. They were anonymized by the health-
care professionals themselves, before transferring
the data to the NLP startup.
If it relates to other ethically protected subjects,
have appropriate obligations been met?
Yes,
all obligations have been met and ensured in the
data collection process.
If it relates to people, were there any ethical
review applications/reviews/approvals?
Yes,
healthcare professionals ensured the ethical review
was complete.
If it relates to people, were they told what the
dataset would be used for and did they consent?
Yes, patients were told in advance about the ob-
jective of data collection and they provided their
consent for this use.
If it relates to people, could this dataset expose
people to harm or legal action?
No, as the data
is anonymized by the healthcare professionals.
If it relates to people, does it unfairly advantage
or disadvantage a particular social group?
No.
If it relates to people, were they provided with
privacy guarantees?
Yes, all personal informa-
tion has been removed by the healthcare profes-
sionals.
37https://hf.co/datasets/LenguajeNaturalAI/
ClinDiagnosES

--- Page 37 ---

Does the dataset comply with the EU General
Data Protection Regulation (GDPR)?
Yes, it
complies with GDPR.
Does the dataset contain information that might
be considered sensitive or confidential?
No, all
potentially sensitive or confidential information has
been removed.
Does the dataset contain information that might
be considered inappropriate or offensive?
No.
HumorQA
The
HumorQA
dataset
(LenguajeNatural.AI,
2024a), developed collaboratively by LenguajeNat-
ural.AI and Human Profit Consulting, focuses on
humor classification. It consists of jokes paired
with labels indicating the joke type: C/E (Com-
parison/Exaggeration), JP (Wordplay), R3 (Rule
of Three) and AI (Animating the Inanimate). The
data set is based on a study involving 94 executives
and is intended to evaluate the ability of LLMs to
understand and classify humor.
Motivation for Dataset Creation
Why was the dataset created?
HumorQA was
created to assess the ability of LLMs to recognize
and classify different types of humor.
What (other) tasks could the dataset be used
for?
It can also be used for research on senti-
ment analysis and humor recognition, although its
primary purpose is humor classification.
Who funded the creation of the dataset?
The
dataset was developed through a collaboration be-
tween an NLP startup and a psychology consulting
firm.
Dataset Composition
What are the instances?
Each instance com-
prises a joke and its corresponding humor-type
label.
Are relationships between instances made ex-
plicit in the data?
No, there are no explicit rela-
tionships between instances.
How many instances of each type are there?
The dataset contains 51 examples.
What data does each instance consist of?
Each
instance includes text data representing a joke and
a label indicating its humor category.
Is everything included or does the data rely
on external resources?
The dataset is self-
contained.
Are there recommended data splits or evalu-
ation measures?
No specific splits are recom-
mended; it is intended for evaluation purposes.
Data Collection Process
How was the data collected?
Jokes were col-
lected and curated as part of a research study in-

--- Page 38 ---

volving humor workshops and interviews with 94
executives.
Who was involved in the data collection pro-
cess?
The data collection involved humor experts
at Human Profit Consulting along with participat-
ing executives.
Over what time-frame was the data collected?
The data was collected in 2024.
How was the data associated with each instance
acquired?
Jokes were labeled according to a pre-
defined categorization based on the study’s method-
ology.
Does the dataset contain all possible instances?
It is a curated sample representing various humor
styles.
If the dataset is a sample, then what is the popu-
lation?
The sample represents humorous content
identified in a study with executives from diverse
sectors.
Is there information missing from the dataset
and why?
No, all relevant information is in-
cluded.
Are there any known errors, sources of noise,
or redundancies in the data?
The dataset has
been thoroughly reviewed; no significant errors or
redundancies have been identified.
Data Preprocessing
What preprocessing/cleaning was done?
The
jokes and labels were formatted into a standardized
template with minimal preprocessing.
Was the “raw” data saved in addition to the
preprocessed/clean data?
Yes, the original joke
texts are preserved.
Is the preprocessing software available?
No
specific preprocessing software was used.
Does this dataset collection/processing pro-
cedure achieve the motivation for creating
the dataset stated in the first section of this
datasheet?
Yes, the curation process supports
the evaluation of humor classification by LLMs.
Dataset Distribution
How is the dataset distributed?
The dataset is
available on HuggingFace38.
38https://hf.co/datasets/LenguajeNaturalAI/
HumorQA
When will the dataset be released/first dis-
tributed?
It was released in March 2024.
What license (if any) is it distributed under?
It
is distributed under the CC BY-NC-SA 4.0 license.
Are there any fees or access/export restrictions?
There are no fees or restrictions.
Dataset Maintenance
Who is supporting/hosting/maintaining the
dataset?
The dataset is hosted on HuggingFace
by the NLP startup.
Will the dataset be updated? How often and by
whom?
No updates are planned at this time.
Is there a repository to link to any/all pa-
pers/systems that use this dataset?
The dataset
is available on HuggingFace39.
Legal & Ethical Considerations
If the dataset relates to people, were they in-
formed about the data collection?
The dataset
is based on humorous content and research; it does
not involve personal data.
If it relates to other ethically protected subjects,
have appropriate obligations been met?
Not
applicable.
If it relates to people, were there any ethical re-
view applications/reviews/approvals?
Not ap-
plicable.
If it relates to people, were they told what the
dataset would be used for and did they consent?
Not applicable.
If it relates to people, could this dataset expose
people to harm or legal action?
No.
If it relates to people, does it unfairly advantage
or disadvantage a particular social group?
No.
If it relates to people, were they provided with
privacy guarantees?
Not applicable.
Does the dataset comply with the EU General
Data Protection Regulation (GDPR)?
Yes, it
complies with GDPR.
Does the dataset contain information that might
be considered sensitive or confidential?
No.
Does the dataset contain information that might
be considered inappropriate or offensive?
No.
39https://hf.co/datasets/LenguajeNaturalAI/
HumorQA

--- Page 39 ---

RagQuAS
The
Retrieval-Augmented-Generation
and
Question-Answering
in
Spanish
(RagQuAS)
dataset (Instituto de Ingeniería del Conocimiento,
2024b), created by Instituto de Ingeniería del
Conocimiento, is a high-quality monolingual
Spanish dataset designed to evaluate models
in retrieval-augmented generation (RAG) and
question-answering tasks. It consists of 201 exam-
ples covering a wide range of knowledge domains,
such as hobbies, linguistics, health, astronomy,
and customer service.
Each example includes
a question, multiple context passages extracted
from different documents, and a gold-standard
answer.
This dataset is particularly useful for
assessing a model’s ability to retrieve relevant
information from multiple sources and generate
accurate, contextually appropriate responses.
Motivation for Dataset Creation
Why was the dataset created?
(e.g., were there
specific tasks in mind, or a specific gap that needed
to be filled?) RagQuAS was created to provide
high-quality examples of questions and answers
with related contexts that can be used to evaluate
models in retrieval-augmented generation (RAG)
and question-answering tasks.
What (other) tasks could the dataset be used
for?
Are there obvious tasks for which it should
not be used? There are no recommended uses for
this dataset other than evaluation.
Who funded the creation of the dataset?
If
there is an associated grant, provide the grant num-
ber. The dataset was created and funded by Insti-
tuto de Ingeniería de Conocimiento.
Dataset Composition
What are the instances?
(that is, examples; e.g.,
documents, images, people, countries) Are there
multiple types of instances? (e.g., movies, users,
ratings; people, interactions between them; nodes,
edges) Each instance consists of several categories
of text: the topic, a question, an indicator of the
variant of the question (this represents questions
with linguistic differences but pertaining to the
same contexts than other questions), an answer,
one to five contexts, one to five complete docu-
ments from where the contexts were extracted and
the links to these documents.
Are relationships between instances made ex-
plicit in the data
(e.g., social network links,
user/movie ratings, etc.)? There are no known rela-
tionships between instances.
How many instances of each type are there?
The dataset consists of 201 examples.
What data does each instance consist of?
“Raw” data (e.g., unprocessed text or images)?
Features/attributes? Is there a label/target asso-
ciated with instances? If the instances are related
to people, are subpopulations identified (e.g., by
age, gender, etc.) and what is their distribution?
The instances consist of text data and are labeled
with the corresponding topic.
Is everything included or does the data rely on
external resources?
Everything is included in
the dataset.
Are there recommended data splits or evalua-
tion measures?
Since the dataset is intended for
testing, there is no recommended split.
Data Collection Process
How was the data collected?
The data for the
contexts was gathered from different sources manu-
ally with the help of generative models (to suggest
web searches and results). The rest of the dataset
was curated and created manually.
Who was involved in the data collection pro-
cess? How were they compensated?
The data
was collected by computational linguists and data
scientists from the research institute.
Over what time-frame was the data collected?
The data was collected during 2023, when the
dataset was created.
How was the data associated with each instance
acquired?
The question-answer pairs were cre-
ated and revised by computational linguists.
Does the dataset contain all possible instances?
The dataset is composed of selected instances of a
dataset created by the research institute.
If the dataset is a sample, then what is the pop-
ulation?
This dataset is a 24% sample of the
original complete datasets. The instances were
randomly selected from the original dataset.
Is there information missing from the dataset
and why?
There is no data missing.

--- Page 40 ---

Are there any known errors, sources of noise, or
redundancies in the data?
There are no known
errors because the revision process ensured the data
is as clean and error free as possible.
Data Preprocessing
What preprocessing/cleaning was done?
The
text contained in context and document part of each
instance in the dataset has not undergone any pre-
processing or changes. The questions were created
manually by computational linguists following a
rigorous methodology and were subjected to revi-
sion afterwards. The answers were carefully cu-
rated and revised by linguists from generated texts.
Was the “raw” data saved in addition to the
preprocessed/clean data?
No, the text in the
dataset is the raw data.
Is the preprocessing software available?
No
preprocessing software was used.
Does this dataset collection/processing pro-
cedure achieve the motivation for creating
the dataset stated in the first section of this
datasheet?
Yes, the methodology used when
creating the dataset ensures it is sufficiently varied
so it can be used to evaluate a model on a wide
range of topics. However, there are some potential
limitations in the dataset which might slightly bias
the data towards particular topics, because not all
topics included have the exact same representation
in the dataset, and obviously it was not possible to
cover all topics in existence.
Dataset Distribution
How is the dataset distributed?
The dataset is
available in HuggingFace40.
When will the dataset be released/first dis-
tributed?
The dataset was released in 2024.
What license (if any) is it distributed under?
Are there any copyrights on the data? The dataset
is licensed under CC BY-NC-SA 4.0.
Are there any fees or access/export restrictions?
There are no fees or restrictions.
Dataset Maintenance
Who
is
supporting/hosting/maintaining
the
dataset?
How
does
one
contact
the
owner/curator/manager of the dataset?
The
40https://hf.co/datasets/IIC/RagQuAS
dataset is hosted at HuggingFace, and the re-
search institute can be contacted through email
contacto.iic@iic.uam.es.
Will the dataset be updated? How often and
by whom?
How will updates/revisions be docu-
mented and communicated? Is there an erratum? It
is not planned to update the dataset at the moment.
Is there a repository to link to any/all pa-
pers/systems that use this dataset?
No.
Legal & Ethical Considerations
If the dataset relates to people or was gener-
ated by people, were they informed about the
data collection?
Not applicable. The data was
collected from public web sources, and does not
contain sensitive personal information.
If it relates to other ethically protected subjects,
have appropriate obligations been met?
Not
applicable.
If it relates to people, were there any ethical
review applications/reviews/approvals?
Not
applicable.
If it relates to people, were they told what the
dataset would be used for and did they consent?
Not applicable.
If it relates to people, could this dataset expose
people to harm or legal action?
Not applicable.
If it relates to people, does it unfairly advantage
or disadvantage a particular social group?
Not
applicable.
If it relates to people, were they provided with
privacy guarantees?
Not applicable.
Does the dataset comply with the EU Gen-
eral Data Protection Regulation (GDPR)?
The
dataset complies with GDPR.
Does the dataset contain information that might
be considered sensitive or confidential?
No.
Does the dataset contain information that might
be considered inappropriate or offensive?
No.

--- Page 41 ---

SpaLawEx
The
SpaLawEx
dataset
(LenguajeNatural.AI,
2024c) consists of multiple-choice legal questions
extracted from Spanish Bar Examination papers
of 2022 and 2023. Each instance includes a legal
question along with four answer options (A, B, C,
and D).
Motivation for Dataset Creation
Why was the dataset created?
SpaLawEx was
created to evaluate the legal reasoning and knowl-
edge of LLMs within the context of Spanish law
using multiple-choice questions.
What (other) tasks could the dataset be used
for?
In addition to benchmarking legal question
answering systems, it may be used for legal educa-
tion; it is not intended for non-legal tasks.
Who funded the creation of the dataset?
The
dataset was developed by an NLP startup, with
contributions from legal experts.
Dataset Composition
What are the instances?
Each instance is a
multiple-choice legal question accompanied by
four answer options.
Are relationships between instances made ex-
plicit in the data?
No, there are no explicit rela-
tionships between instances.
How many instances of each type are there?
The dataset contains 119 examples.
What data does each instance consist of?
Each
instance comprises text data, including a legal ques-
tion and its four answer options (A, B, C, and D).
Is everything included or does the data rely
on external resources?
The dataset is self-
contained, extracted from publicly available ex-
amination papers.
Are there recommended data splits or evalu-
ation measures?
No specific splits are recom-
mended; the dataset is intended for evaluation pur-
poses.
Data Collection Process
How was the data collected?
Data were ex-
tracted from official Spanish Bar Examination pa-
pers from 2022 and 2023.
Who was involved in the data collection process?
The extraction was performed by the developers at
an NLP startup, with input from legal experts.
Over what time-frame was the data collected?
The data was collected in 2024.
How was the data associated with each instance
acquired?
Questions and answer options were
directly extracted from exam documents.
Does the dataset contain all possible instances?
It is a comprehensive collection of questions from
the specified examination periods. However, it is
not exhaustive and it does not contain all possible
instances.
If the dataset is a sample, then what is the popu-
lation?
It represents the pool of questions from
the Spanish Bar Examinations of 2022 and 2023.
Is there information missing from the dataset
and why?
No, all relevant information is in-
cluded.
Are there any known errors, sources of noise, or
redundancies in the data?
The dataset has been
checked for accuracy; any minor extraction errors
are not known to be significant.
Data Preprocessing
What preprocessing/cleaning was done?
The
exam questions and answer options were formatted
into a standardized template with minimal cleaning.
Was the “raw” data saved in addition to the
preprocessed/clean data?
Yes, the original ex-
tracted text is preserved.
Is the preprocessing software available?
No
specific preprocessing software was used.
Does this dataset collection/processing pro-
cedure achieve the motivation for creating
the dataset stated in the first section of this
datasheet?
Yes, the process ensures the dataset
is suitable for evaluating legal reasoning in LLMs.
Dataset Distribution
How is the dataset distributed?
The dataset is
available on HuggingFace41.
When will the dataset be released/first dis-
tributed?
It was released in March 2024.
41https://hf.co/datasets/LenguajeNaturalAI/
SpaLawEx

--- Page 42 ---

What license (if any) is it distributed under?
It
is distributed under the CC BY-NC-SA 4.0 license.
Are there any fees or access/export restrictions?
There are no fees or restrictions.
Dataset Maintenance
Who is supporting/hosting/maintaining the
dataset?
The dataset is hosted on HuggingFace
by the NLP startup.
Will the dataset be updated? How often and by
whom?
No updates are planned at this time.
Is there a repository to link to any/all pa-
pers/systems that use this dataset?
No reposi-
tory has been provided.
Legal & Ethical Considerations
If the dataset relates to people, were they in-
formed about the data collection?
The dataset
is derived from public examination materials and
does not involve personal data.
If it relates to other ethically protected subjects,
have appropriate obligations been met?
Not
applicable.
If it relates to people, were there any ethical re-
view applications/reviews/approvals?
Not ap-
plicable.
If it relates to people, were they told what the
dataset would be used for and did they consent?
Not applicable.
If it relates to people, could this dataset expose
people to harm or legal action?
No.
If it relates to people, does it unfairly advantage
or disadvantage a particular social group?
No.
If it relates to people, were they provided with
privacy guarantees?
Not applicable.
Does the dataset comply with the EU General
Data Protection Regulation (GDPR)?
Yes, it
complies with GDPR.
Does the dataset contain information that might
be considered sensitive or confidential?
No.
Does the dataset contain information that might
be considered inappropriate or offensive?
No.
TELEIA
The TELEIA (Mayor-Rocher et al., 2025) dataset
is intended for the evaluation of Spanish language
knowledge focusing on reading comprehension and
grammatical competence. The dataset is designed
as a set of multiple-choice questions that have the
same format and level as those used in several Span-
ish evaluation tests for humans. The questions are
divided into three blocks which resemble existing
tests of Spanish for foreign learners and University
access. In total, one hundred questions are included
that have been prepared and revised by experts on
Spanish language, and that have been validated by
comparing the results with the original exams.
Motivation for Dataset Creation
Why was the dataset created?
The main mo-
tivation was to have a simple test to evaluate the
competence of LLMs in Spanish, similar to tests
used with humans.
What (other) tasks could the dataset be used
for?
The test also checks reading comprehension
and thus can be used to evaluate natural language
understanding.
Who funded the creation of the dataset?
The
development of the dataset was supported by the
FUN4DATE (PID2022-136684OB-C22) project
funded by the Spanish Agencia Estatal de Investi-
gación (AEI) 10.13039/501100011033.
Dataset Composition
What are the instances?
The test is made of
multiple-choice questions.
Are relationships between instances made ex-
plicit in the data
No.
How many instances of each type are there?
The dataset consists of 100 questions.
What data does each instance consist of?
Each
question has a text presenting the question and four
answer options, of which only one is correct.
Is everything included or does the data rely on
external resources?
Everything is included in
the dataset.
Are there recommended data splits or evalua-
tion measures?
No.

--- Page 43 ---

Data Collection Process
How was the data collected?
Questions were
formulated and peer-reviewed by experts in Span-
ish.
Who was involved in the data collection pro-
cess?
Experts in Spanish who participated as
researchers in our group.
Over what time-frame was the data collected?
The questions were created during the spring of
2024.
How was the data associated with each instance
acquired?
Data was created by experts.
Does the dataset contain all possible instances?
Questions are examples, and many other similar
questions can be formulated.
If the dataset is a sample, then what is the popu-
lation?
Not applicable.
Is there information missing from the dataset
and why?
No.
Are there any known errors, sources of noise, or
redundancies in the data?
No.
Data Preprocessing
What preprocessing/cleaning was done?
None.
Was the “raw” data saved in addition to the
preprocessed/clean data?
Not applicable.
Is the preprocessing software available?
Not
applicable.
Does this dataset collection/processing pro-
cedure achieve the motivation for creating
the dataset stated in the first section of this
datasheet?
Yes.
Dataset Distribution
How is the dataset distributed?
Websites.
When will the dataset be released/first dis-
tributed?
Data is available since July 2024.
What license (if any) is it distributed under?
No license or restrictions are applicable.
Are there any fees or access/export restrictions?
No.
Dataset Maintenance
Who is supporting/hosting/maintaining the
dataset?
The dataset is hosted at Zenodo42 pro-
viding contact details for all the authors.
Will the dataset be updated?
No updates are
expected, but the repository supports versioning.
Is there a repository to link to any/all pa-
pers/systems that use this dataset?
No.
Legal & Ethical Considerations
If the dataset relates to people (e.g., their at-
tributes) or was generated by people, were they
informed about the data collection?
Not appli-
cable.
If it relates to other ethically protected subjects,
have appropriate obligations been met?
Not
applicable.
If it relates to people, were there any ethical
review applications/reviews/approvals?
Not
applicable.
If it relates to people, were they told what the
dataset would be used for and did they consent?
Not applicable.
If it relates to people, could this dataset expose
people to harm or legal action?
Not applicable.
If it relates to people, does it unfairly advantage
or disadvantage a particular social group?
Not
applicable.
If it relates to people, were they provided with
privacy guarantees?
Not applicable.
Does the dataset comply with the EU General
Data Protection Regulation (GDPR)?
Yes.
Does the dataset contain information that might
be considered sensitive or confidential?
No.
Does the dataset contain information that might
be considered inappropriate or offensive?
No.
42https://zenodo.org/records/12571763

```
