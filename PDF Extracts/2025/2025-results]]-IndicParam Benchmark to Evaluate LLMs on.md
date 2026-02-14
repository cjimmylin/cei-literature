---\ntitle: "2025-results]]-IndicParam Benchmark to Evaluate LLMs on - PDF Extract"\nsource_pdf: "2025/2025-results]]-IndicParam Benchmark to Evaluate LLMs on.pdf"\npages: 21\nextracted_at: "2026-02-14T02:17:32.250853"\n---\n\n# PDF Extract: 2025-results]]-IndicParam Benchmark to Evaluate LLMs on\n\n**Source PDF:** 2025/2025-results]]-IndicParam Benchmark to Evaluate LLMs on.pdf\n**Total Pages:** 21\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nIndicParam: Benchmark to evaluate LLMs on low-resource Indic
Languages
Ayush Maheshwari, Kaushal Sharma♠, Vivek Patel♠, Aditya Maheshwari♠
♠Indian Institute of Management Indore, India ; ♠BharatGen
ayush.hakmn@gmail.com, {kaushals,vivekp,adityam}@iimidr.ac.in
Abstract
While large language models excel on high-
resource multilingual tasks, low- and ex-
tremely low-resource Indic languages remain
severely under-evaluated. We present Indic-
Param, a human-curated benchmark of over
13,000 multiple-choice questions covering 11
such languages (Nepali, Gujarati, Marathi,
Odia as low-resource; Dogri, Maithili, Ra-
jasthani, Sanskrit, Bodo, Santali, Konkani as
extremely low-resource).
We evaluated 20
LLMs, both proprietary and open-weights,
which reveals that even the top-performing
Gemini-2.5 reaches 58% average accuracy,
followed by GPT-5 (45) and DeepSeek-3.2
(43.1).
We additionally label each question
as knowledge-oriented or purely linguistic to
discriminate factual recall from grammatical
proﬁciency. Further, we assess the ability of
LLMs to handle diverse question formats-such
as list-based matching, assertion-reason pairs,
and sequence ordering-alongside conventional
multiple-choice questions. IndicParam pro-
vides insights into limitations of cross-lingual
transfer and establishes a challenging bench-
mark for Indic languages.
The dataset
is available at https://huggingface.co/
datasets/bharatgenai/IndicParam1.
1
Introduction
Large language models (LLMs) have delivered
state-of-the-art results across a range of multi-
lingual tasks, particularly in high- and medium-
resource settings such as translation, named en-
tity recognition, and question answering (Liu et al.,
2024). However, systematic evaluation for low and
extremely-low-resource Indic languages remains
limited. Existing benchmarks for Indic languages
have signiﬁcant coverage for major languages (e.g.
Hindi, Tamil, Telugu) (Singh et al., 2024; Kakwani
1Scripts to run benchmark are present at https://
github.com/ayushbits/IndicParam
Language
#Words (in M)
#Speakers (in M)
Nepali
1642.9
19.4
Marathi
1541.2
99.1
Gujarati
934.1
60.3
Odia
333.8
42.6
Sanskrit
16.9
3.1
Maithili
14.0
14.3
Konkani
2.8
2.6
Santali
0.8
7.7
Bodo
0.8
1.5
Dogri
0.6
2.8
Rajasthani
-
25.8
Total
4480
279.1
Table 1: Number of words (in millions) present in
FineWeb2 corpus and number of speakers (in millions)
for each language considered in IndicParam.
et al., 2020), yet they provide only partial or no sup-
port for several understudied languages. Addition-
ally, they rarely include coverage for code-mixed
usage and evaluation.
In Table 1, we present word counts for the Indic-
Param languages within FineWeb2 (Penedo et al.,
2025). FineWeb2 is a cleaned pretraining corpus
comprising of approximately 3 trillion words from
around 1800 languages (excluding English) gath-
ered from more than 100 Common Crawl snap-
shots. For the 11 languages analyzed in this bench-
mark, the FineWeb2 corpus contains 4.49 billion
words. Four languages-Nepali, Marathi, Gujarati,
and Odia-account for 4.45 billion of these words,
leaving only 36 million words for the remaining six
languages. Collectively, these 11 languages repre-
sent about 280 million speakers across the Indian
subcontinent, yet their aggregate web presence is
disproportionately small relative to their speaker
base.
Based on the availability of web corpus,
we classify Marathi, Gujarati, Nepali and Odia
as low-resource languages while remaining seven
languages as extremely low-resource languages.
arXiv:2512.00333v2  [cs.CL]  12 Jan 2026

--- Page 2 ---\n\nFigure 1: Average performance for all languages on IndicParam. Except DeepSeek-V3.2, all closed models out-
perform best performing open-weight models.
Low resource (4): Nepali, Gujarati, Marathi,
Odia
Extremely-low resource (7): Dogri, Maithili,
Rajasthani, Sanskrit, Bodo, Santali, Konkani
India, with a population of approximately 1.4
billion, is home to over 120 languages, at least 30
of which have one million or more speakers (Oﬃce
of the Registrar General & Census Commissioner,
India, 2018). These languages span multiple fam-
ilies, for instance, Marathi and Hindi belong to the
Indo-European branch; Kannada and Telugu are
Dravidian; Santali is Austro-Asiatic; and Bodo is
Sino-Tibetan. The Indian Constitution recognizes
22 languages in the Eighth Schedule, yet most ex-
isting benchmarks concentrate on 11 major lan-
guages that together account for more than 93%
of speakers, largely reﬂecting the limited availabil-
ity of web-scale data for others (IAMAI, 2024).
With recent advances in multilingual LLMs, lan-
guage understanding has improved for many of
these widely used languages (Hu et al., 2020; Qin
et al., 2025). However, despite a few benchmarks
covering the majority set of 11 languages, there
exists almost no evaluation resources for other In-
dic languages (Kumar et al., 2022; Madasu et al.,
2023).
To address these limitations, this paper intro-
duces IndicParam, a human-supervised evalua-
tion set comprising more than 13,000 questions
for 11 low- and extremely low-resource Indic lan-
guages. We also include a code-mixed Sanskrit-
English language set evaluation. We hypothesize
that despite limited pretraining data in several of
these languages, LLMs can exploit cross-lingual
transfer among typologically and script-wise re-
lated languages to improve performance on these
target languages.
To separate language under-
standing from factual recall, each question is la-
beled as either linguistic (e.g., morphology, syntax,
semantics, discourse) or knowledge-based (world
facts and entities).
We evaluate 20 LLMs spanning open- and
closed-source systems and a range of parameter
scales and architectures on IndicParam.
The
evaluated models includes closed models such as
GPT-5, Gemini-2.5, Claude-Haiku-4.5, and open
weight models such as Llama4-Scout, DeepSeek-
V3.2 among others. In Figure 1, we present the
average performance of all models. Larger models
with substantial exposure to multilingual Indic cor-
pora tend to outperform smaller models. However,
no model exceeds a 58% average score on Indic-
Param. Gemini-2.5 achieves the highest overall
accuracy at 58, followed by GPT-5 at 45, Claude-
Haiku at 42.7 and Grok-4 at 39.6, indicating that
model robustness on these languages remains lim-

--- Page 3 ---\n\nited even among state-of-the-art proprietary mod-
els.
Open-weight models narrows the gap with
DeepSeek-V3.2 (DeepSeek-AI, 2025a), which is a
685B parameter model (43.1%) while Llama 3.3-
70B attains average accuracy of 39.6.
Overall,
results indicate that multilingual performance for
Indic languages remains challenging across both
closed and open models, with substantial room for
improvement in cross-lingual generalization. Our
contributions can be summarised as follows:
1. We present IndicParam, a benchmark consist-
ing of 13K+ questions on 11 low- and extremely-
low resource Indic languages, as well as a code-
mixed English-Sanskrit variant.
2. We provide granular annotations for each in-
stance in the benchmark, including question-type
and question-category labels, to enable systematic
analysis of LLM capabilities.
3. We conduct an extensive evaluation encompass-
ing 20 LLMs, including both proprietary closed-
source and open-weight models.
2
Related Work
LLMs have demonstrated substantial improve-
ments in language understanding performance
for several Indic languages (SarvamAI; Pundalik
et al., 2025). Multiple Indic multilingual bench-
marks evaluate such progress, primarily targeting
major mid- and high-resource languages (Singh
et al., 2025, 2024; Maheshwari et al., 2024). Indic-
GenBench (Singh et al., 2024) proposes a bench-
mark on 29 Indic languages, including those ex-
amined in this study. Its evaluation suite includes
tasks such as reading comprehension and trans-
lation, which are primarily adapted from English
benchmark datasets like XQUAD (Artetxe et al.,
2020) and FLORES (Goyal et al., 2022). Indic-
GenBench QA tasks restrict answers to spans sup-
ported by the given passage. In contrast, Indic-
Param extends this evaluation paradigm by as-
sessing both language understanding and domain-
speciﬁc general knowledge of LLMs using ques-
tions drawn from graduate-level examinations.
IndicGLUE (Kakwani et al., 2020) is a suite
of supervised NLP tasks for prominent Indic lan-
guages, with a particular emphasis on Hindi, in-
cluding classiﬁcation tasks such as news catego-
rization and headline prediction, as well as natural
language inference, among others. IndicXTREME
(Doddapaneni et al., 2023) broadens task cover-
age to named entity recognition, question answer-
ing, and paraphrase detection, and expands lan-
guage coverage by translating and curating bench-
marks in 11 Indic languages; however, many long-
tail languages remain outside its scope. Recent In-
dic QA benchmarks further diversify evaluation:
ParamBench (Maheshwari et al., 2025) focuses
on graduate-level questionnaires with varied ques-
tion types in Hindi, while MILU (Verma et al.,
2025) contains 79K questions across 11 Indian
languages, including Odia, Gujarati, and Marathi,
which are also covered in IndicParam. Sanskriti
(Maji et al., 2025a) and Pariksha (Watts et al.,
2024) are English-language benchmarks designed
to assess the socio-cultural alignment of LLMs.
Drishtikon (Maji et al., 2025b) further extends this
line of work to multimodal cultural understanding
across 15 Indic languages.
Despite this progress, most benchmarks concen-
trate on the majority of 11 widely used Indian lan-
guages, with very limited coverage for extremely
low-resource languages. In this paper, we intro-
duce graduate-level language understanding ques-
tionnaires in 4 low-resource and 7 extremely low-
resource languages, enabling targeted assessment
of both language competence and general knowl-
edge for underrepresented Indic languages.
3
IndicParam
IndicParam is a high-quality QA benchmark con-
sisting of 13,207 questions that evaluates language
understanding and general knowledge of multilin-
gual LLMs in 11 Indic languages. These languages
are spoken by approximately 280 million people
across the Indian subcontinent, of whom 10 lan-
guages are recognized as scheduled languages in
the Indian Constitution. Rajasthani, though not a
scheduled language, is spoken by roughly 25 mil-
lion people. We also include a QA set of code-
mixed version of Sanskrit where questions include
a mix of English and Sanskrit.
The language-wise distribution of questions is
shown in Table 2. The questions are collected from
UGC-NET2, which is a nationwide examination
administered by a government agency to determine
eligibility for PhD admission and appointment to
teaching positions in Indian universities and col-
leges. The exam is oﬀered in around 85 subjects
and is conducted twice annually. Each test consists
of two papers composed of multiple-choice ques-
tions (MCQs). We developed the dataset by down-
2https://ugcnet.nta.ac.in

