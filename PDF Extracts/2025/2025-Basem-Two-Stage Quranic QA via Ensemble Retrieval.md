---
title: "2025-Basem-Two-Stage Quranic QA via Ensemble Retrieval - PDF Extract"
source_pdf: "2025-Basem-Two-Stage Quranic QA via Ensemble Retrieval.pdf"
pages: 8
extracted_at: "2026-02-13T09:15:43.654631"
---

# PDF Extract: 2025-Basem-Two-Stage Quranic QA via Ensemble Retrieval

**Source PDF:** 2025-Basem-Two-Stage Quranic QA via Ensemble Retrieval.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Two-Stage Quranic QA via Ensemble Retrieval and
Instruction-Tuned Answer Extraction
Mohamed Basem1, Islam Oshallah1, Ali Hamdi1, Khaled Shaban2, Hozaifa Kassab3
1Dept. of Computer Science, MSA University, Giza, Egypt
{mohamed.basem1, islam.abdulhakeem, ahamdi}@msa.edu.eg
2Dept. of Computer Science, Qatar University, Doha, Qatar
khaled.shaban@qu.edu.qa
3AiTech AU, Australia
hozaifa@aitech.net.au
Abstract—Quranic Question Answering presents unique chal-
lenges due to the linguistic complexity of Classical Arabic and the
semantic richness of religious texts. In this paper, we propose a
novel two-stage framework that addresses both passage retrieval
and answer extraction. For passage retrieval, we ensemble fine-
tuned Arabic language models to achieve superior ranking
performance. For answer extraction, we employ instruction-tuned
large language models with few-shot prompting to overcome
the limitations of fine-tuning on small datasets. Our approach
achieves state-of-the-art results on the Quran QA 2023 Shared
Task, with a MAP@10 of 0.3128 and MRR@10 of 0.5763 for
retrieval, and a pAP@10 of 0.669 for extraction, substantially
outperforming previous methods. These results demonstrate that
combining model ensembling and instruction-tuned language
models effectively addresses the challenges of low-resource ques-
tion answering in specialized domains.
Index Terms—Quranic Question Answering, Passage Retrieval,
Span Extraction, Few-Shot Prompting, Instruction Tuning.
I. INTRODUCTION
The Holy Qur’an, revealed over 1,400 years ago, remains
the primary source of guidance for over 1.8 billion Muslims
worldwide. Beyond its religious significance, the Qur’an repre-
sents a masterpiece of Classical Arabic literature, containing
profound linguistic, historical, and ethical insights that con-
tinue to be studied by scholars across multiple disciplines [1].
However, accessing and understanding specific Quranic con-
tent in response to natural language queries presents significant
computational challenges that have only recently begun to be
addressed by the natural language processing community [2],
[3].
Question Answering (QA) systems have emerged as a
cornerstone technology for information access across diverse
domains, from general knowledge retrieval to specialized
applications in legal, medical, and educational contexts [4],
[5]. The development of effective QA systems for religious
texts, particularly the Qur’an, represents both a meaningful
application with substantial social impact and a challenging
technical problem that pushes the boundaries of current Arabic
NLP capabilities [2], [6].
Quranic Question Answering presents unique challenges
that distinguish it from conventional QA tasks. First, the
linguistic complexity of Classical Arabic—with its rich mor-
phology, complex syntax, and archaic vocabulary—poses sig-
nificant difficulties for models primarily trained on Mod-
ern Standard Arabic or contemporary dialects [7]. Second,
the semantic richness and multi-layered meanings inherent
in Quranic verses require sophisticated understanding that
goes beyond surface-level text matching. Third, the limited
availability of large-scale, high-quality annotated datasets for
Quranic content constrains the development and evaluation of
machine learning models [8]–[10]. Finally, the cultural and
religious sensitivity of the domain requires both precision and
humility. Quranic interpretation has traditionally been reserved
for scholars, and AI outputs risk being mistaken for authori-
tative tafs¯ır, potentially misleading users or fueling sectarian
disputes. To avoid this, systems should present answers as
informational aids rather than interpretive rulings [11].
Recent advances in transformer-based language models
have shown promising results for Arabic NLP tasks [12]–
[15]. However, these models face particular challenges when
applied to Classical Arabic texts, where the linguistic gap
between training data and target domain significantly impacts
performance [16]. While ensemble methods have proven ef-
fective in improving robustness across various NLP tasks [17],
their application to low-resource, high-complexity domains
like Quranic QA remains underexplored [18]. Similarly, the
emergence of instruction-tuned large language models offers
new possibilities for few-shot learning in specialized domains,
yet their effectiveness for Classical Arabic text understanding
has not been thoroughly investigated [19]–[21].
The Qur’an QA 2023 Shared Task was designed to address
these challenges through two complementary tasks: (1) Pas-
sage Retrieval, which requires identifying the most relevant
Quranic verses for a given natural language question, and (2)
Machine Reading Comprehension (MRC), which focuses on
extracting precise answer spans from retrieved passages [22].
Despite the participation of multiple research teams
[23]–
[26], the shared task results revealed significant room for im-
provement in both tasks, particularly in handling the linguistic
complexity and semantic nuances of Quranic texts.
This paper proposes a two-stage framework combining
arXiv:2508.06971v2  [cs.CL]  3 Sep 2025

--- Page 2 ---

