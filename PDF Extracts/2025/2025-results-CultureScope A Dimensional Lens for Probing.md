---
title: "2025-results]]-CultureScope A Dimensional Lens for Probing - PDF Extract"
source_pdf: "2025-results]]-CultureScope A Dimensional Lens for Probing.pdf"
pages: 20
extracted_at: "2026-02-13T09:15:45.459715"
---

# PDF Extract: 2025-results]]-CultureScope A Dimensional Lens for Probing

**Source PDF:** 2025-results]]-CultureScope A Dimensional Lens for Probing.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs
Jinghao Zhang1, Sihang Jiang1, *, Shiwei Guo2, Shisong Chen3, Yanghua Xiao1, *, Hongwei Feng1,
Jiaqing Liang1, Minggui HE4, Shimin Tao4, Hongxia Ma4 *
1Shanghai Key Laboratory of Data Science, College of Computer Science and Artificial Intelligence, Fudan University
2School of Foreign Languages and Literatures, Fudan University
3Shanghai Institute of Artificial Intelligence for Education, East China Normal University
4Huawei, China
zhangjinghao24@m.fudan.edu.cn, {jiangsihang, shawyh}@fudan.edu.cn
Abstract
As large language models (LLMs) are increasingly deployed
in diverse cultural environments, evaluating their cultural
understanding capability has become essential for ensur-
ing trustworthy and culturally aligned applications. How-
ever, most existing benchmarks lack comprehensiveness and
are challenging to scale and adapt across different cul-
tural contexts, because their frameworks often lack guidance
from well-established cultural theories and tend to rely on
expert-driven manual annotations. To address these issues,
we propose CultureScope, the most comprehensive evalua-
tion framework to date for assessing cultural understanding
in LLMs. Inspired by the cultural iceberg theory, we de-
sign a novel dimensional schema for cultural knowledge clas-
sification, comprising 3 layers and 140 dimensions, which
guides the automated construction of culture-specific knowl-
edge bases and corresponding evaluation datasets for any
given languages and cultures. Experimental results demon-
strate that our method can effectively evaluate cultural under-
standing. They also reveal that existing large language models
lack comprehensive cultural competence, and merely incor-
porating multilingual data does not necessarily enhance cul-
tural understanding. All code and data files are available at
https://github.com/HoganZinger/Culture
Introduction
Large language models (LLMs) have demonstrated impres-
sive capabilities across a wide spectrum of natural language
processing tasks, and are now widely adopted in applications
ranging from virtual assistants to educational tools.(Mohan
et al. 2024; Raiaan et al. 2024; Raza et al. 2025) Despite
these achievements, a persistent challenge remains: Cur-
rent large language models still exhibit significant short-
comings in cultural understanding, often leading to cultural
misalignment when applied in real-world contexts(Benkler
et al. 2023; AlKhamissi et al. 2024; Shen et al. 2024). For
example, if a healthcare chatbot powered by an LLM rec-
ommended placing an elderly parent in a nursing facility to
a Chinese user, it fails to account for the cultural signifi-
cance of filial piety (Xiaoshun) in traditional Chinese so-
ciety. While the suggestion aligns with Western notions of
efficiency, it conflicts with deeply rooted Chinese values,
leading to user dissatisfaction and negative public response.
*Corresponding authors.
 China has a 
nine-year 
compulsory 
education 
system covering 
primary and 
junior secondary 
levels.
Culture Knowledge in Real World
In India, the 
greeting 
“Namaste” is 
done with 
palms pressed 
together.
Spain 
traditionally has 
a midday siesta, 
with shops 
closing in the 
afternoon.
In China, the 
concept of “一线
城市” (first-tier 
cities) such as 
Beijing, Shanghai, 
and Shenzhen is 
widely 
understood
American culture
emphasizes individual
freedom, often
expressed in the 
phrase
“life, liberty, and the
pursuit of happiness.”
CommonSense Norms
Behaviors and Habits
Values and Society
Chinese has 
specific terms for 
different uncles 
and aunts 
depending on 
family side and 
age.
Figure 1: The classification of real-world cultural knowledge
is inherently complex and diverse, encompassing a wide
range of aspects such as institutions, geography, behavioral
habits, etiquette, values, and social structures. Existing eval-
uation datasets often fail to comprehensively and accurately
cover these types of knowledge.
Therefore, how to comprehensively and accurately evaluate
LLMs’ cultural understanding abilities in specific cultural
contexts has become an urgent issue that must be addressed
for their broader adoption.
Cultural understanding refers to a model’s ability to com-
prehend culturally grounded definitions and concepts, iden-
tify cultural stereotypes or biases, and appropriately apply
cultural knowledge in real-world or context-sensitive sce-
narios(Earley, Earley, and Quotes 2002). As is shown in Fig-
ure 1, culture is a complex and holistic concept(Tylor 1871),
and cultural knowledge in the real world scenarios encom-
passes multiple dimensions. Despite growing efforts in the
evaluation and enhancement of cultural understanding, ex-
arXiv:2509.16188v1  [cs.CL]  19 Sep 2025

--- Page 2 ---

Value Orientation Theory
Cultural Patterns
Cultural Iceberg
Model
Experts In 
Culture Studies
Geography and Customs
Population and Geography
Dates of Significance
Institutional Norms
Behavioral Patterns
Core Vaues and Social Structures
18 Topic Aspects
5 Categories
3 Cultural Layers
140 Detailed 
Dimensions
Hofstede’s Cultural 
Dimensions Theory
Social Memory Theory
Design
Regulation and Policy
Transportation Rules
Data Format
Measurement Unit
Financial Market Rules
Personal Choices and Habits
Daily Life and Travel
Diet and Health Concept
Education and Knowledge
Art and Entertainment 
Etiquette and Courtesy
Values and Beliefs
Religion
Do’s and Don’ts
Culture Values
Social Relationship 
and Structures
Family Dynamics
Household Structures
Gender Roles
Fixed Expressions in 
Language
National holidays
Religious holidays
Origin of festivals
Celebration of festivals
 Existing Cultural Studies
Culture Knowledge Extraction
DIMENSION: 
Celebration of Festivals
KNOWLEDGE:
Use of Symbolic Elements: Symbolic 
elements such as fire, water, and 
specific foods play crucial roles in many 
Spanish festivals. Fire is especially 
prominent in celebrations like Las 
Fallas and San Juan’s Night.
Question Generation
QUESTION:
During the festival of Las Fallas in Valencia, which element is 
prominently featured and plays a significant role in the celebrations?
A) Ice sculptures  B) Fireworks and bonfires  
C) Water fountains  D) Sandcastles
ANSWER:
B) Fireworks and bonfires
Las Fallas is a famous festival in Valencia, Spain, where fire is a central 
and symbolic element.         
REFERENCE:
Use of Symbolic Elements: Symbolic elements such as fire, water, and 
specific foods play crucial roles in many Spanish festivals. Fire is 
especially prominent in celebrations like Las Fallas and San Juan’s 
Night.
Please think step by step about all relevant 
cultural points based on the context, and 
generate a Factual question. The question 
type can be multiple choice, true/false, or fill-
in-the-blank. Please ensure that the question 
stem is clear, the options are plausible and 
distracting, and the answer is accurate.
Dimensional Schema 
of CultureScope
Data Collection and 
Generation Pipeline
Celebration of Festivals in 
Spanish culture
Professional 
Cultural 
Websites
Google 
Search
Engine
Relevance Filtering
Format Rewriting
Specified
Prompts
Question
Generator
Quality
Verifier
Knowledge Conformity 
True
Logical Consistency 
True
Result
Success
Deduplication
Symbolic Events
Community and Unity
Religious Celebrations
1100+ Keywords
Clustering
Figure 2: The overall framework of CultureScope. The framework can be applied to the evaluation of cultural understanding
ability in any target culture. We invite experts in culture studies to to develop the most comprehensive knowledge classification
schema to date for evaluating the cultural understanding of large language models, based on the most influential existing
cross-cultural and mono-cultural theories. This framework enables more fine-grained analysis and interpretation of LLMs’
performances on specific cultural dimensions.
isting benchmarks still suffer from significant limitations.
First, existing evaluations tend to lack comprehensive-
ness, which limits their practical utility, and the assessed
capability scores may be misaligned with real-world risks
and alignment requirements. Previous studies either directly
rewrite existing surveys(Jiang et al. 2024; Zhao et al. 2024;
Li et al. 2024), or generate and manually annotate data by
selecting a small number of keywords(Chiu et al. 2024; Lee
et al. 2024; Myung et al. 2024). Their classification frame-
works for cultural knowledge dimensions lack rigorous the-
oretical guidance and tend to rely on intuitive and empiri-
cal experience. Second, existing evaluation benchmarks are
difficult to scale and adapt to other cultural and linguistic
contexts, as they heavily rely on manual annotation(Myung
et al. 2024; Palta and Rudinger 2023; Mousi et al. 2024). The
high cost, labor intensity, and cultural specificity of manual
labeling limit their scalability and hinder their generalizabil-
ity across diverse cultural settings. Moreover, many exist-
ing evaluations mainly test cultural knowledge, but a com-
prehensive assessment should also examine whether models
can recognize cultural bias and apply cultural knowledge in
context, closer to real-world scenarios.
In this paper, we propose CultureScope, an automated,
scalable, and currently the most comprehensive evaluation
framework for LLMs’ cultural understanding capabilities.
To address the issues above, we argue that the evalua-
tion framework for cultural understanding should meet four
key criteria: comprehensiveness, operability, interpretabil-
ity, and scalability. As is shown in Figure 2, to ensure
that our framework provides comprehensive coverage of
cultural knowledge, we first introduce a dimension-based
schema for classifying cultural knowledge. This schema is

