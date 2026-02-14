---
title: "2025-Gómez-RigoChat 2 An Adapted Language Model to Spanish Using a Bounded - PDF Extract"
source_pdf: "2025-Gómez-RigoChat 2 An Adapted Language Model to Spanish Using a Bounded.pdf"
pages: 21
extracted_at: "2026-02-13T17:43:20.835793"
---

# PDF Extract: 2025-Gómez-RigoChat 2 An Adapted Language Model to Spanish Using a Bounded

**Source PDF:** 2025-Gómez-RigoChat 2 An Adapted Language Model to Spanish Using a Bounded.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

RIGOCHAT 2: AN ADAPTED LANGUAGE MODEL TO SPANISH
USING A BOUNDED DATASET AND REDUCED HARDWARE
Gonzalo Santamaría Gómez
Guillem García Subies
Pablo Gutiérrez Ruiz
Mario González Valero
Natàlia Fuertes
Helena Montoro Zamorano
Carmen Muñoz Sanz
Leire Rosado Plaza
Nuria Aldama García
David Betancur Sánchez
Kateryna Sushkova
Marta Guerrero Nieto
Álvaro Barbero Jiménez
Instituto de Ingeniería del Conocimiento
{name.firstsurname}@iic.uam.es
Madrid, Spain
ABSTRACT
Large Language Models (LLMs) have become a key element of modern artificial intelligence,
demonstrating the ability to address a wide range of language processing tasks at unprecedented
levels of accuracy without the need of collecting problem-specific data. However, these versatile
models face a significant challenge: both their training and inference processes require substantial
computational resources, time, and memory. Consequently, optimizing this kind of models to
minimize these requirements is crucial. In this article, we demonstrate that, with minimal resources
and in a remarkably short time, it is possible to enhance a state-of-the-art model, specifically for a
given language task, without compromising its overall capabilities using a relatively small pretrained
LLM as a basis. Specifically, we present our use case, RigoChat 2, illustrating how LLMs can be
adapted to achieve superior results in Spanish-language tasks.
1
Introduction and Previous Work
Training Large Language Models (LLMs) [1,2] has become a cornerstone of Natural Language Processing (NLP),
enabling sophisticated applications across various domains. These models are trained on vast corpora, often containing
billions or even trillions of tokens, which allows them to capture complex linguistic patterns and generalize well across
a wide range of tasks. However, their training process is computationally intensive and requires extensive hardware
resources and time. This challenge is exacerbated by the need for powerful large data centers that support their training
process, which is resource-demanding and time-consuming, making the creation of state-of-the-art models available to
only a few organizations.
Efforts to optimize both LLMs training and inference have led to several promising approaches. One notable method
involves the use of smaller, pre-trained language models (SLMs) as a foundation for fine-tuning on specific tasks [3].
This approach leverages the strengths of existing models while reducing the need for extensive training data and
computational resources. A second approach includes the use of datasets as small as possible, maximizing statistical
significance in those use cases to which the model will be exposed [4,5].
Recent advancements have also seen the emergence of techniques aimed at reducing the computational requirements
of LLMs during training. For example, LoRA [6] enables fine-tuning of LLMs using additive updates in the form of
low-rank matrices, which significantly reduce the number of parameters that need to be updated, leading to a reduced
memory usage. QLoRA [7] builds upon LoRA by further compressing the model through quantization of the original
weights and keeping the low-rank matrices at full precision.
Some libraries and research efforts such as llama.cpp [8] include several methods to quantize and serve LLMs in a
bounded hardware for inference. There are also more efficient computational algorithms to implement the self-attention
operation, making use of specialized hardware features, such as FlashAttention [9–11], which can save computation
efforts in both the training phase and inference time.
arXiv:2503.08188v1  [cs.CL]  11 Mar 2025

--- Page 2 ---

In summary, even though the training and inference of LLMs remains resource-intensive, various strategies have been
developed to optimize these processes. These include the use of smaller datasets, model distillation such as Llama-
3.1 [2], parameter-efficient methods like LoRA or QLoRA, or smaller models as a basis. Each of these approaches
addresses different aspects of the computational burden, offering a range of solutions to make LLMs more accessible
and efficient for a broader range of applications.
This work builds upon existing methodologies to demonstrate that, even with limited resources, state-of-the-art models
can be aligned to specific use cases while maintaining general performance. The approach utilizes a 7-billion-parameter
pre-trained LLM as a foundation. To illustrate this concept, the case of RigoChat 2 is presented, an Spanish-aligned
model showcasing how existing LLMs can be adapted to improve their performance in Spanish-language tasks.
Before delving into subsequent sections, it is essential to emphasize that this work involved significant efforts in
data collection and quality assessment. Extensive research has been conducted on data collection methodologies, as
highlighted in studies such as [12], where they also focused on obtaining data resources in Spanish. Our training process
relied on the direct preference optimization algorithm (DPO) [13], which requires a dataset that reflects human judgment.
However, this approach becomes prohibitively expensive when managing large volumes of data. Consequently, the
development of automated methods to simulate human evaluation—particularly those leveraging models—emerges as a
highly valuable alternative. Several studies [14–21] have addressed this challenge. Building on these contributions,
we propose a methodology to generate automated evaluations based on LLMs, aiming to align them with assessments
conducted by human experts (computational linguists).
Bearing this in mind, the contributions of this paper are the following:
• We propose a methodology for collecting and quality-filtering open conversational corpora.
• A new technique to augment conversation threads in conversational datasets using LLMs is introduced.
• A review and experimental analysis of automatic evaluation methods for LLM responses in the Spanish
language is carried out.
• As a result of the previous steps, a high-quality conversational dataset for preferences learning in the
Spanish language is produced.
• By making use of this dataset we create the RigoChat 2 model, an alignment of an open-weights state-of-
the-art LLM to the Spanish language, producing better performance in this language.
2
Training Data: Preparation and Methodology
The core contribution of our work is a methodology for collecting and processing high-quality data to align a Large
Language Model (LLM) to the Spanish language. This process involves a series of steps that progressively refine and
augment a large corpus of Spanish conversations to produce a high-quality dataset suitable for preference learning
(DPO). The steps are as follows:
1. Collecting data: Aggregating a large-scale corpus of Spanish conversations from various public and proprietary
sources.
2. Filtering high-quality Conversations (HQ): Applying quality criteria to filter out low-quality and inappropri-
ate conversations, resulting in a High Quality dataset.
3. Augmenting conversations (HQ+): Using a batch of LLM to generate alternative responses for each
conversation thread, expanding the dataset and improving its quality.
4. Evaluating responses: Developing and employing automatic evaluation methods to assess the quality of the
generated responses from private and open-source corpora designed by computational linguists.
5. Generating preferences (PD): making use of the automated evaluations, we produce a Preferences Dataset
aimed to produce an alignment toward responses either annotated by humans or generated by high-performing
models.
In a nutshell, given that reinforcement learning over preference data has been shown to be an effective method to
improve performance and align LLMs, in particular using the DPO algorithm [13], our focus was to transform data
resources to this kind of data format. This process was specifically applied to Spanish, although the underlying concepts
can be generalized to other languages and use cases.
2