dataset expansion with tailored modeling: ensemble methods
improve retrieval, while instruction-tuned LLMs with prompt-
ing enhance extraction.
Our main contributions are:
• Dataset Enhancement Strategy: We expand the original
dataset from 251 to over 2,000 questions through system-
atic paraphrasing and integration of diverse Quranic re-
sources, significantly improving model training coverage
and linguistic diversity.
• Ensemble-Based Retrieval Framework: We develop
and evaluate multiple ensemble strategies for combining
fine-tuned Arabic language models, achieving substantial
improvements in passage retrieval accuracy.
• Instruction-Tuned Extraction Approach: We demon-
strate that few-shot prompting with instruction-tuned
large language models significantly outperforms fine-
tuned approaches for answer extraction in low-resource
settings.
• State-of-the-Art Results: Our framework achieves new
benchmarks on the Quran QA 2023 Shared Task, with
MAP@10 of 0.3128 and MRR@10 of 0.5763 for passage
retrieval, and pAP@10 of 0.669 for answer extraction.
The remainder of this paper is organized as follows: Section
II reviews related work in Arabic QA and Quranic text
processing. Section III describes our methodology, includ-
ing dataset enhancement, model architectures, and ensemble
strategies. Section IV presents comprehensive experimental
results and analysis. Section V discusses implications and
limitations, and Section VI concludes with future research
directions.
II. RELATED WORK
This section surveys prior research relevant to our study
on Quranic Question Answering (QA), covering Arabic QA
systems, ensemble methods for retrieval, instruction-tuned
language models for answer extraction, and specific efforts
in Quranic QA. We highlight how these works inform our
approach to tackling the linguistic and semantic challenges of
Classical Arabic in the Qur’an.
A. Arabic QA Datasets
The field of Arabic Question Answering (QA) has ad-
vanced significantly, driven by the adoption of deep learning
techniques and transformer-based models [27]. Datasets like
Arabic-SQuAD, which rely on machine-translated questions,
suffer from quality issues that limit model performance in
specialized domains [27].
To address this, recent efforts have introduced more robust
and domain-specific resources. For example, the ArabicaQA
dataset [10] contains over 89,000 answerable and 3,700 unan-
swerable questions derived from Arabic Wikipedia. These
models are typically fine-tuned on domain-specific datasets
such as the Quranic Passage Collection (QPC), the Arabic
Reading Comprehension Dataset (ARCD), and newer large-
scale corpora aimed at improving generalization in non-
English QA.
B. Arabic QA Systems
Several Arabic QA systems have been evaluated on bench-
marks such as Arabic-SQuAD and ARCD. Mozannar et
al. [28] reported F1 scores of 48% on Arabic-SQuAD and 51%
on ARCD, highlighting the challenges in processing Arabic
text even with advanced neural architectures.
In addition, early efforts focused on religious texts. Durach-
man and Adriani [29] built a system to extract answers from
Indonesian Quran translations, achieving only 60% accuracy.
Similarly, Bhaskar et al. [30] proposed a rule-based multi-
task QA system combining biomedical tasks using ensemble
methods and NLTK-style pipelines, but lacked deep semantic
modeling in general-purpose or Quranic Arabic.
C. Ensemble Approaches
Ensemble methods improve QA systems, as shown in
MRQA 2019 [17] where combining BiDAF, QANet,and BERT
enhanced eneralization. However, Quranic QA presents unique
challenges since retrieving isolated verses (¯ay¯at) risks unin-
tended doctrinal weighting, as meaning emerges from inter-
connected passages within tafs¯ır traditions [31]. Our system
retrieves thematic passages rather than individual verses, pre-
serving coherence while maintaining ensemble benefits.
Similarly, ElKomy and Sarhan [18] applied ensemble meth-
ods in Arabic QA using AraELECTRA, AraBERT, and other
transformer models. Their approach achieved improved partial
Reciprocal Rank (pRR) scores, reaching up to 65% on the
Quranic Reading Comprehension Dataset (QRCD).
ElKomy and Sarhan [18] further advanced ensemble-based
Arabic QA by augmenting datasets through translation and
question reformulation. They fine-tuned models like AraBERT
and QARiB, reporting MAP@10 of 0.34 and MRR of 0.52,
with notable gains on QRCD.
III. METHODOLOGY
A. Tasks Definition
1) Passage Retrieval: The Passage Retrieval task aims to
identify up to 10 Qur’anic passages relevant to a question
in MSA. Some questions have no answer in the Qur’an,
in which case no passages should be returned. The dataset
is an extended version of AyaTECv1.2, containing 1,266
topical passages and 251 questions, including 37 zero-answer
questions.
2) Machine Reading Comprehension (MRC): The MRC
task involves extracting answers from a given Qur’anic pas-
sage in response to a question in MSA. Each passage may con-
tain single, multiple, or no answers. The dataset is an extended
version of QRCDv1.2, comprising 1,562 question–passage
pairs, including 62 with no answer.
B. Dataset Collection
1) Passage Retrieval Task Dataset: To improve coverage,
diversity, and relevance of the Passage Retrieval task training
set, we merged the official shared-task dataset with several
external sources to form an expanded composite dataset. The
combined dataset contains:

--- Page 3 ---

