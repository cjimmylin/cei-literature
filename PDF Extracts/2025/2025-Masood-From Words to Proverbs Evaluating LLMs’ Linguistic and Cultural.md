---
title: "2025-Masood-From Words to Proverbs Evaluating LLMs’ Linguistic and Cultural - PDF Extract"
source_pdf: "2025-Masood-From Words to Proverbs Evaluating LLMs’ Linguistic and Cultural.pdf"
pages: 32
extracted_at: "2026-02-13T13:57:13.380490"
---

# PDF Extract: 2025-Masood-From Words to Proverbs Evaluating LLMs’ Linguistic and Cultural

**Source PDF:** 2025-Masood-From Words to Proverbs Evaluating LLMs’ Linguistic and Cultural.pdf
**Total Pages:** 32

---

## Content

```
--- Page 1 ---

From Words to Proverbs: Evaluating LLMs’
Linguistic and Cultural Competence in Saudi
Dialects with Absher
Renad Al-Monef1, 2, Hassan Alhuzali3, Nora Alturayeif4,
Ashwag Alasmari1, 2*
1*Department of Computer Science, King Khalid University, Abha, Saudi
Arabia.
2Center for Artificial Intelligence, King Khalid University, Abha, Saudi
Arabia.
3Department of Computer Science and Artificial Intelligence, Umm
Al-Qura University, Makkah, Saudi Arabia.
4Imam Abdulrahman Bin Faisal University, Dammam, Saudi Arabia.
*Corresponding author(s). E-mail(s): aasmry@kku.edu.sa;
Contributing authors: renadsalem01@gmail.com; hrhuzali@uqu.edu.sa;
nsalturayeif@iau.edu.sa;
Abstract
As large language models (LLMs) become increasingly central to Arabic NLP
applications, their effectiveness in linguistically diverse settings, particularly
regions with rich dialectal variation such as Saudi Arabia, remains underex-
plored. Existing evaluation paradigms tend to prioritize high-resource languages
or Modern Standard Arabic (MSA), overlooking regional linguistic and cul-
tural specificities. This leads to performance limitations and cultural biases in
real-world deployments. To address this gap, we introduce Absher, the first com-
prehensive and fine-grained benchmark designed to assess the understanding of
LLMs regarding Saudi dialects and their embedded cultural nuances. Absher
consists of over 18,000 multiple choice questions derived from a curated dataset
of dialectal words, phrases, and proverbs sourced from five major Saudi regions.
The benchmark spans six task categories: Meaning, True/False, Fill-in-the-Blank,
Contextual Usage, Cultural Interpretation, and Location Recognition, enabling
multifaceted evaluation across both linguistic and cultural dimensions.We per-
form zero-shot evaluations on six state-of-the-art open LLMs: ALLaM, LLaMA,
Jais, Mistral, Qwen, and AceGPT. Our results reveal substantial performance
1
arXiv:2507.10216v2  [cs.CL]  21 Dec 2025

--- Page 2 ---

variability across dialects and question types. Qwen achieved the highest overall
accuracy, excelling in word-level questions (63%), while ALLaM outperformed
others in the interpretation of proverbs (48% accuracy). All models struggled
with content from underrepresented dialects, particularly Southern and Eastern
variants, and with context-free True/False questions, highlighting weaknesses in
dialect grounding and binary reasoning. These findings demonstrate the need
for dialect-aware training and culturally aligned evaluation. We position Absher
as a critical step towards more equitable and effective LLM development for
real-world Arabic applications.
Keywords: Large Language Models, Natural Language Processing , Cultural aware
LLMs, Dialects Understanding
1 Introduction
Recent breakthroughs in the area of language processing have shown that contempo-
rary computational models can perform a variety of tasks, including text production,
question answering, and machine translation [1, 2]. These powerful computational
models are becoming indispensable tools across various sectors, from education and
healthcare to public services and entertainment. However, a critical challenge remains:
the vast majority of these models, along with their foundational training data and eval-
uation benchmarks, are developed with a prevailing focus on high-resource languages
like English or, within the Arabic-speaking world, Modern Standard Arabic (MSA).
This limits their performance and applicability in domains characterized by significant
linguistic and cultural diversity, particularly those with rich regional dialects [3, 4].
Language is inherently cultural; its full comprehension demands reasoning beyond
literal meaning to grasp social implications and regional specificities.
Saudi Arabia exemplifies this challenge with its rich landscape of regional dialects.
These dialects are not merely linguistic variants, but embody unique cultural prac-
tices, idiomatic expressions, and proverbs critical to authentic communication [5].
Despite this profound linguistic and cultural diversity, existing Arabic natural lan-
guage processing (NLP) benchmarks and large language models (LLMs) training data
largely overlook these fine-grained Saudi dialectal and cultural nuances [3, 6]. There-
fore, models struggle to interpret local identity, leading to significant performance
gaps and potentially biases against underrepresented languages.
To address this critical gap and rigorously assess LLMs’ cultural and linguistic
competence in this domain, we introduce Absher, a novel, comprehensive, and first-of-
its-kind benchmark. Absher offers an evaluation framework built on a curated dataset
of authentic Saudi dialectal content, sourced from diverse regions across the King-
dom. It comprises 18, 564 multiple-choice questions, systematically generated to cover
six distinct categories: Meaning, True/False, Fill-in-the-Blank, Contextual Usage,
Cultural Interpretation, and Location Recognition. This multi-faceted design facili-
tates a deep, granular assessment of LLMs’ capabilities that moves beyond superficial
linguistic understanding toward genuine cultural competence.
2

--- Page 3 ---

Beyond technical accuracy, the ability of LLMs to process and respond to Saudi
dialects carries broader sociolinguistic significance. These dialects are not only linguis-
tic systems but also carriers of regional identity, social norms, and cultural heritage.
Ensuring their equitable representation in AI systems is crucial for linguistic inclusion
and mitigating the marginalization of underrepresented communities. Such efforts are
vital for the development of equitable AI systems and for informing culturally aware
language technologies and public policy.
W
o
r
d
s
P
r
o
v
e
r
b
s
p
h
r
a
s
e
s
ء
بـسر
اﻟﺴﻌﻮدﻳﺔ؟ اﻟﺜﻘﺎﻓﺔ ﻓﻲ "داﻓﻮر" ﻟﻘﺐ دﻻﻟﺔ ﻫﻲ ﻣﺎ :اﻟﺴﺆال
:اﻻﺧﺘﻴﺎرات
اﻟﺮﻳﺎﺿﺔ ﻓﻲ اﻟﻄﻤﻮﺣﻴﻦ اﻷﺷﺨﺎص ﻟﻮﺻﻒ ﺴﺘﺨﺪمُﻳ (أ
اﻟﺪراﺳﻲ اﻟﻔﺸﻞ ﻋﻠﻰ ﻳﺪل (ب
واﻟﻤﺜﺎﺑﺮة واﻻﺟﺘﻬﺎد اﻟﺬﻛﺎء ﻋﻠﻰ ﻋﻼﻣﺔ ﻌﺘﺒﺮُﻳ (ج
اﻻﻧﻌﺰاﻟﻴﺔ إﻟﻰ ﺸﻴﺮُﻳ (د
Cultural Interpretation
."ﺑﻚ؟ ﻣﺎذا" ﺗﻌﻨﻲ 'ﻋﻼﻣﻚ' ﻛﻠﻤﺔ :ااﻟﺴﺆال
:اﻟﺨﻴﺎرات
ﺻﺢ (أ
ﺧﻄﺄ (ب
True\False
"ﻫﺒﺸﺔ" ﻛﻠﻤﺔ ﻓﻴﻬﺎ ﺗﺴﺘﺨﺪم اﻟﺘﺎﻟﻴﺔ اﻟﺠﻤﻞ ﻣﻦ أي :اﻟﺴﺆال
ﺻﺤﻴﺢ؟ ﺑﺸﻜﻞ
:اﻟﺨﻴﺎرات
.اﻟﺘﻤﺮ ﻣﻦ ﻫﺒﺸﺔ أﻋﻄﻨﻲ (أ
.اﻟﺠﻮ ﻓﻲ ﻃﻴﺎرة اﻟﻬﺒﺸﺔ (ب
.ﺳﻴﺎرة ﻫﺒﺸﺔ اﺷﺘﺮى ﻫﻮ (ج
.اﻟﺸﺎي ﻣﻊ اﻟﻬﺒﺸﺔ أﻛﻞ أﺣﺐ (د
Contextua Usage
اﻟﻤﺜﻞ ﻫﺬا ﻳﺴﺘﺨﺪم ﺳﻌﻮدﻳﺔ ﻣﻨﻄﻘﺔ أي ﻓﻲ :اﻟﺴﺆال
ﺷﺎﺋﻊ؟ ﺑﺸﻜﻞ "ﻴﻪِراﻋ ﺎﻧﺎَﻏ ﻮلُﻤَﺣ ﻰَﻧْأد"
:اﻟﺨﻴﺎرات
ﻧﺠﺪ (أ
اﻟﺤﺠﺎز (ب
ﻋﺴﻴﺮ (ج
اﻟﺸﺮﻗﻴﺔ اﻟﻤﻨﻄﻘﺔ (د
Location Recognition
واﺗﻜﺎ أﻛﻞ ﻣﺎ ﺑﻌﺪ' اﻟﻤﻨﺎﺳﺒﺔ ﺑﺎﻟﻜﻠﻤﺔ اﻟﻤﺜﻞ أﻛﻤﻞ :اﻟﺴﺆال
. '.___________ رﻳﺤﺘﻪ ﻗﺎل
:اﻟﺨﻴﺎرات
ﻣﺴﺘﻜﺎ (أ
ﻃﻴﺒﻪ (ب
ﻟﺬﻳﺬة (ج
ﺑﺎرده (د
Fill in Blank
؟'ﻧﻮﺣﻚ وش' ﻋﺒﺎرة اﺳﺘﺨﺪام ﻳﻤﻜﻦ ﻣﺘﻰ :اﻟﺴﺆال
:اﻟﺨﻴﺎرات
اﻟﻄﻘﺲ ﺣﺎﻟﺔ ﻋﻦ ﺗﺴﺄل ﻋﻨﺪﻣﺎ (أ
ﺎًﻣﺘﻀﺎﻳﻘ ﺎًﺷﺨﺼ ﺗﺮى ﻋﻨﺪﻣﺎ (ب
اﻟﻄﻌﺎم ﻋﻦ ﺗﺘﺤﺪث ﻋﻨﺪﻣﺎ (ج
اﻟﻮﻗﺖ ﻋﻦ ﺗﺴﺄل أن ﺗﺮﻳﺪ ﻋﻨﺪﻣﺎ (د
Contextual Usage
واﻟﻤﻘﺼﻮد ،"دروﺑﻚ أورﻳﻚ" :ﻟﻪ ﻗﺎل ،اﻟﻨﻘﺎش أﺛﻨﺎء :ااﻟﺴﺆال
._______ :ﻫﻮ اﻟﻌﺒﺎرة ﺑﻬﺬه
:اﻟﺨﻴﺎرات
ﻫﺪﻳﺔ أﻋﻄﻴﻚ (أ
(واﻟﻘﻮة ﺑﺸﺪة) ﺳﺄرﻳﻚ (ب
ﺎًﻣﻌﺮوﻓ ﻣﻨﻚ أﻃﻠﺐ (ج
واﻟﻜﺘﺎﺑﺔ اﻟﻘﺮاءة ﻤﻚّأﻋﻠ (د
Fill in Blank
ﻛﺒﺮ ﻋﻠﻰ اﻷﻋﻤﻰ ﻳﺤﺴﺪون“ اﻟﻤﺜﻞ دﻻﻟﺔ ﻫﻲ ﻣﺎ :اﻟﺴﺆال
اﻟﺴﻌﻮدﻳﺔ؟ اﻟﺜﻘﺎﻓﺔ ﻓﻲ ”ﻋﻴﻮﻧﻪ
:اﻻﺧﺘﻴﺎرات
ﺑﺴﻴﻄﺔ أﻣﻮر ﻣﻦ اﻟﺸﻜﻮى ﻜﺜﺮُﻳ ﻣﻦ ﻟﻮﺻﻒ ﺴﺘﺨﺪمُﻳ (أ
واﺿﺢ ﺳﺒﺐ دون اﻵﺧﺮﻳﻦ ﻳﻐﺒﻂ ﻣﻦ إﻟﻰ ﺸﻴﺮُﻳ (ب
ﻣﻨﻪ ﻟﻪ ﻓﺎﺋﺪة ﻻ ﺷﻲء ﻋﻠﻰ ﺎًﺷﺨﺼ ﻳﺤﺴﺪ ﻦَﻣ ﻓﻲ ﻀﺮبُﻳ (ج
اﻟﻤﺎل ﻓﻲ اﻟﺰاﺋﺪ اﻟﻄﻤﻊ ﻋﻠﻰ ﻟﻠﺪﻻﻟﺔ ﺴﺘﺨﺪمُﻳ (د
Cultural Interpretation
 ؟ اﻟﺸﻤﺎﻟﻴﺔ اﻟﻠﻬﺠﺔ ﻓﻲ "وﻏﺪان" ﻛﻠﻤﺔ ﻣﻌﻨﻰ ﻣﺎ :اﻟﺴﺆال
 :اﻟﺨﻴﺎرات
 اﻟﺴﻦ ﻛﺒﺎر (أ
 أﻃﻔﺎل (ب
 ﺑﺎﻟﻐﻮن (ج
 ﻋﺎﺋﻼت (د
Meaning
؟'ادﻳﻠﻮ' ﻛﻠﻤﺔ ﻣﻌﻨﻰ ﻣﺎ :اﻟﺴﺆال
:اﻟﺨﻴﺎرات
اﻋﻄﻴﻪ (أ
ﺧﺬه (ب
اﺗﺮﻛﻪ (ج
ﺟﺮﺣﻪ (د
Meaning
"ﻗﺮوﻧﻬﺎ ﻋﻠﻰ اﻟﺒﻘﺮة ﺣﺠﺖ إذا" اﻟﻤﺜﻞ ﻳﺸﻴﺮ :اﻟﺴﺆال
.ﻟﻠﺘﺤﻘﻴﻖ ﻗﺎﺑﻞ ﻏﻴﺮ أو ﻣﺴﺘﺤﻴﻞ ﺷﻲء إﻟﻰ
:اﻟﺨﻴﺎرات
ﺻﺢ (أ
ﺧﻄﺄ (ب
True\False
 ؟"ﺟﻐﻤﻪ ﻫﺒﻠﻲ" ﻋﺒﺎرة ﻣﻌﻨﻰ ﻣﺎ :اﻟﺴﺆال
 :اﻟﺨﻴﺎرات
 ﻗﻠﻴﻼ ﻷﺷﺮب أﻋﻄﻨﻲ (أ
 اﻵن اﻟﻄﻌﺎم أﻋﻄﻨﻲ (ب
 اﻟﺴﻮق إﻟﻰ اذﻫﺐ (ج
 ﻧﻮم إﻟﻰ أﺣﺘﺎج (د
Meaning
Center
Western
Southern
Northern 
Eastern
General 
Fig. 1: Overview of Absher, covering all regions of Saudi Arabia (five specific
regions and a general category) and presents representative examples from its three
types of content: words, phrases, and proverbs. The benchmark also spans all six
question types: Meaning, True/False, Fill-in-the-Blank, Contextual Usage, Cultural
Interpretation, and Location Recognition.
In this work, our objective is to provide answers to key research questions concern-
ing LLMs’ capabilities in interpreting Saudi dialects, the specific challenges they face,
and a comparative analysis of their performance. Our goal is twofold: (1) to develop
a novel, fine-grained benchmark that systematically evaluates LLMs across Saudi
3

--- Page 4 ---

dialects and linguistic units; and (2) to conduct a comprehensive evaluation of state-
of-the-art LLMs, analyzing their performance, weaknesses, and areas for improvement.
Our key contributions are as follows:
• Benchmark Development: We introduce Absher, the first large-scale benchmark
tailored to Saudi dialects, featuring over 18,000 multiple-choice questions. These
questions span six task categories and are grounded in authentic dialectal words,
phrases, and proverbs from five major Saudi regions, addressing a critical gap in
Arabic NLP evaluation. Figure
1 illustrates the composition of Absher across
different regions and categories.
• Methodological Framework: We propose a scalable pipeline that combines
prompt engineering with automated question generation using LLMs, followed by
a rigorous multi-stage human validation process. This ensures high linguistic and
cultural fidelity, making Absher a reliable tool for dialectal evaluation.
• Model Evaluation and Analysis: We conduct a comprehensive evaluation of
multilingual and Arabic-specific LLMs on the Absher benchmark. Our analysis
reveals significant performance variability across dialects, task categories, and lin-
guistic units. We also investigate the impact of model size, language orientation, and
architecture, offering insights into the limitations and strengths of current LLMs in
dialect-sensitive settings.
This paper is structured as follows: Section 2 reviews the existing literature on Ara-
bic dialects in LLMs. Section 3 details the methodology for constructing the Absher
benchmark, including data collection, pre-processing, prompt design, question gener-
ation, and human evaluation. Section 4 presents the experimental setup and results of
our LLM evaluations. Section 5 provides a detailed analysis of our findings, including
comparative performance across models, content types, and question types. Finally,
Section 6 discusses the broader implications of our results and outlines promising
directions for future research.
2 Related Work
2.1 Arabic Dialects in LLMs
Recent efforts in Arabic NLP have increasingly emphasized dialectal and cultural
aspects in evaluating LLMs. Several benchmarks have emerged to measure model per-
formance in these dimensions. For example, AraDiCE [3] assessed LLMs on dialectal
and cultural understanding across Levantine, Egyptian, and Gulf Arabic, highlighting
limitations in generation and reasoning. Calibration-Arabic-PLMs [7] examined model
confidence in dialect identification, revealing misalignment between confidence and
accuracy. Health-LLM-Arabic [8] introduced a Cultural Sensitivity Score to evaluate
model responses to health-related claims in Saudi, Egyptian, and Moroccan dialects.
In addition, to these evaluation efforts, several datasets and models have been
designed to enhance dialect awareness. Dallah [9] developed a multimodal assistant
fine-tuned on six dialects, while AraReasoner [10] proposed a benchmark suite for
evaluating Arabic reasoning capabilities. Jawaher [11] focused on figurative language
through a collection of Arabic proverbs, and CARE [12] evaluated cultural alignment
4

--- Page 5 ---

via human preferences in Arabic and Chinese contexts. Palm [4] contributed a lin-
guistically diverse dataset covering 22 Arab countries, combining MSA and dialectal
instructions.
In the multimodal space, Peacock [13] released the Henna benchmark to test
cultural competence, and JEEM [14] introduced dialect-aware visual tasks involv-
ing culturally grounded images. ArabicMTEB and Swan [15] offered resources for
evaluating cross-lingual, dialectal, and domain-specific Arabic embeddings.
2.2 Saudi Dialects in LLMs
Despite growing interest in Arabic dialects, Saudi-specific evaluations remain limited.
SaudiCulture [6] evaluated five LLMs across five Saudi regions, revealing performance
drops on culturally grounded content. AL-QASIDA [16] examined nine LLMs across
eight dialects—including Saudi Arabic—using fidelity and diglossia metrics, and dis-
cussed pretraining implications. Other benchmarks, such as Dallah [9] and Palm [4],
included Saudi dialects but lacked focused analysis. LLM-MT-Data [17] used LLMs to
translate Saudi speech data into MSA, and AraBench [18] explored dialect-to-English
translation with fine-tuning and back-translation.
A notable data-centric effort is the KIND dataset [19], which collected fine-grained
dialectal Arabic through a community-driven competition. KIND includes parallel
corpora and Q&A spanning 29 Saudi dialects, with city-level granularity. However, it
is primarily designed for data collection and does not offer a structured evaluation of
LLMs’ contextual understanding, a gap Absher seeks to fill.
A key point of contrast is with SaudiCulture [6], which introduced a pioneering
cultural benchmark. However, it is limited to 441 questions focused mainly on general
knowledge and cultural themes predominantly in MSA. In contrast, Absher provides a
broader and more targeted evaluation with a significantly larger volume of questions.
It is uniquely designed for a fine-grained, dialect-sensitive assessment across Saudi
dialects, focusing on the nuanced understanding of words, phrases, and proverbs.
Unlike SaudiCulture, which emphasizes high-level cultural reasoning, Absher enables
a deep, multi-category evaluation drawn from region-specific vernacular data, making
it a more comprehensive and regionally grounded resource for advancing Arabic NLP.
While these studies offer valuable insights, none provide a comprehensive bench-
mark that systematically evaluates LLMs on Saudi dialects across linguistic units such
as words, phrases, and proverbs. Existing work often overlooks the sociocultural speci-
ficity of regional expressions. In contrast, Absher introduces a fine-grained, culturally
contextualized benchmark that spans multiple Saudi dialects and domains, enabling
detailed evaluation of LLMs’ dialectal and cultural understanding. It further differen-
tiates itself through real-world question design, multi-unit coverage, and region-aware
analysis of model behavior.
3 Constructing Absher Benchmark
To assess the ability of computational systems to understand the dialectal and cultural
nuances specific to Saudi Arabia, we introduce the Absher Benchmark. This evaluation
framework is built upon a curated set of dialectal contents, including words, phrases,
5

--- Page 6 ---

and proverbs, representing diverse regions across Saudi Arabia. The development
process followed a structured pipeline encompassing data collection, pre-processing,
prompt engineering, automated question generation, and expert-based review as seen
in Figure 2.
Data Collection 
Prompt Design
Question Generation 
using ChatGPT API
Human Evaluation 
Saudi Dialects
Words
Phrases
Proverbs
Preprocessing
Models
LLMs Performance Evaluation
Benchmark Development
Fig. 2: The overall pipeline of constructing Absher benchmark.
The resulting benchmark provides a systematic and scalable method for evaluating
LLMs on their ability to interpret regional language variation, contextual meanings,
and culturally embedded expressions. As illustrated in Figure 2, the development
process spans from initial data acquisition to final model evaluation, allowing both
fine-grained analysis and performance benchmarking of LLMs in Saudi dialects.
3.1 Data Collection
To evaluate the ability of computational models to interpret Saudi dialects and cultur-
ally embedded expressions, we introduce Absher, a benchmark grounded in authentic
regional content. It is built from a curated collection of dialectal items, including
words, phrases, and proverbs, representing linguistic diversity across Saudi Arabia.
The core of the dataset was collected from the Moajam website1, a digital repos-
itory that aggregates dialectal vocabulary across Arabic regions. We scraped and
organized entries into three categories: words, phrases, and proverbs, each annotated
with its meaning, dialect label, contextual usage, and translation. This process ensured
a comprehensive coverage of both literal and figurative expressions relevant to regional
Saudi Arabic.
• Words refer to vocabulary items specific to Saudi dialects, often including slang or
regional variants not found in Modern Standard Arabic.
• Phrases encompass idiomatic or conversational expressions commonly used across
regions.
• Proverbs are culturally rooted sayings that convey implicit meanings, requiring
contextual and cultural understanding.
1https://ar.mo3jam.com/
6

--- Page 7 ---

The raw collection initially consisted of 5,483 items, which were refined through
pre-processing and filtering, resulting in 3,094 unique contents used to generate over
18,000 multiple-choice questions across six task types. Table 1 summarizes the dataset
statistics.
Table 1: Content statistics before and after pre-processing and the number of
generated questions by category.
Category
# Contents (Raw)
# Contents (Filtered)
# Generated Qs
Words
4,428
2,533
15,198
Phrases
869
478
2,868
Proverbs
186
83
498
Total
5,483
3,094
18,564
3.2 Pre-processing Steps
After data collection, we applied a systematic pre-processing pipeline to refine the
dataset for effective question generation. This phase included deduplication, normal-
ization, and structural formatting. We focused exclusively on entries labeled as Saudi
dialects, retaining regional variants such as Central, Western, Southern, Northern, and
Eastern. Additionally, general Saudi terms—expressions widely used across the coun-
try regardless of region—were preserved to ensure comprehensive linguistic coverage.
We further standardized spelling and usage variations across dialects to ensure consis-
tency, particularly for words with multiple colloquial forms. This harmonization was
essential for generating uniform prompts and minimizing ambiguity in model evalu-
ation. After filtering and normalization, the dataset was reduced to 3,094 contents:
2,533 words, 478 phrases, and 83 proverbs, as shown in Table 1. Finally, the cleaned
data was structured into a machine-readable format suitable for automated prompt
generation, forming a high-quality foundation for the benchmark tasks.
3.3 Prompt Design
To rigorously assess the capabilities of LLMs in interpreting Saudi dialects, we
employed a structured prompt design strategy tailored to dialectal understanding.
Each prompt template included four core components: a task description, a dialect-
based question, multiple-choice answer options, and a designated correct answer.
Table 2 provides an illustration. The prompts were derived from dialectal contents,
such as words, phrases, and proverbs. Each annotated with its dialect label, meaning,
and a contextual usage example.
The initial prompt generation followed a simple formulation process, but several
issues emerged. Correct answers frequently appeared in fixed positions (e.g., always
option A), True/False questions were heavily biased toward “True”, and some ques-
tions included incorrect dialectal labels. These inconsistencies introduced unintended
biases, undermining the fairness and reliability of the benchmark.
7

--- Page 8 ---

To address these limitations, we refined the prompt design by introducing struc-
tural controls. The correct answer positions were randomized to prevent positional
bias, and the distribution of True/False items was balanced to ensure fairness. Dialect
annotations were reviewed and validated by linguistic experts to confirm their accu-
racy. Crucially, we implemented a rigorous two-step filtering strategy to handle
abnormal model outputs from GPT-4o:
• Automated Filtering (Formatting and Structure): All generated outputs
were subjected to a validation script to check for strict structural integrity. This
script automatically flagged and discarded any questions that contained malformed
JSON output, failed to include exactly four distinct multiple-choice options, or did
not designate a clear correct answer. This ensured only well-structured, testable
items proceeded to the next phase.
• Manual Curation (Hallucination and Semantic Errors): A team of two
native Saudi Arabic speakers and linguistic experts manually reviewed a sample
of automatically validated questions. Their primary task was to filter out seman-
tic errors and hallucinations, specifically removing questions where the generated
options were culturally inaccurate, the question’s premise contradicted the source
material (meaning or context), or the designated correct answer was objectively
wrong.
These refinements significantly improved the robustness, validity, and represen-
tativeness of the final set of multiple-choice questions, establishing Absher as a
dependable tool for dialect-sensitive LLMs evaluation. For the complete prompt
template, please refer to Appendix A.
Table 2: Template for question formulation
Component
Description
Task:
Describes the task or the function of the question.
Question:
The question that is presented to the model.
Multi-choice Options:
Option A, B, C, and D.
True/False Options:
A) True, B) False
Correct Answer:
The correct answer to the question.
3.4 Question Generation
Building upon the refined prompt templates, we conducted large-scale question gen-
eration using the ChatGPT API (GPT-4o). We selected GPT-4o for this task
due to its strong multilingual capabilities and demonstrated proficiency in both
literal and contextual understanding. Its robustness in handling diverse linguistic
inputs made it particularly well-suited for generating high-quality, dialect-specific
multiple-choice questions that require nuanced cultural reasoning. Compared to
smaller or monolingual models, GPT-4o also exhibited greater consistency and fewer
hallucinations—qualities essential for ensuring the validity of benchmark items.
8

--- Page 9 ---

Each cleaned and pre-processed content item, whether a word, phrase, or proverb,
was programmatically paired with its dialect label, meaning, and usage example to
construct a complete input prompt. This setup enabled GPT-4o to generate questions
that evaluated not only surface-level understanding but also deeper comprehension
of dialectal and cultural nuances. For each dialectal item, the model generated six
distinct types of questions, with each type targeting a specific dimension of language
understanding:
• Meaning: Assessing the model’s ability to correctly interpret or define dialectal
expressions.
• True/False: Testing the factual correctness of statements about the term or its
usage.
• Fill-in-the-Blank: Evaluating the model’s ability to infer missing words in context.
• Contextual Usage: Determining whether the model can accurately apply the term
within a complete sentence.
• Cultural Interpretation: Probing the understanding of cultural or metaphorical
meanings, particularly in proverbs.
• Location Recognition: Identifying the geographic or regional origin associated
with the dialectal term.
This systematic generation approach ensured comprehensive coverage of the lin-
guistic and cultural characteristics embedded in the Saudi dialects. By applying the
process across all content categories, words, phrases, and proverbs, a total of 18,564
multiple-choice questions were generated. These questions form the core of the Absher
benchmark and allow for a rigorous, multifaceted evaluation of LLM performance.
Table 3 shows the distribution of questions across regional dialects, highlighting the
benchmark’s broad linguistic representation.
The distribution of questions across regional dialects reflects the linguistic land-
scape of Saudi Arabia. The Najdi dialect, spoken predominantly in the Central region,
and the Hejazi dialect, prevalent in the Western region, are spoken by a larger portion
of the population and receive extensive exposure through media and online platforms.
This widespread usage provides a richer pool of linguistic material. By contrast, the
Southern, Northern, and Eastern dialects have a more localized presence, with fewer
readily accessible resources. Despite these differences, the benchmark includes all
major dialects, thus capturing the full spectrum of Saudi Arabic and supporting a
comprehensive evaluation of LLM performance.
Figure 3 illustrates the six types of questions included in the benchmark. Together,
these types enable a well-rounded evaluation of model capabilities, covering meaning
interpretation, cultural and regional understanding, and recognition of local expres-
sions. The use of a standardized prompt template throughout the generation process
ensures consistency, minimizes bias, and strengthens the reliability of the evaluation.
3.5 Human Evaluation
To validate the reliability, correctness, and cultural appropriateness of the questions in
the Absher benchmark, we performed a structured human evaluation. This step was
9

--- Page 10 ---

Table 3: Number of questions
per regional dialects in the
Absher benchmark.
Dialect
# Qs
Central
5,652
Western
5,262
Southern
2,682
Northern
414
Eastern
216
General Saudi Terms
4,338
Phrases – Meaning
Words – True/False
Proverbs – Fill-in-the-Blank
Phrases – Cultural Interpretation
Proverbs – Contextual Usage
Words – Location Recognition
 اختر اإلجابة الصحيحة فقط دون أي:المهمة
.مالحظات إضافية
"؟'اش بك يواد' ما معنى العبارة" :السؤال 
 :الخيارات 
  كيف حالك؟)A 
  ماذا بك ايها الفتى)B 
  أين كنت؟)C 
  لماذا تأخرت؟)D 
 اختر اإلجابة الصحيحة واحدة فقط دون:المهمة
.أي مالحظات إضافية
 في اللهجة"أريد"  تعني"أشا"  كلمة:السؤال
.الجيزانية
:الخيارات
 صحيح)A
 خطأ)B
 
 اختر اإلجابة الصحيحة فقط دون أي:المهمة
.مالحظات إضافية
"._____ اللي ما يعرف الصقر"  مثل:السؤال
:الخيارات
يصيده  )A
يزرعه  )B
يشويه  )C
يجمعه  )D
 
 اختر اإلجابة الصحيحة فقط دون أي:المهمة
.مالحظات إضافية
اطلع من'  ما الذي ترمز إليه عبارة:السؤال
 في الثقافة السعودية؟'مخي
:الخيارات
. تدل على التجاهل)A
. تعبر عن الصداقة)B
. تشير إلى االنشغال)C
. الحلول السريعة للمشاكل)D
 اختر إجابة واحدة فقط دون أي مالحظات:المهمة
.إضافية
 في أي سياق يمكن استخدام المثل:السؤال
؟"الذيب على طاريه"
:الخيارات
 عندما يظهر شخص فجأة بعد الحديث عنه)A
 عندما يتغلب شخص على الصعوبات)B
 عندما يقوم شخص بمساعدة اآلخرين)C
ل عندما يكون شخص ما محتااً)D
. حدد الموقع الجغرافي المرتبط بالكلمة:المهمة
 في أي منطقة سعودية ُت ستخدم كلمة:السؤال
 بشكل أكبر؟'عْ ْاْف َق'
:الخيارات
 مكة)أ
 الرياض)ب
 جدة)ج
 الدمام)د
Fig. 3: An illustration of the different question types. The first line in each example
indicates the task type, the second line presents the question, and the subsequent lines
list the answer options. The correct answers are marked in green.
essential to ensure that the automatically generated content adhered to linguistic stan-
dards and dialectal relevance, especially given the complexity and regional variability
of Saudi dialects. Four native Saudi Arabic speakers participated in the evaluation.
All annotators were fluent in multiple regional dialects and possessed strong familiar-
ity with the cultural and linguistic diversity across Saudi Arabia. They were divided
into two independent groups, each assigned a distinct subset of the data. This setup
enabled broader dataset coverage, minimized cross-group bias, and reduced cognitive
fatigue.
A pilot study preceded the main annotation phase to ensure consistent interpre-
tation of the evaluation guidelines. Annotators were presented with 20 representative
sample contents (120 questions total), covering diverse dialects and question types.
10

--- Page 11 ---

These examples served to familiarize them with the annotation tasks and resolve any
ambiguities in advance. To test attentiveness and accuracy, the pilot set included
quality control questions with plausible yet incorrect answers. Annotators, who mis-
classified these, were received follow-up clarifications to align their understanding
with the evaluation standards. This step improved consistency and reliability of the
judgment in the formal evaluation.
The main evaluation involved a stratified random sample comprising 10% of the
benchmark contents, i.e., Words, Phrases, and Proverbs, across all six question types.
This resulted in 600 annotated questions. Complete annotation guidelines, includ-
ing task definitions, assessment criteria, and illustrative examples, are provided in
Appendix B. Based on these instructions, annotators completed two core tasks:
• Question Quality: Evaluate each question for clarity, fluency, and logical struc-
ture, with attention to dialectal appropriateness and cultural sensitivity.
• Answer Correctness: Verify whether the answer labeled as correct by the model
aligns with the ground-truth answer based on the dialectal dataset.
Inter-annotator agreement was measured using Cohen’s Kappa coefficient. Table 4
shows strong agreement across most question types, particularly for Meaning and
Cultural Interpretation, where Kappa values exceed 0.94. While Fill-in-the-Blank and
Contextual Usage tasks yielded slightly lower agreement in question quality (0.71 and
0.72, respectively), the values still fall within acceptable reliability thresholds. Addi-
tionally, we computed the overall alignment between model-generated answers and
human judgments, which reached 93.03%, confirming the reliability and consistency
of the benchmark’s human evaluation process.
Table 4: Cohen’s Kappa scores for question quality and
answer correctness across different question types. Bold
denotes the top scores.
Q-Type
Q-Quality
A-Correctness
Meaning
0.97
0.97
True/False
0.95
0.87
Fill-in-the-Blank
0.71
0.91
Contextual Usage
0.72
0.88
Cultural Interpretation
0.83
0.94
Location Recognition
0.85
0.92
4 Experiments
We evaluated a set of open-source LLMs: LLaMA-3 8B Instruct [20], Jais-13B [21],
ALLaM-7B [22], Mistral-7B [23], Qwen2.5-7B Instruct [24], and AceGPT-7B-
chat [25]. These models were chosen based on three main criteria: open availability,
Arabic language support, and competitive performance across a range of NLP tasks.
11

--- Page 12 ---

All models were evaluated in a zero-shot setting, without any task-specific fine-tuning,
to assess their inherent ability to understand Saudi dialects and cultural content. Since
the benchmark is composed exclusively of multiple-choice questions, we employed
four standard classification metrics: Accuracy, Precision, Recall, and F1 Score. These
metrics offer a comprehensive and balanced evaluation of model performance, in line
with prior work on zero-shot LLMs assessment for low-resource languages [26].
Table 5: Average evaluation results of models performance. Bold denotes the best
result achieved across all models for each content type, while underlining indicates
the best-performing content type for each individual model.
Model
Content Type
Accuracy
Precision
Recall
F1-score
ALLaM
Word
40.32%
33.07%
26.63%
17.28%
Phrase
42.28%
30.54%
26.38%
19.42%
Proverb
48.74%
39.95%
37.76%
31.43%
LLaMA
Word
41.30%
36.19%
23.99%
16.63%
Phrase
43.41%
29.66%
24.13%
18.07%
Proverb
45.31%
28.55%
28.60%
18.87%
Jais
Word
42.66%
32.78%
24.76%
14.78%
Phrase
41.94%
37.81%
27.27%
16.27%
Proverb
41.81%
17.52%
28.33%
15.91%
Mistral
Word
47.90%
22.80%
30.05%
23.98%
Phrase
44.80%
28.11%
33.09%
26.02%
Proverb
45.10%
18.27%
29.05%
22.31%
Qwen
Word
63.00%
42.07%
46.10%
41.18%
Phrase
43.68%
33.58%
32.93%
26.00%
Proverb
44.38%
31.36%
33.16%
29.56%
ACEGPT
Word
41.90%
33.98%
33.18%
28.30%
Phrase
39.93%
33.68%
32.55%
29.61%
Proverb
34.81%
37.93%
33.15%
27.51%
4.1 Results
Table 5 presents the performance of the six evaluated models, such as ALLaM,
LLaMA, Jais, Mistral, Qwen, and ACEGPT, across different content types, namely
words, phrases, and proverbs. The results reveal noticeable variations in performance
depending on both the linguistic content and the complexity of the task2. For word-
level content, the Qwen model demonstrated the strongest capabilities, achieving an
2The full set of results is provided in Appendix D.
12

--- Page 13 ---

accuracy of 63.00% and an F1-score of 41.18%. These results indicate Qwen’s effec-
tiveness in handling isolated lexical items, suggesting its advantage in processing tasks
that rely on clear, context-independent meanings.
To contextualize the reported performance, it is important to note the chance-level
baseline for this benchmark. Since most multiple-choice questions contain four options,
random guessing corresponds to 25% accuracy (and 50% for True/False items). There-
fore, the observed performance range of approximately 40–60% accuracy across models
is substantially above chance, highlighting both the non-trivial capability of the eval-
uated LLMs and the inherent difficulty of the dialect- and culture-sensitive questions
in Absher.
In contrast, phrase-level tasks presented a more competitive landscape. Mistral
achieved the highest F1-score at 26.02%, with Qwen and ACEGPT following closely
behind. This reflects a broader challenge for all models when dealing with phrases,
which often carry more ambiguous or context-dependent meanings compared to indi-
vidual words. Proverb-based tasks emerged as the most challenging across all models,
reflecting the complexity and cultural depth embedded in such expressions. Despite
these challenges, ALLaM led in this category with an accuracy of 48.74% and an F1-
score of 31.43%, indicating its relative strength in handling idiomatic and culturally
grounded language. In contrast, models such as Jais consistently recorded lower F1-
scores across all content types, particularly for proverbs, highlighting limitations in
their ability to process culturally rich or metaphorical expressions.
These findings show a consistent trend: while certain models demonstrate strong
performance on words or phrases, accurately processing complex cultural constructs
like proverbs remains a significant challenge. This highlights the need for further
research to enhance LLMs’ ability to handle the nuanced and context-heavy aspects
of language, particularly those rooted in cultural knowledge and idiomatic usage.
5 Analysis
5.1 Impact of Model Size and Language Orientation
Table 6 summarizes the models evaluated with respect to parameter size, language ori-
entation, and open-source availability. The set of models includes Arabic-specific and
multilingual LLMs, spanning different sizes and scales, from 7B to 13B parameters.
While it is often assumed that larger parameter counts lead to better performance,
our results demonstrate that accuracy does not scale linearly with size. For example,
Qwen, a 7B multilingual model, achieved the highest overall accuracy of 50.35%, out-
performing the larger Arabic-native Jais model (13B) by nearly 10%. Similarly, Mistral
(7B) achieved 45.93%, exceeding the performance of some larger Arabic-specialized
models. A deeper comparison of Arabic-native models (ALLaM, Jais, ACEGPT) ver-
sus multilingual LLMs (Qwen, Mistral, LLaMA) reveals additional insights. Despite
being trained specifically on Arabic data, Arabic-native models did not consistently
outperform their multilingual counterparts in tasks involving dialectal variation and
cultural nuances.
13

--- Page 14 ---

Table 6: Overview of the evaluated models, highlighting their size, supported lan-
guages, and average accuracy achieved in the experiments. The best results are listed
from highest to lowest, with the three best results in bold.
Model
Size
Language
Accuracy
Qwen2.5 Instruct
7B
Multilingual
50.35%
Mistral
7B
Multilingual
45.93%
ALLaM 3rd
7B
Arabic
43.78%
LLaMA-3 Instruct
8B
Multilingual
43.34%
Jais
13B
Arabic
42.14%
AceGPT-chat
7B
Arabic
38.88%
Qwen demonstrated strong performance across tasks, particularly in contextual
usage (64.7%) and cultural interpretation (63.7%), highlighting the benefits of mul-
tilingual pretraining combined with advanced architecture. ALLaM, though smaller
and Arabic-focused, performed competitively in proverb-based cultural interpreta-
tion (60.0%) and contextual usage tasks. Mistral, a multilingual model with only 7B
parameters, achieved balanced performance and notably excelled in binary reasoning
(58.4% in word-level True/False questions), emphasizing the importance of architec-
tural optimization. LLaMA showed clear strengths in location recognition (66.3%) but
underperformed in tasks requiring deeper semantic understanding. Among Arabic-
native models, ACEGPT achieved solid results in contextual usage (54.5%), while Jais
led in location recognition (67.6%) but exhibited limitations in cultural and semantic
tasks.
Overall, these findings suggest that specialization in Arabic does not inher-
ently guarantee superior performance on culturally complex or dialectally rich tasks.
Instead, the combination of diverse multilingual training, effective architectural
design, and optimized parameter utilization appears to be more influential. Perfor-
mance tends to be stronger on lexical and recognition tasks but decreases as linguistic
and cultural complexity increases, particularly with proverbs and culturally loaded
expressions.
5.2 Examination of Model Responses by Region
Our evaluation of LLMs responses to region-specific linguistic questions, detailed in
Figure 4, reveals considerable performance variability influenced by both the geo-
graphic origin of expressions and the nature of the linguistic task. Notably, we observed
strong performance in the General category for a widely known proverb, with five out
of six models providing correct answers. This aligns with the expectation that fre-
quently cited expressions, which appear widely in public discourse, are more likely to
be accurately interpreted due to their higher representation in pretraining datasets.
In contrast, expressions from the Southern region resulted in a consistent failure
across all six models. The proverb tested was regionally specific and less documented,
14

--- Page 15 ---

Fig. 4: Model responses to dialect-based questions from different Saudi regions. Each
example shows the question, its regional, and the answers from six LLMs.
suggesting limited representation in training data and highlighting the persistent chal-
lenges LLMs face with culturally embedded content from low-resource dialects. For the
Central region, performance on a location recognition task was mixed. While ALLaM
and Jais correctly identified the dialectal origin, other models defaulted to major urban
centers such as Riyadh or Jeddah. This pattern likely reflects an urban-centric bias
within the models’ training corpora. Interestingly, the Northern region, despite being
underrepresented in online resources, saw three models correctly answer a true/false
phrase question. This suggests that task structure can, to some extent, mitigate data
scarcity, as binary questions allow models to leverage contextual inference or statistical
patterns to produce correct responses.
In the Eastern region, performance remained low, with only ACEGPT correctly
interpreting the contextual usage of a time-related word. This outcome emphasizes the
difficulty models encounter when handling dialectal expressions that rely on contex-
tual understanding, particularly for less represented regions. Finally, for the Western
region, five of six models successfully identified the cultural function of a widely circu-
lated annoyance phrase. This likely reflects the increased presence of such expressions
in social or digital spaces, enhancing their visibility within pre-training data.
Overall, these results reveal persistent challenges in capturing region-specific lin-
guistic and cultural nuances. Although models tend to perform well with broadly
known or globally circulated expressions, they consistently struggle with dialects and
15

--- Page 16 ---

phrases deeply rooted in local practices. This underscores the need for more inclu-
sive and dialect-rich datasets that reflect the full diversity of linguistic and cultural
realities between regions.
5.3 Performance Across Content and Question Types
Figure 5 presents a detailed analysis of model performance across content categories,
revealing key trends in how different LLMs handle dialectal material. Qwen con-
sistently outperformed other models, achieving the highest accuracy on word-level
questions, particularly in the meaning and contextual usage types, with an overall
peak of approximately 63.5%. ALLaM demonstrated notable strengths in cultural
interpretation tasks, especially when dealing with proverbs, where it surpassed 48%
accuracy. An interesting pattern emerged in relation to content type: questions based
on proverbs consistently resulted in higher model accuracy compared to those based
on isolated words or phrases. This may be attributed to the richer context and more
explicit cultural cues embedded within proverbs, which provide clearer semantic and
pragmatic signals.These results suggest that LLMs benefit from contextually grounded
input and perform more reliably when exposed to culturally meaningful expressions.
Complementing this content-based analysis, Figure 6 illustrates how the models
performed on different types of questions. Among all types, location recognition ques-
tions were the most successfully handled, with average model accuracy exceeding 58%.
Jais performed particularly well in this category, reaching 62% accuracy—indicating
that models are generally capable of linking dialectal features to their corresponding
regions. In contrast, the True/False questions pose the greatest challenge, especially
when derived from short or context-poor input, such as individual words or brief
phrases. These questions required binary reasoning with limited context, leading to
lower performance. Accuracy for this type ranged from 22% (Jais) to 58% (Qwen),
underscoring the difficulties LLMs face in making confident decisions under ambiguity
or minimal input cues. Overall, these results highlight the dual importance of lin-
guistic structure and contextual richness in benchmarking the dialectal and cultural
understanding of LLMs.
5.4 Case Study of LLMs Responses Across Question Types
and Dialects
Our case study investigates the performance of six LLMs across culturally embedded
tasks derived from various Saudi dialectal regions. To illustrate observed performance
patterns, we examine specific model responses across varied content types, ques-
tion structures, and dialects, as detailed in Tables 7 to 9. The results indicate that
regionally common and widely used expressions are more accurately interpreted by
LLMs. For example, in the general category, the proverb: ”Itha Hajat Al-Baqara Ala
Qoroniha”, its translation is ”If the cow performs Hajj on its horns” (See Table 7)
was correctly understood by five out of six models: ALLaM, LLaMA, Jais, Qwen, and
ACEGPT all provided the correct answer, while only Mistral failed. This proverb is
relatively widespread, and its meaning, “something impossible to achieve”, is often
documented in public sources, likely increasing its representation in model training
16

--- Page 17 ---

Fig. 5: Average Accuracy for Different Models by Content Type
Fig. 6: Average Accuracy for Different Models by Question Type
data. In contrast, proverbs that are more regionally isolated or culturally specific,
such as the Southern fill-in-the-blank proverb : ”Khattet fi maa wa aqbas fi heid”, its
translation is ”Plan in water and pinch in a rock” (See Table 8), saw a complete failure
across all six models. None of the models, i.e., ALLaM, LLaMA, Jais, Mistral, Qwen,
and ACEGPT, selected the correct option, suggesting a consistent gap in exposure to
underrepresented regional idioms, especially those originating from areas with fewer
accessible textual resources.
Additionally, the study revealed notable differences in the models’ ability to com-
prehend regional dialects, particularly in how they responded to specific tasks based
on region and question type. For example, when tasked with identifying a location-
specific term (See Table 9) from the Central region, only two models, ALLaM and
Jais, were able to correctly associate it with the Al-Qassim region. The other mod-
els, however, defaulted to more familiar urban areas, like Riyadh and Jeddah, likely
17

--- Page 18 ---

Table 7: Model answers to a proverb meaning question in the general dialect.
Content Type:
Proverb
Question Type:
Meaning
Region:
General
Models’ Answer:
ALLaM: B ,
LLaMA: B ,
Jais: B ,
Mistral: C ,
Qwen: B ,
ACEGPT: B
Table 8: Model answers to a fill-in-the-blank proverb in the southern dialect.
Content Type:
Proverb
Question Type:
Fill-in-the-Blank
Region:
Southern
Models’ Answer:
ALLaM: D ,
LLaMA: B ,
Jais: D ,
Mistral: D ,
Qwen: A ,
ACEGPT: D
due to the prevalence of these dialects in the training materials. Urban dialects from
cities such as Riyadh, Jeddah, and Khobar are more commonly represented in online
resources, which could explain why the models showed a preference for these regions.
In contrast, like Qassim, Aseer, or the southern regions face challenges due to limited
textual data from these areas.
Moreover, when it comes to other local dialects from the Eastern, Northern, or
Southern parts of Saudi Arabia, significant discrepancies in the models’ performance
were noted. Expressions and words specific to these regions were often misunderstood,
18

--- Page 19 ---

Table 9: Model answers to a location recognition word question in the central dialect.
Content Type:
Word
Question Type:
Location Recognition
Region:
Central
Models’ Answer:
ALLaM : A ,
LLaMA : B ,
Jais : A ,
Mistral : B ,
Qwen : C ,
ACEGPT : D
highlighting the gap in representation for these dialects. This contrast underscores the
fact that while widely recognized expressions are easily interpreted, culturally unique
idioms that are specific to certain regions are much harder for the models to grasp.
Overall, our comprehensive evaluation underscores that while contemporary LLMs
possess considerable linguistic breadth in Arabic dialects, their depth of understanding
for more nuanced, regionally isolated, or culturally embedded expressions remains a
significant limitation. These findings collectively point to the crucial need for more
extensive and geographically diverse dialectal data in future LLMs training to achieve
truly robust and culturally sensitive linguistic AI.
6 Discussion
This research presents Absher, a novel benchmark aimed at evaluating LLMs on
Saudi dialects, a linguistically rich yet underrepresented subset of Arabic. Unlike prior
work such as Dallah [9], Palm [4], and AL-QASIDA [16], which aggregate dialects
or focus on broader Arabic settings, Absher uniquely provides fine-grained, region-
specific coverage of Saudi dialects, including Central, Western, Southern, Eastern, and
Northern varieties. Absher’s strength lies in its foundation: over 18,000 multiple-choice
questions derived from a curated dataset of dialectal words, phrases, and proverbs
sourced from these five major Saudi regions. The benchmark systematically spans six
distinct task categories: Meaning, True/False, Fill-in-the-Blank, Contextual Usage,
Cultural Interpretation, and Location Recognition.
Our findings highlight notable patterns in how LLMs handle Saudi dialects. Loca-
tion Recognition tasks yielded the highest performance, likely due to the concrete
and frequently occurring nature of geographic references in training data, which aids
retrieval and identification. In contrast, True/False questions were the most chal-
lenging, especially in low-context settings, reflecting the inherent difficulty of binary
19

--- Page 20 ---

reasoning tasks that require nuanced cultural and contextual understanding beyond
surface-level lexical cues.
Furthermore, Qwen’s strong performance, especially in Meaning, Contextual
Usage, and Cultural Interpretation questions, demonstrates its robust semantic under-
standing and ability to accurately interpret dialectal expressions in context. Across
content types, performance varied by model rather than being uniformly highest for
any single type. While some models (e.g., ALLaM) achieved relatively stronger results
on Proverbs, others, such as Qwen, performed best on Word-level questions, indicat-
ing that certain models benefit more from the richer contextual and cultural cues
provided by longer and more nuanced inputs. For instance, ALLAM’s relatively high
performance in Cultural Interpretation of proverbs highlights its ability for deeper
socio-cultural reasoning, likely attributed to its Arabic-centric training.
The results reveal a noticeable gap between multilingual and Arabic-native mod-
els. Models like Qwen and Mistral, which were trained on a wide range of languages,
outperformed their Arabic-centric counterparts in overall accuracy. Their ability to
generalize across dialectal variations, despite not being trained explicitly on Saudi
dialects, reflects the benefits of exposure to diverse language data. These results
align with observations from Palm [4] and related studies, where multilingual models
correlated with higher robustness on non-standard Arabic input.
Nevertheless, Arabic-native models demonstrated strengths in specific areas.
For example, ALLaM achieved high accuracy in tasks involving proverbs, while
Jais performed relatively well in location-based recognition. These patterns sug-
gest that domain-specific pretraining provides advantages in interpreting traditional
or idiomatic expressions, even if it does not generalize as effectively across diverse
question types. Such findings align with results from the AraDiCE benchmark [3],
where models exhibited improved performance when test data resembled the training
distribution. To further demonstrate model differences, consider a Cultural Inter-
pretation question based on the proverb: ”Ally ma ya’arf alsger yshwaeh”, meaning
”He who doesn’t recognize the falcon cooks it” While ALLAM accurately selected
the metaphorical interpretation (“Those who lack knowledge may misuse valuable
things”), other models like Jais and ACEGPT selected overly literal or generic options.
This reflects ALLAM’s stronger grounding in socio-cultural expressions—a critical
strength when applying LLMs in culturally sensitive settings.
In summary, our findings reveal a clear gap in current LLMs’ ability to com-
prehensively handle the diverse spectrum of Saudi Arabic dialects, especially in less
standardized or culturally nuanced forms. While multilingual models demonstrate
stronger generalization capabilities, Arabic-native models show targeted strengths
in specific areas such as cultural interpretation. However, neither category achieves
consistently strong performance across all dialects and task types. This discrepancy
can be attributed to structural imbalances in the representation of dialectal forms
within the training data, where widely documented or urban-centered dialects are
more prevalent, whereas regionally specific or culturally embedded expressions remain
underrepresented. Furthermore, performance patterns indicate that model success is
influenced not only by linguistic coverage but also by the alignment between task type
and the type of cultural knowledge required. These insights underscore the need for
20

--- Page 21 ---

more representative and balanced datasets, alongside tailored adaptation strategies
and controlled evaluation methods, to improve model alignment with dialectal Ara-
bic at the national level and to better understand why certain models excel in some
contexts while struggling in others.
6.1 Limitations
While the Absher benchmark represents a significant step toward evaluating LLMs on
Saudi dialects and culture, the study is subject to several limitations. First, the evalu-
ations were conducted under constrained computational resources, which limited our
ability to explore multiple model configurations or conduct repeated trials. Second,
all models were assessed using a fixed prompt structure (e.g., “Answer as if you are
a Saudi. . . ”), which may have influenced model behavior. Future work could explore
the impact of prompt variation and instruction tuning. Third, although human eval-
uation was performed on a stratified sample to ensure dataset quality, a complete
manual review of all 18,564 questions was not feasible due to the scale and diversity of
the benchmark. Finally, while Absher covers various regional Saudi dialects, the rep-
resentation of these dialects within the dataset is not perfectly balanced; for instance,
Central and Western dialects are more prevalent. That highlights the need for more
diverse and evenly distributed resources to comprehensively capture all Saudi dialectal
variations in future research. Future research should leverage more extensive computa-
tional infrastructure, experiment with prompt engineering strategies and fine-tuning
methods. It should also incorporate broader expert reviews to further enhance the
accuracy, reliability, and cultural validity of the benchmark evaluations.
6.2 Ethical Considerations
This study utilizes publicly available data sources to evaluate the dialectal under-
standing of LLMs within the Saudi context. Care was taken to ensure that no private,
identifiable, or sensitive information was included in the dataset. To guarantee this, all
dialectal content—including words, phrases, and proverbs— was sourced exclusively
from the publicly accessible Moajam website. This resource functions as a digital
repository of aggregated dialectal vocabulary and cultural expressions. We explicitly
excluded any conversational data, social media content, or personally generated user
text to safeguard against the unintentional inclusion of private information or the
leakage of toxic language that is often prevalent in online datasets.
The primary ethical risk in dialectal evaluation is the potential for linguistic dis-
crimination, where underrepresented dialects are implicitly or explicitly associated
with lower social status or performance failure by the model. To mitigate this critical
risk, we implemented two concrete measures. First, the Absher dataset was rigorously
designed to ensure fair coverage across the five major Saudi regions (Central, West-
ern, Southern, Eastern, and Northern), deliberately challenging the common bias in
NLP datasets that over-represent urban or dominant dialects. Second, the evalua-
tion tasks focus strictly on testing linguistic competence (meaning, contextual usage,
and cultural interpretation) rather than social or demographic inference, preventing
21

--- Page 22 ---

the model from being scored on tasks that could encourage or propagate negative
stereotypes associated with any specific regional dialect.
Given that language models may produce hallucinated or inaccurate out-
puts—particularly in low-resource or culturally nuanced scenarios—we stress that
these outputs should not be used for critical decision-making without human over-
sight. The evaluation framework was carefully designed to minimize cultural bias and
to avoid reinforcing stereotypes.
Finally, our commitment to responsible AI usage extended to our human validation
processes. The validation, which was performed by native speakers from each of the five
regions to confirm dialectal authenticity, was governed. Throughout the project, we
maintained a commitment to transparency and responsible AI usage, acknowledging
the inherent limitations of current LLMs, with the ultimate goal of promoting the
development of fair, inclusive, and culturally aware language technologies.
6.3 Conclusion and Future Work
This paper introduced Absher, a novel benchmark designed to evaluate the capa-
bilities of LLMs in understanding the diverse dialects and rich cultural expressions
across Saudi Arabia. Unlike existing Arabic benchmarks that focus on Modern Stan-
dard Arabic (MSA) or treat dialects at a coarse level, Absher offers fine-grained,
region-specific evaluation through over 18,000 carefully constructed multiple-choice
questions. These questions span six task types—ranging from meaning identification
to cultural interpretation—and are grounded in authentic dialectal content from var-
ious Saudi regions. These questions are derived from a curated dataset of dialectal
words, phrases, and proverbs sourced from five major Saudi regions, and systematically
span six distinct task categories: Meaning, True/False, Fill-in-the-Blank, Contextual
Usage, Cultural Interpretation, and Location Recognition. This comprehensive design
enables multifaceted evaluation across both linguistic and cultural dimensions.
Our evaluation of several state-of-the-art LLMs revealed significant variation in
performance across dialects, question types, and linguistic units. While some models
performed well on tasks like location recognition and contextual usage, they strug-
gled with cultural inference and binary reasoning, especially in low-context scenarios.
Notably, multilingual models such as Qwen and Mistral outperformed Arabic-native
models in general tasks, whereas the latter showed an advantage in interpreting
culturally embedded expressions like proverbs.
Beyond technical performance, this work contributes to a broader sociolinguis-
tic goal: fostering inclusive and culturally sensitive NLP systems. By systematically
incorporating dialectal diversity and cultural context, Absher helps bridge existing
evaluation gaps and supports the development of language technologies that reflect
the lived linguistic realities of users.
Looking forward, future work will expand Absher to include additional dialects,
question formats, and model types. We plan to conduct more in-depth evaluations
using alternative strategies, such as few-shot and fine-tuning scenarios, to better
explore models’ capabilities across dialectal variations and cultural contexts. In addi-
tion, we aim to perform deeper causal analyses to understand the factors driving
model performance across dialects and task types, providing clearer insights into how
22

--- Page 23 ---

linguistic and cultural features influence LLM behavior. Integrating sociolinguistic
features and region-specific datasets may further improve alignment with real-world
language use. Through these efforts, we aim to promote more inclusive, robust, and
context-aware Arabic NLP systems.
Data Availability
We provided several illustrative examples from our benchmark in this paper, and
the complete dataset will be made publicly available for research purposes upon
acceptance.
CRediT authorship contribution statement
Renad Al-Monef: Methodology, Data Curation, Software, Validation, Formal
analysis, Visualization, Writing - original draft. Hassan Alhuzali: Conceptualization,
Supervision, Validation, Writing - review & editing. Nora Alturayeif: Supervi-
sion, Writing - review & editing. Ashwag Alasmari: Conceptualization, Supervision,
Validation, Writing - review & editing.
Declaration of competing interest
The authors declare that they have no competing interests.
Acknowledgment
Declaration of generative AI and AI-assisted technologies in the writing process: Dur-
ing the preparation of this work, we used GPT-4, an AI chatbot developed by OpenAI,
to improve our written work. After using this tool/service, we reviewed and edited
the content as needed and take full responsibility for the content of the publication.
The authors would like also to extend their appreciation to the Deanship of
Research and Graduate Studies at King Khalid University for funding this work
through small group research under grant number RGP1/69/46. The authors also
express their sincere gratitude to Al Bandari Ali Alqahtani , Zainab Abdulaziz Dalim
for their invaluable support and insightful contributions during the evaluation of
Absher benchmark
References
[1] Brown, T.B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Nee-
lakantan, A., Shyam, P., Sastry, G., Askell, A., Agarwal, S., Herbert-Voss, A.,
Krueger, G., Henighan, T., Child, R., Ramesh, A., Ziegler, D.M., Wu, J., Win-
ter, C., Hesse, C., Chen, M., Sigler, E., Litwin, M., Gray, S., Chess, B., Clark,
J., Berner, C., McCandlish, S., Radford, A., Sutskever, I., Amodei, D.: Language
models are few-shot learners (2020)
[2] OpenAI: GPT-4 Technical Report (2023). https://openai.com/research/gpt-4
23

--- Page 24 ---

[3] Mousi, B., Durrani, N., Ahmad, F., Hasan, M.A., Hasanain, M., Kabbani, T.,
Dalvi, F., Chowdhury, S.A., Alam, F.: AraDiCE: Benchmarks for dialectal and
cultural capabilities in LLMs, 4186–4218 (2025)
[4] Alwajih, F., Mekki, A.E., Magdy, S.M., Elmadany, A.A., Nacar, O., Nagoudi,
E.M.B., Abdel-Salam, R., Atwany, H., Nafea, Y., Yahya, A.M., Alhamouri, R.,
Alsayadi, H.A., Zayed, H., Shatnawi, S., Sibaee, S., Ech-Chammakhy, Y., Al-
Dhabyani, W., Ali, M.M., Jarraya, I., El-Shangiti, A.O., Alraeesi, A., Al-Ghrawi,
M.A., Al-Batati, A.S., Mohamed, E., Elgindi, N.T., Saeed, M., Atou, H., Yahia,
I.A., Bouayad, A., Machrouh, M., Makouar, A., Alkawi, D., Mohamed, M.,
Abdelfadil, S.T., Ounnoughene, A.Z., Anfel, R., Assi, R., Sorkatti, A., Tourad,
M.C., Koubaa, A., Berrada, I., Jarrar, M., Shehata, S., Abdul-Mageed, M.: Palm:
A culturally inclusive and linguistically diverse dataset for Arabic LLMs. In:
Proceedings of the 63rd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pp. 32871–32894. Association for Compu-
tational Linguistics, Vienna, Austria (2025). https://doi.org/10.18653/v1/2025.
acl-long.1579 . https://aclanthology.org/2025.acl-long.1579/
[5] Al-Twairesh, N., Al-Matham, R., Madi, N., Almugren, N., Al-Aljmi, A.-H., Alsha-
lan, S., Alshalan, R., Alrumayyan, N., Al-Manea, S., Bawazeer, S., Al-Mutlaq,
N., Almanea, N., Huwaymil, W.B., Alqusair, D., Alotaibi, R., Al-Senaydi, S.,
Alfutamani, A.: Suar: Towards building a corpus for the saudi dialect. Procedia
Computer Science 142, 72–82 (2018) https://doi.org/10.1016/j.procs.2018.10.462
. Arabic Computational Linguistics
[6] Ayash, L., Alhuzali, H., Alasmari, A., Aloufi, S.: Saudiculture: A benchmark
for evaluating large language models’ cultural competence within saudi arabia.
Journal of King Saud University Computer and Information Sciences 37(6), 123
(2025) https://doi.org/10.1007/s44443-025-00137-9
[7] Al-Laith, A., Kebdani, R.: Evaluating calibration of Arabic pre-trained language
models on dialectal text. In: Ezzini, S., Alami, H., Berrada, I., Benlahbib, A.,
El Mahdaouy, A., Lamsiyah, S., Derrouz, H., Haddad Haddad, A., Jarrar, M.,
El-Haj, M., Mitkov, R., Rayson, P. (eds.) Proceedings of the 4th Workshop on
Arabic Corpus Linguistics (WACL-4), pp. 68–76. Association for Computational
Linguistics, Abu Dhabi, UAE (2025). https://aclanthology.org/2025.wacl-1.8/
[8] Alharbi, A.o., Alsuhaibani, A., Alalawi, A.A., Naseem, U., Jameel, S., Kanhere,
S., Razzak, I.: Evaluating large language models on health-related claims across
Arabic dialects. In: El-Haj, M. (ed.) Proceedings of the 1st Workshop on NLP for
Languages Using Arabic Script, pp. 95–103. Association for Computational Lin-
guistics, Abu Dhabi, UAE (2025). https://aclanthology.org/2025.abjadnlp-1.11/
[9] Alwajih, F., Bhatia, G., Abdul-Mageed, M.: Dallah: A dialect-aware multimodal
large language model for Arabic, 320–336 (2024) https://doi.org/10.18653/v1/
2024.arabicnlp-1.27
24

--- Page 25 ---

[10] Hasanaath, A., Alansari, A., Ashraf, A., Salmane, C., Luqman, H., Ezzini, S.:
Arareasoner: Evaluating reasoning-based llms for arabic nlp. arXiv preprint
arXiv:2506.08768 (2025)
[11] Magdy, S.M., Kwon, S.Y., Alwajih, F., Abdelfadil, S.T., Shehata, S., Abdul-
Mageed, M.: JAWAHER: A multidialectal dataset of Arabic proverbs for
LLM benchmarking, 12320–12341 (2025) https://doi.org/10.18653/v1/2025.
naacl-long.613
[12] Guo, G., Naous, T., Wakaki, H., Nishimura, Y., Mitsufuji, Y., Ritter, A., Xu, W.:
Care: Aligning language models for regional cultural awareness. arXiv preprint
arXiv:2504.05154 (2025)
[13] Alwajih, F., Nagoudi, E.M.B., Bhatia, G., Mohamed, A., Abdul-Mageed, M.:
Peacock: A family of Arabic multimodal large language models and benchmarks,
12753–12776 (2024) https://doi.org/10.18653/v1/2024.acl-long.689
[14] Kadaoui, K., Atwany, H., Al-Ali, H., Mohamed, A., Mekky, A., Tilga, S.,
Fedorova, N., Artemova, E., Aldarmaki, H., Kementchedjhieva, Y.: Jeem: Vision-
language understanding in four arabic dialects. arXiv preprint arXiv:2503.21910
(2025)
[15] Bhatia, G., Nagoudi, E.M.B., El Mekki, A., Alwajih, F., Abdul-Mageed, M.:
Swan and ArabicMTEB: Dialect-aware, Arabic-centric, cross-lingual, and cross-
cultural embedding models and benchmarks, 4654–4670 (2025) https://doi.org/
10.18653/v1/2025.findings-naacl.263
[16] Robinson, N.R., Abdelmoneim, S., Marchisio, K., Ruder, S.: AL-QASIDA: Ana-
lyzing LLM quality and accuracy systematically in dialectal Arabic, 22048–22065
(2025) https://doi.org/10.18653/v1/2025.findings-acl.1137
[17] Abdelaziz, A.A.A., Elneima, A.H., Darwish, K.: LLM-based MT data creation:
Dialectal to MSA translation shared task. In: Al-Khalifa, H., Darwish, K.,
Mubarak, H., Ali, M., Elsayed, T. (eds.) Proceedings of the 6th Workshop
on Open-Source Arabic Corpora and Processing Tools (OSACT) with Shared
Tasks on Arabic LLMs Hallucination and Dialect to MSA Machine Translation
@ LREC-COLING 2024, pp. 112–116. ELRA and ICCL, Torino, Italia (2024).
https://aclanthology.org/2024.osact-1.14/
[18] Sajjad, H., Abdelali, A., Durrani, N., Dalvi, F.: AraBench: Benchmarking
dialectal Arabic-English machine translation. In: Scott, D., Bel, N., Zong,
C. (eds.) Proceedings of the 28th International Conference on Computational
Linguistics, pp. 5094–5107. International Committee on Computational Lin-
guistics, Barcelona, Spain (Online) (2020). https://doi.org/10.18653/v1/2020.
coling-main.447 . https://aclanthology.org/2020.coling-main.447/
[19] Yamani, A., Alziyady, R., AlYami, R., Albelali, S., Albelali, L., Almulhim, J.,
25

--- Page 26 ---

Alsulami, A., Alfarraj, M., Al-Zaidy, R.: The kind dataset: A social collaboration
approach for nuanced dialect data collection. In: Proceedings of the 18th Confer-
ence of the European Chapter of the Association for Computational Linguistics:
Student Research Workshop, pp. 32–43 (2024)
[20] Touvron, H., Lavril, T., Izacard, G., et al.: LLaMA 3: Open Foundation and
Instruction-Tuned Models. Meta AI. (2024)
[21] Sengupta, N., Sahu, S.K., Jia, B., Katipomu, S., Li, H., Koto, F., Afzal, O.M.,
Kamboj, S., Pandit, O., Pal, R., Pradhan, L., Mujahid, Z.M., Baali, M., Fikri Aji,
A., Liu, Z., Hock, A., Feldman, A., Lee, J., Jackson, A., Nakov, P., Bald-
win, T., Xing, E.: Jais-13b. Hugging Face. Accessed: 2025-08-1 (2023). https:
//huggingface.co/inceptionai/jais-13b
[22] Bari, M.S., Alnumay, Y., Alzahrani, N.A., Alotaibi, N.M., Alyahya, H.A.,
AlRashed, S., Mirza, F.A., Alsubaie, S.Z., Alahmed, H.A., Alabduljabbar,
G., Alkhathran, R., Almushayqih, Y., Alnajim, R., Alsubaihi, S., Mansour,
M.A., Hassan, S.A., Alrubaian, D.M., Alammari, A., Alawami, Z., Al-Thubaity,
A., Abdelali, A., Kuriakose, J., Abujabal, A., Al-Twairesh, N., Alowisheq,
A., Khan, H.: ALLam: Large language models for arabic and english. In:
The Thirteenth International Conference on Learning Representations (2025).
https://openreview.net/forum?id=MscdsFVZrN
[23] Jiang, A., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D.S., Casas, D.,
Bressand, F., Lengyel, G., Lample, G., Lavaud, L.R., Saulnier, L., Lachaux, M.-
A., Stock, P., Le Scao, T., Lavril, T., Wang, T., Lacroix, T., El Sayed, W.:
Mistral-7B-v0.1. Hugging Face. Accessed: 2025-8-1 (2023). https://huggingface.
co/mistralai/Mistral-7B-v0.1
[24] Yang, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Li, C., Liu, D., Huang,
F., Wei, H., Lin, H., Yang, J., Tu, J., Zhang, J., Yang, J., Yang, J., Zhou, J., Lin,
J., Dang, K., Lu, K., Bao, K., Yang, K., Yu, L., Li, M., Xue, M., Zhang, P., Zhu,
Q., Men, R., Lin, R., Li, T., Tang, T., Xia, T., Ren, X., Ren, X., Fan, Y., Su,
Y., Zhang, Y., Wan, Y., Liu, Y., Cui, Z., Zhang, Z., Qiu, Z., et al.: Qwen2.5: A
Party of Foundation Models (2024). https://qwenlm.github.io/blog/qwen2.5/
[25] Huang, H., Yu, F., Zhu, J., Sun, X., Cheng, H., Dingjie, S., Chen, Z., Alharthi,
M., An, B., He, J., Liu, Z., Chen, J., Li, J., Wang, B., Zhang, L., Sun, R., Wan, X.,
Li, H., Xu, J.: AceGPT, localizing large language models in Arabic, 8139–8163
(2024) https://doi.org/10.18653/v1/2024.naacl-long.450
[26] Nazi, Z.A., Hossain, M.R., Mamun, F.A.: Evaluation of open and closed-source
llms for low-resource language with zero-shot, few-shot, and chain-of-thought
prompting. Natural Language Processing Journal 10, 100124 (2025) https://doi.
org/10.1016/j.nlp.2024.100124
26

--- Page 27 ---

Appendices
A Prompt Example
27

--- Page 28 ---

B Annotation Guideline
Evaluation Guidelines 
1. Answer Correctness (✔️ True / ❌ False) 
 
Task: Ensure that the answer is accurate and correctly corresponds to the 
correct response. 
 
Examples of errors: 
If the selected correct answer is inaccurate or incorrect. 
If the selected correct answer is inaccurate or incorrect : The evaluation is marked as incorrect, 
and further evaluation should be stopped. 
2. Question Quality Evaluation (✔️ Appropriate / ❌ Inappropriate) 
 
The question must be clear and direct, without ambiguity or confusion. 
 
The question should be logical and aligned with the topic. The answer choices 
should logically reflect the question's content and not contain unrealistic or 
irrelevant answers. 
 
Ensure that there is only one correct answer, with no more than one choice that 
could be considered correct. 
 
False 
المهمة :اختيار اإلجابة الصحيحة. 
السؤال :ما معنى كلمة "اهرج "في اللهجة الحجازية؟ 
الخيارات: 
A) اكتب 
B) اتكلم 
C) اسمع 
D) اضحك 
اإلجابة الصحيحة 
 :
 C
 
Reason: The selected correct answer is incorrect, as "اهرج" means "Speak" and not "Listen." 
Appropriate 
Inappropriate 
المهمة :اختيار اإلجابة الصحيحة.
 
السؤال :ما معنى كلمة "اهرج "في اللهجة الحجازية؟ 
الخيارات:
 
   A) اكتب 
   B) اتكلم 
  C) اسمع 
  D) اضحك 
اإلجابة الصحيحة: 
 
 B
 
Reason: The options are more logical, 
and the correct answer is clearly aligned 
with the question. 
المهمة :اختيار اإلجابة الصحيحة. 
السؤال :ما معنى كلمة "اهرج "في اللهجة الحجازية؟ 
الخيارات: 
(A 
 نافذة 
(B 
 شجرة 
C 
 )أتكلم 
D
 )قمر 
اإلجابة الصحيحة 
 :
 C
 
Reason: Options A, B, and D are completely illogical as they are unrelated 
to the meaning of the word "اهرج," making the question weak in terms of 
challenge. 
28

--- Page 29 ---

C The Annotation interface
 
D Detailed Performance
29

--- Page 30 ---

Table 10: Detailed evaluation of the results across content and question types, with
the best results highlighted in dark green to represent the highest scores.
Model
Content Type
Question Type
Accuracy
Precision
Recall
F1-score
ALLaM
Word
Meaning
24.42%
28.08%
25.32%
10.48%
True/False
21.88%
20.45%
24.27%
9.21%
Fill-in-the-Blank
44.24%
39.54%
32.19%
28.19%
Contextual Usage
42.08%
48.53%
27.49%
19.46%
Cultural Interpretation
42.33%
38.99%
25.42%
15.86%
Location Recognition
67.44%
27.63%
25.04%
20.46%
Phrase
Meaning
46.03%
48.09%
35.48%
24.49%
True/False
22.00%
5.55%
24.26%
9.03%
Fill-in-the-Blank
43.53%
32.71%
27.84%
23.35%
Contextual Usage
37.26%
50.58%
23.49%
17.40%
Cultural Interpretation
39.18%
9.82%
24.86%
14.07%
Location Recognition
65.50%
16.48%
24.92%
19.84%
Proverb
Meaning
46.15%
35.00%
32.14%
25.40%
True/False
30.77%
29.17%
32.14%
29.09%
Fill-in-the-Blank
55.56%
38.51%
26.15%
21.53%
Contextual Usage
45.00%
47.22%
51.30%
42.04%
Cultural Interpretation
60.00%
58.79%
52.46%
52.99%
Location Recognition
53.25%
31.00%
30.36%
27.73%
LLaMA
Word
Meaning
25.98%
49.80%
25.49%
13.15%
True/False
27.24%
25.12%
24.93%
13.16%
Fill-in-the-Blank
42.64%
38.67%
27.45%
20.38%
Contextual Usage
43.55%
44.36%
22.98%
18.27%
Cultural Interpretation
41.99%
28.15%
20.12%
13.14%
Location Recognition
66.32%
30.85%
21.87%
20.66%
Phrase
Meaning
42.86%
23.33%
24.88%
16.46%
True/False
29.56%
28.41%
26.60%
14.20%
Fill-in-the-Blank
45.91%
31.11%
27.16%
20.46%
Contextual Usage
38.33%
37.73%
23.43%
18.02%
Cultural Interpretation
40.69%
42.47%
26.00%
16.90%
Location Recognition
63.32%
24.41%
21.79%
20.35%
Proverb
Meaning
30.77%
10.26%
33.33%
15.69%
True/False
32.50%
41.31%
38.33%
21.57%
Fill-in-the-Blank
56.79%
38.82%
28.12%
23.35%
Contextual Usage
40.00%
34.74%
26.56%
16.96%
Cultural Interpretation
46.25%
24.04%
25.81%
17.30%
Location Recognition
54.55%
13.64%
25.00%
17.65%
Jais
Word
Meaning
23.89%
30.87%
25.26%
10.02%
True/False
22.26%
22.82%
24.79%
9.26%
Fill-in-the-Blank
39.57%
35.41%
20.48%
12.29%
Contextual Usage
40.36%
33.62%
25.55%
15.98%
Continued on next page
30

--- Page 31 ---

Model
Content Type
Question Type
Accuracy
Precision
Recall
F1-score
Cultural Interpretation
44.31%
52.65%
27.68%
20.96%
Location Recognition
67.57%
16.91%
24.97%
20.17%
Phrase
Meaning
42.86%
14.29%
33.33%
20.00%
True/False
23.11%
40.92%
33.53%
12.75%
Fill-in-the-Blank
41.59%
51.99%
25.94%
16.68%
Contextual Usage
35.76%
31.09%
20.46%
11.77%
Cultural Interpretation
39.61%
45.27%
25.39%
16.10%
Location Recognition
65.72%
41.48%
25.15%
20.30%
Proverb
Meaning
30.77%
10.26%
33.33%
15.69%
True/False
21.25%
7.08%
33.33%
11.68%
Fill-in-the-Blank
51.85%
12.96%
25.00%
17.07%
Contextual Usage
37.50%
9.38%
25.00%
13.64%
Cultural Interpretation
45.00%
11.25%
25.00%
15.52%
Location Recognition
54.55%
13.64%
25.00%
17.65%
Mistral
Word
Meaning
32.08%
29.91%
26.60%
22.09%
True/False
58.40%
58.15%
59.70%
56.56%
Fill-in-the-Blank
42.97%
10.74%
25.00%
15.03%
Contextual Usage
39.48%
9.87%
25.00%
14.15%
Cultural Interpretation
45.07%
11.27%
25.00%
15.53%
Location Recognition
69.77%
17.44%
25.00%
20.55%
Phrase
Meaning
38.71%
27.44%
26.34%
24.64%
True/False
56.00%
58.28%
59.38%
55.36%
Fill-in-the-Blank
41.38%
35.31%
25.11%
14.82%
Contextual Usage
35.12%
7.04%
20.00%
10.41%
Cultural Interpretation
39.39%
9.85%
25.00%
14.13%
Location Recognition
58.70%
30.77%
46.51%
34.36%
Proverb
Meaning
30.77%
11.11%
33.33%
16.67%
True/False
46.15%
30.00%
33.33%
31.58%
Fill-in-the-Blank
50.62%
12.97%
24.40%
16.94%
Contextual Usage
36.25%
9.18%
24.17%
13.30%
Cultural Interpretation
45.00%
11.25%
25.00%
15.52%
Location Recognition
53.85%
35.42%
35.00%
34.85%
Qwen
Word
Meaning
64.47%
35.52%
37.59%
35.81%
True/False
75.13%
31.78%
30.60%
30.82%
Fill-in-the-Blank
60.51%
47.27%
54.62%
48.08%
Contextual Usage
64.67%
52.41%
54.08%
52.96%
Cultural Interpretation
63.74%
40.79%
44.49%
41.28%
Location Recognition
51.45%
44.65%
56.56%
43.11%
Phrase
Meaning
61.29%
36.27%
37.65%
36.12%
True/False
18.49%
32.23%
31.89%
11.45%
Fill-in-the-Blank
33.33%
25.04%
27.41%
16.58%
Contextual Usage
33.75%
24.97%
16.79%
13.41%
Cultural Interpretation
63.93%
39.62%
46.12%
40.16%
Continued on next page
31

--- Page 32 ---

Model
Content Type
Question Type
Accuracy
Precision
Recall
F1-score
Location Recognition
51.97%
42.94%
51.74%
40.61%
Proverb
Meaning
47.56%
24.38%
12.04%
16.12%
True/False
31.71%
23.13%
33.11%
13.64%
Fill-in-the-Blank
31.71%
20.00%
14.84%
15.69%
Contextual Usage
67.50%
59.91%
59.74%
57.64%
Cultural Interpretation
50.00%
24.40%
12.65%
16.67%
Location Recognition
31.71%
24.07%
8.02%
12.04%
ACEGPT
Word
Meaning
43.80%
26.37%
22.11%
21.07%
True/False
37.22%
19.86%
20.11%
14.96%
Fill-in-the-Blank
41.84%
35.63%
41.09%
33.47%
Contextual Usage
54.53%
47.50%
45.84%
44.14%
Cultural Interpretation
40.23%
33.23%
31.89%
26.85%
Location Recognition
40.28%
36.79%
38.93%
29.34%
Phrase
Meaning
39.47%
23.94%
22.26%
21.26%
True/False
40.48%
27.03%
27.35%
20.72%
Fill-in-the-Blank
36.84%
34.81%
41.95%
29.54%
Contextual Usage
49.12%
48.07%
48.73%
41.73%
Cultural Interpretation
39.29%
35.71%
33.49%
26.63%
Location Recognition
36.95%
34.43%
41.52%
26.72%
Proverb
Meaning
42.31%
44.70%
32.44%
34.03%
True/False
23.81%
41.67%
43.38%
23.64%
Fill-in-the-Blank
28.57%
26.67%
15.56%
19.64%
Contextual Usage
43.24%
50.75%
39.73%
32.26%
Cultural Interpretation
28.26%
49.38%
38.98%
29.33%
Location Recognition
38.67%
30.48%
37.80%
28.22%
32

```
