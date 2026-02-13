---
title: "2025-Kanepajs-LAG-MMLU Benchmarking Frontier LLM Understanding in - PDF Extract"
source_pdf: "2025-Kanepajs-LAG-MMLU Benchmarking Frontier LLM Understanding in.pdf"
pages: 17
extracted_at: "2026-02-13T09:15:44.465264"
---

# PDF Extract: 2025-Kanepajs-LAG-MMLU Benchmarking Frontier LLM Understanding in

**Source PDF:** 2025-Kanepajs-LAG-MMLU Benchmarking Frontier LLM Understanding in.pdf
**Total Pages:** 17

---

## Content

```
--- Page 1 ---

LAG-MMLU: Benchmarking Frontier LLM Understanding in Latvian
and Giriama
Naome A. Etori1,4, Kevin Lu3, Randu Karisa4 and Arturs Kanepajs2
1University of Minnesota-Twin Cities
2Independent Researcher
3Bellarmine College Preparatory
4Masakhane
etori001@umn.edu
Abstract
As large language models (LLMs) rapidly
advance, evaluating their performance is
critical.
LLMs are trained on multi-
lingual data, but their reasoning abili-
ties are mainly evaluated using English
datasets. Hence, robust evaluation frame-
works are needed using high-quality non-
English datasets, especially low-resource
languages (LRLs). This study evaluates
eight state-of-the-art (SOTA) LLMs on Lat-
vian and Giriama using a Massive Mul-
titask Language Understanding (MMLU)
subset curated with native speakers for lin-
guistic and cultural relevance. Giriama is
benchmarked for the first time. Our evalua-
tion shows that OpenAI’s o1 model outper-
forms others across all languages, scoring
92.8% in English, 88.8% in Latvian, and
70.8% in Giriama on 0-shot tasks. Mistral-
large (35.6%) and Llama-70B IT (41%)
have weak performance, on both Latvian
and Giriama. Our results underscore the
need for localized benchmarks and human
evaluations in advancing cultural AI con-
textualization.
1
Introduction
Large Language Models (LLMs) have significantly
advanced natural language processing (NLP), en-
abling progress in tasks such as machine trans-
lation(MT) (Wang et al., 2023), knowledge rea-
soning (Singh et al., 2024), and Conversational
(Etori and Gini, 2024b). Models like GPT-4 (Hurst
et al., 2024; OpenAI, 2024), LLaMA (Touvron
et al., 2023; Dubey et al., 2024a), and BLOOM
(Le Scao et al., 2023) have demonstrated remark-
able performance, attributed mainly to their pre-
training on vast, multilingual datasets. Therefore,
it is crucial to rigorously assess LLMs’ ability to
represent knowledge and reason across multiple
languages.(Koto et al., 2023; Adelani et al., 2024).
Figure 1: Distribution of subjects and categories of
the subjects in LAG-MMLU. We included subjects
with a frequency of 7 and above. 55 out of 57 sub-
jects are represented. See more details in Table 4
in the appendix.
Benchmarking is critical in assessing LLM’s per-
formance and capabilities across diverse tasks due
to its standardized evaluation frameworks. How-
ever, the limited availability of robust multilingual
benchmarks has led to the continued focus on a few
common and widely spoken languages in LLMs
and within the NLP research community (Dar`gis
et al., 2024a; Li et al., 2023).
As a result, some existing frameworks, such
as Massive Multitask Language Understanding
(MMLU) (Hendrycks et al., 2020), are widely
recognized as gold standards for evaluating the
capabilities of large language models (LLMs).
MMLU assesses knowledge across various sub-
ject domains, including STEM, humanities, and
social sciences. For instance, MMLU was recently
featured in the Gpt-4o system card (Hurst et al.,
2024). Due to its reliance on U.S. English, its
applicability for assessing multilingual capabili-
ties is limited unless the dataset is translated into
different languages. However, translating English
arXiv:2503.11911v2  [cs.CL]  18 Mar 2025

--- Page 2 ---