(a) Passage Retrieval Task
(b) Answer Extraction Task
Fig. 1. Overview of retrieve the most relevant Qur’anic passage and extract the exact answer span.
• Quran QA 2023 Shared Task Dataset: The official
benchmark dataset containing 251 Arabic questions
linked explicitly to relevant passages within the Qur’anic
Passage Collection (QPC). This dataset served as a Ini-
tial benchmarks and starting training examples for the
model [8].
• 1,000 Questions and Answers from the Qur’an: A pub-
licly available dataset compiled from Tafseer literature.
Its integration expanded our question-passage coverage,
enabling the models to cover more Quranic subjects,
linguistic differences and more in-depth analyses [32].
• List of Plants Mentioned in the Qur’an and Hadith:
A focused thematic dataset covering plant references in
Islamic texts. The resource has been utilized to enhance
the capacity of the model to address questions regard-
ing nature and Environmental issues addressed in the
Qur’an [33].
• Tafsir al-Jalalayn Pairs: A collection of Quranic verses,
in pairs. with their Tafsir of Al-Jalalayn. This helped the
model connect every verse with its interpretation, enhanc-
ing comprehension of significance and context [34].
• TyDi QA (Arabic Subset): A multilingual QA dataset
with questions and answers in Arabic. It enhanced the
performance of the model on general Arabic question
answering [35].
By integrating these diverse resources, we built a more and
more representative dataset. The addition enriched the ability
of the model to generalize between common and specialized
Quranic content, to aid better retrieval performance of [36],
[37].
2) Machine Reading Comprehension Task Dataset: For
MRC Task, we built a high-quality domain-specific dataset
by merging and refining several complementary resources.
Every resource was selected with care to maximise linguistic
diversity, thematic range, and structural coherence consistency,
maintaining high answer extraction performance.
• QRCDv1.2 Dataset: The official dataset released by
Quran QA 2023, with fully annotated question-passage
pairs. It was our primary training and evaluation re-
source type, including single-answer, multi-answer, and
unanswerable questions [38].
• QUQA Dataset: A varied set of questions pairs of
passages sourced directly from the Qur’an. Its inclusion
generated the dataset’s thematic and linguistic diversity,
enabling the models to deal with more semantic and
Interpretative differences [9].
• ARCD Dataset: A general-purpose MSA reading com-
prehension set. We adapted it to better handle Arabic
structure and improve Quranic communication. [39].
For the convenience of standardizing all the datasets, we
reformatted and standardized QUQA and ARCD to align with
the QRCDv1.2 schema. This alignment enabled concerted
training and evaluation workflows, regardless of the initial
dataset structure.
The complete integration and normalization of our dataset
ensured that both prompt-based and fine-tuned models had
access to rich, diverse, and well-structured examples. This
significantly enhanced their capacity to apply knowledge to
new and unseen Quranic QA scenarios.
C. Dataset Expansion
The initial Quran QA 2023 Shared Task dataset contained
only 251 Arabic questions, insufficient for training robust
language models. We implemented a multi-phase expansion
strategy to enhance both dataset size and linguistic diversity.
1) Phase 1: Expansion via External Sources: We began
by incorporating additional questions from external Quranic
resources to extend the coverage beyond the original shared
task dataset:
• 1000 Questions and Answers from the Qur’an: This
resource provided a rich collection of question-passage
pairs covering various Quranic themes. By selecting and
curating relevant entries, we expanded the dataset from
251 to 665 questions.
• Plants in the Qur’an Resource: In order to introduce
more specialized content, we included a set of questions
focusing on natural elements referenced in the Qur’an.
This facilitated enhance the topical range and prepared

--- Page 4 ---