--- Page 4 ---\n\nLanguage
#Ques
LU(%)
Script
Code
Nepali
1038
18.8
Deva
npi
Marathi
1245
4.7
Deva
mar
Gujarati
1044
0.6
Gujarati
guj
Odia
577
20.3
Orya
ory
Maithili
1286
10.1
Deva
mai
Konkani
1328
2.5
Deva
gom
Santali
873
11.3
Olck
sat
Bodo
1313
-
Deva
brx
Dogri
1027
18.3
Deva
doi
Rajasthani
1190
27.8
Deva
-
Sanskrit
1315
20.7
Deva
san
Sans-Eng
971
11.5
-
-
Total
13207
Table 2: Distribution of question-answer pairs for dif-
ferent languages in IndicParam. ‘Sans-Eng’ denotes a
separate set of Sanskrit-English code-mixed question-
answer pairs. LU refers to % of manually classiﬁed
language-understanding questions; rest are categorized
as knowledge-related (c.f. Section 3.1).
loading question papers and answer keys from the
oﬃcial examination website for the period between
2012-2018.
Each language comprises multiple PDF ques-
tion papers, many machine-readable and a subset
with non-selectable text. Document layouts vary,
with some single-column and most two-column.
To ensure uniform accessibility, all PDFs were pro-
cessed with a proprietary OCR system, and the ex-
tracted text was used for downstream curation and
annotation. To the best of our knowledge, this cor-
pus has not appeared in prior LLM benchmarking
studies and constitutes a newly curated, human-
authored dataset explicitly designed for graduate-
level evaluation in Indic contexts. We describe an-
notation setup and team structure in Section 8 in
Appendix.
3.1
Question Classiﬁcation
In addition to annotating question-answer pairs
in IndicParam, each question is assigned to one
of two categories: (a) language understanding
(LU) that includes questions related to linguis-
tics and grammar, and (b) general knowledge
(GK) targeting fact-based queries. Given the low-
and extremely low-resource nature of the studied
languages, this evaluation investigates model per-
formance under data scarcity conditions and ex-
amines the extent to which cross-lingual trans-
fer mechanisms can compensate for limited in-
language training data.
The distribution of questions across these cate-
gories for each language is presented in Table 2.
The LU column reports, for each language, the
proportion of questions that test language under-
standing while the remaining questions belonging
to the GK category and focusing on factual knowl-
edge. The share of LU questions varies substan-
tially, from under 1% in Gujarati to nearly 28%
in Rajasthani, with several other languages such
as Odia and Sanskrit also exhibiting over 20% LU
coverage.
3.2
Question Type Classiﬁcation
Following ParamBench (Maheshwari et al., 2025),
we annotate each question-answer pair with its cor-
responding question type. We classify them into
six primary categories that capture the diversity of
assessment formats (see Table 3): multiple-choice
questions (MCQ), assertion and reasoning (A&R),
list matching, blank ﬁlling, identify incorrect state-
ment (IS), and ordering. The majority (73%) of
the questions are MCQs followed by list match-
ing (9%), ordering (6.5%), A&R (6.1%), IS (4.1%)
and blank ﬁlling (1.1%). The language wise break-
down of all languages remains the same except for
Bodo, Gujarati, and Dogri, where the proportion
of MCQs remain 36.6%, 33% and 21.7%, respec-
tively, which are signiﬁcantly lower than other lan-
guages in the benchmark. The detailed statistics of
language-wise splits of question types is present in
Table 6. In Table 11, we present example ques-
tions from diﬀerent languages and their respective
question class and question type.
3.3
Quality control and Veriﬁcation
We used a multistep veriﬁcation pipeline for lin-
guistic precision and integrity of data. Primary
data was taken from high-resolution, native PDFs
from the oﬃcial UGC NET portal to minimize ex-
traction noise. Text extraction was script-tailored:
LLMWhisperer3 for Devanagari scripts-Sanskrit,
Maithili, Marathi-to preserve complex conjuncts,
and Surya OCR (Paruchuri and Team, 2025) for
Gujarati and Odia, followed by intensive manual
correction by experts.
A post-veriﬁcation audit on a random 5% sam-
ple (10,427 words and 61,547 characters) reported
3https://unstract.com/llmwhisperer/

