---
title: "2025-González-Borrego-IberBench LLM Evaluation on Iberian Languages - PDF Extract"
source_pdf: "2025-González-Borrego-IberBench LLM Evaluation on Iberian Languages.pdf"
pages: 29
extracted_at: "2026-02-13T09:50:28.271954"
---

# PDF Extract: 2025-González-Borrego-IberBench LLM Evaluation on Iberian Languages

**Source PDF:** 2025-González-Borrego-IberBench LLM Evaluation on Iberian Languages.pdf
**Total Pages:** 29

---

## Content

```
--- Page 1 ---

IberBench: LLM Evaluation on Iberian Languages
Jos´e ´Angel Gonz´aleza, Ian Borrego Obradora, ´Alvaro Romo Herrerob, Areg Mikael Sarvazyana, Mara Chinea-R´ıosa,
Angelo Basilec, Marc Franco-Salvadord,†
aSymanto Research, Valencia, 46011, Spain
bKeepler Data Tech, Madrid, 28014, Spain
cUniversitat Polit`ecnica de Val`encia, Valencia, 46022, Spain
dUnited Nations International Computing Centre (UNICC), Valencia, 46930, Spain
Abstract
Despite their remarkable success, Large Language Models (LLMs) remain difficult to evaluate comprehensively,
particularly for languages other than English, where high-quality data is often limited. Existing benchmarks and
leaderboards are predominantly English-centric, with only a few addressing other languages. These benchmarks fall
short in several key areas: they overlook the diversity of language varieties, prioritize fundamental Natural Language
Processing (NLP) capabilities over tasks of industrial relevance, and are static. With these aspects in mind, we present
IberBench, a comprehensive and extensible benchmark designed to assess LLM performance on both fundamental and
industry-relevant NLP tasks, in languages spoken across the Iberian Peninsula and Ibero-America, including Spanish,
Portuguese, Catalan, Basque, Galician, and English, along with Spanish varieties like Mexican, Uruguayan, Peruvian,
Costa Rican, and Cuban. IberBench integrates 101 datasets from evaluation campaigns and recent benchmarks, cover-
ing 22 task categories such as sentiment and emotion analysis, toxicity detection, and summarization. The benchmark
addresses key limitations in current evaluation practices, such as the lack of linguistic diversity and static evaluation
setups by enabling continual updates and community-driven model and dataset submissions moderated by a commit-
tee of experts. We evaluate 23 LLMs ranging from 100 million to 14 billion parameters and provide empirical insights
into their strengths and limitations. Our findings indicate that (i) LLMs perform worse on industry-relevant tasks
than in fundamental ones, (ii) performance is on average lower for Galician and Basque, (iii) some tasks show results
close to random, and (iv) in other tasks LLMs perform above random but below shared task systems. IberBench
offers open-source implementations for the entire evaluation pipeline, including dataset normalization and hosting,
incremental evaluation of LLMs, and a publicly accessible leaderboard.1
Keywords: LLM Benchmark, Iberian Languages, IberBench
1. Introduction
LLMs have revolutionized NLP since they understand and generate language in zero- and few-shot settings, they
are flexible in handling almost any task, they are easy to use, and they show strong multilingual capabilities. LLM
adoption is growing rapidly among individuals and organizations, to the point that LLMs are used to automate ev-
eryday tasks like writing or editing emails, and core industrial services such as sentiment analysis for market insights
[1, 2].
Evaluating LLMs is essential to understand their strengths in such tasks and promote their adoption. Often, we
are addressing a task T with LLM A, and we want to know whether LLM B is better than A in T . Many times, A is
1The Leaderboard UI is accessible at https://huggingface.co/spaces/iberbench/leaderboard
Email addresses: jose.gonzalez@symanto.com (Jos´e ´Angel Gonz´alez), ian.borrego@symanto.com (Ian Borrego Obrador),
alvaro.romo@keepler.io ( ´Alvaro Romo Herrero), areg.sarvazyan@symanto.com (Areg Mikael Sarvazyan),
mara.chinea@symanto.com (Mara Chinea-R´ıos), abasile@doctor.upv.es (Angelo Basile), francom@unicc.org (Marc Franco-Salvador )
†This publication does not reflect the position/views of UNICC, and only the authors’ views.
Preprint submitted to Elsevier
April 24, 2025
arXiv:2504.16921v1  [cs.CL]  23 Apr 2025

--- Page 2 ---

selected by a priori decision, but if we are able to determine that B is better for T , B will be adopted instead. There
are many LLMs available, generally falling into two categories: open-source models such as Llama [3], Qwen [4],
and DeepSeek [5], and closed-source models such as GPT [6] and Gemini [7]. The landscape is vast, with variations
in reasoning-focused and chat-based models, monolingual and multilingual capabilities, parameter size, fine-tuning
strategy, and more. This diversity makes choosing the right LLM for a specific task and language challenging, as
factors such as performance, latency, and cost must be carefully considered.
Extensive research has been conducted on LLM evaluation. There are, at least, two main approaches: (i) automatic
evaluation using carefully designed benchmarks and (ii) manual evaluation, where real users interact with models and
express their preferences. Notable examples of the former include HELM [8] and the Open LLM Leaderboard [9],
while Chatbot Arena [10] is the most well-known example of the latter. However, most benchmarks following these
approaches lack at least one of these dimensions: multilingual coverage, industrial interest, and immutability.
Most evaluations of LLM capabilities prioritize English, often overlooking the rich linguistic diversity of other
languages. This gap is particularly evident when it comes to the languages of the Iberian Peninsula—Spanish, Por-
tuguese, Catalan, Basque, and Galician—as well as the many regional varieties of Spanish and Portuguese spo-
ken across Ibero-America, such as Mexican, Peruvian, Cuban, or Uruguayan.2 Despite having over 800 million
speakers, Iberian languages remain underrepresented in LLM evaluations, with some recent attempts to alleviate this
[11, 12, 13]. Most of these benchmarks focus on fundamental language capabilities and knowledge-based tasks, such
as question answering, language understanding, proficiency, and textual entailment. They overlook industry-relevant
tasks like intent classification, toxicity detection, affective analysis, and user profiling. Another major limitation of
existing benchmarks is their static nature: once established, the datasets remain unchanged over time. This lack of
adaptability increases the risk of saturation and prevents the inclusion of novel tasks and languages, ultimately limiting
their long-term utility.
To fill these gaps, we introduce IberBench, a benchmark specifically crafted to continually evaluate LLMs across
both fundamental NLP tasks and industry-relevant challenges in Iberian languages. IberBench draws its datasets from
two main sources. The first is a collection of shared tasks from workshops like IberLEF [14], IberEval [15], TASS
[16], and PAN [17], spanning editions from 2014 to 2024, co-located with the Spanish Society for Natural Language
Processing (SEPLN) and the Conference and Labs of the Evaluation Forum (CLEF). These workshops have played
a key role in advancing research and fostering collaboration within the Iberian NLP community, providing a wealth
of practical, industry-aligned tasks. The second source consists of recent general-purpose benchmarks specifically
designed to assess LLMs on fundamental language tasks. This includes near all datasets from La Leaderboard [11],
the evaluation suite of the Latxa model [18], and others. IberBench brings together a diverse collection of datasets
developed over the years for training and evaluating NLP models, combining both workshop-based resources and
contributions from the broader scientific literature. In total, IberBench comprises 101 datasets, tailored to the Iberian
languages shown in Figure 1 and spanning 22 task categories.
Beyond the datasets, three key components orchestrate the evaluation of LLMs in IberBench. First, the Leader-
board UI serves as the main interface, displaying various LLM rankings, plots, and reports; allowing users to request
new models for evaluation; and describing the datasets included in the benchmark. The second component is the in-
troduction of a committee of NLP specialists from both academia and industry which is responsible for key decisions,
such as determining which user-requested LLMs should be evaluated and which new datasets should be included.
Finally, the third component is the evaluation framework. For this, we rely on lm-evaluation-harness [19], which
we have extended to (i) include the IberBench datasets, (ii) support sequence labeling tasks, and (iii) streamline the
evaluation process by integrating a caching mechanism to add new datasets and evaluate LLMs solely on this data.
This way we ensure the relevance and applicability of IberBench over time.
So far, we have evaluated 23 LLMs, ranging from 100 million to 14 billion parameters. These include major
multilingual families like Llama, Qwen, and Phi [20], as well as models tailored for Iberian and European languages,
such as Latxa [18], Salamandra [21], and EuroLLM [22]. Our main findings reveal that (i) LLMs struggle with
industry-relevant tasks compared to fundamental language tasks, which dominate existing benchmarks, (ii) Galician
and Basque present greater challenges than other languages, (iii) some tasks like lexical borrowing detection, intent
classification, and machine-generated text detection remain largely unsolved, with top-performing LLMs barely sur-
2For simplicity, we will refer to all these languages collectively as Iberian languages.
2

--- Page 3 ---

Basque (eu)
Catalan (ca)
English (en)
Galician (gl)
Portuguese (pt)
Spanish (es-ES)
(a) Iberian Peninsula languages
Costa Rican (es-CR)
Cuban (es-CU)
Mexican (es-MX)
Peruvian (es-PE)
Uruguayan (es-UY)
(b) Spanish varieties in Ibero-America
Figure 1: Maps showing the Iberian languages considered in IberBench.
passing a random guesser, and (iv) in other tasks such as sentiment analysis, humor detection, and fake news detection,
LLMs are better than the random baseline but worse than most shared task submissions.
In summary, these are our key contributions:
• We introduce IberBench, a comprehensive benchmark comprising 101 datasets that span a wide range of fun-
damental and industry-relevant NLP tasks, broadening the scope of LLM evaluations in Iberian languages. The
IberBench pipeline is publicly released.
• We design IberBench with scalability, extensibility, and reproducibility in mind, to seamlessly integrate new
datasets, language varieties, and models over time, ensuring its continued relevance as the field evolves.
• We collect and standardize 58 datasets from workshops on Iberian languages—many of which are difficult to
access—and make them readily available through a unified evaluation framework.
• We evaluate both multilingual and language-specific models, providing insights into their performance on tasks
that reflect the linguistic diversity of Iberian languages.
2. Related Work
LLM evaluation schemes can often be categorized into two perspectives: human and automatic. Human evaluation
is subjective, often to measure specific behavioral properties or human preferences to model outputs. It estimates
output quality by crafting tailored inputs to elicit specific outputs from LLMs and assess user-centric or ethical aspects
such as helpfulness, fairness, security or safety. Prominent examples include evaluating a model’s robustness to
red-teaming and jailbreaking attempts [23, 24], multi-turn conversation and instruction following abilities [25], and
general human preference toward a specific model’s outputs [10, 26]. Unfortunately, human evaluation of LLMs
incurs high costs and is often biased, making it inadequate for large-scale, objective, reproducible model evaluations
[27, 28]. Moreover, human evaluation can include malicious actors that may poison the results [29].
Automatic evaluation is faster, more cost effective, less bias-prone and reproducible [19]. It is often used to mea-
sure performance in industry-relevant tasks like sentiment analysis or topic modeling, and fundamental capabilities
like natural language understanding, generation, and question answering. Automatic benchmarks are often created by
collecting existing datasets, releasing them along with LLM leaderboards and automatic evaluation pipelines. Some of
the first popular benchmarks include GLUE [30] and MMLU [31], which mainly measured fundamental capabilities
like reading comprehension, common sense reasoning, or general knowledge, while more recent efforts like LM Eval
Harness [19], HELM [8], and the Open LLM Leaderboard [9] also include a range of industry-relevant tasks such
as domain-specific sentiment analysis, social media toxicity detection, programming, and mathematical reasoning.
Moreover, recent advances in LLM-as-a-judge techniques show that LLMs are good alternatives to humans in specific
3

--- Page 4 ---

scenarios [32] when evaluating behavioral properties. It is proven that LLMs generate highly correlated answers to
humans [33], and exhibiting similar bias levels [34].
While most of the work has been done for English capability evaluations, there are recent efforts focusing on non-
English languages, with new benchmarks for European [35], Indic [36], South-east Asian [37], Arabic [38] languages,
and more. Spanish co-official languages have been represented in various initiatives such as La Leaderboard [11],
IberoBench [12],3 and Odesia [13]. However, these efforts still fail to capture the full extent of linguistic variation in
Iberian languages, they primarily focus on fundamental language and knowledge tasks, and are static. La Leaderboard
and IberoBench focus on language understanding datasets sourced from multilingual human translations of existing
English corpora, while Odesia focuses on a small set of sexism and propaganda detection datasets from existing shared
tasks in the IberLEF evaluation campaigns. IberBench extends these approaches to include (i) both fundamental and
industry-relevant tasks from workshops like IberLEF, IberEval, TASS, and PAN, (ii) not only Spain’s co-official
languages but also language varieties from Ibero-America, and (iii) a scalable framework to extend the benchmark
with new datasets and language varieties over time.
Most existing benchmarks focus on classification or generation tasks, largely ignoring sequence labeling tasks such
as Named Entity Recognition (NER) and Aspect-Based Sentiment Analysis (ABSA), that are essential for industrial
applications. Recent studies indicate that LLMs can match or even surpass encoder models in sequence labeling tasks
[39, 40], however, since current benchmarks largely overlook these tasks, LLMs have yet to be thoroughly evaluated in
this scenario. Bearing this in mind, IberBench allows to evaluate LLMs in sequence-labeling tasks through a custom
evaluation scheme, integrated in lm-evaluation-harness.
3. Iberbench
IberBench is made up of four key components that manage interactions, datasets, and evaluations: leaderboard
UI, organization, datasets, and LLM evaluation. The entire pipeline of IberBench is illustrated in Figure 2.
The benchmark’s entry point is the leaderboard UI, hosted on a HuggingFace Space,4 where users can view rank-
ings, plots and detailed reports of the evaluation results, submit new models for evaluation, and explore the datasets
of the benchmark. When a new LLM is requested, the request is queued to be reviewed by the IberBench organiza-
tion, which decides whether to include it in the leaderboard.5 In the same way, users can request the addition of new
datasets through discussions with the organization.6 Upon acceptance, the new datasets will be downloaded, normal-
ized, and hosted in a private HuggingFace repository. Each time a new model or dataset is accepted and prepared,
the organization will run the LLM Evaluation through a custom evaluation module that relies on lm-evaluation-
harness,7 and the results will be reflected on the leaderboard UI. All these components are described in more detail
in sections below.
3.1. Leaderboard UI
Inspired by prominent existing benchmarks [9, 35], IberBench introduces a comprehensive, interactive, and user-
friendly leaderboard interface, hosted in a dedicated HuggingFace Space, that presents model rankings across task
types, languages, and language varieties. The interface includes a wide array of plots, reports, and statistics, enabling
users to perform fine-grained analyses and gain a detailed understanding of LLM capabilities for Iberian languages.
Users can compare model performance across languages, domains, and tasks, facilitating both broad and targeted
evaluations. The leaderboard displays general rankings across all Iberian languages, as well as language-specific
rankings that highlight model performance on individual tasks within each language or variety. Each ranking includes
detailed metadata such as model name, parameter size, and evaluation scores, aggregated by language, variety, and
task type. The interface also provides a suite of visualizations, including plots to see what are the top-performing
3Despite the name similarity, IberBench and IberoBench were developed independently and in parallel, without the involved parties being aware
of each other.
4The Leaderboard UI is accessible at https://huggingface.co/spaces/iberbench/leaderboard
5The organization space is accessible at https://huggingface.co/iberbench
6The discussions space is accessible at https://huggingface.co/spaces/iberbench/README/discussions
7The evaluation module is accessible at https://github.com/IberBench/iberbench-evaluation/
4

--- Page 5 ---

Figure 2: IberBench overview. Users can view rankings, plots, and reports; request LLMs for evaluation through the UI; and propose new datasets
to the organization. The organization reviews these proposals for possible inclusion in the leaderboard. Once approved, datasets and models are
prepared, evaluated, and hosted to be displayed in the UI.
models on average, across tasks, Iberian languages, and performance trends with respect to model size, model type,
and task type.
To support community-driven evaluations, the interface includes a request portal that guides users through the
process of requesting new models. The request form requires: (i) the model or adapter name as listed on the Hugging-
Face Hub [41], (ii) a short model description, (iii) a contact email for correspondence, (iv) the weight precision format
(e.g., bfloat16, 8-bit, or quantization methods such as GPTQ [42]), (v) the weight type —original or adapted, (vi) the
base model (only for adapted models), and (vii) whether the model is pre-trained, fine-tuned, or fine-tuned for chat
applications. These model details directly influence the evaluation process, as they determine how models are loaded
and which inference parameters are applied in evaluation. Certain attributes such as the precision format, can signifi-
cantly affect inference behavior and performance outcomes. For this reason, and to ensure the novelty, compatibility,
and significance of the models, all requests are subject to a review process by the organization. Upon acceptance, the
model undergoes a rigorous, consistent, and reproducible evaluation process through lm-evaluation-harness.
Users can also explore the descriptions of the datasets associated with each language in the benchmark through the
visualization portal. This is essential to ensure transparency and to properly acknowledge the contributions of dataset
creators. All datasets included in IberBench have been developed over the years by the NLP community dedicated
to Iberian languages and it is therefore critical to give due credit. To this end, the leaderboard interface includes a
dedicated section that includes dataset details such as the source, task type,language, variety, number of labels (if
applicable), and URL of the creator’s website. In addition, some of the rankings and visualizations group tasks into
categories to enable broader insights. For example, aggressiveness and offensive language detection tasks are grouped
under Toxicity and Harmful Language Detection, while tasks such as Text Summarization and Intent Classification are
categorized as industry-relevant tasks. To maintain transparency in this aggregation process, the visualization portal
explicitly displays the mappings used to define these groups.
5

--- Page 6 ---

3.2. Organization
The IberBench organization serves as the central entity responsible for maintaining the high-quality standards that
ensure the long-term reliability and impact of the benchmark. At the time of writing, it is composed of seven members,
including experts in NLP, engineering, language ethics, and gender bias, drawn from both academia and industry. Most
of its members have previously served as shared-task participants, organizers, or members of committees in workshops
like IberLEF and PAN, bringing valuable experience and domain-specific knowledge. Their collective expertise plays
a key role in guiding the development of IberBench, ensuring its methodological rigor, ethical integrity, and continued
relevance to the research community.
Each time a new model or dataset is proposed, or when a user requests to join the organization, the team as-
sesses the request based on internal acceptance criteria. For model requests, priority is given to: (i) models trained
exclusively on Iberian languages, (ii) multilingual models in which Iberian languages constitute more than 30% of
the training tokens, and (iii) models developed in Europe, particularly within the Iberian Peninsula or Ibero-America.
For dataset inclusion, preference is given to datasets that: (i) focus specifically on Iberian languages, (ii) originate
from workshops organized in the Iberian Peninsula or Ibero-America, and (iii) target domains, language varieties,
or tasks not yet represented in the benchmark. The organization is also responsible for reviewing applications from
prospective new members. In this regard, preference is given to individuals from both academia and industry with
extensive experience working with Iberian languages, particularly those who have organized shared tasks, participated
in evaluation campaigns, or contributed to the creation of datasets in this linguistic context.
The role of the IberBench organization also involves dataset collection and model evaluation. Whenever a model
is accepted, designated members of the organization are responsible for running the evaluation pipeline with this
model on the existing IberBench datasets, either as batch or individual jobs, by leveraging cached results. Upon the
acceptance of a dataset, members are tasked with downloading, normalizing, and storing the dataset in a long-term
repository on HuggingFace, privately hosted under the IberBench HuggingFace organization. Additionally, they must
create a well-grounded configuration file for the lm-evaluation-harness to ensure that the evaluation process is
conducted fairly and consistently. Detailed descriptions of these procedures are provided in the following sections.
3.3. Datasets
Datasets are a core part of the IberBench benchmark, used to evaluate models across a wide range of NLP tasks.
As the first step in building IberBench, we carefully collected and prepared a set of 101 existing datasets to make them
suitable for LLM evaluation. This initial collection lays the groundwork for a future expansion with new datasets from
upcoming evaluation campaigns. All datasets were sourced from existing workshops and benchmarks.
Many of the datasets included in IberBench are sourced from recurring workshops and evaluation campaigns such
as IberLEF [14], IberEVAL [15], and TASS [16]—organized by SEPLN—as well as PAN [43], held within CLEF.
These datasets are often scattered across different platforms and are not always easily accessible, typically requiring
users to request access directly from the organizers through various channels. Due to these restrictions, we contacted
the organizers of all shared tasks from these workshops to obtain explicit permission for inclusion in IberBench. We
only incorporate into the benchmark those datasets for which we were granted authorization by the creators. This
process resulted in the retrospective compilation of 58 workshop-sourced datasets from 2014 to 2024. The remainder
of the IberBench datasets include the evaluation suite used to assess the Latxa model, the Belebele benchmark [44]
for multilingual natural language understanding, and nearly all datasets included in La Leaderboard. This integration
aims to unify recent LLM benchmarks with curated workshop datasets into a single benchmark that spans a broad
range of tasks, Iberian languages, and both foundational and industry-relevant task types.
During the dataset collection phase, we communicated IberBench’s data usage policy to all dataset creators.
Specifically, IberBench adheres to best practices regarding data management and ethical reuse: (i) dataset creators
are appropriately credited on the interface and dataset cards; (ii) we do not claim ownership of any dataset; and (iii)
all datasets are maintained in private repositories to prevent leakage and potential contamination. Preventing contam-
ination is particularly critical, as evaluation results become unreliable if an LLM has been exposed to test data during
training [45]. To this end, datasets are never released publicly and are only accessed during evaluation through inter-
nal, secure servers. However, we acknowledge that our measures can only prevent contamination from IberBench’s
infrastructure, and cannot account for prior public release of the datasets by their original authors.
6

--- Page 7 ---

Dataset preparation
Text
Real Madrid lose against Valencia CF in Madrid
Reference labels
[B-football team, I-football team, O, O, B-football team, I-football team, O, B-location]
Annotated example
<response> <football team> Real Madrid </football team> lose against <football team> Valencia
CF </football team> in <location> Madrid </location> </response>
Evaluation
Prompt
Your task is to perform Named Entity Recognition by wrapping each entity from the input text with
label tags. The set of label tags you can use are: football team, and location. Wrap all your response
between <response> ... </response>. Here are some examples:
Text: OpenAI is developing GPT-5.
Labels: <response> OpenAI is developing GPT-5 </response>
Text: Real Madrid lose against Valencia CF in Madrid.
Labels:
<response> <football team> Real Madrid </football team> lose against <football -
team> Valencia CF </football team> in <location> Madrid </location> </response>
Text: FC Barcelona is playing in Barcelona
LLM output
<response> <football team> FC Barcelona </football team> is playing in <location> Barcelona
</location> <response>
Parsed output
[B-football team, I-football team, O, O, O, B-location]
Table 1: Example of dataset preparation and evaluation of a NER task using the proposed annotation schema. The prompt includes two in-context
examples and the instance to predict is added below them. The underlines and colorings have been added for easier understanding but are not
included as part of the inputs or outputs.
Following the initial collection phase, all datasets were standardized using a custom normalization pipeline de-
veloped to automate this process.8 The pipeline is designed to handle datasets in diverse formats, including Excel
spreadsheets, tabular or comma-separated value files, HuggingFace datasets, and plaintext. The pipeline performs
a series of processing steps: it merges multiple files when necessary (e.g., when sample identifiers and labels are
stored separately), removes extraneous columns not relevant to the task, standardizes column names (e.g., to “text”
and “label”), adds language and language variety annotations where applicable, and cleans textual artifacts such as
mojibake and mixed encodings (e.g., “caf´e” is recovered from “caf ˜A©”) . Once processed, the normalized datasets
are uploaded to a private HuggingFace repository [46], accompanied by metadata such as the originating workshop,
year, and label set.
While this process is relatively straightforward for text classification and generation tasks, sequence labeling
tasks pose additional challenges. As they require a specific annotation schema, we designed one inspired by prior
work [40, 47]. In such cases, LLMs must be given explicit instructions on how to produce span-annotated outputs.
To this end, we include annotated examples in the datasets to be used later as few-shot examples. We define an
annotation schema where output labels are directly included into the input text by enclosing each annotated span
within corresponding label tags. An example of dataset preparation and evaluation of a NER task using this schema is
shown in Table 1. We prepare an annotated example for each text and its reference IOB labels in the dataset. During
evaluation, some annotated examples from the dataset are used as shots to instruct the LLM to follow the schema. We
then parse the generated output to extract the predicted sequence of IOB labels. Detailed instructions for preparing
sequence labeling datasets within IberBench are available in the documentation.9
We put together a total of 101 datasets, which are detailed in Tables 2 and 3. These tables include information
on the originating workshop, dataset or task name, year, language, language variety (if applicable), number of labels
(if applicable), and citation. URL information is available in the Appendix (Tables A.6 and A.7). Additionally, the
8The normalization pipeline is available at https://github.com/IberBench/dataset-preparation
9We provide a guide to prepare sequence-labeling datasets at https://github.com/IberBench/iberbench-evaluation/blob/main/
docs/token_classification_guide.md
7

--- Page 8 ---

Source
Task
Subtask
Year
Language
|L|
Category
TweetLID
TweetLID [48]
Language dentification
2014
es
7
Language Identification
TASS
TASS [49]
Emotion analysis
2020
es
7
Sentiment and Emotion Analysis
TASS [49]
Sentiment analysis
2020
es-{UY, MX, ES, CR, PE}
3
Sentiment and Emotion Analysis
PAN
Author Profiling [50]
Age detection
2015
es
4
Author Profiling
Author Profiling [43]
Gender detection
2017
es
2
Author Profiling
IberEval
MultiStanceCat [51]
Stance detection
2018
{es, ca}
3
Stance Detection
IberLEF
HAHA [52]
Humor detection
2019
es
2
Humor Detection
IroSvA [53]
Irony detection
2019
es-{CU, MX, ES}
2
Irony and Sarcasm Detection
MEX-A3T [54]
Aggressiveness detection
2019
es-MX
2
Toxicity and Harmful Language Detection
DETOXIS [55]
Aggressiveness detection
2021
es
2
Toxicity and Harmful Language Detection
DETOXIS [55]
Improper language detection
2021
es
2
Toxicity and Harmful Language Detection
DETOXIS [55]
Insult detection
2021
es
2
Toxicity and Harmful Language Detection
DETOXIS [55]
Mockery detection
2021
es
2
Toxicity and Harmful Language Detection
DETOXIS [55]
Sarcasm detection
2021
es
2
Irony and Sarcasm Detection
DETOXIS [55]
Toxicity detection
2021
es
2
Toxicity and Harmful Language Detection
EmoEvalEs [56]
Emotion analysis
2021
es
7
Sentiment and Emotion Analysis
EmoEvalEs [56]
Offensiveness detection
2021
es
2
Toxicity and Harmful Language Detection
EXIST [57]
Sexism categorization
2021
es
6
Prejudice and Discrimination Detection
EXIST [57]
Sexism detection
2021
es
2
Prejudice and Discrimination Detection
FakeDeS [58]
Fake News detection
2021
es
2
Fake News Detection
HAHA [59]
Humor detection
2021
es
2
Humor Detection
MeOffendEs [60]
Gender detection
2021
es
2
Author Profiling
MeOffendEs [60]
Offensiveness detection
2021
es
4
Toxicity and Harmful Language Detection
Rest-Mex [61]
Gender detection
2021
es-MX
3
Author Profiling
Rest-Mex [61]
Sentiment analysis
2021
es-MX
5
Sentiment and Emotion Analysis
VaxxStance [62]
Stance detection
2021
{eu, es}
3
Stance Detection
PAR-MEX [63]
Paraphrase detection
2022
es
2
Paraphrase Detection
Rest-Mex [64]
Sentiment analysis
2022
es-MX
5
Sentiment and Emotion Analysis
MentalRiskES [65]
Depression categorization
2023
es
4
Mental Health Detection
MentalRiskES [65]
Depression detection
2023
es
2
Mental Health Detection
MentalRiskES [65]
Eating disorder detection
2023
es
2
Mental Health Detection
HUHU [66]
Fatphobia detection
2023
es
2
Prejudice and Discrimination Detection
HUHU [66]
Humor detection
2023
es
2
Humor Detection
HUHU [66]
LGBTIQ prejudice detection
2023
es
2
Prejudice and Discrimination Detection
HUHU [66]
Racial prejudice detection
2023
es
2
Prejudice and Discrimination Detection
HUHU [66]
Women prejudice detection
2023
es
2
Prejudice and Discrimination Detection
DETESTS-Dis [67]
Stereotype detection
2024
es
2
Prejudice and Discrimination Detection
IberAuTexTification [68]
MGT attribution
2024
{en, es, eu, pt, ca, gl}
6
MGT Detection and Attribution
IberAuTexTification [68]
MGT detection
2024
{en, es, eu, pt, ca, gl}
2
MGT Detection and Attribution
General
PAWS [69, 70, 71]
Paraphrase Detection
2019
{es, gl, pt, ca}
2
Paraphrase detection
XLSum [72]
Text summarization
2021
{es, pt}
-
Text Summarization
Parafraseja [73]
Paraphrase detection
2022
ca
2
Paraphrase Detection
BEC [74]
Sentiment analysis
2024
eu
3
Sentiment and Emotion Analysis
BHTC [74]
Topic classification
2024
eu
12
Topic Classification
caBreu [71]
Text summarization
2024
ca
-
Text Summarization
ClinDiagnosES [75]
Topic classification
2024
es
8
Topic Classification
FMTODeu [74]
Intent classification
2024
eu
12
Intent Classification
HateCheck [76]
Hate speech detection
2024
pt
2
Toxicity and Harmful Lang Detection
Table 2: Industry-relevant tasks and datasets in IberBench. |L| refers to the number of labels or candidate answers if applicable. We indicate
language varieties in brackets. If no variety is specified, it means the source does not provide information about which varieties are included in the
dataset.
datasets are organized into categories and assessed for relevance to facilitate broader insights following evaluation.
Categories represent broad semantic groupings of tasks; for example, Gender detection and Age detection are both
subcategories of Author profiling. Relevance, on the other hand, differentiates between fundamental and industry-
relevant tasks. Fundamental tasks are those that an LLM must be able to perform in order to demonstrate proficiency
in language use, reasoning, and factual knowledge. Industry-relevant tasks, conversely, are those with economic sig-
nificance, such as detecting hate speech or machine-generated text for content moderation, and performing sentiment
analysis or author profiling for customer insights. Most industry-relevant tasks are sourced from workshops, while the
majority of fundamental tasks originate from established LLM benchmarks (designated in Tables 2 and 3 as “Gen-
eral” in the source column). This highlights two key points: (i) workshops are closely aligned with industry needs
of NLP-focused companies, and (ii) existing LLM benchmarks tend to overlook industry-relevant tasks in favor of
evaluating the fundamental capabilities of LLMs.
To complement the dataset descriptions, Table 4 presents total and aggregated statistics per category and relevance.
8

--- Page 9 ---

Source
Task
Subtask
Year
Language
|L|
Category
IberLEF
ADoBo [77]
Lexical borrowing chunking
2021
es
2
Lexical Analysis
General
TE-ca [78]
Textual entailment
2021
ca
2
Textual Entailment
OpenBookQA [79, 73]
Question answering
2022
{es, ca}
4
Question Answering
ARC [12, 73]
Question answering
2024
{eu, ca}
4
Question Answering
Belebele [44]
Reading comprehension
2024
{eu, es, pt, ca}
4
Reading Comprehension
CoLA [80, 81, 70]
Linguistic acceptability
2024
{es, gl, ca}
2
Linguistic Acceptability
COPA [12, 79, 71]
Commonsense reasoning
2024
{eu, es, ca}
2
Commonsense reasoning
EusExams [18]
Question answering
2024
{eu, es}
4
Question Answering
EusProficiency [18]
Proficiency evaluation
2024
eu
4
Proficiency Evaluation
EusReading [18]
Reading comprehension
2024
eu
-
Reading Comprehension
EusTrivia [18]
Question answering
2024
eu
4
Question Answering
EusTrivia [18]
Topic classification
2024
eu
5
Topic Classification
PIQA [12]
Commonsense reasoning
2024
eu
2
Commonsense Reasoning
QNLI [74]
Textual entailment
2024
eu
2
Textual Entailment
TELEIA [82]
Proficiency evaluation
2024
es
4
Proficiency Evaluation
XNLI [83, 70, 71]
Textual Entailment
2024
{es, gl, ca}
2
Textual entailment
XStoryCloze [70, 73]
Question answering
2024
{gl, pt, ca}
2
Question Answering
Table 3: Fundamental tasks and datasets in IberBench. |L| refers to the number of labels or candidate answers if applicable. We indicate language
varieties in brackets. If no variety is specified, it means the source does not provide information about which varieties are included in the dataset.
|D|
|S|
eu
ca
gl
pt
en
es
PE
UY
CR
AMB
CU
MX
ES
MGT Detection and Attribution
12
67.3
8.6
12.6
2.6
13.7
15.7
0
0
0
13.8
0
0
0
Author Profiling
4
54.4
0
0
0
0
0
0
0
0
52.2
0
2.2
0
Question Answering
10
43.6
18.7
3.2
1.5
1.5
0
0
0
0
18.7
0
0
0
Toxicity and Harmful Language Detection
9
23.9
0
0
0
3.7
0
0
0
0
19.7
0
0.6
0
Language Identification
1
18.4
0
0
0
0
0
0
0
0
18.4
0
0
0
Textual Entailment
5
14.9
0.2
7.1
5.0
0
0
0
0
0
2.5
0
0
0
Humor Detection
3
12.8
0
0
0
0
0
0
0
0
12.8
0
0
0
Text Summarization
3
12.2
0
0.3
0
7.2
0
0
0
0
4.7
0
0
0
Paraphrase Detection
6
12.1
0
6.0
2.0
2.0
0
0
0
0
2.0
0
0.1
0
Linguistic Acceptability
3
11.9
0
9.2
1.7
0
0
0
0
0
1.1
0
0
0
Prejudice and Discrimination Detection
7
9.6
0
0
0
0
0
0
0
0
9.6
0
0
0
Proficiency Evaluation
2
5.3
5.2
0
0
0
0
0
0
0
0.1
0
0
0
Reading Comprehension
5
3.9
1.2
0.9
0
0.9
0
0
0
0
0.9
0
0
0
Topic Classification
3
3.6
3.6
0
0
0
0
0
0
0
0.06
0
0
0
Commonsense Reasoning
4
3.3
2.3
0.5
0
0
0
0
0
0
0.5
0
0
0
Stance Detection
4
3.3
0.3
1.2
0
0
0
0
0
0
1.8
0
0
0
Irony and Sarcasm Detection
4
2.7
0
0
0
0
0
0
0
0
0.9
0.6
0.6
0.6
Sentiment and Emotion Analysis
10
26.4
1.3
0
0
0
0
1.4
1.4
1.4
2.5
0
16.7
1.7
Lexical Analysis
1
1.8
0
0
0
0
0
0
0
0
1.8
0
0
0
Intent Classification
1
1.1
1.1
0
0
0
0
0
0
0
0
0
0
0
Fake News Detection
1
0.6
0
0
0
0
0
0
0
0
0.66
0
0
0
Mental Health Detection
3
0.4
0
0
0
0
0
0
0
0
0.4
0
0
0
Industry NLP
70
247.1
13.2
20.1
4.6
26.6
15.8
1.4
1.4
1.2
139.6
0.6
20.1
2.3
Fundamental NLP
31
86.4
29.4
20.9
8.2
2.4
0
0
0
0
25.6
0
0
0
Total
101
333.5
42.6
41.0
12.8
29.0
15.8
1.4
1.4
1.2
165.2
0.6
20.1
2.3
Table 4: Statistics of IberBench. |D| and |S| refer to number of datasets and samples respectively. The remaining columns show the number of
samples per language in thousands. “AMB” stands for “ambiguous” and refers to potential mixes of language variations that are not explicitly
identified by dataset creators.
IberBench comprises 101 datasets, distributed across 22 categories, with over 333 thousand samples, which are widely
9

--- Page 10 ---

dispersed across 12 Iberian languages.10 Ninety-seven of these datasets are framed as text classification, 3 of them as
text generation, and 1 as sequence labeling.
Regarding languages, Spanish is the most represented, with 192.3 thousand samples, accounting for approximately
60% of the benchmark, followed by Basque and Catalan, which together represent around 12%. Galician is the least
represented, with only 4% of the total. Mexican (6.0%) and Spanish from Spain (0.6%) are the most represented
among the Spanish varieties, without considering the “ambiguous” variety (49.5%) that potentially contain mixed
variations. Other varieties including Peruvian, Uruguayan, Costa Rican, and Cuban, require more effort to generate
meaningful resources for the NLP scientific community and achieve better representation. Still, most Spanish varieties
are primarily included in a few task categories, such as Sentiment and Emotion Analysis, and Irony and Sarcasm
Detection.
Concerning task categories, the most populated ones are Sentiment and Emotion Analysis (7.9%), Machine-
Generated Text Detection and Attribution (20.2%), Author Profiling (16.3%), and Question Answering (13.1%). The
first three categories are mainly derived from the TASS, IberLEF, and PAN workshops, which have historically focused
on addressing these tasks across a wide range of Iberian languages. In contrast, Question Answering is almost entirely
composed of datasets from LLM benchmarks. The two categories with the most samples are Machine-Generated Text
(MGT) Detection and Attribution, and Author Profiling. The datasets used in these tasks are typically generated au-
tomatically, either by using LLMs to generate text or inferring user demographics from social media. Mental Health
and Fake News Detection stand out among the less populated task categories. Despite being critically important for
industry NLP, these categories are inherently complex, making it challenging to create datasets to study them effec-
tively. There is a high imbalance in terms of (task category, language) pairs. For instance, Mental Health Detection
only comprises data in Spanish but Sentiment and Emotion Analysis comprises data in near all Iberian language.
This implies that LLMs might appear weaker or stronger in cross-lingual and cross-task comparisons depending on
how well they perform on overrepresented or underrepresented combinations. We expect that in the future, novel and
comparable datasets across languages may arise, that can incrementally added into IberBench.
IberBench includes 70 datasets for industry-relevant tasks and 31 for fundamental ones. Of the total, 247.1 thou-
sand samples are from industry-relevant tasks, while 86.4 thousand are from fundamental tasks, representing 74%
and 26% of the total, respectively. It has been proven that recent LLMs demonstrate strong capabilities in natural
language understanding, generation, and knowledge. However, their use in industry-relevant tasks that matter most
to NLP-focused companies is still largely unexplored. Therefore, we consider these proportions to represent a bal-
anced trade-off between evaluating the language and knowledge capabilities of LLMs and assessing their practical
usefulness in real-world scenarios.
There are several areas for improvement where the Iberian NLP community should focus future efforts on dataset
creation. The task-language table is sparse, emphasizing the need to develop more datasets. Industry-relevant tasks
and certain Spanish varieties, particularly Peruvian, Uruguayan, and Costa Rican Spanish, show the most gaps. Addi-
tionally, we observe the absence of specific language varieties, such as Brazilian Portuguese and Argentinian Spanish.
Ninety-seven of the datasets included in IberBench are framed as text classification tasks, 3 as text generation (which
only include text summarization), and 1 as sequence labeling. These proportions reflect the greater difficulty involved
in creating text generation and sequence labeling datasets, as well as the complexities associated with their evaluation.
As a result, there is a clear need for more efforts to develop datasets for more diverse task types.
In this section, we have mainly discussed the retrospective collection of datasets. However, IberBench also facil-
itates prospective dataset collection. When the organization approves new datasets, a designated team member runs
the workflow outlined in this section. This process includes downloading the dataset, specifying a configuration file
to guide the normalization process,11 and uploading the processed dataset to the private HuggingFace repository.
3.4. LLM Evaluation
IberBench is designed to exclusively evaluate autoregressive LLMs. This choice is motivated by their substantial
flexibility in addressing a wide range of NLP tasks and their significant traction in both academic research and indus-
10We include English for two reasons. First, to leverage the efforts of the Iberian NLP community in creating English datasets. Second, because
English is spoken in Gibraltar, a region geographically connected to the Iberian Peninsula. Only English datasets created within Iberian evaluation
campaigns are included.
11We provide examples of configurations to normalize datasets at https://github.com/IberBench/dataset-preparation/tree/main/
configs
10

--- Page 11 ---

trial applications. The evaluation of an autoregressive LLM on a task T proceeds as follows. Let f : P × X →˜P
denote a verbalization function that formats an input x ∈X into a prompt template, where p ∈P is a prompt tem-
plate containing a task description—potentially including few-shot exemplars. Let D = {(x1, y1), . . . , (xn, yn) : xi ∈
X, yi ∈Y} denote a test dataset comprising input-output pairs, then a set of instantiated prompts is constructed as
S = {s1, . . . , sn : si = f(pi, xi) ∈˜P}. The LLM is then prompted with each si ∈S and generates a corresponding
output that is subsequently compared with the reference output yi. The nature of the generated output depends on
the type of task; in this work, we restrict our focus to text classification, text generation, and sequence labeling. For
classification tasks the label set is predefined, allowing the model to compute the likelihood of each candidate label.
The label with the highest likelihood is selected, as formalized in Equation 1,
ˆy = argmax
y∈Y
|y|
Y
j=0
pLLM(y j | si, y<j)
(1)
where pLLM(y j | si, y<j) denotes the probability assigned by the LLM to the j-th token of the label, conditioned on
the instantiated prompt si and the preceding tokens of the label. For generation tasks, we employ greedy decoding to
ensure reproducibility. Under this decoding strategy, the LLM generates l tokens in an output sequence ˆy = (ˆy1, . . . , ˆyl),
where each token ˆy j is produced according to Equation 2,
ˆy j = argmax
w∈V
pLLM(w | si, ˆy< j)
(2)
where V denotes the vocabulary of the LLM. This formulation is employed in our evaluation pipeline for both open-
ended text generation tasks such as summarization, and for sequence labeling tasks that follow the annotation scheme
outlined in Section 3.3. In open-ended text generation, the LLM continues generating tokens until an end-of-sequence
token is produced, whereas in sequence labeling tasks, generation halts upon emitting the <response> tag.
Once the outputs for all input texts are generated by the LLM, we apply standard evaluation metrics to assess
model performance. For classification tasks, we report the Macro-F1 score to mitigate the impact of label imbalance
in the test set. For generation tasks, we adopt ROUGE-1 [84], which measures unigram overlapping between the
generated outputs and the reference texts. In the absence of artifact-free, perfectly human-aligned, and efficient
automatic evaluation metrics for text summarization [85], we opt for ROUGE-1 due to its widespread use in prior
LLM benchmarks for evaluating text generation capabilities [11]. For sequence labeling tasks, we report the F1 score
as computed by the seqeval library [86], a widely adopted tool for evaluating model performance on chunking tasks.
All evaluations in IberBench are conducted using lm-eval-harness, a well-established, extensively tested, open-
source framework for LLM evaluation. This framework has served as the evaluation backbone for numerous leader-
boards, becoming the reference framework in the scientific community due to its simplicity and flexibility. It facili-
tates the evaluation of LLMs from various providers with minimal effort, requiring only a YAML configuration file to
specify the dataset, prompt, and generation hyperparameters,12 supporting a wide range of setups and hardware con-
figurations. For IberBench, we adapted lm-eval-harness for three primary purposes: managing sequence-labeling
tasks, enabling incremental evaluation through caching, and supporting on-premise execution.
To evaluate sequence-labeling tasks, (i) we designed a custom annotation schema, (ii) implemented label recon-
struction from generations, (iii) integrated the seqeval metric into the framework, and (iv) prepared YAML configu-
ration files and guidelines for its application.13 While we store all LLM evaluation requests and results in HuggingFace
repositories, lm-eval-harness does not natively interact with our results datasets and re-computes the results each
time a task is executed with an LLM. This is not desirable for incremental evaluation, and we address it by developing
custom evaluation code within lm-eval-harness that (i) identifies models pending evaluation, including both new
models and existing ones that have not been evaluated with recently added tasks, (ii) checks which tasks have already
been computed by a model, (iii) runs the model only on tasks not yet evaluated, and (iv) caches the results in Hugging-
12We release all the prompts we use to evaluate LLMs at https://github.com/IberBench/iberbench-evaluation/tree/main/lm_
eval/tasks/iberbench
13We show an example of YAML for a sequence-labeling task at https://github.com/IberBench/iberbench-evaluation/blob/main/
lm_eval/tasks/iberbench/iberlef-adobo-lexical_borrowing_chunking-2021-spanish.yaml
11

--- Page 12 ---

Face repositories.14 Finally, most of the leaderboards hosted on HuggingFace rely on the lm-eval-harness pipeline
integrated into HuggingFace’s servers, which are based on CPU. This setup is insufficient for evaluating LLMs with
large parameter sizes at scale. Instead, IberBench performs evaluations on-premise, on a custom server equipped with
two 48GB A6000 Nvidia GPUs, evaluating unquantized models up to 14 billion parameters in approximately 12 hours
per model.
The organization is responsible for running the custom evaluation code on-premise whenever a batch of models
or datasets is approved. For a new model, the evaluation script is executed, automatically assessing the model across
all existing datasets. For a new dataset, the organization creates a YAML configuration file and runs the evaluation
module, which updates the results of all existing models with the new dataset.
4. Evaluation
We conducted an extensive evaluation of multilingual LLMs, including those specialized on some Iberian lan-
guages, on the IberBench benchmark. This section details the models assessed so far, presents the evaluation results,
and discusses the key insights derived from the analysis.
4.1. Models
The ecosystem of LLMs—particularly high-quality ones—for Iberian languages remains limited. The majority of
existing models rely on further pre-training of multilingual LLMs to improve language adaptation, or on enhancing
alignment with human preferences in the target languages through supervised fine-tuning and reinforcement learning
techniques [87, 88]. Only a small number of models have been pre-trained from scratch with Iberian languages on
mind, most notably Salamandra [21] and EuroLLM [22].
In IberBench we aim to evaluate a broad spectrum of LLMs, which include (i) multilingual LLMs not specialized
in Iberian languages that are close to the state of the art in English, (ii) LLMs pre-trained from scratch on most Iberian
languages, and (iii) LLMs obtained by adapting existing multilingual models to one or more Iberian languages. For the
first group, we include Microsoft’s phi-4 [20] and phi-4-mini-instruct [89], Meta’s Llama 3.1 and 3.2 families
[3], Alibaba’s Qwen 2.5 family [4], and Mistral-7B-Instruct-v0.3 [90].15 In the second group, we include
Salamandra [21] and EuroLLM [22] families. For the third group, we include RigoChat-7b-v2 for Spanish [93],
Latxa-Llama-3.1-8B-Instruct for Basque [18], CataLlama-v0.2-Instruct-SFT for Catalan [94], sabia-
7b for Portuguese [95], and Aitana-6.3B for Catalan/Valencian [96]. The selected collection encompasses both
base models pre-trained solely for causal language modeling and instruction-tuned models designed for instruction
following and conversational tasks. Model sizes range from 100 million to 14 billion parameters, covering scenarios
with low to moderate computational requirements for deployment and inference.
Table 5 provides an overview of the LLMs evaluated within IberBench. Of the models evaluated, 78.3% are
chat-based, while 21.7% are base models. In terms of parameter size, 47.8% of the models fall within the 0.1-5
billion parameter range, 47.8% within 5.1-10 billion parameters, and only 4.4% within 10.1-15 billion parameters.
All the LLMs, except for gpt2 and gemma-2-2b-it, support at least Spanish and English, with 82.6% also covering
Portuguese. The most widely covered co-official language in Spain is Catalan, included in either pre-training or fine-
tuning by 34.8% of the models, followed by Galician (26.1%), and Basque (13.0%). None of the LLMs specifically
target Spanish varieties from Ibero-America, or this information is not reported in the source publication.
We evaluate these LLMs in a zero-shot setting, i.e., without providing any in-context examples. While few-shot
learning can enhance performance on certain tasks, the effects of factors such as the selection, quality, ordering,
format, and quantity of examples remain subjects of ongoing debate [97]. Furthermore, few-shot prompting is not yet
a widespread practice in industry, partly since many non-technical users are unfamiliar with this prompting technique
and because obtaining realistic examples can be challenging for tasks such as depression detection. To maintain
consistency across tasks, better reflect real-world scenarios, and assess the capabilities acquired during pre-training
14The evaluation script for incremental evaluation can be accessed at https://github.com/IberBench/iberbench-evaluation/blob/
main/scripts/iberbench/eval_iberbench.py
15We also included gpt2 [91] and gemma-2-2b-it [92] as functional baselines. They were trained exclusively on English and thus serves as
low-bar baselines for assessing the relative performance of more recent models on other Iberian languages.
12

--- Page 13 ---

Model Name
Type
Num. Params (billions)
Pre-training Languages
Fine-tuning Languages
phi-4 [20]
14.1
es, en, pt
EuroLLM-9B-Instruct [22]
9.1
es, en, ca, pt, gl
es, en, ca, pt, gl
EuroLLM-9B [22]
9.1
es, en, ca, pt, gl
-
CataLlama-v0.2-Instruct-SFT [94]
8.0
es, en, pt
ca
Llama-3.1-8B-Instruct [3]
7.5
es, en, pt
es, en, pt
Latxa-Llama-3.1-8B-Instruct [18]
7.5
es, en, pt
eu
Qwen2.5-7B-Instruct [4]
7.1
es, en, pt
RigoChat-7b-v2 [93]
7.1
es, en, pt
es
Mistral-7B-Instruct-v0.3 [90]
7.1
es, en
salamandra-7b-instruct [21]
6.7
es, en, ca, pt, gl, eu
es, en, ca, pt, gl, eu
sabia-7b [95]
6.7
es, en, pt
-
Aitana-6.3B [96]
6.3
es, en, ca
-
Qwen2.5-3B-Instruct [4]
3.1
es, en, pt
Llama-3.2-3B-Instruct [3]
3.2
es, en, pt
es, en, pt
phi-4-mini-instruct [89]
3.8
es, en, pt
gemma-2-2b-it [92]
2.6
en
en
salamandra-2b-instruct [21]
1.7
es, en, ca, pt, gl, eu
es, en, ca, pt, gl, eu
EuroLLM-1.7B-Instruct [22]
1.7
es, en, ca, pt, gl
es, en, ca, pt, gl
EuroLLM-1.7B [22]
1.7
es, en, ca, pt, gl
-
Qwen2.5-1.5B-Instruct [4]
1.5
es, en, pt
Llama-3.2-1B-Instruct [3]
1.2
es, en, pt
es, en, pt
Qwen2.5-0.5B-Instruct [4]
0.5
es, en, pt
gpt2 [91]
0.1
en
-
Table 5: LLMs evaluated in IberBench. Includes the model name, type, number of parameters in billions, and Iberian languages included in the
pre-training and fine-tuning mixtures.
indicates base models solely pre-trained via causal language modeling;
marks models further fine-
tuned for instruction-following or chat tasks;
denotes cases where training details are unspecified in the source. Fine-tuning languages for base
models are marked as “-”, since no fine-tuning has been performed on these models. All LLMs can be accessed in the HuggingFace Hub searching
by model name.
and fine-tuning without relying on pattern matching from provided examples, we opted to evaluate all LLMs in a zero-
shot setting, with the only exception being sequence-labeling tasks. For these tasks, a few examples are necessary to
guide the model in properly formatting the output sequences, and we used three shots for this purpose.
To provide a more grounded evaluation of the results obtained with LLMs, we compare their performance against
random baselines. For classification tasks, the random baseline assigns a label randomly, following a uniform distri-
bution. In generation tasks, the random baseline’s prediction consists of two randomly selected sentences from the
context (e.g., a document in text summarization) joined by a whitespace. For sequence-labeling tasks, the random
baseline’s prediction for an instance is generated by shuffling the reference sequence of labels.
As part of the IberBench release, we evaluated a selected set of LLMs consisting of the most prominent models for
Iberian languages. Users also have the option to request the evaluation of additional LLMs for through the leaderboard
interface.
4.2. Results
We analyze LLM performance across multiple dimensions, including overall performance and performance per
task category, relevance, languages, and model types.
4.2.1. Overall Model Performance
We aim to identify which models are most competitive overall across tasks and languages in IberBench. To do
this, we present the averaged performance across all datasets and languages together with model sizes in Figure 3.
13

--- Page 14 ---

0
2B
4B
6B
8B
10B
12B
14B
25
30
35
40
45
Aitana
CataLlama
EuroLLM
Latxa
Llama-3.1
Llama-3.2
Mistral
Phi
Qwen2.5
RigoChat
Gemma
GPT2
Sabia
Salamandra
Num. Parameters
Performance
Random
Figure 3: Performance per model size (number of parameters), averaged across all the languages and tasks. Legend shows model families, e.g., the
Llama-3.2 family includes Llama-3.2-1B-Instruct and Llama-3.2-3b-Instruct, which are plotted with the same marker and color. The
random baseline is shown as horizontal line.
Base
Chat
25
30
35
40
45
Model Type
Performance
Figure 4: Averaged performance per model type.
The top-3 LLMs are all from the Qwen-2.5 family. Qwen-2.5-7b-Instruct dominates the benchmark with a mean
score of 46.8%, followed closely by RigoChat-7b-v2 with 46.7%, and Qwen-2.5-3b-Instruct with 45.9%. These
models are among the more recent in the ecosystem, with RigoChat-7b-v2 being a fine-tuned version of Qwen-
2.5-7b-Instruct optimized for Spanish. The Qwen-2.5 family is also one of the top-performing models in other
multilingual benchmarks [13, 9].
Fine-tuning for language specialization can harm performance in other Iberian languages. We observe this behav-
ior through RigoChat-7b-v2 reporting better results than the original Qwen-2.5-7b-Instruct model. However,
RigoChat-7b-v2 performs slightly worse overall than Qwen-2.5-7b-Instruct. A similar observation can be done
by comparing Latxa-Llama-3.1-8B-Instruct, an LLM optimized for Basque, with its base model Llama-3.1-
8b-Instruct, which suggests that further specialization in a single language harms the performance of the model on
other Iberian languages.
Models from 3.1 to 10 billion parameters dominate the leaderboard. The best-performing models are primarily con-
centrated in the 3.1–10B parameter range. Models with fewer than 3B parameters, as well as phi-4 (14B), often
underperform relative to others. Based on scaling laws [98], we expect that larger models will eventually outperform
14

--- Page 15 ---

the current LLMs in the benchmark. In fact, scaling laws hold within families, e.g., salamandra-7b-Instruct
performs better overall than salamandra-2b-Instruct. The same behavior is observed in Llama-3.2, Qwen-2.5,
and EuroLLM families.
European LLMs fall short compared to popular multilingual LLMs. On average, European flagship models pre-
trained from scratch with a focus on Iberian languages—such as salamandra-7B-Instruct and EuroLLM-9B-
Instruct— perform on par with, or slightly below, models like Qwen-2.5-7B-Instruct, Qwen-2.5-3B-Instruct,
and Llama-3.1-8B-Instruct, despite having comparable or larger parameter counts. Similarly, the smaller vari-
ants—salamandra-2B-Instruct and EuroLLM-1.7B-Instruct—fail to outperform Llama-3.2-1B-Instruct,
even though they are slightly larger. Notably, none of these small models achieve better results than gemma-2-2b-it,
despite it being an English monolingual model.
LLMs focused in Iberian languages are competitive only if they are instruction-tuned. Among the models that have
been further pre-trained or fine-tuned from existing LLMs with a focus on specific Iberian languages—such as
Aitana-6.3B, sabia-7B, CataLlama-v0.2-Instruct-SFT, Latxa-Llama-3.1-8B-Instruct, and RigoChat-
7B-v2—only the latter three demonstrate competitive performance relative to the best-performing models. As evi-
denced in Figure 4, this disparity may be attributed to the fact that Aitana-6.3B and sabia-7B are base models,
which generally underperform compared to instruction-tuned models.
It is hard to beat the random baseline. Thirty-nine percent of the models performed below the random baseline.
Among these, we identified all the base models and several instruction-tuned models with fewer than 2B parame-
ters, including Llama-3.2-1B-instruct, salamandra-2B-instruct, Qwen2.5-0.5B-instruct, and EuroLLM-
1.7B-instruct. This emphasizes the significance of model scale for instruction-tuned models: only those exceeding
2B parameters demonstrate competitive performance. Base models, even those surpassing the 6B parameter thresh-
old, are not competitive. The difference between the best-performing LLM and the random baseline is approximately
10%, highlighting that IberBench is still far from being adequately solved.
4.2.2. Performance per Task
We analyze performance by task to gain a better understanding of how well the LLMs handle each of them,
specifically identifying tasks that are far from being solved and highlighting those that are better addressed by the
models. Since the landscape of tasks in IberBench is broad, we focus on task categories and we analyze the results
across languages and LLMs, presenting the results per task category in Figure 5.
LLMs perform better in fundamental tasks than on industry-relevant ones. The highest performances and medians
are observed in Commonsense Reasoning, Question Answering, Reading Comprehension, Textual Entailment, and
Paraphrase Detection. From Table 3 we see that most of these tasks are fundamental, and dominate existing bench-
marks [12]. In contrast, tasks with lower medians are more often industry-relevant, particularly Intent Classification,
Stance Detection, Author Profiling, Summarization, and MGT Detection and Attribution. This performance gap is
more clearly illustrated in Figure 6, which shows that models struggle more with industry-relevant tasks than with
fundamental ones. This highlights the usefulness of IberBench, and suggests that benchmarks should shift their focus
to other types of tasks to more realistically assess LLM capabilities.
Sequence-labeling tasks (for lexical analysis) remain challenging for LLMs. Results on Lexical Analysis, which
involves a single task of detecting English borrowings in Spanish texts, are among the lowest across the benchmark,
alongside those of Intent Classification. The best result in this task is 31.98% Macro F1, achieved by phi-4, while the
other models do not exceed 20%, with most scoring below 10% (and half of these below 1%). This suggests that (i)
sequence-labeling tasks may not be well-suited for LLMs, and (ii) models with fewer than 14B parameters struggle to
follow the instruction to generate text in the expected annotation schema. It remains uncertain whether larger models
will be able to address the task effectively.
15

--- Page 16 ---

Intent
Classiﬁcation
Mental Health
Detection
Prejudice and
Discrimination
Topic
Classiﬁcation
Author
Proﬁling
Stance
Detection
Toxicity and 
Harmful
Language
Fake News
Detection
Humor
Detection
Language
Identiﬁcation
0
20
40
60
80
Lexical
Analysis
Irony and
Sarcasm
Sentiment and
Emotion Analysis
MGT Detection
and Attribution
Summarization
Paraphrase
Detection
0
20
40
60
80
Reading
Comprehension
Question
Answering
Commonsense
Reasoning
Linguistic
Acceptability
Textual
Entailment
Proﬁciency
Evaluation
Performance
Performance
Figure 5: Performance per task category across all models and languages. The random baseline for each category is marked with a black cross.
The random baseline is surpassed by far in fundamental tasks and it is hard to beat in some industry-relevant tasks.
In 85.7% of the fundamental tasks, the median results surpass the baseline, with some tasks, such as Reading Compre-
hension and Question Answering, showing the largest margins across all tasks. In industry-relevant tasks, the median
surpasses the random baseline 60% of the time, with a particularly large margin in Language Identification. Stance
Detection, Fake News Detection, Author Profiling, Summarization, and MGT Detection and Attribution are the most
challenging tasks. In MGT tasks, the baseline outperforms all the LLMs, highlighting the challenge for LLMs in
identifying and attributing text generated by other LLMs.
Intent classification is hard... in Basque. Intent classification is a traditional, relatively simple task compared to
more complex tasks such as summarization, mental health detection, or fake news detection. However, the LLMs’
performances on this task are among the lowest in the benchmark. Notably, the Intent Classification category consists
of only a single dataset in Basque. This suggests that most models struggle with Basque, a point we will further explore
in our analysis per language. Despite this, even the best model achieves only around 20% Macro F1. Interestingly,
this model is sabia-7b, an LLM further pre-trained for Portuguese.
What does it mean to “break the ice”? LLM: It is a song by Britney Spears. Since LLMs can generate human-like
text and handle complex classification tasks, one might expect it to accurately identify the language and demonstrate
a high level of proficiency. This does not hold, as Language Identification, Proficiency Evaluation, and Linguistic
Acceptability remain challenging for LLMs. This is particularly notable in the case of Proficiency Evaluation, which
is framed as a question answering task requiring models to select the correct answer from proficiency exam questions.
Despite this similarity, the median performance in Proficiency Evaluation is around 30%, while the median perfor-
mance in Question Answering tasks aimed to measure knowledge capabilities is around 50%. We attribute these
results to the specific challenges posed by the data. In Proficiency Evaluation, the category is dominated by Basque
instances, a language that most models struggle with. For Language Identification, the difficulty likely stems from the
16

--- Page 17 ---

Fundamental
Industry
10
20
30
40
50
60
70
80
90
Relevance
Performance
Figure 6: Performance in fundamental and industry-relevant tasks, averaged across all the languages and models.
domain, as all texts in this category are tweets: short, often informal messages that include slang, abbreviations, and
non-standard writing styles.
Shared task participants still lead, but LLMs are narrowing the gap. Since all the tasks in IberBench originate from
existing publications, we compare the LLMs’ performance at the task category level with the best results reported
in the literature. We focus only on task categories that include datasets from shared tasks. For this comparison, we
average the performance of the best published models for the tasks within each task category and contrast them with
the LLM results presented in Figure 5. In some tasks considered to be largely solved, such as Sentiment Analysis
and Emotion Detection, the performance gap remains notable: the best LLM achieves 48.83%, while the average
of the best published results reaches 61.87%. Large differences are also observed in Humor Detection (72.67% vs.
84.26%) and Lexical Analysis (31.98% vs. 80.42%). In other tasks, such as Fake News Detection (75.04% vs.
76.66%), Irony and Sarcasm Detection (62.92% vs. 67.87%), and Mental Health Detection (62.32% vs. 68.76%),
LLMs still underperform compared to reported models, but the margins are smaller. It is important to note that our
evaluation is conducted in a zero-shot setting, whereas the best published results are obtained with models fine-tuned
on thousands of examples. We expect that under few- or many-shot conditions, the evaluated LLMs will outperform
the best published results.
So far, we have discussed how well LLMs address the tasks in IberBench. However, we have not explicitly shown
the ranking of LLMs per task category. For completeness, we present this ranking in Figure B.10 of the Appendix.
4.2.3. Performance per Iberian language
We examine the performance of LLMs across Iberian languages, focusing on their challenges, distinctions, and
unique characteristics, as well as the distribution of LLM performances across languages. We analyze (i) overall
results per language averaged across LLMs and tasks (shown in Figure 7), and (ii) LLM results per language and
Spanish variety averaged across tasks (shown in Figures 8 and 9, respectively).
English poses a unique challenge. Given that the datasets have been sourced mainly from evaluation campaigns with a
focus on Iberian languages, the only category with English data is Machine Generated Text Detection and Attribution,
which is very difficult for LLMs to solve without tailored techniques. As shown in Figure 7, a random baseline easily
beats all the models.
Galician and Basque present greater challenges than other languages. As shown in Figure 8, the performances in
Catalan, Portuguese, and Spanish are remarkably better than the random baseline, with many models outperforming it
by large margins. In contrast, while the top models in Galician outperform the random baseline by a large margin, only
34% of models exceed it. In Basque, only three models barely beat the random baseline. This can be attributed to (i)
the imbalance in task difficulty across languages, (ii) differences in language characteristics and (iii) differences in the
amount of available resources for LLM training. Spanish, Portuguese, Catalan, and Galician are Romance languages
17

--- Page 18 ---

20
30
40
50
60
English
Spanish
Galician
Portuguese
Catalan
Basque
20
30
40
50
60
Mexico
Uruguay
Costa Rica
Cuba
Peru
Spain
Performance
Performance
Figure 7: Performance per language and Spanish variety averaged across LLMs and tasks. For clarity, we remove the “ambiguous” Spanish variety.
0
20
40
60
Aitana-6.3B
RigoChat-7b-v2
sabia-7b
CataLlama-v0.2-Instruct-SFT
EuroLLM-9B-Instruct
EuroLLM-9B
EuroLLM-1.7B-Instruct
EuroLLM-1.7B
Mistral-7B-Instruct-v0.3
Latxa-Llama-3.1-8B-Instruct
gemma-2-2b-it
Llama-3.2-3B-Instruct
Llama-3.2-1B-Instruct
Llama-3.1-8B-Instruct
Phi-4-mini-instruct
phi-4
Qwen2.5-7B-Instruct
Qwen2.5-3B-Instruct
Qwen2.5-1.5B-Instruct
Qwen2.5-0.5B-Instruct
gpt2
salamandra-7b-instruct
salamandra-2b-instruct
0
20
40
60
0
20
40
60
Aitana-6.3B
RigoChat-7b-v2
sabia-7b
CataLlama-v0.2-Instruct-SFT
EuroLLM-9B-Instruct
EuroLLM-9B
EuroLLM-1.7B-Instruct
EuroLLM-1.7B
Mistral-7B-Instruct-v0.3
Latxa-Llama-3.1-8B-Instruct
gemma-2-2b-it
Llama-3.2-3B-Instruct
Llama-3.2-1B-Instruct
Llama-3.1-8B-Instruct
Phi-4-mini-instruct
phi-4
Qwen2.5-7B-Instruct
Qwen2.5-3B-Instruct
Qwen2.5-1.5B-Instruct
Qwen2.5-0.5B-Instruct
gpt2
salamandra-7b-instruct
salamandra-2b-instruct
Performance
Spanish
Basque
English
Portuguese
Galician
Catalan
Figure 8: LLM performances in Iberian languages, averaged across tasks. Vertical lines denote the random baseline.
18

--- Page 19 ---

0
20
40
60
Aitana-6.3B
RigoChat-7b-v2
sabia-7b
CataLlama-v0.2-Instruct-SFT
EuroLLM-9B-Instruct
EuroLLM-9B
EuroLLM-1.7B-Instruct
EuroLLM-1.7B
Mistral-7B-Instruct-v0.3
Latxa-Llama-3.1-8B-Instruct
gemma-2-2b-it
Llama-3.2-3B-Instruct
Llama-3.2-1B-Instruct
Llama-3.1-8B-Instruct
Phi-4-mini-instruct
phi-4
Qwen2.5-7B-Instruct
Qwen2.5-3B-Instruct
Qwen2.5-1.5B-Instruct
Qwen2.5-0.5B-Instruct
gpt2
salamandra-7b-instruct
salamandra-2b-instruct
0
20
40
60
0
20
40
60
Aitana-6.3B
RigoChat-7b-v2
sabia-7b
CataLlama-v0.2-Instruct-SFT
EuroLLM-9B-Instruct
EuroLLM-9B
EuroLLM-1.7B-Instruct
EuroLLM-1.7B
Mistral-7B-Instruct-v0.3
Latxa-Llama-3.1-8B-Instruct
gemma-2-2b-it
Llama-3.2-3B-Instruct
Llama-3.2-1B-Instruct
Llama-3.1-8B-Instruct
Phi-4-mini-instruct
phi-4
Qwen2.5-7B-Instruct
Qwen2.5-3B-Instruct
Qwen2.5-1.5B-Instruct
Qwen2.5-0.5B-Instruct
gpt2
salamandra-7b-instruct
salamandra-2b-instruct
Performance
Costa Rica
Spain
Uruguay
Mexico
Cuba
Peru
Figure 9: Model performance in Spanish varieties. Vertical lines denote the random baseline.
that share many common features. However, despite recent efforts [73, 70], the latter two languages, particularly
Galician, are under-resourced in comparison. Galician is particularly interesting due to its similarity to Portuguese
[99], meaning that language understanding and generation capabilities developed for Portuguese are expected to
transfer to Galician as well. This is evident in the performance of sabia-7b, a base model further pre-trained for
Portuguese. The performance of this model is very similar in both Portuguese and Galician, while it shows more
variation in other languages.
Model rankings are remarkably consistent across languages and Spanish varieties. That is, a model A that outper-
forms another model B in a given language L1, it typically does so in another language L2 as well. To confirm this we
compute Kendall’s τ and Spearman’s ρ among the performance distributions for every pair of languages and varieties.
In all cases, we find τ ≈ρ > 0.99 with p < 1 × 10−11, underscoring the strong and statistically significant agreement
in model rankings.
The curious case of Basque. From Figure 8 we find that Latxa-Llama-3.1-8B-Instruct, a model obtained by fur-
ther pre-training Llama-3.1-8b-Instruct with Basque data, performs similarly to salamandra-7b-Instruct, a
multilingual LLM focused on Iberian languages. These three LLMs are the only ones that surpass the random base-
line. Further pre-training for Basque improves performance in Basque, but this does not hold for Spanish, where
19

--- Page 20 ---

RigoChat-7b-v2 does not outperform Qwen-2.5-7B-Instruct in Spanish. Interestingly, further pre-training with
a focus on Basque leads to catastrophic forgetting in other languages, as seen with Latxa-Llama-3.1-8B-Instruct:
while it improves on the performance of Llama-3.1-8B-Instruct in Basque, it scores worse in every other lan-
guage. In contrast, this effect is not observed when fine-tuning Qwen-2.5-7B-Instruct for Spanish (RigoChat-7b-
v2). This highlights the distinctive characteristics of the Basque language in comparison to other Iberian languages:
it lacks known linguistic relatives and is unrelated to the surrounding languages of the Iberian Peninsula [100].
Two distinct types of Spanish varieties. We identify two groups of varieties in Figure 7, (i) varieties with low spread,
lower median, and many outliers such as Peruvian, Costa Rican and Uruguayan, and (ii) varieties with higher spread,
higher median, and no outliers like Cuban, Mexican and Spanish from Spain. From Figure 9 we see that some LLMs
such as EuroLLM-9B or Qwen-2.5-0.5b-Instruct generally perform better in the latter group than in the former.
Notably, Cuban and Spanish from Spain are the only varieties where the median does not surpass the baseline.
Multilingual models (including basque-tuned ones) outperform Spanish-specific models across Spanish varieties. As
shown in Figure 9, RigoChat-7b-v2 is outperformed by a multilingual model in every Spanish variety. For instance,
Llama-3.1-8B-Instruct surpasses it in Mexican and Cuban, while salamandra-2b-Instruct performs better in
Uruguayan, Costa Rican, and Peruvian. Interestingly, Latxa-Llama-3.1-8B-Instruct ranks as the top-performing
model in every Spanish variety except for Mexican and Cuban, often improving upon Llama-3.1-8B-Instruct.
Despite showing signs of catastrophic forgetting in other languages, this improvement suggests that Latxa’s fine-tuning
may enhance either (i) generalization across Spanish varieties or (ii) performance on sentiment analysis. Notably,
many of the Spanish varieties where Latxa excels contain only a single dataset focused on this task. From the model
rankings per task category shown in Figure B.10 of the Appendix we see that Latxa-Llama-3.1-8B-Instruct
ranks second in Sentiment and Emotion Analysis, making the latter explanation more likely.
Akin to the ranking of LLMs per task from the previous section, we present the ranking of LLMs per Iberian
language in Figure B.11 of the Appendix.
5. Conclusion
This work introduces IberBench, a multilingual and multitask benchmark designed to evaluate LLMs across
Iberian languages in fundamental language skills and industry-relevant applications. Our benchmark focuses on the
linguistic diversity of the Iberian Peninsula and Ibero-America, covering Spanish, Portuguese, Catalan, Basque, Gali-
cian, and English, as well as Spanish varieties such as Mexican, Uruguayan, Peruvian, Costa Rican, and Cuban. This
scope enables more comprehensive and representative evaluations of LLMs in the underrepresented context of Iberian
languages.
IberBench integrates 101 datasets compiled from evaluation campaigns and recent benchmarks, spanning 22 dis-
tinct task categories. To date, we have evaluated 23 LLMs ranging from 100 million to 14 billion parameters, covering
models that are monolingual and multilingual, base models and models fine-tuned for chat applications, and more.
We find that (i) LLMs struggle with industry-relevant tasks compared to fundamental language tasks, which domi-
nate existing benchmarks, (ii) Galician and Basque present greater challenges than other languages, (iii) some tasks
like lexical borrowing detection, intent classification, and machine-generated text detection remain largely unsolved,
with top-performing LLMs barely surpassing a random guesser, and (iv) in other tasks such as sentiment analysis,
humor detection, and fake news detection, LLMs are better than the random baseline but worse than most shared task
submissions.
IberBench offers a complete open-source infrastructure for benchmarking, covering every stage from dataset pro-
cessing and hosting to the incremental evaluation of LLMs. Evaluation results are integrated into a public leaderboard
hosted on Hugging Face, providing easy access and fostering transparency. By open sourcing the IberBench pipeline,
we hope to encourage community collaboration, reproducible research, and the responsible development of Iberian
language technologies.
As future work, we aim to benchmark new LLMs on IberBench and progressively extend it with additional datasets
as new evaluation campaigns with a focus on Iberian languages are launched within the NLP research community.
20

--- Page 21 ---

Limitations and Ethical Considerations
While IberBench provides a robust and flexible platform for evaluating language models in Iberian languages, it is
important to highlight its limitations, especially related with data, modeling, evaluation, and computational resources.
The data that comprises IberBench was collected from existing LLM benchmarks, and shared tasks from NLP
workshops. By gathering these datasets, IberBench includes a diverse set of Iberian languages, domains and tasks.
This also means that (i) IberBench is constrained to the data that is available from these sources with a permissive
license, or where dataset authors have granted us explicit permission for use, (ii) it is primarily comprised of clas-
sification tasks, few generation tasks only including summarization, and one sequence labeling, and (ii) language
varieties with a large number of speakers are underrepresented, as examples such as Argentinian Spanish or Brazil-
ian Portuguese are not covered. Moreover, some datasets may contain artifacts or inherent biases that can influence
evaluation results. This can be likely (i) when labels or texts are obtained automatically, such as in author profiling
or MGT detection tasks, (ii) where annotation is inherently difficult, like in mental health detection tasks, or (iii) it
is subjective, e.g. in humor detection tasks. Similarly to existing benchmarks, the task types and distributions across
languages are imbalanced. All of these aspects can introduce bias to the evaluations and analyses, particularly when
seeking fine-grained insights across languages or task categories.
The main modeling limitations stem from the prompting strategy. We employ a single prompt per task, designed
according to established best practices. However, it is well known that LLMs are highly sensitive to the prompt
phrasing and formatting. Alternative prompts could potentially yield better performance, particularly for sequence
labeling tasks where the annotation schema may not align naturally with the format-following capabilities of an LLM.
Nevertheless, exploring a wide range of prompt variations is not feasible within our current experimental framework.
Another important limitation is our exclusive use of zero-shot evaluation—except for sequence-labeling tasks—which
may underestimate model performance. Although few-shot prompting can improve results, its effectiveness is influ-
enced by various factors and remains a topic of debate. It is not yet widely adopted in practical applications due to
data challenges, which motivates our choice of zero-shot evaluation to ensure consistency across tasks and better align
IberBench with real-world usage scenarios.
The evaluation metrics used in IberBench also present drawbacks, particularly for assessing open-ended text gen-
eration. In such cases, we adopt ROUGE-1, following its use in other established benchmarks. However, ROUGE-1
focuses solely on unigram lexical overlap and does not capture other important dimensions of generation quality, such
as fluency, coherence, hallucination, abstractiveness, or factual consistency.
The current evaluation process is restricted by the availability of computational and financial resources, which
may bottleneck the frequency and scale at which new models can be assessed. Our first release of IberBench includes
evaluations of LLMs with up to 14 billion parameters in 16-bit precision, excluding larger and closed-source LLMs.
The deployment and use of benchmark evaluations in NLP entail several ethical considerations too. First, the
selection of datasets and tasks can introduce biases if certain languages, varieties, or demographic groups are under-
represented. To mitigate this we strive to include a diverse range of tasks and data sources, although limitations in
access and permissions currently hinder this goal. Additionally, publishing model results and logs involves handling
potentially sensitive data and outputs. We ensure that only publicly available and ethically sourced datasets are used
in evaluations. We also avoid the inclusion of tasks that may contain harmful or discriminatory data unless they are
explicitly designed to moderate this behavior.
Acknowledgements
We would like to express our sincere gratitude to the organizers of TASS, IberEVAL, IberLEF, and PAN workshops
as well to the creators of existing LLM benchmarks in Iberian languages for providing access to the datasets included
in this benchmark. The work from Symanto has been partially funded by the Instituto Valenciano de la Competitividad
Empresarial (IVACE) under the grant IMINOK/2023/122.
21

--- Page 22 ---

References
[1] T. Eloundou, S. Manning, P. Mishkin, D. Rock, Gpts are gpts: An early look at the labor market impact potential of large language models
(2023). arXiv:2303.10130.
[2] G. Yenduri, M. Ramalingam, G. C. Selvi, Y. Supriya, G. Srivastava, P. K. R. Maddikunta, G. D. Raj, R. H. Jhaveri, B. Prabadevi, W. Wang,
A. V. Vasilakos, T. R. Gadekallu, Gpt (generative pre-trained transformer)— a comprehensive review on enabling technologies, potential
applications, emerging challenges, and future directions, IEEE Access 12 (2024) 54608–54649.
[3] A. Grattafiori, A. Dubey, A. Jauhri, A. Pandey, A. Kadian, The llama 3 herd of models (2024). arXiv:2407.21783.
[4] A. Yang, B. Yang, B. Zhang, B. Hui, B. Zheng, Qwen2.5 technical report (2025). arXiv:2412.15115.
[5] D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning (2025).
arXiv:2501.12948.
[6] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, Gpt-4 technical report (et al., 2024). arXiv:2303.08774.
[7] P. Georgiev, V. I. Lei, R. Burnell, L. Bai, A. Gulati, Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context
(2024). arXiv:2403.05530.
[8] P. Liang, R. Bommasani, T. Lee, D. Tsipras, D. Soylu, et al., Holistic Evaluation of Language Models, Transactions on Machine Learning
Research (2023).
[9] C. Fourrier, N. Habib, A. Lozovskaya, K. Szafer, T. Wolf, Open llm leaderboard v2, https://huggingface.co/spaces/
open-llm-leaderboard/open_llm_leaderboard (2024).
[10] W.-L. Chiang, L. Zheng, Y. Sheng, A. N. Angelopoulos, T. Li, D. Li, B. Zhu, H. Zhang, M. Jordan, J. E. Gonzalez, I. Stoica, Chatbot arena:
An open platform for evaluating llms by human preference, in: Proceedings of the International Conference on Machine Learning, 2024,
pp. 8359–8388.
[11] M. Grandury, J. Aula-Blasco, C. Fourrier, M. Gonz´alez, G. Mart´ınez, G. Santamar´ıa, A. Vaca, La leaderboard: Leaderboard of spanish
varieties and official languages, https://huggingface.co/spaces/la-leaderboard/la-leaderboard (2024).
[12] I. Baucells, J. Aula-Blasco, I. de Dios-Flores, S. Paniagua Su´arez, N. Perez, A. Salles, S. Sotelo Docio, J. Falc˜ao, J. J. Saiz, R. Sepul-
veda Torres, J. Barnes, P. Gamallo, A. Gonzalez-Agirre, G. Rigau, M. Villegas, IberoBench: A benchmark for LLM evaluation in Iberian
languages, in: Proceedings of the International Conference on Computational Linguistics, 2025, pp. 10491–10519.
[13] E. Amig´o, J. C. de Albornoz, A. Fern´andez, J. Gonzalo, M. Lucas, G. Marco, R. Morante, J. Pedrosa, L. Plaza, E. S´anchez, A. Villa,
Proyecto espacio de observaci´on de inteligencia artificial en espa˜nol (odesia), https://leaderboard.odesia.uned.es/leaderboard/
tablesV2 (2025).
[14] L. Chiruzzo, S. M. Jim´enez-Zafra, F. Rangel, Overview of iberlef 2024: Natural language processing challenges for spanish and other
iberian languages, in: CEUR Workshop Proceedings, Vol. 3756, CEUR-WS, 2024.
[15] P. Rosso, J. Gonzalo, R. Mart´ınez, S. Montalvo, J. C. de Albornoz (Eds.), Proceedings of the Third Workshop on Evaluation of Human
Language Technologies for Iberian Languages (IberEval 2018) co-located with 34th Conference of the Spanish Society for Natural Language
Processing (SEPLN 2018), Sevilla, Spain, September 18th, 2018, Vol. 2150 of CEUR Workshop Proceedings, CEUR-WS.org, 2018.
[16] E. M. C´amara, Y. Almeida-Cruz, M. C. D´ıaz-Galiano, S. Est´evez-Velarde, M. ´A. G. Cumbreras, M. G. Vega, Y. Guti´errez, A. Montejo-R´aez,
A. Montoyo, R. Mu˜noz, A. Piad-Morffis, J. Villena-Rom´an (Eds.), Proceedings of TASS 2018: Workshop on Semantic Analysis at SEPLN,
TASS@SEPLN 2018, co-located with 34nd SEPLN Conference (SEPLN 2018), Sevilla, Spain, September 18th, 2018, Vol. 2172 of CEUR
Workshop Proceedings, CEUR-WS.org, 2018.
[17] E. Stamatatos, M. Potthast, F. M. R. Pardo, P. Rosso, B. Stein, Overview of the PAN/CLEF 2015 evaluation lab, in: J. Mothe, J. Savoy,
J. Kamps, K. Pinel-Sauvagnat, G. J. F. Jones, E. SanJuan, L. Cappellato, N. Ferro (Eds.), Experimental IR Meets Multilinguality, Multi-
modality, and Interaction - 6th International Conference of the CLEF Association, CLEF 2015, Toulouse, France, September 8-11, 2015,
Proceedings, Vol. 9283 of Lecture Notes in Computer Science, Springer, 2015, pp. 518–538.
[18] J. Etxaniz, O. Sainz, N. Miguel, I. Aldabe, G. Rigau, E. Agirre, A. Ormazabal, M. Artetxe, A. Soroa, Latxa: An open language model
and evaluation suite for Basque, in: Proceedings of the Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), 2024, pp. 14952–14972.
[19] S. Biderman, H. Schoelkopf, L. Sutawika, L. Gao, J. Tow, B. Abbasi, A. F. Aji, P. S. Ammanamanchi, S. Black, J. Clive, A. DiPofi,
J. Etxaniz, B. Fattori, J. Z. Forde, C. Foster, J. Hsu, M. Jaiswal, W. Y. Lee, H. Li, C. Lovering, N. Muennighoff, E. Pavlick, J. Phang,
A. Skowron, S. Tan, X. Tang, K. A. Wang, G. I. Winata, F. Yvon, A. Zou, Lessons from the trenches on reproducible evaluation of language
models, arXiv preprint arXiv:2405.14782 (2024).
[20] M. Abdin, J. Aneja, H. Behl, S. Bubeck, R. Eldan, S. Gunasekar, M. Harrison, R. J. Hewett, M. Javaheripi, P. Kauffmann, J. R. Lee, Y. T.
Lee, Y. Li, W. Liu, C. C. T. Mendes, A. Nguyen, E. Price, G. de Rosa, O. Saarikivi, A. Salim, S. Shah, X. Wang, R. Ward, Y. Wu, D. Yu,
C. Zhang, Y. Zhang, Phi-4 technical report (2024). arXiv:2412.08905.
[21] A. Gonzalez-Agirre, M. P`amies, J. Llop, I. Baucells, S. D. Dalt, D. Tamayo, J. J. Saiz, F. Espu˜na, J. Prats, J. Aula-Blasco, M. Mina,
I. Pikabea, A. Rubio, A. Shvets, A. Sall´es, I. Lacunza, J. Palomar, J. Falc˜ao, L. Tormo, L. Vasquez-Reina, M. Marimon, O. Pareras, V. Ruiz-
Fern´andez, M. Villegas, Salamandra technical report (2025). arXiv:2502.08489.
[22] P. H. Martins, P. Fernandes, J. Alves, N. M. Guerreiro, R. Rei, D. M. Alves, J. Pombal, A. Farajian, M. Faysse, M. Klimaszewski, P. Colombo,
B. Haddow, J. G. de Souza, A. Birch, A. F. Martins, Eurollm: Multilingual language models for europe, Procedia Computer Science 255
(2025) 53–62.
[23] J. Xu, D. Ju, M. Li, Y.-L. Boureau, J. Weston, E. Dinan, Bot-adversarial dialogue for safe conversational agents, in: Proceedings of the
Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, 2021, pp.
2950–2968.
[24] A. Wei, N. Haghtalab, J. Steinhardt, Jailbroken: How does LLM safety training fail?, in: Proceedings of the Conference on Neural Informa-
tion Processing Systems, 2023, pp. 80079–80110.
[25] G. Bai, J. Liu, X. Bu, Y. He, J. Liu, Z. Zhou, Z. Lin, W. Su, T. Ge, B. Zheng, W. Ouyang, MT-bench-101: A fine-grained benchmark
22