Fig. 2. Overview of Task A pipeline for Passage Retrieval, illustrating dataset expansion, integration of external resources (e.g., Tafseer, TyDiQA), model
fine-tuning, relevance scoring via Cross-Encoder, and final ensemble-based ranking of Quranic passages.
the model for Addressing more specific inquiries from
users.
Phase 2 - Paraphrasing and Quality Review: Each of the
665 questions was manually paraphrased into two alternative
forms, creating three versions per question. All paraphrased
questions underwent human annotation review for relevance
and linguistic quality.
Final Dataset: The expansion process yielded 665 unique
questions with 2,000 total variations, providing a robust foun-
dation for retrieval model fine-tuning and few-shot prompt
construction. This diversified dataset significantly enhanced
system performance, particularly in the Passage Retrieval Task.
D. Model Architecture
1) Task A: Passage Retrieval Architecture: Task A employs
uses a multi-step architecture designed to maximize passage
retrieval for Quranic Question Answering. The method com-
bines dataset augmentation, model fine-tuning, and ensemble
techniques.
a) Data Expansion and Processing.: The original 251-
question dataset was expanded using external resources includ-
ing Tafseer literature and thematic collections. Each question
was paraphrased into two variants for linguistic diversity,
yielding over 2,000 unique formulations. The dataset was then
cleaned by removing duplicates and standardizing phrasing
(Figure 2).
b) Dataset Composition.: The ultimate dataset merged
original shared task questions with outside questions resources.
In each question, a verse from the Quran was included
, ensuring a comprehensive coverage of both general and
domain-specific topics.
c) Model Fine-Tuning.: Four pre-trained Arabic mod-
els were fine-tuned: AraBERTv02-ARCD, AraELECTRA,
CamelBERT-tydi-tafseer, and AraBERTv02-tydi-tafseer.
Training on the extended dataset improved MAP@10 and
MRR@10 performance. Hyperparameter optimization ex-
plored learning rates, batch sizes, and sequence lengths to
prevent overfitting and enhance generalizability.
d) Cross-Encoder Fine-Tuning and Relevance Scoring.:
After the initial model training, a Cross-Encoder was fine-
tuned on the same data. This model was utilized to estimate
pairwise relevance scores between every question and its
candidate passages. A thresholding procedure was utilized to
Remove irrelevant results based on these scores.
e) Ensemble Strategy.: An ensemble strategy was applied
to merge the predictions of several fine-tuned models. This
strategy played to the strengths of every single model. The
ensemble enhanced the robustness of the enhancements and
improved the overall passage ranking accuracy.
f) Retrieval Performance.:
This architecture achieved
competitive performance in the Quran QA 2023 Shared Task.
The ensemble model achieved a MAP@10 score of 0.3128
and an MRR@10 of 0.5763. The integration of dataset en-
largement,model diversity, and ensemble methods led to the
high effectiveness of the passage retrieval pipeline.
2) Task B: Machine Reading Comprehension Architecture:
For mrc Task, we employed a comprehensive two-phase archi-
tecture tailored to span extraction challenges in low-resource
contexts.
a) Phase 1: Fine-tuned Transformer Models: Initially,
we fine-tuned transformer-based Arabic models on QR-
CDv1.2, QUQA, and ARCD datasets. Models were trained to
identify the start and end positions of answer spans within
passages. However, their performance was constrained by
limited exposure to varied linguistic structures.
b) Phase 2: API-Based Prompting with LLMs: To over-
come these limitations, we introduced API-based instruction-
tuned large language models, namely:
• Gemini API
• DeepSeek API
We generated three-shot prompts from examples in QR-
CDv1.2, assisting the models in predicting correct spans. The
results obtained from these models were combined to make
predictions more robust and accuracy.
c) Final Span Extraction Output: The merger of fine-
tuned transformers and API models produced strong and
accurate extraction results. API-based models specifically

--- Page 5 ---

outperformed transformers, and their total produced better
consistency and enhanced overall accuracy.
Fig. 3. Overview of Answer Extraction task pipeline, covering data prepa-
ration, formatting for prompting or fine-tuning, model application (few-shot
and fine-tuned), ensemble of model outputs, and final answer extraction.
E. Few-Shot Strategy and Prompt Engineering
To optimize the performance of API-based language mod-
els like Gemini and DeepSeek, we employed a few-shot
prompting approach. This involves adding carefully selected
examples to the prompt, helping the model understand the task
[40].
Three instances from the QRCD v1.2 dataset were chosen
to illustrate varied answering contexts: multiple correct spans,
single correct span, and no solution. This ensures the model
can handle diverse questions, from answerable to unanswer-
able.
We also designed a structured prompt to guide the model
in generating accurate, text-aligned responses, minimizing
unnecessary elaboration or hallucination. The prompt format
includes clear instructions, examples, the input passage, and
the question.
A sample of our prompt template is provided below:
• Answer-Extraction Task from Qur’anic Texts
• Instructions:
– Extract all phrases from the text that answer the
question, whether the answer is explicit or implicit.
– The answer must be a literal quotation from the
passage.
– If no suitable answer is found, write: No answer
found in the given text.
– Do not add any explanation or commentary.
– Consult the tafs¯ır (interpretation) of each verse to
ensure accuracyto reach an accurate answer.
– Write the answers in the following format:
∗“First answer”
∗“Second answer”
– Examples: {few_shot_text}
– Answer the following passage:
– Passage: {passage}
– Question: {question}
– Answers:
The structured prompting method ensures precise, extractive
responses while minimizing off-topic or fabricated outputs.
It enhances model consistency when handling Quranic texts,
which require exact phrasing and high semantic fidelity.
F. Ensemble Method
To enhance the overall performance of both Passage Re-
trieval Task and MRC Task, we employed ensemble techniques
leveraging the strengths of multiple models.
Passage Retrieval Task In this task, we employed two var-
ious ensemble techniques depending on model performance:
We ensembled AraBERTv02-ARCD and AraELECTRA
predictions. The ensemble employed dynamic weighting by
giving more importance to the predictions with confidence
higher than 0.95. Predictions with more than 0.99 received
an additional boost to prioritize highly confident outputs. We
employed a weighted averaging strategy to merge rankings
from both the models, which enhanced precision by priori-
tizing most consistent predictions without compromising on
balanced ranking coverage.
We then employed Reciprocal Rank Fusion (RRF) to fuse
predictions of three models: AraELECTRA, CamelBERT-tydi-
tafseer, and AraBERTv02-tydi-tafseer. To maintain consis-
tency among the results, we normalized the scores of all the
models using min-max scaling. Lastly, the RRF approach was
augmented with an exponential decay factor along with a
confidence-based boosting mechanism specifically for scores
above 0.8. Model-specific weights, determined based on prior
performance evaluations, were applied, with AraELECTRA
receiving the highest weight due to its superior individual
performance. The final ranked list was generated by combining
the RRF scores with the weighted normalized scores using a
geometric mean, further improving retrieval accuracy across
diverse question formulations.
Machine Reading Comprehension Task
In this task, we employed an ensemble multi-level strat-
egy. We combined fine-tuned language models, specifically
AraBERTv02 + CAMeLBERT and AraBERTv02 + BERT-
large, for better extraction consistency among different model
variants. This improved ensemble reached moderate improve-
ments, its performance leveled off at pAP@10 scores of 0.517
and 0.509, respectively.