benchmarks introduces biases and noise and fails
to account for region-specific and cultural under-
standing. This may also add another layer of cul-
tural misalignment of the target language, such as
questions about U.S. laws or customs (Liu et al.,
2023).
Recently, NLP researchers have addressed this
limitation; several diverse linguistic and cul-
tural context MMLU evaluation benchmarks have
been developed to address the gap, such as Ara-
bicMMLU (Koto et al., 2024) evaluates tasks
from North Africa, the Levant, and the Gulf, In-
doMMLU (Koto et al., 2023) incorporates Indone-
sia’s local languages and cultures.
Others in-
clude, CMMLU (Li et al., 2023), KMMLU (Son
et al., 2024),TurkishMMLU (Yüksel et al., 2024),
PersianMMLU (Ghahroodi et al., 2024), Global
MMLU (Singh et al., 2024) evaluates cultural and
linguistic bias in 42 languages.
Despite these advancements, significant gaps
remain for African LRLs and some Eastern Euro-
pean languages. Our work narrows this gap, by
including Giriama, a LRL language spoken by ap-
proximately 2.6 million people in Kenya, which is
currently absent from existing NLP benchmarks.
Similarly, even though the Latvian language has
been benchmarked before EU20-MMLU (Thell-
mann et al., 2024), with relatively high-quality
datasets, the datasets lack human-curated trans-
lations. As a result, they encounter challenges,
including inaccurate auto-translations that compro-
mise reliable evaluations. Giriama, in particular,
has a limited digital presence and has historically
been underrepresented in linguistic resources, mak-
ing this the first multilingual benchmark developed
explicitly for the language. Our contributions can
be summarized as follows:
• Novel Datasets: we present LAG-MMLU, a
curated dataset that includes Giriama’s first
gold-standard (human-translated) collection,
alongside two silver-standard datasets for Lat-
vian: one machine-translated and another
machine-translated with subsequent human
curation. Each dataset comprises 500 samples,
randomly selected from the original MMLU
benchmark. And will be publicly available
for further research in multilingual NLP
• Multilingual Comparative Analysis: We
evaluate the performance of LLMs on two
multilingual datasets, Giriama and Latvian,
highlighting their understanding of complex
knowledge representation.
• Model Evaluation: We evaluate the perfor-
mance of eight (8) state-of-the-art (SOTA)
closed and open-source LLMs using the In-
spect AI framework. Our analysis includes
both zero-shot and few-shot evaluations, with
and without applying chain-of-thought (CoT)
reasoning, for comprehensive insights.
• Statistical Validation: We employed confi-
dence intervals (CI) and standard errors (SE)
for statistical significance to ensure the robust-
ness of our findings.
Driven by these considerations, the experiments
in this paper aim to address the following key ques-
tions:
• Q1: Which LLM exhibits the highest perfor-
mance and comprehension across 55 tasks in
both Latvian and Giriama?
• Q2: How does the performances of the three
language datasets compare when evaluated
across SOTA LLMs
• Q3:Does chain-of-thought (CoT) reasoning
enhance performance?
2
Related works
2.1
Multilingual Models Across Cultures
The evaluation of the multilingual capabilities of
LLMs has garnered significant attention.
This
has led to increased research exploring their per-
formance across diverse linguistic landscapes.
SOTA massively multilingual language Models
(MMLMs) such as mBERT (Devlin, 2018), XLMR
(Conneau, 2019), and mT5 (Xue, 2020) support
100+ languages worldwide and have shown ex-
ceptional proficiency in understanding text across
diverse linguistic contexts. While encoder-decoder
architectures like mT5 (Xue, 2020) also demon-
strate strong capabilities in natural language gener-
ation(NLG).
Additionally, generative models like GPT-4
(Achiam et al., 2023), LLaMA (Touvron et al.,
2023), BLOOM (Le Scao et al., 2023), and
BLOOMZ (Muennighoff et al., 2022) are also gain-
ing world recognition for their contributions to ad-
vancing natural language generation (NLG) and
understanding. Significant challenges remain in
ensuring cultural sensitivity and language equity
(Dawson et al., 2024).
Several research efforts have shown that multi-
lingual models perform well in high-resource lan-
guages (HRLs) like English and French, but still
struggle with very LRLs (Li et al., 2024; Hedderich

--- Page 3 ---

et al., 2020; Ranathunga and De Silva, 2022), par-
ticularly in Africa (Adelani et al., 2021; Alabi et al.,
2022; Adebara et al., 2024) and South Asia (Lahoti
et al., 2022; Baruah et al., 2021), due to limited
training data (Adebara et al., 2024; Magueresse
et al., 2020). Challenges such as cultural nuances
(Romero et al., 2024; Winata et al., 2024), dialectal
variation (Faisal et al., 2024), and code-switching
(Winata et al., 2021; Etori and Gini, 2024a) fur-
ther hinder model performance. While efforts like
cross-lingual transfer learning and culturally rel-
evant datasets have been made to address these
issues (Hu et al., 2020; Winata et al., 2022; Liu
et al., 2021), performance gaps persist in under-
represented languages, especially African (Adelani
et al., 2024).
2.2
Multilingual LLMs Evaluation
The evaluation of LLMs has evolved significantly
with the development of various benchmarks to as-
sess their performance across tasks and languages.
Early benchmarks like GLUE (Wang, 2018) and
SuperGLUE (Wang et al., 2019) focused on natural
language understanding (NLU) tasks in English, us-
ing datasets of different sizes. Multilingual evalua-
tion later gained attention with benchmarks such as
XGLUE (Liang et al., 2020) XTREME (Hu et al.,
2020), and XTREME-R (Ruder et al., 2021), which
extended the evaluation to over 20 languages, em-
phasizing cross-lingual transfer capabilities, how-
ever, the coverage of Baltic and African languages
in XTREME is limited. For natural language gen-
eration (NLG), the GEM benchmark introduced by
Gehrmann et al. (2021) includes tasks like transla-
tion, summarization, and description generation in
multiple languages.
As LLMs became extensive and with near
human-level performance, evaluation tasks shifted
to emphasize reasoning and real-world knowledge.
Benchmarks like MMLU (Hendrycks et al., 2020),
HellaSwag (Zellers et al., 2019), HELM (Liang
et al., 2022), LAMBADA (Paperno et al., 2016)
and WinoGrande (Sakaguchi et al., 2021) became
standards for assessing reasoning abilities and
knowledge representation. Models like GPT-4o
and LLaMA have been evaluated on some bench-
marks, with GPT-4o achieving human-level perfor-
mance on various tasks (Hurst et al., 2024).
Recent research has focused on the develop-
ment of multilingual datasets to more accurately
capture linguistic and cultural diversity.
Initia-
tives such as CVQA (Romero et al., 2024), World-
Cuisines (Winata et al., 2024), D-PLACE (Kirby
et al., 2016), Wikipedia Cultural Diversity Dataset
(Miquel-Ribé and Laniado, 2019), TeDDi Sam-
ple (Moran et al., 2022), Cheetah (Adebara et al.,
2024), Irokobench (Ifeoluwa Adelani et al., 2024),
and CulturalBench (Chiu et al., 2024) have made
significant progress in improving the representa-
tion within multilingual models.
Leveraging community-driven approaches to de-
velop localized datasets ensures that diverse lin-
guistic and cultural nuances are effectively incor-
porated into language technologies. Underscoring
cultural context in which language is used rather
than relying solely on translation-based approaches
(Tiedemann, 2020).
2.3
Human evaluation of multilingual models
The development of evaluation datasets for specific
languages involves significant human resources.
Therefore, a widely used strategy is to apply ma-
chine translation, with or without manual post-
editing (Dar`gis et al., 2024a).
Human ability to understand language is general,
flexible, and robust (Wang, 2018; Lin and Och,
2004). Hence, human evaluations are typically
considered the gold standard in NLG to assess the
effectiveness of multilingual models (Clark et al.,
2021; Chiang and Lee, 2023), particularly in eval-
uating their ability to generate text that aligns with
diverse linguistic and cultural contexts.
The use of automatic metrics such as BLEU (Pa-
pineni et al., 2002) and ROUGE (Lin, 2004), even
though commonly used, often fail to capture cul-
tural nuances, making human evaluation essential
for a more comprehensive assessment (Kocmi et al.,
2021). Human evaluations are essential for assess-
ing how well multilingual models handle grammat-
ical, syntactical, and contextual differences, partic-
ularly in LRLs (Costa-jussà et al., 2022). Human
raters are better at identifying these nuances, using
criteria such as appropriateness, bias detection, and
cultural sensitivity (Choenni et al., 2024).
3
Methodology
3.1
LAG-MMLU Dataset
We carefully curated a shuffled subset of 500
samples from the original MMLU benchmark
(Hendrycks et al., 2021). The original MMLU
contains over 15,000 multiple-choice questions
(MCQs) spanning 57 subjects across disciplines
such as social science, history, and STEM. Sourced
from publicly available materials, including prac-
tice exams like the GRE and USMLE. The dataset

--- Page 4 ---

Language
Question and Answers (Question subject: miscellaneous)
English
According to the children’s nursery rhyme what type of ocean did Columbus sail in 1492?
A: calm X, B: blue ✓, C: windy X, D: really big X
Giriama
Kulingana na wira wa kitalu cha ahoho ni aina yani ya bahari ambayo Columbus wasafiri
makathi ga 1492?
A: Kuhurira X, B: buluu ✓, C: peho X, D: bomu jeri X
Latvian
Saskan, ¯a ar b¯ernu b¯ernud¯arza atskan, u, k¯ada veida oke¯anu Kolumbs ku ‘goja 1492. gad¯a?
(autotranslated)
A: Mier¯ıgs X, B: zils ✓, C: V¯ejains X, D: L, oti liels X
Latvian
Saskan, ¯a ar b¯ernud¯arza pantin, u, k¯ada veida oke¯anu Kolumbs ku ‘goja 1492. gad¯a?
(autotranslated & edited)
A: Mier¯ıgu X, B: Zilu ✓, C: V¯ejainu X, D: L, oti lielu X
Table 1: Sample question translated into Giriama and Latvian (AT: autotranslated, AT+E: autotranslated and edited)
with correct answers marked (✓) and incorrect answers marked (X). The correct answer "blue" in English refers to the
popular children’s rhyme "In 1492, Columbus sailed the ocean blue," which is a cultural reference that may not resonate
in Latvian or Giriama without further explanation.
categorizes questions from elementary to advanced
professional levels.
3.2
Dataset Selection Process
To ensure a representative and diverse evaluation
dataset, we began by shuffling the full MMLU
dataset. The shuffling step ensured randomization
across topics, avoiding biases from subject-specific
clustering. Following this, the top 500 entries were
selected for inclusion. The dataset was then format-
ted using a custom pipeline that maps records to
standardized MCQ samples, preserving key fields
such as questions, answers, and metadata. To en-
sure an evenly distributed, high-quality subset.
3.3
Languages covered
LAG-MMLU evaluates two languages:
Latvian (lav):
Latvian1 is an East Baltic lan-
guage that belongs to the Indo-European language
family and is spoken in the Baltic region. With
around 2 million speakers worldwide, Latvian is
the official language of Latvia and is spoken as
a second language by over 500,000 non-Latvians
within the country (Smith-Sivertsen, 2004). Lat-
vian is more morphologically complex (Paikens
et al., 2024) than English, and there is still limited
research and representation in widely used multi-
lingual benchmarks on NLP for the language. The
complexity further adds to the difficulty of LLMs
processing (Dar`gis et al., 2024b).
Giriama (nyf):
Giriama (Kigiryama)2, is a
Bantu language spoken by approx. 700,000 people,
primarily in the coastal part of Kenya. It is one of
the nine (9) ethnic groups or tribes that make up
Mijikenda languages—classified under the North-
eastern Bantu subgroup of the Niger-Congo family.
Predominantly oral, Giriama has limited digital
1(Smith-Sivertsen, 2004)
2Giriama people
texts, though recent efforts have promoted liter-
acy using the Latin alphabet. Despite these ef-
forts, Giriama remains under-resourced regarding
linguistic and digital resources.
3.3.1
Dataset collection
Our random shuffled dataset collected in three sets:
Baseline Dataset:
The process began with the
original MMLU English dataset, comprising 500
questions. These questions form the baseline, for
comparison and evaluation in subsequent steps.
Machine Translations:
The baseline questions
were translated into Latvian using the MyMemory
API 3(MyMemory, 2024). The MyMemory API is
a machine translation (MT) system that combines
translation memory (TM) with statistical methods.
Using a large repository of human-translated texts
retrieves relevant segments for accurate, context-
aware translations, hence a hybrid approach.
Human-Edited Translations:
To ensure ac-
curacy and cultural inclusivity, the machine-
translated Latvian questions were reviewed and
curated by human translators. Additionally, human
experts who are native speakers, translated the En-
glish questions into Giriama, to ensure high-quality
datasets.
3.3.2
Dataset Statistics
The dataset comprises 55 tasks across four do-
mains: Humanities (34%, 170 tasks), STEM
(22%, 112 tasks), Social Sciences (20%, 99 tasks),
and Other (24%, 119 tasks). Professional law (57
tasks), moral scenarios (31 tasks), mathematics
(17 tasks), psychology (47 tasks across subfields),
and clinical knowledge (15 tasks) have the highest
representations. The random selection effectively
captured 55 of the original 57 tasks, hence 96.5%
retention rate as shown in Table 4 at the Appendix.
3https://mymemory.translated.net/