--- Page 3 ---

2.1
Data Resources
The initial dataset is compiled from a combination of public and proprietary sources. After collecting a large amount
of data, several filtering and quality classification steps were applied. First, a language filter was implemented: if
the texts had been pre-classified by language, this classification was used; otherwise, the langdetect library [22] was
employed with a confidence threshold of 75%. Next, data quality was assessed following the criteria described in 2.2.
Additionally, corpora were classified based on the variety and nature of responses, as detailed in 2.3. Finally, specific
considerations regarding the IIC private corpora were addressed, including a comparison with other resources.
Table 1 summarizes the analyzed sources and the number of samples retained after applying all the quality filters.
Name
Samples
Filtered samples
Quality
Type
Evol Instruct Spanish [23]
59022
0
M
4
Instruct-Aira Dataset [24]
40946
0
M
4
ShareGPT [25]
1643
0
M
4
LMSYS-Chat-1M [26]
23758
0
M
4
Chatbot Arena Conversations Dataset [27]
519
0
M
4
OpenAssistant [28]
15438
5917
H
1
OpenHermes 2.5 Spanish [29]
1000000
0
M
4
M2Lingual [30]
2550
0
M
4
Multilingual BioASQ-6B [31]
2744
0
M
2
AsistenciaRefugiados [32]
21431
0
M
2
Wikihow in Spanish [33]
113160
0
M
4
LingComp_QA [34]
1004
1004
H
1
somos-clean-alpaca-es [35]
44932
0
M
2
Databricks Dolly [36]
15015
4598
H
2
MentorES [37]
10175
10175
H
2
Aya Dataset [38]
3854
3854
H
2
RAG Multilingual [39]
15018
15018
H
4
IIC Private Corpora
88822
2102
H
2
Total
1460031
26646
-
-
Table 1: All the collected Spanish dataset resources, their corresponding number of samples, the filtered high-quality
samples and their quality rating.
Figure 1 illustrates the task distribution of all the collated the datasets as reported in their original sources.
3

--- Page 4 ---

Figure 1: Task distribution estimation of the compilation of data resources.
2.2
Corpus-level quality filter (HQ)
To identify high-quality conversations, a corpus-level filtering process was conducted. Three computational linguists
reviewed the datasets, assigning a quality rating based on the following criteria:
Low quality data
• Grammatical and Linguistic Issues: Texts with numerous grammatical errors, poorly executed translations,
excessive use of anglicisms or fragmented sentences.
• Inappropriate Language: Texts containing insults, profanity, or other inappropriate language.
• Encoding Errors: Systematic issues such as incorrect characters or missing spaces.
• Incomplete Information: Instances where questions or answers are missing, responses include placeholders
like None, or there is repetitive looping in responses.
Medium quality data
• Texts written in Spanish with only minor errors that do not significantly hinder comprehension. However, the
accuracy of the content cannot be determined due to its technical or specific nature.
High-quality data
• Texts of exceptional quality, characterized by proper use of Spanish, relevant and engaging content, and
reliable answers. This category includes texts with high conversational or contextual relevance, validated both
by external reviewers and by assurances of correctness for highly technical responses provided by the creators
of the datasets.
In some cases, such as OpenAssistant [28], human validations were already included. For these datasets, filtering was
applied to retain only conversations with responses scoring above 70%. Similarly, for the translated Dolly dataset [36],
only the task types closed-qa and information-extraction were selected. After scoring each dataset, only those with a
high quality rating were retained, filtering out datasets of medium or low quality. This resulted in a significantly reduced
corpus, as shown in Table 1.
4

--- Page 5 ---

2.3
Data resources classification
Collected sources, along with the augmented data generated using the methodology outlined in the previous section, can
be categorized based on whether they have been generated or evaluated by humans. This classification distinguishes
four cases concerning the nature of the responses and their quality, as presented in Table 2.
Data type
Expert annotation?
Variants validated?
Type 1
Yes
Yes
Type 2
Yes
No
Type 3
No
Yes
Type 4
No
No
Table 2: Quality criteria classification for each thread in the dataset.
The highest quality score (Type 1) corresponds to datasets manually created by human experts, with alternative responses
either created or validated also by human experts. Second in quality (Type 2) drops the requirement of alternative
responses to be manually checked, thus allowing for automated generation. Next (Type 3) are those datasets were all
responses were created automatically, including the main response, but all of them were checked by a human. The
lowest quality standard (Type 4) corresponds to fully automated and unrevised datasets.
According to this rating most of the collected datasets fall under Type 4. Only conversations of Types 1 and 3 are
useful to apply DPO, as they provide a meaningful learning signal for the LLM. The Type 2 conversations will be
automatically converted into Type 1 by augmenting the data, as described in the following sections, by assuming that
the annotated answer is always more desirable than the generated alternatives.
2.4
Data Augmentation (HQ+)
The high-quality dataset (HQ) was further augmented by generating alternative responses for each conversation thread
using LLMs. Each conversation is segmented into multiple threads, corresponding to the number of turns it contains.
For instance, a conversation with n turns between a user and an assistant, represented as cn = {u1, a1, . . . , un, an},
can be decomposed into n separate threads:
• t1: {u1, a1}
• t2: {u1, a1, u2, a2}
• · · ·
• tn: {u1, a1, . . . , un, an}
Each thread ti can be further divided into input-output components:
• Input: the chat history up to the user’s latest query, {u1, a1, . . . , ui}.
• Output: the assistant’s most recent response, ai.
For each thread ti, we generated alternative responses using multiple LLMs. Each LLM j was provided with the thread
input, thereby generating an alternative response aj
i. The resulting augmented thread is represented as:
ti = {u1, a1, . . . , ui, {ai, a1
i , a2
i , . . . , am
i }}
where m is the number of deployed models, ai is the original response, and aj
i corresponds to the response generated
by model j. The models used to generate new responses were the following: RigoChat-7b-v1 (private model), Qwen2-
7B-Instruct [40], Llama-3.1-8B-Instruct [2], gpt-3.5-turbo-0125 and gpt-4o-mini [41], stablelm-2-12b-chat [42] and
gemma-2-9b-it [43].
2.5
Automating response scoring
In order to create preference scores for the generated data without the need of human intervention we conducted an
analysis of different automated metrics, with the objective to find a low-cost method that provided scores as close as
possible to human judgment. Various types of automated evaluators were tested, including approaches based on metrics
previously discussed in the state of the art and LLM-based methods as defined in the preceding section:
5

--- Page 6 ---