--- Page 6 ---

TABLE I
PERFORMANCE COMPARISON FOR PASSAGE RETRIEVAL TASK BEFORE AND AFTER DATASET EXTENSION, SORTED IN ASCENDING ORDER BY
MAP@10 AFTER EXTENSION.
Model
Before Extension
After Extension
MAP@10
MRR@10
MAP@10
MRR@10
AraBERTv02-ARCD
0.2047
0.4445
0.2176
0.4709
AraELECTRA
0.2072
0.4473
0.2408
0.4934
AraBERTv02-tydi-tafseer
0.2494
0.5519
0.2673
0.5655
CamelBERT-tydi-tafseer
0.2508
0.5126
0.2926
0.4921
CamelBERT + AraBERTv02-ARCD + AraBERTv02-tydi
N/A
N/A
0.3009
0.5860
CamelBERT + AraBERTv02-ARCD
N/A
N/A
0.3017
0.5346
CamelBERT + AraBERTv02-tydi
N/A
N/A
0.3128
0.5763
For better performance, we further ensembled the top-
performing API-based few-shot LLMs, namely Gemini (API-
enhanced prompt) and DeepSeek (API-enhanced prompt). We
merged their answer spans, keeping all unique responses while
eliminating duplicates. This ensemble achieved the best overall
performance with a pAP@10 of 0.669, outperforming all
individual models and fine-tuned ensembles.
This layered ensemble approach—combining both fine-
tuned models and instruction-tuned LLMs—demonstrated su-
perior robustness and coverage, effectively handling both
straightforward and ambiguous extraction scenarios.
IV. EXPERIMENTS AND RESULTS
A. Evaluation Metrics
For both Passage Retrieval task and MRC task, the Quran
QA 2023 shared task uses standard evaluation metrics com-
monly employed in Information Retrieval (IR) and Question
Answering (QA) tasks.
Passage Retrieval
The evaluation for this task is based on two primary
metrics, Mean Average Precision at 10 (MAP@10) and Mean
Reciprocal Rank at 10 (MRR@10):
• Mean Average Precision at 10 (MAP@10): MAP@10
evaluates the average precision of relevant passages
within the top 10 retrieved passages. It is calculated as
follows:
MAP@10 =
1
|Q|
X
q∈Q
1
min(Rq, 10)
10
X
k=1
P(k) δk
where Q denotes the collection of inquiries,and Rq is the
total relevant passages for query q, P(k) is precision at
rank k, and δk = 1 if the passage at rank k is relevant
and 0 otherwise.
• Mean Reciprocal Rank at 10 (MRR@10): MRR@10
evaluates the rank position of the first relevant excerpt. It
is defined as:
MRR@10 =
1
|Q|
X
q∈Q
1
rankq
where rankq is the rank of the first relevant passage
retrieved within the top 10 positions for query q. If no
relevant passage is retrieved, the reciprocal rank is 0.
Machine Reading Comprehension (MRC)
For this task, the evaluation metric is partial Average
Precision at 10 (pAP@10):
• partial Average Precision at 10 (pAP@10): This metric
calculates the precision of exact answer spans extracted
from the top-ranked passages. pAP@10 considers partial
correctness of the extracted spans and is calculated sim-
ilarly to MAP, but with partial relevance scores:
pAP@10(q) =
1
min(Rq, 10)
10
X
k=1
P(k) δpartial
k
Here, δpartial
k
represents the partial correctness of the
answer span at rank kis partially correct, with values from
0 to 1 depending on the overlap with the correct span.
All the measurements are obtained using the official evaluation
script provided by the Quran QA 2023 shared task organizers.
B. Experiment Comparison
Table I compares Passage Retrieval task results before and
after dataset expansion, showing consistent improvements.
CamelBERT-tydi-tafseer
achieved
the
best
individual
post-expansion
performance
with
MAP@10
of
0.2926
and MRR@10 of 0.4921. An ensemble of CamelBERT,
AraBERTv02, and AraBERTv02-tydi further improved results
to MAP@10 of 0.3116 and MRR@10 of 0.5736.
Table II details MRC task performances of fine-tuned and
few-shot LLM models. Few-shot LLMs with API-augmented
prompting outperformed traditional fine-tuned models.
The best individual model was Gemini (API-enhanced
prompt) led with a pAP@10 of 0.637, followed by DeepSeek
at 0.624. Simple API usage without enhanced prompting
scored lower (approximately 0.592–0.593), highlighting the
importance of prompt optimization.
Fine-tuned
models
lagged
behind,
with
AraBERTv02
(Merged DS - Tydi) top among them at 0.503. Model ensem-
bles such as AraBERTv02 + CAMeLBERT and AraBERTv02
+ BERT-large scored 0.517 and 0.509 respectively.
The highest overall performance was realized through en-
seming Gemini (API-enhanced prompt) and DeepSeek (API-
enhanced prompt), with 0.669 pAP@10, a considerable im-
provement over the best single model. This confirms that
Combining complementary LLM predictions leads to superior
results in extractive QA.

