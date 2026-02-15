---
title: "2025-Cheng-HKCanto-Eval A Benchmark for Evaluating Cantonese Language - PDF Extract"
source_pdf: "2025-Cheng-HKCanto-Eval A Benchmark for Evaluating Cantonese Language.pdf"
pages: 25
extracted_at: "2026-02-15T17:51:59.250219"
---

# PDF Extract: 2025-Cheng-HKCanto-Eval A Benchmark for Evaluating Cantonese Language

**Source PDF:** 2025-Cheng-HKCanto-Eval A Benchmark for Evaluating Cantonese Language.pdf
**Total Pages:** 25

---

## Content

```
--- Page 1 ---

arXiv:2503.12440v2  [cs.CL]  6 Jul 2025
HKCanto-Eval: A Benchmark for Evaluating Cantonese Language
Understanding and Cultural Comprehension in LLMs
Tsz Chung Cheng1, Chung Shing Cheng2, Chaak Ming Lau3,
Eugene Tin-Ho Lam5, Chun Yat Wong4, Hoi On Yu5, Cheuk Hei Chong6,7
1 Kyushu University, 2 hon9kon9ize, 3 The Education University of Hong Kong,
4 The University of Hong Kong, 5 Independent Researcher, 6 Votee AI, 7 Beever AI
Correspondence: Tsz Chung Cheng: jed.cheng@mag.ed.kyushu-u.ac.jp,
Chung Shing Cheng: joseph.cheng@hon9kon9ize.com Chaak Ming Lau: lchaakming@eduhk.hk
Abstract
The ability of language models to comprehend
and interact in diverse linguistic and cultural
landscapes is crucial. The Cantonese language
used in Hong Kong presents unique challenges
for natural language processing due to its rich
cultural nuances and lack of dedicated evalua-
tion datasets. The HKCanto-Eval benchmark
addresses this gap by evaluating the perfor-
mance of large language models (LLMs) on
Cantonese language understanding tasks, ex-
tending to English and Written Chinese for
cross-lingual evaluation. HKCanto-Eval inte-
grates cultural and linguistic nuances intrin-
sic to Hong Kong, providing a robust frame-
work for assessing language models in real-
istic scenarios. Additionally, the benchmark
includes questions designed to tap into the
underlying linguistic metaknowledge of the
models. Our findings indicate that while pro-
prietary models generally outperform open-
weight models, significant limitations remain
in handling Cantonese-specific linguistic and
cultural knowledge, highlighting the need
for more targeted training data and evalua-
tion methods. The code can be accessed at
https://github.com/hon9kon9ize/hkeval2025
1
Introduction
Recent advancements in large language models
(LLMs) such as GPT-4, Gemini, and various open-
weight models have demonstrated remarkable ca-
pabilities in natural language understanding across
multiple languages (Xu et al., 2024). However,
the performance of most models significantly de-
clines when applied to languages other than En-
glish, yielding particularly poor outcomes for low-
resource languages (LRLs). These languages are
under-represented lingua francas that play a crucial
role in certain communities, and it is imperative to
improve multilingual support for LRLs by creat-
ing benchmarks to guide the future development
of multilingual LLMs. Since they are poorly sup-
ported due to the lack of training data, if there is a
close language with more resources, this problem
can potentially be mitigated through few-shot learn-
ing. A notable example of this strategy is the use
of Bahasa Indonesian to handle regional languages
in Indonesia (Aji et al., 2022; Winata et al., 2022).
This strategy aligns with the spirit of language sus-
tainability and AI support for marginalised commu-
nities (Du et al., 2020), which is also applicable to
Cantonese.
This paper investigates the status of LLM sup-
port for Cantonese (ISO 639-3: yue), a member of
the Sinitic (“Chinese”) branch of the Sino-Tibetan
language family, and a distinct variety unintelli-
gible to users of Mandarin, the standard variety
of Chinese used in Mainland China (Pˇut¯onghuà)
and Taiwan (Guóyˇu). Cantonese, spoken by over
85 million people according to Ethnologue (Eber-
hard et al., 2024), serves as the most common
and de facto official language of Hong Kong and
Macau, and is also widely used in parts of Guang-
dong, Guangxi, Malaysia, and Singapore. Addi-
tionally, it is used as a diasporic language in coun-
tries such as Canada (Sachdevl et al., 1987), the
United States (Leung and Uchikoshi, 2012), Aus-
tralia (Zhang et al., 2023), and the United King-
dom (Bauer, 2016; Tsapali and Wong, 2023). De-
spite its widespread use, Cantonese is still consid-
ered a low-resource language (Xiang et al., 2024)
due to the lack of quality written resources. This
scarcity results from a “diglossia" that requires
Written Chinese (which resembles Mandarin) to
be used in formal settings1, and a longstanding,
ideologically-driven stigmatisation of Cantonese as
an informal/vulgar language (Lau, 2024), further
confines written Cantonese to informal contexts
1Even in Mandarin-like Written Chinese, there are per-
sistent lexical differences with other regions due to vastly
different governmental, legal and education systems. For in-
stance, the word “taxi” is rendered as “
” in mainland
China, “
” in Taiwan, and “
” in Hong Kong and
Macau.
1

--- Page 2 ---

like social media and texting.
Cantonese is partially supported by certain
LLMs, with models like GPT-4 and Gemini ca-
pable of comprehending and responding in Can-
tonese (Fu et al., 2024; Hong et al., 2024; Jiang
et al., 2024). There are models dedicated to better
supporting Chinese languages and dialects: The
Hong Kong government is developing an inter-
nal tool based on locally developed LLMs for ad-
ministrative use (Yiu, 2024); SenseTime released
SenseChat (Cantonese), a model trained on 6 bil-
lion tokens of Hong Kong-specific data (Sense-
Time, 2024). However, the current support level
is mostly contributed to by small pockets of Can-
tonese presented in the sheer volume of Written
Chinese training data. There have been compar-
isons between Chinese and Western models on how
well languages spoken in China are handled (Wen-
Yi et al., 2025), showing that Chinese models out-
performed Western ones on Mandarin, but the same
cannot be said for Cantonese or other languages
in China. The following section outlines how cur-
rent benchmarking studies have yet to provide a
comprehensive evaluation for Cantonese and Hong
Kong-related tasks that tap into the in-depth rep-
resentation of underlying aspects of the language,
which we believe is the prerequisite for accurate
comprehension in uncommon scenarios.
2
Related Benchmarks
The development of LLMs has spurred signifi-
cant research into evaluating their performance and
comparing their capabilities to human reasoning
across general and domain-specific tasks. A promi-
nent benchmark in this area is the MMLU dataset
(Hendrycks et al., 2020), which comprises 57
tasks ranging from elementary to university-level
multiple-choice questions. Despite its widespread
use, MMLU has been criticised for containing
flawed questions and answers (Gema et al., 2024;
Gupta et al., 2024). To address these shortcomings,
alternative benchmarks such as BIG-Bench (Sri-
vastava et al., 2022), MMLU-Pro (Taghanaki et al.,
2024), and MMLU-Pro+ (Wang et al., 2024) have
been introduced, aiming to improve accuracy while
presenting more diverse and challenging questions.
In addition to comprehensive benchmarks, re-
searchers have developed domain-specific, expert-
curated datasets to evaluate the reasoning capabili-
ties of LLMs in specialised fields such as program-
ming (HumanEval (Chen et al., 2021); NL2Code
(Zan et al., 2022)) and mathematical reasoning
(GSM8K (Cobbe et al., 2021); MATH (Hendrycks
et al., 2021); MATH 401 (Yuan et al., 2023); Omni-
MATH (Gao et al., 2024)).
Although most existing LLM benchmarks fo-
cus on English-language tasks, culturally-aware
datasets integrating machine-translated questions,
native datasets, and exam questions have been de-
veloped in other languages, including Arabic (Koto
et al., 2024), Basque (Etxaniz et al., 2024a,b), Span-
ish (Plaza et al., 2024), Indic languages (Verma
et al., 2024), and Korean (Son et al., 2024). Simi-
lar benchmarks have been published for Chinese,
such as CMMLU (Li et al., 2023) and C-Eval
(Huang et al., 2024) that gathered questions from
various academic and professional exams in main-
land China, and TMLU (Chen et al., 2024) and
TMMLU+ (Tam et al., 2024) that evaluate knowl-
edge in Traditional Chinese in the context of Tai-
wan.
These benchmarks are not applicable to the
Hong Kong context due to the aforementioned
diglossia and regional lexical differences.
Re-
cently, Jiang et al. (2024) introduced a Cantonese
evaluation benchmark that combines four datasets
translated from other languages (ARC, GSM8K,
CMMLU, and Truthful-QA)2, resulting in a dataset
that is heavily biased towards American culture
(16.9% entries in the Truthful-QA dataset refer-
ence the United States) or mainland Chinese exams
(CMMLU) (see Appendix A).
3
Methodology
HKCanto-Eval introduces a specialised benchmark
to address the lack of systematic tests for evalu-
ating the Cantonese capabilities and Hong Kong
knowledge of an LLM in these aspects: (1) Lan-
guage Proficiency, the capability in an accurate
and nuanced understanding of Cantonese and local-
flavoured Written Chinese, as well as generating
fluent, idiomatic, genre-appropriate Cantonese text
in question and answering, translation, and sum-
marisation tasks; (2) Cultural Knowledge, in-
depth knowledge about not only general historical
and geographical facts related to Hong Kong, but
also everyday practices, local customs, beliefs and
values, and cultural references from movies, music,
literature, and internet culture; (3) Reasoning and
2It also contains a translation evaluation component for
English-Cantonese and Simplified-to-Traditional Chinese
translations, but its data sources and evaluation methods are
not fully transparent.
2

--- Page 3 ---

Figure 1: Diagram showing the tasks of the HKCanto-Eval Benchmark
Problem-Solving, reasoning and problem-solving
skills within a Cantonese and/or Hong Kong-based
context, including reasoning about the sound and
written forms of the language.
These aspects are incorporated into the five
datasets outlined below.
3.1
Translated MMLU Dataset
The first dataset comprises 14,042 questions from
the original MMLU dataset in English (Hendrycks
et al., 2020) and their Cantonese translation3. This
allows us to compare how LLMs perform when
handling knowledge in a wide range of subjects in
Cantonese rather than in English (See Appendix
B).
3.2
Academic and Professional Dataset
The Academic and Professional Dataset is a set
of multiple-choice questions curated to measure
LLMs’ reasoning and problem-solving abilities in
domain-specific knowledge. The dataset contains
multiple-choice questions from 3 sub-categories:
(1) Academic: Questions sourced from Hong Kong
Diploma of Secondary Education (HKDSE), a
territory-wide high-school graduate-level exam; ex-
tracted and manually corrected from scanned PDFs
and are believed to have never appeared online in a
3The translation was done by the Google Gemini 1.5 Flash
API, which offers a balance between top performance and cost
as one would find in the later section. To address concerns
regarding the accuracy of LLM translation, we have selected
4 questions from each category for human checking. 202 out
of 228 sentences were judged to be good by the raters.
plain-text form; (2) Professional: Questions from
seven professional qualification exams, extracted
from text PDF files found on the corresponding of-
ficial sites (in which the model answers were not on
the same page as the questions, avoiding data con-
tamination concerns), and an additional set of Taxi
Licensing Exam Styled Route Planning questions
on Hong Kong roads and geographical features; (3)
Law: Questions about law in Hong Kong across
15 categories sourced from the Internet, and an
additional subset of the Basic Law edited by the
authors.
All questions are in Written Chinese (in the Tra-
ditional script). We also included an English ver-
sion if it is available. The details of this dataset can
be found in Appendix C.
3.3
Hong Kong Cultural Questions Dataset
This dataset contains 277 manually crafted ques-
tions divided into five categories that capture cul-
tural knowledge common to people who have lived
or grown up in Hong Kong, that are often not
learned in schools. The categories are Food Cul-
ture, History and Landmarks, Language and
Expressions, Life in Hong Kong and Local Area
Knowledge. The questions were collected in a
way to capture knowledge from all walks of life.
244 questions were developed by the authors and
volunteers for the first four categories, and the last
category comes from an online quiz. Questions
were created so that they were non-trivial and at
the same time not too obscure, and have been ver-
3

--- Page 4 ---

ified by all the authors. Details can be found in
Appendix D.
3.4
Linguistic Knowledge Dataset
This is an assessment of the linguistic knowledge
represented in the models, inspired by the approach
of PhonologyBench (Suvarna et al., 2024) for En-
glish. To our knowledge, this innovative approach
has never been incorporated into existing Can-
tonese or Chinese benchmarks in general.
3.4.1
Phonological Knowledge
The dataset contains 100 questions that evalu-
ate phonological knowledge about characters and
words of an LLM, including the judgment of homo-
phones and rhyming and other non-trivial reasoning
tasks based on word pronunciation. These are par-
ticularly important in the Cantonese context, as the
writing system does not provide reliable cues about
the pronunciation of words, and Cantonese mate-
rials are not accompanied by sound transcription.
This knowledge needs to be present in the training
data for tasks that require sound-related operations
or reasoning (See Appendix E.1).
3.4.2
Orthographic Knowledge
The Orthographic Knowledge Dataset evaluates
the character meta-knowledge of an LLM. Can-
tonese users from Hong Kong need to know around
4,000 characters by the age of 12 and will have
built sound knowledge about the representation of
the characters. This subset contains 100 questions
about the strokes, structure, arrangement, and radi-
cal and constituent components of common charac-
ters. Cantonese uses the Traditional Chinese script
(ISO 15924: Hant) in Hong Kong and Macau, and
the script is also used in Taiwan. There could be
influence from Mandarin data or Taiwan usage not
shared by Cantonese. It is also expected that cer-
tain models may produce incorrect answers due to
the over-reliance on simplified Chinese data (See
Appendix E.2).
3.4.3
Grapheme-to-Phoneme (G2P)
Conversion
This dataset addresses the task of converting a
string of written text represented in Traditional Chi-
nese characters into Jyutping, a widely adopted ro-
manisation standard of Cantonese4. This is similar
to typical G2P tasks except that Jyutping is used in-
stead of the International Phonetic Alphabet (IPA)
4https://lshk.org/jyutping-scheme
as the output. G2P functionalities have been imple-
mented by PyCantonese (Lee et al., 2022), a Can-
tonese NLP package, Hambaanglaang Converter5
and Visual Fonts6. As the task is non-deterministic,
rule-based conversions are bound to be unreliable
(although Visual Fonts have achieved very high
accuracy now). There is also no reliable non-rule-
based G2P system to our best knowledge. This
part of the dataset contains 150 pairs of Character-
Jyutping sentences from both Standard Written
Chinese and Cantonese and in a range of formal-
ity levels, manually checked by professional lin-
guists from the Linguistic Society of Hong Kong,
the organisation that established and maintains the
Jyutping system. The score calculation method is
discussed in Appendix E.3.
3.5
NLP Tasks Dataset
Multiple-choice questions offer a structured ap-
proach to assess LLM factual knowledge and rea-
soning, but they are insufficient for evaluating
real-world language understanding and generation.
Open-ended tasks, including translation and sum-
marisation, were incorporated.
A translation dataset comprising 20 Cantonese
sentences with complex linguistic nuances was
created, with each sentence manually translated
into English and written Chinese (resulting in 4
translation pairs per sentence) (See Appendix F).
For summarisation, 10 Cantonese articles and 10
TED talk subtitles were used. The importance of
transcription-based summarisation, reflecting Can-
tonese’s prevalence in oral communication, is em-
phasised by the inclusion of TED talks (See Ap-
pendix G).
Performance on traditional NLP tasks like senti-
ment analysis was also evaluated. Leveraging the
OpenRice dataset (toastynews, 2020) (restaurant re-
views categorised as positive, neutral, or negative),
1200 reviews (avg. 309 characters) with a balanced
sentiment distribution were included. Additionally,
a new dataset of 399 Facebook comments (avg. 24
characters), labelled by paid interns, was created
(See Appendix H).
3.6
Evaluation Method
The evaluation process of multiple-choice ques-
tions follows the standard 5-shot evaluation pro-
cedures in MMLU formulation. However, for the
Hong Kong Cultural Questions Dataset, a zero-shot
5https://test.hambaanglaang.hk
6https://visual-fonts.com
4

--- Page 5 ---

evaluation was also conducted to emulate actual us-
age. The translated MMLU dataset used the same
system prompt as the original MMLU dataset. For
other multiple-choice questions, a short sentence
with the name of the exam or question subcategory
is added.
For the G2P dataset, character error rates (CER)
and Levenshtein distance were both used to calcu-
late the discrepancy between the model output and
the gold standard in a five-shot evaluation. The
summarisation tasks were evaluated without any
example to avoid exceeding the context length of
any model, while zero and three-shot evaluations
were carried out for the translation task.
The outputs of both translation and summari-
sation evaluation were evaluated and graded by
paid undergraduate students and teaching assistants.
The rubric can be found in Appendix F and G. As
technology improves, future LLMs can perform
the task to offer scalability. Nonetheless, the re-
sults from this human evaluation will be useful for
verifying the validity and consistency of LLM-as-
a-judge in the future.
3.7
Model Selection
13 model families were selected for evaluation. Pro-
prietary models including OpenAI GPT4o (Hurst
et al., 2024) and GPT4-mini (OpenAI, 2024),
Google Gemini 1.5 Flash and Gemini 1.5 Pro
(Gemini Team et al., 2024) and Anthropic Claude
3.5 Sonnet (Anthropic, 2024) were selected for
their reported superior performance across differ-
ent languages.
Three proprietary models from Chinese com-
panies, including Doubao Pro from ByteDance
(Doubao, 2024), Erne 4.0 from Baidu (Baidu Inc.,
2023) and SenseChat (Cantonese) from SenseTime
(SenseTime, 2024), were also incorporated. All
proprietary models were accessed through their
API, except SenseChat, which was accessed via the
web interface due to a failure to get verified to use
their API.
Popular multilingual open-weight models includ-
ing Aya 23 8B (Aryabumi et al., 2024), Gemma 2
2B, 9B and 27B (Gemma Team et al., 2024), Llama
3.1 8B, 70B and 405B (Dubey et al., 2024), and
Mistral Nemo Instruct 2407 12B (Mistral, 2024)
were included to assess their cross-lingual ability.
The collection also included two open-weight mul-
tilingual models from Chinese companies, Yi 1.5
6B, 9B and 34B (Young et al., 2024) and Qwen2
7B and 72B (Yang et al., 2024). In addition, Can-
toneseLLM (CLLM) v0.5 6B and 34B7 are two of
the few open-weight models trained specifically on
Cantonese data. They were trained by fine-tuning
Yi 1.5 6B and 34B models with around 400 million
tokens of Hong Kong-related content. Open-weight
instructions fine-tuned models smaller than 70B pa-
rameters were evaluated using Nvidia H100 GPUs.
The 70B and 405B models were evaluated using
the API of SiliconFlow8.
4
Results
4.1
MMLU
Table 1 shows the results of the multiple-choice
questions. Proprietary models and open-weight
models like Llama 3.1 70B, 405B, and Qwen 2
72B performed well in MMLU, but experienced
an average of 7.46 percentage point drop when
questions were in Cantonese. Considering potential
errors from machine translations, this is evidence of
Cantonese reasoning and problem-solving ability.
4.2
Academic and Professional Questions
The results of this dataset showed expected
problem-solving abilities across models in differ-
ent subject areas, in particular, general weaknesses
in handling secondary school-level mathematics
and strong performance in legal questions. Pro-
prietary models generally performed better than
open-weight models. The sub-scores in the in-
dividual tasks show that most models struggled
with academic questions that were never posted
online. It is worth noting that some open-weight
models (e.g. CLLM v0.5 34B and Qwen2 72B)
outperformed most models, and we can conduct
further investigation on what additional training
data was used to achieve this performance. Writ-
ten Chinese yielded better overall results, and this
is attributed to the Law dataset, which only came
in Chinese. Discounting this set, Written Chinese
caused a slight drop in performance. This indi-
cates that multi-lingual open-weight LLMs showed
cross-lingual capabilities, maintaining similar per-
formance across both languages.
4.3
Hong Kong Cultural Questions
Proprietary models and Qwen 2 72B showed a good
understanding of Hong Kong cultural knowledge,
yet none of the models performed well across the
7https://huggingface.co/hon9kon9ize/CantoneseLLMChat-
v0.5
8https://siliconflow.cn
5

--- Page 6 ---

MMLU
Academic &
Professional
Cultural
Average
Model
EN
YUE
EN
ZH
0-shot
5-shot
EN
ZH/YUE
Claude 3.5 Sonnet
85.0%
81.5%
75.1%
75.2%
71.7%
75.0%
80.1%
75.8%
Doubao Pro
79.8%
74.2%
60.8%
70.5%
70.7%
75.0%
70.3%
72.6%
Ernie 4.0
81.0%
75.2%
70.4%
72.4%
68.2%
75.2%
75.7%
72.8%
Gemini 1.5 Flash
79.0%
73.1%
67.4%
68.3%
61.0%
64.0%
73.2%
66.6%
Gemini 1.5 Pro
83.2%
77.6%
71.0%
71.7%
74.0%
73.8%
77.1%
74.3%
GPT4o
84.8%
80.3%
77.6%
75.3%
77.5%
77.2%
81.2%
77.6%
GPT4o-mini
76.7%
69.4%
62.0%
65.6%
55.6%
60.6%
69.4%
62.8%
SenseChat
78.7%
70.1%
73.6%
75.6%
67.4%
77.4%
76.1%
68.8%
Aya 23 8B
56.6%
47.1%
44.8%
49.0%
39.5%
37.7%
50.7%
43.3%
CLLM v0.5 6B
58.6%
51.7%
50.9%
53.5%
52.0%
56.1%
54.7%
53.3%
CLLM v0.5 34B
75.9%
69.9%
66.8%
69.9%
72.5%
76.7%
71.3%
72.3%
Yi 1.5 6B
64.1%
54.0%
53.7%
58.3%
47.7%
50.7%
58.9%
52.7%
Yi 1.5 9B
70.9%
60.8%
59.2%
63.3%
48.7%
57.3%
65.0%
57.5%
Yi 1.5 34B
76.1%
68.5%
63.7%
68.7%
67.7%
72.9%
69.9%
69.5%
Gemma 2 2B
58.5%
46.5%
45.3%
48.5%
33.3%
35.2%
51.9%
40.9%
Gemma 2 9B
73.4%
64.3%
63.6%
64.0%
49.1%
51.6%
68.5%
57.3%
Gemma 2 27B
76.4%
68.4%
65.1%
68.1%
57.1%
60.9%
70.7%
63.6%
Llama 3.1 8B
69.0%
56.4%
51.4%
57.1%
45.6%
52.7%
60.2%
52.9%
Llama 3.1 70B
80.3%
74.9%
68.2%
70.0%
63.0%
64.4%
74.2%
68.1%
Llama 3.1 405B
84.5%
78.4%
70.9%
74.2%
67.9%
69.9%
77.7%
72.6%
Mistral Nemo 12B
68.8%
58.4%
54.6%
58.0%
40.1%
42.7%
61.7%
49.8%
Qwen2 7B
71.2%
64.8%
60.7%
65.4%
53.6%
54.8%
66.0%
59.6%
Qwen2 72B
82.9%
78.3%
74.7%
76.3%
72.9%
77.7%
78.8%
76.3%
Random
25.0%
25.5%
22.9%
24.6%
29.8%
28.1%
23.9%
27.0%
Table 1: Model performance on MMLU, Academic and Professional, and Cultural questions. Note that SenseChat
refused to answer one subset of questions in Cultural Question 5-shot evaluation.
subcategories. Looking into the sub-scores, mod-
els occasionally matched humans in most sub-tests
(e.g. Food Culture and Life in HK ). However,
when inspecting the results, good performance by
percentage only reflects the size of existing Hong
Kong knowledge represented in Wikipedia entries.
For example, only two models (Yi 1.5 6B and
Qwen2 72B) correctly answered the origin of De-
mae Itcho noodles sold in Hong Kong, while 94%
of humans did. The results for Language & Ex-
pressions also show that most models did not have
a nuanced understanding of Cantonese.
Com-
pared to human performance at 85.8%, SenseChat
scored the highest point out of all models in 5-
shot (79.6%), but its performance dropped signif-
icantly in zero-shot (61.4%). In zero-shot evalu-
ation, CLLM v0.5 34B delivered the best perfor-
mance at 77.3%. Furthermore, model size affects
the performance of geospatial tasks, with open-
source models in the 6-9B parameter range achiev-
ing only about 50% of larger models’ performance
on Local Area Knowledge (e.g. Yi 1.5 34B 67.9%,
9B 35.7%). The overall results of this dataset sug-
gest that Hong Kong cultural knowledge is under-
represented in LLM training. See Appendix C for
details.
4.4
Linguistic and NLP Tasks
These two groups of tasks reveal the representa-
tion of Cantonese phonological, orthographic, lex-
ical and grammatical knowledge in existing mod-
els. The overall results (Table 2) show a consistent
trend where proprietary models outperformed open-
weight models (but more pronounced in linguistic
tasks). GPT-4o led with 76.7% and 89.6% in both
linguistic and NLP tasks. Lower scores are often
due to chance-level performance when knowledge
is absent, or below chance-level due to influence
from Mandarin. Here are the key findings and ob-
servations:
Most LLMs understand Cantonese fine. Most
6

--- Page 7 ---

Phonological Knowledge
Orthographic Knowledge
NLP
Model
Homo-
phone
Rhyme
Misc.
Visual
Sim.
Canton.
Char.
Misc.
Avg.
Claude 3.5 Sonnet
28.0%
64.0%
16.0%
50.0%
76.9%
59.3%
89.2%
Doubao Pro
16.0%
44.0%
16.0%
70.0%
80.8%
48.1%
87.0%
Ernie 4.0
28.0%
60.0%
18.0%
70.0%
80.8%
53.7%
82.7%
Gemini 1.5 Flash
12.0%
20.0%
24.0%
40.0%
73.1%
31.5%
83.2%
Gemini 1.5 Pro
16.0%
40.0%
24.0%
50.0%
88.5%
46.3%
87.9%
GPT4o
56.0%
96.0%
28.0%
50.0%
65.4%
63.0%
89.6%
GPT4o-mini
20.0%
60.0%
20.0%
30.0%
57.7%
40.7%
86.1%
SenseChat
16.0%
36.0%
22.0%
75.0%
76.9%
42.6%
78.8%
Aya 23 8B
12.0%
40.0%
14.0%
15.0%
19.2%
31.5%
70.1%
CLLM v0.5 6B
24.0%
8.0%
18.0%
20.0%
50.0%
27.8%
71.9%
CLLM v0.5 34B
28.0%
28.0%
14.0%
35.0%
76.9%
37.0%
73.3%
Yi 1.5 6B
28.0%
12.0%
12.0%
10.0%
50.0%
20.4%
56.6%
Yi 1.5 9B
36.0%
40.0%
24.0%
30.0%
57.7%
18.5%
72.2%
Yi 1.5 34B
16.0%
32.0%
26.0%
30.0%
61.5%
33.3%
82.9%
Gemma 2 2B
8.0%
24.0%
18.0%
25.0%
53.8%
22.2%
73.4%
Gemma 2 9B
20.0%
28.0%
24.0%
25.0%
50.0%
33.3%
85.0%
Gemma 2 27B
20.0%
12.0%
16.0%
25.0%
65.4%
24.1%
83.2%
Llama 3.1 8B
12.0%
16.0%
18.0%
25.0%
42.3%
38.9%
60.3%
Llama 3.1 70B
28.0%
40.0%
12.0%
30.0%
61.5%
35.2%
84.5%
Llama 3.1 405B
20.0%
44.0%
18.0%
35.0%
65.4%
50.0%
64.4%
Mistral Nemo 12B
12.0%
28.0%
10.0%
25.0%
23.1%
37.0%
68.8%
Qwen2 7B
8.0%
40.0%
12.0%
35.0%
46.2%
33.3%
66.8%
Qwen2 72B
12.0%
28.0%
16.0%
50.0%
76.9%
48.1%
83.5%
Random/Control
16.0%
28.0%
24.0%
30.0%
11.5%
27.8%
76.8%
Table 2: Model performance on Linguistic Knowledge Dataset multiple-choice questions and NLP tasks. The bottom
row indicates the expected correctness from random selection for the Phonological and Orthographic Knowledge
tasks. For NLP, the reported figure is the average evaluation of professionally prepared translations for translation
tasks serving as a control.
models performed well in Sentiment Analysis
(GPT4o 79.7%, Llama 3.1 405B 78.8%), Trans-
lation (3-shot: GPT4o 98.3%, Qwen2 72B 96.6%),
and Summarisation (Claude 3.5 Sonnet 92.7%,
Gemma 2 9B 91.3%). Models that obtained lower
scores are often due to task completion problems,
e.g. failure to handle long input and problems with
low-frequency/mixed-language tokens.
Proprietary and large open-weight models have
good Cantonese lexical knowledge. The perfor-
mance in translation and sentiment analysis is
closely tied to the ability to determine the meaning
of Cantonese-specific words that are not found or
used differently in Mandarin. Most models also per-
formed well in the Cantoense Character Selection
sub-task (Canton. Char. in Table 2) under Ortho-
graphic Knowledge. It is noteworthy that despite
good performance with proprietary models (73.1%
- 88.5%) and some open-weight models (CLLM
v0.5 34B and Qwen2 72B, both 76.9%), GPT4o
struggled with Cantonese orthography (65.4%).
LLMs in general lack knowledge about Can-
tonese pronunciation.
In the Grapheme-to-
Phoneme (G2P) conversion task, all models per-
formed far worse than the rule-based control (Vi-
sual Fonts v3.3, CER 0.8%), with the closest be-
ing GPT-4o (5.4%) and Claude 3.5 Sonnet (7.9%)
as shown in Table 3. The appalling results from
all tested language models reveal how linguistic
knowledge is seriously under-represented. While
it is expected that the G2P tasks will be signif-
icantly improved in newer/future models, actual
linguistic tasks that involve sounds require more
advanced knowledge about the language’s sound
system. Most models struggled with tasks like
judging homophone or rhyme pairs in Table 2, with
GPT-4o being a notable exception (Homophone:
56.0%; Rhyming: 96.0%). Poor (close to chance
7

--- Page 8 ---

Model
CER
Levenshtein
Claude 3.5 Sonnet
7.9%
0.018
Doubao Pro
20.9%
0.044
Ernie 4.0
34.4%
0.094
Gemini 1.5 Flash
34.7%
0.083
Gemini 1.5 Pro
15.3%
0.030
GPT4o
5.4%
0.009
GPT4o-mini
12.0%
0.023
SenseChat
54.4%
0.163
Aya 23 8B
96.6%
0.724
CLLM v0.5 6B
94.1%
0.859
CLLM v0.5 34B
23.4%
0.058
Yi 1.5 6B
99.0%
0.577
Yi 1.5 9B
97.2%
0.528
Yi 1.5 34B
79.6%
0.837
Gemma 2 2B
97.5%
0.524
Gemma 2 9B
73.0%
0.259
Gemma 2 27B
62.5%
0.201
Llama 3.1 8B
69.9%
0.270
Llama 3.1 70B
31.3%
0.086
Llama 3.1 405B
26.3%
0.074
Mistral Nemo 12B
59.8%
0.201
Qwen2 7B
97.3%
0.466
Qwen2 72B
74.0%
0.268
Rule Based
0.8%
0.001
Table 3:
Model performance in the Grapheme-to-
Phoneme (G2P) dataset. Scores calculated based on
character error rates (CER) and Levenshtein distance.
(Lower is better)
level) performance in other models is not only due
to the lack of G2P ability, a prerequisite for phono-
logical reasoning, but also due to how Mandarin
homophones partially influence this task. This will
continue to be challenging for Cantonese due to
limited specialised data.
LLMs in general do not have meta-linguistic
knowledge represented in Cantonese. Although
certain models, especially the Chinese proprietary
models, performed well in the visual similarity task
(SenseChat 70%, Doubao 70%, Ernie 75%) or or-
thographic reasoning (GPT4o 63.0%), the knowl-
edge seems to have come from Simplified Chinese,
thus their good performance is not transferred to
Cantonese-specific items. This seems to be caused
by insufficient descriptive knowledge about the
structure and properties associated with the individ-
ual glyphs.
5
Conclusion
This paper presents HKCanto-Eval, the first com-
prehensive evaluation benchmark focusing on
Hong Kong Cantonese, by comparing the Can-
tonese language support of 6 proprietary and 7
open-weight model families. Our findings indicate
that while these models can understand Cantonese
in various contexts, retrieve knowledge about Hong
Kong, and address problems written in or about
Cantonese to some extent, there are notable limita-
tions. Most models, especially open-weight models
in the 6–9B range, lack sufficient linguistic, cul-
tural and professional knowledge in Cantonese and
Hong Kong. Performance was particularly poor
for questions requiring knowledge not commonly
found in major online sources.
One area that we paid close attention to is the
presence of metalinguistic knowledge in these mod-
els. There is concern that models showed Can-
tonese proficiency in linguistic and NLP tasks pri-
marily through Mandarin. If their linguistic under-
standing is based solely on Mandarin, they may
perform well on simpler tasks but struggle signifi-
cantly with “false friends" between languages, as
Mandarin knowledge becomes a hindrance. This
benchmark introduces a novel perspective, focus-
ing on Cantonese processing abilities beyond su-
perficial slang and expressions. By requiring rea-
soning about sounds and characters specific to Can-
tonese, our benchmark provides a fairer judgement
that credits models accurately capturing Cantonese
phonology and orthography, while exposing those
that appear competent in Cantonese but are heavily
reliant on Mandarin.
This challenge in processing Cantonese is shared
by other low-resource languages. As training data
increases, models tend to favour high-resource lan-
guages like Mandarin Chinese. The apparent simi-
larity between Cantonese and Written Chinese fur-
ther affects the ability of even proprietary models
to distinguish between these linguistic contexts ac-
curately. Addressing the segregation of regional
and linguistic knowledge is crucial for developing
culturally and linguistically adaptive LLMs. This
issue extends beyond Cantonese to other under-
represented language communities.
6
Limitations & Future Directions
The current benchmark exhibits several limitations.
Inaccuracies in machine-translated materi-
als: First, the use of machine translation introduces
8

--- Page 9 ---

potential inaccuracies. While Gemini 1.5 Flash
balances cost and quality, human-translated ques-
tions could provide a more reliable benchmark,
albeit at a higher resource cost. The reliance on
multiple-choice and text-based questions does not
fully capture the capabilities required for practi-
cal LLM applications such as code generation and
mathematical problem-solving, which demand co-
herent and contextual text generation. The dataset
also lacks multi-modal data like image and audio,
which is now supported by proprietary models and
should be evaluated.
Biases in topic selection: The newly and man-
ually created questions might contain biases and
a lack of scalability and comprehensiveness. The
cultural questions, predominantly created by col-
leagues and relatives of the authors, may introduce
bias in cultural references and wordings, leading
to an over-representation of certain perspectives
while under-representing others, such as traditional
practices. Political topics were also specifically
excluded, due to political complications, limiting
cultural representation. This can also be considered
a reasonable compromise since many models (e.g.
those from Chinese companies) are configured to
censor these topics, and there is a risk that our ac-
counts or IP addresses will be banned before we
complete all the benchmarking tasks for this paper.
Lack of Crosslingual Evaluation: English
translations for cross-lingual ability evaluation
were also not included due to resource limitations.
An additional comparison should be added to com-
pare whether the same set of questions will be an-
swered less satisfactorily when presented in En-
glish or Standard Written Chinese instead of Can-
tonese, in line with the evaluation done for Basque
(Etxaniz et al., 2024a) and Mongolian and Tibetan
(Zhang et al., 2025). We will leave this for future
research.
Reliance on human evaluation: Human evalu-
ation, while insightful, is not scalable. Automated
and objective evaluation methods, such as LLM-as-
a-judge or rule-based approaches, are necessary for
efficient evaluation, but this is challenging due to
the low-resource nature of Cantonese.
Future directions include developing bench-
marks incorporating audio, images, and tables, and
addressing the aforementioned limitations to cre-
ate more comprehensive and representative evalua-
tions.
Acknowledgments
Open-source models evaluated with computer re-
sources offered under the categories of Trial Use
and General Projects by the Research Institute for
Information Technology, Kyushu University. Vo-
tee AI gratefully sponsored the usage fee. T.C.C
is supported by the MEXT Initiative to Establish
Next-Generation Novel Integrated Circuit Centers
(X-NICS). The project is partially supported by
funding from the Centre for Research on Linguis-
tics and Language Studies (CRLLS), the Education
University of Hong Kong.
References
Alham Fikri Aji, Genta Indra Winata, Fajri Koto,
Samuel Cahyawijaya, Ade Romadhony, Rahmad Ma-
hendra, Kemal Kurniawan, David Moeljadi, Radi-
tyo Eko Prasojo, Timothy Baldwin, Jey Han Lau,
and Sebastian Ruder. 2022. One country, 700+ lan-
guages: NLP challenges for underrepresented lan-
guages and dialects in Indonesia. In Proceedings
of the 60th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 7226–7249, Dublin, Ireland. Association for
Computational Linguistics.
Anthropic. 2024. Claude 3 model card.
Viraat Aryabumi, John Dang, Dwarak Talupuru,
Saurabh Dash, David Cairuz, Hangyu Lin, Bharat
Venkitesh, Madeline Smith, Jon Ander Campos,
Yi Chern Tan, Kelly Marchisio, Max Bartolo, Se-
bastian Ruder, Acyr Locatelli, Julia Kreutzer, Nick
Frosst, Aidan Gomez, Phil Blunsom, Marzieh Fadaee,
Ahmet Üstün, and Sara Hooker. 2024.
Aya 23:
Open weight releases to further multilingual progress.
Preprint, arXiv:2405.15032.
Baidu Inc. 2023. Baidu launches ernie 4.0 foundation
model, leading a new wave of ai-native applications.
Robert S. Bauer. 2016. The hong kong cantonese lan-
guage: Current features and future prospects. Global
Chinese, 2(2):115–161.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming
Yuan, Henrique Ponde De Oliveira Pinto, Jared Ka-
plan, Harri Edwards, Yuri Burda, Nicholas Joseph,
Greg Brockman, et al. 2021.
Evaluating large
language models trained on code. arXiv preprint
arXiv:2107.03374.
Po-Heng Chen, Sijia Cheng, Wei-Lin Chen, Yen-Ting
Lin, and Yun-Nung Chen. 2024.
Measuring tai-
wanese mandarin language understanding.
arXiv
preprint arXiv:2403.20180.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
9

--- Page 10 ---

Nakano, et al. 2021. Training verifiers to solve math
word problems. arXiv preprint arXiv:2110.14168.
ByteDance Doubao. 2024. Doubao models.
Jia Tina Du, Iris Xie, and Jenny Waycott. 2020.
Marginalized communities, emerging technologies,
and social innovation in the digital age: Introduc-
tion to the special issue. Information Processing &
Management, 57(3):102235.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, et al. 2024. The llama 3 herd of models. arXiv
preprint arXiv:2407.21783.
David M. Eberhard, Gary F. Simons, and Charles D.
Fennig. 2024. Ethnologue: Languages of the World,
27 edition. SIL International, Dallas.
Julen Etxaniz, Gorka Azkune, Aitor Soroa, Oier La-
calle, and Mikel Artetxe. 2024a. Bertaqa: How much
do language models know about local culture? Ad-
vances in Neural Information Processing Systems,
37:34077–34097.
Julen Etxaniz, Oscar Sainz, Naiara Miguel, Itziar Ald-
abe, German Rigau, Eneko Agirre, Aitor Ormazabal,
Mikel Artetxe, and Aitor Soroa. 2024b. Latxa: An
open language model and evaluation suite for basque.
In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 14952–14972.
Ziru Fu, Yu Cheng Hsu, Christian S Chan, Chaak Ming
Lau, Joyce Liu, and Paul Siu Fai Yip. 2024. Efficacy
of chatgpt in cantonese sentiment analysis: compar-
ative study. Journal of Medical Internet Research,
26:e51069.
Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo
Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang
Chen, Runxin Xu, et al. 2024. Omni-math: A univer-
sal olympiad level mathematic benchmark for large
language models. arXiv preprint arXiv:2410.07985.
Aryo Pradipta Gema, Joshua Ong Jun Leang, Giwon
Hong, Alessio Devoto, Alberto Carlo Maria Mancino,
Rohit Saxena, Xuanli He, Yu Zhao, Xiaotang Du, Mo-
hammad Reza Ghasemi Madani, et al. 2024. Are we
done with mmlu? arXiv preprint arXiv:2406.04127.
Gemini Team, Petko Georgiev, Ving Ian Lei, Ryan
Burnell, Libin Bai, Anmol Gulati, Garrett Tanzer,
Damien Vincent, Zhufeng Pan, Shibo Wang, et al.
2024. Gemini 1.5: Unlocking multimodal under-
standing across millions of tokens of context. arXiv
preprint arXiv:2403.05530.
Gemma Team, Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupati-
raju, Léonard Hussenot, Thomas Mesnard, Bobak
Shahriari, Alexandre Ramé, et al. 2024. Gemma 2:
Improving open language models at a practical size.
arXiv preprint arXiv:2408.00118.
Vipul Gupta, David Pantoja, Candace Ross, Adina
Williams, and Megan Ung. 2024. Changing answer
order can decrease mmlu accuracy. arXiv preprint
arXiv:2406.19470.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing. arXiv preprint arXiv:2009.03300.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and Ja-
cob Steinhardt. 2021. Measuring mathematical prob-
lem solving with the math dataset. arXiv preprint
arXiv:2103.03874.
Kung Yin Hong, Lifeng Han, Riza Theresa Batista-
Navarro, and Goran Nenadic. 2024.
Cantonmt:
Cantonese-english neural machine translation look-
ing into evaluations. In Proceedings of the 16th Con-
ference of the Association for Machine Translation
in the Americas (Volume 2: User Track), pages 133–
144.
Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei
Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu,
Chuancheng Lv, Yikai Zhang, Yao Fu, et al. 2024.
C-eval: A multi-level multi-discipline chinese evalua-
tion suite for foundation models. Advances in Neural
Information Processing Systems, 36.
Aaron Hurst, Adam Lerer, Adam P Goucher, Adam
Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow,
Akila Welihinda, Alan Hayes, Alec Radford, et al.
2024. Gpt-4o system card.
Jiyue Jiang, Liheng Chen, Pengan Chen, Sheng Wang,
Qinghang Bao, Lingpeng Kong, Yu Li, and Chuan
Wu. 2024. How far can cantonese nlp go? bench-
marking cantonese capabilities of large language
models. arXiv e-prints, pages arXiv–2408.
Fajri Koto, Haonan Li, Sara Shatnawi, Jad Dough-
man, Abdelrahman Boda Sadallah, Aisha Alraeesi,
Khalid Almubarak, Zaid Alyafeai, Neha Sengupta,
Shady Shehata, et al. 2024. Arabicmmlu: Assessing
massive multitask language understanding in arabic.
arXiv preprint arXiv:2402.12840.
Chaak Ming Lau. 2024. Ideologically driven divergence
in cantonese vernacular writing practices. In J.-F.
Dupré, editor, Politics of Language in Hong Kong.
Routledge.
Chaak Ming Lau, Mingfei Lau, and Ann Wai Huen To.
2024. The extraction and fine-grained classification
of written cantonese materials through linguistic fea-
ture detection. In Proceedings of the 2nd Workshop
on Resources and Technologies for Indigenous, En-
dangered and Lesser-resourced Languages in Eura-
sia (EURALI)@ LREC-COLING 2024, pages 24–29.
Jackson Lee, Litong Chen, Charles Lam, Chaak Ming
Lau, and Tsz-Him Tsui. 2022. PyCantonese: Can-
tonese linguistics and NLP in python. In Proceedings
10

--- Page 11 ---

of the Thirteenth Language Resources and Evalua-
tion Conference, pages 6607–6611, Marseille, France.
European Language Resources Association.
Genevieve Leung and Yuuko Uchikoshi. 2012. Relation-
ships among language ideologies, family language
policies, and children’s language achievement: A
look at cantonese-english bilinguals in the us. Bilin-
gual Research Journal, 35(3):294–313.
Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, Hai
Zhao, Yeyun Gong, Nan Duan, and Timothy Bald-
win. 2023. Cmmlu: Measuring massive multitask
language understanding in chinese. arXiv preprint
arXiv:2306.09212.
Mistral. 2024. Mistral nemo.
OpenAI. 2024. Gpt-4o mini: advancing cost-efficient
intelligence.
Irene Plaza, Nina Melero, Cristina del Pozo, Javier
Conde, Pedro Reviriego, Marina Mayor-Rocher, and
María Grandury. 2024.
Spanish and llm bench-
marks: is mmlu lost in translation? arXiv preprint
arXiv:2406.17789.
Itesh Sachdevl, Richard Bourhis, Sue-wen Phang, and
John D’Eye. 1987. Language attitudes and vitality
perceptions: Intergenerational effects amongst chi-
nese canadian communities. Journal of Language
and Social Psychology, 6(3-4):287–307.
SenseTime. 2024. Sensetime introduces sensechat (can-
tonese) to hong kong users, delivering localised ai
experiences free-of-charge.
Guijin Son, Hanwool Lee, Sungdong Kim, Seungone
Kim, Niklas Muennighoff, Taekyoon Choi, Cheon-
bok Park, Kang Min Yoo, and Stella Biderman.
2024. Kmmlu: Measuring massive multitask lan-
guage understanding in korean.
arXiv preprint
arXiv:2402.11548.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao,
Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch,
Adam R Brown, Adam Santoro, Aditya Gupta,
Adrià Garriga-Alonso, et al. 2022.
Beyond the
imitation game: Quantifying and extrapolating the
capabilities of language models.
arXiv preprint
arXiv:2206.04615.
Ashima Suvarna, Harshita Khandelwal, and Nanyun
Peng. 2024. PhonologyBench: Evaluating phono-
logical skills of large language models. In Proceed-
ings of the 1st Workshop on Towards Knowledgeable
Language Models (KnowLLM 2024), pages 1–14,
Bangkok, Thailand. Association for Computational
Linguistics.
Saeid Asgari Taghanaki, Aliasgahr Khani, and Amir
Khasahmadi. 2024. Mmlu-pro+: Evaluating higher-
order reasoning and shortcut learning in llms. arXiv
preprint arXiv:2409.02257.
Zhi-Rui Tam, Ya-Ting Pai, Yen-Wei Lee, Jun-Da Chen,
Wei-Min Chu, Sega Cheng, and Hong-Han Shuai.
2024.
An improved traditional chinese evalua-
tion suite for foundation model.
arXiv preprint
arXiv:2403.01858.
toastynews. 2020. openrice-senti.
Maria Tsapali and Hiu Ching Wong. 2023. The future
of cantonese and traditional chinese among newly
arrived hong kong immigrant children in the united
kingdom–a study on parents’ attitudes, challenges
faced and support needed. Cambridge Educational
Research e-Journal, 10:14–31.
Sshubam Verma, Mohammed Safi Ur Rahman Khan,
Vishwajeet Kumar, Rudra Murthy, and Jaydeep Sen.
2024. Milu: A multi-task indic language understand-
ing benchmark. arXiv preprint arXiv:2411.02538.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni,
Abhranil Chandra, Shiguang Guo, Weiming Ren,
Aaran Arulraj, Xuan He, Ziyan Jiang, et al. 2024.
Mmlu-pro: A more robust and challenging multi-task
language understanding benchmark. arXiv preprint
arXiv:2406.01574.
Andrea W Wen-Yi, Unso Eun Seo Jo, and David Mimno.
2025. Do chinese models speak chinese languages?
arXiv preprint arXiv:2504.00289.
Genta Winata, Shijie Wu, Mayank Kulkarni, Thamar
Solorio, and Daniel Preotiuc-Pietro. 2022. Cross-
lingual few-shot learning on unseen languages. In
Proceedings of the 2nd Conference of the Asia-Pacific
Chapter of the Association for Computational Lin-
guistics and the 12th International Joint Conference
on Natural Language Processing (Volume 1: Long
Papers), pages 777–791, Online only. Association for
Computational Linguistics.
Rong Xiang, Emmanuele Chersoni, Yixia Li, Jing Li,
Chu-Ren Huang, Yushan Pan, and Yushi Li. 2024.
Cantonese natural language processing in the trans-
formers era: a survey and current challenges. Lan-
guage Resources and Evaluation, pages 1–27.
Yuemei Xu, Ling Hu, Jiayi Zhao, Zihan Qiu, Kevin Xu,
Yuqi Ye, and Hanwen Gu. 2024. A survey on multi-
lingual large language models: Corpora, alignment,
and bias. arXiv preprint arXiv:2404.00929.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan
Li, Dayiheng Liu, Fei Huang, et al. 2024. Qwen2
technical report. arXiv preprint arXiv:2407.10671.
William Yiu. 2024. Hong kong government to adopt
city’s own chatgpt-style tool after openai further
blocks access.
Alex Young, Bei Chen, Chao Li, Chengen Huang,
Ge Zhang, Guanwei Zhang, Heng Li, Jiangcheng
Zhu, Jianqun Chen, Jing Chang, et al. 2024. Yi:
Open foundation models by 01. ai. arXiv preprint
arXiv:2403.04652.
11

--- Page 12 ---

Zheng Yuan, Hongyi Yuan, Chuanqi Tan, Wei Wang,
and Songfang Huang. 2023. How well do large lan-
guage models perform in arithmetic tasks?
arXiv
preprint arXiv:2304.02015.
Daoguang Zan, Bei Chen, Fengji Zhang, Dianjie
Lu, Bingchao Wu, Bei Guan, Yongji Wang, and
Jian-Guang Lou. 2022.
Large language mod-
els meet nl2code:
A survey.
arXiv preprint
arXiv:2212.09420.
Chen Zhang, Zhiyuan Liao, and Yansong Feng.
2025.
Cross-lingual transfer of cultural knowl-
edge: An asymmetric phenomenon. arXiv preprint
arXiv:2506.01675.
Lubei Zhang, Linda Tsung, and Xian Qi. 2023. Home
language use and shift in australia: Trends in the new
millennium. Frontiers in Psychology, 14:1096147.
Appendix
A
Questionable Practices in an Existing
Work
Jiang et al. (2024) recently proposed a Cantonese
evaluation dataset consisting of 5 datasets. The au-
thors cited a HuggingFace organisation homepage
in a footnote for their translation dataset but offered
no further specifics. Yet, the dataset’s entries were
not identifiable within the linked account. Nonethe-
less, the translation pairs between Cantonese and
English are dubious. During the machine transla-
tion process, the less advanced models before GPT-
3.5 tend to break English sentences into phrases
by punctuation marks or connecting words such as
"and" and "but". Then the phrases were translated
individually and finally put together into one sen-
tence in Cantonese. As a result, the translated texts
were full of wrong wordings such as the following
translation pair:
English:
Once upon a time, there was a three year
old girl named Gwen. One day, she was
walking with her mom when she saw
something unusual. She wondered out
loud, âCœWhat is that?âC Her mom ex-
plained, âCœThatâC™s an old license.
It shows that the person is allowed to
drive.âC Gwen then asked, âCœCan I
get one?âC Her mom smiled, shaking
her head. âCœNo, not now.
Cantonese translation:
Gwen
，
。
，
，
。
：「
？」
：
「
，
。」Gwen
：
「
？！」
：「
，
。
The age of a person was counted using
(year)
instead of the correct word
(years of age).
Another example is incomprehensible:
English:
Once upon a time, there was a big di-
nosaur. He was very fast and could run
really quickly. One day, the dinosaur
went for a walk and saw a little boy. The
12

--- Page 13 ---

boy was sad because he lost his toy car.
The dinosaur felt sorry for the boy and
decided to help him. He ran very fast to
search for the toy car. After a while, the
dinosaur found the toy car and returned
it to the little boy. The boy was happy
and thanked the dinosaur for being so
kind. From that day on, the boy and the
dinosaur became good friends and went
on many adventures together.
Cantonese translation:
，
，
。
，
，
。
，
。
，
。
。
，
，
。
，
。
，
，
。
The translation service broke down the original
English sentences by punctuation and connectives
(such as "and"). Then, it translated the broken-
down phrases individually and joined them into a
Cantonese/Chinese sentence, resulting in awkward
and incorrect punctuation usage. The heavy use of
poor machine translation of existing work offered
little in terms of novel contributions or insights into
the language.
The use of the BLEU score is inappropriate for
Cantonese translation. Please see Appendix F for
our rationale.
B
Translated MMLU Dataset
The original MMLU dataset was translated into
Cantonese by Gemini 1.5 Flash using the following
prompt:
：
*** Input: (Example question 1)
** A: (Example 1 option A)
** B: (Example 1 option B)
** C: (Example 1 option C)
** D: (Example 1 option D)
** Target: (Example 1 Answer)
：
***
：(Manually translated Exam-
ple Question 1)
**
A：(Manually
translated
Example 1 option A)
**
B：(Manually
translated
Example 1 option B)
**
C：(Manually
translated
Example 1 option C)
**
D：(Manually
translated
Example 1 option D)
**
：(Example 1 Answer)
=================
(Another four examples)
=================
：
** Input: (Input Question)
** A: (Option A)
** B: (Option B)
** C: (Option C)
** D: (Option D)
** Target: (Answer)
English translation of the prompt:
Translate the following multiple choice
question to Cantonese：
*** Input: (Example question 1)
** A: (Example 1 option A)
** B: (Example 1 option B)
** C: (Example 1 option C)
** D: (Example 1 option D)
** Target: (Example 1 Answer)
Cantonese Translation：
*** Input：(Manually translated Exam-
ple Question 1)
** Option A：(Manually translated
Example 1 option A)
** Option B：(Manually translated
Example 1 option B)
** Option C：(Manually translated
13

--- Page 14 ---

Example 1 option C)
** Option D：(Manually translated
Example 1 option D)
** Target：(Example 1 Answer)
=================
(Another four examples)
=================
Translate the following multiple choice
question to Cantonese：
** Input: (Input Question)
** A: (Option A)
** B: (Option B)
** C: (Option C)
** D: (Option D)
** Target: (Answer)
C
Academic and Professional Dataset
The Professional Dataset subset consists of 7 pro-
fessional qualification exams:
1. Estate Agents Qualifying Exam (EAQE):
Exam from the Estate Agents Authority
(EAA) which grants an estate agent’s license
for a person to become a director or a partner
of an estate agency.
2. Insurance Intermediaries Qualifying Ex-
amination: The Insurance Authority in Hong
Kong regulates and licenses all insurance in-
termediaries in Hong Kong and offers this
exam for any person who wishes to carry out
insurance activities.
3. Leveraged Foreign Exchange Trading Ex-
amination: An industry qualification exam
offered by the Vocational Training Council
(VTC) and approved by the Securities and
Future Commission.
4. Licensing Exam for Securities & Futures
Intermediaries: An exam offered by the
Hong Kong Securities and Investment Insti-
tute and recognised by the Securities and Fu-
tures Commission (SFC). It is a professional
qualification exam for people who would like
to work in the securities and investment indus-
try in Hong Kong.
5. Mandatory
Provident
Fund
Schemes
(MPF)/Intermediaries Exam:
The MPF
is the pension scheme in Hong Kong and
any intermediaries involved in providing the
service are required to pass this exam.
6. Pleasure Vessel Operator Grade 2 Certifi-
cate: The Marine Department of Hong Kong
offers this exam for anyone who wishes to op-
erate a boat less than 15 meters in length for
pleasure purposes.
7. EAA Salespersons Qualifying Examination:
Exam from the EAA which grants a salesper-
son’s license for a salesperson to carry out
estate agency work.
8. Taxi License Written Exam Route Planning
Exam: Unique questions created in the form
of the Taxi License Written Exam Route Plan-
ning Exam which are multiple-choice ques-
tions about selecting the shortest route be-
tween any two places or landmarks without
considering toll fees.
All the exams suggested above were sourced from
PDF files provided by the exam provider and pro-
cessed by Google Gemini 1.5 Flash. The pages
containing the model answers were separated from
the questions pages, which could mitigate the data
contamination issue. The following sentence is
added to the front of the prompt during the evalua-
tion:
Follow the given examples and answer
the question. The question is about pro-
fessional knowledge in Hong Kong. You
should only return the answer: A, B, C,
or D.
The next two law-related categories were
sourced from the Internet:
1. Hong Kong Law: Questions across 15 cate-
gories such as child abuse, domestic violence,
the Employment Ordinance, Equal Opportu-
nities, family law, etc. were gathered across
the Internet.
2. Basic Law:
Constitution-type question
sourced from a website. The questions were
updated according to the current and actual
practice of the Basic Law and options were
also appended to 4 options per question by the
authors.
14

--- Page 15 ---

Name
Source
No.
Eng.
Estate Agent
PDF
50
Y
Insurance Interm.
PDF
130
Y
Leveraged FX
PDF
20
Y
Securities & Futures
PDF
400
Y
MPF Interm.
PDF
26
Y
Pleasure Vessel
PDF
66
Y
Salesperson
PDF
50
Y
Taxi
New
30
N
HK Law
Web
360
N
Basic Law
Web
64
N
Total
1,196
Table 4: Professional Dataset Summary
A sentence describing the task is added at the
front of the prompt:
Follow the given examples and answer
the question. The question is about Hong
Kong law. You should only return the
answer: A, B, C, or D.
The number of questions and the source of each
professional exam can be found in Table 4.
The Academic Dataset subset was sourced from
scanned copies of the HKDSE exam from the last
2 to 4 years. The details can be found in Table
5. The scanned PDFs were processed to extract
text with the Google Gemini 1.5 Pro API. The ex-
tracted text was then corrected and filtered by the
authors to remove questions that required informa-
tion from other questions. Those requiring refer-
ences to visual materials like pictures and maps
were also removed but reserved for future evalua-
tion of vision-enabled LLMs.
Although only multiple-choice questions were
included in the dataset, more complicated ques-
tions that require complex reasoning and human
judgment, such as Chinese listening and Liberal
Studies exams were studied. Initial testing showed
proprietary LLMs can easily achieve perfect scores
in the Chinese listening exam when given the tran-
script, while the length of the transcript exceeded
some open-weight LLMs’ context length. Further
experiments were conducted with Google Gemini
1.5 Flash and Pro to take the audio file and written
questions as input. Although the two models again
achieved a perfect score, no other model supported
audio input at the time of the experiment, so the
Subject
No.
Eng.
Biology
52
Y
Business, Accounting
& Financial Studies
50
Y
Chemistry
42
Y
Economics
46
Y
Geography
54
Y
Information &
Comm. Tech.
73
Y
Mathematics
63
Y
Physics
30
Y
Tourism &
Hospitality Studies
56
N
Total
466
Table 5: Academic Dataset Summary
task was excluded. For the now-defunct Liberal
Studies, examinees were required to write a pas-
sage taking into account the provided reference
materials and then develop their own point of view
supported by examples from the candidates’ own
knowledge. However, initial testing showed that
none of the LLMs were able to include their own
examples despite being explicitly requested in the
prompt. These tasks were therefore not included in
the final evaluation.
During the evaluation, a short sentence is added
to the front to explain the nature of the dataset:
Follow the given examples and answer
the question. The question is about Hong
Kong DSE. You should only return the
answer: A, B, C, or D.
D
Hong Kong Cultural Questions Dataset
The Hong Kong Cultural Questions Dataset con-
tains four categories of newly created questions and
one existing question set, which the breakdown can
be found in Table 6.
1. Food Culture: Hong Kong has a unique culi-
nary and food culture due to cultural influ-
ences from East and West. The questions were
designed to highlight local dishes, street food,
high-end dining, and “
” Cha chaan
teng (Hong Kong-styled cafe) culture.
2. History and Landmarks: Questions in this
category assess the knowledge of significant
historical events, figures, and iconic land-
marks that have shaped Hong Kong’s identity.
15

--- Page 16 ---

Subject
No. of Q.
New Q.
History & Landmarks
61
Y
Food Culture
59
Y
Lang. & Expressions
49
Y
Life in HK
75
Y
Local Area Knowledge
33
N
Total
277
Table 6: Summary of the Hong Kong Cultural Ques-
tions Dataset
3. Language and Expressions: This category
focuses on Cantonese-specific vocabulary, col-
loquialisms, slang, and common expressions
used in daily life and social media networks.
4. Life in Hong Kong: This category covers
the customs, traditions, social norms, popular
culture (TV and cinema), recent events and ev-
eryday life experiences unique to Hong Kong.
5. Local Area Knowledge: Contains 33 ques-
tions on non-trivial local area knowledge se-
lected from the Hong Kong Geography Tatsu-
jin Challenge, an online questionnaire partici-
pated by over 100,000 participants.
A question bank of 244 questions, written in
pure Cantonese, was created for the first four cat-
egories. To ensure the questions were based on
common knowledge of the population, these ques-
tions were sent to 30 Hong Kong volunteers aged
20-50 years, and they were instructed not to use a
search engine when attempting the questions. Con-
sent was sought for using their data to inform the
design of an LLM benchmark for Cantonese. Items
with an accuracy under 40.0% were excluded. For
the last category, the questions were randomly se-
lected from the Hong Kong Geography Tatsujin
Challenge, which we have access to question-based
correctness measures. The average correct rate of
the selected questions is 53.0% for this subset. The
questions in this subcategory were in Written Chi-
nese.
The following sentence is added to the front of
the prompt:
Follow the given examples and answer
the question. The question is about Hong
Kong. Only return the answer: A, B, C,
or D. DO NOT EXPLAIN.
Given the unique and novel challenges presented
by this dataset, a breakdown of model performance
at five-shot evaluation is included in Table 7. The
average score of the human evaluation was also
included as a reference, where no model outper-
formed humans in the Food Culture and Language
and Expressions category. SenseChat (Cantonese)
refused to answer any questions in the History &
Landmark due to the appearance of the name of the
Hong Kong Chief Executive John Lee in the 5-shot
examples.
E
Linguistic Knowledge Dataset
This dataset comprises three sub-datasets with ques-
tions carefully designed with expert input from
researchers specialising in different areas of Can-
tonese linguistics. The structure and questions of
each dataset are outlined below.
E.1
Phonological Knowledge Dataset
The Phonological Knowledge Dataset include three
groups of questions: Homophone Judgment (25
questions), Rhyme Judgment (25 questions), and
a group of Phonological Reasoning Tasks (Multi-
Pron Resolution, Tone Matching, Poetry Rhyme,
Shared Feature Judgment, and Couplet Reasoning,
50 questions in total).
1. Homophone Judgment: The task is to deter-
mine which character from a list shares the
same pronunciation in Cantonese as the given
character, if any. For example, if the given
character is
and the list of characters is A
, B
, C
, D
, the answer would be
none of the above, as none of the characters
(ji6, jat6, ji1, ji2) is a homophone of the given
character (jat1).
2. Rhyme Judgment: The task is to determine
which character from a list rhymes with a
given character in Cantonese. For example,
if the given character is
and the list is A
, B
, C
, D
, the answer will be C,
as it is pronounced ban6 in Cantonese, which
rhymes with the given character man4.
3a. MultiPron Resolution: A word that contains
a character that can be pronounced in multi-
ple ways (like the English word read can be
pronounced as red or reed), and the task is
to decide how this character should be pro-
nounced. For example, if the given word is
and the question asks for a homophone
for the 2nd character, given the list A
B
C
D
, the answer is none of the above.
16

--- Page 17 ---

Model
Food
Culture
History &
Landmarks
Language &
Expressions
Life in HK
Local Area
Knowledge
Average
Claude 3.5 Sonnet
74.1%
80.4%
70.5%
85.7%
64.3%
75.0%
Doubao Pro
81.5%
82.1%
77.3%
77.1%
57.1%
75.0%
Ernie 4.0
74.1%
75.0%
75.0%
84.3%
67.9%
75.2%
Gemini 1.5 Flash
59.3%
69.6%
56.8%
77.1%
57.1%
64.0%
Gemini 1.5 Pro
75.9%
82.1%
65.9%
84.3%
60.7%
73.8%
GPT4o
83.3%
83.9%
68.2%
82.9%
67.9%
77.2%
GPT4o-mini
57.4%
67.9%
50.0%
74.3%
53.6%
60.6%
SenseChat
87.0%
N.A.
79.6%
78.6%
64.3%
77.4%
Aya 23 8B
35.2%
46.4%
34.1%
44.3%
28.6%
37.7%
CLLM v0.5 6B
51.9%
67.9%
63.6%
54.3%
42.9%
56.1%
CLLM v0.5 34B
77.8%
87.5%
72.7%
74.3%
71.4%
76.7%
Yi 1.5 6B
40.7%
64.3%
50.0%
55.7%
42.9%
50.7%
Yi 1.5 9B
53.7%
60.7%
52.3%
70.0%
50.0%
57.3%
Yi 1.5 34B
74.1%
82.1%
61.4%
75.7%
71.4%
72.9%
Gemma 2 2B
29.6%
37.5%
34.1%
42.9%
32.1%
35.2%
Gemma 2 9B
48.2%
57.1%
50.0%
60.0%
42.9%
51.6%
Gemma 2 27B
61.1%
69.6%
56.8%
67.1%
50.0%
60.9%
Llama 3.1 8B
51.9%
57.1%
50.0%
54.3%
50.0%
52.7%
Llama 3.1 70B
61.1%
78.6%
52.3%
72.9%
57.1%
64.4%
Llama 3.1 405B
64.8%
75.0%
59.1%
75.7%
75.0%
69.9%
Mistral Nemo 12B
31.5%
53.6%
45.5%
54.3%
28.6%
42.7%
Qwen2 7B
55.6%
67.9%
50.0%
68.6%
32.1%
54.8%
Qwen2 72B
75.9%
82.1%
72.7%
82.9%
75.0%
77.7%
Random
35.2%
21.4%
27.3%
31.4%
25.0%
28.1%
Human
81.7%
73.4%
85.8%
83.9%
53.0%
75.6%
Table 7: Model performance on the Hong Kong Cultural Questions Dataset in 5-shots settings
17

--- Page 18 ---

The given character should be pronounced as
ho4 and none of the answer (ho2, ho6, ho1,
wo4) matches this pronunciation.
3b. Tone Matching: Given a polysyllabic word,
choose a word from a list that matches the
tonal (pitch) pattern based on tone-melodic
requirement. For example, given the word
, and the list A
B, B
, C
, D
, the answer is B. Its pronunciation is
do1ci3, which is a high tone followed by a
mid tone, same as the given word ci1sin3.
3c. Poetry Rhyme: Given a poem, choose the cor-
rect combination of rhyming characters, e.g.
in the poem
，
，
，
。The last
syllables are zeon6, lau4, muk6, lau4 in Can-
tonese,
and
are the two characters that
rhyme in the poem when recited in Cantonese.
3d. Shared Feature Judgment: The task is to
choose an odd character from a list that does
not share a common phonological feature. For
example, the list A
B
C
D
is
ng6, ngaa4, daa2, saa1 in Jyutping. The last
three characters share the same rhyme aa, so
A is the odd one.
3e. Couplet Reasoning: One line of a couplet
will be given. Characters in a couplet can
be divided into two rhythmic categories,
(ping4, Level) and
(zak1, Oblique). This
distinction is taught at school and is a long-
standing poetry tradition. The task is to de-
termine the category for each of the charac-
ters, and decide whether it is the upper (
) or lower (
) line. For example, the line
is tin1 zang1 seoi3 jyut6
jan4 zang1 sau6 in Jyutping, and its pattern
is LLOOLLO, and as it ends with an oblique
sound, it is the upper line. Therefore it is
described as
、
.
The questions were evaluated using the follow-
ing system prompt:
You are a speaker of Cantonese from
Hong Kong. Please answer these ques-
tions about the sounds of the language.
Do not include any further explanation.
Example questions for each task:
1. Which of the following character is a homo-
phone of `
` in Cantonese? (A)
(B)
(C)
(D)
(E) None of the above
2. Which of the following character rhymes with
the character `
` in Cantonese? (A)
(B)
(C)
(D)
(E) None of the above
3a. Which of the following character best repre-
sents the sound of `
` in the word `
` in
Cantonese? (A)
(B)
(C)
(D)
(E)
None of the above
3b. Which of the following words have the near-
est tone or pitch pattern with `
` in Can-
tonese? (A)
B (B)
(C)
(D)
(E) None of the above
3c. In the following poem
```
，
。
，
。```
What are the last words of the rhyming lines if
recited in Cantonese? `(A)
(B)
(C)
(D)
(E) None of the above`
3d. Three of the four characters below share a
common phonological feature in Cantonese,
and one does not. Which one is the odd one?
(A)
(B)
(C)
(D)
(E) None of the
above
3e. This is a line of a couplet (
): `
`
Which of the following is a correct descrip-
tion of the line, according to its Cantonese
pronunciation? (A)
、
(B)
、
(C)
、
(D)
、
(E) Cannot be determined.
E.2
Orthographic Knowledge Dataset
The Orthographic Knowledge Dataset consists
of three sub-tasks: Visual Similarity Judgment
(25 questions), Cantonese Character Selection (26
questions), and a group of Orthographic Reasoning
Tasks (Character Calculation, Radical Description,
Character Structure, 54 questions in total).
1. Visual Similarity Judgement: The task is to
determine which character from a list is the
most visually similar to the given character.
For example, given the character
, and the
18

--- Page 19 ---

list “A
B
C
D
”, the answer will
be B, as the character is only different from the
given character in the length of the horizontal
strokes.
2. Cantonese Characters Selection: Cantonese
words do not necessarily have a standardised
form. Some very common characters can be
written in multiple ways. The task provides
a sentence frame with a missing character,
which should be clear from the context what
the syllable is. This is followed by a list of
possible characters for insertion. For example,
given the sentence “
＿
” (I am too something and I cannot finish eat-
ing this.), it should be filled with a word that
means “full” in Cantonese. Given the list “A
B
C
D
”, D should be chosen
as it is the most accepted word for the Can-
tonese word baau2. Answer A is marginally
acceptable in Written Chinese, but it com-
monly means “to support” (caang3) in Can-
tonese, thus should not be selected.
3a. Character Calculation: The task is to deter-
mine the end result of operations that involve
adding, removing or changing glyph compo-
nents of a character, and choose the closest
character from a list. For example, given the
instruction to remove “
” from “
”, and a
list of “A
B
C
D
”, the answer
will be A as this is the closest character that
matches with the instruction.
3b. Radical Description: A character will be
given, followed by a list of Kangxi radi-
cals.
For example, the character “
” is
listed under the “
” (water) radical, and the
Cantonese name for the radical is “
”
(three drops of water).
3c. Character Structure: The task is to choose
the best description of the structure of the
given character. For example, the character
“
” is formed by combining two characters
in the left-right frame (“
”).
The questions were evaluated using the follow-
ing system prompt:
You are a speaker of Cantonese from
Hong Kong. Please answer these ques-
tions about the properties of the language.
Do not include any further explanation.
Example questions for each task:
1. Select the character that is visually similar to
`
` in the Hong Kong context (A)
(B)
(C)
(D)
(E) None of the above
2. Consider this Cantonese sentence `
＿
`. Choose one character below
that is the most widely-accepted way to repre-
sent the missing word. (A)
(B)
(C)
(D)
(E) None of the above
3a. What character do you get by removing `
`
from `
`? (A)
(B)
(C)
(D)
(E)
None of the above
3b. What is the radical of the character `
` and
how is it called in Cantonese? (A)
（
）(B)
（
）(C)
（
）(D)
（
）(E) None of the above
3c. What is the best description of the character
structure of `
`? (A)
(B)
(C)
(D)
(E) None of the above
E.3
Grapheme-to-Phoneme (G2P) Conversion
Dataset
Cantonese transliteration is not trivial because the
characters and pronunciation form a many-to-many
relation. The same syllable can be represented by
different characters, which is a crucial feature of
an ideographic writing system, whereas the same
character may have multiple pronunciations due to
the overloading of certain characters or multiple
layers of pronunciation norms. These judgements
are often not well-documented. Characters with
multiple pronunciations are often semantically or
lexically determined, for example: “
” can be
pronounced as hang4 (e.g. “
” action, “
” trend), haang4 (e.g. “
” to walk, “
” to
go shopping), hong4 (e.g. “
” bank, “
”
occupation), hong2 (e.g. “
” investment bank).
For a smaller subset of characters, there can be
different pronunciations due to a literary-colloquial
distinction, e.g. “
” (to sit) can be zo6 or co5;
“
” (to invite) can be cing2 or ceng2.
The five-shot evaluation prompt used for the G2P
dataset evaluation:
You are an expert in Cantonese linguis-
tics.
Please convert the given Can-
tonese sentence into Jyutping romani-
sation. You can ignore all punctuation
marks, and normalise all numerals and
19

--- Page 20 ---

English loanwords into Cantonese pro-
nunciation. Do not include any further
explanation.
Example 1
，
？
gam1 jat6 tin1 hei3 hou2 hou2 bat1 jyu4
ceot1 heoi3 saan3 bou6
Example 2
ngo5 zung1 ji3 haang4 soeng1 coeng4
m4 zung1 ji3 haang4 gaai1 si5
Example 3
zyu1 mi1 mi4 hai6 coeng3 go1 hou2 lek1
ge3 go1 sau2
Example 4
，
。
gam1 tin1 si6 hok6 haau6 zing3 soeng4
soeng5 fo3 jat6 ceng2 gok3 wai2 gaa1
zoeng2 duk1 cuk1 zi2 neoi5 zeon2 si4
soeng5 hok6
Example 5
，
hok6 ji4 si4 zaap6 zi1 bat1 jik6 jyut6 fu4
Score calculation: All acceptable variants have
been listed as answers and all variants are consid-
ered equally good. This is to handle variant forms
and ambiguous interpretations that may not be the
standard, but native speakers of Cantonese accept.
We will use the answer with the highest score for
the subsequent calculation. Two metrics were used:
character error rate (CER) and Levenshtein dis-
tance. A lower score means a better performance.
The answers with the lowest Levenshtein distance
(i.e. the best score) were used for the calculation.
F
Translation Task
The translation dataset consists of 20 Cantonese
sentences.
These sentences were designed to
check the models’ understanding of sentence nu-
ances as they involve lexical or contextual ambi-
guities that require good linguistic reasoning to
resolve. Each Cantonese sentence was translated
into both English and written Chinese by a profes-
sional translator. This provides the source for four
translation pairs per original Cantonese sentence:
Cantonese-English, Cantonese-Written_Chinese,
English-Cantonese, Written_Chinese-Cantonese.
Here is an example sentence taken from the few
shot examples:
Cantonese (avg. 28.6 characters):
，
，
。
English (avg. 23.1 words):
Your day job is so exhausting that you
are like half-dead after work. If you keep
pushing yourself like this, the money you
earn won’t even cover your medical bills.
Written Chinese (avg. 29.6 characters):
，
，
。
Evaluation prompt for the three-shot translation
task (from Written Chinese to Cantonese) (Note:
the prompt uses the word “Traditional Chinese” to
force the model to return the results in the Tradi-
tional script.):
，
：
1：
: (e.g. 1)
: (e.g. 1)
2：
: (e.g. 2)
: (e.g. 2)
3：
: (e.g. 3)
: (e.g. 3)
：
(Text to translate)
，
，
English translation of the prompt:
Translate
the
following
Traditional
Chinese sentence to the Cantonese used
in Hong Kong, referring to the examples
below:
20

--- Page 21 ---

Model
Translation
(0-shot)
Translation
(3-shot)
Summarisation
Sentiment
Claude 3.5 Sonnet
96.2%
91.9%
92.7%
76.0%
Doubao Pro
97.5%
97.4%
85.5%
67.7%
Ernie 4.0
86.2%
87.1%
83.3%
74.1%
Gemini 1.5 Flash
92.6%
95.5%
70.0%
74.9%
Gemini 1.5 Pro
95.3%
91.1%
90.0%
75.3%
GPT4o
96.7%
98.3%
83.7%
79.7%
GPT4o-mini
89.8%
95.2%
84.8%
74.7%
SenseChat
90.6%
93.8%
54.3%
76.5%
Aya 23 8B
81.0%
79.4%
52.8%
67.1%
CLLM v0.5 6B
97.5%
94.7%
29.0%
66.5%
CLLM v0.5 34B
86.6%
90.3%
43.2%
73.1%
Yi 1.5 6B
62.9%
56.7%
42.5%
64.3%
Yi 1.5 9B
69.5%
88.1%
62.2%
69.1%
Yi 1.5 34B
87.3%
95.8%
70.3%
78.2%
Gemma 2 2B
71.4%
64.4%
86.3%
71.6%
Gemma 2 9B
87.8%
88.2%
91.3%
72.6%
Gemma 2 27B
89.3%
78.4%
89.0%
76.1%
Llama 3.1 8B
76.3%
81.1%
15.3%
68.6%
Llama 3.1 70B
92.1%
86.6%
81.7%
77.5%
Llama 3.1 405B
77.5%
93.3%
8.0%
78.8%
Mistral Nemo 12B
77.0%
84.8%
40.7%
72.7%
Qwen2 7B
84.5%
90.1%
14.8%
77.9%
Qwen2 72B
97.1%
96.6%
62.2%
78.2%
Control
99.1%
99.1%
-
-
Table 8: Model performance in various NLP tasks
21

--- Page 22 ---

Example 1: Written Chinese: (e.g. 1)
Cantonese: (e.g. 1)
Example 2: Written Chinese: (e.g. 2)
Cantonese: (e.g. 2)
Example 3: Written Chinese: (e.g. 3)
Cantonese: (e.g. 3)
Text to Translate:
(Text to translate)
Ensure the translation is accurate and nat-
ural, preserving the original meaning and
using concise and fluent English expres-
sion.
Only return the translation. Do not ex-
plain.
The other 2 translation pairs used a similar for-
mat, but an English prompt is used when translating
from Cantonese to English:
Translate the following Cantonese text
into English, referring to the examples
below:
Example 1: Cantonese: (e.g. 1) English:
(e.g. 1)
Example 2: Cantonese: (e.g. 2) English:
(e.g. 2)
Example 3: Cantonese: (e.g. 3) English:
(e.g. 3)
Text to Translate:
(Text to translate)
Ensure the translation is accurate and nat-
ural, preserving the original meaning and
using concise and fluent English expres-
sion.
ONLY RETURN THE TRANSLATION.
DO NOT EXPLAIN.
For zero-shot evaluation, similar prompts were
used but without the few-shot examples and refer-
ences to them.
F.1
Translation Results Evaluation
We used manual evaluation for the translation task.
The BLEU score was not used in this work to eval-
uate the translation task because it relied on exact
matches between the answer and the gold standard,
which is often not ideal for pairs that involve Writ-
ten Chinese. Translation between closely related
varieties in a diglossic situation is similar to stylis-
tic change, with a wide range of acceptable answers.
One kind of translation strategy would be favoured
by using a BLEU score, and models that could have
been rated excellent by Hong Kong users would
be penalised. Adding to this is the lack of exist-
ing libraries that handle orthographic variants well
enough to conduct a fair string comparison with the
gold standard. This is why manual annotation was
opted for by us. This is to address the problems of
an earlier benchmark (Jiang et al., 2024), outlined
in Appendix A.
A graphical user interface based on Label Stu-
dio was configured such that annotators (paid un-
dergraduate students and teaching assistants from
Hong Kong) can highlight mistakes in the trans-
lated text for the following categories:
1. Additional words
2. Collocation
3. Inconsistent Terminology
4. Literal Translation
5. Mistranslation
6. Mixed up Cantonese-Mandarin
7. Orthography
8. Omission (Labelled in the source text)
9. Register Issues
10. Ungrammatical
11. Unintelligibility
12. Unnatural Code-mixing
The annotators were required to label the five
most relevant issues in the translated text, and ev-
ery sentence was evaluated by four annotators. It
should be noted that translation performance can
be highly subjective, especially for languages like
Cantonese that do not have a well-defined standard
norm for its written form.
Some models exhibited a tendency to repeat the
last sentence excessively, resulting in extra words
beyond the expected translation. To account for
this, if the "Additional words" labelled constituted
more than half of the generated output, the labelled
22

--- Page 23 ---

additional words were removed and not counted as
erroneous output. The accuracy of the translation
was then calculated using the following formula:
accuracy = lentarget −lenlabelled errortarget
lentarget + lenlabelled errorsource
(1)
The average score across all translation pairs of
all models can be found in Table 8.
G
Summarisation
The following prompt was used in the summarisa-
tion task evaluation:
。
200
，
，
、
，
。
##
（
）：(Original Text)
##
：
English translation of the prompt:
We will provide a text written in Can-
tonese. Please summarise the text into a
200 words Cantonese text while preserv-
ing the core message and theme. Ensure
the content is accurate, the writing flows
smoothly and coherently, and it remains
faithful to the original meaning.
## Text（Original text）：(Original
Text)
## Expected Output：
G.1
Summarisation Results Evaluation
For the summarisation outputs, annotators (paid un-
dergraduate students and research assistants from
Hong Kong) were given the following rubric and
tasked to give a score for each output. Under each
category, the annotators rated whether the summary
passes (5 points) or fails (3 points for minor viola-
tion, 1 point for complete failure).
Task instructions given to annotators:
TED
（
）
，
，
Google Form
English Translation:
You will receive multiple Cantonese tran-
scripts of TED talks or passages (Origi-
nal Text). Your task is to read the original
text and then score different versions of
the summaries according to the specified
guidelines. First, you need to read the
original text to understand the main idea
of the article. You may read it more than
once. Then, begin reading the summaries
one by one. The actual scoring will be
conducted on a Google Form.
The annotation rubrics were explained in detail
in face-to-face meetings and in online working chat.
A manually-crafted marking scheme was prepared
to ease the annotation task.
Annotation Rubrics (English Translation):
• Category: Relevance
The summary successfully retains the key
points of the original text, rather than extract-
ing overly verbose content, judged by whether
the summary contains all the key points listed
in the reference marking scheme provided.
Omitted content and problematic sentences
should be added as a comment if a fail (3 or
1) rating is given.
• Category: Accuracy
The summary correctly extracted information
from the original text, judging by comparing
sentence by sentence with the original text, to
identify any completely opposite or fabricated
content. Sentences that contain incorrect in-
formation should be added as a comment if a
fail rating is given.
• Category: Fluency
The words and sentence structures used in the
summary are smooth and conforming to Can-
tonese usage. This score does not require ref-
erencing the original text. The text should be
acceptable for reading on a news programme.
If words that are exclusive to Written Chinese
(e.g.
,
,
) or grammatical issues were
found, a fail rating should be given.
• Category: Coherence
The sentences and paragraphs in the summary
are logically coherent, with appropriate struc-
ture and adequate sentential connection. This
score does not require referencing the original
text.
23

--- Page 24 ---

Score Calculation: Scores from all raters on the
four categories were aggregated and normalised
to 100%, then a length penalty is applied, based
on its length: if the summary exceeds 500 charac-
ters, a penalty factor is calculated by reducing the
score proportionally to the excess length, ensuring
the penalty factor remains between 0 and 1. The
resultant score can be found in Table 8.
H
Sentiment Analysis
As detailed in Section 3.5, the sentiment analysis
dataset consists of an existing dataset known as the
OpenRice dataset (toastynews, 2020) and a newly
created dataset. The newly created datasets were
sourced from Facebook comments and filtered by
CantoneseDetect (Lau et al., 2024). Paid interns
(undergraduate students from Hong Kong) then la-
belled the comments with the following guidelines:
(posi-
tive)、
(negative)，
(neutral)。
：
(positive),
(negative),
(neutral)。
，
。
(positive)
1.
:
、
、
、
、
。
2.
:
、
、
。
3.
: “
！
！”
4.
:
“
，
！”
(negative)
1.
:
、
、
、
、
、
。
2.
:
、
、
。
3.
: “
，
！”
4.
: “
，
！”
(neutral)
1.
:
、
、
。
2.
:
、
，
。
3.
: “
32
。”
4.
: “
。”
Translation in English:
This task aims to determine whether the
sentiment expressed in a given text is
positive, negative, or neutral. We will
use three labels: positive, negative, and
neutral. Please carefully read the follow-
ing guidelines to ensure consistency and
accuracy in labelling.
Positive
1. Meaning: Expresses happiness, sat-
isfaction, appreciation, optimism,
or other positive emotions.
2. Explanation: The content of the
text makes people feel good and
happy, or has a positive evaluation
of things.
3. Examples:
(a) “The food in this restaurant is
really delicious! The service is
also great!”
(b) “The weather is so nice today, it
makes me feel good!”
Negative
1. Meaning: Expresses unhappiness,
dissatisfaction, criticism, anger, sad-
ness, or other negative emotions.
2. Explanation: The content of the text
makes people feel bad, unhappy, or
has a negative evaluation of things.
3. Examples:
(a) “The service attitude of this ho-
tel is really bad, I will never
come again!”
24

--- Page 25 ---

(b) “This report is not clear at all, it
makes me very angry!”
Neutral
1. Meaning: Expresses objective facts,
information, or content without ob-
vious emotions.
2. Explanation: The text mainly states
facts, provides information, and
has no obvious positive or negative
emotional tendency.
3. Examples:
(a) “The highest temperature in
Hong Kong today is 32 degrees
Celsius.”
(b) “The main function of this prod-
uct is to help users manage their
time.”
The average score across the two datasets of each
model can be found in Table 8.
25

```