--- Page 3 ---

Benchmark
Theoretical
Guidance
Commonsense
Norms
Behaviors
& Habits
Values
& Society
Transferability
to other cultures
Number of
dimensions
BLEnD(2024)
6
CultureLLM(2024)
7
WorldValuesBench(2024)
12
KorNAT (2024)
/
ARADICE (2024)
30
Ours(CultureScope)
140
Table 1: Existing benchmarks lack guidance from well-established cultural theories, with dimension systems largely designed
based on empirical heuristics. As a result, they provide limited coverage of cultural knowledge, hindering comprehensive
evaluation of culture understanding. Moreover, the reliance on manual annotation in many existing methods leads to limited
automation and poses significant challenges in extending them to diverse cultural contexts.
grounded in existing cultural studies and represents the most
comprehensive classification system to date, enabling more
systematic, comparable, and fine-grained assessments of
large language models’ abilities across specific cultural di-
mensions. Using the sub-dimensions defined in this schema
as a foundation, we then automatically extract cultural
knowledge instances and construct cultural understanding
evaluation datasets for Chinese and Spanish cultures. Fur-
thermore, we expand the schema by clustering the extracted
cultural knowledge.
We conduct extensive evaluations of existing LLMs us-
ing our constructed evaluation datasets. Our findings indi-
cate that cultural capability fundamentally involves the mas-
tery and application of cultural knowledge. Relying exclu-
sively on linguistic knowledge is insufficient for improving
a model’s cultural alignment, and deeper reasoning does not
inherently lead to better cultural competence. Furthermore,
existing models perform inconsistently across different cul-
tural dimensions and languages, which provides clear guid-
ance for targeted enhancements of the models.
Our contributions are as follows:
• Building on previous monocultural and cross-cultural re-
search, we propose the most comprehensive framework
to date for assessing LLMs’ capabilities in specific cul-
tural contexts. This framework captures both surface-
level practices and deep-level assumptions in a certain
culture, covering a wide range of cultural knowledge, in-
cluding cultural facts, behavioral norms, values, and be-
liefs, enabling automatic data generation and can be flex-
ibly extended to any given culture.
• We extract a substantial volume of cultural knowledge
embedded in specific cultural contexts from various data
sources, which can facilitate subsequent evaluation and
training of LLMs. These cultural knowledge possess high
quality, and the accuracy of knowledge instances re-
trieved and generated in different languages remain com-
parable.
• We construct several comprehensive evaluation datasets
and conduct a series of extensive experiments on com-
monly used LLMs to evaluate their cultural understand-
ing abilities. The performances of these LLMs vary sig-
nificantly across different cultural dimensions and lan-
guages. Enhancing models solely through multilingual
data and deep reasoning is insufficient to achieve stable
improvements in cultural understanding.
Related Work
Culture Understanding Benchmarks
In recent years, the evaluation and improvement of LLMs’
cultural understanding capabilities have received significant
attention within the research community and industry. These
capability assessments can broadly be divided into two cate-
gories. (1) Question answering on factual knowledge within
specific cultural contexts(Onohara et al. 2024; Singh et al.
2024; Nayak et al. 2024), and (2) Evaluation of cultural val-
ues and moral reasoning(Hadar-Shoval et al. 2024; Karin-
shak et al. 2024; Aksoy 2025; Ji et al. 2025). Common data
construction methods include manual annotation and LLM
generation. However, current research on the evaluation of
LLMs’ cultural understanding capabilities still faces notable
limitations. Table 1 provides a detailed comparison between
our evaluation benchmark and previous works. On one hand,
most existing evaluation benchmarks are not grounded in
robust theoretical frameworks, and their dimensional struc-
tures are typically based on intuitive, experience-driven
approaches. As a result, their evaluation frameworks fail
to cover a broad spectrum of cultural knowledge and can-
not fully reveal the limitations and areas for improvement of
LLMs in culturally rich scenarios. On the other hand, ex-
isting methods often rely on expert manual annotation,
which incurs high data generation costs and makes it dif-
ficult to scale to other cultures. Some datasets even involve
hundreds of annotators, which is evidently costly and diffi-
cult to replicate.
Multilingual Large Language Models
Multilingual Large Language Models (LLMs)(Lai et al.
2023) can be broadly categorized into two major paradigms.
The first paradigm consists of general-purpose multilingual
models trained from scratch on massive multilingual cor-
pora(Xu et al. 2025; Wang et al. 2024; Wei et al. 2023).

--- Page 4 ---