--- Page 5 ---

Figure 2: Frontier LLMs in Latvian and Giriama Dataset and Benchmarking pipeline
3.3.3
Translations and annotation
We recruited one Giriama language coordinator,
who also doubled as a translator. Holds a mas-
ter’s degree in computer science and is a native
speaker of the language with extensive experience
as a translator. As for the Latvian language, a
Latvian-Native translator and annotator reviewed
and edited the machine-translated questions. The
goal is to correct any errors that could hinder com-
prehension or lead to misinterpretations of the an-
swers.
Quality Check: Language coordinators thor-
oughly reviewed and corrected poorly translated
sentences to preserve the highest quality.
The
translator was compensated after the quality as-
surance phase, aligning payments with the local
living wage to recognize their efforts fairly.
3.4
Task Overview
We evaluate the multilingual understanding of open
and closed LLMs using translated questions from
the MMLU benchmark, which tests world knowl-
edge and problem-solving skills in zero-shot and
few-shot settings. We assess model performance
across three languages—English, Latvian, and
Giriama—using human-annotated translations of
500 questions.
3.5
Inspect Evaluation Framework
We employed the UK AISI Inspect framework (AI
Safety Institute, 2024) 4 to evaluate LAG-MMLU
benchmark across zero-shot, few-shot, and CoT
4https://github.com/UKGovernmentBEIS/
inspect_ai
reasoning. Inspect facilitates modular evaluation
through dynamic prompt engineering, dataset fil-
tering, and scoring metrics such as exact match and
choice-based evaluation.
3.6
Model Choice
We used closed and open large LLMs to evaluate
their performance. 5 As shown in Table 2.
Closed LLMs: The four closed SOTA models
selected for this study include OpenAI o1 (Jaech
et al., 2024), Claude 3.5 Sonnet (Anthropic, 2024),
GPT-4o (Hurst et al., 2024), and Gemini 1.5 pro
(Team et al., 2024). These models were chosen due
to their established performance and popularity in
handling various tasks. Recent work has shown
that proprietary models exhibit better multilingual
capabilities (Ahuja et al., 2023). However, their
pre-training, fine-tuning processes and model size
are not disclosed.
Open LLMs: We evaluate four open models:
Meta-Llama-3.3 70B IT (Dubey et al., 2024b),
Mistral-Large (Jiang et al., 2023),DeepSeek-V3
(Liu et al., 2024) and DeepSeek-R1 (Guo et al.,
2025). Both decoder-only models are effective for
multilingual and LRLs. These models are openly
available under licenses ranging from research to
fully open and permissive, providing transparency
in their architecture. However, the exact composi-
tion of their training data is, in fact, not known. De-
termining whether Giriama or Latvian is included
in the pretraining data of models is challenging.
5Models: claude-3-5-sonnet-20241022, gemini-1.5-pro-
002, gpt-4o-2024-08-06, Meta-Llama-3.3-70B-Instruct-Turbo,
mistral-large-2407,o1, DeepSeek-V3 and DeepSeek-R1

--- Page 6 ---

Figure 3: Examples of English-Latvian translated;
topics include high-school macroeconomics, high-
school geography, and miscellaneous
3.7
Evaluation metrics
We evaluated the performance of all LLMs with
an accuracy score. For each model, accuracy was
computed as the proportion of correct outputs from
a test set comprising 500 samples. We calculate the
(binomial) standard error to account for uncertainty
in the performance estimates.
0-Shot Evaluation: We implement the 0-shot
evaluation, on the entire dataset without filtering
based on the number of available examples per
subject. In this configuration, the prompt provided
to the model consists solely of the test question.
Few-Shot Evaluation: We employ a 5-shot
prompt-based evaluation, retaining subjects with
at least six samples—one reserved as the test
instance.
For each test sample, the function
mmlu_n_shot_solver(n=5)retrieves
five
example question-answer pairs from the subject’s
development set.
These are formatted using
the MMLU_MULTISHOT_PROMPT_TEMPLATE,
which presents the examples followed by the test
question. The model is then conditioned on this
prompt, generating a single-token answer via
generate(max_tokens=1).See Figure 7.
Figure 4: Examples of English-Giriama translated;
topics such as high-school macroeconomics, high-
school geography, and miscellaneous
4
Experiment Setup
We evaluate model performance using:
Shots, CoT, and Temperature Settings:
We
evaluate our Models under 0-shot and 5-shot set-
tings, with and without chain-of-thought (CoT)
reasoning. A temperature of 0 was applied uni-
formly for deterministic behavior, with GPT-4o
also tested at temperature 1 (Table 3). The evalu-
ation covered three datasets, comprising 55 tasks
across four categories (Figure 1). 6
4.1
Results and Discussion
4.1.1
Results across all models
Table 2 presents the performance of all LLMs eval-
uated in three languages—English, Latvian, and
Giriama—in both zero-shot and five-shot settings,
with and without CoT prompting. Performance
is reported as accuracy with confidence intervals
(CIs). As expected, the OpenAI-o1 model stands
out as the top performer among both closed and
open models, with remarkable accuracy of 92.8%
in English, 88.8% in Latvian, and 70.8% in the
0-shot test without chain-of-thought (CoT), rein-
6https://github.com/akanepajs/
capabilities_lv_giriama/tree/main/MMLU

--- Page 7 ---