--- Page 23 ---

for evaluating large language models in multi-turn dialogues, in: Proceedings of the Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 2024, pp. 7421–7454.
[26] T. Li, W.-L. Chiang, E. Frick, L. Dunlap, T. Wu, B. Zhu, J. E. Gonzalez, I. Stoica, From crowdsourced data to high-quality benchmarks:
Arena-hard and benchbuilder pipeline (2024). arXiv:2406.11939.
[27] M. Wu, A. F. Aji, Style over substance: Evaluation biases for large language models, in: Proceedings of the International Conference on
Computational Linguistics, 2025, pp. 297–312.
[28] S. Schoch, D. Yang, Y. Ji, “this is a problem, don‘t you agree?” framing and bias in human evaluation for natural language generation, in:
Proceedings of the Workshop on Evaluating NLG Evaluation, 2020, pp. 10–16.
[29] T. Baumann, Universal jailbreak backdoors in large language model alignment, in: Neurips Safe Generative AI Workshop 2024, 2024.
[30] A. Wang, A. Singh, J. Michael, F. Hill, O. Levy, S. Bowman, GLUE: A multi-task benchmark and analysis platform for natural language
understanding, in: Proceedings of the EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP, 2018, pp.
353–355.
[31] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, J. Steinhardt, Measuring massive multitask language understanding,
Proceedings of the International Conference on Learning Representations (2021) 1–30.
[32] A. Bavaresco, R. Bernardi, L. Bertolazzi, D. Elliott, R. Fern´andez, A. Gatt, E. Ghaleb, M. Giulianelli, M. Hanna, A. Koller, A. F. T. Martins,
P. Mondorf, V. Neplenbroek, S. Pezzelle, B. Plank, D. Schlangen, A. Suglia, A. K. Surikuchi, E. Takmaz, A. Testoni, Llms instead of human
judges? a large scale empirical study across 20 nlp evaluation tasks, arXiv preprint arXiv:2406.18403 (2024).
[33] L. Zheng, W.-L. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. P. Xing, H. Zhang, J. E. Gonzalez, I. Stoica,
Judging llm-as-a-judge with mt-bench and chatbot arena, in: Proceedings of the International Conference on Neural Information Processing
Systems, 2023, pp. 46595–46623.
[34] G. H. Chen, S. Chen, Z. Liu, F. Jiang, B. Wang, Humans or LLMs as the judge? a study on judgement bias, in: Proceedings of the 2024
Conference on Empirical Methods in Natural Language Processing, 2024, pp. 8301–8327.
[35] M. Ali, M. Fromm, K. Thellmann, J. Ebert, A. A. Weber, R. Rutmann, C. Jain, M. L¨ubbering, D. Steinigen, J. Leveling, K. Klug, J. S.
Buschhoff, L. Jurkschat, H. Abdelwahab, B. J. Stein, K.-H. Sylla, P. Denisov, N. Brandizzi, Q. Saleem, A. Bhowmick, L. Helmer, C. John,
P. O. Suarez, M. Ostendorff, A. Jude, L. Manjunath, S. Weinbach, C. Penke, O. Filatov, S. Asaadi, F. Barth, R. Sifa, F. K¨uch, A. Herten,
R. J¨akel, G. Rehm, S. Kesselheim, J. K¨ohler, N. Flores-Herr, Teuken-7b-base & teuken-7b-instruct: Towards european llms (2024). arXiv:
2410.03730.
[36] H. Singh, N. Gupta, S. Bharadwaj, D. Tewari, P. Talukdar, IndicGenBench: A multilingual benchmark to evaluate generation capabilities
of LLMs on Indic languages, in: Proceedings of the Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), 2024, pp. 11047–11073.
[37] Y. Susanto, A. V. Hulagadri, J. R. Montalan, J. G. Ngui, X. B. Yong, W. Leong, H. Rengarajan, P. Limkonchotiwat, Y. Mai, W. C. Tjhi,
Sea-helm: Southeast asian holistic evaluation of language models (2025). arXiv:2502.14301.
[38] E. Almazrouei, R. Cojocaru, M. Baldo, Q. Malartic, H. Alobeidli, D. Mazzotta, G. Penedo, G. Campesan, M. Farooq, M. Alhammadi, J. Lau-
nay, B. Noune, AlGhafa evaluation benchmark for Arabic language models, in: Proceedings of the Arabic Natural Language Processing
Conference, 2023, pp. 244–275.
[39] D. Duki´c, J. Snajder, Looking right is sometimes right: Investigating the capabilities of decoder-only LLMs for sequence labeling, in:
Findings of the Association for Computational Linguistic, 2024, pp. 14168–14181.
[40] S. Wang, X. Sun, X. Li, R. Ouyang, F. Wu, T. Zhang, J. Li, G. Wang, Gpt-ner: Named entity recognition via large language models (2023).
arXiv:2304.10428.
[41] N. Houlsby, A. Giurgiu, S. Jastrzebski, B. Morrone, Q. de Laroussilhe, A. Gesmundo, M. Attariyan, S. Gelly, Parameter-efficient transfer
learning for nlp, in: Proceedings of the International Conference on Machine Learning, 2019, pp. 2790–2799.
[42] E. Frantar, S. Ashkboos, T. Hoefler, D. Alistarh, OPTQ: Accurate quantization for generative pre-trained transformers, in: The Eleventh
International Conference on Learning Representations, 2023.
[43] F. Rangel, P. Rosso, M. Potthast, B. Stein, Overview of the 5th author profiling task at pan 2017: Gender and language variety identification
in twitter, Working notes papers of the CLEF 48 (2017).
[44] L. Bandarkar, D. Liang, B. Muller, M. Artetxe, S. N. Shukla, D. Husa, N. Goyal, A. Krishnan, L. Zettlemoyer, M. Khabsa, The belebele
benchmark: a parallel reading comprehension dataset in 122 language variants, in: Proceedings of the Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), 2024, pp. 749–775.
[45] R. Schaeffer, Pretraining on the test set is all you need, arXiv preprint arXiv:2309.08632 (2023).
[46] Q. Lhoest, A. Villanova del Moral, Y. Jernite, A. Thakur, P. von Platen, Datasets: A community library for natural language processing, in:
H. Adel, S. Shi (Eds.), Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing: System Demonstrations,
Association for Computational Linguistics, Online and Punta Cana, Dominican Republic, et al., 2021, pp. 175–184.
[47] Y. Hu, Q. Chen, J. Du, X. Peng, V. K. Keloth, X. Zuo, Y. Zhou, Z. Li, X. Jiang, Z. Lu, K. Roberts, H. Xu, Improving large language models
for clinical named entity recognition via prompt engineering, Journal of the American Medical Informatics 31 (9) (2024) 1812–1820.
[48] A. Zubiaga, I. S. Vicente, P. Gamallo, J. R. Pichel, I. Alegria, N. Aranberri, A. Ezeiza, V. Fresno, Tweetlid: a benchmark for tweet language
identification, Language Resources and Evaluation 50 (2016) 729–766.
[49] M. Garcia-Vega, M. D´ıaz-Galiano, M. Garc´ıa-Cumbreras, F. M. P. Del Arco, A. Montejo-Ra´ez, S. Jim´enez-Zafra, E. M. C´amara, C. Aguilar,
M. Cabezudo, L. Chiruzzo, et al., Overview of tass 2020: Introducing emotion detection, in: Proceedings of the Iberian Languages Evalua-
tion Forum Co-Located with Conference of the Spanish Society for Natural Language Processing, 2020, pp. 163–170.
[50] F. M. Rangel Pardo, F. Celli, P. Rosso, M. Potthast, B. Stein, W. Daelemans, Overview of the author profiling task at pan 2015, in: Working
notes papers of the CLEF, 2015, pp. 1–8.
[51] M. Taul´e, F. M. R. Pardo, M. A. Mart´ı, P. Rosso, Overview of the task on multimodal stance detection in tweets on catalan# 1oct referendum,
in: Proceedings of the Workshop on Evaluation of Human Language Technologies for Iberian Languages, 2018, pp. 149–166.
[52] L. Chiruzzo, S. Castro, M. Etcheverry, D. Garat, J. J. Prada, A. Ros´a, Overview of haha at iberlef 2019: Humor analysis based on human
annotation, in: Proceedings of the Iberian Languages Evaluation Forum, 2019, pp. 132–144.
23