--- Page 7 ---

TABLE II
PERFORMANCE OF OUR TOP MODELS.
Model
Type
pAP@10
Gemini + DeepSeek (Ensemble)
Few-shot LLM
0.669
Gemini (API-enhanced prompt)
Few-shot LLM
0.637
DeepSeek (API-enhanced prompt)
Few-shot LLM
0.624
DeepSeek (API)
Few-shot LLM
0.593
Gemini (API)
Few-shot LLM
0.592
AraBERTv02 + CAMeLBERT (Ensemble)
Fine-tuned
0.517
AraBERTv02 + BERT-large (Ensemble)
Fine-tuned
0.509
AraBERTv02 (Merged DS - Tydi)
Fine-tuned
0.503
BERT-large (Merged DS - Tydi)
Fine-tuned
0.478
CAMeLBERT (Merged DS - Tydi)
Fine-tuned
0.442
BERT-large (QRCDv1.2 - Tydi)
Fine-tuned
0.438
AraELECTRA (Merged DS - Tydi)
Fine-tuned
0.425
C. Results
Table
III and Table
IV are representative of the official
leaderboard The results of the Quran QA 2023 Shared Task
for Passage Retrieval task and MRC task, respectively. Our
submissions got the highest scores on both tasks. outdoing
every other rival team and the established standards.
In passage retrieval task, our collaborative submission,
CamelBERT + AraBERTv02-tydi scored a MAP@10 of
0.3128 and MRR@10 of 0.5763, beating the next best com-
petitor (TCE’s run M00 with 0.2506 MAP@10 and 0.4610
MRR@10) by a significant margin. Similarly,in mrc task, our
ensemble of Gemini and DeepSeek, using API-augmented
prompting, attained a pAP@10. of 0.669, outscoring the
leading leaderboard submission by TCE (0.5711 pAP@10).
The results explain the success of our method, Complement-
ing dataset augmentation, fine-tuning methods, and ensemble
methods techniques to maximize performance in both passages
retrieval and extractive span detection
TABLE III
OFFICIAL TASK A LEADERBOARD (MAP@10 AND MRR@10).
Team
Run
MAP@10
MRR@10
Ours
Ensemble
0.3128
0.5763
TCE
M00
0.2506
0.4610
TCE
A00
0.2464
0.4940
TCE
C00
0.2302
0.4706
AHJL
SG2
0.1995
0.3889
AHJL
SWOP3
0.1318
0.3021
LKAU23
run63
0.1242
0.3750
AHJL
SS1
0.1202
0.2907
LKAU23
run61
0.1166
0.3632
Baseline
BM25
0.0904
0.2260
D. Discussion
This paper discussed the principal issues in Quranic Ques-
tion Able to answer passage and span extraction questions.
Increasing the dataset from 251 to over 665 distinct questions,
alongside paraphrasing, were essential to improving model
generality and retrieval accuracy. Although fine-tuning the
models for mrc task had limited success because due to
TABLE IV
OFFICIAL TASK B LEADERBOARD (PAP@10).
Team
Run
pAP@10
Ours
Gemini + DeepSeek (Ensemble)
0.669
TCE
4dfb8d601
0.5711
TCE
dac0bdf4b
0.5643
Al-Jawaab
tpgp4
0.5457
Al-Jawaab
tgp4
0.5393
TCE
ccc877dca
0.5311
LKAU23
run03
0.5008
LKAU23
run02
0.4989
LowResContextQA
run01
0.4745
LowResContextQA
run02
0.4745
LowResContextQA
run03
0.4745
GYM
run0
0.4613
GYM
ensemble
0.4588
LKAU23
run01
0.4541
GYM
test1
0.4304
Baseline
WholePassage
0.3268
data paucity, shifting to instruction-tuned API models like
Gemini and DeepSeek. These performed better by few-shot
prompt without further training. Ensembling these models
continued to improve stability and performance throughout
both responsibilities. Nevertheless, the use of APIs presents
reproducibility and transparency concerns. Future work should
focus on open, reproducible systems using graph-based link-
ing and retrieval-augmented generation for deeper semantic
reasoning across Quranic verses.
V. CONCLUSION
In this paper, we have suggested a robust response system
to the Quranic question that achieves state-of-the-art results
for passage retrieval task and mrc task in the Quran QA
2023 Shared Task. In order to overcome the limited coverage
and capacity of the initial In first task, we increased the
size of our training set considerably. by leveraging several
outside resources, manual question generation and extensive
rephrasing, leading to a diversified dataset of over 2,000
questionnaires. Using on this enhanced dataset, we fine-
tuned state-of-the-art Arabic language models—AraBERT,
CamelBERT, and ELECTRA—and used an ensemble ap-
proach, resulting in better MAP@10 and MRR@10 rank-
ings against the official winning outcomes. For second task,
recognizing the challenge of fine-tuning small datasets, we
successfully leveraged instruction-tuned Large Language
Models (LLMs), namely Gemini and DeepSeek operates in
a few-shot prompting setting. By carefully generating good
prompts and corroborating findings by means of With an
ensemble method, our system achieved a pAP@10 score of
0.669, surpassing the top reported scores from the common
task. Our research demonstrates that leveraging dataset ex-
pansion, model ensembling, and few-shot prompting with
LLMs effectively advances the state-of-the-art of Arabic QA
systems. This research not only sets a new benchmark for The
Quranic QA also offers an explicit methodological framework.
Future work will enhance access to Islamic understanding
by employing Graph Neural Networks (GNNs) to model