These models emphasize learning multilingual representa-
tions that cover dozenof languages. The second paradigm
focuses on continued training or fine-tuning of existing
general-purpose models to enhance their multilingual capa-
bilities(Kadiyala et al. 2025; Toraman 2024; Thillainathan
et al. 2025). However, whether multilingual training data
alone can enable models to fully acquire corresponding cul-
tural understanding remains an open question(Wang et al.
2023; Juanda et al. 2024). Cultural knowledge involves com-
plex social norms and contextual nuances that may not be
fully captured by multilingual text corpora(Morris et al.
2015), and further research is needed to evaluate and im-
prove the cultural competence of these models.
CultureScope Framework
We propose the most comprehensive, automated, and exten-
sive evaluation framework to date for evaluating LLMs’ cul-
tural understanding capabilities, which can be flexibly ex-
tended to any given cultures. This framework comprises 3
layers, 5 categories, 18 topic aspects and 140 dimensions.
Dimensional Schema Design
Classification Principles
To comprehensively and scien-
tifically evaluate the cultural understanding capability of
LLMs, the dimensional framework for classifying cultural
knowledge should satisfy four core principles. 1) Compre-
hensiveness: The dimensions should cover cultural knowl-
edge as fully as possible. 2) Operationalizability: The
framework should effectively guide data collection and the
practical construction of knowledge bases. 3) Interpretabil-
ity: It should enable clear attribution analysis of model be-
haviors, revealing preferences and performance variations
across dimensions. 4) Extensibility: The system should be
designed for high scalability through data-driven expansion,
supporting increasingly fine-grained evaluation in the future.
Dimensional Schema
Drawing inspiration from the cul-
tural iceberg theory (Hall 1976; Baker 2009), we construct
a hierarchical classification of cultural knowledge that cap-
tures both surface-level practices and deep-level assump-
tions, dividing it into three layers: Institutional Norms, Be-
havioral Patterns, and Core Values and Social Structures.
The three layers respectively cover cultural knowledge of
common norms (e.g., geography and festivals), behaviors
and habits, and underlying values and social structures. As
is shown in Figure 2, the schema is divided into four levels:
Culture Layer, Category, Topic Aspect, and Detailed Dimen-
sion, which provides systematic dimensions against which
LLMs’ cultural understanding can be rigorously assessed.
The detailed content of the proposed dimensional schema is
shown in Appendix.
Cultural Knowledge Extraction
Some studies have found that even datasets widely re-
garded as reliable, such as Wikipedia, still exhibit cultural
biases(Naous et al. 2023). Therefore, in our data construc-
tion process, we incorporate complementary data sources to
ensure diversity and to mitigate the risk of bias from relying
Size
Knowledge Instances
Evaluation Dataset
En
Local
En
Local
Spanish
2767
2483
11.09k
10.68k
Chinese
3177
3535
11.2k
11.2k
Table 2: Statistics of CultureScope. We report the number of
knowledge instances in each language-specific contexts. The
number of data samples is the same across different types
of question content(Factual, Conceptual, Misleading, Multi-
hop) across languages.
Culture
Annotator
Knowledge
Evaluation Dataset
Spanish
Annotator1
98.57%
99.46%
Annotator2
97.85%
99.12%
Chinese
Annotator1
97.14%
100.0%
Annotator2
99.29%
99.11%
Table 3: The quality assessment results of the cultural
knowledge and the evaluation dataset via manual sampling
inspection. The validation of the cultural knowledge in-
stances focuses on identifying factual or expression-related
errors, and the quality of the evaluation set emphasizes the
logical consistency among the question, the answer, and the
reference knowledge
on a single source. The data construction process of Cul-
tureScope takes into account two types of data sources. The
first is manually selected professional cultural websites1.
These sites offer highly reliable content, but the amount of
data, the coverage across dimensions is limited, and data ex-
traction often requires specialized processing. The other is
data retrieved through Google search. This method allows us
to cover the full range of dimensions, and provides a large
and scalable volume of data, but the quality of the content
requires further verification. We convert the fine-grained di-
mensions in the dimensional schema into search keywords
and combine them with the target culture to construct re-
trieval queries(e.g., Celebration of Festivals in Spanish cul-
ture). In this step, we apply GPT-4o to filter the page content,
summarize and extract information from the retrieved texts.
Evaluation Dataset Generation
We draw on cognitive science theories(Wilberschied and
Lee 2015; Avgousti 2018; Feng, Aziz, and Dalib 2025) to
define four content types for our questions: Factual, Concep-
tual, Misleading and Multi-hop, as this design ensures that
the evaluation not only probes different facets of cultural
knowledge but also reflects the practical challenges mod-
els face in real-world cultural understanding and interac-
tion. These four question types respectively assess whether
the model knows cultural facts, understands the underlying
meaning of cultural phenomena, can identify cultural biases,
and is able to synthesize multiple cultural elements while
1For example, https://culturalatlas.sbs.com.au/

--- Page 5 ---

(a) Spanish Cultural Knowledge
(b) Chinese Cultural Knowledge
Figure 3: Distribution of Retrieved Cultural Knowledge in Spanish and Chinese. These cultural knowledge instances are col-
lected from multiple sources under the guidance of the dimensional schema, and their distribution is consistent with the dimen-
sions defined in the schema.
grasping the deeper logic or internal connections among cul-
tural phenomena. The question formats include multiple-
choice, true/false, short answer, and essay questions. For
each type of question, we apply specific expert-designed
prompts to clearly define the task requirements. Question
generation is based on a Retrieval-Augmented Generation
(RAG)(Lewis et al. 2020) approach, randomly selecting a set
of cultural rules for the LLM to reference during generation.
Detailed prompt formulations are provided in the Appendix.
Quality Control
For cultural knowledge and generation-related tasks, the
framework provides LLM-based quality evaluation and fil-
tering. For the validation of cultural knowledge, we primar-
ily focus on the consistency between the rewritten content
and the source webpages, since we found that when using
queries such as “eating habits in Spanish culture”, the top
five results returned by Google are consistently high-quality
webpages that are highly relevant to the target dimension of
the query. In addition to widely recognized platforms such
as Wikipedia, these results also include official releases from
relevant government agencies of the target country, author-
itative media outlets, long-established authoritative tourism
information portals and so on.
On the other hand, the evaluation of the generated ques-
tions primarily focuses on examining the logical consistency
among the question itself, the provided answer, and the un-
derlying reference cultural knowledge. Specifically, it as-
sesses whether the question is formulated in a way that is
coherent with the reference knowledge, whether the corre-
sponding answer logically follows from the question, and
whether any contradictions or reasoning errors arise across
these three components.
Evaluation Benchmark
Dataset Construction
Leveraging the proposed framework, we independently con-
struct evaluation datasets grounded in Chinese culture and
Spanish-speaking cultural contexts. For each culture, we
conduct knowledge extraction and evaluation dataset gen-
eration in both English and the corresponding native lan-
guage (i.e., Spanish or Chinese). We conduct a categorical
analysis of the source websites of the cultural knowledge in-
stances. The distribution of webpage types is shown in Ap-
pendix. We find that online cultural data is inherently het-
erogeneous, with a broad spectrum of sources that comple-
ment each other. In addition, we cluster the extracted culture
knowledge instances, obtaining 1.1k cultural keywords to
further enrich the dimensional schema.
Evaluation Metric
We adopt an automated evaluation method to analyze and
summarize results on the dataset, using answer accuracy as
the primary metric, defined as the proportion of correct re-
sponses over all evaluated items. For objective questions
(e.g., multiple-choice, true/false), we apply direct answer
matching: a prediction ˆy is marked correct if it matches the
ground truth y. For subjective questions(e.g., short answers,
essays), we adopt the LLM-as-a-Judge approach(Desmond

--- Page 6 ---

Models
Spanish Culture
Chinese Culture
Lang
Acc
G & C
PC & H
R& P
SR & S
V & B
Lang
Acc
G & C
PC & H
R& P
SR & S
V & B
General-purpose models
Qwen2.5-7B
en
0.832
0.850
0.808
0.800
0.958
0.868
en
0.741
0.883
0.681
0.740
0.771
0.829
sp
0.659
0.750
0.620
0.640
0.688
0.737
cn
0.827
0.800
0.815
0.810
0.896
0.868
Qwen2.5-14B
en
0.870
0.883
0.851
0.840
0.958
0.908
en
0.783
0.917
0.761
0.717
0.750
0.867
sp
0.745
0.767
0.728
0.730
0.771
0.790
cn
0.871
0.917
0.844
0.880
0.896
0.908
Qwen2.5-32B
en
0.861
0.900
0.848
0.820
0.896
0.908
en
0.798
0.917
0.772
0.740
0.854
0.842
sp
0.753
0.817
0.714
0.710
0.792
0.880
cn
0.586
0.667
0.583
0.550
0.563
0.592
Llama3-8B
en
0.800
0.783
0.786
0.760
0.938
0.829
en
0.651
0.683
0.627
0.576
0.792
0.720
sp
0.563
0.567
0.554
0.480
0.625
0.658
cn
0.655
0.610
0.634
0.600
0.729
0.790
GPT-4o
en
0.875
0.850
0.870
0.840
0.938
0.921
en
0.780
0.850
0.765
0.690
0.750
0.921
sp
0.761
0.850
0.710
0.770
0.813
0.829
cn
0.773
0.800
0.765
0.750
0.771
0.816
Deep-reasoning models
Deepseek-r1
en
0.845
0.733
0.851
0.810
0.938
0.895
en
0.837
0.883
0.801
0.840
0.854
0.921
sp
0.664
0.810
0.629
0.586
0.729
0.737
cn
0.870
0.917
0.848
0.840
0.896
0.934
Deepseek-v3
en
0.879
0.933
0.859
0.860
0.938
0.895
en
0.794
0.900
0.743
0.790
0.851
0.868
sp
0.644
0.683
0.623
0.660
0.542
0.733
cn
0.675
0.683
0.659
0.640
0.688
0.763
Qwen3-8B
en
0.834
0.833
0.786
0.870
0.979
0.868
en
0.796
0.867
0.757
0.770
0.833
0.895
sp
0.734
0.817
0.703
0.720
0.792
0.763
cn
0.893
0.917
0.877
0.890
0.896
0.934
Qwen3-8B-f
en
0.827
0.833
0.804
0.800
0.958
0.855
en
0.779
0.900
0.750
0.740
0.792
0.829
sp
0.713
0.817
0.688
0.680
0.688
0.776
cn
0.838
0.867
0.823
0.810
0.875
0.882
Models Continually-trained on Multilingual Corpus
PolyLM-7B
en
0.113
0.133
0.130
0.090
0.042
0.105
en
0.111
0.133
0.091
0.120
0.167
0.118
sp
0.057
0.083
0.044
0.040
0.083
0.092
cn
0.141
0.117
0.145
0.140
0.125
0.158
PolyLM-13B
en
0.458
0.367
0.491
0.390
0.500
0.474
en
0.225
0.150
0.243
0.172
0.292
0.250
sp
0.204
0.200
0.207
0.250
0.063
0.224
cn
0.330
0.283
0.330
0.330
0.250
0.421
Table 4: Main evaluation results on Spanish culture and Chinese culture. We evaluate the question-answer accuracy of several
types of LLMs on different languages and cultural categories mentioned above. Lang refers to the language of the questions.
Qwen3-8B-f refers to Qwen3-8B without deep reasoning enabled. Abbreviations follow a consistent pattern: for example,
“G&C” stands for Geography and Customs; other abbreviations follow the same convention.
et al. 2025), where the question q, reference answer aref,
and model-generated answer atest are jointly evaluated by a
Judge Model to determine whether atest aligns with the key
semantic content of aref.
Due to the flexibility of answers in subjective questions,
we require the Judge Model to compare the reference answer
with the model-generated answer and determine whether the
content of the latter conflicts with the cultural knowledge in
the reference. If a conflict exists, the answer is considered
incorrect. This approach ensures that the evaluation captures
cultural understanding while allowing a certain degree of an-
swer flexibility.
Acc = 1
N
N
X
i=1
1
 ˆyi = yi,