Model
COT
English Accuracy (%)
Latvian Accuracy (%)
Giriama Accuracy (%)
0-shot
5-shot
0-shot
5-shot
0-shot
5-shot
Open AI o1
✗
92.8 [90.5, 95.1]
–
88.8 [86.0, 91.6]
–
70.8 [66.8, 74.8]
–
GPT-4o
✗
83.6 [80.4, 86.8]
–
75.6 [71.8, 79.4]
78.0 [74.4, 81.6]
53.2 [48.8, 57.6]
–
✓
–
84.5 [81.3, 87.7]
79.5 [76.0, 83.0]
–
–
62.3 [58.1, 66.5]
Claude 3.5
✗
88.8 [86.0, 91.6]
–
78.2 [74.6, 81.8]
–
54.8 [50.4, 59.2]
–
✓
–
87.1 [84.2, 90.0]
–
83.0 [79.7, 86.3]
–
60.9 [56.6, 65.2]
Gemini 1.5 Pro
✗
84.0 [80.8, 87.2]
–
70.3 [66.3, 74.3]
–
51.4 [47.0, 55.8]
–
✓
–
85.4 [82.3, 88.5]
–
79.9 [76.4, 83.4]
–
61.8 [57.5, 66.1]
DeepSeek-V3
✗
87.6 [84.7, 90.5]
–
70.7 [66.7, 74.7]
–
49.8 [45.4, 54.2]
–
✓
–
87.9 [85.0, 90.8]
–
76.1 [72.4, 79.8]
–
52.3 [47.9, 56.7]
Llama-70B IT
✗
81.0 [77.6, 84.4]
–
57.3 [53.0, 61.6]
–
41.0 [36.7, 45.3]
–
Mistral-large
✗
80.0 [76.5, 83.5]
–
49.3 [44.9, 53.7]
–
35.6 [31.4, 39.8]
–
DeepSeek-R1
✗
81.4 [78.0, 84.8]
–
70.2 [66.2, 74.2]
–
52.2 [47.8, 56.6]
–
Table 2: Performance of Models on LAG-MMLU. The table shows Accuracy (%) with 95% Confidence
Intervals (CI) across three languages (English, Latvian, and Giriama) under 0-shot and 5-shot settings.
Results are presented for models with and without Chain-of-Thought (CoT) prompting, where (✗)
represents No CoT and (✓) represents CoT. (Also See Table 5). All experiments were conducted with the
temperature set to 0. OpenAI-o1 achieves the highest overall accuracy (92.8%) across the languages.
The symbol - indicates that no experiment was conducted for that setting.
English
Latvian
Giriama
Model
COT
0-shot
5-shot
0-shot
5-shot
0-shot
5-shot
GPT_4o
✗
0.830 ± 0.017
–
0.762 ± 0.019
0.790 ± 0.018
0.514 ± 0.022
–
✓
–
0.847 ± 0.016
–
0.802 ± 0.018
–
0.582 ± 0.022
Table 3: Performance of GPT_4o. Accuracy has standard error (±) under 0-shot and 5-shot settings for
English, Latvian, and Giriama, using the temperature set =1. Results are shown for both the no CoT (✗)
and CoT (✓). The symbol - indicates that no data is reported.
forcing its general ability to handle a broad spec-
trum of tasks effectively in multiple languages and
serves as the benchmark for other models. Even in
LRLs like Latvian or Giriama, they tend to main-
tain a comfortable margin over other models. In
addition, Claude 3.5 Sonnet demonstrates strong
results, achieving 87.1% in 5-shot, further solid-
ifying its position as a solid closed model con-
tender. Gemini-1.5-pro also shows competitive
performance, reaching 85.4% in the 5-shot test,
but still trails behind its closed model’s counter-
parts, particularly the GPT-4o.
The open-sourced models show some impres-
sive performances, albeit generally weaker than
closed-source. DeepSeek-V3 leads the open mod-
els, achieving 87.6% in the 0-shot test and 87.9%
in the 5-shot test. While these results indicate
strong performance, particularly in the 5-shot task,
they still fall short of matching the best-performing
closed models across languages. For instance, the
open models like Mistral-Large, Llama 3.3 70B
IT, have low accuracies across the tasks, espe-
cially on Latvian and Giriama with a CI of 31.4%-
45.3%.
The results reinforce the strengths of closed-
source modelsin providing a robust performance.
This advantage is apparent in multilingual settings
(across resource-rich and lower-resource languages
like Latvian or Giriama) and in their ability to
approach complex tasks with minimal prompting.
Nevertheless, open models like DeepSeek-V3 still
manage to showcase competitive performance, par-
ticularly when prompted with 5-shot examples,
open models hold potential for unique use cases
where customization, transparency, or self-hosting
becomes critical factors. This performance gap
also underscores that, while the top closed models
set a high benchmark, open models remain valu-
able contenders.
Llama-70B IT and Mistral-Large both exhibit

--- Page 8 ---

Figure 5: Performance of All Models on LAG-MMLU on English, Latvian, and Giriama (0-shot).
OpenAI-o1 shows the best performance then claude 3.5 Sonnet. Mistral-large underperforms in LRLs.
Figure 6: 0-shot vs. 5-shot performance across
four models. Few-shot learning improves most
models, except Claude 3.5, which drops by 1.7%.
weaker performance, scoring around 80.0–81.0%
under the 0-shot English.
while DeepSeek-R1
achieves a slightly higher accuracy of 81.4%.
However, their performance drops significantly
in LRLs, with Llama-70B IT 57.3% in Latvian
and 41.0% in Giriama, and Mistral-Large per-
forming even lower at 49.3% (Latvian) and 35.6%
(Giriama). In contrast, DeepSeek-R1 maintains a
relatively stronger performance at 70.2% (Latvian)
and 52.2% (Giriama). Still, none of them reach the
higher English accuracy of DeepSeek-V3 (87.6%
in 0-shot).
4.1.2
Performance Across All Languages
Table 2 demonstrates that across all conditions all
evaluated models perform best in English, which is
unsurprising given the abundant training data avail-
able for this language, followed by Latvian, with
Giriama consistently showing the lowest scores.
For instance, the closed-source OpenAI-o1 model
reaches an accuracy of 92.8% in English, while its
performance in Latvian and Giriama—though still
high—shows a measurable decline (with Latvian
accuracy at 88.8% and Giriama dropping further
to 70.8%).
In contrast,
open-source models such as
Llama3.3 70B IT and Mistral-Large exhibit
a weak performance drop when shifting from
English to these LRLs.
For example, while
DeepSeek-V3 scores competitively in English
(87.6% in the 0-shot setting), its accuracy in
Giriama falls by a larger margin relative to the
closed-source models. closed-source models main-
tain a relatively stable performance across all lan-
guages, likely due to extensive pretraining with
robust multilingual data and continual fine-tuning.
Despite their black boxes; their internal architec-
tures, training data, and fine-tuning methodologies
remain largely opaque.
4.1.3
CoT vs. non-CoT Performance
Many benchmark results such as CMMLU (Li
et al., 2023), GSM8K(Zhong et al., 2024), and
KMMLU (Son et al., 2024) have demonstrated that
CoT prompting has improved the performance on
multitask evaluations. Table 2 and Figure 5 demon-
strate that enabling CoT prompting yields substan-
tial accuracy improvements for most models. We

--- Page 9 ---