• Open-source LLMs: Llama 3.1 [2].
• Commercial LLMs: GPT-4o [44].
• Specialized evaluation models: Prometheus [14].
• Metrics based on semantic similarity: SAS [20].
• Ensembles combining several of these strategies. Specifically, an attempt was made to average several of these
strategies to see if any improvement could be achieved.
Figure 2 shows the prompt that was used to transform an LLM into an evaluator with the same criteria as humans when
addressing Abstractive Question-Answering tasks.
LLM Evaluation System Prompt in Abstractive Question-Answering:
Evaluarás la calidad de una respuesta generativa comparándola con una respuesta de referencia, basán-
dote en un contexto dado y un histórico de la conversación. La evaluación será en una escala de 1 a 5, donde 1 es
la peor calificación y 5 es la mejor. A continuación, se presentan las definiciones de cada puntuación:
- Score 1:
La respuesta generada es irrelevante, incorrecta o no guarda ninguna relación con la pre-
gunta, el contexto o la respuesta de referencia. La información es confusa o errónea.
- Score 2: La respuesta generada es parcialmente relevante pero contiene errores significativos o malin-
terpretaciones en comparación con la respuesta de referencia. Muestra una comprensión limitada del contexto y
no responde completamente a la pregunta.
- Score 3: La respuesta generada es relevante y correcta en términos generales, pero carece de profundi-
dad o detalle comparada con la respuesta de referencia. Cumple con los requisitos básicos, pero no aporta
información adicional ni matices importantes.
- Score 4: La respuesta generada es precisa y detallada, demostrando una buena comprensión del con-
texto y es comparable en calidad a la respuesta de referencia. Responde a la pregunta de manera completa y
proporciona información adicional útil, aunque puede faltar algún pequeño detalle.
- Score 5: La respuesta generada es excepcionalmente clara, completa y precisa.
Demuestra una com-
prensión profunda del contexto y responde a la pregunta de manera exhaustiva, proporcionando detalles y matices
que enriquecen la respuesta, igualando o superando la calidad de la respuesta de referencia.
Tu evaluación debe seguir el siguiente formato: {"score": <integer>}.
Figure 2: System prompt used for the LLM evaluation in Abstractive Question-Answering.
Table 3 summarizes the accuracy of various automatic evaluators compared to human evaluations. The two-model
ensemble combined the Llama-3.1 and SAS scores, while the three-model ensemble combined, in addition to those
already mentioned, the Prometheus metric. The Quantized Llama-3.1-70B-Instruct model achieved the highest average
accuracy of 0.452.
6

--- Page 7 ---

Model
Average
Score 1
Score 2
Score 3
Score 4
Score 5
Prometheus
0.276
0.8
0.25
0.29
0
0.04
Normalized SAS
0.33
0.7
0
0
0
0.95
Llama-3.1-8B-Instruct
0.404
0.3
0.25
0.25
0.58
0.64
Ensemble of 3 models
0.39
0.6
0.12
0.29
0.84
0.1
Ensemble of 2 models
0.364
0.27
0.22
0.07
0.65
0.61
Quantized Llama-3.1-70B-Instruct
0.452
0.5
0.71
0.09
0.53
0.43
GPT-4o
0.356
0.5
0.29
0.27
0.53
0.19
Table 3: Accuracy for each metric in each score definition.
Table 4 shows the number of matches and correlation coefficients between the automatic evaluations and human
evaluations. The Llama-3.1-8B-Instruct model had the highest number of matches (43 out of 90) and strong correlations.
Model
Matches
Pearson correlation [45]
Kendall correlation [46]
Prometheus
13
0.42
0.33
Normalized SAS
27
0.68
0.57
Llama-3.1-8B-Instruct
43
0.62
0.48
Ensemble 3 Models
27
0.62
0.45
Ensemble 2 Models
41
0.65
0.49
Quantized Llama-3.1-70B-Instruct
36
0.74
0.56
GPT-4o
31
0.73
0.59
Table 4: Matches and correlations between models and human evaluation.
Figure 3 compares the score density distributions across the 90 example conversations, showing that the LLM-based
evaluators, particularly Llama-3.1-based and GPT-4o, had the most similar distributions to human evaluations. The
distributions are discrete, since all the evaluations have been characterized as 5 different scores, but the graph shows a
KDE Plot with all the approximate distributions, ordered by their proximity to the human evaluation (Human Eval),
based on the Wasserstein distance [47]. The Llama-3.1-8B-Instruct model was selected as the automated evaluator due
to its strong performance in matching human evaluations and its efficiency.
7

--- Page 8 ---

Figure 3: Density comparisons across different metrics. Legend and color map are sorted based on distance to human
evaluations.
2.6
IIC Private Corpora
The data were created from plain text extracted from the web, encompassing information from various domains. To
collect these data, texts were carefully selected from the chosen domains, and contexts were subsequently extracted to
formulate corresponding questions and answers. Particular emphasis was placed on ensuring that the contexts were
comprehensive and detailed.
All high-quality private corpora were generated and reviewed manually by humans following a specific annotation guide.
This guide required computational linguists to generate question-answer pairs based on a given context. Each response
was written by an annotator and subsequently reviewed by other annotators to ensure accuracy and consistency.
In addition to using high-quality sources, experiments were conducted to generate quality data for function calling,
autonomous agents, and SQL execution tasks. These experiments aimed to address underrepresented use cases in
Spanish. However, the data was ultimately discarded due to the lack of human review.
2.7
Preferences Dataset (PD)
Based on the filter and data augmentation criteria, we created a Preferences Dataset (PD). Only the Type 1, 2, and 3
conversations described in Table 2 were retained. For the Type 2 conversations, which lack variants but were annotated
by experts, we decided to use only the private sources of the IIC, although many others sources passed the quality filters.
This decision was made to better represent the kind of task we wanted to put focus on: abstractive question answerin.
New responses were generated using the LLMs mentioned in 2.4 under the assumption that the expert-annotated
response is always better than any model-generated response, and the Llama-3.1-8B-Instruct model was used as
evaluator to score these responses and sort them. Finally, the best and worst generated responses were selected, resulting
in three pairs of preferences:
• Expert-annotated is better than the best-scored generated response.
• Expert-annotated is better than the worst-scored generated response.
• The best-scored generated response is better than the worst-scored generated response.
8

--- Page 9 ---