Obj
Judge(qi, aref
i , atest
i ),
Subj

(1)
Statistics
Our constructed benchmark consists of 11962 cultural
knowledge instances and 44.1k questions in total, Table 2
shows the detailed statistics of each culture and language.
The distribution of the English version of the cultural knowl-
edge instances is illustrated in Figure 3. The distribution of
cultural knowledge instances exhibits a trend similar to that
of the dimensions in the schema, a pattern that holds consis-
tently across different languages.
We invite human experts to manually evaluate the quality
of the culture knowledge and the correctness of the evalu-
ation dataset. Table 3 shows the quality evaluation results
of the constructed benchmark. The validation of cultural
knowledge focuses on identifying factual or expression-
related errors, whereas the evaluation of the dataset ques-
tions emphasizes the logical consistency among the ques-
tion, the answer, and the reference knowledge. The results
show that the generated cultural knowledge and evaluation
questions are of high quality and can be used to assess
the cultural understanding capabilities of LLMs, which also
validates the effectiveness of our automatic quality control
method.
Experiments
We carry out a series of experiments to examine: 1) To
what extent can current LLMs align with specific cultural
knowledge. 2) What are the factors that influence the per-
formances of LLMs on culture-specific knowledge-related
tasks. 3) Whether there is a noticeable difference in the per-
formances of LLMs across different cultural dimensions,
languages, and types of question.
Models and Implementation
Our evaluation include
three types of LLMs: General-purpose models, includ-
ing Qwen2.5-7B-Instruct, Qwen2.5-14B-Instruct, Qwen2.5-
32B-Instruct(Qwen Team et al. 2024) and GPT-4o(Hurst
et al. 2024); Deep-reasoning models and its non-deep-
reasoning version, including Qwen-3(Yang et al. 2025),
Deepseek-r1(Guo et al. 2025)and Deepseek-v3(Liu et al.
2024); models trained specifically on multilingual data, in-
cluding polylm-qwen-7b and polylm-qwen-13b(Wei et al.
2023). All experiments are conducted using NVIDIA A800

--- Page 7 ---

Figure 4: Models’ performances across different question
content types. Factual evaluates the understanding of factual
cultural knowledge; Conceptual assesses the models’ grasp
of the deeper meanings of cultural concepts; Mislead exam-
ines whether the models can detect cultural bias; and Multi-
hop evaluates the models’ ability to apply cultural knowl-
edge in real-world communicative scenarios.
GPUs with 80GB memory. Local models are loaded us-
ing FP16 precision and implemented with PyTorch and the
Transformers library. The generation limit is 1024 new to-
kens.
Results
The overall performances of all LLMs are listed in Table 4.
We evaluate different models across all dimensions, lan-
guages, and question types, and analyzed potential influenc-
ing factors.
Observation 1: The cultural understanding ability of
LLMs is language-dependent. Overall, as is shown in Ta-
ble 4, the accuracy of model responses to cultural ques-
tions is directly related to the language of the questions. For
Spanish-speaking cultures, When the language switch from
English to Spanish, all models show a trend of accuracy de-
cline. However, for Chinese culture, many models perform
better on questions in Chinese than in English. This indicate
that there is still a performance gap between current LLMs
in English and other relatively low-resource languages.
On the other hand, the models demonstrate a culture-
specific weakness in identifying cultural bias. As is shown
in Figure 4, the models’ performances on handling Mislead-
Figure 5: Different models’ performance variation with dif-
ferent amounts of injected cultural knowledge via prompts.
type questions are significantly lower than on other types
within Spanish culture, while in Chinese culture, such a
disparity is less pronounced and exhibits lower consistency
across models. This suggests that the models may be more
susceptible to misleading content or less robust in reason-
ing under deception in specific cultural contexts, highlight-
ing potential cultural sensitivity or bias in their reasoning
capabilities.
Meanwhile, all models exhibit varying performances
across different Topic Aspects. We evaluate the finer-
grained Categories within each Layer and present a subset
of the results in the Figure 7, and the complete results can
be found in the Appendix. In the context of Spanish cul-
ture, as the cultural knowledge evaluation progresses from
shallow to deep layers, the models exhibit increasing perfor-
mance divergence within the same dimension when ques-
tioned in different languages. At the Institutional Norm
Layer, all models perform poorly on questions related to
Measurement Units, while demonstrating better mastery of
knowledge concerning Dates of Significance. At the Core
Values and Social Structures Layer, for Family Dynamics
and Household Structures, almost all models answer English
questions very well but perform poorly on Spanish ones.
For Chinese culture, however, as the evaluation deepens, the
models’ performances across different languages tend to sta-
bilize within the same dimension.
Observation
2:
Larger
models
typically
exhibit
stronger performance on cultural understanding tasks,
as they encode a broader range of knowledge. Models
from the same series exhibit a generally positive correla-
tion between performance and model size. On one hand,
for Spanish culture, increasing model size consistently leads
to notable performance gains across all models on Spanish-

--- Page 8 ---