--- Page 24 ---

[53] R. Ortega-Bueno, F. Rangel, D. Hern´andez Farıas, P. Rosso, M. Montes-y G´omez, J. E. Medina Pagola, Overview of the task on irony
detection in spanish variants, in: Proceedings of the Iberian languages evaluation forum, co-located with conference of the Spanish Society
for natural language processing, Vol. 2421, 2019, pp. 229–256.
[54] M. E. Arag´on, M. ´A. ´Alvarez-Carmona, M. Montes-y G´omez, H. J. Escalante, L. V. Pineda, D. Moctezuma, Overview of mex-a3t at iberlef
2019: Authorship and aggressiveness analysis in mexican spanish tweets., in: Proceedings of the Iberian Languages Evaluation Forum,
2019, pp. 478–494.
[55] M. Taul´e, A. Ariza, M. Nofre, E. Amig´o, P. Rosso, Overview of detoxis at iberlef 2021: Detection of toxicity in comments in spanish,
Procesamiento del Lenguaje Natural 67 (2021) 209–221.
[56] F. M. Plaza-del Arco, S. M. Jim´enez-Zafra, A. Montejo-R´aez, M. D. Molina-Gonz´alez, L. A. Ure˜na-L´opez, M. T. Mart´ın-Valdivia, Overview
of the emoevales task on emotion detection for spanish at iberlef 2021, Procesamiento del Lenguaje Natural 67 (2021) 155–161.
[57] F. J. Rodr´ıguez-S´anchez, J. Carrillo-de Albornoz, L. Plaza, J. Gonzalo, P. Rosso, M. Comet, T. Donoso, Overview of exist 2021: sexism
identification in social networks, Procesamiento del Lenguaje Natural 67 (2021) 195–207.
[58] H. G´omez-Adorno, J. P. Posadas-Dur´an, G. Bel Enguix, C. Porto Capetillo, Overview of fakedes at iberlef 2021: Fake news detection in
spanish shared task, Procesamiento del Lenguaje Natural 67 (2021) 223–231.
[59] L. Chiruzzo, S. Castro, S. G´ongora, A. Ros´a, J. Meaney, R. Mihalcea, Overview of haha at iberlef 2021: Detecting, rating and analyzing
humor in spanish, Procesamiento del Lenguaje Natural 67 (2021) 257–268.
[60] H. Jarqu´ın-V´asquez, L. Villase˜nor Pineda, F. M. Plaza-del Arco, M. Casavantes, H. J. Escalante, M. T. Mart´ın Valdivia, A. Montejo R´aez,
M. Montes y G´omez, Overview of meoffendes at iberlef 2021: Offensive language detection in spanish variants, Procesamiento del Lenguaje
Natural 67 (2021) 183–194.
[61] M. ´A. ´Alvarez Carmona, R. Aranda, S. Arce-Cardenas, D. Fajardo-Delgado, R. Guerrero-Rodr´ıguez, A. P. L´opez-Monroy, J. Mart´ınez-
Miranda, H. P´erez-Espinosa, A. Y. Rodr´ıguez-Gonz´alez, Overview of rest-mex at iberlef 2021: Recommendation system for text mexican
tourism, Procesamiento del Lenguaje Natural 67 (2021) 163–172.
[62] R. Agerri Gasc´on, R. Centeno S´anchez, M. Espinosa, J. Fern´andez de Landa, ´A. Rodrigo Yuste, Vaxxstance@iberlef 2021: Overview of the
task on going beyond text in cross-lingual stance detection, Procesamiento del Lenguaje Natural 67 (2021) 173–181.
[63] G. Bel-Enguix, G. Sierra, H. G´omez-Adorno, J.-M. Torres-Moreno, J.-G. Ortiz-Barajas, J. V´asquez, Overview of par-mex at iberlef 2022:
Paraphrase detection in spanish shared task, Procesamiento del Lenguaje Natural 69 (2022) 255–263.
[64] M. ´A. ´Alvarez Carmona, ´A. D´ıaz-Pacheco, R. Aranda, A. Y. Rodr´ıguez-Gonz´alez, D. Fajardo-Delgado, R. Guerrero-Rodr´ıguez, L. Bustio-
Mart´ınez, Overview of rest-mex at iberlef 2022: Recommendation system, sentiment analysis and covid semaphore prediction for mexican
tourist texts, Procesamiento del Lenguaje Natural 69 (2022) 289–299.
[65] A. M. M´armol-Romero, A. Moreno-Mu˜noz, F. M. Plaza-del Arco, M. D. Molina-Gonz´alez, M. T. Mart´ın-Valdivia, L. A. Ure˜na-L´opez,
A. Montejo-R´aez, Overview of mentalriskes at iberlef 2023: Early detection of mental disorders risk in spanish, Procesamiento del Lenguaje
Natural 71 (2023) 329–350.
[66] R. Labadie Tamayo, B. Chulvi, P. Rosso, Everybody hurts, sometimes. overview of hurtful humour at iberlef 2023: Detection of humour
spreading prejudice in twitter, Procesamiento del Lenguaje Natural 71 (2023) 383–395.
[67] W. S. S.-N. y Pol Pastells y Simona Frenda y Alejandro Ariza-Casabona y Mireia Farr´us y Paolo Rosso y Mariona Taul´e, Overview of
detests-dis at iberlef 2024: Detection and classification of racial stereotypes in spanish - learning with disagreement, Procesamiento del
Lenguaje Natural 73 (0) (2024) 323–333.
[68] A. M. S. y Jos´e ´Angel Gonz´alez y Francisco Rangel y Paolo Rosso y Marc Franco-Salvador, Overview of iberautextification at iberlef
2024: Detection and attribution of machine-generated text on languages of the iberian peninsula, Procesamiento del Lenguaje Natural 73 (0)
(2024) 421–434.
[69] Y. Yang, Y. Zhang, C. Tar, J. Baldridge, PAWS-X: A cross-lingual adversarial dataset for paraphrase identification, in: Proceedings of the
Conference on Empirical Methods in Natural Language Processing and the International Joint Conference on Natural Language Processing,
2019, pp. 3687–3692.
[70] A. I. Vladu, I. de Dios-Flores, C. Magari˜nos, J. E. Ortega, J. R. Pichel, M. Garcia, P. Gamallo, E. F. Rei, A. Bugar´ın, M. G. Gonz´alez,
et al., Proxecto n´os: Artificial intelligence at the service of the galician language, in: Proceedings of the Annual Conference of the Spanish
Association for Natural Language Processing: Projects and Demonstrations, 2022, pp. 26–30.
[71] A. Gonzalez-Agirre, M. Marimon, C. Rodriguez-Penagos, J. Aula-Blasco, I. Baucells, C. Armentano-Oller, J. Palomar-Giner, B. Kulebi,
M. Villegas, Building a data infrastructure for a mid-resource language: The case of Catalan, in: Proceedings of the Joint International
Conference on Computational Linguistics, Language Resources and Evaluation, 2024, pp. 2556–2566.
[72] T. Hasan, A. Bhattacharjee, M. S. Islam, K. Mubasshir, Y.-F. Li, Y.-B. Kang, M. S. Rahman, R. Shahriyar, XL-sum: Large-scale multilingual
abstractive summarization for 44 languages, in: Findings of the Association for Computational Linguistics, 2021, pp. 4693–4703.
[73] Barcelona Supercomputing Center, Projecte aina: Recursos ling¨u´ıstics i tecnol`ogics per al catal`a a l’era digital (2021).
URL https://projecteaina.cat/
[74] G. Urbizu, I. San Vicente, X. Saralegi, R. Agerri, A. Soroa, Basqueglue: A natural language understanding benchmark for basque, in:
Proceedings of the Language Resources and Evaluation Conference, Marseille, France, 2022, pp. 1603–1612.
[75] A. V. Serrano, I. L. Montalb´an, D. V. Vel´azquez, M. Moreno, Clindiagnoses (2024).
URL https://huggingface.co/datasets/LenguajeNaturalAI/ClinDiagnosES
[76] P. R¨ottger, H. Seelawi, D. Nozza, Z. Talat, B. Vidgen, Multilingual HateCheck: Functional tests for multilingual hate speech detection
models, in: Proceedings of the Workshop on Online Abuse and Harms, 2022, pp. 154–169.
[77] E. ´Alvarez Mellado, L. Espinosa Anke, J. G. Arroyo, C. Lignos, J. Porta Zamorano, Overview of adobo 2021: Automatic detection of
unassimilated borrowings in the spanish press, Procesamiento del Lenguaje Natural 67 (2021) 277–285.
[78] J. Armengol-Estap´e, C. P. Carrino, C. Rodriguez-Penagos, O. de Gibert Bonet, C. Armentano-Oller, A. Gonzalez-Agirre, M. Melero,
M. Villegas, Are multilingual models the best choice for moderately under-resourced languages? A comprehensive assessment for Catalan,
in: Findings of the Association for Computational Linguistics: ACL-IJCNLP, 2021, pp. 4933–4946.
[79] Secretar´ıa de Estado de Digitalizaci´on e Inteligencia Artificial, Proyecto del impulso de las lenguas en la inteligencia artificial (ilenia) (2022).
24