Notably, the only case where humans are not involved is the latter, as both the evaluation and the responses are generated
by models. In this way, the model is learning both from human feedback and from the outputs of a series of LLMs,
arranged by their quality, resulting in a form of model distillation.
The final preference corpus comprises 21,975 conversations, including variants, suitable for both reinforcement learning
algorithms and supervised fine-tuning. Table 5 details the sources and number of samples in the preference dataset.
Name
nº samples
OpenAssistant [28]
16870
IIC Private Corpora
5105
Table 5: Preferences dataset after data augmentation.
Table 6 provides the number of samples in the train and validation subsets of the preference dataset.
Split
nº samples
Train
21755
Validation
220
Table 6: Preferences dataset splitting.
In summary, the process of deriving the preference dataset involved collecting a large-scale corpus, filtering it to retain
high-quality conversations, augmenting it with alternative responses, and evaluating the quality of these responses. This
iterative approach ensures that the final dataset is well-suited for preference learning and the alignment of LLMs to the
Spanish language.
3
Model
Pursuing our objective of creating a model with limited computational resources, open-source models were utilized and
aligned with the Preferences Dataset (PD) described in the previous section, using the Direct Preference Optimization
(DPO) algorithm [13]. Additionally, the final model was quantized to different precisions using llama.cpp [8] to allow
for efficient inference.
3.1
Architecture
RigoChat-7b-v2 is a model based on Qwen-2.5 [40,48]. Specifically, it builds upon the Qwen2.5-7B-Instruct model
and has been fine-tuned using DPO to enhance its performance in the Spanish language. We do not perform any
modifications in the model architecture or its tokenizer.
3.2
Training process
The training details are provided in Table 7. For this work, the Transformer Reinforcement Learning (TRL) library [49]
was employed. Specifically, the example script published for applying DPO was adapted to the dataset presented in
Table 6.
9

--- Page 10 ---

DPOConfig argument
Value
num_train_epochs
2
eval_steps
500
save_steps
100
save_total_limit
5
per_device_train_batch_size
1
per_device_eval_batch_size
1
gradient_accumulation_steps
16
learning_rate
5 · 10−6
max_length
8192
max_prompt_length
6656
gradient_checkpointing
True
weight_decay
0.001
optim
rmsprop
lr_scheduler_type
cosine
Table 7: Configuration for the DPO training. Parameters not shown here used the default values of the library.
To manage memory usage during training, the Parameter-Efficient Fine-Tuning (PEFT) framework [50] was employed,
particularly the LoRA method [6]. The model configuration details are also available in Table 8.
LoRA Config Parameter
Value
r
64
lora_alpha
16
lora_dropout
0.1
task_type
CAUSAL_LM
target_modules
all-linear
use_rslora [51]
True
Table 8: Configuration for the PEFT model and LoRA hyperparameters. Parameters not shown here used the default
values of the library.
The model was trained on a single NVIDIA A100 GPU with Tensor Core for 8.5 hours, a minimal fraction of the
compute power required when training a full LLM from scratch. However, and as discussed in subsequent sections,
these results demonstrate that it is possible to align LLMs to a particular language, with limited hardware resources,
while maintaining or slightly improving performance compared to state-of-the-art models across various use cases.
Figure 4 presents the evolution of the DPO loss during the training process. A noticeable reduction in error was observed
during the second epoch; while this might hint some kind of overfitting to our preference data, further results will show
that the performance of the model does in fact increase for other datasets.
10

--- Page 11 ---

Figure 4: DPO Loss [13] of the training process.
The algorithm demonstrated significant sensitivity to the learning rate, with catastrophic forgetting occurring at
values above 10−5, rendering the experiment ineffective, while smaller values showed no substantial improvements.
Additionally, experiments were conducted using different training approaches, including fine-tuning the base model
Qwen2.5-7B with the high-quality instruction dataset from Table 1 before applying DPO, but results were inferior to
starting directly from Qwen2.5-7B-Instruct. Other tests explored the impact of supervised learning alone, without DPO,
as well as alternative state-of-the-art models. This section presents only the most successful approach, while a summary
of additional experiments is provided in the evaluation section as ablation studies (refere to 4.3).
3.3
Quantizations
Quantized versions of the trained model were also generated using the llama.cpp library [8], to allow for efficient
inference. Most quantization methods rely on truncation, scaling, or similar strategies to convert bfloat16 precision
weights into lower-precision weights. However, some techniques employ a small dataset to calibrate the final model. For
those strategies we employed the best threads (responses validated by humans) from the Preferences Dataset described
in 5.
All quantization methods, along with their bit precision, types and size are detailed in Table 10. Quantizations requiring a
calibration dataset are prefixed with an ‘i’, indicating that an importance matrix was be computed during the quantization
process. This approach is particularly useful when the precision of the quantized model is too low. For more information
on llama.cpp quantization methods, see [52]; for details on the importance matrix computation, refer to [53].
3.4
Model availability
RigoChat 2 (https://huggingface.co/IIC/RigoChat-7b-v2) and all its quantized variants (https://
huggingface.co/IIC/RigoChat-7b-v2-GGUF) are publicly available at Hugging Face under a permissive license
suitable for research and non-commercial applications.
4
Evaluations
To assess the performance of RigoChat 2 and other competing LLMs, several high-quality corpora tailored to specific
evaluation needs were developed:
11

--- Page 12 ---