Figure 6: Performances of models on the Institutional Norms Layer and Core Values and Social Structures Layer, within the
Spanish cultural context. For institutional norms, performances across dimensions is similar in both English and Spanish.
However, for values and social structures, many dimensions exhibit significant differences between the two languages, such as
Family Dynamics and Religion.
language questions. On the other hand, for Chinese culture,
as the scale increases, nearly all models show improved per-
formance on both English and Chinese questions.
Observation 3: Deep reasoning does not inherently
yield substantial gains on cultural understanding capa-
bility When a model does not possess adequate knowledge
of the relevant culture, deeper reasoning processes may not
lead to better performance on cultural questions. Although
models with deep thinking enabled outperform those with-
out it in the context of Chinese culture, a similar advantage
is not observed for Spanish-speaking cultures. Deep think-
ing models we used(Deepseek-r1 and Qwen3) were trained
on larger Chinese corpora and thus possess stronger Chi-
nese language capabilities. This suggests that deep thinking
yields greater benefits only when the model has been trained
on sufficiently rich corpora in the target language. Without
access to relevant knowledge, no amount of reasoning can
fully compensate for the limitations in cultural understand-
ing.
Observation 4: Language̸=Culture. As shown in the
Figure 7, compared to the similarly sized Qwen models,
PolyLM(Wei et al. 2023), which incorporates additional
multilingual data, exhibits a significant performance drop
for both Spanish and Chinese cultures, rather than an im-
provement. This indicates that multilingualism does not
equate to multicultural understanding, and increasing the
proportion of data in a particular language during training
does not necessarily enhance cultural capability evaluation.
Observation 5: Incomplete external cultural knowl-
edge can impair the model’s performance on cultural
understanding tasks. Figure 5 shows the models’ perfor-
mance on the evaluation dataset when injecting 0, 1, 2, and 3
pieces of cultural knowledge instances via prompts. We ob-
serve that when only a small amount of external knowledge
is injected, the model’s performance is even worse than rea-
soning solely with its internal knowledge. Only when a suffi-
cient amount of relevant external cultural knowledge is pro-
vided does a model’s performance improve, and the amount
of cultural knowledge required for performance gains varies
across different models.
Conclusion
In this study, we address the critical challenge of system-
atically and comprehensively evaluating the cultural under-
standing capability of LLMs. We propose a theoretically
grounded and extensible cultural knowledge dimensional
framework that satisfies four core principles: comprehen-
siveness, operationalizability, interpretability, and scalabil-
ity. In this framework, we develop an automated pipeline to
extract high-quality culture knowledge instances and evalu-
ation datasets across any given languages and cultures. Our
experimental results on Spanish and Chinese cultures reveal
that models exhibit significant differences in cultural capa-
bility across languages and dimensions. We find that cul-
tural capability fundamentally depends on a model’s cul-
tural knowledge rather than on language knowledge alone,
and that deep reasoning does not reliably compensate for
cultural knowledge gaps. These findings highlight the lim-
itations of conventional multilingual training for achieving
true cultural alignment, which offers valuable insights for
the future training, evaluation, and deployment of culturally
aligned LLMs.

--- Page 9 ---

Ethical Statement
This work involves the construction and use of a large-scale
cultural understanding evaluation dataset, which contains
content ranging from common cultural norms to sensitive
aspects such as values and beliefs. The data was collected
exclusively from publicly available internet sources, includ-
ing educational materials, open-access cultural databases,
and publicly shared questionnaires or forums. No private,
proprietary, or identifiable personal data was included. We
acknowledge that cultural data can reflect deeply held val-
ues and potentially contentious viewpoints. In constructing
the dataset, we took care to avoid harmful stereotypes and
minimizing cultural bias. When selecting and annotating the
data, we consulted domain experts in cultural studies to en-
sure contextual fidelity and respect toward the represented
communities. Furthermore, the dataset is intended solely
for research purposes, such as evaluating the capabilities of
language models in understanding cultural knowledge. It is
not designed to make normative claims about cultures, nor
should it be used for profiling, ranking, or stereotyping in-
dividuals or groups. To mitigate risks of misuse, we restrict
the release of the dataset under a research-use license and
require users to agree not to employ it for downstream ap-
plications that could cause harm, including but not limited to
cultural discrimination, misinformation propagation, or au-
tomated decision-making in sensitive contexts (e.g., hiring,
immigration, education). We are committed to ongoing eth-
ical reflection and welcome feedback from cultural commu-
nities, stakeholders, and the wider research community.
References
Aksoy, M. 2025. Whose morality do they speak? Unravel-
ing cultural bias in multilingual language models. Natural
Language Processing Journal, 100172.
AlKhamissi, B.; ElNokrashy, M. N.; AlKhamissi, M.; and
Diab, M. 2024. Investigating Cultural Alignment of Large
Language Models. ArXiv, abs/2402.13231.
Avgousti, M. 2018.
Intercultural communicative compe-
tence and online exchanges: a systematic review. Computer
Assisted Language Learning, 31: 819 – 853.
Baker, W. 2009. The cultural iceberg.
Benkler, N.; Mosaphir, D.; Friedman, S. E.; Smart, A.; and
Schmer-Galunder, S. 2023.
Assessing LLMs for Moral
Value Pluralism. ArXiv, abs/2312.10075.
Chiu, Y. Y.; Jiang, L.; Lin, B. Y.; Park, C. Y.; Li, S. S.; Ravi,
S.; Bhatia, M.; Antoniak, M.; Tsvetkov, Y.; Shwartz, V.;
et al. 2024. CulturalBench: a Robust, Diverse and Challeng-
ing Benchmark on Measuring (the Lack of) Cultural Knowl-
edge of LLMs.
Desmond, M.; Ashktorab, Z.; Geyer, W.; Daly, E. M.;
Cooper, M. S.; Pan, Q.; Nair, R.; Wagner, N.; and Pedapati,
T. 2025. EvalAssist: LLM-as-a-Judge Simplified. 29637–
29639.
Earley, E.; Earley, C.; and Quotes, P. 2002. Redefining inter-
actions across cultures and organizations: Moving forward
with cultural intelligence. Research in Organizational Be-
havior, 24: 271–299.
Feng, M.; Aziz, M. N. B. A.; and Dalib, S. 2025. Exploring
Intercultural Communicative Competence Among Chinese
Students: Insights from a Qualitative Study. SAGE Open.
Guo, D.; Yang, D.; Zhang, H.; et al. 2025. Deepseek-R1: In-
centivizing reasoning capability in LLMs via reinforcement
learning. arXiv preprint arXiv:2501.12948.
Hadar-Shoval, D.; Asraf, K.; Mizrachi, Y.; Haber, Y.; and
Elyoseph, Z. 2024. Assessing the alignment of large lan-
guage models with human values for mental health integra-
tion: cross-sectional study using Schwartz’s theory of basic
values. JMIR Mental Health, 11: e55988.
Hall, E. T. 1976. Beyond Culture. Garden City, New York:
Anchor Press / Doubleday. ISBN 9780385087476.
Hurst, A.; Lerer, A.; Goucher, A. P.; Perelman, A.; Ramesh,
A.; Clark, A.; Ostrow, A.; Welihinda, A.; Hayes, A.; Rad-
ford, A.; et al. 2024. Gpt-4o system card. arXiv preprint
arXiv:2410.21276.
Ji, J.; Chen, Y.; Jin, M.; Xu, W.; Hua, W.; and Zhang, Y.
2025. Moralbench: Moral evaluation of llms. ACM SIGKDD
Explorations Newsletter, 27(1): 62–71.
Jiang, L.; Sorensen, T.; Levine, S.; and Choi, Y. 2024. Can
language models reason about individualistic human values
and preferences? arXiv preprint arXiv:2410.03868.
Juanda; Azis; R, M.; Effendri, Y.; Putradi, A. W. A.; Purba,
B.; and Afandi, I. 2024.
Multilingualism and Cultural
Awareness: A Correlational Analysis in Language Educa-
tion in Indonesian Higher Education. Language Teaching
Research Quarterly.
Kadiyala, R. M. R.; Pullakhandam, S.; Gupta, S.; Sharma,
D.; Purbey, J.; Mehreen, K.; Arham, M.; and Farooq,
H. 2025.
Improving Multilingual Capabilities with Cul-
tural and Local Knowledge in Large Language Models
While Enhancing Native Performance.
arXiv preprint
arXiv:2504.09753.
Karinshak, E.; Hu, A.; Kong, K.; Rao, V.; Wang, J.; Wang,
J.; and Zeng, Y. 2024. Llm-globe: A benchmark evaluating
the cultural values embedded in llm output. arXiv preprint
arXiv:2411.06032.
Lai, V. D.; Ngo, N. T.; Veyseh, A. P. B.; et al. 2023. ChatGPT
Beyond English: Towards a Comprehensive Evaluation of
Large Language Models in Multilingual Learning.
arXiv
preprint arXiv:2304.05613.
Lee, J.; Kim, M.; Kim, S.; Kim, J.; Won, S.; Lee, H.; and
Choi, E. 2024. Kornat: Llm alignment benchmark for ko-
rean social values and common knowledge. arXiv preprint
arXiv:2402.13605.
Lewis, P.; Perez, E.; Piktus, A.; Petroni, F.; Karpukhin, V.;
Goyal, N.; K¨uttler, H.; Lewis, M.; Yih, W.; Rockt¨aschel, T.;
Riedel, S.; and Kiela, D. 2020. Retrieval-Augmented Gen-
eration for Knowledge-Intensive NLP Tasks. In Advances in
Neural Information Processing Systems 33 (NeurIPS 2020).
Red Hook, NY: Curran Associates, Inc. ArXiv:2005.11401.
Li, C.; Chen, M.; Wang, J.; Sitaram, S.; and Xie, X. 2024.
Culturellm: Incorporating cultural differences into large lan-
guage models. Advances in Neural Information Processing
Systems, 37: 84799–84838.

