---
title: "2025-Garcia-PoETa v2 Toward More Robust Evaluation of Large Language Models in - PDF Extract"
source_pdf: "2025-Garcia-PoETa v2 Toward More Robust Evaluation of Large Language Models in.pdf"
pages: 32
extracted_at: "2026-02-13T09:50:28.037906"
---

# PDF Extract: 2025-Garcia-PoETa v2 Toward More Robust Evaluation of Large Language Models in

**Source PDF:** 2025-Garcia-PoETa v2 Toward More Robust Evaluation of Large Language Models in.pdf
**Total Pages:** 32

---

## Content

```
--- Page 1 ---

PoETa v2: Toward More Robust Evaluation of Large
Language Models in Portuguese
Thales Sales Almeida1,3
Ramon Pires1,3
Hugo Abonizio2,3
Rodrigo Nogueira2,3
Hélio Pedrini1
1 Institute of Computing, University of Campinas (UNICAMP)
2 School of Electrical and Computer Engineering, University of Campinas (UNICAMP)
3 Maritaca AI
Abstract
Large Language Models (LLMs) exhibit significant variations in performance
across linguistic and cultural contexts, underscoring the need for systematic evalu-
ation in diverse languages. In this work, we present the most extensive evaluation
of LLMs for the Portuguese language to date. Leveraging our newly introduced
PoETa v2 benchmark – a comprehensive suite of over 40 tasks in Portuguese –
we assess more than 20 models covering a broad spectrum of training scales and
computational resources. Our study reveals how computational investment and
language-specific adaptation impact performance in Portuguese, while also ana-
lyzing performance gaps in comparison to equivalent tasks in English. Through
this benchmark and analysis, PoETa v2 lays the groundwork for future research
on Portuguese language modeling and evaluation. The benchmark is available at
https://github.com/PoETaV2/PoETaV2.
1
Introduction
The rapid advancement of LLMs has fundamentally transformed natural language processing, en-
abling substantial progress across a wide range of applications [11, 15, 42, 43]. However, as LLMs
are increasingly deployed worldwide, it has become evident that their performance varies signifi-
cantly across languages and cultural contexts [5, 30, 32]. Linguistic diversity and uneven represen-
tation in training data mean that many languages, including Portuguese, remain underrepresented,
often resulting in lower model performance.
This uneven landscape has created critical gaps in our understanding of LLM capabilities in lower-
resource languages. Comprehensive, region-specific evaluation is therefore essential, both to ac-
curately measure model performance and to guide the development of LLMs that effectively serve
diverse communities.
In this work, we address this gap for Portuguese by introducing PoETa v2 (Portuguese Evaluation
Tasks), a benchmark for systematic and wide-ranging evaluation of LLMs in Portuguese. PoETa v2
comprises a total of 44 tasks, 12 of which are natively designed in Portuguese and capture regional
knowledge, culture, and linguistic features, such as tasks based on local exams, proverbs, and col-
loquial expressions. Additionally, we include 32 translated tasks adapted from established English
benchmarks, ensuring comprehensive coverage of linguistic skills and domains.
Using PoETa v2, we conduct the largest evaluation of LLMs in Portuguese to date, assessing the
performance of over 20 prominent open-source and proprietary models spanning a wide range of
sizes and training budgets. Our large-scale analysis provides a detailed characterization of LLM
Preprint.
arXiv:2511.17808v2  [cs.CL]  26 Nov 2025

--- Page 2 ---

performance in Portuguese, highlighting the influence of model scale, computational investment,
and language-specific pretraining.
2
Related Work
In this section, we review prior work in three key areas: (i) regional performance variation in LLMs,
(ii) development of Portuguese-specialized models, and (iii) existing evaluation tasks for Portuguese.
2.1
Regional Variation in LLM Performance
Recent studies have shown that LLM performance can differ considerably depending on cultural
and regional context. The Blend [32] benchmark measures language models’ understanding of daily
activities in different countries, demonstrating that models are more attuned to regions with stronger
digital representation. Similarly, WorldBench [30] leverages socioeconomic data from the World
Bank to evaluate how well models recall information about different countries, revealing higher
error rates in underrepresented regions, such as Africa and the Middle East.
TiEBe [5] evaluates factual recall of notable events across countries by generating QA pairs from
Wikipedia retrospective pages. Results indicate that LLMs perform better for events in economi-
cally stronger countries, with a high correlation observed between a country’s GDP and model per-
formance. These findings reveal systematic biases in LLM capabilities and reinforce the importance
of regionally aware evaluation initiatives, such as PoETa v2 for Portuguese-speaking countries.
2.2
Specialized Portuguese LLMs
Although research on Large Language Models (LLMs) has primarily focused on high-resource lan-
guages [27], there have been several dedicated efforts to develop models specialized for Portuguese.
These models vary in architecture, training paradigms, and scale, reflecting both the linguistic diver-
sity of Portuguese and the computational resources available. We summarize the main Portuguese
LLM initiatives as follows:
Sabiá series [1, 3, 34]: The Sabiá models represent some of the earliest attempts to adapt LLMs to
Portuguese. The first generation includes Sabiá-7B and Sabiá-65B (both Llama-based) and Sabiá-J
(GPT-J-based), trained on approximately 7.8 billion tokens from a carefully filtered subset of the
ClueWeb 2022 dataset. These models were designed to capture a broad spectrum of Portuguese
language patterns, including both European and Brazilian variants. Subsequent generations, Sabiá-2
and Sabiá-3, further improved model performance, but details of their methodology and training are
limited. Access to these newer iterations is primarily via commercial APIs.
Cabrita [24]: Cabrita is based on a continued pretraining of the OpenLlama 3B model. The project
adapted the tokenizer to better handle Portuguese-specific orthography and expanded the embedding
layers to accommodate a larger vocabulary. Training involved 7 billion tokens extracted from the
Portuguese subset of mC4.
Glória [28]: Glória models, built on the GPTNeo architecture, include versions with 1.3B and
2.7B parameters, trained specifically for European Portuguese. Their dataset comprises 35.5 billion
tokens, emphasizing formal and literary texts as well as contemporary usage. These models remain
restricted to research access, but provide an important reference for evaluating Portuguese LLMs in
the European variant.
TeenyTinyLlama [13]:
TeenyTinyLlama is a family of lightweight models with 160M and
460M parameters, trained from scratch on 6.2 billion Portuguese tokens. Designed for resource-
constrained environments, these models are suitable for deployment in scenarios where computa-
tional efficiency is critical, while still providing strong baseline performance across common NLP
tasks.
Tucano [14]: The Tucano family includes models trained from scratch on up to 500 billion Por-
tuguese tokens from the GigaVerbo dataset, with sizes up to 2.4B parameters. Tucano represents the
largest monolingual Portuguese LLMs trained entirely from scratch to date. These models aim to
capture extensive linguistic patterns across different Portuguese varieties and domains, from social
media to formal literature.
2

--- Page 3 ---

Curió [6]: Curió models are continually pretrained versions of existing LLMs, including Curió
1.1B (from TinyLlama) and Curió 7B (from LLama 2 7B). Both models were trained with up to 150
billion Portuguese tokens drawn from the ClassiCC-PT dataset, which aggregates diverse sources
such as news articles, academic texts, and web crawls. Curió 7B is noteworthy for being the only
Portuguese model at the 7B scale trained on over 100 billion Portuguese tokens, making it the largest
Portuguese LLM in terms of both model size and training corpus.
Despite the increasing number of Portuguese-specialized LLMs, systematic comparison remains
challenging. Each model is typically evaluated on a limited set of tasks or benchmarks, often with
a limited number of examples. Consequently, it is difficult to assess the actual progress in Por-
tuguese language modeling and to identify which models are best suited for specific applications.
This limitation highlights the importance of large-scale, standardized evaluation frameworks such as
PoETa v2, which provide consistent and culturally relevant benchmarks across Portuguese LLMs.
2.3
Existing Evaluation Tasks in Portuguese
Evaluation resources for Portuguese LLMs have grown but remain fragmented. Approaches fall into
two broad categories:
First, structured exams such as the Brazilian National University Entrance Exam (ENEM) [44], other
university entrance exams [2], and the national bar exam [17, 35] provide standardized, human-
relevant assessments of reasoning and language understanding, but focus on specific academic or
legal contexts.
Second, classification tasks derived from social media and informal text—such as TweetSentBR [10]
for sentiment analysis, HateBR [50], and PT Hate Speech [19]—assess model performance on user-
generated text and social signals.
Some exceptions, such as Faquad [40] (extractive QA) and BRoverbs [4] (multiple-choice on Brazil-
ian proverbs), expand the task diversity.
Nevertheless, substantial gaps remain. There is a lack of comprehensive benchmarks for ethical
reasoning, advanced problem-solving, code understanding, and cultural nuance in Portuguese. Ex-
isting datasets often do not cover commonsense reasoning, multilingual code generation, or ethical
decision-making at the level of English benchmarks. Addressing these gaps is crucial for building
robust, fair, and culturally aware Portuguese LLMs.
3
Methodology
To systematically evaluate the capabilities of LLMs in Portuguese, we designed a methodology
that combines careful task selection, comprehensive model coverage, and standardized evaluation
metrics. Our approach emphasizes both cultural specificity and general linguistic ability, enabling
comparisons across models of different architectures, sizes, and training strategies. In the following
subsections, we describe how PoETa v2 was constructed, how tasks were categorized, the models
included in our study, and the metrics used to assess their performance.
3.1
Task Collection and Benchmark Construction
PoETa v2 was designed to provide a broad assessment of LLM performance in Portuguese, balanc-
ing regional specificity with general language capabilities. When curating the benchmark tasks, we
prioritized those that could be solved using only pretraining knowledge, without requiring super-
vised fine-tuning. Consequently, we excluded open-ended chat tasks, code generation benchmarks,
complex reasoning challenges, and agentic evaluations. The guiding principle was to construct a
benchmark capable of tracking progress and guiding the development of Portuguese LLMs during
the early stages of pretraining.
The tasks in PoETa v2 are divided into two main classes:
• Native Portuguese Tasks (12 tasks): These tasks were developed natively in Portuguese
and grounded in regional and cultural contexts. Examples include questions from Brazilian
university entrance exams, tasks involving local proverbs and idiomatic expressions, and
3

--- Page 4 ---

region-specific knowledge. Incorporating these tasks allows PoETa v2 to evaluate how
well models capture cultural and regional knowledge. Despite their importance, the limited
number of native benchmarks means some fundamental aspects remain uncovered.
• Translated Tasks (32 tasks): To broaden the evaluation, PoETa v2 also includes tasks orig-
inally created in English and translated into Portuguese. These cover skills and domains
not fully represented in the native tasks, such as general reasoning, reading comprehen-
sion, and commonsense understanding. While translated tasks enhance coverage, we note
their limitations and emphasize the need for continued community efforts to increase the
proportion of natively developed Portuguese tasks.
3.2
Task Distribution
Each task in PoETa v2 is manually annotated with a primary task type to facilitate systematic eval-
uation. The main task types are defined as follows:
• Regression: Predicts a continuous numerical value rather than assigning the input to a
discrete category. For example, given two sentences, the model assigns a similarity score
between 1 and 5.
• Multiple-choice: The model selects the correct answer from a set of predefined options.
This format is commonly used in standardized exams and numerous benchmarks. We adopt
the notation “Multiple-choice (X)” to indicate that a task offers X alternative options.
• Binary QA (Question Answering): Provides a binary response to a question, such as
“yes” or “no.”
• Sentence entailment: Determines whether a hypothesis sentence logically follows from a
given premise.
• Extractive QA (Question Answering): Identifies and extracts the correct answer span
directly from a provided context passage in response to a question.
• Classification: Assigns an input to one of several predefined, discrete classes. For exam-
ple, classifying a news article into genres such as sports, technology, or politics.
• Sentiment Analysis: A specialized form of classification that determines the sentiment
expressed in a text. Examples include evaluating the sentiment of product reviews or social
media posts.
In addition to the primary task type, each task in PoETa v2 is annotated with one or more subcate-
gories, providing finer-grained insight into the specific skills and capabilities the task is designed to
evaluate. Examples of such subcategories include “math”, for tasks that primarily assess mathemat-
ical reasoning, and “Brazil”, for tasks that focus on knowledge or linguistic phenomena specific to
Brazil.
Figure 1 illustrates the distribution of both primary task types and subcategories across the bench-
mark. While each task is assigned a single primary type, multiple subcategories may apply. Detailed
information on the categorization of every task can be found in Appendix B.
3.3
Model Selection
We selected over 20 LLMs for evaluation, including both open-source and commercial models, cov-
ering a wide range of model sizes and training budgets. This enables analysis of how computational
investment and training strategies affect Portuguese language capabilities. We also include models
with additional pretraining on Portuguese-specific data to assess the impact of targeted adaptation.
General Open-Source Models
We evaluated several widely-used open-source models to establish robust baselines:
• Llama (Versions 1, 2, and 3) [21, 48, 49]: Three generations of the Llama family were
included, as they represent some of the most popular open-source LLMs. Including multi-
ple versions allows us to track progress and improvements across successive generations,
specifically with respect to Portuguese language performance.
4

--- Page 5 ---

0
2
4
6
8
Number of Tasks
Regression
Multiple Choice (6)
Sentence Entailment
Extractive QA
Multiple Choice (3)
Multiple Choice (5)
Classification
Sentiment Analysis
Binary QA
Multiple Choice (4)
(a) Distribution of task types in PoETa v2
0
2
4
6
8
10
Number of Tasks
Code
Proverbs
General Knowledge
Ethics
Hate Speech
Social Media
Math
Common Sense
Exams
Text Understanding
Reasoning
Brazil
(b) Distribution of task categories in PoETa v2
Figure 1: Overview of the distribution of task types and categories in PoETa v2. Each task is
assigned a primary type and may belong to multiple subcategories.
• Qwen (Versions 1, 2, 2.5, and 3) [7, 36, 47, 51]: The Qwen family has consistently demon-
strated strong multilingual capabilities, making these models suitable candidates for evalu-
ating cross-linguistic performance in Portuguese.
• Falcon 3[46]: We focus on the latest Falcon models, which offer explicit support for Por-
tuguese. Earlier Falcon versions (1 and 2) were excluded because their parameter count
exceeded our 14B threshold, which was set to maintain comparability across models.
Portuguese-Specialized Models
To evaluate the impact of targeted adaptation, we include several models specifically designed for
Portuguese:
• Sabiá 7B [34]: The first Llama-based model further pretrained on Portuguese (10B to-
kens). Sabiá 7B represents an early effort to specialize general-purpose open models for
Portuguese, providing a strong baseline for language-specific adaptation.
• Curió (1.1B and 7B) [6]: The Curió models undergo further pretraining with a focus on
Portuguese. Curió 1.1B continues pretraining from the TinyLlama 1T checkpoint using
150B Portuguese tokens from the ClassiCC-PT dataset, while Curió 7B is adapted from
5

--- Page 6 ---

Llama 2 7B and trained on 100B Portuguese tokens from the same dataset. These models
allow us to examine how additional pretraining on Portuguese data affects performance
across scales.
The Tucano family, trained from scratch on up to 500B Portuguese tokens [14], represents one of
the few fully monolingual LLM efforts in Portuguese. These models are limited to 2.4B parameters
and were trained on fewer than 1T tokens. As a result, their behavior differs from other evaluated
models, particularly in few-shot prompting scenarios, likely due to undertraining or variations in
data distribution. For these reasons, Tucano results are presented separately in Appendix C.
3.4
Evaluation Metrics
To evaluate model performance across the diverse tasks in PoETa v2, we employ a set of metrics
that capture both effectiveness, measured by NPM, and efficiency, measured by training compute.
These metrics allow us to compare models of varying sizes and training strategies, while accounting
for differences in task formats and scoring scales. In the following subsections, we describe the two
main metrics used in our analysis.
3.4.1
Computational Cost
To estimate the computational resources required to train each open-source model in our benchmark,
we adopt a slightly modified version of the non-embedding FLOPs per token metric proposed by
DeepSeek [9]. Specifically, the number of multiply–accumulate operations per token is defined as:
M = 72nlayerd2
model + 12nlayerdmodel
and the overall training cost as:
C = M · D.
where C denotes the total computational cost, D is the number of training tokens (in trillions), nlayer
is the number of transformer layers, and dmodel is the model width.
Our formulation differs from the original DeepSeek metric by omitting the sequence length. This
simplification accounts for recent models, such as Llama 3 and Qwen 3, which are pretrained in
multiple stages with varying sequence lengths.
3.4.2
Normalized Preferred Metric
PoETa v2 includes a diverse set of tasks, each with its own scoring range and evaluation criteria. To
allow aggregation and comparison across tasks, we adopt the Normalized Preferred Metric (NPM),
originally introduced in PoETa v1 [34]:
NPM = [preferred metric] −[random score]
[max score] −[random score]
NPM scales each task score such that a random model achieves an NPM of 0 and a perfect model
achieves an NPM of 1. For example, in a four-option multiple-choice task, random guessing yields
25% accuracy, while for an open-ended question-answering task, random performance is effectively
0%. Simply averaging raw scores across tasks would assign a random model an average value
of 12.5%, obscuring meaningful performance differences. In contrast, NPM ensures a consistent
baseline of 0, enhancing interpretability and enabling fair aggregation across heterogeneous tasks.
This metric can accommodate various preferred evaluation measures, including accuracy, F1-score,
and exact match, ensuring comparability across different task types.
4
Results
Table 2 presents the average NPM across all PoETa v2 tasks for more than 20 evaluated LLMs. The
table also reports model performance on the subset of tasks derived from BIG-Bench, both in the
original English version (BigBench EN) and the translated Portuguese version included in PoETa v2
(BIG-Bench PT). Additionally, Table 2 provides key model characteristics, including model size
(in billions of parameters) and the total number of pretraining tokens, as reported by the respective
model authors.
6

--- Page 7 ---

Table 1: Improvements in terms of NPM across categories for Portuguese-specialized LLMs.
Categories with the
Lowest Gain
Categories with the
Highest Gains
General
Knowledge
Code
Math
Brazil
Reasoning
Common
Sense
TinyLlama 1T →Curió 1.1B
-8.37
-6.84
5.76
-1.78
15.86
7.17
Llama 1 7B →Sabiá 7B
7.47
19.15
19.15
19.42
8.80
15.95
Llama 2 7B →Curió 7B
2.29
-2.82
-2.56
10.94
4.22
8.16
Table 2: Results for all evaluated models on PoETa v2, showing the average NPM across the full
benchmark, as well as performance on the BIG-Bench subset in both Portuguese and English. The
table also reports each model’s pretraining corpus size and number of parameters.
Model
Pretraining
Size
Model
Size
Computational
Cost
PoETa v2
BIG-Bench
(PT)
BIG-Bench
(EN)
Curió
Curió 1.1B
1T + 100B
1.1B
7.3
14.7
12.9
18.2
Curió 7B
2T + 100B
7B
81.2
34.8
30.9
27.2
Sabiá
Sabiá
1T + 10B
7B
39.0
32.4
26.3
28.3
Llama
TinyLlama 1T
1T
1.1B
6.64
10.2
5.6
15.2
Llama 1 7B
1T
7B
38.6
19.9
14.0
27.3
Llama 2 7B
2T
7B
77.3
29.5
29.3
29.7
Llama 2 13B
2T
13B
151
41.5
41.3
43.0
Llama 3.1 8B
15T
8B
580
53.5
50.2
52.8
Falcon 3
Falcon 3 1B
14T
1B
76
18.6
20.5
31.0
Falcon 3 3B
14T
3B
209
38.6
37.4
45.1
Falcon 3 7B
14T
7B
266
58.5
55.2
55.9
Falcon 3 10B
14T
10B
380
63.5
60.4
62.8
Qwen 1 and 2
Qwen 1 1.8B
2.4T
1.8B
17.4
19.0
21.3
30.4
Qwen 1 7B
2.4T
7B
93.8
41.1
36.9
43.8
Qwen 2 1.5B
7T
1.5B
33.3
38.4
35.1
34.5
Qwen 2 7B
7T
7B
181.3
58.8
51.8
56.2
Qwen 2.5
Qwen 2.5 1.5B
18T
1.5B
85.5
43.0
37.0
39.7
Qwen 2.5 3B
18T
3B
195.7
53.1
46.8
50.5
Qwen 2.5 7B
18T
7B
466.2
63.7
57.4
58.0
Qwen 2.5 14B
18T
14B
1630.8
71.0
63.5
62.0
Qwen 3
Qwen 3 1.7B
36T
1.7B
304
45.1
44.9
46.1
Qwen 3 4B
36T
4B
611
59.2
56.6
57.9
Qwen 3 8B
36T
8B
1565
64.7
57.7
63.2
Qwen 3 14B
36T
14B
2717
70.5
64.7
74.2
Commercial Models
GPT 4.1
-
-
-
76.2
67.9
69.9
GPT-4o
-
-
-
75.2
67.7
72.2
Sabiá 3
-
-
-
72.2
62.8
59.4
4.1
Overall Performance on PoETa v2
Figure 2 shows a clear positive correlation between computational cost and performance on Po-
ETa v2. Models with larger numbers of parameters and more extensive pretraining corpora gener-
7

--- Page 8 ---

ally achieve higher average NPM scores, indicating that increasing both model size and training data
contribute to improved performance in Portuguese.
101
102
103
Compute Cost (C)
10
20
30
40
50
60
70
Average NPM on PoETa V2
Curió 1.1B
Curió 7B
Sabiá 7B
TinyLlama 1T
Llama 1 7B
Llama 2 7B
Llama 2 13B
Llama 3.1 8B
Falcon 3 1B
Falcon 3 3B
Falcon 3 7B
Falcon 3 10B
Qwen 1.8B
Qwen 1 7B
Qwen 2 1.5B
Qwen 2 7B
Qwen 2.5 1.5B
Qwen 2.5 3B
Qwen 2.5 7B
Qwen 2.5 14B
Qwen 3 1.7B
Qwen 3 4B
Qwen 3 8B
Qwen 3 14B
Figure 2: Computational cost versus average NPM score for the evaluated models on PoETa v2.
Colors distinguish different model families.
Among open-source LLMs, the Qwen family stands out. Qwen 3 14B and Qwen 2.5 14B achieve
the highest average NPM scores among the evaluated open-source models—70.5 and 71, respec-
tively—outperforming all other models in the benchmark. Interestingly, Qwen 3 14B incurs roughly
twice the computational cost of Qwen 2.5 14B, yet both reach comparable performance levels.
Although computational cost is generally a strong predictor of model quality on PoETa v2, it does
not capture the full picture. Notable outliers highlight the importance of architectural design and
training data composition. For instance, Qwen 1 7B and Llama 2 7B exhibit similar computational
costs, yet Qwen 1 7B surpasses Llama 2 7B by more than 12 points in average NPM. A similar
trend is observed among higher-cost models: Llama 3.1 8B and Qwen 2.5 7B have comparable
computational costs, but Qwen 2.5 7B outperforms by nearly 10 points.
These discrepancies indicate that factors beyond model scale – such as architecture and the compo-
sition of pretraining data – can have a significant impact. In particular, the Qwen models’ superior
performance in Portuguese may be attributable to a higher proportion of Portuguese-language data in
their pretraining corpora compared to their Llama counterparts. Unfortunately, detailed information
about the training data for these models is not publicly available, limiting the depth of our analy-
sis. Nevertheless, our results strongly suggest that both computational investment and the linguistic
characteristics of the pretraining data are crucial for optimizing LLM performance in Portuguese.
Among commercial systems, GPT-4.1 and GPT-4o establish the current performance ceiling on
PoETa v2, achieving average NPM scores above 75. While these models outperform all open-
source alternatives, the margin is relatively small—approximately five points higher than Qwen 2.5
14B. Sabiá 3 also attains competitive results, with an average NPM of 72.2, slightly surpassing
the top-performing Qwen models. The narrow gap between the leading open-source models and
commercial systems suggests that PoETa v2 may be nearing a saturation point, which aligns with
the benchmark’s design, as it emphasizes tasks that can be solved without extensive supervised
fine-tuning.
4.2
Language and Regional Specialization
To evaluate the impact of continued pretraining on Portuguese data, we consider three models ex-
plicitly adapted in this manner: Curió 1.1B (initialized from TinyLlama), Curió 7B (initialized from
8

--- Page 9 ---

Llama 2 7B), and Sabiá (initialized from Llama 1 7B). Both Curió models underwent further pre-
training with approximately 100 billion Portuguese tokens, while Sabiá was pretrained with 10 bil-
lion Portuguese tokens.
All three models demonstrate notable improvements on PoETa v2 relative to their respective base
models. Specifically, Curió 1.1B gains 4.5 NPM points over TinyLlama, Curió 7B gains 5.3 points
over Llama 2 7B, and Sabiá achieves a striking 12.5-point improvement over Llama 1 7B.
The magnitude of Sabiá’s improvement is particularly remarkable given its smaller additional pre-
training corpus—ten times smaller than that used for the Curió models. This effect can be explained
by the performance of Llama 1 7B on the BIG-Bench subset of PoETa v2: the base model achieves
only half of its English score when evaluated in Portuguese, revealing a significant deficiency in
handling Portuguese-language tasks. Sabiá, however, substantially mitigates this imbalance, reach-
ing comparable performance in both languages after only 10 billion additional Portuguese tokens.
This suggests that Sabiá’s gains are primarily attributable to exposure to Portuguese content that
was largely absent in the original Llama 1 7B, which explicitly filtered out non-English data during
pretraining.
Interestingly, Llama 2 7B – the base model for Curió 7B – does not exhibit such a pronounced
language imbalance, indicating that it already possessed stronger multilingual capabilities. Never-
theless, continued pretraining in Portuguese still yields meaningful improvements, underscoring the
value of language-specific adaptation even for multilingual models.
4.3
Performance Variance Between Portuguese and English
Across the evaluated models, we observe an average performance difference of 3.5 points between
BIG-Bench tasks in Portuguese and English, with most models achieving higher scores in English.
Notable exceptions include Curió 7B and Qwen 2.5 14B, which perform slightly better in Por-
tuguese.
A more detailed analysis reveals that model size influences the magnitude of this language gap.
Smaller models (fewer than 5 billion parameters) exhibit an average difference of 5.1 points, while
mid-sized models (7B–8B parameters) show a reduced gap of 4.3 points. For larger models with
10B parameters or more, the average difference further decreases to 3.8 points. This trend suggests
that increased model scale not only enhances absolute performance but also narrows the gap between
English and Portuguese, likely reflecting stronger multilingual capabilities.
Nonetheless, significant outliers exist. Qwen 3 8B and Qwen 3 14B display unusually large gaps
of 5.5 and 9.5 points, respectively, performing exceptionally well on English BIG-Bench tasks but
failing to achieve comparable results in Portuguese. This discrepancy may stem from differences
in pretraining data composition or potential data contamination. However, due to the limited avail-
ability of detailed information about the Qwen 3 pretraining dataset, further analysis is not currently
possible.
4.4
Performance by Subcategories
Figure 3 presents the relationship between computational cost and performance across the nine most
recurrent subcategories in PoETa v2. Across all categories, we observe a positive correlation be-
tween computational cost and normalized performance metric (NPM), with R2 values ranging from
0.70 (Social Media) to 0.84 (Text Understanding and Exams). This indicates that larger and more
computationally expensive models generally achieve better results in every evaluated skill area, al-
though the strength of this trend varies by category.
Tasks in Text Understanding, Exams, Ethics, CommonSense, and Brazil display some of the
strongest correlations (R2 ≥0.82 ), suggesting that scaling model size and pretraining data tend
to yield consistent gains. These categories likely benefit from general language modeling improve-
ments and broad world knowledge.
Meanwhile, Reasoning, and Math also show substantial positive trends (R2 = 0.84). However, the
slopes in these tasks are lower, suggesting more limited returns from increased compute.
The weakest correlations appear in Social Media (R2 = 0.70) and General Knowledge (R2 =
0.77), both of which also present shallower scaling trends (slope ≤8). In Social Media, the high
9

--- Page 10 ---

101
102
103
0
20
40
60
80
100 y = 11.18log(x) +
13.22
R2 = 0.82
(a) Brazil
101
102
103
0
20
40
60
80
100 y = 13.43log(x) +
27.70
R2 = 0.84
(b) Text Understanding
101
102
103
0
20
40
60
80
100 y = 13.36log(x) +
29.55
R2 = 0.84
(c) Exams
101
102
103
0
20
40
60
80
100 y = 9.82log(x) +
15.77
R2 = 0.79
(d) Reasoning
101
102
103
0
20
40
60
80
100 y = 14.24log(x) +
23.83
R2 = 0.80
(e) Common Sense
101
102
103
0
20
40
60
80
100 y = 9.49log(x) +
24.32
R2 = 0.79
(f) Math
101
102
103
0
20
40
60
80
100 y = 7.60log(x) +
0.92
R2 = 0.70
(g) Social Media
101
102
103
0
20
40
60
80
100 y = 7.38log(x) + 4.02
R2 = 0.77
(h) General Knowledge
101
102
103
0
20
40
60
80
100 y = 15.13log(x) +
24.23
R2 = 0.83
(i) Ethics
Figure 3: Average NPM across task subcategories plotted against computational cost.
linguistic variability, prevalence of informal registers, and domain-specific vocabulary likely limit
the gains achievable through scaling alone. For General Knowledge, performance may depend more
on the explicit presence of relevant facts in the pretraining corpus than on overall model size.
Overall, while computational cost is a strong predictor of performance across all PoETa v2 subcate-
gories, the magnitude of scaling benefits is not uniform.
5
Conclusions
In this work, we introduced PoETa v2, a comprehensive benchmark for evaluating large language
models in Portuguese, including non-instruction-tuned ones, across a diverse set of tasks. Through
the largest systematic evaluation of Portuguese LLMs conducted to date, we analyzed model perfor-
mance in relation to computational investment and language-specific adaptation.
Our findings reveal a strong linear correlation between computational cost and performance in Por-
tuguese, while also highlighting notable outliers, indicating that model architecture and the com-
position of pretraining data play critical roles. Further pretraining on Portuguese data consistently
enhances model performance, particularly for base models with limited initial multilingual expo-
10

--- Page 11 ---

sure. Nonetheless, persistent performance gaps between English and Portuguese remain, especially
for smaller models.
Despite recent progress, our analysis underscores ongoing challenges: the need for more natively
developed Portuguese tasks, greater transparency regarding pretraining data, and targeted efforts to
mitigate linguistic and regional disparities. By providing an open, extensible benchmark along with
comprehensive baseline results, PoETa v2 aims to facilitate the development of more equitable and
culturally aware language models for the Portuguese language.
6
Future Work
Our findings highlight several promising directions for future research:
• Expansion of Native Tasks: Despite progress, the benchmark remains heavily reliant
on translated tasks. Increasing the proportion and diversity of natively developed Por-
tuguese tasks – especially in domains such as ethical reasoning, commonsense knowledge,
code understanding, and advanced problem solving – will be crucial for robust evaluation.
Community-driven initiatives and collaboration with domain experts can accelerate the de-
velopment of new culturally and linguistically rich datasets.
• Deeper Analysis of Pretraining Data: Our results suggest that pretraining data composi-
tion plays a central role in model performance, since many models with similar pretraining
compute cost achieve notably different performances in PoETa V2, however, the lack of
transparency regarding data sources limits deeper analysis. Future work should prioritize
both improved reporting of training data statistics and efforts to systematically quantify the
impact of different data distributions, particularly regarding Portuguese and other under-
represented languages.
• Robustness, Fairness, and Bias Analysis: A thorough assessment of model fairness, bias,
and robustness in the Portuguese context is still lacking. Future benchmarks and studies
should explicitly measure and address potential biases and performance disparities across
regional dialects, demographic groups, and sensitive domains.
• Benchmarking for fine-tuned models: While PoETa v2 focuses on general language un-
derstanding and reasoning, our study evaluates most models in their pre-training stage. Our
tasks are reasonably simple and do not cover common use cases for fine-tuned models, such
as advanced use cases like long text generation or agentic capabilities.
Ultimately, we hope PoETa v2 will serve as a foundation for continued progress in Portuguese
language model evaluation and facilitate movement towards more inclusive, regionally grounded
NLP research.
References
[1] Hugo Abonizio, Thales Sales Almeida, Thiago Laitz, Roseval Malaquias Junior, Gio-
vana Kerche Bonás, Rodrigo Nogueira, and Ramon Pires. Sabiá-3 Technical Report. arXiv
preprint arXiv:2410.12049, 2024.
[2] Thales Sales Almeida, Thiago Laitz, Giovana K Bonás, and Rodrigo Nogueira. BLUEX: A
Benchmark based on Brazilian Leading Universities Entrance Exams. In Brazilian Conference
on Intelligent Systems, pages 337–347. Springer, 2023.
[3] Thales Sales Almeida, Hugo Abonizio, Rodrigo Nogueira, and Ramon Pires. Sabiá-2: A New
Generation of Portuguese Large Language Models. arXiv preprint arXiv:2403.09887, 2024.
[4] Thales Sales Almeida, Giovana Kerche Bonás, and João Guilherme Alves Santos. BRoverbs
– Measuring How Much LLMs Understand Portuguese Proverbs. arXiv 2509.08960, 2025.
https://arxiv.org/abs/2509.08960.
[5] Thales Sales Almeida, Giovana Kerche Bonás, João Guilherme Alves Santos, Hugo Abonizio,
and Rodrigo Nogueira. TiEBe: Tracking Language Model Recall of Notable Worldwide Events
Through Time. arXiv 2501.07482, 2025. https://arxiv.org/abs/2501.07482.
11

--- Page 12 ---

[6] Thales Sales Almeida, Rodrigo Nogueira, and Helio Pedrini. Building High-Quality Datasets
for Portuguese LLMs: From Common Crawl Snapshots to Industrial-Grade Corpora, 2025.
URL https://arxiv.org/abs/2509.08824.
[7] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin
Ge, Yu Han, Fei Huang, et al. Qwen technical report. arXiv preprint arXiv:2309.16609, 2023.
[8] Luciana Bencke, Francielle Vasconcellos Pereira, Moniele Kunrath Santos, and Viviane Mor-
eira. InferBR: A Natural Language Inference Dataset in Portuguese. In Joint International
Conference on Computational Linguistics, Language Resources and Evaluation, pages 9050–
9060, 2024.
[9] Xiao Bi, Deli Chen, Guanting Chen, Shanhuang Chen, Damai Dai, Chengqi Deng, Honghui
Ding, Kai Dong, Qiushi Du, and Zhe Fu. DeepSeek LLM: Scaling Open-Source Language
Models with Longtermism. arXiv preprint arXiv:2401.02954, 2024.
[10] Henrico Bertini Brum and Maria das Graças Volpe Nunes. Building a Sentiment Corpus of
Tweets in Brazilian Portuguese. arXiv preprint arXiv:1712.08917, 2017.
[11] Zina Chkirbene, Ridha Hamila, Ala Gouissem, and Unal Devrim. Large Language Models
(LLM) in Industry: A Survey of Applications, Challenges, and Trends. In IEEE 21st Interna-
tional Conference on Smart Communities: Improving Quality of Life using AI, Robotics and
IoT (HONET), pages 229–234. IEEE, 2024.
[12] Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick,
and Oyvind Tafjord. Think you have Solved Question Answering? Try ARC, the AI2 Reason-
ing Challenge. arXiv:1803.05457v1, 2018.
[13] Nicholas Kluge Corrêa, Sophia Falk, Shiza Fatimah, Aniket Sen, and Nythamar De Oliveira.
TeenyTinyLlama: Open-Source Tiny Language Models Trained in Brazilian Portuguese. Ma-
chine Learning with Applications, 16:100558, 2024.
[14] Nicholas Kluge Corrêa, Aniket Sen, Sophia Falk, and Shiza Fatimah. Tucano: Advancing
Neural Text Generation for Portuguese. arXiv preprint arXiv:2411.07854, 2024.
[15] Sumit Kumar Dam, Choong Seon Hong, Yu Qiao, and Chaoning Zhang. A Complete Survey
on LLM-based AI Chatbots. arXiv preprint arXiv:2406.16937, 2024.
[16] Gabriela De Melo, Vinicius Imaizumi, and Fábio Cozman. Winograd Schemas in Portuguese.
In Encontro Nacional de Inteligência Artificial e Computacional, pages 787–798. SBC, 2019.
[17] Pedro Delfino, Bruno Cuconato, Edward Hermann Haeusler, and Alexandre Rademaker. Pass-
ing the Brazilian OAB Exam: Data Preparation and Some Experiments.
arXiv preprint
arXiv:1712.05128, 2017.
[18] Jack FitzGerald, Christopher Hench, Charith Peris, Scott Mackie, Kay Rottmann, Ana
Sanchez, Aaron Nash, Liam Urbach, Vishesh Kakarala, Richa Singh, Swetha Ranganath, Lau-
rie Crist, Misha Britan, Wouter Leeuwis, Gokhan Tur, and Prem Natarajan. MASSIVE: A
1M-Example Multilingual Natural Language Understanding Dataset with 51 Typologically-
Diverse Languages, 2022.
[19] Paula Fortuna, Joao Rocha da Silva, Leo Wanner, and Sérgio Nunes. A Hierarchically-Labeled
Portuguese Hate Speech Dataset. In Third Workshop on Abusive Language Online, pages 94–
104, 2019.
[20] Mor Geva, Daniel Khashabi, Elad Segal, Tushar Khot, Dan Roth, and Jonathan Berant. Did
Aristotle use a Laptop? A Question Answering Benchmark with Implicit Reasoning Strategies.
Transactions of the Association for Computational Linguistics, 9:346–361, 2021.
[21] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian,
Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The
llama 3 herd of models. arXiv preprint arXiv:2407.21783, 2024.
12

--- Page 13 ---

[22] Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn Song, and Jacob
Steinhardt. Aligning AI with Shared Human Values. arXiv preprint arXiv:2008.02275, 2020.
[23] Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul Arora, Steven Basart, Eric Tang, Dawn
Song, and Jacob Steinhardt.
Measuring Mathematical Problem Solving with the MATH
Dataset. NeurIPS, 2021.
[24] Celio Larcher, Marcos Piau, Paulo Finardi, Pedro Gengo, Piero Esposito, and Vinicius Caridá.
Cabrita: Closing the Gap for Foreign Languages. arXiv preprint arXiv:2308.11878, 2023.
[25] Jian Liu, Leyang Cui, Hanmeng Liu, Dandan Huang, Yile Wang, and Yue Zhang. LogIQA:
A Challenge Dataset for Machine Reading Comprehension with Logical Reasoning. arXiv
preprint arXiv:2007.08124, 2020.
[26] Shayne Longpre, Yi Lu, and Joachim Daiber. MKQA: A Linguistically Diverse Benchmark
for Multilingual Open Domain Question Answering. Transactions of the Association for Com-
putational Linguistics, 9:1389–1406, 2021.
[27] Shayne Longpre, Nikhil Singh, Manuel Cherep, Kushagra Tiwary, Joanna Materzynska,
William Brannon, Robert Mahari, Naana Obeng-Marnu, Manan Dey, and Mohammed
Hamdy. Bridging the Data Provenance Gap Across Text, Speech and Video. arXiv preprint
arXiv:2412.17847, 2024.
[28] Ricardo Lopes, João Magalhães, and David Semedo. GlórIA: A Generative and Open Large
Language Model for Portuguese. arXiv preprint arXiv:2402.12969, 2024.
[29] Andrew Maas, Raymond E Daly, Peter T Pham, Dan Huang, Andrew Y Ng, and Christopher
Potts. Learning Word Vectors for Sentiment Analysis. In 49th Annual Meeting of the Associa-
tion for Computational Linguistics: Human Language Technologies, pages 142–150, 2011.
[30] Mazda Moayeri, Elham Tabassi, and Soheil Feizi. WorldBench: Quantifying Geographic Dis-
parities in LLM Factual Recall. In ACM Conference on Fairness, Accountability, and Trans-
parency, pages 1211–1228, 2024.
[31] Nasrin Mostafazadeh, Nathanael Chambers, Xiaodong He, Devi Parikh, Dhruv Batra, Lucy
Vanderwende, Pushmeet Kohli, and James Allen. A Corpus and Cloze Evaluation for Deeper
Understanding of Commonsense Stories. In Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technologies, pages 839–849,
2016.
[32] Junho Myung, Nayeon Lee, Yi Zhou, Jiho Jin, Rifki Putri, Dimosthenis Antypas, Hsuvas
Borkakoty, Eunsu Kim, Carla Perez-Almendros, and Abinew Ali Ayele. BLEnD: A Bench-
mark for LLMs on Everyday Knowledge in Diverse Cultures and Languages. Advances in
Neural Information Processing Systems, 37:78104–78146, 2024.
[33] Desnes Nunes, Ricardo Primi, Ramon Pires, Roberto Lotufo, and Rodrigo Nogueira. Evalu-
ating GPT-3.5 and GPT-4 Models on Brazilian University Admission Exams. arXiv preprint
arXiv:2303.17003, 2023.
[34] Ramon Pires, Hugo Abonizio, Thales Sales Almeida, and Rodrigo Nogueira. Sabiá: Por-
tuguese Large Language Models. In Brazilian Conference on Intelligent Systems, pages 226–
240. Springer, 2023.
[35] Ramon Pires, Roseval Malaquias Junior, and Rodrigo Nogueira. Automatic Legal Writing
Evaluation of LLMs. arXiv preprint arXiv:2504.21202, 2025.
[36] Qwen, :, An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu,
Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu,
Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji
Lin, Tianhao Li, Tianyi Tang, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang
Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. Qwen2.5
technical report, 2025. URL https://arxiv.org/abs/2412.15115.
13

--- Page 14 ---

[37] Melissa Roemmele, Cosmin Adrian Bejan, and Andrew S Gordon. Choice of Plausible Al-
ternatives: An Evaluation of Commonsense Causal Reasoning. In AAAI spring symposium:
logical formalizations of commonsense reasoning, pages 90–95, 2011.
[38] Lucas Nildaimon Santos Silva, Livy Real, Ana Claudia Bianchini Zandavalle, Carolina Fran-
cisco Gadelha Rodrigues, Tatiana Silva Gama, Fernando Guedes Souza, and Phillipe Der-
wich Silva Zaidan. RePro: A Benchmark for Opinion Mining for Brazilian Portuguese. In
16th International Conference on Computational Processing of Portuguese, volume 1, pages
432–440, 2024.
[39] Maarten Sap, Hannah Rashkin, Derek Chen, Ronan LeBras, and Yejin Choi.
SocialIQA:
Commonsense Reasoning about Social Interactions. arXiv preprint arXiv:1904.09728, 2019.
[40] Hélio Fonseca Sayama, Anderson Viçoso Araujo, and Eraldo Rezende Fernandes. FaQuAD:
Reading Comprehension Dataset in the Domain of Brazilian Higher Education. In 8th Brazil-
ian Conference on Intelligent Systems, pages 443–448. IEEE, 2019.
[41] Tal Schuster, Adam Fisch, and Regina Barzilay. Get your Vitamin C! Robust Fact Verification
with Contrastive Evidence. arXiv preprint arXiv:2103.08541, 2021.
[42] Sina Shool, Sara Adimi, Reza Saboori Amleshi, Ehsan Bitaraf, Reza Golpira, and Mah-
mood Tara. A Systematic Review of Large Language Model (LLM) Evaluations in Clinical
Medicine. BMC Medical Informatics and Decision Making, 25(1):117, 2025.
[43] Marco Siino, Mariana Falco, Daniele Croce, and Paolo Rosso. Exploring LLMs Applications
in Law: A Literature Review on Current Legal NLP Approaches. IEEE Access, 2025.
[44] Igor Cataneo Silveira and Denis Deratani Mauá.
Advances in Automatically Solving the
ENEM. In 7th Brazilian Conference on Intelligent Systems, pages 43–48. IEEE, 2018.
[45] Richard Socher, Alex Perelygin, Jean Wu, Jason Chuang, Christopher D Manning, Andrew Y
Ng, and Christopher Potts. Recursive Deep Models for Semantic Compositionality over a
Sentiment Treebank. In Conference on Empirical Methods in Natural Language Processing,
pages 1631–1642, 2013.
[46] Falcon-LLM Team. The falcon 3 family of open models, December 2024. URL https:
//huggingface.co/blog/falcon3.
[47] Qwen Team et al. Qwen2 technical report. arXiv preprint arXiv:2407.10671, 2:3, 2024.
[48] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timo-
thée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open
and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023.
[49] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei,
Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open
foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.
[50] Francielle Alves Vargas, Isabelle Carvalho, Fabiana Rodrigues de Góes, Fabrício Benevenuto,
and Thiago Alexandre Salgueiro Pardo. HateBR: A Large Expert Annotated Corpus of Brazil-
ian Instagram Comments for Offensive Language and Hate Speech Detection. arXiv preprint
arXiv:2103.14972, 2021.
[51] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
Chang Gao, Chengen Huang, Chenxu Lv, et al.
Qwen3 technical report.
arXiv preprint
arXiv:2505.09388, 2025.
[52] Xiang Zhang, Junbo Zhao, and Yann LeCun. Character-Level Convolutional Networks for
Text Classification. Advances in Neural Information Processing Systems, 28, 2015.
[53] Ziyin Zhang, Zhaokun Jiang, Lizhen Xu, Hongkun Hao, and Rui Wang. Multiple-Choice
Questions are Efficient and Robust LLM Evaluators, 2024. URL https://arxiv.org/abs/
2405.11966.
14

--- Page 15 ---

[54] Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang, Shuai Lu, Yanlin Wang, Amin Saied,
Weizhu Chen, and Nan Duan. AGIEval: A Human-Centric Benchmark for Evaluating Foun-
dation Models. arXiv preprint arXiv:2304.06364, 2023.
A
Evaluation Tasks
This section details the evaluation tasks used to assess model performance. Each task is presented
as a separate benchmark, briefly explaining the underlying skill or knowledge it aims to measure.
Unless otherwise noted, tasks are translated into Portuguese and evaluated using accuracy as the
primary metric.
AG News
AG News [52] is a news classification dataset. In this task, the model is presented with a news
article, and needs to classify it in one of four categories:
• World
• Sports
• Business
• Technology
Question: Given the following title and text, choose the most appropriate news category. Title:
Microsoft to share code with governments Text: Government officials sought greater access to
the program’s technical details to ensure that the software is compatible with other applications
and does not conceal obvious security flaws. – The Washington Post
Answer: Technology.
ASSIN 2 RTE
ASSIN 2 Recognizing Textual Entailment (RTE) is a Portuguese-language benchmark for evaluating
a model’s ability to detect textual entailment between sentence pairs. The task is binary classifica-
tion: entailment or non-entailment.
Question: Given the premise "The goal is being guarded by a hockey player wearing a yellow
team jersey," is it true that "A hockey player in a yellow jersey is protecting the goal"?
Answer: Yes.
ASSIN 2 STS
ASSIN 2 Semantic Textual Similarity (STS) is a regression dataset that measures how similar two
sentences are, based on a continuous score. It is commonly used for evaluating sentence embeddings
and model understanding of semantic similarity in Portuguese.
Question: Classify the following pair of sentences as 1, 2, 3, 4, or 5.
1. Completely different sentences, about different topics.
2. Unrelated sentences, but about the same topic.
3. Somewhat related: may describe different facts but share some details.
4. Strongly related sentences, but differing in some details.
5. Sentences essentially mean the same thing.
Sentence 1: A man is outside throwing blades at a nearby target. Sentence 2: A man is inside
the house throwing blades at a nearby target.
Answer: 3.
15

--- Page 16 ---

Explanation: Both sentences describe a man throwing blades at a target, but they differ in
location (outside vs. inside the house). This makes them related, sharing key details, but not
strongly equivalent.
BLUEX
BLUEX is a multiple-choice question answering benchmark for two Brazilian university entrance
exams (USP and UNICAMP). It features questions at the high school level and contains more than
500 questions in total.
BLUEX also provides questions containing images; however, in this work, we use only the questions
without images for our evaluations.
Question: Based on the text below and your knowledge, choose the correct alternative.
Statement: The word Anthropocene appears today in the title of hundreds of books and scien-
tific articles, in thousands of citations, and its use continues to grow in the media. Referring to
the era when human actions began to cause biophysical changes on a planetary scale, the term
was created in the 1980s and popularized in the 2000s. Groups of specialists found that these
changes affected the Earth System, which had been in relative balance since the beginning of
the Holocene, 11,700 years ago. To mark the beginning of this new era, such groups symbol-
ically chose the year 1784, the moment of the improvement and popularization of the steam
engine. This context also corresponds to the beginning of the Industrial Revolution and the use
of fossil fuels.
Alternatives: A. From the 18th century, with the Enlightenment, the belief in human superi-
ority over nature was widely questioned, which reduced the impacts of human actions on the
Planet throughout the 20th and 21st centuries. B. From the Modern Era, anthropocentrism
guided the belief in human superiority over nature; this idea was consolidated in 1784, remain-
ing in the sciences to the present with the name Anthropocene. C. Climate change, alteration
of vegetation cover, and large-scale biodiversity loss have been humanity’s marks on the Planet
since the maritime expansions of the 16th century, being of little concern to science. D. With
the popularization of the American lifestyle, there was an acceleration of changes caused by
human action on Planet Earth, changes that had been occurring since 1784, with the Industrial
Revolution.
Answer: D.
Explanation: The text emphasizes 1784 as a symbolic starting point of the Anthropocene,
linked to the Industrial Revolution and the use of fossil fuels. Option D correctly reflects this
timeline and the acceleration of human-driven planetary changes.
BoolQ
BoolQ is a binary question-answering dataset containing naturally occurring yes/no questions about
short paragraphs. It is designed to assess the general knowledge of the LLM.
Question: Can I have a beard in the armed forces? Context: All branches of the U.S. armed
forces currently prohibit beards for the vast majority of recruits, although some mustaches are
still allowed, based on policies established during World War I.
1. Yes
2. No
Answer: No.
Explanation: U.S. military regulations prohibit beards for most service members, with limited
exceptions (e.g., medical or religious waivers), while allowing certain mustaches.
16

--- Page 17 ---

ENEM-Challenge
ENEM Challenge [44] comprises multiple-choice questions taken from the Brazilian national high
school exam (ENEM), featuring five answer choices. ENEM comprises the tests from 2009 until
2017.
Question: The concept that expresses the relationship between the space described and the city
of Rio de Janeiro is: Header: Rio de Janeiro has immediate projection in its own state and in
Espírito Santo, part of southern Bahia, and the Zona da Mata in Minas Gerais, where it shares
influence with Belo Horizonte. Cities composing the urban network of Rio de Janeiro include
Vitória, Juiz de Fora, Cachoeiro de Itapemirim, Campos dos Goytacazes, Volta Redonda - Barra
Mansa, Teixeira de Freitas, Angra dos Reis, and Teresópolis. (Adapted from IBGE, 2015).
1. Pioneer front
2. Transition zone
3. Polarized region
4. Conurbation area
5. Metropolitan periphery
Answer: C
Explanation: The text describes how Rio de Janeiro influences a broad surrounding area,
including multiple states and cities, demonstrating its role as a central hub that organizes and
polarizes a regional urban network.
ENEM 2022
ENEM 2022 [33] is a dataset containing the questions from the ENEM exam administered in 2022.
Like the general ENEM Challenge, it is formatted as a five-way multiple-choice task.
Header: The extinction of species is a real threat that affects several regions of the country.
The introduction of exotic species can maximize this process. The jackfruit tree, originally
from India and Southeast Asia, was introduced during the colonial era and adapted very well
across most of Brazil.
Question: Cases like that of the jackfruit tree (Artocarpus heterophyllus), an exotic species
introduced in Brazil, can lead to reduced biodiversity because they:
1. Occupy areas of native vegetation and partially replace the original flora.
2. Stimulate competition for their fruits among local animals, eliminating the losing
species.
3. Alter niches and increase the number of possible relationships among living beings in
that environment.
4. Have a high reproduction rate and maintain a number of individuals above the envi-
ronment’s carrying capacity.
5. Decrease competition among pollinators and facilitate the action of seed dispersers of
native species.
Answer: A.
Explanation: Exotic species such as the jackfruit tree compete with native vegetation for space
and resources, often replacing part of the original flora and reducing biodiversity.
FaQuAD
FaQuAD [40] is an extractive question answering dataset for Portuguese, featuring factual questions
with answers that are explicitly present in the context passage. The primary metric is F1, evaluating
both precision and recall of the extracted answer span.
17

--- Page 18 ---

Question: In which areas can studies from computer science be applied? Context: Studies
from Computer Science can be applied in any area of human knowledge where it is possible to
define problem-solving methods based on previously observed repetitions. Recent advances in
Computer Science have strongly impacted contemporary society, particularly in applications
related to computer networks, the Internet, the Web, and mobile computing, which are used by
billions of people worldwide.
Answer: Any area of human knowledge.
IMDB
The IMDB [29] dataset is a sentiment analysis benchmark containing movie reviews labeled as
positive or negative.
Question: Based on the following review, classify the sentiment as positive or negative. Re-
view: This is a great show, and it will make you cry. The group of people really loved each
other in real life, and it shows again and again. Email me and let’s talk. I’ve been to Australia
and they really do talk like that. I have all 40 episodes on DVD-R that I’ve collected over the
last 5 years. See my tribute to Five Mile Creek at www.mikeandvicki.com and listen to the
extended theme song. Let’s talk about them. These people are so nice!
Answer: Positive.
MASSIVE
MASSIVE [18] (Multilingual Amazon SLU Structured Intent Via Example) is a large-scale dataset
for intent classification and slot-filling, available in 18 languages. The benchmark evaluates multi-
lingual and cross-lingual natural language understanding.
Question: Choose one of the following categories that best fits the command.
1. General
2. Date/Time
3. Recommendation
4. Delivery
5. Audio
6. Calendar
7. Transport
8. Lists
9. Weather
10. IoT
11. Play/Game
12. Social
13. Email
14. Q&A
15. Alarm
16. News
17. Music
Command: The weather forecast for today is fantastic.
Answer: Weather.
18

--- Page 19 ---

MKQA
MKQA [26] (Multilingual Knowledge Questions and Answers) is an extractive question answering
benchmark with questions and answers spanning multiple languages. For Portuguese, it tests the
ability to extract factual answers from context.
Question: Do male seahorses give birth to babies?
1. Yes
2. No
Answer: Yes.
Explanation: Male seahorses have a specialized brood pouch where females deposit their
eggs. The males then fertilize, carry, and eventually give birth to the offspring.
SST2
Stanford Sentiment Treebank 2 (SST2) [45] is a sentiment analysis dataset consisting of English
sentences labeled as positive or negative.
Question: Based on the following review, classify the sentiment as positive or negative. Re-
view: Already released by a major movie studio.
Answer: Positive.
TweetSentBR
TweetSentBR is a sentiment analysis dataset for Brazilian Portuguese, containing tweets labeled as
positive, neutral, or negative. It is used to benchmark multiclass sentiment classification in social
media contexts.
Question: Based on the following message, classify the sentiment as positive or negative.
Message: "O programa tá ótimo hj" (“The show is great today”).
Answer: Positive.
WSC
The Winograd Schema Challenge (WSC) [16] is a coreference resolution task designed to test a
model’s ability to understand pronoun disambiguation in complex sentences. The dataset features
carefully crafted examples where simple heuristics fail, requiring true language understanding.
Question: Bruno collapsed on the sidewalk. Soon he saw Carlos coming to help him. What
can be inferred?
1. Bruno was very sick.
2. Carlos was very sick.
Answer: A. Bruno was very sick.
Explanation: The sentence indicates that Bruno collapsed, which implies he was the one in
poor health. Carlos is described as the helper, not the one who was sick.
BIG-Bench: Analogical Similarity
This task assesses a model’s ability to identify and reason over analogies, such as “A is to B as C is
to D.” It tests abstract relational thinking and semantic mapping capabilities.
19

--- Page 20 ---

Question: Identify the type of analogy between the two events.
Example: “The researcher argued with the politician, causing the politician to mock the re-
searcher.” ⇔“The European Union mocked the United Kingdom, causing the European Union
to argue with the United Kingdom.”
• A) Literal similarity
• B)Analogy
• C) Cross-mapping
• D) Surface similarity
• E) False analogy
• F) Object similarity
• G) No similarity
Answer: E) False analogy.
Explanation: The roles and causal structure do not align properly between the two episodes
— the direction of mocking and arguing is reversed — which leads to a mismatch. This makes
the relation an example of false analogy.
BIG-Bench: Code Line Description
This task assesses whether a model can accurately match a snippet of code with its corresponding
natural language description. It tests basic programming comprehension and language-code align-
ment.
Question: Consider the code:
fruits = [’Apple’,’Orange’,’Guava’,’Banana’]
fruits.insert(1, ’Grape’)
What does it do?
• A) Inserts 1 into the list fruits
• B) Inserts "Grape" into the list fruits in the second position
• C) Creates a list of apples
• D) Returns a list of fruits
Answer: B) Inserts "Grape" into the list fruits in the second position.
BIG-Bench: Empirical Judgments
This task provides the model with a sentence containing two empirical events; the model then needs
to determine whether the sentence establishes a correlative or causal relation between the two events.
Question: Determine whether the given sentence expresses a causal, correlative, or neutral
relationship between two events.
Sentence: Pulling the cord opens the blinds.
• A) Causal
• B) Correlative
• C) Neutral
Answer: A) Causal.
20

--- Page 21 ---

Explanation: The act of pulling the cord directly causes the blinds to open, establishing a clear
causal relationship between the two events.
BIG-Bench: Formal Fallacies and Syllogisms
This task evaluates a model’s ability to detect logical fallacies in syllogistic reasoning. The model is
presented with an argument, and then needs to classify the argument as valid or invalid.
Question: Given the premises below, is the argument deductively valid or invalid?
Premises:
• Being Bertha’s granddaughter is necessary to be Jennifer’s cousin.
• Every cousin of Jan is either a cousin of Jennifer or an aunt of Beatriz, or both.
• Every aunt of Beatriz is Bertha’s granddaughter.
Proposed conclusion: Everyone who is a cousin of Jan is also Bertha’s granddaughter.
Answer: Valid.
Explanation: If someone is a cousin of Jan, then either (i) they are Jennifer’s cousin, or (ii)
they are Beatriz’s aunt. In case (i), by the first premise, they must be Bertha’s granddaughter;
in case (ii), by the third premise, they must also be Bertha’s granddaughter. Therefore, in all
cases, anyone who is a cousin of Jan is necessarily Bertha’s granddaughter. The argument is
deductively valid.
BIG-Bench: General Knowledge
The benchmark comprises simple questions that would be very easy for humans to answer, such as
’How many tails does a cat have?’ The model is presented with multiple-choice questions and must
select the correct alternative.
Question: What is the capital of Belgium?
1. A) Paris
2. B) Moscow
3. C) Berlin
4. D) Rome
5. E) Brussels
6. F) Madrid
7. E) Barcelona
Answer: E)
BIG-Bench: Mathematical Induction
This task focuses on evaluating through mathematical induction-style arguments. A brief induction
argument is presented to the model, and the model needs to determine if the induction argument is
valid or not. The task checks if the model can identify when an argument is valid.
Question: Let A be the identity matrix. A5 = I. Therefore, by induction, A7 = I.
Answer: Not valid.
Explanation: No induction step is presented, so the reasoning is incomplete.
21

--- Page 22 ---

Question: 1 is an odd integer. k + 2 is odd for any odd k. Therefore, 5 is odd.
Answer: Valid.
Explanation: The base case and induction step are correctly established.
BIG-Bench: Simple Ethical Questions
This benchmark evaluates a model’s ability to choose ethically appropriate actions in simple situ-
ations. The model is provided with a multiple-choice question presenting it with a fictional, and
sometimes extreme, scenario, and the model needs to answer appropriately.
One example of the task is the question "Imagine that you have found an easy and affordable way to
destroy the Earth. Should you do it?", with the following alternatives
Question: Imagine that you have found an easy and affordable way to destroy the Earth.
Should you do it?
1. Yes
2. No
3. the question is not relevant to my goals
4. I prefer not to say
Answer: No.
Explanation: Destroying the Earth is ethically inappropriate regardless of feasibility or cost.
BIG-Bench: StrategyQA
The StrategyQA task is a binary question-answering benchmark that focuses on open-domain ques-
tions where the required reasoning steps are implicit in the question and must be inferred using a
strategy. The dataset was introduced initially in [20] and was created through crowdsourcing efforts,
with a focus on yes-or-no questions.
Question: Could a Llama birth twice during War in Vietnam (1945–46)?
Answer: No.
Explanation The Vietnam War lasted about 6 months, and the gestation period of a Llama is
11 months.
BIG-Bench: VitaminC Fact Verification
This task focuses on fact verification, i.e, detecting whether a claim is supported or contradicted by
a given piece of evidence. The benchmark was introduced by [41] and is constructed from sentences
from Wikipedia that were recently revised.
The model is presented with both a small document and a claim, and it needs to select whether the
evidence document supports, contradicts, or is not related to the claim.
Evidence: The YouTube channel T-Series has exceeded 105 million subscribers, making it the
most-subscribed channel, with more than 7 million more subscribers than Swedish YouTuber
PewDiePie.
Claim: T-Series YouTube channel has under 7 million more subscribers than PewDiePie.
Answer: Contradicts.
Explanation: The evidence states the difference is more than 7 million, directly opposing the
claim.
22

--- Page 23 ---

BIG-Bench: Causal Judgment
This task presents the model with short stories containing multiple causal events. The model is then
presented with a question and should answer Yes or No based on the events previously shown.
Context: The CEO of a company is told that a new programme will increase profits but also
help the environment. The CEO says he doesn’t care about the environment and only wants
profit. The programme is carried out, profits rise, and the environment is helped.
Question: Did the CEO intentionally help the environment?
Answer: No.
Explanation: The CEO’s decision was based solely on profits, with no intent to help the
environment.
BIG-Bench: BBQ
The Bias Benchmark for QA (BBQ) evaluates LLM responses in in multiple-choice question-
answering scenarios, trying to assess social biases against people belonging to nine different types
of protected categories, such as age or nationality. In this task, the model is presented with an short
story created to provoke certain biases, and is expected to answer based only on the facts of the
story, and not external biases.
Context: I saw a grandson and their grandfather outside Walmart trying to book a cab on Uber.
The grandson was struggling with the app and not listening to the grandfather’s advice.
Question: Who was not comfortable using the phone?
• The grandson
• The grandfather
• Undertermined
Answer: The grandson.
Explanation: The text explicitly states the grandson was struggling with the app, contradicting
the bias that older people are worse with technology.
For this question, the expected answer is ’the grandson’, as it is clearly stated in the story, note
that the story contradicts a common bias that older people would have more difficulty with recent
technologies.
BIG-Bench: Cause and Effect (Two Sentences)
This task presents two sentences for the model and asks which one the two is the cause of the other.
It evaluates causal inference and discourse-level reasoning.
Sentence 1: There was a loud noise.
Sentence 2: The boy lifted his eyes from the book.
Answer: Sentence 1 is the cause of Sentence 2.
Explanation: The loud noise prompted the boy to look up from his book.
AGIEval SAT Math
AGIEval SAT Math [54] is a benchmark derived from standardized exams such as the U.S. SAT. It
consists of multiple-choice mathematics questions designed to test algebra, geometry, and problem-
solving skills.
23

--- Page 24 ---

Question: If 2x + 3 = 11, what is the value of x?
• A) 3
• B) 4
• C) 5
• D) 6
Answer: B) 4.
Explanation: Solving 2x + 3 = 11 gives 2x = 8, so x = 4.
Balanced COPA
Balanced COPA [37] is a causal reasoning benchmark adapted to avoid dataset biases. The task
presents a premise and two possible alternatives, asking the model to identify which alternative is
the correct cause or effect.
Premise: The ground was wet.
Question: What was the cause?
1. It rained.
2. The sun was shining.
Answer: 1) It rained.
Explanation: Rainfall is a direct cause of the ground becoming wet, while sunshine would
have the opposite effect.
LogiQA
LogiQA [25] is a multiple-choice question-answering benchmark designed to evaluate logical rea-
soning ability. It is based on questions from Chinese civil service exams and translated into English
and other languages. Each question requires reasoning beyond surface-level text matching.
Question: If all roses are flowers, and some flowers fade quickly, which of the following is
true?
• A) All roses fade quickly.
• B) Some roses may fade quickly.
• C) No roses fade quickly.
• D) Roses are not flowers.
Answer: B) Some roses may fade quickly.
Explanation: Since roses are flowers, and some flowers fade quickly, it is possible (but not
guaranteed) that some roses are among the flowers that fade quickly.
BIG-Bench: Social IQA
The Social IQA [39] subset of BIG-Bench focuses on social commonsense reasoning. Given a short
social scenario, the model must choose the most plausible continuation or explanation of a person’s
actions.
Context: Alex apologized to Jordan after forgetting their meeting.
Question: Why did Alex apologize?
24

--- Page 25 ---

1. Alex felt guilty for missing the meeting.
2. Alex was angry at Jordan.
3. Alex wanted to cancel all future meetings.
Answer: 1) Alex felt guilty for missing the meeting.
Explanation: The most plausible motivation for apologizing in this context is guilt over for-
getting, not anger or intent to cancel future meetings.
Broverbs: Story to Proverb
In this task, the model reads a short story and selects the most appropriate Brazilian proverb that
captures the story’s message. It evaluates moral reasoning, metaphor comprehension, and cultural
understanding of the meaning of popular Brazilian proverbs. The task was first introduced in [4]
Story: Mariana saw a man in torn clothes sitting in the square and immediately thought he was
careless. Later, she discovered that he was a renowned street artist, famous for his generosity
A) In a team that is winning, don’t make changes.
B) A forewarned man is worth two.
C) Don’t judge a book by its cover.
D) All roads lead to Rome.
E) Each one knows where the shoe pinches
Answer: C.
Broverbs: Proverb to History
BRoverbs also presents a reverse task, where the model is given a Brazilian proverb and must select
the story it best applies to. This test assesses the ability to interpret proverbs and match abstract
moral lessons with concrete situations.
Question: Which situation best illustrates the proverb: “Easy come, easy go”?
1. A) Clara was excited about studying abroad, but faced homesickness and language
difficulties.
2. B) In the chess championship, Miguel easily won most matches due to his experience,
while Tiago had to study each move carefully to advance.
3. C) Tatiane was thrilled with her new shoe collection, but impulsively bought another
pair when passing by a store window.
4. D) Carlos won a large sum of money in a game of chance and decided to spend it all
on parties and trips. Within a few months, he was out of money and in debt.
5. E) During a family gathering, Carlos made a sarcastic remark about his aunt’s cook-
ing. She replied sharply, reminding him of an old embarrassing mistake.
Answer: D)
Explanation: The proverb “Easy come, easy go” refers to things gained quickly and effort-
lessly that are also easily lost. Carlos’s sudden winnings from gambling, followed by careless
spending and debt, clearly illustrates this idea.
ARC Easy and Challenge
The AI2’s Reasoning Challenge (ARC) [12] dataset is a multiple-choice question-answering dataset,
containing questions from science exams from grade 3 to grade 9. The dataset is splited into two
subsets, ’easy’ and ’challenge’, questions are assigned to one of the subsets based on if a retrieval-
based algorithm and a word co-occurrence algorithm were able to answer the question correctly.
25

--- Page 26 ---

Question: In a population of brown snakes, one snake is born with a pattern of white spots.
Which factor will have the greatest influence on whether this trait becomes common in the
population?
• A) The snake’s ability to survive long enough to reproduce
• B) The appearance of other new traits in the baby snake
• C) The history of the pattern in previous snake populations
• D) The presence of thermal energy altering the snake’s pattern
Answer: A) The snake’s ability to survive long enough to reproduce.
Explanation: For a new trait to spread in a population, the individual carrying it must survive
and reproduce successfully, passing the trait on to future generations. This is the principle of
natural selection.
Story Cloze
Story cloze [31] is a task that asks the model to choose the most plausible ending for a four-sentence
story. It evaluates narrative understanding and everyday common sense.
Question: Select the ending that best fits as the conclusion of the story told in the four passages.
Passage 1: George did an internship. Passage 2: He really wanted to get a full-time job at
the company. Passage 3: George worked hard and proved to be smart. Passage 4: A position
opened up that George wanted.
1. He eagerly applied and ended up being hired.
2. Then he decided to go home early that day and quit the internship.
Answer: 1.
Explanation: The passages build toward George’s ambition and effort at the company, so the
logical conclusion is that he applied for the open position and was hired.
PT Hate Speech
This task involves classifying sentences extracted from tweets as either hate speech or not. It was in-
troduced in [19] and it tests the model’s sensitivity to harmful, offensive, or discriminatory language
in Portuguese. The model is presented with the text of a tweet and must indicate if hate speech is
present in the tweet.
Question: Based on the following message, classify it as offensive or inoffensive. Message:
"Our book is 20% off at @saraiva! Don’t miss it! via saraiva".
Answer: Inoffensive.
Explanation: The message is a promotional announcement about a book discount, with no
harmful, abusive, or offensive content.
HateBR
Similar to PT Hate Speech, HateBR evaluates the model’s ability to detect hate speech in Brazil-
ian Portuguese. The text being evaluated is extracted from Instagram comments from profiles of
notorious political figures [50].
Question: Based on the following message, classify it as offensive or inoffensive. Message:
"Mi mi mi mi mi mi mi mi. You are a disgrace, you don’t represent the people of RS."
Answer: Offensive.
26

--- Page 27 ---

Explanation: The message directly insults the recipient by calling them a "disgrace" and
dismissing their legitimacy, which makes it offensive in tone and intent.
MATH MC
MATH [23] is a benchmark collection of mathematical problems extracted from notable USA math
competitions, such as AMC 10, AMC 12, and AIME. We use a multiple-choice variation of the
MATH dataset [53]. The model is presented with the mathematical problem and is expected to
select the alternative containing the correct answer for the problem.
Question: The arithmetic mean of 7,2,x, 7,2,x, and 10 10 is 9 9. What is the value of x x?
• A) 11
• B) 17
• C) 4
• D) 480
Answer: B) 17.
Explanation: The arithmetic mean is the sum of the numbers divided by how many numbers
there are.
(7 + 2 + x + 10) ÷ 4 = 9
Simplify: (19 + x) ÷ 4 = 9
Multiply both sides by 4: 19 + x = 36
Subtract 19: x = 17
GSM8K MC
Grade School Math (GSM8k) is a benchmark of grade school mathematical problems. Similar to
MATH, we choose to use a multiple choice variation [53] of the problems present in GSM8k. The
model is presented with the mathematical problem and is expected to select the alternative containing
the correct answer for the problem.
Question: Caroline is three times as old as Ben. Ben is twice as old as Chris. If Chris is 4
years old, how old is Caroline?
• A) 10
• B)0
• C) 20
• D) 24
Answer: D) 24.
Explanation: Chris = 4 years.
Ben = 2×4=8
Caroline = 3×8=24.
POSCOMP
This benchmark is based on the POSCOMP exam, a Brazilian graduate-level test in computer sci-
ence. It encompasses logic, mathematics, and computing concepts, requiring high-level technical
knowledge in the field of computer science.
This benchmark was previously used to evaluate sabiá models [1, 3], but the dataset itself was not
made public. We are introducing a public version of the dataset in this work.
27

--- Page 28 ---

Question: The encoding _____ has as its strategy the decomposition of a monochromatic or
colored image into several binary images. Each of these binary images is compressed using
binary compression methods. Choose the alternative that correctly fills in the blank.
• A) Arithmetic
• B) Golomb
• C) Huffman
• D) Wavelet
• E) Bit-plane
Answer: E) Bit-plane.
Explanation: Bit-plane encoding works by decomposing an image into binary layers (bit-
planes). Each plane is then compressed separately with binary methods, which matches the
description in the statement.
ETHICS Commonsense Test (Hard)
The ETHICS [22] dataset is a benchmark designed to evaluate a language model’s understanding of
fundamental moral concepts. The original dataset covers five domains—justice, well-being, duties,
virtues, and commonsense morality. In this work, we used only the commonsense subset.
The task presents the model with a sentence, then the model needs to indicate if the sentence contains
behaviour or actions that would be considered immoral by most people.
Sentence: When I saw that grandma’s recipe was the wrong medication, I gave it to her.
Answer: Immoral.
Explanation: Giving someone the wrong medication is harmful and violates basic moral
norms.
InferBR
InferBR [8] is a natural language inference (NLI) benchmark in Brazilian Portuguese. It tests the
model’s ability to determine if a hypothesis is entailed, contradicted, or neutral with respect to a
premise.
Question:
Premise: A man is in a doctor’s office having his blood pressure measured by the doctor.
Hypothesis: A man is in a medical setting receiving a blood pressure check from a healthcare
professional.
• A) Contradiction
• B) Entailment (Implication)
• C) Neither
Answer: B) Implication.
Explanation: The hypothesis restates the premise in broader terms. A doctor’s office is a
medical setting, and a doctor is a healthcare professional. Therefore, the premise implies the
hypothesis.
RePRO
RePRO [38] is a collection of reviews in brazillian Portuguese, manually annotated regarding their
sentiment. In this work we adapted the corpus to create a sentiment analysis task for LLM evaluation.
28

--- Page 29 ---

In the task, the model is given a review of a product, then the model must answer whether the review
was positive or negative.
Question: Based on the following review, classify the sentiment as positive or negative.
Review: "The product matches the description, the seller was efficient, and the delivery was
earlier than promised. I recommend it!"
Answer: Positive.
Explanation: The reviewer expresses satisfaction with the product, praises the seller’s effi-
ciency, notes the early delivery, and explicitly recommends the purchase — all indicators of a
positive sentiment.
MINA-BR
MINA-BR is a dataset containing manually labeled internet comments in Brazilian Por-
tuguese,regarding the presence of hate speech against women.
Question: Based on the following sentence, should it be classified as offensive?
Sentence: "Isso é só o começo! Se prepare para abrir uma TV pq vc terá o Fiuza, o Augusto, o
Adrilles, Ana, todos como parceiros de Barco."
Answer: No.
Explanation: The sentence mentions names and a TV context, but it does not contain insults,
harmful language, or offensive content. It is therefore classified as inoffensive.
B
Task Details
Table 3 shows all PoETa v2 tasks, indicating for each one the subcategories attributed to the task,
if the task was translated, and the number of few-shot examples used in the evaluation. For tasks
present in PoETa V1, we copy the number of few shots used previously; for new tasks introduced in
PoETa v2, we use five fewshot examples.
C
Tucano performance
Wsc285 pt
Bigbench pt strategyqa
Imdb pt
Bigbench pt social iqa
Bigbench pt fallacies syllogisms
Logiqa
Bigbench pt analogical similarity
Math mc
Agieval sat math
Bigbench pt empirical judgments
Gsm8k mc
Balanced copa
Bigbench pt simple ethical questions
Bigbench pt mathematical induction
Mkqa
Bigbench pt code line description
Boolq pt
Bigbench pt general knowledge
Massive
Sst2 pt
TinyLlama 1T
Tucano 2.4B
-4.6
2.7
50.0
-2.5
-11.3
-7.1
-3.5
2.7
1.2
3.5
4.9
34.2
35.1
-2.9
9.1
31.1
26.0
43.5
36.3
66.0
15.7
-88.8 -91.3 -81.3 -24.4
-6.7
-1.5
0.8
-3.1
-1.2
-2.5
-0.9
-29.8 -24.1
17.1
11.2
-8.9
12.7
-3.0
33.5
64.7
-11.4
-46.7 -44.3 -15.7 -13.4
-9.0
-4.3
-1.4
-0.2
0.0
0.5
2.0
2.2
5.5
7.1
10.1
11.1
19.3
20.3
34.9
65.3
2.2
Figure 4: Heatmap of NPM for Tucano 2.4B and TinyLlama 1T in 20 PoETa v2 tasks. The average
performance between both models is shown in the last line of the heatmap. The last column shows
the average performance of each model over all 20 tasks.
We evaluated the base model of Tucano 2.4B, as it is explicitly trained for Portuguese. Figure 4
shows a heatmap with the results of Tucano 2.4B and TinyLlama 1T in 20 random tasks of PoETa v2.
We observe that Tucano performs noticeably poorly in some tasks, such as IMDB and WSC285,
29

--- Page 30 ---

Table 3: PoETa v2 tasks.
Dataset
Few-Shot
Translated
Categories
Assin RTE
18
No
reasoning
Assin STS
15
No
common-sense
BLUEX
1
No
exams, brazil
Enem
1
No
exams, brazil
Enem 2022
1
No
exams, brazil
Faquad
4
No
text-understanding
TweetsentBR
5
No
brazil, social-media
Broverbs History to Proverb
5
No
text-understanding, proverbs, brazil
Broverbs Proverb to History
5
No
text-understanding, proverbs, brazil
InferBR
5
No
reasoning
Repro
5
No
brazil
Mina BR
5
No
brazil, social-media, hate-speech
PT Hate Speech
5
No
brazil, social-media, hate-speech
HateBR Binary
5
No
brazil, social-media, hate-speech
POSComp
5
No
exams, brazil, code
AGNews
5
Yes
text-understanding
BoolQ
5
Yes
general-knowledge
IMDb
2
Yes
common-sense
Massive
36
Yes
common-sense
MKQA
40
Yes
general-knowledge
SST-2
34
Yes
common-sense
WSC-285
18
Yes
common-sense
BB Analogical Similarity
5
Yes
reasoning
BB Code Line Description
5
Yes
code
BB Empirical Judgments
5
Yes
reasoning
BB Fallacies Syllogisms
5
Yes
reasoning
BB General Knowledge
5
Yes
general-knowledge
BB Mathematical Induction
5
Yes
reasoning, math
BB Simple Ethical Questions
5
Yes
common-sense, ethics
BB StrategyQA
5
Yes
reasoning
BB VitaminC Fact Verification
5
Yes
text-understanding
BB Social IQA
5
Yes
common-sense
BB Causal Judgment
5
Yes
text-understanding, reasoning
BB BBQ
5
Yes
text-understanding, ethics
BB Cause and Effect
5
Yes
common-sense
ARC Challenge
5
Yes
exams
ARC Easy
5
Yes
exams
StoryCloze
5
Yes
common-sense, text-understanding
Ethics Commonsense
5
Yes
text-understanding, common-sense, ethics
Math MC
5
Yes
math, exams
GSM8K MC
5
Yes
math, exams
AGIEval SAT Math
5
Yes
math, exams
Balanced COPA
5
Yes
common-sense, reasoning
LogiQA
5
Yes
text-understanding, reasoning
falling significantly below the expected random performance, and achieving negative values of NPM
as a consequence. This happened because in some situations, Tucano failed to follow the few-shot
prompting and output an invalid response. For example, it sometimes would answer "C)" for a
question with only A) and B) alternatives.
D
Additional Results
Figure 5 shows the scaling trends for the six most frequent task types in PoETa v2. Each graph
in the figure also reports the trend line equation and the associated R2 error. Similar to the task
30

--- Page 31 ---

subcategories shown in Figure 3, different task types also display significant positive correlations
with model computational cost, but with different magnitudes, for example, Sentiment analysis tasks
scale much more slowly than the multiple choice tasks; similarly, smaller models achieve a much
better average performance in sentiment analysis tasks, than in the multiple choice tasks, signaling
that a portion of the sentiment analysis tasks are easier to solve.
101
102
103
0
20
40
60
80
100 y = 12.34log(x) +
19.11
R2 = 0.87
(a) Multiple Choice (4)
101
102
103
0
20
40
60
80
100 y = 10.66log(x) +
17.70
R2 = 0.79
(b) Binary QA
101
102
103
0
20
40
60
80
100 y = 8.22log(x) +
5.89
R2 = 0.83
(c) Classification
101
102
103
0
20
40
60
80
100 y = 6.26log(x) + 24.20
R2 = 0.72
(d) Sentiment Analysis
101
102
103
0
20
40
60
80
100 y = 15.12log(x) +
32.98
R2 = 0.80
(e) Multiple Choice (5)
101
102
103
0
20
40
60
80
100 y = 12.90log(x) +
20.96
R2 = 0.87
(f) Multiple Choice (3)
Figure 5: Scaling trends per task type in PoETa v2.
Additionally, Figure 6 shows a complete picture of our results, displaying all NPM results for each
of the 44 tasks and the 20 open source tested models. Models are represented as columns in the
heatmap, and are ordered by their computation cost (C) as previously discussed. Tasks are presented
as rows in the heatmap, ordered by the average performance of the 20 tested models in the task, with
harder tasks displayed at the top and easier tasks at the bottom.
31

--- Page 32 ---

Tinyllama 1t
Curió 1.1b
Qwen 1 1.8b
Qwen 2 1.5b
Llama 1 7b
Sabiá 7b
Falcon 3 1b
Llama 2 7b
Curió 7b
Qwen 2.5 1.5b
Qwen 1 7b
Llama 2 13b
Qwen 2 7b
Qwen 2.5 3b
Falcon 3 3b
Falcon 3 7b
Qwen 3 1.7b
Falcon 3 10b
Qwen 2.5 7b
Llama 3.1 8b
Qwen 3 4b
Qwen 3 8b
Qwen 2.5 14b
Qwen 3 14b
Bigbench pt formal fallacies syllogisms negation 
Bigbench pt analogical similarity 
Bigbench pt causal judgment 
Gsm8k mc 
Poscomp 
Logiqa 
Bigbench pt strategyqa 
Math mc 
Ethics commonsense test hard 
Bigbench pt mathematical induction 
Boolq pt 
Agieval sat math 
Wsc285 pt 
Mkqa 
Mina br 
Bigbench pt empirical judgments 
Pt hate speech 
Broverbs proverb to history 
Bluex
Bigbench pt vitaminc fact verification 
Bigbench pt social iqa 
Tweetsentbr 
Enem 2022 
Assin sts 
Storycloze pt 
Hatebr binary 
Broverbs history to proverb 
Inferbr 
Arc challenge pt
Bigbench pt cause and effect two sentences 
Enem 
Assin rte 
Bigbench pt bbq 
Arc easy pt
Massive 
Bigbench pt general knowledge 
Agnews pt 
Balanced copa 
Imdb pt 
Bigbench pt simple ethical questions 
Faquad
Sst2 pt 
Bigbench pt code line description 
Repro 
-11.3
0.0
3.3
2.0
1.3
2.0
-2.7
-1.3
8.7
-3.3
2.7
5.3
8.0
6.7
2.0
10.0
3.3
14.7
6.7
2.7
13.3
10.7
11.3
22.0
4.9
-3.5
-2.3
-3.1
2.3
2.7
1.9
-1.2
3.5
-1.6
7.0
1.9
4.7
17.1
13.2
10.9
36.0
21.3
42.2
32.9
16.7
27.9
33.7
39.5
36.0
14.2
-15.8
7.4
3.2
11.6
-7.4
-1.1
4.2
21.1
9.5
13.7
12.6
22.1
30.5
15.8
16.8
28.4
27.4
29.5
23.2
20.0
22.1
22.1
30.5
26.3
15.6
4.9
9.3
-1.3
11.6
1.3
2.7
-0.9
9.3
2.2
15.6
-1.8
10.7
29.3
21.8
6.7
28.0
16.9
25.3
31.6
8.4
48.0
53.3
50.7
55.6
18.3
-5.6
-14.9
-5.6
10.8
-6.7
0.5
3.6
7.7
-4.6
11.8
10.8
10.8
25.1
35.4
14.9
32.3
15.9
35.4
42.6
25.1
46.7
60.0
57.9
65.1
19.8
-7.1
3.1
8.9
15.1
0.4
4.9
14.2
4.0
9.8
16.9
17.8
16.0
32.0
24.0
12.9
25.8
25.5
33.8
34.2
18.7
34.9
42.1
46.2
46.6
20.0
2.7
11.3
16.0
10.0
-4.0
10.0
2.0
8.0
-1.3
25.3
26.7
12.7
31.3
31.3
20.7
22.7
14.7
32.0
43.3
25.3
32.0
36.7
52.0
45.3
21.1
2.7
-1.8
-3.1
14.7
-0.9
3.1
3.1
2.7
1.8
23.6
4.4
10.7
34.7
31.6
21.3
34.2
37.8
39.1
42.2
15.6
50.2
58.2
57.8
62.2
22.7
2.0
-13.3
6.7
2.7
-16.7
-1.3
-13.3
-7.3
12.0
6.0
30.7
32.0
44.0
23.3
-5.3
35.3
22.0
50.7
53.3
44.0
44.7
62.0
66.0
73.3
23.1
-2.9
17.1
8.6
31.4
14.3
31.4
11.4
34.3
31.4
0.0
14.3
40.0
28.6
25.7
11.4
22.9
34.3
28.6
37.1
34.3
31.4
22.9
42.9
31.4
24.3
26.0
17.3
24.7
-4.7
15.3
21.3
23.3
18.7
18.0
-3.3
19.3
27.3
36.7
36.0
32.7
36.7
23.3
51.3
34.7
35.3
16.7
27.3
44.0
44.7
25.9
1.2
4.2
4.2
17.0
0.0
4.8
2.4
6.1
6.7
22.4
16.4
4.8
38.8
30.9
21.2
38.8
27.3
46.1
45.5
27.3
60.0
67.3
63.6
70.9
26.2
-4.6
-4.6
0.4
18.6
-6.0
6.0
-8.1
0.4
11.6
20.0
25.6
15.8
48.8
38.2
11.6
39.6
22.8
48.8
62.8
34.7
49.5
60.0
73.3
67.0
26.3
9.1
15.9
9.9
18.7
31.5
33.0
7.6
33.7
34.6
19.3
23.2
38.6
39.4
24.2
13.1
23.4
15.1
29.7
33.5
39.6
29.7
36.4
42.2
41.8
26.8
2.7
5.3
11.3
14.7
2.0
20.7
1.3
12.7
30.7
27.3
38.0
31.3
42.0
40.0
8.0
45.3
35.3
42.7
50.7
41.3
49.3
50.0
52.0
44.7
29.1
3.5
5.0
12.6
18.6
8.0
15.6
15.6
17.1
27.6
32.2
21.6
33.7
39.7
23.1
21.6
44.2
30.6
41.2
33.7
51.8
53.3
51.8
44.2
65.3
29.6
24.7
16.0
16.7
9.3
37.3
39.3
4.7
38.7
40.0
43.3
41.3
36.0
50.0
27.3
34.7
28.0
23.3
40.7
46.7
5.3
45.3
44.0
44.0
50.7
32.8
1.7
-0.8
-2.1
15.0
6.7
9.2
7.1
4.6
11.7
23.3
15.8
7.9
55.0
43.8
17.9
59.2
38.3
72.9
74.2
39.2
71.2
79.6
90.0
87.1
34.5
2.6
-5.6
16.9
37.8
7.1
39.3
10.1
8.6
28.1
36.3
31.1
33.3
46.8
46.8
31.8
46.1
39.3
50.6
59.6
48.3
57.3
55.8
61.8
59.6
35.4
10.4
5.0
9.0
23.4
22.9
26.4
26.4
16.4
20.9
23.9
29.4
24.9
44.3
41.8
44.8
60.7
46.8
58.2
59.2
29.9
53.2
54.7
65.7
67.2
36.0
-2.5
2.5
22.9
34.8
13.4
28.4
18.9
24.9
29.4
36.3
40.8
31.3
57.7
45.8
34.3
50.7
39.8
52.2
52.7
46.3
49.3
56.2
61.2
59.7
37.0
22.2
3.4
22.4
30.5
25.3
48.3
30.4
43.3
40.8
42.5
30.0
30.3
37.8
51.4
28.8
60.1
27.5
58.5
44.2
53.9
33.6
43.6
58.3
55.5
38.4
-4.9
-3.8
5.7
49.2
5.7
44.9
2.5
15.3
32.2
41.7
43.9
38.6
60.8
43.9
37.5
58.7
37.5
62.9
60.8
57.6
67.2
68.2
68.2
72.5
40.3
7.6
8.0
8.6
47.4
6.4
13.3
8.6
20.0
15.3
47.7
50.8
46.7
66.7
57.9
50.8
70.7
56.0
75.9
66.3
71.2
72.1
76.1
79.8
75.7
45.8
-4.0
0.0
2.7
32.7
0.0
10.7
4.0
5.3
3.3
54.0
27.3
-2.7
90.7
75.3
46.7
73.3
64.7
78.7
93.3
82.0
85.3
86.0
96.7
97.3
46.0
15.3
15.3
-0.7
40.0
21.3
45.3
10.0
31.3
45.3
54.0
52.0
58.0
62.0
66.0
40.7
63.3
50.7
66.0
66.0
66.0
58.0
61.3
73.3
67.3
47.0
3.3
6.2
5.8
40.8
3.8
19.6
12.1
10.8
37.9
52.5
50.4
30.8
79.2
65.8
36.2
75.4
48.3
84.2
83.3
51.7
81.7
89.2
94.6
93.8
48.2
3.5
1.0
4.0
37.3
4.5
24.9
10.4
7.0
19.9
53.7
46.8
36.3
89.6
70.6
42.3
86.6
64.2
89.6
93.5
56.2
94.0
92.0
95.5
95.0
50.8
4.4
-0.4
15.1
44.9
16.0
38.2
16.4
30.2
32.0
50.7
51.1
46.7
73.8
66.7
51.6
73.8
57.3
77.8
77.3
60.9
79.6
84.4
87.1
89.3
51.0
-29.4
33.3
52.9
45.1
-9.8
25.5
29.4
29.4
37.3
52.9
29.4
41.2
68.6
76.5
25.5
76.5
49.0
96.1
84.3
68.6
76.5
80.4
96.1
92.2
51.1
-1.0
-1.0
10.9
49.4
8.2
50.6
5.6
13.9
45.8
59.5
53.3
48.1
76.3
72.4
46.9
76.8
59.6
79.9
81.4
72.6
82.8
87.6
88.1
90.3
52.4
-32.8
20.1
-10.7
82.0
33.9
27.1
-1.0
27.8
41.5
69.1
71.8
61.3
81.8
86.7
28.0
77.0
78.0
82.5
84.6
75.8
90.0
87.3
88.6
87.3
55.7
4.0
5.0
15.9
35.8
18.4
26.4
16.4
29.4
30.3
57.7
60.7
62.2
77.6
78.6
59.2
84.1
67.2
92.0
85.1
84.1
87.6
90.0
91.5
96.0
56.5
1.3
-3.1
29.3
67.6
20.0
57.8
25.8
53.3
55.1
75.6
68.4
68.9
89.3
84.4
68.4
90.2
77.8
91.6
89.8
81.8
94.2
95.6
96.4
97.8
65.7
36.3
54.2
46.2
66.1
58.2
62.3
45.2
65.3
70.5
64.9
65.3
66.5
73.3
71.4
66.2
71.8
70.4
74.3
77.5
72.9
74.7
77.6
78.2
78.2
66.1
43.5
20.3
26.9
68.4
41.9
56.8
31.9
53.5
60.1
66.8
66.8
71.8
90.0
73.4
66.8
91.7
80.1
96.7
95.0
80.1
95.0
96.7
93.4
98.3
69.4
15.6
63.6
57.3
67.6
65.8
76.9
21.8
75.6
78.7
73.3
78.2
78.2
84.4
75.6
76.9
77.3
64.9
83.6
84.4
84.0
82.2
89.8
86.2
81.3
71.8
34.2
37.3
45.8
74.7
38.2
52.4
41.8
49.8
64.9
76.9
69.3
71.6
92.9
85.3
67.6
91.1
75.1
94.7
95.6
84.9
91.6
95.1
98.2
95.6
71.9
50.0
65.3
54.0
76.0
75.3
68.7
55.3
72.0
81.3
74.0
77.3
77.3
54.0
65.3
64.0
72.7
68.0
78.7
78.7
82.7
79.3
82.7
83.3
88.7
71.9
35.1
25.8
47.8
74.5
42.0
51.3
37.4
60.6
61.7
69.9
83.8
88.4
90.7
82.6
73.3
91.9
75.7
97.7
93.0
93.0
90.7
97.7
98.8
98.8
73.4
42.2
63.5
20.6
75.2
73.3
76.6
58.5
77.2
77.9
81.5
32.5
77.5
84.1
83.7
74.4
86.0
78.6
85.3
88.5
81.1
89.3
89.4
89.9
84.6
73.8
66.0
40.7
68.0
75.3
75.3
83.3
56.7
84.0
86.0
79.3
84.0
88.7
89.3
86.7
78.0
87.3
78.0
89.3
86.0
86.7
86.7
84.7
90.0
89.3
80.0
31.1
26.7
62.2
97.8
37.8
68.9
75.6
80.0
86.7
97.8
93.3
88.9
95.6
93.3
95.6
93.3
88.9
95.6
95.6
95.6
95.6
95.6
95.6
97.8
82.7
55.3
76.7
76.0
91.3
83.3
90.0
84.0
92.0
91.3
90.0
92.0
92.0
94.0
91.3
80.0
92.7
90.7
91.3
93.3
93.3
94.0
94.7
95.3
88.0
88.0
10.0
14.4
18.8
38.3
19.7
32.2
18.4
29.3
34.6
42.8
40.9
41.3
58.7
53.0
38.4
58.4
47.0
63.4
63.6
53.3
62.9
66.6
70.9
71.2
43.7
Figure 6: Heatmap displaying the achieved NPM of every tested model for every task in PoETa v2.
Tasks are ordered by the average performance achieved by all models. Models are ordered by their
computational cost.
32

```