• AQuAS [54]: A manually curated corpus created by two computational linguists to evaluate language models
in the task of Abstractive Question-Answering in Spanish. It includes examples from domains such as finance,
insurance, healthcare, law, and music.
• RagQuAS [55]: Another manually curated corpus developed by the same linguists to evaluate full RAG
systems and language models in Abstractive Question-Answering tasks in Spanish. This corpus spans a wide
range of domains, including hobbies, linguistics, pets, health, astronomy, customer service, cars, daily life,
documentation, energy, skiing, fraud, gastronomy, languages, games, nail care, music, skating, first aid, recipes,
recycling, complaints, insurance, tennis, transportation, tourism, veterinary, travel, and yoga.
• CAM (private corpus): This corpus consists of frequently asked questions (FAQs) sourced from consumer-
related topics on the public websites of the Comunidad de Madrid (Autonomous Community of Madrid). The
questions are categorized into three levels of degradation—E1, E2, and E3—intended to measure the LLMs’
ability to understand and effectively respond to poorly formulated queries caused by spelling errors, varying
levels of colloquialism, and similar issues. This task also falls under the Abstractive Question-Answering
category.
• Shops (private corpus): A multi-turn conversational corpus centered on policies from various clothing
companies. The task involves Multi-turn Abstractive Question-Answering.
• Insurance (private corpus): Another multi-turn conversational corpus, this one focuses on policies from
various insurance companies. It also involves Multi-turn Abstractive Question-Answering.
Each corpus includes the following columns: question, answer, and context(s) containing relevant information from
which the model can derive the answer. In multi-turn tasks, a chat history is also provided. It is important to emphasize
that the datasets used for model evaluation are distinct from those used for training in the IIC Private Corpora explained in
Tables 1 and 5. Among our private training corpora, they share only a similar distribution—not specific examples—with
the AQuAS, RagQuAS, and Shops datasets.
To score all responses the Llama-3.1-8b-Instruct model evaluator with the approach described in Figure 2 was used. All
corpora are private except for AQuAS and RagQuAS, which are publicly available and can serve as examples of the
structure and content of the others.
4.1
Comparison against other LLMs
Table 9 shows the results of evaluating RigoChat 2 and other relevant LLMs over the presented evaluation datasets.
The Llama-3.1-8B-Instruct model was used as the evaluator and it is important to highlight that, due to the variability
in LLMs’ responses in real-world use cases—arising from factors such as generation parameters and system prompt
configurations—we have estimated a margin of error of 0.5% in these scores. This estimate was obtained by conducting
repeated evaluations across various models.
Model
Average
AQuAS
RagQuAS
CAM
CAM_E1
CAM_E2
CAM_E3
Shops
Insurance
RigoChat-7b-v2
79.55
82.52
79.10
78.91
79.17
76.73
78.23
80.79
81.04
GPT-4o [44,56]
78.26
85.23
77.91
78.00
74.91
73.45
77.09
78.60
80.89
stablelm-2-12b-chat [42]
77.74
78.88
78.21
77.82
78.73
77.27
74.73
77.03
79.26
Mistral-Small-Instruct [57]
77.29
80.56
78.81
77.82
75.82
73.27
73.45
78.25
80.36
Qwen2.5-7B-Instruct [40,48]
77.17
80.93
77.41
77.82
75.09
75.45
72.91
78.08
79.67
Llama-3.1-8B-Instruct [2]
76.55
81.87
80.50
72.91
73.45
75.45
71.64
77.73
78.88
GPT-4o-mini [41]
76.48
82.80
75.82
76.36
74.36
72.36
71.82
78.25
80.08
Phi-3.5-mini-instruct [58]
76.38
81.68
81.09
75.82
74.73
71.45
70.36
77.43
78.45
gemma-2-9b-it [43]
75.80
82.80
78.11
72.91
73.45
71.09
71.27
77.08
79.72
Ministral-8B-Instruct [59]
75.19
79.63
77.31
76.00
73.45
72.36
70.18
76.44
76.14
GPT-3.5-turbo
74.78
80.93
73.53
76.73
72.55
72.18
69.09
75.63
77.64
Llama-2-7b-chat [60]
71.18
67.10
77.31
71.45
70.36
70.73
68.55
72.07
71.90
granite-3.0-8b-instruct [61]
71.08
73.08
72.44
72.36
71.82
69.09
66.18
69.97
73.73
RigoChat-7b-v1
62.13
72.34
67.46
61.27
59.45
57.45
57.64
62.10
59.34
salamandra-7b-instruct [62]
61.96
63.74
60.70
64.91
63.27
62.36
60.55
59.94
60.23
Table 9: Evaluation results across different models and tasks in Spanish.
The information in Table 9 is condensed in Figure 5. RigoChat-7b-v2 demonstrates a significant improvement over
other state-of-the-art models of similar size, including the base model we used for training (Qwen2.5-7B-Instruct),
12

--- Page 13 ---

and even surpassing more powerful models such as GPT-4o in these evaluations. This result highlights the feasibility
of adapting LLMs to specific use cases with limited resources and reduced training time. Additionally, due to the
complexity of the training dataset, these evaluations present certain challenges. Further improvements could likely be
achieved if the training process was more closely aligned with the evaluated use cases.
Figure 5: Bar Plot of the evaluation results. The figure is scaled from 50 to 90 in order to better appreciate the differences
between all tested models.
A final comparison involves evaluating the sensitivity of language models to colloquialisms, jargon, or any type of noise
introduced into user queries. For this purpose, the private CAM evaluation corpus is used, which quantifies different
query variants with varying levels of degradation. Figure 6 illustrates the performance evolution of the models as noise
increases in user queries. The general trend shows a decline in score as colloquialisms, jargon, and grammatical errors
increase. However, RigoChat-7b-v2 demonstrates greater resilience, maintaining its performance more effectively than
the other models.
13

--- Page 14 ---

Figure 6: Evolution of LLM performance as a function of degradation.
4.2
Performance of RigoChat 2 quantizations
The evaluations of RigoChat-7b-v2 across different quantization precisions can be found in Table 10. We can see that
the LLM-performance increases as bit accuracy increases back to that of the original model (Figure 7) .Observing
the performance decline as model size and precision are reduced provides valuable insight. Notably, models with as
little as 3-bit precision emerge as viable and cost-effective alternatives for the specific use cases they are designed for.
Additionally, models with up to 5-bit precision can be efficiently run on a standard CPU with 16 GB of RAM, making
them highly accessible for various applications.
Figure 7: Line Plot of the evaluation results of RigoChat-7b-v2 across different precisions.
14

--- Page 15 ---