--- Page 10 ---

Liu, A.; Feng, B.; Xue, B.; et al. 2024. DeepSeek-V3 Tech-
nical Report. arXiv preprint arXiv:2412.19437.
Mohan, G.; Kumar, R. P.; Krishh, P. V.; Keerthinathan, A.;
Lavanya, G.; Meghana, M. K. U.; Sulthana, S.; and Doss,
S. 2024. An analysis of large language models: their impact
and potential applications. Knowl. Inf. Syst., 66: 5047–5070.
Morris, M.; yi Hong, Y.; Chiu, C.; and Liu, Z. 2015. Nor-
mology: Integrating insights about social norms to under-
stand cultural dynamics. Organizational Behavior and Hu-
man Decision Processes, 129: 1–13.
Mousi, B.; Durrani, N.; Ahmad, F.; Hasan, M. A.; Hasanain,
M.; Kabbani, T.; Dalvi, F.; Chowdhury, S. A.; and Alam, F.
2024. Aradice: Benchmarks for dialectal and cultural capa-
bilities in llms. arXiv preprint arXiv:2409.11404.
Myung, J.; Lee, N.; Zhou, Y.; Jin, J.; Putri, R.; Antypas,
D.; Borkakoty, H.; Kim, E.; Perez-Almendros, C.; Ayele,
A. A.; et al. 2024. Blend: A benchmark for llms on everyday
knowledge in diverse cultures and languages. Advances in
Neural Information Processing Systems, 37: 78104–78146.
Naous, T.; Ryan, M. J.; Ritter, A.; and Xu, W. 2023. Having
beer after prayer? measuring cultural bias in large language
models. arXiv preprint arXiv:2305.14456.
Nayak, S.; Jain, K.; Awal, R.; Reddy, S.; Van Steenkiste, S.;
Hendricks, L. A.; Agrawal, A.; et al. 2024. Benchmarking
vision language models for cultural understanding. arXiv
preprint arXiv:2407.10920.
Onohara, S.; Miyai, A.; Imajuku, Y.; Egashira, K.; Baek, J.;
Yue, X.; Neubig, G.; and Aizawa, K. 2024.
Jmmmu: A
japanese massive multi-discipline multimodal understand-
ing benchmark for culture-aware evaluation. arXiv preprint
arXiv:2410.17250.
Palta, S.; and Rudinger, R. 2023. FORK: A bite-sized test
set for probing culinary cultural biases in commonsense rea-
soning models. In Findings of the Association for Computa-
tional Linguistics: ACL 2023, 9952–9962.
Qwen Team, A. Y.; Yang, B.; Zhang, B.; Hui, B.; Zheng, B.;
Yu, B.; Li, C.; Liu, D.; Huang, F.; Wei, H.; Lin, H.; Yang,
J.; Tu, J.; Zhang, J.; Yang, J.; Yang, J.; Zhou, J.; Lin, J.;
Dang, K.; Lu, K.; Bao, K.; Yang, K.; Yu, L.; Li, M.; Xue,
M.; Zhang, P.; Zhu, Q.; Men, R.; Lin, R.; Li, T.; Xia, T.;
Ren, X.; Ren, X.; Fan, Y.; Su, Y.; Zhang, Y.; Wan, Y.; Liu,
Y.; Cui, Z.; Zhang, Z.; and Qiu, Z. 2024. Qwen2.5 Technical
Report. arXiv preprint arXiv:2412.15115.
Raiaan, M. A. K.; Mukta, M. S. H.; Fatema, K.; Fahad,
N. M.; Sakib, S.; Mim, M. M. J.; Ahmad, J.; Ali, M. E.;
and Azam, S. 2024. A review on large language models: Ar-
chitectures, applications, taxonomies, open issues and chal-
lenges. IEEE access, 12: 26839–26874.
Raza, M.; Jahangir, Z.; Riaz, M. B.; Saeed, M. J.; and Sat-
tar, M. A. 2025. Industrial applications of large language
models. Scientific Reports, 15(1): 13755.
Shen, S.; Logeswaran, L.; Lee, M.; Lee, H.; Poria, S.; and
Mihalcea, R. 2024. Understanding the Capabilities and Lim-
itations of Large Language Models for Cultural Common-
sense. 5668–5680.
Singh, S.; Romanou, A.; Fourrier, C.; Adelani, D. I.; Ngui,
J. G.; Vila-Suero, D.; Limkonchotiwat, P.; Marchisio, K.;
Leong, W. Q.; Susanto, Y.; et al. 2024. Global mmlu: Un-
derstanding and addressing cultural and linguistic biases in
multilingual evaluation. arXiv preprint arXiv:2412.03304.
Thillainathan, S.; Yuan, S.; Lee, E.-S. A.; Jayasena, S.; and
Ranathunga, S. 2025. Beyond Vanilla Fine-Tuning: Lever-
aging Multistage, Multilingual, and Domain-Specific Meth-
ods for Low-Resource Machine Translation. arXiv preprint
arXiv:2503.22582.
Toraman, C. 2024.
LlamaTurk: Adapting Open-Source
Generative Large Language Models for Low-Resource Lan-
guage. arXiv preprint arXiv:2405.07745.
Tylor, E. B. 1871. Primitive culture: researches into the de-
velopment of mythology, philosophy, religion, art, and cus-
tom, volume 2. J. Murray.
Wang, B.; Liu, Z.; Huang, X.; Jiao, F.; Ding, Y.; Aw, A.;
and Chen, N. F. 2023. SeaEval for Multilingual Foundation
Models: From Cross-Lingual Alignment to Cultural Reason-
ing. ArXiv, abs/2309.04766.
Wang, J.; Lu, Y.; Weber, M.; Ryabinin, M.; Chen, Y.; Tang,
R.; and Stenetorp, P. 2024. Multilingual pretraining using
a large corpus machine-translated from a single source lan-
guage. arXiv preprint arXiv:2410.23956.
Wei, X.; Wei, H.; Lin, H.; Li, T.; Zhang, P.; Ren, X.; Li,
M.; Wan, Y.; Cao, Z.; Xie, B.; et al. 2023.
Polylm: An
open source polyglot large language model. arXiv preprint
arXiv:2307.06018.
Wilberschied; and Lee, F. 2015. Intercultural Communica-
tive Competence: Literature Review. 2: 4.
Xu, Y.; Hu, L.; Zhao, J.; Qiu, Z.; Xu, K.; Ye, Y.; and Gu, H.
2025. A survey on multilingual large language models: Cor-
pora, alignment, and bias. Frontiers of Computer Science,
19(11): 1911362.
Yang, A.; Li, A.; Yang, B.; et al. 2025. Qwen3 Technical
Report. arXiv preprint arXiv:2505.09388.
Zhao, W.; Mondal, D.; Tandon, N.; Dillion, D.; Gray, K.;
and Gu, Y. 2024. Worldvaluesbench: A large-scale bench-
mark dataset for multi-cultural value awareness of language
models. arXiv preprint arXiv:2404.16308.
Supplementary Data
Experimental Results
We evaluate the finer-grained Cat-
egories within each Layer and the results are shown in Fig-
ure 7. The use of different languages leads to notable differ-
ences in cultural understanding capability across various di-
mensions. We find that the models perform differently across
different Layers depending on the cultural context.
In the context of Spanish culture, as the cultural knowl-
edge evaluation progresses from shallow to deep layers, the
model exhibits increasing performance divergence within
the same dimension when questioned in different languages.
At the Institutional Norm layer, evaluation results across dif-
ferent languages show a certain degree of consistency. All
models perform poorly on questions related to Measurement
Units, while demonstrating better mastery of knowledge

--- Page 11 ---