--- Page 25 ---

URL "https://proyectoilenia.es/"
[80] N. Bel, M. Punsola, V. Ruiz-Fern´andez, EsCoLA: Spanish corpus of linguistic acceptability, in: Proceedings of the Joint International
Conference on Computational Linguistics, Language Resources and Evaluation, 2024, pp. 6268–6277.
[81] N. Bel, M. Punsola, V. Ruiz-Fern´andez, Catcola, catalan corpus of linguistic acceptability, Procesamiento del Lenguaje Natural 73 (2024)
177–190.
[82] M. Mayor-Rocher, N. Melero, E. Merino-G´omez, M. Gonz´alez, R. Ferrando, J. Conde, P. Reviriego, Spanish Language Benchmark for
Artificial Intelligence Models (TELEIA) (2024).
URL https://doi.org/10.5281/zenodo.12571763
[83] A. Conneau, R. Rinott, G. Lample, A. Williams, S. R. Bowman, H. Schwenk, V. Stoyanov, Xnli: Evaluating cross-lingual sentence repre-
sentations, in: Proceedings of the Conference on Empirical Methods in Natural Language Processing, 2018, pp. 2475–2485.
[84] C.-Y. Lin, ROUGE: A package for automatic evaluation of summaries, in: Text Summarization Branches Out, Association for Computational
Linguistics, 2004, pp. 74–81.
[85] T. He, J. Zhang, T. Wang, S. Kumar, K. Cho, J. Glass, Y. Tsvetkov, On the blind spots of model-based evaluation metrics for text generation,
in: Proceedings of the Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2023, pp. 12067–12097.
[86] H. Nakayama, seqeval: A python framework for sequence labeling evaluation (2018).
URL https://github.com/chakki-works/seqeval
[87] R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, C. Finn, Direct preference optimization: Your language model is secretly a
reward model, in: Advances in Neural Information Processing Systems, Vol. 36, Curran Associates, Inc., 2023, pp. 53728–53741.
[88] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, O. Klimov, Proximal policy optimization algorithms (2017). arXiv:1707.06347.
[89] A. Abouelenin, A. Ashfaq, A. Atkinson, H. Awadalla, N. Bach, Phi-4-mini technical report: Compact yet powerful multimodal language
models via mixture-of-loras (et al., 2025). arXiv:2503.01743.
[90] A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot, D. de las Casas, F. Bressand, G. Lengyel, G. Lample, L. Saulnier, L. R.
Lavaud, M.-A. Lachaux, P. Stock, T. L. Scao, T. Lavril, T. Wang, T. Lacroix, W. E. Sayed, Mistral 7b (2023). arXiv:2310.06825.
[91] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, I. Sutskever, Language models are unsupervised multitask learners, technical report
(2019).
[92] M. Riviere, S. Pathak, P. G. Sessa, C. Hardin, S. Bhupatiraju, Gemma 2: Improving open language models at a practical size (2024).
arXiv:2408.00118.
[93] G. S. G´omez, G. G. Subies, P. G. Ruiz, M. G. Valero, N. Fuertes, H. M. Zamorano, C. M. Sanz, L. R. Plaza, N. A. Garc´ıa, D. B. S´anchez,
K. Sushkova, M. G. Nieto, ´Alvaro Barbero Jim´enez, Rigochat 2: an adapted language model to spanish using a bounded dataset and reduced
hardware (2025). arXiv:2503.08188.
[94] L. Petrea, Catallama, https://huggingface.co/catallama/CataLlama-v0.2-Instruct-SFT (2024).
[95] R. Pires, H. Abonizio, T. S. Almeida, R. Nogueira, Sabi´a: Portuguese large language models, in: Intelligent Systems, 2023, pp. 226–240.
[96] Language, I. S. Group, Aitana, https://huggingface.co/gplsi/Aitana-6.3B (2024).
[97] Q. Dong, L. Li, D. Dai, C. Zheng, J. Ma, R. Li, H. Xia, J. Xu, Z. Wu, B. Chang, X. Sun, L. Li, Z. Sui, A survey on in-context learning, in:
Proceedings of the Conference on Empirical Methods in Natural Language Processing, 2024, pp. 1107–1128.
[98] J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai, E. Rutherford, D. de Las Casas, L. A. Hendricks, J. Welbl, A. Clark,
et al., Training compute-optimal large language models, in: Proceedings of the International Conference on Neural Information Processing
Systems, 2022, pp. 30016–30030.
[99] B. O’Rourke, The galician language in the twenty-first century, A companion to Galician culture 344 (2014) 73.
[100] A. Tovar, H. P. Houghton, The Basque Language, University of Pennsylvania Press, 1957.
25