precision
quant-type
size
Average
AQuAS
RagQuAS
CAM
CAM_E1
CAM_E2
CAM_E3
Shops
Insurance
16-bit
-
15.2
79.55
82.52
79.10
78.91
79.17
76.73
78.23
80.79
81.04
8-bit
q8_0
8.10
79.06
82.12
77.61
79.45
78.55
76.18
77.45
80.87
80.25
6-bit
q6_k
6.25
79.13
81.62
78.91
79.45
78.55
75.82
77.73
80.06
80.91
5-bit
q5_1
5.76
78.50
81.32
78.41
80.91
75.64
75.64
77.27
78.89
79.90
q5_k_m
5.44
78.73
81.62
79.30
79.27
77.09
76.55
75.82
79.24
80.96
q5_0
5.33
78.63
80.50
79.90
79.64
75.82
76.00
76.73
80.12
80.30
q5_k_s
5.32
78.53
80.44
79.90
78.73
77.45
75.64
75.45
80.76
79.87
4-bit
q4_1
4.87
78.41
81.68
77.91
79.09
76.36
76.18
75.45
80.41
80.23
q4_k_m
4.68
78.57
80.93
77.91
80.91
76.36
76.73
76.73
78.89
80.13
q4_k_s
4.46
78.62
81.18
78.61
78.18
77.64
76.00
76.36
80.29
80.66
q4_0
4.44
78.62
79.63
81.09
79.82
77.64
76.18
74.55
80.23
79.82
iq4_nl
4.44
78.61
81.12
78.51
78.91
76.73
78.00
75.45
79.94
80.20
iq4_xs
4.22
78.79
81.49
79.30
79.82
77.27
77.82
75.09
79.53
80.00
3-bit
q3_k_l
4.09
77.58
80.74
78.51
77.45
74.73
74.00
75.64
80.00
79.59
q3_k_m
3.81
78.11
80.37
77.61
78.55
77.09
76.00
76.18
79.77
79.34
q3_k
3.81
77.95
81.31
78.21
77.45
76.18
75.09
76.18
80.12
79.04
iq3_m
3.57
77.73
78.06
78.91
78.91
75.45
74.73
77.09
78.83
79.85
iq3_s
3.50
77.95
79.31
78.81
77.45
77.09
76.36
75.82
79.36
79.37
q3_k_s
3.49
77.88
80.93
78.01
77.82
76.55
75.45
75.09
79.71
79.44
iq3_xs
3.35
77.68
79.06
77.61
77.45
76.55
77.64
74.91
79.07
79.11
iq3_xxs
3.11
77.66
80.56
78.61
79.09
76.55
75.64
73.27
78.60
78.98
2-bit
q2_k
3.02
76.23
77.38
78.31
77.64
75.09
74.36
72.36
76.44
78.27
q2_k_s
2.83
75.95
77.57
76.42
79.09
75.64
74.00
73.27
75.39
76.24
iq2_m
2.78
76.37
77.06
76.82
77.82
76.00
74.18
74.36
77.43
77.26
iq2_s
2.60
75.04
77.94
76.42
75.09
75.45
72.73
70.55
76.68
75.48
iq2_xs
2.47
74.01
77.38
74.01
74.36
72.00
72.91
71.09
75.80
74.52
tq2_0
2.44
26.88
26.73
27.86
25.64
26.36
25.45
27.27
25.95
29.80
iq2_xxs
2.27
70.24
71.21
73.23
72.55
69.82
66.91
65.45
72.48
70.23
1-bit
tq1_0
2.14
27.08
27.85
28.56
27.09
25.27
25.82
26.18
27.00
28.86
iq1_m
2.04
59.59
56.45
64.38
59.09
61.27
58.36
58.55
60.64
58.02
iq1_s
1.90
40.50
36.82
39.70
40.91
38.91
41.45
40.73
42.27
43.17
Table 10: Evaluation results of RigoChat-7b-v2 across different precisions using llama.cpp quantizations and shorted by
model size. The models size is represented in gigabytes (GB).
4.3
Comparison of alternative fine-tuning strategies
Several alternative strategies to make use of the High Quality corpus from Table 1 and the Preferences Dataset from
5 were tested; in the following we present the most relevant ones, specifically those obtained with the Llama-3.1-8B
family and the previously discussed Qwen-2.5-7B. Table 11 presents the average score attained by these alternative
approaches in the evaluation datasets. The symbol ‘+’ is used to indicate several sequential steps of fine-tuning. For
instance, SFT + DPO refers to the application of the Supervised Fine-Tuning algorithm followed by Direct Preference
Optimization. Scores for the baseline models (no SFT or DPO applied) are also presented for reference. It should be
noted that the application of DPO directly to the base models was not tested, as it was deemed ineffective.
15

--- Page 16 ---

Model and algorithms
Llama-3.1 Score
Qwen2.5-7B
68.32
Qwen2.5-7B + SFT
69.23
Qwen2.5-7B + SFT + DPO
72.29
Qwen2.5-7B-Instruct
77.17
Qwen2.5-7B-Instruct + SFT
70.41
Qwen2.5-7B-Instruct + SFT + DPO
72.43
Qwen2.5-7B-Instruct + DPO
79.55
Llama-3.1-8B
66.16
Llama-3.1-8B + SFT
69.04
Llama-3.1-8B + SFT + DPO
71.11
Llama-3.1-8B-Instruct
76.55
Llama-3.1-8B-Instruct + SFT
70.36
Llama-3.1-8B-Instruct + SFT + DPO
72.13
Llama-3.1-8B-Instruct + DPO
78.38
Table 11: Average Llama-3.1 Score in the set of evaluations of all the experiments.
The training parameters used in DPO are presented in Table 7, while Table 12 details those for Supervised Fine Tuning.
Additionally, LoRA was employed with the configuration outlined in Table 8. Notably, applying our training approach
to the Llama-3.1-8B-Instruct model also demonstrates improvements, further validating the approach taken to adapt
LLMs to use cases efficiently and effectively.
DPOConfig argument
Value
num_train_epochs
2
eval_steps
50
save_steps
150
save_total_limit
5
per_device_train_batch_size
2
per_device_eval_batch_size
2
gradient_accumulation_steps
16
learning_rate
2 · 10−4
max_length
8192
gradient_checkpointing
True
weight_decay
0.001
optim
adamw_torch
lr_scheduler_type
cosine
Table 12: Configuration for the SFT training. Parameters not shown here used the default values of the library.
4.4
General performance of RigoChat-7b-v2
After demonstrating that RigoChat-7b-v2 achieves improvements in certain tasks related with question answering
with contexts in Spanish, it is essential to assess whether for a broader selection of tasks it remains as competent as
Qwen2.5-7B-Instruct (the original base model), or if some kind of catastrophic forgetting or heavy task-focusing has
taken place. To this end, Table 13 presents a comparison of results between RigoChat-7b-v2 and Qwen2.5-7B-Instruct
across some widely used datasets for LLM evaluation. Although some noticeable drops in performance can be observed
for the DROP, HumanEval and IfEval datasets, the rest of tasks present similar performance for both models, with a
significant improvement taking place for the Spanish MMMLU dataset. This confirms that the proposed procedure
has succeeded in aligning the base model to the Spanish language, while retaining most of the capabilities of the base
model for the English language and general-purpose tasks.
16

--- Page 17 ---

Datasets
RigoChat-7b-v2
Qwen2.5-7B-Instruct
General
MMLU [63]
74.07
74.24
MMMLU [63] (ES)
62.95
60.44
MMLU-Pro [64]
55.70
56.20
Reasoning
GPQA [65]
33.84
32.83
HellaSwag [66]
84.78
85.15
DROP [67]
62.14
66.20
Math
MATH [68]
68.42
69.16
GSM8K [69]
79.83
80.52
Coding
HumanEval [70]
78.66
81.71
LiveCodeBench [71]
15.38
12.44
Aligment
IfEval [72]
75.42
79.6
Table 13: General performance of RigoChat-7b-v2 and Qwen-2.5-7B-Instruct across classical LLM benchmarks.
These evaluations have been carried out with the open-source evaluation tool OpenCompass [73].
5
Conclusions and Future Work
Leveraging limited hardware resources, our study demonstrates that robust performance is achievable—even surpassing
state-of-the-art models in certain scenarios. Crucially, our results emphasize that high-quality and representative data
are as important as abundant computational power. By meticulously curating our datasets, we effectively align a
multilingual, open-source model to perform more effectively in Spanish, thereby democratizing access to advanced AI
while enhancing privacy, reducing dependency on third-party providers, and optimizing resource efficiency.
The proposed approach to augment data by obtaining responses from different models on threads of interest has been
shown to be an effective distillation method if these responses are ranked and DPO is applied. Furthermore, the model
obtained using this approach, RigoChat-v2, does not lose general performance in those tasks for which its base model
was initially designed, as shown in the evaluations of classical tasks in 4.4.
For future research focused on improving LLMs, we plan to:
• Expand and enhance data quality: Make a substantial investment in acquiring and curating high-quality
datasets, as they serve as long-lasting assets that can be reused in the future. Unlike models and GPUs, which
can become outdated quickly and require repeated investments, high-quality data maximize the potential of
available hardware while offering a more sustainable and cost-effective strategy.
• Develop robust evaluation methods: Advance methodologies to automate human evaluation simulation,
Data Augmentation and further maximize data utilization.
• Integrate advanced training techniques to take advantage of all data presented in 1. Specifically, apply
Group Relative Policy Optimization (GRPO) [74] on tasks where outcome quality can be easily measured, in
conjunction with our best-performing DPO-trained model on our large-scale instruction corpus. This approach
could effectively transfer the high-quality responses from the preference corpus to the extensive set of threads
available.
17