--- Page 8 ---

deeper semantic links between passages, improving retrieval
accuracy and context-aware answer extraction.
ACKNOWLEDGMENT
This publication was supported by Qatar University High
Impact Grant, Number LAW: 775. The findings achieved
herein are solely the responsibility of the authors.
REFERENCES
[1] Mattson, Ingrid. The story of the Qur’an: its history and place in Muslim
life. John Wiley & Sons, 2012.
[2] Utomo, FS, N. Suryana, and MS Azmi. “Question answering systems on
holy quran: a review of existing frameworks, approaches, algorithms and
research issues.” In Journal of Physics: Conference Series, vol. 1501,
no. 1, pp. 012022, IOP Publishing, 2020.
[3] Gilbert Badaro, Ramy Baly, Hazem Hajj, Wassim El-Hajj, Khaled
Bashir Shaban, Nizar Habash, Ahmad Al-Sallab, and Ali Hamdi. 2019.
A Survey of Opinion Mining in Arabic: A Comprehensive System
Perspective Covering Challenges and Advances in Tools, Resources,
Models, Applications, and Visualizations. ACM Trans. Asian Low-
Resour. Lang. Inf. Process. 18, 3, Article 27 (September 2019), 52 pages.
[4] Martinez-Gil, Jorge. “A survey on legal question–answering systems.”
Computer Science Review, vol. 48, pp. 100552, 2023.
[5] Wang, Dandan and Shiqing Zhang. “Large language models in medical
and healthcare fields: applications, advances, and challenges.” Artificial
Intelligence Review, vol. 57, no. 11, pp. 299, 2024.
[6] Hamdi, Ali, Khaled Shaban, and Anazida Zainal. “A Review on Chal-
lenging Issues in Arabic Sentiment Analysis.” Journal of Computer
Science, vol. 12, no. 9, Dec. 2016, pp. 471-481.
[7] Altammami, Shatha and Eric Atwell. “Challenging the transformer-
based models with a classical arabic dataset: Quran and hadith.In
Proceedings of the Thirteenth Language Resources and Evaluation
Conference, pp. 1462–1471,2022.
[8] Malhas, Rana and Tamer Elsayed. “AyaTEC: Building a Reusable Verse-
Based Test Collection for Arabic Question Answering on the Holy
Qur’an.” ACM Transactions on Asian and Low-Resource Language
Information Processing, vol. 19, no. 6, pp. 1–21, November 2020.
[9] Al-Khalifa, Hend S. and Nouf Alnazzawi. “QUQA: Question Answering
Dataset for the Holy Qur’an.” 2023.
[10] Abdallah, Abdelrahman, Mahmoud SalahEldin Kasem, Mahmoud Ab-
dalla, Mohamed Mahmoud, Mohamed Elkasaby, Yasser Elbendary,
and Adam Jatowt. “ArabicaQA: A Comprehensive Dataset for Arabic
Question Answering.”
[11] Seyyed Hossein Nasr, Caner K. Dagli, Maria Massi Dakake, Joseph E.
B. Lumbard, and Mohammed Rustom, editors. The Study Quran: A New
Translation and Commentary. HarperOne, New York, 2015.
[12] Mohamed, M., Emad, R., & Hamdi, A. (2025). A Multi-Layered Large
Language Model Framework for Disease Prediction.
[13] A. Allam, S. Ahmed, A. Hamdi and A. Mohammed, ”Arabic Large
Language Models for Medical Text Generation,” 2025 4th Interna-
tional Conference on Computer Technologies (ICCTech), Kuala Lumpur,
Malaysia, 2025, pp. 1-6.
[14] Antoun, Wissam, Fady Baly, and Hazem Hajj. “AraBERT: Transformer-
based Model for Arabic Language Understanding.” In LREC 2020
Workshop Language Resources and Evaluation Conference 11–16 May
2020, pp. 9, 2020.
[15] Antoun, Wissam, Fady Baly, and Hazem Hajj. “AraELECTRA: Pre-
Training Text Discriminators for Arabic Language Understanding.” In
Proceedings of the Sixth Arabic Natural Language Processing Workshop,
pp. 191–195, Association for Computational Linguistics, 2021.
[16] Inoue, Go, Bashar Alhafni, Nurpeiis Baimukan, Houda Bouamor, and
Nizar Habash. “The Interplay of Variant, Size, and Task Type in Arabic
Pre-trained Language Models.” In Proceedings of the Sixth Arabic
Natural Language Processing Workshop, Association for Computational
Linguistics, April 2021.
[17] Khot, Tushar, Alon Talmor, Robin Jia, Peter Clark, Sewon Min, Eunsol
Choi, and Hannaneh Hajishirzi. “MRQA 2019 Shared Task: Evaluating
Generalization in Reading Comprehension.” In Proceedings of the 2nd
Workshop on Machine Reading for Question Answering (MRQA), pp.
1–13, 2019.
[18] ElKomy, Ahmed and Hadeer Sarhan. “TCE at Qur’an QA 2022:
Arabic Language Question Answering Over Holy Qur’an Using a Post-
Processed Ensemble of BERT-based Models.”
[19] Zhu, Yutao, Huaying Yuan, Shuting Wang, Jiongnan Liu, Wenhan Liu,
Chenlong Deng, Haonan Chen, Zheng Liu, Zhicheng Dou, and Ji-Rong
Wen. “Large language models for information retrieval: A survey.
[20] Ramachandran, Anand. “Unveiling Google’s Gemini 2.0: A Compre-
hensive Study of its Multimodal AI Design, Advanced Architecture,
and Real-World Applications.” ResearchGate, 2024.
[21] DeepSeek-AI, Aixin Liu, Bei Feng, and others. “DeepSeek-V3 Technical
Report.” arXiv preprint arXiv:2412.19437, 2025.
[22] Malhas, Mohammad, Hamdy Mubarak, and Kareem Darwish. “Qur’an
QA 2023: Overview of the First Workshop on Question Answering on
the Quran.” Proceedings of the 1st Workshop on Question Answering on
the Quran, pp. 1–13, October 2023.
[23] Elkomy, Abdelrahman, Mahmoud Elsayed, and Mohamed Hefny. “Tce
team: Transformer-based ensemble for extractive qur’anic qa.” In Pro-
ceedings of the 1st Workshop on Question Answering on the Quran, pp.
110–117, 2023.
[24] Alawwad, Hessa, Lujain Alawwad, Jamilah Alharbi, and Abdullah
Alharbi. “Ahjl at qur’an qa 2023 shared task: Enhancing passage
retrieval using sentence transformer and translation.” In Proceedings of
ArabicNLP 2023, pp. 702–707, 2023.
[25] Alnefaie, Raghad, Nouf Alghamdi, Atheer Bajawi, Abeer Aljohani,
Areej Barnawi, Fatimah Daghistani, and Abdullah Awajan. “Lkau23
team: Transformer-based ensemble for qur’anic qa.” In Proceedings of
the 1st Workshop on Question Answering on the Quran, pp. 141–147,
2023.
[26] Zekiye, Muhammed, Mohamed Bakouri, Mariam Oudah, and Alaa
Mourad. “Al-jawaab team: Generative constraint modeling with dense
passage retrieval for quranic question answering.” In Proceedings of the
1st Workshop on Question Answering on the Quran, pp. 126–133, 2023.
[27] Alkhurayyif, Yazeed and Abdul Rahaman Wahab Sait. “Developing
an Open Domain Arabic Question Answering System Using a Deep
Learning Technique.” IEEE Access, vol. 11, pp. 79659–79671, 2023.
[28] Mozannar, Hussein, Muhammad Abdul-Mageed, and Nizar Habash.
“Neural Arabic Question Answering.
[29] Durachman, A. and A. Adriani. “IndoQA: A Question Answering
System for Indonesian Factoid Questions.” In Proceedings of the 2019
International Conference on Asian Language Processing (IALP), pp.
329–334, IEEE, 2019.
[30] Bhaskar, Prashant, Hammad Sheikh, and Nasimul Majumder. “SIEG at
MEDIQA 2019: Multi-task Neural Ensemble for Biomedical Question
Answering.” In Proceedings of the 18th BioNLP Workshop and Shared
Task, pp. 398–403, 2019.
[31] Abdullah Saeed.
Interpreting the Qur’an: Towards a Contemporary
Approach. Routledge, London and New York, 2005.
[32] Ashor, Q. “1000 QAs from the Holy Qur’an.” Noor Book, 2023.
[33] Qur’anic Botanic Garden (QBG). “List of Plants Citation in Qur’an and
Hadith v5.” Qur’anic Botanic Garden Publication, 2021.
[34] Al-Mahalli, Jalal al-Din and Jalal al-Din al-Suyuti. “Tafsir al-Jalalayn.”
Interactive Tafsir Platform, 2021.
[35] Clark, Jonathan H., Eunsol Choi, Michael Collins, Dan Garrette, Tom
Kwiatkowski, Vitaly Nikolaev, and Jennimaria Palomaki. “Tydi qa: A
benchmark for information-seeking question answering in typologically
diverse languages.” Transactions of the Association for Computational
Linguistics, vol. 8, pp. 454–470, 2020.
[36] M. Basem, I. Oshallah, B. Hikal, A. Hamdi, and A. Mohamed, “Op-
timized Quran Passage Retrieval Using an Expanded QA Dataset and
Fine-Tuned Language Models,” in Proc. Int. Conf. Advanced Computing
and Informatics, pp. 244–254, Springer, 2024.
[37] Oshallah, I., Basem, M., Hamdi, A. and Mohammed, A., 2025. Cross-
Language Approach for Quranic QA. arXiv preprint arXiv:2501.17449.
[38] Malhas, Rana and Tamer Elsayed. “Arabic Machine Reading Compre-
hension on the Holy Qur’an using CL-AraBERT.” Information Process-
ing & Management, vol. 59, no. 6, pp. 103068, 2022.
[39] TheDevastator. “ARCD Dataset: Unlocking Arabic Language Compre-
hension with the Arabic Reading Comprehension Dataset.” 2021.
[40] Basem, Mohamed, Islam Oshallah, Ali Hamdi, and Ammar Mohammed.
“Few-Shot Prompting for Extractive Quranic QA with Instruction-Tuned
LLMs.” arXiv preprint arXiv:2508.06103, 2025.

```