--- Page 5 ---\n\nQuestion Type
#Questions
Multiple-choice
9653
Assertion & Reason
811
List Matching
1185
Fill in the blanks
157
Identify incorrect statement
545
Ordering
856
Total
13207
Table 3: Distribution of questions across all languages
in IndicParam.
a Word Error Rate (WER) of 0.68% and a Char-
acter Error Rate (CER) of 0.12%, conﬁrming high
reliability of the processed text. Please refer to the
Appendix section 8.1 for more details.
3.4
Setup
We evaluated 20 state-of-the-art models spanning
both open-weight and proprietary LLMs.
The
open-weight models range from 3 billion to over
685 billion parameters, including both dense and
mixture-of-experts (MoE) architectures.
These
models collectively represent the state of the art
in multilingual reasoning, code understanding, and
multimodal generation.
All models were used
in their instruction-tuned conﬁgurations and eval-
uated under a zero-shot prompting setup.
The
prompt used during evaluation is present in Table
8. We apply a single, standardized prompt tem-
plate across all languages and models. We also ex-
perimented with alternative prompt formulations,
including prompts written in diﬀerent languages;
however, these variations did not meaningfully af-
fect the results
Open-weights models are retrieved from pub-
licly available checkpoints at HuggingFace and use
transformers library for inference. We load param-
eter weights in bf16 precision for all open-weight
models except Llama4-Scout which was loaded
with 8-bit quantization.
We use greedy decod-
ing while generating predictions by setting max-
tokens as 50, temperature as 0, do_sample ﬂag
to false and batch size is set to 16. We disable
thinking mode for Qwen3-MoE and keep reason-
ing levels at low for GPT-OSS-120B. For Gemma
and Mistral, we follow their respective strategies
from response generation instead of transformers
pipeline function. We use OpenRouter (https:
//openrouter.ai) to generate predictions for
closed models. We next describe the models in-
cluded in our evaluation.
1.
Qwen Series (Team-Qwen3, 2025):
We
evaluated multiple models of the Qwen fam-
ily,
including Qwen2.5-3B, Qwen3-4B-2507,
Qwen3-30B-A3B, and Qwen3-32B. The Qwen 3
series integrates substantial architectural and pre-
training improvements over the 2.5 generation,
trained on roughly 36 trillion multilingual tokens
spanning 119 languages.
The Qwen3-30B-A3B
variant adopts a mixture-of-experts (MoE) design
with 3 billion active parameters per forward pass,
providing strong eﬃciency while maintaining per-
formance parity with larger dense models.
2.
Llama Series (Team, 2024):
We evalu-
ated Metas Llama-3.2-3B, Llama-3.1-8B, and
Llama-3.3-70B. These models are trained on a
mixture of high-quality multilingual and code data
totaling approximately 15 trillion tokens. We also
evaluated on Llama-4-Scout-17B-16E which is
an MoE model having a 17 billion active pa-
rameters with 16 experts with a total of 109 bil-
lion model parameters. This model is trained on
40T tokens speciﬁcally designed to improve multi-
lingual text and images.
3.
Gemma Series (Team, 2025):
We evalu-
ated Gemma-3 models at 4B, 12B, and 27B pa-
rameter scales. Developed by Google DeepMind,
the Gemma 3 family employs hybrid instruction-
ﬁne-tuning strategies and trained on diverse mul-
tilingual datasets.
These models have demon-
strated strong alignment and competitive perfor-
mance across multilingual and reasoning bench-
marks.
4.
Aya Expanse (Aryabumi et al., 2024):
The Aya-Expanse-8B and Aya-Expanse-32B
models are instruction-tuned multilingual LLMs.
These models prioritize cultural and linguistic
diversity and are trained on extensive parallel
datasets that include over 100 diﬀerent languages.
5.
Mistral 3.1 (MistralAI): We evaluated the
Mistral-Small-3.1-24B-2503 which is a 24
billion parameter multi-lingual model achieving
competitive performance while maintaining fast
inference throughput.
6.
DeepSeek V3.2 (DeepSeek-AI, 2025b):
We evaluated DeepSeek-V3.2-Experimental
model consisting of 685B parameters. It employs
specialized routing and sparsity mechanisms to re-
duce inference costs while preserving high-quality
reasoning, code synthesis, and mathematical rea-

--- Page 6 ---\n\nsoning performance.
7. GPT-OSS-120B (OpenAI et al., 2025): We ex-
amined the GPT-OSS-120B model, an open-weight
MoE model by OpenAI, trained on trillions of to-
kens with a focus on STEM, coding, and general
knowledge. It has a total of 116.8B parameters and
5.1B active parameters per token per forward pass.
8. Frontier Proprietary Models: For complete-
ness, we also benchmarked several leading closed-
source systems accessible through public APIs:
GPT-5, Claude-Haiku-4.5, and Grok-4-Fast.
– GPT-5 (OpenAI) represents the current ﬂagship
frontier model, incorporating multimodal reason-
ing and tool-use capabilities.
– Claude-Haiku-4.5 (Anthropic) is a lightweight
yet high-accuracy variant of the Claude 4.5 fam-
ily designed for eﬃciency-critical environments.
– Grok-4-Fast (xAI) is optimized for rapid infer-
ence and contextual awareness within streaming
conversational environments.
– Gemini-2.5-Flash
(Comanici et al., 2025)
(Google) is a sparse MoE model and a distilled ver-
sion of a larger Gemini-2.5 model.
4
Results and discussion
4.1
Overall Model Performance
The evaluation results presented in Figure 1
demonstrate that average performance on Indic-
Param for 20 evaluated models remains mod-
erate, though several interesting patterns emerge
when grouped by model scale. Among the small-
capacity models (<8B parameters), the Qwen fam-
ily performs best: Qwen3-4B and Qwen2.5-3B
achieves the accuracy of 30.8 and 30.1 respec-
tively. Other models in this category, including
Gemma-3-4B, and Llama-3.2-3B, remain around
the 27-30% range.
In
the
medium-size
category
(8B-27B),
performance
improves
considerably,
with
Gemma-3-27B
leading
at
37.3%,
fol-
lowed
closely
by
Gemma-3-12B
(35.3)
and
Mistral-Small-3.1-24B (35.1).
Other mod-
els like Aya-Expanse-8B and Llama-3.1-8B
score less than 30%. These ﬁndings underscore
that model scale beyond 8B yields measurable
gains, but pre-training coverage and multilingual
representation continue to play a decisive role in
performance.
Among the larger and frontier models (≥27B),
overall accuracy rises substantially.
The best
performance is achieved by Gemini-2.5, which
attains an average of 58%, followed by GPT-5 (45),
DeepSeek-V3.2
(43.1),
Claude-Haiku-4.5
(42.7),
and
Grok-4-Fast
(39.6).
Open-
weight models such as Llama-3.3-70B and
GPT-OSS-120B achieve 38.6 and 37.7, respec-
tively,
while
the
Llama-4-Scout-17B-16E
models remain slightly lower at 35.5.
These
results indicate that while data and parameter size
enhance overall accuracy, the highest-performing
models also beneﬁt from reﬁned ﬁne-tuned on
multilingual or Indic-rich corpora.
Overall, the evaluation reveals a clear up-
ward trajectory in accuracy with increasing model
scale, yet even the most capable frontier systems
such as Gemini-2.5, GPT-5 and DeepSeek-V3.2
demonstrate that substantial headroom remains for
further enhancement in Indic language understand-
ing. The results aﬃrm that cross-lingual gener-
alization, ﬁne-tuning quality, and the underlying
token distribution remain central determinants of
downstream accuracy.
4.2
Performance on Low- and Extremely
Low-Resource Indic Languages
Table 4 and Table 5 compare contemporary LLMs
on eight extremely low-resource Indic languages
(Dogri, Maithili, Rajasthani, Sanskrit, Sanskrit–
English code-mixed, Bodo, Santali, and Konkani)
and four higher (yet still low-resource) Indic lan-
guages (Nepali, Gujarati, Marathi, and Odia)
respectively.
On extremely low-resource lan-
guages, Gemini-2.5 achieves the highest average
of 59.2%, followed by GPT-5 (45.1), open-weight
DeepSeek-3.2 at 43.7. No model exceeds 53 on
the most underrepresented languages (Bodo and
Santali), with most models remaining below 36%.
Gemini-2.5 shows strong performance on San-
skrit (72.4) and Sanskrit–English code-mixed text
(80.3).
Despite Gemini-2.5 performing remark-
ably better than other LLMs, the remaining models
exhibit substantially lower performance, suggest-
ing that strong Indic-language capability is not yet
widespread across current LLMs.
With the exception of Rajasthani and Sanskrit,
all models including Gemini scores less than 54%
for all other languages. Notably, even very large
parameter Deepseek model scores under 44%,
aside from the Sanskrit variants. The relatively
stronger results for Rajasthani may stem from its
linguistic proximity to Hindi, which is typically
well represented in model pretraining corpora. De-
spite limited web-scale data availability, Sanskrit

--- Page 7 ---\n\nSize
Model
Dogri
Maithili
Rajasthani
Sanskrit
Sans-Eng
Bodo
Santali
Konkani
Average
Small
Qwen2.5-3B
32.1
28.8
28.6
31.9
34.8
28.3
33.1
31.4
30.9
Llama-3.2-3B
27.9
21.9
26.3
28
27.9
27.8
27.4
28.8
26.9
Gemma-3-4b
30.5
24.5
27.6
29.1
32.2
25.8
31.7
29.1
28.5
Qwen3-4B
34.6
31.6
30
33.8
33.6
25.1
33.8
29.6
31.2
Medium
Aya–8b
31.5
29.9
30.8
29.4
29.9
28.1
30.8
26.9
29.5
Llama-3.1-8B
26.4
29
31.8
32.2
34
26.8
30.6
29.5
30.0
Gemma-3-12b
37.2
31.6
35
37.1
41.8
30.6
33.7
35.7
35.1
Mistral3.1-24b
38
37.4
34.8
40
44.1
30.1
35.7
32
36.2
Gemma-3-27b
37.6
34.4
39.8
38.6
49.1
28.9
36.7
36.5
37.3
Large
Aya-32b
35.2
33.2
34.6
35.2
39
27.2
35.6
33.1
33.7
Qwen3-32B
43.4
34
33.8
39.2
48.6
31.8
39.7
34.5
33.9
Llama-3.3-70B
37.3
37.5
38.2
41.7
51.6
28.6
40.1
37.3
37.6
DeepSeek-3.2
43.3
41.4
40.1
51.3
61.4
36.4
41.5
37.6
43.7
MoE
Qwen3-A3B
35.7
30.9
31.6
36.7
44.2
29.9
35.9
28.3
38.6
Llama-4-Scout
30.5
31.3
34.8
44
48.7
25.9
36.3
34.6
35.4
gpt-oss-120b
39.7
35.6
39.4
40.2
48.1
28.3
35.6
35.4
37.4
Closed
GPT-5
45.7
43.4
44.6
54.8
64.6
31.6
40.4
39
45.1
Grok-4-fast
40.2
38.1
39.1
42.9
54.2
30.6
38.8
37.4
39.7
Claude-4.5
44.8
42.4
44.1
47.8
58.1
28.1
40.4
42.1
43.0
Gemini-2.5
54.2
54
66.6
72.4
80.3
48.1
52.9
48.4
59.2
Table 4: Performance on extremely-low resource languages on IndicParam. We bold and italicize the best overall
performance, underline and italicize the best performance in each model-size category and underline the second
best overall performance.
Size
Model
Nepali
Gujarati
Marathi
Odia
Average
Small
Qwen2.5-3B
27.1
29.5
27.9
28.8
28.2
Llama3.2-3B
26.2
26.1
28.6
27
27.1
Gemma-3-4b
29
26.2
29.9
31.5
28.9
Qwen3-4B
28.7
27.4
30.5
34.7
29.8
Medium
Aya-8b
28.2
27.7
28.3
28.1
28.1
Llama3.1-8B
25.5
27.2
32.2
29.3
28.7
Gemma-3-12b
34.8
33.8
38.4
34.5
35.6
Mistral3.1-24b
34.9
32.6
32.9
27.6
32.6
Gemma3-27b
39.3
31.1
39.9
39.9
37.4
Large
Aya-32b
31.6
30.7
35.5
34.5
33.0
Qwen3-32B
33
28.4
33.2
28.9
31.2
Llama3.3-70B
35
35.9
40.8
40.7
37.9
DeepSeek-3.2
39.7
39.5
44.6
42.1
41.6
MoE
Qwen3-A3B
37.2
33.5
43.5
40.4
38.7
Llama-4-Scout
34.6
27.3
43.5
35
35.5
gpt-oss-120b
37.1
37
39.7
39.9
38.3
Closed
GPT-5
43.4
40
48.4
48.7
44.9
Grok-4-fast
40.9
35.9
39.8
40.7
39.2
Claude-4.5
43.8
37
43.9
44
42.0
Gemini-2.5
52
51.7
55.7
64.5
54.9
Table 5: Performance on low resource languages on IndicParam. We bold and italicize the best overall perfor-
mance, underline and italicize the best performance in each model-size category and underline the second best
overall performance.
is a well-studied language in the NLP literature,
which may partially explain its comparatively bet-
ter performance.
Among smaller models, the Qwen family out-

--- Page 8 ---\n\nperforms Gemma and Llama models.
In con-
trast, Gemma3-27B surpasses Qwen3-32B, which
is counter-intuitive to the assumption that Qwen3’s
larger pretraining corpus necessarily yields consis-
tent downstream gains. Overall, within the open-
weight models, DeepSeek performs best, sug-
gesting beneﬁts from its architectural choices and
larger parameter scale.
In the low-resource group, Gemini-2.5 again
leads with 54.9%,
ahead of
GPT-5 (44.9),
Claude-4.5 (42.0) and DeepSeek-3.2 (41.6).
Among other open models, Gemma-3-27b (37.4)
and the MoE Qwen3-A3B (38.7) perform best
in their respective size categories.
Notably,
Gemini-2.5 achieves the highest performance in
Odia (64.5), followed by Marathi (55.7) having a
8.8 points drop. In contrast, other models exhibit a
much smaller performance gap between these two
languages.
Except for Gemini, all other models score be-
low 50% across each of the four languages con-
sidered. Small-size models achieve their highest
score in Odia (34.7), and medium-size models like-
wise obtain their best result in Odia (39.9). Among
larger open-weight models, DeepSeek attains the
strongest performance, scoring 44.6 on Marathi.
Overall, these ﬁndings suggest that improving per-
formance on low-resource Indic languages likely
requires both stronger general pretraining data and
targeted, language-speciﬁc resources.
4.3
Performance on General Knowledge and
Language Understanding Tasks
We distinguish between two complementary ca-
pabilities: (i) General Knowledge questions that
require factual reasoning and culturally grounded
world knowledge (Table 9), and (ii) Language-
Speciﬁc Understanding questions that probe gram-
matical, lexical, morphosyntactic, and discourse-
level proﬁciency within each Indic language (Ta-
ble 10). LU questions forms a very small percent-
age of overall questions, particularly for Gujarati
(0.6%).
4.3.1
General Knowledge
Frontier models exhibit clear separation from the
rest of the models.
Gemini-2.5 achieves the
highest average (58), followed by GPT-5 (54.8),
Claude-4.5 (43.5) and DeepSeek-3.2 (43.3).
Among open-weight systems, Llama-3.3-70B
(39.3) and gpt-oss-120b (38) perform compet-
itively, while Grok-4-fast attains 40.3. Large
gains are observed with scale: medium-sized mod-
els (8B–27B) top out at 37.9 (Gemma-3-27b), and
small models (<8B) remain below 32 (Qwen3-4B:
31.3). As shown in Table 9, Gemini dominates
Sanskrit (74.4) and Sanskrit–English code-mixed
(80.3) contexts,
reﬂecting superior classical-
language representation.
4.3.2
Language-Speciﬁc Understanding
Performance on pure linguistic tasks is higher
than GK questions on all languages except San-
skrit. Except Gemini, none of the models rarely
exceed 67% on any single language (see Ta-
ble 10).
Gemini-2.5 again leads (69.8 av-
erage), followed by GPT-5 (52.5) Claude-4.5
(49.8) and DeepSeek-3.2 (46.3).
Several
medium-scale models punch above their parameter
count: Llama-4-Scout (41.7, especially strong
on Marathi) and Gemma-3-27b (42.2) occasionally
outperform larger dense models on morphologi-
cally complex languages. Smaller models struggle
severely, with many scores in the 20-35% range; as
evident in Table 10. Sanskrit, Sanskrit+Eng, Do-
gri, Nepali and Santali prove particularly challeng-
ing across the board.
A comparative analysis of GK and LU re-
veals distinct scaling behaviours. General knowl-
edge accuracy correlates strongly with model scale
(Pearson r = 0.91 across the 20 evaluated models),
whereas language-speciﬁc understanding shows a
weaker but still substantial correlation (r = 0.73).
The correlation between the two dimensions is
moderately high (r = 0.79), indicating that top-tier
factual reasoning usually co-occurs with stronger
linguistic proﬁciency, yet meaningful divergences
remain.
Several models achieve notably balanced per-
formance.
Gemma-3-27b (GK: 37.9, LU: 40.9)
and Mistral3.1-24b (GK: 35.3, LU: 42.7) out-
perform many larger dense models on linguistic
tasks, demonstrating that continued pre-training on
diverse Indic corpora and instruction tuning can
compensate for parameter count in morphosyntac-
tically demanding settings. Similarly, MoE-based
Llama-4-Scout reaches 41.8 on language under-
standing while scoring only 35.6 on general knowl-
edge, highlighting the value of sparse architectures
for grammar-heavy tasks.
These results underscore that future progress
on low- and extremely low-resource Indic lan-
guages will require not only continued scaling but
also (i) higher-quality and more diverse Indic pre-

--- Page 9 ---\n\ntraining data, (ii) dedicated cross-lingual continua-
tion training, and (iii) architectural innovations that
prioritise ﬁne-grained morphological and syntac-
tic representation.
5
Conclusion
We present IndicParam consisting of >13k ques-
tions for 11 low and extremely-low resource In-
dic languages. Our benchmark reveals that even
the strongest contemporary LLMs, including fron-
tier proprietary systems, remain far from reli-
able on graduate-level questions in low- and ex-
tremely low-resource Indic languages, with no
model surpassing 45% average accuracy except
Gemini-2.5.
While larger closed models such
as Gemini-2.5, GPT-5, Claude-4.5 and open-
weight model, DeepSeek-3.2 consistently outper-
form open-weight alternatives.
These ﬁndings
indicate IndicParam as a challenging, human-
curated evaluation suite that ﬁlls a key gap in ex-
isting Indic benchmarks and underline the need
for more balanced pretraining and adaptation for
under-represented Indic languages.
6
Limitations
While IndicParam substantially broadens evalu-
ation for low- and extremely low-resource Indic
languages, the benchmark is derived exclusively
from UGC-NET language papers in linguistics and
literature, which biases the content toward aca-
demic exam styles and may not fully represent ev-
eryday or domain-general language use. Further,
our evaluation is conducted using a log-likelihood-
based multiple-choice setup in a zero-shot conﬁgu-
ration, which may yield diﬀerent results from alter-
native evaluation schemes such few-shot prompt-
ing, or chain-of-thought prompting, and therefore
does not capture the full range of behaviors that
these models might exhibit under richer prompting
strategies.
7
Ethics
All data described in this work was collected from
publicly available resources. We sought permis-
sion of UGC-NTA for releasing the benchmark.
IndicParam is released for non-commercial re-
search use; code and annotation scripts are li-
censed under MIT. All annotation was conducted
by consenting native speakers compensated at lo-
cal rates, and no personally identiﬁable exam-
candidate information appears in the benchmark.
Users interested in commercial use should contact
UGC-NTA for relevant permissions.
References
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama.
2020. On the cross-lingual transferability of mono-
lingual representations. In Proceedings of the 58th
Annual Meeting of the Association for Computa-
tional Linguistics, pages 4623–4637.
Viraat Aryabumi,
John Dang,
Dwarak Talupuru,
Saurabh Dash, David Cairuz, Hangyu Lin, Bharat
Venkitesh, Madeline Smith, Jon Ander Campos,
Yi Chern Tan, Kelly Marchisio, Max Bartolo,
Sebastian Ruder, Acyr Locatelli, Julia Kreutzer,
Nick Frosst, Aidan Gomez, Phil Blunsom, Marzieh
Fadaee, Ahmet Üstün, and Sara Hooker. 2024. Aya
23: Open weight releases to further multilingual
progress.
Gheorghe Comanici, Eric Bieber, Mike Schaekermann,
Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon,
Marcel Blistein, Ori Ram, Dan Zhang, Evan Rosen,
et al. 2025. Gemini 2.5: Pushing the frontier with ad-
vanced reasoning, multimodality, long context, and
next generation agentic capabilities. arXiv preprint
arXiv:2507.06261.
DeepSeek-AI. 2025a.
Deepseek-v3.2-exp: Boosting
long-context eﬃciency with deepseek sparse atten-
tion.
DeepSeek-AI. 2025b.
Deepseek-v3.2-exp: Boosting
long-context eﬃciency with deepseek sparse atten-
tion.
Sumanth Doddapaneni, Rahul Aralikatte, Gowtham
Ramesh, Shreya Goyal, Mitesh M Khapra, Anoop
Kunchukuttan, and Pratyush Kumar. 2023. Towards
leaving no indic language behind: Building monolin-
gual corpora, benchmark and models for indic lan-
guages.
In Proceedings of the 61st Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 12402–12426.
Naman Goyal, Cynthia Gao, Vishrav Chaudhary, Peng-
Jen Chen, Guillaume Wenzek, Da Ju, Sanjana Kr-
ishnan, MarcAurelio Ranzato, Francisco Guzmán,
and Angela Fan. 2022.
The ﬂores-101 evaluation
benchmark for low-resource and multilingual ma-
chine translation. Transactions of the Association for
Computational Linguistics, 10:522–538.
Junjie Hu, Sebastian Ruder, Aditya Siddhant, Graham
Neubig, Orhan Firat, and Melvin Johnson. 2020.
Xtreme: A massively multilingual multi-task bench-
mark for evaluating cross-lingual generalisation. In
International conference on machine learning, pages
4411–4421. PMLR.
IAMAI. 2024. Internet in india 2024. Research report,
Internet and Mobile Association of India (IAMAI).
Prepared in collaboration with Kantar.

--- Page 10 ---\n\nDivyanshu Kakwani, Anoop Kunchukuttan, Satish
Golla, Gokul NC, Avik Bhattacharyya, Mitesh M
Khapra, and Pratyush Kumar. 2020. Indicnlpsuite:
Monolingual corpora, evaluation benchmarks and
pre-trained multilingual language models for indian
languages. In Findings of the association for com-
putational linguistics: EMNLP 2020, pages 4948–
4961.
Aman Kumar, Himani Shrotriya, Prachi Sahu, Amogh
Mishra, Raj Dabre, Ratish Puduppully, Anoop
Kunchukuttan, Mitesh M Khapra, and Pratyush Ku-
mar. 2022.
Indicnlg benchmark:
Multilingual
datasets for diverse nlg tasks in indic languages.
In Proceedings of the 2022 conference on empiri-
cal methods in natural language processing, pages
5363–5394.
Yang Liu, Meng Xu, Shuo Wang, Liner Yang, Haoyu
Wang, Zhenghao Liu, Cunliang Kong, Yun Chen,
Maosong Sun, and Erhong Yang. 2024. Omgeval:
An open multilingual generative evaluation bench-
mark for large language models.
arXiv preprint
arXiv:2402.13524.
Lokesh
Madasu,
Gopichand
Kanumolu,
Nir-
mal
Surange,
and
Manish
Shrivastava.
2023.
Mukhyansh:
A headline generation dataset for
indic languages. In Proceedings of the 37th Paciﬁc
Asia Conference on Language, Information and
Computation, pages 620–634.
Ayush Maheshwari, Ashim Gupta, Amrith Krishna,
Atul Kumar Singh, Ganesh Ramakrishnan, Anil Ku-
mar Gourishetty, and Jitin Singla. 2024. Samayik: A
benchmark and dataset for English-Sanskrit transla-
tion.
Ayush Maheshwari, Kaushal Sharma, Vivek Patel,
and Aditya Maheshwari. 2025.
Parambench: A
graduate-level benchmark for evaluating llm un-
derstanding on indic subjects.
arXiv preprint
arXiv:2508.16185.
Arijit Maji, Raghvendra Kumar, Akash Ghosh, Sri-
parna Saha, et al. 2025a.
Sanskriti: A compre-
hensive benchmark for evaluating language mod-
els’ knowledge of indian culture.
arXiv preprint
arXiv:2506.15355.
Arijit Maji, Raghvendra Kumar, Akash Ghosh, Ne-
mil Shah, Abhilekh Borah, Vanshika Shah, Nishant
Mishra, Sriparna Saha, et al. 2025b.
Drishtikon:
A multimodal multilingual benchmark for testing
language models’ understanding on indian culture.
arXiv preprint arXiv:2509.19274.
Team MistralAI.
Mistralai/mistral-small-3.1-24b-
instruct-2503 ů hugging face.
Oﬃce of the Registrar General & Census Commis-
sioner, India. 2018. Census of india 2011: Paper 1
of 2018 – language, india, states and union territories
(table c-16). Census of India 2011, Paper 1 of 2018,
Language Data (Table C-16).
OpenAI, :, Sandhini Agarwal, Lama Ahmad, Jason Ai,
Sam Altman, Andy Applebaum, Edwin Arbus, and
Rahul K. 2025. gpt-oss-120b & gpt-oss-20b model
card.
Vikas Paruchuri and Datalab Team. 2025.
Surya:
A lightweight document ocr and analysis toolkit.
https://github.com/VikParuchuri/surya.
GitHub repository.
Guilherme Penedo, Hynek Kydlíek, Vinko Sabolec,
Bettina Messmer, Negar Foroutan, Amir Hossein
Kargaran, Colin Raﬀel, Martin Jaggi, Leandro Von
Werra, and Thomas Wolf. 2025.
Fineweb2: One
pipeline to scale them all – adapting pre-training data
processing to every language.
Kundeshwar Pundalik, Piyush Sawarkar, Nihar Sa-
hoo, Abhishek Shinde, Prateek Chanda, Vedant
Goswami, Ajay Nagpal, Atul Singh, Viraj Thakur,
Vijay Dewane, Aamod Thakur, Bhargav Patel, Smita
Gautam, Bhagwan Panditi, Shyam Pawar, Madhav
Kotcha, Suraj Racha, Saral Sureka, Pankaj Singh,
Rishi Bal, Rohit Saluja, and Ganesh Ramakrishnan.
2025. Param-1 BharatGen 2.9b model.
Libo Qin, Qiguang Chen, Yuhang Zhou, Zhi Chen,
Yinghui Li, Lizi Liao, Min Li, Wanxiang Che, and
Philip S. Yu. 2025. A survey of multilingual large
language models. Patterns, 6(1).
SarvamAI. Sarvam AI | Sovereign Indian AI Ecosys-
tem for LLMs, Agents, and AI Assistants — sar-
vam.ai.
https://www.sarvam.ai/.
[Accessed
20-08-2025].
Abhishek Kumar Singh, Vishwajeet Kumar, Rudra
Murthy, Jaydeep Sen, Ashish Mittal, and Ganesh Ra-
makrishnan. 2025. Indic qa benchmark: A multi-
lingual benchmark to evaluate question answering
capability of llms for indic languages. In Findings
of the Association for Computational Linguistics:
NAACL 2025, pages 2607–2626.
Harman Singh, Nitish Gupta, Shikhar Bharadwaj, Di-
nesh Tewari, and Partha Talukdar. 2024. Indicgen-
bench: A multilingual benchmark to evaluate gen-
eration capabilities of llms on indic languages. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 11047–11073.
Gemma 3 Team. 2025. Gemma 3 technical report.
Llama 3 Team. 2024. The llama 3 herd of models.
Team-Qwen3. 2025. Qwen3 technical report.
Sshubam Verma, Mohammed SaﬁUr Rahman, Vish-
wajeet Kumar, Rudra Murthy Venkataramana, and
Jaydeep Sen. 2025. Milu: A multi-task indic lan-
guage understanding benchmark. In Annual Confer-
ence of the North American Chapter of the Associa-
tion for Computational Linguistics.

--- Page 11 ---\n\nIshaan Watts, Varun Gumma, Aditya Yadavalli, Vivek
Seshadri, Manohar Swaminathan, and Sunayana
Sitaram. 2024. Pariksha: A large-scale investigation
of human-llm evaluator agreement on multilingual
and multi-cultural data. In Proceedings of the 2024
Conference on Empirical Methods in Natural Lan-
guage Processing, pages 7900–7932.

--- Page 12 ---\n\nAppendix
8
Annotation Setup
For each language, we ﬁrst collected oﬃcial UGC-NET language papers and corresponding answer keys
from the oﬃcial website4 and converted all ﬁles into a uniform machine-readable format. Question papers
appeared in double-column layouts, and many PDFs contained non-selectable text. Hence, all documents
were processed through a proprietary OCR pipeline to extract text consistently across heterogeneous
layouts and scan qualities. During this stage, each question was tagged with its language, subject, exam
session, and year, and answer keys were aligned to their corresponding items.
Following OCR, human annotators manually corrected recognition errors, restored missing characters
and diacritics, and normalised punctuation and spacing so that questions and options follow a pre-speciﬁed
parsing format. Beyond surface correction, annotators standardised structural formattingsuch as option
markers, numbering schemes, and line breaks. Each ﬁnal entry in IndicParam is stored with explicit
ﬁelds for question text, question type, four answer options, correct option, language, subject, year, and
unique question identiﬁer.
Annotation was carried out by native speakers having expertise in the target language and having
prior experience reading graduate-level exam material. Since many papers mix language-focused and
knowledge-focused content, annotators were required to demonstrate strong proﬁciency in the relevant
Indic script. All annotators received detailed written guidelines describing how to handle incomplete
questions, ambiguous answer keys, and exam-speciﬁc conventions, as well as how to assign labels for
language understanding (LU) versus knowledge-related (KR) items and for the six question types used in
the benchmark. Prior to full-scale annotation, annotators were given a sample dataset along with worked
examples. They were then assigned trial ﬁles, which were reviewed and corrected by the reviewers. Feed-
back was provided iteratively, and only after demonstrating consistent accuracy were annotators assigned
larger batches of data. For questionanswer pairs, annotation quality followed a focused two-step review
pipeline. In the ﬁrst step, annotators corrected OCR errors in the question and options, aligned each item
with the oﬃcial answer key, and ensured that exactly one option was marked as correct. In the second
step, a senior reviewer re-checked these corrected pairs against the original exam papers, verifying that the
question text and the designated correct option was faithful to the source. Annotators were compensated
at a rate of $1 per 10 questions.
8.1
Quality Control and Veriﬁcation
A multi-stage quality control and veriﬁcation pipeline was implemented to ensure that the dataset main-
tained integrity and linguistic precision. This ﬁrst involved acquiring the primary source data directly
from the oﬃcial website of UGC NET, in high quality, natively generated PDFs, thereby ensuring high
initial resolution and low extraction noise.
For the text extraction task, a approach was used based on script requirements. For languages using the
Devanagari script, such as Sanskrit, Maithili, and Marathi, LLMWhisperer5 was used because it has been
optimized for retaining complex Indic conjuncts. In contrast, non-Devanagari scripts, such as Gujarati
and Odia, had signiﬁcant extraction limits on multiple platforms. After comparing several options, Surya
OCR (Paruchuri and Team, 2025) was implemented, but it had more script-speciﬁc mistakes that required
intensive manual correction by subject area experts in Gujarati and Odia. All the Devanagari extractions
then underwent parallel manual veriﬁcation, wherein human annotators followed strict linguistic rules to
correct ocr-induced errors and ensure structural consistency.
Quantiﬁcation of ﬁnal data quality was done via a post-veriﬁcation audit on a randomized 5% sample
of the total ﬁle corpus. A sample of this size consists of 10,427 words and 61,547 characters, with 71
errors, which is a negligibly small WER of 0.68% and CER of 0.12%.
4https://ugcnet.nta.nic.in/
5https://unstract.com/llmwhisperer/

--- Page 13 ---\n\n9
Ethical considerations
This work introduces a new benchmark dataset derived from publicly available exam questions. As the
dataset is built exclusively from existing public materials and involves no new data collection from human
participants, no formal review by an Institutional Review Board (IRB) or equivalent ethics committee was
required or conducted. Instead, the authors performed an internal assessment of data provenance, potential
societal impacts, licensing considerations, and responsible use, in line with community standards for
responsible machine learning research (e.g., NeurIPS Ethics Guidelines).
9.1
Intended use and beneﬁciaries
The benchmark is designed to support research in evaluating LLM understanding on Indic subjects. It
aims to provide a challenging, realistic evaluation resource for the academic and AI research communi-
ties, as well as developers working on automated educational tools or knowledge-intensive systems. By
releasing this dataset, we hope to foster progress in fair, transparent, and reproducible benchmarking of
models at the graduate level, ultimately beneﬁting educators, students, and researchers seeking improved
AI capabilities in knowledge assessment.
9.2
Licensing and copyright considerations
The original UGC-NET exam questions are publicly released by the National Testing Agency (NTA),
Government of India, primarily for candidate preparation and result-related purposes (available on ugc-
net.nta.ac.in). No explicit redistribution license (e.g., Creative Commons) or statement prohibiting non-
commercial research use is provided on the oﬃcial website.
On November 21, 2025, we proactively contacted the NTA/UGC-NET team via email to seek formal per-
mission for including these publicly available questions in ParamBench. Our request emphasized that the
benchmark is strictly for non-commercial academic research under the DST-funded BharatGen project
(now part of the national IndiaAI Mission), with full attribution to "UGC-NET, National Testing Agency,
Government of India" in the paper and dataset. We attached the draft paper for their review. As of the
latest revision of this manuscript, we await their response and will update the dataset release accordingly
should any conditions be speciﬁed.
Pending explicit permission, we consider our transformative use (curated selection, cleaning, and re-
formatting into a machine-readable benchmark for 13,207 questions focused on Indian languages) per-
missible under fair dealing provisions of the Indian Copyright Act, 1957, for non-commercial research
and educational purposes. We do not redistribute raw original question papers/PDFs; only processed
question-answer pairs with metadata are released. The derived IndicParam dataset will be made available
under the Creative Commons Attribution 4.0 International (CC-BY-4.0) license, requiring attribution to
both this work and the original UGC-NET source.
10
Question Types-wise results
Table 6 presents the distribution of question types across subjects, and Table 7 provides the corresponding
performance results for these question types.
10.1
Question Types
Table 6 provides a detailed breakdown of the types of questions present in each language. MCQs dominate
the distribution, but a substantial number of list matching, AssertionReasoning(A&R), identiﬁcation of
incorrect statements (IS), ordering and blank ﬁlling questions contribute to diﬀerent question types.
10.2
Question type-wise results
Table 7 shows the performance of each model on IndicParam by question type. In the smaller-sized
models, Qwen3-4B demonstrates better performance in a majority formats of questions, which includes
MCQ, IS, ﬁll in the blanks and Ordering. This model outperforms alternative 34B models, including
Llama3.2-3B and Gemma3-4B. In the medium-size model category, Gemma3-27B shows the best overall
performance, with considerable improvements in MCQ, A&R, and ﬁll in the blanks. At the same time,

--- Page 14 ---\n\nLanguage
MCQ
A&R
List Matching
Blank Filling
IS
Ordering
Total
Nepali
957
1
38
5
25
12
1038
Marathi
933
83
139
1
54
35
1245
Gujarati
345
172
208
0
128
191
1044
Odia
379
40
70
1
22
65
577
Maithili
1265
0
0
21
0
0
1286
Konkani
1069
30
134
19
45
31
1328
Santali
772
36
46
11
2
6
873
Bodo
481
288
270
17
0
257
1313
Dogri
223
153
217
1
231
202
1027
Rajasthani
1114
4
11
14
13
34
1190
Sanskrit
1210
1
39
34
11
20
1315
Sans-Eng
905
3
13
33
14
3
971
Total
9653
811
1185
157
545
856
13207
Table 6: Diﬀerent question types across all languages in IndicParam. A&R refers to Assertion and Reason type
question, IS refers to identiﬁcation of incorrect statement. ‘Sans-Eng’ denotes a separate set of Sanskrit-English
code-mixed question-answer pairs which forms a separate set.
Gemma3-12B and Mistral3.1-24B also show competitive results in List Matching and Ordering, respec-
tively. Large models show a considerable improvement in their ability to handle diﬀerent question types.
Llama3.3-70B model performs best on most question types, especially MCQ, list matching, A&R and
IS. DeepSeek-3.2 performs best on MCQ, list matching, A&R shows good results compared to other
large-sized models in the category. Within MoE models, Qwen3-A3B performs best on MCQ, IS and ﬁll
in the blanks type questions. On the other hand, gpt-oss-120b shows the best results on list matching,
A&R, and ordering related questions. Closed-source models consistently outperform their open-source
counterparts. GPT-5, achieves best scores across almost all question categories, including MCQ, ﬁll in
the blanks, list matching, A&R and ordering. In contrast, Claude-4.5 demonstrates best performance
for IS questions. Grok4-fast performance is consistently lower than that of GPT-5 and Claude-4.5.
11
Performance on KR and LU questions
The trends observed in Table 9 and Table 10 show that accuracy improves consistently with increasing
model scale, with frontier models achieving the strongest results. As discussed in Section 4.3.1, general
knowledge tasks display steady but moderate gains, whereas Section 4.3.2 highlights far greater vari-
ability in language-speciﬁc tasks, reﬂecting the diﬃculty of deep multilingual grounding. Architectural
improvements, including MoE routing, enable mid-sized models narrow the performance gap with larger
systems.
12
Zero shot prompting template
In Table 8, we provide the zero-shot prompt used while evaluating all the models.

--- Page 15 ---\n\nSize
Model
MCQ
List Matching
A&R
Blanks
IS
Ordering
Small-size
Qwen2.5-3B
30.3
32.6
25.6
26.1
27.7
30.5
Llama3.2-3B
26.9
25.2
29.3
28.7
22.4
31.2
Gemma3-4b
28.7
27.6
30.8
28
27.5
28.7
Qwen3-4B
31.5
27.8
27.1
31.8
28.4
32.6
Medium-size
Aya-8b
29.1
28.9
32.3
34.4
25.5
27.9
Llama3.1-8B
30.5
23.2
32.7
35
24.4
27.6
Gemma3-12b
35.1
35.9
36.7
33.1
37.1
34.8
Mistral3.1-24b
35.7
34.3
27.1
33.8
35.8
37
Gemma3-27b
38.1
32.8
37.2
38.9
36.3
35.7
Large-size
Aya-32b
33.8
36.4
31.4
36.9
27.2
31.3
Qwen3-32B
34.6
24.6
32.8
29.9
31.9
29.8
Llama3.3-70B
37
39.7
41.6
34.4
40.7
38.1
DeepSeek-3.2
43.2
47.2
44.5
45.9
38
37.1
MoE
Qwen3-A3B
39.9
33.1
37.9
40.1
35.6
34
Llama-4-Scout
37.5
28.3
34.6
35
30.8
26.4
gpt-oss-120b
37.9
38
38.7
38.2
32.5
37.4
Closed
GPT-5
46.1
41.3
41.4
47.8
43.3
41.6
Grok4-fast
40.4
39.2
33.7
36.9
38.5
36.9
Claude-4.5
43.9
39
40
37.6
45.7
36.6
Gemini-2.5
57.2
65.6
55
59.5
58.5
51.4
Table 7: Question-type wise performance of all models on IndicParam.
Zero-Shot Prompting
Prompt = f"""Question:
{[’question_text’]}
Options:
A) {[‘option_a’]}
B) {[‘option_b’]}
C) {[‘option_c’]}
D) {[‘option_d’]}
The above question is written in {language} language. Please analyze the question and options carefully,
and select the correct answer. Respond ONLY with one letter (A, B, C, or D) corresponding to the correct
option. Do not provide any explanation or additional text.”’
Table 8: Zero-Shot prompt applied across all models for evaluation

--- Page 16 ---\n\nModel
Gujarati
Konkani
Maithili
Marathi
Oriya
Rajasthani
Sanskrit
Sans-Eng
Dogri
Nepali
Santali
Qwen2.5-3B
29.3
31.5
29.2
28.2
29.1
27.1
31.7
35.5
32.2
27.3
33.5
Llama3.2-3B
26.2
28.2
21.1
28.3
27.4
26.3
27.8
27.9
28
25.1
27.3
Gemma-3-4b
26.3
29.1
23.8
29.2
30.4
25.3
29.5
32.3
30.4
28.2
31.5
Qwen3-4B
27.3
29.3
31.5
29.7
32.6
27.4
34.5
33.6
35.6
28.9
33.9
Aya–8b
27.6
26.6
29
28.3
27.8
31.5
29.7
30.7
31.2
27.2
30.1
Llama-3.1-8B
27.3
29.1
27.9
31.8
28.9
29.3
32.4
34.2
25.9
24.6
30.4
Gemma-3-12b
33.9
35.5
29.7
37.5
33
32.6
39
43.1
36.7
34.8
33.5
Mistral3.1-24b
32.3
31.7
36.3
32.1
28
32.3
41.3
45.2
38
34.8
35.8
Gemma-3-27b
31.3
36
33.2
38.9
37.8
36.9
39.9
49.4
37.8
39.4
36.7
Aya-32b
28.4
32.5
31.7
32.5
28.3
33
36.3
40.6
35.3
32.5
35.5
Qwen3-32B
35.9
34.2
31.5
40
38.5
29.5
40.1
49.5
43.1
33.6
39.7
Llama-3.3-70B
33.6
37.2
35.2
42.7
39.3
36.6
42.8
52.1
37.5
35.8
39
DeepSeek-3.2
39.6
37.3
39.7
43.9
38.7
37.4
53.5
62.9
42.8
39.5
40.7
Qwen3-A3B
30.5
28.3
29.6
34.9
33.9
29.1
38.2
44.7
35.8
30.8
35.3
Llama-4-Scout
27.4
34.4
30
42.1
32.2
32.2
44.3
49.4
30
34
35.7
gpt-oss-120b
37
34.9
33.9
38.7
36.3
35.5
41.5
50.2
38.7
36.1
35.7
GPT-5
40.1
38.5
41.4
47.7
44.1
40.8
57.8
66.3
45.1
41.5
40.1
Grok-4-fast
35.9
37.1
36.5
38.8
38.3
37.1
45.2
55.9
39.9
40.6
38.1
Claude-4.5
37
41.9
40.3
42.9
39.8
39.7
48.8
59.5
44.9
43.4
40.3
Gemini-2.5
51.8
47.6
50.4
54.3
60.9
64
74.4
80.3
52.4
50.4
52.3
Table 9: Performance of models on knowledge related question category.
Model
Gujarati
Konkani
Maithili
Marathi
Oriya
Rajasthani
Sanskrit
Sans-Eng
Dogri
Nepali
Santali
Qwen2.5-3B
66.7
27.3
25.4
20.7
27.4
32.4
32.6
29.7
31.9
26.2
30.3
Llama3.2-3B
16.7
51.5
28.5
34.5
25.6
26.4
28.8
27.9
27.7
30.8
28.3
Gemma-3-4b
16.7
30.3
30.8
43.1
35.9
33.6
27.7
31.5
30.9
32.3
33.3
Qwen3-4B
50
39.4
33.1
46.6
42.7
36.7
30.7
33.3
29.8
27.7
33.3
Aya–8b
50
39.4
38.5
27.6
29.1
29.1
28.4
23.4
33
32.8
36.4
Llama-3.1-8B
16.7
45.5
39.2
39.7
30.8
38.2
31.4
32.4
28.7
29.7
32.3
Gemma-3-12b
16.7
42.4
49.2
56.9
40.2
41.5
29.5
31.5
39.4
34.9
35.4
Mistral3.1-24b
83.3
45.5
46.9
48.3
25.6
41.2
34.8
35.1
37.8
35.4
35.4
Gemma-3-27b
0
57.6
44.6
60.3
47.9
47.6
33.3
46.8
36.7
39
36.4
Aya-32b
33.3
57.6
46.2
46.6
31.6
38.8
31.1
27
34.6
35.4
36.4
Qwen3-32B
33.3
45.5
56.2
56.9
49.6
44.8
36
41.4
44.7
41
40.4
Llama-3.3-70B
16.7
42.4
57.7
58.6
44.4
42.4
37.5
47.7
36.2
43.1
48.5
DeepSeek-3.2
16.7
48.5
56.9
58.6
55.6
47
42.8
49.5
45.7
40.5
47.5
Qwen3-A3B
50
30.3
43.1
48.3
36.8
38.2
30.7
40.5
35.6
34.9
40.4
Llama-4-Scout
16.7
45.5
42.3
70.7
46.2
41.5
42.8
43.2
32.4
36.9
41.4
gpt-oss-120b
33.3
54.5
50.8
60.3
53.8
49.7
34.8
31.5
44.1
41.5
35.4
GPT-5
33.3
60.6
60.8
63.8
66.7
54.5
43.2
51.4
48.4
51.8
43.4
Grok-4-fast
33.3
51.5
52.3
60.3
50.4
44.2
33.7
40.5
41.5
42.6
44.4
Claude-4.5
33.3
51.5
60.8
63.8
60.7
55.8
43.6
46.8
44.1
45.6
41.4
Gemini-2.5
33.3
78.8
85.4
84.5
78.6
73.3
64.4
80.2
62.2
59
57.6
Table 10: Performance of models on language understanding (LU) question category.

--- Page 17 ---\n\n13
Examples questions in IndicParam
Table 11 presents examples of six distinct types of questions for each language used in IndicParam.
Question
option(a)
option(b) option(c)
option(d) Ans Type
Class Lang
1.बािलवधस्य
वणर्नमिस्त
रामायणस्य
सुन्दरकाण्डेिकिष्कन्धा
काण्डे
अरण्यकाण्डेबालकाण्डे
b
MCQ
G
san
2.'मिन्त्रपिरषदं
द्वादशामात्यान्कुवीर्त'
इित
कस्यमान्यता?
बाहर्स्पत्यानाम्कौिटल्यस्य
औशनसाम्
मानवानाम्
d
MCQ
G
san
3.अधोऽिडकतानां
समीचीनमुत्तरंिचनुत-
(a)
सरमा-पिण
1.
बृहदारण्यकोप-सम्वाद:
िनषत्
(b)
स्वाध्यायान्मा
2.
ऋग्वेदस्यप्रमदःदशममण्डले
(c)
कल्प:
3.
तैित्तरीयोपिनषत्
(d) आत्मनस्तु4. हस्त:
कामायसवर्ंिप्रयंभवित(a)
(b) (c) (d)
1 3 2 4
4 2 3 1
2 3 4 1
3 2 1 4
c
Order
G
san
4.भाशादीसभनेंथमांलौहकी
इकाइर्एे:
ध्विन
ध्विनग्राम
रूपग्राम
वाक्य
a
MCQ
L
doi
5.पैहूलीचंदीचिदत्तीगेिदयें
प्रिविष्टयाेंदादूइर्चंदीिदयें
प्रिविष्टयेंकन्नैस्हेइर्िमलानकरो
:
चंदी-1
चंदी-2
(अ) डोगरीकाव्य-चचार्(i) प्रो.
रामनाथशास्त्री
(ब)
परख-पड़ताल
(ii)
िशवनाथ
(स) डोगरीसािहत्यदाइितहास
(iii) प्रो. चम्पाशमार्
(द) बाबािजत्तो(iv) ओम
गोस्वामी
कोड: (अ) (ब) (स) (द)
(ii)
(i)
(iii) (iv)
(iv)
(ii)
(i) (iii)
(iii) (iv)
(ii) (i)
(i)
(iii)
(iv) (ii)
c
LM
G
doi
6.इकलड़ाइर्होर' ते'बंजर' दे
रचेतान:
मदन
मोहन
शमार्
ते
मोहनिंस˷ह
।
मोहनिंस˷ह
तेनरिंस˷ह
देव
जम्वाल।
मोहनिंस˷ह
ते
मदन
मोहन
शमार्।
िजतेन्द्र
शमार्
ते
दीनू
भाइर्
पंत।
c
Order
G
doi

--- Page 18 ---\n\n7.
બƀેયાદʋનીɳવગતોસર-
ખાવીસાચાંજાેડકાંબનાવો:
(a) શેષાɱદ્ર
(i) ɳવજયરાય
વૈદ્ય
(b) રામǟૃંદાવની
(ii) ɳત્રǚુ-
વનદાસǝુહાર
(c) ɳત્રǠુળ
(iii) રાજેન્દ્ર
શાહ
(d) મǜૂરાનંદ
(iv) ખબરદાર
(a) (b) (c) (d)
(i)
(iv)
(iii) (ii)
(iv) (iii)
(ii) (i)
(ii)
(iv)
(iii) (i)
(iii)
(ii)
(i) (iv)
b
LM
G
guj
8. નીચેનાંɳવધાનોનેકાયર્કાર-
ણસંબંધેતપાસો:
(A) 'વદતો˄ાઘાત' મધ્યમપ-
દલોપીસમાસછે.
(R)
મધ્યમપદલોપી
સમાસ
સવર્પદપ્રધાનછે.
(A)
અને
(R)
બƀે
સાચાંછે.
(A)
અને
(R)
બƀે
ખોટાંછે.
(A) સાǑું
છે
અને
(R)
ખોટુʡ
છે.
(A) ખોટુʡ
છે
અને
(R) સાǑૂં
છે.
b
A&R
G
guj
9.નીચેનામાંથીǢુસંગતɳવગત-
જૂથજણાવો:
વીસમી
સદʋ,
વૈƆાનર,
નટમંડળ
Ǐુજરાત
ɳવદ્યા-
સભા,
Ǐુજરાતી
સાɲહત્ય
પɱરષદ,
Ǐુજરાત
સાɲહત્ય
અકાદમી
ઊડણ
ચરકલડʊ,
સોયǗું
નાકુʡ,
મનીષા
ખીચડʊ,
અંત:Ƌોતા,
આવતી-
કાલનો
Ǣૂરજ
b
MCQ
G
guj
10.फावो
तो
पयार्य
वेंचून
काडूनवाक्यपूणर्करात.
सोळाव्या
शेंकड्यातल्या
रामायणाच्याहातबरपांत
ठांयींठांयीं
पुतुर्गेज
उतरां
मेळटात.
कांयच
पुतुर्गेज
उतरां
मेळनात.
संस्कृत
उतरां
भरसून
पुतुर्गेजीक
काेंकणीची
सया
मारता.
देशीआनी
अपभ्रंशी
भारतीय
भासो
मेळटात.
b
Blank
ﬁll-
ing
G
gom
11.भाशीकनादांचोभाशेचे
बांदावळीचे
नदरेंतल्यान
अभ्यासकरपीव्याकरणाक
िकतेंम्हणतात?
अथर्िवज्ञान
नादिवज्ञान
वाक्य-
िवचार
स्वनीम-
िवचार
d
MCQ
G
gom
12.
काळोिकट' होसमास
हांतलोखंयचो?
उपमावाचक
कमर्धारय
समास
िवशेशण
उभयपद
समास
द्वंद्वसमास
बहुिव्रिह
समास
b
MCQ
L
gom
13. हुनकासँभेंटभेलछल'
िलखनेछिथ
मिणपद्म
अमर
सुमन
मधुप
a
MCQ
G
mai
14. "िशवकी..... िवषपचाय
यिदिलतिथनिहमाथे।"
देिखतिथ
बुिझतिथ
किरतिथ
सिकतिथ
d
Blank
ﬁll-
ing
G
mai
15.
एकावलीपिरणय' में
अंगीरसअिछ
शान्त
अद्भुत
हास्य
श्रृंगार
d
MCQ
L
mai

--- Page 19 ---\n\n16. पुढीलपैकीकोणतेनाटक
िवजयतेंडुलकरयांनीिलिहले
नाही?
गृहस्थ
सूयार्स्त
बेबी
श्रीमंत
b
MCQ
G
mar
17.
पुढीलपैकी
कोणती
कादंबरीएेितहािसकनाही?
वज्राघात
कािलकामूिर्त˷ सावळ्या
तांडेल
दुदैर्वीरंगू
b
IS
G
mar
18.
पुढीलसािहत्यकृतींचा
कालानुसारक्रमलावा.
धग,
िकडलेली
माणसे,
औदुंबर,
स्मृितिचत्रे,
िकडलेली
माणसे,
औदुंबर,
स्मृितिचत्रे,
धग,
धग,
औदुंबर,
स्मृितिचत्रे,
िकडलेली
माणसे,
औदंबर,
स्मृितिचत्रे,
िकडलेली
माणसे,
धग,
d
Order
G
mar
19.
शास्त्रीयमाक्सर्वादी
दृिष्टमाआइिडयोलजीभन्नाले
केबुिझन्छ?
भ्रमपूणर्
चेतना।
सैद्धािन्तक
आस्था
प्रचिलत
िवचारधारा
।
पुस्तकहरू
पढेरपाइने
ज्ञान।
a
MCQ
G
nep
20.
वाक्यमाशब्दहरूमाझ
रहनेसम्बन्धलाइर्केभिनच्छ?
िवन्यासक्रमी
सम्बन्ध।
सहचारक्रमी
सम्बन्ध।
व्यितरेकी
सम्बन्ध।
परस्परव्यािप
सम्बन्ध।
a
MCQ
L
nep
21. नेपालीभाषामाप्रयोगहुने
'चोलो',
'पटुका',
'मुन्धुम',
'बाउसे' शब्दहरूकुनभाषा
पिरवारबाटआएकाहुन्?
भारोपेली
।
भोट-
बमेर्ली
।
आग्नेय।
द्रिवड़।
b
MCQ
L
nep
22.
"राजस्थानीभाषारौ
िवगसावनागरअपभ्रंशसूंहुयौ
है।" ओकथनहै-
डॉ.
एल.पी.
टेिस्सटोरी
डॉ.
िग्रयसर्न
डॉ.
सुनीितकुमार
चटजीर्
डॉ.
सुकुमार
सेन
b
MCQ
G
Raj
23.
राजस्थानीअनुवादरी
दीठसूंिकसौअनुवादरौजोड़ौ
गलतहै?
गांधीजीरी
आत्मकथा
-
आइर्दानिंस˷ह
भाटी
भरथरी
शतक
-
मनोहर
शमार्
मेघदूत
-
नारायणिंस˷ह
भाटी
रचाव
-
चेतन
स्वामी
d
IS
G
Raj
24. बुगचौ' सबदरौसहीअथर्
है:
लुगाइयां
रै
कपड़ा
राखणरौ
कपड़े
रौ
थेलौ
लुगाइयां
रीलकड़ी
रीपेटी
लुगाइयां
री
कपड़ा
राखणरी
लोह
री
पेटी
मड़दां
रै
कपड़ा
राखणरी
लकड़ीरी
पेटी
a
MCQ
L
Raj
25.
सिहकदािचद्वाच्ये
िविधरूपेप्रितषेधरूपः' अत्रस
इत्यनेनकोऽिभप्रेतः?
वाच्याथर्ः
लक्ष्याथर्ः
व्यङ्गाथर्:
तात्पयार्थर्ः
c
MCQ
L
sans-
mix
26. कौषीतिकउपिनषद्कस्य
वेदस्यअिस्त?
कौषीतिकउपिनषद्िकसवेद
कीहै?
Of
which
Veda
is
कौषीतिकउपिनषद्?
अथवर्वेदस्यसामवेदस्य
ऋग्वेदस्य
कृष्णयजुवेर्
दस्य
c
MCQ
G
sans-
mix

--- Page 20 ---\n\n27.
अधोिलिखतेषुकेनसह
कस्यसम्बन्धः?
उिचतां
तािलकांिचनुत-
(a)
सत्कायर्वाद:
(i)
न्यायवैशेिषकाणाम्
(b)
परमाणुवादः
(ii)
बौद्धानाम्
(c) िववतर्वादः(iii) संख्यानाम्
(d)
िवज्ञानवाद:
(iv)
अद्वैतवेदािन्तनाम्
(a) (b) (c) (d)
(iii)
(ii)
(i) (iv)
(iii) (iv)
(i) (ii)
(iii)
(i)
(iv) (ii)
(iii)
(i)
(ii) (iv)
c
LM
G
sans-
mix
28. सेदायहापड़ामकोकाथा
लेकाते
होड़
होपोनकोवाक्
पािरसदोओकोजायगारेको
हािटजलेदा?
चाम्पा
चाय
सासाडबेडा
जारपी
c
MCQ
G
sat
29.
लाताररेओलआकान
थािपतकाथा(A) आरओजे
(R)
रेनाक्
ओका
गादेल
बाड़तीसुिहया?
थािपत(A) : भारतीयनोजोर
तेगायानसाँवहेतुदोसुकरे
मुच़ातलाकतीयाना।
ओजे(R) : चेदाक्जेनोवा
काथाहाेंपिछमिदसोमरेन
साँपहेतुिहया
नोजोर
ते
हाें
नापाया।
(A)
आर
(R)
बाङसुहीया
(A)
सुहीया,
(R)
बाडसुहीया
(A)
बाडसुहीया,
(R)
सुहीया
(A)
आर
(R) बानार
सुहीया
d
A&R
G
sat
30.
ओकापारसीघाराेंचू
रेनाक्ओकापारसीकाना?
ओनासुहीिमलावमें।
सूची- I
सूची- II
a.आयर्भाषापिरवार
1.
ितब्बती
b. अग्नेयभाषापिरवार
2.
माल्तो
c. द्रािवड़भाषापिरवार
3.
मुण्डा
d.
चीनीभाषापिरवार
4.
बंगला
कूट: a b c d
1 2 3 4
4 3 2 1
3 1 4 2
2 4 3 1
b
LM
G
sat
31.
ମୁକୃ
ଅକ୍ଷରେଶଷେର
କଣଥାଏ?
ଅକ୍ଷର
ସୂରଧୂନି
ବ୍ୟęନଧୂନି
ସୁକƅ ଧୂନି
b
MCQ
L
ory
32.
}କାଶକାଳଅନୁଯାୟୀ
ଉପଯୁú ̾ମନିĴର୍ାରଣକର
।
ଉଷା,
ଚିଲିକା,
ପାବର୍ତୀ,
ମହାଯାxା
ଚିଲିକା,
ଉଷା,
ପାବର୍ତୀ,
ମହାଯାxା
ପାବର୍ତୀ,
ଚିଲିକା,
ଉଷା,
ମହାଯାxା
ଉଷା,
ପାବର୍ତୀ,
ଚିଲିକା,
ମହାଯାତ୍।
d
Order
G
ory
33.
େକଉଁଟି
େବ୍ୟାମେକଶ
xିପାଠୀĊ ନାଟକନୁେହଁ?
ସିଂହĶାର
ଜାଗରଣ
ମୁଠାଏମାଟି
ସୁନାଫର
ୁ
ଆ
c
IS
G
ory

--- Page 21 ---\n\n34.
बाहायनानेगाहायाव
होनाय
मेथाइफोरिन
बाहायजानाय
सम
फािर
साजायनायखौसायख-
I. बैसागोमेथाइ
II. दोहोरोमिसिबनायमेथाइ
III. बेलाड
IV. मैंगंखानायावखननाय
मेथाइ
II III IV I
III II I IV
IV III I II
I II IV III
b
Order
G
brx
35. अलंबार' लाइिसखौसोर
सुजुदाेंमोन
मदाराम
ब्रह्म
सुकुमार
बसुमतारी
सितस
चन्द्र
बसुमतारी
प्रम'द
चन्द्रब्रह्म
d
MCQ
G
brx
36. गाहायिनबुंफोरनाय(A)
आरोजाहोन(R) खौगेबेंना
गोरोिन्थबाहायनानैसायख:
बुंफोरनाय(A) : आिथखालाव
मोननायबािसरामजोहोलाव
बेलाडखौथारैआबुंबेलाडएबा
natural ballad बुंथावा।
जाहोन(R) : मानोनाबेबेलाडा
िलरनायमहरावफोसावजानाय
।
(A)-आराें
(R)
मोननैबो
गेबें
(A)-आ
गेबें
आरो
(R)-आ
गोरोिन्थ
(A)
आरो(R)
मोननैबो
गोरोिन्थ
(A)-आ
गोरोिन्थ
आरो(R)
आगेबें
b
A&R
G
brx
Table 11: Sample questions from all languages in IndicParam along with their options, answers, question types, and
question classes, with languages indicated using ISO-639 codes. We use Order to denote ordering-type questions,
and the abbreviations G and L refers to General Knowledge (GK) and Language Understanding (LU) questions
respectively.
\n```\n