--- Page 26 ---

Appendix A. Datasets and Sources
Table A.6 lists the main URLs of the workshops, shared tasks and other sources we include in IberBench as
industry-relevant tasks. Table A.7 shows the URLs of workshops, shared tasks and other sources that comprise the
fundamental tasks of IberBench.
Task
Subtask
Year
Language
URL
TweetLID
Language identification
2014
es
http://komunitatea.elhuyar.eus/tweetlid/
TASS
Emotion analysis
2020
es
http://tass.sepln.org/2020/
TASS
Sentiment analysis
2020
es-{UY, MX, ES, CR, PE}
http://tass.sepln.org/2020/
Author Profiling
Age detection
2015
es
https://pan.webis.de/clef15/pan15-web/author-profiling
Author Profiling
Gender detection
2017
es
https://pan.webis.de/clef17/pan17-web/author-profiling
MultiStanceCat
Stance Detection
2018
{es, ca}
https://ceur-ws.org/Vol-2150/overview-Multistance18.pdf
HAHA
Humor detection
2019
es
https://www.fing.edu.uy/inco/grupos/pln/haha/2019
IroSvA
Irony detection
2019
es-{CU, MX, ES}
https://ceur-ws.org/Vol-2421/IroSvA_overview.pdf
MEX-A3T
Aggressiveness detection
2019
es-MX
https://sites.google.com/view/mex-a3t2019
DETOXIS
Aggressiveness detection
2021
es
https://detoxisiberlef.wixsite.com/website
DETOXIS
Improper language detection
2021
es
https://detoxisiberlef.wixsite.com/website
DETOXIS
Insult detection
2021
es
https://detoxisiberlef.wixsite.com/website
DETOXIS
Mockery detection
2021
es
https://detoxisiberlef.wixsite.com/website
DETOXIS
Sarcasm detection
2021
es
https://detoxisiberlef.wixsite.com/website
DETOXIS
Toxicity detection
2021
es
https://detoxisiberlef.wixsite.com/website
EmoEvalES
Offensiveness detection
2021
es
https://competitions.codalab.org/competitions/28682
EmoEvalES
Emotion analysis
2021
es
https://competitions.codalab.org/competitions/28682
EXIST
Sexism detection
2021
es
https://nlp.uned.es/exist2021/
EXIST
Sexism categorization
2021
es
https://nlp.uned.es/exist2021/
FakeDeS
Fake News detection
2021
es
https://sites.google.com/view/fakedes
HAHA
Humor detection
2021
es
https://www.fing.edu.uy/inco/grupos/pln/haha/
MeOffendEs
Gender detection
2021
es
https://competitions.codalab.org/competitions/28679
MeOffendEs
Offensiveness detection
2021
es
https://competitions.codalab.org/competitions/28679
Rest-Mex
Gender detection
2021
es-MX
https://sites.google.com/cicese.edu.mx/rest-mex-2021
Rest-Mex
Sentiment analysis
2021
es-MX
https://sites.google.com/cicese.edu.mx/rest-mex-2021
VaxxStance
Stance detection
2021
{eu, es}
https://vaxxstance.github.io
Par-Mex
Paraphrase detection
2022
es
https://sites.google.com/view/par-mex/home
Rest-Mex
Sentiment analysis
2022
es-MX
https://sites.google.com/cicese.edu.mx/rest-mex-2022/home
MentalRiskES
Eating disorder detection
2023
es
https://sites.google.com/view/mentalriskes
MentalRiskES
Depression detection
2023
es
https://sites.google.com/view/mentalriskes
MentalRiskES
Depression categorization
2023
es
https://sites.google.com/view/mentalriskes
HUHU
Fatphobia detection
2023
es
https://sites.google.com/view/huhuatiberlef23
HUHU
Humor detection
2023
es
https://sites.google.com/view/huhuatiberlef23
HUHU
LGBTIQ prejudice detection
2023
es
https://sites.google.com/view/huhuatiberlef23
HUHU
Racial prejudice detection
2023
es
https://sites.google.com/view/huhuatiberlef23
HUHU
Women prejudice detection
2023
es
https://sites.google.com/view/huhuatiberlef23
DETESTS-Dis
Stereotype detection
2024
es
https://detests-dis.github.io/
IberAuTexTification
MGT detection
2024
{en, es, eu, pt, ca, gl}
https://sites.google.com/view/iberautextification
IberAuTexTification
MGT attribution
2024
{en, es, eu, pt, ca, gl}
https://sites.google.com/view/iberautextification
PAWS
Paraphrase detection
2019
es
https://huggingface.co/datasets/google-research-datasets/paws-x
gl
https://huggingface.co/datasets/proxectonos/PAWS-gl
pt
https://huggingface.co/datasets/proxectonos/PAWS_pt
ca
https://huggingface.co/datasets/projecte-aina/PAWS-ca
XLSum
Text summarization
2021
{es, pt}
https://huggingface.co/datasets/csebuetnlp/xlsum
BEC
Sentiment analysis
2024
eu
https://huggingface.co/datasets/orai-nlp/basqueGLUE
BHTC
Topic classification
2024
eu
https://huggingface.co/datasets/orai-nlp/basqueGLUE
caBreu
Text summarization
2024
ca
https://huggingface.co/datasets/projecte-aina/caBreu
ClinDiagnosES
Topic classification
2024
es
https://huggingface.co/datasets/LenguajeNaturalAI/ClinDiagnosES
FMTODeu
Intent classification
2024
eu
https://huggingface.co/datasets/orai-nlp/basqueGLUE
HateCheck
Hate speech detection
2024
pt
https://huggingface.co/datasets/Paul/hatecheck-portuguese
Parafraseja
Paraphrase detection
2024
ca
https://huggingface.co/datasets/projecte-aina/Parafraseja
Table A.6: Industry-relevant tasks with URLs.
26