concerning Dates of Significance. At the Behavioral Habits
layer, models exhibit different preferences across languages.
For Art and Entertainment questions in English, all models
perform poorly, whereas on Spanish questions, Art and En-
tertainment outperforms other secondary dimensions. At the
Cultural Values layer, language-dependent preference differ-
ences become more pronounced. Nearly all models perform
well on Religion-related Spanish questions but poorly on
the same questions in English. Conversely, for Family Dy-
namics and Household Structures, almost all models answer
English questions very well but perform poorly on Spanish
ones.
In contrast, for Chinese culture, as the evaluation deepens,
the models’ performance across different languages tend to
stabilize within the same dimension.
Statistics
In addition to the statistics mentioned in the
main technical content, we also analyze the data distribution
and sources of the extracted cultural knowledge instances.
Figure 8 shows the statistics of data source for Spanish and
Chinese culture bases retrieved in corresponding languages.
The data sources of the two knowledge bases exhibit distinct
distributions: approximately 20% of the Spanish knowledge
base is derived from cultural and tourism websites, whereas
this source category accounts for only a small proportion in
the Chinese knowledge base. This highlights certain differ-
ences in the distribution of internet data across languages
within cultural contexts.
Figure 9 illustrates the distribution of cultural knowledge
across dimensions in different cultural knowledge bases re-
trieved using different languages. Despite notable differ-
ences in data sources among the knowledge bases, the
knowledge distributions appear to be largely consistent, fol-
lowing similar patterns that align with the number of dimen-
sions defined in the taxonomy. This suggests that the density
of culturally relevant textual content on the Internet is rela-
tively uniform across languages, and that through retrieval
and rewriting, comparable amounts of cultural knowledge
can be obtained for each dimension.
Detailed Dimensions
Our proposed dimension schema contains 4 levels, Cultural
Layers, Category, Topic Aspect and Fine-grained Dimen-
sions. There are in total 3 Cultural Layers, 5 Categories, 18
Topic Aspects and 140 Fine-grained Dimensions, encom-
passing a wide range of cultural knowledge from explicit
commonsense facts, behavioral patterns to implicit values.
We transfer the most detailed dimensions into keywords for
Google search, thereby effectively guiding the construction
and evaluation of the cultural knowledge base. A detailed
description of the dimensions is provided in Table 6.
Data Instances
This section provides representative samples from the con-
structed dataset, covering both cultural knowledge instances
and question examples in evaluation dataset.
Cultural Knowledge
The extracted cultural knowledge instances are organized
according to the evaluation dimensions. Each cultural
knowledge instance provides a characteristic description of
the corresponding cultural dimension as manifested in a spe-
cific cultural context, encompassing relevant commonsense
knowledge, shared beliefs, values, and more. During dataset
construction, we used the aforementioned fine-grained eval-
uation dimensions as cues for retrieval and rewriting. Cul-
tural knowledge associated with the same dimension is
grouped together. Furthermore, we clustered the knowledge
instances under each dimension to derive even more fine-
grained sub-dimensions, which can serve as references for
future dataset construction and evaluation. We provide a de-
tailed illustration of examples from the constructed knowl-
edge bases in Table 5.
Evaluation Dataset
As is mentioned in the main context, the questions in our
evaluation dataset are categorized into four types based on
their content: Factual, Conceptual, Misleading, and Multi-
hop reasoning. Each instance in the evaluation set consists
of a question, its corresponding answer, and the associated
cultural knowledge. The questions are categorized into sub-
jective types (short answer and essay questions) and ob-
jective types (single-choice, multiple-choice, and true/false
questions). Here, we present the examples organized by their
content types in Table 7.
Prompts
During the dataset construction process, we leveraged large
language models (LLMs) for text rewriting, question gener-
ation, and quality assessment. In these steps, we employed
carefully expert-designed prompts to guide the LLMs in
performing the corresponding tasks. These prompts are
language-specific and correspond to the language of the tar-
get data. Here, we present the prompts used across different
languages.

--- Page 12 ---

(a) Institutional Norms of Spanish culture
(b) Institutional Norms of Chinese culture
(c) Behavioral Patterns of Spanish culture
(d) Behavioral Patterns of Chinese culture
(e) Core Values and Social Structures of Spanish culture
(f) Core Values and Social Structures of Chinese culture
Figure 7: Performance of Models across Layers and Languages

--- Page 13 ---

Dimension
Knowledge
Clustered category
Alcohol
[1] Alcohol is deeply integrated into daily life
and social activities in Spain, such as drinking
beer with friends at bars or enjoying wine with
meals.
Cultural Integration
[2] The legal drinking age in Spain is 18, with
strict drink-driving laws (blood alcohol limit:
0.5 g/L).
Legal and Social Norms
[3] Spaniards practice moderate drinking, with
binge drinking being uncommon.
Drinking Habits and Moderation
[4] Beer and wine are the most popular alco-
holic beverages, with craft beer gaining popu-
larity.
Regional and Traditional Beverages
Physical Contact
[1] Spaniards emphasize physical contact as
a tactile and emotional expression to convey
friendliness, intimacy, or support.
Frequency and Context of Physical Contact
[2] Public displays of affection (e.g., holding
hands) between couples are widely accepted as
normal in Spanish culture.
Cultural Acceptance and Boundaries
[3] Friends use gestures like nudging arms,
linking arms, or holding shoulders to show ap-
preciation and support.
Forms of Physical Contact
[4] Casual touches (e.g., adjusting clothes or
lightly touching collars) signal approachability
and friendliness.
Forms of Physical Contact
Widely Spoken Languages
[1] Spanish is the official language in 20 coun-
tries and one U.S. territory (Puerto Rico).
Official Status and Recognition
[2] Spanish is widely spoken in regions like the
United States, parts of Africa, Asia, and Ocea-
nia. ”,
Geographical Distribution
[3] The majority of Spanish speakers reside in
Hispanic America, particularly Mexico (largest
population of native speakers).
Geographical Distribution
[4] Spanish is recognized as an official/co-
official language in international organizations
(UN, EU, OAS, African Union).
Official Status and Recognition
Table 5: Examples of extracted knowledge instances. Dimension refers to the finest-grained level used for retrieval and rewrit-
ing; these dimensions serve as keywords for Google search. Cluster category denotes the result of clustering the cultural knowl-
edge, with each piece of knowledge corresponding to a more fine-grained category.

--- Page 14 ---

(a) Spanish Culture
(b) Chinese Culture
Figure 8: Data Source Statistics for Different Extracted Cultural Knowledge Instances
(a) Spanish Cultural Knowledge in English
(b) Spanish Cultural Knowledge in Spanish
(c) Chinese Cultural Knowledge in English
(d) Chinese Cultural Knowledge in Chinese
Figure 9: The distribution of knowledge instances retrieved through searches in different languages.

--- Page 15 ---

Layer
Category
Topic Aspect
Fine-grained Dimension
population rank
population distribution
land area percentage
main regions
Population and
ethnicity
Geography
official languages
Geography & Customs
widely spoken languages
famous river
climate
national holidays
religious holidays
Dates of Significance
cultural holidays
origin of festivals
celebration of festivals
symbol of festivals
Institutional
Norms
vehicle movement rules
traffic signs and signals
Transportation Rules
pedestrian and non-motorized vehicles
motor vehicle driving rules
parking regulations
data order
separator type
year format
Data Format
month representation
zero-padding
natural language date
Regulation & Policy
calendar system
Measurement Unit
measurement system
localization
regulation structure
market type
entity type
access & licensing
conduct & compliance
Financial Market
capital & risk
Rules
monetary & payment system
finTech regulation
tax & accounting
international alignment
stability & resolution
payment habits
travel habits
Daily Life and Travel
bathing habits
pet-raising habits
social media usage pattern
marriage customs
Diet and Health
eating habits
Concept
attitudes towards birth, aging, illness and death
traditional and modern medicine
educational practices
Education and
teacher student concept
Knowledge
major selection
career choices

--- Page 16 ---