--- Page 18 ---

These steps aim to reinforce the pivotal role of data quality in achieving superior model performance and to drive
continued innovation in resource-efficient AI.
Finally, the significant progress in high-quality massive multilingual corpora, such as FineWeb-2 [75], combined with
the stagnation in the publication of Natural Language Understanding (NLU) models until the release of ModernBERT
[76]—a state-of-the-art model incorporating the latest innovations—makes it feasible to train a Spanish-specific NLU
model. This approach follows the path we previously took with RigoBERTa [77].
References
[1] OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, and Lama Ahmad et al. Gpt-4 technical report, 2024.
[2] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, and Ahmad Al-Dahle et al. The llama 3
herd of models, 2024.
[3] Loubna Ben Allal, Anton Lozhkov, Elie Bakouch, Gabriel Martín Blázquez, Lewis Tunstall, Agustín Piqueres,
Andres Marafioti, Cyril Zakka, Leandro von Werra, and Thomas Wolf. Smollm2 - with great data, comes great
performance, 2024.
[4] Chunting Zhou, Pengfei Liu, Puxin Xu, Srini Iyer, Jiao Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, Ping Yu,
Lili Yu, Susan Zhang, Gargi Ghosh, Mike Lewis, Luke Zettlemoyer, and Omer Levy. Lima: Less is more for
alignment, 2023.
[5] Guilherme Penedo, Hynek Kydlíˇcek, Loubna Ben allal, Anton Lozhkov, Margaret Mitchell, Colin Raffel, Le-
andro Von Werra, and Thomas Wolf. The fineweb datasets: Decanting the web for the finest text data at scale,
2024.
[6] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu
Chen. Lora: Low-rank adaptation of large language models, 2021.
[7] Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer. Qlora: Efficient finetuning of quantized
llms, 2023.
[8] Georgi Gerganov. llama.cpp, 2024.
[9] Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Ré. Flashattention: Fast and memory-efficient
exact attention with io-awareness, 2022.
[10] Tri Dao. Flashattention-2: Faster attention with better parallelism and work partitioning, 2023.
[11] Jay Shah, Ganesh Bikshandi, Ying Zhang, Vijay Thakkar, Pradeep Ramani, and Tri Dao. Flashattention-3: Fast
and accurate attention with asynchrony and low-precision, 2024.
[12] María Grandury. The #somos600m project: Generating nlp resources that represent the diversity of the languages
from latam, the caribbean, and spain, 2024.
[13] Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, and Chelsea Finn. Direct
preference optimization: Your language model is secretly a reward model, 2024.
[14] Seungone Kim, Juyoung Suk, Shayne Longpre, Bill Yuchen Lin, Jamin Shin, Sean Welleck, Graham Neubig,
Moontae Lee, Kyungjae Lee, and Minjoon Seo. Prometheus 2: An open source language model specialized in
evaluating other language models, 2024.
[15] Yukyung Lee, Joonghoon Kim, Jaehee Kim, Hyowon Cho, and Pilsung Kang. Checkeval: Robust evaluation
framework using large language model via checklist, 2024.
[16] Fangyun Wei, Xi Chen, and Lin Luo. Rethinking generative large language model evaluation for semantic
comprehension, 2024.
[17] Chi Hu, Yuan Ge, Xiangnan Ma, Hang Cao, Qiang Li, Yonghua Yang, Tong Xiao, and Jingbo Zhu. Rankprompt:
Step-by-step comparisons make language models better reasoners, 2024.
[18] Hui Huang, Yingqi Qu, Jing Liu, Muyun Yang, Bing Xu, Tiejun Zhao, and Wenpeng Lu. Self-evaluation of large
language model based on glass-box features, 2024.
[19] Jiayin Wang, Fengran Mo, Weizhi Ma, Peijie Sun, Min Zhang, and Jian-Yun Nie. A user-centric multi-intent
benchmark for evaluating large language models, 2024.
[20] Julian Risch, Timo Möller, Julian Gutsch, and Malte Pietsch. Semantic answer similarity for evaluating question
answering models, 2021.
18

--- Page 19 ---