--- Page 27 ---

Task
Subtask
Year
Language
URL
ADoBo
Lexical borrowing chunking
2021
es
https://adobo-task.github.io/
TE-ca
Textual entailment
2021
ca
https://huggingface.co/datasets/projecte-aina/teca
OpenBookQA
Question answering
2022
es
https://huggingface.co/datasets/BSC-LT/openbookqa-es
ca
https://huggingface.co/datasets/projecte-aina/openbookqa_ca
ARC
Question answering
2024
eu
https://huggingface.co/datasets/HiTZ/ARC-eu
ca
https://huggingface.co/datasets/projecte-aina/arc_ca
Belebele
Reading comprehension
2024
{eu, es, pt, ca}
https://huggingface.co/datasets/facebook/belebele
CoLA
Linguistic acceptability
2024
es
https://huggingface.co/datasets/nbel/EsCoLA
gl
https://huggingface.co/datasets/proxectonos/galcola
ca
https://huggingface.co/datasets/nbel/CatCoLA
COPA
Commonsense reasoning
2024
eu
https://huggingface.co/datasets/HiTZ/XCOPA-eu
es
https://huggingface.co/datasets/BSC-LT/COPA-es
ca
https://huggingface.co/datasets/projecte-aina/COPA-ca
EusExams
Question answering
2024
{eu, es}
https://huggingface.co/datasets/HiTZ/EusExams
EusProficiency
Proficiency evaluation
2024
eu
https://huggingface.co/datasets/HiTZ/EusProficiency
EusReading
Reading comprehension
2024
eu
https://huggingface.co/datasets/HiTZ/EusReading
EusTrivia
Topic classification
2024
eu
https://huggingface.co/datasets/HiTZ/EusTrivia
EusTrivia
Question answering
2024
eu
https://huggingface.co/datasets/HiTZ/EusTrivia
PIQA
Commonsense reasoning
2024
eu
https://huggingface.co/datasets/HiTZ/PIQA-eu
TELEIA
Proficiency evaluation
2024
es
https://huggingface.co/datasets/gonzmart/teleia
QNLI
Textual entailment
2024
eu
https://huggingface.co/datasets/orai-nlp/basqueGLUE
XNLI
Textual entailment
2024
es
https://huggingface.co/datasets/facebook/xnli
gl
https://huggingface.co/datasets/proxectonos/xnli_gl
ca
https://huggingface.co/datasets/projecte-aina/xnli-ca
XStoryCloze
Question answering
2024
gl
https://huggingface.co/proxectonos/xstorycloze_gl
pt
https://huggingface.co/datasets/proxectonos/xstorycloze_pt
ca
https://huggingface.co/datasets/projecte-aina/xstorycloze_ca
Table A.7: Fundamental tasks with URLs.
27