Layer
Category
Topic Aspect
Fine-grained Dimension
festive entertainment activities in different places
with the same origin
Art and Entertainment
traditional music and dance
contemporary art
basic etiquette
naming convention
name origin
name significance
punctuality when visiting
shoe etiquette during a visit
hospitality customs when receiving guests
bringing gifts for the host
seating etiquette for guests and hosts
serving etiquette during a visit
leaving food after eating
using salt while eating
giving compliments during a meal
eating with the right hand
alcohol
Personal Choices
pork
& Habits
handing gifts
gifts for children
opening gifts
general greeting principles
greeting between men and men
Behavioral
Etiquette and Courtesy
greeting between women and women
Patterns
greeting between men to women
appointment scheduling before the business meeting
dress code before the business meeting
business card exchange before the business meeting
network building before the business meeting
age and experience before the business meeting
familiarity before the business meeting
socialization during the business meeting
meeting duration during the business meeting
open door policy during the business meeting
interruptions during the business meeting
deference to senior during the business meeting
negotiation style during the business meeting
decision making during the business meeting
bartering during the business meeting
private meetings during the business meeting
confrontation avoidance during the business meeting
follow up after the business meeting
ongoing negotiations after the business meeting
communication style

--- Page 17 ---

Layer
Category
Topic Aspect
Fine-grained Dimension
indirect communication
humour
physical contact
personal space
gestures
beckoning
eye contact
idiom
Fixed Expressions
common saying
in Language
proverb
neologism and abbreviation
Family Dynamics
communal living
parental care
Social Relationship
patriarchy
and Structures
women roles in the family
Household Structures
social interaction
urban rural gap
concept of seniority and childhood
male dominance
Gender Roles
social compliance
Core Values
honour gender
and Social
changing attitudes of gender
Structures
power distance
collectivism
individualism
Culture Values
motivation towards achievement and success
uncertainty avoidance
long term orientation
indulgence
Values and
Religion
religion
Beliefs
modest dress
informality
compliments
cultural acknowledgement
education
Do’s and Don’ts
insults
dirty jokes
political criticism
sensitive topics
ethnicity assumptions
stereotyping
Table 6: The complete dimensional schema of CultureScope

--- Page 18 ---

Type
Question
Answer
Associated Knowledge
Factual
During the festival of Las Fallas in Valen-
cia, which element is prominently featured
and plays a significant role in the celebra-
tions? A) Ice sculptures B) Fireworks and
bonfires C) Water fountains D) Sandcastles
B) Fireworks and bon-
fires
Use of Symbolic Elements: Sym-
bolic elements such as fire, wa-
ter, and specific foods play crucial
roles in many Spanish festivals. Fire
is especially prominent in celebra-
tions like Las Fallas and San Juan’s
Night.
Mislead
You are a foreign exchange student in
Spain... *(long prompt truncated here for
brevity in description — see full LaTeX
for exact content)* ...Which of the fol-
lowing statements best reflects a criti-
cal understanding of Spanish culture? A)
My friend’s comment is accurate... B)
My friend’s comment reflects a common
stereotype... C) My friend’s comment is
partially correct... D) My friend’s comment
is entirely incorrect...
B)
My
friend’s
com-
ment reflects a common
stereotype, but it does not
accurately represent the
reality of modern Span-
ish families, where roles
are
more
flexible
and
shared.
Increasing
numbers
of
Spanish
women now pursue careers while
balancing family duties. In His-
panic households, daughters are ex-
pected to help with chores, while
sons participate less. In Spanish
culture, women traditionally take
primary responsibility for house-
hold chores and child-rearing.
Multi-
hop
Imagine you are a Spanish student... *(long
prompt truncated here)* 1. Contextual Un-
derstanding: What could be the possible
month... 2. Cultural Practices: Why do
you think shared meals... 3. Language and
Grammar: How would you abbreviate...
1. Likely July (Julio) or
August (Agosto), named
after Julius Caesar and
Augustus.
2.
Shared
meals foster community,
bonding, and family tra-
dition. 3. Abbreviations:
”jul.” / ”ago.”; lowercase
in
most
grammatical
uses.
Cultural significance of months:
Julio (Julius Caesar), Agosto (Au-
gustus); Sept–Dec = Latin numbers.
Food as bonding ritual in Spanish
culture. Grammar: months in lower-
case unless at sentence start; mascu-
line nouns; accepted abbreviations
like “en.” for enero.
Conceptual In a Spanish business context, you notice
that after a formal meeting, colleagues of-
ten suggest coffee or drinks. What is the
primary purpose? A) Finalize decisions B)
Build personal trust C) Discuss new oppor-
tunities D) Reduce stress
B) To build personal re-
lationships and trust out-
side of the formal setting
Informal
gatherings
(after-work
events, coffee breaks) build trust
and relationships outside formal
settings. Personal bonds are often
foundational before formal busi-
ness discussions in Spain.
Table 7: Examples of generated evaluation data set. Based on content classification, the evaluation dataset comprises four
distinct question types. Each question includes a prompt, a corresponding answer, and relevant cultural knowledge.

--- Page 19 ---

Knowledge Summary(English)
I will provide a web article. Please extract the key
characteristics and content related to the cultural di-
mension in Chinese culture from it. Present these
features clearly under distinct headings.
Each feature should begin with a section titled:
Title Then list the following points below:
Description of the feature:
Source of information: (Quote the original text and
indicate the paragraph if possible.)
The content should be well-structured and logically
coherent. If the information is insufficient to support
a certain feature, do not fabricate content.
The article is as follows:
===
Input Text
===
Knowledge Summary(Spanish)
Eres un investigador especializado en la cultura
espa˜nola. Se te proporcionar´a un texto de una p´agina
web (puede estar en cualquier idioma).
Tu tarea es identificar las caracter´ısticas culturales
que est´en relacionadas con el siguiente aspecto es-
pec´ıfico de la cultura espa˜nola:
Dimensi´on cultural:**dimension**
Por favor, extrae del texto solo los elementos rele-
vantes que est´en claramente relacionados con esta
dimensi´on cultural.
Escribe las caracter´ısticas en espa˜nol, siguiendo este
formato:
[T´ıtulo breve de la caracter´ıstica]
[Descripci´on clara y concisa en espa˜nol]
Fuente de informaci´on: [Frase, palabra clave o idea
tomada directamente del texto original]
Escribe siempre en espa˜nol. .
Texto de la p´agina web:
”””
Input text
”””
Question Instruction(Factual)
Based on the context, think through all relevant cul-
tural points step by step and generate a factual ques-
tion. The question type can include single-choice,
true/false, or fill-in-the-blank. Ensure that the ques-
tion stem is clear, the options are plausible but mis-
leading (distractors), and the answer is accurate.

--- Page 20 ---

Question Instruction(Conceptual)
Based on the context, think through all relevant cul-
tural points step by step and generate a conceptual
explanation question. The question should focus on
the learner’s understanding of the concepts, struc-
tures, or values behind cultural phenomena, rather
than simple memorization. Suitable formats include
multiple-choice or true/false questions. Ensure the
question is thought-provoking and the answer is
well-justified.
Question Instruction(Mislead)
Based on the context, think through all relevant cul-
tural points step by step and generate a mislead-
ing question to assess whether learners can identify
cultural misunderstandings, stereotypes, or biases.
The question should focus on learners’ critical think-
ing about culture, identifying which statements or
behaviors reflect misunderstandings, oversimplifica-
tions, biases, or stereotypes, and guide them toward
more accurate or respectful understandings. Possi-
ble formats include multiple-choice, true/false, case
analysis, or short-answer questions.
Question Instruction(Multi-hop)
Based on the context, think through all relevant cul-
tural points step by step and generate a multi-hop
reasoning question to assess whether the learner
can synthesize multiple cultural elements and under-
stand the deeper logic or internal connections among
cultural phenomena. The question should prompt
learners to start from multiple information points,
integrate cultural knowledge, and perform logical
analysis, comparison, or generalization. Scenario-
based, integrated analysis, or comparative reasoning
questions are recommended.
Question Generation(English)
Task: Answer in English. instruction
Note:
1. The question should avoid explicitly mentioning
cultural concepts, terminology, or characteristics, in
order to effectively assess the student’s understand-
ing of cultural traits.
2. A reference answer should be provided after the
question.
Context:
”’
Context
”’
Question:
Reference Answer:
Knowledge Injection(English)
Reference:
reference knowledge
Question:
question

```