have four models—GPT4_o, Claude 3.5 Sonnet,
Gemini 1.5 Pro, and DeepSeek-V3— that employ
CoT prompting, and they generally achieve sig-
nificant accuracy gains compared to their no-CoT
baselines. For example, Claude 3.5 Sonnet sees
an increase from 54.8% to 60.9% in the Giriama
0-shot setting when CoT is enabled, but there is a
slight decrease in performance on the English lan-
guage when CoT is enabled (from 88.8% to 87.1%).
GPT4_o experiences a comparable improvement
from 75.6% to 79.5% in the Latvian 0-shot set-
ting when CoT is enabled. This pattern suggests
that both closed-source and open-sourced, benefit
most from CoT’s structured approach. COT has
minimal effect on English performance, as mod-
els already achieve high zero-shot accuracy (e.g.,
GPT-4o: 0.836 →0.845).
4.1.4
Few-Shot Performance
Shifting from 0-shot to 5-shot prompts benefits
every model in Table 2 and Table 3, both closed-
source and open-source models benefit from few-
shot prompting; however, the degree of improve-
ment from 0-shot to 5-shot vary across models. In
our experiments, the 5-shot setting—proved to be
a critical factor in enhancing model performance.
GPT-4o shows a 0.9% improvement, indicating a
moderate benefit from few-shot learning. Gemini
1.5 gains the most, with a 1.4% increase, while
DeepSeek-V3 experiences a smaller improvement
of 0.3%. However, Claude 3.5 Sonnet performs
worse with few-shot learning, exhibiting a 1.7%
decrease in accuracy as shown in Figure 6.
5
Conclusion
We introduce the LAG-MMLU Benchmark, a mul-
tilingual evaluation dataset comprising 500 MCQs
across 55 subjects or tasks, originally sourced
from MMLU. The dataset includes: (1) human-
translated Giriama questions and (2) machine-
translated, human-edited Latvian questions. This
benchmark is designed to assess multi-task lan-
guage understanding capabilities in Latvian and
Giriama. Our findings reveal significant perfor-
mance gaps in existing SOTA LLMs, particularly
in Giriama, where models underperformed even
in few-shot settings. Gemini 1.5 Pro exhibits the
most significant improvement with CoT enabled,
gaining +9.6 and +10.4 respectively in Latvian
and Giriama. English performance remains strong,
Latvian and Giriama results indicate substantial
room for improvement, reinforcing the need for
dedicated training data, fine-tuning, and linguistic
adaptations for LRLs. We believe that the LAG-
MMLU Benchmark will serve as a valuable re-
source for the LRL research community.
6
Limitations
LAG-MMLU benchmark offers valuable insights
for the NLP community but faces several limita-
tions that future work must address. As mentioned,
native speakers curated the dataset to ensure high
translation quality, but errors from automatic trans-
lation persist. For instance, 6% of the MMLU
dataset (Miller, 2024)included mistranslations such
as "Not wrong, wrong" rendered as "Not wrong,
Not wrong" in Latvian, increasing the English-
Latvian error gap by 2%.
Some culturally specific questions remain chal-
lenging to translate accurately. The small sample
size limits generalizability, and lack formal quality
control measures, such as inter-annotator agree-
ment (IAA) or computational frameworks like
AfriCOMET (Wang et al., 2023), further impacts
the validity of results. Statistical techniques such
as clustered standard error calculations (Miller,
2024)) could enhance analysis reliability.
The black-box nature of closed models intro-
duces uncertainty and undermines fair compar-
isons. LAG-MMLU represents only a fraction of
the world’s many languages (Singh et al., 2024),
hence neglecting many dialects, creoles(Robinson
et al., 2024), code-switching (Etori and Gini,
2024a). Future work should include more lan-
guages and geo-cultural to improve inclusivity.
7
Ethical considerations
The MMLU dataset includes highly technical terms
from fields such as law, science, and ethics (e.g.,
"neurotransmitters" and "Pauli exclusion princi-
ple"), which are difficult to translate into LRLs
like Giriama as shown in Table 1. A lack of es-
tablished vocabulary or the need for highly spe-
cialized translators often leads to inconsistent or
unclear translations. Additionally, the dataset re-
flects Western-centric knowledge and perspectives,
which can misrepresent cultural nuances such as
political ideologies or gender roles when translated.
The linguistic and cultural challenges undermine
language models’ accuracy, consistency, and real-
world applicability in the target culture.
8
Acknowledgements
We appreciate our annotators’ exceptional effort
and dedication to producing high-quality work.

--- Page 10 ---

References
Josh Achiam, Steven Adler, Sandhini Agar-
wal,
Lama Ahmad,
Ilge Akkaya,
Floren-
cia Leoni Aleman, Diogo Almeida, Janko Al-
tenschmidt, Sam Altman, Shyamal Anadkat,
et al. 2023.
Gpt-4 technical report.
arXiv
preprint arXiv:2303.08774.
Ife Adebara, AbdelRahim Elmadany, and Muham-
mad Abdul-Mageed. 2024. Cheetah: Natural
language generation for 517 african languages.
arXiv preprint arXiv:2401.01053.
David Ifeoluwa Adelani, Jade Abbott, Graham
Neubig, Daniel D’souza, Julia Kreutzer, Con-
stantine Lignos, Chester Palen-Michel, Happy
Buzaaba, Shruti Rijhwani, Sebastian Ruder, et al.
2021. Masakhaner: Named entity recognition
for african languages. Transactions of the Asso-
ciation for Computational Linguistics, 9:1116–
1131.
David Ifeoluwa Adelani, Jessica Ojo, Israel Abebe
Azime, Jian Yun Zhuang, Jesujoba O Alabi, Xu-
anli He, Millicent Ochieng, Sara Hooker, An-
diswa Bukula, En-Shiun Annie Lee, et al. 2024.
Irokobench: A new benchmark for african lan-
guages in the age of large language models.
arXiv preprint arXiv:2406.03368.
Sanchit Ahuja,
Divyanshu Aggarwal,
Varun
Gumma, Ishaan Watts, Ashutosh Sathe, Milli-
cent Ochieng, Rishav Hada, Prachi Jain, Max-
amed Axmed, Kalika Bali, et al. 2023. Mega-
verse: Benchmarking large language models
across languages, modalities, models and tasks.
arXiv preprint arXiv:2311.07463.
AI
Safety
Institute.
2024.
Inspect
-
ai
safety
institute.
https://inspect.
ai-safety-institute.org.uk/.
Accessed: 2024-10-15.
Jesujoba O Alabi, David Ifeoluwa Adelani, Marius
Mosbach, and Dietrich Klakow. 2022. Adapt-
ing pre-trained language models to african lan-
guages via multilingual adaptive fine-tuning.
arXiv preprint arXiv:2204.06487.
Anthropic. 2024.
Claude-3.5 sonnet.
An-
thropic AI Systems.
Retrieved October
22, 2024, from https://www.anthropic.
com/news/claude-3-5-sonnet.
Rupjyoti Baruah, Rajesh Kumar Mundotiya, and
Anil Kumar Singh. 2021. Low resource neural
machine translation: Assamese to/from other
indo-aryan (indic) languages. Transactions on
Asian and Low-Resource Language Information
Processing, 21(1):1–32.
Cheng-Han Chiang and Hung-yi Lee. 2023.
Can large language models be an alterna-
tive to human evaluations?
arXiv preprint
arXiv:2305.01937.
Yu Ying Chiu, Liwei Jiang, Bill Yuchen Lin,
Chan Young Park, Shuyue Stella Li, Sahithya
Ravi, Mehar Bhatia, Maria Antoniak, Yulia
Tsvetkov, Vered Shwartz, et al. 2024. Cultural-
bench: a robust, diverse and challenging bench-
mark on measuring the (lack of) cultural knowl-
edge of llms. arXiv preprint arXiv:2410.02677.
Rochelle Choenni, Sara Rajaee, Christof Monz,
and Ekaterina Shutova. 2024. On the evaluation
practices in multilingual nlp: Can machine trans-
lation offer an alternative to human translations?
arXiv preprint arXiv:2406.14267.
Elizabeth Clark, Tal August, Sofia Serrano, Nikita
Haduong, Suchin Gururangan, and Noah A
Smith. 2021. All that’s’ human’is not gold: Eval-
uating human evaluation of generated text. arXiv
preprint arXiv:2107.00061.
A Conneau. 2019. Unsupervised cross-lingual rep-
resentation learning at scale.
arXiv preprint
arXiv:1911.02116.
Marta R Costa-jussà, James Cross, Onur Çelebi,
Maha Elbayad, Kenneth Heafield, Kevin Heffer-
nan, Elahe Kalbassi, Janice Lam, Daniel Licht,
Jean Maillard, et al. 2022. No language left
behind: Scaling human-centered machine trans-
lation. arXiv preprint arXiv:2207.04672.
Roberts Dar`gis, Guntis Barzdins, Inguna Skadin, a,
and Baiba Saul¯ıte. 2024a.
Evaluating open-
source llms in low-resource languages: Insights
from latvian high school exams. In Proceedings
of the 4th International Conference on Natural
Language Processing for Digital Humanities,
pages 289–293.
Roberts Dar`gis, Arturs Znotins, Ilze Auzin, a, Baiba
Saul¯ıte, Sanita Reinsone, Raivis Dejus, Antra
Klavinska, and Normunds Gruzitis. 2024b. Bal-
sutalka. lv-boosting the common voice corpus

--- Page 11 ---

for low-resource languages. In Proceedings of
the 2024 Joint International Conference on Com-
putational Linguistics, Language Resources and
Evaluation (LREC-COLING 2024), pages 2080–
2085.
Fiifi Dawson, Zainab Mosunmola, Sahil Pocker,
Raj Abhijit Dandekar, Rajat Dandekar, and Sree-
dath Panat. 2024. Evaluating cultural aware-
ness of llms for yoruba, malayalam, and english.
arXiv preprint arXiv:2410.01811.
Jacob Devlin. 2018. Bert: Pre-training of deep
bidirectional transformers for language under-
standing. arXiv preprint arXiv:1810.04805.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav
Pandey, Abhishek Kadian, Ahmad Al-Dahle,
Aiesha Letman, Akhil Mathur, Alan Schelten,
Amy Yang, Angela Fan, and others. 2024a.
The Llama 3 Herd of Models. arXiv preprint
arXiv:2407.21783.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav
Pandey, Abhishek Kadian, Ahmad Al-Dahle,
Aiesha Letman, Akhil Mathur, Alan Schel-
ten, Amy Yang, Angela Fan, et al. 2024b.
The llama 3 herd of models.
arXiv preprint
arXiv:2407.21783.
Naome Etori and Maria Gini. 2024a.
Rideke:
Leveraging low-resource twitter user-generated
content for sentiment and emotion detection on
code-switched rhs dataset. In Proceedings of the
14th Workshop on Computational Approaches to
Subjectivity, Sentiment, & Social Media Analysis,
pages 234–249.
Naome A Etori and Maria Gini. 2024b. Wiscom-
panion: Integrating the socratic method with
chatgpt-based ai for enhanced explainability in
emotional support for older adults. In Interna-
tional Conference on Human-Computer Interac-
tion, pages 179–198. Springer.
Fahim Faisal, Orevaoghene Ahia, Aarohi Sri-
vastava, Kabir Ahuja, David Chiang, Yulia
Tsvetkov, and Antonios Anastasopoulos. 2024.
Dialectbench: A nlp benchmark for dialects, va-
rieties, and closely-related languages.
arXiv
preprint arXiv:2403.11009.
Sebastian Gehrmann, Tosin Adewumi, Karmanya
Aggarwal, Pawan Sasanka Ammanamanchi,
Aremu Anuoluwapo, Antoine Bosselut, Khy-
athi Raghavi Chandu, Miruna Clinciu, Dipan-
jan Das, Kaustubh D Dhole, et al. 2021. The
gem benchmark: Natural language generation,
its evaluation and metrics.
arXiv preprint
arXiv:2102.01672.
Omid Ghahroodi, Marzia Nouri, Mohammad Vali
Sanian, Alireza Sahebi, Doratossadat Dast-
gheib, Ehsaneddin Asgari, Mahdieh Soleymani
Baghshah, and Mohammad Hossein Rohban.
2024. Khayyam challenge (persianmmlu): Is
your llm truly wise to the persian language?
arXiv preprint arXiv:2404.06644.
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao
Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu,
Shirong Ma, Peiyi Wang, Xiao Bi, et al. 2025.
Deepseek-r1: Incentivizing reasoning capabil-
ity in llms via reinforcement learning. arXiv
preprint arXiv:2501.12948.
Michael A Hedderich, Lukas Lange, Heike Adel,
Jannik Strötgen, and Dietrich Klakow. 2020. A
survey on recent approaches for natural language
processing in low-resource scenarios.
arXiv
preprint arXiv:2010.12309.
Dan Hendrycks, Collin Burns, Steven Basart, Andy
Zou, Mantas Mazeika, Dawn Song, and Jacob
Steinhardt. 2020.
Measuring massive multi-
task language understanding.
arXiv preprint
arXiv:2009.03300.
Dan Hendrycks, Collin Burns, Steven Basart, Andy
Zou, Mantas Mazeika, Dawn Song, and Jacob
Steinhardt. 2021. Measuring massive multitask
language understanding.
Junjie Hu, Sebastian Ruder, Aditya Siddhant, Gra-
ham Neubig, Orhan Firat, and Melvin Johnson.
2020. Xtreme: A massively multilingual multi-
task benchmark for evaluating cross-lingual gen-
eralisation. In International Conference on Ma-
chine Learning, pages 4411–4421. PMLR.
Aaron Hurst, Adam Lerer, Adam P Goucher, Adam
Perelman, Aditya Ramesh, Aidan Clark, AJ Os-
trow, Akila Welihinda, Alan Hayes, Alec Rad-
ford, et al. 2024. Gpt-4o system card. arXiv
preprint arXiv:2410.21276.
David Ifeoluwa Adelani, Jessica Ojo, Israel
Abebe Azime, Jian Yun Zhuang, Jesujoba O Al-
abi, Xuanli He, Millicent Ochieng, Sara Hooker,

--- Page 12 ---

Andiswa Bukula, En-Shiun Annie Lee, et al.
2024. Irokobench: A new benchmark for african
languages in the age of large language models.
arXiv e-prints, pages arXiv–2406.
Aaron Jaech, Adam Kalai, Adam Lerer, Adam
Richardson, Ahmed El-Kishky, Aiden Low, Alec
Helyar, Aleksander Madry, Alex Beutel, Alex
Carney, et al. 2024.
Openai o1 system card.
arXiv preprint arXiv:2412.16720.
Albert Q Jiang, Alexandre Sablayrolles, Arthur
Mensch, Chris Bamford, Devendra Singh Chap-
lot, Diego de las Casas, Florian Bressand,
Gianna Lengyel, Guillaume Lample, Lucile
Saulnier, et al. 2023. Mistral 7b. arXiv preprint
arXiv:2310.06825.
Kathryn R Kirby, Russell D Gray, Simon J Green-
hill, Fiona M Jordan, Stephanie Gomes-Ng,
Hans-Jörg Bibiko, Damián E Blasi, Carlos A
Botero, Claire Bowern, Carol R Ember, et al.
2016. D-place: A global database of cultural,
linguistic and environmental diversity. PloS one,
11(7):e0158391.
Tom Kocmi, Christian Federmann, Roman Grund-
kiewicz, Marcin Junczys-Dowmunt, Hitokazu
Matsushita, and Arul Menezes. 2021. To ship or
not to ship: An extensive evaluation of automatic
metrics for machine translation. arXiv preprint
arXiv:2107.10821.
Fajri Koto, Nurul Aisyah, Haonan Li, and Timo-
thy Baldwin. 2023. Large language models only
pass primary school exams in indonesia: A com-
prehensive test on indommlu. arXiv preprint
arXiv:2310.04928.
Fajri Koto, Haonan Li, Sara Shatnawi, Jad Dough-
man, Abdelrahman Boda Sadallah, Aisha Al-
raeesi, Khalid Almubarak, Zaid Alyafeai, Neha
Sengupta, Shady Shehata, et al. 2024.
Ara-
bicmmlu:
Assessing massive multitask lan-
guage understanding in arabic. arXiv preprint
arXiv:2402.12840.
Pawan Lahoti, Namita Mittal, and Girdhari Singh.
2022. A survey on nlp resources, tools, and tech-
niques for marathi language processing. ACM
Transactions on Asian and Low-Resource Lan-
guage Information Processing, 22(2):1–34.
Teven Le Scao, Angela Fan, Christopher Akiki, El-
lie Pavlick, Suzana Ili´c, Daniel Hesslow, Roman
Castagné, Alexandra Sasha Luccioni, François
Yvon, Matthias Gallé, et al. 2023. Bloom: A
176b-parameter open-access multilingual lan-
guage model.
Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang,
Hai Zhao, Yeyun Gong, Nan Duan, and Tim-
othy Baldwin. 2023. Cmmlu: Measuring mas-
sive multitask language understanding in chinese.
arXiv preprint arXiv:2306.09212.
Zihao Li, Yucheng Shi, Zirui Liu, Fan Yang,
Ninghao Liu, and Mengnan Du. 2024. Quan-
tifying multilingual performance of large lan-
guage models across languages. arXiv preprint
arXiv:2404.11553.
Percy Liang, Rishi Bommasani, Tony Lee, Dim-
itris Tsipras, Dilara Soylu, Michihiro Yasunaga,
Yian Zhang, Deepak Narayanan, Yuhuai Wu,
Ananya Kumar, et al. 2022.
Holistic eval-
uation of language models.
arXiv preprint
arXiv:2211.09110.
Yaobo Liang, Nan Duan, Yeyun Gong, Ning Wu,
Fenfei Guo, Weizhen Qi, Ming Gong, Linjun
Shou, Daxin Jiang, Guihong Cao, et al. 2020.
Xglue: A new benchmark dataset for cross-
lingual pre-training, understanding and gener-
ation. arXiv preprint arXiv:2004.01401.
Chin-Yew Lin. 2004. ROUGE: A package for auto-
matic evaluation of summaries. In Text Summa-
rization Branches Out, pages 74–81, Barcelona,
Spain. Association for Computational Linguis-
tics.
Chin-Yew Lin and Franz Josef Och. 2004. OR-
ANGE: a method for evaluating automatic eval-
uation metrics for machine translation. In COL-
ING 2004: Proceedings of the 20th International
Conference on Computational Linguistics, pages
501–507, Geneva, Switzerland. COLING.
Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang,
Bochao Wu, Chengda Lu, Chenggang Zhao,
Chengqi Deng, Chenyu Zhang, Chong Ruan,
et al. 2024. Deepseek-v3 technical report. arXiv
preprint arXiv:2412.19437.
Chen Cecilia Liu, Fajri Koto, Timothy Baldwin,
and Iryna Gurevych. 2023. Are multilingual
llms culturally-diverse reasoners? an investi-
gation into multicultural proverbs and sayings.
arXiv preprint arXiv:2309.08591.

--- Page 13 ---

Zihan Liu, Genta I Winata, Samuel Cahyawijaya,
Andrea Madotto, Zhaojiang Lin, and Pascale
Fung. 2021. On the importance of word order in-
formation in cross-lingual sequence labeling. In
Proceedings of the AAAI Conference on Artificial
Intelligence, volume 35, pages 13461–13469.
Alexandre Magueresse, Vincent Carles, and Evan
Heetderks. 2020. Low-resource languages: A
review of past work and future challenges. arXiv
preprint arXiv:2006.07264.
Evan Miller. 2024. Adding error bars to evals: A
statistical approach to language model evalua-
tions. arXiv preprint arXiv:2411.00640.
Marc Miquel-Ribé and David Laniado. 2019.
Wikipedia cultural diversity dataset: A complete
cartography for 300 language editions. In Pro-
ceedings of the International AAAI Conference
on Web and Social Media, volume 13, pages
620–629.
Steven Moran, Christian Bentz, Ximena Gutierrez-
Vasques, Olga Pelloni, and Tanja Samardzic.
2022. Teddi sample: Text data diversity sam-
ple for language comparison and multilingual
nlp. In Proceedings of the Thirteenth Language
Resources and Evaluation Conference, pages
1150–1158.
Niklas Muennighoff, Thomas Wang, Lintang
Sutawika, Adam Roberts, Stella Biderman,
Teven Le Scao, M Saiful Bari, Sheng Shen,
Zheng-Xin Yong, Hailey Schoelkopf, et al. 2022.
Crosslingual generalization through multitask
finetuning. arXiv preprint arXiv:2211.01786.
MyMemory.
2024.
Mymemory
trans-
lation
memory
-
api
documentation.
https://mymemory.translated.
net/doc/spec.php.
Accessed: 2024-10-
15.
OpenAI. 2024. O1 system card. Technical report,
OpenAI. Accessed on October 16, 2024.
Peteris Paikens, Lauma Pretkalnin, a, and Laura Ri-
tuma. 2024. A computational model of latvian
morphology. In Proceedings of the 2024 Joint
International Conference on Computational Lin-
guistics, Language Resources and Evaluation
(LREC-COLING 2024), pages 221–232.
Denis Paperno,
Germán Kruszewski,
Ange-
liki Lazaridou, Quan Ngoc Pham, Raffaella
Bernardi,
Sandro Pezzelle,
Marco Baroni,
Gemma Boleda, and Raquel Fernández. 2016.
The lambada dataset: Word prediction requir-
ing a broad discourse context. arXiv preprint
arXiv:1606.06031.
Kishore Papineni, Salim Roukos, Todd Ward, and
Wei jing Zhu. 2002. Bleu: a method for auto-
matic evaluation of machine translation. pages
311–318.
Surangika Ranathunga and Nisansa De Silva. 2022.
Some languages are more equal than others:
Probing deeper into the linguistic disparity in
the nlp world. arXiv preprint arXiv:2210.08523.
Nathaniel R Robinson, Raj Dabre, Ammon Shurtz,
Rasul Dent, Onenamiyi Onesi, Claire Bizon
Monroc, Loïc Grobol, Hasan Muhammad, Ashi
Garg, Naome A Etori, et al. 2024. Krey\ol-mt:
Building mt for latin american, caribbean and
colonial african creole languages. arXiv preprint
arXiv:2405.05376.
David Romero,
Chenyang Lyu,
Haryo Ak-
barianto Wibowo, Teresa Lynn, Injy Hamed,
Aditya Nanda Kishore, Aishik Mandal, Alina
Dragonetti, Artem Abzaliev, Atnafu Lambebo
Tonja, et al. 2024. Cvqa: Culturally-diverse mul-
tilingual visual question answering benchmark.
arXiv preprint arXiv:2406.05967.
Sebastian Ruder, Noah Constant, Jan Botha, Aditya
Siddhant, Orhan Firat, Jinlan Fu, Pengfei Liu,
Junjie Hu, Dan Garrette, Graham Neubig, et al.
2021. Xtreme-r: Towards more challenging and
nuanced multilingual evaluation. arXiv preprint
arXiv:2104.07412.
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bha-
gavatula, and Yejin Choi. 2021. Winogrande:
An adversarial winograd schema challenge at
scale. Communications of the ACM, 64(9):99–
106.
Shivalika Singh, Angelika Romanou, Clémen-
tine Fourrier, David I Adelani, Jian Gang
Ngui, Daniel Vila-Suero, Peerat Limkonchoti-
wat, Kelly Marchisio, Wei Qi Leong, Yosephine
Susanto, et al. 2024.
Global mmlu: Under-
standing and addressing cultural and linguistic
biases in multilingual evaluation. arXiv preprint
arXiv:2412.03304.

--- Page 14 ---

Hermann Smith-Sivertsen. 2004.
Latvia.
The
handbook of political change in eastern Europe,
2:95–133.
Guijin Son, Hanwool Lee, Sungdong Kim, Seun-
gone Kim, Niklas Muennighoff, Taekyoon Choi,
Cheonbok Park, Kang Min Yoo, and Stella Bi-
derman. 2024. Kmmlu: Measuring massive mul-
titask language understanding in korean. arXiv
preprint arXiv:2402.11548.
Gemini Team, Petko Georgiev, Ving Ian Lei, Ryan
Burnell, Libin Bai, Anmol Gulati, Garrett Tanzer,
Damien Vincent, Zhufeng Pan, Shibo Wang,
et al. 2024. Gemini 1.5: Unlocking multimodal
understanding across millions of tokens of con-
text. arXiv preprint arXiv:2403.05530.
Klaudia Thellmann, Bernhard Stadler, Michael
Fromm, Jasper Schulze Buschhoff, Alex Jude,
Fabio Barth, Johannes Leveling, Nicolas Flores-
Herr, Joachim Köhler, René Jäkel, et al.
2024.
Towards multilingual llm evalua-
tion for european languages.
arXiv preprint
arXiv:2410.08928.
Jörg Tiedemann. 2020.
The tatoeba transla-
tion challenge–realistic data sets for low re-
source and multilingual mt.
arXiv preprint
arXiv:2010.06354.
Hugo Touvron, Thibaut Lavril, Gautier Izacard,
Xavier Martinet, Marie-Anne Lachaux, Timo-
thée Lacroix, Baptiste Rozière, Naman Goyal,
Eric Hambro, Faisal Azhar, et al. 2023. Llama:
Open and efficient foundation language models.
arXiv preprint arXiv:2302.13971.
Alex Wang. 2018. Glue: A multi-task benchmark
and analysis platform for natural language un-
derstanding. arXiv preprint arXiv:1804.07461.
Alex Wang, Yada Pruksachatkun, Nikita Nangia,
Amanpreet Singh, Julian Michael, Felix Hill,
Omer Levy, and Samuel Bowman. 2019. Super-
glue: A stickier benchmark for general-purpose
language understanding systems. Advances in
neural information processing systems, 32.
Jiayi Wang, David Ifeoluwa Adelani, Sweta
Agrawal, Marek Masiak, Ricardo Rei, Elefthe-
ria Briakou, Marine Carpuat, Xuanli He, Sofia
Bourhim, Andiswa Bukula, et al. 2023. Afrimte
and africomet: Enhancing comet to embrace
under-resourced african languages.
Genta Winata, Shijie Wu, Mayank Kulkarni,
Thamar Solorio, and Daniel Preo¸tiuc-Pietro.
2022. Cross-lingual few-shot learning on un-
seen languages. In Proceedings of the 2nd Con-
ference of the Asia-Pacific Chapter of the Asso-
ciation for Computational Linguistics and the
12th International Joint Conference on Natural
Language Processing (Volume 1: Long Papers),
pages 777–791.
Genta Indra Winata, Samuel Cahyawijaya, Zi-
han Liu, Zhaojiang Lin, Andrea Madotto, and
Pascale Fung. 2021. Are multilingual models
effective in code-switching?
arXiv preprint
arXiv:2103.13309.
Genta
Indra
Winata,
Frederikus
Hudi,
Patrick Amadeus Irawan, David Anugraha,
Rifki
Afina
Putri,
Yutong
Wang,
Adam
Nohejl, Ubaidillah Ariq Prathama, Nedjma
Ousidhoum, Afifa Amriani, et al. 2024. World-
cuisines:
A massive-scale benchmark for
multilingual and multicultural visual question
answering on global cuisines. arXiv preprint
arXiv:2410.12705.
L Xue. 2020. mt5: A massively multilingual pre-
trained text-to-text transformer. arXiv preprint
arXiv:2010.11934.
Arda Yüksel, Abdullatif Köksal, Lütfi Kerem
¸Senel, Anna Korhonen, and Hinrich Schütze.
2024. Turkishmmlu: Measuring massive mul-
titask language understanding in turkish. arXiv
preprint arXiv:2407.12402.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. Hellaswag: Can
a machine really finish your sentence? arXiv
preprint arXiv:1905.07830.
Qihuang Zhong, Kang Wang, Ziyang Xu, Juhua
Liu, Liang Ding, Bo Du, and Dacheng Tao. 2024.
Achieving> 97% on gsm8k: Deeply understand-
ing the problems makes llms perfect reasoners.
arXiv e-prints, pages arXiv–2404.

--- Page 15 ---

A
Few-Shots Templates
Figure 7: MMLU Multi-Shot Prompt and Question Template. The templates define the format for
multiple-choice question prompts and individual test questions, ensuring consistent structure across
different subject areas.

--- Page 16 ---

B
Datasets Statistics
Humanities
STEM
Subject
Freq
Subject
Freq
moral_disputes
12
abstract_algebra
3
professional_law
57
anatomy
1
formal_logic
6
astronomy
4
high_school_european_history
3
college_chemistry
2
high_school_us_history
9
college_computer_science
2
high_school_world_history
12
college_mathematics
5
international_law
2
college_physics
4
jurisprudence
4
computer_security
4
logical_fallacies
9
conceptual_physics
6
moral_scenarios
31
electrical_engineering
7
philosophy
9
elementary_mathematics
17
prehistory
11
high_school_biology
7
world_religions
5
high_school_chemistry
10
Total
170
high_school_computer_science
3
high_school_mathematics
16
high_school_physics
6
high_school_statistics
10
machine_learning
5
Total
112
Social Sciences
Other
Subject
Freq
Subject
Freq
econometrics
1
business_ethics
4
high_school_geography
9
clinical_knowledge
15
high_school_government_and_politics
4
college_medicine
3
high_school_macroeconomics
8
global_facts
5
high_school_microeconomics
5
human_aging
8
high_school_psychology
21
management
4
human_sexuality
7
marketing
19
professional_psychology
26
miscellaneous
30
public_relations
2
nutrition
7
security_studies
4
professional_accounting
9
sociology
10
professional_medicine
8
us_foreign_policy
2
virology
7
Total
99
Total
119
Table 4: Distribution of Subject Tasks Across Categories in LAG-MMLU. In this table we present the
frequency of subject-specific tasks categorized into Humanities, STEM, Social Sciences, and Other. This
categorization was based on the original MMLU dataset and paper (Hendrycks et al., 2021)

--- Page 17 ---

C
Performance with Standard Errors
Model
COT
English (%)
Latvian (%)
Giriama (%)
0-shot
5-shot
0-shot
5-shot
0-shot
5-shot
OpenAI o1
✗
92.8 ± 1.2
–
88.8 ± 1.4
–
70.8 ± 2.0
–
GPT-4o
✗
83.6 ± 1.7
–
75.6 ± 1.9
78.0 ± 1.9
53.2 ± 2.2
–
✓
–
84.5 ± 1.6
79.5 ± 1.8
–
–
62.3 ± 2.2
Claude 3.5
✗
88.8 ± 1.4
–
78.2 ± 1.8
–
54.8 ± 2.2
–
✓
–
87.1 ± 1.5
–
83.0 ± 1.7
–
60.9 ± 2.2
Gemini 1.5 Pro
✗
84.0 ± 1.6
–
70.3 ± 2.0
–
51.4 ± 2.2
–
✓
–
85.4 ± 1.6
–
79.9 ± 1.8
–
61.8 ± 2.2
DeepSeek-V3
✗
87.6 ± 1.5
–
70.7 ± 2.0
–
49.8 ± 2.2
–
✓
–
87.9 ± 1.5
–
76.1 ± 1.9
–
52.3 ± 2.2
Llama-70B IT
✗
81.0 ± 1.8
–
57.3 ± 2.2
–
41.0 ± 2.2
–
Mistral-large
✗
80.0 ± 1.8
–
49.3 ± 2.2
–
35.6 ± 2.1
–
DeepSeek-R1
✗
81.4 ± 1.7
–
70.2 ± 2.0
–
52.2 ± 2.2
–
Table 5: Performance of Models on LAG-MMLU. Accuracy (%) with standard error (SE) across three
languages (English, Latvian, and Giriama) under 0-shot and 5-shot settings. Results are presented for
models with and without CoT prompting. The LAG-MMLU benchmark reveals a clear performance gap
between high-resource and low-resource languages, with OpenAI o1 leading in zero-shot settings across
English (92.8%), Latvian (88.8%), and Giriama (70.8%). COT significantly boosts few-shot performance,
particularly for GPT-4o, Claude 3.5, and Gemini 1.5 Pro, improving accuracy in Latvian and Giriama.
However, Giriama remains challenging for all models, with closed-source models outperforming open
ones—though DeepSeek-V3 leads among open models.

```