--- Page 28 ---

Appendix B. Model Rankings
Figures B.10 and B.11 show heatmaps of the rankings of each LLM in a given task and Iberian language respec-
tively.
20
22
9
8
6
13
18
19
16
21
2
7
11
23
3
5
4
12
17
14
15
10
1
18
15
21
19
12
7
8
2
16
11
6
10
22
14
9
3
5
13
23
4
17
20
1
18
6
10
9
17
16
14
8
22
19
7
15
20
23
1
2
3
4
21
5
13
11
12
20
21
16
17
15
7
6
3
10
14
9
8
23
12
5
1
2
13
19
22
18
11
4
14
18
6
9
21
16
13
11
22
19
8
15
2
10
3
5
4
23
7
12
1
20
17
21
17
8
4
12
1
9
6
18
13
5
7
20
3
2
10
11
23
16
22
14
15
19
17
11
13
15
7
1
12
6
14
10
8
19
21
18
9
3
2
22
23
5
20
16
4
15
22
20
18
3
2
13
11
16
12
4
10
14
9
5
6
7
8
23
1
19
21
17
16
10
22
17
14
4
13
12
18
23
3
8
19
20
7
2
1
6
21
11
15
9
5
7
13
3
6
19
23
18
11
1
8
2
12
14
16
9
10
5
22
17
15
4
21
20
18
11
14
22
13
9
10
2
19
5
15
7
17
8
1
4
6
12
21
23
20
16
3
22
11
23
19
9
6
17
10
16
15
14
5
12
7
3
2
1
8
18
13
21
20
4
22
11
21
16
19
8
14
4
17
12
6
7
15
9
3
2
1
18
23
10
20
13
5
21
12
22
23
15
11
6
4
17
9
7
2
16
13
8
3
5
10
20
1
18
19
14
20
13
23
21
14
7
6
4
16
11
12
10
18
15
8
2
3
9
22
1
17
19
5
23
9
21
20
15
13
3
1
16
10
11
6
17
14
8
5
4
12
22
2
18
19
7
18
16
19
15
21
5
2
10
14
12
7
3
22
13
11
6
4
17
23
9
20
8
1
22
8
15
12
21
20
18
4
14
5
7
6
17
16
10
1
2
19
23
11
13
9
3
14
22
19
15
18
2
7
3
9
4
1
8
17
12
10
6
5
21
23
20
11
16
13
17
13
20
19
9
7
12
10
21
16
5
1
23
14
6
2
3
15
22
8
18
11
4
20
7
17
16
8
12
1
9
22
19
11
13
15
14
3
18
21
5
23
2
10
6
4
23
12
14
16
10
2
11
1
13
9
5
3
22
15
4
6
7
21
20
18
19
17
8
Aitana-6.3B
CataLlama-v0.2-Instruct-SFT
EuroLLM-1.7B
EuroLLM-1.7B-Instruct
EuroLLM-9B
EuroLLM-9B-Instruct
Latxa-Llama-3.1-8B-Instruct
Llama-3.1-8B-Instruct
Llama-3.2-1B-Instruct
Llama-3.2-3B-Instruct
Mistral-7B-Instruct-v0.3
Phi-4-mini-instruct
Qwen2.5-0.5B-Instruct
Qwen2.5-1.5B-Instruct
Qwen2.5-3B-Instruct
Qwen2.5-7B-Instruct
RigoChat-7b-v2
gemma-2-2b-it
gpt2
phi-4
sabia-7b
salamandra-2b-instruct
salamandra-7b-instruct
Toxicity and 
Harmful Language
Topic
Classiﬁcation
Textual
Entailment
Summarization
Stance
Detection
Sentiment and
Emotion Analysis
Reading
Comprehension
Question
Answering
Proﬁciency
Evaluation
Prejudice and
Discrimination
Paraphrase
Detection
Mental Health
Detection
MGT Detection
and Attribution
Linguistic
Acceptability
Lexical
Analysis
Language
Identiﬁcation
Irony and
Sarcasm
Intent
Classiﬁcation
Humor
Detection
Fake News
Detection
Commonsense
Reasoning
Author
Proﬁling
Figure B.10: Ranking of models per task category.
28