[21] Milan Gritta, Gerasimos Lampouras, and Ignacio Iacobacci. Humanrankeval: Automatic evaluation of lms as
conversational assistants, 2024.
[22] Nakatani Shuyo. Language detection library for java, 2010.
[23] Zhihong Chen, Shuo Yan, Juhao Liang, Feng Jiang, Xiangbo Wu, Fei Yu, Guiming Hardy Chen, Junying
Chen, Hongbo Zhang, Li Jianquan, Wan Xiang, and Benyou Wang. MultilingualSIFT: Multilingual Supervised
Instruction Fine-tuning, July 2023.
[24] Nicholas Kluge Corrêa. Aira, 2023.
[25] Ryoko AI. Sharegpt, 2023.
[26] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Tianle Li, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang,
Zhuohan Li, Zi Lin, Eric. P Xing, Joseph E. Gonzalez, Ion Stoica, and Hao Zhang. Lmsys-chat-1m: A large-scale
real-world llm conversation dataset, 2023.
[27] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan
Li, Dacheng Li, Eric. P Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. Judging llm-as-a-judge with
mt-bench and chatbot arena, 2023.
[28] Andreas Köpf, Yannic Kilcher, Dimitri von Rütte, Sotiris Anagnostidis, and Zhi-Rui Tam et al. Openassistant
conversations – democratizing large language model alignment, 2023.
[29] Iker García-Ferrero. Openhermes 2.5 spanish: Translation of instruction dataset for generalist llm assistants in any
language., 2024.
[30] Rishabh Maheshwary, Vikas Yadav, Hoang Nguyen, Khyati Mahajan, and Sathwik Tejaswi Madhusudhan.
M2lingual: Enhancing multilingual, multi-turn instruction alignment in large language models, 2024.
[31] Iker García-Ferrero, Rodrigo Agerri, Aitziber Atutxa Salazar, Elena Cabrio, and Iker de la Iglesia et al. Medical
mt5: An open-source multilingual text-to-text llm for the medical domain, 2024.
[32] Alvaro Hidalgo Eduardo Muñoz, Teresa Martín. Asistenciarefugiados, 2024.
[33] David Alonso Quispe Castillo. Wikihowes, 2024.
[34] Jorge Zamora Rey, Mario Crespo Miguel, and Isabel Moyano Moreno. Lingcomp_qa, un corpus educativo de
lingüística computacional en español, 2024.
[35] María Grandury, Javier de la Rosa, Daniel Vila, Natalia Elvira, and Carlos Alarcon. Somos clean alpaca-es, 2024.
[36] Argilla. Databricks dolly multilingual, 2024.
[37] Language Technologies Unit Barcelona Supercomputing Center. Mentor_es, 2024.
[38] Shivalika Singh, Freddie Vargus, Daniel Dsouza, Börje F. Karlsson, and Abinaya Mahendiran et al. Aya dataset:
An open-access collection for multilingual instruction tuning, 2024.
[39] Language Technologies Unit Barcelona Supercomputing Center. Rag multilingual, 2024.
[40] An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, and Chang Zhou et al. Qwen2 technical report.
arXiv, 2024.
[41] OpenAI. Gpt-4o mini: advancing cost-efficient intelligence, 2024. Online; accessed 2024.
[42] Marco Bellagente, Jonathan Tow, Dakota Mahan, Duy Phung, Maksym Zhuravinskyi, Reshinth Adithyan, James
Baicoianu, Ben Brooks, Nathan Cooper, Ashish Datta, et al. Stable lm 2 1.6 b technical report. arXiv preprint
arXiv:2402.17834, 2024.
[43] Gemma Team, Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, and Cassidy Hardin et al. Gemma 2:
Improving open language models at a practical size, 2024.
[44] OpenAI. Hello gpt-4o, 2024. Online; accessed 2024.
[45] Wilhelm Kirch, editor. Pearson’s Correlation Coefficient, pages 1090–1091. Springer Netherlands, Dordrecht,
2008.
[46] Maurice Kendall. A new measure of rank correlation. Biometrika, 1938.
[47] Cédric Villani. The Wasserstein distances, pages 93–111. Springer Berlin Heidelberg, Berlin, Heidelberg, 2009.
[48] Qwen Team. Qwen2.5: A party of foundation models, September 2024.
[49] Leandro von Werra, Younes Belkada, Lewis Tunstall, Edward Beeching, Tristan Thrush, Nathan Lambert,
Shengyi Huang, Kashif Rasul, and Quentin Gallouédec. Trl: Transformer reinforcement learning. https:
//github.com/huggingface/trl, 2020.
19

--- Page 20 ---

[50] Sourab Mangrulkar, Sylvain Gugger, Lysandre Debut, Younes Belkada, Sayak Paul, and Benjamin Bossan. Peft:
State-of-the-art parameter-efficient fine-tuning methods. https://github.com/huggingface/peft, 2022.
[51] Damjan Kalajdzievski. A rank stabilization scaling factor for fine-tuning with lora, 2023.
[52] HuggingFace. Gguf quantization types, 2024.
[53] Georgi Gerganov. llama.cpp imatrix, 2024.
[54] Instituto de Ingeniería del Conocimiento (IIC). Abstractive question-answering in spanish (aquas) dataset, 2024.
[55] Instituto de Ingeniería del Conocimiento (IIC). Retrieval-augmented-generation and queston-answering in spanish
(ragquas) dataset, 2024.
[56] OpenAI, Aaron Hurst, Adam Lerer, Adam P. Goucher, and Adam Perelman et al. Gpt-4o system card, 2024.
[57] Mistral AI. Mistral-small-instruct-2409, 2024.
[58] Marah Abdin, Jyoti Aneja, Hany Awadalla, Ahmed Awadallah, and Ammar Ahmad Awan et al. Phi-3 technical
report: A highly capable language model locally on your phone, 2024.
[59] Mistral AI. Ministral-8b-instruct-2410, 2024.
[60] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, and Amjad Almahairi et al. Llama 2: Open foundation
and fine-tuned chat models, 2023.
[61] IBM. granite-3.1-8b-instruct, 2024.
[62] Barcelona Supercomputing Center. salamandra-7b-instruct, 2024.
[63] Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
Measuring massive multitask language understanding. CoRR, abs/2009.03300, 2020.
[64] Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran
Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, and Wenhu
Chen. Mmlu-pro: A more robust and challenging multi-task language understanding benchmark, 2024.
[65] David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian
Michael, and Samuel R. Bowman. Gpqa: A graduate-level google-proof q and a benchmark, 2023.
[66] Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. Hellaswag: Can a machine really finish
your sentence? In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics,
2019.
[67] Dheeru Dua, Yizhong Wang, Pradeep Dasigi, Gabriel Stanovsky, Sameer Singh, and Matt Gardner. Drop: A
reading comprehension benchmark requiring discrete reasoning over paragraphs, 2019.
[68] Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn Song, and Jacob
Steinhardt. Measuring mathematical problem solving with the math dataset, 2021.
[69] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert,
Jerry Tworek, Jacob Hilton, Reiichiro Nakano, Christopher Hesse, and John Schulman. Training verifiers to solve
math word problems, 2021.
[70] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri
Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael
Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov,
Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave
Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex
Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders,
Christopher Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford,
Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam
McCandlish, Ilya Sutskever, and Wojciech Zaremba. Evaluating large language models trained on code, 2021.
[71] Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama,
Koushik Sen, and Ion Stoica. Livecodebench: Holistic and contamination free evaluation of large language models
for code, 2024.
[72] Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou, and Le Hou.
Instruction-following evaluation for large language models, 2023.
[73] OpenCompass Contributors. Opencompass: A universal evaluation platform for foundation models. https:
//github.com/open-compass/opencompass, 2023.
20

--- Page 21 ---

[74] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang,
Y. K. Li, Y. Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language
models, 2024.
[75] Guilherme Penedo, Hynek Kydlíˇcek, Vinko Sabolˇcec, Bettina Messmer, Negar Foroutan, Martin Jaggi, Leandro
von Werra, and Thomas Wolf. Fineweb2: A sparkling update with 1000s of languages, December 2024.
[76] Benjamin Warner, Antoine Chaffin, Benjamin Clavié, Orion Weller, Oskar Hallström, Said Taghadouini, Alexis
Gallagher, Raja Biswas, Faisal Ladhak, Tom Aarsen, Nathan Cooper, Griffin Adams, Jeremy Howard, and Iacopo
Poli. Smarter, better, faster, longer: A modern bidirectional encoder for fast, memory efficient, and long context
finetuning and inference, 2024.
[77] Alejandro Vaca Serrano, Guillem Garcia Subies, Helena Montoro Zamorano, Nuria Aldama Garcia, Doaa
Samy, David Betancur Sanchez, Antonio Moreno Sandoval, Marta Guerrero Nieto, and Alvaro Barbero Jimenez.
Rigoberta: A state-of-the-art language model for spanish, 2022.
21

```