--- Page 29 ---

Aitana-6.3B
CataLlama-v0.2-Instruct-SFT
EuroLLM-1.7B
EuroLLM-1.7B-Instruct
EuroLLM-9B
EuroLLM-9B-Instruct
Latxa-Llama-3.1-8B-Instruct
Llama-3.1-8B-Instruct
Llama-3.2-1B-Instruct
Llama-3.2-3B-Instruct
Mistral-7B-Instruct-v0.3
Phi-4-mini-instruct
Qwen2.5-0.5B-Instruct
Qwen2.5-1.5B-Instruct
Qwen2.5-3B-Instruct
Qwen2.5-7B-Instruct
RigoChat-7b-v2
gemma-2-2b-it
gpt2
phi-4
sabia-7b
salamandra-2b-instruct
salamandra-7b-instruct
English
Spanish
Galician
Portuguese
Catalan
Basque
Mexico
Uruguay
Costa Rica
Cuba
Peru
Spain
8
2
21
21
16
23
15
7
19
11
3
5
9
12
4
13
10
14
18
17
1
21
6
22
15
21
19
14
4
10
5
17
13
6
8
20
11
3
1
2
12
23
9
18
16
7
22
5
21
19
16
15
10
9
12
13
8
4
20
14
3
2
1
7
18
6
17
23
11
23
8
21
20
12
3
13
2
16
14
11
7
17
15
4
9
6
10
22
1
18
19
5
22
5
21
19
11
10
15
9
16
13
6
7
20
14
8
1
2
12
23
3
17
18
4
21
12
17
15
23
22
1
3
18
11
9
4
20
19
7
6
5
9
16
8
13
14
2
23
19
18
16
10
1
17
2
12
11
6
8
13
7
5
3
4
14
21
22
20
15
9
17
12
19
5
21
4
1
8
11
12
2
16
23
9
18
15
14
7
22
10
20
3
6
18
17
19
7
21
4
1
16
6
11
10
5
23
8
14
13
9
2
22
15
20
3
12
21
6
14
9
15
1
12
4
19
16
3
7
20
5
2
8
10
22
18
23
17
11
13
17
18
19
8
21
4
1
12
9
14
7
11
23
3
16
15
13
5
22
10
20
2
6
17
18
19
9
21
3
1
4
15
8
5
13
23
7
14
10
11
12
22
16
20
6
2
Figure B.11: Ranking of models per Iberian language.
29

```
